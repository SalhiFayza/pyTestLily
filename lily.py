from datetime import datetime, date
import os
import random

class Person:
    def __init__(self):
        self.name = ""

    def set_name(self, name):
        self.name = name


person_obj = Person()

def lily_speak(text):
    return text

def get_today_file():
    return datetime.today().strftime('%Y-%m-%d') + ".csv"

def get_last_line(filename):
    if not os.path.exists(filename):
        return None

    with open(filename, "rb") as f:
        try:
            f.seek(-2, os.SEEK_END)
            while f.read(1) != b'\n':
                f.seek(-2, os.SEEK_CUR)
        except OSError:
            f.seek(0)
        return f.readline().decode()

def parse_last_values():
    file = get_today_file()
    line = get_last_line(file)

    if not line:
        return None

    parts = line.strip().split(',')

    try:
        return {
            "humidity": float(parts[2]),
            "temperature": float(parts[3]),
            "water_temp": float(parts[4]),
            "ph": float(parts[5])
        }
    except:
        return None

def get_intent(text):
    if "water_temp" in text:
        return "water_temp"
    elif "temperature" in text:
        return "temperature"
    elif "humidity" in text:
        return "humidity"
    elif "ph" in text:
        return "ph"
    elif "quality" in text or "safe" in text:
        return "quality"
    elif "time" in text:
        return "time"
    elif "date" in text:
        return "date"
    elif "hello" in text or "hi" in text:
        return "greeting"
    elif "my name is" in text:
        return "set_name"
    elif "your name" in text:
        return "ask_name"
    else:
        return "unknown"

def fallback():
    responses = [
        "I didn't understand.",
        "Try asking about temperature or pH.",
        "Can you rephrase?"
    ]
    return random.choice(responses)


def process_message(user_input):
    intent = get_intent(user_input)

    data = parse_last_values()

    if intent == "greeting":
        return f"Hello {person_obj.name or ''}"

    elif intent == "ask_name":
        return "My name is Lily"

    elif intent == "set_name":
        name = user_input.split("is")[-1].strip()
        person_obj.set_name(name)
        return f"I will remember that {name}"

    elif intent == "time":
        return datetime.now().strftime('%I:%M %p')

    elif intent == "date":
        return date.today().strftime('%B %d, %Y')

    elif intent == "temperature":
        return f"Temperature is {data['temperature']} °C" if data else "No data"

    elif intent == "water_temp":
        return f"Water temperature is {data['water_temp']} °C" if data else "No data"

    elif intent == "humidity":
        return f"Humidity is {data['humidity']} %" if data else "No data"

    elif intent == "ph":
        return f"pH is {data['ph']}" if data else "No data"

    elif intent == "quality":
        if not data:
            return "No data"

        ph = data["ph"]
        temp = data["water_temp"]

        msg = ""
        msg += "pH OK. " if 6 <= ph <= 8 else "⚠️ pH not safe. "
        msg += "Temp OK." if 10 <= temp <= 30 else "⚠️ Temp not optimal."
        return msg

    else:
        return fallback()
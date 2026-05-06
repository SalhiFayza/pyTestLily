from lily import get_intent, process_message


def test_greeting_intent():
    assert get_intent("hello") == "greeting"

def test_name_intent():
    assert get_intent("my name is Fizo") == "set_name"

def test_temperature_intent():
    assert get_intent("temperature") == "temperature"



def test_greeting_response():
    result = process_message("hello")
    assert isinstance(result, str)

def test_set_name():
    process_message("my name is Fizo")
    result = process_message("hello")
    assert "Fizo" in result or "Hello" in result

def test_time_response():
    result = process_message("what time is it")
    assert ":" in result



def test_ph_response():
    result = process_message("ph")
    assert "pH" in result

def test_humidity_response():
    result = process_message("humidity")
    assert "%" in result or "Humidity" in result

def test_water_temp_response():
    result = process_message("water_temp")
    assert "Water" in result or "°C" in result


def test_unknown_input():
    result = process_message("asdasdasd")
    assert result is not None

def test_empty_input():
    result = process_message("")
    assert isinstance(result, str)
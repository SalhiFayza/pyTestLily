from playwright.sync_api import sync_playwright

BASE_URL = "http://127.0.0.1:5000"


def test_basic_chat():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(BASE_URL)

        page.fill("#input", "hello")
        page.click("button")

        page.wait_for_timeout(800)

        bot_messages = page.locator(".message.bot .bubble")
        assert bot_messages.count() > 0

        browser.close()


def test_name_memory():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(BASE_URL)

        page.fill("#input", "my name is Alex")
        page.click("button")
        page.wait_for_timeout(500)

        page.fill("#input", "hello")
        page.click("button")
        page.wait_for_timeout(800)

        bot_messages = page.locator(".message.bot .bubble")
        assert bot_messages.count() >= 2

        browser.close()


def test_sensor_queries():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(BASE_URL)

        page.fill("#input", "temperature")
        page.click("button")
        page.wait_for_timeout(500)

        page.fill("#input", "ph")
        page.click("button")
        page.wait_for_timeout(500)

        bot_messages = page.locator(".message.bot .bubble")
        assert bot_messages.count() >= 2

        browser.close()


def test_unknown_input():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(BASE_URL)

        page.fill("#input", "asdasdasd123")
        page.click("button")

        page.wait_for_timeout(800)

        bot_messages = page.locator(".message.bot .bubble")
        assert bot_messages.count() > 0

        browser.close()


def test_full_conversation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(BASE_URL)

        messages = [
            "hello",
            "my name is John",
            "temperature",
            "is water safe?"
        ]

        for msg in messages:
            page.fill("#input", msg)
            page.click("button")
            page.wait_for_timeout(600)

        bot_messages = page.locator(".message.bot .bubble")
        assert bot_messages.count() >= len(messages)

        browser.close()

def test_ui_elements():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(BASE_URL)

        assert page.locator("#input").is_visible()
        assert page.locator("button").is_visible()
        assert page.locator("#messages").is_visible()

        browser.close()
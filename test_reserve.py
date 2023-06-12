import os

from selenium import webdriver
from selenium.webdriver.common.by import By

STUDIO_NAME = os.getenv("STUDIO_NAME") or "Donnersbergerbrücke"
EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]


class TestReserve:
    def setup_method(self, method):
        webdriver_options = webdriver.ChromeOptions()
        webdriver_options.add_argument("--headless")
        self.driver = webdriver.Chrome(webdriver_options)
        self.vars = {}

    def teardown_method(self, method):
        # LOGOUT
        self.driver.find_element(By.CSS_SELECTOR, "div > .button").click()
        print(f"Logged out.")

        self.driver.quit()

    def test_reserve(self):
        self.driver.get("https://slots.elements.com/")
        self.driver.set_window_size(1440, 783)

        # LOGIN
        self.driver.find_element(By.ID, "input_login_email").click()
        self.driver.find_element(By.ID, "input_login_email").send_keys(EMAIL)
        self.driver.find_element(By.ID, "input_login_password").send_keys(PASSWORD)
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > input").click()

        assert self.driver.title == "Kursplan", "login did not succeed"
        print("Logged in.")

        # STUDIO SELECTION
        dropdown = self.driver.find_element(By.ID, "select_studio")
        dropdown.find_element(
            By.XPATH, f"//option[. = 'TIMESLOTS {STUDIO_NAME}']"
        ).click()

        assert (
            self.driver.find_element(By.TAG_NAME, "h2").text
            == f"TIMESLOTS {STUDIO_NAME}"
        ), "error when selecting studio"
        print(f"Selected {STUDIO_NAME}.")

        # RESERVATION
        registration_button = self.driver.find_element(
            By.CSS_SELECTOR, "span > .button"
        )
        assert (
            registration_button.text == "PLATZ RESERVIEREN"
        ), "button does not say reserve"

        registration_button.click()
        print(f"Triggered reservation in {STUDIO_NAME}.")

        assert (
            (
                self.driver.find_element(By.CLASS_NAME, "form-message").text
                == "Anmeldung erfolgreich"
            ),
            "reservation failed",
        )
        print(f"Reservation for {STUDIO_NAME} was acknowledged.")

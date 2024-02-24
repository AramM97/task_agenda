import time
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
# Import Appium UiAutomator2 driver for Android platforms (AppiumOptions)
from appium.options.android import UiAutomator2Options

from logic.task_agenda_home_page import HomePage
from infra.warpper_page import WrapperPage






class TestAppium(unittest.TestCase):

    def setUp(self) -> None:
       self.wrapper = WrapperPage()
       self.driver = self.wrapper.driver_setup()

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_all_events(self) -> None:
        home_page = HomePage(self.driver)
        home_page.open_menu()
        home_page.go_to_all_events()

        # Get the actual text from the page
        actual_title = home_page.check_all_elements_title()

        # Define the expected text
        expected_title = "All events"

        # Assert that the actual text matches the expected text
        self.assertEqual(actual_title, expected_title, f"Expected text: {expected_title}, Actual text: {actual_title}")

    def test_late_events(self) -> None:
        home_page = HomePage(self.driver)
        home_page.open_menu()
        home_page.go_to_late_events()

        # Get the actual text from the page
        actual_title = home_page.check_late_elements_title()

        # Define the expected text
        expected_title = "Late events"

        # Assert that the actual text matches the expected text
        self.assertEqual(actual_title, expected_title,
                         f"Expected text: {expected_title}, Actual text: {actual_title}")

    def test_calendar_view(self) -> None:
        home_page = HomePage(self.driver)
        home_page.go_to_calendar()

    def test_pending_events(self) -> None:
        home_page = HomePage(self.driver)
        home_page.check_pending_events()

    def test_next_week_events(self) -> None:
        home_page = HomePage(self.driver)
        current_week = home_page.check_display_date()
        print(current_week)
        home_page.go_to_next_week()
        new_week = home_page.check_display_date()
        print(new_week)
        self.assertNotEqual(current_week, new_week)


    def test_last_week_events(self) -> None:
        home_page = HomePage(self.driver)
        current_week = home_page.check_display_date()
        print(current_week)
        home_page.go_to_last_week()
        new_week = home_page.check_display_date()
        print(new_week)
        self.assertNotEqual(current_week, new_week)

    def test_go_to_about_section(self) -> None:
        desired_text = 'Developed by Apps CC'
        home_page = HomePage(self.driver)
        descp_text = home_page.check_about()
        self.assertIn(desired_text , descp_text)








if __name__ == '__main__':
    unittest.main()
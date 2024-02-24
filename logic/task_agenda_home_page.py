from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    PLUS_BUTTON = "com.claudivan.taskagenda:id/btNovoEvento"
    CALENDAR_PATH = '//android.widget.LinearLayout[@content-desc="Calendar"]'
    PENDIG_EVENTS_BUTTON = 'com.claudivan.taskagenda:id/btEventosSemana'

    CURRRENT_WEEK_DISPLAY = '//android.widget.TextView[@resource-id="com.claudivan.taskagenda:id/tvVisor"]'

    NEXT_WEEK_TAB = '(//android.widget.ImageView[@content-desc="Image"])[2]'
    LAST_WEEK_TAB = '(//android.widget.ImageView[@content-desc="Image"])[1]'

    HAMBURGER_MENU = '//android.widget.ImageView[@resource-id="com.claudivan.taskagenda:id/hamburguer"]'

    SELECT_TOMORROW = '//android.widget.TextView[@resource-id="android:id/text1" and @text="Tomorrow"]'
    SELECT_TODAY = '//android.widget.TextView[@resource-id="android:id/text1" and @text="Today"]'
    SELECT_OTHER = '//android.widget.TextView[@resource-id="android:id/text1" and @text="Other"]'

    ALL_EVENTS = '//android.widget.TextView[@text="All events"]'
    LATE_EVENTS = '//android.widget.RelativeLayout[@resource-id="com.claudivan.taskagenda:id/btEventosAtrasados"]'

    ALL_EVENTS_TITLE = '//android.widget.TextView[@text="All events"]'
    LATE_EVENTS_TITLE = '// android.widget.TextView[ @ text = "Late events"]'

    ABOUT_PAGE_BUTTON = '//android.widget.LinearLayout[@resource-id="com.claudivan.taskagenda:id/btSobre"]'
    ABOUT_DECREPSOTION = '//android.widget.TextView[@resource-id="com.claudivan.taskagenda:id/tvTexto"]'

    def __init__(self, driver):
        self.driver = driver

        self.plus_button = self.driver.find_element(by=AppiumBy.ID, value=self.PLUS_BUTTON)
        self.hamburger_menu = self.driver.find_element(by=AppiumBy.XPATH, value=self.HAMBURGER_MENU)
        self.pending_events = self.driver.find_element(by=AppiumBy.ID, value=self.PENDIG_EVENTS_BUTTON)
        self.calendar_section = self.driver.find_element(by=AppiumBy.XPATH, value=self.CALENDAR_PATH)
        self.current_week_display = self.driver.find_element(by=AppiumBy.XPATH, value=self.CURRRENT_WEEK_DISPLAY)
        self.next_week_button = self.driver.find_element(by=AppiumBy.XPATH, value=self.NEXT_WEEK_TAB)
        self.last_week_button = self.driver.find_element(by=AppiumBy.XPATH, value=self.LAST_WEEK_TAB)

    def open_menu(self):
        try:
            self.hamburger_menu.click()
        except (StaleElementReferenceException, NoSuchElementException):
            # If the element is stale or not found, try to find it again
            self.hamburger_menu = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, self.HAMBURGER_MENU))
            )
            self.hamburger_menu.click()

    def go_to_all_events(self):
        self.all_events = self.driver.find_element(by=AppiumBy.XPATH, value=self.ALL_EVENTS)
        self.all_events.click()

    def go_to_late_events(self):
        self.late_events = self.driver.find_element(by=AppiumBy.XPATH, value=self.LATE_EVENTS)
        self.late_events.click()


    def check_all_elements_title(self):
        try:
            # Wait up to 10 seconds until the element is present on the page
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, self.ALL_EVENTS_TITLE))
            )

            # Once the element is present, find and return its text
            self.all_events_element = self.driver.find_element(by=AppiumBy.XPATH, value=self.ALL_EVENTS_TITLE)
            self.actual_text = self.all_events_element.text
            return self.actual_text

        except NoSuchElementException:
            # Handle the case where the element is not found even after waiting
            raise NoSuchElementException("Element not found on the screen")


    def check_late_elements_title(self):
        try:
            # Wait up to 10 seconds until the element is present on the page
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, self.LATE_EVENTS_TITLE))
            )

            # Once the element is present, find and return its text
            self.late_events_element = self.driver.find_element(by=AppiumBy.XPATH, value=self.LATE_EVENTS_TITLE)
            self.actual_text = self.late_events_element.text
            return self.actual_text

        except NoSuchElementException:
            # Handle the case where the element is not found even after waiting
            raise NoSuchElementException("Element not found on the screen")

    def go_to_calendar(self):
        self.calendar_section.click()

    def check_pending_events(self):
        self.pending_events.click()

    def go_to_next_week(self):
        self.next_week_button.click()

    def go_to_last_week(self):
        self.last_week_button.click()

    def check_display_date(self):
        try:
            # Wait up to 10 seconds until the element is present on the page
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, self.CURRRENT_WEEK_DISPLAY))
            )

            # Once the element is present, find and return its text
            #self.all_events_element = self.driver.find_element(by=AppiumBy.XPATH, value=self.ALL_EVENTS_TITLE)
            self.week_display_text = self.current_week_display.text
            return self.week_display_text

        except NoSuchElementException:
            # Handle the case where the element is not found even after waiting
            raise NoSuchElementException("Element not found on the screen")

    def get_about_app(self):
        try:
            self.open_menu()

            # Wait up to 10 seconds until the element is present on the page
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, self.ABOUT_PAGE_BUTTON))
            )

            # Once the element is present, find and return its text
            self.about_menu_button = self.driver.find_element(by=AppiumBy.XPATH, value=self.ABOUT_PAGE_BUTTON)
            self.about_menu_button.click()
            return

        except NoSuchElementException:
            # Handle the case where the element is not found even after waiting
            raise NoSuchElementException("Element not found on the screen")

    def get_about_app_desc(self):
        try:

            # Wait up to 10 seconds until the element is present on the page
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, self.ABOUT_DECREPSOTION))
            )

            # Once the element is present, find and return its text
            self.about_descp = self.driver.find_element(by=AppiumBy.XPATH, value=self.ABOUT_DECREPSOTION)
            self.descp_text = self.about_descp.text
            return self.descp_text

        except NoSuchElementException:
            # Handle the case where the element is not found even after waiting
            raise NoSuchElementException("Element not found on the screen")

    def check_about(self):
        self.get_about_app()
        about_decp = self.get_about_app_desc()
        return about_decp

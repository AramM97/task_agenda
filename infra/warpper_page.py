from appium.options.android import UiAutomator2Options
from appium import webdriver


class WrapperPage:
    CAPS = dict(
        platformName="Android",
        deviceName="emulator-5556",
        platformVersion="13.0",
        automationName="UiAutomator2",
        appPackage="com.claudivan.taskagenda",
        appActivity=".Activities.MainActivity"
    )

    URL = 'http://localhost:4723'
    # Converts capabilities to AppiumOptions instance


    def __init__(self):
        self.driver = None


    def driver_setup(self) -> None:
        capabilities_options = UiAutomator2Options().load_capabilities(self.CAPS)
        self.driver = webdriver.Remote(
            command_executor=self.URL,
            options=capabilities_options
        )
        return self.driver

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from tempfile import mkdtemp


class WebDriver:
    def __init__(self):
        options = Options()
        options.binary_location = "/opt/chrome/chrome"

        # Test locally
        # options.add_argument("--window-size=1280x1696")
        # options.add_argument("--no-sandbox")
        # options.add_argument("--disable-gpu")
        # options.add_argument("--disable-extensions")

        # Run tests
        options.add_argument("--window-size=1280x1696")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-dev-tools")
        options.add_argument("--no-zygote")
        options.add_argument(f"--user-data-dir={mkdtemp()}")
        options.add_argument(f"--data-path={mkdtemp()}")
        options.add_argument(f"--disk-cache-dir={mkdtemp()}")
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument("--single-process")
        # This setting is affecting the tests
        # options.add_argument("--headless=new")

        service = webdriver.ChromeService("/opt/chromedriver/chromedriver")

        self.web_driver = webdriver.Chrome(options=options, service=service)

    def get(self, url: str):
        self.web_driver.get(url)

    def frame_to_be_available_and_switch_to_it(self, selector, timeout=10):
        WebDriverWait(self.web_driver, timeout).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, selector))
        )

    def element_to_be_clickable_and_click_it(self, selector, timeout=10):
        WebDriverWait(self.web_driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, selector))
        ).click()

    def switch_to_default_content(self):
        self.web_driver.switch_to.default_content()

    def find_element_by_xpath(self, selector):
        return self.web_driver.find_element(By.XPATH, selector)

    def find_element_by_id(self, selector):
        return self.web_driver.find_element(By.ID, selector)

    def find_elements_by_id(self, selector):
        return self.web_driver.find_elements(By.ID, selector)

    def quit(self):
        self.web_driver.quit()

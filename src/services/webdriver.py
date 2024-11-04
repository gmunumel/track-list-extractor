"""
This module provides a Driver class to initialize a Selenium WebDriver with specific options.
"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC


class WebDriver:
    """
    A class used to initialize a Selenium WebDriver with specific options.
    """

    def __init__(self):
        options = Options()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        # options.add_argument("--headless")
        self.web_driver = webdriver.Chrome(options=options)

    def get(self, url: str):
        """
        Navigate to the specified URL using the web driver.

        Args:
            url (str): The URL to navigate to.
        """
        self.web_driver.get(url)
    
    def frame_to_be_available_and_switch_to_it(self, selector, timeout=10):
        """
        Waits for a frame to be available and switches to it.

        Args:
            selector (str): The XPATH selector of the frame to switch to.
            timeout (int, optional): The maximum number of seconds to wait for the frame to be available. Defaults to 10.

        Raises:
            TimeoutException: If the frame is not available within the specified timeout.
        """
        WebDriverWait(self.web_driver, timeout).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, selector))
        )

    def element_to_be_clickable_and_click_it(self, selector, timeout=10):
        """
        Waits for an element to be clickable and then clicks it.

        Args:
            selector (str): The XPATH selector of the element to be clicked.
            timeout (int, optional): The maximum amount of time to wait for the element to be clickable. Defaults to 10 seconds.

        Raises:
            TimeoutException: If the element is not clickable within the specified timeout.
        """
        WebDriverWait(self.web_driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, selector))
        ).click()

    def switch_to_default_content(self):
        """
        Switches the context to the default content of the web page.

        This method is used to switch the driver's focus back to the main document
        after interacting with an iframe or a frame. It ensures that subsequent
        commands are executed in the context of the main document.
        """
        self.web_driver.switch_to.default_content()

    def find_element_by_xpath(self, selector):
        """
        Finds an element on the web page using the given XPath selector.

        Args:
            selector (str): The XPath selector used to locate the element.

        Returns:
            WebElement: The web element found by the XPath selector.

        Raises:
            NoSuchElementException: If no element is found with the given XPath selector.
        """
        return self.web_driver.find_element(By.XPATH, selector)

    def find_element_by_id(self, selector):
        """
        Finds an element on the web page using the given ID selector.

        Args:
            selector (str): The ID selector used to locate the element.

        Returns:
            WebElement: The web element found by the ID selector.

        Raises:
            NoSuchElementException: If no element is found with the given ID selector.
        """
        return self.web_driver.find_element(By.ID, selector)

    def find_elements_by_id(self, selector):
        """
        Finds multiple elements on the web page using the given ID selector.

        Args:
            selector (str): The ID selector used to locate the elements.

        Returns:
            List[WebElement]: A list of web elements found by the ID selector.
        """
        return self.web_driver.find_elements(By.ID, selector)

    def quit(self):
        """
        Quits the WebDriver and closes all associated windows.
        """
        self.web_driver.quit()

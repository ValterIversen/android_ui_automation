import uiautomator2 as u2
from robot.api.deco import keyword

class AndroidUiAutomation:
    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    """
    AndroidUiLibrary

    A Python library for automating Android devices using uiautomator2.
    Provides functionalities for device management, app control, UI element interaction,
    text input, and key/button actions.
    """

    def __init__(self):
        """
        Initializes the library without connecting to any device yet.
        Use connect_device() to establish a connection.
        """
        self.d = None
        
    # Device ---------------------------------------------------

    def connect_device(self, device_id="emulator-5554"):
        """
        Connects to an Android device or emulator.

        Args:
            device_id (str): The device ID or emulator name. Default is "emulator-5554".
        
        Raises:
            Exception: If unable to connect to the device.
        """
        self.d = u2.connect(device_id)
        if not self.d.info:
            raise Exception("Unable to connect to device.")
        print("Connected to device:", self.d.device_info)

    def open_app(self, package_name):
        """
        Launches an app on the connected device.

        Args:
            package_name (str): The package name of the app to start.

        Raises:
            Exception: If device is not connected.
        """
        if not self.d:
            raise Exception("Device not connected.")
        self.d.app_start(package_name)
        print(f"App {package_name} started.")

    def close_app(self, package_name):
        """
        Stops an app on the connected device.

        Args:
            package_name (str): The package name of the app to stop.

        Raises:
            Exception: If device is not connected.
        """
        if not self.d:
            raise Exception("Device not connected.")
        self.d.app_stop(package_name)
        print(f"App {package_name} closed.")
        
    # Check visibility or invisibility ---------------------------
        
    def wait_until_text_appears(self, texto, timeout=10):
        """
        Waits until an element with the specified text is visible.

        Args:
            texto (str): Text of the element to wait for.
            timeout (int): Maximum seconds to wait. Default is 10.

        Raises:
            Exception: If the element is not found within the timeout.
        """
        if not self.d(text=texto).wait(timeout=timeout):
            raise Exception(f"Element with text '{texto}' not found after {timeout} seconds.")
        
    def wait_until_text_disappears(self, texto, timeout=10):
        """
        Waits until an element with the specified text disappears.

        Args:
            texto (str): Text of the element to wait to disappear.
            timeout (int): Maximum seconds to wait. Default is 10.

        Raises:
            Exception: If the element remains visible after the timeout.
        """
        if not self.d(text=texto).wait_gone(timeout=timeout):
            raise Exception(f"Element with text '{texto}' still visible even after {timeout} seconds.")
        
    def wait_until_element_appears(self, selector, timeout=10):
        """
        Waits until an element located via XPath is visible.

        Args:
            selector (str): XPath string starting with '//'.
            timeout (int): Maximum seconds to wait. Default is 10.

        Returns:
            uiautomator2.Element: The found element.

        Raises:
            TypeError: If selector is not a string.
            Exception: If element does not appear within the timeout.
        """
        element = self.d.xpath(selector)

        if not element.wait(timeout=timeout):
            raise Exception(f"Element with selector '{selector}' not found after {timeout} seconds.")
        return element
        
    def wait_until_element_disappears(self, selector, timeout=10):
        """
        Waits until an element located via XPath disappears.

        Args:
            selector (str): XPath string starting with '//'.
            timeout (int): Maximum seconds to wait. Default is 10.

        Returns:
            uiautomator2.Element: The element (after it disappears).

        Raises:
            TypeError: If selector is not a string.
            Exception: If element remains visible after the timeout.
        """
        element = self.d.xpath(selector)

        if not element.wait_gone(timeout=timeout):
            raise Exception(f"Element with selector '{selector}' still visible even after {timeout} seconds.")
        return element
    
    # Tap ---------------------------------------------------
    
    def tap_element(self, selector, timeout=10):
        """
        Waits for an element (XPath) and taps it.

        Args:
            selector (str): XPath string.
            timeout (int): Maximum seconds to wait. Default is 10.

        Raises:
            TypeError: If selector is not a string.
            Exception: If element does not appear within the timeout.
        """
        element = self.d.xpath(selector)    

        if not element.wait(timeout=timeout):
            raise Exception(f"Element with selector '{selector}' not found after {timeout} seconds.")
        element.click()
    
    def tap_by_text(self, texto, timeout=10):
        """
        Waits for an element with the specified text and taps it.

        Args:
            texto (str): Text of the element.
            timeout (int): Maximum seconds to wait. Default is 10.

        Raises:
            Exception: If element is not found within the timeout.
        """
        if not self.d(text=texto).wait(timeout=timeout):
            raise Exception(f"Element with text '{texto}' not found after {timeout} seconds.")
        self.d(text=texto).click()
        
    # Get ---------------------------------------------------
        
    def get_text(self, selector, timeout=10):
        """
        Retrieves the text of an element located via XPath.

        Args:
            selector (str): XPath string.
            timeout (int): Maximum seconds to wait. Default is 10.

        Returns:
            str: Text of the element.

        Raises:
            TypeError: If selector is not a string.
            Exception: If element is not found within the timeout.
        """
        element = self.d.xpath(selector)

        if not element.wait(timeout=timeout):
            raise Exception(f"Element with selector '{selector}' not found after {timeout} seconds.")
        return element.get_text()
        
    # Set ---------------------------------------------------
    
    def input_text(self, selector, text, timeout=10):
        """
        Sets text into an input element located via XPath.

        Args:
            selector (str): XPath string.
            text (str): Text to input.
            timeout (int): Maximum seconds to wait. Default is 10.

        Raises:
            TypeError: If selector is not a string.
            Exception: If element is not found within the timeout.
        """
        element = self.d.xpath(selector)

        if not element.wait(timeout=timeout):
            raise Exception(f"Element with selector '{selector}' not found after {timeout} seconds.")
        
        return element.set_text(text)
    
    # Keyboard / Key Actions ---------------------------------------------------
    
    def type_keys(self, keys, timeout=5):
        """
        Types a sequence of letters or numbers using d.press().

        Args:
            keys (str): Sequence of characters to type. Example: "INPUT".
            timeout (int): Optional timeout for each key press (currently unused).
        """
        for char in keys:
            self.d.press(char.lower())

    @keyword("Press Home Button")
    def press_home(self):
        """
        Presses the Android Home button.
        """
        self.d.press("home")

    @keyword("Press Back Button")
    def press_back(self):
        """
        Presses the Android Back button.
        """
        self.d.press("back")

    @keyword("Press Menu Button")
    def press_menu(self):
        """
        Presses the Android Menu button.
        """
        self.d.press("menu")

# android_ui_automation/__init__.py

from .android_ui_library import AndroidUiAutomation
from robot.api.deco import keyword

class AndroidUiAutomationLibrary(AndroidUiAutomation):
    """
    Robot Framework library wrapper for AndroidUiAutomation.
    All public methods of AndroidUiAutomation are exposed as keywords.
    """
    ROBOT_LIBRARY_SCOPE = "GLOBAL" 

    # Aliases ---
    @keyword("Press Home Button")
    def press_home_button(self):
        self.press_home()

    @keyword("Press Back Button")
    def press_back_button(self):
        self.press_back()

    @keyword("Press Menu Button")
    def press_menu_button(self):
        self.press_menu()
    
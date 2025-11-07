# android_ui_automation

Python library for Android UI automation using uiautomator2, compatible with Robot Framework.

## Installation

You can install the library via pip:

```bash
pip install robotframework-androiduiautomation
```
Or install locally for development:

```bash
git clone https://github.com/ValterIversen/android_ui_automation
cd robotframework-androiduiautomation
pip install -e .
```

Make sure `uiautomator2` is installed automatically as a dependency.

## Usage in Robot Framework

### Settings

```robot
*** Settings ***
Library    AndroidUiAutomation
```

### Variables

```robot
*** Variables ***
${DEVICE}    emulator-5554
${APP}       com.example.app
```

### Test Case Example

```robot
*** Test Cases ***
Open App And Click Button
    [Documentation]    Example test to open an app, click a button, type keys, and use system buttons
    Connect Device    ${DEVICE}
    Open App    ${APP}
    Type Keys    INPUT
    Click By Text    Confirm
    Press Back Button
    Close App    ${APP}
```

### Features

* Connect to Android devices/emulators
* Launch and close apps
* Wait for elements (text, XPath, UiSelector) to appear/disappear
* Click elements by text, XPath, or UiSelector
* Get and set text
* Press keys or system buttons (Home, Back, Menu)
* Fully compatible with Robot Framework keywords

### Notes

* All Python public methods are automatically available as Robot Framework keywords.
* Some system buttons have friendlier aliases: `Press Home Button`, `Press Back Button`, `Press Menu Button`.
* Set `ROBOT_LIBRARY_SCOPE = GLOBAL` to maintain device connection across multiple tests.

# android_ui_automation

Python library for Android UI automation using **uiautomator2**, fully compatible with **Robot Framework**.

## Installation

Install from PyPI:

```bash
pip install robotframework-androiduiautomation
```

Or install locally for development:

```bash
git clone https://github.com/ValterIversen/android_ui_automation
cd android_ui_automation
pip install -e .
```

`uiautomator2` will be installed automatically as a dependency.

---

## Usage in Robot Framework

### ***Settings***

```robot
*** Settings ***
Library    AndroidUiAutomation
```

### ***Variables***

```robot
*** Variables ***
${DEVICE}    emulator-5554
${APP}       com.example.app
```

### ***Test Case Example***

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

---

## Features

- Connect to Android devices/emulators  
- Launch and close apps  
- Wait for elements (Text or XPath) to appear/disappear  
- Click by text or XPath  
- Get and set text  
- Type keys  
- Press Android system buttons (Home, Back, Menu)  
- Fully compatible with Robot Framework keyword-style usage  
- All public Python methods automatically become RF keywords  

---

## Notes

- System buttons have friendly aliases:  
  - `Press Home Button`  
  - `Press Back Button`  
  - `Press Menu Button`  

---

# Example Project (Base Template)

To see a **complete working example** using this library, check out the base project:

**https://github.com/ValterIversen/RobotFramework-UiAutomatorLibrary**

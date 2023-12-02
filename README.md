# Ajax Systems Application Tests Task 
**Automated UI Testing** of Android app using **[Appium](https://appium.io/)** (**[Appium Python Client](Appium Python Client)**) and **[pytest](https://github.com/pytest-dev/pytest)**.
### How to run
1. Go through the next Appium guides to set up Appium server and driver for Android:
 [Install Appium](https://appium.io/docs/en/2.0/quickstart/install/) and [Install the UiAutomator2 Driver](https://appium.io/docs/en/2.0/quickstart/uiauto2-driver/).
2. [Install Python ](https://www.python.org/downloads/release/python-380/) (version>=3.8) if needed
3. Install required packages with
`pip install -r requirements.txt` command
4. Rename .env.example and add there valid credentials for Ajax App.
5. Prepare your [real Android device](https://developer.android.com/tools/adb#Enabling) or [emulator](https://developer.android.com/studio/run/emulator).
6. Run with `pytest` command.

#### Tasks
1) - [x] Implement base functional to work with app (done via page model)
2) - [x] Write user login test (with positive and negative cases).
3) - [x] Use parametrization.
4) - [x] Commit to GitHub,

#### Additional tasks
- [x] *Test logging.
- [x] *Dynamic udid identification using subprocess.
- [x] **Test for SideBar elements.


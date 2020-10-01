# End-to-End Testing (with selenium and python)

## Requirements (Develompment Tools)

This App was devepled with the following dev tools:
- Python 3.8.0

## NOTE: The first step, Clone the repo if you have not. :innocent:

### :warning: PreSetup (Required) 
1. create python virtual environment `python_venv` and activate it, navigate to root directory, run following command from the root directory.
```
cd tests/
python3 -m venv python_venv
source python_venv/bin/activate
pip install -r requirements.txt
```
if you want to deactivate `python_venv`. run following command for that.
```
deactivate
```

2. Download chromedriver for e2e test run script based on your Operating System (OS). (fyi: the repo has chromedriver for MacOS)
  - (if needs) Here is some References to resolve errors related to chromedriver :innocent:
     - https://www.businessinsider.com/what-version-of-google-chrome-do-i-have
     - https://sites.google.com/a/chromium.org/chromedriver/downloads
     - https://stackoverflow.com/questions/8255929/running-selenium-webdriver-python-bindings-in-chrome

### Run E2E testing Script
Navigate to root directory and run following commands:
```
cd tests/
source python_venv/bin/activate
python3 e2e_test_run.py
```
If you see `e2e Test Pass` print on console then it's Done! :tada:


Ref Doc for Selenium - Python: https://selenium-python.readthedocs.io/getting-started.html

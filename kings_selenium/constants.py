import json
import os

POLL_FREQUENCY = 0.5
CHROME_DEBUGGER_ADDRESS = ""
DRIVER_LOCATION = ""
COMMAND_EXECUTOR = "127.0.0.1:9222"
DESIRED_CAPABILITIES = {}
TIMEOUT = 30


def init():
    file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.json'
    with open(file_path, 'r', encoding='utf8')as fp:
        json_data = json.load(fp)
        global POLL_FREQUENCY
        global CHROME_DEBUGGER_ADDRESS
        global DRIVER_LOCATION
        global COMMAND_EXECUTOR
        global DESIRED_CAPABILITIES
        global TIMEOUT

        """          公共          """
        POLL_FREQUENCY = json_data.get("POLL_FREQUENCY", 0.5)
        TIMEOUT = json_data.get("TIMEOUT", 30)

        """          web          """
        CHROME_DEBUGGER_ADDRESS = json_data.get("CHROME_DEBUGGER_ADDRESS", "127.0.0.1:9222")
        DRIVER_LOCATION = json_data.get("DRIVER_LOCATION")

        # phone
        COMMAND_EXECUTOR = json_data.get("COMMAND_EXECUTOR", "http://127.0.0.1:4723/wd/hub")
        DESIRED_CAPABILITIES = json_data.get("DESIRED_CAPABILITIES")


init()

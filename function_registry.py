import os
import webbrowser
import psutil

def open_chrome():
    webbrowser.open("https://www.google.com")

def open_calculator():
    os.system("calc")

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)


# print("CPU Usage:", get_cpu_usage(), "%")

function_bank = {
    "open_chrome": {
        "function": open_chrome,
        "description": "Open/Start Google Chrome browser",
        "code": """
                   import webbrowser
                   def open_chrome():
                   webbrowser.open('https://www.google.com')"""
    },

    "open_calculator": {
        "function": open_calculator,
        "description": "Open/Start/Launch the system calculator application",
        "code": """def open_calculator():
                   import os
                   os.system('calc')"""
    },

    "get_cpu_usage": {
        "function": get_cpu_usage,
        "description": "Get/Retrieve/Check/Show CPU usage of the system",
        "code": """def get_cpu_usage():
                   import psutil
                   return psutil.cpu_percent(interval=1)"""
    }
}

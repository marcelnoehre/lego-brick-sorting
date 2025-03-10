# Lego Brick Sorting

## Installing Dependencies on Raspberry Pi
This guide outlines how to set up a Python environment and install dependencies from a `requirements.txt` file.

### 1) Update System and Install Dependencies
First, update your system to ensure everything is up to date:

```bash
sudo apt update && sudo apt upgrade -y
```

Next, install Python, pip, and required build tools:

```bash
sudo apt install -y python3 python3-pip python3-venv python3-dev libffi-dev libssl-dev build-essential
```

### 2) Check Python and Pip Versions
Verify that Python and pip are installed:

```bash
python3 --version
pip3 --version
```

### 3) Create a Virtual Environment
Create a virtual environment for your project to avoid conflicts with system-wide packages.

Create a new virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Your prompt should change to indicate that you are now working inside the virtual environment.

### 4) Install Dependencies from requirements.txt
With the virtual environment active, install the necessary dependencies:

```bash
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

### 5) Verify the Installation
To confirm that the dependencies are installed, you can check the installed packages:

```bash
pip3 list
```

### 6) Deactivate the Virtual Environment
When you’re done, deactivate the virtual environment:

```bash
deactivate
```

## Hardware Requirements
Before running the project, ensure the following hardware components are properly connected to the Raspberry Pi:

- **Raspberry Pi Camera**: Ensure the camera is connected and enabled.
- **Relay (16 Channels)**: Connect the relay board to the Raspberry Pi's GPIO pins for valve control. Make sure to connect the 5V and GND pins as well.
- **Motor Driver (optional)**: If you're using a motor driver for vibratory plate control, connect it to the Raspberry Pi's GPIO pins. Make sure to connect the GND pins as well.
- **Optocoupler (optional)**: If you're using an optocoupler for handling light barrier events, connect it to Raspberry Pi's GPIO pin. Make sure to connect the 5V and GND as well.  

### Configuration
The GPIO pin IDs for the above components can be configured in the file:

- **`config/hardware_config.py`**

In this file, you can set the specific GPIO pin IDs used for the **Raspberry Pi Camera**, **Relay**, and **Vibration Plate with Light Barrier**. You can also adjust additional settings for the camera, light barrier, and valves within this file.

If a **vibration plate** is available, you can enable it by adjusting the flag in:

- **`config/flags.py`**

### Example Configuration
Here is an example of how the configuration could look:

Example: ```hardware_config.py```

```python
import numpy as np

CAMERA_MODULE = {
    "resolution": (400, 400),
    "badge": {
        "top_left": (350, 0),
        "bottom_right": (400, 50)
    },
    "color_ranges": {
        "red": (np.array([0, 120, 70]), np.array([10, 255, 255])),
        "blue": (np.array([100, 150, 70]), np.array([130, 255, 255])),
        "green": (np.array([40, 70, 70]), np.array([80, 255, 255])),
        "yellow": (np.array([22, 150, 100]), np.array([30, 255, 255])),
        "orange": (np.array([10, 150, 100]), np.array([20, 255, 255])),
        "lime": (np.array([35, 50, 70]), np.array([50, 255, 255])),
        "light_blue": (np.array([90, 100, 100]), np.array([100, 255, 255])),
        "white": (np.array([0, 0, 200]), np.array([180, 50, 255])),
        "brown": (np.array([10, 50, 20]), np.array([18, 255, 100])),
        "beige": (np.array([12, 40, 150]), np.array([20, 100, 255])),
        "grey": (np.array([0, 0, 50]), np.array([180, 10, 180])),
        "purple": (np.array([140, 100, 50]), np.array([160, 255, 255])),
        "pink": (np.array([160, 100, 100]), np.array([175, 255, 255]))
    },
    "color_map": {
        "red": (0, 0, 255),
        "blue": (255, 0, 0),
        "green": (0, 255, 0),
        "yellow": (0, 255, 255),
        "orange": (0, 165, 255),
        "lime": (144, 238, 144),
        "light_blue": (173, 216, 230),
        "white": (255, 255, 255),
        "brown": (42, 42, 165),
        "beige": (245, 245, 220),
        "grey": (128, 128, 128),
        "purple": (128, 0, 128),
        "pink": (255, 105, 180)
    }
}

VALVES = {
    "open_duration": 0.25,
    "amount": 16,
    "valves": {
        1: { "pin": 2, "duration": 10, "color": "red" },
        2: { "pin": 3, "duration": 20, "color": "blue" },
        3: { "pin": 4, "duration": 30, "color": "green" },
        4: { "pin": 14, "duration": 40, "color": "yellow" },
        5: { "pin": 15, "duration": 50, "color": "orange" },
        6: { "pin": 17, "duration": 60, "color": "lime" },
        7: { "pin": 18, "duration": 70, "color": "light_blue" },
        8: { "pin": 27, "duration": 80, "color": "white" },
        9: { "pin": 22, "duration": 90, "color": "brown" },
        10: { "pin": 23, "duration": 100, "color": "beige" },
        11: { "pin": 24, "duration": 110, "color": "grey" },
        12: { "pin": 10, "duration": 120, "color": "purple" },
        13: { "pin": 9, "duration": 130, "color": "pink" },
        14: { "pin": 25, "duration": 140, "color": "" },
        15: { "pin": 11, "duration": 150, "color": "" },
        16: { "pin": 8, "duration": 160, "color": "" },
    }
}

LIGHT_BARRIER = {
    "pin": 7,
    "bounce_time": 200
}

VIBRATORY_PLATE = {
    "motor_a": {
        "in_1": 12,
        "in_2": 16
    },
    "motor_b": {
        "in_3": 20,
        "in_4": 21
    }
}
```

## How to Run the Machine
Run the main script by executing the following command:

```bash
python3 main.py
```

Once the program is running, you'll be presented with the available commands.
* **start** - Starts the sorting machine
* **stop** - Stops the sorting machine
* **quit** - Quits the program

> [!WARNING]  
> Please ensure that all hardware components are properly set up and connected before running the program. Improper connections may result in malfunction or damage to the components.

## How to Run Isolated Tests
Run the test script by executing the following command:

```bash
python3 test.py
```

Once the program is running, you'll be presented with the available commands.
* **0** - Quit testing
* **1** - Activate user defined valve
* **2** - Get the color of the current brick
* **3** - Run the vibratory plate for 5 seconds
* **4** - Await trigger of the light barrier
* **5** - Run vibratory plate until brick is detected

> [!WARNING]  
> Please ensure that all required hardware components are properly set up and connected before running the program. Improper connections may result in malfunction or damage to the components.
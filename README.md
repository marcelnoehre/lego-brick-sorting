# Lego Brick Sorting
The Lego Brick Sorting Machine is designed to automate the sorting of Lego bricks into 16 distinct colors. This system simplifies the organization of large Lego collections, making it easier to find and separate bricks by color. Optionally, a vibratory plate can be added to improve the separation of bricks before sorting.

## Table of Contents
- [Installing Dependencies on Raspberry Pi](#installing-dependencies-on-raspberry-pi)
- [Hardware Requirements](#hardware-requirements)
- [How to Run the Machine](#how-to-run-the-machine)
- [How to Run Isolated Tests](#how-to-run-isolated-tests)
- [Contributing](#contributing)

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
        "width": 50,
        "height": 25,
        "timer": 2
    },
    "target_line": 350,
    "padding": 25,
    "threshold": {
        "contour": 1000,
        "tracking": 100,
        "frequency": 0.5
    },
    "color_ranges": {
        "red": (np.array([0, 120, 70]), np.array([5, 255, 255])),
        "blue": (np.array([111, 150, 140]), np.array([129, 255, 255])),
        "green": (np.array([40, 70, 70]), np.array([80, 255, 255])),
        "yellow": (np.array([22, 150, 100]), np.array([30, 255, 255])),
        "orange": (np.array([10, 150, 100]), np.array([20, 255, 255])),
        "lime": (np.array([35, 50, 70]), np.array([50, 255, 255])),
        "white": (np.array([0, 0, 210]), np.array([180, 40, 255])),
        "light_blue": (np.array([90, 100, 100]), np.array([110, 255, 255])),
        "brown": (np.array([6, 100, 20]), np.array([18, 255, 90])),
        "sand": (np.array([10, 40, 130]), np.array([30, 180, 200])),
        "grey": (np.array([0, 0, 90]), np.array([180, 30, 170])),
        "violett": (np.array([130, 220, 100]), np.array([150, 255, 145])),
        "rosa": (np.array([150, 60, 180]), np.array([160, 120, 220])),
        "pink": (np.array([150, 180, 180]), np.array([163, 215, 220])),
        "magenta": (np.array([160, 216, 80]), np.array([170, 255, 170])),
        "lavendel": (np.array([120, 30, 180]), np.array([140, 110, 240]))
    },
    "color_map": {
        "red": (0, 0, 255),
        "blue": (255, 0, 0),
        "green": (0, 200, 0),
        "yellow": (0, 255, 255),
        "orange": (0, 165, 255),
        "lime": (69, 217, 191),
        "white": (255, 255, 255),
        "light_blue": (222, 184, 135),
        "brown": (15, 30, 100),
        "sand": (135, 206, 235),
        "grey": (128, 128, 128),
        "violett": (128, 0, 126),
        "rosa": (203, 192, 255),
        "pink": (147, 20, 255),
        "magenta": (90, 0, 139),
        "lavendel": (200, 162, 200)
    }
}

VALVES = {
    "open_duration": 0.25,
    "amount": 16,
    "valves": {
        1: { "pin": 2, "duration": 4.3, "color": "red" },
        2: { "pin": 3, "duration": 6.9, "color": "blue" },
        3: { "pin": 4, "duration": 9.3, "color": "green" },
        4: { "pin": 14, "duration": 11.8, "color": "yellow" },
        5: { "pin": 15, "duration": 14.3, "color": "orange" },
        6: { "pin": 17, "duration": 16.7, "color": "lime" },
        7: { "pin": 18, "duration": 19.2, "color": "white" },
        8: { "pin": 27, "duration": 21.3, "color": "light_blue" },
        9: { "pin": 22, "duration": 4.5, "color": "brown" },
        10: { "pin": 23, "duration": 6.9, "color": "sand" },
        11: { "pin": 24, "duration": 9.4, "color": "grey" },
        12: { "pin": 10, "duration": 11.9, "color": "violett" },
        13: { "pin": 9, "duration": 14.4, "color": "rosa" },
        14: { "pin": 25, "duration": 16.9, "color": "pink" },
        15: { "pin": 11, "duration": 19.4, "color": "magenta" },
        16: { "pin": 8, "duration": 21.3, "color": "lavendel" }
    }
}

LIGHT_BARRIER = {
    "pin": 7,
    "bounce_time": 100
}

VIBRATORY_PLATE = {
    "timeout": 2,
    "motor": {
        "in_1": 12,
        "in_2": 16,
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

If the `vibratory_plate` flag is set to true, the light barrier will be triggered.
In this case, you need to run the script with sudo to ensure access to the required GPIO pin:

```bash
sudo python3 main.py
```

Once the program is running, you'll be presented with the available commands.
* **start** - Starts the sorting machine
* **stop** - Stops the sorting machine
* **quit** - Quits the program

> [!WARNING]  
> Please ensure that all hardware components are properly set up and connected before running the program. Improper connections may result in malfunction or damage to the components.

## Contributing

Feel free to fork the project and modify the logic to suit your needs. A formatter script is included to help maintain consistent code formatting across the project. You can run it with the following command:

```bash
sh formatter.sh
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

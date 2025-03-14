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
        "tracking": 100
    },
    "color_ranges": {
        "red": (np.array([0, 120, 70]), np.array([6, 255, 255])),
        "blue": (np.array([111, 150, 70]), np.array([150, 255, 255])),
        "green": (np.array([40, 70, 70]), np.array([80, 255, 255])),
        "yellow": (np.array([22, 150, 100]), np.array([30, 255, 255])),
        "orange": (np.array([10, 150, 100]), np.array([20, 255, 255])),
        "lime": (np.array([35, 50, 70]), np.array([50, 255, 255])),
        "white": (np.array([0, 0, 210]), np.array([180, 40, 255])),
        "light_blue": (np.array([90, 100, 100]), np.array([110, 255, 255])),
        "brown": (np.array([7, 100, 20]), np.array([18, 255, 90])),
        "sand": (np.array([10, 40, 130]), np.array([30, 180, 200])),
        "light_grey": (np.array([0, 0, 100]), np.array([180, 30, 160])),
        "dark_grey": (np.array([0, 0, 50]), np.array([180, 30, 90]))
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
        "brown": (20, 40, 120),
        "sand": (135, 206, 235),
        "light_grey": (128, 128, 128),
        "dark_grey": (105, 105, 105)
    }
}

VALVES = {
    "open_duration": 0.25,
    "amount": 16,
    "valves": {
        1: { "pin": 2, "duration": 6.5, "color": "red" },
        2: { "pin": 3, "duration": 6.5, "color": "blue" },
        3: { "pin": 4, "duration": 9, "color": "green" },
        4: { "pin": 14, "duration": 9, "color": "yellow" },
        5: { "pin": 15, "duration": 11.5, "color": "orange" },
        6: { "pin": 17, "duration": 11.5, "color": "lime" },
        7: { "pin": 18, "duration": 14, "color": "white" },
        8: { "pin": 27, "duration": 14, "color": "light_blue" },
        9: { "pin": 22, "duration": 16.5, "color": "brown" },
        10: { "pin": 23, "duration": 16.5, "color": "sand" },
        11: { "pin": 24, "duration": 19, "color": "light_grey" },
        12: { "pin": 10, "duration": 19, "color": "dark_grey" },
        13: { "pin": 9, "duration": 21.5, "color": "" },
        14: { "pin": 25, "duration": 21.5, "color": "" },
        15: { "pin": 11, "duration": 24, "color": "" },
        16: { "pin": 8, "duration": 24, "color": "" }
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

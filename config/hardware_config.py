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
        "pruple": (128, 0, 128),
        "pink": (255, 105, 180)
    }
}

VALVES = {
    "open_duration": 0.25,
    1: { "pin": 3, "duration": 10 },
    2: { "pin": 5, "duration": 20 },
    3: { "pin": 7, "duration": 30 },
    4: { "pin": 8, "duration": 40 },
    5: { "pin": 10, "duration": 50 },
    6: { "pin": 11, "duration": 60 },
    7: { "pin": 12, "duration": 70 },
    8: { "pin": 13, "duration": 80 },
    9: { "pin": 15, "duration": 90 },
    10: { "pin": 16, "duration": 100 },
    11: { "pin": 18, "duration": 110 },
    12: { "pin": 19, "duration": 120 },
    13: { "pin": 21, "duration": 130 },
    14: { "pin": 22, "duration": 140 },
    15: { "pin": 23, "duration": 150 },
    16: { "pin": 24, "duration": 160 }
}

LIGHT_BARRIER = {
    "pin": 26,
    "bounce_time": 200
}

VIBRATORY_PLATE = {
    "motor_a": {
        "in_1": 32,
        "in_2": 36
    },
    "motor_b": {
        "in_1": 38,
        "in_2": 40
    }
}

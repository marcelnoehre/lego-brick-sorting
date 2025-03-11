import numpy as np

CAMERA_MODULE = {
    "resolution": (400, 400),
    "badge": {
        "top_left": (350, 0),
        "bottom_right": (400, 50)
    },
    "color_ranges": {
        "red": (np.array([0, 120, 70]), np.array([4, 255, 255])),
        "blue": (np.array([105, 150, 70]), np.array([150, 255, 255])),
        "green": (np.array([40, 70, 70]), np.array([80, 255, 255])),
        "yellow": (np.array([22, 150, 100]), np.array([30, 255, 255])),
        "orange": (np.array([10, 150, 100]), np.array([20, 255, 255])),
        "lime": (np.array([35, 50, 70]), np.array([50, 255, 255])),
        "white": (np.array([0, 0, 220]), np.array([180, 30, 255])),
        "light_blue": (np.array([90, 150, 100]), np.array([104, 255, 255])),
        "brown": (np.array([5, 100, 20]), np.array([18, 255, 90])),
        "beige": (np.array([12, 50, 150]), np.array([22, 120, 255])),
        "light_grey": (np.array([0, 0, 100]), np.array([180, 30, 160])),
        "dark_grey": (np.array([0, 0, 50]), np.array([180, 30, 90]))
    },
    "color_map": {
        "red": (0, 0, 255),
        "blue": (255, 0, 0),
        "green": (0, 255, 0),
        "yellow": (0, 255, 255),
        "orange": (0, 165, 255),
        "lime": (144, 238, 144),
        "white": (255, 255, 255),
        "light_blue": (173, 216, 230),
        "brown": (42, 42, 165),
        "beige": (245, 245, 220),
        "light_grey": (128, 128, 128),
        "dark_grey": (105, 105, 105)
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
        7: { "pin": 18, "duration": 70, "color": "white" },
        8: { "pin": 27, "duration": 80, "color": "light_grey" },
        9: { "pin": 22, "duration": 90, "color": "dark_grey" },
        10: { "pin": 23, "duration": 100, "color": "" },
        11: { "pin": 24, "duration": 110, "color": "" },
        12: { "pin": 10, "duration": 120, "color": "" },
        13: { "pin": 9, "duration": 130, "color": "" },
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

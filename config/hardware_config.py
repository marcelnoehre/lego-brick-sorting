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
        11: { "pin": 24, "duration": 19, "color": "grey" },
        12: { "pin": 10, "duration": 19, "color": "violett" },
        13: { "pin": 9, "duration": 21.5, "color": "rosa" },
        14: { "pin": 25, "duration": 21.5, "color": "pink" },
        15: { "pin": 11, "duration": 24, "color": "magenta" },
        16: { "pin": 8, "duration": 24, "color": "lavendel" }
    }
}

LIGHT_BARRIER = {
    "pin": 7,
    "bounce_time": 200
}

VIBRATORY_PLATE = {
    "timeout": 2,
    "motor_a": {
        "in_1": 12,
        "in_2": 16
    },
    "motor_b": {
        "in_3": 20,
        "in_4": 21
    }
}

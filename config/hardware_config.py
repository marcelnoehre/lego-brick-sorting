CAMERA_MODULE = {
    "resolution": (480, 480),
    "color_ranges": {
        "red": [(0, 100, 100), (10, 255, 255)],
        "orange": [(11, 100, 100), (25, 255, 255)],
        "yellow": [(26, 100, 100), (35, 255, 255)],
        "green": [(36, 100, 100), (85, 255, 255)],
        "cyan": [(86, 100, 100), (95, 255, 255)],
        "blue": [(96, 100, 100), (125, 255, 255)],
        "purple": [(126, 100, 100), (145, 255, 255)],
        "pink": [(146, 100, 100), (165, 255, 255)],
        "brown": [(10, 50, 50), (20, 200, 150)],
        "gray": [(0, 0, 50), (180, 50, 200)],
        "white": [(0, 0, 200), (180, 50, 255)],
        "black": [(0, 0, 0), (180, 50, 50)],
        "dark_red": [(0, 100, 50), (10, 255, 99)],
        "light_green": [(36, 50, 100), (85, 255, 200)],
        "dark_blue": [(96, 100, 50), (125, 255, 99)],
        "light_yellow": [(26, 50, 200), (35, 255, 255)]
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

RASPBERRY_PI_CONFIG = {
    "led_pin": -1,
    "color_box_light_barrier_pin": -1,
    "valve_init_light_barrier_pin": -1,
    "vibratory_plate_light_barrier_pin": -1,
}
# TODO: Add remaining hardware configuration values
# TODO: Add the missing configuration values

TIME = {
    "tick": 0.1,
    "light_barrier_interval": 0.1,
    "valve_open_duration": 0.25,
}

COLOR_SENSOR = {
    "i2c_bus": 1,
    "i2c_address": 0x39,
    "integration_time": 0x00,
    "red_channel": 0x08,
    "green_channel": 0x09,
    "blue_channel": 0x0A,
    "ensure_power": 0x03
}

CAMERA_MODULE = {
    "resolution": (640, 480),
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

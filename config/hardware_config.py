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
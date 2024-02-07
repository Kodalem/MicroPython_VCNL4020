# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_vcnl4020 import vcnl4020

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
vcn = vcnl4020.VCNL4020(i2c)

vcn.ambient_light_average = vcnl4020.AL_AVERAGE4

while True:
    for ambient_light_average in vcnl4020.ambient_light_average_values:
        print("Current Ambient light average setting: ", vcn.ambient_light_average)
        for _ in range(10):
            light = vcn.light
            print(f"Proximity: {vcn.proximity}")
            print(f"Ambient light: {vcn.ambient} lux")
            print()
            time.sleep(0.5)
        vcn.ambient_light_average = ambient_light_average

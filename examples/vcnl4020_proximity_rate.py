# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_vcnl4020 import vcnl4020

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
vcn = vcnl4020.VCNL4020(i2c)

vcn.proximity_rate = vcnl4020.SAMPLERATE_31_25

while True:
    for proximity_rate in vcnl4020.proximity_rate_values:
        print("Current Proximity rate setting: ", vcn.proximity_rate)
        for _ in range(10):
            print(f"Proximity: {vcn.proximity}")
            print(f"Ambient light: {vcn.ambient} lux")
            print()
            time.sleep(0.5)
        vcn.proximity_rate = proximity_rate

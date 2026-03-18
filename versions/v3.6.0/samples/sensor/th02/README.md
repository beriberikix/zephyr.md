---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/sensor/th02/README.html
original_path: samples/sensor/th02/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# TH02: Temperature and Humidity Monitor

## Overview

This sample periodically reads temperature and humidity from the Grove
Temperature & Humidity Sensor (TH02) and display the results on the Grove LCD
display.

## Requirements

This sample uses the TH02 sensor and the grove LCD display. Both devices are
controlled using the I2C interface.

More details about the sensor and the display can be found here:

- [Grove Temperature And Humidity](http://wiki.seeed.cc/Grove-TemptureAndHumidity_Sensor-High-Accuracy_AndMini-v1.0/)
- [Grove LCD Module](http://wiki.seeed.cc/Grove-LCD_RGB_Backlight/)

## Wiring

The easiest way to get this wired is to use the Grove shield and connect both
devices to I2C. No additional wiring is required. Depending on the board you are
using you might need to connect two 10K ohm resistors to SDL and SDA (I2C).
The LCD display requires 5 volts, so the voltage switch on the shield needs to
be on 5v.

## References

> - TH02 (Si7005): [https://www.silabs.com/documents/public/data-sheets/Si7005.pdf](https://www.silabs.com/documents/public/data-sheets/Si7005.pdf)

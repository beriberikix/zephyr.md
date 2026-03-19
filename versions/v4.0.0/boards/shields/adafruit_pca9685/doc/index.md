---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/shields/adafruit_pca9685/doc/index.html
original_path: boards/shields/adafruit_pca9685/doc/index.html
---

# Adafruit 16-channel PWM/Servo Shield

## Overview

The Adafruit 16-channel PWM/Servo shield is an Arduino
UNO R3 compatible shield based on the NXP PCA9685 IC.

More information about the shield can be found
at the [Adafruit 16-channel PWM/Servo Shield webpage](https://learn.adafruit.com/adafruit-16-channel-pwm-slash-servo-shield?view=all) [[1]](#id1).

### Pins Assignments

| Shield Connector Pin | Function |
| --- | --- |
| A5 | I2C - SCL1 |
| A4 | I2C - SDA1 |

## Programming

Set `--shield adafruit_pca9685` when you invoke `west build`.
For example:

```shell
# From the root of the zephyr repository
west build -b nrf52840dk/nrf52840 --shield adafruit_pca9685 samples/drivers/led/pwm
```

## References

[[1](#id2)]

[https://learn.adafruit.com/adafruit-16-channel-pwm-slash-servo-shield?view=all](https://learn.adafruit.com/adafruit-16-channel-pwm-slash-servo-shield?view=all)

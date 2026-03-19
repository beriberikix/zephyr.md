---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/shields/adafruit_aw9523/doc/index.html
original_path: boards/shields/adafruit_aw9523/doc/index.html
---

# Adafruit AW9523 GPIO Expander and LED Driver

## Overview

The [Adafruit AW9523 GPIO Expander and LED Driver](https://learn.adafruit.com/adafruit-aw9523-gpio-expander-and-led-driver) provides
16-channel GPIO/LED controller function.

![Adafruit AW9523](../../../../_images/adafruit_aw9523.webp)

Adafruit AW9523 (Credit: Adafruit)

### Pin Assignments

| Shield Pin | Function |
| --- | --- |
| SDA | AW9523B I2C SDA |
| SCL | AW9523B I2C SCL |
| INT (Pad on board) | AW9523B Interrupt output [[1]](#id3) |
| RST (Pad on board) | AW9523B Reset pin [[2]](#id4) |

[[1](#id1)]

To receive interrupts, connect the INT pin to the SoC’s GPIO and set the connected
GPIO in the `int-gpios` property in an additional overlay. The INT terminal must be
pulled up.

[[2](#id2)]

If you want to control the reset pin from the SoC, connect it to a GPIO on the SoC
and define the `reset-gpios` property in an additional overlay.

## Programming

Set `--shield adafruit_aw9523` when you invoke `west build`.

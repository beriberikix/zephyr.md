---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/shields/arduino_modulino_buttons/doc/index.html
original_path: boards/shields/arduino_modulino_buttons/doc/index.html
---

# Arduino Modulino Buttons

## Overview

The Arduino Modulino Buttons is a QWIIC compatible module with three buttons
and three LEDs.

![Arduino Modulino Buttons module](../../../../_images/arduino_modulino_buttons.webp)

## Programming

Set `--shield arduino_modulino_buttons` when you invoke `west build`, the
buttons will be available through the input subsystem and the LEDs through the
LED subsystem.

For example,

```shell
# From the root of the zephyr repository
west build -b arduino_uno_r4@wifi --shield arduino_modulino_buttons samples/subsys/input
```

---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/shields/x_nucleo_53l0a1/README.html
original_path: samples/shields/x_nucleo_53l0a1/README.html
---

# X-NUCLEO-53L0A1 shield

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/shields/x_nucleo_53l0a1/README.rst/..)

## Overview

This sample demonstrate the usage of the 4 digits x 7 segments display and the
three VL53L0X ranging sensors on the [X-NUCLEO-53L0A1 ranging and gesture detection sensor expansion board](../../../boards/shields/x_nucleo_53l0a1/doc/index.md#x-nucleo-53l0a1-shield).

When flashed on a board, 2 modes are available. To switch from one mode to the
other, press the button `sw0`.

### Distance (onboard sensor)

This is the default mode when starting up. In this mode, if the distance to
the center sensor (soldered on the shield) is lower than 1.25m, then the
4x7 segment display shows the distance in cm.

### Proximity (onboard + satellites)

In this mode, the 4x7 segment display shows 3 stacked horizontal bars if there
is something in proximity for each sensor. The left sensor is shown on the
leftmost digit, then the center sensor, then the right sensor.
The proximity threshold is configured in
[`CONFIG_VL53L0X_PROXIMITY_THRESHOLD`](../../../kconfig.md#CONFIG_VL53L0X_PROXIMITY_THRESHOLD "CONFIG_VL53L0X_PROXIMITY_THRESHOLD")

To switch from one mode to another, press the button `sw0`

## Requirements

This sample communicates over I2C with the X-NUCLEO-53L0A1 shield
stacked on a board with an Arduino connector. The board’s I2C must be
configured for the I2C Arduino connector (both for pin muxing
and devicetree). The board must also have a button with the alias `sw0`
in its device tree.

## References

- [X-NUCLEO-53L0A1 website](https://www.st.com/en/evaluation-tools/x-nucleo-53l0a1.html)

## Building and Running

This sample runs with X-NUCLEO-53L0A1 stacked on any board with a matching
Arduino connector. For this example, we use a [Nucleo F429ZI](../../../boards/st/nucleo_f429zi/doc/index.md#nucleo_f429zi) board.

```shell
west build -b nucleo_f429zi samples/shields/x_nucleo_53l0a1
```

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)

[GPIO Driver APIs](../../../doxygen/html/group__gpio__interface.md)

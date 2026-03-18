---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/shields/x_nucleo_53l0a1/README.html
original_path: samples/shields/x_nucleo_53l0a1/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# X-NUCLEO-53L0A1 shield

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
Arduino connector. For this example, we use a [ST Nucleo F429ZI](../../../boards/st/nucleo_f429zi/doc/index.md#nucleo-f429zi-board) board.

```shell
west build -b nucleo_f429zi samples/shields/x_nucleo_53l0a1
```

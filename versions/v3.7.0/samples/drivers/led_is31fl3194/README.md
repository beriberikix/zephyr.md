---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/drivers/led_is31fl3194/README.html
original_path: samples/drivers/led_is31fl3194/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# IS31FL3194 RGB LED

## Overview

This sample cycles several colors on an RGB LED forever using the LED API.

## Building and Running

This sample can be built and executed on an Arduino Nicla Sense ME, or on
any board where the devicetree has an I2C device node with compatible
[`issi,is31fl3194`](../../../build/dts/api/bindings/led/issi%2Cis31fl3194.md#std-dtcompatible-issi-is31fl3194) enabled, along with the relevant bus
controller node also being enabled.

```shell
west build -b arduino_nicla_sense_me samples/drivers/led/issi_is31fl3194
west flash
```

After flashing, the LED starts to switch colors and messages with the current
LED color are printed on the console. If a runtime error occurs, the sample
exits without printing to the console.

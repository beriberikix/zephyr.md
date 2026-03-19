---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/basic/custom_dts_binding/README.html
original_path: samples/basic/custom_dts_binding/README.html
---

# GPIO with custom Devicetree binding

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/basic/custom_dts_binding/README.rst/..)

## Overview

In Zephyr, all hardware-specific configuration is described in the devicetree.

Consequently, also GPIO pins are configured in the devicetree and assigned to a specific purpose
using a compatible.

This is in contrast to other embedded environments like Arduino, where e.g. the direction (input /
output) of a GPIO pin is configured in the application firmware.

For typical use cases like LEDs or buttons, the existing [`gpio-leds`](../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) or
[`gpio-keys`](../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) compatibles can be used.

This sample demonstrates how to use a GPIO pin for other purposes with a custom devicetree binding.

We assume that a load with high current demands should be switched on or off via a MOSFET. The
custom devicetree binding for the power output controlled via a GPIO pin is specified in the file
[samples/basic/custom\_dts\_binding/dts/bindings/power-switch.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/basic/custom_dts_binding/dts/bindings/power-switch.yaml). The gate driver for
the MOSFET would be connected to the pin as specified in the `.overlay` file in the boards
folder.

## Building and Running

For each board that should be supported, a `.overlay` file has to be defined
in the `boards` subfolder.

Afterwards, the sample can be built and executed for the `<board>` as follows:

```shell
west build -b <board> samples/basic/custom_dts_binding
west flash
```

For demonstration purposes, some boards use the GPIO pin of the built-in LED.

### Sample output

The GPIO pin should be switched to active level after one second.

The following output is printed:

```shell
Initializing pin with inactive level.
Waiting one second.
Setting pin to active level.
```

## See also

[GPIO Driver APIs](../../../doxygen/html/group__gpio__interface.md)

[Node identifiers and helpers](../../../doxygen/html/group__devicetree-generic-id.md)

[Existence checks](../../../doxygen/html/group__devicetree-generic-exist.md)

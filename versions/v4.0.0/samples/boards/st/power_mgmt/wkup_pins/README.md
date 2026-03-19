---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/boards/st/power_mgmt/wkup_pins/README.html
original_path: samples/boards/st/power_mgmt/wkup_pins/README.html
---

# GPIO as a wake-up pin source

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/st/power_mgmt/wkup_pins/README.rst/..)

## Overview

This sample is a minimum application to demonstrate using a wake-up pin with a GPIO as
a source to power on an STM32 SoC after Poweroff.

The system will power off automatically `WAIT_TIME_US` us after boot.
Press the user button designated in boards’s devicetree overlay as “wkup-src” to power it on again.

## Requirements

The SoC should support POWEROFF functionality & have a wake-up pin that corresponds
to the GPIO pin of a user button.
To support another board, add an overlay in boards folder.
Make sure that wake-up pins are configured in SoC dtsi file.

## Building and Running

Build and flash wkup\_pins as follows, changing `nucleo_u5a5zj_q` for your board:

```shell
west build -b nucleo_u5a5zj_q samples/boards/st/power_mgmt/wkup_pins
west flash
```

After flashing, the LED in ON.
The LED will be turned off when the system is powered off.
Press the user button to power on the system again.

## See also

[System power off](../../../../../doxygen/html/group__sys__poweroff.md)

[GPIO Driver APIs](../../../../../doxygen/html/group__gpio__interface.md)

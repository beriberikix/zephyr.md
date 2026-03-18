---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/boards/stm32/power_mgmt/wkup_pins/README.html
original_path: samples/boards/stm32/power_mgmt/wkup_pins/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# GPIO As A Wake-up Pin Source

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
west build -b nucleo_u5a5zj_q samples/boards/stm32/power_mgmt/wkup_pins
west flash
```

After flashing, the LED in ON.
The LED will be turned off when the system is powered off.
Press the user button to power on the system again.

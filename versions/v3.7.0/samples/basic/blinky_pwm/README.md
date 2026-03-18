---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/basic/blinky_pwm/README.html
original_path: samples/basic/blinky_pwm/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# PWM Blinky

## Overview

This application blinks an LED using the [PWM API](../../../hardware/peripherals/pwm.md#pwm-api). See
[Blinky](../blinky/README.md#blinky "Blink an LED forever using the GPIO API.") for a GPIO-based sample.

The LED starts blinking at a 1 Hz frequency. The frequency doubles every 4
seconds until it reaches 128 Hz. The frequency will then be halved every 4
seconds until it returns to 1 Hz, completing a single blinking cycle. This
faster-then-slower blinking cycle then repeats forever.

Some PWM hardware cannot set the PWM period to 1 second to achieve the blinking
frequency of 1 Hz. This sample calibrates itself to what the hardware supports
at startup. The maximum PWM period is decreased appropriately until a value
supported by the hardware is found.

## Requirements

The board must have an LED connected to a PWM output channel. The PWM
controlling this LED must be configured using the `pwm_led0` [devicetree](../../../build/dts/index.md#dt-guide) alias, usually in the [BOARD.dts file](../../../build/dts/intro-input-output.md#devicetree-in-out-files).

## Wiring

No additional wiring is necessary if `pwm_led0` refers to hardware that is
already connected to an LED on the board.

In these other cases, however, manual wiring is necessary:

| Board | Wiring |
| --- | --- |
| [ST Nucleo F401RE](../../../boards/st/nucleo_f401re/doc/index.md#nucleo-f401re-board) | connect PWM2 (PA0) to an LED |
| [ST Nucleo L476RG](../../../boards/st/nucleo_l476rg/doc/index.md#nucleo-l476rg-board) | connect PWM2 (PA0) to an LED |
| [ST STM32F4 Discovery](../../../boards/st/stm32f4_disco/doc/index.md#stm32f4-disco-board) | connect PWM2 (PA0) to an LED |
| [ST Nucleo F302R8](../../../boards/st/nucleo_f302r8/doc/index.md#nucleo-f302r8-board) | connect PWM2 (PA0) to an LED |
| [ST Nucleo F103RB](../../../boards/st/nucleo_f103rb/doc/index.md#nucleo-f103rb-board) | connect PWM1 (PA8) to an LED |
| [ST Nucleo WB55RG](../../../boards/st/nucleo_wb55rg/doc/nucleo_wb55rg.md#nucleo-wb55rg-board) | connect PWM1 (PA8) to an LED |
| [ESP32-DEVKITC-WROOM](../../../boards/espressif/esp32_devkitc_wroom/doc/index.md#esp32-devkitc-wroom) | connect GPIO2 to an LED |
| [ESP32-S2](../../../boards/espressif/esp32s2_saola/doc/index.md#esp32s2-saola) | connect GPIO2 to an LED |
| [ESP32-C3](../../../boards/espressif/esp32c3_devkitm/doc/index.md#esp32c3-devkitm) | connect GPIO2 to an LED |

## Building and Running

To build and flash this sample for the [nRF52840 DK](../../../boards/nordic/nrf52840dk/doc/index.md#nrf52840dk-nrf52840):

```shell
west build -b nrf52840dk/nrf52840 samples/basic/blinky_pwm
west flash
```

Change `nrf52840dk/nrf52840` appropriately for other supported boards.

After flashing, the sample starts blinking the LED as described above. It also
prints information to the board’s console.

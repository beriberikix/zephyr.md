---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/adafruit/macropad_rp2040/doc/index.html
original_path: boards/adafruit/macropad_rp2040/doc/index.html
---

# Adafruit MacroPad RP2040

Board Overview

[![../../../../_images/adafruit_macropad_rp2040.webp](../../../../_images/adafruit_macropad_rp2040.webp)
](../../../../_images/adafruit_macropad_rp2040.webp)

Adafruit MacroPad RP2040

Name:
:   `adafruit_macropad_rp2040`

Vendor:
:   Adafruit Industries, LLC

Architecture:
:   arm

SoC:
:   rp2040

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adafruit/macropad_rp2040/doc/index.rst/../..)

## Adafruit MacroPad RP2040

### Overview

The Adafruit MacroPad RP2040 is a 3x4 mechanical keyboard development board featuring
the Raspberry Pi RP2040 microcontroller. It includes 12 mechanical key switches with
individual RGB NeoPixels, a rotary encoder with push button, a 128x64 OLED display,
and a small speaker for audio feedback.

### Hardware

- Dual core Cortex-M0+ at up to 133MHz
- 264KB of SRAM
- 8MB of QSPI flash memory
- 12 mechanical key switches (Cherry MX compatible)
- 12 RGB NeoPixel LEDs (one per key)
- 128x64 monochrome OLED display (SH1106)
- Rotary encoder with push button
- Small speaker with Class D amplifier
- STEMMA QT / Qwiic I2C connector
- USB Type-C connector
- Reset button
- 4x M3 mounting holes

### Supported Features

The `adafruit_macropad_rp2040` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Programming and Debugging

Applications for the `adafruit_macropad_rp2040` board target can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Building and Flashing

The MacroPad RP2040 has a built-in UF2 bootloader which can be entered by holding down the rotary
encoder button (BOOT) and, while continuing to hold it, pressing and releasing the reset button.
A “RPI-RP2” drive should appear on your host machine.

Here is an example for building and flashing the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample application
using UF2.

```shell
# From the root of the zephyr repository
west build -b adafruit_macropad_rp2040 samples/basic/blinky
west flash --runner uf2
```

### References

- [Adafruit MacroPad RP2040 Product Page](https://www.adafruit.com/product/5128)
- [Adafruit MacroPad RP2040 Learn Guide](https://learn.adafruit.com/adafruit-macropad-rp2040)

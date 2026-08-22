---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/shields/arduino_giga_display_shield/doc/index.html
original_path: boards/shields/arduino_giga_display_shield/doc/index.html
---

# Arduino GIGA Display Shield

## Overview

The Arduino GIGA Display Shield is an extension for the Arduino GIGA R1 WiFi board.
It provides a convenient way to add a display to your projects by offering connectors
for various display modules, including DSI and DPI interfaces.
Additionally, it exposes connectors for the camera interface and includes a microSD card slot.

The front of the shield is equipped with the KD040WVFID026-01-C025A panel, a 3.97-inch
TFT display with a resolution of 480\*800 pixels. The panel also features a capacitive
multi-touch screen with a GT911 controller accessible over I2C.

The shield can be connected to the Arduino GIGA R1 WiFi board via the high-density connectors.

More information about the shield can be found at [Arduino GIGA Display Shield website](https://docs.arduino.cc/hardware/giga-display-shield/) [[1]](#id3).

![../../../../_images/ASX00039_00.default_1000x750.webp](../../../../_images/ASX00039_00.default_1000x750.webp)

Arduino GIGA Display Shield

## Requirements

This shield can only be used with the Arduino GIGA R1 WiFi board, which provides the
necessary connectors and interfaces for display and camera modules.
The board must define node aliases for the required peripherals (e.g., I2C, SPI, DSI)
to properly interface with the shield.

## Programming

Include `--shield arduino_giga_display_shield` when you invoke `west build`
for projects utilizing this shield. For example:

```shell
# From the root of the zephyr repository
west build -b arduino_giga_r1/stm32h747xx/m7 --shield arduino_giga_display_shield samples/subsys/display/lvgl
```

## References

[[1](#id4)]

[https://docs.arduino.cc/hardware/giga-display-shield/](https://docs.arduino.cc/hardware/giga-display-shield/)

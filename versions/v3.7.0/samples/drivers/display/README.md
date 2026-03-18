---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/drivers/display/README.html
original_path: samples/drivers/display/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Display

## Overview

This sample will draw some basic rectangles onto the display.
The rectangle colors and positions are chosen so that you can check the
orientation of the LCD and correct RGB bit order. The rectangles are drawn
in clockwise order, from top left corner: red, green, blue, grey. The shade of
grey changes from black through to white. If the grey looks too green or red
at any point or the order of the corners is not as described above then the LCD
may be endian swapped.

## Building and Running

As this is a generic sample it should work with any display supported by Zephyr.

Below is an example on how to build for a [nRF52840 DK](../../../boards/nordic/nrf52840dk/doc/index.md#nrf52840dk-nrf52840) board with a
[Adafruit 2.8” TFT Touch Shield v2](../../../boards/shields/adafruit_2_8_tft_touch_v2/doc/index.md#adafruit-2-8-tft-touch-v2).

```shell
west build -b nrf52840dk/nrf52840 --shield adafruit_2_8_tft_touch_v2 samples/drivers/display
```

For testing purpose without the need of any hardware, the [native\_sim](../../../boards/native/native_sim/doc/index.md#native-sim)
board is also supported and can be built as follows;

```shell
west build -b native_sim samples/drivers/display
```

## List of Arduino-based display shields

- [Adafruit 2.8” TFT Touch Shield v2](../../../boards/shields/adafruit_2_8_tft_touch_v2/doc/index.md#adafruit-2-8-tft-touch-v2)
- [SSD1306 128x64(/32) pixels generic shield](../../../boards/shields/ssd1306/doc/index.md#ssd1306-128-shield)
- [Generic ST7789V Display Shield](../../../boards/shields/st7789v_generic/doc/index.md#st7789v-generic)
- [WAVESHARE e-Paper Raw Panel Shield](../../../boards/shields/waveshare_epaper/doc/index.md#waveshare-epaper)

---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/display/README.html
original_path: samples/drivers/display/README.html
---

# Display

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/display/README.rst/..)

## Overview

This sample will draw some basic rectangles onto the display.
The rectangle colors and positions are chosen so that you can check the
orientation of the LCD and correct RGB bit order. The rectangles are drawn
in clockwise order, from top left corner: red, green, blue, grey. The shade of
grey changes from black through to white. If the grey looks too green or red
at any point or the order of the corners is not as described above then the LCD
may be endian swapped.

On displays with the [`SCREEN_INFO_X_ALIGNMENT_WIDTH`](../../../doxygen/html/group__display__interface.md#gga23030b6c27446c4579103fe38e821341a1c51db66639919571af38bbc91eb28c1) capability,
such as those using the [`sharp,ls0xx`](../../../build/dts/api/bindings/display/sharp%2Cls0xx.md#std-dtcompatible-sharp-ls0xx) driver, it is only possible
to draw full lines at a time. On these displays, the rectangles described above
will be replaced with bars that take up the entire width of the display. Only
the green and grey bar will be visible.

On monochrome displays, the rectangles (or bars) will all be some shade of grey.

On displays with 1 bit per pixel, the greyscale animation of the bottom
rectangle (or bar) will appear as flickering between black and white.

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

## See also

[Display Interface](../../../doxygen/html/group__display__interface.md)

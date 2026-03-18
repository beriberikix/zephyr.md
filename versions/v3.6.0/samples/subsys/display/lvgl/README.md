---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/subsys/display/lvgl/README.html
original_path: samples/subsys/display/lvgl/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# LVGL basic sample

## Overview

This sample application displays “Hello World” in the center of the screen
and a counter at the bottom which increments every second.
Based on the available input devices on the board used to run the sample,
additional widgets may be displayed and additional interactions enabled:

- Pointer
  :   If your board has a touch panel controller
      ([`zephyr,lvgl-pointer-input`](../../../../build/dts/api/bindings/input/zephyr%2Clvgl-pointer-input.md#std-dtcompatible-zephyr-lvgl-pointer-input)), a button widget is displayed
      in the center of the screen. Otherwise a label widget is displayed.
- Button
  :   The button pseudo device ([`zephyr,lvgl-button-input`](../../../../build/dts/api/bindings/input/zephyr%2Clvgl-button-input.md#std-dtcompatible-zephyr-lvgl-button-input)) maps
      a press/release action to a specific coordinate on screen. In the case
      of this sample, the coordinates are mapped to the center of the screen.
- Encoder
  :   The encoder pseudo device ([`zephyr,lvgl-encoder-input`](../../../../build/dts/api/bindings/input/zephyr%2Clvgl-encoder-input.md#std-dtcompatible-zephyr-lvgl-encoder-input))
      can be used to navigate between widgets and edit their values. If the
      board contains an encoder, an arc widget is displayed, which can be
      edited.
- Keypad
  :   The keypad pseudo device ([`zephyr,lvgl-keypad-input`](../../../../build/dts/api/bindings/input/zephyr%2Clvgl-keypad-input.md#std-dtcompatible-zephyr-lvgl-keypad-input)) can
      be used for focus shifting and also entering characters inside editable
      widgets such as text areas. If the board used with this sample has a
      keypad device, a button matrix is displayed at the bottom of the screen
      to showcase the focus shifting capabilities.

## Requirements

Display shield and a board which provides a configuration
for Arduino connectors, for example:

- [Adafruit 2.8” TFT Touch Shield v2](../../../../boards/shields/adafruit_2_8_tft_touch_v2/doc/index.md#adafruit-2-8-tft-touch-v2) and [nRF52840 DK](../../../../boards/arm/nrf52840dk_nrf52840/doc/index.md#nrf52840dk-nrf52840)
- [Buydisplay 2.8” TFT Touch Shield with Arduino adapter](../../../../boards/shields/buydisplay_2_8_tft_touch_arduino/doc/index.md#buydisplay-2-8-tft-touch-arduino) and [nRF52840 DK](../../../../boards/arm/nrf52840dk_nrf52840/doc/index.md#nrf52840dk-nrf52840)
- [SSD1306 128x64(/32) pixels generic shield](../../../../boards/shields/ssd1306/doc/index.md#ssd1306-128-shield) and [NXP FRDM-K64F](../../../../boards/arm/frdm_k64f/doc/index.md#frdm-k64f)

or a board with an integrated display:

- [ESP-WROVER-KIT](../../../../boards/xtensa/esp_wrover_kit/doc/index.md#esp-wrover-kit)

or a simulated display environment in a [native\_sim](../../../../boards/posix/native_sim/doc/index.md#native-sim) application:

- [Native simulator - native\_sim](../../../../boards/posix/native_sim/doc/index.md#native-sim)
- [SDL2](https://www.libsdl.org) [[1]](#id1)

or

- [NXP MIMXRT1050-EVK](../../../../boards/arm/mimxrt1050_evk/doc/index.md#mimxrt1050-evk)
- [RK043FN02H-CT](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/i.mx-applications-processors/i.mx-rt-series/4.3-lcd-panel:RK043FN02H-CT) [[2]](#id3)

or

- [NXP MIMXRT1060-EVK](../../../../boards/arm/mimxrt1060_evk/doc/index.md#mimxrt1060-evk)
- [RK043FN02H-CT](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/i.mx-applications-processors/i.mx-rt-series/4.3-lcd-panel:RK043FN02H-CT) [[2]](#id3)

## Building and Running

Example building for [nRF52840 DK](../../../../boards/arm/nrf52840dk_nrf52840/doc/index.md#nrf52840dk-nrf52840):

```shell
# From the root of the zephyr repository
west build -b nrf52840dk_nrf52840 samples/subsys/display/lvgl -- -DSHIELD=adafruit_2_8_tft_touch_v2
west flash
```

Example building for [native\_sim](../../../../boards/posix/native_sim/doc/index.md#native-sim):

```shell
# From the root of the zephyr repository
west build -b native_sim samples/subsys/display/lvgl
west build -t run
```

Alternatively, if building from a 64-bit host machine, the previous target
board argument may also be replaced by `native_sim_64`.

## References

[[1](#id2)]

[https://www.libsdl.org](https://www.libsdl.org)

[2]
([1](#id4),[2](#id5))

[https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/i.mx-applications-processors/i.mx-rt-series/4.3-lcd-panel:RK043FN02H-CT](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/i.mx-applications-processors/i.mx-rt-series/4.3-lcd-panel:RK043FN02H-CT)

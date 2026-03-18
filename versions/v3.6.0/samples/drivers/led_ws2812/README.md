---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/drivers/led_ws2812/README.html
original_path: samples/drivers/led_ws2812/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# WS2812 LED strip

## Overview

This sample application demonstrates basic usage of the WS2812 LED
strip driver, for controlling LED strips using WS2812, WS2812b,
SK6812, Everlight B1414 and compatible driver chips.

## Requirements

- LED strip using WS2812 or compatible, such as the [NeoPixel Ring 12
  from AdaFruit](https://www.adafruit.com/product/1643).
- Note that 5V communications may require a level translator, such as the
  [74AHCT125](https://cdn-shop.adafruit.com/datasheets/74AHC125.pdf).
- LED power strip supply. It’s fine to power the LED strip off of your board’s
  IO voltage level even if that’s below 5V; the LEDs will simply be dimmer in
  this case.

## Wiring

1. Ensure your Zephyr board, and the LED strip share a common ground.
2. Connect the LED strip control pin (either I2S SDOUT, SPI MOSI or GPIO) from
   your board to the data input pin of the first WS2812 IC in the strip.
3. Power the LED strip at an I/O level compatible with the control pin signals.

## Wiring on a thingy52

The thingy52 has integrated NMOS transistors, that can be used instead of a level shifter.
The I2S driver supports inverting the output to suit this scheme, using the `out-active-low` dts
property. See the overlay file
[samples/drivers/led\_ws2812/boards/thingy52\_nrf52832.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/led_ws2812/boards/thingy52_nrf52832.overlay) for more detail.

## Building and Running

This sample’s source directory is [samples/drivers/led\_ws2812/](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/led_ws2812/).

To make sure the sample is set up properly for building, you must:

- select the correct WS2812 driver backend for your SoC. This currently should
  be [`CONFIG_WS2812_STRIP_SPI`](../../../kconfig.md#CONFIG_WS2812_STRIP_SPI "CONFIG_WS2812_STRIP_SPI") unless you are using an nRF51 SoC, in
  which case it will be [`CONFIG_WS2812_STRIP_GPIO`](../../../kconfig.md#CONFIG_WS2812_STRIP_GPIO "CONFIG_WS2812_STRIP_GPIO").
  For the nRF52832, the SPI peripheral might output some garbage at the end of
  transmissions, and that might confuse older WS2812 strips. Use the I2S driver
  in those cases.
- create a `led-strip` [devicetree alias](../../../build/dts/intro-syntax-structure.md#dt-alias-chosen), which refers
  to a node in your [devicetree](../../../build/dts/index.md#dt-guide) with a
  `worldsemi,ws2812-i2s`, `worldsemi,ws2812-spi` or
  `worldsemi,ws2812-gpio` compatible. The node must be properly configured for
  the driver backend (I2S, SPI or GPIO) and daisy chain length (number of WS2812
  chips).

For example devicetree configurations for each compatible, see
[samples/drivers/led\_ws2812/boards/thingy52\_nrf52832.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/led_ws2812/boards/thingy52_nrf52832.overlay),
[samples/drivers/led\_ws2812/boards/nrf52dk\_nrf52832.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/led_ws2812/boards/nrf52dk_nrf52832.overlay) and
[samples/drivers/led\_ws2812/boards/nrf51dk\_nrf51422.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/led_ws2812/boards/nrf51dk_nrf51422.overlay).

Some boards are already supported out of the box; see the `boards`
directory for this sample for details.

The sample updates the LED strip periodically. The update frequency can be
modified by changing the `CONFIG_SAMPLE_LED_UPDATE_DELAY`.

Then build and flash the application:

```shell
west build -b <board> samples/drivers/led_ws2812
west flash
```

When you connect to your board’s serial console, you should see the
following output:

```text
***** Booting Zephyr OS build v2.1.0-rc1-191-gd2466cdaf045 *****
[00:00:00.005,920] <inf> main: Found LED strip device WS2812
[00:00:00.005,950] <inf> main: Displaying pattern on strip
```

## Supported drivers

This sample uses different drivers depending on the selected board:

I2S driver:

- thingy52\_nrf52832
- nrf5340dk\_nrf5340 (3.3V logic level, a logic level shifter may be required)
  :   - should work for other boards featuring an nRF5340 host processor

SPI driver:

- mimxrt1050\_evk
- mimxrt1050\_evk\_qspi
- nrf52dk\_nrf52832
- nucleo\_f070rb
- nucleo\_g071rb
- nucleo\_h743zi
- nucleo\_l476rg

GPIO driver (cortex-M0 only):

- bbc\_microbit
- nrf51dk\_nrf51422

## References

- [RGB LED strips: an overview](http://nut-bolt.nl/2012/rgb-led-strips/)
- [74AHCT125 datasheet](https://cdn-shop.adafruit.com/datasheets/74AHC125.pdf)
- An excellent [blog post on WS2812 timing](https://wp.josh.com/2014/05/13/ws2812-neopixels-are-not-so-finicky-once-you-get-to-know-them/).

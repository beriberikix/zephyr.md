---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/led/led_strip/README.html
original_path: samples/drivers/led/led_strip/README.html
---

# LED strip

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/led/led_strip/README.rst/..)

## Overview

This sample application demonstrates basic usage of the LED strip.

## Requirements

Zephyr supports various LED strip chips. For example,

- WS2812, such as the [NeoPixel(WS2812 compatible) LED Strip from AdaFruit](https://www.adafruit.com/product/3919).
- APA102, such as the [Dotstar(APA102 compatible) LED Strip from AdaFruit](https://www.adafruit.com/product/2242).
- LPD8806, such as the [LPD8806 LED Strip from AdaFruit](https://www.adafruit.com/product/1948).
- Power supply. These LED strips usually require a 5V supply.
- If the LED strip connects to the SPI bus, SPI communications usually use 5V
  signaling, which may require a level translator, such as the
  [74AHCT125 datasheet](https://cdn-shop.adafruit.com/datasheets/74AHC125.pdf).

## Wiring

### APA020 and LPD880x

1. Ensure your Zephyr board, the 5V power supply, and the LED strip
   share a common ground.
2. Connect the MOSI pin of your board’s SPI master to the data input
   pin of the first IC in the strip.
3. Connect the SCLK pin of your board’s SPI master to the clock input
   pin of the first IC in the strip.
4. Connect the 5V power supply pin to the 5V input of the LED strip.

### WS2812

1. Ensure your Zephyr board, and the LED strip share a common ground.
2. Connect the LED strip control pin (either I2S SDOUT, SPI MOSI or GPIO) from
   your board to the data input pin of the first WS2812 IC in the strip.
3. Power the LED strip at an I/O level compatible with the control pin signals.

#### Note about thingy52

The thingy52 has integrated NMOS transistors, that can be used instead of a level shifter.
The I2S driver supports inverting the output to suit this scheme, using the `out-active-low` dts
property. See the overlay file
[samples/drivers/led/led\_strip/boards/thingy52\_nrf52832.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/led/led_strip/boards/thingy52_nrf52832.overlay) for more detail.

## Building and Running

The sample updates the LED strip periodically. The update frequency can be
modified by changing the `CONFIG_SAMPLE_LED_UPDATE_DELAY`.

Then build and flash the application:

```shell
west build -b <board> samples/drivers/led/led_strip
west flash
```

When you connect to your board’s serial console, you should see the
following output:

```text
***** Booting Zephyr OS build v2.1.0-rc1-191-gd2466cdaf045 *****
[00:00:00.005,920] <inf> main: Found LED strip device WS2812
[00:00:00.005,950] <inf> main: Displaying pattern on strip
```

## References

- [WS2812 datasheet](https://cdn-shop.adafruit.com/datasheets/WS2812.pdf)
- [LPD8806 datasheet](https://cdn-shop.adafruit.com/datasheets/lpd8806+english.pdf)
- [APA102C datasheet](https://cdn-shop.adafruit.com/product-files/2477/APA102C-iPixelLED.pdf)
- [74AHCT125 datasheet](https://cdn-shop.adafruit.com/datasheets/74AHC125.pdf)
- [RGB LED strips: an overview](http://nut-bolt.nl/2012/rgb-led-strips/)
- An excellent [blog post on WS2812 timing](https://wp.josh.com/2014/05/13/ws2812-neopixels-are-not-so-finicky-once-you-get-to-know-them/).

## See also

[LED Strip Interface](../../../../doxygen/html/group__led__strip__interface.md)

---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/drivers/led_apa102/README.html
original_path: samples/drivers/led_apa102/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# APA102 LED strip

## Overview

This sample application demonstrates basic usage of the APA102 LED
strip driver, for controlling LED strips using APA102, Adafruit DotStar,
and compatible driver chips.

## Requirements

- LED strip using APA102 or compatible, such as the any [Dotstar product
  from AdaFruit](https://www.adafruit.com/category/885).
- Zephyr board with SPI master driver. SPI communications must use 5V
  signaling, which may require a level translator, such as the
  [74AHCT125](https://cdn-shop.adafruit.com/datasheets/74AHC125.pdf).
- 5V power supply.

## Wiring

1. Ensure your Zephyr board, the 5V power supply, and the LED strip
   share a common ground.
2. Connect the MOSI pin of your board’s SPI master to the data input
   pin of the first APA102 IC in the strip.
3. Connect the SCLK pin of your board’s SPI master to the clock input
   pin of the first APA102 IC in the strip.
4. Connect the 5V power supply pin to the 5V input of the LED strip.

## Building and Running

The sample application is located at `samples/drivers/led_apa102/`
in the Zephyr source tree.

### Configure For Your Board

Now check if your board is already supported, by looking for a file
named `boards/YOUR_BOARD_NAME.conf` in the application directory.

If your board isn’t supported yet, you’ll need to configure the
application as follows.

1. Configure your board’s SPI master in a configuration file under
   `boards/` in the sample directory.

   To provide additional configuration for some particular board,
   create a `boards/YOUR_BOARD_NAME.conf` file in the application
   directory. It will be merged into the application configuration.

   In this file, you must ensure that the SPI peripheral you want to
   use for this demo is enabled. See `boards/nucleo_l432kc.conf` for
   an example.

   #. Configure your board’s dts overlay. See `nucleo_l432kc.overlay`
   for an example.
2. Set the number of LEDs in your strip in the application sources.
   This is determined by the macro `STRIP_NUM_LEDS` in the file
   `src/main.c`.

Then build and flash the application:

```shell
west build -b <board> samples/drivers/led_apa102
west flash
```

Refer to your [board’s documentation](../../../boards/index.md#boards) for alternative
flash instructions if your board doesn’t support the `flash` target.

When you connect to your board’s serial console, you should see the
following output:

```text
***** BOOTING ZEPHYR OS zephyr-v1.13.XX *****
[general] [INF] main: Found LED strip device APA102
```

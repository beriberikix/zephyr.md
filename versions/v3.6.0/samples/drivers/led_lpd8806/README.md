---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/drivers/led_lpd8806/README.html
original_path: samples/drivers/led_lpd8806/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# LPD880x LED strip

## Overview

This sample application demonstrates basic usage of the lpd880x LED
strip driver, for controlling LED strips using LPD8803, LPD8806, and
compatible driver chips.

## Requirements

- LED strip using LPD8806 or compatible, such as [these strips from AdaFruit](https://www.adafruit.com/product/306).
- Zephyr board with SPI master driver. SPI communications must use 5V
  signaling, which may require a level translator, such as the
  [74AHCT125](https://cdn-shop.adafruit.com/datasheets/74AHC125.pdf).
- 5V power supply.

## Wiring

1. Ensure your Zephyr board, the 5V power supply, and the LED strip
   share a common ground.
2. Connect the MOSI pin of your board’s SPI master to the data input
   pin of the first LPD8806 IC in the strip.
3. Connect the SCLK pin of your board’s SPI master to the clock input
   pin of the first LPD8806 IC in the strip.
4. Connect the 5V power supply pin to the 5V input of the LED strip.

## Building and Running

The sample application is located at `samples/drivers/led_lpd8806/`
in the Zephyr source tree.

Before running the application, configure it as follows.

1. Configure your board’s SPI master in a configuration file under
   `boards/` in the sample directory.

   To provide additional configuration for some particular board,
   create a `boards/YOUR_BOARD_NAME.conf` file in the application
   directory. It will be merged into the application configuration.

   In this file, you must ensure that the SPI peripheral you want to
   use for this demo is enabled, and that its name is “lpd8806\_spi”.
   See `boards/96b_carbon.conf` for an example, and refer to your
   board’s configuration options to set up your desired SPI master.
2. Set the number of LEDs in your strip in the application sources.
   This is determined by the macro `STRIP_NUM_LEDS` in the file
   `src/main.c`. The value in the file was chosen to work with one
   meter of the AdaFruit strip.

Then build and flash the application:

```shell
west build -b <board> samples/drivers/led_lpd8806
west flash
```

Refer to your [board’s documentation](../../../boards/index.md#boards) for alternative
flash instructions if your board doesn’t support the `flash` target.

When you connect to your board’s serial console, you should see the
following output:

```text
***** BOOTING ZEPHYR OS v1.9.99 *****
[general] [INF] main: Found SPI device lpd8806_spi
[general] [INF] main: Found LED strip device lpd880x_strip
[general] [INF] main: Displaying pattern on strip
```

## References

- [LPD8806 datasheet](https://cdn-shop.adafruit.com/datasheets/lpd8806+english.pdf)
- [74AHCT125 datasheet](https://cdn-shop.adafruit.com/datasheets/74AHC125.pdf)

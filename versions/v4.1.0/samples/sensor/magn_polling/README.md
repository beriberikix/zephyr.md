---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/sensor/magn_polling/README.html
original_path: samples/sensor/magn_polling/README.html
---

# Magnetometer Sensor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/magn_polling/README.rst/..)

## Overview

Sample application that periodically reads magnetometer (X, Y, Z) data from
the first available device that implements SENSOR\_CHAN\_MAGN\_\* (predefined array
of device names).

## Board-specific overlays

### TMAG5170 via Raspberry Pi Pico

The Zephyr driver for the `` ti,tmag5170` `` requires an SPI driver
that supports 32-bit SPI\_WORD\_SIZE. On the [Raspberry Pi Pico](../../../boards/raspberrypi/rpi_pico/doc/index.md#rpi_pico), the
[`raspberrypi,pico-spi-pio`](../../../build/dts/api/bindings/spi/raspberrypi%2Cpico-spi-pio.md#std-dtcompatible-raspberrypi-pico-spi-pio) SPI driver provides this support,
demonstrated with the
[samples/sensor/magn\_polling/boards/rpi\_pico.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/sensor/magn_polling/boards/rpi_pico.overlay).

The GPIO pin assignments in the overlay file are arbitrary. The PIO SPI
driver allows using any four GPIO pins for the SPI bus. Just keep in mind
that the pin assignments in the pinctrl block and the pio0\_spi0 block
must match.

With the sensor wired to the desired pins, build and flash with:

```shell
# From the root of the zephyr repository
west build -b rpi_pico samples/sensor/magn_polling
west flash
```

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)

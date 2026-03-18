---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/sensor/bme280/README.html
original_path: samples/sensor/bme280/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# BME280 Humidity and Pressure Sensor

## Overview

This sample shows how to use the Zephyr [Sensors](../../../hardware/peripherals/sensor/index.md#sensor) API driver for the
[Bosch BME280](https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/) environmental sensor.

The sample periodically reads temperature, pressure and humidity data from the
first available BME280 device discovered in the system. The sample checks the
sensor in polling mode (without interrupt trigger).

## Building and Running

The sample can be configured to support BME280 sensors connected via either I2C
or SPI. Configuration is done via [devicetree](../../../build/dts/index.md#dt-guide). The devicetree
must have an enabled node with `compatible = "bosch,bme280";`. See
[`bosch,bme280`](../../../build/dts/api/compatibles/bosch%2Cbme280.md#std-dtcompatible-bosch-bme280) for the devicetree binding and see below for
examples and common configurations.

If the sensor is not built into your board, start by wiring the sensor pins
according to the connection diagram given in the [BME280 datasheet](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme280-ds002.pdf) at
page 38.

### Boards with a built-in BME280

Your board may have a BME280 node configured in its devicetree by default. Make
sure this node has `status = "okay";`, then build and run with:

```shell
# From the root of the zephyr repository
west build -b adafruit_feather_m0_basic_proto samples/sensor/bme280
west flash
```

### BME280 via Arduino SPI pins

If you wired the sensor to a SPI peripheral on an Arduino header, build and
flash with:

```shell
# From the root of the zephyr repository
west build -b None samples/sensor/bme280 -- -DDTC_OVERLAY_FILE=arduino_spi.overlay
west flash
```

The devicetree overlay [samples/sensor/bme280/arduino\_spi.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/sensor/bme280/arduino_spi.overlay)
works on any board with a properly configured Arduino pin-compatible SPI
peripheral.

### BME280 via Arduino I2C pins

If you wired the sensor to an I2C peripheral on an Arduino header, build and
flash with:

```shell
# From the root of the zephyr repository
west build -b None samples/sensor/bme280 -- -DDTC_OVERLAY_FILE=arduino_i2c.overlay
west flash
```

The devicetree overlay [samples/sensor/bme280/arduino\_i2c.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/sensor/bme280/arduino_i2c.overlay)
works on any board with a properly configured Arduino pin-compatible I2C
peripheral.

### BME280 via Raspberry Pi Pico

The default assignment of the built-in spi0 device on the [Raspberry Pi Pico](../../../boards/raspberrypi/rpi_pico/doc/index.md#rpi-pico) is
to GPIO16 through GPIO19. With the sensor wired to those lines, build and
flash with:

```shell
# From the root of the zephyr repository
west build -b rpi_pico samples/sensor/bme280
west flash
```

An alternative is to use PIO serving as an SPI device. The devicetree
overlay [samples/sensor/bme280/rpi\_pico\_spi\_pio.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/sensor/bme280/rpi_pico_spi_pio.overlay)
demonstrates using PIO SPI with the sensor wired to arbitrary GPIO pins.
Build and flash with:

```shell
# From the root of the zephyr repository
west build -b rpi_pico samples/sensor/bme280 -- -DDTC_OVERLAY_FILE=rpi_pico_spi_pio.overlay
west flash
```

Note that miso-gpios, mosi-gpios, and clk-gpios need to be assigned to the
selected PIO device in pinctrl, while cs-gpios should not; chip select is
controlled by the SPI context and must operate as a conventional GPIO pin,
not under control of PIO.

### Board-specific overlays

If your board’s devicetree does not have a BME280 node already, you can create
a board-specific devicetree overlay adding one in the `boards` directory.
See existing overlays for examples.

The build system uses these overlays by default when targeting those boards, so
no `DTC_OVERLAY_FILE` setting is needed when building and running.

For example, to build for the [Adafruit Feather M0 Basic Proto](../../../boards/adafruit/feather_m0_basic_proto/doc/index.md#adafruit-feather-m0-basic-proto) using the
[samples/sensor/bme280/boards/adafruit\_feather\_m0\_basic\_proto.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/sensor/bme280/boards/adafruit_feather_m0_basic_proto.overlay)
overlay provided with this sample:

```shell
# From the root of the zephyr repository
west build -b adafruit_feather_m0_basic_proto samples/sensor/bme280
west flash
```

### Sample Output

The sample prints output to the serial console. BME280 device driver messages
are also logged. Refer to your board’s documentation for information on
connecting to its serial console.

Here is example output for the default application settings, assuming that only
one BME280 sensor is connected to the standard Arduino I2C pins:

```text
[00:00:00.379,760] <dbg> BME280.bme280_init: initializing "BME280_SPI" on bus "SPI_3"
[00:00:00.379,821] <dbg> BME280.bme280_init: bad chip id 0xff
[00:00:00.379,821] <dbg> BME280.bme280_init: initializing "BME280_I2C" on bus "I2C_0"
[00:00:00.380,340] <dbg> BME280.bme280_init: ID OK
[00:00:00.385,559] <dbg> BME280.bme280_init: BME280_I2C OK
*** Booting Zephyr OS build zephyr-v2.4.0-2940-gbb732ada394f  ***
Found device BME280_I2C, getting sensor data
temp: 20.260000; press: 99.789019; humidity: 46.458984
temp: 20.260000; press: 99.789480; humidity: 46.424804
temp: 20.250000; press: 99.789246; humidity: 46.423828
```

Here is example output for the default application settings, assuming that two
different BME280 sensors are connected to the standard Arduino I2C and SPI pins:

```text
[00:00:00.377,777] <dbg> BME280.bme280_init: initializing "BME280_SPI" on bus "SPI_3"
[00:00:00.377,838] <dbg> BME280.bme280_init: ID OK
[00:00:00.379,608] <dbg> BME280.bme280_init: BME280_SPI OK
[00:00:00.379,638] <dbg> BME280.bme280_init: initializing "BME280_I2C" on bus "I2C_0"
[00:00:00.380,126] <dbg> BME280.bme280_init: ID OK
[00:00:00.385,345] <dbg> BME280.bme280_init: BME280_I2C OK
*** Booting Zephyr OS build zephyr-v2.4.0-2940-gbb732ada394f  ***
Found device BME280_I2C, getting sensor data
temp: 20.150000; press: 99.857675; humidity: 46.447265
temp: 20.150000; press: 99.859121; humidity: 46.458984
temp: 20.150000; press: 99.859234; humidity: 46.469726
```

That the driver logs include a line saying `BME280_I2C OK` in both cases, but
`BME280_SPI OK` is missing when that device is not connected.

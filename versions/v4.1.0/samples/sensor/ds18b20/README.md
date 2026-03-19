---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/sensor/ds18b20/README.html
original_path: samples/sensor/ds18b20/README.html
---

# DS18B20 1-Wire Temperature Sensor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/ds18b20/README.rst/..)

## Overview

This sample shows how to use the Zephyr [Sensors](../../../hardware/peripherals/sensor/index.md#sensor) API driver for the
[DS18B20](https://www.analog.com/en/products/ds18b20.html) 1-Wire temperature sensor.

The sample periodically reads temperature data from the
first available DS18B20 device discovered in the system. The sample checks the
sensor in polling mode (without interrupt trigger).

## Building and Running

The devicetree must have an enabled node with `compatible = "maxim,ds18b20";`.
See below for examples and common configurations.

If the sensor is not built into your board, start by wiring the sensor pins
as shown in the Figure Hardware Configuration of the [DS18B20 datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/ds18b20.pdf) at
page 10.

### Boards with a built-in DS18B20 or a board-specific overlay

Your board may have a DS18B20 node configured in its devicetree by default,
or a board specific overlay file with an DS18B20 node is available.
Make sure this node has `status = "okay";`, then build and run with:

```shell
# From the root of the zephyr repository
west build -b nucleo_g0b1re samples/sensor/ds18b20
west flash
```

### DS18B20 via Arduino Serial pins

Make sure that you have an external circuit to provide an open-drain interface
for the 1-Wire bus.
Once you have wired the sensor and the serial peripheral on the Arduino header
to the 1-Wire bus, build and flash with:

```shell
# From the root of the zephyr repository
west build -b None samples/sensor/ds18b20 -- -DDTC_OVERLAY_FILE=arduino_serial.overlay
west flash
```

The devicetree overlay [samples/sensor/ds18b20/arduino\_serial.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/sensor/ds18b20/arduino_serial.overlay)
should work on any board with a properly configured Arduino pin-compatible Serial
peripheral.

### Sample Output

The sample prints output to the serial console. DS18B20 device driver messages
are also logged. Refer to your board’s documentation for information on
connecting to its serial console.

Here is example output for the default application settings, assuming that only
one DS18B20 sensor is connected to the standard Arduino Serial pins:

```text
*** Booting Zephyr OS build zephyr-v2.6.0-1929-gf7abe4a6689e  ***
Found device "DS18B20", getting sensor data
[00:00:00.000,039] <dbg> w1_serial: w1_serial_init: w1-serial initialized, with 1 devices
[00:00:00.015,140] <dbg> DS18B20: ds18b20_init: Using external power supply: 1
[00:00:00.021,213] <dbg> DS18B20: ds18b20_init: Init DS18B20: ROM=28b1bb3f070000b9

Temp: 25.040000
Temp: 25.030000
```

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)

[1-Wire Sensor API](../../../doxygen/html/group__w1__sensor.md)

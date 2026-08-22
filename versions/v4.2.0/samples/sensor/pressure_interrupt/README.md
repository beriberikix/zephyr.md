---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/samples/sensor/pressure_interrupt/README.html
original_path: samples/sensor/pressure_interrupt/README.html
---

# Barometric pressure and temperature sensor interrupt example

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/pressure_interrupt/README.rst/..)

## Overview

This sample application uses a pressure sensor interrupt line to:

- Inform when a measure is available in the sensor FIFO.
  Temperature and pressure data are read and displayed in terminal.
  If floats are supported, estimated altitude is also displayed.
- Inform when the pressure value crosses a specified threshold.
  Threshold corresponds to around a 50cm altitude increase.
  A message is displayed in the terminal.
- Inform when the pressure value changed more than the specified
  value between two consecutive samples.
  Change value corresponds to a finger pressing the sensor.
  A message is displayed in the terminal.

## Wiring

This sample uses an external breakout for the sensor. A devicetree
overlay must be provided to identify the I2C/SPI bus and GPIO used to
control the sensor.

## Building and Running

This sample supports pressure sensor devices. Device needs
to be aliased as `pressure-sensor`. For example:

```devicetree
/ {
        aliases {
                pressure-sensor = &icp201xx;
        };
};
```

Make sure the aliases are in devicetree, then build and run with:

```shell
# From the root of the zephyr repository
west build -b nrf52dk/nrf52832 samples/sensor/pressure_interrupt
west flash
```

### Sample Output

```shell

```

## Default configuration

> [00:00:00.266,479] <inf> PRESS\_INT\_SAMPLE: Starting ICP201xx sample.
> [00:00:00.273,803] <inf> PRESS\_INT\_SAMPLE: temp 25.49 Cel, pressure 96.271438 kPa, altitude 447.208465 m
> [00:00:00.280,914] <inf> PRESS\_INT\_SAMPLE: temp 25.50 Cel, pressure 96.271331 kPa, altitude 447.234161 m
> [00:00:00.288,024] <inf> PRESS\_INT\_SAMPLE: temp 25.49 Cel, pressure 96.266685 kPa, altitude 447.636077 m
> [00:00:00.295,135] <inf> PRESS\_INT\_SAMPLE: temp 25.50 Cel, pressure 96.267951 kPa, altitude 447.537078 m
> [00:00:00.302,246] <inf> PRESS\_INT\_SAMPLE: temp 25.51 Cel, pressure 96.268577 kPa, altitude 447.488281 m
> [00:00:00.309,356] <inf> PRESS\_INT\_SAMPLE: temp 25.50 Cel, pressure 96.269340 kPa, altitude 447.414978 m
> [00:00:00.316,467] <inf> PRESS\_INT\_SAMPLE: temp 25.50 Cel, pressure 96.268562 kPa, altitude 447.473663 m
> [00:00:00.323,547] <inf> PRESS\_INT\_SAMPLE: temp 25.50 Cel, pressure 96.267341 kPa, altitude 447.596496 m
> <repeats endlessly>
>
> <when sensor is pressed>
> [00:00:09.819,061] <inf> PRESS\_INT\_SAMPLE: PRESSURE CHANGE INTERRUPT
>
> <when the sensor pressure crosses defined threhold>
> [00:00:09.859,039] <inf> PRESS\_INT\_SAMPLE: PRESSURE THRESHOLD INTERRUPT

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)

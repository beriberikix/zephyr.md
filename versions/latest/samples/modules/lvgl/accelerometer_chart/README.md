---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/modules/lvgl/accelerometer_chart/README.html
original_path: samples/modules/lvgl/accelerometer_chart/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# LVGL line chart with accelerometer data

## Overview

A sample application that demonstrates how to use LVGL and the [sensor API](../../../../hardware/peripherals/sensor.md#sensor-api) to
display acceleration data on a line chart that is updated in real time.

This sample creates a line chart with three series, one for each axis of the accelerometer. An LVGL
timer fetches the latest acceleration data from the sensor every 20 ms (default value) and updates
the chart. The update period is configurable, see
[Building and Running](#lvgl-accelerometer-chart-building-and-running) below.

## Requirements

- A board with a display.
- A sensor that provides acceleration data ([`SENSOR_CHAN_ACCEL_XYZ`](../../../../hardware/peripherals/sensor.md#c.sensor_channel.SENSOR_CHAN_ACCEL_XYZ "SENSOR_CHAN_ACCEL_XYZ")) and available
  under the `&accel0` Devicetree alias.

Note

A Devicetree overlay declaring an emulated BMI160 accelerometer is provided for the
`native_posix*` and `native_sim*` board variants, making it possible to run this sample on
your local machine.

## Building and Running

The maximum number of points to display for each series and the sampling rate of the
accelerometer can be configured using the `CONFIG_SAMPLE_CHART_POINTS_PER_SERIES`
and `CONFIG_SAMPLE_ACCEL_SAMPLING_RATE` Kconfig options, respectively.

The default sampling rate is 50 Hz, and the default maximum number of points per series is 50.

The demo can be built as follows (note how in this particular case the sampling rate is set to a
custom value of 20 Hz):

```shell
west build -b native_sim samples/modules/lvgl/accelerometer_chart -- -DCONFIG_SAMPLE_ACCEL_SAMPLING_RATE=20
west build -t run
```

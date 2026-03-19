---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/bluetooth/bthome_sensor_template/README.html
original_path: samples/bluetooth/bthome_sensor_template/README.html
---

# BTHome sensor template

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/bthome_sensor_template/README.rst/..)

## Overview

This code sample provides a template for implementing a [BTHome](https://bthome.io/) sensor.

## Requirements

- A board with Bluetooth LE support
- A BTHome compatible listener, for example [Home Assistant](https://www.home-assistant.io/) with the BTHome integration running.

## Building and Running

This sample can be found under [samples/bluetooth/bthome\_sensor\_template](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/bthome_sensor_template) in the Zephyr tree.

See [Bluetooth](../bluetooth.md#bluetooth) samples for details.

When the sample is running, navigate to Devices & Services under settings in Home
Assistant. There you will be asked to configure the BTHome sensor if everything
went well.

## See also

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)

---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/bluetooth/bthome_sensor_template/README.html
original_path: samples/bluetooth/bthome_sensor_template/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Bluetooth: BTHome sensor template

Template for a [BTHome](https://bthome.io/) sensor.

## Requirements

- A board with BLE support
- A BTHome compatible listener, for example [Home Assistant](https://www.home-assistant.io/) with the BTHome integration running.

## Building and Running

This sample can be found under [samples/bluetooth/bthome\_sensor\_template](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/bthome_sensor_template) in the Zephyr tree.

See [bluetooth samples section](../bluetooth.md#bluetooth-samples) for details.

When the sample is running, navigate to Devices & Services under settings in Home
Assistant. There you will be asked to configure the BTHome sensor if everything
went well.

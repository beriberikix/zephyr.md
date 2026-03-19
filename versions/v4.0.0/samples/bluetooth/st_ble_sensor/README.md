---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/bluetooth/st_ble_sensor/README.html
original_path: samples/bluetooth/st_ble_sensor/README.html
---

# ST Bluetooth LE Sensor Demo

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/st_ble_sensor/README.rst/..)

## Overview

This application demonstrates Bluetooth LE peripheral by exposing vendor-specific
GATT services. Currently only button notification and LED service are
implemented. Other Bluetooth LE sensor services can easily be added.
See [BlueST protocol](https://www.st.com/resource/en/user_manual/dm00550659.pdf) document for details of how to add a new service.

## Requirements

- [ST Bluetooth LE Sensor Android app](https://play.google.com/store/apps/details?id=com.st.bluems)
- A board with Bluetooth LE support

## Building and Running

This sample can be found under [samples/bluetooth/st\_ble\_sensor](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/st_ble_sensor) in the
Zephyr tree.

Open ST Bluetooth LE Sensor app and click on “CONNECT TO A DEVICE” button to scan Bluetooth LE devices.
To connect click on the device shown in the Device List.
After connected, tap LED image on Android to test LED service.
Push SW0 button on embedded device to test button service.

See [Bluetooth](../bluetooth.md#bluetooth) samples for details.

## See also

[Generic Attribute Profile (GATT)](../../../doxygen/html/group__bt__gatt.md)

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)

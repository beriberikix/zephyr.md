---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/bluetooth/ibeacon/README.html
original_path: samples/bluetooth/ibeacon/README.html
---

# iBeacon

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/ibeacon/README.rst/..)

## Overview

This simple application demonstrates the GAP Broadcaster role
functionality by advertising an Apple iBeacon. The calibrated RSSI @ 1
meter distance can be set using an IBEACON\_RSSI build variable
(e.g. IBEACON\_RSSI=0xb8 for -72 dBm RSSI @ 1 meter), or by manually
editing the default value in the `main.c` file.

Because of the hard-coded values of iBeacon UUID, major, and minor,
the application is not suitable for production use, but is quite
convenient for quick demonstrations of iBeacon functionality.

## Requirements

- A board with Bluetooth LE support, or
- QEMU with BlueZ running on the host

## Building and Running

This sample can be found under [samples/bluetooth/ibeacon](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/ibeacon) in the
Zephyr tree.

See [Bluetooth](../bluetooth.md#bluetooth) samples for details on how
to run the sample inside QEMU.

For other boards, build and flash the application as follows:

```shell
west build -b <board> samples/bluetooth/ibeacon
west flash
```

Refer to your [board’s documentation](../../../boards/index.md#boards) for alternative
flash instructions if your board doesn’t support the `flash` target.

## See also

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)

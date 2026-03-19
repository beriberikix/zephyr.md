---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/bluetooth/bap_broadcast_sink/README.html
original_path: samples/bluetooth/bap_broadcast_sink/README.html
---

# Basic Audio Profile (BAP) Broadcast Audio Sink

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/bap_broadcast_sink/README.rst/..)

## Overview

Application demonstrating the BAP Broadcast Sink functionality.
Starts by scanning for BAP Broadcast Sources and then synchronizes to
the first found and listens to it until the source is (potentially) stopped.

This sample can be found under
[samples/bluetooth/bap\_broadcast\_sink](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/bap_broadcast_sink) in the Zephyr tree.

Check the [Bluetooth](../bluetooth.md#bluetooth) samples for general information.

Use `CONFIG_TARGET_BROADCAST_NAME` Kconfig to specify the name
([`CONFIG_BT_DEVICE_NAME`](../../../kconfig.md#CONFIG_BT_DEVICE_NAME "CONFIG_BT_DEVICE_NAME")) of a broadcast source to listen to. With default value
(empty string), sink device will listen to all available broadcast sources.

## Requirements

- BlueZ running on the host, or
- A board with Bluetooth Low Energy 5.2 support

## Building and Running

When building targeting an nrf52 series board with the Zephyr Bluetooth Controller,
use `-DEXTRA_CONF_FILE=overlay-bt_ll_sw_split.conf` to enable the required ISO
feature support.

### Building for an nrf5340dk

You can build both the application core image and an appropriate controller image for the network
core with:

```shell
# From the root of the zephyr repository
west build -b nrf5340dk/nrf5340/cpuapp --sysbuild samples/bluetooth/bap_broadcast_sink/
```

If you prefer to only build the application core image, you can do so by doing instead:

```shell
# From the root of the zephyr repository
west build -b nrf5340dk/nrf5340/cpuapp samples/bluetooth/bap_broadcast_sink/
```

In that case you can pair this application core image with the
[HCI IPC](../hci_ipc/README.md#bluetooth_hci_ipc "Expose a Bluetooth controller to another device or CPU using the IPC subsystem.") sample
[samples/bluetooth/hci\_ipc/nrf5340\_cpunet\_iso-bt\_ll\_sw\_split.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/hci_ipc/nrf5340_cpunet_iso-bt_ll_sw_split.conf) configuration.

### Building for a simulated nrf5340bsim

Similarly to how you would for real HW, you can do:

```shell
# From the root of the zephyr repository
west build -b nrf5340bsim/nrf5340/cpuapp --sysbuild samples/bluetooth/bap_broadcast_sink/
```

Note this will produce a Linux executable in `./build/zephyr/zephyr.exe`.
For more information, check [this board documentation](../../../boards/native/nrf_bsim/doc/nrf5340bsim.md#nrf5340bsim).

### Building for a simulated nrf52\_bsim

```shell
# From the root of the zephyr repository
west build -b nrf52_bsim samples/bluetooth/bap_broadcast_sink/ -- -DEXTRA_CONF_FILE=overlay-bt_ll_sw_split.conf
```

## See also

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)

[Bluetooth Audio](../../../doxygen/html/group__bt__audio.md)

[Bluetooth Basic Audio Profile](../../../doxygen/html/group__bt__bap.md)

[Connection management](../../../doxygen/html/group__bt__conn.md)

[Published Audio Capabilities Service (PACS)](../../../doxygen/html/group__bt__pacs.md)

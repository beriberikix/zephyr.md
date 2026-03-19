---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/bluetooth/pbp_public_broadcast_source/README.html
original_path: samples/bluetooth/pbp_public_broadcast_source/README.html
---

# Public Broadcast Profile (PBP) Public Broadcast Source

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/pbp_public_broadcast_source/README.rst/..)

## Overview

Application demonstrating the PBP Public Broadcast Source functionality.
Will start advertising extended advertising and includes a Broadcast Audio Announcement.
The advertised broadcast audio stream quality will cycle between high and standard quality
every 15 seconds.

This sample can be found under
[samples/bluetooth/pbp\_public\_broadcast\_source](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/pbp_public_broadcast_source) in the Zephyr tree.

Check the [Bluetooth](../bluetooth.md#bluetooth) samples for general information.

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
west build -b nrf5340dk/nrf5340/cpuapp --sysbuild samples/bluetooth/pbp_public_broadcast_source/
```

If you prefer to only build the application core image, you can do so by doing instead:

```shell
# From the root of the zephyr repository
west build -b nrf5340dk/nrf5340/cpuapp samples/bluetooth/pbp_public_broadcast_source/
```

In that case you can pair this application core image with the
[HCI IPC](../hci_ipc/README.md#bluetooth_hci_ipc "Expose a Bluetooth controller to another device or CPU using the IPC subsystem.") sample
[samples/bluetooth/hci\_ipc/nrf5340\_cpunet\_iso-bt\_ll\_sw\_split.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/hci_ipc/nrf5340_cpunet_iso-bt_ll_sw_split.conf) configuration.

### Building for a simulated nrf5340bsim

Similarly to how you would for real HW, you can do:

```shell
# From the root of the zephyr repository
west build -b nrf5340bsim/nrf5340/cpuapp --sysbuild samples/bluetooth/pbp_public_broadcast_source/
```

Note this will produce a Linux executable in `./build/zephyr/zephyr.exe`.
For more information, check [this board documentation](../../../boards/native/nrf_bsim/doc/nrf5340bsim.md#nrf5340bsim).

### Building for a simulated nrf52\_bsim

```shell
# From the root of the zephyr repository
west build -b nrf52_bsim samples/bluetooth/pbp_public_broadcast_source/ -- -DEXTRA_CONF_FILE=overlay-bt_ll_sw_split.conf
```

## See also

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)

[Bluetooth Audio](../../../doxygen/html/group__bt__audio.md)

[Bluetooth Basic Audio Profile](../../../doxygen/html/group__bt__bap.md)

[Public Broadcast Profile (PBP)](../../../doxygen/html/group__bt__pbp.md)

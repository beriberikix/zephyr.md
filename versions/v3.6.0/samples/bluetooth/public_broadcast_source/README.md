---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/bluetooth/public_broadcast_source/README.html
original_path: samples/bluetooth/public_broadcast_source/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Bluetooth: Public Broadcast Source

## Overview

Application demonstrating the LE Public Broadcast Profile source functionality.
Will start advertising extended advertising and includes a Broadcast Audio Announcement.
The advertised broadcast audio stream quality will cycle between high and standard quality
every 15 seconds.

This sample can be found under
[samples/bluetooth/public\_broadcast\_source](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/public_broadcast_source) in the Zephyr tree.

Check the [bluetooth samples section](../bluetooth.md#bluetooth-samples) for general information.

## Requirements

- BlueZ running on the host, or
- A board with Bluetooth Low Energy 5.2 support

## Building and Running

When building targeting an nrf52 series board with the Zephyr Bluetooth Controller,
use -DOVERLAY\_CONFIG=overlay-bt\_ll\_sw\_split.conf to enable the required ISO
feature support.

### Building for an nrf5340dk

You can build both the application core image and an appropriate controller image for the network
core with:

```shell
# From the root of the zephyr repository
west build -b nrf5340dk_nrf5340_cpuapp --sysbuild samples/bluetooth/public_broadcast_source/
```

If you prefer to only build the application core image, you can do so by doing instead:

```shell
# From the root of the zephyr repository
west build -b nrf5340dk_nrf5340_cpuapp samples/bluetooth/public_broadcast_source/
```

In that case you can pair this application core image with the
[hci\_ipc sample](../hci_ipc/README.md#bluetooth-hci-ipc-sample)
[samples/bluetooth/hci\_ipc/nrf5340\_cpunet\_iso-bt\_ll\_sw\_split.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/hci_ipc/nrf5340_cpunet_iso-bt_ll_sw_split.conf) configuration.

### Building for a simulated nrf5340bsim

Similarly to how you would for real HW, you can do:

```shell
# From the root of the zephyr repository
west build -b nrf5340bsim_nrf5340_cpuapp --sysbuild samples/bluetooth/public_broadcast_source/
```

Note this will produce a Linux executable in ./build/zephyr/zephyr.exe.
For more information, check [this board documentation](../../../boards/posix/nrf_bsim/doc/nrf5340bsim.md#nrf5340bsim).

### Building for a simulated nrf52\_bsim

```shell
# From the root of the zephyr repository
west build -b nrf52_bsim samples/bluetooth/public_broadcast_source/ -- -DOVERLAY_CONFIG=overlay-bt_ll_sw_split.conf
```

---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/bluetooth/bap_broadcast_source/README.html
original_path: samples/bluetooth/bap_broadcast_source/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Bluetooth: Broadcast Audio Source

## Overview

Application demonstrating the LE Audio broadcast audio source functionality.
Will start advertising extended advertising with audio flags, periodic advertising with the
broadcast audio source endpoint (BASE) and finally the BIGinfo together with
(mock) Audio (ISO) data.

The broadcast source will reset every 30 seconds to show the full API.

This sample can be found under
[samples/bluetooth/bap\_broadcast\_source](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/bap_broadcast_source) in the Zephyr tree.

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
west build -b nrf5340dk/nrf5340/cpuapp --sysbuild samples/bluetooth/bap_broadcast_source/
```

If you prefer to only build the application core image, you can do so by doing instead:

```shell
# From the root of the zephyr repository
west build -b nrf5340dk/nrf5340/cpuapp samples/bluetooth/bap_broadcast_source/
```

In that case you can pair this application core image with the
[hci\_ipc sample](../hci_ipc/README.md#bluetooth-hci-ipc-sample)
[samples/bluetooth/hci\_ipc/nrf5340\_cpunet\_iso-bt\_ll\_sw\_split.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/hci_ipc/nrf5340_cpunet_iso-bt_ll_sw_split.conf) configuration.

### Building for a simulated nrf5340bsim

Similarly to how you would for real HW, you can do:

```shell
# From the root of the zephyr repository
west build -b nrf5340bsim/nrf5340/cpuapp --sysbuild samples/bluetooth/bap_broadcast_source/
```

Note this will produce a Linux executable in ./build/zephyr/zephyr.exe.
For more information, check [this board documentation](../../../boards/native/nrf_bsim/doc/nrf5340bsim.md#nrf5340bsim).

### Building for a simulated nrf52\_bsim

```shell
# From the root of the zephyr repository
west build -b nrf52_bsim samples/bluetooth/bap_broadcast_source/ -- -DOVERLAY_CONFIG=overlay-bt_ll_sw_split.conf
```

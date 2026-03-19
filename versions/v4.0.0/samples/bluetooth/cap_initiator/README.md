---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/bluetooth/cap_initiator/README.html
original_path: samples/bluetooth/cap_initiator/README.html
---

# Common Audio Profile (CAP) Initiator

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/cap_initiator/README.rst/..)

## Overview

Application demonstrating the CAP Initiator functionality.
Starts by either scanning for a CAP Acceptor and then connects to and sets up available unicast
audio streams, sets up a broadcast audio stream, or both.

This sample can be found under [samples/bluetooth/cap\_initiator](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/cap_initiator) in the Zephyr tree.

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
west build -b nrf5340dk/nrf5340/cpuapp --sysbuild samples/bluetooth/cap_initiator/
```

If you prefer to only build the application core image, you can do so by doing instead:

```shell
# From the root of the zephyr repository
west build -b nrf5340dk/nrf5340/cpuapp samples/bluetooth/cap_initiator/
```

In that case you can pair this application core image with the
[HCI IPC](../hci_ipc/README.md#bluetooth_hci_ipc "Expose a Bluetooth controller to another device or CPU using the IPC subsystem.") sample
[samples/bluetooth/hci\_ipc/nrf5340\_cpunet\_iso-bt\_ll\_sw\_split.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/hci_ipc/nrf5340_cpunet_iso-bt_ll_sw_split.conf) configuration.

### Building for a simulated nrf5340bsim

Similarly to how you would for real HW, you can do:

```shell
# From the root of the zephyr repository
west build -b nrf5340bsim/nrf5340/cpuapp --sysbuild samples/bluetooth/cap_initiator/
```

Note this will produce a Linux executable in `./build/zephyr/zephyr.exe`.
For more information, check [this board documentation](../../../boards/native/nrf_bsim/doc/nrf5340bsim.md#nrf5340bsim).

### Building for a simulated nrf52\_bsim

```shell
# From the root of the zephyr repository
west build -b nrf52_bsim samples/bluetooth/cap_initiator/ -- -DEXTRA_CONF_FILE=overlay-bt_ll_sw_split.conf
```

## See also

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)

[Bluetooth Basic Audio Profile](../../../doxygen/html/group__bt__bap.md)

[Common Audio Profile (CAP)](../../../doxygen/html/group__bt__cap.md)

[Connection management](../../../doxygen/html/group__bt__conn.md)

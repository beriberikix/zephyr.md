---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/bluetooth/mesh_provisioner/README.html
original_path: samples/bluetooth/mesh_provisioner/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Bluetooth: Mesh Provisioner

## Overview

This sample demonstrates how to use the Bluetooth Mesh APIs related to
provisioning and using the Configuration Database (CDB). It is intended
to be tested together with a device capable of being provisioned. For
example, one could use the sample in
[samples/bluetooth/mesh](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/mesh)
or [tests/bluetooth/mesh\_shell](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/bluetooth/mesh_shell).

The application provisions itself and loads the CDB with an application
key, then waits to receive an Unprovisioned Beacon from a device. If the
board has a push button connected via GPIO and configured using the
`sw0` [devicetree](../../../build/dts/index.md#dt-guide) alias, the application then waits
for the user to press the button, which will trigger provisioning using
PB-ADV. If the board doesn’t have the push button, the sample will
provision detected devices automatically. Once provisioning is done, the
node will be present in the CDB but not yet marked as configured. The
application will notice the unconfigured node and start configuring it.
If no errors are encountered, the node is marked as configured.

The configuration of a node involves adding an application key, getting
the composition data, and binding all its models to the application key.

## Requirements

- A board with Bluetooth LE support, or
- QEMU with BlueZ running on the host

## Building and Running

This sample can be found under
[samples/bluetooth/mesh\_provisioner](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/mesh_provisioner) in the Zephyr tree.

See [bluetooth samples section](../bluetooth.md#bluetooth-samples) for details on
how to run the sample inside QEMU.

For other boards, build and flash the application as follows:

```shell
west build -b <board> samples/bluetooth/mesh_provisioner
west flash
```

Refer to your [board’s documentation](../../../boards/index.md#boards) for alternative
flash instructions if your board doesn’t support the `flash` target.

To run the application on an [nRF5340 DK](../../../boards/nordic/nrf5340dk/doc/index.md#nrf5340dk-nrf5340), a Bluetooth controller application
must also run on the network core. The [Bluetooth: HCI IPC](../hci_ipc/README.md#bluetooth-hci-ipc-sample) sample
application may be used. Build this sample with configuration
[samples/bluetooth/hci\_ipc/nrf5340\_cpunet\_bt\_mesh-bt\_ll\_sw\_split.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/hci_ipc/nrf5340_cpunet_bt_mesh-bt_ll_sw_split.conf)
to enable mesh support.

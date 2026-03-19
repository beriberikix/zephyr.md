---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/bluetooth/mesh_demo/README.html
original_path: samples/bluetooth/mesh_demo/README.html
---

# Mesh Demo

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/mesh_demo/README.rst/..)

## Overview

This sample is a Bluetooth Mesh application intended for demonstration
purposes only. The application provisions and configures itself (i.e. no
external provisioner needed) with hard-coded network and application key
values. The local unicast address can be set using a NODE\_ADDR build
variable (e.g. NODE\_ADDR=0x0001 for unicast address 0x0001), or by
manually editing the value in the `board.h` file.

Because of the hard-coded values, the application is not suitable for
production use, but is quite convenient for quick demonstrations of mesh
functionality.

The application has some features especially designed for the BBC
micro:bit boards, such as the ability to send messages using the board’s
buttons as well as showing information of received messages on the
board’s 5x5 LED display. It’s generally recommended to use unicast
addresses in the range of 0x0001-0x0009 for the micro:bit since these
map nicely to displayed addresses and the list of destination addresses
which can be cycled with a button press.

A special address, 0x000f, will make the application become a heart-beat
publisher and enable the other nodes to show information of the received
heartbeat messages.

## Requirements

- A board with Bluetooth LE support, or
- QEMU with BlueZ running on the host

## Building and Running

This sample can be found under [samples/bluetooth/mesh\_demo](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/mesh_demo) in
the Zephyr tree.

See [Bluetooth](../bluetooth.md#bluetooth) samples for details on how
to run the sample inside QEMU.

For other boards, build and flash the application as follows:

```shell
west build -b <board> samples/bluetooth/mesh_demo
west flash
```

Refer to your [board’s documentation](../../../boards/index.md#boards) for alternative
flash instructions if your board doesn’t support the `flash` target.

To run the application on an [nRF5340 DK](../../../boards/nordic/nrf5340dk/doc/index.md#nrf5340dk-nrf5340), a Bluetooth controller application
must also run on the network core. The [HCI IPC](../hci_ipc/README.md#bluetooth_hci_ipc "Expose a Bluetooth controller to another device or CPU using the IPC subsystem.") sample
application may be used. Build this sample with configuration
[samples/bluetooth/hci\_ipc/nrf5340\_cpunet\_bt\_mesh-bt\_ll\_sw\_split.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/hci_ipc/nrf5340_cpunet_bt_mesh-bt_ll_sw_split.conf)
to enable mesh support.

## See also

[Bluetooth Mesh](../../../doxygen/html/group__bt__mesh.md)

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)

---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/bluetooth/hci_spi/README.html
original_path: samples/bluetooth/hci_spi/README.html
---

# HCI SPI

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/hci_spi/README.rst/..)

## Overview

Expose Bluetooth Controller support over SPI to another device/CPU using
the Zephyr SPI HCI transport protocol (similar to BlueNRG).

## Requirements

A board with SPI slave, GPIO and Bluetooth Low Energy support.

## Building and Running

You then need to ensure that your [devicetree](../../../build/dts/index.md#dt-guide) defines a node
for the HCI SPI slave device with compatible
[`zephyr,bt-hci-spi-slave`](../../../build/dts/api/bindings/bluetooth/zephyr%2Cbt-hci-spi-slave.md#std-dtcompatible-zephyr-bt-hci-spi-slave). This node sets an interrupt line to
the host and associates the application with a SPI bus to use.

See [boards/nrf51dk\_nrf51822.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/hci_spi/boards/nrf51dk_nrf51822.overlay) in this sample
directory for an example overlay for the [nRF51 DK](../../../boards/nordic/nrf51dk/doc/index.md#nrf51dk-nrf51822) board.

You can then build this application and flash it onto your board in
the usual way; see [Supported Boards and Shields](../../../boards/index.md#boards) for board-specific building and
flashing information.

You will also need a separate chip acting as BT HCI SPI master. This
application is compatible with the HCI SPI master driver provided by
Zephyr’s Bluetooth HCI driver core; see the help associated with the
[`CONFIG_BT_SPI`](../../../kconfig.md#CONFIG_BT_SPI "CONFIG_BT_SPI") configuration option for more information.

Refer to [Bluetooth](../bluetooth.md#bluetooth) for general Bluetooth information, and
to [Providing Bluetooth to 96b\_carbon](../../../boards/96boards/carbon/doc/nrf51822.md#b-carbon-nrf51-bluetooth) for instructions specific to the
96Boards Carbon board.

## See also

[HCI RAW channel](../../../doxygen/html/group__hci__raw.md)

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)

[SPI Interface](../../../doxygen/html/group__spi__interface.md)

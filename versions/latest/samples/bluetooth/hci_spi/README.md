---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/bluetooth/hci_spi/README.html
original_path: samples/bluetooth/hci_spi/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Bluetooth: HCI SPI

## Overview

Expose Zephyr Bluetooth Controller support over SPI to another device/CPU using
the Zephyr SPI HCI transport protocol (similar to BlueNRG).

## Requirements

A board with SPI slave, GPIO and Bluetooth Low Energy support.

## Building and Running

You then need to ensure that your [devicetree](../../../build/dts/index.md#dt-guide) defines a node
for the HCI SPI slave device with compatible
[`zephyr,bt-hci-spi-slave`](../../../build/dts/api/bindings/bluetooth/zephyr%2Cbt-hci-spi-slave.md#std-dtcompatible-zephyr-bt-hci-spi-slave). This node sets an interrupt line to
the host and associates the application with a SPI bus to use.

See [boards/nrf51dk\_nrf51422.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/hci_spi/boards/nrf51dk_nrf51422.overlay) in this sample
directory for an example overlay for the [nRF51 DK](../../../boards/arm/nrf51dk_nrf51422/doc/index.md#nrf51dk-nrf51422) board.

You can then build this application and flash it onto your board in
the usual way; see [Supported Boards](../../../boards/index.md#boards) for board-specific building and
flashing information.

You will also need a separate chip acting as BT HCI SPI master. This
application is compatible with the HCI SPI master driver provided by
Zephyr’s Bluetooth HCI driver core; see the help associated with the
[`CONFIG_BT_SPI`](../../../kconfig.md#CONFIG_BT_SPI "CONFIG_BT_SPI") configuration option for more information.

Refer to [Bluetooth samples](../bluetooth.md#bluetooth-samples) for general Bluetooth information, and
to [Providing Bluetooth to 96b\_carbon](../../../boards/arm/96b_carbon_nrf51/doc/index.md#b-carbon-nrf51-bluetooth) for instructions specific to the
96Boards Carbon board.

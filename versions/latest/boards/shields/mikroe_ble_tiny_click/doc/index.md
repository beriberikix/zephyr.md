---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/shields/mikroe_ble_tiny_click/doc/index.html
original_path: boards/shields/mikroe_ble_tiny_click/doc/index.html
---

# MikroElektronika BLE TINY Click

## Overview

The MikroElektronika BLE TINY Click carries the Renesas [DA14531MOD](https://www.renesas.com/us/en/products/wireless-connectivity/bluetooth-low-energy/da14531mod-smartbond-tiny-bluetooth-low-energy-module) [[1]](#id3) Bluetooth
LE module in a [mikroBUS](https://www.mikroe.com/mikrobus) [[2]](#id5)™ form factor.

![MikroElektronika BLE TINY Click](../../../../_images/ble-tiny-click.webp)

MikroElektronika BLE TINY Click (Credit: MikroElektronika)

## Requirements

This shield can only be used with a board that provides a mikroBUS™
socket and defines the `mikrobus_serial` node label (see [Shields](../../../../hardware/porting/shields.md#shields)
for more details).

Note

The reset input on the DA14531 Module is active high and is connected to
the RST pin on the mikroBUS socket. On many host boards this RST pin is
connected to a system reset signal that is active low. This results in the
host system unintentionally holding the DA14531 Module in reset. This issue
can be overcome by removing resistor R3 on the BLE TINY Click board, see
the [BLE TINY Click Schematic](https://download.mikroe.com/documents/add-on-boards/click/ble_tiny_click/BLE_TINY_click_v102_Schematic.pdf) [[5]](#id11) for further details.

The DA14531 Module contained on the shield must be programmed with a binary
file that supports the HCI interface over UART, without hardware flow control
as these signals are not supported on the Click footprint.

The [Renesas SmartBond Flash Programmer](https://www.renesas.com/us/en/software-tool/smartbond-flash-programmer) [[6]](#id13) tool can be used to download a
suitable binary and then program it into the DA14531 via the SWD header
present on the Click board. Once the tool has been installed, open it and
press the “Search Online” button. The required binary file can be selected
for download as follows:

![DA14531 HCI Binary File Selection](../../../../_images/da14531-hci-binary.webp)

Selecting the DA14531 HCI Binary File for Download

Press the “Program” button to program the binary file into the DA14531 Module.

For more information about interfacing to the DA14531 and the BLE TINY Click,
see the following documentation:

- [DA14531MOD Datasheet](https://www.renesas.com/us/en/document/dst/da14531-module-datasheet?r=1601921) [[3]](#id7)
- [BLE TINY Click](https://www.mikroe.com/ble-tiny-click) [[4]](#id9)

## Programming

Set `--shield mikroe_ble_tiny_click` when you invoke `west build`. For
example:

```shell
# From the root of the zephyr repository
west build -b ek-ra8m1 --shield mikroe_ble_tiny_click samples/bluetooth/beacon
```

## References

[[1](#id4)]

[https://www.renesas.com/us/en/products/wireless-connectivity/bluetooth-low-energy/da14531mod-smartbond-tiny-bluetooth-low-energy-module](https://www.renesas.com/us/en/products/wireless-connectivity/bluetooth-low-energy/da14531mod-smartbond-tiny-bluetooth-low-energy-module)

[[2](#id6)]

[https://www.mikroe.com/mikrobus](https://www.mikroe.com/mikrobus)

[[3](#id8)]

[https://www.renesas.com/us/en/document/dst/da14531-module-datasheet?r=1601921](https://www.renesas.com/us/en/document/dst/da14531-module-datasheet?r=1601921)

[[4](#id10)]

[https://www.mikroe.com/ble-tiny-click](https://www.mikroe.com/ble-tiny-click)

[[5](#id12)]

[https://download.mikroe.com/documents/add-on-boards/click/ble\_tiny\_click/BLE\_TINY\_click\_v102\_Schematic.pdf](https://download.mikroe.com/documents/add-on-boards/click/ble_tiny_click/BLE_TINY_click_v102_Schematic.pdf)

[[6](#id14)]

[https://www.renesas.com/us/en/software-tool/smartbond-flash-programmer](https://www.renesas.com/us/en/software-tool/smartbond-flash-programmer)

---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/shields/renesas_us159_da14531evz/doc/index.html
original_path: boards/shields/renesas_us159_da14531evz/doc/index.html
---

# Renesas DA14531 Pmod Board

## Overview

The Renesas US159 DA14531EVZ carries a [DA14531MOD](https://www.renesas.com/us/en/products/wireless-connectivity/bluetooth-low-energy/da14531mod-smartbond-tiny-bluetooth-low-energy-module) [[1]](#id3) Bluetooth LE module
in a [Digilent Pmod](https://digilent.com/reference/pmod/start) [[2]](#id5)™ form factor.

![Renesas US159 DA14531EVZ Pmod](../../../../_images/us159-da14531evz-pmod.webp)

Renesas US159 DA14531EVZ Pmod (Credit: Renesas Electronics)

## Requirements

This shield can only be used with a board that provides a Pmod™
socket and defines the `pmod_serial` node label (see [Shields](../../../../hardware/porting/shields.md#shields) for
more details).

The DA14531 Module contained on the shield must be programmed with a binary
file that supports the HCI interface over UART, with hardware flow control
enabled.

The [Renesas SmartBond Flash Programmer](https://www.renesas.com/us/en/software-tool/smartbond-flash-programmer) [[3]](#id7) tool can be used to download a
suitable binary and then program it into the DA14531 via the SWD header
present on the Pmod board. Once the tool has been installed, open it and
press the “Search Online” button. The required binary file can be selected
for download as follows:

![DA14531 HCI Binary File Selection](../../../../_images/da14531-hci-hw-flow-binary.webp)

Selecting the DA14531 HCI Binary File for Download

Press the “Program” button to program the binary file into the DA14531 Module.

For more information about interfacing to the DA14531 and the US159 DA14531EVZ
Pmod, see the following documentation:

- [DA14531MOD Datasheet](https://www.renesas.com/us/en/document/dst/da14531-module-datasheet?r=1601921) [[4]](#id9)
- [US159 DA14531EVZ Pmod](https://www.renesas.com/en/products/wireless-connectivity/bluetooth-low-energy/us159-da14531evz-low-power-bluetooth-pmod-board-renesas-quickconnect-iot) [[5]](#id11)

## Programming

Set `--shield renesas_us159_da14531evz` when you invoke `west build`. For
example:

```shell
# From the root of the zephyr repository
west build -b ek_ra8m1 --shield renesas_us159_da14531evz samples/bluetooth/beacon
```

## References

[[1](#id4)]

[https://www.renesas.com/us/en/products/wireless-connectivity/bluetooth-low-energy/da14531mod-smartbond-tiny-bluetooth-low-energy-module](https://www.renesas.com/us/en/products/wireless-connectivity/bluetooth-low-energy/da14531mod-smartbond-tiny-bluetooth-low-energy-module)

[[2](#id6)]

[https://digilent.com/reference/pmod/start](https://digilent.com/reference/pmod/start)

[[3](#id8)]

[https://www.renesas.com/us/en/software-tool/smartbond-flash-programmer](https://www.renesas.com/us/en/software-tool/smartbond-flash-programmer)

[[4](#id10)]

[https://www.renesas.com/us/en/document/dst/da14531-module-datasheet?r=1601921](https://www.renesas.com/us/en/document/dst/da14531-module-datasheet?r=1601921)

[[5](#id12)]

[https://www.renesas.com/en/products/wireless-connectivity/bluetooth-low-energy/us159-da14531evz-low-power-bluetooth-pmod-board-renesas-quickconnect-iot](https://www.renesas.com/en/products/wireless-connectivity/bluetooth-low-energy/us159-da14531evz-low-power-bluetooth-pmod-board-renesas-quickconnect-iot)

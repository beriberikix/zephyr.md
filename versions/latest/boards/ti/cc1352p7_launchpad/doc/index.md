---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/ti/cc1352p7_launchpad/doc/index.html
original_path: boards/ti/cc1352p7_launchpad/doc/index.html
---

# CC1352P7 LaunchPad

Board Overview

[![../../../../_images/lp-cc1352p7-top.jpg](../../../../_images/lp-cc1352p7-top.jpg)
](../../../../_images/lp-cc1352p7-top.jpg)

CC1352P7 LaunchPad

Name:
:   `cc1352p7_lp`

Vendor:
:   Texas Instruments

Architecture:
:   arm

SoC:
:   cc1352p7

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ti/cc1352p7_launchpad/doc/index.rst/../..)

## Overview

The Texas Instruments CC1352P7 LaunchPad™ (LP-CC1352P7) is a
development kit for the SimpleLink™ multi-Standard CC1352P7 wireless MCU.

See the [TI CC1352P7 LaunchPad Product Page](https://www.ti.com/tool/LP-CC1352P7) for details.

## Hardware

The CC1352P7 LaunchPad™ development kit features the CC1352P7 wireless MCU.
The board is equipped with two LEDs, two push buttons, antenna switch and
BoosterPack connectors for expansion. It also includes an integrated (XDS110)
debugger.

The CC1352P7 wireless MCU has a 48 MHz Arm® Cortex®-M4F SoC and an
integrated sub-1GHz and 2.4 GHz transceiver with integrated 20dBm power amplifier
(PA) supporting multiple protocols including Bluetooth® Low Energy and IEEE® 802.15.4.

See the [TI CC1352P7 Product Page](https://www.ti.com/product/CC1352P7) for additional details.

### Supported Features

The `cc1352p7_lp` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

All I/O signals are accessible from the BoosterPack connectors. Pin function
aligns with the LaunchPad standard.

| Pin | Function | Usage |
| --- | --- | --- |
| DIO3 | GPIO |  |
| DIO4 | I2C\_MSSCL | I2C SCL |
| DIO5 | I2C\_MSSDA | I2C SDA |
| DIO6 | GPIO | Red LED |
| DIO7 | GPIO | Green LED |
| DIO8 | SSI0\_RX | SPI MISO |
| DIO9 | SSI0\_TX | SPI MOSI |
| DIO10 | SSI0\_CLK | SPI CLK |
| DIO11 | SSIO\_CS | SPI CS |
| DIO12 | UART0\_RX | UART RXD |
| DIO13 | UART0\_TX | UART TXD |
| DIO14 | GPIO | Button 2 |
| DIO15 | GPIO | Button 1 |
| DIO16 |  | JTAG TDO |
| DIO17 |  | JTAG TDI |
| DIO18 | UART0\_RTS | UART RTS / JTAG SWO |
| DIO19 | UART0\_CTS | UART CTS |
| DIO20 | GPIO | Flash CS |
| DIO21 | GPIO |  |
| DIO22 | GPIO |  |
| DIO23 | AUX\_IO | A0 |
| DIO24 | AUX\_IO | A1 |
| DIO25 | AUX\_IO | A2 |
| DIO26 | AUX\_IO | A3 |
| DIO27 | AUX\_IO | A4 |
| DIO28 | AUX\_IO | A5 |
| DIO29 | AUX\_IO | A6 |
| DIO30 | AUX\_IO | A7 |

## Programming and Debugging

Before flashing or debugging ensure the RESET, TMS, TCK, TDO, and TDI jumpers
are in place. Also place jumpers on the TXD and RXD signals for a serial
console using the XDS110 application serial port.

### Prerequisites:

1. Ensure the XDS-110 emulation firmware on the board is updated.

   Download and install the latest [XDS-110 emulation package](http://processors.wiki.ti.com/index.php/XDS_Emulation_Software_Package#XDS_Emulation_Software_.28emupack.29_Download).

   Follow these [xds110 firmware update directions](http://software-dl.ti.com/ccs/esd/documents/xdsdebugprobes/emu_xds110.html#updating-the-xds110-firmware)

   Note that the emulation package install may place the xdsdfu utility
   in `<install_dir>/ccs_base/common/uscif/xds110/`.
2. Install OpenOCD

   Currently, OpenOCD doesn’t support the CC1352P7.
   Until its support get merged, we have to builld a downstream version that could found [here](https://github.com/anobli/openocd).
   Please refer to OpenOCD documentation to build and install OpenOCD.

   For your convenience, we provide a [prebuilt binary](https://github.com/anobli/openocd/actions/runs/10566225265).

```shell
$ unzip openocd-810cb5b21-x86_64-linux-gnu.zip
$ chmod +x openocd-x86_64-linux-gnu/bin/openocd
$ export OPENOCD_DIST=$PWD/openocd-x86_64-linux-gnu
```

By default, zephyr will try to use the OpenOCD binary from SDK.
You will have to define `OPENOCD` and `OPENOCD_DEFAULT_PATH` to use the custom OpenOCD binary.

### Flashing

Applications for the `CC1352P7 LaunchPad` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

First, run your favorite terminal program to listen for output.

```shell
$ screen <tty_device> 115200
```

Replace `<tty_device>` with the port where the XDS110 application
serial device can be found. For example, `/dev/ttyACM0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b cc1352p7_lp samples/hello_world -- -DOPENOCD=$OPENOCD_DIST/bin/openocd -DOPENOCD_DEFAULT_PATH=$OPENOCD_DIST/share/openocd
west flash
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b cc1352p7_lp samples/hello_world -- -DOPENOCD=$OPENOCD_DIST/bin/openocd -DOPENOCD_DEFAULT_PATH=$OPENOCD_DIST/share/openocd
west debug
```

### Bootloader

The ROM bootloader on CC13x2x7 and CC26x2x7 devices is enabled by default. The
bootloader will start if there is no valid application image in flash or the
so-called backdoor is enabled (via option
[`CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_ENABLE`](../../../../kconfig.md#CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_ENABLE "CONFIG_CC13X2_CC26X2_BOOTLOADER_BACKDOOR_ENABLE")) and BTN-1 is held
down during reset. See the bootloader documentation in chapter 10 of the [TI
CC13x2x7 / CC26x2x7 Technical Reference Manual](https://www.ti.com/lit/ug/swcu192/swcu192.pdf) for additional information.

### Power Management and UART

System and device power management are supported on this platform, and
can be enabled via the standard Kconfig options in Zephyr, such as
[`CONFIG_PM`](../../../../kconfig.md#CONFIG_PM "CONFIG_PM"), [`CONFIG_PM_DEVICE`](../../../../kconfig.md#CONFIG_PM_DEVICE "CONFIG_PM_DEVICE").

When system power management is turned on (CONFIG\_PM=y),
sleep state 2 (standby mode) is allowed, and polling is used to retrieve input
by calling uart\_poll\_in(), it is possible for characters to be missed if the
system enters standby mode between calls to uart\_poll\_in(). This is because
the UART is inactive while the system is in standby mode. The workaround is to
disable sleep state 2 while polling:

```c
pm_policy_state_lock_get(PM_STATE_STANDBY, PM_ALL_SUBSTATES);
<code that calls uart_poll_in() and expects input at any point in time>
pm_policy_state_lock_put(PM_STATE_STANDBY, PM_ALL_SUBSTATES);
```

## References

CC1352P7 LaunchPad Quick Start Guide:
:   [https://www.ti.com/lit/pdf/swru573](https://www.ti.com/lit/pdf/swru573)

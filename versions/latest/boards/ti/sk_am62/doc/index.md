---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/ti/sk_am62/doc/index.html
original_path: boards/ti/sk_am62/doc/index.html
---

# SK-AM62 Evaluation board

Board Overview

[![../../../../_images/sk_am62_angled.webp](https://docs.zephyrproject.org/4.2.0/_images/sk_am62_angled.webp)
](https://docs.zephyrproject.org/4.2.0/_images/sk_am62_angled.webp)

SK-AM62 Evaluation board

Name:
:   `sk_am62`

Vendor:
:   Texas Instruments

Architecture:
:   arm64, arm

SoC:
:   am6234

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ti/sk_am62/doc/index.rst/../..)

## Overview

The SK-AM62 board configuration is used by Zephyr applications that run on
the TI AM62x platform. The board configuration provides support for:

- ARM Cortex-M4F MCU core and the following features:

  > - Nested Vector Interrupt Controller (NVIC)
  > - System Tick System Clock (SYSTICK)
- ARM Cortex-A53 core and the following features:

  > - General Interrupt Controller (GIC)
  > - ARM Generic Timer (arch\_timer)
  > - On-chip SRAM (oc\_sram)
  > - UART interfaces (uart0 to uart6)
  > - Mailbox interface (mbox0)

The board configuration also enables support for the semihosting debugging console.

See the [TI AM62X Product Page](https://www.ti.com/product/AM625) for details.

## Hardware

The SK-AM62 EVM features the AM62x SoC, which is composed of a quad Cortex-A53
cluster and a single Cortex-M4 core in the MCU domain. Zephyr is ported to run on
the M4F and A53 cores. The following listed hardware specifications are used:

- High-performance ARM Cortex-A53
- Low-power ARM Cortex-M4F
- Memory

  > - 256KB of SRAM
  > - 2GB of DDR4
- Debug

  > - XDS110 based JTAG

### Supported Features

The `sk_am62` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `sk_am62/am6234/a53` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-A53 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/ti_am62x_a53.dtsi?plain=1#L22)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/ti_am6234_a53.dtsi?plain=1#L14) | [`arm,cortex-a53`](../../../../build/dts/api/bindings/cpu/arm,cortex-a53.md#std-dtcompatible-arm-cortex-a53) |
| GPIO & Headers | on-chip | GPIO Controller for Davinci and Keystone devices[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/ti_am62x_a53.dtsi?plain=1#L191) | [`ti,davinci-gpio`](../../../../build/dts/api/bindings/gpio/ti,davinci-gpio.md#std-dtcompatible-ti-davinci-gpio) |
| I2C | on-chip | TI OMAP I2C Controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/ti_am62x_a53.dtsi?plain=1#L147) | [`ti,omap-i2c`](../../../../build/dts/api/bindings/i2c/ti,omap-i2c.md#std-dtcompatible-ti-omap-i2c) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/ti_am62x_a53.dtsi?plain=1#L46) | [`arm,gic-v3`](../../../../build/dts/api/bindings/interrupt-controller/arm,gic-v3.md#std-dtcompatible-arm-gic-v3) |
| Mailbox | on-chip | TI OMAP MAILBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/ti_am62x_a53.dtsi?plain=1#L138) | [`ti,omap-mailbox`](../../../../build/dts/api/bindings/mbox/ti,omap-mailbox.md#std-dtcompatible-ti-omap-mailbox) |
| Pin control | on-chip | TI K3 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/ti_am62x_a53.dtsi?plain=1#L55) | [`ti,k3-pinctrl`](../../../../build/dts/api/bindings/pinctrl/ti,k3-pinctrl.md#std-dtcompatible-ti-k3-pinctrl) |
| Serial controller | on-chip | ns16550 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/ti_am62x_a53.dtsi?plain=1#L61)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/ti_am62x_a53.dtsi?plain=1#L72) | [`ns16550`](../../../../build/dts/api/bindings/serial/ns16550.md#std-dtcompatible-ns16550) |
| Timer | on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/ti_am62x_a53.dtsi?plain=1#L33) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm,armv8-timer.md#std-dtcompatible-arm-armv8-timer) |

#### `sk_am62/am6234/m4` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am62x_m4.dtsi?plain=1#L20) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| Clock control | on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am62x_m4.dtsi?plain=1#L37) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| GPIO & Headers | on-chip | GPIO Controller for Davinci and Keystone devices[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am62x_m4.dtsi?plain=1#L79) | [`ti,davinci-gpio`](../../../../build/dts/api/bindings/gpio/ti,davinci-gpio.md#std-dtcompatible-ti-davinci-gpio) |
| I2C | on-chip | TI OMAP I2C Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am62x_m4.dtsi?plain=1#L69) | [`ti,omap-i2c`](../../../../build/dts/api/bindings/i2c/ti,omap-i2c.md#std-dtcompatible-ti-omap-i2c) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| Mailbox | on-chip | TI OMAP MAILBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am62x_m4.dtsi?plain=1#L43) | [`ti,omap-mailbox`](../../../../build/dts/api/bindings/mbox/ti,omap-mailbox.md#std-dtcompatible-ti-omap-mailbox) |
| Pin control | on-chip | TI K3 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am62x_m4.dtsi?plain=1#L52) | [`ti,k3-pinctrl`](../../../../build/dts/api/bindings/pinctrl/ti,k3-pinctrl.md#std-dtcompatible-ti-k3-pinctrl) |
| Serial controller | on-chip | ns16550 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am62x_m4.dtsi?plain=1#L58) | [`ns16550`](../../../../build/dts/api/bindings/serial/ns16550.md#std-dtcompatible-ns16550) |
| SRAM | on-chip | Generic on-chip SRAM[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/am62x_m4.dtsi?plain=1#L27) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |

### Devices

#### System Clock

This board configuration uses a system clock frequency of 400 MHz.

#### DDR RAM

The board has 2GB of DDR RAM available. This board configuration
allocates Zephyr 4kB of RAM (only for resource table: 0x9CC00000 to 0x9CC00400).

#### Serial Port

This board configuration uses a single serial communication channel with the
MCU domain UART (MCU\_UART0).

## SD Card

Download TI’s official [WIC](https://dr-download.ti.com/software-development/software-development-kit-sdk/MD-PvdSyIiioq/10.01.10.04/tisdk-default-image-am62xx-evm-10.01.10.04.rootfs.wic.xz) and flash the WIC file with an etching software
onto an SD-card. This will boot Linux on the A53 application cores of the EVM.
While programming for the M4 core, the A53 cores will then load the zephyr binary on the M4 core using remoteproc.

## Programming for M4F Core

The board can use remoteproc, and uses the OpenAMP resource table to accomplish this.

The testing requires the binary to be copied to the SD card to allow the A53 cores to load it while booting using remoteproc.

To test the M4F core, we build the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample with the following command.

```shell
# From the root of the Zephyr repository
west build -p -b sk_am62/am6234/m4 samples/hello_world
```

This builds the program and the binary is present in the `build/zephyr` directory as
`zephyr.elf`.

We now copy this binary onto the SD card in the `/lib/firmware` directory and name it as
`am62-mcu-m4f0_0-fw`.

```shell
# Mount the SD card at sdcard for example
sudo mount /dev/sdX sdcard
# copy the elf to the /lib/firmware directory
sudo cp --remove-destination zephyr.elf sdcard/lib/firmware/am62-mcu-m4f0_0-fw
```

The SD card can now be used for booting. The binary will now be loaded onto the M4F core on boot.

To allow the board to boot using the SD card, set the boot pins to the SD Card boot mode. Refer to [EVM Setup Page](https://software-dl.ti.com/mcu-plus-sdk/esd/AM62X/08_06_00_18/exports/docs/api_guide_am62x/EVM_SETUP_PAGE.html).

After changing the boot mode, the board should go through the boot sequence on powering up.
The binary will run and print Hello world to the MCU\_UART0 port.

## Programming for A53 Core

Copy the compiled `zephyr.bin` to the first FAT partition of the SD card and
plug the SD card into the board. Power it up and stop the u-boot execution at
prompt.

Use U-Boot to load and kick zephyr.bin:

```shell
fatload mmc 1:1 0x82000000 zephyr.bin; go 0x82000000
```

The Zephyr application should start running on the A53 core.

## Debugging

The board is equipped with an XDS110 JTAG debugger. To debug a binary, utilize the `debug` build target:

- M4F Core

```shell
west build -b sk_am62/am6234/m4 <my_app>
west debug
```

- A53 Core

```shell
west build -b sk_am62/am6234/a53 <my_app>
west debug
```

Hint

To utilize this feature, you’ll need OpenOCD version 0.12 or higher. Due to the possibility of
older versions being available in package feeds, it’s advisable to [build OpenOCD from source](https://docs.u-boot.org/en/latest/board/ti/k3.html#building-openocd-from-source).

## References

AM62x SK EVM TRM:
:   [https://www.ti.com/lit/ug/spruiv7/spruiv7.pdf](https://www.ti.com/lit/ug/spruiv7/spruiv7.pdf)

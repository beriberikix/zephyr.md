---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/beagle/pocketbeagle_2/doc/index.html
original_path: boards/beagle/pocketbeagle_2/doc/index.html
---

# PocketBeagle 2

Board Overview

[![../../../../_images/pocketbeagle_2.webp](https://docs.zephyrproject.org/4.2.0/_images/pocketbeagle_2.webp)
](https://docs.zephyrproject.org/4.2.0/_images/pocketbeagle_2.webp)

PocketBeagle 2

Name:
:   `pocketbeagle_2`

Vendor:
:   BeagleBoard.org Foundation

Architecture:
:   arm64, arm

SoC:
:   am6232

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/beagle/pocketbeagle_2/doc/index.rst/../..)

## Overview

PocketBeagle 2 is a computational platform powered by TI AM62x SoC (there are two
revisions, AM6232 and AM6254).

The board configuration provides support for the ARM Cortex-M4F MCU core.

See the [PocketBeagle 2 Product Page](https://www.beagleboard.org/boards/pocketbeagle-2) for details.

## Hardware

PocketBeagle 2 features the TI AM62x SoC based around an Arm Cortex-A53 multicore
cluster with an Arm Cortex-M4F microcontroller, Imagination Technologies AXE-1-16
graphics processor (from revision A1) and TI programmable real-time unit subsystem
microcontroller cluster coprocessors.

Zephyr is ported to run on the both A53 cores and/or M4F core.

The following listed hardware specifications are used:

- Dual ARM Cortex-A53 cores
- Low-power ARM Cortex-M4F
- Memory

  > - 256KB of SRAM
  > - 512MB of DDR4

Currently supported PocketBeagle 2 revisions:

- A0: Comes wth SOC AM6232

### Supported Features

The `pocketbeagle_2` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `pocketbeagle_2@A0/am6232/a53` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-A53 CPU[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/ti_am62x_a53.dtsi?plain=1#L22) | [`arm,cortex-a53`](../../../../build/dts/api/bindings/cpu/arm,cortex-a53.md#std-dtcompatible-arm-cortex-a53) |
| GPIO & Headers | on-chip | GPIO Controller for Davinci and Keystone devices[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/ti_am62x_a53.dtsi?plain=1#L191)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/ti_am62x_a53.dtsi?plain=1#L201) | [`ti,davinci-gpio`](../../../../build/dts/api/bindings/gpio/ti,davinci-gpio.md#std-dtcompatible-ti-davinci-gpio) |
| I2C | on-chip | TI OMAP I2C Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/ti_am62x_a53.dtsi?plain=1#L169)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/ti_am62x_a53.dtsi?plain=1#L147) | [`ti,omap-i2c`](../../../../build/dts/api/bindings/i2c/ti,omap-i2c.md#std-dtcompatible-ti-omap-i2c) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/ti_am62x_a53.dtsi?plain=1#L46) | [`arm,gic-v3`](../../../../build/dts/api/bindings/interrupt-controller/arm,gic-v3.md#std-dtcompatible-arm-gic-v3) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/beagle/pocketbeagle_2/pocketbeagle_2_am6232_a53.dts?plain=1#L40) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Mailbox | on-chip | TI OMAP MAILBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/ti_am62x_a53.dtsi?plain=1#L138) | [`ti,omap-mailbox`](../../../../build/dts/api/bindings/mbox/ti,omap-mailbox.md#std-dtcompatible-ti-omap-mailbox) |
| Pin control | on-chip | TI K3 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/ti_am62x_a53.dtsi?plain=1#L55) | [`ti,k3-pinctrl`](../../../../build/dts/api/bindings/pinctrl/ti,k3-pinctrl.md#std-dtcompatible-ti-k3-pinctrl) |
| Serial controller | on-chip | ns16550 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/ti_am62x_a53.dtsi?plain=1#L127)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/ti_am62x_a53.dtsi?plain=1#L61) | [`ns16550`](../../../../build/dts/api/bindings/serial/ns16550.md#std-dtcompatible-ns16550) |
| Timer | on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/ti/ti_am62x_a53.dtsi?plain=1#L33) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm,armv8-timer.md#std-dtcompatible-arm-armv8-timer) |

#### `pocketbeagle_2@A0/am6232/m4` target

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

The board has 512MB of DDR RAM available. This board configuration
allocates Zephyr 4kB of RAM (only for resource table: 0x9CC00000 to 0x9CC00400).

#### Serial Port

##### A53 Cores

This board configuration uses single serial communication channel with the MAIN domain UART
(MAIN\_UART6, i.e. debug port).

##### M4F Core

This board configuration uses a single serial communication channel with the
MCU domain UART (MCU\_UART0, i.e. P2.05 as RX and P2.07 as TX).

## SD Card

### A53 Cores

Download BeagleBoard.org’s official [BeagleBoard Imaging Utility](https://github.com/beagleboard/bb-imager-rs/releases) to create bootable
SD-card with the Zephyr image. Optionally, the Zephyr SD Card images can be downloaded from
[bb-zephyr-images](https://github.com/beagleboard/bb-zephyr-images/releases).

### M4F Core

Download BeagleBoard.org’s official [BeagleBoard Imaging Utility](https://github.com/beagleboard/bb-imager-rs/releases) to create bootable
SD-card with the Linux distro image. This will boot Linux on the A53 application
cores. These cores will then load the Zephyr binary on the M4 core using remoteproc.

## Flashing

### A53 Core

The testing requires the binary to be copied to the BOOT partition in SD card.

To test the A53 core, we build the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample with the following command.

```shell
# From the root of the zephyr repository
west build -b pocketbeagle_2/am6232/a53 samples/hello_world
```

We now copy this binary onto the SD card in the `/boot/` directory and name it as
`zephyr.bin`.

```shell
# Mount the SD card at sdcard for example
sudo mount /dev/sdX sdcard
# copy the bin to the /boot/
sudo cp --remove-destination zephyr.bin sdcard/boot/zephyr.bin
```

The SD card can now be used for booting.

The binary will run and print Hello world to the debug port.

### M4F Core

The board supports remoteproc using the OpenAMP resource table.

The testing requires the binary to be copied to the SD card to allow the A53 cores to load it while booting using remoteproc.

To test the M4F core, we build the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample with the following command.

```shell
# From the root of the zephyr repository
west build -b pocketbeagle_2/am6232/m4 samples/hello_world
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

The binary will run and print Hello world to the MCU\_UART0 port.

## Debugging

### M4F Core

The board supports debugging M4 core from the A53 cores running Linux. Since the target needs
superuser privilege, openocd needs to be launched separately for now:

```shell
sudo openocd -f board/ti_am625_swd_native.cfg
```

Start debugging

```shell
west build -b pocketbeagle_2/am6232/m4
west debug
```

## References

- [PocketBeagle 2 Product Page](https://www.beagleboard.org/boards/pocketbeagle-2)
- [Documentation](https://docs.beagleboard.org/boards/pocketbeagle-2/index.html)

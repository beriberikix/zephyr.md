---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/beagle/pocketbeagle_2/doc/index.html
original_path: boards/beagle/pocketbeagle_2/doc/index.html
---

# PocketBeagle 2

Board Overview

[![../../../../_images/pocketbeagle_2.webp](../../../../_images/pocketbeagle_2.webp)
](../../../../_images/pocketbeagle_2.webp)

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

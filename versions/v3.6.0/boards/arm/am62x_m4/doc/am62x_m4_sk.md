---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/am62x_m4/doc/am62x_m4_sk.html
original_path: boards/arm/am62x_m4/doc/am62x_m4_sk.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# AM62x-SK M4F Core

## Overview

The AM62x-SK board configuration is used by Zephyr applications that run on
the TI AM62x platform. The board configuration provides support for the ARM
Cortex-M4F MCU core and the following features:

- Nested Vector Interrupt Controller (NVIC)
- System Tick System Clock (SYSTICK)

The board configuration also enables support for the semihosting debugging console.

See the [TI AM62X Product Page](https://www.ti.com/product/AM625) for details.

![TI AM62x-SK EVM](../../../../_images/sk_am62_angled.webp)

Texas Instruments AM62x SK EVM

## Hardware

The AM62x-SK EVM features the AM62x SoC, which is composed of a quad Cortex-A53
cluster and a single Cortex-M4 core in the MCU domain. Zephyr is ported to run on
the M4F core and the following listed hardware specifications are used:

- Low-power ARM Cortex-M4F
- Memory

  > - 256KB of SRAM
  > - 2GB of DDR4
- Debug

  > - XDS110 based JTAG

### Supported Features

The am62x\_m4\_sk configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| PINCTRL | on-chip | pinctrl |
| UART | on-chip | serial |

Other hardware features are not currently supported by the port.

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

Download TI’s official [WIC](https://dr-download.ti.com/software-development/software-development-kit-sdk/MD-PvdSyIiioq/08.06.00.42/tisdk-default-image-am62xx-evm.wic.xz) and flash the WIC file with an etching software
onto an SD-card. This will boot Linux on the A53 application cores of the EVM.
These cores will then load the zephyr binary on the M4 core using remoteproc.

The default configuration can be found in the defconfig file:

```shell
boards/arm/am62x_m4/am62x_m4_sk_defconfig
```

## Flashing

The board can using remoteproc, and uses the OpenAMP resource table to accomplish this.

The testing requires the binary to be copied to the SD card to allow the A53 cores to load it while booting using remoteproc.

To test the M4F core, we build the hello\_world sample with the following command.

```shell
# From the root of the Zephyr repository
west build -p -b am62x_m4_sk samples/hello_world
```

This builds the program and the binary is present in the build/zephyr directory as zephyr.elf.

We now copy this binary onto the SD card in the /lib/firmware directory and name it as am62-mcu-m4f0\_0-fw.

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

## References

AM62x SK EVM TRM:
:   [https://www.ti.com/lit/ug/spruiv7/spruiv7.pdf](https://www.ti.com/lit/ug/spruiv7/spruiv7.pdf)

---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/ti/sk_am62/doc/index.html
original_path: boards/ti/sk_am62/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# SK-AM62 M4F Core

## Overview

The SK-AM62 board configuration is used by Zephyr applications that run on
the TI AM62x platform. The board configuration provides support for the ARM
Cortex-M4F MCU core and the following features:

- Nested Vector Interrupt Controller (NVIC)
- System Tick System Clock (SYSTICK)

The board configuration also enables support for the semihosting debugging console.

See the [TI AM62X Product Page](https://www.ti.com/product/AM625) for details.

![TI SK-AM62 EVM](../../../../_images/sk_am62_angled.webp)

Texas Instruments SK-AM62 EVM

## Hardware

The SK-AM62 EVM features the AM62x SoC, which is composed of a quad Cortex-A53
cluster and a single Cortex-M4 core in the MCU domain. Zephyr is ported to run on
the M4F core and the following listed hardware specifications are used:

- Low-power ARM Cortex-M4F
- Memory

  > - 256KB of SRAM
  > - 2GB of DDR4
- Debug

  > - XDS110 based JTAG

### Supported Features

The sk\_am62 configuration supports the following hardware features:

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

The default configuration can be found in
[boards/ti/sk\_am62/sk\_am62\_am6234\_m4\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/sk_am62/sk_am62_am6234_m4_defconfig)

## Flashing

The board can using remoteproc, and uses the OpenAMP resource table to accomplish this.

The testing requires the binary to be copied to the SD card to allow the A53 cores to load it while booting using remoteproc.

To test the M4F core, we build the hello\_world sample with the following command.

```shell
# From the root of the Zephyr repository
west build -p -b sk_am62/am6234/m4 samples/hello_world
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

## Debugging

The board is equipped with an XDS110 JTAG debugger. To debug a binary, utilize the debug build target:

```shell
# From the root of the zephyr repository
west build -b sk_am62/am6234/m4 <my_app>
west debug
```

Hint

To utilize this feature, you’ll need OpenOCD version 0.12 or higher. Due to the possibility of
older versions being available in package feeds, it’s advisable to [build OpenOCD from source](https://docs.u-boot.org/en/latest/board/ti/k3.html#building-openocd-from-source).

## References

AM62x SK EVM TRM:
:   [https://www.ti.com/lit/ug/spruiv7/spruiv7.pdf](https://www.ti.com/lit/ug/spruiv7/spruiv7.pdf)

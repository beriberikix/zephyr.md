---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/am62x_m4/doc/am62x_m4_phyboard_lyra.html
original_path: boards/arm/am62x_m4/doc/am62x_m4_phyboard_lyra.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# AM62x phyBOARD-Lyra M4F Core

## Overview

The AM62x phyBOARD-Lyra board configuration is used by Zephyr applications
that run on the TI AM62x platform. The board configuration provides support
for the ARM Cortex-M4F MCU core and the following features:

- Nested Vector Interrupt Controller (NVIC)
- System Tick System Clock (SYSTICK)

The board configuration also enables support for the semihosting debugging console.

See the [PHYTEC AM62x Product Page](https://www.phytec.com/product/phycore-am62x/) for details.

![AM62x phyBOARD-Lyra](../../../../_images/phyCORE-AM62x_Lyra_frontside.webp)

PHYTEC phyBOARD-Lyra with the phyCORE-AM62x SoM

## Hardware

The AM62x phyBOARD-Lyra kit features the AM62x SoC, which is composed of a
quad Cortex-A53 cluster and a single Cortex-M4 core in the MCU domain. Zephyr
is ported to run on the M4F core and the following listed hardware
specifications are used:

- Low-power ARM Cortex-M4F
- Memory

  > - 256KB of SRAM
  > - 2GB of DDR4
- Debug

  > - XDS110 based JTAG

### Supported Features

The am62x\_m4\_phyboard\_lyra configuration supports the following hardware features:

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

Download PHYTEC’s official [WIC](https://download.phytec.de/Software/Linux/BSP-Yocto-AM62x/BSP-Yocto-AM62x-PD23.1.0/images/yogurt/phyboard-lyra-am62xx-2/phytec-qt5demo-image-phyboard-lyra-am62xx-2.wic.xz) as well as [BMAP](https://download.phytec.de/Software/Linux/BSP-Yocto-AM62x/BSP-Yocto-AM62x-PD23.1.0/images/yogurt/phyboard-lyra-am62xx-2/phytec-qt5demo-image-phyboard-lyra-am62xx-2.wic.bmap) and flash the WIC file with
an etching software onto an SD-card. This will boot Linux on the A53 application
cores of the SoM. These cores will then load the zephyr binary on the M4 core
using remoteproc.

The default configuration can be found in the defconfig file:

```shell
boards/arm/am62x_m4/am62x_m4_phyboard_lyra_defconfig
```

## Flashing

The Linux running on the A53 uses the remoteproc framework to manage the M4F co-processor.
Therefore, the testing requires the binary to be copied to the SD card to allow the A53 cores to
load it while booting using remoteproc.

To test the M4F core, we build the hello\_world sample with the following command.

```shell
# From the root of the Zephyr repository
west build -p -b am62x_m4_phyboard_lyra samples/hello_world
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

To allow the board to boot using the SD card, set the boot pins to the SD Card boot mode. Refer to [phyBOARD SD Card Booting Essentials](https://docs.phytec.com/latest/phycore-am62x/bootingessentials/sdcard.html).

After changing the boot mode, stop in U-Boot to enable the M4F co-processor.

```shell
setenv overlays k3-am62-phyboard-lyra-rpmsg.dtbo
# Save the overlays variable permanently
saveenv
boot
```

The board should boot into Linux and the binary will run and print Hello world to the MCU\_UART0
port.

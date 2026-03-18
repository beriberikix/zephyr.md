---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm64/phycore_am62x_a53/doc/index.html
original_path: boards/arm64/phycore_am62x_a53/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# PHYTEC phyCORE-AM62x (Cortex-A53)

## Overview

PHYTEC phyCORE-AM62x board is based on TI Sitara applications
processor, composed of a quad Cortex®-A53 cluster and a single Cortex®-M4 core.
Zephyr OS is ported to run on the Cortex®-A53 core.

- Board features:

  - RAM: 2GB DDR4
  - Storage:

    - 16GB eMMC
    - 64MB OSPI NOR
    - 4KB EEPROM
  - Ethernet

More information about the board can be found at the
[PHYTEC website](https://www.phytec.com/product/phycore-am62x/).

### Supported Features

The Zephyr phycore\_am62x\_a53 board configuration supports the following hardware
features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| GIC-v3 | on-chip | interrupt controller |
| ARM TIMER | on-chip | system clock |
| PINCTRL | on-chip | pinctrl |
| UART | on-chip | serial port |

### Devices

#### System Clock

This board configuration uses a system clock frequency of 200 MHz.

#### DDR RAM

The board has 2GB of DDR RAM available. This board configuration
allocates Zephyr 1MB of RAM (0x82000000 to 0x82100000).

#### Serial Port

This board configuration uses a single serial communication channel with the
CPU’s UART0.

## SD Card

Download PHYTEC’s official [WIC](https://download.phytec.de/Software/Linux/BSP-Yocto-AM62x/BSP-Yocto-AM62x-PD23.1.0/images/yogurt/phyboard-lyra-am62xx-2/phytec-qt5demo-image-phyboard-lyra-am62xx-2.wic.xz) and [bmap](https://download.phytec.de/Software/Linux/BSP-Yocto-AM62x/BSP-Yocto-AM62x-PD23.1.0/images/yogurt/phyboard-lyra-am62xx-2/phytec-qt5demo-image-phyboard-lyra-am62xx-2.wic.bmap) files and flash the WIC file with
bmap-tools on a SD-card.

```shell
bmaptool copy phytec-qt5demo-image-phyboard-lyra-am62xx-2.wic.xz /dev/sdX
```

## Building

You can build an application in the usual way. Refer to
[Building an Application](../../../../develop/application/index.md#build-an-application) for more details. Here is an example for
[Hello World](../../../../samples/hello_world/README.md#hello-world).

```shell
# From the root of the zephyr repository
west build -b phycore_am62x_a53 samples/hello_world
```

## Programming

Copy the compiled `zephyr.bin` to the first FAT partition of the SD card and
plug the SD card into the board. Power it up and stop the u-boot execution at
prompt.

Use U-Boot to load and kick zephyr.bin:

```shell
fatload mmc 1:1 0x82000000 zephyr.bin; dcache flush; icache flush; dcache off; icache off; go 0x82000000
```

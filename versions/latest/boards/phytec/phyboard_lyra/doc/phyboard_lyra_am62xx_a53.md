---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/phytec/phyboard_lyra/doc/phyboard_lyra_am62xx_a53.html
original_path: boards/phytec/phyboard_lyra/doc/phyboard_lyra_am62xx_a53.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# phyBOARD-Lyra AM62x A53 Core

## Overview

PHYTEC phyBOARD-Lyra AM62x board is based on TI Sitara applications
processor, composed of a quad Cortex®-A53 cluster and a single Cortex®-M4 core.
Zephyr OS is ported to run on the Cortex®-A53 core.

- Board features:

  - RAM: 2GB DDR4
  - Storage:

    - 16GB eMMC
    - 64MB OSPI NOR
    - 4KB EEPROM
  - Ethernet

See the [PHYTEC AM62x Product Page](https://www.phytec.com/product/phycore-am62x/) for details.

![phyBOARD-Lyra AM62x](../../../../_images/phyCORE-AM62x_Lyra_frontside.webp)

PHYTEC phyBOARD-Lyra with the phyCORE-AM62x SoM

### Supported Features

The Zephyr phyboard\_lyra/am6234/a53 board configuration supports the following hardware
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

Download PHYTEC’s official [WIC](https://download.phytec.de/Software/Linux/BSP-Yocto-AM62x/BSP-Yocto-Ampliphy-AM62x-PD23.2.1/images/ampliphy-xwayland/phyboard-lyra-am62xx-3/phytec-qt5demo-image-phyboard-lyra-am62xx-3.wic.xz) and [bmap](https://download.phytec.de/Software/Linux/BSP-Yocto-AM62x/BSP-Yocto-Ampliphy-AM62x-PD23.2.1/images/ampliphy-xwayland/phyboard-lyra-am62xx-3/phytec-qt5demo-image-phyboard-lyra-am62xx-3.wic.bmap) files and flash the WIC file with
bmap-tools on a SD-card.

```shell
bmaptool copy phytec-qt5demo-image-phyboard-lyra-am62xx-3.wic.xz /dev/sdX
```

## Building

You can build an application in the usual way. Refer to
[Building an Application](../../../../develop/application/index.md#build-an-application) for more details. Here is an example for
[Hello World](../../../../samples/hello_world/README.md#hello-world).

```shell
# From the root of the zephyr repository
west build -b phyboard_lyra/am6234/a53 samples/hello_world
```

## Programming

Copy the compiled `zephyr.bin` to the first FAT partition of the SD card and
plug the SD card into the board. Power it up and stop the u-boot execution at
prompt.

Use U-Boot to load and kick zephyr.bin:

```shell
fatload mmc 1:1 0x82000000 zephyr.bin; dcache flush; icache flush; dcache off; icache off; go 0x82000000
```

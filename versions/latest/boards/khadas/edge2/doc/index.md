---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/khadas/edge2/doc/index.html
original_path: boards/khadas/edge2/doc/index.html
---

# Edge2

Board Overview

[![../../../../_images/khadas_edge2.jpg](../../../../_images/khadas_edge2.jpg)
](../../../../_images/khadas_edge2.jpg)

Edge2

Name:
:   `khadas_edge2`

Vendor:
:   Khadas

Architecture:
:   arm64

SoC:
:   rk3588s

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/khadas/edge2/doc/index.rst/../..)

## Overview

See [Product page](https://www.khadas.com/edge2)

## Hardware

See [Hardware details](https://docs.khadas.com/products/sbc/edge2/hardware/start)

### Supported Features

The `khadas_edge2` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

There are multiple serial ports on the board: Zephyr is using
uart2 as serial console.

## Programming and Debugging

Use the following configuration to run basic Zephyr applications and
kernel tests on Khadas Edge2 board. For example, with the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console."):

1. Non-SMP mode

```shell
# From the root of the zephyr repository
west build -b khadas_edge2 samples/hello_world
```

This will build an image with the hello world sample app.

Build the zephyr image:

```shell
mkimage -C none -A arm64 -O linux -a 0x10000000 -e 0x10000000 -d build/zephyr/zephyr.bin build/zephyr/zephyr.img
```

Burn the image on the board (we choose to use Rockchip burning tool [rkdeveloptool](https://github.com/rockchip-linux/rkdeveloptool.git), you will need a [SPL](http://dl.khadas.com/products/edge2/firmware/boot/) which is provided by khadas:

```shell
rkdeveloptool db rk3588_spl_loader_*; rkdeveloptool wl 0x100000 zephyr.img; rkdeveloptool rd
```

The sector 0x100000 was chosen arbitrarily (far away from U-Boot image)

Use U-Boot to load and run Zephyr:

```shell
mmc read ${pxefile_addr_r} 0x100000 0x1000; bootm start ${pxefile_addr_r}; bootm loados; bootm go
```

0x1000 is the size (in number of sectors) or your image. Increase it if needed.

It will display the following console output:

```shell
*** Booting Zephyr OS build XXXXXXXXXXXX  ***
Hello World! khadas_edge2
```

### Flashing

Zephyr image can be loaded in DDR memory at address 0x10000000 from SD Card,
EMMC, QSPI Flash or downloaded from network in uboot.

### References

[Edge2 Documentation](https://docs.khadas.com/products/sbc/edge2/start)

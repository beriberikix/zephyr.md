---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/khadas/edgev/doc/index.html
original_path: boards/khadas/edgev/doc/index.html
---

# Edge-V

Board Overview

Name:
:   `khadas_edgev`

Vendor:
:   Khadas

Architecture:
:   arm64

SoC:
:   rk3399

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/khadas/edgev/doc/index.rst/../..)

## Overview

See <[https://www.khadas.com/edge-v](https://www.khadas.com/edge-v)>

## Hardware

See <[https://docs.khadas.com/linux/edge/Hardware.html#Edge-V-1](https://docs.khadas.com/linux/edge/Hardware.html#Edge-V-1)>

### Supported Features

The `khadas_edgev` board supports the hardware features listed below.

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
kernel tests on Khadas Edge-V board. For example, with the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console."):

1. Non-SMP mode

```shell
# From the root of the zephyr repository
west build -b khadas_edgev samples/hello_world
```

This will build an image with the synchronization sample app.

Build the zephyr image:

```shell
mkimage -C none -A arm64 -O linux -a 0x10000000 -e 0x10000000 -d build/zephyr/zephyr.bin build/zephyr/zephyr.img
```

Use u-boot to load and kick Zephyr.bin to CPU Core0:

```shell
tftpboot ${pxefile_addr_r} zephyr.img; bootm start ${pxefile_addr_r}; bootm loados; bootm go
```

It will display the following console output:

```shell
*** Booting Zephyr OS build XXXXXXXXXXXX  ***
Hello World! khadas_edgev
```

### Flashing

Zephyr image can be loaded in DDR memory at address 0x10000000 from SD Card,
EMMC, QSPI Flash or downloaded from network in uboot.

### References

[Documentation:](https://docs.khadas.com/linux/edge/)

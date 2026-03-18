---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/khadas/edgev/doc/index.html
original_path: boards/khadas/edgev/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Khadas Edge-V

## Overview

See <[https://www.khadas.com/edge-v](https://www.khadas.com/edge-v)>

## Hardware

See <[https://docs.khadas.com/linux/edge/Hardware.html#Edge-V-1](https://docs.khadas.com/linux/edge/Hardware.html#Edge-V-1)>

### Supported Features

Khadas Edge-V board default configuration supports the following
hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| GIC-500 | on-chip | GICv3 interrupt controller |
| ARM TIMER | on-chip | System Clock |
| UART | on-chip | Synopsys DesignWare 8250 serial port |

Other hardware features have not been enabled yet for this board.

The default configuration can be found in (NON-SMP)
[boards/khadas/edgev/khadas\_edgev\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/khadas/edgev/khadas_edgev_defconfig)

There are multiple serial ports on the board: Zephyr is using
uart2 as serial console.

## Programming and Debugging

Use the following configuration to run basic Zephyr applications and
kernel tests on Khadas Edge-V board. For example, with the [Hello World](../../../../samples/hello_world/README.md#hello-world):

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

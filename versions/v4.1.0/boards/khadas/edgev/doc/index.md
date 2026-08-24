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

#### `khadas_edgev/rk3399` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-A53 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3399.dtsi?plain=1#L19) | [`arm,cortex-a53`](../../../../build/dts/api/bindings/cpu/arm,cortex-a53.md#std-dtcompatible-arm-cortex-a53) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3399.dtsi?plain=1#L51) | [`arm,gic-v3`](../../../../build/dts/api/bindings/interrupt-controller/arm,gic-v3.md#std-dtcompatible-arm-gic-v3) |
| Serial controller | on-chip | ns16550 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3399.dtsi?plain=1#L86) | [`ns16550`](../../../../build/dts/api/bindings/serial/ns16550.md#std-dtcompatible-ns16550) |
| Timer | on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3399.dtsi?plain=1#L73) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm,armv8-timer.md#std-dtcompatible-arm-armv8-timer) |

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

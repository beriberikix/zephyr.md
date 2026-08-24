---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/khadas/edge2/doc/index.html
original_path: boards/khadas/edge2/doc/index.html
---

# Edge2

Board Overview

[![../../../../_images/khadas_edge2.jpg](https://docs.zephyrproject.org/4.2.0/_images/khadas_edge2.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/khadas_edge2.jpg)

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

#### `khadas_edge2/rk3588s` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-A55 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588s.dtsi?plain=1#L18) | [`arm,cortex-a55`](../../../../build/dts/api/bindings/cpu/arm,cortex-a55.md#std-dtcompatible-arm-cortex-a55) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588s.dtsi?plain=1#L67) | [`arm,gic-v3`](../../../../build/dts/api/bindings/interrupt-controller/arm,gic-v3.md#std-dtcompatible-arm-gic-v3) |
| Serial controller | on-chip | ns16550 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588s.dtsi?plain=1#L94) | [`ns16550`](../../../../build/dts/api/bindings/serial/ns16550.md#std-dtcompatible-ns16550) |
| Timer | on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3588s.dtsi?plain=1#L81) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm,armv8-timer.md#std-dtcompatible-arm-armv8-timer) |

There are multiple serial ports on the board: Zephyr is using
uart2 as serial console.

## Programming and Debugging

The `khadas_edge2` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

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

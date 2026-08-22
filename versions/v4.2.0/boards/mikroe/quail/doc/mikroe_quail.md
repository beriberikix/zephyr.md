---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/mikroe/quail/doc/mikroe_quail.html
original_path: boards/mikroe/quail/doc/mikroe_quail.html
---

# MikroE Quail

Board Overview

[![../../../../_images/mikroe_quail.webp](../../../../_images/mikroe_quail.webp)
](../../../../_images/mikroe_quail.webp)

MikroE Quail

Name:
:   `mikroe_quail`

Vendor:
:   MikroElektronika d.o.o.

Architecture:
:   arm

SoC:
:   stm32f427xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/mikroe/quail/doc/mikroe_quail.rst/../..)

## Overview

MikroE Quail for STM32 is a development board containing an [STM32F427](https://www.st.com/resource/en/datasheet/stm32f427vg.pdf) [[2]](#id4)
microcontroller. It is equipped with four mikroBUS sockets.
The edges of the board are lined with screw terminals and USB ports for
additional connectivity.

## Hardware

The Quail board contains the following connections:

> - Four mikroBUS connectors
> - 32 screw terminals
> - two USB ports, one for programming and one for external storage

Furthermore the board contains three LEDs that are connected
to the microcontroller.

### Supported Features

The `mikroe_quail` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

The four mikroBUS interfaces are aliased in the device tree so that their
peripherals can be accessed using `mikrobus_N_INTERFACE` so e.g. the SPI on
bus 2 can be found by the alias `mikrobus_2_spi`. The numbering corresponds
with the marking on the board.

For connections on the edge connectors, please refer to [Quail for STM32 User Manual](https://download.mikroe.com/documents/starter-boards/other/quail/quail-board-manual-v100.pdf) [[1]](#id2).

## Programming and Debugging

The `mikroe_quail` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

Applications for the `mikroe_quail` board can be built and flashed in the usual way
(see [Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board ships with a locked flash, and will fail with the message:

```shell
Error: stm32x device protected
```

Unlocking with OpenOCD makes it possible to flash.

```shell
$ openocd -f /usr/share/openocd/scripts/interface/stlink-v2.cfg \
    -f /usr/share/openocd/scripts/target/stm32f4x.cfg -c init\
    -c "reset halt" -c "stm32f4x unlock 0" -c "reset run" -c shutdown
```

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b mikroe_quail samples/hello_world
west flash
```

You should see the following message on the console:

```shell
Hello World! mikroe_quail
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b mikroe_quail samples/hello_world
west debug
```

## References

[[1](#id3)]

[https://download.mikroe.com/documents/starter-boards/other/quail/quail-board-manual-v100.pdf](https://download.mikroe.com/documents/starter-boards/other/quail/quail-board-manual-v100.pdf)

[[2](#id5)]

[https://www.st.com/resource/en/datasheet/stm32f427vg.pdf](https://www.st.com/resource/en/datasheet/stm32f427vg.pdf)

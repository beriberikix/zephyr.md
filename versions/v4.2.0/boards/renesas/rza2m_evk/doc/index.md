---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/renesas/rza2m_evk/doc/index.html
original_path: boards/renesas/rza2m_evk/doc/index.html
---

# RZ/A2M Evaluation Kit

Board Overview

[![../../../../_images/rza2m_evkit.webp](../../../../_images/rza2m_evkit.webp)
](../../../../_images/rza2m_evkit.webp)

RZ/A2M Evaluation Kit

Name:
:   `rza2m_evk`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   arm

SoC:
:   r7s921053vcbg

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/rza2m_evk/doc/index.rst/../..)

## Overview

The RZ/A2M Evaluation Board Kit is a best evaluation board kit to evaluate RZ/A2M.

- On-board device: RZ/A2M (R7S921053VCBG: with DRP function, without encryption function, internal
  RAM 4MB) Evaluation of DRP (Dynamically Reconfigurable Processor) is possible.
- MIPI Camera Module (MIPI CSI) is bundled and image recognition processing etc. can be used with
  images input with MIPI camera.
- HyperMCP (Multi-chip package), in which HyperFlash and HyperRAM are installed in one package,
  is mounted. HyperFlash and HyperRAM can be evaluated.
- A Display Output Board is included and the graphic output is possible by connecting it to the
  external display.
- It is possible to evaluate 2ch Ethernet communication.
- Other peripheral functions such as SDHI and USB can also be evaluated.
- Allows for safe and secure connection to the AWS cloud.
  HyperFlash and HyperRAM are trademarks of Cypress Semiconductor Corporation of the U.S.

## Hardware

The Renesas RZ/A2M MPU documentation can be found at [RZ/A2M Group Website](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rz-mpus/rza2m-image-processing-rtos-mpu-drp-and-4mb-chip-ram) [[1]](#id3)

[![RZ/A2M group feature](../../../../_images/rza2m_block_diagram.webp)
](../../../../_images/rza2m_block_diagram.webp)

RZ/A2M block diagram (Credit: Renesas Electronics Corporation)

Detailed hardware features for the board can be found at [RZ/A2M-EVK Website](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rza2m-evkit-rza2m-evaluation-kit) [[2]](#id5)

### Supported Features

The `rza2m_evk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

## Programming and Debugging

The `rza2m_evk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

Applications for the `rza2m_evk` board configuration can be
built and flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Console

The UART port is accessed by USB-Serial port (CN5).

### Building & Flashing

Here is an example for building and flashing the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b rza2m_evk samples/hello_world
west flash
```

## References

[[1](#id4)]

[https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rz-mpus/rza2m-image-processing-rtos-mpu-drp-and-4mb-chip-ram](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rz-mpus/rza2m-image-processing-rtos-mpu-drp-and-4mb-chip-ram)

[[2](#id6)]

[https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rza2m-evkit-rza2m-evaluation-kit](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rza2m-evkit-rza2m-evaluation-kit)

---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/amd/versal2_rpu/doc/index.html
original_path: boards/amd/versal2_rpu/doc/index.html
---

# Versal 2 RPU development board

Board Overview

Name:
:   `versal2_rpu`

Vendor:
:   Advanced Micro Devices (AMD), Inc.

Architecture:
:   arm

SoC:
:   amd\_versal2\_rpu

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/amd/versal2_rpu/doc/index.rst/../..)

## Overview

This configuration provides support for the RPU(R52), real-time processing unit on Xilinx
Versal2 SOC, it can operate as following:

- Two independent R52 cores with their own TCMs (tightly coupled memories)
- Or as a single dual lock step unit with the TCM.

This processing unit is based on an ARM Cortex-R52 CPU, it also enables the following devices:

- ARM GIC v3 Interrupt Controller
- Global Timer Counter
- SBSA UART

## Hardware

### Supported Features

The `versal2_rpu` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Devices

#### System Timer

This board configuration uses a system timer tick frequency of 100 MHz.

#### Serial Port

This board configuration uses a single serial communication channel with the
on-chip UART0.

#### Memories

Although Flash, DDR and OCM memory regions are defined in the DTS file,
all the code plus data of the application will be loaded in the sram0 region,
which points to the DDR memory. The ocm0 memory area is currently available
for usage, although nothing is placed there by default.

### Known Problems or Limitations

The following platform features are unsupported:

- Only the first core of the R52 subsystem is supported.

## Programming and Debugging

Build and flash in the usual way. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b versal2_rpu samples/hello_world
west flash
```

You should see the following message on the console:

```shell
Hello World! versal2_rpu/amd_versal2_rpu
```

## References

1. ARMv8-R Architecture Reference Manual (ARM DDI 0568A.c ID110520)
2. Cortex-R52 and Cortex-R52F Technical Reference Manual (ARM DDI r1p4 100026\_0104\_01\_en)

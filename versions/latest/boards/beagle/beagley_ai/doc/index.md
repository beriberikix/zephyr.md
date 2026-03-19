---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/beagle/beagley_ai/doc/index.html
original_path: boards/beagle/beagley_ai/doc/index.html
---

# BeagleY-AI

Board Overview

[![../../../../_images/beagley_ai.webp](../../../../_images/beagley_ai.webp)
](../../../../_images/beagley_ai.webp)

BeagleY-AI

Name:
:   `beagley_ai`

Vendor:
:   BeagleBoard.org Foundation

Architecture:
:   arm

SoC:
:   j722s

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/beagle/beagley_ai/doc/index.rst/../..)

## Overview

BeagleY-AI is a computational platform powered by TI AM67A (J722S) SoC, which is
targeted for automotive applications.

## Hardware

BeagleY-AI is powered by TI AM67A (J722S) SoC, which has two domains (Main,
MCU). This document gives overview of Zephyr running on both Cortex R5.

### L1 Memory System

BeagleY-AI defaults to single-core mode for the R5 subsystem. Changes in that
will impact the L1 memory system configuration.

- 32KB instruction cache
- 32KB data cache
- 64KB tightly-coupled memory (TCM)
  \* 32KB TCMA
  \* 32KB TCMB

### Region Address Translation

The RAT module performs a region based address translation. It translates a
32-bit input address into a 36-bit output address. Any input transaction that
starts inside of a programmed region will have its address translated, if the
region is enabled.

### VIM Interrupt Controller

The VIM aggregates device interrupts and sends them to the R5F CPU(s). The VIM
module supports 512 interrupt inputs per R5F core. Each interrupt can be either
a level or a pulse (both active-high). The VIM has two interrupt outputs per core
IRQ and FIQ.

## Supported Features

The board configuration supports a console UART via the HAT header pins. Future
versions will also support a console over RPmsg.

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| UART | on-chip | serial port-polling serial port-interrupt |

Other hardware features are currently not supported.

The default configuration can be found in the defconfig file.

Future configurations will add support for GPIO, I2C, SPI, etc.

## Running Zephyr

The AM67A does not have a separate flash for the R5 core. Because of this
an A53 core has to load the program for the R5 core to the right memory
address, set the PC and start the processor.
This can be done from Linux on the A53 core via remoteproc.

This is the memory mapping from A53 to the memory usable by the R5. Note that
the R5 core always sees its local TCMA at address 0x00000000 and its TCMB0
at address 0x41010000.

The A53 Linux configuration allocates a region in DDR that is shared with
the R5. The amount of the allocation can be changed in the Linux device tree.
Note that BeagleY-AI has 4GB of DDR.

| Region | Addr from A53 | MAIN R5F | Size |
| --- | --- | --- | --- |
| ATCM | 0x0078400000 | 0x0000000000 | 32KB |
| BTCM | 0x0078500000 | 0x0041010000 | 32KB |
| DDR Shared Region | 0x00A2000000 | 0x00A2000000 | 16MB |

| Region | Addr from A53 | MCU R5F | Size |
| --- | --- | --- | --- |
| ATCM | 0x0079000000 | 0x0000000000 | 32KB |
| BTCM | 0x0079020000 | 0x0041010000 | 32KB |
| DDR Shared Region | 0x00A1000000 | 0x00A1000000 | 16MB |

### Steps to run the image

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application
targeting the MAIN domain Cortex R5F on BeagleY-AI:

```shell
# From the root of the zephyr repository
west build -b beagley_ai/j722s/main_r5f0_0 samples/hello_world
```

For the MCU domain Cortex R5F on BeagleY-AI:

```shell
# From the root of the zephyr repository
west build -b beagley_ai/j722s/mcu_r5f0_0 samples/hello_world
```

To load the image:

Copy Zephyr image to the /lib/firmware/ directory.

`cp build/zephyr/zephyr.elf /lib/firmware/`

Ensure the Core is not running.

`echo stop > /dev/remoteproc/am67a-{main,mcu}-r5f0_0/state`

Configuring the image name to the remoteproc module.

`echo zephyr.elf > /dev/remoteproc/am67a-{main,mcu}-r5f0_0/firmware`

Once the image name is configured, send the start command.

`echo start > /dev/remoteproc/am67a-{main,mcu}-r5f0_0/state`

### Console

The Zephyr on BeagleY-AI Cortex-R5F uses UART 1 (HAT pins 8-TX, 10-RX)
as console.

## References

- [BeagleY-AI Homepage](https://beagley.ai)
- [AM67A TRM](https://www.ti.com/lit/zip/sprujb3)
- [Pinout guide](https://pinout.beagley.ai/)
- [Documentation](https://docs.beagleboard.org/latest/boards/beagley/ai)

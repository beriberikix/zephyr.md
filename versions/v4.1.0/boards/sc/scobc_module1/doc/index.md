---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/sc/scobc_module1/doc/index.html
original_path: boards/sc/scobc_module1/doc/index.html
---

# OBC module 1

Board Overview

[![../../../../_images/scobc.jpg](../../../../_images/scobc.jpg)
](../../../../_images/scobc.jpg)

OBC module 1

Name:
:   `scobc_module1`

Vendor:
:   Space Cubics, LLC

Architecture:
:   arm

SoC:
:   designstart\_fpga\_cortex\_m3

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/sc/scobc_module1/doc/index.rst/../..)

## Overview

[Space Cubics](https://spacecubics.com/) [[1]](#id2) OBC module 1 is a single board computer for spacecraft,
especially for 3U CubeSats. The board is based on Xilinx Artix-7 FPGA and
implements ARM Cortex M3 as the main CPU.

It is designed to survive in the severe space environment, extreme temperature,
vacuum, and space radiation.

As the name suggests, the board form factor is a module and requires a base I/O
board connected at CON1, a board-to-board connector. This modularity allows
CubeSat designers the freedom to connect and expand the capability required for
their mission.

## Hardware

### Supported Features

The Space Cubics OBC module 1 provides the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| UART | on-chip | serial port-polling; serial port-interrupt |

The default configuration for the board can be found in the defconfig file:
`boards/arm/scobc_module1/scobc_module1_defconfig`.

Other hardware features are not currently supported by the port.

### System Clock

The board has two 24 MHz external oscillators connected to the FPGA for
redundancy. The FPGA will select an active oscillator as CPU system clock. The
selected clock signal is then used by the CMT in the FPGA, and drives the CPU at
48 MHz by default.

### Serial Port

The default configuration contains one SC UART IP, which is register compatible
with Xilinx UART Lite for basic TX and RX. This UART is configured as the
default console and is accessible through the CON1 pin 43 and 45 for Rx and Tx,
respectively.

## Programming and Debugging

### Flashing

Here is an example for building and flashing the `hello\_world`
application for the board:

Here is an example for building and flashing the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application
for the default design:

```shell
# From the root of the zephyr repository
west build -b scobc_module1 samples/hello_world
west flash
```

After flashing, you should see message similar to the following in the terminal:

```shell
*** Booting Zephyr OS build zephyr-v2.7.99  ***
Hello World! scobc_module1
```

Note, however, that the application was not persisted in flash memory by the
above steps. It was merely written to internal RAM in the FPGA.

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b scobc_module1 samples/hello_world
west debug
```

Step through the application in your debugger, and you should see a message
similar to the following in the terminal:

```shell
*** Booting Zephyr OS build zephyr-v2.7.99  ***
Hello World! scobc_module1
```

## References

[[1](#id3)]

[https://spacecubics.com/](https://spacecubics.com/)

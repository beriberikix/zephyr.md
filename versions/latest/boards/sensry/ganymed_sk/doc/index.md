---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/sensry/ganymed_sk/doc/index.html
original_path: boards/sensry/ganymed_sk/doc/index.html
---

# Ganymed Starter Kit (SK)

Board Overview

[![../../../../_images/ganymed_sk.webp](../../../../_images/ganymed_sk.webp)
](../../../../_images/ganymed_sk.webp)

Ganymed Starter Kit (SK)

Name:
:   `ganymed_sk`

Vendor:
:   sensry.io

Architecture:
:   riscv

SoC:
:   sy120\_gbm, sy120\_gen1

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/sensry/ganymed_sk/doc/index.rst/../..)

## Overview

Note

All software for the Ganymed StarterKit (SK) is experimental and hardware availability
is restricted to the participants in the limited sampling program.

The Ganymed board hardware provides support for the Ganymed sy1xx series IoT multicore
RISC-V SoC with optional sensor level.

## Hardware

- 32-Bit RISC-V 1+8-core processor, up to 500MHz

  - 1x Data Acquisition Unit
  - 8x Data Processing Unit
  - Event Bus
  - MicroDMA
- 4096 KB Global SRAM
- 64 KB Secure SRAM
- 512 KB Global MRAM
- 512 KB Secure MRAM
- CLOCK
- Peripherals

  > - 32x GPIO
  > - 4x TWIM
  > - 4x I2S
  > - 7x SPI
  > - 3x UART
  > - 1x TSN
  > - 1x CAN-FD
  > - 3x ADC
- Power section for on-board power generation and power measurement (selectable)

  > - USB type-C
  > - external 5V power source
- 40-pin JTAG connector (compatible to Olimex ARM-JTAG-OCD-H)
- USB over FTDI (connected to UART0)
- Header for all I/Os and configuration
- Assembly options for the SoC

  - SY120-GBM - Generic Base Module without top level sensors
  - SY120-GEN1 - Generic Module type 1 with top level sensors (see below)

The `ganymed-sk/sy120-gen1` comes with additional on-board sensors.

### Supported Features

The `ganymed_sk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

For more detailed description please refer to [Ganymed StarterKit Board Documentation](https://docs.sensry.net/datasheets/sy120-bob/) [[1]](#id2)

## Programming and Testing

The `ganymed_sk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

### Building

Applications for the `ganymed_sk/sy120_gbm` board can be
built and flashed in the usual way. See
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details on
building and running.

Building the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample:

```shell
west build -b ganymed_sk/sy120_gbm samples/hello_world
```

### Flashing

Test the Ganymed with a [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample.

Flash the zephyr image:

```shell
west build -b None --dev-id /dev/ttyUSB0 samples/hello_world
west flash
```

### Testing

Then attach a serial console, ex. minicom / picocom / putty; Reset the target.
The sample output should be:

```shell
Hello World! ganymed_sk/sy120_gbm
```

## References

[[1](#id3)]

[https://docs.sensry.net/datasheets/sy120-bob/](https://docs.sensry.net/datasheets/sy120-bob/)

---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/sensry/ganymed_bob/doc/index.html
original_path: boards/sensry/ganymed_bob/doc/index.html
---

# Ganymed Break-Out-Board (BOB)

## Overview

Note

All software for the Ganymed Break-Out-Board (BOB) is experimental and hardware availability
is restricted to the participants in the limited sampling program.

The Ganymed board hardware provides support for the Ganymed sy1xx series IoT multicore
RISC-V SoC with optional sensor level.

The SoC has the following core features:

- 32-Bit RSIC-V 1+8-core processor, up to 500MHz

  - 1x Data Acquisition Unit
  - 8x Data Processing Unit
  - Event Bus
  - MicroDMA
- 4096 KB Global SRAM
- 64 KB Secure SRAM
- 512 KB Global MRAM
- 512 KB Secure MRAM
- CLOCK
- RAM
- 32x GPIO
- 4x TWIM
- 4x I2S
- 7x SPI
- 3x UART
- 1x TSN
- 1x CAN-FD
- 3x ADC

![Ganymed Break-Out-Board (BOB) equipped with SY120 GBM](../../../../_images/ganymed_bob_sy120_gbm.webp)

Ganymed Break-Out-Board (BOB) equipped with SY120 GBM (Credit: Sensry)

![Ganymed Break-Out-Board (BOB) equipped with SY120 GEN1](../../../../_images/ganymed_bob_sy120_gen1.webp)

Ganymed Break-Out-Board (BOB) equipped with SY120 GEN1 (Credit: Sensry)

## Hardware

The Ganymed BOB has:

- Assembly options for the SoC include

  - SY120-GBM - Generic Base Module without top level sensors
  - SY120-GEN1 - Generic Module type 1 with top level sensors (Bosch BME680 - SPI1 , Bosch BMA456 - SPI0, Bosch BMG250 - SPI2, STMicro MIS2DH - I2C0)
- power section for on-board power generation and power measurement (selectable)
- 40-pin JTAG connector (compatible to Olimex ARM-JTAG-OCD-H)
- USB over FTDI (connected to UART0)
- Header for I/Os and additional configuration

### Supported Features

The `ganymed-bob/sy120-gbm` board supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| SAADC | on-chip | adc |
| CLOCK | on-chip | clock\_control |
| MRAM | on-chip | flash |
| GPIO | on-chip | gpio |
| TWIM | on-chip | i2c |
| PWM | on-chip | pwm |
| GRTC | on-chip | counter |
| RTT | Segger | console |
| SPI(M/S) | on-chip | spi |
| SPU | on-chip | system protection |
| UART | on-chip | serial |
| TSN | on-chip | ethernet MAC |
| CAN | on-chip | CAN |

Other hardware features have not been enabled yet for this board.

The `ganymed-bob/sy120-gen1` board includes all hardware features of the `ganymed-bob/sy120-gbm` board and comes additionally
with these features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| BME680 | on-chip | environment sensor |
| BMA456 | on-chip | acceleration sensor |
| BMG250 | on-chip | gyrosope sensor |
| MIS2DH | on-chip | vibration sensor |

Other hardware features have not been enabled yet for this board.

## Power

- USB type-C
- external 5V power source

## Programming and Debugging

Applications for the `ganymed-bob/sy120-gbm` board can be
built, flashed, and debugged in the usual way. See
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details on
building and running.

## Testing the Ganymed BreakOut Board

Test the Ganymed with a [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample.
The sample output should be:

```shell
Hello World! ganymed-bob/sy120-gbm
```

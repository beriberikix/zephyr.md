---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/sensry/ganymed_bob/doc/index.html
original_path: boards/sensry/ganymed_bob/doc/index.html
---

# Ganymed Break-Out-Board (BOB)

Board Overview

[![../../../../_images/ganymed_bob_sy120_gbm.webp](https://docs.zephyrproject.org/4.2.0/_images/ganymed_bob_sy120_gbm.webp)
](https://docs.zephyrproject.org/4.2.0/_images/ganymed_bob_sy120_gbm.webp)

Ganymed Break-Out-Board (BOB)

Name:
:   `ganymed_bob`

Vendor:
:   sensry.io

Architecture:
:   riscv

SoC:
:   sy120\_gen1, sy120\_gbm

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/sensry/ganymed_bob/doc/index.rst/../..)

## Overview

Note

All software for the Ganymed Break-Out-Board (BOB) is experimental and hardware availability
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

The `ganymed-bob/sy120-gen1` comes with additional on-board sensors.

### Supported Features

The `ganymed_bob` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `ganymed_bob/sy120_gbm` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | Sensry Ganymed SY1xx Core CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L20) | [`sensry,sy1xx`](../../../../build/dts/api/bindings/cpu/sensry%2Cganymed-sy1xx.md#std-dtcompatible-sensry-sy1xx) |
| Ethernet | on-board | Single Port Gigabit Ethernet Copper PHY with GMII/RGMII/MII/RMII Interfaces[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sensry/ganymed_bob/ganymed_bob_sy120_gbm.dts?plain=1#L28) | [`microchip,vsc8541`](../../../../build/dts/api/bindings/ethernet/phy/microchip%2Cvsc8541-phy.md#std-dtcompatible-microchip-vsc8541) |
| on-chip | This file needs to be included by devices that need to specify a set of pin controller states[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L173) | [`sensry,sy1xx-mac`](../../../../build/dts/api/bindings/ethernet/sensry%2Csy1xx-mac.md#std-dtcompatible-sensry-sy1xx-mac) |
| GPIO & Headers | on-chip | Sensry SY1XX GPIO Port[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L146) | [`sensry,sy1xx-gpio`](../../../../build/dts/api/bindings/gpio/sensry%2Csy1xx-gpio.md#std-dtcompatible-sensry-sy1xx-gpio) |
| I2C | on-chip | Sensry SY1XX I2C Driver node[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L96) | [`sensry,sy1xx-i2c`](../../../../build/dts/api/bindings/i2c/sensry%2Csy1xxx-i2c.md#std-dtcompatible-sensry-sy1xx-i2c) |
| Interrupt controller | on-chip | Sensry sy1xx event unit[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L49) | [`sensry,sy1xx-event-unit`](../../../../build/dts/api/bindings/interrupt-controller/sy1xx%2Cevent-unit.md#std-dtcompatible-sensry-sy1xx-event-unit) |
| MDIO | on-chip | Sensry SY1XX MDIO Driver node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L162) | [`sensry,sy1xx-mdio`](../../../../build/dts/api/bindings/mdio/sensry%2Csy1xx-mdio.md#std-dtcompatible-sensry-sy1xx-mdio) |
| Pin control | on-chip | Sensry SY1xx Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L156) | [`sensry,sy1xx-pinctrl`](../../../../build/dts/api/bindings/pinctrl/sensry%2Csy1xx-pinctrl.md#std-dtcompatible-sensry-sy1xx-pinctrl) |
| RNG | on-chip | Sensry SY1XX TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L140) | [`sensry,sy1xx-trng`](../../../../build/dts/api/bindings/rng/sensry%2Csy1xx-trng.md#std-dtcompatible-sensry-sy1xx-trng) |
| Serial controller | on-chip | Sensry SY1xx UART[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L72) | [`sensry,sy1xx-uart`](../../../../build/dts/api/bindings/serial/sensry%2Csy1xx-uart.md#std-dtcompatible-sensry-sy1xx-uart) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L29) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | Sensry ganymed timer peripheral[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L56) | [`sensry,sy1xx-sys-timer`](../../../../build/dts/api/bindings/timer/sy1xx%2Csys-timer.md#std-dtcompatible-sensry-sy1xx-sys-timer) |

#### `ganymed_bob/sy120_gen1` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | Sensry Ganymed SY1xx Core CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L20) | [`sensry,sy1xx`](../../../../build/dts/api/bindings/cpu/sensry%2Cganymed-sy1xx.md#std-dtcompatible-sensry-sy1xx) |
| Ethernet | on-board | Single Port Gigabit Ethernet Copper PHY with GMII/RGMII/MII/RMII Interfaces[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sensry/ganymed_bob/ganymed_bob_sy120_gen1.dts?plain=1#L28) | [`microchip,vsc8541`](../../../../build/dts/api/bindings/ethernet/phy/microchip%2Cvsc8541-phy.md#std-dtcompatible-microchip-vsc8541) |
| on-chip | This file needs to be included by devices that need to specify a set of pin controller states[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L173) | [`sensry,sy1xx-mac`](../../../../build/dts/api/bindings/ethernet/sensry%2Csy1xx-mac.md#std-dtcompatible-sensry-sy1xx-mac) |
| GPIO & Headers | on-chip | Sensry SY1XX GPIO Port[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L146) | [`sensry,sy1xx-gpio`](../../../../build/dts/api/bindings/gpio/sensry%2Csy1xx-gpio.md#std-dtcompatible-sensry-sy1xx-gpio) |
| I2C | on-chip | Sensry SY1XX I2C Driver node[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L96) | [`sensry,sy1xx-i2c`](../../../../build/dts/api/bindings/i2c/sensry%2Csy1xxx-i2c.md#std-dtcompatible-sensry-sy1xx-i2c) |
| Interrupt controller | on-chip | Sensry sy1xx event unit[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L49) | [`sensry,sy1xx-event-unit`](../../../../build/dts/api/bindings/interrupt-controller/sy1xx%2Cevent-unit.md#std-dtcompatible-sensry-sy1xx-event-unit) |
| MDIO | on-chip | Sensry SY1XX MDIO Driver node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L162) | [`sensry,sy1xx-mdio`](../../../../build/dts/api/bindings/mdio/sensry%2Csy1xx-mdio.md#std-dtcompatible-sensry-sy1xx-mdio) |
| Pin control | on-chip | Sensry SY1xx Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L156) | [`sensry,sy1xx-pinctrl`](../../../../build/dts/api/bindings/pinctrl/sensry%2Csy1xx-pinctrl.md#std-dtcompatible-sensry-sy1xx-pinctrl) |
| RNG | on-chip | Sensry SY1XX TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L140) | [`sensry,sy1xx-trng`](../../../../build/dts/api/bindings/rng/sensry%2Csy1xx-trng.md#std-dtcompatible-sensry-sy1xx-trng) |
| Serial controller | on-chip | Sensry SY1xx UART[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L72) | [`sensry,sy1xx-uart`](../../../../build/dts/api/bindings/serial/sensry%2Csy1xx-uart.md#std-dtcompatible-sensry-sy1xx-uart) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L29) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | Sensry ganymed timer peripheral[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/sensry/ganymed-sy1xx.dtsi?plain=1#L56) | [`sensry,sy1xx-sys-timer`](../../../../build/dts/api/bindings/timer/sy1xx%2Csys-timer.md#std-dtcompatible-sensry-sy1xx-sys-timer) |

For more detailed description please refer to [Ganymed BreakOut Board Documentation](https://docs.sensry.net/datasheets/sy120-bob/) [[1]](#id2)

## Programming and Testing

The `ganymed_bob` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |
| **sy1xx** | ✅ (default) |  |

### Building

Applications for the `ganymed_bob/sy120_gbm` board can be
built and flashed in the usual way. See
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details on
building and running.

Building the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample:

```shell
west build -b ganymed_bob/sy120_gbm samples/hello_world
```

### Flashing

Test the Ganymed with a [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample.

Flash the zephyr image:

```shell
west build -b None --serial /dev/ttyUSB0 samples/hello_world
west flash
```

### Testing

Then attach a serial console, ex. minicom / picocom / putty; Reset the target.
The sample output should be:

```shell
Hello World! ganymed_bob/sy120_gbm
```

## References

[[1](#id3)]

[https://docs.sensry.net/datasheets/sy120-bob/](https://docs.sensry.net/datasheets/sy120-bob/)

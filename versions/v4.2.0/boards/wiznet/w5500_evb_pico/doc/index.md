---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/wiznet/w5500_evb_pico/doc/index.html
original_path: boards/wiznet/w5500_evb_pico/doc/index.html
---

# W5500-EVB-Pico

Board Overview

[![../../../../_images/w5500_evb_pico_side.png](../../../../_images/w5500_evb_pico_side.png)
](../../../../_images/w5500_evb_pico_side.png)

W5500-EVB-Pico

Name:
:   `w5500_evb_pico`

Vendor:
:   WIZnet Co., Ltd.

Architecture:
:   arm

SoC:
:   rp2040

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/wiznet/w5500_evb_pico/doc/index.rst/../..)

## Overview

W5500-EVB-Pico is a microcontroller evaluation board based on the Raspberry
Pi RP2040 and fully hardwired TCP/IP controller W5500 - and basically works
the same as Raspberry Pi Pico board but with additional Ethernet via W5500.
The USB bootloader allows the ability to flash without any adapter, in a
drag-and-drop manner. It is also possible to flash and debug the boards with
their SWD interface, using an external adapter.

## Hardware

- Dual core Arm Cortex-M0+ processor running up to 133MHz
- 264KB on-chip SRAM
- 16MB on-board QSPI flash with XIP capabilities
- 26 GPIO pins
- 3 Analog inputs
- 2 UART peripherals
- 2 SPI controllers
- 2 I2C controllers
- 16 PWM channels
- USB 1.1 controller (host/device)
- 8 Programmable I/O (PIO) for custom peripherals
- On-board LED
- 1 Watchdog timer peripheral
- Wiznet W5500 Ethernet MAC/PHY

### Supported Features

The `w5500_evb_pico` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Pin Mapping

The peripherals of the RP2040 SoC can be routed to various pins on the board.
The configuration of these routes can be modified through DTS. Please refer to
the datasheet to see the possible routings for each peripheral.

External pin mapping on the W5500\_EVB\_PICO is identical to the Raspberry Pi
Pico. Since GPIO 25 is routed to the on-board LED on, similar to the Raspberry
Pi Pico, the blinky example works as intended. The W5500 is routed to the SPI0
(P16-P19), with the reset and interrupt signal for the W5500 routed to P20 and
P21, respectively. All of these are shared with the edge connector on the
board.

Refer to [W55500 Evaluation Board Documentation](https://docs.wiznet.io/Product/iEthernet/W5500/w5500-evb-pico) [[1]](#id2) for a board schematic and
other certifications.

#### Default Zephyr Peripheral Mapping:

- UART0\_TX : P0
- UART0\_RX : P1
- I2C0\_SDA : P4
- I2C0\_SCL : P5
- I2C1\_SDA : P14
- I2C1\_SCL : P15
- SPI0\_RX : P16
- SPI0\_CSN : P17
- SPI0\_SCK : P18
- SPI0\_TX : P19
- W5500 Reset : P20
- W5500 Interrupt : P21
- ADC\_CH0 : P26
- ADC\_CH1 : P27
- ADC\_CH2 : P28
- ADC\_CH3 : P29

## Programming and Debugging

The `w5500_evb_pico` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

The overall explanation regarding flashing and debugging is the same as or [Raspberry Pi Pico](../../../raspberrypi/rpi_pico/doc/index.md#rpi_pico).
See [Programming and Debugging](../../../raspberrypi/rpi_pico/doc/index.md#rpi-pico-programming-and-debugging) in [Raspberry Pi Pico](../../../raspberrypi/rpi_pico/doc/index.md#rpi_pico) documentation. N.b. OpenOCD support requires using Raspberry Pi’s forked version of OpenOCD.

Below is an example of building and flashing the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b w5500_evb_pico samples/basic/blinky
west flash --openocd /usr/local/bin/openocd
```

[[1](#id3)]

[https://docs.wiznet.io/Product/iEthernet/W5500/w5500-evb-pico](https://docs.wiznet.io/Product/iEthernet/W5500/w5500-evb-pico)

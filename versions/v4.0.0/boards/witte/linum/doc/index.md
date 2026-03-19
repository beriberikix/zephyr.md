---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/witte/linum/doc/index.html
original_path: boards/witte/linum/doc/index.html
---

# Linum Board

Board Overview

[![../../../../_images/linum-stm32h753bi-top.jpg](../../../../_images/linum-stm32h753bi-top.jpg)
](../../../../_images/linum-stm32h753bi-top.jpg)

Linum Board

Vendor:
:   Witte Technology

Architecture:
:   arm

SoC:
:   stm32h753xx

## Overview

Linum is a development board released by Witte Tenology in 2023, and it was developed around the
STM32H753BI microcontroller. The board has 2 expansion connectors used by the LCD display with
touchscreen and another for access to other peripherals of microcontroller. Also it brings plenty
of communications interfaces like UART with RS232 and RS485 capabillities, CAN bus compatible to
FD standard, and networking over Ethernet.

## Hardware

The board features:
:   - 8 to 52V power supply
    - SWD Pins for use as STLink (Pin header) and TC2030-IDC 6-Pin Tag-Connect Plug-of-Nails™ Connector
    - Crystal for HS 25MHz
    - Crystal for RTC 32.768KHz
    - 1 UART serial for debug
    - 1 Led RGB
    - 1 Buzzer without internal oscillator
    - 1 Mono audio up to 3W
    - 1 Ethernet 10/100
    - 1 MicroSD connector supporting 1 or 4-bit bus
    - 1 USB 2.0 Host/Device
    - 1 EEPROM memory with 512K bits
    - 1 External SRAM memory with 8MB
    - 1 NOR memory with 16MB
    - 2 On-board RS232 Transceiver with RTS/CTS
    - 2 On-board RS485 Transceiver
    - 2 On-board CAN-FD Transceiver

Expansion connector 1 features:
:   - 1 Display RBG 888
    - 1 Capacitive Touchscreen sensor

Expansion connector 2 features.
:   - 1 SPI
    - 1 I2C
    - 1 One Wire
    - 2 DACs
    - 6 PWM Channels
    - 10 ADCs

More information about the board, can be found at the [Witte Linum website](https://wittetech.com/).

### Supported Features

The Zephyr Linum board configuration supports the following hardware
features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| RTC | on-chip | counter |
| I2C | on-chip | i2c |
| PWM | on-chip | pwm |
| ADC | on-chip | adc |
| RNG | on-chip | True Random number generator |
| ETHERNET | on-chip | ethernet |
| SPI | on-chip | spi |
| USB | on-chip | usb\_device |
| CAN/CANFD | on-chip | canbus |
| LTDC | on-chip | LCD Interface |
| FMC | on-chip | memc (SDRAM) |
| SDMMC | on-chip | disk access |

Other hardware features are not yet supported on this Zephyr port.

The default configuration can be found in the defconfig file:
[boards/witte/linum/linum\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/witte/linum/linum_defconfig)

#### Default Zephyr Peripheral Mapping:

#### BOARD-LEDs

The LINUM-STM32H753BI has 3 software controllable LEDs.

> | LED RGB | PINS |
> | --- | --- |
> | LED\_R | PG2 |
> | LED\_G | PG3 |
> | LED\_B | PB2 |

#### UART/USART

The LINUM-STM32H753BI used the USART1 for serial console.

#### USART1

> | USART1 | PINS |
> | --- | --- |
> | TX | PB14 |
> | RX | PB15 |

The LINUM-STM32H753BI board has two on-board RS-232 transceiver connected to USART2 and USART3.

> | USART2 | PINS |
> | --- | --- |
> | TXD | PD5 |
> | RXD | PD6 |
> | CTS | PD3 |
> | RTS | PD4 |
>
> | USART3 | PINS |
> | --- | --- |
> | TXD | PB10 |
> | RXD | PB11 |
> | CTS | PD11 |
> | RTS | PD12 |

The LINUM-STM32H753BI board has two on-board RS-485 transceiver connected to USART4 and USART6.

> | UART4 | PINS |
> | --- | --- |
> | TXD | PB9 |
> | RXD | PB8 |
> | DE | PA15 |
>
> | USART6 | PINS |
> | --- | --- |
> | TXD | PC6 |
> | RXD | PC7 |
> | DE | PG12 |

#### SDMMC

The LINUM-STM32H753BI has one SDCard slot connected as below:

> | SDMMC1 | PINS |
> | --- | --- |
> | SDMMC\_D0 | PC8 |
> | SDMMC\_D1 | PC9 |
> | SDMMC\_D2 | PC10 |
> | SDMMC\_D3 | PC11 |
> | SDMMC\_DK | PC12 |
>
> | GPIO | PINS |
> | --- | --- |
> | SDCARD\_DETECTED | PG7 |
> | SDCARD\_PWR\_EN | PD7 |

#### ETHERNET

The LINUM-STM32H753BI has a ethernet connection using the transceiver KSZ8081RNACA.

> | ETH | PINS |
> | --- | --- |
> | ETH\_REF\_CLK | PA1 |
> | ETH\_MDIO | PA2 |
> | ETH\_CRS\_DV | PA7 |
> | ETH\_MDC | PC1 |
> | ETH\_RXD0 | PC4 |
> | ETH\_RXD1 | PC5 |
> | ETH\_TX\_EN | PG11 |
> | ETH\_TXD0 | PG13 |
> | ETH\_TXD1 | PG14 |
> | ETH\_CLK | PA8 |
> | ETH\_RESET | PI4 |

#### CAN-FD

The LINUM-STM32H753BI board has two on-board CAN-FD transceiver connected to FDCAN1 and FDCAN2.

> | FDCAN1 | PINS |
> | --- | --- |
> | TXD | PH13 |
> | RXD | PH14 |
> | STD | PI2 |
>
> | FDCAN2 | PINS |
> | --- | --- |
> | TXD | PB13 |
> | RXD | PB12 |
> | STD | PE3 |

#### USB

The LINUM-STM32H753BI has one usb port.

> | USB | PINS |
> | --- | --- |
> | USB\_VBUS | PA9 |
> | USB\_N | PA11 |
> | USB\_P | PA12 |
> | USB\_EN | PI12 |
> | USB\_FLT | PI13 |

#### I2C3

The LINUM-STM32H753BI connects the EEPROM memory and the touchscreen sensor to I2C3.

> | I2C3 | PINS |
> | --- | --- |
> | SCL | PH7 |
> | SDA | PH8 |

#### External SDRAM

The LINUM-STM32H753BI has a external SDRAM with 8Mbytes connected to FMC peripheral.

> | FMC | PINS |
> | --- | --- |
> | FMC\_A0 | PF0 |
> | FMC\_A1 | PF1 |
> | FMC\_A2 | PF2 |
> | FMC\_A3 | PF3 |
> | FMC\_A4 | PF4 |
> | FMC\_A5 | PF5 |
> | FMC\_A6 | PF12 |
> | FMC\_A7 | PF13 |
> | FMC\_A8 | PF14 |
> | FMC\_A9 | PF15 |
> | FMC\_A10 | PG0 |
> | FMC\_A11 | PG1 |
> | FMC\_BA0 | PG4 |
> | FMC\_BA1 | PG5 |
> | FMC\_D0 | PD14 |
> | FMC\_D1 | PD15 |
> | FMC\_D2 | PD0 |
> | FMC\_D3 | PD1 |
> | FMC\_D4 | PE7 |
> | FMC\_D5 | PE8 |
> | FMC\_D6 | PE9 |
> | FMC\_D7 | PE10 |
> | FMC\_D8 | PE11 |
> | FMC\_D9 | PE12 |
> | FMC\_D10 | PE13 |
> | FMC\_D11 | PE14 |
> | FMC\_D12 | PE15 |
> | FMC\_D13 | PD8 |
> | FMC\_D14 | PD9 |
> | FMC\_D15 | PD10 |
> | FMC\_NBL0 | PE0 |
> | FMC\_NBL1 | PE1 |
> | FMC\_SDCKE0 | PC3 |
> | FMC\_SDCLK | PG8 |
> | FMC\_SDNCAS | PG15 |
> | FMC\_SDNEO | PC2 |
> | FMC\_SDNRAS | PF11 |
> | FMC\_SDNWE | PC0 |

#### LCD

The LINUM-STM32H753BI use the LTDC to support one LCD with RGB connection.

> | LTDC | PINS |
> | --- | --- |
> | LTDC\_B0 | PJ12 |
> | LTDC\_B1 | PJ13 |
> | LTDC\_B2 | PJ14 |
> | LTDC\_B3 | PJ15 |
> | LTDC\_B4 | PK3 |
> | LTDC\_B5 | PK4 |
> | LTDC\_B6 | PK5 |
> | LTDC\_B7 | PK6 |
> | LTDC\_CLK | PI14 |
> | LTDC\_DE | PK7 |
> | LTDC\_G0 | PJ7 |
> | LTDC\_G1 | PJ8 |
> | LTDC\_G2 | PJ9 |
> | LTDC\_G3 | PJ10 |
> | LTDC\_G4 | PJ11 |
> | LTDC\_G5 | PK0 |
> | LTDC\_G6 | PK1 |
> | LTDC\_G7 | PK2 |
> | LTDC\_HSYNC | PI10 |
> | LTDC\_R0 | PI15 |
> | LTDC\_R1 | PJ0 |
> | LTDC\_R2 | PJ1 |
> | LTDC\_R3 | PJ2 |
> | LTDC\_R4 | PJ3 |
> | LTDC\_R5 | PJ4 |
> | LTDC\_R6 | PJ5 |
> | LTDC\_R7 | PJ6 |
> | LTDC\_VSYNC | PI9 |
> | PWM\_BACKLIGHT | PH6 |

#### System Clock

Linum H753ZI System Clock could be driven by an internal or external
oscillator, as well as the main PLL clock. By default, the System clock is
driven by the PLL clock at 480MHz, driven by an 25MHz high-speed external clock.

## Programming and Debugging

Applications for the `linum` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Note

For debugging or programming Linum you will need to use an external debug
debug or flash tool and connect it to the SWD Connnector. JLink or ST-Link
probes are examples of out of the box compatible tools.

### Flashing

#### Flashing an application to the Linum board

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Run a serial host program to connect with your Nucleo board.

```shell
$ minicom -b 115200 -D /dev/ttyACM0
```

Build and flash the application:

```shell
# From the root of the zephyr repository
west build -b linum samples/hello_world
west flash
```

You should see the following message on the console:

```shell
$ Hello World! linum
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b linum samples/hello_world
west debug
```

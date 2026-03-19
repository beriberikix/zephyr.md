---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/olimex/olimexino_stm32/doc/index.html
original_path: boards/olimex/olimexino_stm32/doc/index.html
---

# OLIMEXINO-STM32

Board Overview

[![../../../../_images/olimexino_stm32.jpg](../../../../_images/olimexino_stm32.jpg)
](../../../../_images/olimexino_stm32.jpg)

OLIMEXINO-STM32

Name:
:   `olimexino_stm32`

Vendor:
:   OLIMEX Ltd.

Architecture:
:   arm

SoC:
:   stm32f103xb

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/olimex/olimexino_stm32/doc/index.rst/../..)

## Overview

The OLIMEXINO-STM32 board is based on the STMicroelectronics STM32F103RB ARM
Cortex-M3 CPU.

More information about the board can be found at the
[OLIMEXINO-STM32 website](https://www.olimex.com/Products/Duino/STM32/OLIMEXINO-STM32/) and [OLIMEXINO-STM32 user manual](https://www.olimex.com/Products/Duino/STM32/OLIMEXINO-STM32/resources/OLIMEXINO-STM32.pdf).
The [ST STM32F103xB Datasheet](https://www.st.com/resource/en/datasheet/stm32f103tb.pdf) contains the processor’s
information and the datasheet.

### Supported Features

The `olimexino_stm32` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Pin Mapping

![OLIMEXINO-STM32 connectors](../../../../_images/olimexino-stm32-front.jpg)

OLIMEXINO-STM32 connectors

#### LED

- LED1 (green) = PA5
- LED2 (yellow) = PA1
- PWR\_LED (red) = power

#### Push buttons

- BUT = PC9 / TIM3CH4 / BOOT0
- RST = NRST

#### External Connectors

SWD

| PIN # | Signal Name | STM32F103RB Functions |
| --- | --- | --- |
| 1 | VCC | N/A |
| 2 | TMS / SWDIO | JTMS / SWDIO / PA13 |
| 3 | GND | N/A |
| 4 | TCK / SWCLK | JTCK / SWCLK / PA14 |
| 5 | GND | N/A |
| 6 | TDO / SWO | JTDO /TIM2\_CH2 / PB3 / TRACESWO / SPI1\_SCK |
| 7 | Cut off | N/A |
| 8 | TDI | JTDI / TIM2\_CH1\_ETR / PA15 / SPI1\_NSS |
| 9 | GND | N/A |
| 10 | RESET | NRST |

UEXT

| PIN # | Signal Name | STM32F103RB Functions |
| --- | --- | --- |
| 1 | VCC | N/A |
| 2 | GND | N/A |
| 3 | D7 (TXD1) | PA9 / USART1\_TX / TIM1\_CH2 |
| 4 | D8 (RXD1) | PA10 / USART1\_RX / TIM1\_CH3 |
| 5 | D29 (SCL2) | PB10 / I2C2\_SCL / USART3\_TX / TIM2\_CH3 |
| 6 | D30 (SDA2) | PB11 / I2C2\_SDA / USART3\_RX / TIM2\_CH4 |
| 7 | D12 (MISO1) | PA6 / SPI1\_MISO / ADC12\_IN6 / TIM3\_CH1 / TIM1\_BKIN |
| 8 | D11 (MOSI1) | PA7 / SPI1\_MOSI / ADC12\_IN7 / TIM3\_CH2 / TIM1\_CH1N |
| 9 | D13 (SCK / LED1) | PA5 / SPI1\_SCK / ADC12\_IN5 |
| 10 | UEXT\_#CS | N/A |

EXT

| PIN # | Signal Name | STM32F103RB Functions |
| --- | --- | --- |
| 1 | D23\_EXT | PC15 / OSC32\_OUT |
| 2 | D24 (CANTX) | PB9 / TIM4\_CH4 / I2C1\_SDA / CANTX |
| 3 | D25 (MMC\_CS) | PD2 / TIM3\_ETR |
| 4 | D26 | PC10 / USART3\_TX |
| 5 | D27 | PB0 / ADC12\_IN8 / TIM3\_CH3 / TIM1\_CH2N |
| 6 | D28 | PB1 / ADC12\_IN9 / TIM3\_CH4 / TIM1\_CH3N |
| 7 | D29 (SCL2) | PB10 / I2C2\_SCL / USART3\_TX / TIM2\_CH3 |
| 8 | D30 (SDA2) | PB11 / I2C2\_SDA / USART3\_RX / TIM2\_CH4 |
| 9 | D31 (#SS2) | PB12 / SPI2\_NSS / I2C2\_SMBAI / USART3\_CK / TIM1\_BKIN |
| 10 | D32 (SCK2) | PB13 / SPI2\_SCK/ USART3\_CTS / TIM1\_CH1N |
| 11 | D33 (MISO2) | PB14 / SPI2\_MISO / USART3\_RTS / TIM1\_CH2N |
| 12 | D34 (MOSI2) | PB15 / SPI2\_MOSI / TIM1\_CH3N |
| 13 | D35 | PC6 / TIM3\_CH1 |
| 14 | D36 | PC7 / TIM3\_CH2 |
| 15 | D37 | PC8 / TIM3\_CH3 |
| 16 | GND | N/A |

#### Arduino Headers

CON1 power

| PIN # | Signal Name | STM32F103RB Functions |
| --- | --- | --- |
| 1 | RESET | NRST |
| 2 | VCC (3V3) | N/A |
| 3 | VDD (3V3A) | N/A |
| 4 | GND | N/A |
| 5 | GND | N/A |
| 6 | VIN | N/A |

CON2 analog

| PIN # | Signal Name | STM32F103RB Functions |
| --- | --- | --- |
| 1 | D15 (A0) | PC0 / ADC12\_IN10 |
| 2 | D16 (A1) | PC1 / ADC12\_IN11 |
| 3 | D17 (A2) | PC2 / ADC12\_IN12 |
| 4 | D18 (A3) | PC3 / ADC12\_IN13 |
| 5 | D19 (A4) | PC4 / ADC12\_IN14 |
| 6 | D20 (A5) | PC5 / ADC12\_IN15 |

CON3 digital

| PIN # | Signal Name | STM32F103RB Functions |
| --- | --- | --- |
| 1 | D0 (RXD2) | PA3 / USART2\_RX / ADC12\_IN3 / TIM2\_CH4 |
| 2 | D1 (TXD2) | PA2 / USART2\_TX / ADC12\_IN2 / TIM2\_CH3 |
| 3 | D2 | PA0 / WKUP / USART2\_CTS / ADC12\_IN0 / TIM2\_CH1 |
| 4 | D3 (LED2) | PA1 / USART2\_RTS / ADC12\_IN1 / TIM2\_CH2 |
| 5 | D4 | PB5 / I2C1\_SMBAI / TIM3\_CH2 / SPI1\_MOSI |
| 6 | D5 | PB6 / I2C1\_SCL / TIM4\_CH1 / USART1\_TX |
| 7 | D6 | PA8 / USART1\_CK / TIM1\_CH1 / MCO |
| 8 | D7 (TXD1) | PA9 / USART1\_TX / TIM1\_CH2 |

CON4 digital

| PIN # | Signal Name | STM32F103RB Functions |
| --- | --- | --- |
| 1 | D8 (RXD1) | PA10 / USART1\_RX / TIM1\_CH3 |
| 2 | D9 | PB7 / I2C1\_SDA / TIM4\_CH2 / USART1\_RX |
| 3 | D10 (#SS1) | PA4 / SPI1\_NSS / USART2\_CK / ADC12\_IN4 |
| 4 | D11 (MOSI1) | PA7 / SPI1\_MOSI / ADC12\_IN7 / TIM3\_CH2 / TIM1\_CH1N |
| 5 | D12 (MISO1) | PA6 / SPI1\_MISO / ADC12\_IN6 / TIM3\_CH1 / TIM1\_BKIN |
| 6 | D13 (SCK1 / LED1) | PA5 / SPI1\_SCK / ADC12\_IN5 |
| 7 | GND | N/A |
| 8 | D14 (CANRX) | PB8 / TIM4\_CH3 / I2C1\_SCL / CANRX |

CAN

| PIN # | Signal Name |
| --- | --- |
| 1 | GND |
| 2 | CAN L |
| 3 | CAN H |

### System Clock

OLIMEXINO-STM32 has two external oscillators. The frequency of
the slow clock is 32.768 kHz. The frequency of the main clock
is 8 MHz. The processor can setup HSE to drive the master clock,
which can be set as high as 72 MHz.

### Serial Port

OLIMEXINO-STM32 board has up to 3 U(S)ARTs. The Zephyr console output is
assigned to USART1. Default settings are 115200 8N1.

### SPI

OLIMEXINO-STM32 board has up to 2 SPIs. The default SPI mapping for Zephyr is:

- SPI1\_NSS : PA4
- SPI1\_SCK : PA5
- SPI1\_MISO : PA6
- SPI1\_MOSI : PA7

### I2C

The OLIMEXINO-STM32 board supports two I2C devices. The default I2C mapping for
Zephyr is:

- I2C1\_SCL : PB6
- I2C1\_SDA : PB7
- I2C2\_SCL : PB10
- I2C2\_SDA : PB11

### USB

OLIMEXINO-STM32 board has a USB 2.0 full-speed device interface available
through its mini USB connector.

- USB\_DM : PA11
- USB\_DP : PA12

### CAN

OLIMEXINO-STM32 board has a CAN interface with transceiver on board.
CAN is accessible through a screw terminal.

- CAN\_RX : PB8
- CAN\_TX : PB9

### Jumpers

The Zephyr kernel uses the OLIMEXINO-STM32 default jumper
settings. Note that all jumpers on the board are SMD type.
You will need to solder, unsolder, or cut them in order to
reconfigure them.

The default jumper settings for the OLIMEXIMO-STM32E are:

| Jumper Name | Open | Close |
| --- | --- | --- |
| LED1\_E |  | x |
| LED2\_E |  | x |
| D23\_E | x |  |
| R-T | x |  |
| P10\_E |  | x |

| Jumper Name | D10 | D4 |
| --- | --- | --- |
| D10/D4 |  | x |

## Flashing Zephyr onto OLIMEXINO-STM32

Flashing the Zephyr kernel onto OLIMEXINO-STM32 requires the
[stm32flash tool](https://sourceforge.net/p/stm32flash/wiki/Home/).

### Building stm32flash command line tool

To build the stm32flash tool, follow the steps below:

1. Checkout the stm32flash tool’s code from the repository.

> ```shell
> $ git clone http://git.code.sf.net/p/stm32flash/code stm32flash
> $ cd stm32flash
> ```

1. Build the stm32flash tool.

> ```shell
> $ make
> ```

1. The resulting binary is available at `stm32flash`.

### Flashing an Application to OLIMEXINO-STM32

To upload an application to the OLIMEXINO-STM32 board a TTL(3.3V)
serial adapter is required. This tutorial uses the
[Button](../../../../samples/basic/button/README.md#button "Handle GPIO inputs with interrupts.") sample application.

1. Connect the serial cable to the UEXT lines of the UART
   interface (pin #3=TX and pin #4=RX).
2. Power the OLIMEXINO-STM32 via the mini USB.
3. Reset the board while holding the button (BUT).
4. To build the application and flash it, enter:

   ```shell
   # From the root of the zephyr repository
   west build -b olimexino_stm32 samples/basic/button
   west flash
   ```
5. Run your favorite terminal program to listen for output.

   ```shell
   $ minicom -D /dev/ttyUSB0 -b 115200
   ```

   The `-b` option sets baud rate ignoring the value
   from config.
6. Press the Reset button and you should see the output of
   button application in your terminal. The state of the BUT
   button’s GPIO line is monitored and printed to the serial
   console. When the input button gets pressed, the interrupt
   handler prints information about this event along with its
   timestamp.

Note

Make sure your terminal program is closed before flashing
the binary image, or it will interfere with the flashing
process.

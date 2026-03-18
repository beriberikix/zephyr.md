---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/olimex_stm32_p405/doc/index.html
original_path: boards/arm/olimex_stm32_p405/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# OLIMEX-STM32-P405

## Overview

The OLIMEX-STM32-P405 board is based on the STMicroelectronics STM32F405RG ARM
Cortex-M4 CPU.

![OLIMEX-STM32-P405](../../../../_images/olimex_stm32_p405.jpg)

OLIMEX-STM32-P405

## Hardware

Information about the board can be found at the
[OLIMEX-STM32-P405 website](https://www.olimex.com/Products/ARM/ST/STM32-P405/) and [OLIMEX-STM32-P405 user manual](https://www.olimex.com/Products/ARM/ST/STM32-P405/resources/STM32-P405_UM.pdf).
The [ST STM32F405RG Datasheet](https://www.st.com/resource/en/reference_manual/dm00031020.pdf) contains the processor’s
information and the datasheet.

### Supported Features

The olimex\_stm32\_p405 board configuration supports the following
hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vectored interrupt controller |
| SYSTICK | on-chip | system clock |
| UART | on-chip | serial port |
| GPIO | on-chip | gpio |

Other hardware features have not been enabled yet for this board.

### Pin Mapping

![OLIMEX-STM32-P405 connectors](../../../../_images/olimex-stm32-p405-front.jpg)

OLIMEX-STM32-P405 connectors

#### LED

- USER\_LED (red) = PC12
- PWR\_LED (red) = power

#### Push buttons

- USER\_BUTTON = PA0
- RST = NRST

#### External Connectors

JTAG debug

| PIN # | Signal Name | Pin # | Signal Name |
| --- | --- | --- | --- |
| 1 | +3.3V | 11 |  |
| 2 | +3.3V | 12 | GND |
| 3 | PB4 / TRST | 13 | PB3 / TDO |
| 4 | GND | 14 | GND |
| 5 | PA15 / TDI | 15 | PB4 / TRST |
| 6 | GND | 16 | GND |
| 7 | PA13 / TMS | 17 |  |
| 8 | GND | 18 | GND |
| 9 | PA14 / TCK | 19 | +5V\_JTAG |
| 10 | GND | 20 | GND |

UEXT

| PIN # | Wire Name | STM32F405 port |
| --- | --- | --- |
| 1 | +3.3V |  |
| 2 | GND |  |
| 3 | PA9/USART1\_TX | PA9 |
| 4 | PA10/USART1\_RX | PA10 |
| 5 | PB6/I2C1\_SCL | PB6 |
| 6 | PB7/I2C1\_SDA | PB7 |
| 7 | PA6/SPI1\_MISO | PA6 |
| 8 | PA7/SPI1\_MOSI | PA7 |
| 9 | PA5/SPI1\_SCK | PA5 |
| 10 | PA4/SPI1\_NSS | PA4 |

GPIO row of pins

| Pin | STM32F405 Pin Functions |
| --- | --- |
| 3V3 | N/A |
| PA1 | PA1/USART2\_RTS/ADC1/TIM2\_CH2 |
| PA8 | PA8/USART1\_CK/TIM1\_CH1/MCO |
| PB0 | PB0/ADC8/TIM3\_CH3/TIM1\_CH2N |
| PB1 | PB1/ADC9/TIM3\_CH4/TIM1\_CH3N |
| PB2 | PB2/BOOT1 |
| PB5 | PB5/I2C1\_SMBAI/TIM3\_CH2/SPI1\_MOSI |
| PB8 | PB8/TIM4\_CH3/I2C1\_SCL/CANRX |
| PB9 | PB9/TIM4\_CH4/I2C1\_SDA/CANTX |
| VDDA | N/A |
| GNDA | N/A |
| PB10 | PB10/I2C2\_SCL/USART3\_TX/TIM2\_CH3 |
| PB11 | PB11/I2C2\_SDA/USART3\_RX/TIM2\_CH4 |
| PB12 | PB12/SPI2\_NSS/I2C2\_SMBAL/USART3\_CK/TIM1\_BKIN |
| PB13 | PB13/SPI2\_SCK/USART3\_CTS/TIM1\_CH1N |
| PB14 | PB14/SPI2\_MISO/USART3\_RTS/TIM1\_CH2N |
| PB15 | PB15/SPI2\_MOSI/TIM1\_CH3N |
| RST | NRST |
| PC0 | PC0/ADC10 |
| PC1 | PC1/ADC11 |
| PC2 | PC2/ADC12 |
| PC3 | PC3/ADC13 |
| PC4 | PC4/ADC14 |
| PC5 | PC5/ADC15 |
| PC6 | PC6/TIM3\_CH1 |
| PC7 | PC7/TIM3\_CH2 |
| PC8 | PC8/TIM3\_CH3 |
| PC9 | PC9/TIM3\_CH4 |
| PC10 | PC10/USART3\_TX |
| PC12 | PC12/USART3\_CK |
| PC13 | PC13/ANTI\_TAMP |
| PD2 | PD2/TIM3\_ETR |
| +5V\_USB | N/A |
| VIN | N/A |
| GND | N/A |

### System Clock

OLIMEX-STM32-P405 has two external oscillators. The frequency of
the slow clock is 32.768 kHz. The frequency of the main clock
is 8 MHz. The processor can setup HSE to drive the master clock,
which can be set as high as 168 MHz.

## Programming and Debugging

The OLIMEX-STM32-P405 board does not include an embedded debug tool
interface. You will need to use ST tools or an external JTAG probe.
In the following examples a ST-Link V2 USB dongle is used.

### Flashing an application to the Olimex-STM32-P405

The sample application [Hello World](../../../../samples/hello_world/README.md#hello-world) is being used in this tutorial.

Connect the ST-Link USB dongle to your host computer and to the JTAG port of
the OLIMEX-STM32-P405 board.

Now build and flash the application.

```shell
# From the root of the zephyr repository
west build -b olimex_stm32_p405 samples/hello_world
west flash
```

Run a serial host program to connect with your board:

```shell
$ minicom -D /dev/ttyACM0
```

After resetting the board, you should see the following message:

```shell
***** BOOTING ZEPHYR OS v1.8.99 - BUILD: Aug  4 2017 14:54:40 *****
Hello World! arm
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b olimex_stm32_p405 samples/hello_world
west debug
```

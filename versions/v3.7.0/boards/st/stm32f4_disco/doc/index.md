---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/st/stm32f4_disco/doc/index.html
original_path: boards/st/stm32f4_disco/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# ST STM32F4 Discovery

## Overview

The STM32F4DISCOVERY Discovery kit features an ARM Cortex-M4 based STM32F407VG MCU
with a wide range of connectivity support and configurations Here are
some highlights of the STM32F4DISCOVERY board:

- STM32 microcontroller in LQFP100 package
- Extension header for all LQFP100 I/Os for quick connection to prototyping board and easy probing
- On-board ST-LINK/V2 debugger/programmer with SWD connector
- Flexible board power supply:

  > - USB VBUS or external source(3.3V, 5V, 7 - 12V)
  > - Power management access point
- Eight LEDs:

  > - USB communication (LD1)
  > - 3.3 V power on (LD2)
  > - Four user LEDs: orange (LD3), green (LD4), red (LD5), and blue (LD6)
  > - 2 USB OTG LEDs for VBUS (LD7) and over-current (LD8)
- Two push-buttons: USER and RESET
- USB OTG FS with micro-AB connector
- LIS302DL or LIS3DSH ST MEMS 3-axis accelerometer
- MP45DT02 ST-MEMS audio sensor omni-directional digital microphone
- CS43L22 audio DAC with integrated class D speaker driver

![STM32F4DISCOVERY](../../../../_images/stm32f4_disco.jpg)

More information about the board can be found at the [STM32F4DISCOVERY website](https://www.st.com/en/evaluation-tools/stm32f4discovery.html).

## Hardware

STM32F4DISCOVERY Discovery kit provides the following hardware components:

- STM32F407VGT6 in LQFP100 package
- ARM® 32-bit Cortex® -M4 CPU with FPU
- 168 MHz max CPU frequency
- VDD from 1.8 V to 3.6 V
- 1 MB Flash
- 192+4 KB SRAM including 64-Kbyte of core coupled memory
- GPIO with external interrupt capability
- 3x12-bit ADC with 24 channels
- 2x12-bit D/A converters
- RTC
- Advanced-control Timer
- General Purpose Timers (17)
- Watchdog Timers (2)
- USART/UART (6)
- I2C (3)
- SPI (3)
- SDIO
- 2xCAN
- USB 2.0 OTG FS with on-chip PHY
- USB 2.0 OTG HS/FS with dedicated DMA, on-chip full-speed PHY and ULPI
- 10/100 Ethernet MAC with dedicated DMA
- 8- to 14-bit parallel camera
- CRC calculation unit
- True random number generator
- DMA Controller

More information about STM32F407VG can be found here:
:   - [STM32F407VG on www.st.com](https://www.st.com/en/microcontrollers/stm32f407vg.html)
    - [STM32F407 reference manual](https://www.st.com/resource/en/reference_manual/dm00031020.pdf)

### Supported Features

The Zephyr stm32f4\_disco board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port-polling; serial port-interrupt |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| PWM | on-chip | pwm |
| USB | on-chip | usb |
| CAN | on-chip | CAN controller |

Note

CAN feature requires CAN transceiver, such as [SK Pang CAN breakout board](https://www.skpang.co.uk/products/can-bus-can-fd-breakout-board-5v-supply-and-3-3v-logic).
Zephyr default configuration uses CAN\_2 exclusively, as simultaneous use
of CAN\_1 and CAN\_2 is not yet supported.

Other hardware features are not yet supported on Zephyr porting.

The default configuration can be found in
[boards/st/stm32f4\_disco/stm32f4\_disco\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32f4_disco/stm32f4_disco_defconfig)

### Pin Mapping

STM32F4DISCOVERY Discovery kit has 8 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

For more details please refer to [STM32F4DISCOVERY board User Manual](https://www.st.com/resource/en/user_manual/dm00039084.pdf).

#### Default Zephyr Peripheral Mapping:

- UART\_1\_TX : PB6
- UART\_1\_RX : PB7
- UART\_2\_TX : PA2
- UART\_2\_RX : PA3
- USER\_PB : PA0
- LD3 : PD13
- LD4 : PD12
- LD5 : PD14
- LD6 : PD15
- USB DM : PA11
- USB DP : PA12
- CAN1\_RX : PB8
- CAN1\_TX : PB9
- CAN2\_RX : PB5
- CAN2\_TX : PB13

### System Clock

STM32F4DISCOVERY System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by PLL clock at 168MHz,
driven by 8MHz high speed external clock.

### Serial Port

STM32F4DISCOVERY Discovery kit has up to 6 UARTs. The Zephyr console output is assigned to UART2.
Default settings are 115200 8N1.
Please note that ST-Link Virtual Com Port is not wired to chip serial port. In order to
enable console output you should use a serial cable and connect it to UART2 pins (PA2/PA3).

## Programming and Debugging

Applications for the `stm32f4_disco` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

STM32F4DISCOVERY Discovery kit includes an ST-LINK/V2 embedded debug tool interface.
This interface is supported by the openocd version included in Zephyr SDK.

#### Flashing an application to STM32F4DISCOVERY

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

Run a serial host program to connect with your board:

```shell
$ minicom -D /dev/ttyACM0
```

Build and flash the application:

```shell
# From the root of the zephyr repository
west build -b stm32f4_disco samples/basic/blinky
west flash
```

You should see user led “LD4” blinking.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b stm32f4_disco samples/hello_world
west debug
```

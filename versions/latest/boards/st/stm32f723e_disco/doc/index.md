---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/st/stm32f723e_disco/doc/index.html
original_path: boards/st/stm32f723e_disco/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# ST STM32F723E Discovery

## Overview

The discovery kit enables a wide diversity of applications taking benefit
from audio, multi-sensor support, graphics, security, security, video,
and high-speed connectivity features. Important board features include:

- STM32F723IEK6 microcontroller featuring 512 Kbytes of Flash memory and 256+16+4 Kbytes of RAM, in BGA176 package
- On-board ST-LINK/V2-1 supporting USB re-enumeration capability
- TFT LCD 240x240 pixels with touch panel
- SAI audio codec
- Audio line in and line out jack
- Stereo speaker outputs
- Four ST MEMS microphones
- Two pushbuttons (user and reset)
- 512-Mbit Quad-SPI Flash memory
- 8-Mbit external PSRAM
- USB OTG HS with Micro-AB connectors
- USB OTG FS with Micro-AB connectors

![STM32F723E-DISCO](../../../../_images/stm32f723e_disco.jpg)

More information about the board can be found at the [32F723E-DISCO website](https://www.st.com/en/evaluation-tools/32f723ediscovery.html).

## Hardware

The STM32F723E Discovery kit provides the following hardware components:

- STM32F723IEK6 in BGA176 package
- ARM® 32-bit Cortex® -M7 CPU with FPU
- 216 MHz max CPU frequency
- VDD from 1.8 V to 3.6 V
- 1 MB Flash
- 256+16+4 KB SRAM including 64KB of tightly coupled memory
- GPIO with external interrupt capability
- 3x12-bit ADC with 24 channels
- 2x12-bit D/A converters
- RTC
- Advanced-control Timer (2)
- General Purpose Timers (13)
- Watchdog Timers (2)
- USART/UART (8)
- I2C (3)
- SPI (5)
- 2xSAI (serial audio interface)
- SDIO (2)
- CAN
- USB 2.0 OTG FS with on-chip PHY
- USB 2.0 OTG HS/FS with dedicated DMA, on-chip full-speed PHY and on-chip hi-speed PHY
- CRC calculation unit
- True random number generator
- DMA Controller

More information about STM32F723IEK6 can be found here:

- [STM32F723IEK6 on www.st.com](https://www.st.com/en/microcontrollers/stm32f723ie.html)
- [STM32F72xxx reference manual](https://www.st.com/resource/en/reference_manual/dm00305990.pdf)

### Supported Features

The Zephyr stm32f723e\_disco board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port-polling; serial port-interrupt |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c |
| SPI | on-chip | spi |
| USB | on-chip | USB device |

Other hardware features are not yet supported on Zephyr porting.

The default configuration can be found in
[boards/st/stm32f723e\_disco/stm32f723e\_disco\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32f723e_disco/stm32f723e_disco_defconfig)

### Pin Mapping

STM32F723E Discovery kit has 7 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

For more details please refer to [32F723E-DISCO board User Manual](https://www.st.com/resource/en/user_manual/dm00342318.pdf).

#### Default Zephyr Peripheral Mapping:

- UART\_2 TX/RX : PA2/PA3 (Arduino Serial)
- UART\_6 TX/RX : PC6/PC7 (ST-Link Virtual Port Com)
- I2C1 SCL/SDA : PB8/PB9
- I2C2 SCL/SDA : PH4/PH5 (Arduino I2C)
- I2C3 SCL/SDA : PA8/PH8
- SPI1 SCK/MISO/MOSI : PA5/PB4/PB5 (Arduino SPI)
- LD1 : PA5
- LD5 : PA7
- LD6 : PB1
- OTG\_FS\_DM : PA11
- OTG\_FS\_DP : PA12

### System Clock

The STM32F723E System Clock can be driven by an internal or external oscillator,
as well as by the main PLL clock. By default, the System clock is driven by the PLL
clock at 216MHz, driven by a 25MHz high speed external clock.

### Serial Port

The STM32F723E Discovery kit has up to 8 UARTs. The Zephyr console output is assigned to UART6
which connected to the onboard ST-LINK/V2 Virtual COM port interface. Default communication
settings are 115200 8N1.

## Programming and Debugging

Applications for the `stm32f723e_disco` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

STM32F723E Discovery kit includes an ST-LINK/V2 embedded debug tool interface.
This interface is supported by the openocd version included in the Zephyr SDK.

#### Flashing an application to STM32F723E-DISCO

First, connect the STM32F723E Discovery kit to your host computer using
the USB port to prepare it for flashing. Then build and flash your application.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b stm32f723e_disco samples/hello_world
west flash
```

Run a serial host program to connect with your board:

```shell
$ minicom -D /dev/ttyACM0
```

You should see the following message on the console:

```shell
Hello World! arm
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b stm32f723e_disco samples/hello_world
west debug
```

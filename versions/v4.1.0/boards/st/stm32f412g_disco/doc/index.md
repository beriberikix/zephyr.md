---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/stm32f412g_disco/doc/index.html
original_path: boards/st/stm32f412g_disco/doc/index.html
---

# STM32F412G Discovery

Board Overview

[![../../../../_images/stm32f412g_disco.jpg](../../../../_images/stm32f412g_disco.jpg)
](../../../../_images/stm32f412g_disco.jpg)

STM32F412G Discovery

Name:
:   `stm32f412g_disco`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32f412zx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm32f412g_disco/doc/index.rst/../..)

## Overview

The STM32F412 Discovery kit features an ARM Cortex-M4 based STM32F412ZG MCU
with a wide range of connectivity support and configurations Here are
some highlights of the STM32F412G-DISCO board:

- STM32F412ZGT6 microcontroller featuring 1 Mbyte of Flash memory and 256 Kbytes of RAM in an LQFP144 package
- On-board ST-LINK/V2-1 SWD debugger supporting USB re-enumeration capability:

  > - USB virtual COM port
  > - mass storage
  > - debug port
- 1.54 inch 240x240 pixel TFT color LCD with parallel interface and capacitive touchscreen
- I2S Audio CODEC, with a stereo headset jack, including analog microphone input and a loudspeaker output
- Stereo digital MEMS microphones
- MicroSD card connector extension
- I2C extension connector
- 128 Mbit Quad-SPI Nor Flash
- Reset button and Joystick
- Four color user LEDs.
- USB OTG FS with Micro-AB connector
- Four power supply options:

  > - ST-LINK/V2-1 USB connector
  > - User USB FS connector
  > - VIN from Arduino\* connectors
  > - - 5 V from Arduino\* connectors
- Two power supplies for MCU: 2.0 V and 3.3 V
- Compatible with Arduino(tm) Uno revision 3 connectors
- Extension connector for direct access to various features of STM32F412ZGT6 MCU
- Comprehensive free software including a variety of examples, part of STM32Cube package

More information about the board can be found at the [32F412GDISCOVERY website](https://www.st.com/en/evaluation-tools/32f412gdiscovery.html).

## Hardware

STM32F412G-DISCO Discovery kit provides the following hardware components:

- STM32F412ZGT6 in LQFP144 package
- ARM® 32-bit Cortex® -M4 CPU with FPU
- 100 MHz max CPU frequency
- VDD from 1.7 V to 3.6 V
- 1 MB Flash
- 256 KB SRAM
- GPIO with external interrupt capability
- LCD parallel interface, 8080/6800 modes
- 1x12-bit ADC with 16 channels
- RTC
- Advanced-control Timer
- General Purpose Timers (12)
- Watchdog Timers (2)
- USART/UART (4)
- I2C (4)
- SPI (5)
- SDIO
- 2xCAN
- CRC calculation unit
- True random number generator
- DMA Controller

More information about STM32F412ZG can be found here:
:   - [STM32F412ZG on www.st.com](https://www.st.com/en/microcontrollers/stm32f412zg.html)
    - [STM32F412 reference manual](https://www.st.com/resource/en/reference_manual/dm00180369.pdf)

### Supported Features

The `stm32f412g_disco` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Pin Mapping

STM32F412G-DISCO Discovery kit has 8 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

For more details please refer to [32F412GDISCOVERY board User Manual](https://www.st.com/resource/en/user_manual/dm00275919.pdf).

#### Default Zephyr Peripheral Mapping:

- UART\_2\_TX : PA2
- UART\_2\_RX : PA3
- LD1 : PE0
- LD2 : PE1
- LD3 : PE2
- LD4 : PE3

### System Clock

STM32F412G-DISCO System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by PLL clock at 100MHz,
driven internal oscillator.

### Serial Port

The STM32F412G Discovery kit has up to 4 UARTs. The Zephyr console output is assigned to UART2.
Default settings are 115200 8N1.

## Programming and Debugging

STM32F412G-DISCO Discovery kit includes an ST-LINK/V2 embedded debug tool interface.

Applications for the `stm32f412g_disco` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD or JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
```

#### Flashing an application to STM32F412G-DISCO

Connect the STM32F412G-DISCO Discovery kit to your host computer using
the USB port, then run a serial host program to connect with your
board:

```shell
$ minicom -D /dev/ttyACM0
```

Then build and flash an application. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b stm32f412g_disco samples/hello_world
west flash
```

You should see the following message on the console:

```shell
Hello World! arm
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b stm32f412g_disco samples/hello_world
west debug
```

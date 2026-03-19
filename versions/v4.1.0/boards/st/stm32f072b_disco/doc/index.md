---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/stm32f072b_disco/doc/index.html
original_path: boards/st/stm32f072b_disco/doc/index.html
---

# STM32F072B Discovery

Board Overview

[![../../../../_images/stm32f072b_disco.jpg](../../../../_images/stm32f072b_disco.jpg)
](../../../../_images/stm32f072b_disco.jpg)

STM32F072B Discovery

Name:
:   `stm32f072b_disco`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32f072xb

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm32f072b_disco/doc/index.rst/../..)

## Overview

The STM32F072B-DISCO Discovery kit features an ARM Cortex-M0 based STM32F072RB
MCU with everything required for beginners and experienced users to get
started quickly. Here are some highlights of the STM32F072B-DISCO board:

- STM32 microcontroller in LQFP64 package
- Extension header for LQFP64 I/Os for a quick connection to the prototyping
  board and easy probing
- On-board ST-LINK/V2, debugger/programmer with SWD connector
- Board power supply: through USB bus or from an external 5 V supply voltage
- External application power supply: 3 V and 5 V
- Six LEDs:

  - LD1 (red/green) for USB communication
  - LD2 (red) for 3.3 V power on
  - Four user LEDs: LD3 (orange), LD4 (green), LD5 (red) and LD6 (blue)
- Two push-buttons: USER and RESET
- USB USER with Mini-B connector
- L3GD20, ST MEMS motion sensor, 3-axis digital output gyroscope
- One linear touch sensor or four touch keys
- RF EEprom daughter board connector

More information about the board can be found at the
[STM32F072B-DISCO website](https://www.st.com/en/evaluation-tools/32f072bdiscovery.html) [[1]](#id2).

## Hardware

STM32F072B-DISCO Discovery kit provides the following hardware components:

- STM32F072RBTT6 in LQFP64 package
- ARM® 32-bit Cortex® -M0 CPU
- 48 MHz max CPU frequency
- VDD from 2.0 V to 3.6 V
- 128 KB Flash
- 16 KB SRAM
- GPIO with external interrupt capability
- 12-bit ADC with 39 channels
- 12-bit D/A converters
- RTC
- General Purpose Timers (12)
- USART/UART (4)
- I2C (2)
- SPI (2)
- CAN
- USB 2.0 full speed interface
- DMA Controller
- 24 capacitive sensing channels for touchkey, linear and rotary touch sensors

More information about STM32F072RB can be found here:
:   - [STM32F072RB on www.st.com](https://www.st.com/en/microcontrollers/stm32f072rb.html) [[3]](#id6)
    - [STM32F072xB reference manual](https://www.st.com/resource/en/reference_manual/dm00031936.pdf) [[4]](#id8)

### Supported Features

The `stm32f072b_disco` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

Note

CAN feature requires CAN transceiver, such as [SK Pang CAN breakout board](https://www.skpang.co.uk/products/can-bus-can-fd-breakout-board-5v-supply-and-5v-logic) [[5]](#id10).

### Pin Mapping

STM32F072B-DISCO Discovery kit has 6 GPIO controllers. These controllers are
responsible for pin muxing, input/output, pull-up, etc.

For more details please refer to [STM32F072B-DISCO board User Manual](https://www.st.com/resource/en/user_manual/dm00099401.pdf) [[2]](#id4).

#### Default Zephyr Peripheral Mapping:

- UART\_1\_TX : PB6
- UART\_1\_RX : PB7
- I2C1\_SCL : PB8
- I2C1\_SDA : PB9
- I2C2\_SCL : PB10
- I2C2\_SDA : PB11
- SPI1\_SCK : PB3
- SPI1\_MISO : PB4
- SPI1\_MOSI : PB5
- USER\_PB : PA0
- LD3 : PC6
- LD4 : PC8
- LD5 : PC9
- LD6 : PC7
- CAN\_RX : PB8
- CAN\_TX : PB9

### System Clock

STM32F072B-DISCO System Clock could be driven by internal or external
oscillator, as well as main PLL clock. By default System clock is driven
by PLL clock at 72 MHz, driven by internal 8 MHz oscillator.

### Serial Port

STM32F072B-DISCO Discovery kit has up to 4 UARTs. The Zephyr console output
is assigned to UART 1. Default settings are 115200 8N1.

## Programming and Debugging

STM32F072B-DISCO board includes an ST-LINK/V2 embedded debug tool interface.

Applications for the `stm32f072b_disco` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) [[6]](#id12) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD or JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
```

#### Flashing an application to STM32F072B-DISCO

First, connect the STM32F072B-DISCO Discovery kit to your host computer using
the USB port to prepare it for flashing. Then build and flash your application.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b stm32f072b_disco samples/hello_world
west flash
```

Run a serial host program to connect with your board. A TTL(3.3V) serial
adapter is required.

```shell
$ minicom -D /dev/<tty device>
```

Replace <tty\_device> with the port where the serial adapter can be found.
For example, under Linux, /dev/ttyUSB0.

You should see the following message on the console:

```shell
Hello World! arm
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b stm32f072b_disco samples/hello_world
west debug
```

## References

[[1](#id3)]

[https://www.st.com/en/evaluation-tools/32f072bdiscovery.html](https://www.st.com/en/evaluation-tools/32f072bdiscovery.html)

[[2](#id5)]

[https://www.st.com/resource/en/user\_manual/dm00099401.pdf](https://www.st.com/resource/en/user_manual/dm00099401.pdf)

[[3](#id7)]

[https://www.st.com/en/microcontrollers/stm32f072rb.html](https://www.st.com/en/microcontrollers/stm32f072rb.html)

[[4](#id9)]

[https://www.st.com/resource/en/reference\_manual/dm00031936.pdf](https://www.st.com/resource/en/reference_manual/dm00031936.pdf)

[[5](#id11)]

[https://www.skpang.co.uk/products/can-bus-can-fd-breakout-board-5v-supply-and-5v-logic](https://www.skpang.co.uk/products/can-bus-can-fd-breakout-board-5v-supply-and-5v-logic)

[[6](#id13)]

[https://www.st.com/en/development-tools/stm32cubeprog.html](https://www.st.com/en/development-tools/stm32cubeprog.html)

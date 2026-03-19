---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/stm32f429i_disc1/doc/index.html
original_path: boards/st/stm32f429i_disc1/doc/index.html
---

# STM32F429I Discovery

Board Overview

[![../../../../_images/stm32f429i_disc1.jpg](../../../../_images/stm32f429i_disc1.jpg)
](../../../../_images/stm32f429i_disc1.jpg)

STM32F429I Discovery

Name:
:   `stm32f429i_disc1`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32f429xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm32f429i_disc1/doc/index.rst/../..)

## Overview

The STM32F429I-DISC1 Discovery kit features an ARM Cortex-M4 based STM32F429ZI MCU
with a wide range of connectivity support and configurations. Here are
some highlights of the STM32F429I-DISC1 board:

- STM32 microcontroller in LQFP144 package
- Extension header for all LQFP144 I/Os for quick connection to prototyping board and easy probing
- On-board ST-LINK/V2-B debugger/programmer with SWD connector
- Flexible board power supply:

  > - ST-LINK/V2-1 USB connector
  > - User USB FS connector
  > - VIN from Arduino\* compatible connectors
- Two push-buttons: USER and RESET
- USB OTG FS with micro-AB connector
- 2.4-inch QVGA LCD with MIPI DSI interface and capacitive touch screen
- 64Mbit SDRAM
- L3GD20, ST-MEMS motion sensor 3-axis digital output gyroscope
- Six LEDs

  > - LD1 (red/green) for USB communication
  > - LD2 (red) for 3.3 V power-on
  > - Two user LEDs: LD3 (green), LD4 (red)
  > - Two USB OTG LEDs: LD5 (green) VBUS and LD6 (red) OC (over-current)

More information about the board can be found at the [STM32F429I-DISC1 website](https://www.st.com/en/evaluation-tools/32f429idiscovery.html).

## Hardware

The STM32F429I-DISC1 Discovery kit provides the following hardware components:

- STM32F429ZIT6 in LQFP144 package
- ARM® 32-bit Cortex® -M4 CPU with FPU
- 180 MHz max CPU frequency
- VDD from 1.8 V to 3.6 V
- 2 MB Flash
- 256+4 KB SRAM including 64-Kbyte of core coupled memory
- GPIO with external interrupt capability
- 3x12-bit ADC with 24 channels
- 2x12-bit D/A converters
- RTC
- Advanced-control Timer
- General Purpose Timers (17)
- Watchdog Timers (2)
- USART/UART (4/4)
- I2C (3)
- SPI (6)
- SDIO
- 2xCAN
- USB 2.0 OTG FS with on-chip PHY
- USB 2.0 OTG HS/FS with dedicated DMA, on-chip full-speed PHY and ULPI
- 10/100 Ethernet MAC with dedicated DMA
- 8- to 14-bit parallel camera
- CRC calculation unit
- True random number generator
- DMA Controller

More information about STM32F429ZI can be found here:
:   - [STM32F429ZI on www.st.com](https://www.st.com/en/microcontrollers/stm32f429-439.html)
    - [STM32F429 Reference Manual](https://www.st.com/content/ccc/resource/technical/document/reference_manual/3d/6d/5a/66/b4/99/40/d4/DM00031020.pdf/files/DM00031020.pdf/jcr:content/translations/en.DM00031020.pdf)

### Supported Features

The `stm32f429i_disc1` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Pin Mapping

The STM32F429I-DISC1 Discovery kit has 8 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

For more details please refer to [STM32F429I-DISC1 board User Manual](https://www.st.com/web/en/resource/technical/document/user_manual/DM00097320.pdf).

#### Default Zephyr Peripheral Mapping:

- UART\_1\_TX : PA9
- UART\_1\_RX : PA10
- USER\_PB : PA0
- LD3 : PG13
- LD4 : PG12
- I2C\_1\_SCL : PB8
- I2C\_1\_SDA : PB9
- I2C\_2\_SCL : PB10
- I2C\_2\_SDA : PB11
- I2C\_3\_SCL : PA8
- I2C\_3\_SDA : PC9
- SPI\_5\_CS : PF6
- SPI\_5\_SCK : PF7
- SPI\_5\_MISO : PF8
- SPI\_5\_MOSI : PF9
- OTG\_HS\_ID : PB12
- OTG\_HS\_DM : PB14
- OTG\_HS\_DP : PB15

### System Clock

The STM32F429I-DISC1 System Clock could be driven by an internal or external oscillator,
as well as by the main PLL clock. By default the system clock is driven by the PLL clock at 168MHz,
driven by an 8MHz high speed external clock.

### Serial Port

The STM32F429I-DISC1 Discovery kit has up to 8 UARTs. The Zephyr console output is assigned to UART1.
The default communication settings are 115200 8N1.

### USB Port

The STM32F429I-DISC1 Discovery kit has a USB FS capable Micro-B port. It is connected to the on-chip
OTG\_HS peripheral, but operates in FS mode only since no HS PHY is present. The board supports device
and host OTG operation, but only device mode has been tested with Zephyr at this time.

## Programming and Debugging

The STM32F429I-DISC1 Discovery kit includes a ST-LINK/V2-B embedded debug tool interface.
Applications for the `stm32f429i_disc1` board configuration can be built
and flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD, JLink, or pyOCD can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
$ west flash --runner pyocd
```

First, connect the STM32F429I-DISC1 Discovery kit to your host computer using
the USB port to prepare it for flashing. Then build and flash your application.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b stm32f429i_disc1 samples/hello_world
west flash
```

Run a serial host program to connect with your board:

```shell
$ minicom -D /dev/ttyACM0
```

Then, press the RESET button (The black one), you should see the following message:

```shell
Hello World! arm
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b stm32f429i_disc1 samples/hello_world
west debug
```

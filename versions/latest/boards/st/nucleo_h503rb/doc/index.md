---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/nucleo_h503rb/doc/index.html
original_path: boards/st/nucleo_h503rb/doc/index.html
---

# Nucleo H503RB

Board Overview

[![../../../../_images/nucleo_h503rb.png](../../../../_images/nucleo_h503rb.png)
](../../../../_images/nucleo_h503rb.png)

Nucleo H503RB

Name:
:   `nucleo_h503rb`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32h503xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_h503rb/doc/index.rst/../..)

## Overview

The Nucleo-H503RB board features an ARM® Cortex®-M33 core-based
STM32H503RBT6 microcontroller with a wide range of connectivity support and
configurations.
Here are some highlights of the Nucleo-H503RB board:

- STM32H503RB microcontroller featuring 128 Kbytes of Flash memory and 32 Kbytes of
  SRAM in LQFP64 package
- Board connectors:

  - User USB Type-C®
  - MIPI10 for debugging (SWD/JTAG)
  - Arduino® Uno V3 connectivity (CN5, CN6, CN8, CN9)
  - ST morpho extension connector (CN7, CN10)
- Flexible board power supply:

  - ST-LINK USB VBUS
  - user USB connector
  - external sources
- On-board ST-LINK/V3EC debugger/programmer:

  - mass storage
  - Virtual COM port
  - debug port
- One user LED shared with ARDUINO® Uno V3
- Two push-buttons: USER and RESET
- 32.768 kHz crystal oscillator
- 24 MHz HSE crystal oscillator

More information about the board can be found at the [NUCLEO\_H503RB website](https://www.st.com/en/evaluation-tools/nucleo-h503rb).

![NUCLEO-H503RB](../../../../_images/nucleo_h503rb1.png)

## Hardware

The STM32H503xx devices are a high-performance microcontrollers family
(STM32H5 series) based on the high-performance Arm® Cortex®-M33 32-bit
RISC core. They operate at a frequency of up to 250 MHz.

- Core: Arm® Cortex®-M33 CPU with FPU, MPU, 375 DMIPS (Dhrystone 2.1),
  and DSP instructions
- ART Accelerator
- Memories

  - 128 Kbytes of embedded flash memory with ECC, two banks of read-while-write
  - 2-Kbyte OTP (one-time programmable)
  - 32-Kbyte SRAM with ECC
  - 2 Kbytes of backup SRAM (available in the lowest power modes)
- Clock management

  - Internal oscillators: 64 MHz HSI, 48 MHz HSI48, 4 MHz CSI, 32 kHz LSI
  - Two PLLs for system clock, USB, audio, and ADC
  - External oscillators: 4 to 50 MHz HSE, 32.768 kHz LSE
- Embedded regulator (LDO)
- Up to 49 fast I/Os (most 5 V tolerant), up to 9 I/Os with independent supply down to 1.08 V
- Analog peripherals

  - 1x 12-bit ADC with up to 2.5 MSPS
  - 1x 12-bit dual-channel DAC
  - 1x ultra-low-power comparator
  - 1x operational amplifier (7 MHz bandwidth)
- 1x Digital temperature sensor
- Up to 11 timers
  - 4x 16-bit
  - 1x 32-bit
  - 2x 16-bit low-power 16-bit timers (available in Stop mode)
  - 2x watchdogs
  - 1x SysTick timer
  - RTC with HW calendar, alarms and calibration
- Up to 16x communication interfaces

  - Up to 2x I2Cs FM + interfaces (SMBus/PMBus®)
  - Up to 2x I3Cs shared with I2C
  - Up to 3x USARTs (ISO7816 interface, LIN, IrDA, modem control)
  - 1x LPUART
  - Up to 3x SPIs including three muxed with full-duplex I2S
  - Up to 3x additional SPI from 3x USART when configured in synchronous mode
  - 1x FDCAN
  - 1x USB 2.0 full-speed host and device
- Two DMA controllers to offload the CPU
- Security

  - HASH (SHA-1, SHA-2), HMAC
  - True random generator
  - 96-bit unique ID
  - Active tamper
- Development support: serial wire debug (SWD) and JTAG interfaces

More information about STM32H533RE can be found here:

- [STM32H503rb on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32h503rb)
- [STM32H503 reference manual](https://www.st.com/resource/en/reference_manual/rm0492-stm32h503-line-armbased-32bit-mcus-stmicroelectronics.pdf)

### Supported Features

The `nucleo_h503rb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

Nucleo-H503RB board has 8 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

For more details please refer to [STM32H5 Nucleo-64 board User Manual](https://www.st.com/resource/en/user_manual/um3121-stm32h5-nucleo64-board-mb1814-stmicroelectronics.pdf).

#### Default Zephyr Peripheral Mapping:

- USART1 TX/RX : PB14/PB15 (Arduino USART1)
- SPI1 SCK/MISO/MOSI/NSS: PA5/PA6/PA7/PC9
- USART3 TX/RX : PA3/PA4 (VCP)
- USER\_PB : PC13
- User LED (green): PA5

#### System Clock

Nucleo H533RE System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by PLL clock at
240 MHz, driven by an 24 MHz high-speed external clock.

#### Serial Port

Nucleo H533RE board has up to 3 U(S)ARTs. The Zephyr console output is assigned
to USART3. Default settings are 115200 8N1.

#### Backup SRAM

In order to test backup SRAM, you may want to disconnect VBAT from VDD\_MCU.
You can do it by removing `SB38` jumper on the back side of the board.
VBAT can be provided via the left ST Morpho connector’s pin 33.

## Programming and Debugging

Nucleo-H503RB board includes an ST-LINK/V3EC embedded debug tool interface.
This probe allows to flash the board using various tools.

Applications for the `nucleo_h503rb` board can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### OpenOCD Support

For now, openocd support for stm32h5 is not available on upstream OpenOCD.
You can check [OpenOCD official Github mirror](https://github.com/openocd-org/openocd/).
In order to use it though, you should clone from the customized
[STMicroelectronics OpenOCD Github](https://github.com/STMicroelectronics/OpenOCD/tree/openocd-cubeide-r6) and compile it following usual README guidelines.
Once it is done, you can set the OPENOCD and OPENOCD\_DEFAULT\_PATH variables in
[boards/st/nucleo\_h563zi/board.cmake](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_h563zi/board.cmake) to point the build
to the paths of the OpenOCD binary and its scripts, before
including the common openocd.board.cmake file:

> ```text
> set(OPENOCD "<path_to_openocd_repo>/src/openocd" CACHE FILEPATH "" FORCE)
> set(OPENOCD_DEFAULT_PATH <path_to_opneocd_repo>/tcl)
> include(${ZEPHYR_BASE}/boards/common/openocd.board.cmake)
> ```

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpencOCD or pyOCD can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner pyocd
```

For pyOCD, additional target information needs to be installed
which can be done by executing the following commands:

```shell
$ pyocd pack --update
$ pyocd pack --install stm32h5
```

#### Flashing an application to Nucleo-H503RB

Connect the Nucleo-H503RB to your host computer using the USB port.
Then build and flash an application. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Run a serial host program to connect with your Nucleo board:

```shell
$ minicom -D /dev/ttyACM0
```

Then build and flash the application.

```shell
# From the root of the zephyr repository
west build -b nucleo_h503rb samples/hello_world
west flash
```

You should see the following message on the console:

```shell
Hello World! nucleo_h503rb/stm32h503xx
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_h503rb samples/basic/blinky
west debug
```

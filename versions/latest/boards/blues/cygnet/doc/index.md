---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/blues/cygnet/doc/index.html
original_path: boards/blues/cygnet/doc/index.html
---

# Cygnet

Board Overview

[![../../../../_images/cygnet.webp](../../../../_images/cygnet.webp)
](../../../../_images/cygnet.webp)

Cygnet

Name:
:   `cygnet`

Vendor:
:   Blues Wireless

Architecture:
:   arm

SoC:
:   stm32l433xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/blues/cygnet/doc/index.rst/../..)

## Overview

The Blues Cygnet board features an ARM Cortex-M4 based STM32L433CC MCU
with a wide range of connectivity support and configurations. Here are
some highlights of the Cygnet board:

- STM32L4 microcontroller in LQFP48 package
- Adafruit Feather connector
- User LED
- User push-button
- USB Type-C connector

More information about the board can be found at the [Blues Cygnet website](https://www.blues.dev/) [[1]](#id2).

## Hardware

The STM32L433CC SoC provides the following hardware IPs:

- Ultra-low-power with FlexPowerControl (down to 28 nA Standby mode and 84
  µA/MHz run mode)
- Core: ARM® 32-bit Cortex® -M4 CPU with FPU, frequency up to 80 MHz,
  100DMIPS/1.25DMIPS/MHz (Dhrystone 2.1)
- Clock Sources:

  - 32 kHz crystal oscillator for RTC (LSE)
  - Internal 16 MHz factory-trimmed RC ( ±1%)
  - Internal low-power 32 kHz RC ( ±5%)
  - Internal multispeed 100 kHz to 48 MHz oscillator, auto-trimmed by
    LSE (better than ±0.25 % accuracy)
  - 2 PLLs for system clock, USB, audio, ADC
- RTC with HW calendar, alarms and calibration
- 11x timers:

  - 1x 16-bit advanced motor-control
  - 1x 32-bit and 2x 16-bit general purpose
  - 2x 16-bit basic
  - 2x low-power 16-bit timers (available in Stop mode)
  - 2x watchdogs
  - SysTick timer
- Up to 21 fast I/Os, most 5 V-tolerant
- Memories

  - Up to 256 KB single bank Flash, proprietary code readout protection
  - 64 KB of SRAM including 16 KB with hardware parity check
- Rich analog peripherals (independent supply)

  - 1x 12-bit ADC 5 MSPS, up to 16-bit with hardware oversampling, 200
    µA/MSPS
  - 2x 12-bit DAC output channels, low-power sample and hold
  - 1x operational amplifiers with built-in PGA
  - 2x ultra-low-power comparators
- 17x communication interfaces

  - USB 2.0 full-speed crystal less solution with LPM and BCD
  - 1x SAI (serial audio interface)
  - 3x I2C FM+(1 Mbit/s), SMBus/PMBus
  - 4x USARTs (ISO 7816, LIN, IrDA, modem)
  - 1x LPUART (Stop 2 wake-up)
  - 3x SPIs (and 1x Quad SPI)
  - CAN (2.0B Active)
- 14-channel DMA controller
- True random number generator
- CRC calculation unit, 96-bit unique ID
- Development support: serial wire debug (SWD), JTAG, Embedded Trace Macrocell\*

More information about STM32L433CC can be found here:

- [STM32L433CC on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32l433cc.html) [[3]](#id6)
- [STM32L432 reference manual](https://www.st.com/resource/en/reference_manual/dm00151940.pdf) [[4]](#id8)

### Supported Features

The `cygnet` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

Note

CAN feature requires a CAN transceiver.

### Connections and IOs

The Cygnet board has 6 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

#### Available pins

![Cygnet Pinout](../../../../_images/cygnet-pinout.webp)

For more details please refer to [Blues Cygnet User Manual](https://dev.blues.io/feather-mcus/cygnet/cygnet-introduction/) [[2]](#id4).

#### Default Zephyr Peripheral Mapping

- LPUART\_1\_TX : PB11
- LPUART\_1\_RX : PB10
- UART\_1\_TX : PA9
- UART\_1\_RX : PA10
- I2C\_1\_SCL : PB6
- I2C\_1\_SDA : PB7
- PWM\_2\_CH1 : PA0
- SPI\_1: SCK/MISO/MOSI : PA5/PA6/PB5

#### System Clock

The Cygnet board System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by PLL clock at 80MHz,
driven by 16MHz high speed internal oscillator.

#### Serial Port

The Cygnet board has 4 U(S)ARTs and 1 LPUART. The Zephyr console output is assigned
to LPUART1. Default settings are 115200 8N1.

## Programming and Debugging

The Cygnet board requires an ST-LINK embedded debug tool in order to be programmed and debugged.

Applications for the `cygnet` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) [[5]](#id10) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD or JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
```

#### Flashing an application to Cygnet

Connect the Cygnet to the ST-LINK debugger, then run a serial host program to connect with your Cygnet board.

```shell
$ picocom /dev/ttyACM0 -b 115200
```

Now build and flash an application. Here is an example for
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.").

```shell
# From the root of the zephyr repository
west build -b cygnet samples/hello_world
west flash
```

You should see the following message on the console:

```shell
$ Hello World! cygnet
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b cygnet samples/hello_world
west debug
```

## References

[[1](#id3)]

[https://www.blues.dev/](https://www.blues.dev/)

[[2](#id5)]

[https://dev.blues.io/feather-mcus/cygnet/cygnet-introduction/](https://dev.blues.io/feather-mcus/cygnet/cygnet-introduction/)

[[3](#id7)]

[https://www.st.com/en/microcontrollers-microprocessors/stm32l433cc.html](https://www.st.com/en/microcontrollers-microprocessors/stm32l433cc.html)

[[4](#id9)]

[https://www.st.com/resource/en/reference\_manual/dm00151940.pdf](https://www.st.com/resource/en/reference_manual/dm00151940.pdf)

[[5](#id11)]

[https://www.st.com/en/development-tools/stm32cubeprog.html](https://www.st.com/en/development-tools/stm32cubeprog.html)

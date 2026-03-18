---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/st/nucleo_l432kc/doc/index.html
original_path: boards/st/nucleo_l432kc/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# ST Nucleo L432KC

## Overview

The Nucleo L432KC board features an ARM Cortex-M4 based STM32L432KC MCU
with a wide range of connectivity support and configurations. Here are
some highlights of the Nucleo L432KC board:

- STM32 microcontroller in UFQFPN32 package
- Arduino Uno V3 connectivity
- On-board ST-LINK/V2-1 debugger/programmer with SWD connector
- Flexible board power supply:

  - USB VBUS or external source(3.3V, 5V, 7 - 12V)
  - Power management access point
- Three LEDs: USB communication (LD1), power LED (LD2), user LED (LD3)
- One push-button: RESET

![Nucleo L432KC](../../../../_images/nucleo_l432kc.jpg)

More information about the board can be found at the [Nucleo L432KC website](https://www.st.com/en/evaluation-tools/nucleo-l432kc.html).

## Hardware

The STM32L432KC SoC provides the following hardware IPs:

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
- Up to 3 capacitive sensing channels: support touchkey, linear and rotary touch sensors
- 11x timers:

  - 1x 16-bit advanced motor-control
  - 1x 32-bit and 2x 16-bit general purpose
  - 2x 16-bit basic
  - 2x low-power 16-bit timers (available in Stop mode)
  - 2x watchdogs
  - SysTick timer
- Up to 26 fast I/Os, most 5 V-tolerant
- Memories

  - Up to 256 KB single bank Flash, proprietary code readout protection
  - Up to 64 KB of SRAM including 16 KB with hardware parity check
  - Quad SPI memory interface
- Rich analog peripherals (independent supply)

  - 1x 12-bit ADC 5 MSPS, up to 16-bit with hardware oversampling, 200
    µA/MSPS
  - 2x 12-bit DAC, low-power sample and hold
  - 1x operational amplifiers with built-in PGA
  - 2x ultra-low-power comparators
- 13x communication interfaces

  - USB OTG 2.0 full-speed crystal less solution with LPM and BCD
  - 1x SAIs (serial audio interface)
  - 2x I2C FM+(1 Mbit/s), SMBus/PMBus
  - 3x USARTs (ISO 7816, LIN, IrDA, modem)
  - 2x SPIs (3x SPIs with the Quad SPI)
  - CAN (2.0B Active)
  - SWPMI single wire protocol master I/F
  - IRTIM (Infrared interface)
- 14-channel DMA controller
- True random number generator
- CRC calculation unit, 96-bit unique ID
- Development support: serial wire debug (SWD), JTAG, Embedded Trace Macrocell\*

More information about STM32L432KC can be found here:

- [STM32L432KC on www.st.com](https://www.st.com/en/microcontrollers/stm32l432kc.html)
- [STM32L432 reference manual](https://www.st.com/resource/en/reference_manual/dm00151940.pdf)

### Supported Features

The Zephyr nucleo\_l432kc board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port-polling; serial port-interrupt |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c |
| PWM | on-chip | pwm |
| CAN | on-chip | can |

Note

CAN feature requires CAN transceiver

Other hardware features are not yet supported on this Zephyr port.

The default configuration can be found in the defconfig file:
[boards/st/nucleo\_l432kc/nucleo\_l432kc\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_l432kc/nucleo_l432kc_defconfig)

### Connections and IOs

Nucleo L432KC Board has 6 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

#### Available pins:

![Nucleo L432KC Arduino connectors](../../../../_images/nucleo_l432kc_arduino_nano.jpg)

For more details please refer to [STM32 Nucleo-32 board User Manual](https://www.st.com/resource/en/user_manual/dm00231744.pdf).

#### Default Zephyr Peripheral Mapping:

- UART\_1\_TX : PA9
- UART\_1\_RX : PA10
- UART\_2\_TX : PA2
- UART\_2\_RX : PA3
- I2C\_1\_SCL : PB6
- I2C\_1\_SDA : PB7
- PWM\_2\_CH1 : PA0
- LD3 : PB3

#### System Clock

Nucleo L432KC System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by PLL clock at 80MHz,
driven by 16MHz high speed internal oscillator.

#### Serial Port

Nucleo L432KC board has 3 U(S)ARTs. The Zephyr console output is assigned to UART2.
Default settings are 115200 8N1.

## Programming and Debugging

Applications for the `nucleo_l432kc` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

Nucleo L432KC board includes an ST-LINK/V2-1 embedded debug tool
interface. This interface is supported by the openocd version
included in the Zephyr SDK since v0.9.2.

#### Flashing an application to Nucleo L432KC

Connect the Nucleo L432KC to your host computer using the USB port,
then run a serial host program to connect with your Nucleo board.

```shell
$ minicom -D /dev/ttyACM0
```

Now build and flash an application. Here is an example for
[Hello World](../../../../samples/hello_world/README.md#hello-world).

```shell
# From the root of the zephyr repository
west build -b nucleo_l432kc samples/hello_world
west flash
```

You should see the following message on the console:

```shell
$ Hello World! arm
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b nucleo_l432kc samples/hello_world
west debug
```

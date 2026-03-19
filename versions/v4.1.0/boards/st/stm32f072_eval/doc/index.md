---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/stm32f072_eval/doc/index.html
original_path: boards/st/stm32f072_eval/doc/index.html
---

# STM32F072 Evaluation

Board Overview

[![../../../../_images/stm32f072_eval.jpg](../../../../_images/stm32f072_eval.jpg)
](../../../../_images/stm32f072_eval.jpg)

STM32F072 Evaluation

Name:
:   `stm32f072_eval`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32f072xb

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm32f072_eval/doc/index.rst/../..)

## Overview

The STM32F072-EVAL Discovery kit features an ARM Cortex-M0 based STM32F072VBT6 MCU
with a wide range of connectivity support and configurations.
Here are some highlights of the STM32F072-EVAL board:

- Four 5 V power supply options: power jack, ST-LINK/V2 USB connector, user USB connector, or daughter board
- Stereo audio jack, which supports a headset with microphone connected to DAC and ADC of STM32F072VBT6.
- 2G Byte (or more) SPI interface MicroSD card
- I2C compatible serial interface temperature sensor
- RF E2PROM
- RS232 and RS485 communication
- IrDA transceiver
- IR LED and IR receiver
- SWD debug support, ST-LINK/V2 embedded
- 240x320 TFT color LCD connected to SPI interface of STM32F072VBT6
- Joystick with 4-direction control and selector
- Reset and tamper buttons
- Four color user LEDs and two LEDs as MCU low power alarm
- Extension connector for daughter board or wrapping board
- MCU voltage choice: fixed 3.3 V or adjustable from 1.65 V to 3.6 V
- USB full-speed connector
- Touch sensing buttons
- RTC with backup battery
- CAN2.0A/B compliant connector
- Light Dependent Resistor (LDR)
- Potentiometer
- Two HDMI connectors with DDC and CEC
- Smart Card slot
- Motor control connector

## Hardware

STM32F072-EVAL Discovery kit provides the following hardware components:

- STM32F072VBT6 in LQFP100 package
- ARM® 32-bit Cortex® -M0 CPU
- 48 MHz max CPU frequency
- VDD from 2.0 V to 3.6 V
- 128 KB Flash
- 16 KB SRAM with HW parity
- GPIO with external interrupt capability
- one 12-bit ADC with 16 channels
- one 12-bit D/A converters with 2 channels
- RTC
- Advanced-control Timer
- General Purpose Timers (8)
- Watchdog Timers (2)
- USART (4)
- I2C (2)
- SPI (2)
- CAN
- USB 2.0 OTG FS with on-chip PHY
- CRC calculation unit
- DMA Controller
- HDMI CEC Controller
- 24 capacitive sensing channels for touchkey, linear, and rotary touch sensors
- Up to 87 fast I/Os: 68 I/Os with 5V tolerant capability and 19 with independent supply

More information about STM32F072VB can be found here:
:   - [STM32F072VB on www.st.com](https://www.st.com/en/microcontrollers/stm32f072vb.html)
    - [STM32F072 reference manual](https://www.st.com/resource/en/reference_manual/dm00031936.pdf)

### Supported Features

The `stm32f072_eval` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Pin Mapping

STM32F072-EVAL Discovery kit has 6 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

For more details please refer to STM32F072-EVAL board User Manual.

#### Default Zephyr Peripheral Mapping:

- UART\_2\_TX : PD5
- UART\_2\_RX : PD6
- TAMPER\_PB : PC13
- JOYSTICK\_RIGHT\_PB : PE3
- JOYSTICK\_LEFT\_PB : PF2
- JOYSTICK\_UP\_PB : PF9
- JOYSTICK\_DOWN\_PB : PF10
- JOYSTICK\_SEL\_PB : PA0
- LD1 : PD8
- LD2 : PD9
- LD3 : PD10
- LD4 : PD11

### System Clock

STM32F072-EVAL System Clock could be driven by an internal or external oscillator,
as well as the main PLL clock. By default the System clock is driven by the PLL clock at 48MHz,
driven by an 8MHz high speed internal clock.

### Serial Port

STM32F072-EVAL Discovery kit has up to 4 UARTs. The Zephyr console output is assigned to UART2.
Default settings are 115200 8N1.

## Programming and Debugging

STM32F072-EVAL Discovery kit includes an ST-LINK/V2 embedded debug tool interface.

Applications for the `stm32f072_eval` board configuration can be built and
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

#### Flashing an application to STM32F072-EVAL

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b stm32f072_eval samples/basic/blinky
west flash
```

You will see the LED blinking every second.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b stm32f072_eval samples/basic/blinky
west debug
```

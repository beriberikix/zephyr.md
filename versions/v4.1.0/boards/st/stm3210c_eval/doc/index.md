---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/stm3210c_eval/doc/index.html
original_path: boards/st/stm3210c_eval/doc/index.html
---

# STM3210C Evaluation

Board Overview

[![../../../../_images/stm3210c_eval.jpg](../../../../_images/stm3210c_eval.jpg)
](../../../../_images/stm3210c_eval.jpg)

STM3210C Evaluation

Name:
:   `stm3210c_eval`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32f107xc

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm3210c_eval/doc/index.rst/../..)

## Overview

The STM3210C-EVAL evaluation board is a complete development platform for STMicroelectronic’s
ARM Cortex-M3 core-based STM32F107VCT microcontroller.

The range of hardware features on the board help you to evaluate all peripherals
(USB-OTG FS, ethernet, motor control, CAN, microSD CardTM, smartcard, USART,
audio DAC, MEMS, EEPROM and more) and develop your own applications.

Extension headers make it easy to connect a daughterboard or wrapping board for your specific
application.

More information about the board can be found at the [STM3210C-EVAL website](https://www.st.com/en/evaluation-tools/stm3210c-eval.html) [[1]](#id2).

## Hardware

STM3210C-EVAL provides the following hardware components:

- Three 5 V power supply options:
  :   - Power jack
      - USB connector
      - daughterboard
- Boot from user Flash, system memory or SRAM.
- I2S audio DAC, stereo audio jack.
- 2 GByte (or more) microSD CardTM.
- Both type A and B smartcard support.
- I2C compatible serial interface 64 Kbit EEPROM, MEMS and I/O expander.
- RS-232 communication.
- IrDA transceiver.
- USB-OTG full speed, USB microAB connector.
- IEEE-802.3-2002 compliant ethernet connector.
- Two channels of CAN2.0A/B compliant connection.
- Inductor motor control connector.
- JTAG and trace debug support.
- 3.2” 240x320 TFT color LCD with touch screen.
- Joystick with 4-direction control and selector.
- Reset, Wakeup, Tamper and User button.
- 4 color LEDs.
- RTC with backup battery.
- MCU consumption measurement circuit.
- Extension connector for daughterboard or wrapping board.

More information about STM32F107VCT can be found here:
:   - [STM32F107VCT reference manual](https://www.st.com/resource/en/reference_manual/CD00171190.pdf) [[2]](#id4)

### Supported Features

The `stm3210c_eval` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

Each of the GPIO pins can be configured by software as output (push-pull or open-drain), as
input (with or without pull-up or pull-down), or as peripheral alternate function. Most of the
GPIO pins are shared with digital or analog alternate functions. All GPIOs are high current
capable except for analog inputs.

#### Board connectors:

![STM3210C_EVAL connectors](../../../../_images/stm3210c_eval_connectors.jpg)

#### Default Zephyr Peripheral Mapping:

- UART\_2\_TX : PD5
- UART\_2\_RX : PD6
- USER\_PB : PB9
- LED2 : PD13

## Programming and Debugging

### Flashing

STM3210C-EVAL board includes an ST-LINK/V2-1 embedded debug tool interface.
At power-on, the board is in firmware-upgrade mode (also called DFU for
“Device Firmware Upgrade”), allowing the firmware to be updated through the USB.
This interface is supported by the openocd version included in Zephyr SDK.

Applications for the `stm3210c_eval` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

#### Flashing an application to STM3210C-EVAL

Connect the STM3210C-EVAL to your host computer using the USB port, then build
and flash an application in the usual way.

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b stm3210c_eval samples/basic/blinky
west flash
```

You will see the LED blinking every second.

### Debugging

You can run a serial host program to connect with your STM3210C-EVAL board. For
example, on Linux:

```shell
$ minicom -D /dev/ttyACM0
```

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b stm3210c_eval samples/hello_world
west debug
```

## References

[[1](#id3)]

[https://www.st.com/en/evaluation-tools/stm3210c-eval.html](https://www.st.com/en/evaluation-tools/stm3210c-eval.html)

[[2](#id5)]

[https://www.st.com/resource/en/reference\_manual/CD00171190.pdf](https://www.st.com/resource/en/reference_manual/CD00171190.pdf)

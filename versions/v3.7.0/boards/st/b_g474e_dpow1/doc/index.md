---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/st/b_g474e_dpow1/doc/index.html
original_path: boards/st/b_g474e_dpow1/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# ST B-G474E-DPOW1 Discovery

## Overview

The B-G474E-DPOW1 Discovery kit is a digital power solution and a complete
demonstration and development platform for the STMicroelectronics STM32G474RET6
microcontroller. Leveraging the new HRTimer-oriented features, 96 Kbytes of
embedded RAM, math accelerator functions and USB-PD 3.0 offered by STM32G474RET6,
the B-G474E-DPOW1 Discovery kit, based on the USB 2.0 FS Type-C™ connector
interface, helps the user to prototype applications with digital power such as a
buck-boost converter, RGB power LED lighting or a class-D audio amplifier. The
B-G474E-DPOW1 Discovery kit does not require any separate probe, as it integrates
the STLINK-V3E debugger and programmer.

- STM32G474RET6 Arm® Cortex®-M4 core-based microcontroller, featuring 512 Kbytes
  of Flash memory and 128 Kbytes of SRAM, in LQFP64 package
- USB Type-C™ with USB 2.0 FS interface compatible with USB-PD 3.0
- RGB power LED for a bright lighting
- Digital power buck-boost converter with internal or external Input voltage and
  with onboard resistor loads
- Audio Class-D amplifier capable
- 4 user LEDs
- 3 LEDs for power and ST-LINK communication
- 4-direction joystick with a selection button
- Reset push-button
- Board connectors:
  :   - USB Type-C™
      - USB Micro-B
      - 2 x 32-pin header, 2.54 mm pitch, daughterboard extension connector for breadboard connection
- Flexible power-supply options: ST-LINK USB VBUS or USB Type-C™ VBUS or external source
- On-board STLINK-V3E debugger/programmer with USB re-enumeration capability: mass storage,
  Virtual COM port, and debug port

![B-G474E-DPOW1](../../../../_images/b_g474e_dpow1.jpg)

More information about the board can be found at the [B-G474E-DPOW1 website](https://www.st.com/en/evaluation-tools/b-g474e-dpow1.html) [[1]](#id1).

More information about STM32G474RE can be found here:

- [G474RE on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32g474re.html) [[4]](#id7)
- [STM32G4 reference manual](https://www.st.com/resource/en/reference_manual/rm0440-stm32g4-series-advanced-armbased-32bit-mcus-stmicroelectronics.pdf) [[2]](#id3)

### Supported Features

The Zephyr b\_g474e\_dpow1 board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port-polling; serial port-interrupt |
| GPIO | on-chip | gpio |
| USB | on-chip | usb |
| UCPD | on-chip | ucpd |
| WATCHDOG | on-chip | independent watchdog |

Other hardware features are not yet supported in this Zephyr port.

The default configuration can be found in the defconfig file:
[boards/st/b\_g474e\_dpow1/b\_g474e\_dpow1\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/b_g474e_dpow1/b_g474e_dpow1_defconfig)

### Connections and IOs

Each of the GPIO pins can be configured by software as output (push-pull or open-drain), as
input (with or without pull-up or pull-down), or as peripheral alternate function. Most of the
GPIO pins are shared with digital or analog alternate functions. All GPIOs are high current
capable except for analog inputs.

#### Default Zephyr Peripheral Mapping:

- UART\_3 TX/RX : PC10/PC11 (ST-Link Virtual Port Com)
- BUTTON (JOY\_SEL) : PC13
- BUTTON (JOY\_LEFT) : PC4
- BUTTON (JOY\_DOWN) : PC5
- BUTTON (JOY\_RIGHT) : PB2
- BUTTON (JOY\_UP) : PB10
- LED (DOWN BLUE) : PA15
- LED (LEFT ORANGE) : PB1
- LED (UP RED) : PB5
- LED (RIGHT GREEN) : PB7
- USB DM : PA11
- USB DP : PA12
- UCPD CC2 : PB4
- UCPD CC1 : PB6

For more details please refer to [B-G474E-DPOW1 Discovery board User Manual](https://www.st.com/resource/en/user_manual/um2577-discovery-kit-with-stm32g474re-mcu-stmicroelectronics.pdf) [[3]](#id5).

## Programming and Debugging

Applications for the `b_g474e_dpow1` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The B-G474E-DPOW1 Discovery board includes an ST-LINK/V3E embedded debug tool interface.

```shell
$ west flash
```

#### Flashing an application to the B\_G474E\_DPOW1

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b b_g474e_dpow1 samples/basic/blinky
west flash
```

You will see the LED blinking every second.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b b_g474e_dpow1 samples/hello_world
west debug
```

## References

[[1](#id2)]

[https://www.st.com/en/evaluation-tools/b-g474e-dpow1.html](https://www.st.com/en/evaluation-tools/b-g474e-dpow1.html)

[[2](#id4)]

[https://www.st.com/resource/en/reference\_manual/rm0440-stm32g4-series-advanced-armbased-32bit-mcus-stmicroelectronics.pdf](https://www.st.com/resource/en/reference_manual/rm0440-stm32g4-series-advanced-armbased-32bit-mcus-stmicroelectronics.pdf)

[[3](#id6)]

[https://www.st.com/resource/en/user\_manual/um2577-discovery-kit-with-stm32g474re-mcu-stmicroelectronics.pdf](https://www.st.com/resource/en/user_manual/um2577-discovery-kit-with-stm32g474re-mcu-stmicroelectronics.pdf)

[[4](#id8)]

[https://www.st.com/en/microcontrollers-microprocessors/stm32g474re.html](https://www.st.com/en/microcontrollers-microprocessors/stm32g474re.html)

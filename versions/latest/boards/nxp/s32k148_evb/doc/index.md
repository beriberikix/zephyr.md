---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/s32k148_evb/doc/index.html
original_path: boards/nxp/s32k148_evb/doc/index.html
---

# S32K148EVB-Q176

Board Overview

[![../../../../_images/s32k148_evb.webp](../../../../_images/s32k148_evb.webp)
](../../../../_images/s32k148_evb.webp)

S32K148EVB-Q176

Name:
:   `s32k148_evb`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   s32k148

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/s32k148_evb/doc/index.rst/../..)

## Overview

[NXP S32K148-Q176](https://www.nxp.com/design/design-center/development-boards-and-designs/automotive-development-platforms/s32k-mcu-platforms/s32k148-q176-evaluation-board-for-automotive-general-purpose:S32K148EVB) [[8]](#id18) is a low-cost evaluation and development board for general-purpose industrial
and automotive applications.
The S32K148-Q176 is based on the 32-bit Arm Cortex-M4F [NXP S32K148](https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32k-auto-general-purpose-mcus/s32k1-microcontrollers-for-automotive-general-purpose:S32K1) [[9]](#id21) microcontroller.
The onboard OpenSDA serial and debug adapter, running a mass storage device (MSD) bootloader
and a collection of OpenSDA Applications, offers options for serial communication,
flash programming, and run-control debugging.
It is a bridge between a USB host and the embedded target processor.

## Hardware

- NXP S32K148

  - Arm Cortex-M4F @ up to 112 Mhz
  - 1.5 MB Flash
  - 256 KB SRAM
  - up to 127 I/Os
  - 3x FlexCAN with FD
  - eDMA, 12-bit ADC, MPU, ECC and more.
- Interfaces

  - CAN, LIN, UART/SCI
  - Ethernet connector compatible with different ethernet daughter cards
  - 2 touchpads, potentiometer, user RGB LED and 2 buttons.

More information about the hardware and design resources can be found at
[NXP S32K148-Q176](https://www.nxp.com/design/design-center/development-boards-and-designs/automotive-development-platforms/s32k-mcu-platforms/s32k148-q176-evaluation-board-for-automotive-general-purpose:S32K148EVB) [[8]](#id18) website.

### Supported Features

The `s32k148_evb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

Note

Before using the Ethernet interface, please take note of the following:

- For boards with the part number `LSF24D` at `U16`, `R553` needs to be depopulated.

### Connections and IOs

This board has 5 GPIO ports named from `gpioa` to `gpioe`.

Pin control can be further configured from your application overlay by adding
children nodes with the desired pinmux configuration to the singleton node
`pinctrl`. Supported properties are described in
[dts/bindings/pinctrl/nxp,port-pinctrl.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/bindings/pinctrl/nxp,port-pinctrl.yaml).

#### LEDs

The NXP S32K148-Q176 board has one user RGB LED that can be used either as a GPIO
LED or as a PWM LED.

RGB LED as GPIO LED

| Devicetree node | Devicetree alias | Label | Pin |
| --- | --- | --- | --- |
| led1\_red | led0 | LED1\_RGB\_RED | PTE21 |
| led1\_green | led1 | LED1\_RGB\_GREEN | PTE22 |
| led1\_blue | led2 | LED1\_RGB\_BLUE | PTE23 |

RGB LED as PWM LED

| Devicetree node | Devicetree alias | Label | Pin |
| --- | --- | --- | --- |
| led1\_red\_pwm | pwm-led0 / red-pwm-led | LED1\_RGB\_RED\_PWM | PTE21 / FTM4\_CH1 |
| led1\_green\_pwm | pwm-led1 / green-pwm-led | LED1\_RGB\_GREEN\_PWM | PTE22 / FTM4\_CH2 |
| led1\_blue\_pwm | pwm-led2 / blue-pwm-led | LED1\_RGB\_BLUE\_PWM | PTE23 / FTM4\_CH3 |

The user can control the LEDs in any way. An output of `0` illuminates the LED.

#### Buttons

The NXP S32K148-Q176 board has two user buttons:

| Devicetree node | Label | Pin |
| --- | --- | --- |
| sw0 / button\_3 | SW3 | PTC12 |
| sw1 / button\_4 | SW4 | PTC13 |

### Serial Console

The serial console is provided via `lpuart1` on the OpenSDA adapter.

| Pin | Pin Function |
| --- | --- |
| PTC7 | LPUART1\_TX |
| PTC6 | LPUART1\_RX |

### System Clock

The Arm Cortex-M4F core is configured to run at 80 MHz (RUN mode).

## Programming and Debugging

The `s32k148_evb` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

Applications for the `s32k148_evb` board can be built in the usual way as
documented in [Building an Application](../../../../develop/application/index.md#build-an-application).

This board configuration supports [SEGGER J-Link](https://wiki.segger.com/S32Kxxx) [[10]](#id23) West runner for flashing and
debugging applications. Follow the steps described in [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools),
to setup the flash and debug host tools for this runner.

### Flashing

Run the `west flash` command to flash the application using SEGGER J-Link.

### Debugging

Run the `west debug` command to start a GDB session using SEGGER J-Link.

### Configuring a Console

We will use OpenSDA as a USB-to-serial adapter for the serial console.

Use the following settings with your serial terminal of choice (minicom, putty, etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk) [[1]](#id4)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC) [[2]](#id6), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) [[3]](#id8) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started) [[4]](#id10)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548) [[5]](#id12)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) [[6]](#id14) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project) [[7]](#id16)

## References

[[1](#id5)]

[https://github.com/nxp-zephyr/nxp-zsdk](https://github.com/nxp-zephyr/nxp-zsdk)

[[2](#id7)]

[https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC)

[[3](#id9)]

[https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki)

[[4](#id11)]

[https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)

[[5](#id13)]

[https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)

[[6](#id15)]

[https://nxp.com/zephyr](https://nxp.com/zephyr)

[[7](#id17)]

[https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

[8]
([1](#id19),[2](#id20))

[https://www.nxp.com/design/design-center/development-boards-and-designs/automotive-development-platforms/s32k-mcu-platforms/s32k148-q176-evaluation-board-for-automotive-general-purpose:S32K148EVB](https://www.nxp.com/design/design-center/development-boards-and-designs/automotive-development-platforms/s32k-mcu-platforms/s32k148-q176-evaluation-board-for-automotive-general-purpose:S32K148EVB)

[[9](#id22)]

[https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32k-auto-general-purpose-mcus/s32k1-microcontrollers-for-automotive-general-purpose:S32K1](https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32k-auto-general-purpose-mcus/s32k1-microcontrollers-for-automotive-general-purpose:S32K1)

[[10](#id24)]

[https://wiki.segger.com/S32Kxxx](https://wiki.segger.com/S32Kxxx)

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

#### `s32k148_evb/s32k148` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L20) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | NXP ADC12[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L336) | [`nxp,adc12`](../../../../build/dts/api/bindings/adc/nxp%2Cadc12.md#std-dtcompatible-nxp-adc12) |
| CAN | on-chip | NXP FlexCAN CANFD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L51)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L59) | [`nxp,flexcan-fd`](../../../../build/dts/api/bindings/can/nxp%2Cflexcan-fd.md#std-dtcompatible-nxp-flexcan-fd) |
| Clock control | on-chip | NXP S32 clock generator IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L146) | [`nxp,s32-clock`](../../../../build/dts/api/bindings/clock/nxp%2Cs32-clock.md#std-dtcompatible-nxp-s32-clock) |
| Ethernet | on-chip | NXP ENET IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k148.dtsi?plain=1#L34) | [`nxp,enet`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet.md#std-dtcompatible-nxp-enet) |
| on-chip | NXP ENET MAC/L2 Device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k148.dtsi?plain=1#L39) | [`nxp,enet-mac`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet-mac.md#std-dtcompatible-nxp-enet-mac) |
| on-chip | NXP ENET PTP (Precision Time Protocol) Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k148.dtsi?plain=1#L54) | [`nxp,enet-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock) |
| GPIO & Headers | on-chip | Kinetis GPIO[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L197) | [`nxp,kinetis-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Ckinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio) |
| I2C | on-chip | NXP LPI2C controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L153)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L164) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp%2Clpi2c.md#std-dtcompatible-nxp-lpi2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32k148_evb/s32k148_evb.dts?plain=1#L80) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32k148_evb/s32k148_evb.dts?plain=1#L42) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32k148_evb/s32k148_evb.dts?plain=1#L61) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MDIO | on-chip | NXP ENET MDIO Features[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k148.dtsi?plain=1#L48) | [`nxp,enet-mdio`](../../../../build/dts/api/bindings/mdio/nxp%2Cenet-mdio.md#std-dtcompatible-nxp-enet-mdio) |
| MMU / MPU | on-chip | NXP System Memory Protection Unit (SYSMPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L35) | [`nxp,sysmpu`](../../../../build/dts/api/bindings/mmu_mpu/nxp%2Csysmpu.md#std-dtcompatible-nxp-sysmpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k148.dtsi?plain=1#L68) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | NXP PORT Pin Controller[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L107) | [`nxp,port-pinmux`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cport-pinmux.md#std-dtcompatible-nxp-port-pinmux) |
| on-chip | NXP PORT Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L27) | [`nxp,port-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cport-pinctrl.md#std-dtcompatible-nxp-port-pinctrl) |
| PWM | on-chip | NXP FlexTimer Module (FTM) PWM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L287) | [`nxp,ftm-pwm`](../../../../build/dts/api/bindings/pwm/nxp%2Cftm-pwm.md#std-dtcompatible-nxp-ftm-pwm) |
| RTC | on-chip | NXP Real Time Clock (RTC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L327) | [`nxp,rtc`](../../../../build/dts/api/bindings/rtc/nxp%2Crtc.md#std-dtcompatible-nxp-rtc) |
| Serial controller | on-chip | NXP LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L182)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L174) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp%2Clpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP LPSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L73)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L85) | [`nxp,lpspi`](../../../../build/dts/api/bindings/spi/nxp%2Clpspi.md#std-dtcompatible-nxp-lpspi) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k148.dtsi?plain=1#L24) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | NXP FlexTimer Module (FTM)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L247) | [`nxp,ftm`](../../../../build/dts/api/bindings/timer/nxp%2Cftm.md#std-dtcompatible-nxp-ftm) |
| Watchdog | on-chip | NXP watchdog (WDOG32)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L137) | [`nxp,wdog32`](../../../../build/dts/api/bindings/watchdog/nxp%2Cwdog32.md#std-dtcompatible-nxp-wdog32) |

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

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

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

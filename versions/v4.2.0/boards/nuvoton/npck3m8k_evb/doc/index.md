---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nuvoton/npck3m8k_evb/doc/index.html
original_path: boards/nuvoton/npck3m8k_evb/doc/index.html
---

# NPCK3M8K\_EVB

Board Overview

[![../../../../_images/npck3m8k_evb.webp](../../../../_images/npck3m8k_evb.webp)
](../../../../_images/npck3m8k_evb.webp)

NPCK3M8K\_EVB

Name:
:   `npck3m8k_evb`

Vendor:
:   Nuvoton Technology Corporation

Architecture:
:   arm

SoC:
:   npck3m8k

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nuvoton/npck3m8k_evb/doc/index.rst/../..)

## Overview

The NPCK3M8K\_EVB kit is a development platform to evaluate the
Nuvoton NPCK3 series microcontrollers. This board is designed to provide
a range of peripherals and interfaces for development and testing. It needs
to be mated with part number NPCK3M8K.

## Hardware

- ARM Cortex-M4F Processor
- 352 KB RAM and 64 KB boot ROM
- GPIO headers
- UART0 and UART1
- JTAG interface

### Supported Features

The `npck3m8k_evb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `npck3m8k_evb/npck3m8k` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L26) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | Nuvoton, NPCX-ADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L368) | [`nuvoton,npcx-adc`](../../../../build/dts/api/bindings/adc/nuvoton%2Cnpcx-adc.md#std-dtcompatible-nuvoton-npcx-adc) |
| Clock control | on-chip | Nuvoton, NPCX PCC (Power and Clock Controller) node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L79) | [`nuvoton,npcx-pcc`](../../../../build/dts/api/bindings/clock/nuvoton%2Cnpcx-pcc.md#std-dtcompatible-nuvoton-npcx-pcc) |
| ESPI | on-chip | Nuvoton NPCX eSPI Virtual Wire (VW) mapping child node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck-espi-vws-map.dtsi?plain=1#L33) | [`nuvoton,npcx-espi-vw-conf`](../../../../build/dts/api/bindings/espi/nuvoton%2Cnpcx-espi-vw-conf.md#std-dtcompatible-nuvoton-npcx-espi-vw-conf) |
| on-chip | Nuvoton, NPCX-eSPI node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L384) | [`nuvoton,npcx-espi`](../../../../build/dts/api/bindings/espi/nuvoton%2Cnpcx-espi.md#std-dtcompatible-nuvoton-npcx-espi) |
| on-chip | The target flash devices accessed by Nuvoton eSPI TAF controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck3.dtsi?plain=1#L256) | [`nuvoton,npcx-espi-taf`](../../../../build/dts/api/bindings/espi/nuvoton%2Cnpcx-espi-taf.md#std-dtcompatible-nuvoton-npcx-espi-taf) |
| on-chip | Nuvoton, NPCX-Host Sub-Modules node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L400) | [`nuvoton,npcx-host-sub`](../../../../build/dts/api/bindings/espi/nuvoton%2Cnpcx-host-sub.md#std-dtcompatible-nuvoton-npcx-host-sub) |
| on-chip | Nuvoton, NPCX-Host UART IO node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L580) | [`nuvoton,npcx-host-uart`](../../../../build/dts/api/bindings/espi/nuvoton%2Cnpcx-host-uart.md#std-dtcompatible-nuvoton-npcx-host-uart) |
| Flash controller | on-chip | Properties defining the NPCX Quad-SPI peripheral of Flash Interface Unit (FIU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L546) | [`nuvoton,npcx-fiu-qspi`](../../../../build/dts/api/bindings/flash_controller/nuvoton%2Cnpcx-fiu-qspi.md#std-dtcompatible-nuvoton-npcx-fiu-qspi) |
| GPIO & Headers | on-chip | Nuvoton, NPCX-GPIO[20 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L136) | [`nuvoton,npcx-gpio`](../../../../build/dts/api/bindings/gpio/nuvoton%2Cnpcx-gpio.md#std-dtcompatible-nuvoton-npcx-gpio) |
| I2C | on-chip | Nuvoton NPCX-I2C controller[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L436) | [`nuvoton,npcx-i2c-ctrl`](../../../../build/dts/api/bindings/i2c/nuvoton%2Cnpcx-i2c-ctrl.md#std-dtcompatible-nuvoton-npcx-i2c-ctrl) |
| on-chip | Nuvoton NPCX-I2C port pads[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L585) | [`nuvoton,npcx-i2c-port`](../../../../build/dts/api/bindings/i2c/nuvoton%2Cnpcx-i2c-port.md#std-dtcompatible-nuvoton-npcx-i2c-port) |
| Input | on-chip | Nuvoton NPCX keyboard scan controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L564) | [`nuvoton,npcx-kbd`](../../../../build/dts/api/bindings/input/nuvoton%2Cnpcx-kbd.md#std-dtcompatible-nuvoton-npcx-kbd) |
| Interrupt controller | on-chip | NPCX-MIWU Wake-Up Unit Input (WUI) mapping child node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck-miwus-wui-map.dtsi?plain=1#L9) | [`nuvoton,npcx-miwu-wui-map`](../../../../build/dts/api/bindings/interrupt-controller/nuvoton%2Cnpcx-miwu-wui-map.md#std-dtcompatible-nuvoton-npcx-miwu-wui-map) |
| on-chip | Nuvoton, NPCX Multi-Input Wake-Up Unit (MIWU) node[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L115)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck-miwus-wui-map.dtsi?plain=1#L602) | [`nuvoton,npcx-miwu`](../../../../build/dts/api/bindings/interrupt-controller/nuvoton%2Cnpcx-miwu.md#std-dtcompatible-nuvoton-npcx-miwu) |
| on-chip | NPCX-MIWU group-interrupt mapping child node[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck-miwus-int-map.dtsi?plain=1#L10) | [`nuvoton,npcx-miwu-int-map`](../../../../build/dts/api/bindings/interrupt-controller/nuvoton%2Cnpcx-miwu-int-map.md#std-dtcompatible-nuvoton-npcx-miwu-int-map) |
| on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nuvoton/npck3m8k_evb/npck3m8k_evb.dts?plain=1#L46) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nuvoton/npck3m8k_evb/npck3m8k_evb.dts?plain=1#L55) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Memory controller | on-chip | Nuvoton, NPCX Battery Backed RAM node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L72) | [`nuvoton,npcx-bbram`](../../../../build/dts/api/bindings/memory-controllers/nuvoton%2Cnpcx-bbram.md#std-dtcompatible-nuvoton-npcx-bbram) |
| Miscellaneous | on-chip | Nuvoton, NPCX soc ID[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L681) | [`nuvoton,npcx-soc-id`](../../../../build/dts/api/bindings/misc/nuvoton%2Cnpcx-soc-id.md#std-dtcompatible-nuvoton-npcx-soc-id) |
| on-chip | Nuvoton, NPCX booter variant options[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L686) | [`nuvoton,npcx-booter-variant`](../../../../build/dts/api/bindings/misc/nuvoton%2Cnpcx-booter-variant.md#std-dtcompatible-nuvoton-npcx-booter-variant) |
| PECI | on-chip | Nuvoton NPCX PECI node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L554) | [`nuvoton,npcx-peci`](../../../../build/dts/api/bindings/peci/nuvoton%2Cnpcx-peci.md#std-dtcompatible-nuvoton-npcx-peci) |
| Pin control | on-chip | Nuvoton NPCX7 Pin-Mux Configuration Configuration map from Nuvoton NPCX GPIO to pinmux controller (SCFG) driver instances[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck-alts-map.dtsi?plain=1#L8) | [`nuvoton,npcx-pinctrl-conf`](../../../../build/dts/api/bindings/pinctrl/nuvoton%2Cnpcx-pinctrl-conf.md#std-dtcompatible-nuvoton-npcx-pinctrl-conf) |
| on-chip | Nuvoton NPCX7 Low-Voltage level detection configuration map between Nuvoton NPCX GPIO and low-voltage controller (LV\_GPIO\_CTL) driver instances[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck-lvol-ctrl-map.dtsi?plain=1#L8) | [`nuvoton,npcx-lvolctrl-conf`](../../../../build/dts/api/bindings/pinctrl/nuvoton%2Cnpcx-lvolctrl-conf.md#std-dtcompatible-nuvoton-npcx-lvolctrl-conf) |
| on-chip | Nuvoton NPCX System Configuration (Pinmux, 1.8V support and so on)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L90) | [`nuvoton,npcx-scfg`](../../../../build/dts/api/bindings/pinctrl/nuvoton%2Cnpcx-scfg.md#std-dtcompatible-nuvoton-npcx-scfg) |
| on-chip | Nuvoton, NPCX Default Pins Configurations[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L49) | [`nuvoton,npcx-pinctrl-def`](../../../../build/dts/api/bindings/pinctrl/nuvoton%2Cnpcx-pinctrl-def.md#std-dtcompatible-nuvoton-npcx-pinctrl-def) |
| on-chip | The Nuvoton pin controller is a singleton node responsible for controlling pin function selection and pin properties[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L58) | [`nuvoton,npcx-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nuvoton%2Cnpcx-pinctrl.md#std-dtcompatible-nuvoton-npcx-pinctrl) |
| on-chip | Nuvoton, NPCX power leakage IOs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L66) | [`nuvoton,npcx-leakage-io`](../../../../build/dts/api/bindings/pinctrl/nuvoton%2Cnpcx-leakage-io.md#std-dtcompatible-nuvoton-npcx-leakage-io) |
| Power management | on-chip | Nuvoton, NPCX Power Switch Logic (PSL) control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L675) | [`nuvoton,npcx-power-psl`](../../../../build/dts/api/bindings/power/nuvoton%2Cnpcx-power-psl.md#std-dtcompatible-nuvoton-npcx-power-psl) |
| PS/2 | on-chip | Nuvoton, NPCX-PS/2 controller node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L525) | [`nuvoton,npcx-ps2-ctrl`](../../../../build/dts/api/bindings/ps2/nuvoton%2Cnpcx-ps2-ctrl.md#std-dtcompatible-nuvoton-npcx-ps2-ctrl) |
| on-chip | Nuvoton, NPCX-PS/2 channel pads node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L532) | [`nuvoton,npcx-ps2-channel`](../../../../build/dts/api/bindings/ps2/nuvoton%2Cnpcx-ps2-channel.md#std-dtcompatible-nuvoton-npcx-ps2-channel) |
| PWM | on-chip | Nuvoton, NPCX Pulse Width Modulator (PWM) node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L305)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L296) | [`nuvoton,npcx-pwm`](../../../../build/dts/api/bindings/pwm/nuvoton%2Cnpcx-pwm.md#std-dtcompatible-nuvoton-npcx-pwm) |
| Serial controller | on-chip | Nuvoton, NPCX-UART node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck3.dtsi?plain=1#L56) | [`nuvoton,npcx-uart`](../../../../build/dts/api/bindings/serial/nuvoton%2Cnpcx-uart.md#std-dtcompatible-nuvoton-npcx-uart) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck3m8k.dtsi?plain=1#L19) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| System controller | on-chip | System Controller Registers R/W[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L103) | [`syscon`](../../../../build/dts/api/bindings/syscon/syscon.md#std-dtcompatible-syscon) |
| Tachometer | on-chip | Nuvoton NPCX Tachometer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L490)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L497) | [`nuvoton,npcx-tach`](../../../../build/dts/api/bindings/tach/nuvoton%2Cnpcx-tach.md#std-dtcompatible-nuvoton-npcx-tach) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | Nuvoton NPCX Internal Timer (ITIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck3.dtsi?plain=1#L45) | [`nuvoton,npcx-itim-timer`](../../../../build/dts/api/bindings/timer/nuvoton%2Cnpcx-itim-timer.md#std-dtcompatible-nuvoton-npcx-itim-timer) |
| Watchdog | on-chip | Nuvoton, NPCX-TWD[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npck/npck.dtsi?plain=1#L378) | [`nuvoton,npcx-watchdog`](../../../../build/dts/api/bindings/watchdog/nuvoton%2Cnpcx-watchdog.md#std-dtcompatible-nuvoton-npcx-watchdog) |

### System Clock

The NPCK3M8K MCU is configured to use the 90Mhz internal oscillator with the
on-chip PLL to generate a resulting EC clock rate of 15 MHz. See Processor clock
control register (chapter 4 in user manual)

### Serial Port

UART1 is configured for serial logs.

## Programming and Debugging

The `npck3m8k_evb` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

This board comes with a Cortex ETM port which facilitates tracing and debugging
using a single physical connection. In addition, it comes with sockets for
JTAG only sessions.

### Flashing

Build the application as usual for the `npck3m8k_evb` board.

### Debugging

Use JTAG/SWD with a J-Link.

## References

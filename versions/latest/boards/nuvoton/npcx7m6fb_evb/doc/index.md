---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nuvoton/npcx7m6fb_evb/doc/index.html
original_path: boards/nuvoton/npcx7m6fb_evb/doc/index.html
---

# NPCX7M6FB\_EVB

Board Overview

[![../../../../_images/npcx7m6fb_evb.jpg](../../../../_images/npcx7m6fb_evb.jpg)
](../../../../_images/npcx7m6fb_evb.jpg)

NPCX7M6FB\_EVB

Name:
:   `npcx7m6fb_evb`

Vendor:
:   Nuvoton Technology Corporation

Architecture:
:   arm

SoC:
:   npcx7m6fb

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nuvoton/npcx7m6fb_evb/doc/index.rst/../..)

## Overview

The NPCX7M6FB\_EVB kit is a development platform to evaluate the
Nuvoton NPCX7 series microcontrollers. This board needs to be mated with
part number NPCX796FB.

## Hardware

- ARM Cortex-M4F Processor
- 256 KB RAM and 64 KB boot ROM
- ADC & GPIO headers
- UART0 and UART1
- FAN PWM interface
- Jtag interface
- Intel Modular Embedded Controller Card (MECC) headers

### Supported Features

The `npcx7m6fb_evb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `npcx7m6fb_evb/npcx7m6fb` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L26) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | Nuvoton, NPCX-ADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L324) | [`nuvoton,npcx-adc`](../../../../build/dts/api/bindings/adc/nuvoton%2Cnpcx-adc.md#std-dtcompatible-nuvoton-npcx-adc) |
| Clock control | on-chip | Nuvoton, NPCX PCC (Power and Clock Controller) node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L67) | [`nuvoton,npcx-pcc`](../../../../build/dts/api/bindings/clock/nuvoton%2Cnpcx-pcc.md#std-dtcompatible-nuvoton-npcx-pcc) |
| ESPI | on-chip | Nuvoton NPCX eSPI Virtual Wire (VW) mapping child node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx-espi-vws-map.dtsi?plain=1#L33) | [`nuvoton,npcx-espi-vw-conf`](../../../../build/dts/api/bindings/espi/nuvoton%2Cnpcx-espi-vw-conf.md#std-dtcompatible-nuvoton-npcx-espi-vw-conf) |
| on-chip | Nuvoton, NPCX-eSPI node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L340) | [`nuvoton,npcx-espi`](../../../../build/dts/api/bindings/espi/nuvoton%2Cnpcx-espi.md#std-dtcompatible-nuvoton-npcx-espi) |
| on-chip | Nuvoton, NPCX-Host Sub-Modules node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L356) | [`nuvoton,npcx-host-sub`](../../../../build/dts/api/bindings/espi/nuvoton%2Cnpcx-host-sub.md#std-dtcompatible-nuvoton-npcx-host-sub) |
| on-chip | Nuvoton, NPCX-Host UART IO node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L479) | [`nuvoton,npcx-host-uart`](../../../../build/dts/api/bindings/espi/nuvoton%2Cnpcx-host-uart.md#std-dtcompatible-nuvoton-npcx-host-uart) |
| Flash controller | on-chip | Properties defining the NPCX Quad-SPI peripheral of Flash Interface Unit (FIU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L435) | [`nuvoton,npcx-fiu-qspi`](../../../../build/dts/api/bindings/flash_controller/nuvoton%2Cnpcx-fiu-qspi.md#std-dtcompatible-nuvoton-npcx-fiu-qspi) |
| on-chip | The SPI NOR flash devices accessed by Nuvoton Flash Interface Unit (FIU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx7m6fb.dtsi?plain=1#L38) | [`nuvoton,npcx-fiu-nor`](../../../../build/dts/api/bindings/flash_controller/nuvoton%2Cnpcx-fiu-nor.md#std-dtcompatible-nuvoton-npcx-fiu-nor) |
| GPIO & Headers | on-chip | Nuvoton, NPCX-GPIO[16 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L124) | [`nuvoton,npcx-gpio`](../../../../build/dts/api/bindings/gpio/nuvoton%2Cnpcx-gpio.md#std-dtcompatible-nuvoton-npcx-gpio) |
| I2C | on-chip | Nuvoton NPCX-I2C controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx7.dtsi?plain=1#L268)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx7.dtsi?plain=1#L277) | [`nuvoton,npcx-i2c-ctrl`](../../../../build/dts/api/bindings/i2c/nuvoton%2Cnpcx-i2c-ctrl.md#std-dtcompatible-nuvoton-npcx-i2c-ctrl) |
| on-chip | Nuvoton NPCX-I2C port pads[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L484)[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L493) | [`nuvoton,npcx-i2c-port`](../../../../build/dts/api/bindings/i2c/nuvoton%2Cnpcx-i2c-port.md#std-dtcompatible-nuvoton-npcx-i2c-port) |
| Input | on-chip | Nuvoton NPCX keyboard scan controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L452) | [`nuvoton,npcx-kbd`](../../../../build/dts/api/bindings/input/nuvoton%2Cnpcx-kbd.md#std-dtcompatible-nuvoton-npcx-kbd) |
| Interrupt controller | on-chip | NPCX-MIWU Wake-Up Unit Input (WUI) mapping child node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx-miwus-wui-map.dtsi?plain=1#L9) | [`nuvoton,npcx-miwu-wui-map`](../../../../build/dts/api/bindings/interrupt-controller/nuvoton%2Cnpcx-miwu-wui-map.md#std-dtcompatible-nuvoton-npcx-miwu-wui-map) |
| on-chip | Nuvoton, NPCX Multi-Input Wake-Up Unit (MIWU) node[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L103)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx-miwus-wui-map.dtsi?plain=1#L497) | [`nuvoton,npcx-miwu`](../../../../build/dts/api/bindings/interrupt-controller/nuvoton%2Cnpcx-miwu.md#std-dtcompatible-nuvoton-npcx-miwu) |
| on-chip | NPCX-MIWU group-interrupt mapping child node[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx-miwus-int-map.dtsi?plain=1#L10) | [`nuvoton,npcx-miwu-int-map`](../../../../build/dts/api/bindings/interrupt-controller/nuvoton%2Cnpcx-miwu-int-map.md#std-dtcompatible-nuvoton-npcx-miwu-int-map) |
| on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nuvoton/npcx7m6fb_evb/npcx7m6fb_evb.dts?plain=1#L33) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Memory controller | on-chip | Nuvoton, NPCX Battery Backed RAM node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx7.dtsi?plain=1#L84) | [`nuvoton,npcx-bbram`](../../../../build/dts/api/bindings/memory-controllers/nuvoton%2Cnpcx-bbram.md#std-dtcompatible-nuvoton-npcx-bbram) |
| Miscellaneous | on-chip | Nuvoton, NPCX soc ID[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L580) | [`nuvoton,npcx-soc-id`](../../../../build/dts/api/bindings/misc/nuvoton%2Cnpcx-soc-id.md#std-dtcompatible-nuvoton-npcx-soc-id) |
| on-chip | Nuvoton, NPCX booter variant options[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L585) | [`nuvoton,npcx-booter-variant`](../../../../build/dts/api/bindings/misc/nuvoton%2Cnpcx-booter-variant.md#std-dtcompatible-nuvoton-npcx-booter-variant) |
| PECI | on-chip | Nuvoton NPCX PECI node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L442) | [`nuvoton,npcx-peci`](../../../../build/dts/api/bindings/peci/nuvoton%2Cnpcx-peci.md#std-dtcompatible-nuvoton-npcx-peci) |
| Pin control | on-chip | Nuvoton NPCX7 Pin-Mux Configuration Configuration map from Nuvoton NPCX GPIO to pinmux controller (SCFG) driver instances[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx-alts-map.dtsi?plain=1#L8) | [`nuvoton,npcx-pinctrl-conf`](../../../../build/dts/api/bindings/pinctrl/nuvoton%2Cnpcx-pinctrl-conf.md#std-dtcompatible-nuvoton-npcx-pinctrl-conf) |
| on-chip | Nuvoton NPCX7 Low-Voltage level detection configuration map between Nuvoton NPCX GPIO and low-voltage controller (LV\_GPIO\_CTL) driver instances[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx-lvol-ctrl-map.dtsi?plain=1#L8) | [`nuvoton,npcx-lvolctrl-conf`](../../../../build/dts/api/bindings/pinctrl/nuvoton%2Cnpcx-lvolctrl-conf.md#std-dtcompatible-nuvoton-npcx-lvolctrl-conf) |
| on-chip | Nuvoton NPCX System Configuration (Pinmux, 1.8V support and so on)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L78) | [`nuvoton,npcx-scfg`](../../../../build/dts/api/bindings/pinctrl/nuvoton%2Cnpcx-scfg.md#std-dtcompatible-nuvoton-npcx-scfg) |
| on-chip | Nuvoton, NPCX Default Pins Configurations[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L33) | [`nuvoton,npcx-pinctrl-def`](../../../../build/dts/api/bindings/pinctrl/nuvoton%2Cnpcx-pinctrl-def.md#std-dtcompatible-nuvoton-npcx-pinctrl-def) |
| on-chip | The Nuvoton pin controller is a singleton node responsible for controlling pin function selection and pin properties[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L53) | [`nuvoton,npcx-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nuvoton%2Cnpcx-pinctrl.md#std-dtcompatible-nuvoton-npcx-pinctrl) |
| on-chip | Nuvoton, NPCX power leakage IOs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L61) | [`nuvoton,npcx-leakage-io`](../../../../build/dts/api/bindings/pinctrl/nuvoton%2Cnpcx-leakage-io.md#std-dtcompatible-nuvoton-npcx-leakage-io) |
| Power management | on-chip | Nuvoton, NPCX Power Switch Logic (PSL) control node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L574) | [`nuvoton,npcx-power-psl`](../../../../build/dts/api/bindings/power/nuvoton%2Cnpcx-power-psl.md#std-dtcompatible-nuvoton-npcx-power-psl) |
| PS/2 | on-chip | Nuvoton, NPCX-PS/2 controller node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L402) | [`nuvoton,npcx-ps2-ctrl`](../../../../build/dts/api/bindings/ps2/nuvoton%2Cnpcx-ps2-ctrl.md#std-dtcompatible-nuvoton-npcx-ps2-ctrl) |
| on-chip | Nuvoton, NPCX-PS/2 channel pads node[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L409) | [`nuvoton,npcx-ps2-channel`](../../../../build/dts/api/bindings/ps2/nuvoton%2Cnpcx-ps2-channel.md#std-dtcompatible-nuvoton-npcx-ps2-channel) |
| PWM | on-chip | Nuvoton, NPCX Pulse Width Modulator (PWM) node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L306)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L252) | [`nuvoton,npcx-pwm`](../../../../build/dts/api/bindings/pwm/nuvoton%2Cnpcx-pwm.md#std-dtcompatible-nuvoton-npcx-pwm) |
| Reset controller | on-chip | NPCX Reset Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx7.dtsi?plain=1#L367) | [`nuvoton,npcx-rst`](../../../../build/dts/api/bindings/reset/nuvoton%2Cnpcx-rst.md#std-dtcompatible-nuvoton-npcx-rst) |
| Serial controller | on-chip | Nuvoton, NPCX-UART node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx7.dtsi?plain=1#L103)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx7.dtsi?plain=1#L112) | [`nuvoton,npcx-uart`](../../../../build/dts/api/bindings/serial/nuvoton%2Cnpcx-uart.md#std-dtcompatible-nuvoton-npcx-uart) |
| SHI | on-chip | Nuvoton NPCX Serial Host Interface (SHI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx7.dtsi?plain=1#L351) | [`nuvoton,npcx-shi`](../../../../build/dts/api/bindings/shi/nuvoton%2Cnpcx-shi.md#std-dtcompatible-nuvoton-npcx-shi) |
| SPI | on-chip | Nuvoton, NPCX SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L462) | [`nuvoton,npcx-spip`](../../../../build/dts/api/bindings/spi/nuvoton%2Cnpcx-spip.md#std-dtcompatible-nuvoton-npcx-spip) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx7m6fb.dtsi?plain=1#L19) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| System controller | on-chip | System Controller Registers R/W[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L91) | [`syscon`](../../../../build/dts/api/bindings/syscon/syscon.md#std-dtcompatible-syscon) |
| Tachometer | on-chip | Nuvoton NPCX Tachometer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L388)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L395) | [`nuvoton,npcx-tach`](../../../../build/dts/api/bindings/tach/nuvoton%2Cnpcx-tach.md#std-dtcompatible-nuvoton-npcx-tach) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | Nuvoton NPCX Internal Timer (ITIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx7.dtsi?plain=1#L92) | [`nuvoton,npcx-itim-timer`](../../../../build/dts/api/bindings/timer/nuvoton%2Cnpcx-itim-timer.md#std-dtcompatible-nuvoton-npcx-itim-timer) |
| Watchdog | on-chip | Nuvoton, NPCX-TWD[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/npcx/npcx.dtsi?plain=1#L334) | [`nuvoton,npcx-watchdog`](../../../../build/dts/api/bindings/watchdog/nuvoton%2Cnpcx-watchdog.md#std-dtcompatible-nuvoton-npcx-watchdog) |

### Connections and IOs

Nuvoton to provide the schematic for this board.

### System Clock

The NPCX7M6FB MCU is configured to use the 90Mhz internal oscillator with the
on-chip PLL to generate a resulting EC clock rate of 15 MHz. See Processor clock
control register (chapter 4 in user manual)

### Serial Port

UART1 is configured for serial logs.

## Programming and Debugging

The `npcx7m6fb_evb` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

This board comes with a Cortex ETM port which facilitates tracing and debugging
using a single physical connection. In addition, it comes with sockets for
JTAG only sessions.

### Flashing

If the correct IDC headers are installed, this board supports both J-TAG and
also the ChromiumOS servo.

To flash using Servo V2, μServo, or Servo V4 (CCD), see the
[Chromium EC Flashing Documentation](https://chromium.googlesource.com/chromiumos/platform/ec#Flashing-via-the-servo-debug-board) [[1]](#id2) for more information.

To flash with J-TAG, install the drivers for your programmer, for example:
SEGGER J-link’s drivers are at [https://www.segger.com/downloads/jlink/](https://www.segger.com/downloads/jlink/)

```shell
# From the root of the zephyr repository
west build -b npcx7m6fb_evb samples/hello_world
west flash
```

### Debugging

Use JTAG/SWD with a J-Link

## References

[[1](#id3)]

[https://chromium.googlesource.com/chromiumos/platform/ec#Flashing-via-the-servo-debug-board](https://chromium.googlesource.com/chromiumos/platform/ec#Flashing-via-the-servo-debug-board)

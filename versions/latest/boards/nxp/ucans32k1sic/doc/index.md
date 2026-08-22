---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/ucans32k1sic/doc/index.html
original_path: boards/nxp/ucans32k1sic/doc/index.html
---

# UCANS32K1SIC

Board Overview

[![../../../../_images/ucans32k1sic_top.webp](../../../../_images/ucans32k1sic_top.webp)
](../../../../_images/ucans32k1sic_top.webp)

UCANS32K1SIC

Name:
:   `ucans32k1sic`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   s32k146

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/ucans32k1sic/doc/index.rst/../..)

## Overview

[NXP UCANS32K1SIC](https://www.nxp.com/design/development-boards/analog-toolbox/can-sic-evaluation-board:UCANS32K1SIC) [[8]](#id18) is a CAN signal improvement capability (SIC) evaluation
board designed for both automotive and industrial applications. The UCANS32K1SIC
provides two CAN SIC interfaces and is based on the 32-bit Arm Cortex-M4F
[NXP S32K146](https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32k-auto-general-purpose-mcus/s32k1-microcontrollers-for-automotive-general-purpose:S32K1) [[9]](#id21) microcontroller.

## Hardware

- NXP S32K146
  :   - Arm Cortex-M4F @ up to 112 Mhz
      - 1 MB Flash
      - 128 KB SRAM
      - up to 127 I/Os
      - 3x FlexCAN with 2x FD
      - eDMA, 12-bit ADC, MPU, ECC and more.
- Interfaces:
  :   - DCD-LZ debug interface with SWD + Console / UART
      - Dual CAN FD PHYs with dual connectors for daisy chain operation
      - JST-GH DroneCode compliant standard connectors and I/O headers
      - user RGB LED and button.

More information about the hardware and design resources can be found at
[NXP UCANS32K1SIC](https://www.nxp.com/design/development-boards/analog-toolbox/can-sic-evaluation-board:UCANS32K1SIC) [[8]](#id18) website.

### Supported Features

The `ucans32k1sic` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `ucans32k1sic/s32k146` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L20) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | NXP ADC12[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L336) | [`nxp,adc12`](../../../../build/dts/api/bindings/adc/nxp%2Cadc12.md#std-dtcompatible-nxp-adc12) |
| CAN | on-chip | NXP FlexCAN CANFD controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L51)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L66) | [`nxp,flexcan-fd`](../../../../build/dts/api/bindings/can/nxp%2Cflexcan-fd.md#std-dtcompatible-nxp-flexcan-fd) |
| Clock control | on-chip | NXP S32 clock generator IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L146) | [`nxp,s32-clock`](../../../../build/dts/api/bindings/clock/nxp%2Cs32-clock.md#std-dtcompatible-nxp-s32-clock) |
| GPIO & Headers | on-chip | Kinetis GPIO[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L197) | [`nxp,kinetis-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Ckinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio) |
| I2C | on-chip | NXP LPI2C controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L153) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp%2Clpi2c.md#std-dtcompatible-nxp-lpi2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/ucans32k1sic/ucans32k1sic.dts?plain=1#L76) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/ucans32k1sic/ucans32k1sic.dts?plain=1#L42) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/ucans32k1sic/ucans32k1sic.dts?plain=1#L59) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MMU / MPU | on-chip | NXP System Memory Protection Unit (SYSMPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L35) | [`nxp,sysmpu`](../../../../build/dts/api/bindings/mmu_mpu/nxp%2Csysmpu.md#std-dtcompatible-nxp-sysmpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k146.dtsi?plain=1#L45) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| PHY | on-board | Simple GPIO controlled CAN transceiver[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/ucans32k1sic/ucans32k1sic.dts?plain=1#L86) | [`can-transceiver-gpio`](../../../../build/dts/api/bindings/phy/can-transceiver-gpio.md#std-dtcompatible-can-transceiver-gpio) |
| Pin control | on-chip | NXP PORT Pin Controller[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L107) | [`nxp,port-pinmux`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cport-pinmux.md#std-dtcompatible-nxp-port-pinmux) |
| on-chip | NXP PORT Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L27) | [`nxp,port-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cport-pinctrl.md#std-dtcompatible-nxp-port-pinctrl) |
| PWM | on-chip | NXP FlexTimer Module (FTM) PWM controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L247) | [`nxp,ftm-pwm`](../../../../build/dts/api/bindings/pwm/nxp%2Cftm-pwm.md#std-dtcompatible-nxp-ftm-pwm) |
| RTC | on-chip | NXP Real Time Clock (RTC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L327) | [`nxp,rtc`](../../../../build/dts/api/bindings/rtc/nxp%2Crtc.md#std-dtcompatible-nxp-rtc) |
| Serial controller | on-chip | NXP LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L182)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L174) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp%2Clpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP LPSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L73)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L85) | [`nxp,lpspi`](../../../../build/dts/api/bindings/spi/nxp%2Clpspi.md#std-dtcompatible-nxp-lpspi) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k146.dtsi?plain=1#L24) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | NXP FlexTimer Module (FTM)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L277) | [`nxp,ftm`](../../../../build/dts/api/bindings/timer/nxp%2Cftm.md#std-dtcompatible-nxp-ftm) |
| Watchdog | on-chip | NXP watchdog (WDOG32)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32k1xx.dtsi?plain=1#L137) | [`nxp,wdog32`](../../../../build/dts/api/bindings/watchdog/nxp%2Cwdog32.md#std-dtcompatible-nxp-wdog32) |

### Connections and IOs

This board has 5 GPIO ports named from `gpioa` to `gpioe`.

Pin control can be further configured from your application overlay by adding
children nodes with the desired pinmux configuration to the singleton node
`pinctrl`. Supported properties are described in
[dts/bindings/pinctrl/nxp,port-pinctrl.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/bindings/pinctrl/nxp,port-pinctrl.yaml).

#### LEDs

The UCANS32K1SIC board has one user RGB LED that can be used either as a GPIO
LED or as a PWM LED.

RGB LED as GPIO LED

| Devicetree node | Devicetree alias | Label | Pin |
| --- | --- | --- | --- |
| led1\_red | led0 | LED1\_RGB\_RED | PTD15 |
| led1\_green | led1 | LED1\_RGB\_GREEN | PTD16 |
| led1\_blue | led2 | LED1\_RGB\_BLUE | PTD0 |

RGB LED as PWM LED

| Devicetree node | Devicetree alias | Label | Pin |
| --- | --- | --- | --- |
| led1\_red\_pwm | pwm-led0 / red-pwm-led | LED1\_RGB\_RED\_PWM | PTD15 / FTM0\_CH0 |
| led1\_green\_pwm | pwm-led1 / green-pwm-led | LED1\_RGB\_GREEN\_PWM | PTD16 / FTM0\_CH1 |
| led1\_blue\_pwm | pwm-led2 / blue-pwm-led | LED1\_RGB\_BLUE\_PWM | PTD0 / FTM0\_CH2 |

The user can control the LEDs in any way. An output of `0` illuminates the LED.

#### Buttons

The UCANS32K1SIC board has one user button:

| Devicetree node | Label | Pin |
| --- | --- | --- |
| sw0 / button\_3 | SW3 | PTD15 |

### Serial Console

The serial console is provided via `lpuart1` on the 7-pin DCD-LZ debug
connector `P6`.

| Connector | Pin | Pin Function |
| --- | --- | --- |
| P6.2 | PTC7 | LPUART1\_TX |
| P6.3 | PTC6 | LPUART1\_RX |

### System Clock

The Arm Cortex-M4F core is configured to run at 80 MHz (RUN mode).

## Programming and Debugging

The `ucans32k1sic` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |
| **[trace32](../../../../develop/flash_debug/host-tools.md#runner-trace32)** | ✅ | ✅ |  |  |  |

Applications for the `ucans32k1sic` board can be built in the usual way as
documented in [Building an Application](../../../../develop/application/index.md#build-an-application).

This board configuration supports [Lauterbach TRACE32](https://www.lauterbach.com) [[10]](#id23) and [SEGGER J-Link](https://wiki.segger.com/S32Kxxx) [[11]](#id25)
West runners for flashing and debugging applications. Follow the steps described
in [Lauterbach TRACE32 Debug Host Tools](../../../../develop/flash_debug/host-tools.md#lauterbach-trace32-debug-host-tools) and [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools),
to setup the flash and debug host tools for these runners, respectively. The
default runner is J-Link.

### Flashing

Run the `west flash` command to flash the application using SEGGER J-Link.
Alternatively, run `west flash -r trace32` to use Lauterbach TRACE32.

The Lauterbach TRACE32 runner supports additional options that can be passed
through command line:

```shell
west flash -r trace32 --startup-args elfFile=<elf_path> loadTo=<flash/sram>
   eraseFlash=<yes/no> verifyFlash=<yes/no>
```

Where:

- `<elf_path>` is the path to the Zephyr application ELF in the output
  directory
- `loadTo=flash` loads the application to the SoC internal program flash
  ([`CONFIG_XIP`](../../../../kconfig.md#CONFIG_XIP "CONFIG_XIP") must be set), and `loadTo=sram` load the
  application to SRAM. The default is `flash`.
- `eraseFlash=yes` erases the whole content of SoC internal flash before the
  application is downloaded to either Flash or SRAM. This routine takes time to
  execute. The default is `no`.
- `verifyFlash=yes` verify the SoC internal flash content after programming
  (use together with `loadTo=flash`). The default is `no`.

For example, to erase and verify flash content:

```shell
west flash -r trace32 --startup-args elfFile=build/zephyr/zephyr.elf loadTo=flash eraseFlash=yes verifyFlash=yes
```

### Debugging

Run the `west debug` command to start a GDB session using SEGGER J-Link.
Alternatively, run `west debug -r trace32` to launch the Lauterbach TRACE32
software debugging interface.

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

[https://www.nxp.com/design/development-boards/analog-toolbox/can-sic-evaluation-board:UCANS32K1SIC](https://www.nxp.com/design/development-boards/analog-toolbox/can-sic-evaluation-board:UCANS32K1SIC)

[[9](#id22)]

[https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32k-auto-general-purpose-mcus/s32k1-microcontrollers-for-automotive-general-purpose:S32K1](https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32k-auto-general-purpose-mcus/s32k1-microcontrollers-for-automotive-general-purpose:S32K1)

[[10](#id24)]

[https://www.lauterbach.com](https://www.lauterbach.com)

[[11](#id26)]

[https://wiki.segger.com/S32Kxxx](https://wiki.segger.com/S32Kxxx)

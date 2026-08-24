---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/lpcxpresso55s36/doc/index.html
original_path: boards/nxp/lpcxpresso55s36/doc/index.html
---

# LPCXpresso55S36

Board Overview

[![../../../../_images/lpcxpresso55S36.jpg](https://docs.zephyrproject.org/4.2.0/_images/lpcxpresso55S36.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/lpcxpresso55S36.jpg)

LPCXpresso55S36

Name:
:   `lpcxpresso55s36`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   lpc55s36

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/lpcxpresso55s36/doc/index.rst/../..)

## Overview

The LPCXpresso55S36 board provides the ideal platform for evaluation
of the LPC55S3x/LPC553x MCU family, based on the Arm® Cortex®-M33
architecture. Arduino® UNO compatible shield connectors are included,
with additional expansion ports around the Arduino footprint, along
with a PMod/host interface port and MikroElektronika Click module
site.

## Hardware

- LPC55S36 Arm® Cortex®-M33 microcontroller running at up to 150 MHz
- 256 KB flash and 112 KB SRAM on-chip
- LPC-Link2 debug high speed USB probe with VCOM port
- I2C and SPI USB bridging to the LPC device via LPC-Link2 probe
- MikroElektronika Click expansion option
- LPCXpresso expansion connectors compatible with Arduino UNO
- PMod compatible expansion / host connector
- Reset, ISP, wake, and user buttons for easy testing of software functionality
- Tri-color LED
- Full-speed USB device / host port
- High-speed USB device / host port
- UART header for external serial to USB cable
- CAN Transceiver
- Stereo audio codec with in/out line

For more information about the LPC55S36 SoC and LPCXPresso55S36 board, see:

- [LPC55S36 SoC Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33/lpc553x-s3x-advanced-analog-armcortex-m33-based-mcu-family:LPC553x)
- [LPC55S36 Datasheet](https://www.nxp.com/docs/en/data-sheet/LPC553x.pdf)
- [LPC55S36 User Manual](https://www.nxp.com/docs/en/reference-manual/LPC553xRM.pdf)
- [LPCXpresso55S36 Website](https://www.nxp.com/design/development-boards/lpcxpresso-boards/development-board-for-the-lpc553x-family-of-mcus:LPCXpresso55S36)
- [LPCXpresso55S36 User Manual](https://www.nxp.com/docs/en/user-manual/LPCXpresso55S36UM.pdf)
- [LPCXpresso55S36 Development Board Design Files](https://www.nxp.com/webapp/Download?colCode=LPCXPRESSO5536_EVK-DESIGN-FILES)

### Supported Features

NXP considers the LPCXpresso55S36 as a superset board for the LPC55(S)3x
family of MCUs. This board is a focus for NXP’s Full Platform Support for
Zephyr, to better enable the entire LPC55(S)3x family. NXP prioritizes enabling
this board with new support for Zephyr features. Another similar superset
board is the [LPCXPRESSO55S69](../../lpcxpresso55s69/doc/index.md#lpcxpresso55s69), and that board may have additional features
already supported, which can also be re-used on this lpcxpresso55s36 board.

The `lpcxpresso55s36` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `lpcxpresso55s36/lpc55s36` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S3x_common.dtsi?plain=1#L21) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | LPC LPADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S3x_common.dtsi?plain=1#L287) | [`nxp,lpc-lpadc`](../../../../build/dts/api/bindings/adc/nxp,lpc-lpadc.md#std-dtcompatible-nxp-lpc-lpadc) |
| ARM architecture | on-chip | LPC Flexcomm node[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S3x_common.dtsi?plain=1#L197) | [`nxp,lpc-flexcomm`](../../../../build/dts/api/bindings/arm/nxp,lpc-flexcomm.md#std-dtcompatible-nxp-lpc-flexcomm) |
| CAN | on-chip | NXP LPC SoC series MCAN CAN FD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S3x_common.dtsi?plain=1#L333) | [`nxp,lpc-mcan`](../../../../build/dts/api/bindings/can/nxp,lpc-mcan.md#std-dtcompatible-nxp-lpc-mcan) |
| Clock control | on-chip | LPC SYSCON & CLKCTL IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S3x_common.dtsi?plain=1#L74) | [`nxp,lpc-syscon`](../../../../build/dts/api/bindings/clock/nxp,lpc-syscon.md#std-dtcompatible-nxp-lpc-syscon) |
| DAC | on-chip | NXP MCUX LPDAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S3x_common.dtsi?plain=1#L306)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S3x_common.dtsi?plain=1#L315) | [`nxp,lpdac`](../../../../build/dts/api/bindings/dac/nxp,lpdac.md#std-dtcompatible-nxp-lpdac) |
| DMA | on-chip | NXP LPC DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S3x_common.dtsi?plain=1#L150)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S3x_common.dtsi?plain=1#L162) | [`nxp,lpc-dma`](../../../../build/dts/api/bindings/dma/nxp,lpc-dma.md#std-dtcompatible-nxp-lpc-dma) |
| Flash controller | on-chip | NXP (In-Application Programming) flash memory controller for the lpc553x family[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S3x_common.dtsi?plain=1#L84) | [`nxp,iap-fmc553`](../../../../build/dts/api/bindings/flash_controller/nxp,iap-fmc553.md#std-dtcompatible-nxp-iap-fmc553) |
| GPIO & Headers | on-chip | LPC GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S3x_common.dtsi?plain=1#L121) | [`nxp,lpc-gpio`](../../../../build/dts/api/bindings/gpio/nxp,lpc-gpio.md#std-dtcompatible-nxp-lpc-gpio) |
| on-chip | LPC GPIO port device[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S3x_common.dtsi?plain=1#L126) | [`nxp,lpc-gpio-port`](../../../../build/dts/api/bindings/gpio/nxp,lpc-gpio-port.md#std-dtcompatible-nxp-lpc-gpio-port) |
| on-board | GPIO pins exposed on Mikro BUS headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso55s36/lpcxpresso55s36.dts?plain=1#L69) | [`mikro-bus`](../../../../build/dts/api/bindings/gpio/mikro-bus.md#std-dtcompatible-mikro-bus) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso55s36/lpcxpresso55s36.dts?plain=1#L92) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso55s36/lpcxpresso55s36.dts?plain=1#L55) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | NXP Pin interrupt and pattern match engine (PINT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S3x_common.dtsi?plain=1#L174) | [`nxp,pint`](../../../../build/dts/api/bindings/interrupt-controller/nxp,pint.md#std-dtcompatible-nxp-pint) |
| on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso55s36/lpcxpresso55s36.dts?plain=1#L39) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S3x_common.dtsi?plain=1#L27) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | Flash node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S3x_common.dtsi?plain=1#L91)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S3x_common.dtsi?plain=1#L98) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso55s36/lpcxpresso55s36.dts?plain=1#L151) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | LPC I/O Pin Configuration (IOCON)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S3x_common.dtsi?plain=1#L110) | [`nxp,lpc-iocon`](../../../../build/dts/api/bindings/pinctrl/nxp,lpc-iocon.md#std-dtcompatible-nxp-lpc-iocon) |
| on-chip | LPC pinctrl node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S3x_common.dtsi?plain=1#L116) | [`nxp,lpc-iocon-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,lpc-iocon-pinctrl.md#std-dtcompatible-nxp-lpc-iocon-pinctrl) |
| PWM | on-chip | NXP eFLEX PWM module with mcux-pwm submodules[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S3x_common.dtsi?plain=1#L344) | [`nxp,flexpwm`](../../../../build/dts/api/bindings/pwm/nxp,flexpwm.md#std-dtcompatible-nxp-flexpwm) |
| on-chip | NXP MCUX PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S3x_common.dtsi?plain=1#L404)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S3x_common.dtsi?plain=1#L349) | [`nxp,imx-pwm`](../../../../build/dts/api/bindings/pwm/nxp,imx-pwm.md#std-dtcompatible-nxp-imx-pwm) |
| on-chip | NXP SCTimer PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S3x_common.dtsi?plain=1#L462) | [`nxp,sctimer-pwm`](../../../../build/dts/api/bindings/pwm/nxp,sctimer-pwm.md#std-dtcompatible-nxp-sctimer-pwm) |
| Regulator | on-chip | NXP VREF SOC peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S3x_common.dtsi?plain=1#L472) | [`nxp,vref`](../../../../build/dts/api/bindings/regulator/nxp,vref.md#std-dtcompatible-nxp-vref) |
| Reset controller | on-chip | LPC SYSCON Peripheral reset controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S3x_common.dtsi?plain=1#L78) | [`nxp,lpc-syscon-reset`](../../../../build/dts/api/bindings/reset/nxp,lpc-syscon-reset.md#std-dtcompatible-nxp-lpc-syscon-reset) |
| Serial controller | on-chip | LPC USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S3x_common.dtsi?plain=1#L186) | [`nxp,lpc-usart`](../../../../build/dts/api/bindings/serial/nxp,lpc-usart.md#std-dtcompatible-nxp-lpc-usart) |
| SPI | on-chip | NXP LPC SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S3x_common.dtsi?plain=1#L274) | [`nxp,lpc-spi`](../../../../build/dts/api/bindings/spi/nxp,lpc-spi.md#std-dtcompatible-nxp-lpc-spi) |
| SRAM | on-chip | Generic on-chip SRAM[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S3x_common.dtsi?plain=1#L48) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| USB | on-chip | NXP LPCIP3511 USB device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc55S3x_common.dtsi?plain=1#L453) | [`nxp,lpcip3511`](../../../../build/dts/api/bindings/usb/nxp,lpcip3511.md#std-dtcompatible-nxp-lpcip3511) |

### Connections and IOs

The LPC55S36 SoC has IOCON registers, which can be used to configure
the functionality of a pin.

| Name | Function | Usage |
| --- | --- | --- |
| PIO0\_17 | GPIO | USR SW3 |
| PIO0\_22 | GPIO | GREEN LED |
| PIO0\_28 | GPIO | RED LED |
| PIO0\_29 | USART | USART RX |
| PIO0\_30 | USART | USART TX |
| PIO1\_11 | GPIO | BLUE\_LED |
| PIO1\_18 | GPIO | Wakeup SW1 |
| PIO1\_20 | FLEXPPWM0\_PWM0\_A | pwm |
| PIO1\_17 | FLEXPPWM0\_PWM0\_B | pwm |
| PIO1\_6 | FLEXPPWM0\_PWM1\_A | pwm |
| PIO1\_22 | FLEXPPWM0\_PWM1\_B | pwm |
| PIO1\_8 | FLEXPPWM0\_PWM2\_A | pwm |
| PIO1\_4 | FLEXPPWM0\_PWM2\_B | pwm |
| PIO1\_21 | FLEXPPWM1\_PWM0\_A | pwm |
| PIO0\_3 | FLEXPPWM1\_PWM0\_B | pwm |
| PIO1\_23 | FLEXPPWM1\_PWM1\_A | pwm |
| PIO0\_21 | FLEXPPWM1\_PWM1\_B | pwm |
| PIO1\_25 | FLEXPPWM1\_PWM2\_A | pwm |
| PIO0\_31 | FLEXPPWM1\_PWM2\_B | pwm |
| PIO1\_2 | CAN0\_TXD | CAN TX |
| PIO1\_3 | CAN0\_RXD | CAN RX |
| PIO0\_22 | USB0\_VBUS | USBFS VBUS |

### System Clock

The LPC55S36 SoC is configured to use PLL1 clocked from the external 24MHz
crystal, running at 144MHz as a source for the system clock. When the flash
controller is enabled, the core clock will be reduced to 96MHz. Other sources for the system clock are
provided in the SOC, depending on your system requirements.

### Serial Port

The LPC55S36 SoC has 8 FLEXCOMM interfaces for serial
communication. One is configured as USART for the console and the
remaining are not used.

## Programming and Debugging

The `lpcxpresso55s36` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[linkserver](../../../../develop/flash_debug/host-tools.md#runner-linkserver)** | ✅ (default) | ✅ (default) | ✅ |  | ✅ |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

LinkServer is the default runner for this board.
A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the integrated [MCU-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#mcu-link-onboard-debug-probe)
in the CMSIS-DAP mode. To use this probe with Zephyr, you need to install the
[LinkServer Debug Host Tools](../../../../develop/flash_debug/host-tools.md#linkserver-debug-host-tools) and make sure they are in your search path.
Refer to the detailed overview about [Application Debugging](../../../../develop/debug/index.md#application-debugging) for additional
information.

The integrated MCU-Link hardware can also be used as a J-Link probe with a
firmware update, as described in [MCU-Link JLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#mcu-link-jlink-onboard-debug-probe).
The [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) should be available in this case.

### Configuring a Console

Connect a USB cable from your PC to J1 (LINK2), and use the serial
terminal of your choice (minicom, putty, etc.) with the following
settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b lpcxpresso55s36 samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v2.2.0 *****
Hello World! lpcxpresso55s36
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b lpcxpresso55s36 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS zephyr-v2.2.0 *****
Hello World! lpcxpresso55s36
```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

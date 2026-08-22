---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/frdm_ke17z512/doc/index.html
original_path: boards/nxp/frdm_ke17z512/doc/index.html
---

# FRDM-KE17Z512

Board Overview

[![../../../../_images/frdm_ke17z512.webp](../../../../_images/frdm_ke17z512.webp)
](../../../../_images/frdm_ke17z512.webp)

FRDM-KE17Z512

Name:
:   `frdm_ke17z512`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mke17z9

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/frdm_ke17z512/doc/index.rst/../..)

## Overview

The FRDM-KE17Z512 is a development board for NXP Kinetis KE1xZ 32-bit
MCU-based platforms. The onboard OpenSDAv2 serial and debug adapter,
running an open source bootloader, offers options for serial
communication, flash programming, and run-control debugging.

## Hardware

- MKE17Z512VLL9 MCU (up to 96 MHz, 512 KB flash memory, 96 KB RAM,
  and 100 Low profile Quad Flat Package (LQFP))
- 3.3 V or 5 V MCU operation
- 6-axis FXOS8700CQ digital accelerometer and magnetometer
- RGB LED
- Two user push-buttons
- Thermistor
- Arduino compatible I/O pin header
- OpenSDA on-board debugger
- Two Touch Electrodes

For more information about the KE1xZ SoC and the FRDM-KE17Z512 board, see
these NXP reference documents:

- [KE1xZ Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/ke-series-arm-cortex-m4-m0-plus/ke1xz-arm-cortex-m0-plus-5v-main-stream-mcu-with-nxp-touch-and-can-control:KE1xZ)
- [KE1xZ Fact Sheet](https://www.nxp.com/docs/en/fact-sheet/KE1xZMCUFAMFS.pdf)
- [KE1xZ Reference Manual](https://www.nxp.com/webapp/Download?colCode=KE1XZP100M72SF0RM)
- [FRDM-KE17Z512 Website](https://www.nxp.com/design/design-center/development-boards-and-designs/general-purpose-mcus/frdm-development-board-for-96-mhz-ke17z-ke13z-ke12z-with-512-kb-flash-mcus:FRDM-KE17Z512)
- [FRDM-KE17Z512 Quick Start Guide](https://www.nxp.com/docs/en/quick-reference-guide/FRDMKE17Z512QSG.pdf)
- [FRDM-KE17Z512 Reference Manual](https://www.nxp.com/docs/en/reference-manual/KE1XZP100M96SF0RM.pdf)

### Supported Features

The `frdm_ke17z512` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `frdm_ke17z512/mke17z9` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xz.dtsi?plain=1#L24) | [`arm,cortex-m0+`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m0%2B.md#std-dtcompatible-arm-cortex-m0) |
| ADC | on-chip | NXP ADC12[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xz.dtsi?plain=1#L144) | [`nxp,adc12`](../../../../build/dts/api/bindings/adc/nxp%2Cadc12.md#std-dtcompatible-nxp-adc12) |
| Clock control | on-chip | NXP Kinetis SCG (System Clock Generator) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xz.dtsi?plain=1#L74) | [`nxp,kinetis-scg`](../../../../build/dts/api/bindings/clock/nxp%2Ckinetis-scg.md#std-dtcompatible-nxp-kinetis-scg) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xz.dtsi?plain=1#L80) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Generic fixed factor clock provider[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xz.dtsi?plain=1#L92) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| on-chip | NXP Kinetis PCC (Peripheral Clock Controller) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xz.dtsi?plain=1#L121) | [`nxp,kinetis-pcc`](../../../../build/dts/api/bindings/clock/nxp%2Ckinetis-pcc.md#std-dtcompatible-nxp-kinetis-pcc) |
| Comparator | on-chip | NXP Kinetis ACMP (Analog CoMParator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xz.dtsi?plain=1#L416) | [`nxp,kinetis-acmp`](../../../../build/dts/api/bindings/comparator/nxp%2Ckinetis-acmp.md#std-dtcompatible-nxp-kinetis-acmp) |
| Counter | on-chip | NXP LPTMR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xz.dtsi?plain=1#L179) | [`nxp,lptmr`](../../../../build/dts/api/bindings/counter/nxp%2Clptmr.md#std-dtcompatible-nxp-lptmr) |
| DMA | on-chip | NXP MCUX EDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xz.dtsi?plain=1#L448) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp%2Cmcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| Flash controller | on-chip | NXP Kinetis Flash Memory Module E (FTFE)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xz.dtsi?plain=1#L127) | [`nxp,kinetis-ftfe`](../../../../build/dts/api/bindings/flash_controller/nxp%2Ckinetis-ftfe.md#std-dtcompatible-nxp-kinetis-ftfe) |
| GPIO & Headers | on-chip | A group of GPIOs that share an interrupt[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xz.dtsi?plain=1#L239) | [`nxp,gpio-cluster`](../../../../build/dts/api/bindings/gpio/nxp%2Cgpio-cluster.md#std-dtcompatible-nxp-gpio-cluster) |
| on-chip | Kinetis GPIO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xz.dtsi?plain=1#L256)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xz.dtsi?plain=1#L247) | [`nxp,kinetis-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Ckinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio) |
| I2C | on-chip | NXP LPI2C controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xz.dtsi?plain=1#L385) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp%2Clpi2c.md#std-dtcompatible-nxp-lpi2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_ke17z512/frdm_ke17z512.dts?plain=1#L72) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_ke17z512/frdm_ke17z512.dts?plain=1#L40) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_ke17z512/frdm_ke17z512.dts?plain=1#L56) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Miscellaneous | on-chip | NXP FlexIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xz.dtsi?plain=1#L462) | [`nxp,flexio`](../../../../build/dts/api/bindings/misc/nxp%2Cflexio.md#std-dtcompatible-nxp-flexio) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xz.dtsi?plain=1#L136) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_ke17z512/frdm_ke17z512.dts?plain=1#L157) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | NXP PORT Pin Controller[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xz.dtsi?plain=1#L189) | [`nxp,port-pinmux`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cport-pinmux.md#std-dtcompatible-nxp-port-pinmux) |
| on-chip | NXP PORT Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xz.dtsi?plain=1#L69) | [`nxp,port-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cport-pinctrl.md#std-dtcompatible-nxp-port-pinctrl) |
| PWM | on-chip | NXP FlexTimer Module (FTM) PWM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xz.dtsi?plain=1#L365) | [`nxp,ftm-pwm`](../../../../build/dts/api/bindings/pwm/nxp%2Cftm-pwm.md#std-dtcompatible-nxp-ftm-pwm) |
| on-chip | Kinetis PWT PWM Capture[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xz.dtsi?plain=1#L374) | [`nxp,kinetis-pwt`](../../../../build/dts/api/bindings/pwm/nxp%2Ckinetis-pwt.md#std-dtcompatible-nxp-kinetis-pwt) |
| RTC | on-chip | NXP Real Time Clock (RTC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xz.dtsi?plain=1#L407) | [`nxp,rtc`](../../../../build/dts/api/bindings/rtc/nxp%2Crtc.md#std-dtcompatible-nxp-rtc) |
| Serial controller | on-chip | NXP LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xz.dtsi?plain=1#L171)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xz.dtsi?plain=1#L155) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp%2Clpuart.md#std-dtcompatible-nxp-lpuart) |
| on-chip | Kinetis UART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke17z512.dtsi?plain=1#L47) | [`nxp,kinetis-uart`](../../../../build/dts/api/bindings/serial/nxp%2Ckinetis-uart.md#std-dtcompatible-nxp-kinetis-uart) |
| SPI | on-chip | NXP LPSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xz.dtsi?plain=1#L424)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xz.dtsi?plain=1#L436) | [`nxp,lpspi`](../../../../build/dts/api/bindings/spi/nxp%2Clpspi.md#std-dtcompatible-nxp-lpspi) |
| Timer | on-chip | ARMv6-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21) | [`arm,armv6m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv6m-systick.md#std-dtcompatible-arm-armv6m-systick) |
| on-chip | NXP FlexTimer Module (FTM)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xz.dtsi?plain=1#L347) | [`nxp,ftm`](../../../../build/dts/api/bindings/timer/nxp%2Cftm.md#std-dtcompatible-nxp-ftm) |
| Watchdog | on-chip | NXP watchdog (WDOG32)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xz.dtsi?plain=1#L229) | [`nxp,wdog32`](../../../../build/dts/api/bindings/watchdog/nxp%2Cwdog32.md#std-dtcompatible-nxp-wdog32) |

### System Clock

The KE17Z9 SoC is configured to run at 48 MHz using the FIRC.

### Serial Port

The KE17Z9 SoC has three LPUARTs. UART2 is configured for the console.

## Programming and Debugging

The `frdm_ke17z512` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **debugserver** | **rtt** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[linkserver](../../../../develop/flash_debug/host-tools.md#runner-linkserver)** | ✅ (default) | ✅ (default) | ✅ | ✅ |  |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use Linkserver.

Early versions of this board have an outdated version of the OpenSDA bootloader
and require an update. Please see the [DAPLink Bootloader Update](https://os.mbed.com/blog/entry/DAPLink-bootloader-update/) page for
instructions to update from the CMSIS-DAP bootloader to the DAPLink bootloader.

#### Option 1: Linkserver

Install the [LinkServer Debug Host Tools](../../../../develop/flash_debug/host-tools.md#linkserver-debug-host-tools) and make sure they are in your
search path. LinkServer works with the default CMSIS-DAP firmware included in
the on-board debugger.

Linkserver is the default for this board, `west flash` and `west debug` will
call the linkserver runner.

#### Option 2: [OpenSDA J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-jlink-onboard-debug-probe)

Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search
path.

Follow the instructions in [OpenSDA J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-jlink-onboard-debug-probe) to program
the [Segger J-Link OpenSDA V2.1 Firmware](https://www.segger.com/downloads/jlink/OpenSDA_V2_1.bin).
Use the `-r jlink` option with west to use the jlink runner.

```shell
west flash -r jlink
```

### Configuring a Console

Regardless of your choice in debug probe, we will use the OpenSDA
microcontroller as a usb-to-serial adapter for the serial console.

Connect a USB cable from your PC to J10.

Use the following settings with your serial terminal of choice (minicom, putty,
etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b frdm_ke17z512 samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the SW1 button), and you should
see the following message in the terminal:

```shell
*** Booting Zephyr OS build v3.6.0-xxxx-gxxxxxxxxxxxx ***
Hello World! frdm_ke17z512/mke17z9
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b frdm_ke17z512 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
*** Booting Zephyr OS build v3.6.0-xxxx-gxxxxxxxxxxxx ***
Hello World! frdm_ke17z512/mke17z9
```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

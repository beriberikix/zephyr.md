---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/frdm_mcxa156/doc/index.html
original_path: boards/nxp/frdm_mcxa156/doc/index.html
---

# FRDM-MCXA156

Board Overview

[![../../../../_images/frdm_mcxa156.webp](../../../../_images/frdm_mcxa156.webp)
](../../../../_images/frdm_mcxa156.webp)

FRDM-MCXA156

Name:
:   `frdm_mcxa156`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mcxa156

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/frdm_mcxa156/doc/index.rst/../..)

## Overview

FRDM-MCXA156 are compact and scalable development boards for rapid prototyping of
MCX A144/5/6 A154/5/6 MCUs. They offer industry standard headers for easy access
to the MCU’s I/Os, integrated open-standard serial interfaces, external flash
memory and an on-board MCU-Link debugger. Additional tools like our Expansion
Board Hub for add-on boards and the Application Code Hub for software examples
are available through the MCUXpresso Developer Experience.

## Hardware

- MCX-A156 Arm Cortex-M33 microcontroller running at 96 MHz
- 1MB dual-bank on chip Flash
- 128 KB RAM
- USB full-speed with on-chip FS PHY. USB Type-C connectors
- 1x FlexCAN with FD, 1x I3Cs
- On-board MCU-Link debugger with CMSIS-DAP
- Arduino Header, FlexIO/LCD Header, SmartDMA/Camera Header, mikroBUS

For more information about the MCX-A156 SoC and FRDM-MCXA156 board, see:

- [MCX-A156 SoC Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/mcx-arm-cortex-m/mcx-a-series-microcontrollers/mcx-a13x-14x-15x-mcus-with-arm-cortex-m33-scalable-device-options-low-power-and-intelligent-peripherals:MCX-A13X-A14X-A15X)
- [MCX-A156 Datasheet](https://www.nxp.com/docs/en/data-sheet/MCXAP100M96FS6.pdf)
- [MCX-A156 Reference Manual](https://www.nxp.com/webapp/Download?colCode=MCXAP100M96FS6RM)
- [FRDM-MCXA156 Website](https://www.nxp.com/design/design-center/development-boards-and-designs/general-purpose-mcus/frdm-development-board-for-mcx-a144-5-6-a154-5-6-mcus:FRDM-MCXA156)
- [FRDM-MCXA156 User Guide](https://www.nxp.com/document/guide/getting-started-with-frdm-mcxa156:GS-FRDM-MCXA156)
- [FRDM-MCXA156 Board User Manual](https://www.nxp.com/docs/en/user-manual/UM12121.pdf)
- [FRDM-MCXA156 Schematics](https://www.nxp.com/webapp/Download?colCode=SPF-90841)

### Supported Features

The `frdm_mcxa156` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `frdm_mcxa156/mcxa156` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L18) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | LPC LPADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L369)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L385) | [`nxp,lpc-lpadc`](../../../../build/dts/api/bindings/adc/nxp%2Clpc-lpadc.md#std-dtcompatible-nxp-lpc-lpadc) |
| CAN | on-chip | NXP FlexCAN controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L256) | [`nxp,flexcan`](../../../../build/dts/api/bindings/can/nxp%2Cflexcan.md#std-dtcompatible-nxp-flexcan) |
| Clock control | on-chip | LPC SYSCON & CLKCTL IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L33) | [`nxp,lpc-syscon`](../../../../build/dts/api/bindings/clock/nxp%2Clpc-syscon.md#std-dtcompatible-nxp-lpc-syscon) |
| Counter | on-chip | NXP MCUX Standard Timer/Counter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L173)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L185) | [`nxp,lpc-ctimer`](../../../../build/dts/api/bindings/counter/nxp%2Clpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer) |
| on-chip | NXP LPTMR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L485) | [`nxp,lptmr`](../../../../build/dts/api/bindings/counter/nxp%2Clptmr.md#std-dtcompatible-nxp-lptmr) |
| DAC | on-chip | NXP MCUX LPDAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L233) | [`nxp,lpdac`](../../../../build/dts/api/bindings/dac/nxp%2Clpdac.md#std-dtcompatible-nxp-lpdac) |
| DMA | on-chip | NXP MCUX EDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L242) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp%2Cmcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| Flash controller | on-chip | NXP MSF1 Flash Memory Module (FMU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L152) | [`nxp,msf1`](../../../../build/dts/api/bindings/flash_controller/nxp%2Cmsf1.md#std-dtcompatible-nxp-msf1) |
| GPIO & Headers | on-chip | Kinetis GPIO[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L83) | [`nxp,kinetis-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Ckinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio) |
| on-board | GPIO pins exposed on NXP LCD 8080 interface (e.g., used on LCD-PAR-035 panel)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxa156/frdm_mcxa156.dts?plain=1#L74) | [`nxp,lcd-8080`](../../../../build/dts/api/bindings/gpio/nxp%2Clcd-8080.md#std-dtcompatible-nxp-lcd-8080) |
| Hardware information | on-chip | NXP LPC 128-bit Unique identifier[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L167) | [`nxp,lpc-uid`](../../../../build/dts/api/bindings/hwinfo/nxp%2Clpc-uid.md#std-dtcompatible-nxp-lpc-uid) |
| I2C | on-chip | NXP LPI2C controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L417)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L428) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp%2Clpi2c.md#std-dtcompatible-nxp-lpi2c) |
| I3C | on-chip | NXP MCUX I3C controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L356) | [`nxp,mcux-i3c`](../../../../build/dts/api/bindings/i3c/nxp%2Cmcux-i3c.md#std-dtcompatible-nxp-mcux-i3c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxa156/frdm_mcxa156.dts?plain=1#L57) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxa156/frdm_mcxa156.dts?plain=1#L41) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MIPI-DBI | on-chip | NXP FlexIO LCD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L272) | [`nxp,mipi-dbi-flexio-lcdif`](../../../../build/dts/api/bindings/mipi-dbi/nxp%2Cmipi-dbi-flexio-lcdif.md#std-dtcompatible-nxp-mipi-dbi-flexio-lcdif) |
| Miscellaneous | on-chip | NXP FlexIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L266) | [`nxp,flexio`](../../../../build/dts/api/bindings/misc/nxp%2Cflexio.md#std-dtcompatible-nxp-flexio) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L160) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxa156/frdm_mcxa156.dts?plain=1#L230) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | NXP PORT Pin Controller[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L53) | [`nxp,port-pinmux`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cport-pinmux.md#std-dtcompatible-nxp-port-pinmux) |
| on-chip | NXP PORT Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L27) | [`nxp,port-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cport-pinctrl.md#std-dtcompatible-nxp-port-pinctrl) |
| PWM | on-chip | NXP eFLEX PWM module with mcux-pwm submodules[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L278) | [`nxp,flexpwm`](../../../../build/dts/api/bindings/pwm/nxp%2Cflexpwm.md#std-dtcompatible-nxp-flexpwm) |
| on-chip | NXP MCUX PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L283)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L294) | [`nxp,imx-pwm`](../../../../build/dts/api/bindings/pwm/nxp%2Cimx-pwm.md#std-dtcompatible-nxp-imx-pwm) |
| Reset controller | on-chip | LPC SYSCON Peripheral reset controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L37) | [`nxp,lpc-syscon-reset`](../../../../build/dts/api/bindings/reset/nxp%2Clpc-syscon-reset.md#std-dtcompatible-nxp-lpc-syscon-reset) |
| Sensors | on-board | NXP P3T1755 digital temperature sensor connected to I3C bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxa156/frdm_mcxa156.dts?plain=1#L179) | [`nxp,p3t1755`](../../../../build/dts/api/compatibles/nxp%2Cp3t1755.md#std-dtcompatible-nxp-p3t1755) |
| on-chip | NXP low-power analog comparator (LPCMP)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L401)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L409) | [`nxp,lpcmp`](../../../../build/dts/api/bindings/sensor/nxp%2Clpcmp.md#std-dtcompatible-nxp-lpcmp) |
| Serial controller | on-chip | NXP LPUART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L132) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp%2Clpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP LPSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L461)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L473) | [`nxp,lpspi`](../../../../build/dts/api/bindings/spi/nxp%2Clpspi.md#std-dtcompatible-nxp-lpspi) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L43) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| USB | on-chip | NPX Kinetis USBFSOTG Controller in device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L496) | [`nxp,kinetis-usbd`](../../../../build/dts/api/bindings/usb/nxp%2Ckinetis-usbd.md#std-dtcompatible-nxp-kinetis-usbd) |
| Watchdog | on-chip | LPC Windowed Watchdog Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxa156.dtsi?plain=1#L506) | [`nxp,lpc-wwdt`](../../../../build/dts/api/bindings/watchdog/nxp%2Clpc-wwdt.md#std-dtcompatible-nxp-lpc-wwdt) |

### Connections and IOs

The MCX-A156 SoC has 5 gpio controllers and has pinmux registers which
can be used to configure the functionality of a pin.

| Name | Function | Usage |
| --- | --- | --- |
| PIO0\_2 | UART | UART RX |
| PIO0\_3 | UART | UART TX |

### System Clock

The MCX-A156 SoC is configured to use FRO running at 96MHz as a source for
the system clock.

### Serial Port

The FRDM-MCXA156 SoC has 5 LPUART interfaces for serial communication.
LPUART 0 is configured as UART for the console.

## Programming and Debugging

The `frdm_mcxa156` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[linkserver](../../../../develop/flash_debug/host-tools.md#runner-linkserver)** | ✅ (default) | ✅ (default) | ✅ |  | ✅ |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the MCU-Link CMSIS-DAP Onboard Debug Probe.

#### Using LinkServer

Linkserver is the default runner for this board, and supports the factory
default MCU-Link firmware. Follow the instructions in
[MCU-Link CMSIS-DAP Onboard Debug Probe](../../../../develop/flash_debug/probes.md#mcu-link-cmsis-onboard-debug-probe) to reprogram the default MCU-Link
firmware. This only needs to be done if the default onboard debug circuit
firmware was changed. To put the board in `DFU mode` to program the firmware,
short jumper JP5.

#### Using J-Link

There are two options. The onboard debug circuit can be updated with Segger
J-Link firmware by following the instructions in
[MCU-Link JLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#mcu-link-jlink-onboard-debug-probe).
To be able to program the firmware, you need to put the board in `DFU mode`
by shortening the jumper JP5.
The second option is to attach a [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe) to the
10-pin SWD connector (J24) of the board. Additionally, the jumper JP7 must
be shortened.
For both options use the `-r jlink` option with west to use the jlink runner.

```shell
west flash -r jlink
```

### Configuring a Console

Connect a USB cable from your PC to J21, and use the serial terminal of your choice
(minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b frdm_mcxa156 samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```shell
*** Booting Zephyr OS build v3.6.0-4478-ge6c3a42f5f52 ***
Hello World! frdm_mcxa156/mcxa156
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b frdm_mcxa156/mcxa156 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
*** Booting Zephyr OS build v3.6.0-4478-ge6c3a42f5f52 ***
Hello World! frdm_mcxa156/mcxa156
```

### Troubleshooting

#### Using Segger SystemView and RTT

Note that when using SEGGER SystemView or RTT with this SOC, the RTT control
block address must be set manually within SystemView or the RTT Viewer. The
address provided to the tool should be the location of the `_SEGGER_RTT`
symbol, which can be found using a debugger or by examining the `zephyr.map`
file output by the linker.

The RTT control block address must be provided manually because this SOC
supports ECC RAM. If the SEGGER tooling searches the ECC RAM space for the
control block a fault will occur, provided that ECC is enabled and the RAM
segment being searched has not been initialized to a known value.

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/frdm_mcxn236/doc/index.html
original_path: boards/nxp/frdm_mcxn236/doc/index.html
---

# FRDM-MCXN236

Board Overview

[![../../../../_images/frdm_mcxn236.webp](https://docs.zephyrproject.org/4.2.0/_images/frdm_mcxn236.webp)
](https://docs.zephyrproject.org/4.2.0/_images/frdm_mcxn236.webp)

FRDM-MCXN236

Name:
:   `frdm_mcxn236`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mcxn236

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/frdm_mcxn236/doc/index.rst/../..)

## Overview

FRDM-MCXN236 are compact and scalable development boards for rapid prototyping of
MCX N23X MCUs. They offer industry standard headers for easy access to the
MCUs I/Os, integrated open-standard serial interfaces, external flash memory and
an on-board MCU-Link debugger. MCX N Series are high-performance, low-power
microcontrollers with intelligent peripherals and accelerators providing multi-tasking
capabilities and performance efficiency.

## Hardware

- MCX-N236 Arm Cortex-M33 microcontroller running at 150 MHz
- 1MB dual-bank on chip Flash
- 352 KB RAM
- USB high-speed (Host/Device) with on-chip HS PHY. HS USB Type-C connectors
- 8x LP Flexcomms each supporting SPI, I2C, UART
- 2x FlexCAN with FD, 2x I3Cs, 2x SAI
- On-board MCU-Link debugger with CMSIS-DAP
- Arduino Header, FlexIO/LCD Header, SmartDMA/Camera Header, mikroBUS

For more information about the MCX-N236 SoC and FRDM-MCXN236 board, see:

- [MCX-N236 SoC Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/mcx-arm-cortex-m/mcx-n-series-microcontrollers/mcx-n23x-highly-integrated-mcus-with-on-chip-accelerators-intelligent-peripherals-and-advanced-security:MCX-N23X)
- [MCX-N236 Datasheet](https://www.nxp.com/docs/en/data-sheet/MCXN23x.pdf)
- [MCX-N236 Reference Manual](https://www.nxp.com/docs/en/reference-manual/MCXN23xRM.pdf)
- [FRDM-MCXN236 Website](https://www.nxp.com/design/design-center/development-boards-and-designs/general-purpose-mcus/frdm-development-board-for-mcx-n23x-mcus:FRDM-MCXN236)
- [FRDM-MCXN236 User Guide](https://www.nxp.com/document/guide/getting-started-with-frdm-mcxn236:GS-FRDM-MCXN236)
- [FRDM-MCXN236 Board User Manual](https://www.nxp.com/docs/en/user-manual/UM12041.pdf)
- [FRDM-MCXN236 Schematics](https://www.nxp.com/webapp/Download?colCode=SPF-90828)

### Supported Features

The `frdm_mcxn236` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `frdm_mcxn236/mcxn236` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L19) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | LPC LPADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L715)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L732) | [`nxp,lpc-lpadc`](../../../../build/dts/api/bindings/adc/nxp,lpc-lpadc.md#std-dtcompatible-nxp-lpc-lpadc) |
| CAN | on-chip | NXP FlexCAN controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L789)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L779) | [`nxp,flexcan`](../../../../build/dts/api/bindings/can/nxp,flexcan.md#std-dtcompatible-nxp-flexcan) |
| Clock control | on-chip | LPC SYSCON & CLKCTL IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L66) | [`nxp,lpc-syscon`](../../../../build/dts/api/bindings/clock/nxp,lpc-syscon.md#std-dtcompatible-nxp-lpc-syscon) |
| Counter | on-chip | NXP MCUX Standard Timer/Counter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L643)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L655) | [`nxp,lpc-ctimer`](../../../../build/dts/api/bindings/counter/nxp,lpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer) |
| on-chip | NXP LPTMR[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L837) | [`nxp,lptmr`](../../../../build/dts/api/bindings/counter/nxp,lptmr.md#std-dtcompatible-nxp-lptmr) |
| on-chip | NXP Multirate Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L857) | [`nxp,mrt`](../../../../build/dts/api/bindings/counter/nxp,mrt.md#std-dtcompatible-nxp-mrt) |
| on-chip | NXP Multirate Timer Channel[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L868)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L873) | [`nxp,mrt-channel`](../../../../build/dts/api/bindings/counter/nxp,mrt-channel.md#std-dtcompatible-nxp-mrt-channel) |
| DMA | on-chip | NXP MCUX EDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L478)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L494) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp,mcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| Flash controller | on-chip | NXP MSF1 Flash Memory Module (FMU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x.dtsi?plain=1#L19) | [`nxp,msf1`](../../../../build/dts/api/bindings/flash_controller/nxp,msf1.md#std-dtcompatible-nxp-msf1) |
| GPIO & Headers | on-chip | Kinetis GPIO[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L112)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L132) | [`nxp,kinetis-gpio`](../../../../build/dts/api/bindings/gpio/nxp,kinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio) |
| on-board | GPIO pins exposed on NXP LCD 8080 interface (e.g., used on LCD-PAR-035 panel)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxn236/frdm_mcxn236.dtsi?plain=1#L54) | [`nxp,lcd-8080`](../../../../build/dts/api/bindings/gpio/nxp,lcd-8080.md#std-dtcompatible-nxp-lcd-8080) |
| I2C | on-chip | NXP LPI2C controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L282)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L198) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp,lpi2c.md#std-dtcompatible-nxp-lpi2c) |
| I3C | on-chip | NXP MCUX I3C controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L824)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L811) | [`nxp,mcux-i3c`](../../../../build/dts/api/bindings/i3c/nxp,mcux-i3c.md#std-dtcompatible-nxp-mcux-i3c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxn236/frdm_mcxn236.dtsi?plain=1#L37) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxn236/frdm_mcxn236.dtsi?plain=1#L21) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Multi-Function Device | on-chip | Low Power Flexcomm[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L250)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L172) | [`nxp,lp-flexcomm`](../../../../build/dts/api/bindings/mfd/nxp,lp-flexcomm.md#std-dtcompatible-nxp-lp-flexcomm) |
| MIPI-DBI | on-chip | NXP FlexIO LCD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L805) | [`nxp,mipi-dbi-flexio-lcdif`](../../../../build/dts/api/bindings/mipi-dbi/nxp,mipi-dbi-flexio-lcdif.md#std-dtcompatible-nxp-mipi-dbi-flexio-lcdif) |
| Miscellaneous | on-chip | NXP FlexIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L799) | [`nxp,flexio`](../../../../build/dts/api/bindings/misc/nxp,flexio.md#std-dtcompatible-nxp-flexio) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L25) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L519) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxn236/frdm_mcxn236.dtsi?plain=1#L114) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | NXP PORT Pin Controller[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L76) | [`nxp,port-pinmux`](../../../../build/dts/api/bindings/pinctrl/nxp,port-pinmux.md#std-dtcompatible-nxp-port-pinmux) |
| on-chip | NXP PORT Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L32) | [`nxp,port-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,port-pinctrl.md#std-dtcompatible-nxp-port-pinctrl) |
| PWM | on-chip | NXP eFLEX PWM module with mcux-pwm submodules[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L543) | [`nxp,flexpwm`](../../../../build/dts/api/bindings/pwm/nxp,flexpwm.md#std-dtcompatible-nxp-flexpwm) |
| on-chip | NXP MCUX PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L598)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L548) | [`nxp,imx-pwm`](../../../../build/dts/api/bindings/pwm/nxp,imx-pwm.md#std-dtcompatible-nxp-imx-pwm) |
| Regulator | on-chip | NXP VREF SOC peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L703) | [`nxp,vref`](../../../../build/dts/api/bindings/regulator/nxp,vref.md#std-dtcompatible-nxp-vref) |
| Reset controller | on-chip | LPC SYSCON Peripheral reset controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L70) | [`nxp,lpc-syscon-reset`](../../../../build/dts/api/bindings/reset/nxp,lpc-syscon-reset.md#std-dtcompatible-nxp-lpc-syscon-reset) |
| RTC | on-chip | IRTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L890) | [`nxp,irtc`](../../../../build/dts/api/bindings/rtc/nxp,irtc.md#std-dtcompatible-nxp-irtc) |
| Sensors | on-chip | NXP low-power analog comparator (LPCMP)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L763)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L771) | [`nxp,lpcmp`](../../../../build/dts/api/bindings/sensor/nxp,lpcmp.md#std-dtcompatible-nxp-lpcmp) |
| Serial controller | on-chip | NXP LPUART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L260)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L182) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp,lpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP LPSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L308)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L188) | [`nxp,lpspi`](../../../../build/dts/api/bindings/spi/nxp,lpspi.md#std-dtcompatible-nxp-lpspi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L56) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | NXP OS Timer on i.MX-RT5xx/6xx[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L528) | [`nxp,os-timer`](../../../../build/dts/api/bindings/timer/nxp,os-timer.md#std-dtcompatible-nxp-os-timer) |
| USB | on-chip | NXP EHCI USB device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L748) | [`nxp,ehci`](../../../../build/dts/api/bindings/usb/nxp,ehci.md#std-dtcompatible-nxp-ehci) |
| on-chip | NXP USB High Speed PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L757) | [`nxp,usbphy`](../../../../build/dts/api/bindings/usb/nxp,usbphy.md#std-dtcompatible-nxp-usbphy) |
| Watchdog | on-chip | LPC Windowed Watchdog Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxn23x_common.dtsi?plain=1#L535) | [`nxp,lpc-wwdt`](../../../../build/dts/api/bindings/watchdog/nxp,lpc-wwdt.md#std-dtcompatible-nxp-lpc-wwdt) |

### Connections and IOs

The MCX-N236 SoC has 6 gpio controllers and has pinmux registers which
can be used to configure the functionality of a pin.

| Name | Function | Usage |
| --- | --- | --- |
| P0\_PIO1\_8 | UART | UART RX |
| P1\_PIO1\_9 | UART | UART TX |

### System Clock

The MCX-N236 SoC is configured to use PLL0 running at 150MHz as a source for
the system clock.

### Serial Port

The FRDM-MCXN236 SoC has 8 FLEXCOMM interfaces for serial communication.
Flexcomm 4 is configured as UART for the console.

## Programming and Debugging

The `frdm_mcxn236` board supports the runners and associated west commands listed below.

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
10-pin SWD connector (J12) of the board. Additionally, the jumper JP7 must
be shortened.
For both options use the `-r jlink` option with west to use the jlink runner.

```shell
west flash -r jlink
```

### Configuring a Console

Connect a USB cable from your PC to J10, and use the serial terminal of your choice
(minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b frdm_mcxn236 samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```shell
*** Booting Zephyr OS build v3.6.0-4478-ge6c3a42f5f52 ***
Hello World! frdm_mcxn236/mcxn236
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b frdm_mcxn236/mcxn236 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
*** Booting Zephyr OS build v3.6.0-4478-ge6c3a42f5f52 ***
Hello World! frdm_mcxn236/mcxn236
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

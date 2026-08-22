---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/twr_ke18f/doc/index.html
original_path: boards/nxp/twr_ke18f/doc/index.html
---

# TWR-KE18F

Board Overview

[![../../../../_images/TWR-KE18F-DEVICE.jpg](../../../../_images/TWR-KE18F-DEVICE.jpg)
](../../../../_images/TWR-KE18F-DEVICE.jpg)

TWR-KE18F

Name:
:   `twr_ke18f`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mke18f16

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/twr_ke18f/doc/index.rst/../..)

## Overview

The TWR-KE18F is a development board for NXP Kinetis KE1xF 32-bit
MCU-based platforms. The onboard OpenSDAv2 serial and debug adapter,
running an open source bootloader, offers options for serial
communication, flash programming, and run-control debugging.

## Hardware

- MKE18F512VLL16 MCU (up to 168 MHz, 512 KB flash memory, 64 KB RAM,
  and 100 Low profile Quad Flat Package (LQFP))
- 3.3 V or 5 V MCU operation
- 6-axis FXOS8700CQ digital accelerometer and magnetometer
- RGB LED
- Four user LEDs
- Two user push-buttons
- Potentiometer
- Thermistor
- Infrared port (IrDA)
- CAN pin header
- Flex I/O pin header

For more information about the KE1xF SoC and the TWR-KE18F board, see
these NXP reference documents:

- [KE1xF Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/kinetis-cortex-m-mcus/e-series5v-robustm0-plus-m4/kinetis-ke1xf-168mhz-performance-with-can-5v-microcontrollers-based-on-arm-cortex-m4:KE1xF)
- [KE1xF Datasheet](https://www.nxp.com/docs/en/data-sheet/KE1xFP100M168SF0.pdf)
- [KE1xF Reference Manual](https://www.nxp.com/docs/en/reference-manual/KE1xFP100M168SF0RM.pdf)
- [TWR-KE18F Website](https://www.nxp.com/TWR-KE18F)
- [TWR-KE18F User Guide](https://www.nxp.com/docs/en/user-guide/TWRKE18FUG.pdf)
- [TWR-KE18F Schematics](https://www.nxp.com/webapp/Download?colCode=TWR-KE18F-SCH-DESIGNFILES)

### Supported Features

The `twr_ke18f` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `twr_ke18f/mke18f16` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L27) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | NXP ADC12[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L508)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L519) | [`nxp,adc12`](../../../../build/dts/api/bindings/adc/nxp%2Cadc12.md#std-dtcompatible-nxp-adc12) |
| CAN | on-chip | NXP FlexCAN controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L406)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L417) | [`nxp,flexcan`](../../../../build/dts/api/bindings/can/nxp%2Cflexcan.md#std-dtcompatible-nxp-flexcan) |
| Clock control | on-chip | Kinetis KE1xF System Integration Module (SIM) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L122) | [`nxp,kinetis-ke1xf-sim`](../../../../build/dts/api/bindings/clock/nxp%2Ckinetis-ke1xf-sim.md#std-dtcompatible-nxp-kinetis-ke1xf-sim) |
| on-chip | NXP Kinetis SCG (System Clock Generator) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L127) | [`nxp,kinetis-scg`](../../../../build/dts/api/bindings/clock/nxp%2Ckinetis-scg.md#std-dtcompatible-nxp-kinetis-scg) |
| on-chip | Generic fixed-rate clock provider[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L132) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Generic fixed factor clock provider[14 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L150) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| on-chip | NXP Kinetis PCC (Peripheral Clock Controller) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L261) | [`nxp,kinetis-pcc`](../../../../build/dts/api/bindings/clock/nxp%2Ckinetis-pcc.md#std-dtcompatible-nxp-kinetis-pcc) |
| Comparator | on-chip | NXP Kinetis ACMP (Analog CoMParator)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L577) | [`nxp,kinetis-acmp`](../../../../build/dts/api/bindings/comparator/nxp%2Ckinetis-acmp.md#std-dtcompatible-nxp-kinetis-acmp) |
| Counter | on-chip | NXP LPTMR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L287) | [`nxp,lptmr`](../../../../build/dts/api/bindings/counter/nxp%2Clptmr.md#std-dtcompatible-nxp-lptmr) |
| DAC | on-chip | NXP Kinetis MCUX DAC32[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L276) | [`nxp,kinetis-dac32`](../../../../build/dts/api/bindings/dac/nxp%2Ckinetis-dac32.md#std-dtcompatible-nxp-kinetis-dac32) |
| DMA | on-chip | NXP MCUX EDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L100) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp%2Cmcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| Flash controller | on-chip | NXP Kinetis Flash Memory Module E (FTFE)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L317) | [`nxp,kinetis-ftfe`](../../../../build/dts/api/bindings/flash_controller/nxp%2Ckinetis-ftfe.md#std-dtcompatible-nxp-kinetis-ftfe) |
| GPIO & Headers | on-chip | Kinetis GPIO[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L458) | [`nxp,kinetis-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Ckinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio) |
| I2C | on-chip | NXP LPI2C controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L360) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp%2Clpi2c.md#std-dtcompatible-nxp-lpi2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/twr_ke18f/twr_ke18f.dts?plain=1#L124) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/twr_ke18f/twr_ke18f.dts?plain=1#L58) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/twr_ke18f/twr_ke18f.dts?plain=1#L91) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Miscellaneous | on-chip | NXP FlexIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L601) | [`nxp,flexio`](../../../../build/dts/api/bindings/misc/nxp%2Cflexio.md#std-dtcompatible-nxp-flexio) |
| MMU / MPU | on-chip | NXP System Memory Protection Unit (SYSMPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L116) | [`nxp,sysmpu`](../../../../build/dts/api/bindings/mmu_mpu/nxp%2Csysmpu.md#std-dtcompatible-nxp-sysmpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf512vlx16.dtsi?plain=1#L33) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/twr_ke18f/twr_ke18f.dts?plain=1#L337) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | NXP PORT Pin Controller[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L428) | [`nxp,port-pinmux`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cport-pinmux.md#std-dtcompatible-nxp-port-pinmux) |
| on-chip | NXP PORT Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L94) | [`nxp,port-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cport-pinctrl.md#std-dtcompatible-nxp-port-pinctrl) |
| PWM | on-chip | Kinetis PWT PWM Capture[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L306) | [`nxp,kinetis-pwt`](../../../../build/dts/api/bindings/pwm/nxp%2Ckinetis-pwt.md#std-dtcompatible-nxp-kinetis-pwt) |
| on-chip | NXP FlexTimer Module (FTM) PWM controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L541) | [`nxp,ftm-pwm`](../../../../build/dts/api/bindings/pwm/nxp%2Cftm-pwm.md#std-dtcompatible-nxp-ftm-pwm) |
| RTC | on-chip | NXP Real Time Clock (RTC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L267) | [`nxp,rtc`](../../../../build/dts/api/bindings/rtc/nxp%2Crtc.md#std-dtcompatible-nxp-rtc) |
| Sensors | on-board | FXOS8700 6-axis accelerometer/magnetometer sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/twr_ke18f/twr_ke18f.dts?plain=1#L250) | [`nxp,fxos8700`](../../../../build/dts/api/compatibles/nxp%2Cfxos8700.md#std-dtcompatible-nxp-fxos8700) |
| on-chip | NXP Kinetis temperature sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L60)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L71) | [`nxp,kinetis-temperature`](../../../../build/dts/api/bindings/sensor/nxp%2Ckinetis-temperature.md#std-dtcompatible-nxp-kinetis-temperature) |
| Serial controller | on-chip | NXP LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L327)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L338) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp%2Clpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP LPSPI controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L382) | [`nxp,lpspi`](../../../../build/dts/api/bindings/spi/nxp%2Clpspi.md#std-dtcompatible-nxp-lpspi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf512vlx16.dtsi?plain=1#L26) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | NXP FlexTimer Module (FTM)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L550) | [`nxp,ftm`](../../../../build/dts/api/bindings/timer/nxp%2Cftm.md#std-dtcompatible-nxp-ftm) |
| Watchdog | on-chip | NXP watchdog (WDOG32)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_ke1xf.dtsi?plain=1#L297) | [`nxp,wdog32`](../../../../build/dts/api/bindings/watchdog/nxp%2Cwdog32.md#std-dtcompatible-nxp-wdog32) |

### System Clock

The KE18 SoC is configured to use the 8 MHz external oscillator on the
board with the on-chip PLL to generate a 120 MHz system clock.

### Serial Port

The KE18 SoC has three UARTs. UART0 is configured for the console. The
remaining UARTs are not used.

### Accelerometer and magnetometer

The TWR-KE18F board by default only supports polling the FXOS8700
accelerometer and magnetometer for sensor values
(`CONFIG_FXOS8700_TRIGGER_NONE=y`).

In order to support FXOS8700 triggers (interrupts) the 0 ohm resistors
`R47` and `R57` must be mounted on the TWR-KE18F board. The
devicetree must also be modified to describe the FXOS8700 interrupt
GPIOs:

```devicetree
/dts-v1/;

&fxos8700 {
        int1-gpios = <&gpioa 14 0>;
        int2-gpios = <&gpioc 17 0>;
};
```

Finally, a trigger option must be enabled in Kconfig (either
`FXOS8700_TRIGGER_GLOBAL_THREAD=y` or
`FXOS8700_TRIGGER_OWN_THREAD=y`).

## Programming and Debugging

The `twr_ke18f` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **canopen** | ✅ |  |  |  |  |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe).

Early versions of this board have an outdated version of the OpenSDA bootloader
and require an update. Please see the [DAPLink Bootloader Update](https://os.mbed.com/blog/entry/DAPLink-bootloader-update/) page for
instructions to update from the CMSIS-DAP bootloader to the DAPLink bootloader.

#### Option 1: [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe) (Recommended)

Install the [pyOCD Debug Host Tools](../../../../develop/flash_debug/host-tools.md#pyocd-debug-host-tools) and make sure they are in your search
path.

Follow the instructions in [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe) to program
the [OpenSDA DAPLink TWR-KE18F Firmware](https://www.nxp.com/support/developer-resources/run-time-software/kinetis-developer-resources/ides-for-kinetis-mcus/opensda-serial-and-debug-adapter:OPENSDA#TWR-KE18F).

#### Option 2: [OpenSDA J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-jlink-onboard-debug-probe)

Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search
path.

Follow the instructions in [OpenSDA J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-jlink-onboard-debug-probe) to program
the [OpenSDA J-Link Firmware for TWR-KE18F](https://www.segger.com/downloads/jlink/OpenSDA_TWR-KE18F).

Add the arguments `-DBOARD_FLASH_RUNNER=jlink` and
`-DBOARD_DEBUG_RUNNER=jlink` when you invoke `west build` to override the
default runner from pyOCD to J-Link:

```shell
# From the root of the zephyr repository
west build -b twr_ke18f samples/hello_world -- -DBOARD_FLASH_RUNNER=jlink -DBOARD_DEBUG_RUNNER=jlink
```

### Configuring a Console

Regardless of your choice in debug probe, we will use the OpenSDA
microcontroller as a usb-to-serial adapter for the serial console.

Connect a USB cable from your PC to J2.

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
west build -b twr_ke18f samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the SW1 button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-xxx-gxxxxxxxxxxxx *****
Hello World! twr_ke18f
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b twr_ke18f samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-xxx-gxxxxxxxxxxxx *****
Hello World! twr_ke18f
```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

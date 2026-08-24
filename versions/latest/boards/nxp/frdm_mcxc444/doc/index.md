---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/frdm_mcxc444/doc/index.html
original_path: boards/nxp/frdm_mcxc444/doc/index.html
---

# FRDM-MCXC444

Board Overview

[![../../../../_images/frdm_mcxc444.webp](https://docs.zephyrproject.org/4.2.0/_images/frdm_mcxc444.webp)
](https://docs.zephyrproject.org/4.2.0/_images/frdm_mcxc444.webp)

FRDM-MCXC444

Name:
:   `frdm_mcxc444`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mcxc444

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/frdm_mcxc444/doc/index.rst/../..)

## Overview

FRDM-MCXC444 is a compact and scalable development board for rapid
prototyping of MCX C444 MCU. It offers industry standard headers
for easy access to the MCU’s I/Os, integrated open-standard serial
interfaces and on-board MCU-Link debugger.
The MCXC is a general purpose ultra-low-power MCU family,
providing additional memory, communications and analog peripheral.

## Hardware

- MCXC444VLH Arm Cortex-M0+ microcontroller running at 48 MHz
- 64LQFP package
- 256 KB flash
- 32 KB SRAM
- USB FS 2.0
- 2x low-power UART, 1x UART, 2x I2C, 2x SPI
- FXLS8974CF accelerometer
- Tri-color LED
- On-board MCU-Link debugger with CMSIS-DAP
- Arduino Header, mikroBUS, Pmod

For more information about the MCXC444 SoC and FRDM-MCXC444 board, see
these references:

- [MCX C14x/24x/44x Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/mcx-arm-cortex-m/mcx-c-series-microcontrollers/mcx-c14x-24x-44x-mcus-with-arm-cortex-m0-plus-entry-level-mcus-with-usb-segment-lcd-and-classical-peripherals:MCX-C14x-24x-44x)
- [MCX C44x Datasheet](https://www.nxp.com/docs/en/data-sheet/MCXC44XP64M48SF6.pdf)
- [MCX C44x Reference Manual](https://www.nxp.com/webapp/Download?colCode=MCXC44XP64M48RM)
- [FRDM-MCXC444 Website](https://www.nxp.com/design/design-center/development-boards-and-designs/general-purpose-mcus/frdm-development-board-for-mcx-c444-mcus:FRDM-MCXC444)
- [FRDM-MCXC444 User Manual](https://www.nxp.com/webapp/Download?colCode=UM12120)
- [FRDM-MCXC444 Design Files](https://www.nxp.com/webapp/Download?colCode=FRDM-MCXC444-DESIGNFILES)

### Supported Features

The `frdm_mcxc444` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `frdm_mcxc444/mcxc444` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxc_common.dtsi?plain=1#L25) | [`arm,cortex-m0+`](../../../../build/dts/api/bindings/cpu/arm,cortex-m0+.md#std-dtcompatible-arm-cortex-m0) |
| ADC | on-chip | Kinetis ADC16[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxc_common.dtsi?plain=1#L186) | [`nxp,kinetis-adc16`](../../../../build/dts/api/bindings/adc/nxp,kinetis-adc16.md#std-dtcompatible-nxp-kinetis-adc16) |
| Clock control | on-chip | NXP Kinetis Multipurpose Clock generator (MCG) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxc_common.dtsi?plain=1#L81) | [`nxp,kinetis-mcg`](../../../../build/dts/api/bindings/clock/nxp,kinetis-mcg.md#std-dtcompatible-nxp-kinetis-mcg) |
| on-chip | Kinetis System Integration Module (SIM) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxc_common.dtsi?plain=1#L89) | [`nxp,kinetis-sim`](../../../../build/dts/api/bindings/clock/nxp,kinetis-sim.md#std-dtcompatible-nxp-kinetis-sim) |
| on-chip | Generic fixed factor clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxc_common.dtsi?plain=1#L94) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| on-chip | NXP MCXC oscillator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxc_common.dtsi?plain=1#L43) | [`nxp,mcxc-osc`](../../../../build/dts/api/bindings/clock/nxp,mcxc-osc.md#std-dtcompatible-nxp-mcxc-osc) |
| Counter | on-chip | NXP LPTMR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxc_common.dtsi?plain=1#L280) | [`nxp,lptmr`](../../../../build/dts/api/bindings/counter/nxp,lptmr.md#std-dtcompatible-nxp-lptmr) |
| on-chip | NXP Periodic Interrupt Timer (PIT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxc_common.dtsi?plain=1#L302) | [`nxp,pit`](../../../../build/dts/api/bindings/counter/nxp,pit.md#std-dtcompatible-nxp-pit) |
| on-chip | Child node for the Periodic Interrupt Timer node, intended for an individual timer channel[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxc_common.dtsi?plain=1#L312) | [`nxp,pit-channel`](../../../../build/dts/api/bindings/counter/nxp,pit-channel.md#std-dtcompatible-nxp-pit-channel) |
| Flash controller | on-chip | NXP Kinetis Flash Memory Module A (FTFA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxc_common.dtsi?plain=1#L63) | [`nxp,kinetis-ftfa`](../../../../build/dts/api/bindings/flash_controller/nxp,kinetis-ftfa.md#std-dtcompatible-nxp-kinetis-ftfa) |
| GPIO & Headers | on-chip | Kinetis GPIO[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxc_common.dtsi?plain=1#L139) | [`nxp,kinetis-gpio`](../../../../build/dts/api/bindings/gpio/nxp,kinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio) |
| I2C | on-chip | Kinetis I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxc_common.dtsi?plain=1#L194)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxc_common.dtsi?plain=1#L205) | [`nxp,kinetis-i2c`](../../../../build/dts/api/bindings/i2c/nxp,kinetis-i2c.md#std-dtcompatible-nxp-kinetis-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxc444/frdm_mcxc444.dts?plain=1#L73) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxc444/frdm_mcxc444.dts?plain=1#L40) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxc444/frdm_mcxc444.dts?plain=1#L56) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxc_common.dtsi?plain=1#L74) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | NXP PORT Pin Controller[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxc_common.dtsi?plain=1#L109) | [`nxp,port-pinmux`](../../../../build/dts/api/bindings/pinctrl/nxp,port-pinmux.md#std-dtcompatible-nxp-port-pinmux) |
| on-chip | NXP PORT Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxc_common.dtsi?plain=1#L37) | [`nxp,port-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,port-pinctrl.md#std-dtcompatible-nxp-port-pinctrl) |
| PWM | on-chip | MCUX Timer/PWM Module (TPM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxc_common.dtsi?plain=1#L250)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxc_common.dtsi?plain=1#L260) | [`nxp,kinetis-tpm`](../../../../build/dts/api/bindings/pwm/nxp,kinetis-tpm.md#std-dtcompatible-nxp-kinetis-tpm) |
| RTC | on-chip | NXP Real Time Clock (RTC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxc_common.dtsi?plain=1#L292) | [`nxp,rtc`](../../../../build/dts/api/bindings/rtc/nxp,rtc.md#std-dtcompatible-nxp-rtc) |
| Sensors | on-board | FXLS8974 3-axis accelerometer sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxc444/frdm_mcxc444.dts?plain=1#L133) | [`nxp,fxls8974`](../../../../build/dts/api/compatibles/nxp,fxls8974.md#std-dtcompatible-nxp-fxls8974) |
| on-chip | NXP Kinetis temperature sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxc_common.dtsi?plain=1#L51) | [`nxp,kinetis-temperature`](../../../../build/dts/api/bindings/sensor/nxp,kinetis-temperature.md#std-dtcompatible-nxp-kinetis-temperature) |
| Serial controller | on-chip | NXP LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxc_common.dtsi?plain=1#L225)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxc_common.dtsi?plain=1#L233) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp,lpuart.md#std-dtcompatible-nxp-lpuart) |
| on-chip | Kinetis UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxc_common.dtsi?plain=1#L241) | [`nxp,kinetis-uart`](../../../../build/dts/api/bindings/serial/nxp,kinetis-uart.md#std-dtcompatible-nxp-kinetis-uart) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxc_common.dtsi?plain=1#L32) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv6-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21) | [`arm,armv6m-systick`](../../../../build/dts/api/bindings/timer/arm,armv6m-systick.md#std-dtcompatible-arm-armv6m-systick) |
| USB | on-chip | NPX Kinetis USBFSOTG Controller in device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_mcxc_common.dtsi?plain=1#L216) | [`nxp,kinetis-usbd`](../../../../build/dts/api/bindings/usb/nxp,kinetis-usbd.md#std-dtcompatible-nxp-kinetis-usbd) |

### Connections and IOs

The MCXC444 SoC has five pairs of pinmux/gpio controllers (PORTA/GPIOA,
PORTB/GPIOB, PORTC/GPIOC, PORTD/GPIOD, and PORTE/GPIOE) for the FRDM-MCXC444 board.

| Name | Function | Usage |
| --- | --- | --- |
| PTE20 | ADC | ADC0 channel 1 |
| PTE31 | GPIO | Red LED |
| PTD5 | GPIO | Green LED |
| PTE29 | GPIO | Blue LED |
| PTA1 | LPUART0\_RX | UART Console |
| PTA2 | LPUART0\_TX | UART Console |
| PTA20 | RESET | RESET Button SW1 |
| PTC3 | GPIO | User button SW2 |
| PTA4 | GPIO | User button SW3 |
| PTE25 | I2C0\_SDA | I2C accelerometer |
| PTE24 | I2C0\_SCL | I2C accelerometer |

### System Clock

The MCXC444 SoC is configured to use HIRC running at 48 MHz as a system clock source.

### Serial Port

The MCXC444 LPUART0 is used for the console.

## Programming and Debugging

The `frdm_mcxc444` board supports the runners and associated west commands listed below.

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
short jumper JP2.

#### Using J-Link

There are two options. The onboard debug circuit can be updated with Segger
J-Link firmware by following the instructions in
[MCU-Link JLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#mcu-link-jlink-onboard-debug-probe).
To be able to program the firmware, you need to put the board in `DFU mode`
by shortening the jumper JP1.
The second option is to attach a [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe) to the
10-pin SWD connector (J10) of the board. Additionally, the jumper JP4 must
be shortened.
For both options use the `-r jlink` option with west to use the jlink runner.

```shell
west flash -r jlink
```

### Configuring a Console

Connect a USB cable from your PC to J13, and use the serial terminal of your choice
(minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b frdm_mcxc444 samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the SW1 button), and you should
see the following message in the terminal:

```shell
*** Booting Zephyr OS build v3.6.0-4475-gfa5bd8bb098e ***
Hello World! frdm_mcxc444/mcxc444
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b frdm_mcxc444 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
*** Booting Zephyr OS build v3.6.0-4475-gfa5bd8bb098e ***
Hello World! frdm_mcxc444/mcxc444
```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

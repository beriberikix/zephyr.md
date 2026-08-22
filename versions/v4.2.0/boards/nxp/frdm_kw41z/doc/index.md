---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/frdm_kw41z/doc/index.html
original_path: boards/nxp/frdm_kw41z/doc/index.html
---

# FRDM-KW41Z

Board Overview

[![../../../../_images/frdm_kw41z.jpg](../../../../_images/frdm_kw41z.jpg)
](../../../../_images/frdm_kw41z.jpg)

FRDM-KW41Z

Name:
:   `frdm_kw41z`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mkw41z4

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/frdm_kw41z/doc/index.rst/../..)

## Overview

The FRDM-KW41Z is a development kit enabled by the Kinetis® W series
KW41Z/31Z/21Z (KW41Z) family built on ARM® Cortex®-M0+ processor with
integrated 2.4 GHz transceiver supporting Bluetooth® Smart/Bluetooth® Low Energy
(BLE) v4.2, Generic FSK, IEEE® 802.15.4 and Thread.

The FRDM-KW41Z kit contains two Freedom boards that can be used as a
development board or a shield to connect to a host processor. The FRDM-KW41Z is
form-factor compatible with the Arduino™ R3 pin layout for more expansion
options.

The FRDM-KW41Z highly-sensitive, optimized 2.4 GHz radio features a PCB
F-antenna which can be bypassed to test via SMA connection, multiple power
supply options, push/capacitive touch buttons, switches, LEDs and integrated
sensors.

## Hardware

- Can be configured as Host or Shield for connection to Host Processor
- Supports all DC-DC configurations (Buck, Boost, Bypass)
- PCB inverted F-type antenna
- SMA RF Connector
- RF regulatory certified
- Serial Flash for OTA firmware upgrades
- On board NXP FXOS8700CQ digital sensor, 3D Accelerometer ( ±2g/
  ±4g/ ±8g) + 3D
  Magnetometer
- OpenSDA and JTAG debug

For more information about the KW41Z SoC and FRDM-KW41Z board:

- [KW41Z Website](https://www.nxp.com/products/wireless/zigbee/kinetis-kw41z-2.4-ghz-dual-mode-bluetooth-low-energy-and-802.15.4-wireless-radio-microcontroller-mcu-based-on-arm-cortex-m0-plus-core:KW41Z)
- [KW41Z Datasheet](https://www.nxp.com/docs/en/data-sheet/MKW41Z512.pdf)
- [KW41Z Reference Manual](https://www.nxp.com/webapp/Download?colCode=MKW41Z512RM)
- [FRDM-KW41Z Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/kinetis-cortex-m-mcus/w-serieswireless-conn.m0-plus-m4/freedom-development-kit-for-kinetis-kw41z-31z-21z-mcus:FRDM-KW41Z)
- [FRDM-KW41Z User Guide](https://www.nxp.com/webapp/Download?colCode=FRDMKW41ZUG)
- [FRDM-KW41Z Schematics](https://www.nxp.com/webapp/Download?colCode=FRDM-KW41Z-SCH)

### Supported Features

The `frdm_kw41z` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `frdm_kw41z/mkw41z4` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw41z.dtsi?plain=1#L26) | [`arm,cortex-m0+`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m0%2B.md#std-dtcompatible-arm-cortex-m0) |
| ADC | on-chip | Kinetis ADC16[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw41z.dtsi?plain=1#L234) | [`nxp,kinetis-adc16`](../../../../build/dts/api/bindings/adc/nxp%2Ckinetis-adc16.md#std-dtcompatible-nxp-kinetis-adc16) |
| Clock control | on-chip | NXP Kinetis Multipurpose Clock generator (MCG) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw41z.dtsi?plain=1#L45) | [`nxp,kinetis-mcg`](../../../../build/dts/api/bindings/clock/nxp%2Ckinetis-mcg.md#std-dtcompatible-nxp-kinetis-mcg) |
| on-chip | Kinetis System Integration Module (SIM) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw41z.dtsi?plain=1#L65) | [`nxp,kinetis-sim`](../../../../build/dts/api/bindings/clock/nxp%2Ckinetis-sim.md#std-dtcompatible-nxp-kinetis-sim) |
| on-chip | Generic fixed factor clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw41z.dtsi?plain=1#L70) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| Flash controller | on-chip | NXP Kinetis Flash Memory Module A (FTFA)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw41z.dtsi?plain=1#L85) | [`nxp,kinetis-ftfa`](../../../../build/dts/api/bindings/flash_controller/nxp%2Ckinetis-ftfa.md#std-dtcompatible-nxp-kinetis-ftfa) |
| GPIO & Headers | on-chip | Kinetis GPIO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw41z.dtsi?plain=1#L151)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw41z.dtsi?plain=1#L161) | [`nxp,kinetis-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Ckinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_kw41z/frdm_kw41z.dts?plain=1#L85) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | Kinetis I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw41z.dtsi?plain=1#L113)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw41z.dtsi?plain=1#L102) | [`nxp,kinetis-i2c`](../../../../build/dts/api/bindings/i2c/nxp%2Ckinetis-i2c.md#std-dtcompatible-nxp-kinetis-i2c) |
| IEEE 802.15.4 | on-chip | NXP KW41Z IEEE 802.15.4 node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw41z.dtsi?plain=1#L249) | [`nxp,kw41z-ieee802154`](../../../../build/dts/api/bindings/ieee802154/nxp%2Ckw41z-ieee802154.md#std-dtcompatible-nxp-kw41z-ieee802154) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_kw41z/frdm_kw41z.dts?plain=1#L71) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_kw41z/frdm_kw41z.dts?plain=1#L39) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_kw41z/frdm_kw41z.dts?plain=1#L55) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw41z.dtsi?plain=1#L94) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_kw41z/frdm_kw41z.dts?plain=1#L179) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | NXP PORT Pin Controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw41z.dtsi?plain=1#L133) | [`nxp,port-pinmux`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cport-pinmux.md#std-dtcompatible-nxp-port-pinmux) |
| on-chip | NXP PORT Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw41z.dtsi?plain=1#L39) | [`nxp,port-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cport-pinctrl.md#std-dtcompatible-nxp-port-pinctrl) |
| PWM | on-chip | MCUX Timer/PWM Module (TPM)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw41z.dtsi?plain=1#L201)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw41z.dtsi?plain=1#L212) | [`nxp,kinetis-tpm`](../../../../build/dts/api/bindings/pwm/nxp%2Ckinetis-tpm.md#std-dtcompatible-nxp-kinetis-tpm) |
| RNG | on-chip | Kinetis TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw41z.dtsi?plain=1#L242) | [`nxp,kinetis-trng`](../../../../build/dts/api/bindings/rng/nxp%2Ckinetis-trng.md#std-dtcompatible-nxp-kinetis-trng) |
| RTC | on-chip | NXP Real Time Clock (RTC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw41z.dtsi?plain=1#L57) | [`nxp,rtc`](../../../../build/dts/api/bindings/rtc/nxp%2Crtc.md#std-dtcompatible-nxp-rtc) |
| Sensors | on-board | FXOS8700 6-axis accelerometer/magnetometer sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_kw41z/frdm_kw41z.dts?plain=1#L130) | [`nxp,fxos8700`](../../../../build/dts/api/compatibles/nxp%2Cfxos8700.md#std-dtcompatible-nxp-fxos8700) |
| Serial controller | on-chip | NXP LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw41z.dtsi?plain=1#L124) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp%2Clpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP DSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw41z.dtsi?plain=1#L180)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw41z.dtsi?plain=1#L191) | [`nxp,dspi`](../../../../build/dts/api/bindings/spi/nxp%2Cdspi.md#std-dtcompatible-nxp-dspi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_kw41z.dtsi?plain=1#L33) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv6-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21) | [`arm,armv6m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv6m-systick.md#std-dtcompatible-arm-armv6m-systick) |

### Connections and IOs

The KW41Z SoC has three pairs of pinmux/gpio controllers, but only two are
currently enabled (PORTA/GPIOA and PORTC/GPIOC) for the FRDM-KW41Z board.

| Name | Function | Usage |
| --- | --- | --- |
| PTC1 | GPIO | Red LED / FXOS8700 INT1 |
| PTA19 | GPIO | Green LED |
| PTA18 | GPIO | Blue LED |
| PTB2 | ADC | ADC0 channel 3 |
| PTC2 | I2C1\_SCL | I2C / FXOS8700 |
| PTC3 | I2C1\_SDA | I2C / FXOS8700 |
| PTC4 | GPIO | SW3 |
| PTC5 | GPIO | SW4 |
| PTC6 | LPUART0\_RX | UART Console |
| PTC7 | LPUART0\_TX | UART Console |
| PTC16 | SPI0\_SCK | SPI |
| PTC17 | SPI0\_SOUT | SPI |
| PTC18 | SPI0\_SIN | SPI |
| PTC19 | SPI0\_PCS0 | SPI |

### System Clock

The KW41Z SoC is configured to use the 32 MHz external oscillator on the board
with the on-chip FLL to generate a 40 MHz system clock.

### Serial Port

The KW41Z SoC has one UART, which is used for the console.

## Programming and Debugging

The `frdm_kw41z` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe).

#### Option 1: [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe) (Recommended)

Install the [pyOCD Debug Host Tools](../../../../develop/flash_debug/host-tools.md#pyocd-debug-host-tools) and make sure they are in your search
path.

Follow the instructions in [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe) to program
the [OpenSDA DAPLink FRDM-KW41Z Firmware](https://www.nxp.com/downloads/en/reference-applications/OpenSDAv2.2_DAPLink_frdmkw41z_rev0241.zip).

#### Option 2: [OpenSDA J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-jlink-onboard-debug-probe)

Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search
path.

Follow the instructions in [OpenSDA J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-jlink-onboard-debug-probe) to program
the [OpenSDA J-Link FRDM-KW41Z Firmware](https://www.segger.com/downloads/jlink/OpenSDA_FRDM-KW41Z).

Add the arguments `-DBOARD_FLASH_RUNNER=jlink` and
`-DBOARD_DEBUG_RUNNER=jlink` when you invoke `west build` to override the
default runner from pyOCD to J-Link:

```shell
# From the root of the zephyr repository
west build -b frdm_kw41z samples/hello_world -- -DBOARD_FLASH_RUNNER=jlink -DBOARD_DEBUG_RUNNER=jlink
```

### Configuring a Console

Regardless of your choice in debug probe, we will use the OpenSDA
microcontroller as a usb-to-serial adapter for the serial console.

Connect a USB cable from your PC to J6.

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
west build -b frdm_kw41z samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the SW1 button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! frdm_kw41z
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b frdm_kw41z samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! frdm_kw41z
```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

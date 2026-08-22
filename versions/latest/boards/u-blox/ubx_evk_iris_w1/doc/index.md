---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/u-blox/ubx_evk_iris_w1/doc/index.html
original_path: boards/u-blox/ubx_evk_iris_w1/doc/index.html
---

# EVK-IRIS-W106-RW612

Board Overview

[![../../../../_images/ubx_evk_iris_w1.webp](../../../../_images/ubx_evk_iris_w1.webp)
](../../../../_images/ubx_evk_iris_w1.webp)

EVK-IRIS-W106-RW612

Name:
:   `ubx_evk_iris_w1`

Vendor:
:   u-blox

Architecture:
:   arm

SoC:
:   rw612

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/u-blox/ubx_evk_iris_w1/doc/index.rst/../..)

## Overview

The EVK-IRIS-W10x evaluation kit enables stand-alone use of the IRIS-W10 series module. This guide
provides details about the hardware functionality of the EVK-IRIS-W10 board and includes setup
instructions for starting development.

All pins and interfaces supported on IRIS-W10 series modules are easily accessible from the
evaluation board. Simple USB connections serve as the physical interfaces for power, programming
COM ports, debugging, and USB peripheral connectors. Additionally, the board features other
interfaces like Ethernet RJ45 and an SDIO header. The EVK-IRIS-W10 board is equipped with a Reset
button, Boot button, and two user-configurable buttons. Current sense resistors are incorporated for
accurate current measurement within the module.

For flexible use, GPIO signals are accessible through headers and are complemented by four
mikroBUS™ standard slots for convenient utilization of Click boards™. Each Click board can be
seamlessly plugged into an available mikroBUS™ slot to facilitate effortless hardware expansion with
a variety of standardized compact add-on boards. Click boards are designed to accommodate a
diverse range of electronic modules, including sensors, transceivers, displays, encoders, motor
drivers, connection ports, and more. For further information about the Click boards, visit the MIKROE
website.

## Hardware

- 260 MHz ARM Cortex-M33, tri-radio cores for Wi-Fi 6 + BLE 5.3 + 802.15.4
- 1.2 MB on-chip SRAM
- EVK-IRIS-W101 evaluation board with IRIS-W101 module. Dual-band PCB antenna for WLAN
  with 100 mm coaxial cable and U.FL connector
- EVK-IRIS-W106 evaluation board with IRIS-W106 module. Dual-band integrated PCB trace
  antenna (external antenna not supplied)

### Flash Memory Configuration

The IRIS-W1 board uses different flash vendors depending on revision:

- `@macronix`: Module build up to 2023 week 45
- `@fidelex`: Module build 2023 week 46 (2346) onward

To build for a specific flash version:

```shell
west build -b ubx_evk_iris_w1@macronix
west build -b ubx_evk_iris_w1@fidelex
```

### Supported Features

The `ubx_evk_iris_w1` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `ubx_evk_iris_w1@fidelex/rw612` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L28) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | NXP GAU GPADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L550) | [`nxp,gau-adc`](../../../../build/dts/api/bindings/adc/nxp%2Cgau-adc.md#std-dtcompatible-nxp-gau-adc) |
| ARM architecture | on-chip | LPC Flexcomm node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L272) | [`nxp,lpc-flexcomm`](../../../../build/dts/api/bindings/arm/nxp%2Clpc-flexcomm.md#std-dtcompatible-nxp-lpc-flexcomm) |
| on-chip | RW SOC controller node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L313) | [`nxp,rw-soc-ctrl`](../../../../build/dts/api/bindings/arm/nxp%2Crw-soc-ctrl.md#std-dtcompatible-nxp-rw-soc-ctrl) |
| on-chip | NXP NBU interruption information[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L585) | [`nxp,nbu`](../../../../build/dts/api/bindings/arm/nxp%2Cnbu.md#std-dtcompatible-nxp-nbu) |
| Audio | on-chip | NXP DMIC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L510) | [`nxp,dmic`](../../../../build/dts/api/bindings/audio/nxp%2Cdmic.md#std-dtcompatible-nxp-dmic) |
| Bluetooth | on-chip | NXP BLE HCI information[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L591) | [`nxp,hci-ble`](../../../../build/dts/api/bindings/bluetooth/nxp%2Chci-ble.md#std-dtcompatible-nxp-hci-ble) |
| Clock control | on-chip | LPC SYSCON & CLKCTL IP node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L145) | [`nxp,lpc-syscon`](../../../../build/dts/api/bindings/clock/nxp%2Clpc-syscon.md#std-dtcompatible-nxp-lpc-syscon) |
| Counter | on-chip | Driver that uses the NXP LPC RTC High resolution counter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L373) | [`nxp,lpc-rtc-highres`](../../../../build/dts/api/bindings/counter/nxp%2Clpc-rtc-highres.md#std-dtcompatible-nxp-lpc-rtc-highres) |
| on-chip | NXP MCUX Standard Timer/Counter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L379)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L392) | [`nxp,lpc-ctimer`](../../../../build/dts/api/bindings/counter/nxp%2Clpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer) |
| on-chip | NXP Multirate Timer[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L442) | [`nxp,mrt`](../../../../build/dts/api/bindings/counter/nxp%2Cmrt.md#std-dtcompatible-nxp-mrt) |
| on-chip | NXP Multirate Timer Channel[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L454)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L459) | [`nxp,mrt-channel`](../../../../build/dts/api/bindings/counter/nxp%2Cmrt-channel.md#std-dtcompatible-nxp-mrt-channel) |
| DAC | on-chip | NXP GAU DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L568) | [`nxp,gau-dac`](../../../../build/dts/api/bindings/dac/nxp%2Cgau-dac.md#std-dtcompatible-nxp-gau-dac) |
| DMA | on-chip | NXP LPC DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L345) | [`nxp,lpc-dma`](../../../../build/dts/api/bindings/dma/nxp%2Clpc-dma.md#std-dtcompatible-nxp-lpc-dma) |
| Ethernet | on-chip | NXP ENET IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L603) | [`nxp,enet`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet.md#std-dtcompatible-nxp-enet) |
| on-chip | NXP ENET MAC/L2 Device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L607) | [`nxp,enet-mac`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet-mac.md#std-dtcompatible-nxp-enet-mac) |
| on-chip | NXP ENET PTP (Precision Time Protocol) Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L623) | [`nxp,enet-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock) |
| GPIO & Headers | on-chip | LPC GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L209) | [`nxp,lpc-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Clpc-gpio.md#std-dtcompatible-nxp-lpc-gpio) |
| on-chip | LPC GPIO port device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L215) | [`nxp,lpc-gpio-port`](../../../../build/dts/api/bindings/gpio/nxp%2Clpc-gpio-port.md#std-dtcompatible-nxp-lpc-gpio-port) |
| IEEE 802.15.4 HDLC RCP interface | on-chip | NXP HDLC RCP interface node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L596) | [`nxp,hdlc-rcp-if`](../../../../build/dts/api/bindings/hdlc_rcp_if/nxp%2Chdlc-rcp-if.md#std-dtcompatible-nxp-hdlc-rcp-if) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/u-blox/ubx_evk_iris_w1/ubx_evk_iris_w1_common.dtsi?plain=1#L55) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| on-chip | NXP Pin interrupt and pattern match engine (PINT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L325) | [`nxp,pint`](../../../../build/dts/api/bindings/interrupt-controller/nxp%2Cpint.md#std-dtcompatible-nxp-pint) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/u-blox/ubx_evk_iris_w1/ubx_evk_iris_w1_common.dtsi?plain=1#L36) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | NXP ENET MDIO Features[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L616) | [`nxp,enet-mdio`](../../../../build/dts/api/bindings/mdio/nxp%2Cenet-mdio.md#std-dtcompatible-nxp-enet-mdio) |
| MIPI-DBI | on-chip | NXP LCDIC Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L355) | [`nxp,lcdic`](../../../../build/dts/api/bindings/mipi-dbi/nxp%2Clcdic.md#std-dtcompatible-nxp-lcdic) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L35) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-board | NXP FlexSPI NOR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/u-blox/ubx_evk_iris_w1/ubx_evk_iris_w1_common.dtsi?plain=1#L111) | [`nxp,imx-flexspi-nor`](../../../../build/dts/api/bindings/mtd/nxp%2Cimx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/u-blox/ubx_evk_iris_w1/ubx_evk_iris_w1_common.dtsi?plain=1#L120) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-board | AP Memory APS6404L pSRAM on NXP FlexSPI bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/u-blox/ubx_evk_iris_w1/ubx_evk_iris_w1_common.dtsi?plain=1#L151) | [`nxp,imx-flexspi-aps6404l`](../../../../build/dts/api/bindings/mtd/nxp%2Cimx-flexspi-aps6404l.md#std-dtcompatible-nxp-imx-flexspi-aps6404l) |
| Pin control | on-chip | MCI IO MUX Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L152) | [`nxp,mci-io-mux`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cmci-io-mux.md#std-dtcompatible-nxp-mci-io-mux) |
| Power management | on-chip | NXP RW PMU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L177) | [`nxp,rw-pmu`](../../../../build/dts/api/bindings/power/nxp%2Crw-pmu.md#std-dtcompatible-nxp-rw-pmu) |
| on-chip | Some NXP SoC’s have pins dedicated to generate a wakeup interrupt[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L180) | [`nxp,aon-wakeup-pin`](../../../../build/dts/api/bindings/power/nxp%2Caon-wakeup-pin.md#std-dtcompatible-nxp-aon-wakeup-pin) |
| on-chip | Properties for NXP power management through the PDCFG register[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L50)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L62) | [`nxp,pdcfg-power`](../../../../build/dts/api/bindings/power/nxp%2Cpdcfg-power.md#std-dtcompatible-nxp-pdcfg-power) |
| Power domain | on-chip | This power domain will Turn On and Off devices when transitioning in and out a specified Power State[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L86) | [`power-domain-soc-state-change`](../../../../build/dts/api/bindings/power-domain/power-domain-soc-state-change.md#std-dtcompatible-power-domain-soc-state-change) |
| PWM | on-chip | NXP SCTimer PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L431) | [`nxp,sctimer-pwm`](../../../../build/dts/api/bindings/pwm/nxp%2Csctimer-pwm.md#std-dtcompatible-nxp-sctimer-pwm) |
| Reset controller | on-chip | NXP RSTCTL Peripheral reset controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L165) | [`nxp,rstctl`](../../../../build/dts/api/bindings/reset/nxp%2Crstctl.md#std-dtcompatible-nxp-rstctl) |
| RNG | on-chip | Kinetis TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L192) | [`nxp,kinetis-trng`](../../../../build/dts/api/bindings/rng/nxp%2Ckinetis-trng.md#std-dtcompatible-nxp-kinetis-trng) |
| RTC | on-chip | NXP LPC RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L368) | [`nxp,lpc-rtc`](../../../../build/dts/api/bindings/rtc/nxp%2Clpc-rtc.md#std-dtcompatible-nxp-lpc-rtc) |
| Serial controller | on-chip | LPC USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L286)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L244) | [`nxp,lpc-usart`](../../../../build/dts/api/bindings/serial/nxp%2Clpc-usart.md#std-dtcompatible-nxp-lpc-usart) |
| SPI | on-chip | NXP FlexSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L141) | [`nxp,imx-flexspi`](../../../../build/dts/api/bindings/spi/nxp%2Cimx-flexspi.md#std-dtcompatible-nxp-imx-flexspi) |
| on-chip | NXP LPC SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L258) | [`nxp,lpc-spi`](../../../../build/dts/api/bindings/spi/nxp%2Clpc-spi.md#std-dtcompatible-nxp-lpc-spi) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L102) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | NXP OS Timer on i.MX-RT5xx/6xx[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L578) | [`nxp,os-timer`](../../../../build/dts/api/bindings/timer/nxp%2Cos-timer.md#std-dtcompatible-nxp-os-timer) |
| USB | on-chip | NXP EHCI USB device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L234) | [`nxp,ehci`](../../../../build/dts/api/bindings/usb/nxp%2Cehci.md#std-dtcompatible-nxp-ehci) |
| Watchdog | on-chip | LPC Windowed Watchdog Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L200) | [`nxp,lpc-wwdt`](../../../../build/dts/api/bindings/watchdog/nxp%2Clpc-wwdt.md#std-dtcompatible-nxp-lpc-wwdt) |
| Wi-Fi | on-chip | NXP Wi-Fi Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L338) | [`nxp,wifi`](../../../../build/dts/api/bindings/wifi/nxp%2Cwifi.md#std-dtcompatible-nxp-wifi) |

Basic functionality like UART (default on FC3), GPIOs (I²C, SPI), and the on-board RGB LEDs is supported.

## Programming and Debugging

The `ubx_evk_iris_w1` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **debugserver** | **rtt** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |
| **[linkserver](../../../../develop/flash_debug/host-tools.md#runner-linkserver)** | ✅ | ✅ | ✅ | ✅ |  |

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the J-Link firmware.

### Configuring a Console

Connect a USB cable from your PC to USB3, and use the serial terminal of your choice
(minicom, PuTTY, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the `hello_world` application.

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```shell
**** Booting Zephyr OS build v4.1.0-2794-g6463c68bc394 ****
     Hello World ! ubx_evk_iris_w1/rw612
```

## Wireless Connectivity Support

### Fetch Binary Blobs

To support Bluetooth or Wi-Fi, `ubx_evk_iris_w1` requires fetching binary blobs. This can be
achieved by running the following command:

```shell
west blobs fetch hal_nxp
```

### Bluetooth

BLE functionality requires fetching binary blobs, so make sure to follow
the “Fetch Binary Blobs” section first.

The required binary blob
`<zephyr workspace>/modules/hal/nxp/zephyr/blobs/rw61x_sb_ble_a2.bin` will be linked
with the application image directly, forming a single monolithic image.

### Wi-Fi

Wi-Fi functionality also requires fetching binary blobs, so make sure to follow
the “Fetch Binary Blobs” section first.

The required binary blob
`<zephyr workspace>/modules/hal/nxp/zephyr/blobs/rw61x_sb_wifi_a2.bin` will be linked
with the application image directly, forming a single monolithic image.

## Resources

- [EVK-IRIS-W1 Website](https://www.u-blox.com/en/product/evk-iris-w1)
- [EVK-IRIS-W1 GitHub](https://github.com/u-blox/u-blox-sho-OpenCPU/tree/master/MCUXpresso/IRIS-W1)
- [EVK-IRIS-W1 User Guide](https://content.u-blox.com/sites/default/files/documents/EVK-IRIS-W1_UserGuide_UBX-23007837.pdf)

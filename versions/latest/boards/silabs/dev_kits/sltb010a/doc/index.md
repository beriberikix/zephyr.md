---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/silabs/dev_kits/sltb010a/doc/index.html
original_path: boards/silabs/dev_kits/sltb010a/doc/index.html
---

# EFR32BG22 Thunderboard (SLTB010A)

Board Overview

[![../../../../../_images/sltb010a.jpg](https://docs.zephyrproject.org/4.2.0/_images/sltb010a.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/sltb010a.jpg)

EFR32BG22 Thunderboard (SLTB010A)

Name:
:   `sltb010a`

Vendor:
:   Silicon Laboratories

Architecture:
:   arm

SoC:
:   efr32bg22c224f512im40

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/dev_kits/sltb010a/doc/index.rst/../..)

SLTB010A is a development kit based on the EFR32BG22 SoC. Early revisions of
the kit (A00 and A01) use a slightly different PCB (BRD4184A) from later
revisions (BRD4184B).

## Hardware

- EFR32BG22 Blue Gecko Wireless SoC with upto 76.8 MHz operating frequency
- ARM® Cortex® M33 core with 32 kB RAM and 512 kB Flash
- Macronix ultra low power 8-Mbit SPI flash (MX25R8035F)
- 2.4 GHz ceramic antenna for wireless transmission
- Silicon Labs Si7021 relative humidity and temperature sensor
- Silicon Labs Si1133 UV index and ambient light sensor (EFR32BG22-BRD4184A)
- Vishay VEML6035 ambient light sensor (EFR32BG22-BRD4184B)
- Silicon Labs Si7210 hall effect sensor
- TDK InvenSense ICM-20648 6-axis inertial sensor
- Two Knowles SPK0641HT4H-1 MEMS microphones with PDM output (EFR32BG22-BRD4184B)
- One LED and one push button
- Power enable signals and isolation switches for ultra low power operation
- On-board SEGGER J-Link debugger for easy programming and debugging, which
  includes a USB virtual COM port and Packet Trace Interface (PTI)
- Mini Simplicity connector for access to energy profiling and advanced wireless
  network debugging
- Breakout pads for GPIO access and connection to external hardware
- Reset button
- Automatic switch-over between USB and battery power
- CR2032 coin cell holder and external battery connector

For more information about the EFR32BG SoC and Thunderboard EFR32BG22 board:

- [EFR32BG22 Website](https://www.silabs.com/wireless/bluetooth/efr32bg22-series-2-socs)
- [EFR32BG22 Datasheet](https://www.silabs.com/documents/public/data-sheets/efr32bg22-datasheet.pdf)
- [EFR32xG22 Reference Manual](https://www.silabs.com/documents/public/reference-manuals/efr32xg22-rm.pdf)
- [Thunderboard EFR32BG22 Website](https://www.silabs.com/development-tools/thunderboard/thunderboard-bg22-kit)
- [EFR32BG22-BRD4184A User Guide](https://www.silabs.com/documents/public/user-guides/ug415-sltb010a-user-guide.pdf)
- [EFR32BG22-BRD4184B User Guide](https://www.silabs.com/documents/public/user-guides/ug464-brd4184b-user-guide.pdf)
- [EFR32BG22-BRD4184A Schematics](https://www.silabs.com/documents/public/schematic-files/BRD4184A-A01-schematic.pdf)
- [EFR32BG22-BRD4184B Schematics](https://www.silabs.com/documents/public/schematic-files/BRD4184B-A02-schematic.pdf)

### Supported Features

The `sltb010a` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `sltb010a@0/efr32bg22c224f512im40` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L113) | [`arm,cortex-m33`](../../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ADC | on-chip | Silicon Labs Series 2 IADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L490) | [`silabs,gecko-iadc`](../../../../../build/dts/api/bindings/adc/silabs%2Cgecko-iadc.md#std-dtcompatible-silabs-gecko-iadc) |
| Bluetooth | on-chip | Silicon Labs Series 2 Bluetooth HCI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/efr32bg22.dtsi?plain=1#L10) | [`silabs,bt-hci-efr32`](../../../../../build/dts/api/bindings/bluetooth/silabs%2Cbt-hci-efr32.md#std-dtcompatible-silabs-bt-hci-efr32) |
| Clock control | on-chip | Silicon Labs Series 2 CMU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L180) | [`silabs,series-clock`](../../../../../build/dts/api/bindings/clock/silabs%2Cseries-clock.md#std-dtcompatible-silabs-series-clock) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L189) | [`fixed-clock`](../../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Silicon Labs Series 2 HFXO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L196) | [`silabs,hfxo`](../../../../../build/dts/api/bindings/clock/silabs%2Chfxo.md#std-dtcompatible-silabs-hfxo) |
| on-chip | Silicon Labs Series 2 LFXO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L208) | [`silabs,series2-lfxo`](../../../../../build/dts/api/bindings/clock/silabs%2Cseries2-lfxo.md#std-dtcompatible-silabs-series2-lfxo) |
| on-chip | Silicon Labs Series 2 HFRCODPLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L219) | [`silabs,series2-hfrcodpll`](../../../../../build/dts/api/bindings/clock/silabs%2Cseries2-hfrcodpll.md#std-dtcompatible-silabs-series2-hfrcodpll) |
| on-chip | Silicon Labs Series 2 LFRCO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L226) | [`silabs,series2-lfrco`](../../../../../build/dts/api/bindings/clock/silabs%2Cseries2-lfrco.md#std-dtcompatible-silabs-series2-lfrco) |
| on-chip | Generic fixed factor clock provider[15 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L23) | [`fixed-factor-clock`](../../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| Debug | on-chip | Silicon Labs Packet Trace Interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/efr32xg22.dtsi?plain=1#L24) | [`silabs,pti`](../../../../../build/dts/api/bindings/debug/silabs%2Cpti.md#std-dtcompatible-silabs-pti) |
| on-chip | ARMv8 instrumentation trace macrocell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L136) | [`arm,armv8m-itm`](../../../../../build/dts/api/bindings/debug/arm%2Carmv8m-itm.md#std-dtcompatible-arm-armv8m-itm) |
| DMA | on-chip | Silicon Labs Series 2 LDMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L458) | [`silabs,ldma`](../../../../../build/dts/api/bindings/dma/silabs%2Cldma.md#std-dtcompatible-silabs-ldma) |
| Flash controller | on-chip | Silicon Labs Series 2 MSC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L240) | [`silabs,series2-flash-controller`](../../../../../build/dts/api/bindings/flash_controller/silabs%2Cseries2-flash-controller.md#std-dtcompatible-silabs-series2-flash-controller) |
| GPIO & Headers | on-chip | Silicon Labs Series 0-2 GPIO Peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L402) | [`silabs,gecko-gpio`](../../../../../build/dts/api/bindings/gpio/silabs%2Cgecko-gpio.md#std-dtcompatible-silabs-gecko-gpio) |
| on-chip | Silicon Labs Series 0-2 GPIO Port[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L412)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L436) | [`silabs,gecko-gpio-port`](../../../../../build/dts/api/bindings/gpio/silabs%2Cgecko-gpio-port.md#std-dtcompatible-silabs-gecko-gpio-port) |
| I2C | on-chip | Silicon Labs Series 0-2 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L380)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L391) | [`silabs,gecko-i2c`](../../../../../build/dts/api/bindings/i2c/silabs%2Cgecko-i2c.md#std-dtcompatible-silabs-gecko-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sltb010a/thunderboard.dtsi?plain=1#L28) | [`gpio-keys`](../../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sltb010a/thunderboard.dtsi?plain=1#L19) | [`gpio-leds`](../../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Miscellaneous | on-board | GPIO Wake Up Trigger for EFR32BG22/EFR32BG27[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sltb010a/thunderboard.dtsi?plain=1#L38) | `silabs,gecko-wake-up-trigger` |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L247) | [`soc-nv-flash`](../../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sltb010a/thunderboard.dtsi?plain=1#L114) | [`fixed-partitions`](../../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-board | Properties supporting Zephyr spi-nor flash driver (over the Zephyr SPI API) control of serial flash memories using the standard M25P80-based command set[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sltb010a/thunderboard.dtsi?plain=1#L87) | [`jedec,spi-nor`](../../../../../build/dts/api/bindings/mtd/jedec%2Cspi-nor.md#std-dtcompatible-jedec-spi-nor) |
| Networking | on-chip | Silicon Labs Series 2 Radio Interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/efr32xg22.dtsi?plain=1#L11) | [`silabs,series2-radio`](../../../../../build/dts/api/bindings/net/wireless/silabs%2Cseries2-radio.md#std-dtcompatible-silabs-series2-radio) |
| Pin control | on-chip | Silicon Labs Series 2 DBUS Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L445) | [`silabs,dbus-pinctrl`](../../../../../build/dts/api/bindings/pinctrl/silabs%2Cdbus-pinctrl.md#std-dtcompatible-silabs-dbus-pinctrl) |
| PWM | on-chip | Silicon Labs TIMER PWM[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L263) | [`silabs,timer-pwm`](../../../../../build/dts/api/bindings/pwm/silabs%2Ctimer-pwm.md#std-dtcompatible-silabs-timer-pwm) |
| on-chip | Silicon Labs LETIMER PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L483) | [`silabs,letimer-pwm`](../../../../../build/dts/api/bindings/pwm/silabs%2Cletimer-pwm.md#std-dtcompatible-silabs-letimer-pwm) |
| Regulator | on-chip | Silicon Labs Series 2 DC-DC converter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L499) | [`silabs,series2-dcdc`](../../../../../build/dts/api/bindings/regulator/silabs%2Cseries2-dcdc.md#std-dtcompatible-silabs-series2-dcdc) |
| on-board | Fixed voltage regulators[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sltb010a/thunderboard.dtsi?plain=1#L44) | [`regulator-fixed`](../../../../../build/dts/api/bindings/regulator/regulator-fixed.md#std-dtcompatible-regulator-fixed) |
| RNG | on-chip | GECKO TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L373) | [`silabs,gecko-trng`](../../../../../build/dts/api/bindings/rng/silabs%2Cgecko-trng.md#std-dtcompatible-silabs-gecko-trng) |
| RTC | on-chip | Silicon Labs Series 2 Sleeptimer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L362) | [`silabs,gecko-stimer`](../../../../../build/dts/api/bindings/rtc/silabs%2Cgecko-stimer.md#std-dtcompatible-silabs-gecko-stimer) |
| Sensors | on-board | Si7210 hall effect magnetic position and temperature sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sltb010a/thunderboard.dtsi?plain=1#L151) | [`silabs,si7210`](../../../../../build/dts/api/bindings/sensor/silabs%2Csi7210.md#std-dtcompatible-silabs-si7210) |
| Serial controller | on-chip | Silicon Labs Series 2 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L345) | [`silabs,usart-uart`](../../../../../build/dts/api/bindings/serial/silabs%2Cusart-uart.md#std-dtcompatible-silabs-usart-uart) |
| SPI | on-chip | Silicon Labs Series 2 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L334) | [`silabs,usart-spi`](../../../../../build/dts/api/bindings/spi/silabs%2Cusart-spi.md#std-dtcompatible-silabs-usart-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L175) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | Silicon Labs TIMER[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L254) | [`silabs,series2-timer`](../../../../../build/dts/api/bindings/timer/silabs%2Cseries2-timer.md#std-dtcompatible-silabs-series2-timer) |
| on-chip | Silicon Labs Series 2 BURTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L354) | [`silabs,gecko-burtc`](../../../../../build/dts/api/bindings/timer/silabs%2Cgecko-burtc.md#std-dtcompatible-silabs-gecko-burtc) |
| on-chip | Silicon Labs LETIMER[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L476) | [`silabs,series2-letimer`](../../../../../build/dts/api/bindings/timer/silabs%2Cseries2-letimer.md#std-dtcompatible-silabs-series2-letimer) |
| Watchdog | on-chip | Silicon Labs Series 1-2 WDOG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L467) | [`silabs,gecko-wdog`](../../../../../build/dts/api/bindings/watchdog/silabs%2Cgecko-wdog.md#std-dtcompatible-silabs-gecko-wdog) |

#### `sltb010a@2/efr32bg22c224f512im40` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L113) | [`arm,cortex-m33`](../../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ADC | on-chip | Silicon Labs Series 2 IADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L490) | [`silabs,gecko-iadc`](../../../../../build/dts/api/bindings/adc/silabs%2Cgecko-iadc.md#std-dtcompatible-silabs-gecko-iadc) |
| Bluetooth | on-chip | Silicon Labs Series 2 Bluetooth HCI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/efr32bg22.dtsi?plain=1#L10) | [`silabs,bt-hci-efr32`](../../../../../build/dts/api/bindings/bluetooth/silabs%2Cbt-hci-efr32.md#std-dtcompatible-silabs-bt-hci-efr32) |
| Clock control | on-chip | Silicon Labs Series 2 CMU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L180) | [`silabs,series-clock`](../../../../../build/dts/api/bindings/clock/silabs%2Cseries-clock.md#std-dtcompatible-silabs-series-clock) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L189) | [`fixed-clock`](../../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Silicon Labs Series 2 HFXO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L196) | [`silabs,hfxo`](../../../../../build/dts/api/bindings/clock/silabs%2Chfxo.md#std-dtcompatible-silabs-hfxo) |
| on-chip | Silicon Labs Series 2 LFXO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L208) | [`silabs,series2-lfxo`](../../../../../build/dts/api/bindings/clock/silabs%2Cseries2-lfxo.md#std-dtcompatible-silabs-series2-lfxo) |
| on-chip | Silicon Labs Series 2 HFRCODPLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L219) | [`silabs,series2-hfrcodpll`](../../../../../build/dts/api/bindings/clock/silabs%2Cseries2-hfrcodpll.md#std-dtcompatible-silabs-series2-hfrcodpll) |
| on-chip | Silicon Labs Series 2 LFRCO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L226) | [`silabs,series2-lfrco`](../../../../../build/dts/api/bindings/clock/silabs%2Cseries2-lfrco.md#std-dtcompatible-silabs-series2-lfrco) |
| on-chip | Generic fixed factor clock provider[15 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L23) | [`fixed-factor-clock`](../../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| Debug | on-chip | Silicon Labs Packet Trace Interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/efr32xg22.dtsi?plain=1#L24) | [`silabs,pti`](../../../../../build/dts/api/bindings/debug/silabs%2Cpti.md#std-dtcompatible-silabs-pti) |
| on-chip | ARMv8 instrumentation trace macrocell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L136) | [`arm,armv8m-itm`](../../../../../build/dts/api/bindings/debug/arm%2Carmv8m-itm.md#std-dtcompatible-arm-armv8m-itm) |
| DMA | on-chip | Silicon Labs Series 2 LDMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L458) | [`silabs,ldma`](../../../../../build/dts/api/bindings/dma/silabs%2Cldma.md#std-dtcompatible-silabs-ldma) |
| Flash controller | on-chip | Silicon Labs Series 2 MSC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L240) | [`silabs,series2-flash-controller`](../../../../../build/dts/api/bindings/flash_controller/silabs%2Cseries2-flash-controller.md#std-dtcompatible-silabs-series2-flash-controller) |
| GPIO & Headers | on-chip | Silicon Labs Series 0-2 GPIO Peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L402) | [`silabs,gecko-gpio`](../../../../../build/dts/api/bindings/gpio/silabs%2Cgecko-gpio.md#std-dtcompatible-silabs-gecko-gpio) |
| on-chip | Silicon Labs Series 0-2 GPIO Port[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L412)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L436) | [`silabs,gecko-gpio-port`](../../../../../build/dts/api/bindings/gpio/silabs%2Cgecko-gpio-port.md#std-dtcompatible-silabs-gecko-gpio-port) |
| I2C | on-chip | Silicon Labs Series 0-2 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L380)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L391) | [`silabs,gecko-i2c`](../../../../../build/dts/api/bindings/i2c/silabs%2Cgecko-i2c.md#std-dtcompatible-silabs-gecko-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sltb010a/thunderboard.dtsi?plain=1#L28) | [`gpio-keys`](../../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sltb010a/thunderboard.dtsi?plain=1#L19) | [`gpio-leds`](../../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Miscellaneous | on-board | GPIO Wake Up Trigger for EFR32BG22/EFR32BG27[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sltb010a/thunderboard.dtsi?plain=1#L38) | `silabs,gecko-wake-up-trigger` |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L247) | [`soc-nv-flash`](../../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sltb010a/thunderboard.dtsi?plain=1#L114) | [`fixed-partitions`](../../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-board | Properties supporting Zephyr spi-nor flash driver (over the Zephyr SPI API) control of serial flash memories using the standard M25P80-based command set[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sltb010a/thunderboard.dtsi?plain=1#L87) | [`jedec,spi-nor`](../../../../../build/dts/api/bindings/mtd/jedec%2Cspi-nor.md#std-dtcompatible-jedec-spi-nor) |
| Networking | on-chip | Silicon Labs Series 2 Radio Interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/efr32xg22.dtsi?plain=1#L11) | [`silabs,series2-radio`](../../../../../build/dts/api/bindings/net/wireless/silabs%2Cseries2-radio.md#std-dtcompatible-silabs-series2-radio) |
| Pin control | on-chip | Silicon Labs Series 2 DBUS Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L445) | [`silabs,dbus-pinctrl`](../../../../../build/dts/api/bindings/pinctrl/silabs%2Cdbus-pinctrl.md#std-dtcompatible-silabs-dbus-pinctrl) |
| PWM | on-chip | Silicon Labs TIMER PWM[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L263) | [`silabs,timer-pwm`](../../../../../build/dts/api/bindings/pwm/silabs%2Ctimer-pwm.md#std-dtcompatible-silabs-timer-pwm) |
| on-chip | Silicon Labs LETIMER PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L483) | [`silabs,letimer-pwm`](../../../../../build/dts/api/bindings/pwm/silabs%2Cletimer-pwm.md#std-dtcompatible-silabs-letimer-pwm) |
| Regulator | on-chip | Silicon Labs Series 2 DC-DC converter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L499) | [`silabs,series2-dcdc`](../../../../../build/dts/api/bindings/regulator/silabs%2Cseries2-dcdc.md#std-dtcompatible-silabs-series2-dcdc) |
| on-board | Fixed voltage regulators[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sltb010a/thunderboard.dtsi?plain=1#L44) | [`regulator-fixed`](../../../../../build/dts/api/bindings/regulator/regulator-fixed.md#std-dtcompatible-regulator-fixed) |
| RNG | on-chip | GECKO TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L373) | [`silabs,gecko-trng`](../../../../../build/dts/api/bindings/rng/silabs%2Cgecko-trng.md#std-dtcompatible-silabs-gecko-trng) |
| RTC | on-chip | Silicon Labs Series 2 Sleeptimer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L362) | [`silabs,gecko-stimer`](../../../../../build/dts/api/bindings/rtc/silabs%2Cgecko-stimer.md#std-dtcompatible-silabs-gecko-stimer) |
| Sensors | on-board | Si7210 hall effect magnetic position and temperature sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sltb010a/thunderboard.dtsi?plain=1#L151) | [`silabs,si7210`](../../../../../build/dts/api/bindings/sensor/silabs%2Csi7210.md#std-dtcompatible-silabs-si7210) |
| Serial controller | on-chip | Silicon Labs Series 2 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L345) | [`silabs,usart-uart`](../../../../../build/dts/api/bindings/serial/silabs%2Cusart-uart.md#std-dtcompatible-silabs-usart-uart) |
| SPI | on-chip | Silicon Labs Series 2 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L334) | [`silabs,usart-spi`](../../../../../build/dts/api/bindings/spi/silabs%2Cusart-spi.md#std-dtcompatible-silabs-usart-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L175) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | Silicon Labs TIMER[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L254) | [`silabs,series2-timer`](../../../../../build/dts/api/bindings/timer/silabs%2Cseries2-timer.md#std-dtcompatible-silabs-series2-timer) |
| on-chip | Silicon Labs Series 2 BURTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L354) | [`silabs,gecko-burtc`](../../../../../build/dts/api/bindings/timer/silabs%2Cgecko-burtc.md#std-dtcompatible-silabs-gecko-burtc) |
| on-chip | Silicon Labs LETIMER[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L476) | [`silabs,series2-letimer`](../../../../../build/dts/api/bindings/timer/silabs%2Cseries2-letimer.md#std-dtcompatible-silabs-series2-letimer) |
| Watchdog | on-chip | Silicon Labs Series 1-2 WDOG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg22/xg22.dtsi?plain=1#L467) | [`silabs,gecko-wdog`](../../../../../build/dts/api/bindings/watchdog/silabs%2Cgecko-wdog.md#std-dtcompatible-silabs-gecko-wdog) |

### Connections and IOs

The EFR32BG22 SoC has four gpio controllers (PORTA, PORTB, PORTC and PORTD).

There are two variants of this board, “A” and “B”. Please take a look at your PCB,
to determine which one you have, as the GPIO pin bindings vary between those two.

BRD4184A (SLTB010A revision A00 and A01):

| Pin | Function | Usage |
| --- | --- | --- |
| PB0 | GPIO | LED0 (YELLOW) |
| PB1 | GPIO | SW0 Push Button PB0 |
| PA5 | UART\_TX | UART TX Console VCOM\_TX US1\_TX #1 |
| PA6 | UART\_RX | UART RX Console VCOM\_RX US1\_RX #1 |

BRD4184B (SLTB010A revision A02 and newer):

| Pin | Function | Usage |
| --- | --- | --- |
| PA4 | GPIO | LED0 (YELLOW) |
| PB3 | GPIO | SW0 Push Button PB0 |
| PA5 | UART\_TX | UART TX Console VCOM\_TX US1\_TX #1 |
| PA6 | UART\_RX | UART RX Console VCOM\_RX US1\_RX #1 |

### System Clock

The EFR32BG22 SoC is configured to use the 38.4 MHz external oscillator on the
board.

### Programming and Debugging

The `sltb010a` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

#### Flashing an application

Connect your device to your host computer using the USB port.
The sample application [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") is used for this example.
Build the Zephyr kernel and application, then flash it to the device:

BRD4184A:

```shell
# From the root of the zephyr repository
west build -b sltb010a@0 samples/hello_world
west flash
```

BRD4184B:

```shell
# From the root of the zephyr repository
west build -b sltb010a@2 samples/hello_world
west flash
```

Note

`west flash` requires [SEGGER J-Link software](https://www.segger.com/downloads/jlink) to be installed on you host
computer.

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you should be able to see on the corresponding Serial Port
the following message:

```shell
Hello World! sltb010a
```

### Bluetooth

To use the BLE function, run the command below to retrieve necessary binary
blobs from the SiLabs HAL repository.

```shell
west blobs fetch hal_silabs
```

Then build the Zephyr kernel and a Bluetooth sample with the following
command. The [Observer](../../../../../samples/bluetooth/observer/README.md#bluetooth_observer "Scan for Bluetooth devices nearby and print their information.") sample application is used in
this example.

BRD4184A:

```shell
# From the root of the zephyr repository
west build -b sltb010a@0 samples/bluetooth/observer
```

BRD4184B:

```shell
# From the root of the zephyr repository
west build -b sltb010a@2 samples/bluetooth/observer
```

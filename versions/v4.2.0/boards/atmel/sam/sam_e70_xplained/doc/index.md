---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/atmel/sam/sam_e70_xplained/doc/index.html
original_path: boards/atmel/sam/sam_e70_xplained/doc/index.html
---

# SAM E70(B) Xplained

Board Overview

[![../../../../../_images/sam_e70_xplained.jpg](https://docs.zephyrproject.org/4.2.0/_images/sam_e70_xplained.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/sam_e70_xplained.jpg)

SAM E70(B) Xplained

Name:
:   `sam_e70_xplained`

Vendor:
:   Atmel Corporation

Architecture:
:   arm

SoC:
:   same70q21, same70q21b

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/atmel/sam/sam_e70_xplained/doc/index.rst/../..)

## Overview

The SAM E70 Xplained evaluation kit is a development platform to evaluate the
Atmel SAM E70 series microcontrollers. The current version allows to use both
IC variations ATSAME70Q21A(B).

## Hardware

- ATSAME70Q21A(B) ARM Cortex-M7 Processor
- 12 MHz crystal oscillator
- 32.768 kHz crystal oscillator (not populated)
- AT24MAC402 EEPROM
- IS42S16100E 16 Mb SDRAM
- SD card connector
- Ethernet port
- Micro-AB USB device
- Micro-AB USB debug interface supporting CMSIS-DAP, Virtual COM Port and Data
  Gateway Interface (DGI)
- JTAG interface connector
- One reset and one user pushbutton
- One green user LED

### Supported Features

The `sam_e70_xplained` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `sam_e70_xplained/same70q21` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L30) | [`arm,cortex-m7`](../../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ADC | on-chip | Atmel SAM family AFEC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L217) | [`atmel,sam-afec`](../../../../../build/dts/api/bindings/adc/atmel%2Csam-afec.md#std-dtcompatible-atmel-sam-afec) |
| ARM architecture | on-chip | Atmel SAM SSC (Synchronous Serial Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L56) | [`atmel,sam-ssc`](../../../../../build/dts/api/bindings/arm/atmel%2Csam-ssc.md#std-dtcompatible-atmel-sam-ssc) |
| CAN | on-chip | Specialization of Bosch m\_can CAN FD controller for Atmel SAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L182)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L194) | [`atmel,sam-can`](../../../../../build/dts/api/bindings/can/atmel%2Csam-can.md#std-dtcompatible-atmel-sam-can) |
| Clock control | on-chip | Atmel Power Management Controller (PMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L330) | [`atmel,sam-pmc`](../../../../../build/dts/api/bindings/clock/atmel%2Csam-pmc.md#std-dtcompatible-atmel-sam-pmc) |
| Counter | on-chip | Atmel SAM Timer Counter (TC) node[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L74) | [`atmel,sam-tc`](../../../../../build/dts/api/bindings/counter/atmel%2Csam-tc.md#std-dtcompatible-atmel-sam-tc) |
| DAC | on-chip | Atmel SAM family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L226) | [`atmel,sam-dac`](../../../../../build/dts/api/bindings/dac/atmel%2Csam-dac.md#std-dtcompatible-atmel-sam-dac) |
| DMA | on-chip | Atmel SAM XDMAC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L321) | [`atmel,sam-xdmac`](../../../../../build/dts/api/bindings/dma/atmel%2Csam-xdmac.md#std-dtcompatible-atmel-sam-xdmac) |
| Ethernet | on-chip | Atmel SAM-family GMAC Ethernet[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L235) | [`atmel,sam-gmac`](../../../../../build/dts/api/bindings/ethernet/atmel%2Csam-gmac.md#std-dtcompatible-atmel-sam-gmac) |
| on-board | Generic MII PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam/sam_e70_xplained/sam_e70_xplained-common.dtsi?plain=1#L140) | [`ethernet-phy`](../../../../../build/dts/api/bindings/ethernet/phy/ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| Flash controller | on-chip | Atmel SAM Enhanced Embedded Flash Controller (EEFC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L354) | [`atmel,sam-flash-controller`](../../../../../build/dts/api/bindings/flash_controller/atmel%2Csam-flash-controller.md#std-dtcompatible-atmel-sam-flash-controller) |
| GPIO & Headers | on-chip | SAM GPIO Port[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L377) | [`atmel,sam-gpio`](../../../../../build/dts/api/bindings/gpio/atmel%2Csam-gpio.md#std-dtcompatible-atmel-sam-gpio) |
| Hardware information | on-chip | ATMEL SAM Reset controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L428) | [`atmel,sam-rstc`](../../../../../build/dts/api/bindings/hwinfo/atmel%2Csam-rstc.md#std-dtcompatible-atmel-sam-rstc) |
| I2C | on-chip | Atmel SAM Family I2C (TWIHS)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L125)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L136) | [`atmel,sam-i2c-twihs`](../../../../../build/dts/api/bindings/i2c/atmel%2Csam-i2c-twihs.md#std-dtcompatible-atmel-sam-i2c-twihs) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam/sam_e70_xplained/sam_e70_xplained-common.dtsi?plain=1#L40) | [`gpio-keys`](../../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam/sam_e70_xplained/sam_e70_xplained-common.dtsi?plain=1#L32) | [`gpio-leds`](../../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | Atmel SAM Family MDIO Driver node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L246) | [`atmel,sam-mdio`](../../../../../build/dts/api/bindings/mdio/atmel%2Csam-mdio.md#std-dtcompatible-atmel-sam-mdio) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L37) | [`arm,armv7m-mpu`](../../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-chip | This binding describes the Atmel SAM flash area layout[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L364) | [`atmel,sam-flash`](../../../../../build/dts/api/bindings/mtd/atmel%2Csam-flash.md#std-dtcompatible-atmel-sam-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam/sam_e70_xplained/sam_e70_xplained-common.dtsi?plain=1#L155) | [`fixed-partitions`](../../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Atmel SAM Pinctrl Container[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L371) | [`atmel,sam-pinctrl`](../../../../../build/dts/api/bindings/pinctrl/atmel%2Csam-pinctrl.md#std-dtcompatible-atmel-sam-pinctrl) |
| Power management | on-chip | Atmel SAM SUPC (Supply-Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L435) | [`atmel,sam-supc`](../../../../../build/dts/api/bindings/power/atmel%2Csam-supc.md#std-dtcompatible-atmel-sam-supc) |
| PWM | on-chip | Atmel SAM PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L147)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L282) | [`atmel,sam-pwm`](../../../../../build/dts/api/bindings/pwm/atmel%2Csam-pwm.md#std-dtcompatible-atmel-sam-pwm) |
| RNG | on-chip | Atmel SAM RNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L313) | [`atmel,sam-trng`](../../../../../build/dts/api/bindings/rng/atmel%2Csam-trng.md#std-dtcompatible-atmel-sam-trng) |
| RTC | on-chip | Atmel SAM family RTC device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L450) | [`atmel,sam-rtc`](../../../../../build/dts/api/bindings/rtc/atmel%2Csam-rtc.md#std-dtcompatible-atmel-sam-rtc) |
| SDHC | on-chip | ATMEL (Microchip) SAM HSMCI SD host controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L49) | [`atmel,sam-hsmci`](../../../../../build/dts/api/bindings/sdhc/atmel%2Csam-hsmci.md#std-dtcompatible-atmel-sam-hsmci) |
| Sensors | on-chip | Atmel SAM Timer Counter (TC) QDEC mode[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L85) | [`atmel,sam-tc-qdec`](../../../../../build/dts/api/bindings/sensor/atmel%2Csam-tc-qdec.md#std-dtcompatible-atmel-sam-tc-qdec) |
| Serial controller | on-chip | Atmel SAM family USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L166)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L158) | [`atmel,sam-usart`](../../../../../build/dts/api/bindings/serial/atmel%2Csam-usart.md#std-dtcompatible-atmel-sam-usart) |
| on-chip | SAM family UART[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L338) | [`atmel,sam-uart`](../../../../../build/dts/api/bindings/serial/atmel%2Csam-uart.md#std-dtcompatible-atmel-sam-uart) |
| SPI | on-chip | Atmel SAM SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L64)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L272) | [`atmel,sam-spi`](../../../../../build/dts/api/bindings/spi/atmel%2Csam-spi.md#std-dtcompatible-atmel-sam-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L44) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| USB | on-chip | Atmel SAM Family USB (USBHS) in device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L206) | [`atmel,sam-usbhs`](../../../../../build/dts/api/bindings/usb/atmel%2Csam-usbhs.md#std-dtcompatible-atmel-sam-usbhs) |
| Watchdog | on-chip | ATMEL SAM0 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L442) | [`atmel,sam-watchdog`](../../../../../build/dts/api/bindings/watchdog/atmel%2Csam-watchdog.md#std-dtcompatible-atmel-sam-watchdog) |

#### `sam_e70_xplained/same70q21b` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L30) | [`arm,cortex-m7`](../../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ADC | on-chip | Atmel SAM family AFEC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L217) | [`atmel,sam-afec`](../../../../../build/dts/api/bindings/adc/atmel%2Csam-afec.md#std-dtcompatible-atmel-sam-afec) |
| ARM architecture | on-chip | Atmel SAM SSC (Synchronous Serial Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L56) | [`atmel,sam-ssc`](../../../../../build/dts/api/bindings/arm/atmel%2Csam-ssc.md#std-dtcompatible-atmel-sam-ssc) |
| CAN | on-chip | Specialization of Bosch m\_can CAN FD controller for Atmel SAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L182)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L194) | [`atmel,sam-can`](../../../../../build/dts/api/bindings/can/atmel%2Csam-can.md#std-dtcompatible-atmel-sam-can) |
| Clock control | on-chip | Atmel Power Management Controller (PMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L330) | [`atmel,sam-pmc`](../../../../../build/dts/api/bindings/clock/atmel%2Csam-pmc.md#std-dtcompatible-atmel-sam-pmc) |
| Counter | on-chip | Atmel SAM Timer Counter (TC) node[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L74) | [`atmel,sam-tc`](../../../../../build/dts/api/bindings/counter/atmel%2Csam-tc.md#std-dtcompatible-atmel-sam-tc) |
| DAC | on-chip | Atmel SAM family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L226) | [`atmel,sam-dac`](../../../../../build/dts/api/bindings/dac/atmel%2Csam-dac.md#std-dtcompatible-atmel-sam-dac) |
| DMA | on-chip | Atmel SAM XDMAC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L321) | [`atmel,sam-xdmac`](../../../../../build/dts/api/bindings/dma/atmel%2Csam-xdmac.md#std-dtcompatible-atmel-sam-xdmac) |
| Ethernet | on-chip | Atmel SAM-family GMAC Ethernet[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L235) | [`atmel,sam-gmac`](../../../../../build/dts/api/bindings/ethernet/atmel%2Csam-gmac.md#std-dtcompatible-atmel-sam-gmac) |
| on-board | Generic MII PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam/sam_e70_xplained/sam_e70_xplained-common.dtsi?plain=1#L140) | [`ethernet-phy`](../../../../../build/dts/api/bindings/ethernet/phy/ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| Flash controller | on-chip | Atmel SAM Enhanced Embedded Flash Controller (EEFC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L354) | [`atmel,sam-flash-controller`](../../../../../build/dts/api/bindings/flash_controller/atmel%2Csam-flash-controller.md#std-dtcompatible-atmel-sam-flash-controller) |
| GPIO & Headers | on-chip | SAM GPIO Port[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L377) | [`atmel,sam-gpio`](../../../../../build/dts/api/bindings/gpio/atmel%2Csam-gpio.md#std-dtcompatible-atmel-sam-gpio) |
| Hardware information | on-chip | ATMEL SAM Reset controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L428) | [`atmel,sam-rstc`](../../../../../build/dts/api/bindings/hwinfo/atmel%2Csam-rstc.md#std-dtcompatible-atmel-sam-rstc) |
| I2C | on-chip | Atmel SAM Family I2C (TWIHS)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L125)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L136) | [`atmel,sam-i2c-twihs`](../../../../../build/dts/api/bindings/i2c/atmel%2Csam-i2c-twihs.md#std-dtcompatible-atmel-sam-i2c-twihs) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam/sam_e70_xplained/sam_e70_xplained-common.dtsi?plain=1#L40) | [`gpio-keys`](../../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam/sam_e70_xplained/sam_e70_xplained-common.dtsi?plain=1#L32) | [`gpio-leds`](../../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | Atmel SAM Family MDIO Driver node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L246) | [`atmel,sam-mdio`](../../../../../build/dts/api/bindings/mdio/atmel%2Csam-mdio.md#std-dtcompatible-atmel-sam-mdio) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L37) | [`arm,armv7m-mpu`](../../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-chip | This binding describes the Atmel SAM flash area layout[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L364) | [`atmel,sam-flash`](../../../../../build/dts/api/bindings/mtd/atmel%2Csam-flash.md#std-dtcompatible-atmel-sam-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam/sam_e70_xplained/sam_e70_xplained-common.dtsi?plain=1#L155) | [`fixed-partitions`](../../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Atmel SAM Pinctrl Container[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L371) | [`atmel,sam-pinctrl`](../../../../../build/dts/api/bindings/pinctrl/atmel%2Csam-pinctrl.md#std-dtcompatible-atmel-sam-pinctrl) |
| Power management | on-chip | Atmel SAM SUPC (Supply-Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L435) | [`atmel,sam-supc`](../../../../../build/dts/api/bindings/power/atmel%2Csam-supc.md#std-dtcompatible-atmel-sam-supc) |
| PWM | on-chip | Atmel SAM PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L147)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L282) | [`atmel,sam-pwm`](../../../../../build/dts/api/bindings/pwm/atmel%2Csam-pwm.md#std-dtcompatible-atmel-sam-pwm) |
| RNG | on-chip | Atmel SAM RNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L313) | [`atmel,sam-trng`](../../../../../build/dts/api/bindings/rng/atmel%2Csam-trng.md#std-dtcompatible-atmel-sam-trng) |
| RTC | on-chip | Atmel SAM family RTC device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L450) | [`atmel,sam-rtc`](../../../../../build/dts/api/bindings/rtc/atmel%2Csam-rtc.md#std-dtcompatible-atmel-sam-rtc) |
| SDHC | on-chip | ATMEL (Microchip) SAM HSMCI SD host controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L49) | [`atmel,sam-hsmci`](../../../../../build/dts/api/bindings/sdhc/atmel%2Csam-hsmci.md#std-dtcompatible-atmel-sam-hsmci) |
| Sensors | on-chip | Atmel SAM Timer Counter (TC) QDEC mode[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L85) | [`atmel,sam-tc-qdec`](../../../../../build/dts/api/bindings/sensor/atmel%2Csam-tc-qdec.md#std-dtcompatible-atmel-sam-tc-qdec) |
| Serial controller | on-chip | Atmel SAM family USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L166)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L158) | [`atmel,sam-usart`](../../../../../build/dts/api/bindings/serial/atmel%2Csam-usart.md#std-dtcompatible-atmel-sam-usart) |
| on-chip | SAM family UART[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L338) | [`atmel,sam-uart`](../../../../../build/dts/api/bindings/serial/atmel%2Csam-uart.md#std-dtcompatible-atmel-sam-uart) |
| SPI | on-chip | Atmel SAM SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L64)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L272) | [`atmel,sam-spi`](../../../../../build/dts/api/bindings/spi/atmel%2Csam-spi.md#std-dtcompatible-atmel-sam-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L44) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| USB | on-chip | Atmel SAM Family USB (USBHS) in device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L206) | [`atmel,sam-usbhs`](../../../../../build/dts/api/bindings/usb/atmel%2Csam-usbhs.md#std-dtcompatible-atmel-sam-usbhs) |
| Watchdog | on-chip | ATMEL SAM0 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samx7x.dtsi?plain=1#L442) | [`atmel,sam-watchdog`](../../../../../build/dts/api/bindings/watchdog/atmel%2Csam-watchdog.md#std-dtcompatible-atmel-sam-watchdog) |

### Connections and IOs

The [SAME70-XPLD User Guide](http://www.atmel.com/Images/Atmel-44050-Cortex-M7-Microcontroller-SAM-E70-XPLD-Xplained_User-guide.pdf) has detailed information about board connections.

### System Clock

The SAM E70 MCU is configured to use the 12 MHz external oscillator on the board
with the on-chip PLL to generate a 300 MHz system clock.

### Serial Port

The ATSAME70Q21 MCU has five UARTs and three USARTs. One of the USARTs is
configured for the console and is available as a Virtual COM Port via EDBG USB
chip.

## Programming and Debugging

The `sam_e70_xplained` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Flashing the Zephyr project onto SAM E70 MCU requires the [OpenOCD tool](http://openocd.org/).
Support for Atmel SAM E microcontroller series was added in OpenOCD release
0.10.0, which was added in Zephyr SDK 0.9.2.

By default a factory new SAM E70 chip will boot SAM-BA boot loader located in
the ROM, not the flashed image. This is determined by the value of GPNVM1
(General-Purpose NVM bit 1). The flash procedure will ensure that GPNVM1 is
set to 1 changing the default behavior to boot from Flash.

If your chip has a security bit GPNVM0 set you will be unable to program flash
memory or connect to it via a debug interface. The only way to clear GPNVM0
is to perform a chip erase procedure that will erase all GPNVM bits and the full
contents of the SAM E70 flash memory:

- With the board power off, set a jumper on the J200 header.
- Turn the board power on. The jumper can be removed soon after the power is on
  (flash erasing procedure is started when the erase line is asserted for at
  least 230ms)

### Flashing

1. Run your favorite terminal program to listen for output. Under Linux the
   terminal should be `/dev/ttyACM0`. For example:

   ```shell
   $ minicom -D /dev/ttyACM0 -o
   ```

   The -o option tells minicom not to send the modem initialization
   string. Connection should be configured as follows:

   - Speed: 115200
   - Data: 8 bits
   - Parity: None
   - Stop bits: 1
2. Connect the SAM E70 Xplained board to your host computer using the
   USB debug port. Then build and flash the [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
   application.

   ```shell
   # From the root of the zephyr repository
   west build -b sam_e70_xplained/same70q21 samples/hello_world
   west flash
   ```

   You should see “Hello World! sam\_e70\_xplained” in your terminal.
3. To use the SoC variation B IC, you need type “sam\_e70\_xplained/same70q21b”.

   ```shell
   # From the root of the zephyr repository
   west build -b sam_e70_xplained/same70q21b samples/hello_world
   west flash
   ```

   You should see “Hello World! sam\_e70\_xplained” in your terminal.

You can flash the image using an external debug adapter such as J-Link
or ULINK, connected to the 20-pin JTAG header. Supply the name of the
debug adapter (e.g., `jlink`) via an OPENOCD\_INTERFACE environment
variable. OpenOCD will look for the appropriate interface
configuration in an `interface/$(OPENOCD_INTERFACE).cfg` file on its
internal search path.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b sam_e70_xplained/same70q21 samples/hello_world
west debug
```

## References

SAM E70 Product Page:
:   [http://www.atmel.com/products/microcontrollers/arm/sam-e.aspx](http://www.atmel.com/products/microcontrollers/arm/sam-e.aspx)

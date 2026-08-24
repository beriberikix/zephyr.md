---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/adi/max32657evkit/doc/index.html
original_path: boards/adi/max32657evkit/doc/index.html
---

# max32657evkit

Board Overview

[![../../../../_images/max32657evkit.webp](https://docs.zephyrproject.org/4.2.0/_images/max32657evkit.webp)
](https://docs.zephyrproject.org/4.2.0/_images/max32657evkit.webp)

max32657evkit

Name:
:   `max32657evkit`

Vendor:
:   Analog Devices, Inc.

Architecture:
:   arm

SoC:
:   max32657

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adi/max32657evkit/doc/index.rst/../..)

## Overview

The MAX32657 microcontroller (MCU) is an advanced system-on-chip (SoC)
featuring an Arm® Cortex®-M33 core with single-precision floating point unit (FPU)
with digital signal processing (DSP) instructions, large flash and SRAM memories,
and the latest generation Bluetooth® 5.4 Low Energy (LE) radio.
The nano-power modes increase battery life substantially.

The MAX32657 is qualified to operate at a temperature range of -20°C to +85°C.
Bluetooth 5.4 LE radio supports Mesh, long-range (coded), and high-throughput modes.
A cryptographic toolbox (CTB) provides advanced root of trust security features,
including an Advanced Encryption Standard (AES) Engine, TRNG, and secure boot.
TrustZone is also included in the M33 Core.
Many high-speed interfaces are supported on the device, including multiple SPI, UART,
and I3C/I2C serial interfaces.
All interfaces support efficient DMA-driven transfers between peripheral and memory.

The Zephyr port is running on the MAX32657 MCU.

## Hardware

- MAX32657 MCU:

  - Arm Cortex-M33 CPU with TrustZone® and FPU
  - 1.2V to 1.6V Input Range for Integrated Boost DC-DC Converter
  - 50MHz Low Power Oscillator
  - External Crystal Support

    - 32MHz required for BLE
  - 1MB Internal Flash with ECC
  - 256kB Internal SRAM
  - 8kB Cache
  - 32.768kHz RTC external crystal
  - Typical Electrical Characteristics

    - ACTIVE: 50μA/MHz Arm Cortex-M33 Running Coremark (50MHz)
  - Bluetooth 5.4 LE Radio

    - Rx Sensitivity: -96dBm; Tx Power: +4.5dBm
    - 15mW Tx Power at 0dBm at 1.5Vin
    - 14mW Rx Power at 1.5Vin
    - Single-Ended Antenna Connection (50Ω)
    - Supports 802.15.4, and LE Audio
    - High-Throughput (2Mbps) Mode
    - Long-Range (125kbps and 500kbps) Modes
  - Optimal Peripheral Mix Provides Platform Scalability

    - 2 DMA Controllers (Secure and non-Secure)
    - One SPI Controller/Peripheral
    - One I2C/I3C
    - 1 Low-Power UART (LPUART)
    - Six 32-Bit Low Power Timers with PWM
    - 14 Configurable GPIO with Internal Pullup/Pulldown Resistors
  - Cryptographic Tool Box (CTB) for IP/Data Security

    - True Random Number Generator (TRNG)
    - AES-128/192/256
    - Unique ID
  - Secure Boot ROM

### Supported Features

The `max32657evkit` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `max32657evkit/max32657` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_common.dtsi?plain=1#L22) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| Clock control | on-chip | MAX32 Global Control[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_common.dtsi?plain=1#L107) | [`adi,max32-gcr`](../../../../build/dts/api/bindings/clock/adi,max32-gcr.md#std-dtcompatible-adi-max32-gcr) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_common.dtsi?plain=1#L36)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_common.dtsi?plain=1#L43) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | ADI MAX32 counter[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_common.dtsi?plain=1#L171) | [`adi,max32-counter`](../../../../build/dts/api/bindings/counter/adi,max32-counter.md#std-dtcompatible-adi-max32-counter) |
| DMA | on-chip | ADI MAX32 DMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657.dtsi?plain=1#L40) | [`adi,max32-dma`](../../../../build/dts/api/bindings/dma/adi,max32-dma.md#std-dtcompatible-adi-max32-dma) |
| Flash controller | on-chip | MAX32XXX flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657.dtsi?plain=1#L24) | [`adi,max32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/adi,max32-flash-controller.md#std-dtcompatible-adi-max32-flash-controller) |
| GPIO & Headers | on-chip | MAX32 GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_common.dtsi?plain=1#L122) | [`adi,max32-gpio`](../../../../build/dts/api/bindings/gpio/adi,max32-gpio.md#std-dtcompatible-adi-max32-gpio) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32657evkit/max32657evkit_max32657_common.dtsi?plain=1#L30) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32657evkit/max32657evkit_max32657_common.dtsi?plain=1#L21) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_common.dtsi?plain=1#L28) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657.dtsi?plain=1#L32) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32657evkit/max32657evkit_max32657.dts?plain=1#L32) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | MAX32 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657.dtsi?plain=1#L20) | [`adi,max32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/adi,max32-pinctrl.md#std-dtcompatible-adi-max32-pinctrl) |
| PWM | on-chip | ADI MAX32 PWM[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_common.dtsi?plain=1#L166) | [`adi,max32-pwm`](../../../../build/dts/api/bindings/pwm/adi,max32-pwm.md#std-dtcompatible-adi-max32-pwm) |
| RNG | on-chip | ADI MAX32XXX TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_common.dtsi?plain=1#L142) | [`adi,max32-trng`](../../../../build/dts/api/bindings/rng/adi,max32-trng.md#std-dtcompatible-adi-max32-trng) |
| Serial controller | on-chip | MAX32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_common.dtsi?plain=1#L133) | [`adi,max32-uart`](../../../../build/dts/api/bindings/serial/adi,max32-uart.md#std-dtcompatible-adi-max32-uart) |
| SPI | on-chip | ADI MAX32 SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_common.dtsi?plain=1#L272) | [`adi,max32-spi`](../../../../build/dts/api/bindings/spi/adi,max32-spi.md#std-dtcompatible-adi-max32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_common.dtsi?plain=1#L77) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | ADI MAX32 timer[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_common.dtsi?plain=1#L158) | [`adi,max32-timer`](../../../../build/dts/api/bindings/timer/adi,max32-timer.md#std-dtcompatible-adi-max32-timer) |
| Watchdog | on-chip | MAX32XXX watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_common.dtsi?plain=1#L149) | [`adi,max32-watchdog`](../../../../build/dts/api/bindings/watchdog/adi,max32-watchdog.md#std-dtcompatible-adi-max32-watchdog) |

#### `max32657evkit/max32657/ns` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_common.dtsi?plain=1#L22) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| Clock control | on-chip | MAX32 Global Control[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_common.dtsi?plain=1#L107) | [`adi,max32-gcr`](../../../../build/dts/api/bindings/clock/adi,max32-gcr.md#std-dtcompatible-adi-max32-gcr) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_common.dtsi?plain=1#L36)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_common.dtsi?plain=1#L43) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | ADI MAX32 counter[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_common.dtsi?plain=1#L171) | [`adi,max32-counter`](../../../../build/dts/api/bindings/counter/adi,max32-counter.md#std-dtcompatible-adi-max32-counter) |
| DMA | on-chip | ADI MAX32 DMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_ns.dtsi?plain=1#L24) | [`adi,max32-dma`](../../../../build/dts/api/bindings/dma/adi,max32-dma.md#std-dtcompatible-adi-max32-dma) |
| Flash controller | on-chip | MAX32XXX flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_ns.dtsi?plain=1#L35) | [`adi,max32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/adi,max32-flash-controller.md#std-dtcompatible-adi-max32-flash-controller) |
| GPIO & Headers | on-chip | MAX32 GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_common.dtsi?plain=1#L122) | [`adi,max32-gpio`](../../../../build/dts/api/bindings/gpio/adi,max32-gpio.md#std-dtcompatible-adi-max32-gpio) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32657evkit/max32657evkit_max32657_common.dtsi?plain=1#L30) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32657evkit/max32657evkit_max32657_common.dtsi?plain=1#L21) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_common.dtsi?plain=1#L28) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_ns.dtsi?plain=1#L43) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32657evkit/max32657evkit_max32657_ns.dts?plain=1#L38) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | MAX32 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_ns.dtsi?plain=1#L20) | [`adi,max32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/adi,max32-pinctrl.md#std-dtcompatible-adi-max32-pinctrl) |
| PWM | on-chip | ADI MAX32 PWM[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_common.dtsi?plain=1#L166) | [`adi,max32-pwm`](../../../../build/dts/api/bindings/pwm/adi,max32-pwm.md#std-dtcompatible-adi-max32-pwm) |
| RNG | on-chip | ADI MAX32XXX TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_common.dtsi?plain=1#L142) | [`adi,max32-trng`](../../../../build/dts/api/bindings/rng/adi,max32-trng.md#std-dtcompatible-adi-max32-trng) |
| Serial controller | on-chip | MAX32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_common.dtsi?plain=1#L133) | [`adi,max32-uart`](../../../../build/dts/api/bindings/serial/adi,max32-uart.md#std-dtcompatible-adi-max32-uart) |
| SPI | on-chip | ADI MAX32 SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_common.dtsi?plain=1#L272) | [`adi,max32-spi`](../../../../build/dts/api/bindings/spi/adi,max32-spi.md#std-dtcompatible-adi-max32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_common.dtsi?plain=1#L77) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | ADI MAX32 timer[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_common.dtsi?plain=1#L158) | [`adi,max32-timer`](../../../../build/dts/api/bindings/timer/adi,max32-timer.md#std-dtcompatible-adi-max32-timer) |
| Watchdog | on-chip | MAX32XXX watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32657_common.dtsi?plain=1#L149) | [`adi,max32-watchdog`](../../../../build/dts/api/bindings/watchdog/adi,max32-watchdog.md#std-dtcompatible-adi-max32-watchdog) |

### Connections and IOs

| Name | Name | Settings | Description |
| --- | --- | --- | --- |
| JP1 | VLDO SEL | | 1-2 | | --- | | 3-4 | | 5-6 | | Open | | | Sets the LDO output used for system power according to the value of resistor R4. | | --- | | Sets the LDO output used for system power to 1.2V. | | Sets the LDO output used for system power to 1.5V. | | Sets the LDO output used for system power to 1.6V. | |
| JP2 | VIN SEL | | 1-2 | | --- | | 2-3 | | | VIN Powered from LDO. (USB Type-C connector is board’s power source) | | --- | | VIN Powered from Battery | |
| JP3 | VIN EN | | 1-2 | | --- | | Open | | | Connects the board’s power source to system power by connecting VIN to VSYS\_IN. | | --- | | Disconnects system power by disconnecting VIN from VSYS\_IN. | |
| JP4 | VDD12 EN | | 1-2 | | --- | | Open | | | Connects system power to the MAX32657 by connecting VDD12 to VSYS\_OUT. | | --- | | Disconnects system power from the MAX32657 by disconnecting VDD12 from VSYS\_OUT. | |
| JP5 | VTREF EN | | 1-2 | | --- | | Open | | | Connects a reference voltage to the OBD circuit. | | --- | | Disconnects a reference voltage from the OBD circuit. | |
| JP6 | OBD VBUS EN | | 1-2 | | --- | | Open | | | Enables the OBD by connecting OBD\_VBUS to VBUS. | | --- | | Disables the OBD by disconnecting OBD\_VBUS from VBUS. | |
| J7 | VSYS EN | | 1-2 | | --- | | Open | | | Connects system power to all peripherals by connecting VSYS to VSYS\_OUT. | | --- | | Disconnects system power to all peripherals by disconnecting VSYS from VSYS\_OUT. | |
| JP7 | ACC VS EN | | 1-2 | | --- | | Open | | | Enables the accelerometer by connecting its supply voltage pin VS to VSYS. | | --- | | Disables the accelerometer by disconnecting its supply voltage pin VS from VSYS. | |
| JP8 | ACC VDD EN | | 1-2 | | --- | | Open | | | Enables the accelerometer by connecting its VDDIO pin to VSYS. | | --- | | Disables the accelerometer by disconnecting its VDDIO pin from VSYS. | |
| JP9 | ACC I2C EN | | 1-2 | | --- | | Open | | | Accelerometer SDA Pin is connected to MAX32657 I2C0\_SDA. | | --- | | Accelerometer SDA Pin is disconnected from MAX32657 I2C0\_SDA. | |
| JP10 | ACC I2C EN | | 1-2 | | --- | | Open | | | Accelerometer SCL Pin is connected to MAX32657 I2C0\_SCL. | | --- | | Accelerometer SCL Pin is disconnected from MAX32657 I2C0\_SCL. | |
| JP11 | BYP MAG SW | | 1-2 | | --- | | Open | | | Bypass Magnetic Switch. | | --- | | Enables magnetic switch. The output of the switch is controlled by the AFE pin. | |
| JP12 | LOCK RSTN | | 1-2 | | --- | | Open | | | AFE Lock Pin is connected to MAX32657 RSTN pin. | | --- | | AFE Lock Pin is disconnected from MAX32657 RSTN pin. | |
| JP13 | LATCH CTRL | | 1-2 | | --- | | 2-3 | | | Connects the AFE (LOCK) to the magnetic switch (OUTPUT LATCH CONTROL). | | --- | | Connects the AFE (WAKE) to the magnetic switch (OUTPUT LATCH CONTROL). | |
| JP14 | AFE EN | | 1-2 | | --- | | Open | | | Enables the AFE (VBAT) by connecting it to VSYS. | | --- | | Disables the AFE (VBAT) by disconnecting it from VSYS. | |
| JP15 | AFE SPI EN | | 1-2 | | --- | | 3-4 | | 5-6 | | 7-8 | | 9-10 | | 11-12 | | Open All | | | AFE CSB is connected to MAX32657 SPI0\_CS0. | | --- | | AFE SDI is connected to MAX32657 SPI0\_MOSI. | | AFE SCLK is connected to MAX32657 SPI0\_SCK. | | AFE SDO is connected to MAX32657 SPI0\_MISO. | | AFE INTB is connected to MAX32657 P0.7. | | AFE GPIO2 is connected to MAX32657 P0.8. | | Disconnect SPI Interface from MAX32657. | |
| JP16 | I2C PU EN | | 1-2 | | --- | | Open | | | Enable SCL PU resistor. | | --- | | Disable SCL PU resistor. | |
| JP17 | I2C PU EN | | 1-2 | | --- | | Open | | | Enable SDA PU resistor. | | --- | | Disable SDA PU resistor. | |
| JP18 | OBD SWD EN | | 3-4 | | --- | | 5-6 | | 7-8 | | 9-10 | | 11-12 | | 13-14 | | Open All | | | OBD SWDIO is connected to the MAX32657 SWDIO. | | --- | | OBD SWCLK is connected to the MAX32657 SWCLK. | | OBD JTAG TDO Enable Jumper (It’s not used on MAX32657). | | OBD JTAG TDI Enable Jumper (It’s not used on MAX32657). | | OBD RSTN is connected to the MAX32657 RSTN. | | OBD JTAG TRST Enable Jumper (It’s not used on MAX32657). | | Disable OBD SWD Connection from MAX32657. | |
| JP19 | OBD VCOM EN | | 3-4 | | --- | | 5-6 | | 7-8 | | 9-10 | | Open | | | OBD VCOM TXD is connected VCOM EN RX Jumper. | | --- | | OBD VCOM RXD is connected VCOM EN TX Jumper. | | OBD VCOM CTS Enable Jumper (It’s not used on MAX32657). | | OBD VCOM RTS Enable Jumper (It’s not used on MAX32657). | | Disable OBD VCOM connection from MAX32657. | |
| JP20 | VCOM EN | | 1-2 | | --- | | Open | | | Connects OBD VCOM RXD to the MAX32657 UART0A\_TX. | | --- | | Disconnects OBD VCOM RXD from the MAX32657 UART0A\_TX. | |
| JP21 | VCOM EN | | 1-2 | | --- | | Open | | | Connects OBD VCOM TXD to the MAX32657 UART0A\_RX. | | --- | | Disconnects OBD VCOM TXD from the MAX32657 UART0A\_RX. | |
| JP22 | EXT SWD EN | | 1-2 | | --- | | Open | | | Connects EXT SWD Connector Data Signals to the MAX32657 SWDIO pin. | | --- | | Disconnects EXT SWD Connector Data Signals from the MAX32657 SWDIO pin. | |
| JP23 | EXT SWD EN | | 1-2 | | --- | | Open | | | Connects EXT SWD Connector Clock Signals to the MAX32657 SWDCLK pin. | | --- | | Disconnects EXT SWD Connector Clock Signals from the MAX32657 SWDCLK pin. | |

## Zephyr board options

The MAX32657 microcontroller (MCU) is an advanced system-on-chip (SoC)
featuring an ARM Cortex-M33 architecture that provides Trustzone technology
which allow define secure and non-secure application.
Zephyr provides support for building for both Secure (S) and Non-Secure (NS) firmware.

The BOARD options are summarized below:

| BOARD | Description |
| --- | --- |
| max32657evkit/max32657 | For building Trust Zone Disabled firmware |
| max32657evkit/max32657/ns | Building with TF-M (includes NS+S images) |

### BOARD: max32657evkit/max32657

Build the zephyr app for `max32657evkit/max32657` board target will generate secure firmware
for zephyr. In this configuration 960KB of flash is used to store the code and 64KB
is used for storage section. In this mode tf-m is off and secure mode flag is on
([`CONFIG_TRUSTED_EXECUTION_SECURE`](../../../../kconfig.md#CONFIG_TRUSTED_EXECUTION_SECURE "CONFIG_TRUSTED_EXECUTION_SECURE") to `y` and
[`CONFIG_BUILD_WITH_TFM`](../../../../kconfig.md#CONFIG_BUILD_WITH_TFM "CONFIG_BUILD_WITH_TFM") to `n`)

| Name | Address[Size] | Comment |
| --- | --- | --- |
| slot0 | 0x1000000[960k] | Secure zephyr image |
| storage | 0x10f0000[64k] | File system, persistent storage |

Here are the instructions to build zephyr with a secure configuration,
using [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample:

```shell
# From the root of the zephyr repository
west build -b max32657evkit/max32657 samples/basic/blinky/
```

### BOARD: max32657evkit/max32657/ns

The `max32657evkit/max32657/ns` board target is used to build the secure firmware
image using TF-M ([`CONFIG_BUILD_WITH_TFM`](../../../../kconfig.md#CONFIG_BUILD_WITH_TFM "CONFIG_BUILD_WITH_TFM") to `y`) and
the non-secure firmware image using Zephyr
([`CONFIG_TRUSTED_EXECUTION_NONSECURE`](../../../../kconfig.md#CONFIG_TRUSTED_EXECUTION_NONSECURE "CONFIG_TRUSTED_EXECUTION_NONSECURE") to `y`).

Here are the instructions to build zephyr with a non-secure configuration,
using [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample:

```shell
# From the root of the zephyr repository
west build -b max32657evkit/max32657/ns samples/basic/blinky/
```

The above command will:
:   - Build a bootloader image (MCUboot)
    - Build a TF-M (secure) firmware image
    - Build Zephyr application as non-secure firmware image
    - Merge them as `tfm_merged.hex` which contain all images.

Note:

Zephyr build TF-M with [`CONFIG_TFM_PROFILE_TYPE_NOT_SET`](../../../../kconfig.md#CONFIG_TFM_PROFILE_TYPE_NOT_SET "CONFIG_TFM_PROFILE_TYPE_NOT_SET") mode
that meet most use case configuration especially for BLE related applications.
if TF-M small profile meet your application requirement you can set TF-M profile as small
[`CONFIG_TFM_PROFILE_TYPE_SMALL`](../../../../kconfig.md#CONFIG_TFM_PROFILE_TYPE_SMALL "CONFIG_TFM_PROFILE_TYPE_SMALL") to `y` to decrease TF-M RAM and flash use.

#### Memory mappings

MAX32657 1MB flash and 256KB RAM split to define section for MCUBoot,
TF-M (S), Zephyr (NS) and storage that used for secure services and configurations.
Default layout of MAX32657 is listed in below table.

| Name | Address[Size] | Comment |
| --- | --- | --- |
| boot | 0x1000000[64K] | MCU Bootloader |
| slot0 | 0x1010000[320k] | Secure image slot0 (TF-M) |
| slot0\_ns | 0x1060000[576k] | Non-secure image slot0 (Zephyr) |
| slot1 | 0x10F0000[0k] | Updates slot0 image |
| slot1\_ns | 0x10F0000[0k] | Updates slot0\_ns image |
| storage | 0x10f0000[64k] | Persistent storage |

| RAM | Address[Size] | Comment |
| --- | --- | --- |
| secure\_ram | 0x20000000[64k] | Secure memory |
| non\_secure\_ram | 0x20010000[192k] | Non-Secure memory |

Flash memory layout are defines both on zephyr board file and [Trusted Firmware M](https://tf-m-user-guide.trustedfirmware.org/building/tfm_build_instruction.html) (TF-M) project
these definition shall be match. Zephyr defines it in
[boards/adi/max32657evkit/max32657evkit\_max32657\_common.dtsi](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32657evkit/max32657evkit_max32657_common.dtsi)
file under flash section. TF-M project define them in
<zephyr\_path>../modules/tee/tf-m/trusted-firmware-m/platform/ext/target/adi/max32657/partition/flash\_layout.h file.`
If you would like to update flash region for your application you shall update related section in
these files.

Additionally if firmware update feature requires slot1 and slot1\_ns section need to be
defined. On default the section size set as 0 due to firmware update not requires on default.

#### Peripherals and Memory Ownership

The ARM Security Extensions model allows system developers to partition device hardware and
software resources, so that they exist in either the Secure world for the security subsystem,
or the Normal world for everything else. Correct system design can ensure that no Secure world
assets can be accessed from the Normal world. A Secure design places all sensitive resources
in the Secure world, and ideally has robust software running that can protect assets against
a wide range of possible software attacks ([1](https://developer.arm.com/documentation/100935/0100/The-TrustZone-hardware-architecture-)).

MPC (Memory Protection Controller) and PPC (Peripheral Protection Controller) are allow to
protect memory and peripheral. Incase of need peripheral and flash ownership can be updated in
<zephyr\_path>../modules/tee/tf-m/trusted-firmware-m/platform/ext/target/adi/max32657/s\_ns\_access.cmake`
file by updating cmake flags to ON/OFF.

As an example for below configuration TRNG, SRAM\_0 and SRAM\_1 is not going to be accessible
by non-secure. All others is going to be accessible by NS world.

```text
set(ADI_NS_PRPH_GCR         ON         CACHE BOOL "")
set(ADI_NS_PRPH_SIR         ON         CACHE BOOL "")
set(ADI_NS_PRPH_FCR         ON         CACHE BOOL "")
set(ADI_NS_PRPH_WDT         ON         CACHE BOOL "")
set(ADI_NS_PRPH_AES         OFF        CACHE BOOL "")
set(ADI_NS_PRPH_AESKEY      OFF        CACHE BOOL "")
set(ADI_NS_PRPH_CRC         ON         CACHE BOOL "")
set(ADI_NS_PRPH_GPIO0       ON         CACHE BOOL "")
set(ADI_NS_PRPH_TIMER0      ON         CACHE BOOL "")
set(ADI_NS_PRPH_TIMER1      ON         CACHE BOOL "")
set(ADI_NS_PRPH_TIMER2      ON         CACHE BOOL "")
set(ADI_NS_PRPH_TIMER3      ON         CACHE BOOL "")
set(ADI_NS_PRPH_TIMER4      ON         CACHE BOOL "")
set(ADI_NS_PRPH_TIMER5      ON         CACHE BOOL "")
set(ADI_NS_PRPH_I3C         ON         CACHE BOOL "")
set(ADI_NS_PRPH_UART        ON         CACHE BOOL "")
set(ADI_NS_PRPH_SPI         ON         CACHE BOOL "")
set(ADI_NS_PRPH_TRNG        OFF        CACHE BOOL "")
set(ADI_NS_PRPH_BTLE_DBB    ON         CACHE BOOL "")
set(ADI_NS_PRPH_BTLE_RFFE   ON         CACHE BOOL "")
set(ADI_NS_PRPH_RSTZ        ON         CACHE BOOL "")
set(ADI_NS_PRPH_BOOST       ON         CACHE BOOL "")
set(ADI_NS_PRPH_BBSIR       ON         CACHE BOOL "")
set(ADI_NS_PRPH_BBFCR       ON         CACHE BOOL "")
set(ADI_NS_PRPH_RTC         ON         CACHE BOOL "")
set(ADI_NS_PRPH_WUT0        ON         CACHE BOOL "")
set(ADI_NS_PRPH_WUT1        ON         CACHE BOOL "")
set(ADI_NS_PRPH_PWR         ON         CACHE BOOL "")
set(ADI_NS_PRPH_MCR         ON         CACHE BOOL "")

# SRAMs
set(ADI_NS_SRAM_0           OFF        CACHE BOOL "Size: 32KB")
set(ADI_NS_SRAM_1           OFF        CACHE BOOL "Size: 32KB")
set(ADI_NS_SRAM_2           ON         CACHE BOOL "Size: 64KB")
set(ADI_NS_SRAM_3           ON         CACHE BOOL "Size: 64KB")
set(ADI_NS_SRAM_4           ON         CACHE BOOL "Size: 64KB")

# Ramfuncs section size
set(ADI_S_RAM_CODE_SIZE     "0x800"    CACHE STRING "Default: 2KB")

# Flash: BL2, TFM and Zephyr are contiguous sections.
set(ADI_FLASH_AREA_BL2_SIZE        "0x10000"  CACHE STRING "Default: 64KB")
set(ADI_FLASH_S_PARTITION_SIZE     "0x50000"  CACHE STRING "Default: 320KB")
set(ADI_FLASH_NS_PARTITION_SIZE    "0x90000"  CACHE STRING "Default: 576KB")
set(ADI_FLASH_PS_AREA_SIZE         "0x4000"   CACHE STRING "Default: 16KB")
set(ADI_FLASH_ITS_AREA_SIZE        "0x4000"   CACHE STRING "Default: 16KB")

#
# Allow user set S-NS resources ownership by overlay file
#
if(EXISTS "${CMAKE_BINARY_DIR}/../../s_ns_access_overlay.cmake")
  include(${CMAKE_BINARY_DIR}/../../s_ns_access_overlay.cmake)
endif()
```

As an alternative method (which recommended) user can configurate ownership peripheral by
an cmake overlay file too without touching TF-M source files. For this path
create `s_ns_access_overlay.cmake` file under your project root folder and put peripheral/memory
you would like to be accessible by secure world.

As an example if below configuration files been put in the `s_ns_access_overlay.cmake` file
TRNG, SRAM\_0 and SRAM\_1 will be accessible by secure world only.

```text
set(ADI_NS_PRPH_TRNG        OFF        CACHE BOOL "")
set(ADI_NS_SRAM_0           OFF        CACHE BOOL "Size: 32KB")
set(ADI_NS_SRAM_1           OFF        CACHE BOOL "Size: 32KB")
```

## Programming and Debugging

The `max32657evkit` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application. This example uses the
[J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) as default.

```shell
# From the root of the zephyr repository
west build -b max32657evkit/max32657 samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS build v4.1.0 *****
Hello World! max32657evkit/max32657
```

#### Building and flashing secure/non-secure with Arm® TrustZone®

The TF-M integration samples can be run using the
`max32657evkit/max32657/ns` board target. To run we need to manually flash
the resulting image (`tfm_merged.hex`) with a J-Link as follows
(reset and erase are for recovering a locked core):

```shell
# From the root of the zephyr repository
west build -b max32657evkit/max32657/ns samples/hello_world
```

```shell
west flash --hex-file build/zephyr/tfm_merged.hex
```

```shell
[INF] Starting bootloader
[WRN] This device was provisioned with dummy keys. This device is NOT SECURE
[INF] PSA Crypto init done, sig_type: RSA-3072
[WRN] Cannot upgrade: slots have non-compatible sectors
[WRN] Cannot upgrade: slots have non-compatible sectors
[INF] Bootloader chainload address offset: 0x10000
[INF] Jumping to the first image slot
***** Booting Zephyr OS build v4.1.0 *****
Hello World! max32657evkit/max32657/ns
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application. This example uses the
[J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) as default.

```shell
# From the root of the zephyr repository
west build -b max32657evkit/max32657 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS build v4.1.0 *****
Hello World! max32657evkit/max32657
```

## References

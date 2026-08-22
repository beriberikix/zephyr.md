---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/st/stm32wb5mmg/doc/stm32wb5mmg.html
original_path: boards/st/stm32wb5mmg/doc/stm32wb5mmg.html
---

# STM32WB5MMG

Board Overview

[![../../../../_images/STM32WB5MMG.jpg](../../../../_images/STM32WB5MMG.jpg)
](../../../../_images/STM32WB5MMG.jpg)

STM32WB5MMG

Name:
:   `stm32wb5mmg`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32wb55xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm32wb5mmg/doc/stm32wb5mmg.rst/../..)

## Overview

STM32WB5MMG is an ultra-low-power and small form factor certified 2.4 GHz
wireless module. It supports Bluetooth|reg| Low Energy 5.4, Zigbee|reg| 3.0,
OpenThread, dynamic, and static concurrent modes, and 802.15.4 proprietary
protocols. This board support is added in order to make it possible use this
module on other boards as HCI layer (Specefically B-U585I-IOT02A Development board).

STM32WB5MMG supports the following features:

- Bluetooth module in SiP-LGA86 package
- Integrated chip antenna
- Bluetooth|reg| Low Energy 5.4, Zigbee|reg| 3.0, OpenThread certified
  Dynamic and static concurrent modes
- IEEE 802.15.4-2011 MAC PHY Supports 2 Mbits/s
- Frequency band 2402-2480 MHz
- Advertising extension
- Tx output power up to +6 dBm
- Rx sensitivity: -96 dBm (Bluetooth|reg| Low Energy at 1 Mbps), -100 dBm (802.15.4)
- Range: up to 75 meters
- Dedicated Arm|reg| Cortex|reg|-M0+ CPU for radio and security tasks
- Dedicated Arm|reg| Cortex|reg|-M4 CPU with FPU and ART (adaptive real-time accelerator) up to 64 MHz speed
- 1-Mbyte flash memory, 256-Kbyte SRAM
- Fully integrated BOM, including 32 MHz radio and 32 kHz RTC crystals
- Integrated SMPS
- Ultra-low-power modes for battery longevity
- 68 GPIOs
- SWD, JTAG

More information about the board can be found at the `` [STM32WB5MMG on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32wb5mmg.html).

## Hardware

STM32WB5MMG is an ultra-low-power and small form factor certified 2.4 GHz
wireless module. It supportsBluetooth|reg| Low Energy 5.4, Zigbee|reg| 3.0, OpenThread,
dynamic, and static concurrent modes, and 802.15.4proprietary protocols. Based
on the STMicroelectronics STM32WB55VGY wireless microcontroller,STM32WB5MMG
provides best-in-class RF performance thanks to its high receiver sensitivity
and output power signal. Its low-power features enable extended battery life,
small coin-cell batteries, and energy harvesting. STM32WB5MMG revision Y is
based on cut 2.1 of the STM32WB55VGY microcontroller. Revision X is based on
cut 2.2.

- Ultra-low-power with FlexPowerControl (down to 600 nA Standby mode with RTC and 32KB RAM)
- Core: ARM® 32-bit Cortex®-M4 CPU with FPU, frequency up to 64 MHz
- Radio:

  - 2.4GHz
  - RF transceiver supporting Bluetooth|reg| 5.4
    specification, IEEE 802.15.4-2011 PHY
    and MAC, supporting Thread 1.3 and
  - Zigbee|reg| 3.0
  - RX sensitivity: -96 dBm (Bluetooth® Low
    Energy at 1 Mbps), -100 dBm (802.15.4)
  - Programmable output power up to +6 dBm
    with 1 dB steps
  - Integrated balun to reduce BOM
  - Support for 2 Mbps
  - Support GATT caching
  - Support EATT (enhanced ATT)
  - Support advertising extension
  - Dedicated Arm|reg| 32-bit Cortex|reg| M0+ CPU
    for real-time Radio layer
  - Accurate RSSI to enable power control
  - Suitable for systems requiring compliance
    with radio frequency regulations ETSI EN
    300 328, EN 300 440, FCC CFR47 Part 15
    and ARIB STD-T66
- Clock Sources:

  - 32 MHz crystal oscillator with integrated
    trimming capacitors (Radio and CPU clock)
  - 32 kHz crystal oscillator for RTC (LSE)
  - Internal low-power 32 kHz (±5%) RC (LSI1)
  - Internal low-power 32 kHz (stability
    ±500 ppm) RC (LSI2)
  - Internal multispeed 100 kHz to 48 MHz
    oscillator, auto-trimmed by LSE (better than
    ±0.25% accuracy)
  - High speed internal 16 MHz factory
    trimmed RC (±1%)
  - 2x PLL for system clock, USB, SAI, ADC
- 2x DMA controllers (seven channels each) supporting ADC, SPI, I2C, USART, QSPI, SAI, AES, timers
- 1x USART (ISO 7816, IrDA, SPI master, Modbus and Smartcard mode)
- 1x LPUART (low power)
- Two SPI running at 32 Mbit/s
- 2x I2C (SMBus/PMBus)
- 1x SAI (dual channel high quality audio)
- 1x USB 2.0 FS device, crystal-less, BCD and LPM
- 1x Touch sensing controller, up to 18 sensors
- 1x LCD 8x40 with step-up converter
- 1x 16-bit, four channels advanced timer
- 2x 16-bit, two channels timers
- 1x 32-bit, four channels timer
- 2x 16-bit ultra-low-power timers
- 1x independent Systick
- 1x independent watchdog
- 1x window watchdog
- Up to 72 fast I/Os, 70 of them 5 V-tolerant
- Memories

  - Up to 1 MB flash memory with sector
    protection (PCROP) against R/W
    operations, enabling radio stack and
    application
  - Up to 256 KB SRAM, including 64 KB with
    hardware parity check
  - 20x 32-bit backup register
  - Boot loader supporting USART, SPI, I2C
    and USB interfaces
  - OTA (over the air) Bluetooth® Low Energy
    and 802.15.4 update
  - Quad SPI memory interface with XIP
  - 1 Kbyte (128 double words) OTP
- 4x digital filters for sigma delta modulator
- Rich analog peripherals (down to 1.62 V)
- 12-bit ADC 4.26 Msps, up to 16-bit with
  hardware oversampling, 200 μA/Msps
- 2x ultra-low-power comparator
- Accurate 2.5 V or 2.048 V reference
  voltage buffered output
- Security and ID

> - Secure firmware installation (SFI) for
>   Bluetooth|reg| Low Energy and 802.15.4 SW stack
> - 3x hardware encryption AES maximum 256-bit for
>   the application, the Bluetooth|reg|
> - Low Energy and IEEE802.15.4
> - Customer key storage/manager services
> - HW public key authority (PKA)
> - Cryptographic algorithms: RSA, Diffie-Helman, ECC over GF(p)
> - True random number generator (RNG)
> - Sector protection against R/W operation (PCROP)
> - CRC calculation unit
> - Die information: 96-bit unique ID
> - IEEE 64-bit unique ID, possibility to derive 802.15.4 64-bit
>   and Bluetooth|reg| Low Energy
> - 48-bit EUI

More information about STM32WB5MMG can be found here:

- [STM32WB5MMG on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32wb5mmg.html)
- [STM32WB5MMG datasheet](https://www.st.com/resource/en/datasheet/stm32wb5mmg.pdf)

### Supported Features

The `stm32wb5mmg` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `stm32wb5mmg/stm32wb55xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L33) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | STM32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L416) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32-adc.md#std-dtcompatible-st-stm32-adc) |
| Bluetooth | on-chip | STM32WB Radio device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L579) | [`st,stm32wb-rf`](../../../../build/dts/api/bindings/bluetooth/st%2Cstm32wb-ble-rf.md#std-dtcompatible-st-stm32wb-rf) |
| Clock control | on-chip | STM32WB Reset and Clock controller node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L163) | [`st,stm32wb-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32wb-rcc.md#std-dtcompatible-st-stm32wb-rcc) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L79)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L87) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 MSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L101) | [`st,stm32-msi-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-msi-clock.md#std-dtcompatible-st-stm32-msi-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L108) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32WB and STM32WL PLL node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L130) | [`st,stm32wb-pll-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32wb-pll-clock.md#std-dtcompatible-st-stm32wb-pll-clock) |
| on-chip | STM32 Clock multiplexer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L136) | [`st,stm32-clock-mux`](../../../../build/dts/api/bindings/clock/st%2Cstm32-clock-mux.md#std-dtcompatible-st-stm32-clock-mux) |
| Counter | on-chip | STM32 counters[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L366) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st%2Cstm32-counter.md#std-dtcompatible-st-stm32-counter) |
| Cryptographic accelerator | on-chip | STM32 AES Accelerator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L515) | [`st,stm32-aes`](../../../../build/dts/api/bindings/crypto/st%2Cstm32-aes.md#std-dtcompatible-st-stm32-aes) |
| DMA | on-chip | STM32 DMA controller (V2)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L449) | [`st,stm32-dma-v2`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dma-v2.md#std-dtcompatible-st-stm32-dma-v2) |
| on-chip | STM32 DMAMUX controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L471) | [`st,stm32-dmamux`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dmamux.md#std-dtcompatible-st-stm32-dmamux) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L144) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO Controller[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L195) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| I2C | on-chip | STM32 I2C V2 controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L263) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L174) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32-exti.md#std-dtcompatible-st-stm32-exti) |
| Memory controller | on-chip | STM32 Battery Backed RAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L297) | [`st,stm32-bbram`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32-bbram.md#std-dtcompatible-st-stm32-bbram) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L153) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st%2Cstm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32wb5mmg/stm32wb5mmg.dts?plain=1#L84) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L574) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L189) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| Power management | on-chip | STM32 power controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L524) | [`st,stm32-pwr`](../../../../build/dts/api/bindings/power/st%2Cstm32-pwr.md#std-dtcompatible-st-stm32-pwr) |
| PWM | on-chip | STM32 PWM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L343) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| QSPI | on-chip | STM32 QSPI Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L497) | [`st,stm32-qspi`](../../../../build/dts/api/bindings/qspi/st%2Cstm32-qspi.md#std-dtcompatible-st-stm32-qspi) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L168) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L507) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st%2Cstm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L287) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st%2Cstm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L548) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L559) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L567) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L254) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L324) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SMbus | on-chip | STM32 SMBus controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L585) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st%2Cstm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller with embedded Rx and Tx FIFOs[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L304) | [`st,stm32-spi-fifo`](../../../../build/dts/api/bindings/spi/st%2Cstm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L62) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 timers[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L333) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers) |
| on-chip | STM32 low-power timer (LPTIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L438) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st%2Cstm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| USB | on-chip | STM32 USB controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L483) | [`st,stm32-usb`](../../../../build/dts/api/bindings/usb/st%2Cstm32-usb.md#std-dtcompatible-st-stm32-usb) |
| Watchdog | on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L246) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |
| on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L432) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |

### Bluetooth and compatibility with STM32WB Copro Wireless Binaries

To operate bluetooth on STM32WB5MMG, Cortex-M0 core should be flashed with
a valid STM32WB Coprocessor binaries (either ‘Full stack’ or ‘HCI Layer’).
These binaries are delivered in STM32WB Cube packages, under
`Projects/STM32WB_Copro_Wireless_Binaries/STM32WB5x/`

For compatibility information with the various versions of these binaries,
please check [hal\_stm32:lib/stm32wb/README.rst](https://github.com/zephyrproject-rtos/hal_stm32/blob/1e753266ddfb4b07a8a0b1ec566e9637ea45d5ef/lib/stm32wb/README.rst).

Note that since STM32WB Cube package V1.13.2, “full stack” binaries are not compatible
anymore for a use in Zephyr and only “HCI Only” versions should be used on the M0
side.

### Connections and IOs

#### Default Zephyr Peripheral Mapping:

- UART\_1 TX/RX : PB7/PB6
- LPUART\_1 TX/RX : PA3/PA2
- USB : PA11/PA12
- SWD : PA13/PA14

#### System Clock

STM32WB5MMG System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by HSE clock at 32MHz.

#### Serial Port

STM32WB5MMG board has 2 (LP)U(S)ARTs. LPUART1 is connected to the main U585I
microcontroller that is used as HCI controller port. USART1 is not connected
to any external pinout, so it is not possible to debug the module directly.
Rather, users can use the available USB port (CN12) to run virtual com port
(VCP) USB stack for the debugging.

## Programming and Debugging

The `stm32wb5mmg` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[stm32cubeprogrammer](../../../../develop/flash_debug/host-tools.md#runner-stm32cubeprogrammer)** | ✅ (default) |  |  |  |  |

Applications for the `stm32wb5mmg` board configuration can be built the
usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)).

### Flashing the module

The onboard ST-Link on the `b_u585i_iot02a` board can be used to flash the
STM32WB5MMG module. To do this you should put SW4 on OFF and SW5 on ON mode.
In this case the firmware will be uploaded on the STM32WB5MMG module.

The module is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, openocd can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
```

#### Flashing `hci_uart` application to STM32WB5MMG

Connect the B-U585I-IOT02A to your host computer using the USB port. Put
the SW4 (MCU SWD) in OFF mode and SW5 (SWD BLE) in ON mode. Then build
and flash an application. Here is an example for the
[HCI UART](../../../../samples/bluetooth/hci_uart/README.md#bluetooth_hci_uart "Expose a Bluetooth controller to another device or CPU over UART.") application.

Run a serial host program to connect with your B-U585I-IOT02A board:

```shell
$ minicom -D /dev/ttyACM0
```

Then build and flash the application for the STM32WB5MMG module.

```shell
# From the root of the zephyr repository
west build -b stm32wb5mmg samples/bluetooth/hci_uart
west flash
```

Next, reverse back the buttons to default mode (SW4 on ON and SW5
on OFF) mode. In this case we will upload the Bluetooth sample on the
main microcontroller.Then, build the bluetooth
[samples/bluetooth/observer](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/observer) demo application for
B-U585I-IOT02A board:

```shell
# From the root of the zephyr repository
west build -b b_u585i_iot02a samples/bluetooth/observer
west flash
```

Rest the board and you should see the following messages on the console:

```shell
Starting Observer Demo
Started scanning...
Exiting main thread.
Device found: 2C:98:F3:64:58:06 (random) (RSSI -82), type 3, AD data len 31
Device found: CE:5B:9A:87:69:4F (random) (RSSI -80), type 3, AD data len 8
Device found: 7B:1E:DD:38:23:E1 (random) (RSSI -85), type 0, AD data len 17
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[HCI UART](../../../../samples/bluetooth/hci_uart/README.md#bluetooth_hci_uart "Expose a Bluetooth controller to another device or CPU over UART.") application.

```shell
# From the root of the zephyr repository
west build -b b_u585i_iot02a samples/bluetooth/observer
west debug
```

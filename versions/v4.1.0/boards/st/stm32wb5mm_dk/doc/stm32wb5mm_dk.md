---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/stm32wb5mm_dk/doc/stm32wb5mm_dk.html
original_path: boards/st/stm32wb5mm_dk/doc/stm32wb5mm_dk.html
---

# STM32WB5MM-DK

Board Overview

[![../../../../_images/STM32WB5MM_DK.jpg](https://docs.zephyrproject.org/4.1.0/_images/STM32WB5MM_DK.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/STM32WB5MM_DK.jpg)

STM32WB5MM-DK

Name:
:   `stm32wb5mm_dk`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32wb55xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm32wb5mm_dk/doc/stm32wb5mm_dk.rst/../..)

## Overview

The STM32WB5MM-DK Discovery kit is designed as a complete demonstration
and development platform for the STMicroelectronics STM32W5MMG module based
on the Arm® Cortex®-M4 and Arm® Cortex®-M0+ cores.
The STM32 device is a multi-protocol wireless and ultra-low-power device
embedding a powerful and ultra-low-power radio compliant with the
Bluetooth® Low Energy (BLE) SIG specification v5.2 and with
IEEE 802.15.4-2011.

STM32WB5MM-DK supports the following features:

- STM32WB5MMG (1-Mbyte Flash memory, 256-Kbyte SRAM)
  :   - Dual-core 32‑bit (Arm® Cortex®-M4 and M0+)
      - 2.4 GHz RF transceiver
      - 0.96-inch 128x64 OLED display
      - 128-Mbit Quad-SPI NOR Flash Memory
      - Temperature sensor
      - Accelerometer/gyroscope sensor
      - Time-of-Flight and gesture-detection sensor
      - Digital microphone
      - RGB LED
      - Infrared LED
      - 3 push-buttons (2 users and 1 reset) and 1 touch key button
- Board connectors:
  :   - STMod+
      - ARDUINO® Uno V3 expansion connector
      - USB user with Micro-B connector
      - TAG10 10-pin footprint
- Flexible power-supply options:
  :   - ST-LINK/V2-1 USB connector,
      - 5 V delivered by:
        :   - ARDUINO®,
            - external connector,
            - USB charger, or USB power
- On-board ST-LINK/V2-1 debugger/programmer with USB re-enumeration
  :   - Virtual COM port and debug port

More information about the board can be found in [STM32WB5MM-DK on www.st.com](https://www.st.com/en/evaluation-tools/stm32wb5mm-dk.html).

## Hardware

STM32WB5MMG is an ultra-low-power and small form factor certified 2.4 GHz
wireless module. It supports Bluetooth® Low Energy 5.4, Zigbee® 3.0,
OpenThread, dynamic, and static concurrent modes, and 802.15.4 proprietary
protocols.

Based on the STMicroelectronics STM32WB55VGY wireless microcontroller,
STM32WB5MMG provides best-in-class RF performance thanks to its high
receiver sensitivity and output power signal. Its low-power features
enable extended battery life, small coin-cell batteries, and energy harvesting.

- Ultra-low-power with FlexPowerControl
- Core: ARM® 32-bit Cortex®-M4 CPU with FPU
- Radio:

  - 2.4GHz
  - RF transceiver supporting:

    - Bluetooth® 5.4 specification,
    - IEEE 802.15.4-2011 PHY and MAC,
    - Zigbee® 3.0
  - RX sensitivity:

    - -96 dBm (Bluetooth® Low Energy at 1 Mbps),
    - -100 dBm (802.15.4)
  - Programmable output power up to +6 dBm with 1 dB steps
  - Integrated balun to reduce BOM
  - Support for 2 Mbps
  - Support GATT caching
  - Support EATT (enhanced ATT)
  - Support advertising extension
  - Accurate RSSI to enable power control
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

More information about STM32WB5MMG can be found here:

- [STM32WB5MM-DK on www.st.com](https://www.st.com/en/evaluation-tools/stm32wb5mm-dk.html)
- [STM32WB5MMG datasheet](https://www.st.com/resource/en/datasheet/stm32wb5mmg.pdf)

### Supported Features

The `stm32wb5mm_dk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `stm32wb5mm_dk/stm32wb55xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L33) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | STM32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L416) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st,stm32-adc.md#std-dtcompatible-st-stm32-adc) |
| Bluetooth | on-chip | STM32WB Radio device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L578) | [`st,stm32wb-rf`](../../../../build/dts/api/bindings/bluetooth/st,stm32wb-ble-rf.md#std-dtcompatible-st-stm32wb-rf) |
| Clock control | on-chip | STM32WB Reset and Clock controller node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L163) | [`st,stm32wb-rcc`](../../../../build/dts/api/bindings/clock/st,stm32wb-rcc.md#std-dtcompatible-st-stm32wb-rcc) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L79)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L87) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 MSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L101) | [`st,stm32-msi-clock`](../../../../build/dts/api/bindings/clock/st,stm32-msi-clock.md#std-dtcompatible-st-stm32-msi-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L108) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32WB and STM32WL PLL node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L130) | [`st,stm32wb-pll-clock`](../../../../build/dts/api/bindings/clock/st,stm32wb-pll-clock.md#std-dtcompatible-st-stm32wb-pll-clock) |
| on-chip | STM32 Clock multiplexer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L136) | [`st,stm32-clock-mux`](../../../../build/dts/api/bindings/clock/st,stm32-clock-mux.md#std-dtcompatible-st-stm32-clock-mux) |
| Counter | on-chip | STM32 counters[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L366) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st,stm32-counter.md#std-dtcompatible-st-stm32-counter) |
| Cryptographic accelerator | on-chip | STM32 AES Accelerator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L514) | [`st,stm32-aes`](../../../../build/dts/api/bindings/crypto/st,stm32-aes.md#std-dtcompatible-st-stm32-aes) |
| DMA | on-chip | STM32 DMA controller (V2)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L449) | [`st,stm32-dma-v2`](../../../../build/dts/api/bindings/dma/st,stm32-dma-v2.md#std-dtcompatible-st-stm32-dma-v2) |
| on-chip | STM32 DMAMUX controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L471) | [`st,stm32-dmamux`](../../../../build/dts/api/bindings/dma/st,stm32-dmamux.md#std-dtcompatible-st-stm32-dmamux) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L144) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st,stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO controller[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L195) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st,stm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| I2C | on-chip | STM32 I2C V2 controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L275)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L263) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st,stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32wb5mm_dk/stm32wb5mm_dk.dts?plain=1#L38) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L174) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st,stm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED strip | on-board | TLC59731 RGB LED Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32wb5mm_dk/stm32wb5mm_dk.dts?plain=1#L28) | [`ti,tlc59731`](../../../../build/dts/api/bindings/led_strip/ti,tlc59731.md#std-dtcompatible-ti-tlc59731) |
| Memory controller | on-chip | STM32 Battery Backed RAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L297) | [`st,stm32-bbram`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-bbram.md#std-dtcompatible-st-stm32-bbram) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L153) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st,stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32wb5mm_dk/stm32wb5mm_dk.dts?plain=1#L134) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L573) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L189) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st,stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| Power management | on-chip | STM32 power controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L523) | [`st,stm32-pwr`](../../../../build/dts/api/bindings/power/st,stm32-pwr.md#std-dtcompatible-st-stm32-pwr) |
| PWM | on-chip | STM32 PWM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L343) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st,stm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| QSPI | on-chip | STM32 QSPI Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L496) | [`st,stm32-qspi`](../../../../build/dts/api/bindings/qspi/st,stm32-qspi.md#std-dtcompatible-st-stm32-qspi) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L168) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st,stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L506) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st,stm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L287) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st,stm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-board | STMicroelectronics VL53L0X Time of Flight sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32wb5mm_dk/stm32wb5mm_dk.dts?plain=1#L185) | [`st,vl53l0x`](../../../../build/dts/api/bindings/sensor/st,vl53l0x.md#std-dtcompatible-st-vl53l0x) |
| on-board | STMicroelectronics ISM330DHCX 6-axis IMU (Inertial Measurement Unit) sensor accessed through SPI bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32wb5mm_dk/stm32wb5mm_dk.dts?plain=1#L191) | [`st,ism330dhcx`](../../../../build/dts/api/compatibles/st,ism330dhcx.md#std-dtcompatible-st-ism330dhcx) |
| on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L547) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st,stm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L558) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st,stm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L566) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st,stm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L254) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st,stm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L324) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st,stm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SMbus | on-chip | STM32 SMBus controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L584) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st,stm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller with embedded Rx and Tx FIFOs[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L304) | [`st,stm32-spi-fifo`](../../../../build/dts/api/bindings/spi/st,stm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L62) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 timers[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L333) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st,stm32-timers.md#std-dtcompatible-st-stm32-timers) |
| on-chip | STM32 low-power timer (LPTIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L438) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st,stm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| USB | on-chip | STM32 USB controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L483) | [`st,stm32-usb`](../../../../build/dts/api/bindings/usb/st,stm32-usb.md#std-dtcompatible-st-stm32-usb) |
| Watchdog | on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L246) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |
| on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb/stm32wb.dtsi?plain=1#L432) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |

### Bluetooth and compatibility with STM32WB Copro Wireless Binaries

To operate bluetooth on STM32WB5MMG, Cortex-M0 core should be flashed with
a valid STM32WB Coprocessor binaries (either ‘Full stack’ or ‘HCI Layer’).
These binaries are delivered in STM32WB Cube packages, under
`Projects/STM32WB_Copro_Wireless_Binaries/STM32WB5x/`.

For compatibility information with the various versions of these binaries,
please check [hal\_stm32:lib/stm32wb/README.rst](https://github.com/zephyrproject-rtos/hal_stm32/blob/55043bcc35fffa3b4a8c75a696d932b5020aad09/lib/stm32wb/README.rst).

Note that since STM32WB Cube package V1.13.2, “full stack” binaries are not
compatible anymore for a use in Zephyr and only “HCI Only” versions should be
used on the M0 side.

### Connections and IOs

#### Default Zephyr Peripheral Mapping:

- UART\_1 TX/RX : PB7/PB6 ( Connected to ST-Link VCP)
- LPUART\_1 TX/RX : PA3/PA2
- USB : PA11/PA12
- SWD : PA13/PA14
- I2C3: SDA/SCL PB11/PB13 (Sensor I2C bus)

#### System Clock

STM32WB5MMG System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by HSE clock at 32MHz.

#### Serial Port

STM32WB5MM-DK board has 2 (LP)U(S)ARTs. The Zephyr console output is assigned to USART1.
Default settings are `115200 8N1`.

#### LEDs

STM32WB5MM-DK has two types of LEDs, The resources coming from STM32WB5MMG are
shared between the RGB and IR LEDs. It is not possible to use them
simultaneously. The selection is done by JP4 and JP5 jumpers.
To use the RGB LED, JP5 must be ON and JP4 OFF. In this configuration,
GPIO\_SELECT2 (PH1) is the chip select for this RGB device on SPI1.

#### Buttons

STM32WB5MM-DK has two user buttons. The first button is mapped to PC12,
and the second to PC13. They have the aliases sw0 and sw1 respectively.

## Programming and Debugging

STM32WB5MM-DK has an on-board ST-Link to flash and debug the firmware on the module.

Applications for the `stm32wb5mm_dk` board configuration can be built the
usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD or pyOCD can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner pyocd
```

#### Flashing `hello_world` application to STM32WB5MM-DK

Connect the STM32WB5MM-DK to your host computer using the USB port (CN11).
Then build and flash an application. Here is an example for the `hello_world`
application.

Run a serial host program to connect with your STM32WB5MM-DK board:

```shell
$ minicom -D /dev/ttyACM0
```

Then first build and flash the application for the STM32WB5MM-DK board.

```shell
# From the root of the zephyr repository
west build -b stm32wb5mm_dk samples/hello_world
west flash
```

Reset the board and you should see the following messages on the console:

```shell
Hello World! stm32w5mm_dk
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello\_World](https://docs.zephyrproject.org/latest/samples/hello_world/README.html) application.

```shell
# From the root of the zephyr repository
west build -b stm32wb5mm_dk samples/hello_world
west debug
```

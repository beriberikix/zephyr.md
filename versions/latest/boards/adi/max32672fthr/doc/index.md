---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/adi/max32672fthr/doc/index.html
original_path: boards/adi/max32672fthr/doc/index.html
---

# MAX32672FTHR

Board Overview

[![../../../../_images/max32672fthr_img2.webp](https://docs.zephyrproject.org/4.2.0/_images/max32672fthr_img2.webp)
](https://docs.zephyrproject.org/4.2.0/_images/max32672fthr_img2.webp)

MAX32672FTHR

Name:
:   `max32672fthr`

Vendor:
:   Analog Devices, Inc.

Architecture:
:   arm

SoC:
:   max32672

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adi/max32672fthr/doc/index.rst/../..)

## Overview

The MAX32672FTHR is a rapid development platform that helps engineers quickly implement complex
sensor solutions using the MAX32672 Arm® Cortex®-M4. The board also includes the MAX8819 PMIC for
battery and power management. The form factor is a small, 0.9in by 2.6in, dual row header footprint
that is compatible with Adafruit® FeatherWing peripheral expansion boards. The board includes
an OLED display, a RGB indicator LED, and a user pushbutton. The MAX32672FTHR provides
a power-optimized flexible platform for quick proof-ofconcepts and early software development
to enhance time to market.

The Zephyr port is running on the MAX32672 MCU.

![MAX32672FTHR Front](https://docs.zephyrproject.org/4.2.0/_images/max32672fthr_img1.webp)
![MAX32672FTHR Back](https://docs.zephyrproject.org/4.2.0/_images/max32672fthr_img21.webp)

## Hardware

- MAX32672 MCU:

  - High-Efficiency Microcontroller for Low-Power High-Reliability Devices

    - Arm Cortex-M4 Processor with FPU up to 100MHz
    - 1MB Dual-Bank Flash with Error Correction
    - 200KB SRAM (160KB with ECC Enabled), Optionally Preserved in Lowest Power Modes
    - EEPROM Emulation on Flash
    - 16KB Unified Cache with ECC
    - Resource Protection Unit (RPU) and MemoryProtection Unit (MPU)
    - Dual- or Single-Supply Operation, 1.7V to 3.6V
    - Wide Operating Temperature: -40°C to +105°C
  - Flexible Clocking Schemes

    - Internal High-Speed 100MHz Oscillator
    - Internal Low-Power 7.3728MHz and Ultra-Low-Power 80kHz Oscillators
    - 16MHz–32MHz Oscillator, 32.768kHz Oscillator(External Crystal Required)
    - External Clock Input for CPU, LPUART, LPTMR
  - Power Management Maximizes Uptime for Battery Applications

    - 59.8μA/MHz ACTIVE at 0.9V up to 12MHz(CoreMark®)
    - 56.6μA/MHz ACTIVE at 1.1V up to 100MHz(While(1))
    - 3.09μA Full Memory Retention Power in BACKUPMode at VDD = 1.8V
    - 350nA Ultra-Low-Power RTC at
    - Wake from LPUART or LPTMR
  - Optimal Peripheral Mix Provides Platform Scalability

    - Up to 42 General-Purpose I/O Pins
    - Up to Three SPI Master/Slave (up to 50Mbps)
    - Up to Three 4-Wire UART
    - Up to Three I2C Master/Slave 3.4Mbps High Speed
    - Up to Four 32-Bit Timers (TMR)
    - Up to Two Low-Power 32-Bit Timers (LPTMR)
    - One I2S Master/Slave for Digital Audio Interface
    - 12-Channel, 12-Bit, 1Msps SAR ADC with On-DieTemperature Sensor
  - Security and Integrity

    - Optional ECDSA-Based Cryptographic SecureBootloader in ROM
    - Secure Cryptographic Accelerator for Elliptic Curve
    - AES-128/192/256 Hardware Acceleration Engine
- Benefits and Features of MAX32672FTHR:

  - MAX8819 PMIC with Integrated Charger
  - On-Board DAPLink Debug and Programming Interface for Arm Cortex-M4
  - Breadboard-Compatible Headers
  - Micro USB Connector
  - RGB Indicator LED
  - User Pushbutton
  - OLED Display
  - SWD Debugger
  - Virtual UART Console

### Supported Features

The `max32672fthr` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `max32672fthr/max32672` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L25) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | ADI MAX32 ADC SAR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L230) | [`adi,max32-adc-sar`](../../../../build/dts/api/bindings/adc/adi,max32-adc-sar.md#std-dtcompatible-adi-max32-adc-sar) |
| Clock control | on-chip | MAX32 Global Control[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L118) | [`adi,max32-gcr`](../../../../build/dts/api/bindings/clock/adi,max32-gcr.md#std-dtcompatible-adi-max32-gcr) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L53)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L67) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | ADI MAX32 counter[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L250) | [`adi,max32-counter`](../../../../build/dts/api/bindings/counter/adi,max32-counter.md#std-dtcompatible-adi-max32-counter) |
| on-chip | ADI MAX32 compatible Counter RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32672.dtsi?plain=1#L179) | [`adi,max32-rtc-counter`](../../../../build/dts/api/bindings/counter/adi,max32-rtc-counter.md#std-dtcompatible-adi-max32-rtc-counter) |
| Display | on-board | Solomon SSD1306 display controller on I2C bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32672fthr/max32672fthr.dts?plain=1#L128) | [`solomon,ssd1306fb`](../../../../build/dts/api/compatibles/solomon,ssd1306fb.md#std-dtcompatible-solomon-ssd1306fb) |
| DMA | on-chip | ADI MAX32 DMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32672.dtsi?plain=1#L101) | [`adi,max32-dma`](../../../../build/dts/api/bindings/dma/adi,max32-dma.md#std-dtcompatible-adi-max32-dma) |
| Flash controller | on-chip | MAX32XXX flash controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L102) | [`adi,max32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/adi,max32-flash-controller.md#std-dtcompatible-adi-max32-flash-controller) |
| GPIO & Headers | on-chip | MAX32 GPIO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L166) | [`adi,max32-gpio`](../../../../build/dts/api/bindings/gpio/adi,max32-gpio.md#std-dtcompatible-adi-max32-gpio) |
| on-board | GPIO pins exposed on Adafruit Feather headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32672fthr/max32672fthr.dts?plain=1#L61) | [`adafruit-feather-header`](../../../../build/dts/api/bindings/gpio/adafruit-feather-header.md#std-dtcompatible-adafruit-feather-header) |
| I2C | on-chip | ADI MAX32 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L149)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L127) | [`adi,max32-i2c`](../../../../build/dts/api/bindings/i2c/adi,max32-i2c.md#std-dtcompatible-adi-max32-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32672fthr/max32672fthr.dts?plain=1#L42) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32672fthr/max32672fthr.dts?plain=1#L26) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L110) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | MAX32 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L160) | [`adi,max32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/adi,max32-pinctrl.md#std-dtcompatible-adi-max32-pinctrl) |
| PWM | on-chip | ADI MAX32 PWM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L254) | [`adi,max32-pwm`](../../../../build/dts/api/bindings/pwm/adi,max32-pwm.md#std-dtcompatible-adi-max32-pwm) |
| RNG | on-chip | ADI MAX32XXX TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L214) | [`adi,max32-trng`](../../../../build/dts/api/bindings/rng/adi,max32-trng.md#std-dtcompatible-adi-max32-trng) |
| Serial controller | on-chip | MAX32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L187)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L196) | [`adi,max32-uart`](../../../../build/dts/api/bindings/serial/adi,max32-uart.md#std-dtcompatible-adi-max32-uart) |
| SPI | on-chip | ADI MAX32 SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32672.dtsi?plain=1#L131)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32672.dtsi?plain=1#L121) | [`adi,max32-spi`](../../../../build/dts/api/bindings/spi/adi,max32-spi.md#std-dtcompatible-adi-max32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L97) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | ADI MAX32 timer[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L242) | [`adi,max32-timer`](../../../../build/dts/api/bindings/timer/adi,max32-timer.md#std-dtcompatible-adi-max32-timer) |
| Watchdog | on-chip | MAX32XXX watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L221)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32672.dtsi?plain=1#L112) | [`adi,max32-watchdog`](../../../../build/dts/api/bindings/watchdog/adi,max32-watchdog.md#std-dtcompatible-adi-max32-watchdog) |

### Connections and IOs

## J9 Pinout

| Pin | Name | Description |
| --- | --- | --- |
| 1 | RST | Master Reset Signal |
| 2 | 3V3 | 3.3V Output. Typically used to provide 3.3V to peripherals connected to the expansion headers. |
| 3 | 1V8 | 1.8V Output. Typically used to provide 1.8V to peripherals connected to the expansion headers. |
| 4 | GND | Ground |
| 5 | P0\_11 | GPIO or Analog Input (AIN3 channel). |
| 6 | P0\_12 | GPIO or Analog Input (AIN4 channel). |
| 7 | P0\_13 | GPIO or Analog Input (AIN5 channel). |
| 8 | P0\_22 | GPIO or ADC\_TRIG signal. |
| 9 | P0\_27 | GPIO or QERR signal. |
| 10 | P0\_26 | GPIO or QDIR signal. |
| 11 | P0\_16 | GPIO or SPI1 clock signal. |
| 12 | P0\_15 | GPIO or SPI1 MOSI signal. |
| 13 | P0\_14 | GPIO or SPI1 MISO signal. |
| 14 | P0\_28 | GPIO or UART1 Rx signal. |
| 15 | P0\_29 | GPIO or UART1 Tx signal. |
| 16 | GND | Ground |

## J7 Pinout

| Pin | Name | Description |
| --- | --- | --- |
| 1 | SYS | SYS Switched Connection to the Battery. This is the primary system power supply and automatically switches between the battery voltage and the USB supply when available. |
| 2 | PWR | In battery-powered mode, turns off the PMIC if shorted to ground. |
| 3 | VBUS | USB VBUS Signal. This can be used as a 5V supply when connected to USB. This pin can also be used as an input to power the board. |
| 4 | P0\_5 | GPIO or HFX\_CLK\_OUT signal. |
| 5 | P0\_6 | GPIO or QEA signal. |
| 6 | P0\_7 | GPIO or QEB signal. |
| 7 | P0\_23 | GPIO or QEI signal. |
| 8 | P0\_17 | GPIO or SPI1 slave select signal. |
| 9 | P0\_24 | GPIO or QES signal. |
| 10 | P0\_25 | GPIO or QMATCH signal. |
| 11 | P0\_18 | GPIO or I2C2 SCL signal. |
| 12 | P0\_19 | GPIO or I2C2 SDA signal. |

## Programming and Debugging

The `max32672fthr` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Flashing

The MAX32625 microcontroller on the board is flashed with DAPLink firmware at the factory.
It allows debugging and flashing the MAX32672 Arm Core over USB.

Once the debug probe is connected to your host computer, then you can simply run the
`west flash` command to write a firmware image into flash. To perform a full erase,
pass the `--erase` option when executing `west flash`.

### Debugging

Please refer to the [Flashing](#flashing) section and run the `west debug` command
instead of `west flash`.

## References

- [MAX32672FTHR web page](https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/max32672fthr.html)

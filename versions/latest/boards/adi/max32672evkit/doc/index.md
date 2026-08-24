---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/adi/max32672evkit/doc/index.html
original_path: boards/adi/max32672evkit/doc/index.html
---

# MAX32672EVKIT

Board Overview

[![../../../../_images/max32672evkit.webp](https://docs.zephyrproject.org/4.2.0/_images/max32672evkit.webp)
](https://docs.zephyrproject.org/4.2.0/_images/max32672evkit.webp)

MAX32672EVKIT

Name:
:   `max32672evkit`

Vendor:
:   Analog Devices, Inc.

Architecture:
:   arm

SoC:
:   max32672

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adi/max32672evkit/doc/index.rst/../..)

## Overview

The MAX32672 evaluation kit (EV kit) provides a platform for evaluating the capabilities
of the MAX32672 microcontroller, which is a small, high-reliability, ultra-low power,
32-bit microcontroller. The MAX32672 is a secure and cost-effective solution
for motion/motor control, industrial sensors, and battery-powered medical devices and offers legacy
designs an easy, cost-optimal upgrade path from 8-bit or 16-bit microcontrollers.

The Zephyr port is running on the MAX32672 MCU.

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
- Benefits and Features of MAX32672EVKIT:

  - Selectable, On-Board, High-Precision Voltage Reference
  - 128 x 128 (1.45in) Color TFT Display with SPI Interface
  - Breadboard-Compatible Headers
  - USB 2.0 Micro B-to-Serial UARTs
  - UART0 and LPUART0 Interface Is Selectable through On-Board Jumpers
  - All GPIOs Signals Accessed through 0.1in Headers
  - 12 Analog Inputs Accessed through 0.1in Headers with Optional Filtering
  - 10-Pin Arm® Cortex® SWD Connector
  - Board Power Provided by USB Port
  - On-Board, 3.3V LDO Regulator
  - Test Loops Provided to Supply Optional VCORE Power Externally
  - Individual Power Measurement on All IC Rails through Jumpers
  - Two General-Purpose LEDs and One General-Purpose Pushbutton Switch

### Supported Features

The `max32672evkit` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `max32672evkit/max32672` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L25) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | ADI MAX32 ADC SAR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L230) | [`adi,max32-adc-sar`](../../../../build/dts/api/bindings/adc/adi,max32-adc-sar.md#std-dtcompatible-adi-max32-adc-sar) |
| Clock control | on-chip | MAX32 Global Control[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L118) | [`adi,max32-gcr`](../../../../build/dts/api/bindings/clock/adi,max32-gcr.md#std-dtcompatible-adi-max32-gcr) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L53)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L67) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | ADI MAX32 counter[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L250) | [`adi,max32-counter`](../../../../build/dts/api/bindings/counter/adi,max32-counter.md#std-dtcompatible-adi-max32-counter) |
| on-chip | ADI MAX32 compatible Counter RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32672.dtsi?plain=1#L179) | [`adi,max32-rtc-counter`](../../../../build/dts/api/bindings/counter/adi,max32-rtc-counter.md#std-dtcompatible-adi-max32-rtc-counter) |
| Display | on-board | Sitronix ST7735X display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32672evkit/max32672evkit.dts?plain=1#L66) | [`sitronix,st7735r`](../../../../build/dts/api/bindings/display/sitronix,st7735r.md#std-dtcompatible-sitronix-st7735r) |
| DMA | on-chip | ADI MAX32 DMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32672.dtsi?plain=1#L101) | [`adi,max32-dma`](../../../../build/dts/api/bindings/dma/adi,max32-dma.md#std-dtcompatible-adi-max32-dma) |
| Flash controller | on-chip | MAX32XXX flash controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L102) | [`adi,max32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/adi,max32-flash-controller.md#std-dtcompatible-adi-max32-flash-controller) |
| GPIO & Headers | on-chip | MAX32 GPIO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L166) | [`adi,max32-gpio`](../../../../build/dts/api/bindings/gpio/adi,max32-gpio.md#std-dtcompatible-adi-max32-gpio) |
| I2C | on-chip | ADI MAX32 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L127)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L138) | [`adi,max32-i2c`](../../../../build/dts/api/bindings/i2c/adi,max32-i2c.md#std-dtcompatible-adi-max32-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32672evkit/max32672evkit.dts?plain=1#L39) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32672evkit/max32672evkit.dts?plain=1#L27) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L110) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | MAX32 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L160) | [`adi,max32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/adi,max32-pinctrl.md#std-dtcompatible-adi-max32-pinctrl) |
| PWM | on-chip | ADI MAX32 PWM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L254) | [`adi,max32-pwm`](../../../../build/dts/api/bindings/pwm/adi,max32-pwm.md#std-dtcompatible-adi-max32-pwm) |
| RNG | on-chip | ADI MAX32XXX TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L214) | [`adi,max32-trng`](../../../../build/dts/api/bindings/rng/adi,max32-trng.md#std-dtcompatible-adi-max32-trng) |
| Serial controller | on-chip | MAX32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L187)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L196) | [`adi,max32-uart`](../../../../build/dts/api/bindings/serial/adi,max32-uart.md#std-dtcompatible-adi-max32-uart) |
| SPI | on-chip | ADI MAX32 SPI[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32672.dtsi?plain=1#L121)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32672.dtsi?plain=1#L141) | [`adi,max32-spi`](../../../../build/dts/api/bindings/spi/adi,max32-spi.md#std-dtcompatible-adi-max32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L97) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | ADI MAX32 timer[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L242) | [`adi,max32-timer`](../../../../build/dts/api/bindings/timer/adi,max32-timer.md#std-dtcompatible-adi-max32-timer) |
| Watchdog | on-chip | MAX32XXX watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L221)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32672.dtsi?plain=1#L112) | [`adi,max32-watchdog`](../../../../build/dts/api/bindings/watchdog/adi,max32-watchdog.md#std-dtcompatible-adi-max32-watchdog) |

### Connections and IOs

| Name | Name | Settings | Description |
| --- | --- | --- | --- |
| JP1 | VREF | | Open | | --- | | Closed | | | Disconnects on-board, high-precision voltage reference. | | --- | | Connects on-board, high-precision voltage reference. | |
| JP2 | P0\_22 | | Open | | --- | | Closed | | | Disconnects red LED D1 from P0\_22. | | --- | | Connects red LED D1 to P0\_22. | |
| JP3 | P0\_23 | | Open | | --- | | Closed | | | Disconnects green LED D2 from P0\_23. | | --- | | Connects green LED D2 to P0\_23. | |
| JP4 | I2C0\_SCL | | Open | | --- | | Closed | | | Disconnects 2.2K pullup sourced by 3V3 from I2C0\_SCL. | | --- | | Connects 2.2K pullup sourced by 3V3 to I2C0\_SCL. | |
| JP5 | I2C0\_SDA | | Open | | --- | | Closed | | | Disconnects 2.2K pullup sourced by 3V3 from I2C0\_SDA. | | --- | | Connects 2.2K pullup sourced by 3V3 to I2C0\_SDA. | |
| JP6 | I2C1\_SCL | | Open | | --- | | Closed | | | Disconnects 2.2K pullup sourced by 3V3 from I2C1\_SCL. | | --- | | Connects 2.2K pullup sourced by 3V3 to I2C1\_SCL. | |
| JP7 | I2C1\_SDA | | Open | | --- | | Closed | | | Disconnects 2.2K pullup sourced by 3V3 from I2C1\_SDA. | | --- | | Connects 2.2K pullup sourced by 3V3 to I2C1\_SDA. | |
| JP8 | I2C2\_SCL | | Open | | --- | | Closed | | | Disconnects 2.2K pullup sourced by 3V3 from I2C2\_SCL. | | --- | | Connects 2.2K pullup sourced by 3V3 to I2C2\_SCL. | |
| JP9 | I2C2\_SDA | | Open | | --- | | Closed | | | Disconnects 2.2K pullup sourced by 3V3 from I2C2\_SDA. | | --- | | Connects 2.2K pullup sourced by 3V3 to I2C2\_SDA. | |
| JP10 | UART\_RX | | 2-1 | | --- | | 2-3 | | | Connects the USB serial bridge to UART0\_RX (P0.8). | | --- | | Connects the USB serial bridge to LUART0\_RX (P0.26). | |
| JP11 | UART\_TX | | 2-1 | | --- | | 2-3 | | | Connects the USB serial bridge to UART0\_TX (P0.9). | | --- | | Connects the USB serial bridge to LUART0\_TX (P0.27). | |
| JP12 | VDDA | | Open | | --- | | Closed | | | Disconnects power from VDDA. | | --- | | Connects power to VDDA. | |
| JP13 | VDD | | Open | | --- | | Closed | | | Disconnects power from VDD. | | --- | | Connects power to VDD. | |
| JP14 | VCORE | | Open | | --- | | Closed | | | Disconnects power from VCORE from an external power supply through test loop TP6. | | --- | | Connects power to VCORE from an external power supply through test loop TP6. | |
| JP15 | LDO DUT | | Open | | --- | | Closed | | | Disconnects power from 3.3V LDO. | | --- | | Connects power to 3.3V LDO. | |

### Detailed Description of Hardware

## Power Supply

The EV kit is powered by +5V, which is made available through VBUS on the Micro USB type-B
connector CN1. The blue VBUS LED (DS1) and the green 3.3V LED will illuminate
when the board is powered.

## Single- or Dual-Supply Operation

The EV kit is configured for single-supply operation. For dual-supply operation,
install a jumper on JP14 and connect an external supply to TP6 (VCORE\_EXT) and ground.
Refer to the MAX32672 data sheet for acceptable voltage values.

## Current Monitoring

Two pin headers provide convenient current monitoring points for VDDA EN (JP12), VDD EN (JP13),
and VCORE EN (JP14). JP14 is only used for current measurements when VCORE is supplied externally.

## Low-Power Mode Current Measurements

To accurately achieve the low-power current values, the EV kit must be configured such that
no outside influence (such as a pullup, external clock, or debugger connector) causes
a current source or sink on that GPIO. For these measurements, the board will be needed to be
configured as follows:

1. Remove jumpers JP2 through JP11.
2. Set SW2 to the DIS position and remove resistor R12.
3. Unplug the SWD connector.

## Clocking

The MAX32672 clocking is provided by an external 16MHz crystal (Y1).

## External Voltage Reference

The external voltage reference input VREF for the ADC can be sourced externally by a high-precision
external reference source (the MAX6071). VREF (JP1) allows the external reference
to be disconnected so that VREF can be sourced internally by VDDA.

## UART Interface

The EV kit provides a USB-to-UART bridge chip (the FTDI FT230XS-R). This bridge eliminates
the requirement for a physical RS-232 COM port. Instead, the IC’s UART access is through
the Micro USB type-B connector (CN1). The USB-to-UART bridge can be connected to the IC’s UART0 or
LPUART0 with jumpers JP10 (RX0) and JP11 (TX0). Virtual COM port drivers and guides for
installing Windows® drivers are available on the FTDI Chip website.

## Boot Loader

The boot loader is activated by the boot-load-enable slide switch (SW2).
This pulls P0\_10 low and, upon a power cycle or reset, the device will enter boot loader mode.

## GPIO and Alternate Function Headers

GPIO and alternate function signals from the MAX32672
can be accessed through 0.1in-spaced headers J3 and J4.

## Analog Headers

The 12 analog inputs can be accessed through 0.1inspaced headers JH1, JH2, and JH3.

## I2C Pullups

The I2C ports can independently pulled up to V\_AUX (3.3V default) through JP4 (I2C0\_CL\_PU) and JP5
(I2C0\_DA\_PU), JP6 (I2C1\_CL\_PU) and JP7 (I2C1\_DA\_PU), and JP8 (I2C2\_CL\_PU) and JP9 (I2C2\_DA\_PU).

## Programming and Debugging

The `max32672evkit` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

The IC can be reset by pushbutton SW1.

### Flashing

SWD debug can be accessed through an Arm Cortex 10-pin connector (J5).
Logic levels are set to 3V3 by default, but they can be set to 1.8V if TP5 (VDD\_VDDA\_EXT)
is supplied externally. Be sure to remove jumper JP15 (LDO\_DUT\_EN) to disconnect the 3.3V
LDO if supplying VDD and VDDA externally.

Once the debug probe is connected to your host computer, then you can simply run the
`west flash` command to write a firmware image into flash. To perform a full erase,
pass the `--erase` option when executing `west flash`.

Note

This board uses OpenOCD as the default debug interface. You can also use
a Segger J-Link with Segger’s native tooling by overriding the runner,
appending `--runner jlink` to your `west` command(s). The J-Link should
be connected to the standard 2\*5 pin debug connector (JH2) using an
appropriate adapter board and cable.

### Debugging

Please refer to the [Flashing](#flashing) section and run the `west debug` command
instead of `west flash`.

## References

- [MAX32672EVKIT web page](https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/max32672evkit.html)

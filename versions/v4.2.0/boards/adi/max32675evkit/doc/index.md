---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/adi/max32675evkit/doc/index.html
original_path: boards/adi/max32675evkit/doc/index.html
---

# MAX32675EVKIT

Board Overview

[![../../../../_images/max32675evkit.webp](https://docs.zephyrproject.org/4.2.0/_images/max32675evkit.webp)
](https://docs.zephyrproject.org/4.2.0/_images/max32675evkit.webp)

MAX32675EVKIT

Name:
:   `max32675evkit`

Vendor:
:   Analog Devices, Inc.

Architecture:
:   arm

SoC:
:   max32675

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adi/max32675evkit/doc/index.rst/../..)

## Overview

The MAX32675 evaluation kit (EV kit) provides a platform for evaluation capabilities of
the MAX32675 microcontroller, which is a highly integrated, mixed-signal, ultralow-power
microcontroller designed for industrial and medical sensors. It contains an integrated, low-power
HART modem which enables the bidirectional transfer of digital data over a current loop, to/from
industrial sensors for configuration and diagnostics.

The Zephyr port is running on the MAX32675 MCU.

## Hardware

- MAX32675 MCU:

  - Low-Power, High-Performance for IndustrialApplications

    - 100MHz Arm Cortex-M4 with FPU
    - 384KB Internal Flash
    - 160KB SRAM
    - 128kB ECC Enabled
    - 44.1μA/MHz ACTIVE Mode at 0.9V up to 12MHzCoremark®
    - 64.5μA/MHz ACTIVE Mode at 1.1V up to 100MHzCoremark
    - 2.84μA Full Memory Retention Current in BACKUPMode at VDDIO = 3.3V
    - Ultra-Low-Power Analog Peripherals
  - Optimal Peripheral Mix Provides Platform Scalability

    - Two Sigma-Delta ADCs
    - 12 Channels, Assignable to Either ADC
    - Flexible Resolution and Sample Rates (24 Bits at 0.4ksps, 16 Bits at 4ksps)
    - 12-Bit DAC
    - On-Die Temperature Sensor
    - SPI (M/S)
    - Up to Two I2C
    - Up to Two UARTs
    - Up to 23 GPIOs
    - Up to Five 32-Bit Timers
    - Two Windowed Watchdog Timers
    - 8-Channel Standard DMA Controller
    - One I2S Slave for Digital Audio Interface
  - Robust Security and Reliability

    - TRNG Compliant to SP800-90B
    - Secure Nonvolatile Key Storage and AES-128/192/256
    - Secure Bootloader to Protect IP/Firmware
    - Wide, -40°C to +105°C Operating TemperatureRange
- Benefits and Features of MAX32675EVKIT:

  > - HART Compatible Secondary Master with the Ability to Connect to Existing 4-20mA Current Loop and Communicate with HART Enabled Devices
  > - USB 2.0 Micro B to Serial UART
  > - Two On-Board, High-Precision Voltage References
  > - All GPIOs Signals Accessed Through 0.1in Headers
  > - Access to 4 Analog Inputs Through SMA Connectors Configured as Differential
  > - Access to 8 Analog Inputs Through 0.1in Headers Configured as Single-Ended
  > - DAC Output Accessed Through SMA Connector or Test Point
  > - 10-Pin SWD and Connector
  > - Board Power Provided by USB Port
  > - On-Board 1.0V, 1.8V, and 3.3V LDO Regulators
  > - Individual Power Measurement on all IC Rails Through Jumpers
  > - Two General-Purpose LEDs and Two General-Purpose Pushbutton Switches

### Supported Features

The `max32675evkit` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `max32675evkit/max32675` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L25) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | ADI MAX32 ADC 10-Bits[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L230) | [`adi,max32-adc-10b`](../../../../build/dts/api/bindings/adc/adi,max32-adc-10b.md#std-dtcompatible-adi-max32-adc-10b) |
| Clock control | on-chip | MAX32 Global Control[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L118) | [`adi,max32-gcr`](../../../../build/dts/api/bindings/clock/adi,max32-gcr.md#std-dtcompatible-adi-max32-gcr) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L53)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L67) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | ADI MAX32 counter[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L250) | [`adi,max32-counter`](../../../../build/dts/api/bindings/counter/adi,max32-counter.md#std-dtcompatible-adi-max32-counter) |
| on-chip | ADI MAX32 compatible Counter RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32675.dtsi?plain=1#L99) | [`adi,max32-rtc-counter`](../../../../build/dts/api/bindings/counter/adi,max32-rtc-counter.md#std-dtcompatible-adi-max32-rtc-counter) |
| DMA | on-chip | ADI MAX32 DMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32675.dtsi?plain=1#L69) | [`adi,max32-dma`](../../../../build/dts/api/bindings/dma/adi,max32-dma.md#std-dtcompatible-adi-max32-dma) |
| Flash controller | on-chip | MAX32XXX flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L102) | [`adi,max32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/adi,max32-flash-controller.md#std-dtcompatible-adi-max32-flash-controller) |
| GPIO & Headers | on-chip | MAX32 GPIO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L166) | [`adi,max32-gpio`](../../../../build/dts/api/bindings/gpio/adi,max32-gpio.md#std-dtcompatible-adi-max32-gpio) |
| I2C | on-chip | ADI MAX32 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L149)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L127) | [`adi,max32-i2c`](../../../../build/dts/api/bindings/i2c/adi,max32-i2c.md#std-dtcompatible-adi-max32-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32675evkit/max32675evkit.dts?plain=1#L38) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32675evkit/max32675evkit.dts?plain=1#L26) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L110) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | MAX32 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L160) | [`adi,max32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/adi,max32-pinctrl.md#std-dtcompatible-adi-max32-pinctrl) |
| PWM | on-chip | ADI MAX32 PWM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L254) | [`adi,max32-pwm`](../../../../build/dts/api/bindings/pwm/adi,max32-pwm.md#std-dtcompatible-adi-max32-pwm) |
| RNG | on-chip | ADI MAX32XXX TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L214) | [`adi,max32-trng`](../../../../build/dts/api/bindings/rng/adi,max32-trng.md#std-dtcompatible-adi-max32-trng) |
| Serial controller | on-chip | MAX32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L187)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L205) | [`adi,max32-uart`](../../../../build/dts/api/bindings/serial/adi,max32-uart.md#std-dtcompatible-adi-max32-uart) |
| SPI | on-chip | ADI MAX32 SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32675.dtsi?plain=1#L79) | [`adi,max32-spi`](../../../../build/dts/api/bindings/spi/adi,max32-spi.md#std-dtcompatible-adi-max32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L97) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | ADI MAX32 timer[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L242) | [`adi,max32-timer`](../../../../build/dts/api/bindings/timer/adi,max32-timer.md#std-dtcompatible-adi-max32-timer) |
| Watchdog | on-chip | MAX32XXX watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L221) | [`adi,max32-watchdog`](../../../../build/dts/api/bindings/watchdog/adi,max32-watchdog.md#std-dtcompatible-adi-max32-watchdog) |

### Connections and IOs

| Name | Name | Settings | Description |
| --- | --- | --- | --- |
| JP1 | P1\_9 | | Open | | --- | | Closed | | | Disconnects red LED D1 from P1\_9. | | --- | | Connects red LED D1 to P1\_9. | |
| JP2 | P1\_10 | | Open | | --- | | Closed | | | Disconnects green LED D2 from P1\_10. | | --- | | Connects green LED D2 to P1\_10. | |
| JP3 | I2C\_SCLK | | Open | | --- | | Closed | | | Disconnects 3V3 from I2C\_SCLK. | | --- | | Connects 3V3 to I2C0\_SCLK. | |
| JP4 | I2C\_SDA | | Open | | --- | | Closed | | | Disconnects 3V3 to I2C\_SDA. | | --- | | Connects 3V3 to I2C\_SDA. | |
| JP5 | UART0\_RX | | Open | | --- | | Closed | | | Disconnects UART0\_RX (P0.8) from the SWD connector. | | --- | | Connects UART0\_RX (P0.8) to the SWD connector. | |
| JP6 | UART0\_TX | | Open | | --- | | Closed | | | Disonnects UART0\_TX (P0.9) from the SWD connector. | | --- | | Connects UART0\_TX (P0.9) to the SWD connector. | |
| JP7 | REF0N | | Open | | --- | | Closed | | | Disconnects REF0N from ground. | | --- | | Connects REF0N to ground. | |
| JP8 | REF1N | | Open | | --- | | Closed | | | Disconnects REF1N from ground. | | --- | | Connects REF1N to ground. | |
| JP9 | | HART\_IN | | --- | | HART\_IN | | HART\_OUT | | HART\_OUT | | HART\_RTS | | HART\_RTS | | HART\_OCD | | HART\_OCD | | | Open | | --- | | 1-2 | | Open | | 3-4 | | Open | | 4-5 | | Open | | 7-8 | | | Disconnects TX of USB - serial bridge from HART\_IN (P0.15). | | --- | | Connects TX of USB - serial bridge to HART\_IN (P0.15). | | Disconnects RX of USB - serial bridge from HART\_OUT (P0.14). | | Connects RX of USB - serial bridge to HART\_OUT (P0.14). | | Disconnects RTS of USB - serial bridge from HART\_RTS (P1.8). | | Connects TX of USB - serial bridge to HART\_RTS (P1.8). | | Disconnects RTS of USB - serial bridge from HART\_OCD (P0.16). | | Connects TX of USB - serial bridge to HART\_OCD (P0.16). | |
| JP10 | SWD\_CLK | | Open | | --- | | Closed | | | Disconnects boot load enable circuit from SWD\_CLK (P0.1). | | --- | | Connects boot load enable circuit to SWD\_CLK (P0.1). | |
| JP11 | FSK\_IN | | Open | | --- | | Closed | | | Disconnects FSK\_IN from HART analog circuitry. | | --- | | Connects FSK\_IN to HART analog circuitry. | |
| JP12 | FSK\_OUT | | Open | | --- | | Closed | | | Disconnects FSK\_OUT from HART analog circuitry. | | --- | | Connects FSK\_OUT to HART analog circuitry. | |
| JP13 | RCV\_FSK | | Open | | --- | | Closed | | | Disconnects RCV\_FSK from CC LOOP. | | --- | | Connects RCV\_FSK to CC LOOP. | |
| JP14 | RCV\_FSK | | Open | | --- | | Closed | | | Disconnects RCV\_FSK from XFMR LOOP. | | --- | | Connects RCV\_FSK to XFMR LOOP. | |
| JP15 | RLOAD | | Open | | --- | | Closed | | | Disconnects 249Ω resistor shunt from CC LOOP. | | --- | | Connects 249Ω resistor shunt to CC LOOP. | |
| JP16 | N/A | N/A | N/A |
| JP17 | N/A | N/A | N/A |
| JP18 | N/A | N/A | N/A |
| JP19 | HART\_RTS | | Open | | --- | | Closed | | | Enables HART\_RTS optical transceiver. | | --- | | Bypasses HART\_RTS optical transceiver. | |
| JP20 | RLOAD | | Open | | --- | | Closed | | | Disconnects 249Ω resistor shunt from XFMR LOOP. | | --- | | Connects 249Ω resistor shunt to XFMR LOOP. | |
| JP21 | VDDIO | | Open | | --- | | Closed | | | Disconnects power from VDDIO. | | --- | | Connects power to VDDIO. | |
| JP22 | VDDA | | Open | | --- | | Closed | | | Disconnects power from VDDA. | | --- | | Connects power to VDDA. | |
| JP23 | VDD18 | | Open | | --- | | Closed | | | Disconnects power from VDD18. | | --- | | Connects power to VDD18. | |
| JP24 | VCORE | | Open | | --- | | Closed | | | Disconnects power from VCORE. | | --- | | Connects power to VCORE. | |
| JP25 | REF0P | | 2-1 | | --- | | 2-3 | | | Connects OB\_VREF to REF0P. | | --- | | Connects INT\_VREF to REF0P. | |
| JP26 | REF1P | | 2-1 | | --- | | 2-3 | | | Connects OB\_VREF to REF1P. | | --- | | Connects INT\_VREF to REF1P. | |

### Detailed Description of Hardware

## HART Interface

The HART circuitry acts as a secondary master with the ability to connect to an existing 4mA–20mA
current loop and communicates with HART-enabled devices. Connection to a capacitance coupled loop
through JH8 and a transformer loop is through JH9. HART communication to the MAX32675 is through
the USB connector CN1.

## USB-to-HART Interface

The EV kit provides a USB-to-HART bridge chip, FTDI FT231. This bridge eliminates the requirement
for a physical RS-232 COM port. Instead, the IC’s HART access is through the Micro-USB type-B
connector, CN1. Virtual COM port drivers and guides for installing Windows® drivers are available
at the FTDI chip website.

## Power Supply

The EV kit is powered by +5V that is made available through VBUS on the Micro-USB type-B
connector CN1. A blue LED (D5) illuminates when the board is powered. Green LEDs (D6), (D7),
and (D8) illuminate when the 3V3, 1V8, and 1V0 LDOs are powered, respectively.

## Current Monitoring

Two pin headers provide convenient current monitoring points for VDDIO EN (JP21),
VDDA EN (JP22), VDD18 EN (JP23), and VCORE (JP24).
To accurately achieve the low-power current values, the EVkit needs to be configured
such that no outside influence (i.e., pullups, external clock, debugger connector, etc.)
causes a current source or sink on that GPIO.

## Clocking

The MAX32675 clocking is provided by an external 16MHz crystal (Y1).

## Voltage Reference

The differential reference inputs REF0 and REF1 can be sourced by an internal reference (INT\_VREF)
or a higher precision external reference source, MAX6071.
This is selected by jumpers JP25 and JP26.

## UART Interface

The EV kit provides a USB-to-UART bridge chip (the FTDI FT230XS-R). This bridge eliminates
the requirement for a physical RS-232 COM port. Instead, the IC’s UART access is through
the Micro USB type-B connector (CN1). The USB-to-UART bridge can be connected to the IC’s UART0
or LPUART0 with jumpers JP10 (RX0) and JP11 (TX0). Virtual COM port drivers and guides for
installing Windows® drivers are available on the FTDI Chip website.

## Boot Loader

Boot load is activated by boot load enable slide switch SW5.

## GPIO and Alternate Function Headers

GPIO and alternate function signals from the MAX32675 can be accessed through 0.1in
spaced headers JH1, JH2, JH3, and JH4.

## Analog Input Access

Analog inputs (AIN0–AIN3) can be accessed differentially from SMA connectors J2 and J3 or
separately from TP10, TP12, TP15, and TP16, respectively. Analog inputs (AIN4–AIN11) can be
accessed through 0.1in spaced headers JH5 and JH6.

## I2C Pullups

The I2C port can independently pulled up to 3V3 through JP3 (I2C\_SCL) and JP4 (I2C\_SDA).

## Reset Pushbutton

The IC can be reset by pushbutton SW3.

## Indicator LEDs

General-purpose indicators LED D1 (red) is connected to GPIO P1.9 and LED D2 (green) is connected
to GPIO P1.10.

## GPIO Pushbutton Switches

The two general-purpose pushbuttons (SW1 and SW2) are connected to GPIO P1.11 and P1.12,
respectively. If the pushbutton is pressed, the attached port pin is pulled low.

## Programming and Debugging

The `max32675evkit` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Flashing

SWD debug can be accessed through an Arm Cortex 10-pin connector (J5).
Logic levels are set to 3V3 by default, but they can be set to 1.8V if TP5 (VDD\_VDDA\_EXT)
is supplied externally. Be sure to remove jumper JP15 (LDO\_DUT\_EN) to disconnect
the 3.3V LDO if supplying VDD and VDDA externally.

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

- [MAX32675EVKIT web page](https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/max32675evkit.html)

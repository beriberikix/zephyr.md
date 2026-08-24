---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/adi/max32680evkit/doc/index.html
original_path: boards/adi/max32680evkit/doc/index.html
---

# MAX32680EVKIT

Board Overview

[![../../../../_images/max32680evkit_img1.jpg](https://docs.zephyrproject.org/4.2.0/_images/max32680evkit_img1.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/max32680evkit_img1.jpg)

MAX32680EVKIT

Name:
:   `max32680evkit`

Vendor:
:   Analog Devices, Inc.

Architecture:
:   arm

SoC:
:   max32680

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adi/max32680evkit/doc/index.rst/../..)

## Overview

The MAX32680 evaluation kit (EV kit) provides a platform
for evaluation capabilities of the MAX32680 microcontroller,
which is an advanced system-on-chip (SoC)
designed for industrial and medical sensors. Power regulation
and management is provided by a single-inductor
multiple-output (SIMO) buck regulator system and contains
the latest generation Bluetooth® 5.2 Low Energy
(LE) radio.

The Zephyr port is running on the MAX32680 MCU.

## Hardware

- MAX32680 MCU:

  - Ultra-Low-Power Wireless Microcontroller

    - Internal 100MHz Oscillator
    - 512KB Flash and 128KB SRAM, Optional ECC on One 32KB SRAM Bank
  - Bluetooth 5.2 LE Radio

    - Dedicated, Ultra-Low-Power, 32-Bit RISC-VCoprocessor to Offload

    Timing-Critical Bluetooth Processing

    - Fully Open-Source Bluetooth 5.2 Stack Available
    - Supports AoA, AoD, LE Audio, and Mesh
    - High-Throughput (2Mbps) Mode•Long-Range (125kbps and 500kbps) Modes
    - Rx Sensitivity: -97.5dBm; Tx Power: +4.5dBm
    - Single-Ended Antenna Connection (50Ω)
  - Smart Integration Reduces BOM, Cost, and PCB Size

    - Two 16-Bit to 24-Bit Sigma-Delta ADCs
    - 12 Channels, Assignable to Either ADC
    - Flexible Resolution and Sample Rates
    - 24-Bits at 0.4ksps, 16-Bits at 4ksps
    - Four External Input, 10-Bit Sigma-Delta ADC 7.8ksps
    - 12-Bit DAC
    - On-Die Temperature Sensor
    - Digital Peripherals: Two SPI, Two I2C, up to FourUART, and up to 36 GPIOs
    - Timers: Six 32-Bit Timers, Two Watchdog Timers,Two Pulse Trains, 1-Wire® Master
  - Power Management Maximizes Battery Life

    - 2.0V to 3.6V Supply Voltage Range
    - Integrated SIMO Power Regulator
    - Dynamic Voltage Scaling (DVS)
    - 23.8μA/MHz ACTIVE Mode Current at 3.0VCoremark®
    - 4.4μA at 3.0V Retention Current for 32KB SRAM
    - Selectable SRAM Retention in Low-Power Modes
  - Robust Security and Reliability

    - TRNG
    - Secure Nonvolatile Key Storage and AES-128/192/256
    - Secure Boot to Protect IP/Firmware
    - Wide, -40°C to +85°C Operating Temperature
- External devices connected to the MAX32680 EVKIT:

  - SMA Connector for Attaching an External Bluetooth Antenna
  - 128 x 128 (1.45in) Color TFT Display with SPI Interface
  - Two Selectable On-Board, High-Precision Voltage References
  - USB 2.0 Micro B to Serial UARTs
  - UART1 and LPUART0 Interface is Selectable Through On-Board Jumpers
  - All GPIOs Signals Accessed Through 0.1in Headers
  - Access to Four Analog Inputs Through SMA Connectors Configured as Differential
  - Access to Eight Analog Inputs Through 0.1in Headers Configured as Single-End
  - Optional Discrete Filter for the Twelve Analog Inputs
  - DAC Accessed Through SMA Connector or Test Point
  - 10-Pin SWD Connector
  - 10-Pin RV JTAG Connector
  - Board Power Provided by USB Port
  - On-Board 3.3V LDO Regulator to Power MAX32680 Internal SIMO
  - Test Loops Provided to Supply Optional VCORE Power Externally
  - Individual Power Measurement on All IC Rails Through Jumpers
  - Two General Purpose LEDs and Two General Purpose Pushbutton Switches

### Supported Features

The `max32680evkit` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `max32680evkit/max32680/m4` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L25) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | ADI MAX32 ADC 10-Bits[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L230) | [`adi,max32-adc-10b`](../../../../build/dts/api/bindings/adc/adi,max32-adc-10b.md#std-dtcompatible-adi-max32-adc-10b) |
| Clock control | on-chip | MAX32 Global Control[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L118) | [`adi,max32-gcr`](../../../../build/dts/api/bindings/clock/adi,max32-gcr.md#std-dtcompatible-adi-max32-gcr) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L53)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L60) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | ADI MAX32 counter[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L250) | [`adi,max32-counter`](../../../../build/dts/api/bindings/counter/adi,max32-counter.md#std-dtcompatible-adi-max32-counter) |
| on-chip | ADI MAX32 compatible Counter RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L318) | [`adi,max32-rtc-counter`](../../../../build/dts/api/bindings/counter/adi,max32-rtc-counter.md#std-dtcompatible-adi-max32-rtc-counter) |
| Display | on-board | Sitronix ST7735X display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32680evkit/max32680evkit_max32680_m4.dts?plain=1#L72) | [`sitronix,st7735r`](../../../../build/dts/api/bindings/display/sitronix,st7735r.md#std-dtcompatible-sitronix-st7735r) |
| DMA | on-chip | ADI MAX32 DMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32680.dtsi?plain=1#L60) | [`adi,max32-dma`](../../../../build/dts/api/bindings/dma/adi,max32-dma.md#std-dtcompatible-adi-max32-dma) |
| Flash controller | on-chip | MAX32XXX flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L102) | [`adi,max32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/adi,max32-flash-controller.md#std-dtcompatible-adi-max32-flash-controller) |
| GPIO & Headers | on-chip | MAX32 GPIO[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L166)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32680.dtsi?plain=1#L24) | [`adi,max32-gpio`](../../../../build/dts/api/bindings/gpio/adi,max32-gpio.md#std-dtcompatible-adi-max32-gpio) |
| I2C | on-chip | ADI MAX32 I2C[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L127)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L149) | [`adi,max32-i2c`](../../../../build/dts/api/bindings/i2c/adi,max32-i2c.md#std-dtcompatible-adi-max32-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32680evkit/max32680evkit_max32680_m4.dts?plain=1#L39) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32680evkit/max32680evkit_max32680_m4.dts?plain=1#L27) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L110) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | MAX32 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L160) | [`adi,max32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/adi,max32-pinctrl.md#std-dtcompatible-adi-max32-pinctrl) |
| PWM | on-chip | ADI MAX32 PWM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L254) | [`adi,max32-pwm`](../../../../build/dts/api/bindings/pwm/adi,max32-pwm.md#std-dtcompatible-adi-max32-pwm) |
| RNG | on-chip | ADI MAX32XXX TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L214) | [`adi,max32-trng`](../../../../build/dts/api/bindings/rng/adi,max32-trng.md#std-dtcompatible-adi-max32-trng) |
| Serial controller | on-chip | MAX32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L196)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L187) | [`adi,max32-uart`](../../../../build/dts/api/bindings/serial/adi,max32-uart.md#std-dtcompatible-adi-max32-uart) |
| SPI | on-chip | ADI MAX32 SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32680.dtsi?plain=1#L79)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32680.dtsi?plain=1#L89) | [`adi,max32-spi`](../../../../build/dts/api/bindings/spi/adi,max32-spi.md#std-dtcompatible-adi-max32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L97) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | ADI MAX32 timer[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L242) | [`adi,max32-timer`](../../../../build/dts/api/bindings/timer/adi,max32-timer.md#std-dtcompatible-adi-max32-timer) |
| 1-Wire | on-chip | ADI MAX32xxx MCUs 1-Wire Master[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32680.dtsi?plain=1#L127) | [`adi,max32-w1`](../../../../build/dts/api/bindings/w1/adi,max32-w1.md#std-dtcompatible-adi-max32-w1) |
| Watchdog | on-chip | MAX32XXX watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L221)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32680.dtsi?plain=1#L70) | [`adi,max32-watchdog`](../../../../build/dts/api/bindings/watchdog/adi,max32-watchdog.md#std-dtcompatible-adi-max32-watchdog) |

### Connections and IOs

| Name | Name | Settings | Description |
| --- | --- | --- | --- |
| JP1 | VREGI | | Open | | --- | | Closed | | | Disconnects 3.3V power from the MAX32680 SIMO. | | --- | | Connects 3.3V power to the MAX32680 SIMO. | |
| JP2 | REF0P | | 2-1 | | --- | | 2-3 | | | Connects the external high-precision voltage reference to REF0P. | | --- | | Connects the internal voltage reference to REF0P. | |
| JP3 | REF0N | | Open | | --- | | Closed | | | Disconnects REF0N from ground. | | --- | | Connects REF0N to ground. | |
| JP4 | VDDIO\_AUX | | Open | | --- | | Closed | | | Disconnects VDDIO\_AUX from pull-ups and reference voltages. | | --- | | Connects VDDIO\_AUX to pull-ups and reference voltages. | |
| JP5 | VDDIOH | | Open | | --- | | Closed | | | Connects VREGO\_A to VDDIOH. | | --- | | Connects the 3.3V from the estrenal LDO to VDDIOH. | |
| JP6 | REF1P | | 2-1 | | --- | | 2-3 | | | Connects the external high-precision voltage reference to REF1P. | | --- | | Connects the internal voltage reference to REF1P. | |
| JP7 | REF1N | | Open | | --- | | Closed | | | Disconnects REF1N from ground. | | --- | | Connects REF1N to ground. | |
| JP8 | I2C0\_SDA I2C0\_SCL | | 2-1 | | --- | | 2-3 | | | Connects I2C0 pullups to VDDIO\_AUX (1.8V). | | --- | | Connects I2C0 pullups to 3.3V. | |
| JP9 | I2C1\_SDA I2C1\_SCL | | 2-1 | | --- | | 2-3 | | | Connects I2C1 pullups to VDDIO\_AUX (1.8V). | | --- | | Connects I2C1 pullups to 3.3V. | |
| JP10 | P0\_24 | | Open | | --- | | Closed | | | Disconnects red LED D1 from P0\_24. | | --- | | Connects red LED D1 to P0\_24. | |
| JP11 | P0\_25 | | Open | | --- | | Closed | | | Disconnects green LED D2 from P0\_25. | | --- | | Connects green LED D2 to P0\_25. | |
| JP12 | FSK\_IN | | Open | | --- | | Closed | | | Disconnects FSK\_IN from HART analog circuitry. | | --- | | Connects FSK\_IN to HART analog circuitry. | |
| JP13 | RCV\_FSK | | Open | | --- | | Closed | | | Disconnects RCV\_FSK from CC LOOP. | | --- | | Connects RCV\_FSK to CC LOOP. | |
| JP14 | FSK\_OUT | | Open | | --- | | Closed | | | Disconnects FSK\_OUT from HART analog circuitry. | | --- | | Connects FSK\_OUT to HART analog circuitry. | |
| JP15 | RCV\_FSK | | Open | | --- | | Closed | | | Disconnects RCV\_FSK from XFMR LOOP. | | --- | | Connects RCV\_FSK to XFMR LOOP. | |
| JP16 | RLOAD | | Open | | --- | | Closed | | | Disconnects 249 ohm resistor shunt from CC LOOP. | | --- | | Connects 249 ohm resistor shunt to CC LOOP. | |
| JP17 | FSK AMP GAIN | | Open | | --- | | Closed | | | Enables FSK variable amp gain. | | --- | | Disables FSK variable amp gain. | |
| JP18 | AMP BYPASS | | 2-1 | | --- | | 2-3 | | | Enables FSK amp. | | --- | | Bypasses FSK amp. | |
| JP19 | FSK AMP GAIN | | Open | | --- | | Closed | | | Enables FSK fixed amp gain. | | --- | | Disables FSK fixed amp gain. | |
| JP20 | HART\_RTS | | Open | | --- | | Closed | | | Enables HART\_RTS optical transceiver. | | --- | | Bypasses HART\_RTS optical transceiver. | |
| JP21 | RLOAD | | Open | | --- | | Closed | | | Disconnects 249 ohm resistor shunt from XFMR LOOP. | | --- | | Connects 249 ohm resistor shunt to XFMR LOOP. | |
| JP22 | UART0\_RX | | 2-1 | | --- | | 2-3 | | | Disconnects the USB - serial bridge from UART1\_RX (P0.12). | | --- | | Connects the USB - serial bridge to LPUART\_RX (P2.6). | |
| JP23 | UART0\_TX | | 2-1 | | --- | | 2-3 | | | Disonnects the USB - serial bridge from UART1\_TX (P0.13). | | --- | | Connects the USB - serial bridge to LPUART\_TX (P2.7). | |
| JP24 | | HART\_IN | | --- | | HART\_IN | | HART\_OUT | | HART\_OUT | | HART\_RTS | | HART\_RTS | | HART\_OCD | | HART\_OCD | | | Open | | --- | | 1-2 | | Open | | 2-3 | | Open | | 3-4 | | Open | | 4-5 | | | Disconnects TX of USB - serial bridge from HART\_IN (P0.1) | | --- | | Connects TX of USB - serial bridge to HART\_IN (P0.1). | | Disconnects RX of USB - serial bridge from HART\_OUT (P0.0). | | Connects RX of USB - serial bridge to HART\_OUT (P0.0). | | Disconnects RTS of USB - serial bridge from HART\_RTS (P0.3). | | Connects TX of USB - serial bridge to HART\_RTS (P0.3). | | Disconnects RTS of USB - serial bridge from HART\_OCD (P0.2). | | Connects TX of USB - serial bridge to HART\_OCD (P0.2). | |
| JP25 | RSTN | | Open | | --- | | Close | | | Disconnects DUT\_3V3\_RSTN from RSTN. | | --- | | Connects DUT\_3V3\_RSTN to RSTN. | |

## Programming and Debugging

The `max32680evkit` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Flashing

The MAX32680 MCU can be flashed by connecting an external debug probe to the
SWD port. SWD debug can be accessed through the Cortex 10-pin connector, JH10.
Logic levels are set to 1.8V (VDDIO\_AUX).

Once the debug probe is connected to your host computer, then you can simply run the
`west flash` command to write a firmware image into flash. To perform a full erase,
pass the `--erase` option when executing `west flash`.

### Debugging

Please refer to the [Flashing](#flashing) section and run the `west debug` command
instead of `west flash`.

## References

- [MAX32680EVKIT web page](https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/max32680evkit.html#eb-overview)

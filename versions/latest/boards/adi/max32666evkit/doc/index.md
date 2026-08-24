---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/adi/max32666evkit/doc/index.html
original_path: boards/adi/max32666evkit/doc/index.html
---

# MAX32666EVKIT

Board Overview

[![../../../../_images/max32666evkit.webp](https://docs.zephyrproject.org/4.2.0/_images/max32666evkit.webp)
](https://docs.zephyrproject.org/4.2.0/_images/max32666evkit.webp)

MAX32666EVKIT

Name:
:   `max32666evkit`

Vendor:
:   Analog Devices, Inc.

Architecture:
:   arm

SoC:
:   max32666

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adi/max32666evkit/doc/index.rst/../..)

## Overview

The MAX32666EVKIT provides a platform for evaluating the capabilities of the MAX32665 and MAX32666
high-efficiency Arm® microcontrollers and audio DSP for wearable and hearable device applications.

The Zephyr port is running on the MAX32666 MCU.

## Hardware

- MAX32666 MCU:

  - High-Efficiency Microcontroller and Audio DSP for Wearable and Hearable Devices

    - Arm Cortex-M4 with FPU Up to 96MHz
    - Optional Second Arm Cortex-M4 with FPU Optimized for Data Processing
    - Low-Power 7.3728MHz System Clock Option
    - 1MB Flash, Organized into Dual Banks 2 x 512KB
    - 560KB (448KB ECC) SRAM; 3 x 16KB Cache
    - Optional Error Correction Code (ECC-SEC-DED)for Cache, SRAM, and Internal Flash
  - Bluetooth 5 Low Energy Radio

    - 1Mbps and 2Mbps Data Throughput
    - Long Range (125kbps and 500kbps)
    - Advertising Extension
    - Rx Sensitivity: -95dbm; Tx Power Up to +4.5dbm
    - On-Chip Matching with Single-Ended Antenna Port
  - Power Management Maximizes Operating Time for Battery Applications

    - Integrated SIMO SMPS for Coin-Cell Operation
    - Dynamic Voltage Scaling Minimizes Active Core Power Consumption
    - 27.3μA/MHz at 3.3V Executing from Cache
    - Selectable SRAM Retention in Low Power Modes with RTC Enabled
  - Multiple Peripherals for System Control

    - Three QSPI Master/Slave with Three Chip Selects Each
    - Three 4-Wire UARTs
    - Three I2C Master/Slave
    - Up to 50 GPIO
    - QSPI (SPIXF) with Real-Time Flash Decryption
    - QSPI (SPIXR) RAM Interface Provides SRAMExpansion
    - 8-Input 10-Bit Delta-Sigma ADC 7.8ksps
    - USB 2.0 HS Engine with Internal Transceiver
    - PDM Interface Supports Two Digital Microphones
    - I2S with TDM
    - Six 32-Bit Timers
    - Two High-Speed Timers
    - 1-Wire Master
    - Sixteen Pulse Trains (PWM)
    - Secure Digital Interface Supports SD3.0/SDIO3.0/eMMC4.51
  - Secure Valuable IP/Data with Hardware Security

    - Trust Protection Unit (TPU) with MAA SupportsFast ECDSA and Modular Arithmetic
    - AES128/192/256, DES, 3DES, Hardware Accelerator
    - TRNG Seed Generator
    - SHA-2 Accelerator•Secure Bootloader
- Benefits and Features of MAX32666EVKIT:

  - Bluetooth SMA connector with a 2.4GHz Hinged Whip Antenna
  - 1.28in 128 x 128 Monochrome TFT Display
  - 64MB XIP Flash
  - 1MB XIP RAM
  - Stereo Audio Codec with Line-In and Line-Out 3.5mm Jacks
  - Digital Audio Microphone
  - USB 2.0 Micro B Interface
  - USB 2.0 Micro B to Serial UARTs
  - Micro SD Card Interface
  - Select GPIOs Accessed Through a 0.1in Header
  - Access to the 8 Analog Inputs Through a 0.1in Header
  - Arm® or SWD JTAG 20-Pin Header
  - 1-Wire RJ11 Port
  - Can Be Solely Sourced by a Coin Cell Battery
  - Board Power Provided by Either USB Port
  - Individual Power Measurement on All IC Rails Through Jumpers
  - On-Board 1.8V and 3.3V Regulators
  - Two General-Purpose LEDs and Two General-Purpose Pushbutton Switches

### Supported Features

The `max32666evkit` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `max32666evkit/max32666/cpu0` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L25) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | ADI MAX32 ADC 10-Bits[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L230) | [`adi,max32-adc-10b`](../../../../build/dts/api/bindings/adc/adi%2Cmax32-adc-10b.md#std-dtcompatible-adi-max32-adc-10b) |
| Clock control | on-chip | MAX32 Global Control[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L118) | [`adi,max32-gcr`](../../../../build/dts/api/bindings/clock/adi%2Cmax32-gcr.md#std-dtcompatible-adi-max32-gcr) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L53)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L60) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | ADI MAX32 counter[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L250) | [`adi,max32-counter`](../../../../build/dts/api/bindings/counter/adi%2Cmax32-counter.md#std-dtcompatible-adi-max32-counter) |
| on-chip | ADI MAX32 compatible Counter RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L318) | [`adi,max32-rtc-counter`](../../../../build/dts/api/bindings/counter/adi%2Cmax32-rtc-counter.md#std-dtcompatible-adi-max32-rtc-counter) |
| DMA | on-chip | ADI MAX32 DMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L100)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L110) | [`adi,max32-dma`](../../../../build/dts/api/bindings/dma/adi%2Cmax32-dma.md#std-dtcompatible-adi-max32-dma) |
| Flash controller | on-chip | MAX32XXX flash controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L102) | [`adi,max32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/adi%2Cmax32-flash-controller.md#std-dtcompatible-adi-max32-flash-controller) |
| GPIO & Headers | on-chip | MAX32 GPIO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L166) | [`adi,max32-gpio`](../../../../build/dts/api/bindings/gpio/adi%2Cmax32-gpio.md#std-dtcompatible-adi-max32-gpio) |
| I2C | on-chip | ADI MAX32 I2C[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L138)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L127) | [`adi,max32-i2c`](../../../../build/dts/api/bindings/i2c/adi%2Cmax32-i2c.md#std-dtcompatible-adi-max32-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32666evkit/max32666evkit_max32666_cpu0.dts?plain=1#L38) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32666evkit/max32666evkit_max32666_cpu0.dts?plain=1#L26) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L110) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | MAX32 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L160) | [`adi,max32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/adi%2Cmax32-pinctrl.md#std-dtcompatible-adi-max32-pinctrl) |
| PWM | on-chip | ADI MAX32 PWM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L254) | [`adi,max32-pwm`](../../../../build/dts/api/bindings/pwm/adi%2Cmax32-pwm.md#std-dtcompatible-adi-max32-pwm) |
| RNG | on-chip | ADI MAX32XXX TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L214) | [`adi,max32-trng`](../../../../build/dts/api/bindings/rng/adi%2Cmax32-trng.md#std-dtcompatible-adi-max32-trng) |
| SDHC | on-chip | ADI MAX32 SDHC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L178) | [`adi,max32-sdhc`](../../../../build/dts/api/bindings/sdhc/adi%2Cmax32-sdhc.md#std-dtcompatible-adi-max32-sdhc) |
| Serial controller | on-chip | MAX32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L196)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L187) | [`adi,max32-uart`](../../../../build/dts/api/bindings/serial/adi%2Cmax32-uart.md#std-dtcompatible-adi-max32-uart) |
| SPI | on-chip | ADI MAX32 SPI[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L120) | [`adi,max32-spi`](../../../../build/dts/api/bindings/spi/adi%2Cmax32-spi.md#std-dtcompatible-adi-max32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L97) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | ADI MAX32 timer[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L242) | [`adi,max32-timer`](../../../../build/dts/api/bindings/timer/adi%2Cmax32-timer.md#std-dtcompatible-adi-max32-timer) |
| 1-Wire | on-chip | ADI MAX32xxx MCUs 1-Wire Master[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32666.dtsi?plain=1#L170) | [`adi,max32-w1`](../../../../build/dts/api/bindings/w1/adi%2Cmax32-w1.md#std-dtcompatible-adi-max32-w1) |
| Watchdog | on-chip | MAX32XXX watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L221) | [`adi,max32-watchdog`](../../../../build/dts/api/bindings/watchdog/adi%2Cmax32-watchdog.md#std-dtcompatible-adi-max32-watchdog) |

### Connections and IOs

| Name | Name | Settings | Description |
| --- | --- | --- | --- |
| JP1 | I2C0\_SCL/SDA | | Open | | --- | | Close | | | Disconnects I2C0 SCL and SDA 1.5K pullups from VDDIOH. | | --- | | Connects I2C0 SCL and SDA 1.5K pullups to VDDIOH. | |
| JP2 | I2C1\_SCL/SDA | | Open | | --- | | Close | | | Disconnects I2C1 SCL and SDA 1.5K pullups from VDDIOH. | | --- | | Connects I2C1 SCL and SDA 1.5K pullups to VDDIOH. | |
| JP3 | I2C2\_SCL/SDA | | Open | | --- | | Close | | | Disconnects I2C2 SCL and SDA 1.5K pullups from VDDIOH. | | --- | | Connects I2C2 SCL and SDA 1.5K pullups to VDDIOH. | |
| JP4 | P1\_14 | | Open | | --- | | Close | | | Disconnects LED D2 from P1\_14. | | --- | | Connects LED D2 to P1\_14. | |
| JP5 | P1\_15 | | Open | | --- | | Close | | | Disconnects LED D3 from P1\_15. | | --- | | Connects LED D3 to P1\_15. | |
| JP6 | VBUS | | 2-1 | | --- | | 2-3 | | | Connects VBUS to USB connector CN1 to supply board power. | | --- | | Connects VBUS to USB connector CN2 to supply board power. | |
| JP7 | N/A | N/A | N/A |
| JP8 | N/A | N/A | N/A |
| JP9 | | P0\_20 | | --- | | P0\_28 | | | 2-1 | | --- | | 2-3 | | | Connects the USB to serial UART to GPIO P0\_20 (RX1). | | --- | | Connects the USB to serial UART to GPIO P0\_28 (RX2). | |
| JP10 | | P0\_21 | | --- | | P0\_29 | | | 2-1 | | --- | | 2-3 | | | Connects the USB to serial UART to GPIO P0\_21 (TX1). | | --- | | Connects the USB to serial UART to GPIO P0\_29 (TX2). | |
| JP11 | | P0\_22 | | --- | | P0\_30 | | | 2-1 | | --- | | 2-3 | | | Connects the USB to serial UART to GPIO P0\_22 (CTS1\_N). | | --- | | Connects the USB to serial UART to GPIO P0\_30 (CTS2\_N). | |
| JP12 | | P0\_23 | | --- | | P0\_31 | | | 2-1 | | --- | | 2-3 | | | Connects the USB to serial UART to GPIO P0\_23 (RTS1\_N). | | --- | | Connects the USB to serial UART to GPIO P0\_31 (RTS2\_N). | |
| JP13 | VREGI | | 2-1 | | --- | | 2-3 | | | Connects VREGI to the coin cell battery. | | --- | | Connects VREGI to 3V3. | |
| JP14 | VDDIOH | | 1-2 | | --- | | 3-4 | | 5-6 | | | Connects VDDIOH to VREGO\_A | | --- | | Connects VDDIOH to 1V8. | | Connects VDDIOH to 3V3. | |
| JP15 | VDDIOH | | Open | | --- | | Close | | | Disconnects power from VDDIOH. | | --- | | Connects power to VDDIOH. | |
| JP16 | VDDB | | Open | | --- | | Close | | | Disconnects power from VDDB. | | --- | | Connects power to VDDB. | |
| JP17 | VDDIO | | 2-1 | | --- | | 2-3 | | | Connects VDDIO to VREGO\_A. | | --- | | Connects VDDIO to 1V8. | |
| JP18 | VDDIO | | Open | | --- | | Close | | | Disconnects power from VDDIO. | | --- | | Connects power to VDDIO. | |
| JP19 | VDDA | | Open | | --- | | Close | | | Disconnects power from VDDA. | | --- | | Connects power to VDDA. | |
| JP20 | VCORE\_A | | Open | | --- | | Close | | | Disconnects power from VCORE\_A. | | --- | | Connects power to VCORE\_A. | |
| JP21 | VCORE\_B | | Open | | --- | | Close | | | Disconnects power from VCORE\_B. | | --- | | Connects power to VCORE\_B. | |
| JP22 | VTXIN | | Open | | --- | | Close | | | Disconnects power from VTXIN. | | --- | | Connects power to VTXIN. | |
| JP23 | VRXIN | | Open | | --- | | Close | | | Disconnects power from VRXIN. | | --- | | Connects power to VRXIN. | |

## Programming and Debugging

The `max32666evkit` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Flashing

The MAX32666 MCU can be flashed by connecting an external debug probe to the
SWD port. SWD debug can be accessed through the Cortex 10-pin connector, J6.
Logic levels are fixed to VDDIOH (1.8V or 3.3V).

Once the debug probe is connected to your host computer, then you can simply run the
`west flash` command to write a firmware image into flash. To perform a full erase,
pass the `--erase` option when executing `west flash`.

Note

This board uses OpenOCD as the default debug interface. You can also use
a Segger J-Link with Segger’s native tooling by overriding the runner,
appending `--runner jlink` to your `west` command(s). The J-Link should
be connected to the standard 20-pin connector (J7) or a Cortex® 10-pin connector (J6).

### Debugging

Please refer to the [Flashing](#flashing) section and run the `west debug` command
instead of `west flash`.

## References

- [MAX32666EVKIT web page](https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/MAX32666EVKIT.html)

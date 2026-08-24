---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/adi/max78000evkit/doc/index.html
original_path: boards/adi/max78000evkit/doc/index.html
---

# MAX78000EVKIT

Board Overview

[![../../../../_images/max78000evkit.webp](https://docs.zephyrproject.org/4.2.0/_images/max78000evkit.webp)
](https://docs.zephyrproject.org/4.2.0/_images/max78000evkit.webp)

MAX78000EVKIT

Name:
:   `max78000evkit`

Vendor:
:   Analog Devices, Inc.

Architecture:
:   arm

SoC:
:   max78000

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adi/max78000evkit/doc/index.rst/../..)

## Overview

The MAX78000 evaluation kit (EV kit) provides a platform for leveraging the capabilities of the MAX78000 to build
new generations of artificial intelligence (AI) devices. Onboard hardware includes a digital microphone, a gyroscope/accelerometer, parallel camera module support
and a 3.5in touch-enabled color TFT display. A secondary display is driven by a power accumulator for tracking
device power consumption over time. Uncommitted GPIO as well as analog inputs are readily accessible through
0.1in pin headers. Primary system power as well as UART access is provided by a USB Micro-B connector. A USB
to SPI bridge provides rapid access to onboard memory, allowing large networks or images to load quickly

The Zephyr port is running on the MAX78000 MCU.

## Hardware

- MAX78000 MCU:

  - Dual-Core, Low-Power Microcontroller

    - Arm Cortex-M4 Processor with FPU up to 100MHz
    - 512KB Flash and 128KB SRAM
    - Optimized Performance with 16KB Instruction Cache
    - Optional Error Correction Code (ECC-SEC-DED) for SRAM
    - 32-Bit RISC-V Coprocessor up to 60MHz
    - Up to 52 General-Purpose I/O Pins
    - 12-Bit Parallel Camera Interface
    - One I2S Master/Slave for Digital Audio Interface
  - Neural Network Accelerator

    - Highly Optimized for Deep Convolutional Neural Networks
    - 442k 8-Bit Weight Capacity with 1,2,4,8-Bit Weights
    - Programmable Input Image Size up to 1024 x 1024 pixels
    - Programmable Network Depth up to 64 Layers
    - Programmable per Layer Network Channel Widths up to 1024 Channels
    - 1 and 2 Dimensional Convolution Processing
    - Streaming Mode
    - Flexibility to Support Other Network Types, Including MLP and Recurrent Neural Networks
  - Power Management Maximizes Operating Time for Battery Applications

    - Integrated Single-Inductor Multiple-Output (SIMO) Switch-Mode Power Supply (SMPS)
    - 2.0V to 3.6V SIMO Supply Voltage Range
    - Dynamic Voltage Scaling Minimizes Active Core Power Consumption
    - 22.2μA/MHz While Loop Execution at 3.0V from Cache (CM4 Only)
    - Selectable SRAM Retention in Low-Power Modes with Real-Time Clock (RTC) Enabled
  - Security and Integrity

    - Available Secure Boot
    - AES 128/192/256 Hardware Acceleration Engine
    - True Random Number Generator (TRNG) Seed Generator

### Supported Features

The `max78000evkit` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `max78000evkit/max78000/m4` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L25) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | ADI MAX32 ADC 10-Bits[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L230) | [`adi,max32-adc-10b`](../../../../build/dts/api/bindings/adc/adi,max32-adc-10b.md#std-dtcompatible-adi-max32-adc-10b) |
| Clock control | on-chip | MAX32 Global Control[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L118) | [`adi,max32-gcr`](../../../../build/dts/api/bindings/clock/adi,max32-gcr.md#std-dtcompatible-adi-max32-gcr) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L53)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L60) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | ADI MAX32 counter[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L250) | [`adi,max32-counter`](../../../../build/dts/api/bindings/counter/adi,max32-counter.md#std-dtcompatible-adi-max32-counter) |
| on-chip | ADI MAX32 compatible Counter RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L318) | [`adi,max32-rtc-counter`](../../../../build/dts/api/bindings/counter/adi,max32-rtc-counter.md#std-dtcompatible-adi-max32-rtc-counter) |
| DMA | on-chip | ADI MAX32 DMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max78000.dtsi?plain=1#L91) | [`adi,max32-dma`](../../../../build/dts/api/bindings/dma/adi,max32-dma.md#std-dtcompatible-adi-max32-dma) |
| Flash controller | on-chip | MAX32XXX flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L102) | [`adi,max32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/adi,max32-flash-controller.md#std-dtcompatible-adi-max32-flash-controller) |
| GPIO & Headers | on-chip | MAX32 GPIO[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L166) | [`adi,max32-gpio`](../../../../build/dts/api/bindings/gpio/adi,max32-gpio.md#std-dtcompatible-adi-max32-gpio) |
| I2C | on-chip | ADI MAX32 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L127)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L138) | [`adi,max32-i2c`](../../../../build/dts/api/bindings/i2c/adi,max32-i2c.md#std-dtcompatible-adi-max32-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max78000evkit/max78000evkit_max78000_m4.dts?plain=1#L39) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max78000evkit/max78000evkit_max78000_m4.dts?plain=1#L25) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L110) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | MAX32 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L160) | [`adi,max32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/adi,max32-pinctrl.md#std-dtcompatible-adi-max32-pinctrl) |
| PWM | on-chip | ADI MAX32 PWM[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L254) | [`adi,max32-pwm`](../../../../build/dts/api/bindings/pwm/adi,max32-pwm.md#std-dtcompatible-adi-max32-pwm) |
| RNG | on-chip | ADI MAX32XXX TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L214) | [`adi,max32-trng`](../../../../build/dts/api/bindings/rng/adi,max32-trng.md#std-dtcompatible-adi-max32-trng) |
| Serial controller | on-chip | MAX32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L187)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L196) | [`adi,max32-uart`](../../../../build/dts/api/bindings/serial/adi,max32-uart.md#std-dtcompatible-adi-max32-uart) |
| SPI | on-chip | ADI MAX32 SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max78000.dtsi?plain=1#L71)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max78000.dtsi?plain=1#L81) | [`adi,max32-spi`](../../../../build/dts/api/bindings/spi/adi,max32-spi.md#std-dtcompatible-adi-max32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L97) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | ADI MAX32 timer[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L242) | [`adi,max32-timer`](../../../../build/dts/api/bindings/timer/adi,max32-timer.md#std-dtcompatible-adi-max32-timer) |
| 1-Wire | on-chip | ADI MAX32xxx MCUs 1-Wire Master[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max78000.dtsi?plain=1#L101) | [`adi,max32-w1`](../../../../build/dts/api/bindings/w1/adi,max32-w1.md#std-dtcompatible-adi-max32-w1) |
| Watchdog | on-chip | MAX32XXX watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L221)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max78000.dtsi?plain=1#L109) | [`adi,max32-watchdog`](../../../../build/dts/api/bindings/watchdog/adi,max32-watchdog.md#std-dtcompatible-adi-max32-watchdog) |

### Connections and IOs

| Name | Name | Settings | Description |
| --- | --- | --- | --- |
| JP1 | LED1 EN | | 1-2 | | --- | | Open | | | Enables auxiliary LED1 | | --- | | Disables auxiliary LED1 | |
| JP2 | LED2 EN | | 1-2 | | --- | | Open | | | Enables auxiliary LED2 | | --- | | Disables auxiliary LED2 | |
| JP3 | TRIG1 | | 1-2 | | --- | | Open | | | Enables power monitor event trigger 1 | | --- | | Disables power monitor event trigger 1 | |
| JP4 | TRIG2 | | 1-2 | | --- | | Open | | | Enables power monitor event trigger 2 | | --- | | Disables power monitor event trigger 2 | |
| JP5 | VREGI | | 1-2 | | --- | | Open | | | Enables 3V3 VREGI power | | --- | | Disables 3V3 VREGI power | |
| JP6 | VREGIA | | 1-2 | | --- | | Open | | | Enables 3V3 VREGIA power | | --- | | Disables 3V3 VREGIA power | |
| JP7 | CNN BOOST | | 1-2 | | --- | | Open | | | Enables 1V1 boost LDO power | | --- | | Disables 1V1 boost LDO power | |
| JP8 | VDDA | | 1-2 | | --- | | 2-3 | | | Internal SIMO powers VDDA | | --- | | External LDO powers VDDA | |
| JP9 | VDDIO | | 1-2 | | --- | | 2-3 | | | Internal SIMO powers VDDIO | | --- | | External LDO powers VDDIO | |
| JP10 | VDDIOH | | 1-2 | | --- | | 2-3 | | | DUT LDO powers VDDIOH | | --- | | AUX LDO powers VDDIOH | |
| JP11 | VCOREB | | 1-2 | | --- | | 2-3 | | | Internal SIMO powers VCOREB | | --- | | External LDO powers VCOREB | |
| JP12 | VCOREA | | 1-2 | | --- | | 2-3 | | | Internal SIMO powers VCOREA | | --- | | External LDO powers VCOREA | |
| JP13 | VREGI PM BYPASS | | 1-2 | | --- | | Open | | | Bypasses power monitor shunt | | --- | | Enables power monitoring using power accumulator | |
| JP14 | CNN 1V1 | | 1-2 | | --- | | Open | | | Connects 1V1 boost LDO to VCOREA | | --- | | Disables 1V1 boost LDO | |
| JP15 | VCOREA PM BYPASS | | 1-2 | | --- | | Open | | | Bypasses power monitor shunt | | --- | | Enables power monitoring using power accumulator | |
| JP16 | VCOREB PM BYPASS | | 1-2 | | --- | | Open | | | Bypasses power monitor shunt | | --- | | Enables power monitoring using power accumulator | |
| JP17 | VREG\_A PM BYPASS | | 1-2 | | --- | | Open | | | Bypasses power monitor shunt | | --- | | Enables power monitoring using power accumulator | |
| JP18 | RESET EN | | 1-2 | | --- | | Open | | | Enables RV JTAG adapter to perform full system reset | | --- | | Disables system reset by RV JTAG adapter | |
| JP19 | TFT BL | | 1-2 | | --- | | Open | | | Enables main TFT screen backlight | | --- | | Disables main TFT screen backlight | |
| JP20 | I2S CLK SEL | | 1-2 | | --- | | 2-3 | | | Onboard 12.288MHz oscillator drives I2S clock | | --- | | External 1V8 CMOS LEVEL source drives I2S clock | |
| JP21 | DUT I | | 1-2 | | --- | | Open | | | DUT 3V3 total current monitor point | | --- | | Open to insert current meter | |
| JP22 | USB-SPI/CAM | | 1-2 | | --- | | 2-3 | | | Enables USB-SPI bridge | | --- | | Enables camera | |
| JH1 | UART 0 EN | | 1-2, 3-4 | | --- | | All Open | | | Enables USB-UART0 bridge, software flow control | | --- | | Disables USB-UART0 bridge, allows reuse of port pins | |
| JH2 | UART 1 EN | | All installed | | --- | | All Open | | | Enables USB-UART1 bridge | | --- | | Disables USB-UART1 bridge, allows reuse of port pins | |

## Programming and Debugging

The `max78000evkit` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Flashing

The MAX78000 MCU can be flashed by connecting an external debug probe to the
SWD port. SWD debug can be accessed through the Cortex 10-pin connector, JH5.
Logic levels are fixed to VDDIO (1.8V).

Once the debug probe is connected to your host computer, then you can simply run the
`west flash` command to write a firmware image into flash. To perform a full erase,
pass the `--erase` option when executing `west flash`.

Note

This board uses OpenOCD as the default debug interface. You can also use
a Segger J-Link with Segger’s native tooling by overriding the runner,
appending `--runner jlink` to your `west` command(s). The J-Link should
be connected to the standard 2\*5 pin debug connector (JH5) using an
appropriate adapter board and cable.

### Debugging

Please refer to the [Flashing](#flashing) section and run the `west debug` command
instead of `west flash`.

## References

- [MAX78000EVKIT web page](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/max78000evkit.html)

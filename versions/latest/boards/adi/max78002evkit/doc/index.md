---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/adi/max78002evkit/doc/index.html
original_path: boards/adi/max78002evkit/doc/index.html
---

# MAX78002EVKIT

Board Overview

[![../../../../_images/max78002evkit.webp](https://docs.zephyrproject.org/4.2.0/_images/max78002evkit.webp)
](https://docs.zephyrproject.org/4.2.0/_images/max78002evkit.webp)

MAX78002EVKIT

Name:
:   `max78002evkit`

Vendor:
:   Analog Devices, Inc.

Architecture:
:   arm

SoC:
:   max78002

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adi/max78002evkit/doc/index.rst/../..)

## Overview

The MAX78002 evaluation kit (EV kit) provides a platform and tools for leveraging device capabilities to build new
generations of artificial intelligence (AI) products.

The kit provides optimal versatility with a modular peripheral architecture, allowing a variety of input and output
devices to be remotely located. DVP and CSI cameras, I2S audio peripherals, digital microphones, and analog sensors
are supported, while a pair of industry-standard QWIIC connectors supports a large and growing array of aftermarket
development boards. An onboard stereo audio codec offers line-level audio input and output, and tactile input is
provided by a touch-enabled 2.4in TFT display. The MAX78002 energy consumption is tracked by a power accumulator,
with four channels of formatted results presented on a secondary TFT display. All device GPIOs are accessible on
0.1in pin headers. A standard coaxial power jack serves as power input, using the included 5V, 3A wall-mount
adapter. Two USB connectors provide serial access to the MAX78002, one directly and the other through a USB to UART
bridge. A third USB connector allows access to the MAX78002 energy consumption data. Rounding out the features, a
microSD connector provides the capability for inexpensive highdensity portable data storage.

The Zephyr port is running on the MAX78002 MCU.

![MAX78002 EVKIT Front](https://docs.zephyrproject.org/4.2.0/_images/max78002evkit1.webp)
![MAX78002 EVKIT Back](https://docs.zephyrproject.org/4.2.0/_images/max78002evkit_back.webp)

## Hardware

- MAX78002 MCU:

  - Dual-Core, Low-Power Microcontroller

    - Arm Cortex-M4 Processor with FPU up to 120MHz
    - 2.5MB Flash, 64KB ROM, and 384KB SRAM
    - Optimized Performance with 16KB Instruction Cache
    - Optional Error Correction Code (ECC SEC-DED) for SRAM
    - 32-Bit RISC-V Coprocessor up to 60MHz
    - Up to 60 General-Purpose I/O Pins
    - MIPI Camera Serial Interface 2 (MIPI CSI-2) Controller V2.1
    - Support for Two Data Lanes
    - 12-Bit Parallel Camera Interface
    - I2S Controller/Target for Digital Audio Interface
    - Secure Digital Interface Supports SD 3.0/SDIO 3.0/eMMC 4.51
  - Convolutional Neural Network (CNN) Accelerator

    - Highly Optimized for Deep CNNs
    - 2 Million 8-Bit Weight Capacity with 1-, 2-, 4-, and 8-bit Weights
    - 1.3MB CNN Data Memory
    - Programmable Input Image Size up to 2048 x 2048 Pixels
    - Programmable Network Depth up to 128 Layers
    - Programmable per Layer Network Channel Widths up to 1024 Channels
    - 1- and 2-Dimensional Convolution Processing
    - Capable of Processing VGA Images at 30fps
  - Power Management for Extending Battery Life

    - Integrated Single-Inductor Multiple-Output (SIMO) Switch-Mode Power Supply (SMPS)
    - 2.85V to 3.6V Supply Voltage Range
    - Support of Optional External Auxiliary CNN Power Supply
    - Dynamic Voltage Scaling Minimizes Active Core Power Consumption
    - 23.9μA/MHz While Loop Execution at 3.3V from Cache (CM4 only)
    - Selectable SRAM Retention in Low-Power Modes with Real-Time Clock (RTC) Enabled
  - Security and Integrity

    - Available Secure Boot
    - AES 128/192/256 Hardware Acceleration Engine
    - True Random Number Generator (TRNG) Seed Generator
- External devices connected to the MAX78002 EVKIT:

  - Color TFT Display
  - Audio Stereo Codec Interface
  - Digital Microphone
  - A 8Mb QSPI ram

### Supported Features

The `max78002evkit` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `max78002evkit/max78002/m4` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L25) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | ADI MAX32 ADC SAR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L230) | [`adi,max32-adc-sar`](../../../../build/dts/api/bindings/adc/adi,max32-adc-sar.md#std-dtcompatible-adi-max32-adc-sar) |
| Clock control | on-chip | MAX32 Global Control[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L118) | [`adi,max32-gcr`](../../../../build/dts/api/bindings/clock/adi,max32-gcr.md#std-dtcompatible-adi-max32-gcr) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L53)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L60) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | ADI MAX32 counter[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L250) | [`adi,max32-counter`](../../../../build/dts/api/bindings/counter/adi,max32-counter.md#std-dtcompatible-adi-max32-counter) |
| on-chip | ADI MAX32 compatible Counter RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L318) | [`adi,max32-rtc-counter`](../../../../build/dts/api/bindings/counter/adi,max32-rtc-counter.md#std-dtcompatible-adi-max32-rtc-counter) |
| DMA | on-chip | ADI MAX32 DMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max78002.dtsi?plain=1#L146) | [`adi,max32-dma`](../../../../build/dts/api/bindings/dma/adi,max32-dma.md#std-dtcompatible-adi-max32-dma) |
| Flash controller | on-chip | MAX32XXX flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L102) | [`adi,max32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/adi,max32-flash-controller.md#std-dtcompatible-adi-max32-flash-controller) |
| GPIO & Headers | on-chip | MAX32 GPIO[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L166) | [`adi,max32-gpio`](../../../../build/dts/api/bindings/gpio/adi,max32-gpio.md#std-dtcompatible-adi-max32-gpio) |
| I2C | on-chip | ADI MAX32 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L127)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L138) | [`adi,max32-i2c`](../../../../build/dts/api/bindings/i2c/adi,max32-i2c.md#std-dtcompatible-adi-max32-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max78002evkit/max78002evkit_max78002_m4.dts?plain=1#L37) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max78002evkit/max78002evkit_max78002_m4.dts?plain=1#L25) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L110) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | MAX32 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L160) | [`adi,max32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/adi,max32-pinctrl.md#std-dtcompatible-adi-max32-pinctrl) |
| PWM | on-chip | ADI MAX32 PWM[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L254) | [`adi,max32-pwm`](../../../../build/dts/api/bindings/pwm/adi,max32-pwm.md#std-dtcompatible-adi-max32-pwm) |
| RNG | on-chip | ADI MAX32XXX TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L214) | [`adi,max32-trng`](../../../../build/dts/api/bindings/rng/adi,max32-trng.md#std-dtcompatible-adi-max32-trng) |
| Serial controller | on-chip | MAX32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L187)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L196) | [`adi,max32-uart`](../../../../build/dts/api/bindings/serial/adi,max32-uart.md#std-dtcompatible-adi-max32-uart) |
| SPI | on-chip | ADI MAX32 SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max78002.dtsi?plain=1#L126)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max78002.dtsi?plain=1#L136) | [`adi,max32-spi`](../../../../build/dts/api/bindings/spi/adi,max32-spi.md#std-dtcompatible-adi-max32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L97) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | ADI MAX32 timer[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L242) | [`adi,max32-timer`](../../../../build/dts/api/bindings/timer/adi,max32-timer.md#std-dtcompatible-adi-max32-timer) |
| 1-Wire | on-chip | ADI MAX32xxx MCUs 1-Wire Master[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max78002.dtsi?plain=1#L203) | [`adi,max32-w1`](../../../../build/dts/api/bindings/w1/adi,max32-w1.md#std-dtcompatible-adi-max32-w1) |
| Watchdog | on-chip | MAX32XXX watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L221)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max78002.dtsi?plain=1#L156) | [`adi,max32-watchdog`](../../../../build/dts/api/bindings/watchdog/adi,max32-watchdog.md#std-dtcompatible-adi-max32-watchdog) |

### Connections and IOs

| Name | Name | Settings | Description |
| --- | --- | --- | --- |
| JP1 | 3V3 MON | | 1-2 | | --- | | Open | | | Normal operation in conjunction with JP3 jumpered 1-2 | | --- | | Test access point for current measurement | |
| JP2 | 3V3 SW PM BYPASS | | 1-2 | | --- | | Open | | | Power monitor shunts for main 3.3 V system power are bypassed | | --- | | Main 3.3V input routes through shunts for power accumulator measurements | |
| JP3 | CNN MON | | 1-2 | | --- | | Open | | | Normal operation in conjunction with JP6 jumpered 1-2 | | --- | | Test access point for current measurement of U4’s share of VCOREA and CNN loads | |
| JP4 | VCOREA PM BYPASS | | 1-2 | | --- | | Open | | | Power monitor shunts for U4’s share of VCOREA + CNN loads are bypassed | | --- | | VCOREA + CNN loads route through shunts for power accumulator | |
| JP5 | VCOREB PM BYPASS | | 1-2 | | --- | | Open | | | Power monitor shunts for VCOREB are bypassed | | --- | | VCOREB power routes through shunts for power accumulator | |
| JP6 | VREGO\_A PM BYPASS | | 1-2 | | --- | | Open | | | Power monitor shunts for VREGO\_A are bypassed | | --- | | VREGO\_A power routes through shunts for power accumulator | |
| JP7 | VBAT | | 1-2 | | --- | | Open | | | Enables 3V3 VBAT power | | --- | | Disables 3V3 VBAT power | |
| JP8 | VREGI | | 1-2 | | --- | | Open | | | Enables 3V3 VREGI power | | --- | | Disables 3V3 VREGI power | |
| JP9 | VREGI/VBAT | | 2-1 | | --- | | 2-3 | | | Onboard 3V3\_PM supplies VREGI/VBAT | | --- | | External source at TP10 supplies VREGI/VBAT | |
| JP10 | VDDIOH | | 2-1 | | --- | | 2-3 | | | Onboard 3V3\_PM supplies VDDIOH | | --- | | Onboard 3V3\_SW supplies VDDIOH | |
| JP11 | VDDA | | 1-2 | | --- | | Open | | | VREGO\_A\_PM powers VDDA | | --- | | VDDA may be powered using TP6 | |
| JP12 | VDDIO | | 1-2 | | --- | | Open | | | VREGO\_A\_PM powers VDDIO | | --- | | VDDIO may be powered using TP7 | |
| JP13 | VCOREB | | 1-2 | | --- | | Open | | | VREGO\_B powers VCOREB | | --- | | VCOREB may be powered using TP8 | |
| JP14 | VCOREA | | 1-2 | | --- | | Open | | | VREGO\_C ties to net VCOREA | | --- | | Net VCOREA may be powered using TP9; JP17 may also be used as a current test point | |
| JP15 | VREF | | 1-2 | | --- | | Open | | | DUT ADC VREF is supplied by precision external reference | | --- | | External ADC VREF disabled; ref voltage may be injected at JP18.1 | |
| JP16 | I2C1 SDA | | 1-2 | | --- | | Open | | | I2C1 DATA pullup | | --- | | Close this jumper as needed to assure proper termination | |
| JP17 | I2C1 SCL | | 1-2 | | --- | | Open | | | I2C1 CLOCK pullup | | --- | | Close this jumper as needed to assure proper termination | |
| JP18 | TRIG1 | | 1-2 | | --- | | Open | | | PWR accumulator trigger signal 1 ties to port 1.6 | | --- | | TRIG1 is disabled, so DVP camera PCIF\_D10 may be used instead | |
| JP19 | TRIG2 | | 1-2 | | --- | | Open | | | PWR accumulator trigger signal 2 ties to port 1.7 | | --- | | TRIG2 is disabled, so DVP camera PCIF\_D11 may be used instead | |
| JP20 | UART0 EN | | Closed | | --- | | Open | | | USB-UART bridge connected to DUT UART0 (RTS and CTS are supported) | | --- | | USB-UART bridge disconnected from DUT UART0 | |
| JP21 | I2C0\_SDA | | 1-2 | | --- | | Open | | | I2C0 DATA pull-up | | --- | | Close this jumper as needed to assure proper termination | |
| JP22 | I2C0\_SCL | | 1-2 | | --- | | Open | | | I2C0 CLOCK pull-up | | --- | | Close this jumper as needed to assure proper termination | |
| JP23 | UART1 EN | | Closed | | --- | | Open | | | USB-UART bridge connected to DUT UART1 (no HW flow control) | | --- | | USB-UART bridge disconnected from DUT UART1 | |
| JP24 | EXT I2C0 EN | | 1-2 | | --- | | Open | | | QWIIC interface for I2C0 enabled by default | | --- | | Open this jumper to place the QWIIC level translator into a high-Z state | |
| JP25 | PB1 PU | | 1-2 | | --- | | Open | | | 100kΩ pull-up enabled for pushbutton mode, port 2.6 | | --- | | Pull-up disabled, allowing port pin to be repurposed (this port shared with AIN6) | |
| JP26 | PB2 PU | | 1-2 | | --- | | Open | | | 100kΩ pull-up enabled for pushbutton mode, port 2.7 | | --- | | Pull-up disabled, allowing port pin to be repurposed (this port shared with AIN7) | |
| JP27 | I2C2 SDA | | 1-2 | | --- | | Open | | | I2C2 DATA pull-up | | --- | | Close this jumper as needed to assure proper termination | |
| JP28 | I2C2 SCL | | 1-2 | | --- | | Open | | | I2C2 CLOCK pull-up | | --- | | Close this jumper as needed to assure proper termination | |
| JP29 | VDDB | | 2-1 | | --- | | 2-3 | | | DUT USB XCVR VDDB powered from VBUS regulated with dedicated 3.3V LDO | | --- | | USB XCVR VDDB powered full time by system 3V3\_PM | |
| JP30 | EXT I2C2 EN | | 1-2 | | --- | | Open | | | QWIIC interface for I2C2 enabled by default | | --- | | Open this jumper to place the QWIIC level translator into a high-Z state | |
| JP31 | L/R SEL | | 1-2 | | --- | | Open | | | MIC ON R CH, I2S microphone data stream | | --- | | MIC ON L CH, I2S microphone data stream | |
| JP32 | MIC-I2S I/O | | 1-2 | | --- | | Open | | | External I2S data from I2S I/O header connected to I2S SDI. | | --- | | External MIC data from I2S MIC header connected to I2S SDI | |
| JP33 | MIC-I2S/CODEC | | 1-2 | | --- | | Open | | | Onboard CODEC data connects to I2S SDI | | --- | | External I2S data (mic or slave I2S) from header connects to I2S SDI | |
| JP34 | I2S VDD | | 2-1 | | --- | | 2-3 | | | External MIC and DATA I2S interface headers run at 1.8V | | --- | | External MIC and DATA I2S interface headers run at 3.3V | |
| JP35 | I2C1 SDA | | 1-2 | | --- | | Open | | | I2C1 DATA pull-up | | --- | | Close this jumper as needed to assure proper termination | |
| JP36 | I2C1 SCL | | 1-2 | | --- | | Open | | | I2C1 CLOCK pull-up | | --- | | Close this jumper as needed to assure proper termination | |
| JP37 | I2S CK SEL | | 1-2 | | --- | | Open | | | I2S master clock sourced from SMA connector J6 | | --- | | I2S master clock sourced from onboard crystal oscillator | |
| JP38 | DVP CAM PWR | | 2-1 | | --- | | 2-3 | | | Sets state of DVP camera PWDN input; default is OFF for OVM7692 | | --- | | Sets state of DVP camera PWDN input; 2-3 will power up OVM7692 | |
| JP39 | SW CAM PWUP | | 1-2 | | --- | | Open | | | Camera reset and power up under port pin control | | --- | | Digilent P5C camera powered down, JP39 can over ride this condition | |
| JP40 | HW PWUP / SW PWUP | | 1-2 | | --- | | Open | | | Camera will reset and power up as soon as 3.3V reaches a valid level | | --- | | Camera reset and power up under port pin control if JP39 is installed; else, camera off | |
| JP41 | CSI CAM I2C EN | | 1-2 | | --- | | Open | | | CSI camera Digilent P5C I2C connects to I2C1 for register setup | | --- | | Level translator and I2C PU are in high-Z state; I2C1 disconnected from P5C registers | |
| JP42 | TFT DC | | 1-2 | | --- | | Open | | | TFT data/command select connects to port 2.2 | | --- | | Pull jumper if using AIN2 | |
| JP43 | TFT CS | | 2-1 | | --- | | 2-3 | | | TFT CS driven by port 0.3, shared with UART0 RTS | | --- | | TFT CS driven by port 1.7, shared with DVP DATA 11 and TRIG2 | |
| JP44 | LED1 EN | | 1-2 | | --- | | Open | | | LED0 illuminates when port 2.4 is high | | --- | | Pull jumper if using AIN4 | |
| JP45 | LED2 EN | | 1-2 | | --- | | Open | | | LED1 illuminates when port 2.5 is high | | --- | | Pull jumper if using AIN5 | |

## Programming and Debugging

The `max78002evkit` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Flashing

The MAX78002 MCU can be flashed by connecting an external debug probe to the
SWD port. SWD debug can be accessed through the Cortex 10-pin connector, JH8.
Logic levels are fixed to VDDIO (1.8V).

Once the debug probe is connected to your host computer, then you can simply run the
`west flash` command to write a firmware image into flash. To perform a full erase,
pass the `--erase` option when executing `west flash`.

Note

This board uses OpenOCD as the default debug interface. You can also use
a Segger J-Link with Segger’s native tooling by overriding the runner,
appending `--runner jlink` to your `west` command(s). The J-Link should
be connected to the standard 2\*5 pin debug connector (JH8) using an
appropriate adapter board and cable.

### Debugging

Please refer to the [Flashing](#flashing) section and run the `west debug` command
instead of `west flash`.

## References

- [MAX78002EVKIT web page](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/max78002evkit.html)

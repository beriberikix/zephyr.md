---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/adi/max32655evkit/doc/index.html
original_path: boards/adi/max32655evkit/doc/index.html
---

# MAX32655EVKIT

Board Overview

[![../../../../_images/max32655evkit_img1.jpg](../../../../_images/max32655evkit_img1.jpg)
](../../../../_images/max32655evkit_img1.jpg)

MAX32655EVKIT

Name:
:   `max32655evkit`

Vendor:
:   Analog Devices, Inc.

Architecture:
:   arm

SoC:
:   max32655

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adi/max32655evkit/doc/index.rst/../..)

## Overview

The MAX32655 evaluation kit (EV kit) provides a platform for evaluation capabilities
of the MAX32655 microcontroller, which is an advanced system-on-chip (SoC).
It features an Arm® Cortex®-M4F CPU for efficient computation of complex functions and
algorithms, integrated power management (SIMO), and the newest generation
Bluetooth® 5.0 Low Energy (Bluetooth LE), long-range radio for wearable and hearable device applications.

The Zephyr port is running on the MAX32655 MCU.

![MAX32655 EVKIT Front](../../../../_images/max32655evkit_img11.jpg)
![MAX32655 Back](../../../../_images/max32655evkit_img2.jpg)

## Hardware

- MAX32655 MCU:

  - Ultra-Low-Power Wireless Microcontroller
    - Internal 100MHz Oscillator
    - Flexible Low-Power Modes with 7.3728MHz System Clock Option
    - 512KB Flash and 128KB SRAM (Optional ECC on One 32KB SRAM Bank)
    - 16KB Instruction Cache
  - Bluetooth 5.2 LE Radio
    - Dedicated, Ultra-Low-Power, 32-Bit RISC-V Coprocessor to Offload Timing-Critical Bluetooth Processing
    - Fully Open-Source Bluetooth 5.2 Stack Available
    - Supports AoA, AoD, LE Audio, and Mesh
    - High-Throughput (2Mbps) Mode
    - Long-Range (125kbps and 500kbps) Modes
    - Rx Sensitivity: -97.5dBm; Tx Power: +4.5dBm
    - Single-Ended Antenna Connection (50Ω)
  - Power Management Maximizes Battery Life
    - 2.0V to 3.6V Supply Voltage Range
    - Integrated SIMO Power Regulator
    - Dynamic Voltage Scaling (DVS)
    - 23.8μA/MHz Active Current at 3.0V
    - 4.4μA at 3.0V Retention Current for 32KB
    - Selectable SRAM Retention + RTC in Low-Power Modes
  - Multiple Peripherals for System Control
    - Up to Two High-Speed SPI Master/Slave
    - Up to Three High-Speed I2C Master/Slave (3.4Mbps)
    - Up to Four UART, One I2S Master/Slave
    - Up to 8-Input, 10-Bit Sigma-Delta ADC 7.8ksps
    - Up to Four Micro-Power Comparators
    - Timers: Up to Two Four 32-Bit, Two LP, TwoWatchdog Timers
    - 1-Wire® Master
    - Up to Four Pulse Train (PWM) Engines
    - RTC with Wake-Up Timer
    - Up to 52 GPIOs
  - Security and Integrity​
    - Available Secure Boot
    - TRNG Seed Generator
    - AES 128/192/256 Hardware Acceleration Engine
- External devices connected to the MAX32655 EVKIT:

  - Color TFT Display
  - Audio Stereo Codec Interface
  - Digital Microphone
  - A 128Mb QSPI flash

### Supported Features

The `max32655evkit` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `max32655evkit/max32655/m4` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L25) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | ADI MAX32 ADC 10-Bits[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L230) | [`adi,max32-adc-10b`](../../../../build/dts/api/bindings/adc/adi%2Cmax32-adc-10b.md#std-dtcompatible-adi-max32-adc-10b) |
| Clock control | on-chip | MAX32 Global Control[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L118) | [`adi,max32-gcr`](../../../../build/dts/api/bindings/clock/adi%2Cmax32-gcr.md#std-dtcompatible-adi-max32-gcr) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L53)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L60) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | ADI MAX32 counter[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L250) | [`adi,max32-counter`](../../../../build/dts/api/bindings/counter/adi%2Cmax32-counter.md#std-dtcompatible-adi-max32-counter) |
| on-chip | ADI MAX32 compatible Counter RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L318) | [`adi,max32-rtc-counter`](../../../../build/dts/api/bindings/counter/adi%2Cmax32-rtc-counter.md#std-dtcompatible-adi-max32-rtc-counter) |
| DMA | on-chip | ADI MAX32 DMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32655.dtsi?plain=1#L78) | [`adi,max32-dma`](../../../../build/dts/api/bindings/dma/adi%2Cmax32-dma.md#std-dtcompatible-adi-max32-dma) |
| Flash controller | on-chip | MAX32XXX flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L102) | [`adi,max32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/adi%2Cmax32-flash-controller.md#std-dtcompatible-adi-max32-flash-controller) |
| GPIO & Headers | on-chip | MAX32 GPIO[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L166) | [`adi,max32-gpio`](../../../../build/dts/api/bindings/gpio/adi%2Cmax32-gpio.md#std-dtcompatible-adi-max32-gpio) |
| I2C | on-chip | ADI MAX32 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L127)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L138) | [`adi,max32-i2c`](../../../../build/dts/api/bindings/i2c/adi%2Cmax32-i2c.md#std-dtcompatible-adi-max32-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32655evkit/max32655evkit_max32655_m4.dts?plain=1#L37) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32655evkit/max32655evkit_max32655_m4.dts?plain=1#L25) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L110) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Properties supporting Zephyr spi-nor flash driver (over the Zephyr SPI API) control of serial flash memories using the standard M25P80-based command set[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32655evkit/max32655evkit_max32655_m4.dts?plain=1#L154) | [`jedec,spi-nor`](../../../../build/dts/api/bindings/mtd/jedec%2Cspi-nor.md#std-dtcompatible-jedec-spi-nor) |
| Pin control | on-chip | MAX32 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L160) | [`adi,max32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/adi%2Cmax32-pinctrl.md#std-dtcompatible-adi-max32-pinctrl) |
| PWM | on-chip | ADI MAX32 PWM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L254) | [`adi,max32-pwm`](../../../../build/dts/api/bindings/pwm/adi%2Cmax32-pwm.md#std-dtcompatible-adi-max32-pwm) |
| RNG | on-chip | ADI MAX32XXX TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L214) | [`adi,max32-trng`](../../../../build/dts/api/bindings/rng/adi%2Cmax32-trng.md#std-dtcompatible-adi-max32-trng) |
| Serial controller | on-chip | MAX32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L187)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L196) | [`adi,max32-uart`](../../../../build/dts/api/bindings/serial/adi%2Cmax32-uart.md#std-dtcompatible-adi-max32-uart) |
| SPI | on-chip | ADI MAX32 SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32655.dtsi?plain=1#L97)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32655.dtsi?plain=1#L107) | [`adi,max32-spi`](../../../../build/dts/api/bindings/spi/adi%2Cmax32-spi.md#std-dtcompatible-adi-max32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L97) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | ADI MAX32 timer[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L242) | [`adi,max32-timer`](../../../../build/dts/api/bindings/timer/adi%2Cmax32-timer.md#std-dtcompatible-adi-max32-timer) |
| 1-Wire | on-chip | ADI MAX32xxx MCUs 1-Wire Master[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32655.dtsi?plain=1#L145) | [`adi,max32-w1`](../../../../build/dts/api/bindings/w1/adi%2Cmax32-w1.md#std-dtcompatible-adi-max32-w1) |
| Watchdog | on-chip | MAX32XXX watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L221)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32655.dtsi?plain=1#L88) | [`adi,max32-watchdog`](../../../../build/dts/api/bindings/watchdog/adi%2Cmax32-watchdog.md#std-dtcompatible-adi-max32-watchdog) |

### Connections and IOs

| Name | Signal | Usage |
| --- | --- | --- |
| JP1 | VREGI | Connect/Disconnect VREGIO power |
| JP2 | P0\_24 | Enable/Disable LED1 |
| JP3 | P0\_25 | Enable/Disable LED2 |
| JP4 | P2\_6/ P2\_7 | Connect/Disconnect the USB to serial UART to GPIO P2\_6 (LPUART\_RX) |
| JP5 | P2\_7/ P0\_1 | Connect/Disconnect the USB to serial UART to GPIO P2\_7 (LPUART\_TX) |
| JP6 | P0\_2 | Connect/Disconnect the USB to serial UART to GPIO P0\_2 (UART0\_CTS) |
| JP7 | P0\_3 | Connect/Disconnect he USB to serial UART to GPIO P0\_3 (UART0\_RTS) |
| JP8 | VREGI | Select VDDIO\_EN power source (3V3 or coin cell) |
| JP9 | VDDIOH\_EN | Select VDDIOH\_EN power source 3V3/VREGI |
| JP10 | VDDIOH | Connect/Disconnect VDDIOH power |
| JP11 | VDDIO\_EN | Select VDDIO\_EN power source 1V8/VREGO\_A |
| JP12 | VDDIO | Connect/Disconnect VDDIO power |
| JP13 | VDDA\_EN | Select VDDA\_EN power source 1V8/VREGO\_A |
| JP14 | VDDA | Connect/Disconnect VDDA power |
| JP15 | VCOREA\_EN | Select VCOREA\_EN power source 1V1/VREGO\_C |
| JP16 | VCOREA | Connect/Disconnect VCOREA power |
| JP17 | VCOREB\_EN | Select VCOREB\_EN power source 1V1/VREGO\_B |
| JP18 | VCOREB | Connect/Disconnect VCOREB power |
| JP19 | BLE\_LDO | Connect/Disconnect BLE\_LDO power |
| JP20 | VREF | Select VREF power source VDDIO/VDDIOH |
| JP21 | I2C0\_PU | Select I2C0\_PU power source VDDIO/VDDIOH |
| JP22 | I2C1\_PU | Select I2C1\_PU power source VDDIO/VDDIOH |
| JP23 | BOARD RESET | Connect/Disconnect RV JTAG NRESET from the BOARD RESET circuitry |

## Programming and Debugging

The `max32655evkit` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Flashing

The MAX32655 MCU can be flashed by connecting an external debug probe to the
SWD port. SWD debug can be accessed through the Cortex 10-pin connector, JH3.
Logic levels are fixed to VDDIO (1.8V).

Once the debug probe is connected to your host computer, then you can simply run the
`west flash` command to write a firmware image into flash. To perform a full erase,
pass the `--erase` option when executing `west flash`.

Note

This board uses OpenOCD as the default debug interface. You can also use
a Segger J-Link with Segger’s native tooling by overriding the runner,
appending `--runner jlink` to your `west` command(s). The J-Link should
be connected to the standard 2\*5 pin debug connector (JW3) using an
appropriate adapter board and cable.

### Debugging

Please refer to the [Flashing](#flashing) section and run the `west debug` command
instead of `west flash`.

## References

- [MAX32655EVKIT web page](https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/max32655evkit.html#eb-overview)

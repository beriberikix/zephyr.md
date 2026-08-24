---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/adi/ad_swiot1l_sl/doc/index.html
original_path: boards/adi/ad_swiot1l_sl/doc/index.html
---

# AD-SWIOT1L-SL

Board Overview

[![../../../../_images/ad_swiot1l_sl.webp](https://docs.zephyrproject.org/4.2.0/_images/ad_swiot1l_sl.webp)
](https://docs.zephyrproject.org/4.2.0/_images/ad_swiot1l_sl.webp)

AD-SWIOT1L-SL

Name:
:   `ad_swiot1l_sl`

Vendor:
:   Analog Devices, Inc.

Architecture:
:   arm

SoC:
:   max32650

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adi/ad_swiot1l_sl/doc/index.rst/../..)

## Overview

The AD-SWIOT1L-SL is a complete hardware and software platform for prototyping intelligent,
secure, network-capable field devices, with applications in factory automation, process
control, and intelligent buildings.

The Zephyr port is running on the MAX32650 MCU.

## Hardware

- MAX32650 MCU:

  - Ultra-Efficient Microcontroller for Battery-Powered Applications

    - 120MHz Arm Cortex-M4 Processor with FPU
    - SmartDMA Provides Background Memory Transfers with Programmable Data Processing
    - 120MHz High-Speed and 50MHz Low-Power Oscillators
    - 7.3728MHz Low-Power Oscillators
    - 32.768kHz and RTC Clock (Requires External Crystal)
    - 8kHz, Always-On, Ultra-Low-Power Oscillator
    - 3MB Internal Flash, 1MB Internal SRAM
    - 104μW/MHz Executing from Cache at 1.1V
    - Five Low-Power Modes: Active, Sleep, Background, Deep Sleep, and Backup
    - 1.8V and 3.3V I/O with No Level Translators
  - Scalable Cached External Memory Interfaces:

    - 120MB/s HyperBus/Xccela DDR Interface
    - SPIXF/SPIXR for External Flash/RAM Expansion
    - 240Mbps SDHC/eMMC/SDIO/microSD Interface
  - Optimal Peripheral Mix Provides Platform Scalability

    - 16-Channel DMA
    - Three SPI Master (60MHz)/Slave (48MHz)
    - One QuadSPI Master (60MHz)/Slave (48MHz)
    - Up to Three 4Mbaud UARTs with Flow Control
    - Two 1MHz I2C Master/Slave
    - I2S Slave
    - Four-Channel, 7.8ksps, 10-Bit Delta-Sigma ADC
    - USB 2.0 Hi-Speed Device Interface with PHY
    - 16 Pulse Train Generators
    - Six 32-Bit Timers with 8mA High Drive
    - 1-Wire® Master
  - Trust Protection Unit (TPU) for IP/Data Security

    - Modular Arithmetic Accelerator (MAA), True Random Number Generator (TRNG)
    - Secure Nonvolatile Key Storage, SHA-256, AES-128/192/256
    - Memory Decryption Integrity Unit, Secure Boot ROM
- External devices connected to the AD-SWIOT1L-SL:

  - On-Board HyperRAM
  - On-Board QSPI Flash
  - MAXQ1065 Ultralow Power Cryptographic Controller with ChipDNA
  - ADIN1110 Robust, Industrial, Low Power 10BASE-T1L Ethernet MAC-PHY
  - 2-Pin external power supply terminal block (24V DC)
  - ADP1032 high performance, isolated micropower management unit (PMU)
  - SWD 10-Pin Header
  - On-Board 3.3V, 1.8V, and 1.1V voltage regulators
  - AD74413R Quad-channel, Software Configurable I/O
  - MAX14906 Quad-channel, Industrial Digital I/O
  - Two general-purpose LEDs

### Supported Features

The `ad_swiot1l_sl` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `ad_swiot1l_sl/max32650` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L25) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | ADI MAX32 ADC 10-Bits[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L230) | [`adi,max32-adc-10b`](../../../../build/dts/api/bindings/adc/adi,max32-adc-10b.md#std-dtcompatible-adi-max32-adc-10b) |
| Clock control | on-chip | MAX32 Global Control[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L118) | [`adi,max32-gcr`](../../../../build/dts/api/bindings/clock/adi,max32-gcr.md#std-dtcompatible-adi-max32-gcr) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L53)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L60) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | ADI MAX32 counter[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L250) | [`adi,max32-counter`](../../../../build/dts/api/bindings/counter/adi,max32-counter.md#std-dtcompatible-adi-max32-counter) |
| on-chip | ADI MAX32 compatible Counter RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L318) | [`adi,max32-rtc-counter`](../../../../build/dts/api/bindings/counter/adi,max32-rtc-counter.md#std-dtcompatible-adi-max32-rtc-counter) |
| DMA | on-chip | ADI MAX32 DMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32650.dtsi?plain=1#L194) | [`adi,max32-dma`](../../../../build/dts/api/bindings/dma/adi,max32-dma.md#std-dtcompatible-adi-max32-dma) |
| Flash controller | on-chip | MAX32XXX flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L102) | [`adi,max32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/adi,max32-flash-controller.md#std-dtcompatible-adi-max32-flash-controller) |
| GPIO & Headers | on-chip | MAX32 GPIO[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L166) | [`adi,max32-gpio`](../../../../build/dts/api/bindings/gpio/adi,max32-gpio.md#std-dtcompatible-adi-max32-gpio) |
| I2C | on-chip | ADI MAX32 I2C[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L127) | [`adi,max32-i2c`](../../../../build/dts/api/bindings/i2c/adi,max32-i2c.md#std-dtcompatible-adi-max32-i2c) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/ad_swiot1l_sl/ad_swiot1l_sl.dts?plain=1#L25) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L110) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | MAX32 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L160) | [`adi,max32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/adi,max32-pinctrl.md#std-dtcompatible-adi-max32-pinctrl) |
| PWM | on-chip | ADI MAX32 PWM[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L254) | [`adi,max32-pwm`](../../../../build/dts/api/bindings/pwm/adi,max32-pwm.md#std-dtcompatible-adi-max32-pwm) |
| RNG | on-chip | ADI MAX32XXX TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32650.dtsi?plain=1#L89) | [`adi,max32-trng`](../../../../build/dts/api/bindings/rng/adi,max32-trng.md#std-dtcompatible-adi-max32-trng) |
| Serial controller | on-chip | MAX32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L187)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L196) | [`adi,max32-uart`](../../../../build/dts/api/bindings/serial/adi,max32-uart.md#std-dtcompatible-adi-max32-uart) |
| SPI | on-chip | ADI MAX32 SPI[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32650.dtsi?plain=1#L138) | [`adi,max32-spi`](../../../../build/dts/api/bindings/spi/adi,max32-spi.md#std-dtcompatible-adi-max32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L97) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | ADI MAX32 timer[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L242) | [`adi,max32-timer`](../../../../build/dts/api/bindings/timer/adi,max32-timer.md#std-dtcompatible-adi-max32-timer) |
| Watchdog | on-chip | MAX32XXX watchdog[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32650.dtsi?plain=1#L178) | [`adi,max32-watchdog`](../../../../build/dts/api/bindings/watchdog/adi,max32-watchdog.md#std-dtcompatible-adi-max32-watchdog) |

## Programming and Debugging

The `ad_swiot1l_sl` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Flashing

The MAX32650 MCU can be flashed by connecting an external debug probe to the
SWD port. SWD debug can be accessed through the Cortex 10-pin connector, J3.
Logic levels are fixed to VDDIO (1.8V).

Once the debug probe is connected to your host computer, then you can simply run the
`west flash` command to write a firmware image into flash.

Note

This board uses OpenOCD as the default debug interface. You can also use
a Segger J-Link with Segger’s native tooling by overriding the runner,
appending `--runner jlink` to your `west` command(s). The J-Link should
be connected to the standard 2\*5 pin debug connector (J3) using an
appropriate adapter board and cable

### Debugging

Please refer to the [Flashing](#flashing) section and run the `west debug` command
instead of `west flash`.

## References

- [AD-SWIOT1L-SL web page](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/AD-SWIOT1L-SL.html)

---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/adi/max32690fthr/doc/index.html
original_path: boards/adi/max32690fthr/doc/index.html
---

# MAX32690FTHR

Board Overview

[![../../../../_images/max32690fthr.webp](https://docs.zephyrproject.org/4.2.0/_images/max32690fthr.webp)
](https://docs.zephyrproject.org/4.2.0/_images/max32690fthr.webp)

MAX32690FTHR

Name:
:   `max32690fthr`

Vendor:
:   Analog Devices, Inc.

Architecture:
:   arm

SoC:
:   max32690

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adi/max32690fthr/doc/index.rst/../..)

## Overview

The MAX32690FTHR is a rapid development platform to help engineers quickly
implement ultra low-power wireless solutions using MAX32690 Arm© Cortex®-M4F
and Bluetooth® 5.2 Low Energy (LE). The board also includes the MAX77654 PMIC
for battery and power management. The form factor is a small 0.9in x 2.6in
dual-row header footprint that is compatible with Adafruit Feather Wing
peripheral expansion boards.

## Hardware

- MAX32690 MCU:

  > - Ultra-Efficient Microcontroller for Battery-Powered Applications
  >
  >   - 120MHz Arm Cortex-M4 Processor with FPU
  >   - 7.3728MHz and 60MHz Low-Power Oscillators
  >   - External Crystal Support (32MHz required for BLE)
  >   - 32.768kHz RTC Clock (Requires External Crystal)
  >   - 8kHz Always-On Ultra-Low Power Oscillator
  >   - 3MB Internal Flash, 1MB Internal SRAM (832kB ECC ON)
  >   - 85 μW/MHz ACTIVE mode at 1.1V
  >   - 1.8V and 3.3V I/O with No Level Translators
  >   - External Flash & SRAM Expansion Interfaces
  > - Bluetooth 5.2 LE Radio
  >
  >   - Dedicated, Ultra-Low-Power, 32-Bit RISC-V Coprocessor to Offload
  >     Timing-Critical Bluetooth Processing
  >   - Fully Open-Source Bluetooth 5.2 Stack Available
  >   - Supports AoA, AoD, LE Audio, and Mesh
  >   - High-Throughput (2Mbps) Mode
  >   - Long-Range (125kbps and 500kbps) Modes
  >   - Rx Sensitivity: -97.5dBm; Tx Power: +4.5dBm
  >   - Single-Ended Antenna Connection (50Ω)
  > - Multiple Peripherals for System Control
  >
  >   - 16-Channel DMA
  >   - Up To Five Quad SPI Master (60MHz)/Slave (48MHz)
  >   - Up To Four 1Mbaud UARTs with Flow Control
  >   - Up To Two 1MHz I2C Master/Slave
  >   - I2S Master/Slave
  >   - Eight External Channel, 12-bit 1MSPS SAR ADC w/ on-die temperature sensor
  >   - USB 2.0 Hi-Speed Device
  >   - 16 Pulse Train Engines
  >   - Up To Six 32-Bit Timers with 8mA High Drive
  >   - Up To Two CAN 2.0 Controllers
  >   - Up To Four Micro-Power Comparators
  >   - 1-Wire Master
  > - Security and Integrity​
  >
  >   - ChipDNA Physically Un-clonable Function (PUF)
  >   - Modular Arithmetic Accelerator (MAA), True Random Number Generator (TRNG)
  >   - Secure Nonvolatile Key Storage, SHA-256, AES-128/192/256
  >   - Secure Boot ROM

### Supported Features

The `max32690fthr` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `max32690fthr/max32690/m4` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L25) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | ADI MAX32 ADC SAR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L230) | [`adi,max32-adc-sar`](../../../../build/dts/api/bindings/adc/adi%2Cmax32-adc-sar.md#std-dtcompatible-adi-max32-adc-sar) |
| CAN | on-chip | ADI MAX32 CAN Node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32690.dtsi?plain=1#L257) | [`adi,max32-can`](../../../../build/dts/api/bindings/can/adi%2Cmax32-can.md#std-dtcompatible-adi-max32-can) |
| Clock control | on-chip | MAX32 Global Control[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L118) | [`adi,max32-gcr`](../../../../build/dts/api/bindings/clock/adi%2Cmax32-gcr.md#std-dtcompatible-adi-max32-gcr) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L74)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L53) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | ADI MAX32 counter[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L250) | [`adi,max32-counter`](../../../../build/dts/api/bindings/counter/adi%2Cmax32-counter.md#std-dtcompatible-adi-max32-counter) |
| on-chip | ADI MAX32 compatible Counter RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L318) | [`adi,max32-rtc-counter`](../../../../build/dts/api/bindings/counter/adi%2Cmax32-rtc-counter.md#std-dtcompatible-adi-max32-rtc-counter) |
| DMA | on-chip | ADI MAX32 DMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32690.dtsi?plain=1#L190) | [`adi,max32-dma`](../../../../build/dts/api/bindings/dma/adi%2Cmax32-dma.md#std-dtcompatible-adi-max32-dma) |
| Flash controller | on-chip | MAX32XXX flash controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L102) | [`adi,max32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/adi%2Cmax32-flash-controller.md#std-dtcompatible-adi-max32-flash-controller) |
| GPIO & Headers | on-chip | MAX32 GPIO[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L166)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32690.dtsi?plain=1#L47) | [`adi,max32-gpio`](../../../../build/dts/api/bindings/gpio/adi%2Cmax32-gpio.md#std-dtcompatible-adi-max32-gpio) |
| on-board | GPIO pins exposed on Adafruit Feather headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32690fthr/max32690fthr_max32690_m4.dts?plain=1#L63) | [`adafruit-feather-header`](../../../../build/dts/api/bindings/gpio/adafruit-feather-header.md#std-dtcompatible-adafruit-feather-header) |
| I2C | on-chip | ADI MAX32 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L127)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L138) | [`adi,max32-i2c`](../../../../build/dts/api/bindings/i2c/adi%2Cmax32-i2c.md#std-dtcompatible-adi-max32-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32690fthr/max32690fthr_max32690_m4.dts?plain=1#L41) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32690fthr/max32690fthr_max32690_m4.dts?plain=1#L25) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Memory controller | on-chip | MAX32 HyperBus (HPB) Memory Controller Interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32690.dtsi?plain=1#L122) | [`adi,max32-hpb`](../../../../build/dts/api/bindings/memory-controllers/adi%2Cmax32-hpb.md#std-dtcompatible-adi-max32-hpb) |
| MTD | on-chip | Flash node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L110) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | MAX32 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L160) | [`adi,max32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/adi%2Cmax32-pinctrl.md#std-dtcompatible-adi-max32-pinctrl) |
| PWM | on-chip | ADI MAX32 PWM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L254) | [`adi,max32-pwm`](../../../../build/dts/api/bindings/pwm/adi%2Cmax32-pwm.md#std-dtcompatible-adi-max32-pwm) |
| RNG | on-chip | ADI MAX32XXX TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L214) | [`adi,max32-trng`](../../../../build/dts/api/bindings/rng/adi%2Cmax32-trng.md#std-dtcompatible-adi-max32-trng) |
| Serial controller | on-chip | MAX32 UART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L187)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L196) | [`adi,max32-uart`](../../../../build/dts/api/bindings/serial/adi%2Cmax32-uart.md#std-dtcompatible-adi-max32-uart) |
| SPI | on-chip | ADI MAX32 SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32690.dtsi?plain=1#L131)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32690.dtsi?plain=1#L141) | [`adi,max32-spi`](../../../../build/dts/api/bindings/spi/adi%2Cmax32-spi.md#std-dtcompatible-adi-max32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L97) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | ADI MAX32 timer[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L242) | [`adi,max32-timer`](../../../../build/dts/api/bindings/timer/adi%2Cmax32-timer.md#std-dtcompatible-adi-max32-timer) |
| USB | on-chip | ADI MAX32 USBHS[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32690.dtsi?plain=1#L245) | [`adi,max32-usbhs`](../../../../build/dts/api/bindings/usb/adi%2Cmax32-usbhs.md#std-dtcompatible-adi-max32-usbhs) |
| 1-Wire | on-chip | ADI MAX32xxx MCUs 1-Wire Master[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32690.dtsi?plain=1#L237) | [`adi,max32-w1`](../../../../build/dts/api/bindings/w1/adi%2Cmax32-w1.md#std-dtcompatible-adi-max32-w1) |
| Watchdog | on-chip | MAX32XXX watchdog[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L221) | [`adi,max32-watchdog`](../../../../build/dts/api/bindings/watchdog/adi%2Cmax32-watchdog.md#std-dtcompatible-adi-max32-watchdog) |

## Programming and Debugging

The `max32690fthr` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Flashing

The MAX32690 MCU can be flashed by connecting an external debug probe to the
SWD port. SWD debug can be accessed through the Cortex 10-pin connector, J4.
Logic levels are fixed to VDDIO (1.8V).

Once the debug probe is connected to your host computer, then you can run the
`west flash` command to write a firmware image into flash. Here is an example
for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application. To perform a full erase,
pass the `--erase` option when executing `west flash`.

```shell
# From the root of the zephyr repository
west build -b max32690fthr/max32690/m4 samples/hello_world
west flash
```

Note

This board uses OpenOCD as the default debug interface. You can also use a
Segger J-Link with Segger’s native tooling by overriding the runner,
appending `--runner jlink` to your `west` command(s). The J-Link should
be connected to the standard 2\*5 pin debug connector (J4) using an
appropriate adapter board and cable.

### Debugging

Once the debug probe is connected to your host computer, then you can run the
`west debug` command to write a firmware image into flash and start a debug
session. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b max32690fthr/max32690/m4 samples/hello_world
west debug
```

## References

- [MAX32690 solution center](https://developer.analog.com/solutions/max32690)

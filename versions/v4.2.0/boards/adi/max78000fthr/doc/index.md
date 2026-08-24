---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/adi/max78000fthr/doc/index.html
original_path: boards/adi/max78000fthr/doc/index.html
---

# MAX78000FTHR

Board Overview

[![../../../../_images/max78000fthr.webp](https://docs.zephyrproject.org/4.2.0/_images/max78000fthr.webp)
](https://docs.zephyrproject.org/4.2.0/_images/max78000fthr.webp)

MAX78000FTHR

Name:
:   `max78000fthr`

Vendor:
:   Analog Devices, Inc.

Architecture:
:   arm

SoC:
:   max78000

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adi/max78000fthr/doc/index.rst/../..)

## Overview

The MAX78000FTHR is a rapid development platform to help engineers quickly implement ultra low-power, artificial
intelligence (AI) solutions using the MAX78000 Arm® Cortex®-M4F processor with an integrated Convolutional Neural Network
accelerator. The board also includes the MAX20303 PMIC for battery and power management. The form factor is 0.9in x 2.6in
dual-row header footprint that is compatible with Adafruit Feather Wing peripheral expansion boards. The board includes a
variety of peripherals, such as a CMOS VGA image sensor, digital microphone, low-power stereo audio CODEC, 1MB QSPI
SRAM, micro SD card connector, RGB indicator LED, and pushbutton. The MAX78000FTHR provides a poweroptimized flexible
platform for quick proof-of-concepts and early software development to enhance time to market.

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

The `max78000fthr` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `max78000fthr/max78000/m4` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L25) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | ADI MAX32 ADC 10-Bits[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L230) | [`adi,max32-adc-10b`](../../../../build/dts/api/bindings/adc/adi%2Cmax32-adc-10b.md#std-dtcompatible-adi-max32-adc-10b) |
| Clock control | on-chip | MAX32 Global Control[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L118) | [`adi,max32-gcr`](../../../../build/dts/api/bindings/clock/adi%2Cmax32-gcr.md#std-dtcompatible-adi-max32-gcr) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L53)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L60) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | ADI MAX32 counter[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L250) | [`adi,max32-counter`](../../../../build/dts/api/bindings/counter/adi%2Cmax32-counter.md#std-dtcompatible-adi-max32-counter) |
| on-chip | ADI MAX32 compatible Counter RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L318) | [`adi,max32-rtc-counter`](../../../../build/dts/api/bindings/counter/adi%2Cmax32-rtc-counter.md#std-dtcompatible-adi-max32-rtc-counter) |
| DMA | on-chip | ADI MAX32 DMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max78000.dtsi?plain=1#L91) | [`adi,max32-dma`](../../../../build/dts/api/bindings/dma/adi%2Cmax32-dma.md#std-dtcompatible-adi-max32-dma) |
| Flash controller | on-chip | MAX32XXX flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L102) | [`adi,max32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/adi%2Cmax32-flash-controller.md#std-dtcompatible-adi-max32-flash-controller) |
| GPIO & Headers | on-chip | MAX32 GPIO[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L166) | [`adi,max32-gpio`](../../../../build/dts/api/bindings/gpio/adi%2Cmax32-gpio.md#std-dtcompatible-adi-max32-gpio) |
| I2C | on-chip | ADI MAX32 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L127)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L138) | [`adi,max32-i2c`](../../../../build/dts/api/bindings/i2c/adi%2Cmax32-i2c.md#std-dtcompatible-adi-max32-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max78000fthr/max78000fthr_max78000_m4.dts?plain=1#L44) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max78000fthr/max78000fthr_max78000_m4.dts?plain=1#L25) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L110) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | MAX32 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L160) | [`adi,max32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/adi%2Cmax32-pinctrl.md#std-dtcompatible-adi-max32-pinctrl) |
| PWM | on-chip | ADI MAX32 PWM[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L254) | [`adi,max32-pwm`](../../../../build/dts/api/bindings/pwm/adi%2Cmax32-pwm.md#std-dtcompatible-adi-max32-pwm) |
| RNG | on-chip | ADI MAX32XXX TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L214) | [`adi,max32-trng`](../../../../build/dts/api/bindings/rng/adi%2Cmax32-trng.md#std-dtcompatible-adi-max32-trng) |
| Serial controller | on-chip | MAX32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L187)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L196) | [`adi,max32-uart`](../../../../build/dts/api/bindings/serial/adi%2Cmax32-uart.md#std-dtcompatible-adi-max32-uart) |
| SPI | on-chip | ADI MAX32 SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max78000.dtsi?plain=1#L71)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max78000.dtsi?plain=1#L81) | [`adi,max32-spi`](../../../../build/dts/api/bindings/spi/adi%2Cmax32-spi.md#std-dtcompatible-adi-max32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L97) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | ADI MAX32 timer[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L242) | [`adi,max32-timer`](../../../../build/dts/api/bindings/timer/adi%2Cmax32-timer.md#std-dtcompatible-adi-max32-timer) |
| 1-Wire | on-chip | ADI MAX32xxx MCUs 1-Wire Master[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max78000.dtsi?plain=1#L101) | [`adi,max32-w1`](../../../../build/dts/api/bindings/w1/adi%2Cmax32-w1.md#std-dtcompatible-adi-max32-w1) |
| Watchdog | on-chip | MAX32XXX watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L221)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max78000.dtsi?plain=1#L109) | [`adi,max32-watchdog`](../../../../build/dts/api/bindings/watchdog/adi%2Cmax32-watchdog.md#std-dtcompatible-adi-max32-watchdog) |

### Connections and IOs

## J8 Pinout

| Pin | Name | Description |
| --- | --- | --- |
| 1 | RST | Master Reset Signal |
| 2 | 3V3 | 3.3V Output. Typically used to provide 3.3V to peripherals connected to the expansion headers. |
| 3 | 1V8 | 1.8V Output. Typically used to provide 1.8V to peripherals connected to the expansion headers. |
| 4 | GND | Ground |
| 5 | P2\_3 | GPIO or Analog Input (AIN3 channel). |
| 6 | P2\_4 | GPIO or Analog Input (AIN4 channel). |
| 7 | P1\_1 | GPIO or UART2 Tx signal |
| 8 | P1\_0 | GPIO or UART2 Rx signal |
| 9 | MPC1 | GPIO controlled by PMIC through I2C interface. Open drain or push-pull programmable |
| 10 | MPC2 | GPIO controlled by PMIC through I2C interface. Open drain or push-pull programmable |
| 11 | P0\_7 | GPIO or QSPI0 clock signal. Shared with SD card and on-board QSPI SRAM |
| 12 | P0\_5 | GPIO or QSPI0 MOSI signal. Shared with SD card and on-board QSPI SRAM |
| 13 | P0\_6 | GPIO or QSPI0 MISO signal. Shared with SD card and on-board QSPI SRAM |
| 14 | P2\_6 | GPIO or LPUART Rx signal |
| 15 | P2\_7 | GPIO or LPUART Tx signal |
| 16 | GND | Ground |

## J4 Pinout

| Pin | Name | Description |
| --- | --- | --- |
| 1 | SYS | SYS Switched Connection to the Battery. This is the primary system power supply and automatically switches between the battery voltage and the USB supply when available. |
| 2 | PWR | Turns off the PMIC if shorted to Ground for 13 seconds. Hard power-down button. |
| 3 | VBUS | USB VBUS Signal. This can be used as a 5V supply when connected to USB. This pin can also be used as an input to power the board. |
| 4 | P1\_6 | GPIO |
| 5 | MPC3 | GPIO controlled by PMIC through the I2C interface. Open drain or push-pull programmable. |
| 6 | P0\_9 | GPIO or QSPI0 SDIO3 signal. Shared with SD card and on-board QSPI SRAM. |
| 7 | P0\_8 | GPIO or QSPI0 SDIO2 signal. Shared with SD Card and on-board QSPI SRAM. |
| 8 | P0\_11 | GPIO or QSPI0 slave select signal |
| 9 | P0\_19 | GPIO |
| 10 | P3\_1 | GPIO or Wake-up signal. This pin is 3.3V only. |
| 11 | P0\_16 | GPIO or I2C1 SCL signal. An on-board level shifter allows selecting 1.8V or 3.3V operation through R15 or R20 resistors. Do not populate both. |
| 12 | P0\_17 | GPIO or I2C1 SDA signal. An on-board level shifter allows selecting 1.8V or 3.3V operation through R15 or R20 resistors. Do not populate both. |

## Programming and Debugging

The `max78000fthr` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Flashing

The MAX32625 microcontroller on the board is preprogrammed with DAPLink firmware.
It allows debugging and programming of the MAX78000 Arm core over USB.

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

- [MAX78000FTHR web page](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/max78000fthr.html)

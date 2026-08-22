---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/adi/max32690evkit/doc/index.html
original_path: boards/adi/max32690evkit/doc/index.html
---

# MAX32690EVKIT

Board Overview

[![../../../../_images/max32690evkit.jpg](../../../../_images/max32690evkit.jpg)
](../../../../_images/max32690evkit.jpg)

MAX32690EVKIT

Name:
:   `max32690evkit`

Vendor:
:   Analog Devices, Inc.

Architecture:
:   arm

SoC:
:   max32690

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adi/max32690evkit/doc/index.rst/../..)

## Overview

The MAX32690 evaluation kit (EV kit) provides a platform for evaluating the capabilities
of the MAX32690 microcontroller, which is an advanced system-on-chip (SoC).
It features an Arm® Cortex®-M4F CPU for efficient computation of complex functions and
algorithms, and the latest generation Bluetooth® 5 Low Energy (Bluetooth LE) radio designed
for wearable and hearable fitness devices, portable and wearable wireless medical devices,
industrial sensors/networks, internet of things (IoT), and asset tracking.

The Zephyr port is running on the MAX32690 MCU.

![MAX32690 EVKIT Front](../../../../_images/max32690evkit1.jpg)
![MAX32690 Back](../../../../_images/max32690evkit_img2.jpg)

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
  >   - TBDμW/MHz Executing from Cache at 1.1V
  >   - 1.8V and 3.3V I/O with No Level Translators
  >   - External Flash & SRAM Expansion Interfaces
  > - Bluetooth 5.2 LE Radio
  >
  >   - Dedicated, Ultra-Low-Power, 32-Bit RISC-V Coprocessor to Offload Timing-Critical Bluetooth Processing
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
- External devices connected to the MAX32690EVKIT:

  - Bluetooth SMA Connector with a Hinged 2.4GHz Whip Antenna
  - 3-Pin Terminal Block for CAN Bus 2.0
  - Selectable On-Board High-Precision Voltage Reference
  - On-Board HyperRAM
  - Stereo Audio Codec with Line-In and Line-Out 3.5mm Jacks
  - 128 x 128 (1.45in) Color TFT Display
  - USB 2.0 Micro-B Interface to the MAX32690
  - USB 2.0 Micro-B to Serial UART
  - Board Power Provided by either USB Port
  - Jumpers to Enable Optional Pull-Up Resistors on I2C port
  - All GPIOs Signals Accessed through 0.1in Headers
  - Three Analog Inputs Accessed through 0.1in Headers with Optional Filtering
  - SWD 10-Pin Header
  - On-Board 3.3V, 1.8V, and 1.1V LDO Regulators
  - Individual Power Measurement on All IC Rails through Jumpers
  - Two General-Purpose LEDs and One GeneralPurpose Push Button Switch

### Supported Features

The `max32690evkit` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `max32690evkit/max32690/m4` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L25) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | ADI MAX32 ADC SAR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L230) | [`adi,max32-adc-sar`](../../../../build/dts/api/bindings/adc/adi%2Cmax32-adc-sar.md#std-dtcompatible-adi-max32-adc-sar) |
| CAN | on-chip | ADI MAX32 CAN Node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32690.dtsi?plain=1#L257)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32690.dtsi?plain=1#L265) | [`adi,max32-can`](../../../../build/dts/api/bindings/can/adi%2Cmax32-can.md#std-dtcompatible-adi-max32-can) |
| Clock control | on-chip | MAX32 Global Control[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L118) | [`adi,max32-gcr`](../../../../build/dts/api/bindings/clock/adi%2Cmax32-gcr.md#std-dtcompatible-adi-max32-gcr) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L53)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L60) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | ADI MAX32 counter[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L250) | [`adi,max32-counter`](../../../../build/dts/api/bindings/counter/adi%2Cmax32-counter.md#std-dtcompatible-adi-max32-counter) |
| on-chip | ADI MAX32 compatible Counter RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L318) | [`adi,max32-rtc-counter`](../../../../build/dts/api/bindings/counter/adi%2Cmax32-rtc-counter.md#std-dtcompatible-adi-max32-rtc-counter) |
| Display | on-board | Sitronix ST7735X display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32690evkit/max32690evkit_max32690_m4.dts?plain=1#L65) | [`sitronix,st7735r`](../../../../build/dts/api/bindings/display/sitronix%2Cst7735r.md#std-dtcompatible-sitronix-st7735r) |
| DMA | on-chip | ADI MAX32 DMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32690.dtsi?plain=1#L190) | [`adi,max32-dma`](../../../../build/dts/api/bindings/dma/adi%2Cmax32-dma.md#std-dtcompatible-adi-max32-dma) |
| Flash controller | on-chip | MAX32XXX flash controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L102) | [`adi,max32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/adi%2Cmax32-flash-controller.md#std-dtcompatible-adi-max32-flash-controller) |
| GPIO & Headers | on-chip | MAX32 GPIO[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L166) | [`adi,max32-gpio`](../../../../build/dts/api/bindings/gpio/adi%2Cmax32-gpio.md#std-dtcompatible-adi-max32-gpio) |
| I2C | on-chip | ADI MAX32 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L127)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L138) | [`adi,max32-i2c`](../../../../build/dts/api/bindings/i2c/adi%2Cmax32-i2c.md#std-dtcompatible-adi-max32-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32690evkit/max32690evkit_max32690_m4.dts?plain=1#L41) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32690evkit/max32690evkit_max32690_m4.dts?plain=1#L29) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Memory controller | on-chip | MAX32 HyperBus (HPB) Memory Controller Interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32690.dtsi?plain=1#L122) | [`adi,max32-hpb`](../../../../build/dts/api/bindings/memory-controllers/adi%2Cmax32-hpb.md#std-dtcompatible-adi-max32-hpb) |
| MTD | on-chip | Flash node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L110) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | MAX32 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L160) | [`adi,max32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/adi%2Cmax32-pinctrl.md#std-dtcompatible-adi-max32-pinctrl) |
| PWM | on-chip | ADI MAX32 PWM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L254) | [`adi,max32-pwm`](../../../../build/dts/api/bindings/pwm/adi%2Cmax32-pwm.md#std-dtcompatible-adi-max32-pwm) |
| RNG | on-chip | ADI MAX32XXX TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L214) | [`adi,max32-trng`](../../../../build/dts/api/bindings/rng/adi%2Cmax32-trng.md#std-dtcompatible-adi-max32-trng) |
| Serial controller | on-chip | MAX32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L205)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L187) | [`adi,max32-uart`](../../../../build/dts/api/bindings/serial/adi%2Cmax32-uart.md#std-dtcompatible-adi-max32-uart) |
| SPI | on-chip | ADI MAX32 SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32690.dtsi?plain=1#L131)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32690.dtsi?plain=1#L141) | [`adi,max32-spi`](../../../../build/dts/api/bindings/spi/adi%2Cmax32-spi.md#std-dtcompatible-adi-max32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L97) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | ADI MAX32 timer[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L242) | [`adi,max32-timer`](../../../../build/dts/api/bindings/timer/adi%2Cmax32-timer.md#std-dtcompatible-adi-max32-timer) |
| USB | on-chip | ADI MAX32 USBHS[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32690.dtsi?plain=1#L245) | [`adi,max32-usbhs`](../../../../build/dts/api/bindings/usb/adi%2Cmax32-usbhs.md#std-dtcompatible-adi-max32-usbhs) |
| 1-Wire | on-chip | ADI MAX32xxx MCUs 1-Wire Master[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32690.dtsi?plain=1#L237) | [`adi,max32-w1`](../../../../build/dts/api/bindings/w1/adi%2Cmax32-w1.md#std-dtcompatible-adi-max32-w1) |
| Watchdog | on-chip | MAX32XXX watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L221)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32690.dtsi?plain=1#L200) | [`adi,max32-watchdog`](../../../../build/dts/api/bindings/watchdog/adi%2Cmax32-watchdog.md#std-dtcompatible-adi-max32-watchdog) |

### Connections and IOs

| Name | Name | Settings | Description |
| --- | --- | --- | --- |
| JP1 | VREF | | 1-2 | | --- | | Open | | | Connects external voltage reference to VREF pin, must be enabled in software. | | --- | | Disconnects external voltage reference. | |
| JP2 | I2C0 PU | | 2-1 | | --- | | 2-3 | | Open | | | Connects VDDIO (1V8) to I2C0 pull-up resistors. | | --- | | Connects VDDIOH (3V3) to I2C0 pull-up resistors. | | Disconnects power from I2C0 pull-up resistors. | |
| JP3 | I2C0\_SDA\_PU | | 1-2 | | --- | | Open | | | Connects pull-up to I2C0A\_SDA (P2.7) sourced by I2C0 PU (JP2). | | --- | | Disconnects pull-up from I2C0A\_SDA (P2.7) sourced by I2C0 PU (JP2). | |
| JP4 | I2C0\_SCL\_PU | | 1-2 | | --- | | Open | | | Connects pull-up to I2C0A\_SCL (P2.8) sourced by I2C0 PU (JP2). | | --- | | Disconnects pull-up from I2C0A\_SCL (P2.8) sourced by I2C0 PU (JP2). | |
| JP5 | LED0 EN | | 1-2 | | --- | | Open | | | Connects red LED D1 to P0.14. | | --- | | Disconnects red LED D1 from P0.14. | |
| JP6 | LED1 EN | | 1-2 | | --- | | Open | | | Connects green LED D2 to P2.12. | | --- | | Disconnects green LED D2 from P2.12. | |
| JP7 | RX EN | | 1-2 | | --- | | Open | | | Connects the USB - serial bridge to UART2A\_RX (P1.9). | | --- | | Disconnects the USB - serial bridge from UART2A\_RX (P1.9). | |
| JP8 | TX EN | | 1-2 | | --- | | Open | | | Connects the USB - serial bridge to UART2A\_TX (P1.10). | | --- | | Disconnects the USB - serial bridge from UART2A\_TX (P1.10). | |
| JP9 | P1\_7 SEL | | 2-1 | | --- | | 2-3 | | | Connects the USB - serial bridge to UART2A\_CTS (P1.7). | | --- | | Connects I2C2C\_SDA (P1.7) to the codec. | |
| JP10 | P1\_8 SEL | | 2-1 | | --- | | 2-3 | | | Connects the USB - serial bridge to UART2A\_RTS (P1.8). | | --- | | Connects I2C2C\_SCL (P1.8) to the codec. | |
| JP11 | V\_AUX SEL | | 2-1 | | --- | | 2-3 | | | Connects V\_AUX to 1V8. | | --- | | Connects V\_AUX to 3V3. | |
| JP12 | VDD3A EN | | 1-2 | | --- | | Open | | | Connects 3V3 to VDD3A. | | --- | | Disconnects 3V3 from VDD3A. | |
| JP13 | VDDIOH EN | | 1-2 | | --- | | Open | | | Connects 3V3 to VDDIOH. | | --- | | Disconnects 3V3 from VDDIOH. | |
| JP14 | VDDB EN | | 1-2 | | --- | | Open | | | Connects a 3V3 LDO sourced by USB\_VBUS (CN1) to VDDB. | | --- | | Disconnects a 3V3 LDO sourced by USB\_VBUS (CN1) from VDDB. | |
| JP15 | VDDA EN | | 1-2 | | --- | | Open | | | Connects 1V8 to VDDA. | | --- | | Disconnects 1V8 from VDDA. | |
| JP16 | VDDIO EN | | 1-2 | | --- | | Open | | | Connects 1V8 to VDDIO. | | --- | | Disconnects 1V8 from VDDIO. | |
| JP17 | VCORE EN | | 1-2 | | --- | | Open | | | Connects 1V1 to VCORE. | | --- | | Disconnects 1V1 from VCORE. | |
| JP18 | BLE LDO EN | | 1-2 | | --- | | Open | | | Connects 1V4 to BLE\_LDO. | | --- | | Disconnects 1V4 from BLE\_LDO. | |
| JH6 | ANALOG PORT3 | | 1-2 | | --- | | 3-4 | | Open | | | Connects LPUART0B\_RX (P3.0) to the SWD connector. | | --- | | Connects LPUART0B\_TX (P3.1) to the SWD connector. | | Disconnects LPUART0B\_RX (P3.0) and LPUART0B\_TX (P3.1) from the SWD connector. | |

## Programming and Debugging

The `max32690evkit` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Flashing

The MAX32690 MCU can be flashed by connecting an external debug probe to the
SWD port. SWD debug can be accessed through the Cortex 10-pin connector, J3.
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

- [MAX32690EVKIT solution center](https://developer.analog.com/solutions/max32690)

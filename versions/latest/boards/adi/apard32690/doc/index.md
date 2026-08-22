---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/adi/apard32690/doc/index.html
original_path: boards/adi/apard32690/doc/index.html
---

# AD-APARD32690-SL

Board Overview

[![../../../../_images/apard32690_img.webp](../../../../_images/apard32690_img.webp)
](../../../../_images/apard32690_img.webp)

AD-APARD32690-SL

Name:
:   `apard32690`

Vendor:
:   Analog Devices, Inc.

Architecture:
:   arm

SoC:
:   max32690

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adi/apard32690/doc/index.rst/../..)

## Overview

The AD-APARD32690-SL is a platform for prototyping intelligent, secure, and connected field devices.
It has an Arduino Mega-compatible form factor and two Pmod-compatible connectors.
The system includes the MAX32690 ARM Cortex-M4 with FPU-Based Microcontroller and Bluetooth LE 5.2.
The MCU is coupled with external RAM (2 x 512 Mb) and Flash (64 Mb) memories to meet the requirements
of the most demanding applications. The MAXQ1065 security coprocessor enables state of the art
security features such as for root-of-trust, mutual authentication, data confidentiality and
integrity, secure boot, and secure communications.
A 10 Mbps single-pair Ethernet link using the ADIN1110 10BASE-T1L MAC/PHY, enables remote
data acquisition and system configuration. The 10BASE-T1L interface also supports Single-pair
Power over Ethernet (SPoE) and be used for powering the system via an Arduino shield implementing
the required power circuitry.

The Zephyr port is running on the MAX32690 MCU.

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
  > - Security and Integrity
  >
  >   - ChipDNA Physically Un-clonable Function (PUF)
  >   - Modular Arithmetic Accelerator (MAA), True Random Number Generator (TRNG)
  >   - Secure Nonvolatile Key Storage, SHA-256, AES-128/192/256
  >   - Secure Boot ROM
- External devices connected to the APARD32690:

  - On-Board HyperRAM
  - On-Board SPI Flash
  - USB 2.0 Type-C interface to the MAX32690
  - SPI PMOD connector
  - I2C PMOD connector
  - SWD 10-Pin Header
  - On-Board Bluetooth 5.2 LE Radio antenna
  - MAXQ1065 Ultralow Power Cryptographic Controller with ChipDNA
  - ADIN1110 Robust, Industrial, Low Power 10BASE-T1L Ethernet MAC-PHY
  - U-Blox NINA-W102 802.11b/g/n module with dual-mode Bluetooth v4.2
  - On-Board 5V, 3.3V, 1.8V, and 1.1V voltage regulators
  - 2-Pin external power supply terminal block (5V - 28V DC)
  - Board Power Provided by either the USB Port or the 2-Pin connector
  - Arduino Mega compatible header.
  - Two general-purpose LEDs and one general purpose push button.

### Supported Features

The `apard32690` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `apard32690/max32690/m4` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L25) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | ADI MAX32 ADC SAR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L230) | [`adi,max32-adc-sar`](../../../../build/dts/api/bindings/adc/adi%2Cmax32-adc-sar.md#std-dtcompatible-adi-max32-adc-sar) |
| CAN | on-chip | ADI MAX32 CAN Node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32690.dtsi?plain=1#L257) | [`adi,max32-can`](../../../../build/dts/api/bindings/can/adi%2Cmax32-can.md#std-dtcompatible-adi-max32-can) |
| Clock control | on-chip | MAX32 Global Control[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L118) | [`adi,max32-gcr`](../../../../build/dts/api/bindings/clock/adi%2Cmax32-gcr.md#std-dtcompatible-adi-max32-gcr) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L53)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L60) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | ADI MAX32 counter[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L250) | [`adi,max32-counter`](../../../../build/dts/api/bindings/counter/adi%2Cmax32-counter.md#std-dtcompatible-adi-max32-counter) |
| on-chip | ADI MAX32 compatible Counter RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L318) | [`adi,max32-rtc-counter`](../../../../build/dts/api/bindings/counter/adi%2Cmax32-rtc-counter.md#std-dtcompatible-adi-max32-rtc-counter) |
| DMA | on-chip | ADI MAX32 DMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32690.dtsi?plain=1#L190) | [`adi,max32-dma`](../../../../build/dts/api/bindings/dma/adi%2Cmax32-dma.md#std-dtcompatible-adi-max32-dma) |
| Ethernet | on-board | ADIN1110 standalone 10BASE-T1L Ethernet controller with SPI interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/apard32690/apard32690_max32690_m4.dts?plain=1#L234) | [`adi,adin1110`](../../../../build/dts/api/bindings/ethernet/phy/adi%2Cadin1110.md#std-dtcompatible-adi-adin1110) |
| on-board | ADIN2111 PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/apard32690/apard32690_max32690_m4.dts?plain=1#L250) | [`adi,adin2111-phy`](../../../../build/dts/api/bindings/ethernet/phy/adi%2Cadin2111-phy.md#std-dtcompatible-adi-adin2111-phy) |
| Flash controller | on-chip | MAX32XXX flash controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L102) | [`adi,max32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/adi%2Cmax32-flash-controller.md#std-dtcompatible-adi-max32-flash-controller) |
| GPIO & Headers | on-chip | MAX32 GPIO[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L166) | [`adi,max32-gpio`](../../../../build/dts/api/bindings/gpio/adi%2Cmax32-gpio.md#std-dtcompatible-adi-max32-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/apard32690/apard32690_max32690_m4.dts?plain=1#L58) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| on-board | GPIO pins exposed on a Digilent Pmod interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/apard32690/apard32690_max32690_m4.dts?plain=1#L87) | [`digilent,pmod`](../../../../build/dts/api/bindings/gpio/digilent%2Cpmod.md#std-dtcompatible-digilent-pmod) |
| I2C | on-chip | ADI MAX32 I2C[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L127) | [`adi,max32-i2c`](../../../../build/dts/api/bindings/i2c/adi%2Cmax32-i2c.md#std-dtcompatible-adi-max32-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/apard32690/apard32690_max32690_m4.dts?plain=1#L42) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/apard32690/apard32690_max32690_m4.dts?plain=1#L26) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-board | ADIN2111 MDIO Driver node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/apard32690/apard32690_max32690_m4.dts?plain=1#L245) | [`adi,adin2111-mdio`](../../../../build/dts/api/bindings/mdio/adi%2Cadin2111-mdio.md#std-dtcompatible-adi-adin2111-mdio) |
| Memory controller | on-chip | MAX32 HyperBus (HPB) Memory Controller Interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32690.dtsi?plain=1#L122) | [`adi,max32-hpb`](../../../../build/dts/api/bindings/memory-controllers/adi%2Cmax32-hpb.md#std-dtcompatible-adi-max32-hpb) |
| MTD | on-chip | Flash node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L110) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | MAX32 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L160) | [`adi,max32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/adi%2Cmax32-pinctrl.md#std-dtcompatible-adi-max32-pinctrl) |
| PWM | on-chip | ADI MAX32 PWM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L254) | [`adi,max32-pwm`](../../../../build/dts/api/bindings/pwm/adi%2Cmax32-pwm.md#std-dtcompatible-adi-max32-pwm) |
| RNG | on-chip | ADI MAX32XXX TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L214) | [`adi,max32-trng`](../../../../build/dts/api/bindings/rng/adi%2Cmax32-trng.md#std-dtcompatible-adi-max32-trng) |
| Serial controller | on-chip | MAX32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L187)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L196) | [`adi,max32-uart`](../../../../build/dts/api/bindings/serial/adi%2Cmax32-uart.md#std-dtcompatible-adi-max32-uart) |
| SPI | on-chip | ADI MAX32 SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32690.dtsi?plain=1#L161)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32690.dtsi?plain=1#L131) | [`adi,max32-spi`](../../../../build/dts/api/bindings/spi/adi%2Cmax32-spi.md#std-dtcompatible-adi-max32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L97) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | ADI MAX32 timer[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L242) | [`adi,max32-timer`](../../../../build/dts/api/bindings/timer/adi%2Cmax32-timer.md#std-dtcompatible-adi-max32-timer) |
| USB | on-chip | ADI MAX32 USBHS[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32690.dtsi?plain=1#L245) | [`adi,max32-usbhs`](../../../../build/dts/api/bindings/usb/adi%2Cmax32-usbhs.md#std-dtcompatible-adi-max32-usbhs) |
| 1-Wire | on-chip | ADI MAX32xxx MCUs 1-Wire Master[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32690.dtsi?plain=1#L237) | [`adi,max32-w1`](../../../../build/dts/api/bindings/w1/adi%2Cmax32-w1.md#std-dtcompatible-adi-max32-w1) |
| Watchdog | on-chip | MAX32XXX watchdog[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L221) | [`adi,max32-watchdog`](../../../../build/dts/api/bindings/watchdog/adi%2Cmax32-watchdog.md#std-dtcompatible-adi-max32-watchdog) |

### Connections and IOs

| Name | Name | Settings | Description |
| --- | --- | --- | --- |
| P55 | SWD TX | | 1-2 | | --- | | 2-3 | | | Connects the SWD UART TX to the (UART) RX port of the U-Blox Nina W102. | | --- | | Connects the SWD UART TX to the UART0 TX pin of the MAX32690. | |
| P50 | SWD RX | | 1-2 | | --- | | 2-3 | | | Connects the SWD UART RX to the (UART) TX port of the U-Blox Nina W102. | | --- | | Connects the SWD UART RX to the UART0 RX pin of the MAX32690. | |
| P51 | SWD POW | | 1-2 | | --- | | 2-3 | | | Connects the SWD Vcc pin to 3.3V. | | --- | | Connects the SWD Vcc pin to 1.8V. | |
| P38 | UART RX WIFI | | 1-2 | | --- | | Open | | | Connect the U-Blox Nina W102 UART RX to the UART2A TX pin of the MAX32690 | | --- | | Disconnects the U-Blox Nina W102 UART RX from the UART2A TX pin | |
| P58 | UART TX WIFI | | 1-2 | | --- | | Open | | | Connect the U-Blox Nina W102 UART TX to the UART2A RX pin of the MAX32690. | | --- | | Disconnects the U-Blox Nina W102 UART TX from the UART2A RX pin. | |
| S4 | SW1 | | On | | --- | | Off | | | Pulls the ADIN1110’s SWPD\_EN pin to 3.3V through a resistor. | | --- | | Leaves the ADIN1110’s SWPD\_EN pin floating. | |
| S4 | SW2 | | On | | --- | | Off | | | Pulls the ADIN1110’s CFG0 pin to 3.3V through a resistor. | | --- | | Leaves the ADIN1110’s CFG0 pin floating. | |
| S4 | SW3 | | On | | --- | | Off | | | Pulls the ADIN1110’s CFG1 pin to 3.3V through a resistor. | | --- | | Leaves the ADIN1110’s CFG1 pin floating. | |

## Programming and Debugging

The `apard32690` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Flashing

The MAX32690 MCU can be flashed by connecting an external debug probe to the
SWD port. SWD debug can be accessed through the Cortex 10-pin connector, P9.
Logic levels are either 1.8V or 3.3V (based on P51 selection).

Once the debug probe is connected to your host computer, then you can simply run the
`west flash` command to write a firmware image into flash. To perform a full erase,
pass the `--erase` option when executing `west flash`.

Note

This board uses OpenOCD as the default debug interface. You can also use
a Segger J-Link with Segger’s native tooling by overriding the runner,
appending `--runner jlink` to your `west` command(s). The J-Link should
be connected to the standard 2\*5 pin debug connector (P9) using an
appropriate adapter board and cable.

### Debugging

Please refer to the [Flashing](#flashing) section and run the `west debug` command
instead of `west flash`.

## References

- [AD-APARD32690-SL solution center](https://developer.analog.com/solutions/max32690)

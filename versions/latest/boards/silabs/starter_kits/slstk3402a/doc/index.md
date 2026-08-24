---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/silabs/starter_kits/slstk3402a/doc/index.html
original_path: boards/silabs/starter_kits/slstk3402a/doc/index.html
---

# EFM32 Pearl Gecko 12 (SLSTK3402A)

Board Overview

[![../../../../../_images/slstk3402a.jpg](https://docs.zephyrproject.org/4.2.0/_images/slstk3402a.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/slstk3402a.jpg)

EFM32 Pearl Gecko 12 (SLSTK3402A)

Name:
:   `slstk3402a`

Vendor:
:   Silicon Laboratories

Architecture:
:   arm

SoC:
:   efm32pg12b500f1024gl125, efm32jg12b500f1024gl125

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/starter_kits/slstk3402a/doc/index.rst/../..)

## Overview

The EFM32 Pearl Gecko 12 Starter Kit SLSTK3402A contains an MCU from the
EFM32PG family built on an ARM® Cortex®-M4F processor with excellent low
power capabilities.

## Hardware

- Advanced Energy Monitoring provides real-time information about the energy
  consumption of an application or prototype design.
- Ultra low power 128x128 pixel Memory-LCD
- 2 user buttons, 2 LEDs and a touch slider
- Humidity, temperature, and inductive-capacitive metal sensor
- On-board Segger J-Link USB debugger

For more information about the EFM32PG SoC and SLSTK3402A board:

- [EFM32PG Website](https://www.silabs.com/products/mcu/32-bit/efm32-pearl-gecko)
- [EFM32PG12 Datasheet](https://www.silabs.com/documents/public/data-sheets/efm32pg12-datasheet.pdf)
- [EFM32PG12 Reference Manual](https://www.silabs.com/documents/public/reference-manuals/efm32pg12-rm.pdf)
- [SLSTK3402A Website](https://www.silabs.com/products/development-tools/mcu/32-bit/efm32-pearl-gecko-pg12-starter-kit)
- [SLSTK3402A User Guide](https://www.silabs.com/documents/public/user-guides/ug257-stk3402-usersguide.pdf)
- [SLSTK3402A Schematics](https://www.silabs.com/documents/public/schematic-files/BRD2501A-A01-schematic.pdf)

### Supported Features

The `slstk3402a` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `slstk3402a/efm32jg12b500f1024gl125` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M3 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32jg12b.dtsi?plain=1#L12) | [`arm,cortex-m3`](../../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m3.md#std-dtcompatible-arm-cortex-m3) |
| ADC | on-chip | Silicon Labs Gecko Series 1 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L248) | [`silabs,gecko-adc`](../../../../../build/dts/api/bindings/adc/silabs%2Cgecko-adc.md#std-dtcompatible-silabs-gecko-adc) |
| Flash controller | on-chip | Silicon Labs Gecko flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L33) | [`silabs,gecko-flash-controller`](../../../../../build/dts/api/bindings/flash_controller/silabs%2Cgecko-flash-controller.md#std-dtcompatible-silabs-gecko-flash-controller) |
| GPIO & Headers | on-chip | Silicon Labs Series 0-2 GPIO Peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L121) | [`silabs,gecko-gpio`](../../../../../build/dts/api/bindings/gpio/silabs%2Cgecko-gpio.md#std-dtcompatible-silabs-gecko-gpio) |
| on-chip | Silicon Labs Series 0-2 GPIO Port[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L131)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L149) | [`silabs,gecko-gpio-port`](../../../../../build/dts/api/bindings/gpio/silabs%2Cgecko-gpio-port.md#std-dtcompatible-silabs-gecko-gpio-port) |
| I2C | on-chip | Silicon Labs Series 0-2 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L92)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L102) | [`silabs,gecko-i2c`](../../../../../build/dts/api/bindings/i2c/silabs%2Cgecko-i2c.md#std-dtcompatible-silabs-gecko-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/starter_kits/slstk3402a/slstk3402a_common.dtsi?plain=1#L46) | [`gpio-keys`](../../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/starter_kits/slstk3402a/slstk3402a_common.dtsi?plain=1#L32) | [`gpio-leds`](../../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/starter_kits/slstk3402a/slstk3402a_common.dtsi?plain=1#L64) | [`pwm-leds`](../../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L41) | [`soc-nv-flash`](../../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/starter_kits/slstk3402a/slstk3402a_common.dtsi?plain=1#L149) | [`fixed-partitions`](../../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Silabs Gecko Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L257) | [`silabs,gecko-pinctrl`](../../../../../build/dts/api/bindings/pinctrl/silabs%2Cgecko-pinctrl.md#std-dtcompatible-silabs-gecko-pinctrl) |
| PWM | on-chip | Silabs Gecko PWM port[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L241) | [`silabs,gecko-pwm`](../../../../../build/dts/api/bindings/pwm/silabs%2Cgecko-pwm.md#std-dtcompatible-silabs-gecko-pwm) |
| RNG | on-chip | GECKO TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L229) | [`silabs,gecko-trng`](../../../../../build/dts/api/bindings/rng/silabs%2Cgecko-trng.md#std-dtcompatible-silabs-gecko-trng) |
| RTC | on-chip | Silabs Gecko RTCC (Real-Time Counter)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L112) | [`silabs,gecko-rtcc`](../../../../../build/dts/api/bindings/rtc/silabs%2Cgecko-rtcc.md#std-dtcompatible-silabs-gecko-rtcc) |
| Serial controller | on-chip | Gecko USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L48)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L57) | [`silabs,gecko-usart`](../../../../../build/dts/api/bindings/serial/silabs%2Cgecko-usart.md#std-dtcompatible-silabs-gecko-usart) |
| on-chip | Gecko LEUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L84) | [`silabs,gecko-leuart`](../../../../../build/dts/api/bindings/serial/silabs%2Cgecko-leuart.md#std-dtcompatible-silabs-gecko-leuart) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L28) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| Watchdog | on-chip | Silicon Labs Series 1-2 WDOG[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L213) | [`silabs,gecko-wdog`](../../../../../build/dts/api/bindings/watchdog/silabs%2Cgecko-wdog.md#std-dtcompatible-silabs-gecko-wdog) |

#### `slstk3402a/efm32pg12b500f1024gl125` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32pg12b.dtsi?plain=1#L12) | [`arm,cortex-m4f`](../../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | Silicon Labs Gecko Series 1 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L248) | [`silabs,gecko-adc`](../../../../../build/dts/api/bindings/adc/silabs%2Cgecko-adc.md#std-dtcompatible-silabs-gecko-adc) |
| Flash controller | on-chip | Silicon Labs Gecko flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L33) | [`silabs,gecko-flash-controller`](../../../../../build/dts/api/bindings/flash_controller/silabs%2Cgecko-flash-controller.md#std-dtcompatible-silabs-gecko-flash-controller) |
| GPIO & Headers | on-chip | Silicon Labs Series 0-2 GPIO Peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L121) | [`silabs,gecko-gpio`](../../../../../build/dts/api/bindings/gpio/silabs%2Cgecko-gpio.md#std-dtcompatible-silabs-gecko-gpio) |
| on-chip | Silicon Labs Series 0-2 GPIO Port[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L131)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L149) | [`silabs,gecko-gpio-port`](../../../../../build/dts/api/bindings/gpio/silabs%2Cgecko-gpio-port.md#std-dtcompatible-silabs-gecko-gpio-port) |
| I2C | on-chip | Silicon Labs Series 0-2 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L92)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L102) | [`silabs,gecko-i2c`](../../../../../build/dts/api/bindings/i2c/silabs%2Cgecko-i2c.md#std-dtcompatible-silabs-gecko-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/starter_kits/slstk3402a/slstk3402a_common.dtsi?plain=1#L46) | [`gpio-keys`](../../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/starter_kits/slstk3402a/slstk3402a_common.dtsi?plain=1#L32) | [`gpio-leds`](../../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/starter_kits/slstk3402a/slstk3402a_common.dtsi?plain=1#L64) | [`pwm-leds`](../../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L41) | [`soc-nv-flash`](../../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/starter_kits/slstk3402a/slstk3402a_common.dtsi?plain=1#L149) | [`fixed-partitions`](../../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Silabs Gecko Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L257) | [`silabs,gecko-pinctrl`](../../../../../build/dts/api/bindings/pinctrl/silabs%2Cgecko-pinctrl.md#std-dtcompatible-silabs-gecko-pinctrl) |
| PWM | on-chip | Silabs Gecko PWM port[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L241) | [`silabs,gecko-pwm`](../../../../../build/dts/api/bindings/pwm/silabs%2Cgecko-pwm.md#std-dtcompatible-silabs-gecko-pwm) |
| RNG | on-chip | GECKO TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L229) | [`silabs,gecko-trng`](../../../../../build/dts/api/bindings/rng/silabs%2Cgecko-trng.md#std-dtcompatible-silabs-gecko-trng) |
| RTC | on-chip | Silabs Gecko RTCC (Real-Time Counter)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L112) | [`silabs,gecko-rtcc`](../../../../../build/dts/api/bindings/rtc/silabs%2Cgecko-rtcc.md#std-dtcompatible-silabs-gecko-rtcc) |
| Serial controller | on-chip | Gecko USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L48)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L57) | [`silabs,gecko-usart`](../../../../../build/dts/api/bindings/serial/silabs%2Cgecko-usart.md#std-dtcompatible-silabs-gecko-usart) |
| on-chip | Gecko LEUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L84) | [`silabs,gecko-leuart`](../../../../../build/dts/api/bindings/serial/silabs%2Cgecko-leuart.md#std-dtcompatible-silabs-gecko-leuart) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L28) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| Watchdog | on-chip | Silicon Labs Series 1-2 WDOG[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_jg_pg_12b.dtsi?plain=1#L213) | [`silabs,gecko-wdog`](../../../../../build/dts/api/bindings/watchdog/silabs%2Cgecko-wdog.md#std-dtcompatible-silabs-gecko-wdog) |

#### EFM32 Jade Gecko SoC

The EFM32 Pearl Gecko Starter Kit SLSTK3402A can also be used to evaluate
the EFM32 Jade Gecko SoC (EFM32JG12). The only difference between the Pearl
Gecko and the Jade Gecko is their core. The Pearl Gecko contains an ARM®
Cortex®-M4F core, and the Jade Gecko an ARM® Cortex®-M3 core. Other features
such as memory and peripherals are the same.

Code that is built for the Jade Gecko also runs on an equivalent Pearl Gecko.

To build firmware for the Jade Gecko and run it on the EFM32 Pearl Gecko Starter
Kit, use the board `slstk3402a/efm32jg12b500f1024gl125` instead of
`slstk3402a/efm32pg12b500f1024gl125`.

### Connections and IOs

The EFM32PG12 SoC has twelve GPIO controllers (PORTA to PORTL), but only four
are currently enabled (PORTA, PORTB, PORTD and PORTF) for the SLSTK3402A
board.

In the following table, the column **Name** contains pin names. For example, PE2
means pin number 2 on PORTE, as used in the board’s datasheets and manuals.

| Name | Function | Usage |
| --- | --- | --- |
| PF4 | GPIO | LED0 |
| PF5 | GPIO | LED1 |
| PF6 | GPIO | Push Button PB0 |
| PF7 | GPIO | Push Button PB1 |
| PA5 | GPIO | Board Controller Enable EFM\_BC\_EN |
| PA0 | UART\_TX | UART TX Console VCOM\_TX US0\_TX #0 |
| PA1 | UART\_RX | UART RX Console VCOM\_RX US0\_RX #0 |
| PD10 | UART\_TX | EXP12\_UART\_TX LEU0\_TX #18 |
| PD11 | UART\_RX | EXP14\_UART\_RX LEU0\_RX #18 |
| PC10 | I2C\_SDA | ENV\_I2C\_SDA I2C0\_SDA #15 |
| PC11 | I2C\_SCL | ENV\_I2C\_SCL I2C0\_SCL #15 |

### System Clock

The EFM32PG12 SoC is configured to use the 40 MHz external oscillator on the
board.

### Serial Port

The EFM32PG12 SoC has four USARTs and one Low Energy UART (LEUART).

## Programming and Debugging

The `slstk3402a` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Note

Before using the kit the first time, you should update the J-Link firmware
in Simplicity Studio.

### Flashing

The SLSTK3402A includes an [J-Link](https://www.segger.com/jlink-debug-probes.html) serial and debug adaptor built into the
board. The adaptor provides:

- A USB connection to the host computer, which exposes a mass storage device and a
  USB serial port.
- A serial flash device, which implements the USB flash disk file storage.
- A physical UART connection which is relayed over interface USB serial port.

#### Flashing an application to SLSTK3402A

The sample application [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") is used for this example.
Build the Zephyr kernel and application:

```shell
# From the root of the zephyr repository
west build -b slstk3402a/efm32pg12b500f1024gl125 samples/hello_world
```

Connect the SLSTK3402A to your host computer using the USB port and you
should see a USB connection which exposes a mass storage device(STK3402A).
Copy the generated zephyr.bin to the STK3402A drive.

Use a USB-to-UART converter such as an FT232/CP2102 to connect to the UART on the
expansion header.

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you’ll see the following message on the corresponding serial port
terminal session:

```shell
Hello World! slstk3402a
```

---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/silabs/starter_kits/slstk3701a/doc/index.html
original_path: boards/silabs/starter_kits/slstk3701a/doc/index.html
---

# EFM32 Giant Gecko 11 (SLSTK3701A)

Board Overview

[![../../../../../_images/slstk3701a.jpg](https://docs.zephyrproject.org/4.1.0/_images/slstk3701a.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/slstk3701a.jpg)

EFM32 Giant Gecko 11 (SLSTK3701A)

Name:
:   `slstk3701a`

Vendor:
:   Silicon Laboratories

Architecture:
:   arm

SoC:
:   efm32gg11b820f2048gl192

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/starter_kits/slstk3701a/doc/index.rst/../..)

## Overview

The EFM32 Giant Gecko Starter Kit SLSTK3701A contains an MCU from the
EFM32GG Series 1 family built on an ARM® Cortex®-M4F processor with excellent
low power capabilities.

## Hardware

- Advanced Energy Monitoring provides real-time information about the energy
  consumption of an application or prototype design.
- Ultra low power 128x128 pixel color Memory-LCD
- 2 user buttons, 2 LEDs and a touch slider
- Relative humidity, magnetic Hall Effect and inductive-capacitive metal sensor
- USB interface for Host/Device/OTG
- 32 Mb Quad-SPI Flash memory
- SD card slot
- RJ-45 Ethernet jack
- 2 digital microphones
- On-board Segger J-Link USB debugger

For more information about the EFM32GG11 SoC and SLSTK3701A board:

- [EFM32GG Series 1 Website](https://www.silabs.com/products/mcu/32-bit/efm32-giant-gecko-s1)
- [EFM32GG11 Datasheet](https://www.silabs.com/documents/public/data-sheets/efm32gg11-datasheet.pdf)
- [EFM32GG11 Reference Manual](https://www.silabs.com/documents/public/reference-manuals/efm32gg11-rm.pdf)
- [SLSTK3701A Website](https://www.silabs.com/products/development-tools/mcu/32-bit/efm32-giant-gecko-gg11-starter-kit)
- [SLSTK3701A User Guide](https://www.silabs.com/documents/public/user-guides/ug287-stk3701.pdf)
- [SLSTK3701A Schematics](https://www.silabs.com/documents/public/schematic-files/BRD2204A-B00-schematic.pdf)

### Supported Features

The `slstk3701a` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `slstk3701a/efm32gg11b820f2048gl192` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L23) | [`arm,cortex-m4f`](../../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| Ethernet | on-chip | SiLabs Gecko Ethernet[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b820f2048gl192.dtsi?plain=1#L26) | [`silabs,gecko-ethernet`](../../../../../build/dts/api/bindings/ethernet/silabs%2Cgecko-ethernet.md#std-dtcompatible-silabs-gecko-ethernet) |
| Flash controller | on-chip | Silicon Labs Gecko flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L34) | [`silabs,gecko-flash-controller`](../../../../../build/dts/api/bindings/flash_controller/silabs%2Cgecko-flash-controller.md#std-dtcompatible-silabs-gecko-flash-controller) |
| GPIO & Headers | on-chip | SiLabs Gecko GPIO node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L176) | [`silabs,gecko-gpio`](../../../../../build/dts/api/bindings/gpio/silabs%2Cgecko-gpio.md#std-dtcompatible-silabs-gecko-gpio) |
| on-chip | SiLabs Gecko GPIO port node[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L186) | [`silabs,gecko-gpio-port`](../../../../../build/dts/api/bindings/gpio/silabs%2Cgecko-gpio-port.md#std-dtcompatible-silabs-gecko-gpio-port) |
| I2C | on-chip | Silabs Gecko I2C[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L146) | [`silabs,gecko-i2c`](../../../../../build/dts/api/bindings/i2c/silabs%2Cgecko-i2c.md#std-dtcompatible-silabs-gecko-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/starter_kits/slstk3701a/slstk3701a.dts?plain=1#L45) | [`gpio-keys`](../../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/starter_kits/slstk3701a/slstk3701a.dts?plain=1#L33) | [`gpio-leds`](../../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L42) | [`soc-nv-flash`](../../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/starter_kits/slstk3701a/slstk3701a.dts?plain=1#L178) | [`fixed-partitions`](../../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | The Silabs pin controller is a singleton node responsible for controlling pin function selection and pin properties[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L291) | [`silabs,gecko-pinctrl`](../../../../../build/dts/api/bindings/pinctrl/silabs%2Cgecko-pinctrl.md#std-dtcompatible-silabs-gecko-pinctrl) |
| RNG | on-chip | GECKO TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L268) | [`silabs,gecko-trng`](../../../../../build/dts/api/bindings/rng/silabs%2Cgecko-trng.md#std-dtcompatible-silabs-gecko-trng) |
| RTC | on-chip | Silabs Gecko RTCC (Real-Time Counter)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L49) | [`silabs,gecko-rtcc`](../../../../../build/dts/api/bindings/rtc/silabs%2Cgecko-rtcc.md#std-dtcompatible-silabs-gecko-rtcc) |
| Serial controller | on-chip | Gecko UART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L58) | [`silabs,gecko-uart`](../../../../../build/dts/api/bindings/serial/silabs%2Cgecko-uart.md#std-dtcompatible-silabs-gecko-uart) |
| on-chip | Gecko USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L76)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L85) | [`silabs,gecko-usart`](../../../../../build/dts/api/bindings/serial/silabs%2Cgecko-usart.md#std-dtcompatible-silabs-gecko-usart) |
| on-chip | Gecko LEUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L130)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L138) | [`silabs,gecko-leuart`](../../../../../build/dts/api/bindings/serial/silabs%2Cgecko-leuart.md#std-dtcompatible-silabs-gecko-leuart) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L29) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| Watchdog | on-chip | Silicon Labs Gecko Family Watchdog driver[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L275)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L283) | [`silabs,gecko-wdog`](../../../../../build/dts/api/bindings/watchdog/silabs%2Cgecko-wdog.md#std-dtcompatible-silabs-gecko-wdog) |

### Connections and IOs

The EFM32GG11 SoC has nine GPIO controllers (PORTA to PORTI), all of which are
currently enabled for the SLSTK3701A board.

In the following table, the column **Name** contains pin names. For example, PE1
means pin number 1 on PORTE, as used in the board’s datasheets and manuals.

| Name | Function | Usage |
| --- | --- | --- |
| PH10 | GPIO | LED0 red |
| PH11 | GPIO | LED0 green |
| PH12 | GPIO | LED0 blue |
| PH13 | GPIO | LED1 red |
| PH14 | GPIO | LED1 green |
| PH15 | GPIO | LED1 blue |
| PC8 | GPIO | Push Button PB0 |
| PC9 | GPIO | Push Button PB1 |
| PE1 | GPIO | Board Controller Enable EFM\_BC\_EN |
| PH4 | UART\_TX | UART TX Console VCOM\_TX US0\_TX #4 |
| PH5 | UART\_RX | UART RX Console VCOM\_RX US0\_RX #4 |
| PI4 | I2C\_SDA | SENSOR\_I2C\_SDA I2C2\_SDA #7 |
| PI5 | I2C\_SCL | SENSOR\_I2C\_SCL I2C2\_SCL #7 |

### System Clock

The EFM32GG11 SoC is configured to use the 50 MHz external oscillator on the
board.

### Serial Port

The EFM32GG11 SoC has six USARTs, two UARTs and two Low Energy UARTs (LEUART).
USART4 is connected to the board controller and is used for the console.

## Programming and Debugging

Note

Before using the kit the first time, you should update the J-Link firmware
in Simplicity Studio.

### Flashing

The SLSTK3701A includes an [J-Link](https://www.segger.com/jlink-debug-probes.html) serial and debug adaptor built into the
board. The adaptor provides:

- A USB connection to the host computer, which exposes a mass storage device and a
  USB serial port.
- A serial flash device, which implements the USB flash disk file storage.
- A physical UART connection which is relayed over interface USB serial port.

#### Flashing an application to SLSTK3701A

The sample application [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") is used for this example.
Build the Zephyr kernel and application:

```shell
# From the root of the zephyr repository
west build -b slstk3701a samples/hello_world
```

Connect the SLSTK3701A to your host computer using the USB port and you
should see a USB connection which exposes a mass storage device(STK3701A) and
a USB Serial Port. Copy the generated zephyr.bin to the STK3701A drive.

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you’ll see the following message on the corresponding serial port
terminal session:

```shell
Hello World! slstk3701a
```

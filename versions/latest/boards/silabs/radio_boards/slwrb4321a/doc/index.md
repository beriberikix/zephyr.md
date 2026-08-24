---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/silabs/radio_boards/slwrb4321a/doc/index.html
original_path: boards/silabs/radio_boards/slwrb4321a/doc/index.html
---

# WGM160P Wi-Fi Module (SLWRB4321A)

Board Overview

[![../../../../../_images/wgm160p-starter-kit.jpg](https://docs.zephyrproject.org/4.2.0/_images/wgm160p-starter-kit.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/wgm160p-starter-kit.jpg)

WGM160P Wi-Fi Module (SLWRB4321A)

Name:
:   `slwrb4321a`

Vendor:
:   Silicon Laboratories

Architecture:
:   arm

SoC:
:   efm32gg11b820f2048gm64

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/radio_boards/slwrb4321a/doc/index.rst/../..)

## Overview

The WGM160P Starter Kit SLWSTK6121A comes with the BRD4321A radio board.
This radio boards contains a WGM160P module, which combines the WF200 Wi-Fi
transceiver with an EFM32GG11 microcontroller.

## Hardware

- Advanced Energy Monitoring provides real-time information about the energy
  consumption of an application or prototype design.
- Ultra low power 128x128 pixel color Memory-LCD
- 2 user buttons and 2 LEDs
- Si7021 Humidity and Temperature Sensor
- On-board Segger J-Link USB and Ethernet debugger
- 10/100Base-TX ethernet PHY and RJ-45 jack (on included expansion board)
- MicroSD card slot
- USB Micro-AB connector

For more information about the WGM160P and SLWSTK6121A board:

- [WGM160P Website](https://www.silabs.com/wireless/wi-fi/wfm160-series-1-modules)
- [WGM160P Datasheet](https://www.silabs.com/documents/public/data-sheets/wgm160p-datasheet.pdf)
- [SLWSTK6121A Website](https://www.silabs.com/development-tools/wireless/wi-fi/wgm160p-wifi-module-starter-kit)
- [SLWSTK6121A User Guide](https://www.silabs.com/documents/public/user-guides/ug351-brd4321a-user-guide.pdf)
- [EFM32GG11 Datasheet](https://www.silabs.com/documents/public/data-sheets/efm32gg11-datasheet.pdf)
- [EFM32GG11 Reference Manual](https://www.silabs.com/documents/public/reference-manuals/efm32gg11-rm.pdf)
- [WF200 Datasheet](https://www.silabs.com/documents/public/data-sheets/wf200-datasheet.pdf)

### Supported Features

The `slwrb4321a` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `slwrb4321a/efm32gg11b820f2048gm64` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L23) | [`arm,cortex-m4f`](../../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| Ethernet | on-chip | SiLabs Gecko Ethernet[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b820f2048gl192.dtsi?plain=1#L26) | [`silabs,gecko-ethernet`](../../../../../build/dts/api/bindings/ethernet/silabs%2Cgecko-ethernet.md#std-dtcompatible-silabs-gecko-ethernet) |
| Flash controller | on-chip | Silicon Labs Gecko flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L34) | [`silabs,gecko-flash-controller`](../../../../../build/dts/api/bindings/flash_controller/silabs%2Cgecko-flash-controller.md#std-dtcompatible-silabs-gecko-flash-controller) |
| GPIO & Headers | on-chip | Silicon Labs Series 0-2 GPIO Peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L176) | [`silabs,gecko-gpio`](../../../../../build/dts/api/bindings/gpio/silabs%2Cgecko-gpio.md#std-dtcompatible-silabs-gecko-gpio) |
| on-chip | Silicon Labs Series 0-2 GPIO Port[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L186)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L240) | [`silabs,gecko-gpio-port`](../../../../../build/dts/api/bindings/gpio/silabs%2Cgecko-gpio-port.md#std-dtcompatible-silabs-gecko-gpio-port) |
| I2C | on-chip | Silicon Labs Series 0-2 I2C[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L146)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L166) | [`silabs,gecko-i2c`](../../../../../build/dts/api/bindings/i2c/silabs%2Cgecko-i2c.md#std-dtcompatible-silabs-gecko-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/slwrb4321a/slwrb4321a.dts?plain=1#L49) | [`gpio-keys`](../../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/slwrb4321a/slwrb4321a.dts?plain=1#L35) | [`gpio-leds`](../../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L42) | [`soc-nv-flash`](../../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/slwrb4321a/slwrb4321a.dts?plain=1#L150) | [`fixed-partitions`](../../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Silabs Gecko Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L291) | [`silabs,gecko-pinctrl`](../../../../../build/dts/api/bindings/pinctrl/silabs%2Cgecko-pinctrl.md#std-dtcompatible-silabs-gecko-pinctrl) |
| RNG | on-chip | GECKO TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L268) | [`silabs,gecko-trng`](../../../../../build/dts/api/bindings/rng/silabs%2Cgecko-trng.md#std-dtcompatible-silabs-gecko-trng) |
| RTC | on-chip | Silabs Gecko RTCC (Real-Time Counter)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L49) | [`silabs,gecko-rtcc`](../../../../../build/dts/api/bindings/rtc/silabs%2Cgecko-rtcc.md#std-dtcompatible-silabs-gecko-rtcc) |
| Serial controller | on-chip | Gecko UART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L58) | [`silabs,gecko-uart`](../../../../../build/dts/api/bindings/serial/silabs%2Cgecko-uart.md#std-dtcompatible-silabs-gecko-uart) |
| on-chip | Gecko USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L76)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L85) | [`silabs,gecko-usart`](../../../../../build/dts/api/bindings/serial/silabs%2Cgecko-usart.md#std-dtcompatible-silabs-gecko-usart) |
| on-chip | Gecko LEUART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L130) | [`silabs,gecko-leuart`](../../../../../build/dts/api/bindings/serial/silabs%2Cgecko-leuart.md#std-dtcompatible-silabs-gecko-leuart) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L29) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| Watchdog | on-chip | Silicon Labs Series 1-2 WDOG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L275)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32gg11b.dtsi?plain=1#L283) | [`silabs,gecko-wdog`](../../../../../build/dts/api/bindings/watchdog/silabs%2Cgecko-wdog.md#std-dtcompatible-silabs-gecko-wdog) |

### Connections and IOs

The WGM160P’s EFM32GG11 SoC has six GPIO controllers (PORTA to PORTF), all of which are
currently enabled for the SLWSTK6121A board.

In the following table, the column **Name** contains pin names. For example, PE1
means pin number 1 on PORTE, as used in the board’s datasheets and manuals.

| Name | Function | Usage |
| --- | --- | --- |
| PA4 | GPIO | LED0 |
| PA5 | GPIO | LED1 |
| PD6 | GPIO | Push Button PB0 |
| PD8 | GPIO | Push Button PB1 |
| PE7 | UART\_TX | UART TX Console VCOM\_TX US0\_TX #1 |
| PE6 | UART\_RX | UART RX Console VCOM\_RX US0\_RX #1 |
| PB11 | I2C\_SDA | SENSOR\_I2C\_SDA I2C1\_SDA #1 |
| PB12 | I2C\_SCL | SENSOR\_I2C\_SCL I2C1\_SCL #1 |

### System Clock

The EFM32GG11 SoC is configured to use the 50 MHz external oscillator on the
board.

### Serial Port

The EFM32GG11 SoC has four USARTs, two UARTs and two Low Energy UARTs (LEUART).
USART0 is connected to the board controller and is used for the console.

## Programming and Debugging

The `slwrb4321a` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |
| **[openocd](../../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |

Note

Before using the kit the first time, you should update the J-Link firmware
in Simplicity Studio.

### Flashing

The SLWSTK6121A includes an [J-Link](https://www.segger.com/jlink-debug-probes.html) serial and debug adaptor built into the
board. The adaptor provides:

- A USB connection to the host computer
- A physical UART connection which is relayed over interface USB serial port.

#### Flashing an application to SLWSTK6121A

Connect the SLWSTK6121A to your host computer using the USB port.

Here is an example to build and flash the [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b slwrb4321a samples/hello_world
west flash
```

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you’ll see the following message on the corresponding serial port
terminal session:

```shell
Hello World! slwrb4321a
```

---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/silabs/radio_boards/slwrb4255a/doc/index.html
original_path: boards/silabs/radio_boards/slwrb4255a/doc/index.html
---

# EFR32FG13 2400/915 MHz 19 dBm Dual Band (SLWRB4255A)

Board Overview

[![../../../../../_images/efr32fg13-slwrb4255a.jpg](https://docs.zephyrproject.org/4.2.0/_images/efr32fg13-slwrb4255a.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/efr32fg13-slwrb4255a.jpg)

EFR32FG13 2400/915 MHz 19 dBm Dual Band (SLWRB4255A)

Name:
:   `slwrb4255a`

Vendor:
:   Silicon Laboratories

Architecture:
:   arm

SoC:
:   efr32fg13p233f512gm48

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/radio_boards/slwrb4255a/doc/index.rst/../..)

## Overview

The EFR32FG13P Flex Gecko 2.4 GHz and 915 MHz Radio Board is delivered as a
[standalone Proprietary Wireless radio board](https://www.silabs.com/development-tools/wireless/proprietary/slwrb4255a-efr32fg13-915-mhz-radio-board). It contains a EFR32FG13P Wireless
SoC built on an ARM Cortex®-M4F processor with excellent low power capabilities.

The BRD4255A a.k.a. SLWRB4255A radio board plugs into the Wireless Starter Kit
Mainboard BRD4001A and is supported as one of [Radio Boards](../../index.md#silabs-radio-boards).

## Hardware

- EFR32FG13P233F512GM48 Flex Gecko SoC
- CPU core: ARM Cortex®-M4 with FPU
- Flash memory: 512 kB
- RAM: 64 kB
- Transmit power: up to 19 dBm
- Operation frequency: 2.4 GHz, 915 MHz
- Crystals for LFXO (32.768 kHz) and HFXO (38.4 MHz).

For more information about the EFR32FG13 SoC and BRD4255A board, refer to these
documents:

- [EFR32FG13 Website](https://www.silabs.com/wireless/proprietary/efr32fg13-series-1-sub-ghz-2-4-ghz-socs)
- [EFR32FG13 Datasheet](https://www.silabs.com/documents/public/data-sheets/efr32fg13-datasheet.pdf)
- [EFR32xG13 Reference Manual](https://www.silabs.com/documents/public/reference-manuals/efr32xg13-rm.pdf)
- [BRD4255A Reference Manual](https://www.silabs.com/documents/public/reference-manuals/brd4255a-rm.pdf)

### Supported Features

The `slwrb4255a` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `slwrb4255a/efr32fg13p233f512gm48` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32xg13p.dtsi?plain=1#L21) | [`arm,cortex-m4f`](../../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| Bluetooth | on-chip | Silicon Labs Series 2 Bluetooth HCI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32xg13p.dtsi?plain=1#L184) | [`silabs,bt-hci-efr32`](../../../../../build/dts/api/bindings/bluetooth/silabs,bt-hci-efr32.md#std-dtcompatible-silabs-bt-hci-efr32) |
| Flash controller | on-chip | Silicon Labs Gecko flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32xg13p.dtsi?plain=1#L32) | [`silabs,gecko-flash-controller`](../../../../../build/dts/api/bindings/flash_controller/silabs,gecko-flash-controller.md#std-dtcompatible-silabs-gecko-flash-controller) |
| GPIO & Headers | on-chip | Silicon Labs Series 0-2 GPIO Peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32xg13p.dtsi?plain=1#L111) | [`silabs,gecko-gpio`](../../../../../build/dts/api/bindings/gpio/silabs,gecko-gpio.md#std-dtcompatible-silabs-gecko-gpio) |
| on-chip | Silicon Labs Series 0-2 GPIO Port[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32xg13p.dtsi?plain=1#L121) | [`silabs,gecko-gpio-port`](../../../../../build/dts/api/bindings/gpio/silabs,gecko-gpio-port.md#std-dtcompatible-silabs-gecko-gpio-port) |
| I2C | on-chip | Silicon Labs Series 0-2 I2C[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32xg13p.dtsi?plain=1#L82) | [`silabs,gecko-i2c`](../../../../../build/dts/api/bindings/i2c/silabs,gecko-i2c.md#std-dtcompatible-silabs-gecko-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/slwrb4255a/../common/efr32-series1-common.dtsi?plain=1#L43) | [`gpio-keys`](../../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/slwrb4255a/../common/efr32-series1-common.dtsi?plain=1#L29) | [`gpio-leds`](../../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32xg13p.dtsi?plain=1#L40) | [`soc-nv-flash`](../../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/slwrb4255a/slwrb4255a.dts?plain=1#L23) | [`fixed-partitions`](../../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-board | Properties supporting Zephyr spi-nor flash driver (over the Zephyr SPI API) control of serial flash memories using the standard M25P80-based command set[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/slwrb4255a/../common/efr32-series1-common.dtsi?plain=1#L82) | [`jedec,spi-nor`](../../../../../build/dts/api/bindings/mtd/jedec,spi-nor.md#std-dtcompatible-jedec-spi-nor) |
| Pin control | on-chip | Silabs Gecko Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32xg13p.dtsi?plain=1#L189) | [`silabs,gecko-pinctrl`](../../../../../build/dts/api/bindings/pinctrl/silabs,gecko-pinctrl.md#std-dtcompatible-silabs-gecko-pinctrl) |
| RTC | on-chip | Silabs Gecko RTCC (Real-Time Counter)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32xg13p.dtsi?plain=1#L102) | [`silabs,gecko-rtcc`](../../../../../build/dts/api/bindings/rtc/silabs,gecko-rtcc.md#std-dtcompatible-silabs-gecko-rtcc) |
| Serial controller | on-chip | Gecko USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32xg13p.dtsi?plain=1#L47)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32xg13p.dtsi?plain=1#L65) | [`silabs,gecko-usart`](../../../../../build/dts/api/bindings/serial/silabs,gecko-usart.md#std-dtcompatible-silabs-gecko-usart) |
| on-chip | Gecko LEUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32xg13p.dtsi?plain=1#L74) | [`silabs,gecko-leuart`](../../../../../build/dts/api/bindings/serial/silabs,gecko-leuart.md#std-dtcompatible-silabs-gecko-leuart) |
| SPI | on-chip | Silicon Labs Series 2 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32xg13p.dtsi?plain=1#L56) | [`silabs,usart-spi`](../../../../../build/dts/api/bindings/spi/silabs,usart-spi.md#std-dtcompatible-silabs-usart-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32xg13p.dtsi?plain=1#L27) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| Watchdog | on-chip | Silicon Labs Series 1-2 WDOG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32xg13p.dtsi?plain=1#L167)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efr32xg13p.dtsi?plain=1#L175) | [`silabs,gecko-wdog`](../../../../../build/dts/api/bindings/watchdog/silabs,gecko-wdog.md#std-dtcompatible-silabs-gecko-wdog) |

### Connections and IOs

In the following table, the column **Pin** contains Pin names. For example, PA2
means Pin number 2 on PORTA, as used in the board’s datasheets and manuals.

| Pin | Function | Usage |
| --- | --- | --- |
| PF4 | GPIO | LED0 |
| PF5 | GPIO | LED1 |
| PF6 | GPIO | Push Button PB0 |
| PF7 | GPIO | Push Button PB1 |
| PA5 | GPIO | Board Controller Enable VCOM\_ENABLE |
| PA0 | USART0\_TX | UART Console VCOM\_TX US0\_TX #0 |
| PA1 | USART0\_RX | UART Console VCOM\_RX US0\_RX #0 |
| PC6 | SPI\_MOSI | Flash MOSI US1\_TX #11 |
| PC7 | SPI\_MISO | Flash MISO US1\_RX #11 |
| PC8 | SPI\_SCLK | Flash SCLK US1\_CLK #11 |
| PA4 | SPI\_CS | Flash Chip Select (GPIO) |

### System Clock

The EFR32FG13P SoC is configured to use the 38.4 MHz external oscillator on the
board.

### Serial Port

The EFR32FG13P SoC has three USARTs and one Low Energy UARTs (LEUART).
USART0 is connected to the board controller and is used for the console.

## Programming and Debugging

The `slwrb4255a` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |
| **[openocd](../../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |

### Flashing

Connect the BRD4001A board with a mounted BRD4255A radio module to your host
computer using the USB port.

Here is an example for the [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b slwrb4255a samples/hello_world
west flash
```

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you should see the following message in the terminal:

```shell
Hello World! slwrb4255a
```

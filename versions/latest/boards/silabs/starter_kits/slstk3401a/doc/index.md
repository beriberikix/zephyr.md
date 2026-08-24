---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/silabs/starter_kits/slstk3401a/doc/index.html
original_path: boards/silabs/starter_kits/slstk3401a/doc/index.html
---

# EFM32 Pearl Gecko (SLSTK3401A)

Board Overview

[![../../../../../_images/slstk3401a.jpg](https://docs.zephyrproject.org/4.2.0/_images/slstk3401a.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/slstk3401a.jpg)

EFM32 Pearl Gecko (SLSTK3401A)

Name:
:   `slstk3401a`

Vendor:
:   Silicon Laboratories

Architecture:
:   arm

SoC:
:   efm32pg1b200f256gm48

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/starter_kits/slstk3401a/doc/index.rst/../..)

## Overview

The EFM32 Pearl Gecko Starter Kit SLSTK3401A contains an MCU from the
EFM32PG family built on an ARM® Cortex®-M4F processor with excellent low
power capabilities.

## Hardware

- Advanced Energy Monitoring provides real-time information about the energy
  consumption of an application or prototype design.
- Ultra low power 128x128 pixel Memory-LCD
- 2 user buttons, 2 LEDs and 2 capacitive buttons
- Humidity and temperature sensor
- On-board Segger J-Link USB debugger

For more information about the EFM32PG SoC and SLSTK3401A board:

- [EFM32PG Website](https://www.silabs.com/products/mcu/32-bit/efm32-pearl-gecko)
- [EFM32PG1 Datasheet](https://www.silabs.com/documents/public/data-sheets/efm32pg1-datasheet.pdf)
- [EFM32PG1 Reference Manual](https://www.silabs.com/documents/public/reference-manuals/efm32pg1-rm.pdf)
- [SLSTK3401A Website](https://www.silabs.com/development-tools/mcu/32-bit/efm32pg1-starter-kit)
- [SLSTK3401A User Guide](https://www.silabs.com/documents/public/user-guides/ug154-stk3401-user-guide.pdf)

### Supported Features

The `slstk3401a` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `slstk3401a/efm32pg1b200f256gm48` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32pg1b.dtsi?plain=1#L11) | [`arm,cortex-m4f`](../../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| Flash controller | on-chip | Silicon Labs Gecko flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_pg_1b.dtsi?plain=1#L28) | [`silabs,gecko-flash-controller`](../../../../../build/dts/api/bindings/flash_controller/silabs%2Cgecko-flash-controller.md#std-dtcompatible-silabs-gecko-flash-controller) |
| GPIO & Headers | on-chip | Silicon Labs Series 0-2 GPIO Peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_pg_1b.dtsi?plain=1#L88) | [`silabs,gecko-gpio`](../../../../../build/dts/api/bindings/gpio/silabs%2Cgecko-gpio.md#std-dtcompatible-silabs-gecko-gpio) |
| on-chip | Silicon Labs Series 0-2 GPIO Port[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_pg_1b.dtsi?plain=1#L98) | [`silabs,gecko-gpio-port`](../../../../../build/dts/api/bindings/gpio/silabs%2Cgecko-gpio-port.md#std-dtcompatible-silabs-gecko-gpio-port) |
| I2C | on-chip | Silicon Labs Series 0-2 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_pg_1b.dtsi?plain=1#L69) | [`silabs,gecko-i2c`](../../../../../build/dts/api/bindings/i2c/silabs%2Cgecko-i2c.md#std-dtcompatible-silabs-gecko-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/starter_kits/slstk3401a/slstk3401a-common.dtsi?plain=1#L43) | [`gpio-keys`](../../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/starter_kits/slstk3401a/slstk3401a-common.dtsi?plain=1#L29) | [`gpio-leds`](../../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_pg_1b.dtsi?plain=1#L36) | [`soc-nv-flash`](../../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/starter_kits/slstk3401a/slstk3401a-common.dtsi?plain=1#L127) | [`fixed-partitions`](../../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Silabs Gecko Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_pg_1b.dtsi?plain=1#L142) | [`silabs,gecko-pinctrl`](../../../../../build/dts/api/bindings/pinctrl/silabs%2Cgecko-pinctrl.md#std-dtcompatible-silabs-gecko-pinctrl) |
| RTC | on-chip | Silabs Gecko RTCC (Real-Time Counter)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_pg_1b.dtsi?plain=1#L79) | [`silabs,gecko-rtcc`](../../../../../build/dts/api/bindings/rtc/silabs%2Cgecko-rtcc.md#std-dtcompatible-silabs-gecko-rtcc) |
| Serial controller | on-chip | Gecko USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_pg_1b.dtsi?plain=1#L43)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_pg_1b.dtsi?plain=1#L52) | [`silabs,gecko-usart`](../../../../../build/dts/api/bindings/serial/silabs%2Cgecko-usart.md#std-dtcompatible-silabs-gecko-usart) |
| on-chip | Gecko LEUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_pg_1b.dtsi?plain=1#L61) | [`silabs,gecko-leuart`](../../../../../build/dts/api/bindings/serial/silabs%2Cgecko-leuart.md#std-dtcompatible-silabs-gecko-leuart) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_pg_1b.dtsi?plain=1#L23) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| Watchdog | on-chip | Silicon Labs Series 1-2 WDOG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32_pg_1b.dtsi?plain=1#L151) | [`silabs,gecko-wdog`](../../../../../build/dts/api/bindings/watchdog/silabs%2Cgecko-wdog.md#std-dtcompatible-silabs-gecko-wdog) |

### Connections and IOs

The EFM32PG1 SoC has five GPIO controllers (PORTA to PORTD and PORTF) and
all are enabled for the SLSTK3401A board.

In the following table, the column **Name** contains pin names. For example, PF4
means pin number 4 on PORTF, as used in the board’s datasheets and manuals.

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

The EFM32PG SoC is configured to use the 40 MHz external oscillator on the
board.

### Serial Port

The EFM32PG SoC has two USARTs and one Low Energy UART (LEUART).

## Programming and Debugging

The `slstk3401a` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Note

Before using the kit the first time, you should update the J-Link firmware
in Simplicity Studio.

### Flashing

The SLSTK3401A includes an [J-Link](https://www.segger.com/jlink-debug-probes.html) serial and debug adaptor built into the
board. The adaptor provides:

- A USB connection to the host computer, which exposes a mass storage device and a
  USB serial port.
- A serial flash device, which implements the USB flash disk file storage.
- A physical UART connection which is relayed over interface USB serial port.

#### Flashing an application to SLSTK3401A

The sample application [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") is used for this example.
Build the Zephyr kernel and application:

```shell
# From the root of the zephyr repository
west build -b slstk3401a samples/hello_world
```

Connect the SLSTK3401A to your host computer using the USB port and you
should see a USB connection which exposes a mass storage device(SLSTK3401A).
Copy the generated zephyr.bin to the SLSTK3401A drive.

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
Hello World! slstk3401a
```

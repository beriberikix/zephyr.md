---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/silabs/starter_kits/efm32wg_stk3800/doc/index.html
original_path: boards/silabs/starter_kits/efm32wg_stk3800/doc/index.html
---

# EFM32 Wonder Gecko (EFM32WG-STK3800)

Board Overview

[![../../../../../_images/efm32wg_stk3800.jpg](../../../../../_images/efm32wg_stk3800.jpg)
](../../../../../_images/efm32wg_stk3800.jpg)

EFM32 Wonder Gecko (EFM32WG-STK3800)

Name:
:   `efm32wg_stk3800`

Vendor:
:   Silicon Laboratories

Architecture:
:   arm

SoC:
:   efm32wg990f256

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/starter_kits/efm32wg_stk3800/doc/index.rst/../..)

## Overview

The EFM32 Wonder Gecko Starter Kit EFM32WG-STK3800 contains a MCU from the
EFM32WG family built on ARM® Cortex®-M4F processor with excellent low
power capabilities.

## Hardware

- Advanced Energy Monitoring provides real-time information about the energy
  consumption of an application or prototype design.
- 32MByte parallel NAND Flash
- 160 segment Energy Micro LCD
- 2 user buttons, 2 LEDs and a touch slider
- Ambient Light Sensor and Inductive-capacitive metal sensor
- On-board Segger J-Link USB debugger

For more information about the EFM32WG SoC and EFM32WG-STK3800 board:

- [EFM32WG Website](http://www.silabs.com/products/mcu/32-bit/efm32-wonder-gecko)
- [EFM32WG Datasheet](http://www.silabs.com/documents/public/data-sheets/EFM32WG990.pdf)
- [EFM32WG Reference Manual](http://www.silabs.com/documents/public/reference-manuals/EFM32WG-RM.pdf)
- [EFM32WG-STK3800 Website](http://www.silabs.com/products/development-tools/mcu/32-bit/efm32-wonder-gecko-starter-kit)
- [EFM32WG-STK3800 User Guide](http://www.silabs.com/documents/public/user-guides/efm32wg-stk3800-ug.pdf)
- [EFM32WG-STK3800 Schematics](http://www.silabs.com/documents/public/schematic-files/BRD2400A_A00.pdf)

### Supported Features

The `efm32wg_stk3800` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `efm32wg_stk3800/efm32wg990f256` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L17) | [`arm,cortex-m4f`](../../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| Flash controller | on-chip | Silicon Labs Gecko flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L28) | [`silabs,gecko-flash-controller`](../../../../../build/dts/api/bindings/flash_controller/silabs%2Cgecko-flash-controller.md#std-dtcompatible-silabs-gecko-flash-controller) |
| GPIO & Headers | on-chip | Silicon Labs Series 0-2 GPIO Peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L124) | [`silabs,gecko-gpio`](../../../../../build/dts/api/bindings/gpio/silabs%2Cgecko-gpio.md#std-dtcompatible-silabs-gecko-gpio) |
| on-chip | Silicon Labs Series 0-2 GPIO Port[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L134)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L152) | [`silabs,gecko-gpio-port`](../../../../../build/dts/api/bindings/gpio/silabs%2Cgecko-gpio-port.md#std-dtcompatible-silabs-gecko-gpio-port) |
| I2C | on-chip | Silicon Labs Series 0-2 I2C[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L104) | [`silabs,gecko-i2c`](../../../../../build/dts/api/bindings/i2c/silabs%2Cgecko-i2c.md#std-dtcompatible-silabs-gecko-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/starter_kits/efm32wg_stk3800/efm32wg_stk3800.dts?plain=1#L44) | [`gpio-keys`](../../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/starter_kits/efm32wg_stk3800/efm32wg_stk3800.dts?plain=1#L30) | [`gpio-leds`](../../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L36) | [`soc-nv-flash`](../../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/starter_kits/efm32wg_stk3800/efm32wg_stk3800.dts?plain=1#L97) | [`fixed-partitions`](../../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Silabs Gecko Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L189) | [`silabs,gecko-pinctrl`](../../../../../build/dts/api/bindings/pinctrl/silabs%2Cgecko-pinctrl.md#std-dtcompatible-silabs-gecko-pinctrl) |
| Serial controller | on-chip | Gecko USART[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L43) | [`silabs,gecko-usart`](../../../../../build/dts/api/bindings/serial/silabs%2Cgecko-usart.md#std-dtcompatible-silabs-gecko-usart) |
| on-chip | Gecko UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L70)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L79) | [`silabs,gecko-uart`](../../../../../build/dts/api/bindings/serial/silabs%2Cgecko-uart.md#std-dtcompatible-silabs-gecko-uart) |
| on-chip | Gecko LEUART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L88) | [`silabs,gecko-leuart`](../../../../../build/dts/api/bindings/serial/silabs%2Cgecko-leuart.md#std-dtcompatible-silabs-gecko-leuart) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/efm32wg.dtsi?plain=1#L23) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |

### Connections and IOs

The EFM32WG SoC has six gpio controllers (PORTA to PORTF), but only three are
currently enabled (PORTB, PORTE and PORTF) for the EFM32WG-STK3800 board.

In the following table, the column Name contains Pin names. For example, PE2
means Pin number 2 on PORTE, as used in the board’s datasheets and manuals.

| Name | Function | Usage |
| --- | --- | --- |
| PE2 | GPIO | LED0 |
| PE3 | GPIO | LED1 |
| PB9 | GPIO | Push Button PB0 |
| PB10 | GPIO | Push Button PB1 |
| PF7 | GPIO | Board Controller Enable EFM\_BC\_EN |
| PE0 | UART0\_TX | UART Console EFM\_BC\_TX U0\_TX #1 |
| PE1 | UART0\_RX | UART Console EFM\_BC\_RX U0\_RX #1 |

### System Clock

The EFM32WG SoC is configured to use the 48 MHz external oscillator on the
board.

### Serial Port

The EFM32WG SoC has three USARTs, two UARTs and two Low Energy UARTs (LEUART).
UART0 is connected to the board controller and is used for the console.

## Programming and Debugging

The `efm32wg_stk3800` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Note

Before using the kit the first time, you should update the J-Link firmware
in Simplicity Studio.

### Flashing

The EFM32WG-STK3800 includes an [J-Link](https://www.segger.com/jlink-debug-probes.html) serial and debug adaptor built into the
board. The adaptor provides:

- A USB connection to the host computer, which exposes a Mass Storage and a
  USB Serial Port.
- A Serial Flash device, which implements the USB flash disk file storage.
- A physical UART connection which is relayed over interface USB Serial port.

#### Flashing an application to EFM32-STK3800

The sample application [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") is used for this example.
Build the Zephyr kernel and application:

```shell
# From the root of the zephyr repository
west build -b efm32wg_stk3800 samples/hello_world
```

Connect the EFM32WG-STK3800 to your host computer using the USB port and you
should see a USB connection which exposes a Mass Storage (STK3800) and a
USB Serial Port. Copy the generated zephyr.bin in the STK3800 drive.

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you should be able to see on the corresponding Serial Port
the following message:

```shell
Hello World! efm32wg_stk3800
```

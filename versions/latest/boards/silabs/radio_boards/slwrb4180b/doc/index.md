---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/silabs/radio_boards/slwrb4180b/doc/index.html
original_path: boards/silabs/radio_boards/slwrb4180b/doc/index.html
---

# EFR32xG21 2.4 GHz 20 dBm (SLWRB4180B)

Board Overview

[![../../../../../_images/efr32mg21-slwrb4180b.webp](../../../../../_images/efr32mg21-slwrb4180b.webp)
](../../../../../_images/efr32mg21-slwrb4180b.webp)

EFR32xG21 2.4 GHz 20 dBm (SLWRB4180B)

Name:
:   `slwrb4180b`

Vendor:
:   Silicon Laboratories

Architecture:
:   arm

SoC:
:   efr32mg21a020f1024im32

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/radio_boards/slwrb4180b/doc/index.rst/../..)

## Overview

The EFR32MG21 Mighty Gecko Radio Board is one of the two
radio boards delivered with [EFR32-SLWSTK6006A Website](https://www.silabs.com/products/development-tools/wireless/efr32xg21-wireless-starter-kit). It features a
Wireless System-On-Chip (SoC) from the EFR32MG21 family, built on an
ARM Cortex®-M33F processor, offering exceptional low-power performance.

The SLWRB4180B radio board is designed to connect seamlessly with
the Wireless Starter Kit Mainboards BRD4001A and BRD4002A

## Hardware

- EFR32MG21A020F1024IM32 Mighty Gecko SoC
- CPU core: ARM Cortex®-M33 with FPU
- Flash memory: 1024 kB
- RAM: 96 kB
- Transmit power: up to +20 dBm
- Operation frequency: 2.4 GHz
- Crystals for LFXO (32.768 kHz) and HFXO (38.4 MHz).

For more information about the EFR32MG21 SoC and BRD4180B board, refer to these
documents:

- [EFR32MG21 Website](https://www.silabs.com/products/wireless/mesh-networking/efr32mg21-series-2-socs)
- [EFR32MG21 Datasheet](https://www.silabs.com/documents/public/data-sheets/efr32mg21-datasheet.pdf)
- [EFR32xG21 Reference Manual](https://www.silabs.com/documents/public/reference-manuals/efr32xg21-rm.pdf)
- [EFR32-SLWSTK6006A Website](https://www.silabs.com/products/development-tools/wireless/efr32xg21-wireless-starter-kit)
- [BRD4180B User Guide](https://www.silabs.com/documents/public/user-guides/ug427-brd4180b-user-guide.pdf)

### Supported Features

The `slwrb4180b` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `slwrb4180b/efr32mg21a020f1024im32` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L101) | [`arm,cortex-m33f`](../../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| Clock control | on-chip | Silicon Labs Series 2 CMU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L126) | [`silabs,series-clock`](../../../../../build/dts/api/bindings/clock/silabs%2Cseries-clock.md#std-dtcompatible-silabs-series-clock) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L135) | [`fixed-clock`](../../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Silicon Labs Series 2 HFXO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L142) | [`silabs,hfxo`](../../../../../build/dts/api/bindings/clock/silabs%2Chfxo.md#std-dtcompatible-silabs-hfxo) |
| on-chip | Silicon Labs Series 2 LFXO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L153) | [`silabs,series2-lfxo`](../../../../../build/dts/api/bindings/clock/silabs%2Cseries2-lfxo.md#std-dtcompatible-silabs-series2-lfxo) |
| on-chip | Silicon Labs Series 2 HFRCODPLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L164) | [`silabs,series2-hfrcodpll`](../../../../../build/dts/api/bindings/clock/silabs%2Cseries2-hfrcodpll.md#std-dtcompatible-silabs-series2-hfrcodpll) |
| on-chip | Silicon Labs Series 2 HFRCOEM23[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L171) | [`silabs,series2-hfrcoem23`](../../../../../build/dts/api/bindings/clock/silabs%2Cseries2-hfrcoem23.md#std-dtcompatible-silabs-series2-hfrcoem23) |
| on-chip | Silicon Labs Series 2 LFRCO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L178) | [`silabs,series2-lfrco`](../../../../../build/dts/api/bindings/clock/silabs%2Cseries2-lfrco.md#std-dtcompatible-silabs-series2-lfrco) |
| on-chip | Generic fixed factor clock provider[13 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L22) | [`fixed-factor-clock`](../../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| Comparator | on-chip | Silicon Labs Series 2 ACMP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L441) | [`silabs,acmp`](../../../../../build/dts/api/bindings/comparator/silabs%2Cacmp.md#std-dtcompatible-silabs-acmp) |
| Cryptographic accelerator | on-chip | Silicon Labs Series 2 SE Mailbox[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L392) | [`silabs,gecko-semailbox`](../../../../../build/dts/api/bindings/crypto/silabs%2Cgecko-semailbox.md#std-dtcompatible-silabs-gecko-semailbox) |
| Debug | on-chip | Silicon Labs Packet Trace Interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/efr32xg21.dtsi?plain=1#L23) | [`silabs,pti`](../../../../../build/dts/api/bindings/debug/silabs%2Cpti.md#std-dtcompatible-silabs-pti) |
| on-chip | ARMv8 instrumentation trace macrocell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L113) | [`arm,armv8m-itm`](../../../../../build/dts/api/bindings/debug/arm%2Carmv8m-itm.md#std-dtcompatible-arm-armv8m-itm) |
| DMA | on-chip | Silicon Labs Series 2 LDMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L400) | [`silabs,ldma`](../../../../../build/dts/api/bindings/dma/silabs%2Cldma.md#std-dtcompatible-silabs-ldma) |
| Flash controller | on-chip | Silicon Labs Series 2 MSC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L199) | [`silabs,series2-flash-controller`](../../../../../build/dts/api/bindings/flash_controller/silabs%2Cseries2-flash-controller.md#std-dtcompatible-silabs-series2-flash-controller) |
| GPIO & Headers | on-chip | Silicon Labs Series 0-2 GPIO Peripheral[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L338) | [`silabs,gecko-gpio`](../../../../../build/dts/api/bindings/gpio/silabs%2Cgecko-gpio.md#std-dtcompatible-silabs-gecko-gpio) |
| on-chip | Silicon Labs Series 0-2 GPIO Port[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L349) | [`silabs,gecko-gpio-port`](../../../../../build/dts/api/bindings/gpio/silabs%2Cgecko-gpio-port.md#std-dtcompatible-silabs-gecko-gpio-port) |
| I2C | on-chip | Silicon Labs Series 0-2 I2C[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L305) | [`silabs,gecko-i2c`](../../../../../build/dts/api/bindings/i2c/silabs%2Cgecko-i2c.md#std-dtcompatible-silabs-gecko-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/slwrb4180b/slwrb4180b.dts?plain=1#L48) | [`gpio-keys`](../../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/slwrb4180b/slwrb4180b.dts?plain=1#L34) | [`gpio-leds`](../../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L108) | [`arm,armv8m-mpu`](../../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L207) | [`soc-nv-flash`](../../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/slwrb4180b/slwrb4180b.dts?plain=1#L158) | [`fixed-partitions`](../../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Networking | on-chip | Silicon Labs Series 2 Radio Interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/efr32xg21.dtsi?plain=1#L11) | [`silabs,series2-radio`](../../../../../build/dts/api/bindings/net/wireless/silabs%2Cseries2-radio.md#std-dtcompatible-silabs-series2-radio) |
| Pin control | on-chip | Silicon Labs Series 2 DBUS Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L386) | [`silabs,dbus-pinctrl`](../../../../../build/dts/api/bindings/pinctrl/silabs%2Cdbus-pinctrl.md#std-dtcompatible-silabs-dbus-pinctrl) |
| PWM | on-chip | Silicon Labs TIMER PWM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L223) | [`silabs,timer-pwm`](../../../../../build/dts/api/bindings/pwm/silabs%2Ctimer-pwm.md#std-dtcompatible-silabs-timer-pwm) |
| on-chip | Silicon Labs LETIMER PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L434) | [`silabs,letimer-pwm`](../../../../../build/dts/api/bindings/pwm/silabs%2Cletimer-pwm.md#std-dtcompatible-silabs-letimer-pwm) |
| RTC | on-chip | Silicon Labs Series 2 Sleeptimer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L327) | [`silabs,gecko-stimer`](../../../../../build/dts/api/bindings/rtc/silabs%2Cgecko-stimer.md#std-dtcompatible-silabs-gecko-stimer) |
| Serial controller | on-chip | Silicon Labs Series 2 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L278)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L287) | [`silabs,usart-uart`](../../../../../build/dts/api/bindings/serial/silabs%2Cusart-uart.md#std-dtcompatible-silabs-usart-uart) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L120) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | Silicon Labs TIMER[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L214) | [`silabs,series2-timer`](../../../../../build/dts/api/bindings/timer/silabs%2Cseries2-timer.md#std-dtcompatible-silabs-series2-timer) |
| on-chip | Silicon Labs LETIMER[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L427) | [`silabs,series2-letimer`](../../../../../build/dts/api/bindings/timer/silabs%2Cseries2-letimer.md#std-dtcompatible-silabs-series2-letimer) |
| Watchdog | on-chip | Silicon Labs Series 1-2 WDOG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L409)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/xg21/xg21.dtsi?plain=1#L418) | [`silabs,gecko-wdog`](../../../../../build/dts/api/bindings/watchdog/silabs%2Cgecko-wdog.md#std-dtcompatible-silabs-gecko-wdog) |

### Connections and IOs

In the following table, the column **Name** contains Pin names. For example, PD2
means Pin number 2 on PORTD, as used in the board’s datasheets and manuals.

| Name | Function | Usage |
| --- | --- | --- |
| PD2 | GPIO | LED0 |
| PD3 | GPIO | LED1 |
| PB0 | GPIO | Push Button PB0 |
| PB1 | GPIO | Push Button PB1 |
| PD4 | GPIO | Board Controller Enable EFM\_BC\_EN |
| PA5 | USART1\_TX | UART Console EFM\_BC\_TX US1\_TX |
| PA6 | USART1\_RX | UART Console EFM\_BC\_RX US1\_RX |

The default configuration can be found in
[boards/silabs/radio\_boards/slwrb4180b/slwrb4180b\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/slwrb4180b/slwrb4180b_defconfig)

## Programming and Debugging

The `slwrb4180b` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |
| **[openocd](../../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **silabs\_commander** | ✅ |  |  |  |  |

### Flashing

Connect the BRD4001A or BRD4002A mainboard, with the BRD4180B radio module mounted,
to your host computer via the USB port.

Here is an example for the [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b slwrb4180b samples/hello_world
west flash
```

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you should see the following message in the terminal:

```shell
Hello World! slwrb4180b
```

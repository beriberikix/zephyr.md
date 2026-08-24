---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/olimex/stm32_h103/doc/index.html
original_path: boards/olimex/stm32_h103/doc/index.html
---

# OLIMEX-STM32-H103

Board Overview

[![../../../../_images/olimex_stm32_h103_top.jpg](https://docs.zephyrproject.org/4.2.0/_images/olimex_stm32_h103_top.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/olimex_stm32_h103_top.jpg)

OLIMEX-STM32-H103

Name:
:   `olimex_stm32_h103`

Vendor:
:   OLIMEX Ltd.

Architecture:
:   arm

SoC:
:   stm32f103xb

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/olimex/stm32_h103/doc/index.rst/../..)

## Overview

The OLIMEX-STM32-H103 is a simple development board based on the
STMicroelectronics STM32F103RBT6 ARM Cortex-M3 CPU, with all the MCU pins
populated and accessible through two male 26-pin connectors.

## Hardware

Information about the board can be found at the
[OLIMEX-STM32-H103 website](https://www.olimex.com/Products/ARM/ST/STM32-H103/) and [OLIMEX-STM32-H103 user manual](https://www.olimex.com/Products/ARM/ST/STM32-H103/resources/STM32-H103.pdf).
The [OLIMEX-STM32-H103 schematic](https://www.olimex.com/Products/ARM/ST/STM32-H405/resources/STM32-H405_sch.pdf) is also available.

The [ST STM32F103RB Datasheet](https://www.st.com/resource/en/datasheet/stm32f103rb.pdf) contains the processor’s
information and the datasheet.

### Supported Features

The `olimex_stm32_h103` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `olimex_stm32_h103/stm32f103xb` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M3 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L31) | [`arm,cortex-m3`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m3.md#std-dtcompatible-arm-cortex-m3) |
| ADC | on-chip | STM32F1 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L363) | [`st,stm32f1-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32f1-adc.md#std-dtcompatible-st-stm32f1-adc) |
| CAN | on-chip | STM32 CAN controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f103X8.dtsi?plain=1#L51) | [`st,stm32-bxcan`](../../../../build/dts/api/bindings/can/st%2Cstm32-bxcan.md#std-dtcompatible-st-stm32-bxcan) |
| Clock control | on-chip | STM32F1/F3/7x RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L123) | [`st,stm32f1-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32f1-rcc.md#std-dtcompatible-st-stm32f1-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L62) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L68) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32F1 Main PLL for low-, medium-, high- and XL-density devices[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L89) | [`st,stm32f1-pll-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32f1-pll-clock.md#std-dtcompatible-st-stm32f1-pll-clock) |
| on-chip | STM32F1 Microcontroller Clock Output (MCO)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L97) | [`st,stm32f1-clock-mco`](../../../../build/dts/api/bindings/clock/st%2Cstm32f1-clock-mco.md#std-dtcompatible-st-stm32f1-clock-mco) |
| Counter | on-chip | STM32 counters[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L304) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st%2Cstm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DMA | on-chip | STM32 DMA controller (V2bis) for the stm32F0, stm32F1 and stm32L1 soc families[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L376) | [`st,stm32-dma-v2bis`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dma-v2bis.md#std-dtcompatible-st-stm32-dma-v2bis) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L105) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO Controller[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L155) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| I2C | on-chip | STM32 I2C V1 controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L223) | [`st,stm32-i2c-v1`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v1.md#std-dtcompatible-st-stm32-i2c-v1) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/olimex/stm32_h103/olimex_stm32_h103.dts?plain=1#L30) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L134) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/olimex/stm32_h103/olimex_stm32_h103.dts?plain=1#L22) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L114) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st%2Cstm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f103X8.dtsi?plain=1#L61) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32F1 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L149) | [`st,stm32f1-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32f1-pinctrl.md#std-dtcompatible-st-stm32f1-pinctrl) |
| Power management | on-chip | STM32 power controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L386) | [`st,stm32-pwr`](../../../../build/dts/api/bindings/power/st%2Cstm32-pwr.md#std-dtcompatible-st-stm32-pwr) |
| PWM | on-chip | STM32 PWM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L281) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L128) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L354) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st%2Cstm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 Internal Temperature Sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L402) | [`st,stm32-temp`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-temp.md#std-dtcompatible-st-stm32-temp) |
| Serial controller | on-chip | STM32 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L205)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L196) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| SMbus | on-chip | STM32 SMBus controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L411) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st%2Cstm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L247) | [`st,stm32-spi`](../../../../build/dts/api/bindings/spi/st%2Cstm32-spi.md#std-dtcompatible-st-stm32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L57) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 timers[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L271) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers) |
| USB | on-chip | STM32 USB controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f103X8.dtsi?plain=1#L38) | [`st,stm32-usb`](../../../../build/dts/api/bindings/usb/st%2Cstm32-usb.md#std-dtcompatible-st-stm32-usb) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L257) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L263) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Connections and IOs

#### System Clock

The on-board 8 MHz crystal is used to produce a 72 MHz system clock with PLL.

#### Zephyr Console

UART2 is used as Zephyr’s console. Default settings are 115200 8N1.

#### On-Board LEDs

The board has one on-board green LED that is connected to PC12, which
is active low.

There is also a red power LED neither connected nor controlled by the MCU.

#### On-Board Button

The board has one user button connected to PA0.

#### USB

USB is not enabled by default.

PC4 can be configured as a GPIO input to detect power on the USB port. It is
possible to disconnect it by desoldering the appropriate pad in the PCB.

PC11 can be used to disconnect the pull-up resistor on the USB-DP line by
setting it high.

#### External Connectors

JTAG/SWD debug

| PIN # | Signal Name | PIN # | Signal Name |
| --- | --- | --- | --- |
| 1 | TVCC +3.3V | 2 | TVCC 3.3V |
| 3 | PB4 / TRST | 4 | GND |
| 5 | PA15 / TDI | 6 | GND |
| 7 | PA13 / TMS / SWDIO | 8 | GND |
| 9 | PA14 / TCK / SWCLK | 10 | GND |
| 11 | NC | 12 | GND |
| 13 | PB3 / TDO | 14 | GND |
| 15 | RST | 16 | GND |
| 17 | NC | 18 | GND |
| 19 | NC | 20 | GND |

EXTENSION 1

| PIN # | Name / STM32F103 Port | PIN # | Name / STM32F103 Port |
| --- | --- | --- | --- |
| 1 | PA11 / **USB\_DM** | 2 | PA8 |
| 3 | PA12 / **USB\_DP** | 4 | PA9 |
| 5 | +3.3V | 6 | GND |
| 7 | PA10 | 8 | PC10 |
| 9 | PC11 / **USB\_DISC** | 10 | PC12 / **LED** |
| 11 | PD2 | 12 | PB5 |
| 13 | PB6 | 14 | PA6 |
| 15 | PB7 | 16 | PB8 |
| 17 | PB9 | 18 | PA5 |
| 19 | PC0 | 20 | PC1 |
| 21 | PB0 | 22 | PA7 |
| 23 | VBAT | 24 | PC13 |
| 25 | RST | 26 | PB1 |

EXTENSION 2

| PIN # | Name / STM32F103 Port | PIN # | Name / STM32F103 Port |
| --- | --- | --- | --- |
| 1 | VDDA | 2 | PC2 |
| 3 | GNDA | 4 | PA0 / **BUTTON** |
| 5 | +3.3V | 6 | GND |
| 7 | PA2 / **USART2\_TX** | 8 | PA1 |
| 9 | PC3 | 10 | PA3 / **USART2\_RX** |
| 11 | PA4 | 12 | PC4 / **USB\_POWER** |
| 13 | PC5 | 14 | PB10 |
| 15 | P11 | 16 | PB13 |
| 17 | PB12 | 18 | PB14 |
| 19 | PB15 | 20 | PC6 |
| 21 | PC7 | 22 | PC8 |
| 23 | +5V USB | 24 | PC9 |
| 25 | GND | 26 | VIN |

## Programming and Debugging

The `olimex_stm32_h103` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[blackmagicprobe](../../../../develop/flash_debug/host-tools.md#runner-blackmagicprobe)** | ✅ | ✅ | ✅ |  |  |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

This board does not include any embedded debug tool interface, instead you
will have to use an external probe connected to the available 20-pin JTAG
connector to program and debug the board. Both JTAG and SWD are supported.

By default when using `west debug` ST-Link will be used with OpenOCD’s
SWD transport, but it is also possible to use JTAG with the Olimex ARM-USB-OCD-H
probe, for instance. For the latter, you should replace the file `openocd.cfg`
by `openocd_olimex_jtag.cfg`, located in the board’s support directory.

The `blackmagicprobe` can also be used to program the device.

### Flashing

Here is an example for the [Button](../../../../samples/basic/button/README.md#button "Handle GPIO inputs with interrupts.") application.

```shell
# From the root of the zephyr repository
west build -b olimex_stm32_h103 samples/basic/button
west flash
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b olimex_stm32_h103 samples/hello_world
west debug
```

## References

- [OLIMEX-STM32-H103 website](https://www.olimex.com/Products/ARM/ST/STM32-H103/)
- [OLIMEX-STM32-H103 user manual](https://www.olimex.com/Products/ARM/ST/STM32-H103/resources/STM32-H103.pdf)
- [OLIMEX-STM32-H103 schematic](https://www.olimex.com/Products/ARM/ST/STM32-H405/resources/STM32-H405_sch.pdf)

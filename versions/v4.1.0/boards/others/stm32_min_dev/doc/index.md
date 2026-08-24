---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/others/stm32_min_dev/doc/index.html
original_path: boards/others/stm32_min_dev/doc/index.html
---

# STM32 Minimum Development Board

Board Overview

[![../../../../_images/stm32_min_dev.jpg](https://docs.zephyrproject.org/4.1.0/_images/stm32_min_dev.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/stm32_min_dev.jpg)

STM32 Minimum Development Board

Name:
:   `stm32_min_dev`

Vendor:
:   Other/Unknown

Architecture:

SoC:
:   stm32f103xb

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/others/stm32_min_dev/doc/index.rst/../..)

## Overview

The STM32 Minimum Development Board, is a popular and inexpensive
breadboard-friendly breakout board for the [STM32F103x8](https://www.st.com/resource/en/datasheet/stm32f103c8.pdf) CPU. There
are two variants of the board:

- Blue Pill Board
- Black Pill Board

Zephyr applications can use the [stm32\_min\_dev@blue](mailto:stm32_min_dev%40blue) or [stm32\_min\_dev@black](mailto:stm32_min_dev%40black) board
configuration to use these boards.

As the name suggests, these boards have the bare minimum components required to
power on the CPU. For practical use, you’ll need to add additional components
and circuits using a breadboard, for example.

### Pin Mapping

This port is a starting point for your own customizations and not a complete
port for a specific board. Most of the GPIOs on the STM32 SoC has been exposed
in the external header with silk screen labels that match the SoC’s pin names.

Each board vendor has their own variations in pin mapping on their boards’
external connectors and placement of components. Many vendors use port PC13/PB12
for connecting an LED, so only this device is supported by our Zephyr port.
Additional device support is left for the user to implement.

More information on hooking up peripherals and lengthy how to articles can be
found at [EmbedJournal](https://embedjournal.com/tag/stm32-min-dev/).

The pinout diagram of STM32 Minimum Development Blue Pill board can be seen
below. The Black Pill’s one is similar:

![Pinout for STM32 Minimum Development Blue Pill Board](https://docs.zephyrproject.org/4.1.0/_images/stm32_min_dev_pinout_blue.jpg)

Pinout for STM32 Minimum Development Blue Pill Board

### STLinkV2 connection:

The board can be flashed by using STLinkV2 with the following connections.

| Pin | STLINKv2 |
| --- | --- |
| G | GND |
| CLK | Clock |
| IO | SW IO |
| V3 | VCC |

### Boot Configuration

The boot configuration for this board is configured through jumpers on B0 (Boot 0)
and B1 (Boot 1). The pins B0 and B1 are present in between logic 0 and 1 lines. The
silk screen on the PCB reads BX- or BX+ to indicate 0 and 1 logic lines for B0 and B1
respectively.

| Boot 1 | Boot 0 | Boot Mode | Aliasing |
| --- | --- | --- | --- |
| X | 0 | Main Flash Memory | Main flash memory is selected as boot space |
| 0 | 1 | System Memory | System memory is selected as boot space |
| 1 | 1 | Embedded SRAM | Embedded SRAM is selected as boot space |

### Supported Features

The `stm32_min_dev` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `stm32_min_dev/stm32f103xb@black` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M3 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L29) | [`arm,cortex-m3`](../../../../build/dts/api/bindings/cpu/arm,cortex-m3.md#std-dtcompatible-arm-cortex-m3) |
| ADC | on-chip | STM32F1 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L342) | [`st,stm32f1-adc`](../../../../build/dts/api/bindings/adc/st,stm32f1-adc.md#std-dtcompatible-st-stm32f1-adc) |
| CAN | on-chip | STM32 CAN controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f103X8.dtsi?plain=1#L50) | [`st,stm32-bxcan`](../../../../build/dts/api/bindings/can/st,stm32-bxcan.md#std-dtcompatible-st-stm32-bxcan) |
| Clock control | on-chip | STM32F1/F3/7x RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L102) | [`st,stm32f1-rcc`](../../../../build/dts/api/bindings/clock/st,stm32f1-rcc.md#std-dtcompatible-st-stm32f1-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L41) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L47) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32F1 Main PLL for low-, medium-, high- and XL-density devices[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L68) | [`st,stm32f1-pll-clock`](../../../../build/dts/api/bindings/clock/st,stm32f1-pll-clock.md#std-dtcompatible-st-stm32f1-pll-clock) |
| on-chip | STM32F1 Microcontroller Clock Output (MCO)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L76) | [`st,stm32f1-clock-mco`](../../../../build/dts/api/bindings/clock/st,stm32f1-clock-mco.md#std-dtcompatible-st-stm32f1-clock-mco) |
| Counter | on-chip | STM32 counters[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L283) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st,stm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DMA | on-chip | STM32 DMA controller (V2bis) for the stm32F0, stm32F1 and stm32L1 soc families[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L355) | [`st,stm32-dma-v2bis`](../../../../build/dts/api/bindings/dma/st,stm32-dma-v2bis.md#std-dtcompatible-st-stm32-dma-v2bis) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L84) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st,stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO controller[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L134) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st,stm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| I2C | on-chip | STM32 I2C V1 controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L202) | [`st,stm32-i2c-v1`](../../../../build/dts/api/bindings/i2c/st,stm32-i2c-v1.md#std-dtcompatible-st-stm32-i2c-v1) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L113) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st,stm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/stm32_min_dev/stm32_min_dev.dts?plain=1#L23) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L93) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st,stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f103X8.dtsi?plain=1#L60) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32F1 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L128) | [`st,stm32f1-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st,stm32f1-pinctrl.md#std-dtcompatible-st-stm32f1-pinctrl) |
| PWM | on-chip | STM32 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L260)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L277) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st,stm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L107) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st,stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L333) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st,stm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 Internal Temperature Sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L365) | [`st,stm32-temp`](../../../../build/dts/api/bindings/sensor/st,stm32-temp.md#std-dtcompatible-st-stm32-temp) |
| Serial controller | on-chip | STM32 USART[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L175) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st,stm32-usart.md#std-dtcompatible-st-stm32-usart) |
| SMbus | on-chip | STM32 SMBus controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L374) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st,stm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L226) | [`st,stm32-spi`](../../../../build/dts/api/bindings/spi/st,stm32-spi.md#std-dtcompatible-st-stm32-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L36) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 timers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L250)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L267) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st,stm32-timers.md#std-dtcompatible-st-stm32-timers) |
| USB | on-chip | STM32 USB controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f103X8.dtsi?plain=1#L38) | [`st,stm32-usb`](../../../../build/dts/api/bindings/usb/st,stm32-usb.md#std-dtcompatible-st-stm32-usb) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L236) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L242) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

#### `stm32_min_dev/stm32f103xb@blue` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M3 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L29) | [`arm,cortex-m3`](../../../../build/dts/api/bindings/cpu/arm,cortex-m3.md#std-dtcompatible-arm-cortex-m3) |
| ADC | on-chip | STM32F1 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L342) | [`st,stm32f1-adc`](../../../../build/dts/api/bindings/adc/st,stm32f1-adc.md#std-dtcompatible-st-stm32f1-adc) |
| CAN | on-chip | STM32 CAN controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f103X8.dtsi?plain=1#L50) | [`st,stm32-bxcan`](../../../../build/dts/api/bindings/can/st,stm32-bxcan.md#std-dtcompatible-st-stm32-bxcan) |
| Clock control | on-chip | STM32F1/F3/7x RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L102) | [`st,stm32f1-rcc`](../../../../build/dts/api/bindings/clock/st,stm32f1-rcc.md#std-dtcompatible-st-stm32f1-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L41) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L47) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32F1 Main PLL for low-, medium-, high- and XL-density devices[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L68) | [`st,stm32f1-pll-clock`](../../../../build/dts/api/bindings/clock/st,stm32f1-pll-clock.md#std-dtcompatible-st-stm32f1-pll-clock) |
| on-chip | STM32F1 Microcontroller Clock Output (MCO)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L76) | [`st,stm32f1-clock-mco`](../../../../build/dts/api/bindings/clock/st,stm32f1-clock-mco.md#std-dtcompatible-st-stm32f1-clock-mco) |
| Counter | on-chip | STM32 counters[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L283) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st,stm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DMA | on-chip | STM32 DMA controller (V2bis) for the stm32F0, stm32F1 and stm32L1 soc families[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L355) | [`st,stm32-dma-v2bis`](../../../../build/dts/api/bindings/dma/st,stm32-dma-v2bis.md#std-dtcompatible-st-stm32-dma-v2bis) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L84) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st,stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO controller[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L134) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st,stm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| I2C | on-chip | STM32 I2C V1 controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L202) | [`st,stm32-i2c-v1`](../../../../build/dts/api/bindings/i2c/st,stm32-i2c-v1.md#std-dtcompatible-st-stm32-i2c-v1) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L113) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st,stm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/stm32_min_dev/stm32_min_dev.dts?plain=1#L23) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L93) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st,stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f103X8.dtsi?plain=1#L60) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32F1 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L128) | [`st,stm32f1-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st,stm32f1-pinctrl.md#std-dtcompatible-st-stm32f1-pinctrl) |
| PWM | on-chip | STM32 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L260)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L277) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st,stm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L107) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st,stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L333) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st,stm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 Internal Temperature Sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L365) | [`st,stm32-temp`](../../../../build/dts/api/bindings/sensor/st,stm32-temp.md#std-dtcompatible-st-stm32-temp) |
| Serial controller | on-chip | STM32 USART[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L175) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st,stm32-usart.md#std-dtcompatible-st-stm32-usart) |
| SMbus | on-chip | STM32 SMBus controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L374) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st,stm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L226) | [`st,stm32-spi`](../../../../build/dts/api/bindings/spi/st,stm32-spi.md#std-dtcompatible-st-stm32-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L36) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 timers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L250)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L267) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st,stm32-timers.md#std-dtcompatible-st-stm32-timers) |
| USB | on-chip | STM32 USB controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f103X8.dtsi?plain=1#L38) | [`st,stm32-usb`](../../../../build/dts/api/bindings/usb/st,stm32-usb.md#std-dtcompatible-st-stm32-usb) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L236) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L242) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Connections and IOs

#### Default Zephyr Peripheral Mapping:

- UART\_1 TX/RX: PA9/PA10
- UART\_2 TX/RX: PA2/PA3
- UART\_3 TX/RX: PB10/PB11
- I2C\_1 SCL/SDA : PB6/PB7
- I2C\_2 SCL/SDA : PB10/PB11
- PWM\_1\_CH1: PA8
- SPI\_1 NSS\_OE/SCK/MISO/MOSI: PA4/PA5/PA6/PA7
- SPI\_2 NSS\_OE/SCK/MISO/MOSI: PB12/PB13/PB14/PB15
- USB\_DC DM/DP: PA11/PA12
- ADC\_1: PA0

#### System Clock

The on-board 8Mhz crystal is used to produce a 72Mhz system clock with PLL.

#### Serial Port

STM32 Minimum Development Board has 3 U(S)ARTs. The Zephyr console output is
assigned to UART\_1. Default settings are 115200 8N1.

#### On-Board LEDs

The board has one on-board LED that is connected to PB12/PC13 on the black/blue
variants respectively.

## Programming and Debugging

Applications for the `stm32_min_dev@(blue|black)` board configuration can be
built and flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b stm32_min_dev samples/basic/blinky
west flash
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b stm32_min_dev samples/hello_world
west debug
```

---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/others/stm32f030_demo/doc/index.html
original_path: boards/others/stm32f030_demo/doc/index.html
---

# STM32F030 DEMO BOARD

Board Overview

[![../../../../_images/stm32f030_demo.jpg](https://docs.zephyrproject.org/4.2.0/_images/stm32f030_demo.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/stm32f030_demo.jpg)

STM32F030 DEMO BOARD

Name:
:   `stm32f030_demo`

Vendor:
:   Other/Unknown

Architecture:
:   arm

SoC:
:   stm32f030x6

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/others/stm32f030_demo/doc/index.rst/../..)

This board has the bare minimum components required to power on
the STM32F030F4P6 MCU. Most of the GPIOs on the STM32 SoC have
been exposed in the external headers with silk screen labels
that match the SoC’s pin names.

For practical use, you’ll need to add additional components
and circuits using a breadboard, for example.

More information about the board can be found at the [stm32-base.org website](https://stm32-base.org/boards/STM32F030F4P6-STM32F030-DEMO-BOARD-V1.1) [[1]](#id2).

More information about STM32F030F4P6 can be found here:

- [STM32F030 reference manual](https://www.st.com/resource/en/reference_manual/dm00091010.pdf) [[2]](#id4)
- [STM32F030 data sheet](https://www.st.com/resource/en/datasheet/stm32f030f4.pdf) [[3]](#id6)

## Hardware

- STM32F030F4P6 ARM Cortex-M0 processor, frequency up to 48 MHz
- 16 KiB of flash memory and 4 KiB of RAM
- 8 MHz quartz crystal
- 1 user LED
- One reset button
- 2-way jumper (BOOT0)
- Serial (1x4 male dupont (2.54mm))
- SWD (1x4 male dupont (2.54mm))
- USB port (power only)

### Supported Features

The `stm32f030_demo` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `stm32f030_demo/stm32f030x6` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f0/stm32f0.dtsi?plain=1#L30) | [`arm,cortex-m0`](../../../../build/dts/api/bindings/cpu/arm,cortex-m0.md#std-dtcompatible-arm-cortex-m0) |
| ADC | on-chip | STM32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f0/stm32f0.dtsi?plain=1#L338) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st,stm32-adc.md#std-dtcompatible-st-stm32-adc) |
| Clock control | on-chip | STM32F0/G0 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f0/stm32f0.dtsi?plain=1#L103) | [`st,stm32f0-rcc`](../../../../build/dts/api/bindings/clock/st,stm32f0-rcc.md#std-dtcompatible-st-stm32f0-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f0/stm32f0.dtsi?plain=1#L42) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f0/stm32f0.dtsi?plain=1#L48) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f0/stm32f0.dtsi?plain=1#L62) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32F0/F3 Main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f0/stm32f0.dtsi?plain=1#L77) | [`st,stm32f0-pll-clock`](../../../../build/dts/api/bindings/clock/st,stm32f0-pll-clock.md#std-dtcompatible-st-stm32f0-pll-clock) |
| Counter | on-chip | STM32 counters[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f0/stm32f0.dtsi?plain=1#L266) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st,stm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DMA | on-chip | STM32 DMA controller (V2bis) for the stm32F0, stm32F1 and stm32L1 soc families[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f0/stm32f0.dtsi?plain=1#L355) | [`st,stm32-dma-v2bis`](../../../../build/dts/api/bindings/dma/st,stm32-dma-v2bis.md#std-dtcompatible-st-stm32-dma-v2bis) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f0/stm32f0.dtsi?plain=1#L85) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st,stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO Controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f0/stm32f0.dtsi?plain=1#L132)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f0/stm32f0.dtsi?plain=1#L148) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st,stm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| I2C | on-chip | STM32 I2C V2 controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f0/stm32f0.dtsi?plain=1#L182) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st,stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f0/stm32f0.dtsi?plain=1#L114) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st,stm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/others/stm32f030_demo/stm32f030_demo.dts?plain=1#L22) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f0/stm32f0.dtsi?plain=1#L94) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st,stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f0/stm32f0.dtsi?plain=1#L126) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st,stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f0/stm32f0.dtsi?plain=1#L243) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st,stm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f0/stm32f0.dtsi?plain=1#L108) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st,stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f0/stm32f0.dtsi?plain=1#L208) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st,stm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f0/stm32f0.dtsi?plain=1#L365) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st,stm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 TEMP for production calibrated sensors with a single calibration temperature[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f0/stm32f030.dtsi?plain=1#L14) | [`st,stm32c0-temp-cal`](../../../../build/dts/api/bindings/sensor/st,stm32c0-temp-cal.md#std-dtcompatible-st-stm32c0-temp-cal) |
| Serial controller | on-chip | STM32 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f0/stm32f0.dtsi?plain=1#L173) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st,stm32-usart.md#std-dtcompatible-st-stm32-usart) |
| SMbus | on-chip | STM32 SMBus controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f0/stm32f0.dtsi?plain=1#L373) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st,stm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller with embedded Rx and Tx FIFOs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f0/stm32f0.dtsi?plain=1#L198) | [`st,stm32-spi-fifo`](../../../../build/dts/api/bindings/spi/st,stm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f0/stm32f0.dtsi?plain=1#L37) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv6-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21) | [`arm,armv6m-systick`](../../../../build/dts/api/bindings/timer/arm,armv6m-systick.md#std-dtcompatible-arm-armv6m-systick) |
| on-chip | STM32 timers[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f0/stm32f0.dtsi?plain=1#L233) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st,stm32-timers.md#std-dtcompatible-st-stm32-timers) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f0/stm32f0.dtsi?plain=1#L219) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f0/stm32f0.dtsi?plain=1#L225) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Pin Mapping

#### Default Zephyr Peripheral Mapping:

- UART\_1 TX/RX : PA9/PA10
- LED : PA4

## Programming and Debugging

The `stm32f030_demo` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |
| **stm32flash** | ✅ |  |  |  |  |

Applications for the `stm32f030_demo` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board can be flashed by using ST-LINKV2 in-circuit debugger and programmer.
This interface is supported by the openocd version included in the Zephyr SDK.

#### Flashing an application to STM32F030 DEMO BOARD

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b stm32f030_demo samples/basic/blinky
west flash
```

You will see the LED blinking every second.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b stm32f030_demo samples/basic/blinky
west debug
```

## References

[[1](#id3)]

[https://stm32-base.org/boards/STM32F030F4P6-STM32F030-DEMO-BOARD-V1.1](https://stm32-base.org/boards/STM32F030F4P6-STM32F030-DEMO-BOARD-V1.1)

[[2](#id5)]

[https://www.st.com/resource/en/reference\_manual/dm00091010.pdf](https://www.st.com/resource/en/reference_manual/dm00091010.pdf)

[[3](#id7)]

[https://www.st.com/resource/en/datasheet/stm32f030f4.pdf](https://www.st.com/resource/en/datasheet/stm32f030f4.pdf)

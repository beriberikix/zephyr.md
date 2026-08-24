---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/stm32c0116_dk/doc/index.html
original_path: boards/st/stm32c0116_dk/doc/index.html
---

# STM32C0116-DK Discovery Kit

Board Overview

[![../../../../_images/stm32c0116_dk.jpg](https://docs.zephyrproject.org/4.1.0/_images/stm32c0116_dk.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/stm32c0116_dk.jpg)

STM32C0116-DK Discovery Kit

Name:
:   `stm32c0116_dk`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32c011xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm32c0116_dk/doc/index.rst/../..)

## Overview

The STM32C0116-DK Discovery kit helps to discover features of the STM32C0 Series
microcontroller in a UFQFPN20 package. This Discovery kit features one UFQFPN20
to DIL20 module designed with the STM32C011F6 microcontroller and allows the user to develop
and share applications. It includes an on-board ST-LINK/V2-1 to debug and program the embedded
STM32 microcontroller. Important board features include:

More information about the board can be found at the [STM32C0116-DK website](https://www.st.com/en/evaluation-tools/stm32c0116-dk.html).

## Hardware

The STM32C0116-DK Discovery kit provides the following hardware components:

- STM32C011F6 microcontroller with 32 Kbytes of Flash memory and 6 Kbytes of RAM, in a UFQFPN20 package
- On-board ST-LINK/V2-1 debugger/programmer with USB re-enumeration capability: mass storage and debug port
- User LED
- Reset push-button
- 5 way joystick using a single ADC input pin
- Individual STM32 UFQFPN20 to DIL20 module
- Board connectors:

  - USB Micro-B
  - DIL20 socket
  - Dedicated LCD footprint
  - Grove (UART)
  - 2 x 10 pin headers for MCU daughterboard
  - Extension connectors

More information about STM32C011F6 can be found here:

- [STM32C011F6 on www.st.com](https://www.st.com/resource/en/datasheet/stm32c011f6.pdf)
- [STM32C0x1 reference manual](https://www.st.com/resource/en/reference_manual/rm0490-stm32c0x1-advanced-armbased-64bit-mcus-stmicroelectronics.pdf)

### Supported Features

The `stm32c0116_dk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `stm32c0116_dk/stm32c011xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L29) | [`arm,cortex-m0+`](../../../../build/dts/api/bindings/cpu/arm,cortex-m0+.md#std-dtcompatible-arm-cortex-m0) |
| ADC | on-chip | STM32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L315) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st,stm32-adc.md#std-dtcompatible-st-stm32-adc) |
| Clock control | on-chip | STM32F0/G0 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L103) | [`st,stm32f0-rcc`](../../../../build/dts/api/bindings/clock/st,stm32f0-rcc.md#std-dtcompatible-st-stm32f0-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L41) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | STM32C0 HSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L47) | [`st,stm32c0-hsi-clock`](../../../../build/dts/api/bindings/clock/st,stm32c0-hsi-clock.md#std-dtcompatible-st-stm32c0-hsi-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L55) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L63) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 Microcontroller Clock Output (MCO)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L72) | [`st,stm32-clock-mco`](../../../../build/dts/api/bindings/clock/st,stm32-clock-mco.md#std-dtcompatible-st-stm32-clock-mco) |
| DMA | on-chip | STM32 DMA controller (V2)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L332) | [`st,stm32-dma-v2`](../../../../build/dts/api/bindings/dma/st,stm32-dma-v2.md#std-dtcompatible-st-stm32-dma-v2) |
| on-chip | STM32 DMAMUX controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L344) | [`st,stm32-dmamux`](../../../../build/dts/api/bindings/dma/st,stm32-dmamux.md#std-dtcompatible-st-stm32-dmamux) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L84) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st,stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L132) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st,stm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| I2C | on-chip | STM32 I2C V2 controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L293) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st,stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32c0116_dk/stm32c0116_dk.dts?plain=1#L39) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| on-board | Input driver for ADC attached resistor ladder buttons[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32c0116_dk/stm32c0116_dk.dts?plain=1#L49) | [`adc-keys`](../../../../build/dts/api/bindings/input/adc-keys.md#std-dtcompatible-adc-keys) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| on-chip | STM32G0 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L114) | [`st,stm32g0-exti`](../../../../build/dts/api/bindings/interrupt-controller/st,stm32g0-exti.md#std-dtcompatible-st-stm32g0-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32c0116_dk/stm32c0116_dk.dts?plain=1#L23) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32c0116_dk/stm32c0116_dk.dts?plain=1#L31) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L93) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st,stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L126) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st,stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L218)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L235) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st,stm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L108) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st,stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L165) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st,stm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 TEMP for production calibrated sensors with a single calibration temperature[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L356) | [`st,stm32c0-temp-cal`](../../../../build/dts/api/bindings/sensor/st,stm32c0-temp-cal.md#std-dtcompatible-st-stm32c0-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L366) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st,stm32-vref.md#std-dtcompatible-st-stm32-vref) |
| Serial controller | on-chip | STM32 USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L190) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st,stm32-usart.md#std-dtcompatible-st-stm32-usart) |
| SMbus | on-chip | STM32 SMBus controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L374) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st,stm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller with embedded Rx and Tx FIFOs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L305) | [`st,stm32-spi-fifo`](../../../../build/dts/api/bindings/spi/st,stm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L36) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv6-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21) | [`arm,armv6m-systick`](../../../../build/dts/api/bindings/timer/arm,armv6m-systick.md#std-dtcompatible-arm-armv6m-systick) |
| on-chip | STM32 timers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L208)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L225) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st,stm32-timers.md#std-dtcompatible-st-stm32-timers) |
| Watchdog | on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L176) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |
| on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/c0/stm32c0.dtsi?plain=1#L184) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |

### Pin Mapping

STM32C0116-DK Discovery kit has 4 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

For more details please refer to [STM32C0116-DK board User Manual](https://www.st.com/resource/en/user_manual/um2970-discovery-kit-with-stm32c011f6-mcu-stmicroelectronics.pdf).

#### Default Zephyr Peripheral Mapping:

The STM32C0116 Discovery board is configured as follows:

- UART\_2 TX/RX : PA2/PA3
- UART\_1 TX/RX : PA9/PA10 (ST-Link Virtual Port Com)
- PWM\_1\_CH3 : PB6
- ADC1\_CH8 : PA8
- LD3 : PB6

## Programming and Debugging

STM32C0116-DK Discovery kit includes an ST-LINK/V2 embedded debug tool interface.

Applications for the `stm32c0116_dk` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner jlink
```

#### Flashing an application to STM32C0116-DK

First, connect the STM32C0116 Discovery kit to your host computer using
the USB port to prepare it for flashing. Then build and flash your application.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b stm32c0116_dk samples/hello_world
west flash
```

Run a serial host program to connect with your board:

```shell
$ minicom -D /dev/ttyACM0
```

You should see the following message on the console:

```shell
Hello World! arm
```

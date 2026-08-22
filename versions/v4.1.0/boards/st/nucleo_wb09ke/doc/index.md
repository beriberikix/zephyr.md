---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/nucleo_wb09ke/doc/index.html
original_path: boards/st/nucleo_wb09ke/doc/index.html
---

# Nucleo WB09KE

Board Overview

[![../../../../_images/nucleo_wb09ke.webp](../../../../_images/nucleo_wb09ke.webp)
](../../../../_images/nucleo_wb09ke.webp)

Nucleo WB09KE

Name:
:   `nucleo_wb09ke`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32wb09

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_wb09ke/doc/index.rst/../..)

## Overview

The Nucleo WB09KE board is a Bluetooth® Low Energy wireless and ultra-low-power
board featuring an ARM Cortex®-M0+ based STM32WB09KEV MCU, embedding a
powerful and ultra-low-power radio compliant with the Bluetooth® Low Energy
SIG specification v5.4.

More information about the board can be found on the [Nucleo WB09KE webpage](https://www.st.com/en/evaluation-tools/nucleo-wb09ke.html).

## Hardware

Nucleo WB09KE provides the following hardware components:

- STM32WB09KEV in VFQFPN32 package
- ARM® 32-bit Cortex®-M0+ CPU
- 64 MHz maximal CPU frequebct
- 512 KB Flash
- 64 KB SRAM

More information about STM32WB09KEV can be found here:

- [WB09KE on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32wb09ke.html)
- [STM32WB09 reference manual](https://www.st.com/resource/en/reference_manual/rm0505-stm32wb09xe-ultralow-power-wireless-32bit-mcu-armbased-cortexm0-with-bluetooth-low-energy-and-24-ghz-radio-solution-stmicroelectronics.pdf)

### Supported Features

The `nucleo_wb09ke` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `nucleo_wb09ke/stm32wb09` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb0/stm32wb0.dtsi?plain=1#L33) | [`arm,cortex-m0+`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m0%2B.md#std-dtcompatible-arm-cortex-m0) |
| ADC | on-chip | STM32WB0 Analog-to-Digital Converter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb0/stm32wb0.dtsi?plain=1#L222) | [`st,stm32wb0-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32wb0-adc.md#std-dtcompatible-st-stm32wb0-adc) |
| Bluetooth | on-chip | Bluetooth HCI driver for ST STM32WB0 series[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb0/stm32wb0.dtsi?plain=1#L280) | [`st,hci-stm32wb0`](../../../../build/dts/api/bindings/bluetooth/st%2Chci-stm32wb0.md#std-dtcompatible-st-hci-stm32wb0) |
| Clock control | on-chip | STM32WB0 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb0/stm32wb0.dtsi?plain=1#L125) | [`st,stm32wb0-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32wb0-rcc.md#std-dtcompatible-st-stm32wb0-rcc) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb0/stm32wb0.dtsi?plain=1#L49)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb0/stm32wb0.dtsi?plain=1#L99) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb0/stm32wb0.dtsi?plain=1#L77) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32WB0 LSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb0/stm32wb0.dtsi?plain=1#L85) | [`st,stm32wb0-lsi-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32wb0-lsi-clock.md#std-dtcompatible-st-stm32wb0-lsi-clock) |
| Counter | on-chip | STM32 counters[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb0/stm32wb05.dtsi?plain=1#L29) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st%2Cstm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DMA | on-chip | STM32 DMA controller (V2bis) for the stm32F0, stm32F1 and stm32L1 soc families[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb0/stm32wb0.dtsi?plain=1#L238) | [`st,stm32-dma-v2bis`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dma-v2bis.md#std-dtcompatible-st-stm32-dma-v2bis) |
| on-chip | STM32 DMAMUX controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb0/stm32wb0.dtsi?plain=1#L249) | [`st,stm32-dmamux`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dmamux.md#std-dtcompatible-st-stm32-dmamux) |
| Flash controller | on-chip | STM32WB0 series flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb0/stm32wb0.dtsi?plain=1#L108) | [`st,stm32wb0-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32wb0-flash-controller.md#std-dtcompatible-st-stm32wb0-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb0/stm32wb0.dtsi?plain=1#L164) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_wb09ke/arduino_r3_connector.dtsi?plain=1#L8) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | STM32 I2C V2 controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb0/stm32wb0.dtsi?plain=1#L200) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_wb09ke/nucleo_wb09ke.dts?plain=1#L50) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| on-chip | STM32WB0 GPIO Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb0/stm32wb0.dtsi?plain=1#L146) | [`st,stm32wb0-gpio-intc`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32wb0-gpio-intc.md#std-dtcompatible-st-stm32wb0-gpio-intc) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_wb09ke/nucleo_wb09ke.dts?plain=1#L29) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_wb09ke/nucleo_wb09ke.dts?plain=1#L42) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb0/stm32wb0.dtsi?plain=1#L116) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st%2Cstm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_wb09ke/nucleo_wb09ke.dts?plain=1#L147) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb0/stm32wb0.dtsi?plain=1#L158) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| Power management | on-chip | STM32WB0 power controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb0/stm32wb0.dtsi?plain=1#L136) | [`st,stm32wb0-pwr`](../../../../build/dts/api/bindings/power/st%2Cstm32wb0-pwr.md#std-dtcompatible-st-stm32wb0-pwr) |
| PWM | on-chip | STM32 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb0/stm32wb05.dtsi?plain=1#L23)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb0/stm32wb05.dtsi?plain=1#L45) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb0/stm32wb0.dtsi?plain=1#L130) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb0/stm32wb0.dtsi?plain=1#L271) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st%2Cstm32-rng.md#std-dtcompatible-st-stm32-rng) |
| Serial controller | on-chip | STM32 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb0/stm32wb0.dtsi?plain=1#L181) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb0/stm32wb0.dtsi?plain=1#L191) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SPI | on-chip | STM32 SPI controller with embedded Rx and Tx FIFOs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb0/stm32wb0.dtsi?plain=1#L212) | [`st,stm32-spi-fifo`](../../../../build/dts/api/bindings/spi/st%2Cstm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb0/stm32wb0.dtsi?plain=1#L40) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv6-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21) | [`arm,armv6m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv6m-systick.md#std-dtcompatible-arm-armv6m-systick) |
| on-chip | STM32 timers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb0/stm32wb05.dtsi?plain=1#L13)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wb0/stm32wb05.dtsi?plain=1#L35) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers) |

#### Bluetooh support

BLE support is enabled; however, to build a Zephyr sample using this board,
you first need to fetch the Bluetooth controller library into Zephyr as a binary BLOB.

To fetch binary BLOBs:

```shell
west blobs fetch hal_stm32
```

### Connections and IOs

#### Default Zephyr Peripheral Mapping:

- USART1 TX/RX : PA1/PB0 (ST-Link Virtual COM Port)
- BUTTON (B1) : PA0
- BUTTON (B2) : PB5
- BUTTON (B3) : PB14
- LED (LD1/BLUE) : PB1
- LED (LD2/GREEN) : PB4
- LED (LD3/RED) : PB2

For more details, please refer to the [Nucleo WB09KE board User Manual](https://www.st.com/resource/en/user_manual/um3345-stm32wb09-nucleo64-board-mb1801-and-mb2032-stmicroelectronics.pdf).

## Programming and Debugging

Nucleo WB09KE board includes an ST-LINK-V3EC embedded debug tool interface.

Applications for the `nucleo_w09ke` board target can be built and flashed
in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run)
for more details).

### Flashing

The board is configured to be flashed using the west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so [it must be installed](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) beforehand.

Alternatively, OpenOCD can also be used to flash the board using the
`--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
```

#### Flashing an application to Nucleo WB09KE

Connect the Nucleo WB09KE to your host computer using the USB port,
then run a serial host program to connect with your Nucleo board:

```shell
$ minicom -D /dev/ttyACM0
```

Now build and flash an application. Here is an example for
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.").

```shell
# From the root of the zephyr repository
west build -b nucleo_wb09ke samples/hello_world
west flash
```

You should see the following message on the console:

```shell
Hello World! nucleo_wb09ke/stm32wb09
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_wb09ke samples/hello_world
west debug
```

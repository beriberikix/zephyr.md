---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/nucleo_f207zg/doc/index.html
original_path: boards/st/nucleo_f207zg/doc/index.html
---

# Nucleo F207ZG

Board Overview

[![../../../../_images/nucleo_f207zg.jpg](../../../../_images/nucleo_f207zg.jpg)
](../../../../_images/nucleo_f207zg.jpg)

Nucleo F207ZG

Name:
:   `nucleo_f207zg`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32f207xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_f207zg/doc/index.rst/../..)

## Overview

The Nucleo F207ZG board features an ARM Cortex-M3 based STM32F207ZG MCU
with a wide range of connectivity support and configurations. Here are
some highlights of the Nucleo F207ZG board:

- STM32 microcontroller in LQFP144 package
- Ethernet compliant with IEEE-802.3-2002
- Two types of extension resources:

  - ST Zio connector including: support for Arduino\* Uno V3 connectivity
    (A0 to A5, D0 to D15) and additional signals exposing a wide range of
    peripherals
  - ST morpho extension pin headers for full access to all STM32 I/Os
- On-board ST-LINK/V2-1 debugger/programmer with SWD connector
- Flexible board power supply:

  - 5 V from ST-LINK/V2-1 USB VBUS
  - External power sources: 3.3 V and 7 - 12 V on ST Zio or ST morpho
    connectors, 5 V on ST morpho connector
- Three user LEDs
- Two push-buttons: USER and RESET

More information about the board can be found at the [Nucleo F207ZG website](https://www.st.com/en/evaluation-tools/nucleo-f207zg.html).

## Hardware

Nucleo F207ZG provides the following hardware components:

- STM32F207ZGT6 in LQFP144 package
- ARM® 32-bit Cortex® -M3 CPU
- 120 MHz max CPU frequency
- VDD from 1.7 V to 3.6 V
- 1 MB Flash
- 128 KB SRAM
- GPIO with external interrupt capability
- 12-bit ADC with 24 channels
- RTC
- 17 General purpose timers
- 2 watchdog timers (independent and window)
- SysTick timer
- USART/UART (6)
- I2C (3)
- SPI (3)
- SDIO
- USB 2.0 OTG FS
- DMA Controller
- 10/100 Ethernet MAC with dedicated DMA
- CRC calculation unit
- True random number generator

More information about STM32F207ZG can be found here:

- [STM32F207ZG on www.st.com](https://www.st.com/en/microcontrollers/stm32f207zg.html)
- [STM32F207 reference manual](https://www.st.com/resource/en/reference_manual/cd00225773.pdf)

### Supported Features

The `nucleo_f207zg` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `nucleo_f207zg/stm32f207xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M3 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L31) | [`arm,cortex-m3`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m3.md#std-dtcompatible-arm-cortex-m3) |
| ADC | on-chip | STM32F4 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L365) | [`st,stm32f4-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32f4-adc.md#std-dtcompatible-st-stm32f4-adc) |
| Clock control | on-chip | STM32 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L95) | [`st,stm32-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32-rcc.md#std-dtcompatible-st-stm32-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L43) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L63)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L49) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32F2 Main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L70) | [`st,stm32f2-pll-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32f2-pll-clock.md#std-dtcompatible-st-stm32f2-pll-clock) |
| Counter | on-chip | STM32 counters[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L459) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st%2Cstm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L401) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st%2Cstm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32 DMA controller (V1)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L391)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L382) | [`st,stm32-dma-v1`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dma-v1.md#std-dtcompatible-st-stm32-dma-v1) |
| Ethernet | on-chip | ST STM32 Ethernet[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f207.dtsi?plain=1#L13) | [`st,stm32-ethernet`](../../../../build/dts/api/bindings/ethernet/st%2Cstm32-ethernet.md#std-dtcompatible-st-stm32-ethernet) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L78) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO controller[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L127) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_f207zg/arduino_r3_connector.dtsi?plain=1#L8) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | STM32 I2C V1 controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L315)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L339) | [`st,stm32-i2c-v1`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v1.md#std-dtcompatible-st-stm32-i2c-v1) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_f207zg/nucleo_f207zg.dts?plain=1#L57) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L106) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_f207zg/nucleo_f207zg.dts?plain=1#L24) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_f207zg/nucleo_f207zg.dts?plain=1#L40) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Memory controller | on-chip | STM32 Battery Backed RAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L210) | [`st,stm32-bbram`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32-bbram.md#std-dtcompatible-st-stm32-bbram) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L86) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st%2Cstm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_f207zg/nucleo_f207zg.dts?plain=1#L195) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L715) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L121) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L419)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L436) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L100) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L690) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st%2Cstm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L200) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st%2Cstm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 Internal Temperature Sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L707) | [`st,stm32-temp`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-temp.md#std-dtcompatible-st-stm32-temp) |
| Serial controller | on-chip | STM32 USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L249)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L231) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 UART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L267) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-uart.md#std-dtcompatible-st-stm32-uart) |
| SMbus | on-chip | STM32 SMBus controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L720) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st%2Cstm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L285)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L295) | [`st,stm32-spi`](../../../../build/dts/api/bindings/spi/st%2Cstm32-spi.md#std-dtcompatible-st-stm32-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L38) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 timers[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L409)[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L426) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers) |
| USB | on-chip | STM32 OTGFS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L351) | [`st,stm32-otgfs`](../../../../build/dts/api/bindings/usb/st%2Cstm32-otgfs.md#std-dtcompatible-st-stm32-otgfs) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L217) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f2/stm32f2.dtsi?plain=1#L223) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Connections and IOs

Nucleo F207ZG Board has 8 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

#### Available pins:

![Nucleo F207ZG ZIO connectors (left)](../../../../_images/nucleo_f207zg_zio_left.jpg)
![Nucleo F207ZG ZIO connectors (right)](../../../../_images/nucleo_f207zg_zio_right.jpg)
![Nucleo F207ZG Morpho connectors (left)](../../../../_images/nucleo_f207zg_morpho_left.jpg)
![Nucleo F207ZG Morpho connectors (right)](../../../../_images/nucleo_f207zg_morpho_right.jpg)

For more details please refer to [STM32 Nucleo-144 board User Manual](https://www.st.com/resource/en/user_manual/dm00244518.pdf).

#### Default Zephyr Peripheral Mapping:

- UART\_3 TX/RX : PD8/PD9 (ST-Link Virtual Port Com)
- UART\_6 TX/RX : PG14/PG9 (Arduino Serial)
- I2C1 SCL/SDA : PB8/PB9 (Arduino I2C)
- SPI1 NSS/SCK/MISO/MOSI : PD14/PA5/PA6/PA7 (Arduino SPI)
- ETH : PA1, PA2, PA7, PB13, PC1, PC4, PC5, PG11, PG13
- USB\_DM : PA11
- USB\_DP : PA12
- USER\_PB : PC13
- LD1 : PB0
- LD2 : PB7
- LD3 : PB14
- DAC: PA4
- ADC: PA0
- PWM\_1\_CH1 : PE9

#### System Clock

Nucleo F207ZG System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by PLL clock at 120MHz,
driven by 8MHz high speed external clock.

#### Serial Port

Nucleo F207ZG board has 4 UARTs. The Zephyr console output is assigned to UART3.
Default settings are 115200 8N1.

#### Network interface

Ethernet configured as the default network interface

#### USB

Nucleo F207ZG board has a USB OTG dual-role device (DRD) controller that
supports both device and host functions through its micro USB connector
(USB USER). Only USB device function is supported in Zephyr at the moment.

#### Backup SRAM

In order to test backup SRAM you may want to disconnect VBAT from VDD. You can
do it by removing `SB156` jumper on the back side of the board.

## Programming and Debugging

Nucleo F207ZG board includes an ST-LINK/V2-1 embedded debug tool interface.

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD or JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
```

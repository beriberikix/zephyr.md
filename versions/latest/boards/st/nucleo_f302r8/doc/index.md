---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/st/nucleo_f302r8/doc/index.html
original_path: boards/st/nucleo_f302r8/doc/index.html
---

# Nucleo F302R8

Board Overview

[![../../../../_images/nucleo_f302r8.jpg](../../../../_images/nucleo_f302r8.jpg)
](../../../../_images/nucleo_f302r8.jpg)

Nucleo F302R8

Name:
:   `nucleo_f302r8`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32f302x8

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_f302r8/doc/index.rst/../..)

## Overview

The Nucleo F302R8 board features an ARM Cortex-M4 based STM32F302R8
mixed-signal MCU with FPU and DSP instructions capable of running at 72 MHz.
Here are some highlights of the Nucleo F302R8 board:

- STM32 microcontroller in LQFP64 package
- LSE crystal: 32.768 kHz crystal oscillator
- Two types of extension resources:

  - Arduino\* Uno V3 connectors
  - ST morpho extension pin headers for full access to all STM32 I/Os
- On-board ST-LINK/V2-1 debugger/programmer with SWD connector
- Flexible board power supply:

  - 5 V from ST-LINK/V2-1 USB VBUS
  - External power sources: 3.3 V and 7 - 12 V on ST Zio or ST morpho
    connectors, 5 V on ST morpho connector
- One user LED
- Two push-buttons: USER and RESET

More information about the board can be found at the [Nucleo F302R8 website](https://www.st.com/en/evaluation-tools/nucleo-f302r8.html),
and in the [STM32 Nucleo-64 board User Manual](https://www.st.com/resource/en/user_manual/dm00105823.pdf).

## Hardware

The Nucleo F302R8 provides the following hardware components:

- STM32F302R8T6 in QFP64 package
- ARM® 32-bit Cortex® -M4 CPU with FPU
- 72 MHz max CPU frequency
- VDD from 2.0 V to 3.6 V
- 64 KB Flash
- 16 KB SRAM
- RTC
- Advanced-control Timer
- General Purpose Timers (4)
- Basic Timer
- Watchdog Timers (2)
- PWM channels (18)
- SPI/I2S (2)
- I2C (3)
- USART/UART (3/3)
- USB 2.0 FS with on-chip PHY
- CAN (2)
- GPIO with external interrupt capability
- DMA channels (7)
- Capacitive sensing channels (18)
- 12-bit ADC with 15 channels
- 12-bit D/A converter
- Analog comparator (3)
- Op amp

More information about the STM32F302R8 can be found here:

- [STM32F302R8 on www.st.com](https://www.st.com/en/microcontrollers/stm32f302r8.html)
- [STM32F302R8 reference manual](https://www.st.com/resource/en/reference_manual/dm00094349.pdf)
- [STM32F302R8 datasheet](https://www.st.com/resource/en/datasheet/stm32f302r8.pdf)

### Supported Features

The `nucleo_f302r8` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `nucleo_f302r8/stm32f302x8` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L29) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | STM32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f302.dtsi?plain=1#L105) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32-adc.md#std-dtcompatible-st-stm32-adc) |
| CAN | on-chip | STM32 CAN controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L420) | [`st,stm32-bxcan`](../../../../build/dts/api/bindings/can/st%2Cstm32-bxcan.md#std-dtcompatible-st-stm32-bxcan) |
| Clock control | on-chip | STM32F3 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L97) | [`st,stm32f3-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32f3-rcc.md#std-dtcompatible-st-stm32f3-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L42) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L63)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L48) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L55) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32F0/F3 Main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L70) | [`st,stm32f0-pll-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32f0-pll-clock.md#std-dtcompatible-st-stm32f0-pll-clock) |
| Counter | on-chip | STM32 counters[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L283) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st%2Cstm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L246) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st%2Cstm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32 DMA controller (V2bis) for the stm32F0, stm32F1 and stm32L1 soc families[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L429) | [`st,stm32-dma-v2bis`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dma-v2bis.md#std-dtcompatible-st-stm32-dma-v2bis) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L78) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO Controller[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L129) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_f302r8/arduino_r3_connector.dtsi?plain=1#L8) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| on-board | GPIO pins exposed on ST Morpho connector[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_f302r8/st_morpho_connector.dtsi?plain=1#L10) | [`st-morpho-header`](../../../../build/dts/api/bindings/gpio/st-morpho-header.md#std-dtcompatible-st-morpho-header) |
| I2C | on-chip | STM32 I2C V2 controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L220)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f302.dtsi?plain=1#L19) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_f302r8/nucleo_f302r8.dts?plain=1#L34) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L108) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_f302r8/nucleo_f302r8.dts?plain=1#L25) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Memory controller | on-chip | STM32 Battery Backed RAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f302X8.dtsi?plain=1#L23) | [`st,stm32-bbram`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32-bbram.md#std-dtcompatible-st-stm32-bbram) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L87) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st%2Cstm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L465) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L123) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L277)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L299) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L102) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L409) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st%2Cstm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L439) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L450) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L458) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L184) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L211) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-uart.md#std-dtcompatible-st-stm32-uart) |
| SMbus | on-chip | STM32 SMBus controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L470) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st%2Cstm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller with embedded Rx and Tx FIFOs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f302.dtsi?plain=1#L51)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f302.dtsi?plain=1#L61) | [`st,stm32-spi-fifo`](../../../../build/dts/api/bindings/spi/st%2Cstm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L36) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 timers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L267)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L289) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers) |
| USB | on-chip | STM32 USB controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L254) | [`st,stm32-usb`](../../../../build/dts/api/bindings/usb/st%2Cstm32-usb.md#std-dtcompatible-st-stm32-usb) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L170) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L176) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Connections and IOs

The Nucleo F302R8 Board has 5 GPIO controllers. These controllers are
responsible for pin muxing, input/output, pull-up, etc.

#### Board connectors:

![Nucleo F302R8 connectors](../../../../_images/nucleo_f302r8_connectors.jpg)

#### Default Zephyr Peripheral Mapping:

The Nucleo F302R8 board features an Arduino Uno V3 connector and a ST
morpho connector. Board is configured as follows:

- UART\_2 TX/RX : PA2/PA3 (ST-Link Virtual Port Com)
- UART\_3 TX/RX : PC10/PC11
- I2C1 SCL/SDA : PB8/PB9 (Arduino I2C)
- SPI2 CS/SCK/MISO/MOSI : PB6/PB13/PB14/P15 (Arduino SPI)
- PWM\_2\_CH2 : PA0
- USER\_PB : PC13
- LD2 : PB13

#### System Clock

The Nucleo F302R8 System Clock can be driven by an internal or
external oscillator, as well as by the main PLL clock. By default the
System Clock is driven by the PLL clock at 72 MHz. The input to the
PLL is an 8 MHz external clock supplied by the processor of the
on-board ST-LINK/V2-1 debugger/programmer.

#### Serial Port

The Nucleo F302R8 board has 3 UARTs. The Zephyr console output is assigned
to UART2. Default settings are 115200 8N1.

## Programming and Debugging

The `nucleo_f302r8` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |
| **[stm32cubeprogrammer](../../../../develop/flash_debug/host-tools.md#runner-stm32cubeprogrammer)** | ✅ (default) |  |  |  |  |

The Nucleo F302R8 board includes an ST-LINK/V2-1 embedded debug tool interface.

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD or JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
```

---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/stm32373c_eval/doc/index.html
original_path: boards/st/stm32373c_eval/doc/index.html
---

# STM32373C Evaluation

Board Overview

[![../../../../_images/stm32373c_eval.jpg](../../../../_images/stm32373c_eval.jpg)
](../../../../_images/stm32373c_eval.jpg)

STM32373C Evaluation

Name:
:   `stm32373c_eval`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32f373xc

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm32373c_eval/doc/index.rst/../..)

## Overview

The STM32373C-EVAL evaluation board is designed as a complete demonstration and development platform for STMicroelectronics ARM Cortex-M4 core-based STM32F373VCT6 microcontroller.

The full range of hardware features on the board can help the user evaluate all peripherals (USB FS, USART, audio DAC, microphone ADC, dot-matrix LCD, IrDA, LDR, MicroSD card, HDMI CEC, ECG, pressure sensor, CAN, IR transmitter and receiver, EEPROM, touch slider, temperature sensor, etc.) and develop their own applications.

Extension headers make it possible to easily connect a daughter board or wrapping board for a specific application.

More information about the board can be found at the [STM32373C-EVAL website](https://www.st.com/en/evaluation-tools/stm32373c-eval.html) [[1]](#id2).

## Hardware

STM32373C-EVAL provides the following hardware components:

- STM32F373VCT6 microcontroller
- Four 5 V power supply options:
  :   - Power jack
      - ST-LINK/V2 USB connector
      - User USB connector
      - Daughter board
- Audio jack connected to I2 S DAC
- Microphone connected to ADC through an amplifier
- 2-GByte (or more) MicroSD card on SPI
- Three components on I2 C bus: temperature sensor, EEPROM and dual interface RF EEPROM
- RS-232 communication configurable for communication of Flash loader
- IrDA transceiver
- 240x320 TFT color LCD connected to SPI interface
- Joystick with 4-direction control and selector
- Reset, Wakeup or Tamper, and Key buttons
- 4 color user LEDs
- 2 LEDs for MCU power range indicator
- ECG, pressure sensor and PT100 temperature sensor connected to the 16-bit Sigma Delta ADC of STM32F373VCT6
- Extension connectors for daughter board or wrapping board
- MCU voltage: 3.3 V or adjustable 2.0 V - 3.6 V
- USB FS connector
- Touch slider
- RTC with backup battery
- CAN 2.0 A/B compliant connection
- Light dependent resistor (LDR)
- Two HDMI connectors with DDC and CEC
- IR transmitter and receiver
- Two ADC & DAC input and output signal connectors and one Sigma Delta ADC input signal connector
- Potentiometer
- JTAG/SWD and ETM trace debug support
- Embedded ST-LINK/V2

More information about STM32F373VCT6 can be found here:
:   - [STM32F373VCT6 reference manual](https://www.st.com/resource/en/reference_manual/dm00041563.pdf) [[2]](#id4)

### Supported Features

The `stm32373c_eval` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `stm32373c_eval/stm32f373xc` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L29) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | STM32F1 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f373.dtsi?plain=1#L187) | [`st,stm32f1-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32f1-adc.md#std-dtcompatible-st-stm32f1-adc) |
| CAN | on-chip | STM32 CAN controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L419) | [`st,stm32-bxcan`](../../../../build/dts/api/bindings/can/st%2Cstm32-bxcan.md#std-dtcompatible-st-stm32-bxcan) |
| Clock control | on-chip | STM32F1/F3/7x RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L97) | [`st,stm32f1-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32f1-rcc.md#std-dtcompatible-st-stm32f1-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L42) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L63)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L48) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L55) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32F0/F3 Main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L70) | [`st,stm32f0-pll-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32f0-pll-clock.md#std-dtcompatible-st-stm32f0-pll-clock) |
| Counter | on-chip | STM32 counters[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L282) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st%2Cstm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DAC | on-chip | STM32 family DAC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L246) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st%2Cstm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32 DMA controller (V2bis) for the stm32F0, stm32F1 and stm32L1 soc families[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L428) | [`st,stm32-dma-v2bis`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dma-v2bis.md#std-dtcompatible-st-stm32-dma-v2bis) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L78) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO controller[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L129) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| I2C | on-chip | STM32 I2C V2 controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L220) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32373c_eval/stm32373c_eval.dts?plain=1#L31) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L108) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32373c_eval/stm32373c_eval.dts?plain=1#L23) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Memory controller | on-chip | STM32 Battery Backed RAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f373.dtsi?plain=1#L201) | [`st,stm32-bbram`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32-bbram.md#std-dtcompatible-st-stm32-bbram) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L87) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st%2Cstm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L464) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L123) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L276) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L102) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L408) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st%2Cstm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L438) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L449) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L457) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L193)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L184) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L211) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-uart.md#std-dtcompatible-st-stm32-uart) |
| SMbus | on-chip | STM32 SMBus controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L469) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st%2Cstm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller with embedded Rx and Tx FIFOs[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L236) | [`st,stm32-spi-fifo`](../../../../build/dts/api/bindings/spi/st%2Cstm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L36) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 timers[14 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L266) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers) |
| USB | on-chip | STM32 USB controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L254) | [`st,stm32-usb`](../../../../build/dts/api/bindings/usb/st%2Cstm32-usb.md#std-dtcompatible-st-stm32-usb) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L170) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f3/stm32f3.dtsi?plain=1#L176) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Connections and IOs

Each of the GPIO pins can be configured by software as output (push-pull or open-drain), as
input (with or without pull-up or pull-down), or as peripheral alternate function. Most of the
GPIO pins are shared with digital or analog alternate functions. All GPIOs are high current
capable except for analog inputs.

#### Board connectors:

![STM32373C_EVAL connectors](../../../../_images/stm32373c_eval_connectors.jpg)

#### Default Zephyr Peripheral Mapping:

- UART\_2\_TX : PD5
- UART\_2\_RX : PD6
- USER\_PB : PA2
- LED2 : PC1

## Programming and Debugging

Applications for the `stm32373c_eval` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

STM32373C-EVAL board includes an ST-LINK/V2-1 embedded debug tool interface.
At power-on, the board is in firmware-upgrade mode (also called DFU for
“Device Firmware Upgrade”), allowing the firmware to be updated through the USB.
This interface is supported by the openocd version included in Zephyr SDK.

#### Flashing an application to STM32373C-EVAL

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b stm32373c_eval samples/basic/blinky
west flash
```

You will see the LED blinking every second.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b stm32373c_eval samples/basic/blinky
west debug
```

## References

[[1](#id3)]

[https://www.st.com/en/evaluation-tools/stm32373c-eval.html](https://www.st.com/en/evaluation-tools/stm32373c-eval.html)

[[2](#id5)]

[https://www.st.com/resource/en/reference\_manual/dm00041563.pdf](https://www.st.com/resource/en/reference_manual/dm00041563.pdf)

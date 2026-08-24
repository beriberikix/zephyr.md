---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/st/stm3210c_eval/doc/index.html
original_path: boards/st/stm3210c_eval/doc/index.html
---

# STM3210C Evaluation

Board Overview

[![../../../../_images/stm3210c_eval.jpg](https://docs.zephyrproject.org/4.2.0/_images/stm3210c_eval.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/stm3210c_eval.jpg)

STM3210C Evaluation

Name:
:   `stm3210c_eval`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32f107xc

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm3210c_eval/doc/index.rst/../..)

## Overview

The STM3210C-EVAL evaluation board is a complete development platform for STMicroelectronic’s
ARM Cortex-M3 core-based STM32F107VCT microcontroller.

The range of hardware features on the board help you to evaluate all peripherals
(USB-OTG FS, ethernet, motor control, CAN, microSD CardTM, smartcard, USART,
audio DAC, MEMS, EEPROM and more) and develop your own applications.

Extension headers make it easy to connect a daughterboard or wrapping board for your specific
application.

More information about the board can be found at the [STM3210C-EVAL website](https://www.st.com/en/evaluation-tools/stm3210c-eval.html) [[1]](#id2).

## Hardware

STM3210C-EVAL provides the following hardware components:

- Three 5 V power supply options:
  :   - Power jack
      - USB connector
      - daughterboard
- Boot from user Flash, system memory or SRAM.
- I2S audio DAC, stereo audio jack.
- 2 GByte (or more) microSD CardTM.
- Both type A and B smartcard support.
- I2C compatible serial interface 64 Kbit EEPROM, MEMS and I/O expander.
- RS-232 communication.
- IrDA transceiver.
- USB-OTG full speed, USB microAB connector.
- IEEE-802.3-2002 compliant ethernet connector.
- Two channels of CAN2.0A/B compliant connection.
- Inductor motor control connector.
- JTAG and trace debug support.
- 3.2” 240x320 TFT color LCD with touch screen.
- Joystick with 4-direction control and selector.
- Reset, Wakeup, Tamper and User button.
- 4 color LEDs.
- RTC with backup battery.
- MCU consumption measurement circuit.
- Extension connector for daughterboard or wrapping board.

More information about STM32F107VCT can be found here:
:   - [STM32F107VCT reference manual](https://www.st.com/resource/en/reference_manual/CD00171190.pdf) [[2]](#id4)

### Supported Features

The `stm3210c_eval` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `stm3210c_eval/stm32f107xc` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M3 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L31) | [`arm,cortex-m3`](../../../../build/dts/api/bindings/cpu/arm,cortex-m3.md#std-dtcompatible-arm-cortex-m3) |
| ADC | on-chip | STM32F1 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L363) | [`st,stm32f1-adc`](../../../../build/dts/api/bindings/adc/st,stm32f1-adc.md#std-dtcompatible-st-stm32f1-adc) |
| CAN | on-chip | STM32 CAN controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f105.dtsi?plain=1#L37) | [`st,stm32-bxcan`](../../../../build/dts/api/bindings/can/st,stm32-bxcan.md#std-dtcompatible-st-stm32-bxcan) |
| Clock control | on-chip | STM32F1/F3/7x RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L123) | [`st,stm32f1-rcc`](../../../../build/dts/api/bindings/clock/st,stm32f1-rcc.md#std-dtcompatible-st-stm32f1-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L62) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L68) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32F105/F107 Main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f105.dtsi?plain=1#L14) | [`st,stm32f105-pll-clock`](../../../../build/dts/api/bindings/clock/st,stm32f105-pll-clock.md#std-dtcompatible-st-stm32f105-pll-clock) |
| on-chip | STM32F105/F107 PLL2[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f105.dtsi?plain=1#L20) | [`st,stm32f105-pll2-clock`](../../../../build/dts/api/bindings/clock/st,stm32f105-pll2-clock.md#std-dtcompatible-st-stm32f105-pll2-clock) |
| on-chip | STM32F1 Microcontroller Clock Output (MCO)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L97) | [`st,stm32f1-clock-mco`](../../../../build/dts/api/bindings/clock/st,stm32f1-clock-mco.md#std-dtcompatible-st-stm32f1-clock-mco) |
| Counter | on-chip | STM32 counters[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L304) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st,stm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f105.dtsi?plain=1#L56) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st,stm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32 DMA controller (V2bis) for the stm32F0, stm32F1 and stm32L1 soc families[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L376) | [`st,stm32-dma-v2bis`](../../../../build/dts/api/bindings/dma/st,stm32-dma-v2bis.md#std-dtcompatible-st-stm32-dma-v2bis) |
| Ethernet | on-chip | ST STM32 Ethernet MAC, a child node of the Ethernet controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f107.dtsi?plain=1#L27) | [`st,stm32-ethernet`](../../../../build/dts/api/bindings/ethernet/st,stm32-ethernet.md#std-dtcompatible-st-stm32-ethernet) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L105) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st,stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO Controller[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L155) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st,stm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| I2C | on-chip | STM32 I2C V1 controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L223) | [`st,stm32-i2c-v1`](../../../../build/dts/api/bindings/i2c/st,stm32-i2c-v1.md#std-dtcompatible-st-stm32-i2c-v1) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm3210c_eval/stm3210c_eval.dts?plain=1#L32) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L134) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st,stm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm3210c_eval/stm3210c_eval.dts?plain=1#L23) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | STM32 MDIO Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f107.dtsi?plain=1#L36) | [`st,stm32-mdio`](../../../../build/dts/api/bindings/mdio/st,stm32-mdio.md#std-dtcompatible-st-stm32-mdio) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L114) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st,stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f105.dtsi?plain=1#L155) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32F1 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L149) | [`st,stm32f1-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st,stm32f1-pinctrl.md#std-dtcompatible-st-stm32f1-pinctrl) |
| Power management | on-chip | STM32 power controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L386) | [`st,stm32-pwr`](../../../../build/dts/api/bindings/power/st,stm32-pwr.md#std-dtcompatible-st-stm32-pwr) |
| PWM | on-chip | STM32 PWM[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L281) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st,stm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L128) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st,stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L354) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st,stm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 Internal Temperature Sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L402) | [`st,stm32-temp`](../../../../build/dts/api/bindings/sensor/st,stm32-temp.md#std-dtcompatible-st-stm32-temp) |
| Serial controller | on-chip | STM32 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L205)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L196) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st,stm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 UART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f105.dtsi?plain=1#L64) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st,stm32-uart.md#std-dtcompatible-st-stm32-uart) |
| SMbus | on-chip | STM32 SMBus controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L411) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st,stm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L247) | [`st,stm32-spi`](../../../../build/dts/api/bindings/spi/st,stm32-spi.md#std-dtcompatible-st-stm32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L57) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 timers[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L271) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st,stm32-timers.md#std-dtcompatible-st-stm32-timers) |
| USB | on-chip | STM32 OTGFS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f105.dtsi?plain=1#L141) | [`st,stm32-otgfs`](../../../../build/dts/api/bindings/usb/st,stm32-otgfs.md#std-dtcompatible-st-stm32-otgfs) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L257) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f1/stm32f1.dtsi?plain=1#L263) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Connections and IOs

Each of the GPIO pins can be configured by software as output (push-pull or open-drain), as
input (with or without pull-up or pull-down), or as peripheral alternate function. Most of the
GPIO pins are shared with digital or analog alternate functions. All GPIOs are high current
capable except for analog inputs.

#### Board connectors:

![STM3210C_EVAL connectors](https://docs.zephyrproject.org/4.2.0/_images/stm3210c_eval_connectors.jpg)

#### Default Zephyr Peripheral Mapping:

- UART\_2\_TX : PD5
- UART\_2\_RX : PD6
- USER\_PB : PB9
- LED2 : PD13

## Programming and Debugging

The `stm3210c_eval` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Flashing

STM3210C-EVAL board includes an ST-LINK/V2-1 embedded debug tool interface.
At power-on, the board is in firmware-upgrade mode (also called DFU for
“Device Firmware Upgrade”), allowing the firmware to be updated through the USB.
This interface is supported by the openocd version included in Zephyr SDK.

Applications for the `stm3210c_eval` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

#### Flashing an application to STM3210C-EVAL

Connect the STM3210C-EVAL to your host computer using the USB port, then build
and flash an application in the usual way.

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b stm3210c_eval samples/basic/blinky
west flash
```

You will see the LED blinking every second.

### Debugging

You can run a serial host program to connect with your STM3210C-EVAL board. For
example, on Linux:

```shell
$ minicom -D /dev/ttyACM0
```

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b stm3210c_eval samples/hello_world
west debug
```

## References

[[1](#id3)]

[https://www.st.com/en/evaluation-tools/stm3210c-eval.html](https://www.st.com/en/evaluation-tools/stm3210c-eval.html)

[[2](#id5)]

[https://www.st.com/resource/en/reference\_manual/CD00171190.pdf](https://www.st.com/resource/en/reference_manual/CD00171190.pdf)

---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/stm32g071b_disco/doc/index.html
original_path: boards/st/stm32g071b_disco/doc/index.html
---

# STM32G071B Discovery

Board Overview

[![../../../../_images/stm32g071b_disco.jpg](../../../../_images/stm32g071b_disco.jpg)
](../../../../_images/stm32g071b_disco.jpg)

STM32G071B Discovery

Name:
:   `stm32g071b_disco`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32g071xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm32g071b_disco/doc/index.rst/../..)

## Overview

The STM32G071B-DISCO Discovery board is a demonstration and development platform
for the STMicroelectronics Arm® Cortex® -M0+ core-based STM32G071RB USB Type-C™
and Power Delivery microcontroller. The STM32G071B-DISCO Discovery board is
presented with all necessary interfaces for easy connection and
interoperability with other USB Type-C™ devices. The STM32G071B-DISCO Discovery
board is intended for discovery and display of USB Type-C™ port characteristics
such as data role, power role, VBUS and IBUS monitoring. It offers an advanced
user mode when associated with the STM32CubeMonUCPD software GUI and can be used
as a USB Type-C™ and Power Delivery analyzer.

- STM32G071RBT6 microcontroller featuring 128 Kbytes of Flash memory and
  32 Kbytes of RAM in LQFP64 package
- Plastic case
- 1” 128 x 64 pixels OLED LCD module with SPI interface
- USB Type-C™ interface plug cable and receptacle connector accessible by door
  with reed sensor detection
- 3 bidirectional current and power monitors with I2C interface to measure VBUS,
  CC1 and CC2 protected and isolated lines
- On-board DC/DC converter to sustain power supply with VBUS varying from 3 V to
  20 V (+/- 5 %)
- 4 user status LEDs about USB Type-C™ configuration
- 3 LEDs for power and ST-LINK communication
- 4-way joystick with selection button
- 1 reset push-button
- Board external connectors:
  :   - USB Type-C™ plug cable
      - USB Type-C™ receptacle connector
      - 8-pin user extension connector including ADC, SPI, USART and
        I2C communication signals
      - USB with Micro-AB (ST-LINK)
- Board internal connectors:
  :   - 2 x 8-pin GPIOs free pins from microcontroller
        :   (accessible internally when case is removed)
      - USB Type-C™ test points for main signals
- Flexible power-supply options: ST-LINK USB VBUS or USB Type-C™ VBUS
- On-board ST-LINK/V2-1 debugger/programmer with USB enumeration capability:
  mass storage, Virtual COM port and debug port

More information about the board can be found at the [STM32G071B-DISCO website](https://www.st.com/en/evaluation-tools/stm32g071b-disco.html) [[1]](#id2).

More information about STM32G071RB can be found here:

- [G071RB on www.st.com](https://www.st.com/en/microcontrollers/stm32g071rb.html) [[4]](#id8)
- [STM32G071 reference manual](https://www.st.com/resource/en/reference_manual/dm00371828.pdf) [[2]](#id4)

### Supported Features

The `stm32g071b_disco` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `stm32g071b_disco/stm32g071xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L32) | [`arm,cortex-m0+`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m0%2B.md#std-dtcompatible-arm-cortex-m0) |
| ADC | on-chip | STM32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L406) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32-adc.md#std-dtcompatible-st-stm32-adc) |
| Clock control | on-chip | STM32F0/G0 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L116) | [`st,stm32f0-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32f0-rcc.md#std-dtcompatible-st-stm32f0-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L60) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | STM32G0 HSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L66) | [`st,stm32g0-hsi-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32g0-hsi-clock.md#std-dtcompatible-st-stm32g0-hsi-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L74) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L82) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32G0 main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L89) | [`st,stm32g0-pll-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32g0-pll-clock.md#std-dtcompatible-st-stm32g0-pll-clock) |
| Counter | on-chip | STM32 counters[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L268) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st%2Cstm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g051.dtsi?plain=1#L66) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st%2Cstm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32 DMA controller (V2)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L429) | [`st,stm32-dma-v2`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dma-v2.md#std-dtcompatible-st-stm32-dma-v2) |
| on-chip | STM32 DMAMUX controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L441) | [`st,stm32-dmamux`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dmamux.md#std-dtcompatible-st-stm32-dmamux) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L97) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO controller[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L145) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| I2C | on-chip | STM32 I2C V2 controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L362)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L374) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32g071b_disco/stm32g071b_disco.dts?plain=1#L44) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| on-chip | STM32G0 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L127) | [`st,stm32g0-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32g0-exti.md#std-dtcompatible-st-stm32g0-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32g071b_disco/stm32g071b_disco.dts?plain=1#L24) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Memory controller | on-chip | STM32 Battery Backed RAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L202) | [`st,stm32-bbram`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32-bbram.md#std-dtcompatible-st-stm32-bbram) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L106) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st%2Cstm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L139) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L262) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L121) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L186) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st%2Cstm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-board | TI INA230, INA231 and INA236 Bidirectional Current and Power Monitor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32g071b_disco/stm32g071b_disco.dts?plain=1#L143) | [`ti,ina230`](../../../../build/dts/api/bindings/sensor/ti%2Cina230.md#std-dtcompatible-ti-ina230) |
| on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L453) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L464) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L472) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g071.dtsi?plain=1#L15)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L223) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g031.dtsi?plain=1#L14) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SMbus | on-chip | STM32 SMBus controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L479) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st%2Cstm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller with embedded Rx and Tx FIFOs[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L386) | [`st,stm32-spi-fifo`](../../../../build/dts/api/bindings/spi/st%2Cstm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L55) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| USB Type-C Port Controller | on-chip | STM32 USB Type-C / Power Delivery[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g071.dtsi?plain=1#L37)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g071.dtsi?plain=1#L45) | [`st,stm32-ucpd`](../../../../build/dts/api/bindings/tcpc/st%2Cstm32-ucpd.md#std-dtcompatible-st-stm32-ucpd) |
| Timer | on-chip | ARMv6-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21) | [`arm,armv6m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv6m-systick.md#std-dtcompatible-arm-armv6m-systick) |
| on-chip | STM32 low-power timer (LPTIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L241) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st%2Cstm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| on-chip | STM32 timers[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L252) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L209) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L215) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Connections and IOs

Each of the GPIO pins can be configured by software as output (push-pull or open-drain), as
input (with or without pull-up or pull-down), or as peripheral alternate function. Most of the
GPIO pins are shared with digital or analog alternate functions. All GPIOs are high current
capable except for analog inputs.

#### Default Zephyr Peripheral Mapping:

- UART\_3 TX/RX : PC10/PC11 (ST-Link Virtual Port Com)
- UCPD1 : PA8/PB15
- BUTTON (JOY\_SEL) : PC0
- BUTTON (JOY\_LEFT) : PC1
- BUTTON (JOY\_DOWN) : PC2
- BUTTON (JOY\_RIGHT) : PC3
- BUTTON (JOY\_UP) : PC4
- LED (TO\_REC) : PD9
- LED (TO\_PLUG) : PD8
- LED (SINK\_SPY) : PD5
- LED (SOURCE) : PC12
- ENCC1 : PB10 (Enable CC1)
- ENCC2 : PB11 (Enable CC2)
- RDCC1 : PB12 (Enable Door Sense on CC1)

For more details please refer to [STM32G0 Discovery board User Manual](https://www.st.com/resource/en/user_manual/dm00496511.pdf) [[3]](#id6).

## Programming and Debugging

The STM32G071B Discovery board includes an ST-LINK/V2-1 embedded debug tool interface.

Applications for the `stm32g071b_disco` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) [[5]](#id10) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

```shell
$ west flash
```

#### Flashing an application to the STM32G071B\_DISCO

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b stm32g071b_disco samples/basic/blinky
west flash
```

You will see the LED blinking every second.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b stm32g071b_disco samples/hello_world
west debug
```

## References

[[1](#id3)]

[https://www.st.com/en/evaluation-tools/stm32g071b-disco.html](https://www.st.com/en/evaluation-tools/stm32g071b-disco.html)

[[2](#id5)]

[https://www.st.com/resource/en/reference\_manual/dm00371828.pdf](https://www.st.com/resource/en/reference_manual/dm00371828.pdf)

[[3](#id7)]

[https://www.st.com/resource/en/user\_manual/dm00496511.pdf](https://www.st.com/resource/en/user_manual/dm00496511.pdf)

[[4](#id9)]

[https://www.st.com/en/microcontrollers/stm32g071rb.html](https://www.st.com/en/microcontrollers/stm32g071rb.html)

[[5](#id11)]

[https://www.st.com/en/development-tools/stm32cubeprog.html](https://www.st.com/en/development-tools/stm32cubeprog.html)

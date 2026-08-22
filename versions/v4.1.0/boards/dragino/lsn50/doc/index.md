---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/dragino/lsn50/doc/index.html
original_path: boards/dragino/lsn50/doc/index.html
---

# LSN50 LoRA Sensor Node

Board Overview

[![../../../../_images/dragino_lsn50.jpg](../../../../_images/dragino_lsn50.jpg)
](../../../../_images/dragino_lsn50.jpg)

LSN50 LoRA Sensor Node

Name:
:   `dragino_lsn50`

Vendor:
:   Dragino Technology Co., Limited

Architecture:
:   arm

SoC:
:   stm32l072xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/dragino/lsn50/doc/index.rst/../..)

## Overview

The Dragino LSN50 LoRA Sensor Node for IoT allows users to develop
applications with LoraWAN connectivity via the HopeRF / SX1276/SX1278.
Dragino LSN50 enables a wide diversity of applications by exploiting
low-power communication, ARM® Cortex®-M0 core-based
STM32L0 Series features.

This kit provides:

- STM32L072CZ MCU
- SX1276/SX1278 LoRa Transceiver
- Expansion connectors:

  > - PMOD
- Li/SOCI2 Unchargable Battery
- GPIOs exposed via screw terminals on the carrier board
- Housing

More information about the board can be found at the [Dragino LSN50 website](https://www.dragino.com/products/lora-lorawan-end-node/item/128-lsn50.html).

## Hardware

The STM32L072CZ SoC provides the following hardware IPs:

- Ultra-low-power (down to 0.29 µA Standby mode and 93 uA/MHz run mode)
- Core: ARM® 32-bit Cortex®-M0+ CPU, frequency up to 32 MHz
- Clock Sources:

  > - 1 to 32 MHz crystal oscillator
  > - 32 kHz crystal oscillator for RTC (LSE)
  > - Internal 16 MHz factory-trimmed RC ( ±1%)
  > - Internal low-power 37 kHz RC ( ±5%)
  > - Internal multispeed low-power 65 kHz to 4.2 MHz RC
- RTC with HW calendar, alarms and calibration
- Up to 24 capacitive sensing channels: support touchkey, linear and rotary touch sensors
- 11x timers:

  > - 2x 16-bit with up to 4 channels
  > - 2x 16-bit with up to 2 channels
  > - 1x 16-bit ultra-low-power timer
  > - 1x SysTick
  > - 1x RTC
  > - 2x 16-bit basic for DAC
  > - 2x watchdogs (independent/window)
- Up to 84 fast I/Os, most 5 V-tolerant.
- Memories

  > - Up to 192 KB Flash, 2 banks read-while-write, proprietary code readout protection
  > - Up to 20 KB of SRAM
  > - External memory interface for static memories supporting SRAM, PSRAM, NOR and NAND memories
- Rich analog peripherals (independent supply)

  > - 1x 12-bit ADC 1.14 MSPS
  > - 2x 12-bit DAC
  > - 2x ultra-low-power comparators
- 11x communication interfaces

  > - USB OTG 2.0 full-speed, LPM and BCD
  > - 3x I2C FM+(1 Mbit/s), SMBus/PMBus
  > - 4x USARTs (ISO 7816, LIN, IrDA, modem)
  > - 6x SPIs (4x SPIs with the Quad SPI)
- 7-channel DMA controller
- True random number generator
- CRC calculation unit, 96-bit unique ID
- Development support: serial wire debug (SWD), JTAG, Embedded Trace Macrocell™

More information about STM32L072CZ can be found here:

> - [STM32L072CZ on www.st.com](https://www.st.com/en/microcontrollers/stm32l072cz.html)
> - [STM32L0x2 reference manual](https://www.st.com/resource/en/reference_manual/DM00108281.pdf)

### Supported Features

The `dragino_lsn50` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `dragino_lsn50/stm32l072xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L29) | [`arm,cortex-m0+`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m0%2B.md#std-dtcompatible-arm-cortex-m0) |
| ADC | on-chip | STM32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L308) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32-adc.md#std-dtcompatible-st-stm32-adc) |
| Clock control | on-chip | STM32 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L129) | [`st,stm32-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32-rcc.md#std-dtcompatible-st-stm32-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L51) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L57)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L79) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32L0/L1 Multi Speed Internal Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L64) | [`st,stm32l0-msi-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32l0-msi-clock.md#std-dtcompatible-st-stm32l0-msi-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L71) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32L0/L1 Main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L86) | [`st,stm32l0-pll-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32l0-pll-clock.md#std-dtcompatible-st-stm32l0-pll-clock) |
| Counter | on-chip | STM32 counters[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L269) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st%2Cstm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l072.dtsi?plain=1#L54) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st%2Cstm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32 DMA controller (V2)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L325) | [`st,stm32-dma-v2`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dma-v2.md#std-dtcompatible-st-stm32-dma-v2) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L111) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO controller[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L158) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| I2C | on-chip | STM32 I2C V2 controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L231) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L140) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32-exti.md#std-dtcompatible-st-stm32-exti) |
| Memory controller | on-chip | STM32 Battery Backed RAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L104) | [`st,stm32-bbram`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32-bbram.md#std-dtcompatible-st-stm32-bbram) |
| MTD | on-chip | STM32L0 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L119) | [`st,stm32l0-nv-flash`](../../../../build/dts/api/bindings/mtd/st%2Cstm32l0-nv-flash.md#std-dtcompatible-st-stm32l0-nv-flash) |
| on-chip | STM32 on-chip EEPROM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L334) | [`st,stm32-eeprom`](../../../../build/dts/api/bindings/mtd/st%2Cstm32-eeprom.md#std-dtcompatible-st-stm32-eeprom) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l072.dtsi?plain=1#L49) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L152) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L263) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L134) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l072.dtsi?plain=1#L40) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st%2Cstm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L94) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st%2Cstm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L340) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L351) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vref.md#std-dtcompatible-st-stm32-vref) |
| Serial controller | on-chip | STM32 USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L213)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l071.dtsi?plain=1#L142) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L222) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SMbus | on-chip | STM32 SMBus controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L359) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st%2Cstm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L243) | [`st,stm32-spi`](../../../../build/dts/api/bindings/spi/st%2Cstm32-spi.md#std-dtcompatible-st-stm32-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L46) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv6-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21) | [`arm,armv6m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv6m-systick.md#std-dtcompatible-arm-armv6m-systick) |
| on-chip | STM32 timers[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L253) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers) |
| on-chip | STM32 low-power timer (LPTIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L297) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st%2Cstm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| USB | on-chip | STM32 USB controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l072.dtsi?plain=1#L26) | [`st,stm32-usb`](../../../../build/dts/api/bindings/usb/st%2Cstm32-usb.md#std-dtcompatible-st-stm32-usb) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L199) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l0/stm32l0.dtsi?plain=1#L205) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Connections and IOs

Dragino LSN50 Board has GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

#### Available pins:

For detailed information about available pins please refer to [Dragino LSN50 website](https://www.dragino.com/products/lora-lorawan-end-node/item/128-lsn50.html).

#### Default Zephyr Peripheral Mapping:

- UART\_1\_TX : PB6
- UART\_1\_RX : PB7
- UART\_2\_TX : PA2
- UART\_2\_RX : PA3

#### System Clock

Dragino LSN50 System Clock is at 32MHz,

#### Serial Port

Dragino LSN50 board has 2 U(S)ARTs. The Zephyr console output is assigned to UART1.
Default settings are 115200 8N1.

## Programming and Debugging

Applications for the `dragino_lsn50` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

Dragino LSN50 board requires an external debugger.

#### Flashing an application to Dragino LSN50

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Connect the Dragino LSN50 to a STLinkV2 to your host computer using the USB port, then
run a serial host program to connect with your board. For example:

```shell
$ minicom -D /dev/ttyACM0
```

Then build and flash the application:

```shell
# From the root of the zephyr repository
west build -b dragino_lsn50 samples/hello_world
west flash
```

You should see the following message on the console:

```shell
$ Hello World! arm
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b dragino_lsn50 samples/hello_world
west debug
```

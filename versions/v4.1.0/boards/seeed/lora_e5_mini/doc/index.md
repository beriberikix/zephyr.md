---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/seeed/lora_e5_mini/doc/index.html
original_path: boards/seeed/lora_e5_mini/doc/index.html
---

# LoRa-E5 mini

Board Overview

[![../../../../_images/lora_e5_mini.jpg](../../../../_images/lora_e5_mini.jpg)
](../../../../_images/lora_e5_mini.jpg)

LoRa-E5 mini

Name:
:   `lora_e5_mini`

Vendor:
:   Seeed Technology Co., Ltd

Architecture:
:   arm

SoC:
:   stm32wle5xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/seeed/lora_e5_mini/doc/index.rst/../..)

## Overview

LoRa-E5 mini is a compacted-sized development board suitable for the rapid
testing and building of small-sized LoRa device, exposing all capabilities of
Seeed Studio LoRa-E5 STM32WLE5JC module.

## Hardware

The boards’ LoRa-E5 Module packages a STM32WLE5JC SOC, a 32MHz TCXO,
and a 32.768kHz crystal oscillator in a 28-pin SMD package.
This STM32WLEJC SOC is powered by ARM Cortex-M4 core and integrates Semtech
SX126X LoRa IP to support (G)FSK, BPSK, (G)MSK, and LoRa modulations.

- LoRa-E5 STM32WLE5JC Module with STM32WLE5JC multiprotocol LPWAN single-core
  32-bit microcontroller (Arm® Cortex®-M4 at 48 MHz) in 28-pin SMD package
  featuring:

  - Ultra-low-power MCU
  - RF transceiver (150 MHz to 960 MHz frequency range) supporting LoRa®,
    (G)FSK, (G)MSK, and BPSK modulations
  - 256-Kbyte Flash memory and 64-Kbyte SRAM
  - Hardware encryption AES256-bit and a True random number generator
- 1 user LED
- 2 serial communication (RX/TX) LEDs
- 1 boot/user and 1 reset push-button
- 32.768 kHz LSE crystal oscillator
- 32 MHz HSE oscillator
- Board connectors:

  - USB Type-C connector
  - +/- (battery) power input pins (3-5V)
  - SMA-K and IPEX antenna connectors
- Delivered with SMA antenna (per default IPEX connector is disconnected)
- Flexible power-supply options: USB Type C or 3-5V battery soldered to +/- pins
- Suitable for rapid prototyping of end nodes based on LoRaWAN, Sigfox, wM-Bus,
  and many other proprietary protocols
- All GPIOs led out from the LoRa-E5 STM32WLE5JC module
- 4x M2 mounting holes

More information about the board can be found at the [LoRa-E5 mini Wiki](https://wiki.seeedstudio.com/LoRa_E5_mini/).

More information about LoRa-E5 STM32WLE5JC Module can be found here:

- [LoRa-E5 STM32WLE5JC Module Wiki](https://wiki.seeedstudio.com/LoRa-E5_STM32WLE5JC_Module/)
- [LoRa-E5 STM32WLE5JC Module datasheet](https://files.seeedstudio.com/products/317990687/res/LoRa-E5%20module%20datasheet_V1.0.pdf)
- [STM32WLE5JC datasheet](https://www.st.com/resource/en/datasheet/stm32wle5jc.pdf)
- [STM32WLE5JC reference manual](https://www.st.com/resource/en/reference_manual/dm00530369-stm32wlex-advanced-armbased-32bit-mcus-with-subghz-radio-solution-stmicroelectronics.pdf)
- [STM32WLE5JC on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32wle5jc.html)

### Supported Features

The `lora_e5_mini` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `lora_e5_mini/stm32wle5xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L31) | [`arm,cortex-m4`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4.md#std-dtcompatible-arm-cortex-m4) |
| ADC | on-chip | STM32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L344) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32-adc.md#std-dtcompatible-st-stm32-adc) |
| Clock control | on-chip | STM32WL RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L128) | [`st,stm32wl-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32wl-rcc.md#std-dtcompatible-st-stm32wl-rcc) |
| on-chip | STM32WL HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L65) | [`st,stm32wl-hse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32wl-hse-clock.md#std-dtcompatible-st-stm32wl-hse-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L95)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L73) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 MSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L80) | [`st,stm32-msi-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-msi-clock.md#std-dtcompatible-st-stm32-msi-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L87) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32WB and STM32WL PLL node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L102) | [`st,stm32wb-pll-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32wb-pll-clock.md#std-dtcompatible-st-stm32wb-pll-clock) |
| Counter | on-chip | STM32 counters[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L402) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st%2Cstm32-counter.md#std-dtcompatible-st-stm32-counter) |
| Cryptographic accelerator | on-chip | STM32 AES Accelerator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L452) | [`st,stm32-aes`](../../../../build/dts/api/bindings/crypto/st%2Cstm32-aes.md#std-dtcompatible-st-stm32-aes) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L361) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st%2Cstm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32 DMA controller (V2)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L471) | [`st,stm32-dma-v2`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dma-v2.md#std-dtcompatible-st-stm32-dma-v2) |
| on-chip | STM32 DMAMUX controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L493) | [`st,stm32-dmamux`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dmamux.md#std-dtcompatible-st-stm32-dmamux) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L110) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L160) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| I2C | on-chip | STM32 I2C V2 controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L281)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L269) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seeed/lora_e5_mini/lora_e5_mini.dts?plain=1#L31) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L139) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seeed/lora_e5_mini/lora_e5_mini.dts?plain=1#L23) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| LoRa | on-chip | STM32WL Sub-GHz Radio[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L335) | [`st,stm32wl-subghz-radio`](../../../../build/dts/api/bindings/lora/st%2Cstm32wl-subghz-radio.md#std-dtcompatible-st-stm32wl-subghz-radio) |
| Memory controller | on-chip | STM32 Battery Backed RAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L220) | [`st,stm32-bbram`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32-bbram.md#std-dtcompatible-st-stm32-bbram) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L118) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st%2Cstm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seeed/lora_e5_mini/lora_e5_mini.dts?plain=1#L101) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L154) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| Power management | on-chip | STM32 power controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L505) | [`st,stm32-pwr`](../../../../build/dts/api/bindings/power/st%2Cstm32-pwr.md#std-dtcompatible-st-stm32-pwr) |
| PWM | on-chip | STM32 PWM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L379) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L133) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L461) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st%2Cstm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L204) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st%2Cstm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L534) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L545) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L553) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L241)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L250) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L259) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SMbus | on-chip | STM32 SMBus controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L560) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st%2Cstm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller with embedded Rx and Tx FIFOs[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L305) | [`st,stm32-spi-fifo`](../../../../build/dts/api/bindings/spi/st%2Cstm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) |
| on-chip | STM32 SUBGHZ SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L325) | [`st,stm32-spi-subghz`](../../../../build/dts/api/bindings/spi/st%2Cstm32-spi-subghz.md#std-dtcompatible-st-stm32-spi-subghz) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L60) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 low-power timer (LPTIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L193) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st%2Cstm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| on-chip | STM32 timers[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L369) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L227) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L233) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Connections and IOs

LoRa-E5 mini has 4 GPIO controllers. These controllers are responsible for pin
muxing, input/output, pull-up, etc.

#### Available pins:

![LoRa-E5 mini Pinout](../../../../_images/lora_e5_mini_pinout.jpg)

#### Default Zephyr Peripheral Mapping:

- USART\_1 TX : PB6
- USART\_1 RX : PB7
- I2C\_2\_SCL : PB15
- I2C\_2\_SDA : PA15
- BOOT\_PB : PB13
- LED\_1 : PB5

#### System Clock

LoRa-E5 mini board System Clock could be driven by the low-power internal (MSI),
High-speed internal (HSI) or High-speed external (HSE) oscillator, as well as
main PLL clock. By default System clock is driven by the MSI clock at 48MHz.

## Programming and Debugging

Applications for the `lora_e5_mini` board configuration can be built the
usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)).

In the factory the module is flashed with an DFU bootloader, an AT command
firmware, and the read protection level 1 is enabled.
So before you can program a Zephyr application to the module for the first time
you have to reset the read protection to level 0.
In case you use an st-link debugger you can use the STM32CubeProgrammer GUI to
set the RDP option byte to `AA`,
or use the STM32\_Programmer\_CLI passing the `--readunprotect` command
to perform this read protection regression.
The RDP level 1 to RDP level 0 regression will erase the factory programmed AT
firmware, from which seeed studio has neither released the source code nor a binary.
Also, note that on the module the `BOOT0` pin of the SOC is not accessible,
so the system bootloader will only be executed if configured in the option bytes.

### Flashing

The LoRa-E5 mini does not include a on-board debug probe.
But the module can be debugged by connecting an external debug probe to the
2.54mm header.
Depending on the external probe used, `openocd`, the `stm32cubeprogrammer`,
`pyocd`, `blackmagic`, or `jlink` runner can be used to flash the board.
Additional notes:

- Pyocd: For STM32WL support Pyocd needs additional target information, which
  can be installed by adding “pack” support with the following pyocd command:

```shell
$ pyocd pack --update
$ pyocd pack --install stm32wl
```

#### Flashing an application to LoRa-E5 mini

Connect the LoRa-E5 to your host computer using the external debug probe.
Then build and flash an application. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Run a serial host program to connect with your board:
Per default the console on `usart1` is available on the USB Type C connector
via the built-in USB to UART converter.

```shell
$ picocom --baud 115200 /dev/ttyACM0
```

Then build and flash the application.

```shell
# From the root of the zephyr repository
west build -b lora_e5_mini samples/hello_world
west flash
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b lora_e5_mini samples/basic/blinky
west debug
```

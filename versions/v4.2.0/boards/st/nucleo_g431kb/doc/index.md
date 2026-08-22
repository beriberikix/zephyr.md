---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/st/nucleo_g431kb/doc/index.html
original_path: boards/st/nucleo_g431kb/doc/index.html
---

# Nucleo G431KB

Board Overview

[![../../../../_images/nucleo_g431kb.webp](../../../../_images/nucleo_g431kb.webp)
](../../../../_images/nucleo_g431kb.webp)

Nucleo G431KB

Name:
:   `nucleo_g431kb`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32g431xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_g431kb/doc/index.rst/../..)

## Overview

The Nucleo G431KB board features an ARM Cortex-M4 based STM32G431KB MCU
with a wide range of connectivity support and configurations.
Here are some highlights of the Nucleo G431KB board:

- STM32 microcontroller in LQFP32 package
- Arduino Nano V3 connectivity
- On-board ST-LINK/V3E debugger/programmer
- Flexible board power supply:

  - USB VBUS or external source(3.3 V, 5 V, 7 - 12 V)
  - Power management access point
- Three LEDs: USB communication (LD1), power LED (LD3), user LED (LD2)
- One push-button for RESET

More information about the board can be found at the [Nucleo G431KB website](https://www.st.com/en/evaluation-tools/nucleo-g431kb.html) [[1]](#id2).

- Development support: serial wire debug (SWD), JTAG, Embedded Trace Macrocell.

More information about STM32G431KB can be found here:

- [STM32G431KB on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32g431kb.html) [[3]](#id6)
- [STM32G4 reference manual](https://www.st.com/resource/en/reference_manual/rm0440-stm32g4-series-advanced-armbased-32bit-mcus-stmicroelectronics.pdf) [[4]](#id8)

### Supported Features

The `nucleo_g431kb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `nucleo_g431kb/stm32g431xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L32) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | STM32 ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L106) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32-adc.md#std-dtcompatible-st-stm32-adc) |
| CAN | on-chip | STM32 FDCAN CAN FD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L388) | [`st,stm32-fdcan`](../../../../build/dts/api/bindings/can/st%2Cstm32-fdcan.md#std-dtcompatible-st-stm32-fdcan) |
| Clock control | on-chip | STM32 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L173) | [`st,stm32-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32-rcc.md#std-dtcompatible-st-stm32-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L60) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L66)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L73) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L80) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32G4 main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L95) | [`st,stm32g4-pll-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32g4-pll-clock.md#std-dtcompatible-st-stm32g4-pll-clock) |
| Counter | on-chip | STM32 counters[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L437) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st%2Cstm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DAC | on-chip | STM32 family DAC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L138) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st%2Cstm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32 DMA controller (V2)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L631) | [`st,stm32-dma-v2`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dma-v2.md#std-dtcompatible-st-stm32-dma-v2) |
| on-chip | STM32 DMAMUX controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L648) | [`st,stm32-dmamux`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dmamux.md#std-dtcompatible-st-stm32-dmamux) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L154) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO Controller[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L206) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| I2C | on-chip | STM32 I2C V2 controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L334)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L322) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L185) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_g431kb/nucleo_g431kb.dts?plain=1#L22) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_g431kb/nucleo_g431kb.dts?plain=1#L32) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L163) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st%2Cstm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_g431kb/nucleo_g431kb.dts?plain=1#L106) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L694) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L200) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L486)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L420) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L179) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L609) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st%2Cstm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L598) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st%2Cstm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L668) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L679) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L687) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L263) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L290) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-uart.md#std-dtcompatible-st-stm32-uart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L299) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SMbus | on-chip | STM32 SMBus controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L699) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st%2Cstm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller with embedded Rx and Tx FIFOs[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L358) | [`st,stm32-spi-fifo`](../../../../build/dts/api/bindings/spi/st%2Cstm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L55) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| USB Type-C Port Controller | on-chip | STM32 USB Type-C / Power Delivery[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L659) | [`st,stm32-ucpd`](../../../../build/dts/api/bindings/tcpc/st%2Cstm32-ucpd.md#std-dtcompatible-st-stm32-ucpd) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 low-power timer (LPTIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L399) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st%2Cstm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| on-chip | STM32 timers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L471)[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L410) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers) |
| USB | on-chip | STM32 USB controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L617) | [`st,stm32-usb`](../../../../build/dts/api/bindings/usb/st%2Cstm32-usb.md#std-dtcompatible-st-stm32-usb) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L308) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L314) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Connections and IOs

Nucleo G431KB Board has 6 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

For more details please refer to [STM32G4 Nucleo-32 board User Manual](https://www.st.com/resource/en/user_manual/um2397-stm32g4-nucleo32-board-mb1430-stmicroelectronics.pdf) [[2]](#id4).

#### Default Zephyr Peripheral Mapping:

- LPUART\_1\_TX : PA2
- LPUART\_1\_RX : PA3
- LD2 : PB8
- PWM\_4\_CH\_3 : PB8
- I2C\_2\_SCL : PA9
- I2C\_2\_SDA : PA8

#### System Clock

The Nucleo G431KB System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default the external oscillator is not connected to the board. Therefore only the internal
High Speed oscillator is supported. By default System clock is driven by PLL clock at 170 MHz,
the PLL is driven by the 16 MHz high speed internal oscillator.

#### Serial Port

Nucleo G431KB board has 1 U(S)ARTs and one LPUART. The Zephyr console output is assigned to LPUART1.
Default settings are 115200 8N1.

Please note that LPUART1 baudrate is limited to 9600 if the MCU is clocked by LSE (32.768 kHz) in
low power mode.

## Programming and Debugging

The `nucleo_g431kb` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |
| **[stm32cubeprogrammer](../../../../develop/flash_debug/host-tools.md#runner-stm32cubeprogrammer)** | ✅ (default) |  |  |  |  |

Nucleo G431KB Board includes an ST-Link/V3 embedded debug tool interface.

Applications for the `nucleo_g431kb` board target can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) [[5]](#id10) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD, or pyOCD can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner pyocd
```

To enable support of the STM32G431KB SoC in pyOCD, its pack has to be installed first:

```shell
$ pyocd pack --update
$ pyocd pack --install stm32g431kb
```

#### Flashing an application to Nucleo G431KB

Connect the Nucleo G431KB to your host computer using the USB port,
then run a serial host program to connect with your Nucleo board.

```shell
$ minicom -D /dev/ttyACM0
```

Now build and flash an application. Here is an example for
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.").

```shell
# From the root of the zephyr repository
west build -b nucleo_g431kb samples/hello_world
west flash
```

You should see the following message on the console:

```shell
$ Hello World! nucleo_g431kb/stm32g431xx
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_g431kb samples/hello_world
west debug
```

## References

[[1](#id3)]

[https://www.st.com/en/evaluation-tools/nucleo-g431kb.html](https://www.st.com/en/evaluation-tools/nucleo-g431kb.html)

[[2](#id5)]

[https://www.st.com/resource/en/user\_manual/um2397-stm32g4-nucleo32-board-mb1430-stmicroelectronics.pdf](https://www.st.com/resource/en/user_manual/um2397-stm32g4-nucleo32-board-mb1430-stmicroelectronics.pdf)

[[3](#id7)]

[https://www.st.com/en/microcontrollers-microprocessors/stm32g431kb.html](https://www.st.com/en/microcontrollers-microprocessors/stm32g431kb.html)

[[4](#id9)]

[https://www.st.com/resource/en/reference\_manual/rm0440-stm32g4-series-advanced-armbased-32bit-mcus-stmicroelectronics.pdf](https://www.st.com/resource/en/reference_manual/rm0440-stm32g4-series-advanced-armbased-32bit-mcus-stmicroelectronics.pdf)

[[5](#id11)]

[https://www.st.com/en/development-tools/stm32cubeprog.html](https://www.st.com/en/development-tools/stm32cubeprog.html)

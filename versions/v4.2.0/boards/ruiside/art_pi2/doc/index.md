---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/ruiside/art_pi2/doc/index.html
original_path: boards/ruiside/art_pi2/doc/index.html
---

# ART-Pi2

Board Overview

[![../../../../_images/art_pi2.webp](../../../../_images/art_pi2.webp)
](../../../../_images/art_pi2.webp)

ART-Pi2

Name:
:   `art_pi2`

Vendor:
:   Shanghai Ruiside Electronic Technology Co., Ltd.

Architecture:
:   arm

SoC:
:   stm32h7r7xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ruiside/art_pi2/doc/index.rst/../..)

## Overview

The ART-Pi2 is an open-source hardware platform designed by the
RT-Thread team specifically for embedded software engineers
and open-source makers, offering extensive expandability for DIY projects.

Key Features

- STM32H7R7L8HxH microcontroller featuring 64 Kbytes of Flash and 620 Kbytes of SRAM in an TFBGA225 package
- On-board ST-LINK/V2.1 debugger/programmer
- SDIO TF Card slot
- SDIO WIFI:CYWL6208
- HDC UART BuleTooth:CYWL6208
- 32-MB HyperRAM
- 64-MB HyperFlash
- One Power LED (blue) for 3.3 V power-on
- Two user LEDs blue and red
- Two ST-LINK LEDs: blue and red
- Two push-buttons (user and reset)
- Board connectors:

  - USB OTG with Type-C connector
  - RGB888 FPC connector

More information about the board can be found at the [ART-Pi2 website](https://github.com/RT-Thread-Studio/sdk-bsp-stm32h7r-realthread-artpi2) [[1]](#id2).

## Hardware

ART-Pi2 provides the following hardware components:

The STM32H7R7xx devices are a high-performance microcontrollers family (STM32H7
Series) based on the high-performance Arm® Cortex®-M7 32-bit RISC core.
They operate at a frequency of up to 600 MHz.

More information about STM32H7R7 can be found here:

- [STM32H7R7L8 on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32h7r7l8.html) [[2]](#id4)
- [STM32H7Rx reference manual](https://www.st.com/resource/en/reference_manual/rm0477-stm32h7rx7sx-armbased-32bit-mcus-stmicroelectronics.pdf) [[3]](#id6)

### Supported Features

The `art_pi2` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `art_pi2/stm32h7r7xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L35) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ADC | on-chip | STM32 ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L764) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32-adc.md#std-dtcompatible-st-stm32-adc) |
| Clock control | on-chip | STM32H7RS RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L195) | [`st,stm32h7rs-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32h7rs-rcc.md#std-dtcompatible-st-stm32h7rs-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L93) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | STM32 HSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L99) | [`st,stm32h7-hsi-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32h7-hsi-clock.md#std-dtcompatible-st-stm32h7-hsi-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L107)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L114) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L121) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32H7RS main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L136)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L143) | [`st,stm32h7rs-pll-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32h7rs-pll-clock.md#std-dtcompatible-st-stm32h7rs-pll-clock) |
| on-chip | STM32 Clock multiplexer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L157) | [`st,stm32-clock-mux`](../../../../build/dts/api/bindings/clock/st%2Cstm32-clock-mux.md#std-dtcompatible-st-stm32-clock-mux) |
| on-chip | STM32 Microcontroller Clock Output (MCO)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L165) | [`st,stm32-clock-mco`](../../../../build/dts/api/bindings/clock/st%2Cstm32-clock-mco.md#std-dtcompatible-st-stm32-clock-mco) |
| Counter | on-chip | STM32 counters[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L567) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st%2Cstm32-counter.md#std-dtcompatible-st-stm32-counter) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L177) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO Controller[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L234) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| I2C | on-chip | STM32 I2C V2 controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L397) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| I2S | on-chip | STM32H7 I2S controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L486) | [`st,stm32h7-i2s`](../../../../build/dts/api/bindings/i2s/st%2Cstm32h7-i2s.md#std-dtcompatible-st-stm32h7-i2s) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ruiside/art_pi2/art_pi2.dts?plain=1#L37) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32H7RS External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L206) | [`st,stm32h7rs-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32h7rs-exti.md#std-dtcompatible-st-stm32h7rs-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ruiside/art_pi2/art_pi2.dts?plain=1#L23) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L42) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L186) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st%2Cstm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L819) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L228) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L544) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L200) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L796) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st%2Cstm32-rng.md#std-dtcompatible-st-stm32-rng) |
| Sensors | on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L824) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L836) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L843) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vref.md#std-dtcompatible-st-stm32-vref) |
| Serial controller | on-chip | STM32 USART[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L331) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L355)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L363) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-uart.md#std-dtcompatible-st-stm32-uart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L388) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SPI | on-chip | STM32H7 SPI controller[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L433) | [`st,stm32h7-spi`](../../../../build/dts/api/bindings/spi/st%2Cstm32h7-spi.md#std-dtcompatible-st-stm32h7-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L50) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 timers[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L534) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers) |
| on-chip | STM32 low-power timer (LPTIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L753) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st%2Cstm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| USB | on-chip | STM32 OTGFS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L804) | [`st,stm32-otgfs`](../../../../build/dts/api/bindings/usb/st%2Cstm32-otgfs.md#std-dtcompatible-st-stm32-otgfs) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L519) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L526) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |
| xSPI | on-chip | STM32 XSPI Controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L497) | [`st,stm32-xspi`](../../../../build/dts/api/bindings/xspi/st%2Cstm32-xspi.md#std-dtcompatible-st-stm32-xspi) |

#### Default Zephyr Peripheral Mapping:

The ART-Pi2 board features a On-board ST-LINK/V2.1 debugger/programmer. Board is configured as follows:

- UART4 TX/RX : PD1/PD0 (ST-Link Virtual Port Com)
- LED1 (red) : PO1
- LED2 (blue) : PO5
- USER PUSH-BUTTON : PC13

#### System Clock

ART-Pi2 System Clock could be driven by an internal or external
oscillator, as well as the main PLL clock. By default, the System clock is
driven by the PLL clock at 250MHz, driven by an 24MHz high-speed external clock.

#### Serial Port

ART-Pi2 board has 4 UARTs and 3 USARTs plus one LowPower UART. The Zephyr console
output is assigned to UART4. Default settings are 115200 8N1.

#### Backup SRAM

In order to test backup SRAM you may want to disconnect VBAT from VDD. You can
do it by removing `SB13` jumper on the back side of the board.

## Programming and Debugging

The `art_pi2` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |
| **[stm32cubeprogrammer](../../../../develop/flash_debug/host-tools.md#runner-stm32cubeprogrammer)** | ✅ (default) |  |  |  |  |

ART-Pi2 board includes an ST-LINK/V2.1 embedded debug tool interface.

Note

Check if your ST-LINK V2.1 has newest FW version. It can be done with [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) [[4]](#id8)

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) [[4]](#id8) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

#### Flashing an application to ART-Pi2

First, connect the art\_pi2 to your host computer using
the USB port to prepare it for flashing. Then build and flash your application.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Run a serial host program to connect with your art\_pi2 board.

```shell
$ minicom -b 115200 -D /dev/ttyACM0
```

or use screen:

```shell
$ screen /dev/ttyACM0 115200
```

Build and flash the application:

```shell
# From the root of the zephyr repository
west build -b art_pi2 samples/hello_world
west flash
```

You should see the following message on the console:

```shell
*** Booting Zephyr OS build v4.1.0-1907-g415ab379a8af ***
Hello World! art_pi2/stm32h7r7xx
```

Blinky example can also be used:

```shell
# From the root of the zephyr repository
west build -b art_pi2 samples/basic/blinky
west flash
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b art_pi2 samples/hello_world
west debug
```

## References

[[1](#id3)]

[https://github.com/RT-Thread-Studio/sdk-bsp-stm32h7r-realthread-artpi2](https://github.com/RT-Thread-Studio/sdk-bsp-stm32h7r-realthread-artpi2)

[[2](#id5)]

[https://www.st.com/en/microcontrollers-microprocessors/stm32h7r7l8.html](https://www.st.com/en/microcontrollers-microprocessors/stm32h7r7l8.html)

[[3](#id7)]

[https://www.st.com/resource/en/reference\_manual/rm0477-stm32h7rx7sx-armbased-32bit-mcus-stmicroelectronics.pdf](https://www.st.com/resource/en/reference_manual/rm0477-stm32h7rx7sx-armbased-32bit-mcus-stmicroelectronics.pdf)

[4]
([1](#id9),[2](#id10))

[https://www.st.com/en/development-tools/stm32cubeprog.html](https://www.st.com/en/development-tools/stm32cubeprog.html)

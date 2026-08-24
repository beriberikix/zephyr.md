---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/makerbase/mks_canable_v20/doc/index.html
original_path: boards/makerbase/mks_canable_v20/doc/index.html
---

# MKS CANable V2.0

Board Overview

[![../../../../_images/mks_canable_v20.webp](https://docs.zephyrproject.org/4.2.0/_images/mks_canable_v20.webp)
](https://docs.zephyrproject.org/4.2.0/_images/mks_canable_v20.webp)

MKS CANable V2.0

Name:
:   `mks_canable_v20`

Vendor:
:   Makerbase Co., Ltd.

Architecture:
:   arm

SoC:
:   stm32g431xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/makerbase/mks_canable_v20/doc/index.rst/../..)

## Overview

The Makerbase MKS CANable V2.0 board features an ARM Cortex-M4 based STM32G431C8 MCU
with a CAN, USB and debugger connections.
Here are some highlights of the MKS CANable V2.0 board:

- STM32 microcontroller in LQFP48 package
- USB Type-C connector (J1)
- CAN-Bus connector (J2)
- ST-LINK/V3E debugger/programmer header (J4)
- USB VBUS power supply (5 V)
- Three LEDs: red/power\_led (D1), blue/stat\_led (D2), green/word\_led (D3)
- One push-button for RESET
- Development support: serial wire debug (SWD), JTAG, Embedded Trace Macrocell.

The LED red/power\_led (D1) is connected directly to on-board 3.3 V and not controllable by the MCU.

More information about the board can be found at the [MKS CANable V2.0 website](https://github.com/makerbase-mks/CANable-MKS) [[1]](#id2).
It is very advisable to take a look in on user manual [MKS CANable V2.0 User Manual](https://github.com/makerbase-mks/CANable-MKS/blob/main/User%20Manual/CANable%20V2.0/Makerbase%20CANable%20V2.0%20Use%20Manual.pdf) [[2]](#id4) and
schematic [MKS CANable V2.0 schematic](https://github.com/makerbase-mks/CANable-MKS/blob/main/Hardware/MKS%20CANable%20V2.0/MKS%20CANable%20V2.0_001%20schematic.pdf) [[3]](#id6) before start.

More information about STM32G431KB can be found here:

- [STM32G431C8 on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32g431c8.html) [[4]](#id10)
- [STM32G4 reference manual](https://www.st.com/resource/en/reference_manual/rm0440-stm32g4-series-advanced-armbased-32bit-mcus-stmicroelectronics.pdf) [[5]](#id12)

### Supported Features

The `mks_canable_v20` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `mks_canable_v20/stm32g431xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L32) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | STM32 ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L106) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32-adc.md#std-dtcompatible-st-stm32-adc) |
| CAN | on-chip | STM32 FDCAN CAN FD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L388) | [`st,stm32-fdcan`](../../../../build/dts/api/bindings/can/st%2Cstm32-fdcan.md#std-dtcompatible-st-stm32-fdcan) |
| Clock control | on-chip | STM32 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L173) | [`st,stm32-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32-rcc.md#std-dtcompatible-st-stm32-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L60) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L66)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L88) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L80) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32G4 main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L95) | [`st,stm32g4-pll-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32g4-pll-clock.md#std-dtcompatible-st-stm32g4-pll-clock) |
| Counter | on-chip | STM32 counters[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L437) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st%2Cstm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DAC | on-chip | STM32 family DAC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L138) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st%2Cstm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32 DMA controller (V2)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L631) | [`st,stm32-dma-v2`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dma-v2.md#std-dtcompatible-st-stm32-dma-v2) |
| on-chip | STM32 DMAMUX controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L648) | [`st,stm32-dmamux`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dmamux.md#std-dtcompatible-st-stm32-dmamux) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L154) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO Controller[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L206) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| I2C | on-chip | STM32 I2C V2 controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L322) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L185) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/makerbase/mks_canable_v20/mks_canable_v20.dts?plain=1#L25) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L163) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st%2Cstm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L694) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L200) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L420) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
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
| on-chip | STM32 timers[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L410) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers) |
| USB | on-chip | STM32 USB controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L617) | [`st,stm32-usb`](../../../../build/dts/api/bindings/usb/st%2Cstm32-usb.md#std-dtcompatible-st-stm32-usb) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L308) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L314) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Connections and IOs

#### Default Zephyr Peripheral Mapping:

- CAN\_RX/BOOT0 : PB8
- CAN\_TX : PB9
- D2 : PA15
- D3 : PA0
- USB\_DN : PA11
- USB\_DP : PA12
- SWDIO : PA13
- SWCLK : PA14
- NRST : PG10

For more details please refer to [MKS CANable V2.0 schematic](https://github.com/makerbase-mks/CANable-MKS/blob/main/Hardware/MKS%20CANable%20V2.0/MKS%20CANable%20V2.0_001%20schematic.pdf) [[3]](#id6).

#### System Clock

The MKS CANable V2.0 system clock is driven by internal high speed oscillator.
By default system clock is driven by PLL clock at 160 MHz,
the PLL is driven by the 16 MHz high speed internal oscillator.

The FDCAN1 peripheral is driven by PLLQ, which has 80 MHz frequency.

## Programming and Debugging

The `mks_canable_v20` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

MKS CANable V2.0 board includes an SWDIO debug connector header J4.

Note

The debugger is not the part of the board!

Applications for the `mks_canable_v20` board target can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board could be flashed using west.

#### Flashing an application to MKS CANable V2.0

The debugger shall be wired to MKS CANable V2.0 board’s J4 connector
according [MKS CANable V2.0 schematic](https://github.com/makerbase-mks/CANable-MKS/blob/main/Hardware/MKS%20CANable%20V2.0/MKS%20CANable%20V2.0_001%20schematic.pdf) [[3]](#id6).

Build and flash an application. Here is an example for
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.").

```shell
west build -b mks_canable_v20 -S rtt-console samples/hello_world
west flash
```

The argument `-S rtt-console` is needed for debug purposes with SEGGER RTT protocol.
This option is optional and may be omitted. Omitting it frees up RAM space but prevents RTT usage.

If option `-S rtt-console` is selected, the connection to the target can be established as follows:

```shell
$ telnet localhost 9090
```

You should see the following message on the console:

```shell
$ Hello World! mks_canable_v20/stm32g431xx
```

Note

Current OpenOCD config will skip Segger RTT for OpenOCD under 0.12.0.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b mks_canable_v20 samples/hello_world
west debug
```

## References

[[1](#id3)]

[https://github.com/makerbase-mks/CANable-MKS](https://github.com/makerbase-mks/CANable-MKS)

[[2](#id5)]

[https://github.com/makerbase-mks/CANable-MKS/blob/main/User%20Manual/CANable%20V2.0/Makerbase%20CANable%20V2.0%20Use%20Manual.pdf](https://github.com/makerbase-mks/CANable-MKS/blob/main/User%20Manual/CANable%20V2.0/Makerbase%20CANable%20V2.0%20Use%20Manual.pdf)

[3]
([1](#id7),[2](#id8),[3](#id9))

[https://github.com/makerbase-mks/CANable-MKS/blob/main/Hardware/MKS%20CANable%20V2.0/MKS%20CANable%20V2.0\_001%20schematic.pdf](https://github.com/makerbase-mks/CANable-MKS/blob/main/Hardware/MKS%20CANable%20V2.0/MKS%20CANable%20V2.0_001%20schematic.pdf)

[[4](#id11)]

[https://www.st.com/en/microcontrollers-microprocessors/stm32g431c8.html](https://www.st.com/en/microcontrollers-microprocessors/stm32g431c8.html)

[[5](#id13)]

[https://www.st.com/resource/en/reference\_manual/rm0440-stm32g4-series-advanced-armbased-32bit-mcus-stmicroelectronics.pdf](https://www.st.com/resource/en/reference_manual/rm0440-stm32g4-series-advanced-armbased-32bit-mcus-stmicroelectronics.pdf)

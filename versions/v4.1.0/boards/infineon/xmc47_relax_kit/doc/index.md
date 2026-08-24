---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/infineon/xmc47_relax_kit/doc/index.html
original_path: boards/infineon/xmc47_relax_kit/doc/index.html
---

# XMC47-RELAX-KIT

Board Overview

[![../../../../_images/xmc47_relax_kit.jpg](https://docs.zephyrproject.org/4.1.0/_images/xmc47_relax_kit.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/xmc47_relax_kit.jpg)

XMC47-RELAX-KIT

Name:
:   `xmc47_relax_kit`

Vendor:
:   Infineon Technologies

Architecture:
:   arm

SoC:
:   xmc4700

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/infineon/xmc47_relax_kit/doc/index.rst/../..)

## Overview

The XMC4700 Relax Kit is designed to evaluate the capabilities of the XMC4700
Microcontroller. It is based on High performance ARM Cortex-M4F which can run
up to 144MHz.

### Features:

- ARM Cortex-M4F XMC4700
- On-board Debug Probe with USB interface supporting SWD + SWO
- Virtual COM Port via Debug Probe
- USB (Micro USB Plug)
- 32 Mbit Quad-SPI Flash
- Ethernet PHY and RJ45 Jack
- 32.768 kHz RTC Crystal
- microSD Card Slot
- CAN Transceiver
- 2 pin header x1 and x2 with 80 pins
- Two buttons and two LEDs for user interaction

Details on the Relax Kit development board can be found in the [Relax Kit User Manual](https://www.infineon.com/dgdl/Infineon-Board_User_Manual_XMC4700_XMC4800_Relax_Kit_Series-UserManual-v01_04-EN.pdf?fileId=5546d46250cc1fdf01513f8e052d07fc) [[1]](#id2).

### Supported Features

The `xmc47_relax_kit` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `xmc47_relax_kit/xmc4700` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L18) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | Infineon XMC4XXX ADC Each ADC group XMC4XXX is assigned to a Zephyr device[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L153) | [`infineon,xmc4xxx-adc`](../../../../build/dts/api/bindings/adc/infineon%2Cxmc4xxx-adc.md#std-dtcompatible-infineon-xmc4xxx-adc) |
| CAN | on-chip | Infineon XMC4xxx CAN[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L265) | [`infineon,xmc4xxx-can`](../../../../build/dts/api/bindings/can/infineon%2Cxmc4xxx-can.md#std-dtcompatible-infineon-xmc4xxx-can) |
| on-chip | Infineon XMC4xxx CAN Node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L280)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L273) | [`infineon,xmc4xxx-can-node`](../../../../build/dts/api/bindings/can/infineon%2Cxmc4xxx-can-node.md#std-dtcompatible-infineon-xmc4xxx-can-node) |
| Clock control | on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L35) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| DMA | on-chip | XMC4xxx DMA Controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L99) | [`infineon,xmc4xxx-dma`](../../../../build/dts/api/bindings/dma/infineon%2Cxmc4xxx-dma.md#std-dtcompatible-infineon-xmc4xxx-dma) |
| Ethernet | on-chip | XMC 4XXX Ethernet[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L251) | [`infineon,xmc4xxx-ethernet`](../../../../build/dts/api/bindings/ethernet/infineon%2Cxmc4xxx-ethernet.md#std-dtcompatible-infineon-xmc4xxx-ethernet) |
| on-board | Generic MII PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/xmc47_relax_kit/xmc47_relax_kit.dts?plain=1#L199) | [`ethernet-phy`](../../../../build/dts/api/bindings/ethernet/ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| Flash controller | on-chip | XMC4XXX flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L24) | [`infineon,xmc4xxx-flash-controller`](../../../../build/dts/api/bindings/flash_controller/infineon%2Cxmc4xxx-flash-controller.md#std-dtcompatible-infineon-xmc4xxx-flash-controller) |
| GPIO & Headers | on-chip | INFINEON XMC4XXX GPIO PORT node[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L58)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L90) | [`infineon,xmc4xxx-gpio`](../../../../build/dts/api/bindings/gpio/infineon%2Cxmc4xxx-gpio.md#std-dtcompatible-infineon-xmc4xxx-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/xmc47_relax_kit/arduino_r3_connector.dtsi?plain=1#L7) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | Infineon XMC4XXX I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L135) | [`infineon,xmc4xxx-i2c`](../../../../build/dts/api/bindings/i2c/infineon%2Cxmc4xxx-i2c.md#std-dtcompatible-infineon-xmc4xxx-i2c) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | Infineon XMC4XXX series Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L42) | [`infineon,xmc4xxx-intc`](../../../../build/dts/api/bindings/interrupt-controller/infineon%2Cxmc4xxx-intc.md#std-dtcompatible-infineon-xmc4xxx-intc) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/xmc47_relax_kit/xmc47_relax_kit.dts?plain=1#L28) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/xmc47_relax_kit/xmc47_relax_kit.dts?plain=1#L39) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MDIO | on-chip | Infineon xmc4xxx Family MDIO Driver node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L257) | [`infineon,xmc4xxx-mdio`](../../../../build/dts/api/bindings/mdio/infineon%2Cxmc4xxx-mdio.md#std-dtcompatible-infineon-xmc4xxx-mdio) |
| MTD | on-chip | XMC4XXX flash[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L29) | [`infineon,xmc4xxx-nv-flash`](../../../../build/dts/api/bindings/mtd/infineon%2Cxmc4xxx-nv-flash.md#std-dtcompatible-infineon-xmc4xxx-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/xmc47_relax_kit/xmc47_relax_kit.dts?plain=1#L73) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | The Infineon XMC4XXX pin controller is responsible for connecting peripheral outputs to specific port/pins (also known as alternate functions) and configures pin properties[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L52) | [`infineon,xmc4xxx-pinctrl`](../../../../build/dts/api/bindings/pinctrl/infineon%2Cxmc4xxx-pinctrl.md#std-dtcompatible-infineon-xmc4xxx-pinctrl) |
| PWM | on-chip | Infineon XMC4XXX PWM Capture Compare Unit 4 (CCU4) module[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L191) | [`infineon,xmc4xxx-ccu4-pwm`](../../../../build/dts/api/bindings/pwm/infineon%2Cxmc4xxx-ccu4-pwm.md#std-dtcompatible-infineon-xmc4xxx-ccu4-pwm) |
| on-chip | Infineon XMC4XXX PWM Capture Compare Unit 8 (CCU8) module[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L219) | [`infineon,xmc4xxx-ccu8-pwm`](../../../../build/dts/api/bindings/pwm/infineon%2Cxmc4xxx-ccu8-pwm.md#std-dtcompatible-infineon-xmc4xxx-ccu8-pwm) |
| RTC | on-chip | Infineon XMC4xxx family RTC device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L240) | [`infineon,xmc4xxx-rtc`](../../../../build/dts/api/bindings/rtc/infineon%2Cxmc4xxx-rtc.md#std-dtcompatible-infineon-xmc4xxx-rtc) |
| Sensors | on-chip | Infineon XMC4XXX die temperature sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L185) | [`infineon,xmc4xxx-temp`](../../../../build/dts/api/bindings/sensor/infineon%2Cxmc4xxx-temp.md#std-dtcompatible-infineon-xmc4xxx-temp) |
| Serial controller | on-chip | INFINEON XMC4XXX UART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L117) | [`infineon,xmc4xxx-uart`](../../../../build/dts/api/bindings/serial/infineon%2Cxmc4xxx-uart.md#std-dtcompatible-infineon-xmc4xxx-uart) |
| SPI | on-chip | INFINEON XMC4XXX SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L141) | [`infineon,xmc4xxx-spi`](../../../../build/dts/api/bindings/spi/infineon%2Cxmc4xxx-spi.md#std-dtcompatible-infineon-xmc4xxx-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4700_F144x2048.dtsi?plain=1#L16) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| Watchdog | on-chip | Infineon XMC4xxx watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L233) | [`infineon,xmc4xxx-watchdog`](../../../../build/dts/api/bindings/watchdog/infineon%2Cxmc4xxx-watchdog.md#std-dtcompatible-infineon-xmc4xxx-watchdog) |

More details about the supported peripherals are available in [XMC4700 TRM](https://www.infineon.com/dgdl/Infineon-ReferenceManual_XMC4700_XMC4800-UM-v01_03-EN.pdf?fileId=5546d462518ffd850151904eb90c0044) [[2]](#id4)

## Build hello world sample

Here is an example for building the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application.

```shell
# From the root of the zephyr repository
west build -b xmc47_relax_kit samples/hello_world
```

## Programming and Debugging

### West Commands

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

> WindowsLinux
>
> ```shell
> # Do a pristine build
> west build -b xmc47_relax_kit -p always samples/hello_world
>
> west flash
> west debug
> ```
>
> ```shell
> # Do a pristine build
> west build -b xmc47_relax_kit -p always samples/hello_world
>
> west flash
> west debug
> ```

Once the gdb console starts after executing the west debug command, you may now set breakpoints and perform other standard GDB debugging.

## References

[[1](#id3)]

[https://www.infineon.com/dgdl/Infineon-Board\_User\_Manual\_XMC4700\_XMC4800\_Relax\_Kit\_Series-UserManual-v01\_04-EN.pdf?fileId=5546d46250cc1fdf01513f8e052d07fc](https://www.infineon.com/dgdl/Infineon-Board_User_Manual_XMC4700_XMC4800_Relax_Kit_Series-UserManual-v01_04-EN.pdf?fileId=5546d46250cc1fdf01513f8e052d07fc)

[[2](#id5)]

[https://www.infineon.com/dgdl/Infineon-ReferenceManual\_XMC4700\_XMC4800-UM-v01\_03-EN.pdf?fileId=5546d462518ffd850151904eb90c0044](https://www.infineon.com/dgdl/Infineon-ReferenceManual_XMC4700_XMC4800-UM-v01_03-EN.pdf?fileId=5546d462518ffd850151904eb90c0044)

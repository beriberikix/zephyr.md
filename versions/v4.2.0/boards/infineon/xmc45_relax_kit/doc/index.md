---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/infineon/xmc45_relax_kit/doc/index.html
original_path: boards/infineon/xmc45_relax_kit/doc/index.html
---

# XMC45-RELAX-KIT

Board Overview

[![../../../../_images/xmc45_relax_kit.jpg](https://docs.zephyrproject.org/4.2.0/_images/xmc45_relax_kit.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/xmc45_relax_kit.jpg)

XMC45-RELAX-KIT

Name:
:   `xmc45_relax_kit`

Vendor:
:   Infineon Technologies

Architecture:
:   arm

SoC:
:   xmc4500

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/infineon/xmc45_relax_kit/doc/index.rst/../..)

## Overview

The XMC4500 Relax Kit is designed to evaluate the capabilities of the XMC4500
Microcontroller. It is based on High performance ARM Cortex-M4F which can run
up to 120MHz.

### Features:

- ARM Cortex-M4F XMC4500
- 32 Mbit Quad-SPI Flash
- 4 x SPI-Master, 3x I2C, 3 x I2S, 3 x UART, 2 x CAN, 17 x ADC
- 2 pin header x1 and x2 with 80 pins
- Two buttons and two LEDs for user interaction
- Detachable on-board debugger (second XMC4500) with Segger J-Link

Details on the Relax Kit development board can be found in the [Relax Kit User Manual](https://www.infineon.com/dgdl/Board_Users_Manual_XMC4500_Relax_Kit-V1_R1.2_released.pdf?fileId=db3a30433acf32c9013adf6b97b112f9) [[1]](#id2).

### Supported Features

The `xmc45_relax_kit` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `xmc45_relax_kit/xmc4500` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L18) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | Infineon XMC4XXX ADC Each ADC group XMC4XXX is assigned to a Zephyr device[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L153) | [`infineon,xmc4xxx-adc`](../../../../build/dts/api/bindings/adc/infineon%2Cxmc4xxx-adc.md#std-dtcompatible-infineon-xmc4xxx-adc) |
| CAN | on-chip | Infineon XMC4xxx CAN[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L265) | [`infineon,xmc4xxx-can`](../../../../build/dts/api/bindings/can/infineon%2Cxmc4xxx-can.md#std-dtcompatible-infineon-xmc4xxx-can) |
| on-chip | Infineon XMC4xxx CAN Node[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L273) | [`infineon,xmc4xxx-can-node`](../../../../build/dts/api/bindings/can/infineon%2Cxmc4xxx-can-node.md#std-dtcompatible-infineon-xmc4xxx-can-node) |
| Clock control | on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L35) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| DMA | on-chip | XMC4xxx DMA Controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L99) | [`infineon,xmc4xxx-dma`](../../../../build/dts/api/bindings/dma/infineon%2Cxmc4xxx-dma.md#std-dtcompatible-infineon-xmc4xxx-dma) |
| Ethernet | on-chip | XMC 4XXX Ethernet[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L251) | [`infineon,xmc4xxx-ethernet`](../../../../build/dts/api/bindings/ethernet/infineon%2Cxmc4xxx-ethernet.md#std-dtcompatible-infineon-xmc4xxx-ethernet) |
| on-board | Generic MII PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/xmc45_relax_kit/xmc45_relax_kit.dts?plain=1#L161) | [`ethernet-phy`](../../../../build/dts/api/bindings/ethernet/phy/ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| Flash controller | on-chip | XMC4XXX flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L24) | [`infineon,xmc4xxx-flash-controller`](../../../../build/dts/api/bindings/flash_controller/infineon%2Cxmc4xxx-flash-controller.md#std-dtcompatible-infineon-xmc4xxx-flash-controller) |
| GPIO & Headers | on-chip | INFINEON XMC4XXX GPIO Port[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L66)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L58) | [`infineon,xmc4xxx-gpio`](../../../../build/dts/api/bindings/gpio/infineon%2Cxmc4xxx-gpio.md#std-dtcompatible-infineon-xmc4xxx-gpio) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | Infineon XMC4XXX series Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L42) | [`infineon,xmc4xxx-intc`](../../../../build/dts/api/bindings/interrupt-controller/infineon%2Cxmc4xxx-intc.md#std-dtcompatible-infineon-xmc4xxx-intc) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/xmc45_relax_kit/xmc45_relax_kit.dts?plain=1#L29) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/xmc45_relax_kit/xmc45_relax_kit.dts?plain=1#L40) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MDIO | on-chip | Infineon xmc4xxx Family MDIO Driver node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L257) | [`infineon,xmc4xxx-mdio`](../../../../build/dts/api/bindings/mdio/infineon%2Cxmc4xxx-mdio.md#std-dtcompatible-infineon-xmc4xxx-mdio) |
| MTD | on-chip | XMC4XXX flash[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L29) | [`infineon,xmc4xxx-nv-flash`](../../../../build/dts/api/bindings/mtd/infineon%2Cxmc4xxx-nv-flash.md#std-dtcompatible-infineon-xmc4xxx-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/xmc45_relax_kit/xmc45_relax_kit.dts?plain=1#L77) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Infineon XMC4XXX Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L52) | [`infineon,xmc4xxx-pinctrl`](../../../../build/dts/api/bindings/pinctrl/infineon%2Cxmc4xxx-pinctrl.md#std-dtcompatible-infineon-xmc4xxx-pinctrl) |
| PWM | on-chip | Infineon XMC4XXX PWM Capture Compare Unit 4 (CCU4) module[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L191) | [`infineon,xmc4xxx-ccu4-pwm`](../../../../build/dts/api/bindings/pwm/infineon%2Cxmc4xxx-ccu4-pwm.md#std-dtcompatible-infineon-xmc4xxx-ccu4-pwm) |
| on-chip | Infineon XMC4XXX PWM Capture Compare Unit 8 (CCU8) module[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L219) | [`infineon,xmc4xxx-ccu8-pwm`](../../../../build/dts/api/bindings/pwm/infineon%2Cxmc4xxx-ccu8-pwm.md#std-dtcompatible-infineon-xmc4xxx-ccu8-pwm) |
| RTC | on-chip | Infineon XMC4xxx family RTC device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L240) | [`infineon,xmc4xxx-rtc`](../../../../build/dts/api/bindings/rtc/infineon%2Cxmc4xxx-rtc.md#std-dtcompatible-infineon-xmc4xxx-rtc) |
| Sensors | on-chip | Infineon XMC4XXX die temperature sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L185) | [`infineon,xmc4xxx-temp`](../../../../build/dts/api/bindings/sensor/infineon%2Cxmc4xxx-temp.md#std-dtcompatible-infineon-xmc4xxx-temp) |
| Serial controller | on-chip | INFINEON XMC4XXX UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L135) | [`infineon,xmc4xxx-uart`](../../../../build/dts/api/bindings/serial/infineon%2Cxmc4xxx-uart.md#std-dtcompatible-infineon-xmc4xxx-uart) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4500_F100x1024.dtsi?plain=1#L17) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| Watchdog | on-chip | Infineon XMC4xxx watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat3/xmc/xmc4xxx.dtsi?plain=1#L233) | [`infineon,xmc4xxx-watchdog`](../../../../build/dts/api/bindings/watchdog/infineon%2Cxmc4xxx-watchdog.md#std-dtcompatible-infineon-xmc4xxx-watchdog) |

The on-board 12-MHz crystal allows the device to run at its maximum operating speed of 120MHz.

## Build hello world sample

Here is an example for building the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application.

```shell
# From the root of the zephyr repository
west build -b xmc45_relax_kit samples/hello_world
```

## Programming and Debugging

The `xmc45_relax_kit` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |

### West Commands

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

> WindowsLinux
>
> ```shell
> # Do a pristine build
> west build -b xmc45_relax_kit -p always samples/hello_world
>
> west flash
> west debug
> ```
>
> ```shell
> # Do a pristine build
> west build -b xmc45_relax_kit -p always samples/hello_world
>
> west flash
> west debug
> ```

Once the gdb console starts after executing the west debug command, you may now set breakpoints and perform other standard GDB debugging.

## References

[[1](#id3)]

[https://www.infineon.com/dgdl/Board\_Users\_Manual\_XMC4500\_Relax\_Kit-V1\_R1.2\_released.pdf?fileId=db3a30433acf32c9013adf6b97b112f9](https://www.infineon.com/dgdl/Board_Users_Manual_XMC4500_Relax_Kit-V1_R1.2_released.pdf?fileId=db3a30433acf32c9013adf6b97b112f9)

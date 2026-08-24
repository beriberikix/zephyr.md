---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/realtek/rts5912_evb/doc/index.html
original_path: boards/realtek/rts5912_evb/doc/index.html
---

# RTS5912 Evaluation Board

Board Overview

[![../../../../_images/rts5912evb.webp](https://docs.zephyrproject.org/4.2.0/_images/rts5912evb.webp)
](https://docs.zephyrproject.org/4.2.0/_images/rts5912evb.webp)

RTS5912 Evaluation Board

Name:
:   `rts5912_evb`

Vendor:
:   Realtek Semiconductor Corp.

Architecture:
:   arm

SoC:
:   rts5912

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/realtek/rts5912_evb/doc/index.rst/../..)

## Overview

The RTS5912 EVB is a development platform to evaluate the Realtek RTS5912 embedded controller.

## Hardware

- Realtek-M300 Processor (compatible to Cortex-M33)
- Memory:

  > - 384 KB SRAM
  > - 64 KB ROM
  > - 512 KB Flash(MCM)
  > - 256 B Battery SRAM
- PECI interface 3.1
- FAN, PWM and TACHO pins
- 6x I2C instances
- eSPI header
- 1x PS/2 ports
- Keyboard interface headers

For more information about the evb board please see [RTS5912\_EVB\_Schematics](https://github.com/JasonLin-RealTek/Realtek_EC/blob/main/RTS5912_EVB_Schematic_Ver%201.1_20240701_1407.pdf) [[1]](#id2) and [RTS5912\_DATASHEET](https://github.com/JasonLin-RealTek/Realtek_EC/blob/main/RTS5912_datasheet_brief.pdf) [[2]](#id4)

The board is powered through the +5V USB Type-C connector or adaptor.

### Supported Features

The `rts5912_evb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `rts5912_evb/rts5912` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L21) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | Realtek rts5912 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L270) | [`realtek,rts5912-adc`](../../../../build/dts/api/bindings/adc/realtek,rts5912-adc.md#std-dtcompatible-realtek-rts5912-adc) |
| Clock control | on-chip | Realtek RTS5912 System Clock Controller (SCCON)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L78) | [`realtek,rts5912-sccon`](../../../../build/dts/api/bindings/clock/realtek,rts5912-sccon.md#std-dtcompatible-realtek-rts5912-sccon) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L52) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | Realtek RTS5912 32bit timer[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L94) | [`realtek,rts5912-timer`](../../../../build/dts/api/bindings/counter/realtek,rts5912-timer.md#std-dtcompatible-realtek-rts5912-timer) |
| on-chip | Realtek RTS5912 32-bit slow timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L251) | [`realtek,rts5912-slwtimer`](../../../../build/dts/api/bindings/counter/realtek,rts5912-slwtimer.md#std-dtcompatible-realtek-rts5912-slwtimer) |
| Cryptographic accelerator | on-chip | Realtek RTS5912 Crypto SHA accelerator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L616) | [`realtek,rts5912-sha`](../../../../build/dts/api/bindings/crypto/realtek,rts5912-sha.md#std-dtcompatible-realtek-rts5912-sha) |
| ESPI | on-chip | Realtek RTS5912 eSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L172) | [`realtek,rts5912-espi`](../../../../build/dts/api/bindings/espi/realtek,rts5912-espi.md#std-dtcompatible-realtek-rts5912-espi) |
| Flash controller | on-chip | Realtek RTS5912 flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L514) | [`realtek,rts5912-flash-controller`](../../../../build/dts/api/bindings/flash_controller/realtek,rts5912-flash-controller.md#std-dtcompatible-realtek-rts5912-flash-controller) |
| GPIO & Headers | on-chip | Realtek RTS5912 GPIO[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L304) | [`realtek,rts5912-gpio`](../../../../build/dts/api/bindings/gpio/realtek,rts5912-gpio.md#std-dtcompatible-realtek-rts5912-gpio) |
| on-chip | Serial Wire - JTAG Connector[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L688) | [`swj-connector`](../../../../build/dts/api/bindings/gpio/swj-connector.md#std-dtcompatible-swj-connector) |
| I2C | on-chip | Synopsys DesignWare I2C[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L528) | [`snps,designware-i2c`](../../../../build/dts/api/bindings/i2c/snps,designware-i2c.md#std-dtcompatible-snps-designware-i2c) |
| on-chip | Realtek RTS5912 I2C node[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L624) | [`realtek,rts5912-i2c`](../../../../build/dts/api/bindings/i2c/realtek,rts5912-i2c.md#std-dtcompatible-realtek-rts5912-i2c) |
| Input | on-chip | Realtek RTS5912 keyboard matrix controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L432) | [`realtek,rts5912-kbd`](../../../../build/dts/api/bindings/input/realtek,rts5912-kbd.md#std-dtcompatible-realtek-rts5912-kbd) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| Memory controller | on-chip | Realtek, RTS5912 Battery Backed RAM node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L72) | [`realtek,rts5912-bbram`](../../../../build/dts/api/bindings/memory-controllers/realtek,rts5912-bbram.md#std-dtcompatible-realtek-rts5912-bbram) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L520) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | Realtek RTS5912 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L297) | [`realtek,rts5912-pinctrl`](../../../../build/dts/api/bindings/pinctrl/realtek,rts5912-pinctrl.md#std-dtcompatible-realtek-rts5912-pinctrl) |
| Power management | on-chip | RTS5912 ULPM power controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L695) | [`realtek,rts5912-ulpm`](../../../../build/dts/api/bindings/power/realtek,rts5912-ulpm.md#std-dtcompatible-realtek-rts5912-ulpm) |
| PWM | on-chip | Realtek RTS5912 PWM[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L450) | [`realtek,rts5912-pwm`](../../../../build/dts/api/bindings/pwm/realtek,rts5912-pwm.md#std-dtcompatible-realtek-rts5912-pwm) |
| RTC | on-chip | RTC on Realtek RTS5912 EC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L86) | [`realtek,rts5912-rtc`](../../../../build/dts/api/bindings/rtc/realtek,rts5912-rtc.md#std-dtcompatible-realtek-rts5912-rtc) |
| Serial controller | on-chip | ns16550 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L279) | [`ns16550`](../../../../build/dts/api/bindings/serial/ns16550.md#std-dtcompatible-ns16550) |
| on-chip | Realtek RTS5912 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L288) | [`realtek,rts5912-uart`](../../../../build/dts/api/bindings/serial/realtek,rts5912-uart.md#std-dtcompatible-realtek-rts5912-uart) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L46) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Tachometer | on-chip | Realtek rts5912 tachometer controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L441) | [`realtek,rts5912-tach`](../../../../build/dts/api/bindings/tach/realtek,rts5912-tach.md#std-dtcompatible-realtek-rts5912-tach) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | RTOS Timer on Realtek RTS5912 EC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L263) | [`realtek,rts5912-rtmr`](../../../../build/dts/api/bindings/timer/realtek,rts5912-rtmr.md#std-dtcompatible-realtek-rts5912-rtmr) |
| Watchdog | on-chip | Realtek RTS5912 watchdog timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L421) | [`realtek,rts5912-watchdog`](../../../../build/dts/api/bindings/watchdog/realtek,rts5912-watchdog.md#std-dtcompatible-realtek-rts5912-watchdog) |

## Programming and Debugging

The `rts5912_evb` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Building

1. Build [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application as you would normally do.
2. The file `zephyr.rts5912.bin` will be created if the build system can build successfully.
   This binary image can be found under file “build/zephyr/”.

### Flashing

1. Connect Dediprog into header `J81` and `J82`.
2. Use Dediprog SF600 programmer to write the binary into the external flash `U10` at the address 0x0.
3. Power off the board.
4. Set the strap pin `GPIO108` to high and power on the board.

### Debugging

Using SWD or JTAG with ULINPRO.

## References

[[1](#id3)]

[https://github.com/JasonLin-RealTek/Realtek\_EC/blob/main/RTS5912\_EVB\_Schematic\_Ver%201.1\_20240701\_1407.pdf](https://github.com/JasonLin-RealTek/Realtek_EC/blob/main/RTS5912_EVB_Schematic_Ver%201.1_20240701_1407.pdf)

[[2](#id5)]

[https://github.com/JasonLin-RealTek/Realtek\_EC/blob/main/RTS5912\_datasheet\_brief.pdf](https://github.com/JasonLin-RealTek/Realtek_EC/blob/main/RTS5912_datasheet_brief.pdf)

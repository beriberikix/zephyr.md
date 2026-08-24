---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nuvoton/numaker_pfm_m487/doc/index.html
original_path: boards/nuvoton/numaker_pfm_m487/doc/index.html
---

# NUMAKER PFM M487

Board Overview

[![../../../../_images/pfm_m487.jpg](https://docs.zephyrproject.org/4.2.0/_images/pfm_m487.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/pfm_m487.jpg)

NUMAKER PFM M487

Name:
:   `numaker_pfm_m487`

Vendor:
:   Nuvoton Technology Corporation

Architecture:
:   arm

SoC:
:   m487

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nuvoton/numaker_pfm_m487/doc/index.rst/../..)

## Overview

The NuMaker PFM M487 is an Internet of Things (IoT) application focused platform
specially developed by Nuvoton. The PFM-M487 is based on the NuMicro® M487
Ethernet series MCU with ARM® -Cortex®-M4F core.

### Features:

- 32-bit Arm Cortex®-M4 M487JIDAE MCU
- Core clock up to 192 MHz
- 512 KB embedded Dual Bank Flash and 160 KB SRAM
- Audio codec (NAU88L25) with Microphone In and Headphone Out
- Ethernet (IP101GR) for network application
- USB 2.0 High-Speed OTG / Host / Device
- USB 1.1 Full-Speed OTG / Host / Device
- External SPI Flash (Winbond W25Q20) which can be regarded as ROM module
- MicroSD Card slot for T-Flash
- M487 extended interface 4 connector with 36 pins each
- Arduino UNO compatible interface
- Three push-buttons: one is for reset and the other two are for user-defined
- Four LEDs: one is for power indication and the other three are for user-defined
- On-board NU-Link-Me ICE debugger/programmer with SWD connector

More information about the board can be found at the [PFM M487 User Manual](https://www.nuvoton.com/export/resource-files/UM_NuMaker-PFM-M487_User_Manual_EN_Rev1.01.pdf) [[1]](#id2).

### Supported Features

The `numaker_pfm_m487` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `numaker_pfm_m487/m487` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m48x.dtsi?plain=1#L16) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| Clock control | on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m48x.dtsi?plain=1#L33) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| GPIO & Headers | on-chip | Nuvoton NuMicro GPIO[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m48x.dtsi?plain=1#L58)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m48x.dtsi?plain=1#L48) | [`nuvoton,numicro-gpio`](../../../../build/dts/api/bindings/gpio/nuvoton,numicro-gpio.md#std-dtcompatible-nuvoton-numicro-gpio) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nuvoton/numaker_pfm_m487/numaker_pfm_m487.dts?plain=1#L47) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nuvoton/numaker_pfm_m487/numaker_pfm_m487.dts?plain=1#L31) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Pin control | on-chip | Nuvoton NuMicro pinctrl node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m48x.dtsi?plain=1#L40) | [`nuvoton,numicro-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nuvoton,numicro-pinctrl.md#std-dtcompatible-nuvoton-numicro-pinctrl) |
| Serial controller | on-chip | NUVOTON NUMICRO FAMILY UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m48x.dtsi?plain=1#L128)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m48x.dtsi?plain=1#L134) | [`nuvoton,numicro-uart`](../../../../build/dts/api/bindings/serial/nuvoton,numicro-uart.md#std-dtcompatible-nuvoton-numicro-uart) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m48x.dtsi?plain=1#L23) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |

The on-board 12-MHz crystal allows the device to run at its maximum operating speed of 192MHz.

More details about the supported peripherals are available in [M480 TRM](https://www.nuvoton.com/export/resource-files/TRM_M480_Series_EN_Rev2.02.pdf) [[2]](#id4)

## Building and Flashing

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

On board debugger Nu-link-Me can emulate UART0 as a virtual COM port over usb,
To enable this, set ISW1 DIP switch 1-3 (TXD RXD VOM) to ON.
Connect the PFM M487 IoT to your host computer using the USB port, then
run a serial host program to connect with your board. For example:

```shell
$ minicom -D /dev/ttyACM0
```

```shell
# From the root of the zephyr repository
west build -b numaker_pfm_m487 samples/hello_world
west flash
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b numaker_pfm_m487 samples/hello_world
west debug
```

Step through the application in your debugger.

## References

[[1](#id3)]

[https://www.nuvoton.com/export/resource-files/UM\_NuMaker-PFM-M487\_User\_Manual\_EN\_Rev1.01.pdf](https://www.nuvoton.com/export/resource-files/UM_NuMaker-PFM-M487_User_Manual_EN_Rev1.01.pdf)

[[2](#id5)]

[https://www.nuvoton.com/export/resource-files/TRM\_M480\_Series\_EN\_Rev2.02.pdf](https://www.nuvoton.com/export/resource-files/TRM_M480_Series_EN_Rev2.02.pdf)

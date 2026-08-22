---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/nuvoton/numaker_m2l31ki/doc/index.html
original_path: boards/nuvoton/numaker_m2l31ki/doc/index.html
---

# NUMAKER M2L31KI

Board Overview

[![../../../../_images/m2l31ki.webp](../../../../_images/m2l31ki.webp)
](../../../../_images/m2l31ki.webp)

NUMAKER M2L31KI

Name:
:   `numaker_m2l31ki`

Vendor:
:   Nuvoton Technology Corporation

Architecture:
:   arm

SoC:
:   m2l31xxx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nuvoton/numaker_m2l31ki/doc/index.rst/../..)

## Overview

The NuMaker M2L31KI is an Internet of Things (IoT) application focused platform
specially developed by Nuvoton. The NuMaker-M2L31KI is based on the NuMicro® M2L31
series MCU with ARM® -Cortex®-M23 core.

### Features:

- 32-bit Arm Cortex®-M23 M2L31KIDAE MCU
- Core clock up to 72 MHz
- 512 KB embedded Dual Bank Flash and 168 KB SRAM
- USB 2.0 Full-Speed OTG / Device
- USB 1.1 Host
- Arduino UNO compatible interface
- One push-button is for reset
- Two LEDs: one is for power indication and the other is for user-defined
- On-board NU-Link2 ICE debugger/programmer with SWD connector

More information about the board can be found at the [NuMaker M2L31KI User Manual](https://www.nuvoton.com/products/microcontrollers/arm-cortex-m23-mcus/m2l31-series/) [[1]](#id2).

### Supported Features

The `numaker_m2l31ki` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `numaker_m2l31ki/m2l31xxx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M23 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m2l31x.dtsi?plain=1#L29) | [`arm,cortex-m23`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m23.md#std-dtcompatible-arm-cortex-m23) |
| ADC | on-chip | Nuvoton, NuMaker ADC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m2l31x.dtsi?plain=1#L318) | [`nuvoton,numaker-adc`](../../../../build/dts/api/bindings/adc/nuvoton%2Cnumaker-adc.md#std-dtcompatible-nuvoton-numaker-adc) |
| CAN | on-chip | Nuvoton NuMaker CAN FD controller, using Bosch M\_CAN IP[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m2l31x.dtsi?plain=1#L364) | [`nuvoton,numaker-canfd`](../../../../build/dts/api/bindings/can/nuvoton%2Cnumaker-canfd.md#std-dtcompatible-nuvoton-numaker-canfd) |
| Clock control | on-chip | Nuvoton NuMaker System Clock Controller (SCC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m2l31x.dtsi?plain=1#L43) | [`nuvoton,numaker-scc`](../../../../build/dts/api/bindings/clock/nuvoton%2Cnumaker-scc.md#std-dtcompatible-nuvoton-numaker-scc) |
| on-chip | Nuvoton NuMaker Peripheral Clock Controller (PCC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m2l31x.dtsi?plain=1#L54) | [`nuvoton,numaker-pcc`](../../../../build/dts/api/bindings/clock/nuvoton%2Cnumaker-pcc.md#std-dtcompatible-nuvoton-numaker-pcc) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m2l31x.dtsi?plain=1#L36) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Flash controller | on-chip | Nuvoton NuMaker RRAM Memory Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m2l31x.dtsi?plain=1#L66) | [`nuvoton,numaker-rmc`](../../../../build/dts/api/bindings/flash_controller/nuvoton%2Cnumaker-rmc.md#std-dtcompatible-nuvoton-numaker-rmc) |
| GPIO & Headers | on-chip | Nuvoton, Numaker-GPIO node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m2l31x.dtsi?plain=1#L186)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m2l31x.dtsi?plain=1#L166) | [`nuvoton,numaker-gpio`](../../../../build/dts/api/bindings/gpio/nuvoton%2Cnumaker-gpio.md#std-dtcompatible-nuvoton-numaker-gpio) |
| I2C | on-chip | Nuvoton, NuMaker I2C controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m2l31x.dtsi?plain=1#L270) | [`nuvoton,numaker-i2c`](../../../../build/dts/api/bindings/i2c/nuvoton%2Cnumaker-i2c.md#std-dtcompatible-nuvoton-numaker-i2c) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nuvoton/numaker_m2l31ki/numaker_m2l31ki.dts?plain=1#L29) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m2l31x.dtsi?plain=1#L72) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nuvoton/numaker_m2l31ki/numaker_m2l31ki.dts?plain=1#L43) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Pin controller is responsible for controlling pin function selection and pin properties[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m2l31x.dtsi?plain=1#L159) | [`nuvoton,numaker-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nuvoton%2Cnumaker-pinctrl.md#std-dtcompatible-nuvoton-numaker-pinctrl) |
| PPC architecture | on-chip | Nuvoton NuMaker USB Type-C power path controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m2l31x.dtsi?plain=1#L434) | [`nuvoton,numaker-ppc`](../../../../build/dts/api/bindings/ppc/nuvoton%2Cnumaker-ppc.md#std-dtcompatible-nuvoton-numaker-ppc) |
| PWM | on-chip | Nuvoton, NuMaker PWM controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m2l31x.dtsi?plain=1#L340) | [`nuvoton,numaker-pwm`](../../../../build/dts/api/bindings/pwm/nuvoton%2Cnumaker-pwm.md#std-dtcompatible-nuvoton-numaker-pwm) |
| Reset controller | on-chip | Nuvoton, Numaker-RESET[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m2l31x.dtsi?plain=1#L60) | [`nuvoton,numaker-rst`](../../../../build/dts/api/bindings/reset/nuvoton%2Cnumaker-rst.md#std-dtcompatible-nuvoton-numaker-rst) |
| RTC | on-chip | Nuvoton, NuMaker RTC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m2l31x.dtsi?plain=1#L331) | [`nuvoton,numaker-rtc`](../../../../build/dts/api/bindings/rtc/nuvoton%2Cnumaker-rtc.md#std-dtcompatible-nuvoton-numaker-rtc) |
| Serial controller | on-chip | Nuvoton, Numaker-UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m2l31x.dtsi?plain=1#L79)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m2l31x.dtsi?plain=1#L89) | [`nuvoton,numaker-uart`](../../../../build/dts/api/bindings/serial/nuvoton%2Cnumaker-uart.md#std-dtcompatible-nuvoton-numaker-uart) |
| SPI | on-chip | Nuvoton, NuMaker SPI controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m2l31x.dtsi?plain=1#L226) | [`nuvoton,numaker-spi`](../../../../build/dts/api/bindings/spi/nuvoton%2Cnumaker-spi.md#std-dtcompatible-nuvoton-numaker-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m2l31kid.dtsi?plain=1#L11) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| USB Type-C Port Controller | on-chip | Nuvoton NuMaker USB Type-C port controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m2l31x.dtsi?plain=1#L413) | [`nuvoton,numaker-tcpc`](../../../../build/dts/api/bindings/tcpc/nuvoton%2Cnumaker-tcpc.md#std-dtcompatible-nuvoton-numaker-tcpc) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| USB | on-chip | Nuvoton NuMaker USB 1.1 device controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m2l31x.dtsi?plain=1#L392) | [`nuvoton,numaker-usbd`](../../../../build/dts/api/bindings/usb/nuvoton%2Cnumaker-usbd.md#std-dtcompatible-nuvoton-numaker-usbd) |
| USB Type-C | on-chip | Nuvoton NuMaker USB Type-C VBUS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m2l31x.dtsi?plain=1#L429) | [`nuvoton,numaker-vbus`](../../../../build/dts/api/bindings/usb-c/nuvoton%2Cnumaker-vbus.md#std-dtcompatible-nuvoton-numaker-vbus) |
| Watchdog | on-chip | Nuvoton, NuMaker window watchdog timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m2l31x.dtsi?plain=1#L405) | [`nuvoton,numaker-wwdt`](../../../../build/dts/api/bindings/watchdog/nuvoton%2Cnumaker-wwdt.md#std-dtcompatible-nuvoton-numaker-wwdt) |

The on-board 12-MHz crystal allows the device to run at its maximum operating speed of 72MHz.

More details about the supported peripherals are available in [M2L31 TRM](https://www.nuvoton.com/products/microcontrollers/arm-cortex-m23-mcus/m2l31-series/) [[1]](#id2)

## Building and Flashing

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

On board debugger Nu-link2 can emulate UART0 as a virtual COM port over usb,
To enable this, set ISW1 DIP switch 1-3 (TXD RXD VOM) to ON.
Connect the NuMaker-M2L31KI to your host computer using the USB port, then
run a serial host program to connect with your board. For example:

```shell
$ minicom -D /dev/ttyACM0
```

```shell
# From the root of the zephyr repository
west build -b numaker_m2l31ki samples/hello_world
west flash
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b numaker_m2l31ki samples/hello_world
west debug
```

Step through the application in your debugger.

## References

[1]
([1](#id3),[2](#id4))

[https://www.nuvoton.com/products/microcontrollers/arm-cortex-m23-mcus/m2l31-series/](https://www.nuvoton.com/products/microcontrollers/arm-cortex-m23-mcus/m2l31-series/)

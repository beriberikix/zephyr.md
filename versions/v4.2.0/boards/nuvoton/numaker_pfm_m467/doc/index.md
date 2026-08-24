---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nuvoton/numaker_pfm_m467/doc/index.html
original_path: boards/nuvoton/numaker_pfm_m467/doc/index.html
---

# NUMAKER PFM M467

Board Overview

[![../../../../_images/pfm_m467.jpeg](https://docs.zephyrproject.org/4.2.0/_images/pfm_m467.jpeg)
](https://docs.zephyrproject.org/4.2.0/_images/pfm_m467.jpeg)

NUMAKER PFM M467

Name:
:   `numaker_pfm_m467`

Vendor:
:   Nuvoton Technology Corporation

Architecture:
:   arm

SoC:
:   m467

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nuvoton/numaker_pfm_m467/doc/index.rst/../..)

## Overview

The NuMaker PFM M467 is an Internet of Things (IoT) application focused platform
specially developed by Nuvoton. The PFM-M467 is based on the NuMicro® M467
Ethernet series MCU with ARM® -Cortex®-M4F core.

### Features:

- 32-bit Arm Cortex®-M4 M467HJHAE MCU
- Core clock up to 200 MHz
- 1024 KB embedded Dual Bank Flash and 512 KB SRAM
- Ethernet (IP101GR) for network application
- USB 2.0 High-Speed OTG / Host / Device
- USB 1.1 Full-Speed OTG / Host / Device
- External SPI Flash (Winbond W25Q20) which can be regarded as ROM module
- MicroSD Card slot for T-Flash
- Arduino UNO compatible interface
- Three push-buttons: one is for reset and the other two are for user-defined
- Four LEDs: one is for power indication and the other three are for user-defined
- On-board NU-Link2 ICE debugger/programmer with SWD connector

More information about the board can be found at the [PFM M467 User Manual](https://www.nuvoton.com/export/resource-files/UM_NuMaker-PFM-M467_User_Manual_EN_Rev1.01.pdf) [[1]](#id2).

### Supported Features

The `numaker_pfm_m467` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `numaker_pfm_m467/m467` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m46x.dtsi?plain=1#L29) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | Nuvoton, NuMaker ADC controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m46x.dtsi?plain=1#L566) | [`nuvoton,numaker-adc`](../../../../build/dts/api/bindings/adc/nuvoton%2Cnumaker-adc.md#std-dtcompatible-nuvoton-numaker-adc) |
| CAN | on-chip | Nuvoton NuMaker CAN FD controller, using Bosch M\_CAN IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m46x.dtsi?plain=1#L440)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m46x.dtsi?plain=1#L454) | [`nuvoton,numaker-canfd`](../../../../build/dts/api/bindings/can/nuvoton%2Cnumaker-canfd.md#std-dtcompatible-nuvoton-numaker-canfd) |
| Clock control | on-chip | Nuvoton NuMaker System Clock Controller (SCC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m46x.dtsi?plain=1#L48) | [`nuvoton,numaker-scc`](../../../../build/dts/api/bindings/clock/nuvoton%2Cnumaker-scc.md#std-dtcompatible-nuvoton-numaker-scc) |
| on-chip | Nuvoton NuMaker Peripheral Clock Controller (PCC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m46x.dtsi?plain=1#L60) | [`nuvoton,numaker-pcc`](../../../../build/dts/api/bindings/clock/nuvoton%2Cnumaker-pcc.md#std-dtcompatible-nuvoton-numaker-pcc) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m46x.dtsi?plain=1#L41) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Ethernet | on-chip | Nuvoton, NuMaker Ethernet controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m46x.dtsi?plain=1#L496) | [`nuvoton,numaker-ethernet`](../../../../build/dts/api/bindings/ethernet/nuvoton%2Cnumaker-ethernet.md#std-dtcompatible-nuvoton-numaker-ethernet) |
| Flash controller | on-chip | Nuvoton NuMaker Flash Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m46x.dtsi?plain=1#L73) | [`nuvoton,numaker-fmc`](../../../../build/dts/api/bindings/flash_controller/nuvoton%2Cnumaker-fmc.md#std-dtcompatible-nuvoton-numaker-fmc) |
| GPIO & Headers | on-chip | Nuvoton Numaker GPIO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m46x.dtsi?plain=1#L205)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m46x.dtsi?plain=1#L195) | [`nuvoton,numaker-gpio`](../../../../build/dts/api/bindings/gpio/nuvoton%2Cnumaker-gpio.md#std-dtcompatible-nuvoton-numaker-gpio) |
| I2C | on-chip | Nuvoton, NuMaker I2C controller[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m46x.dtsi?plain=1#L506) | [`nuvoton,numaker-i2c`](../../../../build/dts/api/bindings/i2c/nuvoton%2Cnumaker-i2c.md#std-dtcompatible-nuvoton-numaker-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nuvoton/numaker_pfm_m467/numaker_pfm_m467.dts?plain=1#L52) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nuvoton/numaker_pfm_m467/numaker_pfm_m467.dts?plain=1#L36) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m46x.dtsi?plain=1#L79) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nuvoton/numaker_pfm_m467/numaker_pfm_m467.dts?plain=1#L80) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Pin controller is responsible for controlling pin function selection and pin properties[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m46x.dtsi?plain=1#L187) | [`nuvoton,numaker-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nuvoton%2Cnumaker-pinctrl.md#std-dtcompatible-nuvoton-numaker-pinctrl) |
| PWM | on-chip | Nuvoton, NuMaker PWM controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m46x.dtsi?plain=1#L416) | [`nuvoton,numaker-pwm`](../../../../build/dts/api/bindings/pwm/nuvoton%2Cnumaker-pwm.md#std-dtcompatible-nuvoton-numaker-pwm) |
| Reset controller | on-chip | Nuvoton, Numaker-RESET[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m46x.dtsi?plain=1#L66) | [`nuvoton,numaker-rst`](../../../../build/dts/api/bindings/reset/nuvoton%2Cnumaker-rst.md#std-dtcompatible-nuvoton-numaker-rst) |
| RTC | on-chip | Nuvoton, NuMaker RTC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m46x.dtsi?plain=1#L626) | [`nuvoton,numaker-rtc`](../../../../build/dts/api/bindings/rtc/nuvoton%2Cnumaker-rtc.md#std-dtcompatible-nuvoton-numaker-rtc) |
| Serial controller | on-chip | Nuvoton, Numaker-UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m46x.dtsi?plain=1#L87)[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m46x.dtsi?plain=1#L97) | [`nuvoton,numaker-uart`](../../../../build/dts/api/bindings/serial/nuvoton%2Cnumaker-uart.md#std-dtcompatible-nuvoton-numaker-uart) |
| SPI | on-chip | Nuvoton, NuMaker SPI controller[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m46x.dtsi?plain=1#L295) | [`nuvoton,numaker-spi`](../../../../build/dts/api/bindings/spi/nuvoton%2Cnumaker-spi.md#std-dtcompatible-nuvoton-numaker-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m46x.dtsi?plain=1#L36) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| USB | on-chip | Nuvoton NuMaker USB 1.1 device controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m46x.dtsi?plain=1#L605) | [`nuvoton,numaker-usbd`](../../../../build/dts/api/bindings/usb/nuvoton%2Cnumaker-usbd.md#std-dtcompatible-nuvoton-numaker-usbd) |
| Watchdog | on-chip | Nuvoton, NuMaker window watchdog timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m46x.dtsi?plain=1#L618) | [`nuvoton,numaker-wwdt`](../../../../build/dts/api/bindings/watchdog/nuvoton%2Cnumaker-wwdt.md#std-dtcompatible-nuvoton-numaker-wwdt) |

The on-board 12-MHz crystal allows the device to run at its maximum operating speed of 200MHz.

More details about the supported peripherals are available in [M460 TRM](https://www.nuvoton.com/export/resource-files/TRM_M460_Series_EN_Rev1.01.pdf) [[2]](#id4)

## Building and Flashing

The `numaker_pfm_m467` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

On board debugger Nu-link2 can emulate UART0 as a virtual COM port over usb,
To enable this, set ISW1 DIP switch 1-3 (TXD RXD VOM) to ON.
Connect the PFM M467 IoT to your host computer using the USB port, then
run a serial host program to connect with your board. For example:

```shell
$ minicom -D /dev/ttyACM0
```

```shell
# From the root of the zephyr repository
west build -b numaker_pfm_m467 samples/hello_world
west flash
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b numaker_pfm_m467 samples/hello_world
west debug
```

Step through the application in your debugger.

## References

[[1](#id3)]

[https://www.nuvoton.com/export/resource-files/UM\_NuMaker-PFM-M467\_User\_Manual\_EN\_Rev1.01.pdf](https://www.nuvoton.com/export/resource-files/UM_NuMaker-PFM-M467_User_Manual_EN_Rev1.01.pdf)

[[2](#id5)]

[https://www.nuvoton.com/export/resource-files/TRM\_M460\_Series\_EN\_Rev1.01.pdf](https://www.nuvoton.com/export/resource-files/TRM_M460_Series_EN_Rev1.01.pdf)

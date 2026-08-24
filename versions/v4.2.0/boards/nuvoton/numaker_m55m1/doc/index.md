---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nuvoton/numaker_m55m1/doc/index.html
original_path: boards/nuvoton/numaker_m55m1/doc/index.html
---

# NUMAKER M55M1

Board Overview

[![../../../../_images/m55m1.webp](https://docs.zephyrproject.org/4.2.0/_images/m55m1.webp)
](https://docs.zephyrproject.org/4.2.0/_images/m55m1.webp)

NUMAKER M55M1

Name:
:   `numaker_m55m1`

Vendor:
:   Nuvoton Technology Corporation

Architecture:
:   arm

SoC:
:   m55m1xxx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nuvoton/numaker_m55m1/doc/index.rst/../..)

## Overview

The NuMaker M55M1 is an Internet of Things (IoT) application focused platform
specially developed by Nuvoton. The NuMaker-M55M1 is based on the NuMicro® M55M1
series MCU with ARM® -Cortex®-M55 core.

### Features

- 32-bit Arm Cortex®-M55 M55M1H2LJAE MCU
- Core clock up to 220 MHz
- 2 MB embedded Dual Bank Flash and 1344 KB SRAM
- 128 KB DTCM and 64 KB ITCM
- USB 2.0 Full-Speed OTG / Device
- USB 1.1 Host
- Arduino UNO compatible interface
- One push-button is for reset
- Two LEDs: one is for power indication and the other is for user-defined
- On-board NU-Link2 ICE debugger/programmer with SWD connector

More information about the board can be found at the [NuMaker M55M1 User Manual](https://www.nuvoton.com/products/microcontrollers/arm-cortex-m55-mcus/m55m1-series/) [[1]](#id2).

### Supported Features

The `numaker_m55m1` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `numaker_m55m1/m55m1xxx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M55 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m55m1x.dtsi?plain=1#L29) | [`arm,cortex-m55`](../../../../build/dts/api/bindings/cpu/arm,cortex-m55.md#std-dtcompatible-arm-cortex-m55) |
| ADC | on-chip | Nuvoton, NuMaker ADC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m55m1x.dtsi?plain=1#L428) | [`nuvoton,numaker-adc`](../../../../build/dts/api/bindings/adc/nuvoton,numaker-adc.md#std-dtcompatible-nuvoton-numaker-adc) |
| CAN | on-chip | Nuvoton NuMaker CAN FD controller, using Bosch M\_CAN IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m55m1x.dtsi?plain=1#L342)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m55m1x.dtsi?plain=1#L356) | [`nuvoton,numaker-canfd`](../../../../build/dts/api/bindings/can/nuvoton,numaker-canfd.md#std-dtcompatible-nuvoton-numaker-canfd) |
| Clock control | on-chip | Nuvoton NuMaker System Clock Controller (SCC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m55m1x.dtsi?plain=1#L43) | [`nuvoton,numaker-scc`](../../../../build/dts/api/bindings/clock/nuvoton,numaker-scc.md#std-dtcompatible-nuvoton-numaker-scc) |
| on-chip | Nuvoton NuMaker Peripheral Clock Controller (PCC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m55m1x.dtsi?plain=1#L57) | [`nuvoton,numaker-pcc`](../../../../build/dts/api/bindings/clock/nuvoton,numaker-pcc.md#std-dtcompatible-nuvoton-numaker-pcc) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m55m1x.dtsi?plain=1#L36) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Ethernet | on-chip | Nuvoton, NuMaker Ethernet controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m55m1x.dtsi?plain=1#L370) | [`nuvoton,numaker-ethernet`](../../../../build/dts/api/bindings/ethernet/nuvoton,numaker-ethernet.md#std-dtcompatible-nuvoton-numaker-ethernet) |
| Flash controller | on-chip | Nuvoton NuMaker Flash Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m55m1x.dtsi?plain=1#L69) | [`nuvoton,numaker-fmc`](../../../../build/dts/api/bindings/flash_controller/nuvoton,numaker-fmc.md#std-dtcompatible-nuvoton-numaker-fmc) |
| GPIO & Headers | on-chip | Nuvoton Numaker GPIO[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m55m1x.dtsi?plain=1#L219)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m55m1x.dtsi?plain=1#L189) | [`nuvoton,numaker-gpio`](../../../../build/dts/api/bindings/gpio/nuvoton,numaker-gpio.md#std-dtcompatible-nuvoton-numaker-gpio) |
| I2C | on-chip | Nuvoton, NuMaker I2C controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m55m1x.dtsi?plain=1#L380) | [`nuvoton,numaker-i2c`](../../../../build/dts/api/bindings/i2c/nuvoton,numaker-i2c.md#std-dtcompatible-nuvoton-numaker-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nuvoton/numaker_m55m1/numaker_m55m1.dts?plain=1#L49) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8.1-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L17) | [`arm,v8.1m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8.1m-nvic.md#std-dtcompatible-arm-v8.1m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nuvoton/numaker_m55m1/numaker_m55m1.dts?plain=1#L35) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m55m1x.dtsi?plain=1#L75) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nuvoton/numaker_m55m1/numaker_m55m1.dts?plain=1#L81) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Pin controller is responsible for controlling pin function selection and pin properties[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m55m1x.dtsi?plain=1#L182) | [`nuvoton,numaker-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nuvoton,numaker-pinctrl.md#std-dtcompatible-nuvoton-numaker-pinctrl) |
| PWM | on-chip | Nuvoton, NuMaker PWM controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m55m1x.dtsi?plain=1#L441) | [`nuvoton,numaker-pwm`](../../../../build/dts/api/bindings/pwm/nuvoton,numaker-pwm.md#std-dtcompatible-nuvoton-numaker-pwm) |
| Reset controller | on-chip | Nuvoton, Numaker-RESET[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m55m1x.dtsi?plain=1#L63) | [`nuvoton,numaker-rst`](../../../../build/dts/api/bindings/reset/nuvoton,numaker-rst.md#std-dtcompatible-nuvoton-numaker-rst) |
| RTC | on-chip | Nuvoton, NuMaker RTC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m55m1x.dtsi?plain=1#L289) | [`nuvoton,numaker-rtc`](../../../../build/dts/api/bindings/rtc/nuvoton,numaker-rtc.md#std-dtcompatible-nuvoton-numaker-rtc) |
| Serial controller | on-chip | Nuvoton, Numaker-UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m55m1x.dtsi?plain=1#L82)[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m55m1x.dtsi?plain=1#L92) | [`nuvoton,numaker-uart`](../../../../build/dts/api/bindings/serial/nuvoton,numaker-uart.md#std-dtcompatible-nuvoton-numaker-uart) |
| SPI | on-chip | Nuvoton, NuMaker SPI controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m55m1x.dtsi?plain=1#L298) | [`nuvoton,numaker-spi`](../../../../build/dts/api/bindings/spi/nuvoton,numaker-spi.md#std-dtcompatible-nuvoton-numaker-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m55m1h2l.dtsi?plain=1#L11) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8.1-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L25) | [`arm,armv8.1m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8.1m-systick.md#std-dtcompatible-arm-armv8.1m-systick) |
| USB | on-chip | Nuvoton NuMaker USB 1.1 device controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m55m1x.dtsi?plain=1#L465) | [`nuvoton,numaker-usbd`](../../../../build/dts/api/bindings/usb/nuvoton,numaker-usbd.md#std-dtcompatible-nuvoton-numaker-usbd) |
| Watchdog | on-chip | Nuvoton, NuMaker window watchdog timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nuvoton/m55m1x.dtsi?plain=1#L478) | [`nuvoton,numaker-wwdt`](../../../../build/dts/api/bindings/watchdog/nuvoton,numaker-wwdt.md#std-dtcompatible-nuvoton-numaker-wwdt) |

The on-board 12-MHz crystal allows the device to run at its maximum operating speed of 220 MHz.

More details about the supported peripherals are available in [M55M1 TRM](https://www.nuvoton.com/products/microcontrollers/arm-cortex-m55-mcus/m55m1-series/) [[1]](#id2)

## Building and Flashing

The `numaker_m55m1` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

On board debugger Nu-link2 can emulate UART0 as a virtual COM port over usb,
To enable this, set ISW1 DIP switch 1-3 (TXD RXD VOM) to ON.
Connect the NuMaker-M55M1 to your host computer using the USB port, then
run a serial host program to connect with your board. For example:

```shell
$ minicom -D /dev/ttyACM0
```

```shell
# From the root of the zephyr repository
west build -b numaker_m55m1 samples/hello_world
west flash
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b numaker_m55m1 samples/hello_world
west debug
```

Step through the application in your debugger.

## References

[1]
([1](#id3),[2](#id4))

[https://www.nuvoton.com/products/microcontrollers/arm-cortex-m55-mcus/m55m1-series/](https://www.nuvoton.com/products/microcontrollers/arm-cortex-m55-mcus/m55m1-series/)

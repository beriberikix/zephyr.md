---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/ambiq/apollo4p_blue_kxr_evb/doc/index.html
original_path: boards/ambiq/apollo4p_blue_kxr_evb/doc/index.html
---

# Apollo4 Blue Plus KXR EVB

Board Overview

[![../../../../_images/apollo4-blue-plus-kxr-soc-eval-board.jpg](https://docs.zephyrproject.org/4.2.0/_images/apollo4-blue-plus-kxr-soc-eval-board.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/apollo4-blue-plus-kxr-soc-eval-board.jpg)

Apollo4 Blue Plus KXR EVB

Name:
:   `apollo4p_blue_kxr_evb`

Vendor:
:   Ambiq Micro, Inc.

Architecture:
:   arm

SoC:
:   apollo4p\_blue

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ambiq/apollo4p_blue_kxr_evb/doc/index.rst/../..)

Apollo4 Blue Plus KXR EVB is a board by Ambiq featuring their ultra-low power Apollo4 Blue Plus SoC.

## Hardware

- Apollo4 Blue Plus SoC with upto 192 MHz operating frequency
- ARM® Cortex® M4F core
- 64 kB 2-way Associative/Direct-Mapped Cache per core
- Up to 2 MB of non-volatile memory (NVM) for code/data
- Up to 2.75 MB of low leakage / low power RAM for code/data
- 384 kB Tightly Coupled RAM
- 384 kB Extended RAM
- Bluetooth 5.1 Low Energy

For more information about the Apollo4 Blue Plus SoC and Apollo4 Blue Plus KXR EVB board:

- [Apollo4 Blue Plus Website](https://ambiq.com/apollo4-blue-plus/)
- [Apollo4 Blue Plus Datasheet](https://contentportal.ambiq.com/documents/20123/388410/Apollo4-Blue-Plus-SoC-Datasheet.pdf)
- [Apollo4 Blue Plus KXR EVB Website](https://www.ambiq.top/en/apollo4-blue-plus-kxr-soc-eval-board)

### Supported Features

The `apollo4p_blue_kxr_evb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `apollo4p_blue_kxr_evb/apollo4p_blue` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p_blue.dtsi?plain=1#L32) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| Bluetooth | on-chip | Bluetooth module that uses Ambiq’s Bluetooth Host Controller Interface SPI driver (e.g[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p_blue.dtsi?plain=1#L225) | [`ambiq,bt-hci-spi`](../../../../build/dts/api/bindings/bluetooth/ambiq,bt-hci-spi.md#std-dtcompatible-ambiq-bt-hci-spi) |
| Clock control | on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p_blue.dtsi?plain=1#L11) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Ambiq Apollo Series SoC Clock Controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p_blue.dtsi?plain=1#L16) | [`ambiq,clkctrl`](../../../../build/dts/api/bindings/clock/ambiq,clkctrl.md#std-dtcompatible-ambiq-clkctrl) |
| Counter | on-chip | Ambiq Timer/Counter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p_blue.dtsi?plain=1#L83) | [`ambiq,counter`](../../../../build/dts/api/bindings/counter/ambiq,counter.md#std-dtcompatible-ambiq-counter) |
| Debug | on-chip | ARMv7 instrumentation trace macrocell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p_blue.dtsi?plain=1#L38) | [`arm,armv7m-itm`](../../../../build/dts/api/bindings/debug/arm,armv7m-itm.md#std-dtcompatible-arm-armv7m-itm) |
| Flash controller | on-chip | Ambiq flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p_blue.dtsi?plain=1#L62) | [`ambiq,flash-controller`](../../../../build/dts/api/bindings/flash_controller/ambiq,flash-controller.md#std-dtcompatible-ambiq-flash-controller) |
| GPIO & Headers | on-chip | Ambiq GPIO provides the GPIO pin mapping for GPIO child nodes[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p_blue.dtsi?plain=1#L349) | [`ambiq,gpio`](../../../../build/dts/api/bindings/gpio/ambiq,gpio.md#std-dtcompatible-ambiq-gpio) |
| on-chip | Ambiq GPIO bank[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p_blue.dtsi?plain=1#L365) | [`ambiq,gpio-bank`](../../../../build/dts/api/bindings/gpio/ambiq,gpio-bank.md#std-dtcompatible-ambiq-gpio-bank) |
| I2C | on-chip | Ambiq I2C[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p_blue.dtsi?plain=1#L139) | [`ambiq,i2c`](../../../../build/dts/api/bindings/i2c/ambiq,i2c.md#std-dtcompatible-ambiq-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ambiq/apollo4p_blue_kxr_evb/apollo4p_blue_kxr_evb.dts?plain=1#L47) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ambiq/apollo4p_blue_kxr_evb/apollo4p_blue_kxr_evb.dts?plain=1#L31) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Multi-Function Device | on-chip | Ambiq SPI/I2C controller common properties[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p_blue.dtsi?plain=1#L127) | [`ambiq,iom`](../../../../build/dts/api/bindings/mfd/ambiq,iom.md#std-dtcompatible-ambiq-iom) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p_blue.dtsi?plain=1#L70) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ambiq/apollo4p_blue_kxr_evb/apollo4p_blue_kxr_evb.dts?plain=1#L130) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Ambiq Apollo4 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p_blue.dtsi?plain=1#L343) | [`ambiq,apollo4-pinctrl`](../../../../build/dts/api/bindings/pinctrl/ambiq,apollo4-pinctrl.md#std-dtcompatible-ambiq-apollo4-pinctrl) |
| RTC | on-chip | AMBIQ RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p_blue.dtsi?plain=1#L335) | [`ambiq,rtc`](../../../../build/dts/api/bindings/rtc/ambiq,rtc.md#std-dtcompatible-ambiq-rtc) |
| Serial controller | on-chip | Ambiq UART controller (PL011 compatible)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p_blue.dtsi?plain=1#L92)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p_blue.dtsi?plain=1#L100) | [`ambiq,pl011-uart`](../../../../build/dts/api/bindings/serial/ambiq,pl011-uart.md#std-dtcompatible-ambiq-pl011-uart) |
| SPI | on-chip | Ambiq SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p_blue.dtsi?plain=1#L216)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p_blue.dtsi?plain=1#L132) | [`ambiq,spi`](../../../../build/dts/api/bindings/spi/ambiq,spi.md#std-dtcompatible-ambiq-spi) |
| on-chip | Ambiq MSPI[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p_blue.dtsi?plain=1#L299) | [`ambiq,mspi`](../../../../build/dts/api/bindings/spi/ambiq,mspi.md#std-dtcompatible-ambiq-mspi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p_blue.dtsi?plain=1#L54) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | Ambiq STIMER[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p_blue.dtsi?plain=1#L76) | [`ambiq,stimer`](../../../../build/dts/api/bindings/timer/ambiq,stimer.md#std-dtcompatible-ambiq-stimer) |
| USB | on-chip | Ambiq USB[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p_blue.dtsi?plain=1#L326) | [`ambiq,usb`](../../../../build/dts/api/bindings/usb/ambiq,usb.md#std-dtcompatible-ambiq-usb) |
| Watchdog | on-chip | Ambiq Watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p_blue.dtsi?plain=1#L403) | [`ambiq,watchdog`](../../../../build/dts/api/bindings/watchdog/ambiq,watchdog.md#std-dtcompatible-ambiq-watchdog) |

### Programming and Debugging

The `apollo4p_blue_kxr_evb` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

#### Flashing an application

Connect your device to your host computer using the JLINK USB port.
The sample application [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") is used for this example.
Build the Zephyr kernel and application, then flash it to the device:

```shell
# From the root of the zephyr repository
west build -b apollo4p_blue_kxr_evb samples/hello_world
west flash
```

Note

`west flash` requires [SEGGER J-Link software](https://www.segger.com/downloads/jlink) and [pylink](https://github.com/Square/pylink) Python module
to be installed on you host computer.

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you should be able to see on the corresponding Serial Port
the following message:

```shell
Hello World! apollo4p_blue_kxr_evb
```

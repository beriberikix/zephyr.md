---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/ambiq/apollo4p_evb/doc/index.html
original_path: boards/ambiq/apollo4p_evb/doc/index.html
---

# Apollo4P EVB

Board Overview

[![../../../../_images/apollo4-plus-soc-eval-board.jpg](https://docs.zephyrproject.org/4.2.0/_images/apollo4-plus-soc-eval-board.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/apollo4-plus-soc-eval-board.jpg)

Apollo4P EVB

Name:
:   `apollo4p_evb`

Vendor:
:   Ambiq Micro, Inc.

Architecture:
:   arm

SoC:
:   apollo4p

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ambiq/apollo4p_evb/doc/index.rst/../..)

Apollo4P EVB is a board by Ambiq featuring their ultra-low power Apollo4 Plus SoC.

## Hardware

- Apollo4 Plus SoC with upto 192 MHz operating frequency
- ARM® Cortex® M4F core
- 64 kB 2-way Associative/Direct-Mapped Cache per core
- Up to 2 MB of non-volatile memory (NVM) for code/data
- Up to 2.75 MB of low leakage / low power RAM for code/data
- 384 kB Tightly Coupled RAM
- 384 kB Extended RAM

For more information about the Apollo4 Plus SoC and Apollo4P EVB board:

- [Apollo4 Plus Website](https://ambiq.com/apollo4-plus/)
- [Apollo4 Plus Datasheet](https://contentportal.ambiq.com/documents/20123/388415/Apollo4-Plus-SoC-Datasheet.pdf)
- [Apollo4P EVB Website](https://www.ambiq.top/en/apollo4-plus-soc-eval-board)

### Supported Features

The `apollo4p_evb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `apollo4p_evb/apollo4p` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p.dtsi?plain=1#L23) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | Ambiq ADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p.dtsi?plain=1#L315) | [`ambiq,adc`](../../../../build/dts/api/bindings/adc/ambiq%2Cadc.md#std-dtcompatible-ambiq-adc) |
| Clock control | on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p.dtsi?plain=1#L12) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | Ambiq Timer/Counter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p.dtsi?plain=1#L102) | [`ambiq,counter`](../../../../build/dts/api/bindings/counter/ambiq%2Ccounter.md#std-dtcompatible-ambiq-counter) |
| Debug | on-chip | ARMv7 instrumentation trace macrocell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p.dtsi?plain=1#L30) | [`arm,armv7m-itm`](../../../../build/dts/api/bindings/debug/arm%2Carmv7m-itm.md#std-dtcompatible-arm-armv7m-itm) |
| Flash controller | on-chip | Ambiq flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p.dtsi?plain=1#L81) | [`ambiq,flash-controller`](../../../../build/dts/api/bindings/flash_controller/ambiq%2Cflash-controller.md#std-dtcompatible-ambiq-flash-controller) |
| GPIO & Headers | on-chip | Ambiq GPIO provides the GPIO pin mapping for GPIO child nodes[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p.dtsi?plain=1#L387) | [`ambiq,gpio`](../../../../build/dts/api/bindings/gpio/ambiq%2Cgpio.md#std-dtcompatible-ambiq-gpio) |
| on-chip | Ambiq GPIO bank[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p.dtsi?plain=1#L403) | [`ambiq,gpio-bank`](../../../../build/dts/api/bindings/gpio/ambiq%2Cgpio-bank.md#std-dtcompatible-ambiq-gpio-bank) |
| on-board | GPIO pins exposed on Ambiq Apollo4p EVB headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ambiq/apollo4p_evb/apollo4p_evb_connector.dtsi?plain=1#L8) | [`ambiq-header`](../../../../build/dts/api/bindings/gpio/ambiq-header.md#std-dtcompatible-ambiq-header) |
| I2C | on-chip | Ambiq I2C[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p.dtsi?plain=1#L159) | [`ambiq,i2c`](../../../../build/dts/api/bindings/i2c/ambiq%2Ci2c.md#std-dtcompatible-ambiq-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ambiq/apollo4p_evb/apollo4p_evb.dts?plain=1#L46) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ambiq/apollo4p_evb/apollo4p_evb.dts?plain=1#L30) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Multi-Function Device | on-chip | Ambiq SPI/I2C controller common properties[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p.dtsi?plain=1#L147) | [`ambiq,iom`](../../../../build/dts/api/bindings/mfd/ambiq%2Ciom.md#std-dtcompatible-ambiq-iom) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p.dtsi?plain=1#L89) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ambiq/apollo4p_evb/apollo4p_evb.dts?plain=1#L139) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Ambiq Apollo4 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p.dtsi?plain=1#L381) | [`ambiq,apollo4-pinctrl`](../../../../build/dts/api/bindings/pinctrl/ambiq%2Capollo4-pinctrl.md#std-dtcompatible-ambiq-apollo4-pinctrl) |
| RTC | on-chip | AMBIQ RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p.dtsi?plain=1#L353) | [`ambiq,rtc`](../../../../build/dts/api/bindings/rtc/ambiq%2Crtc.md#std-dtcompatible-ambiq-rtc) |
| SDHC | on-chip | Ambiq SDIO host controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p.dtsi?plain=1#L361) | [`ambiq,sdio`](../../../../build/dts/api/bindings/sdhc/ambiq%2Csdhc.md#std-dtcompatible-ambiq-sdio) |
| Serial controller | on-chip | Ambiq UART controller (PL011 compatible)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p.dtsi?plain=1#L111)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p.dtsi?plain=1#L120) | [`ambiq,pl011-uart`](../../../../build/dts/api/bindings/serial/ambiq%2Cpl011-uart.md#std-dtcompatible-ambiq-pl011-uart) |
| SPI | on-chip | Ambiq SPI[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p.dtsi?plain=1#L152) | [`ambiq,spi`](../../../../build/dts/api/bindings/spi/ambiq%2Cspi.md#std-dtcompatible-ambiq-spi) |
| on-chip | Ambiq MSPI[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p.dtsi?plain=1#L326) | [`ambiq,mspi`](../../../../build/dts/api/bindings/spi/ambiq%2Cmspi.md#std-dtcompatible-ambiq-mspi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p.dtsi?plain=1#L73) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | Ambiq STIMER[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p.dtsi?plain=1#L95) | [`ambiq,stimer`](../../../../build/dts/api/bindings/timer/ambiq%2Cstimer.md#std-dtcompatible-ambiq-stimer) |
| USB | on-chip | Ambiq USB[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p.dtsi?plain=1#L372) | [`ambiq,usb`](../../../../build/dts/api/bindings/usb/ambiq%2Cusb.md#std-dtcompatible-ambiq-usb) |
| Watchdog | on-chip | Ambiq Watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo4p.dtsi?plain=1#L441) | [`ambiq,watchdog`](../../../../build/dts/api/bindings/watchdog/ambiq%2Cwatchdog.md#std-dtcompatible-ambiq-watchdog) |

### Programming and Debugging

The `apollo4p_evb` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

#### Flashing an application

Connect your device to your host computer using the JLINK USB port.
The sample application [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") is used for this example.
Build the Zephyr kernel and application, then flash it to the device:

```shell
# From the root of the zephyr repository
west build -b apollo4p_evb samples/hello_world
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
Hello World! apollo4p_evb
```

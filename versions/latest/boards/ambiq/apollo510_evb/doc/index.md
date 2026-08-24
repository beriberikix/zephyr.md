---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/ambiq/apollo510_evb/doc/index.html
original_path: boards/ambiq/apollo510_evb/doc/index.html
---

# Apollo510 SOC Evaluation Board

Board Overview

[![../../../../_images/apollo510-soc-eval-board.jpg](https://docs.zephyrproject.org/4.2.0/_images/apollo510-soc-eval-board.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/apollo510-soc-eval-board.jpg)

Apollo510 SOC Evaluation Board

Name:
:   `apollo510_evb`

Vendor:
:   Ambiq Micro, Inc.

Architecture:
:   arm

SoC:
:   apollo510

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ambiq/apollo510_evb/doc/index.rst/../..)

Apollo510 EVB is a board by Ambiq featuring their ultra-low power Apollo510 SoC.

## Hardware

- Apollo510 SoC with up to 250 MHz operating frequency
- ARM® Cortex® M55 core
- 64 kB Instruction Cache and 64 kB Data Cache
- Up to 4 MB of non-volatile memory (NVM) for code/data
- Up to 3 MB of low leakage / low power RAM for code/data
- 256 kB Instruction Tightly Coupled RAM (ITCM)
- 512 kB Data Tightly Coupled RAM (DTCM)

For more information about the Apollo510 SoC and Apollo510 EVB board:

- [Apollo510 Website](https://ambiq.com/apollo510/)
- [Apollo510 Datasheet](https://contentportal.ambiq.com/documents/20123/2877485/Apollo510-SoC-Datasheet.pdf)
- [Apollo510 EVB Website](https://docs.zephyrproject.org/4.2.0/boards/ambiq/apollo510_evb/doc/Formoreinformation,pleasereachouttoSalesandFAE.)

### Supported Features

The `apollo510_evb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `apollo510_evb/apollo510` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M55 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo510.dtsi?plain=1#L50) | [`arm,cortex-m55`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m55.md#std-dtcompatible-arm-cortex-m55) |
| ADC | on-chip | Ambiq ADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo510.dtsi?plain=1#L571) | [`ambiq,adc`](../../../../build/dts/api/bindings/adc/ambiq%2Cadc.md#std-dtcompatible-ambiq-adc) |
| Audio | on-chip | Ambiq PDM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo510.dtsi?plain=1#L507) | [`ambiq,pdm`](../../../../build/dts/api/bindings/audio/ambiq%2Cpdm.md#std-dtcompatible-ambiq-pdm) |
| Clock control | on-chip | Generic fixed-rate clock provider[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo510.dtsi?plain=1#L15) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | Ambiq Timer/Counter[14 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo510.dtsi?plain=1#L146) | [`ambiq,counter`](../../../../build/dts/api/bindings/counter/ambiq%2Ccounter.md#std-dtcompatible-ambiq-counter) |
| Debug | on-chip | ARMv8 instrumentation trace macrocell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo510.dtsi?plain=1#L58) | [`arm,armv8m-itm`](../../../../build/dts/api/bindings/debug/arm%2Carmv8m-itm.md#std-dtcompatible-arm-armv8m-itm) |
| GPIO & Headers | on-chip | Ambiq GPIO provides the GPIO pin mapping for GPIO child nodes[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo510.dtsi?plain=1#L588) | [`ambiq,gpio`](../../../../build/dts/api/bindings/gpio/ambiq%2Cgpio.md#std-dtcompatible-ambiq-gpio) |
| on-chip | Ambiq GPIO bank[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo510.dtsi?plain=1#L607) | [`ambiq,gpio-bank`](../../../../build/dts/api/bindings/gpio/ambiq%2Cgpio-bank.md#std-dtcompatible-ambiq-gpio-bank) |
| I2C | on-chip | Ambiq I2C[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo510.dtsi?plain=1#L310) | [`ambiq,i2c`](../../../../build/dts/api/bindings/i2c/ambiq%2Ci2c.md#std-dtcompatible-ambiq-i2c) |
| I2S | on-chip | Ambiq I2S[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo510.dtsi?plain=1#L514) | [`ambiq,i2s`](../../../../build/dts/api/bindings/i2s/ambiq%2Ci2s.md#std-dtcompatible-ambiq-i2s) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ambiq/apollo510_evb/apollo510_evb.dts?plain=1#L63) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8.1-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L17) | [`arm,v8.1m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8.1m-nvic.md#std-dtcompatible-arm-v8.1m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ambiq/apollo510_evb/apollo510_evb.dts?plain=1#L44) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Multi-Function Device | on-chip | Ambiq SPI/I2C controller common properties[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo510.dtsi?plain=1#L298) | [`ambiq,iom`](../../../../build/dts/api/bindings/mfd/ambiq%2Ciom.md#std-dtcompatible-ambiq-iom) |
| Multi-bit SPI | on-chip | Ambiq MSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo510.dtsi?plain=1#L538)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo510.dtsi?plain=1#L527) | [`ambiq,mspi-controller`](../../../../build/dts/api/bindings/mspi/ambiq%2Cmspi-controller.md#std-dtcompatible-ambiq-mspi-controller) |
| on-board | Ambiq MSPI device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ambiq/apollo510_evb/apollo510_evb.dts?plain=1#L140) | [`ambiq,mspi-device`](../../../../build/dts/api/bindings/mspi/ambiq%2Cmspi-device.md#std-dtcompatible-ambiq-mspi-device) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo510.dtsi?plain=1#L88) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | Ambiq Apollo5 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo510.dtsi?plain=1#L582) | [`ambiq,apollo5-pinctrl`](../../../../build/dts/api/bindings/pinctrl/ambiq%2Capollo5-pinctrl.md#std-dtcompatible-ambiq-apollo5-pinctrl) |
| RTC | on-chip | AMBIQ RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo510.dtsi?plain=1#L272) | [`ambiq,rtc`](../../../../build/dts/api/bindings/rtc/ambiq%2Crtc.md#std-dtcompatible-ambiq-rtc) |
| Serial controller | on-chip | Ambiq UART controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo510.dtsi?plain=1#L466)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo510.dtsi?plain=1#L474) | [`ambiq,uart`](../../../../build/dts/api/bindings/serial/ambiq%2Cuart.md#std-dtcompatible-ambiq-uart) |
| SPI | on-chip | Ambiq SPI Device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo510.dtsi?plain=1#L288) | [`ambiq,spid`](../../../../build/dts/api/bindings/spi/ambiq%2Cspid.md#std-dtcompatible-ambiq-spid) |
| on-chip | Ambiq SPI[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo510.dtsi?plain=1#L303) | [`ambiq,spi`](../../../../build/dts/api/bindings/spi/ambiq%2Cspi.md#std-dtcompatible-ambiq-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo510.dtsi?plain=1#L107) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8.1-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L25) | [`arm,armv8.1m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8.1m-systick.md#std-dtcompatible-arm-armv8.1m-systick) |
| on-chip | Ambiq STIMER[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo510.dtsi?plain=1#L139) | [`ambiq,stimer`](../../../../build/dts/api/bindings/timer/ambiq%2Cstimer.md#std-dtcompatible-ambiq-stimer) |
| USB | on-chip | Ambiq USB[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo510.dtsi?plain=1#L498) | [`ambiq,usb`](../../../../build/dts/api/bindings/usb/ambiq%2Cusb.md#std-dtcompatible-ambiq-usb) |
| Watchdog | on-chip | Ambiq Watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo510.dtsi?plain=1#L280) | [`ambiq,watchdog`](../../../../build/dts/api/bindings/watchdog/ambiq%2Cwatchdog.md#std-dtcompatible-ambiq-watchdog) |

### Programming and Debugging

The `apollo510_evb` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

#### Flashing an application

Connect your device to your host computer using the JLINK USB port.
The sample application [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") is used for this example.
Build the Zephyr kernel and application, then flash it to the device:

```shell
# From the root of the zephyr repository
west build -b apollo510_evb samples/hello_world
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
Hello World! apollo510_evb
```

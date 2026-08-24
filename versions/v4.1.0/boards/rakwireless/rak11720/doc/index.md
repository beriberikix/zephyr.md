---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/rakwireless/rak11720/doc/index.html
original_path: boards/rakwireless/rak11720/doc/index.html
---

# RAK11720

Board Overview

[![../../../../_images/rak11720.webp](https://docs.zephyrproject.org/4.1.0/_images/rak11720.webp)
](https://docs.zephyrproject.org/4.1.0/_images/rak11720.webp)

RAK11720

Name:
:   `rak11720`

Vendor:
:   RAKwireless Technology Limited

Architecture:
:   arm

SoC:
:   apollo3\_blue

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/rakwireless/rak11720/doc/index.rst/../..)

The RAK11720 is a WisBlock Core module for RAK WisBlock.
It is based on the powerful ultra-low power Apollo3 Blue SoC (AMA3B1KK-KBR-B0)
from Ambiq together with a Semtech SX1262 LoRa® transceiver.

The AMA3B1KK-KBR-B0 has an integrated Bluetooth Low Energy transceiver
that enhances the communication capabilities. The RAK11720 stamp module
comes in the same size and footprint as our RAK3172 module which gives
you the opportunity to enhance your existing designs
with BLE without designing a new PCB.

## Hardware

The easiset way to use a RAK11720, is the WisBlock Modular system.
A WisBlock Base board (RAK19007) which provides the power
supply and programming/debug interface is the base to plug a
RAK11722 (WisBlock Core module with the RAK11720) in.

- Apollo3 Blue SoC with up to 96 MHz operating frequency
- ARM® Cortex® M4F core
- 16 kB 2-way Associative/Direct-Mapped Cache per core
- Up to 1 MB of flash memory for code/data
- Up to 384 KB of low leakage / low power RAM for code/data
- Integrated Bluetooth 5 Low-energy controller
- Semtech SX1262 low power high range LoRa transceiver
- iPEX connectors for the LORA antenna and BLE antenna.
- 2 user LEDs on RAK19007 WisBlock Base board
- Powered by either Micro USB, 3.7V rechargeable battery or a 5V Solar Panel Port

For more information about the RAK11720 stamp module:

- [WisDuo RAK11720 Website](https://docs.rakwireless.com/Product-Categories/WisDuo/RAK11720-Module/Overview/#product-description)
- [WisBlock RAK11722 Website](https://docs.rakwireless.com/Product-Categories/WisBlock/RAK11722/Overview/#product-description)

### Supported Features

The `rak11720` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `rak11720/apollo3_blue` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo3_blue.dtsi?plain=1#L23) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | Ambiq ADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo3_blue.dtsi?plain=1#L343) | [`ambiq,adc`](../../../../build/dts/api/bindings/adc/ambiq,adc.md#std-dtcompatible-ambiq-adc) |
| Bluetooth | on-chip | Bluetooth module that uses Ambiq’s Bluetooth Host Controller Interface SPI driver (e.g[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo3_blue.dtsi?plain=1#L382) | [`ambiq,bt-hci-spi`](../../../../build/dts/api/bindings/bluetooth/ambiq,bt-hci-spi.md#std-dtcompatible-ambiq-bt-hci-spi) |
| Clock control | on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo3_blue.dtsi?plain=1#L12) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | Ambiq Timer/Counter[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo3_blue.dtsi?plain=1#L106) | [`ambiq,counter`](../../../../build/dts/api/bindings/counter/ambiq,counter.md#std-dtcompatible-ambiq-counter) |
| Debug | on-chip | ARMv7 instrumentation trace macrocell[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo3_blue.dtsi?plain=1#L30) | [`arm,armv7m-itm`](../../../../build/dts/api/bindings/debug/arm,armv7m-itm.md#std-dtcompatible-arm-armv7m-itm) |
| Flash controller | on-chip | Ambiq flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo3_blue.dtsi?plain=1#L79) | [`ambiq,flash-controller`](../../../../build/dts/api/bindings/flash_controller/ambiq,flash-controller.md#std-dtcompatible-ambiq-flash-controller) |
| GPIO & Headers | on-chip | Ambiq GPIO provides the GPIO pin mapping for GPIO child nodes[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo3_blue.dtsi?plain=1#L395) | [`ambiq,gpio`](../../../../build/dts/api/bindings/gpio/ambiq,gpio.md#std-dtcompatible-ambiq-gpio) |
| on-chip | Ambiq GPIO bank node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo3_blue.dtsi?plain=1#L409) | [`ambiq,gpio-bank`](../../../../build/dts/api/bindings/gpio/ambiq,gpio-bank.md#std-dtcompatible-ambiq-gpio-bank) |
| I2C | on-chip | Ambiq I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo3_blue.dtsi?plain=1#L299)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo3_blue.dtsi?plain=1#L277) | [`ambiq,i2c`](../../../../build/dts/api/bindings/i2c/ambiq,i2c.md#std-dtcompatible-ambiq-i2c) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/rakwireless/rak11720/rak11720.dts?plain=1#L39) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| LoRa | on-board | Semtech SX1262 LoRa Modem[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/rakwireless/rak11720/rak11720.dts?plain=1#L133) | [`semtech,sx1262`](../../../../build/dts/api/bindings/lora/semtech,sx1262.md#std-dtcompatible-semtech-sx1262) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo3_blue.dtsi?plain=1#L87) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/rakwireless/rak11720/rak11720.dts?plain=1#L56) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | The Ambiq Apollo3 pin controller is a node responsible for controlling pin function selection and pin properties, such as routing a UART0 TX to pin 60 and enabling the pullup resistor on that pin[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo3_blue.dtsi?plain=1#L389) | [`ambiq,apollo3-pinctrl`](../../../../build/dts/api/bindings/pinctrl/ambiq,apollo3-pinctrl.md#std-dtcompatible-ambiq-apollo3-pinctrl) |
| Power management | on-chip | Ambiq power control[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo3_blue.dtsi?plain=1#L93) | [`ambiq,pwrctrl`](../../../../build/dts/api/bindings/power/ambiq,pwrctrl.md#std-dtcompatible-ambiq-pwrctrl) |
| RTC | on-chip | AMBIQ RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo3_blue.dtsi?plain=1#L365) | [`ambiq,rtc`](../../../../build/dts/api/bindings/rtc/ambiq,rtc.md#std-dtcompatible-ambiq-rtc) |
| Serial controller | on-chip | Ambiq UART controller (PL011 compatible)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo3_blue.dtsi?plain=1#L178)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo3_blue.dtsi?plain=1#L189) | [`ambiq,uart`](../../../../build/dts/api/bindings/serial/ambiq,uart.md#std-dtcompatible-ambiq-uart) |
| SPI | on-chip | Ambiq SPI Device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo3_blue.dtsi?plain=1#L200) | [`ambiq,spid`](../../../../build/dts/api/bindings/spi/ambiq,spid.md#std-dtcompatible-ambiq-spid) |
| on-chip | Ambiq SPI[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo3_blue.dtsi?plain=1#L211)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo3_blue.dtsi?plain=1#L233) | [`ambiq,spi`](../../../../build/dts/api/bindings/spi/ambiq,spi.md#std-dtcompatible-ambiq-spi) |
| on-chip | Ambiq MSPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo3_blue.dtsi?plain=1#L355) | [`ambiq,mspi`](../../../../build/dts/api/bindings/spi/ambiq,mspi.md#std-dtcompatible-ambiq-mspi) |
| on-chip | This binding gives a representation of SPI controller in some Ambiq Apollox Blue SOC (e.g[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo3_blue.dtsi?plain=1#L373) | [`ambiq,spi-bleif`](../../../../build/dts/api/bindings/spi/ambiq,spi-bleif.md#std-dtcompatible-ambiq-spi-bleif) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo3_blue.dtsi?plain=1#L71) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | Ambiq STIMER[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo3_blue.dtsi?plain=1#L99) | [`ambiq,stimer`](../../../../build/dts/api/bindings/timer/ambiq,stimer.md#std-dtcompatible-ambiq-stimer) |
| Watchdog | on-chip | Ambiq Watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ambiq/ambiq_apollo3_blue.dtsi?plain=1#L430) | [`ambiq,watchdog`](../../../../build/dts/api/bindings/watchdog/ambiq,watchdog.md#std-dtcompatible-ambiq-watchdog) |

### Programming and Debugging

The RAK11720 board shall be connected to a Segger Embedded Debugger Unit
[J-Link OB](https://www.segger.com/jlink-ob.html). This provides a debug
interface to the Apollo3 Blue chip. You can use JLink to communicate with
the Apollo3 Blue.

#### Flashing an application

Connect your device to your host computer using the JLINK USB port.
The sample application [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") is used for this example.
Build the Zephyr kernel and application, then flash it to the device:

```shell
# From the root of the zephyr repository
west build -b rak11720 samples/hello_world
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
Hello World! rak11720/apollo3_blue
```

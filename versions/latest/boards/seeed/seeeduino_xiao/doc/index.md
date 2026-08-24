---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/seeed/seeeduino_xiao/doc/index.html
original_path: boards/seeed/seeeduino_xiao/doc/index.html
---

# Seeeduino XIAO

Board Overview

[![../../../../_images/seeeduino_xiao.jpg](https://docs.zephyrproject.org/4.2.0/_images/seeeduino_xiao.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/seeeduino_xiao.jpg)

Seeeduino XIAO

Name:
:   `seeeduino_xiao`

Vendor:
:   Seeed Technology Co., Ltd

Architecture:
:   arm

SoC:
:   samd21g18a

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/seeed/seeeduino_xiao/doc/index.rst/../..)

## Overview

The Seeeduino XIAO is a tiny (20 mm x 17.5 mm) ARM development
board with onboard LEDs, USB port, and range of I/O broken out
onto 14 pins.

## Hardware

- ATSAMD21G18A ARM Cortex-M0+ processor at 48 MHz
- 256 KiB flash memory and 32 KiB of RAM
- Three user LEDs
- Native USB port

### Supported Features

The `seeeduino_xiao` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `seeeduino_xiao/samd21g18a` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L44) | [`arm,cortex-m0+`](../../../../build/dts/api/bindings/cpu/arm,cortex-m0+.md#std-dtcompatible-arm-cortex-m0) |
| ADC | on-chip | Atmel SAM0 family ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L202) | [`atmel,sam0-adc`](../../../../build/dts/api/bindings/adc/atmel,sam0-adc.md#std-dtcompatible-atmel-sam0-adc) |
| ARM architecture | on-chip | Atmel SAM0 multi-protocol (UART, SPI, I2C) SERCOM unit[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L126) | [`atmel,sam0-sercom`](../../../../build/dts/api/bindings/arm/atmel,sam0-sercom.md#std-dtcompatible-atmel-sam0-sercom) |
| on-chip | For locating the Device ID (serial number) on Atmel SAM0 devices[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L56) | [`atmel,sam0-id`](../../../../build/dts/api/bindings/arm/atmel,sam0-id.md#std-dtcompatible-atmel-sam0-id) |
| Clock control | on-chip | Atmel SAM0 Main Clock Controller (MCLK)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L82) | [`atmel,sam0-mclk`](../../../../build/dts/api/bindings/clock/atmel,sam0-mclk.md#std-dtcompatible-atmel-sam0-mclk) |
| on-chip | Atmel SAMD0 Generic Clock Controller (GCLK)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L90) | [`atmel,sam0-gclk`](../../../../build/dts/api/bindings/clock/atmel,sam0-gclk.md#std-dtcompatible-atmel-sam0-gclk) |
| Counter | on-chip | Atmel SAM0 basic timer counter (TC) operating in 32-bit wide mode[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L156) | [`atmel,sam0-tc32`](../../../../build/dts/api/bindings/counter/atmel,sam0-tc32.md#std-dtcompatible-atmel-sam0-tc32) |
| DAC | on-chip | Atmel SAM0 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L212) | [`atmel,sam0-dac`](../../../../build/dts/api/bindings/dac/atmel,sam0-dac.md#std-dtcompatible-atmel-sam0-dac) |
| DMA | on-chip | Atmel SAM0 DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd21.dtsi?plain=1#L29) | [`atmel,sam0-dmac`](../../../../build/dts/api/bindings/dma/atmel,sam0-dmac.md#std-dtcompatible-atmel-sam0-dmac) |
| Flash controller | on-chip | Atmel SAM0 NVMC (Non-Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L65) | [`atmel,sam0-nvmctrl`](../../../../build/dts/api/bindings/flash_controller/atmel,sam0-nvmctrl.md#std-dtcompatible-atmel-sam0-nvmctrl) |
| GPIO & Headers | on-chip | SAM0 GPIO PORT node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L169) | [`atmel,sam0-gpio`](../../../../build/dts/api/bindings/gpio/atmel,sam0-gpio.md#std-dtcompatible-atmel-sam0-gpio) |
| on-board | GPIO pins exposed on Seeeduino Xiao (and compatible devices) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seeed/seeeduino_xiao/seeed_xiao_connector.dtsi?plain=1#L8) | [`seeed,xiao-gpio`](../../../../build/dts/api/bindings/gpio/seeed-xiao-header.md#std-dtcompatible-seeed-xiao-gpio) |
| I2C | on-chip | Atmel SAM0 series SERCOM I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L132) | [`atmel,sam0-i2c`](../../../../build/dts/api/bindings/i2c/atmel,sam0-i2c.md#std-dtcompatible-atmel-sam0-i2c) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| on-chip | Atmel SAM0 series External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L98) | [`atmel,sam0-eic`](../../../../build/dts/api/bindings/interrupt-controller/atmel,sam0-eic.md#std-dtcompatible-atmel-sam0-eic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seeed/seeeduino_xiao/seeeduino_xiao.dts?plain=1#L25) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L75) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seeed/seeeduino_xiao/seeeduino_xiao.dts?plain=1#L102) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Atmel SAM0 PINMUX[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L104) | [`atmel,sam0-pinmux`](../../../../build/dts/api/bindings/pinctrl/atmel,sam0-pinmux.md#std-dtcompatible-atmel-sam0-pinmux) |
| on-chip | Atmel SAM0 Pinctrl Container[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L162) | [`atmel,sam0-pinctrl`](../../../../build/dts/api/bindings/pinctrl/atmel,sam0-pinctrl.md#std-dtcompatible-atmel-sam0-pinctrl) |
| RTC | on-chip | Atmel SAM0 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L190) | [`atmel,sam0-rtc`](../../../../build/dts/api/bindings/rtc/atmel,sam0-rtc.md#std-dtcompatible-atmel-sam0-rtc) |
| Serial controller | on-chip | Atmel SAM0 SERCOM UART driver[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L144) | [`atmel,sam0-uart`](../../../../build/dts/api/bindings/serial/atmel,sam0-uart.md#std-dtcompatible-atmel-sam0-uart) |
| SPI | on-chip | Atmel SAM0 SERCOM SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L120) | [`atmel,sam0-spi`](../../../../build/dts/api/bindings/spi/atmel,sam0-spi.md#std-dtcompatible-atmel-sam0-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L52) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv6-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21) | [`arm,armv6m-systick`](../../../../build/dts/api/bindings/timer/arm,armv6m-systick.md#std-dtcompatible-arm-armv6m-systick) |
| USB | on-chip | Atmel SAM0 USB in device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd21.dtsi?plain=1#L20) | [`atmel,sam0-usb`](../../../../build/dts/api/bindings/usb/atmel,sam0-usb.md#std-dtcompatible-atmel-sam0-usb) |
| Watchdog | on-chip | Atmel SAM0 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L114) | [`atmel,sam0-watchdog`](../../../../build/dts/api/bindings/watchdog/atmel,sam0-watchdog.md#std-dtcompatible-atmel-sam0-watchdog) |

### Connections and IOs

The [Seeeduino XIAO wiki](https://wiki.seeedstudio.com/Seeeduino-XIAO/) [[1]](#id2) has detailed information about
the board including [pinouts](https://wiki.seeedstudio.com/Seeeduino-XIAO/#hardware-overview) [[2]](#id4) and the [schematic](https://wiki.seeedstudio.com/Seeeduino-XIAO/#resourses) [[3]](#id6).

### System Clock

The SAMD21 MCU is configured to use the 32 kHz external crystal
with the on-chip PLL generating the 48 MHz system clock. The internal
APB and GCLK unit are set up in the same way as the upstream Arduino
libraries.

### SPI Port

The SAMD21 MCU has 6 SERCOM based SPIs. On the XIAO, SERCOM0 can be put
into SPI mode and used to connect to devices over pin 9 (MISO), pin 10
(MOSI), and pin 8 (SCK).

### I2C Port

The SAMD21 MCU has 6 SERCOM based USARTs. On the XIAO, SERCOM2 is available on
pin 4 (SDA) and pin 5 (SCL).

### Serial Port

The SAMD21 MCU has 6 SERCOM based USARTs. On the XIAO, SERCOM4 is
the Zephyr console and is available on pins 7 (RX) and 6 (TX).

### USB Device Port

The SAMD21 MCU has a USB device port that can be used to communicate
with a host PC. See the [USB device support](../../../../samples/subsys/usb/usb.md#usb) sample applications for
more, such as the [USB CDC-ACM](../../../../samples/subsys/usb/cdc_acm/README.md#usb-cdc-acm "Use USB CDC-ACM driver to implement a serial port echo.") sample which sets up a virtual
serial port that echos characters back to the host PC.

### DAC

The SAMD21 MCU has a single channel DAC with 10 bits of resolution. On
the XIAO, the DAC is available on pin 0.

## Programming and Debugging

The `seeeduino_xiao` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[bossac](../../../../develop/flash_debug/host-tools.md#runner-bossac)** | ✅ (default) |  |  |  |  |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |

The XIAO ships the BOSSA compatible UF2 bootloader. The bootloader can be
entered by shorting the RST and GND pads twice.

Additionally, if `CONFIG_USB_CDC_ACM` is enabled then the bootloader
will be entered automatically when you run `west flash`.

### Flashing

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b seeeduino_xiao samples/hello_world
   ```
2. Connect the XIAO to your host computer using USB
3. Connect a 3.3 V USB to serial adapter to the board and to the
   host. See the [Serial Port](#serial-port) section above for the board’s pin
   connections.
4. Run your favorite terminal program to listen for output. Under Linux the
   terminal should be `/dev/ttyUSB0`. For example:

   ```shell
   $ minicom -D /dev/ttyUSB0 -o
   ```

   The -o option tells minicom not to send the modem initialization
   string. Connection should be configured as follows:

   - Speed: 115200
   - Data: 8 bits
   - Parity: None
   - Stop bits: 1
5. Short the RST and GND pads twice quickly to enter bootloader mode
6. Flash the image:

   ```shell
   west build -b seeeduino_xiao samples/hello_world
   west flash
   ```

   You should see “Hello World! seeeduino\_xiao” in your terminal.

## References

[[1](#id3)]

[https://wiki.seeedstudio.com/Seeeduino-XIAO/](https://wiki.seeedstudio.com/Seeeduino-XIAO/)

[[2](#id5)]

[https://wiki.seeedstudio.com/Seeeduino-XIAO/#hardware-overview](https://wiki.seeedstudio.com/Seeeduino-XIAO/#hardware-overview)

[[3](#id7)]

[https://wiki.seeedstudio.com/Seeeduino-XIAO/#resourses](https://wiki.seeedstudio.com/Seeeduino-XIAO/#resourses)

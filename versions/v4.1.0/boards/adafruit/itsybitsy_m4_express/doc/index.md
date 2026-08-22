---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/adafruit/itsybitsy_m4_express/doc/index.html
original_path: boards/adafruit/itsybitsy_m4_express/doc/index.html
---

# ItsyBitsy M4 Express

Board Overview

[![../../../../_images/adafruit_itsybitsy_m4_express.jpg](../../../../_images/adafruit_itsybitsy_m4_express.jpg)
](../../../../_images/adafruit_itsybitsy_m4_express.jpg)

ItsyBitsy M4 Express

Name:
:   `adafruit_itsybitsy_m4_express`

Vendor:
:   Adafruit Industries, LLC

Architecture:
:   arm

SoC:
:   samd51g19a

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adafruit/itsybitsy_m4_express/doc/index.rst/../..)

## Overview

The Adafruit ItsyBitsy M4 express is a small (36 mm x 18 mm) ARM development
board with an onboard RGB LED, USB port, 2 MiB of SPI flash, and range of I/O
broken out onto 23 GPIO pins.

## Hardware

- ATSAMD51G19A ARM Cortex-M4 processor at 120 MHz
- 512 KiB of flash memory and 192 KiB of RAM
- 2 MiB of SPI flash
- Internal trimmed 8 MHz oscillator
- A user LED
- An RGB DotStar LED
- Native USB port
- One reset button

### Supported Features

The `adafruit_itsybitsy_m4_express` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `adafruit_itsybitsy_m4_express/samd51g19a` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L59) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | Atmel SAM0 family ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L342) | [`atmel,sam0-adc`](../../../../build/dts/api/bindings/adc/atmel%2Csam0-adc.md#std-dtcompatible-atmel-sam0-adc) |
| ARM architecture | on-chip | For locating the Device ID (serial number) on Atmel SAM0 devices[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L86) | [`atmel,sam0-id`](../../../../build/dts/api/bindings/arm/atmel%2Csam0-id.md#std-dtcompatible-atmel-sam0-id) |
| on-chip | Atmel SAM0 multi-protocol (UART, SPI, I2C) SERCOM unit[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L177) | [`atmel,sam0-sercom`](../../../../build/dts/api/bindings/arm/atmel%2Csam0-sercom.md#std-dtcompatible-atmel-sam0-sercom) |
| Clock control | on-chip | Atmel SAM0 Main Clock Controller (MCLK)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L94) | [`atmel,sam0-mclk`](../../../../build/dts/api/bindings/clock/atmel%2Csam0-mclk.md#std-dtcompatible-atmel-sam0-mclk) |
| on-chip | Atmel SAM0 32kHz Oscillator Controller (OSC32KCTRL)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L101) | [`atmel,sam0-osc32kctrl`](../../../../build/dts/api/bindings/clock/atmel%2Csam0-osc32kctrl.md#std-dtcompatible-atmel-sam0-osc32kctrl) |
| on-chip | Atmel SAMD0 Generic Clock Controller (GCLK)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L108) | [`atmel,sam0-gclk`](../../../../build/dts/api/bindings/clock/atmel%2Csam0-gclk.md#std-dtcompatible-atmel-sam0-gclk) |
| Counter | on-chip | Atmel SAM0 basic timer counter (TC) operating in 32-bit wide mode[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L391) | [`atmel,sam0-tc32`](../../../../build/dts/api/bindings/counter/atmel%2Csam0-tc32.md#std-dtcompatible-atmel-sam0-tc32) |
| DMA | on-chip | Atmel SAM0 DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L133) | [`atmel,sam0-dmac`](../../../../build/dts/api/bindings/dma/atmel%2Csam0-dmac.md#std-dtcompatible-atmel-sam0-dmac) |
| Flash controller | on-chip | Atmel SAM0 NVMC (Non-Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L116) | [`atmel,sam0-nvmctrl`](../../../../build/dts/api/bindings/flash_controller/atmel%2Csam0-nvmctrl.md#std-dtcompatible-atmel-sam0-nvmctrl) |
| GPIO & Headers | on-chip | SAM0 GPIO PORT node[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L272) | [`atmel,sam0-gpio`](../../../../build/dts/api/bindings/gpio/atmel%2Csam0-gpio.md#std-dtcompatible-atmel-sam0-gpio) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | Atmel SAM0 series External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L142) | [`atmel,sam0-eic`](../../../../build/dts/api/bindings/interrupt-controller/atmel%2Csam0-eic.md#std-dtcompatible-atmel-sam0-eic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adafruit/itsybitsy_m4_express/adafruit_itsybitsy_m4_express.dts?plain=1#L30) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adafruit/itsybitsy_m4_express/adafruit_itsybitsy_m4_express.dts?plain=1#L38) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L68) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L126) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adafruit/itsybitsy_m4_express/adafruit_itsybitsy_m4_express.dts?plain=1#L96) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Atmel SAM0 PINMUX[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L151) | [`atmel,sam0-pinmux`](../../../../build/dts/api/bindings/pinctrl/atmel%2Csam0-pinmux.md#std-dtcompatible-atmel-sam0-pinmux) |
| on-chip | Atmel SAM0 Pinctrl container node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L265) | [`atmel,sam0-pinctrl`](../../../../build/dts/api/bindings/pinctrl/atmel%2Csam0-pinctrl.md#std-dtcompatible-atmel-sam0-pinctrl) |
| PWM | on-chip | Atmel SAM0 TCC in PWM mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L435) | [`atmel,sam0-tcc-pwm`](../../../../build/dts/api/bindings/pwm/atmel%2Csam0-tcc-pwm.md#std-dtcompatible-atmel-sam0-tcc-pwm) |
| RNG | on-chip | Atmel SAM RNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L322) | [`atmel,sam-trng`](../../../../build/dts/api/bindings/rng/atmel%2Csam-trng.md#std-dtcompatible-atmel-sam-trng) |
| RTC | on-chip | Atmel SAM0 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L328) | [`atmel,sam0-rtc`](../../../../build/dts/api/bindings/rtc/atmel%2Csam0-rtc.md#std-dtcompatible-atmel-sam0-rtc) |
| Serial controller | on-chip | Atmel SAM0 SERCOM UART driver[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L210) | [`atmel,sam0-uart`](../../../../build/dts/api/bindings/serial/atmel%2Csam0-uart.md#std-dtcompatible-atmel-sam0-uart) |
| SPI | on-chip | Atmel SAM0 SERCOM SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L188) | [`atmel,sam0-spi`](../../../../build/dts/api/bindings/spi/atmel%2Csam0-spi.md#std-dtcompatible-atmel-sam0-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L76) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| USB | on-chip | Atmel SAM0 USB in device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L313) | [`atmel,sam0-usb`](../../../../build/dts/api/bindings/usb/atmel%2Csam0-usb.md#std-dtcompatible-atmel-sam0-usb) |
| Watchdog | on-chip | Atmel SAM0 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L171) | [`atmel,sam0-watchdog`](../../../../build/dts/api/bindings/watchdog/atmel%2Csam0-watchdog.md#std-dtcompatible-atmel-sam0-watchdog) |

Zephyr can use the default Cortex-M SYSTICK timer or the SAM0 specific RTC.
To use the RTC, set `CONFIG_CORTEX_M_SYSTICK=n` and set
`CONFIG_SYS_CLOCK_TICKS_PER_SEC` to no more than 32 kHZ divided by 7,
i.e. no more than 4500.

### Connections and IOs

The [Adafruit Learning System](https://learn.adafruit.com/introducing-adafruit-itsybitsy-m4) [[1]](#id2) has detailed information about
the board including [pinouts](https://learn.adafruit.com/introducing-adafruit-itsybitsy-m4/pinouts) [[2]](#id4) and the [schematic](https://learn.adafruit.com/introducing-adafruit-itsybitsy-m4/downloads) [[3]](#id6).

### System Clock

The SAMD51 MCU is configured to use the 32 kHz internal oscillator
with the on-chip PLL generating the 120 MHz system clock.

### Serial Port

The SAMD51 MCU has 6 SERCOM based USARTs. On the ItsyBitsy, SERCOM3 is
the Zephyr console and is available on pins 0 (RX) and 1 (TX).

### SPI Port

The SAMD51 MCU has 6 SERCOM based SPIs. On the ItsyBitsy, SERCOM1 can be put
into SPI mode and used to connect to devices over the SCK (SCLK), MO (MOSI), and
MI (MISO) pins.

### PWM

The SAMD51 has three PWM generators with up to six channels each. `TCC_0`
has a resolution of 24 bits and all other generators are 16 bit. `TCC_1`
pin 2 is mapped to PA18 (D7) and pin 3 is mapped to PA19 (D9).

### USB Device Port

The SAMD51 MCU has a USB device port that can be used to communicate
with a host PC. See the [USB device support](../../../../samples/subsys/usb/usb.md#usb) sample applications for
more, such as the [USB CDC-ACM](../../../../samples/subsys/usb/cdc_acm/README.md#usb-cdc-acm "Use USB CDC-ACM driver to implement a serial port echo.") sample which sets up a virtual
serial port that echos characters back to the host PC.

## Programming and Debugging

The ItsyBitsy ships with a the BOSSA compatible UF2 bootloader. The
bootloader can be entered by quickly tapping the reset button twice.

Additionally, if `CONFIG_USB_CDC_ACM` is enabled then the bootloader
will be entered automatically when you run `west flash`.

### Flashing

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b adafruit_itsybitsy_m4_express samples/hello_world
   ```
2. Connect the ItsyBitsy to your host computer using USB
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
5. Tap the reset button twice quickly to enter bootloader mode
6. Flash the image:

   ```shell
   west build -b adafruit_itsybitsy_m4_express samples/hello_world
   west flash
   ```

   You should see “Hello World! adafruit\_itsybitsy\_m4\_express” in your terminal.

### Debugging

In addition to the built-in bootloader, the ItsyBitsy can be flashed and
debugged using a SWD probe such as the Segger J-Link.

1. Connect the board to the probe by connecting the `SWCLK`,
   `SWDIO`, `RESET`, `GND`, and `3V3` pins on the
   ItsyBitsy to the `SWCLK`, `SWDIO`, `RESET`, `GND`,
   and `VTref` pins on the [J-Link](https://www.segger.com/products/debug-probes/j-link/technology/interface-description/) [[4]](#id8).
2. Flash the image:

   ```shell
   west build -b adafruit_itsybitsy_m4_express samples/hello_world
   west flash -r openocd
   ```
3. Start debugging:

   ```shell
   west build -b adafruit_itsybitsy_m4_express samples/hello_world
   west debug
   ```

## References

[[1](#id3)]

[https://learn.adafruit.com/introducing-adafruit-itsybitsy-m4](https://learn.adafruit.com/introducing-adafruit-itsybitsy-m4)

[[2](#id5)]

[https://learn.adafruit.com/introducing-adafruit-itsybitsy-m4/pinouts](https://learn.adafruit.com/introducing-adafruit-itsybitsy-m4/pinouts)

[[3](#id7)]

[https://learn.adafruit.com/introducing-adafruit-itsybitsy-m4/downloads](https://learn.adafruit.com/introducing-adafruit-itsybitsy-m4/downloads)

[[4](#id9)]

[https://www.segger.com/products/debug-probes/j-link/technology/interface-description/](https://www.segger.com/products/debug-probes/j-link/technology/interface-description/)

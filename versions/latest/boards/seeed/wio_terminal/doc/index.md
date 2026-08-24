---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/seeed/wio_terminal/doc/index.html
original_path: boards/seeed/wio_terminal/doc/index.html
---

# Wio Terminal

Board Overview

[![../../../../_images/wio_terminal.png](https://docs.zephyrproject.org/4.2.0/_images/wio_terminal.png)
](https://docs.zephyrproject.org/4.2.0/_images/wio_terminal.png)

Wio Terminal

Name:
:   `wio_terminal`

Vendor:
:   Seeed Technology Co., Ltd

Architecture:
:   arm

SoC:
:   samd51p19a

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/seeed/wio_terminal/doc/index.rst/../..)

## Overview

The Wio Terminal is a small (72 mm x 57 mm x 12 mm) and powerful ARM board with
wireless connectivity (2.4G/5G dual-band Wi-Fi and BLE 5.0), LCD display,
USB C port, FPC connector, microSD card slot, Raspberry Pi compatible 40-pins
header and 2 Grove connectors.

## Hardware

- ATSAMD51P19 ARM Cortex-M4F processor at 120 MHz
- 512 KiB flash memory and 192 KiB of RAM
- 4 MiB external flash
- MicroSD card slot
- RTL8720DN 2.4G/5G Dual Bands Wireless and BLE5.0 Combo Module
- 2.4inch LCD display
- LIS3DH accelerometer
- Microphone 1.0V-10V -42dB
- Speaker ≥78dB @10cm 4000Hz
- Light Sensor 400-1050nm
- Infrared Emitter 940nm
- GPIO 40 pin (Raspberry Pi compatible)
- 2x Grove connectors
- 1x user LED
- 3x user buttons
- 5-way user button
- Power/Reset/Boot mode switch
- Native USB port

### Supported Features

The `wio_terminal` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `wio_terminal/samd51p19a` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L59) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | Atmel SAM0 family ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L342) | [`atmel,sam0-adc`](../../../../build/dts/api/bindings/adc/atmel,sam0-adc.md#std-dtcompatible-atmel-sam0-adc) |
| ARM architecture | on-chip | For locating the Device ID (serial number) on Atmel SAM0 devices[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L86) | [`atmel,sam0-id`](../../../../build/dts/api/bindings/arm/atmel,sam0-id.md#std-dtcompatible-atmel-sam0-id) |
| Clock control | on-chip | Atmel SAM0 Main Clock Controller (MCLK)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L94) | [`atmel,sam0-mclk`](../../../../build/dts/api/bindings/clock/atmel,sam0-mclk.md#std-dtcompatible-atmel-sam0-mclk) |
| on-chip | Atmel SAM0 32kHz Oscillator Controller (OSC32KCTRL)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L101) | [`atmel,sam0-osc32kctrl`](../../../../build/dts/api/bindings/clock/atmel,sam0-osc32kctrl.md#std-dtcompatible-atmel-sam0-osc32kctrl) |
| on-chip | Atmel SAMD0 Generic Clock Controller (GCLK)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L108) | [`atmel,sam0-gclk`](../../../../build/dts/api/bindings/clock/atmel,sam0-gclk.md#std-dtcompatible-atmel-sam0-gclk) |
| Counter | on-chip | Atmel SAM0 basic timer counter (TC) operating in 32-bit wide mode[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L391) | [`atmel,sam0-tc32`](../../../../build/dts/api/bindings/counter/atmel,sam0-tc32.md#std-dtcompatible-atmel-sam0-tc32) |
| Display | on-board | Ilitek ILI9341 320x240 display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seeed/wio_terminal/wio_terminal.dts?plain=1#L135) | [`ilitek,ili9341`](../../../../build/dts/api/bindings/display/ilitek,ili9341.md#std-dtcompatible-ilitek-ili9341) |
| DMA | on-chip | Atmel SAM0 DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L133) | [`atmel,sam0-dmac`](../../../../build/dts/api/bindings/dma/atmel,sam0-dmac.md#std-dtcompatible-atmel-sam0-dmac) |
| Flash controller | on-chip | Atmel SAM0 NVMC (Non-Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L116) | [`atmel,sam0-nvmctrl`](../../../../build/dts/api/bindings/flash_controller/atmel,sam0-nvmctrl.md#std-dtcompatible-atmel-sam0-nvmctrl) |
| GPIO & Headers | on-chip | SAM0 GPIO PORT node[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L272) | [`atmel,sam0-gpio`](../../../../build/dts/api/bindings/gpio/atmel,sam0-gpio.md#std-dtcompatible-atmel-sam0-gpio) |
| on-board | GPIO pins exposed on Grove 4 pins headers[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seeed/wio_terminal/grove_connectors.dtsi?plain=1#L7) | [`grove-header`](../../../../build/dts/api/bindings/gpio/grove-header.md#std-dtcompatible-grove-header) |
| on-board | GPIO pins exposed on Raspberry Pi 40-pin header[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seeed/wio_terminal/raspberrypi_40pins_connector.dtsi?plain=1#L7) | [`raspberrypi-40pins-header`](../../../../build/dts/api/bindings/gpio/raspberrypi-40pins-header.md#std-dtcompatible-raspberrypi-40pins-header) |
| I2C | on-chip | Atmel SAM0 series SERCOM I2C[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L210) | [`atmel,sam0-i2c`](../../../../build/dts/api/bindings/i2c/atmel,sam0-i2c.md#std-dtcompatible-atmel-sam0-i2c) |
| Input | on-board | Group of GPIO-bound input keys[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seeed/wio_terminal/wio_terminal.dts?plain=1#L49) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | Atmel SAM0 series External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L142) | [`atmel,sam0-eic`](../../../../build/dts/api/bindings/interrupt-controller/atmel,sam0-eic.md#std-dtcompatible-atmel-sam0-eic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seeed/wio_terminal/wio_terminal.dts?plain=1#L40) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L68) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L126) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seeed/wio_terminal/wio_terminal.dts?plain=1#L156) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Atmel SAM0 PINMUX[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L151) | [`atmel,sam0-pinmux`](../../../../build/dts/api/bindings/pinctrl/atmel,sam0-pinmux.md#std-dtcompatible-atmel-sam0-pinmux) |
| on-chip | Atmel SAM0 Pinctrl Container[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L265) | [`atmel,sam0-pinctrl`](../../../../build/dts/api/bindings/pinctrl/atmel,sam0-pinctrl.md#std-dtcompatible-atmel-sam0-pinctrl) |
| Regulator | on-board | Fixed voltage regulators[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seeed/wio_terminal/wio_terminal.dts?plain=1#L101) | [`regulator-fixed`](../../../../build/dts/api/bindings/regulator/regulator-fixed.md#std-dtcompatible-regulator-fixed) |
| RNG | on-chip | Atmel SAM RNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L322) | [`atmel,sam-trng`](../../../../build/dts/api/bindings/rng/atmel,sam-trng.md#std-dtcompatible-atmel-sam-trng) |
| RTC | on-chip | Atmel SAM0 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L328) | [`atmel,sam0-rtc`](../../../../build/dts/api/bindings/rtc/atmel,sam0-rtc.md#std-dtcompatible-atmel-sam0-rtc) |
| Sensors | on-board | STMicroelectronics LIS3DH 3-axis accelerometer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seeed/wio_terminal/wio_terminal.dts?plain=1#L232) | [`st,lis3dh`](../../../../build/dts/api/bindings/sensor/st,lis3dh-i2c.md#std-dtcompatible-st-lis3dh) |
| Serial controller | on-chip | Atmel SAM0 SERCOM UART driver[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L188) | [`atmel,sam0-uart`](../../../../build/dts/api/bindings/serial/atmel,sam0-uart.md#std-dtcompatible-atmel-sam0-uart) |
| SPI | on-chip | Atmel SAM0 SERCOM SPI controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L177) | [`atmel,sam0-spi`](../../../../build/dts/api/bindings/spi/atmel,sam0-spi.md#std-dtcompatible-atmel-sam0-spi) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L76) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| USB | on-chip | Atmel SAM0 USB in device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L313) | [`atmel,sam0-usb`](../../../../build/dts/api/bindings/usb/atmel,sam0-usb.md#std-dtcompatible-atmel-sam0-usb) |
| Watchdog | on-chip | Atmel SAM0 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd5x.dtsi?plain=1#L171) | [`atmel,sam0-watchdog`](../../../../build/dts/api/bindings/watchdog/atmel,sam0-watchdog.md#std-dtcompatible-atmel-sam0-watchdog) |

Zephyr can use the default Cortex-M SYSTICK timer or the SAM0 specific RTC.
To use the RTC, set `CONFIG_CORTEX_M_SYSTICK=n` and set
[`CONFIG_SYS_CLOCK_TICKS_PER_SEC`](../../../../kconfig.md#CONFIG_SYS_CLOCK_TICKS_PER_SEC "CONFIG_SYS_CLOCK_TICKS_PER_SEC") to no more than 32 kHZ divided
by 7, i.e. no more than 4500.

### Connections and IOs

The [Wio Terminal Getting started guide](https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/) [[1]](#id2) has detailed information about the
board including [pinouts](https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/#pinout-diagram) [[2]](#id4) and its [schematics](https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/#resources) [[3]](#id6).

### System Clock

The SAMD51 MCU is configured to use the 32.768 kHz internal oscillator with the
on-chip PLL generating the 120 MHz system clock.

### Serial Port

Zephyr console output is available using the USB connector, which is used to
make the console available on PC as USB CDC class.

### USB Device Port

The SAMD51 MCU has a USB device port that can be used to communicate with a
host PC. See the [USB device support](../../../../samples/subsys/usb/usb.md#usb) sample applications for more, such as the
[USB CDC-ACM](../../../../samples/subsys/usb/cdc_acm/README.md#usb-cdc-acm "Use USB CDC-ACM driver to implement a serial port echo.") sample which sets up a virtual serial port that echos
characters back to the host PC.

## Programming and Debugging

The `wio_terminal` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[bossac](../../../../develop/flash_debug/host-tools.md#runner-bossac)** | ✅ (default) |  |  |  |  |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |

The Wio Terminal ships with an UF2 bootloader that is BOSSA compatible. The
bootloader can be entered by quickly tapping the reset button twice.

The UF2 file is generated when building the application, and it is possible to
use it to flash the target. Enter the bootloader by quickly sliding the power
button twice, and copy the UF2 file to the USB mass storage device. The device
reboots on the new firmware after the UF2 file has finished transferring.

### Flashing

1. Build the Zephyr kernel and the `button` sample application:

   ```shell
   west build -b wio_terminal samples/basic/button
   ```
2. Swipe the reset/power button down twice quickly to enter bootloader mode
3. Flash the image:

   ```shell
   west build -b wio_terminal samples/basic/button
   west flash
   ```

   You should see the blue (user) LED flashing whenever you press the third
   (counting from the top left) user button at the top of the Wio Terminal.

### Debugging

In addition to the built-in bootloader, the Wio Terminal can be flashed and
debugged using an SWD probe such as the Segger J-Link.

1. Solder cables to the `SWCLK`, `SWDIO`, `RESET`,
   `GND`, and `3V3` pins. See [Test with SWD](https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/#test-with-swd) [[4]](#id8) for more
   information.
2. Connect the board to the probe by connecting the `SWCLK`,
   `SWDIO`, `RESET`, `GND`, and `3V3` pins on the
   Wio Terminal to the `SWCLK`, `SWDIO`, `RESET`,
   `GND`, and `VTref` pins on the [J-Link](https://www.segger.com/products/debug-probes/j-link/technology/interface-description/) [[5]](#id10).
3. Flash the image:

   ```shell
   west build -b wio_terminal samples/basic/button
   west flash -r openocd
   ```
4. Start debugging:

   ```shell
   west build -b wio_terminal samples/basic/button
   west debug
   ```

## References

[[1](#id3)]

[https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/](https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/)

[[2](#id5)]

[https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/#pinout-diagram](https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/#pinout-diagram)

[[3](#id7)]

[https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/#resources](https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/#resources)

[[4](#id9)]

[https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/#test-with-swd](https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/#test-with-swd)

[[5](#id11)]

[https://www.segger.com/products/debug-probes/j-link/technology/interface-description/](https://www.segger.com/products/debug-probes/j-link/technology/interface-description/)

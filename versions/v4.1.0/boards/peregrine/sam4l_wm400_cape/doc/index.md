---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/peregrine/sam4l_wm400_cape/doc/index.html
original_path: boards/peregrine/sam4l_wm400_cape/doc/index.html
---

# SAM4L WM-400 Cape Board

Board Overview

[![../../../../_images/wm-400-pin-out.webp](https://docs.zephyrproject.org/4.1.0/_images/wm-400-pin-out.webp)
](https://docs.zephyrproject.org/4.1.0/_images/wm-400-pin-out.webp)

SAM4L WM-400 Cape Board

Name:
:   `sam4l_wm400_cape`

Vendor:
:   Peregrine Consultoria e Servicos

Architecture:
:   arm

SoC:
:   sam4lc4b

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/peregrine/sam4l_wm400_cape/doc/index.rst/../..)

## Overview

The SAM4L WM-400 Cape is a full featured design to enable IEEE 802.15.4 low
power nodes. It is a Beaglebone Black cape concept with an Atmel AT86RF233
radio transceiver. User can develop Touch interface and have access to many
sensors and conectivity buses.

## Hardware

- ATSAM4LC4B ARM Cortex-M4 Processor
- 12 MHz crystal oscillator
- 32.768 kHz crystal oscillator
- 1 RS-232 interface
- 1 RS-485 full duplex interface
- Micro-AB USB OTG host/device
- 1 user touch button and One user pushbutton
- 4 user LEDs
- 1 AT86RF233 IEEE 802.15.4 transceiver
- 1 MPL115A2 I²C Barometric Pressure/Temperature Sensor
- 1 VCNL4010 Proximity/Light Sensor
- 1 CC2D33S Advanced Humidity Temperature Sensor
- 1 NCP18WF104J03RB NTC Temperature Sensor
- 1 TEMT6000X01 Ambient Light Sensor

### Supported Features

The `sam4l_wm400_cape` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `sam4l_wm400_cape/sam4lc4b` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L26) | [`arm,cortex-m4`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4.md#std-dtcompatible-arm-cortex-m4) |
| Clock control | on-chip | Atmel Power Management Controller (PMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L57) | [`atmel,sam-pmc`](../../../../build/dts/api/bindings/clock/atmel%2Csam-pmc.md#std-dtcompatible-atmel-sam-pmc) |
| Counter | on-chip | Atmel SAM Timer Counter (TC) node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L211)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L221) | [`atmel,sam-tc`](../../../../build/dts/api/bindings/counter/atmel%2Csam-tc.md#std-dtcompatible-atmel-sam-tc) |
| Flash controller | on-chip | Atmel SAM4L Flash Controller Double Word (FLASHCALW)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L65) | [`atmel,sam4l-flashcalw-controller`](../../../../build/dts/api/bindings/flash_controller/atmel%2Csam4l-flashcalw-controller.md#std-dtcompatible-atmel-sam4l-flashcalw-controller) |
| GPIO & Headers | on-chip | SAM4L GPIO PORT node[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L182) | [`atmel,sam4l-gpio`](../../../../build/dts/api/bindings/gpio/atmel%2Csam4l-gpio.md#std-dtcompatible-atmel-sam4l-gpio) |
| Hardware information | on-chip | ATMEL SAM4L Unique 120-bit Serial Number[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L239) | [`atmel,sam4l-uid`](../../../../build/dts/api/bindings/hwinfo/atmel%2Csam4l-uid.md#std-dtcompatible-atmel-sam4l-uid) |
| I2C | on-chip | Atmel SAM4L Family I2C (TWIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L95)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L85) | [`atmel,sam-i2c-twim`](../../../../build/dts/api/bindings/i2c/atmel%2Csam-i2c-twim.md#std-dtcompatible-atmel-sam-i2c-twim) |
| IEEE 802.15.4 | on-board | ATMEL AT86RF2xx 802.15.4 wireless transceiver[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/peregrine/sam4l_wm400_cape/sam4l_wm400_cape.dts?plain=1#L97) | [`atmel,rf2xx`](../../../../build/dts/api/bindings/ieee802154/atmel%2Crf2xx.md#std-dtcompatible-atmel-rf2xx) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/peregrine/sam4l_wm400_cape/sam4l_wm400_cape.dts?plain=1#L55) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/peregrine/sam4l_wm400_cape/sam4l_wm400_cape.dts?plain=1#L31) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L33) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L72) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/peregrine/sam4l_wm400_cape/sam4l_wm400_cape.dts?plain=1#L71) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-board | I2C EEPROMs compatible with Atmel’s AT24 family[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/peregrine/sam4l_wm400_cape/sam4l_wm400_cape.dts?plain=1#L156) | [`atmel,at24`](../../../../build/dts/api/bindings/mtd/atmel%2Cat24.md#std-dtcompatible-atmel-at24) |
| on-board | Atmel AT45 (or compatible) SPI flash[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/peregrine/sam4l_wm400_cape/sam4l_wm400_cape.dts?plain=1#L107) | [`atmel,at45`](../../../../build/dts/api/bindings/mtd/atmel%2Cat45.md#std-dtcompatible-atmel-at45) |
| Pin control | on-chip | Atmel SAM Pinctrl container node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L176) | [`atmel,sam-pinctrl`](../../../../build/dts/api/bindings/pinctrl/atmel%2Csam-pinctrl.md#std-dtcompatible-atmel-sam-pinctrl) |
| RNG | on-chip | Atmel SAM RNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L231) | [`atmel,sam-trng`](../../../../build/dts/api/bindings/rng/atmel%2Csam-trng.md#std-dtcompatible-atmel-sam-trng) |
| Serial controller | on-chip | Atmel SAM family USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L136)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L150) | [`atmel,sam-usart`](../../../../build/dts/api/bindings/serial/atmel%2Csam-usart.md#std-dtcompatible-atmel-sam-usart) |
| SPI | on-chip | Atmel SAM SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L126) | [`atmel,sam-spi`](../../../../build/dts/api/bindings/spi/atmel%2Csam-spi.md#std-dtcompatible-atmel-sam-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L40) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| USB | on-chip | Atmel SAM Family USB (USBC) in device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L165) | [`atmel,sam-usbc`](../../../../build/dts/api/bindings/usb/atmel%2Csam-usbc.md#std-dtcompatible-atmel-sam-usbc) |
| Watchdog | on-chip | ATMEL SAM4L watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4l.dtsi?plain=1#L245) | [`atmel,sam4l-watchdog`](../../../../build/dts/api/bindings/watchdog/atmel%2Csam4l-watchdog.md#std-dtcompatible-atmel-sam4l-watchdog) |

### Connections and IOs

For detailed information see [SAM4L WM-400 Cape](https://gfbudke.wordpress.com/2014/04/30/modulo-wireless-ieee-802-15-4zigbee-wm-400-e-wm-400l-bbbs) [[1]](#id2) Information.

### System Clock

The SAM4L MCU is configured to use the 12 MHz internal oscillator on the board
with the on-chip PLL to generate an 48 MHz system clock.

### Serial Port

The ATSAM4LC4B MCU has 4 USARTs. One of the USARTs (USART3) is shared between
RS-232 and RS-485 interfaces. The default console terminal is available at
RS-232 onboard port or via USB device.

## Programming and Debugging

The SAM4L WM-400 Cape board has a 10-pin header to connect to a Segger JLink.
Using the JLink is possible to program and debug the SAM4LC4B chip. The board
came with a SAM-BA bootloader that only can be used to flash the software.

### Flashing

1. For JLink instructions, see [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools).
2. Run your favorite terminal program to listen for output. Under Linux the
   terminal should be `/dev/ttyACM0`. For example:

   ```shell
   $ minicom -D /dev/ttyACM0 -o
   ```

   The -o option tells minicom not to send the modem initialization
   string. Connection should be configured as follows:

   - Speed: 115200
   - Data: 8 bits
   - Parity: None
   - Stop bits: 1
3. Connect the SAM4L WM-400 Cape board to your host computer using the
   USB debug port. Then build and flash the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.")
   application.

   ```shell
   # From the root of the zephyr repository
   west build -b sam4l_wm400_cape samples/hello_world
   west flash
   ```

   You should see `Hello World! sam4l_wm400_cape` in your terminal.
4. For SAM-BA bootloader instructions, see [SAM Boot Assistant (SAM-BA)](../../../../develop/flash_debug/host-tools.md#atmel-sam-ba-bootloader).
5. Connect the SAM4L WM-400 Cape board to your host computer using the
   USB debug port pressing the S1 button. Then build and flash the
   [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application. After programming the board
   the application will start automatically.

   ```shell
   # From the root of the zephyr repository
   west build -b sam4l_wm400_cape samples/hello_world
   west flash -r bossac
   ```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b sam4l_wm400_cape samples/hello_world
west debug
```

## References

[[1](#id3)]

[https://gfbudke.wordpress.com/2014/04/30/modulo-wireless-ieee-802-15-4zigbee-wm-400-e-wm-400l-bbbs](https://gfbudke.wordpress.com/2014/04/30/modulo-wireless-ieee-802-15-4zigbee-wm-400-e-wm-400l-bbbs)

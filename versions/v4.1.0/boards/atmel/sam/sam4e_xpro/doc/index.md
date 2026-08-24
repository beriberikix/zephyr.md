---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/atmel/sam/sam4e_xpro/doc/index.html
original_path: boards/atmel/sam/sam4e_xpro/doc/index.html
---

# SAM4E Xplained Pro

Board Overview

[![../../../../../_images/sam4e_xpro.jpg](https://docs.zephyrproject.org/4.1.0/_images/sam4e_xpro.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/sam4e_xpro.jpg)

SAM4E Xplained Pro

Name:
:   `sam4e_xpro`

Vendor:
:   Atmel Corporation

Architecture:
:   arm

SoC:
:   sam4e16e

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/atmel/sam/sam4e_xpro/doc/index.rst/../..)

## Overview

The SAM4E Xplained Pro evaluation kit is a development platform to evaluate the
Atmel SAM4E series microcontrollers.

## Hardware

- ATSAM4E16E ARM Cortex-M4F Processor
- 12 MHz crystal oscillator
- internal 32.768 kHz crystal oscillator
- 2 x IS61WV5128BLL 4Mb SRAM
- MT29F2G08ABAEAWP 2Gb NAND
- SD card connector
- CAN-bus (TLE7250GVIOXUMA1 CAN Transceiver)
- Ethernet port (KSZ8081MNXIA phy)
- Micro-AB USB device
- Micro-AB USB debug interface supporting CMSIS-DAP, Virtual COM Port and Data
  Gateway Interface (DGI)
- One reset and one user pushbutton
- 1 yellow user LEDs

### Supported Features

The `sam4e_xpro` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `sam4e_xpro/sam4e16e` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L26) | [`arm,cortex-m4f`](../../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | Atmel SAM family AFEC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L60) | [`atmel,sam-afec`](../../../../../build/dts/api/bindings/adc/atmel%2Csam-afec.md#std-dtcompatible-atmel-sam-afec) |
| Clock control | on-chip | Atmel Power Management Controller (PMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L41) | [`atmel,sam-pmc`](../../../../../build/dts/api/bindings/clock/atmel%2Csam-pmc.md#std-dtcompatible-atmel-sam-pmc) |
| Counter | on-chip | Atmel SAM Timer Counter (TC) node[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L246) | [`atmel,sam-tc`](../../../../../build/dts/api/bindings/counter/atmel%2Csam-tc.md#std-dtcompatible-atmel-sam-tc) |
| Ethernet | on-chip | Atmel SAM-family GMAC Ethernet[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L168) | [`atmel,sam-gmac`](../../../../../build/dts/api/bindings/ethernet/atmel%2Csam-gmac.md#std-dtcompatible-atmel-sam-gmac) |
| on-board | Generic MII PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam/sam4e_xpro/sam4e_xpro.dts?plain=1#L201) | [`ethernet-phy`](../../../../../build/dts/api/bindings/ethernet/ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| Flash controller | on-chip | Atmel SAM Enhanced Embedded Flash Controller (EEFC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L78) | [`atmel,sam-flash-controller`](../../../../../build/dts/api/bindings/flash_controller/atmel%2Csam-flash-controller.md#std-dtcompatible-atmel-sam-flash-controller) |
| GPIO & Headers | on-chip | SAM GPIO PORT node[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L195) | [`atmel,sam-gpio`](../../../../../build/dts/api/bindings/gpio/atmel%2Csam-gpio.md#std-dtcompatible-atmel-sam-gpio) |
| on-board | GPIO pins exposed on Atmel Xplained Pro headers[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam/sam4e_xpro/sam4e_xpro.dts?plain=1#L51) | [`atmel-xplained-pro-header`](../../../../../build/dts/api/bindings/gpio/atmel-xplained-pro-header.md#std-dtcompatible-atmel-xplained-pro-header) |
| Hardware information | on-chip | ATMEL SAM Reset controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L293) | [`atmel,sam-rstc`](../../../../../build/dts/api/bindings/hwinfo/atmel%2Csam-rstc.md#std-dtcompatible-atmel-sam-rstc) |
| I2C | on-chip | Atmel SAM Family I2C (TWI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L104)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L115) | [`atmel,sam-i2c-twi`](../../../../../build/dts/api/bindings/i2c/atmel%2Csam-i2c-twi.md#std-dtcompatible-atmel-sam-i2c-twi) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam/sam4e_xpro/sam4e_xpro.dts?plain=1#L42) | [`gpio-keys`](../../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/atmel/sam/sam4e_xpro/sam4e_xpro.dts?plain=1#L34) | [`gpio-leds`](../../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | Atmel SAM Family MDIO Driver node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L179) | [`atmel,sam-mdio`](../../../../../build/dts/api/bindings/mdio/atmel%2Csam-mdio.md#std-dtcompatible-atmel-sam-mdio) |
| Memory controller | on-chip | Atmel Static Memory Controller (SMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L300) | [`atmel,sam-smc`](../../../../../build/dts/api/bindings/memory-controllers/atmel%2Csam-smc.md#std-dtcompatible-atmel-sam-smc) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L33) | [`arm,armv7m-mpu`](../../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-chip | This binding describes the Atmel SAM flash area layout[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L89) | [`atmel,sam-flash`](../../../../../build/dts/api/bindings/mtd/atmel%2Csam-flash.md#std-dtcompatible-atmel-sam-flash) |
| Pin control | on-chip | Atmel SAM Pinctrl container node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L188) | [`atmel,sam-pinctrl`](../../../../../build/dts/api/bindings/pinctrl/atmel%2Csam-pinctrl.md#std-dtcompatible-atmel-sam-pinctrl) |
| Power management | on-chip | Atmel SAM SUPC (Supply-Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L49) | [`atmel,sam-supc`](../../../../../build/dts/api/bindings/power/atmel%2Csam-supc.md#std-dtcompatible-atmel-sam-supc) |
| PWM | on-chip | Atmel SAM PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L282) | [`atmel,sam-pwm`](../../../../../build/dts/api/bindings/pwm/atmel%2Csam-pwm.md#std-dtcompatible-atmel-sam-pwm) |
| RTC | on-chip | Atmel SAM family RTC device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L316) | [`atmel,sam-rtc`](../../../../../build/dts/api/bindings/rtc/atmel%2Csam-rtc.md#std-dtcompatible-atmel-sam-rtc) |
| SDHC | on-chip | ATMEL (Microchip) SAM HSMCI SD host controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L309) | [`atmel,sam-hsmci`](../../../../../build/dts/api/bindings/sdhc/atmel%2Csam-hsmci.md#std-dtcompatible-atmel-sam-hsmci) |
| Serial controller | on-chip | SAM family UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L136)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L144) | [`atmel,sam-uart`](../../../../../build/dts/api/bindings/serial/atmel%2Csam-uart.md#std-dtcompatible-atmel-sam-uart) |
| on-chip | Atmel SAM family USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L160)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L152) | [`atmel,sam-usart`](../../../../../build/dts/api/bindings/serial/atmel%2Csam-usart.md#std-dtcompatible-atmel-sam-usart) |
| SPI | on-chip | Atmel SAM SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L126) | [`atmel,sam-spi`](../../../../../build/dts/api/bindings/spi/atmel%2Csam-spi.md#std-dtcompatible-atmel-sam-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L56) | [`mmio-sram`](../../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| Watchdog | on-chip | ATMEL SAM0 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/sam4e.dtsi?plain=1#L96) | [`atmel,sam-watchdog`](../../../../../build/dts/api/bindings/watchdog/atmel%2Csam-watchdog.md#std-dtcompatible-atmel-sam-watchdog) |

### Connections and IOs

The [SAM4E Xplained Pro User Guide](http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-42216-SAM4E-Xplained-Pro_User-Guide.pdf) [[1]](#id2) has detailed information about board
connections. Download the [SAM4E Xplained Pro documentation](http://ww1.microchip.com/downloads/en/DeviceDoc/SAM4E-Xplained-Pro_Design-Documentation.zip) [[2]](#id4) for more detail.

### System Clock

The SAM4E MCU is configured to use the 12 MHz internal oscillator on the board
with the on-chip PLL to generate an 120 MHz system clock.

### Serial Port

The ATSAM4E16E MCU has 2 UARTs and 2 USARTs. One of the UARTs (UART0) is
configured for the console and is available as a Virtual COM Port by EDBG USB
chip.

## Programming and Debugging

Flashing the Zephyr project onto SAM4E MCU requires the [OpenOCD tool](http://openocd.org/) [[3]](#id6).
By default a factory new SAM4E chip will boot SAM-BA boot loader located in
the ROM, not the flashed image. This is determined by the value of GPNVM1
(General-Purpose NVM bit 1). The flash procedure will ensure that GPNVM1 is
set to 1 changing the default behavior to boot from Flash.

If your chip has a security bit GPNVM0 set you will be unable to program flash
memory or connect to it via a debug interface. The only way to clear GPNVM0
is to perform a chip erase procedure that will erase all GPNVM bits and the full
contents of the SAM4E flash memory:

- With the board power off, set a jumper on the J304 header.
- Turn the board power on. The jumper can be removed soon after the power is on
  (flash erasing procedure is started when the erase line is asserted for at
  least 230ms)

### Flashing

For flash the board Zephyr provides two paths. One uses the default OpenOCD
tool and the second one uses [SAM Boot Assistant (SAM-BA)](../../../../../develop/flash_debug/host-tools.md#atmel-sam-ba-bootloader).

#### Using OpenOCD

1. Connect the SAM4E Xplained Pro board to your host computer using the USB
   debug port. Then build and flash the [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

   ```shell
   # From the root of the zephyr repository
   west build -b sam4e_xpro samples/hello_world
   west flash
   ```

#### Using SAM-BA bootloader

1. Close the `ERASE` jumper on the SAM4E Xplained Pro board. Power on the
   board for 10s.
2. Open the `ERASE` jumper.
3. Connect the SAM4E Xplained Pro board to your host computer using the SoC
   USB port. Then build and flash the [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

   ```shell
   # From the root of the zephyr repository
   west build -b sam4e_xpro samples/hello_world
   ```

   ```shell
   $ west flash -r bossac
   ```

#### Visualizing the message

1. Run your favorite terminal program to listen for output. Under Linux the
   terminal should be `/dev/ttyACM0`. For example:

   ```shell
   $ minicom -D /dev/ttyACM0 -o
   ```

   The -o option tells minicom not to send the modem initialization string.
   Connection should be configured as follows:

   - Speed: 115200
   - Data: 8 bits
   - Parity: None
   - Stop bits: 1
2. Press reset button

   You should see “Hello World! sam4e\_xpro” in your terminal.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b sam4e_xpro samples/hello_world
west debug
```

## References

[[1](#id3)]

[http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-42216-SAM4E-Xplained-Pro\_User-Guide.pdf](http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-42216-SAM4E-Xplained-Pro_User-Guide.pdf)

[[2](#id5)]

[http://ww1.microchip.com/downloads/en/DeviceDoc/SAM4E-Xplained-Pro\_Design-Documentation.zip](http://ww1.microchip.com/downloads/en/DeviceDoc/SAM4E-Xplained-Pro_Design-Documentation.zip)

[[3](#id7)]

[http://openocd.org/](http://openocd.org/)

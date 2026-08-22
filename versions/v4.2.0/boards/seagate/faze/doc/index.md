---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/seagate/faze/doc/index.html
original_path: boards/seagate/faze/doc/index.html
---

# FireCuda Gaming SSD (FaZe) board

Board Overview

[![../../../../_images/firecuda-gaming-ssd.jpg](../../../../_images/firecuda-gaming-ssd.jpg)
](../../../../_images/firecuda-gaming-ssd.jpg)

FireCuda Gaming SSD (FaZe) board

Name:
:   `faze`

Vendor:
:   Seagate Technology PLC

Architecture:
:   arm

SoC:
:   lpc11u67

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/seagate/faze/doc/index.rst/../..)

## Overview

The FaZe board can be found in the Seagate FireCuda Gaming SSD devices. A NVMe
SSD and two chips are embedded: an ASMedia ASM2364 USB-to-PCIe bridge controller
and a NXP LPC11U67 MCU. The former is handling the USB type-C to SSD I/Os while
the latter is dedicated to the LED effects. The two chips are connected together
through I2C and GPIOs.

This Zephyr port is running on the NXP LPC11U67 MCU.

## Hardware

- NXP LPC11U67 MCU (LQFP48 package):

  - ARM Cortex-M0+
  - 20 KB SRAM: 16 KB (SRAM0) + 2 KB (SRAM1) + 2KB (USB SRAM)
  - 128 KB on-chip flash
  - 4 KB on-chip EEPROM
- External devices connected to the NXP LPC11U67 MCU:

  - ASMedia ASM2364 USB-to-PCIe bridge (I2C master on port O).
  - 6 RGB LEDs connected to a TI LP5030 LED controller (I2C device on
    port 1).
  - 1 white LED (SSD activity blinking).

More information can be found here:

- [LPC11UXX SoC Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc1100-cortex-m0-plus-m0/scalable-entry-level-32-bit-microcontroller-mcu-based-on-arm-cortex-m0-plus-and-cortex-m0-cores:LPC11U00)
- [LPC11U6X Datasheet](https://www.nxp.com/docs/en/data-sheet/LPC11U6X.pdf)
- [LPC11U6X Reference Manual](https://www.nxp.com/webapp/Download?colCode=UM10732)

### Supported Features

The `faze` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `faze/lpc11u67` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc11u6x.dtsi?plain=1#L16) | [`arm,cortex-m0+`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m0%2B.md#std-dtcompatible-arm-cortex-m0) |
| Clock control | on-chip | LPC11U6X clock controller node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc11u6x.dtsi?plain=1#L131) | [`nxp,lpc11u6x-syscon`](../../../../build/dts/api/bindings/clock/nxp%2Clpc11u6x-syscon.md#std-dtcompatible-nxp-lpc11u6x-syscon) |
| GPIO & Headers | on-chip | NXP LPC11U6X GPIO[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc11u6x.dtsi?plain=1#L81) | [`nxp,lpc11u6x-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Clpc11u6x-gpio.md#std-dtcompatible-nxp-lpc11u6x-gpio) |
| I2C | on-chip | LPC11U6X I2C Controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc11u6x.dtsi?plain=1#L177) | [`nxp,lpc11u6x-i2c`](../../../../build/dts/api/bindings/i2c/nxp%2Clpc11u6x-i2c.md#std-dtcompatible-nxp-lpc11u6x-i2c) |
| on-board | ASMedia ASM2364 USB-to-PCIe bridge controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seagate/faze/faze.dts?plain=1#L68) | [`asmedia,asm2364`](../../../../build/dts/api/bindings/i2c/asmedia%2Casm2364.md#std-dtcompatible-asmedia-asm2364) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seagate/faze/faze.dts?plain=1#L34) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| LED | on-board | Texas Instruments LP5030 I2C LED controller node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seagate/faze/faze.dts?plain=1#L82) | [`ti,lp5030`](../../../../build/dts/api/bindings/led/ti%2Clp5030.md#std-dtcompatible-ti-lp5030) |
| on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seagate/faze/faze.dts?plain=1#L45) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc11u6x.dtsi?plain=1#L39) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | NXP LPC11U6X on-chip EEPROM node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc11u6x.dtsi?plain=1#L44) | [`nxp,lpc11u6x-eeprom`](../../../../build/dts/api/bindings/mtd/nxp%2Clpc11u6x-eeprom.md#std-dtcompatible-nxp-lpc11u6x-eeprom) |
| Pin control | on-chip | LPC I/O Pin Configuration (IOCON)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc11u6x.dtsi?plain=1#L54) | [`nxp,lpc-iocon`](../../../../build/dts/api/bindings/pinctrl/nxp%2Clpc-iocon.md#std-dtcompatible-nxp-lpc-iocon) |
| on-chip | LPC pinctrl node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc11u6x.dtsi?plain=1#L60) | [`nxp,lpc11u6x-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Clpc11u6x-pinctrl.md#std-dtcompatible-nxp-lpc11u6x-pinctrl) |
| on-chip | LPC I/O Pin Configuration (IOCON) Port I/O (PIO)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc11u6x.dtsi?plain=1#L64) | [`nxp,lpc-iocon-pio`](../../../../build/dts/api/bindings/pinctrl/nxp%2Clpc-iocon-pio.md#std-dtcompatible-nxp-lpc-iocon-pio) |
| Serial controller | on-chip | LPC11U6X UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc11u6x.dtsi?plain=1#L137)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc11u6x.dtsi?plain=1#L145) | [`nxp,lpc11u6x-uart`](../../../../build/dts/api/bindings/serial/nxp%2Clpc11u6x-uart.md#std-dtcompatible-nxp-lpc11u6x-uart) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_lpc11u6x.dtsi?plain=1#L22) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv6-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21) | [`arm,armv6m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv6m-systick.md#std-dtcompatible-arm-armv6m-systick) |

### Connections and IOs

The IOCON controller can be used to configure the LPC11U67 pins.

| Name | Function | Usage |
| --- | --- | --- |
| PIO0\_2 | GPIO | ASM2364 interrupt |
| PIO0\_4 | I2C0 | I2C0 SCL |
| PIO0\_5 | I2C0 | I2C0 SDA |
| PIO0\_7 | I2C1 | I2C1 SCL |
| PIO0\_18 | UART | USART0 RX |
| PIO0\_19 | UART | USART0 TX |
| PIO0\_20 | GPIO | USB sleep |
| PIO1\_23 | GPIO | SSD activity white LED |
| PIO1\_24 | I2C1 | I2C1 SDA |

## Programming and Debugging

The `faze` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Flashing

The NXP LPC11U67 MCU can be flashed by connecting an external debug probe to
the SWD port (on-board 4-pins J2 header). In the default OpenOCD configuration
([boards/seagate/faze/support/openocd.cfg](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/seagate/faze/support/openocd.cfg)) the ST Link interface is selected.
You may need to replace it with the interface of your debug probe.

Once the debug probe is connected to both the FaZe board and your host computer
then you can simply run the `west flash` command to write a firmware image you
built into flash.

### Debugging

Please refer to the [Flashing](#flashing) section and run the `west debug` command
instead of `west flash`.

## References

- [LPC11UXX SoC Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc1100-cortex-m0-plus-m0/scalable-entry-level-32-bit-microcontroller-mcu-based-on-arm-cortex-m0-plus-and-cortex-m0-cores:LPC11U00)
- [LPC11U6X Datasheet](https://www.nxp.com/docs/en/data-sheet/LPC11U6X.pdf)
- [LPC11U6X Reference Manual](https://www.nxp.com/webapp/Download?colCode=UM10732)

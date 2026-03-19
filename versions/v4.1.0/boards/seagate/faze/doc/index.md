---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/seagate/faze/doc/index.html
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

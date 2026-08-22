---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/lpcxpresso11u68/doc/index.html
original_path: boards/nxp/lpcxpresso11u68/doc/index.html
---

# LPCXpresso11U68

Board Overview

[![../../../../_images/lpcxpresso11u68.jpg](../../../../_images/lpcxpresso11u68.jpg)
](../../../../_images/lpcxpresso11u68.jpg)

LPCXpresso11U68

Name:
:   `lpcxpresso11u68`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   lpc11u68

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/lpcxpresso11u68/doc/index.rst/../..)

## Overview

The LPCXpresso11u68 development board uses an NXP LPC11U68 MCU based
on an ARM Cortex-M0+ core.

## Hardware

The LPCxpresso 11U68 board provides the following hardware components:

- LPC11U68 microcontroller in LQFP100 package
- ARM Cortex-M0+
- Memory:

  - 256KB of flash memory
  - 32KB of SRAM
  - 2x2KB of additional SRAM
  - 4 KB EEPROM
- USB:

  - USB 2.0 Full-Speed device controller
- DMA controller
- 5x USART
- 2x I2C
- 2x SSP with DMA support
- Board power supply: through USB bus or external power supply (3V and 5V)
- Arduino connectors compatible with the ‘Arduino UNO’ platform
- Tri-color user LED, Power On Led, Reset LED
- Three push buttons: target reset, ISP and user

More information can be found here:

- [LPC11UXX SoC Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc1100-cortex-m0-plus-m0/scalable-entry-level-32-bit-microcontroller-mcu-based-on-arm-cortex-m0-plus-and-cortex-m0-cores:LPC11U00)
- [LPC11U6X Datasheet](https://www.nxp.com/docs/en/data-sheet/LPC11U6X.pdf)
- [LPC11U6X Reference Manual](https://www.nxp.com/webapp/Download?colCode=UM10732)
- [LPCXPRESSO11U68 Website](https://www.nxp.com/design/microcontrollers-developer-resources/lpc-microcontroller-utilities/lpcxpresso-board-for-lpc11u68:OM13058)
- [LPCXPRESSO11U68 Schematics](https://www.nxp.com/downloads/en/schematics/LPC11U68_Xpresso_v2_Schematic_RevC_1.pdf)

### Supported Features

The `lpcxpresso11u68` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

The IOCON controller can be used to configure the LPC11U68 pins.

| Name | Function | Usage |
| --- | --- | --- |
| PIO2\_11 | UART | USART RX |
| PIO2\_12 | UART | USART TX |
| PIO2\_16 | GPIO | GREEN LED |
| PIO2\_17 | GPIO | RED LED |
| PIO2\_18 | GPIO | BLUE\_LED |
| PIO0\_4 | I2C | I2C SCL |
| PIO0\_5 | I2C | I2C SDA |

## Programming and Debugging

The `lpcxpresso11u68` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

### Flashing

The LPCXpresso11U68 board can be flashed by using the on-board LPC-Link2 debug
probe (based on a NXP LPC43xx MCU). This MCU provides either a CMSIS-DAP or
a J-Link interface. It depends on the embedded firmware image. The default
OpenOCD configuration supports the CMSIS-DAP interface. If you want to
switch to J-Link, then you need to edit the
[boards/nxp/lpcxpresso11u68/support/openocd.cfg](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso11u68/support/openocd.cfg) file and to replace:

```text
source [find interface/cmsis-dap.cfg]
```

with:

```text
source [find interface/jlink.cfg]
```

Note

The firmware image of the LPC-Link2 can be updated using the
[LPCScrypt tool](https://www.nxp.com/design/microcontrollers-developer-resources/lpc-microcontroller-utilities/lpcscrypt-v2-1-1:LPCSCRYPT).

Note

The [Mbed project](https://os.mbed.com) also provides some firmware images
[here](https://os.mbed.com/teams/NXP/wiki/Updating-LPCXpresso-firmware).
In addition to a CMSIS-DAP interface, they also provide a convenient update
mechanism through a pseudo USB disk.

Here are the steps to flash a firmware you built into a LPCXpresso11U68 board:

1. Connect the “Link” micro-B USB port to your host computer.
2. Next, simply run the `west flash` command

### Debugging

Please refer to the [Flashing](#flashing) section and run the `west debug` command
instead of `west flash`.

## References

- [LPC11UXX SoC Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc1100-cortex-m0-plus-m0/scalable-entry-level-32-bit-microcontroller-mcu-based-on-arm-cortex-m0-plus-and-cortex-m0-cores:LPC11U00)
- [LPC11U6X Datasheet](https://www.nxp.com/docs/en/data-sheet/LPC11U6X.pdf)
- [LPC11U6X Reference Manual](https://www.nxp.com/webapp/Download?colCode=UM10732)
- [LPCXPRESSO11U68 Website](https://www.nxp.com/design/microcontrollers-developer-resources/lpc-microcontroller-utilities/lpcxpresso-board-for-lpc11u68:OM13058)
- [LPCXPRESSO11U68 Schematics](https://www.nxp.com/downloads/en/schematics/LPC11U68_Xpresso_v2_Schematic_RevC_1.pdf)

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

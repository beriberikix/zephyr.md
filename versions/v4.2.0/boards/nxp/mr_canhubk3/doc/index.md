---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/mr_canhubk3/doc/index.html
original_path: boards/nxp/mr_canhubk3/doc/index.html
---

# MR-CANHUBK3

Board Overview

[![../../../../_images/mr_canhubk3_top.jpg](../../../../_images/mr_canhubk3_top.jpg)
](../../../../_images/mr_canhubk3_top.jpg)

MR-CANHUBK3

Name:
:   `mr_canhubk3`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   s32k344

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/mr_canhubk3/doc/index.rst/../..)

## Overview

[NXP MR-CANHUBK3](https://www.nxp.com/design/development-boards/automotive-development-platforms/s32k-mcu-platforms/s32k344-evaluation-board-for-mobile-robotics-incorporating-100baset1-and-six-can-fd:MR-CANHUBK344) [[8]](#id16) is an evaluation board for mobile robotics applications such
as autonomous mobile robots (AMR) and automated guided vehicles (AGV). It
features an [NXP S32K344](https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32k-auto-general-purpose-mcus/s32k3-microcontrollers-for-automotive-general-purpose:S32K3) [[9]](#id20) general-purpose automotive microcontroller based on
an Arm Cortex-M7 core (Lock-Step).

## Hardware

- NXP S32K344
  :   - Arm Cortex-M7 (Lock-Step), 160 MHz (Max.)
      - 4 MB of program flash, with ECC
      - 320 KB RAM, with ECC
      - Ethernet 100 Mbps, CAN FD, FlexIO, QSPI
      - 12-bit 1 Msps ADC, 16-bit eMIOS timer
- [NXP FS26 Safety System Basis Chip](https://www.nxp.com/products/power-management/pmics-and-sbcs/safety-sbcs/safety-system-basis-chip-with-low-power-fit-for-asil-d:FS26) [[10]](#id22)
- Interfaces:
  :   - Console UART
      - 6x CAN FD
      - 100Base-T1 Ethernet
      - JST-GH connectors and I/O headers for I2C, SPI, GPIO,
        PWM, etc.

More information about the hardware and design resources can be found at
[NXP MR-CANHUBK3](https://www.nxp.com/design/development-boards/automotive-development-platforms/s32k-mcu-platforms/s32k344-evaluation-board-for-mobile-robotics-incorporating-100baset1-and-six-can-fd:MR-CANHUBK344) [[8]](#id16) website.

### Supported Features

The `mr_canhubk3` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

Each GPIO port is divided into two banks: low bank, from pin 0 to 15, and high
bank, from pin 16 to 31. For example, `PTA2` is the pin 2 of `gpioa_l` (low
bank), and `PTA20` is the pin 4 of `gpioa_h` (high bank).

The GPIO controller provides the option to route external input pad interrupts
to either the SIUL2 EIRQ or WKPU interrupt controllers, as supported by the SoC.
By default, GPIO interrupts are routed to SIUL2 EIRQ interrupt controller,
unless they are explicity configured to be directed to the WKPU interrupt
controller, as outlined in [dts/bindings/gpio/nxp,s32-gpio.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/bindings/gpio/nxp,s32-gpio.yaml).

To find information about which GPIOs are compatible with each interrupt
controller, refer to the device reference manual.

Note

It is important to highlight that the current board configuration lacks
support for wake-up events and power-management features. WKPU functionality
is restricted solely to serving as an interrupt controller.

#### LEDs

The MR-CANHUBK3 board has one user RGB LED:

| Devicetree node | Color | Pin | Pin Functions |
| --- | --- | --- | --- |
| led0 / user\_led1\_red | Red | PTE14 | FXIO D7 / EMIOS0 CH19 |
| led1 / user\_led1\_green | Green | PTA27 | FXIO D5 / EMIOS1 CH10 / EMIOS2 CH10 |
| led2 / user\_led1\_blue | Blue | PTE12 | FXIO D8 / EMIOS1 CH5 |

In addition to the RGB LED, the MR-CANHUBK3 board has six red LEDs, each located
next to one of the CAN connectors:

| Devicetree node | Color | Pin | Pin Functions |
| --- | --- | --- | --- |
| can\_led0 | Red | PTC18 | FXIO D6 / FXIO D12 / EMIOS2 CH12 |
| can\_led1 | Red | PTE5 | FXIO D7 / EMIOS1 CH5 / EMIOS0 CH 19 |
| can\_led2 | Red | PTD20 | EMIOS1 CH17 / EMIOS2 CH0 |
| can\_led3 | Red | PTB24 | FXIO D5 / EMIOS1 CH20 / EMIOS2 CH20 |
| can\_led4 | Red | PTB26 | FXIO D7 / EMIOS1 CH22 / EMIOS2 CH22 |
| can\_led5 | Red | PTD31 | FXIO D6 / EMIOS2 CH22 |

The user can control the LEDs in any way. An output of `0` illuminates the LED.

#### Buttons

The MR-CANHUBK3 board has two user buttons:

| Devicetree node | Label | Pin | Pin Functions |
| --- | --- | --- | --- |
| sw0 / user\_button\_1 | SW1 | PTD15 | EIRQ31 |
| sw0 / user\_button\_2 | SW2 | PTA25 | EIRQ5 / WKPU34 |

### System Clock

The Arm Cortex-M7 (Lock-Step) are configured to run at 160 MHz.

### Serial Console

By default, the serial console is provided through `lpuart2` on the 7-pin
DCD-LZ debug connector `P6`.

| Connector | Pin | Pin Function |
| --- | --- | --- |
| P6.2 | PTA9 | LPUART2\_TX |
| P6.3 | PTA8 | LPUART2\_RX |

### CAN

CAN is provided through FLEXCAN interface with 6 instances.

| Devicetree node | Pin | Pin Function | Bus Connector |
| --- | --- | --- | --- |
| flexcan0 | PTA6  PTA7 | PTA6\_CAN0\_RX  PTA7\_CAN0\_TX | P12/P13 |
| flexcan1 | PTC9  PTC8 | PTC9\_CAN0\_RX  PTC8\_CAN0\_TX | P14/P15 |
| flexcan2 | PTE25  PTE24 | PTE25\_CAN0\_RX  PTE24\_CAN0\_TX | P16/P17 |
| flexcan3 | PTC29  PTC28 | PTC29\_CAN0\_RX  PTC28\_CAN0\_TX | P18/019 |
| flexcan4 | PTC31  PTC30 | PTC31\_CAN0\_RX  PTC30\_CAN0\_TX | P20/P21 |
| flexcan5 | PTC11  PTC10 | PTC11\_CAN0\_RX  PTC10\_CAN0\_TX | P22/P23 |

Note

There is limitation by HAL SDK, so CAN only has support maximum 64 message buffers (MBs)
and support maximum 32 message buffers for concurrent active instances with 8 bytes
payload. We need to pay attention to configuration options:

1. [`CONFIG_CAN_MAX_MB`](../../../../kconfig.md#CONFIG_CAN_MAX_MB "CONFIG_CAN_MAX_MB") must be less or equal than the
   maximum number of message buffers that is according to the table below.
2. [`CONFIG_CAN_MAX_FILTER`](../../../../kconfig.md#CONFIG_CAN_MAX_FILTER "CONFIG_CAN_MAX_FILTER") must be less or equal than
   [`CONFIG_CAN_MAX_MB`](../../../../kconfig.md#CONFIG_CAN_MAX_MB "CONFIG_CAN_MAX_MB").

| Devicetree node | Payload | Hardware support | Software support |
| --- | --- | --- | --- |
| flexcan0 | 8 bytes  16 bytes  32 bytes  64 bytes | 96 MBs  63 MBs  36 MBs  21 MBs | 64 MBs  42 MBs  24 MBs  14 MBs |
| flexcan1 | 8 bytes  16 bytes  32 bytes  64 bytes | 64 MBs  42 MBs  24 MBs  14 MBs | 64 MBs  42 MBs  24 MBs  14 MBs |
| flexcan2 | 8 bytes  16 bytes  32 bytes  64 bytes | 64 MBs  42 MBs  24 MBs  14 MBs | 64 MBs  42 MBs  24 MBs  14 MBs |
| flexcan3 | 8 bytes  16 bytes  32 bytes  64 bytes | 32 MBs  21 MBs  12 MBs  7 MBs | 32 MBs  21 MBs  12 MBs  7 MBs |
| flexcan4 | 8 bytes  16 bytes  32 bytes  64 bytes | 32 MBs  21 MBs  12 MBs  7 MBs | 32 MBs  21 MBs  12 MBs  7 MBs |
| flexcan5 | 8 bytes  16 bytes  32 bytes  64 bytes | 32 MBs  21 MBs  12 MBs  7 MBs | 32 MBs  21 MBs  12 MBs  7 MBs |

Note

A CAN bus usually requires 120 Ohm termination at both ends of the bus. This may be
accomplished using one of the included CAN termination boards. For more details, refer
to the section `6.3 CAN Connectors` in the Hardware User Manual of [NXP MR-CANHUBK3](https://www.nxp.com/design/development-boards/automotive-development-platforms/s32k-mcu-platforms/s32k344-evaluation-board-for-mobile-robotics-incorporating-100baset1-and-six-can-fd:MR-CANHUBK344) [[8]](#id16).

### I2C

I2C is provided through LPI2C interface with 2 instances `lpi2c0` and `lpi2c1`
on corresponding connectors `P4`, `P3`.

| Connector | Pin | Pin Function |
| --- | --- | --- |
| P3.2 | PTD9 | LPI2C1\_SCL |
| P3.3 | PTD8 | LPI2C1\_SDA |
| P4.3 | PTD14 | LPI2C0\_SCL |
| P4.4 | PTD13 | LPI2C0\_SDA |

The accompanying display board can be connected to `lpi2c0` via connector `P4`.

### ADC

ADC is provided through ADC SAR controller with 3 instances. ADC channels are divided into
3 groups (precision, standard and external).

Note

All channels of an instance only run on 1 group channel at the same time.

### FS26 SBC Watchdog

On normal operation after the board is powered on, there is a window of 256 ms
on which the FS26 watchdog must be serviced with a good token refresh, otherwise
the watchdog will signal a reset to the MCU. This board configuration enables
the FS26 watchdog driver that handles this initialization.

Note

The FS26 can also be started in debug mode (watchdog disabled) following
these steps:

1. Power off the board.
2. Remove the jumper `JP1` (pins 1-2 open), which is connected by default.
3. Power on the board.
4. Reconnect the jumper `JP1` (pins 1-2 shorted).

### External Flash

The on-board MX25L6433F 64M-bit multi-I/O Serial NOR Flash memory is connected
to the QSPI controller port A1. This board configuration selects it as the
default flash controller.

### Ethernet

This board has a single instance of Ethernet Media Access Controller (EMAC)
interfacing with a [NXP TJA1103](https://www.nxp.com/products/interfaces/ethernet-/automotive-ethernet-phys/asil-b-compliant-100base-t1-ethernet-phy:TJA1103) [[11]](#id24) 100Base-T1 Ethernet PHY. Currently, there is
limited driver for this PHY that allows for overiding the default pin strapping configuration for
the PHY (RMII, master, autonomous mode enabled, polarity correction enabled)
to slave mode.

The 100Base-T1 signals are available in connector `P9` and can be converted to
100Base-T using a Ethernet media converter such as [RDDRONE-T1ADAPT](https://www.nxp.com/products/interfaces/ethernet-/automotive-ethernet-phys/ethernet-media-converter-for-drones-rovers-mobile-robotics-and-automotive:RDDRONE-T1ADAPT) [[12]](#id26).

## Programming and Debugging

The `mr_canhubk3` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

Applications for the `mr_canhubk3` board can be built in the usual way as
documented in [Building an Application](../../../../develop/application/index.md#build-an-application).

This board configuration supports [Lauterbach TRACE32](https://www.lauterbach.com) [[13]](#id28), [SEGGER J-Link](https://wiki.segger.com/NXP_S32K3xx) [[14]](#id30) and [pyOCD](https://pyocd.io/) [[15]](#id32)
West runners for flashing and debugging. Follow the steps described in
[Lauterbach TRACE32 Debug Host Tools](../../../../develop/flash_debug/host-tools.md#lauterbach-trace32-debug-host-tools), [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and
[pyOCD Debug Host Tools](../../../../develop/flash_debug/host-tools.md#pyocd-debug-host-tools), to set up the required host tools.
The default runner is J-Link.

If using TRACE32, ensure you have version >= 2024.09 installed.

### Flashing

Run the `west flash` command to flash the application using SEGGER J-Link.
Alternatively, run `west flash -r trace32` to use Lauterbach TRACE32, or
`` west flash -r pyocd` `` to use pyOCD.

The Lauterbach TRACE32 runner supports additional options that can be passed
through command line:

```shell
west flash -r trace32 --startup-args elfFile=<elf_path> loadTo=<flash/sram>
   eraseFlash=<yes/no> verifyFlash=<yes/no>
```

Where:

- `<elf_path>` is the path to the Zephyr application ELF in the output
  directory
- `loadTo=flash` loads the application to the SoC internal program flash
  ([`CONFIG_XIP`](../../../../kconfig.md#CONFIG_XIP "CONFIG_XIP") must be set), and `loadTo=sram` load the
  application to SRAM. Default is `flash`.
- `eraseFlash=yes` erases the whole content of SoC internal flash before the
  application is downloaded to either Flash or SRAM. This routine takes time to
  execute. Default is `no`.
- `verifyFlash=yes` verify the SoC internal flash content after programming
  (use together with `loadTo=flash`). Default is `no`.

For example, to erase and verify flash content:

```shell
west flash -r trace32 --startup-args elfFile=build/zephyr/zephyr.elf loadTo=flash eraseFlash=yes verifyFlash=yes
```

### Debugging

Run the `west debug` command to start a GDB session using SEGGER J-Link.
Alternatively, run `west debug -r trace32` or `west debug -r pyocd`
to launch the Lauterbach TRACE32 or pyOCD software debugging interface respectively.

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk) [[1]](#id2)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC) [[2]](#id4), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) [[3]](#id6) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started) [[4]](#id8)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548) [[5]](#id10)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) [[6]](#id12) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project) [[7]](#id14)

## References

[[1](#id3)]

[https://github.com/nxp-zephyr/nxp-zsdk](https://github.com/nxp-zephyr/nxp-zsdk)

[[2](#id5)]

[https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC)

[[3](#id7)]

[https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki)

[[4](#id9)]

[https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)

[[5](#id11)]

[https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)

[[6](#id13)]

[https://nxp.com/zephyr](https://nxp.com/zephyr)

[[7](#id15)]

[https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

[8]
([1](#id17),[2](#id18),[3](#id19))

[https://www.nxp.com/design/development-boards/automotive-development-platforms/s32k-mcu-platforms/s32k344-evaluation-board-for-mobile-robotics-incorporating-100baset1-and-six-can-fd:MR-CANHUBK344](https://www.nxp.com/design/development-boards/automotive-development-platforms/s32k-mcu-platforms/s32k344-evaluation-board-for-mobile-robotics-incorporating-100baset1-and-six-can-fd:MR-CANHUBK344)

[[9](#id21)]

[https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32k-auto-general-purpose-mcus/s32k3-microcontrollers-for-automotive-general-purpose:S32K3](https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32k-auto-general-purpose-mcus/s32k3-microcontrollers-for-automotive-general-purpose:S32K3)

[[10](#id23)]

[https://www.nxp.com/products/power-management/pmics-and-sbcs/safety-sbcs/safety-system-basis-chip-with-low-power-fit-for-asil-d:FS26](https://www.nxp.com/products/power-management/pmics-and-sbcs/safety-sbcs/safety-system-basis-chip-with-low-power-fit-for-asil-d:FS26)

[[11](#id25)]

[https://www.nxp.com/products/interfaces/ethernet-/automotive-ethernet-phys/asil-b-compliant-100base-t1-ethernet-phy:TJA1103](https://www.nxp.com/products/interfaces/ethernet-/automotive-ethernet-phys/asil-b-compliant-100base-t1-ethernet-phy:TJA1103)

[[12](#id27)]

[https://www.nxp.com/products/interfaces/ethernet-/automotive-ethernet-phys/ethernet-media-converter-for-drones-rovers-mobile-robotics-and-automotive:RDDRONE-T1ADAPT](https://www.nxp.com/products/interfaces/ethernet-/automotive-ethernet-phys/ethernet-media-converter-for-drones-rovers-mobile-robotics-and-automotive:RDDRONE-T1ADAPT)

[[13](#id29)]

[https://www.lauterbach.com](https://www.lauterbach.com)

[[14](#id31)]

[https://wiki.segger.com/NXP\_S32K3xx](https://wiki.segger.com/NXP_S32K3xx)

[[15](#id33)]

[https://pyocd.io/](https://pyocd.io/)

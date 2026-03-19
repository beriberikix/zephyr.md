---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/makerbase/mks_canable_v20/doc/index.html
original_path: boards/makerbase/mks_canable_v20/doc/index.html
---

# MKS CANable V2.0

Board Overview

[![../../../../_images/mks_canable_v20.webp](../../../../_images/mks_canable_v20.webp)
](../../../../_images/mks_canable_v20.webp)

MKS CANable V2.0

Name:
:   `mks_canable_v20`

Vendor:
:   Makerbase Co., Ltd.

Architecture:
:   arm

SoC:
:   stm32g431xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/makerbase/mks_canable_v20/doc/index.rst/../..)

## Overview

The Makerbase MKS CANable V2.0 board features an ARM Cortex-M4 based STM32G431C8 MCU
with a CAN, USB and debugger connections.
Here are some highlights of the MKS CANable V2.0 board:

- STM32 microcontroller in LQFP48 package
- USB Type-C connector (J1)
- CAN-Bus connector (J2)
- ST-LINK/V3E debugger/programmer header (J4)
- USB VBUS power supply (5 V)
- Three LEDs: red/power\_led (D1), blue/stat\_led (D2), green/word\_led (D3)
- One push-button for RESET
- Development support: serial wire debug (SWD), JTAG, Embedded Trace Macrocell.

The LED red/power\_led (D1) is connected directly to on-board 3.3 V and not controllable by the MCU.

More information about the board can be found at the [MKS CANable V2.0 website](https://github.com/makerbase-mks/CANable-MKS) [[1]](#id2).
It is very advisable to take a look in on user manual [MKS CANable V2.0 User Manual](https://github.com/makerbase-mks/CANable-MKS/blob/main/User%20Manual/CANable%20V2.0/Makerbase%20CANable%20V2.0%20Use%20Manual.pdf) [[2]](#id4) and
schematic [MKS CANable V2.0 schematic](https://github.com/makerbase-mks/CANable-MKS/blob/main/Hardware/MKS%20CANable%20V2.0/MKS%20CANable%20V2.0_001%20schematic.pdf) [[3]](#id6) before start.

More information about STM32G431KB can be found here:

- [STM32G431C8 on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32g431c8.html) [[4]](#id10)
- [STM32G4 reference manual](https://www.st.com/resource/en/reference_manual/rm0440-stm32g4-series-advanced-armbased-32bit-mcus-stmicroelectronics.pdf) [[5]](#id12)

### Supported Features

The `mks_canable_v20` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

#### Default Zephyr Peripheral Mapping:

- CAN\_RX/BOOT0 : PB8
- CAN\_TX : PB9
- D2 : PA15
- D3 : PA0
- USB\_DN : PA11
- USB\_DP : PA12
- SWDIO : PA13
- SWCLK : PA14
- NRST : PG10

For more details please refer to [MKS CANable V2.0 schematic](https://github.com/makerbase-mks/CANable-MKS/blob/main/Hardware/MKS%20CANable%20V2.0/MKS%20CANable%20V2.0_001%20schematic.pdf) [[3]](#id6).

#### System Clock

The MKS CANable V2.0 system clock is driven by internal high speed oscillator.
By default system clock is driven by PLL clock at 160 MHz,
the PLL is driven by the 16 MHz high speed internal oscillator.

The FDCAN1 peripheral is driven by PLLQ, which has 80 MHz frequency.

## Programming and Debugging

MKS CANable V2.0 board includes an SWDIO debug connector header J4.

Note

The debugger is not the part of the board!

Applications for the `mks_canable_v20` board target can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board could be flashed using west.

#### Flashing an application to MKS CANable V2.0

The debugger shall be wired to MKS CANable V2.0 board’s J4 connector
according [MKS CANable V2.0 schematic](https://github.com/makerbase-mks/CANable-MKS/blob/main/Hardware/MKS%20CANable%20V2.0/MKS%20CANable%20V2.0_001%20schematic.pdf) [[3]](#id6).

Build and flash an application. Here is an example for
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.").

```shell
west build -b mks_canable_v20 -S rtt-console samples/hello_world
west flash
```

The argument `-S rtt-console` is needed for debug purposes with SEGGER RTT protocol.
This option is optional and may be omitted. Omitting it frees up RAM space but prevents RTT usage.

If option `-S rtt-console` is selected, the connection to the target can be established as follows:

```shell
$ telnet localhost 9090
```

You should see the following message on the console:

```shell
$ Hello World! mks_canable_v20/stm32g431xx
```

Note

Current OpenOCD config will skip Segger RTT for OpenOCD under 0.12.0.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b mks_canable_v20 samples/hello_world
west debug
```

## References

[[1](#id3)]

[https://github.com/makerbase-mks/CANable-MKS](https://github.com/makerbase-mks/CANable-MKS)

[[2](#id5)]

[https://github.com/makerbase-mks/CANable-MKS/blob/main/User%20Manual/CANable%20V2.0/Makerbase%20CANable%20V2.0%20Use%20Manual.pdf](https://github.com/makerbase-mks/CANable-MKS/blob/main/User%20Manual/CANable%20V2.0/Makerbase%20CANable%20V2.0%20Use%20Manual.pdf)

[3]
([1](#id7),[2](#id8),[3](#id9))

[https://github.com/makerbase-mks/CANable-MKS/blob/main/Hardware/MKS%20CANable%20V2.0/MKS%20CANable%20V2.0\_001%20schematic.pdf](https://github.com/makerbase-mks/CANable-MKS/blob/main/Hardware/MKS%20CANable%20V2.0/MKS%20CANable%20V2.0_001%20schematic.pdf)

[[4](#id11)]

[https://www.st.com/en/microcontrollers-microprocessors/stm32g431c8.html](https://www.st.com/en/microcontrollers-microprocessors/stm32g431c8.html)

[[5](#id13)]

[https://www.st.com/resource/en/reference\_manual/rm0440-stm32g4-series-advanced-armbased-32bit-mcus-stmicroelectronics.pdf](https://www.st.com/resource/en/reference_manual/rm0440-stm32g4-series-advanced-armbased-32bit-mcus-stmicroelectronics.pdf)

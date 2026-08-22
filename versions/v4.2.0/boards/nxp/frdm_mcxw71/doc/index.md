---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/frdm_mcxw71/doc/index.html
original_path: boards/nxp/frdm_mcxw71/doc/index.html
---

# FRDM-MCXW71

Board Overview

[![../../../../_images/frdm_mcxw71.webp](../../../../_images/frdm_mcxw71.webp)
](../../../../_images/frdm_mcxw71.webp)

FRDM-MCXW71

Name:
:   `frdm_mcxw71`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mcxw716c

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/frdm_mcxw71/doc/index.rst/../..)

## Overview

The FRDM-MCXW71 is a compact and scalable development board for rapid
prototyping of the MCX W71 wireless MCU. It offers easy evaluation of the MCX
W71’s multiprotocol wireless support for Bluetooth LE, Zigbee, Thread and
Matter. The board includes an on-board MCU-Link debugger, industry standard
headers for easy access to the MCU’s I/Os, an accelerometer, a light sensor and
external SPI flash memory.

The MCX W71x family features a 96 MHz Arm® Cortex®-M33 core coupled with a
multiprotocol radio subsystem supporting Matter, Thread, Zigbee and Bluetooth
LE. The independent radio subsystem, with a dedicated core and memory, offloads
the main CPU, preserving it for the primary application and allowing firmware
updates to support future wireless standards.

## Hardware

- MCXW71 Arm Cortex-M33 microcontroller running up to 96 MHz
- 1MB on-chip Flash memory unit
- 128 KB TCM RAM
- On-board MCU-Link debugger with CMSIS-DAP

For more information about the MCXW71 SoC and FRDM-MCXW71 board, see:

- [MCXW71 SoC Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/mcx-arm-cortex-m/mcx-w-series-microcontrollers/mcx-w71x-secure-and-ultra-low-power-mcus-for-matter-thread-zigbee-and-bluetooth-le:MCX-W71X) [[8]](#id20)
- [FRDM-MCXW71 Website](https://www.nxp.com/design/design-center/development-boards-and-designs/general-purpose-mcus/frdm-development-board-for-mcx-w71x-wireless-mcus:FRDM-MCXW71) [[9]](#id22)

### Supported Features

The `frdm_mcxw71` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

## Fetch Binary Blobs

To support Bluetooth, frdm\_mcxw71 requires fetching binary blobs, which can be
achieved by running the following command:

```shell
west blobs fetch hal_nxp
```

## Programming and Debugging

The `frdm_mcxw71` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the MCU-Link CMSIS-DAP Onboard Debug Probe.

#### Using LinkServer

Linkserver is the default runner for this board, and supports the factory
default MCU-Link firmware. Follow the instructions in
[MCU-Link CMSIS-DAP Onboard Debug Probe](../../../../develop/flash_debug/probes.md#mcu-link-cmsis-onboard-debug-probe) to reprogram the default MCU-Link
firmware. This only needs to be done if the default onboard debug circuit
firmware was changed. To put the board in `DFU mode` to program the firmware,
short jumper J5.

#### Using J-Link

There are two options. The onboard debug circuit can be updated with Segger
J-Link firmware by following the instructions in
[MCU-Link JLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#mcu-link-jlink-onboard-debug-probe).
To be able to program the firmware, you need to put the board in `DFU mode`
by shortening the jumper JP5.
The second option is to attach a [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe) to the
10-pin SWD connector (J12) of the board.
For both options use the `-r jlink` option with west to use the jlink runner.

```shell
west flash -r jlink
```

### Configuring a Console

Connect a USB cable from your PC to J10, and use the serial terminal of your choice
(minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Application Building

#### Openthread applications

```shell
# From the root of the zephyr repository
west build -b frdm_mcxw71 samples/net/sockets/echo_server -- -DEXTRA_CONF_FILE=overlay-ot.conf
```

```shell
# From the root of the zephyr repository
west build -b frdm_mcxw71 samples/net/sockets/echo_client -- -DEXTRA_CONF_FILE=overlay-ot.conf
```

### Application Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b frdm_mcxw71/mcxw716c samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```shell
*** Booting Zephyr OS build v3.7.0-xxx-xxxx ***
Hello World! frdm_mcxw71/mcxw716c
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b frdm_mcxw71/mcxw716c samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
*** Booting Zephyr OS build v3.7.0-xxx-xxxx ***
Hello World! frdm_mcxw71/mcxw716c
```

### NBU Flashing

BLE functionality requires to fetch binary blobs, so make sure to follow
the `Fetch Binary Blobs` section first.

Two images must be written to the board: one for the host (CM33) and one for the NBU (CM3).

- To flash the application (CM33) refer to the `Application Flashing` section above.
- To flash the `NBU Flashing`, follow the instructions below:

  > - Install `blhost` from NXP’s website. This is the tool that will allow you to flash the NBU.
  > - Enter ISP mode. To boot the MCU in ISP mode, follow these steps:
  >   :   - Disconnect the `FRDM-MCXW71` board from all power sources.
  >       - Keep the `SW3` (ISP) button on the board pressed, while connecting the board to the host computer USB port.
  >       - Release the `SW3` (ISP) button. The MCXW71 MCU boots in ISP mode.
  >       - Reconnect any external power supply, if needed.
  > - Use the following command to flash NBU file:

BLE NBU - WindowsBLE NBU - LinuxDYN NBU - WindowsDYN NBU - Linux

Flash BLE only NBU on Windows

```shell
blhost.exe -p COMxx -- receive-sb-file mcxw71_nbu_ble.sb3
```

Flash BLE only NBU on Linux

```shell
./blhost -p /dev/ttyxx -- receive-sb-file mcxw71_nbu_ble.sb3
```

Flash Dynamic NBU (BLE + 15.4) on Windows

```shell
blhost.exe -p COMxx -- receive-sb-file mcxw71_nbu_ble_15_4_dyn.sb3
```

Flash Dynamic NBU (BLE + 15.4) on Linux

```shell
./blhost -p /dev/ttyxx -- receive-sb-file mcxw71_nbu_ble_15_4_dyn.sb3
```

Please consider changing `COMxx` on Windows or `ttyxx` on Linux to the serial port used by your board.

The NBU files can be found in : `<zephyr workspace>/modules/hal/nxp/zephyr/blobs/mcxw71/` folder.

For more details:

### Troubleshooting

#### Using Segger SystemView and RTT

Note that when using SEGGER SystemView or RTT with this SOC, the RTT control
block address must be set manually within SystemView or the RTT Viewer. The
address provided to the tool should be the location of the `_SEGGER_RTT`
symbol, which can be found using a debugger or by examining the `zephyr.map`
file output by the linker.

The RTT control block address must be provided manually because this SOC
supports ECC RAM. If the SEGGER tooling searches the ECC RAM space for the
control block a fault will occur, provided that ECC is enabled and the RAM
segment being searched has not been initialized to a known value.

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk) [[1]](#id6)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC) [[2]](#id8), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) [[3]](#id10) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started) [[4]](#id12)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548) [[5]](#id14)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) [[6]](#id16) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project) [[7]](#id18)

## References

[[1](#id7)]

[https://github.com/nxp-zephyr/nxp-zsdk](https://github.com/nxp-zephyr/nxp-zsdk)

[[2](#id9)]

[https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC)

[[3](#id11)]

[https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki)

[[4](#id13)]

[https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)

[[5](#id15)]

[https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)

[[6](#id17)]

[https://nxp.com/zephyr](https://nxp.com/zephyr)

[[7](#id19)]

[https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

[[8](#id21)]

[https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/mcx-arm-cortex-m/mcx-w-series-microcontrollers/mcx-w71x-secure-and-ultra-low-power-mcus-for-matter-thread-zigbee-and-bluetooth-le:MCX-W71X](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/mcx-arm-cortex-m/mcx-w-series-microcontrollers/mcx-w71x-secure-and-ultra-low-power-mcus-for-matter-thread-zigbee-and-bluetooth-le:MCX-W71X)

[[9](#id23)]

[https://www.nxp.com/design/design-center/development-boards-and-designs/general-purpose-mcus/frdm-development-board-for-mcx-w71x-wireless-mcus:FRDM-MCXW71](https://www.nxp.com/design/design-center/development-boards-and-designs/general-purpose-mcus/frdm-development-board-for-mcx-w71x-wireless-mcus:FRDM-MCXW71)

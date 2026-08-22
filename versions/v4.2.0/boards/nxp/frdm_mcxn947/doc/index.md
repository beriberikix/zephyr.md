---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/frdm_mcxn947/doc/index.html
original_path: boards/nxp/frdm_mcxn947/doc/index.html
---

# FRDM-MCXN947

Board Overview

[![../../../../_images/frdm_mcxn947.webp](../../../../_images/frdm_mcxn947.webp)
](../../../../_images/frdm_mcxn947.webp)

FRDM-MCXN947

Name:
:   `frdm_mcxn947`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mcxn947

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/frdm_mcxn947/doc/index.rst/../..)

## Overview

FRDM-MCXN947 are compact and scalable development boards for rapid prototyping of
MCX N94 and N54 MCUs. They offer industry standard headers for easy access to the
MCUs I/Os, integrated open-standard serial interfaces, external flash memory and
an on-board MCU-Link debugger. MCX N Series are high-performance, low-power
microcontrollers with intelligent peripherals and accelerators providing multi-tasking
capabilities and performance efficiency.

## Hardware

- MCX-N947 Dual Arm Cortex-M33 microcontroller running at 150 MHz
- 2MB dual-bank on chip Flash
- 512 KB RAM
- External Quad SPI flash over FlexSPI
- USB high-speed (Host/Device) with on-chip HS PHY. HS USB Type-C connectors
- 10x LP Flexcomms each supporting SPI, I2C, UART
- 2x FlexCAN with FD, 2x I3Cs, 2x SAI
- 1x Ethernet with QoS
- On-board MCU-Link debugger with CMSIS-DAP
- Arduino Header, FlexIO/LCD Header, SmartDMA/Camera Header, mikroBUS

For more information about the MCX-N947 SoC and FRDM-MCXN947 board, see:

- [MCX-N947 SoC Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/mcx-arm-cortex-m/mcx-n-series-microcontrollers/mcx-n94x-54x-highly-integrated-multicore-mcus-with-on-chip-accelerators-intelligent-peripherals-and-advanced-security:MCX-N94X-N54X)
- [MCX-N947 Datasheet](https://www.nxp.com/docs/en/data-sheet/MCXNx4xDS.pdf)
- [MCX-N947 Reference Manual](https://www.nxp.com/webapp/Download?colCode=MCXNX4XRM)
- [FRDM-MCXN947 Website](https://www.nxp.com/design/design-center/development-boards/general-purpose-mcus/frdm-development-board-for-mcx-n94-n54-mcus:FRDM-MCXN947)
- [FRDM-MCXN947 User Guide](https://www.nxp.com/document/guide/getting-started-with-frdm-mcxn947:GS-FRDM-MCXNXX)
- [FRDM-MCXN947 Board User Manual](https://www.nxp.com/webapp/Download?colCode=UM12018)
- [FRDM-MCXN947 Schematics](https://www.nxp.com/webapp/Download?colCode=90818-MCXN947SH)

### Supported Features

The `frdm_mcxn947` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

## Dual Core samples

| Core | Flash Region | Comment |
| --- | --- | --- |
| CPU0 | Full flash memory (including partition slot0\_partition) | Primary core with bootloader access and application in slot0\_partition |
| CPU1 | slot1\_partition only | Secondary core restricted to its dedicated partition |

| Memory | Region | Comment |
| --- | --- | --- |
| srama | RAM (320KB) | CPU0 ram |
| sramg | RAM (64KB) | CPU1 ram |
| sramh | RAM (32KB) | Shared memory |

Note

The actual memory addresses are defined in the device tree and can be viewed in the
generated map files after building. CPU0 accesses the full flash memory starting from
its base address, while CPU1 is restricted to the slot1\_partition region.

### Targets available

The default configuration file
[boards/nxp/frdm\_mcxn947/frdm\_mcxn947\_mcxn947\_cpu0\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxn947/frdm_mcxn947_mcxn947_cpu0_defconfig)
only enables the first core. CPU0 is the only target that can run standalone.

CPU1 does not work without CPU0 enabling it.

To enable CPU1, create System Build application project and enable the
second core with config [`CONFIG_SECOND_CORE_MCUX`](../../../../kconfig.md#CONFIG_SECOND_CORE_MCUX "CONFIG_SECOND_CORE_MCUX").

Please have a look at some already enabled samples:

- [samples/subsys/ipc/ipc\_service/static\_vrings](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/ipc/ipc_service/static_vrings)
- [samples/subsys/ipc/openamp](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/ipc/openamp)
- [samples/drivers/mbox](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/mbox)
- [samples/drivers/mbox\_data](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/mbox_data)

### Connections and IOs

The MCX-N947 SoC has 6 gpio controllers and has pinmux registers which
can be used to configure the functionality of a pin.

| Name | Function | Usage |
| --- | --- | --- |
| P0\_PIO1\_8 | UART | UART RX cpu0 |
| P1\_PIO1\_9 | UART | UART TX cpu0 |
| P4\_PIO4\_3 | UART | UART RX cpu1 |
| P4\_PIO4\_2 | UART | UART TX cpu1 |

### System Clock

The MCX-N947 SoC is configured to use PLL0 running at 150MHz as a source for
the system clock.

### Serial Port

The FRDM-MCXN947 SoC has 10 FLEXCOMM interfaces for serial communication.
Flexcomm 4 is configured as UART for the console.

## Programming and Debugging

The `frdm_mcxn947` board supports the runners and associated west commands listed below.

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
short jumper J21.

#### Using J-Link

There are two options. The onboard debug circuit can be updated with Segger
J-Link firmware by following the instructions in
[MCU-Link JLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#mcu-link-jlink-onboard-debug-probe).
To be able to program the firmware, you need to put the board in `DFU mode`
by shortening the jumper J21.
The second option is to attach a [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe) to the
10-pin SWD connector (J23) of the board. Additionally, the jumper J19 must
be shortened.
For both options use the `-r jlink` option with west to use the jlink runner.

```shell
west flash -r jlink
```

### Configuring a Console

Connect a USB cable from your PC to J17, and use the serial terminal of your choice
(minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b frdm_mcxn947/mcxn947/cpu0 samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```shell
*** Booting Zephyr OS build v3.6.0-479-g91faa20c6741 ***
Hello World! frdm_mcxn947/mcxn947/cpu0
```

#### Building a dual-core image

The dual-core samples are run using `frdm_mcxn947/mcxn947/cpu0` target.

Images built for `frdm_mcxn947/mcxn947/cpu1` will be loaded from flash
and executed on the second core when [`CONFIG_SECOND_CORE_MCUX`](../../../../kconfig.md#CONFIG_SECOND_CORE_MCUX "CONFIG_SECOND_CORE_MCUX") is selected.

For an example of building for both cores with System Build, see
[samples/subsys/ipc/ipc\_service/static\_vrings](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/ipc/ipc_service/static_vrings)

Here is an example for the [MBOX Data](../../../../samples/drivers/mbox_data/README.md#mbox_data "Perform inter-processor mailbox communication using the MBOX API with data.") application.

```shell
west build -b frdm_mcxn947/mcxn947/cpu0 --sysbuild zephyr/samples/drivers/mbox_data
west flash
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b frdm_mcxn947/mcxn947/cpu0 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
*** Booting Zephyr OS build v3.6.0-479-g91faa20c6741 ***
Hello World! frdm_mcxn947/mcxn947/cpu0
```

#### Debugging a dual-core image

For dual core builds, the secondary core should be placed into a loop,
then a debugger can be attached.
As a reference please see ([AN13264](https://www.nxp.com/docs/en/application-note/AN13264.pdf), section 4.2.3 for more information).
The reference is for the RT1170 but similar technique can be also used here.

### Using QSPI board variant

The FRDM-MCXN947 board includes an external QSPI flash. The MCXN947 can boot and
XIP directly from this flash using the FlexSPI interface. The QSPI variant
enables building applications and code to execute from the QSPI.

#### Programming the ROM bootloader for external QSPI

By default, the MCXN947 bootloader in ROM will boot using internal flash. But
the MCU can be programmed to boot from external memory on the FlexSPI interface.
Before using the QSPI board variant, the board should be programmed to boot from
QSPI using the steps below.

To configure the ROM bootloader, the Protected Flash Region (PFR) must be
programmed. Programming the PFR is done using NXP’s ROM bootloader tools.
Some simple steps are provided in NXP’s
[MCUXpresso SDK example hello\_world\_qspi\_xip readme](https://github.com/nxp-mcuxpresso/mcuxsdk-examples/blob/main/_boards/frdmmcxn947/demo_apps/hello_world_qspi_xip/example_board_readme.md). The binary to program
with blhost is found at [bootfromflexspi.bin](https://github.com/nxp-mcuxpresso/mcuxsdk-examples/blob/main/_boards/frdmmcxn947/demo_apps/hello_world_qspi_xip/cm33_core0/bootfromflexspi.bin). A much more detailed explanation
is available at this post [Running code from external memory with MCX N94x](https://community.nxp.com/t5/MCX-Microcontrollers-Knowledge/Running-code-from-external-memory-with-MCX-N94x/ta-p/1792204).
The steps below program the FRDM-MCXN947 board. Note that these steps interface
to the ROM bootloader through the UART serial port, but USB is another option.

1. Disconnect any terminal from the UART serial port, since these steps use that
   serial port.
2. Connect a USB Type-C cable to the host computer and J17 on the board, in the
   upper left corner. This powers the board, connects the debug probe, and
   connects the UART serial port used for the `blhost` command.
3. Place the MCU in ISP mode. On the FRDM-MCXN947 board, the ISP button
   can be used for this. Press and hold the ISP button SW3, on the bottom right
   corner of the board. Press and release the Reset button SW1 on the upper left
   corner of the board. The MCU has booted into ISP mode. Release the ISP
   button.
4. Run the `blhost` command:

UbuntuWindows

This step assumes the MCU serial port is connected to /dev/ttyACM0

```shell
blhost -t 2000 -p /dev/ttyACM0,115200 -j -- write-memory 0x01004000 bootfromflexspi.bin
```

Change COMxx to match the COM port number connected to the MCU serial port.

```shell
blhost -t 2000 -p COMxx -j -- write-memory 0x01004000 bootfromflexspi.bin
```

Successful programming should look something like this:

```shell
$ blhost -t 2000 -p /dev/ttyACM0,115200 -j -- write-memory 0x01004000 bootfromflexspi.bin
{
   "command": "write-memory",
   "response": [
      256
   ],
   "status": {
      "description": "0 (0x0) Success.",
      "value": 0
   }
}
```

5. Reset the board with SW1 to exit ISP mode. Now the MCU is ready to boot from
   QSPI.

The ROM bootloader can be configured to boot from internal flash again. Repeat
the steps above to program the PFR, and program the file [bootfromflash.bin](https://github.com/nxp-mcuxpresso/mcuxsdk-examples/blob/main/_boards/frdmmcxn947/demo_apps/hello_world_qspi_xip/cm33_core0/bootfromflash.bin).

#### Build, flash, and debug with the QSPI variant

Once the PFR is programmed to boot from QSPI, the normal Zephyr steps to build,
flash, and debug can be used with the QSPI board variant. Here are some examples.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application:

```shell
west build -b frdm_mcxn947//cpu0/qspi zephyr/samples/hello_world
west flash
```

MCUboot can also be used with the QSPI variant. By default, this places the
MCUboot bootloader in the `boot-partition` in QSPI flash, with the application
images. The ROM bootloader will boot first and load MCUboot in the QSPI, which
will load the app. This example builds and loads the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")
sample with MCUboot using Sysbuild:

```shell
west build -b frdm_mcxn947//cpu0/qspi --sysbuild zephyr/samples/basic/blinky -- -DSB_CONFIG_BOOTLOADER_MCUBOOT=y
west flash
```

Open a serial terminal, reset the board with the SW1 button, and the console
will print:

```shell
*** Booting MCUboot vX.Y.Z ***
*** Using Zephyr OS build vX.Y.Z ***
I: Starting bootloader
I: Image index: 0, Swap type: none
I: Bootloader chainload address offset: 0x14000
I: Image version: v0.0.0
I: Jumping to the first image slot
*** Booting Zephyr OS build vX.Y.Z ***
LED state: OFF
LED state: ON
```

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

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

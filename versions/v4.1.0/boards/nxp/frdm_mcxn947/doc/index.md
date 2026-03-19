---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/nxp/frdm_mcxn947/doc/index.html
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

The FRDM-MCXN947 board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| UART | on-chip | serial port-polling; serial port-interrupt |
| SPI | on-chip | spi |
| DMA | on-chip | dma |
| I2C | on-chip | i2c |
| I3C | on-chip | i3c |
| CLOCK | on-chip | clock\_control |
| FLASH | on-chip | soc flash |
| FLEXSPI | on-chip | flash programming |
| DAC | on-chip | dac |
| ENET QOS | on-chip | ethernet |
| WATCHDOG | on-chip | watchdog |
| PWM | on-chip | pwm |
| SCTimer | on-chip | pwm |
| CTIMER | on-chip | counter |
| USDHC | on-chip | sdhc |
| VREF | on-chip | regulator |
| ADC | on-chip | adc |
| HWINFO | on-chip | Unique device serial number |
| USBHS | on-chip | USB device |
| LPCMP | on-chip | sensor(comparator) |
| FLEXCAN | on-chip | CAN |
| LPTMR | on-chip | counter |
| FLEXIO | on-chip | flexio |
| SAI | on-chip | i2s |
| DISPLAY | on-chip | flexio; MIPI-DBI. Tested with [NXP LCD\_PAR\_S035 TFT LCD Module](../../../shields/lcd_par_s035/doc/index.md#lcd-par-s035) |
| MRT | on-chip | counter |

## Dual Core samples

| Core | Boot Address | Comment |
| --- | --- | --- |
| CPU0 | 0x10000000[1856K] | primary core flash |
| CPU1 | 0x101d0000[192K] | secondary core flash |

| Memory | Address[Size] | Comment |
| --- | --- | --- |
| srama | 0x20000000[320k] | CPU0 ram |
| sramg | 0x20050000[64k] | CPU1 ram |
| sramh | 0x20060000[32k] | Shared memory |

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

### Flashing to QSPI

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
west build -b frdm_mcxn947/mcxn947/cpu0/qspi zephyr/samples/hello_world -- -DCONFIG_MCUBOOT_SIGNATURE_KEY_FILE=\"bootloader/mcuboot/root-rsa-2048.pem\" -DCONFIG_BOOTLOADER_MCUBOOT=y
west flash
```

In order to load Zephyr application from QSPI you should program a bootloader like
MCUboot bootloader to internal flash. Here are the steps.

```shell
west build -b frdm_mcxn947/mcxn947/cpu0/qspi bootloader/mcuboot/boot/zephyr
west flash
```

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```shell
*** Booting MCUboot v2.1.0-rc1-2-g9f034729d99a ***
*** Using Zephyr OS build v3.6.0-4046-gf279a03af8ab ***
I: Starting bootloader
I: Primary image: magic=unset, swap_type=0x1, copy_done=0x3, image_ok=0x3
I: Secondary image: magic=unset, swap_type=0x1, copy_done=0x3, image_ok=0x3
I: Boot source: none
I: Image index: 0, Swap type: none
I: Bootloader chainload address offset: 0x0
I: Jumping to the first image slot
*** Booting Zephyr OS build v3.6.0-4046-gf279a03af8ab ***
Hello World! frdm_mcxn947/mcxn947/cpu0/qspi
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

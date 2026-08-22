---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/twr_ke18f/doc/index.html
original_path: boards/nxp/twr_ke18f/doc/index.html
---

# TWR-KE18F

Board Overview

[![../../../../_images/TWR-KE18F-DEVICE.jpg](../../../../_images/TWR-KE18F-DEVICE.jpg)
](../../../../_images/TWR-KE18F-DEVICE.jpg)

TWR-KE18F

Name:
:   `twr_ke18f`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mke18f16

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/twr_ke18f/doc/index.rst/../..)

## Overview

The TWR-KE18F is a development board for NXP Kinetis KE1xF 32-bit
MCU-based platforms. The onboard OpenSDAv2 serial and debug adapter,
running an open source bootloader, offers options for serial
communication, flash programming, and run-control debugging.

## Hardware

- MKE18F512VLL16 MCU (up to 168 MHz, 512 KB flash memory, 64 KB RAM,
  and 100 Low profile Quad Flat Package (LQFP))
- 3.3 V or 5 V MCU operation
- 6-axis FXOS8700CQ digital accelerometer and magnetometer
- RGB LED
- Four user LEDs
- Two user push-buttons
- Potentiometer
- Thermistor
- Infrared port (IrDA)
- CAN pin header
- Flex I/O pin header

For more information about the KE1xF SoC and the TWR-KE18F board, see
these NXP reference documents:

- [KE1xF Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/kinetis-cortex-m-mcus/e-series5v-robustm0-plus-m4/kinetis-ke1xf-168mhz-performance-with-can-5v-microcontrollers-based-on-arm-cortex-m4:KE1xF)
- [KE1xF Datasheet](https://www.nxp.com/docs/en/data-sheet/KE1xFP100M168SF0.pdf)
- [KE1xF Reference Manual](https://www.nxp.com/docs/en/reference-manual/KE1xFP100M168SF0RM.pdf)
- [TWR-KE18F Website](https://www.nxp.com/TWR-KE18F)
- [TWR-KE18F User Guide](https://www.nxp.com/docs/en/user-guide/TWRKE18FUG.pdf)
- [TWR-KE18F Schematics](https://www.nxp.com/webapp/Download?colCode=TWR-KE18F-SCH-DESIGNFILES)

### Supported Features

The `twr_ke18f` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### System Clock

The KE18 SoC is configured to use the 8 MHz external oscillator on the
board with the on-chip PLL to generate a 120 MHz system clock.

### Serial Port

The KE18 SoC has three UARTs. UART0 is configured for the console. The
remaining UARTs are not used.

### Accelerometer and magnetometer

The TWR-KE18F board by default only supports polling the FXOS8700
accelerometer and magnetometer for sensor values
(`CONFIG_FXOS8700_TRIGGER_NONE=y`).

In order to support FXOS8700 triggers (interrupts) the 0 ohm resistors
`R47` and `R57` must be mounted on the TWR-KE18F board. The
devicetree must also be modified to describe the FXOS8700 interrupt
GPIOs:

```devicetree
/dts-v1/;

&fxos8700 {
        int1-gpios = <&gpioa 14 0>;
        int2-gpios = <&gpioc 17 0>;
};
```

Finally, a trigger option must be enabled in Kconfig (either
`FXOS8700_TRIGGER_GLOBAL_THREAD=y` or
`FXOS8700_TRIGGER_OWN_THREAD=y`).

## Programming and Debugging

The `twr_ke18f` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe).

Early versions of this board have an outdated version of the OpenSDA bootloader
and require an update. Please see the [DAPLink Bootloader Update](https://os.mbed.com/blog/entry/DAPLink-bootloader-update/) page for
instructions to update from the CMSIS-DAP bootloader to the DAPLink bootloader.

#### Option 1: [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe) (Recommended)

Install the [pyOCD Debug Host Tools](../../../../develop/flash_debug/host-tools.md#pyocd-debug-host-tools) and make sure they are in your search
path.

Follow the instructions in [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe) to program
the [OpenSDA DAPLink TWR-KE18F Firmware](https://www.nxp.com/support/developer-resources/run-time-software/kinetis-developer-resources/ides-for-kinetis-mcus/opensda-serial-and-debug-adapter:OPENSDA#TWR-KE18F).

#### Option 2: [OpenSDA J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-jlink-onboard-debug-probe)

Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search
path.

Follow the instructions in [OpenSDA J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-jlink-onboard-debug-probe) to program
the [OpenSDA J-Link Firmware for TWR-KE18F](https://www.segger.com/downloads/jlink/OpenSDA_TWR-KE18F).

Add the arguments `-DBOARD_FLASH_RUNNER=jlink` and
`-DBOARD_DEBUG_RUNNER=jlink` when you invoke `west build` to override the
default runner from pyOCD to J-Link:

```shell
# From the root of the zephyr repository
west build -b twr_ke18f samples/hello_world -- -DBOARD_FLASH_RUNNER=jlink -DBOARD_DEBUG_RUNNER=jlink
```

### Configuring a Console

Regardless of your choice in debug probe, we will use the OpenSDA
microcontroller as a usb-to-serial adapter for the serial console.

Connect a USB cable from your PC to J2.

Use the following settings with your serial terminal of choice (minicom, putty,
etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b twr_ke18f samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the SW1 button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-xxx-gxxxxxxxxxxxx *****
Hello World! twr_ke18f
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b twr_ke18f samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-xxx-gxxxxxxxxxxxx *****
Hello World! twr_ke18f
```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/ti/cc3220sf_launchxl/doc/index.html
original_path: boards/ti/cc3220sf_launchxl/doc/index.html
---

# CC3220SF LaunchXL

Board Overview

Name:
:   `cc3220sf_launchxl`

Vendor:
:   Texas Instruments

Architecture:
:   arm

SoC:
:   cc3220sf

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ti/cc3220sf_launchxl/doc/index.rst/../..)

## Overview

The SimpleLink Wi-Fi CC3220SF LaunchPad development kit (CC3220SF-LAUNCHXL)
highlights CC3220SF, a single-chip wireless microcontroller (MCU) with
1MB internal flash, 4MB external serial flash, 256KB of RAM and enhanced
security features.

See the [TI CC3220 Product Page](http://www.ti.com/product/cc3220) for details.

### Features:

- Two separate execution environments: a user application dedicated ARM
  Cortex-M4 MCU and a network processor MCU to run all Wi-Fi and
  internet logical layers
- 40-pin LaunchPad standard leveraging the BoosterPack ecosystem
- On-board accelerometer and temperature sensor
- Two buttons and three LEDs for user interaction
- UART through USB to PC
- BoosterPack plug-in module for adding graphical displays, audio
  codecs, antenna selection, environmental sensing, and more
- Power from USB for the LaunchPad and optional external BoosterPack
- XDS110-based JTAG emulation with serial port for flash programming

Details on the CC3220SF LaunchXL development board can be found in the
[CC3220SF LaunchPad Dev Kit Hardware User’s Guide](http://www.ti.com/lit/pdf/swru463).

## Hardware

The CC3220SF SoC has two MCUs:

1. Applications MCU - an ARM® Cortex®-M4 Core at 80 MHz, with 256Kb RAM,
   and access to external serial 4MB flash with bootloader and peripheral
   drivers in ROM.
2. Network Coprocessor (NWP) - a dedicated ARM MCU, which completely
   offloads Wi-Fi and internet protocols from the application MCU.

Complete details of the CC3220SF SoC can be found in the [CC3220 TRM](http://www.ti.com/lit/pdf/swru465).

### Supported Features

The `cc3220sf_launchxl` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

Note

For consistency with TI SimpleLink SDK and BoosterPack examples,
the I2C driver defaults to I2C\_BITRATE\_FAST mode (400 kHz) bus speed
on bootup.

The accelerometer, temperature sensors, or other peripherals
accessible through the BoosterPack, are not currently supported.

## Programming and Debugging

TI officially supports development on the CC3220SF using the TI
[CC3220 SDK](http://www.ti.com/tool/download/SIMPLELINK-CC3220-SDK) on Windows and Linux using TI tools: Code Composer
Studio for debugging and [UniFlash](http://processors.wiki.ti.com/index.php/Category:CCS_UniFlash) for flashing.

For Windows developers, see the [CC3220 Getting Started Guide](http://www.ti.com/lit/pdf/swru461) for
instructions on installation of tools, and how to flash the board using
UniFlash.

Note that zephyr.bin produced by the Zephyr SDK may not load via
UniFlash tool. If encountering difficulties, use the zephyr.elf
file and openocd instead (see below).

The following instructions are geared towards Linux developers who
prefer command line tools to an IDE.

Before flashing and debugging the board, there are a few one-time board
setup steps to follow.

### Prerequisites:

1. Download and install the latest version of [UniFlash](http://processors.wiki.ti.com/index.php/Category:CCS_UniFlash).
2. Jumper SOP[2..0] (J15) to [010], and connect the USB cable to the PC.

   This should result in a new device “Texas Instruments XDS110 Embed
   with CMSIS-DAP” appearing at /dev/ttyACM1 and /dev/ttyACM0.
3. Update the service pack, and place the board in “Development Mode”.

   Setting “Development Mode” enables the JTAG interface, necessary
   for subsequent use of OpenOCD and updating XDS110 firmware.

   Follow the instructions in Section 2.4 “Download the Application”,
   in the [CC3220 Getting Started Guide](http://www.ti.com/lit/pdf/swru461), except for steps 5 and 6 in
   Section 2.4.1 which select an MCU image.
4. Ensure the XDS-110 emulation firmware is updated.

   Download and install the latest [XDS-110 emulation package](http://processors.wiki.ti.com/index.php/XDS_Emulation_Software_Package#XDS_Emulation_Software_.28emupack.29_Download).

   Follow these [xds110 firmware update directions](http://software-dl.ti.com/ccs/esd/documents/xdsdebugprobes/emu_xds110.html#updating-the-xds110-firmware)

   Note that the emulation package install may place the xdsdfu utility
   in `<install_dir>/ccs_base/common/uscif/xds110/`.
5. Switch Jumper SOP[2..0] (J15) back to [001].

   Remove power from the board (disconnect USB cable) before switching jumpers.
6. Install OpenOCD

   You can obtain OpenOCD by following these
   [installing the latest Zephyr SDK instructions](../../../../develop/toolchains/zephyr_sdk.md#toolchain-zephyr-sdk).

   After the installation, add the directory containing the OpenOCD executable
   to your environment’s PATH variable. For example, use this command in Linux:

   ```shell
   export PATH=$ZEPHYR_SDK_INSTALL_DIR/sysroots/x86_64-pokysdk-linux/usr/bin/openocd:$PATH
   ```

   If you had previously installed TI OpenOCD, you can simply switch to use
   the one in the Zephyr SDK. If for some reason you wish to continue to use
   your TI OpenOCD installation, you can set the OPENOCD and
   OPENOCD\_DEFAULT\_PATH variables in
   [boards/ti/cc3220sf\_launchxl/board.cmake](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/cc3220sf_launchxl/board.cmake) to point the build
   to the paths of the OpenOCD binary and its scripts, before
   including the common openocd.board.cmake file:

   ```cmake
   set(OPENOCD "/usr/local/bin/openocd" CACHE FILEPATH "" FORCE)
   set(OPENOCD_DEFAULT_PATH /usr/local/share/openocd/scripts)
   include(${ZEPHYR_BASE}/boards/common/openocd.board.cmake)
   ```
7. Ensure CONFIG\_XIP=y (default) is set.

   This locates the program into flash, and sets CONFIG\_CC3220SF\_DEBUG=y,
   which prepends a debug header enabling the flash to persist over
   subsequent reboots, bypassing the bootloader flash signature
   verification.

   See Section 21.10 “Debugging Flash User Application Using JTAG” of the
   [CC3220 TRM](http://www.ti.com/lit/pdf/swru465) for details on the secure flash boot process.

Once the above prerequisites are met, applications for the `_cc3220sf_launchxl`
board can be built, flashed, and debugged with openocd and gdb per the Zephyr
Application Development Primer (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run)).

### Flashing

To build and flash an application, execute the following commands for <my\_app>:

```shell
west build -b cc3220sf_launchxl <my_app>
west flash
```

This will load the image into flash.

To see program output from UART0, connect a separate terminal window:

```shell
% screen /dev/ttyACM0 115200 8N1
```

Then press the reset button (SW1) on the board to run the program.

When using OpenOCD from Zephyr SDK to flash the device, you may notice
the program hangs when starting the network processor on the device, if the
program uses it. There is a known issue with how that version of OpenOCD
resets the network processor. You would need to manually hit the reset button
on the board to properly reset the device after flashing.

### Debugging

To debug a previously flashed image, after resetting the board, use the ‘debug’
build target:

```shell
west build -b cc3220sf_launchxl <my_app>
west debug
```

## Wi-Fi Support

The SimpleLink Host Driver, imported from the SimpleLink SDK, has been ported
to Zephyr, and communicates over a dedicated SPI to the network co-processor.
It is available as a Zephyr Wi-Fi device driver in
[drivers/wifi/simplelink](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/simplelink).

### Usage:

Set [`CONFIG_WIFI_SIMPLELINK`](../../../../kconfig.md#CONFIG_WIFI_SIMPLELINK "CONFIG_WIFI_SIMPLELINK") and [`CONFIG_WIFI`](../../../../kconfig.md#CONFIG_WIFI "CONFIG_WIFI") to `y`
to enable Wi-Fi.
See [samples/net/wifi/shell/boards/cc3220sf\_launchxl.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/wifi/shell/boards/cc3220sf_launchxl.conf).

### Provisioning:

SimpleLink provides a few rather sophisticated Wi-Fi provisioning methods.
To keep it simple for Zephyr development and demos, the SimpleLink
“Fast Connect” policy is enabled, with one-shot scanning.
This enables the cc3220sf\_launchxl to automatically reconnect to the last
good known access point (AP), without having to restart a scan, and
re-specify the SSID and password.

To connect to an AP, first run the Zephyr Wi-Fi shell sample application,
and connect to a known AP with SSID and password.

See [Wi-Fi shell](../../../../samples/net/wifi/shell/README.md#wifi-shell "Test Wi-Fi functionality using the Wi-Fi shell module.")

Once the connection succeeds, the network co-processor keeps the AP identity in
its persistent memory. Newly loaded Wi-Fi applications then need not explicitly
execute any Wi-Fi scan or connect operations, until the need to change to a new AP.

## Secure Socket Offload

The SimpleLink Wi-Fi driver provides socket operations to the Zephyr socket
offload point, enabling Zephyr BSD socket API calls to be directed to the
SimpleLink Wi-Fi driver, by setting [`CONFIG_NET_SOCKETS_OFFLOAD`](../../../../kconfig.md#CONFIG_NET_SOCKETS_OFFLOAD "CONFIG_NET_SOCKETS_OFFLOAD")
to `y`.

Secure socket (TLS) communication is handled as part of the socket APIs,
and enabled by:

- setting both [`CONFIG_NET_SOCKETS_SOCKOPT_TLS`](../../../../kconfig.md#CONFIG_NET_SOCKETS_SOCKOPT_TLS "CONFIG_NET_SOCKETS_SOCKOPT_TLS")
  and [`CONFIG_TLS_CREDENTIAL_FILENAMES`](../../../../kconfig.md#CONFIG_TLS_CREDENTIAL_FILENAMES "CONFIG_TLS_CREDENTIAL_FILENAMES") to `y`,
- using the TI Uniflash tool to program the required certificates and
  keys to the secure flash filesystem, and enabling the TI Trusted
  Root-Certificate Catalog.

See [HTTP GET using plain sockets](../../../../samples/net/sockets/http_get/README.md#sockets-http-get "Implement an HTTP(S) client using plain BSD sockets.") and
[samples/net/sockets/http\_get/boards/cc3220sf\_launchxl.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/http_get/boards/cc3220sf_launchxl.conf) for an
example.

See the document [Simplelink Wi-Fi Certificates Handling](http://www.ti.com/lit/pdf/swpu332) for details on
using the TI UniFlash tool for certificate programming.

## References

CC32xx Wiki:
:   [http://processors.wiki.ti.com/index.php/CC31xx\_%26\_CC32xx](http://processors.wiki.ti.com/index.php/CC31xx_%26_CC32xx)

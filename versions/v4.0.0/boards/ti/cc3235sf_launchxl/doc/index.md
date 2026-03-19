---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/ti/cc3235sf_launchxl/doc/index.html
original_path: boards/ti/cc3235sf_launchxl/doc/index.html
---

# CC3235SF LaunchXL

Board Overview

Vendor:
:   Texas Instruments

Architecture:
:   arm

SoC:
:   cc3235sf

## Overview

The SimpleLink Wi-Fi CC3235SF LaunchPad development kit (CC3235SF-LAUNCHXL)
highlights CC3235SF, a single-chip wireless microcontroller (MCU) with
1MB internal flash, 4MB external serial flash, 256KB of RAM, and enhanced
security features. It supports 802.11 a/b/g/n, both 2.4 GHz and 5 GHz.

See the [TI CC3235 Product Page](http://www.ti.com/product/cc3235SF) [[1]](#id1) for details.

### Features:

- Two separate execution environments: a user application dedicated ARM
  Cortex-M4 MCU and a network processor MCU to run all Wi-Fi and
  internet logical layers
- 40-pin LaunchPad standard leveraging the BoosterPack ecosystem
- On-board accelerometer and temperature sensor
- Two buttons and a RGB LED for user interaction
- UART through USB to PC
- BoosterPack plug-in module for adding graphical displays, audio
  codecs, antenna selection, environmental sensing, and more
- Power from USB for the LaunchPad and optional external BoosterPack
- XDS110-based JTAG emulation with serial port for flash programming

Details on the CC3235SF LaunchXL development board can be found in the
[CC3235SF LaunchPad Dev Kit Hardware User’s Guide](http://www.ti.com/lit/pdf/swru539) [[6]](#id14).

## Hardware

The CC3235SF SoC has two MCUs:

1. Applications MCU - an ARM® Cortex®-M4 Core at 80 MHz, with 256Kb RAM,
   and access to external serial 4MB flash with bootloader and peripheral
   drivers in ROM.
2. Network Coprocessor (NWP) - a dedicated ARM MCU, which completely
   offloads Wi-Fi and internet protocols from the application MCU.

Complete details of the CC3235SF SoC can be found in the [CC3235 TRM](http://www.ti.com/lit/pdf/swru543) [[2]](#id3).

### Supported Features

Zephyr has been ported to the Applications MCU, with basic peripheral
driver support.

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| UART | on-chip | serial port-interrupt |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c |
| SPI\_0 | on-chip | Wi-Fi host driver |

Note

For consistency with TI SimpleLink SDK and BoosterPack examples,
the I2C driver defaults to I2C\_BITRATE\_FAST mode (400 kHz) bus speed
on bootup.

The accelerometer, temperature sensors, or other peripherals
accessible through the BoosterPack, are not currently supported.

## Programming and Debugging

TI officially supports development on the CC3235SF using the TI
[CC32xx SDK](http://www.ti.com/tool/download/SIMPLELINK-CC32xx-SDK/2.40.01.01) [[5]](#id12) on Windows and Linux using TI tools: Code Composer
Studio for debugging and [UniFlash](http://processors.wiki.ti.com/index.php/Category:CCS_UniFlash) [[4]](#id9) for flashing.

For Windows developers, see the [CC32xx Quick Start Guide](http://dev.ti.com/tirex/content/simplelink_cc32xx_sdk_2_40_01_01/docs/simplelink_mcu_sdk/Quick_Start_Guide.html) [[3]](#id6) for
instructions on installation of tools, and how to flash the board using
UniFlash.

Note that `zephyr.bin` produced by the Zephyr SDK may not load via
UniFlash tool. If encountering difficulties, use the `zephyr.elf`
file and openocd instead (see below).

The following instructions are geared towards Linux developers who
prefer command line tools to an IDE.

Before flashing and debugging the board, there are a few one-time board
setup steps to follow.

### Prerequisites:

1. Download and install the latest version of [UniFlash](http://processors.wiki.ti.com/index.php/Category:CCS_UniFlash) [[4]](#id9).
2. Jumper SOP[2..0] (J15) to [010], and connect the USB cable to the PC.

   This should result in a new device “Texas Instruments XDS110 Embed
   with CMSIS-DAP” appearing at /dev/ttyACM1 and /dev/ttyACM0.
3. Update the service pack, and place the board in “Development Mode”.

   Setting “Development Mode” enables the JTAG interface, necessary
   for subsequent use of OpenOCD and updating XDS110 firmware.

   Follow the instructions in Section 2.4 “Download the Application”,
   in the [CC32xx Quick Start Guide](http://dev.ti.com/tirex/content/simplelink_cc32xx_sdk_2_40_01_01/docs/simplelink_mcu_sdk/Quick_Start_Guide.html) [[3]](#id6), except for steps 5 and 6 in
   Section 2.4.1 which select an MCU image.
4. Ensure the XDS-110 emulation firmware is updated.

   Download and install the latest [XDS-110 emulation package](http://processors.wiki.ti.com/index.php/XDS_Emulation_Software_Package#XDS_Emulation_Software_.28emupack.29_Download) [[7]](#id16).

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

   This locates the program into flash, and sets CONFIG\_CC3235SF\_DEBUG=y,
   which prepends a debug header enabling the flash to persist over
   subsequent reboots, bypassing the bootloader flash signature
   verification.

   See Section 21.10 “Debugging Flash User Application Using JTAG” of the
   [CC3235 TRM](http://www.ti.com/lit/pdf/swru543) [[2]](#id3) for details on the secure flash boot process.

Once the above prerequisites are met, applications for the `_cc3235sf_launchxl`
board can be built, flashed, and debugged with openocd and gdb per the Zephyr
Application Development Primer (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run)).

### Flashing

To build and flash an application, execute the following commands for <my\_app>:

```shell
west build -b cc3235sf_launchxl <my_app>
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
west build -b cc3235sf_launchxl <my_app>
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
See [samples/net/wifi/shell/boards/cc3235sf\_launchxl.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/wifi/shell/boards/cc3235sf_launchxl.conf).

### Provisioning:

SimpleLink provides a few rather sophisticated Wi-Fi provisioning methods.
To keep it simple for Zephyr development and demos, the SimpleLink
“Fast Connect” policy is enabled, with one-shot scanning.
This enables the cc3235sf\_launchxl to automatically reconnect to the last
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
[samples/net/sockets/http\_get/boards/cc3235sf\_launchxl.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/http_get/boards/cc3235sf_launchxl.conf) for an
example.

See the document [Simplelink Wi-Fi Certificates Handling](http://www.ti.com/lit/pdf/swpu332) [[8]](#id18) for details on
using the TI UniFlash tool for certificate programming.

## References

[[1](#id2)]

[http://www.ti.com/product/cc3235SF](http://www.ti.com/product/cc3235SF)

[2]
([1](#id4),[2](#id5))

[http://www.ti.com/lit/pdf/swru543](http://www.ti.com/lit/pdf/swru543)

[3]
([1](#id7),[2](#id8))

[http://dev.ti.com/tirex/content/simplelink\_cc32xx\_sdk\_2\_40\_01\_01/docs/simplelink\_mcu\_sdk/Quick\_Start\_Guide.html](http://dev.ti.com/tirex/content/simplelink_cc32xx_sdk_2_40_01_01/docs/simplelink_mcu_sdk/Quick_Start_Guide.html)

[4]
([1](#id10),[2](#id11))

[http://processors.wiki.ti.com/index.php/Category:CCS\_UniFlash](http://processors.wiki.ti.com/index.php/Category:CCS_UniFlash)

[[5](#id13)]

[http://www.ti.com/tool/download/SIMPLELINK-CC32xx-SDK/2.40.01.01](http://www.ti.com/tool/download/SIMPLELINK-CC32xx-SDK/2.40.01.01)

[[6](#id15)]

[http://www.ti.com/lit/pdf/swru539](http://www.ti.com/lit/pdf/swru539)

[[7](#id17)]

[http://processors.wiki.ti.com/index.php/XDS\_Emulation\_Software\_Package#XDS\_Emulation\_Software\_.28emupack.29\_Download](http://processors.wiki.ti.com/index.php/XDS_Emulation_Software_Package#XDS_Emulation_Software_.28emupack.29_Download)

[[8](#id19)]

[http://www.ti.com/lit/pdf/swpu332](http://www.ti.com/lit/pdf/swpu332)

TI SimpleLink MCUs:
:   [http://www.ti.com/microcontrollers/simplelink-mcus/overview.html](http://www.ti.com/microcontrollers/simplelink-mcus/overview.html)

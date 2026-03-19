---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/ti/msp_exp432p401r_launchxl/doc/index.html
original_path: boards/ti/msp_exp432p401r_launchxl/doc/index.html
---

# MSP-EXP432P401R LaunchXL

Board Overview

[![../../../../_images/msp_exp432p401r_launchxl.jpg](../../../../_images/msp_exp432p401r_launchxl.jpg)
](../../../../_images/msp_exp432p401r_launchxl.jpg)

MSP-EXP432P401R LaunchXL

Name:
:   `msp_exp432p401r_launchxl`

Vendor:
:   Texas Instruments

Architecture:
:   arm

SoC:
:   msp432p401r

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ti/msp_exp432p401r_launchxl/doc/index.rst/../..)

## Overview

The SimpleLink MSP‐EXP432P401R LaunchPad development kit is an easy-to-use evaluation
module for the SimpleLink MSP432P401R microcontroller. It contains everything needed to start
developing on the SimpleLink MSP432 low-power + performance ARM® 32-bit Cortex®-M4F
microcontroller (MCU).

### Features:

- Low-power ARM Cortex-M4F MSP432P401R
- 40-pin LaunchPad development kit standard that leverages the BoosterPack plug-in module ecosystem
- XDS110-ET, an open-source onboard debug probe featuring EnergyTrace+ technology and application
  UART
- Two buttons and two LEDs for user interaction
- Backchannel UART through USB to PC

Details on the MSP-EXP432P401R LaunchXL development board can be found in the
MSP-EXP432P401R LaunchXL User’s Guide.

### Supported Features

The `msp_exp432p401r_launchxl` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

- The on-board 32-kHz crystal allows for lower LPM3 sleep currents and a higher-precision clock source than the
  default internal 32-kHz REFOCLK. Therefore, the presence of the crystal allows the full range of low-power
  modes to be used.
- The on-board 48-MHz crystal allows the device to run at its maximum operating speed for MCLK and HSMCLK.

More details about the supported peripherals are available in MSP432P4XX TRM.

## Building and Flashing

### Prerequisites:

1. Ensure the XDS-110 emulation firmware is updated.

   Download and install the latest [XDS-110 emulation package](http://processors.wiki.ti.com/index.php/XDS_Emulation_Software_Package#XDS_Emulation_Software_.28emupack.29_Download) [[1]](#id2).

   Follow these [xds110 firmware update directions](http://software-dl.ti.com/ccs/esd/documents/xdsdebugprobes/emu_xds110.html#updating-the-xds110-firmware)

   Note that the emulation package install may place the xdsdfu utility
   in `<install_dir>/ccs_base/common/uscif/xds110/`.
2. Install OpenOCD

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
   [boards/ti/msp\_exp432p401r\_launchxl/board.cmake](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/msp_exp432p401r_launchxl/board.cmake) to point the build
   to the paths of the OpenOCD binary and its scripts, before
   including the common openocd.board.cmake file:

   ```cmake
   set(OPENOCD "/usr/local/bin/openocd" CACHE FILEPATH "" FORCE)
   set(OPENOCD_DEFAULT_PATH /usr/local/share/openocd/scripts)
   include(${ZEPHYR_BASE}/boards/common/openocd.board.cmake)
   ```

### Flashing

Follow the [Getting Started Guide](../../../../develop/getting_started/index.md#getting-started) instructions for Zephyr application
development.

For example, to build and flash the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application for the
MSP-EXP432P401R LaunchXL:

```shell
# From the root of the zephyr repository
west build -b msp_exp432p401r_launchxl samples/hello_world
west flash
```

This will load the image into flash.

To see program output from UART0, connect a separate terminal window:

```shell
% screen /dev/ttyACM0 115200 8N1
```

Then press the reset button (S3) on the board to run the program.

### Debugging

To debug a previously flashed image, after resetting the board, use the ‘debug’
build target:

```shell
# From the root of the zephyr repository
west build -b msp_exp432p401r_launchxl samples/hello_world
west debug
```

## References

[[1](#id3)]

[http://processors.wiki.ti.com/index.php/XDS\_Emulation\_Software\_Package#XDS\_Emulation\_Software\_.28emupack.29\_Download](http://processors.wiki.ti.com/index.php/XDS_Emulation_Software_Package#XDS_Emulation_Software_.28emupack.29_Download)

TI MSP432 Wiki:
:   [https://en.wikipedia.org/wiki/TI\_MSP432](https://en.wikipedia.org/wiki/TI_MSP432)

TI MSP432P401R Product Page:
:   [http://www.ti.com/product/msp432p401r](http://www.ti.com/product/msp432p401r)

TI MSP432 SDK:
:   [http://www.ti.com/tool/SIMPLELINK-MSP432-SDK](http://www.ti.com/tool/SIMPLELINK-MSP432-SDK)

---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/develop/flash_debug/host-tools.html
original_path: develop/flash_debug/host-tools.html
---

# Flash & Debug Host Tools

This guide describes the software tools you can run on your host workstation to
flash and debug Zephyr applications.

Zephyr’s west tool has built-in support for all of these in its `flash`,
`debug`, `debugserver`, and `attach` commands, provided your board
hardware supports them and your Zephyr board directory’s `board.cmake`
file declares that support properly. See [Building, Flashing and Debugging](../west/build-flash-debug.md#west-build-flash-debug) for
more information on these commands.

## SAM Boot Assistant (SAM-BA)

Atmel SAM Boot Assistant (Atmel SAM-BA) allows In-System Programming (ISP)
from USB or UART host without any external programming interface. Zephyr
allows users to develop and program boards with SAM-BA support using
[west](../west/build-flash-debug.md#west-flashing). Zephyr supports devices with/without ROM
bootloader and both extensions from Arduino and Adafruit. Full support was
introduced in Zephyr SDK 0.12.0.

The typical command to flash the board is:

```shell
west flash [ -r bossac ] [ -p /dev/ttyX ] [ --erase ]
```

Note

By default, flashing with bossac will only erase the flash pages containing
the flashed application, leaving other pages untouched. Should you wish to
erase the entire flash of the target when flashing, pass the `--erase`
parameter when flashing.

Flash configuration for devices:

With ROM bootloaderWithout ROM bootloaderWith compatible SAM-BA bootloader

These devices don’t need any special configuration. After building your
application, just run `west flash` to flash the board.

For these devices, the user should:

1. Define flash partitions required to accommodate the bootloader and
   application image; see [Flash map](../../services/storage/flash_map/flash_map.md#flash-map-api) for details.
2. Have board `.defconfig` file with the
   [`CONFIG_USE_DT_CODE_PARTITION`](../../kconfig.md#CONFIG_USE_DT_CODE_PARTITION "CONFIG_USE_DT_CODE_PARTITION") Kconfig option set to `y` to
   instruct the build system to use these partitions for code relocation.
   This option can also be set in `prj.conf` or any other Kconfig fragment.
3. Build and flash the SAM-BA bootloader on the device.

For these devices, the user should:

1. Define flash partitions required to accommodate the bootloader and
   application image; see [Flash map](../../services/storage/flash_map/flash_map.md#flash-map-api) for details.
2. Have board `.defconfig` file with the
   [`CONFIG_BOOTLOADER_BOSSA`](../../kconfig.md#CONFIG_BOOTLOADER_BOSSA "CONFIG_BOOTLOADER_BOSSA") Kconfig option set to `y`. This will
   automatically select the [`CONFIG_USE_DT_CODE_PARTITION`](../../kconfig.md#CONFIG_USE_DT_CODE_PARTITION "CONFIG_USE_DT_CODE_PARTITION") Kconfig
   option which instruct the build system to use these partitions for code
   relocation. The board `.defconfig` file should have
   [`CONFIG_BOOTLOADER_BOSSA_ARDUINO`](../../kconfig.md#CONFIG_BOOTLOADER_BOSSA_ARDUINO "CONFIG_BOOTLOADER_BOSSA_ARDUINO") ,
   [`CONFIG_BOOTLOADER_BOSSA_ADAFRUIT_UF2`](../../kconfig.md#CONFIG_BOOTLOADER_BOSSA_ADAFRUIT_UF2 "CONFIG_BOOTLOADER_BOSSA_ADAFRUIT_UF2") or the
   [`CONFIG_BOOTLOADER_BOSSA_LEGACY`](../../kconfig.md#CONFIG_BOOTLOADER_BOSSA_LEGACY "CONFIG_BOOTLOADER_BOSSA_LEGACY") Kconfig option set to `y`
   to select the right compatible SAM-BA bootloader mode.
   These options can also be set in `prj.conf` or any other Kconfig fragment.
3. Build and flash the SAM-BA bootloader on the device.

Note

The [`CONFIG_BOOTLOADER_BOSSA_LEGACY`](../../kconfig.md#CONFIG_BOOTLOADER_BOSSA_LEGACY "CONFIG_BOOTLOADER_BOSSA_LEGACY") Kconfig option should be used
as last resource. Try configure first with Devices without ROM bootloader.

### Typical flash layout and configuration

For bootloaders that reside on flash, the devicetree partition layout is
mandatory. For devices that have a ROM bootloader, they are mandatory when
the application uses a storage or other non-application partition. In this
special case, the boot partition should be omitted and code\_partition should
start from offset 0. It is necessary to define the partitions with sizes that
avoid overlaps, always.

A typical flash layout for devices without a ROM bootloader is:

```devicetree
/ {
        chosen {
                zephyr,code-partition = &code_partition;
        };
};

&flash0 {
        partitions {
                compatible = "fixed-partitions";
                #address-cells = <1>;
                #size-cells = <1>;

                boot_partition: partition@0 {
                        label = "sam-ba";
                        reg = <0x00000000 0x2000>;
                        read-only;
                };

                code_partition: partition@2000 {
                        label = "code";
                        reg = <0x2000 0x3a000>;
                        read-only;
                };

                /*
                * The final 16 KiB is reserved for the application.
                * Storage partition will be used by FCB/LittleFS/NVS
                * if enabled.
                */
                storage_partition: partition@3c000 {
                        label = "storage";
                        reg = <0x0003c000 0x00004000>;
                };
        };
};
```

A typical flash layout for devices with a ROM bootloader and storage
partition is:

```devicetree
/ {
        chosen {
                zephyr,code-partition = &code_partition;
        };
};

&flash0 {
        partitions {
                compatible = "fixed-partitions";
                #address-cells = <1>;
                #size-cells = <1>;

                code_partition: partition@0 {
                        label = "code";
                        reg = <0x0 0xF0000>;
                        read-only;
                };

                /*
                * The final 64 KiB is reserved for the application.
                * Storage partition will be used by FCB/LittleFS/NVS
                * if enabled.
                */
                storage_partition: partition@F0000 {
                        label = "storage";
                        reg = <0x000F0000 0x00100000>;
                };
        };
};
```

### Enabling SAM-BA runner

In order to instruct Zephyr west tool to use the SAM-BA bootloader the
`board.cmake` file must have
`include(${ZEPHYR_BASE}/boards/common/bossac.board.cmake)` entry. Note that
Zephyr tool accept more entries to define multiple runners. By default, the
first one will be selected when using `west flash` command. The remaining
options are available passing the runner option, for instance
`west flash -r bossac`.

More implementation details can be found in the [Supported Boards and Shields](../../boards/index.md#boards) documentation.
As a quick reference, see these three board documentation pages:

> - [SAM4E Xplained Pro](../../boards/atmel/sam/sam4e_xpro/doc/index.md#sam4e_xpro) (ROM bootloader)
> - [Feather M0 Basic Proto](../../boards/adafruit/feather_m0_basic_proto/doc/index.md#adafruit_feather_m0_basic_proto) (Adafruit UF2 bootloader)
> - [Arduino Nano 33 IOT](../../boards/arduino/nano_33_iot/doc/index.md#arduino-nano-33-iot) (Arduino bootloader)
> - [Arduino Nano 33 BLE (Sense)](../../boards/arduino/nano_33_ble/doc/index.md#arduino-nano-33-ble) (Arduino legacy bootloader)

### Enabling BOSSAC on Windows Native [Experimental]

Zephyr SDK´s bossac is currently supported on Linux and macOS only. Windows support
can be achieved by using the bossac version from [BOSSA official releases](https://github.com/shumatech/BOSSA/releases).
After installing using default options, the `bossac.exe` must be added to
Windows PATH. A specific bossac executable can be used by passing the
`--bossac` option, as follows:

```shell
west flash -r bossac --bossac="C:\Program Files (x86)\BOSSA\bossac.exe" --bossac-port="COMx"
```

Note

WSL is not currently supported.

## LinkServer Debug Host Tools

Linkserver is a utility for launching and managing GDB servers for NXP debug probes,
which also provides a command-line target flash programming capabilities.
Linkserver can be used with the [NXP MCUXpresso for Visual Studio Code](https://www.nxp.com/design/software/development-software/mcuxpresso-software-and-tools-/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC) implementation,
with custom debug configurations based on GNU tools or as part of a headless solution
for continuous integration and test. LinkServer can be used with MCU-Link, LPC-Link2,
LPC11U35-based and OpenSDA based standalone or on-board debug probes from NXP.

NXP recommends installing LinkServer by using NXP’s [MCUXpresso Installer](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Dependency-Installation).
This method will also install the tools supporting the debug probes below,
including NXP’s MCU-Link and LPCScrypt tools.

LinkServer is compatible with the following debug probes:

- [LPC-LINK2 CMSIS DAP Onboard Debug Probe](probes.md#lpclink2-cmsis-onboard-debug-probe)
- [MCU-Link CMSIS-DAP Onboard Debug Probe](probes.md#mcu-link-cmsis-onboard-debug-probe)
- [OpenSDA DAPLink Onboard Debug Probe](probes.md#opensda-daplink-onboard-debug-probe)

To use LinkServer with West commands, the install folder should be added to the
[`PATH`](../env_vars.md#envvar-PATH) [environment variable](../env_vars.md#env-vars). The default installation
path to add is:

LinuxWindows

```shell
/usr/local/LinkServer
```

```shell
c:\nxp\LinkServer_<version>
```

Supported west commands:

1. flash
2. debug
3. debugserver
4. attach

Notes:

1. Probes can be listed with LinkServer:

```shell
LinkServer probes
```

2. With multiple debug probes attached to the host, use the
LinkServer west runner `--probe` option to pass the probe index.

```shell
west flash --runner=linkserver --probe=3
```

3. Device-specific settings can be overridden with the west runner for LinkServer with
   the option ‘–override’. May be used multiple times. The format is dictated
   by LinkServer, e.g.:

```shell
west flash --runner=linkserver --override /device/memory/5/flash-driver=MIMXRT500_SFDP_MXIC_OSPI_S.cfx
```

4. LinkServer does not install an implicit breakpoint at the reset handler. If
   you would like to single step from the start of their application, you
   will need to add a breakpoint at `main` or the reset handler manually.

## J-Link Debug Host Tools

Segger provides a suite of debug host tools for Linux, macOS, and Windows
operating systems:

- J-Link GDB Server: GDB remote debugging
- J-Link Commander: Command-line control and flash programming
- RTT Viewer: RTT terminal input and output
- SystemView: Real-time event visualization and recording

These debug host tools are compatible with the following debug probes:

- [LPC-Link2 J-Link Onboard Debug Probe](probes.md#lpclink2-jlink-onboard-debug-probe)
- [OpenSDA J-Link Onboard Debug Probe](probes.md#opensda-jlink-onboard-debug-probe)
- [MCU-Link JLink Onboard Debug Probe](probes.md#mcu-link-jlink-onboard-debug-probe)
- [J-Link External Debug Probe](probes.md#jlink-external-debug-probe)
- [ST-LINK/V2-1 Onboard Debug Probe](probes.md#stlink-v21-onboard-debug-probe)

Check if your SoC is listed in [J-Link Supported Devices](https://www.segger.com/downloads/supported-devices.php).

Download and install the [J-Link Software and Documentation Pack](https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack) to get the
J-Link GDB Server and Commander, and to install the associated USB device
drivers. RTT Viewer and SystemView can be downloaded separately, but are not
required.

Note that the J-Link GDB server does not yet support Zephyr RTOS-awareness.

## OpenOCD Debug Host Tools

OpenOCD is a community open source project that provides GDB remote debugging
and flash programming support for a wide range of SoCs. A fork that adds Zephyr
RTOS-awareness is included in the Zephyr SDK; otherwise see [Getting OpenOCD](https://openocd.org/pages/getting-openocd.html)
for options to download OpenOCD from official repositories.

These debug host tools are compatible with the following debug probes:

- [OpenSDA DAPLink Onboard Debug Probe](probes.md#opensda-daplink-onboard-debug-probe)
- [J-Link External Debug Probe](probes.md#jlink-external-debug-probe)
- [ST-LINK/V2-1 Onboard Debug Probe](probes.md#stlink-v21-onboard-debug-probe)

Check if your SoC is listed in [OpenOCD Supported Devices](https://github.com/zephyrproject-rtos/openocd/tree/latest/tcl/target).

Note

On Linux, openocd is available though the [Zephyr SDK](https://github.com/zephyrproject-rtos/sdk-ng/releases).
Windows users should use the following steps to install
openocd:

- Download openocd for Windows from here: [OpenOCD Windows](http://gnutoolchains.com/arm-eabi/openocd/)
- Copy bin and share dirs to `C:\Program Files\OpenOCD\`
- Add `C:\Program Files\OpenOCD\bin` to ‘PATH’ environment variable

## pyOCD Debug Host Tools

pyOCD is an open source project from Arm that provides GDB remote debugging and
flash programming support for Arm Cortex-M SoCs. It is distributed on PyPi and
installed when you complete the [Get Zephyr and install Python dependencies](../getting_started/index.md#gs-python-deps) step in the Getting
Started Guide. pyOCD includes support for Zephyr RTOS-awareness.

These debug host tools are compatible with the following debug probes:

- [LPC-LINK2 CMSIS DAP Onboard Debug Probe](probes.md#lpclink2-cmsis-onboard-debug-probe)
- [MCU-Link CMSIS-DAP Onboard Debug Probe](probes.md#mcu-link-cmsis-onboard-debug-probe)
- [OpenSDA DAPLink Onboard Debug Probe](probes.md#opensda-daplink-onboard-debug-probe)
- [ST-LINK/V2-1 Onboard Debug Probe](probes.md#stlink-v21-onboard-debug-probe)

Check if your SoC is listed in [pyOCD Supported Devices](https://github.com/pyocd/pyOCD/tree/main/pyocd/target/builtin).

## Lauterbach TRACE32 Debug Host Tools

[Lauterbach TRACE32](https://www.lauterbach.com/) is a product line of microprocessor development tools,
debuggers and real-time tracer with support for JTAG, SWD, NEXUS or ETM over
multiple core architectures, including Arm Cortex-A/-R/-M, RISC-V, Xtensa, etc.
Zephyr allows users to develop and program boards with Lauterbach TRACE32
support using [west](../west/build-flash-debug.md#west-flashing).

The runner consists of a wrapper around TRACE32 software, and allows a Zephyr
board to execute a custom start-up script (Practice Script) for the different
commands supported, including the ability to pass extra arguments from CMake.
Is up to the board using this runner to define the actions performed on each
command.

### Install Lauterbach TRACE32 Software

Download Lauterbach TRACE32 software from the [Lauterbach TRACE32 download website](http://www.lauterbach.com/download_trace32.html)
(registration required) and follow the installation steps described in
[Lauterbach TRACE32 Installation Guide](https://www2.lauterbach.com/pdf/installation.pdf).

### Flashing and Debugging

Set the [environment variable](../env_vars.md#env-vars) `T32_DIR` to the TRACE32
system directory. Then execute `west flash` or `west debug` commands to
flash or debug the Zephyr application as detailed in [Building, Flashing and Debugging](../west/build-flash-debug.md#west-build-flash-debug).
The `debug` command launches TRACE32 GUI to allow debug the Zephyr
application, while the `flash` command hides the GUI and perform all
operations in the background.

By default, the `t32` runner will launch TRACE32 using the default
configuration file named `config.t32` located in the TRACE32 system
directory. To use a different configuration file, supply the argument
`--config CONFIG` to the runner, for example:

```shell
west flash --config myconfig.t32
```

For more options, run `west flash --context -r t32` to print the usage.

### Zephyr RTOS Awareness

To enable Zephyr RTOS awareness follow the steps described in
[Lauterbach TRACE32 Zephyr OS Awareness Manual](https://www2.lauterbach.com/pdf/rtos_zephyr.pdf).

## NXP S32 Debug Probe Host Tools

[NXP S32 Debug Probe](probes.md#nxp-s32-debug-probe) is designed to work in conjunction with
[NXP S32 Design Studio for S32 Platform](https://www.nxp.com/design/software/development-software/s32-design-studio-ide/s32-design-studio-for-s32-platform:S32DS-S32PLATFORM).

Download (registration required) NXP S32 Design Studio for S32 Platform and
follow the [S32 Design Studio for S32 Platform Installation User Guide](https://www.nxp.com/webapp/Download?colCode=S32DSIG) to get
the necessary debug host tools and associated USB device drivers.

Note that Zephyr RTOS-awareness support for the NXP S32 GDB server depends on
the target device. Consult the product release notes for more information.

Supported west commands:

1. debug
2. debugserver
3. attach

### Basic usage

Before starting, add NXP S32 Design Studio installation directory to the system
[PATH environment variable](../env_vars.md#env-vars). Alternatively, it can be passed to
the runner on each invocation via `--s32ds-path` as shown below:

LinuxWindows

```shell
west debug --s32ds-path=/opt/NXP/S32DS.3.5
```

```shell
west debug --s32ds-path=C:\NXP\S32DS.3.5
```

If multiple S32 debug probes are connected to the host via USB, the runner will
ask the user to select one via command line prompt before continuing. The
connection string for the probe can be also specified when invoking the runner
via `--dev-id=<connection-string>`. Consult NXP S32 debug probe user manual
for details on how to construct the connection string. For example, if using a
probe with serial ID `00:04:9f:00:ca:fe`:

```shell
west debug --dev-id='s32dbg:00:04:9f:00:ca:fe'
```

It is possible to pass extra options to the debug host tools via `--tool-opt`.
When executing `debug` or `attach` commands, the tool options will be passed
to the GDB client only. When executing `debugserver`, the tool options will be
passed to the GDB server. For example, to load a Zephyr application to SRAM and
afterwards detach the debug session:

```shell
west debug --tool-opt='--batch'
```

## probe-rs Debug Host Tools

probe-rs is an open-source embedded toolkit written in Rust. It provides
out-of-the-box support for a variety of debug probes, including CMSIS-DAP,
ST-Link, SEGGER J-Link, FTDI and built-in USB-JTAG interface on ESP32 devices.

Check [probe-rs Installation](https://probe.rs/docs/getting-started/installation/) for more setup details.

Check if your SoC is listed in [probe-rs Supported Devices](https://probe.rs/targets/).

## STM32CubeProgrammer Flash Host Tools

STMicroelectronics provides [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) (STM32CubeProg) as an official programming tool
for STM32 boards on Linux®, macOS®, and Windows® operating systems.

It provides an easy-to-use and efficient environment for reading, writing, and verifying device memory
through both the debug interface (JTAG and SWD) and the bootloader interface (UART and USB DFU, I2C, SPI, and CAN).

It offers a wide range of features to program STM32 internal memories (such as flash, RAM, and OTP)
as well as external memories.

It also allows option programming and upload, programming content verification, and programming automation
through scripting.

It is delivered in GUI (graphical user interface) and CLI (command-line interface) versions.

It is compatible with the following debug probes:

- [ST-LINK/V2-1 Onboard Debug Probe](probes.md#stlink-v21-onboard-debug-probe)
- [J-Link External Debug Probe](probes.md#jlink-external-debug-probe)
- Standalone [ST-LINK-V2](https://www.st.com/en/development-tools/st-link-v2.html), [ST-LINK-V3](https://www.st.com/en/development-tools/stlink-v3set.html), and [STLINK-V3PWR](https://www.st.com/en/development-tools/stlink-v3pwr.html) probes

### Install STM32CubeProgrammer

The easiest way to get [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) is to download it from STMicroelectronics website.
A valid email address is needed to receive the downloading link.

Alternatively, it can be installed as part of [STM32CubeCLT](https://www.st.com/en/development-tools/stm32cubeclt.html) all-in-one multi-OS command-line toolset
which also includes GDB debugger client and server.

If you have STM32CubeIDE installed on your system, then STM32CubeProg is already present.

### Basic usage

[STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) is setup as the default west runner for all active STM32 boards supported by Zephyr.
It can be used through the `west flash` command to flash Zephyr applications.

```shell
west flash --runner stm32cubeprogrammer
```

For advanced usage via the GUI or CLI, check out the [STM32CubeProgrammer User Manual](https://www.st.com/resource/en/user_manual/um2237-stm32cubeprogrammer-software-description-stmicroelectronics.pdf).

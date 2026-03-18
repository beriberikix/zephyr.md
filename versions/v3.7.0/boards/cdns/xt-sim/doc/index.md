---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/cdns/xt-sim/doc/index.html
original_path: boards/cdns/xt-sim/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Xtensa simulator

## Overview

The Xtensa processor architecture is a configurable, extensible, and
synthesizable 32-bit RISC processor core. Processor and SOC vendors can select
from various processor options and even create customized instructions in
addition to a base ISA to tailor the processor for a particular application.

For more information, see [https://ip.cadence.com/ipportfolio/tensilica-ip/xtensa-customizable](https://ip.cadence.com/ipportfolio/tensilica-ip/xtensa-customizable)

![Xtensa Xplorer (Eclipse base frontend for xt-sim)](../../../../_images/xt-sim.jpg)

Xtensa Xplorer

## Hardware

The following Xtensa cores are officially supported:

- sample\_controller

### System Clock

Xtensa cores can be configured to use either internal or external timers.
The frequency of the clock under simulation is set to 25MHz.

## System requirements

### Prerequisites

A Linux host system is required for Xtensa development work.
We recommend using a \_\_``Debian 9.x (Stretch)``\_\_ or recent \_\_``Ubuntu``\_\_
releases (with multilib support).

Only Xtensa tools version `RF-2016.4-linux` or later are officially
supported. Other versions may work but are not supported by Cadence Systems Inc.

In order to set up the Zephyr OS build system, a Linux 32-bit GCC compiler must
be installed on the building linux box. Install GCC if needed either by
downloading `Zephyr SDK` or by using your distribution package manager.

On Debian/Ubuntu systems, you can install `gcc-multilib` package as follows:

```shell
#aptitude install gcc-multilib # Or what ever package manager (apt, apt-get, ...)
```

### Set up build environment

We recommend you create a `~/.zephyrrc` file, a shell script that shall be
sourced each time before you start working on Zephyr.
You can use the following code to create that file:

```shell
$ cat > ~/.zephyrrc
if test "${CROSS}" = xcc
then
    export ARCH=xtensa
    export BOARD=xt-sim
    export ZEPHYR_TOOLCHAIN_VARIANT=xcc
    export XTENSA_TOOLS_PATH=/opt/xtensa/XtDevTools/install/tools/RG-2016.4-linux/XtensaTools
    export XTENSA_BUILDS_PATH=/opt/xtensa/XtDevTools/install/builds/RG-2016.4-linux
    #export XTENSA_BUILD_DIR= #Keep empty to use default directory
    export EMU_PLATFORM=xt-run
elif test "${CROSS}" = zephyr-xtensa
then
    export ARCH=xtensa
    export BOARD=qemu
    export ZEPHYR_TOOLCHAIN_VARIANT=zephyr
    export ZEPHYR_SDK_INSTALL_DIR=/opt/xtensa/zephyr-sdk-64-INTERNAL-11-22-2016
elif test "${CROSS}" = zephyr-x86
then
    export ARCH=x86
    export BOARD=qemu_x86
    export ZEPHYR_TOOLCHAIN_VARIANT=zephyr
    export ZEPHYR_SDK_INSTALL_DIR=/opt/xtensa/zephyr-sdk-64-INTERNAL-11-22-2016
else
    echo "Unsupported compiler '${CROSS}' defined by environment variable CROSS"
fi
```

Once the `~/.zephyrrc` file is created, you can start working. However, each
time you start a new shell you will need to execute the following commands
before you can compile anything:

```shell
$ cd path/to/zephyr # replace path/to by a real path
$ CROSS=xcc source zephyr-env.sh # Select xcc as compiler
```

### Adding a user-defined Xtensa core

Add your own core to the list of supported cores as follows:

```shell
$ XTENSA_CORE=myCore
$ $(which echo) -e "config ${XTENSA_CORE}\n\tbool \"${XTENSA_CORE} core\"\n" >> "soc/xtensa/Kconfig.cores"
```

Create a folder for that core:

```shell
$ mkdir soc/xtensa/${XTENSA_CORE}
```

Create and copy to that folder a custom linker script (more on linker script in next section):

```shell
$ cp  linker.ld  soc/xtensa/${XTENSA_CORE}/linker.ld
```

Add a Makefile:

```shell
$ echo "obj-y = soc.o" > soc/xtensa/${XTENSA_CORE}/Makefile
```

Add Zephyr specific sections to the linker script.
The file “soc/xtensa/linker\_more.ld” contains Zephyr-specific linker
sections that should be added to the default linker script linker.ld (inside
SECTIONS region). If you are not using a linker script, you must create one
and add these sections. The memory segment and PHDR should be replaced by
appropriate values.

The linker script should be named `linker.ld` and placed in the directory
`soc/xtensa/${XTENSA_CORE}`.

### Configuring build

```shell
# From the root of the zephyr repository
west build -b None samples/hello_world
west build -t menuconfig
```

Below is an example of usage for typical configuration:

1. Select `Architecture`
   :   1. Select `Xtensa architecture`
2. Select `XTENSA core Selection`
   :   1. Select appropriate core (example `hifi3_bd5 core`)
3. Select `XTENSA Options`
   :   1. Set `Hardware clock cycles per second` to appropriate value
       2. Set `The path to Xtensa tool` to appropriate value
       3. Set `The version of Xtensa tool` to appropriate version
       4. Set `Xtensa build directory` to appropriate value
4. Select `Board Selection`
   :   1. Select `Xtensa Development ISS`
5. Select `Device Drivers`
   :   1. Uncheck `Serial Drivers`
6. Select `Compile and Link Features`
   :   1. Set compiler configuration and build options correctly to project requirements
7. Hit `Exit` and confirm saving the changes.

You may need to change other options in menuconfig depending on his project
specific needs.

### Compiling and running

The Xtensa executable can be run in the simulator either with a standalone core,
or with a core connected to simulated peripherals.

Build and run as follows:

```shell
west build -b None
west build -t run
```

## References

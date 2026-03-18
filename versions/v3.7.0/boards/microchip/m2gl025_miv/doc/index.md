---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/microchip/m2gl025_miv/doc/index.html
original_path: boards/microchip/m2gl025_miv/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Microchip M2GL025 Mi-V

## Overview

The Microchip M2GL025 board is an IGLOO2 FPGA based development board.
The Mi-V RISC-V soft CPU can be deployed on the MGL025 board.
More information can be found on
[Microchip’s website](https://www.microchip.com/en-us/products/fpgas-and-plds/fpga-and-soc-design-tools/mi-v).

## Programming and debugging

### Building

Applications for the `m2gl025_miv` board configuration can be built as usual
(see [Building an Application](../../../../develop/application/index.md#build-an-application)):

```shell
west build -b m2gl025_miv
```

### Flashing

In order to upload the application to the device, you’ll need OpenOCD and GDB
with RISC-V support.
You can get them as a part of SoftConsole SDK.
Download and installation instructions can be found on
[Microchip’s SoftConsole website](https://www.microchip.com/en-us/products/fpgas-and-plds/fpga-and-soc-design-tools/soc-fpga/softconsole).

With the necessary tools installed, you can connect to the board using OpenOCD.
To establish an OpenOCD connection run:

```shell
sudo LD_LIBRARY_PATH=<softconsole_path>/openocd/bin \
<softconsole_path>/openocd/bin/openocd  --file \
<softconsole_path>/openocd/share/openocd/scripts/board/microsemi-riscv.cfg
```

Leave it running, and in a different terminal, use GDB to upload the binary to
the board. You can use the RISC-V GDB from a toolchain delivered with
SoftConsole SDK.

Here is the GDB terminal command to connect to the device
and load the binary:

```shell
<softconsole_path>/riscv-unknown-elf-gcc/bin/riscv64-unknown-elf-gdb \
-ex "target extended-remote localhost:3333" \
-ex "set mem inaccessible-by-default off" \
-ex "set arch riscv:rv32" \
-ex "set riscv use_compressed_breakpoints no" \
-ex "load" <path_to_executable>
```

### Debugging

Refer to the detailed overview of [Application Debugging](../../../../develop/debug/index.md#application-debugging).

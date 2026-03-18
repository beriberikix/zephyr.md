---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/riscv/mpfs_icicle/doc/index.html
original_path: boards/riscv/mpfs_icicle/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Microchip mpfs\_icicle

## Overview

The Microchip mpfs\_icicle board is a PolarFire SoC FPGA based development board with a Microchip MPFS250T fpga device.
The E51 RISC-V CPU can be deployed on the mpfs\_icicle board.
More information can be found on the [Microchip website](https://www.microchip.com/en-us/product/MPFS250T).

## Programming and debugging

### Building

Applications for the `mpfs_icicle` board configuration can be built as usual
(see [Building an Application](../../../../develop/application/index.md#build-an-application)):

```shell
west build -b mpfs_icicle
```

### Flashing

In order to upload the application to the device, you’ll need OpenOCD and GDB
with RISC-V support.
You can get them as a part of SoftConsole SDK.
Download and installation instructions can be found on
[Microchip’s SoftConsole website](https://www.microchip.com/en-us/products/fpgas-and-plds/fpga-and-soc-design-tools/programming-and-debug/softconsole).

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
-ex "set arch riscv:rv64" \
-ex "set riscv use_compressed_breakpoints no" \
-ex "load" <path_to_executable>
```

### Debugging

Refer to the detailed overview of [Application Debugging](../../../../develop/debug/index.md#application-debugging).

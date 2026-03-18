---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/riscv/qemu_riscv32/doc/index.html
original_path: boards/riscv/qemu_riscv32/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# RISCV32 Emulation (QEMU)

## Overview

The RISCV32 QEMU board configuration is used to emulate the RISCV32 architecture.

## Programming and Debugging

Applications for the `qemu_riscv32` board configuration can be built and run in
the usual way for emulated boards (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

While this board is emulated and you can’t “flash” it, you can use this
configuration to run basic Zephyr applications and kernel tests in the QEMU
emulated environment. For example, with the [Basic Synchronization](../../../../samples/synchronization/README.md#synchronization "Manipulate basic kernel synchronization primitives.") sample:

```shell
# From the root of the zephyr repository
west build -b qemu_riscv32 samples/synchronization
west build -t run
```

This will build an image with the synchronization sample app, boot it using
QEMU, and display the following console output:

```shell
***** BOOTING ZEPHYR OS v1.8.99 - BUILD: Jun 27 2017 13:09:26 *****
threadA: Hello World from riscv32!
threadB: Hello World from riscv32!
threadA: Hello World from riscv32!
threadB: Hello World from riscv32!
threadA: Hello World from riscv32!
threadB: Hello World from riscv32!
threadA: Hello World from riscv32!
threadB: Hello World from riscv32!
threadA: Hello World from riscv32!
threadB: Hello World from riscv32!
```

Exit QEMU by pressing `CTRL+A` `x`.

### Debugging

Refer to the detailed overview about [Application Debugging](../../../../develop/debug/index.md#application-debugging).

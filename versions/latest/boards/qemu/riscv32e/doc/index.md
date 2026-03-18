---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/qemu/riscv32e/doc/index.html
original_path: boards/qemu/riscv32e/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# RISCV32E Emulation (QEMU)

## Overview

The RISCV32E QEMU board configuration is used to emulate the RISCV32 (RV32E) architecture.

## Programming and Debugging

Applications for the `qemu_riscv32e` board configuration can be built and run in
the usual way for emulated boards (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

While this board is emulated and you can’t “flash” it, you can use this
configuration to run basic Zephyr applications and kernel tests in the QEMU
emulated environment. For example, with the [Basic Synchronization](../../../../samples/synchronization/README.md#synchronization "Manipulate basic kernel synchronization primitives.") sample:

```shell
# From the root of the zephyr repository
west build -b qemu_riscv32e samples/synchronization
west build -t run
```

This will build an image with the synchronization sample app, boot it using
QEMU, and display the following console output:

```shell
*** Booting Zephyr OS build v3.1.0-rc1-59-g0d66cc1f6645  ***
thread_a: Hello World from cpu 0 on qemu_riscv32e!
thread_b: Hello World from cpu 0 on qemu_riscv32e!
thread_a: Hello World from cpu 0 on qemu_riscv32e!
thread_b: Hello World from cpu 0 on qemu_riscv32e!
thread_a: Hello World from cpu 0 on qemu_riscv32e!
thread_b: Hello World from cpu 0 on qemu_riscv32e!
thread_a: Hello World from cpu 0 on qemu_riscv32e!
thread_b: Hello World from cpu 0 on qemu_riscv32e!
thread_a: Hello World from cpu 0 on qemu_riscv32e!
thread_b: Hello World from cpu 0 on qemu_riscv32e!
thread_a: Hello World from cpu 0 on qemu_riscv32e!
thread_b: Hello World from cpu 0 on qemu_riscv32e!
```

Exit QEMU by pressing `CTRL+A` `x`.

### Debugging

Refer to the detailed overview about [Application Debugging](../../../../develop/debug/index.md#application-debugging).

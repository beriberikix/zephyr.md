---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/renode/riscv32_virtual/doc/index.html
original_path: boards/renode/riscv32_virtual/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# RISCV32 Virtual

## Overview

The RISCV32 Virtual board is a virtual platform made with Renode as an alternative to QEMU.
Contrary to QEMU, the peripherals of this platform can be easily configured by editing the
`riscv32_virtual.repl` script and the devicetree files accordingly, this allows certain hardware
configurations that only exist in proprietary boards/SoCs to be tested in upstream CI.

## Programming and debugging

### Building

Applications for the `riscv32_virtual` board configuration can be built as usual
(see [Building an Application](../../../../develop/application/index.md#build-an-application)):

```shell
west build -b riscv32_virtual
```

### Flashing

While this board is emulated and you can’t “flash” it, you can use this
configuration to run basic Zephyr applications and kernel tests in the Renode
emulated environment. For example, with the [Basic Synchronization](../../../../samples/synchronization/README.md#synchronization "Manipulate basic kernel synchronization primitives.") sample:

```shell
# From the root of the zephyr repository
west build -b riscv32_virtual samples/synchronization
west build -t run
```

This will build an image with the synchronization sample app, boot it using
Renode, and display the following console output:

```shell
*** Booting Zephyr OS build zephyr-v3.5.0-1511-g56f73bde0fb0 ***
thread_a: Hello World from cpu 0 on riscv32_virtual!
thread_b: Hello World from cpu 0 on riscv32_virtual!
thread_a: Hello World from cpu 0 on riscv32_virtual!
thread_b: Hello World from cpu 0 on riscv32_virtual!
```

Exit Renode by pressing `CTRL+C`.

### Debugging

Refer to the detailed overview about [Application Debugging](../../../../develop/debug/index.md#application-debugging).

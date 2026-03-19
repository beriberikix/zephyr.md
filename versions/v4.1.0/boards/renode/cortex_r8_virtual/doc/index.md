---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/renode/cortex_r8_virtual/doc/index.html
original_path: boards/renode/cortex_r8_virtual/doc/index.html
---

# Cortex-R8 Virtual

Board Overview

Name:
:   `cortex_r8_virtual`

Vendor:
:   Antmicro’s open source simulation and virtual development framework

Architecture:
:   arm

SoC:
:   cortex\_r8\_virtual

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renode/cortex_r8_virtual/doc/index.rst/../..)

## Overview

The Cortex-R8 Virtual board is a virtual platform that can be emulated with Renode.
Edit the [boards/renode/cortex\_r8\_virtual/support/cortex\_r8\_virtual.repl](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renode/cortex_r8_virtual/support/cortex_r8_virtual.repl) file to adapt the platform layout to your needs.

Refer to the [Renode documentation](https://renode.readthedocs.io/en/latest/)
to learn how to obtain Renode for your host.

## Programming and debugging

### Building

Applications for the `cortex_r8_virtual` board target can be built
using the standard build flow (see [Building an Application](../../../../develop/application/index.md#build-an-application)):

```shell
west build -b cortex_r8_virtual
```

### Flashing

Your software will run in simulation and you don’t need to “flash” the board in a traditional way,
but you can use this configuration to run Zephyr applications
and kernel tests directly in Renode with the use of the `run` command.

For example, with the [Basic Synchronization](../../../../samples/synchronization/README.md#synchronization "Manipulate basic kernel synchronization primitives.") sample:

```shell
# From the root of the zephyr repository
west build -b cortex_r8_virtual samples/synchronization
west build -t run
```

This will build an image with the synchronization sample app, boot it using
Renode, and display the following console output:

```shell
*** Booting Zephyr OS build v3.6.0-5689-g2a5c606abfa7 ***
thread_a: Hello World from cpu 0 on cortex_r8_virtual!
thread_b: Hello World from cpu 0 on cortex_r8_virtual!
thread_a: Hello World from cpu 0 on cortex_r8_virtual!
thread_b: Hello World from cpu 0 on cortex_r8_virtual!
```

Exit Renode by pressing `CTRL+C`.

### Debugging

Refer to the detailed overview about [Application Debugging](../../../../develop/debug/index.md#application-debugging).

Renode can serve as a GDB server. For more information, refer to the
[Renode documentation about GDB debugging](https://renode.readthedocs.io/en/latest/debugging/gdb.html).

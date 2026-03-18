---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/qemu/xtensa/doc/index.html
original_path: boards/qemu/xtensa/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Xtensa Emulation (QEMU)

## Overview

The QEMU board configuration is used to emulate the Xtensa architecture. This board
configuration provides support for the Xtensa simulation environment.

## Programming and Debugging

Use this configuration to run basic Zephyr applications and kernel tests in the QEMU
emulated environment, for example, with the [Basic Synchronization](../../../../samples/synchronization/README.md#synchronization "Manipulate basic kernel synchronization primitives.") sample:

```shell
# From the root of the zephyr repository
west build -b qemu_xtensa samples/synchronization
west build -t run
```

This will build an image with the synchronization sample app, boot it using
QEMU, and display the following console output:

```shell
***** BOOTING ZEPHYR OS v1.8.99 - BUILD: Jun 27 2017 13:09:26 *****
threadA: Hello World from xtensa!
threadB: Hello World from xtensa!
threadA: Hello World from xtensa!
threadB: Hello World from xtensa!
threadA: Hello World from xtensa!
threadB: Hello World from xtensa!
threadA: Hello World from xtensa!
threadB: Hello World from xtensa!
threadA: Hello World from xtensa!
threadB: Hello World from xtensa!
```

Exit QEMU by pressing `CTRL+A` `x`.

### Debugging

Refer to the detailed overview about [Application Debugging](../../../../develop/debug/index.md#application-debugging).

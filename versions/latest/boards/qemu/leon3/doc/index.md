---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/qemu/leon3/doc/index.html
original_path: boards/qemu/leon3/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# LEON3 Emulation (QEMU)

## Overview

The LEON3 QEMU board configuration is used to emulate the LEON3 processor.

## Programming and Debugging

Applications for the `qemu_leon3` board configuration can be built and run in
the usual way for emulated boards (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

While this board is emulated and you can’t “flash” it, you can use this
configuration to run basic Zephyr applications and kernel tests in the QEMU
emulated environment. For example, with the [Basic Synchronization](../../../../samples/synchronization/README.md#synchronization "Manipulate basic kernel synchronization primitives.") sample:

```shell
# From the root of the zephyr repository
west build -b qemu_leon3 samples/synchronization
west build -t run
```

This will build an image with the synchronization sample app, boot it using
QEMU, and display the following console output:

```shell
*** Booting Zephyr OS build zephyr-v2.4.0-27-g7b37fdd5303b  ***
threadA: Hello World from qemu_leon3!
threadB: Hello World from qemu_leon3!
threadA: Hello World from qemu_leon3!
threadB: Hello World from qemu_leon3!
threadA: Hello World from qemu_leon3!
threadB: Hello World from qemu_leon3!
threadA: Hello World from qemu_leon3!
threadB: Hello World from qemu_leon3!
threadA: Hello World from qemu_leon3!
threadB: Hello World from qemu_leon3!
```

Exit QEMU by pressing `CTRL+A` `x`.

### Debugging

Refer to the detailed overview about [Application Debugging](../../../../develop/debug/index.md#application-debugging).

---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/subsys/llext/modules/README.html
original_path: samples/subsys/llext/modules/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Linkable loadable extensions “module” sample

## Overview

This sample demonstrates the use of the [Linkable Loadable Extensions (LLEXT)](../../../../services/llext/index.md#llext) subsystem in Zephyr. The
llext subsystem allows for the loading of relocatable ELF files at runtime;
their symbols can be accessed and functions called.

Specifically, this shows how to call a simple “hello world” function,
implemented in [samples/subsys/llext/modules/src/hello\_world\_ext.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/llext/modules/src/hello_world_ext.c).
This is achieved in two different ways, depending on the value of the Kconfig
symbol `CONFIG_HELLO_WORLD_MODE`:

- if it is `y`, the function is directly compiled and called by the Zephyr
  application. The caller code used in this case is in
  [samples/subsys/llext/modules/src/main\_builtin.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/llext/modules/src/main_builtin.c).
- if it is `m`, the function is compiled as an llext and it is included in
  the application as a binary blob. At runtime, the llext subsystem is used to
  load the extension and call the function. The caller code is in
  [samples/subsys/llext/modules/src/main\_module.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/llext/modules/src/main_module.c).

## Requirements

A board with a supported llext architecture and console. This can also be
executed in QEMU emulation on the [qemu\_xtensa](../../../../boards/qemu/xtensa/doc/index.md#qemu-xtensa) or
[qemu\_cortex\_r5](../../../../boards/qemu/cortex_r5/doc/index.md#qemu-cortex-r5) virtual boards.

## Building and running

- The following commands build and run the sample so that the files are linked
  together in the same binary:

  ```shell
  west build -b qemu_xtensa -T sample.llext.modules.builtin_build samples/subsys/llext/modules
  west build -t run
  ```
- The following commands build and run the sample so that the extension code is
  compiled separately and included in the Zephyr image as a binary blob:

  ```shell
  west build -b qemu_xtensa -T sample.llext.modules.module_build samples/subsys/llext/modules
  west build -t run
  ```

  Take a look at [samples/subsys/llext/modules/sample.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/llext/modules/sample.yaml) for the
  additional architecture-specific configurations required in this case.

To build for a different board, replace `qemu_xtensa` in the commands above
with the desired board name.

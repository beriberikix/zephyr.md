---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/hello_world/README.html
original_path: samples/hello_world/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Hello World

## Overview

A simple sample that can be used with any [supported board](../../boards/index.md#boards) and
prints “Hello World” to the console.

## Building and Running

This application can be built and executed on QEMU as follows:

```shell
west build -b qemu_x86 samples/hello_world
west build -t run
```

To build for another board, change “qemu\_x86” above to that board’s name.

### Sample Output

```shell
Hello World! x86
```

Exit QEMU by pressing `CTRL+A` `x`.

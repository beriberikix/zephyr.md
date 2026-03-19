---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/hello_world/README.html
original_path: samples/hello_world/README.html
---

# Hello World

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/hello_world/README.rst/..)

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

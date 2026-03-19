---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/cpp/hello_world/README.html
original_path: samples/cpp/hello_world/README.html
---

# Hello C++ world

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/cpp/hello_world/README.rst/..)

## Overview

A simple [C++](../../../develop/languages/cpp/index.md#language-cpp) sample that can be used with many supported board and prints
“Hello, C++ world!” to the console.

## Building and Running

This configuration can be built and executed on QEMU as follows:

```shell
west build -b qemu_riscv32 samples/cpp/hello_world
west build -t run
```

To build for another board, change “qemu\_riscv32” above to that board’s name.

### Sample Output

```shell
Hello C++, world! qemu_riscv32
```

Exit QEMU by pressing `CTRL+C`

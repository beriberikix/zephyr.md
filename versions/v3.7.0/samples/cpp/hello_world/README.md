---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/cpp/hello_world/README.html
original_path: samples/cpp/hello_world/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Hello C++ World

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

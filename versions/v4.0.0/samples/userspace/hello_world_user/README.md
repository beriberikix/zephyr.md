---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/userspace/hello_world_user/README.html
original_path: samples/userspace/hello_world_user/README.html
---

# Hello World

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/userspace/hello_world_user/README.rst/..)

## Overview

A simple Hello World example that can be used with any supported board and
prints ‘Hello World from UserSpace!’ to the console.
If unavailable or unconfigured then ‘Hello World from privileged mode.’
is printed instead.

This application can be built into modes:

- single thread
- multi threading

## Building and Running

This project outputs ‘Hello World from UserSpace!’ to the console.
It can be built and executed on QEMU as follows:

```shell
west build -b qemu_riscv32 samples/userspace/hello_world_user
west build -t run
```

### Sample Output

```shell
Hello World from UserSpace! qemu_riscv32
```

Exit QEMU by pressing `CTRL`+`A` `x`.

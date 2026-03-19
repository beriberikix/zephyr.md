---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/synchronization/README.html
original_path: samples/synchronization/README.html
---

# Basic Synchronization

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/synchronization/README.rst/..)

## Overview

A simple application that demonstrates basic sanity of the kernel.
Two threads (A and B) take turns printing a greeting message to the console,
and use sleep requests and semaphores to control the rate at which messages
are generated. This demonstrates that kernel scheduling, communication,
and timing are operating correctly.

## Building and Running

This project outputs to the console. It can be built and executed
on QEMU as follows:

```shell
west build -b qemu_x86 samples/synchronization
west build -t run
```

### Sample Output

```shell
threadA: Hello World!
threadB: Hello World!
threadA: Hello World!
threadB: Hello World!
threadA: Hello World!
threadB: Hello World!
threadA: Hello World!
threadB: Hello World!
threadA: Hello World!
threadB: Hello World!

<repeats endlessly>
```

Exit QEMU by pressing `CTRL+A` `x`.

## See also

[Thread APIs](../../doxygen/html/group__thread__apis.md)

[Semaphore APIs](../../doxygen/html/group__semaphore__apis.md)

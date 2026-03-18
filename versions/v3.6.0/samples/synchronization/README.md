---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/synchronization/README.html
original_path: samples/synchronization/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Basic Synchronization

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

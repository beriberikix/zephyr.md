---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/cpp/cpp_synchronization/README.html
original_path: samples/cpp/cpp_synchronization/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# C++ Synchronization

## Overview

The sample project illustrates usage of pure virtual class, member
functions with different types of arguments, global objects constructor
invocation.

A simple application demonstrates basic sanity of the kernel. The main thread
and a cooperative thread take turns printing a greeting message to the console,
and use timers and semaphores to control the rate at which messages are
generated. This demonstrates that kernel scheduling, communication, and
timing are operating correctly.

## Building and Running

This kernel project outputs to the console. It can be built and executed
on QEMU as follows:

```shell
west build -b qemu_x86 samples/cpp/cpp_synchronization
west build -t run
```

### Sample Output

```shell
Create semaphore 0x001042b0
Create semaphore 0x001042c4
main: Hello World!
coop_thread_entry: Hello World!
main: Hello World!
coop_thread_entry: Hello World!
main: Hello World!
coop_thread_entry: Hello World!
main: Hello World!
coop_thread_entry: Hello World!
main: Hello World!
coop_thread_entry: Hello World!
main: Hello World!
coop_thread_entry: Hello World!
main: Hello World!
coop_thread_entry: Hello World!
main: Hello World!
coop_thread_entry: Hello World!
main: Hello World!
coop_thread_entry: Hello World!
main: Hello World!

<repeats endlessly>
```

Exit QEMU by pressing `CTRL+A` `x`.

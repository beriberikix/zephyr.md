---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/userspace/syscall_perf/README.html
original_path: samples/userspace/syscall_perf/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Syscall performances

The goal of this sample application is to measure the performance loss when a
user thread has to go through a system call compared to a supervisor thread that
calls the function directly.

## Overview

This application creates a supervisor and a user thread.
Then both threads call k\_current\_get() which returns a reference to the
current thread. The user thread has to go through a system call.

Both threads are showing the number of core clock cycles and the number of
instructions executed while calling k\_current\_get().

## Sample Output

```shell
User thread:                   18012 cycles      748 instructions
Supervisor thread:         7 cycles        4 instructions
User thread:                   20136 cycles      748 instructions
Supervisor thread:         7 cycles        4 instructions
User thread:                   18014 cycles      748 instructions
Supervisor thread:         7 cycles        4 instructions
```

---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/userspace/syscall_perf/README.html
original_path: samples/userspace/syscall_perf/README.html
---

# Syscall performance

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/userspace/syscall_perf/README.rst/..)

## Syscall performances

The goal of this sample application is to measure the performance loss when a
user thread has to go through a system call compared to a supervisor thread that
calls the function directly.

### Overview

This application creates a supervisor and a user thread.
Then both threads call [`k_current_get()`](../../../doxygen/html/group__thread__apis.md#ga7ef1ed0fb9513df8096ede1e52fc76b2) which returns a reference to the
current thread. The user thread has to go through a system call.

Both threads are showing the number of core clock cycles and the number of
instructions executed while calling [`k_current_get()`](../../../doxygen/html/group__thread__apis.md#ga7ef1ed0fb9513df8096ede1e52fc76b2).

### Sample Output

```shell
User thread:                   18012 cycles      748 instructions
Supervisor thread:         7 cycles        4 instructions
User thread:                   20136 cycles      748 instructions
Supervisor thread:         7 cycles        4 instructions
User thread:                   18014 cycles      748 instructions
Supervisor thread:         7 cycles        4 instructions
```

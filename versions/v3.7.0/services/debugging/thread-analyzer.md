---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/debugging/thread-analyzer.html
original_path: services/debugging/thread-analyzer.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Thread analyzer

The thread analyzer module enables all the Zephyr options required to track
the thread information, e.g. thread stack size usage and other runtime thread
runtime statistics.

The analysis is performed on demand when the application calls
[`thread_analyzer_run()`](#c.thread_analyzer_run) or [`thread_analyzer_print()`](#c.thread_analyzer_print).

For example, to build the synchronization sample with Thread Analyser enabled,
do the following:

> ```shell
> west build -b qemu_x86 samples/synchronization/ -- -DCONFIG_QEMU_ICOUNT=n -DCONFIG_THREAD_ANALYZER=y \
> -DCONFIG_THREAD_ANALYZER_USE_PRINTK=y -DCONFIG_THREAD_ANALYZER_AUTO=y \
> -DCONFIG_THREAD_ANALYZER_AUTO_INTERVAL=5
> ```

When you run the generated application in Qemu, you will get the additional
information from Thread Analyzer:

```text
thread_a: Hello World from cpu 0 on qemu_x86!
Thread analyze:
 thread_b            : STACK: unused 740 usage 284 / 1024 (27 %); CPU: 0 %
 thread_analyzer     : STACK: unused 8 usage 504 / 512 (98 %); CPU: 0 %
 thread_a            : STACK: unused 648 usage 376 / 1024 (36 %); CPU: 98 %
 idle                : STACK: unused 204 usage 116 / 320 (36 %); CPU: 0 %
thread_b: Hello World from cpu 0 on qemu_x86!
thread_a: Hello World from cpu 0 on qemu_x86!
thread_b: Hello World from cpu 0 on qemu_x86!
thread_a: Hello World from cpu 0 on qemu_x86!
thread_b: Hello World from cpu 0 on qemu_x86!
thread_a: Hello World from cpu 0 on qemu_x86!
thread_b: Hello World from cpu 0 on qemu_x86!
thread_a: Hello World from cpu 0 on qemu_x86!
Thread analyze:
 thread_b            : STACK: unused 648 usage 376 / 1024 (36 %); CPU: 7 %
 thread_analyzer     : STACK: unused 8 usage 504 / 512 (98 %); CPU: 0 %
 thread_a            : STACK: unused 648 usage 376 / 1024 (36 %); CPU: 9 %
 idle                : STACK: unused 204 usage 116 / 320 (36 %); CPU: 82 %
thread_b: Hello World from cpu 0 on qemu_x86!
thread_a: Hello World from cpu 0 on qemu_x86!
thread_b: Hello World from cpu 0 on qemu_x86!
thread_a: Hello World from cpu 0 on qemu_x86!
thread_b: Hello World from cpu 0 on qemu_x86!
thread_a: Hello World from cpu 0 on qemu_x86!
thread_b: Hello World from cpu 0 on qemu_x86!
thread_a: Hello World from cpu 0 on qemu_x86!
Thread analyze:
 thread_b            : STACK: unused 648 usage 376 / 1024 (36 %); CPU: 7 %
 thread_analyzer     : STACK: unused 8 usage 504 / 512 (98 %); CPU: 0 %
 thread_a            : STACK: unused 648 usage 376 / 1024 (36 %); CPU: 8 %
 idle                : STACK: unused 204 usage 116 / 320 (36 %); CPU: 83 %
thread_b: Hello World from cpu 0 on qemu_x86!
thread_a: Hello World from cpu 0 on qemu_x86!
thread_b: Hello World from cpu 0 on qemu_x86!
```

## Configuration

Configure this module using the following options.

- `THREAD_ANALYZER`: enable the module.
- `THREAD_ANALYZER_USE_PRINTK`: use printk for thread statistics.
- `THREAD_ANALYZER_USE_LOG`: use the logger for thread statistics.
- `THREAD_ANALYZER_AUTO`: run the thread analyzer automatically.
  You do not need to add any code to the application when using this option.
- `THREAD_ANALYZER_AUTO_INTERVAL`: the time for which the module sleeps
  between consecutive printing of thread analysis in automatic mode.
- `THREAD_ANALYZER_AUTO_STACK_SIZE`: the stack for thread analyzer
  automatic thread.
- `THREAD_NAME`: enable this option in the kernel to print the name of the
  thread instead of its ID.
- `THREAD_RUNTIME_STATS`: enable this option to print thread runtime data such
  as utilization (This options is automatically selected by THREAD\_ANALYZER).

## API documentation

*group* Thread analyzer
:   Module for analyzing threads.

    This module implements functions and the configuration that simplifies thread analysis.

    Typedefs

    typedef void (\*thread\_analyzer\_cb)(struct [thread\_analyzer\_info](#c.thread_analyzer_info) \*info)
    :   Thread analyzer stack size callback function.

        Callback function with thread analysis information.

        Param info:
        :   Thread analysis information.

    Functions

    void thread\_analyzer\_run([thread\_analyzer\_cb](#c.thread_analyzer_cb) cb)
    :   Run the thread analyzer and provide information to the callback.

        This function analyzes the current state for all threads and calls a given callback on every thread found.

        Parameters:
        :   - **cb** – The callback function handler

    void thread\_analyzer\_print(void)
    :   Run the thread analyzer and print stack size statistics.

        This function runs the thread analyzer and prints the output in standard form.

    struct thread\_analyzer\_info
    :   *#include <thread\_analyzer.h>*

        Public Members

        const char \*name
        :   The name of the thread or stringified address of the thread handle if name is not set.

        size\_t stack\_size
        :   The total size of the stack.

        size\_t stack\_used
        :   Stack size in used.

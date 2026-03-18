---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/kernel/services/other/thread_local_storage.html
original_path: kernel/services/other/thread_local_storage.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Thread Local Storage (TLS)

Thread Local Storage (TLS) allows variables to be allocated on a per-thread
basis. These variables are stored in the thread stack which means every
thread has its own copy of these variables.

Zephyr currently requires toolchain support for TLS.

## Configuration

To enable thread local storage in Zephyr, [`CONFIG_THREAD_LOCAL_STORAGE`](../../../kconfig.md#CONFIG_THREAD_LOCAL_STORAGE "CONFIG_THREAD_LOCAL_STORAGE")
needs to be enabled. Note that this option may not be available if
the architecture or the SoC does not have the hidden option
`CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE` enabled, which means
the architecture or the SoC does not have the necessary code to support
thread local storage and/or the toolchain does not support TLS.

[`CONFIG_ERRNO_IN_TLS`](../../../kconfig.md#CONFIG_ERRNO_IN_TLS "CONFIG_ERRNO_IN_TLS") can be enabled together with
[`CONFIG_ERRNO`](../../../kconfig.md#CONFIG_ERRNO "CONFIG_ERRNO") to let the variable `errno` be a thread local
variable. This allows user threads to access the value of `errno` without
making a system call.

## Declaring and Using Thread Local Variables

The keyword `__thread` can be used to declare thread local variables.

For example, to declare a thread local variable in header files:

```c
extern __thread int i;
```

And to declare the actual variable in source files:

```c
__thread int i;
```

Keyword `static` can also be used to limit the variable within a source file:

```c
static __thread int j;
```

Using the thread local variable is the same as using other variable, for example:

```c
void testing(void) {
    i = 10;
}
```

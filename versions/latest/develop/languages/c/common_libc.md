---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/develop/languages/c/common_libc.html
original_path: develop/languages/c/common_libc.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Common C library code

Zephyr provides some C library functions that are designed to be used in
conjunction with multiple C libraries. These either provide functions not
available in multiple C libraries or are designed to replace functionality
in the C library with code better suited for use in the Zephyr environment

## Time function

This provides an implementation of the standard C function, `time()`,
relying on the Zephyr function, `clock_gettime()`. This function can
be enabled by selecting `COMMON_LIBC_TIME`.

## Dynamic Memory Management

The common dynamic memory management implementation can be enabled by
selecting the [`CONFIG_COMMON_LIBC_MALLOC`](../../../kconfig.md#CONFIG_COMMON_LIBC_MALLOC "CONFIG_COMMON_LIBC_MALLOC") in the
application configuration file.

The common C library internally uses the [kernel memory heap API](../../../kernel/memory_management/heap.md#heap-v2) to manage the memory heap used by the standard dynamic memory
management interface functions such as `malloc()` and `free()`.

The internal memory heap is normally located in the `.bss` section. When
userspace is enabled, however, it is placed in a dedicated memory partition
called `z_malloc_partition`, which can be accessed from the user mode
threads. The size of the internal memory heap is specified by the
[`CONFIG_COMMON_LIBC_MALLOC_ARENA_SIZE`](../../../kconfig.md#CONFIG_COMMON_LIBC_MALLOC_ARENA_SIZE "CONFIG_COMMON_LIBC_MALLOC_ARENA_SIZE").

The default heap size for applications using the common C library is zero
(no heap). For other C library users, if there is an MMU present, then the
default heap is 16kB. Otherwise, the heap uses all available memory.

There are also separate controls to select `calloc()`
(`COMMON_LIBC_CALLOC`) and `reallocarray()`
(`COMMON_LIBC_REALLOCARRAY`). Both of these are enabled by
default as that doesn’t impact memory usage in applications not using them.

The standard dynamic memory management interface functions implemented by
the common C library are thread safe and may be simultaneously called by
multiple threads. These functions are implemented in
`lib/libc/common/source/stdlib/malloc.c`.

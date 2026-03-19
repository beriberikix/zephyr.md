---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/develop/languages/c/common_libc.html
original_path: develop/languages/c/common_libc.html
---

# Common C library code

Zephyr provides some C library functions that are designed to be used in
conjunction with multiple C libraries. These either provide functions not
available in multiple C libraries or are designed to replace functionality
in the C library with code better suited for use in the Zephyr environment

## Time function

This provides an implementation of the standard C function, [`time()`](../../../doxygen/html/lib_2libc_2minimal_2include_2time_8h.md#a99ef1cb2c789827dd5db3886dccf9067),
relying on the Zephyr function, [`clock_gettime()`](../../../doxygen/html/include_2zephyr_2posix_2time_8h.md#a21188eaca1b3e48ac3f7715398a1fc06). This function can
be enabled by selecting `COMMON_LIBC_TIME`.

## Dynamic Memory Management

The common dynamic memory management implementation can be enabled by
selecting the [`CONFIG_COMMON_LIBC_MALLOC`](../../../kconfig.md#CONFIG_COMMON_LIBC_MALLOC "CONFIG_COMMON_LIBC_MALLOC") in the
application configuration file.

The common C library internally uses the [kernel memory heap API](../../../kernel/memory_management/heap.md#heap-v2) to manage the memory heap used by the standard dynamic memory
management interface functions such as [`malloc()`](../../../doxygen/html/stdlib_8h.md#a9c36d0fe3ec4675cbffdc9b52f5fb399) and [`free()`](../../../doxygen/html/stdlib_8h.md#afbedc913aa4651b3c3b4b3aecd9b4711).

The internal memory heap is normally located in the `.bss` section. When
userspace is enabled, however, it is placed in a dedicated memory partition
called `z_malloc_partition`, which can be accessed from the user mode
threads. The size of the internal memory heap is specified by the
[`CONFIG_COMMON_LIBC_MALLOC_ARENA_SIZE`](../../../kconfig.md#CONFIG_COMMON_LIBC_MALLOC_ARENA_SIZE "CONFIG_COMMON_LIBC_MALLOC_ARENA_SIZE").

The default heap size for applications using the common C library is zero
(no heap). For other C library users, if there is an MMU present, then the
default heap is 16kB. Otherwise, the heap uses all available memory.

There are also separate controls to select [`calloc()`](../../../doxygen/html/stdlib_8h.md#a2807e26a012717736641384f91ab2563)
(`COMMON_LIBC_CALLOC`) and [`reallocarray()`](../../../doxygen/html/stdlib_8h.md#aa34babf7c7883ba6714ac6d010952465)
(`COMMON_LIBC_REALLOCARRAY`). Both of these are enabled by
default as that doesn’t impact memory usage in applications not using them.

The standard dynamic memory management interface functions implemented by
the common C library are thread safe and may be simultaneously called by
multiple threads. These functions are implemented in
`lib/libc/common/source/stdlib/malloc.c`.

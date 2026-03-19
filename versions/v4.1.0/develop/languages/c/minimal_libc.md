---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/develop/languages/c/minimal_libc.html
original_path: develop/languages/c/minimal_libc.html
---

# Minimal libc

The most basic C library, named “minimal libc”, is part of the Zephyr codebase
and provides the minimal subset of the standard C library required to meet the
needs of Zephyr and its subsystems, primarily in the areas of string
manipulation and display.

It is very low footprint and is suitable for projects that do not rely on less
frequently used portions of the ISO C standard library. It can also be used
with a number of different toolchains.

The minimal libc implementation can be found in `lib/libc/minimal` in the
main Zephyr tree.

## Functions

The minimal libc implements the minimal subset of the ISO/IEC 9899:2011
standard C library functions required to meet the needs of the Zephyr kernel,
as defined by the [Coding Guidelines Rule A.4](../../../contribute/coding_guidelines/index.md#coding-guideline-libc-usage-restrictions-in-zephyr-kernel).

## Formatted Output

The minimal libc does not implement its own formatted output processor;
instead, it maps the C standard formatted output functions such as `printf`
and `sprintf` to the [`cbprintf()`](../../../doxygen/html/group__cbprintf__apis.md#ga0cebdbf4f142ee28c5bd80a1615647da) function, which is Zephyr’s own
C99-compatible formatted output implementation.

For more details, refer to the [Formatted Output](../../../services/formatted_output.md#formatted-output) OS
service documentation.

## Dynamic Memory Management

The minimal libc uses the malloc api family implementation provided by the
[common C library](common_libc.md#c-library-common), which itself is built upon the
[kernel memory heap API](../../../kernel/memory_management/heap.md#heap-v2).

## Error numbers

Error numbers are used throughout Zephyr APIs to signal error conditions as
return values from functions. They are typically returned as the negative value
of the integer literals defined in this section, and are defined in the
`errno.h` header file.

A subset of the error numbers defined in the [POSIX errno.h specification](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/errno.h.html) and
other de-facto standard sources have been added to the minimal libc.

A conscious effort is made in Zephyr to keep the values of the minimal libc
error numbers consistent with the different implementations of the C standard
libraries supported by Zephyr. The minimal libc `errno.h` is checked
against that of the [Newlib](newlib.md#c-library-newlib) to ensure that the error
numbers are kept aligned.

Below is a list of the error number definitions. For the actual numeric values
please refer to [errno.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/libc/minimal/include/errno.h).

[Error numbers](../../../doxygen/html/group__system__errno.md)

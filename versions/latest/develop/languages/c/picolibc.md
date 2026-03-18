---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/develop/languages/c/picolibc.html
original_path: develop/languages/c/picolibc.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Picolibc

[Picolibc](https://github.com/picolibc/picolibc) is a complete C library implementation written for the
embedded systems, targeting [C17 (ISO/IEC 9899:2018)](https://www.iso.org/standard/74528.html) and [POSIX 2018
(IEEE Std 1003.1-2017)](https://pubs.opengroup.org/onlinepubs/9699919799/functions/printf.html) standards. Picolibc is an external open
source project which is provided for Zephyr as a module, and included
as part of the [Zephyr SDK](../../toolchains/zephyr_sdk.md#toolchain-zephyr-sdk) in precompiled form for
each supported architecture (`libc.a`).

Note

Picolibc is also available for other 3rd-party toolchains, such as
[GNU Arm Embedded](../../toolchains/gnu_arm_embedded.md#toolchain-gnuarmemb).

Zephyr implements the “API hook” functions that are invoked by the C
standard library functions in the Picolibc. These hook functions are
implemented in `lib/libc/picolibc/libc-hooks.c` and translate
the library internal system calls to the equivalent Zephyr API calls.

## Picolibc Module

When built as a Zephyr module, there are several configuration knobs
available to adjust the feature set in the library, balancing what the
library supports versus the code size of the resulting
functions. Because the standard C++ library must be compiled for the
target C library, the Picolibc module cannot be used with applications
which use the standard C++ library. Building the Picolibc module will
increase the time it takes to compile the application.

The Picolibc module can be enabled by selecting
[`CONFIG_PICOLIBC_USE_MODULE`](../../../kconfig.md#CONFIG_PICOLIBC_USE_MODULE "CONFIG_PICOLIBC_USE_MODULE") in the application
configuration file.

When updating the Picolibc module to a newer version, the
[toolchain-bundled Picolibc in the Zephyr SDK](#c-library-picolibc-toolchain) must also be updated to the same version.

## Toolchain Picolibc

Starting with version 0.16, the Zephyr SDK includes precompiled
versions of Picolibc for every target architecture, along with
precompiled versions of libstdc++.

The toolchain version of Picolibc can be enabled by de-selecting
[`CONFIG_PICOLIBC_USE_MODULE`](../../../kconfig.md#CONFIG_PICOLIBC_USE_MODULE "CONFIG_PICOLIBC_USE_MODULE") in the application
configuration file.

For every release of Zephyr, the toolchain-bundled Picolibc and the
[Picolibc module](#c-library-picolibc-module) are guaranteed to be in
sync when using the
[recommended version of Zephyr SDK](../../toolchains/zephyr_sdk.md#toolchain-zephyr-sdk-compatibility).

### Building Without Toolchain bundled Picolibc

For toolchain where there is no bundled Picolibc, it is still
possible to use Picolibc by building it from source. Note that
any restrictions mentioned in [Picolibc Module](#c-library-picolibc-module)
still apply.

To build without toolchain bundled Picolibc, the toolchain must
enable [`CONFIG_PICOLIBC_SUPPORTED`](../../../kconfig.md#CONFIG_PICOLIBC_SUPPORTED "CONFIG_PICOLIBC_SUPPORTED"). For example,
this needs to be added to the toolchain Kconfig file:

```text
config TOOLCHAIN_<name>_PICOLIBC_SUPPORTED
   def_bool y
   select PICOLIBC_SUPPORTED
```

By enabling [`CONFIG_PICOLIBC_SUPPORTED`](../../../kconfig.md#CONFIG_PICOLIBC_SUPPORTED "CONFIG_PICOLIBC_SUPPORTED"), the build
system would automatically build Picolibc from source with its module
when there is no toolchain bundled Picolibc.

#### Formatted Output

Picolibc supports all standard C formatted input and output functions,
including `printf()`, `fprintf()`, `sprintf()` and
`sscanf()`.

Picolibc formatted input and output function implementation supports
all format specifiers defined by the C17 and POSIX 2018 standards with
the following exceptions:

- Floating point format specifiers (e.g. `%f`) require
  [`CONFIG_PICOLIBC_IO_FLOAT`](../../../kconfig.md#CONFIG_PICOLIBC_IO_FLOAT "CONFIG_PICOLIBC_IO_FLOAT").
- Long long format specifiers (e.g. `%lld`) require
  [`CONFIG_PICOLIBC_IO_LONG_LONG`](../../../kconfig.md#CONFIG_PICOLIBC_IO_LONG_LONG "CONFIG_PICOLIBC_IO_LONG_LONG"). This option is
  automatically enabled with [`CONFIG_PICOLIBC_IO_FLOAT`](../../../kconfig.md#CONFIG_PICOLIBC_IO_FLOAT "CONFIG_PICOLIBC_IO_FLOAT").

#### Printk, cbprintf and friends

When using Picolibc, Zephyr formatted output functions are
implemented in terms of stdio calls. This includes:

> - printk, snprintk and vsnprintk
> - cbprintf and cbvprintf
> - fprintfcb, vfprintfcb, printfcb, vprintfcb, snprintfcb and vsnprintfcb

When using tagged args
([`CONFIG_CBPRINTF_PACKAGE_SUPPORT_TAGGED_ARGUMENTS`](../../../kconfig.md#CONFIG_CBPRINTF_PACKAGE_SUPPORT_TAGGED_ARGUMENTS "CONFIG_CBPRINTF_PACKAGE_SUPPORT_TAGGED_ARGUMENTS") and
`CBPRINTF_PACKAGE_ARGS_ARE_TAGGED`), calls to cbpprintf will
not use Picolibc, so formatting of output using those code will differ
from Picolibc results as the cbprintf functions are not completely
C/POSIX compliant.

#### Math Functions

Picolibc provides full C17/[IEEE STD 754-2019](https://ieeexplore.ieee.org/document/8766229) support for float,
double and long double math operations, except for long double
versions of the Bessel functions.

#### Thread Local Storage

Picolibc uses Thread Local Storage (TLS) (where supported) for data
which is supposed to remain local to each thread, like
[`errno`](minimal_libc.md#c.errno "errno"). This means that TLS support is enabled when using
Picolibc. As all TLS variables are allocated out of the thread stack
area, this can affect stack size requirements by a few bytes.

#### C Library Local Variables

Picolibc uses a few internal variables for things like heap
management. These are collected in a dedicated memory partition called
`z_libc_partition`. Applications using
[`CONFIG_USERSPACE`](../../../kconfig.md#CONFIG_USERSPACE "CONFIG_USERSPACE") and memory domains must ensure that
this partition is included in any domain active during Picolibc calls.

#### Dynamic Memory Management

Picolibc uses the malloc api family implementation provided by the
[common C library](common_libc.md#c-library-common), which itself is built upon the
[kernel memory heap API](../../../kernel/memory_management/heap.md#heap-v2).

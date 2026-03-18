---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/develop/languages/cpp/index.html
original_path: develop/languages/cpp/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# C++ Language Support

C++ is a general-purpose object-oriented programming language that is based on
the C language.

## Enabling C++ Support

Zephyr supports applications written in both C and C++. However, to use C++ in
an application you must configure Zephyr to include C++ support by selecting
the [`CONFIG_CPP`](../../../kconfig.md#CONFIG_CPP "CONFIG_CPP") in the application configuration file.

To enable C++ support, the compiler toolchain must also include a C++ compiler
and the included compiler must be supported by the Zephyr build system. The
[Zephyr SDK](../../toolchains/zephyr_sdk.md#toolchain-zephyr-sdk), which includes the GNU C++ Compiler (part of GCC),
is supported by Zephyr, and the features and their availability documented
here assume the use of the Zephyr SDK.

The default C++ standard level (i.e. the language enforced by the
compiler flags passed) for Zephyr apps is C++11. Other standards are
available via kconfig choice, for example
[`CONFIG_STD_CPP98`](../../../kconfig.md#CONFIG_STD_CPP98 "CONFIG_STD_CPP98"). The oldest standard supported and
tested in Zephyr is C++98.

When compiling a source file, the build system selects the C++ compiler based
on the suffix (extension) of the files. Files identified with either a **cpp**
or a **cxx** suffix are compiled using the C++ compiler. For example,
`myCplusplusApp.cpp` is compiled using C++.

The C++ standard requires the `main()` function to have the return type of
`int`. Your `main()` must be defined as `int main(void)`. Zephyr ignores
the return value from main, so applications should not return status
information and should, instead, return zero.

Note

Do not use C++ for kernel, driver, or system initialization code.

## Language Features

Zephyr currently provides only a subset of C++ functionality. The following
features are *not* supported:

- Static global object destruction
- OS-specific C++ standard library classes (e.g. `std::thread`,
  `std::mutex`)

While not an exhaustive list, support for the following functionality is
included:

- Inheritance
- Virtual functions
- Virtual tables
- Static global object constructors
- Dynamic object management with the **new** and **delete** operators
- Exceptions
- RTTI
- Standard Template Library (STL)

Static global object constructors are initialized after the drivers are
initialized but before the application `main()` function. Therefore,
use of C++ is restricted to application code.

In order to make use of the C++ exceptions, the
[`CONFIG_CPP_EXCEPTIONS`](../../../kconfig.md#CONFIG_CPP_EXCEPTIONS "CONFIG_CPP_EXCEPTIONS") must be selected in the application
configuration file.

## Zephyr Minimal C++ Library

Zephyr minimal C++ library (`lib/cpp/minimal`) provides a minimal subset
of the C++ standard library and application binary interface (ABI) functions to
enable basic C++ language support. This includes:

- `new` and `delete` operators
- virtual function stub and vtables
- static global initializers for global constructors

The scope of the minimal C++ library is strictly limited to providing the basic
C++ language support, and it does not implement any [Standard Template Library
(STL)](https://en.wikipedia.org/wiki/Standard_Template_Library) classes and functions. For this reason, it is only suitable for use in
the applications that implement their own (non-standard) class library and do
not rely on the Standard Template Library (STL) components.

Any application that makes use of the Standard Template Library (STL)
components, such as `std::string` and `std::vector`, must enable the C++
standard library support.

## C++ Standard Library

The [C++ Standard Library](https://en.wikipedia.org/wiki/C%2B%2B_Standard_Library) is a collection of classes and functions that are
part of the ISO C++ standard (`std` namespace).

Zephyr does not include any C++ standard library implementation in source code
form. Instead, it allows configuring the build system to link against the
pre-built C++ standard library included in the C++ compiler toolchain.

To enable C++ standard library, select an applicable toolchain-specific C++
standard library type from the [`CONFIG_LIBCPP_IMPLEMENTATION`](../../../kconfig.md#CONFIG_LIBCPP_IMPLEMENTATION "CONFIG_LIBCPP_IMPLEMENTATION")
in the application configuration file.

For instance, when building with the [Zephyr SDK](../../toolchains/zephyr_sdk.md#toolchain-zephyr-sdk), the build
system can be configured to link against the GNU C++ Library (`libstdc++.a`),
which is a fully featured C++ standard library that provides all features
required by the ISO C++ standard including the Standard Template Library (STL),
by selecting [`CONFIG_GLIBCXX_LIBCPP`](../../../kconfig.md#CONFIG_GLIBCXX_LIBCPP "CONFIG_GLIBCXX_LIBCPP") in the application
configuration file.

The following C++ standard libraries are supported by Zephyr:

- GNU C++ Library ([`CONFIG_GLIBCXX_LIBCPP`](../../../kconfig.md#CONFIG_GLIBCXX_LIBCPP "CONFIG_GLIBCXX_LIBCPP"))
- ARC MetaWare C++ Library ([`CONFIG_ARCMWDT_LIBCPP`](../../../kconfig.md#CONFIG_ARCMWDT_LIBCPP "CONFIG_ARCMWDT_LIBCPP"))

A Zephyr subsystem that requires the features from the full C++ standard
library can select, from its config,
[`CONFIG_REQUIRES_FULL_LIBCPP`](../../../kconfig.md#CONFIG_REQUIRES_FULL_LIBCPP "CONFIG_REQUIRES_FULL_LIBCPP"), which automatically selects a
compatible C++ standard library unless the Kconfig symbol for a specific C++
standard library is selected.

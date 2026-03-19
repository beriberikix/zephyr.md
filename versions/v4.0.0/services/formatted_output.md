---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/services/formatted_output.html
original_path: services/formatted_output.html
---

# Formatted Output

Applications as well as Zephyr itself requires infrastructure to format
values for user consumption. The standard C99 library `*printf()`
functionality fulfills this need for streaming output devices or memory
buffers, but in an embedded system devices may not accept streamed data
and memory may not be available to store the formatted output.

Internal Zephyr API traditionally provided this both for
[`printk()`](../doxygen/html/printk_8h.md#a768a7dff8592b69f327a08f96b00fa54) and for Zephyr’s internal minimal libc, but with
separate internal interfaces. Logging, tracing, shell, and other
applications made use of either these APIs or standard libc routines
based on build options.

The [`cbprintf()`](../doxygen/html/group__cbprintf__apis.md#ga0cebdbf4f142ee28c5bd80a1615647da) public APIs convert C99 format strings and
arguments, providing output produced one character at a time through a
callback mechanism, replacing the original internal functions and
providing support for almost all C99 format specifications. Existing
use of `s*printf()` C libraries in Zephyr can be converted to
[`snprintfcb()`](../doxygen/html/group__cbprintf__apis.md#ga909f859afbc2a596cd0174f711a60047) to avoid pulling in libc implementations.

Several Kconfig options control the set of features that are enabled,
allowing some control over features and memory usage:

- [`CONFIG_CBPRINTF_FULL_INTEGRAL`](../kconfig.md#CONFIG_CBPRINTF_FULL_INTEGRAL "CONFIG_CBPRINTF_FULL_INTEGRAL")
  or [`CONFIG_CBPRINTF_REDUCED_INTEGRAL`](../kconfig.md#CONFIG_CBPRINTF_REDUCED_INTEGRAL "CONFIG_CBPRINTF_REDUCED_INTEGRAL")
- [`CONFIG_CBPRINTF_FP_SUPPORT`](../kconfig.md#CONFIG_CBPRINTF_FP_SUPPORT "CONFIG_CBPRINTF_FP_SUPPORT")
- [`CONFIG_CBPRINTF_FP_A_SUPPORT`](../kconfig.md#CONFIG_CBPRINTF_FP_A_SUPPORT "CONFIG_CBPRINTF_FP_A_SUPPORT")
- [`CONFIG_CBPRINTF_FP_ALWAYS_A`](../kconfig.md#CONFIG_CBPRINTF_FP_ALWAYS_A "CONFIG_CBPRINTF_FP_ALWAYS_A")
- [`CONFIG_CBPRINTF_N_SPECIFIER`](../kconfig.md#CONFIG_CBPRINTF_N_SPECIFIER "CONFIG_CBPRINTF_N_SPECIFIER")

[`CONFIG_CBPRINTF_LIBC_SUBSTS`](../kconfig.md#CONFIG_CBPRINTF_LIBC_SUBSTS "CONFIG_CBPRINTF_LIBC_SUBSTS") can be used to provide functions
that behave like standard libc functions but use the selected cbprintf
formatter rather than pulling in another formatter from libc.

In addition [`CONFIG_CBPRINTF_NANO`](../kconfig.md#CONFIG_CBPRINTF_NANO "CONFIG_CBPRINTF_NANO") can be used to revert back to
the very space-optimized but limited formatter used for [`printk()`](../doxygen/html/printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)
before this capability was added.

## Cbprintf Packaging

Typically, strings are formatted synchronously when a function from `printf`
family is called. However, there are cases when it is beneficial that formatting
is deferred. In that case, a state (format string and arguments) must be captured.
Such state forms a self-contained package which contains format string and
arguments. Additionally, package may contain copies of strings which are
part of a format string (format string or any `%s` argument). Package primary
content resembles va\_list stack frame thus standard formatting functions are
used to process a package. Since package contains data which is processed as
va\_list frame, strict alignment must be maintained. Due to required padding,
size of the package depends on alignment. When package is copied, it should be
copied to a memory block with the same alignment as origin.

Package can have following variants:

- **Self-contained** - non read-only strings appended to the package. String can be
  formatted from such package as long as there is access to read-only string
  locations. Package may contain information where read-only strings are located
  within the package. That information can be used to convert packet to fully
  self-contained package.
- **Fully self-contained** - all strings are appended to the package. String can be
  formatted from such package without any external data.
- **Transient**- only arguments are stored. Package contain information
  where pointers to non read-only strings are located within the package. Optionally,
  it may contain read-only string location information. String can be formatted
  from such package as long as non read-only strings are still valid and read-only
  strings are accessible. Alternatively, package can be converted to **self-contained**
  package or **fully self-contained** if information about read-only string
  locations is present in the package.

Package can be created using two methods:

- runtime - using [`cbprintf_package()`](../doxygen/html/group__cbprintf__apis.md#gad9c56f0a84f60cc53fa9e687069a8f1b) or [`cbvprintf_package()`](../doxygen/html/group__cbprintf__apis.md#gaa83f17925daa9747d329b6f1078ab15a). This
  method scans format string and based on detected format specifiers builds the
  package.
- static - types of arguments are detected at compile time by the preprocessor
  and package is created as simple assignments to a provided memory. This method
  is significantly faster than runtime (more than 15 times) but has following
  limitations: requires `_Generic` keyword (C11 feature) to be supported by
  the compiler and cannot distinguish between `%p` and `%s` if char pointer
  is used. It treats all (unsigned) char pointers as `%s` thus it will attempt
  to append string to a package. It can be handled correctly during conversion
  from **transient** package to **self-contained** package using
  [`CBPRINTF_PACKAGE_CONVERT_PTR_CHECK`](../doxygen/html/group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga370563f835488868020effcd48b23b90) flag. However, it requires access
  to the format string and it is not always possible thus it is recommended to
  cast char pointers used for `%p` to `void *`. There is a logging warning
  generated by [`cbprintf_package_convert()`](../doxygen/html/group__cbprintf__apis.md#ga3d7895fa3997bfd4ecf9cb3711c9bf3f) called with
  [`CBPRINTF_PACKAGE_CONVERT_PTR_CHECK`](../doxygen/html/group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga370563f835488868020effcd48b23b90) flag when char pointer is used with
  `%p`.

Several Kconfig options control behavior of the packaging:

- [`CONFIG_CBPRINTF_PACKAGE_LONGDOUBLE`](../kconfig.md#CONFIG_CBPRINTF_PACKAGE_LONGDOUBLE "CONFIG_CBPRINTF_PACKAGE_LONGDOUBLE")
- [`CONFIG_CBPRINTF_STATIC_PACKAGE_CHECK_ALIGNMENT`](../kconfig.md#CONFIG_CBPRINTF_STATIC_PACKAGE_CHECK_ALIGNMENT "CONFIG_CBPRINTF_STATIC_PACKAGE_CHECK_ALIGNMENT")

### Cbprintf package conversion

It is possible to convert package to a variant which contains more information, e.g
**transient** package can be converted to **self-contained**. Conversion to
**fully self-contained** package is possible if [`CBPRINTF_PACKAGE_ADD_RO_STR_POS`](../doxygen/html/group__CBPRINTF__PACKAGE__FLAGS.md#ga406facc18bf99afe16d453253d042dbb)
flag was used when package was created.

[`cbprintf_package_copy()`](../doxygen/html/group__cbprintf__apis.md#ga881520f4756c1a00270b3b3d12d6fc32) is used to calculate space needed for the new
package and to copy and convert a package.

### Cbprintf package format

Format of the package contains paddings which are platform specific. Package consists
of header which contains size of package (excluding appended strings) and number of
appended strings. It is followed by the arguments which contains alignment paddings
and resembles *va\_list* stack frame. It is followed by data associated with character
pointer arguments used by the string which are not appended to the string (but may
be appended later by `cbprinf_package_convert()`). Finally, package, optionally,
contains appended strings. Each string contains 1 byte header which contains index
of the location where address argument is stored. During packaging address is set
to null and before string formatting it is updated to point to the current string
location within the package. Updating address argument must happen just before string
formatting since address changes whenever package is copied.

| Header  sizeof(void \*) | 1 byte: Argument list size including header and *fmt* (in 32 bit words) |
| --- | --- |
| 1 byte: Number of strings appended to the package |
| 1 byte: Number of read-only string argument locations |
| 1 byte: Number of transient string argument locations |
| platform specific padding to sizeof(void \*) |
| Arguments | Pointer to *fmt* (or null if *fmt* is appended to the package) |
| (optional padding for platform specific alignment) |
| argument 0 |
| (optional padding for platform specific alignment) |
| argument 1 |
| … |
| String location information (optional) | Indexes of words within the package where read-only strings are located |
| Pairs of argument index and argument location index where transient strings are located |
| Appended strings (optional) | 1 byte: Index within the package to the location of associated argument |
| Null terminated string |
| … |

Warning

If [`CONFIG_MINIMAL_LIBC`](../kconfig.md#CONFIG_MINIMAL_LIBC "CONFIG_MINIMAL_LIBC") is selected in combination with
[`CONFIG_CBPRINTF_NANO`](../kconfig.md#CONFIG_CBPRINTF_NANO "CONFIG_CBPRINTF_NANO") formatting with C standard library
functions like `printf` or `snprintf` is limited. Among other
things the `%n` specifier, most format flags, precision control, and
floating point are not supported.

### Limitations and recommendations

- C11 `_Generic` support is required by the compiler to use static (fast) packaging.
- It is recommended to cast any character pointer used with `%p` format specifier to
  other pointer type (e.g. `void *`). If format string is not accessible then only
  static packaging is possible and it will append all detected strings. Character pointer
  used for `%p` will be considered as string pointer. Copying from unexpected location
  can have serious consequences (e.g., memory fault or security violation).

## API Reference

[Formatted Output APIs](../doxygen/html/group__cbprintf__apis.md)

---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/formatted_output.html
original_path: services/formatted_output.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Formatted Output

Applications as well as Zephyr itself requires infrastructure to format
values for user consumption. The standard C99 library `*printf()`
functionality fulfills this need for streaming output devices or memory
buffers, but in an embedded system devices may not accept streamed data
and memory may not be available to store the formatted output.

Internal Zephyr API traditionally provided this both for
`printk()` and for Zephyr’s internal minimal libc, but with
separate internal interfaces. Logging, tracing, shell, and other
applications made use of either these APIs or standard libc routines
based on build options.

The [`cbprintf()`](#c.cbprintf) public APIs convert C99 format strings and
arguments, providing output produced one character at a time through a
callback mechanism, replacing the original internal functions and
providing support for almost all C99 format specifications. Existing
use of `s*printf()` C libraries in Zephyr can be converted to
[`snprintfcb()`](#c.snprintfcb) to avoid pulling in libc implementations.

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
the very space-optimized but limited formatter used for `printk()`
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

- runtime - using [`cbprintf_package()`](#c.cbprintf_package) or [`cbvprintf_package()`](#c.cbvprintf_package). This
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
  `CBPRINTF_PACKAGE_CONVERT_PTR_CHECK` flag. However, it requires access
  to the format string and it is not always possible thus it is recommended to
  cast char pointers used for `%p` to `void *`. There is a logging warning
  generated by [`cbprintf_package_convert()`](#c.cbprintf_package_convert) called with
  `CBPRINTF_PACKAGE_CONVERT_PTR_CHECK` flag when char pointer is used with
  `%p`.

Several Kconfig options control behavior of the packaging:

- [`CONFIG_CBPRINTF_PACKAGE_LONGDOUBLE`](../kconfig.md#CONFIG_CBPRINTF_PACKAGE_LONGDOUBLE "CONFIG_CBPRINTF_PACKAGE_LONGDOUBLE")
- [`CONFIG_CBPRINTF_STATIC_PACKAGE_CHECK_ALIGNMENT`](../kconfig.md#CONFIG_CBPRINTF_STATIC_PACKAGE_CHECK_ALIGNMENT "CONFIG_CBPRINTF_STATIC_PACKAGE_CHECK_ALIGNMENT")

### Cbprintf package conversion

It is possible to convert package to a variant which contains more information, e.g
**transient** package can be converted to **self-contained**. Conversion to
**fully self-contained** package is possible if `CBPRINTF_PACKAGE_ADD_RO_STR_POS`
flag was used when package was created.

[`cbprintf_package_copy()`](#c.cbprintf_package_copy) is used to calculate space needed for the new
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

*group* Formatted Output APIs
:   Defines

    CBPRINTF\_PACKAGE\_ALIGNMENT
    :   Required alignment of the buffer used for packaging.

    CBPRINTF\_MUST\_RUNTIME\_PACKAGE(flags, ...)
    :   Determine if string must be packaged in run time.

        Static packaging can be applied if size of the package can be determined at compile time. In general, package size can be determined at compile time if there are no string arguments which might be copied into package body if they are considered transient.

        Note

        By default any char pointers are considered to be pointing at transient strings. This can be narrowed down to non const pointers by using CBPRINTF\_PACKAGE\_CONST\_CHAR\_RO.

        Parameters:
        :   - **...** – String with arguments.
            - **flags** – option flags. See Package flags.

        Return values:
        :   - **1** – if string must be packaged in run time.
            - **0** – string can be statically packaged.

    CBPRINTF\_STATIC\_PACKAGE(packaged, inlen, outlen, align\_offset, flags, ...)
    :   Statically package string.

        Build string package from formatted string. It assumes that formatted string is in the read only memory.

        If \_Generic is not supported then runtime packaging is performed.

        Parameters:
        :   - **packaged** – pointer to where the packaged data can be stored. Pass a null pointer to skip packaging but still calculate the total space required. The data stored here is relocatable, that is it can be moved to another contiguous block of memory. It must be aligned to the size of the longest argument. It is recommended to use CBPRINTF\_PACKAGE\_ALIGNMENT for alignment.
            - **inlen** – set to the number of bytes available at `packaged`. If `packaged` is NULL the value is ignored.
            - **outlen** – variable updated to the number of bytes required to completely store the packed information. If input buffer was too small it is set to -ENOSPC.
            - **align\_offset** – input buffer alignment offset in bytes. Where offset 0 means that buffer is aligned to CBPRINTF\_PACKAGE\_ALIGNMENT. Xtensa requires that `packaged` is aligned to CBPRINTF\_PACKAGE\_ALIGNMENT so it must be multiply of CBPRINTF\_PACKAGE\_ALIGNMENT or 0.
            - **flags** – option flags. See Package flags.
            - **...** – formatted string with arguments. Format string must be constant.

    Typedefs

    typedef int (\*cbprintf\_cb)()
    :   Signature for a cbprintf callback function.

        This function expects two parameters:

        - `c` a character to output. The output behavior should be as if this was cast to an unsigned char.
        - `ctx` a pointer to an object that provides context for the output operation.

        The declaration does not specify the parameter types. This allows a function like `fputc` to be used without requiring all context pointers to be to a `FILE` object.

        Return:
        :   the value of `c` cast to an unsigned char then back to int, or a negative error code that will be returned from [cbprintf()](#group__cbprintf__apis_1ga0cebdbf4f142ee28c5bd80a1615647da).

    typedef int (\*cbprintf\_cb\_local)(int c, void \*ctx)

    typedef int (\*cbprintf\_convert\_cb)(const void \*buf, size\_t len, void \*ctx)
    :   Signature for a cbprintf multibyte callback function.

        return Amount of copied data or negative error code.

        Param buf:
        :   data.

        Param len:
        :   data length.

        Param ctx:
        :   a pointer to an object that provides context for the operation.

    typedef int (\*cbvprintf\_external\_formatter\_func)([cbprintf\_cb](#c.cbprintf_cb) out, void \*ctx, const char \*fmt, va\_list ap)
    :   Signature for a external formatter function identical to cbvprintf.

        This function expects the following parameters:

        Param out:
        :   the function used to emit each generated character.

        Param ctx:
        :   a pointer to an object that provides context for the external formatter.

        Param fmt:
        :   a standard ISO C format string with characters and conversion specifications.

        Param ap:
        :   captured stack arguments corresponding to the conversion specifications found within `fmt`.

        Return:
        :   vprintf like return values: the number of characters printed, or a negative error value returned from external formatter.

    Functions

    int cbprintf\_package(void \*packaged, size\_t len, uint32\_t flags, const char \*format, ...)
    :   Capture state required to output formatted data later.

        Like [cbprintf()](#group__cbprintf__apis_1ga0cebdbf4f142ee28c5bd80a1615647da) but instead of processing the arguments and emitting the formatted results immediately all arguments are captured so this can be done in a different context, e.g. when the output function can block.

        In addition to the values extracted from arguments this will ensure that copies are made of the necessary portions of any string parameters that are not confirmed to be stored in read-only memory (hence assumed to be safe to refer to directly later).

        Parameters:
        :   - **packaged** – pointer to where the packaged data can be stored. Pass a null pointer to store nothing but still calculate the total space required. The data stored here is relocatable, that is it can be moved to another contiguous block of memory. However, under condition that alignment is maintained. It must be aligned to at least the size of a pointer.
            - **len** – this must be set to the number of bytes available at `packaged` if it is not null. If `packaged` is null then it indicates hypothetical buffer alignment offset in bytes compared to CBPRINTF\_PACKAGE\_ALIGNMENT alignment. Buffer alignment offset impacts returned size of the package. Xtensa requires that buffer is always aligned to CBPRINTF\_PACKAGE\_ALIGNMENT so it must be multiply of CBPRINTF\_PACKAGE\_ALIGNMENT or 0 when `packaged` is null.
            - **flags** – option flags. See Package flags.
            - **format** – a standard ISO C format string with characters and conversion specifications.
            - **...** – arguments corresponding to the conversion specifications found within `format`.

        Return values:
        :   - **nonegative** – the number of bytes successfully stored at `packaged`. This will not exceed `len`.
            - **-EINVAL** – if `format` is not acceptable
            - **-EFAULT** – if `packaged` alignment is not acceptable
            - **-ENOSPC** – if `packaged` was not null and the space required to store exceed `len`.

    int cbvprintf\_package(void \*packaged, size\_t len, uint32\_t flags, const char \*format, va\_list ap)
    :   Capture state required to output formatted data later.

        Like [cbprintf()](#group__cbprintf__apis_1ga0cebdbf4f142ee28c5bd80a1615647da) but instead of processing the arguments and emitting the formatted results immediately all arguments are captured so this can be done in a different context, e.g. when the output function can block.

        In addition to the values extracted from arguments this will ensure that copies are made of the necessary portions of any string parameters that are not confirmed to be stored in read-only memory (hence assumed to be safe to refer to directly later).

        Parameters:
        :   - **packaged** – pointer to where the packaged data can be stored. Pass a null pointer to store nothing but still calculate the total space required. The data stored here is relocatable, that is it can be moved to another contiguous block of memory. The pointer must be aligned to a multiple of the largest element in the argument list.
            - **len** – this must be set to the number of bytes available at `packaged`. Ignored if `packaged` is NULL.
            - **flags** – option flags. See Package flags.
            - **format** – a standard ISO C format string with characters and conversion specifications.
            - **ap** – captured stack arguments corresponding to the conversion specifications found within `format`.

        Return values:
        :   - **nonegative** – the number of bytes successfully stored at `packaged`. This will not exceed `len`.
            - **-EINVAL** – if `format` is not acceptable
            - **-ENOSPC** – if `packaged` was not null and the space required to store exceed `len`.

    int cbprintf\_package\_convert(void \*in\_packaged, size\_t in\_len, [cbprintf\_convert\_cb](#c.cbprintf_convert_cb) cb, void \*ctx, uint32\_t flags, uint16\_t \*strl, size\_t strl\_len)
    :   Convert a package.

        Converting may include appending strings used in the package to the package body. If input package was created with CBPRINTF\_PACKAGE\_ADD\_RO\_STR\_POS or CBPRINTF\_PACKAGE\_ADD\_RW\_STR\_POS, it contains information where strings are located within the package. This information can be used to copy strings during the conversion.

        `cb` is called with portions of the output package. At the end of the conversion `cb` is called with null buffer.

        Parameters:
        :   - **in\_packaged** – Input package.
            - **in\_len** – Input package length. If 0 package length will be retrieved from the `in_packaged`
            - **cb** – callback called with portions of the converted package. If null only length of the output package is calculated.
            - **ctx** – Context provided to the `cb`.
            - **flags** – Flags. See Package convert flags.
            - **strl** – **[inout]** if `packaged` is null, it is a pointer to the array where `strl_len` first string lengths will is stored. If `packaged` is not null, it contains lengths of first `strl_len` strings. It can be used to optimize copying so that string length is calculated only once (at length calculation phase when `packaged` is null.)
            - **strl\_len** – Number of elements in `strl` array.

        Return values:
        :   - **Positive** – output package size.
            - **-ENOSPC** – if `packaged` was not null and the space required to store exceed `len`.

    static inline int cbprintf\_package\_copy(void \*in\_packaged, size\_t in\_len, void \*packaged, size\_t len, uint32\_t flags, uint16\_t \*strl, size\_t strl\_len)
    :   Copy package with optional appending of strings.

        [cbprintf\_package\_convert](#group__cbprintf__apis_1ga3d7895fa3997bfd4ecf9cb3711c9bf3f) is used to convert and store converted package in the new location.

        Parameters:
        :   - **in\_packaged** – Input package.
            - **in\_len** – Input package length. If 0 package length will be retrieved from the `in_packaged`
            - **packaged** – **[out]** Output package. If null only length of the output package is calculated.
            - **len** – Available space in the location pointed by `packaged`. Not used when `packaged` is null.
            - **flags** – Flags. See Package convert flags.
            - **strl** – **[inout]** if `packaged` is null, it is a pointer to the array where `strl_len` first string lengths will is stored. If `packaged` is not null, it contains lengths of first `strl_len` strings. It can be used to optimize copying so that string length is calculated only once (at length calculation phase when `packaged` is null.)
            - **strl\_len** – Number of elements in `strl` array.

        Return values:
        :   - **Positive** – Output package size.
            - **-ENOSPC** – if `packaged` was not null and the space required to store exceed `len`.

    static inline int cbprintf\_fsc\_package(void \*in\_packaged, size\_t in\_len, void \*packaged, size\_t len)
    :   Convert package to fully self-contained (fsc) package.

        Package may not be self contain since strings by default are stored by address. Package may be partially self-contained when transient (not read only) strings are appended to the package. Such package can be decoded only when there is an access to read-only strings.

        Fully self-contained has (fsc) contains all strings used in the package. A package can be converted to fsc package if it was create with CBPRINTF\_PACKAGE\_ADD\_RO\_STR\_POS flag. Such package will contain necessary data to find read only strings in the package and copy them into the package body.

        Parameters:
        :   - **in\_packaged** – pointer to original package created with CBPRINTF\_PACKAGE\_ADD\_RO\_STR\_POS.
            - **in\_len** – `in_packaged` length.
            - **packaged** – pointer to location where fully self-contained version of the input package will be written. Pass a null pointer to calculate space required.
            - **len** – must be set to the number of bytes available at `packaged`. Not used if `packaged` is null.

        Return values:
        :   - **nonegative** – the number of bytes successfully stored at `packaged`. This will not exceed `len`. If `packaged` is null, calculated length.
            - **-ENOSPC** – if `packaged` was not null and the space required to store exceed `len`.
            - **-EINVAL** – if `in_packaged` is null.

    int cbpprintf\_external([cbprintf\_cb](#c.cbprintf_cb) out, [cbvprintf\_external\_formatter\_func](#c.cbvprintf_external_formatter_func) formatter, void \*ctx, void \*packaged)
    :   Generate the output for a previously captured format operation using an external formatter.

        Note

        Memory indicated by `packaged` will be modified in a non-destructive way, meaning that it could still be reused with this function again.

        Parameters:
        :   - **out** – the function used to emit each generated character.
            - **formatter** – external formatter function.
            - **ctx** – a pointer to an object that provides context for the external formatter.
            - **packaged** – the data required to generate the formatted output, as captured by [cbprintf\_package()](#group__cbprintf__apis_1gad9c56f0a84f60cc53fa9e687069a8f1b) or [cbvprintf\_package()](#group__cbprintf__apis_1gaa83f17925daa9747d329b6f1078ab15a). The alignment requirement on this data is the same as when it was initially created.

        Returns:
        :   printf like return values: the number of characters printed, or a negative error value returned from external formatter.

    int cbprintf([cbprintf\_cb](#c.cbprintf_cb) out, void \*ctx, const char \*format, ...)
    :   \*printf-like output through a callback.

        This is essentially printf() except the output is generated character-by-character using the provided `out` function. This allows formatting text of unbounded length without incurring the cost of a temporary buffer.

        All formatting specifiers of C99 are recognized, and most are supported if the functionality is enabled.

        Note

        The functionality of this function is significantly reduced when  [`CONFIG_CBPRINTF_NANO`](../kconfig.md#CONFIG_CBPRINTF_NANO "CONFIG_CBPRINTF_NANO") is selected.

        Parameters:
        :   - **out** – the function used to emit each generated character.
            - **ctx** – context provided when invoking out
            - **format** – a standard ISO C format string with characters and conversion specifications.
            - **...** – arguments corresponding to the conversion specifications found within `format`.

        Returns:
        :   the number of characters printed, or a negative error value returned from invoking `out`.

    static inline int cbvprintf([cbprintf\_cb](#c.cbprintf_cb) out, void \*ctx, const char \*format, va\_list ap)
    :   varargs-aware \*printf-like output through a callback.

        This is essentially vsprintf() except the output is generated character-by-character using the provided `out` function. This allows formatting text of unbounded length without incurring the cost of a temporary buffer.

        Note

        This function is available only when  [`CONFIG_CBPRINTF_LIBC_SUBSTS`](../kconfig.md#CONFIG_CBPRINTF_LIBC_SUBSTS "CONFIG_CBPRINTF_LIBC_SUBSTS") is selected.

        Note

        The functionality of this function is significantly reduced when  [`CONFIG_CBPRINTF_NANO`](../kconfig.md#CONFIG_CBPRINTF_NANO "CONFIG_CBPRINTF_NANO") is selected.

        Parameters:
        :   - **out** – the function used to emit each generated character.
            - **ctx** – context provided when invoking out
            - **format** – a standard ISO C format string with characters and conversion specifications.
            - **ap** – a reference to the values to be converted.

        Returns:
        :   the number of characters generated, or a negative error value returned from invoking `out`.

    static inline int cbvprintf\_tagged\_args([cbprintf\_cb](#c.cbprintf_cb) out, void \*ctx, const char \*format, va\_list ap)
    :   varargs-aware \*printf-like output through a callback with tagged arguments.

        This is essentially vsprintf() except the output is generated character-by-character using the provided `out` function. This allows formatting text of unbounded length without incurring the cost of a temporary buffer.

        Note that the argument list `ap` are tagged.

        Note

        This function is available only when  [`CONFIG_CBPRINTF_LIBC_SUBSTS`](../kconfig.md#CONFIG_CBPRINTF_LIBC_SUBSTS "CONFIG_CBPRINTF_LIBC_SUBSTS") is selected.

        Note

        The functionality of this function is significantly reduced when  [`CONFIG_CBPRINTF_NANO`](../kconfig.md#CONFIG_CBPRINTF_NANO "CONFIG_CBPRINTF_NANO") is selected.

        Parameters:
        :   - **out** – the function used to emit each generated character.
            - **ctx** – context provided when invoking out
            - **format** – a standard ISO C format string with characters and conversion specifications.
            - **ap** – a reference to the values to be converted.

        Returns:
        :   the number of characters generated, or a negative error value returned from invoking `out`.

    static inline int cbpprintf([cbprintf\_cb](#c.cbprintf_cb) out, void \*ctx, void \*packaged)
    :   Generate the output for a previously captured format operation.

        Note

        Memory indicated by `packaged` will be modified in a non-destructive way, meaning that it could still be reused with this function again.

        Parameters:
        :   - **out** – the function used to emit each generated character.
            - **ctx** – context provided when invoking out
            - **packaged** – the data required to generate the formatted output, as captured by [cbprintf\_package()](#group__cbprintf__apis_1gad9c56f0a84f60cc53fa9e687069a8f1b) or [cbvprintf\_package()](#group__cbprintf__apis_1gaa83f17925daa9747d329b6f1078ab15a). The alignment requirement on this data is the same as when it was initially created.

        Returns:
        :   the number of characters printed, or a negative error value returned from invoking `out`.

    int fprintfcb(FILE \*stream, const char \*format, ...)
    :   fprintf using Zephyrs cbprintf infrastructure.

        return The number of characters printed.

        Note

        This function is available only when  [`CONFIG_CBPRINTF_LIBC_SUBSTS`](../kconfig.md#CONFIG_CBPRINTF_LIBC_SUBSTS "CONFIG_CBPRINTF_LIBC_SUBSTS") is selected.

        Note

        The functionality of this function is significantly reduced when  [`CONFIG_CBPRINTF_NANO`](../kconfig.md#CONFIG_CBPRINTF_NANO "CONFIG_CBPRINTF_NANO") is selected.

        Parameters:
        :   - **stream** – the stream to which the output should be written.
            - **format** – a standard ISO C format string with characters and conversion specifications.
            - **...** – arguments corresponding to the conversion specifications found within `format`.

    int vfprintfcb(FILE \*stream, const char \*format, va\_list ap)
    :   vfprintf using Zephyrs cbprintf infrastructure.

        Note

        This function is available only when  [`CONFIG_CBPRINTF_LIBC_SUBSTS`](../kconfig.md#CONFIG_CBPRINTF_LIBC_SUBSTS "CONFIG_CBPRINTF_LIBC_SUBSTS") is selected.

        Note

        The functionality of this function is significantly reduced when  [`CONFIG_CBPRINTF_NANO`](../kconfig.md#CONFIG_CBPRINTF_NANO "CONFIG_CBPRINTF_NANO") is selected.

        Parameters:
        :   - **stream** – the stream to which the output should be written.
            - **format** – a standard ISO C format string with characters and conversion specifications.
            - **ap** – a reference to the values to be converted.

        Returns:
        :   The number of characters printed.

    int printfcb(const char \*format, ...)
    :   printf using Zephyrs cbprintf infrastructure.

        Note

        This function is available only when  [`CONFIG_CBPRINTF_LIBC_SUBSTS`](../kconfig.md#CONFIG_CBPRINTF_LIBC_SUBSTS "CONFIG_CBPRINTF_LIBC_SUBSTS") is selected.

        Note

        The functionality of this function is significantly reduced when  [`CONFIG_CBPRINTF_NANO`](../kconfig.md#CONFIG_CBPRINTF_NANO "CONFIG_CBPRINTF_NANO") is selected.

        Parameters:
        :   - **format** – a standard ISO C format string with characters and conversion specifications.
            - **...** – arguments corresponding to the conversion specifications found within `format`.

        Returns:
        :   The number of characters printed.

    int vprintfcb(const char \*format, va\_list ap)
    :   vprintf using Zephyrs cbprintf infrastructure.

        Note

        This function is available only when  [`CONFIG_CBPRINTF_LIBC_SUBSTS`](../kconfig.md#CONFIG_CBPRINTF_LIBC_SUBSTS "CONFIG_CBPRINTF_LIBC_SUBSTS") is selected.

        Note

        The functionality of this function is significantly reduced when  [`CONFIG_CBPRINTF_NANO`](../kconfig.md#CONFIG_CBPRINTF_NANO "CONFIG_CBPRINTF_NANO") is selected.

        Parameters:
        :   - **format** – a standard ISO C format string with characters and conversion specifications.
            - **ap** – a reference to the values to be converted.

        Returns:
        :   The number of characters printed.

    int snprintfcb(char \*str, size\_t size, const char \*format, ...)
    :   snprintf using Zephyrs cbprintf infrastructure.

        Note

        This function is available only when  [`CONFIG_CBPRINTF_LIBC_SUBSTS`](../kconfig.md#CONFIG_CBPRINTF_LIBC_SUBSTS "CONFIG_CBPRINTF_LIBC_SUBSTS") is selected.

        Note

        The functionality of this function is significantly reduced when  [`CONFIG_CBPRINTF_NANO`](../kconfig.md#CONFIG_CBPRINTF_NANO "CONFIG_CBPRINTF_NANO") is selected.

        Parameters:
        :   - **str** – where the formatted content should be written
            - **size** – maximum number of chaacters for the formatted output, including the terminating null byte.
            - **format** – a standard ISO C format string with characters and conversion specifications.
            - **...** – arguments corresponding to the conversion specifications found within `format`.

        Returns:
        :   The number of characters that would have been written to `str`, excluding the terminating null byte. This is greater than the number actually written if `size` is too small.

    int vsnprintfcb(char \*str, size\_t size, const char \*format, va\_list ap)
    :   vsnprintf using Zephyrs cbprintf infrastructure.

        Note

        This function is available only when  [`CONFIG_CBPRINTF_LIBC_SUBSTS`](../kconfig.md#CONFIG_CBPRINTF_LIBC_SUBSTS "CONFIG_CBPRINTF_LIBC_SUBSTS") is selected.

        Note

        The functionality of this function is significantly reduced when  [`CONFIG_CBPRINTF_NANO`](../kconfig.md#CONFIG_CBPRINTF_NANO "CONFIG_CBPRINTF_NANO") is selected.

        Parameters:
        :   - **str** – where the formatted content should be written
            - **size** – maximum number of chaacters for the formatted output, including the terminating null byte.
            - **format** – a standard ISO C format string with characters and conversion specifications.
            - **ap** – a reference to the values to be converted.

        Returns:
        :   The number of characters that would have been written to `str`, excluding the terminating null byte. This is greater than the number actually written if `size` is too small.

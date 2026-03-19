---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__cbprintf__apis.html
original_path: doxygen/html/group__cbprintf__apis.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Formatted Output APIs

[Utilities](group__utilities.md)

| Topics | |
| --- | --- |
|  | [Package convert flags](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md) |
|  | [Package flags](group__CBPRINTF__PACKAGE__FLAGS.md) |

| Macros | |
| --- | --- |
| #define | [CBPRINTF\_PACKAGE\_ALIGNMENT](#ga3b917fb81bb246a0910066e2708dbd78) |
|  | Required alignment of the buffer used for packaging. |
| #define | [CBPRINTF\_MUST\_RUNTIME\_PACKAGE](#ga4d0a2d35198c2feef1423a1454a98ae6)([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), ...) |
|  | Determine if string must be packaged in run time. |
| #define | [CBPRINTF\_STATIC\_PACKAGE](#ga1ac0f7d0956fc96a9d850d2fef928285)(packaged, inlen, outlen, align\_offset, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), ...) |
|  | Statically package string. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [cbprintf\_cb](#gaca8362dda031a176d96855a604395a83)) () |
|  | Signature for a cbprintf callback function. |
| typedef int(\* | [cbprintf\_cb\_local](#ga95f3321c1b62c4441ebf473cae958a39)) (int c, void \*ctx) |
| typedef int(\* | [cbprintf\_convert\_cb](#ga6e31a5fb5cd760fbb8d0ff5fd5cc3991)) (const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, void \*ctx) |
|  | Signature for a cbprintf multibyte callback function. |
| typedef int(\* | [cbvprintf\_external\_formatter\_func](#ga0decdf49ce8a1594d5c99e93648a24f7)) ([cbprintf\_cb](#gaca8362dda031a176d96855a604395a83) out, void \*ctx, const char \*fmt, va\_list ap) |
|  | Signature for a external formatter function identical to cbvprintf. |

| Functions | |
| --- | --- |
| int | [cbprintf\_package](#gad9c56f0a84f60cc53fa9e687069a8f1b) (void \*packaged, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), const char \*format,...) |
|  | Capture state required to output formatted data later. |
| int | [cbvprintf\_package](#gaa83f17925daa9747d329b6f1078ab15a) (void \*packaged, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), const char \*format, va\_list ap) |
|  | Capture state required to output formatted data later. |
| int | [cbprintf\_package\_convert](#ga3d7895fa3997bfd4ecf9cb3711c9bf3f) (void \*in\_packaged, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) in\_len, [cbprintf\_convert\_cb](#ga6e31a5fb5cd760fbb8d0ff5fd5cc3991) cb, void \*ctx, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*strl, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) strl\_len) |
|  | Convert a package. |
| static int | [cbprintf\_package\_copy](#ga881520f4756c1a00270b3b3d12d6fc32) (void \*in\_packaged, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) in\_len, void \*packaged, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*strl, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) strl\_len) |
|  | Copy package with optional appending of strings. |
| static int | [cbprintf\_fsc\_package](#ga66fcefde504d543eb9114bc2fff230d2) (void \*in\_packaged, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) in\_len, void \*packaged, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Convert package to fully self-contained (fsc) package. |
| int | [cbpprintf\_external](#gaa1a040db7e5171dd80d84cd871dfc687) ([cbprintf\_cb](#gaca8362dda031a176d96855a604395a83) out, [cbvprintf\_external\_formatter\_func](#ga0decdf49ce8a1594d5c99e93648a24f7) formatter, void \*ctx, void \*packaged) |
|  | Generate the output for a previously captured format operation using an external formatter. |
| int | [cbprintf](#ga0cebdbf4f142ee28c5bd80a1615647da) ([cbprintf\_cb](#gaca8362dda031a176d96855a604395a83) out, void \*ctx, const char \*format,...) |
|  | \*printf-like output through a callback. |
| static int | [cbvprintf](#ga8958868def2ba1675ebc8b3a70ff86f8) ([cbprintf\_cb](#gaca8362dda031a176d96855a604395a83) out, void \*ctx, const char \*format, va\_list ap) |
|  | varargs-aware \*printf-like output through a callback. |
| static int | [cbvprintf\_tagged\_args](#gae4d5066fff73bb38250f4dc82c43ebdc) ([cbprintf\_cb](#gaca8362dda031a176d96855a604395a83) out, void \*ctx, const char \*format, va\_list ap) |
|  | varargs-aware \*printf-like output through a callback with tagged arguments. |
| static int | [cbpprintf](#ga150fa7bb8dfb96db886006c9115e1dd7) ([cbprintf\_cb](#gaca8362dda031a176d96855a604395a83) out, void \*ctx, void \*packaged) |
|  | Generate the output for a previously captured format operation. |
| int | [fprintfcb](#ga2636e91fd5d78835cfaffe5b5012638b) ([FILE](stdio_8h.md#ac15bbd02a147d1595cdfb8b2979693d7) \*stream, const char \*format,...) |
|  | fprintf using Zephyrs cbprintf infrastructure. |
| int | [vfprintfcb](#ga24d7226976f3acbe579b6d6b5d530ade) ([FILE](stdio_8h.md#ac15bbd02a147d1595cdfb8b2979693d7) \*stream, const char \*format, va\_list ap) |
|  | vfprintf using Zephyrs cbprintf infrastructure. |
| int | [printfcb](#ga17aa694ea800f8188a3de3babd524c3f) (const char \*format,...) |
|  | printf using Zephyrs cbprintf infrastructure. |
| int | [vprintfcb](#gaa70a1b73fb04b88b40c1fa5fd65efd15) (const char \*format, va\_list ap) |
|  | vprintf using Zephyrs cbprintf infrastructure. |
| int | [snprintfcb](#ga909f859afbc2a596cd0174f711a60047) (char \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, const char \*format,...) |
|  | snprintf using Zephyrs cbprintf infrastructure. |
| int | [vsnprintfcb](#ga37b0f96a7b9c025659a902e8fd614b33) (char \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, const char \*format, va\_list ap) |
|  | vsnprintf using Zephyrs cbprintf infrastructure. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga4d0a2d35198c2feef1423a1454a98ae6)CBPRINTF\_MUST\_RUNTIME\_PACKAGE

| #define CBPRINTF\_MUST\_RUNTIME\_PACKAGE | ( |  | *[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[cbprintf.h](cbprintf_8h.md)>`

**Value:**

Z\_CBPRINTF\_MUST\_RUNTIME\_PACKAGE([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), \_\_VA\_ARGS\_\_)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

Determine if string must be packaged in run time.

Static packaging can be applied if size of the package can be determined at compile time. In general, package size can be determined at compile time if there are no string arguments which might be copied into package body if they are considered transient.

Note
:   By default any char pointers are considered to be pointing at transient strings. This can be narrowed down to non const pointers by using [CBPRINTF\_PACKAGE\_CONST\_CHAR\_RO](group__CBPRINTF__PACKAGE__FLAGS.md#ga6c16ab0b5d98012ffb00942e85d859b3 "CBPRINTF_PACKAGE_CONST_CHAR_RO").

Parameters
:   | ... | String with arguments. |
    | --- | --- |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | option flags. See [Package flags](group__CBPRINTF__PACKAGE__FLAGS.md "Package flags"). |

Return values
:   | 1 | if string must be packaged in run time. |
    | --- | --- |
    | 0 | string can be statically packaged. |

## [◆ ](#ga3b917fb81bb246a0910066e2708dbd78)CBPRINTF\_PACKAGE\_ALIGNMENT

| #define CBPRINTF\_PACKAGE\_ALIGNMENT |
| --- |

`#include <[cbprintf.h](cbprintf_8h.md)>`

**Value:**

Z\_POW2\_CEIL([COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(CONFIG\_CBPRINTF\_PACKAGE\_LONGDOUBLE, \

(sizeof(long double)), ([MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)(sizeof(double), sizeof(long long)))))

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:195

[MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)

#define MAX(a, b)

Obtain the maximum of two values.

**Definition** util.h:385

Required alignment of the buffer used for packaging.

## [◆ ](#ga1ac0f7d0956fc96a9d850d2fef928285)CBPRINTF\_STATIC\_PACKAGE

| #define CBPRINTF\_STATIC\_PACKAGE | ( |  | *packaged*, |
| --- | --- | --- | --- |
|  |  |  | *inlen*, |
|  |  |  | *outlen*, |
|  |  |  | *align\_offset*, |
|  |  |  | *[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)*, |
|  |  |  | ... ) |

`#include <[cbprintf.h](cbprintf_8h.md)>`

**Value:**

Z\_CBPRINTF\_STATIC\_PACKAGE(packaged, inlen, outlen, \

align\_offset, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), \_\_VA\_ARGS\_\_)

Statically package string.

Build string package from formatted string. It assumes that formatted string is in the read only memory.

If \_Generic is not supported then runtime packaging is performed.

Parameters
:   | packaged | pointer to where the packaged data can be stored. Pass a null pointer to skip packaging but still calculate the total space required. The data stored here is relocatable, that is it can be moved to another contiguous block of memory. It must be aligned to the size of the longest argument. It is recommended to use CBPRINTF\_PACKAGE\_ALIGNMENT for alignment. |
    | --- | --- |
    | inlen | set to the number of bytes available at `packaged`. If `packaged` is NULL the value is ignored. |
    | outlen | variable updated to the number of bytes required to completely store the packed information. If input buffer was too small it is set to -ENOSPC. |
    | align\_offset | input buffer alignment offset in bytes. Where offset 0 means that buffer is aligned to CBPRINTF\_PACKAGE\_ALIGNMENT. Xtensa requires that `packaged` is aligned to CBPRINTF\_PACKAGE\_ALIGNMENT so it must be multiply of CBPRINTF\_PACKAGE\_ALIGNMENT or 0. |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | option flags. See [Package flags](group__CBPRINTF__PACKAGE__FLAGS.md "Package flags"). |
    | ... | formatted string with arguments. Format string must be constant. |

## Typedef Documentation

## [◆ ](#gaca8362dda031a176d96855a604395a83)cbprintf\_cb

| typedef int(\* cbprintf\_cb) () |
| --- |

`#include <[cbprintf.h](cbprintf_8h.md)>`

Signature for a cbprintf callback function.

This function expects two parameters:

- `c` a character to output. The output behavior should be as if this was cast to an unsigned char.
- `ctx` a pointer to an object that provides context for the output operation.

The declaration does not specify the parameter types. This allows a function like `fputc` to be used without requiring all context pointers to be to a `[FILE](stdio_8h.md#ac15bbd02a147d1595cdfb8b2979693d7)` object.

Returns
:   the value of `c` cast to an unsigned char then back to int, or a negative error code that will be returned from [cbprintf()](#ga0cebdbf4f142ee28c5bd80a1615647da).

## [◆ ](#ga95f3321c1b62c4441ebf473cae958a39)cbprintf\_cb\_local

| typedef int(\* cbprintf\_cb\_local) (int c, void \*ctx) |
| --- |

`#include <[cbprintf.h](cbprintf_8h.md)>`

## [◆ ](#ga6e31a5fb5cd760fbb8d0ff5fd5cc3991)cbprintf\_convert\_cb

| typedef int(\* cbprintf\_convert\_cb) (const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, void \*ctx) |
| --- |

`#include <[cbprintf.h](cbprintf_8h.md)>`

Signature for a cbprintf multibyte callback function.

Parameters
:   | buf | data. |
    | --- | --- |
    | len | data length. |
    | ctx | a pointer to an object that provides context for the operation. |

return Amount of copied data or negative error code.

## [◆ ](#ga0decdf49ce8a1594d5c99e93648a24f7)cbvprintf\_external\_formatter\_func

| typedef int(\* cbvprintf\_external\_formatter\_func) ([cbprintf\_cb](#gaca8362dda031a176d96855a604395a83) out, void \*ctx, const char \*fmt, va\_list ap) |
| --- |

`#include <[cbprintf.h](cbprintf_8h.md)>`

Signature for a external formatter function identical to cbvprintf.

This function expects the following parameters:

Parameters
:   | out | the function used to emit each generated character. |
    | --- | --- |
    | ctx | a pointer to an object that provides context for the external formatter. |
    | fmt | a standard ISO C format string with characters and conversion specifications. |
    | ap | captured stack arguments corresponding to the conversion specifications found within `fmt`. |

Returns
:   vprintf like return values: the number of characters printed, or a negative error value returned from external formatter.

## Function Documentation

## [◆ ](#ga150fa7bb8dfb96db886006c9115e1dd7)cbpprintf()

| | int cbpprintf | ( | [cbprintf\_cb](#gaca8362dda031a176d96855a604395a83) | *out*, | | --- | --- | --- | --- | |  |  | void \* | *ctx*, | |  |  | void \* | *packaged* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[cbprintf.h](cbprintf_8h.md)>`

Generate the output for a previously captured format operation.

Parameters
:   | out | the function used to emit each generated character. |
    | --- | --- |
    | ctx | context provided when invoking out |
    | packaged | the data required to generate the formatted output, as captured by [cbprintf\_package()](#gad9c56f0a84f60cc53fa9e687069a8f1b) or [cbvprintf\_package()](#gaa83f17925daa9747d329b6f1078ab15a). The alignment requirement on this data is the same as when it was initially created. |

Note
:   Memory indicated by `packaged` will be modified in a non-destructive way, meaning that it could still be reused with this function again.

Returns
:   the number of characters printed, or a negative error value returned from invoking `out`.

## [◆ ](#gaa1a040db7e5171dd80d84cd871dfc687)cbpprintf\_external()

| int cbpprintf\_external | ( | [cbprintf\_cb](#gaca8362dda031a176d96855a604395a83) | *out*, |
| --- | --- | --- | --- |
|  |  | [cbvprintf\_external\_formatter\_func](#ga0decdf49ce8a1594d5c99e93648a24f7) | *formatter*, |
|  |  | void \* | *ctx*, |
|  |  | void \* | *packaged* ) |

`#include <[cbprintf.h](cbprintf_8h.md)>`

Generate the output for a previously captured format operation using an external formatter.

Parameters
:   | out | the function used to emit each generated character. |
    | --- | --- |
    | formatter | external formatter function. |
    | ctx | a pointer to an object that provides context for the external formatter. |
    | packaged | the data required to generate the formatted output, as captured by [cbprintf\_package()](#gad9c56f0a84f60cc53fa9e687069a8f1b) or [cbvprintf\_package()](#gaa83f17925daa9747d329b6f1078ab15a). The alignment requirement on this data is the same as when it was initially created. |

Note
:   Memory indicated by `packaged` will be modified in a non-destructive way, meaning that it could still be reused with this function again.

Returns
:   printf like return values: the number of characters printed, or a negative error value returned from external formatter.

## [◆ ](#ga0cebdbf4f142ee28c5bd80a1615647da)cbprintf()

| int cbprintf | ( | [cbprintf\_cb](#gaca8362dda031a176d96855a604395a83) | *out*, |
| --- | --- | --- | --- |
|  |  | void \* | *ctx*, |
|  |  | const char \* | *format*, |
|  |  |  | *...* ) |

`#include <[cbprintf.h](cbprintf_8h.md)>`

\*printf-like output through a callback.

This is essentially [printf()](stdio_8h.md#a6c67912b5a18e7d7ac03ca4e77425715) except the output is generated character-by-character using the provided `out` function. This allows formatting text of unbounded length without incurring the cost of a temporary buffer.

All formatting specifiers of C99 are recognized, and most are supported if the functionality is enabled.

Note
:   The functionality of this function is significantly reduced when

    ```
    CONFIG_CBPRINTF_NANO
    ```

    is selected.

Parameters
:   | out | the function used to emit each generated character. |
    | --- | --- |
    | ctx | context provided when invoking out |
    | format | a standard ISO C format string with characters and conversion specifications. |
    | ... | arguments corresponding to the conversion specifications found within `format`. |

Returns
:   the number of characters printed, or a negative error value returned from invoking `out`.

## [◆ ](#ga66fcefde504d543eb9114bc2fff230d2)cbprintf\_fsc\_package()

| | int cbprintf\_fsc\_package | ( | void \* | *in\_packaged*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *in\_len*, | |  |  | void \* | *packaged*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[cbprintf.h](cbprintf_8h.md)>`

Convert package to fully self-contained (fsc) package.

Package may not be self contain since strings by default are stored by address. Package may be partially self-contained when transient (not read only) strings are appended to the package. Such package can be decoded only when there is an access to read-only strings.

Fully self-contained has (fsc) contains all strings used in the package. A package can be converted to fsc package if it was create with [CBPRINTF\_PACKAGE\_ADD\_RO\_STR\_POS](group__CBPRINTF__PACKAGE__FLAGS.md#ga406facc18bf99afe16d453253d042dbb "CBPRINTF_PACKAGE_ADD_RO_STR_POS") flag. Such package will contain necessary data to find read only strings in the package and copy them into the package body.

Parameters
:   | in\_packaged | pointer to original package created with [CBPRINTF\_PACKAGE\_ADD\_RO\_STR\_POS](group__CBPRINTF__PACKAGE__FLAGS.md#ga406facc18bf99afe16d453253d042dbb "CBPRINTF_PACKAGE_ADD_RO_STR_POS"). |
    | --- | --- |
    | in\_len | `in_packaged` length. |
    | packaged | pointer to location where fully self-contained version of the input package will be written. Pass a null pointer to calculate space required. |
    | len | must be set to the number of bytes available at `packaged`. Not used if `packaged` is null. |

Return values
:   | nonegative | the number of bytes successfully stored at `packaged`. This will not exceed `len`. If `packaged` is null, calculated length. |
    | --- | --- |
    | -ENOSPC | if `packaged` was not null and the space required to store exceed `len`. |
    | -EINVAL | if `in_packaged` is null. |

## [◆ ](#gad9c56f0a84f60cc53fa9e687069a8f1b)cbprintf\_package()

| int cbprintf\_package | ( | void \* | *packaged*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags*, |
|  |  | const char \* | *format*, |
|  |  |  | *...* ) |

`#include <[cbprintf.h](cbprintf_8h.md)>`

Capture state required to output formatted data later.

Like [cbprintf()](#ga0cebdbf4f142ee28c5bd80a1615647da) but instead of processing the arguments and emitting the formatted results immediately all arguments are captured so this can be done in a different context, e.g. when the output function can block.

In addition to the values extracted from arguments this will ensure that copies are made of the necessary portions of any string parameters that are not confirmed to be stored in read-only memory (hence assumed to be safe to refer to directly later).

Parameters
:   | packaged | pointer to where the packaged data can be stored. Pass a null pointer to store nothing but still calculate the total space required. The data stored here is relocatable, that is it can be moved to another contiguous block of memory. However, under condition that alignment is maintained. It must be aligned to at least the size of a pointer. |
    | --- | --- |
    | len | this must be set to the number of bytes available at `packaged` if it is not null. If `packaged` is null then it indicates hypothetical buffer alignment offset in bytes compared to CBPRINTF\_PACKAGE\_ALIGNMENT alignment. Buffer alignment offset impacts returned size of the package. Xtensa requires that buffer is always aligned to CBPRINTF\_PACKAGE\_ALIGNMENT so it must be multiply of CBPRINTF\_PACKAGE\_ALIGNMENT or 0 when `packaged` is null. |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | option flags. See [Package flags](group__CBPRINTF__PACKAGE__FLAGS.md "Package flags"). |
    | format | a standard ISO C format string with characters and conversion specifications. |
    | ... | arguments corresponding to the conversion specifications found within `format`. |

Return values
:   | nonegative | the number of bytes successfully stored at `packaged`. This will not exceed `len`. |
    | --- | --- |
    | -EINVAL | if `format` is not acceptable |
    | -EFAULT | if `packaged` alignment is not acceptable |
    | -ENOSPC | if `packaged` was not null and the space required to store exceed `len`. |

## [◆ ](#ga3d7895fa3997bfd4ecf9cb3711c9bf3f)cbprintf\_package\_convert()

| int cbprintf\_package\_convert | ( | void \* | *in\_packaged*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *in\_len*, |
|  |  | [cbprintf\_convert\_cb](#ga6e31a5fb5cd760fbb8d0ff5fd5cc3991) | *cb*, |
|  |  | void \* | *ctx*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *strl*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *strl\_len* ) |

`#include <[cbprintf.h](cbprintf_8h.md)>`

Convert a package.

Converting may include appending strings used in the package to the package body. If input package was created with [CBPRINTF\_PACKAGE\_ADD\_RO\_STR\_POS](group__CBPRINTF__PACKAGE__FLAGS.md#ga406facc18bf99afe16d453253d042dbb "CBPRINTF_PACKAGE_ADD_RO_STR_POS") or [CBPRINTF\_PACKAGE\_ADD\_RW\_STR\_POS](group__CBPRINTF__PACKAGE__FLAGS.md#gac6ac59dda3a1a8a4572c1012b4adcbaa "CBPRINTF_PACKAGE_ADD_RW_STR_POS"), it contains information where strings are located within the package. This information can be used to copy strings during the conversion.

`cb` is called with portions of the output package. At the end of the conversion `cb` is called with null buffer.

Parameters
:   |  | in\_packaged | Input package. |
    | --- | --- | --- |
    |  | in\_len | Input package length. If 0 package length will be retrieved from the `in_packaged` |
    |  | cb | callback called with portions of the converted package. If null only length of the output package is calculated. |
    |  | ctx | Context provided to the `cb`. |
    |  | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Flags. See [Package convert flags](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md "Package convert flags"). |
    | [in,out] | strl | if `packaged` is null, it is a pointer to the array where `strl_len` first string lengths will is stored. If `packaged` is not null, it contains lengths of first `strl_len` strings. It can be used to optimize copying so that string length is calculated only once (at length calculation phase when `packaged` is null.) |
    |  | strl\_len | Number of elements in `strl` array. |

Return values
:   | Positive | output package size. |
    | --- | --- |
    | -ENOSPC | if `packaged` was not null and the space required to store exceed `len`. |

## [◆ ](#ga881520f4756c1a00270b3b3d12d6fc32)cbprintf\_package\_copy()

| | int cbprintf\_package\_copy | ( | void \* | *in\_packaged*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *in\_len*, | |  |  | void \* | *packaged*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *strl*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *strl\_len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[cbprintf.h](cbprintf_8h.md)>`

Copy package with optional appending of strings.

[cbprintf\_package\_convert](#ga3d7895fa3997bfd4ecf9cb3711c9bf3f) is used to convert and store converted package in the new location.

Parameters
:   |  | in\_packaged | Input package. |
    | --- | --- | --- |
    |  | in\_len | Input package length. If 0 package length will be retrieved from the `in_packaged` |
    | [out] | packaged | Output package. If null only length of the output package is calculated. |
    |  | len | Available space in the location pointed by `packaged`. Not used when `packaged` is null. |
    |  | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Flags. See [Package convert flags](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md "Package convert flags"). |
    | [in,out] | strl | if `packaged` is null, it is a pointer to the array where `strl_len` first string lengths will is stored. If `packaged` is not null, it contains lengths of first `strl_len` strings. It can be used to optimize copying so that string length is calculated only once (at length calculation phase when `packaged` is null.) |
    |  | strl\_len | Number of elements in `strl` array. |

Return values
:   | Positive | Output package size. |
    | --- | --- |
    | -ENOSPC | if `packaged` was not null and the space required to store exceed `len`. |

## [◆ ](#ga8958868def2ba1675ebc8b3a70ff86f8)cbvprintf()

| | int cbvprintf | ( | [cbprintf\_cb](#gaca8362dda031a176d96855a604395a83) | *out*, | | --- | --- | --- | --- | |  |  | void \* | *ctx*, | |  |  | const char \* | *format*, | |  |  | va\_list | *ap* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[cbprintf.h](cbprintf_8h.md)>`

varargs-aware \*printf-like output through a callback.

This is essentially [vsprintf()](stdio_8h.md#a0cf1b75a23729bcc1669ce788d01aa63) except the output is generated character-by-character using the provided `out` function. This allows formatting text of unbounded length without incurring the cost of a temporary buffer.

Note
:   This function is available only when

    ```
    CONFIG_CBPRINTF_LIBC_SUBSTS
    ```

    is selected.
:   The functionality of this function is significantly reduced when

    ```
    CONFIG_CBPRINTF_NANO
    ```

    is selected.

Parameters
:   | out | the function used to emit each generated character. |
    | --- | --- |
    | ctx | context provided when invoking out |
    | format | a standard ISO C format string with characters and conversion specifications. |
    | ap | a reference to the values to be converted. |

Returns
:   the number of characters generated, or a negative error value returned from invoking `out`.

## [◆ ](#gaa83f17925daa9747d329b6f1078ab15a)cbvprintf\_package()

| int cbvprintf\_package | ( | void \* | *packaged*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags*, |
|  |  | const char \* | *format*, |
|  |  | va\_list | *ap* ) |

`#include <[cbprintf.h](cbprintf_8h.md)>`

Capture state required to output formatted data later.

Like [cbprintf()](#ga0cebdbf4f142ee28c5bd80a1615647da) but instead of processing the arguments and emitting the formatted results immediately all arguments are captured so this can be done in a different context, e.g. when the output function can block.

In addition to the values extracted from arguments this will ensure that copies are made of the necessary portions of any string parameters that are not confirmed to be stored in read-only memory (hence assumed to be safe to refer to directly later).

Parameters
:   | packaged | pointer to where the packaged data can be stored. Pass a null pointer to store nothing but still calculate the total space required. The data stored here is relocatable, that is it can be moved to another contiguous block of memory. The pointer must be aligned to a multiple of the largest element in the argument list. |
    | --- | --- |
    | len | this must be set to the number of bytes available at `packaged`. Ignored if `packaged` is NULL. |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | option flags. See [Package flags](group__CBPRINTF__PACKAGE__FLAGS.md "Package flags"). |
    | format | a standard ISO C format string with characters and conversion specifications. |
    | ap | captured stack arguments corresponding to the conversion specifications found within `format`. |

Return values
:   | nonegative | the number of bytes successfully stored at `packaged`. This will not exceed `len`. |
    | --- | --- |
    | -EINVAL | if `format` is not acceptable |
    | -ENOSPC | if `packaged` was not null and the space required to store exceed `len`. |

## [◆ ](#gae4d5066fff73bb38250f4dc82c43ebdc)cbvprintf\_tagged\_args()

| | int cbvprintf\_tagged\_args | ( | [cbprintf\_cb](#gaca8362dda031a176d96855a604395a83) | *out*, | | --- | --- | --- | --- | |  |  | void \* | *ctx*, | |  |  | const char \* | *format*, | |  |  | va\_list | *ap* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[cbprintf.h](cbprintf_8h.md)>`

varargs-aware \*printf-like output through a callback with tagged arguments.

This is essentially [vsprintf()](stdio_8h.md#a0cf1b75a23729bcc1669ce788d01aa63) except the output is generated character-by-character using the provided `out` function. This allows formatting text of unbounded length without incurring the cost of a temporary buffer.

Note that the argument list `ap` are tagged.

Note
:   This function is available only when

    ```
    CONFIG_CBPRINTF_LIBC_SUBSTS
    ```

    is selected.
:   The functionality of this function is significantly reduced when

    ```
    CONFIG_CBPRINTF_NANO
    ```

    is selected.

Parameters
:   | out | the function used to emit each generated character. |
    | --- | --- |
    | ctx | context provided when invoking out |
    | format | a standard ISO C format string with characters and conversion specifications. |
    | ap | a reference to the values to be converted. |

Returns
:   the number of characters generated, or a negative error value returned from invoking `out`.

## [◆ ](#ga2636e91fd5d78835cfaffe5b5012638b)fprintfcb()

| int fprintfcb | ( | [FILE](stdio_8h.md#ac15bbd02a147d1595cdfb8b2979693d7) \* | *stream*, |
| --- | --- | --- | --- |
|  |  | const char \* | *format*, |
|  |  |  | *...* ) |

`#include <[cbprintf.h](cbprintf_8h.md)>`

fprintf using Zephyrs cbprintf infrastructure.

Note
:   This function is available only when

    ```
    CONFIG_CBPRINTF_LIBC_SUBSTS
    ```

    is selected.
:   The functionality of this function is significantly reduced when

    ```
    CONFIG_CBPRINTF_NANO
    ```

    is selected.

Parameters
:   | stream | the stream to which the output should be written. |
    | --- | --- |
    | format | a standard ISO C format string with characters and conversion specifications. |
    | ... | arguments corresponding to the conversion specifications found within `format`. |

return The number of characters printed.

## [◆ ](#ga17aa694ea800f8188a3de3babd524c3f)printfcb()

| int printfcb | ( | const char \* | *format*, |
| --- | --- | --- | --- |
|  |  |  | *...* ) |

`#include <[cbprintf.h](cbprintf_8h.md)>`

printf using Zephyrs cbprintf infrastructure.

Note
:   This function is available only when

    ```
    CONFIG_CBPRINTF_LIBC_SUBSTS
    ```

    is selected.
:   The functionality of this function is significantly reduced when

    ```
    CONFIG_CBPRINTF_NANO
    ```

    is selected.

Parameters
:   | format | a standard ISO C format string with characters and conversion specifications. |
    | --- | --- |
    | ... | arguments corresponding to the conversion specifications found within `format`. |

Returns
:   The number of characters printed.

## [◆ ](#ga909f859afbc2a596cd0174f711a60047)snprintfcb()

| int snprintfcb | ( | char \* | *str*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | const char \* | *format*, |
|  |  |  | *...* ) |

`#include <[cbprintf.h](cbprintf_8h.md)>`

snprintf using Zephyrs cbprintf infrastructure.

Note
:   This function is available only when

    ```
    CONFIG_CBPRINTF_LIBC_SUBSTS
    ```

    is selected.
:   The functionality of this function is significantly reduced when

    ```
    CONFIG_CBPRINTF_NANO
    ```

    is selected.

Parameters
:   | str | where the formatted content should be written |
    | --- | --- |
    | size | maximum number of chaacters for the formatted output, including the terminating null byte. |
    | format | a standard ISO C format string with characters and conversion specifications. |
    | ... | arguments corresponding to the conversion specifications found within `format`. |

Returns
:   The number of characters that would have been written to `str`, excluding the terminating null byte. This is greater than the number actually written if `size` is too small.

## [◆ ](#ga24d7226976f3acbe579b6d6b5d530ade)vfprintfcb()

| int vfprintfcb | ( | [FILE](stdio_8h.md#ac15bbd02a147d1595cdfb8b2979693d7) \* | *stream*, |
| --- | --- | --- | --- |
|  |  | const char \* | *format*, |
|  |  | va\_list | *ap* ) |

`#include <[cbprintf.h](cbprintf_8h.md)>`

vfprintf using Zephyrs cbprintf infrastructure.

Note
:   This function is available only when

    ```
    CONFIG_CBPRINTF_LIBC_SUBSTS
    ```

    is selected.
:   The functionality of this function is significantly reduced when

    ```
    CONFIG_CBPRINTF_NANO
    ```

    is selected.

Parameters
:   | stream | the stream to which the output should be written. |
    | --- | --- |
    | format | a standard ISO C format string with characters and conversion specifications. |
    | ap | a reference to the values to be converted. |

Returns
:   The number of characters printed.

## [◆ ](#gaa70a1b73fb04b88b40c1fa5fd65efd15)vprintfcb()

| int vprintfcb | ( | const char \* | *format*, |
| --- | --- | --- | --- |
|  |  | va\_list | *ap* ) |

`#include <[cbprintf.h](cbprintf_8h.md)>`

vprintf using Zephyrs cbprintf infrastructure.

Note
:   This function is available only when

    ```
    CONFIG_CBPRINTF_LIBC_SUBSTS
    ```

    is selected.
:   The functionality of this function is significantly reduced when

    ```
    CONFIG_CBPRINTF_NANO
    ```

    is selected.

Parameters
:   | format | a standard ISO C format string with characters and conversion specifications. |
    | --- | --- |
    | ap | a reference to the values to be converted. |

Returns
:   The number of characters printed.

## [◆ ](#ga37b0f96a7b9c025659a902e8fd614b33)vsnprintfcb()

| int vsnprintfcb | ( | char \* | *str*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | const char \* | *format*, |
|  |  | va\_list | *ap* ) |

`#include <[cbprintf.h](cbprintf_8h.md)>`

vsnprintf using Zephyrs cbprintf infrastructure.

Note
:   This function is available only when

    ```
    CONFIG_CBPRINTF_LIBC_SUBSTS
    ```

    is selected.
:   The functionality of this function is significantly reduced when

    ```
    CONFIG_CBPRINTF_NANO
    ```

    is selected.

Parameters
:   | str | where the formatted content should be written |
    | --- | --- |
    | size | maximum number of chaacters for the formatted output, including the terminating null byte. |
    | format | a standard ISO C format string with characters and conversion specifications. |
    | ap | a reference to the values to be converted. |

Returns
:   The number of characters that would have been written to `str`, excluding the terminating null byte. This is greater than the number actually written if `size` is too small.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

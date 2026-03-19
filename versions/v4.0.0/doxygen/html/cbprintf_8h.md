---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/cbprintf_8h.html
original_path: doxygen/html/cbprintf_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cbprintf.h File Reference

`#include <stdarg.h>`  
`#include <stddef.h>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[string.h](string_8h_source.md)>`  
`#include <[stdio.h](stdio_8h_source.md)>`  
`#include <[zephyr/sys/cbprintf_internal.h](cbprintf__internal_8h_source.md)>`  
`#include <[zephyr/sys/cbprintf_enums.h](cbprintf__enums_8h_source.md)>`

[Go to the source code of this file.](cbprintf_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [cbprintf\_package\_desc](structcbprintf__package__desc.md) |
|  | cbprintf package descriptor. [More...](structcbprintf__package__desc.md#details) |
| union | [cbprintf\_package\_hdr](unioncbprintf__package__hdr.md) |
|  | cbprintf package header [More...](unioncbprintf__package__hdr.md#details) |
| struct | [cbprintf\_package\_hdr\_ext](structcbprintf__package__hdr__ext.md) |
|  | cbprintf package header with format string pointer. [More...](structcbprintf__package__hdr__ext.md#details) |

| Macros | |
| --- | --- |
| #define | [CBPRINTF\_PACKAGE\_ALIGNMENT](group__cbprintf__apis.md#ga3b917fb81bb246a0910066e2708dbd78) |
|  | Required alignment of the buffer used for packaging. |
| #define | [CBPRINTF\_PACKAGE\_CONST\_CHAR\_RO](group__CBPRINTF__PACKAGE__FLAGS.md#ga6c16ab0b5d98012ffb00942e85d859b3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Assume that const char pointer is pointing to read only (constant) strings. |
| #define | [CBPRINTF\_PACKAGE\_ADD\_RO\_STR\_POS](group__CBPRINTF__PACKAGE__FLAGS.md#ga406facc18bf99afe16d453253d042dbb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Append locations (within the package) of read-only string pointers. |
| #define | [CBPRINTF\_PACKAGE\_ADD\_RW\_STR\_POS](group__CBPRINTF__PACKAGE__FLAGS.md#gac6ac59dda3a1a8a4572c1012b4adcbaa)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Append locations (within the package) of read-write string pointers. |
| #define | [CBPRINTF\_PACKAGE\_FIRST\_RO\_STR\_CNT](group__CBPRINTF__PACKAGE__FLAGS.md#ga26b5e05198f6609049c54e439b78cf3c)(n) |
|  | Indicate that `n` first string format arguments are char pointers to read-only location. |
| #define | [CBPRINTF\_PACKAGE\_ADD\_STRING\_IDXS](group__CBPRINTF__PACKAGE__FLAGS.md#ga95b0b7f91303781b8bad610f7cac3fa3)   ([CBPRINTF\_PACKAGE\_ADD\_RO\_STR\_POS](group__CBPRINTF__PACKAGE__FLAGS.md#ga406facc18bf99afe16d453253d042dbb) | [CBPRINTF\_PACKAGE\_CONST\_CHAR\_RO](group__CBPRINTF__PACKAGE__FLAGS.md#ga6c16ab0b5d98012ffb00942e85d859b3)) |
|  | Append indexes of read-only string arguments in the package. |
| #define | [CBPRINTF\_PACKAGE\_ARGS\_ARE\_TAGGED](group__CBPRINTF__PACKAGE__FLAGS.md#gaa8edaf31e7acfb7cb113afa873efa126)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Indicate the incoming arguments are tagged. |
| #define | [CBPRINTF\_PACKAGE\_CONVERT\_RO\_STR](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga9802b700abd5d3cd7cef0e0cbcceb3e7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Append read-only strings from source package to destination package. |
| #define | [CBPRINTF\_PACKAGE\_CONVERT\_RW\_STR](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga983c65ed8afb356a29fa2736f9de7b39)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Append read-write strings from source package to destination package. |
| #define | [CBPRINTF\_PACKAGE\_CONVERT\_KEEP\_RO\_STR](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga582ebea3e0d18285840bf277c5382da6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Keep read-only location indexes in the package. |
| #define | [CBPRINTF\_PACKAGE\_CONVERT\_PTR\_CHECK](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga370563f835488868020effcd48b23b90)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Check format string if p argument was treated as s in the package. |
| #define | [CBPRINTF\_MUST\_RUNTIME\_PACKAGE](group__cbprintf__apis.md#ga4d0a2d35198c2feef1423a1454a98ae6)([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), ...) |
|  | Determine if string must be packaged in run time. |
| #define | [CBPRINTF\_STATIC\_PACKAGE](group__cbprintf__apis.md#ga1ac0f7d0956fc96a9d850d2fef928285)(packaged, inlen, outlen, align\_offset, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), ...) |
|  | Statically package string. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [cbprintf\_cb](group__cbprintf__apis.md#gaca8362dda031a176d96855a604395a83)) () |
|  | Signature for a cbprintf callback function. |
| typedef int(\* | [cbprintf\_cb\_local](group__cbprintf__apis.md#ga95f3321c1b62c4441ebf473cae958a39)) (int c, void \*ctx) |
| typedef int(\* | [cbprintf\_convert\_cb](group__cbprintf__apis.md#ga6e31a5fb5cd760fbb8d0ff5fd5cc3991)) (const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, void \*ctx) |
|  | Signature for a cbprintf multibyte callback function. |
| typedef int(\* | [cbvprintf\_external\_formatter\_func](group__cbprintf__apis.md#ga0decdf49ce8a1594d5c99e93648a24f7)) ([cbprintf\_cb](group__cbprintf__apis.md#gaca8362dda031a176d96855a604395a83) out, void \*ctx, const char \*fmt, va\_list ap) |
|  | Signature for a external formatter function identical to cbvprintf. |

| Functions | |
| --- | --- |
| int | [cbprintf\_package](group__cbprintf__apis.md#gad9c56f0a84f60cc53fa9e687069a8f1b) (void \*packaged, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), const char \*format,...) |
|  | Capture state required to output formatted data later. |
| int | [cbvprintf\_package](group__cbprintf__apis.md#gaa83f17925daa9747d329b6f1078ab15a) (void \*packaged, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), const char \*format, va\_list ap) |
|  | Capture state required to output formatted data later. |
| int | [cbprintf\_package\_convert](group__cbprintf__apis.md#ga3d7895fa3997bfd4ecf9cb3711c9bf3f) (void \*in\_packaged, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) in\_len, [cbprintf\_convert\_cb](group__cbprintf__apis.md#ga6e31a5fb5cd760fbb8d0ff5fd5cc3991) cb, void \*ctx, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*strl, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) strl\_len) |
|  | Convert a package. |
| static int | [cbprintf\_package\_copy](group__cbprintf__apis.md#ga881520f4756c1a00270b3b3d12d6fc32) (void \*in\_packaged, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) in\_len, void \*packaged, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*strl, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) strl\_len) |
|  | Copy package with optional appending of strings. |
| static int | [cbprintf\_fsc\_package](group__cbprintf__apis.md#ga66fcefde504d543eb9114bc2fff230d2) (void \*in\_packaged, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) in\_len, void \*packaged, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Convert package to fully self-contained (fsc) package. |
| int | [cbpprintf\_external](group__cbprintf__apis.md#gaa1a040db7e5171dd80d84cd871dfc687) ([cbprintf\_cb](group__cbprintf__apis.md#gaca8362dda031a176d96855a604395a83) out, [cbvprintf\_external\_formatter\_func](group__cbprintf__apis.md#ga0decdf49ce8a1594d5c99e93648a24f7) formatter, void \*ctx, void \*packaged) |
|  | Generate the output for a previously captured format operation using an external formatter. |
| int | [cbprintf](group__cbprintf__apis.md#ga0cebdbf4f142ee28c5bd80a1615647da) ([cbprintf\_cb](group__cbprintf__apis.md#gaca8362dda031a176d96855a604395a83) out, void \*ctx, const char \*format,...) |
|  | \*printf-like output through a callback. |
| static int | [cbvprintf](group__cbprintf__apis.md#ga8958868def2ba1675ebc8b3a70ff86f8) ([cbprintf\_cb](group__cbprintf__apis.md#gaca8362dda031a176d96855a604395a83) out, void \*ctx, const char \*format, va\_list ap) |
|  | varargs-aware \*printf-like output through a callback. |
| static int | [cbvprintf\_tagged\_args](group__cbprintf__apis.md#gae4d5066fff73bb38250f4dc82c43ebdc) ([cbprintf\_cb](group__cbprintf__apis.md#gaca8362dda031a176d96855a604395a83) out, void \*ctx, const char \*format, va\_list ap) |
|  | varargs-aware \*printf-like output through a callback with tagged arguments. |
| static int | [cbpprintf](group__cbprintf__apis.md#ga150fa7bb8dfb96db886006c9115e1dd7) ([cbprintf\_cb](group__cbprintf__apis.md#gaca8362dda031a176d96855a604395a83) out, void \*ctx, void \*packaged) |
|  | Generate the output for a previously captured format operation. |
| int | [fprintfcb](group__cbprintf__apis.md#ga2636e91fd5d78835cfaffe5b5012638b) ([FILE](stdio_8h.md#ac15bbd02a147d1595cdfb8b2979693d7) \*stream, const char \*format,...) |
|  | fprintf using Zephyrs cbprintf infrastructure. |
| int | [vfprintfcb](group__cbprintf__apis.md#ga24d7226976f3acbe579b6d6b5d530ade) ([FILE](stdio_8h.md#ac15bbd02a147d1595cdfb8b2979693d7) \*stream, const char \*format, va\_list ap) |
|  | vfprintf using Zephyrs cbprintf infrastructure. |
| int | [printfcb](group__cbprintf__apis.md#ga17aa694ea800f8188a3de3babd524c3f) (const char \*format,...) |
|  | printf using Zephyrs cbprintf infrastructure. |
| int | [vprintfcb](group__cbprintf__apis.md#gaa70a1b73fb04b88b40c1fa5fd65efd15) (const char \*format, va\_list ap) |
|  | vprintf using Zephyrs cbprintf infrastructure. |
| int | [snprintfcb](group__cbprintf__apis.md#ga909f859afbc2a596cd0174f711a60047) (char \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, const char \*format,...) |
|  | snprintf using Zephyrs cbprintf infrastructure. |
| int | [vsnprintfcb](group__cbprintf__apis.md#ga37b0f96a7b9c025659a902e8fd614b33) (char \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, const char \*format, va\_list ap) |
|  | vsnprintf using Zephyrs cbprintf infrastructure. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [cbprintf.h](cbprintf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/stdio_8h.html
original_path: doxygen/html/stdio_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stdio.h File Reference

`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <stdarg.h>`  
`#include <stddef.h>`

[Go to the source code of this file.](stdio_8h_source.md)

| Macros | |
| --- | --- |
| #define | [EOF](#a59adc4c82490d23754cd39c2fb99b0da)   (-1) |
| #define | [stdin](#aaca70138f0cb63ddb026921afc635179)   (([FILE](#ac15bbd02a147d1595cdfb8b2979693d7) \*) 1) |
| #define | [stdout](#a0c0ef221f95f64e8632451312fd18cc8)   (([FILE](#ac15bbd02a147d1595cdfb8b2979693d7) \*) 2) |
| #define | [stderr](#a5ce35bd5ba5021fd3b2e951e8f497656)   (([FILE](#ac15bbd02a147d1595cdfb8b2979693d7) \*) 3) |
| #define | [SEEK\_SET](#a0d112bae8fd35be772185b6ec6bcbe64)   0 /\* Seek from beginning of file. \*/ |
| #define | [SEEK\_CUR](#a4c8d0b76b470ba65a43ca46a88320f39)   1 /\* Seek from current position. \*/ |
| #define | [SEEK\_END](#ad2a2e6c114780c3071efd24f16c7f7d8)   2 /\* Seek from end of file. \*/ |
| #define | [putc](#a0b8e699e4dfd158acee3d6526fe671c2)(c, stream) |
| #define | [putchar](#a568f021a83b2c22e1e700d12559d660a)(c) |

| Typedefs | |
| --- | --- |
| typedef int | [FILE](#ac15bbd02a147d1595cdfb8b2979693d7) |

| Functions | |
| --- | --- |
| int | [printf](#a6c67912b5a18e7d7ac03ca4e77425715) (const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) format,...) |
| int | [snprintf](#a8524c494bbe2f2e686d35c3bd7ca4f2a) (char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) format,...) |
| int | [sprintf](#aa6f061fe9cbedf135d97a91b0f7c0ca8) (char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) str, const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) format,...) |
| int | [fprintf](#af097ff94eaf1896faa4664dd91858778) ([FILE](#ac15bbd02a147d1595cdfb8b2979693d7) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) stream, const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) format,...) |
| int | [vprintf](#a1af16e2ea2a90f8b64983c9b3e644fad) (const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) format, va\_list list) |
| int | [vsnprintf](#a632165581e7417488441b703393668a4) (char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) format, va\_list list) |
| int | [vsprintf](#a0cf1b75a23729bcc1669ce788d01aa63) (char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) str, const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) format, va\_list list) |
| int | [vfprintf](#abc4556d2008bb7d9345dd8bef8ef65ee) ([FILE](#ac15bbd02a147d1595cdfb8b2979693d7) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) stream, const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) format, va\_list ap) |
| void | [perror](#ab39f9634fa53ffd52b87431f3afab11b) (const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
| int | [puts](#ad41876f99f190c7488e64ef39c50a23f) (const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
| int | [fputc](#abe6299d5823dd023e610aaa619735a3f) (int c, [FILE](#ac15bbd02a147d1595cdfb8b2979693d7) \*stream) |
| int | [fputs](#ab6baefe2032389ec8daadad3492af3e0) (const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), [FILE](#ac15bbd02a147d1595cdfb8b2979693d7) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) stream) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [fwrite](#a610723ed7ffdf7b802f6093d45ffa09d) (const void \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) ptr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) nitems, [FILE](#ac15bbd02a147d1595cdfb8b2979693d7) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) stream) |

## Macro Definition Documentation

## [◆ ](#a59adc4c82490d23754cd39c2fb99b0da)EOF

| #define EOF   (-1) |
| --- |

## [◆ ](#a0b8e699e4dfd158acee3d6526fe671c2)putc

| #define putc | ( |  | *c*, |
| --- | --- | --- | --- |
|  |  |  | *stream* ) |

**Value:**

[fputc](#abe6299d5823dd023e610aaa619735a3f)(c, stream)

[fputc](#abe6299d5823dd023e610aaa619735a3f)

int fputc(int c, FILE \*stream)

## [◆ ](#a568f021a83b2c22e1e700d12559d660a)putchar

| #define putchar | ( |  | *c* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[putc](#a0b8e699e4dfd158acee3d6526fe671c2)(c, [stdout](#a0c0ef221f95f64e8632451312fd18cc8))

[putc](#a0b8e699e4dfd158acee3d6526fe671c2)

#define putc(c, stream)

**Definition** stdio.h:63

[stdout](#a0c0ef221f95f64e8632451312fd18cc8)

#define stdout

**Definition** stdio.h:30

## [◆ ](#a4c8d0b76b470ba65a43ca46a88320f39)SEEK\_CUR

| #define SEEK\_CUR   1 /\* Seek from current position. \*/ |
| --- |

## [◆ ](#ad2a2e6c114780c3071efd24f16c7f7d8)SEEK\_END

| #define SEEK\_END   2 /\* Seek from end of file. \*/ |
| --- |

## [◆ ](#a0d112bae8fd35be772185b6ec6bcbe64)SEEK\_SET

| #define SEEK\_SET   0 /\* Seek from beginning of file. \*/ |
| --- |

## [◆ ](#a5ce35bd5ba5021fd3b2e951e8f497656)stderr

| #define stderr   (([FILE](#ac15bbd02a147d1595cdfb8b2979693d7) \*) 3) |
| --- |

## [◆ ](#aaca70138f0cb63ddb026921afc635179)stdin

| #define stdin   (([FILE](#ac15bbd02a147d1595cdfb8b2979693d7) \*) 1) |
| --- |

## [◆ ](#a0c0ef221f95f64e8632451312fd18cc8)stdout

| #define stdout   (([FILE](#ac15bbd02a147d1595cdfb8b2979693d7) \*) 2) |
| --- |

## Typedef Documentation

## [◆ ](#ac15bbd02a147d1595cdfb8b2979693d7)FILE

| typedef int [FILE](#ac15bbd02a147d1595cdfb8b2979693d7) |
| --- |

## Function Documentation

## [◆ ](#af097ff94eaf1896faa4664dd91858778)fprintf()

| int fprintf | ( | [FILE](#ac15bbd02a147d1595cdfb8b2979693d7) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *stream*, |
| --- | --- | --- | --- |
|  |  | const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *format*, |
|  |  |  | *...* ) |

## [◆ ](#abe6299d5823dd023e610aaa619735a3f)fputc()

| int fputc | ( | int | *c*, |
| --- | --- | --- | --- |
|  |  | [FILE](#ac15bbd02a147d1595cdfb8b2979693d7) \* | *stream* ) |

## [◆ ](#ab6baefe2032389ec8daadad3492af3e0)fputs()

| int fputs | ( | const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *s*, |
| --- | --- | --- | --- |
|  |  | [FILE](#ac15bbd02a147d1595cdfb8b2979693d7) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *stream* ) |

## [◆ ](#a610723ed7ffdf7b802f6093d45ffa09d)fwrite()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) fwrite | ( | const void \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *ptr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *nitems*, |
|  |  | [FILE](#ac15bbd02a147d1595cdfb8b2979693d7) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *stream* ) |

## [◆ ](#ab39f9634fa53ffd52b87431f3afab11b)perror()

| void perror | ( | const char \* | *s* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a6c67912b5a18e7d7ac03ca4e77425715)printf()

| int printf | ( | const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *format*, |
| --- | --- | --- | --- |
|  |  |  | *...* ) |

## [◆ ](#ad41876f99f190c7488e64ef39c50a23f)puts()

| int puts | ( | const char \* | *s* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a8524c494bbe2f2e686d35c3bd7ca4f2a)snprintf()

| int snprintf | ( | char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *str*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *format*, |
|  |  |  | *...* ) |

## [◆ ](#aa6f061fe9cbedf135d97a91b0f7c0ca8)sprintf()

| int sprintf | ( | char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *str*, |
| --- | --- | --- | --- |
|  |  | const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *format*, |
|  |  |  | *...* ) |

## [◆ ](#abc4556d2008bb7d9345dd8bef8ef65ee)vfprintf()

| int vfprintf | ( | [FILE](#ac15bbd02a147d1595cdfb8b2979693d7) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *stream*, |
| --- | --- | --- | --- |
|  |  | const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *format*, |
|  |  | va\_list | *ap* ) |

## [◆ ](#a1af16e2ea2a90f8b64983c9b3e644fad)vprintf()

| int vprintf | ( | const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *format*, |
| --- | --- | --- | --- |
|  |  | va\_list | *list* ) |

## [◆ ](#a632165581e7417488441b703393668a4)vsnprintf()

| int vsnprintf | ( | char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *str*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *format*, |
|  |  | va\_list | *list* ) |

## [◆ ](#a0cf1b75a23729bcc1669ce788d01aa63)vsprintf()

| int vsprintf | ( | char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *str*, |
| --- | --- | --- | --- |
|  |  | const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *format*, |
|  |  | va\_list | *list* ) |

- [lib](dir_97aefd0d527b934f1d99a682da8fe6a9.md)
- [libc](dir_b38b009475962ec458a8a4ac1c89fad6.md)
- [minimal](dir_cb013e9b53665816a2b0a66572d8a7af.md)
- [include](dir_33cd71cddfb4d86c87a49ac212c07c64.md)
- [stdio.h](stdio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

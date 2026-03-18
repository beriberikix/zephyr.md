---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/stdio_8h_source.html
original_path: doxygen/html/stdio_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stdio.h

[Go to the documentation of this file.](stdio_8h.md)

1/\* stdio.h \*/

2

3/\*

4 \* Copyright (c) 2014 Wind River Systems, Inc.

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_STDIO\_H\_

10#define ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_STDIO\_H\_

11

12#include <[zephyr/toolchain.h](toolchain_8h.md)>

13#include <stdarg.h> /\* Needed to get definition of va\_list \*/

14#include <stddef.h>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

20#if !defined(\_\_FILE\_defined)

21#define \_\_FILE\_defined

[ 22](stdio_8h.md#ac15bbd02a147d1595cdfb8b2979693d7)typedef int [FILE](stdio_8h.md#ac15bbd02a147d1595cdfb8b2979693d7);

23#endif

24

25#if !defined(EOF)

[ 26](stdio_8h.md#a59adc4c82490d23754cd39c2fb99b0da)#define EOF (-1)

27#endif

28

[ 29](stdio_8h.md#aaca70138f0cb63ddb026921afc635179)#define stdin ((FILE \*) 1)

[ 30](stdio_8h.md#a0c0ef221f95f64e8632451312fd18cc8)#define stdout ((FILE \*) 2)

[ 31](stdio_8h.md#a5ce35bd5ba5021fd3b2e951e8f497656)#define stderr ((FILE \*) 3)

32

[ 33](stdio_8h.md#a0d112bae8fd35be772185b6ec6bcbe64)#define SEEK\_SET 0 /\* Seek from beginning of file. \*/

[ 34](stdio_8h.md#a4c8d0b76b470ba65a43ca46a88320f39)#define SEEK\_CUR 1 /\* Seek from current position. \*/

[ 35](stdio_8h.md#ad2a2e6c114780c3071efd24f16c7f7d8)#define SEEK\_END 2 /\* Seek from end of file. \*/

36

[ 37](stdio_8h.md#a6c67912b5a18e7d7ac03ca4e77425715)int \_\_printf\_like(1, 2) [printf](stdio_8h.md#a6c67912b5a18e7d7ac03ca4e77425715)(const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) format, ...);

[ 38](stdio_8h.md#a8524c494bbe2f2e686d35c3bd7ca4f2a)int \_\_printf\_like(3, 4) [snprintf](stdio_8h.md#a8524c494bbe2f2e686d35c3bd7ca4f2a)(char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) str, size\_t len,

39 const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) format, ...);

[ 40](stdio_8h.md#aa6f061fe9cbedf135d97a91b0f7c0ca8)int \_\_printf\_like(2, 3) [sprintf](stdio_8h.md#aa6f061fe9cbedf135d97a91b0f7c0ca8)(char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) str,

41 const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) format, ...);

[ 42](stdio_8h.md#af097ff94eaf1896faa4664dd91858778)int \_\_printf\_like(2, 3) [fprintf](stdio_8h.md#af097ff94eaf1896faa4664dd91858778)([FILE](stdio_8h.md#ac15bbd02a147d1595cdfb8b2979693d7) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) stream,

43 const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) format, ...);

44

45

[ 46](stdio_8h.md#a1af16e2ea2a90f8b64983c9b3e644fad)int \_\_printf\_like(1, 0) [vprintf](stdio_8h.md#a1af16e2ea2a90f8b64983c9b3e644fad)(const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) format, va\_list list);

[ 47](stdio_8h.md#a632165581e7417488441b703393668a4)int \_\_printf\_like(3, 0) [vsnprintf](stdio_8h.md#a632165581e7417488441b703393668a4)(char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) str, size\_t len,

48 const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) format,

49 va\_list list);

[ 50](stdio_8h.md#a0cf1b75a23729bcc1669ce788d01aa63)int \_\_printf\_like(2, 0) [vsprintf](stdio_8h.md#a0cf1b75a23729bcc1669ce788d01aa63)(char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) str,

51 const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) format, va\_list list);

[ 52](stdio_8h.md#abc4556d2008bb7d9345dd8bef8ef65ee)int \_\_printf\_like(2, 0) [vfprintf](stdio_8h.md#abc4556d2008bb7d9345dd8bef8ef65ee)([FILE](stdio_8h.md#ac15bbd02a147d1595cdfb8b2979693d7) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) stream,

53 const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) format,

54 va\_list ap);

55

[ 56](stdio_8h.md#ab39f9634fa53ffd52b87431f3afab11b)void [perror](stdio_8h.md#ab39f9634fa53ffd52b87431f3afab11b)(const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d));

[ 57](stdio_8h.md#ad41876f99f190c7488e64ef39c50a23f)int [puts](stdio_8h.md#ad41876f99f190c7488e64ef39c50a23f)(const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d));

58

[ 59](stdio_8h.md#abe6299d5823dd023e610aaa619735a3f)int [fputc](stdio_8h.md#abe6299d5823dd023e610aaa619735a3f)(int c, [FILE](stdio_8h.md#ac15bbd02a147d1595cdfb8b2979693d7) \*stream);

[ 60](stdio_8h.md#ab6baefe2032389ec8daadad3492af3e0)int [fputs](stdio_8h.md#ab6baefe2032389ec8daadad3492af3e0)(const char \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), [FILE](stdio_8h.md#ac15bbd02a147d1595cdfb8b2979693d7) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) stream);

[ 61](stdio_8h.md#a610723ed7ffdf7b802f6093d45ffa09d)size\_t [fwrite](stdio_8h.md#a610723ed7ffdf7b802f6093d45ffa09d)(const void \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) ptr, size\_t size, size\_t nitems,

62 [FILE](stdio_8h.md#ac15bbd02a147d1595cdfb8b2979693d7) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) stream);

[ 63](stdio_8h.md#a0b8e699e4dfd158acee3d6526fe671c2)#define putc(c, stream) fputc(c, stream)

[ 64](stdio_8h.md#a568f021a83b2c22e1e700d12559d660a)#define putchar(c) putc(c, stdout)

65

66#ifdef \_\_cplusplus

67}

68#endif

69

70#endif /\* ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_STDIO\_H\_ \*/

[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa s

**Definition** asm-macro-32-bit-gnu.h:17

[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd)

#define ZRESTRICT

**Definition** common.h:36

[vsprintf](stdio_8h.md#a0cf1b75a23729bcc1669ce788d01aa63)

int vsprintf(char \*ZRESTRICT str, const char \*ZRESTRICT format, va\_list list)

[vprintf](stdio_8h.md#a1af16e2ea2a90f8b64983c9b3e644fad)

int vprintf(const char \*ZRESTRICT format, va\_list list)

[fwrite](stdio_8h.md#a610723ed7ffdf7b802f6093d45ffa09d)

size\_t fwrite(const void \*ZRESTRICT ptr, size\_t size, size\_t nitems, FILE \*ZRESTRICT stream)

[vsnprintf](stdio_8h.md#a632165581e7417488441b703393668a4)

int vsnprintf(char \*ZRESTRICT str, size\_t len, const char \*ZRESTRICT format, va\_list list)

[printf](stdio_8h.md#a6c67912b5a18e7d7ac03ca4e77425715)

int printf(const char \*ZRESTRICT format,...)

[snprintf](stdio_8h.md#a8524c494bbe2f2e686d35c3bd7ca4f2a)

int snprintf(char \*ZRESTRICT str, size\_t len, const char \*ZRESTRICT format,...)

[sprintf](stdio_8h.md#aa6f061fe9cbedf135d97a91b0f7c0ca8)

int sprintf(char \*ZRESTRICT str, const char \*ZRESTRICT format,...)

[perror](stdio_8h.md#ab39f9634fa53ffd52b87431f3afab11b)

void perror(const char \*s)

[fputs](stdio_8h.md#ab6baefe2032389ec8daadad3492af3e0)

int fputs(const char \*ZRESTRICT s, FILE \*ZRESTRICT stream)

[vfprintf](stdio_8h.md#abc4556d2008bb7d9345dd8bef8ef65ee)

int vfprintf(FILE \*ZRESTRICT stream, const char \*ZRESTRICT format, va\_list ap)

[fputc](stdio_8h.md#abe6299d5823dd023e610aaa619735a3f)

int fputc(int c, FILE \*stream)

[FILE](stdio_8h.md#ac15bbd02a147d1595cdfb8b2979693d7)

int FILE

**Definition** stdio.h:22

[puts](stdio_8h.md#ad41876f99f190c7488e64ef39c50a23f)

int puts(const char \*s)

[fprintf](stdio_8h.md#af097ff94eaf1896faa4664dd91858778)

int fprintf(FILE \*ZRESTRICT stream, const char \*ZRESTRICT format,...)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [lib](dir_97aefd0d527b934f1d99a682da8fe6a9.md)
- [libc](dir_b38b009475962ec458a8a4ac1c89fad6.md)
- [minimal](dir_cb013e9b53665816a2b0a66572d8a7af.md)
- [include](dir_33cd71cddfb4d86c87a49ac212c07c64.md)
- [stdio.h](stdio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

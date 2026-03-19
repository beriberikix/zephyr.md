---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/posix__trace_8h_source.html
original_path: doxygen/html/posix__trace_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

posix\_trace.h

[Go to the documentation of this file.](posix__trace_8h.md)

1/\*

2 \* Copyright (c) 2018 Oticon A/S

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_ARCH\_POSIX\_POSIX\_TRACE\_H\_

7#define ZEPHYR\_INCLUDE\_ARCH\_POSIX\_POSIX\_TRACE\_H\_

8

9#include <stdarg.h>

10

11#ifdef \_\_cplusplus

12extern "C" {

13#endif

14

[ 15](posix__trace_8h.md#a32a51af41cb882c0501bb546ee9101be)void [posix\_vprint\_error\_and\_exit](posix__trace_8h.md#a32a51af41cb882c0501bb546ee9101be)(const char \*format, va\_list vargs);

[ 16](posix__trace_8h.md#a7f80b5ea2341194449a0ce1f73189f7a)void [posix\_vprint\_warning](posix__trace_8h.md#a7f80b5ea2341194449a0ce1f73189f7a)(const char \*format, va\_list vargs);

[ 17](posix__trace_8h.md#a47734632b39bf660479912d81cb3a1d2)void [posix\_vprint\_trace](posix__trace_8h.md#a47734632b39bf660479912d81cb3a1d2)(const char \*format, va\_list vargs);

[ 18](posix__trace_8h.md#a72de7f92ede3f7cdd10b11f43cad15f4)void [posix\_print\_error\_and\_exit](posix__trace_8h.md#a72de7f92ede3f7cdd10b11f43cad15f4)(const char \*format, ...);

[ 19](posix__trace_8h.md#a0dc1a339ea12ed43d8212afb62fd28fb)void [posix\_print\_warning](posix__trace_8h.md#a0dc1a339ea12ed43d8212afb62fd28fb)(const char \*format, ...);

[ 20](posix__trace_8h.md#a7b6b007c25712162299523a17b876649)void [posix\_print\_trace](posix__trace_8h.md#a7b6b007c25712162299523a17b876649)(const char \*format, ...);

21/\*

22 \* Return 1 if traces to <output> will go to a tty.

23 \* When printing to a terminal we may use ASCII escapes for color or other

24 \* niceties.

25 \* But when redirecting to files, or piping to other commands, those should be

26 \* disabled by default.

27 \*

28 \* Where the <output> should be set to 0 to query about posix\_print\_trace output

29 \* (typically STDOUT)

30 \* and 1 to query about the warning and error output (posix\_print\_error/warning)

31 \* outputs (typically STDERR)

32 \*/

[ 33](posix__trace_8h.md#a6534292708ffe70aa324861b54867aec)int [posix\_trace\_over\_tty](posix__trace_8h.md#a6534292708ffe70aa324861b54867aec)(int output);

34

35#ifdef \_\_cplusplus

36}

37#endif

38

39#endif

[posix\_print\_warning](posix__trace_8h.md#a0dc1a339ea12ed43d8212afb62fd28fb)

void posix\_print\_warning(const char \*format,...)

[posix\_vprint\_error\_and\_exit](posix__trace_8h.md#a32a51af41cb882c0501bb546ee9101be)

void posix\_vprint\_error\_and\_exit(const char \*format, va\_list vargs)

[posix\_vprint\_trace](posix__trace_8h.md#a47734632b39bf660479912d81cb3a1d2)

void posix\_vprint\_trace(const char \*format, va\_list vargs)

[posix\_trace\_over\_tty](posix__trace_8h.md#a6534292708ffe70aa324861b54867aec)

int posix\_trace\_over\_tty(int output)

[posix\_print\_error\_and\_exit](posix__trace_8h.md#a72de7f92ede3f7cdd10b11f43cad15f4)

void posix\_print\_error\_and\_exit(const char \*format,...)

[posix\_print\_trace](posix__trace_8h.md#a7b6b007c25712162299523a17b876649)

void posix\_print\_trace(const char \*format,...)

[posix\_vprint\_warning](posix__trace_8h.md#a7f80b5ea2341194449a0ce1f73189f7a)

void posix\_vprint\_warning(const char \*format, va\_list vargs)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [posix](dir_2eaa0886f2679378503a1f6e740c4205.md)
- [posix\_trace.h](posix__trace_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

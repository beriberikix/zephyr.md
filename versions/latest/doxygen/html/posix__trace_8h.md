---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/posix__trace_8h.html
original_path: doxygen/html/posix__trace_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

posix\_trace.h File Reference

`#include <stdarg.h>`

[Go to the source code of this file.](posix__trace_8h_source.md)

| Functions | |
| --- | --- |
| void | [posix\_vprint\_error\_and\_exit](#a32a51af41cb882c0501bb546ee9101be) (const char \*format, va\_list vargs) |
| void | [posix\_vprint\_warning](#a7f80b5ea2341194449a0ce1f73189f7a) (const char \*format, va\_list vargs) |
| void | [posix\_vprint\_trace](#a47734632b39bf660479912d81cb3a1d2) (const char \*format, va\_list vargs) |
| void | [posix\_print\_error\_and\_exit](#a72de7f92ede3f7cdd10b11f43cad15f4) (const char \*format,...) |
| void | [posix\_print\_warning](#a0dc1a339ea12ed43d8212afb62fd28fb) (const char \*format,...) |
| void | [posix\_print\_trace](#a7b6b007c25712162299523a17b876649) (const char \*format,...) |
| int | [posix\_trace\_over\_tty](#a6534292708ffe70aa324861b54867aec) (int output) |

## Function Documentation

## [◆ ](#a72de7f92ede3f7cdd10b11f43cad15f4)posix\_print\_error\_and\_exit()

| void posix\_print\_error\_and\_exit | ( | const char \* | *format*, |
| --- | --- | --- | --- |
|  |  |  | *...* ) |

## [◆ ](#a7b6b007c25712162299523a17b876649)posix\_print\_trace()

| void posix\_print\_trace | ( | const char \* | *format*, |
| --- | --- | --- | --- |
|  |  |  | *...* ) |

## [◆ ](#a0dc1a339ea12ed43d8212afb62fd28fb)posix\_print\_warning()

| void posix\_print\_warning | ( | const char \* | *format*, |
| --- | --- | --- | --- |
|  |  |  | *...* ) |

## [◆ ](#a6534292708ffe70aa324861b54867aec)posix\_trace\_over\_tty()

| int posix\_trace\_over\_tty | ( | int | *output* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a32a51af41cb882c0501bb546ee9101be)posix\_vprint\_error\_and\_exit()

| void posix\_vprint\_error\_and\_exit | ( | const char \* | *format*, |
| --- | --- | --- | --- |
|  |  | va\_list | *vargs* ) |

## [◆ ](#a47734632b39bf660479912d81cb3a1d2)posix\_vprint\_trace()

| void posix\_vprint\_trace | ( | const char \* | *format*, |
| --- | --- | --- | --- |
|  |  | va\_list | *vargs* ) |

## [◆ ](#a7f80b5ea2341194449a0ce1f73189f7a)posix\_vprint\_warning()

| void posix\_vprint\_warning | ( | const char \* | *format*, |
| --- | --- | --- | --- |
|  |  | va\_list | *vargs* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [posix](dir_2eaa0886f2679378503a1f6e740c4205.md)
- [posix\_trace.h](posix__trace_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

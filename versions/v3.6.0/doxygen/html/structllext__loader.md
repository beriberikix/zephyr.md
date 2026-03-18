---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structllext__loader.html
original_path: doxygen/html/structllext__loader.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

llext\_loader Struct Reference

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext.md) » [Loader context for llext](group__llext__loader.md)

Linkable loadable extension loader context.
[More...](#details)

`#include <[loader.h](loader_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [read](#a29a16df55b72bc299b338036437f53e0) )(struct [llext\_loader](structllext__loader.md) \*ldr, void \*out, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Read (copy) from the loader. |
| int(\* | [seek](#a2376c3774af219972e164b0ee8a6bb6d) )(struct [llext\_loader](structllext__loader.md) \*ldr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) pos) |
|  | Seek to a new absolute location. |
| void \*(\* | [peek](#af5452f4b4f1099379d110c1bcd7773f6) )(struct [llext\_loader](structllext__loader.md) \*ldr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) pos) |
|  | Peek at an absolute location. |

## Detailed Description

Linkable loadable extension loader context.

## Field Documentation

## [◆ ](#af5452f4b4f1099379d110c1bcd7773f6)peek

| void \*(\* llext\_loader::peek) (struct [llext\_loader](structllext__loader.md) \*ldr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) pos) |
| --- |

Peek at an absolute location.

Return a pointer to the buffer at specified offset.

Parameters
:   | [in] | ldr | Loader |
    | --- | --- | --- |
    | [in] | pos | Position to obtain a pointer to |

Return values
:   | pointer | into the buffer |
    | --- | --- |

## [◆ ](#a29a16df55b72bc299b338036437f53e0)read

| int(\* llext\_loader::read) (struct [llext\_loader](structllext__loader.md) \*ldr, void \*out, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| --- |

Read (copy) from the loader.

Copies len bytes into buf from the current position of the loader.

Parameters
:   | [in] | ldr | Loader |
    | --- | --- | --- |
    | [in] | out | Output location |
    | [in] | len | Length to copy into the output location |

Return values
:   | 0 | Success |
    | --- | --- |
    | -errno | Error reading (any errno) |

## [◆ ](#a2376c3774af219972e164b0ee8a6bb6d)seek

| int(\* llext\_loader::seek) (struct [llext\_loader](structllext__loader.md) \*ldr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) pos) |
| --- |

Seek to a new absolute location.

Changes the location of the loader position to a new absolute given position.

Parameters
:   | [in] | ldr | Loader |
    | --- | --- | --- |
    | [in] | pos | Position in stream to move loader |

Return values
:   | 0 | Success |
    | --- | --- |
    | -errno | Error reading (any errno) |

---

The documentation for this struct was generated from the following file:

- zephyr/llext/[loader.h](loader_8h_source.md)

- [llext\_loader](structllext__loader.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

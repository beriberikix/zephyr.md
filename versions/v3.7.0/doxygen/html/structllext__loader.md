---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structllext__loader.html
original_path: doxygen/html/structllext__loader.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

llext\_loader Struct Reference

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext__apis.md) » [ELF loader context](group__llext__loader__apis.md)

Linkable loadable extension loader context.
[More...](#details)

`#include <[loader.h](loader_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [read](#a29a16df55b72bc299b338036437f53e0) )(struct [llext\_loader](structllext__loader.md) \*ldr, void \*out, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Function to read (copy) from the loader. |
| int(\* | [seek](#a2376c3774af219972e164b0ee8a6bb6d) )(struct [llext\_loader](structllext__loader.md) \*ldr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) pos) |
|  | Function to seek to a new absolute location in the stream. |
| void \*(\* | [peek](#af5452f4b4f1099379d110c1bcd7773f6) )(struct [llext\_loader](structllext__loader.md) \*ldr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) pos) |
|  | Optional function to peek at an absolute location in the ELF. |

## Detailed Description

Linkable loadable extension loader context.

This object is used to access the ELF file data and cache its contents while an extension is being loaded by the LLEXT subsystem. Once the extension is loaded, this object is no longer needed.

## Field Documentation

## [◆ ](#af5452f4b4f1099379d110c1bcd7773f6)peek

| void \*(\* llext\_loader::peek) (struct [llext\_loader](structllext__loader.md) \*ldr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) pos) |
| --- |

Optional function to peek at an absolute location in the ELF.

Return a pointer to the buffer at specified offset.

Parameters
:   | [in] | ldr | Loader |
    | --- | --- | --- |
    | [in] | pos | Position to obtain a pointer to |

Returns
:   a pointer into the buffer or NULL if not supported

## [◆ ](#a29a16df55b72bc299b338036437f53e0)read

| int(\* llext\_loader::read) (struct [llext\_loader](structllext__loader.md) \*ldr, void \*out, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| --- |

Function to read (copy) from the loader.

Copies len bytes into buf from the current position of the loader.

Parameters
:   | [in] | ldr | Loader |
    | --- | --- | --- |
    | [in] | out | Output location |
    | [in] | len | Length to copy into the output location |

Returns
:   0 on success, or a negative error code.

## [◆ ](#a2376c3774af219972e164b0ee8a6bb6d)seek

| int(\* llext\_loader::seek) (struct [llext\_loader](structllext__loader.md) \*ldr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) pos) |
| --- |

Function to seek to a new absolute location in the stream.

Changes the location of the loader position to a new absolute given position.

Parameters
:   | [in] | ldr | Loader |
    | --- | --- | --- |
    | [in] | pos | Position in stream to move loader |

Returns
:   0 on success, or a negative error code.

---

The documentation for this struct was generated from the following file:

- zephyr/llext/[loader.h](loader_8h_source.md)

- [llext\_loader](structllext__loader.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/debug_2gdbstub_8h.html
original_path: doxygen/html/debug_2gdbstub_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gdbstub.h File Reference

[Go to the source code of this file.](debug_2gdbstub_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [gdb\_mem\_region](structgdb__mem__region.md) |
|  | Describe one memory region. [More...](structgdb__mem__region.md#details) |

| Macros | |
| --- | --- |
| #define | [GDB\_EXCEPTION\_INVALID\_INSTRUCTION](#a34e3537cdca807d30b24ce76ab1e503c)   4UL |
| #define | [GDB\_EXCEPTION\_BREAKPOINT](#af97b5ae81a45e635e69c613b4e2fa9f4)   5UL |
| #define | [GDB\_EXCEPTION\_MEMORY\_FAULT](#a37ea8e51fd123a434d6d221280cedca2)   7UL |
| #define | [GDB\_EXCEPTION\_DIVIDE\_ERROR](#ad65b407f7c8d6d44ab5886866ee2d9da)   8UL |
| #define | [GDB\_EXCEPTION\_INVALID\_MEMORY](#a94da0c93f951fc608c76a525251a9d3a)   11UL |
| #define | [GDB\_EXCEPTION\_OVERFLOW](#acc588c5509a9cf55df485b90dff54ba4)   16UL |
| #define | [GDB\_MEM\_REGION\_NO\_ACCESS](#a02b9a9d5f33f9ee43bfdd0e68a9a6462)   0UL |
| #define | [GDB\_MEM\_REGION\_READ](#a8a7f81403bcc747817792171bf502d1a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [GDB\_MEM\_REGION\_WRITE](#adb7926e4055fc3ffd94da16c9f0a97b6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [GDB\_MEM\_REGION\_RO](#a083549c8b9db7f28536481e33d362479)   ([GDB\_MEM\_REGION\_READ](#a8a7f81403bcc747817792171bf502d1a)) |
| #define | [GDB\_MEM\_REGION\_RW](#a386751baaedc3e607a37a473a88bb05a)   ([GDB\_MEM\_REGION\_READ](#a8a7f81403bcc747817792171bf502d1a) | [GDB\_MEM\_REGION\_WRITE](#adb7926e4055fc3ffd94da16c9f0a97b6)) |

| Enumerations | |
| --- | --- |
| enum | [gdb\_loop\_state](#aa266df02c8e0a69322bb2a6d40670c57) { [GDB\_LOOP\_RECEIVING](#aa266df02c8e0a69322bb2a6d40670c57ae6d3b76f57693d31a91014cb1d595f73) , [GDB\_LOOP\_CONTINUE](#aa266df02c8e0a69322bb2a6d40670c57a7bb32aeeb3ec6d88e37bf05306cb5e4a) , [GDB\_LOOP\_ERROR](#aa266df02c8e0a69322bb2a6d40670c57a00f30ed14785675b4c9f8392cf5e8077) } |
|  | State of the packet processing loop. [More...](#aa266df02c8e0a69322bb2a6d40670c57) |

| Functions | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [gdb\_bin2hex](#ab392b604a2edf4bea077eb7fa02079e1) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buflen, char \*hex, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) hexlen) |
|  | Convert a binary array into string representation. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [gdb\_mem\_can\_read](#add890d2dc6e197a2b94c45c4de94c8b1) (const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) addr, const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*align) |
|  | Check if a memory block can be read. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [gdb\_mem\_can\_write](#aac6c53353a4751d835028c6fd9906d19) (const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) addr, const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*align) |
|  | Check if a memory block can be written into. |

| Variables | |
| --- | --- |
| const struct [gdb\_mem\_region](structgdb__mem__region.md) | [gdb\_mem\_region\_array](#a9d01831c656bae3ee4592ccb45456295) [] |
|  | Memory region descriptions used for GDB memory access. |
| const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [gdb\_mem\_num\_regions](#a439e80da6ae6e5388f9a78744d0978d1) |
|  | Number of Memory Regions. |

## Macro Definition Documentation

## [◆ ](#af97b5ae81a45e635e69c613b4e2fa9f4)GDB\_EXCEPTION\_BREAKPOINT

| #define GDB\_EXCEPTION\_BREAKPOINT   5UL |
| --- |

## [◆ ](#ad65b407f7c8d6d44ab5886866ee2d9da)GDB\_EXCEPTION\_DIVIDE\_ERROR

| #define GDB\_EXCEPTION\_DIVIDE\_ERROR   8UL |
| --- |

## [◆ ](#a34e3537cdca807d30b24ce76ab1e503c)GDB\_EXCEPTION\_INVALID\_INSTRUCTION

| #define GDB\_EXCEPTION\_INVALID\_INSTRUCTION   4UL |
| --- |

## [◆ ](#a94da0c93f951fc608c76a525251a9d3a)GDB\_EXCEPTION\_INVALID\_MEMORY

| #define GDB\_EXCEPTION\_INVALID\_MEMORY   11UL |
| --- |

## [◆ ](#a37ea8e51fd123a434d6d221280cedca2)GDB\_EXCEPTION\_MEMORY\_FAULT

| #define GDB\_EXCEPTION\_MEMORY\_FAULT   7UL |
| --- |

## [◆ ](#acc588c5509a9cf55df485b90dff54ba4)GDB\_EXCEPTION\_OVERFLOW

| #define GDB\_EXCEPTION\_OVERFLOW   16UL |
| --- |

## [◆ ](#a02b9a9d5f33f9ee43bfdd0e68a9a6462)GDB\_MEM\_REGION\_NO\_ACCESS

| #define GDB\_MEM\_REGION\_NO\_ACCESS   0UL |
| --- |

## [◆ ](#a8a7f81403bcc747817792171bf502d1a)GDB\_MEM\_REGION\_READ

| #define GDB\_MEM\_REGION\_READ   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a083549c8b9db7f28536481e33d362479)GDB\_MEM\_REGION\_RO

| #define GDB\_MEM\_REGION\_RO   ([GDB\_MEM\_REGION\_READ](#a8a7f81403bcc747817792171bf502d1a)) |
| --- |

## [◆ ](#a386751baaedc3e607a37a473a88bb05a)GDB\_MEM\_REGION\_RW

| #define GDB\_MEM\_REGION\_RW   ([GDB\_MEM\_REGION\_READ](#a8a7f81403bcc747817792171bf502d1a) | [GDB\_MEM\_REGION\_WRITE](#adb7926e4055fc3ffd94da16c9f0a97b6)) |
| --- |

## [◆ ](#adb7926e4055fc3ffd94da16c9f0a97b6)GDB\_MEM\_REGION\_WRITE

| #define GDB\_MEM\_REGION\_WRITE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## Enumeration Type Documentation

## [◆ ](#aa266df02c8e0a69322bb2a6d40670c57)gdb\_loop\_state

| enum [gdb\_loop\_state](#aa266df02c8e0a69322bb2a6d40670c57) |
| --- |

State of the packet processing loop.

| Enumerator | |
| --- | --- |
| GDB\_LOOP\_RECEIVING |  |
| GDB\_LOOP\_CONTINUE |  |
| GDB\_LOOP\_ERROR |  |

## Function Documentation

## [◆ ](#ab392b604a2edf4bea077eb7fa02079e1)gdb\_bin2hex()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) gdb\_bin2hex | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *buflen*, |
|  |  | char \* | *hex*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *hexlen* ) |

Convert a binary array into string representation.

Note that this is similar to [bin2hex()](group__sys-util.md#gaf8f2ab98cc3f045ba834dbbb13a5dfd7 "Convert a binary array into string representation.") but does not force a null character at the end of the hexadecimal output buffer.

Parameters
:   | buf | The binary array to convert |
    | --- | --- |
    | buflen | The length of the binary array to convert |
    | hex | Address of where to store the string representation. |
    | hexlen | Size of the storage area for string representation. |

Returns
:   The length of the converted string, or 0 if an error occurred.

## [◆ ](#add890d2dc6e197a2b94c45c4de94c8b1)gdb\_mem\_can\_read()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) gdb\_mem\_can\_read | ( | const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *addr*, |
| --- | --- | --- | --- |
|  |  | const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *align* ) |

Check if a memory block can be read.

This checks if the specified memory block can be read.

Parameters
:   | [in] | addr | Starting address of the memory block |
    | --- | --- | --- |
    | [in] | len | Size of memory block |
    | [out] | align | Read alignment of region |

Returns
:   True if memory block can be read, false otherwise.

## [◆ ](#aac6c53353a4751d835028c6fd9906d19)gdb\_mem\_can\_write()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) gdb\_mem\_can\_write | ( | const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *addr*, |
| --- | --- | --- | --- |
|  |  | const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *align* ) |

Check if a memory block can be written into.

This checks if the specified memory block can be written into.

Parameters
:   | [in] | addr | Starting address of the memory block |
    | --- | --- | --- |
    | [in] | len | Size of memory block |
    | [out] | align | Write alignment of region |

Returns
:   True if GDB stub can write to the block, false otherwise.

## Variable Documentation

## [◆ ](#a439e80da6ae6e5388f9a78744d0978d1)gdb\_mem\_num\_regions

| | const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) gdb\_mem\_num\_regions | | --- | | extern |
| --- | --- | --- |

Number of Memory Regions.

Number of elements in gdb\_mem\_region\_array[];

## [◆ ](#a9d01831c656bae3ee4592ccb45456295)gdb\_mem\_region\_array

| | const struct [gdb\_mem\_region](structgdb__mem__region.md) gdb\_mem\_region\_array[] | | --- | | extern |
| --- | --- | --- |

Memory region descriptions used for GDB memory access.

This array specifies which region of memory GDB can access with read/write attributes. This is used to restrict memory read/write in GDB stub to memory that can be legally accessed without resulting in memory faults.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [debug](dir_44aa0acd5660d74ea205f18be43003ca.md)
- [gdbstub.h](debug_2gdbstub_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

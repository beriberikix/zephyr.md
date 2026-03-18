---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/stream__flash_8h.html
original_path: doxygen/html/stream__flash_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stream\_flash.h File Reference

Public API for stream writes to flash.
[More...](#details)

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/drivers/flash.h](flash_8h_source.md)>`

[Go to the source code of this file.](stream__flash_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [stream\_flash\_ctx](structstream__flash__ctx.md) |
|  | Structure for stream flash context. [More...](structstream__flash__ctx.md#details) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [stream\_flash\_callback\_t](group__stream__flash.md#ga0bf1914bba75d4d799d546b917e35705)) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset) |
|  | Signature for callback invoked after flash write completes. |

| Functions | |
| --- | --- |
| int | [stream\_flash\_init](group__stream__flash.md#ga63e6418e220136a9a0ab2992d9d8f937) (struct [stream\_flash\_ctx](structstream__flash__ctx.md) \*ctx, const struct [device](structdevice.md) \*fdev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buf\_len, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [stream\_flash\_callback\_t](group__stream__flash.md#ga0bf1914bba75d4d799d546b917e35705) cb) |
|  | Initialize context needed for stream writes to flash. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [stream\_flash\_bytes\_written](group__stream__flash.md#gadcff5388f54e0e784619c706795fe7a8) (struct [stream\_flash\_ctx](structstream__flash__ctx.md) \*ctx) |
|  | Read number of bytes written to the flash. |
| int | [stream\_flash\_buffered\_write](group__stream__flash.md#gaa23d33939f344fcd42a281afa5e6f1db) (struct [stream\_flash\_ctx](structstream__flash__ctx.md) \*ctx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) flush) |
|  | Process input buffers to be written to flash device in single blocks. |
| int | [stream\_flash\_erase\_page](group__stream__flash.md#ga75711b22789724c2d8629e1202dcb48d) (struct [stream\_flash\_ctx](structstream__flash__ctx.md) \*ctx, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)) |
|  | Erase the flash page to which a given offset belongs. |
| int | [stream\_flash\_progress\_load](group__stream__flash.md#ga2d90ef00da4ded8c2d0ffb1b2e4c2a2f) (struct [stream\_flash\_ctx](structstream__flash__ctx.md) \*ctx, const char \*settings\_key) |
|  | Load persistent stream write progress stored with key `settings_key` . |
| int | [stream\_flash\_progress\_save](group__stream__flash.md#ga6965ef8973f281fd0507e208d1645483) (struct [stream\_flash\_ctx](structstream__flash__ctx.md) \*ctx, const char \*settings\_key) |
|  | Save persistent stream write progress using key `settings_key` . |
| int | [stream\_flash\_progress\_clear](group__stream__flash.md#gafd736d9014a3c5060d5c43383d07ac59) (struct [stream\_flash\_ctx](structstream__flash__ctx.md) \*ctx, const char \*settings\_key) |
|  | Clear persistent stream write progress stored with key `settings_key` . |

## Detailed Description

Public API for stream writes to flash.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [storage](dir_9ae83148a5180e4d77f53cf673d8ea1c.md)
- [stream\_flash.h](stream__flash_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

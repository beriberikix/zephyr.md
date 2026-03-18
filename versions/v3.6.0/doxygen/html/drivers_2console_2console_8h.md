---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/drivers_2console_2console_8h.html
original_path: doxygen/html/drivers_2console_2console_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

console.h File Reference

[Go to the source code of this file.](drivers_2console_2console_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [console\_input](structconsole__input.md) |
|  | Console input representation. [More...](structconsole__input.md#details) |

| Macros | |
| --- | --- |
| #define | [CONSOLE\_MAX\_LINE\_LEN](#ae5aa23edbc2609d1b766340c14fd5a68)   CONFIG\_CONSOLE\_INPUT\_MAX\_LINE\_LEN |

| Typedefs | |
| --- | --- |
| typedef void(\* | [console\_input\_fn](#a0dab6d89950bb4c2bbb17571b9b1461f)) (struct [k\_fifo](structk__fifo.md) \*avail, struct [k\_fifo](structk__fifo.md) \*lines, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\*completion) (char \*str, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len)) |
|  | Console input processing handler signature. |

## Macro Definition Documentation

## [◆ ](#ae5aa23edbc2609d1b766340c14fd5a68)CONSOLE\_MAX\_LINE\_LEN

| #define CONSOLE\_MAX\_LINE\_LEN   CONFIG\_CONSOLE\_INPUT\_MAX\_LINE\_LEN |
| --- |

## Typedef Documentation

## [◆ ](#a0dab6d89950bb4c2bbb17571b9b1461f)console\_input\_fn

| typedef void(\* console\_input\_fn) (struct [k\_fifo](structk__fifo.md) \*avail, struct [k\_fifo](structk__fifo.md) \*lines, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\*completion)(char \*str, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len)) |
| --- |

Console input processing handler signature.

Input processing is started when string is typed in the console. Carriage return is translated to NULL making string always NULL terminated. Application before calling register function need to initialize two fifo queues mentioned below.

Parameters
:   | avail | [k\_fifo](structk__fifo.md) queue keeping available input slots |
    | --- | --- |
    | lines | [k\_fifo](structk__fifo.md) queue of entered lines which to be processed in the application code. |
    | completion | callback for tab completion of entered commands |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [console](dir_5678202c8994e72aafde82bf91697a82.md)
- [console.h](drivers_2console_2console_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/uart__console_8h.html
original_path: doxygen/html/uart__console_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_console.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

[Go to the source code of this file.](uart__console_8h_source.md)

| Functions | |
| --- | --- |
| void | [uart\_register\_input](#a090eed88ce36e49ecea535d61746abd5) (struct [k\_fifo](structk__fifo.md) \*avail, struct [k\_fifo](structk__fifo.md) \*lines, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\*completion)(char \*str, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len)) |
|  | Register uart input processing. |

## Function Documentation

## [◆ ](#a090eed88ce36e49ecea535d61746abd5)uart\_register\_input()

| void uart\_register\_input | ( | struct [k\_fifo](structk__fifo.md) \* | *avail*, |
| --- | --- | --- | --- |
|  |  | struct [k\_fifo](structk__fifo.md) \* | *lines*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* | *completion*)(char \*str, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len) ) |

Register uart input processing.

Input processing is started when string is typed in the console. Carriage return is translated to NULL making string always NULL terminated. Application before calling register function need to initialize two fifo queues mentioned below.

Parameters
:   | avail | [k\_fifo](structk__fifo.md) queue keeping available input slots |
    | --- | --- |
    | lines | [k\_fifo](structk__fifo.md) queue of entered lines which to be processed in the application code. |
    | completion | callback for tab completion of entered commands |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [console](dir_5678202c8994e72aafde82bf91697a82.md)
- [uart\_console.h](uart__console_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

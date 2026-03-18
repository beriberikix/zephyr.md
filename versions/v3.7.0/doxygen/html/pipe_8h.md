---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/pipe_8h.html
original_path: doxygen/html/pipe_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pipe.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

[Go to the source code of this file.](pipe_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [modem\_pipe\_api\_callback](group__modem__pipe.md#gaf64941177c179cb9086a5736d1ea56f1)) (struct modem\_pipe \*pipe, enum [modem\_pipe\_event](group__modem__pipe.md#gab9dd98d92d6446dd43852d280574f67a) event, void \*user\_data) |

| Enumerations | |
| --- | --- |
| enum | [modem\_pipe\_event](group__modem__pipe.md#gab9dd98d92d6446dd43852d280574f67a) { [MODEM\_PIPE\_EVENT\_OPENED](group__modem__pipe.md#ggab9dd98d92d6446dd43852d280574f67aa68d9924c9fc58cf9ca8760573d32f891) = 0 , [MODEM\_PIPE\_EVENT\_RECEIVE\_READY](group__modem__pipe.md#ggab9dd98d92d6446dd43852d280574f67aa6687ded90e569690afc72020e78624c4) , [MODEM\_PIPE\_EVENT\_TRANSMIT\_IDLE](group__modem__pipe.md#ggab9dd98d92d6446dd43852d280574f67aaa6e11b11afb91ec50c4d0dfb363e7ad4) , [MODEM\_PIPE\_EVENT\_CLOSED](group__modem__pipe.md#ggab9dd98d92d6446dd43852d280574f67aae3ed9618f4986a7c3bef59e16a61316f) } |
|  | Modem pipe event. [More...](group__modem__pipe.md#gab9dd98d92d6446dd43852d280574f67a) |

| Functions | |
| --- | --- |
| int | [modem\_pipe\_open](group__modem__pipe.md#gad53acf3b0641bcc1779d85d5af6fb412) (struct modem\_pipe \*pipe) |
|  | Open pipe. |
| int | [modem\_pipe\_open\_async](group__modem__pipe.md#ga0a7312eadaa76b433fe8a319d8c9ec74) (struct modem\_pipe \*pipe) |
|  | Open pipe asynchronously. |
| void | [modem\_pipe\_attach](group__modem__pipe.md#ga68674becf672b1009d629813c041b868) (struct modem\_pipe \*pipe, [modem\_pipe\_api\_callback](group__modem__pipe.md#gaf64941177c179cb9086a5736d1ea56f1) callback, void \*user\_data) |
|  | Attach pipe to callback. |
| int | [modem\_pipe\_transmit](group__modem__pipe.md#ga72311fcb03f138d57e230af60340c9f6) (struct modem\_pipe \*pipe, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Transmit data through pipe. |
| int | [modem\_pipe\_receive](group__modem__pipe.md#gab030b4040725ad4dab2399840ef73fde) (struct modem\_pipe \*pipe, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Receive data through pipe. |
| void | [modem\_pipe\_release](group__modem__pipe.md#gad1a9fa3dba49a86c187328b7ee022293) (struct modem\_pipe \*pipe) |
|  | Clear callback. |
| int | [modem\_pipe\_close](group__modem__pipe.md#ga43d885be0f284cc580e66572b4bab065) (struct modem\_pipe \*pipe) |
|  | Close pipe. |
| int | [modem\_pipe\_close\_async](group__modem__pipe.md#ga9814c9a1a5da33b2787ac058a6a037f5) (struct modem\_pipe \*pipe) |
|  | Close pipe asynchronously. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [pipe.h](pipe_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/cmux_8h.html
original_path: doxygen/html/cmux_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cmux.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys/ring_buffer.h](ring__buffer_8h_source.md)>`  
`#include <[zephyr/sys/atomic.h](sys_2atomic_8h_source.md)>`  
`#include <[zephyr/modem/pipe.h](pipe_8h_source.md)>`  
`#include <[zephyr/modem/stats.h](modem_2stats_8h_source.md)>`

[Go to the source code of this file.](cmux_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [modem\_cmux\_config](structmodem__cmux__config.md) |
|  | Contains CMUX instance configuration data. [More...](structmodem__cmux__config.md#details) |
| struct | [modem\_cmux\_dlci\_config](structmodem__cmux__dlci__config.md) |
|  | CMUX DLCI configuration. [More...](structmodem__cmux__dlci__config.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [modem\_cmux\_callback](group__modem__cmux.md#ga998b334620c9970ebbb0bcf620ea5923)) (struct modem\_cmux \*cmux, enum [modem\_cmux\_event](group__modem__cmux.md#gab60ea756d37bd9ed59f07c6380952d36) event, void \*user\_data) |

| Enumerations | |
| --- | --- |
| enum | [modem\_cmux\_event](group__modem__cmux.md#gab60ea756d37bd9ed59f07c6380952d36) { [MODEM\_CMUX\_EVENT\_CONNECTED](group__modem__cmux.md#ggab60ea756d37bd9ed59f07c6380952d36a8d37518bf5ba31237e59a413f36be4b2) = 0 , [MODEM\_CMUX\_EVENT\_DISCONNECTED](group__modem__cmux.md#ggab60ea756d37bd9ed59f07c6380952d36a095af6ed667b014e4beb4c13c34c8a21) } |

| Functions | |
| --- | --- |
| void | [modem\_cmux\_init](group__modem__cmux.md#gad72973ad82504ae64d184ce11572ab88) (struct modem\_cmux \*cmux, const struct [modem\_cmux\_config](structmodem__cmux__config.md) \*config) |
|  | Initialize CMUX instance. |
| struct modem\_pipe \* | [modem\_cmux\_dlci\_init](group__modem__cmux.md#gabfd8e728eb8940b4093ae132b7add7d7) (struct modem\_cmux \*cmux, struct modem\_cmux\_dlci \*dlci, const struct [modem\_cmux\_dlci\_config](structmodem__cmux__dlci__config.md) \*config) |
|  | Initialize DLCI instance and register it with CMUX instance. |
| int | [modem\_cmux\_attach](group__modem__cmux.md#gab85f5c71a3cf131ff97aa47749197cb3) (struct modem\_cmux \*cmux, struct modem\_pipe \*pipe) |
|  | Attach CMUX instance to pipe. |
| int | [modem\_cmux\_connect](group__modem__cmux.md#ga362cd4b2dff122e3bbaee02b378dd226) (struct modem\_cmux \*cmux) |
|  | Connect CMUX instance. |
| int | [modem\_cmux\_connect\_async](group__modem__cmux.md#ga9fa4a1cd9cf1e1c253e621c650a611d0) (struct modem\_cmux \*cmux) |
|  | Connect CMUX instance asynchronously. |
| int | [modem\_cmux\_disconnect](group__modem__cmux.md#ga482171f67db206780d0b8a2cf5b32a93) (struct modem\_cmux \*cmux) |
|  | Close down and disconnect CMUX instance. |
| int | [modem\_cmux\_disconnect\_async](group__modem__cmux.md#ga988c8efbebf63871730918d862b7c490) (struct modem\_cmux \*cmux) |
|  | Close down and disconnect CMUX instance asynchronously. |
| void | [modem\_cmux\_release](group__modem__cmux.md#gadc7c6ff92b7ac52717151bd6bf1efdff) (struct modem\_cmux \*cmux) |
|  | Release CMUX instance from pipe. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [cmux.h](cmux_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ubx_8h.html
original_path: doxygen/html/ubx_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ubx.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys/atomic.h](sys_2atomic_8h_source.md)>`  
`#include <[zephyr/modem/pipe.h](pipe_8h_source.md)>`  
`#include <[zephyr/modem/ubx/protocol.h](modem_2ubx_2protocol_8h_source.md)>`

[Go to the source code of this file.](ubx_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [modem\_ubx\_match](structmodem__ubx__match.md) |
| struct | [modem\_ubx\_script](structmodem__ubx__script.md) |
| struct | [modem\_ubx](structmodem__ubx.md) |
| struct | [modem\_ubx\_config](structmodem__ubx__config.md) |

| Macros | |
| --- | --- |
| #define | [ZEPHYR\_MODEM\_UBX\_](#af3b5ad7b53c97ba7ec6a96d2b44f3c27) |
| #define | [MODEM\_UBX\_MATCH\_ARRAY\_DEFINE](group__modem__ubx.md#ga8a37614e3a9cf6d4773b9e74de79d340)(\_name, ...) |
| #define | [MODEM\_UBX\_MATCH\_DEFINE](group__modem__ubx.md#ga4c04f643a1ea9f0fc940d286713be30e)(\_class\_id, \_msg\_id, \_handler) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [modem\_ubx\_match\_callback](group__modem__ubx.md#gae0bfe22e7e8d7d38ae9f41648f7fcfda)) (struct [modem\_ubx](structmodem__ubx.md) \*ubx, const struct [ubx\_frame](structubx__frame.md) \*frame, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, void \*user\_data) |

| Functions | |
| --- | --- |
| int | [modem\_ubx\_attach](group__modem__ubx.md#ga4e459f955e34c9059702c3d7f9794948) (struct [modem\_ubx](structmodem__ubx.md) \*ubx, struct modem\_pipe \*pipe) |
|  | Attach pipe to Modem Ubx. |
| void | [modem\_ubx\_release](group__modem__ubx.md#ga68210f4afd5880c532d82fd0bac1d933) (struct [modem\_ubx](structmodem__ubx.md) \*ubx) |
|  | Release pipe from Modem Ubx instance. |
| int | [modem\_ubx\_init](group__modem__ubx.md#gaf49363fb4decb4656566b508a061212f) (struct [modem\_ubx](structmodem__ubx.md) \*ubx, const struct [modem\_ubx\_config](structmodem__ubx__config.md) \*config) |
|  | Initialize Modem Ubx instance. |
| int | [modem\_ubx\_run\_script](group__modem__ubx.md#ga770650b055fd597f000a1d4f9daaf712) (struct [modem\_ubx](structmodem__ubx.md) \*ubx, struct [modem\_ubx\_script](structmodem__ubx__script.md) \*script) |
|  | Writes the ubx frame in script.request and reads back its response (if available). |
| int | [modem\_ubx\_run\_script\_for\_each](group__modem__ubx.md#ga0fd0def90f6304e679c4123e3c8d0c3f) (struct [modem\_ubx](structmodem__ubx.md) \*ubx, struct [modem\_ubx\_script](structmodem__ubx__script.md) \*script, struct [ubx\_frame](structubx__frame.md) \*array, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) array\_size) |

## Macro Definition Documentation

## [◆ ](#af3b5ad7b53c97ba7ec6a96d2b44f3c27)ZEPHYR\_MODEM\_UBX\_

| #define ZEPHYR\_MODEM\_UBX\_ |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [ubx.h](ubx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

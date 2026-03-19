---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/pipelink_8h.html
original_path: doxygen/html/pipelink_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pipelink.h File Reference

`#include <[zephyr/modem/pipe.h](pipe_8h_source.md)>`  
`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`

[Go to the source code of this file.](pipelink_8h_source.md)

| Macros | |
| --- | --- |
| #define | [MODEM\_PIPELINK\_DT\_DECLARE](group__modem__pipelink.md#ga46d06461a5a465f4a73c135f721e3aa5)(node\_id, name) |
|  | Declare pipelink from devicetree node identifier and name. |
| #define | [MODEM\_PIPELINK\_DT\_DEFINE](group__modem__pipelink.md#gac1010375931a7a5076d066e2c5ed9a14)(node\_id, name) |
|  | Define pipelink from devicetree node identifier and name. |
| #define | [MODEM\_PIPELINK\_DT\_GET](group__modem__pipelink.md#gada75e5995e78c8c8daa5a16f5e5abb4a)(node\_id, name) |
|  | Get pointer to pipelink from devicetree node identifier and name. |
| MODEM\_PIPELINK\_DT\_INST macros | |
| Device driver instance variants of MODEM\_PIPELINK\_DT macros | |
| #define | [MODEM\_PIPELINK\_DT\_INST\_DECLARE](group__modem__pipelink.md#gaedc5b4665d541fe4d471a287177e6674)(inst, name) |
| #define | [MODEM\_PIPELINK\_DT\_INST\_DEFINE](group__modem__pipelink.md#ga1ca071affbb19bfac4c2ef7f25bf9c65)(inst, name) |
| #define | [MODEM\_PIPELINK\_DT\_INST\_GET](group__modem__pipelink.md#ga1c3a0ff1f1939e12fdefee85a7f5eeed)(inst, name) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [modem\_pipelink\_callback](group__modem__pipelink.md#ga4f93732f1df6cab41cc352526d6a849e)) (struct modem\_pipelink \*link, enum [modem\_pipelink\_event](group__modem__pipelink.md#ga399168cacd287e376df68c4cf221ba00) event, void \*user\_data) |
|  | Pipelink callback definition. |

| Enumerations | |
| --- | --- |
| enum | [modem\_pipelink\_event](group__modem__pipelink.md#ga399168cacd287e376df68c4cf221ba00) { [MODEM\_PIPELINK\_EVENT\_CONNECTED](group__modem__pipelink.md#gga399168cacd287e376df68c4cf221ba00ab1a51a16b5dbe02ebca8fb0efe4be81f) = 0 , [MODEM\_PIPELINK\_EVENT\_DISCONNECTED](group__modem__pipelink.md#gga399168cacd287e376df68c4cf221ba00ae118b022efcba2033701dfb8f2e7d38d) } |
|  | Pipelink event. [More...](group__modem__pipelink.md#ga399168cacd287e376df68c4cf221ba00) |

| Functions | |
| --- | --- |
| void | [modem\_pipelink\_attach](group__modem__pipelink.md#ga7ee7b3454a9fe94c20855a893dd2b2a1) (struct modem\_pipelink \*link, [modem\_pipelink\_callback](group__modem__pipelink.md#ga4f93732f1df6cab41cc352526d6a849e) callback, void \*user\_data) |
|  | Attach callback to pipelink. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [modem\_pipelink\_is\_connected](group__modem__pipelink.md#ga7c7638ad3f22533f374e002b787b11ce) (struct modem\_pipelink \*link) |
|  | Check whether pipelink pipe is connected. |
| struct modem\_pipe \* | [modem\_pipelink\_get\_pipe](group__modem__pipelink.md#gab09d76f7bd93a19b82a7d5e818b80d80) (struct modem\_pipelink \*link) |
|  | Get pipe from pipelink. |
| void | [modem\_pipelink\_release](group__modem__pipelink.md#ga684ff47ddb0e0487022cea62052b32e2) (struct modem\_pipelink \*link) |
|  | Clear callback. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [pipelink.h](pipelink_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

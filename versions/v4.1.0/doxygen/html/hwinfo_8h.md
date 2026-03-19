---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/hwinfo_8h.html
original_path: doxygen/html/hwinfo_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hwinfo.h File Reference

Public APIs to get device Information.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <zephyr/syscalls/hwinfo.h>`

[Go to the source code of this file.](hwinfo_8h_source.md)

| Macros | |
| --- | --- |
| Reset cause flags | |
|  | |
| #define | [RESET\_PIN](group__hwinfo__interface.md#ga08bca59db4b190eaaea4d47b7562869c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | External pin. |
| #define | [RESET\_SOFTWARE](group__hwinfo__interface.md#ga737ea2c652086e38a9b895cc42593908)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Software reset. |
| #define | [RESET\_BROWNOUT](group__hwinfo__interface.md#gac9dc9b22ba1fc551a3d68810155a640e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Brownout (drop in voltage). |
| #define | [RESET\_POR](group__hwinfo__interface.md#ga21fa7b8a5ec2e1c077dbc453ca3a4265)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Power-on reset (POR). |
| #define | [RESET\_WATCHDOG](group__hwinfo__interface.md#ga112ab452e5015120edcb88b9a6de3de0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Watchdog timer expiration. |
| #define | [RESET\_DEBUG](group__hwinfo__interface.md#ga031454a8ff535f8cf66ddbdbc2acba5e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Debug event. |
| #define | [RESET\_SECURITY](group__hwinfo__interface.md#ga846cce95f808d3c1a5b48376f8de3612)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Security violation. |
| #define | [RESET\_LOW\_POWER\_WAKE](group__hwinfo__interface.md#ga3ce47e00b35b155416a3d48dd5c477ac)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Waking up from low power mode. |
| #define | [RESET\_CPU\_LOCKUP](group__hwinfo__interface.md#gad6721dc841941ccdca349999ce655e83)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
|  | CPU lock-up detected. |
| #define | [RESET\_PARITY](group__hwinfo__interface.md#gac32af4272b5356a498cb3d4ce6fb87e7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
|  | Parity error. |
| #define | [RESET\_PLL](group__hwinfo__interface.md#gaed16942e0487d525c79c539b385e6f31)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
|  | PLL error. |
| #define | [RESET\_CLOCK](group__hwinfo__interface.md#ga9bb4063cded0167c496b834d642fd73c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
|  | Clock error. |
| #define | [RESET\_HARDWARE](group__hwinfo__interface.md#gaf9659a85b05447ef9267606182bf568a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
|  | Hardware reset. |
| #define | [RESET\_USER](group__hwinfo__interface.md#ga5aa032c5d8560a4bb351ca29d1464939)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
|  | User reset. |
| #define | [RESET\_TEMPERATURE](group__hwinfo__interface.md#gade167088d6c99163f5af385bcac93f58)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
|  | Temperature reset. |

| Functions | |
| --- | --- |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [hwinfo\_get\_device\_id](group__hwinfo__interface.md#ga197b58d995c77aae423527d0f8d9ff31) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Copy the device id to a buffer. |
| int | [hwinfo\_get\_device\_eui64](group__hwinfo__interface.md#ga0f5ab222b4f7e75a3e9d3650e954a036) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer) |
|  | Copy the device EUI64 to a buffer. |
| int | [hwinfo\_get\_reset\_cause](group__hwinfo__interface.md#ga390c1c29088813ace17856ffa97d97b5) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*cause) |
|  | Retrieve cause of device reset. |
| int | [hwinfo\_clear\_reset\_cause](group__hwinfo__interface.md#gaeaa23e68c53eb6a2b56f06c74b83e613) (void) |
|  | Clear cause of device reset. |
| int | [hwinfo\_get\_supported\_reset\_cause](group__hwinfo__interface.md#gaf0d345653c4fbb5f38a78aba766a6bb8) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*supported) |
|  | Get supported reset cause flags. |

## Detailed Description

Public APIs to get device Information.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [hwinfo.h](hwinfo_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/os__mgmt__client_8h.html
original_path: doxygen/html/os__mgmt__client_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

os\_mgmt\_client.h File Reference

`#include <[inttypes.h](inttypes_8h_source.md)>`  
`#include <[zephyr/mgmt/mcumgr/smp/smp_client.h](smp__client_8h_source.md)>`

[Go to the source code of this file.](os__mgmt__client_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [os\_mgmt\_client](structos__mgmt__client.md) |
|  | OS mgmt client object. [More...](structos__mgmt__client.md#details) |

| Functions | |
| --- | --- |
| void | [os\_mgmt\_client\_init](group__mcumgr__os__mgmt__client.md#gafab4d3da30fa2bf855110d541b8fee08) (struct [os\_mgmt\_client](structos__mgmt__client.md) \*client, struct [smp\_client\_object](structsmp__client__object.md) \*smp\_client) |
|  | Initialize OS management client. |
| int | [os\_mgmt\_client\_echo](group__mcumgr__os__mgmt__client.md#ga2dd2edb7c3952413c361b3d38dc2eaad) (struct [os\_mgmt\_client](structos__mgmt__client.md) \*client, const char \*echo\_string, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) max\_len) |
|  | Send SMP message for Echo command. |
| int | [os\_mgmt\_client\_reset](group__mcumgr__os__mgmt__client.md#ga5cb153bf30c40e82e8f55ac18a45fa09) (struct [os\_mgmt\_client](structos__mgmt__client.md) \*client) |
|  | Send SMP Reset command. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [os\_mgmt](dir_1a5ff9dfdb0e06a8ce3ba8e3db8b26fb.md)
- [os\_mgmt\_client.h](os__mgmt__client_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

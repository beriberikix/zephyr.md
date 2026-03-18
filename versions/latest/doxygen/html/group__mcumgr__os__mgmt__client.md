---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__mcumgr__os__mgmt__client.html
original_path: doxygen/html/group__mcumgr__os__mgmt__client.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MCUmgr os\_mgmt\_client API

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md)

MCUmgr OS management client API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [os\_mgmt\_client](structos__mgmt__client.md) |
|  | OS mgmt client object. [More...](structos__mgmt__client.md#details) |

| Functions | |
| --- | --- |
| void | [os\_mgmt\_client\_init](#gafab4d3da30fa2bf855110d541b8fee08) (struct [os\_mgmt\_client](structos__mgmt__client.md) \*client, struct [smp\_client\_object](structsmp__client__object.md) \*smp\_client) |
|  | Initialize OS management client. |
| int | [os\_mgmt\_client\_echo](#ga2dd2edb7c3952413c361b3d38dc2eaad) (struct [os\_mgmt\_client](structos__mgmt__client.md) \*client, const char \*echo\_string, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) max\_len) |
|  | Send SMP message for Echo command. |
| int | [os\_mgmt\_client\_reset](#ga5cb153bf30c40e82e8f55ac18a45fa09) (struct [os\_mgmt\_client](structos__mgmt__client.md) \*client) |
|  | Send SMP Reset command. |

## Detailed Description

MCUmgr OS management client API.

## Function Documentation

## [◆ ](#ga2dd2edb7c3952413c361b3d38dc2eaad)os\_mgmt\_client\_echo()

| int os\_mgmt\_client\_echo | ( | struct [os\_mgmt\_client](structos__mgmt__client.md) \* | *client*, |
| --- | --- | --- | --- |
|  |  | const char \* | *echo\_string*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *max\_len* ) |

`#include <[os_mgmt_client.h](os__mgmt__client_8h.md)>`

Send SMP message for Echo command.

Parameters
:   | client | OS mgmt client object |
    | --- | --- |
    | echo\_string | Echo string |
    | max\_len | Max length of `echo_string` |

Returns
:   0 on success.
:   [mcumgr\_err\_t](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5 "mcumgr_err_t") code on failure.

## [◆ ](#gafab4d3da30fa2bf855110d541b8fee08)os\_mgmt\_client\_init()

| void os\_mgmt\_client\_init | ( | struct [os\_mgmt\_client](structos__mgmt__client.md) \* | *client*, |
| --- | --- | --- | --- |
|  |  | struct [smp\_client\_object](structsmp__client__object.md) \* | *smp\_client* ) |

`#include <[os_mgmt_client.h](os__mgmt__client_8h.md)>`

Initialize OS management client.

Parameters
:   | client | OS mgmt client object |
    | --- | --- |
    | smp\_client | SMP client object |

## [◆ ](#ga5cb153bf30c40e82e8f55ac18a45fa09)os\_mgmt\_client\_reset()

| int os\_mgmt\_client\_reset | ( | struct [os\_mgmt\_client](structos__mgmt__client.md) \* | *client* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[os_mgmt_client.h](os__mgmt__client_8h.md)>`

Send SMP Reset command.

Parameters
:   | client | OS mgmt client object |
    | --- | --- |

Returns
:   0 on success.
:   [mcumgr\_err\_t](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5 "mcumgr_err_t") code on failure.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

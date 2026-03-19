---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__mcumgr__smp__client.html
original_path: doxygen/html/group__mcumgr__smp__client.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

SMP client API

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md)

MCUmgr SMP client API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [smp\_client\_object](structsmp__client__object.md) |
|  | SMP client object. [More...](structsmp__client__object.md#details) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [smp\_client\_res\_fn](#gae7974bf0e951403f6dfe8b33a2547acc)) (struct [net\_buf](structnet__buf.md) \*nb, void \*user\_data) |
|  | Response callback for SMP send. |

| Functions | |
| --- | --- |
| int | [smp\_client\_object\_init](#ga07f36d0ac230d158c2959e8010444e47) (struct [smp\_client\_object](structsmp__client__object.md) \*smp\_client, int smp\_type) |
|  | Initialize a SMP client object. |
| int | [smp\_client\_single\_response](#ga42022a3ea929da134644996c4414cfce) (struct [net\_buf](structnet__buf.md) \*nb, const struct smp\_hdr \*res\_hdr) |
|  | SMP client response handler. |
| struct [net\_buf](structnet__buf.md) \* | [smp\_client\_buf\_allocation](#ga57ec028fc6bcb3591298815b1d9b8a3b) (struct [smp\_client\_object](structsmp__client__object.md) \*smp\_client, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [group](structgroup.md), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) command\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) op, enum [smp\_mcumgr\_version\_t](mgmt_2mcumgr_2smp_2smp_8h.md#aa05d01653e39ef61a93f33319c9a00ed) version) |
|  | Allocate buffer and initialize with SMP header. |
| void | [smp\_client\_buf\_free](#gace302f95e5f45076db72fbecf190f0f5) (struct [net\_buf](structnet__buf.md) \*nb) |
|  | Free a SMP client buffer. |
| int | [smp\_client\_send\_cmd](#gaeb20d13ddf14ddb924b0a84a014abda5) (struct [smp\_client\_object](structsmp__client__object.md) \*smp\_client, struct [net\_buf](structnet__buf.md) \*nb, [smp\_client\_res\_fn](#gae7974bf0e951403f6dfe8b33a2547acc) cb, void \*user\_data, int timeout\_in\_sec) |
|  | SMP client data send request. |

## Detailed Description

MCUmgr SMP client API.

## Typedef Documentation

## [◆ ](#gae7974bf0e951403f6dfe8b33a2547acc)smp\_client\_res\_fn

| typedef int(\* smp\_client\_res\_fn) (struct [net\_buf](structnet__buf.md) \*nb, void \*user\_data) |
| --- |

`#include <[smp_client.h](smp__client_8h.md)>`

Response callback for SMP send.

Parameters
:   | nb | [net\_buf](structnet__buf.md "Network buffer representation.") for response |
    | --- | --- |
    | user\_data | same user data that was provided as part of the request |

Returns
:   0 on success.
:   [mcumgr\_err\_t](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5 "mcumgr_err_t") code on failure.

## Function Documentation

## [◆ ](#ga57ec028fc6bcb3591298815b1d9b8a3b)smp\_client\_buf\_allocation()

| struct [net\_buf](structnet__buf.md) \* smp\_client\_buf\_allocation | ( | struct [smp\_client\_object](structsmp__client__object.md) \* | *smp\_client*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *group*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *command\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *op*, |
|  |  | enum [smp\_mcumgr\_version\_t](mgmt_2mcumgr_2smp_2smp_8h.md#aa05d01653e39ef61a93f33319c9a00ed) | *version* ) |

`#include <[smp_client.h](smp__client_8h.md)>`

Allocate buffer and initialize with SMP header.

Parameters
:   | smp\_client | SMP client object |
    | --- | --- |
    | [group](structgroup.md "Group structure.") | SMP group id |
    | command\_id | SMP command id |
    | op | SMP operation type |
    | version | SMP MCUmgr version |

Returns
:   A newly-allocated buffer [net\_buf](structnet__buf.md "Network buffer representation.") on success
:   NULL on failure.

## [◆ ](#gace302f95e5f45076db72fbecf190f0f5)smp\_client\_buf\_free()

| void smp\_client\_buf\_free | ( | struct [net\_buf](structnet__buf.md) \* | *nb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[smp_client.h](smp__client_8h.md)>`

Free a SMP client buffer.

Parameters
:   | nb | The [net\_buf](structnet__buf.md "Network buffer representation.") to free. |
    | --- | --- |

## [◆ ](#ga07f36d0ac230d158c2959e8010444e47)smp\_client\_object\_init()

| int smp\_client\_object\_init | ( | struct [smp\_client\_object](structsmp__client__object.md) \* | *smp\_client*, |
| --- | --- | --- | --- |
|  |  | int | *smp\_type* ) |

`#include <[smp_client.h](smp__client_8h.md)>`

Initialize a SMP client object.

Parameters
:   | smp\_client | The Client to construct. |
    | --- | --- |
    | smp\_type | SMP transport type for discovering transport object |

Returns
:   0 if successful
:   [mcumgr\_err\_t](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5 "MCUmgr error codes.") code on failure

## [◆ ](#gaeb20d13ddf14ddb924b0a84a014abda5)smp\_client\_send\_cmd()

| int smp\_client\_send\_cmd | ( | struct [smp\_client\_object](structsmp__client__object.md) \* | *smp\_client*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \* | *nb*, |
|  |  | [smp\_client\_res\_fn](#gae7974bf0e951403f6dfe8b33a2547acc) | *cb*, |
|  |  | void \* | *user\_data*, |
|  |  | int | *timeout\_in\_sec* ) |

`#include <[smp_client.h](smp__client_8h.md)>`

SMP client data send request.

Parameters
:   | smp\_client | SMP client object |
    | --- | --- |
    | nb | [net\_buf](structnet__buf.md "Network buffer representation.") packet for send |
    | cb | Callback for response handler |
    | user\_data | user defined data pointer which will be returned back to response callback |
    | timeout\_in\_sec | Timeout in seconds for send process. Client will retry transport based CONFIG\_SMP\_CMD\_RETRY\_TIME |

Returns
:   0 on success.
:   [mcumgr\_err\_t](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5 "mcumgr_err_t") code on failure.

## [◆ ](#ga42022a3ea929da134644996c4414cfce)smp\_client\_single\_response()

| int smp\_client\_single\_response | ( | struct [net\_buf](structnet__buf.md) \* | *nb*, |
| --- | --- | --- | --- |
|  |  | const struct smp\_hdr \* | *res\_hdr* ) |

`#include <[smp_client.h](smp__client_8h.md)>`

SMP client response handler.

Parameters
:   | nb | response [net\_buf](structnet__buf.md "Network buffer representation.") |
    | --- | --- |
    | res\_hdr | Parsed SMP header |

Returns
:   0 on success.
:   [mcumgr\_err\_t](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5 "mcumgr_err_t") code on failure.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__sink__callbacks.html
original_path: doxygen/html/group__sink__callbacks.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Sink\_callbacks

[USB-C Device API](group____usbc__device__api.md)

| Typedefs | |
| --- | --- |
| typedef int(\* | [policy\_cb\_get\_snk\_cap\_t](#gaaed0161142c3481ce9180015b6968357)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*\*pdos, int \*num\_pdos) |
|  | Callback type used to get the Sink Capabilities. |
| typedef void(\* | [policy\_cb\_set\_src\_cap\_t](#ga6096d6909698f1b86a1a9cbd1f8d4097)) (const struct [device](structdevice.md) \*dev, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*pdos, const int num\_pdos) |
|  | Callback type used to report the received Port Partner's Source Capabilities. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [policy\_cb\_check\_t](#ga2aacd704d08a8cecbf818150e8ec51b6)) (const struct [device](structdevice.md) \*dev, const enum [usbc\_policy\_check\_t](group____usbc__device__api.md#gafea882f4f3cc96c502d53a24a3e5aec5) policy\_check) |
|  | Callback type used to check a policy. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [policy\_cb\_wait\_notify\_t](#gaea62016b263dfaf5f869dd6ea036fdad)) (const struct [device](structdevice.md) \*dev, const enum [usbc\_policy\_wait\_t](group____usbc__device__api.md#gadf5d2934b5dc8e2b01d20bb904988784) wait\_notify) |
|  | Callback type used to notify Device Policy Manager of WAIT message reception. |
| typedef void(\* | [policy\_cb\_notify\_t](#ga44af668d9c22e757983c803d7b8ff82e)) (const struct [device](structdevice.md) \*dev, const enum [usbc\_policy\_notify\_t](group____usbc__device__api.md#ga66f934a5c5cd88b574c71d1f18fbda23) policy\_notify) |
|  | Callback type used to notify Device Policy Manager of a policy change. |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [policy\_cb\_get\_rdo\_t](#gae0448c6b271273c5db59775c3a6260dc)) (const struct [device](structdevice.md) \*dev) |
|  | Callback type used to get the Request Data Object (RDO). |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [policy\_cb\_is\_snk\_at\_default\_t](#ga1a3da6faad509213f607893fef16b673)) (const struct [device](structdevice.md) \*dev) |
|  | Callback type used to check if the sink power supply is at the default level. |

## Detailed Description

## Typedef Documentation

## [◆ ](#ga2aacd704d08a8cecbf818150e8ec51b6)policy\_cb\_check\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* policy\_cb\_check\_t) (const struct [device](structdevice.md) \*dev, const enum [usbc\_policy\_check\_t](group____usbc__device__api.md#gafea882f4f3cc96c502d53a24a3e5aec5) policy\_check) |
| --- |

`#include <[usbc.h](usbc_8h.md)>`

Callback type used to check a policy.

Parameters
:   | dev | USB-C Connector Instance |
    | --- | --- |
    | policy\_check | policy to check |

Returns
:   true if policy is currently allowed by the device policy manager

## [◆ ](#gae0448c6b271273c5db59775c3a6260dc)policy\_cb\_get\_rdo\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* policy\_cb\_get\_rdo\_t) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[usbc.h](usbc_8h.md)>`

Callback type used to get the Request Data Object (RDO).

Parameters
:   | dev | USB-C Connector Instance |
    | --- | --- |

Returns
:   RDO

## [◆ ](#gaaed0161142c3481ce9180015b6968357)policy\_cb\_get\_snk\_cap\_t

| typedef int(\* policy\_cb\_get\_snk\_cap\_t) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*\*pdos, int \*num\_pdos) |
| --- |

`#include <[usbc.h](usbc_8h.md)>`

Callback type used to get the Sink Capabilities.

Parameters
:   | dev | USB-C Connector Instance |
    | --- | --- |
    | pdos | pointer where pdos are stored |
    | num\_pdos | pointer where number of pdos is stored |

Returns
:   0 on success

## [◆ ](#ga1a3da6faad509213f607893fef16b673)policy\_cb\_is\_snk\_at\_default\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* policy\_cb\_is\_snk\_at\_default\_t) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[usbc.h](usbc_8h.md)>`

Callback type used to check if the sink power supply is at the default level.

Parameters
:   | dev | USB-C Connector Instance |
    | --- | --- |

Returns
:   true if power supply is at default level

## [◆ ](#ga44af668d9c22e757983c803d7b8ff82e)policy\_cb\_notify\_t

| typedef void(\* policy\_cb\_notify\_t) (const struct [device](structdevice.md) \*dev, const enum [usbc\_policy\_notify\_t](group____usbc__device__api.md#ga66f934a5c5cd88b574c71d1f18fbda23) policy\_notify) |
| --- |

`#include <[usbc.h](usbc_8h.md)>`

Callback type used to notify Device Policy Manager of a policy change.

Parameters
:   | dev | USB-C Connector Instance |
    | --- | --- |
    | policy\_notify | policy notification |

## [◆ ](#ga6096d6909698f1b86a1a9cbd1f8d4097)policy\_cb\_set\_src\_cap\_t

| typedef void(\* policy\_cb\_set\_src\_cap\_t) (const struct [device](structdevice.md) \*dev, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*pdos, const int num\_pdos) |
| --- |

`#include <[usbc.h](usbc_8h.md)>`

Callback type used to report the received Port Partner's Source Capabilities.

Parameters
:   | dev | USB-C Connector Instance |
    | --- | --- |
    | pdos | pointer to the partner's source pdos |
    | num\_pdos | number of source pdos |

## [◆ ](#gaea62016b263dfaf5f869dd6ea036fdad)policy\_cb\_wait\_notify\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* policy\_cb\_wait\_notify\_t) (const struct [device](structdevice.md) \*dev, const enum [usbc\_policy\_wait\_t](group____usbc__device__api.md#gadf5d2934b5dc8e2b01d20bb904988784) wait\_notify) |
| --- |

`#include <[usbc.h](usbc_8h.md)>`

Callback type used to notify Device Policy Manager of WAIT message reception.

Parameters
:   | dev | USB-C Connector Instance |
    | --- | --- |
    | wait\_notify | wait notification |

Returns
:   return true if the PE should wait and resend the message

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

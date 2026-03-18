---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__mesh__cfg__cli__hb__sub.html
original_path: doxygen/html/structbt__mesh__cfg__cli__hb__sub.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_cfg\_cli\_hb\_sub Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Configuration Client Model](group__bt__mesh__cfg__cli.md)

Heartbeat subscription configuration parameters.
[More...](#details)

`#include <[cfg_cli.h](cfg__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [src](#a01ec0c3cab7bb7ed76d7728390eb4f25) |
|  | Source address to receive Heartbeat messages from. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [dst](#abc9ea18fbe86c260d6cf5d53c26a0248) |
|  | Destination address to receive Heartbeat messages on. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [period](#a5a75c924f0868c664652503335b1b012) |
|  | Logarithmic subscription period to keep listening for. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [count](#a93624ab6c8a0c15c0b50490e0fcd3675) |
|  | Logarithmic Heartbeat subscription receive count. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [min](#a480b214e0e1974a6a54426c49e5d62d1) |
|  | Minimum hops in received messages, ie the shortest registered path from the publishing node to the subscribing node. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [max](#aac96c2ab606e38f412e94539795c5594) |
|  | Maximum hops in received messages, ie the longest registered path from the publishing node to the subscribing node. |

## Detailed Description

Heartbeat subscription configuration parameters.

## Field Documentation

## [◆ ](#a93624ab6c8a0c15c0b50490e0fcd3675)count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_cfg\_cli\_hb\_sub::count |
| --- |

Logarithmic Heartbeat subscription receive count.

The decoded Heartbeat count is (1 << (count - 1)) if count is between 1 and 0xfe, 0 if count is 0 and 0xffff if count is 0xff.

Ignored in Heartbeat subscription set.

## [◆ ](#abc9ea18fbe86c260d6cf5d53c26a0248)dst

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_cfg\_cli\_hb\_sub::dst |
| --- |

Destination address to receive Heartbeat messages on.

## [◆ ](#aac96c2ab606e38f412e94539795c5594)max

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_cfg\_cli\_hb\_sub::max |
| --- |

Maximum hops in received messages, ie the longest registered path from the publishing node to the subscribing node.

A Heartbeat received from an immediate neighbor has hop count = 1.

Ignored in Heartbeat subscription set.

## [◆ ](#a480b214e0e1974a6a54426c49e5d62d1)min

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_cfg\_cli\_hb\_sub::min |
| --- |

Minimum hops in received messages, ie the shortest registered path from the publishing node to the subscribing node.

A Heartbeat received from an immediate neighbor has hop count = 1.

Ignored in Heartbeat subscription set.

## [◆ ](#a5a75c924f0868c664652503335b1b012)period

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_cfg\_cli\_hb\_sub::period |
| --- |

Logarithmic subscription period to keep listening for.

The decoded subscription period is (1 << (period - 1)) seconds, or 0 seconds if period is 0.

## [◆ ](#a01ec0c3cab7bb7ed76d7728390eb4f25)src

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_cfg\_cli\_hb\_sub::src |
| --- |

Source address to receive Heartbeat messages from.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[cfg\_cli.h](cfg__cli_8h_source.md)

- [bt\_mesh\_cfg\_cli\_hb\_sub](structbt__mesh__cfg__cli__hb__sub.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

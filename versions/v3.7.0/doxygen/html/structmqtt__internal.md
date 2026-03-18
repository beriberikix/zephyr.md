---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structmqtt__internal.html
original_path: doxygen/html/structmqtt__internal.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_internal Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT Client library](group__mqtt__socket.md)

MQTT internal state.
[More...](#details)

`#include <[mqtt.h](mqtt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [sys\_mutex](structsys__mutex.md) | [mutex](#af866a252b9e18496c8e1627704d8a8b2) |
|  | Internal. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [last\_activity](#a8f30cb1440efecf8ae8fc448e4f462f8) |
|  | Internal. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [state](#acf93a973de5a5430e767e2996f1cd048) |
|  | Internal. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rx\_buf\_datalen](#a45aeafd71dadaf1d0fd0bc3969c921de) |
|  | Internal. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [remaining\_payload](#a921477a9839447f4fe1c823911680c92) |
|  | Internal. |

## Detailed Description

MQTT internal state.

## Field Documentation

## [◆ ](#a8f30cb1440efecf8ae8fc448e4f462f8)last\_activity

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mqtt\_internal::last\_activity |
| --- |

Internal.

Wall clock value (in milliseconds) of the last activity that occurred. Needed for periodic PING.

## [◆ ](#af866a252b9e18496c8e1627704d8a8b2)mutex

| struct [sys\_mutex](structsys__mutex.md) mqtt\_internal::mutex |
| --- |

Internal.

Mutex to protect access to the client instance.

## [◆ ](#a921477a9839447f4fe1c823911680c92)remaining\_payload

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mqtt\_internal::remaining\_payload |
| --- |

Internal.

Remaining payload length to read.

## [◆ ](#a45aeafd71dadaf1d0fd0bc3969c921de)rx\_buf\_datalen

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mqtt\_internal::rx\_buf\_datalen |
| --- |

Internal.

Packet length read so far.

## [◆ ](#acf93a973de5a5430e767e2996f1cd048)state

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mqtt\_internal::state |
| --- |

Internal.

Client's state in the connection.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[mqtt.h](mqtt_8h_source.md)

- [mqtt\_internal](structmqtt__internal.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

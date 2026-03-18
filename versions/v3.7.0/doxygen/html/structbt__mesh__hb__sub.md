---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__mesh__hb__sub.html
original_path: doxygen/html/structbt__mesh__hb__sub.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_hb\_sub Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Heartbeat](group__bt__mesh__heartbeat.md)

Heartbeat Subscription parameters.
[More...](#details)

`#include <[heartbeat.h](heartbeat_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [period](#af7b20a7337c31110b1ae38c7eacc071a) |
|  | Subscription period in seconds. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [remaining](#ad66fd08eb09d475bef9c290fa7ae0a90) |
|  | Remaining subscription time in seconds. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [src](#afb9fba6c32257690539dd621e215708b) |
|  | Source address to receive Heartbeats from. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [dst](#ab10708af9ddfd7a80c370d40d2146a8b) |
|  | Destination address to received Heartbeats on. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [count](#a41dd595eb6a0c980c49f84aca11b3ac2) |
|  | The number of received Heartbeat messages so far. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [min\_hops](#aae4eb4e77166dfb49a7341ae8fcb9e6e) |
|  | Minimum hops in received messages, ie the shortest registered path from the publishing node to the subscribing node. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [max\_hops](#a38252818d3a2e136e5dfc9bda847d0b0) |
|  | Maximum hops in received messages, ie the longest registered path from the publishing node to the subscribing node. |

## Detailed Description

Heartbeat Subscription parameters.

## Field Documentation

## [◆ ](#a41dd595eb6a0c980c49f84aca11b3ac2)count

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_hb\_sub::count |
| --- |

The number of received Heartbeat messages so far.

## [◆ ](#ab10708af9ddfd7a80c370d40d2146a8b)dst

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_hb\_sub::dst |
| --- |

Destination address to received Heartbeats on.

## [◆ ](#a38252818d3a2e136e5dfc9bda847d0b0)max\_hops

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_hb\_sub::max\_hops |
| --- |

Maximum hops in received messages, ie the longest registered path from the publishing node to the subscribing node.

A Heartbeat received from an immediate neighbor has hop count = 1.

## [◆ ](#aae4eb4e77166dfb49a7341ae8fcb9e6e)min\_hops

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_hb\_sub::min\_hops |
| --- |

Minimum hops in received messages, ie the shortest registered path from the publishing node to the subscribing node.

A Heartbeat received from an immediate neighbor has hop count = 1.

## [◆ ](#af7b20a7337c31110b1ae38c7eacc071a)period

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_mesh\_hb\_sub::period |
| --- |

Subscription period in seconds.

## [◆ ](#ad66fd08eb09d475bef9c290fa7ae0a90)remaining

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_mesh\_hb\_sub::remaining |
| --- |

Remaining subscription time in seconds.

## [◆ ](#afb9fba6c32257690539dd621e215708b)src

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_hb\_sub::src |
| --- |

Source address to receive Heartbeats from.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[heartbeat.h](heartbeat_8h_source.md)

- [bt\_mesh\_hb\_sub](structbt__mesh__hb__sub.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

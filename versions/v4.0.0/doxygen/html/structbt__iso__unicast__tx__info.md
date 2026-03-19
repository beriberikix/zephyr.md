---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__iso__unicast__tx__info.html
original_path: doxygen/html/structbt__iso__unicast__tx__info.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_iso\_unicast\_tx\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Isochronous channels (ISO)](group__bt__iso.md)

ISO Unicast TX Info Structure.
[More...](#details)

`#include <[iso.h](iso_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [latency](#a14548ee24fad8a26287aa0daba451a47) |
|  | The transport latency in us. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flush\_timeout](#aaf1f623eac2f84ca06082776179b71c5) |
|  | The flush timeout (N \* 1.25 ms). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [max\_pdu](#afe7dce9255613e5e2939d3719c720822) |
|  | The maximum PDU size in octets. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [phy](#a3134e0bdb663ad7184e23531504233a5) |
|  | The transport PHY. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bn](#ab4ea9d5bb535d29ae9406e948d8707a9) |
|  | The burst number. |

## Detailed Description

ISO Unicast TX Info Structure.

## Field Documentation

## [◆ ](#ab4ea9d5bb535d29ae9406e948d8707a9)bn

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_unicast\_tx\_info::bn |
| --- |

The burst number.

## [◆ ](#aaf1f623eac2f84ca06082776179b71c5)flush\_timeout

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_iso\_unicast\_tx\_info::flush\_timeout |
| --- |

The flush timeout (N \* 1.25 ms).

## [◆ ](#a14548ee24fad8a26287aa0daba451a47)latency

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_iso\_unicast\_tx\_info::latency |
| --- |

The transport latency in us.

## [◆ ](#afe7dce9255613e5e2939d3719c720822)max\_pdu

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_iso\_unicast\_tx\_info::max\_pdu |
| --- |

The maximum PDU size in octets.

## [◆ ](#a3134e0bdb663ad7184e23531504233a5)phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_unicast\_tx\_info::phy |
| --- |

The transport PHY.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[iso.h](iso_8h_source.md)

- [bt\_iso\_unicast\_tx\_info](structbt__iso__unicast__tx__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

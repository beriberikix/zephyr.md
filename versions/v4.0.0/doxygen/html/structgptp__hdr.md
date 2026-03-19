---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structgptp__hdr.html
original_path: doxygen/html/structgptp__hdr.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gptp\_hdr Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [gPTP support](group__gptp.md)

gPTP message header
[More...](#details)

`#include <[gptp.h](gptp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [message\_type](#adbc9eed0fdaf07410542780c3794d642):4 |
|  | Type of the message. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [transport\_specific](#acc57b0662f64bda3bc21c9c8b6286052):4 |
|  | Transport specific, always 1. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ptp\_version](#aab942e44507bcff9af8e0a168b9fb810):4 |
|  | Version of the PTP, always 2. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [reserved0](#af9f79833695719ef42ecf0536bdfc317):4 |
|  | Reserved field. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [message\_length](#ab58626c44b57827266606a4b85bf25cc) |
|  | Total length of the message from the header to the last TLV. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [domain\_number](#a435a37858ba67222f22d4cfde3322511) |
|  | Domain number, always 0. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [reserved1](#aec4214f5392123bb3cd328b94aea8d2a) |
|  | Reserved field. |
| struct [gptp\_flags](structgptp__flags.md) | [flags](#a4c6eadb27839a3b45461df5e2078b5a7) |
|  | Message flags. |
| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [correction\_field](#a38d80a7ef0ed94c50baf6285b735cf4d) |
|  | Correction Field. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [reserved2](#ac6340bd434fad75f7faa8386bb591412) |
|  | Reserved field. |
| struct [gptp\_port\_identity](structgptp__port__identity.md) | [port\_id](#a7e89c039b956b5fa7229b58dde855a20) |
|  | Port Identity of the sender. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sequence\_id](#a50f192fb70ae8633c80fa5eeb178f852) |
|  | Sequence Id. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [control](#a68f6642239b801f2fe602a4331743d83) |
|  | Control value. |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [log\_msg\_interval](#a5fab00d293c3fb38fedf483b11f72890) |
|  | Message Interval in Log2 for Sync and Announce messages. |

## Detailed Description

gPTP message header

## Field Documentation

## [◆ ](#a68f6642239b801f2fe602a4331743d83)control

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gptp\_hdr::control |
| --- |

Control value.

Sync: 0, Follow-up: 2, Others: 5.

## [◆ ](#a38d80a7ef0ed94c50baf6285b735cf4d)correction\_field

| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) gptp\_hdr::correction\_field |
| --- |

Correction Field.

The content depends of the message type.

## [◆ ](#a435a37858ba67222f22d4cfde3322511)domain\_number

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gptp\_hdr::domain\_number |
| --- |

Domain number, always 0.

## [◆ ](#a4c6eadb27839a3b45461df5e2078b5a7)flags

| struct [gptp\_flags](structgptp__flags.md) gptp\_hdr::flags |
| --- |

Message flags.

## [◆ ](#a5fab00d293c3fb38fedf483b11f72890)log\_msg\_interval

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) gptp\_hdr::log\_msg\_interval |
| --- |

Message Interval in Log2 for Sync and Announce messages.

## [◆ ](#ab58626c44b57827266606a4b85bf25cc)message\_length

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) gptp\_hdr::message\_length |
| --- |

Total length of the message from the header to the last TLV.

## [◆ ](#adbc9eed0fdaf07410542780c3794d642)message\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gptp\_hdr::message\_type |
| --- |

Type of the message.

## [◆ ](#a7e89c039b956b5fa7229b58dde855a20)port\_id

| struct [gptp\_port\_identity](structgptp__port__identity.md) gptp\_hdr::port\_id |
| --- |

Port Identity of the sender.

## [◆ ](#aab942e44507bcff9af8e0a168b9fb810)ptp\_version

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gptp\_hdr::ptp\_version |
| --- |

Version of the PTP, always 2.

## [◆ ](#af9f79833695719ef42ecf0536bdfc317)reserved0

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gptp\_hdr::reserved0 |
| --- |

Reserved field.

## [◆ ](#aec4214f5392123bb3cd328b94aea8d2a)reserved1

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gptp\_hdr::reserved1 |
| --- |

Reserved field.

## [◆ ](#ac6340bd434fad75f7faa8386bb591412)reserved2

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gptp\_hdr::reserved2 |
| --- |

Reserved field.

## [◆ ](#a50f192fb70ae8633c80fa5eeb178f852)sequence\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) gptp\_hdr::sequence\_id |
| --- |

Sequence Id.

## [◆ ](#acc57b0662f64bda3bc21c9c8b6286052)transport\_specific

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gptp\_hdr::transport\_specific |
| --- |

Transport specific, always 1.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[gptp.h](gptp_8h_source.md)

- [gptp\_hdr](structgptp__hdr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structscmi__protocol.html
original_path: doxygen/html/structscmi__protocol.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

scmi\_protocol Struct Reference

SCMI protocol structure.
[More...](#details)

`#include <[protocol.h](protocol_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [id](#ae2c2026eeaad8c5bf73be885fdd6315c) |
|  | protocol ID |
| struct [scmi\_channel](structscmi__channel.md) \* | [tx](#aa2a78f57d21a573c6091fba89a757a52) |
|  | TX channel. |
| const struct [device](structdevice.md) \* | [transport](#a9081097c7aa12c407ec1d837c541d666) |
|  | transport layer device |
| void \* | [data](#ad6c1e08eebc96ff76ae656510d04a9d5) |
|  | protocol private data |

## Detailed Description

SCMI protocol structure.

## Field Documentation

## [◆ ](#ad6c1e08eebc96ff76ae656510d04a9d5)data

| void\* scmi\_protocol::data |
| --- |

protocol private data

## [◆ ](#ae2c2026eeaad8c5bf73be885fdd6315c)id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) scmi\_protocol::id |
| --- |

protocol ID

## [◆ ](#a9081097c7aa12c407ec1d837c541d666)transport

| const struct [device](structdevice.md)\* scmi\_protocol::transport |
| --- |

transport layer device

## [◆ ](#aa2a78f57d21a573c6091fba89a757a52)tx

| struct [scmi\_channel](structscmi__channel.md)\* scmi\_protocol::tx |
| --- |

TX channel.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/firmware/scmi/[protocol.h](protocol_8h_source.md)

- [scmi\_protocol](structscmi__protocol.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

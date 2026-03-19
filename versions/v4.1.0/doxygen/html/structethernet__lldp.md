---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structethernet__lldp.html
original_path: doxygen/html/structethernet__lldp.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ethernet\_lldp Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Ethernet Support Functions](group__ethernet.md)

Ethernet LLDP specific parameters.
[More...](#details)

`#include <[ethernet.h](ethernet_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a8cf37774b067ffbc4876e42c3b28e536) |
|  | Used for track timers. |
| const struct [net\_lldpdu](structnet__lldpdu.md) \* | [lldpdu](#aede4281b7f53be43f524d47bb2c606d1) |
|  | LLDP Data Unit mandatory TLVs for the interface. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [optional\_du](#a732d685dd27d2be5cb6b51175b8af70f) |
|  | LLDP Data Unit optional TLVs for the interface. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [optional\_len](#aabc1141bbc72a17e3884138c61bd5b0c) |
|  | Length of the optional Data Unit TLVs. |
| struct [net\_if](structnet__if.md) \* | [iface](#ae15dfbab311c17a9075c94b6915b5fd6) |
|  | Network interface that has LLDP supported. |
| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [tx\_timer\_start](#af4c5d4a5ad00e08dc311e5ab6fa44a97) |
|  | LLDP TX timer start time. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [tx\_timer\_timeout](#af179e53f86d44af34608a2a40a5e0294) |
|  | LLDP TX timeout. |
| [net\_lldp\_recv\_cb\_t](group__lldp.md#ga1e9fb662d7cdfc3c4c68cfd0312987cf) | [cb](#a8d2452f182c52000bec93f4c53501220) |
|  | LLDP RX callback function. |

## Detailed Description

Ethernet LLDP specific parameters.

## Field Documentation

## [◆ ](#a8d2452f182c52000bec93f4c53501220)cb

| [net\_lldp\_recv\_cb\_t](group__lldp.md#ga1e9fb662d7cdfc3c4c68cfd0312987cf) ethernet\_lldp::cb |
| --- |

LLDP RX callback function.

## [◆ ](#ae15dfbab311c17a9075c94b6915b5fd6)iface

| struct [net\_if](structnet__if.md)\* ethernet\_lldp::iface |
| --- |

Network interface that has LLDP supported.

## [◆ ](#aede4281b7f53be43f524d47bb2c606d1)lldpdu

| const struct [net\_lldpdu](structnet__lldpdu.md)\* ethernet\_lldp::lldpdu |
| --- |

LLDP Data Unit mandatory TLVs for the interface.

## [◆ ](#a8cf37774b067ffbc4876e42c3b28e536)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) ethernet\_lldp::node |
| --- |

Used for track timers.

## [◆ ](#a732d685dd27d2be5cb6b51175b8af70f)optional\_du

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* ethernet\_lldp::optional\_du |
| --- |

LLDP Data Unit optional TLVs for the interface.

## [◆ ](#aabc1141bbc72a17e3884138c61bd5b0c)optional\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ethernet\_lldp::optional\_len |
| --- |

Length of the optional Data Unit TLVs.

## [◆ ](#af4c5d4a5ad00e08dc311e5ab6fa44a97)tx\_timer\_start

| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) ethernet\_lldp::tx\_timer\_start |
| --- |

LLDP TX timer start time.

## [◆ ](#af179e53f86d44af34608a2a40a5e0294)tx\_timer\_timeout

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ethernet\_lldp::tx\_timer\_timeout |
| --- |

LLDP TX timeout.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ethernet.h](ethernet_8h_source.md)

- [ethernet\_lldp](structethernet__lldp.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

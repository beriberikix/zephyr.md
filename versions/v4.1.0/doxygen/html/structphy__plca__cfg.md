---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structphy__plca__cfg.html
original_path: doxygen/html/structphy__plca__cfg.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

phy\_plca\_cfg Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Ethernet PHY Interface](group__ethernet__phy.md)

PLCA (Physical Layer Collision Avoidance) Reconciliation Sublayer configurations.
[More...](#details)

`#include <[phy.h](phy_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [version](#a2c5eafc46d4869f11336094657978879) |
|  | PLCA register map version. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [enable](#a3f8580797874684e64fed0bd9bf25a94) |
|  | PLCA configured mode (enable/disable). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [node\_id](#a7b98e4e26e7571aa7e4d1a99d81ea84a) |
|  | PLCA local node identifier. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [node\_count](#a22346f28e7959b87038e938b169e670a) |
|  | PLCA node count. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [burst\_count](#a841b0ab053ea1903e8d0756f2ec6be87) |
|  | Additional frames a node is allowed to send in single transmit opportunity (TO). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [burst\_timer](#aed0ad2e0da7dd1f7fb9e90dcd9d206ca) |
|  | Wait time for the MAC to send a new frame before interrupting the burst. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [to\_timer](#a0be4e9b562c9baabff0fb8c91868e549) |
|  | PLCA to\_timer in bit-times, which determines the PLCA transmit opportunity. |

## Detailed Description

PLCA (Physical Layer Collision Avoidance) Reconciliation Sublayer configurations.

## Field Documentation

## [◆ ](#a841b0ab053ea1903e8d0756f2ec6be87)burst\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) phy\_plca\_cfg::burst\_count |
| --- |

Additional frames a node is allowed to send in single transmit opportunity (TO).

## [◆ ](#aed0ad2e0da7dd1f7fb9e90dcd9d206ca)burst\_timer

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) phy\_plca\_cfg::burst\_timer |
| --- |

Wait time for the MAC to send a new frame before interrupting the burst.

## [◆ ](#a3f8580797874684e64fed0bd9bf25a94)enable

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) phy\_plca\_cfg::enable |
| --- |

PLCA configured mode (enable/disable).

## [◆ ](#a22346f28e7959b87038e938b169e670a)node\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) phy\_plca\_cfg::node\_count |
| --- |

PLCA node count.

## [◆ ](#a7b98e4e26e7571aa7e4d1a99d81ea84a)node\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) phy\_plca\_cfg::node\_id |
| --- |

PLCA local node identifier.

## [◆ ](#a0be4e9b562c9baabff0fb8c91868e549)to\_timer

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) phy\_plca\_cfg::to\_timer |
| --- |

PLCA to\_timer in bit-times, which determines the PLCA transmit opportunity.

## [◆ ](#a2c5eafc46d4869f11336094657978879)version

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) phy\_plca\_cfg::version |
| --- |

PLCA register map version.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[phy.h](phy_8h_source.md)

- [phy\_plca\_cfg](structphy__plca__cfg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

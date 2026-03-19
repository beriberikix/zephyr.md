---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structdsa__slave__config.html
original_path: doxygen/html/structdsa__slave__config.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dsa\_slave\_config Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Distributed Switch Architecture definitions and helpers](group__DSA.md)

Structure to provide mac address for each LAN interface.
[More...](#details)

`#include <[dsa.h](dsa_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [mac\_addr](#a1bdd6dc67a85170b4fa74358581dd854) [6] |
|  | MAC address for each LAN{123.,} ports. |

## Detailed Description

Structure to provide mac address for each LAN interface.

## Field Documentation

## [◆ ](#a1bdd6dc67a85170b4fa74358581dd854)mac\_addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dsa\_slave\_config::mac\_addr[6] |
| --- |

MAC address for each LAN{123.,} ports.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[dsa.h](dsa_8h_source.md)

- [dsa\_slave\_config](structdsa__slave__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

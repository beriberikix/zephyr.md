---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structvcpu__info.html
original_path: doxygen/html/structvcpu__info.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

vcpu\_info Struct Reference

`#include <[xen.h](xen_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [evtchn\_upcall\_pending](#a36147b6f38a5398d4226ddcd1fd8b0e3) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [pad0](#a2f48138d80da05071cbf64a7d334eefe) |
| [xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc) | [evtchn\_pending\_sel](#a34f154443856775657a7ce8ef77a7156) |
| struct [arch\_vcpu\_info](structarch__vcpu__info.md) | [arch](#a433f67b9e1c989e316d04d5976804c0a) |
| [vcpu\_time\_info\_t](xen_8h.md#a46b8329725a49204352d786ce96d8b85) | [time](#af4a9ddd9cf24c74364df924c0a815231) |

## Field Documentation

## [◆ ](#a433f67b9e1c989e316d04d5976804c0a)arch

| struct [arch\_vcpu\_info](structarch__vcpu__info.md) vcpu\_info::arch |
| --- |

## [◆ ](#a34f154443856775657a7ce8ef77a7156)evtchn\_pending\_sel

| [xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc) vcpu\_info::evtchn\_pending\_sel |
| --- |

## [◆ ](#a36147b6f38a5398d4226ddcd1fd8b0e3)evtchn\_upcall\_pending

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vcpu\_info::evtchn\_upcall\_pending |
| --- |

## [◆ ](#a2f48138d80da05071cbf64a7d334eefe)pad0

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vcpu\_info::pad0 |
| --- |

## [◆ ](#af4a9ddd9cf24c74364df924c0a815231)time

| [vcpu\_time\_info\_t](xen_8h.md#a46b8329725a49204352d786ce96d8b85) vcpu\_info::time |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/xen/public/[xen.h](xen_8h_source.md)

- [vcpu\_info](structvcpu__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structvirtual__interface__context.html
original_path: doxygen/html/structvirtual__interface__context.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

virtual\_interface\_context Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Virtual Network Interface Support Functions](group__virtual.md)

Virtual L2 context that is needed to binding to the real network interface.
[More...](#details)

`#include <[virtual.h](virtual_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [net\_if](structnet__if.md) \* | [iface](#a4a0aada1d7af7a86d2a4b12063f35c71) |
|  | Other network interface this virtual network interface is attached to. |
| enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) | [virtual\_l2\_flags](#a493cef75dd5000b19eab5db156015c6e) |
|  | This tells what L2 features does virtual support. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [is\_init](#a7e4699c462a1edfdb755833a9ab28d8f) |
|  | Is this context already initialized. |
| struct [net\_linkaddr\_storage](structnet__linkaddr__storage.md) | [lladdr](#aaf591f82e0448f2b0cbf4ea6fcf05bff) |
|  | Link address for this network interface. |
| char | [name](#a7d53af8860331f23b8ff83ba0bfcaacf) [VIRTUAL\_MAX\_NAME\_LEN] |
|  | User friendly name of this L2 layer. |

## Detailed Description

Virtual L2 context that is needed to binding to the real network interface.

## Field Documentation

## [◆ ](#a4a0aada1d7af7a86d2a4b12063f35c71)iface

| struct [net\_if](structnet__if.md)\* virtual\_interface\_context::iface |
| --- |

Other network interface this virtual network interface is attached to.

These values can be chained so virtual network interfaces can run on top of other virtual interfaces.

## [◆ ](#a7e4699c462a1edfdb755833a9ab28d8f)is\_init

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) virtual\_interface\_context::is\_init |
| --- |

Is this context already initialized.

## [◆ ](#aaf591f82e0448f2b0cbf4ea6fcf05bff)lladdr

| struct [net\_linkaddr\_storage](structnet__linkaddr__storage.md) virtual\_interface\_context::lladdr |
| --- |

Link address for this network interface.

## [◆ ](#a7d53af8860331f23b8ff83ba0bfcaacf)name

| char virtual\_interface\_context::name[VIRTUAL\_MAX\_NAME\_LEN] |
| --- |

User friendly name of this L2 layer.

## [◆ ](#a493cef75dd5000b19eab5db156015c6e)virtual\_l2\_flags

| enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) virtual\_interface\_context::virtual\_l2\_flags |
| --- |

This tells what L2 features does virtual support.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[virtual.h](virtual_8h_source.md)

- [virtual\_interface\_context](structvirtual__interface__context.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

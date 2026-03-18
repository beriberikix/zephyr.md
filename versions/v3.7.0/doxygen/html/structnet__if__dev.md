---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structnet__if__dev.html
original_path: doxygen/html/structnet__if__dev.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_if\_dev Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Interface abstraction layer](group__net__if.md)

Network Interface Device structure.
[More...](#details)

`#include <[net_if.h](net__if_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [dev](#aab633a44f165f571910dc9fc9e131c50) |
|  | The actually device driver instance the [net\_if](structnet__if.md "Network Interface structure.") is related to. |
| const struct [net\_l2](structnet__l2.md) \*const | [l2](#a85d713c62875f5fe9e3ec29773150797) |
|  | Interface's L2 layer. |
| void \* | [l2\_data](#a8fec6a7f612fc1268ef486d8bdebe018) |
|  | Interface's private L2 data pointer. |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [flags](#ac8f9c30e1dea05c28c88d3b367b130f5) [[ATOMIC\_BITMAP\_SIZE](group__atomic__apis.md#gafac28874aaad3bcec72c693186e988cb)(NET\_IF\_NUM\_FLAGS)] |
|  | For internal use. |
| struct [net\_linkaddr](structnet__linkaddr.md) | [link\_addr](#aac6d5d341ab520e6aac7f7b03737c197) |
|  | The hardware link address. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [mtu](#aa15ccca2eb67b8d2afca153ccacb3742) |
|  | The hardware MTU. |
| enum [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9) | [oper\_state](#a30eabb2ffae082d0de81a50c510738a3) |
|  | RFC 2863 operational status. |

## Detailed Description

Network Interface Device structure.

Used to handle a network interface on top of a device driver instance. There can be many [net\_if\_dev](structnet__if__dev.md "Network Interface Device structure.") instance against the same device.

Such interface is mainly to be used by the link layer, but is also tight to a network context: it then makes the relation with a network context and the network device.

Because of the strong relationship between a device driver and such network interface, each [net\_if\_dev](structnet__if__dev.md "Network Interface Device structure.") should be instantiated by one of the network device init macros found in [net\_if.h](net__if_8h.md "Public API for network interface.").

## Field Documentation

## [◆ ](#aab633a44f165f571910dc9fc9e131c50)dev

| const struct [device](structdevice.md)\* net\_if\_dev::dev |
| --- |

The actually device driver instance the [net\_if](structnet__if.md "Network Interface structure.") is related to.

## [◆ ](#ac8f9c30e1dea05c28c88d3b367b130f5)flags

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) net\_if\_dev::flags[[ATOMIC\_BITMAP\_SIZE](group__atomic__apis.md#gafac28874aaad3bcec72c693186e988cb)(NET\_IF\_NUM\_FLAGS)] |
| --- |

For internal use.

## [◆ ](#a85d713c62875f5fe9e3ec29773150797)l2

| const struct [net\_l2](structnet__l2.md)\* const net\_if\_dev::l2 |
| --- |

Interface's L2 layer.

## [◆ ](#a8fec6a7f612fc1268ef486d8bdebe018)l2\_data

| void\* net\_if\_dev::l2\_data |
| --- |

Interface's private L2 data pointer.

## [◆ ](#aac6d5d341ab520e6aac7f7b03737c197)link\_addr

| struct [net\_linkaddr](structnet__linkaddr.md) net\_if\_dev::link\_addr |
| --- |

The hardware link address.

## [◆ ](#aa15ccca2eb67b8d2afca153ccacb3742)mtu

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_if\_dev::mtu |
| --- |

The hardware MTU.

## [◆ ](#a30eabb2ffae082d0de81a50c510738a3)oper\_state

| enum [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9) net\_if\_dev::oper\_state |
| --- |

RFC 2863 operational status.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_if.h](net__if_8h_source.md)

- [net\_if\_dev](structnet__if__dev.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

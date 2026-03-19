---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/unionpd__header.html
original_path: doxygen/html/unionpd__header.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pd\_header Union Reference

[Device Driver APIs](group__io__interfaces.md) » [USB Power Delivery](group__usb__power__delivery.md)

Build a PD message header See Table 6-1 Message Header.
[More...](#details)

`#include <[usbc_pd.h](usbc__pd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct { |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [message\_type](#a70768acc6a6bc9ebb9249df7ed635a94): 5 |  |
|  | Type of message. [More...](#a70768acc6a6bc9ebb9249df7ed635a94) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [port\_data\_role](#af1b027c9c57497421117b290dcb6ac66): 1 |  |
|  | Port Data role. [More...](#af1b027c9c57497421117b290dcb6ac66) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [specification\_revision](#a85cce1728afe0d62bb29f618a1cf70e1): 2 |  |
|  | Specification Revision. [More...](#a85cce1728afe0d62bb29f618a1cf70e1) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [port\_power\_role](#a20ac99d9738c9d278a78e8ccfc401902): 1 |  |
|  | Port Power Role. [More...](#a20ac99d9738c9d278a78e8ccfc401902) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [message\_id](#ae4a0a5695e73fd3e1b7e3f38cd2a758c): 3 |  |
|  | Message ID. [More...](#ae4a0a5695e73fd3e1b7e3f38cd2a758c) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [number\_of\_data\_objects](#a63d89119f0918ba7d6eb9e01fa1ed406): 3 |  |
|  | Number of Data Objects. [More...](#a63d89119f0918ba7d6eb9e01fa1ed406) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [extended](#a5750b964c12c3bc2d2523a64cb9eb7d0): 1 |  |
|  | Extended Message. [More...](#a5750b964c12c3bc2d2523a64cb9eb7d0) |
| }; |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [raw\_value](#afa6c6699be5fe95bcb4962396e33e35d) |

## Detailed Description

Build a PD message header See Table 6-1 Message Header.

## Field Documentation

## [◆ ](#a3b4f5771e6e0fe0072d310732ea43959)[struct]

| struct { ... } [pd\_header](unionpd__header.md) |
| --- |

## [◆ ](#a5750b964c12c3bc2d2523a64cb9eb7d0)extended

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pd\_header::extended |
| --- |

Extended Message.

## [◆ ](#ae4a0a5695e73fd3e1b7e3f38cd2a758c)message\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pd\_header::message\_id |
| --- |

Message ID.

## [◆ ](#a70768acc6a6bc9ebb9249df7ed635a94)message\_type

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pd\_header::message\_type |
| --- |

Type of message.

## [◆ ](#a63d89119f0918ba7d6eb9e01fa1ed406)number\_of\_data\_objects

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pd\_header::number\_of\_data\_objects |
| --- |

Number of Data Objects.

## [◆ ](#af1b027c9c57497421117b290dcb6ac66)port\_data\_role

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pd\_header::port\_data\_role |
| --- |

Port Data role.

## [◆ ](#a20ac99d9738c9d278a78e8ccfc401902)port\_power\_role

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pd\_header::port\_power\_role |
| --- |

Port Power Role.

## [◆ ](#afa6c6699be5fe95bcb4962396e33e35d)raw\_value

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pd\_header::raw\_value |
| --- |

## [◆ ](#a85cce1728afe0d62bb29f618a1cf70e1)specification\_revision

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pd\_header::specification\_revision |
| --- |

Specification Revision.

---

The documentation for this union was generated from the following file:

- zephyr/drivers/usb\_c/[usbc\_pd.h](usbc__pd_8h_source.md)

- [pd\_header](unionpd__header.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

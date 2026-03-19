---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__mesh__comp.html
original_path: doxygen/html/structbt__mesh__comp.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_comp Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Access layer](group__bt__mesh__access.md)

Node Composition.
[More...](#details)

`#include <[access.h](access_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [cid](#a648f695898305ef9e6f4f9db42dd8cf9) |
|  | Company ID. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [pid](#a54031f4c3683a7209e8f7441c5875788) |
|  | Product ID. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [vid](#a7e4351e81e4e04bb9681e76d384f2fa5) |
|  | Version ID. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [elem\_count](#aff69499c7ac2c1ba643c946c75aa21ce) |
|  | The number of elements in this device. |
| const struct [bt\_mesh\_elem](structbt__mesh__elem.md) \* | [elem](#ad3da0629db1cb423260aa202cab7f062) |
|  | List of elements. |

## Detailed Description

Node Composition.

## Field Documentation

## [◆ ](#a648f695898305ef9e6f4f9db42dd8cf9)cid

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_comp::cid |
| --- |

Company ID.

## [◆ ](#ad3da0629db1cb423260aa202cab7f062)elem

| const struct [bt\_mesh\_elem](structbt__mesh__elem.md)\* bt\_mesh\_comp::elem |
| --- |

List of elements.

## [◆ ](#aff69499c7ac2c1ba643c946c75aa21ce)elem\_count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_mesh\_comp::elem\_count |
| --- |

The number of elements in this device.

## [◆ ](#a54031f4c3683a7209e8f7441c5875788)pid

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_comp::pid |
| --- |

Product ID.

## [◆ ](#a7e4351e81e4e04bb9681e76d384f2fa5)vid

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_comp::vid |
| --- |

Version ID.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[access.h](access_8h_source.md)

- [bt\_mesh\_comp](structbt__mesh__comp.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

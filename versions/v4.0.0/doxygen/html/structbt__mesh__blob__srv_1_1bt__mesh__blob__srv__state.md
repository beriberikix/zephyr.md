---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.html
original_path: doxygen/html/structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_blob\_srv::bt\_mesh\_blob\_srv\_state Struct Reference

`#include <[blob_srv.h](blob__srv_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) | [xfer](#ac5d12eef4c5723af0e19296d75f1c820) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [cli](#a08358fb301e775ed23c0d062676fbf22) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [app\_idx](#a6273d55eda23f868d51382c56bc41e27) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [timeout\_base](#a0c87b3052680c675303747e805c2990e) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [mtu\_size](#aadd08825d36f3ae1e4fe3a7845903f41) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ttl](#a79b0521bbd2473c6b414a24c5a7bf98a) |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [blocks](#a0f5d7d310be154f85ee96ccceb12e971) [[ATOMIC\_BITMAP\_SIZE](group__atomic__apis.md#gafac28874aaad3bcec72c693186e988cb)(1)] |

## Field Documentation

## [◆ ](#a6273d55eda23f868d51382c56bc41e27)app\_idx

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_blob\_srv::bt\_mesh\_blob\_srv\_state::app\_idx |
| --- |

## [◆ ](#a0f5d7d310be154f85ee96ccceb12e971)blocks

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) bt\_mesh\_blob\_srv::bt\_mesh\_blob\_srv\_state::blocks[[ATOMIC\_BITMAP\_SIZE](group__atomic__apis.md#gafac28874aaad3bcec72c693186e988cb)(1)] |
| --- |

## [◆ ](#a08358fb301e775ed23c0d062676fbf22)cli

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_blob\_srv::bt\_mesh\_blob\_srv\_state::cli |
| --- |

## [◆ ](#aadd08825d36f3ae1e4fe3a7845903f41)mtu\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_blob\_srv::bt\_mesh\_blob\_srv\_state::mtu\_size |
| --- |

## [◆ ](#a0c87b3052680c675303747e805c2990e)timeout\_base

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_blob\_srv::bt\_mesh\_blob\_srv\_state::timeout\_base |
| --- |

## [◆ ](#a79b0521bbd2473c6b414a24c5a7bf98a)ttl

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_blob\_srv::bt\_mesh\_blob\_srv\_state::ttl |
| --- |

## [◆ ](#ac5d12eef4c5723af0e19296d75f1c820)xfer

| struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) bt\_mesh\_blob\_srv::bt\_mesh\_blob\_srv\_state::xfer |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[blob\_srv.h](blob__srv_8h_source.md)

- [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md)
- [bt\_mesh\_blob\_srv\_state](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__conn__le__cs__procedure__enable__complete.html
original_path: doxygen/html/structbt__conn__le__cs__procedure__enable__complete.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_conn\_le\_cs\_procedure\_enable\_complete Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Connection management](group__bt__conn.md)

`#include <[conn.h](conn_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [config\_id](#a2e290c25ec5af8b0259d45f04d6c543d) |
| enum [bt\_conn\_le\_cs\_procedure\_enable\_state](group__bt__conn.md#gaf3653de72793f775e33fd9eb04c3e7a2) | [state](#acc1d12d347e1b02b2eea562ea064a40b) |
| enum [bt\_conn\_le\_cs\_tone\_antenna\_config\_selection](group__bt__conn.md#gab7acdbdf273fc760799cf0d8cf71591c) | [tone\_antenna\_config\_selection](#a3fa8ad4dd264eb4e2489dea9c1048d22) |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [selected\_tx\_power](#aeb918e438cd02296c7f693757268f6bf) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [subevent\_len](#ae990a10c468ec62fbaf9325c94733c7c) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [subevents\_per\_event](#a40b03220932852b6b51d65f557c21f17) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [subevent\_interval](#a77a2bd8ee384c4567321a09f6b64782c) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [event\_interval](#a4129ab9519ba140ffb198aa9a5cde6ac) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [procedure\_interval](#a8511deef97f19c53ddaa4dec8492658f) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [procedure\_count](#ab83778fe2d1274e5658fd5f5f867314f) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [max\_procedure\_len](#ad71825d71ab89baea138e41f9a3ff57e) |

## Field Documentation

## [◆ ](#a2e290c25ec5af8b0259d45f04d6c543d)config\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_cs\_procedure\_enable\_complete::config\_id |
| --- |

## [◆ ](#a4129ab9519ba140ffb198aa9a5cde6ac)event\_interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_cs\_procedure\_enable\_complete::event\_interval |
| --- |

## [◆ ](#ad71825d71ab89baea138e41f9a3ff57e)max\_procedure\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_cs\_procedure\_enable\_complete::max\_procedure\_len |
| --- |

## [◆ ](#ab83778fe2d1274e5658fd5f5f867314f)procedure\_count

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_cs\_procedure\_enable\_complete::procedure\_count |
| --- |

## [◆ ](#a8511deef97f19c53ddaa4dec8492658f)procedure\_interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_cs\_procedure\_enable\_complete::procedure\_interval |
| --- |

## [◆ ](#aeb918e438cd02296c7f693757268f6bf)selected\_tx\_power

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_conn\_le\_cs\_procedure\_enable\_complete::selected\_tx\_power |
| --- |

## [◆ ](#acc1d12d347e1b02b2eea562ea064a40b)state

| enum [bt\_conn\_le\_cs\_procedure\_enable\_state](group__bt__conn.md#gaf3653de72793f775e33fd9eb04c3e7a2) bt\_conn\_le\_cs\_procedure\_enable\_complete::state |
| --- |

## [◆ ](#a77a2bd8ee384c4567321a09f6b64782c)subevent\_interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_cs\_procedure\_enable\_complete::subevent\_interval |
| --- |

## [◆ ](#ae990a10c468ec62fbaf9325c94733c7c)subevent\_len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_conn\_le\_cs\_procedure\_enable\_complete::subevent\_len |
| --- |

## [◆ ](#a40b03220932852b6b51d65f557c21f17)subevents\_per\_event

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_cs\_procedure\_enable\_complete::subevents\_per\_event |
| --- |

## [◆ ](#a3fa8ad4dd264eb4e2489dea9c1048d22)tone\_antenna\_config\_selection

| enum [bt\_conn\_le\_cs\_tone\_antenna\_config\_selection](group__bt__conn.md#gab7acdbdf273fc760799cf0d8cf71591c) bt\_conn\_le\_cs\_procedure\_enable\_complete::tone\_antenna\_config\_selection |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[conn.h](conn_8h_source.md)

- [bt\_conn\_le\_cs\_procedure\_enable\_complete](structbt__conn__le__cs__procedure__enable__complete.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__l2cap__br__chan.html
original_path: doxygen/html/structbt__l2cap__br__chan.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_l2cap\_br\_chan Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [L2CAP](group__bt__l2cap.md)

BREDR L2CAP Channel structure.
[More...](#details)

`#include <[zephyr/bluetooth/l2cap.h](l2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) | [chan](#a28ed2b2541697390c325c706d4ad8f0b) |
|  | Common L2CAP channel reference object. |
| struct [bt\_l2cap\_br\_endpoint](structbt__l2cap__br__endpoint.md) | [rx](#a00d49d2d73f2dafdc73a9f7b9393b98d) |
|  | Channel Receiving Endpoint. |
| struct [bt\_l2cap\_br\_endpoint](structbt__l2cap__br__endpoint.md) | [tx](#a67aec1f3bef3afe689c164185bd77f98) |
|  | Channel Transmission Endpoint. |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [flags](#a09ded589b7e1571fc5d021ceafa68b5f) [1] |
| [bt\_l2cap\_chan\_state\_t](group__bt__l2cap.md#ga5a80330e52ea0fa4ee3266094570bb16) | [state](#a556858a2e539bd4d5ed2ae66f392dc74) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [psm](#a1ca3ed81f6f8edafc2993941de4c9771) |
|  | Remote PSM to be connected. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ident](#ace996412a41a168c37d60d5e4096dc94) |
|  | Helps match request context during CoC. |
| [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) | [required\_sec\_level](#a19bb2e243fb616b73d8b082df7c4a394) |
| struct [k\_work\_delayable](structk__work__delayable.md) | [rtx\_work](#a0e637544c14d7d2b0ccd2af5424555fb) |
| struct [k\_work\_sync](structk__work__sync.md) | [rtx\_sync](#a21224ab26501eca21aaed468681d6274) |
| struct [bt\_l2cap\_br\_window](structbt__l2cap__br__window.md) | [tx\_win](#a96cb3a6bb3f3c97372c314eb1bfca32b) [CONFIG\_BT\_L2CAP\_MAX\_WINDOW\_SIZE] |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [tx\_seq](#ad4c352f1d43dce110ddf47c665b7ae17) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [next\_tx\_seq](#a6e559e94251ce9ef1c7d139695adf7ef) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [expected\_ack\_seq](#ae48194e987caf3153738f3027ec7022d) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [req\_seq](#afa3dcfc293485a09d76a67c30ee0acf8) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [expected\_tx\_seq](#a734b9699538989fa8e5cec11eb84609e) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [buffer\_seq](#aa1fd44c5eb136e1fbd0f46f09d5fde0a) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [retry\_count](#a3f9621b9d02b70f1dc9492520ff7cd03) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [srej\_save\_req\_seq](#a97266be01c9ee7e5f64f182173d50418) |
| struct [k\_work\_delayable](structk__work__delayable.md) | [ret\_work](#a6a1788de2f5c037b46070a65c2a1111d) |
| struct [k\_work\_delayable](structk__work__delayable.md) | [monitor\_work](#ac887d3192240594de4d6cb8d4af9553b) |

## Detailed Description

BREDR L2CAP Channel structure.

## Field Documentation

## [◆ ](#aa1fd44c5eb136e1fbd0f46f09d5fde0a)buffer\_seq

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_l2cap\_br\_chan::buffer\_seq |
| --- |

## [◆ ](#a28ed2b2541697390c325c706d4ad8f0b)chan

| struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) bt\_l2cap\_br\_chan::chan |
| --- |

Common L2CAP channel reference object.

## [◆ ](#ae48194e987caf3153738f3027ec7022d)expected\_ack\_seq

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_l2cap\_br\_chan::expected\_ack\_seq |
| --- |

## [◆ ](#a734b9699538989fa8e5cec11eb84609e)expected\_tx\_seq

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_l2cap\_br\_chan::expected\_tx\_seq |
| --- |

## [◆ ](#a09ded589b7e1571fc5d021ceafa68b5f)flags

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) bt\_l2cap\_br\_chan::flags[1] |
| --- |

## [◆ ](#ace996412a41a168c37d60d5e4096dc94)ident

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_l2cap\_br\_chan::ident |
| --- |

Helps match request context during CoC.

## [◆ ](#ac887d3192240594de4d6cb8d4af9553b)monitor\_work

| struct [k\_work\_delayable](structk__work__delayable.md) bt\_l2cap\_br\_chan::monitor\_work |
| --- |

## [◆ ](#a6e559e94251ce9ef1c7d139695adf7ef)next\_tx\_seq

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_l2cap\_br\_chan::next\_tx\_seq |
| --- |

## [◆ ](#a1ca3ed81f6f8edafc2993941de4c9771)psm

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_l2cap\_br\_chan::psm |
| --- |

Remote PSM to be connected.

## [◆ ](#afa3dcfc293485a09d76a67c30ee0acf8)req\_seq

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_l2cap\_br\_chan::req\_seq |
| --- |

## [◆ ](#a19bb2e243fb616b73d8b082df7c4a394)required\_sec\_level

| [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) bt\_l2cap\_br\_chan::required\_sec\_level |
| --- |

## [◆ ](#a6a1788de2f5c037b46070a65c2a1111d)ret\_work

| struct [k\_work\_delayable](structk__work__delayable.md) bt\_l2cap\_br\_chan::ret\_work |
| --- |

## [◆ ](#a3f9621b9d02b70f1dc9492520ff7cd03)retry\_count

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_l2cap\_br\_chan::retry\_count |
| --- |

## [◆ ](#a21224ab26501eca21aaed468681d6274)rtx\_sync

| struct [k\_work\_sync](structk__work__sync.md) bt\_l2cap\_br\_chan::rtx\_sync |
| --- |

## [◆ ](#a0e637544c14d7d2b0ccd2af5424555fb)rtx\_work

| struct [k\_work\_delayable](structk__work__delayable.md) bt\_l2cap\_br\_chan::rtx\_work |
| --- |

## [◆ ](#a00d49d2d73f2dafdc73a9f7b9393b98d)rx

| struct [bt\_l2cap\_br\_endpoint](structbt__l2cap__br__endpoint.md) bt\_l2cap\_br\_chan::rx |
| --- |

Channel Receiving Endpoint.

## [◆ ](#a97266be01c9ee7e5f64f182173d50418)srej\_save\_req\_seq

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_l2cap\_br\_chan::srej\_save\_req\_seq |
| --- |

## [◆ ](#a556858a2e539bd4d5ed2ae66f392dc74)state

| [bt\_l2cap\_chan\_state\_t](group__bt__l2cap.md#ga5a80330e52ea0fa4ee3266094570bb16) bt\_l2cap\_br\_chan::state |
| --- |

## [◆ ](#a67aec1f3bef3afe689c164185bd77f98)tx

| struct [bt\_l2cap\_br\_endpoint](structbt__l2cap__br__endpoint.md) bt\_l2cap\_br\_chan::tx |
| --- |

Channel Transmission Endpoint.

## [◆ ](#ad4c352f1d43dce110ddf47c665b7ae17)tx\_seq

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_l2cap\_br\_chan::tx\_seq |
| --- |

## [◆ ](#a96cb3a6bb3f3c97372c314eb1bfca32b)tx\_win

| struct [bt\_l2cap\_br\_window](structbt__l2cap__br__window.md) bt\_l2cap\_br\_chan::tx\_win[CONFIG\_BT\_L2CAP\_MAX\_WINDOW\_SIZE] |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[l2cap.h](l2cap_8h_source.md)

- [bt\_l2cap\_br\_chan](structbt__l2cap__br__chan.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

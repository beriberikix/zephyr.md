---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__l2cap__le__chan.html
original_path: doxygen/html/structbt__l2cap__le__chan.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_l2cap\_le\_chan Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [L2CAP](group__bt__l2cap.md)

LE L2CAP Channel structure.
[More...](#details)

`#include <[l2cap.h](l2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) | [chan](#a980126cabc3824ab623d634d91f7d761) |
|  | Common L2CAP channel reference object. |
| struct [bt\_l2cap\_le\_endpoint](structbt__l2cap__le__endpoint.md) | [rx](#a95808ad9bcd910b65bee31fa6bd4b638) |
|  | Channel Receiving Endpoint. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [pending\_rx\_mtu](#a55d8ce850f365ac7ab7ff450ecb61f23) |
|  | Pending RX MTU on ECFC reconfigure, used internally by stack. |
| struct [bt\_l2cap\_le\_endpoint](structbt__l2cap__le__endpoint.md) | [tx](#a059f98cebf6f43a05937ac82815009e7) |
|  | Channel Transmission Endpoint. |

## Detailed Description

LE L2CAP Channel structure.

## Field Documentation

## [◆ ](#a980126cabc3824ab623d634d91f7d761)chan

| struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) bt\_l2cap\_le\_chan::chan |
| --- |

Common L2CAP channel reference object.

## [◆ ](#a55d8ce850f365ac7ab7ff450ecb61f23)pending\_rx\_mtu

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_l2cap\_le\_chan::pending\_rx\_mtu |
| --- |

Pending RX MTU on ECFC reconfigure, used internally by stack.

## [◆ ](#a95808ad9bcd910b65bee31fa6bd4b638)rx

| struct [bt\_l2cap\_le\_endpoint](structbt__l2cap__le__endpoint.md) bt\_l2cap\_le\_chan::rx |
| --- |

Channel Receiving Endpoint.

If the application has set an alloc\_buf channel callback for the channel to support receiving segmented L2CAP SDUs the application should inititalize the MTU of the Receiving Endpoint. Otherwise the MTU of the receiving endpoint will be initialized to [BT\_L2CAP\_SDU\_RX\_MTU](group__bt__l2cap.md#ga13b93a8f09157fbcf739fa4949840efe "BT_L2CAP_SDU_RX_MTU") by the stack.

This is the source of the MTU, MPS and credit values when sending L2CAP\_LE\_CREDIT\_BASED\_CONNECTION\_REQ/RSP and L2CAP\_CONFIGURATION\_REQ.

## [◆ ](#a059f98cebf6f43a05937ac82815009e7)tx

| struct [bt\_l2cap\_le\_endpoint](structbt__l2cap__le__endpoint.md) bt\_l2cap\_le\_chan::tx |
| --- |

Channel Transmission Endpoint.

This is an image of the remote's rx.

The MTU and MPS is controlled by the remote by L2CAP\_LE\_CREDIT\_BASED\_CONNECTION\_REQ/RSP or L2CAP\_CONFIGURATION\_REQ.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[l2cap.h](l2cap_8h_source.md)

- [bt\_l2cap\_le\_chan](structbt__l2cap__le__chan.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

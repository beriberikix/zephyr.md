---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__l2cap__chan.html
original_path: doxygen/html/structbt__l2cap__chan.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_l2cap\_chan Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [L2CAP](group__bt__l2cap.md)

L2CAP Channel structure.
[More...](#details)

`#include <[l2cap.h](l2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct bt\_conn \* | [conn](#a007a7ef11a00c0dff22cd64961260d3d) |
|  | Channel connection reference. |
| const struct [bt\_l2cap\_chan\_ops](structbt__l2cap__chan__ops.md) \* | [ops](#a3e370744f17ca4cff200cc0a2ee1a74b) |
|  | Channel operations reference. |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a123ae4bb1db6f4b41561b3d4691b1c02) |
| [bt\_l2cap\_chan\_destroy\_t](group__bt__l2cap.md#ga88baae9c159f3de4ccb34fd0e3cc8c3b) | [destroy](#ac0fbde11b35e0b6b424970e73c945a40) |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [status](#a7603e2c212e0522a1ffca2198224a994) [[ATOMIC\_BITMAP\_SIZE](group__atomic__apis.md#gafac28874aaad3bcec72c693186e988cb)([BT\_L2CAP\_NUM\_STATUS](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015ca91bd77f9889b59ba5b0005a51016ba2c))] |

## Detailed Description

L2CAP Channel structure.

## Field Documentation

## [◆ ](#a007a7ef11a00c0dff22cd64961260d3d)conn

| struct bt\_conn\* bt\_l2cap\_chan::conn |
| --- |

Channel connection reference.

## [◆ ](#ac0fbde11b35e0b6b424970e73c945a40)destroy

| [bt\_l2cap\_chan\_destroy\_t](group__bt__l2cap.md#ga88baae9c159f3de4ccb34fd0e3cc8c3b) bt\_l2cap\_chan::destroy |
| --- |

## [◆ ](#a123ae4bb1db6f4b41561b3d4691b1c02)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) bt\_l2cap\_chan::node |
| --- |

## [◆ ](#a3e370744f17ca4cff200cc0a2ee1a74b)ops

| const struct [bt\_l2cap\_chan\_ops](structbt__l2cap__chan__ops.md)\* bt\_l2cap\_chan::ops |
| --- |

Channel operations reference.

## [◆ ](#a7603e2c212e0522a1ffca2198224a994)status

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) bt\_l2cap\_chan::status[[ATOMIC\_BITMAP\_SIZE](group__atomic__apis.md#gafac28874aaad3bcec72c693186e988cb)([BT\_L2CAP\_NUM\_STATUS](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015ca91bd77f9889b59ba5b0005a51016ba2c))] |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[l2cap.h](l2cap_8h_source.md)

- [bt\_l2cap\_chan](structbt__l2cap__chan.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

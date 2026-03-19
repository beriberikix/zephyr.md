---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__bap__ascs__rsp.html
original_path: doxygen/html/structbt__bap__ascs__rsp.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_ascs\_rsp Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md)

Structure storing values of fields of ASE Control Point notification.
[More...](#details)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) | [code](#a8ea364298f7e3e784b7878215db63d91) |
|  | Value of the Response Code field. |
| union { |  |
| enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45)   [reason](#a138532bc40f60547c56d8b108ad44d1e) |  |
|  | Response reason. [More...](#a138532bc40f60547c56d8b108ad44d1e) |
| enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354)   [metadata\_type](#a736f44864015244a8b48a859eff6b902) |  |
|  | Response metadata type. [More...](#a736f44864015244a8b48a859eff6b902) |
| }; |  |
|  | Value of the Reason field. |

## Detailed Description

Structure storing values of fields of ASE Control Point notification.

## Field Documentation

## [◆ ](#a69145bb4bb3a642a8165f834d73e5d7c)[union]

| union { ... } [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) |
| --- |

Value of the Reason field.

The meaning of this value depend on the Response Code field.

## [◆ ](#a8ea364298f7e3e784b7878215db63d91)code

| enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) bt\_bap\_ascs\_rsp::code |
| --- |

Value of the Response Code field.

The following response codes are accepted:

- [BT\_BAP\_ASCS\_RSP\_CODE\_SUCCESS](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ae6e8ebcfc2578eefec11cb9e8222eafd "BT_BAP_ASCS_RSP_CODE_SUCCESS")
- [BT\_BAP\_ASCS\_RSP\_CODE\_CAP\_UNSUPPORTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a96278dcde41d37b6e9fd2a926c9ff16a "BT_BAP_ASCS_RSP_CODE_CAP_UNSUPPORTED")
- [BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_UNSUPPORTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a5a0230629bffc7659ec8127169a90b62 "BT_BAP_ASCS_RSP_CODE_CONF_UNSUPPORTED")
- [BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_REJECTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1af587ec0a8b72fd9a7379aa173a8beb21 "BT_BAP_ASCS_RSP_CODE_CONF_REJECTED")
- [BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_UNSUPPORTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ad604f01d7a964fc8ae55dc76a5a8e0a7 "BT_BAP_ASCS_RSP_CODE_METADATA_UNSUPPORTED")
- [BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_REJECTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a9945d6001d365d759023fc233514ed06 "BT_BAP_ASCS_RSP_CODE_METADATA_REJECTED")
- [BT\_BAP\_ASCS\_RSP\_CODE\_NO\_MEM](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a9676a2e7fc5e417cbae2cea663204ccb "BT_BAP_ASCS_RSP_CODE_NO_MEM")
- [BT\_BAP\_ASCS\_RSP\_CODE\_UNSPECIFIED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ac6c03bd8827040ce48905c58ea7d423a "BT_BAP_ASCS_RSP_CODE_UNSPECIFIED")

## [◆ ](#a736f44864015244a8b48a859eff6b902)metadata\_type

| enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) bt\_bap\_ascs\_rsp::metadata\_type |
| --- |

Response metadata type.

If the Response Code is one of the following:

- [BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_UNSUPPORTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ad604f01d7a964fc8ae55dc76a5a8e0a7 "BT_BAP_ASCS_RSP_CODE_METADATA_UNSUPPORTED")
- [BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_REJECTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a9945d6001d365d759023fc233514ed06 "BT_BAP_ASCS_RSP_CODE_METADATA_REJECTED") the value of the Metadata Type shall be used.

## [◆ ](#a138532bc40f60547c56d8b108ad44d1e)reason

| enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) bt\_bap\_ascs\_rsp::reason |
| --- |

Response reason.

If the Response Code is one of the following:

- [BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_UNSUPPORTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a5a0230629bffc7659ec8127169a90b62 "BT_BAP_ASCS_RSP_CODE_CONF_UNSUPPORTED")
- [BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_REJECTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1af587ec0a8b72fd9a7379aa173a8beb21 "BT_BAP_ASCS_RSP_CODE_CONF_REJECTED") all values from [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45 "bt_bap_ascs_reason") can be used.

If the Response Code is one of the following:

- [BT\_BAP\_ASCS\_RSP\_CODE\_SUCCESS](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ae6e8ebcfc2578eefec11cb9e8222eafd "BT_BAP_ASCS_RSP_CODE_SUCCESS")
- [BT\_BAP\_ASCS\_RSP\_CODE\_CAP\_UNSUPPORTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a96278dcde41d37b6e9fd2a926c9ff16a "BT_BAP_ASCS_RSP_CODE_CAP_UNSUPPORTED")
- [BT\_BAP\_ASCS\_RSP\_CODE\_NO\_MEM](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a9676a2e7fc5e417cbae2cea663204ccb "BT_BAP_ASCS_RSP_CODE_NO_MEM")
- [BT\_BAP\_ASCS\_RSP\_CODE\_UNSPECIFIED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ac6c03bd8827040ce48905c58ea7d423a "BT_BAP_ASCS_RSP_CODE_UNSPECIFIED") only value [BT\_BAP\_ASCS\_REASON\_NONE](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a1d4794f987bab3c784955ac10e1cdcdd "BT_BAP_ASCS_REASON_NONE") shall be used.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

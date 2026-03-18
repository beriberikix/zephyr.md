---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__usb__hid__items.html
original_path: doxygen/html/group__usb__hid__items.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

USB HID Item helpers

[Connectivity](group__connectivity.md) » [USB](group__usb.md) » [USB HID common definitions](group__usb__hid__definitions.md)

| Macros | |
| --- | --- |
| #define | [HID\_ITEM](#ga4e9dc6652402e0b87e1313c143737ed4)(bTag, bType, bSize) |
|  | Define HID short item. |
| #define | [HID\_INPUT](#ga8646699330c45fb008d50b54be339c6c)(a) |
|  | Define HID Input item with the data length of one byte. |
| #define | [HID\_OUTPUT](#ga6ef7aa576bf69f9ba5f93df500a1403c)(a) |
|  | Define HID Output item with the data length of one byte. |
| #define | [HID\_FEATURE](#ga951a415e05e95492250d4fb43a37090d)(a) |
|  | Define HID Feature item with the data length of one byte. |
| #define | [HID\_COLLECTION](#gad010ed98662b0e653754caff1dfd352f)(a) |
|  | Define HID Collection item with the data length of one byte. |
| #define | [HID\_END\_COLLECTION](#ga6cd6affb9d52e0bf98c7a5c83d03a764)   [HID\_ITEM](#ga4e9dc6652402e0b87e1313c143737ed4)([HID\_ITEM\_TAG\_COLLECTION\_END](group__usb__hid__definitions.md#ga3f4fe1817887966f0d05aa597cd0ab79), [HID\_ITEM\_TYPE\_MAIN](group__usb__hid__definitions.md#ga9a71248c522943951b5af70ec9c14c02), 0) |
|  | Define HID End Collection (non-data) item. |
| #define | [HID\_USAGE\_PAGE](#ga30dc3f62583822ba27edd984dc2dec39)(page) |
|  | Define HID Usage Page item. |
| #define | [HID\_LOGICAL\_MIN8](#gacd141f6ede5122f260cd50338649d458)(a) |
|  | Define HID Logical Minimum item with the data length of one byte. |
| #define | [HID\_LOGICAL\_MAX8](#ga2f6b809ae85b6716ade8c52da4fa56af)(a) |
|  | Define HID Logical Maximum item with the data length of one byte. |
| #define | [HID\_LOGICAL\_MIN16](#ga5e290798d55bccd7474dbfb6bc2d1033)(a, b) |
|  | Define HID Logical Minimum item with the data length of two bytes. |
| #define | [HID\_LOGICAL\_MAX16](#ga9b804d676812dcfb0ec12f3aa887e37f)(a, b) |
|  | Define HID Logical Maximum item with the data length of two bytes. |
| #define | [HID\_LOGICAL\_MIN32](#gad4b2ff8642676d692fd0d56ab0cbeaa7)(a, b, c, [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)) |
|  | Define HID Logical Minimum item with the data length of four bytes. |
| #define | [HID\_LOGICAL\_MAX32](#gae9d17e753685b0df6c53f942ce9c95d2)(a, b, c, [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)) |
|  | Define HID Logical Maximum item with the data length of four bytes. |
| #define | [HID\_REPORT\_SIZE](#ga3135a21a63c491daf8647fa771def0e7)(size) |
|  | Define HID Report Size item with the data length of one byte. |
| #define | [HID\_REPORT\_ID](#ga1b45fce2c7df2847b1326fca29cef389)(id) |
|  | Define HID Report ID item with the data length of one byte. |
| #define | [HID\_REPORT\_COUNT](#ga71192f2a55f05456b893069ebfbc5b98)(count) |
|  | Define HID Report Count item with the data length of one byte. |
| #define | [HID\_USAGE](#gac8429a70866a898887ead55664e04bd7)(idx) |
|  | Define HID Usage Index item with the data length of one byte. |
| #define | [HID\_USAGE\_MIN8](#gabf53f1e2eae6d686aeb7d62cc46b22ad)(a) |
|  | Define HID Usage Minimum item with the data length of one byte. |
| #define | [HID\_USAGE\_MAX8](#gae7fc9684ef10f50d69df6f495cc09e91)(a) |
|  | Define HID Usage Maximum item with the data length of one byte. |
| #define | [HID\_USAGE\_MIN16](#ga0dbc847d11cf64676f7cfc51b54150fa)(a, b) |
|  | Define HID Usage Minimum item with the data length of two bytes. |
| #define | [HID\_USAGE\_MAX16](#gadd11a09546bc275c82e7a992cb9441cc)(a, b) |
|  | Define HID Usage Maximum item with the data length of two bytes. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gad010ed98662b0e653754caff1dfd352f)HID\_COLLECTION

| #define HID\_COLLECTION | ( |  | *a* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hid.h](hid_8h.md)>`

**Value:**

[HID\_ITEM](#ga4e9dc6652402e0b87e1313c143737ed4)([HID\_ITEM\_TAG\_COLLECTION](group__usb__hid__definitions.md#ga2c06052593b060466f4c338a88319485), [HID\_ITEM\_TYPE\_MAIN](group__usb__hid__definitions.md#ga9a71248c522943951b5af70ec9c14c02), 1), a

[HID\_ITEM\_TAG\_COLLECTION](group__usb__hid__definitions.md#ga2c06052593b060466f4c338a88319485)

#define HID\_ITEM\_TAG\_COLLECTION

HID Collection item tag.

**Definition** hid.h:82

[HID\_ITEM\_TYPE\_MAIN](group__usb__hid__definitions.md#ga9a71248c522943951b5af70ec9c14c02)

#define HID\_ITEM\_TYPE\_MAIN

HID Main item type.

**Definition** hid.h:71

[HID\_ITEM](#ga4e9dc6652402e0b87e1313c143737ed4)

#define HID\_ITEM(bTag, bType, bSize)

Define HID short item.

**Definition** hid.h:181

Define HID Collection item with the data length of one byte.

For usage examples, see [HID\_MOUSE\_REPORT\_DESC()](group__usb__hid__mk__report__desc.md#ga3696f0782268d504b0c8bb540236779f "HID_MOUSE_REPORT_DESC()"), [HID\_KEYBOARD\_REPORT\_DESC()](group__usb__hid__mk__report__desc.md#gaea973ffbe1612187c90614133956cfd6 "HID_KEYBOARD_REPORT_DESC()")

Parameters
:   | a | Collection item data |
    | --- | --- |

Returns
:   HID Collection item

## [◆ ](#ga6cd6affb9d52e0bf98c7a5c83d03a764)HID\_END\_COLLECTION

| #define HID\_END\_COLLECTION   [HID\_ITEM](#ga4e9dc6652402e0b87e1313c143737ed4)([HID\_ITEM\_TAG\_COLLECTION\_END](group__usb__hid__definitions.md#ga3f4fe1817887966f0d05aa597cd0ab79), [HID\_ITEM\_TYPE\_MAIN](group__usb__hid__definitions.md#ga9a71248c522943951b5af70ec9c14c02), 0) |
| --- |

`#include <[hid.h](hid_8h.md)>`

Define HID End Collection (non-data) item.

For usage examples, see [HID\_MOUSE\_REPORT\_DESC()](group__usb__hid__mk__report__desc.md#ga3696f0782268d504b0c8bb540236779f "HID_MOUSE_REPORT_DESC()"), [HID\_KEYBOARD\_REPORT\_DESC()](group__usb__hid__mk__report__desc.md#gaea973ffbe1612187c90614133956cfd6 "HID_KEYBOARD_REPORT_DESC()")

Returns
:   HID End Collection item

## [◆ ](#ga951a415e05e95492250d4fb43a37090d)HID\_FEATURE

| #define HID\_FEATURE | ( |  | *a* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hid.h](hid_8h.md)>`

**Value:**

[HID\_ITEM](#ga4e9dc6652402e0b87e1313c143737ed4)([HID\_ITEM\_TAG\_FEATURE](group__usb__hid__definitions.md#gaeadcca849f0a0923d9a70605c44464a6), [HID\_ITEM\_TYPE\_MAIN](group__usb__hid__definitions.md#ga9a71248c522943951b5af70ec9c14c02), 1), a

[HID\_ITEM\_TAG\_FEATURE](group__usb__hid__definitions.md#gaeadcca849f0a0923d9a70605c44464a6)

#define HID\_ITEM\_TAG\_FEATURE

HID Feature item tag.

**Definition** hid.h:84

Define HID Feature item with the data length of one byte.

Parameters
:   | a | Feature item data |
    | --- | --- |

Returns
:   HID Feature item

## [◆ ](#ga8646699330c45fb008d50b54be339c6c)HID\_INPUT

| #define HID\_INPUT | ( |  | *a* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hid.h](hid_8h.md)>`

**Value:**

[HID\_ITEM](#ga4e9dc6652402e0b87e1313c143737ed4)([HID\_ITEM\_TAG\_INPUT](group__usb__hid__definitions.md#ga66e1c50fe814fd05d61dce12ce3888c1), [HID\_ITEM\_TYPE\_MAIN](group__usb__hid__definitions.md#ga9a71248c522943951b5af70ec9c14c02), 1), a

[HID\_ITEM\_TAG\_INPUT](group__usb__hid__definitions.md#ga66e1c50fe814fd05d61dce12ce3888c1)

#define HID\_ITEM\_TAG\_INPUT

HID Input item tag.

**Definition** hid.h:78

Define HID Input item with the data length of one byte.

For usage examples, see [HID\_MOUSE\_REPORT\_DESC()](group__usb__hid__mk__report__desc.md#ga3696f0782268d504b0c8bb540236779f "HID_MOUSE_REPORT_DESC()"), [HID\_KEYBOARD\_REPORT\_DESC()](group__usb__hid__mk__report__desc.md#gaea973ffbe1612187c90614133956cfd6 "HID_KEYBOARD_REPORT_DESC()")

Parameters
:   | a | Input item data |
    | --- | --- |

Returns
:   HID Input item

## [◆ ](#ga4e9dc6652402e0b87e1313c143737ed4)HID\_ITEM

| #define HID\_ITEM | ( |  | *bTag*, |
| --- | --- | --- | --- |
|  |  |  | *bType*, |
|  |  |  | *bSize* ) |

`#include <[hid.h](hid_8h.md)>`

**Value:**

(((bTag & 0xF) << 4) | \

((bType & 0x3) << 2) | (bSize & 0x3))

Define HID short item.

Parameters
:   | bTag | Item tag |
    | --- | --- |
    | bType | Item type |
    | bSize | Item data size |

Returns
:   HID Input item

## [◆ ](#ga9b804d676812dcfb0ec12f3aa887e37f)HID\_LOGICAL\_MAX16

| #define HID\_LOGICAL\_MAX16 | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *b* ) |

`#include <[hid.h](hid_8h.md)>`

**Value:**

[HID\_ITEM](#ga4e9dc6652402e0b87e1313c143737ed4)([HID\_ITEM\_TAG\_LOGICAL\_MAX](group__usb__hid__definitions.md#gaab6aec72cca41670464605d6970ad553), [HID\_ITEM\_TYPE\_GLOBAL](group__usb__hid__definitions.md#ga8e56e8090f1af7aae473e8a8b6832fb8), 2), a, b

[HID\_ITEM\_TYPE\_GLOBAL](group__usb__hid__definitions.md#ga8e56e8090f1af7aae473e8a8b6832fb8)

#define HID\_ITEM\_TYPE\_GLOBAL

HID Global item type.

**Definition** hid.h:73

[HID\_ITEM\_TAG\_LOGICAL\_MAX](group__usb__hid__definitions.md#gaab6aec72cca41670464605d6970ad553)

#define HID\_ITEM\_TAG\_LOGICAL\_MAX

HID Logical Maximum item tag.

**Definition** hid.h:93

Define HID Logical Maximum item with the data length of two bytes.

Parameters
:   | a | Minimum value lower byte |
    | --- | --- |
    | b | Minimum value higher byte |

Returns
:   HID Logical Maximum item

## [◆ ](#gae9d17e753685b0df6c53f942ce9c95d2)HID\_LOGICAL\_MAX32

| #define HID\_LOGICAL\_MAX32 | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *b*, |
|  |  |  | *c*, |
|  |  |  | *[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)* ) |

`#include <[hid.h](hid_8h.md)>`

**Value:**

[HID\_ITEM](#ga4e9dc6652402e0b87e1313c143737ed4)([HID\_ITEM\_TAG\_LOGICAL\_MAX](group__usb__hid__definitions.md#gaab6aec72cca41670464605d6970ad553), [HID\_ITEM\_TYPE\_GLOBAL](group__usb__hid__definitions.md#ga8e56e8090f1af7aae473e8a8b6832fb8), 3), a, b, c, [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)

[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)

irp nz macro MOVR cc d

**Definition** asm-macro-32-bit-gnu.h:11

Define HID Logical Maximum item with the data length of four bytes.

Parameters
:   | a | Minimum value lower byte |
    | --- | --- |
    | b | Minimum value low middle byte |
    | c | Minimum value high middle byte |
    | [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417) | Minimum value higher byte |

Returns
:   HID Logical Maximum item

## [◆ ](#ga2f6b809ae85b6716ade8c52da4fa56af)HID\_LOGICAL\_MAX8

| #define HID\_LOGICAL\_MAX8 | ( |  | *a* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hid.h](hid_8h.md)>`

**Value:**

[HID\_ITEM](#ga4e9dc6652402e0b87e1313c143737ed4)([HID\_ITEM\_TAG\_LOGICAL\_MAX](group__usb__hid__definitions.md#gaab6aec72cca41670464605d6970ad553), [HID\_ITEM\_TYPE\_GLOBAL](group__usb__hid__definitions.md#ga8e56e8090f1af7aae473e8a8b6832fb8), 1), a

Define HID Logical Maximum item with the data length of one byte.

For usage examples, see [HID\_MOUSE\_REPORT\_DESC()](group__usb__hid__mk__report__desc.md#ga3696f0782268d504b0c8bb540236779f "HID_MOUSE_REPORT_DESC()"), [HID\_KEYBOARD\_REPORT\_DESC()](group__usb__hid__mk__report__desc.md#gaea973ffbe1612187c90614133956cfd6 "HID_KEYBOARD_REPORT_DESC()")

Parameters
:   | a | Maximum value in logical units |
    | --- | --- |

Returns
:   HID Logical Maximum item

## [◆ ](#ga5e290798d55bccd7474dbfb6bc2d1033)HID\_LOGICAL\_MIN16

| #define HID\_LOGICAL\_MIN16 | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *b* ) |

`#include <[hid.h](hid_8h.md)>`

**Value:**

[HID\_ITEM](#ga4e9dc6652402e0b87e1313c143737ed4)([HID\_ITEM\_TAG\_LOGICAL\_MIN](group__usb__hid__definitions.md#ga034033b1ae6f4677aef82d4243c6f712), [HID\_ITEM\_TYPE\_GLOBAL](group__usb__hid__definitions.md#ga8e56e8090f1af7aae473e8a8b6832fb8), 2), a, b

[HID\_ITEM\_TAG\_LOGICAL\_MIN](group__usb__hid__definitions.md#ga034033b1ae6f4677aef82d4243c6f712)

#define HID\_ITEM\_TAG\_LOGICAL\_MIN

HID Logical Minimum item tag.

**Definition** hid.h:91

Define HID Logical Minimum item with the data length of two bytes.

Parameters
:   | a | Minimum value lower byte |
    | --- | --- |
    | b | Minimum value higher byte |

Returns
:   HID Logical Minimum item

## [◆ ](#gad4b2ff8642676d692fd0d56ab0cbeaa7)HID\_LOGICAL\_MIN32

| #define HID\_LOGICAL\_MIN32 | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *b*, |
|  |  |  | *c*, |
|  |  |  | *[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)* ) |

`#include <[hid.h](hid_8h.md)>`

**Value:**

[HID\_ITEM](#ga4e9dc6652402e0b87e1313c143737ed4)([HID\_ITEM\_TAG\_LOGICAL\_MIN](group__usb__hid__definitions.md#ga034033b1ae6f4677aef82d4243c6f712), [HID\_ITEM\_TYPE\_GLOBAL](group__usb__hid__definitions.md#ga8e56e8090f1af7aae473e8a8b6832fb8), 3), a, b, c, [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)

Define HID Logical Minimum item with the data length of four bytes.

Parameters
:   | a | Minimum value lower byte |
    | --- | --- |
    | b | Minimum value low middle byte |
    | c | Minimum value high middle byte |
    | [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417) | Minimum value higher byte |

Returns
:   HID Logical Minimum item

## [◆ ](#gacd141f6ede5122f260cd50338649d458)HID\_LOGICAL\_MIN8

| #define HID\_LOGICAL\_MIN8 | ( |  | *a* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hid.h](hid_8h.md)>`

**Value:**

[HID\_ITEM](#ga4e9dc6652402e0b87e1313c143737ed4)([HID\_ITEM\_TAG\_LOGICAL\_MIN](group__usb__hid__definitions.md#ga034033b1ae6f4677aef82d4243c6f712), [HID\_ITEM\_TYPE\_GLOBAL](group__usb__hid__definitions.md#ga8e56e8090f1af7aae473e8a8b6832fb8), 1), a

Define HID Logical Minimum item with the data length of one byte.

For usage examples, see [HID\_MOUSE\_REPORT\_DESC()](group__usb__hid__mk__report__desc.md#ga3696f0782268d504b0c8bb540236779f "HID_MOUSE_REPORT_DESC()"), [HID\_KEYBOARD\_REPORT\_DESC()](group__usb__hid__mk__report__desc.md#gaea973ffbe1612187c90614133956cfd6 "HID_KEYBOARD_REPORT_DESC()")

Parameters
:   | a | Minimum value in logical units |
    | --- | --- |

Returns
:   HID Logical Minimum item

## [◆ ](#ga6ef7aa576bf69f9ba5f93df500a1403c)HID\_OUTPUT

| #define HID\_OUTPUT | ( |  | *a* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hid.h](hid_8h.md)>`

**Value:**

[HID\_ITEM](#ga4e9dc6652402e0b87e1313c143737ed4)([HID\_ITEM\_TAG\_OUTPUT](group__usb__hid__definitions.md#ga70c32518a6b538831e821ad30022679b), [HID\_ITEM\_TYPE\_MAIN](group__usb__hid__definitions.md#ga9a71248c522943951b5af70ec9c14c02), 1), a

[HID\_ITEM\_TAG\_OUTPUT](group__usb__hid__definitions.md#ga70c32518a6b538831e821ad30022679b)

#define HID\_ITEM\_TAG\_OUTPUT

HID Output item tag.

**Definition** hid.h:80

Define HID Output item with the data length of one byte.

For usage examples, see [HID\_KEYBOARD\_REPORT\_DESC()](group__usb__hid__mk__report__desc.md#gaea973ffbe1612187c90614133956cfd6 "HID_KEYBOARD_REPORT_DESC()")

Parameters
:   | a | Output item data |
    | --- | --- |

Returns
:   HID Output item

## [◆ ](#ga71192f2a55f05456b893069ebfbc5b98)HID\_REPORT\_COUNT

| #define HID\_REPORT\_COUNT | ( |  | *count* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hid.h](hid_8h.md)>`

**Value:**

[HID\_ITEM](#ga4e9dc6652402e0b87e1313c143737ed4)([HID\_ITEM\_TAG\_REPORT\_COUNT](group__usb__hid__definitions.md#ga1847701703130ce8f57547811f28b2b4), [HID\_ITEM\_TYPE\_GLOBAL](group__usb__hid__definitions.md#ga8e56e8090f1af7aae473e8a8b6832fb8), 1), count

[HID\_ITEM\_TAG\_REPORT\_COUNT](group__usb__hid__definitions.md#ga1847701703130ce8f57547811f28b2b4)

#define HID\_ITEM\_TAG\_REPORT\_COUNT

HID Report count item tag.

**Definition** hid.h:107

Define HID Report Count item with the data length of one byte.

For usage examples, see [HID\_MOUSE\_REPORT\_DESC()](group__usb__hid__mk__report__desc.md#ga3696f0782268d504b0c8bb540236779f "HID_MOUSE_REPORT_DESC()"), [HID\_KEYBOARD\_REPORT\_DESC()](group__usb__hid__mk__report__desc.md#gaea973ffbe1612187c90614133956cfd6 "HID_KEYBOARD_REPORT_DESC()")

Parameters
:   | count | Number of data fields included in the report |
    | --- | --- |

Returns
:   HID Report Count item

## [◆ ](#ga1b45fce2c7df2847b1326fca29cef389)HID\_REPORT\_ID

| #define HID\_REPORT\_ID | ( |  | *id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hid.h](hid_8h.md)>`

**Value:**

[HID\_ITEM](#ga4e9dc6652402e0b87e1313c143737ed4)([HID\_ITEM\_TAG\_REPORT\_ID](group__usb__hid__definitions.md#ga76cd3a266ae5d5e29292d93caceece72), [HID\_ITEM\_TYPE\_GLOBAL](group__usb__hid__definitions.md#ga8e56e8090f1af7aae473e8a8b6832fb8), 1), id

[HID\_ITEM\_TAG\_REPORT\_ID](group__usb__hid__definitions.md#ga76cd3a266ae5d5e29292d93caceece72)

#define HID\_ITEM\_TAG\_REPORT\_ID

HID Report ID item tag.

**Definition** hid.h:105

Define HID Report ID item with the data length of one byte.

Parameters
:   | id | Report ID |
    | --- | --- |

Returns
:   HID Report ID item

## [◆ ](#ga3135a21a63c491daf8647fa771def0e7)HID\_REPORT\_SIZE

| #define HID\_REPORT\_SIZE | ( |  | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hid.h](hid_8h.md)>`

**Value:**

[HID\_ITEM](#ga4e9dc6652402e0b87e1313c143737ed4)([HID\_ITEM\_TAG\_REPORT\_SIZE](group__usb__hid__definitions.md#ga0e6d7a56593bd25a5e15683e9271bb19), [HID\_ITEM\_TYPE\_GLOBAL](group__usb__hid__definitions.md#ga8e56e8090f1af7aae473e8a8b6832fb8), 1), size

[HID\_ITEM\_TAG\_REPORT\_SIZE](group__usb__hid__definitions.md#ga0e6d7a56593bd25a5e15683e9271bb19)

#define HID\_ITEM\_TAG\_REPORT\_SIZE

HID Report Size item tag.

**Definition** hid.h:103

Define HID Report Size item with the data length of one byte.

For usage examples, see [HID\_MOUSE\_REPORT\_DESC()](group__usb__hid__mk__report__desc.md#ga3696f0782268d504b0c8bb540236779f "HID_MOUSE_REPORT_DESC()"), [HID\_KEYBOARD\_REPORT\_DESC()](group__usb__hid__mk__report__desc.md#gaea973ffbe1612187c90614133956cfd6 "HID_KEYBOARD_REPORT_DESC()")

Parameters
:   | size | Report field size in bits |
    | --- | --- |

Returns
:   HID Report Size item

## [◆ ](#gac8429a70866a898887ead55664e04bd7)HID\_USAGE

| #define HID\_USAGE | ( |  | *idx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hid.h](hid_8h.md)>`

**Value:**

[HID\_ITEM](#ga4e9dc6652402e0b87e1313c143737ed4)([HID\_ITEM\_TAG\_USAGE](group__usb__hid__definitions.md#gaefd616ecaa8fc8762e65ec9d7b01f0cd), [HID\_ITEM\_TYPE\_LOCAL](group__usb__hid__definitions.md#ga0bfb0e326d9a01072c029cba788d6456), 1), idx

[HID\_ITEM\_TYPE\_LOCAL](group__usb__hid__definitions.md#ga0bfb0e326d9a01072c029cba788d6456)

#define HID\_ITEM\_TYPE\_LOCAL

HID Local item type.

**Definition** hid.h:75

[HID\_ITEM\_TAG\_USAGE](group__usb__hid__definitions.md#gaefd616ecaa8fc8762e65ec9d7b01f0cd)

#define HID\_ITEM\_TAG\_USAGE

HID Usage item tag.

**Definition** hid.h:110

Define HID Usage Index item with the data length of one byte.

For usage examples, see [HID\_MOUSE\_REPORT\_DESC()](group__usb__hid__mk__report__desc.md#ga3696f0782268d504b0c8bb540236779f "HID_MOUSE_REPORT_DESC()"), [HID\_KEYBOARD\_REPORT\_DESC()](group__usb__hid__mk__report__desc.md#gaea973ffbe1612187c90614133956cfd6 "HID_KEYBOARD_REPORT_DESC()")

Parameters
:   | idx | Number of data fields included in the report |
    | --- | --- |

Returns
:   HID Usage Index item

## [◆ ](#gadd11a09546bc275c82e7a992cb9441cc)HID\_USAGE\_MAX16

| #define HID\_USAGE\_MAX16 | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *b* ) |

`#include <[hid.h](hid_8h.md)>`

**Value:**

[HID\_ITEM](#ga4e9dc6652402e0b87e1313c143737ed4)([HID\_ITEM\_TAG\_USAGE\_MAX](group__usb__hid__definitions.md#gac2a0aff74caff6c03511fc0b6db6167b), [HID\_ITEM\_TYPE\_LOCAL](group__usb__hid__definitions.md#ga0bfb0e326d9a01072c029cba788d6456), 2), a, b

[HID\_ITEM\_TAG\_USAGE\_MAX](group__usb__hid__definitions.md#gac2a0aff74caff6c03511fc0b6db6167b)

#define HID\_ITEM\_TAG\_USAGE\_MAX

HID Usage Maximum item tag.

**Definition** hid.h:114

Define HID Usage Maximum item with the data length of two bytes.

For usage examples, see [HID\_MOUSE\_REPORT\_DESC()](group__usb__hid__mk__report__desc.md#ga3696f0782268d504b0c8bb540236779f "HID_MOUSE_REPORT_DESC()"), [HID\_KEYBOARD\_REPORT\_DESC()](group__usb__hid__mk__report__desc.md#gaea973ffbe1612187c90614133956cfd6 "HID_KEYBOARD_REPORT_DESC()")

Parameters
:   | a | Ending Usage lower byte |
    | --- | --- |
    | b | Ending Usage higher byte |

Returns
:   HID Usage Maximum item

## [◆ ](#gae7fc9684ef10f50d69df6f495cc09e91)HID\_USAGE\_MAX8

| #define HID\_USAGE\_MAX8 | ( |  | *a* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hid.h](hid_8h.md)>`

**Value:**

[HID\_ITEM](#ga4e9dc6652402e0b87e1313c143737ed4)([HID\_ITEM\_TAG\_USAGE\_MAX](group__usb__hid__definitions.md#gac2a0aff74caff6c03511fc0b6db6167b), [HID\_ITEM\_TYPE\_LOCAL](group__usb__hid__definitions.md#ga0bfb0e326d9a01072c029cba788d6456), 1), a

Define HID Usage Maximum item with the data length of one byte.

For usage examples, see [HID\_MOUSE\_REPORT\_DESC()](group__usb__hid__mk__report__desc.md#ga3696f0782268d504b0c8bb540236779f "HID_MOUSE_REPORT_DESC()"), [HID\_KEYBOARD\_REPORT\_DESC()](group__usb__hid__mk__report__desc.md#gaea973ffbe1612187c90614133956cfd6 "HID_KEYBOARD_REPORT_DESC()")

Parameters
:   | a | Ending Usage |
    | --- | --- |

Returns
:   HID Usage Maximum item

## [◆ ](#ga0dbc847d11cf64676f7cfc51b54150fa)HID\_USAGE\_MIN16

| #define HID\_USAGE\_MIN16 | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *b* ) |

`#include <[hid.h](hid_8h.md)>`

**Value:**

[HID\_ITEM](#ga4e9dc6652402e0b87e1313c143737ed4)([HID\_ITEM\_TAG\_USAGE\_MIN](group__usb__hid__definitions.md#ga4e6f4133f12276f4f9fa51ab06580676), [HID\_ITEM\_TYPE\_LOCAL](group__usb__hid__definitions.md#ga0bfb0e326d9a01072c029cba788d6456), 2), a, b

[HID\_ITEM\_TAG\_USAGE\_MIN](group__usb__hid__definitions.md#ga4e6f4133f12276f4f9fa51ab06580676)

#define HID\_ITEM\_TAG\_USAGE\_MIN

HID Usage Minimum item tag.

**Definition** hid.h:112

Define HID Usage Minimum item with the data length of two bytes.

For usage examples, see [HID\_MOUSE\_REPORT\_DESC()](group__usb__hid__mk__report__desc.md#ga3696f0782268d504b0c8bb540236779f "HID_MOUSE_REPORT_DESC()"), [HID\_KEYBOARD\_REPORT\_DESC()](group__usb__hid__mk__report__desc.md#gaea973ffbe1612187c90614133956cfd6 "HID_KEYBOARD_REPORT_DESC()")

Parameters
:   | a | Starting Usage lower byte |
    | --- | --- |
    | b | Starting Usage higher byte |

Returns
:   HID Usage Minimum item

## [◆ ](#gabf53f1e2eae6d686aeb7d62cc46b22ad)HID\_USAGE\_MIN8

| #define HID\_USAGE\_MIN8 | ( |  | *a* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hid.h](hid_8h.md)>`

**Value:**

[HID\_ITEM](#ga4e9dc6652402e0b87e1313c143737ed4)([HID\_ITEM\_TAG\_USAGE\_MIN](group__usb__hid__definitions.md#ga4e6f4133f12276f4f9fa51ab06580676), [HID\_ITEM\_TYPE\_LOCAL](group__usb__hid__definitions.md#ga0bfb0e326d9a01072c029cba788d6456), 1), a

Define HID Usage Minimum item with the data length of one byte.

For usage examples, see [HID\_MOUSE\_REPORT\_DESC()](group__usb__hid__mk__report__desc.md#ga3696f0782268d504b0c8bb540236779f "HID_MOUSE_REPORT_DESC()"), [HID\_KEYBOARD\_REPORT\_DESC()](group__usb__hid__mk__report__desc.md#gaea973ffbe1612187c90614133956cfd6 "HID_KEYBOARD_REPORT_DESC()")

Parameters
:   | a | Starting Usage |
    | --- | --- |

Returns
:   HID Usage Minimum item

## [◆ ](#ga30dc3f62583822ba27edd984dc2dec39)HID\_USAGE\_PAGE

| #define HID\_USAGE\_PAGE | ( |  | *page* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hid.h](hid_8h.md)>`

**Value:**

[HID\_ITEM](#ga4e9dc6652402e0b87e1313c143737ed4)([HID\_ITEM\_TAG\_USAGE\_PAGE](group__usb__hid__definitions.md#ga73f58fa37c0bf6698463b9d31c8a511f), [HID\_ITEM\_TYPE\_GLOBAL](group__usb__hid__definitions.md#ga8e56e8090f1af7aae473e8a8b6832fb8), 1), page

[HID\_ITEM\_TAG\_USAGE\_PAGE](group__usb__hid__definitions.md#ga73f58fa37c0bf6698463b9d31c8a511f)

#define HID\_ITEM\_TAG\_USAGE\_PAGE

HID Usage Page item tag.

**Definition** hid.h:89

Define HID Usage Page item.

For usage examples, see [HID\_MOUSE\_REPORT\_DESC()](group__usb__hid__mk__report__desc.md#ga3696f0782268d504b0c8bb540236779f "HID_MOUSE_REPORT_DESC()"), [HID\_KEYBOARD\_REPORT\_DESC()](group__usb__hid__mk__report__desc.md#gaea973ffbe1612187c90614133956cfd6 "HID_KEYBOARD_REPORT_DESC()")

Parameters
:   | page | Usage Page |
    | --- | --- |

Returns
:   HID Usage Page item

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

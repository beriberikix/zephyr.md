---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__usb__hid__definitions.html
original_path: doxygen/html/group__usb__hid__definitions.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

USB HID common definitions

[Connectivity](group__connectivity.md) » [USB](group__usb.md)

[hid.h](hid_8h.md "USB Human Interface Device (HID) common definitions header.") API
[More...](#details)

| Topics | |
| --- | --- |
|  | [Mouse and keyboard report descriptors](group__usb__hid__mk__report__desc.md) |
|  | [USB HID Item helpers](group__usb__hid__items.md) |

| USB HID types and values | |
| --- | --- |
| #define | [USB\_HID\_VERSION](#ga77f649cbc5ab446b2cfe3e68eb88ac91)   0x0111 |
|  | HID Specification release v1.11. |
| #define | [USB\_DESC\_HID](#ga07e8028979ff1c3d30408b08778bfd3d)   0x21 |
|  | USB HID Class HID descriptor type. |
| #define | [USB\_DESC\_HID\_REPORT](#gaca594a2caf9cb5ebac863c6c2f233f31)   0x22 |
|  | USB HID Class Report descriptor type. |
| #define | [USB\_DESC\_HID\_PHYSICAL](#ga2d543337d798d1c85436d2fee1c5be3f)   0x23 |
|  | USB HID Class physical descriptor type. |
| #define | [USB\_HID\_GET\_REPORT](#ga3d4f67db0b3531f3493cde381110809d)   0x01 |
|  | USB HID Class GetReport bRequest value. |
| #define | [USB\_HID\_GET\_IDLE](#ga9d69e0dae00cf3c6c5dc5602f63b2f2f)   0x02 |
|  | USB HID Class GetIdle bRequest value. |
| #define | [USB\_HID\_GET\_PROTOCOL](#ga09469e20036a4c3df8281a2575358747)   0x03 |
|  | USB HID Class GetProtocol bRequest value. |
| #define | [USB\_HID\_SET\_REPORT](#gaed6de2caf14f9caa049fab82902299cf)   0x09 |
|  | USB HID Class SetReport bRequest value. |
| #define | [USB\_HID\_SET\_IDLE](#ga1cbc5f99d9bd85fca7b9a624efb41078)   0x0A |
|  | USB HID Class SetIdle bRequest value. |
| #define | [USB\_HID\_SET\_PROTOCOL](#ga2058ed723b6a4613b4dcb8040b739684)   0x0B |
|  | USB HID Class SetProtocol bRequest value. |
| #define | [HID\_BOOT\_IFACE\_CODE\_NONE](#ga953074178d707cd3538da80f36a96ff6)   0 |
|  | USB HID Boot Interface Protocol (bInterfaceProtocol) Code None. |
| #define | [HID\_BOOT\_IFACE\_CODE\_KEYBOARD](#ga6e6276ae88c414e10c602d5e041738ab)   1 |
|  | USB HID Boot Interface Protocol (bInterfaceProtocol) Code Keyboard. |
| #define | [HID\_BOOT\_IFACE\_CODE\_MOUSE](#ga900873d4834ea511a08b08debe62bedf)   2 |
|  | USB HID Boot Interface Protocol (bInterfaceProtocol) Code Mouse. |
| #define | [HID\_PROTOCOL\_BOOT](#gafd24e87747c82293e689f58157f06128)   0 |
|  | USB HID Class Boot protocol code. |
| #define | [HID\_PROTOCOL\_REPORT](#ga982c0da911cbda6e09bd48a5e4ab85f1)   1 |
|  | USB HID Class Report protocol code. |
| #define | [HID\_ITEM\_TYPE\_MAIN](#ga9a71248c522943951b5af70ec9c14c02)   0x0 |
|  | HID Main item type. |
| #define | [HID\_ITEM\_TYPE\_GLOBAL](#ga8e56e8090f1af7aae473e8a8b6832fb8)   0x1 |
|  | HID Global item type. |
| #define | [HID\_ITEM\_TYPE\_LOCAL](#ga0bfb0e326d9a01072c029cba788d6456)   0x2 |
|  | HID Local item type. |
| #define | [HID\_ITEM\_TAG\_INPUT](#ga66e1c50fe814fd05d61dce12ce3888c1)   0x8 |
|  | HID Input item tag. |
| #define | [HID\_ITEM\_TAG\_OUTPUT](#ga70c32518a6b538831e821ad30022679b)   0x9 |
|  | HID Output item tag. |
| #define | [HID\_ITEM\_TAG\_COLLECTION](#ga2c06052593b060466f4c338a88319485)   0xA |
|  | HID Collection item tag. |
| #define | [HID\_ITEM\_TAG\_FEATURE](#gaeadcca849f0a0923d9a70605c44464a6)   0xB |
|  | HID Feature item tag. |
| #define | [HID\_ITEM\_TAG\_COLLECTION\_END](#ga3f4fe1817887966f0d05aa597cd0ab79)   0xC |
|  | HID End Collection item tag. |
| #define | [HID\_ITEM\_TAG\_USAGE\_PAGE](#ga73f58fa37c0bf6698463b9d31c8a511f)   0x0 |
|  | HID Usage Page item tag. |
| #define | [HID\_ITEM\_TAG\_LOGICAL\_MIN](#ga034033b1ae6f4677aef82d4243c6f712)   0x1 |
|  | HID Logical Minimum item tag. |
| #define | [HID\_ITEM\_TAG\_LOGICAL\_MAX](#gaab6aec72cca41670464605d6970ad553)   0x2 |
|  | HID Logical Maximum item tag. |
| #define | [HID\_ITEM\_TAG\_PHYSICAL\_MIN](#ga6dfdd60d0b985d683a58ad752d3ef3c3)   0x3 |
|  | HID Physical Minimum item tag. |
| #define | [HID\_ITEM\_TAG\_PHYSICAL\_MAX](#gaa68bd8a73cee33d810484f4aa3f30e92)   0x4 |
|  | HID Physical Maximum item tag. |
| #define | [HID\_ITEM\_TAG\_UNIT\_EXPONENT](#ga7c6d81ee211814ec9b5d17f95e57639b)   0x5 |
|  | HID Unit Exponent item tag. |
| #define | [HID\_ITEM\_TAG\_UNIT](#ga98267b4ff28f435d67d2a7bf1055fc7c)   0x6 |
|  | HID Unit item tag. |
| #define | [HID\_ITEM\_TAG\_REPORT\_SIZE](#ga0e6d7a56593bd25a5e15683e9271bb19)   0x7 |
|  | HID Report Size item tag. |
| #define | [HID\_ITEM\_TAG\_REPORT\_ID](#ga76cd3a266ae5d5e29292d93caceece72)   0x8 |
|  | HID Report ID item tag. |
| #define | [HID\_ITEM\_TAG\_REPORT\_COUNT](#ga1847701703130ce8f57547811f28b2b4)   0x9 |
|  | HID Report count item tag. |
| #define | [HID\_ITEM\_TAG\_USAGE](#gaefd616ecaa8fc8762e65ec9d7b01f0cd)   0x0 |
|  | HID Usage item tag. |
| #define | [HID\_ITEM\_TAG\_USAGE\_MIN](#ga4e6f4133f12276f4f9fa51ab06580676)   0x1 |
|  | HID Usage Minimum item tag. |
| #define | [HID\_ITEM\_TAG\_USAGE\_MAX](#gac2a0aff74caff6c03511fc0b6db6167b)   0x2 |
|  | HID Usage Maximum item tag. |
| #define | [HID\_COLLECTION\_PHYSICAL](#gaca1e227f9241c217b8b1aeae6c4bd672)   0x00 |
|  | Physical collection type. |
| #define | [HID\_COLLECTION\_APPLICATION](#ga2e5e5ad0919fbaea0e6f8e5d86f4c2fd)   0x01 |
|  | Application collection type. |
| #define | [HID\_COLLECTION\_LOGICAL](#ga904a372a663bd7d9205402a3a014c04b)   0x02 |
|  | Logical collection type. |
| #define | [HID\_COLLECTION\_REPORT](#gac58ab4780c054754b7f94ff97a152694)   0x03 |
|  | Report collection type. |
| #define | [HID\_COLLECTION\_NAMED\_ARRAY](#ga8e1610365a1556adf7121cc3b1f83080)   0x04 |
|  | Named Array collection type. |
| #define | [HID\_COLLECTION\_USAGE\_SWITCH](#ga64af797e424ea1e2c02c745f30721e48)   0x05 |
|  | Usage Switch collection type. |
| #define | [HID\_COLLECTION\_MODIFIER](#gaabc1c6bed23b88f4cdc89d5347595d4f)   0x06 |
|  | Modifier collection type. |
| #define | [HID\_USAGE\_GEN\_DESKTOP](#gacb3fc5b0f838dfa5eb95e9e1bf52b589)   0x01 |
|  | HID Generic Desktop Controls Usage page. |
| #define | [HID\_USAGE\_GEN\_KEYBOARD](#ga1fdbfffd0b343cec1480e9f0347efa5d)   0x07 |
|  | HID Keyboard Usage page. |
| #define | [HID\_USAGE\_GEN\_LEDS](#gae632e9a37203506c051c3cacfdf0c2c7)   0x08 |
|  | HID LEDs Usage page. |
| #define | [HID\_USAGE\_GEN\_BUTTON](#ga13401731a0ead5448a0823d0f6142404)   0x09 |
|  | HID Button Usage page. |
| #define | [HID\_USAGE\_GEN\_DESKTOP\_UNDEFINED](#ga1441517d7c57529dcf726a1dd8b09a07)   0x00 |
|  | HID Generic Desktop Undefined Usage ID. |
| #define | [HID\_USAGE\_GEN\_DESKTOP\_POINTER](#ga77a7162980a77efa1e2e7b21942bb7dd)   0x01 |
|  | HID Generic Desktop Pointer Usage ID. |
| #define | [HID\_USAGE\_GEN\_DESKTOP\_MOUSE](#ga983274dd50058de26e0e86d10d50e81a)   0x02 |
|  | HID Generic Desktop Mouse Usage ID. |
| #define | [HID\_USAGE\_GEN\_DESKTOP\_JOYSTICK](#gada59a9f3aeaeaefc6112c7d9902b2d6d)   0x04 |
|  | HID Generic Desktop Joystick Usage ID. |
| #define | [HID\_USAGE\_GEN\_DESKTOP\_GAMEPAD](#ga17404e33133204a538f976d321c84ff0)   0x05 |
|  | HID Generic Desktop Gamepad Usage ID. |
| #define | [HID\_USAGE\_GEN\_DESKTOP\_KEYBOARD](#ga0bdaa3d23c79204a1064cb53b279bd77)   0x06 |
|  | HID Generic Desktop Keyboard Usage ID. |
| #define | [HID\_USAGE\_GEN\_DESKTOP\_KEYPAD](#ga69f8e44306828b3f44d3a7704ff07807)   0x07 |
|  | HID Generic Desktop Keypad Usage ID. |
| #define | [HID\_USAGE\_GEN\_DESKTOP\_X](#gae283a3558ba536e163140a3b6cdbb273)   0x30 |
|  | HID Generic Desktop X Usage ID. |
| #define | [HID\_USAGE\_GEN\_DESKTOP\_Y](#gad1ab1f8f9c8a4a80bfc8e3a327e3b2fb)   0x31 |
|  | HID Generic Desktop Y Usage ID. |
| #define | [HID\_USAGE\_GEN\_DESKTOP\_WHEEL](#gaa8c772d412ac1ac7a36739c52f04c0a9)   0x38 |
|  | HID Generic Desktop Wheel Usage ID. |

## Detailed Description

[hid.h](hid_8h.md "USB Human Interface Device (HID) common definitions header.") API

Since
:   1.11

Version
:   1.0.0

## Macro Definition Documentation

## [◆ ](#ga6e6276ae88c414e10c602d5e041738ab)HID\_BOOT\_IFACE\_CODE\_KEYBOARD

| #define HID\_BOOT\_IFACE\_CODE\_KEYBOARD   1 |
| --- |

`#include <[hid.h](hid_8h.md)>`

USB HID Boot Interface Protocol (bInterfaceProtocol) Code Keyboard.

## [◆ ](#ga900873d4834ea511a08b08debe62bedf)HID\_BOOT\_IFACE\_CODE\_MOUSE

| #define HID\_BOOT\_IFACE\_CODE\_MOUSE   2 |
| --- |

`#include <[hid.h](hid_8h.md)>`

USB HID Boot Interface Protocol (bInterfaceProtocol) Code Mouse.

## [◆ ](#ga953074178d707cd3538da80f36a96ff6)HID\_BOOT\_IFACE\_CODE\_NONE

| #define HID\_BOOT\_IFACE\_CODE\_NONE   0 |
| --- |

`#include <[hid.h](hid_8h.md)>`

USB HID Boot Interface Protocol (bInterfaceProtocol) Code None.

## [◆ ](#ga2e5e5ad0919fbaea0e6f8e5d86f4c2fd)HID\_COLLECTION\_APPLICATION

| #define HID\_COLLECTION\_APPLICATION   0x01 |
| --- |

`#include <[hid.h](hid_8h.md)>`

Application collection type.

## [◆ ](#ga904a372a663bd7d9205402a3a014c04b)HID\_COLLECTION\_LOGICAL

| #define HID\_COLLECTION\_LOGICAL   0x02 |
| --- |

`#include <[hid.h](hid_8h.md)>`

Logical collection type.

## [◆ ](#gaabc1c6bed23b88f4cdc89d5347595d4f)HID\_COLLECTION\_MODIFIER

| #define HID\_COLLECTION\_MODIFIER   0x06 |
| --- |

`#include <[hid.h](hid_8h.md)>`

Modifier collection type.

## [◆ ](#ga8e1610365a1556adf7121cc3b1f83080)HID\_COLLECTION\_NAMED\_ARRAY

| #define HID\_COLLECTION\_NAMED\_ARRAY   0x04 |
| --- |

`#include <[hid.h](hid_8h.md)>`

Named Array collection type.

## [◆ ](#gaca1e227f9241c217b8b1aeae6c4bd672)HID\_COLLECTION\_PHYSICAL

| #define HID\_COLLECTION\_PHYSICAL   0x00 |
| --- |

`#include <[hid.h](hid_8h.md)>`

Physical collection type.

## [◆ ](#gac58ab4780c054754b7f94ff97a152694)HID\_COLLECTION\_REPORT

| #define HID\_COLLECTION\_REPORT   0x03 |
| --- |

`#include <[hid.h](hid_8h.md)>`

Report collection type.

## [◆ ](#ga64af797e424ea1e2c02c745f30721e48)HID\_COLLECTION\_USAGE\_SWITCH

| #define HID\_COLLECTION\_USAGE\_SWITCH   0x05 |
| --- |

`#include <[hid.h](hid_8h.md)>`

Usage Switch collection type.

## [◆ ](#ga2c06052593b060466f4c338a88319485)HID\_ITEM\_TAG\_COLLECTION

| #define HID\_ITEM\_TAG\_COLLECTION   0xA |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Collection item tag.

## [◆ ](#ga3f4fe1817887966f0d05aa597cd0ab79)HID\_ITEM\_TAG\_COLLECTION\_END

| #define HID\_ITEM\_TAG\_COLLECTION\_END   0xC |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID End Collection item tag.

## [◆ ](#gaeadcca849f0a0923d9a70605c44464a6)HID\_ITEM\_TAG\_FEATURE

| #define HID\_ITEM\_TAG\_FEATURE   0xB |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Feature item tag.

## [◆ ](#ga66e1c50fe814fd05d61dce12ce3888c1)HID\_ITEM\_TAG\_INPUT

| #define HID\_ITEM\_TAG\_INPUT   0x8 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Input item tag.

## [◆ ](#gaab6aec72cca41670464605d6970ad553)HID\_ITEM\_TAG\_LOGICAL\_MAX

| #define HID\_ITEM\_TAG\_LOGICAL\_MAX   0x2 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Logical Maximum item tag.

## [◆ ](#ga034033b1ae6f4677aef82d4243c6f712)HID\_ITEM\_TAG\_LOGICAL\_MIN

| #define HID\_ITEM\_TAG\_LOGICAL\_MIN   0x1 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Logical Minimum item tag.

## [◆ ](#ga70c32518a6b538831e821ad30022679b)HID\_ITEM\_TAG\_OUTPUT

| #define HID\_ITEM\_TAG\_OUTPUT   0x9 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Output item tag.

## [◆ ](#gaa68bd8a73cee33d810484f4aa3f30e92)HID\_ITEM\_TAG\_PHYSICAL\_MAX

| #define HID\_ITEM\_TAG\_PHYSICAL\_MAX   0x4 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Physical Maximum item tag.

## [◆ ](#ga6dfdd60d0b985d683a58ad752d3ef3c3)HID\_ITEM\_TAG\_PHYSICAL\_MIN

| #define HID\_ITEM\_TAG\_PHYSICAL\_MIN   0x3 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Physical Minimum item tag.

## [◆ ](#ga1847701703130ce8f57547811f28b2b4)HID\_ITEM\_TAG\_REPORT\_COUNT

| #define HID\_ITEM\_TAG\_REPORT\_COUNT   0x9 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Report count item tag.

## [◆ ](#ga76cd3a266ae5d5e29292d93caceece72)HID\_ITEM\_TAG\_REPORT\_ID

| #define HID\_ITEM\_TAG\_REPORT\_ID   0x8 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Report ID item tag.

## [◆ ](#ga0e6d7a56593bd25a5e15683e9271bb19)HID\_ITEM\_TAG\_REPORT\_SIZE

| #define HID\_ITEM\_TAG\_REPORT\_SIZE   0x7 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Report Size item tag.

## [◆ ](#ga98267b4ff28f435d67d2a7bf1055fc7c)HID\_ITEM\_TAG\_UNIT

| #define HID\_ITEM\_TAG\_UNIT   0x6 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Unit item tag.

## [◆ ](#ga7c6d81ee211814ec9b5d17f95e57639b)HID\_ITEM\_TAG\_UNIT\_EXPONENT

| #define HID\_ITEM\_TAG\_UNIT\_EXPONENT   0x5 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Unit Exponent item tag.

## [◆ ](#gaefd616ecaa8fc8762e65ec9d7b01f0cd)HID\_ITEM\_TAG\_USAGE

| #define HID\_ITEM\_TAG\_USAGE   0x0 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Usage item tag.

## [◆ ](#gac2a0aff74caff6c03511fc0b6db6167b)HID\_ITEM\_TAG\_USAGE\_MAX

| #define HID\_ITEM\_TAG\_USAGE\_MAX   0x2 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Usage Maximum item tag.

## [◆ ](#ga4e6f4133f12276f4f9fa51ab06580676)HID\_ITEM\_TAG\_USAGE\_MIN

| #define HID\_ITEM\_TAG\_USAGE\_MIN   0x1 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Usage Minimum item tag.

## [◆ ](#ga73f58fa37c0bf6698463b9d31c8a511f)HID\_ITEM\_TAG\_USAGE\_PAGE

| #define HID\_ITEM\_TAG\_USAGE\_PAGE   0x0 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Usage Page item tag.

## [◆ ](#ga8e56e8090f1af7aae473e8a8b6832fb8)HID\_ITEM\_TYPE\_GLOBAL

| #define HID\_ITEM\_TYPE\_GLOBAL   0x1 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Global item type.

## [◆ ](#ga0bfb0e326d9a01072c029cba788d6456)HID\_ITEM\_TYPE\_LOCAL

| #define HID\_ITEM\_TYPE\_LOCAL   0x2 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Local item type.

## [◆ ](#ga9a71248c522943951b5af70ec9c14c02)HID\_ITEM\_TYPE\_MAIN

| #define HID\_ITEM\_TYPE\_MAIN   0x0 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Main item type.

## [◆ ](#gafd24e87747c82293e689f58157f06128)HID\_PROTOCOL\_BOOT

| #define HID\_PROTOCOL\_BOOT   0 |
| --- |

`#include <[hid.h](hid_8h.md)>`

USB HID Class Boot protocol code.

## [◆ ](#ga982c0da911cbda6e09bd48a5e4ab85f1)HID\_PROTOCOL\_REPORT

| #define HID\_PROTOCOL\_REPORT   1 |
| --- |

`#include <[hid.h](hid_8h.md)>`

USB HID Class Report protocol code.

## [◆ ](#ga13401731a0ead5448a0823d0f6142404)HID\_USAGE\_GEN\_BUTTON

| #define HID\_USAGE\_GEN\_BUTTON   0x09 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Button Usage page.

## [◆ ](#gacb3fc5b0f838dfa5eb95e9e1bf52b589)HID\_USAGE\_GEN\_DESKTOP

| #define HID\_USAGE\_GEN\_DESKTOP   0x01 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Generic Desktop Controls Usage page.

## [◆ ](#ga17404e33133204a538f976d321c84ff0)HID\_USAGE\_GEN\_DESKTOP\_GAMEPAD

| #define HID\_USAGE\_GEN\_DESKTOP\_GAMEPAD   0x05 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Generic Desktop Gamepad Usage ID.

## [◆ ](#gada59a9f3aeaeaefc6112c7d9902b2d6d)HID\_USAGE\_GEN\_DESKTOP\_JOYSTICK

| #define HID\_USAGE\_GEN\_DESKTOP\_JOYSTICK   0x04 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Generic Desktop Joystick Usage ID.

## [◆ ](#ga0bdaa3d23c79204a1064cb53b279bd77)HID\_USAGE\_GEN\_DESKTOP\_KEYBOARD

| #define HID\_USAGE\_GEN\_DESKTOP\_KEYBOARD   0x06 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Generic Desktop Keyboard Usage ID.

## [◆ ](#ga69f8e44306828b3f44d3a7704ff07807)HID\_USAGE\_GEN\_DESKTOP\_KEYPAD

| #define HID\_USAGE\_GEN\_DESKTOP\_KEYPAD   0x07 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Generic Desktop Keypad Usage ID.

## [◆ ](#ga983274dd50058de26e0e86d10d50e81a)HID\_USAGE\_GEN\_DESKTOP\_MOUSE

| #define HID\_USAGE\_GEN\_DESKTOP\_MOUSE   0x02 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Generic Desktop Mouse Usage ID.

## [◆ ](#ga77a7162980a77efa1e2e7b21942bb7dd)HID\_USAGE\_GEN\_DESKTOP\_POINTER

| #define HID\_USAGE\_GEN\_DESKTOP\_POINTER   0x01 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Generic Desktop Pointer Usage ID.

## [◆ ](#ga1441517d7c57529dcf726a1dd8b09a07)HID\_USAGE\_GEN\_DESKTOP\_UNDEFINED

| #define HID\_USAGE\_GEN\_DESKTOP\_UNDEFINED   0x00 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Generic Desktop Undefined Usage ID.

## [◆ ](#gaa8c772d412ac1ac7a36739c52f04c0a9)HID\_USAGE\_GEN\_DESKTOP\_WHEEL

| #define HID\_USAGE\_GEN\_DESKTOP\_WHEEL   0x38 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Generic Desktop Wheel Usage ID.

## [◆ ](#gae283a3558ba536e163140a3b6cdbb273)HID\_USAGE\_GEN\_DESKTOP\_X

| #define HID\_USAGE\_GEN\_DESKTOP\_X   0x30 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Generic Desktop X Usage ID.

## [◆ ](#gad1ab1f8f9c8a4a80bfc8e3a327e3b2fb)HID\_USAGE\_GEN\_DESKTOP\_Y

| #define HID\_USAGE\_GEN\_DESKTOP\_Y   0x31 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Generic Desktop Y Usage ID.

## [◆ ](#ga1fdbfffd0b343cec1480e9f0347efa5d)HID\_USAGE\_GEN\_KEYBOARD

| #define HID\_USAGE\_GEN\_KEYBOARD   0x07 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Keyboard Usage page.

## [◆ ](#gae632e9a37203506c051c3cacfdf0c2c7)HID\_USAGE\_GEN\_LEDS

| #define HID\_USAGE\_GEN\_LEDS   0x08 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID LEDs Usage page.

## [◆ ](#ga07e8028979ff1c3d30408b08778bfd3d)USB\_DESC\_HID

| #define USB\_DESC\_HID   0x21 |
| --- |

`#include <[hid.h](hid_8h.md)>`

USB HID Class HID descriptor type.

## [◆ ](#ga2d543337d798d1c85436d2fee1c5be3f)USB\_DESC\_HID\_PHYSICAL

| #define USB\_DESC\_HID\_PHYSICAL   0x23 |
| --- |

`#include <[hid.h](hid_8h.md)>`

USB HID Class physical descriptor type.

## [◆ ](#gaca594a2caf9cb5ebac863c6c2f233f31)USB\_DESC\_HID\_REPORT

| #define USB\_DESC\_HID\_REPORT   0x22 |
| --- |

`#include <[hid.h](hid_8h.md)>`

USB HID Class Report descriptor type.

## [◆ ](#ga9d69e0dae00cf3c6c5dc5602f63b2f2f)USB\_HID\_GET\_IDLE

| #define USB\_HID\_GET\_IDLE   0x02 |
| --- |

`#include <[hid.h](hid_8h.md)>`

USB HID Class GetIdle bRequest value.

## [◆ ](#ga09469e20036a4c3df8281a2575358747)USB\_HID\_GET\_PROTOCOL

| #define USB\_HID\_GET\_PROTOCOL   0x03 |
| --- |

`#include <[hid.h](hid_8h.md)>`

USB HID Class GetProtocol bRequest value.

## [◆ ](#ga3d4f67db0b3531f3493cde381110809d)USB\_HID\_GET\_REPORT

| #define USB\_HID\_GET\_REPORT   0x01 |
| --- |

`#include <[hid.h](hid_8h.md)>`

USB HID Class GetReport bRequest value.

## [◆ ](#ga1cbc5f99d9bd85fca7b9a624efb41078)USB\_HID\_SET\_IDLE

| #define USB\_HID\_SET\_IDLE   0x0A |
| --- |

`#include <[hid.h](hid_8h.md)>`

USB HID Class SetIdle bRequest value.

## [◆ ](#ga2058ed723b6a4613b4dcb8040b739684)USB\_HID\_SET\_PROTOCOL

| #define USB\_HID\_SET\_PROTOCOL   0x0B |
| --- |

`#include <[hid.h](hid_8h.md)>`

USB HID Class SetProtocol bRequest value.

## [◆ ](#gaed6de2caf14f9caa049fab82902299cf)USB\_HID\_SET\_REPORT

| #define USB\_HID\_SET\_REPORT   0x09 |
| --- |

`#include <[hid.h](hid_8h.md)>`

USB HID Class SetReport bRequest value.

## [◆ ](#ga77f649cbc5ab446b2cfe3e68eb88ac91)USB\_HID\_VERSION

| #define USB\_HID\_VERSION   0x0111 |
| --- |

`#include <[hid.h](hid_8h.md)>`

HID Specification release v1.11.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

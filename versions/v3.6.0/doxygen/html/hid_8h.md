---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/hid_8h.html
original_path: doxygen/html/hid_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hid.h File Reference

USB Human Interface Device (HID) common definitions header.
[More...](#details)

[Go to the source code of this file.](hid_8h_source.md)

| Macros | |
| --- | --- |
| #define | [HID\_ITEM](group__usb__hid__items.md#ga4e9dc6652402e0b87e1313c143737ed4)(bTag, bType, bSize) |
|  | Define HID short item. |
| #define | [HID\_INPUT](group__usb__hid__items.md#ga8646699330c45fb008d50b54be339c6c)(a) |
|  | Define HID Input item with the data length of one byte. |
| #define | [HID\_OUTPUT](group__usb__hid__items.md#ga6ef7aa576bf69f9ba5f93df500a1403c)(a) |
|  | Define HID Output item with the data length of one byte. |
| #define | [HID\_FEATURE](group__usb__hid__items.md#ga951a415e05e95492250d4fb43a37090d)(a) |
|  | Define HID Feature item with the data length of one byte. |
| #define | [HID\_COLLECTION](group__usb__hid__items.md#gad010ed98662b0e653754caff1dfd352f)(a) |
|  | Define HID Collection item with the data length of one byte. |
| #define | [HID\_END\_COLLECTION](group__usb__hid__items.md#ga6cd6affb9d52e0bf98c7a5c83d03a764)   [HID\_ITEM](group__usb__hid__items.md#ga4e9dc6652402e0b87e1313c143737ed4)([HID\_ITEM\_TAG\_COLLECTION\_END](group__usb__hid__definitions.md#ga3f4fe1817887966f0d05aa597cd0ab79), [HID\_ITEM\_TYPE\_MAIN](group__usb__hid__definitions.md#ga9a71248c522943951b5af70ec9c14c02), 0) |
|  | Define HID End Collection (non-data) item. |
| #define | [HID\_USAGE\_PAGE](group__usb__hid__items.md#ga30dc3f62583822ba27edd984dc2dec39)(page) |
|  | Define HID Usage Page item. |
| #define | [HID\_LOGICAL\_MIN8](group__usb__hid__items.md#gacd141f6ede5122f260cd50338649d458)(a) |
|  | Define HID Logical Minimum item with the data length of one byte. |
| #define | [HID\_LOGICAL\_MAX8](group__usb__hid__items.md#ga2f6b809ae85b6716ade8c52da4fa56af)(a) |
|  | Define HID Logical Maximum item with the data length of one byte. |
| #define | [HID\_LOGICAL\_MIN16](group__usb__hid__items.md#ga5e290798d55bccd7474dbfb6bc2d1033)(a, b) |
|  | Define HID Logical Minimum item with the data length of two bytes. |
| #define | [HID\_LOGICAL\_MAX16](group__usb__hid__items.md#ga9b804d676812dcfb0ec12f3aa887e37f)(a, b) |
|  | Define HID Logical Maximum item with the data length of two bytes. |
| #define | [HID\_LOGICAL\_MIN32](group__usb__hid__items.md#gad4b2ff8642676d692fd0d56ab0cbeaa7)(a, b, c, [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)) |
|  | Define HID Logical Minimum item with the data length of four bytes. |
| #define | [HID\_LOGICAL\_MAX32](group__usb__hid__items.md#gae9d17e753685b0df6c53f942ce9c95d2)(a, b, c, [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)) |
|  | Define HID Logical Maximum item with the data length of four bytes. |
| #define | [HID\_REPORT\_SIZE](group__usb__hid__items.md#ga3135a21a63c491daf8647fa771def0e7)(size) |
|  | Define HID Report Size item with the data length of one byte. |
| #define | [HID\_REPORT\_ID](group__usb__hid__items.md#ga1b45fce2c7df2847b1326fca29cef389)(id) |
|  | Define HID Report ID item with the data length of one byte. |
| #define | [HID\_REPORT\_COUNT](group__usb__hid__items.md#ga71192f2a55f05456b893069ebfbc5b98)(count) |
|  | Define HID Report Count item with the data length of one byte. |
| #define | [HID\_USAGE](group__usb__hid__items.md#gac8429a70866a898887ead55664e04bd7)(idx) |
|  | Define HID Usage Index item with the data length of one byte. |
| #define | [HID\_USAGE\_MIN8](group__usb__hid__items.md#gabf53f1e2eae6d686aeb7d62cc46b22ad)(a) |
|  | Define HID Usage Minimum item with the data length of one byte. |
| #define | [HID\_USAGE\_MAX8](group__usb__hid__items.md#gae7fc9684ef10f50d69df6f495cc09e91)(a) |
|  | Define HID Usage Maximum item with the data length of one byte. |
| #define | [HID\_USAGE\_MIN16](group__usb__hid__items.md#ga0dbc847d11cf64676f7cfc51b54150fa)(a, b) |
|  | Define HID Usage Minimum item with the data length of two bytes. |
| #define | [HID\_USAGE\_MAX16](group__usb__hid__items.md#gadd11a09546bc275c82e7a992cb9441cc)(a, b) |
|  | Define HID Usage Maximum item with the data length of two bytes. |
| #define | [HID\_MOUSE\_REPORT\_DESC](group__usb__hid__mk__report__desc.md#ga3696f0782268d504b0c8bb540236779f)(bcnt) |
|  | Simple HID mouse report descriptor for n button mouse. |
| #define | [HID\_KEYBOARD\_REPORT\_DESC](group__usb__hid__mk__report__desc.md#gaea973ffbe1612187c90614133956cfd6)() |
|  | Simple HID keyboard report descriptor. |
| USB HID types and values | |
| #define | [USB\_HID\_VERSION](group__usb__hid__definitions.md#ga77f649cbc5ab446b2cfe3e68eb88ac91)   0x0111 |
|  | HID Specification release v1.11. |
| #define | [USB\_DESC\_HID](group__usb__hid__definitions.md#ga07e8028979ff1c3d30408b08778bfd3d)   0x21 |
|  | USB HID Class HID descriptor type. |
| #define | [USB\_DESC\_HID\_REPORT](group__usb__hid__definitions.md#gaca594a2caf9cb5ebac863c6c2f233f31)   0x22 |
|  | USB HID Class Report descriptor type. |
| #define | [USB\_DESC\_HID\_PHYSICAL](group__usb__hid__definitions.md#ga2d543337d798d1c85436d2fee1c5be3f)   0x23 |
|  | USB HID Class physical descriptor type. |
| #define | [USB\_HID\_GET\_REPORT](group__usb__hid__definitions.md#ga3d4f67db0b3531f3493cde381110809d)   0x01 |
|  | USB HID Class GetReport bRequest value. |
| #define | [USB\_HID\_GET\_IDLE](group__usb__hid__definitions.md#ga9d69e0dae00cf3c6c5dc5602f63b2f2f)   0x02 |
|  | USB HID Class GetIdle bRequest value. |
| #define | [USB\_HID\_GET\_PROTOCOL](group__usb__hid__definitions.md#ga09469e20036a4c3df8281a2575358747)   0x03 |
|  | USB HID Class GetProtocol bRequest value. |
| #define | [USB\_HID\_SET\_REPORT](group__usb__hid__definitions.md#gaed6de2caf14f9caa049fab82902299cf)   0x09 |
|  | USB HID Class SetReport bRequest value. |
| #define | [USB\_HID\_SET\_IDLE](group__usb__hid__definitions.md#ga1cbc5f99d9bd85fca7b9a624efb41078)   0x0A |
|  | USB HID Class SetIdle bRequest value. |
| #define | [USB\_HID\_SET\_PROTOCOL](group__usb__hid__definitions.md#ga2058ed723b6a4613b4dcb8040b739684)   0x0B |
|  | USB HID Class SetProtocol bRequest value. |
| #define | [HID\_BOOT\_IFACE\_CODE\_NONE](group__usb__hid__definitions.md#ga953074178d707cd3538da80f36a96ff6)   0 |
|  | USB HID Boot Interface Protocol (bInterfaceProtocol) Code None. |
| #define | [HID\_BOOT\_IFACE\_CODE\_KEYBOARD](group__usb__hid__definitions.md#ga6e6276ae88c414e10c602d5e041738ab)   1 |
|  | USB HID Boot Interface Protocol (bInterfaceProtocol) Code Keyboard. |
| #define | [HID\_BOOT\_IFACE\_CODE\_MOUSE](group__usb__hid__definitions.md#ga900873d4834ea511a08b08debe62bedf)   2 |
|  | USB HID Boot Interface Protocol (bInterfaceProtocol) Code Mouse. |
| #define | [HID\_PROTOCOL\_BOOT](group__usb__hid__definitions.md#gafd24e87747c82293e689f58157f06128)   0 |
|  | USB HID Class Boot protocol code. |
| #define | [HID\_PROTOCOL\_REPORT](group__usb__hid__definitions.md#ga982c0da911cbda6e09bd48a5e4ab85f1)   1 |
|  | USB HID Class Report protocol code. |
| #define | [HID\_ITEM\_TYPE\_MAIN](group__usb__hid__definitions.md#ga9a71248c522943951b5af70ec9c14c02)   0x0 |
|  | HID Main item type. |
| #define | [HID\_ITEM\_TYPE\_GLOBAL](group__usb__hid__definitions.md#ga8e56e8090f1af7aae473e8a8b6832fb8)   0x1 |
|  | HID Global item type. |
| #define | [HID\_ITEM\_TYPE\_LOCAL](group__usb__hid__definitions.md#ga0bfb0e326d9a01072c029cba788d6456)   0x2 |
|  | HID Local item type. |
| #define | [HID\_ITEM\_TAG\_INPUT](group__usb__hid__definitions.md#ga66e1c50fe814fd05d61dce12ce3888c1)   0x8 |
|  | HID Input item tag. |
| #define | [HID\_ITEM\_TAG\_OUTPUT](group__usb__hid__definitions.md#ga70c32518a6b538831e821ad30022679b)   0x9 |
|  | HID Output item tag. |
| #define | [HID\_ITEM\_TAG\_COLLECTION](group__usb__hid__definitions.md#ga2c06052593b060466f4c338a88319485)   0xA |
|  | HID Collection item tag. |
| #define | [HID\_ITEM\_TAG\_FEATURE](group__usb__hid__definitions.md#gaeadcca849f0a0923d9a70605c44464a6)   0xB |
|  | HID Feature item tag. |
| #define | [HID\_ITEM\_TAG\_COLLECTION\_END](group__usb__hid__definitions.md#ga3f4fe1817887966f0d05aa597cd0ab79)   0xC |
|  | HID End Collection item tag. |
| #define | [HID\_ITEM\_TAG\_USAGE\_PAGE](group__usb__hid__definitions.md#ga73f58fa37c0bf6698463b9d31c8a511f)   0x0 |
|  | HID Usage Page item tag. |
| #define | [HID\_ITEM\_TAG\_LOGICAL\_MIN](group__usb__hid__definitions.md#ga034033b1ae6f4677aef82d4243c6f712)   0x1 |
|  | HID Logical Minimum item tag. |
| #define | [HID\_ITEM\_TAG\_LOGICAL\_MAX](group__usb__hid__definitions.md#gaab6aec72cca41670464605d6970ad553)   0x2 |
|  | HID Logical Maximum item tag. |
| #define | [HID\_ITEM\_TAG\_PHYSICAL\_MIN](group__usb__hid__definitions.md#ga6dfdd60d0b985d683a58ad752d3ef3c3)   0x3 |
|  | HID Physical Minimum item tag. |
| #define | [HID\_ITEM\_TAG\_PHYSICAL\_MAX](group__usb__hid__definitions.md#gaa68bd8a73cee33d810484f4aa3f30e92)   0x4 |
|  | HID Physical Maximum item tag. |
| #define | [HID\_ITEM\_TAG\_UNIT\_EXPONENT](group__usb__hid__definitions.md#ga7c6d81ee211814ec9b5d17f95e57639b)   0x5 |
|  | HID Unit Exponent item tag. |
| #define | [HID\_ITEM\_TAG\_UNIT](group__usb__hid__definitions.md#ga98267b4ff28f435d67d2a7bf1055fc7c)   0x6 |
|  | HID Unit item tag. |
| #define | [HID\_ITEM\_TAG\_REPORT\_SIZE](group__usb__hid__definitions.md#ga0e6d7a56593bd25a5e15683e9271bb19)   0x7 |
|  | HID Report Size item tag. |
| #define | [HID\_ITEM\_TAG\_REPORT\_ID](group__usb__hid__definitions.md#ga76cd3a266ae5d5e29292d93caceece72)   0x8 |
|  | HID Report ID item tag. |
| #define | [HID\_ITEM\_TAG\_REPORT\_COUNT](group__usb__hid__definitions.md#ga1847701703130ce8f57547811f28b2b4)   0x9 |
|  | HID Report count item tag. |
| #define | [HID\_ITEM\_TAG\_USAGE](group__usb__hid__definitions.md#gaefd616ecaa8fc8762e65ec9d7b01f0cd)   0x0 |
|  | HID Usage item tag. |
| #define | [HID\_ITEM\_TAG\_USAGE\_MIN](group__usb__hid__definitions.md#ga4e6f4133f12276f4f9fa51ab06580676)   0x1 |
|  | HID Usage Minimum item tag. |
| #define | [HID\_ITEM\_TAG\_USAGE\_MAX](group__usb__hid__definitions.md#gac2a0aff74caff6c03511fc0b6db6167b)   0x2 |
|  | HID Usage Maximum item tag. |
| #define | [HID\_COLLECTION\_PHYSICAL](group__usb__hid__definitions.md#gaca1e227f9241c217b8b1aeae6c4bd672)   0x00 |
|  | Physical collection type. |
| #define | [HID\_COLLECTION\_APPLICATION](group__usb__hid__definitions.md#ga2e5e5ad0919fbaea0e6f8e5d86f4c2fd)   0x01 |
|  | Application collection type. |
| #define | [HID\_COLLECTION\_LOGICAL](group__usb__hid__definitions.md#ga904a372a663bd7d9205402a3a014c04b)   0x02 |
|  | Logical collection type. |
| #define | [HID\_COLLECTION\_REPORT](group__usb__hid__definitions.md#gac58ab4780c054754b7f94ff97a152694)   0x03 |
|  | Report collection type. |
| #define | [HID\_COLLECTION\_NAMED\_ARRAY](group__usb__hid__definitions.md#ga8e1610365a1556adf7121cc3b1f83080)   0x04 |
|  | Named Array collection type. |
| #define | [HID\_COLLECTION\_USAGE\_SWITCH](group__usb__hid__definitions.md#ga64af797e424ea1e2c02c745f30721e48)   0x05 |
|  | Usage Switch collection type. |
| #define | [HID\_COLLECTION\_MODIFIER](group__usb__hid__definitions.md#gaabc1c6bed23b88f4cdc89d5347595d4f)   0x06 |
|  | Modifier collection type. |
| #define | [HID\_USAGE\_GEN\_DESKTOP](group__usb__hid__definitions.md#gacb3fc5b0f838dfa5eb95e9e1bf52b589)   0x01 |
|  | HID Generic Desktop Controls Usage page. |
| #define | [HID\_USAGE\_GEN\_KEYBOARD](group__usb__hid__definitions.md#ga1fdbfffd0b343cec1480e9f0347efa5d)   0x07 |
|  | HID Keyboard Usage page. |
| #define | [HID\_USAGE\_GEN\_LEDS](group__usb__hid__definitions.md#gae632e9a37203506c051c3cacfdf0c2c7)   0x08 |
|  | HID LEDs Usage page. |
| #define | [HID\_USAGE\_GEN\_BUTTON](group__usb__hid__definitions.md#ga13401731a0ead5448a0823d0f6142404)   0x09 |
|  | HID Button Usage page. |
| #define | [HID\_USAGE\_GEN\_DESKTOP\_UNDEFINED](group__usb__hid__definitions.md#ga1441517d7c57529dcf726a1dd8b09a07)   0x00 |
|  | HID Generic Desktop Undefined Usage ID. |
| #define | [HID\_USAGE\_GEN\_DESKTOP\_POINTER](group__usb__hid__definitions.md#ga77a7162980a77efa1e2e7b21942bb7dd)   0x01 |
|  | HID Generic Desktop Pointer Usage ID. |
| #define | [HID\_USAGE\_GEN\_DESKTOP\_MOUSE](group__usb__hid__definitions.md#ga983274dd50058de26e0e86d10d50e81a)   0x02 |
|  | HID Generic Desktop Mouse Usage ID. |
| #define | [HID\_USAGE\_GEN\_DESKTOP\_JOYSTICK](group__usb__hid__definitions.md#gada59a9f3aeaeaefc6112c7d9902b2d6d)   0x04 |
|  | HID Generic Desktop Joystick Usage ID. |
| #define | [HID\_USAGE\_GEN\_DESKTOP\_GAMEPAD](group__usb__hid__definitions.md#ga17404e33133204a538f976d321c84ff0)   0x05 |
|  | HID Generic Desktop Gamepad Usage ID. |
| #define | [HID\_USAGE\_GEN\_DESKTOP\_KEYBOARD](group__usb__hid__definitions.md#ga0bdaa3d23c79204a1064cb53b279bd77)   0x06 |
|  | HID Generic Desktop Keyboard Usage ID. |
| #define | [HID\_USAGE\_GEN\_DESKTOP\_KEYPAD](group__usb__hid__definitions.md#ga69f8e44306828b3f44d3a7704ff07807)   0x07 |
|  | HID Generic Desktop Keypad Usage ID. |
| #define | [HID\_USAGE\_GEN\_DESKTOP\_X](group__usb__hid__definitions.md#gae283a3558ba536e163140a3b6cdbb273)   0x30 |
|  | HID Generic Desktop X Usage ID. |
| #define | [HID\_USAGE\_GEN\_DESKTOP\_Y](group__usb__hid__definitions.md#gad1ab1f8f9c8a4a80bfc8e3a327e3b2fb)   0x31 |
|  | HID Generic Desktop Y Usage ID. |
| #define | [HID\_USAGE\_GEN\_DESKTOP\_WHEEL](group__usb__hid__definitions.md#gaa8c772d412ac1ac7a36739c52f04c0a9)   0x38 |
|  | HID Generic Desktop Wheel Usage ID. |

| Enumerations | |
| --- | --- |
| enum | [hid\_kbd\_code](group__usb__hid__mk__report__desc.md#ga4f2bb15109c64695f852afd6bd99e3bf) {     [HID\_KEY\_A](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa5413afa6a28a21dd52f07db101f2d139) = 4 , [HID\_KEY\_B](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfabb0b25fe8c201dc75b72c7b078f745d6) = 5 , [HID\_KEY\_C](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa932c610512cc99157654c3997bc2b922) = 6 , [HID\_KEY\_D](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfabc172093417a4c40a7443eee551e9700) = 7 ,     [HID\_KEY\_E](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaff7192b9ddd4228e02c44b6fb2d7bf85) = 8 , [HID\_KEY\_F](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfacc002ca9f0f3bdc01b4de42d00e5560b) = 9 , [HID\_KEY\_G](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa1eadd56346bbd64b1c33fa5393f65bda) = 10 , [HID\_KEY\_H](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4bfc341fccde664ec9267af6e705ba0c) = 11 ,     [HID\_KEY\_I](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfafcd25dc5bba218f7097698f8f49fdc45) = 12 , [HID\_KEY\_J](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa2a78196208c634941d63429cd1e1df7a) = 13 , [HID\_KEY\_K](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4ceddaaaa90d84f0afb3e1ee9a35a976) = 14 , [HID\_KEY\_L](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaf5de66adc9eb2aa183eab1e23f977894) = 15 ,     [HID\_KEY\_M](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4f8174feca1eb72901576c4e24c8f8a9) = 16 , [HID\_KEY\_N](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfab4d202043e8b0b7a8c2d4c519fd1eb07) = 17 , [HID\_KEY\_O](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfad8884ef7e77722099e6bd61265f6564c) = 18 , [HID\_KEY\_P](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaca0480331288d15eccec9f072f123817) = 19 ,     [HID\_KEY\_Q](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa05fb920f8129f57dd350036f17fbe519) = 20 , [HID\_KEY\_R](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa037de00c763ae6b270895b7a5f0f57a7) = 21 , [HID\_KEY\_S](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfae6a84e8474b6c3e8f9f7d344408cfa0b) = 22 , [HID\_KEY\_T](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa893799f48b30c438349335556a0e15b6) = 23 ,     [HID\_KEY\_U](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfab3c7c9f3a73e83623c651cdfddddeb05) = 24 , [HID\_KEY\_V](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa02f14e6303b4d2e4e46747324d649dda) = 25 , [HID\_KEY\_W](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfadf81a88f3f92f15e2abec83911bf3732) = 26 , [HID\_KEY\_X](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa9f3b8bb63f6628db9a1678b72ec12b6d) = 27 ,     [HID\_KEY\_Y](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4ca2ebe26c09f2400a8ebc0aa445ce89) = 28 , [HID\_KEY\_Z](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaa5cd01ad23ede98de1ae176920b8fc8f) = 29 , [HID\_KEY\_1](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa039ced168420140b97e2d0676e1bb12a) = 30 , [HID\_KEY\_2](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfae98dd71460def5e66fcf32e9783b96ea) = 31 ,     [HID\_KEY\_3](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaf58d848786f8d2dfac702f7fae178311) = 32 , [HID\_KEY\_4](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa17019d72e84302486f72f7d8101baca5) = 33 , [HID\_KEY\_5](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaf32ab36da2e30066c9ed2816596011c8) = 34 , [HID\_KEY\_6](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfae16b76c1bf9f7aa58a1b1c556a6b6022) = 35 ,     [HID\_KEY\_7](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa5887a1854f7d0787121bd75034cdd726) = 36 , [HID\_KEY\_8](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa1761228849d7dc2b84d0565d3337b2e2) = 37 , [HID\_KEY\_9](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa758aec2540a6a2153702d6905c44ce52) = 38 , [HID\_KEY\_0](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa856ca663233681e789ef4aa94c44ebaf) = 39 ,     [HID\_KEY\_ENTER](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaeeab6ddad27c449cbc44ca2458912a75) = 40 , [HID\_KEY\_ESC](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa763b39fe76a92c4cc1fc32f47d2a760a) = 41 , [HID\_KEY\_BACKSPACE](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfafd6cf6a44966d518b173df4ed57ae720) = 42 , [HID\_KEY\_TAB](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa5a6c79e8ea85f6593c06d19098d69a03) = 43 ,     [HID\_KEY\_SPACE](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaf4fc3d7b4b86f9f095cec624d190ebec) = 44 , [HID\_KEY\_MINUS](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaa59864204064d3e8fac5271b69a7da23) = 45 , [HID\_KEY\_EQUAL](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfac8d82858905175ba79c24b0be1b1b1a8) = 46 , [HID\_KEY\_LEFTBRACE](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfac232473666b21ca772c84b68be6c1f3d) = 47 ,     [HID\_KEY\_RIGHTBRACE](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaef692bd882621d292255cb99d4697513) = 48 , [HID\_KEY\_BACKSLASH](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa25ba5457bc128593b1624d95ec536182) = 49 , [HID\_KEY\_HASH](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa0d57ce7c99d06ee9b15fef880af075eb) = 50 , [HID\_KEY\_SEMICOLON](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa3743f920856a12e726e1be05932c7411) = 51 ,     [HID\_KEY\_APOSTROPHE](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa7325a5bd52e9dc0cc38a85609b1c55ab) = 52 , [HID\_KEY\_GRAVE](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa8b84c64da5b8c5f5d99b86c1cfe09ffc) = 53 , [HID\_KEY\_COMMA](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaa81aa5b3424f02fdf02295de47b11b19) = 54 , [HID\_KEY\_DOT](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa403fe927ebb0014e2c1b3dc25e1d9779) = 55 ,     [HID\_KEY\_SLASH](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa24c2c93a1c895745828311affc011dea) = 56 , [HID\_KEY\_CAPSLOCK](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4d40549a59fdcfdd0b2d592a6675bc89) = 57 , [HID\_KEY\_F1](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa9642163abbbad8aa5c7088c8529aadd7) = 58 , [HID\_KEY\_F2](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa9ce331f5f41ba3e3e05f485bc2d4138e) = 59 ,     [HID\_KEY\_F3](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa76adde1d9295cf62e7efb35e27911a1e) = 60 , [HID\_KEY\_F4](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaa9956a2b95afe1a05fda65db5cc66467) = 61 , [HID\_KEY\_F5](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bface9e8d409d981f193f69fc5b29f38ca7) = 62 , [HID\_KEY\_F6](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfabc92147e725c8108c18f4e03005afbdc) = 63 ,     [HID\_KEY\_F7](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa1e2eabf8b9fa6cbfea613696b2c4122a) = 64 , [HID\_KEY\_F8](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa5092add2863231d273ba60cd583ebe33) = 65 , [HID\_KEY\_F9](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa5a09deabde1a3a44378b7de44dad27b6) = 66 , [HID\_KEY\_F10](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfac2c4a3aec85b4d8171de4429ccabbe19) = 67 ,     [HID\_KEY\_F11](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa76bb35a0f71733b0a0f1bd7e3837064c) = 68 , [HID\_KEY\_F12](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfab44ba4426c1574f4b296794b7bfe2172) = 69 , [HID\_KEY\_SYSRQ](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfae5405b62cb20962cb5864ba6e90a4ab2) = 70 , [HID\_KEY\_SCROLLLOCK](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfae16bd57629c7aba96a554d0446e83d98) = 71 ,     [HID\_KEY\_PAUSE](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa1905733a0fe81f78e0752e3b0bb99c69) = 72 , [HID\_KEY\_INSERT](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa1e1c320cea0644c3dc38da06c865837b) = 73 , [HID\_KEY\_HOME](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa5fc1127fe9014018f4831cbf272c883b) = 74 , [HID\_KEY\_PAGEUP](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa2468ac3b37d38b6158cd989ed54bcd8c) = 75 ,     [HID\_KEY\_DELETE](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfae8f5051cb476c3e9253b008094c431fc) = 76 , [HID\_KEY\_END](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa8f933f0f6e5a1a3c3cdc1819ffcdce63) = 77 , [HID\_KEY\_PAGEDOWN](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaf7615ff4f608d64ae20a61540d939065) = 78 , [HID\_KEY\_RIGHT](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4c203feb452e3212089e8246b8d75f6c) = 79 ,     [HID\_KEY\_LEFT](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaf7d3c678a8ac31916068a0c5aff54d4b) = 80 , [HID\_KEY\_DOWN](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa9e2597c2a109abda1c63c8d5ca5376b3) = 81 , [HID\_KEY\_UP](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaf5fe431b55adf16d82604e0fc2239090) = 82 , [HID\_KEY\_NUMLOCK](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfafec8c71efd5ee9decd156f0d33739fbe) = 83 ,     [HID\_KEY\_KPSLASH](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa44e83040efab214dcfe462ac0d338e0c) = 84 , [HID\_KEY\_KPASTERISK](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaff47eb8157a7118183573e3aefb7df08) = 85 , [HID\_KEY\_KPMINUS](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa6fb35c78b12ae434cb7a7280501886e9) = 86 , [HID\_KEY\_KPPLUS](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa2cb7852467d2ebd785e2f7556383a883) = 87 ,     [HID\_KEY\_KPENTER](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfab5b923992d0bdc176f716cd8ace3a66e) = 88 , [HID\_KEY\_KP\_1](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa7eea75b0eb4b4f0306daa3e6fccf09e4) = 89 , [HID\_KEY\_KP\_2](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa68db65e7002e7cc599394a7eea116e3c) = 90 , [HID\_KEY\_KP\_3](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4210f9a5ae469c8b863b28b9b2d8189d) = 91 ,     [HID\_KEY\_KP\_4](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa48eefeeb48a942eaaa0726bd4a2df01d) = 92 , [HID\_KEY\_KP\_5](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa1b8d299d56a0289ae15cbf8c67e36a7c) = 93 , [HID\_KEY\_KP\_6](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa90f2c51ad42e335a474061c4d5e4e5a9) = 94 , [HID\_KEY\_KP\_7](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa1e191017084fadf830a7394de0e1cc05) = 95 ,     [HID\_KEY\_KP\_8](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfadd7c795e2c9c212a4adeaba904bda447) = 96 , [HID\_KEY\_KP\_9](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bface8d41615c6afd45724f4b6d16238c36) = 97 , [HID\_KEY\_KP\_0](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4ae4af2b06f6f2585a598353bfef9af7) = 98   } |
|  | HID keyboard button codes. [More...](group__usb__hid__mk__report__desc.md#ga4f2bb15109c64695f852afd6bd99e3bf) |
| enum | [hid\_kbd\_modifier](group__usb__hid__mk__report__desc.md#ga12f11556b697518b00fa86eb040f9eb8) {     [HID\_KBD\_MODIFIER\_NONE](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8a79b0eb4f485bedb745180f1b8798c603) = 0x00 , [HID\_KBD\_MODIFIER\_LEFT\_CTRL](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8a4df663509a05599fd66657cfc90a37c7) = 0x01 , [HID\_KBD\_MODIFIER\_LEFT\_SHIFT](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8aba69ca183306d3d1427b66666803e57f) = 0x02 , [HID\_KBD\_MODIFIER\_LEFT\_ALT](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8a829d884291b546c0e276afa4ad92ac18) = 0x04 ,     [HID\_KBD\_MODIFIER\_LEFT\_UI](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8a718c92a2d0ca9dd6603825b97a99fc77) = 0x08 , [HID\_KBD\_MODIFIER\_RIGHT\_CTRL](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8a8e346c0e9c7d5b58e4b8748380423a92) = 0x10 , [HID\_KBD\_MODIFIER\_RIGHT\_SHIFT](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8affdba298e8860b000a0916be7495c2dc) = 0x20 , [HID\_KBD\_MODIFIER\_RIGHT\_ALT](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8a85ce29a6ab9feef68350deca92001db2) = 0x40 ,     [HID\_KBD\_MODIFIER\_RIGHT\_UI](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8a1b4b75cd0364824cbfc80dfc68e294dd) = 0x80   } |
|  | HID keyboard modifiers. [More...](group__usb__hid__mk__report__desc.md#ga12f11556b697518b00fa86eb040f9eb8) |
| enum | [hid\_kbd\_led](group__usb__hid__mk__report__desc.md#ga8cef56ba216d0a01c6cc89f723d1740b) {     [HID\_KBD\_LED\_NUM\_LOCK](group__usb__hid__mk__report__desc.md#gga8cef56ba216d0a01c6cc89f723d1740ba6cb2e1acb52cc5bab8dd3aa6ef6ac01b) = 0x01 , [HID\_KBD\_LED\_CAPS\_LOCK](group__usb__hid__mk__report__desc.md#gga8cef56ba216d0a01c6cc89f723d1740baa17e5130bd8c45eb21661d8783517266) = 0x02 , [HID\_KBD\_LED\_SCROLL\_LOCK](group__usb__hid__mk__report__desc.md#gga8cef56ba216d0a01c6cc89f723d1740ba6ea943f59b98680aefd0d5be4ef22e36) = 0x04 , [HID\_KBD\_LED\_COMPOSE](group__usb__hid__mk__report__desc.md#gga8cef56ba216d0a01c6cc89f723d1740bad62692e71ae45351311c8bf2ce13e3c9) = 0x08 ,     [HID\_KBD\_LED\_KANA](group__usb__hid__mk__report__desc.md#gga8cef56ba216d0a01c6cc89f723d1740bafd5d599c1955bdb1c62c7b17286b37f1) = 0x10   } |
|  | HID keyboard LEDs. [More...](group__usb__hid__mk__report__desc.md#ga8cef56ba216d0a01c6cc89f723d1740b) |

## Detailed Description

USB Human Interface Device (HID) common definitions header.

Header follows Device Class Definition for Human Interface Devices (HID) Version 1.11 document (HID1\_11-1.pdf).

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [class](dir_c68ea25cffcb2672410964c117624aed.md)
- [hid.h](hid_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

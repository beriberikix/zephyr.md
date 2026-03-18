---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/hid_8h_source.html
original_path: doxygen/html/hid_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hid.h

[Go to the documentation of this file.](hid_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation

3 \* Copyright (c) 2018,2021 Nordic Semiconductor ASA

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

15

16#ifndef ZEPHYR\_INCLUDE\_USB\_CLASS\_HID\_H\_

17#define ZEPHYR\_INCLUDE\_USB\_CLASS\_HID\_H\_

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

29

34

[ 36](group__usb__hid__definitions.md#ga77f649cbc5ab446b2cfe3e68eb88ac91)#define USB\_HID\_VERSION 0x0111

37

[ 39](group__usb__hid__definitions.md#ga07e8028979ff1c3d30408b08778bfd3d)#define USB\_DESC\_HID 0x21

[ 41](group__usb__hid__definitions.md#gaca594a2caf9cb5ebac863c6c2f233f31)#define USB\_DESC\_HID\_REPORT 0x22

[ 43](group__usb__hid__definitions.md#ga2d543337d798d1c85436d2fee1c5be3f)#define USB\_DESC\_HID\_PHYSICAL 0x23

44

[ 46](group__usb__hid__definitions.md#ga3d4f67db0b3531f3493cde381110809d)#define USB\_HID\_GET\_REPORT 0x01

[ 48](group__usb__hid__definitions.md#ga9d69e0dae00cf3c6c5dc5602f63b2f2f)#define USB\_HID\_GET\_IDLE 0x02

[ 50](group__usb__hid__definitions.md#ga09469e20036a4c3df8281a2575358747)#define USB\_HID\_GET\_PROTOCOL 0x03

[ 52](group__usb__hid__definitions.md#gaed6de2caf14f9caa049fab82902299cf)#define USB\_HID\_SET\_REPORT 0x09

[ 54](group__usb__hid__definitions.md#ga1cbc5f99d9bd85fca7b9a624efb41078)#define USB\_HID\_SET\_IDLE 0x0A

[ 56](group__usb__hid__definitions.md#ga2058ed723b6a4613b4dcb8040b739684)#define USB\_HID\_SET\_PROTOCOL 0x0B

57

[ 59](group__usb__hid__definitions.md#ga953074178d707cd3538da80f36a96ff6)#define HID\_BOOT\_IFACE\_CODE\_NONE 0

[ 61](group__usb__hid__definitions.md#ga6e6276ae88c414e10c602d5e041738ab)#define HID\_BOOT\_IFACE\_CODE\_KEYBOARD 1

[ 63](group__usb__hid__definitions.md#ga900873d4834ea511a08b08debe62bedf)#define HID\_BOOT\_IFACE\_CODE\_MOUSE 2

64

[ 66](group__usb__hid__definitions.md#gafd24e87747c82293e689f58157f06128)#define HID\_PROTOCOL\_BOOT 0

[ 68](group__usb__hid__definitions.md#ga982c0da911cbda6e09bd48a5e4ab85f1)#define HID\_PROTOCOL\_REPORT 1

69

[ 71](group__usb__hid__definitions.md#ga9a71248c522943951b5af70ec9c14c02)#define HID\_ITEM\_TYPE\_MAIN 0x0

[ 73](group__usb__hid__definitions.md#ga8e56e8090f1af7aae473e8a8b6832fb8)#define HID\_ITEM\_TYPE\_GLOBAL 0x1

[ 75](group__usb__hid__definitions.md#ga0bfb0e326d9a01072c029cba788d6456)#define HID\_ITEM\_TYPE\_LOCAL 0x2

76

[ 78](group__usb__hid__definitions.md#ga66e1c50fe814fd05d61dce12ce3888c1)#define HID\_ITEM\_TAG\_INPUT 0x8

[ 80](group__usb__hid__definitions.md#ga70c32518a6b538831e821ad30022679b)#define HID\_ITEM\_TAG\_OUTPUT 0x9

[ 82](group__usb__hid__definitions.md#ga2c06052593b060466f4c338a88319485)#define HID\_ITEM\_TAG\_COLLECTION 0xA

[ 84](group__usb__hid__definitions.md#gaeadcca849f0a0923d9a70605c44464a6)#define HID\_ITEM\_TAG\_FEATURE 0xB

[ 86](group__usb__hid__definitions.md#ga3f4fe1817887966f0d05aa597cd0ab79)#define HID\_ITEM\_TAG\_COLLECTION\_END 0xC

87

[ 89](group__usb__hid__definitions.md#ga73f58fa37c0bf6698463b9d31c8a511f)#define HID\_ITEM\_TAG\_USAGE\_PAGE 0x0

[ 91](group__usb__hid__definitions.md#ga034033b1ae6f4677aef82d4243c6f712)#define HID\_ITEM\_TAG\_LOGICAL\_MIN 0x1

[ 93](group__usb__hid__definitions.md#gaab6aec72cca41670464605d6970ad553)#define HID\_ITEM\_TAG\_LOGICAL\_MAX 0x2

[ 95](group__usb__hid__definitions.md#ga6dfdd60d0b985d683a58ad752d3ef3c3)#define HID\_ITEM\_TAG\_PHYSICAL\_MIN 0x3

[ 97](group__usb__hid__definitions.md#gaa68bd8a73cee33d810484f4aa3f30e92)#define HID\_ITEM\_TAG\_PHYSICAL\_MAX 0x4

[ 99](group__usb__hid__definitions.md#ga7c6d81ee211814ec9b5d17f95e57639b)#define HID\_ITEM\_TAG\_UNIT\_EXPONENT 0x5

[ 101](group__usb__hid__definitions.md#ga98267b4ff28f435d67d2a7bf1055fc7c)#define HID\_ITEM\_TAG\_UNIT 0x6

[ 103](group__usb__hid__definitions.md#ga0e6d7a56593bd25a5e15683e9271bb19)#define HID\_ITEM\_TAG\_REPORT\_SIZE 0x7

[ 105](group__usb__hid__definitions.md#ga76cd3a266ae5d5e29292d93caceece72)#define HID\_ITEM\_TAG\_REPORT\_ID 0x8

[ 107](group__usb__hid__definitions.md#ga1847701703130ce8f57547811f28b2b4)#define HID\_ITEM\_TAG\_REPORT\_COUNT 0x9

108

[ 110](group__usb__hid__definitions.md#gaefd616ecaa8fc8762e65ec9d7b01f0cd)#define HID\_ITEM\_TAG\_USAGE 0x0

[ 112](group__usb__hid__definitions.md#ga4e6f4133f12276f4f9fa51ab06580676)#define HID\_ITEM\_TAG\_USAGE\_MIN 0x1

[ 114](group__usb__hid__definitions.md#gac2a0aff74caff6c03511fc0b6db6167b)#define HID\_ITEM\_TAG\_USAGE\_MAX 0x2

115

[ 117](group__usb__hid__definitions.md#gaca1e227f9241c217b8b1aeae6c4bd672)#define HID\_COLLECTION\_PHYSICAL 0x00

[ 119](group__usb__hid__definitions.md#ga2e5e5ad0919fbaea0e6f8e5d86f4c2fd)#define HID\_COLLECTION\_APPLICATION 0x01

[ 121](group__usb__hid__definitions.md#ga904a372a663bd7d9205402a3a014c04b)#define HID\_COLLECTION\_LOGICAL 0x02

[ 123](group__usb__hid__definitions.md#gac58ab4780c054754b7f94ff97a152694)#define HID\_COLLECTION\_REPORT 0x03

[ 125](group__usb__hid__definitions.md#ga8e1610365a1556adf7121cc3b1f83080)#define HID\_COLLECTION\_NAMED\_ARRAY 0x04

[ 127](group__usb__hid__definitions.md#ga64af797e424ea1e2c02c745f30721e48)#define HID\_COLLECTION\_USAGE\_SWITCH 0x05

[ 129](group__usb__hid__definitions.md#gaabc1c6bed23b88f4cdc89d5347595d4f)#define HID\_COLLECTION\_MODIFIER 0x06

130

131

132/\* Usage page and IDs from Universal Serial Bus HID Usage Tables \*/

133

[ 135](group__usb__hid__definitions.md#gacb3fc5b0f838dfa5eb95e9e1bf52b589)#define HID\_USAGE\_GEN\_DESKTOP 0x01

[ 137](group__usb__hid__definitions.md#ga1fdbfffd0b343cec1480e9f0347efa5d)#define HID\_USAGE\_GEN\_KEYBOARD 0x07

[ 139](group__usb__hid__definitions.md#gae632e9a37203506c051c3cacfdf0c2c7)#define HID\_USAGE\_GEN\_LEDS 0x08

[ 141](group__usb__hid__definitions.md#ga13401731a0ead5448a0823d0f6142404)#define HID\_USAGE\_GEN\_BUTTON 0x09

142

[ 144](group__usb__hid__definitions.md#ga1441517d7c57529dcf726a1dd8b09a07)#define HID\_USAGE\_GEN\_DESKTOP\_UNDEFINED 0x00

[ 146](group__usb__hid__definitions.md#ga77a7162980a77efa1e2e7b21942bb7dd)#define HID\_USAGE\_GEN\_DESKTOP\_POINTER 0x01

[ 148](group__usb__hid__definitions.md#ga983274dd50058de26e0e86d10d50e81a)#define HID\_USAGE\_GEN\_DESKTOP\_MOUSE 0x02

[ 150](group__usb__hid__definitions.md#gada59a9f3aeaeaefc6112c7d9902b2d6d)#define HID\_USAGE\_GEN\_DESKTOP\_JOYSTICK 0x04

[ 152](group__usb__hid__definitions.md#ga17404e33133204a538f976d321c84ff0)#define HID\_USAGE\_GEN\_DESKTOP\_GAMEPAD 0x05

[ 154](group__usb__hid__definitions.md#ga0bdaa3d23c79204a1064cb53b279bd77)#define HID\_USAGE\_GEN\_DESKTOP\_KEYBOARD 0x06

[ 156](group__usb__hid__definitions.md#ga69f8e44306828b3f44d3a7704ff07807)#define HID\_USAGE\_GEN\_DESKTOP\_KEYPAD 0x07

[ 158](group__usb__hid__definitions.md#gae283a3558ba536e163140a3b6cdbb273)#define HID\_USAGE\_GEN\_DESKTOP\_X 0x30

[ 160](group__usb__hid__definitions.md#gad1ab1f8f9c8a4a80bfc8e3a327e3b2fb)#define HID\_USAGE\_GEN\_DESKTOP\_Y 0x31

[ 162](group__usb__hid__definitions.md#gaa8c772d412ac1ac7a36739c52f04c0a9)#define HID\_USAGE\_GEN\_DESKTOP\_WHEEL 0x38

163

167

172

[ 181](group__usb__hid__items.md#ga4e9dc6652402e0b87e1313c143737ed4)#define HID\_ITEM(bTag, bType, bSize) (((bTag & 0xF) << 4) | \

182 ((bType & 0x3) << 2) | (bSize & 0x3))

183

[ 193](group__usb__hid__items.md#ga8646699330c45fb008d50b54be339c6c)#define HID\_INPUT(a) \

194 HID\_ITEM(HID\_ITEM\_TAG\_INPUT, HID\_ITEM\_TYPE\_MAIN, 1), a

195

[ 204](group__usb__hid__items.md#ga6ef7aa576bf69f9ba5f93df500a1403c)#define HID\_OUTPUT(a) \

205 HID\_ITEM(HID\_ITEM\_TAG\_OUTPUT, HID\_ITEM\_TYPE\_MAIN, 1), a

206

[ 213](group__usb__hid__items.md#ga951a415e05e95492250d4fb43a37090d)#define HID\_FEATURE(a) \

214 HID\_ITEM(HID\_ITEM\_TAG\_FEATURE, HID\_ITEM\_TYPE\_MAIN, 1), a

215

[ 225](group__usb__hid__items.md#gad010ed98662b0e653754caff1dfd352f)#define HID\_COLLECTION(a) \

226 HID\_ITEM(HID\_ITEM\_TAG\_COLLECTION, HID\_ITEM\_TYPE\_MAIN, 1), a

227

[ 236](group__usb__hid__items.md#ga6cd6affb9d52e0bf98c7a5c83d03a764)#define HID\_END\_COLLECTION \

237 HID\_ITEM(HID\_ITEM\_TAG\_COLLECTION\_END, HID\_ITEM\_TYPE\_MAIN, 0)

238

[ 248](group__usb__hid__items.md#ga30dc3f62583822ba27edd984dc2dec39)#define HID\_USAGE\_PAGE(page) \

249 HID\_ITEM(HID\_ITEM\_TAG\_USAGE\_PAGE, HID\_ITEM\_TYPE\_GLOBAL, 1), page

250

[ 260](group__usb__hid__items.md#gacd141f6ede5122f260cd50338649d458)#define HID\_LOGICAL\_MIN8(a) \

261 HID\_ITEM(HID\_ITEM\_TAG\_LOGICAL\_MIN, HID\_ITEM\_TYPE\_GLOBAL, 1), a

262

[ 272](group__usb__hid__items.md#ga2f6b809ae85b6716ade8c52da4fa56af)#define HID\_LOGICAL\_MAX8(a) \

273 HID\_ITEM(HID\_ITEM\_TAG\_LOGICAL\_MAX, HID\_ITEM\_TYPE\_GLOBAL, 1), a

274

[ 282](group__usb__hid__items.md#ga5e290798d55bccd7474dbfb6bc2d1033)#define HID\_LOGICAL\_MIN16(a, b) \

283 HID\_ITEM(HID\_ITEM\_TAG\_LOGICAL\_MIN, HID\_ITEM\_TYPE\_GLOBAL, 2), a, b

284

[ 292](group__usb__hid__items.md#ga9b804d676812dcfb0ec12f3aa887e37f)#define HID\_LOGICAL\_MAX16(a, b) \

293 HID\_ITEM(HID\_ITEM\_TAG\_LOGICAL\_MAX, HID\_ITEM\_TYPE\_GLOBAL, 2), a, b

294

[ 304](group__usb__hid__items.md#gad4b2ff8642676d692fd0d56ab0cbeaa7)#define HID\_LOGICAL\_MIN32(a, b, c, d) \

305 HID\_ITEM(HID\_ITEM\_TAG\_LOGICAL\_MIN, HID\_ITEM\_TYPE\_GLOBAL, 3), a, b, c, d

306

[ 316](group__usb__hid__items.md#gae9d17e753685b0df6c53f942ce9c95d2)#define HID\_LOGICAL\_MAX32(a, b, c, d) \

317 HID\_ITEM(HID\_ITEM\_TAG\_LOGICAL\_MAX, HID\_ITEM\_TYPE\_GLOBAL, 3), a, b, c, d

318

[ 328](group__usb__hid__items.md#ga3135a21a63c491daf8647fa771def0e7)#define HID\_REPORT\_SIZE(size) \

329 HID\_ITEM(HID\_ITEM\_TAG\_REPORT\_SIZE, HID\_ITEM\_TYPE\_GLOBAL, 1), size

330

[ 337](group__usb__hid__items.md#ga1b45fce2c7df2847b1326fca29cef389)#define HID\_REPORT\_ID(id) \

338 HID\_ITEM(HID\_ITEM\_TAG\_REPORT\_ID, HID\_ITEM\_TYPE\_GLOBAL, 1), id

339

[ 349](group__usb__hid__items.md#ga71192f2a55f05456b893069ebfbc5b98)#define HID\_REPORT\_COUNT(count) \

350 HID\_ITEM(HID\_ITEM\_TAG\_REPORT\_COUNT, HID\_ITEM\_TYPE\_GLOBAL, 1), count

351

[ 361](group__usb__hid__items.md#gac8429a70866a898887ead55664e04bd7)#define HID\_USAGE(idx) \

362 HID\_ITEM(HID\_ITEM\_TAG\_USAGE, HID\_ITEM\_TYPE\_LOCAL, 1), idx

363

[ 373](group__usb__hid__items.md#gabf53f1e2eae6d686aeb7d62cc46b22ad)#define HID\_USAGE\_MIN8(a) \

374 HID\_ITEM(HID\_ITEM\_TAG\_USAGE\_MIN, HID\_ITEM\_TYPE\_LOCAL, 1), a

375

[ 385](group__usb__hid__items.md#gae7fc9684ef10f50d69df6f495cc09e91)#define HID\_USAGE\_MAX8(a) \

386 HID\_ITEM(HID\_ITEM\_TAG\_USAGE\_MAX, HID\_ITEM\_TYPE\_LOCAL, 1), a

387

[ 398](group__usb__hid__items.md#ga0dbc847d11cf64676f7cfc51b54150fa)#define HID\_USAGE\_MIN16(a, b) \

399 HID\_ITEM(HID\_ITEM\_TAG\_USAGE\_MIN, HID\_ITEM\_TYPE\_LOCAL, 2), a, b

400

[ 411](group__usb__hid__items.md#gadd11a09546bc275c82e7a992cb9441cc)#define HID\_USAGE\_MAX16(a, b) \

412 HID\_ITEM(HID\_ITEM\_TAG\_USAGE\_MAX, HID\_ITEM\_TYPE\_LOCAL, 2), a, b

413

417

422

[ 428](group__usb__hid__mk__report__desc.md#ga3696f0782268d504b0c8bb540236779f)#define HID\_MOUSE\_REPORT\_DESC(bcnt) { \

429 HID\_USAGE\_PAGE(HID\_USAGE\_GEN\_DESKTOP), \

430 HID\_USAGE(HID\_USAGE\_GEN\_DESKTOP\_MOUSE), \

431 HID\_COLLECTION(HID\_COLLECTION\_APPLICATION), \

432 HID\_USAGE(HID\_USAGE\_GEN\_DESKTOP\_POINTER), \

433 HID\_COLLECTION(HID\_COLLECTION\_PHYSICAL), \

434 /\* Bits used for button signalling \*/ \

435 HID\_USAGE\_PAGE(HID\_USAGE\_GEN\_BUTTON), \

436 HID\_USAGE\_MIN8(1), \

437 HID\_USAGE\_MAX8(bcnt), \

438 HID\_LOGICAL\_MIN8(0), \

439 HID\_LOGICAL\_MAX8(1), \

440 HID\_REPORT\_SIZE(1), \

441 HID\_REPORT\_COUNT(bcnt), \

442 /\* HID\_INPUT (Data,Var,Abs) \*/ \

443 HID\_INPUT(0x02), \

444 /\* Unused bits \*/ \

445 HID\_REPORT\_SIZE(8 - bcnt), \

446 HID\_REPORT\_COUNT(1), \

447 /\* HID\_INPUT (Cnst,Ary,Abs) \*/ \

448 HID\_INPUT(1), \

449 /\* X and Y axis, scroll \*/ \

450 HID\_USAGE\_PAGE(HID\_USAGE\_GEN\_DESKTOP), \

451 HID\_USAGE(HID\_USAGE\_GEN\_DESKTOP\_X), \

452 HID\_USAGE(HID\_USAGE\_GEN\_DESKTOP\_Y), \

453 HID\_USAGE(HID\_USAGE\_GEN\_DESKTOP\_WHEEL), \

454 HID\_LOGICAL\_MIN8(-127), \

455 HID\_LOGICAL\_MAX8(127), \

456 HID\_REPORT\_SIZE(8), \

457 HID\_REPORT\_COUNT(3), \

458 /\* HID\_INPUT (Data,Var,Rel) \*/ \

459 HID\_INPUT(0x06), \

460 HID\_END\_COLLECTION, \

461 HID\_END\_COLLECTION, \

462}

463

[ 467](group__usb__hid__mk__report__desc.md#gaea973ffbe1612187c90614133956cfd6)#define HID\_KEYBOARD\_REPORT\_DESC() { \

468 HID\_USAGE\_PAGE(HID\_USAGE\_GEN\_DESKTOP), \

469 HID\_USAGE(HID\_USAGE\_GEN\_DESKTOP\_KEYBOARD), \

470 HID\_COLLECTION(HID\_COLLECTION\_APPLICATION), \

471 HID\_USAGE\_PAGE(HID\_USAGE\_GEN\_DESKTOP\_KEYPAD), \

472 /\* HID\_USAGE\_MINIMUM(Keyboard LeftControl) \*/ \

473 HID\_USAGE\_MIN8(0xE0), \

474 /\* HID\_USAGE\_MAXIMUM(Keyboard Right GUI) \*/ \

475 HID\_USAGE\_MAX8(0xE7), \

476 HID\_LOGICAL\_MIN8(0), \

477 HID\_LOGICAL\_MAX8(1), \

478 HID\_REPORT\_SIZE(1), \

479 HID\_REPORT\_COUNT(8), \

480 /\* HID\_INPUT(Data,Var,Abs) \*/ \

481 HID\_INPUT(0x02), \

482 HID\_REPORT\_SIZE(8), \

483 HID\_REPORT\_COUNT(1), \

484 /\* HID\_INPUT(Cnst,Var,Abs) \*/ \

485 HID\_INPUT(0x03), \

486 HID\_REPORT\_SIZE(1), \

487 HID\_REPORT\_COUNT(5), \

488 HID\_USAGE\_PAGE(HID\_USAGE\_GEN\_LEDS), \

489 /\* HID\_USAGE\_MINIMUM(Num Lock) \*/ \

490 HID\_USAGE\_MIN8(1), \

491 /\* HID\_USAGE\_MAXIMUM(Kana) \*/ \

492 HID\_USAGE\_MAX8(5), \

493 /\* HID\_OUTPUT(Data,Var,Abs) \*/ \

494 HID\_OUTPUT(0x02), \

495 HID\_REPORT\_SIZE(3), \

496 HID\_REPORT\_COUNT(1), \

497 /\* HID\_OUTPUT(Cnst,Var,Abs) \*/ \

498 HID\_OUTPUT(0x03), \

499 HID\_REPORT\_SIZE(8), \

500 HID\_REPORT\_COUNT(6), \

501 HID\_LOGICAL\_MIN8(0), \

502 HID\_LOGICAL\_MAX8(101), \

503 HID\_USAGE\_PAGE(HID\_USAGE\_GEN\_DESKTOP\_KEYPAD), \

504 /\* HID\_USAGE\_MIN8(Reserved) \*/ \

505 HID\_USAGE\_MIN8(0), \

506 /\* HID\_USAGE\_MAX8(Keyboard Application) \*/ \

507 HID\_USAGE\_MAX8(101), \

508 /\* HID\_INPUT (Data,Ary,Abs) \*/ \

509 HID\_INPUT(0x00), \

510 HID\_END\_COLLECTION, \

511}

512

[ 516](group__usb__hid__mk__report__desc.md#ga4f2bb15109c64695f852afd6bd99e3bf)enum [hid\_kbd\_code](group__usb__hid__mk__report__desc.md#ga4f2bb15109c64695f852afd6bd99e3bf) {

[ 517](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa5413afa6a28a21dd52f07db101f2d139) [HID\_KEY\_A](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa5413afa6a28a21dd52f07db101f2d139) = 4,

[ 518](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfabb0b25fe8c201dc75b72c7b078f745d6) [HID\_KEY\_B](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfabb0b25fe8c201dc75b72c7b078f745d6) = 5,

[ 519](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa932c610512cc99157654c3997bc2b922) [HID\_KEY\_C](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa932c610512cc99157654c3997bc2b922) = 6,

[ 520](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfabc172093417a4c40a7443eee551e9700) [HID\_KEY\_D](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfabc172093417a4c40a7443eee551e9700) = 7,

[ 521](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaff7192b9ddd4228e02c44b6fb2d7bf85) [HID\_KEY\_E](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaff7192b9ddd4228e02c44b6fb2d7bf85) = 8,

[ 522](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfacc002ca9f0f3bdc01b4de42d00e5560b) [HID\_KEY\_F](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfacc002ca9f0f3bdc01b4de42d00e5560b) = 9,

[ 523](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa1eadd56346bbd64b1c33fa5393f65bda) [HID\_KEY\_G](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa1eadd56346bbd64b1c33fa5393f65bda) = 10,

[ 524](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4bfc341fccde664ec9267af6e705ba0c) [HID\_KEY\_H](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4bfc341fccde664ec9267af6e705ba0c) = 11,

[ 525](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfafcd25dc5bba218f7097698f8f49fdc45) [HID\_KEY\_I](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfafcd25dc5bba218f7097698f8f49fdc45) = 12,

[ 526](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa2a78196208c634941d63429cd1e1df7a) [HID\_KEY\_J](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa2a78196208c634941d63429cd1e1df7a) = 13,

[ 527](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4ceddaaaa90d84f0afb3e1ee9a35a976) [HID\_KEY\_K](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4ceddaaaa90d84f0afb3e1ee9a35a976) = 14,

[ 528](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaf5de66adc9eb2aa183eab1e23f977894) [HID\_KEY\_L](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaf5de66adc9eb2aa183eab1e23f977894) = 15,

[ 529](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4f8174feca1eb72901576c4e24c8f8a9) [HID\_KEY\_M](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4f8174feca1eb72901576c4e24c8f8a9) = 16,

[ 530](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfab4d202043e8b0b7a8c2d4c519fd1eb07) [HID\_KEY\_N](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfab4d202043e8b0b7a8c2d4c519fd1eb07) = 17,

[ 531](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfad8884ef7e77722099e6bd61265f6564c) [HID\_KEY\_O](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfad8884ef7e77722099e6bd61265f6564c) = 18,

[ 532](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaca0480331288d15eccec9f072f123817) [HID\_KEY\_P](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaca0480331288d15eccec9f072f123817) = 19,

[ 533](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa05fb920f8129f57dd350036f17fbe519) [HID\_KEY\_Q](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa05fb920f8129f57dd350036f17fbe519) = 20,

[ 534](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa037de00c763ae6b270895b7a5f0f57a7) [HID\_KEY\_R](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa037de00c763ae6b270895b7a5f0f57a7) = 21,

[ 535](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfae6a84e8474b6c3e8f9f7d344408cfa0b) [HID\_KEY\_S](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfae6a84e8474b6c3e8f9f7d344408cfa0b) = 22,

[ 536](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa893799f48b30c438349335556a0e15b6) [HID\_KEY\_T](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa893799f48b30c438349335556a0e15b6) = 23,

[ 537](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfab3c7c9f3a73e83623c651cdfddddeb05) [HID\_KEY\_U](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfab3c7c9f3a73e83623c651cdfddddeb05) = 24,

[ 538](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa02f14e6303b4d2e4e46747324d649dda) [HID\_KEY\_V](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa02f14e6303b4d2e4e46747324d649dda) = 25,

[ 539](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfadf81a88f3f92f15e2abec83911bf3732) [HID\_KEY\_W](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfadf81a88f3f92f15e2abec83911bf3732) = 26,

[ 540](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa9f3b8bb63f6628db9a1678b72ec12b6d) [HID\_KEY\_X](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa9f3b8bb63f6628db9a1678b72ec12b6d) = 27,

[ 541](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4ca2ebe26c09f2400a8ebc0aa445ce89) [HID\_KEY\_Y](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4ca2ebe26c09f2400a8ebc0aa445ce89) = 28,

[ 542](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaa5cd01ad23ede98de1ae176920b8fc8f) [HID\_KEY\_Z](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaa5cd01ad23ede98de1ae176920b8fc8f) = 29,

[ 543](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa039ced168420140b97e2d0676e1bb12a) [HID\_KEY\_1](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa039ced168420140b97e2d0676e1bb12a) = 30,

[ 544](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfae98dd71460def5e66fcf32e9783b96ea) [HID\_KEY\_2](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfae98dd71460def5e66fcf32e9783b96ea) = 31,

[ 545](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaf58d848786f8d2dfac702f7fae178311) [HID\_KEY\_3](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaf58d848786f8d2dfac702f7fae178311) = 32,

[ 546](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa17019d72e84302486f72f7d8101baca5) [HID\_KEY\_4](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa17019d72e84302486f72f7d8101baca5) = 33,

[ 547](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaf32ab36da2e30066c9ed2816596011c8) [HID\_KEY\_5](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaf32ab36da2e30066c9ed2816596011c8) = 34,

[ 548](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfae16b76c1bf9f7aa58a1b1c556a6b6022) [HID\_KEY\_6](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfae16b76c1bf9f7aa58a1b1c556a6b6022) = 35,

[ 549](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa5887a1854f7d0787121bd75034cdd726) [HID\_KEY\_7](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa5887a1854f7d0787121bd75034cdd726) = 36,

[ 550](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa1761228849d7dc2b84d0565d3337b2e2) [HID\_KEY\_8](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa1761228849d7dc2b84d0565d3337b2e2) = 37,

[ 551](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa758aec2540a6a2153702d6905c44ce52) [HID\_KEY\_9](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa758aec2540a6a2153702d6905c44ce52) = 38,

[ 552](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa856ca663233681e789ef4aa94c44ebaf) [HID\_KEY\_0](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa856ca663233681e789ef4aa94c44ebaf) = 39,

[ 553](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaeeab6ddad27c449cbc44ca2458912a75) [HID\_KEY\_ENTER](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaeeab6ddad27c449cbc44ca2458912a75) = 40,

[ 554](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa763b39fe76a92c4cc1fc32f47d2a760a) [HID\_KEY\_ESC](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa763b39fe76a92c4cc1fc32f47d2a760a) = 41,

[ 555](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfafd6cf6a44966d518b173df4ed57ae720) [HID\_KEY\_BACKSPACE](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfafd6cf6a44966d518b173df4ed57ae720) = 42,

[ 556](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa5a6c79e8ea85f6593c06d19098d69a03) [HID\_KEY\_TAB](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa5a6c79e8ea85f6593c06d19098d69a03) = 43,

[ 557](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaf4fc3d7b4b86f9f095cec624d190ebec) [HID\_KEY\_SPACE](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaf4fc3d7b4b86f9f095cec624d190ebec) = 44,

[ 558](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaa59864204064d3e8fac5271b69a7da23) [HID\_KEY\_MINUS](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaa59864204064d3e8fac5271b69a7da23) = 45,

[ 559](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfac8d82858905175ba79c24b0be1b1b1a8) [HID\_KEY\_EQUAL](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfac8d82858905175ba79c24b0be1b1b1a8) = 46,

[ 560](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfac232473666b21ca772c84b68be6c1f3d) [HID\_KEY\_LEFTBRACE](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfac232473666b21ca772c84b68be6c1f3d) = 47,

[ 561](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaef692bd882621d292255cb99d4697513) [HID\_KEY\_RIGHTBRACE](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaef692bd882621d292255cb99d4697513) = 48,

[ 562](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa25ba5457bc128593b1624d95ec536182) [HID\_KEY\_BACKSLASH](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa25ba5457bc128593b1624d95ec536182) = 49,

[ 563](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa0d57ce7c99d06ee9b15fef880af075eb) [HID\_KEY\_HASH](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa0d57ce7c99d06ee9b15fef880af075eb) = 50, /\* Non-US # and ~ \*/

[ 564](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa3743f920856a12e726e1be05932c7411) [HID\_KEY\_SEMICOLON](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa3743f920856a12e726e1be05932c7411) = 51,

[ 565](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa7325a5bd52e9dc0cc38a85609b1c55ab) [HID\_KEY\_APOSTROPHE](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa7325a5bd52e9dc0cc38a85609b1c55ab) = 52,

[ 566](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa8b84c64da5b8c5f5d99b86c1cfe09ffc) [HID\_KEY\_GRAVE](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa8b84c64da5b8c5f5d99b86c1cfe09ffc) = 53,

[ 567](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaa81aa5b3424f02fdf02295de47b11b19) [HID\_KEY\_COMMA](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaa81aa5b3424f02fdf02295de47b11b19) = 54,

[ 568](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa403fe927ebb0014e2c1b3dc25e1d9779) [HID\_KEY\_DOT](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa403fe927ebb0014e2c1b3dc25e1d9779) = 55,

[ 569](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa24c2c93a1c895745828311affc011dea) [HID\_KEY\_SLASH](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa24c2c93a1c895745828311affc011dea) = 56,

[ 570](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4d40549a59fdcfdd0b2d592a6675bc89) [HID\_KEY\_CAPSLOCK](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4d40549a59fdcfdd0b2d592a6675bc89) = 57,

[ 571](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa9642163abbbad8aa5c7088c8529aadd7) [HID\_KEY\_F1](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa9642163abbbad8aa5c7088c8529aadd7) = 58,

[ 572](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa9ce331f5f41ba3e3e05f485bc2d4138e) [HID\_KEY\_F2](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa9ce331f5f41ba3e3e05f485bc2d4138e) = 59,

[ 573](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa76adde1d9295cf62e7efb35e27911a1e) [HID\_KEY\_F3](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa76adde1d9295cf62e7efb35e27911a1e) = 60,

[ 574](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaa9956a2b95afe1a05fda65db5cc66467) [HID\_KEY\_F4](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaa9956a2b95afe1a05fda65db5cc66467) = 61,

[ 575](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bface9e8d409d981f193f69fc5b29f38ca7) [HID\_KEY\_F5](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bface9e8d409d981f193f69fc5b29f38ca7) = 62,

[ 576](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfabc92147e725c8108c18f4e03005afbdc) [HID\_KEY\_F6](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfabc92147e725c8108c18f4e03005afbdc) = 63,

[ 577](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa1e2eabf8b9fa6cbfea613696b2c4122a) [HID\_KEY\_F7](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa1e2eabf8b9fa6cbfea613696b2c4122a) = 64,

[ 578](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa5092add2863231d273ba60cd583ebe33) [HID\_KEY\_F8](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa5092add2863231d273ba60cd583ebe33) = 65,

[ 579](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa5a09deabde1a3a44378b7de44dad27b6) [HID\_KEY\_F9](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa5a09deabde1a3a44378b7de44dad27b6) = 66,

[ 580](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfac2c4a3aec85b4d8171de4429ccabbe19) [HID\_KEY\_F10](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfac2c4a3aec85b4d8171de4429ccabbe19) = 67,

[ 581](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa76bb35a0f71733b0a0f1bd7e3837064c) [HID\_KEY\_F11](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa76bb35a0f71733b0a0f1bd7e3837064c) = 68,

[ 582](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfab44ba4426c1574f4b296794b7bfe2172) [HID\_KEY\_F12](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfab44ba4426c1574f4b296794b7bfe2172) = 69,

[ 583](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfae5405b62cb20962cb5864ba6e90a4ab2) [HID\_KEY\_SYSRQ](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfae5405b62cb20962cb5864ba6e90a4ab2) = 70, /\* PRINTSCREEN \*/

[ 584](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfae16bd57629c7aba96a554d0446e83d98) [HID\_KEY\_SCROLLLOCK](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfae16bd57629c7aba96a554d0446e83d98) = 71,

[ 585](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa1905733a0fe81f78e0752e3b0bb99c69) [HID\_KEY\_PAUSE](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa1905733a0fe81f78e0752e3b0bb99c69) = 72,

[ 586](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa1e1c320cea0644c3dc38da06c865837b) [HID\_KEY\_INSERT](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa1e1c320cea0644c3dc38da06c865837b) = 73,

[ 587](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa5fc1127fe9014018f4831cbf272c883b) [HID\_KEY\_HOME](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa5fc1127fe9014018f4831cbf272c883b) = 74,

[ 588](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa2468ac3b37d38b6158cd989ed54bcd8c) [HID\_KEY\_PAGEUP](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa2468ac3b37d38b6158cd989ed54bcd8c) = 75,

[ 589](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfae8f5051cb476c3e9253b008094c431fc) [HID\_KEY\_DELETE](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfae8f5051cb476c3e9253b008094c431fc) = 76,

[ 590](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa8f933f0f6e5a1a3c3cdc1819ffcdce63) [HID\_KEY\_END](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa8f933f0f6e5a1a3c3cdc1819ffcdce63) = 77,

[ 591](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaf7615ff4f608d64ae20a61540d939065) [HID\_KEY\_PAGEDOWN](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaf7615ff4f608d64ae20a61540d939065) = 78,

[ 592](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4c203feb452e3212089e8246b8d75f6c) [HID\_KEY\_RIGHT](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4c203feb452e3212089e8246b8d75f6c) = 79,

[ 593](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaf7d3c678a8ac31916068a0c5aff54d4b) [HID\_KEY\_LEFT](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaf7d3c678a8ac31916068a0c5aff54d4b) = 80,

[ 594](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa9e2597c2a109abda1c63c8d5ca5376b3) [HID\_KEY\_DOWN](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa9e2597c2a109abda1c63c8d5ca5376b3) = 81,

[ 595](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaf5fe431b55adf16d82604e0fc2239090) [HID\_KEY\_UP](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaf5fe431b55adf16d82604e0fc2239090) = 82,

[ 596](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfafec8c71efd5ee9decd156f0d33739fbe) [HID\_KEY\_NUMLOCK](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfafec8c71efd5ee9decd156f0d33739fbe) = 83,

[ 597](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa44e83040efab214dcfe462ac0d338e0c) [HID\_KEY\_KPSLASH](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa44e83040efab214dcfe462ac0d338e0c) = 84, /\* NUMPAD DIVIDE \*/

[ 598](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaff47eb8157a7118183573e3aefb7df08) [HID\_KEY\_KPASTERISK](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaff47eb8157a7118183573e3aefb7df08) = 85, /\* NUMPAD MULTIPLY \*/

[ 599](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa6fb35c78b12ae434cb7a7280501886e9) [HID\_KEY\_KPMINUS](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa6fb35c78b12ae434cb7a7280501886e9) = 86,

[ 600](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa2cb7852467d2ebd785e2f7556383a883) [HID\_KEY\_KPPLUS](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa2cb7852467d2ebd785e2f7556383a883) = 87,

[ 601](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfab5b923992d0bdc176f716cd8ace3a66e) [HID\_KEY\_KPENTER](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfab5b923992d0bdc176f716cd8ace3a66e) = 88,

[ 602](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa7eea75b0eb4b4f0306daa3e6fccf09e4) [HID\_KEY\_KP\_1](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa7eea75b0eb4b4f0306daa3e6fccf09e4) = 89,

[ 603](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa68db65e7002e7cc599394a7eea116e3c) [HID\_KEY\_KP\_2](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa68db65e7002e7cc599394a7eea116e3c) = 90,

[ 604](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4210f9a5ae469c8b863b28b9b2d8189d) [HID\_KEY\_KP\_3](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4210f9a5ae469c8b863b28b9b2d8189d) = 91,

[ 605](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa48eefeeb48a942eaaa0726bd4a2df01d) [HID\_KEY\_KP\_4](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa48eefeeb48a942eaaa0726bd4a2df01d) = 92,

[ 606](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa1b8d299d56a0289ae15cbf8c67e36a7c) [HID\_KEY\_KP\_5](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa1b8d299d56a0289ae15cbf8c67e36a7c) = 93,

[ 607](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa90f2c51ad42e335a474061c4d5e4e5a9) [HID\_KEY\_KP\_6](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa90f2c51ad42e335a474061c4d5e4e5a9) = 94,

[ 608](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa1e191017084fadf830a7394de0e1cc05) [HID\_KEY\_KP\_7](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa1e191017084fadf830a7394de0e1cc05) = 95,

[ 609](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfadd7c795e2c9c212a4adeaba904bda447) [HID\_KEY\_KP\_8](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfadd7c795e2c9c212a4adeaba904bda447) = 96,

[ 610](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bface8d41615c6afd45724f4b6d16238c36) [HID\_KEY\_KP\_9](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bface8d41615c6afd45724f4b6d16238c36) = 97,

[ 611](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4ae4af2b06f6f2585a598353bfef9af7) [HID\_KEY\_KP\_0](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4ae4af2b06f6f2585a598353bfef9af7) = 98,

612};

613

[ 617](group__usb__hid__mk__report__desc.md#ga12f11556b697518b00fa86eb040f9eb8)enum [hid\_kbd\_modifier](group__usb__hid__mk__report__desc.md#ga12f11556b697518b00fa86eb040f9eb8) {

[ 618](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8a79b0eb4f485bedb745180f1b8798c603) [HID\_KBD\_MODIFIER\_NONE](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8a79b0eb4f485bedb745180f1b8798c603) = 0x00,

[ 619](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8a4df663509a05599fd66657cfc90a37c7) [HID\_KBD\_MODIFIER\_LEFT\_CTRL](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8a4df663509a05599fd66657cfc90a37c7) = 0x01,

[ 620](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8aba69ca183306d3d1427b66666803e57f) [HID\_KBD\_MODIFIER\_LEFT\_SHIFT](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8aba69ca183306d3d1427b66666803e57f) = 0x02,

[ 621](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8a829d884291b546c0e276afa4ad92ac18) [HID\_KBD\_MODIFIER\_LEFT\_ALT](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8a829d884291b546c0e276afa4ad92ac18) = 0x04,

[ 622](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8a718c92a2d0ca9dd6603825b97a99fc77) [HID\_KBD\_MODIFIER\_LEFT\_UI](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8a718c92a2d0ca9dd6603825b97a99fc77) = 0x08,

[ 623](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8a8e346c0e9c7d5b58e4b8748380423a92) [HID\_KBD\_MODIFIER\_RIGHT\_CTRL](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8a8e346c0e9c7d5b58e4b8748380423a92) = 0x10,

[ 624](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8affdba298e8860b000a0916be7495c2dc) [HID\_KBD\_MODIFIER\_RIGHT\_SHIFT](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8affdba298e8860b000a0916be7495c2dc) = 0x20,

[ 625](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8a85ce29a6ab9feef68350deca92001db2) [HID\_KBD\_MODIFIER\_RIGHT\_ALT](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8a85ce29a6ab9feef68350deca92001db2) = 0x40,

[ 626](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8a1b4b75cd0364824cbfc80dfc68e294dd) [HID\_KBD\_MODIFIER\_RIGHT\_UI](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8a1b4b75cd0364824cbfc80dfc68e294dd) = 0x80,

627};

628

[ 632](group__usb__hid__mk__report__desc.md#ga8cef56ba216d0a01c6cc89f723d1740b)enum [hid\_kbd\_led](group__usb__hid__mk__report__desc.md#ga8cef56ba216d0a01c6cc89f723d1740b) {

[ 633](group__usb__hid__mk__report__desc.md#gga8cef56ba216d0a01c6cc89f723d1740ba6cb2e1acb52cc5bab8dd3aa6ef6ac01b) [HID\_KBD\_LED\_NUM\_LOCK](group__usb__hid__mk__report__desc.md#gga8cef56ba216d0a01c6cc89f723d1740ba6cb2e1acb52cc5bab8dd3aa6ef6ac01b) = 0x01,

[ 634](group__usb__hid__mk__report__desc.md#gga8cef56ba216d0a01c6cc89f723d1740baa17e5130bd8c45eb21661d8783517266) [HID\_KBD\_LED\_CAPS\_LOCK](group__usb__hid__mk__report__desc.md#gga8cef56ba216d0a01c6cc89f723d1740baa17e5130bd8c45eb21661d8783517266) = 0x02,

[ 635](group__usb__hid__mk__report__desc.md#gga8cef56ba216d0a01c6cc89f723d1740ba6ea943f59b98680aefd0d5be4ef22e36) [HID\_KBD\_LED\_SCROLL\_LOCK](group__usb__hid__mk__report__desc.md#gga8cef56ba216d0a01c6cc89f723d1740ba6ea943f59b98680aefd0d5be4ef22e36) = 0x04,

[ 636](group__usb__hid__mk__report__desc.md#gga8cef56ba216d0a01c6cc89f723d1740bad62692e71ae45351311c8bf2ce13e3c9) [HID\_KBD\_LED\_COMPOSE](group__usb__hid__mk__report__desc.md#gga8cef56ba216d0a01c6cc89f723d1740bad62692e71ae45351311c8bf2ce13e3c9) = 0x08,

[ 637](group__usb__hid__mk__report__desc.md#gga8cef56ba216d0a01c6cc89f723d1740bafd5d599c1955bdb1c62c7b17286b37f1) [HID\_KBD\_LED\_KANA](group__usb__hid__mk__report__desc.md#gga8cef56ba216d0a01c6cc89f723d1740bafd5d599c1955bdb1c62c7b17286b37f1) = 0x10,

638};

639

643

647

648#ifdef \_\_cplusplus

649}

650#endif

651

652#endif /\* ZEPHYR\_INCLUDE\_USB\_CLASS\_HID\_H\_ \*/

[hid\_kbd\_modifier](group__usb__hid__mk__report__desc.md#ga12f11556b697518b00fa86eb040f9eb8)

hid\_kbd\_modifier

HID keyboard modifiers.

**Definition** hid.h:617

[hid\_kbd\_code](group__usb__hid__mk__report__desc.md#ga4f2bb15109c64695f852afd6bd99e3bf)

hid\_kbd\_code

HID keyboard button codes.

**Definition** hid.h:516

[hid\_kbd\_led](group__usb__hid__mk__report__desc.md#ga8cef56ba216d0a01c6cc89f723d1740b)

hid\_kbd\_led

HID keyboard LEDs.

**Definition** hid.h:632

[HID\_KBD\_MODIFIER\_RIGHT\_UI](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8a1b4b75cd0364824cbfc80dfc68e294dd)

@ HID\_KBD\_MODIFIER\_RIGHT\_UI

**Definition** hid.h:626

[HID\_KBD\_MODIFIER\_LEFT\_CTRL](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8a4df663509a05599fd66657cfc90a37c7)

@ HID\_KBD\_MODIFIER\_LEFT\_CTRL

**Definition** hid.h:619

[HID\_KBD\_MODIFIER\_LEFT\_UI](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8a718c92a2d0ca9dd6603825b97a99fc77)

@ HID\_KBD\_MODIFIER\_LEFT\_UI

**Definition** hid.h:622

[HID\_KBD\_MODIFIER\_NONE](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8a79b0eb4f485bedb745180f1b8798c603)

@ HID\_KBD\_MODIFIER\_NONE

**Definition** hid.h:618

[HID\_KBD\_MODIFIER\_LEFT\_ALT](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8a829d884291b546c0e276afa4ad92ac18)

@ HID\_KBD\_MODIFIER\_LEFT\_ALT

**Definition** hid.h:621

[HID\_KBD\_MODIFIER\_RIGHT\_ALT](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8a85ce29a6ab9feef68350deca92001db2)

@ HID\_KBD\_MODIFIER\_RIGHT\_ALT

**Definition** hid.h:625

[HID\_KBD\_MODIFIER\_RIGHT\_CTRL](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8a8e346c0e9c7d5b58e4b8748380423a92)

@ HID\_KBD\_MODIFIER\_RIGHT\_CTRL

**Definition** hid.h:623

[HID\_KBD\_MODIFIER\_LEFT\_SHIFT](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8aba69ca183306d3d1427b66666803e57f)

@ HID\_KBD\_MODIFIER\_LEFT\_SHIFT

**Definition** hid.h:620

[HID\_KBD\_MODIFIER\_RIGHT\_SHIFT](group__usb__hid__mk__report__desc.md#gga12f11556b697518b00fa86eb040f9eb8affdba298e8860b000a0916be7495c2dc)

@ HID\_KBD\_MODIFIER\_RIGHT\_SHIFT

**Definition** hid.h:624

[HID\_KEY\_V](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa02f14e6303b4d2e4e46747324d649dda)

@ HID\_KEY\_V

**Definition** hid.h:538

[HID\_KEY\_R](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa037de00c763ae6b270895b7a5f0f57a7)

@ HID\_KEY\_R

**Definition** hid.h:534

[HID\_KEY\_1](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa039ced168420140b97e2d0676e1bb12a)

@ HID\_KEY\_1

**Definition** hid.h:543

[HID\_KEY\_Q](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa05fb920f8129f57dd350036f17fbe519)

@ HID\_KEY\_Q

**Definition** hid.h:533

[HID\_KEY\_HASH](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa0d57ce7c99d06ee9b15fef880af075eb)

@ HID\_KEY\_HASH

**Definition** hid.h:563

[HID\_KEY\_4](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa17019d72e84302486f72f7d8101baca5)

@ HID\_KEY\_4

**Definition** hid.h:546

[HID\_KEY\_8](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa1761228849d7dc2b84d0565d3337b2e2)

@ HID\_KEY\_8

**Definition** hid.h:550

[HID\_KEY\_PAUSE](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa1905733a0fe81f78e0752e3b0bb99c69)

@ HID\_KEY\_PAUSE

**Definition** hid.h:585

[HID\_KEY\_KP\_5](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa1b8d299d56a0289ae15cbf8c67e36a7c)

@ HID\_KEY\_KP\_5

**Definition** hid.h:606

[HID\_KEY\_KP\_7](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa1e191017084fadf830a7394de0e1cc05)

@ HID\_KEY\_KP\_7

**Definition** hid.h:608

[HID\_KEY\_INSERT](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa1e1c320cea0644c3dc38da06c865837b)

@ HID\_KEY\_INSERT

**Definition** hid.h:586

[HID\_KEY\_F7](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa1e2eabf8b9fa6cbfea613696b2c4122a)

@ HID\_KEY\_F7

**Definition** hid.h:577

[HID\_KEY\_G](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa1eadd56346bbd64b1c33fa5393f65bda)

@ HID\_KEY\_G

**Definition** hid.h:523

[HID\_KEY\_PAGEUP](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa2468ac3b37d38b6158cd989ed54bcd8c)

@ HID\_KEY\_PAGEUP

**Definition** hid.h:588

[HID\_KEY\_SLASH](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa24c2c93a1c895745828311affc011dea)

@ HID\_KEY\_SLASH

**Definition** hid.h:569

[HID\_KEY\_BACKSLASH](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa25ba5457bc128593b1624d95ec536182)

@ HID\_KEY\_BACKSLASH

**Definition** hid.h:562

[HID\_KEY\_J](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa2a78196208c634941d63429cd1e1df7a)

@ HID\_KEY\_J

**Definition** hid.h:526

[HID\_KEY\_KPPLUS](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa2cb7852467d2ebd785e2f7556383a883)

@ HID\_KEY\_KPPLUS

**Definition** hid.h:600

[HID\_KEY\_SEMICOLON](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa3743f920856a12e726e1be05932c7411)

@ HID\_KEY\_SEMICOLON

**Definition** hid.h:564

[HID\_KEY\_DOT](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa403fe927ebb0014e2c1b3dc25e1d9779)

@ HID\_KEY\_DOT

**Definition** hid.h:568

[HID\_KEY\_KP\_3](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4210f9a5ae469c8b863b28b9b2d8189d)

@ HID\_KEY\_KP\_3

**Definition** hid.h:604

[HID\_KEY\_KPSLASH](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa44e83040efab214dcfe462ac0d338e0c)

@ HID\_KEY\_KPSLASH

**Definition** hid.h:597

[HID\_KEY\_KP\_4](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa48eefeeb48a942eaaa0726bd4a2df01d)

@ HID\_KEY\_KP\_4

**Definition** hid.h:605

[HID\_KEY\_KP\_0](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4ae4af2b06f6f2585a598353bfef9af7)

@ HID\_KEY\_KP\_0

**Definition** hid.h:611

[HID\_KEY\_H](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4bfc341fccde664ec9267af6e705ba0c)

@ HID\_KEY\_H

**Definition** hid.h:524

[HID\_KEY\_RIGHT](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4c203feb452e3212089e8246b8d75f6c)

@ HID\_KEY\_RIGHT

**Definition** hid.h:592

[HID\_KEY\_Y](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4ca2ebe26c09f2400a8ebc0aa445ce89)

@ HID\_KEY\_Y

**Definition** hid.h:541

[HID\_KEY\_K](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4ceddaaaa90d84f0afb3e1ee9a35a976)

@ HID\_KEY\_K

**Definition** hid.h:527

[HID\_KEY\_CAPSLOCK](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4d40549a59fdcfdd0b2d592a6675bc89)

@ HID\_KEY\_CAPSLOCK

**Definition** hid.h:570

[HID\_KEY\_M](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa4f8174feca1eb72901576c4e24c8f8a9)

@ HID\_KEY\_M

**Definition** hid.h:529

[HID\_KEY\_F8](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa5092add2863231d273ba60cd583ebe33)

@ HID\_KEY\_F8

**Definition** hid.h:578

[HID\_KEY\_A](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa5413afa6a28a21dd52f07db101f2d139)

@ HID\_KEY\_A

**Definition** hid.h:517

[HID\_KEY\_7](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa5887a1854f7d0787121bd75034cdd726)

@ HID\_KEY\_7

**Definition** hid.h:549

[HID\_KEY\_F9](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa5a09deabde1a3a44378b7de44dad27b6)

@ HID\_KEY\_F9

**Definition** hid.h:579

[HID\_KEY\_TAB](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa5a6c79e8ea85f6593c06d19098d69a03)

@ HID\_KEY\_TAB

**Definition** hid.h:556

[HID\_KEY\_HOME](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa5fc1127fe9014018f4831cbf272c883b)

@ HID\_KEY\_HOME

**Definition** hid.h:587

[HID\_KEY\_KP\_2](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa68db65e7002e7cc599394a7eea116e3c)

@ HID\_KEY\_KP\_2

**Definition** hid.h:603

[HID\_KEY\_KPMINUS](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa6fb35c78b12ae434cb7a7280501886e9)

@ HID\_KEY\_KPMINUS

**Definition** hid.h:599

[HID\_KEY\_APOSTROPHE](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa7325a5bd52e9dc0cc38a85609b1c55ab)

@ HID\_KEY\_APOSTROPHE

**Definition** hid.h:565

[HID\_KEY\_9](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa758aec2540a6a2153702d6905c44ce52)

@ HID\_KEY\_9

**Definition** hid.h:551

[HID\_KEY\_ESC](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa763b39fe76a92c4cc1fc32f47d2a760a)

@ HID\_KEY\_ESC

**Definition** hid.h:554

[HID\_KEY\_F3](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa76adde1d9295cf62e7efb35e27911a1e)

@ HID\_KEY\_F3

**Definition** hid.h:573

[HID\_KEY\_F11](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa76bb35a0f71733b0a0f1bd7e3837064c)

@ HID\_KEY\_F11

**Definition** hid.h:581

[HID\_KEY\_KP\_1](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa7eea75b0eb4b4f0306daa3e6fccf09e4)

@ HID\_KEY\_KP\_1

**Definition** hid.h:602

[HID\_KEY\_0](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa856ca663233681e789ef4aa94c44ebaf)

@ HID\_KEY\_0

**Definition** hid.h:552

[HID\_KEY\_T](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa893799f48b30c438349335556a0e15b6)

@ HID\_KEY\_T

**Definition** hid.h:536

[HID\_KEY\_GRAVE](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa8b84c64da5b8c5f5d99b86c1cfe09ffc)

@ HID\_KEY\_GRAVE

**Definition** hid.h:566

[HID\_KEY\_END](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa8f933f0f6e5a1a3c3cdc1819ffcdce63)

@ HID\_KEY\_END

**Definition** hid.h:590

[HID\_KEY\_KP\_6](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa90f2c51ad42e335a474061c4d5e4e5a9)

@ HID\_KEY\_KP\_6

**Definition** hid.h:607

[HID\_KEY\_C](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa932c610512cc99157654c3997bc2b922)

@ HID\_KEY\_C

**Definition** hid.h:519

[HID\_KEY\_F1](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa9642163abbbad8aa5c7088c8529aadd7)

@ HID\_KEY\_F1

**Definition** hid.h:571

[HID\_KEY\_F2](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa9ce331f5f41ba3e3e05f485bc2d4138e)

@ HID\_KEY\_F2

**Definition** hid.h:572

[HID\_KEY\_DOWN](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa9e2597c2a109abda1c63c8d5ca5376b3)

@ HID\_KEY\_DOWN

**Definition** hid.h:594

[HID\_KEY\_X](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfa9f3b8bb63f6628db9a1678b72ec12b6d)

@ HID\_KEY\_X

**Definition** hid.h:540

[HID\_KEY\_MINUS](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaa59864204064d3e8fac5271b69a7da23)

@ HID\_KEY\_MINUS

**Definition** hid.h:558

[HID\_KEY\_Z](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaa5cd01ad23ede98de1ae176920b8fc8f)

@ HID\_KEY\_Z

**Definition** hid.h:542

[HID\_KEY\_COMMA](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaa81aa5b3424f02fdf02295de47b11b19)

@ HID\_KEY\_COMMA

**Definition** hid.h:567

[HID\_KEY\_F4](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaa9956a2b95afe1a05fda65db5cc66467)

@ HID\_KEY\_F4

**Definition** hid.h:574

[HID\_KEY\_U](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfab3c7c9f3a73e83623c651cdfddddeb05)

@ HID\_KEY\_U

**Definition** hid.h:537

[HID\_KEY\_F12](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfab44ba4426c1574f4b296794b7bfe2172)

@ HID\_KEY\_F12

**Definition** hid.h:582

[HID\_KEY\_N](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfab4d202043e8b0b7a8c2d4c519fd1eb07)

@ HID\_KEY\_N

**Definition** hid.h:530

[HID\_KEY\_KPENTER](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfab5b923992d0bdc176f716cd8ace3a66e)

@ HID\_KEY\_KPENTER

**Definition** hid.h:601

[HID\_KEY\_B](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfabb0b25fe8c201dc75b72c7b078f745d6)

@ HID\_KEY\_B

**Definition** hid.h:518

[HID\_KEY\_D](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfabc172093417a4c40a7443eee551e9700)

@ HID\_KEY\_D

**Definition** hid.h:520

[HID\_KEY\_F6](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfabc92147e725c8108c18f4e03005afbdc)

@ HID\_KEY\_F6

**Definition** hid.h:576

[HID\_KEY\_LEFTBRACE](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfac232473666b21ca772c84b68be6c1f3d)

@ HID\_KEY\_LEFTBRACE

**Definition** hid.h:560

[HID\_KEY\_F10](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfac2c4a3aec85b4d8171de4429ccabbe19)

@ HID\_KEY\_F10

**Definition** hid.h:580

[HID\_KEY\_EQUAL](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfac8d82858905175ba79c24b0be1b1b1a8)

@ HID\_KEY\_EQUAL

**Definition** hid.h:559

[HID\_KEY\_P](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaca0480331288d15eccec9f072f123817)

@ HID\_KEY\_P

**Definition** hid.h:532

[HID\_KEY\_F](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfacc002ca9f0f3bdc01b4de42d00e5560b)

@ HID\_KEY\_F

**Definition** hid.h:522

[HID\_KEY\_KP\_9](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bface8d41615c6afd45724f4b6d16238c36)

@ HID\_KEY\_KP\_9

**Definition** hid.h:610

[HID\_KEY\_F5](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bface9e8d409d981f193f69fc5b29f38ca7)

@ HID\_KEY\_F5

**Definition** hid.h:575

[HID\_KEY\_O](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfad8884ef7e77722099e6bd61265f6564c)

@ HID\_KEY\_O

**Definition** hid.h:531

[HID\_KEY\_KP\_8](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfadd7c795e2c9c212a4adeaba904bda447)

@ HID\_KEY\_KP\_8

**Definition** hid.h:609

[HID\_KEY\_W](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfadf81a88f3f92f15e2abec83911bf3732)

@ HID\_KEY\_W

**Definition** hid.h:539

[HID\_KEY\_6](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfae16b76c1bf9f7aa58a1b1c556a6b6022)

@ HID\_KEY\_6

**Definition** hid.h:548

[HID\_KEY\_SCROLLLOCK](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfae16bd57629c7aba96a554d0446e83d98)

@ HID\_KEY\_SCROLLLOCK

**Definition** hid.h:584

[HID\_KEY\_SYSRQ](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfae5405b62cb20962cb5864ba6e90a4ab2)

@ HID\_KEY\_SYSRQ

**Definition** hid.h:583

[HID\_KEY\_S](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfae6a84e8474b6c3e8f9f7d344408cfa0b)

@ HID\_KEY\_S

**Definition** hid.h:535

[HID\_KEY\_DELETE](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfae8f5051cb476c3e9253b008094c431fc)

@ HID\_KEY\_DELETE

**Definition** hid.h:589

[HID\_KEY\_2](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfae98dd71460def5e66fcf32e9783b96ea)

@ HID\_KEY\_2

**Definition** hid.h:544

[HID\_KEY\_ENTER](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaeeab6ddad27c449cbc44ca2458912a75)

@ HID\_KEY\_ENTER

**Definition** hid.h:553

[HID\_KEY\_RIGHTBRACE](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaef692bd882621d292255cb99d4697513)

@ HID\_KEY\_RIGHTBRACE

**Definition** hid.h:561

[HID\_KEY\_5](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaf32ab36da2e30066c9ed2816596011c8)

@ HID\_KEY\_5

**Definition** hid.h:547

[HID\_KEY\_SPACE](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaf4fc3d7b4b86f9f095cec624d190ebec)

@ HID\_KEY\_SPACE

**Definition** hid.h:557

[HID\_KEY\_3](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaf58d848786f8d2dfac702f7fae178311)

@ HID\_KEY\_3

**Definition** hid.h:545

[HID\_KEY\_L](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaf5de66adc9eb2aa183eab1e23f977894)

@ HID\_KEY\_L

**Definition** hid.h:528

[HID\_KEY\_UP](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaf5fe431b55adf16d82604e0fc2239090)

@ HID\_KEY\_UP

**Definition** hid.h:595

[HID\_KEY\_PAGEDOWN](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaf7615ff4f608d64ae20a61540d939065)

@ HID\_KEY\_PAGEDOWN

**Definition** hid.h:591

[HID\_KEY\_LEFT](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaf7d3c678a8ac31916068a0c5aff54d4b)

@ HID\_KEY\_LEFT

**Definition** hid.h:593

[HID\_KEY\_I](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfafcd25dc5bba218f7097698f8f49fdc45)

@ HID\_KEY\_I

**Definition** hid.h:525

[HID\_KEY\_BACKSPACE](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfafd6cf6a44966d518b173df4ed57ae720)

@ HID\_KEY\_BACKSPACE

**Definition** hid.h:555

[HID\_KEY\_NUMLOCK](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfafec8c71efd5ee9decd156f0d33739fbe)

@ HID\_KEY\_NUMLOCK

**Definition** hid.h:596

[HID\_KEY\_KPASTERISK](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaff47eb8157a7118183573e3aefb7df08)

@ HID\_KEY\_KPASTERISK

**Definition** hid.h:598

[HID\_KEY\_E](group__usb__hid__mk__report__desc.md#gga4f2bb15109c64695f852afd6bd99e3bfaff7192b9ddd4228e02c44b6fb2d7bf85)

@ HID\_KEY\_E

**Definition** hid.h:521

[HID\_KBD\_LED\_NUM\_LOCK](group__usb__hid__mk__report__desc.md#gga8cef56ba216d0a01c6cc89f723d1740ba6cb2e1acb52cc5bab8dd3aa6ef6ac01b)

@ HID\_KBD\_LED\_NUM\_LOCK

**Definition** hid.h:633

[HID\_KBD\_LED\_SCROLL\_LOCK](group__usb__hid__mk__report__desc.md#gga8cef56ba216d0a01c6cc89f723d1740ba6ea943f59b98680aefd0d5be4ef22e36)

@ HID\_KBD\_LED\_SCROLL\_LOCK

**Definition** hid.h:635

[HID\_KBD\_LED\_CAPS\_LOCK](group__usb__hid__mk__report__desc.md#gga8cef56ba216d0a01c6cc89f723d1740baa17e5130bd8c45eb21661d8783517266)

@ HID\_KBD\_LED\_CAPS\_LOCK

**Definition** hid.h:634

[HID\_KBD\_LED\_COMPOSE](group__usb__hid__mk__report__desc.md#gga8cef56ba216d0a01c6cc89f723d1740bad62692e71ae45351311c8bf2ce13e3c9)

@ HID\_KBD\_LED\_COMPOSE

**Definition** hid.h:636

[HID\_KBD\_LED\_KANA](group__usb__hid__mk__report__desc.md#gga8cef56ba216d0a01c6cc89f723d1740bafd5d599c1955bdb1c62c7b17286b37f1)

@ HID\_KBD\_LED\_KANA

**Definition** hid.h:637

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [class](dir_c68ea25cffcb2672410964c117624aed.md)
- [hid.h](hid_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

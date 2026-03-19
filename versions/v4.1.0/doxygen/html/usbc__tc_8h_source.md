---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/usbc__tc_8h_source.html
original_path: doxygen/html/usbc__tc_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbc\_tc.h

[Go to the documentation of this file.](usbc__tc_8h.md)

1/\*

2 \* Copyright 2022 The Chromium OS Authors

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

13

14#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_USBC\_USBC\_TC\_H\_

15#define ZEPHYR\_INCLUDE\_DRIVERS\_USBC\_USBC\_TC\_H\_

16

23

24#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

25

26#ifdef \_\_cplusplus

27extern "C" {

28#endif

29

[ 34](group__usb__type__c.md#ga025aeca5768435b245ecb9fe8bfa29c8)#define TC\_V\_SINK\_DISCONNECT\_MIN\_MV 800

35

[ 40](group__usb__type__c.md#ga151c5852b9d2ad3f6f7f0869505e854b)#define TC\_V\_SINK\_DISCONNECT\_MAX\_MV 3670

41

[ 47](group__usb__type__c.md#gace546c362f92ed1ba0455a5d8006357c)#define TC\_T\_VBUS\_ON\_MAX\_MS 275

48

[ 54](group__usb__type__c.md#ga2d6440c7b480ee75ccadf8242e29e7e9)#define TC\_T\_VBUS\_OFF\_MAX\_MS 650

55

[ 60](group__usb__type__c.md#gaf2cbadac415eedae8c4db3dc91f3623b)#define TC\_T\_VCONN\_ON\_MAX\_MS 2

61

[ 67](group__usb__type__c.md#ga24837587c589d85bc48bed2a6815798d)#define TC\_T\_VCONN\_ON\_PA\_MAX\_MS 100

68

[ 74](group__usb__type__c.md#ga2f347359b4ffc4478338cbbc8a62d4d9)#define TC\_T\_VCONN\_OFF\_MAX\_MS 35

75

[ 81](group__usb__type__c.md#gaa1291eb2b50b59a9746ffe0658d60258)#define TC\_T\_SINK\_ADJ\_MAX\_MS 60

82

[ 87](group__usb__type__c.md#gab042a018fbc99a402ab23371c3d6fe47)#define TC\_T\_DRP\_MIN\_MS 50

88

[ 93](group__usb__type__c.md#gaba34e5687c2e12984629a9297f0e7813)#define TC\_T\_DRP\_MAX\_MS 100

94

[ 100](group__usb__type__c.md#ga6ab07167512c79d9587d547902443049)#define TC\_T\_DRP\_TRANSITION\_MIN\_MS 0

101

[ 107](group__usb__type__c.md#gae1e9780a30b644a1f15463cba216e385)#define TC\_T\_DRP\_TRANSITION\_MAX\_MS 1

108

[ 113](group__usb__type__c.md#ga1ee8d43885ebc26a2f4da640d5758188)#define TC\_T\_DRP\_TRY\_MIN\_MS 75

114

[ 119](group__usb__type__c.md#ga95cd5ac306f2d27440b980593c759f07)#define TC\_T\_DRP\_TRY\_MAX\_MS 150

120

[ 125](group__usb__type__c.md#gae19a1dc5b950495866359deef2cd6c7c)#define TC\_T\_DRP\_TRY\_WAIT\_MIN\_MS 400

126

[ 131](group__usb__type__c.md#ga0eb5b996e1678f3830c38584f84a6268)#define TC\_T\_DRP\_TRY\_WAIT\_MAX\_MS 800

132

[ 137](group__usb__type__c.md#ga45be1dbb0a9ad2e9a9b0549f953cb8c2)#define TC\_T\_TRY\_TIMEOUT\_MIN\_MS 550

138

[ 143](group__usb__type__c.md#gae3e98e8acbfb5fa7f398dea64265cb0a)#define TC\_T\_TRY\_TIMEOUT\_MAX\_MS 1100

144

[ 150](group__usb__type__c.md#ga50a154595c40bba3e46751f6f46df848)#define TC\_T\_VPD\_DETACH\_MIN\_MS 10

151

[ 157](group__usb__type__c.md#ga33b792a38351081f316e6f854710a96e)#define TC\_T\_VPD\_DETACH\_MAX\_MS 20

158

[ 163](group__usb__type__c.md#gae059acba0f01f24cb682ee2c3ded59d9)#define TC\_T\_CC\_DEBOUNCE\_MIN\_MS 100

164

[ 169](group__usb__type__c.md#gac4eb3955701e40ddabf8b2afae68ea8d)#define TC\_T\_CC\_DEBOUNCE\_MAX\_MS 200

170

[ 176](group__usb__type__c.md#ga46e03b71bd69657786755bd716383fe7)#define TC\_T\_PD\_DEBOUNCE\_MIN\_MS 10

177

[ 183](group__usb__type__c.md#ga4327b09ebf8f27675ac8fc6125ab6bbc)#define TC\_T\_PD\_DEBOUNCE\_MAX\_MS 20

184

[ 190](group__usb__type__c.md#ga21ce86c10d5b0b9e3e7fa08e902d6f77)#define TC\_T\_TRY\_CC\_DEBOUNCE\_MIN\_MS 10

191

[ 197](group__usb__type__c.md#ga1b736eb0d37209d95f4e305baaefc1f0)#define TC\_T\_TRY\_CC\_DEBOUNCE\_MAX\_MS 10

198

[ 203](group__usb__type__c.md#ga70a063a53fba92977ed35169743368f0)#define TC\_T\_ERROR\_RECOVERY\_SELF\_POWERED\_MIN\_MS 25

204

[ 210](group__usb__type__c.md#gaaee37a1ff25fc71a5c66f04b327f9b04)#define TC\_T\_ERROR\_RECOVERY\_SOURCE\_MIN\_MS 240

211

[ 217](group__usb__type__c.md#ga22273343713c29c84f7ff95fc34e9573)#define TC\_T\_RP\_VALUE\_CHANGE\_MIN\_MS 10

218

[ 224](group__usb__type__c.md#gade24fb4955e80390e4f47b86fbce1874)#define TC\_T\_RP\_VALUE\_CHANGE\_MAX\_MS 20

225

[ 231](group__usb__type__c.md#ga767c754753786419f50faa2888859cdb)#define TC\_T\_SRC\_DISCONNECT\_MIN\_MS 0

232

[ 238](group__usb__type__c.md#ga92232c9516031a90da1a6fbd1be03b73)#define TC\_T\_SRC\_DISCONNECT\_MAX\_MS 20

239

[ 244](group__usb__type__c.md#ga5ccab8bbe9c386d47f705551c3b5f918)#define TC\_T\_NO\_TOGGLE\_CONNECT\_MIN\_MS 0

245

[ 250](group__usb__type__c.md#ga7e56e9ff953b5fc425c4304831c19738)#define TC\_T\_NO\_TOGGLE\_CONNECT\_MAX\_MS 5

251

[ 257](group__usb__type__c.md#ga44d9260612a215407d79415b30e63613)#define TC\_T\_ONE\_PORT\_TOGGLE\_CONNECT\_MIN\_MS 0

258

[ 264](group__usb__type__c.md#ga62662057432f68c48dd59be8b28297d4)#define TC\_T\_ONE\_PORT\_TOGGLE\_CONNECT\_MAX\_MS 80

265

[ 271](group__usb__type__c.md#ga96c2bf7f24deb8e8a0d327536a0a023e)#define TC\_T\_TWO\_PORT\_TOGGLE\_CONNECT\_MIN\_MS 0

272

[ 278](group__usb__type__c.md#gad911bc40a17b676c8a87d87d51fc0fbf)#define TC\_T\_TWO\_PORT\_TOGGLE\_CONNECT\_MAX\_MS 510

279

[ 287](group__usb__type__c.md#gae2ebe887ccb4f9549d130e85b999062e)#define TC\_T\_VPDCTDD\_MIN\_US 30

288

[ 296](group__usb__type__c.md#ga75223d9754d7ce76e302ee2ed40d11ef)#define TC\_T\_VPDCTDD\_MAX\_MS 5

297

[ 303](group__usb__type__c.md#ga56ece8323bd0a8e4ce0755e0e9e06f96)#define TC\_T\_VPDDISABLE\_MIN\_MS 25

304

[ 308](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c)enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) {

[ 310](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca1f4b82ea64d23167df5083fd7550cf05) [TC\_CC\_VOLT\_OPEN](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca1f4b82ea64d23167df5083fd7550cf05) = 0,

[ 312](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca17a8d72f4dc6b29e1d4ad35a4f1531ea) [TC\_CC\_VOLT\_RA](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca17a8d72f4dc6b29e1d4ad35a4f1531ea) = 1,

[ 314](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca2267bbcda871c265e77228a5fe6342a9) [TC\_CC\_VOLT\_RD](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca2267bbcda871c265e77228a5fe6342a9) = 2,

[ 316](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca06bd58eb73aa7f097046e7b88fde0293) [TC\_CC\_VOLT\_RP\_DEF](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca06bd58eb73aa7f097046e7b88fde0293) = 5,

317 /\*8 Port partner is applying Rp (1.5A) \*/

[ 318](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca3cc0d3c1ac9775b1b8ba77b87868bc72) [TC\_CC\_VOLT\_RP\_1A5](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca3cc0d3c1ac9775b1b8ba77b87868bc72) = 6,

[ 320](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca3965e449dbcc8ca6e87d72cd5a73f0ca) [TC\_CC\_VOLT\_RP\_3A0](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca3965e449dbcc8ca6e87d72cd5a73f0ca) = 7,

321};

322

[ 326](group__usb__type__c.md#ga015455a6c5620dfc96cfb713bbb72161)enum [tc\_vbus\_level](group__usb__type__c.md#ga015455a6c5620dfc96cfb713bbb72161) {

[ 328](group__usb__type__c.md#gga015455a6c5620dfc96cfb713bbb72161a86bf4c0568d7a7ec89180e8e36c91827) [TC\_VBUS\_SAFE0V](group__usb__type__c.md#gga015455a6c5620dfc96cfb713bbb72161a86bf4c0568d7a7ec89180e8e36c91827) = 0,

[ 330](group__usb__type__c.md#gga015455a6c5620dfc96cfb713bbb72161a33f8f0dac47bfaffe331553cd42495f5) [TC\_VBUS\_PRESENT](group__usb__type__c.md#gga015455a6c5620dfc96cfb713bbb72161a33f8f0dac47bfaffe331553cd42495f5) = 1,

[ 332](group__usb__type__c.md#gga015455a6c5620dfc96cfb713bbb72161a84aaa14f5d6dd4b1bf52564af73f24bc) [TC\_VBUS\_REMOVED](group__usb__type__c.md#gga015455a6c5620dfc96cfb713bbb72161a84aaa14f5d6dd4b1bf52564af73f24bc) = 2

333};

334

[ 338](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5)enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5) {

[ 340](group__usb__type__c.md#gga4e0eec97f7c5c97b87eff9561deea2d5a22d5e50479ca672f0469af9006b4f4bb) [TC\_RP\_USB](group__usb__type__c.md#gga4e0eec97f7c5c97b87eff9561deea2d5a22d5e50479ca672f0469af9006b4f4bb) = 0,

[ 342](group__usb__type__c.md#gga4e0eec97f7c5c97b87eff9561deea2d5a1c74df7e2b6bbe75d8c61ca4a7202a28) [TC\_RP\_1A5](group__usb__type__c.md#gga4e0eec97f7c5c97b87eff9561deea2d5a1c74df7e2b6bbe75d8c61ca4a7202a28) = 1,

[ 344](group__usb__type__c.md#gga4e0eec97f7c5c97b87eff9561deea2d5afa7eda9742f3670a90736a52620cfe3c) [TC\_RP\_3A0](group__usb__type__c.md#gga4e0eec97f7c5c97b87eff9561deea2d5afa7eda9742f3670a90736a52620cfe3c) = 2,

[ 346](group__usb__type__c.md#gga4e0eec97f7c5c97b87eff9561deea2d5a215508ac427e2cc53478e5f096a400d1) [TC\_RP\_RESERVED](group__usb__type__c.md#gga4e0eec97f7c5c97b87eff9561deea2d5a215508ac427e2cc53478e5f096a400d1) = 3

347};

348

[ 352](group__usb__type__c.md#ga0200c820510eb786f3ca30a9b5f7aada)enum [tc\_cc\_pull](group__usb__type__c.md#ga0200c820510eb786f3ca30a9b5f7aada) {

[ 354](group__usb__type__c.md#gga0200c820510eb786f3ca30a9b5f7aadaaf52a9f9d10c81fca5b048ad2230cf1e8) [TC\_CC\_RA](group__usb__type__c.md#gga0200c820510eb786f3ca30a9b5f7aadaaf52a9f9d10c81fca5b048ad2230cf1e8) = 0,

[ 356](group__usb__type__c.md#gga0200c820510eb786f3ca30a9b5f7aadaa7a0a6a716cb42af3a572f43bedc2a322) [TC\_CC\_RP](group__usb__type__c.md#gga0200c820510eb786f3ca30a9b5f7aadaa7a0a6a716cb42af3a572f43bedc2a322) = 1,

[ 358](group__usb__type__c.md#gga0200c820510eb786f3ca30a9b5f7aadaa60a4e008afce1c9395a0fb6d34767c6e) [TC\_CC\_RD](group__usb__type__c.md#gga0200c820510eb786f3ca30a9b5f7aadaa60a4e008afce1c9395a0fb6d34767c6e) = 2,

[ 360](group__usb__type__c.md#gga0200c820510eb786f3ca30a9b5f7aadaa4859548c59439c79e3ad080e1fa07fa8) [TC\_CC\_OPEN](group__usb__type__c.md#gga0200c820510eb786f3ca30a9b5f7aadaa4859548c59439c79e3ad080e1fa07fa8) = 3,

[ 362](group__usb__type__c.md#gga0200c820510eb786f3ca30a9b5f7aadaa95c81809d680f28281e9dcaef4fff35e) [TC\_RA\_RD](group__usb__type__c.md#gga0200c820510eb786f3ca30a9b5f7aadaa95c81809d680f28281e9dcaef4fff35e) = 4

363};

364

[ 369](group__usb__type__c.md#ga8707ac194510396d55a40887673b53ca)enum [tc\_cable\_plug](group__usb__type__c.md#ga8707ac194510396d55a40887673b53ca) {

370 /\* Message originated from a DFP or UFP \*/

[ 371](group__usb__type__c.md#gga8707ac194510396d55a40887673b53caad1092c45d3fad497dbafe15fd9f1c3b3) [PD\_PLUG\_FROM\_DFP\_UFP](group__usb__type__c.md#gga8707ac194510396d55a40887673b53caad1092c45d3fad497dbafe15fd9f1c3b3) = 0,

372 /\* Message originated from a Cable Plug or VPD \*/

[ 373](group__usb__type__c.md#gga8707ac194510396d55a40887673b53caa49960a4dee1da0c7330cce2b13c4c0ed) [PD\_PLUG\_FROM\_CABLE\_VPD](group__usb__type__c.md#gga8707ac194510396d55a40887673b53caa49960a4dee1da0c7330cce2b13c4c0ed) = 1

374};

375

[ 379](group__usb__type__c.md#gaa6dda0612045b5f55b9d8ba63d2b9f9d)enum [tc\_power\_role](group__usb__type__c.md#gaa6dda0612045b5f55b9d8ba63d2b9f9d) {

[ 381](group__usb__type__c.md#ggaa6dda0612045b5f55b9d8ba63d2b9f9da0023468cf2e977c8372899e6f1a0aafb) [TC\_ROLE\_SINK](group__usb__type__c.md#ggaa6dda0612045b5f55b9d8ba63d2b9f9da0023468cf2e977c8372899e6f1a0aafb) = 0,

[ 383](group__usb__type__c.md#ggaa6dda0612045b5f55b9d8ba63d2b9f9da1b8caf27ae76de5ea874b0e52adc4cf1) [TC\_ROLE\_SOURCE](group__usb__type__c.md#ggaa6dda0612045b5f55b9d8ba63d2b9f9da1b8caf27ae76de5ea874b0e52adc4cf1) = 1

384};

385

[ 389](group__usb__type__c.md#ga6b98bbe238e62cfd5531688494a63de2)enum [tc\_data\_role](group__usb__type__c.md#ga6b98bbe238e62cfd5531688494a63de2) {

[ 391](group__usb__type__c.md#gga6b98bbe238e62cfd5531688494a63de2a9472c4319bf0be6937436e1602c7b414) [TC\_ROLE\_UFP](group__usb__type__c.md#gga6b98bbe238e62cfd5531688494a63de2a9472c4319bf0be6937436e1602c7b414) = 0,

[ 393](group__usb__type__c.md#gga6b98bbe238e62cfd5531688494a63de2a812112dccb0c3d8dd555d351a7f5b9e1) [TC\_ROLE\_DFP](group__usb__type__c.md#gga6b98bbe238e62cfd5531688494a63de2a812112dccb0c3d8dd555d351a7f5b9e1) = 1,

[ 395](group__usb__type__c.md#gga6b98bbe238e62cfd5531688494a63de2a155c3d22f151d83899f46e516e88a058) [TC\_ROLE\_DISCONNECTED](group__usb__type__c.md#gga6b98bbe238e62cfd5531688494a63de2a155c3d22f151d83899f46e516e88a058) = 2

396};

397

[ 401](group__usb__type__c.md#gac5b4b58840c9b076a869a5816ba100db)enum [tc\_cc\_polarity](group__usb__type__c.md#gac5b4b58840c9b076a869a5816ba100db) {

[ 403](group__usb__type__c.md#ggac5b4b58840c9b076a869a5816ba100dba1ace08cbeb63866305ccfb0c3bf338c2) [TC\_POLARITY\_CC1](group__usb__type__c.md#ggac5b4b58840c9b076a869a5816ba100dba1ace08cbeb63866305ccfb0c3bf338c2) = 0,

[ 405](group__usb__type__c.md#ggac5b4b58840c9b076a869a5816ba100dbae3ad03c80e84e32f8974a14e815ed910) [TC\_POLARITY\_CC2](group__usb__type__c.md#ggac5b4b58840c9b076a869a5816ba100dbae3ad03c80e84e32f8974a14e815ed910) = 1

406};

407

[ 411](group__usb__type__c.md#ga5bb2cfcf3ab60423048db38103657197)enum [tc\_cc\_states](group__usb__type__c.md#ga5bb2cfcf3ab60423048db38103657197) {

[ 413](group__usb__type__c.md#gga5bb2cfcf3ab60423048db38103657197a21cf3890c4a2fa6ee9f137f2b22e51f0) [TC\_CC\_NONE](group__usb__type__c.md#gga5bb2cfcf3ab60423048db38103657197a21cf3890c4a2fa6ee9f137f2b22e51f0) = 0,

414

416

[ 418](group__usb__type__c.md#gga5bb2cfcf3ab60423048db38103657197a90544a6af90af7722cec8ffe83f752f0) [TC\_CC\_UFP\_NONE](group__usb__type__c.md#gga5bb2cfcf3ab60423048db38103657197a90544a6af90af7722cec8ffe83f752f0) = 1,

[ 420](group__usb__type__c.md#gga5bb2cfcf3ab60423048db38103657197a4b841a1438a120652ab78fb3ae2c7dea) [TC\_CC\_UFP\_AUDIO\_ACC](group__usb__type__c.md#gga5bb2cfcf3ab60423048db38103657197a4b841a1438a120652ab78fb3ae2c7dea) = 2,

[ 422](group__usb__type__c.md#gga5bb2cfcf3ab60423048db38103657197aaba130e5d3d999794eb87e2b8a09cf78) [TC\_CC\_UFP\_DEBUG\_ACC](group__usb__type__c.md#gga5bb2cfcf3ab60423048db38103657197aaba130e5d3d999794eb87e2b8a09cf78) = 3,

[ 424](group__usb__type__c.md#gga5bb2cfcf3ab60423048db38103657197a0cfcabb4325e4b59213002aaeda75524) [TC\_CC\_UFP\_ATTACHED](group__usb__type__c.md#gga5bb2cfcf3ab60423048db38103657197a0cfcabb4325e4b59213002aaeda75524) = 4,

425

427

[ 429](group__usb__type__c.md#gga5bb2cfcf3ab60423048db38103657197a950c6ff65a4af5db2f1fdab3383489ba) [TC\_CC\_DFP\_ATTACHED](group__usb__type__c.md#gga5bb2cfcf3ab60423048db38103657197a950c6ff65a4af5db2f1fdab3383489ba) = 5,

[ 431](group__usb__type__c.md#gga5bb2cfcf3ab60423048db38103657197a8821754209b4cd977b2c97d43957166c) [TC\_CC\_DFP\_DEBUG\_ACC](group__usb__type__c.md#gga5bb2cfcf3ab60423048db38103657197a8821754209b4cd977b2c97d43957166c) = 6

432};

433

437

438#ifdef \_\_cplusplus

439}

440#endif

441

442#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_USBC\_USBC\_TC\_H\_ \*/

[tc\_vbus\_level](group__usb__type__c.md#ga015455a6c5620dfc96cfb713bbb72161)

tc\_vbus\_level

VBUS level voltages.

**Definition** usbc\_tc.h:326

[tc\_cc\_pull](group__usb__type__c.md#ga0200c820510eb786f3ca30a9b5f7aada)

tc\_cc\_pull

CC pull resistors.

**Definition** usbc\_tc.h:352

[tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5)

tc\_rp\_value

Pull-Up resistor values.

**Definition** usbc\_tc.h:338

[tc\_cc\_states](group__usb__type__c.md#ga5bb2cfcf3ab60423048db38103657197)

tc\_cc\_states

Possible port partner connections based on CC line states.

**Definition** usbc\_tc.h:411

[tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c)

tc\_cc\_voltage\_state

CC Voltage status.

**Definition** usbc\_tc.h:308

[tc\_data\_role](group__usb__type__c.md#ga6b98bbe238e62cfd5531688494a63de2)

tc\_data\_role

Power Delivery Data Role.

**Definition** usbc\_tc.h:389

[tc\_cable\_plug](group__usb__type__c.md#ga8707ac194510396d55a40887673b53ca)

tc\_cable\_plug

Cable plug.

**Definition** usbc\_tc.h:369

[tc\_power\_role](group__usb__type__c.md#gaa6dda0612045b5f55b9d8ba63d2b9f9d)

tc\_power\_role

Power Delivery Power Role.

**Definition** usbc\_tc.h:379

[tc\_cc\_polarity](group__usb__type__c.md#gac5b4b58840c9b076a869a5816ba100db)

tc\_cc\_polarity

Polarity of the CC lines.

**Definition** usbc\_tc.h:401

[TC\_VBUS\_PRESENT](group__usb__type__c.md#gga015455a6c5620dfc96cfb713bbb72161a33f8f0dac47bfaffe331553cd42495f5)

@ TC\_VBUS\_PRESENT

VBUS is at least vSafe5V min.

**Definition** usbc\_tc.h:330

[TC\_VBUS\_REMOVED](group__usb__type__c.md#gga015455a6c5620dfc96cfb713bbb72161a84aaa14f5d6dd4b1bf52564af73f24bc)

@ TC\_VBUS\_REMOVED

VBUS is less than vSinkDisconnect max.

**Definition** usbc\_tc.h:332

[TC\_VBUS\_SAFE0V](group__usb__type__c.md#gga015455a6c5620dfc96cfb713bbb72161a86bf4c0568d7a7ec89180e8e36c91827)

@ TC\_VBUS\_SAFE0V

VBUS is less than vSafe0V max.

**Definition** usbc\_tc.h:328

[TC\_CC\_OPEN](group__usb__type__c.md#gga0200c820510eb786f3ca30a9b5f7aadaa4859548c59439c79e3ad080e1fa07fa8)

@ TC\_CC\_OPEN

No CC resistor.

**Definition** usbc\_tc.h:360

[TC\_CC\_RD](group__usb__type__c.md#gga0200c820510eb786f3ca30a9b5f7aadaa60a4e008afce1c9395a0fb6d34767c6e)

@ TC\_CC\_RD

Rd Pull-Down resistor.

**Definition** usbc\_tc.h:358

[TC\_CC\_RP](group__usb__type__c.md#gga0200c820510eb786f3ca30a9b5f7aadaa7a0a6a716cb42af3a572f43bedc2a322)

@ TC\_CC\_RP

Rp Pull-Up resistor.

**Definition** usbc\_tc.h:356

[TC\_RA\_RD](group__usb__type__c.md#gga0200c820510eb786f3ca30a9b5f7aadaa95c81809d680f28281e9dcaef4fff35e)

@ TC\_RA\_RD

Ra and Rd Pull-Down resistor.

**Definition** usbc\_tc.h:362

[TC\_CC\_RA](group__usb__type__c.md#gga0200c820510eb786f3ca30a9b5f7aadaaf52a9f9d10c81fca5b048ad2230cf1e8)

@ TC\_CC\_RA

Ra Pull-Down resistor.

**Definition** usbc\_tc.h:354

[TC\_RP\_1A5](group__usb__type__c.md#gga4e0eec97f7c5c97b87eff9561deea2d5a1c74df7e2b6bbe75d8c61ca4a7202a28)

@ TC\_RP\_1A5

Pull-Up resistor for a current of 1.5A.

**Definition** usbc\_tc.h:342

[TC\_RP\_RESERVED](group__usb__type__c.md#gga4e0eec97f7c5c97b87eff9561deea2d5a215508ac427e2cc53478e5f096a400d1)

@ TC\_RP\_RESERVED

No Pull-Up resistor is applied.

**Definition** usbc\_tc.h:346

[TC\_RP\_USB](group__usb__type__c.md#gga4e0eec97f7c5c97b87eff9561deea2d5a22d5e50479ca672f0469af9006b4f4bb)

@ TC\_RP\_USB

Pull-Up resistor for a current of 900mA.

**Definition** usbc\_tc.h:340

[TC\_RP\_3A0](group__usb__type__c.md#gga4e0eec97f7c5c97b87eff9561deea2d5afa7eda9742f3670a90736a52620cfe3c)

@ TC\_RP\_3A0

Pull-Up resistor for a current of 3.0A.

**Definition** usbc\_tc.h:344

[TC\_CC\_UFP\_ATTACHED](group__usb__type__c.md#gga5bb2cfcf3ab60423048db38103657197a0cfcabb4325e4b59213002aaeda75524)

@ TC\_CC\_UFP\_ATTACHED

Plain UFP attached.

**Definition** usbc\_tc.h:424

[TC\_CC\_NONE](group__usb__type__c.md#gga5bb2cfcf3ab60423048db38103657197a21cf3890c4a2fa6ee9f137f2b22e51f0)

@ TC\_CC\_NONE

No port partner attached.

**Definition** usbc\_tc.h:413

[TC\_CC\_UFP\_AUDIO\_ACC](group__usb__type__c.md#gga5bb2cfcf3ab60423048db38103657197a4b841a1438a120652ab78fb3ae2c7dea)

@ TC\_CC\_UFP\_AUDIO\_ACC

UFP Audio accessory connected.

**Definition** usbc\_tc.h:420

[TC\_CC\_DFP\_DEBUG\_ACC](group__usb__type__c.md#gga5bb2cfcf3ab60423048db38103657197a8821754209b4cd977b2c97d43957166c)

@ TC\_CC\_DFP\_DEBUG\_ACC

DFP debug accessory connected.

**Definition** usbc\_tc.h:431

[TC\_CC\_UFP\_NONE](group__usb__type__c.md#gga5bb2cfcf3ab60423048db38103657197a90544a6af90af7722cec8ffe83f752f0)

@ TC\_CC\_UFP\_NONE

From DFP perspective.

**Definition** usbc\_tc.h:418

[TC\_CC\_DFP\_ATTACHED](group__usb__type__c.md#gga5bb2cfcf3ab60423048db38103657197a950c6ff65a4af5db2f1fdab3383489ba)

@ TC\_CC\_DFP\_ATTACHED

From UFP perspective.

**Definition** usbc\_tc.h:429

[TC\_CC\_UFP\_DEBUG\_ACC](group__usb__type__c.md#gga5bb2cfcf3ab60423048db38103657197aaba130e5d3d999794eb87e2b8a09cf78)

@ TC\_CC\_UFP\_DEBUG\_ACC

UFP Debug accessory connected.

**Definition** usbc\_tc.h:422

[TC\_CC\_VOLT\_RP\_DEF](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca06bd58eb73aa7f097046e7b88fde0293)

@ TC\_CC\_VOLT\_RP\_DEF

Port partner is applying Rp (0.5A).

**Definition** usbc\_tc.h:316

[TC\_CC\_VOLT\_RA](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca17a8d72f4dc6b29e1d4ad35a4f1531ea)

@ TC\_CC\_VOLT\_RA

Port partner is applying Ra.

**Definition** usbc\_tc.h:312

[TC\_CC\_VOLT\_OPEN](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca1f4b82ea64d23167df5083fd7550cf05)

@ TC\_CC\_VOLT\_OPEN

No port partner connection.

**Definition** usbc\_tc.h:310

[TC\_CC\_VOLT\_RD](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca2267bbcda871c265e77228a5fe6342a9)

@ TC\_CC\_VOLT\_RD

Port partner is applying Rd.

**Definition** usbc\_tc.h:314

[TC\_CC\_VOLT\_RP\_3A0](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca3965e449dbcc8ca6e87d72cd5a73f0ca)

@ TC\_CC\_VOLT\_RP\_3A0

Port partner is applying Rp (3.0A).

**Definition** usbc\_tc.h:320

[TC\_CC\_VOLT\_RP\_1A5](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca3cc0d3c1ac9775b1b8ba77b87868bc72)

@ TC\_CC\_VOLT\_RP\_1A5

**Definition** usbc\_tc.h:318

[TC\_ROLE\_DISCONNECTED](group__usb__type__c.md#gga6b98bbe238e62cfd5531688494a63de2a155c3d22f151d83899f46e516e88a058)

@ TC\_ROLE\_DISCONNECTED

Port is disconnected.

**Definition** usbc\_tc.h:395

[TC\_ROLE\_DFP](group__usb__type__c.md#gga6b98bbe238e62cfd5531688494a63de2a812112dccb0c3d8dd555d351a7f5b9e1)

@ TC\_ROLE\_DFP

Data role is a Downstream Facing Port.

**Definition** usbc\_tc.h:393

[TC\_ROLE\_UFP](group__usb__type__c.md#gga6b98bbe238e62cfd5531688494a63de2a9472c4319bf0be6937436e1602c7b414)

@ TC\_ROLE\_UFP

Data role is an Upstream Facing Port.

**Definition** usbc\_tc.h:391

[PD\_PLUG\_FROM\_CABLE\_VPD](group__usb__type__c.md#gga8707ac194510396d55a40887673b53caa49960a4dee1da0c7330cce2b13c4c0ed)

@ PD\_PLUG\_FROM\_CABLE\_VPD

**Definition** usbc\_tc.h:373

[PD\_PLUG\_FROM\_DFP\_UFP](group__usb__type__c.md#gga8707ac194510396d55a40887673b53caad1092c45d3fad497dbafe15fd9f1c3b3)

@ PD\_PLUG\_FROM\_DFP\_UFP

**Definition** usbc\_tc.h:371

[TC\_ROLE\_SINK](group__usb__type__c.md#ggaa6dda0612045b5f55b9d8ba63d2b9f9da0023468cf2e977c8372899e6f1a0aafb)

@ TC\_ROLE\_SINK

Power role is a sink.

**Definition** usbc\_tc.h:381

[TC\_ROLE\_SOURCE](group__usb__type__c.md#ggaa6dda0612045b5f55b9d8ba63d2b9f9da1b8caf27ae76de5ea874b0e52adc4cf1)

@ TC\_ROLE\_SOURCE

Power role is a source.

**Definition** usbc\_tc.h:383

[TC\_POLARITY\_CC1](group__usb__type__c.md#ggac5b4b58840c9b076a869a5816ba100dba1ace08cbeb63866305ccfb0c3bf338c2)

@ TC\_POLARITY\_CC1

Use CC1 IO for Power Delivery communication.

**Definition** usbc\_tc.h:403

[TC\_POLARITY\_CC2](group__usb__type__c.md#ggac5b4b58840c9b076a869a5816ba100dbae3ad03c80e84e32f8974a14e815ed910)

@ TC\_POLARITY\_CC2

Use CC2 IO for Power Delivery communication.

**Definition** usbc\_tc.h:405

[types.h](include_2zephyr_2types_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [usb\_c](dir_a57818ecbbcbfd5f3cb9a612ed0259e0.md)
- [usbc\_tc.h](usbc__tc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

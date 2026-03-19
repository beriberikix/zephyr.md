---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/usb__device_8h_source.html
original_path: doxygen/html/usb__device_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_device.h

[Go to the documentation of this file.](usb__device_8h.md)

1/\* SPDX-License-Identifier: BSD-3-Clause \*/

2

3/\*

4 \* LPCUSB, an USB device driver for LPC microcontrollers

5 \* Copyright (C) 2006 Bertrik Sikken (bertrik@sikken.nl)

6 \* Copyright (c) 2016 Intel Corporation

7 \*

8 \* Redistribution and use in source and binary forms, with or without

9 \* modification, are permitted provided that the following conditions are met:

10 \*

11 \* 1. Redistributions of source code must retain the above copyright

12 \* notice, this list of conditions and the following disclaimer.

13 \* 2. Redistributions in binary form must reproduce the above copyright

14 \* notice, this list of conditions and the following disclaimer in the

15 \* documentation and/or other materials provided with the distribution.

16 \* 3. The name of the author may not be used to endorse or promote products

17 \* derived from this software without specific prior written permission.

18 \*

19 \* THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR

20 \* IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES

21 \* OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.

22 \* IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,

23 \* INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT

24 \* NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,

25 \* DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY

26 \* THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT

27 \* (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF

28 \* THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

29 \*/

30

37

38#ifndef ZEPHYR\_INCLUDE\_USB\_USB\_DEVICE\_H\_

39#define ZEPHYR\_INCLUDE\_USB\_USB\_DEVICE\_H\_

40

41#include <[zephyr/drivers/usb/usb\_dc.h](usb__dc_8h.md)>

42#include <[zephyr/usb/usb\_ch9.h](usb__ch9_8h.md)>

43#include <[zephyr/logging/log.h](log_8h.md)>

44#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

45

46#ifdef \_\_cplusplus

47extern "C" {

48#endif

49

50/\*

51 \* These macros should be used to place the USB descriptors

52 \* in predetermined order in the RAM.

53 \*/

[ 54](usb__device_8h.md#a95efe03ee4bbfa4d9b0c3932b8ddfe31)#define USBD\_DEVICE\_DESCR\_DEFINE(p) \

55 static \_\_in\_section(usb, descriptor\_##p, 0) \_\_used \_\_aligned(1)

[ 56](usb__device_8h.md#a9403c2bd43e638b4d5634288dfb6574b)#define USBD\_CLASS\_DESCR\_DEFINE(p, instance) \

57 static \_\_in\_section(usb, descriptor\_##p.1, instance) \_\_used \_\_aligned(1)

[ 58](usb__device_8h.md#a6ff803fe6831ca99e3e9543dd1d2f37d)#define USBD\_MISC\_DESCR\_DEFINE(p) \

59 static \_\_in\_section(usb, descriptor\_##p, 2) \_\_used \_\_aligned(1)

[ 60](usb__device_8h.md#a76a98dcc6ca0284195d61bb928197e38)#define USBD\_USER\_DESCR\_DEFINE(p) \

61 static \_\_in\_section(usb, descriptor\_##p, 3) \_\_used \_\_aligned(1)

[ 62](usb__device_8h.md#acb8451e935bab6c8fe2f7eea97a8ae6f)#define USBD\_STRING\_DESCR\_DEFINE(p) \

63 static \_\_in\_section(usb, descriptor\_##p, 4) \_\_used \_\_aligned(1)

[ 64](usb__device_8h.md#a5bc3e0d5484c0c54e5996d99ebedc51b)#define USBD\_STRING\_DESCR\_USER\_DEFINE(p) \

65 static \_\_in\_section(usb, descriptor\_##p, 5) \_\_used \_\_aligned(1)

[ 66](usb__device_8h.md#a2ad0dd7628d3038c32809e6850baf23f)#define USBD\_TERM\_DESCR\_DEFINE(p) \

67 static \_\_in\_section(usb, descriptor\_##p, 6) \_\_used \_\_aligned(1)

68

69/\*

70 \* This macro should be used to place the struct usb\_cfg\_data

71 \* inside usb data section in the RAM.

72 \*/

[ 73](usb__device_8h.md#a5db8e2eb30dd2afc51dbb9e08fbc07c6)#define USBD\_DEFINE\_CFG\_DATA(name) \

74 static STRUCT\_SECTION\_ITERABLE(usb\_cfg\_data, name)

75

76/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

77 \* USB configuration

78 \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

79

[ 80](usb__device_8h.md#a3d01cf3cbbd08db3d6cfcfb45062b961)#define USB\_MAX\_CTRL\_MPS 64

[ 81](usb__device_8h.md#a07bbd07466b47a0c498f26e25932392f)#define USB\_MAX\_FS\_BULK\_MPS 64

[ 82](usb__device_8h.md#ae88dc2d0b2a21779d8c353cd63ae3455)#define USB\_MAX\_FS\_INT\_MPS 64

[ 83](usb__device_8h.md#ae45dfb00deef73b2a142576bf136b062)#define USB\_MAX\_FS\_ISO\_MPS 1023

84

85/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

86 \* USB application interface

87 \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

88

96

[ 100](group____usb__device__core__api.md#ga9a45db26a9be295640ed122533427725)typedef void (\*[usb\_ep\_callback](group____usb__device__core__api.md#ga9a45db26a9be295640ed122533427725))([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep,

101 enum [usb\_dc\_ep\_cb\_status\_code](group____usb__device__controller__api.md#gaf7f083f61e1406e7d41513113dccd3bd) cb\_status);

102

[ 114](group____usb__device__core__api.md#gaddacbff094a41c885c3041af72fa6804)typedef int (\*[usb\_request\_handler](group____usb__device__core__api.md#gaddacbff094a41c885c3041af72fa6804))(struct [usb\_setup\_packet](structusb__setup__packet.md) \*setup,

115 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*transfer\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*payload\_data);

116

[ 120](group____usb__device__core__api.md#ga3439af9464471b3acdc21f4359efb53a)typedef void (\*[usb\_interface\_config](group____usb__device__core__api.md#ga3439af9464471b3acdc21f4359efb53a))(struct [usb\_desc\_header](structusb__desc__header.md) \*head,

121 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bInterfaceNumber);

122

[ 128](structusb__ep__cfg__data.md)struct [usb\_ep\_cfg\_data](structusb__ep__cfg__data.md) {

[ 134](structusb__ep__cfg__data.md#a5d03244508b6a58d9d0bfb896c2537d1) [usb\_ep\_callback](group____usb__device__core__api.md#ga9a45db26a9be295640ed122533427725) [ep\_cb](structusb__ep__cfg__data.md#a5d03244508b6a58d9d0bfb896c2537d1);

[ 141](structusb__ep__cfg__data.md#aa87f676a577a8c1605bb9a8fa04f411c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ep\_addr](structusb__ep__cfg__data.md#aa87f676a577a8c1605bb9a8fa04f411c);

142};

143

[ 149](structusb__interface__cfg__data.md)struct [usb\_interface\_cfg\_data](structusb__interface__cfg__data.md) {

[ 151](structusb__interface__cfg__data.md#a144ed5ba67d1adb8dbb1d936ac440272) [usb\_request\_handler](group____usb__device__core__api.md#gaddacbff094a41c885c3041af72fa6804) [class\_handler](structusb__interface__cfg__data.md#a144ed5ba67d1adb8dbb1d936ac440272);

[ 153](structusb__interface__cfg__data.md#a2d5d65d41cef609173287161797318d2) [usb\_request\_handler](group____usb__device__core__api.md#gaddacbff094a41c885c3041af72fa6804) [vendor\_handler](structusb__interface__cfg__data.md#a2d5d65d41cef609173287161797318d2);

[ 163](structusb__interface__cfg__data.md#a117a1a88c02048ee43994d3e5a4ce922) [usb\_request\_handler](group____usb__device__core__api.md#gaddacbff094a41c885c3041af72fa6804) [custom\_handler](structusb__interface__cfg__data.md#a117a1a88c02048ee43994d3e5a4ce922);

164};

165

[ 174](structusb__cfg__data.md)struct [usb\_cfg\_data](structusb__cfg__data.md) {

[ 179](structusb__cfg__data.md#a842d4d8a08dd619dd8ee5ccf62ae1e2a) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[usb\_device\_description](structusb__cfg__data.md#a842d4d8a08dd619dd8ee5ccf62ae1e2a);

[ 181](structusb__cfg__data.md#ade7cc5e164a82a86d7c57d7a2a4ef306) void \*[interface\_descriptor](structusb__cfg__data.md#ade7cc5e164a82a86d7c57d7a2a4ef306);

[ 183](structusb__cfg__data.md#a3ea73c7ea8759d3637852ff2d02ee96b) [usb\_interface\_config](group____usb__device__core__api.md#ga3439af9464471b3acdc21f4359efb53a) [interface\_config](structusb__cfg__data.md#a3ea73c7ea8759d3637852ff2d02ee96b);

[ 185](structusb__cfg__data.md#aaf33be8983eb59105beb2d6e551ff195) void (\*[cb\_usb\_status](structusb__cfg__data.md#aaf33be8983eb59105beb2d6e551ff195))(struct [usb\_cfg\_data](structusb__cfg__data.md) \*cfg,

186 enum [usb\_dc\_status\_code](group____usb__device__controller__api.md#gac09e3e0af1a2b41a5bfbad91f900baf7) cb\_status,

187 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*param);

[ 189](structusb__cfg__data.md#a84b41f3ddabab946ed165c03e3812e10) struct [usb\_interface\_cfg\_data](structusb__interface__cfg__data.md) [interface](structusb__cfg__data.md#a84b41f3ddabab946ed165c03e3812e10);

[ 191](structusb__cfg__data.md#a5e58af56af22ecdf0e2222afc408a33b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_endpoints](structusb__cfg__data.md#a5e58af56af22ecdf0e2222afc408a33b);

[ 197](structusb__cfg__data.md#adbd7a747db040b54d047c48bed2f50c3) struct [usb\_ep\_cfg\_data](structusb__ep__cfg__data.md) \*[endpoint](structusb__cfg__data.md#adbd7a747db040b54d047c48bed2f50c3);

198};

199

[ 210](group____usb__device__core__api.md#ga28783e727e35db1a651309a7f9f5444a)int [usb\_set\_config](group____usb__device__core__api.md#ga28783e727e35db1a651309a7f9f5444a)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*usb\_descriptor);

211

[ 219](group____usb__device__core__api.md#ga2d485c77055dd975f3170fbaea7f2bdf)int [usb\_deconfig](group____usb__device__core__api.md#ga2d485c77055dd975f3170fbaea7f2bdf)(void);

220

[ 237](group____usb__device__core__api.md#gad1fa5e491d93c2bd1fe7967c12148902)int [usb\_enable](group____usb__device__core__api.md#gad1fa5e491d93c2bd1fe7967c12148902)([usb\_dc\_status\_callback](group____usb__device__controller__api.md#ga2ddb0b059b4e1e76473ed7f56d0cf2ee) status\_cb);

238

[ 248](group____usb__device__core__api.md#ga65723c9469a12c87e5554169396f8e76)int [usb\_disable](group____usb__device__core__api.md#ga65723c9469a12c87e5554169396f8e76)(void);

249

[ 266](group____usb__device__core__api.md#ga6d4b568f2f3aac4f099c35393fb601b3)int [usb\_write](group____usb__device__core__api.md#ga6d4b568f2f3aac4f099c35393fb601b3)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*bytes\_ret);

267

[ 285](group____usb__device__core__api.md#gab2c21738baa839b483654d1d5baf2981)int [usb\_read](group____usb__device__core__api.md#gab2c21738baa839b483654d1d5baf2981)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_data\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*ret\_bytes);

286

[ 298](group____usb__device__core__api.md#gaaf206afaf32bde1b8d77d04bc6ec091f)int [usb\_ep\_set\_stall](group____usb__device__core__api.md#gaaf206afaf32bde1b8d77d04bc6ec091f)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

299

[ 311](group____usb__device__core__api.md#gae7bc410d0db8a6d2142992153bb1424d)int [usb\_ep\_clear\_stall](group____usb__device__core__api.md#gae7bc410d0db8a6d2142992153bb1424d)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

312

[ 331](group____usb__device__core__api.md#ga4c919f7e993f80150bdde2d7fab254ee)int [usb\_ep\_read\_wait](group____usb__device__core__api.md#ga4c919f7e993f80150bdde2d7fab254ee)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_data\_len,

332 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*read\_bytes);

333

334

[ 348](group____usb__device__core__api.md#gaab17b8c523ac211ff308c8dc774ba092)int [usb\_ep\_read\_continue](group____usb__device__core__api.md#gaab17b8c523ac211ff308c8dc774ba092)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

349

[ 353](group____usb__device__core__api.md#ga2e599eb20f647d9bb2369d76a7dc51db)typedef void (\*[usb\_transfer\_callback](group____usb__device__core__api.md#ga2e599eb20f647d9bb2369d76a7dc51db))([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, int tsize, void \*priv);

354

355/\* USB transfer flags \*/

[ 356](group____usb__device__core__api.md#gabb531b022f5d2d859227a7b35d593d80)#define USB\_TRANS\_READ BIT(0)

[ 357](group____usb__device__core__api.md#ga163ee39a47b0a3d9fe3697cc4f24e787)#define USB\_TRANS\_WRITE BIT(1)

[ 358](group____usb__device__core__api.md#ga81c618544f27e0dc0e556021b0418c40)#define USB\_TRANS\_NO\_ZLP BIT(2)

359

[ 366](group____usb__device__core__api.md#ga3485c3d1c3fa7259de32fd57d303bc77)void [usb\_transfer\_ep\_callback](group____usb__device__core__api.md#ga3485c3d1c3fa7259de32fd57d303bc77)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, enum [usb\_dc\_ep\_cb\_status\_code](group____usb__device__controller__api.md#gaf7f083f61e1406e7d41513113dccd3bd));

367

[ 385](group____usb__device__core__api.md#ga27c3040dca474b5b45e6bea63a500cce)int [usb\_transfer](group____usb__device__core__api.md#ga27c3040dca474b5b45e6bea63a500cce)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t dlen, unsigned int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

386 [usb\_transfer\_callback](group____usb__device__core__api.md#ga2e599eb20f647d9bb2369d76a7dc51db) cb, void \*priv);

387

[ 404](group____usb__device__core__api.md#ga1060e3a473a7f0bc71763a413e91ab56)int [usb\_transfer\_sync](group____usb__device__core__api.md#ga1060e3a473a7f0bc71763a413e91ab56)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t dlen, unsigned int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

405

[ 412](group____usb__device__core__api.md#gab399dc4a43a99c927ee7588a57c49211)void [usb\_cancel\_transfer](group____usb__device__core__api.md#gab399dc4a43a99c927ee7588a57c49211)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

413

[ 417](group____usb__device__core__api.md#ga758a63b22c48d2ae9d025adb92ed5925)void [usb\_cancel\_transfers](group____usb__device__core__api.md#ga758a63b22c48d2ae9d025adb92ed5925)(void);

418

[ 427](group____usb__device__core__api.md#ga6292a473cffc1f8683da902c2a85d653)bool [usb\_transfer\_is\_busy](group____usb__device__core__api.md#ga6292a473cffc1f8683da902c2a85d653)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

428

[ 439](group____usb__device__core__api.md#ga7d67c8d49b52fb33818d654ca647c1e5)int [usb\_wakeup\_request](group____usb__device__core__api.md#ga7d67c8d49b52fb33818d654ca647c1e5)(void);

440

[ 446](group____usb__device__core__api.md#ga577018c415eec38ef5038cdb2f45ed2f)bool [usb\_get\_remote\_wakeup\_status](group____usb__device__core__api.md#ga577018c415eec38ef5038cdb2f45ed2f)(void);

447

[ 452](group____usb__device__core__api.md#ga40975f1b023ea36118137e86e099e649)#define USB\_DEVICE\_BOS\_DESC\_DEFINE\_CAP \

453 static \_\_in\_section(usb, bos\_desc\_area, 1) \_\_aligned(1) \_\_used

454

[ 463](group____usb__device__core__api.md#ga1bf8ec88cf752e98234d9f8bb57f976a)void [usb\_bos\_register\_cap](group____usb__device__core__api.md#ga1bf8ec88cf752e98234d9f8bb57f976a)(void \*hdr);

464

468

469#ifdef \_\_cplusplus

470}

471#endif

472

473#endif /\* ZEPHYR\_INCLUDE\_USB\_USB\_DEVICE\_H\_ \*/

[usb\_dc\_status\_callback](group____usb__device__controller__api.md#ga2ddb0b059b4e1e76473ed7f56d0cf2ee)

void(\* usb\_dc\_status\_callback)(enum usb\_dc\_status\_code cb\_status, const uint8\_t \*param)

Callback function signature for the device.

**Definition** usb\_dc.h:135

[usb\_dc\_status\_code](group____usb__device__controller__api.md#gac09e3e0af1a2b41a5bfbad91f900baf7)

usb\_dc\_status\_code

USB Driver Status Codes.

**Definition** usb\_dc.h:35

[usb\_dc\_ep\_cb\_status\_code](group____usb__device__controller__api.md#gaf7f083f61e1406e7d41513113dccd3bd)

usb\_dc\_ep\_cb\_status\_code

USB Endpoint Callback Status Codes.

**Definition** usb\_dc.h:67

[usb\_transfer\_sync](group____usb__device__core__api.md#ga1060e3a473a7f0bc71763a413e91ab56)

int usb\_transfer\_sync(uint8\_t ep, uint8\_t \*data, size\_t dlen, unsigned int flags)

Start a transfer and block-wait for completion.

[usb\_bos\_register\_cap](group____usb__device__core__api.md#ga1bf8ec88cf752e98234d9f8bb57f976a)

void usb\_bos\_register\_cap(void \*hdr)

Register BOS capability descriptor.

[usb\_transfer](group____usb__device__core__api.md#ga27c3040dca474b5b45e6bea63a500cce)

int usb\_transfer(uint8\_t ep, uint8\_t \*data, size\_t dlen, unsigned int flags, usb\_transfer\_callback cb, void \*priv)

Start a transfer.

[usb\_set\_config](group____usb__device__core__api.md#ga28783e727e35db1a651309a7f9f5444a)

int usb\_set\_config(const uint8\_t \*usb\_descriptor)

Configure USB controller.

[usb\_deconfig](group____usb__device__core__api.md#ga2d485c77055dd975f3170fbaea7f2bdf)

int usb\_deconfig(void)

Deconfigure USB controller.

[usb\_transfer\_callback](group____usb__device__core__api.md#ga2e599eb20f647d9bb2369d76a7dc51db)

void(\* usb\_transfer\_callback)(uint8\_t ep, int tsize, void \*priv)

Callback function signature for transfer completion.

**Definition** usb\_device.h:353

[usb\_interface\_config](group____usb__device__core__api.md#ga3439af9464471b3acdc21f4359efb53a)

void(\* usb\_interface\_config)(struct usb\_desc\_header \*head, uint8\_t bInterfaceNumber)

Function for interface runtime configuration.

**Definition** usb\_device.h:120

[usb\_transfer\_ep\_callback](group____usb__device__core__api.md#ga3485c3d1c3fa7259de32fd57d303bc77)

void usb\_transfer\_ep\_callback(uint8\_t ep, enum usb\_dc\_ep\_cb\_status\_code)

Transfer management endpoint callback.

[usb\_ep\_read\_wait](group____usb__device__core__api.md#ga4c919f7e993f80150bdde2d7fab254ee)

int usb\_ep\_read\_wait(uint8\_t ep, uint8\_t \*data, uint32\_t max\_data\_len, uint32\_t \*read\_bytes)

Read data from the specified endpoint.

[usb\_get\_remote\_wakeup\_status](group____usb__device__core__api.md#ga577018c415eec38ef5038cdb2f45ed2f)

bool usb\_get\_remote\_wakeup\_status(void)

Get status of the USB remote wakeup feature.

[usb\_transfer\_is\_busy](group____usb__device__core__api.md#ga6292a473cffc1f8683da902c2a85d653)

bool usb\_transfer\_is\_busy(uint8\_t ep)

Check that transfer is ongoing for the endpoint.

[usb\_disable](group____usb__device__core__api.md#ga65723c9469a12c87e5554169396f8e76)

int usb\_disable(void)

Disable the USB device.

[usb\_write](group____usb__device__core__api.md#ga6d4b568f2f3aac4f099c35393fb601b3)

int usb\_write(uint8\_t ep, const uint8\_t \*data, uint32\_t data\_len, uint32\_t \*bytes\_ret)

Write data to the specified endpoint.

[usb\_cancel\_transfers](group____usb__device__core__api.md#ga758a63b22c48d2ae9d025adb92ed5925)

void usb\_cancel\_transfers(void)

Cancel all ongoing transfers.

[usb\_wakeup\_request](group____usb__device__core__api.md#ga7d67c8d49b52fb33818d654ca647c1e5)

int usb\_wakeup\_request(void)

Start the USB remote wakeup procedure.

[usb\_ep\_callback](group____usb__device__core__api.md#ga9a45db26a9be295640ed122533427725)

void(\* usb\_ep\_callback)(uint8\_t ep, enum usb\_dc\_ep\_cb\_status\_code cb\_status)

Callback function signature for the USB Endpoint status.

**Definition** usb\_device.h:100

[usb\_ep\_read\_continue](group____usb__device__core__api.md#gaab17b8c523ac211ff308c8dc774ba092)

int usb\_ep\_read\_continue(uint8\_t ep)

Continue reading data from the endpoint.

[usb\_ep\_set\_stall](group____usb__device__core__api.md#gaaf206afaf32bde1b8d77d04bc6ec091f)

int usb\_ep\_set\_stall(uint8\_t ep)

Set STALL condition on the specified endpoint.

[usb\_read](group____usb__device__core__api.md#gab2c21738baa839b483654d1d5baf2981)

int usb\_read(uint8\_t ep, uint8\_t \*data, uint32\_t max\_data\_len, uint32\_t \*ret\_bytes)

Read data from the specified endpoint.

[usb\_cancel\_transfer](group____usb__device__core__api.md#gab399dc4a43a99c927ee7588a57c49211)

void usb\_cancel\_transfer(uint8\_t ep)

Cancel any ongoing transfer on the specified endpoint.

[usb\_enable](group____usb__device__core__api.md#gad1fa5e491d93c2bd1fe7967c12148902)

int usb\_enable(usb\_dc\_status\_callback status\_cb)

Enable the USB subsystem and associated hardware.

[usb\_request\_handler](group____usb__device__core__api.md#gaddacbff094a41c885c3041af72fa6804)

int(\* usb\_request\_handler)(struct usb\_setup\_packet \*setup, int32\_t \*transfer\_len, uint8\_t \*\*payload\_data)

Callback function signature for class specific requests.

**Definition** usb\_device.h:114

[usb\_ep\_clear\_stall](group____usb__device__core__api.md#gae7bc410d0db8a6d2142992153bb1424d)

int usb\_ep\_clear\_stall(uint8\_t ep)

Clears STALL condition on the specified endpoint.

[log.h](log_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[usb\_cfg\_data](structusb__cfg__data.md)

USB device configuration.

**Definition** usb\_device.h:174

[usb\_cfg\_data::interface\_config](structusb__cfg__data.md#a3ea73c7ea8759d3637852ff2d02ee96b)

usb\_interface\_config interface\_config

Function for interface runtime configuration.

**Definition** usb\_device.h:183

[usb\_cfg\_data::num\_endpoints](structusb__cfg__data.md#a5e58af56af22ecdf0e2222afc408a33b)

uint8\_t num\_endpoints

Number of individual endpoints in the device configuration.

**Definition** usb\_device.h:191

[usb\_cfg\_data::usb\_device\_description](structusb__cfg__data.md#a842d4d8a08dd619dd8ee5ccf62ae1e2a)

const uint8\_t \* usb\_device\_description

USB device description, see http://www.beyondlogic.org/usbnutshell/usb5.shtml#DeviceDescriptors.

**Definition** usb\_device.h:179

[usb\_cfg\_data::interface](structusb__cfg__data.md#a84b41f3ddabab946ed165c03e3812e10)

struct usb\_interface\_cfg\_data interface

USB interface (Class) handler and storage space.

**Definition** usb\_device.h:189

[usb\_cfg\_data::cb\_usb\_status](structusb__cfg__data.md#aaf33be8983eb59105beb2d6e551ff195)

void(\* cb\_usb\_status)(struct usb\_cfg\_data \*cfg, enum usb\_dc\_status\_code cb\_status, const uint8\_t \*param)

Callback to be notified on USB connection status change.

**Definition** usb\_device.h:185

[usb\_cfg\_data::endpoint](structusb__cfg__data.md#adbd7a747db040b54d047c48bed2f50c3)

struct usb\_ep\_cfg\_data \* endpoint

Pointer to an array of endpoint structs of length equal to the number of EP associated with the devic...

**Definition** usb\_device.h:197

[usb\_cfg\_data::interface\_descriptor](structusb__cfg__data.md#ade7cc5e164a82a86d7c57d7a2a4ef306)

void \* interface\_descriptor

Pointer to interface descriptor.

**Definition** usb\_device.h:181

[usb\_desc\_header](structusb__desc__header.md)

Header of an USB descriptor.

**Definition** usb\_ch9.h:144

[usb\_ep\_cfg\_data](structusb__ep__cfg__data.md)

USB Endpoint Configuration.

**Definition** usb\_device.h:128

[usb\_ep\_cfg\_data::ep\_cb](structusb__ep__cfg__data.md#a5d03244508b6a58d9d0bfb896c2537d1)

usb\_ep\_callback ep\_cb

Callback function for notification of data received and available to application or transmit done,...

**Definition** usb\_device.h:134

[usb\_ep\_cfg\_data::ep\_addr](structusb__ep__cfg__data.md#aa87f676a577a8c1605bb9a8fa04f411c)

uint8\_t ep\_addr

The number associated with the EP in the device configuration structure IN EP = 0x80 | <endpoint numb...

**Definition** usb\_device.h:141

[usb\_interface\_cfg\_data](structusb__interface__cfg__data.md)

USB Interface Configuration.

**Definition** usb\_device.h:149

[usb\_interface\_cfg\_data::custom\_handler](structusb__interface__cfg__data.md#a117a1a88c02048ee43994d3e5a4ce922)

usb\_request\_handler custom\_handler

The custom request handler gets a first chance at handling the request before it is handed over to th...

**Definition** usb\_device.h:163

[usb\_interface\_cfg\_data::class\_handler](structusb__interface__cfg__data.md#a144ed5ba67d1adb8dbb1d936ac440272)

usb\_request\_handler class\_handler

Handler for USB Class specific Control (EP 0) communications.

**Definition** usb\_device.h:151

[usb\_interface\_cfg\_data::vendor\_handler](structusb__interface__cfg__data.md#a2d5d65d41cef609173287161797318d2)

usb\_request\_handler vendor\_handler

Handler for USB Vendor specific commands.

**Definition** usb\_device.h:153

[usb\_setup\_packet](structusb__setup__packet.md)

USB Setup Data packet defined in spec.

**Definition** usb\_ch9.h:40

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[usb\_ch9.h](usb__ch9_8h.md)

USB Chapter 9 structures and definitions.

[usb\_dc.h](usb__dc_8h.md)

USB device controller APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [usb\_device.h](usb__device_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

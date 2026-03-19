---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/img__mgmt__callbacks_8h_source.html
original_path: doxygen/html/img__mgmt__callbacks_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

img\_mgmt\_callbacks.h

[Go to the documentation of this file.](img__mgmt__callbacks_8h.md)

1/\*

2 \* Copyright (c) 2022 Laird Connectivity

3 \* Copyright (c) 2022 Nordic Semiconductor ASA

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef H\_MCUMGR\_IMG\_MGMT\_CALLBACKS\_

9#define H\_MCUMGR\_IMG\_MGMT\_CALLBACKS\_

10

11#include <[stdbool.h](stdbool_8h.md)>

12#include <[stdint.h](stdint_8h.md)>

13#include <zcbor\_common.h>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

19/\* Dummy definitions, include zephyr/mgmt/mcumgr/grp/img\_mgmt/img\_mgmt.h for actual definitions \*/

20struct [img\_mgmt\_upload\_action](structimg__mgmt__upload__action.md);

21struct [img\_mgmt\_upload\_req](structimg__mgmt__upload__req.md);

22

29

[ 36](structimg__mgmt__upload__check.md)struct [img\_mgmt\_upload\_check](structimg__mgmt__upload__check.md) {

[ 38](structimg__mgmt__upload__check.md#aea96e650e2701e6064638dd4c384df55) struct [img\_mgmt\_upload\_action](structimg__mgmt__upload__action.md) \*[action](structimg__mgmt__upload__check.md#aea96e650e2701e6064638dd4c384df55);

39

[ 41](structimg__mgmt__upload__check.md#ab8a3e937302b1def309508eace664793) struct [img\_mgmt\_upload\_req](structimg__mgmt__upload__req.md) \*[req](structimg__mgmt__upload__check.md#ab8a3e937302b1def309508eace664793);

42};

43

[ 49](structimg__mgmt__image__confirmed.md)struct [img\_mgmt\_image\_confirmed](structimg__mgmt__image__confirmed.md) {

[ 51](structimg__mgmt__image__confirmed.md#a2cd305cbe1446fd26b97a25cacad0e5c) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [image](structimg__mgmt__image__confirmed.md#a2cd305cbe1446fd26b97a25cacad0e5c);

52};

53

[ 59](structimg__mgmt__state__slot__encode.md)struct [img\_mgmt\_state\_slot\_encode](structimg__mgmt__state__slot__encode.md) {

[ 60](structimg__mgmt__state__slot__encode.md#a9279018722b20380da6e48046787d220) bool \*[ok](structimg__mgmt__state__slot__encode.md#a9279018722b20380da6e48046787d220);

[ 61](structimg__mgmt__state__slot__encode.md#a62157cb9a3288806f4ec11e5c2ef20ac) zcbor\_state\_t \*[zse](structimg__mgmt__state__slot__encode.md#a62157cb9a3288806f4ec11e5c2ef20ac);

[ 62](structimg__mgmt__state__slot__encode.md#ad669d8c2062f90d008f715dee206c687) const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [slot](structimg__mgmt__state__slot__encode.md#ad669d8c2062f90d008f715dee206c687);

[ 63](structimg__mgmt__state__slot__encode.md#aa4bf77897519408786c1ee28029342dd) const char \*[version](structimg__mgmt__state__slot__encode.md#aa4bf77897519408786c1ee28029342dd);

[ 64](structimg__mgmt__state__slot__encode.md#a5c2486f75743eb44133819b5f35d97cb) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[hash](structimg__mgmt__state__slot__encode.md#a5c2486f75743eb44133819b5f35d97cb);

[ 65](structimg__mgmt__state__slot__encode.md#a9e53ce9a8a88b76e035b02cd2289fb07) const int [flags](structimg__mgmt__state__slot__encode.md#a9e53ce9a8a88b76e035b02cd2289fb07);

66};

67

[ 73](structimg__mgmt__slot__info__image.md)struct [img\_mgmt\_slot\_info\_image](structimg__mgmt__slot__info__image.md) {

[ 75](structimg__mgmt__slot__info__image.md#a2456d0f9cc29a5cb56d5e8fb45f149d7) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [image](structimg__mgmt__slot__info__image.md#a2456d0f9cc29a5cb56d5e8fb45f149d7);

76

[ 81](structimg__mgmt__slot__info__image.md#af19f99ee4e86a586177b014c364be94c) zcbor\_state\_t \*[zse](structimg__mgmt__slot__info__image.md#af19f99ee4e86a586177b014c364be94c);

82};

83

[ 89](structimg__mgmt__slot__info__slot.md)struct [img\_mgmt\_slot\_info\_slot](structimg__mgmt__slot__info__slot.md) {

[ 91](structimg__mgmt__slot__info__slot.md#ab809efd89381e763f73a45b5c5e807d7) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [image](structimg__mgmt__slot__info__slot.md#ab809efd89381e763f73a45b5c5e807d7);

92

[ 94](structimg__mgmt__slot__info__slot.md#a4fbfd8fb9135cc3fa2cc65f71ca2199e) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [slot](structimg__mgmt__slot__info__slot.md#a4fbfd8fb9135cc3fa2cc65f71ca2199e);

95

[ 97](structimg__mgmt__slot__info__slot.md#a53ef029264545a7caca289d61e7983a1) const struct [flash\_area](structflash__area.md) \*[fa](structimg__mgmt__slot__info__slot.md#a53ef029264545a7caca289d61e7983a1);

98

[ 103](structimg__mgmt__slot__info__slot.md#a316d66379317f7a13be21cd242cdddda) zcbor\_state\_t \*[zse](structimg__mgmt__slot__info__slot.md#a316d66379317f7a13be21cd242cdddda);

104};

105

109

110#ifdef \_\_cplusplus

111}

112#endif

113

114#endif

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[flash\_area](structflash__area.md)

Flash partition.

**Definition** flash\_map.h:54

[img\_mgmt\_image\_confirmed](structimg__mgmt__image__confirmed.md)

Structure provided in the MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CONFIRMED notification callback: This callback fun...

**Definition** img\_mgmt\_callbacks.h:49

[img\_mgmt\_image\_confirmed::image](structimg__mgmt__image__confirmed.md#a2cd305cbe1446fd26b97a25cacad0e5c)

const uint8\_t image

Image number which has been confirmed.

**Definition** img\_mgmt\_callbacks.h:51

[img\_mgmt\_slot\_info\_image](structimg__mgmt__slot__info__image.md)

Structure provided in the MGMT\_EVT\_OP\_IMG\_MGMT\_SLOT\_INFO\_IMAGE notification callback: This callback f...

**Definition** img\_mgmt\_callbacks.h:73

[img\_mgmt\_slot\_info\_image::image](structimg__mgmt__slot__info__image.md#a2456d0f9cc29a5cb56d5e8fb45f149d7)

const uint8\_t image

The image that is currently being enumerated.

**Definition** img\_mgmt\_callbacks.h:75

[img\_mgmt\_slot\_info\_image::zse](structimg__mgmt__slot__info__image.md#af19f99ee4e86a586177b014c364be94c)

zcbor\_state\_t \* zse

The zcbor encoder which is currently being used to output information, additional fields can be added...

**Definition** img\_mgmt\_callbacks.h:81

[img\_mgmt\_slot\_info\_slot](structimg__mgmt__slot__info__slot.md)

Structure provided in the MGMT\_EVT\_OP\_IMG\_MGMT\_SLOT\_INFO\_SLOT notification callback: This callback fu...

**Definition** img\_mgmt\_callbacks.h:89

[img\_mgmt\_slot\_info\_slot::zse](structimg__mgmt__slot__info__slot.md#a316d66379317f7a13be21cd242cdddda)

zcbor\_state\_t \* zse

The zcbor encoder which is currently being used to output information, additional fields can be added...

**Definition** img\_mgmt\_callbacks.h:103

[img\_mgmt\_slot\_info\_slot::slot](structimg__mgmt__slot__info__slot.md#a4fbfd8fb9135cc3fa2cc65f71ca2199e)

const uint8\_t slot

The slot that is currently being enumerated.

**Definition** img\_mgmt\_callbacks.h:94

[img\_mgmt\_slot\_info\_slot::fa](structimg__mgmt__slot__info__slot.md#a53ef029264545a7caca289d61e7983a1)

const struct flash\_area \* fa

Flash area of the slot that is current being enumerated.

**Definition** img\_mgmt\_callbacks.h:97

[img\_mgmt\_slot\_info\_slot::image](structimg__mgmt__slot__info__slot.md#ab809efd89381e763f73a45b5c5e807d7)

const uint8\_t image

The image that is currently being enumerated.

**Definition** img\_mgmt\_callbacks.h:91

[img\_mgmt\_state\_slot\_encode](structimg__mgmt__state__slot__encode.md)

Structure provided in the MGMT\_EVT\_OP\_IMG\_MGMT\_IMAGE\_SLOT\_STATE notification callback: This callback ...

**Definition** img\_mgmt\_callbacks.h:59

[img\_mgmt\_state\_slot\_encode::hash](structimg__mgmt__state__slot__encode.md#a5c2486f75743eb44133819b5f35d97cb)

const uint8\_t \* hash

**Definition** img\_mgmt\_callbacks.h:64

[img\_mgmt\_state\_slot\_encode::zse](structimg__mgmt__state__slot__encode.md#a62157cb9a3288806f4ec11e5c2ef20ac)

zcbor\_state\_t \* zse

**Definition** img\_mgmt\_callbacks.h:61

[img\_mgmt\_state\_slot\_encode::ok](structimg__mgmt__state__slot__encode.md#a9279018722b20380da6e48046787d220)

bool \* ok

**Definition** img\_mgmt\_callbacks.h:60

[img\_mgmt\_state\_slot\_encode::flags](structimg__mgmt__state__slot__encode.md#a9e53ce9a8a88b76e035b02cd2289fb07)

const int flags

**Definition** img\_mgmt\_callbacks.h:65

[img\_mgmt\_state\_slot\_encode::version](structimg__mgmt__state__slot__encode.md#aa4bf77897519408786c1ee28029342dd)

const char \* version

**Definition** img\_mgmt\_callbacks.h:63

[img\_mgmt\_state\_slot\_encode::slot](structimg__mgmt__state__slot__encode.md#ad669d8c2062f90d008f715dee206c687)

const uint32\_t slot

**Definition** img\_mgmt\_callbacks.h:62

[img\_mgmt\_upload\_action](structimg__mgmt__upload__action.md)

Describes what to do during processing of an upload request.

**Definition** img\_mgmt.h:210

[img\_mgmt\_upload\_check](structimg__mgmt__upload__check.md)

Structure provided in the MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CHUNK notification callback: This callback functio...

**Definition** img\_mgmt\_callbacks.h:36

[img\_mgmt\_upload\_check::req](structimg__mgmt__upload__check.md#ab8a3e937302b1def309508eace664793)

struct img\_mgmt\_upload\_req \* req

Upload request information.

**Definition** img\_mgmt\_callbacks.h:41

[img\_mgmt\_upload\_check::action](structimg__mgmt__upload__check.md#aea96e650e2701e6064638dd4c384df55)

struct img\_mgmt\_upload\_action \* action

Action to take.

**Definition** img\_mgmt\_callbacks.h:38

[img\_mgmt\_upload\_req](structimg__mgmt__upload__req.md)

Represents an individual upload request.

**Definition** img\_mgmt.h:187

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [img\_mgmt](dir_731c1b2142dfc9d7fee3a06aa394438e.md)
- [img\_mgmt\_callbacks.h](img__mgmt__callbacks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

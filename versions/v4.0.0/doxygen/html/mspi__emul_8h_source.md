---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mspi__emul_8h_source.html
original_path: doxygen/html/mspi__emul_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mspi\_emul.h

[Go to the documentation of this file.](mspi__emul_8h.md)

[ 1](group__mspi__emul__interface.md#gabecb33236ed3a6a93a28edef0a4c3ae7)/\*

2 \* Copyright 2020 Google LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MSPI\_EMUL\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_MSPI\_EMUL\_H\_

9

10#include <[zephyr/device.h](device_8h.md)>

11#include <[zephyr/drivers/emul.h](drivers_2emul_8h.md)>

12#include <[zephyr/drivers/mspi.h](mspi_8h.md)>

13#include <[zephyr/sys/slist.h](slist_8h.md)>

14#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

15

21

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

33struct [mspi\_emul](structmspi__emul.md);

34

46typedef struct [mspi\_emul](structmspi__emul.md) \*(\*mspi\_emul\_find\_emul)(const struct [device](structdevice.md) \*dev,

47 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dev\_idx);

48

[ 59](group__mspi__emul__interface.md#gaaa0c99ea6582cacba89f8630d8d554be)typedef int (\*[mspi\_emul\_trigger\_event](group__mspi__emul__interface.md#gaaa0c99ea6582cacba89f8630d8d554be))(const struct [device](structdevice.md) \*dev,

60 enum [mspi\_bus\_event](group__mspi__interface.md#ga4cd05950729893e08ef0d4a12e2242d5) evt\_type);

61

[ 75](group__mspi__emul__interface.md#ga15df8cc9ccc2831c5446002e864f1717)typedef int (\*[emul\_mspi\_dev\_api\_transceive](group__mspi__emul__interface.md#ga15df8cc9ccc2831c5446002e864f1717))(const struct [emul](structemul.md) \*target,

76 const struct [mspi\_xfer\_packet](structmspi__xfer__packet.md) \*packets,

77 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_packet,

78 bool async,

79 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeout);

80

[ 82](structemul__mspi__device__api.md)struct [emul\_mspi\_device\_api](structemul__mspi__device__api.md) {

[ 83](structemul__mspi__device__api.md#afb3852793d752722841739fc486c6e4f) [emul\_mspi\_dev\_api\_transceive](group__mspi__emul__interface.md#ga15df8cc9ccc2831c5446002e864f1717) [transceive](structemul__mspi__device__api.md#afb3852793d752722841739fc486c6e4f);

84};

85

[ 87](structmspi__emul.md)struct [mspi\_emul](structmspi__emul.md) {

[ 88](structmspi__emul.md#aa3e45d11717b737ea8c6b4b19459991a) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structmspi__emul.md#aa3e45d11717b737ea8c6b4b19459991a);

[ 90](structmspi__emul.md#aa2b65e70ab7c2218929a6042bd0fd548) const struct [emul](structemul.md) \*[target](structmspi__emul.md#aa2b65e70ab7c2218929a6042bd0fd548);

[ 92](structmspi__emul.md#a2d247195c375c1aac30beec32dc11099) const struct [emul\_mspi\_device\_api](structemul__mspi__device__api.md) \*[api](structmspi__emul.md#a2d247195c375c1aac30beec32dc11099);

[ 94](structmspi__emul.md#a5386510f101d186581abbde6b624be09) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dev\_idx](structmspi__emul.md#a5386510f101d186581abbde6b624be09);

95};

96

[ 98](structemul__mspi__driver__api.md)struct [emul\_mspi\_driver\_api](structemul__mspi__driver__api.md) {

99 /\* The struct mspi\_driver\_api has to be first in

100 \* struct emul\_mspi\_driver\_api to make pointer casting working

101 \*/

[ 102](structemul__mspi__driver__api.md#a2b5aef76272e620fcb77ba9532f0aee6) struct [mspi\_driver\_api](structmspi__driver__api.md) [mspi\_api](structemul__mspi__driver__api.md#a2b5aef76272e620fcb77ba9532f0aee6);

103 /\* The rest, emulator specific functions \*/

[ 104](structemul__mspi__driver__api.md#a7b2ab7da5d949ab05dda7cc0dbc24ff9) [mspi\_emul\_trigger\_event](group__mspi__emul__interface.md#gaaa0c99ea6582cacba89f8630d8d554be) [trigger\_event](structemul__mspi__driver__api.md#a7b2ab7da5d949ab05dda7cc0dbc24ff9);

[ 105](structemul__mspi__driver__api.md#a0fe96769384075e9aee7daa1c30e32a6) [mspi\_emul\_find\_emul](group__mspi__emul__interface.md#gabecb33236ed3a6a93a28edef0a4c3ae7) [find\_emul](structemul__mspi__driver__api.md#a0fe96769384075e9aee7daa1c30e32a6);

106};

107

[ 115](group__mspi__emul__interface.md#ga98c9a359f3385f49fbfe52b27254d261)int [mspi\_emul\_register](group__mspi__emul__interface.md#ga98c9a359f3385f49fbfe52b27254d261)(const struct [device](structdevice.md) \*dev, struct [mspi\_emul](structmspi__emul.md) \*[emul](structemul.md));

116

117#ifdef \_\_cplusplus

118}

119#endif

120

124

125#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MSPI\_EMUL\_H\_ \*/

[device.h](device_8h.md)

[emul.h](drivers_2emul_8h.md)

[emul\_mspi\_dev\_api\_transceive](group__mspi__emul__interface.md#ga15df8cc9ccc2831c5446002e864f1717)

int(\* emul\_mspi\_dev\_api\_transceive)(const struct emul \*target, const struct mspi\_xfer\_packet \*packets, uint32\_t num\_packet, bool async, uint32\_t timeout)

Loopback MSPI transceive request to the device emulator as no real hardware attached.

**Definition** mspi\_emul.h:75

[mspi\_emul\_register](group__mspi__emul__interface.md#ga98c9a359f3385f49fbfe52b27254d261)

int mspi\_emul\_register(const struct device \*dev, struct mspi\_emul \*emul)

Register an emulated device on the controller.

[mspi\_emul\_trigger\_event](group__mspi__emul__interface.md#gaaa0c99ea6582cacba89f8630d8d554be)

int(\* mspi\_emul\_trigger\_event)(const struct device \*dev, enum mspi\_bus\_event evt\_type)

Triggers an event on the emulator of MSPI controller side which causes calling specific callbacks.

**Definition** mspi\_emul.h:59

[mspi\_emul\_find\_emul](group__mspi__emul__interface.md#gabecb33236ed3a6a93a28edef0a4c3ae7)

struct mspi\_emul \*(\* mspi\_emul\_find\_emul)(const struct device \*dev, uint16\_t dev\_idx)

Find an emulator present on a MSPI bus.

**Definition** mspi\_emul.h:46

[mspi\_bus\_event](group__mspi__interface.md#ga4cd05950729893e08ef0d4a12e2242d5)

mspi\_bus\_event

MSPI bus event.

**Definition** mspi.h:123

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[types.h](include_2zephyr_2types_8h.md)

[mspi.h](mspi_8h.md)

Public APIs for MSPI driver.

[slist.h](slist_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[emul\_mspi\_device\_api](structemul__mspi__device__api.md)

Definition of the MSPI device emulator API.

**Definition** mspi\_emul.h:82

[emul\_mspi\_device\_api::transceive](structemul__mspi__device__api.md#afb3852793d752722841739fc486c6e4f)

emul\_mspi\_dev\_api\_transceive transceive

**Definition** mspi\_emul.h:83

[emul\_mspi\_driver\_api](structemul__mspi__driver__api.md)

Definition of the MSPI controller emulator API.

**Definition** mspi\_emul.h:98

[emul\_mspi\_driver\_api::find\_emul](structemul__mspi__driver__api.md#a0fe96769384075e9aee7daa1c30e32a6)

mspi\_emul\_find\_emul find\_emul

**Definition** mspi\_emul.h:105

[emul\_mspi\_driver\_api::mspi\_api](structemul__mspi__driver__api.md#a2b5aef76272e620fcb77ba9532f0aee6)

struct mspi\_driver\_api mspi\_api

**Definition** mspi\_emul.h:102

[emul\_mspi\_driver\_api::trigger\_event](structemul__mspi__driver__api.md#a7b2ab7da5d949ab05dda7cc0dbc24ff9)

mspi\_emul\_trigger\_event trigger\_event

**Definition** mspi\_emul.h:104

[emul](structemul.md)

An emulator instance - represents the target emulated device/peripheral that is interacted with throu...

**Definition** emul.h:82

[mspi\_driver\_api](structmspi__driver__api.md)

**Definition** mspi.h:505

[mspi\_emul](structmspi__emul.md)

Node in a linked list of emulators for MSPI devices.

**Definition** mspi\_emul.h:87

[mspi\_emul::api](structmspi__emul.md#a2d247195c375c1aac30beec32dc11099)

const struct emul\_mspi\_device\_api \* api

API provided for this device.

**Definition** mspi\_emul.h:92

[mspi\_emul::dev\_idx](structmspi__emul.md#a5386510f101d186581abbde6b624be09)

uint16\_t dev\_idx

device index

**Definition** mspi\_emul.h:94

[mspi\_emul::target](structmspi__emul.md#aa2b65e70ab7c2218929a6042bd0fd548)

const struct emul \* target

Target emulator - REQUIRED for all emulated bus nodes of any type.

**Definition** mspi\_emul.h:90

[mspi\_emul::node](structmspi__emul.md#aa3e45d11717b737ea8c6b4b19459991a)

sys\_snode\_t node

**Definition** mspi\_emul.h:88

[mspi\_xfer\_packet](structmspi__xfer__packet.md)

MSPI peripheral xfer packet format.

**Definition** mspi.h:367

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mspi\_emul.h](mspi__emul_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

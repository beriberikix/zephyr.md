---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ibi_8h_source.html
original_path: doxygen/html/ibi_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ibi.h

[Go to the documentation of this file.](ibi_8h.md)

1/\*

2 \* Copyright 2022 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_IBI\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_IBI\_H\_

9

16

17#include <[stdint.h](stdint_8h.md)>

18

19#include <[zephyr/device.h](device_8h.md)>

20#include <[zephyr/kernel.h](kernel_8h.md)>

21#include <[zephyr/sys/slist.h](slist_8h.md)>

22

23#ifndef CONFIG\_I3C\_IBI\_MAX\_PAYLOAD\_SIZE

[ 24](group__i3c__ibi.md#ga7bbbff351dc33d1c00abf6c22bbd50d4)#define CONFIG\_I3C\_IBI\_MAX\_PAYLOAD\_SIZE 0

25#endif

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

31struct [i3c\_device\_desc](structi3c__device__desc.md);

32

[ 36](group__i3c__ibi.md#gaf4be72fc9c862d996d860c0b7fbc862b)enum [i3c\_ibi\_type](group__i3c__ibi.md#gaf4be72fc9c862d996d860c0b7fbc862b) {

[ 38](group__i3c__ibi.md#ggaf4be72fc9c862d996d860c0b7fbc862ba368e8ad08a003ebf197add6d73ffd43d) [I3C\_IBI\_TARGET\_INTR](group__i3c__ibi.md#ggaf4be72fc9c862d996d860c0b7fbc862ba368e8ad08a003ebf197add6d73ffd43d),

39

[ 41](group__i3c__ibi.md#ggaf4be72fc9c862d996d860c0b7fbc862ba00235d326559f945d54638b0c0558815) [I3C\_IBI\_CONTROLLER\_ROLE\_REQUEST](group__i3c__ibi.md#ggaf4be72fc9c862d996d860c0b7fbc862ba00235d326559f945d54638b0c0558815),

42

[ 44](group__i3c__ibi.md#ggaf4be72fc9c862d996d860c0b7fbc862ba493d3b1e9669434c3d62f16aa3d6f92f) [I3C\_IBI\_HOTJOIN](group__i3c__ibi.md#ggaf4be72fc9c862d996d860c0b7fbc862ba493d3b1e9669434c3d62f16aa3d6f92f),

45

[ 46](group__i3c__ibi.md#ggaf4be72fc9c862d996d860c0b7fbc862baab12781f76c743cec6b72ffa7d8c27ee) [I3C\_IBI\_TYPE\_MAX](group__i3c__ibi.md#ggaf4be72fc9c862d996d860c0b7fbc862baab12781f76c743cec6b72ffa7d8c27ee) = [I3C\_IBI\_HOTJOIN](group__i3c__ibi.md#ggaf4be72fc9c862d996d860c0b7fbc862ba493d3b1e9669434c3d62f16aa3d6f92f),

47

[ 52](group__i3c__ibi.md#ggaf4be72fc9c862d996d860c0b7fbc862ba39d8f6a9b69d092eabf9ca9726deec8c) [I3C\_IBI\_WORKQUEUE\_CB](group__i3c__ibi.md#ggaf4be72fc9c862d996d860c0b7fbc862ba39d8f6a9b69d092eabf9ca9726deec8c),

53};

54

[ 58](structi3c__ibi.md)struct [i3c\_ibi](structi3c__ibi.md) {

[ 60](structi3c__ibi.md#a88b0ccd636c042ca929412c42a05bc25) enum [i3c\_ibi\_type](group__i3c__ibi.md#gaf4be72fc9c862d996d860c0b7fbc862b) [ibi\_type](structi3c__ibi.md#a88b0ccd636c042ca929412c42a05bc25);

61

[ 63](structi3c__ibi.md#a584e3298059e412d7d3671a451ecc117) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[payload](structi3c__ibi.md#a584e3298059e412d7d3671a451ecc117);

64

[ 66](structi3c__ibi.md#aa51b8214d4a0708861ac9617f844043f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [payload\_len](structi3c__ibi.md#aa51b8214d4a0708861ac9617f844043f);

67};

68

[ 74](structi3c__ibi__payload.md)struct [i3c\_ibi\_payload](structi3c__ibi__payload.md) {

[ 78](structi3c__ibi__payload.md#aad4208fcdfef0bc9fb67c86ee1d302de) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [payload\_len](structi3c__ibi__payload.md#aad4208fcdfef0bc9fb67c86ee1d302de);

79

[ 83](structi3c__ibi__payload.md#ab869cf38c7a9677fda3ecf48cd358355) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [payload](structi3c__ibi__payload.md#ab869cf38c7a9677fda3ecf48cd358355)[[CONFIG\_I3C\_IBI\_MAX\_PAYLOAD\_SIZE](group__i3c__ibi.md#ga7bbbff351dc33d1c00abf6c22bbd50d4)];

84};

85

[ 89](structi3c__ibi__work.md)struct [i3c\_ibi\_work](structi3c__ibi__work.md) {

[ 90](structi3c__ibi__work.md#a66ece8f194350c94f8991eaf1ee5bc0b) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structi3c__ibi__work.md#a66ece8f194350c94f8991eaf1ee5bc0b);

91

[ 95](structi3c__ibi__work.md#a4a0373423ababe549d00ee13fe657315) struct [k\_work](structk__work.md) [work](structi3c__ibi__work.md#a4a0373423ababe549d00ee13fe657315);

96

[ 100](structi3c__ibi__work.md#a3ec8e089facfbb187342e9bf9a525e50) enum [i3c\_ibi\_type](group__i3c__ibi.md#gaf4be72fc9c862d996d860c0b7fbc862b) [type](structi3c__ibi__work.md#a3ec8e089facfbb187342e9bf9a525e50);

101

102 union {

[ 106](structi3c__ibi__work.md#a195e49bd7db79d0f1f45803e42e963ca) const struct [device](structdevice.md) \*[controller](structi3c__ibi__work.md#a195e49bd7db79d0f1f45803e42e963ca);

107

[ 112](structi3c__ibi__work.md#a6c75e0b678fee04f3357c2c1aa9e7376) struct [i3c\_device\_desc](structi3c__device__desc.md) \*[target](structi3c__ibi__work.md#a6c75e0b678fee04f3357c2c1aa9e7376);

113 };

114

115 union {

[ 119](structi3c__ibi__work.md#a08531106055235eaf85cb8fae690235c) struct [i3c\_ibi\_payload](structi3c__ibi__payload.md) [payload](structi3c__ibi__work.md#a08531106055235eaf85cb8fae690235c);

120

[ 125](structi3c__ibi__work.md#a6a3dfd49762d96b591b5e248f9ce1668) [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) [work\_cb](structi3c__ibi__work.md#a6a3dfd49762d96b591b5e248f9ce1668);

126 };

127};

128

[ 146](group__i3c__ibi.md#ga814cf622b240808216ce4e87802e965c)typedef int (\*[i3c\_target\_ibi\_cb\_t](group__i3c__ibi.md#ga814cf622b240808216ce4e87802e965c))(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

147 struct [i3c\_ibi\_payload](structi3c__ibi__payload.md) \*[payload](structi3c__ibi__payload.md#ab869cf38c7a9677fda3ecf48cd358355));

148

149

[ 167](group__i3c__ibi.md#gaafc2fdf9f2402691c3ebe11d06106840)int [i3c\_ibi\_work\_enqueue](group__i3c__ibi.md#gaafc2fdf9f2402691c3ebe11d06106840)(struct [i3c\_ibi\_work](structi3c__ibi__work.md) \*ibi\_work);

168

[ 184](group__i3c__ibi.md#ga7fbf838ea07516849dc1296d48af65d1)int [i3c\_ibi\_work\_enqueue\_target\_irq](group__i3c__ibi.md#ga7fbf838ea07516849dc1296d48af65d1)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

185 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[payload](structi3c__ibi__payload.md#ab869cf38c7a9677fda3ecf48cd358355), size\_t [payload\_len](structi3c__ibi__payload.md#aad4208fcdfef0bc9fb67c86ee1d302de));

186

[ 200](group__i3c__ibi.md#gad643c7f0512e1e6dcddbe5821e70fc0d)int [i3c\_ibi\_work\_enqueue\_controller\_request](group__i3c__ibi.md#gad643c7f0512e1e6dcddbe5821e70fc0d)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target);

201

[ 215](group__i3c__ibi.md#gab135cb893efd50c7db16c1734b6a0bab)int [i3c\_ibi\_work\_enqueue\_hotjoin](group__i3c__ibi.md#gab135cb893efd50c7db16c1734b6a0bab)(const struct [device](structdevice.md) \*dev);

216

[ 231](group__i3c__ibi.md#ga4c6f4516e55d0ab6c539fb800d7ec45a)int [i3c\_ibi\_work\_enqueue\_cb](group__i3c__ibi.md#ga4c6f4516e55d0ab6c539fb800d7ec45a)(const struct [device](structdevice.md) \*dev,

232 [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) work\_cb);

233

234#ifdef \_\_cplusplus

235}

236#endif

237

241

242#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_IBI\_H\_ \*/

[device.h](device_8h.md)

[i3c\_ibi\_work\_enqueue\_cb](group__i3c__ibi.md#ga4c6f4516e55d0ab6c539fb800d7ec45a)

int i3c\_ibi\_work\_enqueue\_cb(const struct device \*dev, k\_work\_handler\_t work\_cb)

Queue a generic callback for future processing.

[CONFIG\_I3C\_IBI\_MAX\_PAYLOAD\_SIZE](group__i3c__ibi.md#ga7bbbff351dc33d1c00abf6c22bbd50d4)

#define CONFIG\_I3C\_IBI\_MAX\_PAYLOAD\_SIZE

**Definition** ibi.h:24

[i3c\_ibi\_work\_enqueue\_target\_irq](group__i3c__ibi.md#ga7fbf838ea07516849dc1296d48af65d1)

int i3c\_ibi\_work\_enqueue\_target\_irq(struct i3c\_device\_desc \*target, uint8\_t \*payload, size\_t payload\_len)

Queue a target interrupt IBI for future processing.

[i3c\_target\_ibi\_cb\_t](group__i3c__ibi.md#ga814cf622b240808216ce4e87802e965c)

int(\* i3c\_target\_ibi\_cb\_t)(struct i3c\_device\_desc \*target, struct i3c\_ibi\_payload \*payload)

Function called when In-Band Interrupt received from target device.

**Definition** ibi.h:146

[i3c\_ibi\_work\_enqueue](group__i3c__ibi.md#gaafc2fdf9f2402691c3ebe11d06106840)

int i3c\_ibi\_work\_enqueue(struct i3c\_ibi\_work \*ibi\_work)

Queue an IBI work item for future processing.

[i3c\_ibi\_work\_enqueue\_hotjoin](group__i3c__ibi.md#gab135cb893efd50c7db16c1734b6a0bab)

int i3c\_ibi\_work\_enqueue\_hotjoin(const struct device \*dev)

Queue a hot join IBI for future processing.

[i3c\_ibi\_work\_enqueue\_controller\_request](group__i3c__ibi.md#gad643c7f0512e1e6dcddbe5821e70fc0d)

int i3c\_ibi\_work\_enqueue\_controller\_request(struct i3c\_device\_desc \*target)

Queue a controllership request IBI for future processing.

[i3c\_ibi\_type](group__i3c__ibi.md#gaf4be72fc9c862d996d860c0b7fbc862b)

i3c\_ibi\_type

IBI Types.

**Definition** ibi.h:36

[I3C\_IBI\_CONTROLLER\_ROLE\_REQUEST](group__i3c__ibi.md#ggaf4be72fc9c862d996d860c0b7fbc862ba00235d326559f945d54638b0c0558815)

@ I3C\_IBI\_CONTROLLER\_ROLE\_REQUEST

Controller Role Request.

**Definition** ibi.h:41

[I3C\_IBI\_TARGET\_INTR](group__i3c__ibi.md#ggaf4be72fc9c862d996d860c0b7fbc862ba368e8ad08a003ebf197add6d73ffd43d)

@ I3C\_IBI\_TARGET\_INTR

Target interrupt.

**Definition** ibi.h:38

[I3C\_IBI\_WORKQUEUE\_CB](group__i3c__ibi.md#ggaf4be72fc9c862d996d860c0b7fbc862ba39d8f6a9b69d092eabf9ca9726deec8c)

@ I3C\_IBI\_WORKQUEUE\_CB

Not an actual IBI type, but simply used by the IBI workq for generic callbacks.

**Definition** ibi.h:52

[I3C\_IBI\_HOTJOIN](group__i3c__ibi.md#ggaf4be72fc9c862d996d860c0b7fbc862ba493d3b1e9669434c3d62f16aa3d6f92f)

@ I3C\_IBI\_HOTJOIN

Hot Join Request.

**Definition** ibi.h:44

[I3C\_IBI\_TYPE\_MAX](group__i3c__ibi.md#ggaf4be72fc9c862d996d860c0b7fbc862baab12781f76c743cec6b72ffa7d8c27ee)

@ I3C\_IBI\_TYPE\_MAX

**Definition** ibi.h:46

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda)

void(\* k\_work\_handler\_t)(struct k\_work \*work)

The signature for a work item handler function.

**Definition** kernel.h:3387

[kernel.h](kernel_8h.md)

Public kernel APIs.

[slist.h](slist_8h.md)

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[i3c\_device\_desc](structi3c__device__desc.md)

Structure describing a I3C target device.

**Definition** i3c.h:888

[i3c\_ibi\_payload](structi3c__ibi__payload.md)

Structure of payload buffer for IBI.

**Definition** ibi.h:74

[i3c\_ibi\_payload::payload\_len](structi3c__ibi__payload.md#aad4208fcdfef0bc9fb67c86ee1d302de)

uint8\_t payload\_len

Length of available data in the payload buffer.

**Definition** ibi.h:78

[i3c\_ibi\_payload::payload](structi3c__ibi__payload.md#ab869cf38c7a9677fda3ecf48cd358355)

uint8\_t payload[0]

Pointer to byte array as payload buffer.

**Definition** ibi.h:83

[i3c\_ibi\_work](structi3c__ibi__work.md)

Node about a queued IBI.

**Definition** ibi.h:89

[i3c\_ibi\_work::payload](structi3c__ibi__work.md#a08531106055235eaf85cb8fae690235c)

struct i3c\_ibi\_payload payload

IBI payload.

**Definition** ibi.h:119

[i3c\_ibi\_work::controller](structi3c__ibi__work.md#a195e49bd7db79d0f1f45803e42e963ca)

const struct device \* controller

Use for.

**Definition** ibi.h:106

[i3c\_ibi\_work::type](structi3c__ibi__work.md#a3ec8e089facfbb187342e9bf9a525e50)

enum i3c\_ibi\_type type

IBI type.

**Definition** ibi.h:100

[i3c\_ibi\_work::work](structi3c__ibi__work.md#a4a0373423ababe549d00ee13fe657315)

struct k\_work work

k\_work struct.

**Definition** ibi.h:95

[i3c\_ibi\_work::node](structi3c__ibi__work.md#a66ece8f194350c94f8991eaf1ee5bc0b)

sys\_snode\_t node

**Definition** ibi.h:90

[i3c\_ibi\_work::work\_cb](structi3c__ibi__work.md#a6a3dfd49762d96b591b5e248f9ce1668)

k\_work\_handler\_t work\_cb

Generic workqueue callback when type is I3C\_IBI\_WORKQUEUE\_CB.

**Definition** ibi.h:125

[i3c\_ibi\_work::target](structi3c__ibi__work.md#a6c75e0b678fee04f3357c2c1aa9e7376)

struct i3c\_device\_desc \* target

Use for.

**Definition** ibi.h:112

[i3c\_ibi](structi3c__ibi.md)

Struct for IBI request.

**Definition** ibi.h:58

[i3c\_ibi::payload](structi3c__ibi.md#a584e3298059e412d7d3671a451ecc117)

uint8\_t \* payload

Pointer to payload of IBI.

**Definition** ibi.h:63

[i3c\_ibi::ibi\_type](structi3c__ibi.md#a88b0ccd636c042ca929412c42a05bc25)

enum i3c\_ibi\_type ibi\_type

Type of IBI.

**Definition** ibi.h:60

[i3c\_ibi::payload\_len](structi3c__ibi.md#aa51b8214d4a0708861ac9617f844043f)

uint8\_t payload\_len

Length in bytes of the IBI payload.

**Definition** ibi.h:66

[k\_work](structk__work.md)

A structure used to submit work.

**Definition** kernel.h:4006

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i3c](dir_7fe10d7a610a8b04680264e2afe29300.md)
- [ibi.h](ibi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

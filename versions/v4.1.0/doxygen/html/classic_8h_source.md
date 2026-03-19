---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/classic_8h_source.html
original_path: doxygen/html/classic_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

classic.h

[Go to the documentation of this file.](classic_8h.md)

1

4

5/\*

6 \* Copyright (c) 2015-2016 Intel Corporation

7 \* Copyright 2024 NXP

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_CLASSIC\_H\_

12#define ZEPHYR\_INCLUDE\_BLUETOOTH\_CLASSIC\_H\_

13

20

21#include <[stdbool.h](stdbool_8h.md)>

22#include <[string.h](string_8h.md)>

23

24#include <[zephyr/sys/util.h](sys_2util_8h.md)>

25#include <[zephyr/net\_buf.h](net__buf_8h.md)>

26#include <[zephyr/bluetooth/addr.h](addr_8h.md)>

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31

40

45struct bt\_br\_discovery\_priv {

47 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) clock\_offset;

49 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pscan\_rep\_mode;

51 bool resolving;

52};

53

[ 55](structbt__br__discovery__result.md)struct [bt\_br\_discovery\_result](structbt__br__discovery__result.md) {

57 struct bt\_br\_discovery\_priv \_priv;

58

[ 60](structbt__br__discovery__result.md#a833b05883132a0c20690f71b2c14a62a) [bt\_addr\_t](structbt__addr__t.md) [addr](structbt__br__discovery__result.md#a833b05883132a0c20690f71b2c14a62a);

61

[ 63](structbt__br__discovery__result.md#ad1f6bbfc27796e998ed30e307a251841) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__br__discovery__result.md#ad1f6bbfc27796e998ed30e307a251841);

64

[ 66](structbt__br__discovery__result.md#aec239cbb82436ace39c8928a3baa0cf6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cod](structbt__br__discovery__result.md#aec239cbb82436ace39c8928a3baa0cf6)[3];

67

[ 69](structbt__br__discovery__result.md#a6bfe9a421257e2460eb9b4381252f9cc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [eir](structbt__br__discovery__result.md#a6bfe9a421257e2460eb9b4381252f9cc)[240];

70};

71

[ 73](structbt__br__discovery__param.md)struct [bt\_br\_discovery\_param](structbt__br__discovery__param.md) {

[ 77](structbt__br__discovery__param.md#a3087af0c5a264d50a27395d974f99e1e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [length](structbt__br__discovery__param.md#a3087af0c5a264d50a27395d974f99e1e);

78

[ 80](structbt__br__discovery__param.md#ac02d03f8cfdf4ad7aee3178e871cc105) bool [limited](structbt__br__discovery__param.md#ac02d03f8cfdf4ad7aee3178e871cc105);

81};

82

[ 100](group__bt__gap.md#ga9760190192dde5c498ec96628468be8d)int [bt\_br\_discovery\_start](group__bt__gap.md#ga9760190192dde5c498ec96628468be8d)(const struct [bt\_br\_discovery\_param](structbt__br__discovery__param.md) \*param,

101 struct [bt\_br\_discovery\_result](structbt__br__discovery__result.md) \*results, size\_t count);

102

[ 112](group__bt__gap.md#ga567c71b49399fe7e1a5593edbf005e3a)int [bt\_br\_discovery\_stop](group__bt__gap.md#ga567c71b49399fe7e1a5593edbf005e3a)(void);

113

[ 114](structbt__br__discovery__cb.md)struct [bt\_br\_discovery\_cb](structbt__br__discovery__cb.md) {

115

[ 121](structbt__br__discovery__cb.md#a3315f86bf3c9dbf339aa2254e0679182) void (\*[recv](structbt__br__discovery__cb.md#a3315f86bf3c9dbf339aa2254e0679182))(const struct [bt\_br\_discovery\_result](structbt__br__discovery__result.md) \*result);

122

[ 128](structbt__br__discovery__cb.md#a09c9f7258ea1739bf9330cf5c5bd882d) void (\*[timeout](structbt__br__discovery__cb.md#a09c9f7258ea1739bf9330cf5c5bd882d))(const struct [bt\_br\_discovery\_result](structbt__br__discovery__result.md) \*results,

129 size\_t count);

130

[ 131](structbt__br__discovery__cb.md#a6ea814cabf9747cc7720ece9be59c8b9) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structbt__br__discovery__cb.md#a6ea814cabf9747cc7720ece9be59c8b9);

132};

133

[ 145](group__bt__gap.md#ga430de0ad30da7322c5353941f1f6a133)void [bt\_br\_discovery\_cb\_register](group__bt__gap.md#ga430de0ad30da7322c5353941f1f6a133)(struct [bt\_br\_discovery\_cb](structbt__br__discovery__cb.md) \*cb);

146

[ 154](group__bt__gap.md#ga25ab96ac005237aee739bf32fc1aac94)void [bt\_br\_discovery\_cb\_unregister](group__bt__gap.md#ga25ab96ac005237aee739bf32fc1aac94)(struct [bt\_br\_discovery\_cb](structbt__br__discovery__cb.md) \*cb);

155

[ 156](structbt__br__oob.md)struct [bt\_br\_oob](structbt__br__oob.md) {

[ 158](structbt__br__oob.md#a9b9f4c830a4e48736ac6b793d628ee98) [bt\_addr\_t](structbt__addr__t.md) [addr](structbt__br__oob.md#a9b9f4c830a4e48736ac6b793d628ee98);

159};

160

[ 169](group__bt__gap.md#ga2ec860d06c45098624b106b59fbab634)int [bt\_br\_oob\_get\_local](group__bt__gap.md#ga2ec860d06c45098624b106b59fbab634)(struct [bt\_br\_oob](structbt__br__oob.md) \*oob);

170

[ 183](group__bt__gap.md#gad3b9075cc9bab5c1ae37514a6dfe555c)int [bt\_br\_set\_discoverable](group__bt__gap.md#gad3b9075cc9bab5c1ae37514a6dfe555c)(bool enable);

184

[ 197](group__bt__gap.md#ga80aed18a099948bef8f3649ad537e541)int [bt\_br\_set\_connectable](group__bt__gap.md#ga80aed18a099948bef8f3649ad537e541)(bool enable);

198

202

203#ifdef \_\_cplusplus

204}

205#endif

209

210#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_CLASSIC\_H\_ \*/

[addr.h](addr_8h.md)

Bluetooth device address definitions and utilities.

[bt\_br\_discovery\_cb\_unregister](group__bt__gap.md#ga25ab96ac005237aee739bf32fc1aac94)

void bt\_br\_discovery\_cb\_unregister(struct bt\_br\_discovery\_cb \*cb)

Unregister discovery packet callbacks.

[bt\_br\_oob\_get\_local](group__bt__gap.md#ga2ec860d06c45098624b106b59fbab634)

int bt\_br\_oob\_get\_local(struct bt\_br\_oob \*oob)

Get BR/EDR local Out Of Band information.

[bt\_br\_discovery\_cb\_register](group__bt__gap.md#ga430de0ad30da7322c5353941f1f6a133)

void bt\_br\_discovery\_cb\_register(struct bt\_br\_discovery\_cb \*cb)

Register discovery packet callbacks.

[bt\_br\_discovery\_stop](group__bt__gap.md#ga567c71b49399fe7e1a5593edbf005e3a)

int bt\_br\_discovery\_stop(void)

Stop BR/EDR discovery.

[bt\_br\_set\_connectable](group__bt__gap.md#ga80aed18a099948bef8f3649ad537e541)

int bt\_br\_set\_connectable(bool enable)

Enable/disable set controller in connectable state.

[bt\_br\_discovery\_start](group__bt__gap.md#ga9760190192dde5c498ec96628468be8d)

int bt\_br\_discovery\_start(const struct bt\_br\_discovery\_param \*param, struct bt\_br\_discovery\_result \*results, size\_t count)

Start BR/EDR discovery.

[bt\_br\_set\_discoverable](group__bt__gap.md#gad3b9075cc9bab5c1ae37514a6dfe555c)

int bt\_br\_set\_discoverable(bool enable)

Enable/disable set controller in discoverable state.

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[net\_buf.h](net__buf_8h.md)

Buffer management.

[stdbool.h](stdbool_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[string.h](string_8h.md)

[bt\_addr\_t](structbt__addr__t.md)

Bluetooth Device Address.

**Definition** addr.h:40

[bt\_br\_discovery\_cb](structbt__br__discovery__cb.md)

**Definition** classic.h:114

[bt\_br\_discovery\_cb::timeout](structbt__br__discovery__cb.md#a09c9f7258ea1739bf9330cf5c5bd882d)

void(\* timeout)(const struct bt\_br\_discovery\_result \*results, size\_t count)

The inquiry has stopped after discovery timeout.

**Definition** classic.h:128

[bt\_br\_discovery\_cb::recv](structbt__br__discovery__cb.md#a3315f86bf3c9dbf339aa2254e0679182)

void(\* recv)(const struct bt\_br\_discovery\_result \*result)

An inquiry response received callback.

**Definition** classic.h:121

[bt\_br\_discovery\_cb::node](structbt__br__discovery__cb.md#a6ea814cabf9747cc7720ece9be59c8b9)

sys\_snode\_t node

**Definition** classic.h:131

[bt\_br\_discovery\_param](structbt__br__discovery__param.md)

BR/EDR discovery parameters.

**Definition** classic.h:73

[bt\_br\_discovery\_param::length](structbt__br__discovery__param.md#a3087af0c5a264d50a27395d974f99e1e)

uint8\_t length

Maximum length of the discovery in units of 1.28 seconds.

**Definition** classic.h:77

[bt\_br\_discovery\_param::limited](structbt__br__discovery__param.md#ac02d03f8cfdf4ad7aee3178e871cc105)

bool limited

True if limited discovery procedure is to be used.

**Definition** classic.h:80

[bt\_br\_discovery\_result](structbt__br__discovery__result.md)

BR/EDR discovery result structure.

**Definition** classic.h:55

[bt\_br\_discovery\_result::eir](structbt__br__discovery__result.md#a6bfe9a421257e2460eb9b4381252f9cc)

uint8\_t eir[240]

Extended Inquiry Response.

**Definition** classic.h:69

[bt\_br\_discovery\_result::addr](structbt__br__discovery__result.md#a833b05883132a0c20690f71b2c14a62a)

bt\_addr\_t addr

Remote device address.

**Definition** classic.h:60

[bt\_br\_discovery\_result::rssi](structbt__br__discovery__result.md#ad1f6bbfc27796e998ed30e307a251841)

int8\_t rssi

RSSI from inquiry.

**Definition** classic.h:63

[bt\_br\_discovery\_result::cod](structbt__br__discovery__result.md#aec239cbb82436ace39c8928a3baa0cf6)

uint8\_t cod[3]

Class of Device.

**Definition** classic.h:66

[bt\_br\_oob](structbt__br__oob.md)

**Definition** classic.h:156

[bt\_br\_oob::addr](structbt__br__oob.md#a9b9f4c830a4e48736ac6b793d628ee98)

bt\_addr\_t addr

BR/EDR address.

**Definition** classic.h:158

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [classic](dir_28cc012f073a9d41ddbe6a63c5d8e2de.md)
- [classic.h](classic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

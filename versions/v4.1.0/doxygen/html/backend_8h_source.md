---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/backend_8h_source.html
original_path: doxygen/html/backend_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

backend.h

[Go to the documentation of this file.](backend_8h.md)

1/\*

2 \* Copyright (c) 2020 Google LLC.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_MGMT\_EC\_HOST\_CMD\_BACKEND\_H\_

13#define ZEPHYR\_INCLUDE\_MGMT\_EC\_HOST\_CMD\_BACKEND\_H\_

14

15#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

16#include <[zephyr/device.h](device_8h.md)>

17#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h.md)>

18#include <[zephyr/kernel.h](kernel_8h.md)>

19#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

[ 25](structec__host__cmd__backend.md)struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) {

[ 27](structec__host__cmd__backend.md#aadf44f4eff331abeca40bc0f69bc173d) const struct [ec\_host\_cmd\_backend\_api](structec__host__cmd__backend__api.md) \*[api](structec__host__cmd__backend.md#aadf44f4eff331abeca40bc0f69bc173d);

[ 29](structec__host__cmd__backend.md#a57236d69bdc9a99b1cb3acbac0be275b) void \*[ctx](structec__host__cmd__backend.md#a57236d69bdc9a99b1cb3acbac0be275b);

30};

31

38

[ 42](structec__host__cmd__rx__ctx.md)struct [ec\_host\_cmd\_rx\_ctx](structec__host__cmd__rx__ctx.md) {

[ 49](structec__host__cmd__rx__ctx.md#afcae3b7881f1c8634bb3ac1315111294) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structec__host__cmd__rx__ctx.md#afcae3b7881f1c8634bb3ac1315111294);

[ 51](structec__host__cmd__rx__ctx.md#ae9f1c0c78d27dd5aa9bf47c56452a75a) size\_t [len](structec__host__cmd__rx__ctx.md#ae9f1c0c78d27dd5aa9bf47c56452a75a);

[ 53](structec__host__cmd__rx__ctx.md#a2db5dc5740436c8e0e232b959472ed0f) size\_t [len\_max](structec__host__cmd__rx__ctx.md#a2db5dc5740436c8e0e232b959472ed0f);

54};

55

[ 59](structec__host__cmd__tx__buf.md)struct [ec\_host\_cmd\_tx\_buf](structec__host__cmd__tx__buf.md) {

[ 66](structec__host__cmd__tx__buf.md#a6444723bccc196fb9792e95957bd98a5) void \*[buf](structec__host__cmd__tx__buf.md#a6444723bccc196fb9792e95957bd98a5);

[ 68](structec__host__cmd__tx__buf.md#afaff8fbcb798a0445b029db1cedb6fd1) size\_t [len](structec__host__cmd__tx__buf.md#afaff8fbcb798a0445b029db1cedb6fd1);

[ 70](structec__host__cmd__tx__buf.md#a0f115f85bd271fa0defec1a2fc461d4c) size\_t [len\_max](structec__host__cmd__tx__buf.md#a0f115f85bd271fa0defec1a2fc461d4c);

71};

72

[ 90](group__ec__host__cmd__interface.md#ga811b9c355942811f0fee22c1fa8a5787)typedef int (\*[ec\_host\_cmd\_backend\_api\_init](group__ec__host__cmd__interface.md#ga811b9c355942811f0fee22c1fa8a5787))(const struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \*backend,

91 struct [ec\_host\_cmd\_rx\_ctx](structec__host__cmd__rx__ctx.md) \*rx\_ctx,

92 struct [ec\_host\_cmd\_tx\_buf](structec__host__cmd__tx__buf.md) \*tx);

93

[ 104](group__ec__host__cmd__interface.md#ga1097b2148a5e7e6bf9f2a67e54dd5ba5)typedef int (\*[ec\_host\_cmd\_backend\_api\_send](group__ec__host__cmd__interface.md#ga1097b2148a5e7e6bf9f2a67e54dd5ba5))(const struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \*backend);

105

[ 106](structec__host__cmd__backend__api.md)struct [ec\_host\_cmd\_backend\_api](structec__host__cmd__backend__api.md) {

[ 107](structec__host__cmd__backend__api.md#ae2619efe5d809f7aa51252727b1a05c4) [ec\_host\_cmd\_backend\_api\_init](group__ec__host__cmd__interface.md#ga811b9c355942811f0fee22c1fa8a5787) [init](structec__host__cmd__backend__api.md#ae2619efe5d809f7aa51252727b1a05c4);

[ 108](structec__host__cmd__backend__api.md#afed14f2aa633e836c90c8c559a9fe7bb) [ec\_host\_cmd\_backend\_api\_send](group__ec__host__cmd__interface.md#ga1097b2148a5e7e6bf9f2a67e54dd5ba5) [send](structec__host__cmd__backend__api.md#afed14f2aa633e836c90c8c559a9fe7bb);

109};

110

[ 121](group__ec__host__cmd__interface.md#ga32d7a58724694ab753efbf7f81e8d940)struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \*[ec\_host\_cmd\_backend\_get\_espi](group__ec__host__cmd__interface.md#ga32d7a58724694ab753efbf7f81e8d940)(const struct [device](structdevice.md) \*dev);

122

[ 128](group__ec__host__cmd__interface.md#gaa4562dd46503cf8844a546b102ce01e9)struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \*[ec\_host\_cmd\_backend\_get\_shi\_npcx](group__ec__host__cmd__interface.md#gaa4562dd46503cf8844a546b102ce01e9)(void);

129

[ 135](group__ec__host__cmd__interface.md#ga892fec4587de508805fdf5ace9dd1050)struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \*[ec\_host\_cmd\_backend\_get\_shi\_ite](group__ec__host__cmd__interface.md#ga892fec4587de508805fdf5ace9dd1050)(void);

136

[ 147](group__ec__host__cmd__interface.md#ga558b7690dad9a9a5eb8771fcfeba3b63)struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \*[ec\_host\_cmd\_backend\_get\_uart](group__ec__host__cmd__interface.md#ga558b7690dad9a9a5eb8771fcfeba3b63)(const struct [device](structdevice.md) \*dev);

148

[ 159](group__ec__host__cmd__interface.md#ga12574d2eff8f07fd36967ccbc7600e1c)struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \*[ec\_host\_cmd\_backend\_get\_spi](group__ec__host__cmd__interface.md#ga12574d2eff8f07fd36967ccbc7600e1c)(struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*cs);

160

164

165#ifdef \_\_cplusplus

166}

167#endif

168

169#endif /\* ZEPHYR\_INCLUDE\_MGMT\_EC\_HOST\_CMD\_EC\_HOST\_CMD\_BACKEND\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[device.h](device_8h.md)

[gpio.h](drivers_2gpio_8h.md)

Public APIs for GPIO drivers.

[ec\_host\_cmd\_backend\_api\_send](group__ec__host__cmd__interface.md#ga1097b2148a5e7e6bf9f2a67e54dd5ba5)

int(\* ec\_host\_cmd\_backend\_api\_send)(const struct ec\_host\_cmd\_backend \*backend)

Sends data to the host.

**Definition** backend.h:104

[ec\_host\_cmd\_backend\_get\_spi](group__ec__host__cmd__interface.md#ga12574d2eff8f07fd36967ccbc7600e1c)

struct ec\_host\_cmd\_backend \* ec\_host\_cmd\_backend\_get\_spi(struct gpio\_dt\_spec \*cs)

Get the SPI Host Command backend pointer.

[ec\_host\_cmd\_backend\_get\_espi](group__ec__host__cmd__interface.md#ga32d7a58724694ab753efbf7f81e8d940)

struct ec\_host\_cmd\_backend \* ec\_host\_cmd\_backend\_get\_espi(const struct device \*dev)

Get the eSPI Host Command backend pointer.

[ec\_host\_cmd\_backend\_get\_uart](group__ec__host__cmd__interface.md#ga558b7690dad9a9a5eb8771fcfeba3b63)

struct ec\_host\_cmd\_backend \* ec\_host\_cmd\_backend\_get\_uart(const struct device \*dev)

Get the UART Host Command backend pointer.

[ec\_host\_cmd\_backend\_api\_init](group__ec__host__cmd__interface.md#ga811b9c355942811f0fee22c1fa8a5787)

int(\* ec\_host\_cmd\_backend\_api\_init)(const struct ec\_host\_cmd\_backend \*backend, struct ec\_host\_cmd\_rx\_ctx \*rx\_ctx, struct ec\_host\_cmd\_tx\_buf \*tx)

Initialize a host command backend.

**Definition** backend.h:90

[ec\_host\_cmd\_backend\_get\_shi\_ite](group__ec__host__cmd__interface.md#ga892fec4587de508805fdf5ace9dd1050)

struct ec\_host\_cmd\_backend \* ec\_host\_cmd\_backend\_get\_shi\_ite(void)

Get the SHI ITE Host Command backend pointer.

[ec\_host\_cmd\_backend\_get\_shi\_npcx](group__ec__host__cmd__interface.md#gaa4562dd46503cf8844a546b102ce01e9)

struct ec\_host\_cmd\_backend \* ec\_host\_cmd\_backend\_get\_shi\_npcx(void)

Get the SHI NPCX Host Command backend pointer.

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[ec\_host\_cmd\_backend\_api](structec__host__cmd__backend__api.md)

**Definition** backend.h:106

[ec\_host\_cmd\_backend\_api::init](structec__host__cmd__backend__api.md#ae2619efe5d809f7aa51252727b1a05c4)

ec\_host\_cmd\_backend\_api\_init init

**Definition** backend.h:107

[ec\_host\_cmd\_backend\_api::send](structec__host__cmd__backend__api.md#afed14f2aa633e836c90c8c559a9fe7bb)

ec\_host\_cmd\_backend\_api\_send send

**Definition** backend.h:108

[ec\_host\_cmd\_backend](structec__host__cmd__backend.md)

**Definition** backend.h:25

[ec\_host\_cmd\_backend::ctx](structec__host__cmd__backend.md#a57236d69bdc9a99b1cb3acbac0be275b)

void \* ctx

Context for the backed.

**Definition** backend.h:29

[ec\_host\_cmd\_backend::api](structec__host__cmd__backend.md#aadf44f4eff331abeca40bc0f69bc173d)

const struct ec\_host\_cmd\_backend\_api \* api

API provided by the backed.

**Definition** backend.h:27

[ec\_host\_cmd\_rx\_ctx](structec__host__cmd__rx__ctx.md)

Context for host command backend and handler to pass rx data.

**Definition** backend.h:42

[ec\_host\_cmd\_rx\_ctx::len\_max](structec__host__cmd__rx__ctx.md#a2db5dc5740436c8e0e232b959472ed0f)

size\_t len\_max

Maximum number of bytes to receive with one request packet.

**Definition** backend.h:53

[ec\_host\_cmd\_rx\_ctx::len](structec__host__cmd__rx__ctx.md#ae9f1c0c78d27dd5aa9bf47c56452a75a)

size\_t len

Number of bytes written to buf by backend.

**Definition** backend.h:51

[ec\_host\_cmd\_rx\_ctx::buf](structec__host__cmd__rx__ctx.md#afcae3b7881f1c8634bb3ac1315111294)

uint8\_t \* buf

Buffer to hold received data.

**Definition** backend.h:49

[ec\_host\_cmd\_tx\_buf](structec__host__cmd__tx__buf.md)

Context for host command backend and handler to pass tx data.

**Definition** backend.h:59

[ec\_host\_cmd\_tx\_buf::len\_max](structec__host__cmd__tx__buf.md#a0f115f85bd271fa0defec1a2fc461d4c)

size\_t len\_max

Maximum number of bytes to send with one response packet.

**Definition** backend.h:70

[ec\_host\_cmd\_tx\_buf::buf](structec__host__cmd__tx__buf.md#a6444723bccc196fb9792e95957bd98a5)

void \* buf

Data to write to the host The buffer is provided by the handler if CONFIG\_EC\_HOST\_CMD\_HANDLER\_TX\_BUFF...

**Definition** backend.h:66

[ec\_host\_cmd\_tx\_buf::len](structec__host__cmd__tx__buf.md#afaff8fbcb798a0445b029db1cedb6fd1)

size\_t len

Number of bytes to write from buf.

**Definition** backend.h:68

[gpio\_dt\_spec](structgpio__dt__spec.md)

Container for GPIO pin information specified in devicetree.

**Definition** gpio.h:289

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [ec\_host\_cmd](dir_d53ada025add0f463456d44507c0d96c.md)
- [backend.h](backend_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

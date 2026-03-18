---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/coap__link__format_8h_source.html
original_path: doxygen/html/coap__link__format_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

coap\_link\_format.h

[Go to the documentation of this file.](coap__link__format_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

12

13#ifndef ZEPHYR\_INCLUDE\_NET\_COAP\_LINK\_FORMAT\_H\_

14#define ZEPHYR\_INCLUDE\_NET\_COAP\_LINK\_FORMAT\_H\_

15

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

[ 30](group__coap.md#ga09d2c727fc6fc76aa9d908b759a3f40b)#define COAP\_WELL\_KNOWN\_CORE\_PATH \

31 ((const char \* const[]) { ".well-known", "core", NULL })

32

[ 44](group__coap.md#ga3f2eded87dbeb7408ff6f07e04afb30b)int [coap\_well\_known\_core\_get](group__coap.md#ga3f2eded87dbeb7408ff6f07e04afb30b)(struct [coap\_resource](structcoap__resource.md) \*resource,

45 const struct [coap\_packet](structcoap__packet.md) \*request,

46 struct [coap\_packet](structcoap__packet.md) \*response,

47 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len);

48

[ 61](group__coap.md#ga49d63f12b593d7509690a504b05da730)int [coap\_well\_known\_core\_get\_len](group__coap.md#ga49d63f12b593d7509690a504b05da730)(struct [coap\_resource](structcoap__resource.md) \*resources,

62 size\_t resources\_len,

63 const struct [coap\_packet](structcoap__packet.md) \*request,

64 struct [coap\_packet](structcoap__packet.md) \*response,

65 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len);

66

[ 72](structcoap__core__metadata.md)struct [coap\_core\_metadata](structcoap__core__metadata.md) {

[ 73](structcoap__core__metadata.md#aeb04ef8b47ecc144dd036007cccd2e59) const char \* const \*[attributes](structcoap__core__metadata.md#aeb04ef8b47ecc144dd036007cccd2e59);

[ 74](structcoap__core__metadata.md#a74e8a533d7f8596498d5d0ce2afc102f) void \*[user\_data](structcoap__core__metadata.md#a74e8a533d7f8596498d5d0ce2afc102f);

75};

76

77#ifdef \_\_cplusplus

78}

79#endif

80

84

85#endif /\* ZEPHYR\_INCLUDE\_NET\_COAP\_LINK\_FORMAT\_H\_ \*/

[coap\_well\_known\_core\_get](group__coap.md#ga3f2eded87dbeb7408ff6f07e04afb30b)

int coap\_well\_known\_core\_get(struct coap\_resource \*resource, const struct coap\_packet \*request, struct coap\_packet \*response, uint8\_t \*data, uint16\_t data\_len)

Build a CoAP response for a .well-known/core CoAP request.

[coap\_well\_known\_core\_get\_len](group__coap.md#ga49d63f12b593d7509690a504b05da730)

int coap\_well\_known\_core\_get\_len(struct coap\_resource \*resources, size\_t resources\_len, const struct coap\_packet \*request, struct coap\_packet \*response, uint8\_t \*data, uint16\_t data\_len)

Build a CoAP response for a .well-known/core CoAP request.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[coap\_core\_metadata](structcoap__core__metadata.md)

In case you want to add attributes to the resources included in the 'well-known/core' "virtual" resou...

**Definition** coap\_link\_format.h:72

[coap\_core\_metadata::user\_data](structcoap__core__metadata.md#a74e8a533d7f8596498d5d0ce2afc102f)

void \* user\_data

**Definition** coap\_link\_format.h:74

[coap\_core\_metadata::attributes](structcoap__core__metadata.md#aeb04ef8b47ecc144dd036007cccd2e59)

const char \*const \* attributes

**Definition** coap\_link\_format.h:73

[coap\_packet](structcoap__packet.md)

Representation of a CoAP Packet.

**Definition** coap.h:270

[coap\_resource](structcoap__resource.md)

Description of CoAP resource.

**Definition** coap.h:247

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [coap\_link\_format.h](coap__link__format_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

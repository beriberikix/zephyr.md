---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/log__internal_8h_source.html
original_path: doxygen/html/log__internal_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_internal.h

[Go to the documentation of this file.](log__internal_8h.md)

1/\*

2 \* Copyright (c) 2021 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_LOGGING\_LOG\_INTERNAL\_H\_

7#define ZEPHYR\_INCLUDE\_LOGGING\_LOG\_INTERNAL\_H\_

8

9#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

10#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

11#include <[zephyr/logging/log\_core.h](log__core_8h.md)>

12#include <[zephyr/sys/mpsc\_pbuf.h](mpsc__pbuf_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

18/\* Header contains declarations of functions used internally in the logging,

19 \* shared between various portions of logging subsystem. Functions are internal

20 \* not intended to be used outside, including logging backends.

21 \*/

22

[ 24](structlog__mpsc__pbuf.md)struct [log\_mpsc\_pbuf](structlog__mpsc__pbuf.md) {

[ 25](structlog__mpsc__pbuf.md#ac5349613a2a7505e124401af1020fa13) struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) [buf](structlog__mpsc__pbuf.md#ac5349613a2a7505e124401af1020fa13);

26};

27

[ 29](structlog__msg__ptr.md)struct [log\_msg\_ptr](structlog__msg__ptr.md) {

[ 30](structlog__msg__ptr.md#a9948bc14a584c773bfecff939e1f82af) union [log\_msg\_generic](unionlog__msg__generic.md) \*[msg](structlog__msg__ptr.md#a9948bc14a584c773bfecff939e1f82af);

31};

32

39void z\_log\_dropped(bool buffered);

40

45[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_log\_dropped\_read\_and\_clear(void);

46

52bool z\_log\_dropped\_pending(void);

53

58void z\_log\_free(void \*[buf](unionlog__msg__generic.md#a74b4fa4fff98e914f8e7536fe0be568d));

59

60/\* Initialize runtime filters \*/

61void z\_log\_runtime\_filters\_init(void);

62

63/\* Initialize links. \*/

64void z\_log\_links\_initiate(void);

65

66/\* Activate links.

67 \* Attempt to activate links,

68 \*

69 \* @param active\_mask Mask with links to activate. N bit set indicates that Nth

70 \* link should be activated.

71 \*

72 \* @param[in, out] offset Offset assigned to domains. Initialize to 0 before first use.

73 \*

74 \* @return Mask with links that still remain inactive.

75 \*/

76[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_log\_links\_activate([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) active\_mask, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*offset);

77

78/\* Notify log\_core that a backend was enabled. \*/

79void z\_log\_notify\_backend\_enabled(void);

80

87static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*z\_log\_dynamic\_filters\_get([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) source\_id)

88{

89 return &[TYPE\_SECTION\_START](group__iterable__section__apis.md#gac97b7f4fd42a2d9e11b6a585bc716a05)(log\_dynamic)[source\_id].filters;

90}

91

93static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_log\_sources\_count(void)

94{

95 return [log\_const\_source\_id](log__core_8h.md#add353f5f883b7edee6428adb7fb7e4d5)([TYPE\_SECTION\_END](group__iterable__section__apis.md#ga14d6bc375423775e5484183eeadd1fad)(log\_const));

96}

97

102[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) z\_log\_ext\_domain\_count(void);

103

105void z\_log\_msg\_init(void);

106

111void z\_log\_msg\_commit(struct [log\_msg](structlog__msg.md) \*msg);

112

118union [log\_msg\_generic](unionlog__msg__generic.md) \*z\_log\_msg\_claim([k\_timeout\_t](structk__timeout__t.md) \*backoff);

119

124void z\_log\_msg\_free(union [log\_msg\_generic](unionlog__msg__generic.md) \*msg);

125

131bool z\_log\_msg\_pending(void);

132

133static inline void z\_log\_notify\_drop(const struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer,

134 const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \*item)

135{

136 ARG\_UNUSED(buffer);

137 ARG\_UNUSED(item);

138

139 z\_log\_dropped(true);

140}

141

146const char \*z\_log\_get\_tag(void);

147

154static inline bool z\_log\_is\_local\_domain([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) domain\_id)

155{

156 return ![IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_LOG\_MULTIDOMAIN) ||

157 (domain\_id == Z\_LOG\_LOCAL\_DOMAIN\_ID);

158}

159

164[log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8) z\_log\_timestamp(void);

165

166#ifdef \_\_cplusplus

167}

168#endif

169

170#endif /\* ZEPHYR\_INCLUDE\_LOGGING\_LOG\_INTERNAL\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[TYPE\_SECTION\_END](group__iterable__section__apis.md#ga14d6bc375423775e5484183eeadd1fad)

#define TYPE\_SECTION\_END(secname)

iterable section end symbol for a generic type

**Definition** iterable\_sections.h:65

[TYPE\_SECTION\_START](group__iterable__section__apis.md#gac97b7f4fd42a2d9e11b6a585bc716a05)

#define TYPE\_SECTION\_START(secname)

iterable section start symbol for a generic type

**Definition** iterable\_sections.h:55

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:148

[types.h](include_2zephyr_2types_8h.md)

[log\_core.h](log__core_8h.md)

[log\_const\_source\_id](log__core_8h.md#add353f5f883b7edee6428adb7fb7e4d5)

static uint32\_t log\_const\_source\_id(const struct log\_source\_const\_data \*data)

Get index of the log source based on the address of the constant data associated with the source.

**Definition** log\_core.h:468

[log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8)

uint32\_t log\_timestamp\_t

**Definition** log\_msg.h:36

[mpsc\_pbuf.h](mpsc__pbuf_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[log\_mpsc\_pbuf](structlog__mpsc__pbuf.md)

Structure wrapper to be used for memory section.

**Definition** log\_internal.h:24

[log\_mpsc\_pbuf::buf](structlog__mpsc__pbuf.md#ac5349613a2a7505e124401af1020fa13)

struct mpsc\_pbuf\_buffer buf

**Definition** log\_internal.h:25

[log\_msg\_ptr](structlog__msg__ptr.md)

Structure wrapper to be used for memory section.

**Definition** log\_internal.h:29

[log\_msg\_ptr::msg](structlog__msg__ptr.md#a9948bc14a584c773bfecff939e1f82af)

union log\_msg\_generic \* msg

**Definition** log\_internal.h:30

[log\_msg](structlog__msg.md)

**Definition** log\_msg.h:94

[mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md)

MPSC packet buffer structure.

**Definition** mpsc\_pbuf.h:90

[log\_msg\_generic](unionlog__msg__generic.md)

**Definition** log\_msg.h:117

[log\_msg\_generic::buf](unionlog__msg__generic.md#a74b4fa4fff98e914f8e7536fe0be568d)

union mpsc\_pbuf\_generic buf

**Definition** log\_msg.h:118

[mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md)

Generic packet header.

**Definition** mpsc\_packet.h:49

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_internal.h](log__internal_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

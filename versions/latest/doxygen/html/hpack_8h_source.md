---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/hpack_8h_source.html
original_path: doxygen/html/hpack_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hpack.h

[Go to the documentation of this file.](hpack_8h.md)

1

4

5/\*

6 \* Copyright (c) 2023 Emna Rekik

7 \* Copyright (c) 2024 Nordic Semiconductor ASA

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11

12#ifndef ZEPHYR\_INCLUDE\_NET\_HTTP\_SERVER\_HPACK\_H\_

13#define ZEPHYR\_INCLUDE\_NET\_HTTP\_SERVER\_HPACK\_H\_

14

15#include <stddef.h>

16#include <[stdint.h](stdint_8h.md)>

17

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

30

31enum http\_hpack\_static\_key {

32 HTTP\_SERVER\_HPACK\_INVALID = 0,

33 HTTP\_SERVER\_HPACK\_AUTHORITY = 1,

34 HTTP\_SERVER\_HPACK\_METHOD\_GET = 2,

35 HTTP\_SERVER\_HPACK\_METHOD\_POST = 3,

36 HTTP\_SERVER\_HPACK\_PATH\_ROOT = 4,

37 HTTP\_SERVER\_HPACK\_PATH\_INDEX = 5,

38 HTTP\_SERVER\_HPACK\_SCHEME\_HTTP = 6,

39 HTTP\_SERVER\_HPACK\_SCHEME\_HTTPS = 7,

40 HTTP\_SERVER\_HPACK\_STATUS\_200 = 8,

41 HTTP\_SERVER\_HPACK\_STATUS\_204 = 9,

42 HTTP\_SERVER\_HPACK\_STATUS\_206 = 10,

43 HTTP\_SERVER\_HPACK\_STATUS\_304 = 11,

44 HTTP\_SERVER\_HPACK\_STATUS\_400 = 12,

45 HTTP\_SERVER\_HPACK\_STATUS\_404 = 13,

46 HTTP\_SERVER\_HPACK\_STATUS\_500 = 14,

47 HTTP\_SERVER\_HPACK\_ACCEPT\_CHARSET = 15,

48 HTTP\_SERVER\_HPACK\_ACCEPT\_ENCODING = 16,

49 HTTP\_SERVER\_HPACK\_ACCEPT\_LANGUAGE = 17,

50 HTTP\_SERVER\_HPACK\_ACCEPT\_RANGES = 18,

51 HTTP\_SERVER\_HPACK\_ACCEPT = 19,

52 HTTP\_SERVER\_HPACK\_ACCESS\_CONTROL\_ALLOW\_ORIGIN = 20,

53 HTTP\_SERVER\_HPACK\_AGE = 21,

54 HTTP\_SERVER\_HPACK\_ALLOW = 22,

55 HTTP\_SERVER\_HPACK\_AUTHORIZATION = 23,

56 HTTP\_SERVER\_HPACK\_CACHE\_CONTROL = 24,

57 HTTP\_SERVER\_HPACK\_CONTENT\_DISPOSITION = 25,

58 HTTP\_SERVER\_HPACK\_CONTENT\_ENCODING = 26,

59 HTTP\_SERVER\_HPACK\_CONTENT\_LANGUAGE = 27,

60 HTTP\_SERVER\_HPACK\_CONTENT\_LENGTH = 28,

61 HTTP\_SERVER\_HPACK\_CONTENT\_LOCATION = 29,

62 HTTP\_SERVER\_HPACK\_CONTENT\_RANGE = 30,

63 HTTP\_SERVER\_HPACK\_CONTENT\_TYPE = 31,

64 HTTP\_SERVER\_HPACK\_COOKIE = 32,

65 HTTP\_SERVER\_HPACK\_DATE = 33,

66 HTTP\_SERVER\_HPACK\_ETAG = 34,

67 HTTP\_SERVER\_HPACK\_EXPECT = 35,

68 HTTP\_SERVER\_HPACK\_EXPIRES = 36,

69 HTTP\_SERVER\_HPACK\_FROM = 37,

70 HTTP\_SERVER\_HPACK\_HOST = 38,

71 HTTP\_SERVER\_HPACK\_IF\_MATCH = 39,

72 HTTP\_SERVER\_HPACK\_IF\_MODIFIED\_SINCE = 40,

73 HTTP\_SERVER\_HPACK\_IF\_NONE\_MATCH = 41,

74 HTTP\_SERVER\_HPACK\_IF\_RANGE = 42,

75 HTTP\_SERVER\_HPACK\_IF\_UNMODIFIED\_SINCE = 43,

76 HTTP\_SERVER\_HPACK\_LAST\_MODIFIED = 44,

77 HTTP\_SERVER\_HPACK\_LINK = 45,

78 HTTP\_SERVER\_HPACK\_LOCATION = 46,

79 HTTP\_SERVER\_HPACK\_MAX\_FORWARDS = 47,

80 HTTP\_SERVER\_HPACK\_PROXY\_AUTHENTICATE = 48,

81 HTTP\_SERVER\_HPACK\_PROXY\_AUTHORIZATION = 49,

82 HTTP\_SERVER\_HPACK\_RANGE = 50,

83 HTTP\_SERVER\_HPACK\_REFERER = 51,

84 HTTP\_SERVER\_HPACK\_REFRESH = 52,

85 HTTP\_SERVER\_HPACK\_RETRY\_AFTER = 53,

86 HTTP\_SERVER\_HPACK\_SERVER = 54,

87 HTTP\_SERVER\_HPACK\_SET\_COOKIE = 55,

88 HTTP\_SERVER\_HPACK\_STRICT\_TRANSPORT\_SECURITY = 56,

89 HTTP\_SERVER\_HPACK\_TRANSFER\_ENCODING = 57,

90 HTTP\_SERVER\_HPACK\_USER\_AGENT = 58,

91 HTTP\_SERVER\_HPACK\_VARY = 59,

92 HTTP\_SERVER\_HPACK\_VIA = 60,

93 HTTP\_SERVER\_HPACK\_WWW\_AUTHENTICATE = 61,

94};

95

96/\* TODO Kconfig \*/

97#define HTTP2\_HEADER\_FIELD\_MAX\_LEN 256

98

99#if defined(CONFIG\_HTTP\_SERVER)

100#define HTTP\_SERVER\_HUFFMAN\_DECODE\_BUFFER\_SIZE CONFIG\_HTTP\_SERVER\_HUFFMAN\_DECODE\_BUFFER\_SIZE

101#else

102#define HTTP\_SERVER\_HUFFMAN\_DECODE\_BUFFER\_SIZE 0

103#endif

104

106

[ 108](structhttp__hpack__header__buf.md)struct [http\_hpack\_header\_buf](structhttp__hpack__header__buf.md) {

[ 110](structhttp__hpack__header__buf.md#ac0b781b733a16dc0c9e99753a4d2b25d) const char \*[name](structhttp__hpack__header__buf.md#ac0b781b733a16dc0c9e99753a4d2b25d);

111

[ 113](structhttp__hpack__header__buf.md#a957db215f89359b64a76e98e878e8c83) const char \*[value](structhttp__hpack__header__buf.md#a957db215f89359b64a76e98e878e8c83);

114

[ 116](structhttp__hpack__header__buf.md#ad6079192782eec8e4a0c1d89018c6d7b) size\_t [name\_len](structhttp__hpack__header__buf.md#ad6079192782eec8e4a0c1d89018c6d7b);

117

[ 119](structhttp__hpack__header__buf.md#a48291a396efc761d85ffb5f46ddddf07) size\_t [value\_len](structhttp__hpack__header__buf.md#a48291a396efc761d85ffb5f46ddddf07);

120

[ 122](structhttp__hpack__header__buf.md#a6d1d09942d85f148e3979cf88f1cb87a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [buf](structhttp__hpack__header__buf.md#a6d1d09942d85f148e3979cf88f1cb87a)[HTTP\_SERVER\_HUFFMAN\_DECODE\_BUFFER\_SIZE];

123

[ 125](structhttp__hpack__header__buf.md#a9d1c7d2daaf55f201c03e7438b033abf) size\_t [datalen](structhttp__hpack__header__buf.md#a9d1c7d2daaf55f201c03e7438b033abf);

126};

127

129

130int http\_hpack\_huffman\_decode(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*encoded\_buf, size\_t encoded\_len,

131 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t buflen);

132int http\_hpack\_huffman\_encode(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*str, size\_t str\_len,

133 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t buflen);

134int http\_hpack\_decode\_header(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t datalen,

135 struct [http\_hpack\_header\_buf](structhttp__hpack__header__buf.md) \*header);

136int http\_hpack\_encode\_header([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t buflen,

137 struct [http\_hpack\_header\_buf](structhttp__hpack__header__buf.md) \*header);

138

140

141#ifdef \_\_cplusplus

142}

143#endif

144

148

149#endif

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[http\_hpack\_header\_buf](structhttp__hpack__header__buf.md)

HTTP2 header field with decoding buffer.

**Definition** hpack.h:108

[http\_hpack\_header\_buf::value\_len](structhttp__hpack__header__buf.md#a48291a396efc761d85ffb5f46ddddf07)

size\_t value\_len

Length of the decoded header field value.

**Definition** hpack.h:119

[http\_hpack\_header\_buf::buf](structhttp__hpack__header__buf.md#a6d1d09942d85f148e3979cf88f1cb87a)

uint8\_t buf[HTTP\_SERVER\_HUFFMAN\_DECODE\_BUFFER\_SIZE]

Encoding/Decoding buffer.

**Definition** hpack.h:122

[http\_hpack\_header\_buf::value](structhttp__hpack__header__buf.md#a957db215f89359b64a76e98e878e8c83)

const char \* value

A pointer to the decoded header field value.

**Definition** hpack.h:113

[http\_hpack\_header\_buf::datalen](structhttp__hpack__header__buf.md#a9d1c7d2daaf55f201c03e7438b033abf)

size\_t datalen

Length of the data in the decoding buffer.

**Definition** hpack.h:125

[http\_hpack\_header\_buf::name](structhttp__hpack__header__buf.md#ac0b781b733a16dc0c9e99753a4d2b25d)

const char \* name

A pointer to the decoded header field name.

**Definition** hpack.h:110

[http\_hpack\_header\_buf::name\_len](structhttp__hpack__header__buf.md#ad6079192782eec8e4a0c1d89018c6d7b)

size\_t name\_len

Length of the decoded header field name.

**Definition** hpack.h:116

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [http](dir_12a17b6e7ad2c8cb36f68b2ff871e607.md)
- [hpack.h](hpack_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

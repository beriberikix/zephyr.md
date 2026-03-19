---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/hpack_8h_source.html
original_path: doxygen/html/hpack_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

32

33enum http\_hpack\_static\_key {

34 HTTP\_SERVER\_HPACK\_INVALID = 0,

35 HTTP\_SERVER\_HPACK\_AUTHORITY = 1,

36 HTTP\_SERVER\_HPACK\_METHOD\_GET = 2,

37 HTTP\_SERVER\_HPACK\_METHOD\_POST = 3,

38 HTTP\_SERVER\_HPACK\_PATH\_ROOT = 4,

39 HTTP\_SERVER\_HPACK\_PATH\_INDEX = 5,

40 HTTP\_SERVER\_HPACK\_SCHEME\_HTTP = 6,

41 HTTP\_SERVER\_HPACK\_SCHEME\_HTTPS = 7,

42 HTTP\_SERVER\_HPACK\_STATUS\_200 = 8,

43 HTTP\_SERVER\_HPACK\_STATUS\_204 = 9,

44 HTTP\_SERVER\_HPACK\_STATUS\_206 = 10,

45 HTTP\_SERVER\_HPACK\_STATUS\_304 = 11,

46 HTTP\_SERVER\_HPACK\_STATUS\_400 = 12,

47 HTTP\_SERVER\_HPACK\_STATUS\_404 = 13,

48 HTTP\_SERVER\_HPACK\_STATUS\_500 = 14,

49 HTTP\_SERVER\_HPACK\_ACCEPT\_CHARSET = 15,

50 HTTP\_SERVER\_HPACK\_ACCEPT\_ENCODING = 16,

51 HTTP\_SERVER\_HPACK\_ACCEPT\_LANGUAGE = 17,

52 HTTP\_SERVER\_HPACK\_ACCEPT\_RANGES = 18,

53 HTTP\_SERVER\_HPACK\_ACCEPT = 19,

54 HTTP\_SERVER\_HPACK\_ACCESS\_CONTROL\_ALLOW\_ORIGIN = 20,

55 HTTP\_SERVER\_HPACK\_AGE = 21,

56 HTTP\_SERVER\_HPACK\_ALLOW = 22,

57 HTTP\_SERVER\_HPACK\_AUTHORIZATION = 23,

58 HTTP\_SERVER\_HPACK\_CACHE\_CONTROL = 24,

59 HTTP\_SERVER\_HPACK\_CONTENT\_DISPOSITION = 25,

60 HTTP\_SERVER\_HPACK\_CONTENT\_ENCODING = 26,

61 HTTP\_SERVER\_HPACK\_CONTENT\_LANGUAGE = 27,

62 HTTP\_SERVER\_HPACK\_CONTENT\_LENGTH = 28,

63 HTTP\_SERVER\_HPACK\_CONTENT\_LOCATION = 29,

64 HTTP\_SERVER\_HPACK\_CONTENT\_RANGE = 30,

65 HTTP\_SERVER\_HPACK\_CONTENT\_TYPE = 31,

66 HTTP\_SERVER\_HPACK\_COOKIE = 32,

67 HTTP\_SERVER\_HPACK\_DATE = 33,

68 HTTP\_SERVER\_HPACK\_ETAG = 34,

69 HTTP\_SERVER\_HPACK\_EXPECT = 35,

70 HTTP\_SERVER\_HPACK\_EXPIRES = 36,

71 HTTP\_SERVER\_HPACK\_FROM = 37,

72 HTTP\_SERVER\_HPACK\_HOST = 38,

73 HTTP\_SERVER\_HPACK\_IF\_MATCH = 39,

74 HTTP\_SERVER\_HPACK\_IF\_MODIFIED\_SINCE = 40,

75 HTTP\_SERVER\_HPACK\_IF\_NONE\_MATCH = 41,

76 HTTP\_SERVER\_HPACK\_IF\_RANGE = 42,

77 HTTP\_SERVER\_HPACK\_IF\_UNMODIFIED\_SINCE = 43,

78 HTTP\_SERVER\_HPACK\_LAST\_MODIFIED = 44,

79 HTTP\_SERVER\_HPACK\_LINK = 45,

80 HTTP\_SERVER\_HPACK\_LOCATION = 46,

81 HTTP\_SERVER\_HPACK\_MAX\_FORWARDS = 47,

82 HTTP\_SERVER\_HPACK\_PROXY\_AUTHENTICATE = 48,

83 HTTP\_SERVER\_HPACK\_PROXY\_AUTHORIZATION = 49,

84 HTTP\_SERVER\_HPACK\_RANGE = 50,

85 HTTP\_SERVER\_HPACK\_REFERER = 51,

86 HTTP\_SERVER\_HPACK\_REFRESH = 52,

87 HTTP\_SERVER\_HPACK\_RETRY\_AFTER = 53,

88 HTTP\_SERVER\_HPACK\_SERVER = 54,

89 HTTP\_SERVER\_HPACK\_SET\_COOKIE = 55,

90 HTTP\_SERVER\_HPACK\_STRICT\_TRANSPORT\_SECURITY = 56,

91 HTTP\_SERVER\_HPACK\_TRANSFER\_ENCODING = 57,

92 HTTP\_SERVER\_HPACK\_USER\_AGENT = 58,

93 HTTP\_SERVER\_HPACK\_VARY = 59,

94 HTTP\_SERVER\_HPACK\_VIA = 60,

95 HTTP\_SERVER\_HPACK\_WWW\_AUTHENTICATE = 61,

96};

97

98/\* TODO Kconfig \*/

99#define HTTP2\_HEADER\_FIELD\_MAX\_LEN 256

100

101#if defined(CONFIG\_HTTP\_SERVER)

102#define HTTP\_SERVER\_HUFFMAN\_DECODE\_BUFFER\_SIZE CONFIG\_HTTP\_SERVER\_HUFFMAN\_DECODE\_BUFFER\_SIZE

103#else

104#define HTTP\_SERVER\_HUFFMAN\_DECODE\_BUFFER\_SIZE 0

105#endif

106

108

[ 110](structhttp__hpack__header__buf.md)struct [http\_hpack\_header\_buf](structhttp__hpack__header__buf.md) {

[ 112](structhttp__hpack__header__buf.md#ac0b781b733a16dc0c9e99753a4d2b25d) const char \*[name](structhttp__hpack__header__buf.md#ac0b781b733a16dc0c9e99753a4d2b25d);

113

[ 115](structhttp__hpack__header__buf.md#a957db215f89359b64a76e98e878e8c83) const char \*[value](structhttp__hpack__header__buf.md#a957db215f89359b64a76e98e878e8c83);

116

[ 118](structhttp__hpack__header__buf.md#ad6079192782eec8e4a0c1d89018c6d7b) size\_t [name\_len](structhttp__hpack__header__buf.md#ad6079192782eec8e4a0c1d89018c6d7b);

119

[ 121](structhttp__hpack__header__buf.md#a48291a396efc761d85ffb5f46ddddf07) size\_t [value\_len](structhttp__hpack__header__buf.md#a48291a396efc761d85ffb5f46ddddf07);

122

[ 124](structhttp__hpack__header__buf.md#a6d1d09942d85f148e3979cf88f1cb87a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [buf](structhttp__hpack__header__buf.md#a6d1d09942d85f148e3979cf88f1cb87a)[HTTP\_SERVER\_HUFFMAN\_DECODE\_BUFFER\_SIZE];

125

[ 127](structhttp__hpack__header__buf.md#a9d1c7d2daaf55f201c03e7438b033abf) size\_t [datalen](structhttp__hpack__header__buf.md#a9d1c7d2daaf55f201c03e7438b033abf);

128};

129

131

132int http\_hpack\_huffman\_decode(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*encoded\_buf, size\_t encoded\_len,

133 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t buflen);

134int http\_hpack\_huffman\_encode(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*str, size\_t str\_len,

135 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t buflen);

136int http\_hpack\_decode\_header(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t datalen,

137 struct [http\_hpack\_header\_buf](structhttp__hpack__header__buf.md) \*header);

138int http\_hpack\_encode\_header([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t buflen,

139 struct [http\_hpack\_header\_buf](structhttp__hpack__header__buf.md) \*header);

140

142

143#ifdef \_\_cplusplus

144}

145#endif

146

150

151#endif

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[http\_hpack\_header\_buf](structhttp__hpack__header__buf.md)

HTTP2 header field with decoding buffer.

**Definition** hpack.h:110

[http\_hpack\_header\_buf::value\_len](structhttp__hpack__header__buf.md#a48291a396efc761d85ffb5f46ddddf07)

size\_t value\_len

Length of the decoded header field value.

**Definition** hpack.h:121

[http\_hpack\_header\_buf::buf](structhttp__hpack__header__buf.md#a6d1d09942d85f148e3979cf88f1cb87a)

uint8\_t buf[HTTP\_SERVER\_HUFFMAN\_DECODE\_BUFFER\_SIZE]

Encoding/Decoding buffer.

**Definition** hpack.h:124

[http\_hpack\_header\_buf::value](structhttp__hpack__header__buf.md#a957db215f89359b64a76e98e878e8c83)

const char \* value

A pointer to the decoded header field value.

**Definition** hpack.h:115

[http\_hpack\_header\_buf::datalen](structhttp__hpack__header__buf.md#a9d1c7d2daaf55f201c03e7438b033abf)

size\_t datalen

Length of the data in the decoding buffer.

**Definition** hpack.h:127

[http\_hpack\_header\_buf::name](structhttp__hpack__header__buf.md#ac0b781b733a16dc0c9e99753a4d2b25d)

const char \* name

A pointer to the decoded header field name.

**Definition** hpack.h:112

[http\_hpack\_header\_buf::name\_len](structhttp__hpack__header__buf.md#ad6079192782eec8e4a0c1d89018c6d7b)

size\_t name\_len

Length of the decoded header field name.

**Definition** hpack.h:118

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [http](dir_12a17b6e7ad2c8cb36f68b2ff871e607.md)
- [hpack.h](hpack_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

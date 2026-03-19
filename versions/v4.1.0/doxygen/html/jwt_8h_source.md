---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/jwt_8h_source.html
original_path: doxygen/html/jwt_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

jwt.h

[Go to the documentation of this file.](jwt_8h.md)

1/\*

2 \* Copyright (c) 2018 Linaro Ltd

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DATA\_JWT\_H\_

8#define ZEPHYR\_INCLUDE\_DATA\_JWT\_H\_

9

10#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

11#include <[stdbool.h](stdbool_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

23

[ 32](structjwt__builder.md)struct [jwt\_builder](structjwt__builder.md) {

[ 34](structjwt__builder.md#a23a0aa512e5bc66722b6d7a8cf20aa95) char \*[base](structjwt__builder.md#a23a0aa512e5bc66722b6d7a8cf20aa95);

35

[ 38](structjwt__builder.md#a74a3d3e645f8b438bcdf12abdf0aabf7) char \*[buf](structjwt__builder.md#a74a3d3e645f8b438bcdf12abdf0aabf7);

39

[ 41](structjwt__builder.md#a8fcc85d6704b63cd773397a5a4d9774d) size\_t [len](structjwt__builder.md#a8fcc85d6704b63cd773397a5a4d9774d);

42

[ 47](structjwt__builder.md#af53cb40609f623b95ff68d3c66a387ce) bool [overflowed](structjwt__builder.md#af53cb40609f623b95ff68d3c66a387ce);

48

49 /\* Pending bytes yet to be converted to base64. \*/

[ 50](structjwt__builder.md#a4bd0376eef7f162e9e9e1e1399388fed) unsigned char [wip](structjwt__builder.md#a4bd0376eef7f162e9e9e1e1399388fed)[3];

51

52 /\* Number of pending bytes. \*/

[ 53](structjwt__builder.md#a7e4880c8fc8136083bad0ef2559c67e4) int [pending](structjwt__builder.md#a7e4880c8fc8136083bad0ef2559c67e4);

54};

55

[ 70](group__jwt.md#gab10ee40ee3c0b3eea98051c2acbb8a75)int [jwt\_init\_builder](group__jwt.md#gab10ee40ee3c0b3eea98051c2acbb8a75)(struct [jwt\_builder](structjwt__builder.md) \*builder,

71 char \*buffer,

72 size\_t buffer\_size);

73

[ 92](group__jwt.md#ga209dc2bdbaf72b4c9d11be02e0ffe479)int [jwt\_add\_payload](group__jwt.md#ga209dc2bdbaf72b4c9d11be02e0ffe479)(struct [jwt\_builder](structjwt__builder.md) \*builder,

93 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) exp,

94 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) iat,

95 const char \*aud);

96

[ 109](group__jwt.md#gaa000189c83e9b9113f401cd7d523cefe)int [jwt\_sign](group__jwt.md#gaa000189c83e9b9113f401cd7d523cefe)(struct [jwt\_builder](structjwt__builder.md) \*builder,

110 const char \*der\_key,

111 size\_t der\_key\_len);

112

113#ifdef \_\_cplusplus

114}

115#endif

116

120

121#endif /\* ZEPHYR\_INCLUDE\_DATA\_JWT\_H\_ \*/

[jwt\_add\_payload](group__jwt.md#ga209dc2bdbaf72b4c9d11be02e0ffe479)

int jwt\_add\_payload(struct jwt\_builder \*builder, int32\_t exp, int32\_t iat, const char \*aud)

Add JWT payload.

[jwt\_sign](group__jwt.md#gaa000189c83e9b9113f401cd7d523cefe)

int jwt\_sign(struct jwt\_builder \*builder, const char \*der\_key, size\_t der\_key\_len)

Sign the JWT.

[jwt\_init\_builder](group__jwt.md#gab10ee40ee3c0b3eea98051c2acbb8a75)

int jwt\_init\_builder(struct jwt\_builder \*builder, char \*buffer, size\_t buffer\_size)

Initialize the JWT builder.

[types.h](include_2zephyr_2types_8h.md)

[stdbool.h](stdbool_8h.md)

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[jwt\_builder](structjwt__builder.md)

JWT data tracking.

**Definition** jwt.h:32

[jwt\_builder::base](structjwt__builder.md#a23a0aa512e5bc66722b6d7a8cf20aa95)

char \* base

The base of the buffer we are writing to.

**Definition** jwt.h:34

[jwt\_builder::wip](structjwt__builder.md#a4bd0376eef7f162e9e9e1e1399388fed)

unsigned char wip[3]

**Definition** jwt.h:50

[jwt\_builder::buf](structjwt__builder.md#a74a3d3e645f8b438bcdf12abdf0aabf7)

char \* buf

The place in this buffer where we are currently writing.

**Definition** jwt.h:38

[jwt\_builder::pending](structjwt__builder.md#a7e4880c8fc8136083bad0ef2559c67e4)

int pending

**Definition** jwt.h:53

[jwt\_builder::len](structjwt__builder.md#a8fcc85d6704b63cd773397a5a4d9774d)

size\_t len

The remaining free space in buf.

**Definition** jwt.h:41

[jwt\_builder::overflowed](structjwt__builder.md#af53cb40609f623b95ff68d3c66a387ce)

bool overflowed

Flag that is set if we try to write past the end of the buffer.

**Definition** jwt.h:47

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [data](dir_f6906818b29bc0a2a087f651f21ae7e0.md)
- [jwt.h](jwt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

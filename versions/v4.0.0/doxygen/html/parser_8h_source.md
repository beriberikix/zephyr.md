---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/parser_8h_source.html
original_path: doxygen/html/parser_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

parser.h

[Go to the documentation of this file.](parser_8h.md)

1/\* SPDX-License-Identifier: MIT \*/

2

3/\* Copyright Joyent, Inc. and other Node contributors. All rights reserved.

4 \*

5 \* Permission is hereby granted, free of charge, to any person obtaining a copy

6 \* of this software and associated documentation files (the "Software"), to

7 \* deal in the Software without restriction, including without limitation the

8 \* rights to use, copy, modify, merge, publish, distribute, sublicense, and/or

9 \* sell copies of the Software, and to permit persons to whom the Software is

10 \* furnished to do so, subject to the following conditions:

11 \*

12 \* The above copyright notice and this permission notice shall be included in

13 \* all copies or substantial portions of the Software.

14 \*

15 \* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR

16 \* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,

17 \* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE

18 \* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER

19 \* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING

20 \* FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS

21 \* IN THE SOFTWARE.

22 \*/

23#ifndef ZEPHYR\_INCLUDE\_NET\_HTTP\_PARSER\_H\_

24#define ZEPHYR\_INCLUDE\_NET\_HTTP\_PARSER\_H\_

25

26/\* Also update SONAME in the Makefile whenever you change these. \*/

[ 27](parser_8h.md#abfeef6f3e39791acc311791feda09d27)#define HTTP\_PARSER\_VERSION\_MAJOR 2

[ 28](parser_8h.md#ab8479153443ca4fe95b3de5adb0224de)#define HTTP\_PARSER\_VERSION\_MINOR 7

[ 29](parser_8h.md#afb999672cce2ebd7f952bd3f28d8f5e5)#define HTTP\_PARSER\_VERSION\_PATCH 1

30

31#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

32#if defined(\_WIN32) && !defined(\_\_MINGW32\_\_) && \

33 (!defined(\_MSC\_VER) || \_MSC\_VER < 1600) && !defined(\_\_WINE\_\_)

34#include <BaseTsd.h>

35#include <stddef.h>

36typedef \_\_int8 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6);

37typedef unsigned \_\_int8 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d);

38typedef \_\_int16 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf);

39typedef unsigned \_\_int16 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e);

40typedef \_\_int32 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2);

41typedef unsigned \_\_int32 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f);

42typedef \_\_int64 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b);

43typedef unsigned \_\_int64 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1);

44#else

45#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

46#include <stddef.h>

47#endif

48#include <[zephyr/net/http/method.h](method_8h.md)>

49#include <[zephyr/net/http/parser\_state.h](parser__state_8h.md)>

50#include <[zephyr/net/http/parser\_url.h](parser__url_8h.md)>

51

52#ifdef \_\_cplusplus

53extern "C" {

54#endif

55

56/\* Maximum header size allowed. If the macro is not defined

57 \* before including this header then the default is used. To

58 \* change the maximum header size, define the macro in the build

59 \* environment (e.g. -DHTTP\_MAX\_HEADER\_SIZE=<value>). To remove

60 \* the effective limit on the size of the header, define the macro

61 \* to a very large number (e.g. -DHTTP\_MAX\_HEADER\_SIZE=0x7fffffff)

62 \*/

63#ifndef HTTP\_MAX\_HEADER\_SIZE

[ 64](parser_8h.md#a6272a7f92e0f1b66e07680f32f6f21b6)# define HTTP\_MAX\_HEADER\_SIZE (80 \* 1024)

65#endif

66

67struct [http\_parser](structhttp__parser.md);

68struct [http\_parser\_settings](structhttp__parser__settings.md);

69

70

71/\* Callbacks should return non-zero to indicate an error. The parser will

72 \* then halt execution.

73 \*

74 \* The one exception is on\_headers\_complete. In a HTTP\_RESPONSE parser

75 \* returning '1' from on\_headers\_complete will tell the parser that it

76 \* should not expect a body. This is used when receiving a response to a

77 \* HEAD request which may contain 'Content-Length' or 'Transfer-Encoding:

78 \* chunked' headers that indicate the presence of a body.

79 \*

80 \* Returning `2` from on\_headers\_complete will tell parser that it should not

81 \* expect neither a body nor any further responses on this connection. This is

82 \* useful for handling responses to a CONNECT request which may not contain

83 \* `Upgrade` or `Connection: upgrade` headers.

84 \*

85 \* http\_data\_cb does not return data chunks. It will be called arbitrarily

86 \* many times for each string. E.G. you might get 10 callbacks for "on\_url"

87 \* each providing just a few characters more data.

88 \*/

[ 89](parser_8h.md#a1aab76595c275d0615cbea1cee1807c8)typedef int (\*[http\_data\_cb](parser_8h.md#a1aab76595c275d0615cbea1cee1807c8))(struct [http\_parser](structhttp__parser.md) \*, const char \*at,

90 size\_t length);

[ 91](parser_8h.md#aa0f8424a6e7d3dd0b2f3b6358b57f1a1)typedef int (\*[http\_cb](parser_8h.md#aa0f8424a6e7d3dd0b2f3b6358b57f1a1))(struct [http\_parser](structhttp__parser.md) \*);

92

[ 93](parser_8h.md#af9d6d304f8c255158175951b434cfa7aadac18fbd072752213fd5308bb5fc8684)enum [http\_parser\_type](parser_8h.md#af9d6d304f8c255158175951b434cfa7a) { [HTTP\_REQUEST](parser_8h.md#af9d6d304f8c255158175951b434cfa7aa9f727b57e9e9c1651ee0df29aa1b1713), [HTTP\_RESPONSE](parser_8h.md#af9d6d304f8c255158175951b434cfa7aa132597b93208763e8e81c4a4a0e8a642), [HTTP\_BOTH](parser_8h.md#af9d6d304f8c255158175951b434cfa7aadac18fbd072752213fd5308bb5fc8684) };

94

95/\* Flag values for http\_parser.flags field \*/

[ 96](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)enum [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) {

[ 97](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9a092619f8f7babc8fc3fa7533e78c3c29) [F\_CHUNKED](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9a092619f8f7babc8fc3fa7533e78c3c29) = 1 << 0,

[ 98](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9a5c5e8921e5747d1128ad9611a6d4a782) [F\_CONNECTION\_KEEP\_ALIVE](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9a5c5e8921e5747d1128ad9611a6d4a782) = 1 << 1,

[ 99](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9a133e98dc07339e6c1605f32fc4fd6c78) [F\_CONNECTION\_CLOSE](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9a133e98dc07339e6c1605f32fc4fd6c78) = 1 << 2,

[ 100](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9af0eea4f6920c6ff5c68cdd1f2e27d044) [F\_CONNECTION\_UPGRADE](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9af0eea4f6920c6ff5c68cdd1f2e27d044) = 1 << 3,

[ 101](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9aa75b5b1dcec2decaa7386264d4e1dc29) [F\_TRAILING](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9aa75b5b1dcec2decaa7386264d4e1dc29) = 1 << 4,

[ 102](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9a600ff486c803dcf2ec13453bdaf1100c) [F\_UPGRADE](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9a600ff486c803dcf2ec13453bdaf1100c) = 1 << 5,

[ 103](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9ae71592851a69f477b80b1947399c1740) [F\_SKIPBODY](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9ae71592851a69f477b80b1947399c1740) = 1 << 6,

[ 104](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9a9b2f205685c9ce94d3d73148de48decb) [F\_CONTENTLENGTH](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9a9b2f205685c9ce94d3d73148de48decb) = 1 << 7

105};

106

[ 107](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64)enum [http\_errno](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64) {

[ 108](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64adf532f653497f3085108a5e1f097aa8e) [HPE\_OK](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64adf532f653497f3085108a5e1f097aa8e),

[ 109](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a5b44995fcd173cf38a88fc3ceaf0cb41) [HPE\_CB\_message\_begin](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a5b44995fcd173cf38a88fc3ceaf0cb41),

[ 110](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64ae15b73f73f8aad8c5e39d03b29414f9b) [HPE\_CB\_url](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64ae15b73f73f8aad8c5e39d03b29414f9b),

[ 111](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64ade6f685cd47ad03c836aeee97efff1ed) [HPE\_CB\_header\_field](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64ade6f685cd47ad03c836aeee97efff1ed),

[ 112](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64aceed4040be7acf32b6bceb3aace8405e) [HPE\_CB\_header\_value](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64aceed4040be7acf32b6bceb3aace8405e),

[ 113](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a5d82bb467f93eed296d892408c44816a) [HPE\_CB\_headers\_complete](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a5d82bb467f93eed296d892408c44816a),

[ 114](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a5dc4b0888f48cd87fc3ded374ffac8a2) [HPE\_CB\_body](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a5dc4b0888f48cd87fc3ded374ffac8a2),

[ 115](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64ae0f56ef0ecc6638fb0594d130a1ee490) [HPE\_CB\_message\_complete](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64ae0f56ef0ecc6638fb0594d130a1ee490),

[ 116](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a9adad03852eddb1f361abe9d856a1a0f) [HPE\_CB\_status](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a9adad03852eddb1f361abe9d856a1a0f),

[ 117](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a69ccadce5be8074b104b19aa74dce556) [HPE\_CB\_chunk\_header](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a69ccadce5be8074b104b19aa74dce556),

[ 118](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a008e232118d6133c4dbdd9770d926694) [HPE\_CB\_chunk\_complete](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a008e232118d6133c4dbdd9770d926694),

[ 119](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a4103809c185fee62b11c188ff0eab39a) [HPE\_INVALID\_EOF\_STATE](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a4103809c185fee62b11c188ff0eab39a),

[ 120](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a5270cdc2f8af1802ccf3a2f33fde9307) [HPE\_HEADER\_OVERFLOW](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a5270cdc2f8af1802ccf3a2f33fde9307),

[ 121](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a7fbc6a25f20237b1cc795db489312e8e) [HPE\_CLOSED\_CONNECTION](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a7fbc6a25f20237b1cc795db489312e8e),

[ 122](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a5a1b7ae13c36ef37fd52b2b68112b501) [HPE\_INVALID\_VERSION](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a5a1b7ae13c36ef37fd52b2b68112b501),

[ 123](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64aa4a2007f1dc03bf22aff5ca8885f6b59) [HPE\_INVALID\_STATUS](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64aa4a2007f1dc03bf22aff5ca8885f6b59),

[ 124](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64ac031cfd48285e22ddec18964f6281f6e) [HPE\_INVALID\_METHOD](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64ac031cfd48285e22ddec18964f6281f6e),

[ 125](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64ad92573bf62e7b0a13d398926a984fa9d) [HPE\_INVALID\_URL](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64ad92573bf62e7b0a13d398926a984fa9d),

[ 126](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a6391e880280eda55707145bda1170294) [HPE\_INVALID\_HOST](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a6391e880280eda55707145bda1170294),

[ 127](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a3e7c3b8a95f34bbd40ea047fcd43ffa5) [HPE\_INVALID\_PORT](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a3e7c3b8a95f34bbd40ea047fcd43ffa5),

[ 128](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a69e17a8b5a35b9f93ea914224c2d4f2a) [HPE\_INVALID\_PATH](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a69e17a8b5a35b9f93ea914224c2d4f2a),

[ 129](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a383ef24f0ac59de1c128ca776d813865) [HPE\_INVALID\_QUERY\_STRING](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a383ef24f0ac59de1c128ca776d813865),

[ 130](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64afa80e3a0c0dd1c93cf0a11cacbd59079) [HPE\_INVALID\_FRAGMENT](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64afa80e3a0c0dd1c93cf0a11cacbd59079),

[ 131](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64af9f23325bd502239af0326a0b407b41d) [HPE\_LF\_EXPECTED](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64af9f23325bd502239af0326a0b407b41d),

[ 132](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64ac0348f1ca04bf4d882affcd0249336b5) [HPE\_INVALID\_HEADER\_TOKEN](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64ac0348f1ca04bf4d882affcd0249336b5),

[ 133](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a18b873c41a1d7aa9ee9486f719aa7509) [HPE\_INVALID\_CONTENT\_LENGTH](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a18b873c41a1d7aa9ee9486f719aa7509),

[ 134](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a2406df24d500b1228fc5ef4a8d60e7c3) [HPE\_UNEXPECTED\_CONTENT\_LENGTH](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a2406df24d500b1228fc5ef4a8d60e7c3),

[ 135](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a36842cc306c491da8c42023be68585e9) [HPE\_INVALID\_CHUNK\_SIZE](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a36842cc306c491da8c42023be68585e9),

[ 136](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a1b9ec4aeef6f168f9d711c27a0c6faa8) [HPE\_INVALID\_CONSTANT](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a1b9ec4aeef6f168f9d711c27a0c6faa8),

[ 137](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64abb98b653c0972e3e22bc5ff8b57d0d55) [HPE\_INVALID\_INTERNAL\_STATE](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64abb98b653c0972e3e22bc5ff8b57d0d55),

[ 138](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a7f92de0f01b2d0e37209854069183f16) [HPE\_STRICT](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a7f92de0f01b2d0e37209854069183f16),

[ 139](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64aed64f2a65634183e8f708ac80af3f6f2) [HPE\_PAUSED](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64aed64f2a65634183e8f708ac80af3f6f2),

[ 140](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a36cb81d8c40b00602b558f82a38eaecc) [HPE\_UNKNOWN](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a36cb81d8c40b00602b558f82a38eaecc)

141};

142

143/\* Get an http\_errno value from an http\_parser \*/

[ 144](parser_8h.md#a356ebaa93536e6f94c2948a1416697c7)#define HTTP\_PARSER\_ERRNO(p) ((enum http\_errno) (p)->http\_errno)

145

146

[ 147](structhttp__parser.md)struct [http\_parser](structhttp__parser.md) {

[ 149](structhttp__parser.md#ac6c327558547d55eb64a8aea1310cc2e) unsigned int [type](structhttp__parser.md#ac6c327558547d55eb64a8aea1310cc2e) : 2; /\* enum http\_parser\_type \*/

[ 150](structhttp__parser.md#a5e54708e0cb3f9ced19bd829dcdeaf53) unsigned int [flags](structhttp__parser.md#a5e54708e0cb3f9ced19bd829dcdeaf53) : 8; /\* F\_xxx values from 'flags' enum;

151 \* semi-public

152 \*/

[ 153](structhttp__parser.md#a6f5952e0b47c83aeacf64fc287fd8003) unsigned int [state](structhttp__parser.md#a6f5952e0b47c83aeacf64fc287fd8003) : 7; /\* enum state from http\_parser.c \*/

[ 154](structhttp__parser.md#ac5b254b99c6472ca19ae1f426758ce75) unsigned int [header\_state](structhttp__parser.md#ac5b254b99c6472ca19ae1f426758ce75) : 7; /\* enum header\_state from http\_parser.c

155 \*/

[ 156](structhttp__parser.md#a6f7ba706f975f447b3bf72be97facdf8) unsigned int [index](structhttp__parser.md#a6f7ba706f975f447b3bf72be97facdf8) : 7; /\* index into current matcher \*/

[ 157](structhttp__parser.md#acd80a931fcc87d41999397af1662fc3c) unsigned int [lenient\_http\_headers](structhttp__parser.md#acd80a931fcc87d41999397af1662fc3c) : 1;

158

[ 159](structhttp__parser.md#a78085ca896bb3b9aa1ecb0f6fddc039d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [nread](structhttp__parser.md#a78085ca896bb3b9aa1ecb0f6fddc039d); /\* # bytes read in various scenarios \*/

[ 160](structhttp__parser.md#a7fd5a194802b1206bb773e096d291f29) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [content\_length](structhttp__parser.md#a7fd5a194802b1206bb773e096d291f29); /\* # bytes in body (0 if no Content-Length

161 \* header)

162 \*/

[ 164](structhttp__parser.md#ac994a4a8268652f5ce82de5bde5c3f9d) unsigned short [http\_major](structhttp__parser.md#ac994a4a8268652f5ce82de5bde5c3f9d);

[ 165](structhttp__parser.md#ae8af6433c824f5348773842db62ad4ab) unsigned short [http\_minor](structhttp__parser.md#ae8af6433c824f5348773842db62ad4ab);

[ 166](structhttp__parser.md#a82f5aed92ca3566489def7bc384bab26) unsigned int [status\_code](structhttp__parser.md#a82f5aed92ca3566489def7bc384bab26) : 16; /\* responses only \*/

[ 167](structhttp__parser.md#a7955de339fafd81ad54380845913457d) unsigned int [method](structhttp__parser.md#a7955de339fafd81ad54380845913457d) : 8; /\* requests only \*/

[ 168](structhttp__parser.md#ab8638d65fa174bc1925d77e2533117fa) unsigned int [http\_errno](structhttp__parser.md#ab8638d65fa174bc1925d77e2533117fa) : 7;

169

170 /\* 1 = Upgrade header was present and the parser has exited because of

171 \* that.

172 \* 0 = No upgrade header present.

173 \* Should be checked when http\_parser\_execute() returns in addition to

174 \* error checking.

175 \*/

[ 176](structhttp__parser.md#a748f476eacc5ac56b84dd07dbafb42a4) unsigned int [upgrade](structhttp__parser.md#a748f476eacc5ac56b84dd07dbafb42a4) : 1;

177

[ 179](structhttp__parser.md#a7e87ce57b97f60f1fdb7039a8ecb0bca) void \*[data](structhttp__parser.md#a7e87ce57b97f60f1fdb7039a8ecb0bca); /\* A pointer to get hook to the "connection" or "socket"

180 \* object

181 \*/

182

183 /\* Remote socket address of http connection, where parser can initiate

184 \* replies if necessary.

185 \*/

[ 186](structhttp__parser.md#aecffbbbfebfc4f4a8cb4c034d18ef375) const struct [sockaddr](structsockaddr.md) \*[addr](structhttp__parser.md#aecffbbbfebfc4f4a8cb4c034d18ef375);

187};

188

189

[ 190](structhttp__parser__settings.md)struct [http\_parser\_settings](structhttp__parser__settings.md) {

[ 191](structhttp__parser__settings.md#ac44144daecc8e8adbd477b7e6a794e26) [http\_cb](parser_8h.md#aa0f8424a6e7d3dd0b2f3b6358b57f1a1) [on\_message\_begin](structhttp__parser__settings.md#ac44144daecc8e8adbd477b7e6a794e26);

[ 192](structhttp__parser__settings.md#a9c24dfa900b49bf3439bbfba572b42fb) [http\_data\_cb](parser_8h.md#a1aab76595c275d0615cbea1cee1807c8) [on\_url](structhttp__parser__settings.md#a9c24dfa900b49bf3439bbfba572b42fb);

[ 193](structhttp__parser__settings.md#a6d0f0203f3461a8889ad471de119c993) [http\_data\_cb](parser_8h.md#a1aab76595c275d0615cbea1cee1807c8) [on\_status](structhttp__parser__settings.md#a6d0f0203f3461a8889ad471de119c993);

[ 194](structhttp__parser__settings.md#acfb3fd7947c5ff3e16649c71aa13bff2) [http\_data\_cb](parser_8h.md#a1aab76595c275d0615cbea1cee1807c8) [on\_header\_field](structhttp__parser__settings.md#acfb3fd7947c5ff3e16649c71aa13bff2);

[ 195](structhttp__parser__settings.md#a2af4e9085fa79ee52b31e626179bc561) [http\_data\_cb](parser_8h.md#a1aab76595c275d0615cbea1cee1807c8) [on\_header\_value](structhttp__parser__settings.md#a2af4e9085fa79ee52b31e626179bc561);

[ 196](structhttp__parser__settings.md#a743b24c8f33e0f1cf60a96c824c42071) [http\_cb](parser_8h.md#aa0f8424a6e7d3dd0b2f3b6358b57f1a1) [on\_headers\_complete](structhttp__parser__settings.md#a743b24c8f33e0f1cf60a96c824c42071);

[ 197](structhttp__parser__settings.md#aaa145d7c24c91f471b2079ecb6368ae4) [http\_data\_cb](parser_8h.md#a1aab76595c275d0615cbea1cee1807c8) [on\_body](structhttp__parser__settings.md#aaa145d7c24c91f471b2079ecb6368ae4);

[ 198](structhttp__parser__settings.md#afdd5beef93a4a7b32bc61ae088da64d2) [http\_cb](parser_8h.md#aa0f8424a6e7d3dd0b2f3b6358b57f1a1) [on\_message\_complete](structhttp__parser__settings.md#afdd5beef93a4a7b32bc61ae088da64d2);

199 /\* When on\_chunk\_header is called, the current chunk length is stored

200 \* in parser->content\_length.

201 \*/

[ 202](structhttp__parser__settings.md#a497cf8f9d68e06e54684b71ee0f9f828) [http\_cb](parser_8h.md#aa0f8424a6e7d3dd0b2f3b6358b57f1a1) [on\_chunk\_header](structhttp__parser__settings.md#a497cf8f9d68e06e54684b71ee0f9f828);

[ 203](structhttp__parser__settings.md#ac1c8453573094795ef41d4ba26e78846) [http\_cb](parser_8h.md#aa0f8424a6e7d3dd0b2f3b6358b57f1a1) [on\_chunk\_complete](structhttp__parser__settings.md#ac1c8453573094795ef41d4ba26e78846);

204};

205

206

207/\* Returns the library version. Bits 16-23 contain the major version number,

208 \* bits 8-15 the minor version number and bits 0-7 the patch level.

209 \* Usage example:

210 \*

211 \* unsigned long version = http\_parser\_version();

212 \* unsigned major = (version >> 16) & 255;

213 \* unsigned minor = (version >> 8) & 255;

214 \* unsigned patch = version & 255;

215 \* printf("http\_parser v%u.%u.%u\n", major, minor, patch);

216 \*/

[ 217](parser_8h.md#a2559b4d373c7f0d85c77a2a3c308a5ee)unsigned long [http\_parser\_version](parser_8h.md#a2559b4d373c7f0d85c77a2a3c308a5ee)(void);

218

[ 219](parser_8h.md#ab8ae8e721c5c9f7309e94c174c72a940)void [http\_parser\_init](parser_8h.md#ab8ae8e721c5c9f7309e94c174c72a940)(struct [http\_parser](structhttp__parser.md) \*parser, enum [http\_parser\_type](parser_8h.md#af9d6d304f8c255158175951b434cfa7a) type);

220

221

222/\* Initialize http\_parser\_settings members to 0

223 \*/

[ 224](parser_8h.md#a76d2e1f7225617f6941042fc95d888fe)void [http\_parser\_settings\_init](parser_8h.md#a76d2e1f7225617f6941042fc95d888fe)(struct [http\_parser\_settings](structhttp__parser__settings.md) \*settings);

225

226

227/\* Executes the parser. Returns number of parsed bytes. Sets

228 \* `parser->http\_errno` on error.

229 \*/

230

[ 231](parser_8h.md#a54f1346f15b326f6308a3ff7f0f75b52)size\_t [http\_parser\_execute](parser_8h.md#a54f1346f15b326f6308a3ff7f0f75b52)(struct [http\_parser](structhttp__parser.md) \*parser,

232 const struct [http\_parser\_settings](structhttp__parser__settings.md) \*settings,

233 const char \*data, size\_t len);

234

235/\* If http\_should\_keep\_alive() in the on\_headers\_complete or

236 \* on\_message\_complete callback returns 0, then this should be

237 \* the last message on the connection.

238 \* If you are the server, respond with the "Connection: close" header.

239 \* If you are the client, close the connection.

240 \*/

[ 241](parser_8h.md#a903c39c3abea292860780856ba90d560)int [http\_should\_keep\_alive](parser_8h.md#a903c39c3abea292860780856ba90d560)(const struct [http\_parser](structhttp__parser.md) \*parser);

242

243/\* Returns a string version of the HTTP method. \*/

[ 244](parser_8h.md#abb207665b6ff41700e5bbb260b580cb6)const char \*[http\_method\_str](parser_8h.md#abb207665b6ff41700e5bbb260b580cb6)(enum [http\_method](group__http__methods.md#gaacd5f203e33ac338ca5cb8f02a3ff3b8) m);

245

246/\* Return a string name of the given error \*/

[ 247](parser_8h.md#acce1b9056442d75d4d609e797bcce2fd)const char \*[http\_errno\_name](parser_8h.md#acce1b9056442d75d4d609e797bcce2fd)(enum [http\_errno](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64) err);

248

249/\* Return a string description of the given error \*/

[ 250](parser_8h.md#a88adfab20d97366aac1fe05aa7dde7da)const char \*[http\_errno\_description](parser_8h.md#a88adfab20d97366aac1fe05aa7dde7da)(enum [http\_errno](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64) err);

251

252/\* Pause or un-pause the parser; a nonzero value pauses \*/

[ 253](parser_8h.md#aa3764343ba4d2bb13fe39b05425633ba)void [http\_parser\_pause](parser_8h.md#aa3764343ba4d2bb13fe39b05425633ba)(struct [http\_parser](structhttp__parser.md) \*parser, int paused);

254

255/\* Checks if this is the final chunk of the body. \*/

[ 256](parser_8h.md#a5156a631a251516a6e78b17e1faadbb2)int [http\_body\_is\_final](parser_8h.md#a5156a631a251516a6e78b17e1faadbb2)(const struct [http\_parser](structhttp__parser.md) \*parser);

257

258#ifdef \_\_cplusplus

259}

260#endif

261#endif

[http\_method](group__http__methods.md#gaacd5f203e33ac338ca5cb8f02a3ff3b8)

http\_method

HTTP Request Methods.

**Definition** method.h:28

[types.h](include_2zephyr_2types_8h.md)

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[method.h](method_8h.md)

HTTP request methods.

[http\_errno](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64)

http\_errno

**Definition** parser.h:107

[HPE\_CB\_chunk\_complete](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a008e232118d6133c4dbdd9770d926694)

@ HPE\_CB\_chunk\_complete

**Definition** parser.h:118

[HPE\_INVALID\_CONTENT\_LENGTH](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a18b873c41a1d7aa9ee9486f719aa7509)

@ HPE\_INVALID\_CONTENT\_LENGTH

**Definition** parser.h:133

[HPE\_INVALID\_CONSTANT](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a1b9ec4aeef6f168f9d711c27a0c6faa8)

@ HPE\_INVALID\_CONSTANT

**Definition** parser.h:136

[HPE\_UNEXPECTED\_CONTENT\_LENGTH](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a2406df24d500b1228fc5ef4a8d60e7c3)

@ HPE\_UNEXPECTED\_CONTENT\_LENGTH

**Definition** parser.h:134

[HPE\_INVALID\_CHUNK\_SIZE](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a36842cc306c491da8c42023be68585e9)

@ HPE\_INVALID\_CHUNK\_SIZE

**Definition** parser.h:135

[HPE\_UNKNOWN](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a36cb81d8c40b00602b558f82a38eaecc)

@ HPE\_UNKNOWN

**Definition** parser.h:140

[HPE\_INVALID\_QUERY\_STRING](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a383ef24f0ac59de1c128ca776d813865)

@ HPE\_INVALID\_QUERY\_STRING

**Definition** parser.h:129

[HPE\_INVALID\_PORT](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a3e7c3b8a95f34bbd40ea047fcd43ffa5)

@ HPE\_INVALID\_PORT

**Definition** parser.h:127

[HPE\_INVALID\_EOF\_STATE](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a4103809c185fee62b11c188ff0eab39a)

@ HPE\_INVALID\_EOF\_STATE

**Definition** parser.h:119

[HPE\_HEADER\_OVERFLOW](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a5270cdc2f8af1802ccf3a2f33fde9307)

@ HPE\_HEADER\_OVERFLOW

**Definition** parser.h:120

[HPE\_INVALID\_VERSION](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a5a1b7ae13c36ef37fd52b2b68112b501)

@ HPE\_INVALID\_VERSION

**Definition** parser.h:122

[HPE\_CB\_message\_begin](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a5b44995fcd173cf38a88fc3ceaf0cb41)

@ HPE\_CB\_message\_begin

**Definition** parser.h:109

[HPE\_CB\_headers\_complete](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a5d82bb467f93eed296d892408c44816a)

@ HPE\_CB\_headers\_complete

**Definition** parser.h:113

[HPE\_CB\_body](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a5dc4b0888f48cd87fc3ded374ffac8a2)

@ HPE\_CB\_body

**Definition** parser.h:114

[HPE\_INVALID\_HOST](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a6391e880280eda55707145bda1170294)

@ HPE\_INVALID\_HOST

**Definition** parser.h:126

[HPE\_CB\_chunk\_header](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a69ccadce5be8074b104b19aa74dce556)

@ HPE\_CB\_chunk\_header

**Definition** parser.h:117

[HPE\_INVALID\_PATH](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a69e17a8b5a35b9f93ea914224c2d4f2a)

@ HPE\_INVALID\_PATH

**Definition** parser.h:128

[HPE\_STRICT](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a7f92de0f01b2d0e37209854069183f16)

@ HPE\_STRICT

**Definition** parser.h:138

[HPE\_CLOSED\_CONNECTION](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a7fbc6a25f20237b1cc795db489312e8e)

@ HPE\_CLOSED\_CONNECTION

**Definition** parser.h:121

[HPE\_CB\_status](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64a9adad03852eddb1f361abe9d856a1a0f)

@ HPE\_CB\_status

**Definition** parser.h:116

[HPE\_INVALID\_STATUS](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64aa4a2007f1dc03bf22aff5ca8885f6b59)

@ HPE\_INVALID\_STATUS

**Definition** parser.h:123

[HPE\_INVALID\_INTERNAL\_STATE](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64abb98b653c0972e3e22bc5ff8b57d0d55)

@ HPE\_INVALID\_INTERNAL\_STATE

**Definition** parser.h:137

[HPE\_INVALID\_METHOD](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64ac031cfd48285e22ddec18964f6281f6e)

@ HPE\_INVALID\_METHOD

**Definition** parser.h:124

[HPE\_INVALID\_HEADER\_TOKEN](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64ac0348f1ca04bf4d882affcd0249336b5)

@ HPE\_INVALID\_HEADER\_TOKEN

**Definition** parser.h:132

[HPE\_CB\_header\_value](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64aceed4040be7acf32b6bceb3aace8405e)

@ HPE\_CB\_header\_value

**Definition** parser.h:112

[HPE\_INVALID\_URL](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64ad92573bf62e7b0a13d398926a984fa9d)

@ HPE\_INVALID\_URL

**Definition** parser.h:125

[HPE\_CB\_header\_field](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64ade6f685cd47ad03c836aeee97efff1ed)

@ HPE\_CB\_header\_field

**Definition** parser.h:111

[HPE\_OK](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64adf532f653497f3085108a5e1f097aa8e)

@ HPE\_OK

**Definition** parser.h:108

[HPE\_CB\_message\_complete](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64ae0f56ef0ecc6638fb0594d130a1ee490)

@ HPE\_CB\_message\_complete

**Definition** parser.h:115

[HPE\_CB\_url](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64ae15b73f73f8aad8c5e39d03b29414f9b)

@ HPE\_CB\_url

**Definition** parser.h:110

[HPE\_PAUSED](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64aed64f2a65634183e8f708ac80af3f6f2)

@ HPE\_PAUSED

**Definition** parser.h:139

[HPE\_LF\_EXPECTED](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64af9f23325bd502239af0326a0b407b41d)

@ HPE\_LF\_EXPECTED

**Definition** parser.h:131

[HPE\_INVALID\_FRAGMENT](parser_8h.md#a14687aec2341ce0e62db2e543dd1da64afa80e3a0c0dd1c93cf0a11cacbd59079)

@ HPE\_INVALID\_FRAGMENT

**Definition** parser.h:130

[http\_data\_cb](parser_8h.md#a1aab76595c275d0615cbea1cee1807c8)

int(\* http\_data\_cb)(struct http\_parser \*, const char \*at, size\_t length)

**Definition** parser.h:89

[http\_parser\_version](parser_8h.md#a2559b4d373c7f0d85c77a2a3c308a5ee)

unsigned long http\_parser\_version(void)

[http\_body\_is\_final](parser_8h.md#a5156a631a251516a6e78b17e1faadbb2)

int http\_body\_is\_final(const struct http\_parser \*parser)

[http\_parser\_execute](parser_8h.md#a54f1346f15b326f6308a3ff7f0f75b52)

size\_t http\_parser\_execute(struct http\_parser \*parser, const struct http\_parser\_settings \*settings, const char \*data, size\_t len)

[http\_parser\_settings\_init](parser_8h.md#a76d2e1f7225617f6941042fc95d888fe)

void http\_parser\_settings\_init(struct http\_parser\_settings \*settings)

[http\_errno\_description](parser_8h.md#a88adfab20d97366aac1fe05aa7dde7da)

const char \* http\_errno\_description(enum http\_errno err)

[http\_should\_keep\_alive](parser_8h.md#a903c39c3abea292860780856ba90d560)

int http\_should\_keep\_alive(const struct http\_parser \*parser)

[http\_cb](parser_8h.md#aa0f8424a6e7d3dd0b2f3b6358b57f1a1)

int(\* http\_cb)(struct http\_parser \*)

**Definition** parser.h:91

[http\_parser\_pause](parser_8h.md#aa3764343ba4d2bb13fe39b05425633ba)

void http\_parser\_pause(struct http\_parser \*parser, int paused)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[F\_CHUNKED](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9a092619f8f7babc8fc3fa7533e78c3c29)

@ F\_CHUNKED

**Definition** parser.h:97

[F\_CONNECTION\_CLOSE](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9a133e98dc07339e6c1605f32fc4fd6c78)

@ F\_CONNECTION\_CLOSE

**Definition** parser.h:99

[F\_CONNECTION\_KEEP\_ALIVE](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9a5c5e8921e5747d1128ad9611a6d4a782)

@ F\_CONNECTION\_KEEP\_ALIVE

**Definition** parser.h:98

[F\_UPGRADE](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9a600ff486c803dcf2ec13453bdaf1100c)

@ F\_UPGRADE

**Definition** parser.h:102

[F\_CONTENTLENGTH](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9a9b2f205685c9ce94d3d73148de48decb)

@ F\_CONTENTLENGTH

**Definition** parser.h:104

[F\_TRAILING](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9aa75b5b1dcec2decaa7386264d4e1dc29)

@ F\_TRAILING

**Definition** parser.h:101

[F\_SKIPBODY](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9ae71592851a69f477b80b1947399c1740)

@ F\_SKIPBODY

**Definition** parser.h:103

[F\_CONNECTION\_UPGRADE](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9af0eea4f6920c6ff5c68cdd1f2e27d044)

@ F\_CONNECTION\_UPGRADE

**Definition** parser.h:100

[http\_parser\_init](parser_8h.md#ab8ae8e721c5c9f7309e94c174c72a940)

void http\_parser\_init(struct http\_parser \*parser, enum http\_parser\_type type)

[http\_method\_str](parser_8h.md#abb207665b6ff41700e5bbb260b580cb6)

const char \* http\_method\_str(enum http\_method m)

[http\_errno\_name](parser_8h.md#acce1b9056442d75d4d609e797bcce2fd)

const char \* http\_errno\_name(enum http\_errno err)

[http\_parser\_type](parser_8h.md#af9d6d304f8c255158175951b434cfa7a)

http\_parser\_type

**Definition** parser.h:93

[HTTP\_RESPONSE](parser_8h.md#af9d6d304f8c255158175951b434cfa7aa132597b93208763e8e81c4a4a0e8a642)

@ HTTP\_RESPONSE

**Definition** parser.h:93

[HTTP\_REQUEST](parser_8h.md#af9d6d304f8c255158175951b434cfa7aa9f727b57e9e9c1651ee0df29aa1b1713)

@ HTTP\_REQUEST

**Definition** parser.h:93

[HTTP\_BOTH](parser_8h.md#af9d6d304f8c255158175951b434cfa7aadac18fbd072752213fd5308bb5fc8684)

@ HTTP\_BOTH

**Definition** parser.h:93

[parser\_state.h](parser__state_8h.md)

[parser\_url.h](parser__url_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[http\_parser\_settings](structhttp__parser__settings.md)

**Definition** parser.h:190

[http\_parser\_settings::on\_header\_value](structhttp__parser__settings.md#a2af4e9085fa79ee52b31e626179bc561)

http\_data\_cb on\_header\_value

**Definition** parser.h:195

[http\_parser\_settings::on\_chunk\_header](structhttp__parser__settings.md#a497cf8f9d68e06e54684b71ee0f9f828)

http\_cb on\_chunk\_header

**Definition** parser.h:202

[http\_parser\_settings::on\_status](structhttp__parser__settings.md#a6d0f0203f3461a8889ad471de119c993)

http\_data\_cb on\_status

**Definition** parser.h:193

[http\_parser\_settings::on\_headers\_complete](structhttp__parser__settings.md#a743b24c8f33e0f1cf60a96c824c42071)

http\_cb on\_headers\_complete

**Definition** parser.h:196

[http\_parser\_settings::on\_url](structhttp__parser__settings.md#a9c24dfa900b49bf3439bbfba572b42fb)

http\_data\_cb on\_url

**Definition** parser.h:192

[http\_parser\_settings::on\_body](structhttp__parser__settings.md#aaa145d7c24c91f471b2079ecb6368ae4)

http\_data\_cb on\_body

**Definition** parser.h:197

[http\_parser\_settings::on\_chunk\_complete](structhttp__parser__settings.md#ac1c8453573094795ef41d4ba26e78846)

http\_cb on\_chunk\_complete

**Definition** parser.h:203

[http\_parser\_settings::on\_message\_begin](structhttp__parser__settings.md#ac44144daecc8e8adbd477b7e6a794e26)

http\_cb on\_message\_begin

**Definition** parser.h:191

[http\_parser\_settings::on\_header\_field](structhttp__parser__settings.md#acfb3fd7947c5ff3e16649c71aa13bff2)

http\_data\_cb on\_header\_field

**Definition** parser.h:194

[http\_parser\_settings::on\_message\_complete](structhttp__parser__settings.md#afdd5beef93a4a7b32bc61ae088da64d2)

http\_cb on\_message\_complete

**Definition** parser.h:198

[http\_parser](structhttp__parser.md)

**Definition** parser.h:147

[http\_parser::flags](structhttp__parser.md#a5e54708e0cb3f9ced19bd829dcdeaf53)

unsigned int flags

**Definition** parser.h:150

[http\_parser::state](structhttp__parser.md#a6f5952e0b47c83aeacf64fc287fd8003)

unsigned int state

**Definition** parser.h:153

[http\_parser::index](structhttp__parser.md#a6f7ba706f975f447b3bf72be97facdf8)

unsigned int index

**Definition** parser.h:156

[http\_parser::upgrade](structhttp__parser.md#a748f476eacc5ac56b84dd07dbafb42a4)

unsigned int upgrade

**Definition** parser.h:176

[http\_parser::nread](structhttp__parser.md#a78085ca896bb3b9aa1ecb0f6fddc039d)

uint32\_t nread

**Definition** parser.h:159

[http\_parser::method](structhttp__parser.md#a7955de339fafd81ad54380845913457d)

unsigned int method

**Definition** parser.h:167

[http\_parser::data](structhttp__parser.md#a7e87ce57b97f60f1fdb7039a8ecb0bca)

void \* data

PUBLIC.

**Definition** parser.h:179

[http\_parser::content\_length](structhttp__parser.md#a7fd5a194802b1206bb773e096d291f29)

uint64\_t content\_length

**Definition** parser.h:160

[http\_parser::status\_code](structhttp__parser.md#a82f5aed92ca3566489def7bc384bab26)

unsigned int status\_code

**Definition** parser.h:166

[http\_parser::http\_errno](structhttp__parser.md#ab8638d65fa174bc1925d77e2533117fa)

unsigned int http\_errno

**Definition** parser.h:168

[http\_parser::header\_state](structhttp__parser.md#ac5b254b99c6472ca19ae1f426758ce75)

unsigned int header\_state

**Definition** parser.h:154

[http\_parser::type](structhttp__parser.md#ac6c327558547d55eb64a8aea1310cc2e)

unsigned int type

PRIVATE.

**Definition** parser.h:149

[http\_parser::http\_major](structhttp__parser.md#ac994a4a8268652f5ce82de5bde5c3f9d)

unsigned short http\_major

READ-ONLY.

**Definition** parser.h:164

[http\_parser::lenient\_http\_headers](structhttp__parser.md#acd80a931fcc87d41999397af1662fc3c)

unsigned int lenient\_http\_headers

**Definition** parser.h:157

[http\_parser::http\_minor](structhttp__parser.md#ae8af6433c824f5348773842db62ad4ab)

unsigned short http\_minor

**Definition** parser.h:165

[http\_parser::addr](structhttp__parser.md#aecffbbbfebfc4f4a8cb4c034d18ef375)

const struct sockaddr \* addr

**Definition** parser.h:186

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:388

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [http](dir_12a17b6e7ad2c8cb36f68b2ff871e607.md)
- [parser.h](parser_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/stdint_8h_source.html
original_path: doxygen/html/stdint_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stdint.h

[Go to the documentation of this file.](stdint_8h.md)

1/\* stdint.h \*/

2

3/\*

4 \* Copyright (c) 2014 Wind River Systems, Inc.

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_STDINT\_H\_

10#define ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_STDINT\_H\_

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

[ 16](stdint_8h.md#aaf7f29f45f1a513b4748a4e5014ddf6a)#define INT8\_MAX \_\_INT8\_MAX\_\_

[ 17](stdint_8h.md#ac58f2c111cc9989c86db2a7dc4fd84ca)#define INT16\_MAX \_\_INT16\_MAX\_\_

[ 18](stdint_8h.md#a181807730d4a375f848ba139813ce04f)#define INT32\_MAX \_\_INT32\_MAX\_\_

[ 19](stdint_8h.md#ad0d744f05898e32d01f73f8af3cd2071)#define INT64\_MAX \_\_INT64\_MAX\_\_

[ 20](stdint_8h.md#a022b9b0a3564d786244a4631847c37a3)#define INTMAX\_MAX \_\_INT64\_MAX\_\_

21

[ 22](stdint_8h.md#aadcf2a81af243df333b31efa6461ab8e)#define INT8\_MIN (-INT8\_MAX - 1)

[ 23](stdint_8h.md#ad4e9955955b27624963643eac448118a)#define INT16\_MIN (-INT16\_MAX - 1)

[ 24](stdint_8h.md#a688eb21a22db27c2b2bd5836943cdcbe)#define INT32\_MIN (-INT32\_MAX - 1)

[ 25](stdint_8h.md#ab21f12f372f67b8ff0aa3432336ede67)#define INT64\_MIN (-INT64\_MAX - 1LL)

26

[ 27](stdint_8h.md#aeb4e270a084ee26fe73e799861bd0252)#define UINT8\_MAX \_\_UINT8\_MAX\_\_

[ 28](stdint_8h.md#a3ea490c9b3617d4479bd80ef93cd5602)#define UINT16\_MAX \_\_UINT16\_MAX\_\_

[ 29](stdint_8h.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)#define UINT32\_MAX \_\_UINT32\_MAX\_\_

[ 30](stdint_8h.md#a30654b4b67d97c42ca3f9b6052dda916)#define UINT64\_MAX \_\_UINT64\_MAX\_\_

[ 31](stdint_8h.md#aa54fd5210434219e9027bfa0f0e325c8)#define UINTMAX\_MAX \_\_UINT64\_MAX\_\_

32

[ 33](stdint_8h.md#acbcdb3bee0f5f904da5df8de69a80ca3)#define INT\_FAST8\_MAX \_\_INT\_FAST8\_MAX\_\_

[ 34](stdint_8h.md#a2fd35d0ea091e04caec504ff0042cf00)#define INT\_FAST16\_MAX \_\_INT\_FAST16\_MAX\_\_

[ 35](stdint_8h.md#ac96fa0f41b19e89f109e4f9913ca6635)#define INT\_FAST32\_MAX \_\_INT\_FAST32\_MAX\_\_

[ 36](stdint_8h.md#a13c95cf9c209d8daacb36cbf0d5ba275)#define INT\_FAST64\_MAX \_\_INT\_FAST64\_MAX\_\_

37

[ 38](stdint_8h.md#aad8fb982cb19143efd5ee9a1a7a89390)#define INT\_FAST8\_MIN (-INT\_FAST8\_MAX - 1)

[ 39](stdint_8h.md#a169460a4e2a79138723d68d99372d958)#define INT\_FAST16\_MIN (-INT\_FAST16\_MAX - 1)

[ 40](stdint_8h.md#ad93df1652ed0635513d5efe4f1219926)#define INT\_FAST32\_MIN (-INT\_FAST32\_MAX - 1)

[ 41](stdint_8h.md#a50f0fdcb00ea2500cec0f3d6d45c36f3)#define INT\_FAST64\_MIN (-INT\_FAST64\_MAX - 1LL)

42

[ 43](stdint_8h.md#a2c6f97ea2d76d0cf6260c84046cdb44e)#define UINT\_FAST8\_MAX \_\_UINT\_FAST8\_MAX\_\_

[ 44](stdint_8h.md#aed28ca63d9b222f6f1377358fe73a183)#define UINT\_FAST16\_MAX \_\_UINT\_FAST16\_MAX\_\_

[ 45](stdint_8h.md#ad51246a178143208b2db3315efd21c45)#define UINT\_FAST32\_MAX \_\_UINT\_FAST32\_MAX\_\_

[ 46](stdint_8h.md#aeb74410af7781bc84b5f64ae7a8f4a17)#define UINT\_FAST64\_MAX \_\_UINT\_FAST64\_MAX\_\_

47

[ 48](stdint_8h.md#aa05109908fb2770f632d2b646b9f85bf)#define INT\_LEAST8\_MAX \_\_INT\_LEAST8\_MAX\_\_

[ 49](stdint_8h.md#a7eb2a8e2a1c65d6c9ad0f86154890baa)#define INT\_LEAST16\_MAX \_\_INT\_LEAST16\_MAX\_\_

[ 50](stdint_8h.md#a5618711a0a54f722190a3a1219e278c2)#define INT\_LEAST32\_MAX \_\_INT\_LEAST32\_MAX\_\_

[ 51](stdint_8h.md#a35d0f98a2e507fd1be779d49da92724e)#define INT\_LEAST64\_MAX \_\_INT\_LEAST64\_MAX\_\_

52

[ 53](stdint_8h.md#a3e986cad833f63f420962ff60eda87e5)#define INT\_LEAST8\_MIN (-INT\_LEAST8\_MAX - 1)

[ 54](stdint_8h.md#a1f91bfd5820c2f27af3d260fc75813e1)#define INT\_LEAST16\_MIN (-INT\_LEAST16\_MAX - 1)

[ 55](stdint_8h.md#a2360a536116dd734820a6b5b3d560ce7)#define INT\_LEAST32\_MIN (-INT\_LEAST32\_MAX - 1)

[ 56](stdint_8h.md#ac12b4f6966b57ad82feb683b284b4060)#define INT\_LEAST64\_MIN (-INT\_LEAST64\_MAX - 1LL)

57

[ 58](stdint_8h.md#a2a80bde77ee1698d0f42f334adad4f2b)#define UINT\_LEAST8\_MAX \_\_UINT\_LEAST8\_MAX\_\_

[ 59](stdint_8h.md#a6ef6a1a518bbf516ca8b0180b11c358f)#define UINT\_LEAST16\_MAX \_\_UINT\_LEAST16\_MAX\_\_

[ 60](stdint_8h.md#a70cad8bacc9a6db301e1cdc86cc8d571)#define UINT\_LEAST32\_MAX \_\_UINT\_LEAST32\_MAX\_\_

[ 61](stdint_8h.md#aab530113fa96e280e49c3c138b0f917d)#define UINT\_LEAST64\_MAX \_\_UINT\_LEAST64\_MAX\_\_

62

[ 63](stdint_8h.md#a9e5742f2bae4a5283431a3c03499e3a9)#define INTPTR\_MAX \_\_INTPTR\_MAX\_\_

[ 64](stdint_8h.md#a2aaa6d3aa1d7d1e0e326955aa24db752)#define INTPTR\_MIN (-INTPTR\_MAX - 1)

[ 65](stdint_8h.md#ab2355300ea19395357e62d780f4dd073)#define UINTPTR\_MAX \_\_UINTPTR\_MAX\_\_

66

[ 67](stdint_8h.md#add2ef7bffac19cfdd1f4b5495409672f)#define PTRDIFF\_MAX \_\_PTRDIFF\_MAX\_\_

[ 68](stdint_8h.md#ad9b88ba2fb858f98b50b38e49875d90e)#define PTRDIFF\_MIN (-PTRDIFF\_MAX - 1)

69

[ 70](stdint_8h.md#a3c75bb398badb69c7577b21486f9963f)#define SIZE\_MAX \_\_SIZE\_MAX\_\_

71

[ 72](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)typedef \_\_INT8\_TYPE\_\_ [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6);

[ 73](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)typedef \_\_INT16\_TYPE\_\_ [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf);

[ 74](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)typedef \_\_INT32\_TYPE\_\_ [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2);

[ 75](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)typedef \_\_INT64\_TYPE\_\_ [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b);

[ 76](stdint_8h.md#a9d6c1dc12f73927ba41516de04a5fdb8)typedef \_\_INT64\_TYPE\_\_ [intmax\_t](stdint_8h.md#a9d6c1dc12f73927ba41516de04a5fdb8);

77

[ 78](stdint_8h.md#a98f573ff8187ff09c9594a3f2af7be0d)typedef \_\_INT\_FAST8\_TYPE\_\_ [int\_fast8\_t](stdint_8h.md#a98f573ff8187ff09c9594a3f2af7be0d);

[ 79](stdint_8h.md#a888269be199d49b7f40006aaafa5a350)typedef \_\_INT\_FAST16\_TYPE\_\_ [int\_fast16\_t](stdint_8h.md#a888269be199d49b7f40006aaafa5a350);

[ 80](stdint_8h.md#a530ba8ffc89f6393d2d0e2fb2db38b54)typedef \_\_INT\_FAST32\_TYPE\_\_ [int\_fast32\_t](stdint_8h.md#a530ba8ffc89f6393d2d0e2fb2db38b54);

[ 81](stdint_8h.md#abcdb0a9f6e7d139ad4f521ab8f4efdc0)typedef \_\_INT\_FAST64\_TYPE\_\_ [int\_fast64\_t](stdint_8h.md#abcdb0a9f6e7d139ad4f521ab8f4efdc0);

82

[ 83](stdint_8h.md#adb5f4bf8afa3bee9e4da1bb9daf4908d)typedef \_\_INT\_LEAST8\_TYPE\_\_ [int\_least8\_t](stdint_8h.md#adb5f4bf8afa3bee9e4da1bb9daf4908d);

[ 84](stdint_8h.md#a3a4bc1e426626e17f6a6e0f64decec56)typedef \_\_INT\_LEAST16\_TYPE\_\_ [int\_least16\_t](stdint_8h.md#a3a4bc1e426626e17f6a6e0f64decec56);

[ 85](stdint_8h.md#a4462f62ae74ff8172526401354d2fc9b)typedef \_\_INT\_LEAST32\_TYPE\_\_ [int\_least32\_t](stdint_8h.md#a4462f62ae74ff8172526401354d2fc9b);

[ 86](stdint_8h.md#a8a5003442318117c64d16d6f32f64f37)typedef \_\_INT\_LEAST64\_TYPE\_\_ [int\_least64\_t](stdint_8h.md#a8a5003442318117c64d16d6f32f64f37);

87

[ 88](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)typedef \_\_UINT8\_TYPE\_\_ [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d);

[ 89](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)typedef \_\_UINT16\_TYPE\_\_ [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e);

[ 90](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)typedef \_\_UINT32\_TYPE\_\_ [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f);

[ 91](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)typedef \_\_UINT64\_TYPE\_\_ [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1);

[ 92](stdint_8h.md#aac7deaa1633720ec64bd432bbc31af40)typedef \_\_UINT64\_TYPE\_\_ [uintmax\_t](stdint_8h.md#aac7deaa1633720ec64bd432bbc31af40);

93

[ 94](stdint_8h.md#a2464ed69ccd3fd2b3b4c93cb78f6fa20)typedef \_\_UINT\_FAST8\_TYPE\_\_ [uint\_fast8\_t](stdint_8h.md#a2464ed69ccd3fd2b3b4c93cb78f6fa20);

[ 95](stdint_8h.md#aaabed6e034edb01c259c003894d7f7c8)typedef \_\_UINT\_FAST16\_TYPE\_\_ [uint\_fast16\_t](stdint_8h.md#aaabed6e034edb01c259c003894d7f7c8);

[ 96](stdint_8h.md#aa44ff507c3d9a49e27fac64e9fadf062)typedef \_\_UINT\_FAST32\_TYPE\_\_ [uint\_fast32\_t](stdint_8h.md#aa44ff507c3d9a49e27fac64e9fadf062);

[ 97](stdint_8h.md#a62c711f66c6d29c81429aeafdc4bc592)typedef \_\_UINT\_FAST64\_TYPE\_\_ [uint\_fast64\_t](stdint_8h.md#a62c711f66c6d29c81429aeafdc4bc592);

98

[ 99](stdint_8h.md#a61d44370ed65907c324edad5e8d34632)typedef \_\_UINT\_LEAST8\_TYPE\_\_ [uint\_least8\_t](stdint_8h.md#a61d44370ed65907c324edad5e8d34632);

[ 100](stdint_8h.md#a1a01d6a4e68e435471be2ae8db7e8fdc)typedef \_\_UINT\_LEAST16\_TYPE\_\_ [uint\_least16\_t](stdint_8h.md#a1a01d6a4e68e435471be2ae8db7e8fdc);

[ 101](stdint_8h.md#a678494ae5435d8904e7972c94618e774)typedef \_\_UINT\_LEAST32\_TYPE\_\_ [uint\_least32\_t](stdint_8h.md#a678494ae5435d8904e7972c94618e774);

[ 102](stdint_8h.md#aba0cb5638c172422eb4a7555a143fbbc)typedef \_\_UINT\_LEAST64\_TYPE\_\_ [uint\_least64\_t](stdint_8h.md#aba0cb5638c172422eb4a7555a143fbbc);

103

[ 104](stdint_8h.md#a0bd5dec00e345e69027427f8621d6a6c)typedef \_\_INTPTR\_TYPE\_\_ [intptr\_t](stdint_8h.md#a0bd5dec00e345e69027427f8621d6a6c);

[ 105](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)typedef \_\_UINTPTR\_TYPE\_\_ [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808);

106

107#if defined(\_\_GNUC\_\_) || defined(\_\_clang\_\_)

108/\* These macros must produce constant integer expressions, which can't

109 \* be done in the preprocessor (casts aren't allowed). Defer to the

110 \* GCC internal functions where they're available.

111 \*/

112#define INT8\_C(\_v) \_\_INT8\_C(\_v)

113#define INT16\_C(\_v) \_\_INT16\_C(\_v)

114#define INT32\_C(\_v) \_\_INT32\_C(\_v)

115#define INT64\_C(\_v) \_\_INT64\_C(\_v)

116#define INTMAX\_C(\_v) \_\_INTMAX\_C(\_v)

117

118#define UINT8\_C(\_v) \_\_UINT8\_C(\_v)

119#define UINT16\_C(\_v) \_\_UINT16\_C(\_v)

120#define UINT32\_C(\_v) \_\_UINT32\_C(\_v)

121#define UINT64\_C(\_v) \_\_UINT64\_C(\_v)

122#define UINTMAX\_C(\_v) \_\_UINTMAX\_C(\_v)

123#endif /\* defined(\_\_GNUC\_\_) || defined(\_\_clang\_\_) \*/

124

125#ifdef \_\_CCAC\_\_

126#ifndef \_\_INT8\_C

127#define \_\_INT8\_C(x) x

128#endif

129

130#ifndef INT8\_C

131#define INT8\_C(x) \_\_INT8\_C(x)

132#endif

133

134#ifndef \_\_UINT8\_C

135#define \_\_UINT8\_C(x) x ## U

136#endif

137

138#ifndef UINT8\_C

139#define UINT8\_C(x) \_\_UINT8\_C(x)

140#endif

141

142#ifndef \_\_INT16\_C

143#define \_\_INT16\_C(x) x

144#endif

145

146#ifndef INT16\_C

147#define INT16\_C(x) \_\_INT16\_C(x)

148#endif

149

150#ifndef \_\_UINT16\_C

151#define \_\_UINT16\_C(x) x ## U

152#endif

153

154#ifndef UINT16\_C

155#define UINT16\_C(x) \_\_UINT16\_C(x)

156#endif

157

158#ifndef \_\_INT32\_C

159#define \_\_INT32\_C(x) x

160#endif

161

162#ifndef INT32\_C

163#define INT32\_C(x) \_\_INT32\_C(x)

164#endif

165

166#ifndef \_\_UINT32\_C

167#define \_\_UINT32\_C(x) x ## U

168#endif

169

170#ifndef UINT32\_C

171#define UINT32\_C(x) \_\_UINT32\_C(x)

172#endif

173

174#ifndef \_\_INT64\_C

175#define \_\_INT64\_C(x) x

176#endif

177

178#ifndef INT64\_C

179#define INT64\_C(x) \_\_INT64\_C(x)

180#endif

181

182#ifndef \_\_UINT64\_C

183#define \_\_UINT64\_C(x) x ## ULL

184#endif

185

186#ifndef UINT64\_C

187#define UINT64\_C(x) \_\_UINT64\_C(x)

188#endif

189

190#ifndef \_\_INTMAX\_C

191#define \_\_INTMAX\_C(x) x

192#endif

193

194#ifndef INTMAX\_C

195#define INTMAX\_C(x) \_\_INTMAX\_C(x)

196#endif

197

198#ifndef \_\_UINTMAX\_C

199#define \_\_UINTMAX\_C(x) x ## ULL

200#endif

201

202#ifndef UINTMAX\_C

203#define UINTMAX\_C(x) \_\_UINTMAX\_C(x)

204#endif

205#endif /\* \_\_CCAC\_\_ \*/

206

207#ifdef \_\_cplusplus

208}

209#endif

210

211#endif /\* ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_STDINT\_H\_ \*/

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[intptr\_t](stdint_8h.md#a0bd5dec00e345e69027427f8621d6a6c)

\_\_INTPTR\_TYPE\_\_ intptr\_t

**Definition** stdint.h:104

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint\_least16\_t](stdint_8h.md#a1a01d6a4e68e435471be2ae8db7e8fdc)

\_\_UINT\_LEAST16\_TYPE\_\_ uint\_least16\_t

**Definition** stdint.h:100

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint\_fast8\_t](stdint_8h.md#a2464ed69ccd3fd2b3b4c93cb78f6fa20)

\_\_UINT\_FAST8\_TYPE\_\_ uint\_fast8\_t

**Definition** stdint.h:94

[int\_least16\_t](stdint_8h.md#a3a4bc1e426626e17f6a6e0f64decec56)

\_\_INT\_LEAST16\_TYPE\_\_ int\_least16\_t

**Definition** stdint.h:84

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[int\_least32\_t](stdint_8h.md#a4462f62ae74ff8172526401354d2fc9b)

\_\_INT\_LEAST32\_TYPE\_\_ int\_least32\_t

**Definition** stdint.h:85

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[int\_fast32\_t](stdint_8h.md#a530ba8ffc89f6393d2d0e2fb2db38b54)

\_\_INT\_FAST32\_TYPE\_\_ int\_fast32\_t

**Definition** stdint.h:80

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[uint\_least8\_t](stdint_8h.md#a61d44370ed65907c324edad5e8d34632)

\_\_UINT\_LEAST8\_TYPE\_\_ uint\_least8\_t

**Definition** stdint.h:99

[uint\_fast64\_t](stdint_8h.md#a62c711f66c6d29c81429aeafdc4bc592)

\_\_UINT\_FAST64\_TYPE\_\_ uint\_fast64\_t

**Definition** stdint.h:97

[uint\_least32\_t](stdint_8h.md#a678494ae5435d8904e7972c94618e774)

\_\_UINT\_LEAST32\_TYPE\_\_ uint\_least32\_t

**Definition** stdint.h:101

[int\_fast16\_t](stdint_8h.md#a888269be199d49b7f40006aaafa5a350)

\_\_INT\_FAST16\_TYPE\_\_ int\_fast16\_t

**Definition** stdint.h:79

[int\_least64\_t](stdint_8h.md#a8a5003442318117c64d16d6f32f64f37)

\_\_INT\_LEAST64\_TYPE\_\_ int\_least64\_t

**Definition** stdint.h:86

[int\_fast8\_t](stdint_8h.md#a98f573ff8187ff09c9594a3f2af7be0d)

\_\_INT\_FAST8\_TYPE\_\_ int\_fast8\_t

**Definition** stdint.h:78

[intmax\_t](stdint_8h.md#a9d6c1dc12f73927ba41516de04a5fdb8)

\_\_INT64\_TYPE\_\_ intmax\_t

**Definition** stdint.h:76

[uint\_fast32\_t](stdint_8h.md#aa44ff507c3d9a49e27fac64e9fadf062)

\_\_UINT\_FAST32\_TYPE\_\_ uint\_fast32\_t

**Definition** stdint.h:96

[uint\_fast16\_t](stdint_8h.md#aaabed6e034edb01c259c003894d7f7c8)

\_\_UINT\_FAST16\_TYPE\_\_ uint\_fast16\_t

**Definition** stdint.h:95

[uintmax\_t](stdint_8h.md#aac7deaa1633720ec64bd432bbc31af40)

\_\_UINT64\_TYPE\_\_ uintmax\_t

**Definition** stdint.h:92

[uint\_least64\_t](stdint_8h.md#aba0cb5638c172422eb4a7555a143fbbc)

\_\_UINT\_LEAST64\_TYPE\_\_ uint\_least64\_t

**Definition** stdint.h:102

[int\_fast64\_t](stdint_8h.md#abcdb0a9f6e7d139ad4f521ab8f4efdc0)

\_\_INT\_FAST64\_TYPE\_\_ int\_fast64\_t

**Definition** stdint.h:81

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[int\_least8\_t](stdint_8h.md#adb5f4bf8afa3bee9e4da1bb9daf4908d)

\_\_INT\_LEAST8\_TYPE\_\_ int\_least8\_t

**Definition** stdint.h:83

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

- [lib](dir_97aefd0d527b934f1d99a682da8fe6a9.md)
- [libc](dir_b38b009475962ec458a8a4ac1c89fad6.md)
- [minimal](dir_cb013e9b53665816a2b0a66572d8a7af.md)
- [include](dir_33cd71cddfb4d86c87a49ac212c07c64.md)
- [stdint.h](stdint_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

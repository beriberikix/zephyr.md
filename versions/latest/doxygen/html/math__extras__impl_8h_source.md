---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/math__extras__impl_8h_source.html
original_path: doxygen/html/math__extras__impl_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

math\_extras\_impl.h

[Go to the documentation of this file.](math__extras__impl_8h.md)

1/\*

2 \* Copyright (c) 2019 Facebook.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_SYS\_MATH\_EXTRAS\_H\_

13#error "please include <sys/math\_extras.h> instead of this file"

14#endif

15

16#include <[zephyr/toolchain.h](toolchain_8h.md)>

17

18/\*

19 \* Force the use of portable C code (no builtins) by defining

20 \* PORTABLE\_MISC\_MATH\_EXTRAS before including <misc/math\_extras.h>.

21 \* This is primarily for use by tests.

22 \*

23 \* We'll #undef use\_builtin again at the end of the file.

24 \*/

25#ifdef PORTABLE\_MISC\_MATH\_EXTRAS

26#define use\_builtin(x) 0

27#else

[ 28](math__extras__impl_8h.md#a64a27aae3fe9b5182e18f3bf424eb7f5)#define use\_builtin(x) HAS\_BUILTIN(x)

29#endif

30

31#if use\_builtin(\_\_builtin\_add\_overflow)

32static inline bool [u16\_add\_overflow](math__extras__impl_8h.md#a62d018abdf97551665cab7486b5a519a)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) a, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) b, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*result)

33{

34 return \_\_builtin\_add\_overflow(a, b, result);

35}

36

37static inline bool [u32\_add\_overflow](math__extras__impl_8h.md#a3f36aa272f5595d78c6e8219b2c4dbfb)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) a, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) b, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*result)

38{

39 return \_\_builtin\_add\_overflow(a, b, result);

40}

41

42static inline bool [u64\_add\_overflow](math__extras__impl_8h.md#af98ec1d8b1c00e30382eed01853e3307)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) a, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) b, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*result)

43{

44 return \_\_builtin\_add\_overflow(a, b, result);

45}

46

47static inline bool [size\_add\_overflow](math__extras__impl_8h.md#a7aaec179564038b540aaf4ab3c9a666d)(size\_t a, size\_t b, size\_t \*result)

48{

49 return \_\_builtin\_add\_overflow(a, b, result);

50}

51#else /\* !use\_builtin(\_\_builtin\_add\_overflow) \*/

[ 52](math__extras__impl_8h.md#a62d018abdf97551665cab7486b5a519a)static inline bool [u16\_add\_overflow](math__extras__impl_8h.md#a62d018abdf97551665cab7486b5a519a)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) a, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) b, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*result)

53{

54 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) c = a + b;

55

56 \*result = c;

57

58 return c < a;

59}

60

[ 61](math__extras__impl_8h.md#a3f36aa272f5595d78c6e8219b2c4dbfb)static inline bool [u32\_add\_overflow](math__extras__impl_8h.md#a3f36aa272f5595d78c6e8219b2c4dbfb)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) a, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) b, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*result)

62{

63 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) c = a + b;

64

65 \*result = c;

66

67 return c < a;

68}

69

[ 70](math__extras__impl_8h.md#af98ec1d8b1c00e30382eed01853e3307)static inline bool [u64\_add\_overflow](math__extras__impl_8h.md#af98ec1d8b1c00e30382eed01853e3307)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) a, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) b, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*result)

71{

72 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) c = a + b;

73

74 \*result = c;

75

76 return c < a;

77}

78

[ 79](math__extras__impl_8h.md#a7aaec179564038b540aaf4ab3c9a666d)static inline bool [size\_add\_overflow](math__extras__impl_8h.md#a7aaec179564038b540aaf4ab3c9a666d)(size\_t a, size\_t b, size\_t \*result)

80{

81 size\_t c = a + b;

82

83 \*result = c;

84

85 return c < a;

86}

87#endif /\* use\_builtin(\_\_builtin\_add\_overflow) \*/

88

89#if use\_builtin(\_\_builtin\_mul\_overflow)

90static inline bool [u16\_mul\_overflow](math__extras__impl_8h.md#a292df7083a9da5525cda13e2546e81ba)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) a, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) b, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*result)

91{

92 return \_\_builtin\_mul\_overflow(a, b, result);

93}

94

95static inline bool [u32\_mul\_overflow](math__extras__impl_8h.md#a427e8cd4fcafab244576994acc9b960f)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) a, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) b, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*result)

96{

97 return \_\_builtin\_mul\_overflow(a, b, result);

98}

99

100static inline bool [u64\_mul\_overflow](math__extras__impl_8h.md#a366f6606874071677bf9079647d9abce)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) a, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) b, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*result)

101{

102 return \_\_builtin\_mul\_overflow(a, b, result);

103}

104

105static inline bool [size\_mul\_overflow](math__extras__impl_8h.md#a790b24a5d239afcc08d9e4f66c25ea56)(size\_t a, size\_t b, size\_t \*result)

106{

107 return \_\_builtin\_mul\_overflow(a, b, result);

108}

109#else /\* !use\_builtin(\_\_builtin\_mul\_overflow) \*/

[ 110](math__extras__impl_8h.md#a292df7083a9da5525cda13e2546e81ba)static inline bool [u16\_mul\_overflow](math__extras__impl_8h.md#a292df7083a9da5525cda13e2546e81ba)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) a, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) b, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*result)

111{

112 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) c = a \* b;

113

114 \*result = c;

115

116 return a != 0 && (c / a) != b;

117}

118

[ 119](math__extras__impl_8h.md#a427e8cd4fcafab244576994acc9b960f)static inline bool [u32\_mul\_overflow](math__extras__impl_8h.md#a427e8cd4fcafab244576994acc9b960f)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) a, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) b, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*result)

120{

121 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) c = a \* b;

122

123 \*result = c;

124

125 return a != 0 && (c / a) != b;

126}

127

[ 128](math__extras__impl_8h.md#a366f6606874071677bf9079647d9abce)static inline bool [u64\_mul\_overflow](math__extras__impl_8h.md#a366f6606874071677bf9079647d9abce)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) a, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) b, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*result)

129{

130 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) c = a \* b;

131

132 \*result = c;

133

134 return a != 0 && (c / a) != b;

135}

136

[ 137](math__extras__impl_8h.md#a790b24a5d239afcc08d9e4f66c25ea56)static inline bool [size\_mul\_overflow](math__extras__impl_8h.md#a790b24a5d239afcc08d9e4f66c25ea56)(size\_t a, size\_t b, size\_t \*result)

138{

139 size\_t c = a \* b;

140

141 \*result = c;

142

143 return a != 0 && (c / a) != b;

144}

145#endif /\* use\_builtin(\_\_builtin\_mul\_overflow) \*/

146

147

148/\*

149 \* The GCC builtins \_\_builtin\_clz(), \_\_builtin\_ctz(), and 64-bit

150 \* variants are described by the GCC documentation as having undefined

151 \* behavior when the argument is zero. See

152 \* https://gcc.gnu.org/onlinedocs/gcc/Other-Builtins.html.

153 \*

154 \* The undefined behavior applies to all architectures, regardless of

155 \* the behavior of the instruction used to implement the builtin.

156 \*

157 \* We don't want to expose users of this API to the undefined behavior,

158 \* so we use a conditional to explicitly provide the correct result when

159 \* x=0.

160 \*

161 \* Most instruction set architectures have a CLZ instruction or similar

162 \* that already computes the correct result for x=0. Both GCC and Clang

163 \* know this and simply generate a CLZ instruction, optimizing away the

164 \* conditional.

165 \*

166 \* For x86, and for compilers that fail to eliminate the conditional,

167 \* there is often another opportunity for optimization since code using

168 \* these functions tends to contain a zero check already. For example,

169 \* from kernel/sched.c:

170 \*

171 \* struct k\_thread \*z\_priq\_mq\_best(struct \_priq\_mq \*pq)

172 \* {

173 \* if (!pq->bitmask) {

174 \* return NULL;

175 \* }

176 \*

177 \* struct k\_thread \*thread = NULL;

178 \* sys\_dlist\_t \*l =

179 \* &pq->queues[u32\_count\_trailing\_zeros(pq->bitmask)];

180 \*

181 \* ...

182 \*

183 \* The compiler will often be able to eliminate the redundant x == 0

184 \* check after inlining the call to u32\_count\_trailing\_zeros().

185 \*/

186

187#if use\_builtin(\_\_builtin\_clz)

188static inline int [u32\_count\_leading\_zeros](math__extras__impl_8h.md#a97e8d8a40a45899ab7e5ce718342536b)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) x)

189{

190 return x == 0 ? 32 : \_\_builtin\_clz(x);

191}

192#else /\* !use\_builtin(\_\_builtin\_clz) \*/

[ 193](math__extras__impl_8h.md#a97e8d8a40a45899ab7e5ce718342536b)static inline int [u32\_count\_leading\_zeros](math__extras__impl_8h.md#a97e8d8a40a45899ab7e5ce718342536b)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) x)

194{

195 int b;

196

197 for (b = 0; b < 32 && (x >> 31) == 0; b++) {

198 x <<= 1;

199 }

200

201 return b;

202}

203#endif /\* use\_builtin(\_\_builtin\_clz) \*/

204

205#if use\_builtin(\_\_builtin\_clzll)

206static inline int [u64\_count\_leading\_zeros](math__extras__impl_8h.md#af5f31e98f2f675a0b4cc54b7fba6f56c)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x)

207{

208 return x == 0 ? 64 : \_\_builtin\_clzll(x);

209}

210#else /\* !use\_builtin(\_\_builtin\_clzll) \*/

[ 211](math__extras__impl_8h.md#af5f31e98f2f675a0b4cc54b7fba6f56c)static inline int [u64\_count\_leading\_zeros](math__extras__impl_8h.md#af5f31e98f2f675a0b4cc54b7fba6f56c)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x)

212{

213 if (x == ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))x) {

214 return 32 + [u32\_count\_leading\_zeros](math__extras__impl_8h.md#a97e8d8a40a45899ab7e5ce718342536b)(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))x);

215 } else {

216 return [u32\_count\_leading\_zeros](math__extras__impl_8h.md#a97e8d8a40a45899ab7e5ce718342536b)(x >> 32);

217 }

218}

219#endif /\* use\_builtin(\_\_builtin\_clzll) \*/

220

221#if use\_builtin(\_\_builtin\_ctz)

222static inline int [u32\_count\_trailing\_zeros](math__extras__impl_8h.md#a4cb313f98c3fd3b00d6f4db74a9a0076)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) x)

223{

224 return x == 0 ? 32 : \_\_builtin\_ctz(x);

225}

226#else /\* !use\_builtin(\_\_builtin\_ctz) \*/

[ 227](math__extras__impl_8h.md#a4cb313f98c3fd3b00d6f4db74a9a0076)static inline int [u32\_count\_trailing\_zeros](math__extras__impl_8h.md#a4cb313f98c3fd3b00d6f4db74a9a0076)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) x)

228{

229 int b;

230

231 for (b = 0; b < 32 && (x & 1) == 0; b++) {

232 x >>= 1;

233 }

234

235 return b;

236}

237#endif /\* use\_builtin(\_\_builtin\_ctz) \*/

238

239#if use\_builtin(\_\_builtin\_ctzll)

240static inline int [u64\_count\_trailing\_zeros](math__extras__impl_8h.md#a300356629c0388d37958ef026180ea4d)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x)

241{

242 return x == 0 ? 64 : \_\_builtin\_ctzll(x);

243}

244#else /\* !use\_builtin(\_\_builtin\_ctzll) \*/

[ 245](math__extras__impl_8h.md#a300356629c0388d37958ef026180ea4d)static inline int [u64\_count\_trailing\_zeros](math__extras__impl_8h.md#a300356629c0388d37958ef026180ea4d)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x)

246{

247 if (([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))x) {

248 return [u32\_count\_trailing\_zeros](math__extras__impl_8h.md#a4cb313f98c3fd3b00d6f4db74a9a0076)(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))x);

249 } else {

250 return 32 + [u32\_count\_trailing\_zeros](math__extras__impl_8h.md#a4cb313f98c3fd3b00d6f4db74a9a0076)(x >> 32);

251 }

252}

253#endif /\* use\_builtin(\_\_builtin\_ctzll) \*/

254

255#undef use\_builtin

[u16\_mul\_overflow](math__extras__impl_8h.md#a292df7083a9da5525cda13e2546e81ba)

static bool u16\_mul\_overflow(uint16\_t a, uint16\_t b, uint16\_t \*result)

**Definition** math\_extras\_impl.h:110

[u64\_count\_trailing\_zeros](math__extras__impl_8h.md#a300356629c0388d37958ef026180ea4d)

static int u64\_count\_trailing\_zeros(uint64\_t x)

**Definition** math\_extras\_impl.h:245

[u64\_mul\_overflow](math__extras__impl_8h.md#a366f6606874071677bf9079647d9abce)

static bool u64\_mul\_overflow(uint64\_t a, uint64\_t b, uint64\_t \*result)

**Definition** math\_extras\_impl.h:128

[u32\_add\_overflow](math__extras__impl_8h.md#a3f36aa272f5595d78c6e8219b2c4dbfb)

static bool u32\_add\_overflow(uint32\_t a, uint32\_t b, uint32\_t \*result)

**Definition** math\_extras\_impl.h:61

[u32\_mul\_overflow](math__extras__impl_8h.md#a427e8cd4fcafab244576994acc9b960f)

static bool u32\_mul\_overflow(uint32\_t a, uint32\_t b, uint32\_t \*result)

**Definition** math\_extras\_impl.h:119

[u32\_count\_trailing\_zeros](math__extras__impl_8h.md#a4cb313f98c3fd3b00d6f4db74a9a0076)

static int u32\_count\_trailing\_zeros(uint32\_t x)

**Definition** math\_extras\_impl.h:227

[u16\_add\_overflow](math__extras__impl_8h.md#a62d018abdf97551665cab7486b5a519a)

static bool u16\_add\_overflow(uint16\_t a, uint16\_t b, uint16\_t \*result)

**Definition** math\_extras\_impl.h:52

[size\_mul\_overflow](math__extras__impl_8h.md#a790b24a5d239afcc08d9e4f66c25ea56)

static bool size\_mul\_overflow(size\_t a, size\_t b, size\_t \*result)

**Definition** math\_extras\_impl.h:137

[size\_add\_overflow](math__extras__impl_8h.md#a7aaec179564038b540aaf4ab3c9a666d)

static bool size\_add\_overflow(size\_t a, size\_t b, size\_t \*result)

**Definition** math\_extras\_impl.h:79

[u32\_count\_leading\_zeros](math__extras__impl_8h.md#a97e8d8a40a45899ab7e5ce718342536b)

static int u32\_count\_leading\_zeros(uint32\_t x)

**Definition** math\_extras\_impl.h:193

[u64\_count\_leading\_zeros](math__extras__impl_8h.md#af5f31e98f2f675a0b4cc54b7fba6f56c)

static int u64\_count\_leading\_zeros(uint64\_t x)

**Definition** math\_extras\_impl.h:211

[u64\_add\_overflow](math__extras__impl_8h.md#af98ec1d8b1c00e30382eed01853e3307)

static bool u64\_add\_overflow(uint64\_t a, uint64\_t b, uint64\_t \*result)

**Definition** math\_extras\_impl.h:70

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [math\_extras\_impl.h](math__extras__impl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/addr_8h_source.html
original_path: doxygen/html/addr_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

addr.h

[Go to the documentation of this file.](addr_8h.md)

1

4

5/\*

6 \* Copyright (c) 2019 Nordic Semiconductor ASA

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_ADDR\_H\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_ADDR\_H\_

12

13#include <[stdint.h](stdint_8h.md)>

14#include <[string.h](string_8h.md)>

15

16#include <[zephyr/sys/printk.h](printk_8h.md)>

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

28

[ 29](group__bt__addr.md#ga1717d2b4e61b28637be8a5f78685a3c4)#define BT\_ADDR\_LE\_PUBLIC 0x00

[ 30](group__bt__addr.md#ga6e81e967527b5418ee6cbc6d72c5aef9)#define BT\_ADDR\_LE\_RANDOM 0x01

[ 31](group__bt__addr.md#ga1fd60d5eb4c8a6d8f4df06eaba85fb96)#define BT\_ADDR\_LE\_PUBLIC\_ID 0x02

[ 32](group__bt__addr.md#gafdf2572991427d95bb44d1a5ee2ad85a)#define BT\_ADDR\_LE\_RANDOM\_ID 0x03

[ 33](group__bt__addr.md#gad02c40564a140300efda28ecb15674be)#define BT\_ADDR\_LE\_UNRESOLVED 0xFE /\* Resolvable Private Address

[ 34](group__bt__addr.md#gab2ddd85c5972a53da0aee3974edc0258) \* (Controller unable to resolve)

35 \*/

36#define BT\_ADDR\_LE\_ANONYMOUS 0xFF /\* No address provided

[ 37](group__bt__addr.md#ga6b6f56325b5136d2719f02eecc780d49) \* (anonymous advertisement)

38 \*/

39

[ 40](structbt__addr__t.md)/\*\* Length in bytes of a standard Bluetooth address \*/

[ 41](structbt__addr__t.md#a59e03c3fd06d16dc41132fd21ac42952)#define BT\_ADDR\_SIZE 6

42

43

44typedef struct {

45 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [val](structbt__addr__t.md#a59e03c3fd06d16dc41132fd21ac42952)[[BT\_ADDR\_SIZE](group__bt__addr.md#ga6b6f56325b5136d2719f02eecc780d49)];

[ 46](group__bt__addr.md#ga2656b9a936bf8cb9f1cc86668fca6108)} [bt\_addr\_t](structbt__addr__t.md);

47/\*\*/

48

[ 49](structbt__addr__le__t.md)/\*\* Length in bytes of an LE Bluetooth address. Not packed, so no sizeof() \*/

[ 50](structbt__addr__le__t.md#aa4ede005c57893383a21983bc3e47958)#define BT\_ADDR\_LE\_SIZE 7

[ 51](structbt__addr__le__t.md#aacada5fc5b04ff22a02518e6f59387ed)

53typedef struct {

54 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__addr__le__t.md#aa4ede005c57893383a21983bc3e47958);

55 [bt\_addr\_t](structbt__addr__t.md) [a](structbt__addr__le__t.md#aacada5fc5b04ff22a02518e6f59387ed);

56} [bt\_addr\_le\_t](structbt__addr__le__t.md);

57

58/\* Global Bluetooth address constants defined in bluetooth/common/addr.c \*/

59extern const [bt\_addr\_t](structbt__addr__t.md) [bt\_addr\_any](group__bt__addr.md#gadd64afda1a14cbc2740f205e90169152);

60extern const [bt\_addr\_t](structbt__addr__t.md) [bt\_addr\_none](group__bt__addr.md#ga0b2f611fbd28b066d261b81303c4b93f);

[ 61](group__bt__addr.md#ga40ddc9769e38b7537bbb4e8002de592a)extern const [bt\_addr\_le\_t](structbt__addr__le__t.md) [bt\_addr\_le\_any](group__bt__addr.md#ga40c282f720d13b5d24a2dd62bfdceb73);

62extern const [bt\_addr\_le\_t](structbt__addr__le__t.md) [bt\_addr\_le\_none](group__bt__addr.md#gaefa17a553b6f8e9ad599e8db7538e1b8);

[ 63](group__bt__addr.md#gacb24d83ded350176fc96dfc0f5dde6be)

[ 65](group__bt__addr.md#ga17e9efacd50c682b2f709c217e920d48)#define BT\_ADDR\_ANY (&bt\_addr\_any)

[ 67](group__bt__addr.md#gadfcc0281e453cba990b623631c26f80b)#define BT\_ADDR\_NONE (&bt\_addr\_none)

69#define BT\_ADDR\_LE\_ANY (&bt\_addr\_le\_any)

71#define BT\_ADDR\_LE\_NONE (&bt\_addr\_le\_none)

72

[ 76](group__bt__addr.md#ga41ff9419098728f037c3e97d29c30ba9) \* @param b Second Bluetooth device address to compare

77 \*

78 \* @return negative value if @a a < @a b, 0 if @a a == @a b, else positive

79 \*/

80static inline int [bt\_addr\_cmp](group__bt__addr.md#ga41ff9419098728f037c3e97d29c30ba9)(const [bt\_addr\_t](structbt__addr__t.md) \*a, const [bt\_addr\_t](structbt__addr__t.md) \*b)

81{

82 return [memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(a, b, sizeof(\*a));

83}

84

[ 86](group__bt__addr.md#gadecf8fe8e183a11a4ff569bc0d673ec1) \*

87 \* @retval #true if the two addresses are equal

88 \* @retval #false otherwise

89 \*/

90static inline bool [bt\_addr\_eq](group__bt__addr.md#gadecf8fe8e183a11a4ff569bc0d673ec1)(const [bt\_addr\_t](structbt__addr__t.md) \*a, const [bt\_addr\_t](structbt__addr__t.md) \*b)

91{

92 return [bt\_addr\_cmp](group__bt__addr.md#ga41ff9419098728f037c3e97d29c30ba9)(a, b) == 0;

93}

94

[ 100](group__bt__addr.md#ga588d392f51372ff2951c3ff39da22f12) \* @return negative value if @a a < @a b, 0 if @a a == @a b, else positive

101 \*

102 \* @sa bt\_addr\_le\_eq

103 \*/

104static inline int [bt\_addr\_le\_cmp](group__bt__addr.md#ga588d392f51372ff2951c3ff39da22f12)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*a, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*b)

105{

106 return [memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(a, b, sizeof(\*a));

107}

108

[ 113](group__bt__addr.md#ga8644e77108f029088adb203e5392016b) \*

114 \* @retval #true if the two addresses are equal

115 \* @retval #false otherwise

116 \*/

117static inline bool [bt\_addr\_le\_eq](group__bt__addr.md#ga8644e77108f029088adb203e5392016b)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*a, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*b)

118{

119 return [bt\_addr\_le\_cmp](group__bt__addr.md#ga588d392f51372ff2951c3ff39da22f12)(a, b) == 0;

120}

121

[ 123](group__bt__addr.md#ga5a8284cf34d0835d725dab31d710ea4c) \*

124 \* @param dst Bluetooth device address destination buffer.

125 \* @param src Bluetooth device address source buffer.

126 \*/

127static inline void [bt\_addr\_copy](group__bt__addr.md#ga5a8284cf34d0835d725dab31d710ea4c)([bt\_addr\_t](structbt__addr__t.md) \*dst, const [bt\_addr\_t](structbt__addr__t.md) \*src)

128{

129 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(dst, src, sizeof(\*dst));

130}

131

[ 133](group__bt__addr.md#gac6c9b20f17936efaa082fe63aedc2138) \*

134 \* @param dst Bluetooth LE device address destination buffer.

135 \* @param src Bluetooth LE device address source buffer.

136 \*/

137static inline void [bt\_addr\_le\_copy](group__bt__addr.md#gac6c9b20f17936efaa082fe63aedc2138)([bt\_addr\_le\_t](structbt__addr__le__t.md) \*dst, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*src)

138{

[ 139](group__bt__addr.md#ga32abc1a2e827542efea5b9cb05a57fbc) [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(dst, src, sizeof(\*dst));

140}

141

143#define BT\_ADDR\_IS\_RPA(a) (((a)->val[5] & 0xc0) == 0x40)

146#define BT\_ADDR\_IS\_NRPA(a) (((a)->val[5] & 0xc0) == 0x00)

148#define BT\_ADDR\_IS\_STATIC(a) (((a)->val[5] & 0xc0) == 0xc0)

[ 149](group__bt__addr.md#ga6b23035316e9bdd071e10ecc803fcdbc)

[ 151](group__bt__addr.md#gaa6261bf0b96099b58f0a0c3674ce5713)#define BT\_ADDR\_SET\_RPA(a) ((a)->val[5] = (((a)->val[5] & 0x3f) | 0x40))

153#define BT\_ADDR\_SET\_NRPA(a) ((a)->val[5] &= 0x3f)

155#define BT\_ADDR\_SET\_STATIC(a) ((a)->val[5] |= 0xc0)

156

158int [bt\_addr\_le\_create\_nrpa](group__bt__addr.md#gaf2d38888131c9e8bdbc820b415c14082)([bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr);

159

161int [bt\_addr\_le\_create\_static](group__bt__addr.md#gad1b43f2f0ab58ec2c5ceaaa0d2cbc444)([bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr);

162

[ 166](group__bt__addr.md#ga42bcee6b5aadde7ccdbe243df25043bc) \* @param addr Bluetooth LE device address.

167 \*

168 \* @return true if address is a random private resolvable address.

169 \*/

170static inline bool [bt\_addr\_le\_is\_rpa](group__bt__addr.md#ga42bcee6b5aadde7ccdbe243df25043bc)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr)

171{

172 if (addr->[type](structbt__addr__le__t.md#aa4ede005c57893383a21983bc3e47958) != [BT\_ADDR\_LE\_RANDOM](group__bt__addr.md#ga6e81e967527b5418ee6cbc6d72c5aef9)) {

173 return false;

174 }

175

176 return [BT\_ADDR\_IS\_RPA](group__bt__addr.md#ga32abc1a2e827542efea5b9cb05a57fbc)(&addr->[a](structbt__addr__le__t.md#aacada5fc5b04ff22a02518e6f59387ed));

177}

178

[ 184](group__bt__addr.md#ga7a6acc7a9267ae2645aeee38e553b8b3) \* @param addr Bluetooth LE device address.

185 \*

186 \* @return true if address is a valid identity address.

187 \*/

188static inline bool [bt\_addr\_le\_is\_identity](group__bt__addr.md#ga7a6acc7a9267ae2645aeee38e553b8b3)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr)

189{

190 if (addr->[type](structbt__addr__le__t.md#aa4ede005c57893383a21983bc3e47958) == [BT\_ADDR\_LE\_PUBLIC](group__bt__addr.md#ga1717d2b4e61b28637be8a5f78685a3c4)) {

191 return true;

192 }

193

194 return [BT\_ADDR\_IS\_STATIC](group__bt__addr.md#ga0cb3aa4d48cf41d8485b570ef0e7447a)(&addr->[a](structbt__addr__le__t.md#aacada5fc5b04ff22a02518e6f59387ed));

195}

196

204#define BT\_ADDR\_STR\_LEN 18

205

213#define BT\_ADDR\_LE\_STR\_LEN 30

214

[ 221](group__bt__addr.md#ga151bdd0ada8635acfebd60f0e203cde2) \* BT\_ADDR\_STR\_LEN about recommended value.

222 \*

223 \* @return Number of successfully formatted bytes from binary address.

224 \*/

225static inline int [bt\_addr\_to\_str](group__bt__addr.md#ga151bdd0ada8635acfebd60f0e203cde2)(const [bt\_addr\_t](structbt__addr__t.md) \*addr, char \*str, size\_t len)

226{

227 return [snprintk](printk_8h.md#a0b0af71688f7e9170103d771d4e1eab2)(str, len, "%02X:%02X:%02X:%02X:%02X:%02X",

228 addr->[val](structbt__addr__t.md#a59e03c3fd06d16dc41132fd21ac42952)[5], addr->[val](structbt__addr__t.md#a59e03c3fd06d16dc41132fd21ac42952)[4], addr->[val](structbt__addr__t.md#a59e03c3fd06d16dc41132fd21ac42952)[3],

229 addr->[val](structbt__addr__t.md#a59e03c3fd06d16dc41132fd21ac42952)[2], addr->[val](structbt__addr__t.md#a59e03c3fd06d16dc41132fd21ac42952)[1], addr->[val](structbt__addr__t.md#a59e03c3fd06d16dc41132fd21ac42952)[0]);

230}

231

[ 238](group__bt__addr.md#ga74a644cd3de081a353a281d80b32b91e) \* BT\_ADDR\_LE\_STR\_LEN about recommended value.

239 \*

240 \* @return Number of successfully formatted bytes from binary address.

241 \*/

242static inline int [bt\_addr\_le\_to\_str](group__bt__addr.md#ga74a644cd3de081a353a281d80b32b91e)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, char \*str,

243 size\_t len)

244{

245 char type[10];

246

247 switch (addr->[type](structbt__addr__le__t.md#aa4ede005c57893383a21983bc3e47958)) {

248 case [BT\_ADDR\_LE\_PUBLIC](group__bt__addr.md#ga1717d2b4e61b28637be8a5f78685a3c4):

249 [strcpy](string_8h.md#a6d729a7b6396b8508060821c56f4adbc)(type, "public");

250 break;

251 case [BT\_ADDR\_LE\_RANDOM](group__bt__addr.md#ga6e81e967527b5418ee6cbc6d72c5aef9):

252 [strcpy](string_8h.md#a6d729a7b6396b8508060821c56f4adbc)(type, "random");

253 break;

254 case [BT\_ADDR\_LE\_PUBLIC\_ID](group__bt__addr.md#ga1fd60d5eb4c8a6d8f4df06eaba85fb96):

255 [strcpy](string_8h.md#a6d729a7b6396b8508060821c56f4adbc)(type, "public-id");

256 break;

257 case [BT\_ADDR\_LE\_RANDOM\_ID](group__bt__addr.md#gafdf2572991427d95bb44d1a5ee2ad85a):

258 [strcpy](string_8h.md#a6d729a7b6396b8508060821c56f4adbc)(type, "random-id");

259 break;

260 default:

261 [snprintk](printk_8h.md#a0b0af71688f7e9170103d771d4e1eab2)(type, sizeof(type), "0x%02x", addr->[type](structbt__addr__le__t.md#aa4ede005c57893383a21983bc3e47958));

262 break;

263 }

264

265 return [snprintk](printk_8h.md#a0b0af71688f7e9170103d771d4e1eab2)(str, len, "%02X:%02X:%02X:%02X:%02X:%02X (%s)",

266 addr->[a](structbt__addr__le__t.md#aacada5fc5b04ff22a02518e6f59387ed).[val](structbt__addr__t.md#a59e03c3fd06d16dc41132fd21ac42952)[5], addr->[a](structbt__addr__le__t.md#aacada5fc5b04ff22a02518e6f59387ed).[val](structbt__addr__t.md#a59e03c3fd06d16dc41132fd21ac42952)[4], addr->[a](structbt__addr__le__t.md#aacada5fc5b04ff22a02518e6f59387ed).[val](structbt__addr__t.md#a59e03c3fd06d16dc41132fd21ac42952)[3],

267 addr->[a](structbt__addr__le__t.md#aacada5fc5b04ff22a02518e6f59387ed).[val](structbt__addr__t.md#a59e03c3fd06d16dc41132fd21ac42952)[2], addr->[a](structbt__addr__le__t.md#aacada5fc5b04ff22a02518e6f59387ed).[val](structbt__addr__t.md#a59e03c3fd06d16dc41132fd21ac42952)[1], addr->[a](structbt__addr__le__t.md#aacada5fc5b04ff22a02518e6f59387ed).[val](structbt__addr__t.md#a59e03c3fd06d16dc41132fd21ac42952)[0], type);

268}

269

278int [bt\_addr\_from\_str](group__bt__addr.md#gad93410d0161ca84939f4bf983da29c14)(const char \*str, [bt\_addr\_t](structbt__addr__t.md) \*addr);

279

289int [bt\_addr\_le\_from\_str](group__bt__addr.md#ga2539a1ac8774587fb75702aac66f8e19)(const char \*str, const char \*type, [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr);

290

294

295#ifdef \_\_cplusplus

296}

297#endif

298

299#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_ADDR\_H\_ \*/

[bt\_addr\_none](group__bt__addr.md#ga0b2f611fbd28b066d261b81303c4b93f)

const bt\_addr\_t bt\_addr\_none

[BT\_ADDR\_IS\_STATIC](group__bt__addr.md#ga0cb3aa4d48cf41d8485b570ef0e7447a)

#define BT\_ADDR\_IS\_STATIC(a)

Check if a Bluetooth LE random address is a static address.

**Definition** addr.h:144

[bt\_addr\_to\_str](group__bt__addr.md#ga151bdd0ada8635acfebd60f0e203cde2)

static int bt\_addr\_to\_str(const bt\_addr\_t \*addr, char \*str, size\_t len)

Converts binary Bluetooth address to string.

**Definition** addr.h:221

[BT\_ADDR\_LE\_PUBLIC](group__bt__addr.md#ga1717d2b4e61b28637be8a5f78685a3c4)

#define BT\_ADDR\_LE\_PUBLIC

**Definition** addr.h:29

[BT\_ADDR\_LE\_PUBLIC\_ID](group__bt__addr.md#ga1fd60d5eb4c8a6d8f4df06eaba85fb96)

#define BT\_ADDR\_LE\_PUBLIC\_ID

**Definition** addr.h:31

[bt\_addr\_le\_from\_str](group__bt__addr.md#ga2539a1ac8774587fb75702aac66f8e19)

int bt\_addr\_le\_from\_str(const char \*str, const char \*type, bt\_addr\_le\_t \*addr)

Convert LE Bluetooth address from string to binary.

[BT\_ADDR\_IS\_RPA](group__bt__addr.md#ga32abc1a2e827542efea5b9cb05a57fbc)

#define BT\_ADDR\_IS\_RPA(a)

Check if a Bluetooth LE random address is resolvable private address.

**Definition** addr.h:139

[bt\_addr\_le\_any](group__bt__addr.md#ga40c282f720d13b5d24a2dd62bfdceb73)

const bt\_addr\_le\_t bt\_addr\_le\_any

[bt\_addr\_cmp](group__bt__addr.md#ga41ff9419098728f037c3e97d29c30ba9)

static int bt\_addr\_cmp(const bt\_addr\_t \*a, const bt\_addr\_t \*b)

Compare Bluetooth device addresses.

**Definition** addr.h:76

[bt\_addr\_le\_is\_rpa](group__bt__addr.md#ga42bcee6b5aadde7ccdbe243df25043bc)

static bool bt\_addr\_le\_is\_rpa(const bt\_addr\_le\_t \*addr)

Check if a Bluetooth LE address is a random private resolvable address.

**Definition** addr.h:166

[bt\_addr\_le\_cmp](group__bt__addr.md#ga588d392f51372ff2951c3ff39da22f12)

static int bt\_addr\_le\_cmp(const bt\_addr\_le\_t \*a, const bt\_addr\_le\_t \*b)

Compare Bluetooth LE device addresses.

**Definition** addr.h:100

[bt\_addr\_copy](group__bt__addr.md#ga5a8284cf34d0835d725dab31d710ea4c)

static void bt\_addr\_copy(bt\_addr\_t \*dst, const bt\_addr\_t \*src)

Copy Bluetooth device address.

**Definition** addr.h:123

[BT\_ADDR\_SIZE](group__bt__addr.md#ga6b6f56325b5136d2719f02eecc780d49)

#define BT\_ADDR\_SIZE

Length in bytes of a standard Bluetooth address.

**Definition** addr.h:37

[BT\_ADDR\_LE\_RANDOM](group__bt__addr.md#ga6e81e967527b5418ee6cbc6d72c5aef9)

#define BT\_ADDR\_LE\_RANDOM

**Definition** addr.h:30

[bt\_addr\_le\_to\_str](group__bt__addr.md#ga74a644cd3de081a353a281d80b32b91e)

static int bt\_addr\_le\_to\_str(const bt\_addr\_le\_t \*addr, char \*str, size\_t len)

Converts binary LE Bluetooth address to string.

**Definition** addr.h:238

[bt\_addr\_le\_is\_identity](group__bt__addr.md#ga7a6acc7a9267ae2645aeee38e553b8b3)

static bool bt\_addr\_le\_is\_identity(const bt\_addr\_le\_t \*addr)

Check if a Bluetooth LE address is valid identity address.

**Definition** addr.h:184

[bt\_addr\_le\_eq](group__bt__addr.md#ga8644e77108f029088adb203e5392016b)

static bool bt\_addr\_le\_eq(const bt\_addr\_le\_t \*a, const bt\_addr\_le\_t \*b)

Determine equality of two Bluetooth LE device addresses.

**Definition** addr.h:113

[bt\_addr\_le\_copy](group__bt__addr.md#gac6c9b20f17936efaa082fe63aedc2138)

static void bt\_addr\_le\_copy(bt\_addr\_le\_t \*dst, const bt\_addr\_le\_t \*src)

Copy Bluetooth LE device address.

**Definition** addr.h:133

[bt\_addr\_le\_create\_static](group__bt__addr.md#gad1b43f2f0ab58ec2c5ceaaa0d2cbc444)

int bt\_addr\_le\_create\_static(bt\_addr\_le\_t \*addr)

Create a Bluetooth LE random static address.

[bt\_addr\_from\_str](group__bt__addr.md#gad93410d0161ca84939f4bf983da29c14)

int bt\_addr\_from\_str(const char \*str, bt\_addr\_t \*addr)

Convert Bluetooth address from string to binary.

[bt\_addr\_any](group__bt__addr.md#gadd64afda1a14cbc2740f205e90169152)

const bt\_addr\_t bt\_addr\_any

[bt\_addr\_eq](group__bt__addr.md#gadecf8fe8e183a11a4ff569bc0d673ec1)

static bool bt\_addr\_eq(const bt\_addr\_t \*a, const bt\_addr\_t \*b)

Determine equality of two Bluetooth device addresses.

**Definition** addr.h:86

[bt\_addr\_le\_none](group__bt__addr.md#gaefa17a553b6f8e9ad599e8db7538e1b8)

const bt\_addr\_le\_t bt\_addr\_le\_none

[bt\_addr\_le\_create\_nrpa](group__bt__addr.md#gaf2d38888131c9e8bdbc820b415c14082)

int bt\_addr\_le\_create\_nrpa(bt\_addr\_le\_t \*addr)

Create a Bluetooth LE random non-resolvable private address.

[BT\_ADDR\_LE\_RANDOM\_ID](group__bt__addr.md#gafdf2572991427d95bb44d1a5ee2ad85a)

#define BT\_ADDR\_LE\_RANDOM\_ID

**Definition** addr.h:32

[printk.h](printk_8h.md)

[snprintk](printk_8h.md#a0b0af71688f7e9170103d771d4e1eab2)

int snprintk(char \*str, size\_t size, const char \*fmt,...)

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[string.h](string_8h.md)

[strcpy](string_8h.md#a6d729a7b6396b8508060821c56f4adbc)

char \* strcpy(char \*ZRESTRICT d, const char \*ZRESTRICT s)

[memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)

int memcmp(const void \*m1, const void \*m2, size\_t n)

[memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)

void \* memcpy(void \*ZRESTRICT d, const void \*ZRESTRICT s, size\_t n)

[bt\_addr\_le\_t](structbt__addr__le__t.md)

Bluetooth LE Device Address.

**Definition** addr.h:49

[bt\_addr\_le\_t::type](structbt__addr__le__t.md#aa4ede005c57893383a21983bc3e47958)

uint8\_t type

**Definition** addr.h:50

[bt\_addr\_le\_t::a](structbt__addr__le__t.md#aacada5fc5b04ff22a02518e6f59387ed)

bt\_addr\_t a

**Definition** addr.h:51

[bt\_addr\_t](structbt__addr__t.md)

Bluetooth Device Address.

**Definition** addr.h:40

[bt\_addr\_t::val](structbt__addr__t.md#a59e03c3fd06d16dc41132fd21ac42952)

uint8\_t val[6]

**Definition** addr.h:41

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [addr.h](addr_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

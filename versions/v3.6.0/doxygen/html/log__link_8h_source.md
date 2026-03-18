---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/log__link_8h_source.html
original_path: doxygen/html/log__link_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_link.h

[Go to the documentation of this file.](log__link_8h.md)

1/\*

2 \* Copyright (c) 2022 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_LOGGING\_LOG\_LINK\_H\_

7#define ZEPHYR\_INCLUDE\_LOGGING\_LOG\_LINK\_H\_

8

9#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

10#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

11#include <[zephyr/logging/log\_msg.h](include_2zephyr_2logging_2log__msg_8h.md)>

12#include <[zephyr/logging/log\_internal.h](log__internal_8h.md)>

13#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

25

26struct [log\_link](structlog__link.md);

27

[ 28](group__log__link.md#gadc72a0abf0311deb3bece478a43e5745)typedef void (\*[log\_link\_callback\_t](group__log__link.md#gadc72a0abf0311deb3bece478a43e5745))(const struct [log\_link](structlog__link.md) \*link,

29 union [log\_msg\_generic](unionlog__msg__generic.md) \*msg);

30

[ 31](group__log__link.md#ga63dc4a2ad58b754beb259d1748c8ab79)typedef void (\*[log\_link\_dropped\_cb\_t](group__log__link.md#ga63dc4a2ad58b754beb259d1748c8ab79))(const struct [log\_link](structlog__link.md) \*link,

32 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dropped);

33

[ 34](structlog__link__config.md)struct [log\_link\_config](structlog__link__config.md) {

[ 35](structlog__link__config.md#a84950437c5613a095620f6f5d2d20972) [log\_link\_callback\_t](group__log__link.md#gadc72a0abf0311deb3bece478a43e5745) [msg\_cb](structlog__link__config.md#a84950437c5613a095620f6f5d2d20972);

[ 36](structlog__link__config.md#a085cf099a0036d2a3a9f5c286cc788a1) [log\_link\_dropped\_cb\_t](group__log__link.md#ga63dc4a2ad58b754beb259d1748c8ab79) [dropped\_cb](structlog__link__config.md#a085cf099a0036d2a3a9f5c286cc788a1);

37};

38

[ 39](structlog__link__api.md)struct [log\_link\_api](structlog__link__api.md) {

[ 40](structlog__link__api.md#a82eb7351ca56f7b7f4215f5188697e29) int (\*[initiate](structlog__link__api.md#a82eb7351ca56f7b7f4215f5188697e29))(const struct [log\_link](structlog__link.md) \*link, struct [log\_link\_config](structlog__link__config.md) \*config);

[ 41](structlog__link__api.md#a153036e50cbab5c9bf4e62aeee5b3361) int (\*[activate](structlog__link__api.md#a153036e50cbab5c9bf4e62aeee5b3361))(const struct [log\_link](structlog__link.md) \*link);

[ 42](structlog__link__api.md#a7c08926ee7f33796c9627ede345a02dc) int (\*[get\_domain\_name](structlog__link__api.md#a7c08926ee7f33796c9627ede345a02dc))(const struct [log\_link](structlog__link.md) \*link, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id,

43 char \*buf, size\_t \*length);

[ 44](structlog__link__api.md#a1f770c5f70d77aa69b825a91df15f5bc) int (\*[get\_source\_name](structlog__link__api.md#a1f770c5f70d77aa69b825a91df15f5bc))(const struct [log\_link](structlog__link.md) \*link, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id,

45 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) source\_id, char \*buf, size\_t \*length);

[ 46](structlog__link__api.md#ae09ac3bf464a5372d8161c36f881906e) int (\*[get\_levels](structlog__link__api.md#ae09ac3bf464a5372d8161c36f881906e))(const struct [log\_link](structlog__link.md) \*link, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id,

47 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) source\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*level,

48 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*runtime\_level);

[ 49](structlog__link__api.md#a994ea743a12677bdd4bf2d1eb51e6331) int (\*[set\_runtime\_level](structlog__link__api.md#a994ea743a12677bdd4bf2d1eb51e6331))(const struct [log\_link](structlog__link.md) \*link, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id,

50 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) source\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level);

51};

52

[ 53](structlog__link__ctrl__blk.md)struct [log\_link\_ctrl\_blk](structlog__link__ctrl__blk.md) {

[ 54](structlog__link__ctrl__blk.md#a96eab52ab1863b8d9e9b2570d9fd9808) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [domain\_cnt](structlog__link__ctrl__blk.md#a96eab52ab1863b8d9e9b2570d9fd9808);

[ 55](structlog__link__ctrl__blk.md#a5c443cba449be55477220dcd350c6a68) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [source\_cnt](structlog__link__ctrl__blk.md#a5c443cba449be55477220dcd350c6a68)[1 + [COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(CONFIG\_LOG\_MULTIDOMAIN,

56 (CONFIG\_LOG\_REMOTE\_DOMAIN\_MAX\_COUNT),

57 (0))];

[ 58](structlog__link__ctrl__blk.md#a6fe49a96b5b9d79f641125e43c67ba50) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [domain\_offset](structlog__link__ctrl__blk.md#a6fe49a96b5b9d79f641125e43c67ba50);

[ 59](structlog__link__ctrl__blk.md#a3352b5f8f8ee8b78825db1216c60aa0d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[filters](structlog__link__ctrl__blk.md#a3352b5f8f8ee8b78825db1216c60aa0d);

60};

61

[ 62](structlog__link.md)struct [log\_link](structlog__link.md) {

[ 63](structlog__link.md#a1df7a4c08d3488a68b7058a018c92e46) const struct [log\_link\_api](structlog__link__api.md) \*[api](structlog__link.md#a1df7a4c08d3488a68b7058a018c92e46);

[ 64](structlog__link.md#a46a2eafdb546ec8a5f7b5fc9102121c7) const char \*[name](structlog__link.md#a46a2eafdb546ec8a5f7b5fc9102121c7);

[ 65](structlog__link.md#aaa4f473c397f6b90d73b395a62cfbc7e) struct [log\_link\_ctrl\_blk](structlog__link__ctrl__blk.md) \*[ctrl\_blk](structlog__link.md#aaa4f473c397f6b90d73b395a62cfbc7e);

[ 66](structlog__link.md#a1a1adfb2d621ba37d2dd8c814fce659e) void \*[ctx](structlog__link.md#a1a1adfb2d621ba37d2dd8c814fce659e);

[ 67](structlog__link.md#ae06e6147fc50e18a277b3610016c10a8) struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*[mpsc\_pbuf](structlog__link.md#ae06e6147fc50e18a277b3610016c10a8);

[ 68](structlog__link.md#a312ff38285a989e56d6f59b9bc1429cf) const struct [mpsc\_pbuf\_buffer\_config](structmpsc__pbuf__buffer__config.md) \*[mpsc\_pbuf\_config](structlog__link.md#a312ff38285a989e56d6f59b9bc1429cf);

69};

70

[ 86](group__log__link.md#ga9cf22f4fc8fb8c964396d6502fb20522)#define LOG\_LINK\_DEF(\_name, \_api, \_buf\_wlen, \_ctx) \

87 static uint32\_t \_\_aligned(Z\_LOG\_MSG\_ALIGNMENT) \_name##\_buf32[\_buf\_wlen]; \

88 static const struct mpsc\_pbuf\_buffer\_config \_name##\_mpsc\_pbuf\_config = { \

89 .buf = (uint32\_t \*)\_name##\_buf32, \

90 .size = \_buf\_wlen, \

91 .notify\_drop = z\_log\_notify\_drop, \

92 .get\_wlen = log\_msg\_generic\_get\_wlen, \

93 .flags = IS\_ENABLED(CONFIG\_LOG\_MODE\_OVERFLOW) ? \

94 MPSC\_PBUF\_MODE\_OVERWRITE : 0 \

95 }; \

96 COND\_CODE\_0(\_buf\_wlen, (), (static STRUCT\_SECTION\_ITERABLE(log\_msg\_ptr, \

97 \_name##\_log\_msg\_ptr);)) \

98 static STRUCT\_SECTION\_ITERABLE\_ALTERNATE(log\_mpsc\_pbuf, \

99 mpsc\_pbuf\_buffer, \

100 \_name##\_log\_mpsc\_pbuf); \

101 static struct log\_link\_ctrl\_blk \_name##\_ctrl\_blk; \

102 static const STRUCT\_SECTION\_ITERABLE(log\_link, \_name) = \

103 { \

104 .api = &\_api, \

105 .name = STRINGIFY(\_name), \

106 .ctrl\_blk = &\_name##\_ctrl\_blk, \

107 .ctx = \_ctx, \

108 .mpsc\_pbuf = \_buf\_wlen ? &\_name##\_log\_mpsc\_pbuf : NULL, \

109 .mpsc\_pbuf\_config = \_buf\_wlen ? &\_name##\_mpsc\_pbuf\_config : NULL \

110 }

111

[ 123](group__log__link.md#gaff08dcc178a95e3a1e28aeba7ccfe189)static inline int [log\_link\_initiate](group__log__link.md#gaff08dcc178a95e3a1e28aeba7ccfe189)(const struct [log\_link](structlog__link.md) \*link,

124 struct [log\_link\_config](structlog__link__config.md) \*config)

125{

126 \_\_ASSERT\_NO\_MSG(link);

127

128 return link->[api](structlog__link.md#a1df7a4c08d3488a68b7058a018c92e46)->[initiate](structlog__link__api.md#a82eb7351ca56f7b7f4215f5188697e29)(link, config);

129}

130

[ 142](group__log__link.md#ga5659a791d3336f05bc614b31ba2ce798)static inline int [log\_link\_activate](group__log__link.md#ga5659a791d3336f05bc614b31ba2ce798)(const struct [log\_link](structlog__link.md) \*link)

143{

144 \_\_ASSERT\_NO\_MSG(link);

145

146 return link->[api](structlog__link.md#a1df7a4c08d3488a68b7058a018c92e46)->[activate](structlog__link__api.md#a153036e50cbab5c9bf4e62aeee5b3361)(link);

147}

148

[ 156](group__log__link.md#ga855a02a7a3282ca85e0f44004e924bc3)static inline int [log\_link\_is\_active](group__log__link.md#ga855a02a7a3282ca85e0f44004e924bc3)(const struct [log\_link](structlog__link.md) \*link)

157{

158 return link->[ctrl\_blk](structlog__link.md#aaa4f473c397f6b90d73b395a62cfbc7e)->[domain\_offset](structlog__link__ctrl__blk.md#a6fe49a96b5b9d79f641125e43c67ba50) > 0 ? 0 : -[EINPROGRESS](group__system__errno.md#ga6c045d5be06e715cc335784a7320714e);

159}

160

[ 167](group__log__link.md#gac8f066b2a0509935ef2c3f950928495a)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [log\_link\_domains\_count](group__log__link.md#gac8f066b2a0509935ef2c3f950928495a)(const struct [log\_link](structlog__link.md) \*link)

168{

169 \_\_ASSERT\_NO\_MSG(link);

170

171 return link->[ctrl\_blk](structlog__link.md#aaa4f473c397f6b90d73b395a62cfbc7e)->[domain\_cnt](structlog__link__ctrl__blk.md#a96eab52ab1863b8d9e9b2570d9fd9808);

172}

173

[ 181](group__log__link.md#ga694e4b69f46f1dbd6d1cda9a7d4cf3c4)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [log\_link\_sources\_count](group__log__link.md#ga694e4b69f46f1dbd6d1cda9a7d4cf3c4)(const struct [log\_link](structlog__link.md) \*link,

182 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id)

183{

184 \_\_ASSERT\_NO\_MSG(link);

185

186 return link->[ctrl\_blk](structlog__link.md#aaa4f473c397f6b90d73b395a62cfbc7e)->[source\_cnt](structlog__link__ctrl__blk.md#a5c443cba449be55477220dcd350c6a68)[domain\_id];

187}

188

[ 201](group__log__link.md#ga3aa0a15b8dbb52fb3550826277801835)static inline int [log\_link\_get\_domain\_name](group__log__link.md#ga3aa0a15b8dbb52fb3550826277801835)(const struct [log\_link](structlog__link.md) \*link,

202 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, char \*[buf](structmpsc__pbuf__buffer__config.md#a2090b3da5dc85c68601fd7bdb54f6174),

203 size\_t \*length)

204{

205 \_\_ASSERT\_NO\_MSG(link);

206

207 return link->[api](structlog__link.md#a1df7a4c08d3488a68b7058a018c92e46)->[get\_domain\_name](structlog__link__api.md#a7c08926ee7f33796c9627ede345a02dc)(link, domain\_id, [buf](structmpsc__pbuf__buffer__config.md#a2090b3da5dc85c68601fd7bdb54f6174), length);

208}

209

[ 222](group__log__link.md#gad097d791057b9826aa7f2c4077506673)static inline int [log\_link\_get\_source\_name](group__log__link.md#gad097d791057b9826aa7f2c4077506673)(const struct [log\_link](structlog__link.md) \*link,

223 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) source\_id,

224 char \*[buf](structmpsc__pbuf__buffer__config.md#a2090b3da5dc85c68601fd7bdb54f6174), size\_t \*length)

225{

226 \_\_ASSERT\_NO\_MSG(link);

227 \_\_ASSERT\_NO\_MSG([buf](structmpsc__pbuf__buffer__config.md#a2090b3da5dc85c68601fd7bdb54f6174));

228

229 return link->[api](structlog__link.md#a1df7a4c08d3488a68b7058a018c92e46)->[get\_source\_name](structlog__link__api.md#a1f770c5f70d77aa69b825a91df15f5bc)(link, domain\_id, source\_id,

230 [buf](structmpsc__pbuf__buffer__config.md#a2090b3da5dc85c68601fd7bdb54f6174), length);

231}

232

[ 243](group__log__link.md#ga2fc15a236cdf8dd0193df9754394d5db)static inline int [log\_link\_get\_levels](group__log__link.md#ga2fc15a236cdf8dd0193df9754394d5db)(const struct [log\_link](structlog__link.md) \*link,

244 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) source\_id,

245 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*level, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*runtime\_level)

246{

247 \_\_ASSERT\_NO\_MSG(link);

248

249 return link->[api](structlog__link.md#a1df7a4c08d3488a68b7058a018c92e46)->[get\_levels](structlog__link__api.md#ae09ac3bf464a5372d8161c36f881906e)(link, domain\_id, source\_id,

250 level, runtime\_level);

251}

252

[ 262](group__log__link.md#ga56655f534c45dbc777b1500bafd9a0d7)static inline int [log\_link\_set\_runtime\_level](group__log__link.md#ga56655f534c45dbc777b1500bafd9a0d7)(const struct [log\_link](structlog__link.md) \*link,

263 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) source\_id,

264 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level)

265{

266 \_\_ASSERT\_NO\_MSG(link);

267 \_\_ASSERT\_NO\_MSG(level);

268

269 return link->[api](structlog__link.md#a1df7a4c08d3488a68b7058a018c92e46)->[set\_runtime\_level](structlog__link__api.md#a994ea743a12677bdd4bf2d1eb51e6331)(link, domain\_id, source\_id, level);

270}

271

282void z\_log\_msg\_enqueue(const struct [log\_link](structlog__link.md) \*link, const void \*data, size\_t len);

283

287

288#ifdef \_\_cplusplus

289}

290#endif

291

292#endif /\* ZEPHYR\_INCLUDE\_LOGGING\_LOG\_LINK\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[log\_link\_get\_levels](group__log__link.md#ga2fc15a236cdf8dd0193df9754394d5db)

static int log\_link\_get\_levels(const struct log\_link \*link, uint32\_t domain\_id, uint16\_t source\_id, uint8\_t \*level, uint8\_t \*runtime\_level)

Get level settings of the given source.

**Definition** log\_link.h:243

[log\_link\_get\_domain\_name](group__log__link.md#ga3aa0a15b8dbb52fb3550826277801835)

static int log\_link\_get\_domain\_name(const struct log\_link \*link, uint32\_t domain\_id, char \*buf, size\_t \*length)

Get domain name.

**Definition** log\_link.h:201

[log\_link\_activate](group__log__link.md#ga5659a791d3336f05bc614b31ba2ce798)

static int log\_link\_activate(const struct log\_link \*link)

Activate log link.

**Definition** log\_link.h:142

[log\_link\_set\_runtime\_level](group__log__link.md#ga56655f534c45dbc777b1500bafd9a0d7)

static int log\_link\_set\_runtime\_level(const struct log\_link \*link, uint32\_t domain\_id, uint16\_t source\_id, uint8\_t level)

Set runtime level of the given source.

**Definition** log\_link.h:262

[log\_link\_dropped\_cb\_t](group__log__link.md#ga63dc4a2ad58b754beb259d1748c8ab79)

void(\* log\_link\_dropped\_cb\_t)(const struct log\_link \*link, uint32\_t dropped)

**Definition** log\_link.h:31

[log\_link\_sources\_count](group__log__link.md#ga694e4b69f46f1dbd6d1cda9a7d4cf3c4)

static uint16\_t log\_link\_sources\_count(const struct log\_link \*link, uint32\_t domain\_id)

Get number of sources in the domain.

**Definition** log\_link.h:181

[log\_link\_is\_active](group__log__link.md#ga855a02a7a3282ca85e0f44004e924bc3)

static int log\_link\_is\_active(const struct log\_link \*link)

Check if link is activated.

**Definition** log\_link.h:156

[log\_link\_domains\_count](group__log__link.md#gac8f066b2a0509935ef2c3f950928495a)

static uint8\_t log\_link\_domains\_count(const struct log\_link \*link)

Get number of domains in the link.

**Definition** log\_link.h:167

[log\_link\_get\_source\_name](group__log__link.md#gad097d791057b9826aa7f2c4077506673)

static int log\_link\_get\_source\_name(const struct log\_link \*link, uint32\_t domain\_id, uint16\_t source\_id, char \*buf, size\_t \*length)

Get source name.

**Definition** log\_link.h:222

[log\_link\_callback\_t](group__log__link.md#gadc72a0abf0311deb3bece478a43e5745)

void(\* log\_link\_callback\_t)(const struct log\_link \*link, union log\_msg\_generic \*msg)

**Definition** log\_link.h:28

[log\_link\_initiate](group__log__link.md#gaff08dcc178a95e3a1e28aeba7ccfe189)

static int log\_link\_initiate(const struct log\_link \*link, struct log\_link\_config \*config)

Initiate log link.

**Definition** log\_link.h:123

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:179

[EINPROGRESS](group__system__errno.md#ga6c045d5be06e715cc335784a7320714e)

#define EINPROGRESS

Operation now in progress.

**Definition** errno.h:104

[log\_msg.h](include_2zephyr_2logging_2log__msg_8h.md)

[types.h](include_2zephyr_2types_8h.md)

[log\_internal.h](log__internal_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[log\_link\_api](structlog__link__api.md)

**Definition** log\_link.h:39

[log\_link\_api::activate](structlog__link__api.md#a153036e50cbab5c9bf4e62aeee5b3361)

int(\* activate)(const struct log\_link \*link)

**Definition** log\_link.h:41

[log\_link\_api::get\_source\_name](structlog__link__api.md#a1f770c5f70d77aa69b825a91df15f5bc)

int(\* get\_source\_name)(const struct log\_link \*link, uint32\_t domain\_id, uint16\_t source\_id, char \*buf, size\_t \*length)

**Definition** log\_link.h:44

[log\_link\_api::get\_domain\_name](structlog__link__api.md#a7c08926ee7f33796c9627ede345a02dc)

int(\* get\_domain\_name)(const struct log\_link \*link, uint32\_t domain\_id, char \*buf, size\_t \*length)

**Definition** log\_link.h:42

[log\_link\_api::initiate](structlog__link__api.md#a82eb7351ca56f7b7f4215f5188697e29)

int(\* initiate)(const struct log\_link \*link, struct log\_link\_config \*config)

**Definition** log\_link.h:40

[log\_link\_api::set\_runtime\_level](structlog__link__api.md#a994ea743a12677bdd4bf2d1eb51e6331)

int(\* set\_runtime\_level)(const struct log\_link \*link, uint32\_t domain\_id, uint16\_t source\_id, uint8\_t level)

**Definition** log\_link.h:49

[log\_link\_api::get\_levels](structlog__link__api.md#ae09ac3bf464a5372d8161c36f881906e)

int(\* get\_levels)(const struct log\_link \*link, uint32\_t domain\_id, uint16\_t source\_id, uint8\_t \*level, uint8\_t \*runtime\_level)

**Definition** log\_link.h:46

[log\_link\_config](structlog__link__config.md)

**Definition** log\_link.h:34

[log\_link\_config::dropped\_cb](structlog__link__config.md#a085cf099a0036d2a3a9f5c286cc788a1)

log\_link\_dropped\_cb\_t dropped\_cb

**Definition** log\_link.h:36

[log\_link\_config::msg\_cb](structlog__link__config.md#a84950437c5613a095620f6f5d2d20972)

log\_link\_callback\_t msg\_cb

**Definition** log\_link.h:35

[log\_link\_ctrl\_blk](structlog__link__ctrl__blk.md)

**Definition** log\_link.h:53

[log\_link\_ctrl\_blk::filters](structlog__link__ctrl__blk.md#a3352b5f8f8ee8b78825db1216c60aa0d)

uint32\_t \* filters

**Definition** log\_link.h:59

[log\_link\_ctrl\_blk::source\_cnt](structlog__link__ctrl__blk.md#a5c443cba449be55477220dcd350c6a68)

uint16\_t source\_cnt[1+COND\_CODE\_1(CONFIG\_LOG\_MULTIDOMAIN,(CONFIG\_LOG\_REMOTE\_DOMAIN\_MAX\_COUNT),(0))]

**Definition** log\_link.h:57

[log\_link\_ctrl\_blk::domain\_offset](structlog__link__ctrl__blk.md#a6fe49a96b5b9d79f641125e43c67ba50)

uint32\_t domain\_offset

**Definition** log\_link.h:58

[log\_link\_ctrl\_blk::domain\_cnt](structlog__link__ctrl__blk.md#a96eab52ab1863b8d9e9b2570d9fd9808)

uint32\_t domain\_cnt

**Definition** log\_link.h:54

[log\_link](structlog__link.md)

**Definition** log\_link.h:62

[log\_link::ctx](structlog__link.md#a1a1adfb2d621ba37d2dd8c814fce659e)

void \* ctx

**Definition** log\_link.h:66

[log\_link::api](structlog__link.md#a1df7a4c08d3488a68b7058a018c92e46)

const struct log\_link\_api \* api

**Definition** log\_link.h:63

[log\_link::mpsc\_pbuf\_config](structlog__link.md#a312ff38285a989e56d6f59b9bc1429cf)

const struct mpsc\_pbuf\_buffer\_config \* mpsc\_pbuf\_config

**Definition** log\_link.h:68

[log\_link::name](structlog__link.md#a46a2eafdb546ec8a5f7b5fc9102121c7)

const char \* name

**Definition** log\_link.h:64

[log\_link::ctrl\_blk](structlog__link.md#aaa4f473c397f6b90d73b395a62cfbc7e)

struct log\_link\_ctrl\_blk \* ctrl\_blk

**Definition** log\_link.h:65

[log\_link::mpsc\_pbuf](structlog__link.md#ae06e6147fc50e18a277b3610016c10a8)

struct mpsc\_pbuf\_buffer \* mpsc\_pbuf

**Definition** log\_link.h:67

[mpsc\_pbuf\_buffer\_config](structmpsc__pbuf__buffer__config.md)

MPSC packet buffer configuration.

**Definition** mpsc\_pbuf.h:131

[mpsc\_pbuf\_buffer\_config::buf](structmpsc__pbuf__buffer__config.md#a2090b3da5dc85c68601fd7bdb54f6174)

uint32\_t \* buf

**Definition** mpsc\_pbuf.h:133

[mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md)

MPSC packet buffer structure.

**Definition** mpsc\_pbuf.h:90

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[log\_msg\_generic](unionlog__msg__generic.md)

**Definition** log\_msg.h:117

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_link.h](log__link_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

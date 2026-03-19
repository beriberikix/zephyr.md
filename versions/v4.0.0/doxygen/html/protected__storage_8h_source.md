---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/protected__storage_8h_source.html
original_path: doxygen/html/protected__storage_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

protected\_storage.h

[Go to the documentation of this file.](protected__storage_8h.md)

1/\* Copyright (c) 2024 Nordic Semiconductor

2 \* SPDX-License-Identifier: Apache-2.0

3 \*/

4#ifndef PSA\_PROTECTED\_STORAGE\_H

5#define PSA\_PROTECTED\_STORAGE\_H

6

11

13#ifdef CONFIG\_SECURE\_STORAGE\_PS\_IMPLEMENTATION\_ITS

14#include "[../internal/zephyr/secure\_storage/its.h](its_8h.md)"

15#define ITS\_UID (secure\_storage\_its\_uid\_t){.uid = uid, \

16 .caller\_id = SECURE\_STORAGE\_ITS\_CALLER\_PSA\_PS}

17#else

18#include "[../internal/zephyr/secure\_storage/ps.h](ps_8h.md)"

19#endif

21

22#include <[psa/storage\_common.h](storage__common_8h.md)>

23

[ 24](protected__storage_8h.md#a97b66d0647ab7536fba2d6267e8fccef)#define PSA\_PS\_API\_VERSION\_MAJOR 1

[ 25](protected__storage_8h.md#adf9faa1eb9f9ed6fa8595c6718f89a5d)#define PSA\_PS\_API\_VERSION\_MINOR 0

26

47static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 49](protected__storage_8h.md#ac27f8fc33b69e0a9ed09b73195b42eab)[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) [psa\_ps\_set](protected__storage_8h.md#ac27f8fc33b69e0a9ed09b73195b42eab)([psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid, size\_t data\_length,

50 const void \*p\_data, [psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211) create\_flags)

51{

52#ifdef CONFIG\_SECURE\_STORAGE\_PS\_IMPLEMENTATION\_ITS

53 return [secure\_storage\_its\_set](its_8h.md#a3d6f3a7b47866ebcbfe9eb4a5ca99758)(ITS\_UID, data\_length, p\_data, create\_flags);

54#else

55 return [secure\_storage\_ps\_set](ps_8h.md#ab0be3c9374c1db65b45c43fdc6c05825)(uid, data\_length, p\_data, create\_flags);

56#endif

57}

58

80static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 82](protected__storage_8h.md#a2ad1b8347d8cf174c028f0c485a66db6)[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) [psa\_ps\_get](protected__storage_8h.md#a2ad1b8347d8cf174c028f0c485a66db6)([psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid, size\_t data\_offset,

83 size\_t data\_size, void \*p\_data, size\_t \*p\_data\_length)

84{

85#ifdef CONFIG\_SECURE\_STORAGE\_PS\_IMPLEMENTATION\_ITS

86 return [secure\_storage\_its\_get](its_8h.md#a806bb5b9698a0f90b80b294d5f44645e)(ITS\_UID, data\_offset, data\_size, p\_data, p\_data\_length);

87#else

88 return [secure\_storage\_ps\_get](ps_8h.md#a0387828802c41350b9572a1555ecdeac)(uid, data\_offset, data\_size, p\_data, p\_data\_length);

89#endif

90}

91

108static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 110](protected__storage_8h.md#af716b24d0761837d1c7b70042bd4966f)[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) [psa\_ps\_get\_info](protected__storage_8h.md#af716b24d0761837d1c7b70042bd4966f)([psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid, struct [psa\_storage\_info\_t](structpsa__storage__info__t.md) \*p\_info)

111{

112#ifdef CONFIG\_SECURE\_STORAGE\_PS\_IMPLEMENTATION\_ITS

113 return [secure\_storage\_its\_get\_info](its_8h.md#a8588925b41cf848d473a7e50087df606)(ITS\_UID, p\_info);

114#else

115 return [secure\_storage\_ps\_get\_info](ps_8h.md#af6c6741b58d91798e2a9c2b3644f0bf1)(uid, p\_info);

116#endif

117}

118

136static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 138](protected__storage_8h.md#a147a92d8387de36c32a8ede10d6d9a02)[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) [psa\_ps\_remove](protected__storage_8h.md#a147a92d8387de36c32a8ede10d6d9a02)([psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid)

139{

140#ifdef CONFIG\_SECURE\_STORAGE\_PS\_IMPLEMENTATION\_ITS

141 return [secure\_storage\_its\_remove](its_8h.md#a2d3337b1eb55deda25a8c75ea8d74ff5)(ITS\_UID);

142#else

143 return [secure\_storage\_ps\_remove](ps_8h.md#aef4fa69c85d80640a909868ad1749e8c)(uid);

144#endif

145}

146

170static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 172](protected__storage_8h.md#aa2c4d67afd77676a95becad71e902508)[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) [psa\_ps\_create](protected__storage_8h.md#aa2c4d67afd77676a95becad71e902508)([psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid, size\_t capacity,

173 [psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211) create\_flags)

174{

175#ifdef CONFIG\_SECURE\_STORAGE\_PS\_SUPPORTS\_SET\_EXTENDED

176 return [secure\_storage\_ps\_create](ps_8h.md#ae044a9d36445840539578b9ea3a1e4d0)(uid, capacity, create\_flags);

177#else

178 return [PSA\_ERROR\_NOT\_SUPPORTED](subsys_2secure__storage_2include_2psa_2error_8h.md#a1dcc6d130633ed5db8942257581b55dd);

179#endif

180}

181

208static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 210](protected__storage_8h.md#a1630b75fce6941c4d619256822d5de9a)[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) [psa\_ps\_set\_extended](protected__storage_8h.md#a1630b75fce6941c4d619256822d5de9a)([psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid, size\_t data\_offset,

211 size\_t data\_length, const void \*p\_data)

212{

213#ifdef CONFIG\_SECURE\_STORAGE\_PS\_SUPPORTS\_SET\_EXTENDED

214 return [secure\_storage\_ps\_set\_extended](ps_8h.md#ab1612b91d341295578e16eb64d7035c4)(uid, data\_offset, data\_length, p\_data);

215#else

216 return [PSA\_ERROR\_NOT\_SUPPORTED](subsys_2secure__storage_2include_2psa_2error_8h.md#a1dcc6d130633ed5db8942257581b55dd);

217#endif

218}

219

227static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 229](protected__storage_8h.md#a7e1725cb412be305bd21e3e1af8c2312)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [psa\_ps\_get\_support](protected__storage_8h.md#a7e1725cb412be305bd21e3e1af8c2312)(void)

230{

231 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) = 0;

232

233#ifdef CONFIG\_SECURE\_STORAGE\_PS\_SUPPORTS\_SET\_EXTENDED

234 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) |= [PSA\_STORAGE\_SUPPORT\_SET\_EXTENDED](storage__common_8h.md#ad9f16fc478036752ffb2ce9e50b2a710);

235#endif

236 return [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

237}

238

239#undef ITS\_UID

240

241#endif

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[its.h](its_8h.md)

The secure storage ITS implementation.

[secure\_storage\_its\_remove](its_8h.md#a2d3337b1eb55deda25a8c75ea8d74ff5)

psa\_status\_t secure\_storage\_its\_remove(secure\_storage\_its\_uid\_t uid)

See psa\_its\_remove(), to which this function is analogous.

[secure\_storage\_its\_set](its_8h.md#a3d6f3a7b47866ebcbfe9eb4a5ca99758)

psa\_status\_t secure\_storage\_its\_set(secure\_storage\_its\_uid\_t uid, size\_t data\_length, const void \*p\_data, psa\_storage\_create\_flags\_t create\_flags)

See psa\_its\_set(), to which this function is analogous.

[secure\_storage\_its\_get](its_8h.md#a806bb5b9698a0f90b80b294d5f44645e)

psa\_status\_t secure\_storage\_its\_get(secure\_storage\_its\_uid\_t uid, size\_t data\_offset, size\_t data\_size, void \*p\_data, size\_t \*p\_data\_length)

See psa\_its\_get(), to which this function is analogous.

[secure\_storage\_its\_get\_info](its_8h.md#a8588925b41cf848d473a7e50087df606)

psa\_status\_t secure\_storage\_its\_get\_info(secure\_storage\_its\_uid\_t uid, struct psa\_storage\_info\_t \*p\_info)

See psa\_its\_get\_info(), to which this function is analogous.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[psa\_ps\_remove](protected__storage_8h.md#a147a92d8387de36c32a8ede10d6d9a02)

psa\_status\_t psa\_ps\_remove(psa\_storage\_uid\_t uid)

Removes the provided uid and its associated data.

**Definition** protected\_storage.h:138

[psa\_ps\_set\_extended](protected__storage_8h.md#a1630b75fce6941c4d619256822d5de9a)

psa\_status\_t psa\_ps\_set\_extended(psa\_storage\_uid\_t uid, size\_t data\_offset, size\_t data\_length, const void \*p\_data)

Writes part of the data associated with the provided uid.

**Definition** protected\_storage.h:210

[psa\_ps\_get](protected__storage_8h.md#a2ad1b8347d8cf174c028f0c485a66db6)

psa\_status\_t psa\_ps\_get(psa\_storage\_uid\_t uid, size\_t data\_offset, size\_t data\_size, void \*p\_data, size\_t \*p\_data\_length)

Retrieves data associated with the provided uid.

**Definition** protected\_storage.h:82

[psa\_ps\_get\_support](protected__storage_8h.md#a7e1725cb412be305bd21e3e1af8c2312)

uint32\_t psa\_ps\_get\_support(void)

Lists optional features.

**Definition** protected\_storage.h:229

[psa\_ps\_create](protected__storage_8h.md#aa2c4d67afd77676a95becad71e902508)

psa\_status\_t psa\_ps\_create(psa\_storage\_uid\_t uid, size\_t capacity, psa\_storage\_create\_flags\_t create\_flags)

Reserves storage for the provided uid.

**Definition** protected\_storage.h:172

[psa\_ps\_set](protected__storage_8h.md#ac27f8fc33b69e0a9ed09b73195b42eab)

psa\_status\_t psa\_ps\_set(psa\_storage\_uid\_t uid, size\_t data\_length, const void \*p\_data, psa\_storage\_create\_flags\_t create\_flags)

Creates a new or modifies an existing entry.

**Definition** protected\_storage.h:49

[psa\_ps\_get\_info](protected__storage_8h.md#af716b24d0761837d1c7b70042bd4966f)

psa\_status\_t psa\_ps\_get\_info(psa\_storage\_uid\_t uid, struct psa\_storage\_info\_t \*p\_info)

Retrieves the metadata of a given entry.

**Definition** protected\_storage.h:110

[ps.h](ps_8h.md)

The secure storage PS implementation.

[secure\_storage\_ps\_get](ps_8h.md#a0387828802c41350b9572a1555ecdeac)

psa\_status\_t secure\_storage\_ps\_get(const psa\_storage\_uid\_t uid, size\_t data\_offset, size\_t data\_length, void \*p\_data, size\_t \*p\_data\_length)

See psa\_ps\_get(), to which this function is analogous.

[secure\_storage\_ps\_set](ps_8h.md#ab0be3c9374c1db65b45c43fdc6c05825)

psa\_status\_t secure\_storage\_ps\_set(const psa\_storage\_uid\_t uid, size\_t data\_length, const void \*p\_data, psa\_storage\_create\_flags\_t create\_flags)

See psa\_ps\_set(), to which this function is analogous.

[secure\_storage\_ps\_set\_extended](ps_8h.md#ab1612b91d341295578e16eb64d7035c4)

psa\_status\_t secure\_storage\_ps\_set\_extended(psa\_storage\_uid\_t uid, size\_t data\_offset, size\_t data\_length, const void \*p\_data)

See psa\_ps\_set\_extended(), to which this function is analogous.

[secure\_storage\_ps\_create](ps_8h.md#ae044a9d36445840539578b9ea3a1e4d0)

psa\_status\_t secure\_storage\_ps\_create(psa\_storage\_uid\_t uid, size\_t capacity, psa\_storage\_create\_flags\_t create\_flags)

See psa\_ps\_create(), to which this function is analogous.

[secure\_storage\_ps\_remove](ps_8h.md#aef4fa69c85d80640a909868ad1749e8c)

psa\_status\_t secure\_storage\_ps\_remove(const psa\_storage\_uid\_t uid)

See psa\_ps\_remove(), to which this function is analogous.

[secure\_storage\_ps\_get\_info](ps_8h.md#af6c6741b58d91798e2a9c2b3644f0bf1)

psa\_status\_t secure\_storage\_ps\_get\_info(const psa\_storage\_uid\_t uid, struct psa\_storage\_info\_t \*p\_info)

See psa\_ps\_get\_info(), to which this function is analogous.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[storage\_common.h](storage__common_8h.md)

Common definitions of the PSA Secure Storage API.

[psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211)

uint32\_t psa\_storage\_create\_flags\_t

Flags used when creating an entry.

**Definition** storage\_common.h:26

[PSA\_STORAGE\_SUPPORT\_SET\_EXTENDED](storage__common_8h.md#ad9f16fc478036752ffb2ce9e50b2a710)

#define PSA\_STORAGE\_SUPPORT\_SET\_EXTENDED

Flag indicating that psa\_ps\_create() and psa\_ps\_set\_extended() are supported.

**Definition** storage\_common.h:48

[psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6)

uint64\_t psa\_storage\_uid\_t

UID type for identifying entries.

**Definition** storage\_common.h:23

[psa\_storage\_info\_t](structpsa__storage__info__t.md)

Metadata associated with a specific entry.

**Definition** storage\_common.h:38

[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9)

int32\_t psa\_status\_t

**Definition** error.h:13

[PSA\_ERROR\_NOT\_SUPPORTED](subsys_2secure__storage_2include_2psa_2error_8h.md#a1dcc6d130633ed5db8942257581b55dd)

#define PSA\_ERROR\_NOT\_SUPPORTED

**Definition** error.h:19

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [secure\_storage](dir_5fedd937c27a983db9815c43dc43c138.md)
- [include](dir_3887dba27d172300e5fca4cbd714c7ed.md)
- [psa](dir_d06fbc62883e41d574c8881d2ac75d4f.md)
- [protected\_storage.h](protected__storage_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

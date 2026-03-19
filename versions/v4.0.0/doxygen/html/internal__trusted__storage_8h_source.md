---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/internal__trusted__storage_8h_source.html
original_path: doxygen/html/internal__trusted__storage_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

internal\_trusted\_storage.h

[Go to the documentation of this file.](internal__trusted__storage_8h.md)

1/\* Copyright (c) 2024 Nordic Semiconductor

2 \* SPDX-License-Identifier: Apache-2.0

3 \*/

4#ifndef PSA\_INTERNAL\_TRUSTED\_STORAGE\_H

5#define PSA\_INTERNAL\_TRUSTED\_STORAGE\_H

6

11

13#include "[../internal/zephyr/secure\_storage/its.h](its_8h.md)"

14#ifdef BUILDING\_MBEDTLS\_CRYPTO

15#define ITS\_CALLER\_ID SECURE\_STORAGE\_ITS\_CALLER\_MBEDTLS

16#else

17#define ITS\_CALLER\_ID SECURE\_STORAGE\_ITS\_CALLER\_PSA\_ITS

18#endif

19#define ITS\_UID (secure\_storage\_its\_uid\_t){.uid = uid, .caller\_id = ITS\_CALLER\_ID}

21

22#include <[psa/storage\_common.h](storage__common_8h.md)>

23

[ 24](internal__trusted__storage_8h.md#a7eacf1684848e1b3bbe5cdaec2b4572d)#define PSA\_ITS\_API\_VERSION\_MAJOR 1

[ 25](internal__trusted__storage_8h.md#ad6886b2f339df083e21afe24109d8471)#define PSA\_ITS\_API\_VERSION\_MINOR 0

26

48static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 50](internal__trusted__storage_8h.md#a01e5344273e6d776d1f456c4d54a2ed8)[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) [psa\_its\_set](internal__trusted__storage_8h.md#a01e5344273e6d776d1f456c4d54a2ed8)([psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid, size\_t data\_length,

51 const void \*p\_data, [psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211) create\_flags)

52{

53 return [secure\_storage\_its\_set](its_8h.md#a3d6f3a7b47866ebcbfe9eb4a5ca99758)(ITS\_UID, data\_length, p\_data, create\_flags);

54}

55

74static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 76](internal__trusted__storage_8h.md#a387d450b2a21673fba6c56e66c74b5f7)[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) [psa\_its\_get](internal__trusted__storage_8h.md#a387d450b2a21673fba6c56e66c74b5f7)([psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid, size\_t data\_offset,

77 size\_t data\_size, void \*p\_data, size\_t \*p\_data\_length)

78{

79 return [secure\_storage\_its\_get](its_8h.md#a806bb5b9698a0f90b80b294d5f44645e)(ITS\_UID, data\_offset, data\_size, p\_data, p\_data\_length);

80}

81

95static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 97](internal__trusted__storage_8h.md#ae4efe6e7f9088fdf8ef4e126045a432b)[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) [psa\_its\_get\_info](internal__trusted__storage_8h.md#ae4efe6e7f9088fdf8ef4e126045a432b)([psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid, struct [psa\_storage\_info\_t](structpsa__storage__info__t.md) \*p\_info)

98{

99 return [secure\_storage\_its\_get\_info](its_8h.md#a8588925b41cf848d473a7e50087df606)(ITS\_UID, p\_info);

100}

101

116static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 118](internal__trusted__storage_8h.md#abd70b9f9bc063e3651f315408f4ae04c)[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) [psa\_its\_remove](internal__trusted__storage_8h.md#abd70b9f9bc063e3651f315408f4ae04c)([psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid)

119{

120 return [secure\_storage\_its\_remove](its_8h.md#a2d3337b1eb55deda25a8c75ea8d74ff5)(ITS\_UID);

121}

122

123#undef ITS\_UID

124#undef ITS\_CALLER\_ID

125

126#endif

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[psa\_its\_set](internal__trusted__storage_8h.md#a01e5344273e6d776d1f456c4d54a2ed8)

psa\_status\_t psa\_its\_set(psa\_storage\_uid\_t uid, size\_t data\_length, const void \*p\_data, psa\_storage\_create\_flags\_t create\_flags)

Creates a new or modifies an existing entry.

**Definition** internal\_trusted\_storage.h:50

[psa\_its\_get](internal__trusted__storage_8h.md#a387d450b2a21673fba6c56e66c74b5f7)

psa\_status\_t psa\_its\_get(psa\_storage\_uid\_t uid, size\_t data\_offset, size\_t data\_size, void \*p\_data, size\_t \*p\_data\_length)

Retrieves data associated with the provided uid.

**Definition** internal\_trusted\_storage.h:76

[psa\_its\_remove](internal__trusted__storage_8h.md#abd70b9f9bc063e3651f315408f4ae04c)

psa\_status\_t psa\_its\_remove(psa\_storage\_uid\_t uid)

Removes the provided uid and its associated data.

**Definition** internal\_trusted\_storage.h:118

[psa\_its\_get\_info](internal__trusted__storage_8h.md#ae4efe6e7f9088fdf8ef4e126045a432b)

psa\_status\_t psa\_its\_get\_info(psa\_storage\_uid\_t uid, struct psa\_storage\_info\_t \*p\_info)

Retrieves the metadata of a given entry.

**Definition** internal\_trusted\_storage.h:97

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

[storage\_common.h](storage__common_8h.md)

Common definitions of the PSA Secure Storage API.

[psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211)

uint32\_t psa\_storage\_create\_flags\_t

Flags used when creating an entry.

**Definition** storage\_common.h:26

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

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [secure\_storage](dir_5fedd937c27a983db9815c43dc43c138.md)
- [include](dir_3887dba27d172300e5fca4cbd714c7ed.md)
- [psa](dir_d06fbc62883e41d574c8881d2ac75d4f.md)
- [internal\_trusted\_storage.h](internal__trusted__storage_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

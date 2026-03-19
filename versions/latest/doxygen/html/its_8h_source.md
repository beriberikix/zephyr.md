---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/its_8h_source.html
original_path: doxygen/html/its_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

its.h

[Go to the documentation of this file.](its_8h.md)

1/\* Copyright (c) 2024 Nordic Semiconductor

2 \* SPDX-License-Identifier: Apache-2.0

3 \*/

4#ifndef SECURE\_STORAGE\_ITS\_H

5#define SECURE\_STORAGE\_ITS\_H

6

14#include "[its/common.h](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.md)"

15

[ 17](its_8h.md#a3d6f3a7b47866ebcbfe9eb4a5ca99758)[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) [secure\_storage\_its\_set](its_8h.md#a3d6f3a7b47866ebcbfe9eb4a5ca99758)([secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) uid, size\_t data\_length,

18 const void \*p\_data, [psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211) create\_flags);

19

[ 21](its_8h.md#a806bb5b9698a0f90b80b294d5f44645e)[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) [secure\_storage\_its\_get](its_8h.md#a806bb5b9698a0f90b80b294d5f44645e)([secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) uid, size\_t data\_offset,

22 size\_t data\_size, void \*p\_data, size\_t \*p\_data\_length);

23

[ 25](its_8h.md#a8588925b41cf848d473a7e50087df606)[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) [secure\_storage\_its\_get\_info](its_8h.md#a8588925b41cf848d473a7e50087df606)([secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) uid,

26 struct [psa\_storage\_info\_t](structpsa__storage__info__t.md) \*p\_info);

27

[ 29](its_8h.md#a2d3337b1eb55deda25a8c75ea8d74ff5)[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) [secure\_storage\_its\_remove](its_8h.md#a2d3337b1eb55deda25a8c75ea8d74ff5)([secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) uid);

30

31#endif

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

[psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211)

uint32\_t psa\_storage\_create\_flags\_t

Flags used when creating an entry.

**Definition** storage\_common.h:26

[psa\_storage\_info\_t](structpsa__storage__info__t.md)

Metadata associated with a specific entry.

**Definition** storage\_common.h:38

[secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md)

The UID (caller + entry IDs) of an ITS entry.

**Definition** common.h:26

[common.h](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.md)

Common definitions of the secure storage subsystem's ITS APIs.

[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9)

int32\_t psa\_status\_t

**Definition** error.h:13

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [secure\_storage](dir_5fedd937c27a983db9815c43dc43c138.md)
- [include](dir_3887dba27d172300e5fca4cbd714c7ed.md)
- [internal](dir_49025992370a830d8c3dd47cf1bb57bb.md)
- [zephyr](dir_29af7cd685f88a83c3e1809490f18587.md)
- [secure\_storage](dir_b251feb5349caf21c27bf417dfd4e083.md)
- [its.h](its_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

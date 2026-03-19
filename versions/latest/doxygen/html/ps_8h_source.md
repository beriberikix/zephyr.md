---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ps_8h_source.html
original_path: doxygen/html/ps_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ps.h

[Go to the documentation of this file.](ps_8h.md)

1/\* Copyright (c) 2024 Nordic Semiconductor

2 \* SPDX-License-Identifier: Apache-2.0

3 \*/

4#ifndef SECURE\_STORAGE\_PS\_H

5#define SECURE\_STORAGE\_PS\_H

6

14#include <[psa/storage\_common.h](storage__common_8h.md)>

15

[ 17](ps_8h.md#ab0be3c9374c1db65b45c43fdc6c05825)[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) [secure\_storage\_ps\_set](ps_8h.md#ab0be3c9374c1db65b45c43fdc6c05825)(const [psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid, size\_t data\_length,

18 const void \*p\_data, [psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211) create\_flags);

19

[ 21](ps_8h.md#a0387828802c41350b9572a1555ecdeac)[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) [secure\_storage\_ps\_get](ps_8h.md#a0387828802c41350b9572a1555ecdeac)(const [psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid, size\_t data\_offset,

22 size\_t data\_length, void \*p\_data, size\_t \*p\_data\_length);

23

[ 25](ps_8h.md#af6c6741b58d91798e2a9c2b3644f0bf1)[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) [secure\_storage\_ps\_get\_info](ps_8h.md#af6c6741b58d91798e2a9c2b3644f0bf1)(const [psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid,

26 struct [psa\_storage\_info\_t](structpsa__storage__info__t.md) \*p\_info);

27

[ 29](ps_8h.md#aef4fa69c85d80640a909868ad1749e8c)[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) [secure\_storage\_ps\_remove](ps_8h.md#aef4fa69c85d80640a909868ad1749e8c)(const [psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid);

30

[ 32](ps_8h.md#ae044a9d36445840539578b9ea3a1e4d0)[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) [secure\_storage\_ps\_create](ps_8h.md#ae044a9d36445840539578b9ea3a1e4d0)([psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid, size\_t capacity,

33 [psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211) create\_flags);

34

[ 36](ps_8h.md#ab1612b91d341295578e16eb64d7035c4)[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) [secure\_storage\_ps\_set\_extended](ps_8h.md#ab1612b91d341295578e16eb64d7035c4)([psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid, size\_t data\_offset,

37 size\_t data\_length, const void \*p\_data);

38

39#endif

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
- [internal](dir_49025992370a830d8c3dd47cf1bb57bb.md)
- [zephyr](dir_29af7cd685f88a83c3e1809490f18587.md)
- [secure\_storage](dir_b251feb5349caf21c27bf417dfd4e083.md)
- [ps.h](ps_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/storage__common_8h_source.html
original_path: doxygen/html/storage__common_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

storage\_common.h

[Go to the documentation of this file.](storage__common_8h.md)

1/\* Copyright (c) 2024 Nordic Semiconductor

2 \* SPDX-License-Identifier: Apache-2.0

3 \*/

4#ifndef PSA\_STORAGE\_COMMON\_H

5#define PSA\_STORAGE\_COMMON\_H

19#include <[psa/error.h](subsys_2secure__storage_2include_2psa_2error_8h.md)>

20#include <stddef.h>

21

[ 23](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6)typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6);

24

[ 26](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211);

27

[ 29](storage__common_8h.md#a65299349e8643d466eeaeb5bb62cfb6e)#define PSA\_STORAGE\_FLAG\_NONE 0u

[ 31](storage__common_8h.md#a15dbec8d862073de6024924bf015dcdd)#define PSA\_STORAGE\_FLAG\_WRITE\_ONCE (1u << 0)

[ 33](storage__common_8h.md#ab3688fcb77630ebdb3774516560b5226)#define PSA\_STORAGE\_FLAG\_NO\_CONFIDENTIALITY (1u << 1)

[ 35](storage__common_8h.md#a5781482a6bea58c8f9acdb1da921efbe)#define PSA\_STORAGE\_FLAG\_NO\_REPLAY\_PROTECTION (1u << 2)

36

[ 38](structpsa__storage__info__t.md)struct [psa\_storage\_info\_t](structpsa__storage__info__t.md) {

[ 40](structpsa__storage__info__t.md#a1b2d4b80f2989c0c182bf519442090ae) size\_t [capacity](structpsa__storage__info__t.md#a1b2d4b80f2989c0c182bf519442090ae);

[ 42](structpsa__storage__info__t.md#a2a18bf8e7a44cc050e088fb34a453a1d) size\_t [size](structpsa__storage__info__t.md#a2a18bf8e7a44cc050e088fb34a453a1d);

[ 44](structpsa__storage__info__t.md#a3dfb41a4b9bf931f3b3fe96f13c1d289) [psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211) [flags](structpsa__storage__info__t.md#a3dfb41a4b9bf931f3b3fe96f13c1d289);

45};

46

[ 48](storage__common_8h.md#ad9f16fc478036752ffb2ce9e50b2a710)#define PSA\_STORAGE\_SUPPORT\_SET\_EXTENDED (1u << 0)

49

51#endif

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

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

[psa\_storage\_info\_t::capacity](structpsa__storage__info__t.md#a1b2d4b80f2989c0c182bf519442090ae)

size\_t capacity

The allocated capacity of the storage associated with an entry.

**Definition** storage\_common.h:40

[psa\_storage\_info\_t::size](structpsa__storage__info__t.md#a2a18bf8e7a44cc050e088fb34a453a1d)

size\_t size

The size of an entry's data.

**Definition** storage\_common.h:42

[psa\_storage\_info\_t::flags](structpsa__storage__info__t.md#a3dfb41a4b9bf931f3b3fe96f13c1d289)

psa\_storage\_create\_flags\_t flags

The flags used when the entry was created.

**Definition** storage\_common.h:44

[error.h](subsys_2secure__storage_2include_2psa_2error_8h.md)

Return values of the PSA Secure Storage API.

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [secure\_storage](dir_5fedd937c27a983db9815c43dc43c138.md)
- [include](dir_3887dba27d172300e5fca4cbd714c7ed.md)
- [psa](dir_d06fbc62883e41d574c8881d2ac75d4f.md)
- [storage\_common.h](storage__common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

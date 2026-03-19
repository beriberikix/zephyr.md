---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/store_8h_source.html
original_path: doxygen/html/store_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

store.h

[Go to the documentation of this file.](store_8h.md)

1/\* Copyright (c) 2024 Nordic Semiconductor

2 \* SPDX-License-Identifier: Apache-2.0

3 \*/

4#ifndef SECURE\_STORAGE\_ITS\_STORE\_H

5#define SECURE\_STORAGE\_ITS\_STORE\_H

6

14#include <[zephyr/secure\_storage/its/common.h](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.md)>

15

[ 24](store_8h.md#aed06855314e4dafb4e935d31b6fb21bb)[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) [secure\_storage\_its\_store\_set](store_8h.md#aed06855314e4dafb4e935d31b6fb21bb)([secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) uid,

25 size\_t data\_length, const void \*data);

26

[ 37](store_8h.md#a22d16815fb645ff5cc014f2fe4e9e987)[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) [secure\_storage\_its\_store\_get](store_8h.md#a22d16815fb645ff5cc014f2fe4e9e987)([secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) uid, size\_t data\_size,

38 void \*data, size\_t \*data\_length);

39

[ 46](store_8h.md#a58eb126f3d92112b3ed19d1920d43fa0)[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) [secure\_storage\_its\_store\_remove](store_8h.md#a58eb126f3d92112b3ed19d1920d43fa0)([secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) uid);

47

48#endif

[secure\_storage\_its\_store\_get](store_8h.md#a22d16815fb645ff5cc014f2fe4e9e987)

psa\_status\_t secure\_storage\_its\_store\_get(secure\_storage\_its\_uid\_t uid, size\_t data\_size, void \*data, size\_t \*data\_length)

Retrieves the data of an ITS entry from the storage medium.

[secure\_storage\_its\_store\_remove](store_8h.md#a58eb126f3d92112b3ed19d1920d43fa0)

psa\_status\_t secure\_storage\_its\_store\_remove(secure\_storage\_its\_uid\_t uid)

Removes an ITS entry from the storage medium.

[secure\_storage\_its\_store\_set](store_8h.md#aed06855314e4dafb4e935d31b6fb21bb)

psa\_status\_t secure\_storage\_its\_store\_set(secure\_storage\_its\_uid\_t uid, size\_t data\_length, const void \*data)

Writes the data of an ITS entry to the storage medium.

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
- [its](dir_8ffdb9b26f60d93440ec7ee1d2751029.md)
- [store.h](store_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

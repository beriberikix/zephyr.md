---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/settings__get_8h_source.html
original_path: doxygen/html/settings__get_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

settings\_get.h

[Go to the documentation of this file.](settings__get_8h.md)

1/\* Copyright (c) 2024 Nordic Semiconductor

2 \* SPDX-License-Identifier: Apache-2.0

3 \*/

4#ifndef SECURE\_STORAGE\_ITS\_STORE\_SETTINGS\_GET\_H

5#define SECURE\_STORAGE\_ITS\_STORE\_SETTINGS\_GET\_H

6

15#include <[zephyr/secure\_storage/its/common.h](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.md)>

16

[ 17](settings__get_8h.md#a0f0cc8b19de1f5d8bc891a61cf7932c0ad536c1e2bded234819838096526b74bd)enum { [SECURE\_STORAGE\_ITS\_STORE\_SETTINGS\_NAME\_BUF\_SIZE](settings__get_8h.md#a0f0cc8b19de1f5d8bc891a61cf7932c0ad536c1e2bded234819838096526b74bd)

18 = CONFIG\_SECURE\_STORAGE\_ITS\_STORE\_SETTINGS\_NAME\_MAX\_LEN + 1 };

19

[ 25](settings__get_8h.md#a3d3cf7e3354e379167f9d2a448d3e3dd)void [secure\_storage\_its\_store\_settings\_get\_name](settings__get_8h.md#a3d3cf7e3354e379167f9d2a448d3e3dd)(

26 [secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) uid,

27 char name[static [SECURE\_STORAGE\_ITS\_STORE\_SETTINGS\_NAME\_BUF\_SIZE](settings__get_8h.md#a0f0cc8b19de1f5d8bc891a61cf7932c0ad536c1e2bded234819838096526b74bd)]);

28

29#endif

[SECURE\_STORAGE\_ITS\_STORE\_SETTINGS\_NAME\_BUF\_SIZE](settings__get_8h.md#a0f0cc8b19de1f5d8bc891a61cf7932c0ad536c1e2bded234819838096526b74bd)

@ SECURE\_STORAGE\_ITS\_STORE\_SETTINGS\_NAME\_BUF\_SIZE

**Definition** settings\_get.h:17

[secure\_storage\_its\_store\_settings\_get\_name](settings__get_8h.md#a3d3cf7e3354e379167f9d2a448d3e3dd)

void secure\_storage\_its\_store\_settings\_get\_name(secure\_storage\_its\_uid\_t uid, char name[static SECURE\_STORAGE\_ITS\_STORE\_SETTINGS\_NAME\_BUF\_SIZE])

Returns the setting name to use for an ITS entry.

[secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md)

The UID (caller + entry IDs) of an ITS entry.

**Definition** common.h:26

[common.h](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.md)

Common definitions of the secure storage subsystem's ITS APIs.

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [secure\_storage](dir_5fedd937c27a983db9815c43dc43c138.md)
- [include](dir_3887dba27d172300e5fca4cbd714c7ed.md)
- [internal](dir_49025992370a830d8c3dd47cf1bb57bb.md)
- [zephyr](dir_29af7cd685f88a83c3e1809490f18587.md)
- [secure\_storage](dir_b251feb5349caf21c27bf417dfd4e083.md)
- [its](dir_8ffdb9b26f60d93440ec7ee1d2751029.md)
- [store](dir_ec89f69c8843f11be29f68cdb1d05909.md)
- [settings\_get.h](settings__get_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

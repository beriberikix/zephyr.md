---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/settings__mgmt_8h_source.html
original_path: doxygen/html/settings__mgmt_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

settings\_mgmt.h

[Go to the documentation of this file.](settings__mgmt_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef H\_SETTINGS\_MGMT\_

8#define H\_SETTINGS\_MGMT\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

[ 17](settings__mgmt_8h.md#aff2f915e03116c35567dfa3b61353e34)#define SETTINGS\_MGMT\_ID\_READ\_WRITE 0

[ 18](settings__mgmt_8h.md#a1c3751a9b7a6b267f78fcc8b2b8954fb)#define SETTINGS\_MGMT\_ID\_DELETE 1

[ 19](settings__mgmt_8h.md#a85687e53d63edfe4d3bd55988d863e9d)#define SETTINGS\_MGMT\_ID\_COMMIT 2

[ 20](settings__mgmt_8h.md#a3add3a2acfcd23eb7af5df404378050c)#define SETTINGS\_MGMT\_ID\_LOAD\_SAVE 3

21

[ 25](settings__mgmt_8h.md#afb39b95aec3183531602aa6964ceb1cc)enum [settings\_mgmt\_ret\_code\_t](settings__mgmt_8h.md#afb39b95aec3183531602aa6964ceb1cc) {

[ 27](settings__mgmt_8h.md#afb39b95aec3183531602aa6964ceb1ccab337460951137340ebdd8fa85d929a8f) [SETTINGS\_MGMT\_ERR\_OK](settings__mgmt_8h.md#afb39b95aec3183531602aa6964ceb1ccab337460951137340ebdd8fa85d929a8f) = 0,

28

[ 30](settings__mgmt_8h.md#afb39b95aec3183531602aa6964ceb1cca47500e585ffceef9e05006f8298e825d) [SETTINGS\_MGMT\_ERR\_UNKNOWN](settings__mgmt_8h.md#afb39b95aec3183531602aa6964ceb1cca47500e585ffceef9e05006f8298e825d),

31

[ 33](settings__mgmt_8h.md#afb39b95aec3183531602aa6964ceb1cca89805202eb970bdb3689067884c71a28) [SETTINGS\_MGMT\_ERR\_KEY\_TOO\_LONG](settings__mgmt_8h.md#afb39b95aec3183531602aa6964ceb1cca89805202eb970bdb3689067884c71a28),

34

[ 36](settings__mgmt_8h.md#afb39b95aec3183531602aa6964ceb1ccacb9f7104664f9be3d7b56bbfcbabf32f) [SETTINGS\_MGMT\_ERR\_KEY\_NOT\_FOUND](settings__mgmt_8h.md#afb39b95aec3183531602aa6964ceb1ccacb9f7104664f9be3d7b56bbfcbabf32f),

37

[ 39](settings__mgmt_8h.md#afb39b95aec3183531602aa6964ceb1cca93c1c519a357196a5186bf1fdaf18ae2) [SETTINGS\_MGMT\_ERR\_READ\_NOT\_SUPPORTED](settings__mgmt_8h.md#afb39b95aec3183531602aa6964ceb1cca93c1c519a357196a5186bf1fdaf18ae2),

40

[ 42](settings__mgmt_8h.md#afb39b95aec3183531602aa6964ceb1cca4ebaa41c929542cc39f32c418b406a55) [SETTINGS\_MGMT\_ERR\_ROOT\_KEY\_NOT\_FOUND](settings__mgmt_8h.md#afb39b95aec3183531602aa6964ceb1cca4ebaa41c929542cc39f32c418b406a55),

43

[ 45](settings__mgmt_8h.md#afb39b95aec3183531602aa6964ceb1cca18928efa693757f2bf564b049a9d799b) [SETTINGS\_MGMT\_ERR\_WRITE\_NOT\_SUPPORTED](settings__mgmt_8h.md#afb39b95aec3183531602aa6964ceb1cca18928efa693757f2bf564b049a9d799b),

46

[ 48](settings__mgmt_8h.md#afb39b95aec3183531602aa6964ceb1ccaacb2dafde9aed9953c5764597463762d) [SETTINGS\_MGMT\_ERR\_DELETE\_NOT\_SUPPORTED](settings__mgmt_8h.md#afb39b95aec3183531602aa6964ceb1ccaacb2dafde9aed9953c5764597463762d),

49};

50

51#ifdef \_\_cplusplus

52}

53#endif

54

55#endif

[settings\_mgmt\_ret\_code\_t](settings__mgmt_8h.md#afb39b95aec3183531602aa6964ceb1cc)

settings\_mgmt\_ret\_code\_t

Command result codes for settings management group.

**Definition** settings\_mgmt.h:25

[SETTINGS\_MGMT\_ERR\_WRITE\_NOT\_SUPPORTED](settings__mgmt_8h.md#afb39b95aec3183531602aa6964ceb1cca18928efa693757f2bf564b049a9d799b)

@ SETTINGS\_MGMT\_ERR\_WRITE\_NOT\_SUPPORTED

The provided key name does not support being written.

**Definition** settings\_mgmt.h:45

[SETTINGS\_MGMT\_ERR\_UNKNOWN](settings__mgmt_8h.md#afb39b95aec3183531602aa6964ceb1cca47500e585ffceef9e05006f8298e825d)

@ SETTINGS\_MGMT\_ERR\_UNKNOWN

Unknown error occurred.

**Definition** settings\_mgmt.h:30

[SETTINGS\_MGMT\_ERR\_ROOT\_KEY\_NOT\_FOUND](settings__mgmt_8h.md#afb39b95aec3183531602aa6964ceb1cca4ebaa41c929542cc39f32c418b406a55)

@ SETTINGS\_MGMT\_ERR\_ROOT\_KEY\_NOT\_FOUND

The provided root key name does not exist.

**Definition** settings\_mgmt.h:42

[SETTINGS\_MGMT\_ERR\_KEY\_TOO\_LONG](settings__mgmt_8h.md#afb39b95aec3183531602aa6964ceb1cca89805202eb970bdb3689067884c71a28)

@ SETTINGS\_MGMT\_ERR\_KEY\_TOO\_LONG

The provided key name is too long to be used.

**Definition** settings\_mgmt.h:33

[SETTINGS\_MGMT\_ERR\_READ\_NOT\_SUPPORTED](settings__mgmt_8h.md#afb39b95aec3183531602aa6964ceb1cca93c1c519a357196a5186bf1fdaf18ae2)

@ SETTINGS\_MGMT\_ERR\_READ\_NOT\_SUPPORTED

The provided key name does not support being read.

**Definition** settings\_mgmt.h:39

[SETTINGS\_MGMT\_ERR\_DELETE\_NOT\_SUPPORTED](settings__mgmt_8h.md#afb39b95aec3183531602aa6964ceb1ccaacb2dafde9aed9953c5764597463762d)

@ SETTINGS\_MGMT\_ERR\_DELETE\_NOT\_SUPPORTED

The provided key name does not support being deleted.

**Definition** settings\_mgmt.h:48

[SETTINGS\_MGMT\_ERR\_OK](settings__mgmt_8h.md#afb39b95aec3183531602aa6964ceb1ccab337460951137340ebdd8fa85d929a8f)

@ SETTINGS\_MGMT\_ERR\_OK

No error, this is implied if there is no ret value in the response.

**Definition** settings\_mgmt.h:27

[SETTINGS\_MGMT\_ERR\_KEY\_NOT\_FOUND](settings__mgmt_8h.md#afb39b95aec3183531602aa6964ceb1ccacb9f7104664f9be3d7b56bbfcbabf32f)

@ SETTINGS\_MGMT\_ERR\_KEY\_NOT\_FOUND

The provided key name does not exist.

**Definition** settings\_mgmt.h:36

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [settings\_mgmt](dir_f7c37d3a1c1d534b483feb4fbb3dbf95.md)
- [settings\_mgmt.h](settings__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

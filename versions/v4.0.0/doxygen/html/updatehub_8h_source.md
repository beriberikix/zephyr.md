---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/updatehub_8h_source.html
original_path: doxygen/html/updatehub_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

updatehub.h

[Go to the documentation of this file.](updatehub_8h.md)

1/\*

2 \* Copyright (c) 2018-2023 O.S.Systems

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_MGMT\_UPDATEHUB\_H\_

15#define ZEPHYR\_INCLUDE\_MGMT\_UPDATEHUB\_H\_

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

[ 29](group__updatehub.md#ga6e6eb49b1e4b558cd8be0da8b45a07b8)enum [updatehub\_response](group__updatehub.md#ga6e6eb49b1e4b558cd8be0da8b45a07b8) {

[ 30](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8aa0d2256936bee57106ccffe48c3d080a) [UPDATEHUB\_NETWORKING\_ERROR](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8aa0d2256936bee57106ccffe48c3d080a) = 0,

[ 31](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8a75c0d76cdc28948d09a6512c3e316e76) [UPDATEHUB\_INCOMPATIBLE\_HARDWARE](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8a75c0d76cdc28948d09a6512c3e316e76),

[ 32](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8a5f5ae5102a0d8e318652067b2a097037) [UPDATEHUB\_UNCONFIRMED\_IMAGE](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8a5f5ae5102a0d8e318652067b2a097037),

[ 33](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8a5c7ed853ebe09b62b8c6348a695a6171) [UPDATEHUB\_METADATA\_ERROR](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8a5c7ed853ebe09b62b8c6348a695a6171),

[ 34](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8ae610dad426920bb70a42eae7bdb6b00f) [UPDATEHUB\_DOWNLOAD\_ERROR](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8ae610dad426920bb70a42eae7bdb6b00f),

[ 35](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8a5ec33576cdc17687e0e26aaf45f4382f) [UPDATEHUB\_INSTALL\_ERROR](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8a5ec33576cdc17687e0e26aaf45f4382f),

[ 36](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8afeea264fa5140271de9ff5e6196c80a2) [UPDATEHUB\_FLASH\_INIT\_ERROR](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8afeea264fa5140271de9ff5e6196c80a2),

[ 37](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8a8ec40cbba06d67803fa611bf30984f43) [UPDATEHUB\_OK](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8a8ec40cbba06d67803fa611bf30984f43),

[ 38](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8a458c9aab40f11bb32e492e9dec1f362c) [UPDATEHUB\_HAS\_UPDATE](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8a458c9aab40f11bb32e492e9dec1f362c),

[ 39](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8a6bfb08c9056ed87c58025419280af730) [UPDATEHUB\_NO\_UPDATE](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8a6bfb08c9056ed87c58025419280af730),

40};

41

[ 48](group__updatehub.md#ga2a1665a1fe1b191bbc7d80c4bbaa4299)\_\_syscall void [updatehub\_autohandler](group__updatehub.md#ga2a1665a1fe1b191bbc7d80c4bbaa4299)(void);

49

[ 59](group__updatehub.md#ga89d1715033200c89a7587dd229944a23)\_\_syscall enum [updatehub\_response](group__updatehub.md#ga6e6eb49b1e4b558cd8be0da8b45a07b8) [updatehub\_probe](group__updatehub.md#ga89d1715033200c89a7587dd229944a23)(void);

60

[ 74](group__updatehub.md#gabb00cf9b63ce13554c26286c0c37fa8a)\_\_syscall enum [updatehub\_response](group__updatehub.md#ga6e6eb49b1e4b558cd8be0da8b45a07b8) [updatehub\_update](group__updatehub.md#gabb00cf9b63ce13554c26286c0c37fa8a)(void);

75

[ 84](group__updatehub.md#gad1a3f6b1d91a7c9969a3411e0fd74f72)\_\_syscall int [updatehub\_confirm](group__updatehub.md#gad1a3f6b1d91a7c9969a3411e0fd74f72)(void);

85

[ 91](group__updatehub.md#gac433e995a18418771cac9fe4559ce84b)\_\_syscall int [updatehub\_reboot](group__updatehub.md#gac433e995a18418771cac9fe4559ce84b)(void);

92

93#ifdef \_\_cplusplus

94}

95#endif

96

100

101#include <zephyr/syscalls/updatehub.h>

102#endif /\* ZEPHYR\_INCLUDE\_MGMT\_UPDATEHUB\_H\_ \*/

[updatehub\_autohandler](group__updatehub.md#ga2a1665a1fe1b191bbc7d80c4bbaa4299)

void updatehub\_autohandler(void)

Runs UpdateHub probe and UpdateHub update automatically.

[updatehub\_response](group__updatehub.md#ga6e6eb49b1e4b558cd8be0da8b45a07b8)

updatehub\_response

Responses messages from UpdateHub.

**Definition** updatehub.h:29

[updatehub\_probe](group__updatehub.md#ga89d1715033200c89a7587dd229944a23)

enum updatehub\_response updatehub\_probe(void)

The UpdateHub probe verify if there is some update to be performed.

[updatehub\_update](group__updatehub.md#gabb00cf9b63ce13554c26286c0c37fa8a)

enum updatehub\_response updatehub\_update(void)

Apply the update package.

[updatehub\_reboot](group__updatehub.md#gac433e995a18418771cac9fe4559ce84b)

int updatehub\_reboot(void)

Request system to reboot.

[updatehub\_confirm](group__updatehub.md#gad1a3f6b1d91a7c9969a3411e0fd74f72)

int updatehub\_confirm(void)

Confirm that image is running as expected.

[UPDATEHUB\_HAS\_UPDATE](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8a458c9aab40f11bb32e492e9dec1f362c)

@ UPDATEHUB\_HAS\_UPDATE

**Definition** updatehub.h:38

[UPDATEHUB\_METADATA\_ERROR](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8a5c7ed853ebe09b62b8c6348a695a6171)

@ UPDATEHUB\_METADATA\_ERROR

**Definition** updatehub.h:33

[UPDATEHUB\_INSTALL\_ERROR](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8a5ec33576cdc17687e0e26aaf45f4382f)

@ UPDATEHUB\_INSTALL\_ERROR

**Definition** updatehub.h:35

[UPDATEHUB\_UNCONFIRMED\_IMAGE](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8a5f5ae5102a0d8e318652067b2a097037)

@ UPDATEHUB\_UNCONFIRMED\_IMAGE

**Definition** updatehub.h:32

[UPDATEHUB\_NO\_UPDATE](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8a6bfb08c9056ed87c58025419280af730)

@ UPDATEHUB\_NO\_UPDATE

**Definition** updatehub.h:39

[UPDATEHUB\_INCOMPATIBLE\_HARDWARE](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8a75c0d76cdc28948d09a6512c3e316e76)

@ UPDATEHUB\_INCOMPATIBLE\_HARDWARE

**Definition** updatehub.h:31

[UPDATEHUB\_OK](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8a8ec40cbba06d67803fa611bf30984f43)

@ UPDATEHUB\_OK

**Definition** updatehub.h:37

[UPDATEHUB\_NETWORKING\_ERROR](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8aa0d2256936bee57106ccffe48c3d080a)

@ UPDATEHUB\_NETWORKING\_ERROR

**Definition** updatehub.h:30

[UPDATEHUB\_DOWNLOAD\_ERROR](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8ae610dad426920bb70a42eae7bdb6b00f)

@ UPDATEHUB\_DOWNLOAD\_ERROR

**Definition** updatehub.h:34

[UPDATEHUB\_FLASH\_INIT\_ERROR](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8afeea264fa5140271de9ff5e6196c80a2)

@ UPDATEHUB\_FLASH\_INIT\_ERROR

**Definition** updatehub.h:36

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [updatehub.h](updatehub_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

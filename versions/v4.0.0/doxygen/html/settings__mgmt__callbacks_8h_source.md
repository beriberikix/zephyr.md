---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/settings__mgmt__callbacks_8h_source.html
original_path: doxygen/html/settings__mgmt__callbacks_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

settings\_mgmt\_callbacks.h

[Go to the documentation of this file.](settings__mgmt__callbacks_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef H\_MCUMGR\_SETTINGS\_MGMT\_CALLBACKS\_

8#define H\_MCUMGR\_SETTINGS\_MGMT\_CALLBACKS\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

20

[ 21](group__mcumgr__callback__api__settings__mgmt.md#ga40c179f978718409c7db43448efc8f47)enum [settings\_mgmt\_access\_types](group__mcumgr__callback__api__settings__mgmt.md#ga40c179f978718409c7db43448efc8f47) {

[ 22](group__mcumgr__callback__api__settings__mgmt.md#gga40c179f978718409c7db43448efc8f47aea0d3b2628423306fbb4d52718d7af00) [SETTINGS\_ACCESS\_READ](group__mcumgr__callback__api__settings__mgmt.md#gga40c179f978718409c7db43448efc8f47aea0d3b2628423306fbb4d52718d7af00),

[ 23](group__mcumgr__callback__api__settings__mgmt.md#gga40c179f978718409c7db43448efc8f47a614d170f1bdd53361576fd7c73b7c590) [SETTINGS\_ACCESS\_WRITE](group__mcumgr__callback__api__settings__mgmt.md#gga40c179f978718409c7db43448efc8f47a614d170f1bdd53361576fd7c73b7c590),

[ 24](group__mcumgr__callback__api__settings__mgmt.md#gga40c179f978718409c7db43448efc8f47a1d4e86a55ad3d9869b0185cc0b4d9dbd) [SETTINGS\_ACCESS\_DELETE](group__mcumgr__callback__api__settings__mgmt.md#gga40c179f978718409c7db43448efc8f47a1d4e86a55ad3d9869b0185cc0b4d9dbd),

[ 25](group__mcumgr__callback__api__settings__mgmt.md#gga40c179f978718409c7db43448efc8f47a377d59e22e96f09348df99cd62fad4de) [SETTINGS\_ACCESS\_COMMIT](group__mcumgr__callback__api__settings__mgmt.md#gga40c179f978718409c7db43448efc8f47a377d59e22e96f09348df99cd62fad4de),

[ 26](group__mcumgr__callback__api__settings__mgmt.md#gga40c179f978718409c7db43448efc8f47acc68c6153dcb7c7b0c7182fd6eb525ce) [SETTINGS\_ACCESS\_LOAD](group__mcumgr__callback__api__settings__mgmt.md#gga40c179f978718409c7db43448efc8f47acc68c6153dcb7c7b0c7182fd6eb525ce),

[ 27](group__mcumgr__callback__api__settings__mgmt.md#gga40c179f978718409c7db43448efc8f47a37c25f343771851dab3aa4f99c97e543) [SETTINGS\_ACCESS\_SAVE](group__mcumgr__callback__api__settings__mgmt.md#gga40c179f978718409c7db43448efc8f47a37c25f343771851dab3aa4f99c97e543),

28};

29

[ 36](structsettings__mgmt__access.md)struct [settings\_mgmt\_access](structsettings__mgmt__access.md) {

[ 38](structsettings__mgmt__access.md#a9b798a118844083d77af6db53df5eb37) enum [settings\_mgmt\_access\_types](group__mcumgr__callback__api__settings__mgmt.md#ga40c179f978718409c7db43448efc8f47) [access](structsettings__mgmt__access.md#a9b798a118844083d77af6db53df5eb37);

39

49#ifdef CONFIG\_MCUMGR\_GRP\_SETTINGS\_BUFFER\_TYPE\_HEAP

50 const char \*[name](structsettings__mgmt__access.md#ae0f02e70ee2da823801d4d475f4a2e76);

51#else

[ 52](structsettings__mgmt__access.md#ae0f02e70ee2da823801d4d475f4a2e76) char \*[name](structsettings__mgmt__access.md#ae0f02e70ee2da823801d4d475f4a2e76);

53#endif

54

[ 56](structsettings__mgmt__access.md#aeb23615be870929a987c6cfbd3f445de) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[val](structsettings__mgmt__access.md#aeb23615be870929a987c6cfbd3f445de);

57

[ 59](structsettings__mgmt__access.md#ab13bdcd8763dca5a99d3d52270f9b4d2) const size\_t \*[val\_length](structsettings__mgmt__access.md#ab13bdcd8763dca5a99d3d52270f9b4d2);

60};

61

65

66#ifdef \_\_cplusplus

67}

68#endif

69

70#endif

[settings\_mgmt\_access\_types](group__mcumgr__callback__api__settings__mgmt.md#ga40c179f978718409c7db43448efc8f47)

settings\_mgmt\_access\_types

**Definition** settings\_mgmt\_callbacks.h:21

[SETTINGS\_ACCESS\_DELETE](group__mcumgr__callback__api__settings__mgmt.md#gga40c179f978718409c7db43448efc8f47a1d4e86a55ad3d9869b0185cc0b4d9dbd)

@ SETTINGS\_ACCESS\_DELETE

**Definition** settings\_mgmt\_callbacks.h:24

[SETTINGS\_ACCESS\_COMMIT](group__mcumgr__callback__api__settings__mgmt.md#gga40c179f978718409c7db43448efc8f47a377d59e22e96f09348df99cd62fad4de)

@ SETTINGS\_ACCESS\_COMMIT

**Definition** settings\_mgmt\_callbacks.h:25

[SETTINGS\_ACCESS\_SAVE](group__mcumgr__callback__api__settings__mgmt.md#gga40c179f978718409c7db43448efc8f47a37c25f343771851dab3aa4f99c97e543)

@ SETTINGS\_ACCESS\_SAVE

**Definition** settings\_mgmt\_callbacks.h:27

[SETTINGS\_ACCESS\_WRITE](group__mcumgr__callback__api__settings__mgmt.md#gga40c179f978718409c7db43448efc8f47a614d170f1bdd53361576fd7c73b7c590)

@ SETTINGS\_ACCESS\_WRITE

**Definition** settings\_mgmt\_callbacks.h:23

[SETTINGS\_ACCESS\_LOAD](group__mcumgr__callback__api__settings__mgmt.md#gga40c179f978718409c7db43448efc8f47acc68c6153dcb7c7b0c7182fd6eb525ce)

@ SETTINGS\_ACCESS\_LOAD

**Definition** settings\_mgmt\_callbacks.h:26

[SETTINGS\_ACCESS\_READ](group__mcumgr__callback__api__settings__mgmt.md#gga40c179f978718409c7db43448efc8f47aea0d3b2628423306fbb4d52718d7af00)

@ SETTINGS\_ACCESS\_READ

**Definition** settings\_mgmt\_callbacks.h:22

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[settings\_mgmt\_access](structsettings__mgmt__access.md)

Structure provided in the MGMT\_EVT\_OP\_SETTINGS\_MGMT\_ACCESS notification callback: This callback funct...

**Definition** settings\_mgmt\_callbacks.h:36

[settings\_mgmt\_access::access](structsettings__mgmt__access.md#a9b798a118844083d77af6db53df5eb37)

enum settings\_mgmt\_access\_types access

Type of access.

**Definition** settings\_mgmt\_callbacks.h:38

[settings\_mgmt\_access::val\_length](structsettings__mgmt__access.md#ab13bdcd8763dca5a99d3d52270f9b4d2)

const size\_t \* val\_length

Length of data provided by the user (only set for SETTINGS\_ACCESS\_WRITE).

**Definition** settings\_mgmt\_callbacks.h:59

[settings\_mgmt\_access::name](structsettings__mgmt__access.md#ae0f02e70ee2da823801d4d475f4a2e76)

char \* name

Key name for accesses (only set for SETTINGS\_ACCESS\_READ, SETTINGS\_ACCESS\_WRITE and SETTINGS\_ACCESS\_D...

**Definition** settings\_mgmt\_callbacks.h:52

[settings\_mgmt\_access::val](structsettings__mgmt__access.md#aeb23615be870929a987c6cfbd3f445de)

const uint8\_t \* val

Data provided by the user (only set for SETTINGS\_ACCESS\_WRITE).

**Definition** settings\_mgmt\_callbacks.h:56

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [settings\_mgmt](dir_f7c37d3a1c1d534b483feb4fbb3dbf95.md)
- [settings\_mgmt\_callbacks.h](settings__mgmt__callbacks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

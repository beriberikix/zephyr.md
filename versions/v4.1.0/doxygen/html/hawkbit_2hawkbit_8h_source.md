---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/hawkbit_2hawkbit_8h_source.html
original_path: doxygen/html/hawkbit_2hawkbit_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hawkbit.h

[Go to the documentation of this file.](hawkbit_2hawkbit_8h.md)

1/\*

2 \* Copyright (c) 2020 Linumiz

3 \* Copyright (c) 2024 Vogl Electronic GmbH

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

12

19

20#ifndef ZEPHYR\_INCLUDE\_MGMT\_HAWKBIT\_HAWKBIT\_H\_

21#define ZEPHYR\_INCLUDE\_MGMT\_HAWKBIT\_HAWKBIT\_H\_

22

23#include <[stdint.h](stdint_8h.md)>

24

[ 33](group__hawkbit.md#ga96c59c754178451d8dbd08b32813220b)enum [hawkbit\_response](group__hawkbit.md#ga96c59c754178451d8dbd08b32813220b) {

[ 35](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220baa18639f74548a317808b24c702f2fcb9) [HAWKBIT\_NO\_RESPONSE](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220baa18639f74548a317808b24c702f2fcb9),

[ 37](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba9f5a200928474863a88d170c11594048) [HAWKBIT\_UPDATE\_INSTALLED](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba9f5a200928474863a88d170c11594048),

[ 39](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bac73c46deb3e54dba690f814a2fb9db71) [HAWKBIT\_NO\_UPDATE](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bac73c46deb3e54dba690f814a2fb9db71),

[ 41](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba5a36eadcadc43c1fd0936a8546fb15e8) [HAWKBIT\_NETWORKING\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba5a36eadcadc43c1fd0936a8546fb15e8),

[ 43](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bad4b0587da0bdfd829d0d08ed2407357d) [HAWKBIT\_UNCONFIRMED\_IMAGE](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bad4b0587da0bdfd829d0d08ed2407357d),

[ 45](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba1d79e6fe8487cc4dc36c6c91bcabd124) [HAWKBIT\_PERMISSION\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba1d79e6fe8487cc4dc36c6c91bcabd124),

[ 47](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba2b7d188d8c28a3373d9b8a7f831b1e3a) [HAWKBIT\_METADATA\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba2b7d188d8c28a3373d9b8a7f831b1e3a),

[ 49](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220baf1a448b0addfc769515c725ce5b1bab9) [HAWKBIT\_DOWNLOAD\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220baf1a448b0addfc769515c725ce5b1bab9),

[ 51](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bacee282923e7435b81794ccec9749ce01) [HAWKBIT\_ALLOC\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bacee282923e7435b81794ccec9749ce01),

[ 53](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bac4ba42120229e92b52c82d4a4d4cd708) [HAWKBIT\_NOT\_INITIALIZED](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bac4ba42120229e92b52c82d4a4d4cd708),

[ 55](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba28ccbb4060d41592884829cf205414f6) [HAWKBIT\_PROBE\_IN\_PROGRESS](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba28ccbb4060d41592884829cf205414f6),

56};

57

[ 69](group__hawkbit.md#ga2774769ec44f2793895b5d783b4dceda)typedef int (\*[hawkbit\_config\_device\_data\_cb\_handler\_t](group__hawkbit.md#ga2774769ec44f2793895b5d783b4dceda))(const char \*device\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer,

70 const size\_t buffer\_size);

71

[ 83](group__hawkbit.md#gad8e83255a969eb61244b1edfd0b95e5d)int [hawkbit\_set\_custom\_data\_cb](group__hawkbit.md#gad8e83255a969eb61244b1edfd0b95e5d)([hawkbit\_config\_device\_data\_cb\_handler\_t](group__hawkbit.md#ga2774769ec44f2793895b5d783b4dceda) cb);

84

[ 91](group__hawkbit.md#ga0ef6151f205088405de242e012984ca6)int [hawkbit\_init](group__hawkbit.md#ga0ef6151f205088405de242e012984ca6)(void);

92

[ 98](group__hawkbit.md#ga525173f0c3d0ca4e26124a34d098d0b9)enum [hawkbit\_response](group__hawkbit.md#ga96c59c754178451d8dbd08b32813220b) [hawkbit\_probe](group__hawkbit.md#ga525173f0c3d0ca4e26124a34d098d0b9)(void);

99

[ 103](group__hawkbit.md#ga03631b12a4107d660bac14bfd33bfebd)void [hawkbit\_reboot](group__hawkbit.md#ga03631b12a4107d660bac14bfd33bfebd)(void);

104

[ 111](group__hawkbit.md#ga154220c632a7594c0630cdcd79385055)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[hawkbit\_get\_device\_identity\_cb\_handler\_t](group__hawkbit.md#ga154220c632a7594c0630cdcd79385055))(char \*id, int id\_max\_len);

112

[ 123](group__hawkbit.md#ga4ce085b8f2bb46af2c2e9f3f2879d633)int [hawkbit\_set\_device\_identity\_cb](group__hawkbit.md#ga4ce085b8f2bb46af2c2e9f3f2879d633)([hawkbit\_get\_device\_identity\_cb\_handler\_t](group__hawkbit.md#ga154220c632a7594c0630cdcd79385055) cb);

124

[ 135](group__hawkbit.md#ga26f0066c87c57b500170ac377b560bb4)int [hawkbit\_reset\_action\_id](group__hawkbit.md#ga26f0066c87c57b500170ac377b560bb4)(void);

136

140

141#endif /\* ZEPHYR\_INCLUDE\_MGMT\_HAWKBIT\_HAWKBIT\_H\_ \*/

[hawkbit\_reboot](group__hawkbit.md#ga03631b12a4107d660bac14bfd33bfebd)

void hawkbit\_reboot(void)

Request system to reboot.

[hawkbit\_init](group__hawkbit.md#ga0ef6151f205088405de242e012984ca6)

int hawkbit\_init(void)

Init the flash partition.

[hawkbit\_get\_device\_identity\_cb\_handler\_t](group__hawkbit.md#ga154220c632a7594c0630cdcd79385055)

bool(\* hawkbit\_get\_device\_identity\_cb\_handler\_t)(char \*id, int id\_max\_len)

Callback to get the device identity.

**Definition** hawkbit.h:111

[hawkbit\_reset\_action\_id](group__hawkbit.md#ga26f0066c87c57b500170ac377b560bb4)

int hawkbit\_reset\_action\_id(void)

Resets the hawkBit action id, that is saved in settings.

[hawkbit\_config\_device\_data\_cb\_handler\_t](group__hawkbit.md#ga2774769ec44f2793895b5d783b4dceda)

int(\* hawkbit\_config\_device\_data\_cb\_handler\_t)(const char \*device\_id, uint8\_t \*buffer, const size\_t buffer\_size)

Callback to provide the custom data to the hawkBit server.

**Definition** hawkbit.h:69

[hawkbit\_set\_device\_identity\_cb](group__hawkbit.md#ga4ce085b8f2bb46af2c2e9f3f2879d633)

int hawkbit\_set\_device\_identity\_cb(hawkbit\_get\_device\_identity\_cb\_handler\_t cb)

Set the device identity callback.

[hawkbit\_probe](group__hawkbit.md#ga525173f0c3d0ca4e26124a34d098d0b9)

enum hawkbit\_response hawkbit\_probe(void)

The hawkBit probe verify if there is some update to be performed.

[hawkbit\_response](group__hawkbit.md#ga96c59c754178451d8dbd08b32813220b)

hawkbit\_response

Response message from hawkBit.

**Definition** hawkbit.h:33

[hawkbit\_set\_custom\_data\_cb](group__hawkbit.md#gad8e83255a969eb61244b1edfd0b95e5d)

int hawkbit\_set\_custom\_data\_cb(hawkbit\_config\_device\_data\_cb\_handler\_t cb)

Set the custom data callback.

[HAWKBIT\_PERMISSION\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba1d79e6fe8487cc4dc36c6c91bcabd124)

@ HAWKBIT\_PERMISSION\_ERROR

fail to get the permission to access the hawkBit server

**Definition** hawkbit.h:45

[HAWKBIT\_PROBE\_IN\_PROGRESS](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba28ccbb4060d41592884829cf205414f6)

@ HAWKBIT\_PROBE\_IN\_PROGRESS

probe is currently running

**Definition** hawkbit.h:55

[HAWKBIT\_METADATA\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba2b7d188d8c28a3373d9b8a7f831b1e3a)

@ HAWKBIT\_METADATA\_ERROR

fail to parse or to encode the metadata

**Definition** hawkbit.h:47

[HAWKBIT\_NETWORKING\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba5a36eadcadc43c1fd0936a8546fb15e8)

@ HAWKBIT\_NETWORKING\_ERROR

fail to connect to the hawkBit server

**Definition** hawkbit.h:41

[HAWKBIT\_UPDATE\_INSTALLED](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba9f5a200928474863a88d170c11594048)

@ HAWKBIT\_UPDATE\_INSTALLED

an update was installed.

**Definition** hawkbit.h:37

[HAWKBIT\_NO\_RESPONSE](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220baa18639f74548a317808b24c702f2fcb9)

@ HAWKBIT\_NO\_RESPONSE

matching events were not received within the specified time

**Definition** hawkbit.h:35

[HAWKBIT\_NOT\_INITIALIZED](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bac4ba42120229e92b52c82d4a4d4cd708)

@ HAWKBIT\_NOT\_INITIALIZED

hawkBit is not initialized

**Definition** hawkbit.h:53

[HAWKBIT\_NO\_UPDATE](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bac73c46deb3e54dba690f814a2fb9db71)

@ HAWKBIT\_NO\_UPDATE

no update was available

**Definition** hawkbit.h:39

[HAWKBIT\_ALLOC\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bacee282923e7435b81794ccec9749ce01)

@ HAWKBIT\_ALLOC\_ERROR

fail to allocate memory

**Definition** hawkbit.h:51

[HAWKBIT\_UNCONFIRMED\_IMAGE](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bad4b0587da0bdfd829d0d08ed2407357d)

@ HAWKBIT\_UNCONFIRMED\_IMAGE

image is unconfirmed

**Definition** hawkbit.h:43

[HAWKBIT\_DOWNLOAD\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220baf1a448b0addfc769515c725ce5b1bab9)

@ HAWKBIT\_DOWNLOAD\_ERROR

fail while downloading the update package

**Definition** hawkbit.h:49

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [hawkbit](dir_a48dfaa3f142fb7c063e17169510ae85.md)
- [hawkbit.h](hawkbit_2hawkbit_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

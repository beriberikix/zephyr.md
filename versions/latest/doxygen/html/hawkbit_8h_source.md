---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/hawkbit_8h_source.html
original_path: doxygen/html/hawkbit_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hawkbit.h

[Go to the documentation of this file.](hawkbit_8h.md)

1/\*

2 \* Copyright (c) 2020 Linumiz

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13#ifndef ZEPHYR\_INCLUDE\_MGMT\_HAWKBIT\_H\_

14#define ZEPHYR\_INCLUDE\_MGMT\_HAWKBIT\_H\_

15

[ 16](group__hawkbit.md#gae2550864ddf596fe544052af73dc1dba)#define HAWKBIT\_JSON\_URL "/default/controller/v1"

17

[ 26](group__hawkbit.md#ga96c59c754178451d8dbd08b32813220b)enum [hawkbit\_response](group__hawkbit.md#ga96c59c754178451d8dbd08b32813220b) {

[ 27](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba5a36eadcadc43c1fd0936a8546fb15e8) [HAWKBIT\_NETWORKING\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba5a36eadcadc43c1fd0936a8546fb15e8),

[ 28](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bad4b0587da0bdfd829d0d08ed2407357d) [HAWKBIT\_UNCONFIRMED\_IMAGE](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bad4b0587da0bdfd829d0d08ed2407357d),

[ 29](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba1d79e6fe8487cc4dc36c6c91bcabd124) [HAWKBIT\_PERMISSION\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba1d79e6fe8487cc4dc36c6c91bcabd124),

[ 30](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba2b7d188d8c28a3373d9b8a7f831b1e3a) [HAWKBIT\_METADATA\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba2b7d188d8c28a3373d9b8a7f831b1e3a),

[ 31](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220baf1a448b0addfc769515c725ce5b1bab9) [HAWKBIT\_DOWNLOAD\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220baf1a448b0addfc769515c725ce5b1bab9),

[ 32](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba6af6cd1b834d74a5298f4b3626b48ad3) [HAWKBIT\_OK](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba6af6cd1b834d74a5298f4b3626b48ad3),

[ 33](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba9f5a200928474863a88d170c11594048) [HAWKBIT\_UPDATE\_INSTALLED](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba9f5a200928474863a88d170c11594048),

[ 34](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bac73c46deb3e54dba690f814a2fb9db71) [HAWKBIT\_NO\_UPDATE](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bac73c46deb3e54dba690f814a2fb9db71),

[ 35](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba9d677899d5ff00957dfeab70f484863f) [HAWKBIT\_CANCEL\_UPDATE](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba9d677899d5ff00957dfeab70f484863f),

[ 36](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba28ccbb4060d41592884829cf205414f6) [HAWKBIT\_PROBE\_IN\_PROGRESS](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba28ccbb4060d41592884829cf205414f6),

37};

38

[ 44](group__hawkbit.md#ga0ef6151f205088405de242e012984ca6)int [hawkbit\_init](group__hawkbit.md#ga0ef6151f205088405de242e012984ca6)(void);

45

[ 52](group__hawkbit.md#gac077f546d8947d6b55dcb9276ce98283)void [hawkbit\_autohandler](group__hawkbit.md#gac077f546d8947d6b55dcb9276ce98283)(void);

53

[ 64](group__hawkbit.md#ga525173f0c3d0ca4e26124a34d098d0b9)enum [hawkbit\_response](group__hawkbit.md#ga96c59c754178451d8dbd08b32813220b) [hawkbit\_probe](group__hawkbit.md#ga525173f0c3d0ca4e26124a34d098d0b9)(void);

65

69

70#endif /\* \_HAWKBIT\_H\_ \*/

[hawkbit\_init](group__hawkbit.md#ga0ef6151f205088405de242e012984ca6)

int hawkbit\_init(void)

Init the flash partition.

[hawkbit\_probe](group__hawkbit.md#ga525173f0c3d0ca4e26124a34d098d0b9)

enum hawkbit\_response hawkbit\_probe(void)

The hawkBit probe verify if there is some update to be performed.

[hawkbit\_response](group__hawkbit.md#ga96c59c754178451d8dbd08b32813220b)

hawkbit\_response

Response message from hawkBit.

**Definition** hawkbit.h:26

[hawkbit\_autohandler](group__hawkbit.md#gac077f546d8947d6b55dcb9276ce98283)

void hawkbit\_autohandler(void)

Runs hawkBit probe and hawkBit update automatically.

[HAWKBIT\_PERMISSION\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba1d79e6fe8487cc4dc36c6c91bcabd124)

@ HAWKBIT\_PERMISSION\_ERROR

**Definition** hawkbit.h:29

[HAWKBIT\_PROBE\_IN\_PROGRESS](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba28ccbb4060d41592884829cf205414f6)

@ HAWKBIT\_PROBE\_IN\_PROGRESS

**Definition** hawkbit.h:36

[HAWKBIT\_METADATA\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba2b7d188d8c28a3373d9b8a7f831b1e3a)

@ HAWKBIT\_METADATA\_ERROR

**Definition** hawkbit.h:30

[HAWKBIT\_NETWORKING\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba5a36eadcadc43c1fd0936a8546fb15e8)

@ HAWKBIT\_NETWORKING\_ERROR

**Definition** hawkbit.h:27

[HAWKBIT\_OK](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba6af6cd1b834d74a5298f4b3626b48ad3)

@ HAWKBIT\_OK

**Definition** hawkbit.h:32

[HAWKBIT\_CANCEL\_UPDATE](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba9d677899d5ff00957dfeab70f484863f)

@ HAWKBIT\_CANCEL\_UPDATE

**Definition** hawkbit.h:35

[HAWKBIT\_UPDATE\_INSTALLED](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba9f5a200928474863a88d170c11594048)

@ HAWKBIT\_UPDATE\_INSTALLED

**Definition** hawkbit.h:33

[HAWKBIT\_NO\_UPDATE](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bac73c46deb3e54dba690f814a2fb9db71)

@ HAWKBIT\_NO\_UPDATE

**Definition** hawkbit.h:34

[HAWKBIT\_UNCONFIRMED\_IMAGE](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bad4b0587da0bdfd829d0d08ed2407357d)

@ HAWKBIT\_UNCONFIRMED\_IMAGE

**Definition** hawkbit.h:28

[HAWKBIT\_DOWNLOAD\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220baf1a448b0addfc769515c725ce5b1bab9)

@ HAWKBIT\_DOWNLOAD\_ERROR

**Definition** hawkbit.h:31

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [hawkbit.h](hawkbit_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/os__mgmt_8h_source.html
original_path: doxygen/html/os__mgmt_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

os\_mgmt.h

[Go to the documentation of this file.](os__mgmt_8h.md)

1/\*

2 \* Copyright (c) 2018-2021 mcumgr authors

3 \* Copyright (c) 2022 Laird Connectivity

4 \* Copyright (c) 2023 Nordic Semiconductor ASA

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef H\_OS\_MGMT\_

10#define H\_OS\_MGMT\_

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

[ 19](os__mgmt_8h.md#a24751ec5a8ba224238f484e2048f152a)#define OS\_MGMT\_ID\_ECHO 0

[ 20](os__mgmt_8h.md#a0093a8df477e7114ffa195a022851cbe)#define OS\_MGMT\_ID\_CONS\_ECHO\_CTRL 1

[ 21](os__mgmt_8h.md#a067886d5d5d1d8979f93bab61fc2a670)#define OS\_MGMT\_ID\_TASKSTAT 2

[ 22](os__mgmt_8h.md#aa2918e287d063fb2a82bd87d5c29aba4)#define OS\_MGMT\_ID\_MPSTAT 3

[ 23](os__mgmt_8h.md#af4370119858111637ee80af735b0e50c)#define OS\_MGMT\_ID\_DATETIME\_STR 4

[ 24](os__mgmt_8h.md#a4447fa2fa0c5f37713f7ef555174e814)#define OS\_MGMT\_ID\_RESET 5

[ 25](os__mgmt_8h.md#a6eb9918c2e6d1564fc362fe3dcdc63d5)#define OS\_MGMT\_ID\_MCUMGR\_PARAMS 6

[ 26](os__mgmt_8h.md#a0103b1f0d37106c5166b1793c7743513)#define OS\_MGMT\_ID\_INFO 7

[ 27](os__mgmt_8h.md#a142393f94135f1dd91b8cf098e01aa6b)#define OS\_MGMT\_ID\_BOOTLOADER\_INFO 8

28

[ 32](os__mgmt_8h.md#a14dc9256e6585450ea34b13666aa8765)enum [os\_mgmt\_err\_code\_t](os__mgmt_8h.md#a14dc9256e6585450ea34b13666aa8765) {

[ 34](os__mgmt_8h.md#a14dc9256e6585450ea34b13666aa8765a25f3f37eb72fae4e2a074ee0115014f4) [OS\_MGMT\_ERR\_OK](os__mgmt_8h.md#a14dc9256e6585450ea34b13666aa8765a25f3f37eb72fae4e2a074ee0115014f4) = 0,

35

[ 37](os__mgmt_8h.md#a14dc9256e6585450ea34b13666aa8765a401c167c9780d54de8af0d5a49d07752) [OS\_MGMT\_ERR\_UNKNOWN](os__mgmt_8h.md#a14dc9256e6585450ea34b13666aa8765a401c167c9780d54de8af0d5a49d07752),

38

[ 40](os__mgmt_8h.md#a14dc9256e6585450ea34b13666aa8765a8367c0f0a31be507a67a3e981a8d14dd) [OS\_MGMT\_ERR\_INVALID\_FORMAT](os__mgmt_8h.md#a14dc9256e6585450ea34b13666aa8765a8367c0f0a31be507a67a3e981a8d14dd),

41

[ 43](os__mgmt_8h.md#a14dc9256e6585450ea34b13666aa8765ad28fc3f5aa39ae710d83c9140423cb1d) [OS\_MGMT\_ERR\_QUERY\_YIELDS\_NO\_ANSWER](os__mgmt_8h.md#a14dc9256e6585450ea34b13666aa8765ad28fc3f5aa39ae710d83c9140423cb1d),

44

[ 46](os__mgmt_8h.md#a14dc9256e6585450ea34b13666aa8765a654f35347c0a92d45de8c39161c0a517) [OS\_MGMT\_ERR\_RTC\_NOT\_SET](os__mgmt_8h.md#a14dc9256e6585450ea34b13666aa8765a654f35347c0a92d45de8c39161c0a517),

47

[ 49](os__mgmt_8h.md#a14dc9256e6585450ea34b13666aa8765a110d57281369d1b5a8c1a1863dcb633a) [OS\_MGMT\_ERR\_RTC\_COMMAND\_FAILED](os__mgmt_8h.md#a14dc9256e6585450ea34b13666aa8765a110d57281369d1b5a8c1a1863dcb633a),

50};

51

52/\* Bitmask values used by the os info command handler. Note that the width of this variable is

53 \* 32-bits, allowing 32 flags, custom user-level implementations should start at

54 \* OS\_MGMT\_INFO\_FORMAT\_USER\_CUSTOM\_START and reference that directly as additional format

55 \* specifiers might be added to this list in the future.

56 \*/

[ 57](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26f)enum [os\_mgmt\_info\_formats](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26f) {

[ 58](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26faef8107b37da9f80226729774b2b658a0) [OS\_MGMT\_INFO\_FORMAT\_KERNEL\_NAME](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26faef8107b37da9f80226729774b2b658a0) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 59](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26fa5c2b986a7e1c24e319e940193e6333e3) [OS\_MGMT\_INFO\_FORMAT\_NODE\_NAME](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26fa5c2b986a7e1c24e319e940193e6333e3) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 60](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26fa16d8270fccec21d7672ce417292114bd) [OS\_MGMT\_INFO\_FORMAT\_KERNEL\_RELEASE](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26fa16d8270fccec21d7672ce417292114bd) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 61](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26fa07febed600a0fb099942b9cc1267e328) [OS\_MGMT\_INFO\_FORMAT\_KERNEL\_VERSION](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26fa07febed600a0fb099942b9cc1267e328) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 62](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26fac5667c4a29bf2c5a0183bae3d963045d) [OS\_MGMT\_INFO\_FORMAT\_BUILD\_DATE\_TIME](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26fac5667c4a29bf2c5a0183bae3d963045d) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 63](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26fa1d7217a77e0463c984615efa33142848) [OS\_MGMT\_INFO\_FORMAT\_MACHINE](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26fa1d7217a77e0463c984615efa33142848) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

[ 64](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26fa1279c1778984153bc77c0e34ee6c2082) [OS\_MGMT\_INFO\_FORMAT\_PROCESSOR](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26fa1279c1778984153bc77c0e34ee6c2082) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

[ 65](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26fa19d79c2eba087c14a4d4082d48e77fa5) [OS\_MGMT\_INFO\_FORMAT\_HARDWARE\_PLATFORM](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26fa19d79c2eba087c14a4d4082d48e77fa5) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

[ 66](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26fa6ccf1e846fb57c9957c5f1698f1fba76) [OS\_MGMT\_INFO\_FORMAT\_OPERATING\_SYSTEM](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26fa6ccf1e846fb57c9957c5f1698f1fba76) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8),

67

[ 68](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26fa7f409757f5912d9f950b0566896803e2) [OS\_MGMT\_INFO\_FORMAT\_USER\_CUSTOM\_START](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26fa7f409757f5912d9f950b0566896803e2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9),

69};

70

71/\* Structure provided in the MGMT\_EVT\_OP\_OS\_MGMT\_INFO\_CHECK notification callback \*/

[ 72](structos__mgmt__info__check.md)struct [os\_mgmt\_info\_check](structos__mgmt__info__check.md) {

73 /\* Input format string from the mcumgr client \*/

[ 74](structos__mgmt__info__check.md#aa5da5de4bfd4f9f54319458c3c8a5fbb) struct zcbor\_string \*[format](structos__mgmt__info__check.md#aa5da5de4bfd4f9f54319458c3c8a5fbb);

75 /\* Bitmask of values specifying which outputs should be present \*/

[ 76](structos__mgmt__info__check.md#a068e3425bf3a12b043f26b0d6dd07267) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[format\_bitmask](structos__mgmt__info__check.md#a068e3425bf3a12b043f26b0d6dd07267);

77 /\* Number of valid format characters parsed, must be incremented by 1 for each valid

78 \* character

79 \*/

[ 80](structos__mgmt__info__check.md#a7aae2f1feb1adfdc18f11a671c3bad26) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*[valid\_formats](structos__mgmt__info__check.md#a7aae2f1feb1adfdc18f11a671c3bad26);

81 /\* Needs to be set to true if the OS name is being provided by external code \*/

[ 82](structos__mgmt__info__check.md#a09c4371a4bfa20192411fff922747a2c) bool \*[custom\_os\_name](structos__mgmt__info__check.md#a09c4371a4bfa20192411fff922747a2c);

83};

84

85/\* Structure provided in the MGMT\_EVT\_OP\_OS\_MGMT\_INFO\_APPEND notification callback \*/

[ 86](structos__mgmt__info__append.md)struct [os\_mgmt\_info\_append](structos__mgmt__info__append.md) {

87 /\* The format bitmask from the processed commands, the bits should be cleared once

88 \* processed, note that if all\_format\_specified is specified, the corrisponding bits here

89 \* will not be set

90 \*/

[ 91](structos__mgmt__info__append.md#a6c43c79ab799b7b585453ead48f3c1a3) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[format\_bitmask](structos__mgmt__info__append.md#a6c43c79ab799b7b585453ead48f3c1a3);

92 /\* Will be true if the all 'a' specifier was provided \*/

[ 93](structos__mgmt__info__append.md#abf016939fbc1d0aaba9712dfacf2d04f) bool [all\_format\_specified](structos__mgmt__info__append.md#abf016939fbc1d0aaba9712dfacf2d04f);

94 /\* The output buffer which the responses should be appended to. If prior\_output is true, a

95 \* space must be added prior to the output response

96 \*/

[ 97](structos__mgmt__info__append.md#a1fb38ad80f92519c649aab7ef258095b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[output](structos__mgmt__info__append.md#a1fb38ad80f92519c649aab7ef258095b);

98 /\* The current size of the output response in the output buffer, must be updated to be the

99 \* size of the output response after appending data

100 \*/

[ 101](structos__mgmt__info__append.md#acd3e277aef6b3bc69346996c073f993b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*[output\_length](structos__mgmt__info__append.md#acd3e277aef6b3bc69346996c073f993b);

102 /\* The size of the output buffer, including null terminator character, if the output

103 \* response would exceed this size, the function must abort and return false to return a

104 \* memory error to the client

105 \*/

[ 106](structos__mgmt__info__append.md#ae96963a00ef4b15099cf36399a159382) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [buffer\_size](structos__mgmt__info__append.md#ae96963a00ef4b15099cf36399a159382);

107 /\* If there has been prior output, must be set to true if a response has been output \*/

[ 108](structos__mgmt__info__append.md#acc89541b668ff791a1927c549d36b1b2) bool \*[prior\_output](structos__mgmt__info__append.md#acc89541b668ff791a1927c549d36b1b2);

109};

110

111#ifdef \_\_cplusplus

112}

113#endif

114

115#endif /\* H\_OS\_MGMT\_ \*/

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[os\_mgmt\_err\_code\_t](os__mgmt_8h.md#a14dc9256e6585450ea34b13666aa8765)

os\_mgmt\_err\_code\_t

Command result codes for OS management group.

**Definition** os\_mgmt.h:32

[OS\_MGMT\_ERR\_RTC\_COMMAND\_FAILED](os__mgmt_8h.md#a14dc9256e6585450ea34b13666aa8765a110d57281369d1b5a8c1a1863dcb633a)

@ OS\_MGMT\_ERR\_RTC\_COMMAND\_FAILED

RTC command failed.

**Definition** os\_mgmt.h:49

[OS\_MGMT\_ERR\_OK](os__mgmt_8h.md#a14dc9256e6585450ea34b13666aa8765a25f3f37eb72fae4e2a074ee0115014f4)

@ OS\_MGMT\_ERR\_OK

No error, this is implied if there is no ret value in the response.

**Definition** os\_mgmt.h:34

[OS\_MGMT\_ERR\_UNKNOWN](os__mgmt_8h.md#a14dc9256e6585450ea34b13666aa8765a401c167c9780d54de8af0d5a49d07752)

@ OS\_MGMT\_ERR\_UNKNOWN

Unknown error occurred.

**Definition** os\_mgmt.h:37

[OS\_MGMT\_ERR\_RTC\_NOT\_SET](os__mgmt_8h.md#a14dc9256e6585450ea34b13666aa8765a654f35347c0a92d45de8c39161c0a517)

@ OS\_MGMT\_ERR\_RTC\_NOT\_SET

RTC is not set.

**Definition** os\_mgmt.h:46

[OS\_MGMT\_ERR\_INVALID\_FORMAT](os__mgmt_8h.md#a14dc9256e6585450ea34b13666aa8765a8367c0f0a31be507a67a3e981a8d14dd)

@ OS\_MGMT\_ERR\_INVALID\_FORMAT

The provided format value is not valid.

**Definition** os\_mgmt.h:40

[OS\_MGMT\_ERR\_QUERY\_YIELDS\_NO\_ANSWER](os__mgmt_8h.md#a14dc9256e6585450ea34b13666aa8765ad28fc3f5aa39ae710d83c9140423cb1d)

@ OS\_MGMT\_ERR\_QUERY\_YIELDS\_NO\_ANSWER

Query was not recognized.

**Definition** os\_mgmt.h:43

[os\_mgmt\_info\_formats](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26f)

os\_mgmt\_info\_formats

**Definition** os\_mgmt.h:57

[OS\_MGMT\_INFO\_FORMAT\_KERNEL\_VERSION](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26fa07febed600a0fb099942b9cc1267e328)

@ OS\_MGMT\_INFO\_FORMAT\_KERNEL\_VERSION

**Definition** os\_mgmt.h:61

[OS\_MGMT\_INFO\_FORMAT\_PROCESSOR](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26fa1279c1778984153bc77c0e34ee6c2082)

@ OS\_MGMT\_INFO\_FORMAT\_PROCESSOR

**Definition** os\_mgmt.h:64

[OS\_MGMT\_INFO\_FORMAT\_KERNEL\_RELEASE](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26fa16d8270fccec21d7672ce417292114bd)

@ OS\_MGMT\_INFO\_FORMAT\_KERNEL\_RELEASE

**Definition** os\_mgmt.h:60

[OS\_MGMT\_INFO\_FORMAT\_HARDWARE\_PLATFORM](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26fa19d79c2eba087c14a4d4082d48e77fa5)

@ OS\_MGMT\_INFO\_FORMAT\_HARDWARE\_PLATFORM

**Definition** os\_mgmt.h:65

[OS\_MGMT\_INFO\_FORMAT\_MACHINE](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26fa1d7217a77e0463c984615efa33142848)

@ OS\_MGMT\_INFO\_FORMAT\_MACHINE

**Definition** os\_mgmt.h:63

[OS\_MGMT\_INFO\_FORMAT\_NODE\_NAME](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26fa5c2b986a7e1c24e319e940193e6333e3)

@ OS\_MGMT\_INFO\_FORMAT\_NODE\_NAME

**Definition** os\_mgmt.h:59

[OS\_MGMT\_INFO\_FORMAT\_OPERATING\_SYSTEM](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26fa6ccf1e846fb57c9957c5f1698f1fba76)

@ OS\_MGMT\_INFO\_FORMAT\_OPERATING\_SYSTEM

**Definition** os\_mgmt.h:66

[OS\_MGMT\_INFO\_FORMAT\_USER\_CUSTOM\_START](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26fa7f409757f5912d9f950b0566896803e2)

@ OS\_MGMT\_INFO\_FORMAT\_USER\_CUSTOM\_START

**Definition** os\_mgmt.h:68

[OS\_MGMT\_INFO\_FORMAT\_BUILD\_DATE\_TIME](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26fac5667c4a29bf2c5a0183bae3d963045d)

@ OS\_MGMT\_INFO\_FORMAT\_BUILD\_DATE\_TIME

**Definition** os\_mgmt.h:62

[OS\_MGMT\_INFO\_FORMAT\_KERNEL\_NAME](os__mgmt_8h.md#a54512f3d774835d1d277872835a3b26faef8107b37da9f80226729774b2b658a0)

@ OS\_MGMT\_INFO\_FORMAT\_KERNEL\_NAME

**Definition** os\_mgmt.h:58

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[os\_mgmt\_info\_append](structos__mgmt__info__append.md)

**Definition** os\_mgmt.h:86

[os\_mgmt\_info\_append::output](structos__mgmt__info__append.md#a1fb38ad80f92519c649aab7ef258095b)

uint8\_t \* output

**Definition** os\_mgmt.h:97

[os\_mgmt\_info\_append::format\_bitmask](structos__mgmt__info__append.md#a6c43c79ab799b7b585453ead48f3c1a3)

uint32\_t \* format\_bitmask

**Definition** os\_mgmt.h:91

[os\_mgmt\_info\_append::all\_format\_specified](structos__mgmt__info__append.md#abf016939fbc1d0aaba9712dfacf2d04f)

bool all\_format\_specified

**Definition** os\_mgmt.h:93

[os\_mgmt\_info\_append::prior\_output](structos__mgmt__info__append.md#acc89541b668ff791a1927c549d36b1b2)

bool \* prior\_output

**Definition** os\_mgmt.h:108

[os\_mgmt\_info\_append::output\_length](structos__mgmt__info__append.md#acd3e277aef6b3bc69346996c073f993b)

uint16\_t \* output\_length

**Definition** os\_mgmt.h:101

[os\_mgmt\_info\_append::buffer\_size](structos__mgmt__info__append.md#ae96963a00ef4b15099cf36399a159382)

uint16\_t buffer\_size

**Definition** os\_mgmt.h:106

[os\_mgmt\_info\_check](structos__mgmt__info__check.md)

**Definition** os\_mgmt.h:72

[os\_mgmt\_info\_check::format\_bitmask](structos__mgmt__info__check.md#a068e3425bf3a12b043f26b0d6dd07267)

uint32\_t \* format\_bitmask

**Definition** os\_mgmt.h:76

[os\_mgmt\_info\_check::custom\_os\_name](structos__mgmt__info__check.md#a09c4371a4bfa20192411fff922747a2c)

bool \* custom\_os\_name

**Definition** os\_mgmt.h:82

[os\_mgmt\_info\_check::valid\_formats](structos__mgmt__info__check.md#a7aae2f1feb1adfdc18f11a671c3bad26)

uint16\_t \* valid\_formats

**Definition** os\_mgmt.h:80

[os\_mgmt\_info\_check::format](structos__mgmt__info__check.md#aa5da5de4bfd4f9f54319458c3c8a5fbb)

struct zcbor\_string \* format

**Definition** os\_mgmt.h:74

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [os\_mgmt](dir_1a5ff9dfdb0e06a8ce3ba8e3db8b26fb.md)
- [os\_mgmt.h](os__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

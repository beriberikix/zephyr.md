---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/esai_8h_source.html
original_path: doxygen/html/esai_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esai.h

[Go to the documentation of this file.](esai_8h.md)

1/\*

2 \* Copyright 2024 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef \_INCLUDE\_ZEPHYR\_DT\_BINDINGS\_DAI\_ESAI\_H\_

8#define \_INCLUDE\_ZEPHYR\_DT\_BINDINGS\_DAI\_ESAI\_H\_

9

10/\* ESAI pin IDs

11 \* the values of these macros are meant to match

12 \* the bit position from PCRC/PRRC's PC/PDC associated

13 \* with each of these pins.

14 \*/

[ 15](esai_8h.md#a0ecf07d3d8c2c903415855b8f965acb0)#define ESAI\_PIN\_SCKR 0

[ 16](esai_8h.md#aaa068c1d85f68a1920c09869f0357fb0)#define ESAI\_PIN\_FSR 1

[ 17](esai_8h.md#a51c7d00b37bc05083003cd6dbced3729)#define ESAI\_PIN\_HCKR 2

[ 18](esai_8h.md#af7b3a20b6d2bd2d5981fdbbf2b0aa724)#define ESAI\_PIN\_SCKT 3

[ 19](esai_8h.md#a39a776b51d482d1d3703687d1245707b)#define ESAI\_PIN\_FST 4

[ 20](esai_8h.md#a8d1d03217fa1c8a34b4da979fd9109f6)#define ESAI\_PIN\_HCKT 5

[ 21](esai_8h.md#a0be21dd83a00fb159ebaab72d0167963)#define ESAI\_PIN\_SDO5\_SDI0 6

[ 22](esai_8h.md#ad37097a420f0c7a3a02b91e4dba4ff30)#define ESAI\_PIN\_SDO4\_SDI1 7

[ 23](esai_8h.md#afef3657ae9abe5b87825130e339da830)#define ESAI\_PIN\_SDO3\_SDI2 8

[ 24](esai_8h.md#a7123d6105473a424d5e19ef9a19b0199)#define ESAI\_PIN\_SDO2\_SDI3 9

[ 25](esai_8h.md#aa17e5a390c45ea4178099101ac237a69)#define ESAI\_PIN\_SDO1 10

[ 26](esai_8h.md#a07435a87e30cf1515e531e4c8d2dba9c)#define ESAI\_PIN\_SDO0 11

27

28/\* ESAI pin modes

29 \* the values of these macros are set according to

30 \* the following table:

31 \*

32 \* PDC = 0, PC = 0 => DISCONNECTED (0)

33 \* PDC = 0, PC = 1 => GPIO INPUT (1)

34 \* PDC = 1, PC = 0 => GPIO OUTPUT (2)

35 \* PDC = 1, PC = 1 => ESAI (3)

36 \*/

[ 37](esai_8h.md#ac56cf8438edfd9a85874e483ce60c735)#define ESAI\_PIN\_DISCONNECTED 0

[ 38](esai_8h.md#af8daf7391a773a57c7ec12533dc37311)#define ESAI\_PIN\_GPIO\_INPUT 1

[ 39](esai_8h.md#a44ed57556dec275c32655a744d9a73e1)#define ESAI\_PIN\_GPIO\_OUTPUT 2

[ 40](esai_8h.md#a6b646d2a0fca23ae6d64fc23e7f22b82)#define ESAI\_PIN\_ESAI 3

41

42/\* ESAI clock IDs \*/

[ 43](esai_8h.md#a4e42ff9c73e9c4fea3dd64094c2dbe4b)#define ESAI\_CLOCK\_HCKT 0

[ 44](esai_8h.md#a17e8525d3614a83135c1db5e4c01cfb9)#define ESAI\_CLOCK\_HCKR 1

[ 45](esai_8h.md#a1ee9d84226904ec56d5c0b0a3cdc4029)#define ESAI\_CLOCK\_SCKR 2

[ 46](esai_8h.md#ae88b5ef4c02cc0295370bd3eadbbed4d)#define ESAI\_CLOCK\_SCKT 3

[ 47](esai_8h.md#af276b6b50ad3547a86781ad62046559f)#define ESAI\_CLOCK\_FSR 4

[ 48](esai_8h.md#af6b2e21a927badb50d300d77c80a8a87)#define ESAI\_CLOCK\_FST 5

49

50/\* ESAI clock directions \*/

[ 51](esai_8h.md#a7a507b5077c73ffd5b283edbb468d083)#define ESAI\_CLOCK\_INPUT 0

[ 52](esai_8h.md#a6396996ca6821c8dba963c013e7496f3)#define ESAI\_CLOCK\_OUTPUT 1

53

54#endif /\* \_INCLUDE\_ZEPHYR\_DT\_BINDINGS\_DAI\_ESAI\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [dai](dir_a572f0b88e12c9a0d1447f9e03031b53.md)
- [esai.h](esai_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

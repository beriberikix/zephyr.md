---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/mcp7940n_8h_source.html
original_path: doxygen/html/mcp7940n_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mcp7940n.h

[Go to the documentation of this file.](mcp7940n_8h.md)

1/\*

2 \* Copyright (c) 2021 Laird Connectivity

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_RTC\_MCP7940N\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_RTC\_MCP7940N\_H\_

9

10#include <[zephyr/sys/timeutil.h](timeutil_8h.md)>

11#include <time.h>

12

[ 13](structmcp7940n__rtc__sec.md)struct [mcp7940n\_rtc\_sec](structmcp7940n__rtc__sec.md) {

[ 14](structmcp7940n__rtc__sec.md#ace288b683bce6aeb2b69c7db69c217b2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sec\_one](structmcp7940n__rtc__sec.md#ace288b683bce6aeb2b69c7db69c217b2) : 4;

[ 15](structmcp7940n__rtc__sec.md#a9c381492f172f8aaa64c4da6a8d647fb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sec\_ten](structmcp7940n__rtc__sec.md#a9c381492f172f8aaa64c4da6a8d647fb) : 3;

[ 16](structmcp7940n__rtc__sec.md#acf5d8dacfdd0f59fda45aa1701a80d16) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [start\_osc](structmcp7940n__rtc__sec.md#acf5d8dacfdd0f59fda45aa1701a80d16) : 1;

17} \_\_packed;

18

[ 19](structmcp7940n__rtc__min.md)struct [mcp7940n\_rtc\_min](structmcp7940n__rtc__min.md) {

[ 20](structmcp7940n__rtc__min.md#aa9a0c45db431a07251e1101c0c7c1fb9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [min\_one](structmcp7940n__rtc__min.md#aa9a0c45db431a07251e1101c0c7c1fb9) : 4;

[ 21](structmcp7940n__rtc__min.md#a75e2870f8f221b2edf6786d786b098f0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [min\_ten](structmcp7940n__rtc__min.md#a75e2870f8f221b2edf6786d786b098f0) : 3;

[ 22](structmcp7940n__rtc__min.md#aabfa681bfc2f45e1f6447ddf6d996592) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [nimp](structmcp7940n__rtc__min.md#aabfa681bfc2f45e1f6447ddf6d996592) : 1;

23} \_\_packed;

24

[ 25](structmcp7940n__rtc__hours.md)struct [mcp7940n\_rtc\_hours](structmcp7940n__rtc__hours.md) {

[ 26](structmcp7940n__rtc__hours.md#a9b2346401aaeb8bffd9f7ddfd0038bff) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [hr\_one](structmcp7940n__rtc__hours.md#a9b2346401aaeb8bffd9f7ddfd0038bff) : 4;

[ 27](structmcp7940n__rtc__hours.md#aa187c1bb717f8d2c09dc4f067c61a4f3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [hr\_ten](structmcp7940n__rtc__hours.md#aa187c1bb717f8d2c09dc4f067c61a4f3) : 2;

[ 28](structmcp7940n__rtc__hours.md#a7c45eca341d518a9d922ffa68f8cdc6b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [twelve\_hr](structmcp7940n__rtc__hours.md#a7c45eca341d518a9d922ffa68f8cdc6b) : 1;

[ 29](structmcp7940n__rtc__hours.md#a8e238443f2e19c2c2feeb5a9e5854356) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [nimp](structmcp7940n__rtc__hours.md#a8e238443f2e19c2c2feeb5a9e5854356) : 1;

30} \_\_packed;

31

[ 32](structmcp7940n__rtc__weekday.md)struct [mcp7940n\_rtc\_weekday](structmcp7940n__rtc__weekday.md) {

[ 33](structmcp7940n__rtc__weekday.md#a9aad56ee23af55ea2f41020d96095ddd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [weekday](structmcp7940n__rtc__weekday.md#a9aad56ee23af55ea2f41020d96095ddd) : 3;

[ 34](structmcp7940n__rtc__weekday.md#ad904822d76ac2f170807b3d6260061a3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [vbaten](structmcp7940n__rtc__weekday.md#ad904822d76ac2f170807b3d6260061a3) : 1;

[ 35](structmcp7940n__rtc__weekday.md#a5ce2be23d666085e0d3af23e4ccdd326) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pwrfail](structmcp7940n__rtc__weekday.md#a5ce2be23d666085e0d3af23e4ccdd326) : 1;

[ 36](structmcp7940n__rtc__weekday.md#a93d4320e89948c63805bf4f3aef4bc47) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [oscrun](structmcp7940n__rtc__weekday.md#a93d4320e89948c63805bf4f3aef4bc47) : 1;

[ 37](structmcp7940n__rtc__weekday.md#a0f6c1b9c71caf71b1db29fe2d1838ebe) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [nimp](structmcp7940n__rtc__weekday.md#a0f6c1b9c71caf71b1db29fe2d1838ebe) : 2;

38} \_\_packed;

39

[ 40](structmcp7940n__rtc__date.md)struct [mcp7940n\_rtc\_date](structmcp7940n__rtc__date.md) {

[ 41](structmcp7940n__rtc__date.md#a9cbb6bdad4518b4be7cc4b4a54566558) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [date\_one](structmcp7940n__rtc__date.md#a9cbb6bdad4518b4be7cc4b4a54566558) : 4;

[ 42](structmcp7940n__rtc__date.md#ae9907ab46390955454466c75367e026b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [date\_ten](structmcp7940n__rtc__date.md#ae9907ab46390955454466c75367e026b) : 2;

[ 43](structmcp7940n__rtc__date.md#a57cb56d3480895702813791d5a1cd572) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [nimp](structmcp7940n__rtc__date.md#a57cb56d3480895702813791d5a1cd572) : 2;

44} \_\_packed;

45

[ 46](structmcp7940n__rtc__month.md)struct [mcp7940n\_rtc\_month](structmcp7940n__rtc__month.md) {

[ 47](structmcp7940n__rtc__month.md#a69e6a907088bc39d558abf0d98446f8f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [month\_one](structmcp7940n__rtc__month.md#a69e6a907088bc39d558abf0d98446f8f) : 4;

[ 48](structmcp7940n__rtc__month.md#a7f4a43b85f74fa561b04202562c37a0f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [month\_ten](structmcp7940n__rtc__month.md#a7f4a43b85f74fa561b04202562c37a0f) : 1;

[ 49](structmcp7940n__rtc__month.md#a116c474a129357f8227e7a573e9f00cb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [lpyr](structmcp7940n__rtc__month.md#a116c474a129357f8227e7a573e9f00cb) : 1;

[ 50](structmcp7940n__rtc__month.md#a208c72632da64fc68e23d5506fd85a91) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [nimp](structmcp7940n__rtc__month.md#a208c72632da64fc68e23d5506fd85a91) : 2;

51} \_\_packed;

52

[ 53](structmcp7940n__rtc__year.md)struct [mcp7940n\_rtc\_year](structmcp7940n__rtc__year.md) {

[ 54](structmcp7940n__rtc__year.md#aa092364e515280cb627318dcc46fd247) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [year\_one](structmcp7940n__rtc__year.md#aa092364e515280cb627318dcc46fd247) : 4;

[ 55](structmcp7940n__rtc__year.md#a9770cbfb607d917f444369c2c0a433eb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [year\_ten](structmcp7940n__rtc__year.md#a9770cbfb607d917f444369c2c0a433eb) : 4;

56} \_\_packed;

57

[ 58](structmcp7940n__rtc__control.md)struct [mcp7940n\_rtc\_control](structmcp7940n__rtc__control.md) {

[ 59](structmcp7940n__rtc__control.md#a4b14ddf9ff38434096104ec59ef47f33) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sqwfs](structmcp7940n__rtc__control.md#a4b14ddf9ff38434096104ec59ef47f33) : 2;

[ 60](structmcp7940n__rtc__control.md#ac1cc15310736cf89c3452cab847d7d9a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [crs\_trim](structmcp7940n__rtc__control.md#ac1cc15310736cf89c3452cab847d7d9a) : 1;

[ 61](structmcp7940n__rtc__control.md#a0319904e52ccb2ef1f90dcb2f1a63f25) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ext\_osc](structmcp7940n__rtc__control.md#a0319904e52ccb2ef1f90dcb2f1a63f25) : 1;

[ 62](structmcp7940n__rtc__control.md#a7b5bac46017674dceeef43e1b23b49b0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [alm0\_en](structmcp7940n__rtc__control.md#a7b5bac46017674dceeef43e1b23b49b0) : 1;

[ 63](structmcp7940n__rtc__control.md#acd7bba87747ab836427d8a81ff34791a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [alm1\_en](structmcp7940n__rtc__control.md#acd7bba87747ab836427d8a81ff34791a) : 1;

[ 64](structmcp7940n__rtc__control.md#ae38c44315866707295c920756acb0e48) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sqw\_en](structmcp7940n__rtc__control.md#ae38c44315866707295c920756acb0e48) : 1;

[ 65](structmcp7940n__rtc__control.md#a8ed513f2c51f7cc90327c853a8783d6d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [out](structmcp7940n__rtc__control.md#a8ed513f2c51f7cc90327c853a8783d6d) : 1;

66} \_\_packed;

67

[ 68](structmcp7940n__rtc__osctrim.md)struct [mcp7940n\_rtc\_osctrim](structmcp7940n__rtc__osctrim.md) {

[ 69](structmcp7940n__rtc__osctrim.md#a99f1e86f33aac0766a596fed2d9202fd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [trim\_val](structmcp7940n__rtc__osctrim.md#a99f1e86f33aac0766a596fed2d9202fd) : 7;

[ 70](structmcp7940n__rtc__osctrim.md#aee14f5eb945eb5622a6fa927caa98281) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sign](structmcp7940n__rtc__osctrim.md#aee14f5eb945eb5622a6fa927caa98281) : 1;

71} \_\_packed;

72

[ 73](structmcp7940n__alm__sec.md)struct [mcp7940n\_alm\_sec](structmcp7940n__alm__sec.md) {

[ 74](structmcp7940n__alm__sec.md#a53efab44066a056f700900367deb48f6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sec\_one](structmcp7940n__alm__sec.md#a53efab44066a056f700900367deb48f6) : 4;

[ 75](structmcp7940n__alm__sec.md#a2e67b7fb412cab0a791620bc7135fe6b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sec\_ten](structmcp7940n__alm__sec.md#a2e67b7fb412cab0a791620bc7135fe6b) : 3;

[ 76](structmcp7940n__alm__sec.md#a569c96382bc2c4c79017653fddae9b0a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [nimp](structmcp7940n__alm__sec.md#a569c96382bc2c4c79017653fddae9b0a) : 1;

77} \_\_packed;

78

[ 79](structmcp7940n__alm__min.md)struct [mcp7940n\_alm\_min](structmcp7940n__alm__min.md) {

[ 80](structmcp7940n__alm__min.md#a38c9e3781b886d69b4db406e5ceebffd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [min\_one](structmcp7940n__alm__min.md#a38c9e3781b886d69b4db406e5ceebffd) : 4;

[ 81](structmcp7940n__alm__min.md#a92075bebd635ee16ffc94e64ba95988e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [min\_ten](structmcp7940n__alm__min.md#a92075bebd635ee16ffc94e64ba95988e) : 3;

[ 82](structmcp7940n__alm__min.md#a04f1fd0b76307c6fdc4dd8355345ff81) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [nimp](structmcp7940n__alm__min.md#a04f1fd0b76307c6fdc4dd8355345ff81) : 1;

83} \_\_packed;

84

[ 85](structmcp7940n__alm__hours.md)struct [mcp7940n\_alm\_hours](structmcp7940n__alm__hours.md) {

[ 86](structmcp7940n__alm__hours.md#a6fe6936a15425ca4c9a707207db9584d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [hr\_one](structmcp7940n__alm__hours.md#a6fe6936a15425ca4c9a707207db9584d) : 4;

[ 87](structmcp7940n__alm__hours.md#a820c5a98c34f967ea800592b08226d13) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [hr\_ten](structmcp7940n__alm__hours.md#a820c5a98c34f967ea800592b08226d13) : 2;

[ 88](structmcp7940n__alm__hours.md#ab234b9d34e397d05a7ac8e260170ebcc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [twelve\_hr](structmcp7940n__alm__hours.md#ab234b9d34e397d05a7ac8e260170ebcc) : 1;

[ 89](structmcp7940n__alm__hours.md#a43d2b4c53de34cf63cf8392f1fc63b4f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [nimp](structmcp7940n__alm__hours.md#a43d2b4c53de34cf63cf8392f1fc63b4f) : 1;

90} \_\_packed;

91

[ 92](structmcp7940n__alm__weekday.md)struct [mcp7940n\_alm\_weekday](structmcp7940n__alm__weekday.md) {

[ 93](structmcp7940n__alm__weekday.md#ae0179530d0837ad642d1640545779db2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [weekday](structmcp7940n__alm__weekday.md#ae0179530d0837ad642d1640545779db2) : 3;

[ 94](structmcp7940n__alm__weekday.md#af0c373dc09f47fe36a7ec203bfa8ab5c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [alm\_if](structmcp7940n__alm__weekday.md#af0c373dc09f47fe36a7ec203bfa8ab5c) : 1;

[ 95](structmcp7940n__alm__weekday.md#ab32d6feecbc378727fb463e81d70420c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [alm\_msk](structmcp7940n__alm__weekday.md#ab32d6feecbc378727fb463e81d70420c) : 3;

[ 96](structmcp7940n__alm__weekday.md#a66362fcb6c0ec7c8dac4f4a224ec9ab2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [alm\_pol](structmcp7940n__alm__weekday.md#a66362fcb6c0ec7c8dac4f4a224ec9ab2) : 1;

97} \_\_packed;

98

[ 99](structmcp7940n__alm__date.md)struct [mcp7940n\_alm\_date](structmcp7940n__alm__date.md) {

[ 100](structmcp7940n__alm__date.md#a78ad71fa8455f392b4dd8cecdf1eb0b3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [date\_one](structmcp7940n__alm__date.md#a78ad71fa8455f392b4dd8cecdf1eb0b3) : 4;

[ 101](structmcp7940n__alm__date.md#a15e4d057a6d76e4af375420394c0784e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [date\_ten](structmcp7940n__alm__date.md#a15e4d057a6d76e4af375420394c0784e) : 2;

[ 102](structmcp7940n__alm__date.md#aabfce8e23b449ecb3e629e79a472a44b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [nimp](structmcp7940n__alm__date.md#aabfce8e23b449ecb3e629e79a472a44b) : 2;

103} \_\_packed;

104

[ 105](structmcp7940n__alm__month.md)struct [mcp7940n\_alm\_month](structmcp7940n__alm__month.md) {

[ 106](structmcp7940n__alm__month.md#a1f66c0ad21747b0340649995eea42ec8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [month\_one](structmcp7940n__alm__month.md#a1f66c0ad21747b0340649995eea42ec8) : 4;

[ 107](structmcp7940n__alm__month.md#a8c59887fcc251d447be5a1373c69189b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [month\_ten](structmcp7940n__alm__month.md#a8c59887fcc251d447be5a1373c69189b) : 1;

[ 108](structmcp7940n__alm__month.md#a4d4e10f9ede94433156d2e7c9ba3a5bf) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [nimp](structmcp7940n__alm__month.md#a4d4e10f9ede94433156d2e7c9ba3a5bf) : 3;

109} \_\_packed;

110

[ 111](structmcp7940n__time__registers.md)struct [mcp7940n\_time\_registers](structmcp7940n__time__registers.md) {

[ 112](structmcp7940n__time__registers.md#ae96b450630ae6c66e302f96f972a2aec) struct [mcp7940n\_rtc\_sec](structmcp7940n__rtc__sec.md) [rtc\_sec](structmcp7940n__time__registers.md#ae96b450630ae6c66e302f96f972a2aec);

[ 113](structmcp7940n__time__registers.md#ad0c9ab52de1cdd739af5439f124af0a5) struct [mcp7940n\_rtc\_min](structmcp7940n__rtc__min.md) [rtc\_min](structmcp7940n__time__registers.md#ad0c9ab52de1cdd739af5439f124af0a5);

[ 114](structmcp7940n__time__registers.md#a815aefe0ea74e1b9f04e34fe3ac25b19) struct [mcp7940n\_rtc\_hours](structmcp7940n__rtc__hours.md) [rtc\_hours](structmcp7940n__time__registers.md#a815aefe0ea74e1b9f04e34fe3ac25b19);

[ 115](structmcp7940n__time__registers.md#a4b1193f1596d173f68f5d758bf900e88) struct [mcp7940n\_rtc\_weekday](structmcp7940n__rtc__weekday.md) [rtc\_weekday](structmcp7940n__time__registers.md#a4b1193f1596d173f68f5d758bf900e88);

[ 116](structmcp7940n__time__registers.md#a5f55fd69218970b68ad3bb0fbab9ca68) struct [mcp7940n\_rtc\_date](structmcp7940n__rtc__date.md) [rtc\_date](structmcp7940n__time__registers.md#a5f55fd69218970b68ad3bb0fbab9ca68);

[ 117](structmcp7940n__time__registers.md#a0d88f52f9618209c43e83938e1a39760) struct [mcp7940n\_rtc\_month](structmcp7940n__rtc__month.md) [rtc\_month](structmcp7940n__time__registers.md#a0d88f52f9618209c43e83938e1a39760);

[ 118](structmcp7940n__time__registers.md#a42df0d52374ca2cb1df82e25c3b06790) struct [mcp7940n\_rtc\_year](structmcp7940n__rtc__year.md) [rtc\_year](structmcp7940n__time__registers.md#a42df0d52374ca2cb1df82e25c3b06790);

[ 119](structmcp7940n__time__registers.md#ae024d2ded62acb73d263b980c6fc4d6e) struct [mcp7940n\_rtc\_control](structmcp7940n__rtc__control.md) [rtc\_control](structmcp7940n__time__registers.md#ae024d2ded62acb73d263b980c6fc4d6e);

[ 120](structmcp7940n__time__registers.md#a0fbb1991a66e18823a91c984cfa7767a) struct [mcp7940n\_rtc\_osctrim](structmcp7940n__rtc__osctrim.md) [rtc\_osctrim](structmcp7940n__time__registers.md#a0fbb1991a66e18823a91c984cfa7767a);

121} \_\_packed;

122

[ 123](structmcp7940n__alarm__registers.md)struct [mcp7940n\_alarm\_registers](structmcp7940n__alarm__registers.md) {

[ 124](structmcp7940n__alarm__registers.md#a2d46f94bcd97e2ff3e1e85a3fb43539e) struct [mcp7940n\_alm\_sec](structmcp7940n__alm__sec.md) [alm\_sec](structmcp7940n__alarm__registers.md#a2d46f94bcd97e2ff3e1e85a3fb43539e);

[ 125](structmcp7940n__alarm__registers.md#aa7b921fad0f40df38c8ac8cab2c620b6) struct [mcp7940n\_alm\_min](structmcp7940n__alm__min.md) [alm\_min](structmcp7940n__alarm__registers.md#aa7b921fad0f40df38c8ac8cab2c620b6);

[ 126](structmcp7940n__alarm__registers.md#a25ebc6d4e4c8f17f38d100f6e3e87404) struct [mcp7940n\_alm\_hours](structmcp7940n__alm__hours.md) [alm\_hours](structmcp7940n__alarm__registers.md#a25ebc6d4e4c8f17f38d100f6e3e87404);

[ 127](structmcp7940n__alarm__registers.md#a91cf619c5d0a481c944b76183c3c74a5) struct [mcp7940n\_alm\_weekday](structmcp7940n__alm__weekday.md) [alm\_weekday](structmcp7940n__alarm__registers.md#a91cf619c5d0a481c944b76183c3c74a5);

[ 128](structmcp7940n__alarm__registers.md#aadf6522ed74b6a29de42b871d81c02dd) struct [mcp7940n\_alm\_date](structmcp7940n__alm__date.md) [alm\_date](structmcp7940n__alarm__registers.md#aadf6522ed74b6a29de42b871d81c02dd);

[ 129](structmcp7940n__alarm__registers.md#a0b5cd03aadccd31b5f432aa3a728e62d) struct [mcp7940n\_alm\_month](structmcp7940n__alm__month.md) [alm\_month](structmcp7940n__alarm__registers.md#a0b5cd03aadccd31b5f432aa3a728e62d);

130} \_\_packed;

131

[ 132](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037ca)enum [mcp7940n\_register](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037ca) {

[ 133](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa9a800906ad19632da63aafdf0af64305) [REG\_RTC\_SEC](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa9a800906ad19632da63aafdf0af64305) = 0x0,

[ 134](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa5b0a41180b9865a6f7000cc999d99bc2) [REG\_RTC\_MIN](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa5b0a41180b9865a6f7000cc999d99bc2) = 0x1,

[ 135](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa9b294fcabf3e24b374c5ef73319cbd9f) [REG\_RTC\_HOUR](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa9b294fcabf3e24b374c5ef73319cbd9f) = 0x2,

[ 136](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caaba2a5b1f906ae6eb0fd7b8e886c89dae) [REG\_RTC\_WDAY](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caaba2a5b1f906ae6eb0fd7b8e886c89dae) = 0x3,

[ 137](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa2dd675d187d16817c1c137087141931a) [REG\_RTC\_DATE](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa2dd675d187d16817c1c137087141931a) = 0x4,

[ 138](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa207229ad1a6d8eb308f7e07e5ba24078) [REG\_RTC\_MONTH](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa207229ad1a6d8eb308f7e07e5ba24078) = 0x5,

[ 139](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa4d3873828e277cd12e7f07cfdbd1ea09) [REG\_RTC\_YEAR](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa4d3873828e277cd12e7f07cfdbd1ea09) = 0x6,

[ 140](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa9e100b8ccff22f359f9c5e7ce75da69b) [REG\_RTC\_CONTROL](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa9e100b8ccff22f359f9c5e7ce75da69b) = 0x7,

[ 141](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa5aac6210cc3409f00739f7afcf99f163) [REG\_RTC\_OSCTRIM](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa5aac6210cc3409f00739f7afcf99f163) = 0x8,

142 /\* 0x9 not implemented \*/

[ 143](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caaaef514cad1cf33114d05f2f562923aff) [REG\_ALM0\_SEC](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caaaef514cad1cf33114d05f2f562923aff) = 0xA,

[ 144](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa79b99c060b928e4cfb172d1e2f7dd23b) [REG\_ALM0\_MIN](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa79b99c060b928e4cfb172d1e2f7dd23b) = 0xB,

[ 145](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caacb9a858775500b6dafe4ba1612cc262e) [REG\_ALM0\_HOUR](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caacb9a858775500b6dafe4ba1612cc262e) = 0xC,

[ 146](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa2ea0bce5ed8eafb4220ea9ed4a414894) [REG\_ALM0\_WDAY](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa2ea0bce5ed8eafb4220ea9ed4a414894) = 0xD,

[ 147](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caae8fcb4847553ddb7e446d31e6a877dab) [REG\_ALM0\_DATE](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caae8fcb4847553ddb7e446d31e6a877dab) = 0xE,

[ 148](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caaaff2236a08b98016c4efff385ec8c567) [REG\_ALM0\_MONTH](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caaaff2236a08b98016c4efff385ec8c567) = 0xF,

149 /\* 0x10 not implemented \*/

[ 150](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa2e9bbfb2d2df268ab59dfb9f0eeec0f5) [REG\_ALM1\_SEC](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa2e9bbfb2d2df268ab59dfb9f0eeec0f5) = 0x11,

[ 151](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caab9e65b5fc4175acdfa6ff8762c71cf4a) [REG\_ALM1\_MIN](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caab9e65b5fc4175acdfa6ff8762c71cf4a) = 0x12,

[ 152](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa6b53616e27962f1abf22157fe15d6d2c) [REG\_ALM1\_HOUR](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa6b53616e27962f1abf22157fe15d6d2c) = 0x13,

[ 153](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caab656649d997513e04eed5ce254bd4da1) [REG\_ALM1\_WDAY](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caab656649d997513e04eed5ce254bd4da1) = 0x14,

[ 154](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caade386d1238918f92cf07b7f62e6daa52) [REG\_ALM1\_DATE](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caade386d1238918f92cf07b7f62e6daa52) = 0x15,

[ 155](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa1434f2ba901755b53e2429d0c479777e) [REG\_ALM1\_MONTH](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa1434f2ba901755b53e2429d0c479777e) = 0x16,

156 /\* 0x17 not implemented \*/

[ 157](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa672f863a6949b04d1934de5d78075bc7) [REG\_PWR\_DWN\_MIN](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa672f863a6949b04d1934de5d78075bc7) = 0x18,

[ 158](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa20073e04c75b4172d393e7fbb5e7b71c) [REG\_PWR\_DWN\_HOUR](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa20073e04c75b4172d393e7fbb5e7b71c) = 0x19,

[ 159](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa1c21f52339c4006174b302dbcc79b8bc) [REG\_PWR\_DWN\_DATE](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa1c21f52339c4006174b302dbcc79b8bc) = 0x1A,

[ 160](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa36d2316580c285b19af2d593481b594b) [REG\_PWR\_DWN\_MONTH](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa36d2316580c285b19af2d593481b594b) = 0x1B,

[ 161](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caac2a1ddbe5a3db3655fb6a0bd4671c996) [REG\_PWR\_UP\_MIN](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caac2a1ddbe5a3db3655fb6a0bd4671c996) = 0x1C,

[ 162](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa6d6803d2407ca7dbbc9cafd33e61c767) [REG\_PWR\_UP\_HOUR](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa6d6803d2407ca7dbbc9cafd33e61c767) = 0x1D,

[ 163](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caad393438b0790e2547d8abd839714fffe) [REG\_PWR\_UP\_DATE](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caad393438b0790e2547d8abd839714fffe) = 0x1E,

[ 164](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa0927849a6855cee0183d7fa30f2d2403) [REG\_PWR\_UP\_MONTH](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa0927849a6855cee0183d7fa30f2d2403) = 0x1F,

[ 165](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa6cf45e9c55ef77958f5f8ee86fa0fe94) [SRAM\_MIN](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa6cf45e9c55ef77958f5f8ee86fa0fe94) = 0x20,

[ 166](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa2c55bf2bc9ff1401129467be5fa8ae9b) [SRAM\_MAX](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa2c55bf2bc9ff1401129467be5fa8ae9b) = 0x5F,

[ 167](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caaf41178dbb5f80ac8d5e5af6c634dce2e) [REG\_INVAL](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caaf41178dbb5f80ac8d5e5af6c634dce2e) = 0x60,

168};

169

170/\* Mutually exclusive alarm trigger settings \*/

[ 171](mcp7940n_8h.md#ab0abecad5284f476a3cc754f6f460c56)enum [mcp7940n\_alarm\_trigger](mcp7940n_8h.md#ab0abecad5284f476a3cc754f6f460c56) {

[ 172](mcp7940n_8h.md#ab0abecad5284f476a3cc754f6f460c56a432b8881c205779a5d719da529712db8) [MCP7940N\_ALARM\_TRIGGER\_SECONDS](mcp7940n_8h.md#ab0abecad5284f476a3cc754f6f460c56a432b8881c205779a5d719da529712db8) = 0x0,

[ 173](mcp7940n_8h.md#ab0abecad5284f476a3cc754f6f460c56a0703a8e8c9c7126bae4deac00729b27c) [MCP7940N\_ALARM\_TRIGGER\_MINUTES](mcp7940n_8h.md#ab0abecad5284f476a3cc754f6f460c56a0703a8e8c9c7126bae4deac00729b27c) = 0x1,

[ 174](mcp7940n_8h.md#ab0abecad5284f476a3cc754f6f460c56a29a1714cd8617b1f47e9db6bef69460a) [MCP7940N\_ALARM\_TRIGGER\_HOURS](mcp7940n_8h.md#ab0abecad5284f476a3cc754f6f460c56a29a1714cd8617b1f47e9db6bef69460a) = 0x2,

[ 175](mcp7940n_8h.md#ab0abecad5284f476a3cc754f6f460c56ac1e977636f2081b261035d1e7c5b04e7) [MCP7940N\_ALARM\_TRIGGER\_WDAY](mcp7940n_8h.md#ab0abecad5284f476a3cc754f6f460c56ac1e977636f2081b261035d1e7c5b04e7) = 0x3,

[ 176](mcp7940n_8h.md#ab0abecad5284f476a3cc754f6f460c56a192356760370bf7649f91efc2bd6eb2d) [MCP7940N\_ALARM\_TRIGGER\_DATE](mcp7940n_8h.md#ab0abecad5284f476a3cc754f6f460c56a192356760370bf7649f91efc2bd6eb2d) = 0x4,

177 /\* TRIGGER\_ALL matches seconds, minutes, hours, weekday, date and month \*/

[ 178](mcp7940n_8h.md#ab0abecad5284f476a3cc754f6f460c56ae900f75907656299d7a0db6e294441b8) [MCP7940N\_ALARM\_TRIGGER\_ALL](mcp7940n_8h.md#ab0abecad5284f476a3cc754f6f460c56ae900f75907656299d7a0db6e294441b8) = 0x7,

179};

180

[ 195](mcp7940n_8h.md#a489e58e2b26bc3986d87abeb0f2831de)int [mcp7940n\_rtc\_set\_time](mcp7940n_8h.md#a489e58e2b26bc3986d87abeb0f2831de)(const struct [device](structdevice.md) \*dev, [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) unix\_time);

196

197#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_RTC\_MCP7940N\_H\_ \*/

[time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7)

\_TIME\_T\_ time\_t

**Definition** \_timespec.h:14

[mcp7940n\_rtc\_set\_time](mcp7940n_8h.md#a489e58e2b26bc3986d87abeb0f2831de)

int mcp7940n\_rtc\_set\_time(const struct device \*dev, time\_t unix\_time)

Set the RTC to a given Unix time.

[mcp7940n\_register](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037ca)

mcp7940n\_register

**Definition** mcp7940n.h:132

[REG\_PWR\_UP\_MONTH](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa0927849a6855cee0183d7fa30f2d2403)

@ REG\_PWR\_UP\_MONTH

**Definition** mcp7940n.h:164

[REG\_ALM1\_MONTH](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa1434f2ba901755b53e2429d0c479777e)

@ REG\_ALM1\_MONTH

**Definition** mcp7940n.h:155

[REG\_PWR\_DWN\_DATE](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa1c21f52339c4006174b302dbcc79b8bc)

@ REG\_PWR\_DWN\_DATE

**Definition** mcp7940n.h:159

[REG\_PWR\_DWN\_HOUR](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa20073e04c75b4172d393e7fbb5e7b71c)

@ REG\_PWR\_DWN\_HOUR

**Definition** mcp7940n.h:158

[REG\_RTC\_MONTH](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa207229ad1a6d8eb308f7e07e5ba24078)

@ REG\_RTC\_MONTH

**Definition** mcp7940n.h:138

[SRAM\_MAX](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa2c55bf2bc9ff1401129467be5fa8ae9b)

@ SRAM\_MAX

**Definition** mcp7940n.h:166

[REG\_RTC\_DATE](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa2dd675d187d16817c1c137087141931a)

@ REG\_RTC\_DATE

**Definition** mcp7940n.h:137

[REG\_ALM1\_SEC](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa2e9bbfb2d2df268ab59dfb9f0eeec0f5)

@ REG\_ALM1\_SEC

**Definition** mcp7940n.h:150

[REG\_ALM0\_WDAY](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa2ea0bce5ed8eafb4220ea9ed4a414894)

@ REG\_ALM0\_WDAY

**Definition** mcp7940n.h:146

[REG\_PWR\_DWN\_MONTH](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa36d2316580c285b19af2d593481b594b)

@ REG\_PWR\_DWN\_MONTH

**Definition** mcp7940n.h:160

[REG\_RTC\_YEAR](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa4d3873828e277cd12e7f07cfdbd1ea09)

@ REG\_RTC\_YEAR

**Definition** mcp7940n.h:139

[REG\_RTC\_OSCTRIM](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa5aac6210cc3409f00739f7afcf99f163)

@ REG\_RTC\_OSCTRIM

**Definition** mcp7940n.h:141

[REG\_RTC\_MIN](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa5b0a41180b9865a6f7000cc999d99bc2)

@ REG\_RTC\_MIN

**Definition** mcp7940n.h:134

[REG\_PWR\_DWN\_MIN](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa672f863a6949b04d1934de5d78075bc7)

@ REG\_PWR\_DWN\_MIN

**Definition** mcp7940n.h:157

[REG\_ALM1\_HOUR](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa6b53616e27962f1abf22157fe15d6d2c)

@ REG\_ALM1\_HOUR

**Definition** mcp7940n.h:152

[SRAM\_MIN](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa6cf45e9c55ef77958f5f8ee86fa0fe94)

@ SRAM\_MIN

**Definition** mcp7940n.h:165

[REG\_PWR\_UP\_HOUR](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa6d6803d2407ca7dbbc9cafd33e61c767)

@ REG\_PWR\_UP\_HOUR

**Definition** mcp7940n.h:162

[REG\_ALM0\_MIN](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa79b99c060b928e4cfb172d1e2f7dd23b)

@ REG\_ALM0\_MIN

**Definition** mcp7940n.h:144

[REG\_RTC\_SEC](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa9a800906ad19632da63aafdf0af64305)

@ REG\_RTC\_SEC

**Definition** mcp7940n.h:133

[REG\_RTC\_HOUR](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa9b294fcabf3e24b374c5ef73319cbd9f)

@ REG\_RTC\_HOUR

**Definition** mcp7940n.h:135

[REG\_RTC\_CONTROL](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caa9e100b8ccff22f359f9c5e7ce75da69b)

@ REG\_RTC\_CONTROL

**Definition** mcp7940n.h:140

[REG\_ALM0\_SEC](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caaaef514cad1cf33114d05f2f562923aff)

@ REG\_ALM0\_SEC

**Definition** mcp7940n.h:143

[REG\_ALM0\_MONTH](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caaaff2236a08b98016c4efff385ec8c567)

@ REG\_ALM0\_MONTH

**Definition** mcp7940n.h:148

[REG\_ALM1\_WDAY](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caab656649d997513e04eed5ce254bd4da1)

@ REG\_ALM1\_WDAY

**Definition** mcp7940n.h:153

[REG\_ALM1\_MIN](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caab9e65b5fc4175acdfa6ff8762c71cf4a)

@ REG\_ALM1\_MIN

**Definition** mcp7940n.h:151

[REG\_RTC\_WDAY](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caaba2a5b1f906ae6eb0fd7b8e886c89dae)

@ REG\_RTC\_WDAY

**Definition** mcp7940n.h:136

[REG\_PWR\_UP\_MIN](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caac2a1ddbe5a3db3655fb6a0bd4671c996)

@ REG\_PWR\_UP\_MIN

**Definition** mcp7940n.h:161

[REG\_ALM0\_HOUR](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caacb9a858775500b6dafe4ba1612cc262e)

@ REG\_ALM0\_HOUR

**Definition** mcp7940n.h:145

[REG\_PWR\_UP\_DATE](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caad393438b0790e2547d8abd839714fffe)

@ REG\_PWR\_UP\_DATE

**Definition** mcp7940n.h:163

[REG\_ALM1\_DATE](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caade386d1238918f92cf07b7f62e6daa52)

@ REG\_ALM1\_DATE

**Definition** mcp7940n.h:154

[REG\_ALM0\_DATE](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caae8fcb4847553ddb7e446d31e6a877dab)

@ REG\_ALM0\_DATE

**Definition** mcp7940n.h:147

[REG\_INVAL](mcp7940n_8h.md#a91e4854e96032d65f4f1825d47b037caaf41178dbb5f80ac8d5e5af6c634dce2e)

@ REG\_INVAL

**Definition** mcp7940n.h:167

[mcp7940n\_alarm\_trigger](mcp7940n_8h.md#ab0abecad5284f476a3cc754f6f460c56)

mcp7940n\_alarm\_trigger

**Definition** mcp7940n.h:171

[MCP7940N\_ALARM\_TRIGGER\_MINUTES](mcp7940n_8h.md#ab0abecad5284f476a3cc754f6f460c56a0703a8e8c9c7126bae4deac00729b27c)

@ MCP7940N\_ALARM\_TRIGGER\_MINUTES

**Definition** mcp7940n.h:173

[MCP7940N\_ALARM\_TRIGGER\_DATE](mcp7940n_8h.md#ab0abecad5284f476a3cc754f6f460c56a192356760370bf7649f91efc2bd6eb2d)

@ MCP7940N\_ALARM\_TRIGGER\_DATE

**Definition** mcp7940n.h:176

[MCP7940N\_ALARM\_TRIGGER\_HOURS](mcp7940n_8h.md#ab0abecad5284f476a3cc754f6f460c56a29a1714cd8617b1f47e9db6bef69460a)

@ MCP7940N\_ALARM\_TRIGGER\_HOURS

**Definition** mcp7940n.h:174

[MCP7940N\_ALARM\_TRIGGER\_SECONDS](mcp7940n_8h.md#ab0abecad5284f476a3cc754f6f460c56a432b8881c205779a5d719da529712db8)

@ MCP7940N\_ALARM\_TRIGGER\_SECONDS

**Definition** mcp7940n.h:172

[MCP7940N\_ALARM\_TRIGGER\_WDAY](mcp7940n_8h.md#ab0abecad5284f476a3cc754f6f460c56ac1e977636f2081b261035d1e7c5b04e7)

@ MCP7940N\_ALARM\_TRIGGER\_WDAY

**Definition** mcp7940n.h:175

[MCP7940N\_ALARM\_TRIGGER\_ALL](mcp7940n_8h.md#ab0abecad5284f476a3cc754f6f460c56ae900f75907656299d7a0db6e294441b8)

@ MCP7940N\_ALARM\_TRIGGER\_ALL

**Definition** mcp7940n.h:178

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[mcp7940n\_alarm\_registers](structmcp7940n__alarm__registers.md)

**Definition** mcp7940n.h:123

[mcp7940n\_alarm\_registers::alm\_month](structmcp7940n__alarm__registers.md#a0b5cd03aadccd31b5f432aa3a728e62d)

struct mcp7940n\_alm\_month alm\_month

**Definition** mcp7940n.h:129

[mcp7940n\_alarm\_registers::alm\_hours](structmcp7940n__alarm__registers.md#a25ebc6d4e4c8f17f38d100f6e3e87404)

struct mcp7940n\_alm\_hours alm\_hours

**Definition** mcp7940n.h:126

[mcp7940n\_alarm\_registers::alm\_sec](structmcp7940n__alarm__registers.md#a2d46f94bcd97e2ff3e1e85a3fb43539e)

struct mcp7940n\_alm\_sec alm\_sec

**Definition** mcp7940n.h:124

[mcp7940n\_alarm\_registers::alm\_weekday](structmcp7940n__alarm__registers.md#a91cf619c5d0a481c944b76183c3c74a5)

struct mcp7940n\_alm\_weekday alm\_weekday

**Definition** mcp7940n.h:127

[mcp7940n\_alarm\_registers::alm\_min](structmcp7940n__alarm__registers.md#aa7b921fad0f40df38c8ac8cab2c620b6)

struct mcp7940n\_alm\_min alm\_min

**Definition** mcp7940n.h:125

[mcp7940n\_alarm\_registers::alm\_date](structmcp7940n__alarm__registers.md#aadf6522ed74b6a29de42b871d81c02dd)

struct mcp7940n\_alm\_date alm\_date

**Definition** mcp7940n.h:128

[mcp7940n\_alm\_date](structmcp7940n__alm__date.md)

**Definition** mcp7940n.h:99

[mcp7940n\_alm\_date::date\_ten](structmcp7940n__alm__date.md#a15e4d057a6d76e4af375420394c0784e)

uint8\_t date\_ten

**Definition** mcp7940n.h:101

[mcp7940n\_alm\_date::date\_one](structmcp7940n__alm__date.md#a78ad71fa8455f392b4dd8cecdf1eb0b3)

uint8\_t date\_one

**Definition** mcp7940n.h:100

[mcp7940n\_alm\_date::nimp](structmcp7940n__alm__date.md#aabfce8e23b449ecb3e629e79a472a44b)

uint8\_t nimp

**Definition** mcp7940n.h:102

[mcp7940n\_alm\_hours](structmcp7940n__alm__hours.md)

**Definition** mcp7940n.h:85

[mcp7940n\_alm\_hours::nimp](structmcp7940n__alm__hours.md#a43d2b4c53de34cf63cf8392f1fc63b4f)

uint8\_t nimp

**Definition** mcp7940n.h:89

[mcp7940n\_alm\_hours::hr\_one](structmcp7940n__alm__hours.md#a6fe6936a15425ca4c9a707207db9584d)

uint8\_t hr\_one

**Definition** mcp7940n.h:86

[mcp7940n\_alm\_hours::hr\_ten](structmcp7940n__alm__hours.md#a820c5a98c34f967ea800592b08226d13)

uint8\_t hr\_ten

**Definition** mcp7940n.h:87

[mcp7940n\_alm\_hours::twelve\_hr](structmcp7940n__alm__hours.md#ab234b9d34e397d05a7ac8e260170ebcc)

uint8\_t twelve\_hr

**Definition** mcp7940n.h:88

[mcp7940n\_alm\_min](structmcp7940n__alm__min.md)

**Definition** mcp7940n.h:79

[mcp7940n\_alm\_min::nimp](structmcp7940n__alm__min.md#a04f1fd0b76307c6fdc4dd8355345ff81)

uint8\_t nimp

**Definition** mcp7940n.h:82

[mcp7940n\_alm\_min::min\_one](structmcp7940n__alm__min.md#a38c9e3781b886d69b4db406e5ceebffd)

uint8\_t min\_one

**Definition** mcp7940n.h:80

[mcp7940n\_alm\_min::min\_ten](structmcp7940n__alm__min.md#a92075bebd635ee16ffc94e64ba95988e)

uint8\_t min\_ten

**Definition** mcp7940n.h:81

[mcp7940n\_alm\_month](structmcp7940n__alm__month.md)

**Definition** mcp7940n.h:105

[mcp7940n\_alm\_month::month\_one](structmcp7940n__alm__month.md#a1f66c0ad21747b0340649995eea42ec8)

uint8\_t month\_one

**Definition** mcp7940n.h:106

[mcp7940n\_alm\_month::nimp](structmcp7940n__alm__month.md#a4d4e10f9ede94433156d2e7c9ba3a5bf)

uint8\_t nimp

**Definition** mcp7940n.h:108

[mcp7940n\_alm\_month::month\_ten](structmcp7940n__alm__month.md#a8c59887fcc251d447be5a1373c69189b)

uint8\_t month\_ten

**Definition** mcp7940n.h:107

[mcp7940n\_alm\_sec](structmcp7940n__alm__sec.md)

**Definition** mcp7940n.h:73

[mcp7940n\_alm\_sec::sec\_ten](structmcp7940n__alm__sec.md#a2e67b7fb412cab0a791620bc7135fe6b)

uint8\_t sec\_ten

**Definition** mcp7940n.h:75

[mcp7940n\_alm\_sec::sec\_one](structmcp7940n__alm__sec.md#a53efab44066a056f700900367deb48f6)

uint8\_t sec\_one

**Definition** mcp7940n.h:74

[mcp7940n\_alm\_sec::nimp](structmcp7940n__alm__sec.md#a569c96382bc2c4c79017653fddae9b0a)

uint8\_t nimp

**Definition** mcp7940n.h:76

[mcp7940n\_alm\_weekday](structmcp7940n__alm__weekday.md)

**Definition** mcp7940n.h:92

[mcp7940n\_alm\_weekday::alm\_pol](structmcp7940n__alm__weekday.md#a66362fcb6c0ec7c8dac4f4a224ec9ab2)

uint8\_t alm\_pol

**Definition** mcp7940n.h:96

[mcp7940n\_alm\_weekday::alm\_msk](structmcp7940n__alm__weekday.md#ab32d6feecbc378727fb463e81d70420c)

uint8\_t alm\_msk

**Definition** mcp7940n.h:95

[mcp7940n\_alm\_weekday::weekday](structmcp7940n__alm__weekday.md#ae0179530d0837ad642d1640545779db2)

uint8\_t weekday

**Definition** mcp7940n.h:93

[mcp7940n\_alm\_weekday::alm\_if](structmcp7940n__alm__weekday.md#af0c373dc09f47fe36a7ec203bfa8ab5c)

uint8\_t alm\_if

**Definition** mcp7940n.h:94

[mcp7940n\_rtc\_control](structmcp7940n__rtc__control.md)

**Definition** mcp7940n.h:58

[mcp7940n\_rtc\_control::ext\_osc](structmcp7940n__rtc__control.md#a0319904e52ccb2ef1f90dcb2f1a63f25)

uint8\_t ext\_osc

**Definition** mcp7940n.h:61

[mcp7940n\_rtc\_control::sqwfs](structmcp7940n__rtc__control.md#a4b14ddf9ff38434096104ec59ef47f33)

uint8\_t sqwfs

**Definition** mcp7940n.h:59

[mcp7940n\_rtc\_control::alm0\_en](structmcp7940n__rtc__control.md#a7b5bac46017674dceeef43e1b23b49b0)

uint8\_t alm0\_en

**Definition** mcp7940n.h:62

[mcp7940n\_rtc\_control::out](structmcp7940n__rtc__control.md#a8ed513f2c51f7cc90327c853a8783d6d)

uint8\_t out

**Definition** mcp7940n.h:65

[mcp7940n\_rtc\_control::crs\_trim](structmcp7940n__rtc__control.md#ac1cc15310736cf89c3452cab847d7d9a)

uint8\_t crs\_trim

**Definition** mcp7940n.h:60

[mcp7940n\_rtc\_control::alm1\_en](structmcp7940n__rtc__control.md#acd7bba87747ab836427d8a81ff34791a)

uint8\_t alm1\_en

**Definition** mcp7940n.h:63

[mcp7940n\_rtc\_control::sqw\_en](structmcp7940n__rtc__control.md#ae38c44315866707295c920756acb0e48)

uint8\_t sqw\_en

**Definition** mcp7940n.h:64

[mcp7940n\_rtc\_date](structmcp7940n__rtc__date.md)

**Definition** mcp7940n.h:40

[mcp7940n\_rtc\_date::nimp](structmcp7940n__rtc__date.md#a57cb56d3480895702813791d5a1cd572)

uint8\_t nimp

**Definition** mcp7940n.h:43

[mcp7940n\_rtc\_date::date\_one](structmcp7940n__rtc__date.md#a9cbb6bdad4518b4be7cc4b4a54566558)

uint8\_t date\_one

**Definition** mcp7940n.h:41

[mcp7940n\_rtc\_date::date\_ten](structmcp7940n__rtc__date.md#ae9907ab46390955454466c75367e026b)

uint8\_t date\_ten

**Definition** mcp7940n.h:42

[mcp7940n\_rtc\_hours](structmcp7940n__rtc__hours.md)

**Definition** mcp7940n.h:25

[mcp7940n\_rtc\_hours::twelve\_hr](structmcp7940n__rtc__hours.md#a7c45eca341d518a9d922ffa68f8cdc6b)

uint8\_t twelve\_hr

**Definition** mcp7940n.h:28

[mcp7940n\_rtc\_hours::nimp](structmcp7940n__rtc__hours.md#a8e238443f2e19c2c2feeb5a9e5854356)

uint8\_t nimp

**Definition** mcp7940n.h:29

[mcp7940n\_rtc\_hours::hr\_one](structmcp7940n__rtc__hours.md#a9b2346401aaeb8bffd9f7ddfd0038bff)

uint8\_t hr\_one

**Definition** mcp7940n.h:26

[mcp7940n\_rtc\_hours::hr\_ten](structmcp7940n__rtc__hours.md#aa187c1bb717f8d2c09dc4f067c61a4f3)

uint8\_t hr\_ten

**Definition** mcp7940n.h:27

[mcp7940n\_rtc\_min](structmcp7940n__rtc__min.md)

**Definition** mcp7940n.h:19

[mcp7940n\_rtc\_min::min\_ten](structmcp7940n__rtc__min.md#a75e2870f8f221b2edf6786d786b098f0)

uint8\_t min\_ten

**Definition** mcp7940n.h:21

[mcp7940n\_rtc\_min::min\_one](structmcp7940n__rtc__min.md#aa9a0c45db431a07251e1101c0c7c1fb9)

uint8\_t min\_one

**Definition** mcp7940n.h:20

[mcp7940n\_rtc\_min::nimp](structmcp7940n__rtc__min.md#aabfa681bfc2f45e1f6447ddf6d996592)

uint8\_t nimp

**Definition** mcp7940n.h:22

[mcp7940n\_rtc\_month](structmcp7940n__rtc__month.md)

**Definition** mcp7940n.h:46

[mcp7940n\_rtc\_month::lpyr](structmcp7940n__rtc__month.md#a116c474a129357f8227e7a573e9f00cb)

uint8\_t lpyr

**Definition** mcp7940n.h:49

[mcp7940n\_rtc\_month::nimp](structmcp7940n__rtc__month.md#a208c72632da64fc68e23d5506fd85a91)

uint8\_t nimp

**Definition** mcp7940n.h:50

[mcp7940n\_rtc\_month::month\_one](structmcp7940n__rtc__month.md#a69e6a907088bc39d558abf0d98446f8f)

uint8\_t month\_one

**Definition** mcp7940n.h:47

[mcp7940n\_rtc\_month::month\_ten](structmcp7940n__rtc__month.md#a7f4a43b85f74fa561b04202562c37a0f)

uint8\_t month\_ten

**Definition** mcp7940n.h:48

[mcp7940n\_rtc\_osctrim](structmcp7940n__rtc__osctrim.md)

**Definition** mcp7940n.h:68

[mcp7940n\_rtc\_osctrim::trim\_val](structmcp7940n__rtc__osctrim.md#a99f1e86f33aac0766a596fed2d9202fd)

uint8\_t trim\_val

**Definition** mcp7940n.h:69

[mcp7940n\_rtc\_osctrim::sign](structmcp7940n__rtc__osctrim.md#aee14f5eb945eb5622a6fa927caa98281)

uint8\_t sign

**Definition** mcp7940n.h:70

[mcp7940n\_rtc\_sec](structmcp7940n__rtc__sec.md)

**Definition** mcp7940n.h:13

[mcp7940n\_rtc\_sec::sec\_ten](structmcp7940n__rtc__sec.md#a9c381492f172f8aaa64c4da6a8d647fb)

uint8\_t sec\_ten

**Definition** mcp7940n.h:15

[mcp7940n\_rtc\_sec::sec\_one](structmcp7940n__rtc__sec.md#ace288b683bce6aeb2b69c7db69c217b2)

uint8\_t sec\_one

**Definition** mcp7940n.h:14

[mcp7940n\_rtc\_sec::start\_osc](structmcp7940n__rtc__sec.md#acf5d8dacfdd0f59fda45aa1701a80d16)

uint8\_t start\_osc

**Definition** mcp7940n.h:16

[mcp7940n\_rtc\_weekday](structmcp7940n__rtc__weekday.md)

**Definition** mcp7940n.h:32

[mcp7940n\_rtc\_weekday::nimp](structmcp7940n__rtc__weekday.md#a0f6c1b9c71caf71b1db29fe2d1838ebe)

uint8\_t nimp

**Definition** mcp7940n.h:37

[mcp7940n\_rtc\_weekday::pwrfail](structmcp7940n__rtc__weekday.md#a5ce2be23d666085e0d3af23e4ccdd326)

uint8\_t pwrfail

**Definition** mcp7940n.h:35

[mcp7940n\_rtc\_weekday::oscrun](structmcp7940n__rtc__weekday.md#a93d4320e89948c63805bf4f3aef4bc47)

uint8\_t oscrun

**Definition** mcp7940n.h:36

[mcp7940n\_rtc\_weekday::weekday](structmcp7940n__rtc__weekday.md#a9aad56ee23af55ea2f41020d96095ddd)

uint8\_t weekday

**Definition** mcp7940n.h:33

[mcp7940n\_rtc\_weekday::vbaten](structmcp7940n__rtc__weekday.md#ad904822d76ac2f170807b3d6260061a3)

uint8\_t vbaten

**Definition** mcp7940n.h:34

[mcp7940n\_rtc\_year](structmcp7940n__rtc__year.md)

**Definition** mcp7940n.h:53

[mcp7940n\_rtc\_year::year\_ten](structmcp7940n__rtc__year.md#a9770cbfb607d917f444369c2c0a433eb)

uint8\_t year\_ten

**Definition** mcp7940n.h:55

[mcp7940n\_rtc\_year::year\_one](structmcp7940n__rtc__year.md#aa092364e515280cb627318dcc46fd247)

uint8\_t year\_one

**Definition** mcp7940n.h:54

[mcp7940n\_time\_registers](structmcp7940n__time__registers.md)

**Definition** mcp7940n.h:111

[mcp7940n\_time\_registers::rtc\_month](structmcp7940n__time__registers.md#a0d88f52f9618209c43e83938e1a39760)

struct mcp7940n\_rtc\_month rtc\_month

**Definition** mcp7940n.h:117

[mcp7940n\_time\_registers::rtc\_osctrim](structmcp7940n__time__registers.md#a0fbb1991a66e18823a91c984cfa7767a)

struct mcp7940n\_rtc\_osctrim rtc\_osctrim

**Definition** mcp7940n.h:120

[mcp7940n\_time\_registers::rtc\_year](structmcp7940n__time__registers.md#a42df0d52374ca2cb1df82e25c3b06790)

struct mcp7940n\_rtc\_year rtc\_year

**Definition** mcp7940n.h:118

[mcp7940n\_time\_registers::rtc\_weekday](structmcp7940n__time__registers.md#a4b1193f1596d173f68f5d758bf900e88)

struct mcp7940n\_rtc\_weekday rtc\_weekday

**Definition** mcp7940n.h:115

[mcp7940n\_time\_registers::rtc\_date](structmcp7940n__time__registers.md#a5f55fd69218970b68ad3bb0fbab9ca68)

struct mcp7940n\_rtc\_date rtc\_date

**Definition** mcp7940n.h:116

[mcp7940n\_time\_registers::rtc\_hours](structmcp7940n__time__registers.md#a815aefe0ea74e1b9f04e34fe3ac25b19)

struct mcp7940n\_rtc\_hours rtc\_hours

**Definition** mcp7940n.h:114

[mcp7940n\_time\_registers::rtc\_min](structmcp7940n__time__registers.md#ad0c9ab52de1cdd739af5439f124af0a5)

struct mcp7940n\_rtc\_min rtc\_min

**Definition** mcp7940n.h:113

[mcp7940n\_time\_registers::rtc\_control](structmcp7940n__time__registers.md#ae024d2ded62acb73d263b980c6fc4d6e)

struct mcp7940n\_rtc\_control rtc\_control

**Definition** mcp7940n.h:119

[mcp7940n\_time\_registers::rtc\_sec](structmcp7940n__time__registers.md#ae96b450630ae6c66e302f96f972a2aec)

struct mcp7940n\_rtc\_sec rtc\_sec

**Definition** mcp7940n.h:112

[timeutil.h](timeutil_8h.md)

Utilities supporting operation on time data structures.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [rtc](dir_fe6de79d2b035e3fa4834af86b312149.md)
- [mcp7940n.h](mcp7940n_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

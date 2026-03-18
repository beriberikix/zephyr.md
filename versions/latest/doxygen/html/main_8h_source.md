---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/main_8h_source.html
original_path: doxygen/html/main_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

main.h

[Go to the documentation of this file.](main_8h.md)

1

4

5/\*

6 \* Copyright (c) 2017 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_MAIN\_H\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_MAIN\_H\_

12

13#include <[stdbool.h](stdbool_8h.md)>

14#include <[stdint.h](stdint_8h.md)>

15

16#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

17#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

18

25

26#ifdef \_\_cplusplus

27extern "C" {

28#endif

29

31enum {

[ 32](group__bt__mesh__prov.md#ggabe5586cff0697e137730a52728978681affa8679d8be1a12714a34ed09c3b05dd) [BT\_MESH\_PROV\_AUTH\_CMAC\_AES128\_AES\_CCM](group__bt__mesh__prov.md#ggabe5586cff0697e137730a52728978681affa8679d8be1a12714a34ed09c3b05dd),

[ 33](group__bt__mesh__prov.md#ggabe5586cff0697e137730a52728978681a292bf2e4d29f0bd0d746bbb871f2ee5a) [BT\_MESH\_PROV\_AUTH\_HMAC\_SHA256\_AES\_CCM](group__bt__mesh__prov.md#ggabe5586cff0697e137730a52728978681a292bf2e4d29f0bd0d746bbb871f2ee5a),

34};

35

37enum {

[ 38](group__bt__mesh__prov.md#ggabec90bd95082b9dc8fa3ca27a9d7bc66a30e46fe23e508029b570e1f107b38d40) [BT\_MESH\_STATIC\_OOB\_AVAILABLE](group__bt__mesh__prov.md#ggabec90bd95082b9dc8fa3ca27a9d7bc66a30e46fe23e508029b570e1f107b38d40) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 39](group__bt__mesh__prov.md#ggabec90bd95082b9dc8fa3ca27a9d7bc66a61f859a15fabc8d9fd278dabe5a86a37) [BT\_MESH\_OOB\_AUTH\_REQUIRED](group__bt__mesh__prov.md#ggabec90bd95082b9dc8fa3ca27a9d7bc66a61f859a15fabc8d9fd278dabe5a86a37) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1)

40};

41

[ 43](group__bt__mesh__prov.md#ga5512b81ef7eeb45b0a12ef62234c8795)typedef enum {

[ 44](group__bt__mesh__prov.md#gga5512b81ef7eeb45b0a12ef62234c8795ad009060fd1f501c8362a63e6c020b113) [BT\_MESH\_NO\_OUTPUT](group__bt__mesh__prov.md#gga5512b81ef7eeb45b0a12ef62234c8795ad009060fd1f501c8362a63e6c020b113) = 0,

[ 45](group__bt__mesh__prov.md#gga5512b81ef7eeb45b0a12ef62234c8795ac38333011b4f76b036a04e41f1f71e83) [BT\_MESH\_BLINK](group__bt__mesh__prov.md#gga5512b81ef7eeb45b0a12ef62234c8795ac38333011b4f76b036a04e41f1f71e83) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 46](group__bt__mesh__prov.md#gga5512b81ef7eeb45b0a12ef62234c8795ae50031a39d19181df17ee6de1a12272c) [BT\_MESH\_BEEP](group__bt__mesh__prov.md#gga5512b81ef7eeb45b0a12ef62234c8795ae50031a39d19181df17ee6de1a12272c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 47](group__bt__mesh__prov.md#gga5512b81ef7eeb45b0a12ef62234c8795ab45021af96db0465f5edc6e0ea7b6079) [BT\_MESH\_VIBRATE](group__bt__mesh__prov.md#gga5512b81ef7eeb45b0a12ef62234c8795ab45021af96db0465f5edc6e0ea7b6079) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 48](group__bt__mesh__prov.md#gga5512b81ef7eeb45b0a12ef62234c8795a3586ffa3e36247e0d90b83c3f075e591) [BT\_MESH\_DISPLAY\_NUMBER](group__bt__mesh__prov.md#gga5512b81ef7eeb45b0a12ef62234c8795a3586ffa3e36247e0d90b83c3f075e591) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 49](group__bt__mesh__prov.md#gga5512b81ef7eeb45b0a12ef62234c8795aa07d600f2afe278729bb4e35d41bf29b) [BT\_MESH\_DISPLAY\_STRING](group__bt__mesh__prov.md#gga5512b81ef7eeb45b0a12ef62234c8795aa07d600f2afe278729bb4e35d41bf29b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

50} [bt\_mesh\_output\_action\_t](group__bt__mesh__prov.md#ga5512b81ef7eeb45b0a12ef62234c8795);

51

[ 53](group__bt__mesh__prov.md#gaf71f3dbdef6b8c085e9a4f068e1f60c5)typedef enum {

[ 54](group__bt__mesh__prov.md#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ac721b070cad51f1cd9aa1f0b60e59056) [BT\_MESH\_NO\_INPUT](group__bt__mesh__prov.md#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ac721b070cad51f1cd9aa1f0b60e59056) = 0,

[ 55](group__bt__mesh__prov.md#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ae4902ce51142fa49d2d5e97165d6f51c) [BT\_MESH\_PUSH](group__bt__mesh__prov.md#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ae4902ce51142fa49d2d5e97165d6f51c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 56](group__bt__mesh__prov.md#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ad6f22211d09614181cb5b0f42300a9ee) [BT\_MESH\_TWIST](group__bt__mesh__prov.md#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ad6f22211d09614181cb5b0f42300a9ee) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 57](group__bt__mesh__prov.md#ggaf71f3dbdef6b8c085e9a4f068e1f60c5aa0de3817e863d1f06888100de24fb4b0) [BT\_MESH\_ENTER\_NUMBER](group__bt__mesh__prov.md#ggaf71f3dbdef6b8c085e9a4f068e1f60c5aa0de3817e863d1f06888100de24fb4b0) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 58](group__bt__mesh__prov.md#ggaf71f3dbdef6b8c085e9a4f068e1f60c5a5d6bd8e6110c8f53245840aead4201c2) [BT\_MESH\_ENTER\_STRING](group__bt__mesh__prov.md#ggaf71f3dbdef6b8c085e9a4f068e1f60c5a5d6bd8e6110c8f53245840aead4201c2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

59} [bt\_mesh\_input\_action\_t](group__bt__mesh__prov.md#gaf71f3dbdef6b8c085e9a4f068e1f60c5);

60

[ 62](group__bt__mesh__prov.md#gaa157eb0fee30c28092a11993872b8fdd)typedef enum {

[ 63](group__bt__mesh__prov.md#ggaa157eb0fee30c28092a11993872b8fdda5142f018a5426a047688c6507b3af4f8) [BT\_MESH\_PROV\_ADV](group__bt__mesh__prov.md#ggaa157eb0fee30c28092a11993872b8fdda5142f018a5426a047688c6507b3af4f8) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 64](group__bt__mesh__prov.md#ggaa157eb0fee30c28092a11993872b8fdda27c9c1278acc887214a4a30294bf52d8) [BT\_MESH\_PROV\_GATT](group__bt__mesh__prov.md#ggaa157eb0fee30c28092a11993872b8fdda27c9c1278acc887214a4a30294bf52d8) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 65](group__bt__mesh__prov.md#ggaa157eb0fee30c28092a11993872b8fdda4222d03b09ba43b6ea772738b8987501) [BT\_MESH\_PROV\_REMOTE](group__bt__mesh__prov.md#ggaa157eb0fee30c28092a11993872b8fdda4222d03b09ba43b6ea772738b8987501) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

66} [bt\_mesh\_prov\_bearer\_t](group__bt__mesh__prov.md#gaa157eb0fee30c28092a11993872b8fdd);

67

[ 69](group__bt__mesh__prov.md#gaf93f7b49dada5c3f7accc54663648e48)typedef enum {

[ 70](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48a487ffb56c8c15a37b69fa1699fff301a) [BT\_MESH\_PROV\_OOB\_OTHER](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48a487ffb56c8c15a37b69fa1699fff301a) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 71](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48ad861e8de3c1fbc1658a6d0fba38785dd) [BT\_MESH\_PROV\_OOB\_URI](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48ad861e8de3c1fbc1658a6d0fba38785dd) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 72](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48a34d005022a75446a386006f7690a473e) [BT\_MESH\_PROV\_OOB\_2D\_CODE](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48a34d005022a75446a386006f7690a473e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 73](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48abe8fd10b49a7bb6c7499eb73ae3876d3) [BT\_MESH\_PROV\_OOB\_BAR\_CODE](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48abe8fd10b49a7bb6c7499eb73ae3876d3) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 74](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48ad9b4089a740d47950c02b4389d29df56) [BT\_MESH\_PROV\_OOB\_NFC](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48ad9b4089a740d47950c02b4389d29df56) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 75](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48ac5d40459453afebc841f32e1f0b33fbc) [BT\_MESH\_PROV\_OOB\_NUMBER](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48ac5d40459453afebc841f32e1f0b33fbc) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

[ 76](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48a8553379d579a418a6453669323b18088) [BT\_MESH\_PROV\_OOB\_STRING](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48a8553379d579a418a6453669323b18088) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

[ 77](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48a00eb3ba6b7940b02d2fe3892100f497e) [BT\_MESH\_PROV\_OOB\_CERTIFICATE](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48a00eb3ba6b7940b02d2fe3892100f497e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

[ 78](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48aa10724108397ab8d48a3aac2817992f2) [BT\_MESH\_PROV\_OOB\_RECORDS](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48aa10724108397ab8d48a3aac2817992f2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8),

79 /\* 9 - 10 are reserved \*/

[ 80](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48adbbc3c3829bb7caf1a4a5fd2066f3b4a) [BT\_MESH\_PROV\_OOB\_ON\_BOX](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48adbbc3c3829bb7caf1a4a5fd2066f3b4a) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11),

[ 81](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48ae855a27a18bfb6ea03f0ff6165e4a291) [BT\_MESH\_PROV\_OOB\_IN\_BOX](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48ae855a27a18bfb6ea03f0ff6165e4a291) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12),

[ 82](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48a137946e3d53b996b77bebeda5fa930cb) [BT\_MESH\_PROV\_OOB\_ON\_PAPER](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48a137946e3d53b996b77bebeda5fa930cb) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13),

[ 83](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48a4a8a7e4ab87cf360abdb167076349072) [BT\_MESH\_PROV\_OOB\_IN\_MANUAL](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48a4a8a7e4ab87cf360abdb167076349072) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14),

[ 84](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48aa73dd9517eec86e51b48d256fc9660da) [BT\_MESH\_PROV\_OOB\_ON\_DEV](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48aa73dd9517eec86e51b48d256fc9660da) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15),

85} [bt\_mesh\_prov\_oob\_info\_t](group__bt__mesh__prov.md#gaf93f7b49dada5c3f7accc54663648e48);

86

[ 88](structbt__mesh__dev__capabilities.md)struct [bt\_mesh\_dev\_capabilities](structbt__mesh__dev__capabilities.md) {

[ 90](structbt__mesh__dev__capabilities.md#acfef4ecf5ca9324ddc584b9cb910bfe0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [elem\_count](structbt__mesh__dev__capabilities.md#acfef4ecf5ca9324ddc584b9cb910bfe0);

91

[ 93](structbt__mesh__dev__capabilities.md#a762786d98c070d0ae79e09f22bad4b33) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [algorithms](structbt__mesh__dev__capabilities.md#a762786d98c070d0ae79e09f22bad4b33);

94

[ 96](structbt__mesh__dev__capabilities.md#a7f549f5b3923c0b4249e1b21368ee857) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pub\_key\_type](structbt__mesh__dev__capabilities.md#a7f549f5b3923c0b4249e1b21368ee857);

97

[ 99](structbt__mesh__dev__capabilities.md#a744703091988432baa14a84347309bcf) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [oob\_type](structbt__mesh__dev__capabilities.md#a744703091988432baa14a84347309bcf);

100

[ 102](structbt__mesh__dev__capabilities.md#a359caeaf64f45783b0c576ef8ef14975) [bt\_mesh\_output\_action\_t](group__bt__mesh__prov.md#ga5512b81ef7eeb45b0a12ef62234c8795) [output\_actions](structbt__mesh__dev__capabilities.md#a359caeaf64f45783b0c576ef8ef14975);

103

[ 105](structbt__mesh__dev__capabilities.md#a6132c85094980f839cf9dca57d7969ea) [bt\_mesh\_input\_action\_t](group__bt__mesh__prov.md#gaf71f3dbdef6b8c085e9a4f068e1f60c5) [input\_actions](structbt__mesh__dev__capabilities.md#a6132c85094980f839cf9dca57d7969ea);

106

[ 108](structbt__mesh__dev__capabilities.md#a59c959cbd8b1a2aa4e548e7f990cf1f4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [output\_size](structbt__mesh__dev__capabilities.md#a59c959cbd8b1a2aa4e548e7f990cf1f4);

109

[ 111](structbt__mesh__dev__capabilities.md#ac9097c4d634683120509f4c1ac732928) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [input\_size](structbt__mesh__dev__capabilities.md#ac9097c4d634683120509f4c1ac732928);

112};

113

[ 115](structbt__mesh__prov.md)struct [bt\_mesh\_prov](structbt__mesh__prov.md) {

[ 117](structbt__mesh__prov.md#a1152d77c4c4d9271bbd72514d94052f2) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[uuid](structbt__mesh__prov.md#a1152d77c4c4d9271bbd72514d94052f2);

118

[ 124](structbt__mesh__prov.md#a6a11cc0d36ca2f4c5aee67a023c295a2) const char \*[uri](structbt__mesh__prov.md#a6a11cc0d36ca2f4c5aee67a023c295a2);

125

[ 127](structbt__mesh__prov.md#a6ed61556291f7f9d9a32062d588b8f2a) [bt\_mesh\_prov\_oob\_info\_t](group__bt__mesh__prov.md#gaf93f7b49dada5c3f7accc54663648e48) [oob\_info](structbt__mesh__prov.md#a6ed61556291f7f9d9a32062d588b8f2a);

128

[ 136](structbt__mesh__prov.md#a1261ba69e785f005d5834ac49da00778) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[public\_key\_be](structbt__mesh__prov.md#a1261ba69e785f005d5834ac49da00778);

[ 144](structbt__mesh__prov.md#a1ab714e9be35242e02099884c3af45f5) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[private\_key\_be](structbt__mesh__prov.md#a1ab714e9be35242e02099884c3af45f5);

145

[ 147](structbt__mesh__prov.md#a97cf41cf857479c8eefee640f7b66788) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[static\_val](structbt__mesh__prov.md#a97cf41cf857479c8eefee640f7b66788);

[ 149](structbt__mesh__prov.md#a97394dded5fd55b553364a566a2441e8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [static\_val\_len](structbt__mesh__prov.md#a97394dded5fd55b553364a566a2441e8);

150

[ 152](structbt__mesh__prov.md#a4c51aa8e5887b3364d9480c92da3a0a0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [output\_size](structbt__mesh__prov.md#a4c51aa8e5887b3364d9480c92da3a0a0);

[ 154](structbt__mesh__prov.md#a8b88959c5eef7f47591468e9c9768b7c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [output\_actions](structbt__mesh__prov.md#a8b88959c5eef7f47591468e9c9768b7c);

155

[ 157](structbt__mesh__prov.md#ab9044f6dbf9780b3237f18270b2c8582) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [input\_size](structbt__mesh__prov.md#ab9044f6dbf9780b3237f18270b2c8582);

[ 159](structbt__mesh__prov.md#af928a9419f684bcbda0563dda2c34d76) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [input\_actions](structbt__mesh__prov.md#af928a9419f684bcbda0563dda2c34d76);

160

[ 174](structbt__mesh__prov.md#afbc65bb8be99f7dc37ecc911f4ac2151) void (\*[capabilities](structbt__mesh__prov.md#afbc65bb8be99f7dc37ecc911f4ac2151))(const struct [bt\_mesh\_dev\_capabilities](structbt__mesh__dev__capabilities.md) \*cap);

175

[ 186](structbt__mesh__prov.md#af5c30f061ba8b0a713a3d54068dd68cc) int (\*[output\_number](structbt__mesh__prov.md#af5c30f061ba8b0a713a3d54068dd68cc))([bt\_mesh\_output\_action\_t](group__bt__mesh__prov.md#ga5512b81ef7eeb45b0a12ef62234c8795) act, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num);

187

[ 197](structbt__mesh__prov.md#a28284efee6478637446702d7839f6b8c) int (\*[output\_string](structbt__mesh__prov.md#a28284efee6478637446702d7839f6b8c))(const char \*str);

198

[ 213](structbt__mesh__prov.md#a31eff9c903ac721bbca7ab586dda9e80) int (\*[input](structbt__mesh__prov.md#a31eff9c903ac721bbca7ab586dda9e80))([bt\_mesh\_input\_action\_t](group__bt__mesh__prov.md#gaf71f3dbdef6b8c085e9a4f068e1f60c5) act, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size);

214

[ 221](structbt__mesh__prov.md#a2717ddf38465b95452724078f780f9e5) void (\*[input\_complete](structbt__mesh__prov.md#a2717ddf38465b95452724078f780f9e5))(void);

222

[ 233](structbt__mesh__prov.md#a8142a3b8120b1686f68513caeac09497) void (\*[unprovisioned\_beacon](structbt__mesh__prov.md#a8142a3b8120b1686f68513caeac09497))([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [uuid](structbt__mesh__prov.md#a1152d77c4c4d9271bbd72514d94052f2)[16],

234 [bt\_mesh\_prov\_oob\_info\_t](group__bt__mesh__prov.md#gaf93f7b49dada5c3f7accc54663648e48) [oob\_info](structbt__mesh__prov.md#a6ed61556291f7f9d9a32062d588b8f2a),

235 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*uri\_hash);

236

[ 245](structbt__mesh__prov.md#a7eddf1f088264f8b6e3fb86dce4c108e) void (\*[unprovisioned\_beacon\_gatt](structbt__mesh__prov.md#a7eddf1f088264f8b6e3fb86dce4c108e))([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [uuid](structbt__mesh__prov.md#a1152d77c4c4d9271bbd72514d94052f2)[16],

246 [bt\_mesh\_prov\_oob\_info\_t](group__bt__mesh__prov.md#gaf93f7b49dada5c3f7accc54663648e48) [oob\_info](structbt__mesh__prov.md#a6ed61556291f7f9d9a32062d588b8f2a));

247

[ 255](structbt__mesh__prov.md#a44efea3e9221c182cbcacce8219ef6b7) void (\*[link\_open](structbt__mesh__prov.md#a44efea3e9221c182cbcacce8219ef6b7))([bt\_mesh\_prov\_bearer\_t](group__bt__mesh__prov.md#gaa157eb0fee30c28092a11993872b8fdd) bearer);

256

[ 264](structbt__mesh__prov.md#a0183cef77dda3978ef8a40ce7aad043a) void (\*[link\_close](structbt__mesh__prov.md#a0183cef77dda3978ef8a40ce7aad043a))([bt\_mesh\_prov\_bearer\_t](group__bt__mesh__prov.md#gaa157eb0fee30c28092a11993872b8fdd) bearer);

265

[ 275](structbt__mesh__prov.md#ad55abc2b1632455bb23fbd8b03df85ea) void (\*[complete](structbt__mesh__prov.md#ad55abc2b1632455bb23fbd8b03df85ea))([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr);

276

[ 284](structbt__mesh__prov.md#ac131476cdeb002f0027407b4cf80c2b5) void (\*[reprovisioned](structbt__mesh__prov.md#ac131476cdeb002f0027407b4cf80c2b5))([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr);

285

[ 297](structbt__mesh__prov.md#aaa49675e358ea4cba7552b3e855befba) void (\*[node\_added](structbt__mesh__prov.md#aaa49675e358ea4cba7552b3e855befba))([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [uuid](structbt__mesh__prov.md#a1152d77c4c4d9271bbd72514d94052f2)[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

298 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_elem);

299

[ 308](structbt__mesh__prov.md#ae87570de25c89e74bece2516ff957779) void (\*[reset](structbt__mesh__prov.md#ae87570de25c89e74bece2516ff957779))(void);

309};

310

311struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md);

312struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md);

313

[ 323](group__bt__mesh__prov.md#ga2592abf429b40ef9242bce26f5bd085e)int [bt\_mesh\_input\_string](group__bt__mesh__prov.md#ga2592abf429b40ef9242bce26f5bd085e)(const char \*str);

324

[ 334](group__bt__mesh__prov.md#gace8cbf2a6e9144d3118054f234de02ef)int [bt\_mesh\_input\_number](group__bt__mesh__prov.md#gace8cbf2a6e9144d3118054f234de02ef)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num);

335

[ 342](group__bt__mesh__prov.md#gae33b5b6e9650b49d46494b4a81b18674)int [bt\_mesh\_prov\_remote\_pub\_key\_set](group__bt__mesh__prov.md#gae33b5b6e9650b49d46494b4a81b18674)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) public\_key[64]);

343

[ 363](group__bt__mesh__prov.md#ga80be35bf7287e62cb47d8fba99d648a9)int [bt\_mesh\_auth\_method\_set\_input](group__bt__mesh__prov.md#ga80be35bf7287e62cb47d8fba99d648a9)([bt\_mesh\_input\_action\_t](group__bt__mesh__prov.md#gaf71f3dbdef6b8c085e9a4f068e1f60c5) action, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size);

364

[ 387](group__bt__mesh__prov.md#gad66ccc725a1cfdf2b79076f22f853f84)int [bt\_mesh\_auth\_method\_set\_output](group__bt__mesh__prov.md#gad66ccc725a1cfdf2b79076f22f853f84)([bt\_mesh\_output\_action\_t](group__bt__mesh__prov.md#ga5512b81ef7eeb45b0a12ef62234c8795) action, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size);

388

[ 401](group__bt__mesh__prov.md#ga7b6024dc32f6ec7f26cbf91545911084)int [bt\_mesh\_auth\_method\_set\_static](group__bt__mesh__prov.md#ga7b6024dc32f6ec7f26cbf91545911084)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*static\_val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size);

402

[ 417](group__bt__mesh__prov.md#gabab41ebdcae2eaa109e03cb2d8fa78c6)int [bt\_mesh\_auth\_method\_set\_none](group__bt__mesh__prov.md#gabab41ebdcae2eaa109e03cb2d8fa78c6)(void);

418

[ 427](group__bt__mesh__prov.md#ga6c8dc1b09d4cde8738be83c992b860a9)int [bt\_mesh\_prov\_enable](group__bt__mesh__prov.md#ga6c8dc1b09d4cde8738be83c992b860a9)([bt\_mesh\_prov\_bearer\_t](group__bt__mesh__prov.md#gaa157eb0fee30c28092a11993872b8fdd) bearers);

428

[ 437](group__bt__mesh__prov.md#gac7e084e7d12a93377d49b1c3d6313399)int [bt\_mesh\_prov\_disable](group__bt__mesh__prov.md#gac7e084e7d12a93377d49b1c3d6313399)([bt\_mesh\_prov\_bearer\_t](group__bt__mesh__prov.md#gaa157eb0fee30c28092a11993872b8fdd) bearers);

438

[ 454](group__bt__mesh__prov.md#ga4ed6e078c1c0f197758c8dbb23db30f6)int [bt\_mesh\_provision](group__bt__mesh__prov.md#ga4ed6e078c1c0f197758c8dbb23db30f6)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_key[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_idx](structbt__mesh__rpr__node.md#a2197a70aa97209a60136a09da1f513b2),

455 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) iv\_index, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr](structbt__mesh__rpr__node.md#a10ec7b9c480513e742566c6c3b9c4973),

456 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dev\_key[16]);

457

[ 468](group__bt__mesh__prov.md#ga0bfae4ebda53052cfa027c3a7ae51ec8)int [bt\_mesh\_provision\_adv](group__bt__mesh__prov.md#ga0bfae4ebda53052cfa027c3a7ae51ec8)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uuid[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_idx](structbt__mesh__rpr__node.md#a2197a70aa97209a60136a09da1f513b2), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr](structbt__mesh__rpr__node.md#a10ec7b9c480513e742566c6c3b9c4973),

469 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attention\_duration);

470

[ 481](group__bt__mesh__prov.md#ga60666e0d7629caf36026974621bae664)int [bt\_mesh\_provision\_gatt](group__bt__mesh__prov.md#ga60666e0d7629caf36026974621bae664)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uuid[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_idx](structbt__mesh__rpr__node.md#a2197a70aa97209a60136a09da1f513b2), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr](structbt__mesh__rpr__node.md#a10ec7b9c480513e742566c6c3b9c4973),

482 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attention\_duration);

483

[ 496](group__bt__mesh__prov.md#ga9fc414e4e15d6b3ab0dae5483ed62982)int [bt\_mesh\_provision\_remote](group__bt__mesh__prov.md#ga9fc414e4e15d6b3ab0dae5483ed62982)(struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli,

497 const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*srv,

498 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uuid[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_idx](structbt__mesh__rpr__node.md#a2197a70aa97209a60136a09da1f513b2),

499 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr](structbt__mesh__rpr__node.md#a10ec7b9c480513e742566c6c3b9c4973));

500

[ 533](group__bt__mesh__prov.md#gaa02583390f635ac251d22ed9ff953974)int [bt\_mesh\_reprovision\_remote](group__bt__mesh__prov.md#gaa02583390f635ac251d22ed9ff953974)(struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli,

534 struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*srv,

535 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr](structbt__mesh__rpr__node.md#a10ec7b9c480513e742566c6c3b9c4973), bool comp\_change);

536

[ 546](group__bt__mesh__prov.md#ga0307e62001ba7fa303ed311ebc47f116)bool [bt\_mesh\_is\_provisioned](group__bt__mesh__prov.md#ga0307e62001ba7fa303ed311ebc47f116)(void);

547

551

558

[ 560](group__bt__mesh.md#ga0d6985da3c7be76732ee103458b77121)#define BT\_MESH\_NET\_PRIMARY 0x000

561

[ 563](group__bt__mesh.md#gac588eefe83db94784a420ce063f02b55)#define BT\_MESH\_FEAT\_RELAY BIT(0)

[ 565](group__bt__mesh.md#gaee648ce202316c56d4d588cb0ad5aeb4)#define BT\_MESH\_FEAT\_PROXY BIT(1)

[ 567](group__bt__mesh.md#ga8f27086b3bc3c4a6e14621836f9f8e80)#define BT\_MESH\_FEAT\_FRIEND BIT(2)

[ 569](group__bt__mesh.md#gaad71a36c82b4e4d3fa334ecff5cc0171)#define BT\_MESH\_FEAT\_LOW\_POWER BIT(3)

[ 571](group__bt__mesh.md#gac337fd8688d70e862974e010ad42a11b)#define BT\_MESH\_FEAT\_SUPPORTED (BT\_MESH\_FEAT\_RELAY | \

572 BT\_MESH\_FEAT\_PROXY | \

573 BT\_MESH\_FEAT\_FRIEND | \

574 BT\_MESH\_FEAT\_LOW\_POWER)

575

[ 587](group__bt__mesh.md#ga521def6f74467a9bd3f2757c6aabd405)int [bt\_mesh\_init](group__bt__mesh.md#ga521def6f74467a9bd3f2757c6aabd405)(const struct [bt\_mesh\_prov](structbt__mesh__prov.md) \*prov,

588 const struct [bt\_mesh\_comp](structbt__mesh__comp.md) \*comp);

589

[ 600](group__bt__mesh.md#ga69fc65f4e07e6007388473f139e5d8d8)void [bt\_mesh\_reset](group__bt__mesh.md#ga69fc65f4e07e6007388473f139e5d8d8)(void);

601

[ 616](group__bt__mesh.md#ga6c209dbad6881f1e9634d9b7d42f2c34)int [bt\_mesh\_suspend](group__bt__mesh.md#ga6c209dbad6881f1e9634d9b7d42f2c34)(void);

617

[ 625](group__bt__mesh.md#gaa9114ce8941e641dbb23828d7c0451fd)int [bt\_mesh\_resume](group__bt__mesh.md#gaa9114ce8941e641dbb23828d7c0451fd)(void);

626

[ 635](group__bt__mesh.md#ga3fdc601bd036477f6bdf212667c6b0c9)void [bt\_mesh\_iv\_update\_test](group__bt__mesh.md#ga3fdc601bd036477f6bdf212667c6b0c9)(bool enable);

636

[ 645](group__bt__mesh.md#gacdf00423b03057fdf3a4207ee579eb74)bool [bt\_mesh\_iv\_update](group__bt__mesh.md#gacdf00423b03057fdf3a4207ee579eb74)(void);

646

[ 658](group__bt__mesh.md#ga7964f5b1abb7b12728e4ec224c95c849)int [bt\_mesh\_lpn\_set](group__bt__mesh.md#ga7964f5b1abb7b12728e4ec224c95c849)(bool enable);

659

[ 667](group__bt__mesh.md#ga3fd66605950a55e299ca3a7cc697d453)int [bt\_mesh\_lpn\_poll](group__bt__mesh.md#ga3fd66605950a55e299ca3a7cc697d453)(void);

668

[ 670](structbt__mesh__lpn__cb.md)struct [bt\_mesh\_lpn\_cb](structbt__mesh__lpn__cb.md) {

[ 682](structbt__mesh__lpn__cb.md#a74b8b398b383518af069266cf3b0be91) void (\*[established](structbt__mesh__lpn__cb.md#a74b8b398b383518af069266cf3b0be91))([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) friend\_addr,

683 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) queue\_size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) recv\_window);

684

[ 693](structbt__mesh__lpn__cb.md#af2e2f5043503c62926f96a5fcb48890c) void (\*[terminated](structbt__mesh__lpn__cb.md#af2e2f5043503c62926f96a5fcb48890c))([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) friend\_addr);

694

[ 707](structbt__mesh__lpn__cb.md#a9805ad8578faec5b371d6f39178332ef) void (\*[polled](structbt__mesh__lpn__cb.md#a9805ad8578faec5b371d6f39178332ef))([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) friend\_addr, bool retry);

708};

709

[ 715](group__bt__mesh.md#gac18d4ce09495a8ade098a6320bb26ec2)#define BT\_MESH\_LPN\_CB\_DEFINE(\_name) \

716 static const STRUCT\_SECTION\_ITERABLE(bt\_mesh\_lpn\_cb, \

717 \_CONCAT(bt\_mesh\_lpn\_cb\_, \

718 \_name))

719

[ 721](structbt__mesh__friend__cb.md)struct [bt\_mesh\_friend\_cb](structbt__mesh__friend__cb.md) {

[ 732](structbt__mesh__friend__cb.md#a824ed814a46a3954d2c6f669c8900156) void (\*[established](structbt__mesh__friend__cb.md#a824ed814a46a3954d2c6f669c8900156))([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) lpn\_addr,

733 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) recv\_delay, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) polltimeout);

734

[ 743](structbt__mesh__friend__cb.md#a1c0d570eb1b857c65b3b5b4ce31999d6) void (\*[terminated](structbt__mesh__friend__cb.md#a1c0d570eb1b857c65b3b5b4ce31999d6))([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) lpn\_addr);

744

[ 756](structbt__mesh__friend__cb.md#a7b904967d89173f82ac26216e3849d23) void (\*[polled](structbt__mesh__friend__cb.md#a7b904967d89173f82ac26216e3849d23))([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) lpn\_addr);

757};

758

[ 767](group__bt__mesh.md#ga4f00fa03af86b39e24140eb09c51ca4c)#define BT\_MESH\_FRIEND\_CB\_DEFINE(\_name) \

768 static const STRUCT\_SECTION\_ITERABLE(bt\_mesh\_friend\_cb, \

769 \_CONCAT(bt\_mesh\_friend\_cb\_, \

770 \_name))

771#if defined(CONFIG\_BT\_TESTING)

772struct bt\_mesh\_snb {

774 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

775

777 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_id;

778

780 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) iv\_idx;

781

783 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) auth\_val;

784};

785

786struct bt\_mesh\_prb {

788 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) random[13];

789

791 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

792

794 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) iv\_idx;

795

797 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) auth\_tag;

798};

799

801struct bt\_mesh\_beacon\_cb {

809 void (\*snb\_received)(const struct bt\_mesh\_snb \*snb);

810

818 void (\*priv\_received)(const struct bt\_mesh\_prb \*prb);

819};

820

829#define BT\_MESH\_BEACON\_CB\_DEFINE(\_name) \

830 static const STRUCT\_SECTION\_ITERABLE(bt\_mesh\_beacon\_cb, \

831 \_CONCAT(bt\_mesh\_beacon\_cb\_, \

832 \_name))

833#endif

834

[ 843](group__bt__mesh.md#ga28b9b1d7d732e300be8d4bbffdbad391)int [bt\_mesh\_friend\_terminate](group__bt__mesh.md#ga28b9b1d7d732e300be8d4bbffdbad391)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) lpn\_addr);

844

[ 856](group__bt__mesh.md#ga62f9a72c4e9dc5e4f3f42bd4df4fe452)void [bt\_mesh\_rpl\_pending\_store](group__bt__mesh.md#ga62f9a72c4e9dc5e4f3f42bd4df4fe452)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr);

857

[ 873](group__bt__mesh.md#ga20fe74e33e6a35c452cd076c78aa4f05)const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[bt\_mesh\_va\_uuid\_get](group__bt__mesh.md#ga20fe74e33e6a35c452cd076c78aa4f05)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*uuid, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*retaddr);

874

875#ifdef \_\_cplusplus

876}

877#endif

878

882

883#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_MAIN\_H\_ \*/

[bt\_mesh\_is\_provisioned](group__bt__mesh__prov.md#ga0307e62001ba7fa303ed311ebc47f116)

bool bt\_mesh\_is\_provisioned(void)

Check if the local node has been provisioned.

[bt\_mesh\_provision\_adv](group__bt__mesh__prov.md#ga0bfae4ebda53052cfa027c3a7ae51ec8)

int bt\_mesh\_provision\_adv(const uint8\_t uuid[16], uint16\_t net\_idx, uint16\_t addr, uint8\_t attention\_duration)

Provision a Mesh Node using PB-ADV.

[bt\_mesh\_input\_string](group__bt__mesh__prov.md#ga2592abf429b40ef9242bce26f5bd085e)

int bt\_mesh\_input\_string(const char \*str)

Provide provisioning input OOB string.

[bt\_mesh\_provision](group__bt__mesh__prov.md#ga4ed6e078c1c0f197758c8dbb23db30f6)

int bt\_mesh\_provision(const uint8\_t net\_key[16], uint16\_t net\_idx, uint8\_t flags, uint32\_t iv\_index, uint16\_t addr, const uint8\_t dev\_key[16])

Provision the local Mesh Node.

[bt\_mesh\_output\_action\_t](group__bt__mesh__prov.md#ga5512b81ef7eeb45b0a12ef62234c8795)

bt\_mesh\_output\_action\_t

Available Provisioning output authentication actions.

**Definition** main.h:43

[bt\_mesh\_provision\_gatt](group__bt__mesh__prov.md#ga60666e0d7629caf36026974621bae664)

int bt\_mesh\_provision\_gatt(const uint8\_t uuid[16], uint16\_t net\_idx, uint16\_t addr, uint8\_t attention\_duration)

Provision a Mesh Node using PB-GATT.

[bt\_mesh\_prov\_enable](group__bt__mesh__prov.md#ga6c8dc1b09d4cde8738be83c992b860a9)

int bt\_mesh\_prov\_enable(bt\_mesh\_prov\_bearer\_t bearers)

Enable specific provisioning bearers.

[bt\_mesh\_auth\_method\_set\_static](group__bt__mesh__prov.md#ga7b6024dc32f6ec7f26cbf91545911084)

int bt\_mesh\_auth\_method\_set\_static(const uint8\_t \*static\_val, uint8\_t size)

Use static OOB authentication.

[bt\_mesh\_auth\_method\_set\_input](group__bt__mesh__prov.md#ga80be35bf7287e62cb47d8fba99d648a9)

int bt\_mesh\_auth\_method\_set\_input(bt\_mesh\_input\_action\_t action, uint8\_t size)

Use Input OOB authentication.

[bt\_mesh\_provision\_remote](group__bt__mesh__prov.md#ga9fc414e4e15d6b3ab0dae5483ed62982)

int bt\_mesh\_provision\_remote(struct bt\_mesh\_rpr\_cli \*cli, const struct bt\_mesh\_rpr\_node \*srv, const uint8\_t uuid[16], uint16\_t net\_idx, uint16\_t addr)

Provision a Mesh Node using PB-Remote.

[bt\_mesh\_reprovision\_remote](group__bt__mesh__prov.md#gaa02583390f635ac251d22ed9ff953974)

int bt\_mesh\_reprovision\_remote(struct bt\_mesh\_rpr\_cli \*cli, struct bt\_mesh\_rpr\_node \*srv, uint16\_t addr, bool comp\_change)

Reprovision a Mesh Node using PB-Remote.

[bt\_mesh\_prov\_bearer\_t](group__bt__mesh__prov.md#gaa157eb0fee30c28092a11993872b8fdd)

bt\_mesh\_prov\_bearer\_t

Available Provisioning bearers.

**Definition** main.h:62

[bt\_mesh\_auth\_method\_set\_none](group__bt__mesh__prov.md#gabab41ebdcae2eaa109e03cb2d8fa78c6)

int bt\_mesh\_auth\_method\_set\_none(void)

Don't use OOB authentication.

[bt\_mesh\_prov\_disable](group__bt__mesh__prov.md#gac7e084e7d12a93377d49b1c3d6313399)

int bt\_mesh\_prov\_disable(bt\_mesh\_prov\_bearer\_t bearers)

Disable specific provisioning bearers.

[bt\_mesh\_input\_number](group__bt__mesh__prov.md#gace8cbf2a6e9144d3118054f234de02ef)

int bt\_mesh\_input\_number(uint32\_t num)

Provide provisioning input OOB number.

[bt\_mesh\_auth\_method\_set\_output](group__bt__mesh__prov.md#gad66ccc725a1cfdf2b79076f22f853f84)

int bt\_mesh\_auth\_method\_set\_output(bt\_mesh\_output\_action\_t action, uint8\_t size)

Use Output OOB authentication.

[bt\_mesh\_prov\_remote\_pub\_key\_set](group__bt__mesh__prov.md#gae33b5b6e9650b49d46494b4a81b18674)

int bt\_mesh\_prov\_remote\_pub\_key\_set(const uint8\_t public\_key[64])

Provide Device public key.

[bt\_mesh\_input\_action\_t](group__bt__mesh__prov.md#gaf71f3dbdef6b8c085e9a4f068e1f60c5)

bt\_mesh\_input\_action\_t

Available Provisioning input authentication actions.

**Definition** main.h:53

[bt\_mesh\_prov\_oob\_info\_t](group__bt__mesh__prov.md#gaf93f7b49dada5c3f7accc54663648e48)

bt\_mesh\_prov\_oob\_info\_t

Out of Band information location.

**Definition** main.h:69

[BT\_MESH\_DISPLAY\_NUMBER](group__bt__mesh__prov.md#gga5512b81ef7eeb45b0a12ef62234c8795a3586ffa3e36247e0d90b83c3f075e591)

@ BT\_MESH\_DISPLAY\_NUMBER

Output numeric.

**Definition** main.h:48

[BT\_MESH\_DISPLAY\_STRING](group__bt__mesh__prov.md#gga5512b81ef7eeb45b0a12ef62234c8795aa07d600f2afe278729bb4e35d41bf29b)

@ BT\_MESH\_DISPLAY\_STRING

Output alphanumeric.

**Definition** main.h:49

[BT\_MESH\_VIBRATE](group__bt__mesh__prov.md#gga5512b81ef7eeb45b0a12ef62234c8795ab45021af96db0465f5edc6e0ea7b6079)

@ BT\_MESH\_VIBRATE

Vibrate.

**Definition** main.h:47

[BT\_MESH\_BLINK](group__bt__mesh__prov.md#gga5512b81ef7eeb45b0a12ef62234c8795ac38333011b4f76b036a04e41f1f71e83)

@ BT\_MESH\_BLINK

Blink.

**Definition** main.h:45

[BT\_MESH\_NO\_OUTPUT](group__bt__mesh__prov.md#gga5512b81ef7eeb45b0a12ef62234c8795ad009060fd1f501c8362a63e6c020b113)

@ BT\_MESH\_NO\_OUTPUT

**Definition** main.h:44

[BT\_MESH\_BEEP](group__bt__mesh__prov.md#gga5512b81ef7eeb45b0a12ef62234c8795ae50031a39d19181df17ee6de1a12272c)

@ BT\_MESH\_BEEP

Beep.

**Definition** main.h:46

[BT\_MESH\_PROV\_GATT](group__bt__mesh__prov.md#ggaa157eb0fee30c28092a11993872b8fdda27c9c1278acc887214a4a30294bf52d8)

@ BT\_MESH\_PROV\_GATT

PB-GATT bearer.

**Definition** main.h:64

[BT\_MESH\_PROV\_REMOTE](group__bt__mesh__prov.md#ggaa157eb0fee30c28092a11993872b8fdda4222d03b09ba43b6ea772738b8987501)

@ BT\_MESH\_PROV\_REMOTE

PB-Remote bearer.

**Definition** main.h:65

[BT\_MESH\_PROV\_ADV](group__bt__mesh__prov.md#ggaa157eb0fee30c28092a11993872b8fdda5142f018a5426a047688c6507b3af4f8)

@ BT\_MESH\_PROV\_ADV

PB-ADV bearer.

**Definition** main.h:63

[BT\_MESH\_PROV\_AUTH\_HMAC\_SHA256\_AES\_CCM](group__bt__mesh__prov.md#ggabe5586cff0697e137730a52728978681a292bf2e4d29f0bd0d746bbb871f2ee5a)

@ BT\_MESH\_PROV\_AUTH\_HMAC\_SHA256\_AES\_CCM

**Definition** main.h:33

[BT\_MESH\_PROV\_AUTH\_CMAC\_AES128\_AES\_CCM](group__bt__mesh__prov.md#ggabe5586cff0697e137730a52728978681affa8679d8be1a12714a34ed09c3b05dd)

@ BT\_MESH\_PROV\_AUTH\_CMAC\_AES128\_AES\_CCM

**Definition** main.h:32

[BT\_MESH\_STATIC\_OOB\_AVAILABLE](group__bt__mesh__prov.md#ggabec90bd95082b9dc8fa3ca27a9d7bc66a30e46fe23e508029b570e1f107b38d40)

@ BT\_MESH\_STATIC\_OOB\_AVAILABLE

Static OOB information available.

**Definition** main.h:38

[BT\_MESH\_OOB\_AUTH\_REQUIRED](group__bt__mesh__prov.md#ggabec90bd95082b9dc8fa3ca27a9d7bc66a61f859a15fabc8d9fd278dabe5a86a37)

@ BT\_MESH\_OOB\_AUTH\_REQUIRED

OOB authentication required.

**Definition** main.h:39

[BT\_MESH\_ENTER\_STRING](group__bt__mesh__prov.md#ggaf71f3dbdef6b8c085e9a4f068e1f60c5a5d6bd8e6110c8f53245840aead4201c2)

@ BT\_MESH\_ENTER\_STRING

Input alphanumeric.

**Definition** main.h:58

[BT\_MESH\_ENTER\_NUMBER](group__bt__mesh__prov.md#ggaf71f3dbdef6b8c085e9a4f068e1f60c5aa0de3817e863d1f06888100de24fb4b0)

@ BT\_MESH\_ENTER\_NUMBER

Input number.

**Definition** main.h:57

[BT\_MESH\_NO\_INPUT](group__bt__mesh__prov.md#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ac721b070cad51f1cd9aa1f0b60e59056)

@ BT\_MESH\_NO\_INPUT

**Definition** main.h:54

[BT\_MESH\_TWIST](group__bt__mesh__prov.md#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ad6f22211d09614181cb5b0f42300a9ee)

@ BT\_MESH\_TWIST

Twist.

**Definition** main.h:56

[BT\_MESH\_PUSH](group__bt__mesh__prov.md#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ae4902ce51142fa49d2d5e97165d6f51c)

@ BT\_MESH\_PUSH

Push.

**Definition** main.h:55

[BT\_MESH\_PROV\_OOB\_CERTIFICATE](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48a00eb3ba6b7940b02d2fe3892100f497e)

@ BT\_MESH\_PROV\_OOB\_CERTIFICATE

Support for certificate-based provisioning.

**Definition** main.h:77

[BT\_MESH\_PROV\_OOB\_ON\_PAPER](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48a137946e3d53b996b77bebeda5fa930cb)

@ BT\_MESH\_PROV\_OOB\_ON\_PAPER

On piece of paper.

**Definition** main.h:82

[BT\_MESH\_PROV\_OOB\_2D\_CODE](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48a34d005022a75446a386006f7690a473e)

@ BT\_MESH\_PROV\_OOB\_2D\_CODE

2D machine-readable code

**Definition** main.h:72

[BT\_MESH\_PROV\_OOB\_OTHER](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48a487ffb56c8c15a37b69fa1699fff301a)

@ BT\_MESH\_PROV\_OOB\_OTHER

Other.

**Definition** main.h:70

[BT\_MESH\_PROV\_OOB\_IN\_MANUAL](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48a4a8a7e4ab87cf360abdb167076349072)

@ BT\_MESH\_PROV\_OOB\_IN\_MANUAL

Inside manual.

**Definition** main.h:83

[BT\_MESH\_PROV\_OOB\_STRING](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48a8553379d579a418a6453669323b18088)

@ BT\_MESH\_PROV\_OOB\_STRING

String.

**Definition** main.h:76

[BT\_MESH\_PROV\_OOB\_RECORDS](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48aa10724108397ab8d48a3aac2817992f2)

@ BT\_MESH\_PROV\_OOB\_RECORDS

Support for provisioning records.

**Definition** main.h:78

[BT\_MESH\_PROV\_OOB\_ON\_DEV](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48aa73dd9517eec86e51b48d256fc9660da)

@ BT\_MESH\_PROV\_OOB\_ON\_DEV

On device.

**Definition** main.h:84

[BT\_MESH\_PROV\_OOB\_BAR\_CODE](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48abe8fd10b49a7bb6c7499eb73ae3876d3)

@ BT\_MESH\_PROV\_OOB\_BAR\_CODE

Bar Code.

**Definition** main.h:73

[BT\_MESH\_PROV\_OOB\_NUMBER](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48ac5d40459453afebc841f32e1f0b33fbc)

@ BT\_MESH\_PROV\_OOB\_NUMBER

Number.

**Definition** main.h:75

[BT\_MESH\_PROV\_OOB\_URI](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48ad861e8de3c1fbc1658a6d0fba38785dd)

@ BT\_MESH\_PROV\_OOB\_URI

Electronic / URI.

**Definition** main.h:71

[BT\_MESH\_PROV\_OOB\_NFC](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48ad9b4089a740d47950c02b4389d29df56)

@ BT\_MESH\_PROV\_OOB\_NFC

Near Field Communication (NFC).

**Definition** main.h:74

[BT\_MESH\_PROV\_OOB\_ON\_BOX](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48adbbc3c3829bb7caf1a4a5fd2066f3b4a)

@ BT\_MESH\_PROV\_OOB\_ON\_BOX

On box.

**Definition** main.h:80

[BT\_MESH\_PROV\_OOB\_IN\_BOX](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48ae855a27a18bfb6ea03f0ff6165e4a291)

@ BT\_MESH\_PROV\_OOB\_IN\_BOX

Inside box.

**Definition** main.h:81

[bt\_mesh\_va\_uuid\_get](group__bt__mesh.md#ga20fe74e33e6a35c452cd076c78aa4f05)

const uint8\_t \* bt\_mesh\_va\_uuid\_get(uint16\_t addr, const uint8\_t \*uuid, uint16\_t \*retaddr)

Iterate stored Label UUIDs.

[bt\_mesh\_friend\_terminate](group__bt__mesh.md#ga28b9b1d7d732e300be8d4bbffdbad391)

int bt\_mesh\_friend\_terminate(uint16\_t lpn\_addr)

Terminate Friendship.

[bt\_mesh\_lpn\_poll](group__bt__mesh.md#ga3fd66605950a55e299ca3a7cc697d453)

int bt\_mesh\_lpn\_poll(void)

Send out a Friend Poll message.

[bt\_mesh\_iv\_update\_test](group__bt__mesh.md#ga3fdc601bd036477f6bdf212667c6b0c9)

void bt\_mesh\_iv\_update\_test(bool enable)

Toggle the IV Update test mode.

[bt\_mesh\_init](group__bt__mesh.md#ga521def6f74467a9bd3f2757c6aabd405)

int bt\_mesh\_init(const struct bt\_mesh\_prov \*prov, const struct bt\_mesh\_comp \*comp)

Initialize Mesh support.

[bt\_mesh\_rpl\_pending\_store](group__bt__mesh.md#ga62f9a72c4e9dc5e4f3f42bd4df4fe452)

void bt\_mesh\_rpl\_pending\_store(uint16\_t addr)

Store pending RPL entry(ies) in the persistent storage.

[bt\_mesh\_reset](group__bt__mesh.md#ga69fc65f4e07e6007388473f139e5d8d8)

void bt\_mesh\_reset(void)

Reset the state of the local Mesh node.

[bt\_mesh\_suspend](group__bt__mesh.md#ga6c209dbad6881f1e9634d9b7d42f2c34)

int bt\_mesh\_suspend(void)

Suspend the Mesh network temporarily.

[bt\_mesh\_lpn\_set](group__bt__mesh.md#ga7964f5b1abb7b12728e4ec224c95c849)

int bt\_mesh\_lpn\_set(bool enable)

Toggle the Low Power feature of the local device.

[bt\_mesh\_resume](group__bt__mesh.md#gaa9114ce8941e641dbb23828d7c0451fd)

int bt\_mesh\_resume(void)

Resume a suspended Mesh network.

[bt\_mesh\_iv\_update](group__bt__mesh.md#gacdf00423b03057fdf3a4207ee579eb74)

bool bt\_mesh\_iv\_update(void)

Toggle the IV Update state.

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_mesh\_comp](structbt__mesh__comp.md)

Node Composition.

**Definition** access.h:1145

[bt\_mesh\_dev\_capabilities](structbt__mesh__dev__capabilities.md)

Device Capabilities.

**Definition** main.h:88

[bt\_mesh\_dev\_capabilities::output\_actions](structbt__mesh__dev__capabilities.md#a359caeaf64f45783b0c576ef8ef14975)

bt\_mesh\_output\_action\_t output\_actions

Supported Output OOB Actions.

**Definition** main.h:102

[bt\_mesh\_dev\_capabilities::output\_size](structbt__mesh__dev__capabilities.md#a59c959cbd8b1a2aa4e548e7f990cf1f4)

uint8\_t output\_size

Maximum size of Output OOB supported.

**Definition** main.h:108

[bt\_mesh\_dev\_capabilities::input\_actions](structbt__mesh__dev__capabilities.md#a6132c85094980f839cf9dca57d7969ea)

bt\_mesh\_input\_action\_t input\_actions

Supported Input OOB Actions.

**Definition** main.h:105

[bt\_mesh\_dev\_capabilities::oob\_type](structbt__mesh__dev__capabilities.md#a744703091988432baa14a84347309bcf)

uint8\_t oob\_type

Supported OOB Types.

**Definition** main.h:99

[bt\_mesh\_dev\_capabilities::algorithms](structbt__mesh__dev__capabilities.md#a762786d98c070d0ae79e09f22bad4b33)

uint16\_t algorithms

Supported algorithms and other capabilities.

**Definition** main.h:93

[bt\_mesh\_dev\_capabilities::pub\_key\_type](structbt__mesh__dev__capabilities.md#a7f549f5b3923c0b4249e1b21368ee857)

uint8\_t pub\_key\_type

Supported public key types.

**Definition** main.h:96

[bt\_mesh\_dev\_capabilities::input\_size](structbt__mesh__dev__capabilities.md#ac9097c4d634683120509f4c1ac732928)

uint8\_t input\_size

Maximum size in octets of Input OOB supported.

**Definition** main.h:111

[bt\_mesh\_dev\_capabilities::elem\_count](structbt__mesh__dev__capabilities.md#acfef4ecf5ca9324ddc584b9cb910bfe0)

uint8\_t elem\_count

Number of elements supported by the device.

**Definition** main.h:90

[bt\_mesh\_friend\_cb](structbt__mesh__friend__cb.md)

Friend Node callback functions.

**Definition** main.h:721

[bt\_mesh\_friend\_cb::terminated](structbt__mesh__friend__cb.md#a1c0d570eb1b857c65b3b5b4ce31999d6)

void(\* terminated)(uint16\_t net\_idx, uint16\_t lpn\_addr)

Friendship terminated.

**Definition** main.h:743

[bt\_mesh\_friend\_cb::polled](structbt__mesh__friend__cb.md#a7b904967d89173f82ac26216e3849d23)

void(\* polled)(uint16\_t net\_idx, uint16\_t lpn\_addr)

Friend Poll Request.

**Definition** main.h:756

[bt\_mesh\_friend\_cb::established](structbt__mesh__friend__cb.md#a824ed814a46a3954d2c6f669c8900156)

void(\* established)(uint16\_t net\_idx, uint16\_t lpn\_addr, uint8\_t recv\_delay, uint32\_t polltimeout)

Friendship established.

**Definition** main.h:732

[bt\_mesh\_lpn\_cb](structbt__mesh__lpn__cb.md)

Low Power Node callback functions.

**Definition** main.h:670

[bt\_mesh\_lpn\_cb::established](structbt__mesh__lpn__cb.md#a74b8b398b383518af069266cf3b0be91)

void(\* established)(uint16\_t net\_idx, uint16\_t friend\_addr, uint8\_t queue\_size, uint8\_t recv\_window)

Friendship established.

**Definition** main.h:682

[bt\_mesh\_lpn\_cb::polled](structbt__mesh__lpn__cb.md#a9805ad8578faec5b371d6f39178332ef)

void(\* polled)(uint16\_t net\_idx, uint16\_t friend\_addr, bool retry)

Local Poll Request.

**Definition** main.h:707

[bt\_mesh\_lpn\_cb::terminated](structbt__mesh__lpn__cb.md#af2e2f5043503c62926f96a5fcb48890c)

void(\* terminated)(uint16\_t net\_idx, uint16\_t friend\_addr)

Friendship terminated.

**Definition** main.h:693

[bt\_mesh\_prov](structbt__mesh__prov.md)

Provisioning properties & capabilities.

**Definition** main.h:115

[bt\_mesh\_prov::link\_close](structbt__mesh__prov.md#a0183cef77dda3978ef8a40ce7aad043a)

void(\* link\_close)(bt\_mesh\_prov\_bearer\_t bearer)

Provisioning link has been closed.

**Definition** main.h:264

[bt\_mesh\_prov::uuid](structbt__mesh__prov.md#a1152d77c4c4d9271bbd72514d94052f2)

const uint8\_t \* uuid

The UUID that's used when advertising as unprovisioned.

**Definition** main.h:117

[bt\_mesh\_prov::public\_key\_be](structbt__mesh__prov.md#a1261ba69e785f005d5834ac49da00778)

const uint8\_t \* public\_key\_be

Pointer to Public Key in big-endian for OOB public key type support.

**Definition** main.h:136

[bt\_mesh\_prov::private\_key\_be](structbt__mesh__prov.md#a1ab714e9be35242e02099884c3af45f5)

const uint8\_t \* private\_key\_be

Pointer to Private Key in big-endian for OOB public key type support.

**Definition** main.h:144

[bt\_mesh\_prov::input\_complete](structbt__mesh__prov.md#a2717ddf38465b95452724078f780f9e5)

void(\* input\_complete)(void)

The other device finished their OOB input.

**Definition** main.h:221

[bt\_mesh\_prov::output\_string](structbt__mesh__prov.md#a28284efee6478637446702d7839f6b8c)

int(\* output\_string)(const char \*str)

Output of a string is requested.

**Definition** main.h:197

[bt\_mesh\_prov::input](structbt__mesh__prov.md#a31eff9c903ac721bbca7ab586dda9e80)

int(\* input)(bt\_mesh\_input\_action\_t act, uint8\_t size)

Input is requested.

**Definition** main.h:213

[bt\_mesh\_prov::link\_open](structbt__mesh__prov.md#a44efea3e9221c182cbcacce8219ef6b7)

void(\* link\_open)(bt\_mesh\_prov\_bearer\_t bearer)

Provisioning link has been opened.

**Definition** main.h:255

[bt\_mesh\_prov::output\_size](structbt__mesh__prov.md#a4c51aa8e5887b3364d9480c92da3a0a0)

uint8\_t output\_size

Maximum size of Output OOB supported.

**Definition** main.h:152

[bt\_mesh\_prov::uri](structbt__mesh__prov.md#a6a11cc0d36ca2f4c5aee67a023c295a2)

const char \* uri

Optional URI.

**Definition** main.h:124

[bt\_mesh\_prov::oob\_info](structbt__mesh__prov.md#a6ed61556291f7f9d9a32062d588b8f2a)

bt\_mesh\_prov\_oob\_info\_t oob\_info

Out of Band information field.

**Definition** main.h:127

[bt\_mesh\_prov::unprovisioned\_beacon\_gatt](structbt__mesh__prov.md#a7eddf1f088264f8b6e3fb86dce4c108e)

void(\* unprovisioned\_beacon\_gatt)(uint8\_t uuid[16], bt\_mesh\_prov\_oob\_info\_t oob\_info)

PB-GATT Unprovisioned Advertising has been received.

**Definition** main.h:245

[bt\_mesh\_prov::unprovisioned\_beacon](structbt__mesh__prov.md#a8142a3b8120b1686f68513caeac09497)

void(\* unprovisioned\_beacon)(uint8\_t uuid[16], bt\_mesh\_prov\_oob\_info\_t oob\_info, uint32\_t \*uri\_hash)

Unprovisioned beacon has been received.

**Definition** main.h:233

[bt\_mesh\_prov::output\_actions](structbt__mesh__prov.md#a8b88959c5eef7f47591468e9c9768b7c)

uint16\_t output\_actions

Supported Output OOB Actions.

**Definition** main.h:154

[bt\_mesh\_prov::static\_val\_len](structbt__mesh__prov.md#a97394dded5fd55b553364a566a2441e8)

uint8\_t static\_val\_len

Static OOB value length.

**Definition** main.h:149

[bt\_mesh\_prov::static\_val](structbt__mesh__prov.md#a97cf41cf857479c8eefee640f7b66788)

const uint8\_t \* static\_val

Static OOB value.

**Definition** main.h:147

[bt\_mesh\_prov::node\_added](structbt__mesh__prov.md#aaa49675e358ea4cba7552b3e855befba)

void(\* node\_added)(uint16\_t net\_idx, uint8\_t uuid[16], uint16\_t addr, uint8\_t num\_elem)

A new node has been added to the provisioning database.

**Definition** main.h:297

[bt\_mesh\_prov::input\_size](structbt__mesh__prov.md#ab9044f6dbf9780b3237f18270b2c8582)

uint8\_t input\_size

Maximum size of Input OOB supported.

**Definition** main.h:157

[bt\_mesh\_prov::reprovisioned](structbt__mesh__prov.md#ac131476cdeb002f0027407b4cf80c2b5)

void(\* reprovisioned)(uint16\_t addr)

Local node has been reprovisioned.

**Definition** main.h:284

[bt\_mesh\_prov::complete](structbt__mesh__prov.md#ad55abc2b1632455bb23fbd8b03df85ea)

void(\* complete)(uint16\_t net\_idx, uint16\_t addr)

Provisioning is complete.

**Definition** main.h:275

[bt\_mesh\_prov::reset](structbt__mesh__prov.md#ae87570de25c89e74bece2516ff957779)

void(\* reset)(void)

Node has been reset.

**Definition** main.h:308

[bt\_mesh\_prov::output\_number](structbt__mesh__prov.md#af5c30f061ba8b0a713a3d54068dd68cc)

int(\* output\_number)(bt\_mesh\_output\_action\_t act, uint32\_t num)

Output of a number is requested.

**Definition** main.h:186

[bt\_mesh\_prov::input\_actions](structbt__mesh__prov.md#af928a9419f684bcbda0563dda2c34d76)

uint16\_t input\_actions

Supported Input OOB Actions.

**Definition** main.h:159

[bt\_mesh\_prov::capabilities](structbt__mesh__prov.md#afbc65bb8be99f7dc37ecc911f4ac2151)

void(\* capabilities)(const struct bt\_mesh\_dev\_capabilities \*cap)

Provisioning Capabilities.

**Definition** main.h:174

[bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md)

Remote Provisioning Client model instance.

**Definition** rpr\_cli.h:64

[bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md)

Remote provisioning actor, as seen across the mesh.

**Definition** rpr.h:76

[bt\_mesh\_rpr\_node::addr](structbt__mesh__rpr__node.md#a10ec7b9c480513e742566c6c3b9c4973)

uint16\_t addr

Unicast address of the node.

**Definition** rpr.h:78

[bt\_mesh\_rpr\_node::net\_idx](structbt__mesh__rpr__node.md#a2197a70aa97209a60136a09da1f513b2)

uint16\_t net\_idx

Network index used when communicating with the node.

**Definition** rpr.h:80

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [main.h](main_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

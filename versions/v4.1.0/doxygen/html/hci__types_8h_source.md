---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/hci__types_8h_source.html
original_path: doxygen/html/hci__types_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hci\_types.h

[Go to the documentation of this file.](hci__types_8h.md)

1/\* hci.h - Bluetooth Host Control Interface types \*/

2

3/\*

4 \* Copyright (c) 2015-2016 Intel Corporation

5 \* Copyright (c) 2023 Nordic Semiconductor ASA

6 \*

7 \* SPDX-License-Identifier: Apache-2.0

8 \*/

9#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_HCI\_TYPES\_H\_

10#define ZEPHYR\_INCLUDE\_BLUETOOTH\_HCI\_TYPES\_H\_

11

12#include <[stdbool.h](stdbool_8h.md)>

13#include <[stdint.h](stdint_8h.md)>

14#include <[string.h](string_8h.md)>

15

16#include <[zephyr/toolchain.h](toolchain_8h.md)>

17#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

18#include <[zephyr/sys/util.h](sys_2util_8h.md)>

19#include <[zephyr/bluetooth/addr.h](addr_8h.md)>

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

25/\* Bluetooth spec v5.4 Vol 4, Part A Table 2.1: HCI packet indicators

26 \* The following definitions are intended for use with the UART Transport Layer and

27 \* may be reused with other transport layers if desired.

28 \*/

[ 29](hci__types_8h.md#a2a578399cd3a1ed875ba2c8a49b8129b)#define BT\_HCI\_H4\_NONE 0x00 /\* None of the known packet types \*/

[ 30](hci__types_8h.md#a524788ee4d21fe9a4625c35e1756bfe9)#define BT\_HCI\_H4\_CMD 0x01 /\* HCI Command packet \*/

[ 31](hci__types_8h.md#a17386452bbd60c85959296b6539232bd)#define BT\_HCI\_H4\_ACL 0x02 /\* HCI ACL Data packet \*/

[ 32](hci__types_8h.md#a9e1c93f187ed5864cebefccea1b3faa2)#define BT\_HCI\_H4\_SCO 0x03 /\* HCI Synchronous Data packet \*/

[ 33](hci__types_8h.md#a783053bc2846063e50755f1590e81ba8)#define BT\_HCI\_H4\_EVT 0x04 /\* HCI Event packet \*/

[ 34](hci__types_8h.md#af5e6a53cc7d9619f4ac2ea5bd3256149)#define BT\_HCI\_H4\_ISO 0x05 /\* HCI ISO Data packet \*/

35

[ 36](hci__types_8h.md#a1109fda761e1ef8c6df935cf97fdc646)#define BT\_HCI\_OWN\_ADDR\_PUBLIC 0x00

[ 37](hci__types_8h.md#a8693ea59b948960e627d62785515996e)#define BT\_HCI\_OWN\_ADDR\_RANDOM 0x01

[ 38](hci__types_8h.md#a92a5db1ce46bbf3ddeaab4da76bc6685)#define BT\_HCI\_OWN\_ADDR\_RPA\_OR\_PUBLIC 0x02

[ 39](hci__types_8h.md#aec05e679e29fde812e9a066e672405b4)#define BT\_HCI\_OWN\_ADDR\_RPA\_OR\_RANDOM 0x03

[ 40](hci__types_8h.md#a115907057c92a59a407d261133946b59)#define BT\_HCI\_OWN\_ADDR\_RPA\_MASK 0x02

41

[ 42](hci__types_8h.md#aebc5bd975899f765afe697ab322db114)#define BT\_HCI\_PEER\_ADDR\_RPA\_UNRESOLVED 0xfe

[ 43](hci__types_8h.md#a1e6d78149d0990511b2b6dffb617069e)#define BT\_HCI\_PEER\_ADDR\_ANONYMOUS 0xff

44

[ 45](hci__types_8h.md#a90a6c0c50f915c347b75ac3ca46996ac)#define BT\_ENC\_KEY\_SIZE\_MIN 0x07

[ 46](hci__types_8h.md#a4c274cd6947d37bf4f895ca0002c4f63)#define BT\_ENC\_KEY\_SIZE\_MAX 0x10

47

[ 48](hci__types_8h.md#aa85640ad3a1aa78cf862a5d8b2567fa1)#define BT\_HCI\_ADV\_HANDLE\_INVALID 0xff

[ 49](hci__types_8h.md#a4e4a6e6bb2dc713de8cb7c12139583ed)#define BT\_HCI\_SYNC\_HANDLE\_INVALID 0xffff

[ 50](hci__types_8h.md#a98554ced76600577254b4124b27ef8a8)#define BT\_HCI\_PAWR\_SUBEVENT\_MAX 128

51

52/\* Bluetooth spec v5.4 Vol 4, Part E - 5.4.3 HCI Synchronous Data Packets \*/

[ 53](structbt__hci__sco__hdr.md)struct [bt\_hci\_sco\_hdr](structbt__hci__sco__hdr.md) {

[ 54](structbt__hci__sco__hdr.md#a4b4c915bec966c17567c14e2df9c1581) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__sco__hdr.md#a4b4c915bec966c17567c14e2df9c1581); /\* 12 bit handle, 2 bit Packet Status Flag, 1 bit RFU \*/

[ 55](structbt__hci__sco__hdr.md#a158f67c3743684c28728b62db5cf2590) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structbt__hci__sco__hdr.md#a158f67c3743684c28728b62db5cf2590);

56} \_\_packed;

[ 57](hci__types_8h.md#acb8daef29a7f5f2d11a169fd10ae0caa)#define BT\_HCI\_SCO\_HDR\_SIZE 3

58

59/\* Bluetooth spec v5.4 Vol 4, Part E - 5.4.4 HCI Event Packet \*/

[ 60](structbt__hci__evt__hdr.md)struct [bt\_hci\_evt\_hdr](structbt__hci__evt__hdr.md) {

[ 61](structbt__hci__evt__hdr.md#aba3aca89bfbe7e8cbd144765cb20fcea) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [evt](structbt__hci__evt__hdr.md#aba3aca89bfbe7e8cbd144765cb20fcea);

[ 62](structbt__hci__evt__hdr.md#a2d580a0c12b29d23002ee9d494c9e16d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structbt__hci__evt__hdr.md#a2d580a0c12b29d23002ee9d494c9e16d);

63} \_\_packed;

[ 64](hci__types_8h.md#a0edb7e700cfa557e7fb8ec44f5eea961)#define BT\_HCI\_EVT\_HDR\_SIZE 2

65

[ 66](hci__types_8h.md#ae8c5ddd450d47b45a310bc979207ebff)#define BT\_ACL\_START\_NO\_FLUSH 0x00

[ 67](hci__types_8h.md#a0bfb8a0bac96eb223eb8229c1dff9e7d)#define BT\_ACL\_CONT 0x01

[ 68](hci__types_8h.md#a49c9728293c37e718c009ad973f6d43e)#define BT\_ACL\_START 0x02

[ 69](hci__types_8h.md#ad6f24425a0818730d2377e159698922b)#define BT\_ACL\_COMPLETE 0x03

70

[ 71](hci__types_8h.md#a343e6550f9a24a59c5a08efd2dab16bb)#define BT\_ACL\_POINT\_TO\_POINT 0x00

[ 72](hci__types_8h.md#a2f9e6232229ae1bed3d835b5f6531a76)#define BT\_ACL\_BROADCAST 0x01

73

[ 74](hci__types_8h.md#a28a9f26ba563e2687856aff39b044039)#define BT\_ACL\_HANDLE\_MASK BIT\_MASK(12)

75

[ 76](hci__types_8h.md#a500341d3485843d85dc034ce6f8a908c)#define bt\_acl\_handle(h) ((h) & BT\_ACL\_HANDLE\_MASK)

[ 77](hci__types_8h.md#a499f8647747fd6b7b82d9b3280b4b048)#define bt\_acl\_flags(h) ((h) >> 12)

[ 78](hci__types_8h.md#ae358e74ce455f11bb134700ec80fe07b)#define bt\_acl\_flags\_pb(f) ((f) & BIT\_MASK(2))

[ 79](hci__types_8h.md#a55cfcca3e0a6a7401e57e7430421093e)#define bt\_acl\_flags\_bc(f) ((f) >> 2)

[ 80](hci__types_8h.md#aa08e6239d84ce55153baa41f46814363)#define bt\_acl\_handle\_pack(h, f) ((h) | ((f) << 12))

81

82/\* Bluetooth spec v5.4 Vol 4, Part E - 5.4.2 ACL Data Packets \*/

[ 83](structbt__hci__acl__hdr.md)struct [bt\_hci\_acl\_hdr](structbt__hci__acl__hdr.md) {

[ 84](structbt__hci__acl__hdr.md#a8c88ef62a848699e06c49f97e1169363) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__acl__hdr.md#a8c88ef62a848699e06c49f97e1169363);

[ 85](structbt__hci__acl__hdr.md#af55b9c9256f35ada5786e9e5dd1d01bf) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structbt__hci__acl__hdr.md#af55b9c9256f35ada5786e9e5dd1d01bf);

86} \_\_packed;

[ 87](hci__types_8h.md#a7418d845532d6b077a9695454fa65bc5)#define BT\_HCI\_ACL\_HDR\_SIZE 4

88

[ 89](hci__types_8h.md#a9ef86241b4dfb462ec31c855bce4ee28)#define BT\_ISO\_START 0x00

[ 90](hci__types_8h.md#a06c43e91abee990343ece9c22f5a515e)#define BT\_ISO\_CONT 0x01

[ 91](hci__types_8h.md#a1db9801de1c97b2d15cf9d2f0ec2a5f0)#define BT\_ISO\_SINGLE 0x02

[ 92](hci__types_8h.md#ac2da3db69ba73112fff5bf16ef386cb3)#define BT\_ISO\_END 0x03

93

[ 94](hci__types_8h.md#adcdb9dd367b64a820a040724c1c42c15)#define bt\_iso\_handle(h) ((h) & 0x0fff)

[ 95](hci__types_8h.md#a54e2f7efc0f22287d65bdd560dd7ec78)#define bt\_iso\_flags(h) ((h) >> 12)

[ 96](hci__types_8h.md#a7ea328491745f1bde6e2b376c19cc380)#define bt\_iso\_flags\_pb(f) ((f) & 0x0003)

[ 97](hci__types_8h.md#aed6d45daf19ce7fadc1c8fbcc79c9e8a)#define bt\_iso\_flags\_ts(f) (((f) >> 2) & 0x0001)

[ 98](hci__types_8h.md#a9bdbdc6e181731a58ec91d53cdade532)#define bt\_iso\_pack\_flags(pb, ts) \

99 (((pb) & 0x0003) | (((ts) & 0x0001) << 2))

[ 100](hci__types_8h.md#ab96b2d1b49a86ee96b2254b624b2e93f)#define bt\_iso\_handle\_pack(h, pb, ts) \

101 ((h) | (bt\_iso\_pack\_flags(pb, ts) << 12))

[ 102](hci__types_8h.md#a128d269790ccf3f8dcdeb51f80697ba0)#define bt\_iso\_hdr\_len(h) ((h) & BIT\_MASK(14))

103

[ 104](hci__types_8h.md#a52091a307cca85d8d39fbfe5be6b6179)#define BT\_ISO\_DATA\_VALID 0x00

[ 105](hci__types_8h.md#a7149213544fe2ac9e7d3d0fd64ecb271)#define BT\_ISO\_DATA\_INVALID 0x01

[ 106](hci__types_8h.md#ae736b21ff7b99c4bb85df1a3f4bee9cd)#define BT\_ISO\_DATA\_NOP 0x02

107

[ 108](hci__types_8h.md#a0d540918a423992f5f244febcc82248a)#define bt\_iso\_pkt\_len(h) ((h) & BIT\_MASK(12))

[ 109](hci__types_8h.md#a6dbade5730a92ea7f85017792939e941)#define bt\_iso\_pkt\_flags(h) ((h) >> 14)

[ 110](hci__types_8h.md#a3683be1ceedbcb97f61483b6fa4344e6)#define bt\_iso\_pkt\_len\_pack(h, f) (((h) & BIT\_MASK(12)) | ((f) << 14))

111

[ 112](structbt__hci__iso__sdu__hdr.md)struct [bt\_hci\_iso\_sdu\_hdr](structbt__hci__iso__sdu__hdr.md) {

[ 113](structbt__hci__iso__sdu__hdr.md#a683d493de5d00e3b4c5169f6de498c13) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sn](structbt__hci__iso__sdu__hdr.md#a683d493de5d00e3b4c5169f6de498c13);

[ 114](structbt__hci__iso__sdu__hdr.md#a626764862a3757a3119b6de799221ad1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [slen](structbt__hci__iso__sdu__hdr.md#a626764862a3757a3119b6de799221ad1); /\* 12 bit len, 2 bit RFU, 2 bit packet status \*/

115} \_\_packed;

[ 116](hci__types_8h.md#a94b93cd856353f24afee5e4022cdbdb9)#define BT\_HCI\_ISO\_SDU\_HDR\_SIZE 4

117

[ 118](structbt__hci__iso__sdu__ts__hdr.md)struct [bt\_hci\_iso\_sdu\_ts\_hdr](structbt__hci__iso__sdu__ts__hdr.md) {

[ 119](structbt__hci__iso__sdu__ts__hdr.md#a657e03c5ef597f04cc21725f0bc227d4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ts](structbt__hci__iso__sdu__ts__hdr.md#a657e03c5ef597f04cc21725f0bc227d4);

[ 120](structbt__hci__iso__sdu__ts__hdr.md#a3f81175b95f8eaeeeee71ee4bf401864) struct [bt\_hci\_iso\_sdu\_hdr](structbt__hci__iso__sdu__hdr.md) [sdu](structbt__hci__iso__sdu__ts__hdr.md#a3f81175b95f8eaeeeee71ee4bf401864);

121} \_\_packed;

[ 122](hci__types_8h.md#a22db454317bc89afe092ab9127888441)#define BT\_HCI\_ISO\_SDU\_TS\_HDR\_SIZE 8

123

124/\* Bluetooth spec v5.4 Vol 4, Part E - 5.4.5 HCI ISO Data Packets \*/

[ 125](structbt__hci__iso__hdr.md)struct [bt\_hci\_iso\_hdr](structbt__hci__iso__hdr.md) {

[ 126](structbt__hci__iso__hdr.md#af5113383fbcd0e70828f986720c38572) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__iso__hdr.md#af5113383fbcd0e70828f986720c38572); /\* 12 bit handle, 2 bit PB flags, 1 bit TS\_Flag, 1 bit RFU \*/

[ 127](structbt__hci__iso__hdr.md#ab33ae914a9eba85b35c78e45e0f5255f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structbt__hci__iso__hdr.md#ab33ae914a9eba85b35c78e45e0f5255f); /\* 14 bits, 2 bits RFU \*/

128} \_\_packed;

[ 129](hci__types_8h.md#a75c1f5e8a44b034004ecfebdb75ee4be)#define BT\_HCI\_ISO\_HDR\_SIZE 4

130

131/\* Bluetooth spec v5.4 Vol 4, Part E - 5.4.1 HCI Command Packet \*/

[ 132](structbt__hci__cmd__hdr.md)struct [bt\_hci\_cmd\_hdr](structbt__hci__cmd__hdr.md) {

[ 133](structbt__hci__cmd__hdr.md#a09c63aab094ca0f39bab44708fdb83e4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [opcode](structbt__hci__cmd__hdr.md#a09c63aab094ca0f39bab44708fdb83e4);

[ 134](structbt__hci__cmd__hdr.md#afe2a97da8b473cafd3cc4e5e52dadf93) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [param\_len](structbt__hci__cmd__hdr.md#afe2a97da8b473cafd3cc4e5e52dadf93);

135} \_\_packed;

[ 136](hci__types_8h.md#acdf2b6de1459a7492415a8987ad9a896)#define BT\_HCI\_CMD\_HDR\_SIZE 3

137

138/\* Supported Commands \*/

[ 139](hci__types_8h.md#a7d5bc35e597d03fbc65084b39771cf0b)#define BT\_CMD\_TEST(cmd, octet, bit) (cmd[octet] & BIT(bit))

[ 140](hci__types_8h.md#ae3aaad5ae408cb8c72a29ff7a8817c21)#define BT\_CMD\_LE\_STATES(cmd) BT\_CMD\_TEST(cmd, 28, 3)

141

[ 142](hci__types_8h.md#a41e5b49e645ed511340a61f843f6b238)#define BT\_FEAT\_TEST(feat, page, octet, bit) (feat[page][octet] & BIT(bit))

143

[ 144](hci__types_8h.md#a5508c481ff6b8fd46f2f2c077aaa90c9)#define BT\_FEAT\_BREDR(feat) !BT\_FEAT\_TEST(feat, 0, 4, 5)

[ 145](hci__types_8h.md#a8b1df8d6b9e0dfcaa13635588cc3bfe3)#define BT\_FEAT\_LE(feat) BT\_FEAT\_TEST(feat, 0, 4, 6)

[ 146](hci__types_8h.md#ac26ebac4f1641d5ff4484f74579852d7)#define BT\_FEAT\_EXT\_FEATURES(feat) BT\_FEAT\_TEST(feat, 0, 7, 7)

[ 147](hci__types_8h.md#af011519b6fb0477ac7f87e5dc98daed0)#define BT\_FEAT\_HOST\_SSP(feat) BT\_FEAT\_TEST(feat, 1, 0, 0)

[ 148](hci__types_8h.md#a9ecf892ec94af8cbfd2e6c99310b1fa2)#define BT\_FEAT\_SC(feat) BT\_FEAT\_TEST(feat, 2, 1, 0)

149

[ 150](hci__types_8h.md#a24f24640d9f52adb15336a1b17122346)#define BT\_FEAT\_LMP\_SCO\_CAPABLE(feat) BT\_FEAT\_TEST(feat, 0, 1, 3)

[ 151](hci__types_8h.md#a7622a2fc0a65f82a827ab3cc84e4e7c5)#define BT\_FEAT\_LMP\_ESCO\_CAPABLE(feat) BT\_FEAT\_TEST(feat, 0, 3, 7)

[ 152](hci__types_8h.md#ad59c138e945d7f27d3befc286b679e03)#define BT\_FEAT\_HV2\_PKT(feat) BT\_FEAT\_TEST(feat, 0, 1, 4)

[ 153](hci__types_8h.md#aed6f11d60161c919b4d2b7eb13f46e47)#define BT\_FEAT\_HV3\_PKT(feat) BT\_FEAT\_TEST(feat, 0, 1, 5)

[ 154](hci__types_8h.md#ad154d0649e8e90c1102b74cae8327fa7)#define BT\_FEAT\_EV4\_PKT(feat) BT\_FEAT\_TEST(feat, 0, 4, 0)

[ 155](hci__types_8h.md#a0a6b9afb4673dc852e1a4d8e867003c9)#define BT\_FEAT\_EV5\_PKT(feat) BT\_FEAT\_TEST(feat, 0, 4, 1)

[ 156](hci__types_8h.md#a8dbbf37965a9d0ddab5a07f88d7cd7ca)#define BT\_FEAT\_2EV3\_PKT(feat) BT\_FEAT\_TEST(feat, 0, 5, 5)

[ 157](hci__types_8h.md#a00aec89aa4d1504934e85ec79462b346)#define BT\_FEAT\_3EV3\_PKT(feat) BT\_FEAT\_TEST(feat, 0, 5, 6)

[ 158](hci__types_8h.md#a5219ff658b46cf28104a99f089854444)#define BT\_FEAT\_3SLOT\_PKT(feat) BT\_FEAT\_TEST(feat, 0, 5, 7)

159

160/\* LE features \*/

[ 161](hci__types_8h.md#abd616dd5af5ed3742be9bae400ded848)#define BT\_LE\_FEAT\_BIT\_ENC 0

[ 162](hci__types_8h.md#ab816048bdd6c1e42b0e458abebb76572)#define BT\_LE\_FEAT\_BIT\_CONN\_PARAM\_REQ 1

[ 163](hci__types_8h.md#ae5644021aff31996c09f6edf3ede197c)#define BT\_LE\_FEAT\_BIT\_EXT\_REJ\_IND 2

[ 164](hci__types_8h.md#aeaea6ea6595de9e3283fd6063bf7c579)#define BT\_LE\_FEAT\_BIT\_PER\_INIT\_FEAT\_XCHG 3

[ 165](hci__types_8h.md#a9b4dc56ef4433b0c0dc74a3d95cf289e)#define BT\_LE\_FEAT\_BIT\_PING 4

[ 166](hci__types_8h.md#ac09127210b281e5ee45fbc134df64aa6)#define BT\_LE\_FEAT\_BIT\_DLE 5

[ 167](hci__types_8h.md#a3c4196c04a73aa537baa845e061e9654)#define BT\_LE\_FEAT\_BIT\_PRIVACY 6

[ 168](hci__types_8h.md#a8f1fa8948f79bec50373e0342ab0969a)#define BT\_LE\_FEAT\_BIT\_EXT\_SCAN 7

[ 169](hci__types_8h.md#afcbc8d664c8e924b777c06ffb4c17315)#define BT\_LE\_FEAT\_BIT\_PHY\_2M 8

[ 170](hci__types_8h.md#aea19f3c3cdcec054c81c176d5aa5f319)#define BT\_LE\_FEAT\_BIT\_SMI\_TX 9

[ 171](hci__types_8h.md#a9430a65ea813861b6890252ed4748f19)#define BT\_LE\_FEAT\_BIT\_SMI\_RX 10

[ 172](hci__types_8h.md#a800686aa45cf336fbd6efc76b3752959)#define BT\_LE\_FEAT\_BIT\_PHY\_CODED 11

[ 173](hci__types_8h.md#ae1a0751e7c380117c4e31741712096a4)#define BT\_LE\_FEAT\_BIT\_EXT\_ADV 12

[ 174](hci__types_8h.md#a1ac5bab6d48775b4e63e249b5759a683)#define BT\_LE\_FEAT\_BIT\_PER\_ADV 13

[ 175](hci__types_8h.md#a9120867d6f31465cb5f085b610d5ed70)#define BT\_LE\_FEAT\_BIT\_CHAN\_SEL\_ALGO\_2 14

[ 176](hci__types_8h.md#a938f823110f31a3a5d034cbe9b9d26eb)#define BT\_LE\_FEAT\_BIT\_PWR\_CLASS\_1 15

[ 177](hci__types_8h.md#ac8cf36c670ae359ec24e62efb4505758)#define BT\_LE\_FEAT\_BIT\_MIN\_USED\_CHAN\_PROC 16

[ 178](hci__types_8h.md#aed34742e8554b830c3b6c4bf04f0e2db)#define BT\_LE\_FEAT\_BIT\_CONN\_CTE\_REQ 17

[ 179](hci__types_8h.md#aa5279a2ce26decb5856a6b709d0641c9)#define BT\_LE\_FEAT\_BIT\_CONN\_CTE\_RESP 18

[ 180](hci__types_8h.md#a331e7697a3fdc073abba5dd0ff47346b)#define BT\_LE\_FEAT\_BIT\_CONNECTIONLESS\_CTE\_TX 19

[ 181](hci__types_8h.md#a6abf01c846a5d637ca98997f6cfc263d)#define BT\_LE\_FEAT\_BIT\_CONNECTIONLESS\_CTE\_RX 20

[ 182](hci__types_8h.md#a41eae1585972ae6792eb1a639c2e3a8e)#define BT\_LE\_FEAT\_BIT\_ANT\_SWITCH\_TX\_AOD 21

[ 183](hci__types_8h.md#a480fc67a1c8a2f36410f285ef0ee36e7)#define BT\_LE\_FEAT\_BIT\_ANT\_SWITCH\_RX\_AOA 22

[ 184](hci__types_8h.md#a9d9449f1935d6522291eca581f3fa9b0)#define BT\_LE\_FEAT\_BIT\_RX\_CTE 23

[ 185](hci__types_8h.md#aa05da01a6a9b9ac26423d6fc2661f3db)#define BT\_LE\_FEAT\_BIT\_PAST\_SEND 24

[ 186](hci__types_8h.md#a28a862eaf11f8b45237f3b87e4bb15c7)#define BT\_LE\_FEAT\_BIT\_PAST\_RECV 25

[ 187](hci__types_8h.md#a829e9d23a16912bad19448a6c4061e3b)#define BT\_LE\_FEAT\_BIT\_SCA\_UPDATE 26

[ 188](hci__types_8h.md#a6d17dd4238ea471daca22f74e3cc3bcb)#define BT\_LE\_FEAT\_BIT\_REMOTE\_PUB\_KEY\_VALIDATE 27

[ 189](hci__types_8h.md#aa98eed376b6d5263621f14c55d776088)#define BT\_LE\_FEAT\_BIT\_CIS\_CENTRAL 28

[ 190](hci__types_8h.md#a298fde96c2d6376e3333a99f7e03409d)#define BT\_LE\_FEAT\_BIT\_CIS\_PERIPHERAL 29

[ 191](hci__types_8h.md#af08a1ffd734d1c211f38d90b4fe72417)#define BT\_LE\_FEAT\_BIT\_ISO\_BROADCASTER 30

[ 192](hci__types_8h.md#a2fed771f5611212e48027025e11f7678)#define BT\_LE\_FEAT\_BIT\_SYNC\_RECEIVER 31

[ 193](hci__types_8h.md#a0d80ccb33d263abd3b42de1b69cfeeeb)#define BT\_LE\_FEAT\_BIT\_ISO\_CHANNELS 32

[ 194](hci__types_8h.md#ae58f5260530d1b94608874f5d03d766d)#define BT\_LE\_FEAT\_BIT\_PWR\_CTRL\_REQ 33

[ 195](hci__types_8h.md#a0138172a0ed78244d8d3ac9d6936cf85)#define BT\_LE\_FEAT\_BIT\_PWR\_CHG\_IND 34

[ 196](hci__types_8h.md#a434fb43b6b3176393f5d22d3932d69fa)#define BT\_LE\_FEAT\_BIT\_PATH\_LOSS\_MONITOR 35

[ 197](hci__types_8h.md#ad5a8221cb25d79b63f1a574699983038)#define BT\_LE\_FEAT\_BIT\_PER\_ADV\_ADI\_SUPP 36

[ 198](hci__types_8h.md#aa45b06a49232372891ceb5e4496d46da)#define BT\_LE\_FEAT\_BIT\_CONN\_SUBRATING 37

[ 199](hci__types_8h.md#adb884a30bc1a24e3dfb115cef7149c81)#define BT\_LE\_FEAT\_BIT\_CONN\_SUBRATING\_HOST\_SUPP 38

[ 200](hci__types_8h.md#af2a4be520b4d8c3eb56231b865738e90)#define BT\_LE\_FEAT\_BIT\_CHANNEL\_CLASSIFICATION 39

[ 201](hci__types_8h.md#a4d920d42e8042c9117f97e334f889f51)#define BT\_LE\_FEAT\_BIT\_ADV\_CODING\_SEL 40

[ 202](hci__types_8h.md#ad711e7491883e1f1e068fe167cca8a4e)#define BT\_LE\_FEAT\_BIT\_ADV\_CODING\_SEL\_HOST 41

203

[ 204](hci__types_8h.md#af251cb9d905586fd53113f5920038dae)#define BT\_LE\_FEAT\_BIT\_PAWR\_ADVERTISER 43

[ 205](hci__types_8h.md#a00bb51972e0db07be84d4f3dfd007cea)#define BT\_LE\_FEAT\_BIT\_PAWR\_SCANNER 44

206

[ 207](hci__types_8h.md#ab918084874aace22954aa748333baf6d)#define BT\_LE\_FEAT\_BIT\_CHANNEL\_SOUNDING 46

[ 208](hci__types_8h.md#aa4572a11d78651ce775a010178c6dfa2)#define BT\_LE\_FEAT\_BIT\_CHANNEL\_SOUNDING\_HOST 47

209

[ 210](hci__types_8h.md#a6bf20989952fed3726bc45873beb896e)#define BT\_LE\_FEAT\_TEST(feat, n) (feat[(n) >> 3] & \

211 BIT((n) & 7))

212

[ 213](hci__types_8h.md#a51464aacf5bbcbfb873fa6c757bbcd79)#define BT\_FEAT\_LE\_ENCR(feat) BT\_LE\_FEAT\_TEST(feat, \

214 BT\_LE\_FEAT\_BIT\_ENC)

[ 215](hci__types_8h.md#a554c027fb3946de6f861ea267968ba17)#define BT\_FEAT\_LE\_CONN\_PARAM\_REQ\_PROC(feat) BT\_LE\_FEAT\_TEST(feat, \

216 BT\_LE\_FEAT\_BIT\_CONN\_PARAM\_REQ)

[ 217](hci__types_8h.md#a132b2561dcd4140458fb612b6e0d8b25)#define BT\_FEAT\_LE\_PER\_INIT\_FEAT\_XCHG(feat) BT\_LE\_FEAT\_TEST(feat, \

218 BT\_LE\_FEAT\_BIT\_PER\_INIT\_FEAT\_XCHG)

[ 219](hci__types_8h.md#a62e7d152cd9dfabf5b1420945099ecb6)#define BT\_FEAT\_LE\_DLE(feat) BT\_LE\_FEAT\_TEST(feat, \

220 BT\_LE\_FEAT\_BIT\_DLE)

[ 221](hci__types_8h.md#aaf11993f4938bb4894cdd317f9386fa3)#define BT\_FEAT\_LE\_PHY\_2M(feat) BT\_LE\_FEAT\_TEST(feat, \

222 BT\_LE\_FEAT\_BIT\_PHY\_2M)

[ 223](hci__types_8h.md#abb89a0bebe4046ae310b01dd27e02c99)#define BT\_FEAT\_LE\_PHY\_CODED(feat) BT\_LE\_FEAT\_TEST(feat, \

224 BT\_LE\_FEAT\_BIT\_PHY\_CODED)

[ 225](hci__types_8h.md#a0b2781f29085a5807d0b2235c32f5173)#define BT\_FEAT\_LE\_PRIVACY(feat) BT\_LE\_FEAT\_TEST(feat, \

226 BT\_LE\_FEAT\_BIT\_PRIVACY)

[ 227](hci__types_8h.md#a8bce94a732d28ce74ad2663e01da09b2)#define BT\_FEAT\_LE\_EXT\_ADV(feat) BT\_LE\_FEAT\_TEST(feat, \

228 BT\_LE\_FEAT\_BIT\_EXT\_ADV)

[ 229](hci__types_8h.md#a5d479d919db4920b7a53c054e4ae7a19)#define BT\_FEAT\_LE\_EXT\_PER\_ADV(feat) BT\_LE\_FEAT\_TEST(feat, \

230 BT\_LE\_FEAT\_BIT\_PER\_ADV)

[ 231](hci__types_8h.md#a51316a5b67950e7644dfb71c4c6baa96)#define BT\_FEAT\_LE\_CONNECTION\_CTE\_REQ(feat) BT\_LE\_FEAT\_TEST(feat, \

232 BT\_LE\_FEAT\_BIT\_CONN\_CTE\_REQ)

[ 233](hci__types_8h.md#a0cdc67a1345969d3504380fce94a4cda)#define BT\_FEAT\_LE\_CONNECTION\_CTE\_RESP(feat) BT\_LE\_FEAT\_TEST(feat, \

234 BT\_LE\_FEAT\_BIT\_CONN\_CTE\_RESP)

[ 235](hci__types_8h.md#a81e30f5630750ce4f805748fbe14b456)#define BT\_FEAT\_LE\_CONNECTIONLESS\_CTE\_TX(feat) BT\_LE\_FEAT\_TEST(feat, \

236 BT\_LE\_FEAT\_BIT\_CONNECTIONLESS\_CTE\_TX)

[ 237](hci__types_8h.md#aeb0639a8e5cbc904d7f5c02d72375913)#define BT\_FEAT\_LE\_CONNECTIONLESS\_CTE\_RX(feat) BT\_LE\_FEAT\_TEST(feat, \

238 BT\_LE\_FEAT\_BIT\_CONNECTIONLESS\_CTE\_RX)

[ 239](hci__types_8h.md#ae503f9186d39fbea2347036c891fc8bf)#define BT\_FEAT\_LE\_ANT\_SWITCH\_TX\_AOD(feat) BT\_LE\_FEAT\_TEST(feat, \

240 BT\_LE\_FEAT\_BIT\_ANT\_SWITCH\_TX\_AOD)

[ 241](hci__types_8h.md#a1c3c0e6a213b71e680ca24738047f09a)#define BT\_FEAT\_LE\_ANT\_SWITCH\_RX\_AOA(feat) BT\_LE\_FEAT\_TEST(feat, \

242 BT\_LE\_FEAT\_BIT\_ANT\_SWITCH\_RX\_AOA)

[ 243](hci__types_8h.md#adf4303d47abfab3bd23080c545b77ef7)#define BT\_FEAT\_LE\_RX\_CTE(feat) BT\_LE\_FEAT\_TEST(feat, \

244 BT\_LE\_FEAT\_BIT\_RX\_CTE)

[ 245](hci__types_8h.md#a9e68dcf290273a4a140645c187cd7aee)#define BT\_FEAT\_LE\_PAST\_SEND(feat) BT\_LE\_FEAT\_TEST(feat, \

246 BT\_LE\_FEAT\_BIT\_PAST\_SEND)

[ 247](hci__types_8h.md#a7a88046c26b3603a2bb8b0f2ee158b5f)#define BT\_FEAT\_LE\_PAST\_RECV(feat) BT\_LE\_FEAT\_TEST(feat, \

248 BT\_LE\_FEAT\_BIT\_PAST\_RECV)

[ 249](hci__types_8h.md#adce7c3804a224e7b7317728fa27d4945)#define BT\_FEAT\_LE\_CIS\_CENTRAL(feat) BT\_LE\_FEAT\_TEST(feat, \

250 BT\_LE\_FEAT\_BIT\_CIS\_CENTRAL)

[ 251](hci__types_8h.md#a8a6860b285b3b4401021ba16f59404ce)#define BT\_FEAT\_LE\_CIS\_PERIPHERAL(feat) BT\_LE\_FEAT\_TEST(feat, \

252 BT\_LE\_FEAT\_BIT\_CIS\_PERIPHERAL)

[ 253](hci__types_8h.md#a1c6fd06877a5606ae33aedc45a71f853)#define BT\_FEAT\_LE\_ISO\_BROADCASTER(feat) BT\_LE\_FEAT\_TEST(feat, \

254 BT\_LE\_FEAT\_BIT\_ISO\_BROADCASTER)

[ 255](hci__types_8h.md#af33c8331e204eeee2a7a02e2ad46c7a2)#define BT\_FEAT\_LE\_SYNC\_RECEIVER(feat) BT\_LE\_FEAT\_TEST(feat, \

256 BT\_LE\_FEAT\_BIT\_SYNC\_RECEIVER)

[ 257](hci__types_8h.md#a0b24b74715fbf84c2da2dd2cbbb34605)#define BT\_FEAT\_LE\_ISO\_CHANNELS(feat) BT\_LE\_FEAT\_TEST(feat, \

258 BT\_LE\_FEAT\_BIT\_ISO\_CHANNELS)

[ 259](hci__types_8h.md#a8ab0d3ca572861bb1c40191766481799)#define BT\_FEAT\_LE\_PWR\_CTRL\_REQ(feat) BT\_LE\_FEAT\_TEST(feat, \

260 BT\_LE\_FEAT\_BIT\_PWR\_CTRL\_REQ)

[ 261](hci__types_8h.md#a342ce6074faa59b507cf179868e612ba)#define BT\_FEAT\_LE\_PWR\_CHG\_IND(feat) BT\_LE\_FEAT\_TEST(feat, \

262 BT\_LE\_FEAT\_BIT\_PWR\_CHG\_IND)

[ 263](hci__types_8h.md#a8d771bd34d22853f117dbbd41ef4afe5)#define BT\_FEAT\_LE\_PATH\_LOSS\_MONITOR(feat) BT\_LE\_FEAT\_TEST(feat, \

264 BT\_LE\_FEAT\_BIT\_PATH\_LOSS\_MONITOR)

[ 265](hci__types_8h.md#a6213deacc8582f14546b23331d41c3a3)#define BT\_FEAT\_LE\_PER\_ADV\_ADI\_SUPP(feat) BT\_LE\_FEAT\_TEST(feat, \

266 BT\_LE\_FEAT\_BIT\_PER\_ADV\_ADI\_SUPP)

[ 267](hci__types_8h.md#a75bf595ba1e16deeeedb45a55f470620)#define BT\_FEAT\_LE\_CONN\_SUBRATING(feat) BT\_LE\_FEAT\_TEST(feat, \

268 BT\_LE\_FEAT\_BIT\_CONN\_SUBRATING)

[ 269](hci__types_8h.md#a37adeecbf4c200cf8b060344718e7949)#define BT\_FEAT\_LE\_CONN\_SUBRATING\_HOST\_SUPP(feat) BT\_LE\_FEAT\_TEST(feat, \

270 BT\_LE\_FEAT\_BIT\_CONN\_SUBRATING\_HOST\_SUPP)

[ 271](hci__types_8h.md#abb7763cc16340d23bc7d687e60badcc0)#define BT\_FEAT\_LE\_CHANNEL\_CLASSIFICATION(feat) BT\_LE\_FEAT\_TEST(feat, \

272 BT\_LE\_FEAT\_BIT\_CHANNEL\_CLASSIFICATION)

[ 273](hci__types_8h.md#af10735230c38d2b5a0baf5377212e827)#define BT\_FEAT\_LE\_ADV\_CODING\_SEL(feat) BT\_LE\_FEAT\_TEST(feat, \

274 BT\_LE\_FEAT\_BIT\_ADV\_CODING\_SEL)

[ 275](hci__types_8h.md#aecf06a32c61c783305ad3817f9e5a596)#define BT\_FEAT\_LE\_ADV\_CODING\_SEL\_HOST(feat) BT\_LE\_FEAT\_TEST(feat, \

276 BT\_LE\_FEAT\_BIT\_ADV\_CODING\_SEL\_HOST)

[ 277](hci__types_8h.md#ac5d15de2be03bc837afdb33905ea40be)#define BT\_FEAT\_LE\_PAWR\_ADVERTISER(feat) BT\_LE\_FEAT\_TEST(feat, \

278 BT\_LE\_FEAT\_BIT\_PAWR\_ADVERTISER)

[ 279](hci__types_8h.md#a3ee6277e0e4db5e925912e8cb89269fa)#define BT\_FEAT\_LE\_PAWR\_SCANNER(feat) BT\_LE\_FEAT\_TEST(feat, \

280 BT\_LE\_FEAT\_BIT\_PAWR\_SCANNER)

[ 281](hci__types_8h.md#a7b13b55fd2cfb4d756d3591215b47b7e)#define BT\_FEAT\_LE\_CHANNEL\_SOUNDING(feat) BT\_LE\_FEAT\_TEST(feat, \

282 BT\_LE\_FEAT\_BIT\_CHANNEL\_SOUNDING)

[ 283](hci__types_8h.md#aff2b8ca285698906deecfeff7447a74a)#define BT\_FEAT\_LE\_CHANNEL\_SOUNDING\_HOST(feat) BT\_LE\_FEAT\_TEST(feat, \

284 BT\_LE\_FEAT\_BIT\_CHANNEL\_SOUNDING\_HOST)

285

[ 286](hci__types_8h.md#abe5a1ddbede473f583106e3500dccdb1)#define BT\_FEAT\_LE\_CIS(feat) (BT\_FEAT\_LE\_CIS\_CENTRAL(feat) | \

287 BT\_FEAT\_LE\_CIS\_PERIPHERAL(feat))

[ 288](hci__types_8h.md#a46b2f535c74178c8cc9359a7b1d2e140)#define BT\_FEAT\_LE\_BIS(feat) (BT\_FEAT\_LE\_ISO\_BROADCASTER(feat) | \

289 BT\_FEAT\_LE\_SYNC\_RECEIVER(feat))

[ 290](hci__types_8h.md#a7b1b490bf00af8b0bf8ecbf4ef4aaba3)#define BT\_FEAT\_LE\_ISO(feat) (BT\_FEAT\_LE\_CIS(feat) | \

291 BT\_FEAT\_LE\_BIS(feat))

292

293/\* LE States. See Core\_v5.4, Vol 4, Part E, Section 7.8.27 \*/

[ 294](hci__types_8h.md#abff5a0c6d1f3ab8ecf297d4ef29f7940)#define BT\_LE\_STATES\_PER\_CONN\_ADV(states) (states & BIT64\_MASK(38))

295

296#if defined(CONFIG\_BT\_SCAN\_AND\_INITIATE\_IN\_PARALLEL)

297/\* Both passive and active scanner can be run in parallel with initiator. \*/

298#define BT\_LE\_STATES\_SCAN\_INIT(states) ((states) & BIT64\_MASK(22) && \

299 (states) & BIT64\_MASK(23))

300

301#else

[ 302](hci__types_8h.md#a9871a7d021f9e0bcfda278c82c3731d7)#define BT\_LE\_STATES\_SCAN\_INIT(states) 0

303#endif

304

305/\* Bonding/authentication types \*/

[ 306](hci__types_8h.md#ac886a10eed1313f6114fcfc3810a34f0)#define BT\_HCI\_NO\_BONDING 0x00

[ 307](hci__types_8h.md#a89c6d0d285c1c99c51c96d282fe593b9)#define BT\_HCI\_NO\_BONDING\_MITM 0x01

[ 308](hci__types_8h.md#aae1149095ff44d1b749e8b4b4d4aa32f)#define BT\_HCI\_DEDICATED\_BONDING 0x02

[ 309](hci__types_8h.md#aa1361f09852be86296cf91896d8f0853)#define BT\_HCI\_DEDICATED\_BONDING\_MITM 0x03

[ 310](hci__types_8h.md#ad777455cbcdfe02dd297dee5510e63b4)#define BT\_HCI\_GENERAL\_BONDING 0x04

[ 311](hci__types_8h.md#a5b30ffdf3753d0a2a6c8ab025d32acef)#define BT\_HCI\_GENERAL\_BONDING\_MITM 0x05

312

313/\*

314 \* MITM protection is enabled in SSP authentication requirements octet when

315 \* LSB bit is set.

316 \*/

[ 317](hci__types_8h.md#a47ba0b282416c3e8f4275a38b7780b59)#define BT\_MITM 0x01

318

319/\* I/O capabilities \*/

[ 320](hci__types_8h.md#ac656a702e4193044a59cac517099e2cf)#define BT\_IO\_DISPLAY\_ONLY 0x00

[ 321](hci__types_8h.md#a701d4fa8a4ebc07647f70264ad36153e)#define BT\_IO\_DISPLAY\_YESNO 0x01

[ 322](hci__types_8h.md#a5a2a51ccedf3041c42ecdbd69e8c4a68)#define BT\_IO\_KEYBOARD\_ONLY 0x02

[ 323](hci__types_8h.md#ad68c0057160d5dacae12fce949fdaa32)#define BT\_IO\_NO\_INPUT\_OUTPUT 0x03

324

325/\* SCO packet types \*/

[ 326](hci__types_8h.md#aecb5b3886467c41baf979d01d8bde4a1)#define HCI\_PKT\_TYPE\_HV1 0x0020

[ 327](hci__types_8h.md#ae68633ce74639ec6f06d5ef4feee2d09)#define HCI\_PKT\_TYPE\_HV2 0x0040

[ 328](hci__types_8h.md#aecd04ca27f536a1cb15aacf9ee80aba8)#define HCI\_PKT\_TYPE\_HV3 0x0080

329

330/\* eSCO packet types \*/

[ 331](hci__types_8h.md#a4b048addd84409867177a97c785c4a73)#define HCI\_PKT\_TYPE\_SCO\_HV1 0x0001

[ 332](hci__types_8h.md#a98f8217b27c0b9b7817c86520da45018)#define HCI\_PKT\_TYPE\_SCO\_HV2 0x0002

[ 333](hci__types_8h.md#af67cdc23b6542e6d8323f14e17c7171d)#define HCI\_PKT\_TYPE\_SCO\_HV3 0x0004

[ 334](hci__types_8h.md#a9530e916a0cf905e2185cd021320bfff)#define HCI\_PKT\_TYPE\_ESCO\_EV3 0x0008

[ 335](hci__types_8h.md#a3e0b6a1aa3818cb0c36f7883fd361c7e)#define HCI\_PKT\_TYPE\_ESCO\_EV4 0x0010

[ 336](hci__types_8h.md#a1f7474cb16a495bd81dc1f23d4103f70)#define HCI\_PKT\_TYPE\_ESCO\_EV5 0x0020

[ 337](hci__types_8h.md#a1ccc4d6e5cfc560b7e2cb80c4c386607)#define HCI\_PKT\_TYPE\_ESCO\_2EV3 0x0040

[ 338](hci__types_8h.md#ac5f09e3db1bc4d697ff705802e9ec3a0)#define HCI\_PKT\_TYPE\_ESCO\_3EV3 0x0080

[ 339](hci__types_8h.md#a1252be2692bcfb7a1256c63c4deed15d)#define HCI\_PKT\_TYPE\_ESCO\_2EV5 0x0100

[ 340](hci__types_8h.md#aa45e51b1be89505fe599bc7983fcb950)#define HCI\_PKT\_TYPE\_ESCO\_3EV5 0x0200

341

342

[ 343](hci__types_8h.md#a8afe2c798b2d9657778f0815e3cb11c8)#define ESCO\_PKT\_MASK (HCI\_PKT\_TYPE\_SCO\_HV1 | \

344 HCI\_PKT\_TYPE\_SCO\_HV2 | \

345 HCI\_PKT\_TYPE\_SCO\_HV3 | \

346 HCI\_PKT\_TYPE\_ESCO\_EV3 | \

347 HCI\_PKT\_TYPE\_ESCO\_EV4 | \

348 HCI\_PKT\_TYPE\_ESCO\_EV5)

[ 349](hci__types_8h.md#a1ef7929257a087f340f1f421cd8f51ce)#define SCO\_PKT\_MASK (HCI\_PKT\_TYPE\_SCO\_HV1 | \

350 HCI\_PKT\_TYPE\_SCO\_HV2 | \

351 HCI\_PKT\_TYPE\_SCO\_HV3)

[ 352](hci__types_8h.md#aa3a50b43beddbd76ae67b71e79a80175)#define EDR\_ESCO\_PKT\_MASK (HCI\_PKT\_TYPE\_ESCO\_2EV3 | \

353 HCI\_PKT\_TYPE\_ESCO\_3EV3 | \

354 HCI\_PKT\_TYPE\_ESCO\_2EV5 | \

355 HCI\_PKT\_TYPE\_ESCO\_3EV5)

356

357/\* HCI BR/EDR link types \*/

[ 358](hci__types_8h.md#a5e79467b20a9173726c6be86b091e596)#define BT\_HCI\_SCO 0x00

[ 359](hci__types_8h.md#afee2289cd70b50f888518fd0b6b3f559)#define BT\_HCI\_ACL 0x01

[ 360](hci__types_8h.md#a4c57b051b336788e503a8521bb5ada80)#define BT\_HCI\_ESCO 0x02

361

362/\* OpCode Group Fields \*/

[ 363](hci__types_8h.md#abb6c50fe170ffaaaf4a0827058331381)#define BT\_OGF\_LINK\_CTRL 0x01

[ 364](hci__types_8h.md#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)#define BT\_OGF\_BASEBAND 0x03

[ 365](hci__types_8h.md#ac7c7348e291360169bf0ca5bb57b3d7e)#define BT\_OGF\_INFO 0x04

[ 366](hci__types_8h.md#a5ce14b9103bd538f3610afd80284157e)#define BT\_OGF\_STATUS 0x05

[ 367](hci__types_8h.md#abb09db6a211185842f039eddb9fadca5)#define BT\_OGF\_LE 0x08

[ 368](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65)#define BT\_OGF\_VS 0x3f

369

370/\* Construct OpCode from OGF and OCF \*/

[ 371](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)#define BT\_OP(ogf, ocf) ((ocf) | ((ogf) << 10))

372

373/\* Invalid opcode \*/

[ 374](hci__types_8h.md#a1bf4881fa3237f4a5b22e5fdb417762b)#define BT\_OP\_NOP 0x0000

375

376/\* Obtain OGF from OpCode \*/

[ 377](hci__types_8h.md#af3ae81176a4ace13a562262ad53aeae6)#define BT\_OGF(opcode) (((opcode) >> 10) & BIT\_MASK(6))

378/\* Obtain OCF from OpCode \*/

[ 379](hci__types_8h.md#ac267cc5384724efba92df0be57379a89)#define BT\_OCF(opcode) ((opcode) & BIT\_MASK(10))

380

[ 381](hci__types_8h.md#adce48ff5cdde5f4f8ab5bc960717581a)#define BT\_HCI\_OP\_INQUIRY BT\_OP(BT\_OGF\_LINK\_CTRL, 0x0001) /\* 0x0401 \*/

[ 382](structbt__hci__op__inquiry.md)struct [bt\_hci\_op\_inquiry](structbt__hci__op__inquiry.md) {

[ 383](structbt__hci__op__inquiry.md#abdd03feccecbdbbb5d2c7c7f3213b62f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [lap](structbt__hci__op__inquiry.md#abdd03feccecbdbbb5d2c7c7f3213b62f)[3];

[ 384](structbt__hci__op__inquiry.md#ae77fa706c9875b5568a4af26a7724d08) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [length](structbt__hci__op__inquiry.md#ae77fa706c9875b5568a4af26a7724d08);

[ 385](structbt__hci__op__inquiry.md#ac8ed23243dbd9a7c46fedd8abe9666f5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_rsp](structbt__hci__op__inquiry.md#ac8ed23243dbd9a7c46fedd8abe9666f5);

386} \_\_packed;

387

[ 388](hci__types_8h.md#ae2d4e5e9cbf056bff03a668e74523442)#define BT\_HCI\_OP\_INQUIRY\_CANCEL BT\_OP(BT\_OGF\_LINK\_CTRL, 0x0002) /\* 0x0402 \*/

389

[ 390](hci__types_8h.md#addfd3dec2a69e7e5e2634c4fe63769f2)#define BT\_HCI\_OP\_CONNECT BT\_OP(BT\_OGF\_LINK\_CTRL, 0x0005) /\* 0x0405 \*/

[ 391](structbt__hci__cp__connect.md)struct [bt\_hci\_cp\_connect](structbt__hci__cp__connect.md) {

[ 392](structbt__hci__cp__connect.md#a6f0753aad19d4c9591fa74152d151aa9) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__connect.md#a6f0753aad19d4c9591fa74152d151aa9);

[ 393](structbt__hci__cp__connect.md#a652a4e01641893a8588110dc505ceea0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [packet\_type](structbt__hci__cp__connect.md#a652a4e01641893a8588110dc505ceea0);

[ 394](structbt__hci__cp__connect.md#a35b0e1f73f696aae2ca519e16d7bb668) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pscan\_rep\_mode](structbt__hci__cp__connect.md#a35b0e1f73f696aae2ca519e16d7bb668);

[ 395](structbt__hci__cp__connect.md#aef01fcac1b9792353bd8095e6911d6c3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reserved](structbt__hci__cp__connect.md#aef01fcac1b9792353bd8095e6911d6c3);

[ 396](structbt__hci__cp__connect.md#ac379ec381ad4cf6760750203924e5dda) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [clock\_offset](structbt__hci__cp__connect.md#ac379ec381ad4cf6760750203924e5dda);

[ 397](structbt__hci__cp__connect.md#a7a3d772bfd4c83236f9f1ad657e33f17) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [allow\_role\_switch](structbt__hci__cp__connect.md#a7a3d772bfd4c83236f9f1ad657e33f17);

398} \_\_packed;

399

[ 400](hci__types_8h.md#ab3d8612855550e52a0887e231371fbc2)#define BT\_HCI\_OP\_DISCONNECT BT\_OP(BT\_OGF\_LINK\_CTRL, 0x0006) /\* 0x0406 \*/

[ 401](structbt__hci__cp__disconnect.md)struct [bt\_hci\_cp\_disconnect](structbt__hci__cp__disconnect.md) {

[ 402](structbt__hci__cp__disconnect.md#a9cb5bcd135082c37a19cce57ffa123ff) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__disconnect.md#a9cb5bcd135082c37a19cce57ffa123ff);

[ 403](structbt__hci__cp__disconnect.md#a8e10edb1e700c1ef38f39bf20b9b374f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reason](structbt__hci__cp__disconnect.md#a8e10edb1e700c1ef38f39bf20b9b374f);

404} \_\_packed;

405

[ 406](hci__types_8h.md#ac50eb14115129bcc8c47016a6479149d)#define BT\_HCI\_OP\_CONNECT\_CANCEL BT\_OP(BT\_OGF\_LINK\_CTRL, 0x0008) /\* 0x0408 \*/

[ 407](structbt__hci__cp__connect__cancel.md)struct [bt\_hci\_cp\_connect\_cancel](structbt__hci__cp__connect__cancel.md) {

[ 408](structbt__hci__cp__connect__cancel.md#a2adaf1b708689525e44e9a9572f5f357) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__connect__cancel.md#a2adaf1b708689525e44e9a9572f5f357);

409} \_\_packed;

[ 410](structbt__hci__rp__connect__cancel.md)struct [bt\_hci\_rp\_connect\_cancel](structbt__hci__rp__connect__cancel.md) {

[ 411](structbt__hci__rp__connect__cancel.md#a05d0c9e4163bc62a57dba8618294eb65) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__connect__cancel.md#a05d0c9e4163bc62a57dba8618294eb65);

[ 412](structbt__hci__rp__connect__cancel.md#a0ccfcbd294aa067879ab8d7a41bc41c9) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__rp__connect__cancel.md#a0ccfcbd294aa067879ab8d7a41bc41c9);

413} \_\_packed;

414

[ 415](hci__types_8h.md#af45bed44788b16be1b172c56c33eea34)#define BT\_HCI\_OP\_ACCEPT\_CONN\_REQ BT\_OP(BT\_OGF\_LINK\_CTRL, 0x0009) /\* 0x0409 \*/

[ 416](structbt__hci__cp__accept__conn__req.md)struct [bt\_hci\_cp\_accept\_conn\_req](structbt__hci__cp__accept__conn__req.md) {

[ 417](structbt__hci__cp__accept__conn__req.md#aa2954d98fdd42882cf7095e4ce7a3dc5) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__accept__conn__req.md#aa2954d98fdd42882cf7095e4ce7a3dc5);

[ 418](structbt__hci__cp__accept__conn__req.md#a95e445018d1b9da5a914f0845bb9dbad) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [role](structbt__hci__cp__accept__conn__req.md#a95e445018d1b9da5a914f0845bb9dbad);

419} \_\_packed;

420

[ 421](hci__types_8h.md#ac4e12b8f7b89a658da7bbbaf371358e0)#define BT\_HCI\_OP\_SETUP\_SYNC\_CONN BT\_OP(BT\_OGF\_LINK\_CTRL, 0x0028) /\* 0x0428 \*/

[ 422](structbt__hci__cp__setup__sync__conn.md)struct [bt\_hci\_cp\_setup\_sync\_conn](structbt__hci__cp__setup__sync__conn.md) {

[ 423](structbt__hci__cp__setup__sync__conn.md#ad065185846694fc0070bb366e642f1c7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__setup__sync__conn.md#ad065185846694fc0070bb366e642f1c7);

[ 424](structbt__hci__cp__setup__sync__conn.md#aa35718e13a7d778c779be535c2b1945e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tx\_bandwidth](structbt__hci__cp__setup__sync__conn.md#aa35718e13a7d778c779be535c2b1945e);

[ 425](structbt__hci__cp__setup__sync__conn.md#a137601ab44970782e2f3d4fcd2c8fcc2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rx\_bandwidth](structbt__hci__cp__setup__sync__conn.md#a137601ab44970782e2f3d4fcd2c8fcc2);

[ 426](structbt__hci__cp__setup__sync__conn.md#a5ffb5e552d4913974a10a16083f82864) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_latency](structbt__hci__cp__setup__sync__conn.md#a5ffb5e552d4913974a10a16083f82864);

[ 427](structbt__hci__cp__setup__sync__conn.md#a4d7df5b1aa714bc14d0b6c3cbccc5014) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [content\_format](structbt__hci__cp__setup__sync__conn.md#a4d7df5b1aa714bc14d0b6c3cbccc5014);

[ 428](structbt__hci__cp__setup__sync__conn.md#a61ebbc775d3ca0724ea173d72a96e0c0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [retrans\_effort](structbt__hci__cp__setup__sync__conn.md#a61ebbc775d3ca0724ea173d72a96e0c0);

[ 429](structbt__hci__cp__setup__sync__conn.md#a6d4c16a4d77d3ee4f8f65ab18a0f192d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pkt\_type](structbt__hci__cp__setup__sync__conn.md#a6d4c16a4d77d3ee4f8f65ab18a0f192d);

430} \_\_packed;

431

[ 432](hci__types_8h.md#a97976c13fe03d346313bc19489d45360)#define BT\_HCI\_OP\_ACCEPT\_SYNC\_CONN\_REQ BT\_OP(BT\_OGF\_LINK\_CTRL, 0x0029) /\* 0x0429 \*/

[ 433](structbt__hci__cp__accept__sync__conn__req.md)struct [bt\_hci\_cp\_accept\_sync\_conn\_req](structbt__hci__cp__accept__sync__conn__req.md) {

[ 434](structbt__hci__cp__accept__sync__conn__req.md#a6a5a56d3a9d1a6d1064e7bd4c9fd333e) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__accept__sync__conn__req.md#a6a5a56d3a9d1a6d1064e7bd4c9fd333e);

[ 435](structbt__hci__cp__accept__sync__conn__req.md#a53fe4c6d61dbb99f99aa445b2c47a8ef) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tx\_bandwidth](structbt__hci__cp__accept__sync__conn__req.md#a53fe4c6d61dbb99f99aa445b2c47a8ef);

[ 436](structbt__hci__cp__accept__sync__conn__req.md#aceda6dbd3e221ad080850e9635886a86) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rx\_bandwidth](structbt__hci__cp__accept__sync__conn__req.md#aceda6dbd3e221ad080850e9635886a86);

[ 437](structbt__hci__cp__accept__sync__conn__req.md#a4ba6dffd840ef868524b490d227fd085) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_latency](structbt__hci__cp__accept__sync__conn__req.md#a4ba6dffd840ef868524b490d227fd085);

[ 438](structbt__hci__cp__accept__sync__conn__req.md#adba31b588bf12e852cc43b85c006aaa3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [content\_format](structbt__hci__cp__accept__sync__conn__req.md#adba31b588bf12e852cc43b85c006aaa3);

[ 439](structbt__hci__cp__accept__sync__conn__req.md#ab5ece67c5a1e62fc4124556eef743c26) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [retrans\_effort](structbt__hci__cp__accept__sync__conn__req.md#ab5ece67c5a1e62fc4124556eef743c26);

[ 440](structbt__hci__cp__accept__sync__conn__req.md#ab5d9c27ebdf45fb54b0c6330b5b095be) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pkt\_type](structbt__hci__cp__accept__sync__conn__req.md#ab5d9c27ebdf45fb54b0c6330b5b095be);

441} \_\_packed;

442

[ 443](hci__types_8h.md#aabb1f800ad4574e0350007af94cd786d)#define BT\_HCI\_OP\_REJECT\_CONN\_REQ BT\_OP(BT\_OGF\_LINK\_CTRL, 0x000a) /\* 0x040a \*/

[ 444](structbt__hci__cp__reject__conn__req.md)struct [bt\_hci\_cp\_reject\_conn\_req](structbt__hci__cp__reject__conn__req.md) {

[ 445](structbt__hci__cp__reject__conn__req.md#a9a1cb4173367c6f018fbd30a47c590b4) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__reject__conn__req.md#a9a1cb4173367c6f018fbd30a47c590b4);

[ 446](structbt__hci__cp__reject__conn__req.md#a1c2e234d6d00296bc01962b95e849df0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reason](structbt__hci__cp__reject__conn__req.md#a1c2e234d6d00296bc01962b95e849df0);

447} \_\_packed;

448

[ 449](hci__types_8h.md#a7da489e05d679c00f6cbbca0dfaaf136)#define BT\_HCI\_OP\_LINK\_KEY\_REPLY BT\_OP(BT\_OGF\_LINK\_CTRL, 0x000b) /\* 0x040b \*/

[ 450](structbt__hci__cp__link__key__reply.md)struct [bt\_hci\_cp\_link\_key\_reply](structbt__hci__cp__link__key__reply.md) {

[ 451](structbt__hci__cp__link__key__reply.md#ab5221952fbcfe413d7c3bd3a441a9b17) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__link__key__reply.md#ab5221952fbcfe413d7c3bd3a441a9b17);

[ 452](structbt__hci__cp__link__key__reply.md#a2af0b4b55a5ffcff0221da841ba0cbba) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [link\_key](structbt__hci__cp__link__key__reply.md#a2af0b4b55a5ffcff0221da841ba0cbba)[16];

453} \_\_packed;

454

[ 455](hci__types_8h.md#a7db25bd8bdbd4351e0dcef1df8dc7077)#define BT\_HCI\_OP\_LINK\_KEY\_NEG\_REPLY BT\_OP(BT\_OGF\_LINK\_CTRL, 0x000c) /\* 0x040c \*/

[ 456](structbt__hci__cp__link__key__neg__reply.md)struct [bt\_hci\_cp\_link\_key\_neg\_reply](structbt__hci__cp__link__key__neg__reply.md) {

[ 457](structbt__hci__cp__link__key__neg__reply.md#aca3114707eb7c631af582626551619cd) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__link__key__neg__reply.md#aca3114707eb7c631af582626551619cd);

458} \_\_packed;

459

[ 460](hci__types_8h.md#a7713e5641070ac7fca91e027fc9b8c40)#define BT\_HCI\_OP\_PIN\_CODE\_REPLY BT\_OP(BT\_OGF\_LINK\_CTRL, 0x000d) /\* 0x040d \*/

[ 461](structbt__hci__cp__pin__code__reply.md)struct [bt\_hci\_cp\_pin\_code\_reply](structbt__hci__cp__pin__code__reply.md) {

[ 462](structbt__hci__cp__pin__code__reply.md#a627800dcb580110be785576dfcc49bb1) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__pin__code__reply.md#a627800dcb580110be785576dfcc49bb1);

[ 463](structbt__hci__cp__pin__code__reply.md#aa0cbf668608c3eb4998356ad7b18c01a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pin\_len](structbt__hci__cp__pin__code__reply.md#aa0cbf668608c3eb4998356ad7b18c01a);

[ 464](structbt__hci__cp__pin__code__reply.md#afc4ed5ae429087f4692af716d6b56997) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pin\_code](structbt__hci__cp__pin__code__reply.md#afc4ed5ae429087f4692af716d6b56997)[16];

465} \_\_packed;

[ 466](structbt__hci__rp__pin__code__reply.md)struct [bt\_hci\_rp\_pin\_code\_reply](structbt__hci__rp__pin__code__reply.md) {

[ 467](structbt__hci__rp__pin__code__reply.md#a3f167661b8d3f63ab12e6f64fb33986b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__pin__code__reply.md#a3f167661b8d3f63ab12e6f64fb33986b);

[ 468](structbt__hci__rp__pin__code__reply.md#afc7c991fd8050e8aae56b8587b5ee01d) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__rp__pin__code__reply.md#afc7c991fd8050e8aae56b8587b5ee01d);

469} \_\_packed;

470

[ 471](hci__types_8h.md#a5833de4cefd59cee9c614163de7e927b)#define BT\_HCI\_OP\_PIN\_CODE\_NEG\_REPLY BT\_OP(BT\_OGF\_LINK\_CTRL, 0x000e) /\* 0x040e \*/

[ 472](structbt__hci__cp__pin__code__neg__reply.md)struct [bt\_hci\_cp\_pin\_code\_neg\_reply](structbt__hci__cp__pin__code__neg__reply.md) {

[ 473](structbt__hci__cp__pin__code__neg__reply.md#a8aec3ba6c530850dce0a2d7b7f7f86ee) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__pin__code__neg__reply.md#a8aec3ba6c530850dce0a2d7b7f7f86ee);

474} \_\_packed;

[ 475](structbt__hci__rp__pin__code__neg__reply.md)struct [bt\_hci\_rp\_pin\_code\_neg\_reply](structbt__hci__rp__pin__code__neg__reply.md) {

[ 476](structbt__hci__rp__pin__code__neg__reply.md#a10bcc55407e22417256c464684a41e58) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__pin__code__neg__reply.md#a10bcc55407e22417256c464684a41e58);

[ 477](structbt__hci__rp__pin__code__neg__reply.md#a168caf2a517aa573bd6acaf48e414e9b) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__rp__pin__code__neg__reply.md#a168caf2a517aa573bd6acaf48e414e9b);

478} \_\_packed;

479

[ 480](hci__types_8h.md#a4c24e505f9c799275fc2f35619b7df97)#define BT\_HCI\_OP\_AUTH\_REQUESTED BT\_OP(BT\_OGF\_LINK\_CTRL, 0x0011) /\* 0x0411 \*/

[ 481](structbt__hci__cp__auth__requested.md)struct [bt\_hci\_cp\_auth\_requested](structbt__hci__cp__auth__requested.md) {

[ 482](structbt__hci__cp__auth__requested.md#a079490f8f8569e281ce16f13847cbf33) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__auth__requested.md#a079490f8f8569e281ce16f13847cbf33);

483} \_\_packed;

484

[ 485](hci__types_8h.md#ac32c04cf6bc9de299f0a307dbeed63f3)#define BT\_HCI\_OP\_SET\_CONN\_ENCRYPT BT\_OP(BT\_OGF\_LINK\_CTRL, 0x0013) /\* 0x0413 \*/

[ 486](structbt__hci__cp__set__conn__encrypt.md)struct [bt\_hci\_cp\_set\_conn\_encrypt](structbt__hci__cp__set__conn__encrypt.md) {

[ 487](structbt__hci__cp__set__conn__encrypt.md#a39e0c40ed6e6e9387ae384fd122fca4b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__set__conn__encrypt.md#a39e0c40ed6e6e9387ae384fd122fca4b);

[ 488](structbt__hci__cp__set__conn__encrypt.md#aa259563efd49d04a8886f74169fd30b1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [encrypt](structbt__hci__cp__set__conn__encrypt.md#aa259563efd49d04a8886f74169fd30b1);

489} \_\_packed;

490

[ 491](hci__types_8h.md#a2e759212d10ecd3a2e975379bf18d374)#define BT\_HCI\_OP\_REMOTE\_NAME\_REQUEST BT\_OP(BT\_OGF\_LINK\_CTRL, 0x0019) /\* 0x0419 \*/

[ 492](structbt__hci__cp__remote__name__request.md)struct [bt\_hci\_cp\_remote\_name\_request](structbt__hci__cp__remote__name__request.md) {

[ 493](structbt__hci__cp__remote__name__request.md#a5093f7bb70fa36f4948039d02d594e27) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__remote__name__request.md#a5093f7bb70fa36f4948039d02d594e27);

[ 494](structbt__hci__cp__remote__name__request.md#aed0aea58ca6f5dc15220083d377cbf5c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pscan\_rep\_mode](structbt__hci__cp__remote__name__request.md#aed0aea58ca6f5dc15220083d377cbf5c);

[ 495](structbt__hci__cp__remote__name__request.md#ab1883aa2b08d89f9c3190f338808a43c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reserved](structbt__hci__cp__remote__name__request.md#ab1883aa2b08d89f9c3190f338808a43c);

[ 496](structbt__hci__cp__remote__name__request.md#a5d7ea30052f8e4e2b3564659ca187c48) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [clock\_offset](structbt__hci__cp__remote__name__request.md#a5d7ea30052f8e4e2b3564659ca187c48);

497} \_\_packed;

498

[ 499](hci__types_8h.md#a76f79f4e14396297cc5db4ca8dba0c4c)#define BT\_HCI\_OP\_REMOTE\_NAME\_CANCEL BT\_OP(BT\_OGF\_LINK\_CTRL, 0x001a) /\* 0x041a \*/

[ 500](structbt__hci__cp__remote__name__cancel.md)struct [bt\_hci\_cp\_remote\_name\_cancel](structbt__hci__cp__remote__name__cancel.md) {

[ 501](structbt__hci__cp__remote__name__cancel.md#a0b7b4362804077ce828aeeb2b8af86b9) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__remote__name__cancel.md#a0b7b4362804077ce828aeeb2b8af86b9);

502} \_\_packed;

[ 503](structbt__hci__rp__remote__name__cancel.md)struct [bt\_hci\_rp\_remote\_name\_cancel](structbt__hci__rp__remote__name__cancel.md) {

[ 504](structbt__hci__rp__remote__name__cancel.md#ac7fadee392b126cb50cef7a6336926cb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__remote__name__cancel.md#ac7fadee392b126cb50cef7a6336926cb);

[ 505](structbt__hci__rp__remote__name__cancel.md#a455432799a1272f88b2b00a35a2e7ef5) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__rp__remote__name__cancel.md#a455432799a1272f88b2b00a35a2e7ef5);

506} \_\_packed;

507

[ 508](hci__types_8h.md#ab6282249d4c14412674083007346b005)#define BT\_HCI\_OP\_READ\_REMOTE\_FEATURES BT\_OP(BT\_OGF\_LINK\_CTRL, 0x001b) /\* 0x041b \*/

[ 509](structbt__hci__cp__read__remote__features.md)struct [bt\_hci\_cp\_read\_remote\_features](structbt__hci__cp__read__remote__features.md) {

[ 510](structbt__hci__cp__read__remote__features.md#ae14362a04c00b37342f3cc413f3933d3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__read__remote__features.md#ae14362a04c00b37342f3cc413f3933d3);

511} \_\_packed;

512

[ 513](hci__types_8h.md#a87f6747b2b5d52a7886a1ec72100d9d0)#define BT\_HCI\_OP\_READ\_REMOTE\_EXT\_FEATURES BT\_OP(BT\_OGF\_LINK\_CTRL, 0x001c) /\* 0x041c \*/

[ 514](structbt__hci__cp__read__remote__ext__features.md)struct [bt\_hci\_cp\_read\_remote\_ext\_features](structbt__hci__cp__read__remote__ext__features.md) {

[ 515](structbt__hci__cp__read__remote__ext__features.md#aaa236c11d148252e34fd20d794d991f3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__read__remote__ext__features.md#aaa236c11d148252e34fd20d794d991f3);

[ 516](structbt__hci__cp__read__remote__ext__features.md#a6aff189605b276998e58b051429a5cd2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [page](structbt__hci__cp__read__remote__ext__features.md#a6aff189605b276998e58b051429a5cd2);

517} \_\_packed;

518

[ 519](hci__types_8h.md#ae723b797305fe7a370b94d8c865e5708)#define BT\_HCI\_OP\_READ\_REMOTE\_VERSION\_INFO BT\_OP(BT\_OGF\_LINK\_CTRL, 0x001d) /\* 0x041d \*/

[ 520](structbt__hci__cp__read__remote__version__info.md)struct [bt\_hci\_cp\_read\_remote\_version\_info](structbt__hci__cp__read__remote__version__info.md) {

[ 521](structbt__hci__cp__read__remote__version__info.md#a504b83f16a82b1e179d74547c7a29bf3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__read__remote__version__info.md#a504b83f16a82b1e179d74547c7a29bf3);

522} \_\_packed;

523

[ 524](hci__types_8h.md#a343a3c5c594dd25483fedf38c304a09a)#define BT\_HCI\_OP\_IO\_CAPABILITY\_REPLY BT\_OP(BT\_OGF\_LINK\_CTRL, 0x002b) /\* 0x042b \*/

[ 525](structbt__hci__cp__io__capability__reply.md)struct [bt\_hci\_cp\_io\_capability\_reply](structbt__hci__cp__io__capability__reply.md) {

[ 526](structbt__hci__cp__io__capability__reply.md#afbe2bc0c1dcc0791a98068b052aea1f2) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__io__capability__reply.md#afbe2bc0c1dcc0791a98068b052aea1f2);

[ 527](structbt__hci__cp__io__capability__reply.md#a0995c81ba1f653c59bda9a444fb17915) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [capability](structbt__hci__cp__io__capability__reply.md#a0995c81ba1f653c59bda9a444fb17915);

[ 528](structbt__hci__cp__io__capability__reply.md#ac002ea0b276200a15d603b5ac83666e5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [oob\_data](structbt__hci__cp__io__capability__reply.md#ac002ea0b276200a15d603b5ac83666e5);

[ 529](structbt__hci__cp__io__capability__reply.md#a8983418dca3a7725f3b113a4d0ee177e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [authentication](structbt__hci__cp__io__capability__reply.md#a8983418dca3a7725f3b113a4d0ee177e);

530} \_\_packed;

531

[ 532](hci__types_8h.md#ab688441778a4239e1e8f2b2e0b74004f)#define BT\_HCI\_OP\_USER\_CONFIRM\_REPLY BT\_OP(BT\_OGF\_LINK\_CTRL, 0x002c) /\* 0x042c \*/

[ 533](hci__types_8h.md#aecc09326c190d2ab7b89f99375cd39bd)#define BT\_HCI\_OP\_USER\_CONFIRM\_NEG\_REPLY BT\_OP(BT\_OGF\_LINK\_CTRL, 0x002d) /\* 0x042d \*/

[ 534](structbt__hci__cp__user__confirm__reply.md)struct [bt\_hci\_cp\_user\_confirm\_reply](structbt__hci__cp__user__confirm__reply.md) {

[ 535](structbt__hci__cp__user__confirm__reply.md#abe0e8da3e590c565364ed30ba107a0e6) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__user__confirm__reply.md#abe0e8da3e590c565364ed30ba107a0e6);

536} \_\_packed;

[ 537](structbt__hci__rp__user__confirm__reply.md)struct [bt\_hci\_rp\_user\_confirm\_reply](structbt__hci__rp__user__confirm__reply.md) {

[ 538](structbt__hci__rp__user__confirm__reply.md#ab07114550c2da3c1e9925cb883bf3a89) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__user__confirm__reply.md#ab07114550c2da3c1e9925cb883bf3a89);

[ 539](structbt__hci__rp__user__confirm__reply.md#a91678db3ae2a696ba7b9dd5bc080c488) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__rp__user__confirm__reply.md#a91678db3ae2a696ba7b9dd5bc080c488);

540} \_\_packed;

541

[ 542](hci__types_8h.md#ad1fce315b731f9978cd52a8c23994a10)#define BT\_HCI\_OP\_USER\_PASSKEY\_REPLY BT\_OP(BT\_OGF\_LINK\_CTRL, 0x002e) /\* 0x042e \*/

[ 543](structbt__hci__cp__user__passkey__reply.md)struct [bt\_hci\_cp\_user\_passkey\_reply](structbt__hci__cp__user__passkey__reply.md) {

[ 544](structbt__hci__cp__user__passkey__reply.md#a56dbb4a858ecbf36eee61e24ed3742cf) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__user__passkey__reply.md#a56dbb4a858ecbf36eee61e24ed3742cf);

[ 545](structbt__hci__cp__user__passkey__reply.md#a80483025a32f37e7f75b3a220d48148c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [passkey](structbt__hci__cp__user__passkey__reply.md#a80483025a32f37e7f75b3a220d48148c);

546} \_\_packed;

547

[ 548](hci__types_8h.md#a96f9c5c3439d829dfac94cca9ad1f015)#define BT\_HCI\_OP\_USER\_PASSKEY\_NEG\_REPLY BT\_OP(BT\_OGF\_LINK\_CTRL, 0x002f) /\* 0x042f \*/

[ 549](structbt__hci__cp__user__passkey__neg__reply.md)struct [bt\_hci\_cp\_user\_passkey\_neg\_reply](structbt__hci__cp__user__passkey__neg__reply.md) {

[ 550](structbt__hci__cp__user__passkey__neg__reply.md#ade9d7068054b15089b8c238ecc3e4397) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__user__passkey__neg__reply.md#ade9d7068054b15089b8c238ecc3e4397);

551} \_\_packed;

552

[ 553](hci__types_8h.md#a75d9a0acb6522dd0ae290572c4255540)#define BT\_HCI\_OP\_IO\_CAPABILITY\_NEG\_REPLY BT\_OP(BT\_OGF\_LINK\_CTRL, 0x0034) /\* 0x0434 \*/

[ 554](structbt__hci__cp__io__capability__neg__reply.md)struct [bt\_hci\_cp\_io\_capability\_neg\_reply](structbt__hci__cp__io__capability__neg__reply.md) {

[ 555](structbt__hci__cp__io__capability__neg__reply.md#a8dba05bc84de2573eaea43ea9e428015) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__io__capability__neg__reply.md#a8dba05bc84de2573eaea43ea9e428015);

[ 556](structbt__hci__cp__io__capability__neg__reply.md#a82c54e5ad7fd4a6d81952832ae4de373) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reason](structbt__hci__cp__io__capability__neg__reply.md#a82c54e5ad7fd4a6d81952832ae4de373);

557} \_\_packed;

558

[ 559](hci__types_8h.md#abb9bf6d936310a43c4a88244ad12640d)#define BT\_HCI\_OP\_SET\_EVENT\_MASK BT\_OP(BT\_OGF\_BASEBAND, 0x0001) /\* 0x0c01 \*/

[ 560](structbt__hci__cp__set__event__mask.md)struct [bt\_hci\_cp\_set\_event\_mask](structbt__hci__cp__set__event__mask.md) {

[ 561](structbt__hci__cp__set__event__mask.md#ab3af227511f47ee03f2d6aba8ae65c5d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [events](structbt__hci__cp__set__event__mask.md#ab3af227511f47ee03f2d6aba8ae65c5d)[8];

562} \_\_packed;

563

[ 564](hci__types_8h.md#abb515eb4ea9e66503bf1f375af01a6c0)#define BT\_HCI\_OP\_RESET BT\_OP(BT\_OGF\_BASEBAND, 0x0003) /\* 0x0c03 \*/

565

[ 566](hci__types_8h.md#a9b328487dbeeaa587e6f75011441f340)#define BT\_HCI\_OP\_WRITE\_LOCAL\_NAME BT\_OP(BT\_OGF\_BASEBAND, 0x0013) /\* 0x0c13 \*/

[ 567](structbt__hci__write__local__name.md)struct [bt\_hci\_write\_local\_name](structbt__hci__write__local__name.md) {

[ 568](structbt__hci__write__local__name.md#a8d2cd9a16525c3fc10ae0e3f196110da) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [local\_name](structbt__hci__write__local__name.md#a8d2cd9a16525c3fc10ae0e3f196110da)[248];

569} \_\_packed;

570

[ 571](hci__types_8h.md#af302a5e40644307f522154f3803572d0)#define BT\_HCI\_OP\_READ\_CONN\_ACCEPT\_TIMEOUT BT\_OP(BT\_OGF\_BASEBAND, 0x0015) /\* 0x0c15 \*/

[ 572](structbt__hci__rp__read__conn__accept__timeout.md)struct [bt\_hci\_rp\_read\_conn\_accept\_timeout](structbt__hci__rp__read__conn__accept__timeout.md) {

[ 573](structbt__hci__rp__read__conn__accept__timeout.md#afeb5888722ee368e02c6b27b75ab2a70) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__conn__accept__timeout.md#afeb5888722ee368e02c6b27b75ab2a70);

[ 574](structbt__hci__rp__read__conn__accept__timeout.md#a01ca30c92311ec1df19a4cf835ea74cf) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_accept\_timeout](structbt__hci__rp__read__conn__accept__timeout.md#a01ca30c92311ec1df19a4cf835ea74cf);

575} \_\_packed;

576

[ 577](hci__types_8h.md#a6799bd267ef7c19b05ed2dd57baf0393)#define BT\_HCI\_OP\_WRITE\_CONN\_ACCEPT\_TIMEOUT BT\_OP(BT\_OGF\_BASEBAND, 0x0016) /\* 0x0c16 \*/

[ 578](structbt__hci__cp__write__conn__accept__timeout.md)struct [bt\_hci\_cp\_write\_conn\_accept\_timeout](structbt__hci__cp__write__conn__accept__timeout.md) {

[ 579](structbt__hci__cp__write__conn__accept__timeout.md#a13de5f88920c6a41dafa598734b7acf9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_accept\_timeout](structbt__hci__cp__write__conn__accept__timeout.md#a13de5f88920c6a41dafa598734b7acf9);

580} \_\_packed;

581

[ 582](structbt__hci__rp__write__conn__accept__timeout.md)struct [bt\_hci\_rp\_write\_conn\_accept\_timeout](structbt__hci__rp__write__conn__accept__timeout.md) {

[ 583](structbt__hci__rp__write__conn__accept__timeout.md#a1f9eee1a5843747e0d224b86b602a3da) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__write__conn__accept__timeout.md#a1f9eee1a5843747e0d224b86b602a3da);

584} \_\_packed;

585

[ 586](hci__types_8h.md#a5ef44fe1cca74a2258ffab1edd04acdf)#define BT\_HCI\_OP\_WRITE\_PAGE\_TIMEOUT BT\_OP(BT\_OGF\_BASEBAND, 0x0018) /\* 0x0c18 \*/

587

[ 588](hci__types_8h.md#a0c8b9dc68ec6cd91ec0e9e565701a887)#define BT\_HCI\_OP\_WRITE\_SCAN\_ENABLE BT\_OP(BT\_OGF\_BASEBAND, 0x001a) /\* 0x0c1a \*/

[ 589](hci__types_8h.md#a19b4c20d243de28462b686088e2971a3)#define BT\_BREDR\_SCAN\_DISABLED 0x00

[ 590](hci__types_8h.md#a2f75eaee67bbb6c0211f3146d881278f)#define BT\_BREDR\_SCAN\_INQUIRY 0x01

[ 591](hci__types_8h.md#a006d877a26f4e8dd0689b1324107a843)#define BT\_BREDR\_SCAN\_PAGE 0x02

592

[ 593](hci__types_8h.md#aa8793a9bc39bf833124c8c961e441a43)#define BT\_COD(major\_service, major\_device, minor\_device) \

594 (((uint32\_t)major\_service << 13) | ((uint32\_t)major\_device << 8) | \

595 ((uint32\_t)minor\_device << 2))

[ 596](hci__types_8h.md#af2c925e431eec42930101a72b00a7283)#define BT\_COD\_VALID(cod) ((0 == (cod[0] & (BIT(0) | BIT(1)))) ? true : false)

[ 597](hci__types_8h.md#ab598bdad77874748f74187aa32049ea6)#define BT\_COD\_MAJOR\_SERVICE\_CLASSES(cod) \

598 ((((uint32\_t)cod[2] & 0xFF) >> 5) | (((uint32\_t)cod[1] & 0xD0) >> 5))

[ 599](hci__types_8h.md#a129895b48ad9071017a2e97335ec6d2b)#define BT\_COD\_MAJOR\_DEVICE\_CLASS(cod) ((((uint32\_t)cod[1]) & 0x1FUL))

[ 600](hci__types_8h.md#adcf892b98d0924ea8a78d4b8b588bddb)#define BT\_COD\_MINOR\_DEVICE\_CLASS(cod) (((((uint32\_t)cod[0]) & 0xFF) >> 2))

601

[ 602](hci__types_8h.md#ad14acbda93a611913f675175a433c6e3)#define BT\_COD\_MAJOR\_MISC 0x00

[ 603](hci__types_8h.md#acdd58e03fb46b783025cfd54d429263b)#define BT\_COD\_MAJOR\_COMPUTER 0x01

[ 604](hci__types_8h.md#a59dd55c19cb4d995175a49125529536f)#define BT\_COD\_MAJOR\_PHONE 0x02

[ 605](hci__types_8h.md#a81ce79e07c526ae4ef3be26cca65cb2d)#define BT\_COD\_MAJOR\_LAN\_NETWORK\_AP 0x03

[ 606](hci__types_8h.md#ae35a91503887ea73a32342888cc75239)#define BT\_COD\_MAJOR\_AUDIO\_VIDEO 0x04

[ 607](hci__types_8h.md#ad5cf6294b462dd8b1f49c23a93deb267)#define BT\_COD\_MAJOR\_PERIPHERAL 0x05

[ 608](hci__types_8h.md#a1daeb8de054847bcd5fbee8c5797648c)#define BT\_COD\_MAJOR\_IMAGING 0x06

[ 609](hci__types_8h.md#ac5d662f2a86144c1d9698cf0443c9ea7)#define BT\_COD\_MAJOR\_WEARABLE 0x07

[ 610](hci__types_8h.md#a592ae9ac7a15862b8fa866a2f79d36e8)#define BT\_COD\_MAJOR\_TOY 0x08

[ 611](hci__types_8h.md#a9091627f66847298c6a1f9fa566d261d)#define BT\_COD\_MAJOR\_HEALTH 0x09

[ 612](hci__types_8h.md#ac6cffb2a74393e469b587adc5dfb12b1)#define BT\_COD\_MAJOR\_UNCATEGORIZED 0x1F

613

614/\* Minor Device Class field - Computer Major Class \*/

[ 615](hci__types_8h.md#aec73961628a8ba0ea835b08971d23ce3)#define BT\_COD\_MAJOR\_COMPUTER\_MINOR\_UNCATEGORIZED 0x00

[ 616](hci__types_8h.md#a54cd2fc8881fc63b3784d4267df0cc98)#define BT\_COD\_MAJOR\_COMPUTER\_MINOR\_DESKTOP 0x01

[ 617](hci__types_8h.md#af247d382b726b0599b706900fe189e4d)#define BT\_COD\_MAJOR\_COMPUTER\_MINOR\_SERVER\_CLASS\_COMPUTER 0x02

[ 618](hci__types_8h.md#a8655f31e07a18335fa7a3f42635c1352)#define BT\_COD\_MAJOR\_COMPUTER\_MINOR\_LAPTOP 0x03

[ 619](hci__types_8h.md#ac6b246fe1bb6faf7c5a4d7d1004ad73e)#define BT\_COD\_MAJOR\_COMPUTER\_MINOR\_HANDHELD\_PC\_PDA 0x04

[ 620](hci__types_8h.md#a0d44dc3f155861fa6e1ea8620d957e97)#define BT\_COD\_MAJOR\_COMPUTER\_MINOR\_PALM\_SIZE\_PC\_PDA 0x05

[ 621](hci__types_8h.md#a4a02b61073979297d275c16302d1452f)#define BT\_COD\_MAJOR\_COMPUTER\_MINOR\_WEARABLE\_COMPUTER 0x06

[ 622](hci__types_8h.md#ac4a3ced7c754169af6fe24f987f80e3a)#define BT\_COD\_MAJOR\_COMPUTER\_MINOR\_TABLET 0x07

623

624/\* Minor Device Class field - Phone Major Class \*/

[ 625](hci__types_8h.md#a70e534fba0ee653a1d8fffc4f57a399d)#define BT\_COD\_MAJOR\_PHONE\_MINOR\_UNCATEGORIZED 0x00

[ 626](hci__types_8h.md#a4954e6760da119f71d91624200b70344)#define BT\_COD\_MAJOR\_PHONE\_MINOR\_CELLULAR 0x01

[ 627](hci__types_8h.md#ab6dc621f45cd579242a58b523cf250bf)#define BT\_COD\_MAJOR\_PHONE\_MINOR\_CORDLESS 0x02

[ 628](hci__types_8h.md#a3c22870123a8c9015d2664e061bf095a)#define BT\_COD\_MAJOR\_PHONE\_MINOR\_SMARTPHONE 0x03

[ 629](hci__types_8h.md#a7f2801f76561e04801c8cd7bc0de3cc1)#define BT\_COD\_MAJOR\_PHONE\_MINOR\_WIRED\_MODEM\_VOICE\_GATEWAY 0x04

[ 630](hci__types_8h.md#a4eded4ed6985c8110e040c0a4e3b5341)#define BT\_COD\_MAJOR\_PHONE\_MINOR\_ISDN 0x05

631

632/\* Minor Device Class field - Audio/Video Major Class \*/

[ 633](hci__types_8h.md#a0432846ee3f571d35feba5af70b1b0af)#define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_UNCATEGORIZED 0x00

[ 634](hci__types_8h.md#a56c2a8e3602b53fce244faafd4101af4)#define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_WEARABLE\_HEADSET 0x01

[ 635](hci__types_8h.md#a7eff517cf71309181024f9eb7babb277)#define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_HANDS\_FREE 0x02

[ 636](hci__types_8h.md#a50941bdf421209a7bd41b5e225c8a8ed)#define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_RFU 0x03

[ 637](hci__types_8h.md#ac586986c21d07748bf92e4ade2cb857c)#define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_MICROPHONE 0x04

[ 638](hci__types_8h.md#a54790088ccbeca72e3a41cd559f1c994)#define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_LOUDSPEAKER 0x05

[ 639](hci__types_8h.md#ab93463c966352ee2b246003edad18924)#define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_HEADPHONES 0x06

[ 640](hci__types_8h.md#a516cf67e162628fa7e8ab15c85aa50a1)#define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_PORTABLE\_AUDIO 0x07

[ 641](hci__types_8h.md#a9df23b6e094f75de44fdc6e072d07ed6)#define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_CAR\_AUDIO 0x08

[ 642](hci__types_8h.md#a28db3d9daf698fcb382b417532a53652)#define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_SET\_TOP\_BOX 0x09

[ 643](hci__types_8h.md#a0ab46892a2ab50747d8fcec489b8a5c2)#define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_HIFI\_AUDIO 0x0A

[ 644](hci__types_8h.md#a0c0c540721712ba407ea08972420cad6)#define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_VCR 0x0B

[ 645](hci__types_8h.md#a0b61e3de9a35c714fc1414f29a2a79c5)#define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_VIDEO\_CAMERA 0x0C

[ 646](hci__types_8h.md#a1c77c5966d3cb71e827a4e59234240f9)#define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_CAMCORDER 0x0D

[ 647](hci__types_8h.md#a13af74023c32c24f7baa6249cc538e2c)#define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_VIDEO\_MONITOR 0x0E

[ 648](hci__types_8h.md#a5569a391b209cdb551576392e228dcb0)#define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_VIDEO\_DISPLAY\_LOUDSPEAKER 0x0F

[ 649](hci__types_8h.md#afa9446149a24189fd4192c8b32a5ae97)#define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_VIDEO\_CONFERENCING 0x10

[ 650](hci__types_8h.md#a85de6aa2ca223da1ac43ffe57489ac24)#define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_RFU2 0x11

[ 651](hci__types_8h.md#a2ed0612651757c12606bab74ea10d14a)#define BT\_COD\_MAJOR\_AUDIO\_VIDEO\_MINOR\_GAME\_TOY 0x12

652

[ 653](hci__types_8h.md#ace988e19fa62bf61654a329acaf99018)#define BT\_HCI\_OP\_WRITE\_CLASS\_OF\_DEVICE BT\_OP(BT\_OGF\_BASEBAND, 0x0024) /\* 0x0c24 \*/

[ 654](structbt__hci__cp__write__class__of__device.md)struct [bt\_hci\_cp\_write\_class\_of\_device](structbt__hci__cp__write__class__of__device.md) {

[ 655](structbt__hci__cp__write__class__of__device.md#acc3b940de1a5da095e8a4f18e69229f2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [class\_of\_device](structbt__hci__cp__write__class__of__device.md#acc3b940de1a5da095e8a4f18e69229f2)[3];

656} \_\_packed;

657

[ 658](hci__types_8h.md#ac1ebc6168b2823aea2af2e2f89ffb6cd)#define BT\_TX\_POWER\_LEVEL\_CURRENT 0x00

[ 659](hci__types_8h.md#ad835bc44abee2e174f86cd55ac0338e3)#define BT\_TX\_POWER\_LEVEL\_MAX 0x01

[ 660](hci__types_8h.md#aaac00b7d9f9f96d1438643ee054ab21a)#define BT\_HCI\_OP\_READ\_TX\_POWER\_LEVEL BT\_OP(BT\_OGF\_BASEBAND, 0x002d) /\* 0x0c2d \*/

[ 661](structbt__hci__cp__read__tx__power__level.md)struct [bt\_hci\_cp\_read\_tx\_power\_level](structbt__hci__cp__read__tx__power__level.md) {

[ 662](structbt__hci__cp__read__tx__power__level.md#a1c268364fc80b9478d70b7eb997d9825) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__read__tx__power__level.md#a1c268364fc80b9478d70b7eb997d9825);

[ 663](structbt__hci__cp__read__tx__power__level.md#a1920e671ec2deda1daf47f06a86d2881) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__hci__cp__read__tx__power__level.md#a1920e671ec2deda1daf47f06a86d2881);

664} \_\_packed;

665

[ 666](structbt__hci__rp__read__tx__power__level.md)struct [bt\_hci\_rp\_read\_tx\_power\_level](structbt__hci__rp__read__tx__power__level.md) {

[ 667](structbt__hci__rp__read__tx__power__level.md#af40a8e2e663872e8d9fdde839cc6d1b4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__tx__power__level.md#af40a8e2e663872e8d9fdde839cc6d1b4);

[ 668](structbt__hci__rp__read__tx__power__level.md#ac2bd21e90145102bc483c2b0b3cdd416) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__read__tx__power__level.md#ac2bd21e90145102bc483c2b0b3cdd416);

[ 669](structbt__hci__rp__read__tx__power__level.md#a46526b820038bb445a7824a7b4bfc870) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power\_level](structbt__hci__rp__read__tx__power__level.md#a46526b820038bb445a7824a7b4bfc870);

670} \_\_packed;

671

[ 672](hci__types_8h.md#a740a01412d6fad277362634e1854f54b)#define BT\_HCI\_LE\_TX\_POWER\_PHY\_1M 0x01

[ 673](hci__types_8h.md#aa3eadebe7675de492b01ec117f72d808)#define BT\_HCI\_LE\_TX\_POWER\_PHY\_2M 0x02

[ 674](hci__types_8h.md#a66f2c7c03e65392c3477faddc14d9787)#define BT\_HCI\_LE\_TX\_POWER\_PHY\_CODED\_S8 0x03

[ 675](hci__types_8h.md#ab2bed6683929c37a3d087dba88309e45)#define BT\_HCI\_LE\_TX\_POWER\_PHY\_CODED\_S2 0x04

[ 676](hci__types_8h.md#aebd5487b500c54a47a926bb1daa56f5e)#define BT\_HCI\_OP\_LE\_ENH\_READ\_TX\_POWER\_LEVEL BT\_OP(BT\_OGF\_LE, 0x0076) /\* 0x2076 \*/

[ 677](structbt__hci__cp__le__read__tx__power__level.md)struct [bt\_hci\_cp\_le\_read\_tx\_power\_level](structbt__hci__cp__le__read__tx__power__level.md) {

[ 678](structbt__hci__cp__le__read__tx__power__level.md#af8c2d89b183d7bdc0f55a0bf783a373d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__read__tx__power__level.md#af8c2d89b183d7bdc0f55a0bf783a373d);

[ 679](structbt__hci__cp__le__read__tx__power__level.md#a4863396dfe4dca65aaef68293e29291b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__cp__le__read__tx__power__level.md#a4863396dfe4dca65aaef68293e29291b);

680} \_\_packed;

681

[ 682](structbt__hci__rp__le__read__tx__power__level.md)struct [bt\_hci\_rp\_le\_read\_tx\_power\_level](structbt__hci__rp__le__read__tx__power__level.md) {

[ 683](structbt__hci__rp__le__read__tx__power__level.md#a4c83db208bfcb7c9fd2211d192a26d90) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__tx__power__level.md#a4c83db208bfcb7c9fd2211d192a26d90);

[ 684](structbt__hci__rp__le__read__tx__power__level.md#aec00dfb34abce2d95af183b74f63d1f3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__read__tx__power__level.md#aec00dfb34abce2d95af183b74f63d1f3);

[ 685](structbt__hci__rp__le__read__tx__power__level.md#ae65a43aad74b1081e88afdb533cbe813) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__rp__le__read__tx__power__level.md#ae65a43aad74b1081e88afdb533cbe813);

[ 686](structbt__hci__rp__le__read__tx__power__level.md#ad14f660eb67f1014d1a62b0e5a113969) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [current\_tx\_power\_level](structbt__hci__rp__le__read__tx__power__level.md#ad14f660eb67f1014d1a62b0e5a113969);

[ 687](structbt__hci__rp__le__read__tx__power__level.md#a5f9c59660f7c5842712a4ad9ae1d9527) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [max\_tx\_power\_level](structbt__hci__rp__le__read__tx__power__level.md#a5f9c59660f7c5842712a4ad9ae1d9527);

688} \_\_packed;

689

[ 690](hci__types_8h.md#ac5bc187df83f28a48ba1f87f84aed54a)#define BT\_HCI\_OP\_LE\_READ\_REMOTE\_TX\_POWER\_LEVEL BT\_OP(BT\_OGF\_LE, 0x0077) /\* 0x2077 \*/

691

[ 692](hci__types_8h.md#a46bac5521c33da56df1d06ed7c472a06)#define BT\_HCI\_LE\_TX\_POWER\_REPORT\_DISABLE 0x00

[ 693](hci__types_8h.md#a31f7372543b6dec580fe464ec011d752)#define BT\_HCI\_LE\_TX\_POWER\_REPORT\_ENABLE 0x01

[ 694](hci__types_8h.md#aec22a58c052e856558b316b4f94f8561)#define BT\_HCI\_OP\_LE\_SET\_TX\_POWER\_REPORT\_ENABLE BT\_OP(BT\_OGF\_LE, 0x007A) /\* 0x207A \*/

[ 695](structbt__hci__cp__le__set__tx__power__report__enable.md)struct [bt\_hci\_cp\_le\_set\_tx\_power\_report\_enable](structbt__hci__cp__le__set__tx__power__report__enable.md) {

[ 696](structbt__hci__cp__le__set__tx__power__report__enable.md#a4a37c87f8f6a966a90c5de09096d1356) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__set__tx__power__report__enable.md#a4a37c87f8f6a966a90c5de09096d1356);

[ 697](structbt__hci__cp__le__set__tx__power__report__enable.md#a30580470d1ba516d86c8b157ca415ef3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [local\_enable](structbt__hci__cp__le__set__tx__power__report__enable.md#a30580470d1ba516d86c8b157ca415ef3);

[ 698](structbt__hci__cp__le__set__tx__power__report__enable.md#ab4e8fb4fd7a1fbbc8b5736f8a6f65c5e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [remote\_enable](structbt__hci__cp__le__set__tx__power__report__enable.md#ab4e8fb4fd7a1fbbc8b5736f8a6f65c5e);

699} \_\_packed;

700

[ 701](structbt__hci__cp__le__set__path__loss__reporting__parameters.md)struct [bt\_hci\_cp\_le\_set\_path\_loss\_reporting\_parameters](structbt__hci__cp__le__set__path__loss__reporting__parameters.md) {

[ 702](structbt__hci__cp__le__set__path__loss__reporting__parameters.md#a2dec83b0269835538cf4bc5553483f19) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__set__path__loss__reporting__parameters.md#a2dec83b0269835538cf4bc5553483f19);

[ 703](structbt__hci__cp__le__set__path__loss__reporting__parameters.md#ac8b7b832ba241c0448c80be22249b3ca) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [high\_threshold](structbt__hci__cp__le__set__path__loss__reporting__parameters.md#ac8b7b832ba241c0448c80be22249b3ca);

[ 704](structbt__hci__cp__le__set__path__loss__reporting__parameters.md#ab5de762b7b82c8f453dafe1ea9bbf46d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [high\_hysteresis](structbt__hci__cp__le__set__path__loss__reporting__parameters.md#ab5de762b7b82c8f453dafe1ea9bbf46d);

[ 705](structbt__hci__cp__le__set__path__loss__reporting__parameters.md#a79a53ca3a481e013a5ee892d779e7bfd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [low\_threshold](structbt__hci__cp__le__set__path__loss__reporting__parameters.md#a79a53ca3a481e013a5ee892d779e7bfd);

[ 706](structbt__hci__cp__le__set__path__loss__reporting__parameters.md#a28f79bd4ccec4ed108e20a0080ec842d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [low\_hysteresis](structbt__hci__cp__le__set__path__loss__reporting__parameters.md#a28f79bd4ccec4ed108e20a0080ec842d);

[ 707](structbt__hci__cp__le__set__path__loss__reporting__parameters.md#a2289e8198eea1686030ffd3e225c8e7d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [min\_time\_spent](structbt__hci__cp__le__set__path__loss__reporting__parameters.md#a2289e8198eea1686030ffd3e225c8e7d);

708} \_\_packed;

709

[ 710](structbt__hci__cp__le__set__path__loss__reporting__enable.md)struct [bt\_hci\_cp\_le\_set\_path\_loss\_reporting\_enable](structbt__hci__cp__le__set__path__loss__reporting__enable.md) {

[ 711](structbt__hci__cp__le__set__path__loss__reporting__enable.md#a79487ac2235da100b41ec50c77bad808) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__set__path__loss__reporting__enable.md#a79487ac2235da100b41ec50c77bad808);

[ 712](structbt__hci__cp__le__set__path__loss__reporting__enable.md#a209a77ef3cf545150feaecdb814797f0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enable](structbt__hci__cp__le__set__path__loss__reporting__enable.md#a209a77ef3cf545150feaecdb814797f0);

713} \_\_packed;

714

[ 715](hci__types_8h.md#a48a3e41f8d6598e617d02ebc609911c6)#define BT\_HCI\_OP\_LE\_SET\_PATH\_LOSS\_REPORTING\_PARAMETERS BT\_OP(BT\_OGF\_LE, 0x0078) /\* 0x2078 \*/

716

[ 717](hci__types_8h.md#a9faae90b3adfcbcdf7da19c631e68a69)#define BT\_HCI\_LE\_PATH\_LOSS\_REPORTING\_DISABLE 0x00

[ 718](hci__types_8h.md#ab2e698e4ebbb45d9e3db0663ae5e4657)#define BT\_HCI\_LE\_PATH\_LOSS\_REPORTING\_ENABLE 0x01

[ 719](hci__types_8h.md#a09c0d554937de38a7b74661a2820237b)#define BT\_HCI\_OP\_LE\_SET\_PATH\_LOSS\_REPORTING\_ENABLE BT\_OP(BT\_OGF\_LE, 0x0079) /\* 0x2079 \*/

720

[ 721](structbt__hci__cp__le__set__default__subrate.md)struct [bt\_hci\_cp\_le\_set\_default\_subrate](structbt__hci__cp__le__set__default__subrate.md) {

[ 722](structbt__hci__cp__le__set__default__subrate.md#a9d8fd7cad5260c8943b90ab50c04b225) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [subrate\_min](structbt__hci__cp__le__set__default__subrate.md#a9d8fd7cad5260c8943b90ab50c04b225);

[ 723](structbt__hci__cp__le__set__default__subrate.md#ad18a8042c38a1b4d83d6fccad1ab5af8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [subrate\_max](structbt__hci__cp__le__set__default__subrate.md#ad18a8042c38a1b4d83d6fccad1ab5af8);

[ 724](structbt__hci__cp__le__set__default__subrate.md#a16adacc30fd5ae00b3944f068b075b1a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_latency](structbt__hci__cp__le__set__default__subrate.md#a16adacc30fd5ae00b3944f068b075b1a);

[ 725](structbt__hci__cp__le__set__default__subrate.md#aff2e682b4c8e5c3078885be126c5b958) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [continuation\_number](structbt__hci__cp__le__set__default__subrate.md#aff2e682b4c8e5c3078885be126c5b958);

[ 726](structbt__hci__cp__le__set__default__subrate.md#a1906f4dd7955200c81093b8f7c5d55c0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [supervision\_timeout](structbt__hci__cp__le__set__default__subrate.md#a1906f4dd7955200c81093b8f7c5d55c0);

727} \_\_packed;

728

[ 729](structbt__hci__cp__le__subrate__request.md)struct [bt\_hci\_cp\_le\_subrate\_request](structbt__hci__cp__le__subrate__request.md) {

[ 730](structbt__hci__cp__le__subrate__request.md#a2595419182358e3386a0fb6e523a3dda) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__subrate__request.md#a2595419182358e3386a0fb6e523a3dda);

[ 731](structbt__hci__cp__le__subrate__request.md#a18ba526d8a843ad9c74c22d0899d9c1f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [subrate\_min](structbt__hci__cp__le__subrate__request.md#a18ba526d8a843ad9c74c22d0899d9c1f);

[ 732](structbt__hci__cp__le__subrate__request.md#a5c95a2bea462fb72d34d6314046041b7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [subrate\_max](structbt__hci__cp__le__subrate__request.md#a5c95a2bea462fb72d34d6314046041b7);

[ 733](structbt__hci__cp__le__subrate__request.md#a04ccc83303baabf30b663983883e7e77) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_latency](structbt__hci__cp__le__subrate__request.md#a04ccc83303baabf30b663983883e7e77);

[ 734](structbt__hci__cp__le__subrate__request.md#ab32a92ed52266c6b7d6d9ab08787e770) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [continuation\_number](structbt__hci__cp__le__subrate__request.md#ab32a92ed52266c6b7d6d9ab08787e770);

[ 735](structbt__hci__cp__le__subrate__request.md#a60bcbe27605063725422a0b1c35f21e7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [supervision\_timeout](structbt__hci__cp__le__subrate__request.md#a60bcbe27605063725422a0b1c35f21e7);

736} \_\_packed;

737

[ 738](hci__types_8h.md#a05c5f2cb7028e3ae831047e53b767836)#define BT\_HCI\_OP\_LE\_SET\_DEFAULT\_SUBRATE BT\_OP(BT\_OGF\_LE, 0x007D) /\* 0x207D \*/

[ 739](hci__types_8h.md#af6825cfdac02620af56b8c747d1ef308)#define BT\_HCI\_OP\_LE\_SUBRATE\_REQUEST BT\_OP(BT\_OGF\_LE, 0x007E) /\* 0x207E \*/

740

[ 741](hci__types_8h.md#a252ef06a33818e117fc7f8146413cbd0)#define BT\_HCI\_CTL\_TO\_HOST\_FLOW\_DISABLE 0x00

[ 742](hci__types_8h.md#a4231ce6514091008191d5843b2c0b452)#define BT\_HCI\_CTL\_TO\_HOST\_FLOW\_ENABLE 0x01

[ 743](hci__types_8h.md#abe87fa64cb529d2cfe7ddf4fa045d3b5)#define BT\_HCI\_OP\_SET\_CTL\_TO\_HOST\_FLOW BT\_OP(BT\_OGF\_BASEBAND, 0x0031) /\* 0x0c31 \*/

[ 744](structbt__hci__cp__set__ctl__to__host__flow.md)struct [bt\_hci\_cp\_set\_ctl\_to\_host\_flow](structbt__hci__cp__set__ctl__to__host__flow.md) {

[ 745](structbt__hci__cp__set__ctl__to__host__flow.md#a75b614de1ab1fbfc6aa9c11d833976a6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flow\_enable](structbt__hci__cp__set__ctl__to__host__flow.md#a75b614de1ab1fbfc6aa9c11d833976a6);

746} \_\_packed;

747

[ 748](hci__types_8h.md#a2e05f146890ad81be27dca91250bf69d)#define BT\_HCI\_OP\_HOST\_BUFFER\_SIZE BT\_OP(BT\_OGF\_BASEBAND, 0x0033) /\* 0x0c33 \*/

[ 749](structbt__hci__cp__host__buffer__size.md)struct [bt\_hci\_cp\_host\_buffer\_size](structbt__hci__cp__host__buffer__size.md) {

[ 750](structbt__hci__cp__host__buffer__size.md#a07039a81ba81c700a26009ea407744b6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [acl\_mtu](structbt__hci__cp__host__buffer__size.md#a07039a81ba81c700a26009ea407744b6);

[ 751](structbt__hci__cp__host__buffer__size.md#a1b1d8c7f60ecbb13699b815bc8fca550) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sco\_mtu](structbt__hci__cp__host__buffer__size.md#a1b1d8c7f60ecbb13699b815bc8fca550);

[ 752](structbt__hci__cp__host__buffer__size.md#a8240837fecc7c50461724b697f0eda47) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [acl\_pkts](structbt__hci__cp__host__buffer__size.md#a8240837fecc7c50461724b697f0eda47);

[ 753](structbt__hci__cp__host__buffer__size.md#a943252480194e1a8608951be08b6b91c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sco\_pkts](structbt__hci__cp__host__buffer__size.md#a943252480194e1a8608951be08b6b91c);

754} \_\_packed;

755

[ 756](structbt__hci__handle__count.md)struct [bt\_hci\_handle\_count](structbt__hci__handle__count.md) {

[ 757](structbt__hci__handle__count.md#acacc000905835724b7fe882a8ad85f82) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__handle__count.md#acacc000905835724b7fe882a8ad85f82);

[ 758](structbt__hci__handle__count.md#a71577f376985909744fa14f246e69e1d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [count](structbt__hci__handle__count.md#a71577f376985909744fa14f246e69e1d);

759} \_\_packed;

760

[ 761](hci__types_8h.md#a6c7afa8e3b324714bc5f8dce9702604d)#define BT\_HCI\_OP\_HOST\_NUM\_COMPLETED\_PACKETS BT\_OP(BT\_OGF\_BASEBAND, 0x0035) /\* 0x0c35 \*/

[ 762](structbt__hci__cp__host__num__completed__packets.md)struct [bt\_hci\_cp\_host\_num\_completed\_packets](structbt__hci__cp__host__num__completed__packets.md) {

[ 763](structbt__hci__cp__host__num__completed__packets.md#a43a42e52757de9ec307e8a828dff416f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_handles](structbt__hci__cp__host__num__completed__packets.md#a43a42e52757de9ec307e8a828dff416f);

[ 764](structbt__hci__cp__host__num__completed__packets.md#a127f146b4967de49bc74b90ce1643eb7) struct [bt\_hci\_handle\_count](structbt__hci__handle__count.md) [h](structbt__hci__cp__host__num__completed__packets.md#a127f146b4967de49bc74b90ce1643eb7)[0];

765} \_\_packed;

766

[ 767](hci__types_8h.md#a04985a29d0f131c09aeb9769689b727b)#define BT\_HCI\_OP\_WRITE\_INQUIRY\_MODE BT\_OP(BT\_OGF\_BASEBAND, 0x0045) /\* 0x0c45 \*/

[ 768](structbt__hci__cp__write__inquiry__mode.md)struct [bt\_hci\_cp\_write\_inquiry\_mode](structbt__hci__cp__write__inquiry__mode.md) {

[ 769](structbt__hci__cp__write__inquiry__mode.md#a827e138b7faaec54ec84a1cc1e0c480f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mode](structbt__hci__cp__write__inquiry__mode.md#a827e138b7faaec54ec84a1cc1e0c480f);

770} \_\_packed;

771

[ 772](hci__types_8h.md#ac7a73c5e38a2308d56f0dbaaf0a4795b)#define BT\_HCI\_OP\_WRITE\_SSP\_MODE BT\_OP(BT\_OGF\_BASEBAND, 0x0056) /\* 0x0c56 \*/

[ 773](structbt__hci__cp__write__ssp__mode.md)struct [bt\_hci\_cp\_write\_ssp\_mode](structbt__hci__cp__write__ssp__mode.md) {

[ 774](structbt__hci__cp__write__ssp__mode.md#a8ebf7f7890adec53aa8c2307d2b1a33f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mode](structbt__hci__cp__write__ssp__mode.md#a8ebf7f7890adec53aa8c2307d2b1a33f);

775} \_\_packed;

776

[ 777](hci__types_8h.md#af5d2954950e00dfd5a69fc19db0fe530)#define BT\_HCI\_OP\_SET\_EVENT\_MASK\_PAGE\_2 BT\_OP(BT\_OGF\_BASEBAND, 0x0063) /\* 0x0c63 \*/

[ 778](structbt__hci__cp__set__event__mask__page__2.md)struct [bt\_hci\_cp\_set\_event\_mask\_page\_2](structbt__hci__cp__set__event__mask__page__2.md) {

[ 779](structbt__hci__cp__set__event__mask__page__2.md#aacf1308d0892226e2c10216a07cd1fcc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [events\_page\_2](structbt__hci__cp__set__event__mask__page__2.md#aacf1308d0892226e2c10216a07cd1fcc)[8];

780} \_\_packed;

781

[ 782](hci__types_8h.md#a2afc45fe32acff87265d36865c8d0b17)#define BT\_HCI\_OP\_LE\_WRITE\_LE\_HOST\_SUPP BT\_OP(BT\_OGF\_BASEBAND, 0x006d) /\* 0x0c6d \*/

[ 783](structbt__hci__cp__write__le__host__supp.md)struct [bt\_hci\_cp\_write\_le\_host\_supp](structbt__hci__cp__write__le__host__supp.md) {

[ 784](structbt__hci__cp__write__le__host__supp.md#ace1838a80b6061231b536f36e8999ac0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [le](structbt__hci__cp__write__le__host__supp.md#ace1838a80b6061231b536f36e8999ac0);

[ 785](structbt__hci__cp__write__le__host__supp.md#ad2c27c0f98b2334490022e90563e1271) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [simul](structbt__hci__cp__write__le__host__supp.md#ad2c27c0f98b2334490022e90563e1271);

786} \_\_packed;

787

[ 788](hci__types_8h.md#a0480dd89b0f851d0a791b97138b01a5b)#define BT\_HCI\_OP\_WRITE\_SC\_HOST\_SUPP BT\_OP(BT\_OGF\_BASEBAND, 0x007a) /\* 0x0c7a \*/

[ 789](structbt__hci__cp__write__sc__host__supp.md)struct [bt\_hci\_cp\_write\_sc\_host\_supp](structbt__hci__cp__write__sc__host__supp.md) {

[ 790](structbt__hci__cp__write__sc__host__supp.md#a48ef951f4de05c5772be5c08edca7cec) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sc\_support](structbt__hci__cp__write__sc__host__supp.md#a48ef951f4de05c5772be5c08edca7cec);

791} \_\_packed;

792

[ 793](hci__types_8h.md#a0ea6134bcd33e24b068f35d080cdc4e0)#define BT\_HCI\_OP\_READ\_AUTH\_PAYLOAD\_TIMEOUT BT\_OP(BT\_OGF\_BASEBAND, 0x007b) /\* 0x0c7b \*/

[ 794](structbt__hci__cp__read__auth__payload__timeout.md)struct [bt\_hci\_cp\_read\_auth\_payload\_timeout](structbt__hci__cp__read__auth__payload__timeout.md) {

[ 795](structbt__hci__cp__read__auth__payload__timeout.md#adcdd657feb3ea6b892e2a5034365dd77) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__read__auth__payload__timeout.md#adcdd657feb3ea6b892e2a5034365dd77);

796} \_\_packed;

797

[ 798](structbt__hci__rp__read__auth__payload__timeout.md)struct [bt\_hci\_rp\_read\_auth\_payload\_timeout](structbt__hci__rp__read__auth__payload__timeout.md) {

[ 799](structbt__hci__rp__read__auth__payload__timeout.md#a3eadeab880eb75c914be654dbc685f3f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__auth__payload__timeout.md#a3eadeab880eb75c914be654dbc685f3f);

[ 800](structbt__hci__rp__read__auth__payload__timeout.md#ab53b7e03c68dcd040e38fdc7429b2d3b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__read__auth__payload__timeout.md#ab53b7e03c68dcd040e38fdc7429b2d3b);

[ 801](structbt__hci__rp__read__auth__payload__timeout.md#ab4092720dad9a01f4e179eb2f0112aed) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [auth\_payload\_timeout](structbt__hci__rp__read__auth__payload__timeout.md#ab4092720dad9a01f4e179eb2f0112aed);

802} \_\_packed;

803

[ 804](hci__types_8h.md#ae74450b7b643f947fa2e83a80e0e2fae)#define BT\_HCI\_OP\_WRITE\_AUTH\_PAYLOAD\_TIMEOUT BT\_OP(BT\_OGF\_BASEBAND, 0x007c) /\* 0x0c7c \*/

[ 805](structbt__hci__cp__write__auth__payload__timeout.md)struct [bt\_hci\_cp\_write\_auth\_payload\_timeout](structbt__hci__cp__write__auth__payload__timeout.md) {

[ 806](structbt__hci__cp__write__auth__payload__timeout.md#ad99d5b9f416f11492ac0f412b400aeb6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__write__auth__payload__timeout.md#ad99d5b9f416f11492ac0f412b400aeb6);

[ 807](structbt__hci__cp__write__auth__payload__timeout.md#a385c88012b09ec561b9ba7edaadeb574) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [auth\_payload\_timeout](structbt__hci__cp__write__auth__payload__timeout.md#a385c88012b09ec561b9ba7edaadeb574);

808} \_\_packed;

809

[ 810](structbt__hci__rp__write__auth__payload__timeout.md)struct [bt\_hci\_rp\_write\_auth\_payload\_timeout](structbt__hci__rp__write__auth__payload__timeout.md) {

[ 811](structbt__hci__rp__write__auth__payload__timeout.md#af1783a29e6a167fc20b62bd273215b35) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__write__auth__payload__timeout.md#af1783a29e6a167fc20b62bd273215b35);

[ 812](structbt__hci__rp__write__auth__payload__timeout.md#a467c6585c913dba03dcfdf5bf4fa688e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__write__auth__payload__timeout.md#a467c6585c913dba03dcfdf5bf4fa688e);

813} \_\_packed;

814

[ 815](hci__types_8h.md#abc80a803d0e540541bcd889772e59940)#define BT\_HCI\_OP\_CONFIGURE\_DATA\_PATH BT\_OP(BT\_OGF\_BASEBAND, 0x0083) /\* 0x0c83 \*/

[ 816](structbt__hci__cp__configure__data__path.md)struct [bt\_hci\_cp\_configure\_data\_path](structbt__hci__cp__configure__data__path.md) {

[ 817](structbt__hci__cp__configure__data__path.md#a528ba2bd5a220d1b7db064f8b51a8718) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_path\_dir](structbt__hci__cp__configure__data__path.md#a528ba2bd5a220d1b7db064f8b51a8718);

[ 818](structbt__hci__cp__configure__data__path.md#a92967e6b5258b2acd6d82bfbfb8b7940) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_path\_id](structbt__hci__cp__configure__data__path.md#a92967e6b5258b2acd6d82bfbfb8b7940);

[ 819](structbt__hci__cp__configure__data__path.md#a2573fe029e1774bf5fa7e8cffff08cec) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [vs\_config\_len](structbt__hci__cp__configure__data__path.md#a2573fe029e1774bf5fa7e8cffff08cec);

[ 820](structbt__hci__cp__configure__data__path.md#aa79c4aa6603b09f49a8c7f216f135e6e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [vs\_config](structbt__hci__cp__configure__data__path.md#aa79c4aa6603b09f49a8c7f216f135e6e)[0];

821} \_\_packed;

822

[ 823](structbt__hci__rp__configure__data__path.md)struct [bt\_hci\_rp\_configure\_data\_path](structbt__hci__rp__configure__data__path.md) {

[ 824](structbt__hci__rp__configure__data__path.md#a10cfe9bf5a7be202706957d7b8e1f371) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__configure__data__path.md#a10cfe9bf5a7be202706957d7b8e1f371);

825} \_\_packed;

826

827/\* HCI version from Assigned Numbers \*/

[ 828](hci__types_8h.md#a4947ee8a84f7cd81e242ee812b5b8760)#define BT\_HCI\_VERSION\_1\_0B 0

[ 829](hci__types_8h.md#a0fac5f104d8ab1539e84a900aafa9e43)#define BT\_HCI\_VERSION\_1\_1 1

[ 830](hci__types_8h.md#afe6fd8249a97d3762fe454bfb7eab021)#define BT\_HCI\_VERSION\_1\_2 2

[ 831](hci__types_8h.md#afc0d24e2ba5e6b992aec81104cbf035e)#define BT\_HCI\_VERSION\_2\_0 3

[ 832](hci__types_8h.md#a98d73e8f548d5ae7eddff91a3e647aae)#define BT\_HCI\_VERSION\_2\_1 4

[ 833](hci__types_8h.md#acaf91cc6895552243c5b85c2fc007db5)#define BT\_HCI\_VERSION\_3\_0 5

[ 834](hci__types_8h.md#aeb77e725323c3f31c90482e676dad08a)#define BT\_HCI\_VERSION\_4\_0 6

[ 835](hci__types_8h.md#a08cca779ede398a551359efccdaf3090)#define BT\_HCI\_VERSION\_4\_1 7

[ 836](hci__types_8h.md#aa398d6e6fcca0b427a2ccd3a0a343835)#define BT\_HCI\_VERSION\_4\_2 8

[ 837](hci__types_8h.md#a9a203a5a633d28c644b30125d437701a)#define BT\_HCI\_VERSION\_5\_0 9

[ 838](hci__types_8h.md#acfa0dbddfde8ee82b114dd34ff75c5bc)#define BT\_HCI\_VERSION\_5\_1 10

[ 839](hci__types_8h.md#aa4828a916c53d97de0541992d0359c09)#define BT\_HCI\_VERSION\_5\_2 11

[ 840](hci__types_8h.md#a37b04f40e68e821a1aac3b785903b379)#define BT\_HCI\_VERSION\_5\_3 12

[ 841](hci__types_8h.md#ae8eadab2b7be415160f145bd63bae367)#define BT\_HCI\_VERSION\_5\_4 13

[ 842](hci__types_8h.md#a66f6fbbc23991a16aa8bcfa2998f025f)#define BT\_HCI\_VERSION\_6\_0 14

843

[ 844](hci__types_8h.md#a195b8faf6d7d3e4f1b528185c73b4d67)#define BT\_HCI\_OP\_READ\_LOCAL\_VERSION\_INFO BT\_OP(BT\_OGF\_INFO, 0x0001) /\* 0x1001 \*/

[ 845](structbt__hci__rp__read__local__version__info.md)struct [bt\_hci\_rp\_read\_local\_version\_info](structbt__hci__rp__read__local__version__info.md) {

[ 846](structbt__hci__rp__read__local__version__info.md#a935f990f7c28f7c89660c2b8ab975f43) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__local__version__info.md#a935f990f7c28f7c89660c2b8ab975f43);

[ 847](structbt__hci__rp__read__local__version__info.md#a1cc521426e530344a328e935152dd488) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [hci\_version](structbt__hci__rp__read__local__version__info.md#a1cc521426e530344a328e935152dd488);

[ 848](structbt__hci__rp__read__local__version__info.md#a04161ed3cc0b9c3c442e3464501ce118) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [hci\_revision](structbt__hci__rp__read__local__version__info.md#a04161ed3cc0b9c3c442e3464501ce118);

[ 849](structbt__hci__rp__read__local__version__info.md#a634641751852f66aabb408bf1b4d0cd2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [lmp\_version](structbt__hci__rp__read__local__version__info.md#a634641751852f66aabb408bf1b4d0cd2);

[ 850](structbt__hci__rp__read__local__version__info.md#a7cd6ba190137eaf7c4eb9c2d7e5b36ce) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [manufacturer](structbt__hci__rp__read__local__version__info.md#a7cd6ba190137eaf7c4eb9c2d7e5b36ce);

[ 851](structbt__hci__rp__read__local__version__info.md#a43f29cf08a2399e818bfa441c6b7a1f3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [lmp\_subversion](structbt__hci__rp__read__local__version__info.md#a43f29cf08a2399e818bfa441c6b7a1f3);

852} \_\_packed;

853

[ 854](hci__types_8h.md#ac0d7533d221db0fa44cfb83135dfcc6a)#define BT\_HCI\_OP\_READ\_SUPPORTED\_COMMANDS BT\_OP(BT\_OGF\_INFO, 0x0002) /\* 0x1002 \*/

[ 855](structbt__hci__rp__read__supported__commands.md)struct [bt\_hci\_rp\_read\_supported\_commands](structbt__hci__rp__read__supported__commands.md) {

[ 856](structbt__hci__rp__read__supported__commands.md#a3d36d892f83cfcb1d2fc955ec71ff061) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__supported__commands.md#a3d36d892f83cfcb1d2fc955ec71ff061);

[ 857](structbt__hci__rp__read__supported__commands.md#afd0dc4411a4c7692515139392bffedd0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [commands](structbt__hci__rp__read__supported__commands.md#afd0dc4411a4c7692515139392bffedd0)[64];

858} \_\_packed;

859

[ 860](hci__types_8h.md#a882f120b35a9baa2f70bc33ef5ced6d3)#define BT\_HCI\_OP\_READ\_LOCAL\_EXT\_FEATURES BT\_OP(BT\_OGF\_INFO, 0x0004) /\* 0x1004 \*/

[ 861](structbt__hci__cp__read__local__ext__features.md)struct [bt\_hci\_cp\_read\_local\_ext\_features](structbt__hci__cp__read__local__ext__features.md) {

[ 862](structbt__hci__cp__read__local__ext__features.md#a79c6a6a6f1026a7e9ee774183ea7e132) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [page](structbt__hci__cp__read__local__ext__features.md#a79c6a6a6f1026a7e9ee774183ea7e132);

863};

[ 864](structbt__hci__rp__read__local__ext__features.md)struct [bt\_hci\_rp\_read\_local\_ext\_features](structbt__hci__rp__read__local__ext__features.md) {

[ 865](structbt__hci__rp__read__local__ext__features.md#a9011f2c89f75939fa92fcf249d2203da) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__local__ext__features.md#a9011f2c89f75939fa92fcf249d2203da);

[ 866](structbt__hci__rp__read__local__ext__features.md#a7e3669651dc2c2ed9541b7e4945a27f9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [page](structbt__hci__rp__read__local__ext__features.md#a7e3669651dc2c2ed9541b7e4945a27f9);

[ 867](structbt__hci__rp__read__local__ext__features.md#a3532e208b3fd347db80d8c55eade3c2d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_page](structbt__hci__rp__read__local__ext__features.md#a3532e208b3fd347db80d8c55eade3c2d);

[ 868](structbt__hci__rp__read__local__ext__features.md#a669e8c6faa4e45f472e4f8a3ebb03050) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ext\_features](structbt__hci__rp__read__local__ext__features.md#a669e8c6faa4e45f472e4f8a3ebb03050)[8];

869} \_\_packed;

870

[ 871](hci__types_8h.md#a8524505dff48ceb41c008c8662da6408)#define BT\_HCI\_OP\_READ\_LOCAL\_FEATURES BT\_OP(BT\_OGF\_INFO, 0x0003) /\* 0x1003 \*/

[ 872](structbt__hci__rp__read__local__features.md)struct [bt\_hci\_rp\_read\_local\_features](structbt__hci__rp__read__local__features.md) {

[ 873](structbt__hci__rp__read__local__features.md#a0ff73da5704ada47f8f79c113254820d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__local__features.md#a0ff73da5704ada47f8f79c113254820d);

[ 874](structbt__hci__rp__read__local__features.md#ae660b4a772f96bf72bd08124bf26b352) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [features](structbt__hci__rp__read__local__features.md#ae660b4a772f96bf72bd08124bf26b352)[8];

875} \_\_packed;

876

[ 877](hci__types_8h.md#acd5d9ecda744969d4692e6ebface2e53)#define BT\_HCI\_OP\_READ\_BUFFER\_SIZE BT\_OP(BT\_OGF\_INFO, 0x0005) /\* 0x1005 \*/

[ 878](structbt__hci__rp__read__buffer__size.md)struct [bt\_hci\_rp\_read\_buffer\_size](structbt__hci__rp__read__buffer__size.md) {

[ 879](structbt__hci__rp__read__buffer__size.md#a6adf126acfcec722dc078d097d2b2ba8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__buffer__size.md#a6adf126acfcec722dc078d097d2b2ba8);

[ 880](structbt__hci__rp__read__buffer__size.md#aba3f1597c929e3721c769beb98000218) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [acl\_max\_len](structbt__hci__rp__read__buffer__size.md#aba3f1597c929e3721c769beb98000218);

[ 881](structbt__hci__rp__read__buffer__size.md#a7d475559145f469006b2ef147704cd99) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sco\_max\_len](structbt__hci__rp__read__buffer__size.md#a7d475559145f469006b2ef147704cd99);

[ 882](structbt__hci__rp__read__buffer__size.md#a87ff361282be71aa60c7f88c50a7492f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [acl\_max\_num](structbt__hci__rp__read__buffer__size.md#a87ff361282be71aa60c7f88c50a7492f);

[ 883](structbt__hci__rp__read__buffer__size.md#abc01fa1df6d787f0a2cb865daed5f4cc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sco\_max\_num](structbt__hci__rp__read__buffer__size.md#abc01fa1df6d787f0a2cb865daed5f4cc);

884} \_\_packed;

885

[ 886](hci__types_8h.md#a4ba1bf2078ac12686e2a7727f637f70b)#define BT\_HCI\_OP\_READ\_BD\_ADDR BT\_OP(BT\_OGF\_INFO, 0x0009) /\* 0x1009 \*/

[ 887](structbt__hci__rp__read__bd__addr.md)struct [bt\_hci\_rp\_read\_bd\_addr](structbt__hci__rp__read__bd__addr.md) {

[ 888](structbt__hci__rp__read__bd__addr.md#a5230de2a3a6c4161d076b59901790e1e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__bd__addr.md#a5230de2a3a6c4161d076b59901790e1e);

[ 889](structbt__hci__rp__read__bd__addr.md#aec2c022a465982a3868100699c95f4e6) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__rp__read__bd__addr.md#aec2c022a465982a3868100699c95f4e6);

890} \_\_packed;

891

892/\* logic transport type bits as returned when reading supported codecs \*/

[ 893](hci__types_8h.md#a89eeffc2f46c776ecdb5eea81cb1f47a)#define BT\_HCI\_CODEC\_TRANSPORT\_MASK\_BREDR\_ACL BIT(0)

[ 894](hci__types_8h.md#ab50b70f27bd9beb4da6fe8d4b91398c1)#define BT\_HCI\_CODEC\_TRANSPORT\_MASK\_BREDR\_SCO BIT(1)

[ 895](hci__types_8h.md#a38dd1118554de13f3f6f2853900212c5)#define BT\_HCI\_CODEC\_TRANSPORT\_MASK\_LE\_CIS BIT(2)

[ 896](hci__types_8h.md#a7d90fc1df2260a4067c3eb4ab169c406)#define BT\_HCI\_CODEC\_TRANSPORT\_MASK\_LE\_BIS BIT(3)

897

898/\* logic transport types for reading codec capabilities and controller delays \*/

[ 899](hci__types_8h.md#a73dfca6788b272380e6920d2907bf43f)#define BT\_HCI\_LOGICAL\_TRANSPORT\_TYPE\_BREDR\_ACL 0x00

[ 900](hci__types_8h.md#ad10d8c5ffd49cb183731a9ba97c0e058)#define BT\_HCI\_LOGICAL\_TRANSPORT\_TYPE\_BREDR\_SCO 0x01

[ 901](hci__types_8h.md#a5e53f28cedf59f18ce8d494f16933b3c)#define BT\_HCI\_LOGICAL\_TRANSPORT\_TYPE\_LE\_CIS 0x02

[ 902](hci__types_8h.md#a560cb22e5f39c144e3d477eea5c32beb)#define BT\_HCI\_LOGICAL\_TRANSPORT\_TYPE\_LE\_BIS 0x03

903

904/\* audio datapath directions \*/

[ 905](hci__types_8h.md#a0f74c19fabbcb3088e1a819d33a05a1c)#define BT\_HCI\_DATAPATH\_DIR\_HOST\_TO\_CTLR 0x00

[ 906](hci__types_8h.md#af8d89c712a3d27f9b6f92a31bea2a8c3)#define BT\_HCI\_DATAPATH\_DIR\_CTLR\_TO\_HOST 0x01

907

908/\* audio datapath IDs \*/

[ 909](hci__types_8h.md#a5f748cb264265b9fc12f146ba47fa14c)#define BT\_HCI\_DATAPATH\_ID\_HCI 0x00

[ 910](hci__types_8h.md#a0382b1713c7b2a774a8f004b6d1bc33f)#define BT\_HCI\_DATAPATH\_ID\_VS 0x01

[ 911](hci__types_8h.md#abf755f2839b36a3ac3431bff04193b2f)#define BT\_HCI\_DATAPATH\_ID\_VS\_END 0xfe

912

913/\* coding format assigned numbers, used for codec IDs \*/

[ 914](hci__types_8h.md#a4f4939e7fa43ab73861f64d25b6549d8)#define BT\_HCI\_CODING\_FORMAT\_ULAW\_LOG 0x00

[ 915](hci__types_8h.md#a36f18d10467a580e9864eb8629b8ce01)#define BT\_HCI\_CODING\_FORMAT\_ALAW\_LOG 0x01

[ 916](hci__types_8h.md#a80dc369e54038df30f44ca4c13ee14d6)#define BT\_HCI\_CODING\_FORMAT\_CVSD 0x02

[ 917](hci__types_8h.md#ad93af498e2265c180a01055eca2a4de0)#define BT\_HCI\_CODING\_FORMAT\_TRANSPARENT 0x03

[ 918](hci__types_8h.md#a2630de3f8cc3ccc3d81f0f2fa4084587)#define BT\_HCI\_CODING\_FORMAT\_LINEAR\_PCM 0x04

[ 919](hci__types_8h.md#a9178f80b7783c9cffb4574667d3033af)#define BT\_HCI\_CODING\_FORMAT\_MSBC 0x05

[ 920](hci__types_8h.md#a1fa62d6f28ef56ebe9c18d5ab86fbf8e)#define BT\_HCI\_CODING\_FORMAT\_LC3 0x06

[ 921](hci__types_8h.md#a405e22871772b5155f99774178e4093d)#define BT\_HCI\_CODING\_FORMAT\_G729A 0x07

[ 922](hci__types_8h.md#a46839c453b81e80fb8e578f89dc31864)#define BT\_HCI\_CODING\_FORMAT\_VS 0xFF

923

924

[ 925](hci__types_8h.md#a8755487f4672f196051cc513894e4603)#define BT\_HCI\_OP\_READ\_CODECS BT\_OP(BT\_OGF\_INFO, 0x000b) /\* 0x100b \*/

[ 926](structbt__hci__std__codec__info.md)struct [bt\_hci\_std\_codec\_info](structbt__hci__std__codec__info.md) {

[ 927](structbt__hci__std__codec__info.md#a56e21eca5bbc83cb081aea1c67a7a60d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [codec\_id](structbt__hci__std__codec__info.md#a56e21eca5bbc83cb081aea1c67a7a60d);

928} \_\_packed;

[ 929](structbt__hci__std__codecs.md)struct [bt\_hci\_std\_codecs](structbt__hci__std__codecs.md) {

[ 930](structbt__hci__std__codecs.md#ad3e63bf445bb6b8e654baa8490cdf547) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_codecs](structbt__hci__std__codecs.md#ad3e63bf445bb6b8e654baa8490cdf547);

[ 931](structbt__hci__std__codecs.md#a32767e90384ef74a3e740597eacfcf53) struct [bt\_hci\_std\_codec\_info](structbt__hci__std__codec__info.md) [codec\_info](structbt__hci__std__codecs.md#a32767e90384ef74a3e740597eacfcf53)[0];

932} \_\_packed;

[ 933](structbt__hci__vs__codec__info.md)struct [bt\_hci\_vs\_codec\_info](structbt__hci__vs__codec__info.md) {

[ 934](structbt__hci__vs__codec__info.md#a8170dac825b76f3dfb5fde5eed04c4c0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [company\_id](structbt__hci__vs__codec__info.md#a8170dac825b76f3dfb5fde5eed04c4c0);

[ 935](structbt__hci__vs__codec__info.md#a3c7eea7bae36c7a63457051401526382) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [codec\_id](structbt__hci__vs__codec__info.md#a3c7eea7bae36c7a63457051401526382);

936} \_\_packed;

[ 937](structbt__hci__vs__codecs.md)struct [bt\_hci\_vs\_codecs](structbt__hci__vs__codecs.md) {

[ 938](structbt__hci__vs__codecs.md#a2caf18ce5905e3962da000f3b00b623f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_codecs](structbt__hci__vs__codecs.md#a2caf18ce5905e3962da000f3b00b623f);

[ 939](structbt__hci__vs__codecs.md#a4e72426599d5bc617fde4f1a4a095527) struct [bt\_hci\_vs\_codec\_info](structbt__hci__vs__codec__info.md) [codec\_info](structbt__hci__vs__codecs.md#a4e72426599d5bc617fde4f1a4a095527)[0];

940} \_\_packed;

[ 941](structbt__hci__rp__read__codecs.md)struct [bt\_hci\_rp\_read\_codecs](structbt__hci__rp__read__codecs.md) {

[ 942](structbt__hci__rp__read__codecs.md#a017182988634c6acbfbfdd7c9609f5dc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__codecs.md#a017182988634c6acbfbfdd7c9609f5dc);

943 /\* other fields filled in dynamically \*/

[ 944](structbt__hci__rp__read__codecs.md#a44e615f375b35cce9f949562555c429b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [codecs](structbt__hci__rp__read__codecs.md#a44e615f375b35cce9f949562555c429b)[0];

945} \_\_packed;

946

[ 947](hci__types_8h.md#acb09b1a94453c1c341decabc029bbc04)#define BT\_HCI\_OP\_READ\_CODECS\_V2 BT\_OP(BT\_OGF\_INFO, 0x000d) /\* 0x100d \*/

[ 948](structbt__hci__std__codec__info__v2.md)struct [bt\_hci\_std\_codec\_info\_v2](structbt__hci__std__codec__info__v2.md) {

[ 949](structbt__hci__std__codec__info__v2.md#ae82a0896904c7feb2634579b393bf05e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [codec\_id](structbt__hci__std__codec__info__v2.md#ae82a0896904c7feb2634579b393bf05e);

[ 950](structbt__hci__std__codec__info__v2.md#aea766ba4b911223eeb351e0123e54f5f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [transports](structbt__hci__std__codec__info__v2.md#aea766ba4b911223eeb351e0123e54f5f); /\* bitmap \*/

951} \_\_packed;

[ 952](structbt__hci__std__codecs__v2.md)struct [bt\_hci\_std\_codecs\_v2](structbt__hci__std__codecs__v2.md) {

[ 953](structbt__hci__std__codecs__v2.md#ab14fdde478e290235f68aae375969c09) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_codecs](structbt__hci__std__codecs__v2.md#ab14fdde478e290235f68aae375969c09);

[ 954](structbt__hci__std__codecs__v2.md#aafdb6d96d99063a7a447d80e1830a624) struct [bt\_hci\_std\_codec\_info\_v2](structbt__hci__std__codec__info__v2.md) [codec\_info](structbt__hci__std__codecs__v2.md#aafdb6d96d99063a7a447d80e1830a624)[0];

955} \_\_packed;

[ 956](structbt__hci__vs__codec__info__v2.md)struct [bt\_hci\_vs\_codec\_info\_v2](structbt__hci__vs__codec__info__v2.md) {

[ 957](structbt__hci__vs__codec__info__v2.md#aa6ce27b4acd3dff516e4d7ed2e6434bc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [company\_id](structbt__hci__vs__codec__info__v2.md#aa6ce27b4acd3dff516e4d7ed2e6434bc);

[ 958](structbt__hci__vs__codec__info__v2.md#ae7b7d5d65629a1e3039b3c7cf167a9c1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [codec\_id](structbt__hci__vs__codec__info__v2.md#ae7b7d5d65629a1e3039b3c7cf167a9c1);

[ 959](structbt__hci__vs__codec__info__v2.md#ac2a91a045e4b53315850b6d4f1d38b2c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [transports](structbt__hci__vs__codec__info__v2.md#ac2a91a045e4b53315850b6d4f1d38b2c); /\* bitmap \*/

960} \_\_packed;

[ 961](structbt__hci__vs__codecs__v2.md)struct [bt\_hci\_vs\_codecs\_v2](structbt__hci__vs__codecs__v2.md) {

[ 962](structbt__hci__vs__codecs__v2.md#ae4cb3a40401594f8e0f18391b9d31a23) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_codecs](structbt__hci__vs__codecs__v2.md#ae4cb3a40401594f8e0f18391b9d31a23);

[ 963](structbt__hci__vs__codecs__v2.md#a6cd8aa58517d59d565474513f755cfee) struct [bt\_hci\_vs\_codec\_info\_v2](structbt__hci__vs__codec__info__v2.md) [codec\_info](structbt__hci__vs__codecs__v2.md#a6cd8aa58517d59d565474513f755cfee)[0];

964} \_\_packed;

[ 965](structbt__hci__rp__read__codecs__v2.md)struct [bt\_hci\_rp\_read\_codecs\_v2](structbt__hci__rp__read__codecs__v2.md) {

[ 966](structbt__hci__rp__read__codecs__v2.md#a2e9866d0f9fb42b54c406a9ea5890913) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__codecs__v2.md#a2e9866d0f9fb42b54c406a9ea5890913);

967 /\* other fields filled in dynamically \*/

[ 968](structbt__hci__rp__read__codecs__v2.md#a098563f274de085ac97415f1b5e15f3c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [codecs](structbt__hci__rp__read__codecs__v2.md#a098563f274de085ac97415f1b5e15f3c)[0];

969} \_\_packed;

970

[ 971](structbt__hci__cp__codec__id.md)struct [bt\_hci\_cp\_codec\_id](structbt__hci__cp__codec__id.md) {

[ 972](structbt__hci__cp__codec__id.md#aec80c74b12edb9c63330cc5a404eed5d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [coding\_format](structbt__hci__cp__codec__id.md#aec80c74b12edb9c63330cc5a404eed5d);

[ 973](structbt__hci__cp__codec__id.md#a98fd438270a64d843fa27c7c196645df) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [company\_id](structbt__hci__cp__codec__id.md#a98fd438270a64d843fa27c7c196645df);

[ 974](structbt__hci__cp__codec__id.md#a70296440c202544af11db2dc8e80fc5b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [vs\_codec\_id](structbt__hci__cp__codec__id.md#a70296440c202544af11db2dc8e80fc5b);

975} \_\_packed;

976

[ 977](hci__types_8h.md#a4b9e24d16cd92ce6ee1d6444410cfb43)#define BT\_HCI\_OP\_READ\_CODEC\_CAPABILITIES BT\_OP(BT\_OGF\_INFO, 0x000e) /\* 0x100e \*/

[ 978](structbt__hci__cp__read__codec__capabilities.md)struct [bt\_hci\_cp\_read\_codec\_capabilities](structbt__hci__cp__read__codec__capabilities.md) {

[ 979](structbt__hci__cp__read__codec__capabilities.md#ad48b7f228742d86a71dffa314331bbe1) struct [bt\_hci\_cp\_codec\_id](structbt__hci__cp__codec__id.md) [codec\_id](structbt__hci__cp__read__codec__capabilities.md#ad48b7f228742d86a71dffa314331bbe1);

[ 980](structbt__hci__cp__read__codec__capabilities.md#a6479561573172356d7515ef92f75b8d4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [transport](structbt__hci__cp__read__codec__capabilities.md#a6479561573172356d7515ef92f75b8d4);

[ 981](structbt__hci__cp__read__codec__capabilities.md#a237695f4d0a1359d5ce71d831708a69c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [direction](structbt__hci__cp__read__codec__capabilities.md#a237695f4d0a1359d5ce71d831708a69c);

982} \_\_packed;

[ 983](structbt__hci__codec__capability__info.md)struct [bt\_hci\_codec\_capability\_info](structbt__hci__codec__capability__info.md) {

[ 984](structbt__hci__codec__capability__info.md#a24516347742a8fd9f3386d78b66a4e81) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [length](structbt__hci__codec__capability__info.md#a24516347742a8fd9f3386d78b66a4e81);

[ 985](structbt__hci__codec__capability__info.md#ac53f02f2abdb832ed82da35a36abc323) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__hci__codec__capability__info.md#ac53f02f2abdb832ed82da35a36abc323)[0];

986} \_\_packed;

[ 987](structbt__hci__rp__read__codec__capabilities.md)struct [bt\_hci\_rp\_read\_codec\_capabilities](structbt__hci__rp__read__codec__capabilities.md) {

[ 988](structbt__hci__rp__read__codec__capabilities.md#ac224ea998e3af12f97232288266da8d2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__codec__capabilities.md#ac224ea998e3af12f97232288266da8d2);

[ 989](structbt__hci__rp__read__codec__capabilities.md#a71b7df63502bf42a26868e69893ddcfe) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_capabilities](structbt__hci__rp__read__codec__capabilities.md#a71b7df63502bf42a26868e69893ddcfe);

990 /\* other fields filled in dynamically \*/

[ 991](structbt__hci__rp__read__codec__capabilities.md#ae0c84013512c461f3b6231162d6f3020) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [capabilities](structbt__hci__rp__read__codec__capabilities.md#ae0c84013512c461f3b6231162d6f3020)[0];

992} \_\_packed;

993

[ 994](hci__types_8h.md#a9a183b26d18453d5daa6de2dcbe4d9a1)#define BT\_HCI\_OP\_READ\_CTLR\_DELAY BT\_OP(BT\_OGF\_INFO, 0x000f) /\* 0x100f \*/

[ 995](structbt__hci__cp__read__ctlr__delay.md)struct [bt\_hci\_cp\_read\_ctlr\_delay](structbt__hci__cp__read__ctlr__delay.md) {

[ 996](structbt__hci__cp__read__ctlr__delay.md#a2afb9ca8bc2e24cd479b29bc1a53c867) struct [bt\_hci\_cp\_codec\_id](structbt__hci__cp__codec__id.md) [codec\_id](structbt__hci__cp__read__ctlr__delay.md#a2afb9ca8bc2e24cd479b29bc1a53c867);

[ 997](structbt__hci__cp__read__ctlr__delay.md#a60a6a5b87896d0c27d734b56ead58a9b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [transport](structbt__hci__cp__read__ctlr__delay.md#a60a6a5b87896d0c27d734b56ead58a9b);

[ 998](structbt__hci__cp__read__ctlr__delay.md#a5e9f74d4f82809289038da29af0c663d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [direction](structbt__hci__cp__read__ctlr__delay.md#a5e9f74d4f82809289038da29af0c663d);

[ 999](structbt__hci__cp__read__ctlr__delay.md#ac881526b479d5f1717efbe35cdcc7e87) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [codec\_config\_len](structbt__hci__cp__read__ctlr__delay.md#ac881526b479d5f1717efbe35cdcc7e87);

[ 1000](structbt__hci__cp__read__ctlr__delay.md#a6c15d141c40bca8bd095f4a86f5a93bd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [codec\_config](structbt__hci__cp__read__ctlr__delay.md#a6c15d141c40bca8bd095f4a86f5a93bd)[0];

1001} \_\_packed;

[ 1002](structbt__hci__rp__read__ctlr__delay.md)struct [bt\_hci\_rp\_read\_ctlr\_delay](structbt__hci__rp__read__ctlr__delay.md) {

[ 1003](structbt__hci__rp__read__ctlr__delay.md#a2f17081cf767643f3a9ad9d115ef5320) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__ctlr__delay.md#a2f17081cf767643f3a9ad9d115ef5320);

[ 1004](structbt__hci__rp__read__ctlr__delay.md#ab48d1d92cdf9470a93487434b3824d17) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [min\_ctlr\_delay](structbt__hci__rp__read__ctlr__delay.md#ab48d1d92cdf9470a93487434b3824d17)[3];

[ 1005](structbt__hci__rp__read__ctlr__delay.md#a4c468053c4a86d1ab462c1e6f17f1013) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_ctlr\_delay](structbt__hci__rp__read__ctlr__delay.md#a4c468053c4a86d1ab462c1e6f17f1013)[3];

1006} \_\_packed;

1007

[ 1008](hci__types_8h.md#a528902591490d9d20a6966a042254b3a)#define BT\_HCI\_OP\_READ\_RSSI BT\_OP(BT\_OGF\_STATUS, 0x0005) /\* 0x1405 \*/

[ 1009](structbt__hci__cp__read__rssi.md)struct [bt\_hci\_cp\_read\_rssi](structbt__hci__cp__read__rssi.md) {

[ 1010](structbt__hci__cp__read__rssi.md#a0662bc56b344ca2bf9a2dcabe8a13c09) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__read__rssi.md#a0662bc56b344ca2bf9a2dcabe8a13c09);

1011} \_\_packed;

[ 1012](structbt__hci__rp__read__rssi.md)struct [bt\_hci\_rp\_read\_rssi](structbt__hci__rp__read__rssi.md) {

[ 1013](structbt__hci__rp__read__rssi.md#a8f91b69a99bd61a7a59d84b3a9c3f235) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__rssi.md#a8f91b69a99bd61a7a59d84b3a9c3f235);

[ 1014](structbt__hci__rp__read__rssi.md#aa3c4041dd240b1185c7fc8bbef74a17a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__read__rssi.md#aa3c4041dd240b1185c7fc8bbef74a17a);

[ 1015](structbt__hci__rp__read__rssi.md#a1071300bd61fcaab65683187ae393cae) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__hci__rp__read__rssi.md#a1071300bd61fcaab65683187ae393cae);

1016} \_\_packed;

1017

[ 1018](hci__types_8h.md#ab4eedd90a583b3893c77f51aee16e3c0)#define BT\_HCI\_ENCRYPTION\_KEY\_SIZE\_MIN 7

[ 1019](hci__types_8h.md#ae4271fbdb039750aceac7c0712d4f3db)#define BT\_HCI\_ENCRYPTION\_KEY\_SIZE\_MAX 16

1020

[ 1021](hci__types_8h.md#adefeb2117010fa2d53937ce513e28a18)#define BT\_HCI\_OP\_READ\_ENCRYPTION\_KEY\_SIZE BT\_OP(BT\_OGF\_STATUS, 0x0008) /\* 0x1408 \*/

[ 1022](structbt__hci__cp__read__encryption__key__size.md)struct [bt\_hci\_cp\_read\_encryption\_key\_size](structbt__hci__cp__read__encryption__key__size.md) {

[ 1023](structbt__hci__cp__read__encryption__key__size.md#af15765007fd0e2fc4186b54323553019) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__read__encryption__key__size.md#af15765007fd0e2fc4186b54323553019);

1024} \_\_packed;

[ 1025](structbt__hci__rp__read__encryption__key__size.md)struct [bt\_hci\_rp\_read\_encryption\_key\_size](structbt__hci__rp__read__encryption__key__size.md) {

[ 1026](structbt__hci__rp__read__encryption__key__size.md#a17213ccb9179739aa79c3749a2296f65) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__encryption__key__size.md#a17213ccb9179739aa79c3749a2296f65);

[ 1027](structbt__hci__rp__read__encryption__key__size.md#af0b89b2035f956891244b10409be0f51) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__read__encryption__key__size.md#af0b89b2035f956891244b10409be0f51);

[ 1028](structbt__hci__rp__read__encryption__key__size.md#af1cd71c6216b26d460c04a68405f05d5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key\_size](structbt__hci__rp__read__encryption__key__size.md#af1cd71c6216b26d460c04a68405f05d5);

1029} \_\_packed;

1030

1031/\* Bluetooth LE \*/

1032

[ 1033](hci__types_8h.md#aa9a3688473bf15c8845f52a3128362f7)#define BT\_HCI\_OP\_LE\_SET\_EVENT\_MASK BT\_OP(BT\_OGF\_LE, 0x0001) /\* 0x2001 \*/

[ 1034](structbt__hci__cp__le__set__event__mask.md)struct [bt\_hci\_cp\_le\_set\_event\_mask](structbt__hci__cp__le__set__event__mask.md) {

[ 1035](structbt__hci__cp__le__set__event__mask.md#af7de4823aca253f15e57f54ee9b3879e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [events](structbt__hci__cp__le__set__event__mask.md#af7de4823aca253f15e57f54ee9b3879e)[8];

1036} \_\_packed;

1037

[ 1038](hci__types_8h.md#a965e30fec3f9b5956bd2ea38e57b8b00)#define BT\_HCI\_OP\_LE\_READ\_BUFFER\_SIZE BT\_OP(BT\_OGF\_LE, 0x0002) /\* 0x2002 \*/

[ 1039](structbt__hci__rp__le__read__buffer__size.md)struct [bt\_hci\_rp\_le\_read\_buffer\_size](structbt__hci__rp__le__read__buffer__size.md) {

[ 1040](structbt__hci__rp__le__read__buffer__size.md#a90a1206f1dbbefd298e5323ac07691f1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__buffer__size.md#a90a1206f1dbbefd298e5323ac07691f1);

[ 1041](structbt__hci__rp__le__read__buffer__size.md#a8bc64cd8743984cd5a8dedfc86aaee56) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [le\_max\_len](structbt__hci__rp__le__read__buffer__size.md#a8bc64cd8743984cd5a8dedfc86aaee56);

[ 1042](structbt__hci__rp__le__read__buffer__size.md#a3e393d6c51d8c3f8a5d88413198e3f28) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [le\_max\_num](structbt__hci__rp__le__read__buffer__size.md#a3e393d6c51d8c3f8a5d88413198e3f28);

1043} \_\_packed;

1044

[ 1045](hci__types_8h.md#ae4e1d6098793b91ee0e4974886b98336)#define BT\_HCI\_OP\_LE\_READ\_LOCAL\_FEATURES BT\_OP(BT\_OGF\_LE, 0x0003) /\* 0x2003 \*/

[ 1046](structbt__hci__rp__le__read__local__features.md)struct [bt\_hci\_rp\_le\_read\_local\_features](structbt__hci__rp__le__read__local__features.md) {

[ 1047](structbt__hci__rp__le__read__local__features.md#ac1000822beba8a7be0dda684c0a86b6b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__local__features.md#ac1000822beba8a7be0dda684c0a86b6b);

[ 1048](structbt__hci__rp__le__read__local__features.md#ada42e525338cd5526ff211c359c93b3b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [features](structbt__hci__rp__le__read__local__features.md#ada42e525338cd5526ff211c359c93b3b)[8];

1049} \_\_packed;

1050

[ 1051](hci__types_8h.md#af34eced252d01bbc27bd8e19ed4dc80e)#define BT\_HCI\_OP\_LE\_SET\_RANDOM\_ADDRESS BT\_OP(BT\_OGF\_LE, 0x0005) /\* 0x2005 \*/

[ 1052](structbt__hci__cp__le__set__random__address.md)struct [bt\_hci\_cp\_le\_set\_random\_address](structbt__hci__cp__le__set__random__address.md) {

[ 1053](structbt__hci__cp__le__set__random__address.md#a919ef74473f4f86d00595ec8606789d0) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__le__set__random__address.md#a919ef74473f4f86d00595ec8606789d0);

1054} \_\_packed;

1055

[ 1056](hci__types_8h.md#a338499e51470b8910e9f663be8f55db5)#define BT\_HCI\_ADV\_IND 0x00

[ 1057](hci__types_8h.md#afaecb8d6be1b1c0ce98db7edd8bad343)#define BT\_HCI\_ADV\_DIRECT\_IND 0x01

[ 1058](hci__types_8h.md#ae94df1ac3bc14f42be1207531872104a)#define BT\_HCI\_ADV\_SCAN\_IND 0x02

[ 1059](hci__types_8h.md#a48e13ce185bf9612455c49484ff80bb9)#define BT\_HCI\_ADV\_NONCONN\_IND 0x03

[ 1060](hci__types_8h.md#a67c1c0c5349b2de661030138185d7b0d)#define BT\_HCI\_ADV\_DIRECT\_IND\_LOW\_DUTY 0x04

[ 1061](hci__types_8h.md#afb3e678c87b81f9348749f1c5721ce26)#define BT\_HCI\_ADV\_SCAN\_RSP 0x04

1062

[ 1063](hci__types_8h.md#ac89392b0484164812b77360d15d9984b)#define BT\_LE\_ADV\_INTERVAL\_MIN 0x0020

[ 1064](hci__types_8h.md#a6479fb2c964155cfcdd3cc48c3a45618)#define BT\_LE\_ADV\_INTERVAL\_MAX 0x4000

[ 1065](hci__types_8h.md#a607201e55561cdccf34e18ceac0f23b7)#define BT\_LE\_ADV\_INTERVAL\_DEFAULT 0x0800

1066

[ 1067](hci__types_8h.md#af9652f7d96b61e7cc9f44f3d923bd962)#define BT\_LE\_ADV\_CHAN\_MAP\_CHAN\_37 0x01

[ 1068](hci__types_8h.md#a07c18344ec56b22c8a3e902bc53ba191)#define BT\_LE\_ADV\_CHAN\_MAP\_CHAN\_38 0x02

[ 1069](hci__types_8h.md#a14be9af8f16dcdf70aebf251bcfb52f3)#define BT\_LE\_ADV\_CHAN\_MAP\_CHAN\_39 0x04

[ 1070](hci__types_8h.md#af96bfa8c912e66233f64b7cc1844b82e)#define BT\_LE\_ADV\_CHAN\_MAP\_ALL 0x07

1071

[ 1072](hci__types_8h.md#abc1615c8d22ab64844c3f3394023c1b4)#define BT\_LE\_ADV\_FP\_NO\_FILTER 0x00

[ 1073](hci__types_8h.md#aba027e2aeacea1040c3b45ccaeb23d3c)#define BT\_LE\_ADV\_FP\_FILTER\_SCAN\_REQ 0x01

[ 1074](hci__types_8h.md#a5f3d27b78705afc3abff35e353eee9fa)#define BT\_LE\_ADV\_FP\_FILTER\_CONN\_IND 0x02

[ 1075](hci__types_8h.md#a980ff7f9bf7154c7866b5e302a1f2a55)#define BT\_LE\_ADV\_FP\_FILTER\_BOTH 0x03

1076

[ 1077](hci__types_8h.md#a446b6e7a74800ee657f5ddcf1c198d02)#define BT\_HCI\_OP\_LE\_SET\_ADV\_PARAM BT\_OP(BT\_OGF\_LE, 0x0006) /\* 0x2006 \*/

[ 1078](structbt__hci__cp__le__set__adv__param.md)struct [bt\_hci\_cp\_le\_set\_adv\_param](structbt__hci__cp__le__set__adv__param.md) {

[ 1079](structbt__hci__cp__le__set__adv__param.md#a2476c2a1858eab7e9b1449c1901363c4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [min\_interval](structbt__hci__cp__le__set__adv__param.md#a2476c2a1858eab7e9b1449c1901363c4);

[ 1080](structbt__hci__cp__le__set__adv__param.md#ab42c6b8f482e782d09386a3a1758903d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_interval](structbt__hci__cp__le__set__adv__param.md#ab42c6b8f482e782d09386a3a1758903d);

[ 1081](structbt__hci__cp__le__set__adv__param.md#a9b09964156846fd480911dcc2d996a98) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__hci__cp__le__set__adv__param.md#a9b09964156846fd480911dcc2d996a98);

[ 1082](structbt__hci__cp__le__set__adv__param.md#ad8c74cac74254354b314f07df7df1bf0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [own\_addr\_type](structbt__hci__cp__le__set__adv__param.md#ad8c74cac74254354b314f07df7df1bf0);

[ 1083](structbt__hci__cp__le__set__adv__param.md#ac774ef72175e43b083d04ecac263941b) [bt\_addr\_le\_t](structbt__addr__le__t.md) [direct\_addr](structbt__hci__cp__le__set__adv__param.md#ac774ef72175e43b083d04ecac263941b);

[ 1084](structbt__hci__cp__le__set__adv__param.md#a2269ae424e47adddce5aa5f2f5b84c89) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel\_map](structbt__hci__cp__le__set__adv__param.md#a2269ae424e47adddce5aa5f2f5b84c89);

[ 1085](structbt__hci__cp__le__set__adv__param.md#a662c5ae81f25a897a8e597f7227a1e39) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter\_policy](structbt__hci__cp__le__set__adv__param.md#a662c5ae81f25a897a8e597f7227a1e39);

1086} \_\_packed;

1087

[ 1088](hci__types_8h.md#afd47d6bbfd4688383aaa6b5014cf0019)#define BT\_HCI\_OP\_LE\_READ\_ADV\_CHAN\_TX\_POWER BT\_OP(BT\_OGF\_LE, 0x0007) /\* 0x2007 \*/

[ 1089](structbt__hci__rp__le__read__chan__tx__power.md)struct [bt\_hci\_rp\_le\_read\_chan\_tx\_power](structbt__hci__rp__le__read__chan__tx__power.md) {

[ 1090](structbt__hci__rp__le__read__chan__tx__power.md#a09a3805bccdabef399d21b29f84e3a4f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__chan__tx__power.md#a09a3805bccdabef399d21b29f84e3a4f);

[ 1091](structbt__hci__rp__le__read__chan__tx__power.md#a3b6b79d1d28c3e4bf565ae364089f365) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power\_level](structbt__hci__rp__le__read__chan__tx__power.md#a3b6b79d1d28c3e4bf565ae364089f365);

1092} \_\_packed;

1093

[ 1094](hci__types_8h.md#adb8f5236ac1b5eaa4c82d620c78c45aa)#define BT\_HCI\_OP\_LE\_SET\_ADV\_DATA BT\_OP(BT\_OGF\_LE, 0x0008) /\* 0x2008 \*/

[ 1095](structbt__hci__cp__le__set__adv__data.md)struct [bt\_hci\_cp\_le\_set\_adv\_data](structbt__hci__cp__le__set__adv__data.md) {

[ 1096](structbt__hci__cp__le__set__adv__data.md#a664313db17c12adb0de14371e46d26a8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structbt__hci__cp__le__set__adv__data.md#a664313db17c12adb0de14371e46d26a8);

[ 1097](structbt__hci__cp__le__set__adv__data.md#a6fb8734ff5a9b77586b3e283b83985bb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__hci__cp__le__set__adv__data.md#a6fb8734ff5a9b77586b3e283b83985bb)[31];

1098} \_\_packed;

1099

[ 1100](hci__types_8h.md#a81718bfe6796648eb5831f3cd03049c8)#define BT\_HCI\_OP\_LE\_SET\_SCAN\_RSP\_DATA BT\_OP(BT\_OGF\_LE, 0x0009) /\* 0x2009 \*/

[ 1101](structbt__hci__cp__le__set__scan__rsp__data.md)struct [bt\_hci\_cp\_le\_set\_scan\_rsp\_data](structbt__hci__cp__le__set__scan__rsp__data.md) {

[ 1102](structbt__hci__cp__le__set__scan__rsp__data.md#a0fe51008184419c9560bb5d8f287d8be) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structbt__hci__cp__le__set__scan__rsp__data.md#a0fe51008184419c9560bb5d8f287d8be);

[ 1103](structbt__hci__cp__le__set__scan__rsp__data.md#aa719449dc2b85f094081d66398b72c7d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__hci__cp__le__set__scan__rsp__data.md#aa719449dc2b85f094081d66398b72c7d)[31];

1104} \_\_packed;

1105

[ 1106](hci__types_8h.md#ae8361a3ca39019757304034c32391b47)#define BT\_HCI\_LE\_ADV\_DISABLE 0x00

[ 1107](hci__types_8h.md#a6b8140956fbf85bd5aab2f1974b673f9)#define BT\_HCI\_LE\_ADV\_ENABLE 0x01

1108

[ 1109](hci__types_8h.md#a5f218883bda0698b5c52fd6a34d5e9f0)#define BT\_HCI\_OP\_LE\_SET\_ADV\_ENABLE BT\_OP(BT\_OGF\_LE, 0x000a) /\* 0x200a \*/

[ 1110](structbt__hci__cp__le__set__adv__enable.md)struct [bt\_hci\_cp\_le\_set\_adv\_enable](structbt__hci__cp__le__set__adv__enable.md) {

[ 1111](structbt__hci__cp__le__set__adv__enable.md#a15e92d187d586fef560adf9c793f776a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enable](structbt__hci__cp__le__set__adv__enable.md#a15e92d187d586fef560adf9c793f776a);

1112} \_\_packed;

1113

1114/\* Scan types \*/

[ 1115](hci__types_8h.md#a56db98b00b57fd713f8cedbf34e2f8fa)#define BT\_HCI\_OP\_LE\_SET\_SCAN\_PARAM BT\_OP(BT\_OGF\_LE, 0x000b) /\* 0x200b \*/

[ 1116](hci__types_8h.md#a2274aacde21083e9633fe59fbff0df87)#define BT\_HCI\_LE\_SCAN\_PASSIVE 0x00

[ 1117](hci__types_8h.md#ac13c2e39ac1e13cf5cd2cfa248a6f316)#define BT\_HCI\_LE\_SCAN\_ACTIVE 0x01

1118

[ 1119](hci__types_8h.md#a278ccd7cfefd1a46f6de843b722f583a)#define BT\_HCI\_LE\_SCAN\_FP\_BASIC\_NO\_FILTER 0x00

[ 1120](hci__types_8h.md#ac6f3763ab47d20efee1af16d8d019bf3)#define BT\_HCI\_LE\_SCAN\_FP\_BASIC\_FILTER 0x01

[ 1121](hci__types_8h.md#aed7fa63104bbc551bc0dbfa21e38744a)#define BT\_HCI\_LE\_SCAN\_FP\_EXT\_NO\_FILTER 0x02

[ 1122](hci__types_8h.md#a45846e02e2630608b14f62f9b9020f9d)#define BT\_HCI\_LE\_SCAN\_FP\_EXT\_FILTER 0x03

1123

[ 1124](structbt__hci__cp__le__set__scan__param.md)struct [bt\_hci\_cp\_le\_set\_scan\_param](structbt__hci__cp__le__set__scan__param.md) {

[ 1125](structbt__hci__cp__le__set__scan__param.md#ad19a479cc3c27ab24286b537b646261e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [scan\_type](structbt__hci__cp__le__set__scan__param.md#ad19a479cc3c27ab24286b537b646261e);

[ 1126](structbt__hci__cp__le__set__scan__param.md#adcd8be074a8b19e0e7d02c4ea8209c93) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__hci__cp__le__set__scan__param.md#adcd8be074a8b19e0e7d02c4ea8209c93);

[ 1127](structbt__hci__cp__le__set__scan__param.md#a3b5b4767092fc69a63d2219d60722407) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [window](structbt__hci__cp__le__set__scan__param.md#a3b5b4767092fc69a63d2219d60722407);

[ 1128](structbt__hci__cp__le__set__scan__param.md#a694c74a6fc95f767d2e89e6596d51e98) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr\_type](structbt__hci__cp__le__set__scan__param.md#a694c74a6fc95f767d2e89e6596d51e98);

[ 1129](structbt__hci__cp__le__set__scan__param.md#ab7a268e17a5d564d475ff9dee5e6e14b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter\_policy](structbt__hci__cp__le__set__scan__param.md#ab7a268e17a5d564d475ff9dee5e6e14b);

1130} \_\_packed;

1131

[ 1132](hci__types_8h.md#a894cf6904ec16b11f6d930d72d30fce6)#define BT\_HCI\_OP\_LE\_SET\_SCAN\_ENABLE BT\_OP(BT\_OGF\_LE, 0x000c) /\* 0x200c \*/

1133

[ 1134](hci__types_8h.md#a152712b517c9ee0452555408d14bbfa7)#define BT\_HCI\_LE\_SCAN\_DISABLE 0x00

[ 1135](hci__types_8h.md#a6859aeda42fe72b75d5cc1896b7e6afd)#define BT\_HCI\_LE\_SCAN\_ENABLE 0x01

1136

[ 1137](hci__types_8h.md#a6fb35a340e8eecd7bc2602ed010aa6c1)#define BT\_HCI\_LE\_SCAN\_FILTER\_DUP\_DISABLE 0x00

[ 1138](hci__types_8h.md#a4c9503d4a13f78a1dc44e087af922793)#define BT\_HCI\_LE\_SCAN\_FILTER\_DUP\_ENABLE 0x01

1139

[ 1140](structbt__hci__cp__le__set__scan__enable.md)struct [bt\_hci\_cp\_le\_set\_scan\_enable](structbt__hci__cp__le__set__scan__enable.md) {

[ 1141](structbt__hci__cp__le__set__scan__enable.md#a5e429a0b11be1493515803a360932b06) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enable](structbt__hci__cp__le__set__scan__enable.md#a5e429a0b11be1493515803a360932b06);

[ 1142](structbt__hci__cp__le__set__scan__enable.md#a77b0f05c0e76681ed633bd42b3f21811) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter\_dup](structbt__hci__cp__le__set__scan__enable.md#a77b0f05c0e76681ed633bd42b3f21811);

1143} \_\_packed;

1144

[ 1145](hci__types_8h.md#aadde6f016c942c7907afddf7b6c94304)#define BT\_HCI\_OP\_LE\_CREATE\_CONN BT\_OP(BT\_OGF\_LE, 0x000d) /\* 0x200d \*/

1146

[ 1147](hci__types_8h.md#ae1bd495a90fd902614014e7e1e2f1239)#define BT\_HCI\_LE\_CREATE\_CONN\_FP\_NO\_FILTER 0x00

[ 1148](hci__types_8h.md#ac04c2c0020d2972d6df169f39c421c08)#define BT\_HCI\_LE\_CREATE\_CONN\_FP\_FILTER 0x01

1149

[ 1150](structbt__hci__cp__le__create__conn.md)struct [bt\_hci\_cp\_le\_create\_conn](structbt__hci__cp__le__create__conn.md) {

[ 1151](structbt__hci__cp__le__create__conn.md#a1a830a0f6cd961d534c338031b2b691b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [scan\_interval](structbt__hci__cp__le__create__conn.md#a1a830a0f6cd961d534c338031b2b691b);

[ 1152](structbt__hci__cp__le__create__conn.md#abf61e67f5e20adc44b5b9314ed43bccc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [scan\_window](structbt__hci__cp__le__create__conn.md#abf61e67f5e20adc44b5b9314ed43bccc);

[ 1153](structbt__hci__cp__le__create__conn.md#a2ca5063f5082a0f330676e56253a21c7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter\_policy](structbt__hci__cp__le__create__conn.md#a2ca5063f5082a0f330676e56253a21c7);

[ 1154](structbt__hci__cp__le__create__conn.md#aa51da7602eb2b44528964c8b706bb043) [bt\_addr\_le\_t](structbt__addr__le__t.md) [peer\_addr](structbt__hci__cp__le__create__conn.md#aa51da7602eb2b44528964c8b706bb043);

[ 1155](structbt__hci__cp__le__create__conn.md#a63c7f9e89528105e484a60e41eeb8a30) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [own\_addr\_type](structbt__hci__cp__le__create__conn.md#a63c7f9e89528105e484a60e41eeb8a30);

[ 1156](structbt__hci__cp__le__create__conn.md#a988cf154b0df1ff9af8d34ce73a920dd) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_interval\_min](structbt__hci__cp__le__create__conn.md#a988cf154b0df1ff9af8d34ce73a920dd);

[ 1157](structbt__hci__cp__le__create__conn.md#aa009d54866d9c675c2785412bdbd182f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_interval\_max](structbt__hci__cp__le__create__conn.md#aa009d54866d9c675c2785412bdbd182f);

[ 1158](structbt__hci__cp__le__create__conn.md#a5a9d5c1d44adac876680a517b1fad63f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_latency](structbt__hci__cp__le__create__conn.md#a5a9d5c1d44adac876680a517b1fad63f);

[ 1159](structbt__hci__cp__le__create__conn.md#ae8e0ad70a3b23ac035c237db0d57adc4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [supervision\_timeout](structbt__hci__cp__le__create__conn.md#ae8e0ad70a3b23ac035c237db0d57adc4);

[ 1160](structbt__hci__cp__le__create__conn.md#a476501ccd209f3a52082decf906ca8f0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [min\_ce\_len](structbt__hci__cp__le__create__conn.md#a476501ccd209f3a52082decf906ca8f0);

[ 1161](structbt__hci__cp__le__create__conn.md#a5b329aa8b48e03998e969b2436d35ab5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_ce\_len](structbt__hci__cp__le__create__conn.md#a5b329aa8b48e03998e969b2436d35ab5);

1162} \_\_packed;

1163

[ 1164](hci__types_8h.md#acacd0832cddc00702da74b4a36e5c825)#define BT\_HCI\_OP\_LE\_CREATE\_CONN\_CANCEL BT\_OP(BT\_OGF\_LE, 0x000e) /\* 0x200e \*/

1165

[ 1166](hci__types_8h.md#aeeba2e21bd5e33abbd48fa18f5e252f3)#define BT\_HCI\_OP\_LE\_READ\_FAL\_SIZE BT\_OP(BT\_OGF\_LE, 0x000f) /\* 0x200f \*/

[ 1167](structbt__hci__rp__le__read__fal__size.md)struct [bt\_hci\_rp\_le\_read\_fal\_size](structbt__hci__rp__le__read__fal__size.md) {

[ 1168](structbt__hci__rp__le__read__fal__size.md#aaceae885848bbdbf71241e7aa3881db5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__fal__size.md#aaceae885848bbdbf71241e7aa3881db5);

[ 1169](structbt__hci__rp__le__read__fal__size.md#ac5fcb88478c1faadf7f7ca6a9f838dde) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [fal\_size](structbt__hci__rp__le__read__fal__size.md#ac5fcb88478c1faadf7f7ca6a9f838dde);

1170} \_\_packed;

1171

[ 1172](hci__types_8h.md#a592ce45c74bdabf1b25954b8021a50bb)#define BT\_HCI\_OP\_LE\_CLEAR\_FAL BT\_OP(BT\_OGF\_LE, 0x0010) /\* 0x2010 \*/

1173

[ 1174](hci__types_8h.md#a103c6fada57c61fc3f994f8902f4123c)#define BT\_HCI\_OP\_LE\_ADD\_DEV\_TO\_FAL BT\_OP(BT\_OGF\_LE, 0x0011) /\* 0x2011 \*/

[ 1175](structbt__hci__cp__le__add__dev__to__fal.md)struct [bt\_hci\_cp\_le\_add\_dev\_to\_fal](structbt__hci__cp__le__add__dev__to__fal.md) {

[ 1176](structbt__hci__cp__le__add__dev__to__fal.md#a11ec9f3cd9b80f34094e70d8eeb13be3) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__hci__cp__le__add__dev__to__fal.md#a11ec9f3cd9b80f34094e70d8eeb13be3);

1177} \_\_packed;

1178

[ 1179](hci__types_8h.md#aedbb03b04ed567e54642e42ae758538a)#define BT\_HCI\_OP\_LE\_REM\_DEV\_FROM\_FAL BT\_OP(BT\_OGF\_LE, 0x0012) /\* 0x2012 \*/

[ 1180](structbt__hci__cp__le__rem__dev__from__fal.md)struct [bt\_hci\_cp\_le\_rem\_dev\_from\_fal](structbt__hci__cp__le__rem__dev__from__fal.md) {

[ 1181](structbt__hci__cp__le__rem__dev__from__fal.md#afe6054303093cc930d1089ca6a16101c) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__hci__cp__le__rem__dev__from__fal.md#afe6054303093cc930d1089ca6a16101c);

1182} \_\_packed;

1183

[ 1184](hci__types_8h.md#ac0c308b64ed89c9b7326982ef04ba6d3)#define BT\_HCI\_OP\_LE\_CONN\_UPDATE BT\_OP(BT\_OGF\_LE, 0x0013) /\* 0x2013 \*/

[ 1185](structhci__cp__le__conn__update.md)struct [hci\_cp\_le\_conn\_update](structhci__cp__le__conn__update.md) {

[ 1186](structhci__cp__le__conn__update.md#a5606b8795defc338b27d1a130064351e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structhci__cp__le__conn__update.md#a5606b8795defc338b27d1a130064351e);

[ 1187](structhci__cp__le__conn__update.md#adcfee3c727118069897515a00e7ead66) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_interval\_min](structhci__cp__le__conn__update.md#adcfee3c727118069897515a00e7ead66);

[ 1188](structhci__cp__le__conn__update.md#a99fc0b3b0f810f1d6e174aa9045d298a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_interval\_max](structhci__cp__le__conn__update.md#a99fc0b3b0f810f1d6e174aa9045d298a);

[ 1189](structhci__cp__le__conn__update.md#a8e48e5e195aea7f581cfc7246da79d72) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_latency](structhci__cp__le__conn__update.md#a8e48e5e195aea7f581cfc7246da79d72);

[ 1190](structhci__cp__le__conn__update.md#ab76ecdf6f7e5a5bb581cbd26f67d8f9f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [supervision\_timeout](structhci__cp__le__conn__update.md#ab76ecdf6f7e5a5bb581cbd26f67d8f9f);

[ 1191](structhci__cp__le__conn__update.md#a3ae86fccacf462463fe520eb1e06fa62) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [min\_ce\_len](structhci__cp__le__conn__update.md#a3ae86fccacf462463fe520eb1e06fa62);

[ 1192](structhci__cp__le__conn__update.md#a401169ccc5dbf6cf0abd6154738f00dc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_ce\_len](structhci__cp__le__conn__update.md#a401169ccc5dbf6cf0abd6154738f00dc);

1193} \_\_packed;

1194

[ 1195](hci__types_8h.md#a6224aab014342d93bcb16c717cd52421)#define BT\_HCI\_OP\_LE\_SET\_HOST\_CHAN\_CLASSIF BT\_OP(BT\_OGF\_LE, 0x0014) /\* 0x2014 \*/

[ 1196](structbt__hci__cp__le__set__host__chan__classif.md)struct [bt\_hci\_cp\_le\_set\_host\_chan\_classif](structbt__hci__cp__le__set__host__chan__classif.md) {

[ 1197](structbt__hci__cp__le__set__host__chan__classif.md#a0fb81bcdebe7da416cc4317486106752) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ch\_map](structbt__hci__cp__le__set__host__chan__classif.md#a0fb81bcdebe7da416cc4317486106752)[5];

1198} \_\_packed;

1199

[ 1200](hci__types_8h.md#a9040e4b5e719d53cc324faa280a670a4)#define BT\_HCI\_OP\_LE\_READ\_CHAN\_MAP BT\_OP(BT\_OGF\_LE, 0x0015) /\* 0x2015 \*/

[ 1201](structbt__hci__cp__le__read__chan__map.md)struct [bt\_hci\_cp\_le\_read\_chan\_map](structbt__hci__cp__le__read__chan__map.md) {

[ 1202](structbt__hci__cp__le__read__chan__map.md#abea9aec016a0433b3e4837d53d6b5d2b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__read__chan__map.md#abea9aec016a0433b3e4837d53d6b5d2b);

1203} \_\_packed;

[ 1204](structbt__hci__rp__le__read__chan__map.md)struct [bt\_hci\_rp\_le\_read\_chan\_map](structbt__hci__rp__le__read__chan__map.md) {

[ 1205](structbt__hci__rp__le__read__chan__map.md#a73a51f243bf4881f9024ba67cf2426ad) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__chan__map.md#a73a51f243bf4881f9024ba67cf2426ad);

[ 1206](structbt__hci__rp__le__read__chan__map.md#a8fcec46574f5601bf0837aae8f745b38) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__read__chan__map.md#a8fcec46574f5601bf0837aae8f745b38);

[ 1207](structbt__hci__rp__le__read__chan__map.md#a2899c53f17ba2293b95477ba25fd1b3d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ch\_map](structbt__hci__rp__le__read__chan__map.md#a2899c53f17ba2293b95477ba25fd1b3d)[5];

1208} \_\_packed;

1209

[ 1210](hci__types_8h.md#ac8d5165a3a5d190b8e2d31feb79a17c9)#define BT\_HCI\_OP\_LE\_READ\_REMOTE\_FEATURES BT\_OP(BT\_OGF\_LE, 0x0016) /\* 0x2016 \*/

[ 1211](structbt__hci__cp__le__read__remote__features.md)struct [bt\_hci\_cp\_le\_read\_remote\_features](structbt__hci__cp__le__read__remote__features.md) {

[ 1212](structbt__hci__cp__le__read__remote__features.md#a843997555fd36f102c83a7d59f65eea9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__read__remote__features.md#a843997555fd36f102c83a7d59f65eea9);

1213} \_\_packed;

1214

[ 1215](hci__types_8h.md#a99fdd1dbff627a2f627e7d9eced68326)#define BT\_HCI\_OP\_LE\_ENCRYPT BT\_OP(BT\_OGF\_LE, 0x0017) /\* 0x2017 \*/

[ 1216](structbt__hci__cp__le__encrypt.md)struct [bt\_hci\_cp\_le\_encrypt](structbt__hci__cp__le__encrypt.md) {

[ 1217](structbt__hci__cp__le__encrypt.md#ab64f1bab8ad3a98217db96e6765a7d24) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key](structbt__hci__cp__le__encrypt.md#ab64f1bab8ad3a98217db96e6765a7d24)[16];

[ 1218](structbt__hci__cp__le__encrypt.md#ad520b84e6e2a4e62f7fefba248c4cf10) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [plaintext](structbt__hci__cp__le__encrypt.md#ad520b84e6e2a4e62f7fefba248c4cf10)[16];

1219} \_\_packed;

[ 1220](structbt__hci__rp__le__encrypt.md)struct [bt\_hci\_rp\_le\_encrypt](structbt__hci__rp__le__encrypt.md) {

[ 1221](structbt__hci__rp__le__encrypt.md#aee480917cc6af7dea77717a9cb5840bb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__encrypt.md#aee480917cc6af7dea77717a9cb5840bb);

[ 1222](structbt__hci__rp__le__encrypt.md#ac20cd9f4ceffea6999114f65437aefdc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enc\_data](structbt__hci__rp__le__encrypt.md#ac20cd9f4ceffea6999114f65437aefdc)[16];

1223} \_\_packed;

1224

[ 1225](hci__types_8h.md#ac3af817deaf472dbb2a825fd57b67f42)#define BT\_HCI\_OP\_LE\_RAND BT\_OP(BT\_OGF\_LE, 0x0018) /\* 0x2018 \*/

[ 1226](structbt__hci__rp__le__rand.md)struct [bt\_hci\_rp\_le\_rand](structbt__hci__rp__le__rand.md) {

[ 1227](structbt__hci__rp__le__rand.md#a73320168836caa3caf724282402e80de) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__rand.md#a73320168836caa3caf724282402e80de);

[ 1228](structbt__hci__rp__le__rand.md#a3f706af9d2baf9e2b199242a28cec9e5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rand](structbt__hci__rp__le__rand.md#a3f706af9d2baf9e2b199242a28cec9e5)[8];

1229} \_\_packed;

1230

[ 1231](hci__types_8h.md#afececfce5819f1b8555ce47fbde2aa0b)#define BT\_HCI\_OP\_LE\_START\_ENCRYPTION BT\_OP(BT\_OGF\_LE, 0x0019) /\* 0x2019 \*/

[ 1232](structbt__hci__cp__le__start__encryption.md)struct [bt\_hci\_cp\_le\_start\_encryption](structbt__hci__cp__le__start__encryption.md) {

[ 1233](structbt__hci__cp__le__start__encryption.md#a4ac6d63f336e36a347242153aced4c71) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__start__encryption.md#a4ac6d63f336e36a347242153aced4c71);

[ 1234](structbt__hci__cp__le__start__encryption.md#ade8ae824dc5d85671971a3baafee8f54) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [rand](structbt__hci__cp__le__start__encryption.md#ade8ae824dc5d85671971a3baafee8f54);

[ 1235](structbt__hci__cp__le__start__encryption.md#a640d201bbfa6f6d8476be02d3656e847) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [ediv](structbt__hci__cp__le__start__encryption.md#a640d201bbfa6f6d8476be02d3656e847);

[ 1236](structbt__hci__cp__le__start__encryption.md#a99d2dd719ce38976e9da8a73f26839a1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ltk](structbt__hci__cp__le__start__encryption.md#a99d2dd719ce38976e9da8a73f26839a1)[16];

1237} \_\_packed;

1238

[ 1239](hci__types_8h.md#a92050425248585bd1c3873e8593db362)#define BT\_HCI\_OP\_LE\_LTK\_REQ\_REPLY BT\_OP(BT\_OGF\_LE, 0x001a) /\* 0x201a \*/

[ 1240](structbt__hci__cp__le__ltk__req__reply.md)struct [bt\_hci\_cp\_le\_ltk\_req\_reply](structbt__hci__cp__le__ltk__req__reply.md) {

[ 1241](structbt__hci__cp__le__ltk__req__reply.md#a46d87451acc1f1ce2ff35dd0dd238db3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__ltk__req__reply.md#a46d87451acc1f1ce2ff35dd0dd238db3);

[ 1242](structbt__hci__cp__le__ltk__req__reply.md#a2d16b44af344237a890341943c4a6582) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ltk](structbt__hci__cp__le__ltk__req__reply.md#a2d16b44af344237a890341943c4a6582)[16];

1243} \_\_packed;

[ 1244](structbt__hci__rp__le__ltk__req__reply.md)struct [bt\_hci\_rp\_le\_ltk\_req\_reply](structbt__hci__rp__le__ltk__req__reply.md) {

[ 1245](structbt__hci__rp__le__ltk__req__reply.md#a831950bab8994f36c96c543310400752) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__ltk__req__reply.md#a831950bab8994f36c96c543310400752);

[ 1246](structbt__hci__rp__le__ltk__req__reply.md#a2dfe012e641e5d8bd6c0f2e15e5a54c2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__ltk__req__reply.md#a2dfe012e641e5d8bd6c0f2e15e5a54c2);

1247} \_\_packed;

1248

[ 1249](hci__types_8h.md#ae04bd3c7ff17142f2b47e24accdf6a20)#define BT\_HCI\_OP\_LE\_LTK\_REQ\_NEG\_REPLY BT\_OP(BT\_OGF\_LE, 0x001b) /\* 0x201b \*/

[ 1250](structbt__hci__cp__le__ltk__req__neg__reply.md)struct [bt\_hci\_cp\_le\_ltk\_req\_neg\_reply](structbt__hci__cp__le__ltk__req__neg__reply.md) {

[ 1251](structbt__hci__cp__le__ltk__req__neg__reply.md#add8cc3b13432e233ceb5c2c11e0107c0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__ltk__req__neg__reply.md#add8cc3b13432e233ceb5c2c11e0107c0);

1252} \_\_packed;

[ 1253](structbt__hci__rp__le__ltk__req__neg__reply.md)struct [bt\_hci\_rp\_le\_ltk\_req\_neg\_reply](structbt__hci__rp__le__ltk__req__neg__reply.md) {

[ 1254](structbt__hci__rp__le__ltk__req__neg__reply.md#a92306e47450b239233a3f39c645eaa4e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__ltk__req__neg__reply.md#a92306e47450b239233a3f39c645eaa4e);

[ 1255](structbt__hci__rp__le__ltk__req__neg__reply.md#ad0f4f9300d9a8b737b41211972151017) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__ltk__req__neg__reply.md#ad0f4f9300d9a8b737b41211972151017);

1256} \_\_packed;

1257

[ 1258](hci__types_8h.md#a286869ebde03594d56ecd8bc1aa7c73c)#define BT\_HCI\_OP\_LE\_READ\_SUPP\_STATES BT\_OP(BT\_OGF\_LE, 0x001c) /\* 0x201c \*/

[ 1259](structbt__hci__rp__le__read__supp__states.md)struct [bt\_hci\_rp\_le\_read\_supp\_states](structbt__hci__rp__le__read__supp__states.md) {

[ 1260](structbt__hci__rp__le__read__supp__states.md#aeed0cc41ee521c27f07d8cbf4b377a4f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__supp__states.md#aeed0cc41ee521c27f07d8cbf4b377a4f);

[ 1261](structbt__hci__rp__le__read__supp__states.md#a9b60476cc158a701b29b28bd21375130) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [le\_states](structbt__hci__rp__le__read__supp__states.md#a9b60476cc158a701b29b28bd21375130)[8];

1262} \_\_packed;

1263

[ 1264](hci__types_8h.md#abd18c6854a0dc97c451b498816f206e4)#define BT\_HCI\_OP\_LE\_RX\_TEST BT\_OP(BT\_OGF\_LE, 0x001d) /\* 0x201d \*/

[ 1265](structbt__hci__cp__le__rx__test.md)struct [bt\_hci\_cp\_le\_rx\_test](structbt__hci__cp__le__rx__test.md) {

[ 1266](structbt__hci__cp__le__rx__test.md#a11cb21a7625d9c097eba0a7b68e93f3f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_ch](structbt__hci__cp__le__rx__test.md#a11cb21a7625d9c097eba0a7b68e93f3f);

1267} \_\_packed;

1268

[ 1269](hci__types_8h.md#aa9ce0f2db7b63303a9c61c37d052d7b7)#define BT\_HCI\_TEST\_PKT\_PAYLOAD\_PRBS9 0x00

[ 1270](hci__types_8h.md#a51d26730c8f4c3c8491b33483bdb9494)#define BT\_HCI\_TEST\_PKT\_PAYLOAD\_11110000 0x01

[ 1271](hci__types_8h.md#aab044752b89bb4493a509580ae8eaf9b)#define BT\_HCI\_TEST\_PKT\_PAYLOAD\_10101010 0x02

[ 1272](hci__types_8h.md#a0eb4fcbb3ab6c7d4e2ed87d61c5b30f1)#define BT\_HCI\_TEST\_PKT\_PAYLOAD\_PRBS15 0x03

[ 1273](hci__types_8h.md#a5008205909cecc994b74c8a1cb1f92af)#define BT\_HCI\_TEST\_PKT\_PAYLOAD\_11111111 0x04

[ 1274](hci__types_8h.md#a1fe8c26f174833a4dccbe192df2c6f7d)#define BT\_HCI\_TEST\_PKT\_PAYLOAD\_00000000 0x05

[ 1275](hci__types_8h.md#a13baca9e4517522c763c25882177a2a7)#define BT\_HCI\_TEST\_PKT\_PAYLOAD\_00001111 0x06

[ 1276](hci__types_8h.md#a8f660f979b14d91abd9423e718921ebb)#define BT\_HCI\_TEST\_PKT\_PAYLOAD\_01010101 0x07

1277

[ 1278](hci__types_8h.md#af5fe87cbe280dcf26ddc21952e84e93e)#define BT\_HCI\_OP\_LE\_TX\_TEST BT\_OP(BT\_OGF\_LE, 0x001e) /\* 0x201e \*/

[ 1279](structbt__hci__cp__le__tx__test.md)struct [bt\_hci\_cp\_le\_tx\_test](structbt__hci__cp__le__tx__test.md) {

[ 1280](structbt__hci__cp__le__tx__test.md#aae634b277125066ecbc36d119bc4244f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_ch](structbt__hci__cp__le__tx__test.md#aae634b277125066ecbc36d119bc4244f);

[ 1281](structbt__hci__cp__le__tx__test.md#a55c5f1621a51da03500910fc9664df54) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [test\_data\_len](structbt__hci__cp__le__tx__test.md#a55c5f1621a51da03500910fc9664df54);

[ 1282](structbt__hci__cp__le__tx__test.md#ad93908905d370842f16e16cc45280495) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pkt\_payload](structbt__hci__cp__le__tx__test.md#ad93908905d370842f16e16cc45280495);

1283} \_\_packed;

1284

[ 1285](hci__types_8h.md#a7ff8a81ae09ddb0d18f999fe454e41df)#define BT\_HCI\_OP\_LE\_TEST\_END BT\_OP(BT\_OGF\_LE, 0x001f) /\* 0x201f \*/

[ 1286](structbt__hci__rp__le__test__end.md)struct [bt\_hci\_rp\_le\_test\_end](structbt__hci__rp__le__test__end.md) {

[ 1287](structbt__hci__rp__le__test__end.md#a2ac412ef9a5fc7651315afe042856cce) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__test__end.md#a2ac412ef9a5fc7651315afe042856cce);

[ 1288](structbt__hci__rp__le__test__end.md#a9e283118e4ea48b0df66a4cd1c1cf9a1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [rx\_pkt\_count](structbt__hci__rp__le__test__end.md#a9e283118e4ea48b0df66a4cd1c1cf9a1);

1289} \_\_packed;

1290

[ 1291](hci__types_8h.md#a8b824639d31fa9f579e73cf1f1344c85)#define BT\_HCI\_OP\_LE\_CONN\_PARAM\_REQ\_REPLY BT\_OP(BT\_OGF\_LE, 0x0020) /\* 0x2020 \*/

[ 1292](structbt__hci__cp__le__conn__param__req__reply.md)struct [bt\_hci\_cp\_le\_conn\_param\_req\_reply](structbt__hci__cp__le__conn__param__req__reply.md) {

[ 1293](structbt__hci__cp__le__conn__param__req__reply.md#aa3b938afe13d4e05806fb6cdfab5cb14) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__conn__param__req__reply.md#aa3b938afe13d4e05806fb6cdfab5cb14);

[ 1294](structbt__hci__cp__le__conn__param__req__reply.md#a10547c7d4836980947d17bbde0d75a51) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval\_min](structbt__hci__cp__le__conn__param__req__reply.md#a10547c7d4836980947d17bbde0d75a51);

[ 1295](structbt__hci__cp__le__conn__param__req__reply.md#aed58f9aa722a284ae39df842394c06cf) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval\_max](structbt__hci__cp__le__conn__param__req__reply.md#aed58f9aa722a284ae39df842394c06cf);

[ 1296](structbt__hci__cp__le__conn__param__req__reply.md#a8c76816cc230387c249ab8e05c402964) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [latency](structbt__hci__cp__le__conn__param__req__reply.md#a8c76816cc230387c249ab8e05c402964);

[ 1297](structbt__hci__cp__le__conn__param__req__reply.md#af25a3f226ceccbe19e7f1482ed5f141e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structbt__hci__cp__le__conn__param__req__reply.md#af25a3f226ceccbe19e7f1482ed5f141e);

[ 1298](structbt__hci__cp__le__conn__param__req__reply.md#a512d605d5c4aacf81b78794fcf260abf) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [min\_ce\_len](structbt__hci__cp__le__conn__param__req__reply.md#a512d605d5c4aacf81b78794fcf260abf);

[ 1299](structbt__hci__cp__le__conn__param__req__reply.md#a932e6a3a45ec0409656325f7246d5d7e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_ce\_len](structbt__hci__cp__le__conn__param__req__reply.md#a932e6a3a45ec0409656325f7246d5d7e);

1300} \_\_packed;

[ 1301](structbt__hci__rp__le__conn__param__req__reply.md)struct [bt\_hci\_rp\_le\_conn\_param\_req\_reply](structbt__hci__rp__le__conn__param__req__reply.md) {

[ 1302](structbt__hci__rp__le__conn__param__req__reply.md#a2f0a9f5b087d1f12c100ef4521e015ff) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__conn__param__req__reply.md#a2f0a9f5b087d1f12c100ef4521e015ff);

[ 1303](structbt__hci__rp__le__conn__param__req__reply.md#a3e598cd87d5298a1cc62ac79a4f34a6e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__conn__param__req__reply.md#a3e598cd87d5298a1cc62ac79a4f34a6e);

1304} \_\_packed;

1305

[ 1306](hci__types_8h.md#a1fbca6b816791f1967278224f37782c1)#define BT\_HCI\_OP\_LE\_CONN\_PARAM\_REQ\_NEG\_REPLY BT\_OP(BT\_OGF\_LE, 0x0021) /\* 0x2021 \*/

[ 1307](structbt__hci__cp__le__conn__param__req__neg__reply.md)struct [bt\_hci\_cp\_le\_conn\_param\_req\_neg\_reply](structbt__hci__cp__le__conn__param__req__neg__reply.md) {

[ 1308](structbt__hci__cp__le__conn__param__req__neg__reply.md#a0040e4a50c5c5479b539eb0bafb7b305) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__conn__param__req__neg__reply.md#a0040e4a50c5c5479b539eb0bafb7b305);

[ 1309](structbt__hci__cp__le__conn__param__req__neg__reply.md#a8c283ac844805224b1ffeb9801e8b14b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reason](structbt__hci__cp__le__conn__param__req__neg__reply.md#a8c283ac844805224b1ffeb9801e8b14b);

1310} \_\_packed;

[ 1311](structbt__hci__rp__le__conn__param__req__neg__reply.md)struct [bt\_hci\_rp\_le\_conn\_param\_req\_neg\_reply](structbt__hci__rp__le__conn__param__req__neg__reply.md) {

[ 1312](structbt__hci__rp__le__conn__param__req__neg__reply.md#a3804e64f9e8693e3e5899067212f6873) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__conn__param__req__neg__reply.md#a3804e64f9e8693e3e5899067212f6873);

[ 1313](structbt__hci__rp__le__conn__param__req__neg__reply.md#ac88f44127c0a1b9b191a27cc003c1052) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__conn__param__req__neg__reply.md#ac88f44127c0a1b9b191a27cc003c1052);

1314} \_\_packed;

1315

[ 1316](hci__types_8h.md#a5aeb49334449851866537ea8703f5ab0)#define BT\_HCI\_OP\_LE\_SET\_DATA\_LEN BT\_OP(BT\_OGF\_LE, 0x0022) /\* 0x2022 \*/

[ 1317](structbt__hci__cp__le__set__data__len.md)struct [bt\_hci\_cp\_le\_set\_data\_len](structbt__hci__cp__le__set__data__len.md) {

[ 1318](structbt__hci__cp__le__set__data__len.md#a874869090428a7f380c5466353573eba) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__set__data__len.md#a874869090428a7f380c5466353573eba);

[ 1319](structbt__hci__cp__le__set__data__len.md#ac579e84a004a09813bbe0ed61db11931) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [tx\_octets](structbt__hci__cp__le__set__data__len.md#ac579e84a004a09813bbe0ed61db11931);

[ 1320](structbt__hci__cp__le__set__data__len.md#a15285a4e8bf8e359bb326de4b30ba8f1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [tx\_time](structbt__hci__cp__le__set__data__len.md#a15285a4e8bf8e359bb326de4b30ba8f1);

1321} \_\_packed;

[ 1322](structbt__hci__rp__le__set__data__len.md)struct [bt\_hci\_rp\_le\_set\_data\_len](structbt__hci__rp__le__set__data__len.md) {

[ 1323](structbt__hci__rp__le__set__data__len.md#a8667db355a95691d58845f89e919aea4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__set__data__len.md#a8667db355a95691d58845f89e919aea4);

[ 1324](structbt__hci__rp__le__set__data__len.md#a207c6da11e0bb145bed7a9e551ddc608) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__set__data__len.md#a207c6da11e0bb145bed7a9e551ddc608);

1325} \_\_packed;

1326

[ 1327](hci__types_8h.md#aa58d9ce08e0f1d4a3e5a2f2b1733a6d2)#define BT\_HCI\_OP\_LE\_READ\_DEFAULT\_DATA\_LEN BT\_OP(BT\_OGF\_LE, 0x0023) /\* 0x2023 \*/

[ 1328](structbt__hci__rp__le__read__default__data__len.md)struct [bt\_hci\_rp\_le\_read\_default\_data\_len](structbt__hci__rp__le__read__default__data__len.md) {

[ 1329](structbt__hci__rp__le__read__default__data__len.md#a62d735826ad3ca5d4bea7d0fb87dea7e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__default__data__len.md#a62d735826ad3ca5d4bea7d0fb87dea7e);

[ 1330](structbt__hci__rp__le__read__default__data__len.md#a1ec4ba1c0286132e87fcffeb988a37f9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_tx\_octets](structbt__hci__rp__le__read__default__data__len.md#a1ec4ba1c0286132e87fcffeb988a37f9);

[ 1331](structbt__hci__rp__le__read__default__data__len.md#ae193eab40c2afa55b78a1906e6a26f26) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_tx\_time](structbt__hci__rp__le__read__default__data__len.md#ae193eab40c2afa55b78a1906e6a26f26);

1332} \_\_packed;

1333

[ 1334](hci__types_8h.md#ae344c1ab9af250787b9ed8109ad3cde0)#define BT\_HCI\_OP\_LE\_WRITE\_DEFAULT\_DATA\_LEN BT\_OP(BT\_OGF\_LE, 0x0024) /\* 0x2024 \*/

[ 1335](structbt__hci__cp__le__write__default__data__len.md)struct [bt\_hci\_cp\_le\_write\_default\_data\_len](structbt__hci__cp__le__write__default__data__len.md) {

[ 1336](structbt__hci__cp__le__write__default__data__len.md#a0ffb8c52d9031dfe448eac0943a4a49c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_tx\_octets](structbt__hci__cp__le__write__default__data__len.md#a0ffb8c52d9031dfe448eac0943a4a49c);

[ 1337](structbt__hci__cp__le__write__default__data__len.md#a2ada0ea5ee8ac8e6d59fc6adc18421b8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_tx\_time](structbt__hci__cp__le__write__default__data__len.md#a2ada0ea5ee8ac8e6d59fc6adc18421b8);

1338} \_\_packed;

1339

[ 1340](hci__types_8h.md#ab1ff230560c1f7712e23a22eb44f0e69)#define BT\_HCI\_OP\_LE\_P256\_PUBLIC\_KEY BT\_OP(BT\_OGF\_LE, 0x0025) /\* 0x2025 \*/

1341

[ 1342](hci__types_8h.md#af2625fcbc0f29199f1a95dc9fe0f929d)#define BT\_HCI\_OP\_LE\_GENERATE\_DHKEY BT\_OP(BT\_OGF\_LE, 0x0026) /\* 0x2026 \*/

[ 1343](structbt__hci__cp__le__generate__dhkey.md)struct [bt\_hci\_cp\_le\_generate\_dhkey](structbt__hci__cp__le__generate__dhkey.md) {

[ 1344](structbt__hci__cp__le__generate__dhkey.md#a0f67195504d877a1d11b7dfb77d09fcc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key](structbt__hci__cp__le__generate__dhkey.md#a0f67195504d877a1d11b7dfb77d09fcc)[64];

1345} \_\_packed;

1346

1347

[ 1348](hci__types_8h.md#aa7bf82632c6df22096210de18902a465)#define BT\_HCI\_OP\_LE\_GENERATE\_DHKEY\_V2 BT\_OP(BT\_OGF\_LE, 0x005e) /\* 0x205e \*/

1349

[ 1350](hci__types_8h.md#ac85ab1283cd175fc575ebd98b52b3335)#define BT\_HCI\_LE\_KEY\_TYPE\_GENERATED 0x00

[ 1351](hci__types_8h.md#a71f16c552b14042c00e98ea20c1e03c4)#define BT\_HCI\_LE\_KEY\_TYPE\_DEBUG 0x01

1352

[ 1353](structbt__hci__cp__le__generate__dhkey__v2.md)struct [bt\_hci\_cp\_le\_generate\_dhkey\_v2](structbt__hci__cp__le__generate__dhkey__v2.md) {

[ 1354](structbt__hci__cp__le__generate__dhkey__v2.md#acc3007adf301674b9e847297007c3cd1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key](structbt__hci__cp__le__generate__dhkey__v2.md#acc3007adf301674b9e847297007c3cd1)[64];

[ 1355](structbt__hci__cp__le__generate__dhkey__v2.md#a3d47ad6d9df4d4023d2586c915ee8f2c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key\_type](structbt__hci__cp__le__generate__dhkey__v2.md#a3d47ad6d9df4d4023d2586c915ee8f2c);

1356} \_\_packed;

1357

1358

[ 1359](hci__types_8h.md#a735c643e8afa27c4e7f7be9bfb09676a)#define BT\_HCI\_OP\_LE\_ADD\_DEV\_TO\_RL BT\_OP(BT\_OGF\_LE, 0x0027) /\* 0x2027 \*/

[ 1360](structbt__hci__cp__le__add__dev__to__rl.md)struct [bt\_hci\_cp\_le\_add\_dev\_to\_rl](structbt__hci__cp__le__add__dev__to__rl.md) {

[ 1361](structbt__hci__cp__le__add__dev__to__rl.md#a3daf2041f04381a56c2cbcd4bb33f4c0) [bt\_addr\_le\_t](structbt__addr__le__t.md) [peer\_id\_addr](structbt__hci__cp__le__add__dev__to__rl.md#a3daf2041f04381a56c2cbcd4bb33f4c0);

[ 1362](structbt__hci__cp__le__add__dev__to__rl.md#aedc27c868a7a4cbd3c175f67db4e3242) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [peer\_irk](structbt__hci__cp__le__add__dev__to__rl.md#aedc27c868a7a4cbd3c175f67db4e3242)[16];

[ 1363](structbt__hci__cp__le__add__dev__to__rl.md#ab5caa38e6eeab09b4a69084b1890317b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [local\_irk](structbt__hci__cp__le__add__dev__to__rl.md#ab5caa38e6eeab09b4a69084b1890317b)[16];

1364} \_\_packed;

1365

[ 1366](hci__types_8h.md#ac4c11605a4cd244ec3ffa972295396fa)#define BT\_HCI\_OP\_LE\_REM\_DEV\_FROM\_RL BT\_OP(BT\_OGF\_LE, 0x0028) /\* 0x2028 \*/

[ 1367](structbt__hci__cp__le__rem__dev__from__rl.md)struct [bt\_hci\_cp\_le\_rem\_dev\_from\_rl](structbt__hci__cp__le__rem__dev__from__rl.md) {

[ 1368](structbt__hci__cp__le__rem__dev__from__rl.md#aacb577a7ae13322145fccdffc3161541) [bt\_addr\_le\_t](structbt__addr__le__t.md) [peer\_id\_addr](structbt__hci__cp__le__rem__dev__from__rl.md#aacb577a7ae13322145fccdffc3161541);

1369} \_\_packed;

1370

[ 1371](hci__types_8h.md#a5efab85a3beac1fe3fc5a5294a2b1079)#define BT\_HCI\_OP\_LE\_CLEAR\_RL BT\_OP(BT\_OGF\_LE, 0x0029) /\* 0x2029 \*/

1372

[ 1373](hci__types_8h.md#a45b38708e807c784bd734ba1f69c7f86)#define BT\_HCI\_OP\_LE\_READ\_RL\_SIZE BT\_OP(BT\_OGF\_LE, 0x002a) /\* 0x202a \*/

[ 1374](structbt__hci__rp__le__read__rl__size.md)struct [bt\_hci\_rp\_le\_read\_rl\_size](structbt__hci__rp__le__read__rl__size.md) {

[ 1375](structbt__hci__rp__le__read__rl__size.md#af8a10aab21d54cce3529b1307769f6c6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__rl__size.md#af8a10aab21d54cce3529b1307769f6c6);

[ 1376](structbt__hci__rp__le__read__rl__size.md#a90c28070ee094c99c21c4dd229ff6ce5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rl\_size](structbt__hci__rp__le__read__rl__size.md#a90c28070ee094c99c21c4dd229ff6ce5);

1377} \_\_packed;

1378

[ 1379](hci__types_8h.md#a6c605e63bd1633f3423a915cf4db00e8)#define BT\_HCI\_OP\_LE\_READ\_PEER\_RPA BT\_OP(BT\_OGF\_LE, 0x002b) /\* 0x202b \*/

[ 1380](structbt__hci__cp__le__read__peer__rpa.md)struct [bt\_hci\_cp\_le\_read\_peer\_rpa](structbt__hci__cp__le__read__peer__rpa.md) {

[ 1381](structbt__hci__cp__le__read__peer__rpa.md#ab0c70a1dbe5152b1fc926b90ec3387b3) [bt\_addr\_le\_t](structbt__addr__le__t.md) [peer\_id\_addr](structbt__hci__cp__le__read__peer__rpa.md#ab0c70a1dbe5152b1fc926b90ec3387b3);

1382} \_\_packed;

[ 1383](structbt__hci__rp__le__read__peer__rpa.md)struct [bt\_hci\_rp\_le\_read\_peer\_rpa](structbt__hci__rp__le__read__peer__rpa.md) {

[ 1384](structbt__hci__rp__le__read__peer__rpa.md#a9c8c799e8c9fbb9f64865e55cdb1f9ef) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__peer__rpa.md#a9c8c799e8c9fbb9f64865e55cdb1f9ef);

[ 1385](structbt__hci__rp__le__read__peer__rpa.md#a4eeee179819865ba5d5171d9bd33e5e9) [bt\_addr\_t](structbt__addr__t.md) [peer\_rpa](structbt__hci__rp__le__read__peer__rpa.md#a4eeee179819865ba5d5171d9bd33e5e9);

1386} \_\_packed;

1387

[ 1388](hci__types_8h.md#af8ec9d3b6889a8530bc5977b8594fea6)#define BT\_HCI\_OP\_LE\_READ\_LOCAL\_RPA BT\_OP(BT\_OGF\_LE, 0x002c) /\* 0x202c \*/

[ 1389](structbt__hci__cp__le__read__local__rpa.md)struct [bt\_hci\_cp\_le\_read\_local\_rpa](structbt__hci__cp__le__read__local__rpa.md) {

[ 1390](structbt__hci__cp__le__read__local__rpa.md#aa96cd60066003e4a7a1f482fb81557f8) [bt\_addr\_le\_t](structbt__addr__le__t.md) [peer\_id\_addr](structbt__hci__cp__le__read__local__rpa.md#aa96cd60066003e4a7a1f482fb81557f8);

1391} \_\_packed;

[ 1392](structbt__hci__rp__le__read__local__rpa.md)struct [bt\_hci\_rp\_le\_read\_local\_rpa](structbt__hci__rp__le__read__local__rpa.md) {

[ 1393](structbt__hci__rp__le__read__local__rpa.md#a55b1ac66c986c0a7879b144163064be2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__local__rpa.md#a55b1ac66c986c0a7879b144163064be2);

[ 1394](structbt__hci__rp__le__read__local__rpa.md#a5b27c5b02cb290452be62c22772fbc53) [bt\_addr\_t](structbt__addr__t.md) [local\_rpa](structbt__hci__rp__le__read__local__rpa.md#a5b27c5b02cb290452be62c22772fbc53);

1395} \_\_packed;

1396

[ 1397](hci__types_8h.md#a017742ee92c9ed7b80b41f339394f1e4)#define BT\_HCI\_ADDR\_RES\_DISABLE 0x00

[ 1398](hci__types_8h.md#a61e677658b5a730b13869ebc0dbbffbe)#define BT\_HCI\_ADDR\_RES\_ENABLE 0x01

1399

[ 1400](hci__types_8h.md#a183431c86b7eb32b7c00e6b3a000f29e)#define BT\_HCI\_OP\_LE\_SET\_ADDR\_RES\_ENABLE BT\_OP(BT\_OGF\_LE, 0x002d) /\* 0x202d \*/

[ 1401](structbt__hci__cp__le__set__addr__res__enable.md)struct [bt\_hci\_cp\_le\_set\_addr\_res\_enable](structbt__hci__cp__le__set__addr__res__enable.md) {

[ 1402](structbt__hci__cp__le__set__addr__res__enable.md#ad0548178cbc9bc2db54612a748a2bd65) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enable](structbt__hci__cp__le__set__addr__res__enable.md#ad0548178cbc9bc2db54612a748a2bd65);

1403} \_\_packed;

1404

[ 1405](hci__types_8h.md#aeabb8438460e694867d855cf7f8e3b31)#define BT\_HCI\_OP\_LE\_SET\_RPA\_TIMEOUT BT\_OP(BT\_OGF\_LE, 0x002e) /\* 0x202e \*/

[ 1406](structbt__hci__cp__le__set__rpa__timeout.md)struct [bt\_hci\_cp\_le\_set\_rpa\_timeout](structbt__hci__cp__le__set__rpa__timeout.md) {

[ 1407](structbt__hci__cp__le__set__rpa__timeout.md#a6b1befe9d2131a889de17339ec1941fa) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [rpa\_timeout](structbt__hci__cp__le__set__rpa__timeout.md#a6b1befe9d2131a889de17339ec1941fa);

1408} \_\_packed;

1409

1410/\* All limits according to BT Core spec 5.4 [Vol 4, Part E, 7.8.46] \*/

[ 1411](hci__types_8h.md#a6c731f3c0644818489c146eeca9e3ea8)#define BT\_HCI\_LE\_MAX\_TX\_OCTETS\_MIN 0x001B

[ 1412](hci__types_8h.md#aec6c2a321f9700572fe8cf84d8bed238)#define BT\_HCI\_LE\_MAX\_TX\_OCTETS\_MAX 0x00FB

[ 1413](hci__types_8h.md#a6c192a213459f5cc7898faa8aa0f5f42)#define BT\_HCI\_LE\_MAX\_RX\_OCTETS\_MIN 0x001B

[ 1414](hci__types_8h.md#a72d22456f1eb112a75b91faa40e3b776)#define BT\_HCI\_LE\_MAX\_RX\_OCTETS\_MAX 0x00FB

1415

[ 1416](hci__types_8h.md#ac7c6251a5342a591ff4c413820125f94)#define BT\_HCI\_LE\_MAX\_TX\_TIME\_MIN 0x0148

[ 1417](hci__types_8h.md#aae4ce04bdfd0ad339c87eb18616d8a8a)#define BT\_HCI\_LE\_MAX\_TX\_TIME\_MAX 0x4290

[ 1418](hci__types_8h.md#a6666cbeff0cb43fa4c820ba92311fc11)#define BT\_HCI\_LE\_MAX\_RX\_TIME\_MIN 0x0148

[ 1419](hci__types_8h.md#ad4c16d0e80cb6dc2b6fd65e72e331173)#define BT\_HCI\_LE\_MAX\_RX\_TIME\_MAX 0x4290

1420

[ 1421](hci__types_8h.md#aafb5872650d77d9f4c6ae43038ef2bf1)#define BT\_HCI\_OP\_LE\_READ\_MAX\_DATA\_LEN BT\_OP(BT\_OGF\_LE, 0x002f) /\* 0x202f \*/

[ 1422](structbt__hci__rp__le__read__max__data__len.md)struct [bt\_hci\_rp\_le\_read\_max\_data\_len](structbt__hci__rp__le__read__max__data__len.md) {

[ 1423](structbt__hci__rp__le__read__max__data__len.md#a654b34b1ee038bf442550a340a26070c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__max__data__len.md#a654b34b1ee038bf442550a340a26070c);

[ 1424](structbt__hci__rp__le__read__max__data__len.md#a2c0b159c6248cb9df458d587f82a4152) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_tx\_octets](structbt__hci__rp__le__read__max__data__len.md#a2c0b159c6248cb9df458d587f82a4152);

[ 1425](structbt__hci__rp__le__read__max__data__len.md#a6adc84bf3cc86f234e61982d871899b6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_tx\_time](structbt__hci__rp__le__read__max__data__len.md#a6adc84bf3cc86f234e61982d871899b6);

[ 1426](structbt__hci__rp__le__read__max__data__len.md#a9273dac6614f1e120f0539b746bfd6cc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_rx\_octets](structbt__hci__rp__le__read__max__data__len.md#a9273dac6614f1e120f0539b746bfd6cc);

[ 1427](structbt__hci__rp__le__read__max__data__len.md#a963ef9c097906c8db46c35459eb4ecab) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_rx\_time](structbt__hci__rp__le__read__max__data__len.md#a963ef9c097906c8db46c35459eb4ecab);

1428} \_\_packed;

1429

[ 1430](hci__types_8h.md#a833ae32a3a5ffefbe57c7aa9cdf2e5a9)#define BT\_HCI\_LE\_PHY\_1M 0x01

[ 1431](hci__types_8h.md#a727a1780d5f3754a78dea0476c2b97bb)#define BT\_HCI\_LE\_PHY\_2M 0x02

[ 1432](hci__types_8h.md#ac5173dfe471fe4d1aad0f7d79904e46a)#define BT\_HCI\_LE\_PHY\_CODED 0x03

1433

[ 1434](hci__types_8h.md#ad2e063f4522a64ceeb36c1d95835e74e)#define BT\_HCI\_OP\_LE\_READ\_PHY BT\_OP(BT\_OGF\_LE, 0x0030) /\* 0x2030 \*/

[ 1435](structbt__hci__cp__le__read__phy.md)struct [bt\_hci\_cp\_le\_read\_phy](structbt__hci__cp__le__read__phy.md) {

[ 1436](structbt__hci__cp__le__read__phy.md#a7e0a4fa47b613c86364e6e94c2d0bef1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__read__phy.md#a7e0a4fa47b613c86364e6e94c2d0bef1);

1437} \_\_packed;

[ 1438](structbt__hci__rp__le__read__phy.md)struct [bt\_hci\_rp\_le\_read\_phy](structbt__hci__rp__le__read__phy.md) {

[ 1439](structbt__hci__rp__le__read__phy.md#a65d412e37eb2cd839fae262f4f9d5b28) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__phy.md#a65d412e37eb2cd839fae262f4f9d5b28);

[ 1440](structbt__hci__rp__le__read__phy.md#ae708b4f8ad2632d73bedea640f138d9f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__read__phy.md#ae708b4f8ad2632d73bedea640f138d9f);

[ 1441](structbt__hci__rp__le__read__phy.md#a644c0065d97e5de006dc28f7bca62268) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_phy](structbt__hci__rp__le__read__phy.md#a644c0065d97e5de006dc28f7bca62268);

[ 1442](structbt__hci__rp__le__read__phy.md#a5a060e0c0d1e5f33222ab10a5d3977e8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_phy](structbt__hci__rp__le__read__phy.md#a5a060e0c0d1e5f33222ab10a5d3977e8);

1443} \_\_packed;

1444

[ 1445](hci__types_8h.md#a7656d3400ccb540e8bd066cf1232c38e)#define BT\_HCI\_LE\_PHY\_TX\_ANY BIT(0)

[ 1446](hci__types_8h.md#a0fb6efaf47f2d676eb51b3fb99d0a691)#define BT\_HCI\_LE\_PHY\_RX\_ANY BIT(1)

1447

[ 1448](hci__types_8h.md#a8101f257838639b46dcd0d50a92bba0c)#define BT\_HCI\_LE\_PHY\_PREFER\_1M BIT(0)

[ 1449](hci__types_8h.md#ae89ffa7723482ced707f8a57febce629)#define BT\_HCI\_LE\_PHY\_PREFER\_2M BIT(1)

[ 1450](hci__types_8h.md#ab33fde130c9fdb99559b15455e827a7a)#define BT\_HCI\_LE\_PHY\_PREFER\_CODED BIT(2)

1451

[ 1452](hci__types_8h.md#aaa4e3fd27b4157a617a5fb6817bc1881)#define BT\_HCI\_OP\_LE\_SET\_DEFAULT\_PHY BT\_OP(BT\_OGF\_LE, 0x0031) /\* 0x2031 \*/

[ 1453](structbt__hci__cp__le__set__default__phy.md)struct [bt\_hci\_cp\_le\_set\_default\_phy](structbt__hci__cp__le__set__default__phy.md) {

[ 1454](structbt__hci__cp__le__set__default__phy.md#abe1d83e372e874739588812040d0b540) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [all\_phys](structbt__hci__cp__le__set__default__phy.md#abe1d83e372e874739588812040d0b540);

[ 1455](structbt__hci__cp__le__set__default__phy.md#a0c4ab2d91021466fd136af3a0b6bde2a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_phys](structbt__hci__cp__le__set__default__phy.md#a0c4ab2d91021466fd136af3a0b6bde2a);

[ 1456](structbt__hci__cp__le__set__default__phy.md#a4c3410f2ce9fb2817bc5d143908936d1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_phys](structbt__hci__cp__le__set__default__phy.md#a4c3410f2ce9fb2817bc5d143908936d1);

1457} \_\_packed;

1458

[ 1459](hci__types_8h.md#a61909ce217268c8cc6274f16d3db8484)#define BT\_HCI\_LE\_PHY\_CODED\_ANY 0x00

[ 1460](hci__types_8h.md#a54bf26868903f0178b0f9f70111ea6b7)#define BT\_HCI\_LE\_PHY\_CODED\_S2 0x01

[ 1461](hci__types_8h.md#abe28c39a93e86d9ad5e6f0c08b09ef9c)#define BT\_HCI\_LE\_PHY\_CODED\_S8 0x02

1462

[ 1463](hci__types_8h.md#a1d21c4ffe4db8caafa374a9138e179fa)#define BT\_HCI\_OP\_LE\_SET\_PHY BT\_OP(BT\_OGF\_LE, 0x0032) /\* 0x2032 \*/

[ 1464](structbt__hci__cp__le__set__phy.md)struct [bt\_hci\_cp\_le\_set\_phy](structbt__hci__cp__le__set__phy.md) {

[ 1465](structbt__hci__cp__le__set__phy.md#ad0759eea02017674459d4ce0af0e526e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__set__phy.md#ad0759eea02017674459d4ce0af0e526e);

[ 1466](structbt__hci__cp__le__set__phy.md#afb8d056dc7d8824eec0ef16fdf9ce924) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [all\_phys](structbt__hci__cp__le__set__phy.md#afb8d056dc7d8824eec0ef16fdf9ce924);

[ 1467](structbt__hci__cp__le__set__phy.md#a06880062ff486b532ebeb789adb57d1e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_phys](structbt__hci__cp__le__set__phy.md#a06880062ff486b532ebeb789adb57d1e);

[ 1468](structbt__hci__cp__le__set__phy.md#ab30eb68920a0578b16794250e592b12a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_phys](structbt__hci__cp__le__set__phy.md#ab30eb68920a0578b16794250e592b12a);

[ 1469](structbt__hci__cp__le__set__phy.md#a458ab90f83b60fafa66167f474c0800d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [phy\_opts](structbt__hci__cp__le__set__phy.md#a458ab90f83b60fafa66167f474c0800d);

1470} \_\_packed;

1471

[ 1472](hci__types_8h.md#a631e672ab64e36a983d4d3aae789b237)#define BT\_HCI\_LE\_MOD\_INDEX\_STANDARD 0x00

[ 1473](hci__types_8h.md#a423acd131760a1ab7b0671c45c9214ca)#define BT\_HCI\_LE\_MOD\_INDEX\_STABLE 0x01

1474

[ 1475](hci__types_8h.md#a27c179b4c8e85f840b41c4765613c99b)#define BT\_HCI\_LE\_RX\_PHY\_1M 0x01

[ 1476](hci__types_8h.md#ac1db92b615a94b30e587a87d3637ad47)#define BT\_HCI\_LE\_RX\_PHY\_2M 0x02

[ 1477](hci__types_8h.md#a689bc0f95a315c18ee4efbc556d31d60)#define BT\_HCI\_LE\_RX\_PHY\_CODED 0x03

1478

[ 1479](hci__types_8h.md#a51c3637712a8701ae7fee16806f677df)#define BT\_HCI\_OP\_LE\_ENH\_RX\_TEST BT\_OP(BT\_OGF\_LE, 0x0033) /\* 0x2033 \*/

[ 1480](structbt__hci__cp__le__enh__rx__test.md)struct [bt\_hci\_cp\_le\_enh\_rx\_test](structbt__hci__cp__le__enh__rx__test.md) {

[ 1481](structbt__hci__cp__le__enh__rx__test.md#a3aa5b3947a4a0c87342695469bf056ec) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_ch](structbt__hci__cp__le__enh__rx__test.md#a3aa5b3947a4a0c87342695469bf056ec);

[ 1482](structbt__hci__cp__le__enh__rx__test.md#aa2bf385221680b25ce184b4ea5d63cd4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__cp__le__enh__rx__test.md#aa2bf385221680b25ce184b4ea5d63cd4);

[ 1483](structbt__hci__cp__le__enh__rx__test.md#a9151393e9f05a2ded484a1248a6edb88) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mod\_index](structbt__hci__cp__le__enh__rx__test.md#a9151393e9f05a2ded484a1248a6edb88);

1484} \_\_packed;

1485

[ 1486](hci__types_8h.md#a0cb0c8d33e23ff6e59241c88b9e5adee)#define BT\_HCI\_LE\_TX\_PHY\_1M 0x01

[ 1487](hci__types_8h.md#a7de4598ca06439f89772f0e72306ac3c)#define BT\_HCI\_LE\_TX\_PHY\_2M 0x02

[ 1488](hci__types_8h.md#a01d96d9e7bb61db9b3cd31d161b0abf4)#define BT\_HCI\_LE\_TX\_PHY\_CODED\_S8 0x03

[ 1489](hci__types_8h.md#a599195b97f069412e112df470bf2b536)#define BT\_HCI\_LE\_TX\_PHY\_CODED\_S2 0x04

1490

[ 1491](hci__types_8h.md#a903b1ce0bfe7df7de86bae5fb143e88f)#define BT\_HCI\_OP\_LE\_ENH\_TX\_TEST BT\_OP(BT\_OGF\_LE, 0x0034) /\* 0x2034 \*/

[ 1492](structbt__hci__cp__le__enh__tx__test.md)struct [bt\_hci\_cp\_le\_enh\_tx\_test](structbt__hci__cp__le__enh__tx__test.md) {

[ 1493](structbt__hci__cp__le__enh__tx__test.md#a0b7883b36d511c6da1bac543f1aae446) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_ch](structbt__hci__cp__le__enh__tx__test.md#a0b7883b36d511c6da1bac543f1aae446);

[ 1494](structbt__hci__cp__le__enh__tx__test.md#af1e27be0ad23887c0e71024739b00f8d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [test\_data\_len](structbt__hci__cp__le__enh__tx__test.md#af1e27be0ad23887c0e71024739b00f8d);

[ 1495](structbt__hci__cp__le__enh__tx__test.md#a9ccb91be1554172d6c724e438508bfe5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pkt\_payload](structbt__hci__cp__le__enh__tx__test.md#a9ccb91be1554172d6c724e438508bfe5);

[ 1496](structbt__hci__cp__le__enh__tx__test.md#a718442db29c5ac455c3e2aac9844cdd0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__cp__le__enh__tx__test.md#a718442db29c5ac455c3e2aac9844cdd0);

1497} \_\_packed;

1498

[ 1499](hci__types_8h.md#ac96cefff0857a4d19025a2d9dec8333e)#define BT\_HCI\_OP\_LE\_SET\_ADV\_SET\_RANDOM\_ADDR BT\_OP(BT\_OGF\_LE, 0x0035) /\* 0x2035 \*/

[ 1500](structbt__hci__cp__le__set__adv__set__random__addr.md)struct [bt\_hci\_cp\_le\_set\_adv\_set\_random\_addr](structbt__hci__cp__le__set__adv__set__random__addr.md) {

[ 1501](structbt__hci__cp__le__set__adv__set__random__addr.md#aafa39422a16cc4ff11c8073e9c0aab71) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle](structbt__hci__cp__le__set__adv__set__random__addr.md#aafa39422a16cc4ff11c8073e9c0aab71);

[ 1502](structbt__hci__cp__le__set__adv__set__random__addr.md#a2883e9bf7ef6a34712eda2594e23c146) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__le__set__adv__set__random__addr.md#a2883e9bf7ef6a34712eda2594e23c146);

1503} \_\_packed;

1504

[ 1505](hci__types_8h.md#ac9597c1c284e23578352a23bd66c9fad)#define BT\_HCI\_LE\_ADV\_PROP\_CONN BIT(0)

[ 1506](hci__types_8h.md#ab886c4c7f33adf396ca3e09d0f38995d)#define BT\_HCI\_LE\_ADV\_PROP\_SCAN BIT(1)

[ 1507](hci__types_8h.md#acd154c93af2dc866cfe8bcf8e370dd3d)#define BT\_HCI\_LE\_ADV\_PROP\_DIRECT BIT(2)

[ 1508](hci__types_8h.md#a0fb43dd85c3671420029027cbfbf8c11)#define BT\_HCI\_LE\_ADV\_PROP\_HI\_DC\_CONN BIT(3)

[ 1509](hci__types_8h.md#a936310de47af573e0d1d5d9401097ba1)#define BT\_HCI\_LE\_ADV\_PROP\_LEGACY BIT(4)

[ 1510](hci__types_8h.md#a21c60f21a4de9136accc32b0a8a0325c)#define BT\_HCI\_LE\_ADV\_PROP\_ANON BIT(5)

[ 1511](hci__types_8h.md#abd14685442f2fe315a095516464fc92d)#define BT\_HCI\_LE\_ADV\_PROP\_TX\_POWER BIT(6)

1512

[ 1513](hci__types_8h.md#a1599475c6673d4fa0e00d16024df9a3b)#define BT\_HCI\_LE\_PRIM\_ADV\_INTERVAL\_MIN 0x000020

[ 1514](hci__types_8h.md#a5b394658223fd700fa152c4deb2f956e)#define BT\_HCI\_LE\_PRIM\_ADV\_INTERVAL\_MAX 0xFFFFFF

1515

[ 1516](hci__types_8h.md#a39fa8033dcf14aa43dfad7cabc1cb429)#define BT\_HCI\_LE\_ADV\_SCAN\_REQ\_ENABLE 1

[ 1517](hci__types_8h.md#aa1f4b7ba3b48ea6bd7b8a34a7b831a25)#define BT\_HCI\_LE\_ADV\_SCAN\_REQ\_DISABLE 0

1518

[ 1519](hci__types_8h.md#a7f4fcc517033a4743ded39503b35ce29)#define BT\_HCI\_LE\_ADV\_TX\_POWER\_NO\_PREF 0x7F

1520

[ 1521](hci__types_8h.md#a12d97417fa11a07b0af5370b595e9a17)#define BT\_HCI\_LE\_ADV\_HANDLE\_MAX 0xEF

1522

[ 1523](hci__types_8h.md#a973c2e0fc4cb22d58c47865b9e76b940)#define BT\_HCI\_LE\_EXT\_ADV\_SID\_INVALID 0xFF

1524

[ 1525](hci__types_8h.md#a098efdd7908adafd26b8e3f63508c476)#define BT\_HCI\_OP\_LE\_SET\_EXT\_ADV\_PARAM BT\_OP(BT\_OGF\_LE, 0x0036) /\* 0x2036 \*/

[ 1526](structbt__hci__cp__le__set__ext__adv__param.md)struct [bt\_hci\_cp\_le\_set\_ext\_adv\_param](structbt__hci__cp__le__set__ext__adv__param.md) {

[ 1527](structbt__hci__cp__le__set__ext__adv__param.md#a65fe609dde9515212659087a024e7c65) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle](structbt__hci__cp__le__set__ext__adv__param.md#a65fe609dde9515212659087a024e7c65);

[ 1528](structbt__hci__cp__le__set__ext__adv__param.md#a4af102ae90ca6917b3134491c5ff079f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [props](structbt__hci__cp__le__set__ext__adv__param.md#a4af102ae90ca6917b3134491c5ff079f);

[ 1529](structbt__hci__cp__le__set__ext__adv__param.md#ab5a80941b3d832c2906daed8cf069a02) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [prim\_min\_interval](structbt__hci__cp__le__set__ext__adv__param.md#ab5a80941b3d832c2906daed8cf069a02)[3];

[ 1530](structbt__hci__cp__le__set__ext__adv__param.md#a08aa741a56e825a11424bf024ac65e14) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [prim\_max\_interval](structbt__hci__cp__le__set__ext__adv__param.md#a08aa741a56e825a11424bf024ac65e14)[3];

[ 1531](structbt__hci__cp__le__set__ext__adv__param.md#ad7a0b9028bcdb57a9011d4677412aed5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [prim\_channel\_map](structbt__hci__cp__le__set__ext__adv__param.md#ad7a0b9028bcdb57a9011d4677412aed5);

[ 1532](structbt__hci__cp__le__set__ext__adv__param.md#a3594f7337ccd739f59ac7845757de0e8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [own\_addr\_type](structbt__hci__cp__le__set__ext__adv__param.md#a3594f7337ccd739f59ac7845757de0e8);

[ 1533](structbt__hci__cp__le__set__ext__adv__param.md#a819e599df4025036fab2dabd7c61ea37) [bt\_addr\_le\_t](structbt__addr__le__t.md) [peer\_addr](structbt__hci__cp__le__set__ext__adv__param.md#a819e599df4025036fab2dabd7c61ea37);

[ 1534](structbt__hci__cp__le__set__ext__adv__param.md#a29a62f8989f89b014cadbad9b94e996a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter\_policy](structbt__hci__cp__le__set__ext__adv__param.md#a29a62f8989f89b014cadbad9b94e996a);

[ 1535](structbt__hci__cp__le__set__ext__adv__param.md#a5f7f3e477b5b0b8122b85f3e53dd7878) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__hci__cp__le__set__ext__adv__param.md#a5f7f3e477b5b0b8122b85f3e53dd7878);

[ 1536](structbt__hci__cp__le__set__ext__adv__param.md#a048874197ccbdbc626f0563be5c41ec7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [prim\_adv\_phy](structbt__hci__cp__le__set__ext__adv__param.md#a048874197ccbdbc626f0563be5c41ec7);

[ 1537](structbt__hci__cp__le__set__ext__adv__param.md#a5793c6afe545290a1e792bcc73585b72) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sec\_adv\_max\_skip](structbt__hci__cp__le__set__ext__adv__param.md#a5793c6afe545290a1e792bcc73585b72);

[ 1538](structbt__hci__cp__le__set__ext__adv__param.md#abc82ba984647eb00bc490c01ce746a15) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sec\_adv\_phy](structbt__hci__cp__le__set__ext__adv__param.md#abc82ba984647eb00bc490c01ce746a15);

[ 1539](structbt__hci__cp__le__set__ext__adv__param.md#af8bc3509fdd5e89c27db466727fe1cd9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__hci__cp__le__set__ext__adv__param.md#af8bc3509fdd5e89c27db466727fe1cd9);

[ 1540](structbt__hci__cp__le__set__ext__adv__param.md#ae694df46b1db4b029d1e177768b3821f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [scan\_req\_notify\_enable](structbt__hci__cp__le__set__ext__adv__param.md#ae694df46b1db4b029d1e177768b3821f);

1541} \_\_packed;

[ 1542](structbt__hci__rp__le__set__ext__adv__param.md)struct [bt\_hci\_rp\_le\_set\_ext\_adv\_param](structbt__hci__rp__le__set__ext__adv__param.md) {

[ 1543](structbt__hci__rp__le__set__ext__adv__param.md#a6baae317455ffbb489066fcd1fb068c8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__set__ext__adv__param.md#a6baae317455ffbb489066fcd1fb068c8);

[ 1544](structbt__hci__rp__le__set__ext__adv__param.md#a8a876d0e3d4d9d066a27c054569f0b9a) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__hci__rp__le__set__ext__adv__param.md#a8a876d0e3d4d9d066a27c054569f0b9a);

1545} \_\_packed;

1546

[ 1547](hci__types_8h.md#a2ba70856f1e7fe8c6e7990ac9cdf5aaa)#define BT\_HCI\_LE\_ADV\_PHY\_OPTION\_NO\_REQUIRED 0x00

[ 1548](hci__types_8h.md#ac707220fea6b3fc077b8b85267ed0030)#define BT\_HCI\_LE\_ADV\_PHY\_OPTION\_REQUIRE\_S2 0x03

[ 1549](hci__types_8h.md#aab845a49577d93974b468187c948beff)#define BT\_HCI\_LE\_ADV\_PHY\_OPTION\_REQUIRE\_S8 0x04

1550

[ 1551](hci__types_8h.md#a66ffb876e588d64ce2b2d9091de94806)#define BT\_HCI\_OP\_LE\_SET\_EXT\_ADV\_PARAM\_V2 BT\_OP(BT\_OGF\_LE, 0x007F) /\* 0x207F \*/

[ 1552](structbt__hci__cp__le__set__ext__adv__param__v2.md)struct [bt\_hci\_cp\_le\_set\_ext\_adv\_param\_v2](structbt__hci__cp__le__set__ext__adv__param__v2.md) {

[ 1553](structbt__hci__cp__le__set__ext__adv__param__v2.md#ad9e43219b471e44884b33ea5ddd90513) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle](structbt__hci__cp__le__set__ext__adv__param__v2.md#ad9e43219b471e44884b33ea5ddd90513);

[ 1554](structbt__hci__cp__le__set__ext__adv__param__v2.md#aff572d12a03ca9cbc2ee80f75e1f77c7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [props](structbt__hci__cp__le__set__ext__adv__param__v2.md#aff572d12a03ca9cbc2ee80f75e1f77c7);

[ 1555](structbt__hci__cp__le__set__ext__adv__param__v2.md#a25fec4dc9203bb50bb030087b42f473e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [prim\_min\_interval](structbt__hci__cp__le__set__ext__adv__param__v2.md#a25fec4dc9203bb50bb030087b42f473e)[3];

[ 1556](structbt__hci__cp__le__set__ext__adv__param__v2.md#a6098216ae6ef0f9459aae16adecd193f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [prim\_max\_interval](structbt__hci__cp__le__set__ext__adv__param__v2.md#a6098216ae6ef0f9459aae16adecd193f)[3];

[ 1557](structbt__hci__cp__le__set__ext__adv__param__v2.md#a1a96a88729e311c6a60571997aae9fc3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [prim\_channel\_map](structbt__hci__cp__le__set__ext__adv__param__v2.md#a1a96a88729e311c6a60571997aae9fc3);

[ 1558](structbt__hci__cp__le__set__ext__adv__param__v2.md#a554f89f00700bc3ea4996b0a971fedbf) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [own\_addr\_type](structbt__hci__cp__le__set__ext__adv__param__v2.md#a554f89f00700bc3ea4996b0a971fedbf);

[ 1559](structbt__hci__cp__le__set__ext__adv__param__v2.md#ad8fccd11fbea598de62e057a69b72156) [bt\_addr\_le\_t](structbt__addr__le__t.md) [peer\_addr](structbt__hci__cp__le__set__ext__adv__param__v2.md#ad8fccd11fbea598de62e057a69b72156);

[ 1560](structbt__hci__cp__le__set__ext__adv__param__v2.md#a047656dd56bf883f1e307dcabe96f1de) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter\_policy](structbt__hci__cp__le__set__ext__adv__param__v2.md#a047656dd56bf883f1e307dcabe96f1de);

[ 1561](structbt__hci__cp__le__set__ext__adv__param__v2.md#a5283a6a40d46e0fe787ed403acab9f90) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__hci__cp__le__set__ext__adv__param__v2.md#a5283a6a40d46e0fe787ed403acab9f90);

[ 1562](structbt__hci__cp__le__set__ext__adv__param__v2.md#a92a215151c603c2f8dd1b7e730a8e979) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [prim\_adv\_phy](structbt__hci__cp__le__set__ext__adv__param__v2.md#a92a215151c603c2f8dd1b7e730a8e979);

[ 1563](structbt__hci__cp__le__set__ext__adv__param__v2.md#ac31b52df1033d11585781fbecc10f578) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sec\_adv\_max\_skip](structbt__hci__cp__le__set__ext__adv__param__v2.md#ac31b52df1033d11585781fbecc10f578);

[ 1564](structbt__hci__cp__le__set__ext__adv__param__v2.md#a6c2a953fab938f304e815bd9d59d05ae) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sec\_adv\_phy](structbt__hci__cp__le__set__ext__adv__param__v2.md#a6c2a953fab938f304e815bd9d59d05ae);

[ 1565](structbt__hci__cp__le__set__ext__adv__param__v2.md#aeb26f7f16e2c71542421aada577a993f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__hci__cp__le__set__ext__adv__param__v2.md#aeb26f7f16e2c71542421aada577a993f);

[ 1566](structbt__hci__cp__le__set__ext__adv__param__v2.md#a9f2a6f38e8965dabe17ad743d3aeda70) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [scan\_req\_notify\_enable](structbt__hci__cp__le__set__ext__adv__param__v2.md#a9f2a6f38e8965dabe17ad743d3aeda70);

[ 1567](structbt__hci__cp__le__set__ext__adv__param__v2.md#a8767fb7f5492f0323edd9afb687318db) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [prim\_adv\_phy\_opt](structbt__hci__cp__le__set__ext__adv__param__v2.md#a8767fb7f5492f0323edd9afb687318db);

[ 1568](structbt__hci__cp__le__set__ext__adv__param__v2.md#a0c7994ef034270a7fd814386e7b76cc8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sec\_adv\_phy\_opt](structbt__hci__cp__le__set__ext__adv__param__v2.md#a0c7994ef034270a7fd814386e7b76cc8);

1569} \_\_packed;

1570

[ 1571](hci__types_8h.md#a68c62ac99c4198dbadf6563e40ce33cb)#define BT\_HCI\_LE\_EXT\_ADV\_OP\_INTERM\_FRAG 0x00

[ 1572](hci__types_8h.md#a65b3ae46e1164815cda1325e55df4091)#define BT\_HCI\_LE\_EXT\_ADV\_OP\_FIRST\_FRAG 0x01

[ 1573](hci__types_8h.md#aade6b8cac66aee356c857fcfae17ce65)#define BT\_HCI\_LE\_EXT\_ADV\_OP\_LAST\_FRAG 0x02

[ 1574](hci__types_8h.md#a5394a0dbcd3856ffb8c63440d352120b)#define BT\_HCI\_LE\_EXT\_ADV\_OP\_COMPLETE\_DATA 0x03

[ 1575](hci__types_8h.md#a2860ae578d2332a1c76c7bfaa0714e08)#define BT\_HCI\_LE\_EXT\_ADV\_OP\_UNCHANGED\_DATA 0x04

1576

[ 1577](hci__types_8h.md#aa1dbb6b62c021501320865ac77b5d6da)#define BT\_HCI\_LE\_EXT\_ADV\_FRAG\_ENABLED 0x00

[ 1578](hci__types_8h.md#a4d9626f1b9f0601708b3c38386b5f85c)#define BT\_HCI\_LE\_EXT\_ADV\_FRAG\_DISABLED 0x01

1579

[ 1580](hci__types_8h.md#a3b3f91c046b0656d489c228d75c8b3ff)#define BT\_HCI\_LE\_EXT\_ADV\_FRAG\_MAX\_LEN 251

1581

[ 1582](hci__types_8h.md#a563769ae57bb58be9d7ee8e92019cb99)#define BT\_HCI\_OP\_LE\_SET\_EXT\_ADV\_DATA BT\_OP(BT\_OGF\_LE, 0x0037) /\* 0x2037 \*/

[ 1583](structbt__hci__cp__le__set__ext__adv__data.md)struct [bt\_hci\_cp\_le\_set\_ext\_adv\_data](structbt__hci__cp__le__set__ext__adv__data.md) {

[ 1584](structbt__hci__cp__le__set__ext__adv__data.md#a803bb793eefcc714c6c4034123a2e487) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle](structbt__hci__cp__le__set__ext__adv__data.md#a803bb793eefcc714c6c4034123a2e487);

[ 1585](structbt__hci__cp__le__set__ext__adv__data.md#ac5eaa1834f82024055923d08a3bef6b3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [op](structbt__hci__cp__le__set__ext__adv__data.md#ac5eaa1834f82024055923d08a3bef6b3);

[ 1586](structbt__hci__cp__le__set__ext__adv__data.md#af9eef9f59bfec5867ea36bdf33e3a9b1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [frag\_pref](structbt__hci__cp__le__set__ext__adv__data.md#af9eef9f59bfec5867ea36bdf33e3a9b1);

[ 1587](structbt__hci__cp__le__set__ext__adv__data.md#aea3055cc7ffbaf4cd14996d885e21ba3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structbt__hci__cp__le__set__ext__adv__data.md#aea3055cc7ffbaf4cd14996d885e21ba3);

[ 1588](structbt__hci__cp__le__set__ext__adv__data.md#a7d7df52500eb53a64b6ba5e62f6cf14f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__hci__cp__le__set__ext__adv__data.md#a7d7df52500eb53a64b6ba5e62f6cf14f)[0];

1589} \_\_packed;

1590

[ 1591](hci__types_8h.md#a586395798b3d827ab17634287862ef54)#define BT\_HCI\_OP\_LE\_SET\_EXT\_SCAN\_RSP\_DATA BT\_OP(BT\_OGF\_LE, 0x0038) /\* 0x2038 \*/

[ 1592](structbt__hci__cp__le__set__ext__scan__rsp__data.md)struct [bt\_hci\_cp\_le\_set\_ext\_scan\_rsp\_data](structbt__hci__cp__le__set__ext__scan__rsp__data.md) {

[ 1593](structbt__hci__cp__le__set__ext__scan__rsp__data.md#a8cf0624b9968686c7f6765ee25e11c90) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle](structbt__hci__cp__le__set__ext__scan__rsp__data.md#a8cf0624b9968686c7f6765ee25e11c90);

[ 1594](structbt__hci__cp__le__set__ext__scan__rsp__data.md#a3323a0844680b71cb8aedffa034837d7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [op](structbt__hci__cp__le__set__ext__scan__rsp__data.md#a3323a0844680b71cb8aedffa034837d7);

[ 1595](structbt__hci__cp__le__set__ext__scan__rsp__data.md#ac4e1691926df370b290c9e6d866d310d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [frag\_pref](structbt__hci__cp__le__set__ext__scan__rsp__data.md#ac4e1691926df370b290c9e6d866d310d);

[ 1596](structbt__hci__cp__le__set__ext__scan__rsp__data.md#a6024eac85f600ed3b7051a84b91bdcfa) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structbt__hci__cp__le__set__ext__scan__rsp__data.md#a6024eac85f600ed3b7051a84b91bdcfa);

[ 1597](structbt__hci__cp__le__set__ext__scan__rsp__data.md#ab086720e1a22523ba155cb238ad75197) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__hci__cp__le__set__ext__scan__rsp__data.md#ab086720e1a22523ba155cb238ad75197)[0];

1598} \_\_packed;

1599

[ 1600](hci__types_8h.md#a99e9573f9bd290fb18f82a327ca55ecd)#define BT\_HCI\_OP\_LE\_SET\_EXT\_ADV\_ENABLE BT\_OP(BT\_OGF\_LE, 0x0039) /\* 0x2039 \*/

[ 1601](structbt__hci__ext__adv__set.md)struct [bt\_hci\_ext\_adv\_set](structbt__hci__ext__adv__set.md) {

[ 1602](structbt__hci__ext__adv__set.md#a9d0fd3f6659db172ff4efd74c2c2d216) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle](structbt__hci__ext__adv__set.md#a9d0fd3f6659db172ff4efd74c2c2d216);

[ 1603](structbt__hci__ext__adv__set.md#acc2afc91fe5c0dfcb4c95eaade4a047a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [duration](structbt__hci__ext__adv__set.md#acc2afc91fe5c0dfcb4c95eaade4a047a);

[ 1604](structbt__hci__ext__adv__set.md#a4467ac9a564ea24bb701de46cda2579a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_ext\_adv\_evts](structbt__hci__ext__adv__set.md#a4467ac9a564ea24bb701de46cda2579a);

1605} \_\_packed;

1606

[ 1607](structbt__hci__cp__le__set__ext__adv__enable.md)struct [bt\_hci\_cp\_le\_set\_ext\_adv\_enable](structbt__hci__cp__le__set__ext__adv__enable.md) {

[ 1608](structbt__hci__cp__le__set__ext__adv__enable.md#ab7148b47bf052d8cba1f6bf3385051c8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enable](structbt__hci__cp__le__set__ext__adv__enable.md#ab7148b47bf052d8cba1f6bf3385051c8);

[ 1609](structbt__hci__cp__le__set__ext__adv__enable.md#a06088af8b432ac134943d9ebb7778ac7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [set\_num](structbt__hci__cp__le__set__ext__adv__enable.md#a06088af8b432ac134943d9ebb7778ac7);

[ 1610](structbt__hci__cp__le__set__ext__adv__enable.md#a04911e19f3b2f0079d4e12980d11157f) struct [bt\_hci\_ext\_adv\_set](structbt__hci__ext__adv__set.md) [s](structbt__hci__cp__le__set__ext__adv__enable.md#a04911e19f3b2f0079d4e12980d11157f)[0];

1611} \_\_packed;

1612

[ 1613](hci__types_8h.md#a0246ea11fada7570bf59e73250b49b95)#define BT\_HCI\_OP\_LE\_READ\_MAX\_ADV\_DATA\_LEN BT\_OP(BT\_OGF\_LE, 0x003a) /\* 0x203a \*/

[ 1614](structbt__hci__rp__le__read__max__adv__data__len.md)struct [bt\_hci\_rp\_le\_read\_max\_adv\_data\_len](structbt__hci__rp__le__read__max__adv__data__len.md) {

[ 1615](structbt__hci__rp__le__read__max__adv__data__len.md#a978911dc5028d1f36820447de8e9e5f7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__max__adv__data__len.md#a978911dc5028d1f36820447de8e9e5f7);

[ 1616](structbt__hci__rp__le__read__max__adv__data__len.md#aa4084a89de4929c3e8e2630d0aad7f82) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_adv\_data\_len](structbt__hci__rp__le__read__max__adv__data__len.md#aa4084a89de4929c3e8e2630d0aad7f82);

1617} \_\_packed;

1618

[ 1619](hci__types_8h.md#a8d2a855322d0aa454ed00e1458cf9a38)#define BT\_HCI\_OP\_LE\_READ\_NUM\_ADV\_SETS BT\_OP(BT\_OGF\_LE, 0x003b) /\* 0x203b \*/

[ 1620](structbt__hci__rp__le__read__num__adv__sets.md)struct [bt\_hci\_rp\_le\_read\_num\_adv\_sets](structbt__hci__rp__le__read__num__adv__sets.md) {

[ 1621](structbt__hci__rp__le__read__num__adv__sets.md#a590934059fb851a14b2eec66f32a5334) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__num__adv__sets.md#a590934059fb851a14b2eec66f32a5334);

[ 1622](structbt__hci__rp__le__read__num__adv__sets.md#a7dd26bda7a8ab75fed2af19bb5af34fc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_sets](structbt__hci__rp__le__read__num__adv__sets.md#a7dd26bda7a8ab75fed2af19bb5af34fc);

1623} \_\_packed;

1624

[ 1625](hci__types_8h.md#ae802afd7081a39f062f65e5c0994a9e4)#define BT\_HCI\_OP\_LE\_REMOVE\_ADV\_SET BT\_OP(BT\_OGF\_LE, 0x003c) /\* 0x203c \*/

[ 1626](structbt__hci__cp__le__remove__adv__set.md)struct [bt\_hci\_cp\_le\_remove\_adv\_set](structbt__hci__cp__le__remove__adv__set.md) {

[ 1627](structbt__hci__cp__le__remove__adv__set.md#ab33bf918b10d847bb8fb8ac2409780e6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle](structbt__hci__cp__le__remove__adv__set.md#ab33bf918b10d847bb8fb8ac2409780e6);

1628} \_\_packed;

1629

[ 1630](hci__types_8h.md#a2f95e881ffcda381d8d8ad7ba8705e7d)#define BT\_HCI\_OP\_CLEAR\_ADV\_SETS BT\_OP(BT\_OGF\_LE, 0x003d) /\* 0x203d \*/

1631

[ 1632](hci__types_8h.md#a04f870ac03c1baca22ab5d984354f3bf)#define BT\_HCI\_LE\_PER\_ADV\_INTERVAL\_MIN 0x0006

[ 1633](hci__types_8h.md#a2f2216a88cf77ccac1c9a2f6c5820746)#define BT\_HCI\_LE\_PER\_ADV\_INTERVAL\_MAX 0xFFFF

1634

[ 1635](hci__types_8h.md#a3a111d29fd682fa825f4f9c8c358243f)#define BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_PARAM BT\_OP(BT\_OGF\_LE, 0x003e) /\* 0x203e \*/

[ 1636](structbt__hci__cp__le__set__per__adv__param.md)struct [bt\_hci\_cp\_le\_set\_per\_adv\_param](structbt__hci__cp__le__set__per__adv__param.md) {

[ 1637](structbt__hci__cp__le__set__per__adv__param.md#a2b61031952b3893add7677d3802e368b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle](structbt__hci__cp__le__set__per__adv__param.md#a2b61031952b3893add7677d3802e368b);

[ 1638](structbt__hci__cp__le__set__per__adv__param.md#af01696ef6bf02e7db37d45a0c9852ef5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [min\_interval](structbt__hci__cp__le__set__per__adv__param.md#af01696ef6bf02e7db37d45a0c9852ef5);

[ 1639](structbt__hci__cp__le__set__per__adv__param.md#a1a2a69ea6e310710892184ced472eb8a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_interval](structbt__hci__cp__le__set__per__adv__param.md#a1a2a69ea6e310710892184ced472eb8a);

[ 1640](structbt__hci__cp__le__set__per__adv__param.md#a879ea10e1ab217b4aa49dfcf3b394691) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [props](structbt__hci__cp__le__set__per__adv__param.md#a879ea10e1ab217b4aa49dfcf3b394691);

1641} \_\_packed;

1642

[ 1643](hci__types_8h.md#aa18edf54edfb8d0fcaca5941e8e5e493)#define BT\_HCI\_LE\_PER\_ADV\_OP\_INTERM\_FRAG 0x00

[ 1644](hci__types_8h.md#a8aeb4c76ec769879fc4796fc2919c459)#define BT\_HCI\_LE\_PER\_ADV\_OP\_FIRST\_FRAG 0x01

[ 1645](hci__types_8h.md#a7f2314472ccb051e87d1bb2f9b3fded8)#define BT\_HCI\_LE\_PER\_ADV\_OP\_LAST\_FRAG 0x02

[ 1646](hci__types_8h.md#ada39c45c3c1c7576d4d9794dad115e61)#define BT\_HCI\_LE\_PER\_ADV\_OP\_COMPLETE\_DATA 0x03

1647

[ 1648](hci__types_8h.md#a7b3cd7870ba4af2ff483a831d2700466)#define BT\_HCI\_LE\_PER\_ADV\_FRAG\_MAX\_LEN 252

1649

[ 1650](hci__types_8h.md#ae6611e7b72b057ac9d4004a1772fe435)#define BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_DATA BT\_OP(BT\_OGF\_LE, 0x003f) /\* 0x203f \*/

[ 1651](structbt__hci__cp__le__set__per__adv__data.md)struct [bt\_hci\_cp\_le\_set\_per\_adv\_data](structbt__hci__cp__le__set__per__adv__data.md) {

[ 1652](structbt__hci__cp__le__set__per__adv__data.md#a93cbb46ce6664880487e009a0b47af02) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle](structbt__hci__cp__le__set__per__adv__data.md#a93cbb46ce6664880487e009a0b47af02);

[ 1653](structbt__hci__cp__le__set__per__adv__data.md#aac34596f0970c976c4ef71250d326c2c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [op](structbt__hci__cp__le__set__per__adv__data.md#aac34596f0970c976c4ef71250d326c2c);

[ 1654](structbt__hci__cp__le__set__per__adv__data.md#ae6ee631a153cb6fed88695e599f63e91) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structbt__hci__cp__le__set__per__adv__data.md#ae6ee631a153cb6fed88695e599f63e91);

[ 1655](structbt__hci__cp__le__set__per__adv__data.md#adaf581f8db6aafb4dc5df669df7ad26d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__hci__cp__le__set__per__adv__data.md#adaf581f8db6aafb4dc5df669df7ad26d)[0];

1656} \_\_packed;

1657

[ 1658](hci__types_8h.md#a1c03932d8c1e2c5436eaf45be093b4d4)#define BT\_HCI\_LE\_SET\_PER\_ADV\_ENABLE\_ENABLE BIT(0)

[ 1659](hci__types_8h.md#aaf9b76b276b5cf7e02bb5e3b0a12ecf6)#define BT\_HCI\_LE\_SET\_PER\_ADV\_ENABLE\_ADI BIT(1)

1660

[ 1661](hci__types_8h.md#a3ae23554c13b099b50b129462e08afe4)#define BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_ENABLE BT\_OP(BT\_OGF\_LE, 0x0040) /\* 0x2040 \*/

[ 1662](structbt__hci__cp__le__set__per__adv__enable.md)struct [bt\_hci\_cp\_le\_set\_per\_adv\_enable](structbt__hci__cp__le__set__per__adv__enable.md) {

[ 1663](structbt__hci__cp__le__set__per__adv__enable.md#afff649b908264c617b249bcfbebadd53) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enable](structbt__hci__cp__le__set__per__adv__enable.md#afff649b908264c617b249bcfbebadd53);

[ 1664](structbt__hci__cp__le__set__per__adv__enable.md#a998f4e38a56f771f234ce099b4528a3d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle](structbt__hci__cp__le__set__per__adv__enable.md#a998f4e38a56f771f234ce099b4528a3d);

1665} \_\_packed;

1666

[ 1667](hci__types_8h.md#a7b0687c9e1faae997b76ece821338fd7)#define BT\_HCI\_OP\_LE\_SET\_EXT\_SCAN\_PARAM BT\_OP(BT\_OGF\_LE, 0x0041) /\* 0x2041 \*/

[ 1668](structbt__hci__ext__scan__phy.md)struct [bt\_hci\_ext\_scan\_phy](structbt__hci__ext__scan__phy.md) {

[ 1669](structbt__hci__ext__scan__phy.md#a4cfebc7b2709973953bed9a09a793b7e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__hci__ext__scan__phy.md#a4cfebc7b2709973953bed9a09a793b7e);

[ 1670](structbt__hci__ext__scan__phy.md#a2f087d18bde86d0ac81a14a09ae5b9b0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__hci__ext__scan__phy.md#a2f087d18bde86d0ac81a14a09ae5b9b0);

[ 1671](structbt__hci__ext__scan__phy.md#a9c0196f0d5f0064796c15a5df2ad4c07) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [window](structbt__hci__ext__scan__phy.md#a9c0196f0d5f0064796c15a5df2ad4c07);

1672} \_\_packed;

1673

[ 1674](hci__types_8h.md#a0ef6a16a2b042b3e7623210fc5fcd1a0)#define BT\_HCI\_LE\_EXT\_SCAN\_PHY\_1M BIT(0)

[ 1675](hci__types_8h.md#ad0f0fe21e4e9136e09e0a443a7253759)#define BT\_HCI\_LE\_EXT\_SCAN\_PHY\_2M BIT(1)

[ 1676](hci__types_8h.md#ae15b1ae9e35d060b3a9619d293a7d9ac)#define BT\_HCI\_LE\_EXT\_SCAN\_PHY\_CODED BIT(2)

1677

[ 1678](structbt__hci__cp__le__set__ext__scan__param.md)struct [bt\_hci\_cp\_le\_set\_ext\_scan\_param](structbt__hci__cp__le__set__ext__scan__param.md) {

[ 1679](structbt__hci__cp__le__set__ext__scan__param.md#a3418aa8dbdb8062ee452f5756eb9f30c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [own\_addr\_type](structbt__hci__cp__le__set__ext__scan__param.md#a3418aa8dbdb8062ee452f5756eb9f30c);

[ 1680](structbt__hci__cp__le__set__ext__scan__param.md#a47f6cf7f83451dcc2feac1a8d5837ad8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter\_policy](structbt__hci__cp__le__set__ext__scan__param.md#a47f6cf7f83451dcc2feac1a8d5837ad8);

[ 1681](structbt__hci__cp__le__set__ext__scan__param.md#a6c38b7d074eb3c0cf5c301eb6c03b60c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phys](structbt__hci__cp__le__set__ext__scan__param.md#a6c38b7d074eb3c0cf5c301eb6c03b60c);

[ 1682](structbt__hci__cp__le__set__ext__scan__param.md#ab4eab9a52dca01bc19b35607d6ec5d36) struct [bt\_hci\_ext\_scan\_phy](structbt__hci__ext__scan__phy.md) [p](structbt__hci__cp__le__set__ext__scan__param.md#ab4eab9a52dca01bc19b35607d6ec5d36)[0];

1683} \_\_packed;

1684

1685/\* Extends BT\_HCI\_LE\_SCAN\_FILTER\_DUP \*/

[ 1686](hci__types_8h.md#ae9ba6da1a01dacc52c6a1a2c84d16948)#define BT\_HCI\_LE\_EXT\_SCAN\_FILTER\_DUP\_ENABLE\_RESET 0x02

1687

[ 1688](hci__types_8h.md#af7a8256887657e482084d4ed3810195b)#define BT\_HCI\_OP\_LE\_SET\_EXT\_SCAN\_ENABLE BT\_OP(BT\_OGF\_LE, 0x0042) /\* 0x2042 \*/

[ 1689](structbt__hci__cp__le__set__ext__scan__enable.md)struct [bt\_hci\_cp\_le\_set\_ext\_scan\_enable](structbt__hci__cp__le__set__ext__scan__enable.md) {

[ 1690](structbt__hci__cp__le__set__ext__scan__enable.md#a922d0c5a7ccb6c1e1864f662227b8307) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enable](structbt__hci__cp__le__set__ext__scan__enable.md#a922d0c5a7ccb6c1e1864f662227b8307);

[ 1691](structbt__hci__cp__le__set__ext__scan__enable.md#aa5b0939838ab13eb8299f4a4b2fd3f14) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter\_dup](structbt__hci__cp__le__set__ext__scan__enable.md#aa5b0939838ab13eb8299f4a4b2fd3f14);

[ 1692](structbt__hci__cp__le__set__ext__scan__enable.md#adcd5e00a240f3e7395d0d25994b4013a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [duration](structbt__hci__cp__le__set__ext__scan__enable.md#adcd5e00a240f3e7395d0d25994b4013a);

[ 1693](structbt__hci__cp__le__set__ext__scan__enable.md#aa60c8ade7047dcd202d83cfc3f18ada2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [period](structbt__hci__cp__le__set__ext__scan__enable.md#aa60c8ade7047dcd202d83cfc3f18ada2);

1694} \_\_packed;

1695

[ 1696](hci__types_8h.md#ac498c9cd93b664b5bd2e58982d36d7ad)#define BT\_HCI\_OP\_LE\_EXT\_CREATE\_CONN BT\_OP(BT\_OGF\_LE, 0x0043) /\* 0x2043 \*/

[ 1697](hci__types_8h.md#a1b6bc4da843ed8d04e0b9571465ffd12)#define BT\_HCI\_OP\_LE\_EXT\_CREATE\_CONN\_V2 BT\_OP(BT\_OGF\_LE, 0x0085) /\* 0x2085 \*/

[ 1698](structbt__hci__ext__conn__phy.md)struct [bt\_hci\_ext\_conn\_phy](structbt__hci__ext__conn__phy.md) {

[ 1699](structbt__hci__ext__conn__phy.md#a4f78503fe42ee81fea740ba1643a732e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [scan\_interval](structbt__hci__ext__conn__phy.md#a4f78503fe42ee81fea740ba1643a732e);

[ 1700](structbt__hci__ext__conn__phy.md#ae0e950c8004bd595631f95a289a5c871) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [scan\_window](structbt__hci__ext__conn__phy.md#ae0e950c8004bd595631f95a289a5c871);

[ 1701](structbt__hci__ext__conn__phy.md#a7fc06c1a458aedb6b29381450a5a4df0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_interval\_min](structbt__hci__ext__conn__phy.md#a7fc06c1a458aedb6b29381450a5a4df0);

[ 1702](structbt__hci__ext__conn__phy.md#a7bcf66a3372d92c809d8427796915b88) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_interval\_max](structbt__hci__ext__conn__phy.md#a7bcf66a3372d92c809d8427796915b88);

[ 1703](structbt__hci__ext__conn__phy.md#a7dd57b7ef0b13b15da47e92076f87d79) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_latency](structbt__hci__ext__conn__phy.md#a7dd57b7ef0b13b15da47e92076f87d79);

[ 1704](structbt__hci__ext__conn__phy.md#aaec54c0743dfc08923b5ccd8fc1a4015) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [supervision\_timeout](structbt__hci__ext__conn__phy.md#aaec54c0743dfc08923b5ccd8fc1a4015);

[ 1705](structbt__hci__ext__conn__phy.md#af48212961ce21f5222e57f70ffeb811b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [min\_ce\_len](structbt__hci__ext__conn__phy.md#af48212961ce21f5222e57f70ffeb811b);

[ 1706](structbt__hci__ext__conn__phy.md#a3c3ccb93014758b3215718d2672ce7f3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_ce\_len](structbt__hci__ext__conn__phy.md#a3c3ccb93014758b3215718d2672ce7f3);

1707} \_\_packed;

1708

[ 1709](structbt__hci__cp__le__ext__create__conn.md)struct [bt\_hci\_cp\_le\_ext\_create\_conn](structbt__hci__cp__le__ext__create__conn.md) {

[ 1710](structbt__hci__cp__le__ext__create__conn.md#a0561b446effa3f735a405c0b307466bf) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter\_policy](structbt__hci__cp__le__ext__create__conn.md#a0561b446effa3f735a405c0b307466bf);

[ 1711](structbt__hci__cp__le__ext__create__conn.md#a12a99044f54e3d5dae30a64392444cbf) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [own\_addr\_type](structbt__hci__cp__le__ext__create__conn.md#a12a99044f54e3d5dae30a64392444cbf);

[ 1712](structbt__hci__cp__le__ext__create__conn.md#a79bc55d9f5b1d719de4fb404db9008f3) [bt\_addr\_le\_t](structbt__addr__le__t.md) [peer\_addr](structbt__hci__cp__le__ext__create__conn.md#a79bc55d9f5b1d719de4fb404db9008f3);

[ 1713](structbt__hci__cp__le__ext__create__conn.md#ae859ff0da5e9cdc872943fd74774ef7e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phys](structbt__hci__cp__le__ext__create__conn.md#ae859ff0da5e9cdc872943fd74774ef7e);

[ 1714](structbt__hci__cp__le__ext__create__conn.md#acdb436d6bf2864745ec579622ae0d532) struct [bt\_hci\_ext\_conn\_phy](structbt__hci__ext__conn__phy.md) [p](structbt__hci__cp__le__ext__create__conn.md#acdb436d6bf2864745ec579622ae0d532)[0];

1715} \_\_packed;

1716

[ 1717](structbt__hci__cp__le__ext__create__conn__v2.md)struct [bt\_hci\_cp\_le\_ext\_create\_conn\_v2](structbt__hci__cp__le__ext__create__conn__v2.md) {

[ 1718](structbt__hci__cp__le__ext__create__conn__v2.md#addf1f80c4d3625e0c6d6e716f6e2e207) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_handle](structbt__hci__cp__le__ext__create__conn__v2.md#addf1f80c4d3625e0c6d6e716f6e2e207);

[ 1719](structbt__hci__cp__le__ext__create__conn__v2.md#a536da199958b3b54469f5b4b029e1bac) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent](structbt__hci__cp__le__ext__create__conn__v2.md#a536da199958b3b54469f5b4b029e1bac);

[ 1720](structbt__hci__cp__le__ext__create__conn__v2.md#a66632dbac1605cff69e8da566e800347) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter\_policy](structbt__hci__cp__le__ext__create__conn__v2.md#a66632dbac1605cff69e8da566e800347);

[ 1721](structbt__hci__cp__le__ext__create__conn__v2.md#a05fd0089a0fd43f98042835231407a60) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [own\_addr\_type](structbt__hci__cp__le__ext__create__conn__v2.md#a05fd0089a0fd43f98042835231407a60);

[ 1722](structbt__hci__cp__le__ext__create__conn__v2.md#a25466a04d224bdf495266b0064c424dd) [bt\_addr\_le\_t](structbt__addr__le__t.md) [peer\_addr](structbt__hci__cp__le__ext__create__conn__v2.md#a25466a04d224bdf495266b0064c424dd);

[ 1723](structbt__hci__cp__le__ext__create__conn__v2.md#ae2d3e3079a2848907224bb7ff0efc64b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phys](structbt__hci__cp__le__ext__create__conn__v2.md#ae2d3e3079a2848907224bb7ff0efc64b);

[ 1724](structbt__hci__cp__le__ext__create__conn__v2.md#a8d606c5aa480f54c8da9f42a35ad513e) struct [bt\_hci\_ext\_conn\_phy](structbt__hci__ext__conn__phy.md) [p](structbt__hci__cp__le__ext__create__conn__v2.md#a8d606c5aa480f54c8da9f42a35ad513e)[0];

1725} \_\_packed;

1726

[ 1727](hci__types_8h.md#a44e729aebc339ada5deb86ad9d350404)#define BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_SUBEVENT\_DATA BT\_OP(BT\_OGF\_LE, 0x0082) /\* 0x2082 \*/

[ 1728](structbt__hci__cp__le__set__pawr__subevent__data__element.md)struct [bt\_hci\_cp\_le\_set\_pawr\_subevent\_data\_element](structbt__hci__cp__le__set__pawr__subevent__data__element.md) {

[ 1729](structbt__hci__cp__le__set__pawr__subevent__data__element.md#abf33f93f0f1ddf3532c6cae13483ec1e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent](structbt__hci__cp__le__set__pawr__subevent__data__element.md#abf33f93f0f1ddf3532c6cae13483ec1e);

[ 1730](structbt__hci__cp__le__set__pawr__subevent__data__element.md#a90178bcd86c1bad0a768f391ce11613f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot\_start](structbt__hci__cp__le__set__pawr__subevent__data__element.md#a90178bcd86c1bad0a768f391ce11613f);

[ 1731](structbt__hci__cp__le__set__pawr__subevent__data__element.md#ad8da1cc672eedf8be8cfc7d0d7ec1b41) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot\_count](structbt__hci__cp__le__set__pawr__subevent__data__element.md#ad8da1cc672eedf8be8cfc7d0d7ec1b41);

[ 1732](structbt__hci__cp__le__set__pawr__subevent__data__element.md#ace5860dfa0f628eaed2b68b171d875da) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent\_data\_length](structbt__hci__cp__le__set__pawr__subevent__data__element.md#ace5860dfa0f628eaed2b68b171d875da);

[ 1733](structbt__hci__cp__le__set__pawr__subevent__data__element.md#a91c975189e409b733ac9a4af5763b12a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent\_data](structbt__hci__cp__le__set__pawr__subevent__data__element.md#a91c975189e409b733ac9a4af5763b12a)[0];

1734} \_\_packed;

1735

[ 1736](structbt__hci__cp__le__set__pawr__subevent__data.md)struct [bt\_hci\_cp\_le\_set\_pawr\_subevent\_data](structbt__hci__cp__le__set__pawr__subevent__data.md) {

[ 1737](structbt__hci__cp__le__set__pawr__subevent__data.md#a47d84125d15cce1fc969db3e5caa07e1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_handle](structbt__hci__cp__le__set__pawr__subevent__data.md#a47d84125d15cce1fc969db3e5caa07e1);

[ 1738](structbt__hci__cp__le__set__pawr__subevent__data.md#a9397eebd6771ad159d1bdae0d59e5f46) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_subevents](structbt__hci__cp__le__set__pawr__subevent__data.md#a9397eebd6771ad159d1bdae0d59e5f46);

[ 1739](structbt__hci__cp__le__set__pawr__subevent__data.md#aa932c1f19de96f89a79bbcb3ecbc1f5d) struct [bt\_hci\_cp\_le\_set\_pawr\_subevent\_data\_element](structbt__hci__cp__le__set__pawr__subevent__data__element.md) [subevents](structbt__hci__cp__le__set__pawr__subevent__data.md#aa932c1f19de96f89a79bbcb3ecbc1f5d)[0];

1740} \_\_packed;

1741

1742

[ 1743](hci__types_8h.md#a2be1e66c896dca2022c04164fd94da49)#define BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_RESPONSE\_DATA BT\_OP(BT\_OGF\_LE, 0x0083) /\* 0x2083 \*/

[ 1744](structbt__hci__cp__le__set__pawr__response__data.md)struct [bt\_hci\_cp\_le\_set\_pawr\_response\_data](structbt__hci__cp__le__set__pawr__response__data.md) {

[ 1745](structbt__hci__cp__le__set__pawr__response__data.md#a034afaaacf4b2168b9cd54cfde583b5c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sync\_handle](structbt__hci__cp__le__set__pawr__response__data.md#a034afaaacf4b2168b9cd54cfde583b5c);

[ 1746](structbt__hci__cp__le__set__pawr__response__data.md#aaf5c337af93f13e243451b46a94ffb77) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [request\_event](structbt__hci__cp__le__set__pawr__response__data.md#aaf5c337af93f13e243451b46a94ffb77);

[ 1747](structbt__hci__cp__le__set__pawr__response__data.md#a675a223891b28f06e78df6223439dc28) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [request\_subevent](structbt__hci__cp__le__set__pawr__response__data.md#a675a223891b28f06e78df6223439dc28);

[ 1748](structbt__hci__cp__le__set__pawr__response__data.md#aaf2e0eb3b491b5ccd15ba5259fd900c7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_subevent](structbt__hci__cp__le__set__pawr__response__data.md#aaf2e0eb3b491b5ccd15ba5259fd900c7);

[ 1749](structbt__hci__cp__le__set__pawr__response__data.md#a4356344510833196533bb9582f6fe18a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot](structbt__hci__cp__le__set__pawr__response__data.md#a4356344510833196533bb9582f6fe18a);

[ 1750](structbt__hci__cp__le__set__pawr__response__data.md#a8c546fa3c6d969d44c54926330e5cf85) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_data\_length](structbt__hci__cp__le__set__pawr__response__data.md#a8c546fa3c6d969d44c54926330e5cf85);

[ 1751](structbt__hci__cp__le__set__pawr__response__data.md#a39cbc74ab95881b6dde8fa377d2951e5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_data](structbt__hci__cp__le__set__pawr__response__data.md#a39cbc74ab95881b6dde8fa377d2951e5)[0];

1752} \_\_packed;

1753

[ 1754](hci__types_8h.md#aea7f44f563c109be1676454412757fab)#define BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_SYNC\_SUBEVENT BT\_OP(BT\_OGF\_LE, 0x0084) /\* 0x2084 \*/

[ 1755](structbt__hci__cp__le__set__pawr__sync__subevent.md)struct [bt\_hci\_cp\_le\_set\_pawr\_sync\_subevent](structbt__hci__cp__le__set__pawr__sync__subevent.md) {

[ 1756](structbt__hci__cp__le__set__pawr__sync__subevent.md#a89f3092c2dd561e5469bb5bf57a06172) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sync\_handle](structbt__hci__cp__le__set__pawr__sync__subevent.md#a89f3092c2dd561e5469bb5bf57a06172);

[ 1757](structbt__hci__cp__le__set__pawr__sync__subevent.md#aa73b23816e6c2c6546de15f6f6caff27) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [periodic\_adv\_properties](structbt__hci__cp__le__set__pawr__sync__subevent.md#aa73b23816e6c2c6546de15f6f6caff27);

[ 1758](structbt__hci__cp__le__set__pawr__sync__subevent.md#a2648ff50e0bad585e77e6f340836555a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_subevents](structbt__hci__cp__le__set__pawr__sync__subevent.md#a2648ff50e0bad585e77e6f340836555a);

[ 1759](structbt__hci__cp__le__set__pawr__sync__subevent.md#a9a362ae841e5305b3985c4b2d88c6753) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevents](structbt__hci__cp__le__set__pawr__sync__subevent.md#a9a362ae841e5305b3985c4b2d88c6753)[0];

1760} \_\_packed;

1761

1762

[ 1763](hci__types_8h.md#a1125bfc15404124bf4bd533520be0f77)#define BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_PARAM\_V2 BT\_OP(BT\_OGF\_LE, 0x0086) /\* 0x2086 \*/

[ 1764](structbt__hci__cp__le__set__per__adv__param__v2.md)struct [bt\_hci\_cp\_le\_set\_per\_adv\_param\_v2](structbt__hci__cp__le__set__per__adv__param__v2.md) {

[ 1765](structbt__hci__cp__le__set__per__adv__param__v2.md#aee1088b46914c8e26d9e97ce573291c6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle](structbt__hci__cp__le__set__per__adv__param__v2.md#aee1088b46914c8e26d9e97ce573291c6);

[ 1766](structbt__hci__cp__le__set__per__adv__param__v2.md#ae36e28210a515f73648e6f8b3984fb55) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [min\_interval](structbt__hci__cp__le__set__per__adv__param__v2.md#ae36e28210a515f73648e6f8b3984fb55);

[ 1767](structbt__hci__cp__le__set__per__adv__param__v2.md#acc9718286ab0847a3444d3fc2d3c93bc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_interval](structbt__hci__cp__le__set__per__adv__param__v2.md#acc9718286ab0847a3444d3fc2d3c93bc);

[ 1768](structbt__hci__cp__le__set__per__adv__param__v2.md#ad2d658bb0be35aee6b5c133fece89068) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [props](structbt__hci__cp__le__set__per__adv__param__v2.md#ad2d658bb0be35aee6b5c133fece89068);

[ 1769](structbt__hci__cp__le__set__per__adv__param__v2.md#a7bea764aa5d21e03946804566b1f9869) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_subevents](structbt__hci__cp__le__set__per__adv__param__v2.md#a7bea764aa5d21e03946804566b1f9869);

[ 1770](structbt__hci__cp__le__set__per__adv__param__v2.md#a79dfc3b13068d9c51f0a756f025aaeba) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent\_interval](structbt__hci__cp__le__set__per__adv__param__v2.md#a79dfc3b13068d9c51f0a756f025aaeba);

[ 1771](structbt__hci__cp__le__set__per__adv__param__v2.md#acdeb503c0a13291158ad389c9f6ac206) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot\_delay](structbt__hci__cp__le__set__per__adv__param__v2.md#acdeb503c0a13291158ad389c9f6ac206);

[ 1772](structbt__hci__cp__le__set__per__adv__param__v2.md#a35fcc697e60d3c398f03be7503f611bd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot\_spacing](structbt__hci__cp__le__set__per__adv__param__v2.md#a35fcc697e60d3c398f03be7503f611bd);

[ 1773](structbt__hci__cp__le__set__per__adv__param__v2.md#a2483eb4457f9dc22ff8473175662e260) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_response\_slots](structbt__hci__cp__le__set__per__adv__param__v2.md#a2483eb4457f9dc22ff8473175662e260);

1774} \_\_packed;

1775

1776

[ 1777](hci__types_8h.md#a490bb7d8cf236e49c60771a95d258247)#define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_FP\_USE\_LIST BIT(0)

[ 1778](hci__types_8h.md#a44f11af392e3188e699d8f987cb2f6d6)#define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_FP\_REPORTS\_DISABLED BIT(1)

[ 1779](hci__types_8h.md#a29c5cf397f94af42bdea484fa95a2a78)#define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_FP\_FILTER\_DUPLICATE BIT(2)

1780

[ 1781](hci__types_8h.md#abb3c8fcfc0b48cf6dbebff206a2a9a48)#define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_NO\_FILTERING 0

[ 1782](hci__types_8h.md#a64c7e74877c8ca638217a09d503e742b)#define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_NO\_AOA BIT(0)

[ 1783](hci__types_8h.md#ad349244f13388a7437651e5c3909bcb9)#define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_NO\_AOD\_1US BIT(1)

[ 1784](hci__types_8h.md#aae32740df5a3096a9b17b9c06e6cc3e9)#define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_NO\_AOD\_2US BIT(2)

[ 1785](hci__types_8h.md#a5532c8ee93198eb831c12b182e13a534)#define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_NO\_CTE BIT(3)

[ 1786](hci__types_8h.md#aa3b526ab2ed1aeaab0e26a5390b3dcea)#define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_ONLY\_CTE BIT(4)

1787/\* Constants to check correctness of CTE type \*/

[ 1788](hci__types_8h.md#a4c884821e7136f6f68bc4d92b394381a)#define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_ALLOWED\_BITS 5

[ 1789](hci__types_8h.md#a6ad9e08bcef788c32481756f76df6a43)#define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_INVALID\_VALUE \

1790 (~BIT\_MASK(BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_ALLOWED\_BITS))

1791

[ 1792](hci__types_8h.md#a589c2da26ce325d5cb45726c772cf7ab)#define BT\_HCI\_OP\_LE\_PER\_ADV\_CREATE\_SYNC BT\_OP(BT\_OGF\_LE, 0x0044) /\* 0x2044 \*/

[ 1793](structbt__hci__cp__le__per__adv__create__sync.md)struct [bt\_hci\_cp\_le\_per\_adv\_create\_sync](structbt__hci__cp__le__per__adv__create__sync.md) {

[ 1794](structbt__hci__cp__le__per__adv__create__sync.md#aff300f352ec5f0fece90f88db811ef75) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [options](structbt__hci__cp__le__per__adv__create__sync.md#aff300f352ec5f0fece90f88db811ef75);

[ 1795](structbt__hci__cp__le__per__adv__create__sync.md#ab5c4debe1babb98c60c1f1bfdf55359a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__hci__cp__le__per__adv__create__sync.md#ab5c4debe1babb98c60c1f1bfdf55359a);

[ 1796](structbt__hci__cp__le__per__adv__create__sync.md#a3a0a0bc1bd5014f2ede0c4ef6cc30d24) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__hci__cp__le__per__adv__create__sync.md#a3a0a0bc1bd5014f2ede0c4ef6cc30d24);

[ 1797](structbt__hci__cp__le__per__adv__create__sync.md#a554552684fa2a8d0022f9e31ade9c222) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [skip](structbt__hci__cp__le__per__adv__create__sync.md#a554552684fa2a8d0022f9e31ade9c222);

[ 1798](structbt__hci__cp__le__per__adv__create__sync.md#a46ea01403f68d42a315ff629374b2a95) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sync\_timeout](structbt__hci__cp__le__per__adv__create__sync.md#a46ea01403f68d42a315ff629374b2a95);

[ 1799](structbt__hci__cp__le__per__adv__create__sync.md#a905b2a9166dd668df5929f0866769576) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__hci__cp__le__per__adv__create__sync.md#a905b2a9166dd668df5929f0866769576);

1800} \_\_packed;

1801

[ 1802](hci__types_8h.md#a3803042099104029f5b49536cb769e6c)#define BT\_HCI\_OP\_LE\_PER\_ADV\_CREATE\_SYNC\_CANCEL BT\_OP(BT\_OGF\_LE, 0x0045) /\* 0x2045 \*/

1803

[ 1804](hci__types_8h.md#a57b7b3cab371b4dd230343dfbc5a5e98)#define BT\_HCI\_OP\_LE\_PER\_ADV\_TERMINATE\_SYNC BT\_OP(BT\_OGF\_LE, 0x0046) /\* 0x2046 \*/

[ 1805](structbt__hci__cp__le__per__adv__terminate__sync.md)struct [bt\_hci\_cp\_le\_per\_adv\_terminate\_sync](structbt__hci__cp__le__per__adv__terminate__sync.md) {

[ 1806](structbt__hci__cp__le__per__adv__terminate__sync.md#a607fce7fd5c88e12f82e3d9731bd7f1a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__per__adv__terminate__sync.md#a607fce7fd5c88e12f82e3d9731bd7f1a);

1807} \_\_packed;

1808

[ 1809](hci__types_8h.md#a393378ba85552bb5f41475a863ca649f)#define BT\_HCI\_OP\_LE\_ADD\_DEV\_TO\_PER\_ADV\_LIST BT\_OP(BT\_OGF\_LE, 0x0047) /\* 0x2047 \*/

[ 1810](structbt__hci__cp__le__add__dev__to__per__adv__list.md)struct [bt\_hci\_cp\_le\_add\_dev\_to\_per\_adv\_list](structbt__hci__cp__le__add__dev__to__per__adv__list.md) {

[ 1811](structbt__hci__cp__le__add__dev__to__per__adv__list.md#ad93d72bfa7e4123ee9728f6bf73b69df) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__hci__cp__le__add__dev__to__per__adv__list.md#ad93d72bfa7e4123ee9728f6bf73b69df);

[ 1812](structbt__hci__cp__le__add__dev__to__per__adv__list.md#a97d9c5dd0cc4b3ab7f6ebfec206b7407) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__hci__cp__le__add__dev__to__per__adv__list.md#a97d9c5dd0cc4b3ab7f6ebfec206b7407);

1813} \_\_packed;

1814

[ 1815](hci__types_8h.md#a8545e1ede192257a4383eea6b2e932b7)#define BT\_HCI\_OP\_LE\_REM\_DEV\_FROM\_PER\_ADV\_LIST BT\_OP(BT\_OGF\_LE, 0x0048) /\* 0x2048 \*/

[ 1816](structbt__hci__cp__le__rem__dev__from__per__adv__list.md)struct [bt\_hci\_cp\_le\_rem\_dev\_from\_per\_adv\_list](structbt__hci__cp__le__rem__dev__from__per__adv__list.md) {

[ 1817](structbt__hci__cp__le__rem__dev__from__per__adv__list.md#adc420288f6a79c1a92f57241d3da3d81) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__hci__cp__le__rem__dev__from__per__adv__list.md#adc420288f6a79c1a92f57241d3da3d81);

[ 1818](structbt__hci__cp__le__rem__dev__from__per__adv__list.md#a6629f3ececf586792a14f3c028cc8e8c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__hci__cp__le__rem__dev__from__per__adv__list.md#a6629f3ececf586792a14f3c028cc8e8c);

1819} \_\_packed;

1820

[ 1821](hci__types_8h.md#affcd4a54d0b26d7b07e39157f17167b4)#define BT\_HCI\_OP\_LE\_CLEAR\_PER\_ADV\_LIST BT\_OP(BT\_OGF\_LE, 0x0049) /\* 0x2049 \*/

1822

[ 1823](hci__types_8h.md#a3e2fd45c015809e131ac6b3f6a9c72fc)#define BT\_HCI\_OP\_LE\_READ\_PER\_ADV\_LIST\_SIZE BT\_OP(BT\_OGF\_LE, 0x004a) /\* 0x204a \*/

[ 1824](structbt__hci__rp__le__read__per__adv__list__size.md)struct [bt\_hci\_rp\_le\_read\_per\_adv\_list\_size](structbt__hci__rp__le__read__per__adv__list__size.md) {

[ 1825](structbt__hci__rp__le__read__per__adv__list__size.md#a70aa5b466bdbbd309fc59570625c35e5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__per__adv__list__size.md#a70aa5b466bdbbd309fc59570625c35e5);

[ 1826](structbt__hci__rp__le__read__per__adv__list__size.md#ab6c4ed1037327669aef623f3a1e9d601) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [list\_size](structbt__hci__rp__le__read__per__adv__list__size.md#ab6c4ed1037327669aef623f3a1e9d601);

1827} \_\_packed;

1828

[ 1829](hci__types_8h.md#a77d132306109474465575369db342dbd)#define BT\_HCI\_OP\_LE\_READ\_TX\_POWER BT\_OP(BT\_OGF\_LE, 0x004b) /\* 0x204b \*/

[ 1830](structbt__hci__rp__le__read__tx__power.md)struct [bt\_hci\_rp\_le\_read\_tx\_power](structbt__hci__rp__le__read__tx__power.md) {

[ 1831](structbt__hci__rp__le__read__tx__power.md#a805629b92c65e006082d819f578ed555) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__tx__power.md#a805629b92c65e006082d819f578ed555);

[ 1832](structbt__hci__rp__le__read__tx__power.md#a6d4ab95efda5cfc97ae11d83787da8d7) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [min\_tx\_power](structbt__hci__rp__le__read__tx__power.md#a6d4ab95efda5cfc97ae11d83787da8d7);

[ 1833](structbt__hci__rp__le__read__tx__power.md#a1d794f1f7ea77eceac7dae2546eab047) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [max\_tx\_power](structbt__hci__rp__le__read__tx__power.md#a1d794f1f7ea77eceac7dae2546eab047);

1834} \_\_packed;

1835

[ 1836](hci__types_8h.md#a6c454d3276f7eaae542b13becad6482c)#define BT\_HCI\_OP\_LE\_READ\_RF\_PATH\_COMP BT\_OP(BT\_OGF\_LE, 0x004c) /\* 0x204c \*/

[ 1837](structbt__hci__rp__le__read__rf__path__comp.md)struct [bt\_hci\_rp\_le\_read\_rf\_path\_comp](structbt__hci__rp__le__read__rf__path__comp.md) {

[ 1838](structbt__hci__rp__le__read__rf__path__comp.md#a84a04bcc64ea6d50fe41e9b416a5ada1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__rf__path__comp.md#a84a04bcc64ea6d50fe41e9b416a5ada1);

[ 1839](structbt__hci__rp__le__read__rf__path__comp.md#a827fa954277823efdc5838c317a1460a) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [tx\_path\_comp](structbt__hci__rp__le__read__rf__path__comp.md#a827fa954277823efdc5838c317a1460a);

[ 1840](structbt__hci__rp__le__read__rf__path__comp.md#a0f46a99c74006dc0a4dfd1a49c72e077) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [rx\_path\_comp](structbt__hci__rp__le__read__rf__path__comp.md#a0f46a99c74006dc0a4dfd1a49c72e077);

1841} \_\_packed;

1842

[ 1843](hci__types_8h.md#a766b66d1fc7df1d8924d060217de9b9b)#define BT\_HCI\_OP\_LE\_WRITE\_RF\_PATH\_COMP BT\_OP(BT\_OGF\_LE, 0x004d) /\* 0x204d \*/

[ 1844](structbt__hci__cp__le__write__rf__path__comp.md)struct [bt\_hci\_cp\_le\_write\_rf\_path\_comp](structbt__hci__cp__le__write__rf__path__comp.md) {

[ 1845](structbt__hci__cp__le__write__rf__path__comp.md#a5f99b131f3fba91706bdc8277c1abba1) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [tx\_path\_comp](structbt__hci__cp__le__write__rf__path__comp.md#a5f99b131f3fba91706bdc8277c1abba1);

[ 1846](structbt__hci__cp__le__write__rf__path__comp.md#a11aad5607e444cf55dd5878f1f6f9436) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [rx\_path\_comp](structbt__hci__cp__le__write__rf__path__comp.md#a11aad5607e444cf55dd5878f1f6f9436);

1847} \_\_packed;

1848

[ 1849](hci__types_8h.md#a423b143e474548458b8bcce59029f722)#define BT\_HCI\_LE\_PRIVACY\_MODE\_NETWORK 0x00

[ 1850](hci__types_8h.md#ae61d38e84e0d58be45ffaf521abad2f6)#define BT\_HCI\_LE\_PRIVACY\_MODE\_DEVICE 0x01

1851

[ 1852](hci__types_8h.md#a7e1fad2d353904bb345f3a1579c98576)#define BT\_HCI\_OP\_LE\_SET\_PRIVACY\_MODE BT\_OP(BT\_OGF\_LE, 0x004e) /\* 0x204e \*/

[ 1853](structbt__hci__cp__le__set__privacy__mode.md)struct [bt\_hci\_cp\_le\_set\_privacy\_mode](structbt__hci__cp__le__set__privacy__mode.md) {

[ 1854](structbt__hci__cp__le__set__privacy__mode.md#a404cc9f04cd11924445f12eb4471ef2e) [bt\_addr\_le\_t](structbt__addr__le__t.md) [id\_addr](structbt__hci__cp__le__set__privacy__mode.md#a404cc9f04cd11924445f12eb4471ef2e);

[ 1855](structbt__hci__cp__le__set__privacy__mode.md#a8ca00418b0638bba6ef586d6cbf253a5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mode](structbt__hci__cp__le__set__privacy__mode.md#a8ca00418b0638bba6ef586d6cbf253a5);

1856} \_\_packed;

1857

[ 1858](hci__types_8h.md#a6764be57300c8dac30a058ebf8387159)#define BT\_HCI\_LE\_TEST\_CTE\_DISABLED 0x00

[ 1859](hci__types_8h.md#a1f45696f06d7bc3f4cc8393bd6967286)#define BT\_HCI\_LE\_TEST\_CTE\_TYPE\_ANY 0x00

[ 1860](hci__types_8h.md#ac4ac180578ed3f662d91c43b5c6b6b53)#define BT\_HCI\_LE\_TEST\_SLOT\_DURATION\_ANY 0x00

[ 1861](hci__types_8h.md#aef669f8887a165b4948eb651c91968c1)#define BT\_HCI\_LE\_TEST\_SWITCH\_PATTERN\_LEN\_ANY 0x00

1862

[ 1863](hci__types_8h.md#abe1567f7cf83148b3f2214b6e0787da0)#define BT\_HCI\_OP\_LE\_RX\_TEST\_V3 BT\_OP(BT\_OGF\_LE, 0x004f) /\* 0x204f \*/

[ 1864](structbt__hci__cp__le__rx__test__v3.md)struct [bt\_hci\_cp\_le\_rx\_test\_v3](structbt__hci__cp__le__rx__test__v3.md) {

[ 1865](structbt__hci__cp__le__rx__test__v3.md#abd33b70c948d4ee42d96d0d2e7f7cb1c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_ch](structbt__hci__cp__le__rx__test__v3.md#abd33b70c948d4ee42d96d0d2e7f7cb1c);

[ 1866](structbt__hci__cp__le__rx__test__v3.md#ad1c211c59cf34d76429d4d4548966630) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__cp__le__rx__test__v3.md#ad1c211c59cf34d76429d4d4548966630);

[ 1867](structbt__hci__cp__le__rx__test__v3.md#a7ffde9dc565194c0108177cf11b02b5b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mod\_index](structbt__hci__cp__le__rx__test__v3.md#a7ffde9dc565194c0108177cf11b02b5b);

[ 1868](structbt__hci__cp__le__rx__test__v3.md#ad1a1082d27b8a10e25eebd347404637c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [expected\_cte\_len](structbt__hci__cp__le__rx__test__v3.md#ad1a1082d27b8a10e25eebd347404637c);

[ 1869](structbt__hci__cp__le__rx__test__v3.md#a55b5c4739e456167f17bf3899d096e61) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [expected\_cte\_type](structbt__hci__cp__le__rx__test__v3.md#a55b5c4739e456167f17bf3899d096e61);

[ 1870](structbt__hci__cp__le__rx__test__v3.md#a5cd5a44b0832b9f6e2198b9ad714b99b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [slot\_durations](structbt__hci__cp__le__rx__test__v3.md#a5cd5a44b0832b9f6e2198b9ad714b99b);

[ 1871](structbt__hci__cp__le__rx__test__v3.md#ab0832e72ef90b1269928378638fcb194) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [switch\_pattern\_len](structbt__hci__cp__le__rx__test__v3.md#ab0832e72ef90b1269928378638fcb194);

[ 1872](structbt__hci__cp__le__rx__test__v3.md#aa6cd0835068f378949da182af13e2438) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ant\_ids](structbt__hci__cp__le__rx__test__v3.md#aa6cd0835068f378949da182af13e2438)[0];

1873} \_\_packed;

1874

[ 1875](hci__types_8h.md#ad570a3edcefcf927e5253805e1d3d4e4)#define BT\_HCI\_OP\_LE\_TX\_TEST\_V3 BT\_OP(BT\_OGF\_LE, 0x0050) /\* 0x2050 \*/

1876

[ 1877](structbt__hci__cp__le__tx__test__v3.md)struct [bt\_hci\_cp\_le\_tx\_test\_v3](structbt__hci__cp__le__tx__test__v3.md) {

[ 1878](structbt__hci__cp__le__tx__test__v3.md#a6486882bc375f229a88bbfa53be49670) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_ch](structbt__hci__cp__le__tx__test__v3.md#a6486882bc375f229a88bbfa53be49670);

[ 1879](structbt__hci__cp__le__tx__test__v3.md#a1c0828e51bb6c24e9dd1f12b5badcfea) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [test\_data\_len](structbt__hci__cp__le__tx__test__v3.md#a1c0828e51bb6c24e9dd1f12b5badcfea);

[ 1880](structbt__hci__cp__le__tx__test__v3.md#ad8f2d2ca3ad3be28c0aec9e8a0e1bc61) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pkt\_payload](structbt__hci__cp__le__tx__test__v3.md#ad8f2d2ca3ad3be28c0aec9e8a0e1bc61);

[ 1881](structbt__hci__cp__le__tx__test__v3.md#a712a30d9d6afc7d302041e1de6721de4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__cp__le__tx__test__v3.md#a712a30d9d6afc7d302041e1de6721de4);

[ 1882](structbt__hci__cp__le__tx__test__v3.md#a52d2d6dcc188d5f02904e0e56f461841) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_len](structbt__hci__cp__le__tx__test__v3.md#a52d2d6dcc188d5f02904e0e56f461841);

[ 1883](structbt__hci__cp__le__tx__test__v3.md#adf6b1653902fb13cc1ccc32cd91c990f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__hci__cp__le__tx__test__v3.md#adf6b1653902fb13cc1ccc32cd91c990f);

[ 1884](structbt__hci__cp__le__tx__test__v3.md#a459b850f35c61bf7f53d3730245cb4bb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [switch\_pattern\_len](structbt__hci__cp__le__tx__test__v3.md#a459b850f35c61bf7f53d3730245cb4bb);

[ 1885](structbt__hci__cp__le__tx__test__v3.md#afdb6dd44108e9a4a21ac31a74c1e083f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ant\_ids](structbt__hci__cp__le__tx__test__v3.md#afdb6dd44108e9a4a21ac31a74c1e083f)[0];

1886} \_\_packed;

1887

1888/\* Min and max Constant Tone Extension length in 8us units \*/

[ 1889](hci__types_8h.md#a80376d34b4d701d5f6092aa101ce0e6c)#define BT\_HCI\_LE\_CTE\_LEN\_MIN 0x2

[ 1890](hci__types_8h.md#acdfe03ade99fa88779b68e435aea23e3)#define BT\_HCI\_LE\_CTE\_LEN\_MAX 0x14

1891

[ 1892](hci__types_8h.md#a9b3306f29525c50cd8bd501f7391e518)#define BT\_HCI\_LE\_AOA\_CTE 0x0

[ 1893](hci__types_8h.md#a8569e960c44660eb41cdccbe5aeb6ead)#define BT\_HCI\_LE\_AOD\_CTE\_1US 0x1

[ 1894](hci__types_8h.md#a970732caa95f5742fc18c91efbc7095b)#define BT\_HCI\_LE\_AOD\_CTE\_2US 0x2

[ 1895](hci__types_8h.md#aeee9fd73771de54542f7ff24f95eceba)#define BT\_HCI\_LE\_NO\_CTE 0xFF

1896

[ 1897](hci__types_8h.md#aec2a77fadbb6bf24267d659a84b7c9a9)#define BT\_HCI\_LE\_CTE\_COUNT\_MIN 0x1

[ 1898](hci__types_8h.md#a442df4f693ae5bb75d1d8f54fe204bda)#define BT\_HCI\_LE\_CTE\_COUNT\_MAX 0x10

1899

[ 1900](hci__types_8h.md#a900509c6e7485b44de09a43555225ce8)#define BT\_HCI\_OP\_LE\_SET\_CL\_CTE\_TX\_PARAMS BT\_OP(BT\_OGF\_LE, 0x0051) /\* 0x2051 \*/

[ 1901](structbt__hci__cp__le__set__cl__cte__tx__params.md)struct [bt\_hci\_cp\_le\_set\_cl\_cte\_tx\_params](structbt__hci__cp__le__set__cl__cte__tx__params.md) {

[ 1902](structbt__hci__cp__le__set__cl__cte__tx__params.md#a8f20e6e3bb408551d6cc494ad19391c4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle](structbt__hci__cp__le__set__cl__cte__tx__params.md#a8f20e6e3bb408551d6cc494ad19391c4);

[ 1903](structbt__hci__cp__le__set__cl__cte__tx__params.md#ab5c4742cf37cf7e802423beb4a9b4fa2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_len](structbt__hci__cp__le__set__cl__cte__tx__params.md#ab5c4742cf37cf7e802423beb4a9b4fa2);

[ 1904](structbt__hci__cp__le__set__cl__cte__tx__params.md#a869192cea35f4cd57984614e4c8bb5a5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__hci__cp__le__set__cl__cte__tx__params.md#a869192cea35f4cd57984614e4c8bb5a5);

[ 1905](structbt__hci__cp__le__set__cl__cte__tx__params.md#af5e82bf572b385904a0f24219bdc72ca) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_count](structbt__hci__cp__le__set__cl__cte__tx__params.md#af5e82bf572b385904a0f24219bdc72ca);

[ 1906](structbt__hci__cp__le__set__cl__cte__tx__params.md#a8208571653e444221648d2a884eabfae) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [switch\_pattern\_len](structbt__hci__cp__le__set__cl__cte__tx__params.md#a8208571653e444221648d2a884eabfae);

[ 1907](structbt__hci__cp__le__set__cl__cte__tx__params.md#a27a228653ea560a77369a6b1829a8a9d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ant\_ids](structbt__hci__cp__le__set__cl__cte__tx__params.md#a27a228653ea560a77369a6b1829a8a9d)[0];

1908} \_\_packed;

1909

[ 1910](hci__types_8h.md#a5527fd8badb977f2ef061ba76468ccf3)#define BT\_HCI\_OP\_LE\_SET\_CL\_CTE\_TX\_ENABLE BT\_OP(BT\_OGF\_LE, 0x0052) /\* 0x2052 \*/

[ 1911](structbt__hci__cp__le__set__cl__cte__tx__enable.md)struct [bt\_hci\_cp\_le\_set\_cl\_cte\_tx\_enable](structbt__hci__cp__le__set__cl__cte__tx__enable.md) {

[ 1912](structbt__hci__cp__le__set__cl__cte__tx__enable.md#a55125c808a888eeecfee9410bcb55859) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle](structbt__hci__cp__le__set__cl__cte__tx__enable.md#a55125c808a888eeecfee9410bcb55859);

[ 1913](structbt__hci__cp__le__set__cl__cte__tx__enable.md#a3530dae940caefeafb9de4ac761ee080) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_enable](structbt__hci__cp__le__set__cl__cte__tx__enable.md#a3530dae940caefeafb9de4ac761ee080);

1914} \_\_packed;

1915

[ 1916](hci__types_8h.md#a1410330e31701a140eb8c0c73c943972)#define BT\_HCI\_LE\_ANTENNA\_SWITCHING\_SLOT\_1US 0x1

[ 1917](hci__types_8h.md#afa70fe0b1b9e277bfcb6bf7d6fc03564)#define BT\_HCI\_LE\_ANTENNA\_SWITCHING\_SLOT\_2US 0x2

1918

[ 1919](hci__types_8h.md#a85450acad700f8cef375d34235752650)#define BT\_HCI\_LE\_SAMPLE\_CTE\_ALL 0x0

[ 1920](hci__types_8h.md#afd22fac7ff6d5006015159ffc978798a)#define BT\_HCI\_LE\_SAMPLE\_CTE\_COUNT\_MIN 0x1

[ 1921](hci__types_8h.md#a0c8888c4dfed6ab4c0f07a37ca3b2278)#define BT\_HCI\_LE\_SAMPLE\_CTE\_COUNT\_MAX 0x10

1922

[ 1923](hci__types_8h.md#a728b9a505c9a2f719424bd277f7e8765)#define BT\_HCI\_OP\_LE\_SET\_CL\_CTE\_SAMPLING\_ENABLE BT\_OP(BT\_OGF\_LE, 0x0053) /\* 0x2053 \*/

[ 1924](structbt__hci__cp__le__set__cl__cte__sampling__enable.md)struct [bt\_hci\_cp\_le\_set\_cl\_cte\_sampling\_enable](structbt__hci__cp__le__set__cl__cte__sampling__enable.md) {

[ 1925](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#a91d3458e2049ab434e220403b7ba235d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sync\_handle](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#a91d3458e2049ab434e220403b7ba235d);

[ 1926](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#aca9e1316c716525f00308f64b8c6cec4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sampling\_enable](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#aca9e1316c716525f00308f64b8c6cec4);

[ 1927](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#aaaed0fc39158c653041fd760a00cecec) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [slot\_durations](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#aaaed0fc39158c653041fd760a00cecec);

[ 1928](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#a38e770b3e5f9d7d63a564dfa7c80451f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_sampled\_cte](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#a38e770b3e5f9d7d63a564dfa7c80451f);

[ 1929](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#a4f52142ef1d2365859189b7a2abe050b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [switch\_pattern\_len](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#a4f52142ef1d2365859189b7a2abe050b);

[ 1930](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#a67bb2dbfe1707f76a5e211e007459c22) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ant\_ids](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#a67bb2dbfe1707f76a5e211e007459c22)[0];

1931} \_\_packed;

1932

[ 1933](structbt__hci__rp__le__set__cl__cte__sampling__enable.md)struct [bt\_hci\_rp\_le\_set\_cl\_cte\_sampling\_enable](structbt__hci__rp__le__set__cl__cte__sampling__enable.md) {

[ 1934](structbt__hci__rp__le__set__cl__cte__sampling__enable.md#a5962f97cef6e53452cdccab1c3440519) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__set__cl__cte__sampling__enable.md#a5962f97cef6e53452cdccab1c3440519);

[ 1935](structbt__hci__rp__le__set__cl__cte__sampling__enable.md#a44db7f831e8d730ec3c80c01ef9543aa) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sync\_handle](structbt__hci__rp__le__set__cl__cte__sampling__enable.md#a44db7f831e8d730ec3c80c01ef9543aa);

1936} \_\_packed;

1937

[ 1938](hci__types_8h.md#a8a079c51fc7c37f29afeda663206c59e)#define BT\_HCI\_OP\_LE\_SET\_CONN\_CTE\_RX\_PARAMS BT\_OP(BT\_OGF\_LE, 0x0054) /\* 0x2054 \*/

[ 1939](structbt__hci__cp__le__set__conn__cte__rx__params.md)struct [bt\_hci\_cp\_le\_set\_conn\_cte\_rx\_params](structbt__hci__cp__le__set__conn__cte__rx__params.md) {

[ 1940](structbt__hci__cp__le__set__conn__cte__rx__params.md#a76968866cf5c6ef4bfb983cb6b68a827) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__set__conn__cte__rx__params.md#a76968866cf5c6ef4bfb983cb6b68a827);

[ 1941](structbt__hci__cp__le__set__conn__cte__rx__params.md#a615cae822878cf1344a990e30fa80044) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sampling\_enable](structbt__hci__cp__le__set__conn__cte__rx__params.md#a615cae822878cf1344a990e30fa80044);

[ 1942](structbt__hci__cp__le__set__conn__cte__rx__params.md#a6246d492b94c67af9604b89912dbdb61) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [slot\_durations](structbt__hci__cp__le__set__conn__cte__rx__params.md#a6246d492b94c67af9604b89912dbdb61);

[ 1943](structbt__hci__cp__le__set__conn__cte__rx__params.md#a89194a5b9e6c7f0c176c915e451911df) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [switch\_pattern\_len](structbt__hci__cp__le__set__conn__cte__rx__params.md#a89194a5b9e6c7f0c176c915e451911df);

[ 1944](structbt__hci__cp__le__set__conn__cte__rx__params.md#a519c37f5d797d8ddac5ba9be7c14b9f9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ant\_ids](structbt__hci__cp__le__set__conn__cte__rx__params.md#a519c37f5d797d8ddac5ba9be7c14b9f9)[0];

1945} \_\_packed;

1946

[ 1947](structbt__hci__rp__le__set__conn__cte__rx__params.md)struct [bt\_hci\_rp\_le\_set\_conn\_cte\_rx\_params](structbt__hci__rp__le__set__conn__cte__rx__params.md) {

[ 1948](structbt__hci__rp__le__set__conn__cte__rx__params.md#ad38bb356876c16904e408405607de73c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__set__conn__cte__rx__params.md#ad38bb356876c16904e408405607de73c);

[ 1949](structbt__hci__rp__le__set__conn__cte__rx__params.md#a3c3fb92d422e7ccaf0c98706d46b3e5a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__set__conn__cte__rx__params.md#a3c3fb92d422e7ccaf0c98706d46b3e5a);

1950} \_\_packed;

1951

[ 1952](hci__types_8h.md#ac80b68b1ca4f55a8a44b6bf0dfa7bfb3)#define BT\_HCI\_LE\_AOA\_CTE\_RSP BIT(0)

[ 1953](hci__types_8h.md#a124137512b0f87a67fff694359d629d0)#define BT\_HCI\_LE\_AOD\_CTE\_RSP\_1US BIT(1)

[ 1954](hci__types_8h.md#a5c1dd462d05e4a5615f80402f892ecbc)#define BT\_HCI\_LE\_AOD\_CTE\_RSP\_2US BIT(2)

1955

[ 1956](hci__types_8h.md#ad74e54836996fc3d02fbb245f9c72b5a)#define BT\_HCI\_LE\_SWITCH\_PATTERN\_LEN\_MIN 0x2

[ 1957](hci__types_8h.md#ad6bdc84c282a4e35ded32687cba94e9f)#define BT\_HCI\_LE\_SWITCH\_PATTERN\_LEN\_MAX 0x4B

1958

[ 1959](hci__types_8h.md#af4110be6e09c80cd7362d9b2580243e7)#define BT\_HCI\_OP\_LE\_SET\_CONN\_CTE\_TX\_PARAMS BT\_OP(BT\_OGF\_LE, 0x0055) /\* 0x2055 \*/

[ 1960](structbt__hci__cp__le__set__conn__cte__tx__params.md)struct [bt\_hci\_cp\_le\_set\_conn\_cte\_tx\_params](structbt__hci__cp__le__set__conn__cte__tx__params.md) {

[ 1961](structbt__hci__cp__le__set__conn__cte__tx__params.md#ae0a482982d804ffd7d16ea2b413e538d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__set__conn__cte__tx__params.md#ae0a482982d804ffd7d16ea2b413e538d);

[ 1962](structbt__hci__cp__le__set__conn__cte__tx__params.md#ab47f852b476ac2c35fc0631180e19fb4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_types](structbt__hci__cp__le__set__conn__cte__tx__params.md#ab47f852b476ac2c35fc0631180e19fb4);

[ 1963](structbt__hci__cp__le__set__conn__cte__tx__params.md#a8f0e5ee74662056f00eaa3a8c72f6fc4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [switch\_pattern\_len](structbt__hci__cp__le__set__conn__cte__tx__params.md#a8f0e5ee74662056f00eaa3a8c72f6fc4);

[ 1964](structbt__hci__cp__le__set__conn__cte__tx__params.md#abff85d652b3b2fd55ad78e53887cd7ce) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ant\_ids](structbt__hci__cp__le__set__conn__cte__tx__params.md#abff85d652b3b2fd55ad78e53887cd7ce)[0];

1965} \_\_packed;

1966

[ 1967](structbt__hci__rp__le__set__conn__cte__tx__params.md)struct [bt\_hci\_rp\_le\_set\_conn\_cte\_tx\_params](structbt__hci__rp__le__set__conn__cte__tx__params.md) {

[ 1968](structbt__hci__rp__le__set__conn__cte__tx__params.md#a56f62b6d2c42cd22f73026a2fabc6986) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__set__conn__cte__tx__params.md#a56f62b6d2c42cd22f73026a2fabc6986);

[ 1969](structbt__hci__rp__le__set__conn__cte__tx__params.md#aad553d484daed7ca08de132f4fb849ee) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__set__conn__cte__tx__params.md#aad553d484daed7ca08de132f4fb849ee);

1970} \_\_packed;

1971

1972/\* Interval between consecutive CTE request procedure starts in number of connection events. \*/

[ 1973](hci__types_8h.md#ad9e1fa26a799b8730c17772482da7982)#define BT\_HCI\_REQUEST\_CTE\_ONCE 0x0

[ 1974](hci__types_8h.md#a13875ad8ac3a77759afdb4b6a76ad3e8)#define BT\_HCI\_REQUEST\_CTE\_INTERVAL\_MIN 0x1

[ 1975](hci__types_8h.md#a0a41f911f5f4b50b571c7f091393c7d8)#define BT\_HCI\_REQUEST\_CTE\_INTERVAL\_MAX 0xFFFF

1976

[ 1977](hci__types_8h.md#ae488ce598705cf60b78da985015bb42b)#define BT\_HCI\_OP\_LE\_CONN\_CTE\_REQ\_ENABLE BT\_OP(BT\_OGF\_LE, 0x0056) /\* 0x2056 \*/

[ 1978](structbt__hci__cp__le__conn__cte__req__enable.md)struct [bt\_hci\_cp\_le\_conn\_cte\_req\_enable](structbt__hci__cp__le__conn__cte__req__enable.md) {

[ 1979](structbt__hci__cp__le__conn__cte__req__enable.md#af340b3b97f9fb12c24baa38415620b44) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__conn__cte__req__enable.md#af340b3b97f9fb12c24baa38415620b44);

[ 1980](structbt__hci__cp__le__conn__cte__req__enable.md#aaf38e3d5664d81ae7ac8d3b1bb03c646) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enable](structbt__hci__cp__le__conn__cte__req__enable.md#aaf38e3d5664d81ae7ac8d3b1bb03c646);

[ 1981](structbt__hci__cp__le__conn__cte__req__enable.md#a956a1a8794b75e962d03cdcf81847cfc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cte\_request\_interval](structbt__hci__cp__le__conn__cte__req__enable.md#a956a1a8794b75e962d03cdcf81847cfc);

[ 1982](structbt__hci__cp__le__conn__cte__req__enable.md#a4d4e41bbe95457ce5e8ad68ffeb85200) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [requested\_cte\_length](structbt__hci__cp__le__conn__cte__req__enable.md#a4d4e41bbe95457ce5e8ad68ffeb85200);

[ 1983](structbt__hci__cp__le__conn__cte__req__enable.md#a5a7443a86e770de4bf7292d813e966e7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [requested\_cte\_type](structbt__hci__cp__le__conn__cte__req__enable.md#a5a7443a86e770de4bf7292d813e966e7);

1984} \_\_packed;

1985

[ 1986](structbt__hci__rp__le__conn__cte__req__enable.md)struct [bt\_hci\_rp\_le\_conn\_cte\_req\_enable](structbt__hci__rp__le__conn__cte__req__enable.md) {

[ 1987](structbt__hci__rp__le__conn__cte__req__enable.md#a1e76e7a6da194a433c1fa6ac2bc36b80) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__conn__cte__req__enable.md#a1e76e7a6da194a433c1fa6ac2bc36b80);

[ 1988](structbt__hci__rp__le__conn__cte__req__enable.md#af00adb07a144156a37fb5fc47ca61ccb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__conn__cte__req__enable.md#af00adb07a144156a37fb5fc47ca61ccb);

1989} \_\_packed;

1990

[ 1991](hci__types_8h.md#a150b54d69fb6fe9175336fadb7d81bb8)#define BT\_HCI\_OP\_LE\_CONN\_CTE\_RSP\_ENABLE BT\_OP(BT\_OGF\_LE, 0x0057) /\* 0x2057 \*/

[ 1992](structbt__hci__cp__le__conn__cte__rsp__enable.md)struct [bt\_hci\_cp\_le\_conn\_cte\_rsp\_enable](structbt__hci__cp__le__conn__cte__rsp__enable.md) {

[ 1993](structbt__hci__cp__le__conn__cte__rsp__enable.md#a9d78072143513020620e02a744d4fa9b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__conn__cte__rsp__enable.md#a9d78072143513020620e02a744d4fa9b);

[ 1994](structbt__hci__cp__le__conn__cte__rsp__enable.md#ae5eaaae211732d772ea53f3936ab32d2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enable](structbt__hci__cp__le__conn__cte__rsp__enable.md#ae5eaaae211732d772ea53f3936ab32d2);

1995} \_\_packed;

1996

[ 1997](structbt__hci__rp__le__conn__cte__rsp__enable.md)struct [bt\_hci\_rp\_le\_conn\_cte\_rsp\_enable](structbt__hci__rp__le__conn__cte__rsp__enable.md) {

[ 1998](structbt__hci__rp__le__conn__cte__rsp__enable.md#a8a21bc015408cc77c5d229cd77289dcc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__conn__cte__rsp__enable.md#a8a21bc015408cc77c5d229cd77289dcc);

[ 1999](structbt__hci__rp__le__conn__cte__rsp__enable.md#ab16f226d871d7d55c3f900614d59d8a1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__conn__cte__rsp__enable.md#ab16f226d871d7d55c3f900614d59d8a1);

2000} \_\_packed;

2001

[ 2002](hci__types_8h.md#a41aac54cd90cfc58990ce93124ce7077)#define BT\_HCI\_LE\_1US\_AOD\_TX BIT(0)

[ 2003](hci__types_8h.md#a70edcf0bd7e63454996ef5d925e91bbf)#define BT\_HCI\_LE\_1US\_AOD\_RX BIT(1)

[ 2004](hci__types_8h.md#a04a69a823bac190d0ac16f3c21481bde)#define BT\_HCI\_LE\_1US\_AOA\_RX BIT(2)

2005

[ 2006](hci__types_8h.md#a112d3fb3d3ec663278aa4463fedbd89b)#define BT\_HCI\_LE\_NUM\_ANT\_MIN 0x1

[ 2007](hci__types_8h.md#ad9ff685b2854b877e0cdd1ae93272ddf)#define BT\_HCI\_LE\_NUM\_ANT\_MAX 0x4B

2008

[ 2009](hci__types_8h.md#a327330c5b69e8ec56dd18fcc3fdf0622)#define BT\_HCI\_LE\_MAX\_SWITCH\_PATTERN\_LEN\_MIN 0x2

[ 2010](hci__types_8h.md#a647de996dd2e75a8242e6459abd565f6)#define BT\_HCI\_LE\_MAX\_SWITCH\_PATTERN\_LEN\_MAX 0x4B

2011

[ 2012](hci__types_8h.md#adee7271e25e6d66ba434502ab56674c3)#define BT\_HCI\_LE\_MAX\_CTE\_LEN\_MIN 0x2

[ 2013](hci__types_8h.md#af54ba281111d90f3edb77c0abf9c57b1)#define BT\_HCI\_LE\_MAX\_CTE\_LEN\_MAX 0x14

2014

[ 2015](hci__types_8h.md#aff3ea5f19135609d5553cacec0d700a6)#define BT\_HCI\_OP\_LE\_READ\_ANT\_INFO BT\_OP(BT\_OGF\_LE, 0x0058) /\* 0x2058 \*/

[ 2016](structbt__hci__rp__le__read__ant__info.md)struct [bt\_hci\_rp\_le\_read\_ant\_info](structbt__hci__rp__le__read__ant__info.md) {

[ 2017](structbt__hci__rp__le__read__ant__info.md#ae1388d3eee3085af7f2b0b57b2aa7b1e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__ant__info.md#ae1388d3eee3085af7f2b0b57b2aa7b1e);

[ 2018](structbt__hci__rp__le__read__ant__info.md#a2c78d3db239c9e00729d91834eb60f21) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [switch\_sample\_rates](structbt__hci__rp__le__read__ant__info.md#a2c78d3db239c9e00729d91834eb60f21);

[ 2019](structbt__hci__rp__le__read__ant__info.md#a1f79b45751d39ebb9349df93d0ff2e13) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_ant](structbt__hci__rp__le__read__ant__info.md#a1f79b45751d39ebb9349df93d0ff2e13);

[ 2020](structbt__hci__rp__le__read__ant__info.md#ae75fe0b9f5fe8c88a8e8482eef299348) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_switch\_pattern\_len](structbt__hci__rp__le__read__ant__info.md#ae75fe0b9f5fe8c88a8e8482eef299348);

[ 2021](structbt__hci__rp__le__read__ant__info.md#a625cc8fa8553eafbbb31cbc0b3f303c7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_cte\_len](structbt__hci__rp__le__read__ant__info.md#a625cc8fa8553eafbbb31cbc0b3f303c7);

2022};

2023

[ 2024](hci__types_8h.md#a1aaaffb3044bfd824aa6744867da0a97)#define BT\_HCI\_LE\_SET\_PER\_ADV\_RECV\_ENABLE\_ENABLE BIT(0)

[ 2025](hci__types_8h.md#a08fe0a16e8c1b3eb6b23869b37739f2d)#define BT\_HCI\_LE\_SET\_PER\_ADV\_RECV\_ENABLE\_FILTER\_DUPLICATE BIT(1)

2026

[ 2027](hci__types_8h.md#a047efb565b182e90178513dc3db6390f)#define BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_RECV\_ENABLE BT\_OP(BT\_OGF\_LE, 0x0059) /\* 0x2059 \*/

[ 2028](structbt__hci__cp__le__set__per__adv__recv__enable.md)struct [bt\_hci\_cp\_le\_set\_per\_adv\_recv\_enable](structbt__hci__cp__le__set__per__adv__recv__enable.md) {

[ 2029](structbt__hci__cp__le__set__per__adv__recv__enable.md#a1e626eecf1d3f0820c3b2a13fd84b92f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__set__per__adv__recv__enable.md#a1e626eecf1d3f0820c3b2a13fd84b92f);

[ 2030](structbt__hci__cp__le__set__per__adv__recv__enable.md#a2187ec96822726daa5e43e910cc41cc3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enable](structbt__hci__cp__le__set__per__adv__recv__enable.md#a2187ec96822726daa5e43e910cc41cc3);

2031} \_\_packed;

2032

[ 2033](hci__types_8h.md#aa1d0bc8ccc0e1e8835938f8e8d87b7f1)#define BT\_HCI\_OP\_LE\_PER\_ADV\_SYNC\_TRANSFER BT\_OP(BT\_OGF\_LE, 0x005a) /\* 0x205a \*/

[ 2034](structbt__hci__cp__le__per__adv__sync__transfer.md)struct [bt\_hci\_cp\_le\_per\_adv\_sync\_transfer](structbt__hci__cp__le__per__adv__sync__transfer.md) {

[ 2035](structbt__hci__cp__le__per__adv__sync__transfer.md#a991f77d6f2f0c301fe3322050b2d359f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__cp__le__per__adv__sync__transfer.md#a991f77d6f2f0c301fe3322050b2d359f);

[ 2036](structbt__hci__cp__le__per__adv__sync__transfer.md#a1327de0f9b2ebd1eaa97b51850087460) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [service\_data](structbt__hci__cp__le__per__adv__sync__transfer.md#a1327de0f9b2ebd1eaa97b51850087460);

[ 2037](structbt__hci__cp__le__per__adv__sync__transfer.md#a38537b7f01a93f7a3e8cfcb92098a172) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sync\_handle](structbt__hci__cp__le__per__adv__sync__transfer.md#a38537b7f01a93f7a3e8cfcb92098a172);

2038} \_\_packed;

2039

[ 2040](structbt__hci__rp__le__per__adv__sync__transfer.md)struct [bt\_hci\_rp\_le\_per\_adv\_sync\_transfer](structbt__hci__rp__le__per__adv__sync__transfer.md) {

[ 2041](structbt__hci__rp__le__per__adv__sync__transfer.md#adb536c4694d2e7c5b91e9f68986e97e1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__per__adv__sync__transfer.md#adb536c4694d2e7c5b91e9f68986e97e1);

[ 2042](structbt__hci__rp__le__per__adv__sync__transfer.md#ab8b4357fd92e01a5f61d3127b04c0318) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__rp__le__per__adv__sync__transfer.md#ab8b4357fd92e01a5f61d3127b04c0318);

2043} \_\_packed;

2044

[ 2045](hci__types_8h.md#ab7d661097af4cc612ac6631b18bbc7e3)#define BT\_HCI\_OP\_LE\_PER\_ADV\_SET\_INFO\_TRANSFER BT\_OP(BT\_OGF\_LE, 0x005b) /\* 0x205b \*/

[ 2046](structbt__hci__cp__le__per__adv__set__info__transfer.md)struct [bt\_hci\_cp\_le\_per\_adv\_set\_info\_transfer](structbt__hci__cp__le__per__adv__set__info__transfer.md) {

[ 2047](structbt__hci__cp__le__per__adv__set__info__transfer.md#a3b2f0c510ef9b385cb42bf9a194fa574) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__cp__le__per__adv__set__info__transfer.md#a3b2f0c510ef9b385cb42bf9a194fa574);

[ 2048](structbt__hci__cp__le__per__adv__set__info__transfer.md#a5f14c3265bffdf3e30a554a3686e9e0c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [service\_data](structbt__hci__cp__le__per__adv__set__info__transfer.md#a5f14c3265bffdf3e30a554a3686e9e0c);

[ 2049](structbt__hci__cp__le__per__adv__set__info__transfer.md#a75b2c0fa1d50ef9d3761ac25f487750b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_handle](structbt__hci__cp__le__per__adv__set__info__transfer.md#a75b2c0fa1d50ef9d3761ac25f487750b);

2050} \_\_packed;

2051

[ 2052](structbt__hci__rp__le__per__adv__set__info__transfer.md)struct [bt\_hci\_rp\_le\_per\_adv\_set\_info\_transfer](structbt__hci__rp__le__per__adv__set__info__transfer.md) {

[ 2053](structbt__hci__rp__le__per__adv__set__info__transfer.md#ab1592bfadd45315ff47e86b7c50374ad) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__per__adv__set__info__transfer.md#ab1592bfadd45315ff47e86b7c50374ad);

[ 2054](structbt__hci__rp__le__per__adv__set__info__transfer.md#a696e5cab4d7507ea79b0e116c4bb92e2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__rp__le__per__adv__set__info__transfer.md#a696e5cab4d7507ea79b0e116c4bb92e2);

2055} \_\_packed;

2056

[ 2057](hci__types_8h.md#a65ff1c4a937422000f6f1eadea28ccba)#define BT\_HCI\_LE\_PAST\_MODE\_NO\_SYNC 0x00

[ 2058](hci__types_8h.md#ac7233f9c34f5e33d765b68b55ebc9b9e)#define BT\_HCI\_LE\_PAST\_MODE\_NO\_REPORTS 0x01

[ 2059](hci__types_8h.md#aaeac19606d3d5e7d0906b38e2c4b4c69)#define BT\_HCI\_LE\_PAST\_MODE\_SYNC 0x02

[ 2060](hci__types_8h.md#ab0232a2abc2b7c86b19ae89298ef8c4b)#define BT\_HCI\_LE\_PAST\_MODE\_SYNC\_FILTER\_DUPLICATES 0x03

2061

[ 2062](hci__types_8h.md#a3a3937965aeb187b6fb18da3b7731ed7)#define BT\_HCI\_LE\_PAST\_CTE\_TYPE\_NO\_AOA BIT(0)

[ 2063](hci__types_8h.md#a440aca4bf97bc6b583284ae6c8037a53)#define BT\_HCI\_LE\_PAST\_CTE\_TYPE\_NO\_AOD\_1US BIT(1)

[ 2064](hci__types_8h.md#ae2d9be5e54595cb5a426ae8909cdee1c)#define BT\_HCI\_LE\_PAST\_CTE\_TYPE\_NO\_AOD\_2US BIT(2)

[ 2065](hci__types_8h.md#af3d8cf0fb8af60c057ba8c24abaf3897)#define BT\_HCI\_LE\_PAST\_CTE\_TYPE\_NO\_CTE BIT(3)

[ 2066](hci__types_8h.md#a6fca2634e0e5b0dd5d86b18666ed38e4)#define BT\_HCI\_LE\_PAST\_CTE\_TYPE\_ONLY\_CTE BIT(4)

2067

[ 2068](hci__types_8h.md#a177ec628eac4a7d535cfe6c07123cb34)#define BT\_HCI\_OP\_LE\_PAST\_PARAM BT\_OP(BT\_OGF\_LE, 0x005c) /\* 0x205c \*/

[ 2069](structbt__hci__cp__le__past__param.md)struct [bt\_hci\_cp\_le\_past\_param](structbt__hci__cp__le__past__param.md) {

[ 2070](structbt__hci__cp__le__past__param.md#a9c99cdd5ae5de58960677781c2287c4d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__cp__le__past__param.md#a9c99cdd5ae5de58960677781c2287c4d);

[ 2071](structbt__hci__cp__le__past__param.md#aa36345a550dfabeef48b430d1a1b0030) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mode](structbt__hci__cp__le__past__param.md#aa36345a550dfabeef48b430d1a1b0030);

[ 2072](structbt__hci__cp__le__past__param.md#a622499d51e917f7828629de2291812e5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [skip](structbt__hci__cp__le__past__param.md#a622499d51e917f7828629de2291812e5);

[ 2073](structbt__hci__cp__le__past__param.md#aec9aa4ffe41c6b6f5cfcbc59eb57efca) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structbt__hci__cp__le__past__param.md#aec9aa4ffe41c6b6f5cfcbc59eb57efca);

[ 2074](structbt__hci__cp__le__past__param.md#a47c571ff27a59e0a7cbcb460303ee194) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__hci__cp__le__past__param.md#a47c571ff27a59e0a7cbcb460303ee194);

2075} \_\_packed;

2076

[ 2077](structbt__hci__rp__le__past__param.md)struct [bt\_hci\_rp\_le\_past\_param](structbt__hci__rp__le__past__param.md) {

[ 2078](structbt__hci__rp__le__past__param.md#a9630362b3d885b13869a4c0fe9e97b12) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__past__param.md#a9630362b3d885b13869a4c0fe9e97b12);

[ 2079](structbt__hci__rp__le__past__param.md#ae6b8a5d7e790516de2f91e41fd893111) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__rp__le__past__param.md#ae6b8a5d7e790516de2f91e41fd893111);

2080} \_\_packed;

2081

[ 2082](hci__types_8h.md#a650fe2941ffe238b16fd99ed5e78b25a)#define BT\_HCI\_OP\_LE\_DEFAULT\_PAST\_PARAM BT\_OP(BT\_OGF\_LE, 0x005d) /\* 0x205d \*/

[ 2083](structbt__hci__cp__le__default__past__param.md)struct [bt\_hci\_cp\_le\_default\_past\_param](structbt__hci__cp__le__default__past__param.md) {

[ 2084](structbt__hci__cp__le__default__past__param.md#a2ef92304264ad0bf1560accf306bb6d9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mode](structbt__hci__cp__le__default__past__param.md#a2ef92304264ad0bf1560accf306bb6d9);

[ 2085](structbt__hci__cp__le__default__past__param.md#a214cb0597d0065bc2c056fe9c51a2220) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [skip](structbt__hci__cp__le__default__past__param.md#a214cb0597d0065bc2c056fe9c51a2220);

[ 2086](structbt__hci__cp__le__default__past__param.md#a159f5245f86b27198264bdcf394d719f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structbt__hci__cp__le__default__past__param.md#a159f5245f86b27198264bdcf394d719f);

[ 2087](structbt__hci__cp__le__default__past__param.md#af18f679f5833c1d782b4e474af5d819c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__hci__cp__le__default__past__param.md#af18f679f5833c1d782b4e474af5d819c);

2088} \_\_packed;

2089

[ 2090](structbt__hci__rp__le__default__past__param.md)struct [bt\_hci\_rp\_le\_default\_past\_param](structbt__hci__rp__le__default__past__param.md) {

[ 2091](structbt__hci__rp__le__default__past__param.md#a292e2d655c77e8cda0d01fc07b43b8c4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__default__past__param.md#a292e2d655c77e8cda0d01fc07b43b8c4);

2092} \_\_packed;

2093

[ 2094](hci__types_8h.md#aa7e78541d152c21e101fab5a094c972f)#define BT\_HCI\_OP\_LE\_READ\_BUFFER\_SIZE\_V2 BT\_OP(BT\_OGF\_LE, 0x0060) /\* 0x2060 \*/

[ 2095](structbt__hci__rp__le__read__buffer__size__v2.md)struct [bt\_hci\_rp\_le\_read\_buffer\_size\_v2](structbt__hci__rp__le__read__buffer__size__v2.md) {

[ 2096](structbt__hci__rp__le__read__buffer__size__v2.md#a3b9cc0577d0f5f3c2b934a28915f2177) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__buffer__size__v2.md#a3b9cc0577d0f5f3c2b934a28915f2177);

[ 2097](structbt__hci__rp__le__read__buffer__size__v2.md#ac391149d3d7442e074aad4b98659bd02) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [acl\_max\_len](structbt__hci__rp__le__read__buffer__size__v2.md#ac391149d3d7442e074aad4b98659bd02);

[ 2098](structbt__hci__rp__le__read__buffer__size__v2.md#a1c7938defb076d973b8339c17cc930df) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [acl\_max\_num](structbt__hci__rp__le__read__buffer__size__v2.md#a1c7938defb076d973b8339c17cc930df);

[ 2099](structbt__hci__rp__le__read__buffer__size__v2.md#a9758d477c502575a1c176eb6a63e1a1a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [iso\_max\_len](structbt__hci__rp__le__read__buffer__size__v2.md#a9758d477c502575a1c176eb6a63e1a1a);

[ 2100](structbt__hci__rp__le__read__buffer__size__v2.md#ac3379adf42f9bbee8ae72fb4a7606fd1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [iso\_max\_num](structbt__hci__rp__le__read__buffer__size__v2.md#ac3379adf42f9bbee8ae72fb4a7606fd1);

2101} \_\_packed;

2102

[ 2103](hci__types_8h.md#acb7f49f17a60a4e29270c8719b7aeeed)#define BT\_HCI\_OP\_LE\_READ\_ISO\_TX\_SYNC BT\_OP(BT\_OGF\_LE, 0x0061) /\* 0x2061 \*/

[ 2104](structbt__hci__cp__le__read__iso__tx__sync.md)struct [bt\_hci\_cp\_le\_read\_iso\_tx\_sync](structbt__hci__cp__le__read__iso__tx__sync.md) {

[ 2105](structbt__hci__cp__le__read__iso__tx__sync.md#a8edc469f73540d4300b1716c96e17c9f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__read__iso__tx__sync.md#a8edc469f73540d4300b1716c96e17c9f);

2106} \_\_packed;

2107

[ 2108](structbt__hci__rp__le__read__iso__tx__sync.md)struct [bt\_hci\_rp\_le\_read\_iso\_tx\_sync](structbt__hci__rp__le__read__iso__tx__sync.md) {

[ 2109](structbt__hci__rp__le__read__iso__tx__sync.md#a188ef5dba77c754c46094135cc52641c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__iso__tx__sync.md#a188ef5dba77c754c46094135cc52641c);

[ 2110](structbt__hci__rp__le__read__iso__tx__sync.md#a8c0003043d3896b1ff93dc33dccc76b4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__read__iso__tx__sync.md#a8c0003043d3896b1ff93dc33dccc76b4);

[ 2111](structbt__hci__rp__le__read__iso__tx__sync.md#af2a02f68aa0a757757c490e707954952) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [seq](structbt__hci__rp__le__read__iso__tx__sync.md#af2a02f68aa0a757757c490e707954952);

[ 2112](structbt__hci__rp__le__read__iso__tx__sync.md#a35520a3e50afc03ed969b6c5ca9e15d9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timestamp](structbt__hci__rp__le__read__iso__tx__sync.md#a35520a3e50afc03ed969b6c5ca9e15d9);

[ 2113](structbt__hci__rp__le__read__iso__tx__sync.md#a29770c3172d5e45409392aa8ffc835ef) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [offset](structbt__hci__rp__le__read__iso__tx__sync.md#a29770c3172d5e45409392aa8ffc835ef)[3];

2114} \_\_packed;

2115

[ 2116](hci__types_8h.md#a18b5fef3eb5b947ce328e17c1e7db02d)#define BT\_HCI\_ISO\_CIG\_ID\_MAX 0xFE

[ 2117](hci__types_8h.md#a26c78a4b760b97682269e66dfe6f99df)#define BT\_HCI\_ISO\_CIS\_COUNT\_MAX 0x1F

[ 2118](hci__types_8h.md#a12e9af0e72013649da8afc7aa70a4e9c)#define BT\_HCI\_ISO\_SDU\_INTERVAL\_MIN 0x0000FF

[ 2119](hci__types_8h.md#aa75800427e808756fc7c6d30da57de37)#define BT\_HCI\_ISO\_SDU\_INTERVAL\_MAX 0x0FFFFF

[ 2120](hci__types_8h.md#a49f62e83dd51d17efd77c89337fdd537)#define BT\_HCI\_ISO\_WORST\_CASE\_SCA\_VALID\_MASK 0x07

[ 2121](hci__types_8h.md#aecaa88e04025e575c9bcda093f027400)#define BT\_HCI\_ISO\_PACKING\_VALID\_MASK 0x01

[ 2122](hci__types_8h.md#aaf4b4fc224c8b5cfdca663250eb29350)#define BT\_HCI\_ISO\_FRAMING\_VALID\_MASK 0x01

[ 2123](hci__types_8h.md#a8d044df1bfab8381b7e334597b303588)#define BT\_HCI\_ISO\_MAX\_TRANSPORT\_LATENCY\_MIN 0x0005

[ 2124](hci__types_8h.md#a9794f59f8d28879753b39bd504cf55be)#define BT\_HCI\_ISO\_MAX\_TRANSPORT\_LATENCY\_MAX 0x0FA0

[ 2125](hci__types_8h.md#a11e614cc72adb58bda2a2bdd5f4b36ef)#define BT\_HCI\_ISO\_CIS\_ID\_VALID\_MAX 0xEF

[ 2126](hci__types_8h.md#a9f3e990cadf1be179fcbac3f8ef74efe)#define BT\_HCI\_ISO\_MAX\_SDU\_VALID\_MASK 0x0FFF

[ 2127](hci__types_8h.md#ae055ed9714ca23bebd48bb399af04d83)#define BT\_HCI\_ISO\_PHY\_VALID\_MASK 0x07

[ 2128](hci__types_8h.md#a9d5e85ae1380fa85bae9d7e5e67aa0ae)#define BT\_HCI\_ISO\_INTERVAL\_MIN 0x0004

[ 2129](hci__types_8h.md#aaadbec2cc6adc2bb14d7117396023d06)#define BT\_HCI\_ISO\_INTERVAL\_MAX 0x0C80

2130

[ 2131](hci__types_8h.md#a0a4b2732026a6300d4b354eb6d93905d)#define BT\_HCI\_OP\_LE\_SET\_CIG\_PARAMS BT\_OP(BT\_OGF\_LE, 0x0062) /\* 0x2062 \*/

[ 2132](structbt__hci__cis__params.md)struct [bt\_hci\_cis\_params](structbt__hci__cis__params.md) {

[ 2133](structbt__hci__cis__params.md#a6dcfca11d7f827b1b7a62b507620d4de) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cis\_id](structbt__hci__cis__params.md#a6dcfca11d7f827b1b7a62b507620d4de);

[ 2134](structbt__hci__cis__params.md#a8a85b914ba5585c6b362da3deb8d42d9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [c\_sdu](structbt__hci__cis__params.md#a8a85b914ba5585c6b362da3deb8d42d9);

[ 2135](structbt__hci__cis__params.md#ae2bffbaf0c4dde9144a7887177b3ffdb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [p\_sdu](structbt__hci__cis__params.md#ae2bffbaf0c4dde9144a7887177b3ffdb);

[ 2136](structbt__hci__cis__params.md#a5a5fcd9276d912446fe84d875ae74c2f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_phy](structbt__hci__cis__params.md#a5a5fcd9276d912446fe84d875ae74c2f);

[ 2137](structbt__hci__cis__params.md#a18bc8e4b531d9fd16f18e10a0d931f6c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_phy](structbt__hci__cis__params.md#a18bc8e4b531d9fd16f18e10a0d931f6c);

[ 2138](structbt__hci__cis__params.md#aa7fa628692f959db63788c6580cc5c66) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_rtn](structbt__hci__cis__params.md#aa7fa628692f959db63788c6580cc5c66);

[ 2139](structbt__hci__cis__params.md#ad55e197ccb70c83fcd4c1c6ba485f468) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_rtn](structbt__hci__cis__params.md#ad55e197ccb70c83fcd4c1c6ba485f468);

2140} \_\_packed;

2141

[ 2142](structbt__hci__cp__le__set__cig__params.md)struct [bt\_hci\_cp\_le\_set\_cig\_params](structbt__hci__cp__le__set__cig__params.md) {

[ 2143](structbt__hci__cp__le__set__cig__params.md#a7dbf75c6ed92a053c4ec0d8f7268c92e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cig\_id](structbt__hci__cp__le__set__cig__params.md#a7dbf75c6ed92a053c4ec0d8f7268c92e);

[ 2144](structbt__hci__cp__le__set__cig__params.md#a14f5c0cf7f99ab406714501038048035) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_interval](structbt__hci__cp__le__set__cig__params.md#a14f5c0cf7f99ab406714501038048035)[3];

[ 2145](structbt__hci__cp__le__set__cig__params.md#a50a260a15f3a0ceae716da6c04c5b768) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_interval](structbt__hci__cp__le__set__cig__params.md#a50a260a15f3a0ceae716da6c04c5b768)[3];

[ 2146](structbt__hci__cp__le__set__cig__params.md#a46a657cdfbc7a49e6761d9f18d980c2a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sca](structbt__hci__cp__le__set__cig__params.md#a46a657cdfbc7a49e6761d9f18d980c2a);

[ 2147](structbt__hci__cp__le__set__cig__params.md#a79fc069492741f14f348650abef4c66b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packing](structbt__hci__cp__le__set__cig__params.md#a79fc069492741f14f348650abef4c66b);

[ 2148](structbt__hci__cp__le__set__cig__params.md#a867bf5ddbcadd27dbec2c3059d67d6d6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [framing](structbt__hci__cp__le__set__cig__params.md#a867bf5ddbcadd27dbec2c3059d67d6d6);

[ 2149](structbt__hci__cp__le__set__cig__params.md#afec8ebd17cc6ca5b3d13ef54f406df62) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [c\_latency](structbt__hci__cp__le__set__cig__params.md#afec8ebd17cc6ca5b3d13ef54f406df62);

[ 2150](structbt__hci__cp__le__set__cig__params.md#a810822396b97d54988ec57561b4ee7d5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [p\_latency](structbt__hci__cp__le__set__cig__params.md#a810822396b97d54988ec57561b4ee7d5);

[ 2151](structbt__hci__cp__le__set__cig__params.md#adf468a8a195447a7bbed4dcd53d287f6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_cis](structbt__hci__cp__le__set__cig__params.md#adf468a8a195447a7bbed4dcd53d287f6);

[ 2152](structbt__hci__cp__le__set__cig__params.md#ac922e59065920421f40468754d2ba5a2) struct [bt\_hci\_cis\_params](structbt__hci__cis__params.md) [cis](structbt__hci__cp__le__set__cig__params.md#ac922e59065920421f40468754d2ba5a2)[0];

2153} \_\_packed;

2154

[ 2155](structbt__hci__rp__le__set__cig__params.md)struct [bt\_hci\_rp\_le\_set\_cig\_params](structbt__hci__rp__le__set__cig__params.md) {

[ 2156](structbt__hci__rp__le__set__cig__params.md#a8426a2b9927bee05fb9a46b4b261c743) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__set__cig__params.md#a8426a2b9927bee05fb9a46b4b261c743);

[ 2157](structbt__hci__rp__le__set__cig__params.md#a951dc88e0cde4e1f0274684498741eac) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cig\_id](structbt__hci__rp__le__set__cig__params.md#a951dc88e0cde4e1f0274684498741eac);

[ 2158](structbt__hci__rp__le__set__cig__params.md#a8aff643e0ae41455eb9391cfdb45ebda) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_handles](structbt__hci__rp__le__set__cig__params.md#a8aff643e0ae41455eb9391cfdb45ebda);

[ 2159](structbt__hci__rp__le__set__cig__params.md#a2e95c6217d11169a8a611ea95dce70b6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__set__cig__params.md#a2e95c6217d11169a8a611ea95dce70b6)[0];

2160} \_\_packed;

2161

[ 2162](hci__types_8h.md#a54df2d12a0c07bab9fb3521dc69ff2f4)#define BT\_HCI\_OP\_LE\_SET\_CIG\_PARAMS\_TEST BT\_OP(BT\_OGF\_LE, 0x0063) /\* 0x2063 \*/

[ 2163](structbt__hci__cis__params__test.md)struct [bt\_hci\_cis\_params\_test](structbt__hci__cis__params__test.md) {

[ 2164](structbt__hci__cis__params__test.md#a0a215b4dffac2aae4ae4310c54de073e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cis\_id](structbt__hci__cis__params__test.md#a0a215b4dffac2aae4ae4310c54de073e);

[ 2165](structbt__hci__cis__params__test.md#ad0cc6d393a536cb3cd83d456b950fc52) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [nse](structbt__hci__cis__params__test.md#ad0cc6d393a536cb3cd83d456b950fc52);

[ 2166](structbt__hci__cis__params__test.md#a98a120efb1495dd90858bef45eb95891) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [c\_sdu](structbt__hci__cis__params__test.md#a98a120efb1495dd90858bef45eb95891);

[ 2167](structbt__hci__cis__params__test.md#aefeca493efe0141590570e8a44bb8f8d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [p\_sdu](structbt__hci__cis__params__test.md#aefeca493efe0141590570e8a44bb8f8d);

[ 2168](structbt__hci__cis__params__test.md#adc092a44b58bcc78f3dfe88528ca724c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [c\_pdu](structbt__hci__cis__params__test.md#adc092a44b58bcc78f3dfe88528ca724c);

[ 2169](structbt__hci__cis__params__test.md#abce4bd6045642b4d29668865655f1548) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [p\_pdu](structbt__hci__cis__params__test.md#abce4bd6045642b4d29668865655f1548);

[ 2170](structbt__hci__cis__params__test.md#aa7ba56fb91718d43ca30ff643757e08e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_phy](structbt__hci__cis__params__test.md#aa7ba56fb91718d43ca30ff643757e08e);

[ 2171](structbt__hci__cis__params__test.md#ab636126046023a329451673c57b4ce96) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_phy](structbt__hci__cis__params__test.md#ab636126046023a329451673c57b4ce96);

[ 2172](structbt__hci__cis__params__test.md#adf5dda2be46f3c2c1a1fe398672416ff) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_bn](structbt__hci__cis__params__test.md#adf5dda2be46f3c2c1a1fe398672416ff);

[ 2173](structbt__hci__cis__params__test.md#ac66b7183d8148250246f17a157dc3d29) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_bn](structbt__hci__cis__params__test.md#ac66b7183d8148250246f17a157dc3d29);

2174} \_\_packed;

2175

[ 2176](structbt__hci__cp__le__set__cig__params__test.md)struct [bt\_hci\_cp\_le\_set\_cig\_params\_test](structbt__hci__cp__le__set__cig__params__test.md) {

[ 2177](structbt__hci__cp__le__set__cig__params__test.md#a161ae960cbd4f7833815285d04f87e46) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cig\_id](structbt__hci__cp__le__set__cig__params__test.md#a161ae960cbd4f7833815285d04f87e46);

[ 2178](structbt__hci__cp__le__set__cig__params__test.md#aa392cbac058beefd0e410fcc9821a0c3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_interval](structbt__hci__cp__le__set__cig__params__test.md#aa392cbac058beefd0e410fcc9821a0c3)[3];

[ 2179](structbt__hci__cp__le__set__cig__params__test.md#a0cf0f3f7c10b29d74ab64aa30a4969de) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_interval](structbt__hci__cp__le__set__cig__params__test.md#a0cf0f3f7c10b29d74ab64aa30a4969de)[3];

[ 2180](structbt__hci__cp__le__set__cig__params__test.md#a1eae50a97188304852589fd95e994150) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_ft](structbt__hci__cp__le__set__cig__params__test.md#a1eae50a97188304852589fd95e994150);

[ 2181](structbt__hci__cp__le__set__cig__params__test.md#af2ed1bf1a6beaff884c3ce3faf26bfb2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_ft](structbt__hci__cp__le__set__cig__params__test.md#af2ed1bf1a6beaff884c3ce3faf26bfb2);

[ 2182](structbt__hci__cp__le__set__cig__params__test.md#aa77765d90fde67c52e4f2d483f0a3ee0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [iso\_interval](structbt__hci__cp__le__set__cig__params__test.md#aa77765d90fde67c52e4f2d483f0a3ee0);

[ 2183](structbt__hci__cp__le__set__cig__params__test.md#a1d060539ff26677c1326a6ed3394fb6e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sca](structbt__hci__cp__le__set__cig__params__test.md#a1d060539ff26677c1326a6ed3394fb6e);

[ 2184](structbt__hci__cp__le__set__cig__params__test.md#a7275312e8b1c8ebc2af7992f765b392c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packing](structbt__hci__cp__le__set__cig__params__test.md#a7275312e8b1c8ebc2af7992f765b392c);

[ 2185](structbt__hci__cp__le__set__cig__params__test.md#a2cb6745b8f908cd2e7d5f12a092c3b69) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [framing](structbt__hci__cp__le__set__cig__params__test.md#a2cb6745b8f908cd2e7d5f12a092c3b69);

[ 2186](structbt__hci__cp__le__set__cig__params__test.md#a50c345ef03c669f476e143728f42cd6d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_cis](structbt__hci__cp__le__set__cig__params__test.md#a50c345ef03c669f476e143728f42cd6d);

[ 2187](structbt__hci__cp__le__set__cig__params__test.md#a5e07eb0d7d13e57be457d1b77a5dba12) struct [bt\_hci\_cis\_params\_test](structbt__hci__cis__params__test.md) [cis](structbt__hci__cp__le__set__cig__params__test.md#a5e07eb0d7d13e57be457d1b77a5dba12)[0];

2188} \_\_packed;

2189

[ 2190](structbt__hci__rp__le__set__cig__params__test.md)struct [bt\_hci\_rp\_le\_set\_cig\_params\_test](structbt__hci__rp__le__set__cig__params__test.md) {

[ 2191](structbt__hci__rp__le__set__cig__params__test.md#a932eadb4d750f79b4a7a9c3feb90fdcd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__set__cig__params__test.md#a932eadb4d750f79b4a7a9c3feb90fdcd);

[ 2192](structbt__hci__rp__le__set__cig__params__test.md#a65c11059bc00244e58d2ab8373e3e725) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cig\_id](structbt__hci__rp__le__set__cig__params__test.md#a65c11059bc00244e58d2ab8373e3e725);

[ 2193](structbt__hci__rp__le__set__cig__params__test.md#a10816d0875092c8e6bd4b13b819c43c7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_handles](structbt__hci__rp__le__set__cig__params__test.md#a10816d0875092c8e6bd4b13b819c43c7);

[ 2194](structbt__hci__rp__le__set__cig__params__test.md#a08b07863ed63ab627401c0c80bc3c7b4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__set__cig__params__test.md#a08b07863ed63ab627401c0c80bc3c7b4)[0];

2195} \_\_packed;

2196

[ 2197](hci__types_8h.md#a63c9af35a55d9b1ed1b253d057657608)#define BT\_HCI\_OP\_LE\_CREATE\_CIS BT\_OP(BT\_OGF\_LE, 0x0064) /\* 0x2064 \*/

[ 2198](structbt__hci__cis.md)struct [bt\_hci\_cis](structbt__hci__cis.md) {

[ 2199](structbt__hci__cis.md#a84165d526c10a91fa42d306276d97c74) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cis\_handle](structbt__hci__cis.md#a84165d526c10a91fa42d306276d97c74);

[ 2200](structbt__hci__cis.md#a754c3c75c0ad13a11d89fa3347112e2c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [acl\_handle](structbt__hci__cis.md#a754c3c75c0ad13a11d89fa3347112e2c);

2201} \_\_packed;

2202

[ 2203](structbt__hci__cp__le__create__cis.md)struct [bt\_hci\_cp\_le\_create\_cis](structbt__hci__cp__le__create__cis.md) {

[ 2204](structbt__hci__cp__le__create__cis.md#acd348a7d68947af8e7119b2e1a864481) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_cis](structbt__hci__cp__le__create__cis.md#acd348a7d68947af8e7119b2e1a864481);

[ 2205](structbt__hci__cp__le__create__cis.md#a5a323d09df7813fc9b834cc1d205d101) struct [bt\_hci\_cis](structbt__hci__cis.md) [cis](structbt__hci__cp__le__create__cis.md#a5a323d09df7813fc9b834cc1d205d101)[0];

2206} \_\_packed;

2207

[ 2208](hci__types_8h.md#ab623f680f2031fc03bd73199ebbf4e4e)#define BT\_HCI\_OP\_LE\_REMOVE\_CIG BT\_OP(BT\_OGF\_LE, 0x0065) /\* 0x2065 \*/

[ 2209](structbt__hci__cp__le__remove__cig.md)struct [bt\_hci\_cp\_le\_remove\_cig](structbt__hci__cp__le__remove__cig.md) {

[ 2210](structbt__hci__cp__le__remove__cig.md#addf395d945f14afbf2d39fa4d0d22f31) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cig\_id](structbt__hci__cp__le__remove__cig.md#addf395d945f14afbf2d39fa4d0d22f31);

2211} \_\_packed;

2212

[ 2213](structbt__hci__rp__le__remove__cig.md)struct [bt\_hci\_rp\_le\_remove\_cig](structbt__hci__rp__le__remove__cig.md) {

[ 2214](structbt__hci__rp__le__remove__cig.md#a1335f26f1dc67ff8e2a1960d1b24b1a0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__remove__cig.md#a1335f26f1dc67ff8e2a1960d1b24b1a0);

[ 2215](structbt__hci__rp__le__remove__cig.md#a82e74fbbce714b035b1e53fd5f1b09b5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cig\_id](structbt__hci__rp__le__remove__cig.md#a82e74fbbce714b035b1e53fd5f1b09b5);

2216} \_\_packed;

2217

[ 2218](hci__types_8h.md#ade7635c85588941a2e628639be06ce7b)#define BT\_HCI\_OP\_LE\_ACCEPT\_CIS BT\_OP(BT\_OGF\_LE, 0x0066) /\* 0x2066 \*/

[ 2219](structbt__hci__cp__le__accept__cis.md)struct [bt\_hci\_cp\_le\_accept\_cis](structbt__hci__cp__le__accept__cis.md) {

[ 2220](structbt__hci__cp__le__accept__cis.md#aec6a6c80403d5827df10cd8722bc12e4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__accept__cis.md#aec6a6c80403d5827df10cd8722bc12e4);

2221} \_\_packed;

2222

[ 2223](hci__types_8h.md#a6c58ebc2082de8c2c3aafd9ee77dfd11)#define BT\_HCI\_OP\_LE\_REJECT\_CIS BT\_OP(BT\_OGF\_LE, 0x0067) /\* 0x2067 \*/

[ 2224](structbt__hci__cp__le__reject__cis.md)struct [bt\_hci\_cp\_le\_reject\_cis](structbt__hci__cp__le__reject__cis.md) {

[ 2225](structbt__hci__cp__le__reject__cis.md#ad697d740bdf5a565090a548e7e8fd399) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__reject__cis.md#ad697d740bdf5a565090a548e7e8fd399);

[ 2226](structbt__hci__cp__le__reject__cis.md#aec5bd3e4d27b6e3a2653112b36a3d128) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reason](structbt__hci__cp__le__reject__cis.md#aec5bd3e4d27b6e3a2653112b36a3d128);

2227} \_\_packed;

2228

[ 2229](structbt__hci__rp__le__reject__cis.md)struct [bt\_hci\_rp\_le\_reject\_cis](structbt__hci__rp__le__reject__cis.md) {

[ 2230](structbt__hci__rp__le__reject__cis.md#af2dc8a839d3e19821ab8ec0d3dc427ec) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__reject__cis.md#af2dc8a839d3e19821ab8ec0d3dc427ec);

[ 2231](structbt__hci__rp__le__reject__cis.md#acd8311e13bdfd7edb2d404d80006f9d4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__reject__cis.md#acd8311e13bdfd7edb2d404d80006f9d4);

2232} \_\_packed;

2233

[ 2234](hci__types_8h.md#a2a57bb6089e3a064e62119188b555ba9)#define BT\_HCI\_OP\_LE\_CREATE\_BIG BT\_OP(BT\_OGF\_LE, 0x0068) /\* 0x2068 \*/

[ 2235](structbt__hci__cp__le__create__big.md)struct [bt\_hci\_cp\_le\_create\_big](structbt__hci__cp__le__create__big.md) {

[ 2236](structbt__hci__cp__le__create__big.md#af5412e4a69c05a09b2e818322636a98a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [big\_handle](structbt__hci__cp__le__create__big.md#af5412e4a69c05a09b2e818322636a98a);

[ 2237](structbt__hci__cp__le__create__big.md#aa686eec31ca4c831262dd34d41f9a1fb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_handle](structbt__hci__cp__le__create__big.md#aa686eec31ca4c831262dd34d41f9a1fb);

[ 2238](structbt__hci__cp__le__create__big.md#ad8491c970417e63c6a98c12278a89c86) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_bis](structbt__hci__cp__le__create__big.md#ad8491c970417e63c6a98c12278a89c86);

[ 2239](structbt__hci__cp__le__create__big.md#a2960a9891b827529c9fa1b68a747e2d5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sdu\_interval](structbt__hci__cp__le__create__big.md#a2960a9891b827529c9fa1b68a747e2d5)[3];

[ 2240](structbt__hci__cp__le__create__big.md#a06fd74e9a5f172060835524da5851c71) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_sdu](structbt__hci__cp__le__create__big.md#a06fd74e9a5f172060835524da5851c71);

[ 2241](structbt__hci__cp__le__create__big.md#a15018e5ebc124bbe90644b38fe3e7e76) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_latency](structbt__hci__cp__le__create__big.md#a15018e5ebc124bbe90644b38fe3e7e76);

[ 2242](structbt__hci__cp__le__create__big.md#a1cb0dd106bf4a1a0c473333d089c95e7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rtn](structbt__hci__cp__le__create__big.md#a1cb0dd106bf4a1a0c473333d089c95e7);

[ 2243](structbt__hci__cp__le__create__big.md#a56cb773a03e4927c3b6bf4d2a6ed6ed9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__cp__le__create__big.md#a56cb773a03e4927c3b6bf4d2a6ed6ed9);

[ 2244](structbt__hci__cp__le__create__big.md#ac027390db21320fb9d1002161c4c2f67) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packing](structbt__hci__cp__le__create__big.md#ac027390db21320fb9d1002161c4c2f67);

[ 2245](structbt__hci__cp__le__create__big.md#a330916d60c05ec2ef7a71933b62c203a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [framing](structbt__hci__cp__le__create__big.md#a330916d60c05ec2ef7a71933b62c203a);

[ 2246](structbt__hci__cp__le__create__big.md#a490bd68d137f8cf60ea2ccd5ea4495e9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [encryption](structbt__hci__cp__le__create__big.md#a490bd68d137f8cf60ea2ccd5ea4495e9);

[ 2247](structbt__hci__cp__le__create__big.md#a0b4b2d77cd0f579aab190336b14597c5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bcode](structbt__hci__cp__le__create__big.md#a0b4b2d77cd0f579aab190336b14597c5)[16];

2248} \_\_packed;

2249

[ 2250](hci__types_8h.md#ad0f1ae4be3f5bb90ef967d88dcaaf353)#define BT\_HCI\_OP\_LE\_CREATE\_BIG\_TEST BT\_OP(BT\_OGF\_LE, 0x0069) /\* 0x2069 \*/

[ 2251](structbt__hci__cp__le__create__big__test.md)struct [bt\_hci\_cp\_le\_create\_big\_test](structbt__hci__cp__le__create__big__test.md) {

[ 2252](structbt__hci__cp__le__create__big__test.md#ac202f5cee0c1d0456b200606860fd5ab) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [big\_handle](structbt__hci__cp__le__create__big__test.md#ac202f5cee0c1d0456b200606860fd5ab);

[ 2253](structbt__hci__cp__le__create__big__test.md#aece09ae6264e0cc1a5548f1603a3f61a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_handle](structbt__hci__cp__le__create__big__test.md#aece09ae6264e0cc1a5548f1603a3f61a);

[ 2254](structbt__hci__cp__le__create__big__test.md#a6ce270f0afd185c44fa5a2c67a7783fb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_bis](structbt__hci__cp__le__create__big__test.md#a6ce270f0afd185c44fa5a2c67a7783fb);

[ 2255](structbt__hci__cp__le__create__big__test.md#a331b1a8ef66804cf20d6681e1bc5aefb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sdu\_interval](structbt__hci__cp__le__create__big__test.md#a331b1a8ef66804cf20d6681e1bc5aefb)[3];

[ 2256](structbt__hci__cp__le__create__big__test.md#a6475ae77af80e89bb65596bc6f907a58) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [iso\_interval](structbt__hci__cp__le__create__big__test.md#a6475ae77af80e89bb65596bc6f907a58);

[ 2257](structbt__hci__cp__le__create__big__test.md#a402c19da1ecf273bc942ecc560730567) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [nse](structbt__hci__cp__le__create__big__test.md#a402c19da1ecf273bc942ecc560730567);

[ 2258](structbt__hci__cp__le__create__big__test.md#a7ebbc81306109e035f89154738900395) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_sdu](structbt__hci__cp__le__create__big__test.md#a7ebbc81306109e035f89154738900395);

[ 2259](structbt__hci__cp__le__create__big__test.md#a2652e0f340f13635a5da6335ec43e801) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_pdu](structbt__hci__cp__le__create__big__test.md#a2652e0f340f13635a5da6335ec43e801);

[ 2260](structbt__hci__cp__le__create__big__test.md#a731ca2f90c17a4f3f868660e51649ce6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__cp__le__create__big__test.md#a731ca2f90c17a4f3f868660e51649ce6);

[ 2261](structbt__hci__cp__le__create__big__test.md#a49822f8e1617e30aab9b0d7d790697a3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packing](structbt__hci__cp__le__create__big__test.md#a49822f8e1617e30aab9b0d7d790697a3);

[ 2262](structbt__hci__cp__le__create__big__test.md#acc5b2c30db0c7642d12019f8241dab26) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [framing](structbt__hci__cp__le__create__big__test.md#acc5b2c30db0c7642d12019f8241dab26);

[ 2263](structbt__hci__cp__le__create__big__test.md#a734174187486ac760b8bf0e566166842) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bn](structbt__hci__cp__le__create__big__test.md#a734174187486ac760b8bf0e566166842);

[ 2264](structbt__hci__cp__le__create__big__test.md#a66ce7ba0498053a588de9097cbbc0891) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [irc](structbt__hci__cp__le__create__big__test.md#a66ce7ba0498053a588de9097cbbc0891);

[ 2265](structbt__hci__cp__le__create__big__test.md#a2f2eaa258463dd51a9f6042e75ecfec6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pto](structbt__hci__cp__le__create__big__test.md#a2f2eaa258463dd51a9f6042e75ecfec6);

[ 2266](structbt__hci__cp__le__create__big__test.md#a50c4308abda01581b436b7867304e982) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [encryption](structbt__hci__cp__le__create__big__test.md#a50c4308abda01581b436b7867304e982);

[ 2267](structbt__hci__cp__le__create__big__test.md#a333319a03d2087067247c4f5e595b4e5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bcode](structbt__hci__cp__le__create__big__test.md#a333319a03d2087067247c4f5e595b4e5)[16];

2268} \_\_packed;

2269

[ 2270](hci__types_8h.md#acc5e6c17e33cf43f2a68cb93bb09ef20)#define BT\_HCI\_OP\_LE\_TERMINATE\_BIG BT\_OP(BT\_OGF\_LE, 0x006a) /\* 0x206a \*/

[ 2271](structbt__hci__cp__le__terminate__big.md)struct [bt\_hci\_cp\_le\_terminate\_big](structbt__hci__cp__le__terminate__big.md) {

[ 2272](structbt__hci__cp__le__terminate__big.md#acb5fb9451cf890245a85704579b1d1c8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [big\_handle](structbt__hci__cp__le__terminate__big.md#acb5fb9451cf890245a85704579b1d1c8);

[ 2273](structbt__hci__cp__le__terminate__big.md#a958ab6b2f2bb30c825060498e6917a18) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reason](structbt__hci__cp__le__terminate__big.md#a958ab6b2f2bb30c825060498e6917a18);

2274} \_\_packed;

2275

[ 2276](hci__types_8h.md#a47af328ede7f14e3d78c81de609af1c9)#define BT\_HCI\_OP\_LE\_BIG\_CREATE\_SYNC BT\_OP(BT\_OGF\_LE, 0x006b) /\* 0x206b \*/

[ 2277](structbt__hci__cp__le__big__create__sync.md)struct [bt\_hci\_cp\_le\_big\_create\_sync](structbt__hci__cp__le__big__create__sync.md) {

[ 2278](structbt__hci__cp__le__big__create__sync.md#a6692dae077ce1ce4f31bc94b9d391afd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [big\_handle](structbt__hci__cp__le__big__create__sync.md#a6692dae077ce1ce4f31bc94b9d391afd);

[ 2279](structbt__hci__cp__le__big__create__sync.md#a70b031f24cdf231e5c168b155517eae0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sync\_handle](structbt__hci__cp__le__big__create__sync.md#a70b031f24cdf231e5c168b155517eae0);

[ 2280](structbt__hci__cp__le__big__create__sync.md#a482edf3326e2dd720b14a03609c1256a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [encryption](structbt__hci__cp__le__big__create__sync.md#a482edf3326e2dd720b14a03609c1256a);

[ 2281](structbt__hci__cp__le__big__create__sync.md#a053475c3af12e6e37dc4befcf634d68f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bcode](structbt__hci__cp__le__big__create__sync.md#a053475c3af12e6e37dc4befcf634d68f)[16];

[ 2282](structbt__hci__cp__le__big__create__sync.md#a37050e3eb914ff06495695d44c3fdb50) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mse](structbt__hci__cp__le__big__create__sync.md#a37050e3eb914ff06495695d44c3fdb50);

[ 2283](structbt__hci__cp__le__big__create__sync.md#a55e83bc3722ce2dbf943879a80ef2872) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sync\_timeout](structbt__hci__cp__le__big__create__sync.md#a55e83bc3722ce2dbf943879a80ef2872);

[ 2284](structbt__hci__cp__le__big__create__sync.md#a7efae2c8dc46d13fb2abca677ac152b0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_bis](structbt__hci__cp__le__big__create__sync.md#a7efae2c8dc46d13fb2abca677ac152b0);

[ 2285](structbt__hci__cp__le__big__create__sync.md#a6d1050c2a0522be215d82d3874fed4b6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bis](structbt__hci__cp__le__big__create__sync.md#a6d1050c2a0522be215d82d3874fed4b6)[0];

2286} \_\_packed;

2287

[ 2288](hci__types_8h.md#aa7576f4ab30ec7985b4afd08a08800d2)#define BT\_HCI\_OP\_LE\_BIG\_TERMINATE\_SYNC BT\_OP(BT\_OGF\_LE, 0x006c) /\* 0x206c \*/

[ 2289](structbt__hci__cp__le__big__terminate__sync.md)struct [bt\_hci\_cp\_le\_big\_terminate\_sync](structbt__hci__cp__le__big__terminate__sync.md) {

[ 2290](structbt__hci__cp__le__big__terminate__sync.md#ad7e4de2a9a3222c1bb8fa048cacd06fa) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [big\_handle](structbt__hci__cp__le__big__terminate__sync.md#ad7e4de2a9a3222c1bb8fa048cacd06fa);

2291} \_\_packed;

2292

[ 2293](structbt__hci__rp__le__big__terminate__sync.md)struct [bt\_hci\_rp\_le\_big\_terminate\_sync](structbt__hci__rp__le__big__terminate__sync.md) {

[ 2294](structbt__hci__rp__le__big__terminate__sync.md#ad4d1d4238402ef829a1ff9ed3b1dc050) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__big__terminate__sync.md#ad4d1d4238402ef829a1ff9ed3b1dc050);

[ 2295](structbt__hci__rp__le__big__terminate__sync.md#a741ab80e08e7ecfc5a0158ec0cf14654) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [big\_handle](structbt__hci__rp__le__big__terminate__sync.md#a741ab80e08e7ecfc5a0158ec0cf14654);

2296} \_\_packed;

2297

[ 2298](hci__types_8h.md#a0057468b1638b07f799b62a24cd096d9)#define BT\_HCI\_OP\_LE\_REQ\_PEER\_SC BT\_OP(BT\_OGF\_LE, 0x006d) /\* 0x206d \*/

[ 2299](structbt__hci__cp__le__req__peer__sca.md)struct [bt\_hci\_cp\_le\_req\_peer\_sca](structbt__hci__cp__le__req__peer__sca.md) {

[ 2300](structbt__hci__cp__le__req__peer__sca.md#a39d65681da55b26f2900f06cde637d88) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__req__peer__sca.md#a39d65681da55b26f2900f06cde637d88);

2301} \_\_packed;

2302

[ 2303](hci__types_8h.md#a97de1164704f5d3c517b9c2ff6b0584a)#define BT\_HCI\_OP\_LE\_SETUP\_ISO\_PATH BT\_OP(BT\_OGF\_LE, 0x006e) /\* 0x206e \*/

[ 2304](structbt__hci__cp__le__setup__iso__path.md)struct [bt\_hci\_cp\_le\_setup\_iso\_path](structbt__hci__cp__le__setup__iso__path.md) {

[ 2305](structbt__hci__cp__le__setup__iso__path.md#a0054fede0e583cef0dbcf6ef3134e480) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__setup__iso__path.md#a0054fede0e583cef0dbcf6ef3134e480);

[ 2306](structbt__hci__cp__le__setup__iso__path.md#a89c1324359a4fc2f10fee9ebbac5cf2b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [path\_dir](structbt__hci__cp__le__setup__iso__path.md#a89c1324359a4fc2f10fee9ebbac5cf2b);

[ 2307](structbt__hci__cp__le__setup__iso__path.md#a7c07d69b2005af1f7f2618f2bfa60d50) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [path\_id](structbt__hci__cp__le__setup__iso__path.md#a7c07d69b2005af1f7f2618f2bfa60d50);

[ 2308](structbt__hci__cp__le__setup__iso__path.md#a5256fc99b362e3a5f986ef2b71b29ccb) struct [bt\_hci\_cp\_codec\_id](structbt__hci__cp__codec__id.md) [codec\_id](structbt__hci__cp__le__setup__iso__path.md#a5256fc99b362e3a5f986ef2b71b29ccb);

[ 2309](structbt__hci__cp__le__setup__iso__path.md#a31948436e6608f9943d34ce89a65c64c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [controller\_delay](structbt__hci__cp__le__setup__iso__path.md#a31948436e6608f9943d34ce89a65c64c)[3];

[ 2310](structbt__hci__cp__le__setup__iso__path.md#a1a816d8e8c434a05ea897b74bc4d89c7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [codec\_config\_len](structbt__hci__cp__le__setup__iso__path.md#a1a816d8e8c434a05ea897b74bc4d89c7);

[ 2311](structbt__hci__cp__le__setup__iso__path.md#ade4dee947e3d288f769d2d69fc57f96a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [codec\_config](structbt__hci__cp__le__setup__iso__path.md#ade4dee947e3d288f769d2d69fc57f96a)[0];

2312} \_\_packed;

2313

[ 2314](structbt__hci__rp__le__setup__iso__path.md)struct [bt\_hci\_rp\_le\_setup\_iso\_path](structbt__hci__rp__le__setup__iso__path.md) {

[ 2315](structbt__hci__rp__le__setup__iso__path.md#adde60b0dc6ec3d8caccae1d55d78d9a4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__setup__iso__path.md#adde60b0dc6ec3d8caccae1d55d78d9a4);

[ 2316](structbt__hci__rp__le__setup__iso__path.md#aa8effdcc4ba155b840ef789f20bad19e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__setup__iso__path.md#aa8effdcc4ba155b840ef789f20bad19e);

2317} \_\_packed;

2318

[ 2319](hci__types_8h.md#addec65d76f67f07c029216435cf117c6)#define BT\_HCI\_OP\_LE\_REMOVE\_ISO\_PATH BT\_OP(BT\_OGF\_LE, 0x006f) /\* 0x206f \*/

[ 2320](structbt__hci__cp__le__remove__iso__path.md)struct [bt\_hci\_cp\_le\_remove\_iso\_path](structbt__hci__cp__le__remove__iso__path.md) {

[ 2321](structbt__hci__cp__le__remove__iso__path.md#ad0106791003f9d1173f2a9f102903c45) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__remove__iso__path.md#ad0106791003f9d1173f2a9f102903c45);

[ 2322](structbt__hci__cp__le__remove__iso__path.md#a46e4b28917ff963ff4b672749fde0971) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [path\_dir](structbt__hci__cp__le__remove__iso__path.md#a46e4b28917ff963ff4b672749fde0971);

2323} \_\_packed;

2324

[ 2325](structbt__hci__rp__le__remove__iso__path.md)struct [bt\_hci\_rp\_le\_remove\_iso\_path](structbt__hci__rp__le__remove__iso__path.md) {

[ 2326](structbt__hci__rp__le__remove__iso__path.md#ab22e50e594e19931526feacd9bff33a3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__remove__iso__path.md#ab22e50e594e19931526feacd9bff33a3);

[ 2327](structbt__hci__rp__le__remove__iso__path.md#ae3b7704359989ca13582a5cd3742f588) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__remove__iso__path.md#ae3b7704359989ca13582a5cd3742f588);

2328} \_\_packed;

2329

[ 2330](hci__types_8h.md#aa857bdd2e81c923ab540761986074557)#define BT\_HCI\_ISO\_TEST\_ZERO\_SIZE\_SDU 0

[ 2331](hci__types_8h.md#aed9e2581c74218e023100d63201721af)#define BT\_HCI\_ISO\_TEST\_VARIABLE\_SIZE\_SDU 1

[ 2332](hci__types_8h.md#af5c0bf9fd20df7b4a4cdb7ce18fdc7fc)#define BT\_HCI\_ISO\_TEST\_MAX\_SIZE\_SDU 2

2333

[ 2334](hci__types_8h.md#a740f1964df5bdb675906c87ad8ee0cef)#define BT\_HCI\_OP\_LE\_ISO\_TRANSMIT\_TEST BT\_OP(BT\_OGF\_LE, 0x0070) /\* 0x2070 \*/

[ 2335](structbt__hci__cp__le__iso__transmit__test.md)struct [bt\_hci\_cp\_le\_iso\_transmit\_test](structbt__hci__cp__le__iso__transmit__test.md) {

[ 2336](structbt__hci__cp__le__iso__transmit__test.md#adffb0d57afc090692ab36ebeaad21bbd) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__iso__transmit__test.md#adffb0d57afc090692ab36ebeaad21bbd);

[ 2337](structbt__hci__cp__le__iso__transmit__test.md#a0653c77af723cc43a6b911816a8db437) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [payload\_type](structbt__hci__cp__le__iso__transmit__test.md#a0653c77af723cc43a6b911816a8db437);

2338} \_\_packed;

2339

[ 2340](structbt__hci__rp__le__iso__transmit__test.md)struct [bt\_hci\_rp\_le\_iso\_transmit\_test](structbt__hci__rp__le__iso__transmit__test.md) {

[ 2341](structbt__hci__rp__le__iso__transmit__test.md#a01ae01d11c606f559107b8c54781d843) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__iso__transmit__test.md#a01ae01d11c606f559107b8c54781d843);

[ 2342](structbt__hci__rp__le__iso__transmit__test.md#a0863c47551b328984e00c392f9f11660) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__iso__transmit__test.md#a0863c47551b328984e00c392f9f11660);

2343} \_\_packed;

2344

[ 2345](hci__types_8h.md#a467736569f030fbb433000e712f1b08e)#define BT\_HCI\_OP\_LE\_ISO\_RECEIVE\_TEST BT\_OP(BT\_OGF\_LE, 0x0071) /\* 0x2071 \*/

[ 2346](structbt__hci__cp__le__iso__receive__test.md)struct [bt\_hci\_cp\_le\_iso\_receive\_test](structbt__hci__cp__le__iso__receive__test.md) {

[ 2347](structbt__hci__cp__le__iso__receive__test.md#ac1272441f5c7b79e1ef5f644f099d19e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__iso__receive__test.md#ac1272441f5c7b79e1ef5f644f099d19e);

[ 2348](structbt__hci__cp__le__iso__receive__test.md#a9ce7e13fc1c1a7c87c01e1ecb24c5324) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [payload\_type](structbt__hci__cp__le__iso__receive__test.md#a9ce7e13fc1c1a7c87c01e1ecb24c5324);

2349} \_\_packed;

2350

[ 2351](structbt__hci__rp__le__iso__receive__test.md)struct [bt\_hci\_rp\_le\_iso\_receive\_test](structbt__hci__rp__le__iso__receive__test.md) {

[ 2352](structbt__hci__rp__le__iso__receive__test.md#a028a77001a5e24dda8fac38718103ef0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__iso__receive__test.md#a028a77001a5e24dda8fac38718103ef0);

[ 2353](structbt__hci__rp__le__iso__receive__test.md#a863a8a44af979a8b1b9d084563b2fe9a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__iso__receive__test.md#a863a8a44af979a8b1b9d084563b2fe9a);

2354} \_\_packed;

2355

[ 2356](hci__types_8h.md#a2b988ffc8ffd10ce1dfde377afa699e1)#define BT\_HCI\_OP\_LE\_ISO\_READ\_TEST\_COUNTERS BT\_OP(BT\_OGF\_LE, 0x0072) /\* 0x2072 \*/

[ 2357](structbt__hci__cp__le__read__test__counters.md)struct [bt\_hci\_cp\_le\_read\_test\_counters](structbt__hci__cp__le__read__test__counters.md) {

[ 2358](structbt__hci__cp__le__read__test__counters.md#a230d973c2db177c3595bb4808ebf5cd2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__read__test__counters.md#a230d973c2db177c3595bb4808ebf5cd2);

2359} \_\_packed;

2360

[ 2361](structbt__hci__rp__le__read__test__counters.md)struct [bt\_hci\_rp\_le\_read\_test\_counters](structbt__hci__rp__le__read__test__counters.md) {

[ 2362](structbt__hci__rp__le__read__test__counters.md#ae1e78d68e9f55b31092a07575a66c1c0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__test__counters.md#ae1e78d68e9f55b31092a07575a66c1c0);

[ 2363](structbt__hci__rp__le__read__test__counters.md#a8121f879a3fb5550cc1aa468aacb81b7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__read__test__counters.md#a8121f879a3fb5550cc1aa468aacb81b7);

[ 2364](structbt__hci__rp__le__read__test__counters.md#a8c4b2674fb129ca0de0bc45c608e13c7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [received\_cnt](structbt__hci__rp__le__read__test__counters.md#a8c4b2674fb129ca0de0bc45c608e13c7);

[ 2365](structbt__hci__rp__le__read__test__counters.md#ae96d05ffb2fbc681c804b04c8791aeab) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [missed\_cnt](structbt__hci__rp__le__read__test__counters.md#ae96d05ffb2fbc681c804b04c8791aeab);

[ 2366](structbt__hci__rp__le__read__test__counters.md#af6261d3547cd9b377fedc7a36891c2f7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [failed\_cnt](structbt__hci__rp__le__read__test__counters.md#af6261d3547cd9b377fedc7a36891c2f7);

2367} \_\_packed;

2368

[ 2369](hci__types_8h.md#a86436e6b0cb17de95b438f192bbff1d2)#define BT\_HCI\_OP\_LE\_ISO\_TEST\_END BT\_OP(BT\_OGF\_LE, 0x0073) /\* 0x2073 \*/

[ 2370](structbt__hci__cp__le__iso__test__end.md)struct [bt\_hci\_cp\_le\_iso\_test\_end](structbt__hci__cp__le__iso__test__end.md) {

[ 2371](structbt__hci__cp__le__iso__test__end.md#ab792ec021319024828bd7609e0fe7e96) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__iso__test__end.md#ab792ec021319024828bd7609e0fe7e96);

2372} \_\_packed;

2373

[ 2374](structbt__hci__rp__le__iso__test__end.md)struct [bt\_hci\_rp\_le\_iso\_test\_end](structbt__hci__rp__le__iso__test__end.md) {

[ 2375](structbt__hci__rp__le__iso__test__end.md#a16feaeb739f6ed34d9ce3fc86248955c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__iso__test__end.md#a16feaeb739f6ed34d9ce3fc86248955c);

[ 2376](structbt__hci__rp__le__iso__test__end.md#a4a4625d7b78abf3c039842df2a72ce8b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__iso__test__end.md#a4a4625d7b78abf3c039842df2a72ce8b);

[ 2377](structbt__hci__rp__le__iso__test__end.md#a55490978e7416ecc308bf510f05afd4f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [received\_cnt](structbt__hci__rp__le__iso__test__end.md#a55490978e7416ecc308bf510f05afd4f);

[ 2378](structbt__hci__rp__le__iso__test__end.md#a10b3ee6110bc0bb9279b22f9963715c1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [missed\_cnt](structbt__hci__rp__le__iso__test__end.md#a10b3ee6110bc0bb9279b22f9963715c1);

[ 2379](structbt__hci__rp__le__iso__test__end.md#ab4352fd5d9b822fb7fb75f8f5e2db6a9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [failed\_cnt](structbt__hci__rp__le__iso__test__end.md#ab4352fd5d9b822fb7fb75f8f5e2db6a9);

2380} \_\_packed;

2381

[ 2382](hci__types_8h.md#a29555bdcc7b439c2d0311fcb0721dc0b)#define BT\_HCI\_OP\_LE\_SET\_HOST\_FEATURE BT\_OP(BT\_OGF\_LE, 0x0074) /\* 0x2074 \*/

[ 2383](structbt__hci__cp__le__set__host__feature.md)struct [bt\_hci\_cp\_le\_set\_host\_feature](structbt__hci__cp__le__set__host__feature.md) {

[ 2384](structbt__hci__cp__le__set__host__feature.md#adcca35df216061ea08bd27e10fefd5e9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bit\_number](structbt__hci__cp__le__set__host__feature.md#adcca35df216061ea08bd27e10fefd5e9);

[ 2385](structbt__hci__cp__le__set__host__feature.md#a78b67164bce232466ab348f8937682c3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bit\_value](structbt__hci__cp__le__set__host__feature.md#a78b67164bce232466ab348f8937682c3);

2386} \_\_packed;

2387

[ 2388](structbt__hci__rp__le__set__host__feature.md)struct [bt\_hci\_rp\_le\_set\_host\_feature](structbt__hci__rp__le__set__host__feature.md) {

[ 2389](structbt__hci__rp__le__set__host__feature.md#a2e7cfc16da9fc0d00c35111811bf7c28) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__set__host__feature.md#a2e7cfc16da9fc0d00c35111811bf7c28);

2390} \_\_packed;

2391

[ 2392](hci__types_8h.md#acd6367a62d2c80d9f2e796d7b6ab1417)#define BT\_HCI\_OP\_LE\_READ\_ISO\_LINK\_QUALITY BT\_OP(BT\_OGF\_LE, 0x0075) /\* 0x2075 \*/

[ 2393](structbt__hci__cp__le__read__iso__link__quality.md)struct [bt\_hci\_cp\_le\_read\_iso\_link\_quality](structbt__hci__cp__le__read__iso__link__quality.md) {

[ 2394](structbt__hci__cp__le__read__iso__link__quality.md#a346fb3cf08203725d5943e42f03cb40d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__read__iso__link__quality.md#a346fb3cf08203725d5943e42f03cb40d);

2395} \_\_packed;

2396

[ 2397](structbt__hci__rp__le__read__iso__link__quality.md)struct [bt\_hci\_rp\_le\_read\_iso\_link\_quality](structbt__hci__rp__le__read__iso__link__quality.md) {

[ 2398](structbt__hci__rp__le__read__iso__link__quality.md#aef80c600f8916c098e08c43ca718d630) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__iso__link__quality.md#aef80c600f8916c098e08c43ca718d630);

[ 2399](structbt__hci__rp__le__read__iso__link__quality.md#a9f2e8c26081ede43c7712b851d79f2cd) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__read__iso__link__quality.md#a9f2e8c26081ede43c7712b851d79f2cd);

[ 2400](structbt__hci__rp__le__read__iso__link__quality.md#aae42e05dff474062726b92c6d45eae4f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tx\_unacked\_packets](structbt__hci__rp__le__read__iso__link__quality.md#aae42e05dff474062726b92c6d45eae4f);

[ 2401](structbt__hci__rp__le__read__iso__link__quality.md#a12c0c3f9fe6c3c94742367f30bdcc630) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tx\_flushed\_packets](structbt__hci__rp__le__read__iso__link__quality.md#a12c0c3f9fe6c3c94742367f30bdcc630);

[ 2402](structbt__hci__rp__le__read__iso__link__quality.md#a0d4468f6871716414ef4a601791bac58) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tx\_last\_subevent\_packets](structbt__hci__rp__le__read__iso__link__quality.md#a0d4468f6871716414ef4a601791bac58);

[ 2403](structbt__hci__rp__le__read__iso__link__quality.md#a7be135da9607045f60b616b84a68f5db) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [retransmitted\_packets](structbt__hci__rp__le__read__iso__link__quality.md#a7be135da9607045f60b616b84a68f5db);

[ 2404](structbt__hci__rp__le__read__iso__link__quality.md#a353070a64655a39f5410fe76e9168e97) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [crc\_error\_packets](structbt__hci__rp__le__read__iso__link__quality.md#a353070a64655a39f5410fe76e9168e97);

[ 2405](structbt__hci__rp__le__read__iso__link__quality.md#a6a16d0aa7ed220bac1ade12eb0f7703e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rx\_unreceived\_packets](structbt__hci__rp__le__read__iso__link__quality.md#a6a16d0aa7ed220bac1ade12eb0f7703e);

[ 2406](structbt__hci__rp__le__read__iso__link__quality.md#a68c23277e65dc5694f5a27ee2cd364ff) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [duplicate\_packets](structbt__hci__rp__le__read__iso__link__quality.md#a68c23277e65dc5694f5a27ee2cd364ff);

2407} \_\_packed;

2408

[ 2409](hci__types_8h.md#a13827b7d7b656ea02c0620ec7b525f65)#define BT\_HCI\_OP\_LE\_TX\_TEST\_V4 BT\_OP(BT\_OGF\_LE, 0x007B) /\* 0x207B \*/

2410

[ 2411](structbt__hci__cp__le__tx__test__v4.md)struct [bt\_hci\_cp\_le\_tx\_test\_v4](structbt__hci__cp__le__tx__test__v4.md) {

[ 2412](structbt__hci__cp__le__tx__test__v4.md#a3ccae40f09b2763b2b07dc16982f3973) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_ch](structbt__hci__cp__le__tx__test__v4.md#a3ccae40f09b2763b2b07dc16982f3973);

[ 2413](structbt__hci__cp__le__tx__test__v4.md#a7a8e2610fb8903ccfb6e4b08017f6112) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [test\_data\_len](structbt__hci__cp__le__tx__test__v4.md#a7a8e2610fb8903ccfb6e4b08017f6112);

[ 2414](structbt__hci__cp__le__tx__test__v4.md#abdd393eb264f04acf65e2dce4bd65ac0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pkt\_payload](structbt__hci__cp__le__tx__test__v4.md#abdd393eb264f04acf65e2dce4bd65ac0);

[ 2415](structbt__hci__cp__le__tx__test__v4.md#a5db011159fe75f4522e03ea1efdc57bd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__cp__le__tx__test__v4.md#a5db011159fe75f4522e03ea1efdc57bd);

[ 2416](structbt__hci__cp__le__tx__test__v4.md#a8dea923a63e787de3bfe07611eb7a1ed) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_len](structbt__hci__cp__le__tx__test__v4.md#a8dea923a63e787de3bfe07611eb7a1ed);

[ 2417](structbt__hci__cp__le__tx__test__v4.md#ae950f71a3fcfca0cf738bc28693256cf) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__hci__cp__le__tx__test__v4.md#ae950f71a3fcfca0cf738bc28693256cf);

[ 2418](structbt__hci__cp__le__tx__test__v4.md#a2039a87b5f32c4a45b8f858808df7cdc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [switch\_pattern\_len](structbt__hci__cp__le__tx__test__v4.md#a2039a87b5f32c4a45b8f858808df7cdc);

[ 2419](structbt__hci__cp__le__tx__test__v4.md#a3fe8ab7c0ee389dce8592cb7a38bc42c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ant\_ids](structbt__hci__cp__le__tx__test__v4.md#a3fe8ab7c0ee389dce8592cb7a38bc42c)[0];

2420} \_\_packed;

2421

[ 2422](hci__types_8h.md#a034d4a4fd8f7d6d324efa820d0b627d1)#define BT\_HCI\_TX\_TEST\_POWER\_MIN -0x7F

[ 2423](hci__types_8h.md#a925dda1fdce843e0bbcdd4acff696440)#define BT\_HCI\_TX\_TEST\_POWER\_MAX 0x14

2424

[ 2425](hci__types_8h.md#a5d0fc1dbb127ba0a383e4e56bb503334)#define BT\_HCI\_TX\_TEST\_POWER\_MIN\_SET 0x7E

[ 2426](hci__types_8h.md#a2e9caac5d12f8df1ce69a54f603500ee)#define BT\_HCI\_TX\_TEST\_POWER\_MAX\_SET 0x7F

2427

2428/\* Helper structure for Tx power parameter in the HCI Tx Test v4 command.

2429 \* Previous parameter of this command is variable size so having separated structure

2430 \* for this parameter helps in command parameters unpacking.

2431 \*/

[ 2432](structbt__hci__cp__le__tx__test__v4__tx__power.md)struct [bt\_hci\_cp\_le\_tx\_test\_v4\_tx\_power](structbt__hci__cp__le__tx__test__v4__tx__power.md) {

[ 2433](structbt__hci__cp__le__tx__test__v4__tx__power.md#a2a8b1c31787066ad2b471aec5c261085) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__hci__cp__le__tx__test__v4__tx__power.md#a2a8b1c31787066ad2b471aec5c261085);

2434} \_\_packed;

2435

[ 2436](hci__types_8h.md#a84e0338551dd8256a821d960bf745208)#define BT\_HCI\_OP\_LE\_CS\_READ\_LOCAL\_SUPPORTED\_CAPABILITIES BT\_OP(BT\_OGF\_LE, 0x0089) /\* 0x2089 \*/

2437

[ 2438](structbt__hci__rp__le__read__local__supported__capabilities.md)struct [bt\_hci\_rp\_le\_read\_local\_supported\_capabilities](structbt__hci__rp__le__read__local__supported__capabilities.md) {

[ 2439](structbt__hci__rp__le__read__local__supported__capabilities.md#aaf578336893980f2ec1b2343b81860e5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__local__supported__capabilities.md#aaf578336893980f2ec1b2343b81860e5);

[ 2440](structbt__hci__rp__le__read__local__supported__capabilities.md#a5f59d0b65cc4e7e44e487fa5535b76a9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_config\_supported](structbt__hci__rp__le__read__local__supported__capabilities.md#a5f59d0b65cc4e7e44e487fa5535b76a9);

[ 2441](structbt__hci__rp__le__read__local__supported__capabilities.md#ad667ba51ffdbaf7754dea6f519615cb7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_consecutive\_procedures\_supported](structbt__hci__rp__le__read__local__supported__capabilities.md#ad667ba51ffdbaf7754dea6f519615cb7);

[ 2442](structbt__hci__rp__le__read__local__supported__capabilities.md#ae0767bb41b7b57e955ddbede2f83c166) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_antennas\_supported](structbt__hci__rp__le__read__local__supported__capabilities.md#ae0767bb41b7b57e955ddbede2f83c166);

[ 2443](structbt__hci__rp__le__read__local__supported__capabilities.md#a7975eb0ce27f0326d1d909bffef57840) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_antenna\_paths\_supported](structbt__hci__rp__le__read__local__supported__capabilities.md#a7975eb0ce27f0326d1d909bffef57840);

[ 2444](structbt__hci__rp__le__read__local__supported__capabilities.md#a0958a5426e0057e2b8ccb80c222d0248) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [roles\_supported](structbt__hci__rp__le__read__local__supported__capabilities.md#a0958a5426e0057e2b8ccb80c222d0248);

[ 2445](structbt__hci__rp__le__read__local__supported__capabilities.md#aaf09d10c19980729ef04654114919211) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [modes\_supported](structbt__hci__rp__le__read__local__supported__capabilities.md#aaf09d10c19980729ef04654114919211);

[ 2446](structbt__hci__rp__le__read__local__supported__capabilities.md#a24ffa02b6a8bfbff8b7d32f5ee46bea5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rtt\_capability](structbt__hci__rp__le__read__local__supported__capabilities.md#a24ffa02b6a8bfbff8b7d32f5ee46bea5);

[ 2447](structbt__hci__rp__le__read__local__supported__capabilities.md#a3a16c62ea321620608d706a80d90575e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rtt\_aa\_only\_n](structbt__hci__rp__le__read__local__supported__capabilities.md#a3a16c62ea321620608d706a80d90575e);

[ 2448](structbt__hci__rp__le__read__local__supported__capabilities.md#ababf476100298c2ba7d79bdadd7a9d1b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rtt\_sounding\_n](structbt__hci__rp__le__read__local__supported__capabilities.md#ababf476100298c2ba7d79bdadd7a9d1b);

[ 2449](structbt__hci__rp__le__read__local__supported__capabilities.md#ad90ce3e635b8bccd29eefe73303f6e42) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rtt\_random\_payload\_n](structbt__hci__rp__le__read__local__supported__capabilities.md#ad90ce3e635b8bccd29eefe73303f6e42);

[ 2450](structbt__hci__rp__le__read__local__supported__capabilities.md#a3eb4830443e7912bf8ca97f603b91545) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [nadm\_sounding\_capability](structbt__hci__rp__le__read__local__supported__capabilities.md#a3eb4830443e7912bf8ca97f603b91545);

[ 2451](structbt__hci__rp__le__read__local__supported__capabilities.md#a0e0bd5b1c624c7143b0229b5d3eeec6e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [nadm\_random\_capability](structbt__hci__rp__le__read__local__supported__capabilities.md#a0e0bd5b1c624c7143b0229b5d3eeec6e);

[ 2452](structbt__hci__rp__le__read__local__supported__capabilities.md#af3d1e7588f2429bb400fac81733748c3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cs\_sync\_phys\_supported](structbt__hci__rp__le__read__local__supported__capabilities.md#af3d1e7588f2429bb400fac81733748c3);

[ 2453](structbt__hci__rp__le__read__local__supported__capabilities.md#a8e7cc92cc4099774e8d0b385fc5f3d79) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [subfeatures\_supported](structbt__hci__rp__le__read__local__supported__capabilities.md#a8e7cc92cc4099774e8d0b385fc5f3d79);

[ 2454](structbt__hci__rp__le__read__local__supported__capabilities.md#a115ffe697da3e09ece4091493fa8f2da) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [t\_ip1\_times\_supported](structbt__hci__rp__le__read__local__supported__capabilities.md#a115ffe697da3e09ece4091493fa8f2da);

[ 2455](structbt__hci__rp__le__read__local__supported__capabilities.md#a88a4277c5dea41b8171c33c85ed760bf) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [t\_ip2\_times\_supported](structbt__hci__rp__le__read__local__supported__capabilities.md#a88a4277c5dea41b8171c33c85ed760bf);

[ 2456](structbt__hci__rp__le__read__local__supported__capabilities.md#a81bd809a734b6cdde2d55e0b23e41237) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [t\_fcs\_times\_supported](structbt__hci__rp__le__read__local__supported__capabilities.md#a81bd809a734b6cdde2d55e0b23e41237);

[ 2457](structbt__hci__rp__le__read__local__supported__capabilities.md#ab026e5abfdead47eca1c5d8d316bc62c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [t\_pm\_times\_supported](structbt__hci__rp__le__read__local__supported__capabilities.md#ab026e5abfdead47eca1c5d8d316bc62c);

[ 2458](structbt__hci__rp__le__read__local__supported__capabilities.md#ad07b464737c59b33de4c89948d4c5686) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [t\_sw\_time\_supported](structbt__hci__rp__le__read__local__supported__capabilities.md#ad07b464737c59b33de4c89948d4c5686);

[ 2459](structbt__hci__rp__le__read__local__supported__capabilities.md#a1806f2f5ec2738b026453bbdb8b38ce9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_snr\_capability](structbt__hci__rp__le__read__local__supported__capabilities.md#a1806f2f5ec2738b026453bbdb8b38ce9);

2460} \_\_packed;

2461

[ 2462](hci__types_8h.md#a4f6dd157a555e06cd028a9097fd7b81a)#define BT\_HCI\_OP\_LE\_CS\_READ\_REMOTE\_SUPPORTED\_CAPABILITIES BT\_OP(BT\_OGF\_LE, 0x008A) /\* 0x208A \*/

2463

[ 2464](structbt__hci__cp__le__read__remote__supported__capabilities.md)struct [bt\_hci\_cp\_le\_read\_remote\_supported\_capabilities](structbt__hci__cp__le__read__remote__supported__capabilities.md) {

[ 2465](structbt__hci__cp__le__read__remote__supported__capabilities.md#ac6f083563e2c72d37cf4e9e8fa695733) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__read__remote__supported__capabilities.md#ac6f083563e2c72d37cf4e9e8fa695733);

2466} \_\_packed;

2467

[ 2468](hci__types_8h.md#acdbbe0da013fb3b6da5514498c3932dd)#define BT\_HCI\_OP\_LE\_CS\_WRITE\_CACHED\_REMOTE\_SUPPORTED\_CAPABILITIES \

2469 BT\_OP(BT\_OGF\_LE, 0x008B) /\* 0x208B \*/

2470

[ 2471](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md)struct [bt\_hci\_cp\_le\_write\_cached\_remote\_supported\_capabilities](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md) {

[ 2472](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a8a884bca80550eb72a433f5ea280f702) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a8a884bca80550eb72a433f5ea280f702);

[ 2473](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a7a60c326707ebd60b96d25924e3c9e40) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_config\_supported](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a7a60c326707ebd60b96d25924e3c9e40);

[ 2474](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#afbfe48ddad696315d6e021a85d32559d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_consecutive\_procedures\_supported](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#afbfe48ddad696315d6e021a85d32559d);

[ 2475](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a96b0c7868da711271e74b82fcfd32fc2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_antennas\_supported](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a96b0c7868da711271e74b82fcfd32fc2);

[ 2476](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a96a49382bef8f3163cd82899f59ed5fe) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_antenna\_paths\_supported](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a96a49382bef8f3163cd82899f59ed5fe);

[ 2477](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#ae88cf07e3c8e6ad64a1beb60270d8961) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [roles\_supported](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#ae88cf07e3c8e6ad64a1beb60270d8961);

[ 2478](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a93f4973a1229273c51f6a20e741e42ed) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [modes\_supported](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a93f4973a1229273c51f6a20e741e42ed);

[ 2479](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a94fb0f963f706c303729d7a0088ef617) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rtt\_capability](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a94fb0f963f706c303729d7a0088ef617);

[ 2480](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#ae4b9b8ba0e83978f131541959062f691) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rtt\_aa\_only\_n](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#ae4b9b8ba0e83978f131541959062f691);

[ 2481](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a31c877363bd315786ef834215614d346) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rtt\_sounding\_n](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a31c877363bd315786ef834215614d346);

[ 2482](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a8f98235e9238a80602806fb60e1261bb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rtt\_random\_payload\_n](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a8f98235e9238a80602806fb60e1261bb);

[ 2483](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a29781bbe7e25c39b06047725f1d11426) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [nadm\_sounding\_capability](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a29781bbe7e25c39b06047725f1d11426);

[ 2484](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a25faaf2be6db05c44256b9f559841c87) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [nadm\_random\_capability](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a25faaf2be6db05c44256b9f559841c87);

[ 2485](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a908322e5c02500abbdd8891c5248998d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cs\_sync\_phys\_supported](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a908322e5c02500abbdd8891c5248998d);

[ 2486](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a2b5c828a30525eee5b1ce48f3ba98896) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [subfeatures\_supported](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a2b5c828a30525eee5b1ce48f3ba98896);

[ 2487](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a257b38d937c1111a66f6c28f1e221211) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [t\_ip1\_times\_supported](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a257b38d937c1111a66f6c28f1e221211);

[ 2488](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a0911e19deceb7f243ac706ddb4cf0a3a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [t\_ip2\_times\_supported](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a0911e19deceb7f243ac706ddb4cf0a3a);

[ 2489](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#af959f1539f5bbf74b0e63db743a132f4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [t\_fcs\_times\_supported](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#af959f1539f5bbf74b0e63db743a132f4);

[ 2490](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a870e068fcc15dd44dca3ac24334000ee) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [t\_pm\_times\_supported](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a870e068fcc15dd44dca3ac24334000ee);

[ 2491](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#ab77f7bda7302cad94805e8ea43b8bf14) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [t\_sw\_time\_supported](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#ab77f7bda7302cad94805e8ea43b8bf14);

[ 2492](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#aa9e48c6f0d22e9a64e8591a34409988e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_snr\_capability](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#aa9e48c6f0d22e9a64e8591a34409988e);

2493} \_\_packed;

2494

[ 2495](hci__types_8h.md#a574168efdaa5729aec9699d48f988d77)#define BT\_HCI\_OP\_LE\_CS\_SECURITY\_ENABLE BT\_OP(BT\_OGF\_LE, 0x008C) /\* 0x208C \*/

2496

[ 2497](structbt__hci__cp__le__security__enable.md)struct [bt\_hci\_cp\_le\_security\_enable](structbt__hci__cp__le__security__enable.md) {

[ 2498](structbt__hci__cp__le__security__enable.md#a772d3744d43f0447187040f2c6f0ac6e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__security__enable.md#a772d3744d43f0447187040f2c6f0ac6e);

2499} \_\_packed;

2500

[ 2501](hci__types_8h.md#addb1ab37dc75ab5389d74c6c96629b02)#define BT\_HCI\_OP\_LE\_CS\_SET\_DEFAULT\_SETTINGS BT\_OP(BT\_OGF\_LE, 0x008D) /\* 0x208D \*/

2502

[ 2503](hci__types_8h.md#a74aaa5b6b799dad3af6778e23093b230)#define BT\_HCI\_OP\_LE\_CS\_INITIATOR\_ROLE\_MASK BIT(0)

[ 2504](hci__types_8h.md#a1beb2f602b3635fee272580f0f2f8719)#define BT\_HCI\_OP\_LE\_CS\_REFLECTOR\_ROLE\_MASK BIT(1)

2505

[ 2506](hci__types_8h.md#a040315a8ac4f80a2c497919a2fd4d7bc)#define BT\_HCI\_OP\_LE\_CS\_MIN\_MAX\_TX\_POWER -127

[ 2507](hci__types_8h.md#a29a240b2d3f209b1f5f3d96e380dde08)#define BT\_HCI\_OP\_LE\_CS\_MAX\_MAX\_TX\_POWER 20

2508

[ 2509](hci__types_8h.md#a7fa26323384443ba9c5e635047b74f51)#define BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_ONE 0x01

[ 2510](hci__types_8h.md#aa6d146c85e3148a2afb66023d94c2eeb)#define BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_TWO 0x02

[ 2511](hci__types_8h.md#a8721a8f4670a8038d66d42adea061f57)#define BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_THREE 0x03

[ 2512](hci__types_8h.md#af0d407f944831f8c85f91fb60f5bc618)#define BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_FOUR 0x04

[ 2513](hci__types_8h.md#afad5b26b2a6ce125b6198856d20bcdd8)#define BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_REP 0xFE

[ 2514](hci__types_8h.md#aed2444a40bc79ccf3f383dd961036f5e)#define BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_NONE 0xFF

2515

[ 2516](structbt__hci__cp__le__cs__set__default__settings.md)struct [bt\_hci\_cp\_le\_cs\_set\_default\_settings](structbt__hci__cp__le__cs__set__default__settings.md) {

[ 2517](structbt__hci__cp__le__cs__set__default__settings.md#a096c3238ccc6624bae89d5a45dd95600) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__cs__set__default__settings.md#a096c3238ccc6624bae89d5a45dd95600);

[ 2518](structbt__hci__cp__le__cs__set__default__settings.md#a04aea510e26136f874ccfbabbbd080bb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [role\_enable](structbt__hci__cp__le__cs__set__default__settings.md#a04aea510e26136f874ccfbabbbd080bb);

[ 2519](structbt__hci__cp__le__cs__set__default__settings.md#aa001c88ab42250c2cfd604af11e0ae27) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cs\_sync\_antenna\_selection](structbt__hci__cp__le__cs__set__default__settings.md#aa001c88ab42250c2cfd604af11e0ae27);

[ 2520](structbt__hci__cp__le__cs__set__default__settings.md#a333341ec01554ab90fc5e340dbfb5130) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [max\_tx\_power](structbt__hci__cp__le__cs__set__default__settings.md#a333341ec01554ab90fc5e340dbfb5130);

2521} \_\_packed;

2522

[ 2523](hci__types_8h.md#afa7a0214b145891562f1d2b7b16860ab)#define BT\_HCI\_OP\_LE\_CS\_READ\_REMOTE\_FAE\_TABLE BT\_OP(BT\_OGF\_LE, 0x008E) /\* 0x208E \*/

2524

[ 2525](structbt__hci__cp__le__read__remote__fae__table.md)struct [bt\_hci\_cp\_le\_read\_remote\_fae\_table](structbt__hci__cp__le__read__remote__fae__table.md) {

[ 2526](structbt__hci__cp__le__read__remote__fae__table.md#a10bdfc4808586f7cccf025c63a6e28a5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__read__remote__fae__table.md#a10bdfc4808586f7cccf025c63a6e28a5);

2527} \_\_packed;

2528

[ 2529](hci__types_8h.md#a44eb5d70628f6522a08b1327588df979)#define BT\_HCI\_OP\_LE\_CS\_WRITE\_CACHED\_REMOTE\_FAE\_TABLE BT\_OP(BT\_OGF\_LE, 0x008F) /\* 0x208F \*/

2530

[ 2531](structbt__hci__cp__le__write__cached__remote__fae__table.md)struct [bt\_hci\_cp\_le\_write\_cached\_remote\_fae\_table](structbt__hci__cp__le__write__cached__remote__fae__table.md) {

[ 2532](structbt__hci__cp__le__write__cached__remote__fae__table.md#a330531f1809cddea8f1527f3b0a92e31) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__write__cached__remote__fae__table.md#a330531f1809cddea8f1527f3b0a92e31);

[ 2533](structbt__hci__cp__le__write__cached__remote__fae__table.md#a8594dd89888d1388f2a45a33e12e94d0) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [remote\_fae\_table](structbt__hci__cp__le__write__cached__remote__fae__table.md#a8594dd89888d1388f2a45a33e12e94d0)[72];

2534} \_\_packed;

2535

[ 2536](hci__types_8h.md#a880439089735247c7011862d5b3e090f)#define BT\_HCI\_OP\_LE\_CS\_SET\_CHANNEL\_CLASSIFICATION BT\_OP(BT\_OGF\_LE, 0x0092) /\* 0x2092 \*/

2537

[ 2538](hci__types_8h.md#ad74850cecd8d8dd8a7878d944abdb411)#define BT\_HCI\_OP\_LE\_CS\_SET\_PROCEDURE\_PARAMETERS BT\_OP(BT\_OGF\_LE, 0x0093) /\* 0x2093 \*/

2539

[ 2540](hci__types_8h.md#a3a8f1c94f40696f18e18810f736497e3)#define BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_1M 0x01

[ 2541](hci__types_8h.md#a016f68a621de8d332f3073df4faf1702)#define BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_2M 0x02

[ 2542](hci__types_8h.md#a2543f9fa20db642fb8b47b949c50af6a)#define BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_CODED\_S8 0x03

[ 2543](hci__types_8h.md#a776a14d8e7fdca584475f26b441c8bfb)#define BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_CODED\_S2 0x04

2544

[ 2545](structbt__hci__cp__le__set__procedure__parameters.md)struct [bt\_hci\_cp\_le\_set\_procedure\_parameters](structbt__hci__cp__le__set__procedure__parameters.md) {

[ 2546](structbt__hci__cp__le__set__procedure__parameters.md#ab8a15269255fb7d960ae712a844b9f35) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__set__procedure__parameters.md#ab8a15269255fb7d960ae712a844b9f35);

[ 2547](structbt__hci__cp__le__set__procedure__parameters.md#a7d2f5d9242df436906b005e66c7bb75d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [config\_id](structbt__hci__cp__le__set__procedure__parameters.md#a7d2f5d9242df436906b005e66c7bb75d);

[ 2548](structbt__hci__cp__le__set__procedure__parameters.md#a5de9205fdf1b6e342f53a12aa82c10c5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_procedure\_len](structbt__hci__cp__le__set__procedure__parameters.md#a5de9205fdf1b6e342f53a12aa82c10c5);

[ 2549](structbt__hci__cp__le__set__procedure__parameters.md#a22ecbaff0fd48a0716a15d265adc590e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [min\_procedure\_interval](structbt__hci__cp__le__set__procedure__parameters.md#a22ecbaff0fd48a0716a15d265adc590e);

[ 2550](structbt__hci__cp__le__set__procedure__parameters.md#ad46165bc5f6d875940ee53a8b98cb5b4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_procedure\_interval](structbt__hci__cp__le__set__procedure__parameters.md#ad46165bc5f6d875940ee53a8b98cb5b4);

[ 2551](structbt__hci__cp__le__set__procedure__parameters.md#ac6bb66fa24aec17a964f27365ca65ec9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_procedure\_count](structbt__hci__cp__le__set__procedure__parameters.md#ac6bb66fa24aec17a964f27365ca65ec9);

[ 2552](structbt__hci__cp__le__set__procedure__parameters.md#a51fb8c789cefce09d5da2b86d5c862ce) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [min\_subevent\_len](structbt__hci__cp__le__set__procedure__parameters.md#a51fb8c789cefce09d5da2b86d5c862ce)[3];

[ 2553](structbt__hci__cp__le__set__procedure__parameters.md#aa9ec99aff85de173ccb2d3f144c85319) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_subevent\_len](structbt__hci__cp__le__set__procedure__parameters.md#aa9ec99aff85de173ccb2d3f144c85319)[3];

[ 2554](structbt__hci__cp__le__set__procedure__parameters.md#aa783e0e63c38ceee503c0b73ac873ca7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tone\_antenna\_config\_selection](structbt__hci__cp__le__set__procedure__parameters.md#aa783e0e63c38ceee503c0b73ac873ca7);

[ 2555](structbt__hci__cp__le__set__procedure__parameters.md#afcd4e8b390fd996ee134043ec2930fe8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__cp__le__set__procedure__parameters.md#afcd4e8b390fd996ee134043ec2930fe8);

[ 2556](structbt__hci__cp__le__set__procedure__parameters.md#ade09ca9d42b0db682cf677d9ac4326d2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_power\_delta](structbt__hci__cp__le__set__procedure__parameters.md#ade09ca9d42b0db682cf677d9ac4326d2);

[ 2557](structbt__hci__cp__le__set__procedure__parameters.md#a7a61ff539f68a02ea7aa466f182dc5ab) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [preferred\_peer\_antenna](structbt__hci__cp__le__set__procedure__parameters.md#a7a61ff539f68a02ea7aa466f182dc5ab);

[ 2558](structbt__hci__cp__le__set__procedure__parameters.md#a8524fd01e35094d2b78488c0a2876832) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [snr\_control\_initiator](structbt__hci__cp__le__set__procedure__parameters.md#a8524fd01e35094d2b78488c0a2876832);

[ 2559](structbt__hci__cp__le__set__procedure__parameters.md#aa5a6a677b6e0d57658041e891535d74b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [snr\_control\_reflector](structbt__hci__cp__le__set__procedure__parameters.md#aa5a6a677b6e0d57658041e891535d74b);

2560} \_\_packed;

2561

[ 2562](hci__types_8h.md#a4eddce6558339caba6a3d16f8fe5d485)#define BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_ENABLE BT\_OP(BT\_OGF\_LE, 0x0094) /\* 0x2094 \*/

2563

[ 2564](hci__types_8h.md#a3e01bbe3a72c946015a288ee49d3cbdd)#define BT\_HCI\_OP\_LE\_CS\_PROCEDURES\_DISABLED 0x00

[ 2565](hci__types_8h.md#a4a88120ae7e83fd791012c913315d14f)#define BT\_HCI\_OP\_LE\_CS\_PROCEDURES\_ENABLED 0x01

2566

[ 2567](structbt__hci__cp__le__procedure__enable.md)struct [bt\_hci\_cp\_le\_procedure\_enable](structbt__hci__cp__le__procedure__enable.md) {

[ 2568](structbt__hci__cp__le__procedure__enable.md#af94d81f71c2fe587c848e34a430825bf) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__procedure__enable.md#af94d81f71c2fe587c848e34a430825bf);

[ 2569](structbt__hci__cp__le__procedure__enable.md#ae1dc5c808bed301ddee6e9dd624c00a5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [config\_id](structbt__hci__cp__le__procedure__enable.md#ae1dc5c808bed301ddee6e9dd624c00a5);

[ 2570](structbt__hci__cp__le__procedure__enable.md#a3a203b453bd913db8bec91be9310003a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enable](structbt__hci__cp__le__procedure__enable.md#a3a203b453bd913db8bec91be9310003a);

2571} \_\_packed;

2572

[ 2573](hci__types_8h.md#af09601cffd1adf3f8b623868d8f8a3e9)#define BT\_HCI\_OP\_LE\_CS\_TEST BT\_OP(BT\_OGF\_LE, 0x0095) /\* 0x2095 \*/

2574

[ 2575](hci__types_8h.md#af1b7924e50ba017e59d697fd8814d491)#define BT\_HCI\_OP\_LE\_CS\_MAIN\_MODE\_1 0x1

[ 2576](hci__types_8h.md#a714152a085bbc317b539d6e973ccffc6)#define BT\_HCI\_OP\_LE\_CS\_MAIN\_MODE\_2 0x2

[ 2577](hci__types_8h.md#a5d2af0ed5e0cc5cf7d9f0baae512ff68)#define BT\_HCI\_OP\_LE\_CS\_MAIN\_MODE\_3 0x3

2578

[ 2579](hci__types_8h.md#a219243d501bbcb6d62668398cde79fca)#define BT\_HCI\_OP\_LE\_CS\_SUB\_MODE\_1 0x1

[ 2580](hci__types_8h.md#ada09c787fca0a1d54bb754635489b51e)#define BT\_HCI\_OP\_LE\_CS\_SUB\_MODE\_2 0x2

[ 2581](hci__types_8h.md#a4b48c199b6b75e9dd62ec36883b40aa4)#define BT\_HCI\_OP\_LE\_CS\_SUB\_MODE\_3 0x3

[ 2582](hci__types_8h.md#ab3fce1eb448b0ade581e4e12b2d56039)#define BT\_HCI\_OP\_LE\_CS\_SUB\_MODE\_UNUSED 0xFF

2583

[ 2584](hci__types_8h.md#a4505bedc3b5aae63b80cf53fc516b342)#define BT\_HCI\_OP\_LE\_CS\_INITIATOR\_ROLE 0x0

[ 2585](hci__types_8h.md#aeb3715dfcac55a46532f51279e29708c)#define BT\_HCI\_OP\_LE\_CS\_REFLECTOR\_ROLE 0x1

2586

[ 2587](hci__types_8h.md#a759eb7a8e43ee7cf1ea88ddd3e69feb5)#define BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_AA\_ONLY 0x0

[ 2588](hci__types_8h.md#aa2ae18252a20ef3481d2402f8924cdda)#define BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_32BIT\_SOUND 0x1

[ 2589](hci__types_8h.md#a73cbfe2a942b684ac0b5b50d900fb83f)#define BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_96BIT\_SOUND 0x2

[ 2590](hci__types_8h.md#abe4efee7cf9371129f4b5bd650b0d64a)#define BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_32BIT\_RAND 0x3

[ 2591](hci__types_8h.md#a77e56fd5302673f6ef295c0cceabdc9f)#define BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_64BIT\_RAND 0x4

[ 2592](hci__types_8h.md#aa60f64ff7259fd79fb1da2c063530348)#define BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_96BIT\_RAND 0x5

[ 2593](hci__types_8h.md#a1fe5e94fbd1156c8196c8e1ab9816bac)#define BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_128BIT\_RAND 0x6

2594

[ 2595](hci__types_8h.md#a7baf90f5bf691ce6b650677e6c2a9600)#define BT\_HCI\_OP\_LE\_CS\_CS\_SYNC\_1M 0x1

[ 2596](hci__types_8h.md#ae49d35db87532e06ea685a63eb89177a)#define BT\_HCI\_OP\_LE\_CS\_CS\_SYNC\_2M 0x2

[ 2597](hci__types_8h.md#ac34716156b071e06eb454f091a63216c)#define BT\_HCI\_OP\_LE\_CS\_CS\_SYNC\_2M\_2BT 0x3

2598

[ 2599](hci__types_8h.md#a500597c78a6ada65d1224960bf6a370f)#define BT\_HCI\_OP\_LE\_CS\_TEST\_MINIMIZE\_TX\_POWER 0x7E

[ 2600](hci__types_8h.md#a50eb827977c0c596cb357ed62a6e80bd)#define BT\_HCI\_OP\_LE\_CS\_TEST\_MAXIMIZE\_TX\_POWER 0x7F

2601

[ 2602](hci__types_8h.md#a92e1ec21014999f40172fa1812c36575)#define BT\_HCI\_OP\_LE\_CS\_ACI\_0 0x0

[ 2603](hci__types_8h.md#a5b082fa5b8ba11a651468cc516d067fe)#define BT\_HCI\_OP\_LE\_CS\_ACI\_1 0x1

[ 2604](hci__types_8h.md#ab30a4e55002080394c39fb885eba36e4)#define BT\_HCI\_OP\_LE\_CS\_ACI\_2 0x2

[ 2605](hci__types_8h.md#a76d1452003c0bd3b688765aa2d25047f)#define BT\_HCI\_OP\_LE\_CS\_ACI\_3 0x3

[ 2606](hci__types_8h.md#af16c4c79e602e6da833b8aa3e0c4bf64)#define BT\_HCI\_OP\_LE\_CS\_ACI\_4 0x4

[ 2607](hci__types_8h.md#ad980d8f134d940b80dc9b0e3a570ac06)#define BT\_HCI\_OP\_LE\_CS\_ACI\_5 0x5

[ 2608](hci__types_8h.md#a4c7ff3c949023f4544bf50353a0f082b)#define BT\_HCI\_OP\_LE\_CS\_ACI\_6 0x6

[ 2609](hci__types_8h.md#acabccf9f5893324dcb6acc0769ab8417)#define BT\_HCI\_OP\_LE\_CS\_ACI\_7 0x7

2610

[ 2611](hci__types_8h.md#a96b13fb3b363a5436e1b9633f54bb248)#define BT\_HCI\_OP\_LE\_CS\_SNR\_18 0x0

[ 2612](hci__types_8h.md#a4b93a8bceafd49d6ca65816924bb4230)#define BT\_HCI\_OP\_LE\_CS\_SNR\_21 0x1

[ 2613](hci__types_8h.md#a135a4dc2f191d2a931b4270e00774cb2)#define BT\_HCI\_OP\_LE\_CS\_SNR\_24 0x2

[ 2614](hci__types_8h.md#a52eb27d8f726a2ed6859149fcdf2355d)#define BT\_HCI\_OP\_LE\_CS\_SNR\_27 0x3

[ 2615](hci__types_8h.md#a181c2d98b93bd18e9edc11a6f9535331)#define BT\_HCI\_OP\_LE\_CS\_SNR\_30 0x4

[ 2616](hci__types_8h.md#a4aa2e02ce5110be3dc68a801bb583372)#define BT\_HCI\_OP\_LE\_CS\_SNR\_NOT\_USED 0xFF

2617

[ 2618](hci__types_8h.md#a0a73e0d46b5ca0e94b4bb00d2f79e89d)#define BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_0\_MASK BIT(0)

[ 2619](hci__types_8h.md#a2a62cbc191abd177cbf5aea27112fb8b)#define BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_2\_MASK BIT(2)

[ 2620](hci__types_8h.md#a560f6f1bddedc60b3a373778bc56b1a7)#define BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_3\_MASK BIT(3)

[ 2621](hci__types_8h.md#a36c2c6debe6bf395853112c68a726d25)#define BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_4\_MASK BIT(4)

[ 2622](hci__types_8h.md#a4aca98e213ba81c999c8495310af9320)#define BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_5\_MASK BIT(5)

[ 2623](hci__types_8h.md#afd7b8b4ec0baf526cc4335d26c380b62)#define BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_6\_MASK BIT(6)

[ 2624](hci__types_8h.md#a695d2ba272dbdd2681ab9216d00ca43a)#define BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_7\_MASK BIT(7)

[ 2625](hci__types_8h.md#ad92a29871be9aff39802fdea4446ef4b)#define BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_8\_MASK BIT(8)

[ 2626](hci__types_8h.md#a90c77fe0022f016453a8eb174b8fcd63)#define BT\_HCI\_OP\_LE\_CS\_TEST\_OVERRIDE\_CONFIG\_10\_MASK BIT(10)

2627

[ 2628](hci__types_8h.md#a77d27762b9faa7743a55d822a1839eac)#define BT\_HCI\_OP\_LE\_CS\_TEST\_CHSEL\_TYPE\_3B 0x0

[ 2629](hci__types_8h.md#af17f867204bc7cf99e5d530c39302be0)#define BT\_HCI\_OP\_LE\_CS\_TEST\_CHSEL\_TYPE\_3C 0x1

2630

[ 2631](hci__types_8h.md#acd33fc2eb3f5ebe10cbe4c5060f8336b)#define BT\_HCI\_OP\_LE\_CS\_TEST\_CH3C\_SHAPE\_HAT 0x0

[ 2632](hci__types_8h.md#ad09c735ab352d7a546cade296e915e85)#define BT\_HCI\_OP\_LE\_CS\_TEST\_CH3C\_SHAPE\_X 0x1

2633

[ 2634](hci__types_8h.md#a9ed8967faa3ee3824433422709148330)#define BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_NONE 0x0

[ 2635](hci__types_8h.md#a0513bf5ca6eb9f43a7e8cecaf943c4d7)#define BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_INIT 0x1

[ 2636](hci__types_8h.md#aa24ae1cf1501de66660051a4a62246df)#define BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_REFL 0x2

[ 2637](hci__types_8h.md#ad7a89a9365e20e4cd1e44bdb74ae7ecb)#define BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_BOTH 0x3

[ 2638](hci__types_8h.md#a50fba6ab75b37ccf39452211ba05e896)#define BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_REPEAT 0x4

2639

[ 2640](hci__types_8h.md#aa4ba4be270035da446389766b795c327)#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_00 0x0

[ 2641](hci__types_8h.md#aa0e9e2081d3cbbb60de9b6dcffe77239)#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_01 0x1

[ 2642](hci__types_8h.md#a762c5efa09e1fba989fdfb0bdcba9b9c)#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_02 0x2

[ 2643](hci__types_8h.md#a2cc7a5d5d2105b1a428703e274cc5388)#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_03 0x3

[ 2644](hci__types_8h.md#a03ffb0ffb8e98b26390575b153471bab)#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_04 0x4

[ 2645](hci__types_8h.md#adbd3820e0ffa5f99e27778217d477010)#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_05 0x5

[ 2646](hci__types_8h.md#a70607449d6bd6207783e319e77d63b16)#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_06 0x6

[ 2647](hci__types_8h.md#acc79a879ea527c2901a8b91dae58d0ed)#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_07 0x7

[ 2648](hci__types_8h.md#a9dfd88863d649182855edc8c268107d6)#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_08 0x8

[ 2649](hci__types_8h.md#ae5a27304aa1cefdfb26ae2cbf42532e3)#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_09 0x9

[ 2650](hci__types_8h.md#a0e9664c52808aa246218f92a4fb55516)#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_10 0xA

[ 2651](hci__types_8h.md#a8fbc80d91e4a1ae04c76cda189cd5d83)#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_11 0xB

[ 2652](hci__types_8h.md#a4c4a44bd33ebf97852e6640b0d510fdd)#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_12 0xC

[ 2653](hci__types_8h.md#a08690b2f762d24c34966b839a6d5e696)#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_13 0xD

[ 2654](hci__types_8h.md#ac2cd3ed1583f86af0480b8481cedca1e)#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_14 0xE

[ 2655](hci__types_8h.md#ab2b0745d98053775e9bf073e36ce5d78)#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_15 0xF

[ 2656](hci__types_8h.md#add2c42aa2583b93b0f98ac33ca61ca9d)#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_16 0x10

[ 2657](hci__types_8h.md#a08db476ea6516691baeb9007b553281d)#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_17 0x11

[ 2658](hci__types_8h.md#a9f0bf05cb0aac50e1df43397c3b913bc)#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_18 0x12

[ 2659](hci__types_8h.md#a5df817bdfefc4de0a1309cf71908a105)#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_19 0x13

[ 2660](hci__types_8h.md#ae64e5a409523b94ef1ce315ed49afed0)#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_20 0x14

[ 2661](hci__types_8h.md#a46f70b5096593956795cc381e33c4aa2)#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_21 0x15

[ 2662](hci__types_8h.md#abe9fa4621e9c004421170b0166ea14e1)#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_22 0x16

[ 2663](hci__types_8h.md#afc41ca64d03a7ed8ea82a641a0217436)#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_23 0x17

[ 2664](hci__types_8h.md#ac9d7cb5a339759b7e0c4ed150a487ca3)#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_LOOP 0xFF

2665

[ 2666](hci__types_8h.md#a1f2bfc1afab1928321c01beddb658f01)#define BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_2\_POSITION\_NOT\_PRESENT 0xFF

2667

[ 2668](hci__types_8h.md#a45e1ff56f1a6dcc59b784905e4fc6726)#define BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_VAL\_0011 0x0

[ 2669](hci__types_8h.md#a5d3c206a5067ddc5a02a5d5e8c3eb7a3)#define BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_VAL\_1100 0x1

[ 2670](hci__types_8h.md#a24d2e56f620500905572e786f2523b0e)#define BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_VAL\_LOOP 0x2

2671

[ 2672](hci__types_8h.md#a4f922c5e0662adf8471686dfa9b719ec)#define BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_PRBS9 0x00

[ 2673](hci__types_8h.md#af20dfb1e245afc06a495179d700f126f)#define BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_11110000 0x01

[ 2674](hci__types_8h.md#ae133ef2939518d660df5322551157d47)#define BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_10101010 0x02

[ 2675](hci__types_8h.md#a92bc70a5ad7938a46ac9f2127f1bc2d9)#define BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_PRBS15 0x03

[ 2676](hci__types_8h.md#aa94eda86c6ffe85a65267f285dae5cb1)#define BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_11111111 0x04

[ 2677](hci__types_8h.md#a04a26b8600cac8c82247a7d51122f600)#define BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_00000000 0x05

[ 2678](hci__types_8h.md#abf19d511680005828add231d64e1e3f0)#define BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_00001111 0x06

[ 2679](hci__types_8h.md#a53f0ca5604489a38a1367736a5297b45)#define BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_01010101 0x07

[ 2680](hci__types_8h.md#a94007d8250c3524ad0b86745dbb74b3b)#define BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_USER 0x80

2681

[ 2682](structbt__hci__op__le__cs__test.md)struct [bt\_hci\_op\_le\_cs\_test](structbt__hci__op__le__cs__test.md) {

[ 2683](structbt__hci__op__le__cs__test.md#af4cdfd8c8cab500277c06a82ac088577) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [main\_mode\_type](structbt__hci__op__le__cs__test.md#af4cdfd8c8cab500277c06a82ac088577);

[ 2684](structbt__hci__op__le__cs__test.md#a090c5d03cf829011196d644cd9f7c7db) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sub\_mode\_type](structbt__hci__op__le__cs__test.md#a090c5d03cf829011196d644cd9f7c7db);

[ 2685](structbt__hci__op__le__cs__test.md#a60cc9a7c46f8cd0933dc2f5a68cca627) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [main\_mode\_repetition](structbt__hci__op__le__cs__test.md#a60cc9a7c46f8cd0933dc2f5a68cca627);

[ 2686](structbt__hci__op__le__cs__test.md#aaf480890608b5cfc9151dac844e9a337) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mode\_0\_steps](structbt__hci__op__le__cs__test.md#aaf480890608b5cfc9151dac844e9a337);

[ 2687](structbt__hci__op__le__cs__test.md#afa0310f818002d7c1ac048f0db8c7f1c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [role](structbt__hci__op__le__cs__test.md#afa0310f818002d7c1ac048f0db8c7f1c);

[ 2688](structbt__hci__op__le__cs__test.md#ae0234031d94e93653dd45e6e657c199f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rtt\_type](structbt__hci__op__le__cs__test.md#ae0234031d94e93653dd45e6e657c199f);

[ 2689](structbt__hci__op__le__cs__test.md#af42701651bca5fe0353ae1de9c453f47) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cs\_sync\_phy](structbt__hci__op__le__cs__test.md#af42701651bca5fe0353ae1de9c453f47);

[ 2690](structbt__hci__op__le__cs__test.md#aef335dd7738634cb8f81c18e0350141e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cs\_sync\_antenna\_selection](structbt__hci__op__le__cs__test.md#aef335dd7738634cb8f81c18e0350141e);

[ 2691](structbt__hci__op__le__cs__test.md#a8ad67a5a0138f32cc5295074011a3808) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent\_len](structbt__hci__op__le__cs__test.md#a8ad67a5a0138f32cc5295074011a3808)[3];

[ 2692](structbt__hci__op__le__cs__test.md#ad52cd2862d2544448a5e175c58541f89) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [subevent\_interval](structbt__hci__op__le__cs__test.md#ad52cd2862d2544448a5e175c58541f89);

[ 2693](structbt__hci__op__le__cs__test.md#a1c105f7a4d48754322fee6992db8c175) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_num\_subevents](structbt__hci__op__le__cs__test.md#a1c105f7a4d48754322fee6992db8c175);

[ 2694](structbt__hci__op__le__cs__test.md#adf2f24dc6988f1f0e0457a6cf3141521) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [transmit\_power\_level](structbt__hci__op__le__cs__test.md#adf2f24dc6988f1f0e0457a6cf3141521);

[ 2695](structbt__hci__op__le__cs__test.md#a0675dfbb050838d98f21cfa28af8615b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [t\_ip1\_time](structbt__hci__op__le__cs__test.md#a0675dfbb050838d98f21cfa28af8615b);

[ 2696](structbt__hci__op__le__cs__test.md#a7538e91b5ced2702965a21f8e754ebcc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [t\_ip2\_time](structbt__hci__op__le__cs__test.md#a7538e91b5ced2702965a21f8e754ebcc);

[ 2697](structbt__hci__op__le__cs__test.md#aa3d510663e5dcc44b5acd9d1c41746d5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [t\_fcs\_time](structbt__hci__op__le__cs__test.md#aa3d510663e5dcc44b5acd9d1c41746d5);

[ 2698](structbt__hci__op__le__cs__test.md#a981da50e0594b8bc05f811e5170b10f5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [t\_pm\_time](structbt__hci__op__le__cs__test.md#a981da50e0594b8bc05f811e5170b10f5);

[ 2699](structbt__hci__op__le__cs__test.md#a09c40ecd0d4e325e0c0504a9d8cd977b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [t\_sw\_time](structbt__hci__op__le__cs__test.md#a09c40ecd0d4e325e0c0504a9d8cd977b);

[ 2700](structbt__hci__op__le__cs__test.md#acaa428a37e68ff56c311397e53f46526) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tone\_antenna\_config\_selection](structbt__hci__op__le__cs__test.md#acaa428a37e68ff56c311397e53f46526);

[ 2701](structbt__hci__op__le__cs__test.md#a9021c55f8cddb741fb1f86317625723e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reserved](structbt__hci__op__le__cs__test.md#a9021c55f8cddb741fb1f86317625723e);

[ 2702](structbt__hci__op__le__cs__test.md#a551c06e651180867dd1d23b3fdf4c031) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [snr\_control\_initiator](structbt__hci__op__le__cs__test.md#a551c06e651180867dd1d23b3fdf4c031);

[ 2703](structbt__hci__op__le__cs__test.md#a3c949d9a7eb4f56427f6e9f8be7cb77b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [snr\_control\_reflector](structbt__hci__op__le__cs__test.md#a3c949d9a7eb4f56427f6e9f8be7cb77b);

[ 2704](structbt__hci__op__le__cs__test.md#aee8c125df0f7136a0ecdb9f04903aaef) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [drbg\_nonce](structbt__hci__op__le__cs__test.md#aee8c125df0f7136a0ecdb9f04903aaef);

[ 2705](structbt__hci__op__le__cs__test.md#a8c23c2e6e8c38bf33fcd6d1e343f5982) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel\_map\_repetition](structbt__hci__op__le__cs__test.md#a8c23c2e6e8c38bf33fcd6d1e343f5982);

[ 2706](structbt__hci__op__le__cs__test.md#acc2d0768b69e5f5b593e5aff71b17f20) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [override\_config](structbt__hci__op__le__cs__test.md#acc2d0768b69e5f5b593e5aff71b17f20);

[ 2707](structbt__hci__op__le__cs__test.md#a373372a93d94e70d674c1c7b4c126734) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [override\_parameters\_length](structbt__hci__op__le__cs__test.md#a373372a93d94e70d674c1c7b4c126734);

[ 2708](structbt__hci__op__le__cs__test.md#a15a68fe7c98b2e242afd6eb67dd9b40a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [override\_parameters\_data](structbt__hci__op__le__cs__test.md#a15a68fe7c98b2e242afd6eb67dd9b40a)[];

2709} \_\_packed;

2710

[ 2711](hci__types_8h.md#af26aad0e137782c8f12937b1736d6ada)#define BT\_HCI\_OP\_LE\_CS\_CREATE\_CONFIG BT\_OP(BT\_OGF\_LE, 0x0090) /\* 0x2090 \*/

2712

[ 2713](structbt__hci__cp__le__cs__create__config.md)struct [bt\_hci\_cp\_le\_cs\_create\_config](structbt__hci__cp__le__cs__create__config.md) {

[ 2714](structbt__hci__cp__le__cs__create__config.md#a3742081b071b992176b725448cc6ab29) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__cs__create__config.md#a3742081b071b992176b725448cc6ab29);

[ 2715](structbt__hci__cp__le__cs__create__config.md#ae833b5f02f878f54dca1a25753eca1f3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [config\_id](structbt__hci__cp__le__cs__create__config.md#ae833b5f02f878f54dca1a25753eca1f3);

[ 2716](structbt__hci__cp__le__cs__create__config.md#a9dc7a6b577c33583b7ca7548e2b555ac) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [create\_context](structbt__hci__cp__le__cs__create__config.md#a9dc7a6b577c33583b7ca7548e2b555ac);

[ 2717](structbt__hci__cp__le__cs__create__config.md#a74c5fdfbc97b112c35ee318aa2b9b463) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [main\_mode\_type](structbt__hci__cp__le__cs__create__config.md#a74c5fdfbc97b112c35ee318aa2b9b463);

[ 2718](structbt__hci__cp__le__cs__create__config.md#a34fa54e8bbd641bb0901b0b057134ffb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sub\_mode\_type](structbt__hci__cp__le__cs__create__config.md#a34fa54e8bbd641bb0901b0b057134ffb);

[ 2719](structbt__hci__cp__le__cs__create__config.md#aeb26115c8b500829ef6bc238aa3a495f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [min\_main\_mode\_steps](structbt__hci__cp__le__cs__create__config.md#aeb26115c8b500829ef6bc238aa3a495f);

[ 2720](structbt__hci__cp__le__cs__create__config.md#aa13e091f99114bb5217489757c1522bd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_main\_mode\_steps](structbt__hci__cp__le__cs__create__config.md#aa13e091f99114bb5217489757c1522bd);

[ 2721](structbt__hci__cp__le__cs__create__config.md#acd11430a6c94b0f0c34e2788a2326a40) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [main\_mode\_repetition](structbt__hci__cp__le__cs__create__config.md#acd11430a6c94b0f0c34e2788a2326a40);

[ 2722](structbt__hci__cp__le__cs__create__config.md#a909e409d55ac539a119e932899a97204) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mode\_0\_steps](structbt__hci__cp__le__cs__create__config.md#a909e409d55ac539a119e932899a97204);

[ 2723](structbt__hci__cp__le__cs__create__config.md#a5a17d6c72daaefcb55fdfa24194cc886) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [role](structbt__hci__cp__le__cs__create__config.md#a5a17d6c72daaefcb55fdfa24194cc886);

[ 2724](structbt__hci__cp__le__cs__create__config.md#a709938176023c5482c91af8995001782) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rtt\_type](structbt__hci__cp__le__cs__create__config.md#a709938176023c5482c91af8995001782);

[ 2725](structbt__hci__cp__le__cs__create__config.md#ac6c9c568918c9ef9aa4f2038a4922020) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cs\_sync\_phy](structbt__hci__cp__le__cs__create__config.md#ac6c9c568918c9ef9aa4f2038a4922020);

[ 2726](structbt__hci__cp__le__cs__create__config.md#abab4907ec883430044bb9f9d6cf9f25d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel\_map](structbt__hci__cp__le__cs__create__config.md#abab4907ec883430044bb9f9d6cf9f25d)[10];

[ 2727](structbt__hci__cp__le__cs__create__config.md#a8182f4becdef488b84f12fe7e4274193) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel\_map\_repetition](structbt__hci__cp__le__cs__create__config.md#a8182f4becdef488b84f12fe7e4274193);

[ 2728](structbt__hci__cp__le__cs__create__config.md#a2c8be699bfd8eaaababd6d0de0b13e18) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel\_selection\_type](structbt__hci__cp__le__cs__create__config.md#a2c8be699bfd8eaaababd6d0de0b13e18);

[ 2729](structbt__hci__cp__le__cs__create__config.md#addaa3592a97bda96a4aba17e809e4018) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ch3c\_shape](structbt__hci__cp__le__cs__create__config.md#addaa3592a97bda96a4aba17e809e4018);

[ 2730](structbt__hci__cp__le__cs__create__config.md#a0223c41abc034d515421fad8c3123387) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ch3c\_jump](structbt__hci__cp__le__cs__create__config.md#a0223c41abc034d515421fad8c3123387);

[ 2731](structbt__hci__cp__le__cs__create__config.md#a40b42ed708733aa7d55879ef7228699e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reserved](structbt__hci__cp__le__cs__create__config.md#a40b42ed708733aa7d55879ef7228699e);

2732} \_\_packed;

2733

[ 2734](hci__types_8h.md#a54116ddaa8338d59b23fb879c185a399)#define BT\_HCI\_OP\_LE\_CS\_REMOVE\_CONFIG BT\_OP(BT\_OGF\_LE, 0x0091) /\* 0x2091 \*/

2735

[ 2736](structbt__hci__cp__le__cs__remove__config.md)struct [bt\_hci\_cp\_le\_cs\_remove\_config](structbt__hci__cp__le__cs__remove__config.md) {

[ 2737](structbt__hci__cp__le__cs__remove__config.md#a4591af2e952f514b185db12c5f1158d5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__cs__remove__config.md#a4591af2e952f514b185db12c5f1158d5);

[ 2738](structbt__hci__cp__le__cs__remove__config.md#a9be71a1360f1ed14e6a7e205f5704e39) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [config\_id](structbt__hci__cp__le__cs__remove__config.md#a9be71a1360f1ed14e6a7e205f5704e39);

2739} \_\_packed;

2740

[ 2741](hci__types_8h.md#a4c45c8b2b33ae857c654cc100b5e5550)#define BT\_HCI\_OP\_LE\_CS\_TEST\_END BT\_OP(BT\_OGF\_LE, 0x0096) /\* 0x2096 \*/

2742

2743/\* Event definitions \*/

2744

[ 2745](hci__types_8h.md#a0f44f6e5037d650b9dd0c5f34ba681b5)#define BT\_HCI\_EVT\_UNKNOWN 0x00

[ 2746](hci__types_8h.md#a955fe06f3fcab82c3370cb621f0dbca0)#define BT\_HCI\_EVT\_VENDOR 0xff

2747

[ 2748](hci__types_8h.md#abd8f15d920c0bdb3c68556b4e873f413)#define BT\_HCI\_EVT\_INQUIRY\_COMPLETE 0x01

[ 2749](structbt__hci__evt__inquiry__complete.md)struct [bt\_hci\_evt\_inquiry\_complete](structbt__hci__evt__inquiry__complete.md) {

[ 2750](structbt__hci__evt__inquiry__complete.md#aa8c1e8dc9807476f4759a3b3648b6332) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__inquiry__complete.md#aa8c1e8dc9807476f4759a3b3648b6332);

2751} \_\_packed;

2752

[ 2753](hci__types_8h.md#a0dd2162851b4a7afc3d96924f69cceca)#define BT\_HCI\_EVT\_CONN\_COMPLETE 0x03

[ 2754](structbt__hci__evt__conn__complete.md)struct [bt\_hci\_evt\_conn\_complete](structbt__hci__evt__conn__complete.md) {

[ 2755](structbt__hci__evt__conn__complete.md#a3dbf4fef53279003b7304ffee4a55e56) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__conn__complete.md#a3dbf4fef53279003b7304ffee4a55e56);

[ 2756](structbt__hci__evt__conn__complete.md#ad8877912008ea7445a67abc43aab5021) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__conn__complete.md#ad8877912008ea7445a67abc43aab5021);

[ 2757](structbt__hci__evt__conn__complete.md#a60a2ca6a8f16e4562c12b369685efa9b) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__evt__conn__complete.md#a60a2ca6a8f16e4562c12b369685efa9b);

[ 2758](structbt__hci__evt__conn__complete.md#afd9a21adf7d35205fb7e222c2e9e0328) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [link\_type](structbt__hci__evt__conn__complete.md#afd9a21adf7d35205fb7e222c2e9e0328);

[ 2759](structbt__hci__evt__conn__complete.md#a975617e8b568675a3ed8883cbe411557) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [encr\_enabled](structbt__hci__evt__conn__complete.md#a975617e8b568675a3ed8883cbe411557);

2760} \_\_packed;

2761

[ 2762](hci__types_8h.md#afc473fec33612ffb044d54bad39e8d76)#define BT\_HCI\_EVT\_CONN\_REQUEST 0x04

[ 2763](structbt__hci__evt__conn__request.md)struct [bt\_hci\_evt\_conn\_request](structbt__hci__evt__conn__request.md) {

[ 2764](structbt__hci__evt__conn__request.md#a03a2ee7ff7754173dff0809e4ebce9e6) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__evt__conn__request.md#a03a2ee7ff7754173dff0809e4ebce9e6);

[ 2765](structbt__hci__evt__conn__request.md#a6059d7c56f45d2fe047a7324db1e820d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dev\_class](structbt__hci__evt__conn__request.md#a6059d7c56f45d2fe047a7324db1e820d)[3];

[ 2766](structbt__hci__evt__conn__request.md#ae11d550701f64717a7d6df5c89b92d0e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [link\_type](structbt__hci__evt__conn__request.md#ae11d550701f64717a7d6df5c89b92d0e);

2767} \_\_packed;

2768

[ 2769](hci__types_8h.md#a32e5051a114f8987b49c6957c84d60e2)#define BT\_HCI\_EVT\_DISCONN\_COMPLETE 0x05

[ 2770](structbt__hci__evt__disconn__complete.md)struct [bt\_hci\_evt\_disconn\_complete](structbt__hci__evt__disconn__complete.md) {

[ 2771](structbt__hci__evt__disconn__complete.md#aed22ac781e9d70d11e7ebbe6f2e063bd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__disconn__complete.md#aed22ac781e9d70d11e7ebbe6f2e063bd);

[ 2772](structbt__hci__evt__disconn__complete.md#ab75f198a6495ad02a00bb3df99ab4258) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__disconn__complete.md#ab75f198a6495ad02a00bb3df99ab4258);

[ 2773](structbt__hci__evt__disconn__complete.md#a172554fbacf7aaa4dfbafe58b60fa5e6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reason](structbt__hci__evt__disconn__complete.md#a172554fbacf7aaa4dfbafe58b60fa5e6);

2774} \_\_packed;

2775

[ 2776](hci__types_8h.md#acc9c74c8406b84baaf55d9452924aaf9)#define BT\_HCI\_EVT\_AUTH\_COMPLETE 0x06

[ 2777](structbt__hci__evt__auth__complete.md)struct [bt\_hci\_evt\_auth\_complete](structbt__hci__evt__auth__complete.md) {

[ 2778](structbt__hci__evt__auth__complete.md#ae2b4b5bcc7195247626004d46ee22dd5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__auth__complete.md#ae2b4b5bcc7195247626004d46ee22dd5);

[ 2779](structbt__hci__evt__auth__complete.md#a7a78803e156218f138866fbb13fdadce) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__auth__complete.md#a7a78803e156218f138866fbb13fdadce);

2780} \_\_packed;

2781

[ 2782](hci__types_8h.md#a1a4be9cf628063db2fb821f67c54ea56)#define BT\_HCI\_EVT\_REMOTE\_NAME\_REQ\_COMPLETE 0x07

[ 2783](structbt__hci__evt__remote__name__req__complete.md)struct [bt\_hci\_evt\_remote\_name\_req\_complete](structbt__hci__evt__remote__name__req__complete.md) {

[ 2784](structbt__hci__evt__remote__name__req__complete.md#ab43d4a3c19d829b829cc7b40a67959f3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__remote__name__req__complete.md#ab43d4a3c19d829b829cc7b40a67959f3);

[ 2785](structbt__hci__evt__remote__name__req__complete.md#a380121873bf059b7c8a4abdf212f4235) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__evt__remote__name__req__complete.md#a380121873bf059b7c8a4abdf212f4235);

[ 2786](structbt__hci__evt__remote__name__req__complete.md#a3e54674692f7fc1670fa389e293714c7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [name](structbt__hci__evt__remote__name__req__complete.md#a3e54674692f7fc1670fa389e293714c7)[248];

2787} \_\_packed;

2788

[ 2789](hci__types_8h.md#a8dee2fc366d0371b68b212ff40e6ea7d)#define BT\_HCI\_EVT\_ENCRYPT\_CHANGE 0x08

[ 2790](structbt__hci__evt__encrypt__change.md)struct [bt\_hci\_evt\_encrypt\_change](structbt__hci__evt__encrypt__change.md) {

[ 2791](structbt__hci__evt__encrypt__change.md#af063bbd28d29edbcc81e907631167de7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__encrypt__change.md#af063bbd28d29edbcc81e907631167de7);

[ 2792](structbt__hci__evt__encrypt__change.md#a7737f659115ca602c1224c364a4c7404) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__encrypt__change.md#a7737f659115ca602c1224c364a4c7404);

[ 2793](structbt__hci__evt__encrypt__change.md#a61cc0e3c209acbb289d071515b44860a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [encrypt](structbt__hci__evt__encrypt__change.md#a61cc0e3c209acbb289d071515b44860a);

2794} \_\_packed;

2795

[ 2796](hci__types_8h.md#acbad340a978d4fc118af826d2c1a81e3)#define BT\_HCI\_EVT\_REMOTE\_FEATURES 0x0b

[ 2797](structbt__hci__evt__remote__features.md)struct [bt\_hci\_evt\_remote\_features](structbt__hci__evt__remote__features.md) {

[ 2798](structbt__hci__evt__remote__features.md#a2cedd8392c87914272ff250a56c80574) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__remote__features.md#a2cedd8392c87914272ff250a56c80574);

[ 2799](structbt__hci__evt__remote__features.md#ada0249bdb7108c5d347fea1218c4f878) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__remote__features.md#ada0249bdb7108c5d347fea1218c4f878);

[ 2800](structbt__hci__evt__remote__features.md#a70c97b9fbf7c363eab7b27f3a4e86e96) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [features](structbt__hci__evt__remote__features.md#a70c97b9fbf7c363eab7b27f3a4e86e96)[8];

2801} \_\_packed;

2802

[ 2803](hci__types_8h.md#a18f58c80d213d666ee8309cda8eb0a26)#define BT\_HCI\_EVT\_REMOTE\_VERSION\_INFO 0x0c

[ 2804](structbt__hci__evt__remote__version__info.md)struct [bt\_hci\_evt\_remote\_version\_info](structbt__hci__evt__remote__version__info.md) {

[ 2805](structbt__hci__evt__remote__version__info.md#a196f9489183d6e0116ff687df66c60c0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__remote__version__info.md#a196f9489183d6e0116ff687df66c60c0);

[ 2806](structbt__hci__evt__remote__version__info.md#a1703a9ac9a5e1ba3ed396fe5799f9f51) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__remote__version__info.md#a1703a9ac9a5e1ba3ed396fe5799f9f51);

[ 2807](structbt__hci__evt__remote__version__info.md#a8442b9f2bdc6cbce564c9bcec4169a20) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [version](structbt__hci__evt__remote__version__info.md#a8442b9f2bdc6cbce564c9bcec4169a20);

[ 2808](structbt__hci__evt__remote__version__info.md#aaa9c3875143700b6ed013715cb3c7107) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [manufacturer](structbt__hci__evt__remote__version__info.md#aaa9c3875143700b6ed013715cb3c7107);

[ 2809](structbt__hci__evt__remote__version__info.md#a02188119418a5a6dd8a4d0c37f5a060d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [subversion](structbt__hci__evt__remote__version__info.md#a02188119418a5a6dd8a4d0c37f5a060d);

2810} \_\_packed;

2811

[ 2812](hci__types_8h.md#a06f6cf60885ac051cdc9b463fc3b7de7)#define BT\_HCI\_EVT\_CMD\_COMPLETE 0x0e

[ 2813](structbt__hci__evt__cmd__complete.md)struct [bt\_hci\_evt\_cmd\_complete](structbt__hci__evt__cmd__complete.md) {

[ 2814](structbt__hci__evt__cmd__complete.md#a4da0539f81057722c8c322685bc12a40) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ncmd](structbt__hci__evt__cmd__complete.md#a4da0539f81057722c8c322685bc12a40);

[ 2815](structbt__hci__evt__cmd__complete.md#a3e61d980b4fa3084d3c50ead735fb76d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [opcode](structbt__hci__evt__cmd__complete.md#a3e61d980b4fa3084d3c50ead735fb76d);

2816} \_\_packed;

2817

[ 2818](structbt__hci__evt__cc__status.md)struct [bt\_hci\_evt\_cc\_status](structbt__hci__evt__cc__status.md) {

[ 2819](structbt__hci__evt__cc__status.md#a97cceaa218700da9b529ebadbb08c42c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__cc__status.md#a97cceaa218700da9b529ebadbb08c42c);

2820} \_\_packed;

2821

[ 2822](hci__types_8h.md#a2b35e7484351228243bb3564273c5bff)#define BT\_HCI\_EVT\_CMD\_STATUS 0x0f

[ 2823](structbt__hci__evt__cmd__status.md)struct [bt\_hci\_evt\_cmd\_status](structbt__hci__evt__cmd__status.md) {

[ 2824](structbt__hci__evt__cmd__status.md#aedd1560409005dbce409b892af1e3edf) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__cmd__status.md#aedd1560409005dbce409b892af1e3edf);

[ 2825](structbt__hci__evt__cmd__status.md#aed690e1cea2411df167e66cfaa742639) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ncmd](structbt__hci__evt__cmd__status.md#aed690e1cea2411df167e66cfaa742639);

[ 2826](structbt__hci__evt__cmd__status.md#a34002b693dc201083be4be77cfddcdb5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [opcode](structbt__hci__evt__cmd__status.md#a34002b693dc201083be4be77cfddcdb5);

2827} \_\_packed;

2828

[ 2829](hci__types_8h.md#a54c3bdd2687d142f925183a46ffc5f8b)#define BT\_HCI\_EVT\_HARDWARE\_ERROR 0x10

[ 2830](structbt__hci__evt__hardware__error.md)struct [bt\_hci\_evt\_hardware\_error](structbt__hci__evt__hardware__error.md) {

[ 2831](structbt__hci__evt__hardware__error.md#ab7be990e7cc32df43a3c976cb922e333) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [hardware\_code](structbt__hci__evt__hardware__error.md#ab7be990e7cc32df43a3c976cb922e333);

2832} \_\_packed;

2833

[ 2834](hci__types_8h.md#a9508e6faf71a345f7ff3d2cec9d85dde)#define BT\_HCI\_EVT\_ROLE\_CHANGE 0x12

[ 2835](structbt__hci__evt__role__change.md)struct [bt\_hci\_evt\_role\_change](structbt__hci__evt__role__change.md) {

[ 2836](structbt__hci__evt__role__change.md#aafe1a9e43a9a42d4030846180e55b8ef) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__role__change.md#aafe1a9e43a9a42d4030846180e55b8ef);

[ 2837](structbt__hci__evt__role__change.md#a18dd22435ae40fcf1c4fd2b90b402c60) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__evt__role__change.md#a18dd22435ae40fcf1c4fd2b90b402c60);

[ 2838](structbt__hci__evt__role__change.md#a2e5736d63e30326c33bec8ebdf986c62) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [role](structbt__hci__evt__role__change.md#a2e5736d63e30326c33bec8ebdf986c62);

2839} \_\_packed;

2840

[ 2841](hci__types_8h.md#a883433c60959629a013d34cea21ab88f)#define BT\_HCI\_EVT\_NUM\_COMPLETED\_PACKETS 0x13

[ 2842](structbt__hci__evt__num__completed__packets.md)struct [bt\_hci\_evt\_num\_completed\_packets](structbt__hci__evt__num__completed__packets.md) {

[ 2843](structbt__hci__evt__num__completed__packets.md#a666ed2c19596a89ab0c77275cbe18d1e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_handles](structbt__hci__evt__num__completed__packets.md#a666ed2c19596a89ab0c77275cbe18d1e);

[ 2844](structbt__hci__evt__num__completed__packets.md#a94fb176924f7e844704be28851366052) struct [bt\_hci\_handle\_count](structbt__hci__handle__count.md) [h](structbt__hci__evt__num__completed__packets.md#a94fb176924f7e844704be28851366052)[0];

2845} \_\_packed;

2846

[ 2847](hci__types_8h.md#a8c16e0bdecf9eae58bbd884fb48b0fc2)#define BT\_HCI\_EVT\_PIN\_CODE\_REQ 0x16

[ 2848](structbt__hci__evt__pin__code__req.md)struct [bt\_hci\_evt\_pin\_code\_req](structbt__hci__evt__pin__code__req.md) {

[ 2849](structbt__hci__evt__pin__code__req.md#a8649a30cd8c7ecf9ee006ddc2e625908) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__evt__pin__code__req.md#a8649a30cd8c7ecf9ee006ddc2e625908);

2850} \_\_packed;

2851

[ 2852](hci__types_8h.md#aab60607637f0e1f8e3cbf9f7292ddc57)#define BT\_HCI\_EVT\_LINK\_KEY\_REQ 0x17

[ 2853](structbt__hci__evt__link__key__req.md)struct [bt\_hci\_evt\_link\_key\_req](structbt__hci__evt__link__key__req.md) {

[ 2854](structbt__hci__evt__link__key__req.md#aed882dfb6b632383543bd7e60536ccc6) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__evt__link__key__req.md#aed882dfb6b632383543bd7e60536ccc6);

2855} \_\_packed;

2856

2857/\* Link Key types \*/

[ 2858](hci__types_8h.md#a7283a42b1220dd6d56c22cd9cb424e7c)#define BT\_LK\_COMBINATION 0x00

[ 2859](hci__types_8h.md#a12ffe67b9e4ec01bbe400a6a3cc5b859)#define BT\_LK\_LOCAL\_UNIT 0x01

[ 2860](hci__types_8h.md#aeb53b797c4fc91a38a459ff5f29d35e1)#define BT\_LK\_REMOTE\_UNIT 0x02

[ 2861](hci__types_8h.md#a916e6133d2dadb9aaf5fe42d0c0e1b96)#define BT\_LK\_DEBUG\_COMBINATION 0x03

[ 2862](hci__types_8h.md#adfea495d48088eae78491a14730bef31)#define BT\_LK\_UNAUTH\_COMBINATION\_P192 0x04

[ 2863](hci__types_8h.md#a6630ceb874d343f721931f80ee5fa67e)#define BT\_LK\_AUTH\_COMBINATION\_P192 0x05

[ 2864](hci__types_8h.md#a5753841a02ba0c2fa627d9e96bad045d)#define BT\_LK\_CHANGED\_COMBINATION 0x06

[ 2865](hci__types_8h.md#ada18ab581a323eafe8754009ef27d05e)#define BT\_LK\_UNAUTH\_COMBINATION\_P256 0x07

[ 2866](hci__types_8h.md#aa941cce486c497afa6d03fec326396b9)#define BT\_LK\_AUTH\_COMBINATION\_P256 0x08

2867

[ 2868](hci__types_8h.md#a15578dd8e9d2b16a28ea0b020ac9112b)#define BT\_HCI\_EVT\_LINK\_KEY\_NOTIFY 0x18

[ 2869](structbt__hci__evt__link__key__notify.md)struct [bt\_hci\_evt\_link\_key\_notify](structbt__hci__evt__link__key__notify.md) {

[ 2870](structbt__hci__evt__link__key__notify.md#a02647d66142c037b8bca2e748bc15319) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__evt__link__key__notify.md#a02647d66142c037b8bca2e748bc15319);

[ 2871](structbt__hci__evt__link__key__notify.md#a4a1b50d8874d01a6a5dc5c52524c9bed) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [link\_key](structbt__hci__evt__link__key__notify.md#a4a1b50d8874d01a6a5dc5c52524c9bed)[16];

[ 2872](structbt__hci__evt__link__key__notify.md#a664580660a690af0d9ae3a62d79ad94b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key\_type](structbt__hci__evt__link__key__notify.md#a664580660a690af0d9ae3a62d79ad94b);

2873} \_\_packed;

2874

2875/\* Overflow link types \*/

[ 2876](hci__types_8h.md#a44233b934e33c65af90d03ad301e6b9d)#define BT\_OVERFLOW\_LINK\_SYNCH 0x00

[ 2877](hci__types_8h.md#a35831810e3a7e2c5446780b14ef7d9c1)#define BT\_OVERFLOW\_LINK\_ACL 0x01

[ 2878](hci__types_8h.md#ad32010743baef10c635d8b08f21c8641)#define BT\_OVERFLOW\_LINK\_ISO 0x02

2879

[ 2880](hci__types_8h.md#ae747b016101bc9e9614163288c5c0d15)#define BT\_HCI\_EVT\_DATA\_BUF\_OVERFLOW 0x1a

[ 2881](structbt__hci__evt__data__buf__overflow.md)struct [bt\_hci\_evt\_data\_buf\_overflow](structbt__hci__evt__data__buf__overflow.md) {

[ 2882](structbt__hci__evt__data__buf__overflow.md#ae0201e03ebb9b9b33e9eae593a56355f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [link\_type](structbt__hci__evt__data__buf__overflow.md#ae0201e03ebb9b9b33e9eae593a56355f);

2883} \_\_packed;

2884

[ 2885](hci__types_8h.md#a92243c99484922771d5aca8f98945d29)#define BT\_HCI\_EVT\_INQUIRY\_RESULT\_WITH\_RSSI 0x22

[ 2886](structbt__hci__evt__inquiry__result__with__rssi.md)struct [bt\_hci\_evt\_inquiry\_result\_with\_rssi](structbt__hci__evt__inquiry__result__with__rssi.md) {

[ 2887](structbt__hci__evt__inquiry__result__with__rssi.md#af955dd1660f83e41e6d1b2b5aecf8133) [bt\_addr\_t](structbt__addr__t.md) [addr](structbt__hci__evt__inquiry__result__with__rssi.md#af955dd1660f83e41e6d1b2b5aecf8133);

[ 2888](structbt__hci__evt__inquiry__result__with__rssi.md#a0a5c188d0d40b4259cbeb613c0dd12cf) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pscan\_rep\_mode](structbt__hci__evt__inquiry__result__with__rssi.md#a0a5c188d0d40b4259cbeb613c0dd12cf);

[ 2889](structbt__hci__evt__inquiry__result__with__rssi.md#a09914ee9998c0b59cb35ed74d08aa4f2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reserved](structbt__hci__evt__inquiry__result__with__rssi.md#a09914ee9998c0b59cb35ed74d08aa4f2);

[ 2890](structbt__hci__evt__inquiry__result__with__rssi.md#ad9b4920e2864ed8350de038dffe64574) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cod](structbt__hci__evt__inquiry__result__with__rssi.md#ad9b4920e2864ed8350de038dffe64574)[3];

[ 2891](structbt__hci__evt__inquiry__result__with__rssi.md#a1ee08f85103581994a88345cc94d7494) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [clock\_offset](structbt__hci__evt__inquiry__result__with__rssi.md#a1ee08f85103581994a88345cc94d7494);

[ 2892](structbt__hci__evt__inquiry__result__with__rssi.md#a6d19e6400d7015db7122516e570d7989) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__hci__evt__inquiry__result__with__rssi.md#a6d19e6400d7015db7122516e570d7989);

2893} \_\_packed;

2894

[ 2895](hci__types_8h.md#a092a782ea069c98475a6617241321122)#define BT\_HCI\_EVT\_REMOTE\_EXT\_FEATURES 0x23

[ 2896](structbt__hci__evt__remote__ext__features.md)struct [bt\_hci\_evt\_remote\_ext\_features](structbt__hci__evt__remote__ext__features.md) {

[ 2897](structbt__hci__evt__remote__ext__features.md#a4f1d489aaa5626e485d34a9ae4cf9a34) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__remote__ext__features.md#a4f1d489aaa5626e485d34a9ae4cf9a34);

[ 2898](structbt__hci__evt__remote__ext__features.md#a0191b80b4f4d5360972faa6d5edf5055) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__remote__ext__features.md#a0191b80b4f4d5360972faa6d5edf5055);

[ 2899](structbt__hci__evt__remote__ext__features.md#aeece2b8d46f4a3713d63df29058f2d9c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [page](structbt__hci__evt__remote__ext__features.md#aeece2b8d46f4a3713d63df29058f2d9c);

[ 2900](structbt__hci__evt__remote__ext__features.md#afa577407f4ded5404394f42e7c73e10b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_page](structbt__hci__evt__remote__ext__features.md#afa577407f4ded5404394f42e7c73e10b);

[ 2901](structbt__hci__evt__remote__ext__features.md#a084199f8e30669c2a1a631af26c0d69a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [features](structbt__hci__evt__remote__ext__features.md#a084199f8e30669c2a1a631af26c0d69a)[8];

2902} \_\_packed;

2903

[ 2904](hci__types_8h.md#a0decb07f1b4ae20b23cffc616dd442e4)#define BT\_HCI\_EVT\_LE\_PER\_ADV\_SYNC\_ESTABLISHED\_V2 0x24

[ 2905](structbt__hci__evt__le__per__adv__sync__established__v2.md)struct [bt\_hci\_evt\_le\_per\_adv\_sync\_established\_v2](structbt__hci__evt__le__per__adv__sync__established__v2.md) {

[ 2906](structbt__hci__evt__le__per__adv__sync__established__v2.md#a96b975f5a2fcf193b0b58c230486ec36) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__per__adv__sync__established__v2.md#a96b975f5a2fcf193b0b58c230486ec36);

[ 2907](structbt__hci__evt__le__per__adv__sync__established__v2.md#ab7d3793e782d7b2bb311b8a5ac3a871b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__per__adv__sync__established__v2.md#ab7d3793e782d7b2bb311b8a5ac3a871b);

[ 2908](structbt__hci__evt__le__per__adv__sync__established__v2.md#a0ce9a9170d93ff69f25ff35eb163511f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__hci__evt__le__per__adv__sync__established__v2.md#a0ce9a9170d93ff69f25ff35eb163511f);

[ 2909](structbt__hci__evt__le__per__adv__sync__established__v2.md#abd67ec989479eb793e7bf99a4cf371b8) [bt\_addr\_le\_t](structbt__addr__le__t.md) [adv\_addr](structbt__hci__evt__le__per__adv__sync__established__v2.md#abd67ec989479eb793e7bf99a4cf371b8);

[ 2910](structbt__hci__evt__le__per__adv__sync__established__v2.md#a36b5c8454ee3635d2298592c83166f14) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__evt__le__per__adv__sync__established__v2.md#a36b5c8454ee3635d2298592c83166f14);

[ 2911](structbt__hci__evt__le__per__adv__sync__established__v2.md#a958630cb9e275ab6f8ed0c548958e5ee) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__hci__evt__le__per__adv__sync__established__v2.md#a958630cb9e275ab6f8ed0c548958e5ee);

[ 2912](structbt__hci__evt__le__per__adv__sync__established__v2.md#a13ab0e87d6673a34e51f3112a5fd5a0c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [clock\_accuracy](structbt__hci__evt__le__per__adv__sync__established__v2.md#a13ab0e87d6673a34e51f3112a5fd5a0c);

[ 2913](structbt__hci__evt__le__per__adv__sync__established__v2.md#af4fb92baa4f98c08c990ba505faf9226) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_subevents](structbt__hci__evt__le__per__adv__sync__established__v2.md#af4fb92baa4f98c08c990ba505faf9226);

[ 2914](structbt__hci__evt__le__per__adv__sync__established__v2.md#ad21df6269d8242d94ba9cbc1e0d4d344) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent\_interval](structbt__hci__evt__le__per__adv__sync__established__v2.md#ad21df6269d8242d94ba9cbc1e0d4d344);

[ 2915](structbt__hci__evt__le__per__adv__sync__established__v2.md#ac4c2bc8789513692ce0f2cc81aa59476) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot\_delay](structbt__hci__evt__le__per__adv__sync__established__v2.md#ac4c2bc8789513692ce0f2cc81aa59476);

[ 2916](structbt__hci__evt__le__per__adv__sync__established__v2.md#aacb6946dbfeb2ffbc251910853559329) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot\_spacing](structbt__hci__evt__le__per__adv__sync__established__v2.md#aacb6946dbfeb2ffbc251910853559329);

2917} \_\_packed;

2918

[ 2919](hci__types_8h.md#a8d067bf751953fd8a7bb5421bdc94970)#define BT\_HCI\_EVT\_LE\_PER\_ADVERTISING\_REPORT\_V2 0x25

[ 2920](structbt__hci__evt__le__per__advertising__report__v2.md)struct [bt\_hci\_evt\_le\_per\_advertising\_report\_v2](structbt__hci__evt__le__per__advertising__report__v2.md) {

[ 2921](structbt__hci__evt__le__per__advertising__report__v2.md#a34b15fb9b5b4f0d199ccf274dd489c6a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__per__advertising__report__v2.md#a34b15fb9b5b4f0d199ccf274dd489c6a);

[ 2922](structbt__hci__evt__le__per__advertising__report__v2.md#a37a9eb7d417da9285e22cc7f83071c69) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__hci__evt__le__per__advertising__report__v2.md#a37a9eb7d417da9285e22cc7f83071c69);

[ 2923](structbt__hci__evt__le__per__advertising__report__v2.md#ad598ffd0108825803a4734959a354bd8) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__hci__evt__le__per__advertising__report__v2.md#ad598ffd0108825803a4734959a354bd8);

[ 2924](structbt__hci__evt__le__per__advertising__report__v2.md#a3276c2e11c946744b73426f54bf62b8c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__hci__evt__le__per__advertising__report__v2.md#a3276c2e11c946744b73426f54bf62b8c);

[ 2925](structbt__hci__evt__le__per__advertising__report__v2.md#a499d82e1e3cfc501d399f570ebbcdc42) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [periodic\_event\_counter](structbt__hci__evt__le__per__advertising__report__v2.md#a499d82e1e3cfc501d399f570ebbcdc42);

[ 2926](structbt__hci__evt__le__per__advertising__report__v2.md#af27b23fe38e9ff092d8839cd81749456) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent](structbt__hci__evt__le__per__advertising__report__v2.md#af27b23fe38e9ff092d8839cd81749456);

[ 2927](structbt__hci__evt__le__per__advertising__report__v2.md#a73496cc962721538e27e9924fff0f3db) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_status](structbt__hci__evt__le__per__advertising__report__v2.md#a73496cc962721538e27e9924fff0f3db);

[ 2928](structbt__hci__evt__le__per__advertising__report__v2.md#a30f4e81346957ad4f9f0488dd93fafc3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [length](structbt__hci__evt__le__per__advertising__report__v2.md#a30f4e81346957ad4f9f0488dd93fafc3);

[ 2929](structbt__hci__evt__le__per__advertising__report__v2.md#a7af1cd4ec9df24e575a83a640eea36d2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__hci__evt__le__per__advertising__report__v2.md#a7af1cd4ec9df24e575a83a640eea36d2)[0];

2930} \_\_packed;

2931

[ 2932](hci__types_8h.md#a5379a2a0016a2551ac79736924c7ea86)#define BT\_HCI\_EVT\_LE\_PAST\_RECEIVED\_V2 0x26

[ 2933](structbt__hci__evt__le__past__received__v2.md)struct [bt\_hci\_evt\_le\_past\_received\_v2](structbt__hci__evt__le__past__received__v2.md) {

[ 2934](structbt__hci__evt__le__past__received__v2.md#aefe79f973eda8c7c5670c7a721d55d8a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__past__received__v2.md#aefe79f973eda8c7c5670c7a721d55d8a);

[ 2935](structbt__hci__evt__le__past__received__v2.md#adb011949f592ec7f8843d4fd47eca2e9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__evt__le__past__received__v2.md#adb011949f592ec7f8843d4fd47eca2e9);

[ 2936](structbt__hci__evt__le__past__received__v2.md#acffc2fa22a16a3a12a4f7dfc3bb45866) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [service\_data](structbt__hci__evt__le__past__received__v2.md#acffc2fa22a16a3a12a4f7dfc3bb45866);

[ 2937](structbt__hci__evt__le__past__received__v2.md#a00bf4bdf12fce6cbf2874b9c4ae09f9f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sync\_handle](structbt__hci__evt__le__past__received__v2.md#a00bf4bdf12fce6cbf2874b9c4ae09f9f);

[ 2938](structbt__hci__evt__le__past__received__v2.md#a05d798c9415541ef7f5716992157b1a1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_sid](structbt__hci__evt__le__past__received__v2.md#a05d798c9415541ef7f5716992157b1a1);

[ 2939](structbt__hci__evt__le__past__received__v2.md#aff78554e8980635290767e9877ac479b) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__hci__evt__le__past__received__v2.md#aff78554e8980635290767e9877ac479b);

[ 2940](structbt__hci__evt__le__past__received__v2.md#ae7a73293519ab45aec40a9a1aeaa4e89) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__evt__le__past__received__v2.md#ae7a73293519ab45aec40a9a1aeaa4e89);

[ 2941](structbt__hci__evt__le__past__received__v2.md#a736af2c2ee0afd3cb00e8eb4d103991c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__hci__evt__le__past__received__v2.md#a736af2c2ee0afd3cb00e8eb4d103991c);

[ 2942](structbt__hci__evt__le__past__received__v2.md#a78853d14c3bf9a9aba3c4e15b2e06abb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [clock\_accuracy](structbt__hci__evt__le__past__received__v2.md#a78853d14c3bf9a9aba3c4e15b2e06abb);

[ 2943](structbt__hci__evt__le__past__received__v2.md#ab8a2a55fe071218284d60f1a2896945b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_subevents](structbt__hci__evt__le__past__received__v2.md#ab8a2a55fe071218284d60f1a2896945b);

[ 2944](structbt__hci__evt__le__past__received__v2.md#aefdc5ac7ef125f4dc5865c198b98c67d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent\_interval](structbt__hci__evt__le__past__received__v2.md#aefdc5ac7ef125f4dc5865c198b98c67d);

[ 2945](structbt__hci__evt__le__past__received__v2.md#a9f55d5f6d17d11e72f7cac363a69fe97) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot\_delay](structbt__hci__evt__le__past__received__v2.md#a9f55d5f6d17d11e72f7cac363a69fe97);

[ 2946](structbt__hci__evt__le__past__received__v2.md#acf711399e575295dcef73cfeeb844eab) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot\_spacing](structbt__hci__evt__le__past__received__v2.md#acf711399e575295dcef73cfeeb844eab);

2947} \_\_packed;

2948

[ 2949](hci__types_8h.md#a4395b8b850e9fd3735c2369798f9c226)#define BT\_HCI\_EVT\_LE\_PER\_ADV\_SUBEVENT\_DATA\_REQUEST 0x27

[ 2950](structbt__hci__evt__le__per__adv__subevent__data__request.md)struct [bt\_hci\_evt\_le\_per\_adv\_subevent\_data\_request](structbt__hci__evt__le__per__adv__subevent__data__request.md) {

[ 2951](structbt__hci__evt__le__per__adv__subevent__data__request.md#ae6f6ef17edabfd210a7e6597087ff512) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_handle](structbt__hci__evt__le__per__adv__subevent__data__request.md#ae6f6ef17edabfd210a7e6597087ff512);

[ 2952](structbt__hci__evt__le__per__adv__subevent__data__request.md#a8f7fd9b149aa52422cb3eb874b91943d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent\_start](structbt__hci__evt__le__per__adv__subevent__data__request.md#a8f7fd9b149aa52422cb3eb874b91943d);

[ 2953](structbt__hci__evt__le__per__adv__subevent__data__request.md#a45cdb248b80602a7f14f24e0324e6f97) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent\_data\_count](structbt__hci__evt__le__per__adv__subevent__data__request.md#a45cdb248b80602a7f14f24e0324e6f97);

2954} \_\_packed;

2955

[ 2956](hci__types_8h.md#a64e0f465068e72e98904fa6cdc33d3de)#define BT\_HCI\_EVT\_LE\_PER\_ADV\_RESPONSE\_REPORT 0x28

2957

[ 2958](structbt__hci__evt__le__per__adv__response.md)struct [bt\_hci\_evt\_le\_per\_adv\_response](structbt__hci__evt__le__per__adv__response.md) {

[ 2959](structbt__hci__evt__le__per__adv__response.md#a74e304822ec7a431802cf8a7539d640e) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__hci__evt__le__per__adv__response.md#a74e304822ec7a431802cf8a7539d640e);

[ 2960](structbt__hci__evt__le__per__adv__response.md#a1100429baf398067a396a6ba8db6778a) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__hci__evt__le__per__adv__response.md#a1100429baf398067a396a6ba8db6778a);

[ 2961](structbt__hci__evt__le__per__adv__response.md#a4197fbae54be038502312efc14b66320) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__hci__evt__le__per__adv__response.md#a4197fbae54be038502312efc14b66320);

[ 2962](structbt__hci__evt__le__per__adv__response.md#aa5b5467f4edd52fb8de078b0948141f0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot](structbt__hci__evt__le__per__adv__response.md#aa5b5467f4edd52fb8de078b0948141f0);

[ 2963](structbt__hci__evt__le__per__adv__response.md#aa524756d2cce0718ecfd66704eaf389d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_status](structbt__hci__evt__le__per__adv__response.md#aa524756d2cce0718ecfd66704eaf389d);

[ 2964](structbt__hci__evt__le__per__adv__response.md#af68f0dc92118f78f6f5b0ffbf1854664) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_length](structbt__hci__evt__le__per__adv__response.md#af68f0dc92118f78f6f5b0ffbf1854664);

[ 2965](structbt__hci__evt__le__per__adv__response.md#ace3b58eba63b55ce5f3038d4a7877ec2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__hci__evt__le__per__adv__response.md#ace3b58eba63b55ce5f3038d4a7877ec2)[0];

2966} \_\_packed;

2967

[ 2968](structbt__hci__evt__le__per__adv__response__report.md)struct [bt\_hci\_evt\_le\_per\_adv\_response\_report](structbt__hci__evt__le__per__adv__response__report.md) {

[ 2969](structbt__hci__evt__le__per__adv__response__report.md#a9d746015a9c2b48c54008319c892b063) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_handle](structbt__hci__evt__le__per__adv__response__report.md#a9d746015a9c2b48c54008319c892b063);

[ 2970](structbt__hci__evt__le__per__adv__response__report.md#ad4f8f61150f82f4ba420e3c0a1f333c2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent](structbt__hci__evt__le__per__adv__response__report.md#ad4f8f61150f82f4ba420e3c0a1f333c2);

[ 2971](structbt__hci__evt__le__per__adv__response__report.md#a46a5b74321a80697fd700a276be18ed3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_status](structbt__hci__evt__le__per__adv__response__report.md#a46a5b74321a80697fd700a276be18ed3);

[ 2972](structbt__hci__evt__le__per__adv__response__report.md#a37f3519eefe33e87d49c7c2ad0f8b40c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_responses](structbt__hci__evt__le__per__adv__response__report.md#a37f3519eefe33e87d49c7c2ad0f8b40c);

[ 2973](structbt__hci__evt__le__per__adv__response__report.md#a3b1bcca7a7dbc6fcf5709f6152268b87) struct [bt\_hci\_evt\_le\_per\_adv\_response](structbt__hci__evt__le__per__adv__response.md) [responses](structbt__hci__evt__le__per__adv__response__report.md#a3b1bcca7a7dbc6fcf5709f6152268b87)[0];

2974} \_\_packed;

2975

[ 2976](hci__types_8h.md#a60ea5e58028aa09c00d20cfff5c942d5)#define BT\_HCI\_EVT\_LE\_ENH\_CONN\_COMPLETE\_V2 0x29

[ 2977](structbt__hci__evt__le__enh__conn__complete__v2.md)struct [bt\_hci\_evt\_le\_enh\_conn\_complete\_v2](structbt__hci__evt__le__enh__conn__complete__v2.md) {

[ 2978](structbt__hci__evt__le__enh__conn__complete__v2.md#ad72ba07d766135a94474a9d004da1a66) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__enh__conn__complete__v2.md#ad72ba07d766135a94474a9d004da1a66);

[ 2979](structbt__hci__evt__le__enh__conn__complete__v2.md#affe2dba0634e0215579fb13d77016a8c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__enh__conn__complete__v2.md#affe2dba0634e0215579fb13d77016a8c);

[ 2980](structbt__hci__evt__le__enh__conn__complete__v2.md#a3343de57a24fa2ebdccf9411f388817d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [role](structbt__hci__evt__le__enh__conn__complete__v2.md#a3343de57a24fa2ebdccf9411f388817d);

[ 2981](structbt__hci__evt__le__enh__conn__complete__v2.md#a7df28c9ddec607d5a84572bb421b7f5a) [bt\_addr\_le\_t](structbt__addr__le__t.md) [peer\_addr](structbt__hci__evt__le__enh__conn__complete__v2.md#a7df28c9ddec607d5a84572bb421b7f5a);

[ 2982](structbt__hci__evt__le__enh__conn__complete__v2.md#a10a1cbf0e9e21bc127dc64adadd53773) [bt\_addr\_t](structbt__addr__t.md) [local\_rpa](structbt__hci__evt__le__enh__conn__complete__v2.md#a10a1cbf0e9e21bc127dc64adadd53773);

[ 2983](structbt__hci__evt__le__enh__conn__complete__v2.md#a014e8bf891684c4cd9e5ec53d986d412) [bt\_addr\_t](structbt__addr__t.md) [peer\_rpa](structbt__hci__evt__le__enh__conn__complete__v2.md#a014e8bf891684c4cd9e5ec53d986d412);

[ 2984](structbt__hci__evt__le__enh__conn__complete__v2.md#a237b8313970cc63b7e57c0ce4913392e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__hci__evt__le__enh__conn__complete__v2.md#a237b8313970cc63b7e57c0ce4913392e);

[ 2985](structbt__hci__evt__le__enh__conn__complete__v2.md#a3daa32ac19c4eda4a49bebb64f3145be) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [latency](structbt__hci__evt__le__enh__conn__complete__v2.md#a3daa32ac19c4eda4a49bebb64f3145be);

[ 2986](structbt__hci__evt__le__enh__conn__complete__v2.md#a2b2ac4890eb9604a3f5cd40f55c2c066) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [supv\_timeout](structbt__hci__evt__le__enh__conn__complete__v2.md#a2b2ac4890eb9604a3f5cd40f55c2c066);

[ 2987](structbt__hci__evt__le__enh__conn__complete__v2.md#a7bb168061803d1122e8ee47dc8af3ae9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [clock\_accuracy](structbt__hci__evt__le__enh__conn__complete__v2.md#a7bb168061803d1122e8ee47dc8af3ae9);

[ 2988](structbt__hci__evt__le__enh__conn__complete__v2.md#a883ba3aed9aed00ec0ce425999d97180) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_handle](structbt__hci__evt__le__enh__conn__complete__v2.md#a883ba3aed9aed00ec0ce425999d97180);

[ 2989](structbt__hci__evt__le__enh__conn__complete__v2.md#a81dca94a6f2a8ea3da7a5a316daa5941) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sync\_handle](structbt__hci__evt__le__enh__conn__complete__v2.md#a81dca94a6f2a8ea3da7a5a316daa5941);

2990} \_\_packed;

2991

[ 2992](hci__types_8h.md#ab77f3074a2236afc1ed773775d17befe)#define BT\_HCI\_EVT\_SYNC\_CONN\_COMPLETE 0x2c

[ 2993](structbt__hci__evt__sync__conn__complete.md)struct [bt\_hci\_evt\_sync\_conn\_complete](structbt__hci__evt__sync__conn__complete.md) {

[ 2994](structbt__hci__evt__sync__conn__complete.md#accd17a95f35ab1988122df7584830f60) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__sync__conn__complete.md#accd17a95f35ab1988122df7584830f60);

[ 2995](structbt__hci__evt__sync__conn__complete.md#aa48aa29ff73e93e8d961013f066c1b5e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__sync__conn__complete.md#aa48aa29ff73e93e8d961013f066c1b5e);

[ 2996](structbt__hci__evt__sync__conn__complete.md#a78f5560783400f1d1a63b2c9d69fa7ed) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__evt__sync__conn__complete.md#a78f5560783400f1d1a63b2c9d69fa7ed);

[ 2997](structbt__hci__evt__sync__conn__complete.md#aacf9919945e9b755913da145f0fe78ae) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [link\_type](structbt__hci__evt__sync__conn__complete.md#aacf9919945e9b755913da145f0fe78ae);

[ 2998](structbt__hci__evt__sync__conn__complete.md#a4b93873ad6f5388657511d87fc0a8c85) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_interval](structbt__hci__evt__sync__conn__complete.md#a4b93873ad6f5388657511d87fc0a8c85);

[ 2999](structbt__hci__evt__sync__conn__complete.md#a68a31880c8aab9245be043c1719464d3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [retansmission\_window](structbt__hci__evt__sync__conn__complete.md#a68a31880c8aab9245be043c1719464d3);

[ 3000](structbt__hci__evt__sync__conn__complete.md#a6a455f56da4666cb602e6c05157e166d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [rx\_pkt\_length](structbt__hci__evt__sync__conn__complete.md#a6a455f56da4666cb602e6c05157e166d);

[ 3001](structbt__hci__evt__sync__conn__complete.md#ab4d4106d5120f10e8300834db12740d8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [tx\_pkt\_length](structbt__hci__evt__sync__conn__complete.md#ab4d4106d5120f10e8300834db12740d8);

[ 3002](structbt__hci__evt__sync__conn__complete.md#a5f6068569bf649bcd1d13928f56f9703) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [air\_mode](structbt__hci__evt__sync__conn__complete.md#a5f6068569bf649bcd1d13928f56f9703);

3003} \_\_packed;

3004

[ 3005](hci__types_8h.md#a9b5405de1e07fcefba54b286bd1fdfbe)#define BT\_HCI\_EVT\_EXTENDED\_INQUIRY\_RESULT 0x2f

[ 3006](structbt__hci__evt__extended__inquiry__result.md)struct [bt\_hci\_evt\_extended\_inquiry\_result](structbt__hci__evt__extended__inquiry__result.md) {

[ 3007](structbt__hci__evt__extended__inquiry__result.md#a76e4e82d1dedaee94bd730a4134d7d77) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_reports](structbt__hci__evt__extended__inquiry__result.md#a76e4e82d1dedaee94bd730a4134d7d77);

[ 3008](structbt__hci__evt__extended__inquiry__result.md#a955a7d36736badfae1f39fa9eda61ebb) [bt\_addr\_t](structbt__addr__t.md) [addr](structbt__hci__evt__extended__inquiry__result.md#a955a7d36736badfae1f39fa9eda61ebb);

[ 3009](structbt__hci__evt__extended__inquiry__result.md#aba4aac84e23ca9d283cb8af265dcaf0d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pscan\_rep\_mode](structbt__hci__evt__extended__inquiry__result.md#aba4aac84e23ca9d283cb8af265dcaf0d);

[ 3010](structbt__hci__evt__extended__inquiry__result.md#ab6ec4b5efe058e225d173cbda9a16f2e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reserved](structbt__hci__evt__extended__inquiry__result.md#ab6ec4b5efe058e225d173cbda9a16f2e);

[ 3011](structbt__hci__evt__extended__inquiry__result.md#ab4ebcf09817827d1d10ddeee13832759) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cod](structbt__hci__evt__extended__inquiry__result.md#ab4ebcf09817827d1d10ddeee13832759)[3];

[ 3012](structbt__hci__evt__extended__inquiry__result.md#a30c5586d954585006238e8c2b33a7601) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [clock\_offset](structbt__hci__evt__extended__inquiry__result.md#a30c5586d954585006238e8c2b33a7601);

[ 3013](structbt__hci__evt__extended__inquiry__result.md#a21f7f48422bcfb867c9ca2e4411a2fbd) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__hci__evt__extended__inquiry__result.md#a21f7f48422bcfb867c9ca2e4411a2fbd);

[ 3014](structbt__hci__evt__extended__inquiry__result.md#a1eba2841941f7cdbb00f548ebf0485e9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [eir](structbt__hci__evt__extended__inquiry__result.md#a1eba2841941f7cdbb00f548ebf0485e9)[240];

3015} \_\_packed;

3016

[ 3017](hci__types_8h.md#aad28cc20cc111ac39e39011932b9d22e)#define BT\_HCI\_EVT\_ENCRYPT\_KEY\_REFRESH\_COMPLETE 0x30

[ 3018](structbt__hci__evt__encrypt__key__refresh__complete.md)struct [bt\_hci\_evt\_encrypt\_key\_refresh\_complete](structbt__hci__evt__encrypt__key__refresh__complete.md) {

[ 3019](structbt__hci__evt__encrypt__key__refresh__complete.md#afdd162cff0f1eedfe9e8ee7223b3226e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__encrypt__key__refresh__complete.md#afdd162cff0f1eedfe9e8ee7223b3226e);

[ 3020](structbt__hci__evt__encrypt__key__refresh__complete.md#af5562687a4f6e3a1e82cd1a81cec5ad6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__encrypt__key__refresh__complete.md#af5562687a4f6e3a1e82cd1a81cec5ad6);

3021} \_\_packed;

3022

[ 3023](hci__types_8h.md#a4d69a943660da9c1a6ffedb9b653ce3f)#define BT\_HCI\_EVT\_IO\_CAPA\_REQ 0x31

[ 3024](structbt__hci__evt__io__capa__req.md)struct [bt\_hci\_evt\_io\_capa\_req](structbt__hci__evt__io__capa__req.md) {

[ 3025](structbt__hci__evt__io__capa__req.md#a52412f7bd8f8dea391904b9f2444b50a) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__evt__io__capa__req.md#a52412f7bd8f8dea391904b9f2444b50a);

3026} \_\_packed;

3027

[ 3028](hci__types_8h.md#a0f5cae40268568e25142eed9e3e5e639)#define BT\_HCI\_EVT\_IO\_CAPA\_RESP 0x32

[ 3029](structbt__hci__evt__io__capa__resp.md)struct [bt\_hci\_evt\_io\_capa\_resp](structbt__hci__evt__io__capa__resp.md) {

[ 3030](structbt__hci__evt__io__capa__resp.md#adac9c9f3999099fd460651e3b012fd0f) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__evt__io__capa__resp.md#adac9c9f3999099fd460651e3b012fd0f);

[ 3031](structbt__hci__evt__io__capa__resp.md#a851eae620ad90067957d4dec2f04efbe) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [capability](structbt__hci__evt__io__capa__resp.md#a851eae620ad90067957d4dec2f04efbe);

[ 3032](structbt__hci__evt__io__capa__resp.md#ab12325d1536fe6a75d0a137bea301e8f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [oob\_data](structbt__hci__evt__io__capa__resp.md#ab12325d1536fe6a75d0a137bea301e8f);

[ 3033](structbt__hci__evt__io__capa__resp.md#a160cb3aea96bf698520e11673a40b2d7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [authentication](structbt__hci__evt__io__capa__resp.md#a160cb3aea96bf698520e11673a40b2d7);

3034} \_\_packed;

3035

[ 3036](hci__types_8h.md#a78cdb5848d8a12a8cbea17767b3d02aa)#define BT\_HCI\_EVT\_USER\_CONFIRM\_REQ 0x33

[ 3037](structbt__hci__evt__user__confirm__req.md)struct [bt\_hci\_evt\_user\_confirm\_req](structbt__hci__evt__user__confirm__req.md) {

[ 3038](structbt__hci__evt__user__confirm__req.md#aaeec83c50764c322af7cd64259e54a97) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__evt__user__confirm__req.md#aaeec83c50764c322af7cd64259e54a97);

[ 3039](structbt__hci__evt__user__confirm__req.md#ac333729f5a7d9241ac26aeb7d3f77935) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [passkey](structbt__hci__evt__user__confirm__req.md#ac333729f5a7d9241ac26aeb7d3f77935);

3040} \_\_packed;

3041

[ 3042](hci__types_8h.md#a38a1bce81af39bb28d40e149f9309b69)#define BT\_HCI\_EVT\_USER\_PASSKEY\_REQ 0x34

[ 3043](structbt__hci__evt__user__passkey__req.md)struct [bt\_hci\_evt\_user\_passkey\_req](structbt__hci__evt__user__passkey__req.md) {

[ 3044](structbt__hci__evt__user__passkey__req.md#a7f1005423296906e0374050bc30781ce) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__evt__user__passkey__req.md#a7f1005423296906e0374050bc30781ce);

3045} \_\_packed;

3046

[ 3047](hci__types_8h.md#a7d2ba655c6954f90de04cafafccd727f)#define BT\_HCI\_EVT\_SSP\_COMPLETE 0x36

[ 3048](structbt__hci__evt__ssp__complete.md)struct [bt\_hci\_evt\_ssp\_complete](structbt__hci__evt__ssp__complete.md) {

[ 3049](structbt__hci__evt__ssp__complete.md#a33d3d47c1cef71cfb787a1195d9b4ec2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__ssp__complete.md#a33d3d47c1cef71cfb787a1195d9b4ec2);

[ 3050](structbt__hci__evt__ssp__complete.md#a5030cf334f97cdd982001b3278ed9db1) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__evt__ssp__complete.md#a5030cf334f97cdd982001b3278ed9db1);

3051} \_\_packed;

3052

[ 3053](hci__types_8h.md#a724d43899b16fcb89c235898a21c13b9)#define BT\_HCI\_EVT\_USER\_PASSKEY\_NOTIFY 0x3b

[ 3054](structbt__hci__evt__user__passkey__notify.md)struct [bt\_hci\_evt\_user\_passkey\_notify](structbt__hci__evt__user__passkey__notify.md) {

[ 3055](structbt__hci__evt__user__passkey__notify.md#af020e1cd131473fe06a193529a0499ac) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__evt__user__passkey__notify.md#af020e1cd131473fe06a193529a0499ac);

[ 3056](structbt__hci__evt__user__passkey__notify.md#a7f6a367e50d41cb7d8897db05db826be) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [passkey](structbt__hci__evt__user__passkey__notify.md#a7f6a367e50d41cb7d8897db05db826be);

3057} \_\_packed;

3058

[ 3059](hci__types_8h.md#ac1d7f9270323d7fa459e60b372cf998b)#define BT\_HCI\_EVT\_LE\_META\_EVENT 0x3e

[ 3060](structbt__hci__evt__le__meta__event.md)struct [bt\_hci\_evt\_le\_meta\_event](structbt__hci__evt__le__meta__event.md) {

[ 3061](structbt__hci__evt__le__meta__event.md#a536464a525f8d0f9df915be5ee3d33da) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent](structbt__hci__evt__le__meta__event.md#a536464a525f8d0f9df915be5ee3d33da);

3062} \_\_packed;

3063

[ 3064](hci__types_8h.md#a589975abd5d9532ba16d15ac21c5e81e)#define BT\_HCI\_EVT\_AUTH\_PAYLOAD\_TIMEOUT\_EXP 0x57

[ 3065](structbt__hci__evt__auth__payload__timeout__exp.md)struct [bt\_hci\_evt\_auth\_payload\_timeout\_exp](structbt__hci__evt__auth__payload__timeout__exp.md) {

[ 3066](structbt__hci__evt__auth__payload__timeout__exp.md#a799bc3c63fe5083d61d8bf152ef4cee7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__auth__payload__timeout__exp.md#a799bc3c63fe5083d61d8bf152ef4cee7);

3067} \_\_packed;

3068

[ 3069](hci__types_8h.md#a150ea8f2095d8510bde3ebd65d521c29)#define BT\_HCI\_ROLE\_CENTRAL 0x00

[ 3070](hci__types_8h.md#a9ca37afd4638ef94cdd55302bd4c99b3)#define BT\_HCI\_ROLE\_PERIPHERAL 0x01

3071

[ 3072](hci__types_8h.md#a2c3c4f81903d1860f21880c7c3cfbaa7)#define BT\_HCI\_EVT\_LE\_CONN\_COMPLETE 0x01

[ 3073](structbt__hci__evt__le__conn__complete.md)struct [bt\_hci\_evt\_le\_conn\_complete](structbt__hci__evt__le__conn__complete.md) {

[ 3074](structbt__hci__evt__le__conn__complete.md#a897981117139c0e53ea7275b689f3799) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__conn__complete.md#a897981117139c0e53ea7275b689f3799);

[ 3075](structbt__hci__evt__le__conn__complete.md#a67618a1efa0149fadc1063a719d5b674) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__conn__complete.md#a67618a1efa0149fadc1063a719d5b674);

[ 3076](structbt__hci__evt__le__conn__complete.md#a8455e714d4333d90c2f117892f3dcd6f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [role](structbt__hci__evt__le__conn__complete.md#a8455e714d4333d90c2f117892f3dcd6f);

[ 3077](structbt__hci__evt__le__conn__complete.md#a97e1aaa10832292ddfe4ee6731ef8999) [bt\_addr\_le\_t](structbt__addr__le__t.md) [peer\_addr](structbt__hci__evt__le__conn__complete.md#a97e1aaa10832292ddfe4ee6731ef8999);

[ 3078](structbt__hci__evt__le__conn__complete.md#abe4bc0407d0295329631cb14672a7ee7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__hci__evt__le__conn__complete.md#abe4bc0407d0295329631cb14672a7ee7);

[ 3079](structbt__hci__evt__le__conn__complete.md#ab60cb42ecc83632c61656cd352b71cbe) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [latency](structbt__hci__evt__le__conn__complete.md#ab60cb42ecc83632c61656cd352b71cbe);

[ 3080](structbt__hci__evt__le__conn__complete.md#a4a90c9824d167b6c45b301e18bfe7f17) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [supv\_timeout](structbt__hci__evt__le__conn__complete.md#a4a90c9824d167b6c45b301e18bfe7f17);

[ 3081](structbt__hci__evt__le__conn__complete.md#a3fff4c3b30da5922f75d36d97fdeee33) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [clock\_accuracy](structbt__hci__evt__le__conn__complete.md#a3fff4c3b30da5922f75d36d97fdeee33);

3082} \_\_packed;

3083

[ 3084](hci__types_8h.md#a56f7acd075e03694d966d949f637946c)#define BT\_HCI\_LE\_RSSI\_NOT\_AVAILABLE 0x7F

3085

[ 3086](hci__types_8h.md#a1a93b78bdbb29982d989aea5eae5ec19)#define BT\_HCI\_EVT\_LE\_ADVERTISING\_REPORT 0x02

[ 3087](structbt__hci__evt__le__advertising__info.md)struct [bt\_hci\_evt\_le\_advertising\_info](structbt__hci__evt__le__advertising__info.md) {

[ 3088](structbt__hci__evt__le__advertising__info.md#a5943685ccd3491a883ba9450f700bb86) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [evt\_type](structbt__hci__evt__le__advertising__info.md#a5943685ccd3491a883ba9450f700bb86);

[ 3089](structbt__hci__evt__le__advertising__info.md#a1d6863f1a601a2df9d772e3cc1fec118) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__hci__evt__le__advertising__info.md#a1d6863f1a601a2df9d772e3cc1fec118);

[ 3090](structbt__hci__evt__le__advertising__info.md#a11c223103bf89300bd90cb8725746121) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [length](structbt__hci__evt__le__advertising__info.md#a11c223103bf89300bd90cb8725746121);

[ 3091](structbt__hci__evt__le__advertising__info.md#af7d9d720ca67714f2a809e2530a1ff98) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__hci__evt__le__advertising__info.md#af7d9d720ca67714f2a809e2530a1ff98)[0];

3092} \_\_packed;

[ 3093](structbt__hci__evt__le__advertising__report.md)struct [bt\_hci\_evt\_le\_advertising\_report](structbt__hci__evt__le__advertising__report.md) {

[ 3094](structbt__hci__evt__le__advertising__report.md#ac69aab36aa421630357e4c6706c13e75) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_reports](structbt__hci__evt__le__advertising__report.md#ac69aab36aa421630357e4c6706c13e75);

[ 3095](structbt__hci__evt__le__advertising__report.md#a9762be19de1f24be4d4626e7e2f8205d) struct [bt\_hci\_evt\_le\_advertising\_info](structbt__hci__evt__le__advertising__info.md) [adv\_info](structbt__hci__evt__le__advertising__report.md#a9762be19de1f24be4d4626e7e2f8205d)[0];

3096} \_\_packed;

3097

[ 3099](hci__types_8h.md#adcf6bcefe1d8a34f65597730910bab69)#define BT\_HCI\_LE\_INTERVAL\_MIN 0x0006

[ 3100](hci__types_8h.md#a23ce5829beb61d9db40fedfce35c368e)#define BT\_HCI\_LE\_INTERVAL\_MAX 0x0c80

[ 3101](hci__types_8h.md#a9af7ce6ecbd978df6193c4e9c2d8b002)#define BT\_HCI\_LE\_PERIPHERAL\_LATENCY\_MAX 0x01f3

[ 3102](hci__types_8h.md#a03dc93eec388a17c286d50395c683fcb)#define BT\_HCI\_LE\_SUPERVISON\_TIMEOUT\_MIN 0x000a

[ 3103](hci__types_8h.md#a2564ee96b802cb887f67e3cc38f8f400)#define BT\_HCI\_LE\_SUPERVISON\_TIMEOUT\_MAX 0x0c80

3104

[ 3105](hci__types_8h.md#aeef912e71549d4b5a0d8b293074a909c)#define BT\_HCI\_EVT\_LE\_CONN\_UPDATE\_COMPLETE 0x03

[ 3106](structbt__hci__evt__le__conn__update__complete.md)struct [bt\_hci\_evt\_le\_conn\_update\_complete](structbt__hci__evt__le__conn__update__complete.md) {

[ 3107](structbt__hci__evt__le__conn__update__complete.md#ad428bd5e29d40f7551ccdd0747e429d6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__conn__update__complete.md#ad428bd5e29d40f7551ccdd0747e429d6);

[ 3108](structbt__hci__evt__le__conn__update__complete.md#a81c0688a5e3b4b3a4d92fbc756a068d5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__conn__update__complete.md#a81c0688a5e3b4b3a4d92fbc756a068d5);

[ 3109](structbt__hci__evt__le__conn__update__complete.md#a69aa00c0c50978b2aa620aad671119f3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__hci__evt__le__conn__update__complete.md#a69aa00c0c50978b2aa620aad671119f3);

[ 3110](structbt__hci__evt__le__conn__update__complete.md#ade2421709a35e0cd0fce3a4d992470c3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [latency](structbt__hci__evt__le__conn__update__complete.md#ade2421709a35e0cd0fce3a4d992470c3);

[ 3111](structbt__hci__evt__le__conn__update__complete.md#aca728975619a10a6e3280b127b59f2f1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [supv\_timeout](structbt__hci__evt__le__conn__update__complete.md#aca728975619a10a6e3280b127b59f2f1);

3112} \_\_packed;

3113

[ 3114](hci__types_8h.md#a8b1653caabce8474fba132343aa62f56)#define BT\_HCI\_EVT\_LE\_REMOTE\_FEAT\_COMPLETE 0x04

[ 3115](structbt__hci__evt__le__remote__feat__complete.md)struct [bt\_hci\_evt\_le\_remote\_feat\_complete](structbt__hci__evt__le__remote__feat__complete.md) {

[ 3116](structbt__hci__evt__le__remote__feat__complete.md#a8a80bade7644f986fec41462843d8319) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__remote__feat__complete.md#a8a80bade7644f986fec41462843d8319);

[ 3117](structbt__hci__evt__le__remote__feat__complete.md#a9a0da26d9415169f02b6c9472120afe7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__remote__feat__complete.md#a9a0da26d9415169f02b6c9472120afe7);

[ 3118](structbt__hci__evt__le__remote__feat__complete.md#a61101c21e317aa07b08725a7ffbb4b81) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [features](structbt__hci__evt__le__remote__feat__complete.md#a61101c21e317aa07b08725a7ffbb4b81)[8];

3119} \_\_packed;

3120

[ 3121](hci__types_8h.md#a9efb73da285829cde0e4c1ac28a48f1a)#define BT\_HCI\_EVT\_LE\_LTK\_REQUEST 0x05

[ 3122](structbt__hci__evt__le__ltk__request.md)struct [bt\_hci\_evt\_le\_ltk\_request](structbt__hci__evt__le__ltk__request.md) {

[ 3123](structbt__hci__evt__le__ltk__request.md#aed00ae384cb7d0deace8d0cc0f8e0068) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__ltk__request.md#aed00ae384cb7d0deace8d0cc0f8e0068);

[ 3124](structbt__hci__evt__le__ltk__request.md#a765cba614cd7a972156b6361536b753f) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [rand](structbt__hci__evt__le__ltk__request.md#a765cba614cd7a972156b6361536b753f);

[ 3125](structbt__hci__evt__le__ltk__request.md#a54d5cbde249349337595085c6c3cabad) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [ediv](structbt__hci__evt__le__ltk__request.md#a54d5cbde249349337595085c6c3cabad);

3126} \_\_packed;

3127

[ 3128](hci__types_8h.md#a77072c10df87395e7e649307b975fb69)#define BT\_HCI\_EVT\_LE\_CONN\_PARAM\_REQ 0x06

[ 3129](structbt__hci__evt__le__conn__param__req.md)struct [bt\_hci\_evt\_le\_conn\_param\_req](structbt__hci__evt__le__conn__param__req.md) {

[ 3130](structbt__hci__evt__le__conn__param__req.md#a4746a001a070f152a3c1c870a7e74df1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__conn__param__req.md#a4746a001a070f152a3c1c870a7e74df1);

[ 3131](structbt__hci__evt__le__conn__param__req.md#a9a9dfc026feb46337b0a36920204b24e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval\_min](structbt__hci__evt__le__conn__param__req.md#a9a9dfc026feb46337b0a36920204b24e);

[ 3132](structbt__hci__evt__le__conn__param__req.md#a0ed70d1a89f270073f78823d38af6ac9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval\_max](structbt__hci__evt__le__conn__param__req.md#a0ed70d1a89f270073f78823d38af6ac9);

[ 3133](structbt__hci__evt__le__conn__param__req.md#a9f61f0a3e6b6d2e2c6af2f4aef625b75) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [latency](structbt__hci__evt__le__conn__param__req.md#a9f61f0a3e6b6d2e2c6af2f4aef625b75);

[ 3134](structbt__hci__evt__le__conn__param__req.md#ae34de4a3d3e3e4686391eb9d9585dc87) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structbt__hci__evt__le__conn__param__req.md#ae34de4a3d3e3e4686391eb9d9585dc87);

3135} \_\_packed;

3136

[ 3137](hci__types_8h.md#a064cf9e32616c6f94041d138a5bf4819)#define BT\_HCI\_EVT\_LE\_DATA\_LEN\_CHANGE 0x07

[ 3138](structbt__hci__evt__le__data__len__change.md)struct [bt\_hci\_evt\_le\_data\_len\_change](structbt__hci__evt__le__data__len__change.md) {

[ 3139](structbt__hci__evt__le__data__len__change.md#a62ebc2f337f23f678c651bf3a276a2a7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__data__len__change.md#a62ebc2f337f23f678c651bf3a276a2a7);

[ 3140](structbt__hci__evt__le__data__len__change.md#ae5ce481170336acafbe85687c672281b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_tx\_octets](structbt__hci__evt__le__data__len__change.md#ae5ce481170336acafbe85687c672281b);

[ 3141](structbt__hci__evt__le__data__len__change.md#a8264e7ec4aa37e9a699f81d0c56afa40) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_tx\_time](structbt__hci__evt__le__data__len__change.md#a8264e7ec4aa37e9a699f81d0c56afa40);

[ 3142](structbt__hci__evt__le__data__len__change.md#a60ecd89a8bbf06ae55b577e3d708d16f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_rx\_octets](structbt__hci__evt__le__data__len__change.md#a60ecd89a8bbf06ae55b577e3d708d16f);

[ 3143](structbt__hci__evt__le__data__len__change.md#a90771e400b998565e7a8bbf4288edd01) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_rx\_time](structbt__hci__evt__le__data__len__change.md#a90771e400b998565e7a8bbf4288edd01);

3144} \_\_packed;

3145

[ 3146](hci__types_8h.md#abe39909eb984dd6edd1220f9c6744546)#define BT\_HCI\_EVT\_LE\_P256\_PUBLIC\_KEY\_COMPLETE 0x08

[ 3147](structbt__hci__evt__le__p256__public__key__complete.md)struct [bt\_hci\_evt\_le\_p256\_public\_key\_complete](structbt__hci__evt__le__p256__public__key__complete.md) {

[ 3148](structbt__hci__evt__le__p256__public__key__complete.md#a57d51fca3a707b445db2534d1e175241) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__p256__public__key__complete.md#a57d51fca3a707b445db2534d1e175241);

[ 3149](structbt__hci__evt__le__p256__public__key__complete.md#af482f81d438b878fb826edbac8d84833) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key](structbt__hci__evt__le__p256__public__key__complete.md#af482f81d438b878fb826edbac8d84833)[64];

3150} \_\_packed;

3151

[ 3152](hci__types_8h.md#a8ab77f497135e365fb9e895dc2d4d453)#define BT\_HCI\_EVT\_LE\_GENERATE\_DHKEY\_COMPLETE 0x09

[ 3153](structbt__hci__evt__le__generate__dhkey__complete.md)struct [bt\_hci\_evt\_le\_generate\_dhkey\_complete](structbt__hci__evt__le__generate__dhkey__complete.md) {

[ 3154](structbt__hci__evt__le__generate__dhkey__complete.md#a3d10643dd45a71b71d35dfa455ed8590) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__generate__dhkey__complete.md#a3d10643dd45a71b71d35dfa455ed8590);

[ 3155](structbt__hci__evt__le__generate__dhkey__complete.md#a8cd8ece786c1443ed43bd3b8fcd4d9bf) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dhkey](structbt__hci__evt__le__generate__dhkey__complete.md#a8cd8ece786c1443ed43bd3b8fcd4d9bf)[32];

3156} \_\_packed;

3157

[ 3158](hci__types_8h.md#a292de9ec009a80e23308ead618656b4f)#define BT\_HCI\_EVT\_LE\_ENH\_CONN\_COMPLETE 0x0a

[ 3159](structbt__hci__evt__le__enh__conn__complete.md)struct [bt\_hci\_evt\_le\_enh\_conn\_complete](structbt__hci__evt__le__enh__conn__complete.md) {

[ 3160](structbt__hci__evt__le__enh__conn__complete.md#ae26575416658bf285c45f57ddf426eb2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__enh__conn__complete.md#ae26575416658bf285c45f57ddf426eb2);

[ 3161](structbt__hci__evt__le__enh__conn__complete.md#a13ceff445de6a89f6ea0e832e8b3fba9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__enh__conn__complete.md#a13ceff445de6a89f6ea0e832e8b3fba9);

[ 3162](structbt__hci__evt__le__enh__conn__complete.md#af24298f8c1d58882b4962a14086fc5c7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [role](structbt__hci__evt__le__enh__conn__complete.md#af24298f8c1d58882b4962a14086fc5c7);

[ 3163](structbt__hci__evt__le__enh__conn__complete.md#a4906d6991489e95f8c74aacf5ad8c22e) [bt\_addr\_le\_t](structbt__addr__le__t.md) [peer\_addr](structbt__hci__evt__le__enh__conn__complete.md#a4906d6991489e95f8c74aacf5ad8c22e);

[ 3164](structbt__hci__evt__le__enh__conn__complete.md#ab275bcb4a3dd09525b446c01e4e5fdad) [bt\_addr\_t](structbt__addr__t.md) [local\_rpa](structbt__hci__evt__le__enh__conn__complete.md#ab275bcb4a3dd09525b446c01e4e5fdad);

[ 3165](structbt__hci__evt__le__enh__conn__complete.md#a4ece4379733f1ab404fa03f4794192a4) [bt\_addr\_t](structbt__addr__t.md) [peer\_rpa](structbt__hci__evt__le__enh__conn__complete.md#a4ece4379733f1ab404fa03f4794192a4);

[ 3166](structbt__hci__evt__le__enh__conn__complete.md#ac0565ecf0c459275d147933bbdaa9fbc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__hci__evt__le__enh__conn__complete.md#ac0565ecf0c459275d147933bbdaa9fbc);

[ 3167](structbt__hci__evt__le__enh__conn__complete.md#a7276bf433c21ffcd3582463492af107b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [latency](structbt__hci__evt__le__enh__conn__complete.md#a7276bf433c21ffcd3582463492af107b);

[ 3168](structbt__hci__evt__le__enh__conn__complete.md#aa99df131f3fb0330ff8051015d2b78dc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [supv\_timeout](structbt__hci__evt__le__enh__conn__complete.md#aa99df131f3fb0330ff8051015d2b78dc);

[ 3169](structbt__hci__evt__le__enh__conn__complete.md#a5641e5cb17df4613cd85f5ad3ba8541c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [clock\_accuracy](structbt__hci__evt__le__enh__conn__complete.md#a5641e5cb17df4613cd85f5ad3ba8541c);

3170} \_\_packed;

3171

[ 3172](hci__types_8h.md#a417144400fd8d7f5c05e050950c75dab)#define BT\_HCI\_EVT\_LE\_DIRECT\_ADV\_REPORT 0x0b

[ 3173](structbt__hci__evt__le__direct__adv__info.md)struct [bt\_hci\_evt\_le\_direct\_adv\_info](structbt__hci__evt__le__direct__adv__info.md) {

[ 3174](structbt__hci__evt__le__direct__adv__info.md#aed957c96860c5f92f9485ab743ce832b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [evt\_type](structbt__hci__evt__le__direct__adv__info.md#aed957c96860c5f92f9485ab743ce832b);

[ 3175](structbt__hci__evt__le__direct__adv__info.md#a66bbb3e53d84e8c39b216edf91ad131d) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__hci__evt__le__direct__adv__info.md#a66bbb3e53d84e8c39b216edf91ad131d);

[ 3176](structbt__hci__evt__le__direct__adv__info.md#ad4ca2d5395bc4c5b95527ac1491c940e) [bt\_addr\_le\_t](structbt__addr__le__t.md) [dir\_addr](structbt__hci__evt__le__direct__adv__info.md#ad4ca2d5395bc4c5b95527ac1491c940e);

[ 3177](structbt__hci__evt__le__direct__adv__info.md#a013e5d53ed53e4cd0b923a55c68e20bc) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__hci__evt__le__direct__adv__info.md#a013e5d53ed53e4cd0b923a55c68e20bc);

3178} \_\_packed;

[ 3179](structbt__hci__evt__le__direct__adv__report.md)struct [bt\_hci\_evt\_le\_direct\_adv\_report](structbt__hci__evt__le__direct__adv__report.md) {

[ 3180](structbt__hci__evt__le__direct__adv__report.md#ae8d1f96739c8fda8827d1c0521f00f94) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_reports](structbt__hci__evt__le__direct__adv__report.md#ae8d1f96739c8fda8827d1c0521f00f94);

[ 3181](structbt__hci__evt__le__direct__adv__report.md#a82800d58d4c3ed1fca49b6575bd8f957) struct [bt\_hci\_evt\_le\_direct\_adv\_info](structbt__hci__evt__le__direct__adv__info.md) [direct\_adv\_info](structbt__hci__evt__le__direct__adv__report.md#a82800d58d4c3ed1fca49b6575bd8f957)[0];

3182} \_\_packed;

3183

[ 3184](hci__types_8h.md#a44f18d799280d47ec09376e7cffd4c40)#define BT\_HCI\_EVT\_LE\_PHY\_UPDATE\_COMPLETE 0x0c

[ 3185](structbt__hci__evt__le__phy__update__complete.md)struct [bt\_hci\_evt\_le\_phy\_update\_complete](structbt__hci__evt__le__phy__update__complete.md) {

[ 3186](structbt__hci__evt__le__phy__update__complete.md#a927a9e6982b29ecd4c3972b19a9bcdc2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__phy__update__complete.md#a927a9e6982b29ecd4c3972b19a9bcdc2);

[ 3187](structbt__hci__evt__le__phy__update__complete.md#a70f472edef3b25fb23490ea6dcce9d43) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__phy__update__complete.md#a70f472edef3b25fb23490ea6dcce9d43);

[ 3188](structbt__hci__evt__le__phy__update__complete.md#ad184e10b7af71582db64ec5d3a66cff9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_phy](structbt__hci__evt__le__phy__update__complete.md#ad184e10b7af71582db64ec5d3a66cff9);

[ 3189](structbt__hci__evt__le__phy__update__complete.md#ad792ffec08aa8e383009e2e353a03fcd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_phy](structbt__hci__evt__le__phy__update__complete.md#ad792ffec08aa8e383009e2e353a03fcd);

3190} \_\_packed;

3191

[ 3192](hci__types_8h.md#ad63fc0c42f0253dfe06b81324a05f505)#define BT\_HCI\_EVT\_LE\_EXT\_ADVERTISING\_REPORT 0x0d

3193

[ 3194](hci__types_8h.md#ae448216e385d4e1175b92e112c941140)#define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_CONN BIT(0)

[ 3195](hci__types_8h.md#a54673fbd23e05fec88e1f6bca6aa70e9)#define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_SCAN BIT(1)

[ 3196](hci__types_8h.md#a1b5738583447011ee63350787236b3b8)#define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DIRECT BIT(2)

[ 3197](hci__types_8h.md#a485843f24c09934b1f15d5274b4a56d5)#define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_SCAN\_RSP BIT(3)

[ 3198](hci__types_8h.md#a0879fbea8bf3acbe56e25f3693c81ad6)#define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_LEGACY BIT(4)

3199

[ 3200](hci__types_8h.md#a9557bf3ea41a526fb9d628d2fd3d5bea)#define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DATA\_STATUS(ev\_type) (((ev\_type) >> 5) & 0x03)

[ 3201](hci__types_8h.md#a85720f3d88c7fa5da9dc9cdffb94ec87)#define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DATA\_STATUS\_COMPLETE 0

[ 3202](hci__types_8h.md#ab7842a3081c9bf5288275b57337955f2)#define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DATA\_STATUS\_PARTIAL 1

[ 3203](hci__types_8h.md#abf119f5606440c075e61abcbfaa683c6)#define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DATA\_STATUS\_INCOMPLETE 2

[ 3204](hci__types_8h.md#ad9bcda2a43eed7e73112f2ef84cc6183)#define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DATA\_STATUS\_RX\_FAILED 0xFF

3205

3206/\* Advertising Coding Selection extended advertising report PHY values.

3207 \* Only used when Kconfig BT\_EXT\_ADV\_CODING\_SELECTION is enabled.

3208 \*/

[ 3209](hci__types_8h.md#a4e3752dfde6a1f6ce6c7561b6c19657c)#define BT\_HCI\_LE\_ADV\_EVT\_PHY\_1M 0x01

[ 3210](hci__types_8h.md#a0eae639d3066358da815743aa7ba2933)#define BT\_HCI\_LE\_ADV\_EVT\_PHY\_2M 0x02

[ 3211](hci__types_8h.md#a51fd268794a726f7d9fa2fb4ce937507)#define BT\_HCI\_LE\_ADV\_EVT\_PHY\_CODED\_S8 0x03

[ 3212](hci__types_8h.md#a865ad7eefd0051e7965bd5e391bf852c)#define BT\_HCI\_LE\_ADV\_EVT\_PHY\_CODED\_S2 0x04

3213

[ 3214](structbt__hci__evt__le__ext__advertising__info.md)struct [bt\_hci\_evt\_le\_ext\_advertising\_info](structbt__hci__evt__le__ext__advertising__info.md) {

[ 3215](structbt__hci__evt__le__ext__advertising__info.md#a040c27dbcb337162f7ca857b8cb84cfe) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [evt\_type](structbt__hci__evt__le__ext__advertising__info.md#a040c27dbcb337162f7ca857b8cb84cfe);

[ 3216](structbt__hci__evt__le__ext__advertising__info.md#acec6858e41ae1b44a2a2ee6d6dbc294d) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__hci__evt__le__ext__advertising__info.md#acec6858e41ae1b44a2a2ee6d6dbc294d);

[ 3217](structbt__hci__evt__le__ext__advertising__info.md#a088f0e6ea0dfbad25d5f72d0741f7d6d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [prim\_phy](structbt__hci__evt__le__ext__advertising__info.md#a088f0e6ea0dfbad25d5f72d0741f7d6d);

[ 3218](structbt__hci__evt__le__ext__advertising__info.md#af4d863e12e6f8f19426a14af292fa6d2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sec\_phy](structbt__hci__evt__le__ext__advertising__info.md#af4d863e12e6f8f19426a14af292fa6d2);

[ 3219](structbt__hci__evt__le__ext__advertising__info.md#a5b4d4adff4d97c06311a76abd9847727) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__hci__evt__le__ext__advertising__info.md#a5b4d4adff4d97c06311a76abd9847727);

[ 3220](structbt__hci__evt__le__ext__advertising__info.md#a39217e77e495e8c4c6288917f8e4d2dc) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__hci__evt__le__ext__advertising__info.md#a39217e77e495e8c4c6288917f8e4d2dc);

[ 3221](structbt__hci__evt__le__ext__advertising__info.md#a6213edbc3ae30f02a6bf2d8e069cd035) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__hci__evt__le__ext__advertising__info.md#a6213edbc3ae30f02a6bf2d8e069cd035);

[ 3222](structbt__hci__evt__le__ext__advertising__info.md#a7da4e49c49eccbf009491bb7da01e111) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__hci__evt__le__ext__advertising__info.md#a7da4e49c49eccbf009491bb7da01e111);

[ 3223](structbt__hci__evt__le__ext__advertising__info.md#a37f4e4981566b43d6e7c7dfffc5b13fb) [bt\_addr\_le\_t](structbt__addr__le__t.md) [direct\_addr](structbt__hci__evt__le__ext__advertising__info.md#a37f4e4981566b43d6e7c7dfffc5b13fb);

[ 3224](structbt__hci__evt__le__ext__advertising__info.md#a20ca10813f6b3aaba2756a5fe00d3878) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [length](structbt__hci__evt__le__ext__advertising__info.md#a20ca10813f6b3aaba2756a5fe00d3878);

[ 3225](structbt__hci__evt__le__ext__advertising__info.md#a9e5536277b0132c8374147677a787b68) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__hci__evt__le__ext__advertising__info.md#a9e5536277b0132c8374147677a787b68)[0];

3226} \_\_packed;

[ 3227](structbt__hci__evt__le__ext__advertising__report.md)struct [bt\_hci\_evt\_le\_ext\_advertising\_report](structbt__hci__evt__le__ext__advertising__report.md) {

[ 3228](structbt__hci__evt__le__ext__advertising__report.md#a72fc9736934b415e88c51a1f96179871) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_reports](structbt__hci__evt__le__ext__advertising__report.md#a72fc9736934b415e88c51a1f96179871);

[ 3229](structbt__hci__evt__le__ext__advertising__report.md#a84b9c47a79ccea04198721e2f05ac1a8) struct [bt\_hci\_evt\_le\_ext\_advertising\_info](structbt__hci__evt__le__ext__advertising__info.md) [adv\_info](structbt__hci__evt__le__ext__advertising__report.md#a84b9c47a79ccea04198721e2f05ac1a8)[0];

3230} \_\_packed;

3231

[ 3232](hci__types_8h.md#a8c721c9e5df496900f661755aff7cbd6)#define BT\_HCI\_EVT\_LE\_PER\_ADV\_SYNC\_ESTABLISHED 0x0e

[ 3233](structbt__hci__evt__le__per__adv__sync__established.md)struct [bt\_hci\_evt\_le\_per\_adv\_sync\_established](structbt__hci__evt__le__per__adv__sync__established.md) {

[ 3234](structbt__hci__evt__le__per__adv__sync__established.md#a9ebe918fee3121168dc5b45e64aaf263) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__per__adv__sync__established.md#a9ebe918fee3121168dc5b45e64aaf263);

[ 3235](structbt__hci__evt__le__per__adv__sync__established.md#a3af8529a858992f347ce9570c5696133) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__per__adv__sync__established.md#a3af8529a858992f347ce9570c5696133);

[ 3236](structbt__hci__evt__le__per__adv__sync__established.md#ab11929ef8d3c71c6f2cb7c549be21282) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__hci__evt__le__per__adv__sync__established.md#ab11929ef8d3c71c6f2cb7c549be21282);

[ 3237](structbt__hci__evt__le__per__adv__sync__established.md#adf65527ea968f4ece37d7e3c91c795d1) [bt\_addr\_le\_t](structbt__addr__le__t.md) [adv\_addr](structbt__hci__evt__le__per__adv__sync__established.md#adf65527ea968f4ece37d7e3c91c795d1);

[ 3238](structbt__hci__evt__le__per__adv__sync__established.md#ab7ce6f56a69b54f02cde8fdae6860e42) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__evt__le__per__adv__sync__established.md#ab7ce6f56a69b54f02cde8fdae6860e42);

[ 3239](structbt__hci__evt__le__per__adv__sync__established.md#a4873b917a5bc140bb2f04ad2bee5dd69) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__hci__evt__le__per__adv__sync__established.md#a4873b917a5bc140bb2f04ad2bee5dd69);

[ 3240](structbt__hci__evt__le__per__adv__sync__established.md#aee68069899cc10bc38ad9fb95cf9b7b7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [clock\_accuracy](structbt__hci__evt__le__per__adv__sync__established.md#aee68069899cc10bc38ad9fb95cf9b7b7);

3241} \_\_packed;

3242

[ 3243](hci__types_8h.md#a31fc096530a89e63d4967d7ddd85b753)#define BT\_HCI\_EVT\_LE\_PER\_ADVERTISING\_REPORT 0x0f

[ 3244](structbt__hci__evt__le__per__advertising__report.md)struct [bt\_hci\_evt\_le\_per\_advertising\_report](structbt__hci__evt__le__per__advertising__report.md) {

[ 3245](structbt__hci__evt__le__per__advertising__report.md#af81ce5bb18ef7fa1d94d00412886b081) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__per__advertising__report.md#af81ce5bb18ef7fa1d94d00412886b081);

[ 3246](structbt__hci__evt__le__per__advertising__report.md#a3a09aca94284a9e4af765d4da543698e) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__hci__evt__le__per__advertising__report.md#a3a09aca94284a9e4af765d4da543698e);

[ 3247](structbt__hci__evt__le__per__advertising__report.md#af874c29b89326877b499f6be1052a626) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__hci__evt__le__per__advertising__report.md#af874c29b89326877b499f6be1052a626);

[ 3248](structbt__hci__evt__le__per__advertising__report.md#aa683d1a4bd3a851f26b3028f566b76e4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__hci__evt__le__per__advertising__report.md#aa683d1a4bd3a851f26b3028f566b76e4);

[ 3249](structbt__hci__evt__le__per__advertising__report.md#abf23b23a12cbfeb7f996e71e2fe8b11c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_status](structbt__hci__evt__le__per__advertising__report.md#abf23b23a12cbfeb7f996e71e2fe8b11c);

[ 3250](structbt__hci__evt__le__per__advertising__report.md#a0ab1d3c5d7eb1487862451cc65c66a76) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [length](structbt__hci__evt__le__per__advertising__report.md#a0ab1d3c5d7eb1487862451cc65c66a76);

[ 3251](structbt__hci__evt__le__per__advertising__report.md#a1f9cdfc01e46e59e957b0c557bae620a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__hci__evt__le__per__advertising__report.md#a1f9cdfc01e46e59e957b0c557bae620a)[0];

3252} \_\_packed;

3253

[ 3254](hci__types_8h.md#ab303042eabbeb133e202bdcfbd38666c)#define BT\_HCI\_EVT\_LE\_PER\_ADV\_SYNC\_LOST 0x10

[ 3255](structbt__hci__evt__le__per__adv__sync__lost.md)struct [bt\_hci\_evt\_le\_per\_adv\_sync\_lost](structbt__hci__evt__le__per__adv__sync__lost.md) {

[ 3256](structbt__hci__evt__le__per__adv__sync__lost.md#a286d534634411da53a2bda8cdfb077f8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__per__adv__sync__lost.md#a286d534634411da53a2bda8cdfb077f8);

3257} \_\_packed;

3258

[ 3259](hci__types_8h.md#a7234c851946c6025aa850c9bf28faab0)#define BT\_HCI\_EVT\_LE\_SCAN\_TIMEOUT 0x11

3260

[ 3261](hci__types_8h.md#a398afcbdb732fe76ec01db1393721ab2)#define BT\_HCI\_EVT\_LE\_ADV\_SET\_TERMINATED 0x12

[ 3262](structbt__hci__evt__le__adv__set__terminated.md)struct [bt\_hci\_evt\_le\_adv\_set\_terminated](structbt__hci__evt__le__adv__set__terminated.md) {

[ 3263](structbt__hci__evt__le__adv__set__terminated.md#a583409e2dc912af2bd5e83124fce3a72) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__adv__set__terminated.md#a583409e2dc912af2bd5e83124fce3a72);

[ 3264](structbt__hci__evt__le__adv__set__terminated.md#af35564406269144cfa2532cd510aa0bd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_handle](structbt__hci__evt__le__adv__set__terminated.md#af35564406269144cfa2532cd510aa0bd);

[ 3265](structbt__hci__evt__le__adv__set__terminated.md#af2503ee8e1c9add6927fa65b69c48551) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__evt__le__adv__set__terminated.md#af2503ee8e1c9add6927fa65b69c48551);

[ 3266](structbt__hci__evt__le__adv__set__terminated.md#a192f13d6223e437261a225e6b28d04db) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_completed\_ext\_adv\_evts](structbt__hci__evt__le__adv__set__terminated.md#a192f13d6223e437261a225e6b28d04db);

3267} \_\_packed;

3268

[ 3269](hci__types_8h.md#a0ebf19a602a02c00793b3de64392e514)#define BT\_HCI\_EVT\_LE\_SCAN\_REQ\_RECEIVED 0x13

[ 3270](structbt__hci__evt__le__scan__req__received.md)struct [bt\_hci\_evt\_le\_scan\_req\_received](structbt__hci__evt__le__scan__req__received.md) {

[ 3271](structbt__hci__evt__le__scan__req__received.md#a62c6d5e5b7079665c0aea8eb676a0433) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle](structbt__hci__evt__le__scan__req__received.md#a62c6d5e5b7079665c0aea8eb676a0433);

[ 3272](structbt__hci__evt__le__scan__req__received.md#a7dca5ad876dc97859a139d8bd4b207af) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__hci__evt__le__scan__req__received.md#a7dca5ad876dc97859a139d8bd4b207af);

3273} \_\_packed;

3274

[ 3275](hci__types_8h.md#ac8dcea08127aa5ce2a870d64fcc843f1)#define BT\_HCI\_LE\_CHAN\_SEL\_ALGO\_1 0x00

[ 3276](hci__types_8h.md#a7a4b52643c764233427314732896d353)#define BT\_HCI\_LE\_CHAN\_SEL\_ALGO\_2 0x01

3277

[ 3278](hci__types_8h.md#a4f012a8357e5bb17b5dd04128bd39911)#define BT\_HCI\_EVT\_LE\_CHAN\_SEL\_ALGO 0x14

[ 3279](structbt__hci__evt__le__chan__sel__algo.md)struct [bt\_hci\_evt\_le\_chan\_sel\_algo](structbt__hci__evt__le__chan__sel__algo.md) {

[ 3280](structbt__hci__evt__le__chan__sel__algo.md#a16393279e08073dad549e111e610c8e8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__chan__sel__algo.md#a16393279e08073dad549e111e610c8e8);

[ 3281](structbt__hci__evt__le__chan__sel__algo.md#a976a62e81b094a59ce42cb6ad3ce45ac) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [chan\_sel\_algo](structbt__hci__evt__le__chan__sel__algo.md#a976a62e81b094a59ce42cb6ad3ce45ac);

3282} \_\_packed;

3283

[ 3284](hci__types_8h.md#ac1ce16d42df9eb71860e51a843dbc943)#define BT\_HCI\_LE\_CTE\_CRC\_OK 0x0

[ 3285](hci__types_8h.md#a3f787f516c3cc233fc700c08552a4034)#define BT\_HCI\_LE\_CTE\_CRC\_ERR\_CTE\_BASED\_TIME 0x1

[ 3286](hci__types_8h.md#a478bc1be161e0b1eb05667bc8b6c9ae5)#define BT\_HCI\_LE\_CTE\_CRC\_ERR\_CTE\_BASED\_OTHER 0x2

[ 3287](hci__types_8h.md#a3bc1e15287e6173d45b7d1e981d6e90e)#define BT\_HCI\_LE\_CTE\_INSUFFICIENT\_RESOURCES 0xFF

3288

[ 3289](hci__types_8h.md#a87364c12ecac6b05681469c9450f887e)#define B\_HCI\_LE\_CTE\_REPORT\_SAMPLE\_COUNT\_MIN 0x9

[ 3290](hci__types_8h.md#a9693358ac3b7d9da498ca557fa0d1410)#define B\_HCI\_LE\_CTE\_REPORT\_SAMPLE\_COUNT\_MAX 0x52

3291

[ 3292](hci__types_8h.md#a40156c4680916b289b00b1546e0d5bb0)#define BT\_HCI\_LE\_CTE\_REPORT\_NO\_VALID\_SAMPLE 0x80

3293

[ 3294](hci__types_8h.md#a04c4a4567eaad7c592f2181e47768522)#define BT\_HCI\_EVT\_LE\_CONNECTIONLESS\_IQ\_REPORT 0x15

[ 3295](structbt__hci__le__iq__sample.md)struct [bt\_hci\_le\_iq\_sample](structbt__hci__le__iq__sample.md) {

[ 3296](structbt__hci__le__iq__sample.md#aacf452456eecd4ad4dab083593b11104) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [i](structbt__hci__le__iq__sample.md#aacf452456eecd4ad4dab083593b11104);

[ 3297](structbt__hci__le__iq__sample.md#a775b6e0ab1842594bc00998faec613f3) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [q](structbt__hci__le__iq__sample.md#a775b6e0ab1842594bc00998faec613f3);

3298};

3299

[ 3300](structbt__hci__evt__le__connectionless__iq__report.md)struct [bt\_hci\_evt\_le\_connectionless\_iq\_report](structbt__hci__evt__le__connectionless__iq__report.md) {

[ 3301](structbt__hci__evt__le__connectionless__iq__report.md#a36f853d29b8dae1dd393546bbdec5ae2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sync\_handle](structbt__hci__evt__le__connectionless__iq__report.md#a36f853d29b8dae1dd393546bbdec5ae2);

[ 3302](structbt__hci__evt__le__connectionless__iq__report.md#af50e710884a17191d22f652eaf5788fd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [chan\_idx](structbt__hci__evt__le__connectionless__iq__report.md#af50e710884a17191d22f652eaf5788fd);

[ 3303](structbt__hci__evt__le__connectionless__iq__report.md#a09112f3711aca00b56045c46958c0992) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [rssi](structbt__hci__evt__le__connectionless__iq__report.md#a09112f3711aca00b56045c46958c0992);

[ 3304](structbt__hci__evt__le__connectionless__iq__report.md#af8c2055666a97f3c8d95747c59515c31) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rssi\_ant\_id](structbt__hci__evt__le__connectionless__iq__report.md#af8c2055666a97f3c8d95747c59515c31);

[ 3305](structbt__hci__evt__le__connectionless__iq__report.md#a6b11b00199b002129c569cfec6e83174) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__hci__evt__le__connectionless__iq__report.md#a6b11b00199b002129c569cfec6e83174);

[ 3306](structbt__hci__evt__le__connectionless__iq__report.md#a9d9f0cfe343d81c44e8342b81e2a0608) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [slot\_durations](structbt__hci__evt__le__connectionless__iq__report.md#a9d9f0cfe343d81c44e8342b81e2a0608);

[ 3307](structbt__hci__evt__le__connectionless__iq__report.md#ab6fb0f6e32e32a3364ae79d867d9e640) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_status](structbt__hci__evt__le__connectionless__iq__report.md#ab6fb0f6e32e32a3364ae79d867d9e640);

[ 3308](structbt__hci__evt__le__connectionless__iq__report.md#abfeb0aaa411464bbd7bca927219144fb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [per\_evt\_counter](structbt__hci__evt__le__connectionless__iq__report.md#abfeb0aaa411464bbd7bca927219144fb);

[ 3309](structbt__hci__evt__le__connectionless__iq__report.md#a39109ea3f657d0566a73c7ca81bdd2b1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sample\_count](structbt__hci__evt__le__connectionless__iq__report.md#a39109ea3f657d0566a73c7ca81bdd2b1);

[ 3310](structbt__hci__evt__le__connectionless__iq__report.md#a1a81f2c8653d85dc29582eed67b4a2a8) struct [bt\_hci\_le\_iq\_sample](structbt__hci__le__iq__sample.md) [sample](structbt__hci__evt__le__connectionless__iq__report.md#a1a81f2c8653d85dc29582eed67b4a2a8)[0];

3311} \_\_packed;

3312

[ 3313](hci__types_8h.md#ace41ae5ec2a8f036aabf83ac94937a8b)#define BT\_HCI\_EVT\_LE\_CONNECTION\_IQ\_REPORT 0x16

[ 3314](structbt__hci__evt__le__connection__iq__report.md)struct [bt\_hci\_evt\_le\_connection\_iq\_report](structbt__hci__evt__le__connection__iq__report.md) {

[ 3315](structbt__hci__evt__le__connection__iq__report.md#a446f4eab3db19452a84023a676333d1d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__evt__le__connection__iq__report.md#a446f4eab3db19452a84023a676333d1d);

[ 3316](structbt__hci__evt__le__connection__iq__report.md#aa052e03491647acc9f7a6dc7d91cedcc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_phy](structbt__hci__evt__le__connection__iq__report.md#aa052e03491647acc9f7a6dc7d91cedcc);

[ 3317](structbt__hci__evt__le__connection__iq__report.md#ac01a14c591c8bd8e6313aff021ca8d61) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_chan\_idx](structbt__hci__evt__le__connection__iq__report.md#ac01a14c591c8bd8e6313aff021ca8d61);

[ 3318](structbt__hci__evt__le__connection__iq__report.md#a49e63523f7219174540666c7e5ab3550) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [rssi](structbt__hci__evt__le__connection__iq__report.md#a49e63523f7219174540666c7e5ab3550);

[ 3319](structbt__hci__evt__le__connection__iq__report.md#a135498a4abae604967f94840e2f88d2c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rssi\_ant\_id](structbt__hci__evt__le__connection__iq__report.md#a135498a4abae604967f94840e2f88d2c);

[ 3320](structbt__hci__evt__le__connection__iq__report.md#a0188ce28a6c0a2002ae2c64a7bd95e52) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__hci__evt__le__connection__iq__report.md#a0188ce28a6c0a2002ae2c64a7bd95e52);

[ 3321](structbt__hci__evt__le__connection__iq__report.md#a74670ca77bb2be81db2cee613dd9c82b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [slot\_durations](structbt__hci__evt__le__connection__iq__report.md#a74670ca77bb2be81db2cee613dd9c82b);

[ 3322](structbt__hci__evt__le__connection__iq__report.md#af66e8f09a4442b658b80a6eb4dd3064b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_status](structbt__hci__evt__le__connection__iq__report.md#af66e8f09a4442b658b80a6eb4dd3064b);

[ 3323](structbt__hci__evt__le__connection__iq__report.md#a1f388ba96bd52f9ce0f68bacb2945ed8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_evt\_counter](structbt__hci__evt__le__connection__iq__report.md#a1f388ba96bd52f9ce0f68bacb2945ed8);

[ 3324](structbt__hci__evt__le__connection__iq__report.md#a801dd9373935ba06175ac52237fea759) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sample\_count](structbt__hci__evt__le__connection__iq__report.md#a801dd9373935ba06175ac52237fea759);

[ 3325](structbt__hci__evt__le__connection__iq__report.md#a5acc2683312523a1137db7897a7373a6) struct [bt\_hci\_le\_iq\_sample](structbt__hci__le__iq__sample.md) [sample](structbt__hci__evt__le__connection__iq__report.md#a5acc2683312523a1137db7897a7373a6)[0];

3326} \_\_packed;

3327

[ 3328](hci__types_8h.md#a5e0814f9ca6e7fbc78b0778634ff075d)#define BT\_HCI\_CTE\_REQ\_STATUS\_RSP\_WITHOUT\_CTE 0x0

3329

[ 3330](hci__types_8h.md#aacaa203f0c8e23c6ca551df0375410e8)#define BT\_HCI\_EVT\_LE\_CTE\_REQUEST\_FAILED 0x17

[ 3331](structbt__hci__evt__le__cte__req__failed.md)struct [bt\_hci\_evt\_le\_cte\_req\_failed](structbt__hci__evt__le__cte__req__failed.md) {

3332 /\* According to BT 5.3 Core Spec the status field may have following

3333 \* values:

3334 \* - BT\_HCI\_CTE\_REQ\_STATUS\_RSP\_WITHOUT\_CTE when received LL\_CTE\_RSP\_PDU without CTE.

3335 \* - Other Controller error code for peer rejected request.

3336 \*/

[ 3337](structbt__hci__evt__le__cte__req__failed.md#a1433f25dee38014dbd2d061b6d75741a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__cte__req__failed.md#a1433f25dee38014dbd2d061b6d75741a);

[ 3338](structbt__hci__evt__le__cte__req__failed.md#aa903954fa411e4ae49a613b4e76219dc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__evt__le__cte__req__failed.md#aa903954fa411e4ae49a613b4e76219dc);

3339} \_\_packed;

3340

[ 3341](hci__types_8h.md#ad61867c0bef6797f7a3b5418c5a4ed5f)#define BT\_HCI\_EVT\_LE\_PAST\_RECEIVED 0x18

[ 3342](structbt__hci__evt__le__past__received.md)struct [bt\_hci\_evt\_le\_past\_received](structbt__hci__evt__le__past__received.md) {

[ 3343](structbt__hci__evt__le__past__received.md#a1b2c229c99d06f44057b88458f168e7c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__past__received.md#a1b2c229c99d06f44057b88458f168e7c);

[ 3344](structbt__hci__evt__le__past__received.md#a1bdbaddb4003cea40738ee540ecb8789) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__evt__le__past__received.md#a1bdbaddb4003cea40738ee540ecb8789);

[ 3345](structbt__hci__evt__le__past__received.md#adaa1e432db60a2529ad6266f16604e15) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [service\_data](structbt__hci__evt__le__past__received.md#adaa1e432db60a2529ad6266f16604e15);

[ 3346](structbt__hci__evt__le__past__received.md#a2cea2f3b9d51ace91ddf63639e821328) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sync\_handle](structbt__hci__evt__le__past__received.md#a2cea2f3b9d51ace91ddf63639e821328);

[ 3347](structbt__hci__evt__le__past__received.md#a110c7cdd2ff1178d1ca686abaae92b05) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_sid](structbt__hci__evt__le__past__received.md#a110c7cdd2ff1178d1ca686abaae92b05);

[ 3348](structbt__hci__evt__le__past__received.md#a3e368e95a6831f823d2efa0c0bc1ef51) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__hci__evt__le__past__received.md#a3e368e95a6831f823d2efa0c0bc1ef51);

[ 3349](structbt__hci__evt__le__past__received.md#aedb668e6f3232b1db9035ea89ccf1b71) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__evt__le__past__received.md#aedb668e6f3232b1db9035ea89ccf1b71);

[ 3350](structbt__hci__evt__le__past__received.md#a41ea6099d3cca1caf37ff518a4e95492) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__hci__evt__le__past__received.md#a41ea6099d3cca1caf37ff518a4e95492);

[ 3351](structbt__hci__evt__le__past__received.md#a00d570636a55c1d84723ad3bc5705d80) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [clock\_accuracy](structbt__hci__evt__le__past__received.md#a00d570636a55c1d84723ad3bc5705d80);

3352} \_\_packed;

3353

[ 3354](hci__types_8h.md#a263d26617702ab43fa8b6717007e1df8)#define BT\_HCI\_EVT\_LE\_CIS\_ESTABLISHED 0x19

[ 3355](structbt__hci__evt__le__cis__established.md)struct [bt\_hci\_evt\_le\_cis\_established](structbt__hci__evt__le__cis__established.md) {

[ 3356](structbt__hci__evt__le__cis__established.md#a4d90dbeda130a6142ff0b7f9e2ee7c16) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__cis__established.md#a4d90dbeda130a6142ff0b7f9e2ee7c16);

[ 3357](structbt__hci__evt__le__cis__established.md#a932e8df0222eb3bcf7bee753414d529e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__evt__le__cis__established.md#a932e8df0222eb3bcf7bee753414d529e);

[ 3358](structbt__hci__evt__le__cis__established.md#ac4e5a2535e3e8d3782adac63a4c5a8d9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cig\_sync\_delay](structbt__hci__evt__le__cis__established.md#ac4e5a2535e3e8d3782adac63a4c5a8d9)[3];

[ 3359](structbt__hci__evt__le__cis__established.md#ae71d6753849ae3c57327c8763cab1802) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cis\_sync\_delay](structbt__hci__evt__le__cis__established.md#ae71d6753849ae3c57327c8763cab1802)[3];

[ 3360](structbt__hci__evt__le__cis__established.md#a877913bb4b9016c64793458de94d84a0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_latency](structbt__hci__evt__le__cis__established.md#a877913bb4b9016c64793458de94d84a0)[3];

[ 3361](structbt__hci__evt__le__cis__established.md#aefb2d4e0458cbe990903a9f449189c30) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_latency](structbt__hci__evt__le__cis__established.md#aefb2d4e0458cbe990903a9f449189c30)[3];

[ 3362](structbt__hci__evt__le__cis__established.md#a53ea1da3f31313ab73b511c72912bd33) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_phy](structbt__hci__evt__le__cis__established.md#a53ea1da3f31313ab73b511c72912bd33);

[ 3363](structbt__hci__evt__le__cis__established.md#a25b84cf026775b582c7944e265ffb0b2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_phy](structbt__hci__evt__le__cis__established.md#a25b84cf026775b582c7944e265ffb0b2);

[ 3364](structbt__hci__evt__le__cis__established.md#a683856418764b1110d5c5fea0494fe1e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [nse](structbt__hci__evt__le__cis__established.md#a683856418764b1110d5c5fea0494fe1e);

[ 3365](structbt__hci__evt__le__cis__established.md#ab6b2d892e3c1e4f6aedee722049b75d3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_bn](structbt__hci__evt__le__cis__established.md#ab6b2d892e3c1e4f6aedee722049b75d3);

[ 3366](structbt__hci__evt__le__cis__established.md#ad0a79bfadd413bf572b697069695c0a5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_bn](structbt__hci__evt__le__cis__established.md#ad0a79bfadd413bf572b697069695c0a5);

[ 3367](structbt__hci__evt__le__cis__established.md#ad0f3bd5f81b660afbc4927a777c2c18e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_ft](structbt__hci__evt__le__cis__established.md#ad0f3bd5f81b660afbc4927a777c2c18e);

[ 3368](structbt__hci__evt__le__cis__established.md#a200afaff044b9eea653d8aee13297dc2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_ft](structbt__hci__evt__le__cis__established.md#a200afaff044b9eea653d8aee13297dc2);

[ 3369](structbt__hci__evt__le__cis__established.md#ae9fdecff4342f25de30165a4531ad703) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [c\_max\_pdu](structbt__hci__evt__le__cis__established.md#ae9fdecff4342f25de30165a4531ad703);

[ 3370](structbt__hci__evt__le__cis__established.md#ae8b195f433570e28e42a5f9d321964de) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [p\_max\_pdu](structbt__hci__evt__le__cis__established.md#ae8b195f433570e28e42a5f9d321964de);

[ 3371](structbt__hci__evt__le__cis__established.md#a0bcdc0d8b3b776660d2e51427f9634dd) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__hci__evt__le__cis__established.md#a0bcdc0d8b3b776660d2e51427f9634dd);

3372} \_\_packed;

3373

[ 3374](hci__types_8h.md#aaa4af1dcdb163a57b0473b43e8107fd7)#define BT\_HCI\_EVT\_LE\_CIS\_REQ 0x1a

[ 3375](structbt__hci__evt__le__cis__req.md)struct [bt\_hci\_evt\_le\_cis\_req](structbt__hci__evt__le__cis__req.md) {

[ 3376](structbt__hci__evt__le__cis__req.md#af8529013adb87340298a89d4727e6867) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [acl\_handle](structbt__hci__evt__le__cis__req.md#af8529013adb87340298a89d4727e6867);

[ 3377](structbt__hci__evt__le__cis__req.md#aeed6f4bf58cdb301d6b784a202722acc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cis\_handle](structbt__hci__evt__le__cis__req.md#aeed6f4bf58cdb301d6b784a202722acc);

[ 3378](structbt__hci__evt__le__cis__req.md#ae0ef0ac224bde55de13df4e5eeaf26be) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cig\_id](structbt__hci__evt__le__cis__req.md#ae0ef0ac224bde55de13df4e5eeaf26be);

[ 3379](structbt__hci__evt__le__cis__req.md#abdf99eeb7a30c8238bbabdcd60a4847a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cis\_id](structbt__hci__evt__le__cis__req.md#abdf99eeb7a30c8238bbabdcd60a4847a);

3380} \_\_packed;

3381

[ 3382](hci__types_8h.md#aade42399ac596746100849328c551259)#define BT\_HCI\_EVT\_LE\_BIG\_COMPLETE 0x1b

[ 3383](structbt__hci__evt__le__big__complete.md)struct [bt\_hci\_evt\_le\_big\_complete](structbt__hci__evt__le__big__complete.md) {

[ 3384](structbt__hci__evt__le__big__complete.md#ad6787806a3622b3bd3da4512bb8ddffe) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__big__complete.md#ad6787806a3622b3bd3da4512bb8ddffe);

[ 3385](structbt__hci__evt__le__big__complete.md#a14eaa705f1df38337722a41e8189f807) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [big\_handle](structbt__hci__evt__le__big__complete.md#a14eaa705f1df38337722a41e8189f807);

[ 3386](structbt__hci__evt__le__big__complete.md#a2847d5fc997f80a3e21b7e03d80c9574) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sync\_delay](structbt__hci__evt__le__big__complete.md#a2847d5fc997f80a3e21b7e03d80c9574)[3];

[ 3387](structbt__hci__evt__le__big__complete.md#a2727d329c37e3b3644cfad02d86abb55) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [latency](structbt__hci__evt__le__big__complete.md#a2727d329c37e3b3644cfad02d86abb55)[3];

[ 3388](structbt__hci__evt__le__big__complete.md#abfa6d6bc135350737451e053aa7d212c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__evt__le__big__complete.md#abfa6d6bc135350737451e053aa7d212c);

[ 3389](structbt__hci__evt__le__big__complete.md#ae77364aafe179588f7b8414292e35f5e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [nse](structbt__hci__evt__le__big__complete.md#ae77364aafe179588f7b8414292e35f5e);

[ 3390](structbt__hci__evt__le__big__complete.md#a2327e42013033767af233d1c2c3acc56) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bn](structbt__hci__evt__le__big__complete.md#a2327e42013033767af233d1c2c3acc56);

[ 3391](structbt__hci__evt__le__big__complete.md#a6c295870732d65002ec21b4b607e7c0b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pto](structbt__hci__evt__le__big__complete.md#a6c295870732d65002ec21b4b607e7c0b);

[ 3392](structbt__hci__evt__le__big__complete.md#a07163dee904412d6d8faca8563a944d9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [irc](structbt__hci__evt__le__big__complete.md#a07163dee904412d6d8faca8563a944d9);

[ 3393](structbt__hci__evt__le__big__complete.md#a8b433ac376e347bf391d4dd804c469f3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_pdu](structbt__hci__evt__le__big__complete.md#a8b433ac376e347bf391d4dd804c469f3);

[ 3394](structbt__hci__evt__le__big__complete.md#a0b0d19d442ed8f1025165c435786ba09) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [iso\_interval](structbt__hci__evt__le__big__complete.md#a0b0d19d442ed8f1025165c435786ba09);

[ 3395](structbt__hci__evt__le__big__complete.md#a995c8fe06ec087f16b771c38171745b1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_bis](structbt__hci__evt__le__big__complete.md#a995c8fe06ec087f16b771c38171745b1);

[ 3396](structbt__hci__evt__le__big__complete.md#af1c8bd66c3dba70df22f8655b4f27925) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__big__complete.md#af1c8bd66c3dba70df22f8655b4f27925)[0];

3397} \_\_packed;

3398

[ 3399](hci__types_8h.md#ac0a1310793a73afda4c2179749df9985)#define BT\_HCI\_EVT\_LE\_BIG\_TERMINATE 0x1c

[ 3400](structbt__hci__evt__le__big__terminate.md)struct [bt\_hci\_evt\_le\_big\_terminate](structbt__hci__evt__le__big__terminate.md) {

[ 3401](structbt__hci__evt__le__big__terminate.md#ad9c9e6d42661366d62d79163fa9ad1c7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [big\_handle](structbt__hci__evt__le__big__terminate.md#ad9c9e6d42661366d62d79163fa9ad1c7);

[ 3402](structbt__hci__evt__le__big__terminate.md#a0303ac64b825f93210dfc70a8a081ea6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reason](structbt__hci__evt__le__big__terminate.md#a0303ac64b825f93210dfc70a8a081ea6);

3403} \_\_packed;

3404

[ 3405](hci__types_8h.md#a8d021615f0b1b2077bbec1f1482b85ef)#define BT\_HCI\_EVT\_LE\_BIG\_SYNC\_ESTABLISHED 0x1d

[ 3406](structbt__hci__evt__le__big__sync__established.md)struct [bt\_hci\_evt\_le\_big\_sync\_established](structbt__hci__evt__le__big__sync__established.md) {

[ 3407](structbt__hci__evt__le__big__sync__established.md#a8feb21ef6eacf45dfc09b09e0bce04b1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__big__sync__established.md#a8feb21ef6eacf45dfc09b09e0bce04b1);

[ 3408](structbt__hci__evt__le__big__sync__established.md#a31a05f8afb69e5885700cc4ad3b161b2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [big\_handle](structbt__hci__evt__le__big__sync__established.md#a31a05f8afb69e5885700cc4ad3b161b2);

[ 3409](structbt__hci__evt__le__big__sync__established.md#aebb25f9a63fa013ec6ef891ca498dbb4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [latency](structbt__hci__evt__le__big__sync__established.md#aebb25f9a63fa013ec6ef891ca498dbb4)[3];

[ 3410](structbt__hci__evt__le__big__sync__established.md#a383dc92f6d16ec971455e20665cd7496) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [nse](structbt__hci__evt__le__big__sync__established.md#a383dc92f6d16ec971455e20665cd7496);

[ 3411](structbt__hci__evt__le__big__sync__established.md#a451466916fbe2f220c277b4b4e62241d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bn](structbt__hci__evt__le__big__sync__established.md#a451466916fbe2f220c277b4b4e62241d);

[ 3412](structbt__hci__evt__le__big__sync__established.md#a6b750de25b2a1afc38995030953364ce) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pto](structbt__hci__evt__le__big__sync__established.md#a6b750de25b2a1afc38995030953364ce);

[ 3413](structbt__hci__evt__le__big__sync__established.md#afd52315dafe02ee28bc26f058b12fe9e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [irc](structbt__hci__evt__le__big__sync__established.md#afd52315dafe02ee28bc26f058b12fe9e);

[ 3414](structbt__hci__evt__le__big__sync__established.md#a13db0d402636a71ed029575c1e5771c5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_pdu](structbt__hci__evt__le__big__sync__established.md#a13db0d402636a71ed029575c1e5771c5);

[ 3415](structbt__hci__evt__le__big__sync__established.md#a610313c11c65faf82e06a121affb8b2b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [iso\_interval](structbt__hci__evt__le__big__sync__established.md#a610313c11c65faf82e06a121affb8b2b);

[ 3416](structbt__hci__evt__le__big__sync__established.md#a2fa405310a8fed0341001b316ca7bd4f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_bis](structbt__hci__evt__le__big__sync__established.md#a2fa405310a8fed0341001b316ca7bd4f);

[ 3417](structbt__hci__evt__le__big__sync__established.md#a48766968cb677614f525ea36551ad6c8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__big__sync__established.md#a48766968cb677614f525ea36551ad6c8)[0];

3418} \_\_packed;

3419

[ 3420](hci__types_8h.md#a9c79430501848b9e75a21020920a8ca8)#define BT\_HCI\_EVT\_LE\_BIG\_SYNC\_LOST 0x1e

[ 3421](structbt__hci__evt__le__big__sync__lost.md)struct [bt\_hci\_evt\_le\_big\_sync\_lost](structbt__hci__evt__le__big__sync__lost.md) {

[ 3422](structbt__hci__evt__le__big__sync__lost.md#ae59a9c18363f7aee67563494d98aa971) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [big\_handle](structbt__hci__evt__le__big__sync__lost.md#ae59a9c18363f7aee67563494d98aa971);

[ 3423](structbt__hci__evt__le__big__sync__lost.md#a02b724a60e71805088aefca9989ad878) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reason](structbt__hci__evt__le__big__sync__lost.md#a02b724a60e71805088aefca9989ad878);

3424} \_\_packed;

3425

[ 3426](hci__types_8h.md#aeb33301a950a9520d7ff706dddb07951)#define BT\_HCI\_EVT\_LE\_REQ\_PEER\_SCA\_COMPLETE 0x1f

[ 3427](structbt__hci__evt__le__req__peer__sca__complete.md)struct [bt\_hci\_evt\_le\_req\_peer\_sca\_complete](structbt__hci__evt__le__req__peer__sca__complete.md) {

[ 3428](structbt__hci__evt__le__req__peer__sca__complete.md#a814d17b8aae9dd68f57402c857ca1810) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__req__peer__sca__complete.md#a814d17b8aae9dd68f57402c857ca1810);

[ 3429](structbt__hci__evt__le__req__peer__sca__complete.md#ab6b648e7f4bff9e84b274e9e22a26166) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__req__peer__sca__complete.md#ab6b648e7f4bff9e84b274e9e22a26166);

[ 3430](structbt__hci__evt__le__req__peer__sca__complete.md#a88f93ead6ec67e1612b1a0e8402a30e7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sca](structbt__hci__evt__le__req__peer__sca__complete.md#a88f93ead6ec67e1612b1a0e8402a30e7);

3431} \_\_packed;

3432

[ 3433](hci__types_8h.md#aff1538e314a97aa4910d4f7066dc4d55)#define BT\_HCI\_LE\_ZONE\_ENTERED\_LOW 0x0

[ 3434](hci__types_8h.md#ab88f3d713f6862c08b73752436ca8b1b)#define BT\_HCI\_LE\_ZONE\_ENTERED\_MIDDLE 0x1

[ 3435](hci__types_8h.md#af7cc15be8165315ee0358ebb517b5e33)#define BT\_HCI\_LE\_ZONE\_ENTERED\_HIGH 0x2

[ 3436](hci__types_8h.md#a0408b7ecb697bd573b2ea7d2c3c93b92)#define BT\_HCI\_LE\_PATH\_LOSS\_UNAVAILABLE 0xFF

3437

[ 3438](hci__types_8h.md#a3e646ec9a2e0baca5126e58368c97995)#define BT\_HCI\_EVT\_LE\_PATH\_LOSS\_THRESHOLD 0x20

[ 3439](structbt__hci__evt__le__path__loss__threshold.md)struct [bt\_hci\_evt\_le\_path\_loss\_threshold](structbt__hci__evt__le__path__loss__threshold.md) {

[ 3440](structbt__hci__evt__le__path__loss__threshold.md#a19b1e37c5e35e1e18424615b5c25d37f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__path__loss__threshold.md#a19b1e37c5e35e1e18424615b5c25d37f);

[ 3441](structbt__hci__evt__le__path__loss__threshold.md#ac2b04c57137dcb6812fda06d4a22402a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [current\_path\_loss](structbt__hci__evt__le__path__loss__threshold.md#ac2b04c57137dcb6812fda06d4a22402a);

[ 3442](structbt__hci__evt__le__path__loss__threshold.md#add7984e06d523bb34e8380dae1710b7f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [zone\_entered](structbt__hci__evt__le__path__loss__threshold.md#add7984e06d523bb34e8380dae1710b7f);

3443} \_\_packed;

3444

3447/\* Local Transmit power changed. \*/

[ 3448](hci__types_8h.md#a443a5a524ec41bf2ea86eab74dd022dc)#define BT\_HCI\_LE\_TX\_POWER\_REPORT\_REASON\_LOCAL\_CHANGED 0x00

3449/\* Remote Transmit power changed. \*/

[ 3450](hci__types_8h.md#a1fbc1b017b13987a017af7cd90bdf708)#define BT\_HCI\_LE\_TX\_POWER\_REPORT\_REASON\_REMOTE\_CHANGED 0x01

3451/\* HCI\_LE\_Read\_Remote\_Transmit\_Power\_Level command completed. \*/

[ 3452](hci__types_8h.md#a268761b9eae9c84f74394a6098f15ee8)#define BT\_HCI\_LE\_TX\_POWER\_REPORT\_REASON\_READ\_REMOTE\_COMPLETED 0x02

3453

[ 3454](hci__types_8h.md#a835280c0bf13ddebf451fef5f08c22d0)#define BT\_HCI\_EVT\_LE\_TRANSMIT\_POWER\_REPORT 0x21

[ 3455](structbt__hci__evt__le__transmit__power__report.md)struct [bt\_hci\_evt\_le\_transmit\_power\_report](structbt__hci__evt__le__transmit__power__report.md) {

[ 3456](structbt__hci__evt__le__transmit__power__report.md#af1629e59dd651e1616b89f4958f47c92) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__transmit__power__report.md#af1629e59dd651e1616b89f4958f47c92);

[ 3457](structbt__hci__evt__le__transmit__power__report.md#a4feadb14800c1b51a9cc523c1d6a9063) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__transmit__power__report.md#a4feadb14800c1b51a9cc523c1d6a9063);

[ 3458](structbt__hci__evt__le__transmit__power__report.md#a341cc0c5cc1ea969e2024b67056a5439) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reason](structbt__hci__evt__le__transmit__power__report.md#a341cc0c5cc1ea969e2024b67056a5439);

[ 3459](structbt__hci__evt__le__transmit__power__report.md#ad6130863713cf31a1cbe33de9fb5428f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__evt__le__transmit__power__report.md#ad6130863713cf31a1cbe33de9fb5428f);

[ 3460](structbt__hci__evt__le__transmit__power__report.md#aa0df9c50a555fa40ed25a14f7b6a5e77) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power\_level](structbt__hci__evt__le__transmit__power__report.md#aa0df9c50a555fa40ed25a14f7b6a5e77);

[ 3461](structbt__hci__evt__le__transmit__power__report.md#a2dc33da8f36cceda362d0c87098b02d6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_power\_level\_flag](structbt__hci__evt__le__transmit__power__report.md#a2dc33da8f36cceda362d0c87098b02d6);

[ 3462](structbt__hci__evt__le__transmit__power__report.md#ac42d60325235f517728ff44385361db2) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [delta](structbt__hci__evt__le__transmit__power__report.md#ac42d60325235f517728ff44385361db2);

3463} \_\_packed;

3464

[ 3465](hci__types_8h.md#a651e36b5529cb7f289721573434154cd)#define BT\_HCI\_EVT\_LE\_BIGINFO\_ADV\_REPORT 0x22

[ 3466](structbt__hci__evt__le__biginfo__adv__report.md)struct [bt\_hci\_evt\_le\_biginfo\_adv\_report](structbt__hci__evt__le__biginfo__adv__report.md) {

[ 3467](structbt__hci__evt__le__biginfo__adv__report.md#a8be20bfc607e6ce34ea75c53e285b0d5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sync\_handle](structbt__hci__evt__le__biginfo__adv__report.md#a8be20bfc607e6ce34ea75c53e285b0d5);

[ 3468](structbt__hci__evt__le__biginfo__adv__report.md#ae68f803bbc3f06e7190f62be98d2fe66) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_bis](structbt__hci__evt__le__biginfo__adv__report.md#ae68f803bbc3f06e7190f62be98d2fe66);

[ 3469](structbt__hci__evt__le__biginfo__adv__report.md#ae28d5378a7e2ef59fabb62a3a430ccc8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [nse](structbt__hci__evt__le__biginfo__adv__report.md#ae28d5378a7e2ef59fabb62a3a430ccc8);

[ 3470](structbt__hci__evt__le__biginfo__adv__report.md#ae92b69ab0bc257d4f50b98e071c6038b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [iso\_interval](structbt__hci__evt__le__biginfo__adv__report.md#ae92b69ab0bc257d4f50b98e071c6038b);

[ 3471](structbt__hci__evt__le__biginfo__adv__report.md#ada35f690706be1c6ee8f40787bbe53e5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bn](structbt__hci__evt__le__biginfo__adv__report.md#ada35f690706be1c6ee8f40787bbe53e5);

[ 3472](structbt__hci__evt__le__biginfo__adv__report.md#af3a871d3de34b90fc2b09b0725caf479) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pto](structbt__hci__evt__le__biginfo__adv__report.md#af3a871d3de34b90fc2b09b0725caf479);

[ 3473](structbt__hci__evt__le__biginfo__adv__report.md#a9c1235653245b517a105570c60ddfa09) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [irc](structbt__hci__evt__le__biginfo__adv__report.md#a9c1235653245b517a105570c60ddfa09);

[ 3474](structbt__hci__evt__le__biginfo__adv__report.md#a12a000c049e85d2b24720d1a362d28df) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_pdu](structbt__hci__evt__le__biginfo__adv__report.md#a12a000c049e85d2b24720d1a362d28df);

[ 3475](structbt__hci__evt__le__biginfo__adv__report.md#a81e236ceb24012bc267f656f20f1f8c4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sdu\_interval](structbt__hci__evt__le__biginfo__adv__report.md#a81e236ceb24012bc267f656f20f1f8c4)[3];

[ 3476](structbt__hci__evt__le__biginfo__adv__report.md#a084c13c4b0c9c8dca0653b56e53a0c74) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_sdu](structbt__hci__evt__le__biginfo__adv__report.md#a084c13c4b0c9c8dca0653b56e53a0c74);

[ 3477](structbt__hci__evt__le__biginfo__adv__report.md#a2301112acf22cf68d6495ff85f0f29bf) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__evt__le__biginfo__adv__report.md#a2301112acf22cf68d6495ff85f0f29bf);

[ 3478](structbt__hci__evt__le__biginfo__adv__report.md#abe0636beae2f51004193ad5f7c9efeef) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [framing](structbt__hci__evt__le__biginfo__adv__report.md#abe0636beae2f51004193ad5f7c9efeef);

[ 3479](structbt__hci__evt__le__biginfo__adv__report.md#ae63eaf93f728109b5fb77ca3179ba99c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [encryption](structbt__hci__evt__le__biginfo__adv__report.md#ae63eaf93f728109b5fb77ca3179ba99c);

3480} \_\_packed;

3481

[ 3483](hci__types_8h.md#a135059b92eba0676689abc78a2f560d3)#define BT\_HCI\_LE\_SUBRATE\_FACTOR\_MIN 0x0001

[ 3484](hci__types_8h.md#a33ce951c9eddfcc5556b0168c14b9769)#define BT\_HCI\_LE\_SUBRATE\_FACTOR\_MAX 0x01f4

[ 3485](hci__types_8h.md#aa2b9a667e0b80a4cf4d8cef9cb022ad4)#define BT\_HCI\_LE\_CONTINUATION\_NUM\_MAX 0x01f3

3486

[ 3487](hci__types_8h.md#a2098d628b6ad185cb29106ef69c3627d)#define BT\_HCI\_EVT\_LE\_SUBRATE\_CHANGE 0x23

[ 3488](structbt__hci__evt__le__subrate__change.md)struct [bt\_hci\_evt\_le\_subrate\_change](structbt__hci__evt__le__subrate__change.md) {

[ 3489](structbt__hci__evt__le__subrate__change.md#aa49286a63d565feaf3d9329cd024ee9f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__subrate__change.md#aa49286a63d565feaf3d9329cd024ee9f);

[ 3490](structbt__hci__evt__le__subrate__change.md#adc08125e663a99c7232d0755c4bd760b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__subrate__change.md#adc08125e663a99c7232d0755c4bd760b);

[ 3491](structbt__hci__evt__le__subrate__change.md#a9387ffe45a856f7f443f5116a59a9ff2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [subrate\_factor](structbt__hci__evt__le__subrate__change.md#a9387ffe45a856f7f443f5116a59a9ff2);

[ 3492](structbt__hci__evt__le__subrate__change.md#a95aaed5f8c93a1d6e8cab4c7ebfad8d7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [peripheral\_latency](structbt__hci__evt__le__subrate__change.md#a95aaed5f8c93a1d6e8cab4c7ebfad8d7);

[ 3493](structbt__hci__evt__le__subrate__change.md#a712b8b818115f1797787aab229040c8a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [continuation\_number](structbt__hci__evt__le__subrate__change.md#a712b8b818115f1797787aab229040c8a);

[ 3494](structbt__hci__evt__le__subrate__change.md#a2ad4a06feeb0d6d36461b4a4e53dfeb1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [supervision\_timeout](structbt__hci__evt__le__subrate__change.md#a2ad4a06feeb0d6d36461b4a4e53dfeb1);

3495} \_\_packed;

3496

[ 3497](hci__types_8h.md#ae5a1301a0fea0ab6c205dab22e39c6c9)#define BT\_HCI\_EVT\_LE\_CIS\_ESTABLISHED\_V2 0x2a

[ 3498](structbt__hci__evt__le__cis__established__v2.md)struct [bt\_hci\_evt\_le\_cis\_established\_v2](structbt__hci__evt__le__cis__established__v2.md) {

[ 3499](structbt__hci__evt__le__cis__established__v2.md#a1f43b72368227f212511bb248b4a0e22) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__cis__established__v2.md#a1f43b72368227f212511bb248b4a0e22);

[ 3500](structbt__hci__evt__le__cis__established__v2.md#a7a7b8303183a916225bb0a3ea11d5480) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__evt__le__cis__established__v2.md#a7a7b8303183a916225bb0a3ea11d5480);

[ 3501](structbt__hci__evt__le__cis__established__v2.md#a754ad7e68821da0bdb8da0bdeb3b4697) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cig\_sync\_delay](structbt__hci__evt__le__cis__established__v2.md#a754ad7e68821da0bdb8da0bdeb3b4697)[3];

[ 3502](structbt__hci__evt__le__cis__established__v2.md#af134783424a77274abac44613bf61264) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cis\_sync\_delay](structbt__hci__evt__le__cis__established__v2.md#af134783424a77274abac44613bf61264)[3];

[ 3503](structbt__hci__evt__le__cis__established__v2.md#ae580ff8c0ef4cd03365cbf1a06aed8bc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_latency](structbt__hci__evt__le__cis__established__v2.md#ae580ff8c0ef4cd03365cbf1a06aed8bc)[3];

[ 3504](structbt__hci__evt__le__cis__established__v2.md#a26b25e1615991977735cbfc679d747f3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_latency](structbt__hci__evt__le__cis__established__v2.md#a26b25e1615991977735cbfc679d747f3)[3];

[ 3505](structbt__hci__evt__le__cis__established__v2.md#a9b7ba96597a5131927e365b7a45f8d6f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_phy](structbt__hci__evt__le__cis__established__v2.md#a9b7ba96597a5131927e365b7a45f8d6f);

[ 3506](structbt__hci__evt__le__cis__established__v2.md#a5a0b08098ac4e6ec93a6ecbbbf4ef587) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_phy](structbt__hci__evt__le__cis__established__v2.md#a5a0b08098ac4e6ec93a6ecbbbf4ef587);

[ 3507](structbt__hci__evt__le__cis__established__v2.md#ac3a87b20b2f10e980639d232a013f702) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [nse](structbt__hci__evt__le__cis__established__v2.md#ac3a87b20b2f10e980639d232a013f702);

[ 3508](structbt__hci__evt__le__cis__established__v2.md#a5f68c3cba98ed96afef0949f6b14ded9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_bn](structbt__hci__evt__le__cis__established__v2.md#a5f68c3cba98ed96afef0949f6b14ded9);

[ 3509](structbt__hci__evt__le__cis__established__v2.md#a64b48b20283415100fc8bdf33edf2b0e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_bn](structbt__hci__evt__le__cis__established__v2.md#a64b48b20283415100fc8bdf33edf2b0e);

[ 3510](structbt__hci__evt__le__cis__established__v2.md#a2de704a032ac2379528991f2d01e6979) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_ft](structbt__hci__evt__le__cis__established__v2.md#a2de704a032ac2379528991f2d01e6979);

[ 3511](structbt__hci__evt__le__cis__established__v2.md#a3b1fc27cca2bc85c36e257aabd8ea612) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_ft](structbt__hci__evt__le__cis__established__v2.md#a3b1fc27cca2bc85c36e257aabd8ea612);

[ 3512](structbt__hci__evt__le__cis__established__v2.md#acd8cf2d2d85b65d839256f3412a4bb43) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [c\_max\_pdu](structbt__hci__evt__le__cis__established__v2.md#acd8cf2d2d85b65d839256f3412a4bb43);

[ 3513](structbt__hci__evt__le__cis__established__v2.md#aeea230245aa75dd7f44bf5a4a286e9a5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [p\_max\_pdu](structbt__hci__evt__le__cis__established__v2.md#aeea230245aa75dd7f44bf5a4a286e9a5);

[ 3514](structbt__hci__evt__le__cis__established__v2.md#a71762f8a31e20b233a252ac974f6d329) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__hci__evt__le__cis__established__v2.md#a71762f8a31e20b233a252ac974f6d329);

[ 3515](structbt__hci__evt__le__cis__established__v2.md#a353409fe069aba91c5372ee8ae6e1b79) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sub\_interval](structbt__hci__evt__le__cis__established__v2.md#a353409fe069aba91c5372ee8ae6e1b79)[3];

[ 3516](structbt__hci__evt__le__cis__established__v2.md#ad054af39ddad854423379b3cc7aafc26) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [c\_max\_sdu](structbt__hci__evt__le__cis__established__v2.md#ad054af39ddad854423379b3cc7aafc26);

[ 3517](structbt__hci__evt__le__cis__established__v2.md#a2a060c0bb2831eb3df0dc8ffb74ecebd) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [p\_max\_sdu](structbt__hci__evt__le__cis__established__v2.md#a2a060c0bb2831eb3df0dc8ffb74ecebd);

[ 3518](structbt__hci__evt__le__cis__established__v2.md#a926a5faeb98a99333310d860da37f6f5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_sdu\_interval](structbt__hci__evt__le__cis__established__v2.md#a926a5faeb98a99333310d860da37f6f5)[3];

[ 3519](structbt__hci__evt__le__cis__established__v2.md#acf30d6a745803fd4e984d66548ceff58) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_sdu\_interval](structbt__hci__evt__le__cis__established__v2.md#acf30d6a745803fd4e984d66548ceff58)[3];

[ 3520](structbt__hci__evt__le__cis__established__v2.md#af59ca6d54ca770ef8334ea091bcc53f6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [framing](structbt__hci__evt__le__cis__established__v2.md#af59ca6d54ca770ef8334ea091bcc53f6);

3521} \_\_packed;

3522

[ 3523](hci__types_8h.md#af457a20ddc90001f8a523a0e3df6a4bd)#define BT\_HCI\_LE\_CS\_INITIATOR\_ROLE\_MASK BIT(0)

[ 3524](hci__types_8h.md#a4c42a75a04962264257c690ba80f6126)#define BT\_HCI\_LE\_CS\_REFLECTOR\_ROLE\_MASK BIT(1)

3525

[ 3526](hci__types_8h.md#a62ab6fbe9acb92c4023f35ae8bb7b14b)#define BT\_HCI\_LE\_CS\_MODES\_SUPPORTED\_MODE\_3\_MASK BIT(0)

3527

[ 3528](hci__types_8h.md#ab7843d7e6463e96bce693b82c3f8cc7d)#define BT\_HCI\_LE\_CS\_RTT\_AA\_ONLY\_N\_10NS\_MASK BIT(0)

[ 3529](hci__types_8h.md#ad701c1822a44a639bf5a576bf291544f)#define BT\_HCI\_LE\_CS\_RTT\_SOUNDING\_N\_10NS\_MASK BIT(1)

[ 3530](hci__types_8h.md#a2135776cd2413e80b3ad653405f0ec67)#define BT\_HCI\_LE\_CS\_RTT\_RANDOM\_PAYLOAD\_N\_10NS\_MASK BIT(2)

3531

[ 3532](hci__types_8h.md#a903505932b23ae60c59fc4f439f8f3ce)#define BT\_HCI\_LE\_CS\_NADM\_SOUNDING\_CAPABILITY\_PHASE\_BASED\_MASK BIT(0)

[ 3533](hci__types_8h.md#a6b64cb407c353d7a143b7483cf16507f)#define BT\_HCI\_LE\_CS\_NADM\_RANDOM\_CAPABILITY\_PHASE\_BASED\_MASK BIT(0)

3534

[ 3535](hci__types_8h.md#ad8742ec8b365df1850b6e5f56c39e655)#define BT\_HCI\_LE\_CS\_SYNC\_PHYS\_2M\_MASK BIT(1)

[ 3536](hci__types_8h.md#aeba1a6050a1ff6ad3864132015063026)#define BT\_HCI\_LE\_CS\_SYNC\_PHYS\_2M\_2BT\_MASK BIT(2)

3537

[ 3538](hci__types_8h.md#a2241cba5ca0dbeb1ea19797654c97397)#define BT\_HCI\_LE\_CS\_SUBFEATURE\_NO\_TX\_FAE\_MASK BIT(1)

[ 3539](hci__types_8h.md#a5a7e8927e6086b70177cc04915d16ff8)#define BT\_HCI\_LE\_CS\_SUBFEATURE\_CHSEL\_ALG\_3C\_MASK BIT(2)

[ 3540](hci__types_8h.md#a4bcdc621f0292fd182f47762a2cf16bb)#define BT\_HCI\_LE\_CS\_SUBFEATURE\_PBR\_FROM\_RTT\_SOUNDING\_SEQ\_MASK BIT(3)

3541

[ 3542](hci__types_8h.md#a85f667356dd1e1d9de288776ec13e721)#define BT\_HCI\_LE\_CS\_T\_IP1\_TIME\_10US\_MASK BIT(0)

[ 3543](hci__types_8h.md#a331eff3b3e89a073b30c9d334014b2da)#define BT\_HCI\_LE\_CS\_T\_IP1\_TIME\_20US\_MASK BIT(1)

[ 3544](hci__types_8h.md#a62112179c80be4546b29bc39f632f619)#define BT\_HCI\_LE\_CS\_T\_IP1\_TIME\_30US\_MASK BIT(2)

[ 3545](hci__types_8h.md#a57232d7cbd988c6d6d01d2462e90a7f5)#define BT\_HCI\_LE\_CS\_T\_IP1\_TIME\_40US\_MASK BIT(3)

[ 3546](hci__types_8h.md#a4aa0365eb6bc4f54bbbd3ebc2b717c41)#define BT\_HCI\_LE\_CS\_T\_IP1\_TIME\_50US\_MASK BIT(4)

[ 3547](hci__types_8h.md#a647ea407f97ea754f3f729ac8a9bbb02)#define BT\_HCI\_LE\_CS\_T\_IP1\_TIME\_60US\_MASK BIT(5)

[ 3548](hci__types_8h.md#a8bd6f366622ed48cea49fc67692349ce)#define BT\_HCI\_LE\_CS\_T\_IP1\_TIME\_80US\_MASK BIT(6)

3549

[ 3550](hci__types_8h.md#a46420b559fcc0e584bc604790ae066ae)#define BT\_HCI\_LE\_CS\_T\_IP2\_TIME\_10US\_MASK BIT(0)

[ 3551](hci__types_8h.md#a5d279467b3b0b239748b23be57fee63b)#define BT\_HCI\_LE\_CS\_T\_IP2\_TIME\_20US\_MASK BIT(1)

[ 3552](hci__types_8h.md#a95d5e9901c50e579600db0ef160425eb)#define BT\_HCI\_LE\_CS\_T\_IP2\_TIME\_30US\_MASK BIT(2)

[ 3553](hci__types_8h.md#a66b0bca7c0b19f43b6871cdf05e57543)#define BT\_HCI\_LE\_CS\_T\_IP2\_TIME\_40US\_MASK BIT(3)

[ 3554](hci__types_8h.md#a875fa244820e7aea6f1d6674e3d7d72a)#define BT\_HCI\_LE\_CS\_T\_IP2\_TIME\_50US\_MASK BIT(4)

[ 3555](hci__types_8h.md#ab73d093bcb50ebdd5630e85677af6223)#define BT\_HCI\_LE\_CS\_T\_IP2\_TIME\_60US\_MASK BIT(5)

[ 3556](hci__types_8h.md#a6d6e20505ba9b86bc254bc3419e5bc04)#define BT\_HCI\_LE\_CS\_T\_IP2\_TIME\_80US\_MASK BIT(6)

3557

[ 3558](hci__types_8h.md#ac1138ac8f702b4b79bc03c9a7d60207b)#define BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_15US\_MASK BIT(0)

[ 3559](hci__types_8h.md#a7023db07ddc8f9e9fbfc59283511bafb)#define BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_20US\_MASK BIT(1)

[ 3560](hci__types_8h.md#a77aea9f93d8bcc5949abddcbda52d919)#define BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_30US\_MASK BIT(2)

[ 3561](hci__types_8h.md#a93fc4d9abc1964278748d7dacec7d15a)#define BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_40US\_MASK BIT(3)

[ 3562](hci__types_8h.md#a9f45646b734d3d831d307485d2c8c076)#define BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_50US\_MASK BIT(4)

[ 3563](hci__types_8h.md#a27771be57984aac0b825b3ff033df070)#define BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_60US\_MASK BIT(5)

[ 3564](hci__types_8h.md#ab9c3168510c3e5161c393d7093c3527b)#define BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_80US\_MASK BIT(6)

[ 3565](hci__types_8h.md#acc787bc6363f4c885816a677f7c47db7)#define BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_100US\_MASK BIT(7)

[ 3566](hci__types_8h.md#a40d5f49728ef8204e9b19be3da28a5ae)#define BT\_HCI\_LE\_CS\_T\_FCS\_TIME\_1200US\_MASK BIT(8)

3567

[ 3568](hci__types_8h.md#a46f2a35868d8422878e89f1ddde0e7dc)#define BT\_HCI\_LE\_CS\_T\_PM\_TIME\_10US\_MASK BIT(0)

[ 3569](hci__types_8h.md#a68e13620f22327e8e132aeb19a7cdaf6)#define BT\_HCI\_LE\_CS\_T\_PM\_TIME\_20US\_MASK BIT(1)

3570

[ 3571](hci__types_8h.md#a24c56f19fcf03aabb170925555209f33)#define BT\_HCI\_LE\_CS\_TX\_SNR\_CAPABILITY\_18DB\_MASK BIT(0)

[ 3572](hci__types_8h.md#a80fe1748abbd89e1700c239ff450ce07)#define BT\_HCI\_LE\_CS\_TX\_SNR\_CAPABILITY\_21DB\_MASK BIT(1)

[ 3573](hci__types_8h.md#acd8cc2c9de0edd52c954b0d70dfa44ac)#define BT\_HCI\_LE\_CS\_TX\_SNR\_CAPABILITY\_24DB\_MASK BIT(2)

[ 3574](hci__types_8h.md#a1f27b2456c323b90eebfa8e45932d92f)#define BT\_HCI\_LE\_CS\_TX\_SNR\_CAPABILITY\_27DB\_MASK BIT(3)

[ 3575](hci__types_8h.md#a5045b5b06b3c79c77a4997066f332d13)#define BT\_HCI\_LE\_CS\_TX\_SNR\_CAPABILITY\_30DB\_MASK BIT(4)

3576

[ 3577](hci__types_8h.md#abceb3da0b6d4c858ad35c631acf0516e)#define BT\_HCI\_EVT\_LE\_CS\_READ\_REMOTE\_SUPPORTED\_CAPABILITIES\_COMPLETE 0x2C

[ 3578](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md)struct [bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md) {

[ 3579](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a40980265955d4d58a9b5407ff845fde4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a40980265955d4d58a9b5407ff845fde4);

[ 3580](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a4f8fe99c2392c06125ba94e61aed0e6c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a4f8fe99c2392c06125ba94e61aed0e6c);

[ 3581](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#ab09a466b2a9a0be5f5021f1da0d7393a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_config\_supported](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#ab09a466b2a9a0be5f5021f1da0d7393a);

[ 3582](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#ac73a8bf5425c80739e84cb30ce94f3e7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_consecutive\_procedures\_supported](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#ac73a8bf5425c80739e84cb30ce94f3e7);

[ 3583](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#adcf35e055d04775c444fa28655b95337) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_antennas\_supported](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#adcf35e055d04775c444fa28655b95337);

[ 3584](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a50ad0408019dce16685215c6a1b6d0ef) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_antenna\_paths\_supported](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a50ad0408019dce16685215c6a1b6d0ef);

[ 3585](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a99f9f7b08de6b41e88cea10ba0ca6010) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [roles\_supported](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a99f9f7b08de6b41e88cea10ba0ca6010);

[ 3586](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#ab7a35b1093ece7ae9cc5def4a3e473b2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [modes\_supported](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#ab7a35b1093ece7ae9cc5def4a3e473b2);

[ 3587](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#ace95740224b31c127f5e13550cb5a23a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rtt\_capability](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#ace95740224b31c127f5e13550cb5a23a);

[ 3588](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a843968ec69106d076596e110407d8a1a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rtt\_aa\_only\_n](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a843968ec69106d076596e110407d8a1a);

[ 3589](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a7f796e2eda8d3c7eae556932e37cd93d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rtt\_sounding\_n](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a7f796e2eda8d3c7eae556932e37cd93d);

[ 3590](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a3f275ad58ca745347172ad0b89faf2c4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rtt\_random\_payload\_n](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a3f275ad58ca745347172ad0b89faf2c4);

[ 3591](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#adebb5328c7baeaa786bc185fec432e40) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [nadm\_sounding\_capability](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#adebb5328c7baeaa786bc185fec432e40);

[ 3592](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a7af3067f319be094af31512d4ee5101e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [nadm\_random\_capability](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a7af3067f319be094af31512d4ee5101e);

[ 3593](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a1f303dc3aa8a23fccde27a2d2f64d732) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cs\_sync\_phys\_supported](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a1f303dc3aa8a23fccde27a2d2f64d732);

[ 3594](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#ac83543c17606e401d919fce841a12c6c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [subfeatures\_supported](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#ac83543c17606e401d919fce841a12c6c);

[ 3595](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#ad330adf1ae5b9b84756d36801a4cf289) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [t\_ip1\_times\_supported](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#ad330adf1ae5b9b84756d36801a4cf289);

[ 3596](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a0a1d9dcdf184e49349e86980da2e4bed) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [t\_ip2\_times\_supported](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a0a1d9dcdf184e49349e86980da2e4bed);

[ 3597](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a44869fd19ae813830e38f6e4b88dbb1d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [t\_fcs\_times\_supported](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a44869fd19ae813830e38f6e4b88dbb1d);

[ 3598](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#afef9f37784d75f54521793f07b5baece) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [t\_pm\_times\_supported](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#afef9f37784d75f54521793f07b5baece);

[ 3599](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a21a322fc8efd0c410dda78e2652d506d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [t\_sw\_time\_supported](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a21a322fc8efd0c410dda78e2652d506d);

[ 3600](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#ae3d06bce4df7a2ca07c5d6dd01124743) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_snr\_capability](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#ae3d06bce4df7a2ca07c5d6dd01124743);

3601} \_\_packed;

3602

[ 3603](hci__types_8h.md#a319b523766bcc778ba6bfb3784ac49b7)#define BT\_HCI\_EVT\_LE\_CS\_READ\_REMOTE\_FAE\_TABLE\_COMPLETE 0x2D

[ 3604](structbt__hci__evt__le__cs__read__remote__fae__table__complete.md)struct [bt\_hci\_evt\_le\_cs\_read\_remote\_fae\_table\_complete](structbt__hci__evt__le__cs__read__remote__fae__table__complete.md) {

[ 3605](structbt__hci__evt__le__cs__read__remote__fae__table__complete.md#a1ee4d133955f28f45d16226730344428) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__cs__read__remote__fae__table__complete.md#a1ee4d133955f28f45d16226730344428);

[ 3606](structbt__hci__evt__le__cs__read__remote__fae__table__complete.md#adcdfbfd2d9c19be0c41121235fbb8eaa) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__evt__le__cs__read__remote__fae__table__complete.md#adcdfbfd2d9c19be0c41121235fbb8eaa);

[ 3607](structbt__hci__evt__le__cs__read__remote__fae__table__complete.md#ae1ca6d2d4f4305565f1d491ef202fcad) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [remote\_fae\_table](structbt__hci__evt__le__cs__read__remote__fae__table__complete.md#ae1ca6d2d4f4305565f1d491ef202fcad)[72];

3608} \_\_packed;

3609

[ 3610](hci__types_8h.md#a9c815ae28e424256fc440b426ba69892)#define BT\_HCI\_LE\_CS\_CONFIG\_ACTION\_REMOVED 0x00

[ 3611](hci__types_8h.md#aa437d198f03b30ddbac6ada679e5e0c6)#define BT\_HCI\_LE\_CS\_CONFIG\_ACTION\_CREATED 0x01

3612

[ 3613](hci__types_8h.md#ae1e6afca81585dda0f08f85adc3c69a3)#define BT\_HCI\_EVT\_LE\_CS\_SECURITY\_ENABLE\_COMPLETE 0x2E

[ 3614](structbt__hci__evt__le__cs__security__enable__complete.md)struct [bt\_hci\_evt\_le\_cs\_security\_enable\_complete](structbt__hci__evt__le__cs__security__enable__complete.md) {

[ 3615](structbt__hci__evt__le__cs__security__enable__complete.md#aaf2de8591b18cd36709f7ef755bee917) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__cs__security__enable__complete.md#aaf2de8591b18cd36709f7ef755bee917);

[ 3616](structbt__hci__evt__le__cs__security__enable__complete.md#aaa96a8944598914e4439249ba489f726) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__cs__security__enable__complete.md#aaa96a8944598914e4439249ba489f726);

3617} \_\_packed;

3618

[ 3619](hci__types_8h.md#ab0d5abde05c53bc194fe07b8726fb307)#define BT\_HCI\_EVT\_LE\_CS\_CONFIG\_COMPLETE 0x2F

[ 3620](structbt__hci__evt__le__cs__config__complete.md)struct [bt\_hci\_evt\_le\_cs\_config\_complete](structbt__hci__evt__le__cs__config__complete.md) {

[ 3621](structbt__hci__evt__le__cs__config__complete.md#ae94aa8c92a8d4b33213adc8fc029a02d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__cs__config__complete.md#ae94aa8c92a8d4b33213adc8fc029a02d);

[ 3622](structbt__hci__evt__le__cs__config__complete.md#a511021f717538d4ae25eb28ad82c5f99) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__cs__config__complete.md#a511021f717538d4ae25eb28ad82c5f99);

[ 3623](structbt__hci__evt__le__cs__config__complete.md#a544b3480034087ca01d64a41c1c4b8f9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [config\_id](structbt__hci__evt__le__cs__config__complete.md#a544b3480034087ca01d64a41c1c4b8f9);

[ 3624](structbt__hci__evt__le__cs__config__complete.md#a748fcb3cbd396851a3d159887b12b3e0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [action](structbt__hci__evt__le__cs__config__complete.md#a748fcb3cbd396851a3d159887b12b3e0);

[ 3625](structbt__hci__evt__le__cs__config__complete.md#a14f4c29a7f84463f048364389341c7b5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [main\_mode\_type](structbt__hci__evt__le__cs__config__complete.md#a14f4c29a7f84463f048364389341c7b5);

[ 3626](structbt__hci__evt__le__cs__config__complete.md#a55789928018a6124d87e76709b1b77d9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sub\_mode\_type](structbt__hci__evt__le__cs__config__complete.md#a55789928018a6124d87e76709b1b77d9);

[ 3627](structbt__hci__evt__le__cs__config__complete.md#a21928853b505764e64fcc9190905b12c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [min\_main\_mode\_steps](structbt__hci__evt__le__cs__config__complete.md#a21928853b505764e64fcc9190905b12c);

[ 3628](structbt__hci__evt__le__cs__config__complete.md#a9b14655fa6bb3c7ac43561a399019a76) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_main\_mode\_steps](structbt__hci__evt__le__cs__config__complete.md#a9b14655fa6bb3c7ac43561a399019a76);

[ 3629](structbt__hci__evt__le__cs__config__complete.md#a7fe1af954bae025b9b8bbef70bd1c60e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [main\_mode\_repetition](structbt__hci__evt__le__cs__config__complete.md#a7fe1af954bae025b9b8bbef70bd1c60e);

[ 3630](structbt__hci__evt__le__cs__config__complete.md#a705a7be2d5ce02c4d78319f4f842b87e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mode\_0\_steps](structbt__hci__evt__le__cs__config__complete.md#a705a7be2d5ce02c4d78319f4f842b87e);

[ 3631](structbt__hci__evt__le__cs__config__complete.md#a6f84ebf8a34a830ced1fc738d46fe244) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [role](structbt__hci__evt__le__cs__config__complete.md#a6f84ebf8a34a830ced1fc738d46fe244);

[ 3632](structbt__hci__evt__le__cs__config__complete.md#ae64ff5dbd9d704c3a7f4c5b98ada399c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rtt\_type](structbt__hci__evt__le__cs__config__complete.md#ae64ff5dbd9d704c3a7f4c5b98ada399c);

[ 3633](structbt__hci__evt__le__cs__config__complete.md#ad0454e31d55ec25a21bc272cae999238) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cs\_sync\_phy](structbt__hci__evt__le__cs__config__complete.md#ad0454e31d55ec25a21bc272cae999238);

[ 3634](structbt__hci__evt__le__cs__config__complete.md#abcf0c43f33a85bcd860323212d57ce5b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel\_map](structbt__hci__evt__le__cs__config__complete.md#abcf0c43f33a85bcd860323212d57ce5b)[10];

[ 3635](structbt__hci__evt__le__cs__config__complete.md#a1e5ba3ebb5dcac2105a0f859683505bc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel\_map\_repetition](structbt__hci__evt__le__cs__config__complete.md#a1e5ba3ebb5dcac2105a0f859683505bc);

[ 3636](structbt__hci__evt__le__cs__config__complete.md#aa323b4a74f7fce33e884d0c32e4014d0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel\_selection\_type](structbt__hci__evt__le__cs__config__complete.md#aa323b4a74f7fce33e884d0c32e4014d0);

[ 3637](structbt__hci__evt__le__cs__config__complete.md#a73bd134e9337a9a47e41bba04623ee0b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ch3c\_shape](structbt__hci__evt__le__cs__config__complete.md#a73bd134e9337a9a47e41bba04623ee0b);

[ 3638](structbt__hci__evt__le__cs__config__complete.md#a5f886c16acd561e143a8796fcc1ea5af) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ch3c\_jump](structbt__hci__evt__le__cs__config__complete.md#a5f886c16acd561e143a8796fcc1ea5af);

[ 3639](structbt__hci__evt__le__cs__config__complete.md#a7a452a5e49ade26af3290aaaf318577f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reserved](structbt__hci__evt__le__cs__config__complete.md#a7a452a5e49ade26af3290aaaf318577f);

[ 3640](structbt__hci__evt__le__cs__config__complete.md#afd62b1ffe5388c7f094cb086da4c86ba) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [t\_ip1\_time](structbt__hci__evt__le__cs__config__complete.md#afd62b1ffe5388c7f094cb086da4c86ba);

[ 3641](structbt__hci__evt__le__cs__config__complete.md#a8fafd0e139a9c85830468e5a056c42b7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [t\_ip2\_time](structbt__hci__evt__le__cs__config__complete.md#a8fafd0e139a9c85830468e5a056c42b7);

[ 3642](structbt__hci__evt__le__cs__config__complete.md#a7aa0fd8a1c9c7270059725416dd0a90f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [t\_fcs\_time](structbt__hci__evt__le__cs__config__complete.md#a7aa0fd8a1c9c7270059725416dd0a90f);

[ 3643](structbt__hci__evt__le__cs__config__complete.md#a7d64425b6aa44b01332ce6fac7813471) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [t\_pm\_time](structbt__hci__evt__le__cs__config__complete.md#a7d64425b6aa44b01332ce6fac7813471);

3644} \_\_packed;

3645

[ 3646](hci__types_8h.md#aa615aebe1d896ca1a06bf618619d96f7)#define BT\_HCI\_LE\_CS\_TEST\_CONN\_HANDLE 0x0FFF

3647

[ 3648](hci__types_8h.md#ace872d54fba6d94d62b59a2373c7d0d5)#define BT\_HCI\_LE\_CS\_PROCEDURE\_DONE\_STATUS\_COMPLETE 0x0

[ 3649](hci__types_8h.md#af057e8492e52d0c8763d4a2e969d949d)#define BT\_HCI\_LE\_CS\_PROCEDURE\_DONE\_STATUS\_PARTIAL 0x1

[ 3650](hci__types_8h.md#a821a29dacea9867e4e576f916cf7be3d)#define BT\_HCI\_LE\_CS\_PROCEDURE\_DONE\_STATUS\_ABORTED 0xF

3651

[ 3652](hci__types_8h.md#aee251ce3c46dc0404d880be7d4550fa6)#define BT\_HCI\_LE\_CS\_SUBEVENT\_DONE\_STATUS\_COMPLETE 0x0

[ 3653](hci__types_8h.md#a414d620018a946fcb6c209b21ad6fb00)#define BT\_HCI\_LE\_CS\_SUBEVENT\_DONE\_STATUS\_PARTIAL 0x1

[ 3654](hci__types_8h.md#af1907f8ae481a08c674d86e689826f49)#define BT\_HCI\_LE\_CS\_SUBEVENT\_DONE\_STATUS\_ABORTED 0xF

3655

[ 3656](hci__types_8h.md#a056a67d663cfdc2189b480fc79946c74)#define BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_NO\_ABORT 0x0

[ 3657](hci__types_8h.md#a21eb191c5d99f902c7a244cad685995f)#define BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_LOCAL\_HOST\_OR\_REMOTE\_REQUEST 0x1

[ 3658](hci__types_8h.md#a6dc3f766ce40bbd0ddb7af3cf85677b1)#define BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_TOO\_FEW\_CHANNELS 0x2

[ 3659](hci__types_8h.md#ae8446a2638bd4009b7dee725bb54c883)#define BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_CHMAP\_INSTANT\_PASSED 0x3

[ 3660](hci__types_8h.md#a1e92177f7be3c6a6be00f97fbfc17dcf)#define BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_UNSPECIFIED 0xF

3661

[ 3662](hci__types_8h.md#a095b6061c31229b951b6b96e5d02381f)#define BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_NO\_ABORT 0x0

[ 3663](hci__types_8h.md#a41bbe08db99fb0a2ef77f4f3103f9b6c)#define BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_LOCAL\_HOST\_OR\_REMOTE\_REQUEST 0x1

[ 3664](hci__types_8h.md#ac4817c265c50019d8f74146f7477bf58)#define BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_NO\_CS\_SYNC\_RECEIVED 0x2

[ 3665](hci__types_8h.md#a31cb520a05fe31313bacf8b021da468c)#define BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_SCHED\_CONFLICT 0x3

[ 3666](hci__types_8h.md#abfdca3ae615e19c8e24c098ba8349618)#define BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_UNSPECIFIED 0xF

3667

[ 3668](hci__types_8h.md#a6efdde19fbbf06a40d5dc8dee0515af8)#define BT\_HCI\_LE\_CS\_SUBEVENT\_RESULT\_N\_AP\_IGNORED 0x00

[ 3669](hci__types_8h.md#ae3e9f6d380a61278a8082f07694bdf43)#define BT\_HCI\_LE\_CS\_SUBEVENT\_RESULT\_N\_AP\_1 0x01

[ 3670](hci__types_8h.md#ad6951a0000c3b5cadfbaae94decb153f)#define BT\_HCI\_LE\_CS\_SUBEVENT\_RESULT\_N\_AP\_2 0x02

[ 3671](hci__types_8h.md#aaeb365c3f3ea16d760d4943587ea0bd7)#define BT\_HCI\_LE\_CS\_SUBEVENT\_RESULT\_N\_AP\_3 0x03

[ 3672](hci__types_8h.md#a4cf750ee707ca0b81d4945e4f66798e3)#define BT\_HCI\_LE\_CS\_SUBEVENT\_RESULT\_N\_AP\_4 0x04

3673

[ 3674](hci__types_8h.md#a385a401b373522160b1832b66838e02d)#define BT\_HCI\_LE\_CS\_SUBEVENT\_RESULT\_FREQ\_COMPENSATION\_NOT\_AVAILABLE 0xC000

3675

[ 3676](hci__types_8h.md#a22b108e24f198dfd41b2ad692d448c01)#define BT\_HCI\_LE\_CS\_SUBEVENT\_RESULT\_PCT\_NOT\_AVAILABLE 0xFFFFFFFF

3677

[ 3678](hci__types_8h.md#aa4345ca4225d3958968131ba7a5ff950)#define BT\_HCI\_LE\_CS\_REF\_POWER\_LEVEL\_UNAVAILABLE 0x7F

3679

[ 3680](hci__types_8h.md#af69d92b7c92c8fbeeba8e14838a41f74)#define BT\_HCI\_LE\_CS\_PCT\_I\_MASK 0x000FFF

[ 3681](hci__types_8h.md#a1720b6024f6156e98cb407d6e06e894e)#define BT\_HCI\_LE\_CS\_PCT\_Q\_MASK 0xFFF000

3682

[ 3683](hci__types_8h.md#adcc92fe105d853cc329bbf4340562835)#define BT\_HCI\_LE\_CS\_TONE\_QUALITY\_HIGH 0x0

[ 3684](hci__types_8h.md#af42a419097a2e8ee37d46419cd5e20c3)#define BT\_HCI\_LE\_CS\_TONE\_QUALITY\_MED 0x1

[ 3685](hci__types_8h.md#accc9e73d5fd38c6ab3d108bc3fd039de)#define BT\_HCI\_LE\_CS\_TONE\_QUALITY\_LOW 0x2

[ 3686](hci__types_8h.md#a2b14945754c982ead67ad3b7e615eba9)#define BT\_HCI\_LE\_CS\_TONE\_QUALITY\_UNAVAILABLE 0x3

3687

[ 3688](hci__types_8h.md#a014d9a06d3c571ce06c94a2ebfdbe4e5)#define BT\_HCI\_LE\_CS\_NOT\_TONE\_EXT\_SLOT 0x0

[ 3689](hci__types_8h.md#a72a59878b1445b037eb633a374de92e8)#define BT\_HCI\_LE\_CS\_TONE\_EXT\_SLOT\_EXT\_NOT\_EXPECTED 0x1

[ 3690](hci__types_8h.md#a932802d089c04b78dd6a541b3ddff1e1)#define BT\_HCI\_LE\_CS\_TONE\_EXT\_SLOT\_EXT\_EXPECTED 0x2

3691

[ 3692](hci__types_8h.md#ad0895b572ba1e3d763dbef69c1541b2c)#define BT\_HCI\_LE\_CS\_TIME\_DIFFERENCE\_NOT\_AVAILABLE ((int16\_t)0x8000)

3693

[ 3694](hci__types_8h.md#a54895cd6caacff2dc5aee25e301144a7)#define BT\_HCI\_LE\_CS\_PACKET\_NADM\_ATTACK\_EXT\_UNLIKELY 0x00

[ 3695](hci__types_8h.md#af10362bcbd6b95f8404654d258acdbcb)#define BT\_HCI\_LE\_CS\_PACKET\_NADM\_ATTACK\_VERY\_UNLIKELY 0x01

[ 3696](hci__types_8h.md#acf2d6f7fd7873e12389a2d470241340f)#define BT\_HCI\_LE\_CS\_PACKET\_NADM\_ATTACK\_UNLIKELY 0x02

[ 3697](hci__types_8h.md#a73bf7224e934c28a73d5e54a632e0e69)#define BT\_HCI\_LE\_CS\_PACKET\_NADM\_ATTACK\_POSSIBLE 0x03

[ 3698](hci__types_8h.md#a93f1786e8177c89eb9db36a72e367122)#define BT\_HCI\_LE\_CS\_PACKET\_NADM\_ATTACK\_LIKELY 0x04

[ 3699](hci__types_8h.md#a0b10dcb24c429d594b17eec494954d74)#define BT\_HCI\_LE\_CS\_PACKET\_NADM\_ATTACK\_VERY\_LIKELY 0x05

[ 3700](hci__types_8h.md#abfedf14c97b27f6cdbbb66f2598734e9)#define BT\_HCI\_LE\_CS\_PACKET\_NADM\_ATTACK\_EXT\_LIKELY 0x06

[ 3701](hci__types_8h.md#a5f7d8e81a83a3b94e18a39b507232823)#define BT\_HCI\_LE\_CS\_PACKET\_NADM\_UNKNOWN 0xFF

3702

[ 3703](hci__types_8h.md#ab05d15713fb0145b32a5977774b50533)#define BT\_HCI\_LE\_CS\_PACKET\_QUALITY\_AA\_CHECK\_SUCCESSFUL 0x0

[ 3704](hci__types_8h.md#a7c0e4053873d629e10567937adc033d3)#define BT\_HCI\_LE\_CS\_PACKET\_QUALITY\_AA\_CHECK\_BIT\_ERRORS\_FOUND 0x1

[ 3705](hci__types_8h.md#af357550f37226be5b2b6491ebad3fd57)#define BT\_HCI\_LE\_CS\_PACKET\_QUALITY\_AA\_CHECK\_AA\_NOT\_FOUND 0x2

3706

[ 3707](hci__types_8h.md#a8ce6b3556a9f5b83648b80d90652f00d)#define BT\_HCI\_LE\_CS\_PACKET\_RSSI\_NOT\_AVAILABLE 0x7F

3708

[ 3709](hci__types_8h.md#a56079aad1e8efe328c0bfd4dbad9d953)#define BT\_HCI\_EVT\_LE\_CS\_SUBEVENT\_RESULT 0x31

[ 3711](structbt__hci__le__cs__step__data__mode__0__initiator.md)struct [bt\_hci\_le\_cs\_step\_data\_mode\_0\_initiator](structbt__hci__le__cs__step__data__mode__0__initiator.md) {

3712#ifdef CONFIG\_LITTLE\_ENDIAN

3713 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_quality\_aa\_check](structbt__hci__le__cs__step__data__mode__0__initiator.md#a811eb38a04e63b12be9e25291126ccc1): 4;

3714 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_quality\_bit\_errors](structbt__hci__le__cs__step__data__mode__0__initiator.md#a339252cacafd05e85c0fb19776343e17): 4;

3715#else

[ 3716](structbt__hci__le__cs__step__data__mode__0__initiator.md#a339252cacafd05e85c0fb19776343e17) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_quality\_bit\_errors](structbt__hci__le__cs__step__data__mode__0__initiator.md#a339252cacafd05e85c0fb19776343e17): 4;

[ 3717](structbt__hci__le__cs__step__data__mode__0__initiator.md#a811eb38a04e63b12be9e25291126ccc1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_quality\_aa\_check](structbt__hci__le__cs__step__data__mode__0__initiator.md#a811eb38a04e63b12be9e25291126ccc1): 4;

3718#endif /\* CONFIG\_LITTLE\_ENDIAN \*/

[ 3719](structbt__hci__le__cs__step__data__mode__0__initiator.md#a11edf6e1c1da5d24aa1136521a249f52) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_rssi](structbt__hci__le__cs__step__data__mode__0__initiator.md#a11edf6e1c1da5d24aa1136521a249f52);

[ 3720](structbt__hci__le__cs__step__data__mode__0__initiator.md#ad9a2193cbe5381d30494dbf6f8d84482) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_antenna](structbt__hci__le__cs__step__data__mode__0__initiator.md#ad9a2193cbe5381d30494dbf6f8d84482);

[ 3721](structbt__hci__le__cs__step__data__mode__0__initiator.md#a48fc1fd87869d4ca2b70c42d5c4e1d75) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [measured\_freq\_offset](structbt__hci__le__cs__step__data__mode__0__initiator.md#a48fc1fd87869d4ca2b70c42d5c4e1d75);

3722} \_\_packed;

3723

[ 3725](structbt__hci__le__cs__step__data__mode__0__reflector.md)struct [bt\_hci\_le\_cs\_step\_data\_mode\_0\_reflector](structbt__hci__le__cs__step__data__mode__0__reflector.md) {

3726#ifdef CONFIG\_LITTLE\_ENDIAN

3727 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_quality\_aa\_check](structbt__hci__le__cs__step__data__mode__0__reflector.md#a9c34ecf0b79449754da1d1ba925b1ff2): 4;

3728 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_quality\_bit\_errors](structbt__hci__le__cs__step__data__mode__0__reflector.md#a16fb71660c4f4afb1c36765fdbd2a96a): 4;

3729#else

[ 3730](structbt__hci__le__cs__step__data__mode__0__reflector.md#a16fb71660c4f4afb1c36765fdbd2a96a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_quality\_bit\_errors](structbt__hci__le__cs__step__data__mode__0__reflector.md#a16fb71660c4f4afb1c36765fdbd2a96a): 4;

[ 3731](structbt__hci__le__cs__step__data__mode__0__reflector.md#a9c34ecf0b79449754da1d1ba925b1ff2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_quality\_aa\_check](structbt__hci__le__cs__step__data__mode__0__reflector.md#a9c34ecf0b79449754da1d1ba925b1ff2): 4;

3732#endif /\* CONFIG\_LITTLE\_ENDIAN \*/

[ 3733](structbt__hci__le__cs__step__data__mode__0__reflector.md#aa058afab8cba3f5ce572b8e7d29ef34d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_rssi](structbt__hci__le__cs__step__data__mode__0__reflector.md#aa058afab8cba3f5ce572b8e7d29ef34d);

[ 3734](structbt__hci__le__cs__step__data__mode__0__reflector.md#ad045baeaf6fbb75de002ffedc4b1a831) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_antenna](structbt__hci__le__cs__step__data__mode__0__reflector.md#ad045baeaf6fbb75de002ffedc4b1a831);

3735} \_\_packed;

3736

[ 3738](structbt__hci__le__cs__step__data__mode__1.md)struct [bt\_hci\_le\_cs\_step\_data\_mode\_1](structbt__hci__le__cs__step__data__mode__1.md) {

3739#ifdef CONFIG\_LITTLE\_ENDIAN

3740 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_quality\_aa\_check](structbt__hci__le__cs__step__data__mode__1.md#a8383926e95cd9d222b91704b2ca6883e): 4;

3741 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_quality\_bit\_errors](structbt__hci__le__cs__step__data__mode__1.md#a0cb4198466318a7a15cbbb172c582eeb): 4;

3742#else

[ 3743](structbt__hci__le__cs__step__data__mode__1.md#a0cb4198466318a7a15cbbb172c582eeb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_quality\_bit\_errors](structbt__hci__le__cs__step__data__mode__1.md#a0cb4198466318a7a15cbbb172c582eeb): 4;

[ 3744](structbt__hci__le__cs__step__data__mode__1.md#a8383926e95cd9d222b91704b2ca6883e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_quality\_aa\_check](structbt__hci__le__cs__step__data__mode__1.md#a8383926e95cd9d222b91704b2ca6883e): 4;

3745#endif /\* CONFIG\_LITTLE\_ENDIAN \*/

[ 3746](structbt__hci__le__cs__step__data__mode__1.md#a4025cf2b229ada27e258d3d519a7b1dd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_nadm](structbt__hci__le__cs__step__data__mode__1.md#a4025cf2b229ada27e258d3d519a7b1dd);

[ 3747](structbt__hci__le__cs__step__data__mode__1.md#a1b9df39c01ab91ab225c809db5066f70) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_rssi](structbt__hci__le__cs__step__data__mode__1.md#a1b9df39c01ab91ab225c809db5066f70);

3748 union {

[ 3749](structbt__hci__le__cs__step__data__mode__1.md#a1365e601f422b98747f9909d3be56b60) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [toa\_tod\_initiator](structbt__hci__le__cs__step__data__mode__1.md#a1365e601f422b98747f9909d3be56b60);

[ 3750](structbt__hci__le__cs__step__data__mode__1.md#ab3425181b2a625fcfbbfd14477d717d1) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [tod\_toa\_reflector](structbt__hci__le__cs__step__data__mode__1.md#ab3425181b2a625fcfbbfd14477d717d1);

3751 };

[ 3752](structbt__hci__le__cs__step__data__mode__1.md#afc8221a5cab14d3842590e6cac52da4d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_antenna](structbt__hci__le__cs__step__data__mode__1.md#afc8221a5cab14d3842590e6cac52da4d);

3753} \_\_packed;

3754

[ 3756](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md)struct [bt\_hci\_le\_cs\_step\_data\_mode\_1\_ss\_rtt](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md) {

3757#ifdef CONFIG\_LITTLE\_ENDIAN

3758 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_quality\_aa\_check](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#ad8f9ca9dda852b435848b988ad872797): 4;

3759 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_quality\_bit\_errors](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#a515fde1d568a19ccf6ebefe9052866a4): 4;

3760#else

[ 3761](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#a515fde1d568a19ccf6ebefe9052866a4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_quality\_bit\_errors](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#a515fde1d568a19ccf6ebefe9052866a4): 4;

[ 3762](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#ad8f9ca9dda852b435848b988ad872797) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_quality\_aa\_check](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#ad8f9ca9dda852b435848b988ad872797): 4;

3763#endif /\* CONFIG\_LITTLE\_ENDIAN \*/

[ 3764](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#a511b281fb1c16fd7d0eaf731906a4292) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_nadm](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#a511b281fb1c16fd7d0eaf731906a4292);

[ 3765](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#a5ec9c30063c09285804973008533e5cb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_rssi](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#a5ec9c30063c09285804973008533e5cb);

3766 union {

[ 3767](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#a77bbcd9451360ad97813f9357e44766e) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [toa\_tod\_initiator](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#a77bbcd9451360ad97813f9357e44766e);

[ 3768](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#ace3843bc24616950f04150b2f86abad4) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [tod\_toa\_reflector](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#ace3843bc24616950f04150b2f86abad4);

3769 };

[ 3770](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#abf20351ab0eaf3a7139a464f1d1a72b0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_antenna](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#abf20351ab0eaf3a7139a464f1d1a72b0);

[ 3771](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#a3f8ba85b776f732ebc1086a4317849a1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_pct1](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#a3f8ba85b776f732ebc1086a4317849a1)[4];

[ 3772](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#a9f969aa6fc134a9e618d07f177d2b7fd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_pct2](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#a9f969aa6fc134a9e618d07f177d2b7fd)[4];

3773} \_\_packed;

3774

3775

[ 3777](structbt__hci__le__cs__step__data__tone__info.md)struct [bt\_hci\_le\_cs\_step\_data\_tone\_info](structbt__hci__le__cs__step__data__tone__info.md) {

[ 3778](structbt__hci__le__cs__step__data__tone__info.md#aeb76aeb54cb4e5613496431ec6d0093a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phase\_correction\_term](structbt__hci__le__cs__step__data__tone__info.md#aeb76aeb54cb4e5613496431ec6d0093a)[3];

3779#ifdef CONFIG\_LITTLE\_ENDIAN

3780 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [quality\_indicator](structbt__hci__le__cs__step__data__tone__info.md#a4d31c0759c17789cb4b9bdc90a8870ca): 4;

3781 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [extension\_indicator](structbt__hci__le__cs__step__data__tone__info.md#a5f2e5e95b97d2be49a8ff1d9376892e8): 4;

3782#else

[ 3783](structbt__hci__le__cs__step__data__tone__info.md#a5f2e5e95b97d2be49a8ff1d9376892e8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [extension\_indicator](structbt__hci__le__cs__step__data__tone__info.md#a5f2e5e95b97d2be49a8ff1d9376892e8): 4;

[ 3784](structbt__hci__le__cs__step__data__tone__info.md#a4d31c0759c17789cb4b9bdc90a8870ca) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [quality\_indicator](structbt__hci__le__cs__step__data__tone__info.md#a4d31c0759c17789cb4b9bdc90a8870ca): 4;

3785#endif /\* CONFIG\_LITTLE\_ENDIAN \*/

3786} \_\_packed;

3787

[ 3789](structbt__hci__le__cs__step__data__mode__2.md)struct [bt\_hci\_le\_cs\_step\_data\_mode\_2](structbt__hci__le__cs__step__data__mode__2.md) {

[ 3790](structbt__hci__le__cs__step__data__mode__2.md#a9feb2b07f8862aa24772a733f451f7a8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [antenna\_permutation\_index](structbt__hci__le__cs__step__data__mode__2.md#a9feb2b07f8862aa24772a733f451f7a8);

[ 3791](structbt__hci__le__cs__step__data__mode__2.md#aef5699cb9bfc522a12be9a284392fd0e) struct [bt\_hci\_le\_cs\_step\_data\_tone\_info](structbt__hci__le__cs__step__data__tone__info.md) [tone\_info](structbt__hci__le__cs__step__data__mode__2.md#aef5699cb9bfc522a12be9a284392fd0e)[];

3792} \_\_packed;

3793

[ 3795](structbt__hci__le__cs__step__data__mode__3.md)struct [bt\_hci\_le\_cs\_step\_data\_mode\_3](structbt__hci__le__cs__step__data__mode__3.md) {

3796#ifdef CONFIG\_LITTLE\_ENDIAN

3797 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_quality\_aa\_check](structbt__hci__le__cs__step__data__mode__3.md#ad4c30784cc2586b5b8dcfa22e7a1f8fb): 4;

3798 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_quality\_bit\_errors](structbt__hci__le__cs__step__data__mode__3.md#a42b8bdf1fd492be1daded674e3d733d6): 4;

3799#else

[ 3800](structbt__hci__le__cs__step__data__mode__3.md#a42b8bdf1fd492be1daded674e3d733d6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_quality\_bit\_errors](structbt__hci__le__cs__step__data__mode__3.md#a42b8bdf1fd492be1daded674e3d733d6): 4;

[ 3801](structbt__hci__le__cs__step__data__mode__3.md#ad4c30784cc2586b5b8dcfa22e7a1f8fb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_quality\_aa\_check](structbt__hci__le__cs__step__data__mode__3.md#ad4c30784cc2586b5b8dcfa22e7a1f8fb): 4;

3802#endif /\* CONFIG\_LITTLE\_ENDIAN \*/

[ 3803](structbt__hci__le__cs__step__data__mode__3.md#a9b7373e7d3faa0cb5553d4f897c94ebc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_nadm](structbt__hci__le__cs__step__data__mode__3.md#a9b7373e7d3faa0cb5553d4f897c94ebc);

[ 3804](structbt__hci__le__cs__step__data__mode__3.md#a60750ac38bf019a0c7a8656ca59fc402) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_rssi](structbt__hci__le__cs__step__data__mode__3.md#a60750ac38bf019a0c7a8656ca59fc402);

3805 union {

[ 3806](structbt__hci__le__cs__step__data__mode__3.md#a183f3ee64a4482c9d3e0f041151fdcf9) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [toa\_tod\_initiator](structbt__hci__le__cs__step__data__mode__3.md#a183f3ee64a4482c9d3e0f041151fdcf9);

[ 3807](structbt__hci__le__cs__step__data__mode__3.md#aa0f1918115a6e550d6fab17529bbb4f2) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [tod\_toa\_reflector](structbt__hci__le__cs__step__data__mode__3.md#aa0f1918115a6e550d6fab17529bbb4f2);

3808 };

[ 3809](structbt__hci__le__cs__step__data__mode__3.md#ad20e9c1deba67aa5759881b52d13311d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_antenna](structbt__hci__le__cs__step__data__mode__3.md#ad20e9c1deba67aa5759881b52d13311d);

[ 3810](structbt__hci__le__cs__step__data__mode__3.md#a609102fc9d42fe73c09907f54526bd40) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [antenna\_permutation\_index](structbt__hci__le__cs__step__data__mode__3.md#a609102fc9d42fe73c09907f54526bd40);

[ 3811](structbt__hci__le__cs__step__data__mode__3.md#a9ae78aa83a22f0618491871d55f2f0b9) struct [bt\_hci\_le\_cs\_step\_data\_tone\_info](structbt__hci__le__cs__step__data__tone__info.md) [tone\_info](structbt__hci__le__cs__step__data__mode__3.md#a9ae78aa83a22f0618491871d55f2f0b9)[];

3812} \_\_packed;

3813

[ 3815](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md)struct [bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md) {

3816#ifdef CONFIG\_LITTLE\_ENDIAN

3817 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_quality\_aa\_check](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#a657ec3570e3ad6b2ddab87bada231587): 4;

3818 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_quality\_bit\_errors](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#af5d8a8559400b45066bdac86fbdac411): 4;

3819#else

[ 3820](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#af5d8a8559400b45066bdac86fbdac411) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_quality\_bit\_errors](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#af5d8a8559400b45066bdac86fbdac411): 4;

[ 3821](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#a657ec3570e3ad6b2ddab87bada231587) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_quality\_aa\_check](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#a657ec3570e3ad6b2ddab87bada231587): 4;

3822#endif /\* CONFIG\_LITTLE\_ENDIAN \*/

[ 3823](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#a9d2428083c401d931520addde0af54fd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_nadm](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#a9d2428083c401d931520addde0af54fd);

[ 3824](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#adc4fe32bc6b7515e5bf1055f19f1a2bd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_rssi](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#adc4fe32bc6b7515e5bf1055f19f1a2bd);

3825 union {

[ 3826](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#ae2181a568ed6da32d3f60ba6d271c64f) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [toa\_tod\_initiator](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#ae2181a568ed6da32d3f60ba6d271c64f);

[ 3827](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#ada4d52f54f1efa804a812c65edd8f125) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [tod\_toa\_reflector](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#ada4d52f54f1efa804a812c65edd8f125);

3828 };

[ 3829](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#a9ce412ad8b18a9315b858cf1fe2a466a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_antenna](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#a9ce412ad8b18a9315b858cf1fe2a466a);

[ 3830](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#aada8b3ff1bb0d0b9eccb846da173b3f4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_pct1](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#aada8b3ff1bb0d0b9eccb846da173b3f4)[4];

[ 3831](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#afdebbafc06475dde12aaed73d2180f96) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_pct2](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#afdebbafc06475dde12aaed73d2180f96)[4];

[ 3832](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#ac4067e27caa12cf9f8c6525bf6a72973) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [antenna\_permutation\_index](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#ac4067e27caa12cf9f8c6525bf6a72973);

[ 3833](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#aea13fc3e16092dcede9fb46ea719f21c) struct [bt\_hci\_le\_cs\_step\_data\_tone\_info](structbt__hci__le__cs__step__data__tone__info.md) [tone\_info](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#aea13fc3e16092dcede9fb46ea719f21c)[];

3834} \_\_packed;

3835

[ 3836](structbt__hci__evt__le__cs__subevent__result__step.md)struct [bt\_hci\_evt\_le\_cs\_subevent\_result\_step](structbt__hci__evt__le__cs__subevent__result__step.md) {

[ 3837](structbt__hci__evt__le__cs__subevent__result__step.md#a65f6ecf6355883df7924067edc277f35) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [step\_mode](structbt__hci__evt__le__cs__subevent__result__step.md#a65f6ecf6355883df7924067edc277f35);

[ 3838](structbt__hci__evt__le__cs__subevent__result__step.md#a1f074ff26f779292ea32bb405f37b877) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [step\_channel](structbt__hci__evt__le__cs__subevent__result__step.md#a1f074ff26f779292ea32bb405f37b877);

[ 3839](structbt__hci__evt__le__cs__subevent__result__step.md#a7fb65809d78fbf08528f177d98e72f6b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [step\_data\_length](structbt__hci__evt__le__cs__subevent__result__step.md#a7fb65809d78fbf08528f177d98e72f6b);

[ 3840](structbt__hci__evt__le__cs__subevent__result__step.md#aebb0c47275e4cf92802314a82ffba820) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [step\_data](structbt__hci__evt__le__cs__subevent__result__step.md#aebb0c47275e4cf92802314a82ffba820)[];

3841} \_\_packed;

3842

[ 3843](structbt__hci__evt__le__cs__subevent__result.md)struct [bt\_hci\_evt\_le\_cs\_subevent\_result](structbt__hci__evt__le__cs__subevent__result.md) {

[ 3844](structbt__hci__evt__le__cs__subevent__result.md#a3b9c8392fa3aadc2e0673923e0346278) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__evt__le__cs__subevent__result.md#a3b9c8392fa3aadc2e0673923e0346278);

[ 3845](structbt__hci__evt__le__cs__subevent__result.md#a2e8bdef7f85a4cefeaf625d0c3a4db03) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [config\_id](structbt__hci__evt__le__cs__subevent__result.md#a2e8bdef7f85a4cefeaf625d0c3a4db03);

[ 3846](structbt__hci__evt__le__cs__subevent__result.md#a0d6b2ca9f148173abb6207cf7c473c7f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [start\_acl\_conn\_event\_counter](structbt__hci__evt__le__cs__subevent__result.md#a0d6b2ca9f148173abb6207cf7c473c7f);

[ 3847](structbt__hci__evt__le__cs__subevent__result.md#ad08558fd68eb6c43d95a3f0f62bafff0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [procedure\_counter](structbt__hci__evt__le__cs__subevent__result.md#ad08558fd68eb6c43d95a3f0f62bafff0);

[ 3848](structbt__hci__evt__le__cs__subevent__result.md#aba480f7ad78069fd8b83493fac42244e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [frequency\_compensation](structbt__hci__evt__le__cs__subevent__result.md#aba480f7ad78069fd8b83493fac42244e);

[ 3849](structbt__hci__evt__le__cs__subevent__result.md#a9a7260f63122a94cf7eb6ddc3344f742) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reference\_power\_level](structbt__hci__evt__le__cs__subevent__result.md#a9a7260f63122a94cf7eb6ddc3344f742);

[ 3850](structbt__hci__evt__le__cs__subevent__result.md#a27a2848009838977f26df75bfc9bc3c3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [procedure\_done\_status](structbt__hci__evt__le__cs__subevent__result.md#a27a2848009838977f26df75bfc9bc3c3);

[ 3851](structbt__hci__evt__le__cs__subevent__result.md#aeda28dfb30c51ce2955e1c313069c111) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent\_done\_status](structbt__hci__evt__le__cs__subevent__result.md#aeda28dfb30c51ce2955e1c313069c111);

3852#ifdef CONFIG\_LITTLE\_ENDIAN

3853 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [procedure\_abort\_reason](structbt__hci__evt__le__cs__subevent__result.md#ab81c9c55697b2f2c92e3ea2073932ad1): 4;

3854 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent\_abort\_reason](structbt__hci__evt__le__cs__subevent__result.md#acf6f9c4e6fa5897be872d9953993517b): 4;

3855#else

[ 3856](structbt__hci__evt__le__cs__subevent__result.md#acf6f9c4e6fa5897be872d9953993517b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent\_abort\_reason](structbt__hci__evt__le__cs__subevent__result.md#acf6f9c4e6fa5897be872d9953993517b): 4;

[ 3857](structbt__hci__evt__le__cs__subevent__result.md#ab81c9c55697b2f2c92e3ea2073932ad1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [procedure\_abort\_reason](structbt__hci__evt__le__cs__subevent__result.md#ab81c9c55697b2f2c92e3ea2073932ad1): 4;

3858#endif /\* CONFIG\_LITTLE\_ENDIAN \*/

[ 3859](structbt__hci__evt__le__cs__subevent__result.md#a9931d5818b801a9c36853f88b259c25e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_antenna\_paths](structbt__hci__evt__le__cs__subevent__result.md#a9931d5818b801a9c36853f88b259c25e);

[ 3860](structbt__hci__evt__le__cs__subevent__result.md#af8c827d508614f553b9f503d0394411b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_steps\_reported](structbt__hci__evt__le__cs__subevent__result.md#af8c827d508614f553b9f503d0394411b);

[ 3861](structbt__hci__evt__le__cs__subevent__result.md#a43b46a37648b9fde72634dd7dd6a68e6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [steps](structbt__hci__evt__le__cs__subevent__result.md#a43b46a37648b9fde72634dd7dd6a68e6)[];

3862} \_\_packed;

3863

[ 3864](hci__types_8h.md#aad00fc66b8bbc4f3e474661cb4122e47)#define BT\_HCI\_EVT\_LE\_CS\_SUBEVENT\_RESULT\_CONTINUE 0x32

3865

[ 3866](structbt__hci__evt__le__cs__subevent__result__continue.md)struct [bt\_hci\_evt\_le\_cs\_subevent\_result\_continue](structbt__hci__evt__le__cs__subevent__result__continue.md) {

[ 3867](structbt__hci__evt__le__cs__subevent__result__continue.md#a4126bebec093f6f4d1a22b43abec6b1c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__evt__le__cs__subevent__result__continue.md#a4126bebec093f6f4d1a22b43abec6b1c);

[ 3868](structbt__hci__evt__le__cs__subevent__result__continue.md#adefb9ad1f998460a6d235ebd39bbfe4a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [config\_id](structbt__hci__evt__le__cs__subevent__result__continue.md#adefb9ad1f998460a6d235ebd39bbfe4a);

[ 3869](structbt__hci__evt__le__cs__subevent__result__continue.md#a3e5b1e8a247fff36c06447c9ff7c3bb8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [procedure\_done\_status](structbt__hci__evt__le__cs__subevent__result__continue.md#a3e5b1e8a247fff36c06447c9ff7c3bb8);

[ 3870](structbt__hci__evt__le__cs__subevent__result__continue.md#a49cf181c8518fb3015a0c54f7558aa8c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent\_done\_status](structbt__hci__evt__le__cs__subevent__result__continue.md#a49cf181c8518fb3015a0c54f7558aa8c);

3871#ifdef CONFIG\_LITTLE\_ENDIAN

3872 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [procedure\_abort\_reason](structbt__hci__evt__le__cs__subevent__result__continue.md#a3c7ac056a5898710ffbc0776ef551b4b): 4;

3873 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent\_abort\_reason](structbt__hci__evt__le__cs__subevent__result__continue.md#a1801aeaac839831198e17b7d96a5532a): 4;

3874#else

[ 3875](structbt__hci__evt__le__cs__subevent__result__continue.md#a1801aeaac839831198e17b7d96a5532a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent\_abort\_reason](structbt__hci__evt__le__cs__subevent__result__continue.md#a1801aeaac839831198e17b7d96a5532a): 4;

[ 3876](structbt__hci__evt__le__cs__subevent__result__continue.md#a3c7ac056a5898710ffbc0776ef551b4b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [procedure\_abort\_reason](structbt__hci__evt__le__cs__subevent__result__continue.md#a3c7ac056a5898710ffbc0776ef551b4b): 4;

3877#endif /\* CONFIG\_LITTLE\_ENDIAN \*/

[ 3878](structbt__hci__evt__le__cs__subevent__result__continue.md#a2f8e1f634e28100815c881a463b51f2c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_antenna\_paths](structbt__hci__evt__le__cs__subevent__result__continue.md#a2f8e1f634e28100815c881a463b51f2c);

[ 3879](structbt__hci__evt__le__cs__subevent__result__continue.md#af127774b52c4e088f628999136b6cd7c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_steps\_reported](structbt__hci__evt__le__cs__subevent__result__continue.md#af127774b52c4e088f628999136b6cd7c);

[ 3880](structbt__hci__evt__le__cs__subevent__result__continue.md#abbddd0e27178e49abe6eef62bc094a16) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [steps](structbt__hci__evt__le__cs__subevent__result__continue.md#abbddd0e27178e49abe6eef62bc094a16)[];

3881} \_\_packed;

3882

[ 3883](hci__types_8h.md#a7dae3e2125d30c3b344b51aba0df68bf)#define BT\_HCI\_EVT\_LE\_CS\_TEST\_END\_COMPLETE 0x33

[ 3884](structbt__hci__evt__le__cs__test__end__complete.md)struct [bt\_hci\_evt\_le\_cs\_test\_end\_complete](structbt__hci__evt__le__cs__test__end__complete.md) {

[ 3885](structbt__hci__evt__le__cs__test__end__complete.md#ae083dabff641736ed9a23ffc5a36a737) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__cs__test__end__complete.md#ae083dabff641736ed9a23ffc5a36a737);

3886} \_\_packed;

3887

[ 3888](hci__types_8h.md#a276cf3951bb5c4ee0b1deeb78a7b5681)#define BT\_HCI\_EVT\_LE\_CS\_PROCEDURE\_ENABLE\_COMPLETE 0x30

[ 3889](structbt__hci__evt__le__cs__procedure__enable__complete.md)struct [bt\_hci\_evt\_le\_cs\_procedure\_enable\_complete](structbt__hci__evt__le__cs__procedure__enable__complete.md) {

[ 3890](structbt__hci__evt__le__cs__procedure__enable__complete.md#a5822ff654eee794442a05033e0f10fae) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__cs__procedure__enable__complete.md#a5822ff654eee794442a05033e0f10fae);

[ 3891](structbt__hci__evt__le__cs__procedure__enable__complete.md#adcf8e32c2346073e0fbe273d261f6741) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__cs__procedure__enable__complete.md#adcf8e32c2346073e0fbe273d261f6741);

[ 3892](structbt__hci__evt__le__cs__procedure__enable__complete.md#a17b62e13cda5f47dee2e8873686b978e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [config\_id](structbt__hci__evt__le__cs__procedure__enable__complete.md#a17b62e13cda5f47dee2e8873686b978e);

[ 3893](structbt__hci__evt__le__cs__procedure__enable__complete.md#a7ff8f1e713d9b835f3a4e0e79cb1b3d1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](structbt__hci__evt__le__cs__procedure__enable__complete.md#a7ff8f1e713d9b835f3a4e0e79cb1b3d1);

[ 3894](structbt__hci__evt__le__cs__procedure__enable__complete.md#a60a9e00cba665d73e65d0ee5b0d9efbc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tone\_antenna\_config\_selection](structbt__hci__evt__le__cs__procedure__enable__complete.md#a60a9e00cba665d73e65d0ee5b0d9efbc);

[ 3895](structbt__hci__evt__le__cs__procedure__enable__complete.md#afd760c9b6809e6764a652ecb3ee4c2b5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [selected\_tx\_power](structbt__hci__evt__le__cs__procedure__enable__complete.md#afd760c9b6809e6764a652ecb3ee4c2b5);

[ 3896](structbt__hci__evt__le__cs__procedure__enable__complete.md#af5959274cb88a8e4fdf09e8dd756f31c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent\_len](structbt__hci__evt__le__cs__procedure__enable__complete.md#af5959274cb88a8e4fdf09e8dd756f31c)[3];

[ 3897](structbt__hci__evt__le__cs__procedure__enable__complete.md#aacc14948a9e6c384ec94051fb4323599) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevents\_per\_event](structbt__hci__evt__le__cs__procedure__enable__complete.md#aacc14948a9e6c384ec94051fb4323599);

[ 3898](structbt__hci__evt__le__cs__procedure__enable__complete.md#a8f5485967662dbd1676d8edd6345fd13) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [subevent\_interval](structbt__hci__evt__le__cs__procedure__enable__complete.md#a8f5485967662dbd1676d8edd6345fd13);

[ 3899](structbt__hci__evt__le__cs__procedure__enable__complete.md#a688bfcb6781b2e3480f021c66a3109fe) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [event\_interval](structbt__hci__evt__le__cs__procedure__enable__complete.md#a688bfcb6781b2e3480f021c66a3109fe);

[ 3900](structbt__hci__evt__le__cs__procedure__enable__complete.md#ad7c21907a38747ec405c992ef14e8dd7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [procedure\_interval](structbt__hci__evt__le__cs__procedure__enable__complete.md#ad7c21907a38747ec405c992ef14e8dd7);

[ 3901](structbt__hci__evt__le__cs__procedure__enable__complete.md#ac8489dc8ff5f9bf052a7c1a67a544106) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [procedure\_count](structbt__hci__evt__le__cs__procedure__enable__complete.md#ac8489dc8ff5f9bf052a7c1a67a544106);

[ 3902](structbt__hci__evt__le__cs__procedure__enable__complete.md#a7a38c8ced8720a428df42e821ec7e9e6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_procedure\_len](structbt__hci__evt__le__cs__procedure__enable__complete.md#a7a38c8ced8720a428df42e821ec7e9e6);

3903} \_\_packed;

3904

3905/\* Event mask bits \*/

3906

[ 3907](hci__types_8h.md#a25201544478590f6ee87a829410c612b)#define BT\_EVT\_BIT(n) (1ULL << (n))

3908

[ 3909](hci__types_8h.md#a79851cd962916f9be81e29ce9797e901)#define BT\_EVT\_MASK\_INQUIRY\_COMPLETE BT\_EVT\_BIT(0)

[ 3910](hci__types_8h.md#a5a13adda8bf4f015550a043667e0b67d)#define BT\_EVT\_MASK\_CONN\_COMPLETE BT\_EVT\_BIT(2)

[ 3911](hci__types_8h.md#ad77bbcd4fb8b0e37700492e8a3cccd38)#define BT\_EVT\_MASK\_CONN\_REQUEST BT\_EVT\_BIT(3)

[ 3912](hci__types_8h.md#a5ea9d4fb977c660bc33be93c73817705)#define BT\_EVT\_MASK\_DISCONN\_COMPLETE BT\_EVT\_BIT(4)

[ 3913](hci__types_8h.md#ad4f80dd3fdf22b23d47785a507aa5a85)#define BT\_EVT\_MASK\_AUTH\_COMPLETE BT\_EVT\_BIT(5)

[ 3914](hci__types_8h.md#a4433027483d6d63911b59c4fe605ba69)#define BT\_EVT\_MASK\_REMOTE\_NAME\_REQ\_COMPLETE BT\_EVT\_BIT(6)

[ 3915](hci__types_8h.md#a334c571248a1aad285bb11bc39d2ade8)#define BT\_EVT\_MASK\_ENCRYPT\_CHANGE BT\_EVT\_BIT(7)

[ 3916](hci__types_8h.md#a7ccade60a01e0f8a175b3b11b5e20f6d)#define BT\_EVT\_MASK\_REMOTE\_FEATURES BT\_EVT\_BIT(10)

[ 3917](hci__types_8h.md#a87331cabdea78ace1577cbf2fa7e3523)#define BT\_EVT\_MASK\_REMOTE\_VERSION\_INFO BT\_EVT\_BIT(11)

[ 3918](hci__types_8h.md#a079c00e59422034a9f977af7dd20234c)#define BT\_EVT\_MASK\_HARDWARE\_ERROR BT\_EVT\_BIT(15)

[ 3919](hci__types_8h.md#a4b4a80b51b2c20bf28fbfac57679a86e)#define BT\_EVT\_MASK\_ROLE\_CHANGE BT\_EVT\_BIT(17)

[ 3920](hci__types_8h.md#a9f5612d89848aafb6e9063a55e5cd6b4)#define BT\_EVT\_MASK\_PIN\_CODE\_REQ BT\_EVT\_BIT(21)

[ 3921](hci__types_8h.md#a1e16ab7caf239e804c0c2057e9b49e42)#define BT\_EVT\_MASK\_LINK\_KEY\_REQ BT\_EVT\_BIT(22)

[ 3922](hci__types_8h.md#aa20a3ce217a60070826d0b55ebd105be)#define BT\_EVT\_MASK\_LINK\_KEY\_NOTIFY BT\_EVT\_BIT(23)

[ 3923](hci__types_8h.md#a829ea33c603291d331faba58689b0198)#define BT\_EVT\_MASK\_DATA\_BUFFER\_OVERFLOW BT\_EVT\_BIT(25)

[ 3924](hci__types_8h.md#aeb5b4cbc01a8cebea5ce8e0090d37261)#define BT\_EVT\_MASK\_INQUIRY\_RESULT\_WITH\_RSSI BT\_EVT\_BIT(33)

[ 3925](hci__types_8h.md#a9d3bbaa1eb1dbe72714b922dcada3347)#define BT\_EVT\_MASK\_REMOTE\_EXT\_FEATURES BT\_EVT\_BIT(34)

[ 3926](hci__types_8h.md#a4f1a905136cb713c09fb5197dd099ce2)#define BT\_EVT\_MASK\_SYNC\_CONN\_COMPLETE BT\_EVT\_BIT(43)

[ 3927](hci__types_8h.md#a9b361fe6314f56fcb016bacb064af815)#define BT\_EVT\_MASK\_EXTENDED\_INQUIRY\_RESULT BT\_EVT\_BIT(46)

[ 3928](hci__types_8h.md#af8d96cc1cf99a7130d4c181450998cb7)#define BT\_EVT\_MASK\_ENCRYPT\_KEY\_REFRESH\_COMPLETE BT\_EVT\_BIT(47)

[ 3929](hci__types_8h.md#a845de3735dc3989d3a9d54cf5e55b408)#define BT\_EVT\_MASK\_IO\_CAPA\_REQ BT\_EVT\_BIT(48)

[ 3930](hci__types_8h.md#a409e33dbe4fdb1dc90050e0b4eab1f86)#define BT\_EVT\_MASK\_IO\_CAPA\_RESP BT\_EVT\_BIT(49)

[ 3931](hci__types_8h.md#a1c04cc7d04f056e5edfc4ddaa97c657f)#define BT\_EVT\_MASK\_USER\_CONFIRM\_REQ BT\_EVT\_BIT(50)

[ 3932](hci__types_8h.md#af56d87ffc24c2e4c08db68ab019fd58e)#define BT\_EVT\_MASK\_USER\_PASSKEY\_REQ BT\_EVT\_BIT(51)

[ 3933](hci__types_8h.md#a6a08ace148ea2728614a3bab02c21f65)#define BT\_EVT\_MASK\_SSP\_COMPLETE BT\_EVT\_BIT(53)

[ 3934](hci__types_8h.md#a2eb47347a5685a290087b236d696971e)#define BT\_EVT\_MASK\_USER\_PASSKEY\_NOTIFY BT\_EVT\_BIT(58)

[ 3935](hci__types_8h.md#a59f89d39350b396f8d0c986e2d477bba)#define BT\_EVT\_MASK\_LE\_META\_EVENT BT\_EVT\_BIT(61)

3936

3937/\* Page 2 \*/

[ 3938](hci__types_8h.md#abe39e63cbdee9bfeac36a1b6a4d40aba)#define BT\_EVT\_MASK\_NUM\_COMPLETE\_DATA\_BLOCKS BT\_EVT\_BIT(8)

[ 3939](hci__types_8h.md#aff43216feb0c29c6813d198473f34fdc)#define BT\_EVT\_MASK\_TRIGG\_CLOCK\_CAPTURE BT\_EVT\_BIT(14)

[ 3940](hci__types_8h.md#ac078d5b46d7e227726cb7456e2163d3f)#define BT\_EVT\_MASK\_SYNCH\_TRAIN\_COMPLETE BT\_EVT\_BIT(15)

[ 3941](hci__types_8h.md#a8901b477ec3584af207b3648b221bb92)#define BT\_EVT\_MASK\_SYNCH\_TRAIN\_RX BT\_EVT\_BIT(16)

[ 3942](hci__types_8h.md#aa8842138b1146d3581c39062d11a6305)#define BT\_EVT\_MASK\_CL\_PER\_BC\_RX BT\_EVT\_BIT(17)

[ 3943](hci__types_8h.md#af513eaa35861cfcfefba97e0263e3f5b)#define BT\_EVT\_MASK\_CL\_PER\_BC\_TIMEOUT BT\_EVT\_BIT(18)

[ 3944](hci__types_8h.md#a9b82f06f42651c32f4c0db9826002134)#define BT\_EVT\_MASK\_TRUNC\_PAGE\_COMPLETE BT\_EVT\_BIT(19)

[ 3945](hci__types_8h.md#ad078befa197baac20294dc0d46eff9dd)#define BT\_EVT\_MASK\_PER\_PAGE\_RSP\_TIMEOUT BT\_EVT\_BIT(20)

[ 3946](hci__types_8h.md#a35f42f297b980a050deceb71237883ba)#define BT\_EVT\_MASK\_CL\_PER\_BC\_CH\_MAP\_CHANGE BT\_EVT\_BIT(21)

[ 3947](hci__types_8h.md#ae8106016a80e123016c6d2fc406224d7)#define BT\_EVT\_MASK\_INQUIRY\_RSP\_NOT BT\_EVT\_BIT(22)

[ 3948](hci__types_8h.md#a33753df12afb5f7e19be01f9febc5d23)#define BT\_EVT\_MASK\_AUTH\_PAYLOAD\_TIMEOUT\_EXP BT\_EVT\_BIT(23)

[ 3949](hci__types_8h.md#a8bfac36e993c48d12bdeb7c130fdd6dc)#define BT\_EVT\_MASK\_SAM\_STATUS\_CHANGE BT\_EVT\_BIT(24)

3950

[ 3951](hci__types_8h.md#a59cd7a15e5b562adb6397509463e375c)#define BT\_EVT\_MASK\_LE\_CONN\_COMPLETE BT\_EVT\_BIT(0)

[ 3952](hci__types_8h.md#a39a55a4c3e71db708e39c8110a2349f7)#define BT\_EVT\_MASK\_LE\_ADVERTISING\_REPORT BT\_EVT\_BIT(1)

[ 3953](hci__types_8h.md#ab1988671f4017f6434dc0438b2e8b9f6)#define BT\_EVT\_MASK\_LE\_CONN\_UPDATE\_COMPLETE BT\_EVT\_BIT(2)

[ 3954](hci__types_8h.md#adba1a3a872ee26a41218c9104e9f957b)#define BT\_EVT\_MASK\_LE\_REMOTE\_FEAT\_COMPLETE BT\_EVT\_BIT(3)

[ 3955](hci__types_8h.md#ab495948af67d01208eff1adb9a33e489)#define BT\_EVT\_MASK\_LE\_LTK\_REQUEST BT\_EVT\_BIT(4)

[ 3956](hci__types_8h.md#ac3eeaa0610a6ac6d3b57880042071f2a)#define BT\_EVT\_MASK\_LE\_CONN\_PARAM\_REQ BT\_EVT\_BIT(5)

[ 3957](hci__types_8h.md#a73489ce7067d812e8443e242ee53a5e6)#define BT\_EVT\_MASK\_LE\_DATA\_LEN\_CHANGE BT\_EVT\_BIT(6)

[ 3958](hci__types_8h.md#a281d70b2b596b918972b59e684b6a476)#define BT\_EVT\_MASK\_LE\_P256\_PUBLIC\_KEY\_COMPLETE BT\_EVT\_BIT(7)

[ 3959](hci__types_8h.md#afbe64037a16680397614ba2db136b452)#define BT\_EVT\_MASK\_LE\_GENERATE\_DHKEY\_COMPLETE BT\_EVT\_BIT(8)

[ 3960](hci__types_8h.md#afb3b477cb835e60c3e77237451ebae5b)#define BT\_EVT\_MASK\_LE\_ENH\_CONN\_COMPLETE BT\_EVT\_BIT(9)

[ 3961](hci__types_8h.md#a3e84268b1e701ae37c77e95847490222)#define BT\_EVT\_MASK\_LE\_DIRECT\_ADV\_REPORT BT\_EVT\_BIT(10)

[ 3962](hci__types_8h.md#ab5f6014468b107486aba04ba698453ed)#define BT\_EVT\_MASK\_LE\_PHY\_UPDATE\_COMPLETE BT\_EVT\_BIT(11)

[ 3963](hci__types_8h.md#a1d7fc1a3ea229622560de8cf0bb63a81)#define BT\_EVT\_MASK\_LE\_EXT\_ADVERTISING\_REPORT BT\_EVT\_BIT(12)

[ 3964](hci__types_8h.md#a96142f5d79029a93a99152ade46fc005)#define BT\_EVT\_MASK\_LE\_PER\_ADV\_SYNC\_ESTABLISHED BT\_EVT\_BIT(13)

[ 3965](hci__types_8h.md#ad7fc62afd0e1e3dc040567d91320e18e)#define BT\_EVT\_MASK\_LE\_PER\_ADVERTISING\_REPORT BT\_EVT\_BIT(14)

[ 3966](hci__types_8h.md#ae78587797f24987f36c348fe790438b2)#define BT\_EVT\_MASK\_LE\_PER\_ADV\_SYNC\_LOST BT\_EVT\_BIT(15)

[ 3967](hci__types_8h.md#a372f6b8e355972d63e5f9ff45a486e9d)#define BT\_EVT\_MASK\_LE\_SCAN\_TIMEOUT BT\_EVT\_BIT(16)

[ 3968](hci__types_8h.md#a11330b1b6847d77d3ba88e1de0aaa36e)#define BT\_EVT\_MASK\_LE\_ADV\_SET\_TERMINATED BT\_EVT\_BIT(17)

[ 3969](hci__types_8h.md#a3f13865e913a1c6afb6d8d05a6d84608)#define BT\_EVT\_MASK\_LE\_SCAN\_REQ\_RECEIVED BT\_EVT\_BIT(18)

[ 3970](hci__types_8h.md#acee0428356c4853fe664709fc1675f02)#define BT\_EVT\_MASK\_LE\_CHAN\_SEL\_ALGO BT\_EVT\_BIT(19)

[ 3971](hci__types_8h.md#a6ef13decc171530c00f12b0226fa9ed1)#define BT\_EVT\_MASK\_LE\_CONNECTIONLESS\_IQ\_REPORT BT\_EVT\_BIT(20)

[ 3972](hci__types_8h.md#a3b2f133db5641414b95bfd953d715ff3)#define BT\_EVT\_MASK\_LE\_CONNECTION\_IQ\_REPORT BT\_EVT\_BIT(21)

[ 3973](hci__types_8h.md#afbd3991be814ec6462d62fbc4c898ac0)#define BT\_EVT\_MASK\_LE\_CTE\_REQUEST\_FAILED BT\_EVT\_BIT(22)

[ 3974](hci__types_8h.md#a5b2139ce8847bfcdbcd99c3241fb5ea2)#define BT\_EVT\_MASK\_LE\_PAST\_RECEIVED BT\_EVT\_BIT(23)

[ 3975](hci__types_8h.md#a9e41b4cb965576490fb39f7dc396722f)#define BT\_EVT\_MASK\_LE\_CIS\_ESTABLISHED BT\_EVT\_BIT(24)

[ 3976](hci__types_8h.md#aa24e9569ace049098a6d822ad7433e26)#define BT\_EVT\_MASK\_LE\_CIS\_REQ BT\_EVT\_BIT(25)

[ 3977](hci__types_8h.md#a447ff4a3e4dfba390ce9729e45abb410)#define BT\_EVT\_MASK\_LE\_BIG\_COMPLETE BT\_EVT\_BIT(26)

[ 3978](hci__types_8h.md#ad4b775d48bfa14c00c78ac1fbb8f2a2a)#define BT\_EVT\_MASK\_LE\_BIG\_TERMINATED BT\_EVT\_BIT(27)

[ 3979](hci__types_8h.md#ab88b8bcde1d07b5f16c55c4cbf4fd20d)#define BT\_EVT\_MASK\_LE\_BIG\_SYNC\_ESTABLISHED BT\_EVT\_BIT(28)

[ 3980](hci__types_8h.md#a87abdedde8bd43f845fe604c80612ca0)#define BT\_EVT\_MASK\_LE\_BIG\_SYNC\_LOST BT\_EVT\_BIT(29)

[ 3981](hci__types_8h.md#a01e518d3bb3d4f99c335743362a84080)#define BT\_EVT\_MASK\_LE\_REQ\_PEER\_SCA\_COMPLETE BT\_EVT\_BIT(30)

[ 3982](hci__types_8h.md#a6aad398435aa48ba67f6917bca2a690e)#define BT\_EVT\_MASK\_LE\_PATH\_LOSS\_THRESHOLD BT\_EVT\_BIT(31)

[ 3983](hci__types_8h.md#a7f9d3cdf0de067ad408bec600b9a691f)#define BT\_EVT\_MASK\_LE\_TRANSMIT\_POWER\_REPORTING BT\_EVT\_BIT(32)

[ 3984](hci__types_8h.md#aff9c37de1e55e6a7085b3a521f34d3e0)#define BT\_EVT\_MASK\_LE\_BIGINFO\_ADV\_REPORT BT\_EVT\_BIT(33)

[ 3985](hci__types_8h.md#a8a52784fd872a8ee6f666c31e846411d)#define BT\_EVT\_MASK\_LE\_SUBRATE\_CHANGE BT\_EVT\_BIT(34)

3986

[ 3987](hci__types_8h.md#a92a360ad268c29e1616de1e16748eb44)#define BT\_EVT\_MASK\_LE\_PER\_ADV\_SYNC\_ESTABLISHED\_V2 BT\_EVT\_BIT(35)

[ 3988](hci__types_8h.md#ad78d5a027581dee52c54bb3f5a19b68d)#define BT\_EVT\_MASK\_LE\_PER\_ADVERTISING\_REPORT\_V2 BT\_EVT\_BIT(36)

[ 3989](hci__types_8h.md#a93aec31c1636fec90b609981736eb2de)#define BT\_EVT\_MASK\_LE\_PAST\_RECEIVED\_V2 BT\_EVT\_BIT(37)

[ 3990](hci__types_8h.md#af0e2c2e66bdac52fbe5e9c91ca26fe49)#define BT\_EVT\_MASK\_LE\_PER\_ADV\_SUBEVENT\_DATA\_REQ BT\_EVT\_BIT(38)

[ 3991](hci__types_8h.md#ab8a9486fedec169e4d44b249f2445acf)#define BT\_EVT\_MASK\_LE\_PER\_ADV\_RESPONSE\_REPORT BT\_EVT\_BIT(39)

[ 3992](hci__types_8h.md#a8b40a701334d25741a6e17ffd86576ad)#define BT\_EVT\_MASK\_LE\_ENH\_CONN\_COMPLETE\_V2 BT\_EVT\_BIT(40)

[ 3993](hci__types_8h.md#a1b02618f1fbfb3a710fd413f205da9a6)#define BT\_EVT\_MASK\_LE\_CIS\_ESTABLISHED\_V2 BT\_EVT\_BIT(41)

3994

[ 3995](hci__types_8h.md#a97d1b704b1638fb85fa4da6f6d31e209)#define BT\_EVT\_MASK\_LE\_CS\_READ\_REMOTE\_SUPPORTED\_CAPABILITIES\_COMPLETE BT\_EVT\_BIT(43)

[ 3996](hci__types_8h.md#a406cdb92d8c6524aca8971425bab7baa)#define BT\_EVT\_MASK\_LE\_CS\_READ\_REMOTE\_FAE\_TABLE\_COMPLETE BT\_EVT\_BIT(44)

[ 3997](hci__types_8h.md#a07b9cc5a2fcc73d56590a034977cf3a0)#define BT\_EVT\_MASK\_LE\_CS\_SECURITY\_ENABLE\_COMPLETE BT\_EVT\_BIT(45)

[ 3998](hci__types_8h.md#abe6f94ab4bae0d34f23e27c0948e3a21)#define BT\_EVT\_MASK\_LE\_CS\_CONFIG\_COMPLETE BT\_EVT\_BIT(46)

[ 3999](hci__types_8h.md#affbe9c98cf94e50673a2a59c8fb68256)#define BT\_EVT\_MASK\_LE\_CS\_PROCEDURE\_ENABLE\_COMPLETE BT\_EVT\_BIT(47)

[ 4000](hci__types_8h.md#a040ef537fe66f923dc3c344fee023002)#define BT\_EVT\_MASK\_LE\_CS\_SUBEVENT\_RESULT BT\_EVT\_BIT(48)

[ 4001](hci__types_8h.md#a226c276713e3cf16108e4a66fad6db79)#define BT\_EVT\_MASK\_LE\_CS\_SUBEVENT\_RESULT\_CONTINUE BT\_EVT\_BIT(49)

[ 4002](hci__types_8h.md#a8a6ec9510323355aa003cb8be519be7d)#define BT\_EVT\_MASK\_LE\_CS\_TEST\_END\_COMPLETE BT\_EVT\_BIT(50)

4003

[ 4005](hci__types_8h.md#a27c890210eded48f159073cccef8582a)#define BT\_HCI\_ERR\_SUCCESS 0x00

[ 4006](hci__types_8h.md#a376012d3b8f7814870e3f03f6cbabb89)#define BT\_HCI\_ERR\_UNKNOWN\_CMD 0x01

[ 4007](hci__types_8h.md#afd68afeb0296e3af363d7d60eaf4e9a1)#define BT\_HCI\_ERR\_UNKNOWN\_CONN\_ID 0x02

[ 4008](hci__types_8h.md#a5dfcb0d206b98be7eacdc67547bb8a2c)#define BT\_HCI\_ERR\_HW\_FAILURE 0x03

[ 4009](hci__types_8h.md#a1e89c8eb63dee6bd720ef9354c867519)#define BT\_HCI\_ERR\_PAGE\_TIMEOUT 0x04

[ 4010](hci__types_8h.md#a070d51dd0de3288f9811f90a558c889b)#define BT\_HCI\_ERR\_AUTH\_FAIL 0x05

[ 4011](hci__types_8h.md#a39f129aefe81c2d06f70552ace008a15)#define BT\_HCI\_ERR\_PIN\_OR\_KEY\_MISSING 0x06

[ 4012](hci__types_8h.md#ac54f84b29901185822f6bad2edf86b61)#define BT\_HCI\_ERR\_MEM\_CAPACITY\_EXCEEDED 0x07

[ 4013](hci__types_8h.md#ab702caf5cd73431cc9aede8891f74610)#define BT\_HCI\_ERR\_CONN\_TIMEOUT 0x08

[ 4014](hci__types_8h.md#a490798f4f1e226e66475f0fb84cfbcd5)#define BT\_HCI\_ERR\_CONN\_LIMIT\_EXCEEDED 0x09

[ 4015](hci__types_8h.md#a56a3d3d9d7798334b29c02214a2e73bf)#define BT\_HCI\_ERR\_SYNC\_CONN\_LIMIT\_EXCEEDED 0x0a

[ 4016](hci__types_8h.md#abcf4cd921e304758cc969a83445d70ec)#define BT\_HCI\_ERR\_CONN\_ALREADY\_EXISTS 0x0b

[ 4017](hci__types_8h.md#a5ee9f2e9625d732e84e5ef593bb2a3f9)#define BT\_HCI\_ERR\_CMD\_DISALLOWED 0x0c

[ 4018](hci__types_8h.md#a0efddbffb31b93158b10a3f678f94f4e)#define BT\_HCI\_ERR\_INSUFFICIENT\_RESOURCES 0x0d

[ 4019](hci__types_8h.md#a08d4bdfc189bccbdb97a51b0089e77a0)#define BT\_HCI\_ERR\_INSUFFICIENT\_SECURITY 0x0e

[ 4020](hci__types_8h.md#a366f85b3bcb3f578b2572149c69b7fc0)#define BT\_HCI\_ERR\_BD\_ADDR\_UNACCEPTABLE 0x0f

[ 4021](hci__types_8h.md#ae4682cbd7a9b9dedd25926efe029c0d7)#define BT\_HCI\_ERR\_CONN\_ACCEPT\_TIMEOUT 0x10

[ 4022](hci__types_8h.md#af73db17855859676827bad84e2ccbabe)#define BT\_HCI\_ERR\_UNSUPP\_FEATURE\_PARAM\_VAL 0x11

[ 4023](hci__types_8h.md#afc76c774f5e71423eb9fea910d1860e9)#define BT\_HCI\_ERR\_INVALID\_PARAM 0x12

[ 4024](hci__types_8h.md#ac0e3b44027180d7a2dedb59395c4b111)#define BT\_HCI\_ERR\_REMOTE\_USER\_TERM\_CONN 0x13

[ 4025](hci__types_8h.md#a5eeadfb220c24b2e7f5ce3fd21e5d46a)#define BT\_HCI\_ERR\_REMOTE\_LOW\_RESOURCES 0x14

[ 4026](hci__types_8h.md#a083f1fc52300f7e47c2f8d4e50551851)#define BT\_HCI\_ERR\_REMOTE\_POWER\_OFF 0x15

[ 4027](hci__types_8h.md#a0f07b75be216456e9370485dca0da992)#define BT\_HCI\_ERR\_LOCALHOST\_TERM\_CONN 0x16

[ 4028](hci__types_8h.md#a11d42e0347cc9d1d50ccd45c2e9a39f6)#define BT\_HCI\_ERR\_REPEATED\_ATTEMPTS 0x17

[ 4029](hci__types_8h.md#a60823c337c91aa95348dcae250a83977)#define BT\_HCI\_ERR\_PAIRING\_NOT\_ALLOWED 0x18

[ 4030](hci__types_8h.md#a0f81b5c19358982bd33c527239200b08)#define BT\_HCI\_ERR\_UNKNOWN\_LMP\_PDU 0x19

[ 4031](hci__types_8h.md#a516751f02bd497a020783f69bcf71453)#define BT\_HCI\_ERR\_UNSUPP\_REMOTE\_FEATURE 0x1a

[ 4032](hci__types_8h.md#a5e28f04c454361508bc791c6ce292bc2)#define BT\_HCI\_ERR\_SCO\_OFFSET\_REJECTED 0x1b

[ 4033](hci__types_8h.md#a5093c6357fcefd1ccdcbdf9a99f18e7c)#define BT\_HCI\_ERR\_SCO\_INTERVAL\_REJECTED 0x1c

[ 4034](hci__types_8h.md#ad8f77a43360e8ab2e6c71a103e14c951)#define BT\_HCI\_ERR\_SCO\_AIR\_MODE\_REJECTED 0x1d

[ 4035](hci__types_8h.md#a943fe81109d82983018b558b9274f9a3)#define BT\_HCI\_ERR\_INVALID\_LL\_PARAM 0x1e

[ 4036](hci__types_8h.md#ab3833bbb70b6a2e57870d8243f528b90)#define BT\_HCI\_ERR\_UNSPECIFIED 0x1f

[ 4037](hci__types_8h.md#af1fa61561b6a91d08f81e9c19cbe89f7)#define BT\_HCI\_ERR\_UNSUPP\_LL\_PARAM\_VAL 0x20

[ 4038](hci__types_8h.md#a070d016f54e7f5f0a7ca6d8c8218505f)#define BT\_HCI\_ERR\_ROLE\_CHANGE\_NOT\_ALLOWED 0x21

[ 4039](hci__types_8h.md#a6317763780d9c81e6752d5a2c8ce3172)#define BT\_HCI\_ERR\_LL\_RESP\_TIMEOUT 0x22

[ 4040](hci__types_8h.md#a0e280074290680d62ad4721384bb603e)#define BT\_HCI\_ERR\_LL\_PROC\_COLLISION 0x23

[ 4041](hci__types_8h.md#a47c02d44d40d785db6fee28c88d3c5b4)#define BT\_HCI\_ERR\_LMP\_PDU\_NOT\_ALLOWED 0x24

[ 4042](hci__types_8h.md#aeb5499a707e1c41cbd9db882cfdf0677)#define BT\_HCI\_ERR\_ENC\_MODE\_NOT\_ACCEPTABLE 0x25

[ 4043](hci__types_8h.md#aee97132db4398e2db0a6e115ca20b9b4)#define BT\_HCI\_ERR\_LINK\_KEY\_CANNOT\_BE\_CHANGED 0x26

[ 4044](hci__types_8h.md#a0e02fd84d7a355f42fe006c756936d78)#define BT\_HCI\_ERR\_REQUESTED\_QOS\_NOT\_SUPPORTED 0x27

[ 4045](hci__types_8h.md#a2d336db995ab250f94de66da952c642c)#define BT\_HCI\_ERR\_INSTANT\_PASSED 0x28

[ 4046](hci__types_8h.md#a059c7d5619823eddf2c541b40a6464cb)#define BT\_HCI\_ERR\_PAIRING\_NOT\_SUPPORTED 0x29

[ 4047](hci__types_8h.md#a3b461d65baa95f8f984b212264dc5072)#define BT\_HCI\_ERR\_DIFF\_TRANS\_COLLISION 0x2a

[ 4048](hci__types_8h.md#a37c2fdc6b32b4a2cb70d5c17dfbe262b)#define BT\_HCI\_ERR\_QOS\_UNACCEPTABLE\_PARAM 0x2c

[ 4049](hci__types_8h.md#a88363d1eb1c0d13dc8138af8edc76abc)#define BT\_HCI\_ERR\_QOS\_REJECTED 0x2d

[ 4050](hci__types_8h.md#a3b9fc13a3e3ecc9f0f4431487c0301b5)#define BT\_HCI\_ERR\_CHAN\_ASSESS\_NOT\_SUPPORTED 0x2e

[ 4051](hci__types_8h.md#a334efee11bd7086e0611c8f628d65abb)#define BT\_HCI\_ERR\_INSUFF\_SECURITY 0x2f

[ 4052](hci__types_8h.md#a29c763a2e70820fae7e2e825d22f4991)#define BT\_HCI\_ERR\_PARAM\_OUT\_OF\_MANDATORY\_RANGE 0x30

[ 4053](hci__types_8h.md#ac9c9a68e696e038d7b05af89e3a0c7b6)#define BT\_HCI\_ERR\_ROLE\_SWITCH\_PENDING 0x32

[ 4054](hci__types_8h.md#ac6244ca7123879ef039c2c5486d50d41)#define BT\_HCI\_ERR\_RESERVED\_SLOT\_VIOLATION 0x34

[ 4055](hci__types_8h.md#ab40a919a2d87376f2aca6d2ea3f55758)#define BT\_HCI\_ERR\_ROLE\_SWITCH\_FAILED 0x35

[ 4056](hci__types_8h.md#a1b7094ad185ed22542f370ab1101c1ae)#define BT\_HCI\_ERR\_EXT\_INQ\_RESP\_TOO\_LARGE 0x36

[ 4057](hci__types_8h.md#afd8840ad198dfdb666bf24851a478c70)#define BT\_HCI\_ERR\_SIMPLE\_PAIR\_NOT\_SUPP\_BY\_HOST 0x37

[ 4058](hci__types_8h.md#a107d85e39fec3146d6b017deb047571b)#define BT\_HCI\_ERR\_HOST\_BUSY\_PAIRING 0x38

[ 4059](hci__types_8h.md#a1adf558f8f606612ca96bdbbb55e0e78)#define BT\_HCI\_ERR\_CONN\_REJECTED\_DUE\_TO\_NO\_CHAN 0x39

[ 4060](hci__types_8h.md#a33167856fe838b833fe42d92c3eac4eb)#define BT\_HCI\_ERR\_CONTROLLER\_BUSY 0x3a

[ 4061](hci__types_8h.md#a712e214942c0d151597ce04e9d0df453)#define BT\_HCI\_ERR\_UNACCEPT\_CONN\_PARAM 0x3b

[ 4062](hci__types_8h.md#abfa408d8366ff3cae1cd35fffcda30c0)#define BT\_HCI\_ERR\_ADV\_TIMEOUT 0x3c

[ 4063](hci__types_8h.md#a71dd49b1b5dc51ad7db8da9aecf9ff06)#define BT\_HCI\_ERR\_TERM\_DUE\_TO\_MIC\_FAIL 0x3d

[ 4064](hci__types_8h.md#ac6c44be2e737d7a10b5c886c69d6b1a5)#define BT\_HCI\_ERR\_CONN\_FAIL\_TO\_ESTAB 0x3e

[ 4065](hci__types_8h.md#af0b9f71a874ca2c3587256c7f665e9fa)#define BT\_HCI\_ERR\_MAC\_CONN\_FAILED 0x3f

[ 4066](hci__types_8h.md#a6e9a4db5962d79b5a7f43a4c2919c9e9)#define BT\_HCI\_ERR\_CLOCK\_ADJUST\_REJECTED 0x40

[ 4067](hci__types_8h.md#a9e7483e2d7f46981e9d1fcdbb8a7515c)#define BT\_HCI\_ERR\_SUBMAP\_NOT\_DEFINED 0x41

[ 4068](hci__types_8h.md#a7646bc91f5dbb28c5eeda7e1828f2e30)#define BT\_HCI\_ERR\_UNKNOWN\_ADV\_IDENTIFIER 0x42

[ 4069](hci__types_8h.md#a86b092455cfd220d48af2bea04900b5b)#define BT\_HCI\_ERR\_LIMIT\_REACHED 0x43

[ 4070](hci__types_8h.md#a85433a7b3bcac0a507d7f6376a084142)#define BT\_HCI\_ERR\_OP\_CANCELLED\_BY\_HOST 0x44

[ 4071](hci__types_8h.md#ab63f7d0c79aaa57abf59aa18e112345f)#define BT\_HCI\_ERR\_PACKET\_TOO\_LONG 0x45

[ 4072](hci__types_8h.md#a9c62f8f73470a3157a60f8d6d56b22a4)#define BT\_HCI\_ERR\_TOO\_LATE 0x46

[ 4073](hci__types_8h.md#a8dcf345b1fea1364f490f40963992cd6)#define BT\_HCI\_ERR\_TOO\_EARLY 0x47

4074

4075#ifdef \_\_cplusplus

4076}

4077#endif

4078

4079#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_HCI\_TYPES\_H\_ \*/

[addr.h](addr_8h.md)

Bluetooth device address definitions and utilities.

[types.h](include_2zephyr_2types_8h.md)

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

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[string.h](string_8h.md)

[bt\_addr\_le\_t](structbt__addr__le__t.md)

Bluetooth LE Device Address.

**Definition** addr.h:49

[bt\_addr\_t](structbt__addr__t.md)

Bluetooth Device Address.

**Definition** addr.h:40

[bt\_hci\_acl\_hdr](structbt__hci__acl__hdr.md)

**Definition** hci\_types.h:83

[bt\_hci\_acl\_hdr::handle](structbt__hci__acl__hdr.md#a8c88ef62a848699e06c49f97e1169363)

uint16\_t handle

**Definition** hci\_types.h:84

[bt\_hci\_acl\_hdr::len](structbt__hci__acl__hdr.md#af55b9c9256f35ada5786e9e5dd1d01bf)

uint16\_t len

**Definition** hci\_types.h:85

[bt\_hci\_cis\_params\_test](structbt__hci__cis__params__test.md)

**Definition** hci\_types.h:2163

[bt\_hci\_cis\_params\_test::cis\_id](structbt__hci__cis__params__test.md#a0a215b4dffac2aae4ae4310c54de073e)

uint8\_t cis\_id

**Definition** hci\_types.h:2164

[bt\_hci\_cis\_params\_test::c\_sdu](structbt__hci__cis__params__test.md#a98a120efb1495dd90858bef45eb95891)

uint16\_t c\_sdu

**Definition** hci\_types.h:2166

[bt\_hci\_cis\_params\_test::c\_phy](structbt__hci__cis__params__test.md#aa7ba56fb91718d43ca30ff643757e08e)

uint8\_t c\_phy

**Definition** hci\_types.h:2170

[bt\_hci\_cis\_params\_test::p\_phy](structbt__hci__cis__params__test.md#ab636126046023a329451673c57b4ce96)

uint8\_t p\_phy

**Definition** hci\_types.h:2171

[bt\_hci\_cis\_params\_test::p\_pdu](structbt__hci__cis__params__test.md#abce4bd6045642b4d29668865655f1548)

uint16\_t p\_pdu

**Definition** hci\_types.h:2169

[bt\_hci\_cis\_params\_test::p\_bn](structbt__hci__cis__params__test.md#ac66b7183d8148250246f17a157dc3d29)

uint8\_t p\_bn

**Definition** hci\_types.h:2173

[bt\_hci\_cis\_params\_test::nse](structbt__hci__cis__params__test.md#ad0cc6d393a536cb3cd83d456b950fc52)

uint8\_t nse

**Definition** hci\_types.h:2165

[bt\_hci\_cis\_params\_test::c\_pdu](structbt__hci__cis__params__test.md#adc092a44b58bcc78f3dfe88528ca724c)

uint16\_t c\_pdu

**Definition** hci\_types.h:2168

[bt\_hci\_cis\_params\_test::c\_bn](structbt__hci__cis__params__test.md#adf5dda2be46f3c2c1a1fe398672416ff)

uint8\_t c\_bn

**Definition** hci\_types.h:2172

[bt\_hci\_cis\_params\_test::p\_sdu](structbt__hci__cis__params__test.md#aefeca493efe0141590570e8a44bb8f8d)

uint16\_t p\_sdu

**Definition** hci\_types.h:2167

[bt\_hci\_cis\_params](structbt__hci__cis__params.md)

**Definition** hci\_types.h:2132

[bt\_hci\_cis\_params::p\_phy](structbt__hci__cis__params.md#a18bc8e4b531d9fd16f18e10a0d931f6c)

uint8\_t p\_phy

**Definition** hci\_types.h:2137

[bt\_hci\_cis\_params::c\_phy](structbt__hci__cis__params.md#a5a5fcd9276d912446fe84d875ae74c2f)

uint8\_t c\_phy

**Definition** hci\_types.h:2136

[bt\_hci\_cis\_params::cis\_id](structbt__hci__cis__params.md#a6dcfca11d7f827b1b7a62b507620d4de)

uint8\_t cis\_id

**Definition** hci\_types.h:2133

[bt\_hci\_cis\_params::c\_sdu](structbt__hci__cis__params.md#a8a85b914ba5585c6b362da3deb8d42d9)

uint16\_t c\_sdu

**Definition** hci\_types.h:2134

[bt\_hci\_cis\_params::c\_rtn](structbt__hci__cis__params.md#aa7fa628692f959db63788c6580cc5c66)

uint8\_t c\_rtn

**Definition** hci\_types.h:2138

[bt\_hci\_cis\_params::p\_rtn](structbt__hci__cis__params.md#ad55e197ccb70c83fcd4c1c6ba485f468)

uint8\_t p\_rtn

**Definition** hci\_types.h:2139

[bt\_hci\_cis\_params::p\_sdu](structbt__hci__cis__params.md#ae2bffbaf0c4dde9144a7887177b3ffdb)

uint16\_t p\_sdu

**Definition** hci\_types.h:2135

[bt\_hci\_cis](structbt__hci__cis.md)

**Definition** hci\_types.h:2198

[bt\_hci\_cis::acl\_handle](structbt__hci__cis.md#a754c3c75c0ad13a11d89fa3347112e2c)

uint16\_t acl\_handle

**Definition** hci\_types.h:2200

[bt\_hci\_cis::cis\_handle](structbt__hci__cis.md#a84165d526c10a91fa42d306276d97c74)

uint16\_t cis\_handle

**Definition** hci\_types.h:2199

[bt\_hci\_cmd\_hdr](structbt__hci__cmd__hdr.md)

**Definition** hci\_types.h:132

[bt\_hci\_cmd\_hdr::opcode](structbt__hci__cmd__hdr.md#a09c63aab094ca0f39bab44708fdb83e4)

uint16\_t opcode

**Definition** hci\_types.h:133

[bt\_hci\_cmd\_hdr::param\_len](structbt__hci__cmd__hdr.md#afe2a97da8b473cafd3cc4e5e52dadf93)

uint8\_t param\_len

**Definition** hci\_types.h:134

[bt\_hci\_codec\_capability\_info](structbt__hci__codec__capability__info.md)

**Definition** hci\_types.h:983

[bt\_hci\_codec\_capability\_info::length](structbt__hci__codec__capability__info.md#a24516347742a8fd9f3386d78b66a4e81)

uint8\_t length

**Definition** hci\_types.h:984

[bt\_hci\_codec\_capability\_info::data](structbt__hci__codec__capability__info.md#ac53f02f2abdb832ed82da35a36abc323)

uint8\_t data[0]

**Definition** hci\_types.h:985

[bt\_hci\_cp\_accept\_conn\_req](structbt__hci__cp__accept__conn__req.md)

**Definition** hci\_types.h:416

[bt\_hci\_cp\_accept\_conn\_req::role](structbt__hci__cp__accept__conn__req.md#a95e445018d1b9da5a914f0845bb9dbad)

uint8\_t role

**Definition** hci\_types.h:418

[bt\_hci\_cp\_accept\_conn\_req::bdaddr](structbt__hci__cp__accept__conn__req.md#aa2954d98fdd42882cf7095e4ce7a3dc5)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:417

[bt\_hci\_cp\_accept\_sync\_conn\_req](structbt__hci__cp__accept__sync__conn__req.md)

**Definition** hci\_types.h:433

[bt\_hci\_cp\_accept\_sync\_conn\_req::max\_latency](structbt__hci__cp__accept__sync__conn__req.md#a4ba6dffd840ef868524b490d227fd085)

uint16\_t max\_latency

**Definition** hci\_types.h:437

[bt\_hci\_cp\_accept\_sync\_conn\_req::tx\_bandwidth](structbt__hci__cp__accept__sync__conn__req.md#a53fe4c6d61dbb99f99aa445b2c47a8ef)

uint32\_t tx\_bandwidth

**Definition** hci\_types.h:435

[bt\_hci\_cp\_accept\_sync\_conn\_req::bdaddr](structbt__hci__cp__accept__sync__conn__req.md#a6a5a56d3a9d1a6d1064e7bd4c9fd333e)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:434

[bt\_hci\_cp\_accept\_sync\_conn\_req::pkt\_type](structbt__hci__cp__accept__sync__conn__req.md#ab5d9c27ebdf45fb54b0c6330b5b095be)

uint16\_t pkt\_type

**Definition** hci\_types.h:440

[bt\_hci\_cp\_accept\_sync\_conn\_req::retrans\_effort](structbt__hci__cp__accept__sync__conn__req.md#ab5ece67c5a1e62fc4124556eef743c26)

uint8\_t retrans\_effort

**Definition** hci\_types.h:439

[bt\_hci\_cp\_accept\_sync\_conn\_req::rx\_bandwidth](structbt__hci__cp__accept__sync__conn__req.md#aceda6dbd3e221ad080850e9635886a86)

uint32\_t rx\_bandwidth

**Definition** hci\_types.h:436

[bt\_hci\_cp\_accept\_sync\_conn\_req::content\_format](structbt__hci__cp__accept__sync__conn__req.md#adba31b588bf12e852cc43b85c006aaa3)

uint16\_t content\_format

**Definition** hci\_types.h:438

[bt\_hci\_cp\_auth\_requested](structbt__hci__cp__auth__requested.md)

**Definition** hci\_types.h:481

[bt\_hci\_cp\_auth\_requested::handle](structbt__hci__cp__auth__requested.md#a079490f8f8569e281ce16f13847cbf33)

uint16\_t handle

**Definition** hci\_types.h:482

[bt\_hci\_cp\_codec\_id](structbt__hci__cp__codec__id.md)

**Definition** hci\_types.h:971

[bt\_hci\_cp\_codec\_id::vs\_codec\_id](structbt__hci__cp__codec__id.md#a70296440c202544af11db2dc8e80fc5b)

uint16\_t vs\_codec\_id

**Definition** hci\_types.h:974

[bt\_hci\_cp\_codec\_id::company\_id](structbt__hci__cp__codec__id.md#a98fd438270a64d843fa27c7c196645df)

uint16\_t company\_id

**Definition** hci\_types.h:973

[bt\_hci\_cp\_codec\_id::coding\_format](structbt__hci__cp__codec__id.md#aec80c74b12edb9c63330cc5a404eed5d)

uint8\_t coding\_format

**Definition** hci\_types.h:972

[bt\_hci\_cp\_configure\_data\_path](structbt__hci__cp__configure__data__path.md)

**Definition** hci\_types.h:816

[bt\_hci\_cp\_configure\_data\_path::vs\_config\_len](structbt__hci__cp__configure__data__path.md#a2573fe029e1774bf5fa7e8cffff08cec)

uint8\_t vs\_config\_len

**Definition** hci\_types.h:819

[bt\_hci\_cp\_configure\_data\_path::data\_path\_dir](structbt__hci__cp__configure__data__path.md#a528ba2bd5a220d1b7db064f8b51a8718)

uint8\_t data\_path\_dir

**Definition** hci\_types.h:817

[bt\_hci\_cp\_configure\_data\_path::data\_path\_id](structbt__hci__cp__configure__data__path.md#a92967e6b5258b2acd6d82bfbfb8b7940)

uint8\_t data\_path\_id

**Definition** hci\_types.h:818

[bt\_hci\_cp\_configure\_data\_path::vs\_config](structbt__hci__cp__configure__data__path.md#aa79c4aa6603b09f49a8c7f216f135e6e)

uint8\_t vs\_config[0]

**Definition** hci\_types.h:820

[bt\_hci\_cp\_connect\_cancel](structbt__hci__cp__connect__cancel.md)

**Definition** hci\_types.h:407

[bt\_hci\_cp\_connect\_cancel::bdaddr](structbt__hci__cp__connect__cancel.md#a2adaf1b708689525e44e9a9572f5f357)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:408

[bt\_hci\_cp\_connect](structbt__hci__cp__connect.md)

**Definition** hci\_types.h:391

[bt\_hci\_cp\_connect::pscan\_rep\_mode](structbt__hci__cp__connect.md#a35b0e1f73f696aae2ca519e16d7bb668)

uint8\_t pscan\_rep\_mode

**Definition** hci\_types.h:394

[bt\_hci\_cp\_connect::packet\_type](structbt__hci__cp__connect.md#a652a4e01641893a8588110dc505ceea0)

uint16\_t packet\_type

**Definition** hci\_types.h:393

[bt\_hci\_cp\_connect::bdaddr](structbt__hci__cp__connect.md#a6f0753aad19d4c9591fa74152d151aa9)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:392

[bt\_hci\_cp\_connect::allow\_role\_switch](structbt__hci__cp__connect.md#a7a3d772bfd4c83236f9f1ad657e33f17)

uint8\_t allow\_role\_switch

**Definition** hci\_types.h:397

[bt\_hci\_cp\_connect::clock\_offset](structbt__hci__cp__connect.md#ac379ec381ad4cf6760750203924e5dda)

uint16\_t clock\_offset

**Definition** hci\_types.h:396

[bt\_hci\_cp\_connect::reserved](structbt__hci__cp__connect.md#aef01fcac1b9792353bd8095e6911d6c3)

uint8\_t reserved

**Definition** hci\_types.h:395

[bt\_hci\_cp\_disconnect](structbt__hci__cp__disconnect.md)

**Definition** hci\_types.h:401

[bt\_hci\_cp\_disconnect::reason](structbt__hci__cp__disconnect.md#a8e10edb1e700c1ef38f39bf20b9b374f)

uint8\_t reason

**Definition** hci\_types.h:403

[bt\_hci\_cp\_disconnect::handle](structbt__hci__cp__disconnect.md#a9cb5bcd135082c37a19cce57ffa123ff)

uint16\_t handle

**Definition** hci\_types.h:402

[bt\_hci\_cp\_host\_buffer\_size](structbt__hci__cp__host__buffer__size.md)

**Definition** hci\_types.h:749

[bt\_hci\_cp\_host\_buffer\_size::acl\_mtu](structbt__hci__cp__host__buffer__size.md#a07039a81ba81c700a26009ea407744b6)

uint16\_t acl\_mtu

**Definition** hci\_types.h:750

[bt\_hci\_cp\_host\_buffer\_size::sco\_mtu](structbt__hci__cp__host__buffer__size.md#a1b1d8c7f60ecbb13699b815bc8fca550)

uint8\_t sco\_mtu

**Definition** hci\_types.h:751

[bt\_hci\_cp\_host\_buffer\_size::acl\_pkts](structbt__hci__cp__host__buffer__size.md#a8240837fecc7c50461724b697f0eda47)

uint16\_t acl\_pkts

**Definition** hci\_types.h:752

[bt\_hci\_cp\_host\_buffer\_size::sco\_pkts](structbt__hci__cp__host__buffer__size.md#a943252480194e1a8608951be08b6b91c)

uint16\_t sco\_pkts

**Definition** hci\_types.h:753

[bt\_hci\_cp\_host\_num\_completed\_packets](structbt__hci__cp__host__num__completed__packets.md)

**Definition** hci\_types.h:762

[bt\_hci\_cp\_host\_num\_completed\_packets::h](structbt__hci__cp__host__num__completed__packets.md#a127f146b4967de49bc74b90ce1643eb7)

struct bt\_hci\_handle\_count h[0]

**Definition** hci\_types.h:764

[bt\_hci\_cp\_host\_num\_completed\_packets::num\_handles](structbt__hci__cp__host__num__completed__packets.md#a43a42e52757de9ec307e8a828dff416f)

uint8\_t num\_handles

**Definition** hci\_types.h:763

[bt\_hci\_cp\_io\_capability\_neg\_reply](structbt__hci__cp__io__capability__neg__reply.md)

**Definition** hci\_types.h:554

[bt\_hci\_cp\_io\_capability\_neg\_reply::reason](structbt__hci__cp__io__capability__neg__reply.md#a82c54e5ad7fd4a6d81952832ae4de373)

uint8\_t reason

**Definition** hci\_types.h:556

[bt\_hci\_cp\_io\_capability\_neg\_reply::bdaddr](structbt__hci__cp__io__capability__neg__reply.md#a8dba05bc84de2573eaea43ea9e428015)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:555

[bt\_hci\_cp\_io\_capability\_reply](structbt__hci__cp__io__capability__reply.md)

**Definition** hci\_types.h:525

[bt\_hci\_cp\_io\_capability\_reply::capability](structbt__hci__cp__io__capability__reply.md#a0995c81ba1f653c59bda9a444fb17915)

uint8\_t capability

**Definition** hci\_types.h:527

[bt\_hci\_cp\_io\_capability\_reply::authentication](structbt__hci__cp__io__capability__reply.md#a8983418dca3a7725f3b113a4d0ee177e)

uint8\_t authentication

**Definition** hci\_types.h:529

[bt\_hci\_cp\_io\_capability\_reply::oob\_data](structbt__hci__cp__io__capability__reply.md#ac002ea0b276200a15d603b5ac83666e5)

uint8\_t oob\_data

**Definition** hci\_types.h:528

[bt\_hci\_cp\_io\_capability\_reply::bdaddr](structbt__hci__cp__io__capability__reply.md#afbe2bc0c1dcc0791a98068b052aea1f2)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:526

[bt\_hci\_cp\_le\_accept\_cis](structbt__hci__cp__le__accept__cis.md)

**Definition** hci\_types.h:2219

[bt\_hci\_cp\_le\_accept\_cis::handle](structbt__hci__cp__le__accept__cis.md#aec6a6c80403d5827df10cd8722bc12e4)

uint16\_t handle

**Definition** hci\_types.h:2220

[bt\_hci\_cp\_le\_add\_dev\_to\_fal](structbt__hci__cp__le__add__dev__to__fal.md)

**Definition** hci\_types.h:1175

[bt\_hci\_cp\_le\_add\_dev\_to\_fal::addr](structbt__hci__cp__le__add__dev__to__fal.md#a11ec9f3cd9b80f34094e70d8eeb13be3)

bt\_addr\_le\_t addr

**Definition** hci\_types.h:1176

[bt\_hci\_cp\_le\_add\_dev\_to\_per\_adv\_list](structbt__hci__cp__le__add__dev__to__per__adv__list.md)

**Definition** hci\_types.h:1810

[bt\_hci\_cp\_le\_add\_dev\_to\_per\_adv\_list::sid](structbt__hci__cp__le__add__dev__to__per__adv__list.md#a97d9c5dd0cc4b3ab7f6ebfec206b7407)

uint8\_t sid

**Definition** hci\_types.h:1812

[bt\_hci\_cp\_le\_add\_dev\_to\_per\_adv\_list::addr](structbt__hci__cp__le__add__dev__to__per__adv__list.md#ad93d72bfa7e4123ee9728f6bf73b69df)

bt\_addr\_le\_t addr

**Definition** hci\_types.h:1811

[bt\_hci\_cp\_le\_add\_dev\_to\_rl](structbt__hci__cp__le__add__dev__to__rl.md)

**Definition** hci\_types.h:1360

[bt\_hci\_cp\_le\_add\_dev\_to\_rl::peer\_id\_addr](structbt__hci__cp__le__add__dev__to__rl.md#a3daf2041f04381a56c2cbcd4bb33f4c0)

bt\_addr\_le\_t peer\_id\_addr

**Definition** hci\_types.h:1361

[bt\_hci\_cp\_le\_add\_dev\_to\_rl::local\_irk](structbt__hci__cp__le__add__dev__to__rl.md#ab5caa38e6eeab09b4a69084b1890317b)

uint8\_t local\_irk[16]

**Definition** hci\_types.h:1363

[bt\_hci\_cp\_le\_add\_dev\_to\_rl::peer\_irk](structbt__hci__cp__le__add__dev__to__rl.md#aedc27c868a7a4cbd3c175f67db4e3242)

uint8\_t peer\_irk[16]

**Definition** hci\_types.h:1362

[bt\_hci\_cp\_le\_big\_create\_sync](structbt__hci__cp__le__big__create__sync.md)

**Definition** hci\_types.h:2277

[bt\_hci\_cp\_le\_big\_create\_sync::bcode](structbt__hci__cp__le__big__create__sync.md#a053475c3af12e6e37dc4befcf634d68f)

uint8\_t bcode[16]

**Definition** hci\_types.h:2281

[bt\_hci\_cp\_le\_big\_create\_sync::mse](structbt__hci__cp__le__big__create__sync.md#a37050e3eb914ff06495695d44c3fdb50)

uint8\_t mse

**Definition** hci\_types.h:2282

[bt\_hci\_cp\_le\_big\_create\_sync::encryption](structbt__hci__cp__le__big__create__sync.md#a482edf3326e2dd720b14a03609c1256a)

uint8\_t encryption

**Definition** hci\_types.h:2280

[bt\_hci\_cp\_le\_big\_create\_sync::sync\_timeout](structbt__hci__cp__le__big__create__sync.md#a55e83bc3722ce2dbf943879a80ef2872)

uint16\_t sync\_timeout

**Definition** hci\_types.h:2283

[bt\_hci\_cp\_le\_big\_create\_sync::big\_handle](structbt__hci__cp__le__big__create__sync.md#a6692dae077ce1ce4f31bc94b9d391afd)

uint8\_t big\_handle

**Definition** hci\_types.h:2278

[bt\_hci\_cp\_le\_big\_create\_sync::bis](structbt__hci__cp__le__big__create__sync.md#a6d1050c2a0522be215d82d3874fed4b6)

uint8\_t bis[0]

**Definition** hci\_types.h:2285

[bt\_hci\_cp\_le\_big\_create\_sync::sync\_handle](structbt__hci__cp__le__big__create__sync.md#a70b031f24cdf231e5c168b155517eae0)

uint16\_t sync\_handle

**Definition** hci\_types.h:2279

[bt\_hci\_cp\_le\_big\_create\_sync::num\_bis](structbt__hci__cp__le__big__create__sync.md#a7efae2c8dc46d13fb2abca677ac152b0)

uint8\_t num\_bis

**Definition** hci\_types.h:2284

[bt\_hci\_cp\_le\_big\_terminate\_sync](structbt__hci__cp__le__big__terminate__sync.md)

**Definition** hci\_types.h:2289

[bt\_hci\_cp\_le\_big\_terminate\_sync::big\_handle](structbt__hci__cp__le__big__terminate__sync.md#ad7e4de2a9a3222c1bb8fa048cacd06fa)

uint8\_t big\_handle

**Definition** hci\_types.h:2290

[bt\_hci\_cp\_le\_conn\_cte\_req\_enable](structbt__hci__cp__le__conn__cte__req__enable.md)

**Definition** hci\_types.h:1978

[bt\_hci\_cp\_le\_conn\_cte\_req\_enable::requested\_cte\_length](structbt__hci__cp__le__conn__cte__req__enable.md#a4d4e41bbe95457ce5e8ad68ffeb85200)

uint8\_t requested\_cte\_length

**Definition** hci\_types.h:1982

[bt\_hci\_cp\_le\_conn\_cte\_req\_enable::requested\_cte\_type](structbt__hci__cp__le__conn__cte__req__enable.md#a5a7443a86e770de4bf7292d813e966e7)

uint8\_t requested\_cte\_type

**Definition** hci\_types.h:1983

[bt\_hci\_cp\_le\_conn\_cte\_req\_enable::cte\_request\_interval](structbt__hci__cp__le__conn__cte__req__enable.md#a956a1a8794b75e962d03cdcf81847cfc)

uint16\_t cte\_request\_interval

**Definition** hci\_types.h:1981

[bt\_hci\_cp\_le\_conn\_cte\_req\_enable::enable](structbt__hci__cp__le__conn__cte__req__enable.md#aaf38e3d5664d81ae7ac8d3b1bb03c646)

uint8\_t enable

**Definition** hci\_types.h:1980

[bt\_hci\_cp\_le\_conn\_cte\_req\_enable::handle](structbt__hci__cp__le__conn__cte__req__enable.md#af340b3b97f9fb12c24baa38415620b44)

uint16\_t handle

**Definition** hci\_types.h:1979

[bt\_hci\_cp\_le\_conn\_cte\_rsp\_enable](structbt__hci__cp__le__conn__cte__rsp__enable.md)

**Definition** hci\_types.h:1992

[bt\_hci\_cp\_le\_conn\_cte\_rsp\_enable::handle](structbt__hci__cp__le__conn__cte__rsp__enable.md#a9d78072143513020620e02a744d4fa9b)

uint16\_t handle

**Definition** hci\_types.h:1993

[bt\_hci\_cp\_le\_conn\_cte\_rsp\_enable::enable](structbt__hci__cp__le__conn__cte__rsp__enable.md#ae5eaaae211732d772ea53f3936ab32d2)

uint8\_t enable

**Definition** hci\_types.h:1994

[bt\_hci\_cp\_le\_conn\_param\_req\_neg\_reply](structbt__hci__cp__le__conn__param__req__neg__reply.md)

**Definition** hci\_types.h:1307

[bt\_hci\_cp\_le\_conn\_param\_req\_neg\_reply::handle](structbt__hci__cp__le__conn__param__req__neg__reply.md#a0040e4a50c5c5479b539eb0bafb7b305)

uint16\_t handle

**Definition** hci\_types.h:1308

[bt\_hci\_cp\_le\_conn\_param\_req\_neg\_reply::reason](structbt__hci__cp__le__conn__param__req__neg__reply.md#a8c283ac844805224b1ffeb9801e8b14b)

uint8\_t reason

**Definition** hci\_types.h:1309

[bt\_hci\_cp\_le\_conn\_param\_req\_reply](structbt__hci__cp__le__conn__param__req__reply.md)

**Definition** hci\_types.h:1292

[bt\_hci\_cp\_le\_conn\_param\_req\_reply::interval\_min](structbt__hci__cp__le__conn__param__req__reply.md#a10547c7d4836980947d17bbde0d75a51)

uint16\_t interval\_min

**Definition** hci\_types.h:1294

[bt\_hci\_cp\_le\_conn\_param\_req\_reply::min\_ce\_len](structbt__hci__cp__le__conn__param__req__reply.md#a512d605d5c4aacf81b78794fcf260abf)

uint16\_t min\_ce\_len

**Definition** hci\_types.h:1298

[bt\_hci\_cp\_le\_conn\_param\_req\_reply::latency](structbt__hci__cp__le__conn__param__req__reply.md#a8c76816cc230387c249ab8e05c402964)

uint16\_t latency

**Definition** hci\_types.h:1296

[bt\_hci\_cp\_le\_conn\_param\_req\_reply::max\_ce\_len](structbt__hci__cp__le__conn__param__req__reply.md#a932e6a3a45ec0409656325f7246d5d7e)

uint16\_t max\_ce\_len

**Definition** hci\_types.h:1299

[bt\_hci\_cp\_le\_conn\_param\_req\_reply::handle](structbt__hci__cp__le__conn__param__req__reply.md#aa3b938afe13d4e05806fb6cdfab5cb14)

uint16\_t handle

**Definition** hci\_types.h:1293

[bt\_hci\_cp\_le\_conn\_param\_req\_reply::interval\_max](structbt__hci__cp__le__conn__param__req__reply.md#aed58f9aa722a284ae39df842394c06cf)

uint16\_t interval\_max

**Definition** hci\_types.h:1295

[bt\_hci\_cp\_le\_conn\_param\_req\_reply::timeout](structbt__hci__cp__le__conn__param__req__reply.md#af25a3f226ceccbe19e7f1482ed5f141e)

uint16\_t timeout

**Definition** hci\_types.h:1297

[bt\_hci\_cp\_le\_create\_big\_test](structbt__hci__cp__le__create__big__test.md)

**Definition** hci\_types.h:2251

[bt\_hci\_cp\_le\_create\_big\_test::max\_pdu](structbt__hci__cp__le__create__big__test.md#a2652e0f340f13635a5da6335ec43e801)

uint16\_t max\_pdu

**Definition** hci\_types.h:2259

[bt\_hci\_cp\_le\_create\_big\_test::pto](structbt__hci__cp__le__create__big__test.md#a2f2eaa258463dd51a9f6042e75ecfec6)

uint8\_t pto

**Definition** hci\_types.h:2265

[bt\_hci\_cp\_le\_create\_big\_test::sdu\_interval](structbt__hci__cp__le__create__big__test.md#a331b1a8ef66804cf20d6681e1bc5aefb)

uint8\_t sdu\_interval[3]

**Definition** hci\_types.h:2255

[bt\_hci\_cp\_le\_create\_big\_test::bcode](structbt__hci__cp__le__create__big__test.md#a333319a03d2087067247c4f5e595b4e5)

uint8\_t bcode[16]

**Definition** hci\_types.h:2267

[bt\_hci\_cp\_le\_create\_big\_test::nse](structbt__hci__cp__le__create__big__test.md#a402c19da1ecf273bc942ecc560730567)

uint8\_t nse

**Definition** hci\_types.h:2257

[bt\_hci\_cp\_le\_create\_big\_test::packing](structbt__hci__cp__le__create__big__test.md#a49822f8e1617e30aab9b0d7d790697a3)

uint8\_t packing

**Definition** hci\_types.h:2261

[bt\_hci\_cp\_le\_create\_big\_test::encryption](structbt__hci__cp__le__create__big__test.md#a50c4308abda01581b436b7867304e982)

uint8\_t encryption

**Definition** hci\_types.h:2266

[bt\_hci\_cp\_le\_create\_big\_test::iso\_interval](structbt__hci__cp__le__create__big__test.md#a6475ae77af80e89bb65596bc6f907a58)

uint16\_t iso\_interval

**Definition** hci\_types.h:2256

[bt\_hci\_cp\_le\_create\_big\_test::irc](structbt__hci__cp__le__create__big__test.md#a66ce7ba0498053a588de9097cbbc0891)

uint8\_t irc

**Definition** hci\_types.h:2264

[bt\_hci\_cp\_le\_create\_big\_test::num\_bis](structbt__hci__cp__le__create__big__test.md#a6ce270f0afd185c44fa5a2c67a7783fb)

uint8\_t num\_bis

**Definition** hci\_types.h:2254

[bt\_hci\_cp\_le\_create\_big\_test::phy](structbt__hci__cp__le__create__big__test.md#a731ca2f90c17a4f3f868660e51649ce6)

uint8\_t phy

**Definition** hci\_types.h:2260

[bt\_hci\_cp\_le\_create\_big\_test::bn](structbt__hci__cp__le__create__big__test.md#a734174187486ac760b8bf0e566166842)

uint8\_t bn

**Definition** hci\_types.h:2263

[bt\_hci\_cp\_le\_create\_big\_test::max\_sdu](structbt__hci__cp__le__create__big__test.md#a7ebbc81306109e035f89154738900395)

uint16\_t max\_sdu

**Definition** hci\_types.h:2258

[bt\_hci\_cp\_le\_create\_big\_test::big\_handle](structbt__hci__cp__le__create__big__test.md#ac202f5cee0c1d0456b200606860fd5ab)

uint8\_t big\_handle

**Definition** hci\_types.h:2252

[bt\_hci\_cp\_le\_create\_big\_test::framing](structbt__hci__cp__le__create__big__test.md#acc5b2c30db0c7642d12019f8241dab26)

uint8\_t framing

**Definition** hci\_types.h:2262

[bt\_hci\_cp\_le\_create\_big\_test::adv\_handle](structbt__hci__cp__le__create__big__test.md#aece09ae6264e0cc1a5548f1603a3f61a)

uint8\_t adv\_handle

**Definition** hci\_types.h:2253

[bt\_hci\_cp\_le\_create\_big](structbt__hci__cp__le__create__big.md)

**Definition** hci\_types.h:2235

[bt\_hci\_cp\_le\_create\_big::max\_sdu](structbt__hci__cp__le__create__big.md#a06fd74e9a5f172060835524da5851c71)

uint16\_t max\_sdu

**Definition** hci\_types.h:2240

[bt\_hci\_cp\_le\_create\_big::bcode](structbt__hci__cp__le__create__big.md#a0b4b2d77cd0f579aab190336b14597c5)

uint8\_t bcode[16]

**Definition** hci\_types.h:2247

[bt\_hci\_cp\_le\_create\_big::max\_latency](structbt__hci__cp__le__create__big.md#a15018e5ebc124bbe90644b38fe3e7e76)

uint16\_t max\_latency

**Definition** hci\_types.h:2241

[bt\_hci\_cp\_le\_create\_big::rtn](structbt__hci__cp__le__create__big.md#a1cb0dd106bf4a1a0c473333d089c95e7)

uint8\_t rtn

**Definition** hci\_types.h:2242

[bt\_hci\_cp\_le\_create\_big::sdu\_interval](structbt__hci__cp__le__create__big.md#a2960a9891b827529c9fa1b68a747e2d5)

uint8\_t sdu\_interval[3]

**Definition** hci\_types.h:2239

[bt\_hci\_cp\_le\_create\_big::framing](structbt__hci__cp__le__create__big.md#a330916d60c05ec2ef7a71933b62c203a)

uint8\_t framing

**Definition** hci\_types.h:2245

[bt\_hci\_cp\_le\_create\_big::encryption](structbt__hci__cp__le__create__big.md#a490bd68d137f8cf60ea2ccd5ea4495e9)

uint8\_t encryption

**Definition** hci\_types.h:2246

[bt\_hci\_cp\_le\_create\_big::phy](structbt__hci__cp__le__create__big.md#a56cb773a03e4927c3b6bf4d2a6ed6ed9)

uint8\_t phy

**Definition** hci\_types.h:2243

[bt\_hci\_cp\_le\_create\_big::adv\_handle](structbt__hci__cp__le__create__big.md#aa686eec31ca4c831262dd34d41f9a1fb)

uint8\_t adv\_handle

**Definition** hci\_types.h:2237

[bt\_hci\_cp\_le\_create\_big::packing](structbt__hci__cp__le__create__big.md#ac027390db21320fb9d1002161c4c2f67)

uint8\_t packing

**Definition** hci\_types.h:2244

[bt\_hci\_cp\_le\_create\_big::num\_bis](structbt__hci__cp__le__create__big.md#ad8491c970417e63c6a98c12278a89c86)

uint8\_t num\_bis

**Definition** hci\_types.h:2238

[bt\_hci\_cp\_le\_create\_big::big\_handle](structbt__hci__cp__le__create__big.md#af5412e4a69c05a09b2e818322636a98a)

uint8\_t big\_handle

**Definition** hci\_types.h:2236

[bt\_hci\_cp\_le\_create\_cis](structbt__hci__cp__le__create__cis.md)

**Definition** hci\_types.h:2203

[bt\_hci\_cp\_le\_create\_cis::cis](structbt__hci__cp__le__create__cis.md#a5a323d09df7813fc9b834cc1d205d101)

struct bt\_hci\_cis cis[0]

**Definition** hci\_types.h:2205

[bt\_hci\_cp\_le\_create\_cis::num\_cis](structbt__hci__cp__le__create__cis.md#acd348a7d68947af8e7119b2e1a864481)

uint8\_t num\_cis

**Definition** hci\_types.h:2204

[bt\_hci\_cp\_le\_create\_conn](structbt__hci__cp__le__create__conn.md)

**Definition** hci\_types.h:1150

[bt\_hci\_cp\_le\_create\_conn::scan\_interval](structbt__hci__cp__le__create__conn.md#a1a830a0f6cd961d534c338031b2b691b)

uint16\_t scan\_interval

**Definition** hci\_types.h:1151

[bt\_hci\_cp\_le\_create\_conn::filter\_policy](structbt__hci__cp__le__create__conn.md#a2ca5063f5082a0f330676e56253a21c7)

uint8\_t filter\_policy

**Definition** hci\_types.h:1153

[bt\_hci\_cp\_le\_create\_conn::min\_ce\_len](structbt__hci__cp__le__create__conn.md#a476501ccd209f3a52082decf906ca8f0)

uint16\_t min\_ce\_len

**Definition** hci\_types.h:1160

[bt\_hci\_cp\_le\_create\_conn::conn\_latency](structbt__hci__cp__le__create__conn.md#a5a9d5c1d44adac876680a517b1fad63f)

uint16\_t conn\_latency

**Definition** hci\_types.h:1158

[bt\_hci\_cp\_le\_create\_conn::max\_ce\_len](structbt__hci__cp__le__create__conn.md#a5b329aa8b48e03998e969b2436d35ab5)

uint16\_t max\_ce\_len

**Definition** hci\_types.h:1161

[bt\_hci\_cp\_le\_create\_conn::own\_addr\_type](structbt__hci__cp__le__create__conn.md#a63c7f9e89528105e484a60e41eeb8a30)

uint8\_t own\_addr\_type

**Definition** hci\_types.h:1155

[bt\_hci\_cp\_le\_create\_conn::conn\_interval\_min](structbt__hci__cp__le__create__conn.md#a988cf154b0df1ff9af8d34ce73a920dd)

uint16\_t conn\_interval\_min

**Definition** hci\_types.h:1156

[bt\_hci\_cp\_le\_create\_conn::conn\_interval\_max](structbt__hci__cp__le__create__conn.md#aa009d54866d9c675c2785412bdbd182f)

uint16\_t conn\_interval\_max

**Definition** hci\_types.h:1157

[bt\_hci\_cp\_le\_create\_conn::peer\_addr](structbt__hci__cp__le__create__conn.md#aa51da7602eb2b44528964c8b706bb043)

bt\_addr\_le\_t peer\_addr

**Definition** hci\_types.h:1154

[bt\_hci\_cp\_le\_create\_conn::scan\_window](structbt__hci__cp__le__create__conn.md#abf61e67f5e20adc44b5b9314ed43bccc)

uint16\_t scan\_window

**Definition** hci\_types.h:1152

[bt\_hci\_cp\_le\_create\_conn::supervision\_timeout](structbt__hci__cp__le__create__conn.md#ae8e0ad70a3b23ac035c237db0d57adc4)

uint16\_t supervision\_timeout

**Definition** hci\_types.h:1159

[bt\_hci\_cp\_le\_cs\_create\_config](structbt__hci__cp__le__cs__create__config.md)

**Definition** hci\_types.h:2713

[bt\_hci\_cp\_le\_cs\_create\_config::ch3c\_jump](structbt__hci__cp__le__cs__create__config.md#a0223c41abc034d515421fad8c3123387)

uint8\_t ch3c\_jump

**Definition** hci\_types.h:2730

[bt\_hci\_cp\_le\_cs\_create\_config::channel\_selection\_type](structbt__hci__cp__le__cs__create__config.md#a2c8be699bfd8eaaababd6d0de0b13e18)

uint8\_t channel\_selection\_type

**Definition** hci\_types.h:2728

[bt\_hci\_cp\_le\_cs\_create\_config::sub\_mode\_type](structbt__hci__cp__le__cs__create__config.md#a34fa54e8bbd641bb0901b0b057134ffb)

uint8\_t sub\_mode\_type

**Definition** hci\_types.h:2718

[bt\_hci\_cp\_le\_cs\_create\_config::handle](structbt__hci__cp__le__cs__create__config.md#a3742081b071b992176b725448cc6ab29)

uint16\_t handle

**Definition** hci\_types.h:2714

[bt\_hci\_cp\_le\_cs\_create\_config::reserved](structbt__hci__cp__le__cs__create__config.md#a40b42ed708733aa7d55879ef7228699e)

uint8\_t reserved

**Definition** hci\_types.h:2731

[bt\_hci\_cp\_le\_cs\_create\_config::role](structbt__hci__cp__le__cs__create__config.md#a5a17d6c72daaefcb55fdfa24194cc886)

uint8\_t role

**Definition** hci\_types.h:2723

[bt\_hci\_cp\_le\_cs\_create\_config::rtt\_type](structbt__hci__cp__le__cs__create__config.md#a709938176023c5482c91af8995001782)

uint8\_t rtt\_type

**Definition** hci\_types.h:2724

[bt\_hci\_cp\_le\_cs\_create\_config::main\_mode\_type](structbt__hci__cp__le__cs__create__config.md#a74c5fdfbc97b112c35ee318aa2b9b463)

uint8\_t main\_mode\_type

**Definition** hci\_types.h:2717

[bt\_hci\_cp\_le\_cs\_create\_config::channel\_map\_repetition](structbt__hci__cp__le__cs__create__config.md#a8182f4becdef488b84f12fe7e4274193)

uint8\_t channel\_map\_repetition

**Definition** hci\_types.h:2727

[bt\_hci\_cp\_le\_cs\_create\_config::mode\_0\_steps](structbt__hci__cp__le__cs__create__config.md#a909e409d55ac539a119e932899a97204)

uint8\_t mode\_0\_steps

**Definition** hci\_types.h:2722

[bt\_hci\_cp\_le\_cs\_create\_config::create\_context](structbt__hci__cp__le__cs__create__config.md#a9dc7a6b577c33583b7ca7548e2b555ac)

uint8\_t create\_context

**Definition** hci\_types.h:2716

[bt\_hci\_cp\_le\_cs\_create\_config::max\_main\_mode\_steps](structbt__hci__cp__le__cs__create__config.md#aa13e091f99114bb5217489757c1522bd)

uint8\_t max\_main\_mode\_steps

**Definition** hci\_types.h:2720

[bt\_hci\_cp\_le\_cs\_create\_config::channel\_map](structbt__hci__cp__le__cs__create__config.md#abab4907ec883430044bb9f9d6cf9f25d)

uint8\_t channel\_map[10]

**Definition** hci\_types.h:2726

[bt\_hci\_cp\_le\_cs\_create\_config::cs\_sync\_phy](structbt__hci__cp__le__cs__create__config.md#ac6c9c568918c9ef9aa4f2038a4922020)

uint8\_t cs\_sync\_phy

**Definition** hci\_types.h:2725

[bt\_hci\_cp\_le\_cs\_create\_config::main\_mode\_repetition](structbt__hci__cp__le__cs__create__config.md#acd11430a6c94b0f0c34e2788a2326a40)

uint8\_t main\_mode\_repetition

**Definition** hci\_types.h:2721

[bt\_hci\_cp\_le\_cs\_create\_config::ch3c\_shape](structbt__hci__cp__le__cs__create__config.md#addaa3592a97bda96a4aba17e809e4018)

uint8\_t ch3c\_shape

**Definition** hci\_types.h:2729

[bt\_hci\_cp\_le\_cs\_create\_config::config\_id](structbt__hci__cp__le__cs__create__config.md#ae833b5f02f878f54dca1a25753eca1f3)

uint8\_t config\_id

**Definition** hci\_types.h:2715

[bt\_hci\_cp\_le\_cs\_create\_config::min\_main\_mode\_steps](structbt__hci__cp__le__cs__create__config.md#aeb26115c8b500829ef6bc238aa3a495f)

uint8\_t min\_main\_mode\_steps

**Definition** hci\_types.h:2719

[bt\_hci\_cp\_le\_cs\_remove\_config](structbt__hci__cp__le__cs__remove__config.md)

**Definition** hci\_types.h:2736

[bt\_hci\_cp\_le\_cs\_remove\_config::handle](structbt__hci__cp__le__cs__remove__config.md#a4591af2e952f514b185db12c5f1158d5)

uint16\_t handle

**Definition** hci\_types.h:2737

[bt\_hci\_cp\_le\_cs\_remove\_config::config\_id](structbt__hci__cp__le__cs__remove__config.md#a9be71a1360f1ed14e6a7e205f5704e39)

uint8\_t config\_id

**Definition** hci\_types.h:2738

[bt\_hci\_cp\_le\_cs\_set\_default\_settings](structbt__hci__cp__le__cs__set__default__settings.md)

**Definition** hci\_types.h:2516

[bt\_hci\_cp\_le\_cs\_set\_default\_settings::role\_enable](structbt__hci__cp__le__cs__set__default__settings.md#a04aea510e26136f874ccfbabbbd080bb)

uint8\_t role\_enable

**Definition** hci\_types.h:2518

[bt\_hci\_cp\_le\_cs\_set\_default\_settings::handle](structbt__hci__cp__le__cs__set__default__settings.md#a096c3238ccc6624bae89d5a45dd95600)

uint16\_t handle

**Definition** hci\_types.h:2517

[bt\_hci\_cp\_le\_cs\_set\_default\_settings::max\_tx\_power](structbt__hci__cp__le__cs__set__default__settings.md#a333341ec01554ab90fc5e340dbfb5130)

int8\_t max\_tx\_power

**Definition** hci\_types.h:2520

[bt\_hci\_cp\_le\_cs\_set\_default\_settings::cs\_sync\_antenna\_selection](structbt__hci__cp__le__cs__set__default__settings.md#aa001c88ab42250c2cfd604af11e0ae27)

uint8\_t cs\_sync\_antenna\_selection

**Definition** hci\_types.h:2519

[bt\_hci\_cp\_le\_default\_past\_param](structbt__hci__cp__le__default__past__param.md)

**Definition** hci\_types.h:2083

[bt\_hci\_cp\_le\_default\_past\_param::timeout](structbt__hci__cp__le__default__past__param.md#a159f5245f86b27198264bdcf394d719f)

uint16\_t timeout

**Definition** hci\_types.h:2086

[bt\_hci\_cp\_le\_default\_past\_param::skip](structbt__hci__cp__le__default__past__param.md#a214cb0597d0065bc2c056fe9c51a2220)

uint16\_t skip

**Definition** hci\_types.h:2085

[bt\_hci\_cp\_le\_default\_past\_param::mode](structbt__hci__cp__le__default__past__param.md#a2ef92304264ad0bf1560accf306bb6d9)

uint8\_t mode

**Definition** hci\_types.h:2084

[bt\_hci\_cp\_le\_default\_past\_param::cte\_type](structbt__hci__cp__le__default__past__param.md#af18f679f5833c1d782b4e474af5d819c)

uint8\_t cte\_type

**Definition** hci\_types.h:2087

[bt\_hci\_cp\_le\_encrypt](structbt__hci__cp__le__encrypt.md)

**Definition** hci\_types.h:1216

[bt\_hci\_cp\_le\_encrypt::key](structbt__hci__cp__le__encrypt.md#ab64f1bab8ad3a98217db96e6765a7d24)

uint8\_t key[16]

**Definition** hci\_types.h:1217

[bt\_hci\_cp\_le\_encrypt::plaintext](structbt__hci__cp__le__encrypt.md#ad520b84e6e2a4e62f7fefba248c4cf10)

uint8\_t plaintext[16]

**Definition** hci\_types.h:1218

[bt\_hci\_cp\_le\_enh\_rx\_test](structbt__hci__cp__le__enh__rx__test.md)

**Definition** hci\_types.h:1480

[bt\_hci\_cp\_le\_enh\_rx\_test::rx\_ch](structbt__hci__cp__le__enh__rx__test.md#a3aa5b3947a4a0c87342695469bf056ec)

uint8\_t rx\_ch

**Definition** hci\_types.h:1481

[bt\_hci\_cp\_le\_enh\_rx\_test::mod\_index](structbt__hci__cp__le__enh__rx__test.md#a9151393e9f05a2ded484a1248a6edb88)

uint8\_t mod\_index

**Definition** hci\_types.h:1483

[bt\_hci\_cp\_le\_enh\_rx\_test::phy](structbt__hci__cp__le__enh__rx__test.md#aa2bf385221680b25ce184b4ea5d63cd4)

uint8\_t phy

**Definition** hci\_types.h:1482

[bt\_hci\_cp\_le\_enh\_tx\_test](structbt__hci__cp__le__enh__tx__test.md)

**Definition** hci\_types.h:1492

[bt\_hci\_cp\_le\_enh\_tx\_test::tx\_ch](structbt__hci__cp__le__enh__tx__test.md#a0b7883b36d511c6da1bac543f1aae446)

uint8\_t tx\_ch

**Definition** hci\_types.h:1493

[bt\_hci\_cp\_le\_enh\_tx\_test::phy](structbt__hci__cp__le__enh__tx__test.md#a718442db29c5ac455c3e2aac9844cdd0)

uint8\_t phy

**Definition** hci\_types.h:1496

[bt\_hci\_cp\_le\_enh\_tx\_test::pkt\_payload](structbt__hci__cp__le__enh__tx__test.md#a9ccb91be1554172d6c724e438508bfe5)

uint8\_t pkt\_payload

**Definition** hci\_types.h:1495

[bt\_hci\_cp\_le\_enh\_tx\_test::test\_data\_len](structbt__hci__cp__le__enh__tx__test.md#af1e27be0ad23887c0e71024739b00f8d)

uint8\_t test\_data\_len

**Definition** hci\_types.h:1494

[bt\_hci\_cp\_le\_ext\_create\_conn\_v2](structbt__hci__cp__le__ext__create__conn__v2.md)

**Definition** hci\_types.h:1717

[bt\_hci\_cp\_le\_ext\_create\_conn\_v2::own\_addr\_type](structbt__hci__cp__le__ext__create__conn__v2.md#a05fd0089a0fd43f98042835231407a60)

uint8\_t own\_addr\_type

**Definition** hci\_types.h:1721

[bt\_hci\_cp\_le\_ext\_create\_conn\_v2::peer\_addr](structbt__hci__cp__le__ext__create__conn__v2.md#a25466a04d224bdf495266b0064c424dd)

bt\_addr\_le\_t peer\_addr

**Definition** hci\_types.h:1722

[bt\_hci\_cp\_le\_ext\_create\_conn\_v2::subevent](structbt__hci__cp__le__ext__create__conn__v2.md#a536da199958b3b54469f5b4b029e1bac)

uint8\_t subevent

**Definition** hci\_types.h:1719

[bt\_hci\_cp\_le\_ext\_create\_conn\_v2::filter\_policy](structbt__hci__cp__le__ext__create__conn__v2.md#a66632dbac1605cff69e8da566e800347)

uint8\_t filter\_policy

**Definition** hci\_types.h:1720

[bt\_hci\_cp\_le\_ext\_create\_conn\_v2::p](structbt__hci__cp__le__ext__create__conn__v2.md#a8d606c5aa480f54c8da9f42a35ad513e)

struct bt\_hci\_ext\_conn\_phy p[0]

**Definition** hci\_types.h:1724

[bt\_hci\_cp\_le\_ext\_create\_conn\_v2::adv\_handle](structbt__hci__cp__le__ext__create__conn__v2.md#addf1f80c4d3625e0c6d6e716f6e2e207)

uint8\_t adv\_handle

**Definition** hci\_types.h:1718

[bt\_hci\_cp\_le\_ext\_create\_conn\_v2::phys](structbt__hci__cp__le__ext__create__conn__v2.md#ae2d3e3079a2848907224bb7ff0efc64b)

uint8\_t phys

**Definition** hci\_types.h:1723

[bt\_hci\_cp\_le\_ext\_create\_conn](structbt__hci__cp__le__ext__create__conn.md)

**Definition** hci\_types.h:1709

[bt\_hci\_cp\_le\_ext\_create\_conn::filter\_policy](structbt__hci__cp__le__ext__create__conn.md#a0561b446effa3f735a405c0b307466bf)

uint8\_t filter\_policy

**Definition** hci\_types.h:1710

[bt\_hci\_cp\_le\_ext\_create\_conn::own\_addr\_type](structbt__hci__cp__le__ext__create__conn.md#a12a99044f54e3d5dae30a64392444cbf)

uint8\_t own\_addr\_type

**Definition** hci\_types.h:1711

[bt\_hci\_cp\_le\_ext\_create\_conn::peer\_addr](structbt__hci__cp__le__ext__create__conn.md#a79bc55d9f5b1d719de4fb404db9008f3)

bt\_addr\_le\_t peer\_addr

**Definition** hci\_types.h:1712

[bt\_hci\_cp\_le\_ext\_create\_conn::p](structbt__hci__cp__le__ext__create__conn.md#acdb436d6bf2864745ec579622ae0d532)

struct bt\_hci\_ext\_conn\_phy p[0]

**Definition** hci\_types.h:1714

[bt\_hci\_cp\_le\_ext\_create\_conn::phys](structbt__hci__cp__le__ext__create__conn.md#ae859ff0da5e9cdc872943fd74774ef7e)

uint8\_t phys

**Definition** hci\_types.h:1713

[bt\_hci\_cp\_le\_generate\_dhkey\_v2](structbt__hci__cp__le__generate__dhkey__v2.md)

**Definition** hci\_types.h:1353

[bt\_hci\_cp\_le\_generate\_dhkey\_v2::key\_type](structbt__hci__cp__le__generate__dhkey__v2.md#a3d47ad6d9df4d4023d2586c915ee8f2c)

uint8\_t key\_type

**Definition** hci\_types.h:1355

[bt\_hci\_cp\_le\_generate\_dhkey\_v2::key](structbt__hci__cp__le__generate__dhkey__v2.md#acc3007adf301674b9e847297007c3cd1)

uint8\_t key[64]

**Definition** hci\_types.h:1354

[bt\_hci\_cp\_le\_generate\_dhkey](structbt__hci__cp__le__generate__dhkey.md)

**Definition** hci\_types.h:1343

[bt\_hci\_cp\_le\_generate\_dhkey::key](structbt__hci__cp__le__generate__dhkey.md#a0f67195504d877a1d11b7dfb77d09fcc)

uint8\_t key[64]

**Definition** hci\_types.h:1344

[bt\_hci\_cp\_le\_iso\_receive\_test](structbt__hci__cp__le__iso__receive__test.md)

**Definition** hci\_types.h:2346

[bt\_hci\_cp\_le\_iso\_receive\_test::payload\_type](structbt__hci__cp__le__iso__receive__test.md#a9ce7e13fc1c1a7c87c01e1ecb24c5324)

uint8\_t payload\_type

**Definition** hci\_types.h:2348

[bt\_hci\_cp\_le\_iso\_receive\_test::handle](structbt__hci__cp__le__iso__receive__test.md#ac1272441f5c7b79e1ef5f644f099d19e)

uint16\_t handle

**Definition** hci\_types.h:2347

[bt\_hci\_cp\_le\_iso\_test\_end](structbt__hci__cp__le__iso__test__end.md)

**Definition** hci\_types.h:2370

[bt\_hci\_cp\_le\_iso\_test\_end::handle](structbt__hci__cp__le__iso__test__end.md#ab792ec021319024828bd7609e0fe7e96)

uint16\_t handle

**Definition** hci\_types.h:2371

[bt\_hci\_cp\_le\_iso\_transmit\_test](structbt__hci__cp__le__iso__transmit__test.md)

**Definition** hci\_types.h:2335

[bt\_hci\_cp\_le\_iso\_transmit\_test::payload\_type](structbt__hci__cp__le__iso__transmit__test.md#a0653c77af723cc43a6b911816a8db437)

uint8\_t payload\_type

**Definition** hci\_types.h:2337

[bt\_hci\_cp\_le\_iso\_transmit\_test::handle](structbt__hci__cp__le__iso__transmit__test.md#adffb0d57afc090692ab36ebeaad21bbd)

uint16\_t handle

**Definition** hci\_types.h:2336

[bt\_hci\_cp\_le\_ltk\_req\_neg\_reply](structbt__hci__cp__le__ltk__req__neg__reply.md)

**Definition** hci\_types.h:1250

[bt\_hci\_cp\_le\_ltk\_req\_neg\_reply::handle](structbt__hci__cp__le__ltk__req__neg__reply.md#add8cc3b13432e233ceb5c2c11e0107c0)

uint16\_t handle

**Definition** hci\_types.h:1251

[bt\_hci\_cp\_le\_ltk\_req\_reply](structbt__hci__cp__le__ltk__req__reply.md)

**Definition** hci\_types.h:1240

[bt\_hci\_cp\_le\_ltk\_req\_reply::ltk](structbt__hci__cp__le__ltk__req__reply.md#a2d16b44af344237a890341943c4a6582)

uint8\_t ltk[16]

**Definition** hci\_types.h:1242

[bt\_hci\_cp\_le\_ltk\_req\_reply::handle](structbt__hci__cp__le__ltk__req__reply.md#a46d87451acc1f1ce2ff35dd0dd238db3)

uint16\_t handle

**Definition** hci\_types.h:1241

[bt\_hci\_cp\_le\_past\_param](structbt__hci__cp__le__past__param.md)

**Definition** hci\_types.h:2069

[bt\_hci\_cp\_le\_past\_param::cte\_type](structbt__hci__cp__le__past__param.md#a47c571ff27a59e0a7cbcb460303ee194)

uint8\_t cte\_type

**Definition** hci\_types.h:2074

[bt\_hci\_cp\_le\_past\_param::skip](structbt__hci__cp__le__past__param.md#a622499d51e917f7828629de2291812e5)

uint16\_t skip

**Definition** hci\_types.h:2072

[bt\_hci\_cp\_le\_past\_param::conn\_handle](structbt__hci__cp__le__past__param.md#a9c99cdd5ae5de58960677781c2287c4d)

uint16\_t conn\_handle

**Definition** hci\_types.h:2070

[bt\_hci\_cp\_le\_past\_param::mode](structbt__hci__cp__le__past__param.md#aa36345a550dfabeef48b430d1a1b0030)

uint8\_t mode

**Definition** hci\_types.h:2071

[bt\_hci\_cp\_le\_past\_param::timeout](structbt__hci__cp__le__past__param.md#aec9aa4ffe41c6b6f5cfcbc59eb57efca)

uint16\_t timeout

**Definition** hci\_types.h:2073

[bt\_hci\_cp\_le\_per\_adv\_create\_sync](structbt__hci__cp__le__per__adv__create__sync.md)

**Definition** hci\_types.h:1793

[bt\_hci\_cp\_le\_per\_adv\_create\_sync::addr](structbt__hci__cp__le__per__adv__create__sync.md#a3a0a0bc1bd5014f2ede0c4ef6cc30d24)

bt\_addr\_le\_t addr

**Definition** hci\_types.h:1796

[bt\_hci\_cp\_le\_per\_adv\_create\_sync::sync\_timeout](structbt__hci__cp__le__per__adv__create__sync.md#a46ea01403f68d42a315ff629374b2a95)

uint16\_t sync\_timeout

**Definition** hci\_types.h:1798

[bt\_hci\_cp\_le\_per\_adv\_create\_sync::skip](structbt__hci__cp__le__per__adv__create__sync.md#a554552684fa2a8d0022f9e31ade9c222)

uint16\_t skip

**Definition** hci\_types.h:1797

[bt\_hci\_cp\_le\_per\_adv\_create\_sync::cte\_type](structbt__hci__cp__le__per__adv__create__sync.md#a905b2a9166dd668df5929f0866769576)

uint8\_t cte\_type

**Definition** hci\_types.h:1799

[bt\_hci\_cp\_le\_per\_adv\_create\_sync::sid](structbt__hci__cp__le__per__adv__create__sync.md#ab5c4debe1babb98c60c1f1bfdf55359a)

uint8\_t sid

**Definition** hci\_types.h:1795

[bt\_hci\_cp\_le\_per\_adv\_create\_sync::options](structbt__hci__cp__le__per__adv__create__sync.md#aff300f352ec5f0fece90f88db811ef75)

uint8\_t options

**Definition** hci\_types.h:1794

[bt\_hci\_cp\_le\_per\_adv\_set\_info\_transfer](structbt__hci__cp__le__per__adv__set__info__transfer.md)

**Definition** hci\_types.h:2046

[bt\_hci\_cp\_le\_per\_adv\_set\_info\_transfer::conn\_handle](structbt__hci__cp__le__per__adv__set__info__transfer.md#a3b2f0c510ef9b385cb42bf9a194fa574)

uint16\_t conn\_handle

**Definition** hci\_types.h:2047

[bt\_hci\_cp\_le\_per\_adv\_set\_info\_transfer::service\_data](structbt__hci__cp__le__per__adv__set__info__transfer.md#a5f14c3265bffdf3e30a554a3686e9e0c)

uint16\_t service\_data

**Definition** hci\_types.h:2048

[bt\_hci\_cp\_le\_per\_adv\_set\_info\_transfer::adv\_handle](structbt__hci__cp__le__per__adv__set__info__transfer.md#a75b2c0fa1d50ef9d3761ac25f487750b)

uint8\_t adv\_handle

**Definition** hci\_types.h:2049

[bt\_hci\_cp\_le\_per\_adv\_sync\_transfer](structbt__hci__cp__le__per__adv__sync__transfer.md)

**Definition** hci\_types.h:2034

[bt\_hci\_cp\_le\_per\_adv\_sync\_transfer::service\_data](structbt__hci__cp__le__per__adv__sync__transfer.md#a1327de0f9b2ebd1eaa97b51850087460)

uint16\_t service\_data

**Definition** hci\_types.h:2036

[bt\_hci\_cp\_le\_per\_adv\_sync\_transfer::sync\_handle](structbt__hci__cp__le__per__adv__sync__transfer.md#a38537b7f01a93f7a3e8cfcb92098a172)

uint16\_t sync\_handle

**Definition** hci\_types.h:2037

[bt\_hci\_cp\_le\_per\_adv\_sync\_transfer::conn\_handle](structbt__hci__cp__le__per__adv__sync__transfer.md#a991f77d6f2f0c301fe3322050b2d359f)

uint16\_t conn\_handle

**Definition** hci\_types.h:2035

[bt\_hci\_cp\_le\_per\_adv\_terminate\_sync](structbt__hci__cp__le__per__adv__terminate__sync.md)

**Definition** hci\_types.h:1805

[bt\_hci\_cp\_le\_per\_adv\_terminate\_sync::handle](structbt__hci__cp__le__per__adv__terminate__sync.md#a607fce7fd5c88e12f82e3d9731bd7f1a)

uint16\_t handle

**Definition** hci\_types.h:1806

[bt\_hci\_cp\_le\_procedure\_enable](structbt__hci__cp__le__procedure__enable.md)

**Definition** hci\_types.h:2567

[bt\_hci\_cp\_le\_procedure\_enable::enable](structbt__hci__cp__le__procedure__enable.md#a3a203b453bd913db8bec91be9310003a)

uint8\_t enable

**Definition** hci\_types.h:2570

[bt\_hci\_cp\_le\_procedure\_enable::config\_id](structbt__hci__cp__le__procedure__enable.md#ae1dc5c808bed301ddee6e9dd624c00a5)

uint8\_t config\_id

**Definition** hci\_types.h:2569

[bt\_hci\_cp\_le\_procedure\_enable::handle](structbt__hci__cp__le__procedure__enable.md#af94d81f71c2fe587c848e34a430825bf)

uint16\_t handle

**Definition** hci\_types.h:2568

[bt\_hci\_cp\_le\_read\_chan\_map](structbt__hci__cp__le__read__chan__map.md)

**Definition** hci\_types.h:1201

[bt\_hci\_cp\_le\_read\_chan\_map::handle](structbt__hci__cp__le__read__chan__map.md#abea9aec016a0433b3e4837d53d6b5d2b)

uint16\_t handle

**Definition** hci\_types.h:1202

[bt\_hci\_cp\_le\_read\_iso\_link\_quality](structbt__hci__cp__le__read__iso__link__quality.md)

**Definition** hci\_types.h:2393

[bt\_hci\_cp\_le\_read\_iso\_link\_quality::handle](structbt__hci__cp__le__read__iso__link__quality.md#a346fb3cf08203725d5943e42f03cb40d)

uint16\_t handle

**Definition** hci\_types.h:2394

[bt\_hci\_cp\_le\_read\_iso\_tx\_sync](structbt__hci__cp__le__read__iso__tx__sync.md)

**Definition** hci\_types.h:2104

[bt\_hci\_cp\_le\_read\_iso\_tx\_sync::handle](structbt__hci__cp__le__read__iso__tx__sync.md#a8edc469f73540d4300b1716c96e17c9f)

uint16\_t handle

**Definition** hci\_types.h:2105

[bt\_hci\_cp\_le\_read\_local\_rpa](structbt__hci__cp__le__read__local__rpa.md)

**Definition** hci\_types.h:1389

[bt\_hci\_cp\_le\_read\_local\_rpa::peer\_id\_addr](structbt__hci__cp__le__read__local__rpa.md#aa96cd60066003e4a7a1f482fb81557f8)

bt\_addr\_le\_t peer\_id\_addr

**Definition** hci\_types.h:1390

[bt\_hci\_cp\_le\_read\_peer\_rpa](structbt__hci__cp__le__read__peer__rpa.md)

**Definition** hci\_types.h:1380

[bt\_hci\_cp\_le\_read\_peer\_rpa::peer\_id\_addr](structbt__hci__cp__le__read__peer__rpa.md#ab0c70a1dbe5152b1fc926b90ec3387b3)

bt\_addr\_le\_t peer\_id\_addr

**Definition** hci\_types.h:1381

[bt\_hci\_cp\_le\_read\_phy](structbt__hci__cp__le__read__phy.md)

**Definition** hci\_types.h:1435

[bt\_hci\_cp\_le\_read\_phy::handle](structbt__hci__cp__le__read__phy.md#a7e0a4fa47b613c86364e6e94c2d0bef1)

uint16\_t handle

**Definition** hci\_types.h:1436

[bt\_hci\_cp\_le\_read\_remote\_fae\_table](structbt__hci__cp__le__read__remote__fae__table.md)

**Definition** hci\_types.h:2525

[bt\_hci\_cp\_le\_read\_remote\_fae\_table::handle](structbt__hci__cp__le__read__remote__fae__table.md#a10bdfc4808586f7cccf025c63a6e28a5)

uint16\_t handle

**Definition** hci\_types.h:2526

[bt\_hci\_cp\_le\_read\_remote\_features](structbt__hci__cp__le__read__remote__features.md)

**Definition** hci\_types.h:1211

[bt\_hci\_cp\_le\_read\_remote\_features::handle](structbt__hci__cp__le__read__remote__features.md#a843997555fd36f102c83a7d59f65eea9)

uint16\_t handle

**Definition** hci\_types.h:1212

[bt\_hci\_cp\_le\_read\_remote\_supported\_capabilities](structbt__hci__cp__le__read__remote__supported__capabilities.md)

**Definition** hci\_types.h:2464

[bt\_hci\_cp\_le\_read\_remote\_supported\_capabilities::handle](structbt__hci__cp__le__read__remote__supported__capabilities.md#ac6f083563e2c72d37cf4e9e8fa695733)

uint16\_t handle

**Definition** hci\_types.h:2465

[bt\_hci\_cp\_le\_read\_test\_counters](structbt__hci__cp__le__read__test__counters.md)

**Definition** hci\_types.h:2357

[bt\_hci\_cp\_le\_read\_test\_counters::handle](structbt__hci__cp__le__read__test__counters.md#a230d973c2db177c3595bb4808ebf5cd2)

uint16\_t handle

**Definition** hci\_types.h:2358

[bt\_hci\_cp\_le\_read\_tx\_power\_level](structbt__hci__cp__le__read__tx__power__level.md)

**Definition** hci\_types.h:677

[bt\_hci\_cp\_le\_read\_tx\_power\_level::phy](structbt__hci__cp__le__read__tx__power__level.md#a4863396dfe4dca65aaef68293e29291b)

uint8\_t phy

**Definition** hci\_types.h:679

[bt\_hci\_cp\_le\_read\_tx\_power\_level::handle](structbt__hci__cp__le__read__tx__power__level.md#af8c2d89b183d7bdc0f55a0bf783a373d)

uint16\_t handle

**Definition** hci\_types.h:678

[bt\_hci\_cp\_le\_reject\_cis](structbt__hci__cp__le__reject__cis.md)

**Definition** hci\_types.h:2224

[bt\_hci\_cp\_le\_reject\_cis::handle](structbt__hci__cp__le__reject__cis.md#ad697d740bdf5a565090a548e7e8fd399)

uint16\_t handle

**Definition** hci\_types.h:2225

[bt\_hci\_cp\_le\_reject\_cis::reason](structbt__hci__cp__le__reject__cis.md#aec5bd3e4d27b6e3a2653112b36a3d128)

uint8\_t reason

**Definition** hci\_types.h:2226

[bt\_hci\_cp\_le\_rem\_dev\_from\_fal](structbt__hci__cp__le__rem__dev__from__fal.md)

**Definition** hci\_types.h:1180

[bt\_hci\_cp\_le\_rem\_dev\_from\_fal::addr](structbt__hci__cp__le__rem__dev__from__fal.md#afe6054303093cc930d1089ca6a16101c)

bt\_addr\_le\_t addr

**Definition** hci\_types.h:1181

[bt\_hci\_cp\_le\_rem\_dev\_from\_per\_adv\_list](structbt__hci__cp__le__rem__dev__from__per__adv__list.md)

**Definition** hci\_types.h:1816

[bt\_hci\_cp\_le\_rem\_dev\_from\_per\_adv\_list::sid](structbt__hci__cp__le__rem__dev__from__per__adv__list.md#a6629f3ececf586792a14f3c028cc8e8c)

uint8\_t sid

**Definition** hci\_types.h:1818

[bt\_hci\_cp\_le\_rem\_dev\_from\_per\_adv\_list::addr](structbt__hci__cp__le__rem__dev__from__per__adv__list.md#adc420288f6a79c1a92f57241d3da3d81)

bt\_addr\_le\_t addr

**Definition** hci\_types.h:1817

[bt\_hci\_cp\_le\_rem\_dev\_from\_rl](structbt__hci__cp__le__rem__dev__from__rl.md)

**Definition** hci\_types.h:1367

[bt\_hci\_cp\_le\_rem\_dev\_from\_rl::peer\_id\_addr](structbt__hci__cp__le__rem__dev__from__rl.md#aacb577a7ae13322145fccdffc3161541)

bt\_addr\_le\_t peer\_id\_addr

**Definition** hci\_types.h:1368

[bt\_hci\_cp\_le\_remove\_adv\_set](structbt__hci__cp__le__remove__adv__set.md)

**Definition** hci\_types.h:1626

[bt\_hci\_cp\_le\_remove\_adv\_set::handle](structbt__hci__cp__le__remove__adv__set.md#ab33bf918b10d847bb8fb8ac2409780e6)

uint8\_t handle

**Definition** hci\_types.h:1627

[bt\_hci\_cp\_le\_remove\_cig](structbt__hci__cp__le__remove__cig.md)

**Definition** hci\_types.h:2209

[bt\_hci\_cp\_le\_remove\_cig::cig\_id](structbt__hci__cp__le__remove__cig.md#addf395d945f14afbf2d39fa4d0d22f31)

uint8\_t cig\_id

**Definition** hci\_types.h:2210

[bt\_hci\_cp\_le\_remove\_iso\_path](structbt__hci__cp__le__remove__iso__path.md)

**Definition** hci\_types.h:2320

[bt\_hci\_cp\_le\_remove\_iso\_path::path\_dir](structbt__hci__cp__le__remove__iso__path.md#a46e4b28917ff963ff4b672749fde0971)

uint8\_t path\_dir

**Definition** hci\_types.h:2322

[bt\_hci\_cp\_le\_remove\_iso\_path::handle](structbt__hci__cp__le__remove__iso__path.md#ad0106791003f9d1173f2a9f102903c45)

uint16\_t handle

**Definition** hci\_types.h:2321

[bt\_hci\_cp\_le\_req\_peer\_sca](structbt__hci__cp__le__req__peer__sca.md)

**Definition** hci\_types.h:2299

[bt\_hci\_cp\_le\_req\_peer\_sca::handle](structbt__hci__cp__le__req__peer__sca.md#a39d65681da55b26f2900f06cde637d88)

uint16\_t handle

**Definition** hci\_types.h:2300

[bt\_hci\_cp\_le\_rx\_test\_v3](structbt__hci__cp__le__rx__test__v3.md)

**Definition** hci\_types.h:1864

[bt\_hci\_cp\_le\_rx\_test\_v3::expected\_cte\_type](structbt__hci__cp__le__rx__test__v3.md#a55b5c4739e456167f17bf3899d096e61)

uint8\_t expected\_cte\_type

**Definition** hci\_types.h:1869

[bt\_hci\_cp\_le\_rx\_test\_v3::slot\_durations](structbt__hci__cp__le__rx__test__v3.md#a5cd5a44b0832b9f6e2198b9ad714b99b)

uint8\_t slot\_durations

**Definition** hci\_types.h:1870

[bt\_hci\_cp\_le\_rx\_test\_v3::mod\_index](structbt__hci__cp__le__rx__test__v3.md#a7ffde9dc565194c0108177cf11b02b5b)

uint8\_t mod\_index

**Definition** hci\_types.h:1867

[bt\_hci\_cp\_le\_rx\_test\_v3::ant\_ids](structbt__hci__cp__le__rx__test__v3.md#aa6cd0835068f378949da182af13e2438)

uint8\_t ant\_ids[0]

**Definition** hci\_types.h:1872

[bt\_hci\_cp\_le\_rx\_test\_v3::switch\_pattern\_len](structbt__hci__cp__le__rx__test__v3.md#ab0832e72ef90b1269928378638fcb194)

uint8\_t switch\_pattern\_len

**Definition** hci\_types.h:1871

[bt\_hci\_cp\_le\_rx\_test\_v3::rx\_ch](structbt__hci__cp__le__rx__test__v3.md#abd33b70c948d4ee42d96d0d2e7f7cb1c)

uint8\_t rx\_ch

**Definition** hci\_types.h:1865

[bt\_hci\_cp\_le\_rx\_test\_v3::expected\_cte\_len](structbt__hci__cp__le__rx__test__v3.md#ad1a1082d27b8a10e25eebd347404637c)

uint8\_t expected\_cte\_len

**Definition** hci\_types.h:1868

[bt\_hci\_cp\_le\_rx\_test\_v3::phy](structbt__hci__cp__le__rx__test__v3.md#ad1c211c59cf34d76429d4d4548966630)

uint8\_t phy

**Definition** hci\_types.h:1866

[bt\_hci\_cp\_le\_rx\_test](structbt__hci__cp__le__rx__test.md)

**Definition** hci\_types.h:1265

[bt\_hci\_cp\_le\_rx\_test::rx\_ch](structbt__hci__cp__le__rx__test.md#a11cb21a7625d9c097eba0a7b68e93f3f)

uint8\_t rx\_ch

**Definition** hci\_types.h:1266

[bt\_hci\_cp\_le\_security\_enable](structbt__hci__cp__le__security__enable.md)

**Definition** hci\_types.h:2497

[bt\_hci\_cp\_le\_security\_enable::handle](structbt__hci__cp__le__security__enable.md#a772d3744d43f0447187040f2c6f0ac6e)

uint16\_t handle

**Definition** hci\_types.h:2498

[bt\_hci\_cp\_le\_set\_addr\_res\_enable](structbt__hci__cp__le__set__addr__res__enable.md)

**Definition** hci\_types.h:1401

[bt\_hci\_cp\_le\_set\_addr\_res\_enable::enable](structbt__hci__cp__le__set__addr__res__enable.md#ad0548178cbc9bc2db54612a748a2bd65)

uint8\_t enable

**Definition** hci\_types.h:1402

[bt\_hci\_cp\_le\_set\_adv\_data](structbt__hci__cp__le__set__adv__data.md)

**Definition** hci\_types.h:1095

[bt\_hci\_cp\_le\_set\_adv\_data::len](structbt__hci__cp__le__set__adv__data.md#a664313db17c12adb0de14371e46d26a8)

uint8\_t len

**Definition** hci\_types.h:1096

[bt\_hci\_cp\_le\_set\_adv\_data::data](structbt__hci__cp__le__set__adv__data.md#a6fb8734ff5a9b77586b3e283b83985bb)

uint8\_t data[31]

**Definition** hci\_types.h:1097

[bt\_hci\_cp\_le\_set\_adv\_enable](structbt__hci__cp__le__set__adv__enable.md)

**Definition** hci\_types.h:1110

[bt\_hci\_cp\_le\_set\_adv\_enable::enable](structbt__hci__cp__le__set__adv__enable.md#a15e92d187d586fef560adf9c793f776a)

uint8\_t enable

**Definition** hci\_types.h:1111

[bt\_hci\_cp\_le\_set\_adv\_param](structbt__hci__cp__le__set__adv__param.md)

**Definition** hci\_types.h:1078

[bt\_hci\_cp\_le\_set\_adv\_param::channel\_map](structbt__hci__cp__le__set__adv__param.md#a2269ae424e47adddce5aa5f2f5b84c89)

uint8\_t channel\_map

**Definition** hci\_types.h:1084

[bt\_hci\_cp\_le\_set\_adv\_param::min\_interval](structbt__hci__cp__le__set__adv__param.md#a2476c2a1858eab7e9b1449c1901363c4)

uint16\_t min\_interval

**Definition** hci\_types.h:1079

[bt\_hci\_cp\_le\_set\_adv\_param::filter\_policy](structbt__hci__cp__le__set__adv__param.md#a662c5ae81f25a897a8e597f7227a1e39)

uint8\_t filter\_policy

**Definition** hci\_types.h:1085

[bt\_hci\_cp\_le\_set\_adv\_param::type](structbt__hci__cp__le__set__adv__param.md#a9b09964156846fd480911dcc2d996a98)

uint8\_t type

**Definition** hci\_types.h:1081

[bt\_hci\_cp\_le\_set\_adv\_param::max\_interval](structbt__hci__cp__le__set__adv__param.md#ab42c6b8f482e782d09386a3a1758903d)

uint16\_t max\_interval

**Definition** hci\_types.h:1080

[bt\_hci\_cp\_le\_set\_adv\_param::direct\_addr](structbt__hci__cp__le__set__adv__param.md#ac774ef72175e43b083d04ecac263941b)

bt\_addr\_le\_t direct\_addr

**Definition** hci\_types.h:1083

[bt\_hci\_cp\_le\_set\_adv\_param::own\_addr\_type](structbt__hci__cp__le__set__adv__param.md#ad8c74cac74254354b314f07df7df1bf0)

uint8\_t own\_addr\_type

**Definition** hci\_types.h:1082

[bt\_hci\_cp\_le\_set\_adv\_set\_random\_addr](structbt__hci__cp__le__set__adv__set__random__addr.md)

**Definition** hci\_types.h:1500

[bt\_hci\_cp\_le\_set\_adv\_set\_random\_addr::bdaddr](structbt__hci__cp__le__set__adv__set__random__addr.md#a2883e9bf7ef6a34712eda2594e23c146)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:1502

[bt\_hci\_cp\_le\_set\_adv\_set\_random\_addr::handle](structbt__hci__cp__le__set__adv__set__random__addr.md#aafa39422a16cc4ff11c8073e9c0aab71)

uint8\_t handle

**Definition** hci\_types.h:1501

[bt\_hci\_cp\_le\_set\_cig\_params\_test](structbt__hci__cp__le__set__cig__params__test.md)

**Definition** hci\_types.h:2176

[bt\_hci\_cp\_le\_set\_cig\_params\_test::p\_interval](structbt__hci__cp__le__set__cig__params__test.md#a0cf0f3f7c10b29d74ab64aa30a4969de)

uint8\_t p\_interval[3]

**Definition** hci\_types.h:2179

[bt\_hci\_cp\_le\_set\_cig\_params\_test::cig\_id](structbt__hci__cp__le__set__cig__params__test.md#a161ae960cbd4f7833815285d04f87e46)

uint8\_t cig\_id

**Definition** hci\_types.h:2177

[bt\_hci\_cp\_le\_set\_cig\_params\_test::sca](structbt__hci__cp__le__set__cig__params__test.md#a1d060539ff26677c1326a6ed3394fb6e)

uint8\_t sca

**Definition** hci\_types.h:2183

[bt\_hci\_cp\_le\_set\_cig\_params\_test::c\_ft](structbt__hci__cp__le__set__cig__params__test.md#a1eae50a97188304852589fd95e994150)

uint8\_t c\_ft

**Definition** hci\_types.h:2180

[bt\_hci\_cp\_le\_set\_cig\_params\_test::framing](structbt__hci__cp__le__set__cig__params__test.md#a2cb6745b8f908cd2e7d5f12a092c3b69)

uint8\_t framing

**Definition** hci\_types.h:2185

[bt\_hci\_cp\_le\_set\_cig\_params\_test::num\_cis](structbt__hci__cp__le__set__cig__params__test.md#a50c345ef03c669f476e143728f42cd6d)

uint8\_t num\_cis

**Definition** hci\_types.h:2186

[bt\_hci\_cp\_le\_set\_cig\_params\_test::cis](structbt__hci__cp__le__set__cig__params__test.md#a5e07eb0d7d13e57be457d1b77a5dba12)

struct bt\_hci\_cis\_params\_test cis[0]

**Definition** hci\_types.h:2187

[bt\_hci\_cp\_le\_set\_cig\_params\_test::packing](structbt__hci__cp__le__set__cig__params__test.md#a7275312e8b1c8ebc2af7992f765b392c)

uint8\_t packing

**Definition** hci\_types.h:2184

[bt\_hci\_cp\_le\_set\_cig\_params\_test::c\_interval](structbt__hci__cp__le__set__cig__params__test.md#aa392cbac058beefd0e410fcc9821a0c3)

uint8\_t c\_interval[3]

**Definition** hci\_types.h:2178

[bt\_hci\_cp\_le\_set\_cig\_params\_test::iso\_interval](structbt__hci__cp__le__set__cig__params__test.md#aa77765d90fde67c52e4f2d483f0a3ee0)

uint16\_t iso\_interval

**Definition** hci\_types.h:2182

[bt\_hci\_cp\_le\_set\_cig\_params\_test::p\_ft](structbt__hci__cp__le__set__cig__params__test.md#af2ed1bf1a6beaff884c3ce3faf26bfb2)

uint8\_t p\_ft

**Definition** hci\_types.h:2181

[bt\_hci\_cp\_le\_set\_cig\_params](structbt__hci__cp__le__set__cig__params.md)

**Definition** hci\_types.h:2142

[bt\_hci\_cp\_le\_set\_cig\_params::c\_interval](structbt__hci__cp__le__set__cig__params.md#a14f5c0cf7f99ab406714501038048035)

uint8\_t c\_interval[3]

**Definition** hci\_types.h:2144

[bt\_hci\_cp\_le\_set\_cig\_params::sca](structbt__hci__cp__le__set__cig__params.md#a46a657cdfbc7a49e6761d9f18d980c2a)

uint8\_t sca

**Definition** hci\_types.h:2146

[bt\_hci\_cp\_le\_set\_cig\_params::p\_interval](structbt__hci__cp__le__set__cig__params.md#a50a260a15f3a0ceae716da6c04c5b768)

uint8\_t p\_interval[3]

**Definition** hci\_types.h:2145

[bt\_hci\_cp\_le\_set\_cig\_params::packing](structbt__hci__cp__le__set__cig__params.md#a79fc069492741f14f348650abef4c66b)

uint8\_t packing

**Definition** hci\_types.h:2147

[bt\_hci\_cp\_le\_set\_cig\_params::cig\_id](structbt__hci__cp__le__set__cig__params.md#a7dbf75c6ed92a053c4ec0d8f7268c92e)

uint8\_t cig\_id

**Definition** hci\_types.h:2143

[bt\_hci\_cp\_le\_set\_cig\_params::p\_latency](structbt__hci__cp__le__set__cig__params.md#a810822396b97d54988ec57561b4ee7d5)

uint16\_t p\_latency

**Definition** hci\_types.h:2150

[bt\_hci\_cp\_le\_set\_cig\_params::framing](structbt__hci__cp__le__set__cig__params.md#a867bf5ddbcadd27dbec2c3059d67d6d6)

uint8\_t framing

**Definition** hci\_types.h:2148

[bt\_hci\_cp\_le\_set\_cig\_params::cis](structbt__hci__cp__le__set__cig__params.md#ac922e59065920421f40468754d2ba5a2)

struct bt\_hci\_cis\_params cis[0]

**Definition** hci\_types.h:2152

[bt\_hci\_cp\_le\_set\_cig\_params::num\_cis](structbt__hci__cp__le__set__cig__params.md#adf468a8a195447a7bbed4dcd53d287f6)

uint8\_t num\_cis

**Definition** hci\_types.h:2151

[bt\_hci\_cp\_le\_set\_cig\_params::c\_latency](structbt__hci__cp__le__set__cig__params.md#afec8ebd17cc6ca5b3d13ef54f406df62)

uint16\_t c\_latency

**Definition** hci\_types.h:2149

[bt\_hci\_cp\_le\_set\_cl\_cte\_sampling\_enable](structbt__hci__cp__le__set__cl__cte__sampling__enable.md)

**Definition** hci\_types.h:1924

[bt\_hci\_cp\_le\_set\_cl\_cte\_sampling\_enable::max\_sampled\_cte](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#a38e770b3e5f9d7d63a564dfa7c80451f)

uint8\_t max\_sampled\_cte

**Definition** hci\_types.h:1928

[bt\_hci\_cp\_le\_set\_cl\_cte\_sampling\_enable::switch\_pattern\_len](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#a4f52142ef1d2365859189b7a2abe050b)

uint8\_t switch\_pattern\_len

**Definition** hci\_types.h:1929

[bt\_hci\_cp\_le\_set\_cl\_cte\_sampling\_enable::ant\_ids](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#a67bb2dbfe1707f76a5e211e007459c22)

uint8\_t ant\_ids[0]

**Definition** hci\_types.h:1930

[bt\_hci\_cp\_le\_set\_cl\_cte\_sampling\_enable::sync\_handle](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#a91d3458e2049ab434e220403b7ba235d)

uint16\_t sync\_handle

**Definition** hci\_types.h:1925

[bt\_hci\_cp\_le\_set\_cl\_cte\_sampling\_enable::slot\_durations](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#aaaed0fc39158c653041fd760a00cecec)

uint8\_t slot\_durations

**Definition** hci\_types.h:1927

[bt\_hci\_cp\_le\_set\_cl\_cte\_sampling\_enable::sampling\_enable](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#aca9e1316c716525f00308f64b8c6cec4)

uint8\_t sampling\_enable

**Definition** hci\_types.h:1926

[bt\_hci\_cp\_le\_set\_cl\_cte\_tx\_enable](structbt__hci__cp__le__set__cl__cte__tx__enable.md)

**Definition** hci\_types.h:1911

[bt\_hci\_cp\_le\_set\_cl\_cte\_tx\_enable::cte\_enable](structbt__hci__cp__le__set__cl__cte__tx__enable.md#a3530dae940caefeafb9de4ac761ee080)

uint8\_t cte\_enable

**Definition** hci\_types.h:1913

[bt\_hci\_cp\_le\_set\_cl\_cte\_tx\_enable::handle](structbt__hci__cp__le__set__cl__cte__tx__enable.md#a55125c808a888eeecfee9410bcb55859)

uint8\_t handle

**Definition** hci\_types.h:1912

[bt\_hci\_cp\_le\_set\_cl\_cte\_tx\_params](structbt__hci__cp__le__set__cl__cte__tx__params.md)

**Definition** hci\_types.h:1901

[bt\_hci\_cp\_le\_set\_cl\_cte\_tx\_params::ant\_ids](structbt__hci__cp__le__set__cl__cte__tx__params.md#a27a228653ea560a77369a6b1829a8a9d)

uint8\_t ant\_ids[0]

**Definition** hci\_types.h:1907

[bt\_hci\_cp\_le\_set\_cl\_cte\_tx\_params::switch\_pattern\_len](structbt__hci__cp__le__set__cl__cte__tx__params.md#a8208571653e444221648d2a884eabfae)

uint8\_t switch\_pattern\_len

**Definition** hci\_types.h:1906

[bt\_hci\_cp\_le\_set\_cl\_cte\_tx\_params::cte\_type](structbt__hci__cp__le__set__cl__cte__tx__params.md#a869192cea35f4cd57984614e4c8bb5a5)

uint8\_t cte\_type

**Definition** hci\_types.h:1904

[bt\_hci\_cp\_le\_set\_cl\_cte\_tx\_params::handle](structbt__hci__cp__le__set__cl__cte__tx__params.md#a8f20e6e3bb408551d6cc494ad19391c4)

uint8\_t handle

**Definition** hci\_types.h:1902

[bt\_hci\_cp\_le\_set\_cl\_cte\_tx\_params::cte\_len](structbt__hci__cp__le__set__cl__cte__tx__params.md#ab5c4742cf37cf7e802423beb4a9b4fa2)

uint8\_t cte\_len

**Definition** hci\_types.h:1903

[bt\_hci\_cp\_le\_set\_cl\_cte\_tx\_params::cte\_count](structbt__hci__cp__le__set__cl__cte__tx__params.md#af5e82bf572b385904a0f24219bdc72ca)

uint8\_t cte\_count

**Definition** hci\_types.h:1905

[bt\_hci\_cp\_le\_set\_conn\_cte\_rx\_params](structbt__hci__cp__le__set__conn__cte__rx__params.md)

**Definition** hci\_types.h:1939

[bt\_hci\_cp\_le\_set\_conn\_cte\_rx\_params::ant\_ids](structbt__hci__cp__le__set__conn__cte__rx__params.md#a519c37f5d797d8ddac5ba9be7c14b9f9)

uint8\_t ant\_ids[0]

**Definition** hci\_types.h:1944

[bt\_hci\_cp\_le\_set\_conn\_cte\_rx\_params::sampling\_enable](structbt__hci__cp__le__set__conn__cte__rx__params.md#a615cae822878cf1344a990e30fa80044)

uint8\_t sampling\_enable

**Definition** hci\_types.h:1941

[bt\_hci\_cp\_le\_set\_conn\_cte\_rx\_params::slot\_durations](structbt__hci__cp__le__set__conn__cte__rx__params.md#a6246d492b94c67af9604b89912dbdb61)

uint8\_t slot\_durations

**Definition** hci\_types.h:1942

[bt\_hci\_cp\_le\_set\_conn\_cte\_rx\_params::handle](structbt__hci__cp__le__set__conn__cte__rx__params.md#a76968866cf5c6ef4bfb983cb6b68a827)

uint16\_t handle

**Definition** hci\_types.h:1940

[bt\_hci\_cp\_le\_set\_conn\_cte\_rx\_params::switch\_pattern\_len](structbt__hci__cp__le__set__conn__cte__rx__params.md#a89194a5b9e6c7f0c176c915e451911df)

uint8\_t switch\_pattern\_len

**Definition** hci\_types.h:1943

[bt\_hci\_cp\_le\_set\_conn\_cte\_tx\_params](structbt__hci__cp__le__set__conn__cte__tx__params.md)

**Definition** hci\_types.h:1960

[bt\_hci\_cp\_le\_set\_conn\_cte\_tx\_params::switch\_pattern\_len](structbt__hci__cp__le__set__conn__cte__tx__params.md#a8f0e5ee74662056f00eaa3a8c72f6fc4)

uint8\_t switch\_pattern\_len

**Definition** hci\_types.h:1963

[bt\_hci\_cp\_le\_set\_conn\_cte\_tx\_params::cte\_types](structbt__hci__cp__le__set__conn__cte__tx__params.md#ab47f852b476ac2c35fc0631180e19fb4)

uint8\_t cte\_types

**Definition** hci\_types.h:1962

[bt\_hci\_cp\_le\_set\_conn\_cte\_tx\_params::ant\_ids](structbt__hci__cp__le__set__conn__cte__tx__params.md#abff85d652b3b2fd55ad78e53887cd7ce)

uint8\_t ant\_ids[0]

**Definition** hci\_types.h:1964

[bt\_hci\_cp\_le\_set\_conn\_cte\_tx\_params::handle](structbt__hci__cp__le__set__conn__cte__tx__params.md#ae0a482982d804ffd7d16ea2b413e538d)

uint16\_t handle

**Definition** hci\_types.h:1961

[bt\_hci\_cp\_le\_set\_data\_len](structbt__hci__cp__le__set__data__len.md)

**Definition** hci\_types.h:1317

[bt\_hci\_cp\_le\_set\_data\_len::tx\_time](structbt__hci__cp__le__set__data__len.md#a15285a4e8bf8e359bb326de4b30ba8f1)

uint16\_t tx\_time

**Definition** hci\_types.h:1320

[bt\_hci\_cp\_le\_set\_data\_len::handle](structbt__hci__cp__le__set__data__len.md#a874869090428a7f380c5466353573eba)

uint16\_t handle

**Definition** hci\_types.h:1318

[bt\_hci\_cp\_le\_set\_data\_len::tx\_octets](structbt__hci__cp__le__set__data__len.md#ac579e84a004a09813bbe0ed61db11931)

uint16\_t tx\_octets

**Definition** hci\_types.h:1319

[bt\_hci\_cp\_le\_set\_default\_phy](structbt__hci__cp__le__set__default__phy.md)

**Definition** hci\_types.h:1453

[bt\_hci\_cp\_le\_set\_default\_phy::tx\_phys](structbt__hci__cp__le__set__default__phy.md#a0c4ab2d91021466fd136af3a0b6bde2a)

uint8\_t tx\_phys

**Definition** hci\_types.h:1455

[bt\_hci\_cp\_le\_set\_default\_phy::rx\_phys](structbt__hci__cp__le__set__default__phy.md#a4c3410f2ce9fb2817bc5d143908936d1)

uint8\_t rx\_phys

**Definition** hci\_types.h:1456

[bt\_hci\_cp\_le\_set\_default\_phy::all\_phys](structbt__hci__cp__le__set__default__phy.md#abe1d83e372e874739588812040d0b540)

uint8\_t all\_phys

**Definition** hci\_types.h:1454

[bt\_hci\_cp\_le\_set\_default\_subrate](structbt__hci__cp__le__set__default__subrate.md)

**Definition** hci\_types.h:721

[bt\_hci\_cp\_le\_set\_default\_subrate::max\_latency](structbt__hci__cp__le__set__default__subrate.md#a16adacc30fd5ae00b3944f068b075b1a)

uint16\_t max\_latency

**Definition** hci\_types.h:724

[bt\_hci\_cp\_le\_set\_default\_subrate::supervision\_timeout](structbt__hci__cp__le__set__default__subrate.md#a1906f4dd7955200c81093b8f7c5d55c0)

uint16\_t supervision\_timeout

**Definition** hci\_types.h:726

[bt\_hci\_cp\_le\_set\_default\_subrate::subrate\_min](structbt__hci__cp__le__set__default__subrate.md#a9d8fd7cad5260c8943b90ab50c04b225)

uint16\_t subrate\_min

**Definition** hci\_types.h:722

[bt\_hci\_cp\_le\_set\_default\_subrate::subrate\_max](structbt__hci__cp__le__set__default__subrate.md#ad18a8042c38a1b4d83d6fccad1ab5af8)

uint16\_t subrate\_max

**Definition** hci\_types.h:723

[bt\_hci\_cp\_le\_set\_default\_subrate::continuation\_number](structbt__hci__cp__le__set__default__subrate.md#aff2e682b4c8e5c3078885be126c5b958)

uint16\_t continuation\_number

**Definition** hci\_types.h:725

[bt\_hci\_cp\_le\_set\_event\_mask](structbt__hci__cp__le__set__event__mask.md)

**Definition** hci\_types.h:1034

[bt\_hci\_cp\_le\_set\_event\_mask::events](structbt__hci__cp__le__set__event__mask.md#af7de4823aca253f15e57f54ee9b3879e)

uint8\_t events[8]

**Definition** hci\_types.h:1035

[bt\_hci\_cp\_le\_set\_ext\_adv\_data](structbt__hci__cp__le__set__ext__adv__data.md)

**Definition** hci\_types.h:1583

[bt\_hci\_cp\_le\_set\_ext\_adv\_data::data](structbt__hci__cp__le__set__ext__adv__data.md#a7d7df52500eb53a64b6ba5e62f6cf14f)

uint8\_t data[0]

**Definition** hci\_types.h:1588

[bt\_hci\_cp\_le\_set\_ext\_adv\_data::handle](structbt__hci__cp__le__set__ext__adv__data.md#a803bb793eefcc714c6c4034123a2e487)

uint8\_t handle

**Definition** hci\_types.h:1584

[bt\_hci\_cp\_le\_set\_ext\_adv\_data::op](structbt__hci__cp__le__set__ext__adv__data.md#ac5eaa1834f82024055923d08a3bef6b3)

uint8\_t op

**Definition** hci\_types.h:1585

[bt\_hci\_cp\_le\_set\_ext\_adv\_data::len](structbt__hci__cp__le__set__ext__adv__data.md#aea3055cc7ffbaf4cd14996d885e21ba3)

uint8\_t len

**Definition** hci\_types.h:1587

[bt\_hci\_cp\_le\_set\_ext\_adv\_data::frag\_pref](structbt__hci__cp__le__set__ext__adv__data.md#af9eef9f59bfec5867ea36bdf33e3a9b1)

uint8\_t frag\_pref

**Definition** hci\_types.h:1586

[bt\_hci\_cp\_le\_set\_ext\_adv\_enable](structbt__hci__cp__le__set__ext__adv__enable.md)

**Definition** hci\_types.h:1607

[bt\_hci\_cp\_le\_set\_ext\_adv\_enable::s](structbt__hci__cp__le__set__ext__adv__enable.md#a04911e19f3b2f0079d4e12980d11157f)

struct bt\_hci\_ext\_adv\_set s[0]

**Definition** hci\_types.h:1610

[bt\_hci\_cp\_le\_set\_ext\_adv\_enable::set\_num](structbt__hci__cp__le__set__ext__adv__enable.md#a06088af8b432ac134943d9ebb7778ac7)

uint8\_t set\_num

**Definition** hci\_types.h:1609

[bt\_hci\_cp\_le\_set\_ext\_adv\_enable::enable](structbt__hci__cp__le__set__ext__adv__enable.md#ab7148b47bf052d8cba1f6bf3385051c8)

uint8\_t enable

**Definition** hci\_types.h:1608

[bt\_hci\_cp\_le\_set\_ext\_adv\_param\_v2](structbt__hci__cp__le__set__ext__adv__param__v2.md)

**Definition** hci\_types.h:1552

[bt\_hci\_cp\_le\_set\_ext\_adv\_param\_v2::filter\_policy](structbt__hci__cp__le__set__ext__adv__param__v2.md#a047656dd56bf883f1e307dcabe96f1de)

uint8\_t filter\_policy

**Definition** hci\_types.h:1560

[bt\_hci\_cp\_le\_set\_ext\_adv\_param\_v2::sec\_adv\_phy\_opt](structbt__hci__cp__le__set__ext__adv__param__v2.md#a0c7994ef034270a7fd814386e7b76cc8)

uint8\_t sec\_adv\_phy\_opt

**Definition** hci\_types.h:1568

[bt\_hci\_cp\_le\_set\_ext\_adv\_param\_v2::prim\_channel\_map](structbt__hci__cp__le__set__ext__adv__param__v2.md#a1a96a88729e311c6a60571997aae9fc3)

uint8\_t prim\_channel\_map

**Definition** hci\_types.h:1557

[bt\_hci\_cp\_le\_set\_ext\_adv\_param\_v2::prim\_min\_interval](structbt__hci__cp__le__set__ext__adv__param__v2.md#a25fec4dc9203bb50bb030087b42f473e)

uint8\_t prim\_min\_interval[3]

**Definition** hci\_types.h:1555

[bt\_hci\_cp\_le\_set\_ext\_adv\_param\_v2::tx\_power](structbt__hci__cp__le__set__ext__adv__param__v2.md#a5283a6a40d46e0fe787ed403acab9f90)

int8\_t tx\_power

**Definition** hci\_types.h:1561

[bt\_hci\_cp\_le\_set\_ext\_adv\_param\_v2::own\_addr\_type](structbt__hci__cp__le__set__ext__adv__param__v2.md#a554f89f00700bc3ea4996b0a971fedbf)

uint8\_t own\_addr\_type

**Definition** hci\_types.h:1558

[bt\_hci\_cp\_le\_set\_ext\_adv\_param\_v2::prim\_max\_interval](structbt__hci__cp__le__set__ext__adv__param__v2.md#a6098216ae6ef0f9459aae16adecd193f)

uint8\_t prim\_max\_interval[3]

**Definition** hci\_types.h:1556

[bt\_hci\_cp\_le\_set\_ext\_adv\_param\_v2::sec\_adv\_phy](structbt__hci__cp__le__set__ext__adv__param__v2.md#a6c2a953fab938f304e815bd9d59d05ae)

uint8\_t sec\_adv\_phy

**Definition** hci\_types.h:1564

[bt\_hci\_cp\_le\_set\_ext\_adv\_param\_v2::prim\_adv\_phy\_opt](structbt__hci__cp__le__set__ext__adv__param__v2.md#a8767fb7f5492f0323edd9afb687318db)

uint8\_t prim\_adv\_phy\_opt

**Definition** hci\_types.h:1567

[bt\_hci\_cp\_le\_set\_ext\_adv\_param\_v2::prim\_adv\_phy](structbt__hci__cp__le__set__ext__adv__param__v2.md#a92a215151c603c2f8dd1b7e730a8e979)

uint8\_t prim\_adv\_phy

**Definition** hci\_types.h:1562

[bt\_hci\_cp\_le\_set\_ext\_adv\_param\_v2::scan\_req\_notify\_enable](structbt__hci__cp__le__set__ext__adv__param__v2.md#a9f2a6f38e8965dabe17ad743d3aeda70)

uint8\_t scan\_req\_notify\_enable

**Definition** hci\_types.h:1566

[bt\_hci\_cp\_le\_set\_ext\_adv\_param\_v2::sec\_adv\_max\_skip](structbt__hci__cp__le__set__ext__adv__param__v2.md#ac31b52df1033d11585781fbecc10f578)

uint8\_t sec\_adv\_max\_skip

**Definition** hci\_types.h:1563

[bt\_hci\_cp\_le\_set\_ext\_adv\_param\_v2::peer\_addr](structbt__hci__cp__le__set__ext__adv__param__v2.md#ad8fccd11fbea598de62e057a69b72156)

bt\_addr\_le\_t peer\_addr

**Definition** hci\_types.h:1559

[bt\_hci\_cp\_le\_set\_ext\_adv\_param\_v2::handle](structbt__hci__cp__le__set__ext__adv__param__v2.md#ad9e43219b471e44884b33ea5ddd90513)

uint8\_t handle

**Definition** hci\_types.h:1553

[bt\_hci\_cp\_le\_set\_ext\_adv\_param\_v2::sid](structbt__hci__cp__le__set__ext__adv__param__v2.md#aeb26f7f16e2c71542421aada577a993f)

uint8\_t sid

**Definition** hci\_types.h:1565

[bt\_hci\_cp\_le\_set\_ext\_adv\_param\_v2::props](structbt__hci__cp__le__set__ext__adv__param__v2.md#aff572d12a03ca9cbc2ee80f75e1f77c7)

uint16\_t props

**Definition** hci\_types.h:1554

[bt\_hci\_cp\_le\_set\_ext\_adv\_param](structbt__hci__cp__le__set__ext__adv__param.md)

**Definition** hci\_types.h:1526

[bt\_hci\_cp\_le\_set\_ext\_adv\_param::prim\_adv\_phy](structbt__hci__cp__le__set__ext__adv__param.md#a048874197ccbdbc626f0563be5c41ec7)

uint8\_t prim\_adv\_phy

**Definition** hci\_types.h:1536

[bt\_hci\_cp\_le\_set\_ext\_adv\_param::prim\_max\_interval](structbt__hci__cp__le__set__ext__adv__param.md#a08aa741a56e825a11424bf024ac65e14)

uint8\_t prim\_max\_interval[3]

**Definition** hci\_types.h:1530

[bt\_hci\_cp\_le\_set\_ext\_adv\_param::filter\_policy](structbt__hci__cp__le__set__ext__adv__param.md#a29a62f8989f89b014cadbad9b94e996a)

uint8\_t filter\_policy

**Definition** hci\_types.h:1534

[bt\_hci\_cp\_le\_set\_ext\_adv\_param::own\_addr\_type](structbt__hci__cp__le__set__ext__adv__param.md#a3594f7337ccd739f59ac7845757de0e8)

uint8\_t own\_addr\_type

**Definition** hci\_types.h:1532

[bt\_hci\_cp\_le\_set\_ext\_adv\_param::props](structbt__hci__cp__le__set__ext__adv__param.md#a4af102ae90ca6917b3134491c5ff079f)

uint16\_t props

**Definition** hci\_types.h:1528

[bt\_hci\_cp\_le\_set\_ext\_adv\_param::sec\_adv\_max\_skip](structbt__hci__cp__le__set__ext__adv__param.md#a5793c6afe545290a1e792bcc73585b72)

uint8\_t sec\_adv\_max\_skip

**Definition** hci\_types.h:1537

[bt\_hci\_cp\_le\_set\_ext\_adv\_param::tx\_power](structbt__hci__cp__le__set__ext__adv__param.md#a5f7f3e477b5b0b8122b85f3e53dd7878)

int8\_t tx\_power

**Definition** hci\_types.h:1535

[bt\_hci\_cp\_le\_set\_ext\_adv\_param::handle](structbt__hci__cp__le__set__ext__adv__param.md#a65fe609dde9515212659087a024e7c65)

uint8\_t handle

**Definition** hci\_types.h:1527

[bt\_hci\_cp\_le\_set\_ext\_adv\_param::peer\_addr](structbt__hci__cp__le__set__ext__adv__param.md#a819e599df4025036fab2dabd7c61ea37)

bt\_addr\_le\_t peer\_addr

**Definition** hci\_types.h:1533

[bt\_hci\_cp\_le\_set\_ext\_adv\_param::prim\_min\_interval](structbt__hci__cp__le__set__ext__adv__param.md#ab5a80941b3d832c2906daed8cf069a02)

uint8\_t prim\_min\_interval[3]

**Definition** hci\_types.h:1529

[bt\_hci\_cp\_le\_set\_ext\_adv\_param::sec\_adv\_phy](structbt__hci__cp__le__set__ext__adv__param.md#abc82ba984647eb00bc490c01ce746a15)

uint8\_t sec\_adv\_phy

**Definition** hci\_types.h:1538

[bt\_hci\_cp\_le\_set\_ext\_adv\_param::prim\_channel\_map](structbt__hci__cp__le__set__ext__adv__param.md#ad7a0b9028bcdb57a9011d4677412aed5)

uint8\_t prim\_channel\_map

**Definition** hci\_types.h:1531

[bt\_hci\_cp\_le\_set\_ext\_adv\_param::scan\_req\_notify\_enable](structbt__hci__cp__le__set__ext__adv__param.md#ae694df46b1db4b029d1e177768b3821f)

uint8\_t scan\_req\_notify\_enable

**Definition** hci\_types.h:1540

[bt\_hci\_cp\_le\_set\_ext\_adv\_param::sid](structbt__hci__cp__le__set__ext__adv__param.md#af8bc3509fdd5e89c27db466727fe1cd9)

uint8\_t sid

**Definition** hci\_types.h:1539

[bt\_hci\_cp\_le\_set\_ext\_scan\_enable](structbt__hci__cp__le__set__ext__scan__enable.md)

**Definition** hci\_types.h:1689

[bt\_hci\_cp\_le\_set\_ext\_scan\_enable::enable](structbt__hci__cp__le__set__ext__scan__enable.md#a922d0c5a7ccb6c1e1864f662227b8307)

uint8\_t enable

**Definition** hci\_types.h:1690

[bt\_hci\_cp\_le\_set\_ext\_scan\_enable::filter\_dup](structbt__hci__cp__le__set__ext__scan__enable.md#aa5b0939838ab13eb8299f4a4b2fd3f14)

uint8\_t filter\_dup

**Definition** hci\_types.h:1691

[bt\_hci\_cp\_le\_set\_ext\_scan\_enable::period](structbt__hci__cp__le__set__ext__scan__enable.md#aa60c8ade7047dcd202d83cfc3f18ada2)

uint16\_t period

**Definition** hci\_types.h:1693

[bt\_hci\_cp\_le\_set\_ext\_scan\_enable::duration](structbt__hci__cp__le__set__ext__scan__enable.md#adcd5e00a240f3e7395d0d25994b4013a)

uint16\_t duration

**Definition** hci\_types.h:1692

[bt\_hci\_cp\_le\_set\_ext\_scan\_param](structbt__hci__cp__le__set__ext__scan__param.md)

**Definition** hci\_types.h:1678

[bt\_hci\_cp\_le\_set\_ext\_scan\_param::own\_addr\_type](structbt__hci__cp__le__set__ext__scan__param.md#a3418aa8dbdb8062ee452f5756eb9f30c)

uint8\_t own\_addr\_type

**Definition** hci\_types.h:1679

[bt\_hci\_cp\_le\_set\_ext\_scan\_param::filter\_policy](structbt__hci__cp__le__set__ext__scan__param.md#a47f6cf7f83451dcc2feac1a8d5837ad8)

uint8\_t filter\_policy

**Definition** hci\_types.h:1680

[bt\_hci\_cp\_le\_set\_ext\_scan\_param::phys](structbt__hci__cp__le__set__ext__scan__param.md#a6c38b7d074eb3c0cf5c301eb6c03b60c)

uint8\_t phys

**Definition** hci\_types.h:1681

[bt\_hci\_cp\_le\_set\_ext\_scan\_param::p](structbt__hci__cp__le__set__ext__scan__param.md#ab4eab9a52dca01bc19b35607d6ec5d36)

struct bt\_hci\_ext\_scan\_phy p[0]

**Definition** hci\_types.h:1682

[bt\_hci\_cp\_le\_set\_ext\_scan\_rsp\_data](structbt__hci__cp__le__set__ext__scan__rsp__data.md)

**Definition** hci\_types.h:1592

[bt\_hci\_cp\_le\_set\_ext\_scan\_rsp\_data::op](structbt__hci__cp__le__set__ext__scan__rsp__data.md#a3323a0844680b71cb8aedffa034837d7)

uint8\_t op

**Definition** hci\_types.h:1594

[bt\_hci\_cp\_le\_set\_ext\_scan\_rsp\_data::len](structbt__hci__cp__le__set__ext__scan__rsp__data.md#a6024eac85f600ed3b7051a84b91bdcfa)

uint8\_t len

**Definition** hci\_types.h:1596

[bt\_hci\_cp\_le\_set\_ext\_scan\_rsp\_data::handle](structbt__hci__cp__le__set__ext__scan__rsp__data.md#a8cf0624b9968686c7f6765ee25e11c90)

uint8\_t handle

**Definition** hci\_types.h:1593

[bt\_hci\_cp\_le\_set\_ext\_scan\_rsp\_data::data](structbt__hci__cp__le__set__ext__scan__rsp__data.md#ab086720e1a22523ba155cb238ad75197)

uint8\_t data[0]

**Definition** hci\_types.h:1597

[bt\_hci\_cp\_le\_set\_ext\_scan\_rsp\_data::frag\_pref](structbt__hci__cp__le__set__ext__scan__rsp__data.md#ac4e1691926df370b290c9e6d866d310d)

uint8\_t frag\_pref

**Definition** hci\_types.h:1595

[bt\_hci\_cp\_le\_set\_host\_chan\_classif](structbt__hci__cp__le__set__host__chan__classif.md)

**Definition** hci\_types.h:1196

[bt\_hci\_cp\_le\_set\_host\_chan\_classif::ch\_map](structbt__hci__cp__le__set__host__chan__classif.md#a0fb81bcdebe7da416cc4317486106752)

uint8\_t ch\_map[5]

**Definition** hci\_types.h:1197

[bt\_hci\_cp\_le\_set\_host\_feature](structbt__hci__cp__le__set__host__feature.md)

**Definition** hci\_types.h:2383

[bt\_hci\_cp\_le\_set\_host\_feature::bit\_value](structbt__hci__cp__le__set__host__feature.md#a78b67164bce232466ab348f8937682c3)

uint8\_t bit\_value

**Definition** hci\_types.h:2385

[bt\_hci\_cp\_le\_set\_host\_feature::bit\_number](structbt__hci__cp__le__set__host__feature.md#adcca35df216061ea08bd27e10fefd5e9)

uint8\_t bit\_number

**Definition** hci\_types.h:2384

[bt\_hci\_cp\_le\_set\_path\_loss\_reporting\_enable](structbt__hci__cp__le__set__path__loss__reporting__enable.md)

**Definition** hci\_types.h:710

[bt\_hci\_cp\_le\_set\_path\_loss\_reporting\_enable::enable](structbt__hci__cp__le__set__path__loss__reporting__enable.md#a209a77ef3cf545150feaecdb814797f0)

uint8\_t enable

**Definition** hci\_types.h:712

[bt\_hci\_cp\_le\_set\_path\_loss\_reporting\_enable::handle](structbt__hci__cp__le__set__path__loss__reporting__enable.md#a79487ac2235da100b41ec50c77bad808)

uint16\_t handle

**Definition** hci\_types.h:711

[bt\_hci\_cp\_le\_set\_path\_loss\_reporting\_parameters](structbt__hci__cp__le__set__path__loss__reporting__parameters.md)

**Definition** hci\_types.h:701

[bt\_hci\_cp\_le\_set\_path\_loss\_reporting\_parameters::min\_time\_spent](structbt__hci__cp__le__set__path__loss__reporting__parameters.md#a2289e8198eea1686030ffd3e225c8e7d)

uint16\_t min\_time\_spent

**Definition** hci\_types.h:707

[bt\_hci\_cp\_le\_set\_path\_loss\_reporting\_parameters::low\_hysteresis](structbt__hci__cp__le__set__path__loss__reporting__parameters.md#a28f79bd4ccec4ed108e20a0080ec842d)

uint8\_t low\_hysteresis

**Definition** hci\_types.h:706

[bt\_hci\_cp\_le\_set\_path\_loss\_reporting\_parameters::handle](structbt__hci__cp__le__set__path__loss__reporting__parameters.md#a2dec83b0269835538cf4bc5553483f19)

uint16\_t handle

**Definition** hci\_types.h:702

[bt\_hci\_cp\_le\_set\_path\_loss\_reporting\_parameters::low\_threshold](structbt__hci__cp__le__set__path__loss__reporting__parameters.md#a79a53ca3a481e013a5ee892d779e7bfd)

uint8\_t low\_threshold

**Definition** hci\_types.h:705

[bt\_hci\_cp\_le\_set\_path\_loss\_reporting\_parameters::high\_hysteresis](structbt__hci__cp__le__set__path__loss__reporting__parameters.md#ab5de762b7b82c8f453dafe1ea9bbf46d)

uint8\_t high\_hysteresis

**Definition** hci\_types.h:704

[bt\_hci\_cp\_le\_set\_path\_loss\_reporting\_parameters::high\_threshold](structbt__hci__cp__le__set__path__loss__reporting__parameters.md#ac8b7b832ba241c0448c80be22249b3ca)

uint8\_t high\_threshold

**Definition** hci\_types.h:703

[bt\_hci\_cp\_le\_set\_pawr\_response\_data](structbt__hci__cp__le__set__pawr__response__data.md)

**Definition** hci\_types.h:1744

[bt\_hci\_cp\_le\_set\_pawr\_response\_data::sync\_handle](structbt__hci__cp__le__set__pawr__response__data.md#a034afaaacf4b2168b9cd54cfde583b5c)

uint16\_t sync\_handle

**Definition** hci\_types.h:1745

[bt\_hci\_cp\_le\_set\_pawr\_response\_data::response\_data](structbt__hci__cp__le__set__pawr__response__data.md#a39cbc74ab95881b6dde8fa377d2951e5)

uint8\_t response\_data[0]

**Definition** hci\_types.h:1751

[bt\_hci\_cp\_le\_set\_pawr\_response\_data::response\_slot](structbt__hci__cp__le__set__pawr__response__data.md#a4356344510833196533bb9582f6fe18a)

uint8\_t response\_slot

**Definition** hci\_types.h:1749

[bt\_hci\_cp\_le\_set\_pawr\_response\_data::request\_subevent](structbt__hci__cp__le__set__pawr__response__data.md#a675a223891b28f06e78df6223439dc28)

uint8\_t request\_subevent

**Definition** hci\_types.h:1747

[bt\_hci\_cp\_le\_set\_pawr\_response\_data::response\_data\_length](structbt__hci__cp__le__set__pawr__response__data.md#a8c546fa3c6d969d44c54926330e5cf85)

uint8\_t response\_data\_length

**Definition** hci\_types.h:1750

[bt\_hci\_cp\_le\_set\_pawr\_response\_data::response\_subevent](structbt__hci__cp__le__set__pawr__response__data.md#aaf2e0eb3b491b5ccd15ba5259fd900c7)

uint8\_t response\_subevent

**Definition** hci\_types.h:1748

[bt\_hci\_cp\_le\_set\_pawr\_response\_data::request\_event](structbt__hci__cp__le__set__pawr__response__data.md#aaf5c337af93f13e243451b46a94ffb77)

uint16\_t request\_event

**Definition** hci\_types.h:1746

[bt\_hci\_cp\_le\_set\_pawr\_subevent\_data\_element](structbt__hci__cp__le__set__pawr__subevent__data__element.md)

**Definition** hci\_types.h:1728

[bt\_hci\_cp\_le\_set\_pawr\_subevent\_data\_element::response\_slot\_start](structbt__hci__cp__le__set__pawr__subevent__data__element.md#a90178bcd86c1bad0a768f391ce11613f)

uint8\_t response\_slot\_start

**Definition** hci\_types.h:1730

[bt\_hci\_cp\_le\_set\_pawr\_subevent\_data\_element::subevent\_data](structbt__hci__cp__le__set__pawr__subevent__data__element.md#a91c975189e409b733ac9a4af5763b12a)

uint8\_t subevent\_data[0]

**Definition** hci\_types.h:1733

[bt\_hci\_cp\_le\_set\_pawr\_subevent\_data\_element::subevent](structbt__hci__cp__le__set__pawr__subevent__data__element.md#abf33f93f0f1ddf3532c6cae13483ec1e)

uint8\_t subevent

**Definition** hci\_types.h:1729

[bt\_hci\_cp\_le\_set\_pawr\_subevent\_data\_element::subevent\_data\_length](structbt__hci__cp__le__set__pawr__subevent__data__element.md#ace5860dfa0f628eaed2b68b171d875da)

uint8\_t subevent\_data\_length

**Definition** hci\_types.h:1732

[bt\_hci\_cp\_le\_set\_pawr\_subevent\_data\_element::response\_slot\_count](structbt__hci__cp__le__set__pawr__subevent__data__element.md#ad8da1cc672eedf8be8cfc7d0d7ec1b41)

uint8\_t response\_slot\_count

**Definition** hci\_types.h:1731

[bt\_hci\_cp\_le\_set\_pawr\_subevent\_data](structbt__hci__cp__le__set__pawr__subevent__data.md)

**Definition** hci\_types.h:1736

[bt\_hci\_cp\_le\_set\_pawr\_subevent\_data::adv\_handle](structbt__hci__cp__le__set__pawr__subevent__data.md#a47d84125d15cce1fc969db3e5caa07e1)

uint8\_t adv\_handle

**Definition** hci\_types.h:1737

[bt\_hci\_cp\_le\_set\_pawr\_subevent\_data::num\_subevents](structbt__hci__cp__le__set__pawr__subevent__data.md#a9397eebd6771ad159d1bdae0d59e5f46)

uint8\_t num\_subevents

**Definition** hci\_types.h:1738

[bt\_hci\_cp\_le\_set\_pawr\_subevent\_data::subevents](structbt__hci__cp__le__set__pawr__subevent__data.md#aa932c1f19de96f89a79bbcb3ecbc1f5d)

struct bt\_hci\_cp\_le\_set\_pawr\_subevent\_data\_element subevents[0]

**Definition** hci\_types.h:1739

[bt\_hci\_cp\_le\_set\_pawr\_sync\_subevent](structbt__hci__cp__le__set__pawr__sync__subevent.md)

**Definition** hci\_types.h:1755

[bt\_hci\_cp\_le\_set\_pawr\_sync\_subevent::num\_subevents](structbt__hci__cp__le__set__pawr__sync__subevent.md#a2648ff50e0bad585e77e6f340836555a)

uint8\_t num\_subevents

**Definition** hci\_types.h:1758

[bt\_hci\_cp\_le\_set\_pawr\_sync\_subevent::sync\_handle](structbt__hci__cp__le__set__pawr__sync__subevent.md#a89f3092c2dd561e5469bb5bf57a06172)

uint16\_t sync\_handle

**Definition** hci\_types.h:1756

[bt\_hci\_cp\_le\_set\_pawr\_sync\_subevent::subevents](structbt__hci__cp__le__set__pawr__sync__subevent.md#a9a362ae841e5305b3985c4b2d88c6753)

uint8\_t subevents[0]

**Definition** hci\_types.h:1759

[bt\_hci\_cp\_le\_set\_pawr\_sync\_subevent::periodic\_adv\_properties](structbt__hci__cp__le__set__pawr__sync__subevent.md#aa73b23816e6c2c6546de15f6f6caff27)

uint16\_t periodic\_adv\_properties

**Definition** hci\_types.h:1757

[bt\_hci\_cp\_le\_set\_per\_adv\_data](structbt__hci__cp__le__set__per__adv__data.md)

**Definition** hci\_types.h:1651

[bt\_hci\_cp\_le\_set\_per\_adv\_data::handle](structbt__hci__cp__le__set__per__adv__data.md#a93cbb46ce6664880487e009a0b47af02)

uint8\_t handle

**Definition** hci\_types.h:1652

[bt\_hci\_cp\_le\_set\_per\_adv\_data::op](structbt__hci__cp__le__set__per__adv__data.md#aac34596f0970c976c4ef71250d326c2c)

uint8\_t op

**Definition** hci\_types.h:1653

[bt\_hci\_cp\_le\_set\_per\_adv\_data::data](structbt__hci__cp__le__set__per__adv__data.md#adaf581f8db6aafb4dc5df669df7ad26d)

uint8\_t data[0]

**Definition** hci\_types.h:1655

[bt\_hci\_cp\_le\_set\_per\_adv\_data::len](structbt__hci__cp__le__set__per__adv__data.md#ae6ee631a153cb6fed88695e599f63e91)

uint8\_t len

**Definition** hci\_types.h:1654

[bt\_hci\_cp\_le\_set\_per\_adv\_enable](structbt__hci__cp__le__set__per__adv__enable.md)

**Definition** hci\_types.h:1662

[bt\_hci\_cp\_le\_set\_per\_adv\_enable::handle](structbt__hci__cp__le__set__per__adv__enable.md#a998f4e38a56f771f234ce099b4528a3d)

uint8\_t handle

**Definition** hci\_types.h:1664

[bt\_hci\_cp\_le\_set\_per\_adv\_enable::enable](structbt__hci__cp__le__set__per__adv__enable.md#afff649b908264c617b249bcfbebadd53)

uint8\_t enable

**Definition** hci\_types.h:1663

[bt\_hci\_cp\_le\_set\_per\_adv\_param\_v2](structbt__hci__cp__le__set__per__adv__param__v2.md)

**Definition** hci\_types.h:1764

[bt\_hci\_cp\_le\_set\_per\_adv\_param\_v2::num\_response\_slots](structbt__hci__cp__le__set__per__adv__param__v2.md#a2483eb4457f9dc22ff8473175662e260)

uint8\_t num\_response\_slots

**Definition** hci\_types.h:1773

[bt\_hci\_cp\_le\_set\_per\_adv\_param\_v2::response\_slot\_spacing](structbt__hci__cp__le__set__per__adv__param__v2.md#a35fcc697e60d3c398f03be7503f611bd)

uint8\_t response\_slot\_spacing

**Definition** hci\_types.h:1772

[bt\_hci\_cp\_le\_set\_per\_adv\_param\_v2::subevent\_interval](structbt__hci__cp__le__set__per__adv__param__v2.md#a79dfc3b13068d9c51f0a756f025aaeba)

uint8\_t subevent\_interval

**Definition** hci\_types.h:1770

[bt\_hci\_cp\_le\_set\_per\_adv\_param\_v2::num\_subevents](structbt__hci__cp__le__set__per__adv__param__v2.md#a7bea764aa5d21e03946804566b1f9869)

uint8\_t num\_subevents

**Definition** hci\_types.h:1769

[bt\_hci\_cp\_le\_set\_per\_adv\_param\_v2::max\_interval](structbt__hci__cp__le__set__per__adv__param__v2.md#acc9718286ab0847a3444d3fc2d3c93bc)

uint16\_t max\_interval

**Definition** hci\_types.h:1767

[bt\_hci\_cp\_le\_set\_per\_adv\_param\_v2::response\_slot\_delay](structbt__hci__cp__le__set__per__adv__param__v2.md#acdeb503c0a13291158ad389c9f6ac206)

uint8\_t response\_slot\_delay

**Definition** hci\_types.h:1771

[bt\_hci\_cp\_le\_set\_per\_adv\_param\_v2::props](structbt__hci__cp__le__set__per__adv__param__v2.md#ad2d658bb0be35aee6b5c133fece89068)

uint16\_t props

**Definition** hci\_types.h:1768

[bt\_hci\_cp\_le\_set\_per\_adv\_param\_v2::min\_interval](structbt__hci__cp__le__set__per__adv__param__v2.md#ae36e28210a515f73648e6f8b3984fb55)

uint16\_t min\_interval

**Definition** hci\_types.h:1766

[bt\_hci\_cp\_le\_set\_per\_adv\_param\_v2::handle](structbt__hci__cp__le__set__per__adv__param__v2.md#aee1088b46914c8e26d9e97ce573291c6)

uint8\_t handle

**Definition** hci\_types.h:1765

[bt\_hci\_cp\_le\_set\_per\_adv\_param](structbt__hci__cp__le__set__per__adv__param.md)

**Definition** hci\_types.h:1636

[bt\_hci\_cp\_le\_set\_per\_adv\_param::max\_interval](structbt__hci__cp__le__set__per__adv__param.md#a1a2a69ea6e310710892184ced472eb8a)

uint16\_t max\_interval

**Definition** hci\_types.h:1639

[bt\_hci\_cp\_le\_set\_per\_adv\_param::handle](structbt__hci__cp__le__set__per__adv__param.md#a2b61031952b3893add7677d3802e368b)

uint8\_t handle

**Definition** hci\_types.h:1637

[bt\_hci\_cp\_le\_set\_per\_adv\_param::props](structbt__hci__cp__le__set__per__adv__param.md#a879ea10e1ab217b4aa49dfcf3b394691)

uint16\_t props

**Definition** hci\_types.h:1640

[bt\_hci\_cp\_le\_set\_per\_adv\_param::min\_interval](structbt__hci__cp__le__set__per__adv__param.md#af01696ef6bf02e7db37d45a0c9852ef5)

uint16\_t min\_interval

**Definition** hci\_types.h:1638

[bt\_hci\_cp\_le\_set\_per\_adv\_recv\_enable](structbt__hci__cp__le__set__per__adv__recv__enable.md)

**Definition** hci\_types.h:2028

[bt\_hci\_cp\_le\_set\_per\_adv\_recv\_enable::handle](structbt__hci__cp__le__set__per__adv__recv__enable.md#a1e626eecf1d3f0820c3b2a13fd84b92f)

uint16\_t handle

**Definition** hci\_types.h:2029

[bt\_hci\_cp\_le\_set\_per\_adv\_recv\_enable::enable](structbt__hci__cp__le__set__per__adv__recv__enable.md#a2187ec96822726daa5e43e910cc41cc3)

uint8\_t enable

**Definition** hci\_types.h:2030

[bt\_hci\_cp\_le\_set\_phy](structbt__hci__cp__le__set__phy.md)

**Definition** hci\_types.h:1464

[bt\_hci\_cp\_le\_set\_phy::tx\_phys](structbt__hci__cp__le__set__phy.md#a06880062ff486b532ebeb789adb57d1e)

uint8\_t tx\_phys

**Definition** hci\_types.h:1467

[bt\_hci\_cp\_le\_set\_phy::phy\_opts](structbt__hci__cp__le__set__phy.md#a458ab90f83b60fafa66167f474c0800d)

uint16\_t phy\_opts

**Definition** hci\_types.h:1469

[bt\_hci\_cp\_le\_set\_phy::rx\_phys](structbt__hci__cp__le__set__phy.md#ab30eb68920a0578b16794250e592b12a)

uint8\_t rx\_phys

**Definition** hci\_types.h:1468

[bt\_hci\_cp\_le\_set\_phy::handle](structbt__hci__cp__le__set__phy.md#ad0759eea02017674459d4ce0af0e526e)

uint16\_t handle

**Definition** hci\_types.h:1465

[bt\_hci\_cp\_le\_set\_phy::all\_phys](structbt__hci__cp__le__set__phy.md#afb8d056dc7d8824eec0ef16fdf9ce924)

uint8\_t all\_phys

**Definition** hci\_types.h:1466

[bt\_hci\_cp\_le\_set\_privacy\_mode](structbt__hci__cp__le__set__privacy__mode.md)

**Definition** hci\_types.h:1853

[bt\_hci\_cp\_le\_set\_privacy\_mode::id\_addr](structbt__hci__cp__le__set__privacy__mode.md#a404cc9f04cd11924445f12eb4471ef2e)

bt\_addr\_le\_t id\_addr

**Definition** hci\_types.h:1854

[bt\_hci\_cp\_le\_set\_privacy\_mode::mode](structbt__hci__cp__le__set__privacy__mode.md#a8ca00418b0638bba6ef586d6cbf253a5)

uint8\_t mode

**Definition** hci\_types.h:1855

[bt\_hci\_cp\_le\_set\_procedure\_parameters](structbt__hci__cp__le__set__procedure__parameters.md)

**Definition** hci\_types.h:2545

[bt\_hci\_cp\_le\_set\_procedure\_parameters::min\_procedure\_interval](structbt__hci__cp__le__set__procedure__parameters.md#a22ecbaff0fd48a0716a15d265adc590e)

uint16\_t min\_procedure\_interval

**Definition** hci\_types.h:2549

[bt\_hci\_cp\_le\_set\_procedure\_parameters::min\_subevent\_len](structbt__hci__cp__le__set__procedure__parameters.md#a51fb8c789cefce09d5da2b86d5c862ce)

uint8\_t min\_subevent\_len[3]

**Definition** hci\_types.h:2552

[bt\_hci\_cp\_le\_set\_procedure\_parameters::max\_procedure\_len](structbt__hci__cp__le__set__procedure__parameters.md#a5de9205fdf1b6e342f53a12aa82c10c5)

uint16\_t max\_procedure\_len

**Definition** hci\_types.h:2548

[bt\_hci\_cp\_le\_set\_procedure\_parameters::preferred\_peer\_antenna](structbt__hci__cp__le__set__procedure__parameters.md#a7a61ff539f68a02ea7aa466f182dc5ab)

uint8\_t preferred\_peer\_antenna

**Definition** hci\_types.h:2557

[bt\_hci\_cp\_le\_set\_procedure\_parameters::config\_id](structbt__hci__cp__le__set__procedure__parameters.md#a7d2f5d9242df436906b005e66c7bb75d)

uint8\_t config\_id

**Definition** hci\_types.h:2547

[bt\_hci\_cp\_le\_set\_procedure\_parameters::snr\_control\_initiator](structbt__hci__cp__le__set__procedure__parameters.md#a8524fd01e35094d2b78488c0a2876832)

uint8\_t snr\_control\_initiator

**Definition** hci\_types.h:2558

[bt\_hci\_cp\_le\_set\_procedure\_parameters::snr\_control\_reflector](structbt__hci__cp__le__set__procedure__parameters.md#aa5a6a677b6e0d57658041e891535d74b)

uint8\_t snr\_control\_reflector

**Definition** hci\_types.h:2559

[bt\_hci\_cp\_le\_set\_procedure\_parameters::tone\_antenna\_config\_selection](structbt__hci__cp__le__set__procedure__parameters.md#aa783e0e63c38ceee503c0b73ac873ca7)

uint8\_t tone\_antenna\_config\_selection

**Definition** hci\_types.h:2554

[bt\_hci\_cp\_le\_set\_procedure\_parameters::max\_subevent\_len](structbt__hci__cp__le__set__procedure__parameters.md#aa9ec99aff85de173ccb2d3f144c85319)

uint8\_t max\_subevent\_len[3]

**Definition** hci\_types.h:2553

[bt\_hci\_cp\_le\_set\_procedure\_parameters::handle](structbt__hci__cp__le__set__procedure__parameters.md#ab8a15269255fb7d960ae712a844b9f35)

uint16\_t handle

**Definition** hci\_types.h:2546

[bt\_hci\_cp\_le\_set\_procedure\_parameters::max\_procedure\_count](structbt__hci__cp__le__set__procedure__parameters.md#ac6bb66fa24aec17a964f27365ca65ec9)

uint16\_t max\_procedure\_count

**Definition** hci\_types.h:2551

[bt\_hci\_cp\_le\_set\_procedure\_parameters::max\_procedure\_interval](structbt__hci__cp__le__set__procedure__parameters.md#ad46165bc5f6d875940ee53a8b98cb5b4)

uint16\_t max\_procedure\_interval

**Definition** hci\_types.h:2550

[bt\_hci\_cp\_le\_set\_procedure\_parameters::tx\_power\_delta](structbt__hci__cp__le__set__procedure__parameters.md#ade09ca9d42b0db682cf677d9ac4326d2)

uint8\_t tx\_power\_delta

**Definition** hci\_types.h:2556

[bt\_hci\_cp\_le\_set\_procedure\_parameters::phy](structbt__hci__cp__le__set__procedure__parameters.md#afcd4e8b390fd996ee134043ec2930fe8)

uint8\_t phy

**Definition** hci\_types.h:2555

[bt\_hci\_cp\_le\_set\_random\_address](structbt__hci__cp__le__set__random__address.md)

**Definition** hci\_types.h:1052

[bt\_hci\_cp\_le\_set\_random\_address::bdaddr](structbt__hci__cp__le__set__random__address.md#a919ef74473f4f86d00595ec8606789d0)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:1053

[bt\_hci\_cp\_le\_set\_rpa\_timeout](structbt__hci__cp__le__set__rpa__timeout.md)

**Definition** hci\_types.h:1406

[bt\_hci\_cp\_le\_set\_rpa\_timeout::rpa\_timeout](structbt__hci__cp__le__set__rpa__timeout.md#a6b1befe9d2131a889de17339ec1941fa)

uint16\_t rpa\_timeout

**Definition** hci\_types.h:1407

[bt\_hci\_cp\_le\_set\_scan\_enable](structbt__hci__cp__le__set__scan__enable.md)

**Definition** hci\_types.h:1140

[bt\_hci\_cp\_le\_set\_scan\_enable::enable](structbt__hci__cp__le__set__scan__enable.md#a5e429a0b11be1493515803a360932b06)

uint8\_t enable

**Definition** hci\_types.h:1141

[bt\_hci\_cp\_le\_set\_scan\_enable::filter\_dup](structbt__hci__cp__le__set__scan__enable.md#a77b0f05c0e76681ed633bd42b3f21811)

uint8\_t filter\_dup

**Definition** hci\_types.h:1142

[bt\_hci\_cp\_le\_set\_scan\_param](structbt__hci__cp__le__set__scan__param.md)

**Definition** hci\_types.h:1124

[bt\_hci\_cp\_le\_set\_scan\_param::window](structbt__hci__cp__le__set__scan__param.md#a3b5b4767092fc69a63d2219d60722407)

uint16\_t window

**Definition** hci\_types.h:1127

[bt\_hci\_cp\_le\_set\_scan\_param::addr\_type](structbt__hci__cp__le__set__scan__param.md#a694c74a6fc95f767d2e89e6596d51e98)

uint8\_t addr\_type

**Definition** hci\_types.h:1128

[bt\_hci\_cp\_le\_set\_scan\_param::filter\_policy](structbt__hci__cp__le__set__scan__param.md#ab7a268e17a5d564d475ff9dee5e6e14b)

uint8\_t filter\_policy

**Definition** hci\_types.h:1129

[bt\_hci\_cp\_le\_set\_scan\_param::scan\_type](structbt__hci__cp__le__set__scan__param.md#ad19a479cc3c27ab24286b537b646261e)

uint8\_t scan\_type

**Definition** hci\_types.h:1125

[bt\_hci\_cp\_le\_set\_scan\_param::interval](structbt__hci__cp__le__set__scan__param.md#adcd8be074a8b19e0e7d02c4ea8209c93)

uint16\_t interval

**Definition** hci\_types.h:1126

[bt\_hci\_cp\_le\_set\_scan\_rsp\_data](structbt__hci__cp__le__set__scan__rsp__data.md)

**Definition** hci\_types.h:1101

[bt\_hci\_cp\_le\_set\_scan\_rsp\_data::len](structbt__hci__cp__le__set__scan__rsp__data.md#a0fe51008184419c9560bb5d8f287d8be)

uint8\_t len

**Definition** hci\_types.h:1102

[bt\_hci\_cp\_le\_set\_scan\_rsp\_data::data](structbt__hci__cp__le__set__scan__rsp__data.md#aa719449dc2b85f094081d66398b72c7d)

uint8\_t data[31]

**Definition** hci\_types.h:1103

[bt\_hci\_cp\_le\_set\_tx\_power\_report\_enable](structbt__hci__cp__le__set__tx__power__report__enable.md)

**Definition** hci\_types.h:695

[bt\_hci\_cp\_le\_set\_tx\_power\_report\_enable::local\_enable](structbt__hci__cp__le__set__tx__power__report__enable.md#a30580470d1ba516d86c8b157ca415ef3)

uint8\_t local\_enable

**Definition** hci\_types.h:697

[bt\_hci\_cp\_le\_set\_tx\_power\_report\_enable::handle](structbt__hci__cp__le__set__tx__power__report__enable.md#a4a37c87f8f6a966a90c5de09096d1356)

uint16\_t handle

**Definition** hci\_types.h:696

[bt\_hci\_cp\_le\_set\_tx\_power\_report\_enable::remote\_enable](structbt__hci__cp__le__set__tx__power__report__enable.md#ab4e8fb4fd7a1fbbc8b5736f8a6f65c5e)

uint8\_t remote\_enable

**Definition** hci\_types.h:698

[bt\_hci\_cp\_le\_setup\_iso\_path](structbt__hci__cp__le__setup__iso__path.md)

**Definition** hci\_types.h:2304

[bt\_hci\_cp\_le\_setup\_iso\_path::handle](structbt__hci__cp__le__setup__iso__path.md#a0054fede0e583cef0dbcf6ef3134e480)

uint16\_t handle

**Definition** hci\_types.h:2305

[bt\_hci\_cp\_le\_setup\_iso\_path::codec\_config\_len](structbt__hci__cp__le__setup__iso__path.md#a1a816d8e8c434a05ea897b74bc4d89c7)

uint8\_t codec\_config\_len

**Definition** hci\_types.h:2310

[bt\_hci\_cp\_le\_setup\_iso\_path::controller\_delay](structbt__hci__cp__le__setup__iso__path.md#a31948436e6608f9943d34ce89a65c64c)

uint8\_t controller\_delay[3]

**Definition** hci\_types.h:2309

[bt\_hci\_cp\_le\_setup\_iso\_path::codec\_id](structbt__hci__cp__le__setup__iso__path.md#a5256fc99b362e3a5f986ef2b71b29ccb)

struct bt\_hci\_cp\_codec\_id codec\_id

**Definition** hci\_types.h:2308

[bt\_hci\_cp\_le\_setup\_iso\_path::path\_id](structbt__hci__cp__le__setup__iso__path.md#a7c07d69b2005af1f7f2618f2bfa60d50)

uint8\_t path\_id

**Definition** hci\_types.h:2307

[bt\_hci\_cp\_le\_setup\_iso\_path::path\_dir](structbt__hci__cp__le__setup__iso__path.md#a89c1324359a4fc2f10fee9ebbac5cf2b)

uint8\_t path\_dir

**Definition** hci\_types.h:2306

[bt\_hci\_cp\_le\_setup\_iso\_path::codec\_config](structbt__hci__cp__le__setup__iso__path.md#ade4dee947e3d288f769d2d69fc57f96a)

uint8\_t codec\_config[0]

**Definition** hci\_types.h:2311

[bt\_hci\_cp\_le\_start\_encryption](structbt__hci__cp__le__start__encryption.md)

**Definition** hci\_types.h:1232

[bt\_hci\_cp\_le\_start\_encryption::handle](structbt__hci__cp__le__start__encryption.md#a4ac6d63f336e36a347242153aced4c71)

uint16\_t handle

**Definition** hci\_types.h:1233

[bt\_hci\_cp\_le\_start\_encryption::ediv](structbt__hci__cp__le__start__encryption.md#a640d201bbfa6f6d8476be02d3656e847)

uint16\_t ediv

**Definition** hci\_types.h:1235

[bt\_hci\_cp\_le\_start\_encryption::ltk](structbt__hci__cp__le__start__encryption.md#a99d2dd719ce38976e9da8a73f26839a1)

uint8\_t ltk[16]

**Definition** hci\_types.h:1236

[bt\_hci\_cp\_le\_start\_encryption::rand](structbt__hci__cp__le__start__encryption.md#ade8ae824dc5d85671971a3baafee8f54)

uint64\_t rand

**Definition** hci\_types.h:1234

[bt\_hci\_cp\_le\_subrate\_request](structbt__hci__cp__le__subrate__request.md)

**Definition** hci\_types.h:729

[bt\_hci\_cp\_le\_subrate\_request::max\_latency](structbt__hci__cp__le__subrate__request.md#a04ccc83303baabf30b663983883e7e77)

uint16\_t max\_latency

**Definition** hci\_types.h:733

[bt\_hci\_cp\_le\_subrate\_request::subrate\_min](structbt__hci__cp__le__subrate__request.md#a18ba526d8a843ad9c74c22d0899d9c1f)

uint16\_t subrate\_min

**Definition** hci\_types.h:731

[bt\_hci\_cp\_le\_subrate\_request::handle](structbt__hci__cp__le__subrate__request.md#a2595419182358e3386a0fb6e523a3dda)

uint16\_t handle

**Definition** hci\_types.h:730

[bt\_hci\_cp\_le\_subrate\_request::subrate\_max](structbt__hci__cp__le__subrate__request.md#a5c95a2bea462fb72d34d6314046041b7)

uint16\_t subrate\_max

**Definition** hci\_types.h:732

[bt\_hci\_cp\_le\_subrate\_request::supervision\_timeout](structbt__hci__cp__le__subrate__request.md#a60bcbe27605063725422a0b1c35f21e7)

uint16\_t supervision\_timeout

**Definition** hci\_types.h:735

[bt\_hci\_cp\_le\_subrate\_request::continuation\_number](structbt__hci__cp__le__subrate__request.md#ab32a92ed52266c6b7d6d9ab08787e770)

uint16\_t continuation\_number

**Definition** hci\_types.h:734

[bt\_hci\_cp\_le\_terminate\_big](structbt__hci__cp__le__terminate__big.md)

**Definition** hci\_types.h:2271

[bt\_hci\_cp\_le\_terminate\_big::reason](structbt__hci__cp__le__terminate__big.md#a958ab6b2f2bb30c825060498e6917a18)

uint8\_t reason

**Definition** hci\_types.h:2273

[bt\_hci\_cp\_le\_terminate\_big::big\_handle](structbt__hci__cp__le__terminate__big.md#acb5fb9451cf890245a85704579b1d1c8)

uint8\_t big\_handle

**Definition** hci\_types.h:2272

[bt\_hci\_cp\_le\_tx\_test\_v3](structbt__hci__cp__le__tx__test__v3.md)

**Definition** hci\_types.h:1877

[bt\_hci\_cp\_le\_tx\_test\_v3::test\_data\_len](structbt__hci__cp__le__tx__test__v3.md#a1c0828e51bb6c24e9dd1f12b5badcfea)

uint8\_t test\_data\_len

**Definition** hci\_types.h:1879

[bt\_hci\_cp\_le\_tx\_test\_v3::switch\_pattern\_len](structbt__hci__cp__le__tx__test__v3.md#a459b850f35c61bf7f53d3730245cb4bb)

uint8\_t switch\_pattern\_len

**Definition** hci\_types.h:1884

[bt\_hci\_cp\_le\_tx\_test\_v3::cte\_len](structbt__hci__cp__le__tx__test__v3.md#a52d2d6dcc188d5f02904e0e56f461841)

uint8\_t cte\_len

**Definition** hci\_types.h:1882

[bt\_hci\_cp\_le\_tx\_test\_v3::tx\_ch](structbt__hci__cp__le__tx__test__v3.md#a6486882bc375f229a88bbfa53be49670)

uint8\_t tx\_ch

**Definition** hci\_types.h:1878

[bt\_hci\_cp\_le\_tx\_test\_v3::phy](structbt__hci__cp__le__tx__test__v3.md#a712a30d9d6afc7d302041e1de6721de4)

uint8\_t phy

**Definition** hci\_types.h:1881

[bt\_hci\_cp\_le\_tx\_test\_v3::pkt\_payload](structbt__hci__cp__le__tx__test__v3.md#ad8f2d2ca3ad3be28c0aec9e8a0e1bc61)

uint8\_t pkt\_payload

**Definition** hci\_types.h:1880

[bt\_hci\_cp\_le\_tx\_test\_v3::cte\_type](structbt__hci__cp__le__tx__test__v3.md#adf6b1653902fb13cc1ccc32cd91c990f)

uint8\_t cte\_type

**Definition** hci\_types.h:1883

[bt\_hci\_cp\_le\_tx\_test\_v3::ant\_ids](structbt__hci__cp__le__tx__test__v3.md#afdb6dd44108e9a4a21ac31a74c1e083f)

uint8\_t ant\_ids[0]

**Definition** hci\_types.h:1885

[bt\_hci\_cp\_le\_tx\_test\_v4\_tx\_power](structbt__hci__cp__le__tx__test__v4__tx__power.md)

**Definition** hci\_types.h:2432

[bt\_hci\_cp\_le\_tx\_test\_v4\_tx\_power::tx\_power](structbt__hci__cp__le__tx__test__v4__tx__power.md#a2a8b1c31787066ad2b471aec5c261085)

int8\_t tx\_power

**Definition** hci\_types.h:2433

[bt\_hci\_cp\_le\_tx\_test\_v4](structbt__hci__cp__le__tx__test__v4.md)

**Definition** hci\_types.h:2411

[bt\_hci\_cp\_le\_tx\_test\_v4::switch\_pattern\_len](structbt__hci__cp__le__tx__test__v4.md#a2039a87b5f32c4a45b8f858808df7cdc)

uint8\_t switch\_pattern\_len

**Definition** hci\_types.h:2418

[bt\_hci\_cp\_le\_tx\_test\_v4::tx\_ch](structbt__hci__cp__le__tx__test__v4.md#a3ccae40f09b2763b2b07dc16982f3973)

uint8\_t tx\_ch

**Definition** hci\_types.h:2412

[bt\_hci\_cp\_le\_tx\_test\_v4::ant\_ids](structbt__hci__cp__le__tx__test__v4.md#a3fe8ab7c0ee389dce8592cb7a38bc42c)

uint8\_t ant\_ids[0]

**Definition** hci\_types.h:2419

[bt\_hci\_cp\_le\_tx\_test\_v4::phy](structbt__hci__cp__le__tx__test__v4.md#a5db011159fe75f4522e03ea1efdc57bd)

uint8\_t phy

**Definition** hci\_types.h:2415

[bt\_hci\_cp\_le\_tx\_test\_v4::test\_data\_len](structbt__hci__cp__le__tx__test__v4.md#a7a8e2610fb8903ccfb6e4b08017f6112)

uint8\_t test\_data\_len

**Definition** hci\_types.h:2413

[bt\_hci\_cp\_le\_tx\_test\_v4::cte\_len](structbt__hci__cp__le__tx__test__v4.md#a8dea923a63e787de3bfe07611eb7a1ed)

uint8\_t cte\_len

**Definition** hci\_types.h:2416

[bt\_hci\_cp\_le\_tx\_test\_v4::pkt\_payload](structbt__hci__cp__le__tx__test__v4.md#abdd393eb264f04acf65e2dce4bd65ac0)

uint8\_t pkt\_payload

**Definition** hci\_types.h:2414

[bt\_hci\_cp\_le\_tx\_test\_v4::cte\_type](structbt__hci__cp__le__tx__test__v4.md#ae950f71a3fcfca0cf738bc28693256cf)

uint8\_t cte\_type

**Definition** hci\_types.h:2417

[bt\_hci\_cp\_le\_tx\_test](structbt__hci__cp__le__tx__test.md)

**Definition** hci\_types.h:1279

[bt\_hci\_cp\_le\_tx\_test::test\_data\_len](structbt__hci__cp__le__tx__test.md#a55c5f1621a51da03500910fc9664df54)

uint8\_t test\_data\_len

**Definition** hci\_types.h:1281

[bt\_hci\_cp\_le\_tx\_test::tx\_ch](structbt__hci__cp__le__tx__test.md#aae634b277125066ecbc36d119bc4244f)

uint8\_t tx\_ch

**Definition** hci\_types.h:1280

[bt\_hci\_cp\_le\_tx\_test::pkt\_payload](structbt__hci__cp__le__tx__test.md#ad93908905d370842f16e16cc45280495)

uint8\_t pkt\_payload

**Definition** hci\_types.h:1282

[bt\_hci\_cp\_le\_write\_cached\_remote\_fae\_table](structbt__hci__cp__le__write__cached__remote__fae__table.md)

**Definition** hci\_types.h:2531

[bt\_hci\_cp\_le\_write\_cached\_remote\_fae\_table::handle](structbt__hci__cp__le__write__cached__remote__fae__table.md#a330531f1809cddea8f1527f3b0a92e31)

uint16\_t handle

**Definition** hci\_types.h:2532

[bt\_hci\_cp\_le\_write\_cached\_remote\_fae\_table::remote\_fae\_table](structbt__hci__cp__le__write__cached__remote__fae__table.md#a8594dd89888d1388f2a45a33e12e94d0)

int8\_t remote\_fae\_table[72]

**Definition** hci\_types.h:2533

[bt\_hci\_cp\_le\_write\_cached\_remote\_supported\_capabilities](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md)

**Definition** hci\_types.h:2471

[bt\_hci\_cp\_le\_write\_cached\_remote\_supported\_capabilities::t\_ip2\_times\_supported](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a0911e19deceb7f243ac706ddb4cf0a3a)

uint16\_t t\_ip2\_times\_supported

**Definition** hci\_types.h:2488

[bt\_hci\_cp\_le\_write\_cached\_remote\_supported\_capabilities::t\_ip1\_times\_supported](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a257b38d937c1111a66f6c28f1e221211)

uint16\_t t\_ip1\_times\_supported

**Definition** hci\_types.h:2487

[bt\_hci\_cp\_le\_write\_cached\_remote\_supported\_capabilities::nadm\_random\_capability](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a25faaf2be6db05c44256b9f559841c87)

uint16\_t nadm\_random\_capability

**Definition** hci\_types.h:2484

[bt\_hci\_cp\_le\_write\_cached\_remote\_supported\_capabilities::nadm\_sounding\_capability](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a29781bbe7e25c39b06047725f1d11426)

uint16\_t nadm\_sounding\_capability

**Definition** hci\_types.h:2483

[bt\_hci\_cp\_le\_write\_cached\_remote\_supported\_capabilities::subfeatures\_supported](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a2b5c828a30525eee5b1ce48f3ba98896)

uint16\_t subfeatures\_supported

**Definition** hci\_types.h:2486

[bt\_hci\_cp\_le\_write\_cached\_remote\_supported\_capabilities::rtt\_sounding\_n](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a31c877363bd315786ef834215614d346)

uint8\_t rtt\_sounding\_n

**Definition** hci\_types.h:2481

[bt\_hci\_cp\_le\_write\_cached\_remote\_supported\_capabilities::num\_config\_supported](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a7a60c326707ebd60b96d25924e3c9e40)

uint8\_t num\_config\_supported

**Definition** hci\_types.h:2473

[bt\_hci\_cp\_le\_write\_cached\_remote\_supported\_capabilities::t\_pm\_times\_supported](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a870e068fcc15dd44dca3ac24334000ee)

uint16\_t t\_pm\_times\_supported

**Definition** hci\_types.h:2490

[bt\_hci\_cp\_le\_write\_cached\_remote\_supported\_capabilities::handle](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a8a884bca80550eb72a433f5ea280f702)

uint16\_t handle

**Definition** hci\_types.h:2472

[bt\_hci\_cp\_le\_write\_cached\_remote\_supported\_capabilities::rtt\_random\_payload\_n](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a8f98235e9238a80602806fb60e1261bb)

uint8\_t rtt\_random\_payload\_n

**Definition** hci\_types.h:2482

[bt\_hci\_cp\_le\_write\_cached\_remote\_supported\_capabilities::cs\_sync\_phys\_supported](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a908322e5c02500abbdd8891c5248998d)

uint8\_t cs\_sync\_phys\_supported

**Definition** hci\_types.h:2485

[bt\_hci\_cp\_le\_write\_cached\_remote\_supported\_capabilities::modes\_supported](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a93f4973a1229273c51f6a20e741e42ed)

uint8\_t modes\_supported

**Definition** hci\_types.h:2478

[bt\_hci\_cp\_le\_write\_cached\_remote\_supported\_capabilities::rtt\_capability](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a94fb0f963f706c303729d7a0088ef617)

uint8\_t rtt\_capability

**Definition** hci\_types.h:2479

[bt\_hci\_cp\_le\_write\_cached\_remote\_supported\_capabilities::max\_antenna\_paths\_supported](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a96a49382bef8f3163cd82899f59ed5fe)

uint8\_t max\_antenna\_paths\_supported

**Definition** hci\_types.h:2476

[bt\_hci\_cp\_le\_write\_cached\_remote\_supported\_capabilities::num\_antennas\_supported](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#a96b0c7868da711271e74b82fcfd32fc2)

uint8\_t num\_antennas\_supported

**Definition** hci\_types.h:2475

[bt\_hci\_cp\_le\_write\_cached\_remote\_supported\_capabilities::tx\_snr\_capability](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#aa9e48c6f0d22e9a64e8591a34409988e)

uint8\_t tx\_snr\_capability

**Definition** hci\_types.h:2492

[bt\_hci\_cp\_le\_write\_cached\_remote\_supported\_capabilities::t\_sw\_time\_supported](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#ab77f7bda7302cad94805e8ea43b8bf14)

uint8\_t t\_sw\_time\_supported

**Definition** hci\_types.h:2491

[bt\_hci\_cp\_le\_write\_cached\_remote\_supported\_capabilities::rtt\_aa\_only\_n](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#ae4b9b8ba0e83978f131541959062f691)

uint8\_t rtt\_aa\_only\_n

**Definition** hci\_types.h:2480

[bt\_hci\_cp\_le\_write\_cached\_remote\_supported\_capabilities::roles\_supported](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#ae88cf07e3c8e6ad64a1beb60270d8961)

uint8\_t roles\_supported

**Definition** hci\_types.h:2477

[bt\_hci\_cp\_le\_write\_cached\_remote\_supported\_capabilities::t\_fcs\_times\_supported](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#af959f1539f5bbf74b0e63db743a132f4)

uint16\_t t\_fcs\_times\_supported

**Definition** hci\_types.h:2489

[bt\_hci\_cp\_le\_write\_cached\_remote\_supported\_capabilities::max\_consecutive\_procedures\_supported](structbt__hci__cp__le__write__cached__remote__supported__capabilities.md#afbfe48ddad696315d6e021a85d32559d)

uint16\_t max\_consecutive\_procedures\_supported

**Definition** hci\_types.h:2474

[bt\_hci\_cp\_le\_write\_default\_data\_len](structbt__hci__cp__le__write__default__data__len.md)

**Definition** hci\_types.h:1335

[bt\_hci\_cp\_le\_write\_default\_data\_len::max\_tx\_octets](structbt__hci__cp__le__write__default__data__len.md#a0ffb8c52d9031dfe448eac0943a4a49c)

uint16\_t max\_tx\_octets

**Definition** hci\_types.h:1336

[bt\_hci\_cp\_le\_write\_default\_data\_len::max\_tx\_time](structbt__hci__cp__le__write__default__data__len.md#a2ada0ea5ee8ac8e6d59fc6adc18421b8)

uint16\_t max\_tx\_time

**Definition** hci\_types.h:1337

[bt\_hci\_cp\_le\_write\_rf\_path\_comp](structbt__hci__cp__le__write__rf__path__comp.md)

**Definition** hci\_types.h:1844

[bt\_hci\_cp\_le\_write\_rf\_path\_comp::rx\_path\_comp](structbt__hci__cp__le__write__rf__path__comp.md#a11aad5607e444cf55dd5878f1f6f9436)

int16\_t rx\_path\_comp

**Definition** hci\_types.h:1846

[bt\_hci\_cp\_le\_write\_rf\_path\_comp::tx\_path\_comp](structbt__hci__cp__le__write__rf__path__comp.md#a5f99b131f3fba91706bdc8277c1abba1)

int16\_t tx\_path\_comp

**Definition** hci\_types.h:1845

[bt\_hci\_cp\_link\_key\_neg\_reply](structbt__hci__cp__link__key__neg__reply.md)

**Definition** hci\_types.h:456

[bt\_hci\_cp\_link\_key\_neg\_reply::bdaddr](structbt__hci__cp__link__key__neg__reply.md#aca3114707eb7c631af582626551619cd)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:457

[bt\_hci\_cp\_link\_key\_reply](structbt__hci__cp__link__key__reply.md)

**Definition** hci\_types.h:450

[bt\_hci\_cp\_link\_key\_reply::link\_key](structbt__hci__cp__link__key__reply.md#a2af0b4b55a5ffcff0221da841ba0cbba)

uint8\_t link\_key[16]

**Definition** hci\_types.h:452

[bt\_hci\_cp\_link\_key\_reply::bdaddr](structbt__hci__cp__link__key__reply.md#ab5221952fbcfe413d7c3bd3a441a9b17)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:451

[bt\_hci\_cp\_pin\_code\_neg\_reply](structbt__hci__cp__pin__code__neg__reply.md)

**Definition** hci\_types.h:472

[bt\_hci\_cp\_pin\_code\_neg\_reply::bdaddr](structbt__hci__cp__pin__code__neg__reply.md#a8aec3ba6c530850dce0a2d7b7f7f86ee)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:473

[bt\_hci\_cp\_pin\_code\_reply](structbt__hci__cp__pin__code__reply.md)

**Definition** hci\_types.h:461

[bt\_hci\_cp\_pin\_code\_reply::bdaddr](structbt__hci__cp__pin__code__reply.md#a627800dcb580110be785576dfcc49bb1)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:462

[bt\_hci\_cp\_pin\_code\_reply::pin\_len](structbt__hci__cp__pin__code__reply.md#aa0cbf668608c3eb4998356ad7b18c01a)

uint8\_t pin\_len

**Definition** hci\_types.h:463

[bt\_hci\_cp\_pin\_code\_reply::pin\_code](structbt__hci__cp__pin__code__reply.md#afc4ed5ae429087f4692af716d6b56997)

uint8\_t pin\_code[16]

**Definition** hci\_types.h:464

[bt\_hci\_cp\_read\_auth\_payload\_timeout](structbt__hci__cp__read__auth__payload__timeout.md)

**Definition** hci\_types.h:794

[bt\_hci\_cp\_read\_auth\_payload\_timeout::handle](structbt__hci__cp__read__auth__payload__timeout.md#adcdd657feb3ea6b892e2a5034365dd77)

uint16\_t handle

**Definition** hci\_types.h:795

[bt\_hci\_cp\_read\_codec\_capabilities](structbt__hci__cp__read__codec__capabilities.md)

**Definition** hci\_types.h:978

[bt\_hci\_cp\_read\_codec\_capabilities::direction](structbt__hci__cp__read__codec__capabilities.md#a237695f4d0a1359d5ce71d831708a69c)

uint8\_t direction

**Definition** hci\_types.h:981

[bt\_hci\_cp\_read\_codec\_capabilities::transport](structbt__hci__cp__read__codec__capabilities.md#a6479561573172356d7515ef92f75b8d4)

uint8\_t transport

**Definition** hci\_types.h:980

[bt\_hci\_cp\_read\_codec\_capabilities::codec\_id](structbt__hci__cp__read__codec__capabilities.md#ad48b7f228742d86a71dffa314331bbe1)

struct bt\_hci\_cp\_codec\_id codec\_id

**Definition** hci\_types.h:979

[bt\_hci\_cp\_read\_ctlr\_delay](structbt__hci__cp__read__ctlr__delay.md)

**Definition** hci\_types.h:995

[bt\_hci\_cp\_read\_ctlr\_delay::codec\_id](structbt__hci__cp__read__ctlr__delay.md#a2afb9ca8bc2e24cd479b29bc1a53c867)

struct bt\_hci\_cp\_codec\_id codec\_id

**Definition** hci\_types.h:996

[bt\_hci\_cp\_read\_ctlr\_delay::direction](structbt__hci__cp__read__ctlr__delay.md#a5e9f74d4f82809289038da29af0c663d)

uint8\_t direction

**Definition** hci\_types.h:998

[bt\_hci\_cp\_read\_ctlr\_delay::transport](structbt__hci__cp__read__ctlr__delay.md#a60a6a5b87896d0c27d734b56ead58a9b)

uint8\_t transport

**Definition** hci\_types.h:997

[bt\_hci\_cp\_read\_ctlr\_delay::codec\_config](structbt__hci__cp__read__ctlr__delay.md#a6c15d141c40bca8bd095f4a86f5a93bd)

uint8\_t codec\_config[0]

**Definition** hci\_types.h:1000

[bt\_hci\_cp\_read\_ctlr\_delay::codec\_config\_len](structbt__hci__cp__read__ctlr__delay.md#ac881526b479d5f1717efbe35cdcc7e87)

uint8\_t codec\_config\_len

**Definition** hci\_types.h:999

[bt\_hci\_cp\_read\_encryption\_key\_size](structbt__hci__cp__read__encryption__key__size.md)

**Definition** hci\_types.h:1022

[bt\_hci\_cp\_read\_encryption\_key\_size::handle](structbt__hci__cp__read__encryption__key__size.md#af15765007fd0e2fc4186b54323553019)

uint16\_t handle

**Definition** hci\_types.h:1023

[bt\_hci\_cp\_read\_local\_ext\_features](structbt__hci__cp__read__local__ext__features.md)

**Definition** hci\_types.h:861

[bt\_hci\_cp\_read\_local\_ext\_features::page](structbt__hci__cp__read__local__ext__features.md#a79c6a6a6f1026a7e9ee774183ea7e132)

uint8\_t page

**Definition** hci\_types.h:862

[bt\_hci\_cp\_read\_remote\_ext\_features](structbt__hci__cp__read__remote__ext__features.md)

**Definition** hci\_types.h:514

[bt\_hci\_cp\_read\_remote\_ext\_features::page](structbt__hci__cp__read__remote__ext__features.md#a6aff189605b276998e58b051429a5cd2)

uint8\_t page

**Definition** hci\_types.h:516

[bt\_hci\_cp\_read\_remote\_ext\_features::handle](structbt__hci__cp__read__remote__ext__features.md#aaa236c11d148252e34fd20d794d991f3)

uint16\_t handle

**Definition** hci\_types.h:515

[bt\_hci\_cp\_read\_remote\_features](structbt__hci__cp__read__remote__features.md)

**Definition** hci\_types.h:509

[bt\_hci\_cp\_read\_remote\_features::handle](structbt__hci__cp__read__remote__features.md#ae14362a04c00b37342f3cc413f3933d3)

uint16\_t handle

**Definition** hci\_types.h:510

[bt\_hci\_cp\_read\_remote\_version\_info](structbt__hci__cp__read__remote__version__info.md)

**Definition** hci\_types.h:520

[bt\_hci\_cp\_read\_remote\_version\_info::handle](structbt__hci__cp__read__remote__version__info.md#a504b83f16a82b1e179d74547c7a29bf3)

uint16\_t handle

**Definition** hci\_types.h:521

[bt\_hci\_cp\_read\_rssi](structbt__hci__cp__read__rssi.md)

**Definition** hci\_types.h:1009

[bt\_hci\_cp\_read\_rssi::handle](structbt__hci__cp__read__rssi.md#a0662bc56b344ca2bf9a2dcabe8a13c09)

uint16\_t handle

**Definition** hci\_types.h:1010

[bt\_hci\_cp\_read\_tx\_power\_level](structbt__hci__cp__read__tx__power__level.md)

**Definition** hci\_types.h:661

[bt\_hci\_cp\_read\_tx\_power\_level::type](structbt__hci__cp__read__tx__power__level.md#a1920e671ec2deda1daf47f06a86d2881)

uint8\_t type

**Definition** hci\_types.h:663

[bt\_hci\_cp\_read\_tx\_power\_level::handle](structbt__hci__cp__read__tx__power__level.md#a1c268364fc80b9478d70b7eb997d9825)

uint16\_t handle

**Definition** hci\_types.h:662

[bt\_hci\_cp\_reject\_conn\_req](structbt__hci__cp__reject__conn__req.md)

**Definition** hci\_types.h:444

[bt\_hci\_cp\_reject\_conn\_req::reason](structbt__hci__cp__reject__conn__req.md#a1c2e234d6d00296bc01962b95e849df0)

uint8\_t reason

**Definition** hci\_types.h:446

[bt\_hci\_cp\_reject\_conn\_req::bdaddr](structbt__hci__cp__reject__conn__req.md#a9a1cb4173367c6f018fbd30a47c590b4)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:445

[bt\_hci\_cp\_remote\_name\_cancel](structbt__hci__cp__remote__name__cancel.md)

**Definition** hci\_types.h:500

[bt\_hci\_cp\_remote\_name\_cancel::bdaddr](structbt__hci__cp__remote__name__cancel.md#a0b7b4362804077ce828aeeb2b8af86b9)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:501

[bt\_hci\_cp\_remote\_name\_request](structbt__hci__cp__remote__name__request.md)

**Definition** hci\_types.h:492

[bt\_hci\_cp\_remote\_name\_request::bdaddr](structbt__hci__cp__remote__name__request.md#a5093f7bb70fa36f4948039d02d594e27)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:493

[bt\_hci\_cp\_remote\_name\_request::clock\_offset](structbt__hci__cp__remote__name__request.md#a5d7ea30052f8e4e2b3564659ca187c48)

uint16\_t clock\_offset

**Definition** hci\_types.h:496

[bt\_hci\_cp\_remote\_name\_request::reserved](structbt__hci__cp__remote__name__request.md#ab1883aa2b08d89f9c3190f338808a43c)

uint8\_t reserved

**Definition** hci\_types.h:495

[bt\_hci\_cp\_remote\_name\_request::pscan\_rep\_mode](structbt__hci__cp__remote__name__request.md#aed0aea58ca6f5dc15220083d377cbf5c)

uint8\_t pscan\_rep\_mode

**Definition** hci\_types.h:494

[bt\_hci\_cp\_set\_conn\_encrypt](structbt__hci__cp__set__conn__encrypt.md)

**Definition** hci\_types.h:486

[bt\_hci\_cp\_set\_conn\_encrypt::handle](structbt__hci__cp__set__conn__encrypt.md#a39e0c40ed6e6e9387ae384fd122fca4b)

uint16\_t handle

**Definition** hci\_types.h:487

[bt\_hci\_cp\_set\_conn\_encrypt::encrypt](structbt__hci__cp__set__conn__encrypt.md#aa259563efd49d04a8886f74169fd30b1)

uint8\_t encrypt

**Definition** hci\_types.h:488

[bt\_hci\_cp\_set\_ctl\_to\_host\_flow](structbt__hci__cp__set__ctl__to__host__flow.md)

**Definition** hci\_types.h:744

[bt\_hci\_cp\_set\_ctl\_to\_host\_flow::flow\_enable](structbt__hci__cp__set__ctl__to__host__flow.md#a75b614de1ab1fbfc6aa9c11d833976a6)

uint8\_t flow\_enable

**Definition** hci\_types.h:745

[bt\_hci\_cp\_set\_event\_mask\_page\_2](structbt__hci__cp__set__event__mask__page__2.md)

**Definition** hci\_types.h:778

[bt\_hci\_cp\_set\_event\_mask\_page\_2::events\_page\_2](structbt__hci__cp__set__event__mask__page__2.md#aacf1308d0892226e2c10216a07cd1fcc)

uint8\_t events\_page\_2[8]

**Definition** hci\_types.h:779

[bt\_hci\_cp\_set\_event\_mask](structbt__hci__cp__set__event__mask.md)

**Definition** hci\_types.h:560

[bt\_hci\_cp\_set\_event\_mask::events](structbt__hci__cp__set__event__mask.md#ab3af227511f47ee03f2d6aba8ae65c5d)

uint8\_t events[8]

**Definition** hci\_types.h:561

[bt\_hci\_cp\_setup\_sync\_conn](structbt__hci__cp__setup__sync__conn.md)

**Definition** hci\_types.h:422

[bt\_hci\_cp\_setup\_sync\_conn::rx\_bandwidth](structbt__hci__cp__setup__sync__conn.md#a137601ab44970782e2f3d4fcd2c8fcc2)

uint32\_t rx\_bandwidth

**Definition** hci\_types.h:425

[bt\_hci\_cp\_setup\_sync\_conn::content\_format](structbt__hci__cp__setup__sync__conn.md#a4d7df5b1aa714bc14d0b6c3cbccc5014)

uint16\_t content\_format

**Definition** hci\_types.h:427

[bt\_hci\_cp\_setup\_sync\_conn::max\_latency](structbt__hci__cp__setup__sync__conn.md#a5ffb5e552d4913974a10a16083f82864)

uint16\_t max\_latency

**Definition** hci\_types.h:426

[bt\_hci\_cp\_setup\_sync\_conn::retrans\_effort](structbt__hci__cp__setup__sync__conn.md#a61ebbc775d3ca0724ea173d72a96e0c0)

uint8\_t retrans\_effort

**Definition** hci\_types.h:428

[bt\_hci\_cp\_setup\_sync\_conn::pkt\_type](structbt__hci__cp__setup__sync__conn.md#a6d4c16a4d77d3ee4f8f65ab18a0f192d)

uint16\_t pkt\_type

**Definition** hci\_types.h:429

[bt\_hci\_cp\_setup\_sync\_conn::tx\_bandwidth](structbt__hci__cp__setup__sync__conn.md#aa35718e13a7d778c779be535c2b1945e)

uint32\_t tx\_bandwidth

**Definition** hci\_types.h:424

[bt\_hci\_cp\_setup\_sync\_conn::handle](structbt__hci__cp__setup__sync__conn.md#ad065185846694fc0070bb366e642f1c7)

uint16\_t handle

**Definition** hci\_types.h:423

[bt\_hci\_cp\_user\_confirm\_reply](structbt__hci__cp__user__confirm__reply.md)

**Definition** hci\_types.h:534

[bt\_hci\_cp\_user\_confirm\_reply::bdaddr](structbt__hci__cp__user__confirm__reply.md#abe0e8da3e590c565364ed30ba107a0e6)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:535

[bt\_hci\_cp\_user\_passkey\_neg\_reply](structbt__hci__cp__user__passkey__neg__reply.md)

**Definition** hci\_types.h:549

[bt\_hci\_cp\_user\_passkey\_neg\_reply::bdaddr](structbt__hci__cp__user__passkey__neg__reply.md#ade9d7068054b15089b8c238ecc3e4397)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:550

[bt\_hci\_cp\_user\_passkey\_reply](structbt__hci__cp__user__passkey__reply.md)

**Definition** hci\_types.h:543

[bt\_hci\_cp\_user\_passkey\_reply::bdaddr](structbt__hci__cp__user__passkey__reply.md#a56dbb4a858ecbf36eee61e24ed3742cf)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:544

[bt\_hci\_cp\_user\_passkey\_reply::passkey](structbt__hci__cp__user__passkey__reply.md#a80483025a32f37e7f75b3a220d48148c)

uint32\_t passkey

**Definition** hci\_types.h:545

[bt\_hci\_cp\_write\_auth\_payload\_timeout](structbt__hci__cp__write__auth__payload__timeout.md)

**Definition** hci\_types.h:805

[bt\_hci\_cp\_write\_auth\_payload\_timeout::auth\_payload\_timeout](structbt__hci__cp__write__auth__payload__timeout.md#a385c88012b09ec561b9ba7edaadeb574)

uint16\_t auth\_payload\_timeout

**Definition** hci\_types.h:807

[bt\_hci\_cp\_write\_auth\_payload\_timeout::handle](structbt__hci__cp__write__auth__payload__timeout.md#ad99d5b9f416f11492ac0f412b400aeb6)

uint16\_t handle

**Definition** hci\_types.h:806

[bt\_hci\_cp\_write\_class\_of\_device](structbt__hci__cp__write__class__of__device.md)

**Definition** hci\_types.h:654

[bt\_hci\_cp\_write\_class\_of\_device::class\_of\_device](structbt__hci__cp__write__class__of__device.md#acc3b940de1a5da095e8a4f18e69229f2)

uint8\_t class\_of\_device[3]

**Definition** hci\_types.h:655

[bt\_hci\_cp\_write\_conn\_accept\_timeout](structbt__hci__cp__write__conn__accept__timeout.md)

**Definition** hci\_types.h:578

[bt\_hci\_cp\_write\_conn\_accept\_timeout::conn\_accept\_timeout](structbt__hci__cp__write__conn__accept__timeout.md#a13de5f88920c6a41dafa598734b7acf9)

uint16\_t conn\_accept\_timeout

**Definition** hci\_types.h:579

[bt\_hci\_cp\_write\_inquiry\_mode](structbt__hci__cp__write__inquiry__mode.md)

**Definition** hci\_types.h:768

[bt\_hci\_cp\_write\_inquiry\_mode::mode](structbt__hci__cp__write__inquiry__mode.md#a827e138b7faaec54ec84a1cc1e0c480f)

uint8\_t mode

**Definition** hci\_types.h:769

[bt\_hci\_cp\_write\_le\_host\_supp](structbt__hci__cp__write__le__host__supp.md)

**Definition** hci\_types.h:783

[bt\_hci\_cp\_write\_le\_host\_supp::le](structbt__hci__cp__write__le__host__supp.md#ace1838a80b6061231b536f36e8999ac0)

uint8\_t le

**Definition** hci\_types.h:784

[bt\_hci\_cp\_write\_le\_host\_supp::simul](structbt__hci__cp__write__le__host__supp.md#ad2c27c0f98b2334490022e90563e1271)

uint8\_t simul

**Definition** hci\_types.h:785

[bt\_hci\_cp\_write\_sc\_host\_supp](structbt__hci__cp__write__sc__host__supp.md)

**Definition** hci\_types.h:789

[bt\_hci\_cp\_write\_sc\_host\_supp::sc\_support](structbt__hci__cp__write__sc__host__supp.md#a48ef951f4de05c5772be5c08edca7cec)

uint8\_t sc\_support

**Definition** hci\_types.h:790

[bt\_hci\_cp\_write\_ssp\_mode](structbt__hci__cp__write__ssp__mode.md)

**Definition** hci\_types.h:773

[bt\_hci\_cp\_write\_ssp\_mode::mode](structbt__hci__cp__write__ssp__mode.md#a8ebf7f7890adec53aa8c2307d2b1a33f)

uint8\_t mode

**Definition** hci\_types.h:774

[bt\_hci\_evt\_auth\_complete](structbt__hci__evt__auth__complete.md)

**Definition** hci\_types.h:2777

[bt\_hci\_evt\_auth\_complete::handle](structbt__hci__evt__auth__complete.md#a7a78803e156218f138866fbb13fdadce)

uint16\_t handle

**Definition** hci\_types.h:2779

[bt\_hci\_evt\_auth\_complete::status](structbt__hci__evt__auth__complete.md#ae2b4b5bcc7195247626004d46ee22dd5)

uint8\_t status

**Definition** hci\_types.h:2778

[bt\_hci\_evt\_auth\_payload\_timeout\_exp](structbt__hci__evt__auth__payload__timeout__exp.md)

**Definition** hci\_types.h:3065

[bt\_hci\_evt\_auth\_payload\_timeout\_exp::handle](structbt__hci__evt__auth__payload__timeout__exp.md#a799bc3c63fe5083d61d8bf152ef4cee7)

uint16\_t handle

**Definition** hci\_types.h:3066

[bt\_hci\_evt\_cc\_status](structbt__hci__evt__cc__status.md)

**Definition** hci\_types.h:2818

[bt\_hci\_evt\_cc\_status::status](structbt__hci__evt__cc__status.md#a97cceaa218700da9b529ebadbb08c42c)

uint8\_t status

**Definition** hci\_types.h:2819

[bt\_hci\_evt\_cmd\_complete](structbt__hci__evt__cmd__complete.md)

**Definition** hci\_types.h:2813

[bt\_hci\_evt\_cmd\_complete::opcode](structbt__hci__evt__cmd__complete.md#a3e61d980b4fa3084d3c50ead735fb76d)

uint16\_t opcode

**Definition** hci\_types.h:2815

[bt\_hci\_evt\_cmd\_complete::ncmd](structbt__hci__evt__cmd__complete.md#a4da0539f81057722c8c322685bc12a40)

uint8\_t ncmd

**Definition** hci\_types.h:2814

[bt\_hci\_evt\_cmd\_status](structbt__hci__evt__cmd__status.md)

**Definition** hci\_types.h:2823

[bt\_hci\_evt\_cmd\_status::opcode](structbt__hci__evt__cmd__status.md#a34002b693dc201083be4be77cfddcdb5)

uint16\_t opcode

**Definition** hci\_types.h:2826

[bt\_hci\_evt\_cmd\_status::ncmd](structbt__hci__evt__cmd__status.md#aed690e1cea2411df167e66cfaa742639)

uint8\_t ncmd

**Definition** hci\_types.h:2825

[bt\_hci\_evt\_cmd\_status::status](structbt__hci__evt__cmd__status.md#aedd1560409005dbce409b892af1e3edf)

uint8\_t status

**Definition** hci\_types.h:2824

[bt\_hci\_evt\_conn\_complete](structbt__hci__evt__conn__complete.md)

**Definition** hci\_types.h:2754

[bt\_hci\_evt\_conn\_complete::status](structbt__hci__evt__conn__complete.md#a3dbf4fef53279003b7304ffee4a55e56)

uint8\_t status

**Definition** hci\_types.h:2755

[bt\_hci\_evt\_conn\_complete::bdaddr](structbt__hci__evt__conn__complete.md#a60a2ca6a8f16e4562c12b369685efa9b)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:2757

[bt\_hci\_evt\_conn\_complete::encr\_enabled](structbt__hci__evt__conn__complete.md#a975617e8b568675a3ed8883cbe411557)

uint8\_t encr\_enabled

**Definition** hci\_types.h:2759

[bt\_hci\_evt\_conn\_complete::handle](structbt__hci__evt__conn__complete.md#ad8877912008ea7445a67abc43aab5021)

uint16\_t handle

**Definition** hci\_types.h:2756

[bt\_hci\_evt\_conn\_complete::link\_type](structbt__hci__evt__conn__complete.md#afd9a21adf7d35205fb7e222c2e9e0328)

uint8\_t link\_type

**Definition** hci\_types.h:2758

[bt\_hci\_evt\_conn\_request](structbt__hci__evt__conn__request.md)

**Definition** hci\_types.h:2763

[bt\_hci\_evt\_conn\_request::bdaddr](structbt__hci__evt__conn__request.md#a03a2ee7ff7754173dff0809e4ebce9e6)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:2764

[bt\_hci\_evt\_conn\_request::dev\_class](structbt__hci__evt__conn__request.md#a6059d7c56f45d2fe047a7324db1e820d)

uint8\_t dev\_class[3]

**Definition** hci\_types.h:2765

[bt\_hci\_evt\_conn\_request::link\_type](structbt__hci__evt__conn__request.md#ae11d550701f64717a7d6df5c89b92d0e)

uint8\_t link\_type

**Definition** hci\_types.h:2766

[bt\_hci\_evt\_data\_buf\_overflow](structbt__hci__evt__data__buf__overflow.md)

**Definition** hci\_types.h:2881

[bt\_hci\_evt\_data\_buf\_overflow::link\_type](structbt__hci__evt__data__buf__overflow.md#ae0201e03ebb9b9b33e9eae593a56355f)

uint8\_t link\_type

**Definition** hci\_types.h:2882

[bt\_hci\_evt\_disconn\_complete](structbt__hci__evt__disconn__complete.md)

**Definition** hci\_types.h:2770

[bt\_hci\_evt\_disconn\_complete::reason](structbt__hci__evt__disconn__complete.md#a172554fbacf7aaa4dfbafe58b60fa5e6)

uint8\_t reason

**Definition** hci\_types.h:2773

[bt\_hci\_evt\_disconn\_complete::handle](structbt__hci__evt__disconn__complete.md#ab75f198a6495ad02a00bb3df99ab4258)

uint16\_t handle

**Definition** hci\_types.h:2772

[bt\_hci\_evt\_disconn\_complete::status](structbt__hci__evt__disconn__complete.md#aed22ac781e9d70d11e7ebbe6f2e063bd)

uint8\_t status

**Definition** hci\_types.h:2771

[bt\_hci\_evt\_encrypt\_change](structbt__hci__evt__encrypt__change.md)

**Definition** hci\_types.h:2790

[bt\_hci\_evt\_encrypt\_change::encrypt](structbt__hci__evt__encrypt__change.md#a61cc0e3c209acbb289d071515b44860a)

uint8\_t encrypt

**Definition** hci\_types.h:2793

[bt\_hci\_evt\_encrypt\_change::handle](structbt__hci__evt__encrypt__change.md#a7737f659115ca602c1224c364a4c7404)

uint16\_t handle

**Definition** hci\_types.h:2792

[bt\_hci\_evt\_encrypt\_change::status](structbt__hci__evt__encrypt__change.md#af063bbd28d29edbcc81e907631167de7)

uint8\_t status

**Definition** hci\_types.h:2791

[bt\_hci\_evt\_encrypt\_key\_refresh\_complete](structbt__hci__evt__encrypt__key__refresh__complete.md)

**Definition** hci\_types.h:3018

[bt\_hci\_evt\_encrypt\_key\_refresh\_complete::handle](structbt__hci__evt__encrypt__key__refresh__complete.md#af5562687a4f6e3a1e82cd1a81cec5ad6)

uint16\_t handle

**Definition** hci\_types.h:3020

[bt\_hci\_evt\_encrypt\_key\_refresh\_complete::status](structbt__hci__evt__encrypt__key__refresh__complete.md#afdd162cff0f1eedfe9e8ee7223b3226e)

uint8\_t status

**Definition** hci\_types.h:3019

[bt\_hci\_evt\_extended\_inquiry\_result](structbt__hci__evt__extended__inquiry__result.md)

**Definition** hci\_types.h:3006

[bt\_hci\_evt\_extended\_inquiry\_result::eir](structbt__hci__evt__extended__inquiry__result.md#a1eba2841941f7cdbb00f548ebf0485e9)

uint8\_t eir[240]

**Definition** hci\_types.h:3014

[bt\_hci\_evt\_extended\_inquiry\_result::rssi](structbt__hci__evt__extended__inquiry__result.md#a21f7f48422bcfb867c9ca2e4411a2fbd)

int8\_t rssi

**Definition** hci\_types.h:3013

[bt\_hci\_evt\_extended\_inquiry\_result::clock\_offset](structbt__hci__evt__extended__inquiry__result.md#a30c5586d954585006238e8c2b33a7601)

uint16\_t clock\_offset

**Definition** hci\_types.h:3012

[bt\_hci\_evt\_extended\_inquiry\_result::num\_reports](structbt__hci__evt__extended__inquiry__result.md#a76e4e82d1dedaee94bd730a4134d7d77)

uint8\_t num\_reports

**Definition** hci\_types.h:3007

[bt\_hci\_evt\_extended\_inquiry\_result::addr](structbt__hci__evt__extended__inquiry__result.md#a955a7d36736badfae1f39fa9eda61ebb)

bt\_addr\_t addr

**Definition** hci\_types.h:3008

[bt\_hci\_evt\_extended\_inquiry\_result::cod](structbt__hci__evt__extended__inquiry__result.md#ab4ebcf09817827d1d10ddeee13832759)

uint8\_t cod[3]

**Definition** hci\_types.h:3011

[bt\_hci\_evt\_extended\_inquiry\_result::reserved](structbt__hci__evt__extended__inquiry__result.md#ab6ec4b5efe058e225d173cbda9a16f2e)

uint8\_t reserved

**Definition** hci\_types.h:3010

[bt\_hci\_evt\_extended\_inquiry\_result::pscan\_rep\_mode](structbt__hci__evt__extended__inquiry__result.md#aba4aac84e23ca9d283cb8af265dcaf0d)

uint8\_t pscan\_rep\_mode

**Definition** hci\_types.h:3009

[bt\_hci\_evt\_hardware\_error](structbt__hci__evt__hardware__error.md)

**Definition** hci\_types.h:2830

[bt\_hci\_evt\_hardware\_error::hardware\_code](structbt__hci__evt__hardware__error.md#ab7be990e7cc32df43a3c976cb922e333)

uint8\_t hardware\_code

**Definition** hci\_types.h:2831

[bt\_hci\_evt\_hdr](structbt__hci__evt__hdr.md)

**Definition** hci\_types.h:60

[bt\_hci\_evt\_hdr::len](structbt__hci__evt__hdr.md#a2d580a0c12b29d23002ee9d494c9e16d)

uint8\_t len

**Definition** hci\_types.h:62

[bt\_hci\_evt\_hdr::evt](structbt__hci__evt__hdr.md#aba3aca89bfbe7e8cbd144765cb20fcea)

uint8\_t evt

**Definition** hci\_types.h:61

[bt\_hci\_evt\_inquiry\_complete](structbt__hci__evt__inquiry__complete.md)

**Definition** hci\_types.h:2749

[bt\_hci\_evt\_inquiry\_complete::status](structbt__hci__evt__inquiry__complete.md#aa8c1e8dc9807476f4759a3b3648b6332)

uint8\_t status

**Definition** hci\_types.h:2750

[bt\_hci\_evt\_inquiry\_result\_with\_rssi](structbt__hci__evt__inquiry__result__with__rssi.md)

**Definition** hci\_types.h:2886

[bt\_hci\_evt\_inquiry\_result\_with\_rssi::reserved](structbt__hci__evt__inquiry__result__with__rssi.md#a09914ee9998c0b59cb35ed74d08aa4f2)

uint8\_t reserved

**Definition** hci\_types.h:2889

[bt\_hci\_evt\_inquiry\_result\_with\_rssi::pscan\_rep\_mode](structbt__hci__evt__inquiry__result__with__rssi.md#a0a5c188d0d40b4259cbeb613c0dd12cf)

uint8\_t pscan\_rep\_mode

**Definition** hci\_types.h:2888

[bt\_hci\_evt\_inquiry\_result\_with\_rssi::clock\_offset](structbt__hci__evt__inquiry__result__with__rssi.md#a1ee08f85103581994a88345cc94d7494)

uint16\_t clock\_offset

**Definition** hci\_types.h:2891

[bt\_hci\_evt\_inquiry\_result\_with\_rssi::rssi](structbt__hci__evt__inquiry__result__with__rssi.md#a6d19e6400d7015db7122516e570d7989)

int8\_t rssi

**Definition** hci\_types.h:2892

[bt\_hci\_evt\_inquiry\_result\_with\_rssi::cod](structbt__hci__evt__inquiry__result__with__rssi.md#ad9b4920e2864ed8350de038dffe64574)

uint8\_t cod[3]

**Definition** hci\_types.h:2890

[bt\_hci\_evt\_inquiry\_result\_with\_rssi::addr](structbt__hci__evt__inquiry__result__with__rssi.md#af955dd1660f83e41e6d1b2b5aecf8133)

bt\_addr\_t addr

**Definition** hci\_types.h:2887

[bt\_hci\_evt\_io\_capa\_req](structbt__hci__evt__io__capa__req.md)

**Definition** hci\_types.h:3024

[bt\_hci\_evt\_io\_capa\_req::bdaddr](structbt__hci__evt__io__capa__req.md#a52412f7bd8f8dea391904b9f2444b50a)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:3025

[bt\_hci\_evt\_io\_capa\_resp](structbt__hci__evt__io__capa__resp.md)

**Definition** hci\_types.h:3029

[bt\_hci\_evt\_io\_capa\_resp::authentication](structbt__hci__evt__io__capa__resp.md#a160cb3aea96bf698520e11673a40b2d7)

uint8\_t authentication

**Definition** hci\_types.h:3033

[bt\_hci\_evt\_io\_capa\_resp::capability](structbt__hci__evt__io__capa__resp.md#a851eae620ad90067957d4dec2f04efbe)

uint8\_t capability

**Definition** hci\_types.h:3031

[bt\_hci\_evt\_io\_capa\_resp::oob\_data](structbt__hci__evt__io__capa__resp.md#ab12325d1536fe6a75d0a137bea301e8f)

uint8\_t oob\_data

**Definition** hci\_types.h:3032

[bt\_hci\_evt\_io\_capa\_resp::bdaddr](structbt__hci__evt__io__capa__resp.md#adac9c9f3999099fd460651e3b012fd0f)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:3030

[bt\_hci\_evt\_le\_adv\_set\_terminated](structbt__hci__evt__le__adv__set__terminated.md)

**Definition** hci\_types.h:3262

[bt\_hci\_evt\_le\_adv\_set\_terminated::num\_completed\_ext\_adv\_evts](structbt__hci__evt__le__adv__set__terminated.md#a192f13d6223e437261a225e6b28d04db)

uint8\_t num\_completed\_ext\_adv\_evts

**Definition** hci\_types.h:3266

[bt\_hci\_evt\_le\_adv\_set\_terminated::status](structbt__hci__evt__le__adv__set__terminated.md#a583409e2dc912af2bd5e83124fce3a72)

uint8\_t status

**Definition** hci\_types.h:3263

[bt\_hci\_evt\_le\_adv\_set\_terminated::conn\_handle](structbt__hci__evt__le__adv__set__terminated.md#af2503ee8e1c9add6927fa65b69c48551)

uint16\_t conn\_handle

**Definition** hci\_types.h:3265

[bt\_hci\_evt\_le\_adv\_set\_terminated::adv\_handle](structbt__hci__evt__le__adv__set__terminated.md#af35564406269144cfa2532cd510aa0bd)

uint8\_t adv\_handle

**Definition** hci\_types.h:3264

[bt\_hci\_evt\_le\_advertising\_info](structbt__hci__evt__le__advertising__info.md)

**Definition** hci\_types.h:3087

[bt\_hci\_evt\_le\_advertising\_info::length](structbt__hci__evt__le__advertising__info.md#a11c223103bf89300bd90cb8725746121)

uint8\_t length

**Definition** hci\_types.h:3090

[bt\_hci\_evt\_le\_advertising\_info::addr](structbt__hci__evt__le__advertising__info.md#a1d6863f1a601a2df9d772e3cc1fec118)

bt\_addr\_le\_t addr

**Definition** hci\_types.h:3089

[bt\_hci\_evt\_le\_advertising\_info::evt\_type](structbt__hci__evt__le__advertising__info.md#a5943685ccd3491a883ba9450f700bb86)

uint8\_t evt\_type

**Definition** hci\_types.h:3088

[bt\_hci\_evt\_le\_advertising\_info::data](structbt__hci__evt__le__advertising__info.md#af7d9d720ca67714f2a809e2530a1ff98)

uint8\_t data[0]

**Definition** hci\_types.h:3091

[bt\_hci\_evt\_le\_advertising\_report](structbt__hci__evt__le__advertising__report.md)

**Definition** hci\_types.h:3093

[bt\_hci\_evt\_le\_advertising\_report::adv\_info](structbt__hci__evt__le__advertising__report.md#a9762be19de1f24be4d4626e7e2f8205d)

struct bt\_hci\_evt\_le\_advertising\_info adv\_info[0]

**Definition** hci\_types.h:3095

[bt\_hci\_evt\_le\_advertising\_report::num\_reports](structbt__hci__evt__le__advertising__report.md#ac69aab36aa421630357e4c6706c13e75)

uint8\_t num\_reports

**Definition** hci\_types.h:3094

[bt\_hci\_evt\_le\_big\_complete](structbt__hci__evt__le__big__complete.md)

**Definition** hci\_types.h:3383

[bt\_hci\_evt\_le\_big\_complete::irc](structbt__hci__evt__le__big__complete.md#a07163dee904412d6d8faca8563a944d9)

uint8\_t irc

**Definition** hci\_types.h:3392

[bt\_hci\_evt\_le\_big\_complete::iso\_interval](structbt__hci__evt__le__big__complete.md#a0b0d19d442ed8f1025165c435786ba09)

uint16\_t iso\_interval

**Definition** hci\_types.h:3394

[bt\_hci\_evt\_le\_big\_complete::big\_handle](structbt__hci__evt__le__big__complete.md#a14eaa705f1df38337722a41e8189f807)

uint8\_t big\_handle

**Definition** hci\_types.h:3385

[bt\_hci\_evt\_le\_big\_complete::bn](structbt__hci__evt__le__big__complete.md#a2327e42013033767af233d1c2c3acc56)

uint8\_t bn

**Definition** hci\_types.h:3390

[bt\_hci\_evt\_le\_big\_complete::latency](structbt__hci__evt__le__big__complete.md#a2727d329c37e3b3644cfad02d86abb55)

uint8\_t latency[3]

**Definition** hci\_types.h:3387

[bt\_hci\_evt\_le\_big\_complete::sync\_delay](structbt__hci__evt__le__big__complete.md#a2847d5fc997f80a3e21b7e03d80c9574)

uint8\_t sync\_delay[3]

**Definition** hci\_types.h:3386

[bt\_hci\_evt\_le\_big\_complete::pto](structbt__hci__evt__le__big__complete.md#a6c295870732d65002ec21b4b607e7c0b)

uint8\_t pto

**Definition** hci\_types.h:3391

[bt\_hci\_evt\_le\_big\_complete::max\_pdu](structbt__hci__evt__le__big__complete.md#a8b433ac376e347bf391d4dd804c469f3)

uint16\_t max\_pdu

**Definition** hci\_types.h:3393

[bt\_hci\_evt\_le\_big\_complete::num\_bis](structbt__hci__evt__le__big__complete.md#a995c8fe06ec087f16b771c38171745b1)

uint8\_t num\_bis

**Definition** hci\_types.h:3395

[bt\_hci\_evt\_le\_big\_complete::phy](structbt__hci__evt__le__big__complete.md#abfa6d6bc135350737451e053aa7d212c)

uint8\_t phy

**Definition** hci\_types.h:3388

[bt\_hci\_evt\_le\_big\_complete::status](structbt__hci__evt__le__big__complete.md#ad6787806a3622b3bd3da4512bb8ddffe)

uint8\_t status

**Definition** hci\_types.h:3384

[bt\_hci\_evt\_le\_big\_complete::nse](structbt__hci__evt__le__big__complete.md#ae77364aafe179588f7b8414292e35f5e)

uint8\_t nse

**Definition** hci\_types.h:3389

[bt\_hci\_evt\_le\_big\_complete::handle](structbt__hci__evt__le__big__complete.md#af1c8bd66c3dba70df22f8655b4f27925)

uint16\_t handle[0]

**Definition** hci\_types.h:3396

[bt\_hci\_evt\_le\_big\_sync\_established](structbt__hci__evt__le__big__sync__established.md)

**Definition** hci\_types.h:3406

[bt\_hci\_evt\_le\_big\_sync\_established::max\_pdu](structbt__hci__evt__le__big__sync__established.md#a13db0d402636a71ed029575c1e5771c5)

uint16\_t max\_pdu

**Definition** hci\_types.h:3414

[bt\_hci\_evt\_le\_big\_sync\_established::num\_bis](structbt__hci__evt__le__big__sync__established.md#a2fa405310a8fed0341001b316ca7bd4f)

uint8\_t num\_bis

**Definition** hci\_types.h:3416

[bt\_hci\_evt\_le\_big\_sync\_established::big\_handle](structbt__hci__evt__le__big__sync__established.md#a31a05f8afb69e5885700cc4ad3b161b2)

uint8\_t big\_handle

**Definition** hci\_types.h:3408

[bt\_hci\_evt\_le\_big\_sync\_established::nse](structbt__hci__evt__le__big__sync__established.md#a383dc92f6d16ec971455e20665cd7496)

uint8\_t nse

**Definition** hci\_types.h:3410

[bt\_hci\_evt\_le\_big\_sync\_established::bn](structbt__hci__evt__le__big__sync__established.md#a451466916fbe2f220c277b4b4e62241d)

uint8\_t bn

**Definition** hci\_types.h:3411

[bt\_hci\_evt\_le\_big\_sync\_established::handle](structbt__hci__evt__le__big__sync__established.md#a48766968cb677614f525ea36551ad6c8)

uint16\_t handle[0]

**Definition** hci\_types.h:3417

[bt\_hci\_evt\_le\_big\_sync\_established::iso\_interval](structbt__hci__evt__le__big__sync__established.md#a610313c11c65faf82e06a121affb8b2b)

uint16\_t iso\_interval

**Definition** hci\_types.h:3415

[bt\_hci\_evt\_le\_big\_sync\_established::pto](structbt__hci__evt__le__big__sync__established.md#a6b750de25b2a1afc38995030953364ce)

uint8\_t pto

**Definition** hci\_types.h:3412

[bt\_hci\_evt\_le\_big\_sync\_established::status](structbt__hci__evt__le__big__sync__established.md#a8feb21ef6eacf45dfc09b09e0bce04b1)

uint8\_t status

**Definition** hci\_types.h:3407

[bt\_hci\_evt\_le\_big\_sync\_established::latency](structbt__hci__evt__le__big__sync__established.md#aebb25f9a63fa013ec6ef891ca498dbb4)

uint8\_t latency[3]

**Definition** hci\_types.h:3409

[bt\_hci\_evt\_le\_big\_sync\_established::irc](structbt__hci__evt__le__big__sync__established.md#afd52315dafe02ee28bc26f058b12fe9e)

uint8\_t irc

**Definition** hci\_types.h:3413

[bt\_hci\_evt\_le\_big\_sync\_lost](structbt__hci__evt__le__big__sync__lost.md)

**Definition** hci\_types.h:3421

[bt\_hci\_evt\_le\_big\_sync\_lost::reason](structbt__hci__evt__le__big__sync__lost.md#a02b724a60e71805088aefca9989ad878)

uint8\_t reason

**Definition** hci\_types.h:3423

[bt\_hci\_evt\_le\_big\_sync\_lost::big\_handle](structbt__hci__evt__le__big__sync__lost.md#ae59a9c18363f7aee67563494d98aa971)

uint8\_t big\_handle

**Definition** hci\_types.h:3422

[bt\_hci\_evt\_le\_big\_terminate](structbt__hci__evt__le__big__terminate.md)

**Definition** hci\_types.h:3400

[bt\_hci\_evt\_le\_big\_terminate::reason](structbt__hci__evt__le__big__terminate.md#a0303ac64b825f93210dfc70a8a081ea6)

uint8\_t reason

**Definition** hci\_types.h:3402

[bt\_hci\_evt\_le\_big\_terminate::big\_handle](structbt__hci__evt__le__big__terminate.md#ad9c9e6d42661366d62d79163fa9ad1c7)

uint8\_t big\_handle

**Definition** hci\_types.h:3401

[bt\_hci\_evt\_le\_biginfo\_adv\_report](structbt__hci__evt__le__biginfo__adv__report.md)

**Definition** hci\_types.h:3466

[bt\_hci\_evt\_le\_biginfo\_adv\_report::max\_sdu](structbt__hci__evt__le__biginfo__adv__report.md#a084c13c4b0c9c8dca0653b56e53a0c74)

uint16\_t max\_sdu

**Definition** hci\_types.h:3476

[bt\_hci\_evt\_le\_biginfo\_adv\_report::max\_pdu](structbt__hci__evt__le__biginfo__adv__report.md#a12a000c049e85d2b24720d1a362d28df)

uint16\_t max\_pdu

**Definition** hci\_types.h:3474

[bt\_hci\_evt\_le\_biginfo\_adv\_report::phy](structbt__hci__evt__le__biginfo__adv__report.md#a2301112acf22cf68d6495ff85f0f29bf)

uint8\_t phy

**Definition** hci\_types.h:3477

[bt\_hci\_evt\_le\_biginfo\_adv\_report::sdu\_interval](structbt__hci__evt__le__biginfo__adv__report.md#a81e236ceb24012bc267f656f20f1f8c4)

uint8\_t sdu\_interval[3]

**Definition** hci\_types.h:3475

[bt\_hci\_evt\_le\_biginfo\_adv\_report::sync\_handle](structbt__hci__evt__le__biginfo__adv__report.md#a8be20bfc607e6ce34ea75c53e285b0d5)

uint16\_t sync\_handle

**Definition** hci\_types.h:3467

[bt\_hci\_evt\_le\_biginfo\_adv\_report::irc](structbt__hci__evt__le__biginfo__adv__report.md#a9c1235653245b517a105570c60ddfa09)

uint8\_t irc

**Definition** hci\_types.h:3473

[bt\_hci\_evt\_le\_biginfo\_adv\_report::framing](structbt__hci__evt__le__biginfo__adv__report.md#abe0636beae2f51004193ad5f7c9efeef)

uint8\_t framing

**Definition** hci\_types.h:3478

[bt\_hci\_evt\_le\_biginfo\_adv\_report::bn](structbt__hci__evt__le__biginfo__adv__report.md#ada35f690706be1c6ee8f40787bbe53e5)

uint8\_t bn

**Definition** hci\_types.h:3471

[bt\_hci\_evt\_le\_biginfo\_adv\_report::nse](structbt__hci__evt__le__biginfo__adv__report.md#ae28d5378a7e2ef59fabb62a3a430ccc8)

uint8\_t nse

**Definition** hci\_types.h:3469

[bt\_hci\_evt\_le\_biginfo\_adv\_report::encryption](structbt__hci__evt__le__biginfo__adv__report.md#ae63eaf93f728109b5fb77ca3179ba99c)

uint8\_t encryption

**Definition** hci\_types.h:3479

[bt\_hci\_evt\_le\_biginfo\_adv\_report::num\_bis](structbt__hci__evt__le__biginfo__adv__report.md#ae68f803bbc3f06e7190f62be98d2fe66)

uint8\_t num\_bis

**Definition** hci\_types.h:3468

[bt\_hci\_evt\_le\_biginfo\_adv\_report::iso\_interval](structbt__hci__evt__le__biginfo__adv__report.md#ae92b69ab0bc257d4f50b98e071c6038b)

uint16\_t iso\_interval

**Definition** hci\_types.h:3470

[bt\_hci\_evt\_le\_biginfo\_adv\_report::pto](structbt__hci__evt__le__biginfo__adv__report.md#af3a871d3de34b90fc2b09b0725caf479)

uint8\_t pto

**Definition** hci\_types.h:3472

[bt\_hci\_evt\_le\_chan\_sel\_algo](structbt__hci__evt__le__chan__sel__algo.md)

**Definition** hci\_types.h:3279

[bt\_hci\_evt\_le\_chan\_sel\_algo::handle](structbt__hci__evt__le__chan__sel__algo.md#a16393279e08073dad549e111e610c8e8)

uint16\_t handle

**Definition** hci\_types.h:3280

[bt\_hci\_evt\_le\_chan\_sel\_algo::chan\_sel\_algo](structbt__hci__evt__le__chan__sel__algo.md#a976a62e81b094a59ce42cb6ad3ce45ac)

uint8\_t chan\_sel\_algo

**Definition** hci\_types.h:3281

[bt\_hci\_evt\_le\_cis\_established\_v2](structbt__hci__evt__le__cis__established__v2.md)

**Definition** hci\_types.h:3498

[bt\_hci\_evt\_le\_cis\_established\_v2::status](structbt__hci__evt__le__cis__established__v2.md#a1f43b72368227f212511bb248b4a0e22)

uint8\_t status

**Definition** hci\_types.h:3499

[bt\_hci\_evt\_le\_cis\_established\_v2::p\_latency](structbt__hci__evt__le__cis__established__v2.md#a26b25e1615991977735cbfc679d747f3)

uint8\_t p\_latency[3]

**Definition** hci\_types.h:3504

[bt\_hci\_evt\_le\_cis\_established\_v2::p\_max\_sdu](structbt__hci__evt__le__cis__established__v2.md#a2a060c0bb2831eb3df0dc8ffb74ecebd)

uint16\_t p\_max\_sdu

**Definition** hci\_types.h:3517

[bt\_hci\_evt\_le\_cis\_established\_v2::c\_ft](structbt__hci__evt__le__cis__established__v2.md#a2de704a032ac2379528991f2d01e6979)

uint8\_t c\_ft

**Definition** hci\_types.h:3510

[bt\_hci\_evt\_le\_cis\_established\_v2::sub\_interval](structbt__hci__evt__le__cis__established__v2.md#a353409fe069aba91c5372ee8ae6e1b79)

uint8\_t sub\_interval[3]

**Definition** hci\_types.h:3515

[bt\_hci\_evt\_le\_cis\_established\_v2::p\_ft](structbt__hci__evt__le__cis__established__v2.md#a3b1fc27cca2bc85c36e257aabd8ea612)

uint8\_t p\_ft

**Definition** hci\_types.h:3511

[bt\_hci\_evt\_le\_cis\_established\_v2::p\_phy](structbt__hci__evt__le__cis__established__v2.md#a5a0b08098ac4e6ec93a6ecbbbf4ef587)

uint8\_t p\_phy

**Definition** hci\_types.h:3506

[bt\_hci\_evt\_le\_cis\_established\_v2::c\_bn](structbt__hci__evt__le__cis__established__v2.md#a5f68c3cba98ed96afef0949f6b14ded9)

uint8\_t c\_bn

**Definition** hci\_types.h:3508

[bt\_hci\_evt\_le\_cis\_established\_v2::p\_bn](structbt__hci__evt__le__cis__established__v2.md#a64b48b20283415100fc8bdf33edf2b0e)

uint8\_t p\_bn

**Definition** hci\_types.h:3509

[bt\_hci\_evt\_le\_cis\_established\_v2::interval](structbt__hci__evt__le__cis__established__v2.md#a71762f8a31e20b233a252ac974f6d329)

uint16\_t interval

**Definition** hci\_types.h:3514

[bt\_hci\_evt\_le\_cis\_established\_v2::cig\_sync\_delay](structbt__hci__evt__le__cis__established__v2.md#a754ad7e68821da0bdb8da0bdeb3b4697)

uint8\_t cig\_sync\_delay[3]

**Definition** hci\_types.h:3501

[bt\_hci\_evt\_le\_cis\_established\_v2::conn\_handle](structbt__hci__evt__le__cis__established__v2.md#a7a7b8303183a916225bb0a3ea11d5480)

uint16\_t conn\_handle

**Definition** hci\_types.h:3500

[bt\_hci\_evt\_le\_cis\_established\_v2::c\_sdu\_interval](structbt__hci__evt__le__cis__established__v2.md#a926a5faeb98a99333310d860da37f6f5)

uint8\_t c\_sdu\_interval[3]

**Definition** hci\_types.h:3518

[bt\_hci\_evt\_le\_cis\_established\_v2::c\_phy](structbt__hci__evt__le__cis__established__v2.md#a9b7ba96597a5131927e365b7a45f8d6f)

uint8\_t c\_phy

**Definition** hci\_types.h:3505

[bt\_hci\_evt\_le\_cis\_established\_v2::nse](structbt__hci__evt__le__cis__established__v2.md#ac3a87b20b2f10e980639d232a013f702)

uint8\_t nse

**Definition** hci\_types.h:3507

[bt\_hci\_evt\_le\_cis\_established\_v2::c\_max\_pdu](structbt__hci__evt__le__cis__established__v2.md#acd8cf2d2d85b65d839256f3412a4bb43)

uint16\_t c\_max\_pdu

**Definition** hci\_types.h:3512

[bt\_hci\_evt\_le\_cis\_established\_v2::p\_sdu\_interval](structbt__hci__evt__le__cis__established__v2.md#acf30d6a745803fd4e984d66548ceff58)

uint8\_t p\_sdu\_interval[3]

**Definition** hci\_types.h:3519

[bt\_hci\_evt\_le\_cis\_established\_v2::c\_max\_sdu](structbt__hci__evt__le__cis__established__v2.md#ad054af39ddad854423379b3cc7aafc26)

uint16\_t c\_max\_sdu

**Definition** hci\_types.h:3516

[bt\_hci\_evt\_le\_cis\_established\_v2::c\_latency](structbt__hci__evt__le__cis__established__v2.md#ae580ff8c0ef4cd03365cbf1a06aed8bc)

uint8\_t c\_latency[3]

**Definition** hci\_types.h:3503

[bt\_hci\_evt\_le\_cis\_established\_v2::p\_max\_pdu](structbt__hci__evt__le__cis__established__v2.md#aeea230245aa75dd7f44bf5a4a286e9a5)

uint16\_t p\_max\_pdu

**Definition** hci\_types.h:3513

[bt\_hci\_evt\_le\_cis\_established\_v2::cis\_sync\_delay](structbt__hci__evt__le__cis__established__v2.md#af134783424a77274abac44613bf61264)

uint8\_t cis\_sync\_delay[3]

**Definition** hci\_types.h:3502

[bt\_hci\_evt\_le\_cis\_established\_v2::framing](structbt__hci__evt__le__cis__established__v2.md#af59ca6d54ca770ef8334ea091bcc53f6)

uint8\_t framing

**Definition** hci\_types.h:3520

[bt\_hci\_evt\_le\_cis\_established](structbt__hci__evt__le__cis__established.md)

**Definition** hci\_types.h:3355

[bt\_hci\_evt\_le\_cis\_established::interval](structbt__hci__evt__le__cis__established.md#a0bcdc0d8b3b776660d2e51427f9634dd)

uint16\_t interval

**Definition** hci\_types.h:3371

[bt\_hci\_evt\_le\_cis\_established::p\_ft](structbt__hci__evt__le__cis__established.md#a200afaff044b9eea653d8aee13297dc2)

uint8\_t p\_ft

**Definition** hci\_types.h:3368

[bt\_hci\_evt\_le\_cis\_established::p\_phy](structbt__hci__evt__le__cis__established.md#a25b84cf026775b582c7944e265ffb0b2)

uint8\_t p\_phy

**Definition** hci\_types.h:3363

[bt\_hci\_evt\_le\_cis\_established::status](structbt__hci__evt__le__cis__established.md#a4d90dbeda130a6142ff0b7f9e2ee7c16)

uint8\_t status

**Definition** hci\_types.h:3356

[bt\_hci\_evt\_le\_cis\_established::c\_phy](structbt__hci__evt__le__cis__established.md#a53ea1da3f31313ab73b511c72912bd33)

uint8\_t c\_phy

**Definition** hci\_types.h:3362

[bt\_hci\_evt\_le\_cis\_established::nse](structbt__hci__evt__le__cis__established.md#a683856418764b1110d5c5fea0494fe1e)

uint8\_t nse

**Definition** hci\_types.h:3364

[bt\_hci\_evt\_le\_cis\_established::c\_latency](structbt__hci__evt__le__cis__established.md#a877913bb4b9016c64793458de94d84a0)

uint8\_t c\_latency[3]

**Definition** hci\_types.h:3360

[bt\_hci\_evt\_le\_cis\_established::conn\_handle](structbt__hci__evt__le__cis__established.md#a932e8df0222eb3bcf7bee753414d529e)

uint16\_t conn\_handle

**Definition** hci\_types.h:3357

[bt\_hci\_evt\_le\_cis\_established::c\_bn](structbt__hci__evt__le__cis__established.md#ab6b2d892e3c1e4f6aedee722049b75d3)

uint8\_t c\_bn

**Definition** hci\_types.h:3365

[bt\_hci\_evt\_le\_cis\_established::cig\_sync\_delay](structbt__hci__evt__le__cis__established.md#ac4e5a2535e3e8d3782adac63a4c5a8d9)

uint8\_t cig\_sync\_delay[3]

**Definition** hci\_types.h:3358

[bt\_hci\_evt\_le\_cis\_established::p\_bn](structbt__hci__evt__le__cis__established.md#ad0a79bfadd413bf572b697069695c0a5)

uint8\_t p\_bn

**Definition** hci\_types.h:3366

[bt\_hci\_evt\_le\_cis\_established::c\_ft](structbt__hci__evt__le__cis__established.md#ad0f3bd5f81b660afbc4927a777c2c18e)

uint8\_t c\_ft

**Definition** hci\_types.h:3367

[bt\_hci\_evt\_le\_cis\_established::cis\_sync\_delay](structbt__hci__evt__le__cis__established.md#ae71d6753849ae3c57327c8763cab1802)

uint8\_t cis\_sync\_delay[3]

**Definition** hci\_types.h:3359

[bt\_hci\_evt\_le\_cis\_established::p\_max\_pdu](structbt__hci__evt__le__cis__established.md#ae8b195f433570e28e42a5f9d321964de)

uint16\_t p\_max\_pdu

**Definition** hci\_types.h:3370

[bt\_hci\_evt\_le\_cis\_established::c\_max\_pdu](structbt__hci__evt__le__cis__established.md#ae9fdecff4342f25de30165a4531ad703)

uint16\_t c\_max\_pdu

**Definition** hci\_types.h:3369

[bt\_hci\_evt\_le\_cis\_established::p\_latency](structbt__hci__evt__le__cis__established.md#aefb2d4e0458cbe990903a9f449189c30)

uint8\_t p\_latency[3]

**Definition** hci\_types.h:3361

[bt\_hci\_evt\_le\_cis\_req](structbt__hci__evt__le__cis__req.md)

**Definition** hci\_types.h:3375

[bt\_hci\_evt\_le\_cis\_req::cis\_id](structbt__hci__evt__le__cis__req.md#abdf99eeb7a30c8238bbabdcd60a4847a)

uint8\_t cis\_id

**Definition** hci\_types.h:3379

[bt\_hci\_evt\_le\_cis\_req::cig\_id](structbt__hci__evt__le__cis__req.md#ae0ef0ac224bde55de13df4e5eeaf26be)

uint8\_t cig\_id

**Definition** hci\_types.h:3378

[bt\_hci\_evt\_le\_cis\_req::cis\_handle](structbt__hci__evt__le__cis__req.md#aeed6f4bf58cdb301d6b784a202722acc)

uint16\_t cis\_handle

**Definition** hci\_types.h:3377

[bt\_hci\_evt\_le\_cis\_req::acl\_handle](structbt__hci__evt__le__cis__req.md#af8529013adb87340298a89d4727e6867)

uint16\_t acl\_handle

**Definition** hci\_types.h:3376

[bt\_hci\_evt\_le\_conn\_complete](structbt__hci__evt__le__conn__complete.md)

**Definition** hci\_types.h:3073

[bt\_hci\_evt\_le\_conn\_complete::clock\_accuracy](structbt__hci__evt__le__conn__complete.md#a3fff4c3b30da5922f75d36d97fdeee33)

uint8\_t clock\_accuracy

**Definition** hci\_types.h:3081

[bt\_hci\_evt\_le\_conn\_complete::supv\_timeout](structbt__hci__evt__le__conn__complete.md#a4a90c9824d167b6c45b301e18bfe7f17)

uint16\_t supv\_timeout

**Definition** hci\_types.h:3080

[bt\_hci\_evt\_le\_conn\_complete::handle](structbt__hci__evt__le__conn__complete.md#a67618a1efa0149fadc1063a719d5b674)

uint16\_t handle

**Definition** hci\_types.h:3075

[bt\_hci\_evt\_le\_conn\_complete::role](structbt__hci__evt__le__conn__complete.md#a8455e714d4333d90c2f117892f3dcd6f)

uint8\_t role

**Definition** hci\_types.h:3076

[bt\_hci\_evt\_le\_conn\_complete::status](structbt__hci__evt__le__conn__complete.md#a897981117139c0e53ea7275b689f3799)

uint8\_t status

**Definition** hci\_types.h:3074

[bt\_hci\_evt\_le\_conn\_complete::peer\_addr](structbt__hci__evt__le__conn__complete.md#a97e1aaa10832292ddfe4ee6731ef8999)

bt\_addr\_le\_t peer\_addr

**Definition** hci\_types.h:3077

[bt\_hci\_evt\_le\_conn\_complete::latency](structbt__hci__evt__le__conn__complete.md#ab60cb42ecc83632c61656cd352b71cbe)

uint16\_t latency

**Definition** hci\_types.h:3079

[bt\_hci\_evt\_le\_conn\_complete::interval](structbt__hci__evt__le__conn__complete.md#abe4bc0407d0295329631cb14672a7ee7)

uint16\_t interval

**Definition** hci\_types.h:3078

[bt\_hci\_evt\_le\_conn\_param\_req](structbt__hci__evt__le__conn__param__req.md)

**Definition** hci\_types.h:3129

[bt\_hci\_evt\_le\_conn\_param\_req::interval\_max](structbt__hci__evt__le__conn__param__req.md#a0ed70d1a89f270073f78823d38af6ac9)

uint16\_t interval\_max

**Definition** hci\_types.h:3132

[bt\_hci\_evt\_le\_conn\_param\_req::handle](structbt__hci__evt__le__conn__param__req.md#a4746a001a070f152a3c1c870a7e74df1)

uint16\_t handle

**Definition** hci\_types.h:3130

[bt\_hci\_evt\_le\_conn\_param\_req::interval\_min](structbt__hci__evt__le__conn__param__req.md#a9a9dfc026feb46337b0a36920204b24e)

uint16\_t interval\_min

**Definition** hci\_types.h:3131

[bt\_hci\_evt\_le\_conn\_param\_req::latency](structbt__hci__evt__le__conn__param__req.md#a9f61f0a3e6b6d2e2c6af2f4aef625b75)

uint16\_t latency

**Definition** hci\_types.h:3133

[bt\_hci\_evt\_le\_conn\_param\_req::timeout](structbt__hci__evt__le__conn__param__req.md#ae34de4a3d3e3e4686391eb9d9585dc87)

uint16\_t timeout

**Definition** hci\_types.h:3134

[bt\_hci\_evt\_le\_conn\_update\_complete](structbt__hci__evt__le__conn__update__complete.md)

**Definition** hci\_types.h:3106

[bt\_hci\_evt\_le\_conn\_update\_complete::interval](structbt__hci__evt__le__conn__update__complete.md#a69aa00c0c50978b2aa620aad671119f3)

uint16\_t interval

**Definition** hci\_types.h:3109

[bt\_hci\_evt\_le\_conn\_update\_complete::handle](structbt__hci__evt__le__conn__update__complete.md#a81c0688a5e3b4b3a4d92fbc756a068d5)

uint16\_t handle

**Definition** hci\_types.h:3108

[bt\_hci\_evt\_le\_conn\_update\_complete::supv\_timeout](structbt__hci__evt__le__conn__update__complete.md#aca728975619a10a6e3280b127b59f2f1)

uint16\_t supv\_timeout

**Definition** hci\_types.h:3111

[bt\_hci\_evt\_le\_conn\_update\_complete::status](structbt__hci__evt__le__conn__update__complete.md#ad428bd5e29d40f7551ccdd0747e429d6)

uint8\_t status

**Definition** hci\_types.h:3107

[bt\_hci\_evt\_le\_conn\_update\_complete::latency](structbt__hci__evt__le__conn__update__complete.md#ade2421709a35e0cd0fce3a4d992470c3)

uint16\_t latency

**Definition** hci\_types.h:3110

[bt\_hci\_evt\_le\_connection\_iq\_report](structbt__hci__evt__le__connection__iq__report.md)

**Definition** hci\_types.h:3314

[bt\_hci\_evt\_le\_connection\_iq\_report::cte\_type](structbt__hci__evt__le__connection__iq__report.md#a0188ce28a6c0a2002ae2c64a7bd95e52)

uint8\_t cte\_type

**Definition** hci\_types.h:3320

[bt\_hci\_evt\_le\_connection\_iq\_report::rssi\_ant\_id](structbt__hci__evt__le__connection__iq__report.md#a135498a4abae604967f94840e2f88d2c)

uint8\_t rssi\_ant\_id

**Definition** hci\_types.h:3319

[bt\_hci\_evt\_le\_connection\_iq\_report::conn\_evt\_counter](structbt__hci__evt__le__connection__iq__report.md#a1f388ba96bd52f9ce0f68bacb2945ed8)

uint16\_t conn\_evt\_counter

**Definition** hci\_types.h:3323

[bt\_hci\_evt\_le\_connection\_iq\_report::conn\_handle](structbt__hci__evt__le__connection__iq__report.md#a446f4eab3db19452a84023a676333d1d)

uint16\_t conn\_handle

**Definition** hci\_types.h:3315

[bt\_hci\_evt\_le\_connection\_iq\_report::rssi](structbt__hci__evt__le__connection__iq__report.md#a49e63523f7219174540666c7e5ab3550)

int16\_t rssi

**Definition** hci\_types.h:3318

[bt\_hci\_evt\_le\_connection\_iq\_report::sample](structbt__hci__evt__le__connection__iq__report.md#a5acc2683312523a1137db7897a7373a6)

struct bt\_hci\_le\_iq\_sample sample[0]

**Definition** hci\_types.h:3325

[bt\_hci\_evt\_le\_connection\_iq\_report::slot\_durations](structbt__hci__evt__le__connection__iq__report.md#a74670ca77bb2be81db2cee613dd9c82b)

uint8\_t slot\_durations

**Definition** hci\_types.h:3321

[bt\_hci\_evt\_le\_connection\_iq\_report::sample\_count](structbt__hci__evt__le__connection__iq__report.md#a801dd9373935ba06175ac52237fea759)

uint8\_t sample\_count

**Definition** hci\_types.h:3324

[bt\_hci\_evt\_le\_connection\_iq\_report::rx\_phy](structbt__hci__evt__le__connection__iq__report.md#aa052e03491647acc9f7a6dc7d91cedcc)

uint8\_t rx\_phy

**Definition** hci\_types.h:3316

[bt\_hci\_evt\_le\_connection\_iq\_report::data\_chan\_idx](structbt__hci__evt__le__connection__iq__report.md#ac01a14c591c8bd8e6313aff021ca8d61)

uint8\_t data\_chan\_idx

**Definition** hci\_types.h:3317

[bt\_hci\_evt\_le\_connection\_iq\_report::packet\_status](structbt__hci__evt__le__connection__iq__report.md#af66e8f09a4442b658b80a6eb4dd3064b)

uint8\_t packet\_status

**Definition** hci\_types.h:3322

[bt\_hci\_evt\_le\_connectionless\_iq\_report](structbt__hci__evt__le__connectionless__iq__report.md)

**Definition** hci\_types.h:3300

[bt\_hci\_evt\_le\_connectionless\_iq\_report::rssi](structbt__hci__evt__le__connectionless__iq__report.md#a09112f3711aca00b56045c46958c0992)

int16\_t rssi

**Definition** hci\_types.h:3303

[bt\_hci\_evt\_le\_connectionless\_iq\_report::sample](structbt__hci__evt__le__connectionless__iq__report.md#a1a81f2c8653d85dc29582eed67b4a2a8)

struct bt\_hci\_le\_iq\_sample sample[0]

**Definition** hci\_types.h:3310

[bt\_hci\_evt\_le\_connectionless\_iq\_report::sync\_handle](structbt__hci__evt__le__connectionless__iq__report.md#a36f853d29b8dae1dd393546bbdec5ae2)

uint16\_t sync\_handle

**Definition** hci\_types.h:3301

[bt\_hci\_evt\_le\_connectionless\_iq\_report::sample\_count](structbt__hci__evt__le__connectionless__iq__report.md#a39109ea3f657d0566a73c7ca81bdd2b1)

uint8\_t sample\_count

**Definition** hci\_types.h:3309

[bt\_hci\_evt\_le\_connectionless\_iq\_report::cte\_type](structbt__hci__evt__le__connectionless__iq__report.md#a6b11b00199b002129c569cfec6e83174)

uint8\_t cte\_type

**Definition** hci\_types.h:3305

[bt\_hci\_evt\_le\_connectionless\_iq\_report::slot\_durations](structbt__hci__evt__le__connectionless__iq__report.md#a9d9f0cfe343d81c44e8342b81e2a0608)

uint8\_t slot\_durations

**Definition** hci\_types.h:3306

[bt\_hci\_evt\_le\_connectionless\_iq\_report::packet\_status](structbt__hci__evt__le__connectionless__iq__report.md#ab6fb0f6e32e32a3364ae79d867d9e640)

uint8\_t packet\_status

**Definition** hci\_types.h:3307

[bt\_hci\_evt\_le\_connectionless\_iq\_report::per\_evt\_counter](structbt__hci__evt__le__connectionless__iq__report.md#abfeb0aaa411464bbd7bca927219144fb)

uint16\_t per\_evt\_counter

**Definition** hci\_types.h:3308

[bt\_hci\_evt\_le\_connectionless\_iq\_report::chan\_idx](structbt__hci__evt__le__connectionless__iq__report.md#af50e710884a17191d22f652eaf5788fd)

uint8\_t chan\_idx

**Definition** hci\_types.h:3302

[bt\_hci\_evt\_le\_connectionless\_iq\_report::rssi\_ant\_id](structbt__hci__evt__le__connectionless__iq__report.md#af8c2055666a97f3c8d95747c59515c31)

uint8\_t rssi\_ant\_id

**Definition** hci\_types.h:3304

[bt\_hci\_evt\_le\_cs\_config\_complete](structbt__hci__evt__le__cs__config__complete.md)

**Definition** hci\_types.h:3620

[bt\_hci\_evt\_le\_cs\_config\_complete::main\_mode\_type](structbt__hci__evt__le__cs__config__complete.md#a14f4c29a7f84463f048364389341c7b5)

uint8\_t main\_mode\_type

**Definition** hci\_types.h:3625

[bt\_hci\_evt\_le\_cs\_config\_complete::channel\_map\_repetition](structbt__hci__evt__le__cs__config__complete.md#a1e5ba3ebb5dcac2105a0f859683505bc)

uint8\_t channel\_map\_repetition

**Definition** hci\_types.h:3635

[bt\_hci\_evt\_le\_cs\_config\_complete::min\_main\_mode\_steps](structbt__hci__evt__le__cs__config__complete.md#a21928853b505764e64fcc9190905b12c)

uint8\_t min\_main\_mode\_steps

**Definition** hci\_types.h:3627

[bt\_hci\_evt\_le\_cs\_config\_complete::handle](structbt__hci__evt__le__cs__config__complete.md#a511021f717538d4ae25eb28ad82c5f99)

uint16\_t handle

**Definition** hci\_types.h:3622

[bt\_hci\_evt\_le\_cs\_config\_complete::config\_id](structbt__hci__evt__le__cs__config__complete.md#a544b3480034087ca01d64a41c1c4b8f9)

uint8\_t config\_id

**Definition** hci\_types.h:3623

[bt\_hci\_evt\_le\_cs\_config\_complete::sub\_mode\_type](structbt__hci__evt__le__cs__config__complete.md#a55789928018a6124d87e76709b1b77d9)

uint8\_t sub\_mode\_type

**Definition** hci\_types.h:3626

[bt\_hci\_evt\_le\_cs\_config\_complete::ch3c\_jump](structbt__hci__evt__le__cs__config__complete.md#a5f886c16acd561e143a8796fcc1ea5af)

uint8\_t ch3c\_jump

**Definition** hci\_types.h:3638

[bt\_hci\_evt\_le\_cs\_config\_complete::role](structbt__hci__evt__le__cs__config__complete.md#a6f84ebf8a34a830ced1fc738d46fe244)

uint8\_t role

**Definition** hci\_types.h:3631

[bt\_hci\_evt\_le\_cs\_config\_complete::mode\_0\_steps](structbt__hci__evt__le__cs__config__complete.md#a705a7be2d5ce02c4d78319f4f842b87e)

uint8\_t mode\_0\_steps

**Definition** hci\_types.h:3630

[bt\_hci\_evt\_le\_cs\_config\_complete::ch3c\_shape](structbt__hci__evt__le__cs__config__complete.md#a73bd134e9337a9a47e41bba04623ee0b)

uint8\_t ch3c\_shape

**Definition** hci\_types.h:3637

[bt\_hci\_evt\_le\_cs\_config\_complete::action](structbt__hci__evt__le__cs__config__complete.md#a748fcb3cbd396851a3d159887b12b3e0)

uint8\_t action

**Definition** hci\_types.h:3624

[bt\_hci\_evt\_le\_cs\_config\_complete::reserved](structbt__hci__evt__le__cs__config__complete.md#a7a452a5e49ade26af3290aaaf318577f)

uint8\_t reserved

**Definition** hci\_types.h:3639

[bt\_hci\_evt\_le\_cs\_config\_complete::t\_fcs\_time](structbt__hci__evt__le__cs__config__complete.md#a7aa0fd8a1c9c7270059725416dd0a90f)

uint8\_t t\_fcs\_time

**Definition** hci\_types.h:3642

[bt\_hci\_evt\_le\_cs\_config\_complete::t\_pm\_time](structbt__hci__evt__le__cs__config__complete.md#a7d64425b6aa44b01332ce6fac7813471)

uint8\_t t\_pm\_time

**Definition** hci\_types.h:3643

[bt\_hci\_evt\_le\_cs\_config\_complete::main\_mode\_repetition](structbt__hci__evt__le__cs__config__complete.md#a7fe1af954bae025b9b8bbef70bd1c60e)

uint8\_t main\_mode\_repetition

**Definition** hci\_types.h:3629

[bt\_hci\_evt\_le\_cs\_config\_complete::t\_ip2\_time](structbt__hci__evt__le__cs__config__complete.md#a8fafd0e139a9c85830468e5a056c42b7)

uint8\_t t\_ip2\_time

**Definition** hci\_types.h:3641

[bt\_hci\_evt\_le\_cs\_config\_complete::max\_main\_mode\_steps](structbt__hci__evt__le__cs__config__complete.md#a9b14655fa6bb3c7ac43561a399019a76)

uint8\_t max\_main\_mode\_steps

**Definition** hci\_types.h:3628

[bt\_hci\_evt\_le\_cs\_config\_complete::channel\_selection\_type](structbt__hci__evt__le__cs__config__complete.md#aa323b4a74f7fce33e884d0c32e4014d0)

uint8\_t channel\_selection\_type

**Definition** hci\_types.h:3636

[bt\_hci\_evt\_le\_cs\_config\_complete::channel\_map](structbt__hci__evt__le__cs__config__complete.md#abcf0c43f33a85bcd860323212d57ce5b)

uint8\_t channel\_map[10]

**Definition** hci\_types.h:3634

[bt\_hci\_evt\_le\_cs\_config\_complete::cs\_sync\_phy](structbt__hci__evt__le__cs__config__complete.md#ad0454e31d55ec25a21bc272cae999238)

uint8\_t cs\_sync\_phy

**Definition** hci\_types.h:3633

[bt\_hci\_evt\_le\_cs\_config\_complete::rtt\_type](structbt__hci__evt__le__cs__config__complete.md#ae64ff5dbd9d704c3a7f4c5b98ada399c)

uint8\_t rtt\_type

**Definition** hci\_types.h:3632

[bt\_hci\_evt\_le\_cs\_config\_complete::status](structbt__hci__evt__le__cs__config__complete.md#ae94aa8c92a8d4b33213adc8fc029a02d)

uint8\_t status

**Definition** hci\_types.h:3621

[bt\_hci\_evt\_le\_cs\_config\_complete::t\_ip1\_time](structbt__hci__evt__le__cs__config__complete.md#afd62b1ffe5388c7f094cb086da4c86ba)

uint8\_t t\_ip1\_time

**Definition** hci\_types.h:3640

[bt\_hci\_evt\_le\_cs\_procedure\_enable\_complete](structbt__hci__evt__le__cs__procedure__enable__complete.md)

**Definition** hci\_types.h:3889

[bt\_hci\_evt\_le\_cs\_procedure\_enable\_complete::config\_id](structbt__hci__evt__le__cs__procedure__enable__complete.md#a17b62e13cda5f47dee2e8873686b978e)

uint8\_t config\_id

**Definition** hci\_types.h:3892

[bt\_hci\_evt\_le\_cs\_procedure\_enable\_complete::status](structbt__hci__evt__le__cs__procedure__enable__complete.md#a5822ff654eee794442a05033e0f10fae)

uint8\_t status

**Definition** hci\_types.h:3890

[bt\_hci\_evt\_le\_cs\_procedure\_enable\_complete::tone\_antenna\_config\_selection](structbt__hci__evt__le__cs__procedure__enable__complete.md#a60a9e00cba665d73e65d0ee5b0d9efbc)

uint8\_t tone\_antenna\_config\_selection

**Definition** hci\_types.h:3894

[bt\_hci\_evt\_le\_cs\_procedure\_enable\_complete::event\_interval](structbt__hci__evt__le__cs__procedure__enable__complete.md#a688bfcb6781b2e3480f021c66a3109fe)

uint16\_t event\_interval

**Definition** hci\_types.h:3899

[bt\_hci\_evt\_le\_cs\_procedure\_enable\_complete::max\_procedure\_len](structbt__hci__evt__le__cs__procedure__enable__complete.md#a7a38c8ced8720a428df42e821ec7e9e6)

uint16\_t max\_procedure\_len

**Definition** hci\_types.h:3902

[bt\_hci\_evt\_le\_cs\_procedure\_enable\_complete::state](structbt__hci__evt__le__cs__procedure__enable__complete.md#a7ff8f1e713d9b835f3a4e0e79cb1b3d1)

uint8\_t state

**Definition** hci\_types.h:3893

[bt\_hci\_evt\_le\_cs\_procedure\_enable\_complete::subevent\_interval](structbt__hci__evt__le__cs__procedure__enable__complete.md#a8f5485967662dbd1676d8edd6345fd13)

uint16\_t subevent\_interval

**Definition** hci\_types.h:3898

[bt\_hci\_evt\_le\_cs\_procedure\_enable\_complete::subevents\_per\_event](structbt__hci__evt__le__cs__procedure__enable__complete.md#aacc14948a9e6c384ec94051fb4323599)

uint8\_t subevents\_per\_event

**Definition** hci\_types.h:3897

[bt\_hci\_evt\_le\_cs\_procedure\_enable\_complete::procedure\_count](structbt__hci__evt__le__cs__procedure__enable__complete.md#ac8489dc8ff5f9bf052a7c1a67a544106)

uint16\_t procedure\_count

**Definition** hci\_types.h:3901

[bt\_hci\_evt\_le\_cs\_procedure\_enable\_complete::procedure\_interval](structbt__hci__evt__le__cs__procedure__enable__complete.md#ad7c21907a38747ec405c992ef14e8dd7)

uint16\_t procedure\_interval

**Definition** hci\_types.h:3900

[bt\_hci\_evt\_le\_cs\_procedure\_enable\_complete::handle](structbt__hci__evt__le__cs__procedure__enable__complete.md#adcf8e32c2346073e0fbe273d261f6741)

uint16\_t handle

**Definition** hci\_types.h:3891

[bt\_hci\_evt\_le\_cs\_procedure\_enable\_complete::subevent\_len](structbt__hci__evt__le__cs__procedure__enable__complete.md#af5959274cb88a8e4fdf09e8dd756f31c)

uint8\_t subevent\_len[3]

**Definition** hci\_types.h:3896

[bt\_hci\_evt\_le\_cs\_procedure\_enable\_complete::selected\_tx\_power](structbt__hci__evt__le__cs__procedure__enable__complete.md#afd760c9b6809e6764a652ecb3ee4c2b5)

uint8\_t selected\_tx\_power

**Definition** hci\_types.h:3895

[bt\_hci\_evt\_le\_cs\_read\_remote\_fae\_table\_complete](structbt__hci__evt__le__cs__read__remote__fae__table__complete.md)

**Definition** hci\_types.h:3604

[bt\_hci\_evt\_le\_cs\_read\_remote\_fae\_table\_complete::status](structbt__hci__evt__le__cs__read__remote__fae__table__complete.md#a1ee4d133955f28f45d16226730344428)

uint8\_t status

**Definition** hci\_types.h:3605

[bt\_hci\_evt\_le\_cs\_read\_remote\_fae\_table\_complete::conn\_handle](structbt__hci__evt__le__cs__read__remote__fae__table__complete.md#adcdfbfd2d9c19be0c41121235fbb8eaa)

uint16\_t conn\_handle

**Definition** hci\_types.h:3606

[bt\_hci\_evt\_le\_cs\_read\_remote\_fae\_table\_complete::remote\_fae\_table](structbt__hci__evt__le__cs__read__remote__fae__table__complete.md#ae1ca6d2d4f4305565f1d491ef202fcad)

int8\_t remote\_fae\_table[72]

**Definition** hci\_types.h:3607

[bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md)

**Definition** hci\_types.h:3578

[bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::t\_ip2\_times\_supported](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a0a1d9dcdf184e49349e86980da2e4bed)

uint16\_t t\_ip2\_times\_supported

**Definition** hci\_types.h:3596

[bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::cs\_sync\_phys\_supported](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a1f303dc3aa8a23fccde27a2d2f64d732)

uint8\_t cs\_sync\_phys\_supported

**Definition** hci\_types.h:3593

[bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::t\_sw\_time\_supported](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a21a322fc8efd0c410dda78e2652d506d)

uint8\_t t\_sw\_time\_supported

**Definition** hci\_types.h:3599

[bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::rtt\_random\_payload\_n](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a3f275ad58ca745347172ad0b89faf2c4)

uint8\_t rtt\_random\_payload\_n

**Definition** hci\_types.h:3590

[bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::status](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a40980265955d4d58a9b5407ff845fde4)

uint8\_t status

**Definition** hci\_types.h:3579

[bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::t\_fcs\_times\_supported](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a44869fd19ae813830e38f6e4b88dbb1d)

uint16\_t t\_fcs\_times\_supported

**Definition** hci\_types.h:3597

[bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::conn\_handle](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a4f8fe99c2392c06125ba94e61aed0e6c)

uint16\_t conn\_handle

**Definition** hci\_types.h:3580

[bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::max\_antenna\_paths\_supported](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a50ad0408019dce16685215c6a1b6d0ef)

uint8\_t max\_antenna\_paths\_supported

**Definition** hci\_types.h:3584

[bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::nadm\_random\_capability](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a7af3067f319be094af31512d4ee5101e)

uint16\_t nadm\_random\_capability

**Definition** hci\_types.h:3592

[bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::rtt\_sounding\_n](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a7f796e2eda8d3c7eae556932e37cd93d)

uint8\_t rtt\_sounding\_n

**Definition** hci\_types.h:3589

[bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::rtt\_aa\_only\_n](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a843968ec69106d076596e110407d8a1a)

uint8\_t rtt\_aa\_only\_n

**Definition** hci\_types.h:3588

[bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::roles\_supported](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#a99f9f7b08de6b41e88cea10ba0ca6010)

uint8\_t roles\_supported

**Definition** hci\_types.h:3585

[bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::num\_config\_supported](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#ab09a466b2a9a0be5f5021f1da0d7393a)

uint8\_t num\_config\_supported

**Definition** hci\_types.h:3581

[bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::modes\_supported](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#ab7a35b1093ece7ae9cc5def4a3e473b2)

uint8\_t modes\_supported

**Definition** hci\_types.h:3586

[bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::max\_consecutive\_procedures\_supported](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#ac73a8bf5425c80739e84cb30ce94f3e7)

uint16\_t max\_consecutive\_procedures\_supported

**Definition** hci\_types.h:3582

[bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::subfeatures\_supported](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#ac83543c17606e401d919fce841a12c6c)

uint16\_t subfeatures\_supported

**Definition** hci\_types.h:3594

[bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::rtt\_capability](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#ace95740224b31c127f5e13550cb5a23a)

uint8\_t rtt\_capability

**Definition** hci\_types.h:3587

[bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::t\_ip1\_times\_supported](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#ad330adf1ae5b9b84756d36801a4cf289)

uint16\_t t\_ip1\_times\_supported

**Definition** hci\_types.h:3595

[bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::num\_antennas\_supported](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#adcf35e055d04775c444fa28655b95337)

uint8\_t num\_antennas\_supported

**Definition** hci\_types.h:3583

[bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::nadm\_sounding\_capability](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#adebb5328c7baeaa786bc185fec432e40)

uint16\_t nadm\_sounding\_capability

**Definition** hci\_types.h:3591

[bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::tx\_snr\_capability](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#ae3d06bce4df7a2ca07c5d6dd01124743)

uint8\_t tx\_snr\_capability

**Definition** hci\_types.h:3600

[bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete::t\_pm\_times\_supported](structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.md#afef9f37784d75f54521793f07b5baece)

uint16\_t t\_pm\_times\_supported

**Definition** hci\_types.h:3598

[bt\_hci\_evt\_le\_cs\_security\_enable\_complete](structbt__hci__evt__le__cs__security__enable__complete.md)

**Definition** hci\_types.h:3614

[bt\_hci\_evt\_le\_cs\_security\_enable\_complete::handle](structbt__hci__evt__le__cs__security__enable__complete.md#aaa96a8944598914e4439249ba489f726)

uint16\_t handle

**Definition** hci\_types.h:3616

[bt\_hci\_evt\_le\_cs\_security\_enable\_complete::status](structbt__hci__evt__le__cs__security__enable__complete.md#aaf2de8591b18cd36709f7ef755bee917)

uint8\_t status

**Definition** hci\_types.h:3615

[bt\_hci\_evt\_le\_cs\_subevent\_result\_continue](structbt__hci__evt__le__cs__subevent__result__continue.md)

**Definition** hci\_types.h:3866

[bt\_hci\_evt\_le\_cs\_subevent\_result\_continue::subevent\_abort\_reason](structbt__hci__evt__le__cs__subevent__result__continue.md#a1801aeaac839831198e17b7d96a5532a)

uint8\_t subevent\_abort\_reason

**Definition** hci\_types.h:3875

[bt\_hci\_evt\_le\_cs\_subevent\_result\_continue::num\_antenna\_paths](structbt__hci__evt__le__cs__subevent__result__continue.md#a2f8e1f634e28100815c881a463b51f2c)

uint8\_t num\_antenna\_paths

**Definition** hci\_types.h:3878

[bt\_hci\_evt\_le\_cs\_subevent\_result\_continue::procedure\_abort\_reason](structbt__hci__evt__le__cs__subevent__result__continue.md#a3c7ac056a5898710ffbc0776ef551b4b)

uint8\_t procedure\_abort\_reason

**Definition** hci\_types.h:3876

[bt\_hci\_evt\_le\_cs\_subevent\_result\_continue::procedure\_done\_status](structbt__hci__evt__le__cs__subevent__result__continue.md#a3e5b1e8a247fff36c06447c9ff7c3bb8)

uint8\_t procedure\_done\_status

**Definition** hci\_types.h:3869

[bt\_hci\_evt\_le\_cs\_subevent\_result\_continue::conn\_handle](structbt__hci__evt__le__cs__subevent__result__continue.md#a4126bebec093f6f4d1a22b43abec6b1c)

uint16\_t conn\_handle

**Definition** hci\_types.h:3867

[bt\_hci\_evt\_le\_cs\_subevent\_result\_continue::subevent\_done\_status](structbt__hci__evt__le__cs__subevent__result__continue.md#a49cf181c8518fb3015a0c54f7558aa8c)

uint8\_t subevent\_done\_status

**Definition** hci\_types.h:3870

[bt\_hci\_evt\_le\_cs\_subevent\_result\_continue::steps](structbt__hci__evt__le__cs__subevent__result__continue.md#abbddd0e27178e49abe6eef62bc094a16)

uint8\_t steps[]

**Definition** hci\_types.h:3880

[bt\_hci\_evt\_le\_cs\_subevent\_result\_continue::config\_id](structbt__hci__evt__le__cs__subevent__result__continue.md#adefb9ad1f998460a6d235ebd39bbfe4a)

uint8\_t config\_id

**Definition** hci\_types.h:3868

[bt\_hci\_evt\_le\_cs\_subevent\_result\_continue::num\_steps\_reported](structbt__hci__evt__le__cs__subevent__result__continue.md#af127774b52c4e088f628999136b6cd7c)

uint8\_t num\_steps\_reported

**Definition** hci\_types.h:3879

[bt\_hci\_evt\_le\_cs\_subevent\_result\_step](structbt__hci__evt__le__cs__subevent__result__step.md)

**Definition** hci\_types.h:3836

[bt\_hci\_evt\_le\_cs\_subevent\_result\_step::step\_channel](structbt__hci__evt__le__cs__subevent__result__step.md#a1f074ff26f779292ea32bb405f37b877)

uint8\_t step\_channel

**Definition** hci\_types.h:3838

[bt\_hci\_evt\_le\_cs\_subevent\_result\_step::step\_mode](structbt__hci__evt__le__cs__subevent__result__step.md#a65f6ecf6355883df7924067edc277f35)

uint8\_t step\_mode

**Definition** hci\_types.h:3837

[bt\_hci\_evt\_le\_cs\_subevent\_result\_step::step\_data\_length](structbt__hci__evt__le__cs__subevent__result__step.md#a7fb65809d78fbf08528f177d98e72f6b)

uint8\_t step\_data\_length

**Definition** hci\_types.h:3839

[bt\_hci\_evt\_le\_cs\_subevent\_result\_step::step\_data](structbt__hci__evt__le__cs__subevent__result__step.md#aebb0c47275e4cf92802314a82ffba820)

uint8\_t step\_data[]

**Definition** hci\_types.h:3840

[bt\_hci\_evt\_le\_cs\_subevent\_result](structbt__hci__evt__le__cs__subevent__result.md)

**Definition** hci\_types.h:3843

[bt\_hci\_evt\_le\_cs\_subevent\_result::start\_acl\_conn\_event\_counter](structbt__hci__evt__le__cs__subevent__result.md#a0d6b2ca9f148173abb6207cf7c473c7f)

uint16\_t start\_acl\_conn\_event\_counter

**Definition** hci\_types.h:3846

[bt\_hci\_evt\_le\_cs\_subevent\_result::procedure\_done\_status](structbt__hci__evt__le__cs__subevent__result.md#a27a2848009838977f26df75bfc9bc3c3)

uint8\_t procedure\_done\_status

**Definition** hci\_types.h:3850

[bt\_hci\_evt\_le\_cs\_subevent\_result::config\_id](structbt__hci__evt__le__cs__subevent__result.md#a2e8bdef7f85a4cefeaf625d0c3a4db03)

uint8\_t config\_id

**Definition** hci\_types.h:3845

[bt\_hci\_evt\_le\_cs\_subevent\_result::conn\_handle](structbt__hci__evt__le__cs__subevent__result.md#a3b9c8392fa3aadc2e0673923e0346278)

uint16\_t conn\_handle

**Definition** hci\_types.h:3844

[bt\_hci\_evt\_le\_cs\_subevent\_result::steps](structbt__hci__evt__le__cs__subevent__result.md#a43b46a37648b9fde72634dd7dd6a68e6)

uint8\_t steps[]

**Definition** hci\_types.h:3861

[bt\_hci\_evt\_le\_cs\_subevent\_result::num\_antenna\_paths](structbt__hci__evt__le__cs__subevent__result.md#a9931d5818b801a9c36853f88b259c25e)

uint8\_t num\_antenna\_paths

**Definition** hci\_types.h:3859

[bt\_hci\_evt\_le\_cs\_subevent\_result::reference\_power\_level](structbt__hci__evt__le__cs__subevent__result.md#a9a7260f63122a94cf7eb6ddc3344f742)

uint8\_t reference\_power\_level

**Definition** hci\_types.h:3849

[bt\_hci\_evt\_le\_cs\_subevent\_result::procedure\_abort\_reason](structbt__hci__evt__le__cs__subevent__result.md#ab81c9c55697b2f2c92e3ea2073932ad1)

uint8\_t procedure\_abort\_reason

**Definition** hci\_types.h:3857

[bt\_hci\_evt\_le\_cs\_subevent\_result::frequency\_compensation](structbt__hci__evt__le__cs__subevent__result.md#aba480f7ad78069fd8b83493fac42244e)

uint16\_t frequency\_compensation

**Definition** hci\_types.h:3848

[bt\_hci\_evt\_le\_cs\_subevent\_result::subevent\_abort\_reason](structbt__hci__evt__le__cs__subevent__result.md#acf6f9c4e6fa5897be872d9953993517b)

uint8\_t subevent\_abort\_reason

**Definition** hci\_types.h:3856

[bt\_hci\_evt\_le\_cs\_subevent\_result::procedure\_counter](structbt__hci__evt__le__cs__subevent__result.md#ad08558fd68eb6c43d95a3f0f62bafff0)

uint16\_t procedure\_counter

**Definition** hci\_types.h:3847

[bt\_hci\_evt\_le\_cs\_subevent\_result::subevent\_done\_status](structbt__hci__evt__le__cs__subevent__result.md#aeda28dfb30c51ce2955e1c313069c111)

uint8\_t subevent\_done\_status

**Definition** hci\_types.h:3851

[bt\_hci\_evt\_le\_cs\_subevent\_result::num\_steps\_reported](structbt__hci__evt__le__cs__subevent__result.md#af8c827d508614f553b9f503d0394411b)

uint8\_t num\_steps\_reported

**Definition** hci\_types.h:3860

[bt\_hci\_evt\_le\_cs\_test\_end\_complete](structbt__hci__evt__le__cs__test__end__complete.md)

**Definition** hci\_types.h:3884

[bt\_hci\_evt\_le\_cs\_test\_end\_complete::status](structbt__hci__evt__le__cs__test__end__complete.md#ae083dabff641736ed9a23ffc5a36a737)

uint8\_t status

**Definition** hci\_types.h:3885

[bt\_hci\_evt\_le\_cte\_req\_failed](structbt__hci__evt__le__cte__req__failed.md)

**Definition** hci\_types.h:3331

[bt\_hci\_evt\_le\_cte\_req\_failed::status](structbt__hci__evt__le__cte__req__failed.md#a1433f25dee38014dbd2d061b6d75741a)

uint8\_t status

**Definition** hci\_types.h:3337

[bt\_hci\_evt\_le\_cte\_req\_failed::conn\_handle](structbt__hci__evt__le__cte__req__failed.md#aa903954fa411e4ae49a613b4e76219dc)

uint16\_t conn\_handle

**Definition** hci\_types.h:3338

[bt\_hci\_evt\_le\_data\_len\_change](structbt__hci__evt__le__data__len__change.md)

**Definition** hci\_types.h:3138

[bt\_hci\_evt\_le\_data\_len\_change::max\_rx\_octets](structbt__hci__evt__le__data__len__change.md#a60ecd89a8bbf06ae55b577e3d708d16f)

uint16\_t max\_rx\_octets

**Definition** hci\_types.h:3142

[bt\_hci\_evt\_le\_data\_len\_change::handle](structbt__hci__evt__le__data__len__change.md#a62ebc2f337f23f678c651bf3a276a2a7)

uint16\_t handle

**Definition** hci\_types.h:3139

[bt\_hci\_evt\_le\_data\_len\_change::max\_tx\_time](structbt__hci__evt__le__data__len__change.md#a8264e7ec4aa37e9a699f81d0c56afa40)

uint16\_t max\_tx\_time

**Definition** hci\_types.h:3141

[bt\_hci\_evt\_le\_data\_len\_change::max\_rx\_time](structbt__hci__evt__le__data__len__change.md#a90771e400b998565e7a8bbf4288edd01)

uint16\_t max\_rx\_time

**Definition** hci\_types.h:3143

[bt\_hci\_evt\_le\_data\_len\_change::max\_tx\_octets](structbt__hci__evt__le__data__len__change.md#ae5ce481170336acafbe85687c672281b)

uint16\_t max\_tx\_octets

**Definition** hci\_types.h:3140

[bt\_hci\_evt\_le\_direct\_adv\_info](structbt__hci__evt__le__direct__adv__info.md)

**Definition** hci\_types.h:3173

[bt\_hci\_evt\_le\_direct\_adv\_info::rssi](structbt__hci__evt__le__direct__adv__info.md#a013e5d53ed53e4cd0b923a55c68e20bc)

int8\_t rssi

**Definition** hci\_types.h:3177

[bt\_hci\_evt\_le\_direct\_adv\_info::addr](structbt__hci__evt__le__direct__adv__info.md#a66bbb3e53d84e8c39b216edf91ad131d)

bt\_addr\_le\_t addr

**Definition** hci\_types.h:3175

[bt\_hci\_evt\_le\_direct\_adv\_info::dir\_addr](structbt__hci__evt__le__direct__adv__info.md#ad4ca2d5395bc4c5b95527ac1491c940e)

bt\_addr\_le\_t dir\_addr

**Definition** hci\_types.h:3176

[bt\_hci\_evt\_le\_direct\_adv\_info::evt\_type](structbt__hci__evt__le__direct__adv__info.md#aed957c96860c5f92f9485ab743ce832b)

uint8\_t evt\_type

**Definition** hci\_types.h:3174

[bt\_hci\_evt\_le\_direct\_adv\_report](structbt__hci__evt__le__direct__adv__report.md)

**Definition** hci\_types.h:3179

[bt\_hci\_evt\_le\_direct\_adv\_report::direct\_adv\_info](structbt__hci__evt__le__direct__adv__report.md#a82800d58d4c3ed1fca49b6575bd8f957)

struct bt\_hci\_evt\_le\_direct\_adv\_info direct\_adv\_info[0]

**Definition** hci\_types.h:3181

[bt\_hci\_evt\_le\_direct\_adv\_report::num\_reports](structbt__hci__evt__le__direct__adv__report.md#ae8d1f96739c8fda8827d1c0521f00f94)

uint8\_t num\_reports

**Definition** hci\_types.h:3180

[bt\_hci\_evt\_le\_enh\_conn\_complete\_v2](structbt__hci__evt__le__enh__conn__complete__v2.md)

**Definition** hci\_types.h:2977

[bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::peer\_rpa](structbt__hci__evt__le__enh__conn__complete__v2.md#a014e8bf891684c4cd9e5ec53d986d412)

bt\_addr\_t peer\_rpa

**Definition** hci\_types.h:2983

[bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::local\_rpa](structbt__hci__evt__le__enh__conn__complete__v2.md#a10a1cbf0e9e21bc127dc64adadd53773)

bt\_addr\_t local\_rpa

**Definition** hci\_types.h:2982

[bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::interval](structbt__hci__evt__le__enh__conn__complete__v2.md#a237b8313970cc63b7e57c0ce4913392e)

uint16\_t interval

**Definition** hci\_types.h:2984

[bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::supv\_timeout](structbt__hci__evt__le__enh__conn__complete__v2.md#a2b2ac4890eb9604a3f5cd40f55c2c066)

uint16\_t supv\_timeout

**Definition** hci\_types.h:2986

[bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::role](structbt__hci__evt__le__enh__conn__complete__v2.md#a3343de57a24fa2ebdccf9411f388817d)

uint8\_t role

**Definition** hci\_types.h:2980

[bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::latency](structbt__hci__evt__le__enh__conn__complete__v2.md#a3daa32ac19c4eda4a49bebb64f3145be)

uint16\_t latency

**Definition** hci\_types.h:2985

[bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::clock\_accuracy](structbt__hci__evt__le__enh__conn__complete__v2.md#a7bb168061803d1122e8ee47dc8af3ae9)

uint8\_t clock\_accuracy

**Definition** hci\_types.h:2987

[bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::peer\_addr](structbt__hci__evt__le__enh__conn__complete__v2.md#a7df28c9ddec607d5a84572bb421b7f5a)

bt\_addr\_le\_t peer\_addr

**Definition** hci\_types.h:2981

[bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::sync\_handle](structbt__hci__evt__le__enh__conn__complete__v2.md#a81dca94a6f2a8ea3da7a5a316daa5941)

uint16\_t sync\_handle

**Definition** hci\_types.h:2989

[bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::adv\_handle](structbt__hci__evt__le__enh__conn__complete__v2.md#a883ba3aed9aed00ec0ce425999d97180)

uint8\_t adv\_handle

**Definition** hci\_types.h:2988

[bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::status](structbt__hci__evt__le__enh__conn__complete__v2.md#ad72ba07d766135a94474a9d004da1a66)

uint8\_t status

**Definition** hci\_types.h:2978

[bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::handle](structbt__hci__evt__le__enh__conn__complete__v2.md#affe2dba0634e0215579fb13d77016a8c)

uint16\_t handle

**Definition** hci\_types.h:2979

[bt\_hci\_evt\_le\_enh\_conn\_complete](structbt__hci__evt__le__enh__conn__complete.md)

**Definition** hci\_types.h:3159

[bt\_hci\_evt\_le\_enh\_conn\_complete::handle](structbt__hci__evt__le__enh__conn__complete.md#a13ceff445de6a89f6ea0e832e8b3fba9)

uint16\_t handle

**Definition** hci\_types.h:3161

[bt\_hci\_evt\_le\_enh\_conn\_complete::peer\_addr](structbt__hci__evt__le__enh__conn__complete.md#a4906d6991489e95f8c74aacf5ad8c22e)

bt\_addr\_le\_t peer\_addr

**Definition** hci\_types.h:3163

[bt\_hci\_evt\_le\_enh\_conn\_complete::peer\_rpa](structbt__hci__evt__le__enh__conn__complete.md#a4ece4379733f1ab404fa03f4794192a4)

bt\_addr\_t peer\_rpa

**Definition** hci\_types.h:3165

[bt\_hci\_evt\_le\_enh\_conn\_complete::clock\_accuracy](structbt__hci__evt__le__enh__conn__complete.md#a5641e5cb17df4613cd85f5ad3ba8541c)

uint8\_t clock\_accuracy

**Definition** hci\_types.h:3169

[bt\_hci\_evt\_le\_enh\_conn\_complete::latency](structbt__hci__evt__le__enh__conn__complete.md#a7276bf433c21ffcd3582463492af107b)

uint16\_t latency

**Definition** hci\_types.h:3167

[bt\_hci\_evt\_le\_enh\_conn\_complete::supv\_timeout](structbt__hci__evt__le__enh__conn__complete.md#aa99df131f3fb0330ff8051015d2b78dc)

uint16\_t supv\_timeout

**Definition** hci\_types.h:3168

[bt\_hci\_evt\_le\_enh\_conn\_complete::local\_rpa](structbt__hci__evt__le__enh__conn__complete.md#ab275bcb4a3dd09525b446c01e4e5fdad)

bt\_addr\_t local\_rpa

**Definition** hci\_types.h:3164

[bt\_hci\_evt\_le\_enh\_conn\_complete::interval](structbt__hci__evt__le__enh__conn__complete.md#ac0565ecf0c459275d147933bbdaa9fbc)

uint16\_t interval

**Definition** hci\_types.h:3166

[bt\_hci\_evt\_le\_enh\_conn\_complete::status](structbt__hci__evt__le__enh__conn__complete.md#ae26575416658bf285c45f57ddf426eb2)

uint8\_t status

**Definition** hci\_types.h:3160

[bt\_hci\_evt\_le\_enh\_conn\_complete::role](structbt__hci__evt__le__enh__conn__complete.md#af24298f8c1d58882b4962a14086fc5c7)

uint8\_t role

**Definition** hci\_types.h:3162

[bt\_hci\_evt\_le\_ext\_advertising\_info](structbt__hci__evt__le__ext__advertising__info.md)

**Definition** hci\_types.h:3214

[bt\_hci\_evt\_le\_ext\_advertising\_info::evt\_type](structbt__hci__evt__le__ext__advertising__info.md#a040c27dbcb337162f7ca857b8cb84cfe)

uint16\_t evt\_type

**Definition** hci\_types.h:3215

[bt\_hci\_evt\_le\_ext\_advertising\_info::prim\_phy](structbt__hci__evt__le__ext__advertising__info.md#a088f0e6ea0dfbad25d5f72d0741f7d6d)

uint8\_t prim\_phy

**Definition** hci\_types.h:3217

[bt\_hci\_evt\_le\_ext\_advertising\_info::length](structbt__hci__evt__le__ext__advertising__info.md#a20ca10813f6b3aaba2756a5fe00d3878)

uint8\_t length

**Definition** hci\_types.h:3224

[bt\_hci\_evt\_le\_ext\_advertising\_info::direct\_addr](structbt__hci__evt__le__ext__advertising__info.md#a37f4e4981566b43d6e7c7dfffc5b13fb)

bt\_addr\_le\_t direct\_addr

**Definition** hci\_types.h:3223

[bt\_hci\_evt\_le\_ext\_advertising\_info::tx\_power](structbt__hci__evt__le__ext__advertising__info.md#a39217e77e495e8c4c6288917f8e4d2dc)

int8\_t tx\_power

**Definition** hci\_types.h:3220

[bt\_hci\_evt\_le\_ext\_advertising\_info::sid](structbt__hci__evt__le__ext__advertising__info.md#a5b4d4adff4d97c06311a76abd9847727)

uint8\_t sid

**Definition** hci\_types.h:3219

[bt\_hci\_evt\_le\_ext\_advertising\_info::rssi](structbt__hci__evt__le__ext__advertising__info.md#a6213edbc3ae30f02a6bf2d8e069cd035)

int8\_t rssi

**Definition** hci\_types.h:3221

[bt\_hci\_evt\_le\_ext\_advertising\_info::interval](structbt__hci__evt__le__ext__advertising__info.md#a7da4e49c49eccbf009491bb7da01e111)

uint16\_t interval

**Definition** hci\_types.h:3222

[bt\_hci\_evt\_le\_ext\_advertising\_info::data](structbt__hci__evt__le__ext__advertising__info.md#a9e5536277b0132c8374147677a787b68)

uint8\_t data[0]

**Definition** hci\_types.h:3225

[bt\_hci\_evt\_le\_ext\_advertising\_info::addr](structbt__hci__evt__le__ext__advertising__info.md#acec6858e41ae1b44a2a2ee6d6dbc294d)

bt\_addr\_le\_t addr

**Definition** hci\_types.h:3216

[bt\_hci\_evt\_le\_ext\_advertising\_info::sec\_phy](structbt__hci__evt__le__ext__advertising__info.md#af4d863e12e6f8f19426a14af292fa6d2)

uint8\_t sec\_phy

**Definition** hci\_types.h:3218

[bt\_hci\_evt\_le\_ext\_advertising\_report](structbt__hci__evt__le__ext__advertising__report.md)

**Definition** hci\_types.h:3227

[bt\_hci\_evt\_le\_ext\_advertising\_report::num\_reports](structbt__hci__evt__le__ext__advertising__report.md#a72fc9736934b415e88c51a1f96179871)

uint8\_t num\_reports

**Definition** hci\_types.h:3228

[bt\_hci\_evt\_le\_ext\_advertising\_report::adv\_info](structbt__hci__evt__le__ext__advertising__report.md#a84b9c47a79ccea04198721e2f05ac1a8)

struct bt\_hci\_evt\_le\_ext\_advertising\_info adv\_info[0]

**Definition** hci\_types.h:3229

[bt\_hci\_evt\_le\_generate\_dhkey\_complete](structbt__hci__evt__le__generate__dhkey__complete.md)

**Definition** hci\_types.h:3153

[bt\_hci\_evt\_le\_generate\_dhkey\_complete::status](structbt__hci__evt__le__generate__dhkey__complete.md#a3d10643dd45a71b71d35dfa455ed8590)

uint8\_t status

**Definition** hci\_types.h:3154

[bt\_hci\_evt\_le\_generate\_dhkey\_complete::dhkey](structbt__hci__evt__le__generate__dhkey__complete.md#a8cd8ece786c1443ed43bd3b8fcd4d9bf)

uint8\_t dhkey[32]

**Definition** hci\_types.h:3155

[bt\_hci\_evt\_le\_ltk\_request](structbt__hci__evt__le__ltk__request.md)

**Definition** hci\_types.h:3122

[bt\_hci\_evt\_le\_ltk\_request::ediv](structbt__hci__evt__le__ltk__request.md#a54d5cbde249349337595085c6c3cabad)

uint16\_t ediv

**Definition** hci\_types.h:3125

[bt\_hci\_evt\_le\_ltk\_request::rand](structbt__hci__evt__le__ltk__request.md#a765cba614cd7a972156b6361536b753f)

uint64\_t rand

**Definition** hci\_types.h:3124

[bt\_hci\_evt\_le\_ltk\_request::handle](structbt__hci__evt__le__ltk__request.md#aed00ae384cb7d0deace8d0cc0f8e0068)

uint16\_t handle

**Definition** hci\_types.h:3123

[bt\_hci\_evt\_le\_meta\_event](structbt__hci__evt__le__meta__event.md)

**Definition** hci\_types.h:3060

[bt\_hci\_evt\_le\_meta\_event::subevent](structbt__hci__evt__le__meta__event.md#a536464a525f8d0f9df915be5ee3d33da)

uint8\_t subevent

**Definition** hci\_types.h:3061

[bt\_hci\_evt\_le\_p256\_public\_key\_complete](structbt__hci__evt__le__p256__public__key__complete.md)

**Definition** hci\_types.h:3147

[bt\_hci\_evt\_le\_p256\_public\_key\_complete::status](structbt__hci__evt__le__p256__public__key__complete.md#a57d51fca3a707b445db2534d1e175241)

uint8\_t status

**Definition** hci\_types.h:3148

[bt\_hci\_evt\_le\_p256\_public\_key\_complete::key](structbt__hci__evt__le__p256__public__key__complete.md#af482f81d438b878fb826edbac8d84833)

uint8\_t key[64]

**Definition** hci\_types.h:3149

[bt\_hci\_evt\_le\_past\_received\_v2](structbt__hci__evt__le__past__received__v2.md)

**Definition** hci\_types.h:2933

[bt\_hci\_evt\_le\_past\_received\_v2::sync\_handle](structbt__hci__evt__le__past__received__v2.md#a00bf4bdf12fce6cbf2874b9c4ae09f9f)

uint16\_t sync\_handle

**Definition** hci\_types.h:2937

[bt\_hci\_evt\_le\_past\_received\_v2::adv\_sid](structbt__hci__evt__le__past__received__v2.md#a05d798c9415541ef7f5716992157b1a1)

uint8\_t adv\_sid

**Definition** hci\_types.h:2938

[bt\_hci\_evt\_le\_past\_received\_v2::interval](structbt__hci__evt__le__past__received__v2.md#a736af2c2ee0afd3cb00e8eb4d103991c)

uint16\_t interval

**Definition** hci\_types.h:2941

[bt\_hci\_evt\_le\_past\_received\_v2::clock\_accuracy](structbt__hci__evt__le__past__received__v2.md#a78853d14c3bf9a9aba3c4e15b2e06abb)

uint8\_t clock\_accuracy

**Definition** hci\_types.h:2942

[bt\_hci\_evt\_le\_past\_received\_v2::response\_slot\_delay](structbt__hci__evt__le__past__received__v2.md#a9f55d5f6d17d11e72f7cac363a69fe97)

uint8\_t response\_slot\_delay

**Definition** hci\_types.h:2945

[bt\_hci\_evt\_le\_past\_received\_v2::num\_subevents](structbt__hci__evt__le__past__received__v2.md#ab8a2a55fe071218284d60f1a2896945b)

uint8\_t num\_subevents

**Definition** hci\_types.h:2943

[bt\_hci\_evt\_le\_past\_received\_v2::response\_slot\_spacing](structbt__hci__evt__le__past__received__v2.md#acf711399e575295dcef73cfeeb844eab)

uint8\_t response\_slot\_spacing

**Definition** hci\_types.h:2946

[bt\_hci\_evt\_le\_past\_received\_v2::service\_data](structbt__hci__evt__le__past__received__v2.md#acffc2fa22a16a3a12a4f7dfc3bb45866)

uint16\_t service\_data

**Definition** hci\_types.h:2936

[bt\_hci\_evt\_le\_past\_received\_v2::conn\_handle](structbt__hci__evt__le__past__received__v2.md#adb011949f592ec7f8843d4fd47eca2e9)

uint16\_t conn\_handle

**Definition** hci\_types.h:2935

[bt\_hci\_evt\_le\_past\_received\_v2::phy](structbt__hci__evt__le__past__received__v2.md#ae7a73293519ab45aec40a9a1aeaa4e89)

uint8\_t phy

**Definition** hci\_types.h:2940

[bt\_hci\_evt\_le\_past\_received\_v2::subevent\_interval](structbt__hci__evt__le__past__received__v2.md#aefdc5ac7ef125f4dc5865c198b98c67d)

uint8\_t subevent\_interval

**Definition** hci\_types.h:2944

[bt\_hci\_evt\_le\_past\_received\_v2::status](structbt__hci__evt__le__past__received__v2.md#aefe79f973eda8c7c5670c7a721d55d8a)

uint8\_t status

**Definition** hci\_types.h:2934

[bt\_hci\_evt\_le\_past\_received\_v2::addr](structbt__hci__evt__le__past__received__v2.md#aff78554e8980635290767e9877ac479b)

bt\_addr\_le\_t addr

**Definition** hci\_types.h:2939

[bt\_hci\_evt\_le\_past\_received](structbt__hci__evt__le__past__received.md)

**Definition** hci\_types.h:3342

[bt\_hci\_evt\_le\_past\_received::clock\_accuracy](structbt__hci__evt__le__past__received.md#a00d570636a55c1d84723ad3bc5705d80)

uint8\_t clock\_accuracy

**Definition** hci\_types.h:3351

[bt\_hci\_evt\_le\_past\_received::adv\_sid](structbt__hci__evt__le__past__received.md#a110c7cdd2ff1178d1ca686abaae92b05)

uint8\_t adv\_sid

**Definition** hci\_types.h:3347

[bt\_hci\_evt\_le\_past\_received::status](structbt__hci__evt__le__past__received.md#a1b2c229c99d06f44057b88458f168e7c)

uint8\_t status

**Definition** hci\_types.h:3343

[bt\_hci\_evt\_le\_past\_received::conn\_handle](structbt__hci__evt__le__past__received.md#a1bdbaddb4003cea40738ee540ecb8789)

uint16\_t conn\_handle

**Definition** hci\_types.h:3344

[bt\_hci\_evt\_le\_past\_received::sync\_handle](structbt__hci__evt__le__past__received.md#a2cea2f3b9d51ace91ddf63639e821328)

uint16\_t sync\_handle

**Definition** hci\_types.h:3346

[bt\_hci\_evt\_le\_past\_received::addr](structbt__hci__evt__le__past__received.md#a3e368e95a6831f823d2efa0c0bc1ef51)

bt\_addr\_le\_t addr

**Definition** hci\_types.h:3348

[bt\_hci\_evt\_le\_past\_received::interval](structbt__hci__evt__le__past__received.md#a41ea6099d3cca1caf37ff518a4e95492)

uint16\_t interval

**Definition** hci\_types.h:3350

[bt\_hci\_evt\_le\_past\_received::service\_data](structbt__hci__evt__le__past__received.md#adaa1e432db60a2529ad6266f16604e15)

uint16\_t service\_data

**Definition** hci\_types.h:3345

[bt\_hci\_evt\_le\_past\_received::phy](structbt__hci__evt__le__past__received.md#aedb668e6f3232b1db9035ea89ccf1b71)

uint8\_t phy

**Definition** hci\_types.h:3349

[bt\_hci\_evt\_le\_path\_loss\_threshold](structbt__hci__evt__le__path__loss__threshold.md)

**Definition** hci\_types.h:3439

[bt\_hci\_evt\_le\_path\_loss\_threshold::handle](structbt__hci__evt__le__path__loss__threshold.md#a19b1e37c5e35e1e18424615b5c25d37f)

uint16\_t handle

**Definition** hci\_types.h:3440

[bt\_hci\_evt\_le\_path\_loss\_threshold::current\_path\_loss](structbt__hci__evt__le__path__loss__threshold.md#ac2b04c57137dcb6812fda06d4a22402a)

uint8\_t current\_path\_loss

**Definition** hci\_types.h:3441

[bt\_hci\_evt\_le\_path\_loss\_threshold::zone\_entered](structbt__hci__evt__le__path__loss__threshold.md#add7984e06d523bb34e8380dae1710b7f)

uint8\_t zone\_entered

**Definition** hci\_types.h:3442

[bt\_hci\_evt\_le\_per\_adv\_response\_report](structbt__hci__evt__le__per__adv__response__report.md)

**Definition** hci\_types.h:2968

[bt\_hci\_evt\_le\_per\_adv\_response\_report::num\_responses](structbt__hci__evt__le__per__adv__response__report.md#a37f3519eefe33e87d49c7c2ad0f8b40c)

uint8\_t num\_responses

**Definition** hci\_types.h:2972

[bt\_hci\_evt\_le\_per\_adv\_response\_report::responses](structbt__hci__evt__le__per__adv__response__report.md#a3b1bcca7a7dbc6fcf5709f6152268b87)

struct bt\_hci\_evt\_le\_per\_adv\_response responses[0]

**Definition** hci\_types.h:2973

[bt\_hci\_evt\_le\_per\_adv\_response\_report::tx\_status](structbt__hci__evt__le__per__adv__response__report.md#a46a5b74321a80697fd700a276be18ed3)

uint8\_t tx\_status

**Definition** hci\_types.h:2971

[bt\_hci\_evt\_le\_per\_adv\_response\_report::adv\_handle](structbt__hci__evt__le__per__adv__response__report.md#a9d746015a9c2b48c54008319c892b063)

uint8\_t adv\_handle

**Definition** hci\_types.h:2969

[bt\_hci\_evt\_le\_per\_adv\_response\_report::subevent](structbt__hci__evt__le__per__adv__response__report.md#ad4f8f61150f82f4ba420e3c0a1f333c2)

uint8\_t subevent

**Definition** hci\_types.h:2970

[bt\_hci\_evt\_le\_per\_adv\_response](structbt__hci__evt__le__per__adv__response.md)

**Definition** hci\_types.h:2958

[bt\_hci\_evt\_le\_per\_adv\_response::rssi](structbt__hci__evt__le__per__adv__response.md#a1100429baf398067a396a6ba8db6778a)

int8\_t rssi

**Definition** hci\_types.h:2960

[bt\_hci\_evt\_le\_per\_adv\_response::cte\_type](structbt__hci__evt__le__per__adv__response.md#a4197fbae54be038502312efc14b66320)

uint8\_t cte\_type

**Definition** hci\_types.h:2961

[bt\_hci\_evt\_le\_per\_adv\_response::tx\_power](structbt__hci__evt__le__per__adv__response.md#a74e304822ec7a431802cf8a7539d640e)

int8\_t tx\_power

**Definition** hci\_types.h:2959

[bt\_hci\_evt\_le\_per\_adv\_response::data\_status](structbt__hci__evt__le__per__adv__response.md#aa524756d2cce0718ecfd66704eaf389d)

uint8\_t data\_status

**Definition** hci\_types.h:2963

[bt\_hci\_evt\_le\_per\_adv\_response::response\_slot](structbt__hci__evt__le__per__adv__response.md#aa5b5467f4edd52fb8de078b0948141f0)

uint8\_t response\_slot

**Definition** hci\_types.h:2962

[bt\_hci\_evt\_le\_per\_adv\_response::data](structbt__hci__evt__le__per__adv__response.md#ace3b58eba63b55ce5f3038d4a7877ec2)

uint8\_t data[0]

**Definition** hci\_types.h:2965

[bt\_hci\_evt\_le\_per\_adv\_response::data\_length](structbt__hci__evt__le__per__adv__response.md#af68f0dc92118f78f6f5b0ffbf1854664)

uint8\_t data\_length

**Definition** hci\_types.h:2964

[bt\_hci\_evt\_le\_per\_adv\_subevent\_data\_request](structbt__hci__evt__le__per__adv__subevent__data__request.md)

**Definition** hci\_types.h:2950

[bt\_hci\_evt\_le\_per\_adv\_subevent\_data\_request::subevent\_data\_count](structbt__hci__evt__le__per__adv__subevent__data__request.md#a45cdb248b80602a7f14f24e0324e6f97)

uint8\_t subevent\_data\_count

**Definition** hci\_types.h:2953

[bt\_hci\_evt\_le\_per\_adv\_subevent\_data\_request::subevent\_start](structbt__hci__evt__le__per__adv__subevent__data__request.md#a8f7fd9b149aa52422cb3eb874b91943d)

uint8\_t subevent\_start

**Definition** hci\_types.h:2952

[bt\_hci\_evt\_le\_per\_adv\_subevent\_data\_request::adv\_handle](structbt__hci__evt__le__per__adv__subevent__data__request.md#ae6f6ef17edabfd210a7e6597087ff512)

uint8\_t adv\_handle

**Definition** hci\_types.h:2951

[bt\_hci\_evt\_le\_per\_adv\_sync\_established\_v2](structbt__hci__evt__le__per__adv__sync__established__v2.md)

**Definition** hci\_types.h:2905

[bt\_hci\_evt\_le\_per\_adv\_sync\_established\_v2::sid](structbt__hci__evt__le__per__adv__sync__established__v2.md#a0ce9a9170d93ff69f25ff35eb163511f)

uint8\_t sid

**Definition** hci\_types.h:2908

[bt\_hci\_evt\_le\_per\_adv\_sync\_established\_v2::clock\_accuracy](structbt__hci__evt__le__per__adv__sync__established__v2.md#a13ab0e87d6673a34e51f3112a5fd5a0c)

uint8\_t clock\_accuracy

**Definition** hci\_types.h:2912

[bt\_hci\_evt\_le\_per\_adv\_sync\_established\_v2::phy](structbt__hci__evt__le__per__adv__sync__established__v2.md#a36b5c8454ee3635d2298592c83166f14)

uint8\_t phy

**Definition** hci\_types.h:2910

[bt\_hci\_evt\_le\_per\_adv\_sync\_established\_v2::interval](structbt__hci__evt__le__per__adv__sync__established__v2.md#a958630cb9e275ab6f8ed0c548958e5ee)

uint16\_t interval

**Definition** hci\_types.h:2911

[bt\_hci\_evt\_le\_per\_adv\_sync\_established\_v2::status](structbt__hci__evt__le__per__adv__sync__established__v2.md#a96b975f5a2fcf193b0b58c230486ec36)

uint8\_t status

**Definition** hci\_types.h:2906

[bt\_hci\_evt\_le\_per\_adv\_sync\_established\_v2::response\_slot\_spacing](structbt__hci__evt__le__per__adv__sync__established__v2.md#aacb6946dbfeb2ffbc251910853559329)

uint8\_t response\_slot\_spacing

**Definition** hci\_types.h:2916

[bt\_hci\_evt\_le\_per\_adv\_sync\_established\_v2::handle](structbt__hci__evt__le__per__adv__sync__established__v2.md#ab7d3793e782d7b2bb311b8a5ac3a871b)

uint16\_t handle

**Definition** hci\_types.h:2907

[bt\_hci\_evt\_le\_per\_adv\_sync\_established\_v2::adv\_addr](structbt__hci__evt__le__per__adv__sync__established__v2.md#abd67ec989479eb793e7bf99a4cf371b8)

bt\_addr\_le\_t adv\_addr

**Definition** hci\_types.h:2909

[bt\_hci\_evt\_le\_per\_adv\_sync\_established\_v2::response\_slot\_delay](structbt__hci__evt__le__per__adv__sync__established__v2.md#ac4c2bc8789513692ce0f2cc81aa59476)

uint8\_t response\_slot\_delay

**Definition** hci\_types.h:2915

[bt\_hci\_evt\_le\_per\_adv\_sync\_established\_v2::subevent\_interval](structbt__hci__evt__le__per__adv__sync__established__v2.md#ad21df6269d8242d94ba9cbc1e0d4d344)

uint8\_t subevent\_interval

**Definition** hci\_types.h:2914

[bt\_hci\_evt\_le\_per\_adv\_sync\_established\_v2::num\_subevents](structbt__hci__evt__le__per__adv__sync__established__v2.md#af4fb92baa4f98c08c990ba505faf9226)

uint8\_t num\_subevents

**Definition** hci\_types.h:2913

[bt\_hci\_evt\_le\_per\_adv\_sync\_established](structbt__hci__evt__le__per__adv__sync__established.md)

**Definition** hci\_types.h:3233

[bt\_hci\_evt\_le\_per\_adv\_sync\_established::handle](structbt__hci__evt__le__per__adv__sync__established.md#a3af8529a858992f347ce9570c5696133)

uint16\_t handle

**Definition** hci\_types.h:3235

[bt\_hci\_evt\_le\_per\_adv\_sync\_established::interval](structbt__hci__evt__le__per__adv__sync__established.md#a4873b917a5bc140bb2f04ad2bee5dd69)

uint16\_t interval

**Definition** hci\_types.h:3239

[bt\_hci\_evt\_le\_per\_adv\_sync\_established::status](structbt__hci__evt__le__per__adv__sync__established.md#a9ebe918fee3121168dc5b45e64aaf263)

uint8\_t status

**Definition** hci\_types.h:3234

[bt\_hci\_evt\_le\_per\_adv\_sync\_established::sid](structbt__hci__evt__le__per__adv__sync__established.md#ab11929ef8d3c71c6f2cb7c549be21282)

uint8\_t sid

**Definition** hci\_types.h:3236

[bt\_hci\_evt\_le\_per\_adv\_sync\_established::phy](structbt__hci__evt__le__per__adv__sync__established.md#ab7ce6f56a69b54f02cde8fdae6860e42)

uint8\_t phy

**Definition** hci\_types.h:3238

[bt\_hci\_evt\_le\_per\_adv\_sync\_established::adv\_addr](structbt__hci__evt__le__per__adv__sync__established.md#adf65527ea968f4ece37d7e3c91c795d1)

bt\_addr\_le\_t adv\_addr

**Definition** hci\_types.h:3237

[bt\_hci\_evt\_le\_per\_adv\_sync\_established::clock\_accuracy](structbt__hci__evt__le__per__adv__sync__established.md#aee68069899cc10bc38ad9fb95cf9b7b7)

uint8\_t clock\_accuracy

**Definition** hci\_types.h:3240

[bt\_hci\_evt\_le\_per\_adv\_sync\_lost](structbt__hci__evt__le__per__adv__sync__lost.md)

**Definition** hci\_types.h:3255

[bt\_hci\_evt\_le\_per\_adv\_sync\_lost::handle](structbt__hci__evt__le__per__adv__sync__lost.md#a286d534634411da53a2bda8cdfb077f8)

uint16\_t handle

**Definition** hci\_types.h:3256

[bt\_hci\_evt\_le\_per\_advertising\_report\_v2](structbt__hci__evt__le__per__advertising__report__v2.md)

**Definition** hci\_types.h:2920

[bt\_hci\_evt\_le\_per\_advertising\_report\_v2::length](structbt__hci__evt__le__per__advertising__report__v2.md#a30f4e81346957ad4f9f0488dd93fafc3)

uint8\_t length

**Definition** hci\_types.h:2928

[bt\_hci\_evt\_le\_per\_advertising\_report\_v2::cte\_type](structbt__hci__evt__le__per__advertising__report__v2.md#a3276c2e11c946744b73426f54bf62b8c)

uint8\_t cte\_type

**Definition** hci\_types.h:2924

[bt\_hci\_evt\_le\_per\_advertising\_report\_v2::handle](structbt__hci__evt__le__per__advertising__report__v2.md#a34b15fb9b5b4f0d199ccf274dd489c6a)

uint16\_t handle

**Definition** hci\_types.h:2921

[bt\_hci\_evt\_le\_per\_advertising\_report\_v2::tx\_power](structbt__hci__evt__le__per__advertising__report__v2.md#a37a9eb7d417da9285e22cc7f83071c69)

int8\_t tx\_power

**Definition** hci\_types.h:2922

[bt\_hci\_evt\_le\_per\_advertising\_report\_v2::periodic\_event\_counter](structbt__hci__evt__le__per__advertising__report__v2.md#a499d82e1e3cfc501d399f570ebbcdc42)

uint16\_t periodic\_event\_counter

**Definition** hci\_types.h:2925

[bt\_hci\_evt\_le\_per\_advertising\_report\_v2::data\_status](structbt__hci__evt__le__per__advertising__report__v2.md#a73496cc962721538e27e9924fff0f3db)

uint8\_t data\_status

**Definition** hci\_types.h:2927

[bt\_hci\_evt\_le\_per\_advertising\_report\_v2::data](structbt__hci__evt__le__per__advertising__report__v2.md#a7af1cd4ec9df24e575a83a640eea36d2)

uint8\_t data[0]

**Definition** hci\_types.h:2929

[bt\_hci\_evt\_le\_per\_advertising\_report\_v2::rssi](structbt__hci__evt__le__per__advertising__report__v2.md#ad598ffd0108825803a4734959a354bd8)

int8\_t rssi

**Definition** hci\_types.h:2923

[bt\_hci\_evt\_le\_per\_advertising\_report\_v2::subevent](structbt__hci__evt__le__per__advertising__report__v2.md#af27b23fe38e9ff092d8839cd81749456)

uint8\_t subevent

**Definition** hci\_types.h:2926

[bt\_hci\_evt\_le\_per\_advertising\_report](structbt__hci__evt__le__per__advertising__report.md)

**Definition** hci\_types.h:3244

[bt\_hci\_evt\_le\_per\_advertising\_report::length](structbt__hci__evt__le__per__advertising__report.md#a0ab1d3c5d7eb1487862451cc65c66a76)

uint8\_t length

**Definition** hci\_types.h:3250

[bt\_hci\_evt\_le\_per\_advertising\_report::data](structbt__hci__evt__le__per__advertising__report.md#a1f9cdfc01e46e59e957b0c557bae620a)

uint8\_t data[0]

**Definition** hci\_types.h:3251

[bt\_hci\_evt\_le\_per\_advertising\_report::tx\_power](structbt__hci__evt__le__per__advertising__report.md#a3a09aca94284a9e4af765d4da543698e)

int8\_t tx\_power

**Definition** hci\_types.h:3246

[bt\_hci\_evt\_le\_per\_advertising\_report::cte\_type](structbt__hci__evt__le__per__advertising__report.md#aa683d1a4bd3a851f26b3028f566b76e4)

uint8\_t cte\_type

**Definition** hci\_types.h:3248

[bt\_hci\_evt\_le\_per\_advertising\_report::data\_status](structbt__hci__evt__le__per__advertising__report.md#abf23b23a12cbfeb7f996e71e2fe8b11c)

uint8\_t data\_status

**Definition** hci\_types.h:3249

[bt\_hci\_evt\_le\_per\_advertising\_report::handle](structbt__hci__evt__le__per__advertising__report.md#af81ce5bb18ef7fa1d94d00412886b081)

uint16\_t handle

**Definition** hci\_types.h:3245

[bt\_hci\_evt\_le\_per\_advertising\_report::rssi](structbt__hci__evt__le__per__advertising__report.md#af874c29b89326877b499f6be1052a626)

int8\_t rssi

**Definition** hci\_types.h:3247

[bt\_hci\_evt\_le\_phy\_update\_complete](structbt__hci__evt__le__phy__update__complete.md)

**Definition** hci\_types.h:3185

[bt\_hci\_evt\_le\_phy\_update\_complete::handle](structbt__hci__evt__le__phy__update__complete.md#a70f472edef3b25fb23490ea6dcce9d43)

uint16\_t handle

**Definition** hci\_types.h:3187

[bt\_hci\_evt\_le\_phy\_update\_complete::status](structbt__hci__evt__le__phy__update__complete.md#a927a9e6982b29ecd4c3972b19a9bcdc2)

uint8\_t status

**Definition** hci\_types.h:3186

[bt\_hci\_evt\_le\_phy\_update\_complete::tx\_phy](structbt__hci__evt__le__phy__update__complete.md#ad184e10b7af71582db64ec5d3a66cff9)

uint8\_t tx\_phy

**Definition** hci\_types.h:3188

[bt\_hci\_evt\_le\_phy\_update\_complete::rx\_phy](structbt__hci__evt__le__phy__update__complete.md#ad792ffec08aa8e383009e2e353a03fcd)

uint8\_t rx\_phy

**Definition** hci\_types.h:3189

[bt\_hci\_evt\_le\_remote\_feat\_complete](structbt__hci__evt__le__remote__feat__complete.md)

**Definition** hci\_types.h:3115

[bt\_hci\_evt\_le\_remote\_feat\_complete::features](structbt__hci__evt__le__remote__feat__complete.md#a61101c21e317aa07b08725a7ffbb4b81)

uint8\_t features[8]

**Definition** hci\_types.h:3118

[bt\_hci\_evt\_le\_remote\_feat\_complete::status](structbt__hci__evt__le__remote__feat__complete.md#a8a80bade7644f986fec41462843d8319)

uint8\_t status

**Definition** hci\_types.h:3116

[bt\_hci\_evt\_le\_remote\_feat\_complete::handle](structbt__hci__evt__le__remote__feat__complete.md#a9a0da26d9415169f02b6c9472120afe7)

uint16\_t handle

**Definition** hci\_types.h:3117

[bt\_hci\_evt\_le\_req\_peer\_sca\_complete](structbt__hci__evt__le__req__peer__sca__complete.md)

**Definition** hci\_types.h:3427

[bt\_hci\_evt\_le\_req\_peer\_sca\_complete::status](structbt__hci__evt__le__req__peer__sca__complete.md#a814d17b8aae9dd68f57402c857ca1810)

uint8\_t status

**Definition** hci\_types.h:3428

[bt\_hci\_evt\_le\_req\_peer\_sca\_complete::sca](structbt__hci__evt__le__req__peer__sca__complete.md#a88f93ead6ec67e1612b1a0e8402a30e7)

uint8\_t sca

**Definition** hci\_types.h:3430

[bt\_hci\_evt\_le\_req\_peer\_sca\_complete::handle](structbt__hci__evt__le__req__peer__sca__complete.md#ab6b648e7f4bff9e84b274e9e22a26166)

uint16\_t handle

**Definition** hci\_types.h:3429

[bt\_hci\_evt\_le\_scan\_req\_received](structbt__hci__evt__le__scan__req__received.md)

**Definition** hci\_types.h:3270

[bt\_hci\_evt\_le\_scan\_req\_received::handle](structbt__hci__evt__le__scan__req__received.md#a62c6d5e5b7079665c0aea8eb676a0433)

uint8\_t handle

**Definition** hci\_types.h:3271

[bt\_hci\_evt\_le\_scan\_req\_received::addr](structbt__hci__evt__le__scan__req__received.md#a7dca5ad876dc97859a139d8bd4b207af)

bt\_addr\_le\_t addr

**Definition** hci\_types.h:3272

[bt\_hci\_evt\_le\_subrate\_change](structbt__hci__evt__le__subrate__change.md)

**Definition** hci\_types.h:3488

[bt\_hci\_evt\_le\_subrate\_change::supervision\_timeout](structbt__hci__evt__le__subrate__change.md#a2ad4a06feeb0d6d36461b4a4e53dfeb1)

uint16\_t supervision\_timeout

**Definition** hci\_types.h:3494

[bt\_hci\_evt\_le\_subrate\_change::continuation\_number](structbt__hci__evt__le__subrate__change.md#a712b8b818115f1797787aab229040c8a)

uint16\_t continuation\_number

**Definition** hci\_types.h:3493

[bt\_hci\_evt\_le\_subrate\_change::subrate\_factor](structbt__hci__evt__le__subrate__change.md#a9387ffe45a856f7f443f5116a59a9ff2)

uint16\_t subrate\_factor

**Definition** hci\_types.h:3491

[bt\_hci\_evt\_le\_subrate\_change::peripheral\_latency](structbt__hci__evt__le__subrate__change.md#a95aaed5f8c93a1d6e8cab4c7ebfad8d7)

uint16\_t peripheral\_latency

**Definition** hci\_types.h:3492

[bt\_hci\_evt\_le\_subrate\_change::status](structbt__hci__evt__le__subrate__change.md#aa49286a63d565feaf3d9329cd024ee9f)

uint8\_t status

**Definition** hci\_types.h:3489

[bt\_hci\_evt\_le\_subrate\_change::handle](structbt__hci__evt__le__subrate__change.md#adc08125e663a99c7232d0755c4bd760b)

uint16\_t handle

**Definition** hci\_types.h:3490

[bt\_hci\_evt\_le\_transmit\_power\_report](structbt__hci__evt__le__transmit__power__report.md)

**Definition** hci\_types.h:3455

[bt\_hci\_evt\_le\_transmit\_power\_report::tx\_power\_level\_flag](structbt__hci__evt__le__transmit__power__report.md#a2dc33da8f36cceda362d0c87098b02d6)

uint8\_t tx\_power\_level\_flag

**Definition** hci\_types.h:3461

[bt\_hci\_evt\_le\_transmit\_power\_report::reason](structbt__hci__evt__le__transmit__power__report.md#a341cc0c5cc1ea969e2024b67056a5439)

uint8\_t reason

**Definition** hci\_types.h:3458

[bt\_hci\_evt\_le\_transmit\_power\_report::handle](structbt__hci__evt__le__transmit__power__report.md#a4feadb14800c1b51a9cc523c1d6a9063)

uint16\_t handle

**Definition** hci\_types.h:3457

[bt\_hci\_evt\_le\_transmit\_power\_report::tx\_power\_level](structbt__hci__evt__le__transmit__power__report.md#aa0df9c50a555fa40ed25a14f7b6a5e77)

int8\_t tx\_power\_level

**Definition** hci\_types.h:3460

[bt\_hci\_evt\_le\_transmit\_power\_report::delta](structbt__hci__evt__le__transmit__power__report.md#ac42d60325235f517728ff44385361db2)

int8\_t delta

**Definition** hci\_types.h:3462

[bt\_hci\_evt\_le\_transmit\_power\_report::phy](structbt__hci__evt__le__transmit__power__report.md#ad6130863713cf31a1cbe33de9fb5428f)

uint8\_t phy

**Definition** hci\_types.h:3459

[bt\_hci\_evt\_le\_transmit\_power\_report::status](structbt__hci__evt__le__transmit__power__report.md#af1629e59dd651e1616b89f4958f47c92)

uint8\_t status

**Definition** hci\_types.h:3456

[bt\_hci\_evt\_link\_key\_notify](structbt__hci__evt__link__key__notify.md)

**Definition** hci\_types.h:2869

[bt\_hci\_evt\_link\_key\_notify::bdaddr](structbt__hci__evt__link__key__notify.md#a02647d66142c037b8bca2e748bc15319)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:2870

[bt\_hci\_evt\_link\_key\_notify::link\_key](structbt__hci__evt__link__key__notify.md#a4a1b50d8874d01a6a5dc5c52524c9bed)

uint8\_t link\_key[16]

**Definition** hci\_types.h:2871

[bt\_hci\_evt\_link\_key\_notify::key\_type](structbt__hci__evt__link__key__notify.md#a664580660a690af0d9ae3a62d79ad94b)

uint8\_t key\_type

**Definition** hci\_types.h:2872

[bt\_hci\_evt\_link\_key\_req](structbt__hci__evt__link__key__req.md)

**Definition** hci\_types.h:2853

[bt\_hci\_evt\_link\_key\_req::bdaddr](structbt__hci__evt__link__key__req.md#aed882dfb6b632383543bd7e60536ccc6)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:2854

[bt\_hci\_evt\_num\_completed\_packets](structbt__hci__evt__num__completed__packets.md)

**Definition** hci\_types.h:2842

[bt\_hci\_evt\_num\_completed\_packets::num\_handles](structbt__hci__evt__num__completed__packets.md#a666ed2c19596a89ab0c77275cbe18d1e)

uint8\_t num\_handles

**Definition** hci\_types.h:2843

[bt\_hci\_evt\_num\_completed\_packets::h](structbt__hci__evt__num__completed__packets.md#a94fb176924f7e844704be28851366052)

struct bt\_hci\_handle\_count h[0]

**Definition** hci\_types.h:2844

[bt\_hci\_evt\_pin\_code\_req](structbt__hci__evt__pin__code__req.md)

**Definition** hci\_types.h:2848

[bt\_hci\_evt\_pin\_code\_req::bdaddr](structbt__hci__evt__pin__code__req.md#a8649a30cd8c7ecf9ee006ddc2e625908)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:2849

[bt\_hci\_evt\_remote\_ext\_features](structbt__hci__evt__remote__ext__features.md)

**Definition** hci\_types.h:2896

[bt\_hci\_evt\_remote\_ext\_features::handle](structbt__hci__evt__remote__ext__features.md#a0191b80b4f4d5360972faa6d5edf5055)

uint16\_t handle

**Definition** hci\_types.h:2898

[bt\_hci\_evt\_remote\_ext\_features::features](structbt__hci__evt__remote__ext__features.md#a084199f8e30669c2a1a631af26c0d69a)

uint8\_t features[8]

**Definition** hci\_types.h:2901

[bt\_hci\_evt\_remote\_ext\_features::status](structbt__hci__evt__remote__ext__features.md#a4f1d489aaa5626e485d34a9ae4cf9a34)

uint8\_t status

**Definition** hci\_types.h:2897

[bt\_hci\_evt\_remote\_ext\_features::page](structbt__hci__evt__remote__ext__features.md#aeece2b8d46f4a3713d63df29058f2d9c)

uint8\_t page

**Definition** hci\_types.h:2899

[bt\_hci\_evt\_remote\_ext\_features::max\_page](structbt__hci__evt__remote__ext__features.md#afa577407f4ded5404394f42e7c73e10b)

uint8\_t max\_page

**Definition** hci\_types.h:2900

[bt\_hci\_evt\_remote\_features](structbt__hci__evt__remote__features.md)

**Definition** hci\_types.h:2797

[bt\_hci\_evt\_remote\_features::status](structbt__hci__evt__remote__features.md#a2cedd8392c87914272ff250a56c80574)

uint8\_t status

**Definition** hci\_types.h:2798

[bt\_hci\_evt\_remote\_features::features](structbt__hci__evt__remote__features.md#a70c97b9fbf7c363eab7b27f3a4e86e96)

uint8\_t features[8]

**Definition** hci\_types.h:2800

[bt\_hci\_evt\_remote\_features::handle](structbt__hci__evt__remote__features.md#ada0249bdb7108c5d347fea1218c4f878)

uint16\_t handle

**Definition** hci\_types.h:2799

[bt\_hci\_evt\_remote\_name\_req\_complete](structbt__hci__evt__remote__name__req__complete.md)

**Definition** hci\_types.h:2783

[bt\_hci\_evt\_remote\_name\_req\_complete::bdaddr](structbt__hci__evt__remote__name__req__complete.md#a380121873bf059b7c8a4abdf212f4235)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:2785

[bt\_hci\_evt\_remote\_name\_req\_complete::name](structbt__hci__evt__remote__name__req__complete.md#a3e54674692f7fc1670fa389e293714c7)

uint8\_t name[248]

**Definition** hci\_types.h:2786

[bt\_hci\_evt\_remote\_name\_req\_complete::status](structbt__hci__evt__remote__name__req__complete.md#ab43d4a3c19d829b829cc7b40a67959f3)

uint8\_t status

**Definition** hci\_types.h:2784

[bt\_hci\_evt\_remote\_version\_info](structbt__hci__evt__remote__version__info.md)

**Definition** hci\_types.h:2804

[bt\_hci\_evt\_remote\_version\_info::subversion](structbt__hci__evt__remote__version__info.md#a02188119418a5a6dd8a4d0c37f5a060d)

uint16\_t subversion

**Definition** hci\_types.h:2809

[bt\_hci\_evt\_remote\_version\_info::handle](structbt__hci__evt__remote__version__info.md#a1703a9ac9a5e1ba3ed396fe5799f9f51)

uint16\_t handle

**Definition** hci\_types.h:2806

[bt\_hci\_evt\_remote\_version\_info::status](structbt__hci__evt__remote__version__info.md#a196f9489183d6e0116ff687df66c60c0)

uint8\_t status

**Definition** hci\_types.h:2805

[bt\_hci\_evt\_remote\_version\_info::version](structbt__hci__evt__remote__version__info.md#a8442b9f2bdc6cbce564c9bcec4169a20)

uint8\_t version

**Definition** hci\_types.h:2807

[bt\_hci\_evt\_remote\_version\_info::manufacturer](structbt__hci__evt__remote__version__info.md#aaa9c3875143700b6ed013715cb3c7107)

uint16\_t manufacturer

**Definition** hci\_types.h:2808

[bt\_hci\_evt\_role\_change](structbt__hci__evt__role__change.md)

**Definition** hci\_types.h:2835

[bt\_hci\_evt\_role\_change::bdaddr](structbt__hci__evt__role__change.md#a18dd22435ae40fcf1c4fd2b90b402c60)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:2837

[bt\_hci\_evt\_role\_change::role](structbt__hci__evt__role__change.md#a2e5736d63e30326c33bec8ebdf986c62)

uint8\_t role

**Definition** hci\_types.h:2838

[bt\_hci\_evt\_role\_change::status](structbt__hci__evt__role__change.md#aafe1a9e43a9a42d4030846180e55b8ef)

uint8\_t status

**Definition** hci\_types.h:2836

[bt\_hci\_evt\_ssp\_complete](structbt__hci__evt__ssp__complete.md)

**Definition** hci\_types.h:3048

[bt\_hci\_evt\_ssp\_complete::status](structbt__hci__evt__ssp__complete.md#a33d3d47c1cef71cfb787a1195d9b4ec2)

uint8\_t status

**Definition** hci\_types.h:3049

[bt\_hci\_evt\_ssp\_complete::bdaddr](structbt__hci__evt__ssp__complete.md#a5030cf334f97cdd982001b3278ed9db1)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:3050

[bt\_hci\_evt\_sync\_conn\_complete](structbt__hci__evt__sync__conn__complete.md)

**Definition** hci\_types.h:2993

[bt\_hci\_evt\_sync\_conn\_complete::tx\_interval](structbt__hci__evt__sync__conn__complete.md#a4b93873ad6f5388657511d87fc0a8c85)

uint8\_t tx\_interval

**Definition** hci\_types.h:2998

[bt\_hci\_evt\_sync\_conn\_complete::air\_mode](structbt__hci__evt__sync__conn__complete.md#a5f6068569bf649bcd1d13928f56f9703)

uint8\_t air\_mode

**Definition** hci\_types.h:3002

[bt\_hci\_evt\_sync\_conn\_complete::retansmission\_window](structbt__hci__evt__sync__conn__complete.md#a68a31880c8aab9245be043c1719464d3)

uint8\_t retansmission\_window

**Definition** hci\_types.h:2999

[bt\_hci\_evt\_sync\_conn\_complete::rx\_pkt\_length](structbt__hci__evt__sync__conn__complete.md#a6a455f56da4666cb602e6c05157e166d)

uint16\_t rx\_pkt\_length

**Definition** hci\_types.h:3000

[bt\_hci\_evt\_sync\_conn\_complete::bdaddr](structbt__hci__evt__sync__conn__complete.md#a78f5560783400f1d1a63b2c9d69fa7ed)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:2996

[bt\_hci\_evt\_sync\_conn\_complete::handle](structbt__hci__evt__sync__conn__complete.md#aa48aa29ff73e93e8d961013f066c1b5e)

uint16\_t handle

**Definition** hci\_types.h:2995

[bt\_hci\_evt\_sync\_conn\_complete::link\_type](structbt__hci__evt__sync__conn__complete.md#aacf9919945e9b755913da145f0fe78ae)

uint8\_t link\_type

**Definition** hci\_types.h:2997

[bt\_hci\_evt\_sync\_conn\_complete::tx\_pkt\_length](structbt__hci__evt__sync__conn__complete.md#ab4d4106d5120f10e8300834db12740d8)

uint16\_t tx\_pkt\_length

**Definition** hci\_types.h:3001

[bt\_hci\_evt\_sync\_conn\_complete::status](structbt__hci__evt__sync__conn__complete.md#accd17a95f35ab1988122df7584830f60)

uint8\_t status

**Definition** hci\_types.h:2994

[bt\_hci\_evt\_user\_confirm\_req](structbt__hci__evt__user__confirm__req.md)

**Definition** hci\_types.h:3037

[bt\_hci\_evt\_user\_confirm\_req::bdaddr](structbt__hci__evt__user__confirm__req.md#aaeec83c50764c322af7cd64259e54a97)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:3038

[bt\_hci\_evt\_user\_confirm\_req::passkey](structbt__hci__evt__user__confirm__req.md#ac333729f5a7d9241ac26aeb7d3f77935)

uint32\_t passkey

**Definition** hci\_types.h:3039

[bt\_hci\_evt\_user\_passkey\_notify](structbt__hci__evt__user__passkey__notify.md)

**Definition** hci\_types.h:3054

[bt\_hci\_evt\_user\_passkey\_notify::passkey](structbt__hci__evt__user__passkey__notify.md#a7f6a367e50d41cb7d8897db05db826be)

uint32\_t passkey

**Definition** hci\_types.h:3056

[bt\_hci\_evt\_user\_passkey\_notify::bdaddr](structbt__hci__evt__user__passkey__notify.md#af020e1cd131473fe06a193529a0499ac)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:3055

[bt\_hci\_evt\_user\_passkey\_req](structbt__hci__evt__user__passkey__req.md)

**Definition** hci\_types.h:3043

[bt\_hci\_evt\_user\_passkey\_req::bdaddr](structbt__hci__evt__user__passkey__req.md#a7f1005423296906e0374050bc30781ce)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:3044

[bt\_hci\_ext\_adv\_set](structbt__hci__ext__adv__set.md)

**Definition** hci\_types.h:1601

[bt\_hci\_ext\_adv\_set::max\_ext\_adv\_evts](structbt__hci__ext__adv__set.md#a4467ac9a564ea24bb701de46cda2579a)

uint8\_t max\_ext\_adv\_evts

**Definition** hci\_types.h:1604

[bt\_hci\_ext\_adv\_set::handle](structbt__hci__ext__adv__set.md#a9d0fd3f6659db172ff4efd74c2c2d216)

uint8\_t handle

**Definition** hci\_types.h:1602

[bt\_hci\_ext\_adv\_set::duration](structbt__hci__ext__adv__set.md#acc2afc91fe5c0dfcb4c95eaade4a047a)

uint16\_t duration

**Definition** hci\_types.h:1603

[bt\_hci\_ext\_conn\_phy](structbt__hci__ext__conn__phy.md)

**Definition** hci\_types.h:1698

[bt\_hci\_ext\_conn\_phy::max\_ce\_len](structbt__hci__ext__conn__phy.md#a3c3ccb93014758b3215718d2672ce7f3)

uint16\_t max\_ce\_len

**Definition** hci\_types.h:1706

[bt\_hci\_ext\_conn\_phy::scan\_interval](structbt__hci__ext__conn__phy.md#a4f78503fe42ee81fea740ba1643a732e)

uint16\_t scan\_interval

**Definition** hci\_types.h:1699

[bt\_hci\_ext\_conn\_phy::conn\_interval\_max](structbt__hci__ext__conn__phy.md#a7bcf66a3372d92c809d8427796915b88)

uint16\_t conn\_interval\_max

**Definition** hci\_types.h:1702

[bt\_hci\_ext\_conn\_phy::conn\_latency](structbt__hci__ext__conn__phy.md#a7dd57b7ef0b13b15da47e92076f87d79)

uint16\_t conn\_latency

**Definition** hci\_types.h:1703

[bt\_hci\_ext\_conn\_phy::conn\_interval\_min](structbt__hci__ext__conn__phy.md#a7fc06c1a458aedb6b29381450a5a4df0)

uint16\_t conn\_interval\_min

**Definition** hci\_types.h:1701

[bt\_hci\_ext\_conn\_phy::supervision\_timeout](structbt__hci__ext__conn__phy.md#aaec54c0743dfc08923b5ccd8fc1a4015)

uint16\_t supervision\_timeout

**Definition** hci\_types.h:1704

[bt\_hci\_ext\_conn\_phy::scan\_window](structbt__hci__ext__conn__phy.md#ae0e950c8004bd595631f95a289a5c871)

uint16\_t scan\_window

**Definition** hci\_types.h:1700

[bt\_hci\_ext\_conn\_phy::min\_ce\_len](structbt__hci__ext__conn__phy.md#af48212961ce21f5222e57f70ffeb811b)

uint16\_t min\_ce\_len

**Definition** hci\_types.h:1705

[bt\_hci\_ext\_scan\_phy](structbt__hci__ext__scan__phy.md)

**Definition** hci\_types.h:1668

[bt\_hci\_ext\_scan\_phy::interval](structbt__hci__ext__scan__phy.md#a2f087d18bde86d0ac81a14a09ae5b9b0)

uint16\_t interval

**Definition** hci\_types.h:1670

[bt\_hci\_ext\_scan\_phy::type](structbt__hci__ext__scan__phy.md#a4cfebc7b2709973953bed9a09a793b7e)

uint8\_t type

**Definition** hci\_types.h:1669

[bt\_hci\_ext\_scan\_phy::window](structbt__hci__ext__scan__phy.md#a9c0196f0d5f0064796c15a5df2ad4c07)

uint16\_t window

**Definition** hci\_types.h:1671

[bt\_hci\_handle\_count](structbt__hci__handle__count.md)

**Definition** hci\_types.h:756

[bt\_hci\_handle\_count::count](structbt__hci__handle__count.md#a71577f376985909744fa14f246e69e1d)

uint16\_t count

**Definition** hci\_types.h:758

[bt\_hci\_handle\_count::handle](structbt__hci__handle__count.md#acacc000905835724b7fe882a8ad85f82)

uint16\_t handle

**Definition** hci\_types.h:757

[bt\_hci\_iso\_hdr](structbt__hci__iso__hdr.md)

**Definition** hci\_types.h:125

[bt\_hci\_iso\_hdr::len](structbt__hci__iso__hdr.md#ab33ae914a9eba85b35c78e45e0f5255f)

uint16\_t len

**Definition** hci\_types.h:127

[bt\_hci\_iso\_hdr::handle](structbt__hci__iso__hdr.md#af5113383fbcd0e70828f986720c38572)

uint16\_t handle

**Definition** hci\_types.h:126

[bt\_hci\_iso\_sdu\_hdr](structbt__hci__iso__sdu__hdr.md)

**Definition** hci\_types.h:112

[bt\_hci\_iso\_sdu\_hdr::slen](structbt__hci__iso__sdu__hdr.md#a626764862a3757a3119b6de799221ad1)

uint16\_t slen

**Definition** hci\_types.h:114

[bt\_hci\_iso\_sdu\_hdr::sn](structbt__hci__iso__sdu__hdr.md#a683d493de5d00e3b4c5169f6de498c13)

uint16\_t sn

**Definition** hci\_types.h:113

[bt\_hci\_iso\_sdu\_ts\_hdr](structbt__hci__iso__sdu__ts__hdr.md)

**Definition** hci\_types.h:118

[bt\_hci\_iso\_sdu\_ts\_hdr::sdu](structbt__hci__iso__sdu__ts__hdr.md#a3f81175b95f8eaeeeee71ee4bf401864)

struct bt\_hci\_iso\_sdu\_hdr sdu

**Definition** hci\_types.h:120

[bt\_hci\_iso\_sdu\_ts\_hdr::ts](structbt__hci__iso__sdu__ts__hdr.md#a657e03c5ef597f04cc21725f0bc227d4)

uint32\_t ts

**Definition** hci\_types.h:119

[bt\_hci\_le\_cs\_step\_data\_mode\_0\_initiator](structbt__hci__le__cs__step__data__mode__0__initiator.md)

Subevent result step data format: Mode 0 Initiator.

**Definition** hci\_types.h:3711

[bt\_hci\_le\_cs\_step\_data\_mode\_0\_initiator::packet\_rssi](structbt__hci__le__cs__step__data__mode__0__initiator.md#a11edf6e1c1da5d24aa1136521a249f52)

uint8\_t packet\_rssi

**Definition** hci\_types.h:3719

[bt\_hci\_le\_cs\_step\_data\_mode\_0\_initiator::packet\_quality\_bit\_errors](structbt__hci__le__cs__step__data__mode__0__initiator.md#a339252cacafd05e85c0fb19776343e17)

uint8\_t packet\_quality\_bit\_errors

**Definition** hci\_types.h:3716

[bt\_hci\_le\_cs\_step\_data\_mode\_0\_initiator::measured\_freq\_offset](structbt__hci__le__cs__step__data__mode__0__initiator.md#a48fc1fd87869d4ca2b70c42d5c4e1d75)

uint16\_t measured\_freq\_offset

**Definition** hci\_types.h:3721

[bt\_hci\_le\_cs\_step\_data\_mode\_0\_initiator::packet\_quality\_aa\_check](structbt__hci__le__cs__step__data__mode__0__initiator.md#a811eb38a04e63b12be9e25291126ccc1)

uint8\_t packet\_quality\_aa\_check

**Definition** hci\_types.h:3717

[bt\_hci\_le\_cs\_step\_data\_mode\_0\_initiator::packet\_antenna](structbt__hci__le__cs__step__data__mode__0__initiator.md#ad9a2193cbe5381d30494dbf6f8d84482)

uint8\_t packet\_antenna

**Definition** hci\_types.h:3720

[bt\_hci\_le\_cs\_step\_data\_mode\_0\_reflector](structbt__hci__le__cs__step__data__mode__0__reflector.md)

Subevent result step data format: Mode 0 Reflector.

**Definition** hci\_types.h:3725

[bt\_hci\_le\_cs\_step\_data\_mode\_0\_reflector::packet\_quality\_bit\_errors](structbt__hci__le__cs__step__data__mode__0__reflector.md#a16fb71660c4f4afb1c36765fdbd2a96a)

uint8\_t packet\_quality\_bit\_errors

**Definition** hci\_types.h:3730

[bt\_hci\_le\_cs\_step\_data\_mode\_0\_reflector::packet\_quality\_aa\_check](structbt__hci__le__cs__step__data__mode__0__reflector.md#a9c34ecf0b79449754da1d1ba925b1ff2)

uint8\_t packet\_quality\_aa\_check

**Definition** hci\_types.h:3731

[bt\_hci\_le\_cs\_step\_data\_mode\_0\_reflector::packet\_rssi](structbt__hci__le__cs__step__data__mode__0__reflector.md#aa058afab8cba3f5ce572b8e7d29ef34d)

uint8\_t packet\_rssi

**Definition** hci\_types.h:3733

[bt\_hci\_le\_cs\_step\_data\_mode\_0\_reflector::packet\_antenna](structbt__hci__le__cs__step__data__mode__0__reflector.md#ad045baeaf6fbb75de002ffedc4b1a831)

uint8\_t packet\_antenna

**Definition** hci\_types.h:3734

[bt\_hci\_le\_cs\_step\_data\_mode\_1\_ss\_rtt](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md)

Subevent result step data format: Mode 1 with sounding sequence RTT support.

**Definition** hci\_types.h:3756

[bt\_hci\_le\_cs\_step\_data\_mode\_1\_ss\_rtt::packet\_pct1](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#a3f8ba85b776f732ebc1086a4317849a1)

uint8\_t packet\_pct1[4]

**Definition** hci\_types.h:3771

[bt\_hci\_le\_cs\_step\_data\_mode\_1\_ss\_rtt::packet\_nadm](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#a511b281fb1c16fd7d0eaf731906a4292)

uint8\_t packet\_nadm

**Definition** hci\_types.h:3764

[bt\_hci\_le\_cs\_step\_data\_mode\_1\_ss\_rtt::packet\_quality\_bit\_errors](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#a515fde1d568a19ccf6ebefe9052866a4)

uint8\_t packet\_quality\_bit\_errors

**Definition** hci\_types.h:3761

[bt\_hci\_le\_cs\_step\_data\_mode\_1\_ss\_rtt::packet\_rssi](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#a5ec9c30063c09285804973008533e5cb)

uint8\_t packet\_rssi

**Definition** hci\_types.h:3765

[bt\_hci\_le\_cs\_step\_data\_mode\_1\_ss\_rtt::toa\_tod\_initiator](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#a77bbcd9451360ad97813f9357e44766e)

int16\_t toa\_tod\_initiator

**Definition** hci\_types.h:3767

[bt\_hci\_le\_cs\_step\_data\_mode\_1\_ss\_rtt::packet\_pct2](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#a9f969aa6fc134a9e618d07f177d2b7fd)

uint8\_t packet\_pct2[4]

**Definition** hci\_types.h:3772

[bt\_hci\_le\_cs\_step\_data\_mode\_1\_ss\_rtt::packet\_antenna](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#abf20351ab0eaf3a7139a464f1d1a72b0)

uint8\_t packet\_antenna

**Definition** hci\_types.h:3770

[bt\_hci\_le\_cs\_step\_data\_mode\_1\_ss\_rtt::tod\_toa\_reflector](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#ace3843bc24616950f04150b2f86abad4)

int16\_t tod\_toa\_reflector

**Definition** hci\_types.h:3768

[bt\_hci\_le\_cs\_step\_data\_mode\_1\_ss\_rtt::packet\_quality\_aa\_check](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md#ad8f9ca9dda852b435848b988ad872797)

uint8\_t packet\_quality\_aa\_check

**Definition** hci\_types.h:3762

[bt\_hci\_le\_cs\_step\_data\_mode\_1](structbt__hci__le__cs__step__data__mode__1.md)

Subevent result step data format: Mode 1.

**Definition** hci\_types.h:3738

[bt\_hci\_le\_cs\_step\_data\_mode\_1::packet\_quality\_bit\_errors](structbt__hci__le__cs__step__data__mode__1.md#a0cb4198466318a7a15cbbb172c582eeb)

uint8\_t packet\_quality\_bit\_errors

**Definition** hci\_types.h:3743

[bt\_hci\_le\_cs\_step\_data\_mode\_1::toa\_tod\_initiator](structbt__hci__le__cs__step__data__mode__1.md#a1365e601f422b98747f9909d3be56b60)

int16\_t toa\_tod\_initiator

**Definition** hci\_types.h:3749

[bt\_hci\_le\_cs\_step\_data\_mode\_1::packet\_rssi](structbt__hci__le__cs__step__data__mode__1.md#a1b9df39c01ab91ab225c809db5066f70)

uint8\_t packet\_rssi

**Definition** hci\_types.h:3747

[bt\_hci\_le\_cs\_step\_data\_mode\_1::packet\_nadm](structbt__hci__le__cs__step__data__mode__1.md#a4025cf2b229ada27e258d3d519a7b1dd)

uint8\_t packet\_nadm

**Definition** hci\_types.h:3746

[bt\_hci\_le\_cs\_step\_data\_mode\_1::packet\_quality\_aa\_check](structbt__hci__le__cs__step__data__mode__1.md#a8383926e95cd9d222b91704b2ca6883e)

uint8\_t packet\_quality\_aa\_check

**Definition** hci\_types.h:3744

[bt\_hci\_le\_cs\_step\_data\_mode\_1::tod\_toa\_reflector](structbt__hci__le__cs__step__data__mode__1.md#ab3425181b2a625fcfbbfd14477d717d1)

int16\_t tod\_toa\_reflector

**Definition** hci\_types.h:3750

[bt\_hci\_le\_cs\_step\_data\_mode\_1::packet\_antenna](structbt__hci__le__cs__step__data__mode__1.md#afc8221a5cab14d3842590e6cac52da4d)

uint8\_t packet\_antenna

**Definition** hci\_types.h:3752

[bt\_hci\_le\_cs\_step\_data\_mode\_2](structbt__hci__le__cs__step__data__mode__2.md)

Subevent result step data format: Mode 2.

**Definition** hci\_types.h:3789

[bt\_hci\_le\_cs\_step\_data\_mode\_2::antenna\_permutation\_index](structbt__hci__le__cs__step__data__mode__2.md#a9feb2b07f8862aa24772a733f451f7a8)

uint8\_t antenna\_permutation\_index

**Definition** hci\_types.h:3790

[bt\_hci\_le\_cs\_step\_data\_mode\_2::tone\_info](structbt__hci__le__cs__step__data__mode__2.md#aef5699cb9bfc522a12be9a284392fd0e)

struct bt\_hci\_le\_cs\_step\_data\_tone\_info tone\_info[]

**Definition** hci\_types.h:3791

[bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md)

Subevent result step data format: Mode 3 with sounding sequence RTT support.

**Definition** hci\_types.h:3815

[bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt::packet\_quality\_aa\_check](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#a657ec3570e3ad6b2ddab87bada231587)

uint8\_t packet\_quality\_aa\_check

**Definition** hci\_types.h:3821

[bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt::packet\_antenna](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#a9ce412ad8b18a9315b858cf1fe2a466a)

uint8\_t packet\_antenna

**Definition** hci\_types.h:3829

[bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt::packet\_nadm](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#a9d2428083c401d931520addde0af54fd)

uint8\_t packet\_nadm

**Definition** hci\_types.h:3823

[bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt::packet\_pct1](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#aada8b3ff1bb0d0b9eccb846da173b3f4)

uint8\_t packet\_pct1[4]

**Definition** hci\_types.h:3830

[bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt::antenna\_permutation\_index](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#ac4067e27caa12cf9f8c6525bf6a72973)

uint8\_t antenna\_permutation\_index

**Definition** hci\_types.h:3832

[bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt::tod\_toa\_reflector](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#ada4d52f54f1efa804a812c65edd8f125)

int16\_t tod\_toa\_reflector

**Definition** hci\_types.h:3827

[bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt::packet\_rssi](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#adc4fe32bc6b7515e5bf1055f19f1a2bd)

uint8\_t packet\_rssi

**Definition** hci\_types.h:3824

[bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt::toa\_tod\_initiator](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#ae2181a568ed6da32d3f60ba6d271c64f)

int16\_t toa\_tod\_initiator

**Definition** hci\_types.h:3826

[bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt::tone\_info](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#aea13fc3e16092dcede9fb46ea719f21c)

struct bt\_hci\_le\_cs\_step\_data\_tone\_info tone\_info[]

**Definition** hci\_types.h:3833

[bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt::packet\_quality\_bit\_errors](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#af5d8a8559400b45066bdac86fbdac411)

uint8\_t packet\_quality\_bit\_errors

**Definition** hci\_types.h:3820

[bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt::packet\_pct2](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md#afdebbafc06475dde12aaed73d2180f96)

uint8\_t packet\_pct2[4]

**Definition** hci\_types.h:3831

[bt\_hci\_le\_cs\_step\_data\_mode\_3](structbt__hci__le__cs__step__data__mode__3.md)

Subevent result step data format: Mode 3.

**Definition** hci\_types.h:3795

[bt\_hci\_le\_cs\_step\_data\_mode\_3::toa\_tod\_initiator](structbt__hci__le__cs__step__data__mode__3.md#a183f3ee64a4482c9d3e0f041151fdcf9)

int16\_t toa\_tod\_initiator

**Definition** hci\_types.h:3806

[bt\_hci\_le\_cs\_step\_data\_mode\_3::packet\_quality\_bit\_errors](structbt__hci__le__cs__step__data__mode__3.md#a42b8bdf1fd492be1daded674e3d733d6)

uint8\_t packet\_quality\_bit\_errors

**Definition** hci\_types.h:3800

[bt\_hci\_le\_cs\_step\_data\_mode\_3::packet\_rssi](structbt__hci__le__cs__step__data__mode__3.md#a60750ac38bf019a0c7a8656ca59fc402)

uint8\_t packet\_rssi

**Definition** hci\_types.h:3804

[bt\_hci\_le\_cs\_step\_data\_mode\_3::antenna\_permutation\_index](structbt__hci__le__cs__step__data__mode__3.md#a609102fc9d42fe73c09907f54526bd40)

uint8\_t antenna\_permutation\_index

**Definition** hci\_types.h:3810

[bt\_hci\_le\_cs\_step\_data\_mode\_3::tone\_info](structbt__hci__le__cs__step__data__mode__3.md#a9ae78aa83a22f0618491871d55f2f0b9)

struct bt\_hci\_le\_cs\_step\_data\_tone\_info tone\_info[]

**Definition** hci\_types.h:3811

[bt\_hci\_le\_cs\_step\_data\_mode\_3::packet\_nadm](structbt__hci__le__cs__step__data__mode__3.md#a9b7373e7d3faa0cb5553d4f897c94ebc)

uint8\_t packet\_nadm

**Definition** hci\_types.h:3803

[bt\_hci\_le\_cs\_step\_data\_mode\_3::tod\_toa\_reflector](structbt__hci__le__cs__step__data__mode__3.md#aa0f1918115a6e550d6fab17529bbb4f2)

int16\_t tod\_toa\_reflector

**Definition** hci\_types.h:3807

[bt\_hci\_le\_cs\_step\_data\_mode\_3::packet\_antenna](structbt__hci__le__cs__step__data__mode__3.md#ad20e9c1deba67aa5759881b52d13311d)

uint8\_t packet\_antenna

**Definition** hci\_types.h:3809

[bt\_hci\_le\_cs\_step\_data\_mode\_3::packet\_quality\_aa\_check](structbt__hci__le__cs__step__data__mode__3.md#ad4c30784cc2586b5b8dcfa22e7a1f8fb)

uint8\_t packet\_quality\_aa\_check

**Definition** hci\_types.h:3801

[bt\_hci\_le\_cs\_step\_data\_tone\_info](structbt__hci__le__cs__step__data__tone__info.md)

Format for per-antenna path step data in modes 2 and 3.

**Definition** hci\_types.h:3777

[bt\_hci\_le\_cs\_step\_data\_tone\_info::quality\_indicator](structbt__hci__le__cs__step__data__tone__info.md#a4d31c0759c17789cb4b9bdc90a8870ca)

uint8\_t quality\_indicator

**Definition** hci\_types.h:3784

[bt\_hci\_le\_cs\_step\_data\_tone\_info::extension\_indicator](structbt__hci__le__cs__step__data__tone__info.md#a5f2e5e95b97d2be49a8ff1d9376892e8)

uint8\_t extension\_indicator

**Definition** hci\_types.h:3783

[bt\_hci\_le\_cs\_step\_data\_tone\_info::phase\_correction\_term](structbt__hci__le__cs__step__data__tone__info.md#aeb76aeb54cb4e5613496431ec6d0093a)

uint8\_t phase\_correction\_term[3]

**Definition** hci\_types.h:3778

[bt\_hci\_le\_iq\_sample](structbt__hci__le__iq__sample.md)

**Definition** hci\_types.h:3295

[bt\_hci\_le\_iq\_sample::q](structbt__hci__le__iq__sample.md#a775b6e0ab1842594bc00998faec613f3)

int8\_t q

**Definition** hci\_types.h:3297

[bt\_hci\_le\_iq\_sample::i](structbt__hci__le__iq__sample.md#aacf452456eecd4ad4dab083593b11104)

int8\_t i

**Definition** hci\_types.h:3296

[bt\_hci\_op\_inquiry](structbt__hci__op__inquiry.md)

**Definition** hci\_types.h:382

[bt\_hci\_op\_inquiry::lap](structbt__hci__op__inquiry.md#abdd03feccecbdbbb5d2c7c7f3213b62f)

uint8\_t lap[3]

**Definition** hci\_types.h:383

[bt\_hci\_op\_inquiry::num\_rsp](structbt__hci__op__inquiry.md#ac8ed23243dbd9a7c46fedd8abe9666f5)

uint8\_t num\_rsp

**Definition** hci\_types.h:385

[bt\_hci\_op\_inquiry::length](structbt__hci__op__inquiry.md#ae77fa706c9875b5568a4af26a7724d08)

uint8\_t length

**Definition** hci\_types.h:384

[bt\_hci\_op\_le\_cs\_test](structbt__hci__op__le__cs__test.md)

**Definition** hci\_types.h:2682

[bt\_hci\_op\_le\_cs\_test::t\_ip1\_time](structbt__hci__op__le__cs__test.md#a0675dfbb050838d98f21cfa28af8615b)

uint8\_t t\_ip1\_time

**Definition** hci\_types.h:2695

[bt\_hci\_op\_le\_cs\_test::sub\_mode\_type](structbt__hci__op__le__cs__test.md#a090c5d03cf829011196d644cd9f7c7db)

uint8\_t sub\_mode\_type

**Definition** hci\_types.h:2684

[bt\_hci\_op\_le\_cs\_test::t\_sw\_time](structbt__hci__op__le__cs__test.md#a09c40ecd0d4e325e0c0504a9d8cd977b)

uint8\_t t\_sw\_time

**Definition** hci\_types.h:2699

[bt\_hci\_op\_le\_cs\_test::override\_parameters\_data](structbt__hci__op__le__cs__test.md#a15a68fe7c98b2e242afd6eb67dd9b40a)

uint8\_t override\_parameters\_data[]

**Definition** hci\_types.h:2708

[bt\_hci\_op\_le\_cs\_test::max\_num\_subevents](structbt__hci__op__le__cs__test.md#a1c105f7a4d48754322fee6992db8c175)

uint8\_t max\_num\_subevents

**Definition** hci\_types.h:2693

[bt\_hci\_op\_le\_cs\_test::override\_parameters\_length](structbt__hci__op__le__cs__test.md#a373372a93d94e70d674c1c7b4c126734)

uint8\_t override\_parameters\_length

**Definition** hci\_types.h:2707

[bt\_hci\_op\_le\_cs\_test::snr\_control\_reflector](structbt__hci__op__le__cs__test.md#a3c949d9a7eb4f56427f6e9f8be7cb77b)

uint8\_t snr\_control\_reflector

**Definition** hci\_types.h:2703

[bt\_hci\_op\_le\_cs\_test::snr\_control\_initiator](structbt__hci__op__le__cs__test.md#a551c06e651180867dd1d23b3fdf4c031)

uint8\_t snr\_control\_initiator

**Definition** hci\_types.h:2702

[bt\_hci\_op\_le\_cs\_test::main\_mode\_repetition](structbt__hci__op__le__cs__test.md#a60cc9a7c46f8cd0933dc2f5a68cca627)

uint8\_t main\_mode\_repetition

**Definition** hci\_types.h:2685

[bt\_hci\_op\_le\_cs\_test::t\_ip2\_time](structbt__hci__op__le__cs__test.md#a7538e91b5ced2702965a21f8e754ebcc)

uint8\_t t\_ip2\_time

**Definition** hci\_types.h:2696

[bt\_hci\_op\_le\_cs\_test::subevent\_len](structbt__hci__op__le__cs__test.md#a8ad67a5a0138f32cc5295074011a3808)

uint8\_t subevent\_len[3]

**Definition** hci\_types.h:2691

[bt\_hci\_op\_le\_cs\_test::channel\_map\_repetition](structbt__hci__op__le__cs__test.md#a8c23c2e6e8c38bf33fcd6d1e343f5982)

uint8\_t channel\_map\_repetition

**Definition** hci\_types.h:2705

[bt\_hci\_op\_le\_cs\_test::reserved](structbt__hci__op__le__cs__test.md#a9021c55f8cddb741fb1f86317625723e)

uint8\_t reserved

**Definition** hci\_types.h:2701

[bt\_hci\_op\_le\_cs\_test::t\_pm\_time](structbt__hci__op__le__cs__test.md#a981da50e0594b8bc05f811e5170b10f5)

uint8\_t t\_pm\_time

**Definition** hci\_types.h:2698

[bt\_hci\_op\_le\_cs\_test::t\_fcs\_time](structbt__hci__op__le__cs__test.md#aa3d510663e5dcc44b5acd9d1c41746d5)

uint8\_t t\_fcs\_time

**Definition** hci\_types.h:2697

[bt\_hci\_op\_le\_cs\_test::mode\_0\_steps](structbt__hci__op__le__cs__test.md#aaf480890608b5cfc9151dac844e9a337)

uint8\_t mode\_0\_steps

**Definition** hci\_types.h:2686

[bt\_hci\_op\_le\_cs\_test::tone\_antenna\_config\_selection](structbt__hci__op__le__cs__test.md#acaa428a37e68ff56c311397e53f46526)

uint8\_t tone\_antenna\_config\_selection

**Definition** hci\_types.h:2700

[bt\_hci\_op\_le\_cs\_test::override\_config](structbt__hci__op__le__cs__test.md#acc2d0768b69e5f5b593e5aff71b17f20)

uint16\_t override\_config

**Definition** hci\_types.h:2706

[bt\_hci\_op\_le\_cs\_test::subevent\_interval](structbt__hci__op__le__cs__test.md#ad52cd2862d2544448a5e175c58541f89)

uint16\_t subevent\_interval

**Definition** hci\_types.h:2692

[bt\_hci\_op\_le\_cs\_test::transmit\_power\_level](structbt__hci__op__le__cs__test.md#adf2f24dc6988f1f0e0457a6cf3141521)

uint8\_t transmit\_power\_level

**Definition** hci\_types.h:2694

[bt\_hci\_op\_le\_cs\_test::rtt\_type](structbt__hci__op__le__cs__test.md#ae0234031d94e93653dd45e6e657c199f)

uint8\_t rtt\_type

**Definition** hci\_types.h:2688

[bt\_hci\_op\_le\_cs\_test::drbg\_nonce](structbt__hci__op__le__cs__test.md#aee8c125df0f7136a0ecdb9f04903aaef)

uint16\_t drbg\_nonce

**Definition** hci\_types.h:2704

[bt\_hci\_op\_le\_cs\_test::cs\_sync\_antenna\_selection](structbt__hci__op__le__cs__test.md#aef335dd7738634cb8f81c18e0350141e)

uint8\_t cs\_sync\_antenna\_selection

**Definition** hci\_types.h:2690

[bt\_hci\_op\_le\_cs\_test::cs\_sync\_phy](structbt__hci__op__le__cs__test.md#af42701651bca5fe0353ae1de9c453f47)

uint8\_t cs\_sync\_phy

**Definition** hci\_types.h:2689

[bt\_hci\_op\_le\_cs\_test::main\_mode\_type](structbt__hci__op__le__cs__test.md#af4cdfd8c8cab500277c06a82ac088577)

uint8\_t main\_mode\_type

**Definition** hci\_types.h:2683

[bt\_hci\_op\_le\_cs\_test::role](structbt__hci__op__le__cs__test.md#afa0310f818002d7c1ac048f0db8c7f1c)

uint8\_t role

**Definition** hci\_types.h:2687

[bt\_hci\_rp\_configure\_data\_path](structbt__hci__rp__configure__data__path.md)

**Definition** hci\_types.h:823

[bt\_hci\_rp\_configure\_data\_path::status](structbt__hci__rp__configure__data__path.md#a10cfe9bf5a7be202706957d7b8e1f371)

uint8\_t status

**Definition** hci\_types.h:824

[bt\_hci\_rp\_connect\_cancel](structbt__hci__rp__connect__cancel.md)

**Definition** hci\_types.h:410

[bt\_hci\_rp\_connect\_cancel::status](structbt__hci__rp__connect__cancel.md#a05d0c9e4163bc62a57dba8618294eb65)

uint8\_t status

**Definition** hci\_types.h:411

[bt\_hci\_rp\_connect\_cancel::bdaddr](structbt__hci__rp__connect__cancel.md#a0ccfcbd294aa067879ab8d7a41bc41c9)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:412

[bt\_hci\_rp\_le\_big\_terminate\_sync](structbt__hci__rp__le__big__terminate__sync.md)

**Definition** hci\_types.h:2293

[bt\_hci\_rp\_le\_big\_terminate\_sync::big\_handle](structbt__hci__rp__le__big__terminate__sync.md#a741ab80e08e7ecfc5a0158ec0cf14654)

uint8\_t big\_handle

**Definition** hci\_types.h:2295

[bt\_hci\_rp\_le\_big\_terminate\_sync::status](structbt__hci__rp__le__big__terminate__sync.md#ad4d1d4238402ef829a1ff9ed3b1dc050)

uint8\_t status

**Definition** hci\_types.h:2294

[bt\_hci\_rp\_le\_conn\_cte\_req\_enable](structbt__hci__rp__le__conn__cte__req__enable.md)

**Definition** hci\_types.h:1986

[bt\_hci\_rp\_le\_conn\_cte\_req\_enable::status](structbt__hci__rp__le__conn__cte__req__enable.md#a1e76e7a6da194a433c1fa6ac2bc36b80)

uint8\_t status

**Definition** hci\_types.h:1987

[bt\_hci\_rp\_le\_conn\_cte\_req\_enable::handle](structbt__hci__rp__le__conn__cte__req__enable.md#af00adb07a144156a37fb5fc47ca61ccb)

uint16\_t handle

**Definition** hci\_types.h:1988

[bt\_hci\_rp\_le\_conn\_cte\_rsp\_enable](structbt__hci__rp__le__conn__cte__rsp__enable.md)

**Definition** hci\_types.h:1997

[bt\_hci\_rp\_le\_conn\_cte\_rsp\_enable::status](structbt__hci__rp__le__conn__cte__rsp__enable.md#a8a21bc015408cc77c5d229cd77289dcc)

uint8\_t status

**Definition** hci\_types.h:1998

[bt\_hci\_rp\_le\_conn\_cte\_rsp\_enable::handle](structbt__hci__rp__le__conn__cte__rsp__enable.md#ab16f226d871d7d55c3f900614d59d8a1)

uint16\_t handle

**Definition** hci\_types.h:1999

[bt\_hci\_rp\_le\_conn\_param\_req\_neg\_reply](structbt__hci__rp__le__conn__param__req__neg__reply.md)

**Definition** hci\_types.h:1311

[bt\_hci\_rp\_le\_conn\_param\_req\_neg\_reply::status](structbt__hci__rp__le__conn__param__req__neg__reply.md#a3804e64f9e8693e3e5899067212f6873)

uint8\_t status

**Definition** hci\_types.h:1312

[bt\_hci\_rp\_le\_conn\_param\_req\_neg\_reply::handle](structbt__hci__rp__le__conn__param__req__neg__reply.md#ac88f44127c0a1b9b191a27cc003c1052)

uint16\_t handle

**Definition** hci\_types.h:1313

[bt\_hci\_rp\_le\_conn\_param\_req\_reply](structbt__hci__rp__le__conn__param__req__reply.md)

**Definition** hci\_types.h:1301

[bt\_hci\_rp\_le\_conn\_param\_req\_reply::status](structbt__hci__rp__le__conn__param__req__reply.md#a2f0a9f5b087d1f12c100ef4521e015ff)

uint8\_t status

**Definition** hci\_types.h:1302

[bt\_hci\_rp\_le\_conn\_param\_req\_reply::handle](structbt__hci__rp__le__conn__param__req__reply.md#a3e598cd87d5298a1cc62ac79a4f34a6e)

uint16\_t handle

**Definition** hci\_types.h:1303

[bt\_hci\_rp\_le\_default\_past\_param](structbt__hci__rp__le__default__past__param.md)

**Definition** hci\_types.h:2090

[bt\_hci\_rp\_le\_default\_past\_param::status](structbt__hci__rp__le__default__past__param.md#a292e2d655c77e8cda0d01fc07b43b8c4)

uint8\_t status

**Definition** hci\_types.h:2091

[bt\_hci\_rp\_le\_encrypt](structbt__hci__rp__le__encrypt.md)

**Definition** hci\_types.h:1220

[bt\_hci\_rp\_le\_encrypt::enc\_data](structbt__hci__rp__le__encrypt.md#ac20cd9f4ceffea6999114f65437aefdc)

uint8\_t enc\_data[16]

**Definition** hci\_types.h:1222

[bt\_hci\_rp\_le\_encrypt::status](structbt__hci__rp__le__encrypt.md#aee480917cc6af7dea77717a9cb5840bb)

uint8\_t status

**Definition** hci\_types.h:1221

[bt\_hci\_rp\_le\_iso\_receive\_test](structbt__hci__rp__le__iso__receive__test.md)

**Definition** hci\_types.h:2351

[bt\_hci\_rp\_le\_iso\_receive\_test::status](structbt__hci__rp__le__iso__receive__test.md#a028a77001a5e24dda8fac38718103ef0)

uint8\_t status

**Definition** hci\_types.h:2352

[bt\_hci\_rp\_le\_iso\_receive\_test::handle](structbt__hci__rp__le__iso__receive__test.md#a863a8a44af979a8b1b9d084563b2fe9a)

uint16\_t handle

**Definition** hci\_types.h:2353

[bt\_hci\_rp\_le\_iso\_test\_end](structbt__hci__rp__le__iso__test__end.md)

**Definition** hci\_types.h:2374

[bt\_hci\_rp\_le\_iso\_test\_end::missed\_cnt](structbt__hci__rp__le__iso__test__end.md#a10b3ee6110bc0bb9279b22f9963715c1)

uint32\_t missed\_cnt

**Definition** hci\_types.h:2378

[bt\_hci\_rp\_le\_iso\_test\_end::status](structbt__hci__rp__le__iso__test__end.md#a16feaeb739f6ed34d9ce3fc86248955c)

uint8\_t status

**Definition** hci\_types.h:2375

[bt\_hci\_rp\_le\_iso\_test\_end::handle](structbt__hci__rp__le__iso__test__end.md#a4a4625d7b78abf3c039842df2a72ce8b)

uint16\_t handle

**Definition** hci\_types.h:2376

[bt\_hci\_rp\_le\_iso\_test\_end::received\_cnt](structbt__hci__rp__le__iso__test__end.md#a55490978e7416ecc308bf510f05afd4f)

uint32\_t received\_cnt

**Definition** hci\_types.h:2377

[bt\_hci\_rp\_le\_iso\_test\_end::failed\_cnt](structbt__hci__rp__le__iso__test__end.md#ab4352fd5d9b822fb7fb75f8f5e2db6a9)

uint32\_t failed\_cnt

**Definition** hci\_types.h:2379

[bt\_hci\_rp\_le\_iso\_transmit\_test](structbt__hci__rp__le__iso__transmit__test.md)

**Definition** hci\_types.h:2340

[bt\_hci\_rp\_le\_iso\_transmit\_test::status](structbt__hci__rp__le__iso__transmit__test.md#a01ae01d11c606f559107b8c54781d843)

uint8\_t status

**Definition** hci\_types.h:2341

[bt\_hci\_rp\_le\_iso\_transmit\_test::handle](structbt__hci__rp__le__iso__transmit__test.md#a0863c47551b328984e00c392f9f11660)

uint16\_t handle

**Definition** hci\_types.h:2342

[bt\_hci\_rp\_le\_ltk\_req\_neg\_reply](structbt__hci__rp__le__ltk__req__neg__reply.md)

**Definition** hci\_types.h:1253

[bt\_hci\_rp\_le\_ltk\_req\_neg\_reply::status](structbt__hci__rp__le__ltk__req__neg__reply.md#a92306e47450b239233a3f39c645eaa4e)

uint8\_t status

**Definition** hci\_types.h:1254

[bt\_hci\_rp\_le\_ltk\_req\_neg\_reply::handle](structbt__hci__rp__le__ltk__req__neg__reply.md#ad0f4f9300d9a8b737b41211972151017)

uint16\_t handle

**Definition** hci\_types.h:1255

[bt\_hci\_rp\_le\_ltk\_req\_reply](structbt__hci__rp__le__ltk__req__reply.md)

**Definition** hci\_types.h:1244

[bt\_hci\_rp\_le\_ltk\_req\_reply::handle](structbt__hci__rp__le__ltk__req__reply.md#a2dfe012e641e5d8bd6c0f2e15e5a54c2)

uint16\_t handle

**Definition** hci\_types.h:1246

[bt\_hci\_rp\_le\_ltk\_req\_reply::status](structbt__hci__rp__le__ltk__req__reply.md#a831950bab8994f36c96c543310400752)

uint8\_t status

**Definition** hci\_types.h:1245

[bt\_hci\_rp\_le\_past\_param](structbt__hci__rp__le__past__param.md)

**Definition** hci\_types.h:2077

[bt\_hci\_rp\_le\_past\_param::status](structbt__hci__rp__le__past__param.md#a9630362b3d885b13869a4c0fe9e97b12)

uint8\_t status

**Definition** hci\_types.h:2078

[bt\_hci\_rp\_le\_past\_param::conn\_handle](structbt__hci__rp__le__past__param.md#ae6b8a5d7e790516de2f91e41fd893111)

uint16\_t conn\_handle

**Definition** hci\_types.h:2079

[bt\_hci\_rp\_le\_per\_adv\_set\_info\_transfer](structbt__hci__rp__le__per__adv__set__info__transfer.md)

**Definition** hci\_types.h:2052

[bt\_hci\_rp\_le\_per\_adv\_set\_info\_transfer::conn\_handle](structbt__hci__rp__le__per__adv__set__info__transfer.md#a696e5cab4d7507ea79b0e116c4bb92e2)

uint16\_t conn\_handle

**Definition** hci\_types.h:2054

[bt\_hci\_rp\_le\_per\_adv\_set\_info\_transfer::status](structbt__hci__rp__le__per__adv__set__info__transfer.md#ab1592bfadd45315ff47e86b7c50374ad)

uint8\_t status

**Definition** hci\_types.h:2053

[bt\_hci\_rp\_le\_per\_adv\_sync\_transfer](structbt__hci__rp__le__per__adv__sync__transfer.md)

**Definition** hci\_types.h:2040

[bt\_hci\_rp\_le\_per\_adv\_sync\_transfer::conn\_handle](structbt__hci__rp__le__per__adv__sync__transfer.md#ab8b4357fd92e01a5f61d3127b04c0318)

uint16\_t conn\_handle

**Definition** hci\_types.h:2042

[bt\_hci\_rp\_le\_per\_adv\_sync\_transfer::status](structbt__hci__rp__le__per__adv__sync__transfer.md#adb536c4694d2e7c5b91e9f68986e97e1)

uint8\_t status

**Definition** hci\_types.h:2041

[bt\_hci\_rp\_le\_rand](structbt__hci__rp__le__rand.md)

**Definition** hci\_types.h:1226

[bt\_hci\_rp\_le\_rand::rand](structbt__hci__rp__le__rand.md#a3f706af9d2baf9e2b199242a28cec9e5)

uint8\_t rand[8]

**Definition** hci\_types.h:1228

[bt\_hci\_rp\_le\_rand::status](structbt__hci__rp__le__rand.md#a73320168836caa3caf724282402e80de)

uint8\_t status

**Definition** hci\_types.h:1227

[bt\_hci\_rp\_le\_read\_ant\_info](structbt__hci__rp__le__read__ant__info.md)

**Definition** hci\_types.h:2016

[bt\_hci\_rp\_le\_read\_ant\_info::num\_ant](structbt__hci__rp__le__read__ant__info.md#a1f79b45751d39ebb9349df93d0ff2e13)

uint8\_t num\_ant

**Definition** hci\_types.h:2019

[bt\_hci\_rp\_le\_read\_ant\_info::switch\_sample\_rates](structbt__hci__rp__le__read__ant__info.md#a2c78d3db239c9e00729d91834eb60f21)

uint8\_t switch\_sample\_rates

**Definition** hci\_types.h:2018

[bt\_hci\_rp\_le\_read\_ant\_info::max\_cte\_len](structbt__hci__rp__le__read__ant__info.md#a625cc8fa8553eafbbb31cbc0b3f303c7)

uint8\_t max\_cte\_len

**Definition** hci\_types.h:2021

[bt\_hci\_rp\_le\_read\_ant\_info::status](structbt__hci__rp__le__read__ant__info.md#ae1388d3eee3085af7f2b0b57b2aa7b1e)

uint8\_t status

**Definition** hci\_types.h:2017

[bt\_hci\_rp\_le\_read\_ant\_info::max\_switch\_pattern\_len](structbt__hci__rp__le__read__ant__info.md#ae75fe0b9f5fe8c88a8e8482eef299348)

uint8\_t max\_switch\_pattern\_len

**Definition** hci\_types.h:2020

[bt\_hci\_rp\_le\_read\_buffer\_size\_v2](structbt__hci__rp__le__read__buffer__size__v2.md)

**Definition** hci\_types.h:2095

[bt\_hci\_rp\_le\_read\_buffer\_size\_v2::acl\_max\_num](structbt__hci__rp__le__read__buffer__size__v2.md#a1c7938defb076d973b8339c17cc930df)

uint8\_t acl\_max\_num

**Definition** hci\_types.h:2098

[bt\_hci\_rp\_le\_read\_buffer\_size\_v2::status](structbt__hci__rp__le__read__buffer__size__v2.md#a3b9cc0577d0f5f3c2b934a28915f2177)

uint8\_t status

**Definition** hci\_types.h:2096

[bt\_hci\_rp\_le\_read\_buffer\_size\_v2::iso\_max\_len](structbt__hci__rp__le__read__buffer__size__v2.md#a9758d477c502575a1c176eb6a63e1a1a)

uint16\_t iso\_max\_len

**Definition** hci\_types.h:2099

[bt\_hci\_rp\_le\_read\_buffer\_size\_v2::iso\_max\_num](structbt__hci__rp__le__read__buffer__size__v2.md#ac3379adf42f9bbee8ae72fb4a7606fd1)

uint8\_t iso\_max\_num

**Definition** hci\_types.h:2100

[bt\_hci\_rp\_le\_read\_buffer\_size\_v2::acl\_max\_len](structbt__hci__rp__le__read__buffer__size__v2.md#ac391149d3d7442e074aad4b98659bd02)

uint16\_t acl\_max\_len

**Definition** hci\_types.h:2097

[bt\_hci\_rp\_le\_read\_buffer\_size](structbt__hci__rp__le__read__buffer__size.md)

**Definition** hci\_types.h:1039

[bt\_hci\_rp\_le\_read\_buffer\_size::le\_max\_num](structbt__hci__rp__le__read__buffer__size.md#a3e393d6c51d8c3f8a5d88413198e3f28)

uint8\_t le\_max\_num

**Definition** hci\_types.h:1042

[bt\_hci\_rp\_le\_read\_buffer\_size::le\_max\_len](structbt__hci__rp__le__read__buffer__size.md#a8bc64cd8743984cd5a8dedfc86aaee56)

uint16\_t le\_max\_len

**Definition** hci\_types.h:1041

[bt\_hci\_rp\_le\_read\_buffer\_size::status](structbt__hci__rp__le__read__buffer__size.md#a90a1206f1dbbefd298e5323ac07691f1)

uint8\_t status

**Definition** hci\_types.h:1040

[bt\_hci\_rp\_le\_read\_chan\_map](structbt__hci__rp__le__read__chan__map.md)

**Definition** hci\_types.h:1204

[bt\_hci\_rp\_le\_read\_chan\_map::ch\_map](structbt__hci__rp__le__read__chan__map.md#a2899c53f17ba2293b95477ba25fd1b3d)

uint8\_t ch\_map[5]

**Definition** hci\_types.h:1207

[bt\_hci\_rp\_le\_read\_chan\_map::status](structbt__hci__rp__le__read__chan__map.md#a73a51f243bf4881f9024ba67cf2426ad)

uint8\_t status

**Definition** hci\_types.h:1205

[bt\_hci\_rp\_le\_read\_chan\_map::handle](structbt__hci__rp__le__read__chan__map.md#a8fcec46574f5601bf0837aae8f745b38)

uint16\_t handle

**Definition** hci\_types.h:1206

[bt\_hci\_rp\_le\_read\_chan\_tx\_power](structbt__hci__rp__le__read__chan__tx__power.md)

**Definition** hci\_types.h:1089

[bt\_hci\_rp\_le\_read\_chan\_tx\_power::status](structbt__hci__rp__le__read__chan__tx__power.md#a09a3805bccdabef399d21b29f84e3a4f)

uint8\_t status

**Definition** hci\_types.h:1090

[bt\_hci\_rp\_le\_read\_chan\_tx\_power::tx\_power\_level](structbt__hci__rp__le__read__chan__tx__power.md#a3b6b79d1d28c3e4bf565ae364089f365)

int8\_t tx\_power\_level

**Definition** hci\_types.h:1091

[bt\_hci\_rp\_le\_read\_default\_data\_len](structbt__hci__rp__le__read__default__data__len.md)

**Definition** hci\_types.h:1328

[bt\_hci\_rp\_le\_read\_default\_data\_len::max\_tx\_octets](structbt__hci__rp__le__read__default__data__len.md#a1ec4ba1c0286132e87fcffeb988a37f9)

uint16\_t max\_tx\_octets

**Definition** hci\_types.h:1330

[bt\_hci\_rp\_le\_read\_default\_data\_len::status](structbt__hci__rp__le__read__default__data__len.md#a62d735826ad3ca5d4bea7d0fb87dea7e)

uint8\_t status

**Definition** hci\_types.h:1329

[bt\_hci\_rp\_le\_read\_default\_data\_len::max\_tx\_time](structbt__hci__rp__le__read__default__data__len.md#ae193eab40c2afa55b78a1906e6a26f26)

uint16\_t max\_tx\_time

**Definition** hci\_types.h:1331

[bt\_hci\_rp\_le\_read\_fal\_size](structbt__hci__rp__le__read__fal__size.md)

**Definition** hci\_types.h:1167

[bt\_hci\_rp\_le\_read\_fal\_size::status](structbt__hci__rp__le__read__fal__size.md#aaceae885848bbdbf71241e7aa3881db5)

uint8\_t status

**Definition** hci\_types.h:1168

[bt\_hci\_rp\_le\_read\_fal\_size::fal\_size](structbt__hci__rp__le__read__fal__size.md#ac5fcb88478c1faadf7f7ca6a9f838dde)

uint8\_t fal\_size

**Definition** hci\_types.h:1169

[bt\_hci\_rp\_le\_read\_iso\_link\_quality](structbt__hci__rp__le__read__iso__link__quality.md)

**Definition** hci\_types.h:2397

[bt\_hci\_rp\_le\_read\_iso\_link\_quality::tx\_last\_subevent\_packets](structbt__hci__rp__le__read__iso__link__quality.md#a0d4468f6871716414ef4a601791bac58)

uint32\_t tx\_last\_subevent\_packets

**Definition** hci\_types.h:2402

[bt\_hci\_rp\_le\_read\_iso\_link\_quality::tx\_flushed\_packets](structbt__hci__rp__le__read__iso__link__quality.md#a12c0c3f9fe6c3c94742367f30bdcc630)

uint32\_t tx\_flushed\_packets

**Definition** hci\_types.h:2401

[bt\_hci\_rp\_le\_read\_iso\_link\_quality::crc\_error\_packets](structbt__hci__rp__le__read__iso__link__quality.md#a353070a64655a39f5410fe76e9168e97)

uint32\_t crc\_error\_packets

**Definition** hci\_types.h:2404

[bt\_hci\_rp\_le\_read\_iso\_link\_quality::duplicate\_packets](structbt__hci__rp__le__read__iso__link__quality.md#a68c23277e65dc5694f5a27ee2cd364ff)

uint32\_t duplicate\_packets

**Definition** hci\_types.h:2406

[bt\_hci\_rp\_le\_read\_iso\_link\_quality::rx\_unreceived\_packets](structbt__hci__rp__le__read__iso__link__quality.md#a6a16d0aa7ed220bac1ade12eb0f7703e)

uint32\_t rx\_unreceived\_packets

**Definition** hci\_types.h:2405

[bt\_hci\_rp\_le\_read\_iso\_link\_quality::retransmitted\_packets](structbt__hci__rp__le__read__iso__link__quality.md#a7be135da9607045f60b616b84a68f5db)

uint32\_t retransmitted\_packets

**Definition** hci\_types.h:2403

[bt\_hci\_rp\_le\_read\_iso\_link\_quality::handle](structbt__hci__rp__le__read__iso__link__quality.md#a9f2e8c26081ede43c7712b851d79f2cd)

uint16\_t handle

**Definition** hci\_types.h:2399

[bt\_hci\_rp\_le\_read\_iso\_link\_quality::tx\_unacked\_packets](structbt__hci__rp__le__read__iso__link__quality.md#aae42e05dff474062726b92c6d45eae4f)

uint32\_t tx\_unacked\_packets

**Definition** hci\_types.h:2400

[bt\_hci\_rp\_le\_read\_iso\_link\_quality::status](structbt__hci__rp__le__read__iso__link__quality.md#aef80c600f8916c098e08c43ca718d630)

uint8\_t status

**Definition** hci\_types.h:2398

[bt\_hci\_rp\_le\_read\_iso\_tx\_sync](structbt__hci__rp__le__read__iso__tx__sync.md)

**Definition** hci\_types.h:2108

[bt\_hci\_rp\_le\_read\_iso\_tx\_sync::status](structbt__hci__rp__le__read__iso__tx__sync.md#a188ef5dba77c754c46094135cc52641c)

uint8\_t status

**Definition** hci\_types.h:2109

[bt\_hci\_rp\_le\_read\_iso\_tx\_sync::offset](structbt__hci__rp__le__read__iso__tx__sync.md#a29770c3172d5e45409392aa8ffc835ef)

uint8\_t offset[3]

**Definition** hci\_types.h:2113

[bt\_hci\_rp\_le\_read\_iso\_tx\_sync::timestamp](structbt__hci__rp__le__read__iso__tx__sync.md#a35520a3e50afc03ed969b6c5ca9e15d9)

uint32\_t timestamp

**Definition** hci\_types.h:2112

[bt\_hci\_rp\_le\_read\_iso\_tx\_sync::handle](structbt__hci__rp__le__read__iso__tx__sync.md#a8c0003043d3896b1ff93dc33dccc76b4)

uint16\_t handle

**Definition** hci\_types.h:2110

[bt\_hci\_rp\_le\_read\_iso\_tx\_sync::seq](structbt__hci__rp__le__read__iso__tx__sync.md#af2a02f68aa0a757757c490e707954952)

uint16\_t seq

**Definition** hci\_types.h:2111

[bt\_hci\_rp\_le\_read\_local\_features](structbt__hci__rp__le__read__local__features.md)

**Definition** hci\_types.h:1046

[bt\_hci\_rp\_le\_read\_local\_features::status](structbt__hci__rp__le__read__local__features.md#ac1000822beba8a7be0dda684c0a86b6b)

uint8\_t status

**Definition** hci\_types.h:1047

[bt\_hci\_rp\_le\_read\_local\_features::features](structbt__hci__rp__le__read__local__features.md#ada42e525338cd5526ff211c359c93b3b)

uint8\_t features[8]

**Definition** hci\_types.h:1048

[bt\_hci\_rp\_le\_read\_local\_rpa](structbt__hci__rp__le__read__local__rpa.md)

**Definition** hci\_types.h:1392

[bt\_hci\_rp\_le\_read\_local\_rpa::status](structbt__hci__rp__le__read__local__rpa.md#a55b1ac66c986c0a7879b144163064be2)

uint8\_t status

**Definition** hci\_types.h:1393

[bt\_hci\_rp\_le\_read\_local\_rpa::local\_rpa](structbt__hci__rp__le__read__local__rpa.md#a5b27c5b02cb290452be62c22772fbc53)

bt\_addr\_t local\_rpa

**Definition** hci\_types.h:1394

[bt\_hci\_rp\_le\_read\_local\_supported\_capabilities](structbt__hci__rp__le__read__local__supported__capabilities.md)

**Definition** hci\_types.h:2438

[bt\_hci\_rp\_le\_read\_local\_supported\_capabilities::roles\_supported](structbt__hci__rp__le__read__local__supported__capabilities.md#a0958a5426e0057e2b8ccb80c222d0248)

uint8\_t roles\_supported

**Definition** hci\_types.h:2444

[bt\_hci\_rp\_le\_read\_local\_supported\_capabilities::nadm\_random\_capability](structbt__hci__rp__le__read__local__supported__capabilities.md#a0e0bd5b1c624c7143b0229b5d3eeec6e)

uint16\_t nadm\_random\_capability

**Definition** hci\_types.h:2451

[bt\_hci\_rp\_le\_read\_local\_supported\_capabilities::t\_ip1\_times\_supported](structbt__hci__rp__le__read__local__supported__capabilities.md#a115ffe697da3e09ece4091493fa8f2da)

uint16\_t t\_ip1\_times\_supported

**Definition** hci\_types.h:2454

[bt\_hci\_rp\_le\_read\_local\_supported\_capabilities::tx\_snr\_capability](structbt__hci__rp__le__read__local__supported__capabilities.md#a1806f2f5ec2738b026453bbdb8b38ce9)

uint8\_t tx\_snr\_capability

**Definition** hci\_types.h:2459

[bt\_hci\_rp\_le\_read\_local\_supported\_capabilities::rtt\_capability](structbt__hci__rp__le__read__local__supported__capabilities.md#a24ffa02b6a8bfbff8b7d32f5ee46bea5)

uint8\_t rtt\_capability

**Definition** hci\_types.h:2446

[bt\_hci\_rp\_le\_read\_local\_supported\_capabilities::rtt\_aa\_only\_n](structbt__hci__rp__le__read__local__supported__capabilities.md#a3a16c62ea321620608d706a80d90575e)

uint8\_t rtt\_aa\_only\_n

**Definition** hci\_types.h:2447

[bt\_hci\_rp\_le\_read\_local\_supported\_capabilities::nadm\_sounding\_capability](structbt__hci__rp__le__read__local__supported__capabilities.md#a3eb4830443e7912bf8ca97f603b91545)

uint16\_t nadm\_sounding\_capability

**Definition** hci\_types.h:2450

[bt\_hci\_rp\_le\_read\_local\_supported\_capabilities::num\_config\_supported](structbt__hci__rp__le__read__local__supported__capabilities.md#a5f59d0b65cc4e7e44e487fa5535b76a9)

uint8\_t num\_config\_supported

**Definition** hci\_types.h:2440

[bt\_hci\_rp\_le\_read\_local\_supported\_capabilities::max\_antenna\_paths\_supported](structbt__hci__rp__le__read__local__supported__capabilities.md#a7975eb0ce27f0326d1d909bffef57840)

uint8\_t max\_antenna\_paths\_supported

**Definition** hci\_types.h:2443

[bt\_hci\_rp\_le\_read\_local\_supported\_capabilities::t\_fcs\_times\_supported](structbt__hci__rp__le__read__local__supported__capabilities.md#a81bd809a734b6cdde2d55e0b23e41237)

uint16\_t t\_fcs\_times\_supported

**Definition** hci\_types.h:2456

[bt\_hci\_rp\_le\_read\_local\_supported\_capabilities::t\_ip2\_times\_supported](structbt__hci__rp__le__read__local__supported__capabilities.md#a88a4277c5dea41b8171c33c85ed760bf)

uint16\_t t\_ip2\_times\_supported

**Definition** hci\_types.h:2455

[bt\_hci\_rp\_le\_read\_local\_supported\_capabilities::subfeatures\_supported](structbt__hci__rp__le__read__local__supported__capabilities.md#a8e7cc92cc4099774e8d0b385fc5f3d79)

uint16\_t subfeatures\_supported

**Definition** hci\_types.h:2453

[bt\_hci\_rp\_le\_read\_local\_supported\_capabilities::modes\_supported](structbt__hci__rp__le__read__local__supported__capabilities.md#aaf09d10c19980729ef04654114919211)

uint8\_t modes\_supported

**Definition** hci\_types.h:2445

[bt\_hci\_rp\_le\_read\_local\_supported\_capabilities::status](structbt__hci__rp__le__read__local__supported__capabilities.md#aaf578336893980f2ec1b2343b81860e5)

uint8\_t status

**Definition** hci\_types.h:2439

[bt\_hci\_rp\_le\_read\_local\_supported\_capabilities::t\_pm\_times\_supported](structbt__hci__rp__le__read__local__supported__capabilities.md#ab026e5abfdead47eca1c5d8d316bc62c)

uint16\_t t\_pm\_times\_supported

**Definition** hci\_types.h:2457

[bt\_hci\_rp\_le\_read\_local\_supported\_capabilities::rtt\_sounding\_n](structbt__hci__rp__le__read__local__supported__capabilities.md#ababf476100298c2ba7d79bdadd7a9d1b)

uint8\_t rtt\_sounding\_n

**Definition** hci\_types.h:2448

[bt\_hci\_rp\_le\_read\_local\_supported\_capabilities::t\_sw\_time\_supported](structbt__hci__rp__le__read__local__supported__capabilities.md#ad07b464737c59b33de4c89948d4c5686)

uint8\_t t\_sw\_time\_supported

**Definition** hci\_types.h:2458

[bt\_hci\_rp\_le\_read\_local\_supported\_capabilities::max\_consecutive\_procedures\_supported](structbt__hci__rp__le__read__local__supported__capabilities.md#ad667ba51ffdbaf7754dea6f519615cb7)

uint16\_t max\_consecutive\_procedures\_supported

**Definition** hci\_types.h:2441

[bt\_hci\_rp\_le\_read\_local\_supported\_capabilities::rtt\_random\_payload\_n](structbt__hci__rp__le__read__local__supported__capabilities.md#ad90ce3e635b8bccd29eefe73303f6e42)

uint8\_t rtt\_random\_payload\_n

**Definition** hci\_types.h:2449

[bt\_hci\_rp\_le\_read\_local\_supported\_capabilities::num\_antennas\_supported](structbt__hci__rp__le__read__local__supported__capabilities.md#ae0767bb41b7b57e955ddbede2f83c166)

uint8\_t num\_antennas\_supported

**Definition** hci\_types.h:2442

[bt\_hci\_rp\_le\_read\_local\_supported\_capabilities::cs\_sync\_phys\_supported](structbt__hci__rp__le__read__local__supported__capabilities.md#af3d1e7588f2429bb400fac81733748c3)

uint8\_t cs\_sync\_phys\_supported

**Definition** hci\_types.h:2452

[bt\_hci\_rp\_le\_read\_max\_adv\_data\_len](structbt__hci__rp__le__read__max__adv__data__len.md)

**Definition** hci\_types.h:1614

[bt\_hci\_rp\_le\_read\_max\_adv\_data\_len::status](structbt__hci__rp__le__read__max__adv__data__len.md#a978911dc5028d1f36820447de8e9e5f7)

uint8\_t status

**Definition** hci\_types.h:1615

[bt\_hci\_rp\_le\_read\_max\_adv\_data\_len::max\_adv\_data\_len](structbt__hci__rp__le__read__max__adv__data__len.md#aa4084a89de4929c3e8e2630d0aad7f82)

uint16\_t max\_adv\_data\_len

**Definition** hci\_types.h:1616

[bt\_hci\_rp\_le\_read\_max\_data\_len](structbt__hci__rp__le__read__max__data__len.md)

**Definition** hci\_types.h:1422

[bt\_hci\_rp\_le\_read\_max\_data\_len::max\_tx\_octets](structbt__hci__rp__le__read__max__data__len.md#a2c0b159c6248cb9df458d587f82a4152)

uint16\_t max\_tx\_octets

**Definition** hci\_types.h:1424

[bt\_hci\_rp\_le\_read\_max\_data\_len::status](structbt__hci__rp__le__read__max__data__len.md#a654b34b1ee038bf442550a340a26070c)

uint8\_t status

**Definition** hci\_types.h:1423

[bt\_hci\_rp\_le\_read\_max\_data\_len::max\_tx\_time](structbt__hci__rp__le__read__max__data__len.md#a6adc84bf3cc86f234e61982d871899b6)

uint16\_t max\_tx\_time

**Definition** hci\_types.h:1425

[bt\_hci\_rp\_le\_read\_max\_data\_len::max\_rx\_octets](structbt__hci__rp__le__read__max__data__len.md#a9273dac6614f1e120f0539b746bfd6cc)

uint16\_t max\_rx\_octets

**Definition** hci\_types.h:1426

[bt\_hci\_rp\_le\_read\_max\_data\_len::max\_rx\_time](structbt__hci__rp__le__read__max__data__len.md#a963ef9c097906c8db46c35459eb4ecab)

uint16\_t max\_rx\_time

**Definition** hci\_types.h:1427

[bt\_hci\_rp\_le\_read\_num\_adv\_sets](structbt__hci__rp__le__read__num__adv__sets.md)

**Definition** hci\_types.h:1620

[bt\_hci\_rp\_le\_read\_num\_adv\_sets::status](structbt__hci__rp__le__read__num__adv__sets.md#a590934059fb851a14b2eec66f32a5334)

uint8\_t status

**Definition** hci\_types.h:1621

[bt\_hci\_rp\_le\_read\_num\_adv\_sets::num\_sets](structbt__hci__rp__le__read__num__adv__sets.md#a7dd26bda7a8ab75fed2af19bb5af34fc)

uint8\_t num\_sets

**Definition** hci\_types.h:1622

[bt\_hci\_rp\_le\_read\_peer\_rpa](structbt__hci__rp__le__read__peer__rpa.md)

**Definition** hci\_types.h:1383

[bt\_hci\_rp\_le\_read\_peer\_rpa::peer\_rpa](structbt__hci__rp__le__read__peer__rpa.md#a4eeee179819865ba5d5171d9bd33e5e9)

bt\_addr\_t peer\_rpa

**Definition** hci\_types.h:1385

[bt\_hci\_rp\_le\_read\_peer\_rpa::status](structbt__hci__rp__le__read__peer__rpa.md#a9c8c799e8c9fbb9f64865e55cdb1f9ef)

uint8\_t status

**Definition** hci\_types.h:1384

[bt\_hci\_rp\_le\_read\_per\_adv\_list\_size](structbt__hci__rp__le__read__per__adv__list__size.md)

**Definition** hci\_types.h:1824

[bt\_hci\_rp\_le\_read\_per\_adv\_list\_size::status](structbt__hci__rp__le__read__per__adv__list__size.md#a70aa5b466bdbbd309fc59570625c35e5)

uint8\_t status

**Definition** hci\_types.h:1825

[bt\_hci\_rp\_le\_read\_per\_adv\_list\_size::list\_size](structbt__hci__rp__le__read__per__adv__list__size.md#ab6c4ed1037327669aef623f3a1e9d601)

uint8\_t list\_size

**Definition** hci\_types.h:1826

[bt\_hci\_rp\_le\_read\_phy](structbt__hci__rp__le__read__phy.md)

**Definition** hci\_types.h:1438

[bt\_hci\_rp\_le\_read\_phy::rx\_phy](structbt__hci__rp__le__read__phy.md#a5a060e0c0d1e5f33222ab10a5d3977e8)

uint8\_t rx\_phy

**Definition** hci\_types.h:1442

[bt\_hci\_rp\_le\_read\_phy::tx\_phy](structbt__hci__rp__le__read__phy.md#a644c0065d97e5de006dc28f7bca62268)

uint8\_t tx\_phy

**Definition** hci\_types.h:1441

[bt\_hci\_rp\_le\_read\_phy::status](structbt__hci__rp__le__read__phy.md#a65d412e37eb2cd839fae262f4f9d5b28)

uint8\_t status

**Definition** hci\_types.h:1439

[bt\_hci\_rp\_le\_read\_phy::handle](structbt__hci__rp__le__read__phy.md#ae708b4f8ad2632d73bedea640f138d9f)

uint16\_t handle

**Definition** hci\_types.h:1440

[bt\_hci\_rp\_le\_read\_rf\_path\_comp](structbt__hci__rp__le__read__rf__path__comp.md)

**Definition** hci\_types.h:1837

[bt\_hci\_rp\_le\_read\_rf\_path\_comp::rx\_path\_comp](structbt__hci__rp__le__read__rf__path__comp.md#a0f46a99c74006dc0a4dfd1a49c72e077)

int16\_t rx\_path\_comp

**Definition** hci\_types.h:1840

[bt\_hci\_rp\_le\_read\_rf\_path\_comp::tx\_path\_comp](structbt__hci__rp__le__read__rf__path__comp.md#a827fa954277823efdc5838c317a1460a)

int16\_t tx\_path\_comp

**Definition** hci\_types.h:1839

[bt\_hci\_rp\_le\_read\_rf\_path\_comp::status](structbt__hci__rp__le__read__rf__path__comp.md#a84a04bcc64ea6d50fe41e9b416a5ada1)

uint8\_t status

**Definition** hci\_types.h:1838

[bt\_hci\_rp\_le\_read\_rl\_size](structbt__hci__rp__le__read__rl__size.md)

**Definition** hci\_types.h:1374

[bt\_hci\_rp\_le\_read\_rl\_size::rl\_size](structbt__hci__rp__le__read__rl__size.md#a90c28070ee094c99c21c4dd229ff6ce5)

uint8\_t rl\_size

**Definition** hci\_types.h:1376

[bt\_hci\_rp\_le\_read\_rl\_size::status](structbt__hci__rp__le__read__rl__size.md#af8a10aab21d54cce3529b1307769f6c6)

uint8\_t status

**Definition** hci\_types.h:1375

[bt\_hci\_rp\_le\_read\_supp\_states](structbt__hci__rp__le__read__supp__states.md)

**Definition** hci\_types.h:1259

[bt\_hci\_rp\_le\_read\_supp\_states::le\_states](structbt__hci__rp__le__read__supp__states.md#a9b60476cc158a701b29b28bd21375130)

uint8\_t le\_states[8]

**Definition** hci\_types.h:1261

[bt\_hci\_rp\_le\_read\_supp\_states::status](structbt__hci__rp__le__read__supp__states.md#aeed0cc41ee521c27f07d8cbf4b377a4f)

uint8\_t status

**Definition** hci\_types.h:1260

[bt\_hci\_rp\_le\_read\_test\_counters](structbt__hci__rp__le__read__test__counters.md)

**Definition** hci\_types.h:2361

[bt\_hci\_rp\_le\_read\_test\_counters::handle](structbt__hci__rp__le__read__test__counters.md#a8121f879a3fb5550cc1aa468aacb81b7)

uint16\_t handle

**Definition** hci\_types.h:2363

[bt\_hci\_rp\_le\_read\_test\_counters::received\_cnt](structbt__hci__rp__le__read__test__counters.md#a8c4b2674fb129ca0de0bc45c608e13c7)

uint32\_t received\_cnt

**Definition** hci\_types.h:2364

[bt\_hci\_rp\_le\_read\_test\_counters::status](structbt__hci__rp__le__read__test__counters.md#ae1e78d68e9f55b31092a07575a66c1c0)

uint8\_t status

**Definition** hci\_types.h:2362

[bt\_hci\_rp\_le\_read\_test\_counters::missed\_cnt](structbt__hci__rp__le__read__test__counters.md#ae96d05ffb2fbc681c804b04c8791aeab)

uint32\_t missed\_cnt

**Definition** hci\_types.h:2365

[bt\_hci\_rp\_le\_read\_test\_counters::failed\_cnt](structbt__hci__rp__le__read__test__counters.md#af6261d3547cd9b377fedc7a36891c2f7)

uint32\_t failed\_cnt

**Definition** hci\_types.h:2366

[bt\_hci\_rp\_le\_read\_tx\_power\_level](structbt__hci__rp__le__read__tx__power__level.md)

**Definition** hci\_types.h:682

[bt\_hci\_rp\_le\_read\_tx\_power\_level::status](structbt__hci__rp__le__read__tx__power__level.md#a4c83db208bfcb7c9fd2211d192a26d90)

uint8\_t status

**Definition** hci\_types.h:683

[bt\_hci\_rp\_le\_read\_tx\_power\_level::max\_tx\_power\_level](structbt__hci__rp__le__read__tx__power__level.md#a5f9c59660f7c5842712a4ad9ae1d9527)

int8\_t max\_tx\_power\_level

**Definition** hci\_types.h:687

[bt\_hci\_rp\_le\_read\_tx\_power\_level::current\_tx\_power\_level](structbt__hci__rp__le__read__tx__power__level.md#ad14f660eb67f1014d1a62b0e5a113969)

int8\_t current\_tx\_power\_level

**Definition** hci\_types.h:686

[bt\_hci\_rp\_le\_read\_tx\_power\_level::phy](structbt__hci__rp__le__read__tx__power__level.md#ae65a43aad74b1081e88afdb533cbe813)

uint8\_t phy

**Definition** hci\_types.h:685

[bt\_hci\_rp\_le\_read\_tx\_power\_level::handle](structbt__hci__rp__le__read__tx__power__level.md#aec00dfb34abce2d95af183b74f63d1f3)

uint16\_t handle

**Definition** hci\_types.h:684

[bt\_hci\_rp\_le\_read\_tx\_power](structbt__hci__rp__le__read__tx__power.md)

**Definition** hci\_types.h:1830

[bt\_hci\_rp\_le\_read\_tx\_power::max\_tx\_power](structbt__hci__rp__le__read__tx__power.md#a1d794f1f7ea77eceac7dae2546eab047)

int8\_t max\_tx\_power

**Definition** hci\_types.h:1833

[bt\_hci\_rp\_le\_read\_tx\_power::min\_tx\_power](structbt__hci__rp__le__read__tx__power.md#a6d4ab95efda5cfc97ae11d83787da8d7)

int8\_t min\_tx\_power

**Definition** hci\_types.h:1832

[bt\_hci\_rp\_le\_read\_tx\_power::status](structbt__hci__rp__le__read__tx__power.md#a805629b92c65e006082d819f578ed555)

uint8\_t status

**Definition** hci\_types.h:1831

[bt\_hci\_rp\_le\_reject\_cis](structbt__hci__rp__le__reject__cis.md)

**Definition** hci\_types.h:2229

[bt\_hci\_rp\_le\_reject\_cis::handle](structbt__hci__rp__le__reject__cis.md#acd8311e13bdfd7edb2d404d80006f9d4)

uint16\_t handle

**Definition** hci\_types.h:2231

[bt\_hci\_rp\_le\_reject\_cis::status](structbt__hci__rp__le__reject__cis.md#af2dc8a839d3e19821ab8ec0d3dc427ec)

uint8\_t status

**Definition** hci\_types.h:2230

[bt\_hci\_rp\_le\_remove\_cig](structbt__hci__rp__le__remove__cig.md)

**Definition** hci\_types.h:2213

[bt\_hci\_rp\_le\_remove\_cig::status](structbt__hci__rp__le__remove__cig.md#a1335f26f1dc67ff8e2a1960d1b24b1a0)

uint8\_t status

**Definition** hci\_types.h:2214

[bt\_hci\_rp\_le\_remove\_cig::cig\_id](structbt__hci__rp__le__remove__cig.md#a82e74fbbce714b035b1e53fd5f1b09b5)

uint8\_t cig\_id

**Definition** hci\_types.h:2215

[bt\_hci\_rp\_le\_remove\_iso\_path](structbt__hci__rp__le__remove__iso__path.md)

**Definition** hci\_types.h:2325

[bt\_hci\_rp\_le\_remove\_iso\_path::status](structbt__hci__rp__le__remove__iso__path.md#ab22e50e594e19931526feacd9bff33a3)

uint8\_t status

**Definition** hci\_types.h:2326

[bt\_hci\_rp\_le\_remove\_iso\_path::handle](structbt__hci__rp__le__remove__iso__path.md#ae3b7704359989ca13582a5cd3742f588)

uint16\_t handle

**Definition** hci\_types.h:2327

[bt\_hci\_rp\_le\_set\_cig\_params\_test](structbt__hci__rp__le__set__cig__params__test.md)

**Definition** hci\_types.h:2190

[bt\_hci\_rp\_le\_set\_cig\_params\_test::handle](structbt__hci__rp__le__set__cig__params__test.md#a08b07863ed63ab627401c0c80bc3c7b4)

uint16\_t handle[0]

**Definition** hci\_types.h:2194

[bt\_hci\_rp\_le\_set\_cig\_params\_test::num\_handles](structbt__hci__rp__le__set__cig__params__test.md#a10816d0875092c8e6bd4b13b819c43c7)

uint8\_t num\_handles

**Definition** hci\_types.h:2193

[bt\_hci\_rp\_le\_set\_cig\_params\_test::cig\_id](structbt__hci__rp__le__set__cig__params__test.md#a65c11059bc00244e58d2ab8373e3e725)

uint8\_t cig\_id

**Definition** hci\_types.h:2192

[bt\_hci\_rp\_le\_set\_cig\_params\_test::status](structbt__hci__rp__le__set__cig__params__test.md#a932eadb4d750f79b4a7a9c3feb90fdcd)

uint8\_t status

**Definition** hci\_types.h:2191

[bt\_hci\_rp\_le\_set\_cig\_params](structbt__hci__rp__le__set__cig__params.md)

**Definition** hci\_types.h:2155

[bt\_hci\_rp\_le\_set\_cig\_params::handle](structbt__hci__rp__le__set__cig__params.md#a2e95c6217d11169a8a611ea95dce70b6)

uint16\_t handle[0]

**Definition** hci\_types.h:2159

[bt\_hci\_rp\_le\_set\_cig\_params::status](structbt__hci__rp__le__set__cig__params.md#a8426a2b9927bee05fb9a46b4b261c743)

uint8\_t status

**Definition** hci\_types.h:2156

[bt\_hci\_rp\_le\_set\_cig\_params::num\_handles](structbt__hci__rp__le__set__cig__params.md#a8aff643e0ae41455eb9391cfdb45ebda)

uint8\_t num\_handles

**Definition** hci\_types.h:2158

[bt\_hci\_rp\_le\_set\_cig\_params::cig\_id](structbt__hci__rp__le__set__cig__params.md#a951dc88e0cde4e1f0274684498741eac)

uint8\_t cig\_id

**Definition** hci\_types.h:2157

[bt\_hci\_rp\_le\_set\_cl\_cte\_sampling\_enable](structbt__hci__rp__le__set__cl__cte__sampling__enable.md)

**Definition** hci\_types.h:1933

[bt\_hci\_rp\_le\_set\_cl\_cte\_sampling\_enable::sync\_handle](structbt__hci__rp__le__set__cl__cte__sampling__enable.md#a44db7f831e8d730ec3c80c01ef9543aa)

uint16\_t sync\_handle

**Definition** hci\_types.h:1935

[bt\_hci\_rp\_le\_set\_cl\_cte\_sampling\_enable::status](structbt__hci__rp__le__set__cl__cte__sampling__enable.md#a5962f97cef6e53452cdccab1c3440519)

uint8\_t status

**Definition** hci\_types.h:1934

[bt\_hci\_rp\_le\_set\_conn\_cte\_rx\_params](structbt__hci__rp__le__set__conn__cte__rx__params.md)

**Definition** hci\_types.h:1947

[bt\_hci\_rp\_le\_set\_conn\_cte\_rx\_params::handle](structbt__hci__rp__le__set__conn__cte__rx__params.md#a3c3fb92d422e7ccaf0c98706d46b3e5a)

uint16\_t handle

**Definition** hci\_types.h:1949

[bt\_hci\_rp\_le\_set\_conn\_cte\_rx\_params::status](structbt__hci__rp__le__set__conn__cte__rx__params.md#ad38bb356876c16904e408405607de73c)

uint8\_t status

**Definition** hci\_types.h:1948

[bt\_hci\_rp\_le\_set\_conn\_cte\_tx\_params](structbt__hci__rp__le__set__conn__cte__tx__params.md)

**Definition** hci\_types.h:1967

[bt\_hci\_rp\_le\_set\_conn\_cte\_tx\_params::status](structbt__hci__rp__le__set__conn__cte__tx__params.md#a56f62b6d2c42cd22f73026a2fabc6986)

uint8\_t status

**Definition** hci\_types.h:1968

[bt\_hci\_rp\_le\_set\_conn\_cte\_tx\_params::handle](structbt__hci__rp__le__set__conn__cte__tx__params.md#aad553d484daed7ca08de132f4fb849ee)

uint16\_t handle

**Definition** hci\_types.h:1969

[bt\_hci\_rp\_le\_set\_data\_len](structbt__hci__rp__le__set__data__len.md)

**Definition** hci\_types.h:1322

[bt\_hci\_rp\_le\_set\_data\_len::handle](structbt__hci__rp__le__set__data__len.md#a207c6da11e0bb145bed7a9e551ddc608)

uint16\_t handle

**Definition** hci\_types.h:1324

[bt\_hci\_rp\_le\_set\_data\_len::status](structbt__hci__rp__le__set__data__len.md#a8667db355a95691d58845f89e919aea4)

uint8\_t status

**Definition** hci\_types.h:1323

[bt\_hci\_rp\_le\_set\_ext\_adv\_param](structbt__hci__rp__le__set__ext__adv__param.md)

**Definition** hci\_types.h:1542

[bt\_hci\_rp\_le\_set\_ext\_adv\_param::status](structbt__hci__rp__le__set__ext__adv__param.md#a6baae317455ffbb489066fcd1fb068c8)

uint8\_t status

**Definition** hci\_types.h:1543

[bt\_hci\_rp\_le\_set\_ext\_adv\_param::tx\_power](structbt__hci__rp__le__set__ext__adv__param.md#a8a876d0e3d4d9d066a27c054569f0b9a)

int8\_t tx\_power

**Definition** hci\_types.h:1544

[bt\_hci\_rp\_le\_set\_host\_feature](structbt__hci__rp__le__set__host__feature.md)

**Definition** hci\_types.h:2388

[bt\_hci\_rp\_le\_set\_host\_feature::status](structbt__hci__rp__le__set__host__feature.md#a2e7cfc16da9fc0d00c35111811bf7c28)

uint8\_t status

**Definition** hci\_types.h:2389

[bt\_hci\_rp\_le\_setup\_iso\_path](structbt__hci__rp__le__setup__iso__path.md)

**Definition** hci\_types.h:2314

[bt\_hci\_rp\_le\_setup\_iso\_path::handle](structbt__hci__rp__le__setup__iso__path.md#aa8effdcc4ba155b840ef789f20bad19e)

uint16\_t handle

**Definition** hci\_types.h:2316

[bt\_hci\_rp\_le\_setup\_iso\_path::status](structbt__hci__rp__le__setup__iso__path.md#adde60b0dc6ec3d8caccae1d55d78d9a4)

uint8\_t status

**Definition** hci\_types.h:2315

[bt\_hci\_rp\_le\_test\_end](structbt__hci__rp__le__test__end.md)

**Definition** hci\_types.h:1286

[bt\_hci\_rp\_le\_test\_end::status](structbt__hci__rp__le__test__end.md#a2ac412ef9a5fc7651315afe042856cce)

uint8\_t status

**Definition** hci\_types.h:1287

[bt\_hci\_rp\_le\_test\_end::rx\_pkt\_count](structbt__hci__rp__le__test__end.md#a9e283118e4ea48b0df66a4cd1c1cf9a1)

uint16\_t rx\_pkt\_count

**Definition** hci\_types.h:1288

[bt\_hci\_rp\_pin\_code\_neg\_reply](structbt__hci__rp__pin__code__neg__reply.md)

**Definition** hci\_types.h:475

[bt\_hci\_rp\_pin\_code\_neg\_reply::status](structbt__hci__rp__pin__code__neg__reply.md#a10bcc55407e22417256c464684a41e58)

uint8\_t status

**Definition** hci\_types.h:476

[bt\_hci\_rp\_pin\_code\_neg\_reply::bdaddr](structbt__hci__rp__pin__code__neg__reply.md#a168caf2a517aa573bd6acaf48e414e9b)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:477

[bt\_hci\_rp\_pin\_code\_reply](structbt__hci__rp__pin__code__reply.md)

**Definition** hci\_types.h:466

[bt\_hci\_rp\_pin\_code\_reply::status](structbt__hci__rp__pin__code__reply.md#a3f167661b8d3f63ab12e6f64fb33986b)

uint8\_t status

**Definition** hci\_types.h:467

[bt\_hci\_rp\_pin\_code\_reply::bdaddr](structbt__hci__rp__pin__code__reply.md#afc7c991fd8050e8aae56b8587b5ee01d)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:468

[bt\_hci\_rp\_read\_auth\_payload\_timeout](structbt__hci__rp__read__auth__payload__timeout.md)

**Definition** hci\_types.h:798

[bt\_hci\_rp\_read\_auth\_payload\_timeout::status](structbt__hci__rp__read__auth__payload__timeout.md#a3eadeab880eb75c914be654dbc685f3f)

uint8\_t status

**Definition** hci\_types.h:799

[bt\_hci\_rp\_read\_auth\_payload\_timeout::auth\_payload\_timeout](structbt__hci__rp__read__auth__payload__timeout.md#ab4092720dad9a01f4e179eb2f0112aed)

uint16\_t auth\_payload\_timeout

**Definition** hci\_types.h:801

[bt\_hci\_rp\_read\_auth\_payload\_timeout::handle](structbt__hci__rp__read__auth__payload__timeout.md#ab53b7e03c68dcd040e38fdc7429b2d3b)

uint16\_t handle

**Definition** hci\_types.h:800

[bt\_hci\_rp\_read\_bd\_addr](structbt__hci__rp__read__bd__addr.md)

**Definition** hci\_types.h:887

[bt\_hci\_rp\_read\_bd\_addr::status](structbt__hci__rp__read__bd__addr.md#a5230de2a3a6c4161d076b59901790e1e)

uint8\_t status

**Definition** hci\_types.h:888

[bt\_hci\_rp\_read\_bd\_addr::bdaddr](structbt__hci__rp__read__bd__addr.md#aec2c022a465982a3868100699c95f4e6)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:889

[bt\_hci\_rp\_read\_buffer\_size](structbt__hci__rp__read__buffer__size.md)

**Definition** hci\_types.h:878

[bt\_hci\_rp\_read\_buffer\_size::status](structbt__hci__rp__read__buffer__size.md#a6adf126acfcec722dc078d097d2b2ba8)

uint8\_t status

**Definition** hci\_types.h:879

[bt\_hci\_rp\_read\_buffer\_size::sco\_max\_len](structbt__hci__rp__read__buffer__size.md#a7d475559145f469006b2ef147704cd99)

uint8\_t sco\_max\_len

**Definition** hci\_types.h:881

[bt\_hci\_rp\_read\_buffer\_size::acl\_max\_num](structbt__hci__rp__read__buffer__size.md#a87ff361282be71aa60c7f88c50a7492f)

uint16\_t acl\_max\_num

**Definition** hci\_types.h:882

[bt\_hci\_rp\_read\_buffer\_size::acl\_max\_len](structbt__hci__rp__read__buffer__size.md#aba3f1597c929e3721c769beb98000218)

uint16\_t acl\_max\_len

**Definition** hci\_types.h:880

[bt\_hci\_rp\_read\_buffer\_size::sco\_max\_num](structbt__hci__rp__read__buffer__size.md#abc01fa1df6d787f0a2cb865daed5f4cc)

uint16\_t sco\_max\_num

**Definition** hci\_types.h:883

[bt\_hci\_rp\_read\_codec\_capabilities](structbt__hci__rp__read__codec__capabilities.md)

**Definition** hci\_types.h:987

[bt\_hci\_rp\_read\_codec\_capabilities::num\_capabilities](structbt__hci__rp__read__codec__capabilities.md#a71b7df63502bf42a26868e69893ddcfe)

uint8\_t num\_capabilities

**Definition** hci\_types.h:989

[bt\_hci\_rp\_read\_codec\_capabilities::status](structbt__hci__rp__read__codec__capabilities.md#ac224ea998e3af12f97232288266da8d2)

uint8\_t status

**Definition** hci\_types.h:988

[bt\_hci\_rp\_read\_codec\_capabilities::capabilities](structbt__hci__rp__read__codec__capabilities.md#ae0c84013512c461f3b6231162d6f3020)

uint8\_t capabilities[0]

**Definition** hci\_types.h:991

[bt\_hci\_rp\_read\_codecs\_v2](structbt__hci__rp__read__codecs__v2.md)

**Definition** hci\_types.h:965

[bt\_hci\_rp\_read\_codecs\_v2::codecs](structbt__hci__rp__read__codecs__v2.md#a098563f274de085ac97415f1b5e15f3c)

uint8\_t codecs[0]

**Definition** hci\_types.h:968

[bt\_hci\_rp\_read\_codecs\_v2::status](structbt__hci__rp__read__codecs__v2.md#a2e9866d0f9fb42b54c406a9ea5890913)

uint8\_t status

**Definition** hci\_types.h:966

[bt\_hci\_rp\_read\_codecs](structbt__hci__rp__read__codecs.md)

**Definition** hci\_types.h:941

[bt\_hci\_rp\_read\_codecs::status](structbt__hci__rp__read__codecs.md#a017182988634c6acbfbfdd7c9609f5dc)

uint8\_t status

**Definition** hci\_types.h:942

[bt\_hci\_rp\_read\_codecs::codecs](structbt__hci__rp__read__codecs.md#a44e615f375b35cce9f949562555c429b)

uint8\_t codecs[0]

**Definition** hci\_types.h:944

[bt\_hci\_rp\_read\_conn\_accept\_timeout](structbt__hci__rp__read__conn__accept__timeout.md)

**Definition** hci\_types.h:572

[bt\_hci\_rp\_read\_conn\_accept\_timeout::conn\_accept\_timeout](structbt__hci__rp__read__conn__accept__timeout.md#a01ca30c92311ec1df19a4cf835ea74cf)

uint16\_t conn\_accept\_timeout

**Definition** hci\_types.h:574

[bt\_hci\_rp\_read\_conn\_accept\_timeout::status](structbt__hci__rp__read__conn__accept__timeout.md#afeb5888722ee368e02c6b27b75ab2a70)

uint8\_t status

**Definition** hci\_types.h:573

[bt\_hci\_rp\_read\_ctlr\_delay](structbt__hci__rp__read__ctlr__delay.md)

**Definition** hci\_types.h:1002

[bt\_hci\_rp\_read\_ctlr\_delay::status](structbt__hci__rp__read__ctlr__delay.md#a2f17081cf767643f3a9ad9d115ef5320)

uint8\_t status

**Definition** hci\_types.h:1003

[bt\_hci\_rp\_read\_ctlr\_delay::max\_ctlr\_delay](structbt__hci__rp__read__ctlr__delay.md#a4c468053c4a86d1ab462c1e6f17f1013)

uint8\_t max\_ctlr\_delay[3]

**Definition** hci\_types.h:1005

[bt\_hci\_rp\_read\_ctlr\_delay::min\_ctlr\_delay](structbt__hci__rp__read__ctlr__delay.md#ab48d1d92cdf9470a93487434b3824d17)

uint8\_t min\_ctlr\_delay[3]

**Definition** hci\_types.h:1004

[bt\_hci\_rp\_read\_encryption\_key\_size](structbt__hci__rp__read__encryption__key__size.md)

**Definition** hci\_types.h:1025

[bt\_hci\_rp\_read\_encryption\_key\_size::status](structbt__hci__rp__read__encryption__key__size.md#a17213ccb9179739aa79c3749a2296f65)

uint8\_t status

**Definition** hci\_types.h:1026

[bt\_hci\_rp\_read\_encryption\_key\_size::handle](structbt__hci__rp__read__encryption__key__size.md#af0b89b2035f956891244b10409be0f51)

uint16\_t handle

**Definition** hci\_types.h:1027

[bt\_hci\_rp\_read\_encryption\_key\_size::key\_size](structbt__hci__rp__read__encryption__key__size.md#af1cd71c6216b26d460c04a68405f05d5)

uint8\_t key\_size

**Definition** hci\_types.h:1028

[bt\_hci\_rp\_read\_local\_ext\_features](structbt__hci__rp__read__local__ext__features.md)

**Definition** hci\_types.h:864

[bt\_hci\_rp\_read\_local\_ext\_features::max\_page](structbt__hci__rp__read__local__ext__features.md#a3532e208b3fd347db80d8c55eade3c2d)

uint8\_t max\_page

**Definition** hci\_types.h:867

[bt\_hci\_rp\_read\_local\_ext\_features::ext\_features](structbt__hci__rp__read__local__ext__features.md#a669e8c6faa4e45f472e4f8a3ebb03050)

uint8\_t ext\_features[8]

**Definition** hci\_types.h:868

[bt\_hci\_rp\_read\_local\_ext\_features::page](structbt__hci__rp__read__local__ext__features.md#a7e3669651dc2c2ed9541b7e4945a27f9)

uint8\_t page

**Definition** hci\_types.h:866

[bt\_hci\_rp\_read\_local\_ext\_features::status](structbt__hci__rp__read__local__ext__features.md#a9011f2c89f75939fa92fcf249d2203da)

uint8\_t status

**Definition** hci\_types.h:865

[bt\_hci\_rp\_read\_local\_features](structbt__hci__rp__read__local__features.md)

**Definition** hci\_types.h:872

[bt\_hci\_rp\_read\_local\_features::status](structbt__hci__rp__read__local__features.md#a0ff73da5704ada47f8f79c113254820d)

uint8\_t status

**Definition** hci\_types.h:873

[bt\_hci\_rp\_read\_local\_features::features](structbt__hci__rp__read__local__features.md#ae660b4a772f96bf72bd08124bf26b352)

uint8\_t features[8]

**Definition** hci\_types.h:874

[bt\_hci\_rp\_read\_local\_version\_info](structbt__hci__rp__read__local__version__info.md)

**Definition** hci\_types.h:845

[bt\_hci\_rp\_read\_local\_version\_info::hci\_revision](structbt__hci__rp__read__local__version__info.md#a04161ed3cc0b9c3c442e3464501ce118)

uint16\_t hci\_revision

**Definition** hci\_types.h:848

[bt\_hci\_rp\_read\_local\_version\_info::hci\_version](structbt__hci__rp__read__local__version__info.md#a1cc521426e530344a328e935152dd488)

uint8\_t hci\_version

**Definition** hci\_types.h:847

[bt\_hci\_rp\_read\_local\_version\_info::lmp\_subversion](structbt__hci__rp__read__local__version__info.md#a43f29cf08a2399e818bfa441c6b7a1f3)

uint16\_t lmp\_subversion

**Definition** hci\_types.h:851

[bt\_hci\_rp\_read\_local\_version\_info::lmp\_version](structbt__hci__rp__read__local__version__info.md#a634641751852f66aabb408bf1b4d0cd2)

uint8\_t lmp\_version

**Definition** hci\_types.h:849

[bt\_hci\_rp\_read\_local\_version\_info::manufacturer](structbt__hci__rp__read__local__version__info.md#a7cd6ba190137eaf7c4eb9c2d7e5b36ce)

uint16\_t manufacturer

**Definition** hci\_types.h:850

[bt\_hci\_rp\_read\_local\_version\_info::status](structbt__hci__rp__read__local__version__info.md#a935f990f7c28f7c89660c2b8ab975f43)

uint8\_t status

**Definition** hci\_types.h:846

[bt\_hci\_rp\_read\_rssi](structbt__hci__rp__read__rssi.md)

**Definition** hci\_types.h:1012

[bt\_hci\_rp\_read\_rssi::rssi](structbt__hci__rp__read__rssi.md#a1071300bd61fcaab65683187ae393cae)

int8\_t rssi

**Definition** hci\_types.h:1015

[bt\_hci\_rp\_read\_rssi::status](structbt__hci__rp__read__rssi.md#a8f91b69a99bd61a7a59d84b3a9c3f235)

uint8\_t status

**Definition** hci\_types.h:1013

[bt\_hci\_rp\_read\_rssi::handle](structbt__hci__rp__read__rssi.md#aa3c4041dd240b1185c7fc8bbef74a17a)

uint16\_t handle

**Definition** hci\_types.h:1014

[bt\_hci\_rp\_read\_supported\_commands](structbt__hci__rp__read__supported__commands.md)

**Definition** hci\_types.h:855

[bt\_hci\_rp\_read\_supported\_commands::status](structbt__hci__rp__read__supported__commands.md#a3d36d892f83cfcb1d2fc955ec71ff061)

uint8\_t status

**Definition** hci\_types.h:856

[bt\_hci\_rp\_read\_supported\_commands::commands](structbt__hci__rp__read__supported__commands.md#afd0dc4411a4c7692515139392bffedd0)

uint8\_t commands[64]

**Definition** hci\_types.h:857

[bt\_hci\_rp\_read\_tx\_power\_level](structbt__hci__rp__read__tx__power__level.md)

**Definition** hci\_types.h:666

[bt\_hci\_rp\_read\_tx\_power\_level::tx\_power\_level](structbt__hci__rp__read__tx__power__level.md#a46526b820038bb445a7824a7b4bfc870)

int8\_t tx\_power\_level

**Definition** hci\_types.h:669

[bt\_hci\_rp\_read\_tx\_power\_level::handle](structbt__hci__rp__read__tx__power__level.md#ac2bd21e90145102bc483c2b0b3cdd416)

uint16\_t handle

**Definition** hci\_types.h:668

[bt\_hci\_rp\_read\_tx\_power\_level::status](structbt__hci__rp__read__tx__power__level.md#af40a8e2e663872e8d9fdde839cc6d1b4)

uint8\_t status

**Definition** hci\_types.h:667

[bt\_hci\_rp\_remote\_name\_cancel](structbt__hci__rp__remote__name__cancel.md)

**Definition** hci\_types.h:503

[bt\_hci\_rp\_remote\_name\_cancel::bdaddr](structbt__hci__rp__remote__name__cancel.md#a455432799a1272f88b2b00a35a2e7ef5)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:505

[bt\_hci\_rp\_remote\_name\_cancel::status](structbt__hci__rp__remote__name__cancel.md#ac7fadee392b126cb50cef7a6336926cb)

uint8\_t status

**Definition** hci\_types.h:504

[bt\_hci\_rp\_user\_confirm\_reply](structbt__hci__rp__user__confirm__reply.md)

**Definition** hci\_types.h:537

[bt\_hci\_rp\_user\_confirm\_reply::bdaddr](structbt__hci__rp__user__confirm__reply.md#a91678db3ae2a696ba7b9dd5bc080c488)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:539

[bt\_hci\_rp\_user\_confirm\_reply::status](structbt__hci__rp__user__confirm__reply.md#ab07114550c2da3c1e9925cb883bf3a89)

uint8\_t status

**Definition** hci\_types.h:538

[bt\_hci\_rp\_write\_auth\_payload\_timeout](structbt__hci__rp__write__auth__payload__timeout.md)

**Definition** hci\_types.h:810

[bt\_hci\_rp\_write\_auth\_payload\_timeout::handle](structbt__hci__rp__write__auth__payload__timeout.md#a467c6585c913dba03dcfdf5bf4fa688e)

uint16\_t handle

**Definition** hci\_types.h:812

[bt\_hci\_rp\_write\_auth\_payload\_timeout::status](structbt__hci__rp__write__auth__payload__timeout.md#af1783a29e6a167fc20b62bd273215b35)

uint8\_t status

**Definition** hci\_types.h:811

[bt\_hci\_rp\_write\_conn\_accept\_timeout](structbt__hci__rp__write__conn__accept__timeout.md)

**Definition** hci\_types.h:582

[bt\_hci\_rp\_write\_conn\_accept\_timeout::status](structbt__hci__rp__write__conn__accept__timeout.md#a1f9eee1a5843747e0d224b86b602a3da)

uint8\_t status

**Definition** hci\_types.h:583

[bt\_hci\_sco\_hdr](structbt__hci__sco__hdr.md)

**Definition** hci\_types.h:53

[bt\_hci\_sco\_hdr::len](structbt__hci__sco__hdr.md#a158f67c3743684c28728b62db5cf2590)

uint8\_t len

**Definition** hci\_types.h:55

[bt\_hci\_sco\_hdr::handle](structbt__hci__sco__hdr.md#a4b4c915bec966c17567c14e2df9c1581)

uint16\_t handle

**Definition** hci\_types.h:54

[bt\_hci\_std\_codec\_info\_v2](structbt__hci__std__codec__info__v2.md)

**Definition** hci\_types.h:948

[bt\_hci\_std\_codec\_info\_v2::codec\_id](structbt__hci__std__codec__info__v2.md#ae82a0896904c7feb2634579b393bf05e)

uint8\_t codec\_id

**Definition** hci\_types.h:949

[bt\_hci\_std\_codec\_info\_v2::transports](structbt__hci__std__codec__info__v2.md#aea766ba4b911223eeb351e0123e54f5f)

uint8\_t transports

**Definition** hci\_types.h:950

[bt\_hci\_std\_codec\_info](structbt__hci__std__codec__info.md)

**Definition** hci\_types.h:926

[bt\_hci\_std\_codec\_info::codec\_id](structbt__hci__std__codec__info.md#a56e21eca5bbc83cb081aea1c67a7a60d)

uint8\_t codec\_id

**Definition** hci\_types.h:927

[bt\_hci\_std\_codecs\_v2](structbt__hci__std__codecs__v2.md)

**Definition** hci\_types.h:952

[bt\_hci\_std\_codecs\_v2::codec\_info](structbt__hci__std__codecs__v2.md#aafdb6d96d99063a7a447d80e1830a624)

struct bt\_hci\_std\_codec\_info\_v2 codec\_info[0]

**Definition** hci\_types.h:954

[bt\_hci\_std\_codecs\_v2::num\_codecs](structbt__hci__std__codecs__v2.md#ab14fdde478e290235f68aae375969c09)

uint8\_t num\_codecs

**Definition** hci\_types.h:953

[bt\_hci\_std\_codecs](structbt__hci__std__codecs.md)

**Definition** hci\_types.h:929

[bt\_hci\_std\_codecs::codec\_info](structbt__hci__std__codecs.md#a32767e90384ef74a3e740597eacfcf53)

struct bt\_hci\_std\_codec\_info codec\_info[0]

**Definition** hci\_types.h:931

[bt\_hci\_std\_codecs::num\_codecs](structbt__hci__std__codecs.md#ad3e63bf445bb6b8e654baa8490cdf547)

uint8\_t num\_codecs

**Definition** hci\_types.h:930

[bt\_hci\_vs\_codec\_info\_v2](structbt__hci__vs__codec__info__v2.md)

**Definition** hci\_types.h:956

[bt\_hci\_vs\_codec\_info\_v2::company\_id](structbt__hci__vs__codec__info__v2.md#aa6ce27b4acd3dff516e4d7ed2e6434bc)

uint16\_t company\_id

**Definition** hci\_types.h:957

[bt\_hci\_vs\_codec\_info\_v2::transports](structbt__hci__vs__codec__info__v2.md#ac2a91a045e4b53315850b6d4f1d38b2c)

uint8\_t transports

**Definition** hci\_types.h:959

[bt\_hci\_vs\_codec\_info\_v2::codec\_id](structbt__hci__vs__codec__info__v2.md#ae7b7d5d65629a1e3039b3c7cf167a9c1)

uint16\_t codec\_id

**Definition** hci\_types.h:958

[bt\_hci\_vs\_codec\_info](structbt__hci__vs__codec__info.md)

**Definition** hci\_types.h:933

[bt\_hci\_vs\_codec\_info::codec\_id](structbt__hci__vs__codec__info.md#a3c7eea7bae36c7a63457051401526382)

uint16\_t codec\_id

**Definition** hci\_types.h:935

[bt\_hci\_vs\_codec\_info::company\_id](structbt__hci__vs__codec__info.md#a8170dac825b76f3dfb5fde5eed04c4c0)

uint16\_t company\_id

**Definition** hci\_types.h:934

[bt\_hci\_vs\_codecs\_v2](structbt__hci__vs__codecs__v2.md)

**Definition** hci\_types.h:961

[bt\_hci\_vs\_codecs\_v2::codec\_info](structbt__hci__vs__codecs__v2.md#a6cd8aa58517d59d565474513f755cfee)

struct bt\_hci\_vs\_codec\_info\_v2 codec\_info[0]

**Definition** hci\_types.h:963

[bt\_hci\_vs\_codecs\_v2::num\_codecs](structbt__hci__vs__codecs__v2.md#ae4cb3a40401594f8e0f18391b9d31a23)

uint8\_t num\_codecs

**Definition** hci\_types.h:962

[bt\_hci\_vs\_codecs](structbt__hci__vs__codecs.md)

**Definition** hci\_types.h:937

[bt\_hci\_vs\_codecs::num\_codecs](structbt__hci__vs__codecs.md#a2caf18ce5905e3962da000f3b00b623f)

uint8\_t num\_codecs

**Definition** hci\_types.h:938

[bt\_hci\_vs\_codecs::codec\_info](structbt__hci__vs__codecs.md#a4e72426599d5bc617fde4f1a4a095527)

struct bt\_hci\_vs\_codec\_info codec\_info[0]

**Definition** hci\_types.h:939

[bt\_hci\_write\_local\_name](structbt__hci__write__local__name.md)

**Definition** hci\_types.h:567

[bt\_hci\_write\_local\_name::local\_name](structbt__hci__write__local__name.md#a8d2cd9a16525c3fc10ae0e3f196110da)

uint8\_t local\_name[248]

**Definition** hci\_types.h:568

[hci\_cp\_le\_conn\_update](structhci__cp__le__conn__update.md)

**Definition** hci\_types.h:1185

[hci\_cp\_le\_conn\_update::min\_ce\_len](structhci__cp__le__conn__update.md#a3ae86fccacf462463fe520eb1e06fa62)

uint16\_t min\_ce\_len

**Definition** hci\_types.h:1191

[hci\_cp\_le\_conn\_update::max\_ce\_len](structhci__cp__le__conn__update.md#a401169ccc5dbf6cf0abd6154738f00dc)

uint16\_t max\_ce\_len

**Definition** hci\_types.h:1192

[hci\_cp\_le\_conn\_update::handle](structhci__cp__le__conn__update.md#a5606b8795defc338b27d1a130064351e)

uint16\_t handle

**Definition** hci\_types.h:1186

[hci\_cp\_le\_conn\_update::conn\_latency](structhci__cp__le__conn__update.md#a8e48e5e195aea7f581cfc7246da79d72)

uint16\_t conn\_latency

**Definition** hci\_types.h:1189

[hci\_cp\_le\_conn\_update::conn\_interval\_max](structhci__cp__le__conn__update.md#a99fc0b3b0f810f1d6e174aa9045d298a)

uint16\_t conn\_interval\_max

**Definition** hci\_types.h:1188

[hci\_cp\_le\_conn\_update::supervision\_timeout](structhci__cp__le__conn__update.md#ab76ecdf6f7e5a5bb581cbd26f67d8f9f)

uint16\_t supervision\_timeout

**Definition** hci\_types.h:1190

[hci\_cp\_le\_conn\_update::conn\_interval\_min](structhci__cp__le__conn__update.md#adcfee3c727118069897515a00e7ead66)

uint16\_t conn\_interval\_min

**Definition** hci\_types.h:1187

[util.h](sys_2util_8h.md)

Misc utilities.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [hci\_types.h](hci__types_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

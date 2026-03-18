---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/hci__types_8h_source.html
original_path: doxygen/html/hci__types_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

18#include <[zephyr/sys/util.h](util_8h.md)>

19#include <[zephyr/bluetooth/addr.h](addr_8h.md)>

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

25/\* Special own address types for LL privacy (used in adv & scan parameters) \*/

[ 26](hci__types_8h.md#a92a5db1ce46bbf3ddeaab4da76bc6685)#define BT\_HCI\_OWN\_ADDR\_RPA\_OR\_PUBLIC 0x02

[ 27](hci__types_8h.md#aec05e679e29fde812e9a066e672405b4)#define BT\_HCI\_OWN\_ADDR\_RPA\_OR\_RANDOM 0x03

[ 28](hci__types_8h.md#a115907057c92a59a407d261133946b59)#define BT\_HCI\_OWN\_ADDR\_RPA\_MASK 0x02

29

[ 30](hci__types_8h.md#aebc5bd975899f765afe697ab322db114)#define BT\_HCI\_PEER\_ADDR\_RPA\_UNRESOLVED 0xfe

[ 31](hci__types_8h.md#a1e6d78149d0990511b2b6dffb617069e)#define BT\_HCI\_PEER\_ADDR\_ANONYMOUS 0xff

32

[ 33](hci__types_8h.md#a90a6c0c50f915c347b75ac3ca46996ac)#define BT\_ENC\_KEY\_SIZE\_MIN 0x07

[ 34](hci__types_8h.md#a4c274cd6947d37bf4f895ca0002c4f63)#define BT\_ENC\_KEY\_SIZE\_MAX 0x10

35

[ 36](hci__types_8h.md#aa85640ad3a1aa78cf862a5d8b2567fa1)#define BT\_HCI\_ADV\_HANDLE\_INVALID 0xff

[ 37](hci__types_8h.md#a4e4a6e6bb2dc713de8cb7c12139583ed)#define BT\_HCI\_SYNC\_HANDLE\_INVALID 0xffff

[ 38](hci__types_8h.md#a98554ced76600577254b4124b27ef8a8)#define BT\_HCI\_PAWR\_SUBEVENT\_MAX 128

39

40/\* Bluetooth spec v5.4 Vol 4, Part E - 5.4.3 HCI Synchronous Data Packets \*/

[ 41](structbt__hci__sco__hdr.md)struct [bt\_hci\_sco\_hdr](structbt__hci__sco__hdr.md) {

[ 42](structbt__hci__sco__hdr.md#a4b4c915bec966c17567c14e2df9c1581) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__sco__hdr.md#a4b4c915bec966c17567c14e2df9c1581); /\* 12 bit handle, 2 bit Packet Status Flag, 1 bit RFU \*/

[ 43](structbt__hci__sco__hdr.md#a158f67c3743684c28728b62db5cf2590) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structbt__hci__sco__hdr.md#a158f67c3743684c28728b62db5cf2590);

44} \_\_packed;

[ 45](hci__types_8h.md#acb8daef29a7f5f2d11a169fd10ae0caa)#define BT\_HCI\_SCO\_HDR\_SIZE 3

46

47/\* Bluetooth spec v5.4 Vol 4, Part E - 5.4.4 HCI Event Packet \*/

[ 48](structbt__hci__evt__hdr.md)struct [bt\_hci\_evt\_hdr](structbt__hci__evt__hdr.md) {

[ 49](structbt__hci__evt__hdr.md#aba3aca89bfbe7e8cbd144765cb20fcea) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [evt](structbt__hci__evt__hdr.md#aba3aca89bfbe7e8cbd144765cb20fcea);

[ 50](structbt__hci__evt__hdr.md#a2d580a0c12b29d23002ee9d494c9e16d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structbt__hci__evt__hdr.md#a2d580a0c12b29d23002ee9d494c9e16d);

51} \_\_packed;

[ 52](hci__types_8h.md#a0edb7e700cfa557e7fb8ec44f5eea961)#define BT\_HCI\_EVT\_HDR\_SIZE 2

53

[ 54](hci__types_8h.md#ae8c5ddd450d47b45a310bc979207ebff)#define BT\_ACL\_START\_NO\_FLUSH 0x00

[ 55](hci__types_8h.md#a0bfb8a0bac96eb223eb8229c1dff9e7d)#define BT\_ACL\_CONT 0x01

[ 56](hci__types_8h.md#a49c9728293c37e718c009ad973f6d43e)#define BT\_ACL\_START 0x02

[ 57](hci__types_8h.md#ad6f24425a0818730d2377e159698922b)#define BT\_ACL\_COMPLETE 0x03

58

[ 59](hci__types_8h.md#a343e6550f9a24a59c5a08efd2dab16bb)#define BT\_ACL\_POINT\_TO\_POINT 0x00

[ 60](hci__types_8h.md#a2f9e6232229ae1bed3d835b5f6531a76)#define BT\_ACL\_BROADCAST 0x01

61

[ 62](hci__types_8h.md#a28a9f26ba563e2687856aff39b044039)#define BT\_ACL\_HANDLE\_MASK BIT\_MASK(12)

63

[ 64](hci__types_8h.md#a500341d3485843d85dc034ce6f8a908c)#define bt\_acl\_handle(h) ((h) & BT\_ACL\_HANDLE\_MASK)

[ 65](hci__types_8h.md#a499f8647747fd6b7b82d9b3280b4b048)#define bt\_acl\_flags(h) ((h) >> 12)

[ 66](hci__types_8h.md#ae358e74ce455f11bb134700ec80fe07b)#define bt\_acl\_flags\_pb(f) ((f) & BIT\_MASK(2))

[ 67](hci__types_8h.md#a55cfcca3e0a6a7401e57e7430421093e)#define bt\_acl\_flags\_bc(f) ((f) >> 2)

[ 68](hci__types_8h.md#aa08e6239d84ce55153baa41f46814363)#define bt\_acl\_handle\_pack(h, f) ((h) | ((f) << 12))

69

70/\* Bluetooth spec v5.4 Vol 4, Part E - 5.4.2 ACL Data Packets \*/

[ 71](structbt__hci__acl__hdr.md)struct [bt\_hci\_acl\_hdr](structbt__hci__acl__hdr.md) {

[ 72](structbt__hci__acl__hdr.md#a8c88ef62a848699e06c49f97e1169363) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__acl__hdr.md#a8c88ef62a848699e06c49f97e1169363);

[ 73](structbt__hci__acl__hdr.md#af55b9c9256f35ada5786e9e5dd1d01bf) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structbt__hci__acl__hdr.md#af55b9c9256f35ada5786e9e5dd1d01bf);

74} \_\_packed;

[ 75](hci__types_8h.md#a7418d845532d6b077a9695454fa65bc5)#define BT\_HCI\_ACL\_HDR\_SIZE 4

76

[ 77](hci__types_8h.md#a9ef86241b4dfb462ec31c855bce4ee28)#define BT\_ISO\_START 0x00

[ 78](hci__types_8h.md#a06c43e91abee990343ece9c22f5a515e)#define BT\_ISO\_CONT 0x01

[ 79](hci__types_8h.md#a1db9801de1c97b2d15cf9d2f0ec2a5f0)#define BT\_ISO\_SINGLE 0x02

[ 80](hci__types_8h.md#ac2da3db69ba73112fff5bf16ef386cb3)#define BT\_ISO\_END 0x03

81

[ 82](hci__types_8h.md#adcdb9dd367b64a820a040724c1c42c15)#define bt\_iso\_handle(h) ((h) & 0x0fff)

[ 83](hci__types_8h.md#a54e2f7efc0f22287d65bdd560dd7ec78)#define bt\_iso\_flags(h) ((h) >> 12)

[ 84](hci__types_8h.md#a7ea328491745f1bde6e2b376c19cc380)#define bt\_iso\_flags\_pb(f) ((f) & 0x0003)

[ 85](hci__types_8h.md#aed6d45daf19ce7fadc1c8fbcc79c9e8a)#define bt\_iso\_flags\_ts(f) (((f) >> 2) & 0x0001)

[ 86](hci__types_8h.md#a9bdbdc6e181731a58ec91d53cdade532)#define bt\_iso\_pack\_flags(pb, ts) \

87 (((pb) & 0x0003) | (((ts) & 0x0001) << 2))

[ 88](hci__types_8h.md#ab96b2d1b49a86ee96b2254b624b2e93f)#define bt\_iso\_handle\_pack(h, pb, ts) \

89 ((h) | (bt\_iso\_pack\_flags(pb, ts) << 12))

[ 90](hci__types_8h.md#a128d269790ccf3f8dcdeb51f80697ba0)#define bt\_iso\_hdr\_len(h) ((h) & BIT\_MASK(14))

91

[ 92](hci__types_8h.md#a52091a307cca85d8d39fbfe5be6b6179)#define BT\_ISO\_DATA\_VALID 0x00

[ 93](hci__types_8h.md#a7149213544fe2ac9e7d3d0fd64ecb271)#define BT\_ISO\_DATA\_INVALID 0x01

[ 94](hci__types_8h.md#ae736b21ff7b99c4bb85df1a3f4bee9cd)#define BT\_ISO\_DATA\_NOP 0x02

95

[ 96](hci__types_8h.md#a0d540918a423992f5f244febcc82248a)#define bt\_iso\_pkt\_len(h) ((h) & BIT\_MASK(12))

[ 97](hci__types_8h.md#a6dbade5730a92ea7f85017792939e941)#define bt\_iso\_pkt\_flags(h) ((h) >> 14)

[ 98](hci__types_8h.md#a3683be1ceedbcb97f61483b6fa4344e6)#define bt\_iso\_pkt\_len\_pack(h, f) (((h) & BIT\_MASK(12)) | ((f) << 14))

99

[ 100](structbt__hci__iso__data__hdr.md)struct [bt\_hci\_iso\_data\_hdr](structbt__hci__iso__data__hdr.md) {

[ 101](structbt__hci__iso__data__hdr.md#a66ed7e709658d3bb3ead2c7242e596b1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sn](structbt__hci__iso__data__hdr.md#a66ed7e709658d3bb3ead2c7242e596b1);

[ 102](structbt__hci__iso__data__hdr.md#ab04366e16e692bb4664c0cdbf89983eb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [slen](structbt__hci__iso__data__hdr.md#ab04366e16e692bb4664c0cdbf89983eb); /\* 12 bit len, 2 bit RFU, 2 bit packet status \*/

103} \_\_packed;

[ 104](hci__types_8h.md#a7c351e4eb31cdd5469cfecbbff0a1db0)#define BT\_HCI\_ISO\_DATA\_HDR\_SIZE 4

105

[ 106](structbt__hci__iso__ts__data__hdr.md)struct [bt\_hci\_iso\_ts\_data\_hdr](structbt__hci__iso__ts__data__hdr.md) {

[ 107](structbt__hci__iso__ts__data__hdr.md#a58c5a3c5dc0aaf7d498b7ecaea6595bd) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ts](structbt__hci__iso__ts__data__hdr.md#a58c5a3c5dc0aaf7d498b7ecaea6595bd);

[ 108](structbt__hci__iso__ts__data__hdr.md#a77cb6fe6584e603488ac5949bf6bf736) struct [bt\_hci\_iso\_data\_hdr](structbt__hci__iso__data__hdr.md) [data](structbt__hci__iso__ts__data__hdr.md#a77cb6fe6584e603488ac5949bf6bf736);

109} \_\_packed;

[ 110](hci__types_8h.md#a0ad84468158c3df92d4dd2fb10771f6e)#define BT\_HCI\_ISO\_TS\_DATA\_HDR\_SIZE 8

111

112/\* Bluetooth spec v5.4 Vol 4, Part E - 5.4.5 HCI ISO Data Packets \*/

[ 113](structbt__hci__iso__hdr.md)struct [bt\_hci\_iso\_hdr](structbt__hci__iso__hdr.md) {

[ 114](structbt__hci__iso__hdr.md#af5113383fbcd0e70828f986720c38572) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__iso__hdr.md#af5113383fbcd0e70828f986720c38572); /\* 12 bit handle, 2 bit PB flags, 1 bit TS\_Flag, 1 bit RFU \*/

[ 115](structbt__hci__iso__hdr.md#ab33ae914a9eba85b35c78e45e0f5255f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structbt__hci__iso__hdr.md#ab33ae914a9eba85b35c78e45e0f5255f); /\* 14 bits, 2 bits RFU \*/

116} \_\_packed;

[ 117](hci__types_8h.md#a75c1f5e8a44b034004ecfebdb75ee4be)#define BT\_HCI\_ISO\_HDR\_SIZE 4

118

119/\* Bluetooth spec v5.4 Vol 4, Part E - 5.4.1 HCI Command Packet \*/

[ 120](structbt__hci__cmd__hdr.md)struct [bt\_hci\_cmd\_hdr](structbt__hci__cmd__hdr.md) {

[ 121](structbt__hci__cmd__hdr.md#a09c63aab094ca0f39bab44708fdb83e4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [opcode](structbt__hci__cmd__hdr.md#a09c63aab094ca0f39bab44708fdb83e4);

[ 122](structbt__hci__cmd__hdr.md#afe2a97da8b473cafd3cc4e5e52dadf93) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [param\_len](structbt__hci__cmd__hdr.md#afe2a97da8b473cafd3cc4e5e52dadf93);

123} \_\_packed;

[ 124](hci__types_8h.md#acdf2b6de1459a7492415a8987ad9a896)#define BT\_HCI\_CMD\_HDR\_SIZE 3

125

126/\* Supported Commands \*/

[ 127](hci__types_8h.md#a7d5bc35e597d03fbc65084b39771cf0b)#define BT\_CMD\_TEST(cmd, octet, bit) (cmd[octet] & BIT(bit))

[ 128](hci__types_8h.md#ae3aaad5ae408cb8c72a29ff7a8817c21)#define BT\_CMD\_LE\_STATES(cmd) BT\_CMD\_TEST(cmd, 28, 3)

129

[ 130](hci__types_8h.md#a41e5b49e645ed511340a61f843f6b238)#define BT\_FEAT\_TEST(feat, page, octet, bit) (feat[page][octet] & BIT(bit))

131

[ 132](hci__types_8h.md#a5508c481ff6b8fd46f2f2c077aaa90c9)#define BT\_FEAT\_BREDR(feat) !BT\_FEAT\_TEST(feat, 0, 4, 5)

[ 133](hci__types_8h.md#a8b1df8d6b9e0dfcaa13635588cc3bfe3)#define BT\_FEAT\_LE(feat) BT\_FEAT\_TEST(feat, 0, 4, 6)

[ 134](hci__types_8h.md#ac26ebac4f1641d5ff4484f74579852d7)#define BT\_FEAT\_EXT\_FEATURES(feat) BT\_FEAT\_TEST(feat, 0, 7, 7)

[ 135](hci__types_8h.md#af011519b6fb0477ac7f87e5dc98daed0)#define BT\_FEAT\_HOST\_SSP(feat) BT\_FEAT\_TEST(feat, 1, 0, 0)

[ 136](hci__types_8h.md#a9ecf892ec94af8cbfd2e6c99310b1fa2)#define BT\_FEAT\_SC(feat) BT\_FEAT\_TEST(feat, 2, 1, 0)

137

[ 138](hci__types_8h.md#a24f24640d9f52adb15336a1b17122346)#define BT\_FEAT\_LMP\_SCO\_CAPABLE(feat) BT\_FEAT\_TEST(feat, 0, 1, 3)

[ 139](hci__types_8h.md#a7622a2fc0a65f82a827ab3cc84e4e7c5)#define BT\_FEAT\_LMP\_ESCO\_CAPABLE(feat) BT\_FEAT\_TEST(feat, 0, 3, 7)

[ 140](hci__types_8h.md#ad59c138e945d7f27d3befc286b679e03)#define BT\_FEAT\_HV2\_PKT(feat) BT\_FEAT\_TEST(feat, 0, 1, 4)

[ 141](hci__types_8h.md#aed6f11d60161c919b4d2b7eb13f46e47)#define BT\_FEAT\_HV3\_PKT(feat) BT\_FEAT\_TEST(feat, 0, 1, 5)

[ 142](hci__types_8h.md#ad154d0649e8e90c1102b74cae8327fa7)#define BT\_FEAT\_EV4\_PKT(feat) BT\_FEAT\_TEST(feat, 0, 4, 0)

[ 143](hci__types_8h.md#a0a6b9afb4673dc852e1a4d8e867003c9)#define BT\_FEAT\_EV5\_PKT(feat) BT\_FEAT\_TEST(feat, 0, 4, 1)

[ 144](hci__types_8h.md#a8dbbf37965a9d0ddab5a07f88d7cd7ca)#define BT\_FEAT\_2EV3\_PKT(feat) BT\_FEAT\_TEST(feat, 0, 5, 5)

[ 145](hci__types_8h.md#a00aec89aa4d1504934e85ec79462b346)#define BT\_FEAT\_3EV3\_PKT(feat) BT\_FEAT\_TEST(feat, 0, 5, 6)

[ 146](hci__types_8h.md#a5219ff658b46cf28104a99f089854444)#define BT\_FEAT\_3SLOT\_PKT(feat) BT\_FEAT\_TEST(feat, 0, 5, 7)

147

148/\* LE features \*/

[ 149](hci__types_8h.md#abd616dd5af5ed3742be9bae400ded848)#define BT\_LE\_FEAT\_BIT\_ENC 0

[ 150](hci__types_8h.md#ab816048bdd6c1e42b0e458abebb76572)#define BT\_LE\_FEAT\_BIT\_CONN\_PARAM\_REQ 1

[ 151](hci__types_8h.md#ae5644021aff31996c09f6edf3ede197c)#define BT\_LE\_FEAT\_BIT\_EXT\_REJ\_IND 2

[ 152](hci__types_8h.md#aeaea6ea6595de9e3283fd6063bf7c579)#define BT\_LE\_FEAT\_BIT\_PER\_INIT\_FEAT\_XCHG 3

[ 153](hci__types_8h.md#a9b4dc56ef4433b0c0dc74a3d95cf289e)#define BT\_LE\_FEAT\_BIT\_PING 4

[ 154](hci__types_8h.md#ac09127210b281e5ee45fbc134df64aa6)#define BT\_LE\_FEAT\_BIT\_DLE 5

[ 155](hci__types_8h.md#a3c4196c04a73aa537baa845e061e9654)#define BT\_LE\_FEAT\_BIT\_PRIVACY 6

[ 156](hci__types_8h.md#a8f1fa8948f79bec50373e0342ab0969a)#define BT\_LE\_FEAT\_BIT\_EXT\_SCAN 7

[ 157](hci__types_8h.md#afcbc8d664c8e924b777c06ffb4c17315)#define BT\_LE\_FEAT\_BIT\_PHY\_2M 8

[ 158](hci__types_8h.md#aea19f3c3cdcec054c81c176d5aa5f319)#define BT\_LE\_FEAT\_BIT\_SMI\_TX 9

[ 159](hci__types_8h.md#a9430a65ea813861b6890252ed4748f19)#define BT\_LE\_FEAT\_BIT\_SMI\_RX 10

[ 160](hci__types_8h.md#a800686aa45cf336fbd6efc76b3752959)#define BT\_LE\_FEAT\_BIT\_PHY\_CODED 11

[ 161](hci__types_8h.md#ae1a0751e7c380117c4e31741712096a4)#define BT\_LE\_FEAT\_BIT\_EXT\_ADV 12

[ 162](hci__types_8h.md#a1ac5bab6d48775b4e63e249b5759a683)#define BT\_LE\_FEAT\_BIT\_PER\_ADV 13

[ 163](hci__types_8h.md#a9120867d6f31465cb5f085b610d5ed70)#define BT\_LE\_FEAT\_BIT\_CHAN\_SEL\_ALGO\_2 14

[ 164](hci__types_8h.md#a938f823110f31a3a5d034cbe9b9d26eb)#define BT\_LE\_FEAT\_BIT\_PWR\_CLASS\_1 15

[ 165](hci__types_8h.md#ac8cf36c670ae359ec24e62efb4505758)#define BT\_LE\_FEAT\_BIT\_MIN\_USED\_CHAN\_PROC 16

[ 166](hci__types_8h.md#aed34742e8554b830c3b6c4bf04f0e2db)#define BT\_LE\_FEAT\_BIT\_CONN\_CTE\_REQ 17

[ 167](hci__types_8h.md#aa5279a2ce26decb5856a6b709d0641c9)#define BT\_LE\_FEAT\_BIT\_CONN\_CTE\_RESP 18

[ 168](hci__types_8h.md#a331e7697a3fdc073abba5dd0ff47346b)#define BT\_LE\_FEAT\_BIT\_CONNECTIONLESS\_CTE\_TX 19

[ 169](hci__types_8h.md#a6abf01c846a5d637ca98997f6cfc263d)#define BT\_LE\_FEAT\_BIT\_CONNECTIONLESS\_CTE\_RX 20

[ 170](hci__types_8h.md#a41eae1585972ae6792eb1a639c2e3a8e)#define BT\_LE\_FEAT\_BIT\_ANT\_SWITCH\_TX\_AOD 21

[ 171](hci__types_8h.md#a480fc67a1c8a2f36410f285ef0ee36e7)#define BT\_LE\_FEAT\_BIT\_ANT\_SWITCH\_RX\_AOA 22

[ 172](hci__types_8h.md#a9d9449f1935d6522291eca581f3fa9b0)#define BT\_LE\_FEAT\_BIT\_RX\_CTE 23

[ 173](hci__types_8h.md#aa05da01a6a9b9ac26423d6fc2661f3db)#define BT\_LE\_FEAT\_BIT\_PAST\_SEND 24

[ 174](hci__types_8h.md#a28a862eaf11f8b45237f3b87e4bb15c7)#define BT\_LE\_FEAT\_BIT\_PAST\_RECV 25

[ 175](hci__types_8h.md#a829e9d23a16912bad19448a6c4061e3b)#define BT\_LE\_FEAT\_BIT\_SCA\_UPDATE 26

[ 176](hci__types_8h.md#a6d17dd4238ea471daca22f74e3cc3bcb)#define BT\_LE\_FEAT\_BIT\_REMOTE\_PUB\_KEY\_VALIDATE 27

[ 177](hci__types_8h.md#aa98eed376b6d5263621f14c55d776088)#define BT\_LE\_FEAT\_BIT\_CIS\_CENTRAL 28

[ 178](hci__types_8h.md#a298fde96c2d6376e3333a99f7e03409d)#define BT\_LE\_FEAT\_BIT\_CIS\_PERIPHERAL 29

[ 179](hci__types_8h.md#af08a1ffd734d1c211f38d90b4fe72417)#define BT\_LE\_FEAT\_BIT\_ISO\_BROADCASTER 30

[ 180](hci__types_8h.md#a2fed771f5611212e48027025e11f7678)#define BT\_LE\_FEAT\_BIT\_SYNC\_RECEIVER 31

[ 181](hci__types_8h.md#a0d80ccb33d263abd3b42de1b69cfeeeb)#define BT\_LE\_FEAT\_BIT\_ISO\_CHANNELS 32

[ 182](hci__types_8h.md#ae58f5260530d1b94608874f5d03d766d)#define BT\_LE\_FEAT\_BIT\_PWR\_CTRL\_REQ 33

[ 183](hci__types_8h.md#a0138172a0ed78244d8d3ac9d6936cf85)#define BT\_LE\_FEAT\_BIT\_PWR\_CHG\_IND 34

[ 184](hci__types_8h.md#a434fb43b6b3176393f5d22d3932d69fa)#define BT\_LE\_FEAT\_BIT\_PATH\_LOSS\_MONITOR 35

[ 185](hci__types_8h.md#ad5a8221cb25d79b63f1a574699983038)#define BT\_LE\_FEAT\_BIT\_PER\_ADV\_ADI\_SUPP 36

[ 186](hci__types_8h.md#aa45b06a49232372891ceb5e4496d46da)#define BT\_LE\_FEAT\_BIT\_CONN\_SUBRATING 37

[ 187](hci__types_8h.md#adb884a30bc1a24e3dfb115cef7149c81)#define BT\_LE\_FEAT\_BIT\_CONN\_SUBRATING\_HOST\_SUPP 38

[ 188](hci__types_8h.md#af2a4be520b4d8c3eb56231b865738e90)#define BT\_LE\_FEAT\_BIT\_CHANNEL\_CLASSIFICATION 39

189

[ 190](hci__types_8h.md#af251cb9d905586fd53113f5920038dae)#define BT\_LE\_FEAT\_BIT\_PAWR\_ADVERTISER 43

[ 191](hci__types_8h.md#a00bb51972e0db07be84d4f3dfd007cea)#define BT\_LE\_FEAT\_BIT\_PAWR\_SCANNER 44

192

[ 193](hci__types_8h.md#a6bf20989952fed3726bc45873beb896e)#define BT\_LE\_FEAT\_TEST(feat, n) (feat[(n) >> 3] & \

194 BIT((n) & 7))

195

[ 196](hci__types_8h.md#a51464aacf5bbcbfb873fa6c757bbcd79)#define BT\_FEAT\_LE\_ENCR(feat) BT\_LE\_FEAT\_TEST(feat, \

197 BT\_LE\_FEAT\_BIT\_ENC)

[ 198](hci__types_8h.md#a554c027fb3946de6f861ea267968ba17)#define BT\_FEAT\_LE\_CONN\_PARAM\_REQ\_PROC(feat) BT\_LE\_FEAT\_TEST(feat, \

199 BT\_LE\_FEAT\_BIT\_CONN\_PARAM\_REQ)

[ 200](hci__types_8h.md#a132b2561dcd4140458fb612b6e0d8b25)#define BT\_FEAT\_LE\_PER\_INIT\_FEAT\_XCHG(feat) BT\_LE\_FEAT\_TEST(feat, \

201 BT\_LE\_FEAT\_BIT\_PER\_INIT\_FEAT\_XCHG)

[ 202](hci__types_8h.md#a62e7d152cd9dfabf5b1420945099ecb6)#define BT\_FEAT\_LE\_DLE(feat) BT\_LE\_FEAT\_TEST(feat, \

203 BT\_LE\_FEAT\_BIT\_DLE)

[ 204](hci__types_8h.md#aaf11993f4938bb4894cdd317f9386fa3)#define BT\_FEAT\_LE\_PHY\_2M(feat) BT\_LE\_FEAT\_TEST(feat, \

205 BT\_LE\_FEAT\_BIT\_PHY\_2M)

[ 206](hci__types_8h.md#abb89a0bebe4046ae310b01dd27e02c99)#define BT\_FEAT\_LE\_PHY\_CODED(feat) BT\_LE\_FEAT\_TEST(feat, \

207 BT\_LE\_FEAT\_BIT\_PHY\_CODED)

[ 208](hci__types_8h.md#a0b2781f29085a5807d0b2235c32f5173)#define BT\_FEAT\_LE\_PRIVACY(feat) BT\_LE\_FEAT\_TEST(feat, \

209 BT\_LE\_FEAT\_BIT\_PRIVACY)

[ 210](hci__types_8h.md#a8bce94a732d28ce74ad2663e01da09b2)#define BT\_FEAT\_LE\_EXT\_ADV(feat) BT\_LE\_FEAT\_TEST(feat, \

211 BT\_LE\_FEAT\_BIT\_EXT\_ADV)

[ 212](hci__types_8h.md#a5d479d919db4920b7a53c054e4ae7a19)#define BT\_FEAT\_LE\_EXT\_PER\_ADV(feat) BT\_LE\_FEAT\_TEST(feat, \

213 BT\_LE\_FEAT\_BIT\_PER\_ADV)

[ 214](hci__types_8h.md#a51316a5b67950e7644dfb71c4c6baa96)#define BT\_FEAT\_LE\_CONNECTION\_CTE\_REQ(feat) BT\_LE\_FEAT\_TEST(feat, \

215 BT\_LE\_FEAT\_BIT\_CONN\_CTE\_REQ)

[ 216](hci__types_8h.md#a0cdc67a1345969d3504380fce94a4cda)#define BT\_FEAT\_LE\_CONNECTION\_CTE\_RESP(feat) BT\_LE\_FEAT\_TEST(feat, \

217 BT\_LE\_FEAT\_BIT\_CONN\_CTE\_RESP)

[ 218](hci__types_8h.md#a81e30f5630750ce4f805748fbe14b456)#define BT\_FEAT\_LE\_CONNECTIONLESS\_CTE\_TX(feat) BT\_LE\_FEAT\_TEST(feat, \

219 BT\_LE\_FEAT\_BIT\_CONNECTIONLESS\_CTE\_TX)

[ 220](hci__types_8h.md#aeb0639a8e5cbc904d7f5c02d72375913)#define BT\_FEAT\_LE\_CONNECTIONLESS\_CTE\_RX(feat) BT\_LE\_FEAT\_TEST(feat, \

221 BT\_LE\_FEAT\_BIT\_CONNECTIONLESS\_CTE\_RX)

[ 222](hci__types_8h.md#ae503f9186d39fbea2347036c891fc8bf)#define BT\_FEAT\_LE\_ANT\_SWITCH\_TX\_AOD(feat) BT\_LE\_FEAT\_TEST(feat, \

223 BT\_LE\_FEAT\_BIT\_ANT\_SWITCH\_TX\_AOD)

[ 224](hci__types_8h.md#a1c3c0e6a213b71e680ca24738047f09a)#define BT\_FEAT\_LE\_ANT\_SWITCH\_RX\_AOA(feat) BT\_LE\_FEAT\_TEST(feat, \

225 BT\_LE\_FEAT\_BIT\_ANT\_SWITCH\_RX\_AOA)

[ 226](hci__types_8h.md#adf4303d47abfab3bd23080c545b77ef7)#define BT\_FEAT\_LE\_RX\_CTE(feat) BT\_LE\_FEAT\_TEST(feat, \

227 BT\_LE\_FEAT\_BIT\_RX\_CTE)

[ 228](hci__types_8h.md#a9e68dcf290273a4a140645c187cd7aee)#define BT\_FEAT\_LE\_PAST\_SEND(feat) BT\_LE\_FEAT\_TEST(feat, \

229 BT\_LE\_FEAT\_BIT\_PAST\_SEND)

[ 230](hci__types_8h.md#a7a88046c26b3603a2bb8b0f2ee158b5f)#define BT\_FEAT\_LE\_PAST\_RECV(feat) BT\_LE\_FEAT\_TEST(feat, \

231 BT\_LE\_FEAT\_BIT\_PAST\_RECV)

[ 232](hci__types_8h.md#adce7c3804a224e7b7317728fa27d4945)#define BT\_FEAT\_LE\_CIS\_CENTRAL(feat) BT\_LE\_FEAT\_TEST(feat, \

233 BT\_LE\_FEAT\_BIT\_CIS\_CENTRAL)

[ 234](hci__types_8h.md#a8a6860b285b3b4401021ba16f59404ce)#define BT\_FEAT\_LE\_CIS\_PERIPHERAL(feat) BT\_LE\_FEAT\_TEST(feat, \

235 BT\_LE\_FEAT\_BIT\_CIS\_PERIPHERAL)

[ 236](hci__types_8h.md#a1c6fd06877a5606ae33aedc45a71f853)#define BT\_FEAT\_LE\_ISO\_BROADCASTER(feat) BT\_LE\_FEAT\_TEST(feat, \

237 BT\_LE\_FEAT\_BIT\_ISO\_BROADCASTER)

[ 238](hci__types_8h.md#af33c8331e204eeee2a7a02e2ad46c7a2)#define BT\_FEAT\_LE\_SYNC\_RECEIVER(feat) BT\_LE\_FEAT\_TEST(feat, \

239 BT\_LE\_FEAT\_BIT\_SYNC\_RECEIVER)

[ 240](hci__types_8h.md#a0b24b74715fbf84c2da2dd2cbbb34605)#define BT\_FEAT\_LE\_ISO\_CHANNELS(feat) BT\_LE\_FEAT\_TEST(feat, \

241 BT\_LE\_FEAT\_BIT\_ISO\_CHANNELS)

[ 242](hci__types_8h.md#a8ab0d3ca572861bb1c40191766481799)#define BT\_FEAT\_LE\_PWR\_CTRL\_REQ(feat) BT\_LE\_FEAT\_TEST(feat, \

243 BT\_LE\_FEAT\_BIT\_PWR\_CTRL\_REQ)

[ 244](hci__types_8h.md#a342ce6074faa59b507cf179868e612ba)#define BT\_FEAT\_LE\_PWR\_CHG\_IND(feat) BT\_LE\_FEAT\_TEST(feat, \

245 BT\_LE\_FEAT\_BIT\_PWR\_CHG\_IND)

[ 246](hci__types_8h.md#a8d771bd34d22853f117dbbd41ef4afe5)#define BT\_FEAT\_LE\_PATH\_LOSS\_MONITOR(feat) BT\_LE\_FEAT\_TEST(feat, \

247 BT\_LE\_FEAT\_BIT\_PATH\_LOSS\_MONITOR)

[ 248](hci__types_8h.md#a6213deacc8582f14546b23331d41c3a3)#define BT\_FEAT\_LE\_PER\_ADV\_ADI\_SUPP(feat) BT\_LE\_FEAT\_TEST(feat, \

249 BT\_LE\_FEAT\_BIT\_PER\_ADV\_ADI\_SUPP)

[ 250](hci__types_8h.md#a75bf595ba1e16deeeedb45a55f470620)#define BT\_FEAT\_LE\_CONN\_SUBRATING(feat) BT\_LE\_FEAT\_TEST(feat, \

251 BT\_LE\_FEAT\_BIT\_CONN\_SUBRATING)

[ 252](hci__types_8h.md#a37adeecbf4c200cf8b060344718e7949)#define BT\_FEAT\_LE\_CONN\_SUBRATING\_HOST\_SUPP(feat) BT\_LE\_FEAT\_TEST(feat, \

253 BT\_LE\_FEAT\_BIT\_CONN\_SUBRATING\_HOST\_SUPP)

[ 254](hci__types_8h.md#abb7763cc16340d23bc7d687e60badcc0)#define BT\_FEAT\_LE\_CHANNEL\_CLASSIFICATION(feat) BT\_LE\_FEAT\_TEST(feat, \

255 BT\_LE\_FEAT\_BIT\_CHANNEL\_CLASSIFICATION)

[ 256](hci__types_8h.md#ac5d15de2be03bc837afdb33905ea40be)#define BT\_FEAT\_LE\_PAWR\_ADVERTISER(feat) BT\_LE\_FEAT\_TEST(feat, \

257 BT\_LE\_FEAT\_BIT\_PAWR\_ADVERTISER)

[ 258](hci__types_8h.md#a3ee6277e0e4db5e925912e8cb89269fa)#define BT\_FEAT\_LE\_PAWR\_SCANNER(feat) BT\_LE\_FEAT\_TEST(feat, \

259 BT\_LE\_FEAT\_BIT\_PAWR\_SCANNER)

260

[ 261](hci__types_8h.md#abe5a1ddbede473f583106e3500dccdb1)#define BT\_FEAT\_LE\_CIS(feat) (BT\_FEAT\_LE\_CIS\_CENTRAL(feat) | \

262 BT\_FEAT\_LE\_CIS\_PERIPHERAL(feat))

[ 263](hci__types_8h.md#a46b2f535c74178c8cc9359a7b1d2e140)#define BT\_FEAT\_LE\_BIS(feat) (BT\_FEAT\_LE\_ISO\_BROADCASTER(feat) | \

264 BT\_FEAT\_LE\_SYNC\_RECEIVER(feat))

[ 265](hci__types_8h.md#a7b1b490bf00af8b0bf8ecbf4ef4aaba3)#define BT\_FEAT\_LE\_ISO(feat) (BT\_FEAT\_LE\_CIS(feat) | \

266 BT\_FEAT\_LE\_BIS(feat))

267

268/\* LE States \*/

[ 269](hci__types_8h.md#abff5a0c6d1f3ab8ecf297d4ef29f7940)#define BT\_LE\_STATES\_PER\_CONN\_ADV(states) (states & 0x0000004000000000)

270

271/\* Bonding/authentication types \*/

[ 272](hci__types_8h.md#ac886a10eed1313f6114fcfc3810a34f0)#define BT\_HCI\_NO\_BONDING 0x00

[ 273](hci__types_8h.md#a89c6d0d285c1c99c51c96d282fe593b9)#define BT\_HCI\_NO\_BONDING\_MITM 0x01

[ 274](hci__types_8h.md#aae1149095ff44d1b749e8b4b4d4aa32f)#define BT\_HCI\_DEDICATED\_BONDING 0x02

[ 275](hci__types_8h.md#aa1361f09852be86296cf91896d8f0853)#define BT\_HCI\_DEDICATED\_BONDING\_MITM 0x03

[ 276](hci__types_8h.md#ad777455cbcdfe02dd297dee5510e63b4)#define BT\_HCI\_GENERAL\_BONDING 0x04

[ 277](hci__types_8h.md#a5b30ffdf3753d0a2a6c8ab025d32acef)#define BT\_HCI\_GENERAL\_BONDING\_MITM 0x05

278

279/\*

280 \* MITM protection is enabled in SSP authentication requirements octet when

281 \* LSB bit is set.

282 \*/

[ 283](hci__types_8h.md#a47ba0b282416c3e8f4275a38b7780b59)#define BT\_MITM 0x01

284

285/\* I/O capabilities \*/

[ 286](hci__types_8h.md#ac656a702e4193044a59cac517099e2cf)#define BT\_IO\_DISPLAY\_ONLY 0x00

[ 287](hci__types_8h.md#a701d4fa8a4ebc07647f70264ad36153e)#define BT\_IO\_DISPLAY\_YESNO 0x01

[ 288](hci__types_8h.md#a5a2a51ccedf3041c42ecdbd69e8c4a68)#define BT\_IO\_KEYBOARD\_ONLY 0x02

[ 289](hci__types_8h.md#ad68c0057160d5dacae12fce949fdaa32)#define BT\_IO\_NO\_INPUT\_OUTPUT 0x03

290

291/\* SCO packet types \*/

[ 292](hci__types_8h.md#aecb5b3886467c41baf979d01d8bde4a1)#define HCI\_PKT\_TYPE\_HV1 0x0020

[ 293](hci__types_8h.md#ae68633ce74639ec6f06d5ef4feee2d09)#define HCI\_PKT\_TYPE\_HV2 0x0040

[ 294](hci__types_8h.md#aecd04ca27f536a1cb15aacf9ee80aba8)#define HCI\_PKT\_TYPE\_HV3 0x0080

295

296/\* eSCO packet types \*/

[ 297](hci__types_8h.md#a4b048addd84409867177a97c785c4a73)#define HCI\_PKT\_TYPE\_SCO\_HV1 0x0001

[ 298](hci__types_8h.md#a98f8217b27c0b9b7817c86520da45018)#define HCI\_PKT\_TYPE\_SCO\_HV2 0x0002

[ 299](hci__types_8h.md#af67cdc23b6542e6d8323f14e17c7171d)#define HCI\_PKT\_TYPE\_SCO\_HV3 0x0004

[ 300](hci__types_8h.md#a9530e916a0cf905e2185cd021320bfff)#define HCI\_PKT\_TYPE\_ESCO\_EV3 0x0008

[ 301](hci__types_8h.md#a3e0b6a1aa3818cb0c36f7883fd361c7e)#define HCI\_PKT\_TYPE\_ESCO\_EV4 0x0010

[ 302](hci__types_8h.md#a1f7474cb16a495bd81dc1f23d4103f70)#define HCI\_PKT\_TYPE\_ESCO\_EV5 0x0020

[ 303](hci__types_8h.md#a1ccc4d6e5cfc560b7e2cb80c4c386607)#define HCI\_PKT\_TYPE\_ESCO\_2EV3 0x0040

[ 304](hci__types_8h.md#ac5f09e3db1bc4d697ff705802e9ec3a0)#define HCI\_PKT\_TYPE\_ESCO\_3EV3 0x0080

[ 305](hci__types_8h.md#a1252be2692bcfb7a1256c63c4deed15d)#define HCI\_PKT\_TYPE\_ESCO\_2EV5 0x0100

[ 306](hci__types_8h.md#aa45e51b1be89505fe599bc7983fcb950)#define HCI\_PKT\_TYPE\_ESCO\_3EV5 0x0200

307

308

[ 309](hci__types_8h.md#a8afe2c798b2d9657778f0815e3cb11c8)#define ESCO\_PKT\_MASK (HCI\_PKT\_TYPE\_SCO\_HV1 | \

310 HCI\_PKT\_TYPE\_SCO\_HV2 | \

311 HCI\_PKT\_TYPE\_SCO\_HV3 | \

312 HCI\_PKT\_TYPE\_ESCO\_EV3 | \

313 HCI\_PKT\_TYPE\_ESCO\_EV4 | \

314 HCI\_PKT\_TYPE\_ESCO\_EV5)

[ 315](hci__types_8h.md#a1ef7929257a087f340f1f421cd8f51ce)#define SCO\_PKT\_MASK (HCI\_PKT\_TYPE\_SCO\_HV1 | \

316 HCI\_PKT\_TYPE\_SCO\_HV2 | \

317 HCI\_PKT\_TYPE\_SCO\_HV3)

[ 318](hci__types_8h.md#aa3a50b43beddbd76ae67b71e79a80175)#define EDR\_ESCO\_PKT\_MASK (HCI\_PKT\_TYPE\_ESCO\_2EV3 | \

319 HCI\_PKT\_TYPE\_ESCO\_3EV3 | \

320 HCI\_PKT\_TYPE\_ESCO\_2EV5 | \

321 HCI\_PKT\_TYPE\_ESCO\_3EV5)

322

323/\* HCI BR/EDR link types \*/

[ 324](hci__types_8h.md#a5e79467b20a9173726c6be86b091e596)#define BT\_HCI\_SCO 0x00

[ 325](hci__types_8h.md#afee2289cd70b50f888518fd0b6b3f559)#define BT\_HCI\_ACL 0x01

[ 326](hci__types_8h.md#a4c57b051b336788e503a8521bb5ada80)#define BT\_HCI\_ESCO 0x02

327

328/\* OpCode Group Fields \*/

[ 329](hci__types_8h.md#abb6c50fe170ffaaaf4a0827058331381)#define BT\_OGF\_LINK\_CTRL 0x01

[ 330](hci__types_8h.md#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)#define BT\_OGF\_BASEBAND 0x03

[ 331](hci__types_8h.md#ac7c7348e291360169bf0ca5bb57b3d7e)#define BT\_OGF\_INFO 0x04

[ 332](hci__types_8h.md#a5ce14b9103bd538f3610afd80284157e)#define BT\_OGF\_STATUS 0x05

[ 333](hci__types_8h.md#abb09db6a211185842f039eddb9fadca5)#define BT\_OGF\_LE 0x08

[ 334](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65)#define BT\_OGF\_VS 0x3f

335

336/\* Construct OpCode from OGF and OCF \*/

[ 337](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)#define BT\_OP(ogf, ocf) ((ocf) | ((ogf) << 10))

338

339/\* Invalid opcode \*/

[ 340](hci__types_8h.md#a1bf4881fa3237f4a5b22e5fdb417762b)#define BT\_OP\_NOP 0x0000

341

342/\* Obtain OGF from OpCode \*/

[ 343](hci__types_8h.md#af3ae81176a4ace13a562262ad53aeae6)#define BT\_OGF(opcode) (((opcode) >> 10) & BIT\_MASK(6))

344/\* Obtain OCF from OpCode \*/

[ 345](hci__types_8h.md#ac267cc5384724efba92df0be57379a89)#define BT\_OCF(opcode) ((opcode) & BIT\_MASK(10))

346

[ 347](hci__types_8h.md#adce48ff5cdde5f4f8ab5bc960717581a)#define BT\_HCI\_OP\_INQUIRY BT\_OP(BT\_OGF\_LINK\_CTRL, 0x0001) /\* 0x0401 \*/

[ 348](structbt__hci__op__inquiry.md)struct [bt\_hci\_op\_inquiry](structbt__hci__op__inquiry.md) {

[ 349](structbt__hci__op__inquiry.md#abdd03feccecbdbbb5d2c7c7f3213b62f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [lap](structbt__hci__op__inquiry.md#abdd03feccecbdbbb5d2c7c7f3213b62f)[3];

[ 350](structbt__hci__op__inquiry.md#ae77fa706c9875b5568a4af26a7724d08) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [length](structbt__hci__op__inquiry.md#ae77fa706c9875b5568a4af26a7724d08);

[ 351](structbt__hci__op__inquiry.md#ac8ed23243dbd9a7c46fedd8abe9666f5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_rsp](structbt__hci__op__inquiry.md#ac8ed23243dbd9a7c46fedd8abe9666f5);

352} \_\_packed;

353

[ 354](hci__types_8h.md#ae2d4e5e9cbf056bff03a668e74523442)#define BT\_HCI\_OP\_INQUIRY\_CANCEL BT\_OP(BT\_OGF\_LINK\_CTRL, 0x0002) /\* 0x0402 \*/

355

[ 356](hci__types_8h.md#addfd3dec2a69e7e5e2634c4fe63769f2)#define BT\_HCI\_OP\_CONNECT BT\_OP(BT\_OGF\_LINK\_CTRL, 0x0005) /\* 0x0405 \*/

[ 357](structbt__hci__cp__connect.md)struct [bt\_hci\_cp\_connect](structbt__hci__cp__connect.md) {

[ 358](structbt__hci__cp__connect.md#a6f0753aad19d4c9591fa74152d151aa9) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__connect.md#a6f0753aad19d4c9591fa74152d151aa9);

[ 359](structbt__hci__cp__connect.md#a652a4e01641893a8588110dc505ceea0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [packet\_type](structbt__hci__cp__connect.md#a652a4e01641893a8588110dc505ceea0);

[ 360](structbt__hci__cp__connect.md#a35b0e1f73f696aae2ca519e16d7bb668) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pscan\_rep\_mode](structbt__hci__cp__connect.md#a35b0e1f73f696aae2ca519e16d7bb668);

[ 361](structbt__hci__cp__connect.md#aef01fcac1b9792353bd8095e6911d6c3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reserved](structbt__hci__cp__connect.md#aef01fcac1b9792353bd8095e6911d6c3);

[ 362](structbt__hci__cp__connect.md#ac379ec381ad4cf6760750203924e5dda) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [clock\_offset](structbt__hci__cp__connect.md#ac379ec381ad4cf6760750203924e5dda);

[ 363](structbt__hci__cp__connect.md#a7a3d772bfd4c83236f9f1ad657e33f17) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [allow\_role\_switch](structbt__hci__cp__connect.md#a7a3d772bfd4c83236f9f1ad657e33f17);

364} \_\_packed;

365

[ 366](hci__types_8h.md#ab3d8612855550e52a0887e231371fbc2)#define BT\_HCI\_OP\_DISCONNECT BT\_OP(BT\_OGF\_LINK\_CTRL, 0x0006) /\* 0x0406 \*/

[ 367](structbt__hci__cp__disconnect.md)struct [bt\_hci\_cp\_disconnect](structbt__hci__cp__disconnect.md) {

[ 368](structbt__hci__cp__disconnect.md#a9cb5bcd135082c37a19cce57ffa123ff) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__disconnect.md#a9cb5bcd135082c37a19cce57ffa123ff);

[ 369](structbt__hci__cp__disconnect.md#a8e10edb1e700c1ef38f39bf20b9b374f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reason](structbt__hci__cp__disconnect.md#a8e10edb1e700c1ef38f39bf20b9b374f);

370} \_\_packed;

371

[ 372](hci__types_8h.md#ac50eb14115129bcc8c47016a6479149d)#define BT\_HCI\_OP\_CONNECT\_CANCEL BT\_OP(BT\_OGF\_LINK\_CTRL, 0x0008) /\* 0x0408 \*/

[ 373](structbt__hci__cp__connect__cancel.md)struct [bt\_hci\_cp\_connect\_cancel](structbt__hci__cp__connect__cancel.md) {

[ 374](structbt__hci__cp__connect__cancel.md#a2adaf1b708689525e44e9a9572f5f357) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__connect__cancel.md#a2adaf1b708689525e44e9a9572f5f357);

375} \_\_packed;

[ 376](structbt__hci__rp__connect__cancel.md)struct [bt\_hci\_rp\_connect\_cancel](structbt__hci__rp__connect__cancel.md) {

[ 377](structbt__hci__rp__connect__cancel.md#a05d0c9e4163bc62a57dba8618294eb65) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__connect__cancel.md#a05d0c9e4163bc62a57dba8618294eb65);

[ 378](structbt__hci__rp__connect__cancel.md#a0ccfcbd294aa067879ab8d7a41bc41c9) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__rp__connect__cancel.md#a0ccfcbd294aa067879ab8d7a41bc41c9);

379} \_\_packed;

380

[ 381](hci__types_8h.md#af45bed44788b16be1b172c56c33eea34)#define BT\_HCI\_OP\_ACCEPT\_CONN\_REQ BT\_OP(BT\_OGF\_LINK\_CTRL, 0x0009) /\* 0x0409 \*/

[ 382](structbt__hci__cp__accept__conn__req.md)struct [bt\_hci\_cp\_accept\_conn\_req](structbt__hci__cp__accept__conn__req.md) {

[ 383](structbt__hci__cp__accept__conn__req.md#aa2954d98fdd42882cf7095e4ce7a3dc5) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__accept__conn__req.md#aa2954d98fdd42882cf7095e4ce7a3dc5);

[ 384](structbt__hci__cp__accept__conn__req.md#a95e445018d1b9da5a914f0845bb9dbad) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [role](structbt__hci__cp__accept__conn__req.md#a95e445018d1b9da5a914f0845bb9dbad);

385} \_\_packed;

386

[ 387](hci__types_8h.md#ac4e12b8f7b89a658da7bbbaf371358e0)#define BT\_HCI\_OP\_SETUP\_SYNC\_CONN BT\_OP(BT\_OGF\_LINK\_CTRL, 0x0028) /\* 0x0428 \*/

[ 388](structbt__hci__cp__setup__sync__conn.md)struct [bt\_hci\_cp\_setup\_sync\_conn](structbt__hci__cp__setup__sync__conn.md) {

[ 389](structbt__hci__cp__setup__sync__conn.md#ad065185846694fc0070bb366e642f1c7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__setup__sync__conn.md#ad065185846694fc0070bb366e642f1c7);

[ 390](structbt__hci__cp__setup__sync__conn.md#aa35718e13a7d778c779be535c2b1945e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tx\_bandwidth](structbt__hci__cp__setup__sync__conn.md#aa35718e13a7d778c779be535c2b1945e);

[ 391](structbt__hci__cp__setup__sync__conn.md#a137601ab44970782e2f3d4fcd2c8fcc2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rx\_bandwidth](structbt__hci__cp__setup__sync__conn.md#a137601ab44970782e2f3d4fcd2c8fcc2);

[ 392](structbt__hci__cp__setup__sync__conn.md#a5ffb5e552d4913974a10a16083f82864) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_latency](structbt__hci__cp__setup__sync__conn.md#a5ffb5e552d4913974a10a16083f82864);

[ 393](structbt__hci__cp__setup__sync__conn.md#a4d7df5b1aa714bc14d0b6c3cbccc5014) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [content\_format](structbt__hci__cp__setup__sync__conn.md#a4d7df5b1aa714bc14d0b6c3cbccc5014);

[ 394](structbt__hci__cp__setup__sync__conn.md#a61ebbc775d3ca0724ea173d72a96e0c0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [retrans\_effort](structbt__hci__cp__setup__sync__conn.md#a61ebbc775d3ca0724ea173d72a96e0c0);

[ 395](structbt__hci__cp__setup__sync__conn.md#a6d4c16a4d77d3ee4f8f65ab18a0f192d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pkt\_type](structbt__hci__cp__setup__sync__conn.md#a6d4c16a4d77d3ee4f8f65ab18a0f192d);

396} \_\_packed;

397

[ 398](hci__types_8h.md#a97976c13fe03d346313bc19489d45360)#define BT\_HCI\_OP\_ACCEPT\_SYNC\_CONN\_REQ BT\_OP(BT\_OGF\_LINK\_CTRL, 0x0029) /\* 0x0429 \*/

[ 399](structbt__hci__cp__accept__sync__conn__req.md)struct [bt\_hci\_cp\_accept\_sync\_conn\_req](structbt__hci__cp__accept__sync__conn__req.md) {

[ 400](structbt__hci__cp__accept__sync__conn__req.md#a6a5a56d3a9d1a6d1064e7bd4c9fd333e) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__accept__sync__conn__req.md#a6a5a56d3a9d1a6d1064e7bd4c9fd333e);

[ 401](structbt__hci__cp__accept__sync__conn__req.md#a53fe4c6d61dbb99f99aa445b2c47a8ef) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tx\_bandwidth](structbt__hci__cp__accept__sync__conn__req.md#a53fe4c6d61dbb99f99aa445b2c47a8ef);

[ 402](structbt__hci__cp__accept__sync__conn__req.md#aceda6dbd3e221ad080850e9635886a86) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rx\_bandwidth](structbt__hci__cp__accept__sync__conn__req.md#aceda6dbd3e221ad080850e9635886a86);

[ 403](structbt__hci__cp__accept__sync__conn__req.md#a4ba6dffd840ef868524b490d227fd085) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_latency](structbt__hci__cp__accept__sync__conn__req.md#a4ba6dffd840ef868524b490d227fd085);

[ 404](structbt__hci__cp__accept__sync__conn__req.md#adba31b588bf12e852cc43b85c006aaa3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [content\_format](structbt__hci__cp__accept__sync__conn__req.md#adba31b588bf12e852cc43b85c006aaa3);

[ 405](structbt__hci__cp__accept__sync__conn__req.md#ab5ece67c5a1e62fc4124556eef743c26) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [retrans\_effort](structbt__hci__cp__accept__sync__conn__req.md#ab5ece67c5a1e62fc4124556eef743c26);

[ 406](structbt__hci__cp__accept__sync__conn__req.md#ab5d9c27ebdf45fb54b0c6330b5b095be) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pkt\_type](structbt__hci__cp__accept__sync__conn__req.md#ab5d9c27ebdf45fb54b0c6330b5b095be);

407} \_\_packed;

408

[ 409](hci__types_8h.md#aabb1f800ad4574e0350007af94cd786d)#define BT\_HCI\_OP\_REJECT\_CONN\_REQ BT\_OP(BT\_OGF\_LINK\_CTRL, 0x000a) /\* 0x040a \*/

[ 410](structbt__hci__cp__reject__conn__req.md)struct [bt\_hci\_cp\_reject\_conn\_req](structbt__hci__cp__reject__conn__req.md) {

[ 411](structbt__hci__cp__reject__conn__req.md#a9a1cb4173367c6f018fbd30a47c590b4) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__reject__conn__req.md#a9a1cb4173367c6f018fbd30a47c590b4);

[ 412](structbt__hci__cp__reject__conn__req.md#a1c2e234d6d00296bc01962b95e849df0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reason](structbt__hci__cp__reject__conn__req.md#a1c2e234d6d00296bc01962b95e849df0);

413} \_\_packed;

414

[ 415](hci__types_8h.md#a7da489e05d679c00f6cbbca0dfaaf136)#define BT\_HCI\_OP\_LINK\_KEY\_REPLY BT\_OP(BT\_OGF\_LINK\_CTRL, 0x000b) /\* 0x040b \*/

[ 416](structbt__hci__cp__link__key__reply.md)struct [bt\_hci\_cp\_link\_key\_reply](structbt__hci__cp__link__key__reply.md) {

[ 417](structbt__hci__cp__link__key__reply.md#ab5221952fbcfe413d7c3bd3a441a9b17) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__link__key__reply.md#ab5221952fbcfe413d7c3bd3a441a9b17);

[ 418](structbt__hci__cp__link__key__reply.md#a2af0b4b55a5ffcff0221da841ba0cbba) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [link\_key](structbt__hci__cp__link__key__reply.md#a2af0b4b55a5ffcff0221da841ba0cbba)[16];

419} \_\_packed;

420

[ 421](hci__types_8h.md#a7db25bd8bdbd4351e0dcef1df8dc7077)#define BT\_HCI\_OP\_LINK\_KEY\_NEG\_REPLY BT\_OP(BT\_OGF\_LINK\_CTRL, 0x000c) /\* 0x040c \*/

[ 422](structbt__hci__cp__link__key__neg__reply.md)struct [bt\_hci\_cp\_link\_key\_neg\_reply](structbt__hci__cp__link__key__neg__reply.md) {

[ 423](structbt__hci__cp__link__key__neg__reply.md#aca3114707eb7c631af582626551619cd) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__link__key__neg__reply.md#aca3114707eb7c631af582626551619cd);

424} \_\_packed;

425

[ 426](hci__types_8h.md#a7713e5641070ac7fca91e027fc9b8c40)#define BT\_HCI\_OP\_PIN\_CODE\_REPLY BT\_OP(BT\_OGF\_LINK\_CTRL, 0x000d) /\* 0x040d \*/

[ 427](structbt__hci__cp__pin__code__reply.md)struct [bt\_hci\_cp\_pin\_code\_reply](structbt__hci__cp__pin__code__reply.md) {

[ 428](structbt__hci__cp__pin__code__reply.md#a627800dcb580110be785576dfcc49bb1) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__pin__code__reply.md#a627800dcb580110be785576dfcc49bb1);

[ 429](structbt__hci__cp__pin__code__reply.md#aa0cbf668608c3eb4998356ad7b18c01a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pin\_len](structbt__hci__cp__pin__code__reply.md#aa0cbf668608c3eb4998356ad7b18c01a);

[ 430](structbt__hci__cp__pin__code__reply.md#afc4ed5ae429087f4692af716d6b56997) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pin\_code](structbt__hci__cp__pin__code__reply.md#afc4ed5ae429087f4692af716d6b56997)[16];

431} \_\_packed;

[ 432](structbt__hci__rp__pin__code__reply.md)struct [bt\_hci\_rp\_pin\_code\_reply](structbt__hci__rp__pin__code__reply.md) {

[ 433](structbt__hci__rp__pin__code__reply.md#a3f167661b8d3f63ab12e6f64fb33986b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__pin__code__reply.md#a3f167661b8d3f63ab12e6f64fb33986b);

[ 434](structbt__hci__rp__pin__code__reply.md#afc7c991fd8050e8aae56b8587b5ee01d) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__rp__pin__code__reply.md#afc7c991fd8050e8aae56b8587b5ee01d);

435} \_\_packed;

436

[ 437](hci__types_8h.md#a5833de4cefd59cee9c614163de7e927b)#define BT\_HCI\_OP\_PIN\_CODE\_NEG\_REPLY BT\_OP(BT\_OGF\_LINK\_CTRL, 0x000e) /\* 0x040e \*/

[ 438](structbt__hci__cp__pin__code__neg__reply.md)struct [bt\_hci\_cp\_pin\_code\_neg\_reply](structbt__hci__cp__pin__code__neg__reply.md) {

[ 439](structbt__hci__cp__pin__code__neg__reply.md#a8aec3ba6c530850dce0a2d7b7f7f86ee) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__pin__code__neg__reply.md#a8aec3ba6c530850dce0a2d7b7f7f86ee);

440} \_\_packed;

[ 441](structbt__hci__rp__pin__code__neg__reply.md)struct [bt\_hci\_rp\_pin\_code\_neg\_reply](structbt__hci__rp__pin__code__neg__reply.md) {

[ 442](structbt__hci__rp__pin__code__neg__reply.md#a10bcc55407e22417256c464684a41e58) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__pin__code__neg__reply.md#a10bcc55407e22417256c464684a41e58);

[ 443](structbt__hci__rp__pin__code__neg__reply.md#a168caf2a517aa573bd6acaf48e414e9b) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__rp__pin__code__neg__reply.md#a168caf2a517aa573bd6acaf48e414e9b);

444} \_\_packed;

445

[ 446](hci__types_8h.md#a4c24e505f9c799275fc2f35619b7df97)#define BT\_HCI\_OP\_AUTH\_REQUESTED BT\_OP(BT\_OGF\_LINK\_CTRL, 0x0011) /\* 0x0411 \*/

[ 447](structbt__hci__cp__auth__requested.md)struct [bt\_hci\_cp\_auth\_requested](structbt__hci__cp__auth__requested.md) {

[ 448](structbt__hci__cp__auth__requested.md#a079490f8f8569e281ce16f13847cbf33) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__auth__requested.md#a079490f8f8569e281ce16f13847cbf33);

449} \_\_packed;

450

[ 451](hci__types_8h.md#ac32c04cf6bc9de299f0a307dbeed63f3)#define BT\_HCI\_OP\_SET\_CONN\_ENCRYPT BT\_OP(BT\_OGF\_LINK\_CTRL, 0x0013) /\* 0x0413 \*/

[ 452](structbt__hci__cp__set__conn__encrypt.md)struct [bt\_hci\_cp\_set\_conn\_encrypt](structbt__hci__cp__set__conn__encrypt.md) {

[ 453](structbt__hci__cp__set__conn__encrypt.md#a39e0c40ed6e6e9387ae384fd122fca4b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__set__conn__encrypt.md#a39e0c40ed6e6e9387ae384fd122fca4b);

[ 454](structbt__hci__cp__set__conn__encrypt.md#aa259563efd49d04a8886f74169fd30b1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [encrypt](structbt__hci__cp__set__conn__encrypt.md#aa259563efd49d04a8886f74169fd30b1);

455} \_\_packed;

456

[ 457](hci__types_8h.md#a2e759212d10ecd3a2e975379bf18d374)#define BT\_HCI\_OP\_REMOTE\_NAME\_REQUEST BT\_OP(BT\_OGF\_LINK\_CTRL, 0x0019) /\* 0x0419 \*/

[ 458](structbt__hci__cp__remote__name__request.md)struct [bt\_hci\_cp\_remote\_name\_request](structbt__hci__cp__remote__name__request.md) {

[ 459](structbt__hci__cp__remote__name__request.md#a5093f7bb70fa36f4948039d02d594e27) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__remote__name__request.md#a5093f7bb70fa36f4948039d02d594e27);

[ 460](structbt__hci__cp__remote__name__request.md#aed0aea58ca6f5dc15220083d377cbf5c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pscan\_rep\_mode](structbt__hci__cp__remote__name__request.md#aed0aea58ca6f5dc15220083d377cbf5c);

[ 461](structbt__hci__cp__remote__name__request.md#ab1883aa2b08d89f9c3190f338808a43c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reserved](structbt__hci__cp__remote__name__request.md#ab1883aa2b08d89f9c3190f338808a43c);

[ 462](structbt__hci__cp__remote__name__request.md#a5d7ea30052f8e4e2b3564659ca187c48) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [clock\_offset](structbt__hci__cp__remote__name__request.md#a5d7ea30052f8e4e2b3564659ca187c48);

463} \_\_packed;

464

[ 465](hci__types_8h.md#a76f79f4e14396297cc5db4ca8dba0c4c)#define BT\_HCI\_OP\_REMOTE\_NAME\_CANCEL BT\_OP(BT\_OGF\_LINK\_CTRL, 0x001a) /\* 0x041a \*/

[ 466](structbt__hci__cp__remote__name__cancel.md)struct [bt\_hci\_cp\_remote\_name\_cancel](structbt__hci__cp__remote__name__cancel.md) {

[ 467](structbt__hci__cp__remote__name__cancel.md#a0b7b4362804077ce828aeeb2b8af86b9) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__remote__name__cancel.md#a0b7b4362804077ce828aeeb2b8af86b9);

468} \_\_packed;

[ 469](structbt__hci__rp__remote__name__cancel.md)struct [bt\_hci\_rp\_remote\_name\_cancel](structbt__hci__rp__remote__name__cancel.md) {

[ 470](structbt__hci__rp__remote__name__cancel.md#ac7fadee392b126cb50cef7a6336926cb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__remote__name__cancel.md#ac7fadee392b126cb50cef7a6336926cb);

[ 471](structbt__hci__rp__remote__name__cancel.md#a455432799a1272f88b2b00a35a2e7ef5) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__rp__remote__name__cancel.md#a455432799a1272f88b2b00a35a2e7ef5);

472} \_\_packed;

473

[ 474](hci__types_8h.md#ab6282249d4c14412674083007346b005)#define BT\_HCI\_OP\_READ\_REMOTE\_FEATURES BT\_OP(BT\_OGF\_LINK\_CTRL, 0x001b) /\* 0x041b \*/

[ 475](structbt__hci__cp__read__remote__features.md)struct [bt\_hci\_cp\_read\_remote\_features](structbt__hci__cp__read__remote__features.md) {

[ 476](structbt__hci__cp__read__remote__features.md#ae14362a04c00b37342f3cc413f3933d3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__read__remote__features.md#ae14362a04c00b37342f3cc413f3933d3);

477} \_\_packed;

478

[ 479](hci__types_8h.md#a87f6747b2b5d52a7886a1ec72100d9d0)#define BT\_HCI\_OP\_READ\_REMOTE\_EXT\_FEATURES BT\_OP(BT\_OGF\_LINK\_CTRL, 0x001c) /\* 0x041c \*/

[ 480](structbt__hci__cp__read__remote__ext__features.md)struct [bt\_hci\_cp\_read\_remote\_ext\_features](structbt__hci__cp__read__remote__ext__features.md) {

[ 481](structbt__hci__cp__read__remote__ext__features.md#aaa236c11d148252e34fd20d794d991f3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__read__remote__ext__features.md#aaa236c11d148252e34fd20d794d991f3);

[ 482](structbt__hci__cp__read__remote__ext__features.md#a6aff189605b276998e58b051429a5cd2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [page](structbt__hci__cp__read__remote__ext__features.md#a6aff189605b276998e58b051429a5cd2);

483} \_\_packed;

484

[ 485](hci__types_8h.md#ae723b797305fe7a370b94d8c865e5708)#define BT\_HCI\_OP\_READ\_REMOTE\_VERSION\_INFO BT\_OP(BT\_OGF\_LINK\_CTRL, 0x001d) /\* 0x041d \*/

[ 486](structbt__hci__cp__read__remote__version__info.md)struct [bt\_hci\_cp\_read\_remote\_version\_info](structbt__hci__cp__read__remote__version__info.md) {

[ 487](structbt__hci__cp__read__remote__version__info.md#a504b83f16a82b1e179d74547c7a29bf3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__read__remote__version__info.md#a504b83f16a82b1e179d74547c7a29bf3);

488} \_\_packed;

489

[ 490](hci__types_8h.md#a343a3c5c594dd25483fedf38c304a09a)#define BT\_HCI\_OP\_IO\_CAPABILITY\_REPLY BT\_OP(BT\_OGF\_LINK\_CTRL, 0x002b) /\* 0x042b \*/

[ 491](structbt__hci__cp__io__capability__reply.md)struct [bt\_hci\_cp\_io\_capability\_reply](structbt__hci__cp__io__capability__reply.md) {

[ 492](structbt__hci__cp__io__capability__reply.md#afbe2bc0c1dcc0791a98068b052aea1f2) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__io__capability__reply.md#afbe2bc0c1dcc0791a98068b052aea1f2);

[ 493](structbt__hci__cp__io__capability__reply.md#a0995c81ba1f653c59bda9a444fb17915) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [capability](structbt__hci__cp__io__capability__reply.md#a0995c81ba1f653c59bda9a444fb17915);

[ 494](structbt__hci__cp__io__capability__reply.md#ac002ea0b276200a15d603b5ac83666e5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [oob\_data](structbt__hci__cp__io__capability__reply.md#ac002ea0b276200a15d603b5ac83666e5);

[ 495](structbt__hci__cp__io__capability__reply.md#a8983418dca3a7725f3b113a4d0ee177e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [authentication](structbt__hci__cp__io__capability__reply.md#a8983418dca3a7725f3b113a4d0ee177e);

496} \_\_packed;

497

[ 498](hci__types_8h.md#ab688441778a4239e1e8f2b2e0b74004f)#define BT\_HCI\_OP\_USER\_CONFIRM\_REPLY BT\_OP(BT\_OGF\_LINK\_CTRL, 0x002c) /\* 0x042c \*/

[ 499](hci__types_8h.md#aecc09326c190d2ab7b89f99375cd39bd)#define BT\_HCI\_OP\_USER\_CONFIRM\_NEG\_REPLY BT\_OP(BT\_OGF\_LINK\_CTRL, 0x002d) /\* 0x042d \*/

[ 500](structbt__hci__cp__user__confirm__reply.md)struct [bt\_hci\_cp\_user\_confirm\_reply](structbt__hci__cp__user__confirm__reply.md) {

[ 501](structbt__hci__cp__user__confirm__reply.md#abe0e8da3e590c565364ed30ba107a0e6) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__user__confirm__reply.md#abe0e8da3e590c565364ed30ba107a0e6);

502} \_\_packed;

[ 503](structbt__hci__rp__user__confirm__reply.md)struct [bt\_hci\_rp\_user\_confirm\_reply](structbt__hci__rp__user__confirm__reply.md) {

[ 504](structbt__hci__rp__user__confirm__reply.md#ab07114550c2da3c1e9925cb883bf3a89) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__user__confirm__reply.md#ab07114550c2da3c1e9925cb883bf3a89);

[ 505](structbt__hci__rp__user__confirm__reply.md#a91678db3ae2a696ba7b9dd5bc080c488) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__rp__user__confirm__reply.md#a91678db3ae2a696ba7b9dd5bc080c488);

506} \_\_packed;

507

[ 508](hci__types_8h.md#ad1fce315b731f9978cd52a8c23994a10)#define BT\_HCI\_OP\_USER\_PASSKEY\_REPLY BT\_OP(BT\_OGF\_LINK\_CTRL, 0x002e) /\* 0x042e \*/

[ 509](structbt__hci__cp__user__passkey__reply.md)struct [bt\_hci\_cp\_user\_passkey\_reply](structbt__hci__cp__user__passkey__reply.md) {

[ 510](structbt__hci__cp__user__passkey__reply.md#a56dbb4a858ecbf36eee61e24ed3742cf) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__user__passkey__reply.md#a56dbb4a858ecbf36eee61e24ed3742cf);

[ 511](structbt__hci__cp__user__passkey__reply.md#a80483025a32f37e7f75b3a220d48148c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [passkey](structbt__hci__cp__user__passkey__reply.md#a80483025a32f37e7f75b3a220d48148c);

512} \_\_packed;

513

[ 514](hci__types_8h.md#a96f9c5c3439d829dfac94cca9ad1f015)#define BT\_HCI\_OP\_USER\_PASSKEY\_NEG\_REPLY BT\_OP(BT\_OGF\_LINK\_CTRL, 0x002f) /\* 0x042f \*/

[ 515](structbt__hci__cp__user__passkey__neg__reply.md)struct [bt\_hci\_cp\_user\_passkey\_neg\_reply](structbt__hci__cp__user__passkey__neg__reply.md) {

[ 516](structbt__hci__cp__user__passkey__neg__reply.md#ade9d7068054b15089b8c238ecc3e4397) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__user__passkey__neg__reply.md#ade9d7068054b15089b8c238ecc3e4397);

517} \_\_packed;

518

[ 519](hci__types_8h.md#a75d9a0acb6522dd0ae290572c4255540)#define BT\_HCI\_OP\_IO\_CAPABILITY\_NEG\_REPLY BT\_OP(BT\_OGF\_LINK\_CTRL, 0x0034) /\* 0x0434 \*/

[ 520](structbt__hci__cp__io__capability__neg__reply.md)struct [bt\_hci\_cp\_io\_capability\_neg\_reply](structbt__hci__cp__io__capability__neg__reply.md) {

[ 521](structbt__hci__cp__io__capability__neg__reply.md#a8dba05bc84de2573eaea43ea9e428015) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__io__capability__neg__reply.md#a8dba05bc84de2573eaea43ea9e428015);

[ 522](structbt__hci__cp__io__capability__neg__reply.md#a82c54e5ad7fd4a6d81952832ae4de373) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reason](structbt__hci__cp__io__capability__neg__reply.md#a82c54e5ad7fd4a6d81952832ae4de373);

523} \_\_packed;

524

[ 525](hci__types_8h.md#abb9bf6d936310a43c4a88244ad12640d)#define BT\_HCI\_OP\_SET\_EVENT\_MASK BT\_OP(BT\_OGF\_BASEBAND, 0x0001) /\* 0x0c01 \*/

[ 526](structbt__hci__cp__set__event__mask.md)struct [bt\_hci\_cp\_set\_event\_mask](structbt__hci__cp__set__event__mask.md) {

[ 527](structbt__hci__cp__set__event__mask.md#ab3af227511f47ee03f2d6aba8ae65c5d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [events](structbt__hci__cp__set__event__mask.md#ab3af227511f47ee03f2d6aba8ae65c5d)[8];

528} \_\_packed;

529

[ 530](hci__types_8h.md#abb515eb4ea9e66503bf1f375af01a6c0)#define BT\_HCI\_OP\_RESET BT\_OP(BT\_OGF\_BASEBAND, 0x0003) /\* 0x0c03 \*/

531

[ 532](hci__types_8h.md#a9b328487dbeeaa587e6f75011441f340)#define BT\_HCI\_OP\_WRITE\_LOCAL\_NAME BT\_OP(BT\_OGF\_BASEBAND, 0x0013) /\* 0x0c13 \*/

[ 533](structbt__hci__write__local__name.md)struct [bt\_hci\_write\_local\_name](structbt__hci__write__local__name.md) {

[ 534](structbt__hci__write__local__name.md#a8d2cd9a16525c3fc10ae0e3f196110da) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [local\_name](structbt__hci__write__local__name.md#a8d2cd9a16525c3fc10ae0e3f196110da)[248];

535} \_\_packed;

536

[ 537](hci__types_8h.md#af302a5e40644307f522154f3803572d0)#define BT\_HCI\_OP\_READ\_CONN\_ACCEPT\_TIMEOUT BT\_OP(BT\_OGF\_BASEBAND, 0x0015) /\* 0x0c15 \*/

[ 538](structbt__hci__rp__read__conn__accept__timeout.md)struct [bt\_hci\_rp\_read\_conn\_accept\_timeout](structbt__hci__rp__read__conn__accept__timeout.md) {

[ 539](structbt__hci__rp__read__conn__accept__timeout.md#afeb5888722ee368e02c6b27b75ab2a70) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__conn__accept__timeout.md#afeb5888722ee368e02c6b27b75ab2a70);

[ 540](structbt__hci__rp__read__conn__accept__timeout.md#a01ca30c92311ec1df19a4cf835ea74cf) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_accept\_timeout](structbt__hci__rp__read__conn__accept__timeout.md#a01ca30c92311ec1df19a4cf835ea74cf);

541} \_\_packed;

542

[ 543](hci__types_8h.md#a6799bd267ef7c19b05ed2dd57baf0393)#define BT\_HCI\_OP\_WRITE\_CONN\_ACCEPT\_TIMEOUT BT\_OP(BT\_OGF\_BASEBAND, 0x0016) /\* 0x0c16 \*/

[ 544](structbt__hci__cp__write__conn__accept__timeout.md)struct [bt\_hci\_cp\_write\_conn\_accept\_timeout](structbt__hci__cp__write__conn__accept__timeout.md) {

[ 545](structbt__hci__cp__write__conn__accept__timeout.md#a13de5f88920c6a41dafa598734b7acf9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_accept\_timeout](structbt__hci__cp__write__conn__accept__timeout.md#a13de5f88920c6a41dafa598734b7acf9);

546} \_\_packed;

547

[ 548](structbt__hci__rp__write__conn__accept__timeout.md)struct [bt\_hci\_rp\_write\_conn\_accept\_timeout](structbt__hci__rp__write__conn__accept__timeout.md) {

[ 549](structbt__hci__rp__write__conn__accept__timeout.md#a1f9eee1a5843747e0d224b86b602a3da) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__write__conn__accept__timeout.md#a1f9eee1a5843747e0d224b86b602a3da);

550} \_\_packed;

551

[ 552](hci__types_8h.md#a5ef44fe1cca74a2258ffab1edd04acdf)#define BT\_HCI\_OP\_WRITE\_PAGE\_TIMEOUT BT\_OP(BT\_OGF\_BASEBAND, 0x0018) /\* 0x0c18 \*/

553

[ 554](hci__types_8h.md#a0c8b9dc68ec6cd91ec0e9e565701a887)#define BT\_HCI\_OP\_WRITE\_SCAN\_ENABLE BT\_OP(BT\_OGF\_BASEBAND, 0x001a) /\* 0x0c1a \*/

[ 555](hci__types_8h.md#a19b4c20d243de28462b686088e2971a3)#define BT\_BREDR\_SCAN\_DISABLED 0x00

[ 556](hci__types_8h.md#a2f75eaee67bbb6c0211f3146d881278f)#define BT\_BREDR\_SCAN\_INQUIRY 0x01

[ 557](hci__types_8h.md#a006d877a26f4e8dd0689b1324107a843)#define BT\_BREDR\_SCAN\_PAGE 0x02

558

[ 559](hci__types_8h.md#ace988e19fa62bf61654a329acaf99018)#define BT\_HCI\_OP\_WRITE\_CLASS\_OF\_DEVICE BT\_OP(BT\_OGF\_BASEBAND, 0x0024) /\* 0x0c24 \*/

[ 560](structbt__hci__cp__write__class__of__device.md)struct [bt\_hci\_cp\_write\_class\_of\_device](structbt__hci__cp__write__class__of__device.md) {

[ 561](structbt__hci__cp__write__class__of__device.md#acc3b940de1a5da095e8a4f18e69229f2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [class\_of\_device](structbt__hci__cp__write__class__of__device.md#acc3b940de1a5da095e8a4f18e69229f2)[3];

562} \_\_packed;

563

[ 564](hci__types_8h.md#ac1ebc6168b2823aea2af2e2f89ffb6cd)#define BT\_TX\_POWER\_LEVEL\_CURRENT 0x00

[ 565](hci__types_8h.md#ad835bc44abee2e174f86cd55ac0338e3)#define BT\_TX\_POWER\_LEVEL\_MAX 0x01

[ 566](hci__types_8h.md#aaac00b7d9f9f96d1438643ee054ab21a)#define BT\_HCI\_OP\_READ\_TX\_POWER\_LEVEL BT\_OP(BT\_OGF\_BASEBAND, 0x002d) /\* 0x0c2d \*/

[ 567](structbt__hci__cp__read__tx__power__level.md)struct [bt\_hci\_cp\_read\_tx\_power\_level](structbt__hci__cp__read__tx__power__level.md) {

[ 568](structbt__hci__cp__read__tx__power__level.md#a1c268364fc80b9478d70b7eb997d9825) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__read__tx__power__level.md#a1c268364fc80b9478d70b7eb997d9825);

[ 569](structbt__hci__cp__read__tx__power__level.md#a1920e671ec2deda1daf47f06a86d2881) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__hci__cp__read__tx__power__level.md#a1920e671ec2deda1daf47f06a86d2881);

570} \_\_packed;

571

[ 572](structbt__hci__rp__read__tx__power__level.md)struct [bt\_hci\_rp\_read\_tx\_power\_level](structbt__hci__rp__read__tx__power__level.md) {

[ 573](structbt__hci__rp__read__tx__power__level.md#af40a8e2e663872e8d9fdde839cc6d1b4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__tx__power__level.md#af40a8e2e663872e8d9fdde839cc6d1b4);

[ 574](structbt__hci__rp__read__tx__power__level.md#ac2bd21e90145102bc483c2b0b3cdd416) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__read__tx__power__level.md#ac2bd21e90145102bc483c2b0b3cdd416);

[ 575](structbt__hci__rp__read__tx__power__level.md#a46526b820038bb445a7824a7b4bfc870) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power\_level](structbt__hci__rp__read__tx__power__level.md#a46526b820038bb445a7824a7b4bfc870);

576} \_\_packed;

577

[ 578](hci__types_8h.md#a740a01412d6fad277362634e1854f54b)#define BT\_HCI\_LE\_TX\_POWER\_PHY\_1M 0x01

[ 579](hci__types_8h.md#aa3eadebe7675de492b01ec117f72d808)#define BT\_HCI\_LE\_TX\_POWER\_PHY\_2M 0x02

[ 580](hci__types_8h.md#a66f2c7c03e65392c3477faddc14d9787)#define BT\_HCI\_LE\_TX\_POWER\_PHY\_CODED\_S8 0x03

[ 581](hci__types_8h.md#ab2bed6683929c37a3d087dba88309e45)#define BT\_HCI\_LE\_TX\_POWER\_PHY\_CODED\_S2 0x04

[ 582](hci__types_8h.md#aebd5487b500c54a47a926bb1daa56f5e)#define BT\_HCI\_OP\_LE\_ENH\_READ\_TX\_POWER\_LEVEL BT\_OP(BT\_OGF\_LE, 0x0076) /\* 0x2076 \*/

[ 583](structbt__hci__cp__le__read__tx__power__level.md)struct [bt\_hci\_cp\_le\_read\_tx\_power\_level](structbt__hci__cp__le__read__tx__power__level.md) {

[ 584](structbt__hci__cp__le__read__tx__power__level.md#af8c2d89b183d7bdc0f55a0bf783a373d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__read__tx__power__level.md#af8c2d89b183d7bdc0f55a0bf783a373d);

[ 585](structbt__hci__cp__le__read__tx__power__level.md#a4863396dfe4dca65aaef68293e29291b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__cp__le__read__tx__power__level.md#a4863396dfe4dca65aaef68293e29291b);

586} \_\_packed;

587

[ 588](structbt__hci__rp__le__read__tx__power__level.md)struct [bt\_hci\_rp\_le\_read\_tx\_power\_level](structbt__hci__rp__le__read__tx__power__level.md) {

[ 589](structbt__hci__rp__le__read__tx__power__level.md#a4c83db208bfcb7c9fd2211d192a26d90) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__tx__power__level.md#a4c83db208bfcb7c9fd2211d192a26d90);

[ 590](structbt__hci__rp__le__read__tx__power__level.md#aec00dfb34abce2d95af183b74f63d1f3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__read__tx__power__level.md#aec00dfb34abce2d95af183b74f63d1f3);

[ 591](structbt__hci__rp__le__read__tx__power__level.md#ae65a43aad74b1081e88afdb533cbe813) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__rp__le__read__tx__power__level.md#ae65a43aad74b1081e88afdb533cbe813);

[ 592](structbt__hci__rp__le__read__tx__power__level.md#ad14f660eb67f1014d1a62b0e5a113969) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [current\_tx\_power\_level](structbt__hci__rp__le__read__tx__power__level.md#ad14f660eb67f1014d1a62b0e5a113969);

[ 593](structbt__hci__rp__le__read__tx__power__level.md#a5f9c59660f7c5842712a4ad9ae1d9527) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [max\_tx\_power\_level](structbt__hci__rp__le__read__tx__power__level.md#a5f9c59660f7c5842712a4ad9ae1d9527);

594} \_\_packed;

595

[ 596](hci__types_8h.md#ac5bc187df83f28a48ba1f87f84aed54a)#define BT\_HCI\_OP\_LE\_READ\_REMOTE\_TX\_POWER\_LEVEL BT\_OP(BT\_OGF\_LE, 0x0077) /\* 0x2077 \*/

597

[ 598](hci__types_8h.md#a46bac5521c33da56df1d06ed7c472a06)#define BT\_HCI\_LE\_TX\_POWER\_REPORT\_DISABLE 0x00

[ 599](hci__types_8h.md#a31f7372543b6dec580fe464ec011d752)#define BT\_HCI\_LE\_TX\_POWER\_REPORT\_ENABLE 0x01

[ 600](hci__types_8h.md#aec22a58c052e856558b316b4f94f8561)#define BT\_HCI\_OP\_LE\_SET\_TX\_POWER\_REPORT\_ENABLE BT\_OP(BT\_OGF\_LE, 0x007A) /\* 0x207A \*/

[ 601](structbt__hci__cp__le__set__tx__power__report__enable.md)struct [bt\_hci\_cp\_le\_set\_tx\_power\_report\_enable](structbt__hci__cp__le__set__tx__power__report__enable.md) {

[ 602](structbt__hci__cp__le__set__tx__power__report__enable.md#a4a37c87f8f6a966a90c5de09096d1356) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__set__tx__power__report__enable.md#a4a37c87f8f6a966a90c5de09096d1356);

[ 603](structbt__hci__cp__le__set__tx__power__report__enable.md#a30580470d1ba516d86c8b157ca415ef3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [local\_enable](structbt__hci__cp__le__set__tx__power__report__enable.md#a30580470d1ba516d86c8b157ca415ef3);

[ 604](structbt__hci__cp__le__set__tx__power__report__enable.md#ab4e8fb4fd7a1fbbc8b5736f8a6f65c5e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [remote\_enable](structbt__hci__cp__le__set__tx__power__report__enable.md#ab4e8fb4fd7a1fbbc8b5736f8a6f65c5e);

605} \_\_packed;

606

[ 607](hci__types_8h.md#a252ef06a33818e117fc7f8146413cbd0)#define BT\_HCI\_CTL\_TO\_HOST\_FLOW\_DISABLE 0x00

[ 608](hci__types_8h.md#a4231ce6514091008191d5843b2c0b452)#define BT\_HCI\_CTL\_TO\_HOST\_FLOW\_ENABLE 0x01

[ 609](hci__types_8h.md#abe87fa64cb529d2cfe7ddf4fa045d3b5)#define BT\_HCI\_OP\_SET\_CTL\_TO\_HOST\_FLOW BT\_OP(BT\_OGF\_BASEBAND, 0x0031) /\* 0x0c31 \*/

[ 610](structbt__hci__cp__set__ctl__to__host__flow.md)struct [bt\_hci\_cp\_set\_ctl\_to\_host\_flow](structbt__hci__cp__set__ctl__to__host__flow.md) {

[ 611](structbt__hci__cp__set__ctl__to__host__flow.md#a75b614de1ab1fbfc6aa9c11d833976a6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flow\_enable](structbt__hci__cp__set__ctl__to__host__flow.md#a75b614de1ab1fbfc6aa9c11d833976a6);

612} \_\_packed;

613

[ 614](hci__types_8h.md#a2e05f146890ad81be27dca91250bf69d)#define BT\_HCI\_OP\_HOST\_BUFFER\_SIZE BT\_OP(BT\_OGF\_BASEBAND, 0x0033) /\* 0x0c33 \*/

[ 615](structbt__hci__cp__host__buffer__size.md)struct [bt\_hci\_cp\_host\_buffer\_size](structbt__hci__cp__host__buffer__size.md) {

[ 616](structbt__hci__cp__host__buffer__size.md#a07039a81ba81c700a26009ea407744b6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [acl\_mtu](structbt__hci__cp__host__buffer__size.md#a07039a81ba81c700a26009ea407744b6);

[ 617](structbt__hci__cp__host__buffer__size.md#a1b1d8c7f60ecbb13699b815bc8fca550) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sco\_mtu](structbt__hci__cp__host__buffer__size.md#a1b1d8c7f60ecbb13699b815bc8fca550);

[ 618](structbt__hci__cp__host__buffer__size.md#a8240837fecc7c50461724b697f0eda47) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [acl\_pkts](structbt__hci__cp__host__buffer__size.md#a8240837fecc7c50461724b697f0eda47);

[ 619](structbt__hci__cp__host__buffer__size.md#a943252480194e1a8608951be08b6b91c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sco\_pkts](structbt__hci__cp__host__buffer__size.md#a943252480194e1a8608951be08b6b91c);

620} \_\_packed;

621

[ 622](structbt__hci__handle__count.md)struct [bt\_hci\_handle\_count](structbt__hci__handle__count.md) {

[ 623](structbt__hci__handle__count.md#acacc000905835724b7fe882a8ad85f82) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__handle__count.md#acacc000905835724b7fe882a8ad85f82);

[ 624](structbt__hci__handle__count.md#a71577f376985909744fa14f246e69e1d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [count](structbt__hci__handle__count.md#a71577f376985909744fa14f246e69e1d);

625} \_\_packed;

626

[ 627](hci__types_8h.md#a6c7afa8e3b324714bc5f8dce9702604d)#define BT\_HCI\_OP\_HOST\_NUM\_COMPLETED\_PACKETS BT\_OP(BT\_OGF\_BASEBAND, 0x0035) /\* 0x0c35 \*/

[ 628](structbt__hci__cp__host__num__completed__packets.md)struct [bt\_hci\_cp\_host\_num\_completed\_packets](structbt__hci__cp__host__num__completed__packets.md) {

[ 629](structbt__hci__cp__host__num__completed__packets.md#a43a42e52757de9ec307e8a828dff416f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_handles](structbt__hci__cp__host__num__completed__packets.md#a43a42e52757de9ec307e8a828dff416f);

[ 630](structbt__hci__cp__host__num__completed__packets.md#a127f146b4967de49bc74b90ce1643eb7) struct [bt\_hci\_handle\_count](structbt__hci__handle__count.md) [h](structbt__hci__cp__host__num__completed__packets.md#a127f146b4967de49bc74b90ce1643eb7)[0];

631} \_\_packed;

632

[ 633](hci__types_8h.md#a04985a29d0f131c09aeb9769689b727b)#define BT\_HCI\_OP\_WRITE\_INQUIRY\_MODE BT\_OP(BT\_OGF\_BASEBAND, 0x0045) /\* 0x0c45 \*/

[ 634](structbt__hci__cp__write__inquiry__mode.md)struct [bt\_hci\_cp\_write\_inquiry\_mode](structbt__hci__cp__write__inquiry__mode.md) {

[ 635](structbt__hci__cp__write__inquiry__mode.md#a827e138b7faaec54ec84a1cc1e0c480f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mode](structbt__hci__cp__write__inquiry__mode.md#a827e138b7faaec54ec84a1cc1e0c480f);

636} \_\_packed;

637

[ 638](hci__types_8h.md#ac7a73c5e38a2308d56f0dbaaf0a4795b)#define BT\_HCI\_OP\_WRITE\_SSP\_MODE BT\_OP(BT\_OGF\_BASEBAND, 0x0056) /\* 0x0c56 \*/

[ 639](structbt__hci__cp__write__ssp__mode.md)struct [bt\_hci\_cp\_write\_ssp\_mode](structbt__hci__cp__write__ssp__mode.md) {

[ 640](structbt__hci__cp__write__ssp__mode.md#a8ebf7f7890adec53aa8c2307d2b1a33f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mode](structbt__hci__cp__write__ssp__mode.md#a8ebf7f7890adec53aa8c2307d2b1a33f);

641} \_\_packed;

642

[ 643](hci__types_8h.md#af5d2954950e00dfd5a69fc19db0fe530)#define BT\_HCI\_OP\_SET\_EVENT\_MASK\_PAGE\_2 BT\_OP(BT\_OGF\_BASEBAND, 0x0063) /\* 0x0c63 \*/

[ 644](structbt__hci__cp__set__event__mask__page__2.md)struct [bt\_hci\_cp\_set\_event\_mask\_page\_2](structbt__hci__cp__set__event__mask__page__2.md) {

[ 645](structbt__hci__cp__set__event__mask__page__2.md#aacf1308d0892226e2c10216a07cd1fcc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [events\_page\_2](structbt__hci__cp__set__event__mask__page__2.md#aacf1308d0892226e2c10216a07cd1fcc)[8];

646} \_\_packed;

647

[ 648](hci__types_8h.md#a2afc45fe32acff87265d36865c8d0b17)#define BT\_HCI\_OP\_LE\_WRITE\_LE\_HOST\_SUPP BT\_OP(BT\_OGF\_BASEBAND, 0x006d) /\* 0x0c6d \*/

[ 649](structbt__hci__cp__write__le__host__supp.md)struct [bt\_hci\_cp\_write\_le\_host\_supp](structbt__hci__cp__write__le__host__supp.md) {

[ 650](structbt__hci__cp__write__le__host__supp.md#ace1838a80b6061231b536f36e8999ac0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [le](structbt__hci__cp__write__le__host__supp.md#ace1838a80b6061231b536f36e8999ac0);

[ 651](structbt__hci__cp__write__le__host__supp.md#ad2c27c0f98b2334490022e90563e1271) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [simul](structbt__hci__cp__write__le__host__supp.md#ad2c27c0f98b2334490022e90563e1271);

652} \_\_packed;

653

[ 654](hci__types_8h.md#a0480dd89b0f851d0a791b97138b01a5b)#define BT\_HCI\_OP\_WRITE\_SC\_HOST\_SUPP BT\_OP(BT\_OGF\_BASEBAND, 0x007a) /\* 0x0c7a \*/

[ 655](structbt__hci__cp__write__sc__host__supp.md)struct [bt\_hci\_cp\_write\_sc\_host\_supp](structbt__hci__cp__write__sc__host__supp.md) {

[ 656](structbt__hci__cp__write__sc__host__supp.md#a48ef951f4de05c5772be5c08edca7cec) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sc\_support](structbt__hci__cp__write__sc__host__supp.md#a48ef951f4de05c5772be5c08edca7cec);

657} \_\_packed;

658

[ 659](hci__types_8h.md#a0ea6134bcd33e24b068f35d080cdc4e0)#define BT\_HCI\_OP\_READ\_AUTH\_PAYLOAD\_TIMEOUT BT\_OP(BT\_OGF\_BASEBAND, 0x007b) /\* 0x0c7b \*/

[ 660](structbt__hci__cp__read__auth__payload__timeout.md)struct [bt\_hci\_cp\_read\_auth\_payload\_timeout](structbt__hci__cp__read__auth__payload__timeout.md) {

[ 661](structbt__hci__cp__read__auth__payload__timeout.md#adcdd657feb3ea6b892e2a5034365dd77) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__read__auth__payload__timeout.md#adcdd657feb3ea6b892e2a5034365dd77);

662} \_\_packed;

663

[ 664](structbt__hci__rp__read__auth__payload__timeout.md)struct [bt\_hci\_rp\_read\_auth\_payload\_timeout](structbt__hci__rp__read__auth__payload__timeout.md) {

[ 665](structbt__hci__rp__read__auth__payload__timeout.md#a3eadeab880eb75c914be654dbc685f3f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__auth__payload__timeout.md#a3eadeab880eb75c914be654dbc685f3f);

[ 666](structbt__hci__rp__read__auth__payload__timeout.md#ab53b7e03c68dcd040e38fdc7429b2d3b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__read__auth__payload__timeout.md#ab53b7e03c68dcd040e38fdc7429b2d3b);

[ 667](structbt__hci__rp__read__auth__payload__timeout.md#ab4092720dad9a01f4e179eb2f0112aed) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [auth\_payload\_timeout](structbt__hci__rp__read__auth__payload__timeout.md#ab4092720dad9a01f4e179eb2f0112aed);

668} \_\_packed;

669

[ 670](hci__types_8h.md#ae74450b7b643f947fa2e83a80e0e2fae)#define BT\_HCI\_OP\_WRITE\_AUTH\_PAYLOAD\_TIMEOUT BT\_OP(BT\_OGF\_BASEBAND, 0x007c) /\* 0x0c7c \*/

[ 671](structbt__hci__cp__write__auth__payload__timeout.md)struct [bt\_hci\_cp\_write\_auth\_payload\_timeout](structbt__hci__cp__write__auth__payload__timeout.md) {

[ 672](structbt__hci__cp__write__auth__payload__timeout.md#ad99d5b9f416f11492ac0f412b400aeb6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__write__auth__payload__timeout.md#ad99d5b9f416f11492ac0f412b400aeb6);

[ 673](structbt__hci__cp__write__auth__payload__timeout.md#a385c88012b09ec561b9ba7edaadeb574) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [auth\_payload\_timeout](structbt__hci__cp__write__auth__payload__timeout.md#a385c88012b09ec561b9ba7edaadeb574);

674} \_\_packed;

675

[ 676](structbt__hci__rp__write__auth__payload__timeout.md)struct [bt\_hci\_rp\_write\_auth\_payload\_timeout](structbt__hci__rp__write__auth__payload__timeout.md) {

[ 677](structbt__hci__rp__write__auth__payload__timeout.md#af1783a29e6a167fc20b62bd273215b35) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__write__auth__payload__timeout.md#af1783a29e6a167fc20b62bd273215b35);

[ 678](structbt__hci__rp__write__auth__payload__timeout.md#a467c6585c913dba03dcfdf5bf4fa688e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__write__auth__payload__timeout.md#a467c6585c913dba03dcfdf5bf4fa688e);

679} \_\_packed;

680

[ 681](hci__types_8h.md#abc80a803d0e540541bcd889772e59940)#define BT\_HCI\_OP\_CONFIGURE\_DATA\_PATH BT\_OP(BT\_OGF\_BASEBAND, 0x0083) /\* 0x0c83 \*/

[ 682](structbt__hci__cp__configure__data__path.md)struct [bt\_hci\_cp\_configure\_data\_path](structbt__hci__cp__configure__data__path.md) {

[ 683](structbt__hci__cp__configure__data__path.md#a528ba2bd5a220d1b7db064f8b51a8718) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_path\_dir](structbt__hci__cp__configure__data__path.md#a528ba2bd5a220d1b7db064f8b51a8718);

[ 684](structbt__hci__cp__configure__data__path.md#a92967e6b5258b2acd6d82bfbfb8b7940) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_path\_id](structbt__hci__cp__configure__data__path.md#a92967e6b5258b2acd6d82bfbfb8b7940);

[ 685](structbt__hci__cp__configure__data__path.md#a2573fe029e1774bf5fa7e8cffff08cec) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [vs\_config\_len](structbt__hci__cp__configure__data__path.md#a2573fe029e1774bf5fa7e8cffff08cec);

[ 686](structbt__hci__cp__configure__data__path.md#aa79c4aa6603b09f49a8c7f216f135e6e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [vs\_config](structbt__hci__cp__configure__data__path.md#aa79c4aa6603b09f49a8c7f216f135e6e)[0];

687} \_\_packed;

688

[ 689](structbt__hci__rp__configure__data__path.md)struct [bt\_hci\_rp\_configure\_data\_path](structbt__hci__rp__configure__data__path.md) {

[ 690](structbt__hci__rp__configure__data__path.md#a10cfe9bf5a7be202706957d7b8e1f371) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__configure__data__path.md#a10cfe9bf5a7be202706957d7b8e1f371);

691} \_\_packed;

692

693/\* HCI version from Assigned Numbers \*/

[ 694](hci__types_8h.md#a4947ee8a84f7cd81e242ee812b5b8760)#define BT\_HCI\_VERSION\_1\_0B 0

[ 695](hci__types_8h.md#a0fac5f104d8ab1539e84a900aafa9e43)#define BT\_HCI\_VERSION\_1\_1 1

[ 696](hci__types_8h.md#afe6fd8249a97d3762fe454bfb7eab021)#define BT\_HCI\_VERSION\_1\_2 2

[ 697](hci__types_8h.md#afc0d24e2ba5e6b992aec81104cbf035e)#define BT\_HCI\_VERSION\_2\_0 3

[ 698](hci__types_8h.md#a98d73e8f548d5ae7eddff91a3e647aae)#define BT\_HCI\_VERSION\_2\_1 4

[ 699](hci__types_8h.md#acaf91cc6895552243c5b85c2fc007db5)#define BT\_HCI\_VERSION\_3\_0 5

[ 700](hci__types_8h.md#aeb77e725323c3f31c90482e676dad08a)#define BT\_HCI\_VERSION\_4\_0 6

[ 701](hci__types_8h.md#a08cca779ede398a551359efccdaf3090)#define BT\_HCI\_VERSION\_4\_1 7

[ 702](hci__types_8h.md#aa398d6e6fcca0b427a2ccd3a0a343835)#define BT\_HCI\_VERSION\_4\_2 8

[ 703](hci__types_8h.md#a9a203a5a633d28c644b30125d437701a)#define BT\_HCI\_VERSION\_5\_0 9

[ 704](hci__types_8h.md#acfa0dbddfde8ee82b114dd34ff75c5bc)#define BT\_HCI\_VERSION\_5\_1 10

[ 705](hci__types_8h.md#aa4828a916c53d97de0541992d0359c09)#define BT\_HCI\_VERSION\_5\_2 11

[ 706](hci__types_8h.md#a37b04f40e68e821a1aac3b785903b379)#define BT\_HCI\_VERSION\_5\_3 12

[ 707](hci__types_8h.md#ae8eadab2b7be415160f145bd63bae367)#define BT\_HCI\_VERSION\_5\_4 13

708

[ 709](hci__types_8h.md#a195b8faf6d7d3e4f1b528185c73b4d67)#define BT\_HCI\_OP\_READ\_LOCAL\_VERSION\_INFO BT\_OP(BT\_OGF\_INFO, 0x0001) /\* 0x1001 \*/

[ 710](structbt__hci__rp__read__local__version__info.md)struct [bt\_hci\_rp\_read\_local\_version\_info](structbt__hci__rp__read__local__version__info.md) {

[ 711](structbt__hci__rp__read__local__version__info.md#a935f990f7c28f7c89660c2b8ab975f43) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__local__version__info.md#a935f990f7c28f7c89660c2b8ab975f43);

[ 712](structbt__hci__rp__read__local__version__info.md#a1cc521426e530344a328e935152dd488) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [hci\_version](structbt__hci__rp__read__local__version__info.md#a1cc521426e530344a328e935152dd488);

[ 713](structbt__hci__rp__read__local__version__info.md#a04161ed3cc0b9c3c442e3464501ce118) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [hci\_revision](structbt__hci__rp__read__local__version__info.md#a04161ed3cc0b9c3c442e3464501ce118);

[ 714](structbt__hci__rp__read__local__version__info.md#a634641751852f66aabb408bf1b4d0cd2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [lmp\_version](structbt__hci__rp__read__local__version__info.md#a634641751852f66aabb408bf1b4d0cd2);

[ 715](structbt__hci__rp__read__local__version__info.md#a7cd6ba190137eaf7c4eb9c2d7e5b36ce) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [manufacturer](structbt__hci__rp__read__local__version__info.md#a7cd6ba190137eaf7c4eb9c2d7e5b36ce);

[ 716](structbt__hci__rp__read__local__version__info.md#a43f29cf08a2399e818bfa441c6b7a1f3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [lmp\_subversion](structbt__hci__rp__read__local__version__info.md#a43f29cf08a2399e818bfa441c6b7a1f3);

717} \_\_packed;

718

[ 719](hci__types_8h.md#ac0d7533d221db0fa44cfb83135dfcc6a)#define BT\_HCI\_OP\_READ\_SUPPORTED\_COMMANDS BT\_OP(BT\_OGF\_INFO, 0x0002) /\* 0x1002 \*/

[ 720](structbt__hci__rp__read__supported__commands.md)struct [bt\_hci\_rp\_read\_supported\_commands](structbt__hci__rp__read__supported__commands.md) {

[ 721](structbt__hci__rp__read__supported__commands.md#a3d36d892f83cfcb1d2fc955ec71ff061) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__supported__commands.md#a3d36d892f83cfcb1d2fc955ec71ff061);

[ 722](structbt__hci__rp__read__supported__commands.md#afd0dc4411a4c7692515139392bffedd0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [commands](structbt__hci__rp__read__supported__commands.md#afd0dc4411a4c7692515139392bffedd0)[64];

723} \_\_packed;

724

[ 725](hci__types_8h.md#a882f120b35a9baa2f70bc33ef5ced6d3)#define BT\_HCI\_OP\_READ\_LOCAL\_EXT\_FEATURES BT\_OP(BT\_OGF\_INFO, 0x0004) /\* 0x1004 \*/

[ 726](structbt__hci__cp__read__local__ext__features.md)struct [bt\_hci\_cp\_read\_local\_ext\_features](structbt__hci__cp__read__local__ext__features.md) {

[ 727](structbt__hci__cp__read__local__ext__features.md#a79c6a6a6f1026a7e9ee774183ea7e132) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [page](structbt__hci__cp__read__local__ext__features.md#a79c6a6a6f1026a7e9ee774183ea7e132);

728};

[ 729](structbt__hci__rp__read__local__ext__features.md)struct [bt\_hci\_rp\_read\_local\_ext\_features](structbt__hci__rp__read__local__ext__features.md) {

[ 730](structbt__hci__rp__read__local__ext__features.md#a9011f2c89f75939fa92fcf249d2203da) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__local__ext__features.md#a9011f2c89f75939fa92fcf249d2203da);

[ 731](structbt__hci__rp__read__local__ext__features.md#a7e3669651dc2c2ed9541b7e4945a27f9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [page](structbt__hci__rp__read__local__ext__features.md#a7e3669651dc2c2ed9541b7e4945a27f9);

[ 732](structbt__hci__rp__read__local__ext__features.md#a3532e208b3fd347db80d8c55eade3c2d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_page](structbt__hci__rp__read__local__ext__features.md#a3532e208b3fd347db80d8c55eade3c2d);

[ 733](structbt__hci__rp__read__local__ext__features.md#a669e8c6faa4e45f472e4f8a3ebb03050) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ext\_features](structbt__hci__rp__read__local__ext__features.md#a669e8c6faa4e45f472e4f8a3ebb03050)[8];

734} \_\_packed;

735

[ 736](hci__types_8h.md#a8524505dff48ceb41c008c8662da6408)#define BT\_HCI\_OP\_READ\_LOCAL\_FEATURES BT\_OP(BT\_OGF\_INFO, 0x0003) /\* 0x1003 \*/

[ 737](structbt__hci__rp__read__local__features.md)struct [bt\_hci\_rp\_read\_local\_features](structbt__hci__rp__read__local__features.md) {

[ 738](structbt__hci__rp__read__local__features.md#a0ff73da5704ada47f8f79c113254820d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__local__features.md#a0ff73da5704ada47f8f79c113254820d);

[ 739](structbt__hci__rp__read__local__features.md#ae660b4a772f96bf72bd08124bf26b352) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [features](structbt__hci__rp__read__local__features.md#ae660b4a772f96bf72bd08124bf26b352)[8];

740} \_\_packed;

741

[ 742](hci__types_8h.md#acd5d9ecda744969d4692e6ebface2e53)#define BT\_HCI\_OP\_READ\_BUFFER\_SIZE BT\_OP(BT\_OGF\_INFO, 0x0005) /\* 0x1005 \*/

[ 743](structbt__hci__rp__read__buffer__size.md)struct [bt\_hci\_rp\_read\_buffer\_size](structbt__hci__rp__read__buffer__size.md) {

[ 744](structbt__hci__rp__read__buffer__size.md#a6adf126acfcec722dc078d097d2b2ba8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__buffer__size.md#a6adf126acfcec722dc078d097d2b2ba8);

[ 745](structbt__hci__rp__read__buffer__size.md#aba3f1597c929e3721c769beb98000218) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [acl\_max\_len](structbt__hci__rp__read__buffer__size.md#aba3f1597c929e3721c769beb98000218);

[ 746](structbt__hci__rp__read__buffer__size.md#a7d475559145f469006b2ef147704cd99) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sco\_max\_len](structbt__hci__rp__read__buffer__size.md#a7d475559145f469006b2ef147704cd99);

[ 747](structbt__hci__rp__read__buffer__size.md#a87ff361282be71aa60c7f88c50a7492f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [acl\_max\_num](structbt__hci__rp__read__buffer__size.md#a87ff361282be71aa60c7f88c50a7492f);

[ 748](structbt__hci__rp__read__buffer__size.md#abc01fa1df6d787f0a2cb865daed5f4cc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sco\_max\_num](structbt__hci__rp__read__buffer__size.md#abc01fa1df6d787f0a2cb865daed5f4cc);

749} \_\_packed;

750

[ 751](hci__types_8h.md#a4ba1bf2078ac12686e2a7727f637f70b)#define BT\_HCI\_OP\_READ\_BD\_ADDR BT\_OP(BT\_OGF\_INFO, 0x0009) /\* 0x1009 \*/

[ 752](structbt__hci__rp__read__bd__addr.md)struct [bt\_hci\_rp\_read\_bd\_addr](structbt__hci__rp__read__bd__addr.md) {

[ 753](structbt__hci__rp__read__bd__addr.md#a5230de2a3a6c4161d076b59901790e1e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__bd__addr.md#a5230de2a3a6c4161d076b59901790e1e);

[ 754](structbt__hci__rp__read__bd__addr.md#aec2c022a465982a3868100699c95f4e6) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__rp__read__bd__addr.md#aec2c022a465982a3868100699c95f4e6);

755} \_\_packed;

756

757/\* logic transport type bits as returned when reading supported codecs \*/

[ 758](hci__types_8h.md#a89eeffc2f46c776ecdb5eea81cb1f47a)#define BT\_HCI\_CODEC\_TRANSPORT\_MASK\_BREDR\_ACL BIT(0)

[ 759](hci__types_8h.md#ab50b70f27bd9beb4da6fe8d4b91398c1)#define BT\_HCI\_CODEC\_TRANSPORT\_MASK\_BREDR\_SCO BIT(1)

[ 760](hci__types_8h.md#a38dd1118554de13f3f6f2853900212c5)#define BT\_HCI\_CODEC\_TRANSPORT\_MASK\_LE\_CIS BIT(2)

[ 761](hci__types_8h.md#a7d90fc1df2260a4067c3eb4ab169c406)#define BT\_HCI\_CODEC\_TRANSPORT\_MASK\_LE\_BIS BIT(3)

762

763/\* logic transport types for reading codec capabilities and controller delays \*/

[ 764](hci__types_8h.md#a73dfca6788b272380e6920d2907bf43f)#define BT\_HCI\_LOGICAL\_TRANSPORT\_TYPE\_BREDR\_ACL 0x00

[ 765](hci__types_8h.md#ad10d8c5ffd49cb183731a9ba97c0e058)#define BT\_HCI\_LOGICAL\_TRANSPORT\_TYPE\_BREDR\_SCO 0x01

[ 766](hci__types_8h.md#a5e53f28cedf59f18ce8d494f16933b3c)#define BT\_HCI\_LOGICAL\_TRANSPORT\_TYPE\_LE\_CIS 0x02

[ 767](hci__types_8h.md#a560cb22e5f39c144e3d477eea5c32beb)#define BT\_HCI\_LOGICAL\_TRANSPORT\_TYPE\_LE\_BIS 0x03

768

769/\* audio datapath directions \*/

[ 770](hci__types_8h.md#a0f74c19fabbcb3088e1a819d33a05a1c)#define BT\_HCI\_DATAPATH\_DIR\_HOST\_TO\_CTLR 0x00

[ 771](hci__types_8h.md#af8d89c712a3d27f9b6f92a31bea2a8c3)#define BT\_HCI\_DATAPATH\_DIR\_CTLR\_TO\_HOST 0x01

772

773/\* audio datapath IDs \*/

[ 774](hci__types_8h.md#a5f748cb264265b9fc12f146ba47fa14c)#define BT\_HCI\_DATAPATH\_ID\_HCI 0x00

[ 775](hci__types_8h.md#a0382b1713c7b2a774a8f004b6d1bc33f)#define BT\_HCI\_DATAPATH\_ID\_VS 0x01

[ 776](hci__types_8h.md#abf755f2839b36a3ac3431bff04193b2f)#define BT\_HCI\_DATAPATH\_ID\_VS\_END 0xfe

777

778/\* coding format assigned numbers, used for codec IDs \*/

[ 779](hci__types_8h.md#a4f4939e7fa43ab73861f64d25b6549d8)#define BT\_HCI\_CODING\_FORMAT\_ULAW\_LOG 0x00

[ 780](hci__types_8h.md#a36f18d10467a580e9864eb8629b8ce01)#define BT\_HCI\_CODING\_FORMAT\_ALAW\_LOG 0x01

[ 781](hci__types_8h.md#a80dc369e54038df30f44ca4c13ee14d6)#define BT\_HCI\_CODING\_FORMAT\_CVSD 0x02

[ 782](hci__types_8h.md#ad93af498e2265c180a01055eca2a4de0)#define BT\_HCI\_CODING\_FORMAT\_TRANSPARENT 0x03

[ 783](hci__types_8h.md#a2630de3f8cc3ccc3d81f0f2fa4084587)#define BT\_HCI\_CODING\_FORMAT\_LINEAR\_PCM 0x04

[ 784](hci__types_8h.md#a9178f80b7783c9cffb4574667d3033af)#define BT\_HCI\_CODING\_FORMAT\_MSBC 0x05

[ 785](hci__types_8h.md#a1fa62d6f28ef56ebe9c18d5ab86fbf8e)#define BT\_HCI\_CODING\_FORMAT\_LC3 0x06

[ 786](hci__types_8h.md#a405e22871772b5155f99774178e4093d)#define BT\_HCI\_CODING\_FORMAT\_G729A 0x07

[ 787](hci__types_8h.md#a46839c453b81e80fb8e578f89dc31864)#define BT\_HCI\_CODING\_FORMAT\_VS 0xFF

788

789

[ 790](hci__types_8h.md#a8755487f4672f196051cc513894e4603)#define BT\_HCI\_OP\_READ\_CODECS BT\_OP(BT\_OGF\_INFO, 0x000b) /\* 0x100b \*/

[ 791](structbt__hci__std__codec__info.md)struct [bt\_hci\_std\_codec\_info](structbt__hci__std__codec__info.md) {

[ 792](structbt__hci__std__codec__info.md#a56e21eca5bbc83cb081aea1c67a7a60d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [codec\_id](structbt__hci__std__codec__info.md#a56e21eca5bbc83cb081aea1c67a7a60d);

793} \_\_packed;

[ 794](structbt__hci__std__codecs.md)struct [bt\_hci\_std\_codecs](structbt__hci__std__codecs.md) {

[ 795](structbt__hci__std__codecs.md#ad3e63bf445bb6b8e654baa8490cdf547) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_codecs](structbt__hci__std__codecs.md#ad3e63bf445bb6b8e654baa8490cdf547);

[ 796](structbt__hci__std__codecs.md#a32767e90384ef74a3e740597eacfcf53) struct [bt\_hci\_std\_codec\_info](structbt__hci__std__codec__info.md) [codec\_info](structbt__hci__std__codecs.md#a32767e90384ef74a3e740597eacfcf53)[0];

797} \_\_packed;

[ 798](structbt__hci__vs__codec__info.md)struct [bt\_hci\_vs\_codec\_info](structbt__hci__vs__codec__info.md) {

[ 799](structbt__hci__vs__codec__info.md#a8170dac825b76f3dfb5fde5eed04c4c0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [company\_id](structbt__hci__vs__codec__info.md#a8170dac825b76f3dfb5fde5eed04c4c0);

[ 800](structbt__hci__vs__codec__info.md#a3c7eea7bae36c7a63457051401526382) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [codec\_id](structbt__hci__vs__codec__info.md#a3c7eea7bae36c7a63457051401526382);

801} \_\_packed;

[ 802](structbt__hci__vs__codecs.md)struct [bt\_hci\_vs\_codecs](structbt__hci__vs__codecs.md) {

[ 803](structbt__hci__vs__codecs.md#a2caf18ce5905e3962da000f3b00b623f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_codecs](structbt__hci__vs__codecs.md#a2caf18ce5905e3962da000f3b00b623f);

[ 804](structbt__hci__vs__codecs.md#a4e72426599d5bc617fde4f1a4a095527) struct [bt\_hci\_vs\_codec\_info](structbt__hci__vs__codec__info.md) [codec\_info](structbt__hci__vs__codecs.md#a4e72426599d5bc617fde4f1a4a095527)[0];

805} \_\_packed;

[ 806](structbt__hci__rp__read__codecs.md)struct [bt\_hci\_rp\_read\_codecs](structbt__hci__rp__read__codecs.md) {

[ 807](structbt__hci__rp__read__codecs.md#a017182988634c6acbfbfdd7c9609f5dc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__codecs.md#a017182988634c6acbfbfdd7c9609f5dc);

808 /\* other fields filled in dynamically \*/

[ 809](structbt__hci__rp__read__codecs.md#a44e615f375b35cce9f949562555c429b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [codecs](structbt__hci__rp__read__codecs.md#a44e615f375b35cce9f949562555c429b)[0];

810} \_\_packed;

811

[ 812](hci__types_8h.md#acb09b1a94453c1c341decabc029bbc04)#define BT\_HCI\_OP\_READ\_CODECS\_V2 BT\_OP(BT\_OGF\_INFO, 0x000d) /\* 0x100d \*/

[ 813](structbt__hci__std__codec__info__v2.md)struct [bt\_hci\_std\_codec\_info\_v2](structbt__hci__std__codec__info__v2.md) {

[ 814](structbt__hci__std__codec__info__v2.md#ae82a0896904c7feb2634579b393bf05e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [codec\_id](structbt__hci__std__codec__info__v2.md#ae82a0896904c7feb2634579b393bf05e);

[ 815](structbt__hci__std__codec__info__v2.md#aea766ba4b911223eeb351e0123e54f5f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [transports](structbt__hci__std__codec__info__v2.md#aea766ba4b911223eeb351e0123e54f5f); /\* bitmap \*/

816} \_\_packed;

[ 817](structbt__hci__std__codecs__v2.md)struct [bt\_hci\_std\_codecs\_v2](structbt__hci__std__codecs__v2.md) {

[ 818](structbt__hci__std__codecs__v2.md#ab14fdde478e290235f68aae375969c09) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_codecs](structbt__hci__std__codecs__v2.md#ab14fdde478e290235f68aae375969c09);

[ 819](structbt__hci__std__codecs__v2.md#aafdb6d96d99063a7a447d80e1830a624) struct [bt\_hci\_std\_codec\_info\_v2](structbt__hci__std__codec__info__v2.md) [codec\_info](structbt__hci__std__codecs__v2.md#aafdb6d96d99063a7a447d80e1830a624)[0];

820} \_\_packed;

[ 821](structbt__hci__vs__codec__info__v2.md)struct [bt\_hci\_vs\_codec\_info\_v2](structbt__hci__vs__codec__info__v2.md) {

[ 822](structbt__hci__vs__codec__info__v2.md#aa6ce27b4acd3dff516e4d7ed2e6434bc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [company\_id](structbt__hci__vs__codec__info__v2.md#aa6ce27b4acd3dff516e4d7ed2e6434bc);

[ 823](structbt__hci__vs__codec__info__v2.md#ae7b7d5d65629a1e3039b3c7cf167a9c1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [codec\_id](structbt__hci__vs__codec__info__v2.md#ae7b7d5d65629a1e3039b3c7cf167a9c1);

[ 824](structbt__hci__vs__codec__info__v2.md#ac2a91a045e4b53315850b6d4f1d38b2c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [transports](structbt__hci__vs__codec__info__v2.md#ac2a91a045e4b53315850b6d4f1d38b2c); /\* bitmap \*/

825} \_\_packed;

[ 826](structbt__hci__vs__codecs__v2.md)struct [bt\_hci\_vs\_codecs\_v2](structbt__hci__vs__codecs__v2.md) {

[ 827](structbt__hci__vs__codecs__v2.md#ae4cb3a40401594f8e0f18391b9d31a23) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_codecs](structbt__hci__vs__codecs__v2.md#ae4cb3a40401594f8e0f18391b9d31a23);

[ 828](structbt__hci__vs__codecs__v2.md#a6cd8aa58517d59d565474513f755cfee) struct [bt\_hci\_vs\_codec\_info\_v2](structbt__hci__vs__codec__info__v2.md) [codec\_info](structbt__hci__vs__codecs__v2.md#a6cd8aa58517d59d565474513f755cfee)[0];

829} \_\_packed;

[ 830](structbt__hci__rp__read__codecs__v2.md)struct [bt\_hci\_rp\_read\_codecs\_v2](structbt__hci__rp__read__codecs__v2.md) {

[ 831](structbt__hci__rp__read__codecs__v2.md#a2e9866d0f9fb42b54c406a9ea5890913) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__codecs__v2.md#a2e9866d0f9fb42b54c406a9ea5890913);

832 /\* other fields filled in dynamically \*/

[ 833](structbt__hci__rp__read__codecs__v2.md#a098563f274de085ac97415f1b5e15f3c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [codecs](structbt__hci__rp__read__codecs__v2.md#a098563f274de085ac97415f1b5e15f3c)[0];

834} \_\_packed;

835

[ 836](structbt__hci__cp__codec__id.md)struct [bt\_hci\_cp\_codec\_id](structbt__hci__cp__codec__id.md) {

[ 837](structbt__hci__cp__codec__id.md#aec80c74b12edb9c63330cc5a404eed5d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [coding\_format](structbt__hci__cp__codec__id.md#aec80c74b12edb9c63330cc5a404eed5d);

[ 838](structbt__hci__cp__codec__id.md#a98fd438270a64d843fa27c7c196645df) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [company\_id](structbt__hci__cp__codec__id.md#a98fd438270a64d843fa27c7c196645df);

[ 839](structbt__hci__cp__codec__id.md#a70296440c202544af11db2dc8e80fc5b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [vs\_codec\_id](structbt__hci__cp__codec__id.md#a70296440c202544af11db2dc8e80fc5b);

840} \_\_packed;

841

[ 842](hci__types_8h.md#a4b9e24d16cd92ce6ee1d6444410cfb43)#define BT\_HCI\_OP\_READ\_CODEC\_CAPABILITIES BT\_OP(BT\_OGF\_INFO, 0x000e) /\* 0x100e \*/

[ 843](structbt__hci__cp__read__codec__capabilities.md)struct [bt\_hci\_cp\_read\_codec\_capabilities](structbt__hci__cp__read__codec__capabilities.md) {

[ 844](structbt__hci__cp__read__codec__capabilities.md#ad48b7f228742d86a71dffa314331bbe1) struct [bt\_hci\_cp\_codec\_id](structbt__hci__cp__codec__id.md) [codec\_id](structbt__hci__cp__read__codec__capabilities.md#ad48b7f228742d86a71dffa314331bbe1);

[ 845](structbt__hci__cp__read__codec__capabilities.md#a6479561573172356d7515ef92f75b8d4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [transport](structbt__hci__cp__read__codec__capabilities.md#a6479561573172356d7515ef92f75b8d4);

[ 846](structbt__hci__cp__read__codec__capabilities.md#a237695f4d0a1359d5ce71d831708a69c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [direction](structbt__hci__cp__read__codec__capabilities.md#a237695f4d0a1359d5ce71d831708a69c);

847} \_\_packed;

[ 848](structbt__hci__codec__capability__info.md)struct [bt\_hci\_codec\_capability\_info](structbt__hci__codec__capability__info.md) {

[ 849](structbt__hci__codec__capability__info.md#a24516347742a8fd9f3386d78b66a4e81) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [length](structbt__hci__codec__capability__info.md#a24516347742a8fd9f3386d78b66a4e81);

[ 850](structbt__hci__codec__capability__info.md#ac53f02f2abdb832ed82da35a36abc323) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__hci__codec__capability__info.md#ac53f02f2abdb832ed82da35a36abc323)[0];

851} \_\_packed;

[ 852](structbt__hci__rp__read__codec__capabilities.md)struct [bt\_hci\_rp\_read\_codec\_capabilities](structbt__hci__rp__read__codec__capabilities.md) {

[ 853](structbt__hci__rp__read__codec__capabilities.md#ac224ea998e3af12f97232288266da8d2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__codec__capabilities.md#ac224ea998e3af12f97232288266da8d2);

[ 854](structbt__hci__rp__read__codec__capabilities.md#a71b7df63502bf42a26868e69893ddcfe) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_capabilities](structbt__hci__rp__read__codec__capabilities.md#a71b7df63502bf42a26868e69893ddcfe);

855 /\* other fields filled in dynamically \*/

[ 856](structbt__hci__rp__read__codec__capabilities.md#ae0c84013512c461f3b6231162d6f3020) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [capabilities](structbt__hci__rp__read__codec__capabilities.md#ae0c84013512c461f3b6231162d6f3020)[0];

857} \_\_packed;

858

[ 859](hci__types_8h.md#a9a183b26d18453d5daa6de2dcbe4d9a1)#define BT\_HCI\_OP\_READ\_CTLR\_DELAY BT\_OP(BT\_OGF\_INFO, 0x000f) /\* 0x100f \*/

[ 860](structbt__hci__cp__read__ctlr__delay.md)struct [bt\_hci\_cp\_read\_ctlr\_delay](structbt__hci__cp__read__ctlr__delay.md) {

[ 861](structbt__hci__cp__read__ctlr__delay.md#a2afb9ca8bc2e24cd479b29bc1a53c867) struct [bt\_hci\_cp\_codec\_id](structbt__hci__cp__codec__id.md) [codec\_id](structbt__hci__cp__read__ctlr__delay.md#a2afb9ca8bc2e24cd479b29bc1a53c867);

[ 862](structbt__hci__cp__read__ctlr__delay.md#a60a6a5b87896d0c27d734b56ead58a9b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [transport](structbt__hci__cp__read__ctlr__delay.md#a60a6a5b87896d0c27d734b56ead58a9b);

[ 863](structbt__hci__cp__read__ctlr__delay.md#a5e9f74d4f82809289038da29af0c663d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [direction](structbt__hci__cp__read__ctlr__delay.md#a5e9f74d4f82809289038da29af0c663d);

[ 864](structbt__hci__cp__read__ctlr__delay.md#ac881526b479d5f1717efbe35cdcc7e87) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [codec\_config\_len](structbt__hci__cp__read__ctlr__delay.md#ac881526b479d5f1717efbe35cdcc7e87);

[ 865](structbt__hci__cp__read__ctlr__delay.md#a6c15d141c40bca8bd095f4a86f5a93bd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [codec\_config](structbt__hci__cp__read__ctlr__delay.md#a6c15d141c40bca8bd095f4a86f5a93bd)[0];

866} \_\_packed;

[ 867](structbt__hci__rp__read__ctlr__delay.md)struct [bt\_hci\_rp\_read\_ctlr\_delay](structbt__hci__rp__read__ctlr__delay.md) {

[ 868](structbt__hci__rp__read__ctlr__delay.md#a2f17081cf767643f3a9ad9d115ef5320) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__ctlr__delay.md#a2f17081cf767643f3a9ad9d115ef5320);

[ 869](structbt__hci__rp__read__ctlr__delay.md#ab48d1d92cdf9470a93487434b3824d17) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [min\_ctlr\_delay](structbt__hci__rp__read__ctlr__delay.md#ab48d1d92cdf9470a93487434b3824d17)[3];

[ 870](structbt__hci__rp__read__ctlr__delay.md#a4c468053c4a86d1ab462c1e6f17f1013) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_ctlr\_delay](structbt__hci__rp__read__ctlr__delay.md#a4c468053c4a86d1ab462c1e6f17f1013)[3];

871} \_\_packed;

872

[ 873](hci__types_8h.md#a528902591490d9d20a6966a042254b3a)#define BT\_HCI\_OP\_READ\_RSSI BT\_OP(BT\_OGF\_STATUS, 0x0005) /\* 0x1405 \*/

[ 874](structbt__hci__cp__read__rssi.md)struct [bt\_hci\_cp\_read\_rssi](structbt__hci__cp__read__rssi.md) {

[ 875](structbt__hci__cp__read__rssi.md#a0662bc56b344ca2bf9a2dcabe8a13c09) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__read__rssi.md#a0662bc56b344ca2bf9a2dcabe8a13c09);

876} \_\_packed;

[ 877](structbt__hci__rp__read__rssi.md)struct [bt\_hci\_rp\_read\_rssi](structbt__hci__rp__read__rssi.md) {

[ 878](structbt__hci__rp__read__rssi.md#a8f91b69a99bd61a7a59d84b3a9c3f235) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__rssi.md#a8f91b69a99bd61a7a59d84b3a9c3f235);

[ 879](structbt__hci__rp__read__rssi.md#aa3c4041dd240b1185c7fc8bbef74a17a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__read__rssi.md#aa3c4041dd240b1185c7fc8bbef74a17a);

[ 880](structbt__hci__rp__read__rssi.md#a1071300bd61fcaab65683187ae393cae) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__hci__rp__read__rssi.md#a1071300bd61fcaab65683187ae393cae);

881} \_\_packed;

882

[ 883](hci__types_8h.md#ab4eedd90a583b3893c77f51aee16e3c0)#define BT\_HCI\_ENCRYPTION\_KEY\_SIZE\_MIN 7

[ 884](hci__types_8h.md#ae4271fbdb039750aceac7c0712d4f3db)#define BT\_HCI\_ENCRYPTION\_KEY\_SIZE\_MAX 16

885

[ 886](hci__types_8h.md#adefeb2117010fa2d53937ce513e28a18)#define BT\_HCI\_OP\_READ\_ENCRYPTION\_KEY\_SIZE BT\_OP(BT\_OGF\_STATUS, 0x0008) /\* 0x1408 \*/

[ 887](structbt__hci__cp__read__encryption__key__size.md)struct [bt\_hci\_cp\_read\_encryption\_key\_size](structbt__hci__cp__read__encryption__key__size.md) {

[ 888](structbt__hci__cp__read__encryption__key__size.md#af15765007fd0e2fc4186b54323553019) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__read__encryption__key__size.md#af15765007fd0e2fc4186b54323553019);

889} \_\_packed;

[ 890](structbt__hci__rp__read__encryption__key__size.md)struct [bt\_hci\_rp\_read\_encryption\_key\_size](structbt__hci__rp__read__encryption__key__size.md) {

[ 891](structbt__hci__rp__read__encryption__key__size.md#a17213ccb9179739aa79c3749a2296f65) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__read__encryption__key__size.md#a17213ccb9179739aa79c3749a2296f65);

[ 892](structbt__hci__rp__read__encryption__key__size.md#af0b89b2035f956891244b10409be0f51) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__read__encryption__key__size.md#af0b89b2035f956891244b10409be0f51);

[ 893](structbt__hci__rp__read__encryption__key__size.md#af1cd71c6216b26d460c04a68405f05d5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key\_size](structbt__hci__rp__read__encryption__key__size.md#af1cd71c6216b26d460c04a68405f05d5);

894} \_\_packed;

895

896/\* BLE \*/

897

[ 898](hci__types_8h.md#aa9a3688473bf15c8845f52a3128362f7)#define BT\_HCI\_OP\_LE\_SET\_EVENT\_MASK BT\_OP(BT\_OGF\_LE, 0x0001) /\* 0x2001 \*/

[ 899](structbt__hci__cp__le__set__event__mask.md)struct [bt\_hci\_cp\_le\_set\_event\_mask](structbt__hci__cp__le__set__event__mask.md) {

[ 900](structbt__hci__cp__le__set__event__mask.md#af7de4823aca253f15e57f54ee9b3879e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [events](structbt__hci__cp__le__set__event__mask.md#af7de4823aca253f15e57f54ee9b3879e)[8];

901} \_\_packed;

902

[ 903](hci__types_8h.md#a965e30fec3f9b5956bd2ea38e57b8b00)#define BT\_HCI\_OP\_LE\_READ\_BUFFER\_SIZE BT\_OP(BT\_OGF\_LE, 0x0002) /\* 0x2002 \*/

[ 904](structbt__hci__rp__le__read__buffer__size.md)struct [bt\_hci\_rp\_le\_read\_buffer\_size](structbt__hci__rp__le__read__buffer__size.md) {

[ 905](structbt__hci__rp__le__read__buffer__size.md#a90a1206f1dbbefd298e5323ac07691f1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__buffer__size.md#a90a1206f1dbbefd298e5323ac07691f1);

[ 906](structbt__hci__rp__le__read__buffer__size.md#a8bc64cd8743984cd5a8dedfc86aaee56) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [le\_max\_len](structbt__hci__rp__le__read__buffer__size.md#a8bc64cd8743984cd5a8dedfc86aaee56);

[ 907](structbt__hci__rp__le__read__buffer__size.md#a3e393d6c51d8c3f8a5d88413198e3f28) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [le\_max\_num](structbt__hci__rp__le__read__buffer__size.md#a3e393d6c51d8c3f8a5d88413198e3f28);

908} \_\_packed;

909

[ 910](hci__types_8h.md#ae4e1d6098793b91ee0e4974886b98336)#define BT\_HCI\_OP\_LE\_READ\_LOCAL\_FEATURES BT\_OP(BT\_OGF\_LE, 0x0003) /\* 0x2003 \*/

[ 911](structbt__hci__rp__le__read__local__features.md)struct [bt\_hci\_rp\_le\_read\_local\_features](structbt__hci__rp__le__read__local__features.md) {

[ 912](structbt__hci__rp__le__read__local__features.md#ac1000822beba8a7be0dda684c0a86b6b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__local__features.md#ac1000822beba8a7be0dda684c0a86b6b);

[ 913](structbt__hci__rp__le__read__local__features.md#ada42e525338cd5526ff211c359c93b3b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [features](structbt__hci__rp__le__read__local__features.md#ada42e525338cd5526ff211c359c93b3b)[8];

914} \_\_packed;

915

[ 916](hci__types_8h.md#af34eced252d01bbc27bd8e19ed4dc80e)#define BT\_HCI\_OP\_LE\_SET\_RANDOM\_ADDRESS BT\_OP(BT\_OGF\_LE, 0x0005) /\* 0x2005 \*/

[ 917](structbt__hci__cp__le__set__random__address.md)struct [bt\_hci\_cp\_le\_set\_random\_address](structbt__hci__cp__le__set__random__address.md) {

[ 918](structbt__hci__cp__le__set__random__address.md#a919ef74473f4f86d00595ec8606789d0) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__le__set__random__address.md#a919ef74473f4f86d00595ec8606789d0);

919} \_\_packed;

920

[ 921](hci__types_8h.md#a338499e51470b8910e9f663be8f55db5)#define BT\_HCI\_ADV\_IND 0x00

[ 922](hci__types_8h.md#afaecb8d6be1b1c0ce98db7edd8bad343)#define BT\_HCI\_ADV\_DIRECT\_IND 0x01

[ 923](hci__types_8h.md#ae94df1ac3bc14f42be1207531872104a)#define BT\_HCI\_ADV\_SCAN\_IND 0x02

[ 924](hci__types_8h.md#a48e13ce185bf9612455c49484ff80bb9)#define BT\_HCI\_ADV\_NONCONN\_IND 0x03

[ 925](hci__types_8h.md#a67c1c0c5349b2de661030138185d7b0d)#define BT\_HCI\_ADV\_DIRECT\_IND\_LOW\_DUTY 0x04

[ 926](hci__types_8h.md#afb3e678c87b81f9348749f1c5721ce26)#define BT\_HCI\_ADV\_SCAN\_RSP 0x04

927

[ 928](hci__types_8h.md#ac89392b0484164812b77360d15d9984b)#define BT\_LE\_ADV\_INTERVAL\_MIN 0x0020

[ 929](hci__types_8h.md#a6479fb2c964155cfcdd3cc48c3a45618)#define BT\_LE\_ADV\_INTERVAL\_MAX 0x4000

[ 930](hci__types_8h.md#a607201e55561cdccf34e18ceac0f23b7)#define BT\_LE\_ADV\_INTERVAL\_DEFAULT 0x0800

931

[ 932](hci__types_8h.md#af9652f7d96b61e7cc9f44f3d923bd962)#define BT\_LE\_ADV\_CHAN\_MAP\_CHAN\_37 0x01

[ 933](hci__types_8h.md#a07c18344ec56b22c8a3e902bc53ba191)#define BT\_LE\_ADV\_CHAN\_MAP\_CHAN\_38 0x02

[ 934](hci__types_8h.md#a14be9af8f16dcdf70aebf251bcfb52f3)#define BT\_LE\_ADV\_CHAN\_MAP\_CHAN\_39 0x04

[ 935](hci__types_8h.md#af96bfa8c912e66233f64b7cc1844b82e)#define BT\_LE\_ADV\_CHAN\_MAP\_ALL 0x07

936

[ 937](hci__types_8h.md#abc1615c8d22ab64844c3f3394023c1b4)#define BT\_LE\_ADV\_FP\_NO\_FILTER 0x00

[ 938](hci__types_8h.md#aba027e2aeacea1040c3b45ccaeb23d3c)#define BT\_LE\_ADV\_FP\_FILTER\_SCAN\_REQ 0x01

[ 939](hci__types_8h.md#a5f3d27b78705afc3abff35e353eee9fa)#define BT\_LE\_ADV\_FP\_FILTER\_CONN\_IND 0x02

[ 940](hci__types_8h.md#a980ff7f9bf7154c7866b5e302a1f2a55)#define BT\_LE\_ADV\_FP\_FILTER\_BOTH 0x03

941

[ 942](hci__types_8h.md#a446b6e7a74800ee657f5ddcf1c198d02)#define BT\_HCI\_OP\_LE\_SET\_ADV\_PARAM BT\_OP(BT\_OGF\_LE, 0x0006) /\* 0x2006 \*/

[ 943](structbt__hci__cp__le__set__adv__param.md)struct [bt\_hci\_cp\_le\_set\_adv\_param](structbt__hci__cp__le__set__adv__param.md) {

[ 944](structbt__hci__cp__le__set__adv__param.md#a2476c2a1858eab7e9b1449c1901363c4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [min\_interval](structbt__hci__cp__le__set__adv__param.md#a2476c2a1858eab7e9b1449c1901363c4);

[ 945](structbt__hci__cp__le__set__adv__param.md#ab42c6b8f482e782d09386a3a1758903d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_interval](structbt__hci__cp__le__set__adv__param.md#ab42c6b8f482e782d09386a3a1758903d);

[ 946](structbt__hci__cp__le__set__adv__param.md#a9b09964156846fd480911dcc2d996a98) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__hci__cp__le__set__adv__param.md#a9b09964156846fd480911dcc2d996a98);

[ 947](structbt__hci__cp__le__set__adv__param.md#ad8c74cac74254354b314f07df7df1bf0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [own\_addr\_type](structbt__hci__cp__le__set__adv__param.md#ad8c74cac74254354b314f07df7df1bf0);

[ 948](structbt__hci__cp__le__set__adv__param.md#ac774ef72175e43b083d04ecac263941b) [bt\_addr\_le\_t](structbt__addr__le__t.md) [direct\_addr](structbt__hci__cp__le__set__adv__param.md#ac774ef72175e43b083d04ecac263941b);

[ 949](structbt__hci__cp__le__set__adv__param.md#a2269ae424e47adddce5aa5f2f5b84c89) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel\_map](structbt__hci__cp__le__set__adv__param.md#a2269ae424e47adddce5aa5f2f5b84c89);

[ 950](structbt__hci__cp__le__set__adv__param.md#a662c5ae81f25a897a8e597f7227a1e39) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter\_policy](structbt__hci__cp__le__set__adv__param.md#a662c5ae81f25a897a8e597f7227a1e39);

951} \_\_packed;

952

[ 953](hci__types_8h.md#afd47d6bbfd4688383aaa6b5014cf0019)#define BT\_HCI\_OP\_LE\_READ\_ADV\_CHAN\_TX\_POWER BT\_OP(BT\_OGF\_LE, 0x0007) /\* 0x2007 \*/

[ 954](structbt__hci__rp__le__read__chan__tx__power.md)struct [bt\_hci\_rp\_le\_read\_chan\_tx\_power](structbt__hci__rp__le__read__chan__tx__power.md) {

[ 955](structbt__hci__rp__le__read__chan__tx__power.md#a09a3805bccdabef399d21b29f84e3a4f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__chan__tx__power.md#a09a3805bccdabef399d21b29f84e3a4f);

[ 956](structbt__hci__rp__le__read__chan__tx__power.md#a3b6b79d1d28c3e4bf565ae364089f365) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power\_level](structbt__hci__rp__le__read__chan__tx__power.md#a3b6b79d1d28c3e4bf565ae364089f365);

957} \_\_packed;

958

[ 959](hci__types_8h.md#adb8f5236ac1b5eaa4c82d620c78c45aa)#define BT\_HCI\_OP\_LE\_SET\_ADV\_DATA BT\_OP(BT\_OGF\_LE, 0x0008) /\* 0x2008 \*/

[ 960](structbt__hci__cp__le__set__adv__data.md)struct [bt\_hci\_cp\_le\_set\_adv\_data](structbt__hci__cp__le__set__adv__data.md) {

[ 961](structbt__hci__cp__le__set__adv__data.md#a664313db17c12adb0de14371e46d26a8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structbt__hci__cp__le__set__adv__data.md#a664313db17c12adb0de14371e46d26a8);

[ 962](structbt__hci__cp__le__set__adv__data.md#a6fb8734ff5a9b77586b3e283b83985bb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__hci__cp__le__set__adv__data.md#a6fb8734ff5a9b77586b3e283b83985bb)[31];

963} \_\_packed;

964

[ 965](hci__types_8h.md#a81718bfe6796648eb5831f3cd03049c8)#define BT\_HCI\_OP\_LE\_SET\_SCAN\_RSP\_DATA BT\_OP(BT\_OGF\_LE, 0x0009) /\* 0x2009 \*/

[ 966](structbt__hci__cp__le__set__scan__rsp__data.md)struct [bt\_hci\_cp\_le\_set\_scan\_rsp\_data](structbt__hci__cp__le__set__scan__rsp__data.md) {

[ 967](structbt__hci__cp__le__set__scan__rsp__data.md#a0fe51008184419c9560bb5d8f287d8be) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structbt__hci__cp__le__set__scan__rsp__data.md#a0fe51008184419c9560bb5d8f287d8be);

[ 968](structbt__hci__cp__le__set__scan__rsp__data.md#aa719449dc2b85f094081d66398b72c7d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__hci__cp__le__set__scan__rsp__data.md#aa719449dc2b85f094081d66398b72c7d)[31];

969} \_\_packed;

970

[ 971](hci__types_8h.md#ae8361a3ca39019757304034c32391b47)#define BT\_HCI\_LE\_ADV\_DISABLE 0x00

[ 972](hci__types_8h.md#a6b8140956fbf85bd5aab2f1974b673f9)#define BT\_HCI\_LE\_ADV\_ENABLE 0x01

973

[ 974](hci__types_8h.md#a5f218883bda0698b5c52fd6a34d5e9f0)#define BT\_HCI\_OP\_LE\_SET\_ADV\_ENABLE BT\_OP(BT\_OGF\_LE, 0x000a) /\* 0x200a \*/

[ 975](structbt__hci__cp__le__set__adv__enable.md)struct [bt\_hci\_cp\_le\_set\_adv\_enable](structbt__hci__cp__le__set__adv__enable.md) {

[ 976](structbt__hci__cp__le__set__adv__enable.md#a15e92d187d586fef560adf9c793f776a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enable](structbt__hci__cp__le__set__adv__enable.md#a15e92d187d586fef560adf9c793f776a);

977} \_\_packed;

978

979/\* Scan types \*/

[ 980](hci__types_8h.md#a56db98b00b57fd713f8cedbf34e2f8fa)#define BT\_HCI\_OP\_LE\_SET\_SCAN\_PARAM BT\_OP(BT\_OGF\_LE, 0x000b) /\* 0x200b \*/

[ 981](hci__types_8h.md#a2274aacde21083e9633fe59fbff0df87)#define BT\_HCI\_LE\_SCAN\_PASSIVE 0x00

[ 982](hci__types_8h.md#ac13c2e39ac1e13cf5cd2cfa248a6f316)#define BT\_HCI\_LE\_SCAN\_ACTIVE 0x01

983

[ 984](hci__types_8h.md#a278ccd7cfefd1a46f6de843b722f583a)#define BT\_HCI\_LE\_SCAN\_FP\_BASIC\_NO\_FILTER 0x00

[ 985](hci__types_8h.md#ac6f3763ab47d20efee1af16d8d019bf3)#define BT\_HCI\_LE\_SCAN\_FP\_BASIC\_FILTER 0x01

[ 986](hci__types_8h.md#aed7fa63104bbc551bc0dbfa21e38744a)#define BT\_HCI\_LE\_SCAN\_FP\_EXT\_NO\_FILTER 0x02

[ 987](hci__types_8h.md#a45846e02e2630608b14f62f9b9020f9d)#define BT\_HCI\_LE\_SCAN\_FP\_EXT\_FILTER 0x03

988

[ 989](structbt__hci__cp__le__set__scan__param.md)struct [bt\_hci\_cp\_le\_set\_scan\_param](structbt__hci__cp__le__set__scan__param.md) {

[ 990](structbt__hci__cp__le__set__scan__param.md#ad19a479cc3c27ab24286b537b646261e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [scan\_type](structbt__hci__cp__le__set__scan__param.md#ad19a479cc3c27ab24286b537b646261e);

[ 991](structbt__hci__cp__le__set__scan__param.md#adcd8be074a8b19e0e7d02c4ea8209c93) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__hci__cp__le__set__scan__param.md#adcd8be074a8b19e0e7d02c4ea8209c93);

[ 992](structbt__hci__cp__le__set__scan__param.md#a3b5b4767092fc69a63d2219d60722407) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [window](structbt__hci__cp__le__set__scan__param.md#a3b5b4767092fc69a63d2219d60722407);

[ 993](structbt__hci__cp__le__set__scan__param.md#a694c74a6fc95f767d2e89e6596d51e98) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr\_type](structbt__hci__cp__le__set__scan__param.md#a694c74a6fc95f767d2e89e6596d51e98);

[ 994](structbt__hci__cp__le__set__scan__param.md#ab7a268e17a5d564d475ff9dee5e6e14b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter\_policy](structbt__hci__cp__le__set__scan__param.md#ab7a268e17a5d564d475ff9dee5e6e14b);

995} \_\_packed;

996

[ 997](hci__types_8h.md#a894cf6904ec16b11f6d930d72d30fce6)#define BT\_HCI\_OP\_LE\_SET\_SCAN\_ENABLE BT\_OP(BT\_OGF\_LE, 0x000c) /\* 0x200c \*/

998

[ 999](hci__types_8h.md#a152712b517c9ee0452555408d14bbfa7)#define BT\_HCI\_LE\_SCAN\_DISABLE 0x00

[ 1000](hci__types_8h.md#a6859aeda42fe72b75d5cc1896b7e6afd)#define BT\_HCI\_LE\_SCAN\_ENABLE 0x01

1001

[ 1002](hci__types_8h.md#a6fb35a340e8eecd7bc2602ed010aa6c1)#define BT\_HCI\_LE\_SCAN\_FILTER\_DUP\_DISABLE 0x00

[ 1003](hci__types_8h.md#a4c9503d4a13f78a1dc44e087af922793)#define BT\_HCI\_LE\_SCAN\_FILTER\_DUP\_ENABLE 0x01

1004

[ 1005](structbt__hci__cp__le__set__scan__enable.md)struct [bt\_hci\_cp\_le\_set\_scan\_enable](structbt__hci__cp__le__set__scan__enable.md) {

[ 1006](structbt__hci__cp__le__set__scan__enable.md#a5e429a0b11be1493515803a360932b06) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enable](structbt__hci__cp__le__set__scan__enable.md#a5e429a0b11be1493515803a360932b06);

[ 1007](structbt__hci__cp__le__set__scan__enable.md#a77b0f05c0e76681ed633bd42b3f21811) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter\_dup](structbt__hci__cp__le__set__scan__enable.md#a77b0f05c0e76681ed633bd42b3f21811);

1008} \_\_packed;

1009

[ 1010](hci__types_8h.md#aadde6f016c942c7907afddf7b6c94304)#define BT\_HCI\_OP\_LE\_CREATE\_CONN BT\_OP(BT\_OGF\_LE, 0x000d) /\* 0x200d \*/

1011

[ 1012](hci__types_8h.md#ae1bd495a90fd902614014e7e1e2f1239)#define BT\_HCI\_LE\_CREATE\_CONN\_FP\_NO\_FILTER 0x00

[ 1013](hci__types_8h.md#ac04c2c0020d2972d6df169f39c421c08)#define BT\_HCI\_LE\_CREATE\_CONN\_FP\_FILTER 0x01

1014

[ 1015](structbt__hci__cp__le__create__conn.md)struct [bt\_hci\_cp\_le\_create\_conn](structbt__hci__cp__le__create__conn.md) {

[ 1016](structbt__hci__cp__le__create__conn.md#a1a830a0f6cd961d534c338031b2b691b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [scan\_interval](structbt__hci__cp__le__create__conn.md#a1a830a0f6cd961d534c338031b2b691b);

[ 1017](structbt__hci__cp__le__create__conn.md#abf61e67f5e20adc44b5b9314ed43bccc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [scan\_window](structbt__hci__cp__le__create__conn.md#abf61e67f5e20adc44b5b9314ed43bccc);

[ 1018](structbt__hci__cp__le__create__conn.md#a2ca5063f5082a0f330676e56253a21c7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter\_policy](structbt__hci__cp__le__create__conn.md#a2ca5063f5082a0f330676e56253a21c7);

[ 1019](structbt__hci__cp__le__create__conn.md#aa51da7602eb2b44528964c8b706bb043) [bt\_addr\_le\_t](structbt__addr__le__t.md) [peer\_addr](structbt__hci__cp__le__create__conn.md#aa51da7602eb2b44528964c8b706bb043);

[ 1020](structbt__hci__cp__le__create__conn.md#a63c7f9e89528105e484a60e41eeb8a30) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [own\_addr\_type](structbt__hci__cp__le__create__conn.md#a63c7f9e89528105e484a60e41eeb8a30);

[ 1021](structbt__hci__cp__le__create__conn.md#a988cf154b0df1ff9af8d34ce73a920dd) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_interval\_min](structbt__hci__cp__le__create__conn.md#a988cf154b0df1ff9af8d34ce73a920dd);

[ 1022](structbt__hci__cp__le__create__conn.md#aa009d54866d9c675c2785412bdbd182f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_interval\_max](structbt__hci__cp__le__create__conn.md#aa009d54866d9c675c2785412bdbd182f);

[ 1023](structbt__hci__cp__le__create__conn.md#a5a9d5c1d44adac876680a517b1fad63f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_latency](structbt__hci__cp__le__create__conn.md#a5a9d5c1d44adac876680a517b1fad63f);

[ 1024](structbt__hci__cp__le__create__conn.md#ae8e0ad70a3b23ac035c237db0d57adc4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [supervision\_timeout](structbt__hci__cp__le__create__conn.md#ae8e0ad70a3b23ac035c237db0d57adc4);

[ 1025](structbt__hci__cp__le__create__conn.md#a476501ccd209f3a52082decf906ca8f0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [min\_ce\_len](structbt__hci__cp__le__create__conn.md#a476501ccd209f3a52082decf906ca8f0);

[ 1026](structbt__hci__cp__le__create__conn.md#a5b329aa8b48e03998e969b2436d35ab5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_ce\_len](structbt__hci__cp__le__create__conn.md#a5b329aa8b48e03998e969b2436d35ab5);

1027} \_\_packed;

1028

[ 1029](hci__types_8h.md#acacd0832cddc00702da74b4a36e5c825)#define BT\_HCI\_OP\_LE\_CREATE\_CONN\_CANCEL BT\_OP(BT\_OGF\_LE, 0x000e) /\* 0x200e \*/

1030

[ 1031](hci__types_8h.md#aeeba2e21bd5e33abbd48fa18f5e252f3)#define BT\_HCI\_OP\_LE\_READ\_FAL\_SIZE BT\_OP(BT\_OGF\_LE, 0x000f) /\* 0x200f \*/

[ 1032](structbt__hci__rp__le__read__fal__size.md)struct [bt\_hci\_rp\_le\_read\_fal\_size](structbt__hci__rp__le__read__fal__size.md) {

[ 1033](structbt__hci__rp__le__read__fal__size.md#aaceae885848bbdbf71241e7aa3881db5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__fal__size.md#aaceae885848bbdbf71241e7aa3881db5);

[ 1034](structbt__hci__rp__le__read__fal__size.md#ac5fcb88478c1faadf7f7ca6a9f838dde) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [fal\_size](structbt__hci__rp__le__read__fal__size.md#ac5fcb88478c1faadf7f7ca6a9f838dde);

1035} \_\_packed;

1036

[ 1037](hci__types_8h.md#a592ce45c74bdabf1b25954b8021a50bb)#define BT\_HCI\_OP\_LE\_CLEAR\_FAL BT\_OP(BT\_OGF\_LE, 0x0010) /\* 0x2010 \*/

1038

[ 1039](hci__types_8h.md#a103c6fada57c61fc3f994f8902f4123c)#define BT\_HCI\_OP\_LE\_ADD\_DEV\_TO\_FAL BT\_OP(BT\_OGF\_LE, 0x0011) /\* 0x2011 \*/

[ 1040](structbt__hci__cp__le__add__dev__to__fal.md)struct [bt\_hci\_cp\_le\_add\_dev\_to\_fal](structbt__hci__cp__le__add__dev__to__fal.md) {

[ 1041](structbt__hci__cp__le__add__dev__to__fal.md#a11ec9f3cd9b80f34094e70d8eeb13be3) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__hci__cp__le__add__dev__to__fal.md#a11ec9f3cd9b80f34094e70d8eeb13be3);

1042} \_\_packed;

1043

[ 1044](hci__types_8h.md#aedbb03b04ed567e54642e42ae758538a)#define BT\_HCI\_OP\_LE\_REM\_DEV\_FROM\_FAL BT\_OP(BT\_OGF\_LE, 0x0012) /\* 0x2012 \*/

[ 1045](structbt__hci__cp__le__rem__dev__from__fal.md)struct [bt\_hci\_cp\_le\_rem\_dev\_from\_fal](structbt__hci__cp__le__rem__dev__from__fal.md) {

[ 1046](structbt__hci__cp__le__rem__dev__from__fal.md#afe6054303093cc930d1089ca6a16101c) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__hci__cp__le__rem__dev__from__fal.md#afe6054303093cc930d1089ca6a16101c);

1047} \_\_packed;

1048

[ 1049](hci__types_8h.md#ac0c308b64ed89c9b7326982ef04ba6d3)#define BT\_HCI\_OP\_LE\_CONN\_UPDATE BT\_OP(BT\_OGF\_LE, 0x0013) /\* 0x2013 \*/

[ 1050](structhci__cp__le__conn__update.md)struct [hci\_cp\_le\_conn\_update](structhci__cp__le__conn__update.md) {

[ 1051](structhci__cp__le__conn__update.md#a5606b8795defc338b27d1a130064351e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structhci__cp__le__conn__update.md#a5606b8795defc338b27d1a130064351e);

[ 1052](structhci__cp__le__conn__update.md#adcfee3c727118069897515a00e7ead66) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_interval\_min](structhci__cp__le__conn__update.md#adcfee3c727118069897515a00e7ead66);

[ 1053](structhci__cp__le__conn__update.md#a99fc0b3b0f810f1d6e174aa9045d298a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_interval\_max](structhci__cp__le__conn__update.md#a99fc0b3b0f810f1d6e174aa9045d298a);

[ 1054](structhci__cp__le__conn__update.md#a8e48e5e195aea7f581cfc7246da79d72) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_latency](structhci__cp__le__conn__update.md#a8e48e5e195aea7f581cfc7246da79d72);

[ 1055](structhci__cp__le__conn__update.md#ab76ecdf6f7e5a5bb581cbd26f67d8f9f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [supervision\_timeout](structhci__cp__le__conn__update.md#ab76ecdf6f7e5a5bb581cbd26f67d8f9f);

[ 1056](structhci__cp__le__conn__update.md#a3ae86fccacf462463fe520eb1e06fa62) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [min\_ce\_len](structhci__cp__le__conn__update.md#a3ae86fccacf462463fe520eb1e06fa62);

[ 1057](structhci__cp__le__conn__update.md#a401169ccc5dbf6cf0abd6154738f00dc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_ce\_len](structhci__cp__le__conn__update.md#a401169ccc5dbf6cf0abd6154738f00dc);

1058} \_\_packed;

1059

[ 1060](hci__types_8h.md#a6224aab014342d93bcb16c717cd52421)#define BT\_HCI\_OP\_LE\_SET\_HOST\_CHAN\_CLASSIF BT\_OP(BT\_OGF\_LE, 0x0014) /\* 0x2014 \*/

[ 1061](structbt__hci__cp__le__set__host__chan__classif.md)struct [bt\_hci\_cp\_le\_set\_host\_chan\_classif](structbt__hci__cp__le__set__host__chan__classif.md) {

[ 1062](structbt__hci__cp__le__set__host__chan__classif.md#a0fb81bcdebe7da416cc4317486106752) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ch\_map](structbt__hci__cp__le__set__host__chan__classif.md#a0fb81bcdebe7da416cc4317486106752)[5];

1063} \_\_packed;

1064

[ 1065](hci__types_8h.md#a9040e4b5e719d53cc324faa280a670a4)#define BT\_HCI\_OP\_LE\_READ\_CHAN\_MAP BT\_OP(BT\_OGF\_LE, 0x0015) /\* 0x2015 \*/

[ 1066](structbt__hci__cp__le__read__chan__map.md)struct [bt\_hci\_cp\_le\_read\_chan\_map](structbt__hci__cp__le__read__chan__map.md) {

[ 1067](structbt__hci__cp__le__read__chan__map.md#abea9aec016a0433b3e4837d53d6b5d2b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__read__chan__map.md#abea9aec016a0433b3e4837d53d6b5d2b);

1068} \_\_packed;

[ 1069](structbt__hci__rp__le__read__chan__map.md)struct [bt\_hci\_rp\_le\_read\_chan\_map](structbt__hci__rp__le__read__chan__map.md) {

[ 1070](structbt__hci__rp__le__read__chan__map.md#a73a51f243bf4881f9024ba67cf2426ad) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__chan__map.md#a73a51f243bf4881f9024ba67cf2426ad);

[ 1071](structbt__hci__rp__le__read__chan__map.md#a8fcec46574f5601bf0837aae8f745b38) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__read__chan__map.md#a8fcec46574f5601bf0837aae8f745b38);

[ 1072](structbt__hci__rp__le__read__chan__map.md#a2899c53f17ba2293b95477ba25fd1b3d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ch\_map](structbt__hci__rp__le__read__chan__map.md#a2899c53f17ba2293b95477ba25fd1b3d)[5];

1073} \_\_packed;

1074

[ 1075](hci__types_8h.md#ac8d5165a3a5d190b8e2d31feb79a17c9)#define BT\_HCI\_OP\_LE\_READ\_REMOTE\_FEATURES BT\_OP(BT\_OGF\_LE, 0x0016) /\* 0x2016 \*/

[ 1076](structbt__hci__cp__le__read__remote__features.md)struct [bt\_hci\_cp\_le\_read\_remote\_features](structbt__hci__cp__le__read__remote__features.md) {

[ 1077](structbt__hci__cp__le__read__remote__features.md#a843997555fd36f102c83a7d59f65eea9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__read__remote__features.md#a843997555fd36f102c83a7d59f65eea9);

1078} \_\_packed;

1079

[ 1080](hci__types_8h.md#a99fdd1dbff627a2f627e7d9eced68326)#define BT\_HCI\_OP\_LE\_ENCRYPT BT\_OP(BT\_OGF\_LE, 0x0017) /\* 0x2017 \*/

[ 1081](structbt__hci__cp__le__encrypt.md)struct [bt\_hci\_cp\_le\_encrypt](structbt__hci__cp__le__encrypt.md) {

[ 1082](structbt__hci__cp__le__encrypt.md#ab64f1bab8ad3a98217db96e6765a7d24) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key](structbt__hci__cp__le__encrypt.md#ab64f1bab8ad3a98217db96e6765a7d24)[16];

[ 1083](structbt__hci__cp__le__encrypt.md#ad520b84e6e2a4e62f7fefba248c4cf10) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [plaintext](structbt__hci__cp__le__encrypt.md#ad520b84e6e2a4e62f7fefba248c4cf10)[16];

1084} \_\_packed;

[ 1085](structbt__hci__rp__le__encrypt.md)struct [bt\_hci\_rp\_le\_encrypt](structbt__hci__rp__le__encrypt.md) {

[ 1086](structbt__hci__rp__le__encrypt.md#aee480917cc6af7dea77717a9cb5840bb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__encrypt.md#aee480917cc6af7dea77717a9cb5840bb);

[ 1087](structbt__hci__rp__le__encrypt.md#ac20cd9f4ceffea6999114f65437aefdc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enc\_data](structbt__hci__rp__le__encrypt.md#ac20cd9f4ceffea6999114f65437aefdc)[16];

1088} \_\_packed;

1089

[ 1090](hci__types_8h.md#ac3af817deaf472dbb2a825fd57b67f42)#define BT\_HCI\_OP\_LE\_RAND BT\_OP(BT\_OGF\_LE, 0x0018) /\* 0x2018 \*/

[ 1091](structbt__hci__rp__le__rand.md)struct [bt\_hci\_rp\_le\_rand](structbt__hci__rp__le__rand.md) {

[ 1092](structbt__hci__rp__le__rand.md#a73320168836caa3caf724282402e80de) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__rand.md#a73320168836caa3caf724282402e80de);

[ 1093](structbt__hci__rp__le__rand.md#a3f706af9d2baf9e2b199242a28cec9e5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rand](structbt__hci__rp__le__rand.md#a3f706af9d2baf9e2b199242a28cec9e5)[8];

1094} \_\_packed;

1095

[ 1096](hci__types_8h.md#afececfce5819f1b8555ce47fbde2aa0b)#define BT\_HCI\_OP\_LE\_START\_ENCRYPTION BT\_OP(BT\_OGF\_LE, 0x0019) /\* 0x2019 \*/

[ 1097](structbt__hci__cp__le__start__encryption.md)struct [bt\_hci\_cp\_le\_start\_encryption](structbt__hci__cp__le__start__encryption.md) {

[ 1098](structbt__hci__cp__le__start__encryption.md#a4ac6d63f336e36a347242153aced4c71) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__start__encryption.md#a4ac6d63f336e36a347242153aced4c71);

[ 1099](structbt__hci__cp__le__start__encryption.md#ade8ae824dc5d85671971a3baafee8f54) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [rand](structbt__hci__cp__le__start__encryption.md#ade8ae824dc5d85671971a3baafee8f54);

[ 1100](structbt__hci__cp__le__start__encryption.md#a640d201bbfa6f6d8476be02d3656e847) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [ediv](structbt__hci__cp__le__start__encryption.md#a640d201bbfa6f6d8476be02d3656e847);

[ 1101](structbt__hci__cp__le__start__encryption.md#a99d2dd719ce38976e9da8a73f26839a1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ltk](structbt__hci__cp__le__start__encryption.md#a99d2dd719ce38976e9da8a73f26839a1)[16];

1102} \_\_packed;

1103

[ 1104](hci__types_8h.md#a92050425248585bd1c3873e8593db362)#define BT\_HCI\_OP\_LE\_LTK\_REQ\_REPLY BT\_OP(BT\_OGF\_LE, 0x001a) /\* 0x201a \*/

[ 1105](structbt__hci__cp__le__ltk__req__reply.md)struct [bt\_hci\_cp\_le\_ltk\_req\_reply](structbt__hci__cp__le__ltk__req__reply.md) {

[ 1106](structbt__hci__cp__le__ltk__req__reply.md#a46d87451acc1f1ce2ff35dd0dd238db3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__ltk__req__reply.md#a46d87451acc1f1ce2ff35dd0dd238db3);

[ 1107](structbt__hci__cp__le__ltk__req__reply.md#a2d16b44af344237a890341943c4a6582) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ltk](structbt__hci__cp__le__ltk__req__reply.md#a2d16b44af344237a890341943c4a6582)[16];

1108} \_\_packed;

[ 1109](structbt__hci__rp__le__ltk__req__reply.md)struct [bt\_hci\_rp\_le\_ltk\_req\_reply](structbt__hci__rp__le__ltk__req__reply.md) {

[ 1110](structbt__hci__rp__le__ltk__req__reply.md#a831950bab8994f36c96c543310400752) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__ltk__req__reply.md#a831950bab8994f36c96c543310400752);

[ 1111](structbt__hci__rp__le__ltk__req__reply.md#a2dfe012e641e5d8bd6c0f2e15e5a54c2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__ltk__req__reply.md#a2dfe012e641e5d8bd6c0f2e15e5a54c2);

1112} \_\_packed;

1113

[ 1114](hci__types_8h.md#ae04bd3c7ff17142f2b47e24accdf6a20)#define BT\_HCI\_OP\_LE\_LTK\_REQ\_NEG\_REPLY BT\_OP(BT\_OGF\_LE, 0x001b) /\* 0x201b \*/

[ 1115](structbt__hci__cp__le__ltk__req__neg__reply.md)struct [bt\_hci\_cp\_le\_ltk\_req\_neg\_reply](structbt__hci__cp__le__ltk__req__neg__reply.md) {

[ 1116](structbt__hci__cp__le__ltk__req__neg__reply.md#add8cc3b13432e233ceb5c2c11e0107c0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__ltk__req__neg__reply.md#add8cc3b13432e233ceb5c2c11e0107c0);

1117} \_\_packed;

[ 1118](structbt__hci__rp__le__ltk__req__neg__reply.md)struct [bt\_hci\_rp\_le\_ltk\_req\_neg\_reply](structbt__hci__rp__le__ltk__req__neg__reply.md) {

[ 1119](structbt__hci__rp__le__ltk__req__neg__reply.md#a92306e47450b239233a3f39c645eaa4e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__ltk__req__neg__reply.md#a92306e47450b239233a3f39c645eaa4e);

[ 1120](structbt__hci__rp__le__ltk__req__neg__reply.md#ad0f4f9300d9a8b737b41211972151017) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__ltk__req__neg__reply.md#ad0f4f9300d9a8b737b41211972151017);

1121} \_\_packed;

1122

[ 1123](hci__types_8h.md#a286869ebde03594d56ecd8bc1aa7c73c)#define BT\_HCI\_OP\_LE\_READ\_SUPP\_STATES BT\_OP(BT\_OGF\_LE, 0x001c) /\* 0x201c \*/

[ 1124](structbt__hci__rp__le__read__supp__states.md)struct [bt\_hci\_rp\_le\_read\_supp\_states](structbt__hci__rp__le__read__supp__states.md) {

[ 1125](structbt__hci__rp__le__read__supp__states.md#aeed0cc41ee521c27f07d8cbf4b377a4f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__supp__states.md#aeed0cc41ee521c27f07d8cbf4b377a4f);

[ 1126](structbt__hci__rp__le__read__supp__states.md#a9b60476cc158a701b29b28bd21375130) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [le\_states](structbt__hci__rp__le__read__supp__states.md#a9b60476cc158a701b29b28bd21375130)[8];

1127} \_\_packed;

1128

[ 1129](hci__types_8h.md#abd18c6854a0dc97c451b498816f206e4)#define BT\_HCI\_OP\_LE\_RX\_TEST BT\_OP(BT\_OGF\_LE, 0x001d) /\* 0x201d \*/

[ 1130](structbt__hci__cp__le__rx__test.md)struct [bt\_hci\_cp\_le\_rx\_test](structbt__hci__cp__le__rx__test.md) {

[ 1131](structbt__hci__cp__le__rx__test.md#a11cb21a7625d9c097eba0a7b68e93f3f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_ch](structbt__hci__cp__le__rx__test.md#a11cb21a7625d9c097eba0a7b68e93f3f);

1132} \_\_packed;

1133

[ 1134](hci__types_8h.md#aa9ce0f2db7b63303a9c61c37d052d7b7)#define BT\_HCI\_TEST\_PKT\_PAYLOAD\_PRBS9 0x00

[ 1135](hci__types_8h.md#a51d26730c8f4c3c8491b33483bdb9494)#define BT\_HCI\_TEST\_PKT\_PAYLOAD\_11110000 0x01

[ 1136](hci__types_8h.md#aab044752b89bb4493a509580ae8eaf9b)#define BT\_HCI\_TEST\_PKT\_PAYLOAD\_10101010 0x02

[ 1137](hci__types_8h.md#a0eb4fcbb3ab6c7d4e2ed87d61c5b30f1)#define BT\_HCI\_TEST\_PKT\_PAYLOAD\_PRBS15 0x03

[ 1138](hci__types_8h.md#a5008205909cecc994b74c8a1cb1f92af)#define BT\_HCI\_TEST\_PKT\_PAYLOAD\_11111111 0x04

[ 1139](hci__types_8h.md#a1fe8c26f174833a4dccbe192df2c6f7d)#define BT\_HCI\_TEST\_PKT\_PAYLOAD\_00000000 0x05

[ 1140](hci__types_8h.md#a13baca9e4517522c763c25882177a2a7)#define BT\_HCI\_TEST\_PKT\_PAYLOAD\_00001111 0x06

[ 1141](hci__types_8h.md#a8f660f979b14d91abd9423e718921ebb)#define BT\_HCI\_TEST\_PKT\_PAYLOAD\_01010101 0x07

1142

[ 1143](hci__types_8h.md#af5fe87cbe280dcf26ddc21952e84e93e)#define BT\_HCI\_OP\_LE\_TX\_TEST BT\_OP(BT\_OGF\_LE, 0x001e) /\* 0x201e \*/

[ 1144](structbt__hci__cp__le__tx__test.md)struct [bt\_hci\_cp\_le\_tx\_test](structbt__hci__cp__le__tx__test.md) {

[ 1145](structbt__hci__cp__le__tx__test.md#aae634b277125066ecbc36d119bc4244f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_ch](structbt__hci__cp__le__tx__test.md#aae634b277125066ecbc36d119bc4244f);

[ 1146](structbt__hci__cp__le__tx__test.md#a55c5f1621a51da03500910fc9664df54) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [test\_data\_len](structbt__hci__cp__le__tx__test.md#a55c5f1621a51da03500910fc9664df54);

[ 1147](structbt__hci__cp__le__tx__test.md#ad93908905d370842f16e16cc45280495) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pkt\_payload](structbt__hci__cp__le__tx__test.md#ad93908905d370842f16e16cc45280495);

1148} \_\_packed;

1149

[ 1150](hci__types_8h.md#a7ff8a81ae09ddb0d18f999fe454e41df)#define BT\_HCI\_OP\_LE\_TEST\_END BT\_OP(BT\_OGF\_LE, 0x001f) /\* 0x201f \*/

[ 1151](structbt__hci__rp__le__test__end.md)struct [bt\_hci\_rp\_le\_test\_end](structbt__hci__rp__le__test__end.md) {

[ 1152](structbt__hci__rp__le__test__end.md#a2ac412ef9a5fc7651315afe042856cce) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__test__end.md#a2ac412ef9a5fc7651315afe042856cce);

[ 1153](structbt__hci__rp__le__test__end.md#a9e283118e4ea48b0df66a4cd1c1cf9a1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [rx\_pkt\_count](structbt__hci__rp__le__test__end.md#a9e283118e4ea48b0df66a4cd1c1cf9a1);

1154} \_\_packed;

1155

[ 1156](hci__types_8h.md#a8b824639d31fa9f579e73cf1f1344c85)#define BT\_HCI\_OP\_LE\_CONN\_PARAM\_REQ\_REPLY BT\_OP(BT\_OGF\_LE, 0x0020) /\* 0x2020 \*/

[ 1157](structbt__hci__cp__le__conn__param__req__reply.md)struct [bt\_hci\_cp\_le\_conn\_param\_req\_reply](structbt__hci__cp__le__conn__param__req__reply.md) {

[ 1158](structbt__hci__cp__le__conn__param__req__reply.md#aa3b938afe13d4e05806fb6cdfab5cb14) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__conn__param__req__reply.md#aa3b938afe13d4e05806fb6cdfab5cb14);

[ 1159](structbt__hci__cp__le__conn__param__req__reply.md#a10547c7d4836980947d17bbde0d75a51) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval\_min](structbt__hci__cp__le__conn__param__req__reply.md#a10547c7d4836980947d17bbde0d75a51);

[ 1160](structbt__hci__cp__le__conn__param__req__reply.md#aed58f9aa722a284ae39df842394c06cf) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval\_max](structbt__hci__cp__le__conn__param__req__reply.md#aed58f9aa722a284ae39df842394c06cf);

[ 1161](structbt__hci__cp__le__conn__param__req__reply.md#a8c76816cc230387c249ab8e05c402964) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [latency](structbt__hci__cp__le__conn__param__req__reply.md#a8c76816cc230387c249ab8e05c402964);

[ 1162](structbt__hci__cp__le__conn__param__req__reply.md#af25a3f226ceccbe19e7f1482ed5f141e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structbt__hci__cp__le__conn__param__req__reply.md#af25a3f226ceccbe19e7f1482ed5f141e);

[ 1163](structbt__hci__cp__le__conn__param__req__reply.md#a512d605d5c4aacf81b78794fcf260abf) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [min\_ce\_len](structbt__hci__cp__le__conn__param__req__reply.md#a512d605d5c4aacf81b78794fcf260abf);

[ 1164](structbt__hci__cp__le__conn__param__req__reply.md#a932e6a3a45ec0409656325f7246d5d7e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_ce\_len](structbt__hci__cp__le__conn__param__req__reply.md#a932e6a3a45ec0409656325f7246d5d7e);

1165} \_\_packed;

[ 1166](structbt__hci__rp__le__conn__param__req__reply.md)struct [bt\_hci\_rp\_le\_conn\_param\_req\_reply](structbt__hci__rp__le__conn__param__req__reply.md) {

[ 1167](structbt__hci__rp__le__conn__param__req__reply.md#a2f0a9f5b087d1f12c100ef4521e015ff) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__conn__param__req__reply.md#a2f0a9f5b087d1f12c100ef4521e015ff);

[ 1168](structbt__hci__rp__le__conn__param__req__reply.md#a3e598cd87d5298a1cc62ac79a4f34a6e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__conn__param__req__reply.md#a3e598cd87d5298a1cc62ac79a4f34a6e);

1169} \_\_packed;

1170

[ 1171](hci__types_8h.md#a1fbca6b816791f1967278224f37782c1)#define BT\_HCI\_OP\_LE\_CONN\_PARAM\_REQ\_NEG\_REPLY BT\_OP(BT\_OGF\_LE, 0x0021) /\* 0x2021 \*/

[ 1172](structbt__hci__cp__le__conn__param__req__neg__reply.md)struct [bt\_hci\_cp\_le\_conn\_param\_req\_neg\_reply](structbt__hci__cp__le__conn__param__req__neg__reply.md) {

[ 1173](structbt__hci__cp__le__conn__param__req__neg__reply.md#a0040e4a50c5c5479b539eb0bafb7b305) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__conn__param__req__neg__reply.md#a0040e4a50c5c5479b539eb0bafb7b305);

[ 1174](structbt__hci__cp__le__conn__param__req__neg__reply.md#a8c283ac844805224b1ffeb9801e8b14b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reason](structbt__hci__cp__le__conn__param__req__neg__reply.md#a8c283ac844805224b1ffeb9801e8b14b);

1175} \_\_packed;

[ 1176](structbt__hci__rp__le__conn__param__req__neg__reply.md)struct [bt\_hci\_rp\_le\_conn\_param\_req\_neg\_reply](structbt__hci__rp__le__conn__param__req__neg__reply.md) {

[ 1177](structbt__hci__rp__le__conn__param__req__neg__reply.md#a3804e64f9e8693e3e5899067212f6873) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__conn__param__req__neg__reply.md#a3804e64f9e8693e3e5899067212f6873);

[ 1178](structbt__hci__rp__le__conn__param__req__neg__reply.md#ac88f44127c0a1b9b191a27cc003c1052) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__conn__param__req__neg__reply.md#ac88f44127c0a1b9b191a27cc003c1052);

1179} \_\_packed;

1180

[ 1181](hci__types_8h.md#a5aeb49334449851866537ea8703f5ab0)#define BT\_HCI\_OP\_LE\_SET\_DATA\_LEN BT\_OP(BT\_OGF\_LE, 0x0022) /\* 0x2022 \*/

[ 1182](structbt__hci__cp__le__set__data__len.md)struct [bt\_hci\_cp\_le\_set\_data\_len](structbt__hci__cp__le__set__data__len.md) {

[ 1183](structbt__hci__cp__le__set__data__len.md#a874869090428a7f380c5466353573eba) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__set__data__len.md#a874869090428a7f380c5466353573eba);

[ 1184](structbt__hci__cp__le__set__data__len.md#ac579e84a004a09813bbe0ed61db11931) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [tx\_octets](structbt__hci__cp__le__set__data__len.md#ac579e84a004a09813bbe0ed61db11931);

[ 1185](structbt__hci__cp__le__set__data__len.md#a15285a4e8bf8e359bb326de4b30ba8f1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [tx\_time](structbt__hci__cp__le__set__data__len.md#a15285a4e8bf8e359bb326de4b30ba8f1);

1186} \_\_packed;

[ 1187](structbt__hci__rp__le__set__data__len.md)struct [bt\_hci\_rp\_le\_set\_data\_len](structbt__hci__rp__le__set__data__len.md) {

[ 1188](structbt__hci__rp__le__set__data__len.md#a8667db355a95691d58845f89e919aea4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__set__data__len.md#a8667db355a95691d58845f89e919aea4);

[ 1189](structbt__hci__rp__le__set__data__len.md#a207c6da11e0bb145bed7a9e551ddc608) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__set__data__len.md#a207c6da11e0bb145bed7a9e551ddc608);

1190} \_\_packed;

1191

[ 1192](hci__types_8h.md#aa58d9ce08e0f1d4a3e5a2f2b1733a6d2)#define BT\_HCI\_OP\_LE\_READ\_DEFAULT\_DATA\_LEN BT\_OP(BT\_OGF\_LE, 0x0023) /\* 0x2023 \*/

[ 1193](structbt__hci__rp__le__read__default__data__len.md)struct [bt\_hci\_rp\_le\_read\_default\_data\_len](structbt__hci__rp__le__read__default__data__len.md) {

[ 1194](structbt__hci__rp__le__read__default__data__len.md#a62d735826ad3ca5d4bea7d0fb87dea7e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__default__data__len.md#a62d735826ad3ca5d4bea7d0fb87dea7e);

[ 1195](structbt__hci__rp__le__read__default__data__len.md#a1ec4ba1c0286132e87fcffeb988a37f9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_tx\_octets](structbt__hci__rp__le__read__default__data__len.md#a1ec4ba1c0286132e87fcffeb988a37f9);

[ 1196](structbt__hci__rp__le__read__default__data__len.md#ae193eab40c2afa55b78a1906e6a26f26) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_tx\_time](structbt__hci__rp__le__read__default__data__len.md#ae193eab40c2afa55b78a1906e6a26f26);

1197} \_\_packed;

1198

[ 1199](hci__types_8h.md#ae344c1ab9af250787b9ed8109ad3cde0)#define BT\_HCI\_OP\_LE\_WRITE\_DEFAULT\_DATA\_LEN BT\_OP(BT\_OGF\_LE, 0x0024) /\* 0x2024 \*/

[ 1200](structbt__hci__cp__le__write__default__data__len.md)struct [bt\_hci\_cp\_le\_write\_default\_data\_len](structbt__hci__cp__le__write__default__data__len.md) {

[ 1201](structbt__hci__cp__le__write__default__data__len.md#a0ffb8c52d9031dfe448eac0943a4a49c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_tx\_octets](structbt__hci__cp__le__write__default__data__len.md#a0ffb8c52d9031dfe448eac0943a4a49c);

[ 1202](structbt__hci__cp__le__write__default__data__len.md#a2ada0ea5ee8ac8e6d59fc6adc18421b8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_tx\_time](structbt__hci__cp__le__write__default__data__len.md#a2ada0ea5ee8ac8e6d59fc6adc18421b8);

1203} \_\_packed;

1204

[ 1205](hci__types_8h.md#ab1ff230560c1f7712e23a22eb44f0e69)#define BT\_HCI\_OP\_LE\_P256\_PUBLIC\_KEY BT\_OP(BT\_OGF\_LE, 0x0025) /\* 0x2025 \*/

1206

[ 1207](hci__types_8h.md#af2625fcbc0f29199f1a95dc9fe0f929d)#define BT\_HCI\_OP\_LE\_GENERATE\_DHKEY BT\_OP(BT\_OGF\_LE, 0x0026) /\* 0x2026 \*/

[ 1208](structbt__hci__cp__le__generate__dhkey.md)struct [bt\_hci\_cp\_le\_generate\_dhkey](structbt__hci__cp__le__generate__dhkey.md) {

[ 1209](structbt__hci__cp__le__generate__dhkey.md#a0f67195504d877a1d11b7dfb77d09fcc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key](structbt__hci__cp__le__generate__dhkey.md#a0f67195504d877a1d11b7dfb77d09fcc)[64];

1210} \_\_packed;

1211

1212

[ 1213](hci__types_8h.md#aa7bf82632c6df22096210de18902a465)#define BT\_HCI\_OP\_LE\_GENERATE\_DHKEY\_V2 BT\_OP(BT\_OGF\_LE, 0x005e) /\* 0x205e \*/

1214

[ 1215](hci__types_8h.md#ac85ab1283cd175fc575ebd98b52b3335)#define BT\_HCI\_LE\_KEY\_TYPE\_GENERATED 0x00

[ 1216](hci__types_8h.md#a71f16c552b14042c00e98ea20c1e03c4)#define BT\_HCI\_LE\_KEY\_TYPE\_DEBUG 0x01

1217

[ 1218](structbt__hci__cp__le__generate__dhkey__v2.md)struct [bt\_hci\_cp\_le\_generate\_dhkey\_v2](structbt__hci__cp__le__generate__dhkey__v2.md) {

[ 1219](structbt__hci__cp__le__generate__dhkey__v2.md#acc3007adf301674b9e847297007c3cd1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key](structbt__hci__cp__le__generate__dhkey__v2.md#acc3007adf301674b9e847297007c3cd1)[64];

[ 1220](structbt__hci__cp__le__generate__dhkey__v2.md#a3d47ad6d9df4d4023d2586c915ee8f2c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key\_type](structbt__hci__cp__le__generate__dhkey__v2.md#a3d47ad6d9df4d4023d2586c915ee8f2c);

1221} \_\_packed;

1222

1223

[ 1224](hci__types_8h.md#a735c643e8afa27c4e7f7be9bfb09676a)#define BT\_HCI\_OP\_LE\_ADD\_DEV\_TO\_RL BT\_OP(BT\_OGF\_LE, 0x0027) /\* 0x2027 \*/

[ 1225](structbt__hci__cp__le__add__dev__to__rl.md)struct [bt\_hci\_cp\_le\_add\_dev\_to\_rl](structbt__hci__cp__le__add__dev__to__rl.md) {

[ 1226](structbt__hci__cp__le__add__dev__to__rl.md#a3daf2041f04381a56c2cbcd4bb33f4c0) [bt\_addr\_le\_t](structbt__addr__le__t.md) [peer\_id\_addr](structbt__hci__cp__le__add__dev__to__rl.md#a3daf2041f04381a56c2cbcd4bb33f4c0);

[ 1227](structbt__hci__cp__le__add__dev__to__rl.md#aedc27c868a7a4cbd3c175f67db4e3242) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [peer\_irk](structbt__hci__cp__le__add__dev__to__rl.md#aedc27c868a7a4cbd3c175f67db4e3242)[16];

[ 1228](structbt__hci__cp__le__add__dev__to__rl.md#ab5caa38e6eeab09b4a69084b1890317b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [local\_irk](structbt__hci__cp__le__add__dev__to__rl.md#ab5caa38e6eeab09b4a69084b1890317b)[16];

1229} \_\_packed;

1230

[ 1231](hci__types_8h.md#ac4c11605a4cd244ec3ffa972295396fa)#define BT\_HCI\_OP\_LE\_REM\_DEV\_FROM\_RL BT\_OP(BT\_OGF\_LE, 0x0028) /\* 0x2028 \*/

[ 1232](structbt__hci__cp__le__rem__dev__from__rl.md)struct [bt\_hci\_cp\_le\_rem\_dev\_from\_rl](structbt__hci__cp__le__rem__dev__from__rl.md) {

[ 1233](structbt__hci__cp__le__rem__dev__from__rl.md#aacb577a7ae13322145fccdffc3161541) [bt\_addr\_le\_t](structbt__addr__le__t.md) [peer\_id\_addr](structbt__hci__cp__le__rem__dev__from__rl.md#aacb577a7ae13322145fccdffc3161541);

1234} \_\_packed;

1235

[ 1236](hci__types_8h.md#a5efab85a3beac1fe3fc5a5294a2b1079)#define BT\_HCI\_OP\_LE\_CLEAR\_RL BT\_OP(BT\_OGF\_LE, 0x0029) /\* 0x2029 \*/

1237

[ 1238](hci__types_8h.md#a45b38708e807c784bd734ba1f69c7f86)#define BT\_HCI\_OP\_LE\_READ\_RL\_SIZE BT\_OP(BT\_OGF\_LE, 0x002a) /\* 0x202a \*/

[ 1239](structbt__hci__rp__le__read__rl__size.md)struct [bt\_hci\_rp\_le\_read\_rl\_size](structbt__hci__rp__le__read__rl__size.md) {

[ 1240](structbt__hci__rp__le__read__rl__size.md#af8a10aab21d54cce3529b1307769f6c6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__rl__size.md#af8a10aab21d54cce3529b1307769f6c6);

[ 1241](structbt__hci__rp__le__read__rl__size.md#a90c28070ee094c99c21c4dd229ff6ce5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rl\_size](structbt__hci__rp__le__read__rl__size.md#a90c28070ee094c99c21c4dd229ff6ce5);

1242} \_\_packed;

1243

[ 1244](hci__types_8h.md#a6c605e63bd1633f3423a915cf4db00e8)#define BT\_HCI\_OP\_LE\_READ\_PEER\_RPA BT\_OP(BT\_OGF\_LE, 0x002b) /\* 0x202b \*/

[ 1245](structbt__hci__cp__le__read__peer__rpa.md)struct [bt\_hci\_cp\_le\_read\_peer\_rpa](structbt__hci__cp__le__read__peer__rpa.md) {

[ 1246](structbt__hci__cp__le__read__peer__rpa.md#ab0c70a1dbe5152b1fc926b90ec3387b3) [bt\_addr\_le\_t](structbt__addr__le__t.md) [peer\_id\_addr](structbt__hci__cp__le__read__peer__rpa.md#ab0c70a1dbe5152b1fc926b90ec3387b3);

1247} \_\_packed;

[ 1248](structbt__hci__rp__le__read__peer__rpa.md)struct [bt\_hci\_rp\_le\_read\_peer\_rpa](structbt__hci__rp__le__read__peer__rpa.md) {

[ 1249](structbt__hci__rp__le__read__peer__rpa.md#a9c8c799e8c9fbb9f64865e55cdb1f9ef) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__peer__rpa.md#a9c8c799e8c9fbb9f64865e55cdb1f9ef);

[ 1250](structbt__hci__rp__le__read__peer__rpa.md#a4eeee179819865ba5d5171d9bd33e5e9) [bt\_addr\_t](structbt__addr__t.md) [peer\_rpa](structbt__hci__rp__le__read__peer__rpa.md#a4eeee179819865ba5d5171d9bd33e5e9);

1251} \_\_packed;

1252

[ 1253](hci__types_8h.md#af8ec9d3b6889a8530bc5977b8594fea6)#define BT\_HCI\_OP\_LE\_READ\_LOCAL\_RPA BT\_OP(BT\_OGF\_LE, 0x002c) /\* 0x202c \*/

[ 1254](structbt__hci__cp__le__read__local__rpa.md)struct [bt\_hci\_cp\_le\_read\_local\_rpa](structbt__hci__cp__le__read__local__rpa.md) {

[ 1255](structbt__hci__cp__le__read__local__rpa.md#aa96cd60066003e4a7a1f482fb81557f8) [bt\_addr\_le\_t](structbt__addr__le__t.md) [peer\_id\_addr](structbt__hci__cp__le__read__local__rpa.md#aa96cd60066003e4a7a1f482fb81557f8);

1256} \_\_packed;

[ 1257](structbt__hci__rp__le__read__local__rpa.md)struct [bt\_hci\_rp\_le\_read\_local\_rpa](structbt__hci__rp__le__read__local__rpa.md) {

[ 1258](structbt__hci__rp__le__read__local__rpa.md#a55b1ac66c986c0a7879b144163064be2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__local__rpa.md#a55b1ac66c986c0a7879b144163064be2);

[ 1259](structbt__hci__rp__le__read__local__rpa.md#a5b27c5b02cb290452be62c22772fbc53) [bt\_addr\_t](structbt__addr__t.md) [local\_rpa](structbt__hci__rp__le__read__local__rpa.md#a5b27c5b02cb290452be62c22772fbc53);

1260} \_\_packed;

1261

[ 1262](hci__types_8h.md#a017742ee92c9ed7b80b41f339394f1e4)#define BT\_HCI\_ADDR\_RES\_DISABLE 0x00

[ 1263](hci__types_8h.md#a61e677658b5a730b13869ebc0dbbffbe)#define BT\_HCI\_ADDR\_RES\_ENABLE 0x01

1264

[ 1265](hci__types_8h.md#a183431c86b7eb32b7c00e6b3a000f29e)#define BT\_HCI\_OP\_LE\_SET\_ADDR\_RES\_ENABLE BT\_OP(BT\_OGF\_LE, 0x002d) /\* 0x202d \*/

[ 1266](structbt__hci__cp__le__set__addr__res__enable.md)struct [bt\_hci\_cp\_le\_set\_addr\_res\_enable](structbt__hci__cp__le__set__addr__res__enable.md) {

[ 1267](structbt__hci__cp__le__set__addr__res__enable.md#ad0548178cbc9bc2db54612a748a2bd65) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enable](structbt__hci__cp__le__set__addr__res__enable.md#ad0548178cbc9bc2db54612a748a2bd65);

1268} \_\_packed;

1269

[ 1270](hci__types_8h.md#aeabb8438460e694867d855cf7f8e3b31)#define BT\_HCI\_OP\_LE\_SET\_RPA\_TIMEOUT BT\_OP(BT\_OGF\_LE, 0x002e) /\* 0x202e \*/

[ 1271](structbt__hci__cp__le__set__rpa__timeout.md)struct [bt\_hci\_cp\_le\_set\_rpa\_timeout](structbt__hci__cp__le__set__rpa__timeout.md) {

[ 1272](structbt__hci__cp__le__set__rpa__timeout.md#a6b1befe9d2131a889de17339ec1941fa) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [rpa\_timeout](structbt__hci__cp__le__set__rpa__timeout.md#a6b1befe9d2131a889de17339ec1941fa);

1273} \_\_packed;

1274

[ 1275](hci__types_8h.md#aafb5872650d77d9f4c6ae43038ef2bf1)#define BT\_HCI\_OP\_LE\_READ\_MAX\_DATA\_LEN BT\_OP(BT\_OGF\_LE, 0x002f) /\* 0x202f \*/

[ 1276](structbt__hci__rp__le__read__max__data__len.md)struct [bt\_hci\_rp\_le\_read\_max\_data\_len](structbt__hci__rp__le__read__max__data__len.md) {

[ 1277](structbt__hci__rp__le__read__max__data__len.md#a654b34b1ee038bf442550a340a26070c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__max__data__len.md#a654b34b1ee038bf442550a340a26070c);

[ 1278](structbt__hci__rp__le__read__max__data__len.md#a2c0b159c6248cb9df458d587f82a4152) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_tx\_octets](structbt__hci__rp__le__read__max__data__len.md#a2c0b159c6248cb9df458d587f82a4152);

[ 1279](structbt__hci__rp__le__read__max__data__len.md#a6adc84bf3cc86f234e61982d871899b6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_tx\_time](structbt__hci__rp__le__read__max__data__len.md#a6adc84bf3cc86f234e61982d871899b6);

[ 1280](structbt__hci__rp__le__read__max__data__len.md#a9273dac6614f1e120f0539b746bfd6cc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_rx\_octets](structbt__hci__rp__le__read__max__data__len.md#a9273dac6614f1e120f0539b746bfd6cc);

[ 1281](structbt__hci__rp__le__read__max__data__len.md#a963ef9c097906c8db46c35459eb4ecab) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_rx\_time](structbt__hci__rp__le__read__max__data__len.md#a963ef9c097906c8db46c35459eb4ecab);

1282} \_\_packed;

1283

[ 1284](hci__types_8h.md#a833ae32a3a5ffefbe57c7aa9cdf2e5a9)#define BT\_HCI\_LE\_PHY\_1M 0x01

[ 1285](hci__types_8h.md#a727a1780d5f3754a78dea0476c2b97bb)#define BT\_HCI\_LE\_PHY\_2M 0x02

[ 1286](hci__types_8h.md#ac5173dfe471fe4d1aad0f7d79904e46a)#define BT\_HCI\_LE\_PHY\_CODED 0x03

1287

[ 1288](hci__types_8h.md#ad2e063f4522a64ceeb36c1d95835e74e)#define BT\_HCI\_OP\_LE\_READ\_PHY BT\_OP(BT\_OGF\_LE, 0x0030) /\* 0x2030 \*/

[ 1289](structbt__hci__cp__le__read__phy.md)struct [bt\_hci\_cp\_le\_read\_phy](structbt__hci__cp__le__read__phy.md) {

[ 1290](structbt__hci__cp__le__read__phy.md#a7e0a4fa47b613c86364e6e94c2d0bef1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__read__phy.md#a7e0a4fa47b613c86364e6e94c2d0bef1);

1291} \_\_packed;

[ 1292](structbt__hci__rp__le__read__phy.md)struct [bt\_hci\_rp\_le\_read\_phy](structbt__hci__rp__le__read__phy.md) {

[ 1293](structbt__hci__rp__le__read__phy.md#a65d412e37eb2cd839fae262f4f9d5b28) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__phy.md#a65d412e37eb2cd839fae262f4f9d5b28);

[ 1294](structbt__hci__rp__le__read__phy.md#ae708b4f8ad2632d73bedea640f138d9f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__read__phy.md#ae708b4f8ad2632d73bedea640f138d9f);

[ 1295](structbt__hci__rp__le__read__phy.md#a644c0065d97e5de006dc28f7bca62268) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_phy](structbt__hci__rp__le__read__phy.md#a644c0065d97e5de006dc28f7bca62268);

[ 1296](structbt__hci__rp__le__read__phy.md#a5a060e0c0d1e5f33222ab10a5d3977e8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_phy](structbt__hci__rp__le__read__phy.md#a5a060e0c0d1e5f33222ab10a5d3977e8);

1297} \_\_packed;

1298

[ 1299](hci__types_8h.md#a7656d3400ccb540e8bd066cf1232c38e)#define BT\_HCI\_LE\_PHY\_TX\_ANY BIT(0)

[ 1300](hci__types_8h.md#a0fb6efaf47f2d676eb51b3fb99d0a691)#define BT\_HCI\_LE\_PHY\_RX\_ANY BIT(1)

1301

[ 1302](hci__types_8h.md#a8101f257838639b46dcd0d50a92bba0c)#define BT\_HCI\_LE\_PHY\_PREFER\_1M BIT(0)

[ 1303](hci__types_8h.md#ae89ffa7723482ced707f8a57febce629)#define BT\_HCI\_LE\_PHY\_PREFER\_2M BIT(1)

[ 1304](hci__types_8h.md#ab33fde130c9fdb99559b15455e827a7a)#define BT\_HCI\_LE\_PHY\_PREFER\_CODED BIT(2)

1305

[ 1306](hci__types_8h.md#aaa4e3fd27b4157a617a5fb6817bc1881)#define BT\_HCI\_OP\_LE\_SET\_DEFAULT\_PHY BT\_OP(BT\_OGF\_LE, 0x0031) /\* 0x2031 \*/

[ 1307](structbt__hci__cp__le__set__default__phy.md)struct [bt\_hci\_cp\_le\_set\_default\_phy](structbt__hci__cp__le__set__default__phy.md) {

[ 1308](structbt__hci__cp__le__set__default__phy.md#abe1d83e372e874739588812040d0b540) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [all\_phys](structbt__hci__cp__le__set__default__phy.md#abe1d83e372e874739588812040d0b540);

[ 1309](structbt__hci__cp__le__set__default__phy.md#a0c4ab2d91021466fd136af3a0b6bde2a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_phys](structbt__hci__cp__le__set__default__phy.md#a0c4ab2d91021466fd136af3a0b6bde2a);

[ 1310](structbt__hci__cp__le__set__default__phy.md#a4c3410f2ce9fb2817bc5d143908936d1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_phys](structbt__hci__cp__le__set__default__phy.md#a4c3410f2ce9fb2817bc5d143908936d1);

1311} \_\_packed;

1312

[ 1313](hci__types_8h.md#a61909ce217268c8cc6274f16d3db8484)#define BT\_HCI\_LE\_PHY\_CODED\_ANY 0x00

[ 1314](hci__types_8h.md#a54bf26868903f0178b0f9f70111ea6b7)#define BT\_HCI\_LE\_PHY\_CODED\_S2 0x01

[ 1315](hci__types_8h.md#abe28c39a93e86d9ad5e6f0c08b09ef9c)#define BT\_HCI\_LE\_PHY\_CODED\_S8 0x02

1316

[ 1317](hci__types_8h.md#a1d21c4ffe4db8caafa374a9138e179fa)#define BT\_HCI\_OP\_LE\_SET\_PHY BT\_OP(BT\_OGF\_LE, 0x0032) /\* 0x2032 \*/

[ 1318](structbt__hci__cp__le__set__phy.md)struct [bt\_hci\_cp\_le\_set\_phy](structbt__hci__cp__le__set__phy.md) {

[ 1319](structbt__hci__cp__le__set__phy.md#ad0759eea02017674459d4ce0af0e526e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__set__phy.md#ad0759eea02017674459d4ce0af0e526e);

[ 1320](structbt__hci__cp__le__set__phy.md#afb8d056dc7d8824eec0ef16fdf9ce924) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [all\_phys](structbt__hci__cp__le__set__phy.md#afb8d056dc7d8824eec0ef16fdf9ce924);

[ 1321](structbt__hci__cp__le__set__phy.md#a06880062ff486b532ebeb789adb57d1e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_phys](structbt__hci__cp__le__set__phy.md#a06880062ff486b532ebeb789adb57d1e);

[ 1322](structbt__hci__cp__le__set__phy.md#ab30eb68920a0578b16794250e592b12a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_phys](structbt__hci__cp__le__set__phy.md#ab30eb68920a0578b16794250e592b12a);

[ 1323](structbt__hci__cp__le__set__phy.md#a458ab90f83b60fafa66167f474c0800d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [phy\_opts](structbt__hci__cp__le__set__phy.md#a458ab90f83b60fafa66167f474c0800d);

1324} \_\_packed;

1325

[ 1326](hci__types_8h.md#a631e672ab64e36a983d4d3aae789b237)#define BT\_HCI\_LE\_MOD\_INDEX\_STANDARD 0x00

[ 1327](hci__types_8h.md#a423acd131760a1ab7b0671c45c9214ca)#define BT\_HCI\_LE\_MOD\_INDEX\_STABLE 0x01

1328

[ 1329](hci__types_8h.md#a27c179b4c8e85f840b41c4765613c99b)#define BT\_HCI\_LE\_RX\_PHY\_1M 0x01

[ 1330](hci__types_8h.md#ac1db92b615a94b30e587a87d3637ad47)#define BT\_HCI\_LE\_RX\_PHY\_2M 0x02

[ 1331](hci__types_8h.md#a689bc0f95a315c18ee4efbc556d31d60)#define BT\_HCI\_LE\_RX\_PHY\_CODED 0x03

1332

[ 1333](hci__types_8h.md#a51c3637712a8701ae7fee16806f677df)#define BT\_HCI\_OP\_LE\_ENH\_RX\_TEST BT\_OP(BT\_OGF\_LE, 0x0033) /\* 0x2033 \*/

[ 1334](structbt__hci__cp__le__enh__rx__test.md)struct [bt\_hci\_cp\_le\_enh\_rx\_test](structbt__hci__cp__le__enh__rx__test.md) {

[ 1335](structbt__hci__cp__le__enh__rx__test.md#a3aa5b3947a4a0c87342695469bf056ec) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_ch](structbt__hci__cp__le__enh__rx__test.md#a3aa5b3947a4a0c87342695469bf056ec);

[ 1336](structbt__hci__cp__le__enh__rx__test.md#aa2bf385221680b25ce184b4ea5d63cd4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__cp__le__enh__rx__test.md#aa2bf385221680b25ce184b4ea5d63cd4);

[ 1337](structbt__hci__cp__le__enh__rx__test.md#a9151393e9f05a2ded484a1248a6edb88) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mod\_index](structbt__hci__cp__le__enh__rx__test.md#a9151393e9f05a2ded484a1248a6edb88);

1338} \_\_packed;

1339

[ 1340](hci__types_8h.md#a0cb0c8d33e23ff6e59241c88b9e5adee)#define BT\_HCI\_LE\_TX\_PHY\_1M 0x01

[ 1341](hci__types_8h.md#a7de4598ca06439f89772f0e72306ac3c)#define BT\_HCI\_LE\_TX\_PHY\_2M 0x02

[ 1342](hci__types_8h.md#a01d96d9e7bb61db9b3cd31d161b0abf4)#define BT\_HCI\_LE\_TX\_PHY\_CODED\_S8 0x03

[ 1343](hci__types_8h.md#a599195b97f069412e112df470bf2b536)#define BT\_HCI\_LE\_TX\_PHY\_CODED\_S2 0x04

1344

[ 1345](hci__types_8h.md#a903b1ce0bfe7df7de86bae5fb143e88f)#define BT\_HCI\_OP\_LE\_ENH\_TX\_TEST BT\_OP(BT\_OGF\_LE, 0x0034) /\* 0x2034 \*/

[ 1346](structbt__hci__cp__le__enh__tx__test.md)struct [bt\_hci\_cp\_le\_enh\_tx\_test](structbt__hci__cp__le__enh__tx__test.md) {

[ 1347](structbt__hci__cp__le__enh__tx__test.md#a0b7883b36d511c6da1bac543f1aae446) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_ch](structbt__hci__cp__le__enh__tx__test.md#a0b7883b36d511c6da1bac543f1aae446);

[ 1348](structbt__hci__cp__le__enh__tx__test.md#af1e27be0ad23887c0e71024739b00f8d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [test\_data\_len](structbt__hci__cp__le__enh__tx__test.md#af1e27be0ad23887c0e71024739b00f8d);

[ 1349](structbt__hci__cp__le__enh__tx__test.md#a9ccb91be1554172d6c724e438508bfe5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pkt\_payload](structbt__hci__cp__le__enh__tx__test.md#a9ccb91be1554172d6c724e438508bfe5);

[ 1350](structbt__hci__cp__le__enh__tx__test.md#a718442db29c5ac455c3e2aac9844cdd0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__cp__le__enh__tx__test.md#a718442db29c5ac455c3e2aac9844cdd0);

1351} \_\_packed;

1352

[ 1353](hci__types_8h.md#ac96cefff0857a4d19025a2d9dec8333e)#define BT\_HCI\_OP\_LE\_SET\_ADV\_SET\_RANDOM\_ADDR BT\_OP(BT\_OGF\_LE, 0x0035) /\* 0x2035 \*/

[ 1354](structbt__hci__cp__le__set__adv__set__random__addr.md)struct [bt\_hci\_cp\_le\_set\_adv\_set\_random\_addr](structbt__hci__cp__le__set__adv__set__random__addr.md) {

[ 1355](structbt__hci__cp__le__set__adv__set__random__addr.md#aafa39422a16cc4ff11c8073e9c0aab71) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle](structbt__hci__cp__le__set__adv__set__random__addr.md#aafa39422a16cc4ff11c8073e9c0aab71);

[ 1356](structbt__hci__cp__le__set__adv__set__random__addr.md#a2883e9bf7ef6a34712eda2594e23c146) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__le__set__adv__set__random__addr.md#a2883e9bf7ef6a34712eda2594e23c146);

1357} \_\_packed;

1358

[ 1359](hci__types_8h.md#ac9597c1c284e23578352a23bd66c9fad)#define BT\_HCI\_LE\_ADV\_PROP\_CONN BIT(0)

[ 1360](hci__types_8h.md#ab886c4c7f33adf396ca3e09d0f38995d)#define BT\_HCI\_LE\_ADV\_PROP\_SCAN BIT(1)

[ 1361](hci__types_8h.md#acd154c93af2dc866cfe8bcf8e370dd3d)#define BT\_HCI\_LE\_ADV\_PROP\_DIRECT BIT(2)

[ 1362](hci__types_8h.md#a0fb43dd85c3671420029027cbfbf8c11)#define BT\_HCI\_LE\_ADV\_PROP\_HI\_DC\_CONN BIT(3)

[ 1363](hci__types_8h.md#a936310de47af573e0d1d5d9401097ba1)#define BT\_HCI\_LE\_ADV\_PROP\_LEGACY BIT(4)

[ 1364](hci__types_8h.md#a21c60f21a4de9136accc32b0a8a0325c)#define BT\_HCI\_LE\_ADV\_PROP\_ANON BIT(5)

[ 1365](hci__types_8h.md#abd14685442f2fe315a095516464fc92d)#define BT\_HCI\_LE\_ADV\_PROP\_TX\_POWER BIT(6)

1366

[ 1367](hci__types_8h.md#a1599475c6673d4fa0e00d16024df9a3b)#define BT\_HCI\_LE\_PRIM\_ADV\_INTERVAL\_MIN 0x000020

[ 1368](hci__types_8h.md#a5b394658223fd700fa152c4deb2f956e)#define BT\_HCI\_LE\_PRIM\_ADV\_INTERVAL\_MAX 0xFFFFFF

1369

[ 1370](hci__types_8h.md#a39fa8033dcf14aa43dfad7cabc1cb429)#define BT\_HCI\_LE\_ADV\_SCAN\_REQ\_ENABLE 1

[ 1371](hci__types_8h.md#aa1f4b7ba3b48ea6bd7b8a34a7b831a25)#define BT\_HCI\_LE\_ADV\_SCAN\_REQ\_DISABLE 0

1372

[ 1373](hci__types_8h.md#a7f4fcc517033a4743ded39503b35ce29)#define BT\_HCI\_LE\_ADV\_TX\_POWER\_NO\_PREF 0x7F

1374

[ 1375](hci__types_8h.md#a12d97417fa11a07b0af5370b595e9a17)#define BT\_HCI\_LE\_ADV\_HANDLE\_MAX 0xEF

1376

[ 1377](hci__types_8h.md#a973c2e0fc4cb22d58c47865b9e76b940)#define BT\_HCI\_LE\_EXT\_ADV\_SID\_INVALID 0xFF

1378

[ 1379](hci__types_8h.md#a098efdd7908adafd26b8e3f63508c476)#define BT\_HCI\_OP\_LE\_SET\_EXT\_ADV\_PARAM BT\_OP(BT\_OGF\_LE, 0x0036) /\* 0x2036 \*/

[ 1380](structbt__hci__cp__le__set__ext__adv__param.md)struct [bt\_hci\_cp\_le\_set\_ext\_adv\_param](structbt__hci__cp__le__set__ext__adv__param.md) {

[ 1381](structbt__hci__cp__le__set__ext__adv__param.md#a65fe609dde9515212659087a024e7c65) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle](structbt__hci__cp__le__set__ext__adv__param.md#a65fe609dde9515212659087a024e7c65);

[ 1382](structbt__hci__cp__le__set__ext__adv__param.md#a4af102ae90ca6917b3134491c5ff079f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [props](structbt__hci__cp__le__set__ext__adv__param.md#a4af102ae90ca6917b3134491c5ff079f);

[ 1383](structbt__hci__cp__le__set__ext__adv__param.md#ab5a80941b3d832c2906daed8cf069a02) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [prim\_min\_interval](structbt__hci__cp__le__set__ext__adv__param.md#ab5a80941b3d832c2906daed8cf069a02)[3];

[ 1384](structbt__hci__cp__le__set__ext__adv__param.md#a08aa741a56e825a11424bf024ac65e14) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [prim\_max\_interval](structbt__hci__cp__le__set__ext__adv__param.md#a08aa741a56e825a11424bf024ac65e14)[3];

[ 1385](structbt__hci__cp__le__set__ext__adv__param.md#ad7a0b9028bcdb57a9011d4677412aed5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [prim\_channel\_map](structbt__hci__cp__le__set__ext__adv__param.md#ad7a0b9028bcdb57a9011d4677412aed5);

[ 1386](structbt__hci__cp__le__set__ext__adv__param.md#a3594f7337ccd739f59ac7845757de0e8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [own\_addr\_type](structbt__hci__cp__le__set__ext__adv__param.md#a3594f7337ccd739f59ac7845757de0e8);

[ 1387](structbt__hci__cp__le__set__ext__adv__param.md#a819e599df4025036fab2dabd7c61ea37) [bt\_addr\_le\_t](structbt__addr__le__t.md) [peer\_addr](structbt__hci__cp__le__set__ext__adv__param.md#a819e599df4025036fab2dabd7c61ea37);

[ 1388](structbt__hci__cp__le__set__ext__adv__param.md#a29a62f8989f89b014cadbad9b94e996a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter\_policy](structbt__hci__cp__le__set__ext__adv__param.md#a29a62f8989f89b014cadbad9b94e996a);

[ 1389](structbt__hci__cp__le__set__ext__adv__param.md#a5f7f3e477b5b0b8122b85f3e53dd7878) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__hci__cp__le__set__ext__adv__param.md#a5f7f3e477b5b0b8122b85f3e53dd7878);

[ 1390](structbt__hci__cp__le__set__ext__adv__param.md#a048874197ccbdbc626f0563be5c41ec7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [prim\_adv\_phy](structbt__hci__cp__le__set__ext__adv__param.md#a048874197ccbdbc626f0563be5c41ec7);

[ 1391](structbt__hci__cp__le__set__ext__adv__param.md#a5793c6afe545290a1e792bcc73585b72) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sec\_adv\_max\_skip](structbt__hci__cp__le__set__ext__adv__param.md#a5793c6afe545290a1e792bcc73585b72);

[ 1392](structbt__hci__cp__le__set__ext__adv__param.md#abc82ba984647eb00bc490c01ce746a15) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sec\_adv\_phy](structbt__hci__cp__le__set__ext__adv__param.md#abc82ba984647eb00bc490c01ce746a15);

[ 1393](structbt__hci__cp__le__set__ext__adv__param.md#af8bc3509fdd5e89c27db466727fe1cd9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__hci__cp__le__set__ext__adv__param.md#af8bc3509fdd5e89c27db466727fe1cd9);

[ 1394](structbt__hci__cp__le__set__ext__adv__param.md#ae694df46b1db4b029d1e177768b3821f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [scan\_req\_notify\_enable](structbt__hci__cp__le__set__ext__adv__param.md#ae694df46b1db4b029d1e177768b3821f);

1395} \_\_packed;

[ 1396](structbt__hci__rp__le__set__ext__adv__param.md)struct [bt\_hci\_rp\_le\_set\_ext\_adv\_param](structbt__hci__rp__le__set__ext__adv__param.md) {

[ 1397](structbt__hci__rp__le__set__ext__adv__param.md#a6baae317455ffbb489066fcd1fb068c8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__set__ext__adv__param.md#a6baae317455ffbb489066fcd1fb068c8);

[ 1398](structbt__hci__rp__le__set__ext__adv__param.md#a8a876d0e3d4d9d066a27c054569f0b9a) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__hci__rp__le__set__ext__adv__param.md#a8a876d0e3d4d9d066a27c054569f0b9a);

1399} \_\_packed;

1400

[ 1401](hci__types_8h.md#a68c62ac99c4198dbadf6563e40ce33cb)#define BT\_HCI\_LE\_EXT\_ADV\_OP\_INTERM\_FRAG 0x00

[ 1402](hci__types_8h.md#a65b3ae46e1164815cda1325e55df4091)#define BT\_HCI\_LE\_EXT\_ADV\_OP\_FIRST\_FRAG 0x01

[ 1403](hci__types_8h.md#aade6b8cac66aee356c857fcfae17ce65)#define BT\_HCI\_LE\_EXT\_ADV\_OP\_LAST\_FRAG 0x02

[ 1404](hci__types_8h.md#a5394a0dbcd3856ffb8c63440d352120b)#define BT\_HCI\_LE\_EXT\_ADV\_OP\_COMPLETE\_DATA 0x03

[ 1405](hci__types_8h.md#a2860ae578d2332a1c76c7bfaa0714e08)#define BT\_HCI\_LE\_EXT\_ADV\_OP\_UNCHANGED\_DATA 0x04

1406

[ 1407](hci__types_8h.md#aa1dbb6b62c021501320865ac77b5d6da)#define BT\_HCI\_LE\_EXT\_ADV\_FRAG\_ENABLED 0x00

[ 1408](hci__types_8h.md#a4d9626f1b9f0601708b3c38386b5f85c)#define BT\_HCI\_LE\_EXT\_ADV\_FRAG\_DISABLED 0x01

1409

[ 1410](hci__types_8h.md#a3b3f91c046b0656d489c228d75c8b3ff)#define BT\_HCI\_LE\_EXT\_ADV\_FRAG\_MAX\_LEN 251

1411

[ 1412](hci__types_8h.md#a563769ae57bb58be9d7ee8e92019cb99)#define BT\_HCI\_OP\_LE\_SET\_EXT\_ADV\_DATA BT\_OP(BT\_OGF\_LE, 0x0037) /\* 0x2037 \*/

[ 1413](structbt__hci__cp__le__set__ext__adv__data.md)struct [bt\_hci\_cp\_le\_set\_ext\_adv\_data](structbt__hci__cp__le__set__ext__adv__data.md) {

[ 1414](structbt__hci__cp__le__set__ext__adv__data.md#a803bb793eefcc714c6c4034123a2e487) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle](structbt__hci__cp__le__set__ext__adv__data.md#a803bb793eefcc714c6c4034123a2e487);

[ 1415](structbt__hci__cp__le__set__ext__adv__data.md#ac5eaa1834f82024055923d08a3bef6b3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [op](structbt__hci__cp__le__set__ext__adv__data.md#ac5eaa1834f82024055923d08a3bef6b3);

[ 1416](structbt__hci__cp__le__set__ext__adv__data.md#af9eef9f59bfec5867ea36bdf33e3a9b1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [frag\_pref](structbt__hci__cp__le__set__ext__adv__data.md#af9eef9f59bfec5867ea36bdf33e3a9b1);

[ 1417](structbt__hci__cp__le__set__ext__adv__data.md#aea3055cc7ffbaf4cd14996d885e21ba3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structbt__hci__cp__le__set__ext__adv__data.md#aea3055cc7ffbaf4cd14996d885e21ba3);

[ 1418](structbt__hci__cp__le__set__ext__adv__data.md#a7d7df52500eb53a64b6ba5e62f6cf14f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__hci__cp__le__set__ext__adv__data.md#a7d7df52500eb53a64b6ba5e62f6cf14f)[0];

1419} \_\_packed;

1420

[ 1421](hci__types_8h.md#a586395798b3d827ab17634287862ef54)#define BT\_HCI\_OP\_LE\_SET\_EXT\_SCAN\_RSP\_DATA BT\_OP(BT\_OGF\_LE, 0x0038) /\* 0x2038 \*/

[ 1422](structbt__hci__cp__le__set__ext__scan__rsp__data.md)struct [bt\_hci\_cp\_le\_set\_ext\_scan\_rsp\_data](structbt__hci__cp__le__set__ext__scan__rsp__data.md) {

[ 1423](structbt__hci__cp__le__set__ext__scan__rsp__data.md#a8cf0624b9968686c7f6765ee25e11c90) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle](structbt__hci__cp__le__set__ext__scan__rsp__data.md#a8cf0624b9968686c7f6765ee25e11c90);

[ 1424](structbt__hci__cp__le__set__ext__scan__rsp__data.md#a3323a0844680b71cb8aedffa034837d7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [op](structbt__hci__cp__le__set__ext__scan__rsp__data.md#a3323a0844680b71cb8aedffa034837d7);

[ 1425](structbt__hci__cp__le__set__ext__scan__rsp__data.md#ac4e1691926df370b290c9e6d866d310d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [frag\_pref](structbt__hci__cp__le__set__ext__scan__rsp__data.md#ac4e1691926df370b290c9e6d866d310d);

[ 1426](structbt__hci__cp__le__set__ext__scan__rsp__data.md#a6024eac85f600ed3b7051a84b91bdcfa) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structbt__hci__cp__le__set__ext__scan__rsp__data.md#a6024eac85f600ed3b7051a84b91bdcfa);

[ 1427](structbt__hci__cp__le__set__ext__scan__rsp__data.md#ab086720e1a22523ba155cb238ad75197) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__hci__cp__le__set__ext__scan__rsp__data.md#ab086720e1a22523ba155cb238ad75197)[0];

1428} \_\_packed;

1429

[ 1430](hci__types_8h.md#a99e9573f9bd290fb18f82a327ca55ecd)#define BT\_HCI\_OP\_LE\_SET\_EXT\_ADV\_ENABLE BT\_OP(BT\_OGF\_LE, 0x0039) /\* 0x2039 \*/

[ 1431](structbt__hci__ext__adv__set.md)struct [bt\_hci\_ext\_adv\_set](structbt__hci__ext__adv__set.md) {

[ 1432](structbt__hci__ext__adv__set.md#a9d0fd3f6659db172ff4efd74c2c2d216) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle](structbt__hci__ext__adv__set.md#a9d0fd3f6659db172ff4efd74c2c2d216);

[ 1433](structbt__hci__ext__adv__set.md#acc2afc91fe5c0dfcb4c95eaade4a047a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [duration](structbt__hci__ext__adv__set.md#acc2afc91fe5c0dfcb4c95eaade4a047a);

[ 1434](structbt__hci__ext__adv__set.md#a4467ac9a564ea24bb701de46cda2579a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_ext\_adv\_evts](structbt__hci__ext__adv__set.md#a4467ac9a564ea24bb701de46cda2579a);

1435} \_\_packed;

1436

[ 1437](structbt__hci__cp__le__set__ext__adv__enable.md)struct [bt\_hci\_cp\_le\_set\_ext\_adv\_enable](structbt__hci__cp__le__set__ext__adv__enable.md) {

[ 1438](structbt__hci__cp__le__set__ext__adv__enable.md#ab7148b47bf052d8cba1f6bf3385051c8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enable](structbt__hci__cp__le__set__ext__adv__enable.md#ab7148b47bf052d8cba1f6bf3385051c8);

[ 1439](structbt__hci__cp__le__set__ext__adv__enable.md#a06088af8b432ac134943d9ebb7778ac7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [set\_num](structbt__hci__cp__le__set__ext__adv__enable.md#a06088af8b432ac134943d9ebb7778ac7);

[ 1440](structbt__hci__cp__le__set__ext__adv__enable.md#a04911e19f3b2f0079d4e12980d11157f) struct [bt\_hci\_ext\_adv\_set](structbt__hci__ext__adv__set.md) [s](structbt__hci__cp__le__set__ext__adv__enable.md#a04911e19f3b2f0079d4e12980d11157f)[0];

1441} \_\_packed;

1442

[ 1443](hci__types_8h.md#a0246ea11fada7570bf59e73250b49b95)#define BT\_HCI\_OP\_LE\_READ\_MAX\_ADV\_DATA\_LEN BT\_OP(BT\_OGF\_LE, 0x003a) /\* 0x203a \*/

[ 1444](structbt__hci__rp__le__read__max__adv__data__len.md)struct [bt\_hci\_rp\_le\_read\_max\_adv\_data\_len](structbt__hci__rp__le__read__max__adv__data__len.md) {

[ 1445](structbt__hci__rp__le__read__max__adv__data__len.md#a978911dc5028d1f36820447de8e9e5f7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__max__adv__data__len.md#a978911dc5028d1f36820447de8e9e5f7);

[ 1446](structbt__hci__rp__le__read__max__adv__data__len.md#aa4084a89de4929c3e8e2630d0aad7f82) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_adv\_data\_len](structbt__hci__rp__le__read__max__adv__data__len.md#aa4084a89de4929c3e8e2630d0aad7f82);

1447} \_\_packed;

1448

[ 1449](hci__types_8h.md#a8d2a855322d0aa454ed00e1458cf9a38)#define BT\_HCI\_OP\_LE\_READ\_NUM\_ADV\_SETS BT\_OP(BT\_OGF\_LE, 0x003b) /\* 0x203b \*/

[ 1450](structbt__hci__rp__le__read__num__adv__sets.md)struct [bt\_hci\_rp\_le\_read\_num\_adv\_sets](structbt__hci__rp__le__read__num__adv__sets.md) {

[ 1451](structbt__hci__rp__le__read__num__adv__sets.md#a590934059fb851a14b2eec66f32a5334) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__num__adv__sets.md#a590934059fb851a14b2eec66f32a5334);

[ 1452](structbt__hci__rp__le__read__num__adv__sets.md#a7dd26bda7a8ab75fed2af19bb5af34fc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_sets](structbt__hci__rp__le__read__num__adv__sets.md#a7dd26bda7a8ab75fed2af19bb5af34fc);

1453} \_\_packed;

1454

[ 1455](hci__types_8h.md#ae802afd7081a39f062f65e5c0994a9e4)#define BT\_HCI\_OP\_LE\_REMOVE\_ADV\_SET BT\_OP(BT\_OGF\_LE, 0x003c) /\* 0x203c \*/

[ 1456](structbt__hci__cp__le__remove__adv__set.md)struct [bt\_hci\_cp\_le\_remove\_adv\_set](structbt__hci__cp__le__remove__adv__set.md) {

[ 1457](structbt__hci__cp__le__remove__adv__set.md#ab33bf918b10d847bb8fb8ac2409780e6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle](structbt__hci__cp__le__remove__adv__set.md#ab33bf918b10d847bb8fb8ac2409780e6);

1458} \_\_packed;

1459

[ 1460](hci__types_8h.md#a2f95e881ffcda381d8d8ad7ba8705e7d)#define BT\_HCI\_OP\_CLEAR\_ADV\_SETS BT\_OP(BT\_OGF\_LE, 0x003d) /\* 0x203d \*/

1461

[ 1462](hci__types_8h.md#a04f870ac03c1baca22ab5d984354f3bf)#define BT\_HCI\_LE\_PER\_ADV\_INTERVAL\_MIN 0x0006

[ 1463](hci__types_8h.md#a2f2216a88cf77ccac1c9a2f6c5820746)#define BT\_HCI\_LE\_PER\_ADV\_INTERVAL\_MAX 0xFFFF

1464

[ 1465](hci__types_8h.md#a3a111d29fd682fa825f4f9c8c358243f)#define BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_PARAM BT\_OP(BT\_OGF\_LE, 0x003e) /\* 0x203e \*/

[ 1466](structbt__hci__cp__le__set__per__adv__param.md)struct [bt\_hci\_cp\_le\_set\_per\_adv\_param](structbt__hci__cp__le__set__per__adv__param.md) {

[ 1467](structbt__hci__cp__le__set__per__adv__param.md#a2b61031952b3893add7677d3802e368b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle](structbt__hci__cp__le__set__per__adv__param.md#a2b61031952b3893add7677d3802e368b);

[ 1468](structbt__hci__cp__le__set__per__adv__param.md#af01696ef6bf02e7db37d45a0c9852ef5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [min\_interval](structbt__hci__cp__le__set__per__adv__param.md#af01696ef6bf02e7db37d45a0c9852ef5);

[ 1469](structbt__hci__cp__le__set__per__adv__param.md#a1a2a69ea6e310710892184ced472eb8a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_interval](structbt__hci__cp__le__set__per__adv__param.md#a1a2a69ea6e310710892184ced472eb8a);

[ 1470](structbt__hci__cp__le__set__per__adv__param.md#a879ea10e1ab217b4aa49dfcf3b394691) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [props](structbt__hci__cp__le__set__per__adv__param.md#a879ea10e1ab217b4aa49dfcf3b394691);

1471} \_\_packed;

1472

[ 1473](hci__types_8h.md#aa18edf54edfb8d0fcaca5941e8e5e493)#define BT\_HCI\_LE\_PER\_ADV\_OP\_INTERM\_FRAG 0x00

[ 1474](hci__types_8h.md#a8aeb4c76ec769879fc4796fc2919c459)#define BT\_HCI\_LE\_PER\_ADV\_OP\_FIRST\_FRAG 0x01

[ 1475](hci__types_8h.md#a7f2314472ccb051e87d1bb2f9b3fded8)#define BT\_HCI\_LE\_PER\_ADV\_OP\_LAST\_FRAG 0x02

[ 1476](hci__types_8h.md#ada39c45c3c1c7576d4d9794dad115e61)#define BT\_HCI\_LE\_PER\_ADV\_OP\_COMPLETE\_DATA 0x03

1477

[ 1478](hci__types_8h.md#a7b3cd7870ba4af2ff483a831d2700466)#define BT\_HCI\_LE\_PER\_ADV\_FRAG\_MAX\_LEN 252

1479

[ 1480](hci__types_8h.md#ae6611e7b72b057ac9d4004a1772fe435)#define BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_DATA BT\_OP(BT\_OGF\_LE, 0x003f) /\* 0x203f \*/

[ 1481](structbt__hci__cp__le__set__per__adv__data.md)struct [bt\_hci\_cp\_le\_set\_per\_adv\_data](structbt__hci__cp__le__set__per__adv__data.md) {

[ 1482](structbt__hci__cp__le__set__per__adv__data.md#a93cbb46ce6664880487e009a0b47af02) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle](structbt__hci__cp__le__set__per__adv__data.md#a93cbb46ce6664880487e009a0b47af02);

[ 1483](structbt__hci__cp__le__set__per__adv__data.md#aac34596f0970c976c4ef71250d326c2c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [op](structbt__hci__cp__le__set__per__adv__data.md#aac34596f0970c976c4ef71250d326c2c);

[ 1484](structbt__hci__cp__le__set__per__adv__data.md#ae6ee631a153cb6fed88695e599f63e91) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structbt__hci__cp__le__set__per__adv__data.md#ae6ee631a153cb6fed88695e599f63e91);

[ 1485](structbt__hci__cp__le__set__per__adv__data.md#adaf581f8db6aafb4dc5df669df7ad26d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__hci__cp__le__set__per__adv__data.md#adaf581f8db6aafb4dc5df669df7ad26d)[0];

1486} \_\_packed;

1487

[ 1488](hci__types_8h.md#a1c03932d8c1e2c5436eaf45be093b4d4)#define BT\_HCI\_LE\_SET\_PER\_ADV\_ENABLE\_ENABLE BIT(0)

[ 1489](hci__types_8h.md#aaf9b76b276b5cf7e02bb5e3b0a12ecf6)#define BT\_HCI\_LE\_SET\_PER\_ADV\_ENABLE\_ADI BIT(1)

1490

[ 1491](hci__types_8h.md#a3ae23554c13b099b50b129462e08afe4)#define BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_ENABLE BT\_OP(BT\_OGF\_LE, 0x0040) /\* 0x2040 \*/

[ 1492](structbt__hci__cp__le__set__per__adv__enable.md)struct [bt\_hci\_cp\_le\_set\_per\_adv\_enable](structbt__hci__cp__le__set__per__adv__enable.md) {

[ 1493](structbt__hci__cp__le__set__per__adv__enable.md#afff649b908264c617b249bcfbebadd53) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enable](structbt__hci__cp__le__set__per__adv__enable.md#afff649b908264c617b249bcfbebadd53);

[ 1494](structbt__hci__cp__le__set__per__adv__enable.md#a998f4e38a56f771f234ce099b4528a3d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle](structbt__hci__cp__le__set__per__adv__enable.md#a998f4e38a56f771f234ce099b4528a3d);

1495} \_\_packed;

1496

[ 1497](hci__types_8h.md#a7b0687c9e1faae997b76ece821338fd7)#define BT\_HCI\_OP\_LE\_SET\_EXT\_SCAN\_PARAM BT\_OP(BT\_OGF\_LE, 0x0041) /\* 0x2041 \*/

[ 1498](structbt__hci__ext__scan__phy.md)struct [bt\_hci\_ext\_scan\_phy](structbt__hci__ext__scan__phy.md) {

[ 1499](structbt__hci__ext__scan__phy.md#a4cfebc7b2709973953bed9a09a793b7e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__hci__ext__scan__phy.md#a4cfebc7b2709973953bed9a09a793b7e);

[ 1500](structbt__hci__ext__scan__phy.md#a2f087d18bde86d0ac81a14a09ae5b9b0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__hci__ext__scan__phy.md#a2f087d18bde86d0ac81a14a09ae5b9b0);

[ 1501](structbt__hci__ext__scan__phy.md#a9c0196f0d5f0064796c15a5df2ad4c07) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [window](structbt__hci__ext__scan__phy.md#a9c0196f0d5f0064796c15a5df2ad4c07);

1502} \_\_packed;

1503

[ 1504](hci__types_8h.md#a0ef6a16a2b042b3e7623210fc5fcd1a0)#define BT\_HCI\_LE\_EXT\_SCAN\_PHY\_1M BIT(0)

[ 1505](hci__types_8h.md#ad0f0fe21e4e9136e09e0a443a7253759)#define BT\_HCI\_LE\_EXT\_SCAN\_PHY\_2M BIT(1)

[ 1506](hci__types_8h.md#ae15b1ae9e35d060b3a9619d293a7d9ac)#define BT\_HCI\_LE\_EXT\_SCAN\_PHY\_CODED BIT(2)

1507

[ 1508](structbt__hci__cp__le__set__ext__scan__param.md)struct [bt\_hci\_cp\_le\_set\_ext\_scan\_param](structbt__hci__cp__le__set__ext__scan__param.md) {

[ 1509](structbt__hci__cp__le__set__ext__scan__param.md#a3418aa8dbdb8062ee452f5756eb9f30c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [own\_addr\_type](structbt__hci__cp__le__set__ext__scan__param.md#a3418aa8dbdb8062ee452f5756eb9f30c);

[ 1510](structbt__hci__cp__le__set__ext__scan__param.md#a47f6cf7f83451dcc2feac1a8d5837ad8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter\_policy](structbt__hci__cp__le__set__ext__scan__param.md#a47f6cf7f83451dcc2feac1a8d5837ad8);

[ 1511](structbt__hci__cp__le__set__ext__scan__param.md#a6c38b7d074eb3c0cf5c301eb6c03b60c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phys](structbt__hci__cp__le__set__ext__scan__param.md#a6c38b7d074eb3c0cf5c301eb6c03b60c);

[ 1512](structbt__hci__cp__le__set__ext__scan__param.md#ab4eab9a52dca01bc19b35607d6ec5d36) struct [bt\_hci\_ext\_scan\_phy](structbt__hci__ext__scan__phy.md) [p](structbt__hci__cp__le__set__ext__scan__param.md#ab4eab9a52dca01bc19b35607d6ec5d36)[0];

1513} \_\_packed;

1514

1515/\* Extends BT\_HCI\_LE\_SCAN\_FILTER\_DUP \*/

[ 1516](hci__types_8h.md#ae9ba6da1a01dacc52c6a1a2c84d16948)#define BT\_HCI\_LE\_EXT\_SCAN\_FILTER\_DUP\_ENABLE\_RESET 0x02

1517

[ 1518](hci__types_8h.md#af7a8256887657e482084d4ed3810195b)#define BT\_HCI\_OP\_LE\_SET\_EXT\_SCAN\_ENABLE BT\_OP(BT\_OGF\_LE, 0x0042) /\* 0x2042 \*/

[ 1519](structbt__hci__cp__le__set__ext__scan__enable.md)struct [bt\_hci\_cp\_le\_set\_ext\_scan\_enable](structbt__hci__cp__le__set__ext__scan__enable.md) {

[ 1520](structbt__hci__cp__le__set__ext__scan__enable.md#a922d0c5a7ccb6c1e1864f662227b8307) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enable](structbt__hci__cp__le__set__ext__scan__enable.md#a922d0c5a7ccb6c1e1864f662227b8307);

[ 1521](structbt__hci__cp__le__set__ext__scan__enable.md#aa5b0939838ab13eb8299f4a4b2fd3f14) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter\_dup](structbt__hci__cp__le__set__ext__scan__enable.md#aa5b0939838ab13eb8299f4a4b2fd3f14);

[ 1522](structbt__hci__cp__le__set__ext__scan__enable.md#adcd5e00a240f3e7395d0d25994b4013a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [duration](structbt__hci__cp__le__set__ext__scan__enable.md#adcd5e00a240f3e7395d0d25994b4013a);

[ 1523](structbt__hci__cp__le__set__ext__scan__enable.md#aa60c8ade7047dcd202d83cfc3f18ada2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [period](structbt__hci__cp__le__set__ext__scan__enable.md#aa60c8ade7047dcd202d83cfc3f18ada2);

1524} \_\_packed;

1525

[ 1526](hci__types_8h.md#ac498c9cd93b664b5bd2e58982d36d7ad)#define BT\_HCI\_OP\_LE\_EXT\_CREATE\_CONN BT\_OP(BT\_OGF\_LE, 0x0043) /\* 0x2043 \*/

[ 1527](hci__types_8h.md#a1b6bc4da843ed8d04e0b9571465ffd12)#define BT\_HCI\_OP\_LE\_EXT\_CREATE\_CONN\_V2 BT\_OP(BT\_OGF\_LE, 0x0085) /\* 0x2085 \*/

[ 1528](structbt__hci__ext__conn__phy.md)struct [bt\_hci\_ext\_conn\_phy](structbt__hci__ext__conn__phy.md) {

[ 1529](structbt__hci__ext__conn__phy.md#a4f78503fe42ee81fea740ba1643a732e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [scan\_interval](structbt__hci__ext__conn__phy.md#a4f78503fe42ee81fea740ba1643a732e);

[ 1530](structbt__hci__ext__conn__phy.md#ae0e950c8004bd595631f95a289a5c871) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [scan\_window](structbt__hci__ext__conn__phy.md#ae0e950c8004bd595631f95a289a5c871);

[ 1531](structbt__hci__ext__conn__phy.md#a7fc06c1a458aedb6b29381450a5a4df0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_interval\_min](structbt__hci__ext__conn__phy.md#a7fc06c1a458aedb6b29381450a5a4df0);

[ 1532](structbt__hci__ext__conn__phy.md#a7bcf66a3372d92c809d8427796915b88) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_interval\_max](structbt__hci__ext__conn__phy.md#a7bcf66a3372d92c809d8427796915b88);

[ 1533](structbt__hci__ext__conn__phy.md#a7dd57b7ef0b13b15da47e92076f87d79) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_latency](structbt__hci__ext__conn__phy.md#a7dd57b7ef0b13b15da47e92076f87d79);

[ 1534](structbt__hci__ext__conn__phy.md#aaec54c0743dfc08923b5ccd8fc1a4015) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [supervision\_timeout](structbt__hci__ext__conn__phy.md#aaec54c0743dfc08923b5ccd8fc1a4015);

[ 1535](structbt__hci__ext__conn__phy.md#af48212961ce21f5222e57f70ffeb811b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [min\_ce\_len](structbt__hci__ext__conn__phy.md#af48212961ce21f5222e57f70ffeb811b);

[ 1536](structbt__hci__ext__conn__phy.md#a3c3ccb93014758b3215718d2672ce7f3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_ce\_len](structbt__hci__ext__conn__phy.md#a3c3ccb93014758b3215718d2672ce7f3);

1537} \_\_packed;

1538

[ 1539](structbt__hci__cp__le__ext__create__conn.md)struct [bt\_hci\_cp\_le\_ext\_create\_conn](structbt__hci__cp__le__ext__create__conn.md) {

[ 1540](structbt__hci__cp__le__ext__create__conn.md#a0561b446effa3f735a405c0b307466bf) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter\_policy](structbt__hci__cp__le__ext__create__conn.md#a0561b446effa3f735a405c0b307466bf);

[ 1541](structbt__hci__cp__le__ext__create__conn.md#a12a99044f54e3d5dae30a64392444cbf) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [own\_addr\_type](structbt__hci__cp__le__ext__create__conn.md#a12a99044f54e3d5dae30a64392444cbf);

[ 1542](structbt__hci__cp__le__ext__create__conn.md#a79bc55d9f5b1d719de4fb404db9008f3) [bt\_addr\_le\_t](structbt__addr__le__t.md) [peer\_addr](structbt__hci__cp__le__ext__create__conn.md#a79bc55d9f5b1d719de4fb404db9008f3);

[ 1543](structbt__hci__cp__le__ext__create__conn.md#ae859ff0da5e9cdc872943fd74774ef7e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phys](structbt__hci__cp__le__ext__create__conn.md#ae859ff0da5e9cdc872943fd74774ef7e);

[ 1544](structbt__hci__cp__le__ext__create__conn.md#acdb436d6bf2864745ec579622ae0d532) struct [bt\_hci\_ext\_conn\_phy](structbt__hci__ext__conn__phy.md) [p](structbt__hci__cp__le__ext__create__conn.md#acdb436d6bf2864745ec579622ae0d532)[0];

1545} \_\_packed;

1546

[ 1547](structbt__hci__cp__le__ext__create__conn__v2.md)struct [bt\_hci\_cp\_le\_ext\_create\_conn\_v2](structbt__hci__cp__le__ext__create__conn__v2.md) {

[ 1548](structbt__hci__cp__le__ext__create__conn__v2.md#addf1f80c4d3625e0c6d6e716f6e2e207) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_handle](structbt__hci__cp__le__ext__create__conn__v2.md#addf1f80c4d3625e0c6d6e716f6e2e207);

[ 1549](structbt__hci__cp__le__ext__create__conn__v2.md#a536da199958b3b54469f5b4b029e1bac) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent](structbt__hci__cp__le__ext__create__conn__v2.md#a536da199958b3b54469f5b4b029e1bac);

[ 1550](structbt__hci__cp__le__ext__create__conn__v2.md#a66632dbac1605cff69e8da566e800347) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter\_policy](structbt__hci__cp__le__ext__create__conn__v2.md#a66632dbac1605cff69e8da566e800347);

[ 1551](structbt__hci__cp__le__ext__create__conn__v2.md#a05fd0089a0fd43f98042835231407a60) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [own\_addr\_type](structbt__hci__cp__le__ext__create__conn__v2.md#a05fd0089a0fd43f98042835231407a60);

[ 1552](structbt__hci__cp__le__ext__create__conn__v2.md#a25466a04d224bdf495266b0064c424dd) [bt\_addr\_le\_t](structbt__addr__le__t.md) [peer\_addr](structbt__hci__cp__le__ext__create__conn__v2.md#a25466a04d224bdf495266b0064c424dd);

[ 1553](structbt__hci__cp__le__ext__create__conn__v2.md#ae2d3e3079a2848907224bb7ff0efc64b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phys](structbt__hci__cp__le__ext__create__conn__v2.md#ae2d3e3079a2848907224bb7ff0efc64b);

[ 1554](structbt__hci__cp__le__ext__create__conn__v2.md#a8d606c5aa480f54c8da9f42a35ad513e) struct [bt\_hci\_ext\_conn\_phy](structbt__hci__ext__conn__phy.md) [p](structbt__hci__cp__le__ext__create__conn__v2.md#a8d606c5aa480f54c8da9f42a35ad513e)[0];

1555} \_\_packed;

1556

[ 1557](hci__types_8h.md#a44e729aebc339ada5deb86ad9d350404)#define BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_SUBEVENT\_DATA BT\_OP(BT\_OGF\_LE, 0x0082) /\* 0x2082 \*/

[ 1558](structbt__hci__cp__le__set__pawr__subevent__data__element.md)struct [bt\_hci\_cp\_le\_set\_pawr\_subevent\_data\_element](structbt__hci__cp__le__set__pawr__subevent__data__element.md) {

[ 1559](structbt__hci__cp__le__set__pawr__subevent__data__element.md#abf33f93f0f1ddf3532c6cae13483ec1e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent](structbt__hci__cp__le__set__pawr__subevent__data__element.md#abf33f93f0f1ddf3532c6cae13483ec1e);

[ 1560](structbt__hci__cp__le__set__pawr__subevent__data__element.md#a90178bcd86c1bad0a768f391ce11613f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot\_start](structbt__hci__cp__le__set__pawr__subevent__data__element.md#a90178bcd86c1bad0a768f391ce11613f);

[ 1561](structbt__hci__cp__le__set__pawr__subevent__data__element.md#ad8da1cc672eedf8be8cfc7d0d7ec1b41) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot\_count](structbt__hci__cp__le__set__pawr__subevent__data__element.md#ad8da1cc672eedf8be8cfc7d0d7ec1b41);

[ 1562](structbt__hci__cp__le__set__pawr__subevent__data__element.md#ace5860dfa0f628eaed2b68b171d875da) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent\_data\_length](structbt__hci__cp__le__set__pawr__subevent__data__element.md#ace5860dfa0f628eaed2b68b171d875da);

[ 1563](structbt__hci__cp__le__set__pawr__subevent__data__element.md#a91c975189e409b733ac9a4af5763b12a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent\_data](structbt__hci__cp__le__set__pawr__subevent__data__element.md#a91c975189e409b733ac9a4af5763b12a)[0];

1564} \_\_packed;

1565

[ 1566](structbt__hci__cp__le__set__pawr__subevent__data.md)struct [bt\_hci\_cp\_le\_set\_pawr\_subevent\_data](structbt__hci__cp__le__set__pawr__subevent__data.md) {

[ 1567](structbt__hci__cp__le__set__pawr__subevent__data.md#a47d84125d15cce1fc969db3e5caa07e1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_handle](structbt__hci__cp__le__set__pawr__subevent__data.md#a47d84125d15cce1fc969db3e5caa07e1);

[ 1568](structbt__hci__cp__le__set__pawr__subevent__data.md#a9397eebd6771ad159d1bdae0d59e5f46) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_subevents](structbt__hci__cp__le__set__pawr__subevent__data.md#a9397eebd6771ad159d1bdae0d59e5f46);

[ 1569](structbt__hci__cp__le__set__pawr__subevent__data.md#aa932c1f19de96f89a79bbcb3ecbc1f5d) struct [bt\_hci\_cp\_le\_set\_pawr\_subevent\_data\_element](structbt__hci__cp__le__set__pawr__subevent__data__element.md) [subevents](structbt__hci__cp__le__set__pawr__subevent__data.md#aa932c1f19de96f89a79bbcb3ecbc1f5d)[0];

1570} \_\_packed;

1571

1572

[ 1573](hci__types_8h.md#a2be1e66c896dca2022c04164fd94da49)#define BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_RESPONSE\_DATA BT\_OP(BT\_OGF\_LE, 0x0083) /\* 0x2083 \*/

[ 1574](structbt__hci__cp__le__set__pawr__response__data.md)struct [bt\_hci\_cp\_le\_set\_pawr\_response\_data](structbt__hci__cp__le__set__pawr__response__data.md) {

[ 1575](structbt__hci__cp__le__set__pawr__response__data.md#a034afaaacf4b2168b9cd54cfde583b5c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sync\_handle](structbt__hci__cp__le__set__pawr__response__data.md#a034afaaacf4b2168b9cd54cfde583b5c);

[ 1576](structbt__hci__cp__le__set__pawr__response__data.md#aaf5c337af93f13e243451b46a94ffb77) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [request\_event](structbt__hci__cp__le__set__pawr__response__data.md#aaf5c337af93f13e243451b46a94ffb77);

[ 1577](structbt__hci__cp__le__set__pawr__response__data.md#a675a223891b28f06e78df6223439dc28) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [request\_subevent](structbt__hci__cp__le__set__pawr__response__data.md#a675a223891b28f06e78df6223439dc28);

[ 1578](structbt__hci__cp__le__set__pawr__response__data.md#aaf2e0eb3b491b5ccd15ba5259fd900c7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_subevent](structbt__hci__cp__le__set__pawr__response__data.md#aaf2e0eb3b491b5ccd15ba5259fd900c7);

[ 1579](structbt__hci__cp__le__set__pawr__response__data.md#a4356344510833196533bb9582f6fe18a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot](structbt__hci__cp__le__set__pawr__response__data.md#a4356344510833196533bb9582f6fe18a);

[ 1580](structbt__hci__cp__le__set__pawr__response__data.md#a8c546fa3c6d969d44c54926330e5cf85) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_data\_length](structbt__hci__cp__le__set__pawr__response__data.md#a8c546fa3c6d969d44c54926330e5cf85);

[ 1581](structbt__hci__cp__le__set__pawr__response__data.md#a39cbc74ab95881b6dde8fa377d2951e5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_data](structbt__hci__cp__le__set__pawr__response__data.md#a39cbc74ab95881b6dde8fa377d2951e5)[0];

1582} \_\_packed;

1583

[ 1584](hci__types_8h.md#aea7f44f563c109be1676454412757fab)#define BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_SYNC\_SUBEVENT BT\_OP(BT\_OGF\_LE, 0x0084) /\* 0x2084 \*/

[ 1585](structbt__hci__cp__le__set__pawr__sync__subevent.md)struct [bt\_hci\_cp\_le\_set\_pawr\_sync\_subevent](structbt__hci__cp__le__set__pawr__sync__subevent.md) {

[ 1586](structbt__hci__cp__le__set__pawr__sync__subevent.md#a89f3092c2dd561e5469bb5bf57a06172) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sync\_handle](structbt__hci__cp__le__set__pawr__sync__subevent.md#a89f3092c2dd561e5469bb5bf57a06172);

[ 1587](structbt__hci__cp__le__set__pawr__sync__subevent.md#aa73b23816e6c2c6546de15f6f6caff27) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [periodic\_adv\_properties](structbt__hci__cp__le__set__pawr__sync__subevent.md#aa73b23816e6c2c6546de15f6f6caff27);

[ 1588](structbt__hci__cp__le__set__pawr__sync__subevent.md#a2648ff50e0bad585e77e6f340836555a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_subevents](structbt__hci__cp__le__set__pawr__sync__subevent.md#a2648ff50e0bad585e77e6f340836555a);

[ 1589](structbt__hci__cp__le__set__pawr__sync__subevent.md#a9a362ae841e5305b3985c4b2d88c6753) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevents](structbt__hci__cp__le__set__pawr__sync__subevent.md#a9a362ae841e5305b3985c4b2d88c6753)[0];

1590} \_\_packed;

1591

1592

[ 1593](hci__types_8h.md#a1125bfc15404124bf4bd533520be0f77)#define BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_PARAM\_V2 BT\_OP(BT\_OGF\_LE, 0x0086) /\* 0x2086 \*/

[ 1594](structbt__hci__cp__le__set__per__adv__param__v2.md)struct [bt\_hci\_cp\_le\_set\_per\_adv\_param\_v2](structbt__hci__cp__le__set__per__adv__param__v2.md) {

[ 1595](structbt__hci__cp__le__set__per__adv__param__v2.md#aee1088b46914c8e26d9e97ce573291c6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle](structbt__hci__cp__le__set__per__adv__param__v2.md#aee1088b46914c8e26d9e97ce573291c6);

[ 1596](structbt__hci__cp__le__set__per__adv__param__v2.md#ae36e28210a515f73648e6f8b3984fb55) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [min\_interval](structbt__hci__cp__le__set__per__adv__param__v2.md#ae36e28210a515f73648e6f8b3984fb55);

[ 1597](structbt__hci__cp__le__set__per__adv__param__v2.md#acc9718286ab0847a3444d3fc2d3c93bc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_interval](structbt__hci__cp__le__set__per__adv__param__v2.md#acc9718286ab0847a3444d3fc2d3c93bc);

[ 1598](structbt__hci__cp__le__set__per__adv__param__v2.md#ad2d658bb0be35aee6b5c133fece89068) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [props](structbt__hci__cp__le__set__per__adv__param__v2.md#ad2d658bb0be35aee6b5c133fece89068);

[ 1599](structbt__hci__cp__le__set__per__adv__param__v2.md#a7bea764aa5d21e03946804566b1f9869) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_subevents](structbt__hci__cp__le__set__per__adv__param__v2.md#a7bea764aa5d21e03946804566b1f9869);

[ 1600](structbt__hci__cp__le__set__per__adv__param__v2.md#a79dfc3b13068d9c51f0a756f025aaeba) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent\_interval](structbt__hci__cp__le__set__per__adv__param__v2.md#a79dfc3b13068d9c51f0a756f025aaeba);

[ 1601](structbt__hci__cp__le__set__per__adv__param__v2.md#acdeb503c0a13291158ad389c9f6ac206) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot\_delay](structbt__hci__cp__le__set__per__adv__param__v2.md#acdeb503c0a13291158ad389c9f6ac206);

[ 1602](structbt__hci__cp__le__set__per__adv__param__v2.md#a35fcc697e60d3c398f03be7503f611bd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot\_spacing](structbt__hci__cp__le__set__per__adv__param__v2.md#a35fcc697e60d3c398f03be7503f611bd);

[ 1603](structbt__hci__cp__le__set__per__adv__param__v2.md#a2483eb4457f9dc22ff8473175662e260) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_response\_slots](structbt__hci__cp__le__set__per__adv__param__v2.md#a2483eb4457f9dc22ff8473175662e260);

1604} \_\_packed;

1605

1606

[ 1607](hci__types_8h.md#a490bb7d8cf236e49c60771a95d258247)#define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_FP\_USE\_LIST BIT(0)

[ 1608](hci__types_8h.md#a44f11af392e3188e699d8f987cb2f6d6)#define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_FP\_REPORTS\_DISABLED BIT(1)

[ 1609](hci__types_8h.md#a29c5cf397f94af42bdea484fa95a2a78)#define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_FP\_FILTER\_DUPLICATE BIT(2)

1610

[ 1611](hci__types_8h.md#abb3c8fcfc0b48cf6dbebff206a2a9a48)#define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_NO\_FILTERING 0

[ 1612](hci__types_8h.md#a64c7e74877c8ca638217a09d503e742b)#define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_NO\_AOA BIT(0)

[ 1613](hci__types_8h.md#ad349244f13388a7437651e5c3909bcb9)#define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_NO\_AOD\_1US BIT(1)

[ 1614](hci__types_8h.md#aae32740df5a3096a9b17b9c06e6cc3e9)#define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_NO\_AOD\_2US BIT(2)

[ 1615](hci__types_8h.md#a5532c8ee93198eb831c12b182e13a534)#define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_NO\_CTE BIT(3)

[ 1616](hci__types_8h.md#aa3b526ab2ed1aeaab0e26a5390b3dcea)#define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_ONLY\_CTE BIT(4)

1617/\* Constants to check correctness of CTE type \*/

[ 1618](hci__types_8h.md#a4c884821e7136f6f68bc4d92b394381a)#define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_ALLOWED\_BITS 5

[ 1619](hci__types_8h.md#a6ad9e08bcef788c32481756f76df6a43)#define BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_INVALID\_VALUE \

1620 (~BIT\_MASK(BT\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CTE\_TYPE\_ALLOWED\_BITS))

1621

[ 1622](hci__types_8h.md#a589c2da26ce325d5cb45726c772cf7ab)#define BT\_HCI\_OP\_LE\_PER\_ADV\_CREATE\_SYNC BT\_OP(BT\_OGF\_LE, 0x0044) /\* 0x2044 \*/

[ 1623](structbt__hci__cp__le__per__adv__create__sync.md)struct [bt\_hci\_cp\_le\_per\_adv\_create\_sync](structbt__hci__cp__le__per__adv__create__sync.md) {

[ 1624](structbt__hci__cp__le__per__adv__create__sync.md#aff300f352ec5f0fece90f88db811ef75) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [options](structbt__hci__cp__le__per__adv__create__sync.md#aff300f352ec5f0fece90f88db811ef75);

[ 1625](structbt__hci__cp__le__per__adv__create__sync.md#ab5c4debe1babb98c60c1f1bfdf55359a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__hci__cp__le__per__adv__create__sync.md#ab5c4debe1babb98c60c1f1bfdf55359a);

[ 1626](structbt__hci__cp__le__per__adv__create__sync.md#a3a0a0bc1bd5014f2ede0c4ef6cc30d24) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__hci__cp__le__per__adv__create__sync.md#a3a0a0bc1bd5014f2ede0c4ef6cc30d24);

[ 1627](structbt__hci__cp__le__per__adv__create__sync.md#a554552684fa2a8d0022f9e31ade9c222) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [skip](structbt__hci__cp__le__per__adv__create__sync.md#a554552684fa2a8d0022f9e31ade9c222);

[ 1628](structbt__hci__cp__le__per__adv__create__sync.md#a46ea01403f68d42a315ff629374b2a95) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sync\_timeout](structbt__hci__cp__le__per__adv__create__sync.md#a46ea01403f68d42a315ff629374b2a95);

[ 1629](structbt__hci__cp__le__per__adv__create__sync.md#a905b2a9166dd668df5929f0866769576) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__hci__cp__le__per__adv__create__sync.md#a905b2a9166dd668df5929f0866769576);

1630} \_\_packed;

1631

[ 1632](hci__types_8h.md#a3803042099104029f5b49536cb769e6c)#define BT\_HCI\_OP\_LE\_PER\_ADV\_CREATE\_SYNC\_CANCEL BT\_OP(BT\_OGF\_LE, 0x0045) /\* 0x2045 \*/

1633

[ 1634](hci__types_8h.md#a57b7b3cab371b4dd230343dfbc5a5e98)#define BT\_HCI\_OP\_LE\_PER\_ADV\_TERMINATE\_SYNC BT\_OP(BT\_OGF\_LE, 0x0046) /\* 0x2046 \*/

[ 1635](structbt__hci__cp__le__per__adv__terminate__sync.md)struct [bt\_hci\_cp\_le\_per\_adv\_terminate\_sync](structbt__hci__cp__le__per__adv__terminate__sync.md) {

[ 1636](structbt__hci__cp__le__per__adv__terminate__sync.md#a607fce7fd5c88e12f82e3d9731bd7f1a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__per__adv__terminate__sync.md#a607fce7fd5c88e12f82e3d9731bd7f1a);

1637} \_\_packed;

1638

[ 1639](hci__types_8h.md#a393378ba85552bb5f41475a863ca649f)#define BT\_HCI\_OP\_LE\_ADD\_DEV\_TO\_PER\_ADV\_LIST BT\_OP(BT\_OGF\_LE, 0x0047) /\* 0x2047 \*/

[ 1640](structbt__hci__cp__le__add__dev__to__per__adv__list.md)struct [bt\_hci\_cp\_le\_add\_dev\_to\_per\_adv\_list](structbt__hci__cp__le__add__dev__to__per__adv__list.md) {

[ 1641](structbt__hci__cp__le__add__dev__to__per__adv__list.md#ad93d72bfa7e4123ee9728f6bf73b69df) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__hci__cp__le__add__dev__to__per__adv__list.md#ad93d72bfa7e4123ee9728f6bf73b69df);

[ 1642](structbt__hci__cp__le__add__dev__to__per__adv__list.md#a97d9c5dd0cc4b3ab7f6ebfec206b7407) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__hci__cp__le__add__dev__to__per__adv__list.md#a97d9c5dd0cc4b3ab7f6ebfec206b7407);

1643} \_\_packed;

1644

[ 1645](hci__types_8h.md#a8545e1ede192257a4383eea6b2e932b7)#define BT\_HCI\_OP\_LE\_REM\_DEV\_FROM\_PER\_ADV\_LIST BT\_OP(BT\_OGF\_LE, 0x0048) /\* 0x2048 \*/

[ 1646](structbt__hci__cp__le__rem__dev__from__per__adv__list.md)struct [bt\_hci\_cp\_le\_rem\_dev\_from\_per\_adv\_list](structbt__hci__cp__le__rem__dev__from__per__adv__list.md) {

[ 1647](structbt__hci__cp__le__rem__dev__from__per__adv__list.md#adc420288f6a79c1a92f57241d3da3d81) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__hci__cp__le__rem__dev__from__per__adv__list.md#adc420288f6a79c1a92f57241d3da3d81);

[ 1648](structbt__hci__cp__le__rem__dev__from__per__adv__list.md#a6629f3ececf586792a14f3c028cc8e8c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__hci__cp__le__rem__dev__from__per__adv__list.md#a6629f3ececf586792a14f3c028cc8e8c);

1649} \_\_packed;

1650

[ 1651](hci__types_8h.md#affcd4a54d0b26d7b07e39157f17167b4)#define BT\_HCI\_OP\_LE\_CLEAR\_PER\_ADV\_LIST BT\_OP(BT\_OGF\_LE, 0x0049) /\* 0x2049 \*/

1652

[ 1653](hci__types_8h.md#a3e2fd45c015809e131ac6b3f6a9c72fc)#define BT\_HCI\_OP\_LE\_READ\_PER\_ADV\_LIST\_SIZE BT\_OP(BT\_OGF\_LE, 0x004a) /\* 0x204a \*/

[ 1654](structbt__hci__rp__le__read__per__adv__list__size.md)struct [bt\_hci\_rp\_le\_read\_per\_adv\_list\_size](structbt__hci__rp__le__read__per__adv__list__size.md) {

[ 1655](structbt__hci__rp__le__read__per__adv__list__size.md#a70aa5b466bdbbd309fc59570625c35e5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__per__adv__list__size.md#a70aa5b466bdbbd309fc59570625c35e5);

[ 1656](structbt__hci__rp__le__read__per__adv__list__size.md#ab6c4ed1037327669aef623f3a1e9d601) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [list\_size](structbt__hci__rp__le__read__per__adv__list__size.md#ab6c4ed1037327669aef623f3a1e9d601);

1657} \_\_packed;

1658

[ 1659](hci__types_8h.md#a77d132306109474465575369db342dbd)#define BT\_HCI\_OP\_LE\_READ\_TX\_POWER BT\_OP(BT\_OGF\_LE, 0x004b) /\* 0x204b \*/

[ 1660](structbt__hci__rp__le__read__tx__power.md)struct [bt\_hci\_rp\_le\_read\_tx\_power](structbt__hci__rp__le__read__tx__power.md) {

[ 1661](structbt__hci__rp__le__read__tx__power.md#a805629b92c65e006082d819f578ed555) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__tx__power.md#a805629b92c65e006082d819f578ed555);

[ 1662](structbt__hci__rp__le__read__tx__power.md#a6d4ab95efda5cfc97ae11d83787da8d7) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [min\_tx\_power](structbt__hci__rp__le__read__tx__power.md#a6d4ab95efda5cfc97ae11d83787da8d7);

[ 1663](structbt__hci__rp__le__read__tx__power.md#a1d794f1f7ea77eceac7dae2546eab047) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [max\_tx\_power](structbt__hci__rp__le__read__tx__power.md#a1d794f1f7ea77eceac7dae2546eab047);

1664} \_\_packed;

1665

[ 1666](hci__types_8h.md#a6c454d3276f7eaae542b13becad6482c)#define BT\_HCI\_OP\_LE\_READ\_RF\_PATH\_COMP BT\_OP(BT\_OGF\_LE, 0x004c) /\* 0x204c \*/

[ 1667](structbt__hci__rp__le__read__rf__path__comp.md)struct [bt\_hci\_rp\_le\_read\_rf\_path\_comp](structbt__hci__rp__le__read__rf__path__comp.md) {

[ 1668](structbt__hci__rp__le__read__rf__path__comp.md#a84a04bcc64ea6d50fe41e9b416a5ada1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__rf__path__comp.md#a84a04bcc64ea6d50fe41e9b416a5ada1);

[ 1669](structbt__hci__rp__le__read__rf__path__comp.md#a827fa954277823efdc5838c317a1460a) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [tx\_path\_comp](structbt__hci__rp__le__read__rf__path__comp.md#a827fa954277823efdc5838c317a1460a);

[ 1670](structbt__hci__rp__le__read__rf__path__comp.md#a0f46a99c74006dc0a4dfd1a49c72e077) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [rx\_path\_comp](structbt__hci__rp__le__read__rf__path__comp.md#a0f46a99c74006dc0a4dfd1a49c72e077);

1671} \_\_packed;

1672

[ 1673](hci__types_8h.md#a766b66d1fc7df1d8924d060217de9b9b)#define BT\_HCI\_OP\_LE\_WRITE\_RF\_PATH\_COMP BT\_OP(BT\_OGF\_LE, 0x004d) /\* 0x204d \*/

[ 1674](structbt__hci__cp__le__write__rf__path__comp.md)struct [bt\_hci\_cp\_le\_write\_rf\_path\_comp](structbt__hci__cp__le__write__rf__path__comp.md) {

[ 1675](structbt__hci__cp__le__write__rf__path__comp.md#a5f99b131f3fba91706bdc8277c1abba1) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [tx\_path\_comp](structbt__hci__cp__le__write__rf__path__comp.md#a5f99b131f3fba91706bdc8277c1abba1);

[ 1676](structbt__hci__cp__le__write__rf__path__comp.md#a11aad5607e444cf55dd5878f1f6f9436) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [rx\_path\_comp](structbt__hci__cp__le__write__rf__path__comp.md#a11aad5607e444cf55dd5878f1f6f9436);

1677} \_\_packed;

1678

[ 1679](hci__types_8h.md#a423b143e474548458b8bcce59029f722)#define BT\_HCI\_LE\_PRIVACY\_MODE\_NETWORK 0x00

[ 1680](hci__types_8h.md#ae61d38e84e0d58be45ffaf521abad2f6)#define BT\_HCI\_LE\_PRIVACY\_MODE\_DEVICE 0x01

1681

[ 1682](hci__types_8h.md#a7e1fad2d353904bb345f3a1579c98576)#define BT\_HCI\_OP\_LE\_SET\_PRIVACY\_MODE BT\_OP(BT\_OGF\_LE, 0x004e) /\* 0x204e \*/

[ 1683](structbt__hci__cp__le__set__privacy__mode.md)struct [bt\_hci\_cp\_le\_set\_privacy\_mode](structbt__hci__cp__le__set__privacy__mode.md) {

[ 1684](structbt__hci__cp__le__set__privacy__mode.md#a404cc9f04cd11924445f12eb4471ef2e) [bt\_addr\_le\_t](structbt__addr__le__t.md) [id\_addr](structbt__hci__cp__le__set__privacy__mode.md#a404cc9f04cd11924445f12eb4471ef2e);

[ 1685](structbt__hci__cp__le__set__privacy__mode.md#a8ca00418b0638bba6ef586d6cbf253a5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mode](structbt__hci__cp__le__set__privacy__mode.md#a8ca00418b0638bba6ef586d6cbf253a5);

1686} \_\_packed;

1687

[ 1688](hci__types_8h.md#a6764be57300c8dac30a058ebf8387159)#define BT\_HCI\_LE\_TEST\_CTE\_DISABLED 0x00

[ 1689](hci__types_8h.md#a1f45696f06d7bc3f4cc8393bd6967286)#define BT\_HCI\_LE\_TEST\_CTE\_TYPE\_ANY 0x00

[ 1690](hci__types_8h.md#ac4ac180578ed3f662d91c43b5c6b6b53)#define BT\_HCI\_LE\_TEST\_SLOT\_DURATION\_ANY 0x00

[ 1691](hci__types_8h.md#aef669f8887a165b4948eb651c91968c1)#define BT\_HCI\_LE\_TEST\_SWITCH\_PATTERN\_LEN\_ANY 0x00

1692

[ 1693](hci__types_8h.md#abe1567f7cf83148b3f2214b6e0787da0)#define BT\_HCI\_OP\_LE\_RX\_TEST\_V3 BT\_OP(BT\_OGF\_LE, 0x004f) /\* 0x204f \*/

[ 1694](structbt__hci__cp__le__rx__test__v3.md)struct [bt\_hci\_cp\_le\_rx\_test\_v3](structbt__hci__cp__le__rx__test__v3.md) {

[ 1695](structbt__hci__cp__le__rx__test__v3.md#abd33b70c948d4ee42d96d0d2e7f7cb1c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_ch](structbt__hci__cp__le__rx__test__v3.md#abd33b70c948d4ee42d96d0d2e7f7cb1c);

[ 1696](structbt__hci__cp__le__rx__test__v3.md#ad1c211c59cf34d76429d4d4548966630) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__cp__le__rx__test__v3.md#ad1c211c59cf34d76429d4d4548966630);

[ 1697](structbt__hci__cp__le__rx__test__v3.md#a7ffde9dc565194c0108177cf11b02b5b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mod\_index](structbt__hci__cp__le__rx__test__v3.md#a7ffde9dc565194c0108177cf11b02b5b);

[ 1698](structbt__hci__cp__le__rx__test__v3.md#ad1a1082d27b8a10e25eebd347404637c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [expected\_cte\_len](structbt__hci__cp__le__rx__test__v3.md#ad1a1082d27b8a10e25eebd347404637c);

[ 1699](structbt__hci__cp__le__rx__test__v3.md#a55b5c4739e456167f17bf3899d096e61) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [expected\_cte\_type](structbt__hci__cp__le__rx__test__v3.md#a55b5c4739e456167f17bf3899d096e61);

[ 1700](structbt__hci__cp__le__rx__test__v3.md#a5cd5a44b0832b9f6e2198b9ad714b99b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [slot\_durations](structbt__hci__cp__le__rx__test__v3.md#a5cd5a44b0832b9f6e2198b9ad714b99b);

[ 1701](structbt__hci__cp__le__rx__test__v3.md#ab0832e72ef90b1269928378638fcb194) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [switch\_pattern\_len](structbt__hci__cp__le__rx__test__v3.md#ab0832e72ef90b1269928378638fcb194);

[ 1702](structbt__hci__cp__le__rx__test__v3.md#aa6cd0835068f378949da182af13e2438) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ant\_ids](structbt__hci__cp__le__rx__test__v3.md#aa6cd0835068f378949da182af13e2438)[0];

1703} \_\_packed;

1704

[ 1705](hci__types_8h.md#ad570a3edcefcf927e5253805e1d3d4e4)#define BT\_HCI\_OP\_LE\_TX\_TEST\_V3 BT\_OP(BT\_OGF\_LE, 0x0050) /\* 0x2050 \*/

1706

[ 1707](structbt__hci__cp__le__tx__test__v3.md)struct [bt\_hci\_cp\_le\_tx\_test\_v3](structbt__hci__cp__le__tx__test__v3.md) {

[ 1708](structbt__hci__cp__le__tx__test__v3.md#a6486882bc375f229a88bbfa53be49670) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_ch](structbt__hci__cp__le__tx__test__v3.md#a6486882bc375f229a88bbfa53be49670);

[ 1709](structbt__hci__cp__le__tx__test__v3.md#a1c0828e51bb6c24e9dd1f12b5badcfea) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [test\_data\_len](structbt__hci__cp__le__tx__test__v3.md#a1c0828e51bb6c24e9dd1f12b5badcfea);

[ 1710](structbt__hci__cp__le__tx__test__v3.md#ad8f2d2ca3ad3be28c0aec9e8a0e1bc61) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pkt\_payload](structbt__hci__cp__le__tx__test__v3.md#ad8f2d2ca3ad3be28c0aec9e8a0e1bc61);

[ 1711](structbt__hci__cp__le__tx__test__v3.md#a712a30d9d6afc7d302041e1de6721de4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__cp__le__tx__test__v3.md#a712a30d9d6afc7d302041e1de6721de4);

[ 1712](structbt__hci__cp__le__tx__test__v3.md#a52d2d6dcc188d5f02904e0e56f461841) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_len](structbt__hci__cp__le__tx__test__v3.md#a52d2d6dcc188d5f02904e0e56f461841);

[ 1713](structbt__hci__cp__le__tx__test__v3.md#adf6b1653902fb13cc1ccc32cd91c990f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__hci__cp__le__tx__test__v3.md#adf6b1653902fb13cc1ccc32cd91c990f);

[ 1714](structbt__hci__cp__le__tx__test__v3.md#a459b850f35c61bf7f53d3730245cb4bb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [switch\_pattern\_len](structbt__hci__cp__le__tx__test__v3.md#a459b850f35c61bf7f53d3730245cb4bb);

[ 1715](structbt__hci__cp__le__tx__test__v3.md#afdb6dd44108e9a4a21ac31a74c1e083f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ant\_ids](structbt__hci__cp__le__tx__test__v3.md#afdb6dd44108e9a4a21ac31a74c1e083f)[0];

1716} \_\_packed;

1717

1718/\* Min and max Constant Tone Extension length in 8us units \*/

[ 1719](hci__types_8h.md#a80376d34b4d701d5f6092aa101ce0e6c)#define BT\_HCI\_LE\_CTE\_LEN\_MIN 0x2

[ 1720](hci__types_8h.md#acdfe03ade99fa88779b68e435aea23e3)#define BT\_HCI\_LE\_CTE\_LEN\_MAX 0x14

1721

[ 1722](hci__types_8h.md#a9b3306f29525c50cd8bd501f7391e518)#define BT\_HCI\_LE\_AOA\_CTE 0x0

[ 1723](hci__types_8h.md#a8569e960c44660eb41cdccbe5aeb6ead)#define BT\_HCI\_LE\_AOD\_CTE\_1US 0x1

[ 1724](hci__types_8h.md#a970732caa95f5742fc18c91efbc7095b)#define BT\_HCI\_LE\_AOD\_CTE\_2US 0x2

[ 1725](hci__types_8h.md#aeee9fd73771de54542f7ff24f95eceba)#define BT\_HCI\_LE\_NO\_CTE 0xFF

1726

[ 1727](hci__types_8h.md#aec2a77fadbb6bf24267d659a84b7c9a9)#define BT\_HCI\_LE\_CTE\_COUNT\_MIN 0x1

[ 1728](hci__types_8h.md#a442df4f693ae5bb75d1d8f54fe204bda)#define BT\_HCI\_LE\_CTE\_COUNT\_MAX 0x10

1729

[ 1730](hci__types_8h.md#a900509c6e7485b44de09a43555225ce8)#define BT\_HCI\_OP\_LE\_SET\_CL\_CTE\_TX\_PARAMS BT\_OP(BT\_OGF\_LE, 0x0051) /\* 0x2051 \*/

[ 1731](structbt__hci__cp__le__set__cl__cte__tx__params.md)struct [bt\_hci\_cp\_le\_set\_cl\_cte\_tx\_params](structbt__hci__cp__le__set__cl__cte__tx__params.md) {

[ 1732](structbt__hci__cp__le__set__cl__cte__tx__params.md#a8f20e6e3bb408551d6cc494ad19391c4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle](structbt__hci__cp__le__set__cl__cte__tx__params.md#a8f20e6e3bb408551d6cc494ad19391c4);

[ 1733](structbt__hci__cp__le__set__cl__cte__tx__params.md#ab5c4742cf37cf7e802423beb4a9b4fa2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_len](structbt__hci__cp__le__set__cl__cte__tx__params.md#ab5c4742cf37cf7e802423beb4a9b4fa2);

[ 1734](structbt__hci__cp__le__set__cl__cte__tx__params.md#a869192cea35f4cd57984614e4c8bb5a5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__hci__cp__le__set__cl__cte__tx__params.md#a869192cea35f4cd57984614e4c8bb5a5);

[ 1735](structbt__hci__cp__le__set__cl__cte__tx__params.md#af5e82bf572b385904a0f24219bdc72ca) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_count](structbt__hci__cp__le__set__cl__cte__tx__params.md#af5e82bf572b385904a0f24219bdc72ca);

[ 1736](structbt__hci__cp__le__set__cl__cte__tx__params.md#a8208571653e444221648d2a884eabfae) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [switch\_pattern\_len](structbt__hci__cp__le__set__cl__cte__tx__params.md#a8208571653e444221648d2a884eabfae);

[ 1737](structbt__hci__cp__le__set__cl__cte__tx__params.md#a27a228653ea560a77369a6b1829a8a9d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ant\_ids](structbt__hci__cp__le__set__cl__cte__tx__params.md#a27a228653ea560a77369a6b1829a8a9d)[0];

1738} \_\_packed;

1739

[ 1740](hci__types_8h.md#a5527fd8badb977f2ef061ba76468ccf3)#define BT\_HCI\_OP\_LE\_SET\_CL\_CTE\_TX\_ENABLE BT\_OP(BT\_OGF\_LE, 0x0052) /\* 0x2052 \*/

[ 1741](structbt__hci__cp__le__set__cl__cte__tx__enable.md)struct [bt\_hci\_cp\_le\_set\_cl\_cte\_tx\_enable](structbt__hci__cp__le__set__cl__cte__tx__enable.md) {

[ 1742](structbt__hci__cp__le__set__cl__cte__tx__enable.md#a55125c808a888eeecfee9410bcb55859) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle](structbt__hci__cp__le__set__cl__cte__tx__enable.md#a55125c808a888eeecfee9410bcb55859);

[ 1743](structbt__hci__cp__le__set__cl__cte__tx__enable.md#a3530dae940caefeafb9de4ac761ee080) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_enable](structbt__hci__cp__le__set__cl__cte__tx__enable.md#a3530dae940caefeafb9de4ac761ee080);

1744} \_\_packed;

1745

[ 1746](hci__types_8h.md#a1410330e31701a140eb8c0c73c943972)#define BT\_HCI\_LE\_ANTENNA\_SWITCHING\_SLOT\_1US 0x1

[ 1747](hci__types_8h.md#afa70fe0b1b9e277bfcb6bf7d6fc03564)#define BT\_HCI\_LE\_ANTENNA\_SWITCHING\_SLOT\_2US 0x2

1748

[ 1749](hci__types_8h.md#a85450acad700f8cef375d34235752650)#define BT\_HCI\_LE\_SAMPLE\_CTE\_ALL 0x0

[ 1750](hci__types_8h.md#afd22fac7ff6d5006015159ffc978798a)#define BT\_HCI\_LE\_SAMPLE\_CTE\_COUNT\_MIN 0x1

[ 1751](hci__types_8h.md#a0c8888c4dfed6ab4c0f07a37ca3b2278)#define BT\_HCI\_LE\_SAMPLE\_CTE\_COUNT\_MAX 0x10

1752

[ 1753](hci__types_8h.md#a728b9a505c9a2f719424bd277f7e8765)#define BT\_HCI\_OP\_LE\_SET\_CL\_CTE\_SAMPLING\_ENABLE BT\_OP(BT\_OGF\_LE, 0x0053) /\* 0x2053 \*/

[ 1754](structbt__hci__cp__le__set__cl__cte__sampling__enable.md)struct [bt\_hci\_cp\_le\_set\_cl\_cte\_sampling\_enable](structbt__hci__cp__le__set__cl__cte__sampling__enable.md) {

[ 1755](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#a91d3458e2049ab434e220403b7ba235d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sync\_handle](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#a91d3458e2049ab434e220403b7ba235d);

[ 1756](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#aca9e1316c716525f00308f64b8c6cec4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sampling\_enable](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#aca9e1316c716525f00308f64b8c6cec4);

[ 1757](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#aaaed0fc39158c653041fd760a00cecec) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [slot\_durations](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#aaaed0fc39158c653041fd760a00cecec);

[ 1758](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#a38e770b3e5f9d7d63a564dfa7c80451f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_sampled\_cte](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#a38e770b3e5f9d7d63a564dfa7c80451f);

[ 1759](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#a4f52142ef1d2365859189b7a2abe050b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [switch\_pattern\_len](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#a4f52142ef1d2365859189b7a2abe050b);

[ 1760](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#a67bb2dbfe1707f76a5e211e007459c22) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ant\_ids](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#a67bb2dbfe1707f76a5e211e007459c22)[0];

1761} \_\_packed;

1762

[ 1763](structbt__hci__rp__le__set__cl__cte__sampling__enable.md)struct [bt\_hci\_rp\_le\_set\_cl\_cte\_sampling\_enable](structbt__hci__rp__le__set__cl__cte__sampling__enable.md) {

[ 1764](structbt__hci__rp__le__set__cl__cte__sampling__enable.md#a5962f97cef6e53452cdccab1c3440519) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__set__cl__cte__sampling__enable.md#a5962f97cef6e53452cdccab1c3440519);

[ 1765](structbt__hci__rp__le__set__cl__cte__sampling__enable.md#a44db7f831e8d730ec3c80c01ef9543aa) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sync\_handle](structbt__hci__rp__le__set__cl__cte__sampling__enable.md#a44db7f831e8d730ec3c80c01ef9543aa);

1766} \_\_packed;

1767

[ 1768](hci__types_8h.md#a8a079c51fc7c37f29afeda663206c59e)#define BT\_HCI\_OP\_LE\_SET\_CONN\_CTE\_RX\_PARAMS BT\_OP(BT\_OGF\_LE, 0x0054) /\* 0x2054 \*/

[ 1769](structbt__hci__cp__le__set__conn__cte__rx__params.md)struct [bt\_hci\_cp\_le\_set\_conn\_cte\_rx\_params](structbt__hci__cp__le__set__conn__cte__rx__params.md) {

[ 1770](structbt__hci__cp__le__set__conn__cte__rx__params.md#a76968866cf5c6ef4bfb983cb6b68a827) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__set__conn__cte__rx__params.md#a76968866cf5c6ef4bfb983cb6b68a827);

[ 1771](structbt__hci__cp__le__set__conn__cte__rx__params.md#a615cae822878cf1344a990e30fa80044) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sampling\_enable](structbt__hci__cp__le__set__conn__cte__rx__params.md#a615cae822878cf1344a990e30fa80044);

[ 1772](structbt__hci__cp__le__set__conn__cte__rx__params.md#a6246d492b94c67af9604b89912dbdb61) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [slot\_durations](structbt__hci__cp__le__set__conn__cte__rx__params.md#a6246d492b94c67af9604b89912dbdb61);

[ 1773](structbt__hci__cp__le__set__conn__cte__rx__params.md#a89194a5b9e6c7f0c176c915e451911df) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [switch\_pattern\_len](structbt__hci__cp__le__set__conn__cte__rx__params.md#a89194a5b9e6c7f0c176c915e451911df);

[ 1774](structbt__hci__cp__le__set__conn__cte__rx__params.md#a519c37f5d797d8ddac5ba9be7c14b9f9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ant\_ids](structbt__hci__cp__le__set__conn__cte__rx__params.md#a519c37f5d797d8ddac5ba9be7c14b9f9)[0];

1775} \_\_packed;

1776

[ 1777](structbt__hci__rp__le__set__conn__cte__rx__params.md)struct [bt\_hci\_rp\_le\_set\_conn\_cte\_rx\_params](structbt__hci__rp__le__set__conn__cte__rx__params.md) {

[ 1778](structbt__hci__rp__le__set__conn__cte__rx__params.md#ad38bb356876c16904e408405607de73c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__set__conn__cte__rx__params.md#ad38bb356876c16904e408405607de73c);

[ 1779](structbt__hci__rp__le__set__conn__cte__rx__params.md#a3c3fb92d422e7ccaf0c98706d46b3e5a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__set__conn__cte__rx__params.md#a3c3fb92d422e7ccaf0c98706d46b3e5a);

1780} \_\_packed;

1781

[ 1782](hci__types_8h.md#ac80b68b1ca4f55a8a44b6bf0dfa7bfb3)#define BT\_HCI\_LE\_AOA\_CTE\_RSP BIT(0)

[ 1783](hci__types_8h.md#a124137512b0f87a67fff694359d629d0)#define BT\_HCI\_LE\_AOD\_CTE\_RSP\_1US BIT(1)

[ 1784](hci__types_8h.md#a5c1dd462d05e4a5615f80402f892ecbc)#define BT\_HCI\_LE\_AOD\_CTE\_RSP\_2US BIT(2)

1785

[ 1786](hci__types_8h.md#ad74e54836996fc3d02fbb245f9c72b5a)#define BT\_HCI\_LE\_SWITCH\_PATTERN\_LEN\_MIN 0x2

[ 1787](hci__types_8h.md#ad6bdc84c282a4e35ded32687cba94e9f)#define BT\_HCI\_LE\_SWITCH\_PATTERN\_LEN\_MAX 0x4B

1788

[ 1789](hci__types_8h.md#af4110be6e09c80cd7362d9b2580243e7)#define BT\_HCI\_OP\_LE\_SET\_CONN\_CTE\_TX\_PARAMS BT\_OP(BT\_OGF\_LE, 0x0055) /\* 0x2055 \*/

[ 1790](structbt__hci__cp__le__set__conn__cte__tx__params.md)struct [bt\_hci\_cp\_le\_set\_conn\_cte\_tx\_params](structbt__hci__cp__le__set__conn__cte__tx__params.md) {

[ 1791](structbt__hci__cp__le__set__conn__cte__tx__params.md#ae0a482982d804ffd7d16ea2b413e538d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__set__conn__cte__tx__params.md#ae0a482982d804ffd7d16ea2b413e538d);

[ 1792](structbt__hci__cp__le__set__conn__cte__tx__params.md#ab47f852b476ac2c35fc0631180e19fb4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_types](structbt__hci__cp__le__set__conn__cte__tx__params.md#ab47f852b476ac2c35fc0631180e19fb4);

[ 1793](structbt__hci__cp__le__set__conn__cte__tx__params.md#a8f0e5ee74662056f00eaa3a8c72f6fc4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [switch\_pattern\_len](structbt__hci__cp__le__set__conn__cte__tx__params.md#a8f0e5ee74662056f00eaa3a8c72f6fc4);

[ 1794](structbt__hci__cp__le__set__conn__cte__tx__params.md#abff85d652b3b2fd55ad78e53887cd7ce) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ant\_ids](structbt__hci__cp__le__set__conn__cte__tx__params.md#abff85d652b3b2fd55ad78e53887cd7ce)[0];

1795} \_\_packed;

1796

[ 1797](structbt__hci__rp__le__set__conn__cte__tx__params.md)struct [bt\_hci\_rp\_le\_set\_conn\_cte\_tx\_params](structbt__hci__rp__le__set__conn__cte__tx__params.md) {

[ 1798](structbt__hci__rp__le__set__conn__cte__tx__params.md#a56f62b6d2c42cd22f73026a2fabc6986) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__set__conn__cte__tx__params.md#a56f62b6d2c42cd22f73026a2fabc6986);

[ 1799](structbt__hci__rp__le__set__conn__cte__tx__params.md#aad553d484daed7ca08de132f4fb849ee) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__set__conn__cte__tx__params.md#aad553d484daed7ca08de132f4fb849ee);

1800} \_\_packed;

1801

1802/\* Interval between consecutive CTE request procedure starts in number of connection events. \*/

[ 1803](hci__types_8h.md#ad9e1fa26a799b8730c17772482da7982)#define BT\_HCI\_REQUEST\_CTE\_ONCE 0x0

[ 1804](hci__types_8h.md#a13875ad8ac3a77759afdb4b6a76ad3e8)#define BT\_HCI\_REQUEST\_CTE\_INTERVAL\_MIN 0x1

[ 1805](hci__types_8h.md#a0a41f911f5f4b50b571c7f091393c7d8)#define BT\_HCI\_REQUEST\_CTE\_INTERVAL\_MAX 0xFFFF

1806

[ 1807](hci__types_8h.md#ae488ce598705cf60b78da985015bb42b)#define BT\_HCI\_OP\_LE\_CONN\_CTE\_REQ\_ENABLE BT\_OP(BT\_OGF\_LE, 0x0056) /\* 0x2056 \*/

[ 1808](structbt__hci__cp__le__conn__cte__req__enable.md)struct [bt\_hci\_cp\_le\_conn\_cte\_req\_enable](structbt__hci__cp__le__conn__cte__req__enable.md) {

[ 1809](structbt__hci__cp__le__conn__cte__req__enable.md#af340b3b97f9fb12c24baa38415620b44) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__conn__cte__req__enable.md#af340b3b97f9fb12c24baa38415620b44);

[ 1810](structbt__hci__cp__le__conn__cte__req__enable.md#aaf38e3d5664d81ae7ac8d3b1bb03c646) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enable](structbt__hci__cp__le__conn__cte__req__enable.md#aaf38e3d5664d81ae7ac8d3b1bb03c646);

[ 1811](structbt__hci__cp__le__conn__cte__req__enable.md#a956a1a8794b75e962d03cdcf81847cfc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cte\_request\_interval](structbt__hci__cp__le__conn__cte__req__enable.md#a956a1a8794b75e962d03cdcf81847cfc);

[ 1812](structbt__hci__cp__le__conn__cte__req__enable.md#a4d4e41bbe95457ce5e8ad68ffeb85200) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [requested\_cte\_length](structbt__hci__cp__le__conn__cte__req__enable.md#a4d4e41bbe95457ce5e8ad68ffeb85200);

[ 1813](structbt__hci__cp__le__conn__cte__req__enable.md#a5a7443a86e770de4bf7292d813e966e7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [requested\_cte\_type](structbt__hci__cp__le__conn__cte__req__enable.md#a5a7443a86e770de4bf7292d813e966e7);

1814} \_\_packed;

1815

[ 1816](structbt__hci__rp__le__conn__cte__req__enable.md)struct [bt\_hci\_rp\_le\_conn\_cte\_req\_enable](structbt__hci__rp__le__conn__cte__req__enable.md) {

[ 1817](structbt__hci__rp__le__conn__cte__req__enable.md#a1e76e7a6da194a433c1fa6ac2bc36b80) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__conn__cte__req__enable.md#a1e76e7a6da194a433c1fa6ac2bc36b80);

[ 1818](structbt__hci__rp__le__conn__cte__req__enable.md#af00adb07a144156a37fb5fc47ca61ccb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__conn__cte__req__enable.md#af00adb07a144156a37fb5fc47ca61ccb);

1819} \_\_packed;

1820

[ 1821](hci__types_8h.md#a150b54d69fb6fe9175336fadb7d81bb8)#define BT\_HCI\_OP\_LE\_CONN\_CTE\_RSP\_ENABLE BT\_OP(BT\_OGF\_LE, 0x0057) /\* 0x2057 \*/

[ 1822](structbt__hci__cp__le__conn__cte__rsp__enable.md)struct [bt\_hci\_cp\_le\_conn\_cte\_rsp\_enable](structbt__hci__cp__le__conn__cte__rsp__enable.md) {

[ 1823](structbt__hci__cp__le__conn__cte__rsp__enable.md#a9d78072143513020620e02a744d4fa9b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__conn__cte__rsp__enable.md#a9d78072143513020620e02a744d4fa9b);

[ 1824](structbt__hci__cp__le__conn__cte__rsp__enable.md#ae5eaaae211732d772ea53f3936ab32d2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enable](structbt__hci__cp__le__conn__cte__rsp__enable.md#ae5eaaae211732d772ea53f3936ab32d2);

1825} \_\_packed;

1826

[ 1827](structbt__hci__rp__le__conn__cte__rsp__enable.md)struct [bt\_hci\_rp\_le\_conn\_cte\_rsp\_enable](structbt__hci__rp__le__conn__cte__rsp__enable.md) {

[ 1828](structbt__hci__rp__le__conn__cte__rsp__enable.md#a8a21bc015408cc77c5d229cd77289dcc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__conn__cte__rsp__enable.md#a8a21bc015408cc77c5d229cd77289dcc);

[ 1829](structbt__hci__rp__le__conn__cte__rsp__enable.md#ab16f226d871d7d55c3f900614d59d8a1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__conn__cte__rsp__enable.md#ab16f226d871d7d55c3f900614d59d8a1);

1830} \_\_packed;

1831

[ 1832](hci__types_8h.md#a41aac54cd90cfc58990ce93124ce7077)#define BT\_HCI\_LE\_1US\_AOD\_TX BIT(0)

[ 1833](hci__types_8h.md#a70edcf0bd7e63454996ef5d925e91bbf)#define BT\_HCI\_LE\_1US\_AOD\_RX BIT(1)

[ 1834](hci__types_8h.md#a04a69a823bac190d0ac16f3c21481bde)#define BT\_HCI\_LE\_1US\_AOA\_RX BIT(2)

1835

[ 1836](hci__types_8h.md#a112d3fb3d3ec663278aa4463fedbd89b)#define BT\_HCI\_LE\_NUM\_ANT\_MIN 0x1

[ 1837](hci__types_8h.md#ad9ff685b2854b877e0cdd1ae93272ddf)#define BT\_HCI\_LE\_NUM\_ANT\_MAX 0x4B

1838

[ 1839](hci__types_8h.md#a327330c5b69e8ec56dd18fcc3fdf0622)#define BT\_HCI\_LE\_MAX\_SWITCH\_PATTERN\_LEN\_MIN 0x2

[ 1840](hci__types_8h.md#a647de996dd2e75a8242e6459abd565f6)#define BT\_HCI\_LE\_MAX\_SWITCH\_PATTERN\_LEN\_MAX 0x4B

1841

[ 1842](hci__types_8h.md#adee7271e25e6d66ba434502ab56674c3)#define BT\_HCI\_LE\_MAX\_CTE\_LEN\_MIN 0x2

[ 1843](hci__types_8h.md#af54ba281111d90f3edb77c0abf9c57b1)#define BT\_HCI\_LE\_MAX\_CTE\_LEN\_MAX 0x14

1844

[ 1845](hci__types_8h.md#aff3ea5f19135609d5553cacec0d700a6)#define BT\_HCI\_OP\_LE\_READ\_ANT\_INFO BT\_OP(BT\_OGF\_LE, 0x0058) /\* 0x2058 \*/

[ 1846](structbt__hci__rp__le__read__ant__info.md)struct [bt\_hci\_rp\_le\_read\_ant\_info](structbt__hci__rp__le__read__ant__info.md) {

[ 1847](structbt__hci__rp__le__read__ant__info.md#ae1388d3eee3085af7f2b0b57b2aa7b1e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__ant__info.md#ae1388d3eee3085af7f2b0b57b2aa7b1e);

[ 1848](structbt__hci__rp__le__read__ant__info.md#a2c78d3db239c9e00729d91834eb60f21) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [switch\_sample\_rates](structbt__hci__rp__le__read__ant__info.md#a2c78d3db239c9e00729d91834eb60f21);

[ 1849](structbt__hci__rp__le__read__ant__info.md#a1f79b45751d39ebb9349df93d0ff2e13) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_ant](structbt__hci__rp__le__read__ant__info.md#a1f79b45751d39ebb9349df93d0ff2e13);

[ 1850](structbt__hci__rp__le__read__ant__info.md#ae75fe0b9f5fe8c88a8e8482eef299348) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_switch\_pattern\_len](structbt__hci__rp__le__read__ant__info.md#ae75fe0b9f5fe8c88a8e8482eef299348);

[ 1851](structbt__hci__rp__le__read__ant__info.md#a625cc8fa8553eafbbb31cbc0b3f303c7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_cte\_len](structbt__hci__rp__le__read__ant__info.md#a625cc8fa8553eafbbb31cbc0b3f303c7);

1852};

1853

[ 1854](hci__types_8h.md#a1aaaffb3044bfd824aa6744867da0a97)#define BT\_HCI\_LE\_SET\_PER\_ADV\_RECV\_ENABLE\_ENABLE BIT(0)

[ 1855](hci__types_8h.md#a08fe0a16e8c1b3eb6b23869b37739f2d)#define BT\_HCI\_LE\_SET\_PER\_ADV\_RECV\_ENABLE\_FILTER\_DUPLICATE BIT(1)

1856

[ 1857](hci__types_8h.md#a047efb565b182e90178513dc3db6390f)#define BT\_HCI\_OP\_LE\_SET\_PER\_ADV\_RECV\_ENABLE BT\_OP(BT\_OGF\_LE, 0x0059) /\* 0x2059 \*/

[ 1858](structbt__hci__cp__le__set__per__adv__recv__enable.md)struct [bt\_hci\_cp\_le\_set\_per\_adv\_recv\_enable](structbt__hci__cp__le__set__per__adv__recv__enable.md) {

[ 1859](structbt__hci__cp__le__set__per__adv__recv__enable.md#a1e626eecf1d3f0820c3b2a13fd84b92f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__set__per__adv__recv__enable.md#a1e626eecf1d3f0820c3b2a13fd84b92f);

[ 1860](structbt__hci__cp__le__set__per__adv__recv__enable.md#a2187ec96822726daa5e43e910cc41cc3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enable](structbt__hci__cp__le__set__per__adv__recv__enable.md#a2187ec96822726daa5e43e910cc41cc3);

1861} \_\_packed;

1862

[ 1863](hci__types_8h.md#aa1d0bc8ccc0e1e8835938f8e8d87b7f1)#define BT\_HCI\_OP\_LE\_PER\_ADV\_SYNC\_TRANSFER BT\_OP(BT\_OGF\_LE, 0x005a) /\* 0x205a \*/

[ 1864](structbt__hci__cp__le__per__adv__sync__transfer.md)struct [bt\_hci\_cp\_le\_per\_adv\_sync\_transfer](structbt__hci__cp__le__per__adv__sync__transfer.md) {

[ 1865](structbt__hci__cp__le__per__adv__sync__transfer.md#a991f77d6f2f0c301fe3322050b2d359f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__cp__le__per__adv__sync__transfer.md#a991f77d6f2f0c301fe3322050b2d359f);

[ 1866](structbt__hci__cp__le__per__adv__sync__transfer.md#a1327de0f9b2ebd1eaa97b51850087460) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [service\_data](structbt__hci__cp__le__per__adv__sync__transfer.md#a1327de0f9b2ebd1eaa97b51850087460);

[ 1867](structbt__hci__cp__le__per__adv__sync__transfer.md#a38537b7f01a93f7a3e8cfcb92098a172) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sync\_handle](structbt__hci__cp__le__per__adv__sync__transfer.md#a38537b7f01a93f7a3e8cfcb92098a172);

1868} \_\_packed;

1869

[ 1870](structbt__hci__rp__le__per__adv__sync__transfer.md)struct [bt\_hci\_rp\_le\_per\_adv\_sync\_transfer](structbt__hci__rp__le__per__adv__sync__transfer.md) {

[ 1871](structbt__hci__rp__le__per__adv__sync__transfer.md#adb536c4694d2e7c5b91e9f68986e97e1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__per__adv__sync__transfer.md#adb536c4694d2e7c5b91e9f68986e97e1);

[ 1872](structbt__hci__rp__le__per__adv__sync__transfer.md#ab8b4357fd92e01a5f61d3127b04c0318) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__rp__le__per__adv__sync__transfer.md#ab8b4357fd92e01a5f61d3127b04c0318);

1873} \_\_packed;

1874

[ 1875](hci__types_8h.md#ab7d661097af4cc612ac6631b18bbc7e3)#define BT\_HCI\_OP\_LE\_PER\_ADV\_SET\_INFO\_TRANSFER BT\_OP(BT\_OGF\_LE, 0x005b) /\* 0x205b \*/

[ 1876](structbt__hci__cp__le__per__adv__set__info__transfer.md)struct [bt\_hci\_cp\_le\_per\_adv\_set\_info\_transfer](structbt__hci__cp__le__per__adv__set__info__transfer.md) {

[ 1877](structbt__hci__cp__le__per__adv__set__info__transfer.md#a3b2f0c510ef9b385cb42bf9a194fa574) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__cp__le__per__adv__set__info__transfer.md#a3b2f0c510ef9b385cb42bf9a194fa574);

[ 1878](structbt__hci__cp__le__per__adv__set__info__transfer.md#a5f14c3265bffdf3e30a554a3686e9e0c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [service\_data](structbt__hci__cp__le__per__adv__set__info__transfer.md#a5f14c3265bffdf3e30a554a3686e9e0c);

[ 1879](structbt__hci__cp__le__per__adv__set__info__transfer.md#a75b2c0fa1d50ef9d3761ac25f487750b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_handle](structbt__hci__cp__le__per__adv__set__info__transfer.md#a75b2c0fa1d50ef9d3761ac25f487750b);

1880} \_\_packed;

1881

[ 1882](structbt__hci__rp__le__per__adv__set__info__transfer.md)struct [bt\_hci\_rp\_le\_per\_adv\_set\_info\_transfer](structbt__hci__rp__le__per__adv__set__info__transfer.md) {

[ 1883](structbt__hci__rp__le__per__adv__set__info__transfer.md#ab1592bfadd45315ff47e86b7c50374ad) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__per__adv__set__info__transfer.md#ab1592bfadd45315ff47e86b7c50374ad);

[ 1884](structbt__hci__rp__le__per__adv__set__info__transfer.md#a696e5cab4d7507ea79b0e116c4bb92e2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__rp__le__per__adv__set__info__transfer.md#a696e5cab4d7507ea79b0e116c4bb92e2);

1885} \_\_packed;

1886

[ 1887](hci__types_8h.md#a65ff1c4a937422000f6f1eadea28ccba)#define BT\_HCI\_LE\_PAST\_MODE\_NO\_SYNC 0x00

[ 1888](hci__types_8h.md#ac7233f9c34f5e33d765b68b55ebc9b9e)#define BT\_HCI\_LE\_PAST\_MODE\_NO\_REPORTS 0x01

[ 1889](hci__types_8h.md#aaeac19606d3d5e7d0906b38e2c4b4c69)#define BT\_HCI\_LE\_PAST\_MODE\_SYNC 0x02

[ 1890](hci__types_8h.md#ab0232a2abc2b7c86b19ae89298ef8c4b)#define BT\_HCI\_LE\_PAST\_MODE\_SYNC\_FILTER\_DUPLICATES 0x03

1891

[ 1892](hci__types_8h.md#a3a3937965aeb187b6fb18da3b7731ed7)#define BT\_HCI\_LE\_PAST\_CTE\_TYPE\_NO\_AOA BIT(0)

[ 1893](hci__types_8h.md#a440aca4bf97bc6b583284ae6c8037a53)#define BT\_HCI\_LE\_PAST\_CTE\_TYPE\_NO\_AOD\_1US BIT(1)

[ 1894](hci__types_8h.md#ae2d9be5e54595cb5a426ae8909cdee1c)#define BT\_HCI\_LE\_PAST\_CTE\_TYPE\_NO\_AOD\_2US BIT(2)

[ 1895](hci__types_8h.md#af3d8cf0fb8af60c057ba8c24abaf3897)#define BT\_HCI\_LE\_PAST\_CTE\_TYPE\_NO\_CTE BIT(3)

[ 1896](hci__types_8h.md#a6fca2634e0e5b0dd5d86b18666ed38e4)#define BT\_HCI\_LE\_PAST\_CTE\_TYPE\_ONLY\_CTE BIT(4)

1897

[ 1898](hci__types_8h.md#a177ec628eac4a7d535cfe6c07123cb34)#define BT\_HCI\_OP\_LE\_PAST\_PARAM BT\_OP(BT\_OGF\_LE, 0x005c) /\* 0x205c \*/

[ 1899](structbt__hci__cp__le__past__param.md)struct [bt\_hci\_cp\_le\_past\_param](structbt__hci__cp__le__past__param.md) {

[ 1900](structbt__hci__cp__le__past__param.md#a9c99cdd5ae5de58960677781c2287c4d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__cp__le__past__param.md#a9c99cdd5ae5de58960677781c2287c4d);

[ 1901](structbt__hci__cp__le__past__param.md#aa36345a550dfabeef48b430d1a1b0030) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mode](structbt__hci__cp__le__past__param.md#aa36345a550dfabeef48b430d1a1b0030);

[ 1902](structbt__hci__cp__le__past__param.md#a622499d51e917f7828629de2291812e5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [skip](structbt__hci__cp__le__past__param.md#a622499d51e917f7828629de2291812e5);

[ 1903](structbt__hci__cp__le__past__param.md#aec9aa4ffe41c6b6f5cfcbc59eb57efca) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structbt__hci__cp__le__past__param.md#aec9aa4ffe41c6b6f5cfcbc59eb57efca);

[ 1904](structbt__hci__cp__le__past__param.md#a47c571ff27a59e0a7cbcb460303ee194) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__hci__cp__le__past__param.md#a47c571ff27a59e0a7cbcb460303ee194);

1905} \_\_packed;

1906

[ 1907](structbt__hci__rp__le__past__param.md)struct [bt\_hci\_rp\_le\_past\_param](structbt__hci__rp__le__past__param.md) {

[ 1908](structbt__hci__rp__le__past__param.md#a9630362b3d885b13869a4c0fe9e97b12) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__past__param.md#a9630362b3d885b13869a4c0fe9e97b12);

[ 1909](structbt__hci__rp__le__past__param.md#ae6b8a5d7e790516de2f91e41fd893111) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__rp__le__past__param.md#ae6b8a5d7e790516de2f91e41fd893111);

1910} \_\_packed;

1911

[ 1912](hci__types_8h.md#a650fe2941ffe238b16fd99ed5e78b25a)#define BT\_HCI\_OP\_LE\_DEFAULT\_PAST\_PARAM BT\_OP(BT\_OGF\_LE, 0x005d) /\* 0x205d \*/

[ 1913](structbt__hci__cp__le__default__past__param.md)struct [bt\_hci\_cp\_le\_default\_past\_param](structbt__hci__cp__le__default__past__param.md) {

[ 1914](structbt__hci__cp__le__default__past__param.md#a2ef92304264ad0bf1560accf306bb6d9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mode](structbt__hci__cp__le__default__past__param.md#a2ef92304264ad0bf1560accf306bb6d9);

[ 1915](structbt__hci__cp__le__default__past__param.md#a214cb0597d0065bc2c056fe9c51a2220) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [skip](structbt__hci__cp__le__default__past__param.md#a214cb0597d0065bc2c056fe9c51a2220);

[ 1916](structbt__hci__cp__le__default__past__param.md#a159f5245f86b27198264bdcf394d719f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structbt__hci__cp__le__default__past__param.md#a159f5245f86b27198264bdcf394d719f);

[ 1917](structbt__hci__cp__le__default__past__param.md#af18f679f5833c1d782b4e474af5d819c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__hci__cp__le__default__past__param.md#af18f679f5833c1d782b4e474af5d819c);

1918} \_\_packed;

1919

[ 1920](structbt__hci__rp__le__default__past__param.md)struct [bt\_hci\_rp\_le\_default\_past\_param](structbt__hci__rp__le__default__past__param.md) {

[ 1921](structbt__hci__rp__le__default__past__param.md#a292e2d655c77e8cda0d01fc07b43b8c4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__default__past__param.md#a292e2d655c77e8cda0d01fc07b43b8c4);

1922} \_\_packed;

1923

[ 1924](hci__types_8h.md#aa7e78541d152c21e101fab5a094c972f)#define BT\_HCI\_OP\_LE\_READ\_BUFFER\_SIZE\_V2 BT\_OP(BT\_OGF\_LE, 0x0060) /\* 0x2060 \*/

[ 1925](structbt__hci__rp__le__read__buffer__size__v2.md)struct [bt\_hci\_rp\_le\_read\_buffer\_size\_v2](structbt__hci__rp__le__read__buffer__size__v2.md) {

[ 1926](structbt__hci__rp__le__read__buffer__size__v2.md#a3b9cc0577d0f5f3c2b934a28915f2177) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__buffer__size__v2.md#a3b9cc0577d0f5f3c2b934a28915f2177);

[ 1927](structbt__hci__rp__le__read__buffer__size__v2.md#ac391149d3d7442e074aad4b98659bd02) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [acl\_max\_len](structbt__hci__rp__le__read__buffer__size__v2.md#ac391149d3d7442e074aad4b98659bd02);

[ 1928](structbt__hci__rp__le__read__buffer__size__v2.md#a1c7938defb076d973b8339c17cc930df) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [acl\_max\_num](structbt__hci__rp__le__read__buffer__size__v2.md#a1c7938defb076d973b8339c17cc930df);

[ 1929](structbt__hci__rp__le__read__buffer__size__v2.md#a9758d477c502575a1c176eb6a63e1a1a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [iso\_max\_len](structbt__hci__rp__le__read__buffer__size__v2.md#a9758d477c502575a1c176eb6a63e1a1a);

[ 1930](structbt__hci__rp__le__read__buffer__size__v2.md#ac3379adf42f9bbee8ae72fb4a7606fd1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [iso\_max\_num](structbt__hci__rp__le__read__buffer__size__v2.md#ac3379adf42f9bbee8ae72fb4a7606fd1);

1931} \_\_packed;

1932

[ 1933](hci__types_8h.md#acb7f49f17a60a4e29270c8719b7aeeed)#define BT\_HCI\_OP\_LE\_READ\_ISO\_TX\_SYNC BT\_OP(BT\_OGF\_LE, 0x0061) /\* 0x2061 \*/

[ 1934](structbt__hci__cp__le__read__iso__tx__sync.md)struct [bt\_hci\_cp\_le\_read\_iso\_tx\_sync](structbt__hci__cp__le__read__iso__tx__sync.md) {

[ 1935](structbt__hci__cp__le__read__iso__tx__sync.md#a8edc469f73540d4300b1716c96e17c9f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__read__iso__tx__sync.md#a8edc469f73540d4300b1716c96e17c9f);

1936} \_\_packed;

1937

[ 1938](structbt__hci__rp__le__read__iso__tx__sync.md)struct [bt\_hci\_rp\_le\_read\_iso\_tx\_sync](structbt__hci__rp__le__read__iso__tx__sync.md) {

[ 1939](structbt__hci__rp__le__read__iso__tx__sync.md#a188ef5dba77c754c46094135cc52641c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__iso__tx__sync.md#a188ef5dba77c754c46094135cc52641c);

[ 1940](structbt__hci__rp__le__read__iso__tx__sync.md#a8c0003043d3896b1ff93dc33dccc76b4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__read__iso__tx__sync.md#a8c0003043d3896b1ff93dc33dccc76b4);

[ 1941](structbt__hci__rp__le__read__iso__tx__sync.md#af2a02f68aa0a757757c490e707954952) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [seq](structbt__hci__rp__le__read__iso__tx__sync.md#af2a02f68aa0a757757c490e707954952);

[ 1942](structbt__hci__rp__le__read__iso__tx__sync.md#a35520a3e50afc03ed969b6c5ca9e15d9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timestamp](structbt__hci__rp__le__read__iso__tx__sync.md#a35520a3e50afc03ed969b6c5ca9e15d9);

[ 1943](structbt__hci__rp__le__read__iso__tx__sync.md#a29770c3172d5e45409392aa8ffc835ef) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [offset](structbt__hci__rp__le__read__iso__tx__sync.md#a29770c3172d5e45409392aa8ffc835ef)[3];

1944} \_\_packed;

1945

[ 1946](hci__types_8h.md#a18b5fef3eb5b947ce328e17c1e7db02d)#define BT\_HCI\_ISO\_CIG\_ID\_MAX 0xFE

[ 1947](hci__types_8h.md#a26c78a4b760b97682269e66dfe6f99df)#define BT\_HCI\_ISO\_CIS\_COUNT\_MAX 0x1F

[ 1948](hci__types_8h.md#a12e9af0e72013649da8afc7aa70a4e9c)#define BT\_HCI\_ISO\_SDU\_INTERVAL\_MIN 0x0000FF

[ 1949](hci__types_8h.md#aa75800427e808756fc7c6d30da57de37)#define BT\_HCI\_ISO\_SDU\_INTERVAL\_MAX 0x0FFFFF

[ 1950](hci__types_8h.md#a49f62e83dd51d17efd77c89337fdd537)#define BT\_HCI\_ISO\_WORST\_CASE\_SCA\_VALID\_MASK 0x07

[ 1951](hci__types_8h.md#aecaa88e04025e575c9bcda093f027400)#define BT\_HCI\_ISO\_PACKING\_VALID\_MASK 0x01

[ 1952](hci__types_8h.md#aaf4b4fc224c8b5cfdca663250eb29350)#define BT\_HCI\_ISO\_FRAMING\_VALID\_MASK 0x01

[ 1953](hci__types_8h.md#a8d044df1bfab8381b7e334597b303588)#define BT\_HCI\_ISO\_MAX\_TRANSPORT\_LATENCY\_MIN 0x0005

[ 1954](hci__types_8h.md#a9794f59f8d28879753b39bd504cf55be)#define BT\_HCI\_ISO\_MAX\_TRANSPORT\_LATENCY\_MAX 0x0FA0

[ 1955](hci__types_8h.md#a11e614cc72adb58bda2a2bdd5f4b36ef)#define BT\_HCI\_ISO\_CIS\_ID\_VALID\_MAX 0xEF

[ 1956](hci__types_8h.md#a9f3e990cadf1be179fcbac3f8ef74efe)#define BT\_HCI\_ISO\_MAX\_SDU\_VALID\_MASK 0x0FFF

[ 1957](hci__types_8h.md#ae055ed9714ca23bebd48bb399af04d83)#define BT\_HCI\_ISO\_PHY\_VALID\_MASK 0x07

[ 1958](hci__types_8h.md#a9d5e85ae1380fa85bae9d7e5e67aa0ae)#define BT\_HCI\_ISO\_INTERVAL\_MIN 0x0004

[ 1959](hci__types_8h.md#aaadbec2cc6adc2bb14d7117396023d06)#define BT\_HCI\_ISO\_INTERVAL\_MAX 0x0C80

1960

[ 1961](hci__types_8h.md#a0a4b2732026a6300d4b354eb6d93905d)#define BT\_HCI\_OP\_LE\_SET\_CIG\_PARAMS BT\_OP(BT\_OGF\_LE, 0x0062) /\* 0x2062 \*/

[ 1962](structbt__hci__cis__params.md)struct [bt\_hci\_cis\_params](structbt__hci__cis__params.md) {

[ 1963](structbt__hci__cis__params.md#a6dcfca11d7f827b1b7a62b507620d4de) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cis\_id](structbt__hci__cis__params.md#a6dcfca11d7f827b1b7a62b507620d4de);

[ 1964](structbt__hci__cis__params.md#a8a85b914ba5585c6b362da3deb8d42d9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [c\_sdu](structbt__hci__cis__params.md#a8a85b914ba5585c6b362da3deb8d42d9);

[ 1965](structbt__hci__cis__params.md#ae2bffbaf0c4dde9144a7887177b3ffdb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [p\_sdu](structbt__hci__cis__params.md#ae2bffbaf0c4dde9144a7887177b3ffdb);

[ 1966](structbt__hci__cis__params.md#a5a5fcd9276d912446fe84d875ae74c2f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_phy](structbt__hci__cis__params.md#a5a5fcd9276d912446fe84d875ae74c2f);

[ 1967](structbt__hci__cis__params.md#a18bc8e4b531d9fd16f18e10a0d931f6c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_phy](structbt__hci__cis__params.md#a18bc8e4b531d9fd16f18e10a0d931f6c);

[ 1968](structbt__hci__cis__params.md#aa7fa628692f959db63788c6580cc5c66) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_rtn](structbt__hci__cis__params.md#aa7fa628692f959db63788c6580cc5c66);

[ 1969](structbt__hci__cis__params.md#ad55e197ccb70c83fcd4c1c6ba485f468) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_rtn](structbt__hci__cis__params.md#ad55e197ccb70c83fcd4c1c6ba485f468);

1970} \_\_packed;

1971

[ 1972](structbt__hci__cp__le__set__cig__params.md)struct [bt\_hci\_cp\_le\_set\_cig\_params](structbt__hci__cp__le__set__cig__params.md) {

[ 1973](structbt__hci__cp__le__set__cig__params.md#a7dbf75c6ed92a053c4ec0d8f7268c92e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cig\_id](structbt__hci__cp__le__set__cig__params.md#a7dbf75c6ed92a053c4ec0d8f7268c92e);

[ 1974](structbt__hci__cp__le__set__cig__params.md#a14f5c0cf7f99ab406714501038048035) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_interval](structbt__hci__cp__le__set__cig__params.md#a14f5c0cf7f99ab406714501038048035)[3];

[ 1975](structbt__hci__cp__le__set__cig__params.md#a50a260a15f3a0ceae716da6c04c5b768) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_interval](structbt__hci__cp__le__set__cig__params.md#a50a260a15f3a0ceae716da6c04c5b768)[3];

[ 1976](structbt__hci__cp__le__set__cig__params.md#a46a657cdfbc7a49e6761d9f18d980c2a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sca](structbt__hci__cp__le__set__cig__params.md#a46a657cdfbc7a49e6761d9f18d980c2a);

[ 1977](structbt__hci__cp__le__set__cig__params.md#a79fc069492741f14f348650abef4c66b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packing](structbt__hci__cp__le__set__cig__params.md#a79fc069492741f14f348650abef4c66b);

[ 1978](structbt__hci__cp__le__set__cig__params.md#a867bf5ddbcadd27dbec2c3059d67d6d6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [framing](structbt__hci__cp__le__set__cig__params.md#a867bf5ddbcadd27dbec2c3059d67d6d6);

[ 1979](structbt__hci__cp__le__set__cig__params.md#afec8ebd17cc6ca5b3d13ef54f406df62) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [c\_latency](structbt__hci__cp__le__set__cig__params.md#afec8ebd17cc6ca5b3d13ef54f406df62);

[ 1980](structbt__hci__cp__le__set__cig__params.md#a810822396b97d54988ec57561b4ee7d5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [p\_latency](structbt__hci__cp__le__set__cig__params.md#a810822396b97d54988ec57561b4ee7d5);

[ 1981](structbt__hci__cp__le__set__cig__params.md#adf468a8a195447a7bbed4dcd53d287f6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_cis](structbt__hci__cp__le__set__cig__params.md#adf468a8a195447a7bbed4dcd53d287f6);

[ 1982](structbt__hci__cp__le__set__cig__params.md#ac922e59065920421f40468754d2ba5a2) struct [bt\_hci\_cis\_params](structbt__hci__cis__params.md) [cis](structbt__hci__cp__le__set__cig__params.md#ac922e59065920421f40468754d2ba5a2)[0];

1983} \_\_packed;

1984

[ 1985](structbt__hci__rp__le__set__cig__params.md)struct [bt\_hci\_rp\_le\_set\_cig\_params](structbt__hci__rp__le__set__cig__params.md) {

[ 1986](structbt__hci__rp__le__set__cig__params.md#a8426a2b9927bee05fb9a46b4b261c743) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__set__cig__params.md#a8426a2b9927bee05fb9a46b4b261c743);

[ 1987](structbt__hci__rp__le__set__cig__params.md#a951dc88e0cde4e1f0274684498741eac) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cig\_id](structbt__hci__rp__le__set__cig__params.md#a951dc88e0cde4e1f0274684498741eac);

[ 1988](structbt__hci__rp__le__set__cig__params.md#a8aff643e0ae41455eb9391cfdb45ebda) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_handles](structbt__hci__rp__le__set__cig__params.md#a8aff643e0ae41455eb9391cfdb45ebda);

[ 1989](structbt__hci__rp__le__set__cig__params.md#a2e95c6217d11169a8a611ea95dce70b6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__set__cig__params.md#a2e95c6217d11169a8a611ea95dce70b6)[0];

1990} \_\_packed;

1991

[ 1992](hci__types_8h.md#a54df2d12a0c07bab9fb3521dc69ff2f4)#define BT\_HCI\_OP\_LE\_SET\_CIG\_PARAMS\_TEST BT\_OP(BT\_OGF\_LE, 0x0063) /\* 0x2063 \*/

[ 1993](structbt__hci__cis__params__test.md)struct [bt\_hci\_cis\_params\_test](structbt__hci__cis__params__test.md) {

[ 1994](structbt__hci__cis__params__test.md#a0a215b4dffac2aae4ae4310c54de073e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cis\_id](structbt__hci__cis__params__test.md#a0a215b4dffac2aae4ae4310c54de073e);

[ 1995](structbt__hci__cis__params__test.md#ad0cc6d393a536cb3cd83d456b950fc52) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [nse](structbt__hci__cis__params__test.md#ad0cc6d393a536cb3cd83d456b950fc52);

[ 1996](structbt__hci__cis__params__test.md#a98a120efb1495dd90858bef45eb95891) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [c\_sdu](structbt__hci__cis__params__test.md#a98a120efb1495dd90858bef45eb95891);

[ 1997](structbt__hci__cis__params__test.md#aefeca493efe0141590570e8a44bb8f8d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [p\_sdu](structbt__hci__cis__params__test.md#aefeca493efe0141590570e8a44bb8f8d);

[ 1998](structbt__hci__cis__params__test.md#adc092a44b58bcc78f3dfe88528ca724c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [c\_pdu](structbt__hci__cis__params__test.md#adc092a44b58bcc78f3dfe88528ca724c);

[ 1999](structbt__hci__cis__params__test.md#abce4bd6045642b4d29668865655f1548) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [p\_pdu](structbt__hci__cis__params__test.md#abce4bd6045642b4d29668865655f1548);

[ 2000](structbt__hci__cis__params__test.md#aa7ba56fb91718d43ca30ff643757e08e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_phy](structbt__hci__cis__params__test.md#aa7ba56fb91718d43ca30ff643757e08e);

[ 2001](structbt__hci__cis__params__test.md#ab636126046023a329451673c57b4ce96) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_phy](structbt__hci__cis__params__test.md#ab636126046023a329451673c57b4ce96);

[ 2002](structbt__hci__cis__params__test.md#adf5dda2be46f3c2c1a1fe398672416ff) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_bn](structbt__hci__cis__params__test.md#adf5dda2be46f3c2c1a1fe398672416ff);

[ 2003](structbt__hci__cis__params__test.md#ac66b7183d8148250246f17a157dc3d29) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_bn](structbt__hci__cis__params__test.md#ac66b7183d8148250246f17a157dc3d29);

2004} \_\_packed;

2005

[ 2006](structbt__hci__cp__le__set__cig__params__test.md)struct [bt\_hci\_cp\_le\_set\_cig\_params\_test](structbt__hci__cp__le__set__cig__params__test.md) {

[ 2007](structbt__hci__cp__le__set__cig__params__test.md#a161ae960cbd4f7833815285d04f87e46) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cig\_id](structbt__hci__cp__le__set__cig__params__test.md#a161ae960cbd4f7833815285d04f87e46);

[ 2008](structbt__hci__cp__le__set__cig__params__test.md#aa392cbac058beefd0e410fcc9821a0c3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_interval](structbt__hci__cp__le__set__cig__params__test.md#aa392cbac058beefd0e410fcc9821a0c3)[3];

[ 2009](structbt__hci__cp__le__set__cig__params__test.md#a0cf0f3f7c10b29d74ab64aa30a4969de) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_interval](structbt__hci__cp__le__set__cig__params__test.md#a0cf0f3f7c10b29d74ab64aa30a4969de)[3];

[ 2010](structbt__hci__cp__le__set__cig__params__test.md#a1eae50a97188304852589fd95e994150) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_ft](structbt__hci__cp__le__set__cig__params__test.md#a1eae50a97188304852589fd95e994150);

[ 2011](structbt__hci__cp__le__set__cig__params__test.md#af2ed1bf1a6beaff884c3ce3faf26bfb2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_ft](structbt__hci__cp__le__set__cig__params__test.md#af2ed1bf1a6beaff884c3ce3faf26bfb2);

[ 2012](structbt__hci__cp__le__set__cig__params__test.md#aa77765d90fde67c52e4f2d483f0a3ee0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [iso\_interval](structbt__hci__cp__le__set__cig__params__test.md#aa77765d90fde67c52e4f2d483f0a3ee0);

[ 2013](structbt__hci__cp__le__set__cig__params__test.md#a1d060539ff26677c1326a6ed3394fb6e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sca](structbt__hci__cp__le__set__cig__params__test.md#a1d060539ff26677c1326a6ed3394fb6e);

[ 2014](structbt__hci__cp__le__set__cig__params__test.md#a7275312e8b1c8ebc2af7992f765b392c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packing](structbt__hci__cp__le__set__cig__params__test.md#a7275312e8b1c8ebc2af7992f765b392c);

[ 2015](structbt__hci__cp__le__set__cig__params__test.md#a2cb6745b8f908cd2e7d5f12a092c3b69) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [framing](structbt__hci__cp__le__set__cig__params__test.md#a2cb6745b8f908cd2e7d5f12a092c3b69);

[ 2016](structbt__hci__cp__le__set__cig__params__test.md#a50c345ef03c669f476e143728f42cd6d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_cis](structbt__hci__cp__le__set__cig__params__test.md#a50c345ef03c669f476e143728f42cd6d);

[ 2017](structbt__hci__cp__le__set__cig__params__test.md#a5e07eb0d7d13e57be457d1b77a5dba12) struct [bt\_hci\_cis\_params\_test](structbt__hci__cis__params__test.md) [cis](structbt__hci__cp__le__set__cig__params__test.md#a5e07eb0d7d13e57be457d1b77a5dba12)[0];

2018} \_\_packed;

2019

[ 2020](structbt__hci__rp__le__set__cig__params__test.md)struct [bt\_hci\_rp\_le\_set\_cig\_params\_test](structbt__hci__rp__le__set__cig__params__test.md) {

[ 2021](structbt__hci__rp__le__set__cig__params__test.md#a932eadb4d750f79b4a7a9c3feb90fdcd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__set__cig__params__test.md#a932eadb4d750f79b4a7a9c3feb90fdcd);

[ 2022](structbt__hci__rp__le__set__cig__params__test.md#a65c11059bc00244e58d2ab8373e3e725) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cig\_id](structbt__hci__rp__le__set__cig__params__test.md#a65c11059bc00244e58d2ab8373e3e725);

[ 2023](structbt__hci__rp__le__set__cig__params__test.md#a10816d0875092c8e6bd4b13b819c43c7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_handles](structbt__hci__rp__le__set__cig__params__test.md#a10816d0875092c8e6bd4b13b819c43c7);

[ 2024](structbt__hci__rp__le__set__cig__params__test.md#a08b07863ed63ab627401c0c80bc3c7b4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__set__cig__params__test.md#a08b07863ed63ab627401c0c80bc3c7b4)[0];

2025} \_\_packed;

2026

[ 2027](hci__types_8h.md#a63c9af35a55d9b1ed1b253d057657608)#define BT\_HCI\_OP\_LE\_CREATE\_CIS BT\_OP(BT\_OGF\_LE, 0x0064) /\* 0x2064 \*/

[ 2028](structbt__hci__cis.md)struct [bt\_hci\_cis](structbt__hci__cis.md) {

[ 2029](structbt__hci__cis.md#a84165d526c10a91fa42d306276d97c74) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cis\_handle](structbt__hci__cis.md#a84165d526c10a91fa42d306276d97c74);

[ 2030](structbt__hci__cis.md#a754c3c75c0ad13a11d89fa3347112e2c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [acl\_handle](structbt__hci__cis.md#a754c3c75c0ad13a11d89fa3347112e2c);

2031} \_\_packed;

2032

[ 2033](structbt__hci__cp__le__create__cis.md)struct [bt\_hci\_cp\_le\_create\_cis](structbt__hci__cp__le__create__cis.md) {

[ 2034](structbt__hci__cp__le__create__cis.md#acd348a7d68947af8e7119b2e1a864481) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_cis](structbt__hci__cp__le__create__cis.md#acd348a7d68947af8e7119b2e1a864481);

[ 2035](structbt__hci__cp__le__create__cis.md#a5a323d09df7813fc9b834cc1d205d101) struct [bt\_hci\_cis](structbt__hci__cis.md) [cis](structbt__hci__cp__le__create__cis.md#a5a323d09df7813fc9b834cc1d205d101)[0];

2036} \_\_packed;

2037

[ 2038](hci__types_8h.md#ab623f680f2031fc03bd73199ebbf4e4e)#define BT\_HCI\_OP\_LE\_REMOVE\_CIG BT\_OP(BT\_OGF\_LE, 0x0065) /\* 0x2065 \*/

[ 2039](structbt__hci__cp__le__remove__cig.md)struct [bt\_hci\_cp\_le\_remove\_cig](structbt__hci__cp__le__remove__cig.md) {

[ 2040](structbt__hci__cp__le__remove__cig.md#addf395d945f14afbf2d39fa4d0d22f31) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cig\_id](structbt__hci__cp__le__remove__cig.md#addf395d945f14afbf2d39fa4d0d22f31);

2041} \_\_packed;

2042

[ 2043](structbt__hci__rp__le__remove__cig.md)struct [bt\_hci\_rp\_le\_remove\_cig](structbt__hci__rp__le__remove__cig.md) {

[ 2044](structbt__hci__rp__le__remove__cig.md#a1335f26f1dc67ff8e2a1960d1b24b1a0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__remove__cig.md#a1335f26f1dc67ff8e2a1960d1b24b1a0);

[ 2045](structbt__hci__rp__le__remove__cig.md#a82e74fbbce714b035b1e53fd5f1b09b5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cig\_id](structbt__hci__rp__le__remove__cig.md#a82e74fbbce714b035b1e53fd5f1b09b5);

2046} \_\_packed;

2047

[ 2048](hci__types_8h.md#ade7635c85588941a2e628639be06ce7b)#define BT\_HCI\_OP\_LE\_ACCEPT\_CIS BT\_OP(BT\_OGF\_LE, 0x0066) /\* 0x2066 \*/

[ 2049](structbt__hci__cp__le__accept__cis.md)struct [bt\_hci\_cp\_le\_accept\_cis](structbt__hci__cp__le__accept__cis.md) {

[ 2050](structbt__hci__cp__le__accept__cis.md#aec6a6c80403d5827df10cd8722bc12e4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__accept__cis.md#aec6a6c80403d5827df10cd8722bc12e4);

2051} \_\_packed;

2052

[ 2053](hci__types_8h.md#a6c58ebc2082de8c2c3aafd9ee77dfd11)#define BT\_HCI\_OP\_LE\_REJECT\_CIS BT\_OP(BT\_OGF\_LE, 0x0067) /\* 0x2067 \*/

[ 2054](structbt__hci__cp__le__reject__cis.md)struct [bt\_hci\_cp\_le\_reject\_cis](structbt__hci__cp__le__reject__cis.md) {

[ 2055](structbt__hci__cp__le__reject__cis.md#ad697d740bdf5a565090a548e7e8fd399) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__reject__cis.md#ad697d740bdf5a565090a548e7e8fd399);

[ 2056](structbt__hci__cp__le__reject__cis.md#aec5bd3e4d27b6e3a2653112b36a3d128) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reason](structbt__hci__cp__le__reject__cis.md#aec5bd3e4d27b6e3a2653112b36a3d128);

2057} \_\_packed;

2058

[ 2059](structbt__hci__rp__le__reject__cis.md)struct [bt\_hci\_rp\_le\_reject\_cis](structbt__hci__rp__le__reject__cis.md) {

[ 2060](structbt__hci__rp__le__reject__cis.md#af2dc8a839d3e19821ab8ec0d3dc427ec) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__reject__cis.md#af2dc8a839d3e19821ab8ec0d3dc427ec);

[ 2061](structbt__hci__rp__le__reject__cis.md#acd8311e13bdfd7edb2d404d80006f9d4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__reject__cis.md#acd8311e13bdfd7edb2d404d80006f9d4);

2062} \_\_packed;

2063

[ 2064](hci__types_8h.md#a2a57bb6089e3a064e62119188b555ba9)#define BT\_HCI\_OP\_LE\_CREATE\_BIG BT\_OP(BT\_OGF\_LE, 0x0068) /\* 0x2068 \*/

[ 2065](structbt__hci__cp__le__create__big.md)struct [bt\_hci\_cp\_le\_create\_big](structbt__hci__cp__le__create__big.md) {

[ 2066](structbt__hci__cp__le__create__big.md#af5412e4a69c05a09b2e818322636a98a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [big\_handle](structbt__hci__cp__le__create__big.md#af5412e4a69c05a09b2e818322636a98a);

[ 2067](structbt__hci__cp__le__create__big.md#aa686eec31ca4c831262dd34d41f9a1fb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_handle](structbt__hci__cp__le__create__big.md#aa686eec31ca4c831262dd34d41f9a1fb);

[ 2068](structbt__hci__cp__le__create__big.md#ad8491c970417e63c6a98c12278a89c86) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_bis](structbt__hci__cp__le__create__big.md#ad8491c970417e63c6a98c12278a89c86);

[ 2069](structbt__hci__cp__le__create__big.md#a2960a9891b827529c9fa1b68a747e2d5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sdu\_interval](structbt__hci__cp__le__create__big.md#a2960a9891b827529c9fa1b68a747e2d5)[3];

[ 2070](structbt__hci__cp__le__create__big.md#a06fd74e9a5f172060835524da5851c71) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_sdu](structbt__hci__cp__le__create__big.md#a06fd74e9a5f172060835524da5851c71);

[ 2071](structbt__hci__cp__le__create__big.md#a15018e5ebc124bbe90644b38fe3e7e76) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_latency](structbt__hci__cp__le__create__big.md#a15018e5ebc124bbe90644b38fe3e7e76);

[ 2072](structbt__hci__cp__le__create__big.md#a1cb0dd106bf4a1a0c473333d089c95e7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rtn](structbt__hci__cp__le__create__big.md#a1cb0dd106bf4a1a0c473333d089c95e7);

[ 2073](structbt__hci__cp__le__create__big.md#a56cb773a03e4927c3b6bf4d2a6ed6ed9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__cp__le__create__big.md#a56cb773a03e4927c3b6bf4d2a6ed6ed9);

[ 2074](structbt__hci__cp__le__create__big.md#ac027390db21320fb9d1002161c4c2f67) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packing](structbt__hci__cp__le__create__big.md#ac027390db21320fb9d1002161c4c2f67);

[ 2075](structbt__hci__cp__le__create__big.md#a330916d60c05ec2ef7a71933b62c203a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [framing](structbt__hci__cp__le__create__big.md#a330916d60c05ec2ef7a71933b62c203a);

[ 2076](structbt__hci__cp__le__create__big.md#a490bd68d137f8cf60ea2ccd5ea4495e9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [encryption](structbt__hci__cp__le__create__big.md#a490bd68d137f8cf60ea2ccd5ea4495e9);

[ 2077](structbt__hci__cp__le__create__big.md#a0b4b2d77cd0f579aab190336b14597c5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bcode](structbt__hci__cp__le__create__big.md#a0b4b2d77cd0f579aab190336b14597c5)[16];

2078} \_\_packed;

2079

[ 2080](hci__types_8h.md#ad0f1ae4be3f5bb90ef967d88dcaaf353)#define BT\_HCI\_OP\_LE\_CREATE\_BIG\_TEST BT\_OP(BT\_OGF\_LE, 0x0069) /\* 0x2069 \*/

[ 2081](structbt__hci__cp__le__create__big__test.md)struct [bt\_hci\_cp\_le\_create\_big\_test](structbt__hci__cp__le__create__big__test.md) {

[ 2082](structbt__hci__cp__le__create__big__test.md#ac202f5cee0c1d0456b200606860fd5ab) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [big\_handle](structbt__hci__cp__le__create__big__test.md#ac202f5cee0c1d0456b200606860fd5ab);

[ 2083](structbt__hci__cp__le__create__big__test.md#aece09ae6264e0cc1a5548f1603a3f61a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_handle](structbt__hci__cp__le__create__big__test.md#aece09ae6264e0cc1a5548f1603a3f61a);

[ 2084](structbt__hci__cp__le__create__big__test.md#a6ce270f0afd185c44fa5a2c67a7783fb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_bis](structbt__hci__cp__le__create__big__test.md#a6ce270f0afd185c44fa5a2c67a7783fb);

[ 2085](structbt__hci__cp__le__create__big__test.md#a331b1a8ef66804cf20d6681e1bc5aefb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sdu\_interval](structbt__hci__cp__le__create__big__test.md#a331b1a8ef66804cf20d6681e1bc5aefb)[3];

[ 2086](structbt__hci__cp__le__create__big__test.md#a6475ae77af80e89bb65596bc6f907a58) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [iso\_interval](structbt__hci__cp__le__create__big__test.md#a6475ae77af80e89bb65596bc6f907a58);

[ 2087](structbt__hci__cp__le__create__big__test.md#a402c19da1ecf273bc942ecc560730567) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [nse](structbt__hci__cp__le__create__big__test.md#a402c19da1ecf273bc942ecc560730567);

[ 2088](structbt__hci__cp__le__create__big__test.md#a7ebbc81306109e035f89154738900395) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_sdu](structbt__hci__cp__le__create__big__test.md#a7ebbc81306109e035f89154738900395);

[ 2089](structbt__hci__cp__le__create__big__test.md#a2652e0f340f13635a5da6335ec43e801) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_pdu](structbt__hci__cp__le__create__big__test.md#a2652e0f340f13635a5da6335ec43e801);

[ 2090](structbt__hci__cp__le__create__big__test.md#a731ca2f90c17a4f3f868660e51649ce6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__cp__le__create__big__test.md#a731ca2f90c17a4f3f868660e51649ce6);

[ 2091](structbt__hci__cp__le__create__big__test.md#a49822f8e1617e30aab9b0d7d790697a3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packing](structbt__hci__cp__le__create__big__test.md#a49822f8e1617e30aab9b0d7d790697a3);

[ 2092](structbt__hci__cp__le__create__big__test.md#acc5b2c30db0c7642d12019f8241dab26) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [framing](structbt__hci__cp__le__create__big__test.md#acc5b2c30db0c7642d12019f8241dab26);

[ 2093](structbt__hci__cp__le__create__big__test.md#a734174187486ac760b8bf0e566166842) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bn](structbt__hci__cp__le__create__big__test.md#a734174187486ac760b8bf0e566166842);

[ 2094](structbt__hci__cp__le__create__big__test.md#a66ce7ba0498053a588de9097cbbc0891) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [irc](structbt__hci__cp__le__create__big__test.md#a66ce7ba0498053a588de9097cbbc0891);

[ 2095](structbt__hci__cp__le__create__big__test.md#a2f2eaa258463dd51a9f6042e75ecfec6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pto](structbt__hci__cp__le__create__big__test.md#a2f2eaa258463dd51a9f6042e75ecfec6);

[ 2096](structbt__hci__cp__le__create__big__test.md#a50c4308abda01581b436b7867304e982) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [encryption](structbt__hci__cp__le__create__big__test.md#a50c4308abda01581b436b7867304e982);

[ 2097](structbt__hci__cp__le__create__big__test.md#a333319a03d2087067247c4f5e595b4e5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bcode](structbt__hci__cp__le__create__big__test.md#a333319a03d2087067247c4f5e595b4e5)[16];

2098} \_\_packed;

2099

[ 2100](hci__types_8h.md#acc5e6c17e33cf43f2a68cb93bb09ef20)#define BT\_HCI\_OP\_LE\_TERMINATE\_BIG BT\_OP(BT\_OGF\_LE, 0x006a) /\* 0x206a \*/

[ 2101](structbt__hci__cp__le__terminate__big.md)struct [bt\_hci\_cp\_le\_terminate\_big](structbt__hci__cp__le__terminate__big.md) {

[ 2102](structbt__hci__cp__le__terminate__big.md#acb5fb9451cf890245a85704579b1d1c8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [big\_handle](structbt__hci__cp__le__terminate__big.md#acb5fb9451cf890245a85704579b1d1c8);

[ 2103](structbt__hci__cp__le__terminate__big.md#a958ab6b2f2bb30c825060498e6917a18) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reason](structbt__hci__cp__le__terminate__big.md#a958ab6b2f2bb30c825060498e6917a18);

2104} \_\_packed;

2105

[ 2106](hci__types_8h.md#a47af328ede7f14e3d78c81de609af1c9)#define BT\_HCI\_OP\_LE\_BIG\_CREATE\_SYNC BT\_OP(BT\_OGF\_LE, 0x006b) /\* 0x206b \*/

[ 2107](structbt__hci__cp__le__big__create__sync.md)struct [bt\_hci\_cp\_le\_big\_create\_sync](structbt__hci__cp__le__big__create__sync.md) {

[ 2108](structbt__hci__cp__le__big__create__sync.md#a6692dae077ce1ce4f31bc94b9d391afd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [big\_handle](structbt__hci__cp__le__big__create__sync.md#a6692dae077ce1ce4f31bc94b9d391afd);

[ 2109](structbt__hci__cp__le__big__create__sync.md#a70b031f24cdf231e5c168b155517eae0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sync\_handle](structbt__hci__cp__le__big__create__sync.md#a70b031f24cdf231e5c168b155517eae0);

[ 2110](structbt__hci__cp__le__big__create__sync.md#a482edf3326e2dd720b14a03609c1256a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [encryption](structbt__hci__cp__le__big__create__sync.md#a482edf3326e2dd720b14a03609c1256a);

[ 2111](structbt__hci__cp__le__big__create__sync.md#a053475c3af12e6e37dc4befcf634d68f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bcode](structbt__hci__cp__le__big__create__sync.md#a053475c3af12e6e37dc4befcf634d68f)[16];

[ 2112](structbt__hci__cp__le__big__create__sync.md#a37050e3eb914ff06495695d44c3fdb50) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mse](structbt__hci__cp__le__big__create__sync.md#a37050e3eb914ff06495695d44c3fdb50);

[ 2113](structbt__hci__cp__le__big__create__sync.md#a55e83bc3722ce2dbf943879a80ef2872) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sync\_timeout](structbt__hci__cp__le__big__create__sync.md#a55e83bc3722ce2dbf943879a80ef2872);

[ 2114](structbt__hci__cp__le__big__create__sync.md#a7efae2c8dc46d13fb2abca677ac152b0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_bis](structbt__hci__cp__le__big__create__sync.md#a7efae2c8dc46d13fb2abca677ac152b0);

[ 2115](structbt__hci__cp__le__big__create__sync.md#a6d1050c2a0522be215d82d3874fed4b6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bis](structbt__hci__cp__le__big__create__sync.md#a6d1050c2a0522be215d82d3874fed4b6)[0];

2116} \_\_packed;

2117

[ 2118](hci__types_8h.md#aa7576f4ab30ec7985b4afd08a08800d2)#define BT\_HCI\_OP\_LE\_BIG\_TERMINATE\_SYNC BT\_OP(BT\_OGF\_LE, 0x006c) /\* 0x206c \*/

[ 2119](structbt__hci__cp__le__big__terminate__sync.md)struct [bt\_hci\_cp\_le\_big\_terminate\_sync](structbt__hci__cp__le__big__terminate__sync.md) {

[ 2120](structbt__hci__cp__le__big__terminate__sync.md#ad7e4de2a9a3222c1bb8fa048cacd06fa) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [big\_handle](structbt__hci__cp__le__big__terminate__sync.md#ad7e4de2a9a3222c1bb8fa048cacd06fa);

2121} \_\_packed;

2122

[ 2123](structbt__hci__rp__le__big__terminate__sync.md)struct [bt\_hci\_rp\_le\_big\_terminate\_sync](structbt__hci__rp__le__big__terminate__sync.md) {

[ 2124](structbt__hci__rp__le__big__terminate__sync.md#ad4d1d4238402ef829a1ff9ed3b1dc050) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__big__terminate__sync.md#ad4d1d4238402ef829a1ff9ed3b1dc050);

[ 2125](structbt__hci__rp__le__big__terminate__sync.md#a741ab80e08e7ecfc5a0158ec0cf14654) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [big\_handle](structbt__hci__rp__le__big__terminate__sync.md#a741ab80e08e7ecfc5a0158ec0cf14654);

2126} \_\_packed;

2127

[ 2128](hci__types_8h.md#a0057468b1638b07f799b62a24cd096d9)#define BT\_HCI\_OP\_LE\_REQ\_PEER\_SC BT\_OP(BT\_OGF\_LE, 0x006d) /\* 0x206d \*/

[ 2129](structbt__hci__cp__le__req__peer__sca.md)struct [bt\_hci\_cp\_le\_req\_peer\_sca](structbt__hci__cp__le__req__peer__sca.md) {

[ 2130](structbt__hci__cp__le__req__peer__sca.md#a39d65681da55b26f2900f06cde637d88) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__req__peer__sca.md#a39d65681da55b26f2900f06cde637d88);

2131} \_\_packed;

2132

[ 2133](hci__types_8h.md#a97de1164704f5d3c517b9c2ff6b0584a)#define BT\_HCI\_OP\_LE\_SETUP\_ISO\_PATH BT\_OP(BT\_OGF\_LE, 0x006e) /\* 0x206e \*/

[ 2134](structbt__hci__cp__le__setup__iso__path.md)struct [bt\_hci\_cp\_le\_setup\_iso\_path](structbt__hci__cp__le__setup__iso__path.md) {

[ 2135](structbt__hci__cp__le__setup__iso__path.md#a0054fede0e583cef0dbcf6ef3134e480) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__setup__iso__path.md#a0054fede0e583cef0dbcf6ef3134e480);

[ 2136](structbt__hci__cp__le__setup__iso__path.md#a89c1324359a4fc2f10fee9ebbac5cf2b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [path\_dir](structbt__hci__cp__le__setup__iso__path.md#a89c1324359a4fc2f10fee9ebbac5cf2b);

[ 2137](structbt__hci__cp__le__setup__iso__path.md#a7c07d69b2005af1f7f2618f2bfa60d50) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [path\_id](structbt__hci__cp__le__setup__iso__path.md#a7c07d69b2005af1f7f2618f2bfa60d50);

[ 2138](structbt__hci__cp__le__setup__iso__path.md#a5256fc99b362e3a5f986ef2b71b29ccb) struct [bt\_hci\_cp\_codec\_id](structbt__hci__cp__codec__id.md) [codec\_id](structbt__hci__cp__le__setup__iso__path.md#a5256fc99b362e3a5f986ef2b71b29ccb);

[ 2139](structbt__hci__cp__le__setup__iso__path.md#a31948436e6608f9943d34ce89a65c64c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [controller\_delay](structbt__hci__cp__le__setup__iso__path.md#a31948436e6608f9943d34ce89a65c64c)[3];

[ 2140](structbt__hci__cp__le__setup__iso__path.md#a1a816d8e8c434a05ea897b74bc4d89c7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [codec\_config\_len](structbt__hci__cp__le__setup__iso__path.md#a1a816d8e8c434a05ea897b74bc4d89c7);

[ 2141](structbt__hci__cp__le__setup__iso__path.md#ade4dee947e3d288f769d2d69fc57f96a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [codec\_config](structbt__hci__cp__le__setup__iso__path.md#ade4dee947e3d288f769d2d69fc57f96a)[0];

2142} \_\_packed;

2143

[ 2144](structbt__hci__rp__le__setup__iso__path.md)struct [bt\_hci\_rp\_le\_setup\_iso\_path](structbt__hci__rp__le__setup__iso__path.md) {

[ 2145](structbt__hci__rp__le__setup__iso__path.md#adde60b0dc6ec3d8caccae1d55d78d9a4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__setup__iso__path.md#adde60b0dc6ec3d8caccae1d55d78d9a4);

[ 2146](structbt__hci__rp__le__setup__iso__path.md#aa8effdcc4ba155b840ef789f20bad19e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__setup__iso__path.md#aa8effdcc4ba155b840ef789f20bad19e);

2147} \_\_packed;

2148

[ 2149](hci__types_8h.md#addec65d76f67f07c029216435cf117c6)#define BT\_HCI\_OP\_LE\_REMOVE\_ISO\_PATH BT\_OP(BT\_OGF\_LE, 0x006f) /\* 0x206f \*/

[ 2150](structbt__hci__cp__le__remove__iso__path.md)struct [bt\_hci\_cp\_le\_remove\_iso\_path](structbt__hci__cp__le__remove__iso__path.md) {

[ 2151](structbt__hci__cp__le__remove__iso__path.md#ad0106791003f9d1173f2a9f102903c45) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__remove__iso__path.md#ad0106791003f9d1173f2a9f102903c45);

[ 2152](structbt__hci__cp__le__remove__iso__path.md#a46e4b28917ff963ff4b672749fde0971) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [path\_dir](structbt__hci__cp__le__remove__iso__path.md#a46e4b28917ff963ff4b672749fde0971);

2153} \_\_packed;

2154

[ 2155](structbt__hci__rp__le__remove__iso__path.md)struct [bt\_hci\_rp\_le\_remove\_iso\_path](structbt__hci__rp__le__remove__iso__path.md) {

[ 2156](structbt__hci__rp__le__remove__iso__path.md#ab22e50e594e19931526feacd9bff33a3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__remove__iso__path.md#ab22e50e594e19931526feacd9bff33a3);

[ 2157](structbt__hci__rp__le__remove__iso__path.md#ae3b7704359989ca13582a5cd3742f588) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__remove__iso__path.md#ae3b7704359989ca13582a5cd3742f588);

2158} \_\_packed;

2159

[ 2160](hci__types_8h.md#aa857bdd2e81c923ab540761986074557)#define BT\_HCI\_ISO\_TEST\_ZERO\_SIZE\_SDU 0

[ 2161](hci__types_8h.md#aed9e2581c74218e023100d63201721af)#define BT\_HCI\_ISO\_TEST\_VARIABLE\_SIZE\_SDU 1

[ 2162](hci__types_8h.md#af5c0bf9fd20df7b4a4cdb7ce18fdc7fc)#define BT\_HCI\_ISO\_TEST\_MAX\_SIZE\_SDU 2

2163

[ 2164](hci__types_8h.md#a740f1964df5bdb675906c87ad8ee0cef)#define BT\_HCI\_OP\_LE\_ISO\_TRANSMIT\_TEST BT\_OP(BT\_OGF\_LE, 0x0070) /\* 0x2070 \*/

[ 2165](structbt__hci__cp__le__iso__transmit__test.md)struct [bt\_hci\_cp\_le\_iso\_transmit\_test](structbt__hci__cp__le__iso__transmit__test.md) {

[ 2166](structbt__hci__cp__le__iso__transmit__test.md#adffb0d57afc090692ab36ebeaad21bbd) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__iso__transmit__test.md#adffb0d57afc090692ab36ebeaad21bbd);

[ 2167](structbt__hci__cp__le__iso__transmit__test.md#a0653c77af723cc43a6b911816a8db437) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [payload\_type](structbt__hci__cp__le__iso__transmit__test.md#a0653c77af723cc43a6b911816a8db437);

2168} \_\_packed;

2169

[ 2170](structbt__hci__rp__le__iso__transmit__test.md)struct [bt\_hci\_rp\_le\_iso\_transmit\_test](structbt__hci__rp__le__iso__transmit__test.md) {

[ 2171](structbt__hci__rp__le__iso__transmit__test.md#a01ae01d11c606f559107b8c54781d843) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__iso__transmit__test.md#a01ae01d11c606f559107b8c54781d843);

[ 2172](structbt__hci__rp__le__iso__transmit__test.md#a0863c47551b328984e00c392f9f11660) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__iso__transmit__test.md#a0863c47551b328984e00c392f9f11660);

2173} \_\_packed;

2174

[ 2175](hci__types_8h.md#a467736569f030fbb433000e712f1b08e)#define BT\_HCI\_OP\_LE\_ISO\_RECEIVE\_TEST BT\_OP(BT\_OGF\_LE, 0x0071) /\* 0x2071 \*/

[ 2176](structbt__hci__cp__le__iso__receive__test.md)struct [bt\_hci\_cp\_le\_iso\_receive\_test](structbt__hci__cp__le__iso__receive__test.md) {

[ 2177](structbt__hci__cp__le__iso__receive__test.md#ac1272441f5c7b79e1ef5f644f099d19e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__iso__receive__test.md#ac1272441f5c7b79e1ef5f644f099d19e);

[ 2178](structbt__hci__cp__le__iso__receive__test.md#a9ce7e13fc1c1a7c87c01e1ecb24c5324) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [payload\_type](structbt__hci__cp__le__iso__receive__test.md#a9ce7e13fc1c1a7c87c01e1ecb24c5324);

2179} \_\_packed;

2180

[ 2181](structbt__hci__rp__le__iso__receive__test.md)struct [bt\_hci\_rp\_le\_iso\_receive\_test](structbt__hci__rp__le__iso__receive__test.md) {

[ 2182](structbt__hci__rp__le__iso__receive__test.md#a028a77001a5e24dda8fac38718103ef0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__iso__receive__test.md#a028a77001a5e24dda8fac38718103ef0);

[ 2183](structbt__hci__rp__le__iso__receive__test.md#a863a8a44af979a8b1b9d084563b2fe9a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__iso__receive__test.md#a863a8a44af979a8b1b9d084563b2fe9a);

2184} \_\_packed;

2185

[ 2186](hci__types_8h.md#a2b988ffc8ffd10ce1dfde377afa699e1)#define BT\_HCI\_OP\_LE\_ISO\_READ\_TEST\_COUNTERS BT\_OP(BT\_OGF\_LE, 0x0072) /\* 0x2072 \*/

[ 2187](structbt__hci__cp__le__read__test__counters.md)struct [bt\_hci\_cp\_le\_read\_test\_counters](structbt__hci__cp__le__read__test__counters.md) {

[ 2188](structbt__hci__cp__le__read__test__counters.md#a230d973c2db177c3595bb4808ebf5cd2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__read__test__counters.md#a230d973c2db177c3595bb4808ebf5cd2);

2189} \_\_packed;

2190

[ 2191](structbt__hci__rp__le__read__test__counters.md)struct [bt\_hci\_rp\_le\_read\_test\_counters](structbt__hci__rp__le__read__test__counters.md) {

[ 2192](structbt__hci__rp__le__read__test__counters.md#ae1e78d68e9f55b31092a07575a66c1c0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__test__counters.md#ae1e78d68e9f55b31092a07575a66c1c0);

[ 2193](structbt__hci__rp__le__read__test__counters.md#a8121f879a3fb5550cc1aa468aacb81b7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__read__test__counters.md#a8121f879a3fb5550cc1aa468aacb81b7);

[ 2194](structbt__hci__rp__le__read__test__counters.md#a8c4b2674fb129ca0de0bc45c608e13c7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [received\_cnt](structbt__hci__rp__le__read__test__counters.md#a8c4b2674fb129ca0de0bc45c608e13c7);

[ 2195](structbt__hci__rp__le__read__test__counters.md#ae96d05ffb2fbc681c804b04c8791aeab) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [missed\_cnt](structbt__hci__rp__le__read__test__counters.md#ae96d05ffb2fbc681c804b04c8791aeab);

[ 2196](structbt__hci__rp__le__read__test__counters.md#af6261d3547cd9b377fedc7a36891c2f7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [failed\_cnt](structbt__hci__rp__le__read__test__counters.md#af6261d3547cd9b377fedc7a36891c2f7);

2197} \_\_packed;

2198

[ 2199](hci__types_8h.md#a86436e6b0cb17de95b438f192bbff1d2)#define BT\_HCI\_OP\_LE\_ISO\_TEST\_END BT\_OP(BT\_OGF\_LE, 0x0073) /\* 0x2073 \*/

[ 2200](structbt__hci__cp__le__iso__test__end.md)struct [bt\_hci\_cp\_le\_iso\_test\_end](structbt__hci__cp__le__iso__test__end.md) {

[ 2201](structbt__hci__cp__le__iso__test__end.md#ab792ec021319024828bd7609e0fe7e96) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__iso__test__end.md#ab792ec021319024828bd7609e0fe7e96);

2202} \_\_packed;

2203

[ 2204](structbt__hci__rp__le__iso__test__end.md)struct [bt\_hci\_rp\_le\_iso\_test\_end](structbt__hci__rp__le__iso__test__end.md) {

[ 2205](structbt__hci__rp__le__iso__test__end.md#a16feaeb739f6ed34d9ce3fc86248955c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__iso__test__end.md#a16feaeb739f6ed34d9ce3fc86248955c);

[ 2206](structbt__hci__rp__le__iso__test__end.md#a4a4625d7b78abf3c039842df2a72ce8b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__iso__test__end.md#a4a4625d7b78abf3c039842df2a72ce8b);

[ 2207](structbt__hci__rp__le__iso__test__end.md#a55490978e7416ecc308bf510f05afd4f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [received\_cnt](structbt__hci__rp__le__iso__test__end.md#a55490978e7416ecc308bf510f05afd4f);

[ 2208](structbt__hci__rp__le__iso__test__end.md#a10b3ee6110bc0bb9279b22f9963715c1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [missed\_cnt](structbt__hci__rp__le__iso__test__end.md#a10b3ee6110bc0bb9279b22f9963715c1);

[ 2209](structbt__hci__rp__le__iso__test__end.md#ab4352fd5d9b822fb7fb75f8f5e2db6a9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [failed\_cnt](structbt__hci__rp__le__iso__test__end.md#ab4352fd5d9b822fb7fb75f8f5e2db6a9);

2210} \_\_packed;

2211

[ 2212](hci__types_8h.md#a29555bdcc7b439c2d0311fcb0721dc0b)#define BT\_HCI\_OP\_LE\_SET\_HOST\_FEATURE BT\_OP(BT\_OGF\_LE, 0x0074) /\* 0x2074 \*/

[ 2213](structbt__hci__cp__le__set__host__feature.md)struct [bt\_hci\_cp\_le\_set\_host\_feature](structbt__hci__cp__le__set__host__feature.md) {

[ 2214](structbt__hci__cp__le__set__host__feature.md#adcca35df216061ea08bd27e10fefd5e9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bit\_number](structbt__hci__cp__le__set__host__feature.md#adcca35df216061ea08bd27e10fefd5e9);

[ 2215](structbt__hci__cp__le__set__host__feature.md#a78b67164bce232466ab348f8937682c3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bit\_value](structbt__hci__cp__le__set__host__feature.md#a78b67164bce232466ab348f8937682c3);

2216} \_\_packed;

2217

[ 2218](structbt__hci__rp__le__set__host__feature.md)struct [bt\_hci\_rp\_le\_set\_host\_feature](structbt__hci__rp__le__set__host__feature.md) {

[ 2219](structbt__hci__rp__le__set__host__feature.md#a2e7cfc16da9fc0d00c35111811bf7c28) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__set__host__feature.md#a2e7cfc16da9fc0d00c35111811bf7c28);

2220} \_\_packed;

2221

[ 2222](hci__types_8h.md#acd6367a62d2c80d9f2e796d7b6ab1417)#define BT\_HCI\_OP\_LE\_READ\_ISO\_LINK\_QUALITY BT\_OP(BT\_OGF\_LE, 0x0075) /\* 0x2075 \*/

[ 2223](structbt__hci__cp__le__read__iso__link__quality.md)struct [bt\_hci\_cp\_le\_read\_iso\_link\_quality](structbt__hci__cp__le__read__iso__link__quality.md) {

[ 2224](structbt__hci__cp__le__read__iso__link__quality.md#a346fb3cf08203725d5943e42f03cb40d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__le__read__iso__link__quality.md#a346fb3cf08203725d5943e42f03cb40d);

2225} \_\_packed;

2226

[ 2227](structbt__hci__rp__le__read__iso__link__quality.md)struct [bt\_hci\_rp\_le\_read\_iso\_link\_quality](structbt__hci__rp__le__read__iso__link__quality.md) {

[ 2228](structbt__hci__rp__le__read__iso__link__quality.md#aef80c600f8916c098e08c43ca718d630) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__le__read__iso__link__quality.md#aef80c600f8916c098e08c43ca718d630);

[ 2229](structbt__hci__rp__le__read__iso__link__quality.md#a9f2e8c26081ede43c7712b851d79f2cd) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__le__read__iso__link__quality.md#a9f2e8c26081ede43c7712b851d79f2cd);

[ 2230](structbt__hci__rp__le__read__iso__link__quality.md#aae42e05dff474062726b92c6d45eae4f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tx\_unacked\_packets](structbt__hci__rp__le__read__iso__link__quality.md#aae42e05dff474062726b92c6d45eae4f);

[ 2231](structbt__hci__rp__le__read__iso__link__quality.md#a12c0c3f9fe6c3c94742367f30bdcc630) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tx\_flushed\_packets](structbt__hci__rp__le__read__iso__link__quality.md#a12c0c3f9fe6c3c94742367f30bdcc630);

[ 2232](structbt__hci__rp__le__read__iso__link__quality.md#a0d4468f6871716414ef4a601791bac58) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tx\_last\_subevent\_packets](structbt__hci__rp__le__read__iso__link__quality.md#a0d4468f6871716414ef4a601791bac58);

[ 2233](structbt__hci__rp__le__read__iso__link__quality.md#a7be135da9607045f60b616b84a68f5db) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [retransmitted\_packets](structbt__hci__rp__le__read__iso__link__quality.md#a7be135da9607045f60b616b84a68f5db);

[ 2234](structbt__hci__rp__le__read__iso__link__quality.md#a353070a64655a39f5410fe76e9168e97) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [crc\_error\_packets](structbt__hci__rp__le__read__iso__link__quality.md#a353070a64655a39f5410fe76e9168e97);

[ 2235](structbt__hci__rp__le__read__iso__link__quality.md#a6a16d0aa7ed220bac1ade12eb0f7703e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rx\_unreceived\_packets](structbt__hci__rp__le__read__iso__link__quality.md#a6a16d0aa7ed220bac1ade12eb0f7703e);

[ 2236](structbt__hci__rp__le__read__iso__link__quality.md#a68c23277e65dc5694f5a27ee2cd364ff) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [duplicate\_packets](structbt__hci__rp__le__read__iso__link__quality.md#a68c23277e65dc5694f5a27ee2cd364ff);

2237} \_\_packed;

2238

[ 2239](hci__types_8h.md#a13827b7d7b656ea02c0620ec7b525f65)#define BT\_HCI\_OP\_LE\_TX\_TEST\_V4 BT\_OP(BT\_OGF\_LE, 0x007B) /\* 0x207B \*/

2240

[ 2241](structbt__hci__cp__le__tx__test__v4.md)struct [bt\_hci\_cp\_le\_tx\_test\_v4](structbt__hci__cp__le__tx__test__v4.md) {

[ 2242](structbt__hci__cp__le__tx__test__v4.md#a3ccae40f09b2763b2b07dc16982f3973) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_ch](structbt__hci__cp__le__tx__test__v4.md#a3ccae40f09b2763b2b07dc16982f3973);

[ 2243](structbt__hci__cp__le__tx__test__v4.md#a7a8e2610fb8903ccfb6e4b08017f6112) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [test\_data\_len](structbt__hci__cp__le__tx__test__v4.md#a7a8e2610fb8903ccfb6e4b08017f6112);

[ 2244](structbt__hci__cp__le__tx__test__v4.md#abdd393eb264f04acf65e2dce4bd65ac0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pkt\_payload](structbt__hci__cp__le__tx__test__v4.md#abdd393eb264f04acf65e2dce4bd65ac0);

[ 2245](structbt__hci__cp__le__tx__test__v4.md#a5db011159fe75f4522e03ea1efdc57bd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__cp__le__tx__test__v4.md#a5db011159fe75f4522e03ea1efdc57bd);

[ 2246](structbt__hci__cp__le__tx__test__v4.md#a8dea923a63e787de3bfe07611eb7a1ed) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_len](structbt__hci__cp__le__tx__test__v4.md#a8dea923a63e787de3bfe07611eb7a1ed);

[ 2247](structbt__hci__cp__le__tx__test__v4.md#ae950f71a3fcfca0cf738bc28693256cf) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__hci__cp__le__tx__test__v4.md#ae950f71a3fcfca0cf738bc28693256cf);

[ 2248](structbt__hci__cp__le__tx__test__v4.md#a2039a87b5f32c4a45b8f858808df7cdc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [switch\_pattern\_len](structbt__hci__cp__le__tx__test__v4.md#a2039a87b5f32c4a45b8f858808df7cdc);

[ 2249](structbt__hci__cp__le__tx__test__v4.md#a3fe8ab7c0ee389dce8592cb7a38bc42c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ant\_ids](structbt__hci__cp__le__tx__test__v4.md#a3fe8ab7c0ee389dce8592cb7a38bc42c)[0];

2250} \_\_packed;

2251

[ 2252](hci__types_8h.md#a034d4a4fd8f7d6d324efa820d0b627d1)#define BT\_HCI\_TX\_TEST\_POWER\_MIN -0x7F

[ 2253](hci__types_8h.md#a925dda1fdce843e0bbcdd4acff696440)#define BT\_HCI\_TX\_TEST\_POWER\_MAX 0x14

2254

[ 2255](hci__types_8h.md#a5d0fc1dbb127ba0a383e4e56bb503334)#define BT\_HCI\_TX\_TEST\_POWER\_MIN\_SET 0x7E

[ 2256](hci__types_8h.md#a2e9caac5d12f8df1ce69a54f603500ee)#define BT\_HCI\_TX\_TEST\_POWER\_MAX\_SET 0x7F

2257

2258/\* Helper structure for Tx power parameter in the HCI Tx Test v4 command.

2259 \* Previous parameter of this command is variable size so having separated structure

2260 \* for this parameter helps in command parameters unpacking.

2261 \*/

[ 2262](structbt__hci__cp__le__tx__test__v4__tx__power.md)struct [bt\_hci\_cp\_le\_tx\_test\_v4\_tx\_power](structbt__hci__cp__le__tx__test__v4__tx__power.md) {

[ 2263](structbt__hci__cp__le__tx__test__v4__tx__power.md#a2a8b1c31787066ad2b471aec5c261085) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__hci__cp__le__tx__test__v4__tx__power.md#a2a8b1c31787066ad2b471aec5c261085);

2264} \_\_packed;

2265

2266/\* Event definitions \*/

2267

[ 2268](hci__types_8h.md#a0f44f6e5037d650b9dd0c5f34ba681b5)#define BT\_HCI\_EVT\_UNKNOWN 0x00

[ 2269](hci__types_8h.md#a955fe06f3fcab82c3370cb621f0dbca0)#define BT\_HCI\_EVT\_VENDOR 0xff

2270

[ 2271](hci__types_8h.md#abd8f15d920c0bdb3c68556b4e873f413)#define BT\_HCI\_EVT\_INQUIRY\_COMPLETE 0x01

[ 2272](structbt__hci__evt__inquiry__complete.md)struct [bt\_hci\_evt\_inquiry\_complete](structbt__hci__evt__inquiry__complete.md) {

[ 2273](structbt__hci__evt__inquiry__complete.md#aa8c1e8dc9807476f4759a3b3648b6332) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__inquiry__complete.md#aa8c1e8dc9807476f4759a3b3648b6332);

2274} \_\_packed;

2275

[ 2276](hci__types_8h.md#a0dd2162851b4a7afc3d96924f69cceca)#define BT\_HCI\_EVT\_CONN\_COMPLETE 0x03

[ 2277](structbt__hci__evt__conn__complete.md)struct [bt\_hci\_evt\_conn\_complete](structbt__hci__evt__conn__complete.md) {

[ 2278](structbt__hci__evt__conn__complete.md#a3dbf4fef53279003b7304ffee4a55e56) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__conn__complete.md#a3dbf4fef53279003b7304ffee4a55e56);

[ 2279](structbt__hci__evt__conn__complete.md#ad8877912008ea7445a67abc43aab5021) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__conn__complete.md#ad8877912008ea7445a67abc43aab5021);

[ 2280](structbt__hci__evt__conn__complete.md#a60a2ca6a8f16e4562c12b369685efa9b) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__evt__conn__complete.md#a60a2ca6a8f16e4562c12b369685efa9b);

[ 2281](structbt__hci__evt__conn__complete.md#afd9a21adf7d35205fb7e222c2e9e0328) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [link\_type](structbt__hci__evt__conn__complete.md#afd9a21adf7d35205fb7e222c2e9e0328);

[ 2282](structbt__hci__evt__conn__complete.md#a975617e8b568675a3ed8883cbe411557) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [encr\_enabled](structbt__hci__evt__conn__complete.md#a975617e8b568675a3ed8883cbe411557);

2283} \_\_packed;

2284

[ 2285](hci__types_8h.md#afc473fec33612ffb044d54bad39e8d76)#define BT\_HCI\_EVT\_CONN\_REQUEST 0x04

[ 2286](structbt__hci__evt__conn__request.md)struct [bt\_hci\_evt\_conn\_request](structbt__hci__evt__conn__request.md) {

[ 2287](structbt__hci__evt__conn__request.md#a03a2ee7ff7754173dff0809e4ebce9e6) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__evt__conn__request.md#a03a2ee7ff7754173dff0809e4ebce9e6);

[ 2288](structbt__hci__evt__conn__request.md#a6059d7c56f45d2fe047a7324db1e820d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dev\_class](structbt__hci__evt__conn__request.md#a6059d7c56f45d2fe047a7324db1e820d)[3];

[ 2289](structbt__hci__evt__conn__request.md#ae11d550701f64717a7d6df5c89b92d0e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [link\_type](structbt__hci__evt__conn__request.md#ae11d550701f64717a7d6df5c89b92d0e);

2290} \_\_packed;

2291

[ 2292](hci__types_8h.md#a32e5051a114f8987b49c6957c84d60e2)#define BT\_HCI\_EVT\_DISCONN\_COMPLETE 0x05

[ 2293](structbt__hci__evt__disconn__complete.md)struct [bt\_hci\_evt\_disconn\_complete](structbt__hci__evt__disconn__complete.md) {

[ 2294](structbt__hci__evt__disconn__complete.md#aed22ac781e9d70d11e7ebbe6f2e063bd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__disconn__complete.md#aed22ac781e9d70d11e7ebbe6f2e063bd);

[ 2295](structbt__hci__evt__disconn__complete.md#ab75f198a6495ad02a00bb3df99ab4258) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__disconn__complete.md#ab75f198a6495ad02a00bb3df99ab4258);

[ 2296](structbt__hci__evt__disconn__complete.md#a172554fbacf7aaa4dfbafe58b60fa5e6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reason](structbt__hci__evt__disconn__complete.md#a172554fbacf7aaa4dfbafe58b60fa5e6);

2297} \_\_packed;

2298

[ 2299](hci__types_8h.md#acc9c74c8406b84baaf55d9452924aaf9)#define BT\_HCI\_EVT\_AUTH\_COMPLETE 0x06

[ 2300](structbt__hci__evt__auth__complete.md)struct [bt\_hci\_evt\_auth\_complete](structbt__hci__evt__auth__complete.md) {

[ 2301](structbt__hci__evt__auth__complete.md#ae2b4b5bcc7195247626004d46ee22dd5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__auth__complete.md#ae2b4b5bcc7195247626004d46ee22dd5);

[ 2302](structbt__hci__evt__auth__complete.md#a7a78803e156218f138866fbb13fdadce) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__auth__complete.md#a7a78803e156218f138866fbb13fdadce);

2303} \_\_packed;

2304

[ 2305](hci__types_8h.md#a1a4be9cf628063db2fb821f67c54ea56)#define BT\_HCI\_EVT\_REMOTE\_NAME\_REQ\_COMPLETE 0x07

[ 2306](structbt__hci__evt__remote__name__req__complete.md)struct [bt\_hci\_evt\_remote\_name\_req\_complete](structbt__hci__evt__remote__name__req__complete.md) {

[ 2307](structbt__hci__evt__remote__name__req__complete.md#ab43d4a3c19d829b829cc7b40a67959f3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__remote__name__req__complete.md#ab43d4a3c19d829b829cc7b40a67959f3);

[ 2308](structbt__hci__evt__remote__name__req__complete.md#a380121873bf059b7c8a4abdf212f4235) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__evt__remote__name__req__complete.md#a380121873bf059b7c8a4abdf212f4235);

[ 2309](structbt__hci__evt__remote__name__req__complete.md#a3e54674692f7fc1670fa389e293714c7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [name](structbt__hci__evt__remote__name__req__complete.md#a3e54674692f7fc1670fa389e293714c7)[248];

2310} \_\_packed;

2311

[ 2312](hci__types_8h.md#a8dee2fc366d0371b68b212ff40e6ea7d)#define BT\_HCI\_EVT\_ENCRYPT\_CHANGE 0x08

[ 2313](structbt__hci__evt__encrypt__change.md)struct [bt\_hci\_evt\_encrypt\_change](structbt__hci__evt__encrypt__change.md) {

[ 2314](structbt__hci__evt__encrypt__change.md#af063bbd28d29edbcc81e907631167de7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__encrypt__change.md#af063bbd28d29edbcc81e907631167de7);

[ 2315](structbt__hci__evt__encrypt__change.md#a7737f659115ca602c1224c364a4c7404) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__encrypt__change.md#a7737f659115ca602c1224c364a4c7404);

[ 2316](structbt__hci__evt__encrypt__change.md#a61cc0e3c209acbb289d071515b44860a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [encrypt](structbt__hci__evt__encrypt__change.md#a61cc0e3c209acbb289d071515b44860a);

2317} \_\_packed;

2318

[ 2319](hci__types_8h.md#acbad340a978d4fc118af826d2c1a81e3)#define BT\_HCI\_EVT\_REMOTE\_FEATURES 0x0b

[ 2320](structbt__hci__evt__remote__features.md)struct [bt\_hci\_evt\_remote\_features](structbt__hci__evt__remote__features.md) {

[ 2321](structbt__hci__evt__remote__features.md#a2cedd8392c87914272ff250a56c80574) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__remote__features.md#a2cedd8392c87914272ff250a56c80574);

[ 2322](structbt__hci__evt__remote__features.md#ada0249bdb7108c5d347fea1218c4f878) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__remote__features.md#ada0249bdb7108c5d347fea1218c4f878);

[ 2323](structbt__hci__evt__remote__features.md#a70c97b9fbf7c363eab7b27f3a4e86e96) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [features](structbt__hci__evt__remote__features.md#a70c97b9fbf7c363eab7b27f3a4e86e96)[8];

2324} \_\_packed;

2325

[ 2326](hci__types_8h.md#a18f58c80d213d666ee8309cda8eb0a26)#define BT\_HCI\_EVT\_REMOTE\_VERSION\_INFO 0x0c

[ 2327](structbt__hci__evt__remote__version__info.md)struct [bt\_hci\_evt\_remote\_version\_info](structbt__hci__evt__remote__version__info.md) {

[ 2328](structbt__hci__evt__remote__version__info.md#a196f9489183d6e0116ff687df66c60c0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__remote__version__info.md#a196f9489183d6e0116ff687df66c60c0);

[ 2329](structbt__hci__evt__remote__version__info.md#a1703a9ac9a5e1ba3ed396fe5799f9f51) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__remote__version__info.md#a1703a9ac9a5e1ba3ed396fe5799f9f51);

[ 2330](structbt__hci__evt__remote__version__info.md#a8442b9f2bdc6cbce564c9bcec4169a20) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [version](structbt__hci__evt__remote__version__info.md#a8442b9f2bdc6cbce564c9bcec4169a20);

[ 2331](structbt__hci__evt__remote__version__info.md#aaa9c3875143700b6ed013715cb3c7107) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [manufacturer](structbt__hci__evt__remote__version__info.md#aaa9c3875143700b6ed013715cb3c7107);

[ 2332](structbt__hci__evt__remote__version__info.md#a02188119418a5a6dd8a4d0c37f5a060d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [subversion](structbt__hci__evt__remote__version__info.md#a02188119418a5a6dd8a4d0c37f5a060d);

2333} \_\_packed;

2334

[ 2335](hci__types_8h.md#a06f6cf60885ac051cdc9b463fc3b7de7)#define BT\_HCI\_EVT\_CMD\_COMPLETE 0x0e

[ 2336](structbt__hci__evt__cmd__complete.md)struct [bt\_hci\_evt\_cmd\_complete](structbt__hci__evt__cmd__complete.md) {

[ 2337](structbt__hci__evt__cmd__complete.md#a4da0539f81057722c8c322685bc12a40) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ncmd](structbt__hci__evt__cmd__complete.md#a4da0539f81057722c8c322685bc12a40);

[ 2338](structbt__hci__evt__cmd__complete.md#a3e61d980b4fa3084d3c50ead735fb76d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [opcode](structbt__hci__evt__cmd__complete.md#a3e61d980b4fa3084d3c50ead735fb76d);

2339} \_\_packed;

2340

[ 2341](structbt__hci__evt__cc__status.md)struct [bt\_hci\_evt\_cc\_status](structbt__hci__evt__cc__status.md) {

[ 2342](structbt__hci__evt__cc__status.md#a97cceaa218700da9b529ebadbb08c42c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__cc__status.md#a97cceaa218700da9b529ebadbb08c42c);

2343} \_\_packed;

2344

[ 2345](hci__types_8h.md#a2b35e7484351228243bb3564273c5bff)#define BT\_HCI\_EVT\_CMD\_STATUS 0x0f

[ 2346](structbt__hci__evt__cmd__status.md)struct [bt\_hci\_evt\_cmd\_status](structbt__hci__evt__cmd__status.md) {

[ 2347](structbt__hci__evt__cmd__status.md#aedd1560409005dbce409b892af1e3edf) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__cmd__status.md#aedd1560409005dbce409b892af1e3edf);

[ 2348](structbt__hci__evt__cmd__status.md#aed690e1cea2411df167e66cfaa742639) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ncmd](structbt__hci__evt__cmd__status.md#aed690e1cea2411df167e66cfaa742639);

[ 2349](structbt__hci__evt__cmd__status.md#a34002b693dc201083be4be77cfddcdb5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [opcode](structbt__hci__evt__cmd__status.md#a34002b693dc201083be4be77cfddcdb5);

2350} \_\_packed;

2351

[ 2352](hci__types_8h.md#a54c3bdd2687d142f925183a46ffc5f8b)#define BT\_HCI\_EVT\_HARDWARE\_ERROR 0x10

[ 2353](structbt__hci__evt__hardware__error.md)struct [bt\_hci\_evt\_hardware\_error](structbt__hci__evt__hardware__error.md) {

[ 2354](structbt__hci__evt__hardware__error.md#ab7be990e7cc32df43a3c976cb922e333) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [hardware\_code](structbt__hci__evt__hardware__error.md#ab7be990e7cc32df43a3c976cb922e333);

2355} \_\_packed;

2356

[ 2357](hci__types_8h.md#a9508e6faf71a345f7ff3d2cec9d85dde)#define BT\_HCI\_EVT\_ROLE\_CHANGE 0x12

[ 2358](structbt__hci__evt__role__change.md)struct [bt\_hci\_evt\_role\_change](structbt__hci__evt__role__change.md) {

[ 2359](structbt__hci__evt__role__change.md#aafe1a9e43a9a42d4030846180e55b8ef) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__role__change.md#aafe1a9e43a9a42d4030846180e55b8ef);

[ 2360](structbt__hci__evt__role__change.md#a18dd22435ae40fcf1c4fd2b90b402c60) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__evt__role__change.md#a18dd22435ae40fcf1c4fd2b90b402c60);

[ 2361](structbt__hci__evt__role__change.md#a2e5736d63e30326c33bec8ebdf986c62) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [role](structbt__hci__evt__role__change.md#a2e5736d63e30326c33bec8ebdf986c62);

2362} \_\_packed;

2363

[ 2364](hci__types_8h.md#a883433c60959629a013d34cea21ab88f)#define BT\_HCI\_EVT\_NUM\_COMPLETED\_PACKETS 0x13

[ 2365](structbt__hci__evt__num__completed__packets.md)struct [bt\_hci\_evt\_num\_completed\_packets](structbt__hci__evt__num__completed__packets.md) {

[ 2366](structbt__hci__evt__num__completed__packets.md#a666ed2c19596a89ab0c77275cbe18d1e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_handles](structbt__hci__evt__num__completed__packets.md#a666ed2c19596a89ab0c77275cbe18d1e);

[ 2367](structbt__hci__evt__num__completed__packets.md#a94fb176924f7e844704be28851366052) struct [bt\_hci\_handle\_count](structbt__hci__handle__count.md) [h](structbt__hci__evt__num__completed__packets.md#a94fb176924f7e844704be28851366052)[0];

2368} \_\_packed;

2369

[ 2370](hci__types_8h.md#a8c16e0bdecf9eae58bbd884fb48b0fc2)#define BT\_HCI\_EVT\_PIN\_CODE\_REQ 0x16

[ 2371](structbt__hci__evt__pin__code__req.md)struct [bt\_hci\_evt\_pin\_code\_req](structbt__hci__evt__pin__code__req.md) {

[ 2372](structbt__hci__evt__pin__code__req.md#a8649a30cd8c7ecf9ee006ddc2e625908) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__evt__pin__code__req.md#a8649a30cd8c7ecf9ee006ddc2e625908);

2373} \_\_packed;

2374

[ 2375](hci__types_8h.md#aab60607637f0e1f8e3cbf9f7292ddc57)#define BT\_HCI\_EVT\_LINK\_KEY\_REQ 0x17

[ 2376](structbt__hci__evt__link__key__req.md)struct [bt\_hci\_evt\_link\_key\_req](structbt__hci__evt__link__key__req.md) {

[ 2377](structbt__hci__evt__link__key__req.md#aed882dfb6b632383543bd7e60536ccc6) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__evt__link__key__req.md#aed882dfb6b632383543bd7e60536ccc6);

2378} \_\_packed;

2379

2380/\* Link Key types \*/

[ 2381](hci__types_8h.md#a7283a42b1220dd6d56c22cd9cb424e7c)#define BT\_LK\_COMBINATION 0x00

[ 2382](hci__types_8h.md#a12ffe67b9e4ec01bbe400a6a3cc5b859)#define BT\_LK\_LOCAL\_UNIT 0x01

[ 2383](hci__types_8h.md#aeb53b797c4fc91a38a459ff5f29d35e1)#define BT\_LK\_REMOTE\_UNIT 0x02

[ 2384](hci__types_8h.md#a916e6133d2dadb9aaf5fe42d0c0e1b96)#define BT\_LK\_DEBUG\_COMBINATION 0x03

[ 2385](hci__types_8h.md#adfea495d48088eae78491a14730bef31)#define BT\_LK\_UNAUTH\_COMBINATION\_P192 0x04

[ 2386](hci__types_8h.md#a6630ceb874d343f721931f80ee5fa67e)#define BT\_LK\_AUTH\_COMBINATION\_P192 0x05

[ 2387](hci__types_8h.md#a5753841a02ba0c2fa627d9e96bad045d)#define BT\_LK\_CHANGED\_COMBINATION 0x06

[ 2388](hci__types_8h.md#ada18ab581a323eafe8754009ef27d05e)#define BT\_LK\_UNAUTH\_COMBINATION\_P256 0x07

[ 2389](hci__types_8h.md#aa941cce486c497afa6d03fec326396b9)#define BT\_LK\_AUTH\_COMBINATION\_P256 0x08

2390

[ 2391](hci__types_8h.md#a15578dd8e9d2b16a28ea0b020ac9112b)#define BT\_HCI\_EVT\_LINK\_KEY\_NOTIFY 0x18

[ 2392](structbt__hci__evt__link__key__notify.md)struct [bt\_hci\_evt\_link\_key\_notify](structbt__hci__evt__link__key__notify.md) {

[ 2393](structbt__hci__evt__link__key__notify.md#a02647d66142c037b8bca2e748bc15319) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__evt__link__key__notify.md#a02647d66142c037b8bca2e748bc15319);

[ 2394](structbt__hci__evt__link__key__notify.md#a4a1b50d8874d01a6a5dc5c52524c9bed) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [link\_key](structbt__hci__evt__link__key__notify.md#a4a1b50d8874d01a6a5dc5c52524c9bed)[16];

[ 2395](structbt__hci__evt__link__key__notify.md#a664580660a690af0d9ae3a62d79ad94b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key\_type](structbt__hci__evt__link__key__notify.md#a664580660a690af0d9ae3a62d79ad94b);

2396} \_\_packed;

2397

2398/\* Overflow link types \*/

[ 2399](hci__types_8h.md#a44233b934e33c65af90d03ad301e6b9d)#define BT\_OVERFLOW\_LINK\_SYNCH 0x00

[ 2400](hci__types_8h.md#a35831810e3a7e2c5446780b14ef7d9c1)#define BT\_OVERFLOW\_LINK\_ACL 0x01

[ 2401](hci__types_8h.md#ad32010743baef10c635d8b08f21c8641)#define BT\_OVERFLOW\_LINK\_ISO 0x02

2402

[ 2403](hci__types_8h.md#ae747b016101bc9e9614163288c5c0d15)#define BT\_HCI\_EVT\_DATA\_BUF\_OVERFLOW 0x1a

[ 2404](structbt__hci__evt__data__buf__overflow.md)struct [bt\_hci\_evt\_data\_buf\_overflow](structbt__hci__evt__data__buf__overflow.md) {

[ 2405](structbt__hci__evt__data__buf__overflow.md#ae0201e03ebb9b9b33e9eae593a56355f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [link\_type](structbt__hci__evt__data__buf__overflow.md#ae0201e03ebb9b9b33e9eae593a56355f);

2406} \_\_packed;

2407

[ 2408](hci__types_8h.md#a92243c99484922771d5aca8f98945d29)#define BT\_HCI\_EVT\_INQUIRY\_RESULT\_WITH\_RSSI 0x22

[ 2409](structbt__hci__evt__inquiry__result__with__rssi.md)struct [bt\_hci\_evt\_inquiry\_result\_with\_rssi](structbt__hci__evt__inquiry__result__with__rssi.md) {

[ 2410](structbt__hci__evt__inquiry__result__with__rssi.md#af955dd1660f83e41e6d1b2b5aecf8133) [bt\_addr\_t](structbt__addr__t.md) [addr](structbt__hci__evt__inquiry__result__with__rssi.md#af955dd1660f83e41e6d1b2b5aecf8133);

[ 2411](structbt__hci__evt__inquiry__result__with__rssi.md#a0a5c188d0d40b4259cbeb613c0dd12cf) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pscan\_rep\_mode](structbt__hci__evt__inquiry__result__with__rssi.md#a0a5c188d0d40b4259cbeb613c0dd12cf);

[ 2412](structbt__hci__evt__inquiry__result__with__rssi.md#a09914ee9998c0b59cb35ed74d08aa4f2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reserved](structbt__hci__evt__inquiry__result__with__rssi.md#a09914ee9998c0b59cb35ed74d08aa4f2);

[ 2413](structbt__hci__evt__inquiry__result__with__rssi.md#ad9b4920e2864ed8350de038dffe64574) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cod](structbt__hci__evt__inquiry__result__with__rssi.md#ad9b4920e2864ed8350de038dffe64574)[3];

[ 2414](structbt__hci__evt__inquiry__result__with__rssi.md#a1ee08f85103581994a88345cc94d7494) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [clock\_offset](structbt__hci__evt__inquiry__result__with__rssi.md#a1ee08f85103581994a88345cc94d7494);

[ 2415](structbt__hci__evt__inquiry__result__with__rssi.md#a6d19e6400d7015db7122516e570d7989) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__hci__evt__inquiry__result__with__rssi.md#a6d19e6400d7015db7122516e570d7989);

2416} \_\_packed;

2417

[ 2418](hci__types_8h.md#a092a782ea069c98475a6617241321122)#define BT\_HCI\_EVT\_REMOTE\_EXT\_FEATURES 0x23

[ 2419](structbt__hci__evt__remote__ext__features.md)struct [bt\_hci\_evt\_remote\_ext\_features](structbt__hci__evt__remote__ext__features.md) {

[ 2420](structbt__hci__evt__remote__ext__features.md#a4f1d489aaa5626e485d34a9ae4cf9a34) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__remote__ext__features.md#a4f1d489aaa5626e485d34a9ae4cf9a34);

[ 2421](structbt__hci__evt__remote__ext__features.md#a0191b80b4f4d5360972faa6d5edf5055) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__remote__ext__features.md#a0191b80b4f4d5360972faa6d5edf5055);

[ 2422](structbt__hci__evt__remote__ext__features.md#aeece2b8d46f4a3713d63df29058f2d9c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [page](structbt__hci__evt__remote__ext__features.md#aeece2b8d46f4a3713d63df29058f2d9c);

[ 2423](structbt__hci__evt__remote__ext__features.md#afa577407f4ded5404394f42e7c73e10b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_page](structbt__hci__evt__remote__ext__features.md#afa577407f4ded5404394f42e7c73e10b);

[ 2424](structbt__hci__evt__remote__ext__features.md#a084199f8e30669c2a1a631af26c0d69a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [features](structbt__hci__evt__remote__ext__features.md#a084199f8e30669c2a1a631af26c0d69a)[8];

2425} \_\_packed;

2426

[ 2427](hci__types_8h.md#a0decb07f1b4ae20b23cffc616dd442e4)#define BT\_HCI\_EVT\_LE\_PER\_ADV\_SYNC\_ESTABLISHED\_V2 0x24

[ 2428](structbt__hci__evt__le__per__adv__sync__established__v2.md)struct [bt\_hci\_evt\_le\_per\_adv\_sync\_established\_v2](structbt__hci__evt__le__per__adv__sync__established__v2.md) {

[ 2429](structbt__hci__evt__le__per__adv__sync__established__v2.md#a96b975f5a2fcf193b0b58c230486ec36) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__per__adv__sync__established__v2.md#a96b975f5a2fcf193b0b58c230486ec36);

[ 2430](structbt__hci__evt__le__per__adv__sync__established__v2.md#ab7d3793e782d7b2bb311b8a5ac3a871b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__per__adv__sync__established__v2.md#ab7d3793e782d7b2bb311b8a5ac3a871b);

[ 2431](structbt__hci__evt__le__per__adv__sync__established__v2.md#a0ce9a9170d93ff69f25ff35eb163511f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__hci__evt__le__per__adv__sync__established__v2.md#a0ce9a9170d93ff69f25ff35eb163511f);

[ 2432](structbt__hci__evt__le__per__adv__sync__established__v2.md#abd67ec989479eb793e7bf99a4cf371b8) [bt\_addr\_le\_t](structbt__addr__le__t.md) [adv\_addr](structbt__hci__evt__le__per__adv__sync__established__v2.md#abd67ec989479eb793e7bf99a4cf371b8);

[ 2433](structbt__hci__evt__le__per__adv__sync__established__v2.md#a36b5c8454ee3635d2298592c83166f14) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__evt__le__per__adv__sync__established__v2.md#a36b5c8454ee3635d2298592c83166f14);

[ 2434](structbt__hci__evt__le__per__adv__sync__established__v2.md#a958630cb9e275ab6f8ed0c548958e5ee) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__hci__evt__le__per__adv__sync__established__v2.md#a958630cb9e275ab6f8ed0c548958e5ee);

[ 2435](structbt__hci__evt__le__per__adv__sync__established__v2.md#a13ab0e87d6673a34e51f3112a5fd5a0c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [clock\_accuracy](structbt__hci__evt__le__per__adv__sync__established__v2.md#a13ab0e87d6673a34e51f3112a5fd5a0c);

[ 2436](structbt__hci__evt__le__per__adv__sync__established__v2.md#af4fb92baa4f98c08c990ba505faf9226) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_subevents](structbt__hci__evt__le__per__adv__sync__established__v2.md#af4fb92baa4f98c08c990ba505faf9226);

[ 2437](structbt__hci__evt__le__per__adv__sync__established__v2.md#ad21df6269d8242d94ba9cbc1e0d4d344) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent\_interval](structbt__hci__evt__le__per__adv__sync__established__v2.md#ad21df6269d8242d94ba9cbc1e0d4d344);

[ 2438](structbt__hci__evt__le__per__adv__sync__established__v2.md#ac4c2bc8789513692ce0f2cc81aa59476) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot\_delay](structbt__hci__evt__le__per__adv__sync__established__v2.md#ac4c2bc8789513692ce0f2cc81aa59476);

[ 2439](structbt__hci__evt__le__per__adv__sync__established__v2.md#aacb6946dbfeb2ffbc251910853559329) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot\_spacing](structbt__hci__evt__le__per__adv__sync__established__v2.md#aacb6946dbfeb2ffbc251910853559329);

2440} \_\_packed;

2441

[ 2442](hci__types_8h.md#a8d067bf751953fd8a7bb5421bdc94970)#define BT\_HCI\_EVT\_LE\_PER\_ADVERTISING\_REPORT\_V2 0x25

[ 2443](structbt__hci__evt__le__per__advertising__report__v2.md)struct [bt\_hci\_evt\_le\_per\_advertising\_report\_v2](structbt__hci__evt__le__per__advertising__report__v2.md) {

[ 2444](structbt__hci__evt__le__per__advertising__report__v2.md#a34b15fb9b5b4f0d199ccf274dd489c6a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__per__advertising__report__v2.md#a34b15fb9b5b4f0d199ccf274dd489c6a);

[ 2445](structbt__hci__evt__le__per__advertising__report__v2.md#a37a9eb7d417da9285e22cc7f83071c69) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__hci__evt__le__per__advertising__report__v2.md#a37a9eb7d417da9285e22cc7f83071c69);

[ 2446](structbt__hci__evt__le__per__advertising__report__v2.md#ad598ffd0108825803a4734959a354bd8) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__hci__evt__le__per__advertising__report__v2.md#ad598ffd0108825803a4734959a354bd8);

[ 2447](structbt__hci__evt__le__per__advertising__report__v2.md#a3276c2e11c946744b73426f54bf62b8c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__hci__evt__le__per__advertising__report__v2.md#a3276c2e11c946744b73426f54bf62b8c);

[ 2448](structbt__hci__evt__le__per__advertising__report__v2.md#a499d82e1e3cfc501d399f570ebbcdc42) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [periodic\_event\_counter](structbt__hci__evt__le__per__advertising__report__v2.md#a499d82e1e3cfc501d399f570ebbcdc42);

[ 2449](structbt__hci__evt__le__per__advertising__report__v2.md#af27b23fe38e9ff092d8839cd81749456) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent](structbt__hci__evt__le__per__advertising__report__v2.md#af27b23fe38e9ff092d8839cd81749456);

[ 2450](structbt__hci__evt__le__per__advertising__report__v2.md#a73496cc962721538e27e9924fff0f3db) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_status](structbt__hci__evt__le__per__advertising__report__v2.md#a73496cc962721538e27e9924fff0f3db);

[ 2451](structbt__hci__evt__le__per__advertising__report__v2.md#a30f4e81346957ad4f9f0488dd93fafc3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [length](structbt__hci__evt__le__per__advertising__report__v2.md#a30f4e81346957ad4f9f0488dd93fafc3);

[ 2452](structbt__hci__evt__le__per__advertising__report__v2.md#a7af1cd4ec9df24e575a83a640eea36d2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__hci__evt__le__per__advertising__report__v2.md#a7af1cd4ec9df24e575a83a640eea36d2)[0];

2453} \_\_packed;

2454

[ 2455](hci__types_8h.md#a5379a2a0016a2551ac79736924c7ea86)#define BT\_HCI\_EVT\_LE\_PAST\_RECEIVED\_V2 0x26

[ 2456](structbt__hci__evt__le__past__received__v2.md)struct [bt\_hci\_evt\_le\_past\_received\_v2](structbt__hci__evt__le__past__received__v2.md) {

[ 2457](structbt__hci__evt__le__past__received__v2.md#aefe79f973eda8c7c5670c7a721d55d8a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__past__received__v2.md#aefe79f973eda8c7c5670c7a721d55d8a);

[ 2458](structbt__hci__evt__le__past__received__v2.md#adb011949f592ec7f8843d4fd47eca2e9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__evt__le__past__received__v2.md#adb011949f592ec7f8843d4fd47eca2e9);

[ 2459](structbt__hci__evt__le__past__received__v2.md#acffc2fa22a16a3a12a4f7dfc3bb45866) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [service\_data](structbt__hci__evt__le__past__received__v2.md#acffc2fa22a16a3a12a4f7dfc3bb45866);

[ 2460](structbt__hci__evt__le__past__received__v2.md#a00bf4bdf12fce6cbf2874b9c4ae09f9f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sync\_handle](structbt__hci__evt__le__past__received__v2.md#a00bf4bdf12fce6cbf2874b9c4ae09f9f);

[ 2461](structbt__hci__evt__le__past__received__v2.md#a05d798c9415541ef7f5716992157b1a1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_sid](structbt__hci__evt__le__past__received__v2.md#a05d798c9415541ef7f5716992157b1a1);

[ 2462](structbt__hci__evt__le__past__received__v2.md#aff78554e8980635290767e9877ac479b) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__hci__evt__le__past__received__v2.md#aff78554e8980635290767e9877ac479b);

[ 2463](structbt__hci__evt__le__past__received__v2.md#ae7a73293519ab45aec40a9a1aeaa4e89) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__evt__le__past__received__v2.md#ae7a73293519ab45aec40a9a1aeaa4e89);

[ 2464](structbt__hci__evt__le__past__received__v2.md#a736af2c2ee0afd3cb00e8eb4d103991c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__hci__evt__le__past__received__v2.md#a736af2c2ee0afd3cb00e8eb4d103991c);

[ 2465](structbt__hci__evt__le__past__received__v2.md#a78853d14c3bf9a9aba3c4e15b2e06abb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [clock\_accuracy](structbt__hci__evt__le__past__received__v2.md#a78853d14c3bf9a9aba3c4e15b2e06abb);

[ 2466](structbt__hci__evt__le__past__received__v2.md#ab8a2a55fe071218284d60f1a2896945b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_subevents](structbt__hci__evt__le__past__received__v2.md#ab8a2a55fe071218284d60f1a2896945b);

[ 2467](structbt__hci__evt__le__past__received__v2.md#aefdc5ac7ef125f4dc5865c198b98c67d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent\_interval](structbt__hci__evt__le__past__received__v2.md#aefdc5ac7ef125f4dc5865c198b98c67d);

[ 2468](structbt__hci__evt__le__past__received__v2.md#a9f55d5f6d17d11e72f7cac363a69fe97) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot\_delay](structbt__hci__evt__le__past__received__v2.md#a9f55d5f6d17d11e72f7cac363a69fe97);

[ 2469](structbt__hci__evt__le__past__received__v2.md#acf711399e575295dcef73cfeeb844eab) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot\_spacing](structbt__hci__evt__le__past__received__v2.md#acf711399e575295dcef73cfeeb844eab);

2470} \_\_packed;

2471

[ 2472](hci__types_8h.md#a4395b8b850e9fd3735c2369798f9c226)#define BT\_HCI\_EVT\_LE\_PER\_ADV\_SUBEVENT\_DATA\_REQUEST 0x27

[ 2473](structbt__hci__evt__le__per__adv__subevent__data__request.md)struct [bt\_hci\_evt\_le\_per\_adv\_subevent\_data\_request](structbt__hci__evt__le__per__adv__subevent__data__request.md) {

[ 2474](structbt__hci__evt__le__per__adv__subevent__data__request.md#ae6f6ef17edabfd210a7e6597087ff512) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_handle](structbt__hci__evt__le__per__adv__subevent__data__request.md#ae6f6ef17edabfd210a7e6597087ff512);

[ 2475](structbt__hci__evt__le__per__adv__subevent__data__request.md#a8f7fd9b149aa52422cb3eb874b91943d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent\_start](structbt__hci__evt__le__per__adv__subevent__data__request.md#a8f7fd9b149aa52422cb3eb874b91943d);

[ 2476](structbt__hci__evt__le__per__adv__subevent__data__request.md#a45cdb248b80602a7f14f24e0324e6f97) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent\_data\_count](structbt__hci__evt__le__per__adv__subevent__data__request.md#a45cdb248b80602a7f14f24e0324e6f97);

2477} \_\_packed;

2478

[ 2479](hci__types_8h.md#a64e0f465068e72e98904fa6cdc33d3de)#define BT\_HCI\_EVT\_LE\_PER\_ADV\_RESPONSE\_REPORT 0x28

2480

[ 2481](structbt__hci__evt__le__per__adv__response.md)struct [bt\_hci\_evt\_le\_per\_adv\_response](structbt__hci__evt__le__per__adv__response.md) {

[ 2482](structbt__hci__evt__le__per__adv__response.md#a74e304822ec7a431802cf8a7539d640e) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__hci__evt__le__per__adv__response.md#a74e304822ec7a431802cf8a7539d640e);

[ 2483](structbt__hci__evt__le__per__adv__response.md#a1100429baf398067a396a6ba8db6778a) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__hci__evt__le__per__adv__response.md#a1100429baf398067a396a6ba8db6778a);

[ 2484](structbt__hci__evt__le__per__adv__response.md#a4197fbae54be038502312efc14b66320) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__hci__evt__le__per__adv__response.md#a4197fbae54be038502312efc14b66320);

[ 2485](structbt__hci__evt__le__per__adv__response.md#aa5b5467f4edd52fb8de078b0948141f0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot](structbt__hci__evt__le__per__adv__response.md#aa5b5467f4edd52fb8de078b0948141f0);

[ 2486](structbt__hci__evt__le__per__adv__response.md#aa524756d2cce0718ecfd66704eaf389d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_status](structbt__hci__evt__le__per__adv__response.md#aa524756d2cce0718ecfd66704eaf389d);

[ 2487](structbt__hci__evt__le__per__adv__response.md#af68f0dc92118f78f6f5b0ffbf1854664) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_length](structbt__hci__evt__le__per__adv__response.md#af68f0dc92118f78f6f5b0ffbf1854664);

[ 2488](structbt__hci__evt__le__per__adv__response.md#ace3b58eba63b55ce5f3038d4a7877ec2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__hci__evt__le__per__adv__response.md#ace3b58eba63b55ce5f3038d4a7877ec2)[0];

2489} \_\_packed;

2490

[ 2491](structbt__hci__evt__le__per__adv__response__report.md)struct [bt\_hci\_evt\_le\_per\_adv\_response\_report](structbt__hci__evt__le__per__adv__response__report.md) {

[ 2492](structbt__hci__evt__le__per__adv__response__report.md#a9d746015a9c2b48c54008319c892b063) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_handle](structbt__hci__evt__le__per__adv__response__report.md#a9d746015a9c2b48c54008319c892b063);

[ 2493](structbt__hci__evt__le__per__adv__response__report.md#ad4f8f61150f82f4ba420e3c0a1f333c2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent](structbt__hci__evt__le__per__adv__response__report.md#ad4f8f61150f82f4ba420e3c0a1f333c2);

[ 2494](structbt__hci__evt__le__per__adv__response__report.md#a46a5b74321a80697fd700a276be18ed3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_status](structbt__hci__evt__le__per__adv__response__report.md#a46a5b74321a80697fd700a276be18ed3);

[ 2495](structbt__hci__evt__le__per__adv__response__report.md#a37f3519eefe33e87d49c7c2ad0f8b40c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_responses](structbt__hci__evt__le__per__adv__response__report.md#a37f3519eefe33e87d49c7c2ad0f8b40c);

[ 2496](structbt__hci__evt__le__per__adv__response__report.md#a3b1bcca7a7dbc6fcf5709f6152268b87) struct [bt\_hci\_evt\_le\_per\_adv\_response](structbt__hci__evt__le__per__adv__response.md) [responses](structbt__hci__evt__le__per__adv__response__report.md#a3b1bcca7a7dbc6fcf5709f6152268b87)[0];

2497} \_\_packed;

2498

[ 2499](hci__types_8h.md#a60ea5e58028aa09c00d20cfff5c942d5)#define BT\_HCI\_EVT\_LE\_ENH\_CONN\_COMPLETE\_V2 0x29

[ 2500](structbt__hci__evt__le__enh__conn__complete__v2.md)struct [bt\_hci\_evt\_le\_enh\_conn\_complete\_v2](structbt__hci__evt__le__enh__conn__complete__v2.md) {

[ 2501](structbt__hci__evt__le__enh__conn__complete__v2.md#ad72ba07d766135a94474a9d004da1a66) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__enh__conn__complete__v2.md#ad72ba07d766135a94474a9d004da1a66);

[ 2502](structbt__hci__evt__le__enh__conn__complete__v2.md#affe2dba0634e0215579fb13d77016a8c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__enh__conn__complete__v2.md#affe2dba0634e0215579fb13d77016a8c);

[ 2503](structbt__hci__evt__le__enh__conn__complete__v2.md#a3343de57a24fa2ebdccf9411f388817d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [role](structbt__hci__evt__le__enh__conn__complete__v2.md#a3343de57a24fa2ebdccf9411f388817d);

[ 2504](structbt__hci__evt__le__enh__conn__complete__v2.md#a7df28c9ddec607d5a84572bb421b7f5a) [bt\_addr\_le\_t](structbt__addr__le__t.md) [peer\_addr](structbt__hci__evt__le__enh__conn__complete__v2.md#a7df28c9ddec607d5a84572bb421b7f5a);

[ 2505](structbt__hci__evt__le__enh__conn__complete__v2.md#a10a1cbf0e9e21bc127dc64adadd53773) [bt\_addr\_t](structbt__addr__t.md) [local\_rpa](structbt__hci__evt__le__enh__conn__complete__v2.md#a10a1cbf0e9e21bc127dc64adadd53773);

[ 2506](structbt__hci__evt__le__enh__conn__complete__v2.md#a014e8bf891684c4cd9e5ec53d986d412) [bt\_addr\_t](structbt__addr__t.md) [peer\_rpa](structbt__hci__evt__le__enh__conn__complete__v2.md#a014e8bf891684c4cd9e5ec53d986d412);

[ 2507](structbt__hci__evt__le__enh__conn__complete__v2.md#a237b8313970cc63b7e57c0ce4913392e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__hci__evt__le__enh__conn__complete__v2.md#a237b8313970cc63b7e57c0ce4913392e);

[ 2508](structbt__hci__evt__le__enh__conn__complete__v2.md#a3daa32ac19c4eda4a49bebb64f3145be) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [latency](structbt__hci__evt__le__enh__conn__complete__v2.md#a3daa32ac19c4eda4a49bebb64f3145be);

[ 2509](structbt__hci__evt__le__enh__conn__complete__v2.md#a2b2ac4890eb9604a3f5cd40f55c2c066) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [supv\_timeout](structbt__hci__evt__le__enh__conn__complete__v2.md#a2b2ac4890eb9604a3f5cd40f55c2c066);

[ 2510](structbt__hci__evt__le__enh__conn__complete__v2.md#a7bb168061803d1122e8ee47dc8af3ae9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [clock\_accuracy](structbt__hci__evt__le__enh__conn__complete__v2.md#a7bb168061803d1122e8ee47dc8af3ae9);

[ 2511](structbt__hci__evt__le__enh__conn__complete__v2.md#a883ba3aed9aed00ec0ce425999d97180) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_handle](structbt__hci__evt__le__enh__conn__complete__v2.md#a883ba3aed9aed00ec0ce425999d97180);

[ 2512](structbt__hci__evt__le__enh__conn__complete__v2.md#a81dca94a6f2a8ea3da7a5a316daa5941) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sync\_handle](structbt__hci__evt__le__enh__conn__complete__v2.md#a81dca94a6f2a8ea3da7a5a316daa5941);

2513} \_\_packed;

2514

[ 2515](hci__types_8h.md#ab77f3074a2236afc1ed773775d17befe)#define BT\_HCI\_EVT\_SYNC\_CONN\_COMPLETE 0x2c

[ 2516](structbt__hci__evt__sync__conn__complete.md)struct [bt\_hci\_evt\_sync\_conn\_complete](structbt__hci__evt__sync__conn__complete.md) {

[ 2517](structbt__hci__evt__sync__conn__complete.md#accd17a95f35ab1988122df7584830f60) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__sync__conn__complete.md#accd17a95f35ab1988122df7584830f60);

[ 2518](structbt__hci__evt__sync__conn__complete.md#aa48aa29ff73e93e8d961013f066c1b5e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__sync__conn__complete.md#aa48aa29ff73e93e8d961013f066c1b5e);

[ 2519](structbt__hci__evt__sync__conn__complete.md#a78f5560783400f1d1a63b2c9d69fa7ed) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__evt__sync__conn__complete.md#a78f5560783400f1d1a63b2c9d69fa7ed);

[ 2520](structbt__hci__evt__sync__conn__complete.md#aacf9919945e9b755913da145f0fe78ae) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [link\_type](structbt__hci__evt__sync__conn__complete.md#aacf9919945e9b755913da145f0fe78ae);

[ 2521](structbt__hci__evt__sync__conn__complete.md#a4b93873ad6f5388657511d87fc0a8c85) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_interval](structbt__hci__evt__sync__conn__complete.md#a4b93873ad6f5388657511d87fc0a8c85);

[ 2522](structbt__hci__evt__sync__conn__complete.md#a68a31880c8aab9245be043c1719464d3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [retansmission\_window](structbt__hci__evt__sync__conn__complete.md#a68a31880c8aab9245be043c1719464d3);

[ 2523](structbt__hci__evt__sync__conn__complete.md#a6a455f56da4666cb602e6c05157e166d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [rx\_pkt\_length](structbt__hci__evt__sync__conn__complete.md#a6a455f56da4666cb602e6c05157e166d);

[ 2524](structbt__hci__evt__sync__conn__complete.md#ab4d4106d5120f10e8300834db12740d8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [tx\_pkt\_length](structbt__hci__evt__sync__conn__complete.md#ab4d4106d5120f10e8300834db12740d8);

[ 2525](structbt__hci__evt__sync__conn__complete.md#a5f6068569bf649bcd1d13928f56f9703) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [air\_mode](structbt__hci__evt__sync__conn__complete.md#a5f6068569bf649bcd1d13928f56f9703);

2526} \_\_packed;

2527

[ 2528](hci__types_8h.md#a9b5405de1e07fcefba54b286bd1fdfbe)#define BT\_HCI\_EVT\_EXTENDED\_INQUIRY\_RESULT 0x2f

[ 2529](structbt__hci__evt__extended__inquiry__result.md)struct [bt\_hci\_evt\_extended\_inquiry\_result](structbt__hci__evt__extended__inquiry__result.md) {

[ 2530](structbt__hci__evt__extended__inquiry__result.md#a76e4e82d1dedaee94bd730a4134d7d77) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_reports](structbt__hci__evt__extended__inquiry__result.md#a76e4e82d1dedaee94bd730a4134d7d77);

[ 2531](structbt__hci__evt__extended__inquiry__result.md#a955a7d36736badfae1f39fa9eda61ebb) [bt\_addr\_t](structbt__addr__t.md) [addr](structbt__hci__evt__extended__inquiry__result.md#a955a7d36736badfae1f39fa9eda61ebb);

[ 2532](structbt__hci__evt__extended__inquiry__result.md#aba4aac84e23ca9d283cb8af265dcaf0d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pscan\_rep\_mode](structbt__hci__evt__extended__inquiry__result.md#aba4aac84e23ca9d283cb8af265dcaf0d);

[ 2533](structbt__hci__evt__extended__inquiry__result.md#ab6ec4b5efe058e225d173cbda9a16f2e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reserved](structbt__hci__evt__extended__inquiry__result.md#ab6ec4b5efe058e225d173cbda9a16f2e);

[ 2534](structbt__hci__evt__extended__inquiry__result.md#ab4ebcf09817827d1d10ddeee13832759) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cod](structbt__hci__evt__extended__inquiry__result.md#ab4ebcf09817827d1d10ddeee13832759)[3];

[ 2535](structbt__hci__evt__extended__inquiry__result.md#a30c5586d954585006238e8c2b33a7601) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [clock\_offset](structbt__hci__evt__extended__inquiry__result.md#a30c5586d954585006238e8c2b33a7601);

[ 2536](structbt__hci__evt__extended__inquiry__result.md#a21f7f48422bcfb867c9ca2e4411a2fbd) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__hci__evt__extended__inquiry__result.md#a21f7f48422bcfb867c9ca2e4411a2fbd);

[ 2537](structbt__hci__evt__extended__inquiry__result.md#a1eba2841941f7cdbb00f548ebf0485e9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [eir](structbt__hci__evt__extended__inquiry__result.md#a1eba2841941f7cdbb00f548ebf0485e9)[240];

2538} \_\_packed;

2539

[ 2540](hci__types_8h.md#aad28cc20cc111ac39e39011932b9d22e)#define BT\_HCI\_EVT\_ENCRYPT\_KEY\_REFRESH\_COMPLETE 0x30

[ 2541](structbt__hci__evt__encrypt__key__refresh__complete.md)struct [bt\_hci\_evt\_encrypt\_key\_refresh\_complete](structbt__hci__evt__encrypt__key__refresh__complete.md) {

[ 2542](structbt__hci__evt__encrypt__key__refresh__complete.md#afdd162cff0f1eedfe9e8ee7223b3226e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__encrypt__key__refresh__complete.md#afdd162cff0f1eedfe9e8ee7223b3226e);

[ 2543](structbt__hci__evt__encrypt__key__refresh__complete.md#af5562687a4f6e3a1e82cd1a81cec5ad6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__encrypt__key__refresh__complete.md#af5562687a4f6e3a1e82cd1a81cec5ad6);

2544} \_\_packed;

2545

[ 2546](hci__types_8h.md#a4d69a943660da9c1a6ffedb9b653ce3f)#define BT\_HCI\_EVT\_IO\_CAPA\_REQ 0x31

[ 2547](structbt__hci__evt__io__capa__req.md)struct [bt\_hci\_evt\_io\_capa\_req](structbt__hci__evt__io__capa__req.md) {

[ 2548](structbt__hci__evt__io__capa__req.md#a52412f7bd8f8dea391904b9f2444b50a) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__evt__io__capa__req.md#a52412f7bd8f8dea391904b9f2444b50a);

2549} \_\_packed;

2550

[ 2551](hci__types_8h.md#a0f5cae40268568e25142eed9e3e5e639)#define BT\_HCI\_EVT\_IO\_CAPA\_RESP 0x32

[ 2552](structbt__hci__evt__io__capa__resp.md)struct [bt\_hci\_evt\_io\_capa\_resp](structbt__hci__evt__io__capa__resp.md) {

[ 2553](structbt__hci__evt__io__capa__resp.md#adac9c9f3999099fd460651e3b012fd0f) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__evt__io__capa__resp.md#adac9c9f3999099fd460651e3b012fd0f);

[ 2554](structbt__hci__evt__io__capa__resp.md#a851eae620ad90067957d4dec2f04efbe) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [capability](structbt__hci__evt__io__capa__resp.md#a851eae620ad90067957d4dec2f04efbe);

[ 2555](structbt__hci__evt__io__capa__resp.md#ab12325d1536fe6a75d0a137bea301e8f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [oob\_data](structbt__hci__evt__io__capa__resp.md#ab12325d1536fe6a75d0a137bea301e8f);

[ 2556](structbt__hci__evt__io__capa__resp.md#a160cb3aea96bf698520e11673a40b2d7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [authentication](structbt__hci__evt__io__capa__resp.md#a160cb3aea96bf698520e11673a40b2d7);

2557} \_\_packed;

2558

[ 2559](hci__types_8h.md#a78cdb5848d8a12a8cbea17767b3d02aa)#define BT\_HCI\_EVT\_USER\_CONFIRM\_REQ 0x33

[ 2560](structbt__hci__evt__user__confirm__req.md)struct [bt\_hci\_evt\_user\_confirm\_req](structbt__hci__evt__user__confirm__req.md) {

[ 2561](structbt__hci__evt__user__confirm__req.md#aaeec83c50764c322af7cd64259e54a97) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__evt__user__confirm__req.md#aaeec83c50764c322af7cd64259e54a97);

[ 2562](structbt__hci__evt__user__confirm__req.md#ac333729f5a7d9241ac26aeb7d3f77935) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [passkey](structbt__hci__evt__user__confirm__req.md#ac333729f5a7d9241ac26aeb7d3f77935);

2563} \_\_packed;

2564

[ 2565](hci__types_8h.md#a38a1bce81af39bb28d40e149f9309b69)#define BT\_HCI\_EVT\_USER\_PASSKEY\_REQ 0x34

[ 2566](structbt__hci__evt__user__passkey__req.md)struct [bt\_hci\_evt\_user\_passkey\_req](structbt__hci__evt__user__passkey__req.md) {

[ 2567](structbt__hci__evt__user__passkey__req.md#a7f1005423296906e0374050bc30781ce) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__evt__user__passkey__req.md#a7f1005423296906e0374050bc30781ce);

2568} \_\_packed;

2569

[ 2570](hci__types_8h.md#a7d2ba655c6954f90de04cafafccd727f)#define BT\_HCI\_EVT\_SSP\_COMPLETE 0x36

[ 2571](structbt__hci__evt__ssp__complete.md)struct [bt\_hci\_evt\_ssp\_complete](structbt__hci__evt__ssp__complete.md) {

[ 2572](structbt__hci__evt__ssp__complete.md#a33d3d47c1cef71cfb787a1195d9b4ec2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__ssp__complete.md#a33d3d47c1cef71cfb787a1195d9b4ec2);

[ 2573](structbt__hci__evt__ssp__complete.md#a5030cf334f97cdd982001b3278ed9db1) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__evt__ssp__complete.md#a5030cf334f97cdd982001b3278ed9db1);

2574} \_\_packed;

2575

[ 2576](hci__types_8h.md#a724d43899b16fcb89c235898a21c13b9)#define BT\_HCI\_EVT\_USER\_PASSKEY\_NOTIFY 0x3b

[ 2577](structbt__hci__evt__user__passkey__notify.md)struct [bt\_hci\_evt\_user\_passkey\_notify](structbt__hci__evt__user__passkey__notify.md) {

[ 2578](structbt__hci__evt__user__passkey__notify.md#af020e1cd131473fe06a193529a0499ac) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__evt__user__passkey__notify.md#af020e1cd131473fe06a193529a0499ac);

[ 2579](structbt__hci__evt__user__passkey__notify.md#a7f6a367e50d41cb7d8897db05db826be) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [passkey](structbt__hci__evt__user__passkey__notify.md#a7f6a367e50d41cb7d8897db05db826be);

2580} \_\_packed;

2581

[ 2582](hci__types_8h.md#ac1d7f9270323d7fa459e60b372cf998b)#define BT\_HCI\_EVT\_LE\_META\_EVENT 0x3e

[ 2583](structbt__hci__evt__le__meta__event.md)struct [bt\_hci\_evt\_le\_meta\_event](structbt__hci__evt__le__meta__event.md) {

[ 2584](structbt__hci__evt__le__meta__event.md#a536464a525f8d0f9df915be5ee3d33da) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent](structbt__hci__evt__le__meta__event.md#a536464a525f8d0f9df915be5ee3d33da);

2585} \_\_packed;

2586

[ 2587](hci__types_8h.md#a589975abd5d9532ba16d15ac21c5e81e)#define BT\_HCI\_EVT\_AUTH\_PAYLOAD\_TIMEOUT\_EXP 0x57

[ 2588](structbt__hci__evt__auth__payload__timeout__exp.md)struct [bt\_hci\_evt\_auth\_payload\_timeout\_exp](structbt__hci__evt__auth__payload__timeout__exp.md) {

[ 2589](structbt__hci__evt__auth__payload__timeout__exp.md#a799bc3c63fe5083d61d8bf152ef4cee7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__auth__payload__timeout__exp.md#a799bc3c63fe5083d61d8bf152ef4cee7);

2590} \_\_packed;

2591

[ 2592](hci__types_8h.md#a150ea8f2095d8510bde3ebd65d521c29)#define BT\_HCI\_ROLE\_CENTRAL 0x00

[ 2593](hci__types_8h.md#a9ca37afd4638ef94cdd55302bd4c99b3)#define BT\_HCI\_ROLE\_PERIPHERAL 0x01

2594

[ 2595](hci__types_8h.md#a2c3c4f81903d1860f21880c7c3cfbaa7)#define BT\_HCI\_EVT\_LE\_CONN\_COMPLETE 0x01

[ 2596](structbt__hci__evt__le__conn__complete.md)struct [bt\_hci\_evt\_le\_conn\_complete](structbt__hci__evt__le__conn__complete.md) {

[ 2597](structbt__hci__evt__le__conn__complete.md#a897981117139c0e53ea7275b689f3799) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__conn__complete.md#a897981117139c0e53ea7275b689f3799);

[ 2598](structbt__hci__evt__le__conn__complete.md#a67618a1efa0149fadc1063a719d5b674) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__conn__complete.md#a67618a1efa0149fadc1063a719d5b674);

[ 2599](structbt__hci__evt__le__conn__complete.md#a8455e714d4333d90c2f117892f3dcd6f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [role](structbt__hci__evt__le__conn__complete.md#a8455e714d4333d90c2f117892f3dcd6f);

[ 2600](structbt__hci__evt__le__conn__complete.md#a97e1aaa10832292ddfe4ee6731ef8999) [bt\_addr\_le\_t](structbt__addr__le__t.md) [peer\_addr](structbt__hci__evt__le__conn__complete.md#a97e1aaa10832292ddfe4ee6731ef8999);

[ 2601](structbt__hci__evt__le__conn__complete.md#abe4bc0407d0295329631cb14672a7ee7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__hci__evt__le__conn__complete.md#abe4bc0407d0295329631cb14672a7ee7);

[ 2602](structbt__hci__evt__le__conn__complete.md#ab60cb42ecc83632c61656cd352b71cbe) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [latency](structbt__hci__evt__le__conn__complete.md#ab60cb42ecc83632c61656cd352b71cbe);

[ 2603](structbt__hci__evt__le__conn__complete.md#a4a90c9824d167b6c45b301e18bfe7f17) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [supv\_timeout](structbt__hci__evt__le__conn__complete.md#a4a90c9824d167b6c45b301e18bfe7f17);

[ 2604](structbt__hci__evt__le__conn__complete.md#a3fff4c3b30da5922f75d36d97fdeee33) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [clock\_accuracy](structbt__hci__evt__le__conn__complete.md#a3fff4c3b30da5922f75d36d97fdeee33);

2605} \_\_packed;

2606

[ 2607](hci__types_8h.md#a56f7acd075e03694d966d949f637946c)#define BT\_HCI\_LE\_RSSI\_NOT\_AVAILABLE 0x7F

2608

[ 2609](hci__types_8h.md#a1a93b78bdbb29982d989aea5eae5ec19)#define BT\_HCI\_EVT\_LE\_ADVERTISING\_REPORT 0x02

[ 2610](structbt__hci__evt__le__advertising__info.md)struct [bt\_hci\_evt\_le\_advertising\_info](structbt__hci__evt__le__advertising__info.md) {

[ 2611](structbt__hci__evt__le__advertising__info.md#a5943685ccd3491a883ba9450f700bb86) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [evt\_type](structbt__hci__evt__le__advertising__info.md#a5943685ccd3491a883ba9450f700bb86);

[ 2612](structbt__hci__evt__le__advertising__info.md#a1d6863f1a601a2df9d772e3cc1fec118) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__hci__evt__le__advertising__info.md#a1d6863f1a601a2df9d772e3cc1fec118);

[ 2613](structbt__hci__evt__le__advertising__info.md#a11c223103bf89300bd90cb8725746121) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [length](structbt__hci__evt__le__advertising__info.md#a11c223103bf89300bd90cb8725746121);

[ 2614](structbt__hci__evt__le__advertising__info.md#af7d9d720ca67714f2a809e2530a1ff98) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__hci__evt__le__advertising__info.md#af7d9d720ca67714f2a809e2530a1ff98)[0];

2615} \_\_packed;

[ 2616](structbt__hci__evt__le__advertising__report.md)struct [bt\_hci\_evt\_le\_advertising\_report](structbt__hci__evt__le__advertising__report.md) {

[ 2617](structbt__hci__evt__le__advertising__report.md#ac69aab36aa421630357e4c6706c13e75) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_reports](structbt__hci__evt__le__advertising__report.md#ac69aab36aa421630357e4c6706c13e75);

[ 2618](structbt__hci__evt__le__advertising__report.md#a9762be19de1f24be4d4626e7e2f8205d) struct [bt\_hci\_evt\_le\_advertising\_info](structbt__hci__evt__le__advertising__info.md) [adv\_info](structbt__hci__evt__le__advertising__report.md#a9762be19de1f24be4d4626e7e2f8205d)[0];

2619} \_\_packed;

2620

[ 2621](hci__types_8h.md#aeef912e71549d4b5a0d8b293074a909c)#define BT\_HCI\_EVT\_LE\_CONN\_UPDATE\_COMPLETE 0x03

[ 2622](structbt__hci__evt__le__conn__update__complete.md)struct [bt\_hci\_evt\_le\_conn\_update\_complete](structbt__hci__evt__le__conn__update__complete.md) {

[ 2623](structbt__hci__evt__le__conn__update__complete.md#ad428bd5e29d40f7551ccdd0747e429d6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__conn__update__complete.md#ad428bd5e29d40f7551ccdd0747e429d6);

[ 2624](structbt__hci__evt__le__conn__update__complete.md#a81c0688a5e3b4b3a4d92fbc756a068d5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__conn__update__complete.md#a81c0688a5e3b4b3a4d92fbc756a068d5);

[ 2625](structbt__hci__evt__le__conn__update__complete.md#a69aa00c0c50978b2aa620aad671119f3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__hci__evt__le__conn__update__complete.md#a69aa00c0c50978b2aa620aad671119f3);

[ 2626](structbt__hci__evt__le__conn__update__complete.md#ade2421709a35e0cd0fce3a4d992470c3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [latency](structbt__hci__evt__le__conn__update__complete.md#ade2421709a35e0cd0fce3a4d992470c3);

[ 2627](structbt__hci__evt__le__conn__update__complete.md#aca728975619a10a6e3280b127b59f2f1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [supv\_timeout](structbt__hci__evt__le__conn__update__complete.md#aca728975619a10a6e3280b127b59f2f1);

2628} \_\_packed;

2629

[ 2630](hci__types_8h.md#a8b1653caabce8474fba132343aa62f56)#define BT\_HCI\_EVT\_LE\_REMOTE\_FEAT\_COMPLETE 0x04

[ 2631](structbt__hci__evt__le__remote__feat__complete.md)struct [bt\_hci\_evt\_le\_remote\_feat\_complete](structbt__hci__evt__le__remote__feat__complete.md) {

[ 2632](structbt__hci__evt__le__remote__feat__complete.md#a8a80bade7644f986fec41462843d8319) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__remote__feat__complete.md#a8a80bade7644f986fec41462843d8319);

[ 2633](structbt__hci__evt__le__remote__feat__complete.md#a9a0da26d9415169f02b6c9472120afe7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__remote__feat__complete.md#a9a0da26d9415169f02b6c9472120afe7);

[ 2634](structbt__hci__evt__le__remote__feat__complete.md#a61101c21e317aa07b08725a7ffbb4b81) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [features](structbt__hci__evt__le__remote__feat__complete.md#a61101c21e317aa07b08725a7ffbb4b81)[8];

2635} \_\_packed;

2636

[ 2637](hci__types_8h.md#a9efb73da285829cde0e4c1ac28a48f1a)#define BT\_HCI\_EVT\_LE\_LTK\_REQUEST 0x05

[ 2638](structbt__hci__evt__le__ltk__request.md)struct [bt\_hci\_evt\_le\_ltk\_request](structbt__hci__evt__le__ltk__request.md) {

[ 2639](structbt__hci__evt__le__ltk__request.md#aed00ae384cb7d0deace8d0cc0f8e0068) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__ltk__request.md#aed00ae384cb7d0deace8d0cc0f8e0068);

[ 2640](structbt__hci__evt__le__ltk__request.md#a765cba614cd7a972156b6361536b753f) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [rand](structbt__hci__evt__le__ltk__request.md#a765cba614cd7a972156b6361536b753f);

[ 2641](structbt__hci__evt__le__ltk__request.md#a54d5cbde249349337595085c6c3cabad) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [ediv](structbt__hci__evt__le__ltk__request.md#a54d5cbde249349337595085c6c3cabad);

2642} \_\_packed;

2643

[ 2644](hci__types_8h.md#a77072c10df87395e7e649307b975fb69)#define BT\_HCI\_EVT\_LE\_CONN\_PARAM\_REQ 0x06

[ 2645](structbt__hci__evt__le__conn__param__req.md)struct [bt\_hci\_evt\_le\_conn\_param\_req](structbt__hci__evt__le__conn__param__req.md) {

[ 2646](structbt__hci__evt__le__conn__param__req.md#a4746a001a070f152a3c1c870a7e74df1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__conn__param__req.md#a4746a001a070f152a3c1c870a7e74df1);

[ 2647](structbt__hci__evt__le__conn__param__req.md#a9a9dfc026feb46337b0a36920204b24e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval\_min](structbt__hci__evt__le__conn__param__req.md#a9a9dfc026feb46337b0a36920204b24e);

[ 2648](structbt__hci__evt__le__conn__param__req.md#a0ed70d1a89f270073f78823d38af6ac9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval\_max](structbt__hci__evt__le__conn__param__req.md#a0ed70d1a89f270073f78823d38af6ac9);

[ 2649](structbt__hci__evt__le__conn__param__req.md#a9f61f0a3e6b6d2e2c6af2f4aef625b75) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [latency](structbt__hci__evt__le__conn__param__req.md#a9f61f0a3e6b6d2e2c6af2f4aef625b75);

[ 2650](structbt__hci__evt__le__conn__param__req.md#ae34de4a3d3e3e4686391eb9d9585dc87) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structbt__hci__evt__le__conn__param__req.md#ae34de4a3d3e3e4686391eb9d9585dc87);

2651} \_\_packed;

2652

[ 2653](hci__types_8h.md#a064cf9e32616c6f94041d138a5bf4819)#define BT\_HCI\_EVT\_LE\_DATA\_LEN\_CHANGE 0x07

[ 2654](structbt__hci__evt__le__data__len__change.md)struct [bt\_hci\_evt\_le\_data\_len\_change](structbt__hci__evt__le__data__len__change.md) {

[ 2655](structbt__hci__evt__le__data__len__change.md#a62ebc2f337f23f678c651bf3a276a2a7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__data__len__change.md#a62ebc2f337f23f678c651bf3a276a2a7);

[ 2656](structbt__hci__evt__le__data__len__change.md#ae5ce481170336acafbe85687c672281b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_tx\_octets](structbt__hci__evt__le__data__len__change.md#ae5ce481170336acafbe85687c672281b);

[ 2657](structbt__hci__evt__le__data__len__change.md#a8264e7ec4aa37e9a699f81d0c56afa40) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_tx\_time](structbt__hci__evt__le__data__len__change.md#a8264e7ec4aa37e9a699f81d0c56afa40);

[ 2658](structbt__hci__evt__le__data__len__change.md#a60ecd89a8bbf06ae55b577e3d708d16f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_rx\_octets](structbt__hci__evt__le__data__len__change.md#a60ecd89a8bbf06ae55b577e3d708d16f);

[ 2659](structbt__hci__evt__le__data__len__change.md#a90771e400b998565e7a8bbf4288edd01) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_rx\_time](structbt__hci__evt__le__data__len__change.md#a90771e400b998565e7a8bbf4288edd01);

2660} \_\_packed;

2661

[ 2662](hci__types_8h.md#abe39909eb984dd6edd1220f9c6744546)#define BT\_HCI\_EVT\_LE\_P256\_PUBLIC\_KEY\_COMPLETE 0x08

[ 2663](structbt__hci__evt__le__p256__public__key__complete.md)struct [bt\_hci\_evt\_le\_p256\_public\_key\_complete](structbt__hci__evt__le__p256__public__key__complete.md) {

[ 2664](structbt__hci__evt__le__p256__public__key__complete.md#a57d51fca3a707b445db2534d1e175241) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__p256__public__key__complete.md#a57d51fca3a707b445db2534d1e175241);

[ 2665](structbt__hci__evt__le__p256__public__key__complete.md#af482f81d438b878fb826edbac8d84833) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key](structbt__hci__evt__le__p256__public__key__complete.md#af482f81d438b878fb826edbac8d84833)[64];

2666} \_\_packed;

2667

[ 2668](hci__types_8h.md#a8ab77f497135e365fb9e895dc2d4d453)#define BT\_HCI\_EVT\_LE\_GENERATE\_DHKEY\_COMPLETE 0x09

[ 2669](structbt__hci__evt__le__generate__dhkey__complete.md)struct [bt\_hci\_evt\_le\_generate\_dhkey\_complete](structbt__hci__evt__le__generate__dhkey__complete.md) {

[ 2670](structbt__hci__evt__le__generate__dhkey__complete.md#a3d10643dd45a71b71d35dfa455ed8590) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__generate__dhkey__complete.md#a3d10643dd45a71b71d35dfa455ed8590);

[ 2671](structbt__hci__evt__le__generate__dhkey__complete.md#a8cd8ece786c1443ed43bd3b8fcd4d9bf) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dhkey](structbt__hci__evt__le__generate__dhkey__complete.md#a8cd8ece786c1443ed43bd3b8fcd4d9bf)[32];

2672} \_\_packed;

2673

[ 2674](hci__types_8h.md#a292de9ec009a80e23308ead618656b4f)#define BT\_HCI\_EVT\_LE\_ENH\_CONN\_COMPLETE 0x0a

[ 2675](structbt__hci__evt__le__enh__conn__complete.md)struct [bt\_hci\_evt\_le\_enh\_conn\_complete](structbt__hci__evt__le__enh__conn__complete.md) {

[ 2676](structbt__hci__evt__le__enh__conn__complete.md#ae26575416658bf285c45f57ddf426eb2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__enh__conn__complete.md#ae26575416658bf285c45f57ddf426eb2);

[ 2677](structbt__hci__evt__le__enh__conn__complete.md#a13ceff445de6a89f6ea0e832e8b3fba9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__enh__conn__complete.md#a13ceff445de6a89f6ea0e832e8b3fba9);

[ 2678](structbt__hci__evt__le__enh__conn__complete.md#af24298f8c1d58882b4962a14086fc5c7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [role](structbt__hci__evt__le__enh__conn__complete.md#af24298f8c1d58882b4962a14086fc5c7);

[ 2679](structbt__hci__evt__le__enh__conn__complete.md#a4906d6991489e95f8c74aacf5ad8c22e) [bt\_addr\_le\_t](structbt__addr__le__t.md) [peer\_addr](structbt__hci__evt__le__enh__conn__complete.md#a4906d6991489e95f8c74aacf5ad8c22e);

[ 2680](structbt__hci__evt__le__enh__conn__complete.md#ab275bcb4a3dd09525b446c01e4e5fdad) [bt\_addr\_t](structbt__addr__t.md) [local\_rpa](structbt__hci__evt__le__enh__conn__complete.md#ab275bcb4a3dd09525b446c01e4e5fdad);

[ 2681](structbt__hci__evt__le__enh__conn__complete.md#a4ece4379733f1ab404fa03f4794192a4) [bt\_addr\_t](structbt__addr__t.md) [peer\_rpa](structbt__hci__evt__le__enh__conn__complete.md#a4ece4379733f1ab404fa03f4794192a4);

[ 2682](structbt__hci__evt__le__enh__conn__complete.md#ac0565ecf0c459275d147933bbdaa9fbc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__hci__evt__le__enh__conn__complete.md#ac0565ecf0c459275d147933bbdaa9fbc);

[ 2683](structbt__hci__evt__le__enh__conn__complete.md#a7276bf433c21ffcd3582463492af107b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [latency](structbt__hci__evt__le__enh__conn__complete.md#a7276bf433c21ffcd3582463492af107b);

[ 2684](structbt__hci__evt__le__enh__conn__complete.md#aa99df131f3fb0330ff8051015d2b78dc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [supv\_timeout](structbt__hci__evt__le__enh__conn__complete.md#aa99df131f3fb0330ff8051015d2b78dc);

[ 2685](structbt__hci__evt__le__enh__conn__complete.md#a5641e5cb17df4613cd85f5ad3ba8541c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [clock\_accuracy](structbt__hci__evt__le__enh__conn__complete.md#a5641e5cb17df4613cd85f5ad3ba8541c);

2686} \_\_packed;

2687

[ 2688](hci__types_8h.md#a417144400fd8d7f5c05e050950c75dab)#define BT\_HCI\_EVT\_LE\_DIRECT\_ADV\_REPORT 0x0b

[ 2689](structbt__hci__evt__le__direct__adv__info.md)struct [bt\_hci\_evt\_le\_direct\_adv\_info](structbt__hci__evt__le__direct__adv__info.md) {

[ 2690](structbt__hci__evt__le__direct__adv__info.md#aed957c96860c5f92f9485ab743ce832b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [evt\_type](structbt__hci__evt__le__direct__adv__info.md#aed957c96860c5f92f9485ab743ce832b);

[ 2691](structbt__hci__evt__le__direct__adv__info.md#a66bbb3e53d84e8c39b216edf91ad131d) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__hci__evt__le__direct__adv__info.md#a66bbb3e53d84e8c39b216edf91ad131d);

[ 2692](structbt__hci__evt__le__direct__adv__info.md#ad4ca2d5395bc4c5b95527ac1491c940e) [bt\_addr\_le\_t](structbt__addr__le__t.md) [dir\_addr](structbt__hci__evt__le__direct__adv__info.md#ad4ca2d5395bc4c5b95527ac1491c940e);

[ 2693](structbt__hci__evt__le__direct__adv__info.md#a013e5d53ed53e4cd0b923a55c68e20bc) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__hci__evt__le__direct__adv__info.md#a013e5d53ed53e4cd0b923a55c68e20bc);

2694} \_\_packed;

[ 2695](structbt__hci__evt__le__direct__adv__report.md)struct [bt\_hci\_evt\_le\_direct\_adv\_report](structbt__hci__evt__le__direct__adv__report.md) {

[ 2696](structbt__hci__evt__le__direct__adv__report.md#ae8d1f96739c8fda8827d1c0521f00f94) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_reports](structbt__hci__evt__le__direct__adv__report.md#ae8d1f96739c8fda8827d1c0521f00f94);

[ 2697](structbt__hci__evt__le__direct__adv__report.md#a82800d58d4c3ed1fca49b6575bd8f957) struct [bt\_hci\_evt\_le\_direct\_adv\_info](structbt__hci__evt__le__direct__adv__info.md) [direct\_adv\_info](structbt__hci__evt__le__direct__adv__report.md#a82800d58d4c3ed1fca49b6575bd8f957)[0];

2698} \_\_packed;

2699

[ 2700](hci__types_8h.md#a44f18d799280d47ec09376e7cffd4c40)#define BT\_HCI\_EVT\_LE\_PHY\_UPDATE\_COMPLETE 0x0c

[ 2701](structbt__hci__evt__le__phy__update__complete.md)struct [bt\_hci\_evt\_le\_phy\_update\_complete](structbt__hci__evt__le__phy__update__complete.md) {

[ 2702](structbt__hci__evt__le__phy__update__complete.md#a927a9e6982b29ecd4c3972b19a9bcdc2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__phy__update__complete.md#a927a9e6982b29ecd4c3972b19a9bcdc2);

[ 2703](structbt__hci__evt__le__phy__update__complete.md#a70f472edef3b25fb23490ea6dcce9d43) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__phy__update__complete.md#a70f472edef3b25fb23490ea6dcce9d43);

[ 2704](structbt__hci__evt__le__phy__update__complete.md#ad184e10b7af71582db64ec5d3a66cff9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_phy](structbt__hci__evt__le__phy__update__complete.md#ad184e10b7af71582db64ec5d3a66cff9);

[ 2705](structbt__hci__evt__le__phy__update__complete.md#ad792ffec08aa8e383009e2e353a03fcd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_phy](structbt__hci__evt__le__phy__update__complete.md#ad792ffec08aa8e383009e2e353a03fcd);

2706} \_\_packed;

2707

[ 2708](hci__types_8h.md#ad63fc0c42f0253dfe06b81324a05f505)#define BT\_HCI\_EVT\_LE\_EXT\_ADVERTISING\_REPORT 0x0d

2709

[ 2710](hci__types_8h.md#ae448216e385d4e1175b92e112c941140)#define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_CONN BIT(0)

[ 2711](hci__types_8h.md#a54673fbd23e05fec88e1f6bca6aa70e9)#define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_SCAN BIT(1)

[ 2712](hci__types_8h.md#a1b5738583447011ee63350787236b3b8)#define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DIRECT BIT(2)

[ 2713](hci__types_8h.md#a485843f24c09934b1f15d5274b4a56d5)#define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_SCAN\_RSP BIT(3)

[ 2714](hci__types_8h.md#a0879fbea8bf3acbe56e25f3693c81ad6)#define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_LEGACY BIT(4)

2715

[ 2716](hci__types_8h.md#a9557bf3ea41a526fb9d628d2fd3d5bea)#define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DATA\_STATUS(ev\_type) (((ev\_type) >> 5) & 0x03)

[ 2717](hci__types_8h.md#a85720f3d88c7fa5da9dc9cdffb94ec87)#define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DATA\_STATUS\_COMPLETE 0

[ 2718](hci__types_8h.md#ab7842a3081c9bf5288275b57337955f2)#define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DATA\_STATUS\_PARTIAL 1

[ 2719](hci__types_8h.md#abf119f5606440c075e61abcbfaa683c6)#define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DATA\_STATUS\_INCOMPLETE 2

[ 2720](hci__types_8h.md#ad9bcda2a43eed7e73112f2ef84cc6183)#define BT\_HCI\_LE\_ADV\_EVT\_TYPE\_DATA\_STATUS\_RX\_FAILED 0xFF

2721

[ 2722](structbt__hci__evt__le__ext__advertising__info.md)struct [bt\_hci\_evt\_le\_ext\_advertising\_info](structbt__hci__evt__le__ext__advertising__info.md) {

[ 2723](structbt__hci__evt__le__ext__advertising__info.md#a040c27dbcb337162f7ca857b8cb84cfe) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [evt\_type](structbt__hci__evt__le__ext__advertising__info.md#a040c27dbcb337162f7ca857b8cb84cfe);

[ 2724](structbt__hci__evt__le__ext__advertising__info.md#acec6858e41ae1b44a2a2ee6d6dbc294d) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__hci__evt__le__ext__advertising__info.md#acec6858e41ae1b44a2a2ee6d6dbc294d);

[ 2725](structbt__hci__evt__le__ext__advertising__info.md#a088f0e6ea0dfbad25d5f72d0741f7d6d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [prim\_phy](structbt__hci__evt__le__ext__advertising__info.md#a088f0e6ea0dfbad25d5f72d0741f7d6d);

[ 2726](structbt__hci__evt__le__ext__advertising__info.md#af4d863e12e6f8f19426a14af292fa6d2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sec\_phy](structbt__hci__evt__le__ext__advertising__info.md#af4d863e12e6f8f19426a14af292fa6d2);

[ 2727](structbt__hci__evt__le__ext__advertising__info.md#a5b4d4adff4d97c06311a76abd9847727) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__hci__evt__le__ext__advertising__info.md#a5b4d4adff4d97c06311a76abd9847727);

[ 2728](structbt__hci__evt__le__ext__advertising__info.md#a39217e77e495e8c4c6288917f8e4d2dc) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__hci__evt__le__ext__advertising__info.md#a39217e77e495e8c4c6288917f8e4d2dc);

[ 2729](structbt__hci__evt__le__ext__advertising__info.md#a6213edbc3ae30f02a6bf2d8e069cd035) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__hci__evt__le__ext__advertising__info.md#a6213edbc3ae30f02a6bf2d8e069cd035);

[ 2730](structbt__hci__evt__le__ext__advertising__info.md#a7da4e49c49eccbf009491bb7da01e111) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__hci__evt__le__ext__advertising__info.md#a7da4e49c49eccbf009491bb7da01e111);

[ 2731](structbt__hci__evt__le__ext__advertising__info.md#a37f4e4981566b43d6e7c7dfffc5b13fb) [bt\_addr\_le\_t](structbt__addr__le__t.md) [direct\_addr](structbt__hci__evt__le__ext__advertising__info.md#a37f4e4981566b43d6e7c7dfffc5b13fb);

[ 2732](structbt__hci__evt__le__ext__advertising__info.md#a20ca10813f6b3aaba2756a5fe00d3878) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [length](structbt__hci__evt__le__ext__advertising__info.md#a20ca10813f6b3aaba2756a5fe00d3878);

[ 2733](structbt__hci__evt__le__ext__advertising__info.md#a9e5536277b0132c8374147677a787b68) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__hci__evt__le__ext__advertising__info.md#a9e5536277b0132c8374147677a787b68)[0];

2734} \_\_packed;

[ 2735](structbt__hci__evt__le__ext__advertising__report.md)struct [bt\_hci\_evt\_le\_ext\_advertising\_report](structbt__hci__evt__le__ext__advertising__report.md) {

[ 2736](structbt__hci__evt__le__ext__advertising__report.md#a72fc9736934b415e88c51a1f96179871) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_reports](structbt__hci__evt__le__ext__advertising__report.md#a72fc9736934b415e88c51a1f96179871);

[ 2737](structbt__hci__evt__le__ext__advertising__report.md#a84b9c47a79ccea04198721e2f05ac1a8) struct [bt\_hci\_evt\_le\_ext\_advertising\_info](structbt__hci__evt__le__ext__advertising__info.md) [adv\_info](structbt__hci__evt__le__ext__advertising__report.md#a84b9c47a79ccea04198721e2f05ac1a8)[0];

2738} \_\_packed;

2739

[ 2740](hci__types_8h.md#a8c721c9e5df496900f661755aff7cbd6)#define BT\_HCI\_EVT\_LE\_PER\_ADV\_SYNC\_ESTABLISHED 0x0e

[ 2741](structbt__hci__evt__le__per__adv__sync__established.md)struct [bt\_hci\_evt\_le\_per\_adv\_sync\_established](structbt__hci__evt__le__per__adv__sync__established.md) {

[ 2742](structbt__hci__evt__le__per__adv__sync__established.md#a9ebe918fee3121168dc5b45e64aaf263) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__per__adv__sync__established.md#a9ebe918fee3121168dc5b45e64aaf263);

[ 2743](structbt__hci__evt__le__per__adv__sync__established.md#a3af8529a858992f347ce9570c5696133) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__per__adv__sync__established.md#a3af8529a858992f347ce9570c5696133);

[ 2744](structbt__hci__evt__le__per__adv__sync__established.md#ab11929ef8d3c71c6f2cb7c549be21282) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__hci__evt__le__per__adv__sync__established.md#ab11929ef8d3c71c6f2cb7c549be21282);

[ 2745](structbt__hci__evt__le__per__adv__sync__established.md#adf65527ea968f4ece37d7e3c91c795d1) [bt\_addr\_le\_t](structbt__addr__le__t.md) [adv\_addr](structbt__hci__evt__le__per__adv__sync__established.md#adf65527ea968f4ece37d7e3c91c795d1);

[ 2746](structbt__hci__evt__le__per__adv__sync__established.md#ab7ce6f56a69b54f02cde8fdae6860e42) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__evt__le__per__adv__sync__established.md#ab7ce6f56a69b54f02cde8fdae6860e42);

[ 2747](structbt__hci__evt__le__per__adv__sync__established.md#a4873b917a5bc140bb2f04ad2bee5dd69) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__hci__evt__le__per__adv__sync__established.md#a4873b917a5bc140bb2f04ad2bee5dd69);

[ 2748](structbt__hci__evt__le__per__adv__sync__established.md#aee68069899cc10bc38ad9fb95cf9b7b7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [clock\_accuracy](structbt__hci__evt__le__per__adv__sync__established.md#aee68069899cc10bc38ad9fb95cf9b7b7);

2749} \_\_packed;

2750

[ 2751](hci__types_8h.md#a31fc096530a89e63d4967d7ddd85b753)#define BT\_HCI\_EVT\_LE\_PER\_ADVERTISING\_REPORT 0x0f

[ 2752](structbt__hci__evt__le__per__advertising__report.md)struct [bt\_hci\_evt\_le\_per\_advertising\_report](structbt__hci__evt__le__per__advertising__report.md) {

[ 2753](structbt__hci__evt__le__per__advertising__report.md#af81ce5bb18ef7fa1d94d00412886b081) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__per__advertising__report.md#af81ce5bb18ef7fa1d94d00412886b081);

[ 2754](structbt__hci__evt__le__per__advertising__report.md#a3a09aca94284a9e4af765d4da543698e) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__hci__evt__le__per__advertising__report.md#a3a09aca94284a9e4af765d4da543698e);

[ 2755](structbt__hci__evt__le__per__advertising__report.md#af874c29b89326877b499f6be1052a626) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__hci__evt__le__per__advertising__report.md#af874c29b89326877b499f6be1052a626);

[ 2756](structbt__hci__evt__le__per__advertising__report.md#aa683d1a4bd3a851f26b3028f566b76e4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__hci__evt__le__per__advertising__report.md#aa683d1a4bd3a851f26b3028f566b76e4);

[ 2757](structbt__hci__evt__le__per__advertising__report.md#abf23b23a12cbfeb7f996e71e2fe8b11c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_status](structbt__hci__evt__le__per__advertising__report.md#abf23b23a12cbfeb7f996e71e2fe8b11c);

[ 2758](structbt__hci__evt__le__per__advertising__report.md#a0ab1d3c5d7eb1487862451cc65c66a76) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [length](structbt__hci__evt__le__per__advertising__report.md#a0ab1d3c5d7eb1487862451cc65c66a76);

[ 2759](structbt__hci__evt__le__per__advertising__report.md#a1f9cdfc01e46e59e957b0c557bae620a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__hci__evt__le__per__advertising__report.md#a1f9cdfc01e46e59e957b0c557bae620a)[0];

2760} \_\_packed;

2761

[ 2762](hci__types_8h.md#ab303042eabbeb133e202bdcfbd38666c)#define BT\_HCI\_EVT\_LE\_PER\_ADV\_SYNC\_LOST 0x10

[ 2763](structbt__hci__evt__le__per__adv__sync__lost.md)struct [bt\_hci\_evt\_le\_per\_adv\_sync\_lost](structbt__hci__evt__le__per__adv__sync__lost.md) {

[ 2764](structbt__hci__evt__le__per__adv__sync__lost.md#a286d534634411da53a2bda8cdfb077f8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__per__adv__sync__lost.md#a286d534634411da53a2bda8cdfb077f8);

2765} \_\_packed;

2766

[ 2767](hci__types_8h.md#a7234c851946c6025aa850c9bf28faab0)#define BT\_HCI\_EVT\_LE\_SCAN\_TIMEOUT 0x11

2768

[ 2769](hci__types_8h.md#a398afcbdb732fe76ec01db1393721ab2)#define BT\_HCI\_EVT\_LE\_ADV\_SET\_TERMINATED 0x12

[ 2770](structbt__hci__evt__le__adv__set__terminated.md)struct [bt\_hci\_evt\_le\_adv\_set\_terminated](structbt__hci__evt__le__adv__set__terminated.md) {

[ 2771](structbt__hci__evt__le__adv__set__terminated.md#a583409e2dc912af2bd5e83124fce3a72) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__adv__set__terminated.md#a583409e2dc912af2bd5e83124fce3a72);

[ 2772](structbt__hci__evt__le__adv__set__terminated.md#af35564406269144cfa2532cd510aa0bd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_handle](structbt__hci__evt__le__adv__set__terminated.md#af35564406269144cfa2532cd510aa0bd);

[ 2773](structbt__hci__evt__le__adv__set__terminated.md#af2503ee8e1c9add6927fa65b69c48551) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__evt__le__adv__set__terminated.md#af2503ee8e1c9add6927fa65b69c48551);

[ 2774](structbt__hci__evt__le__adv__set__terminated.md#a192f13d6223e437261a225e6b28d04db) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_completed\_ext\_adv\_evts](structbt__hci__evt__le__adv__set__terminated.md#a192f13d6223e437261a225e6b28d04db);

2775} \_\_packed;

2776

[ 2777](hci__types_8h.md#a0ebf19a602a02c00793b3de64392e514)#define BT\_HCI\_EVT\_LE\_SCAN\_REQ\_RECEIVED 0x13

[ 2778](structbt__hci__evt__le__scan__req__received.md)struct [bt\_hci\_evt\_le\_scan\_req\_received](structbt__hci__evt__le__scan__req__received.md) {

[ 2779](structbt__hci__evt__le__scan__req__received.md#a62c6d5e5b7079665c0aea8eb676a0433) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle](structbt__hci__evt__le__scan__req__received.md#a62c6d5e5b7079665c0aea8eb676a0433);

[ 2780](structbt__hci__evt__le__scan__req__received.md#a7dca5ad876dc97859a139d8bd4b207af) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__hci__evt__le__scan__req__received.md#a7dca5ad876dc97859a139d8bd4b207af);

2781} \_\_packed;

2782

[ 2783](hci__types_8h.md#ac8dcea08127aa5ce2a870d64fcc843f1)#define BT\_HCI\_LE\_CHAN\_SEL\_ALGO\_1 0x00

[ 2784](hci__types_8h.md#a7a4b52643c764233427314732896d353)#define BT\_HCI\_LE\_CHAN\_SEL\_ALGO\_2 0x01

2785

[ 2786](hci__types_8h.md#a4f012a8357e5bb17b5dd04128bd39911)#define BT\_HCI\_EVT\_LE\_CHAN\_SEL\_ALGO 0x14

[ 2787](structbt__hci__evt__le__chan__sel__algo.md)struct [bt\_hci\_evt\_le\_chan\_sel\_algo](structbt__hci__evt__le__chan__sel__algo.md) {

[ 2788](structbt__hci__evt__le__chan__sel__algo.md#a16393279e08073dad549e111e610c8e8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__chan__sel__algo.md#a16393279e08073dad549e111e610c8e8);

[ 2789](structbt__hci__evt__le__chan__sel__algo.md#a976a62e81b094a59ce42cb6ad3ce45ac) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [chan\_sel\_algo](structbt__hci__evt__le__chan__sel__algo.md#a976a62e81b094a59ce42cb6ad3ce45ac);

2790} \_\_packed;

2791

[ 2792](hci__types_8h.md#ac1ce16d42df9eb71860e51a843dbc943)#define BT\_HCI\_LE\_CTE\_CRC\_OK 0x0

[ 2793](hci__types_8h.md#a3f787f516c3cc233fc700c08552a4034)#define BT\_HCI\_LE\_CTE\_CRC\_ERR\_CTE\_BASED\_TIME 0x1

[ 2794](hci__types_8h.md#a478bc1be161e0b1eb05667bc8b6c9ae5)#define BT\_HCI\_LE\_CTE\_CRC\_ERR\_CTE\_BASED\_OTHER 0x2

[ 2795](hci__types_8h.md#a3bc1e15287e6173d45b7d1e981d6e90e)#define BT\_HCI\_LE\_CTE\_INSUFFICIENT\_RESOURCES 0xFF

2796

[ 2797](hci__types_8h.md#a87364c12ecac6b05681469c9450f887e)#define B\_HCI\_LE\_CTE\_REPORT\_SAMPLE\_COUNT\_MIN 0x9

[ 2798](hci__types_8h.md#a9693358ac3b7d9da498ca557fa0d1410)#define B\_HCI\_LE\_CTE\_REPORT\_SAMPLE\_COUNT\_MAX 0x52

2799

[ 2800](hci__types_8h.md#a40156c4680916b289b00b1546e0d5bb0)#define BT\_HCI\_LE\_CTE\_REPORT\_NO\_VALID\_SAMPLE 0x80

2801

[ 2802](hci__types_8h.md#a04c4a4567eaad7c592f2181e47768522)#define BT\_HCI\_EVT\_LE\_CONNECTIONLESS\_IQ\_REPORT 0x15

[ 2803](structbt__hci__le__iq__sample.md)struct [bt\_hci\_le\_iq\_sample](structbt__hci__le__iq__sample.md) {

[ 2804](structbt__hci__le__iq__sample.md#aacf452456eecd4ad4dab083593b11104) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [i](structbt__hci__le__iq__sample.md#aacf452456eecd4ad4dab083593b11104);

[ 2805](structbt__hci__le__iq__sample.md#a775b6e0ab1842594bc00998faec613f3) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [q](structbt__hci__le__iq__sample.md#a775b6e0ab1842594bc00998faec613f3);

2806};

2807

[ 2808](structbt__hci__evt__le__connectionless__iq__report.md)struct [bt\_hci\_evt\_le\_connectionless\_iq\_report](structbt__hci__evt__le__connectionless__iq__report.md) {

[ 2809](structbt__hci__evt__le__connectionless__iq__report.md#a36f853d29b8dae1dd393546bbdec5ae2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sync\_handle](structbt__hci__evt__le__connectionless__iq__report.md#a36f853d29b8dae1dd393546bbdec5ae2);

[ 2810](structbt__hci__evt__le__connectionless__iq__report.md#af50e710884a17191d22f652eaf5788fd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [chan\_idx](structbt__hci__evt__le__connectionless__iq__report.md#af50e710884a17191d22f652eaf5788fd);

[ 2811](structbt__hci__evt__le__connectionless__iq__report.md#a09112f3711aca00b56045c46958c0992) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [rssi](structbt__hci__evt__le__connectionless__iq__report.md#a09112f3711aca00b56045c46958c0992);

[ 2812](structbt__hci__evt__le__connectionless__iq__report.md#af8c2055666a97f3c8d95747c59515c31) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rssi\_ant\_id](structbt__hci__evt__le__connectionless__iq__report.md#af8c2055666a97f3c8d95747c59515c31);

[ 2813](structbt__hci__evt__le__connectionless__iq__report.md#a6b11b00199b002129c569cfec6e83174) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__hci__evt__le__connectionless__iq__report.md#a6b11b00199b002129c569cfec6e83174);

[ 2814](structbt__hci__evt__le__connectionless__iq__report.md#a9d9f0cfe343d81c44e8342b81e2a0608) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [slot\_durations](structbt__hci__evt__le__connectionless__iq__report.md#a9d9f0cfe343d81c44e8342b81e2a0608);

[ 2815](structbt__hci__evt__le__connectionless__iq__report.md#ab6fb0f6e32e32a3364ae79d867d9e640) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_status](structbt__hci__evt__le__connectionless__iq__report.md#ab6fb0f6e32e32a3364ae79d867d9e640);

[ 2816](structbt__hci__evt__le__connectionless__iq__report.md#abfeb0aaa411464bbd7bca927219144fb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [per\_evt\_counter](structbt__hci__evt__le__connectionless__iq__report.md#abfeb0aaa411464bbd7bca927219144fb);

[ 2817](structbt__hci__evt__le__connectionless__iq__report.md#a39109ea3f657d0566a73c7ca81bdd2b1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sample\_count](structbt__hci__evt__le__connectionless__iq__report.md#a39109ea3f657d0566a73c7ca81bdd2b1);

[ 2818](structbt__hci__evt__le__connectionless__iq__report.md#a1a81f2c8653d85dc29582eed67b4a2a8) struct [bt\_hci\_le\_iq\_sample](structbt__hci__le__iq__sample.md) [sample](structbt__hci__evt__le__connectionless__iq__report.md#a1a81f2c8653d85dc29582eed67b4a2a8)[0];

2819} \_\_packed;

2820

[ 2821](hci__types_8h.md#ace41ae5ec2a8f036aabf83ac94937a8b)#define BT\_HCI\_EVT\_LE\_CONNECTION\_IQ\_REPORT 0x16

[ 2822](structbt__hci__evt__le__connection__iq__report.md)struct [bt\_hci\_evt\_le\_connection\_iq\_report](structbt__hci__evt__le__connection__iq__report.md) {

[ 2823](structbt__hci__evt__le__connection__iq__report.md#a446f4eab3db19452a84023a676333d1d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__evt__le__connection__iq__report.md#a446f4eab3db19452a84023a676333d1d);

[ 2824](structbt__hci__evt__le__connection__iq__report.md#aa052e03491647acc9f7a6dc7d91cedcc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_phy](structbt__hci__evt__le__connection__iq__report.md#aa052e03491647acc9f7a6dc7d91cedcc);

[ 2825](structbt__hci__evt__le__connection__iq__report.md#ac01a14c591c8bd8e6313aff021ca8d61) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_chan\_idx](structbt__hci__evt__le__connection__iq__report.md#ac01a14c591c8bd8e6313aff021ca8d61);

[ 2826](structbt__hci__evt__le__connection__iq__report.md#a49e63523f7219174540666c7e5ab3550) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [rssi](structbt__hci__evt__le__connection__iq__report.md#a49e63523f7219174540666c7e5ab3550);

[ 2827](structbt__hci__evt__le__connection__iq__report.md#a135498a4abae604967f94840e2f88d2c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rssi\_ant\_id](structbt__hci__evt__le__connection__iq__report.md#a135498a4abae604967f94840e2f88d2c);

[ 2828](structbt__hci__evt__le__connection__iq__report.md#a0188ce28a6c0a2002ae2c64a7bd95e52) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__hci__evt__le__connection__iq__report.md#a0188ce28a6c0a2002ae2c64a7bd95e52);

[ 2829](structbt__hci__evt__le__connection__iq__report.md#a74670ca77bb2be81db2cee613dd9c82b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [slot\_durations](structbt__hci__evt__le__connection__iq__report.md#a74670ca77bb2be81db2cee613dd9c82b);

[ 2830](structbt__hci__evt__le__connection__iq__report.md#af66e8f09a4442b658b80a6eb4dd3064b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_status](structbt__hci__evt__le__connection__iq__report.md#af66e8f09a4442b658b80a6eb4dd3064b);

[ 2831](structbt__hci__evt__le__connection__iq__report.md#a1f388ba96bd52f9ce0f68bacb2945ed8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_evt\_counter](structbt__hci__evt__le__connection__iq__report.md#a1f388ba96bd52f9ce0f68bacb2945ed8);

[ 2832](structbt__hci__evt__le__connection__iq__report.md#a801dd9373935ba06175ac52237fea759) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sample\_count](structbt__hci__evt__le__connection__iq__report.md#a801dd9373935ba06175ac52237fea759);

[ 2833](structbt__hci__evt__le__connection__iq__report.md#a5acc2683312523a1137db7897a7373a6) struct [bt\_hci\_le\_iq\_sample](structbt__hci__le__iq__sample.md) [sample](structbt__hci__evt__le__connection__iq__report.md#a5acc2683312523a1137db7897a7373a6)[0];

2834} \_\_packed;

2835

[ 2836](hci__types_8h.md#a5e0814f9ca6e7fbc78b0778634ff075d)#define BT\_HCI\_CTE\_REQ\_STATUS\_RSP\_WITHOUT\_CTE 0x0

2837

[ 2838](hci__types_8h.md#aacaa203f0c8e23c6ca551df0375410e8)#define BT\_HCI\_EVT\_LE\_CTE\_REQUEST\_FAILED 0x17

[ 2839](structbt__hci__evt__le__cte__req__failed.md)struct [bt\_hci\_evt\_le\_cte\_req\_failed](structbt__hci__evt__le__cte__req__failed.md) {

2840 /\* According to BT 5.3 Core Spec the status field may have following

2841 \* values:

2842 \* - BT\_HCI\_CTE\_REQ\_STATUS\_RSP\_WITHOUT\_CTE when received LL\_CTE\_RSP\_PDU without CTE.

2843 \* - Other Controller error code for peer rejected request.

2844 \*/

[ 2845](structbt__hci__evt__le__cte__req__failed.md#a1433f25dee38014dbd2d061b6d75741a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__cte__req__failed.md#a1433f25dee38014dbd2d061b6d75741a);

[ 2846](structbt__hci__evt__le__cte__req__failed.md#aa903954fa411e4ae49a613b4e76219dc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__evt__le__cte__req__failed.md#aa903954fa411e4ae49a613b4e76219dc);

2847} \_\_packed;

2848

[ 2849](hci__types_8h.md#ad61867c0bef6797f7a3b5418c5a4ed5f)#define BT\_HCI\_EVT\_LE\_PAST\_RECEIVED 0x18

[ 2850](structbt__hci__evt__le__past__received.md)struct [bt\_hci\_evt\_le\_past\_received](structbt__hci__evt__le__past__received.md) {

[ 2851](structbt__hci__evt__le__past__received.md#a1b2c229c99d06f44057b88458f168e7c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__past__received.md#a1b2c229c99d06f44057b88458f168e7c);

[ 2852](structbt__hci__evt__le__past__received.md#a1bdbaddb4003cea40738ee540ecb8789) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__evt__le__past__received.md#a1bdbaddb4003cea40738ee540ecb8789);

[ 2853](structbt__hci__evt__le__past__received.md#adaa1e432db60a2529ad6266f16604e15) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [service\_data](structbt__hci__evt__le__past__received.md#adaa1e432db60a2529ad6266f16604e15);

[ 2854](structbt__hci__evt__le__past__received.md#a2cea2f3b9d51ace91ddf63639e821328) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sync\_handle](structbt__hci__evt__le__past__received.md#a2cea2f3b9d51ace91ddf63639e821328);

[ 2855](structbt__hci__evt__le__past__received.md#a110c7cdd2ff1178d1ca686abaae92b05) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_sid](structbt__hci__evt__le__past__received.md#a110c7cdd2ff1178d1ca686abaae92b05);

[ 2856](structbt__hci__evt__le__past__received.md#a3e368e95a6831f823d2efa0c0bc1ef51) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__hci__evt__le__past__received.md#a3e368e95a6831f823d2efa0c0bc1ef51);

[ 2857](structbt__hci__evt__le__past__received.md#aedb668e6f3232b1db9035ea89ccf1b71) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__evt__le__past__received.md#aedb668e6f3232b1db9035ea89ccf1b71);

[ 2858](structbt__hci__evt__le__past__received.md#a41ea6099d3cca1caf37ff518a4e95492) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__hci__evt__le__past__received.md#a41ea6099d3cca1caf37ff518a4e95492);

[ 2859](structbt__hci__evt__le__past__received.md#a00d570636a55c1d84723ad3bc5705d80) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [clock\_accuracy](structbt__hci__evt__le__past__received.md#a00d570636a55c1d84723ad3bc5705d80);

2860} \_\_packed;

2861

[ 2862](hci__types_8h.md#a263d26617702ab43fa8b6717007e1df8)#define BT\_HCI\_EVT\_LE\_CIS\_ESTABLISHED 0x19

[ 2863](structbt__hci__evt__le__cis__established.md)struct [bt\_hci\_evt\_le\_cis\_established](structbt__hci__evt__le__cis__established.md) {

[ 2864](structbt__hci__evt__le__cis__established.md#a4d90dbeda130a6142ff0b7f9e2ee7c16) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__cis__established.md#a4d90dbeda130a6142ff0b7f9e2ee7c16);

[ 2865](structbt__hci__evt__le__cis__established.md#a932e8df0222eb3bcf7bee753414d529e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__evt__le__cis__established.md#a932e8df0222eb3bcf7bee753414d529e);

[ 2866](structbt__hci__evt__le__cis__established.md#ac4e5a2535e3e8d3782adac63a4c5a8d9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cig\_sync\_delay](structbt__hci__evt__le__cis__established.md#ac4e5a2535e3e8d3782adac63a4c5a8d9)[3];

[ 2867](structbt__hci__evt__le__cis__established.md#ae71d6753849ae3c57327c8763cab1802) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cis\_sync\_delay](structbt__hci__evt__le__cis__established.md#ae71d6753849ae3c57327c8763cab1802)[3];

[ 2868](structbt__hci__evt__le__cis__established.md#a877913bb4b9016c64793458de94d84a0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_latency](structbt__hci__evt__le__cis__established.md#a877913bb4b9016c64793458de94d84a0)[3];

[ 2869](structbt__hci__evt__le__cis__established.md#aefb2d4e0458cbe990903a9f449189c30) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_latency](structbt__hci__evt__le__cis__established.md#aefb2d4e0458cbe990903a9f449189c30)[3];

[ 2870](structbt__hci__evt__le__cis__established.md#a53ea1da3f31313ab73b511c72912bd33) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_phy](structbt__hci__evt__le__cis__established.md#a53ea1da3f31313ab73b511c72912bd33);

[ 2871](structbt__hci__evt__le__cis__established.md#a25b84cf026775b582c7944e265ffb0b2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_phy](structbt__hci__evt__le__cis__established.md#a25b84cf026775b582c7944e265ffb0b2);

[ 2872](structbt__hci__evt__le__cis__established.md#a683856418764b1110d5c5fea0494fe1e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [nse](structbt__hci__evt__le__cis__established.md#a683856418764b1110d5c5fea0494fe1e);

[ 2873](structbt__hci__evt__le__cis__established.md#ab6b2d892e3c1e4f6aedee722049b75d3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_bn](structbt__hci__evt__le__cis__established.md#ab6b2d892e3c1e4f6aedee722049b75d3);

[ 2874](structbt__hci__evt__le__cis__established.md#ad0a79bfadd413bf572b697069695c0a5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_bn](structbt__hci__evt__le__cis__established.md#ad0a79bfadd413bf572b697069695c0a5);

[ 2875](structbt__hci__evt__le__cis__established.md#ad0f3bd5f81b660afbc4927a777c2c18e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_ft](structbt__hci__evt__le__cis__established.md#ad0f3bd5f81b660afbc4927a777c2c18e);

[ 2876](structbt__hci__evt__le__cis__established.md#a200afaff044b9eea653d8aee13297dc2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_ft](structbt__hci__evt__le__cis__established.md#a200afaff044b9eea653d8aee13297dc2);

[ 2877](structbt__hci__evt__le__cis__established.md#ae9fdecff4342f25de30165a4531ad703) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [c\_max\_pdu](structbt__hci__evt__le__cis__established.md#ae9fdecff4342f25de30165a4531ad703);

[ 2878](structbt__hci__evt__le__cis__established.md#ae8b195f433570e28e42a5f9d321964de) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [p\_max\_pdu](structbt__hci__evt__le__cis__established.md#ae8b195f433570e28e42a5f9d321964de);

[ 2879](structbt__hci__evt__le__cis__established.md#a0bcdc0d8b3b776660d2e51427f9634dd) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__hci__evt__le__cis__established.md#a0bcdc0d8b3b776660d2e51427f9634dd);

2880} \_\_packed;

2881

[ 2882](hci__types_8h.md#aaa4af1dcdb163a57b0473b43e8107fd7)#define BT\_HCI\_EVT\_LE\_CIS\_REQ 0x1a

[ 2883](structbt__hci__evt__le__cis__req.md)struct [bt\_hci\_evt\_le\_cis\_req](structbt__hci__evt__le__cis__req.md) {

[ 2884](structbt__hci__evt__le__cis__req.md#af8529013adb87340298a89d4727e6867) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [acl\_handle](structbt__hci__evt__le__cis__req.md#af8529013adb87340298a89d4727e6867);

[ 2885](structbt__hci__evt__le__cis__req.md#aeed6f4bf58cdb301d6b784a202722acc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cis\_handle](structbt__hci__evt__le__cis__req.md#aeed6f4bf58cdb301d6b784a202722acc);

[ 2886](structbt__hci__evt__le__cis__req.md#ae0ef0ac224bde55de13df4e5eeaf26be) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cig\_id](structbt__hci__evt__le__cis__req.md#ae0ef0ac224bde55de13df4e5eeaf26be);

[ 2887](structbt__hci__evt__le__cis__req.md#abdf99eeb7a30c8238bbabdcd60a4847a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cis\_id](structbt__hci__evt__le__cis__req.md#abdf99eeb7a30c8238bbabdcd60a4847a);

2888} \_\_packed;

2889

[ 2890](hci__types_8h.md#aade42399ac596746100849328c551259)#define BT\_HCI\_EVT\_LE\_BIG\_COMPLETE 0x1b

[ 2891](structbt__hci__evt__le__big__complete.md)struct [bt\_hci\_evt\_le\_big\_complete](structbt__hci__evt__le__big__complete.md) {

[ 2892](structbt__hci__evt__le__big__complete.md#ad6787806a3622b3bd3da4512bb8ddffe) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__big__complete.md#ad6787806a3622b3bd3da4512bb8ddffe);

[ 2893](structbt__hci__evt__le__big__complete.md#a14eaa705f1df38337722a41e8189f807) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [big\_handle](structbt__hci__evt__le__big__complete.md#a14eaa705f1df38337722a41e8189f807);

[ 2894](structbt__hci__evt__le__big__complete.md#a2847d5fc997f80a3e21b7e03d80c9574) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sync\_delay](structbt__hci__evt__le__big__complete.md#a2847d5fc997f80a3e21b7e03d80c9574)[3];

[ 2895](structbt__hci__evt__le__big__complete.md#a2727d329c37e3b3644cfad02d86abb55) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [latency](structbt__hci__evt__le__big__complete.md#a2727d329c37e3b3644cfad02d86abb55)[3];

[ 2896](structbt__hci__evt__le__big__complete.md#abfa6d6bc135350737451e053aa7d212c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__evt__le__big__complete.md#abfa6d6bc135350737451e053aa7d212c);

[ 2897](structbt__hci__evt__le__big__complete.md#ae77364aafe179588f7b8414292e35f5e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [nse](structbt__hci__evt__le__big__complete.md#ae77364aafe179588f7b8414292e35f5e);

[ 2898](structbt__hci__evt__le__big__complete.md#a2327e42013033767af233d1c2c3acc56) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bn](structbt__hci__evt__le__big__complete.md#a2327e42013033767af233d1c2c3acc56);

[ 2899](structbt__hci__evt__le__big__complete.md#a6c295870732d65002ec21b4b607e7c0b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pto](structbt__hci__evt__le__big__complete.md#a6c295870732d65002ec21b4b607e7c0b);

[ 2900](structbt__hci__evt__le__big__complete.md#a07163dee904412d6d8faca8563a944d9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [irc](structbt__hci__evt__le__big__complete.md#a07163dee904412d6d8faca8563a944d9);

[ 2901](structbt__hci__evt__le__big__complete.md#a8b433ac376e347bf391d4dd804c469f3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_pdu](structbt__hci__evt__le__big__complete.md#a8b433ac376e347bf391d4dd804c469f3);

[ 2902](structbt__hci__evt__le__big__complete.md#a0b0d19d442ed8f1025165c435786ba09) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [iso\_interval](structbt__hci__evt__le__big__complete.md#a0b0d19d442ed8f1025165c435786ba09);

[ 2903](structbt__hci__evt__le__big__complete.md#a995c8fe06ec087f16b771c38171745b1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_bis](structbt__hci__evt__le__big__complete.md#a995c8fe06ec087f16b771c38171745b1);

[ 2904](structbt__hci__evt__le__big__complete.md#af1c8bd66c3dba70df22f8655b4f27925) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__big__complete.md#af1c8bd66c3dba70df22f8655b4f27925)[0];

2905} \_\_packed;

2906

[ 2907](hci__types_8h.md#ac0a1310793a73afda4c2179749df9985)#define BT\_HCI\_EVT\_LE\_BIG\_TERMINATE 0x1c

[ 2908](structbt__hci__evt__le__big__terminate.md)struct [bt\_hci\_evt\_le\_big\_terminate](structbt__hci__evt__le__big__terminate.md) {

[ 2909](structbt__hci__evt__le__big__terminate.md#ad9c9e6d42661366d62d79163fa9ad1c7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [big\_handle](structbt__hci__evt__le__big__terminate.md#ad9c9e6d42661366d62d79163fa9ad1c7);

[ 2910](structbt__hci__evt__le__big__terminate.md#a0303ac64b825f93210dfc70a8a081ea6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reason](structbt__hci__evt__le__big__terminate.md#a0303ac64b825f93210dfc70a8a081ea6);

2911} \_\_packed;

2912

[ 2913](hci__types_8h.md#a8d021615f0b1b2077bbec1f1482b85ef)#define BT\_HCI\_EVT\_LE\_BIG\_SYNC\_ESTABLISHED 0x1d

[ 2914](structbt__hci__evt__le__big__sync__established.md)struct [bt\_hci\_evt\_le\_big\_sync\_established](structbt__hci__evt__le__big__sync__established.md) {

[ 2915](structbt__hci__evt__le__big__sync__established.md#a8feb21ef6eacf45dfc09b09e0bce04b1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__big__sync__established.md#a8feb21ef6eacf45dfc09b09e0bce04b1);

[ 2916](structbt__hci__evt__le__big__sync__established.md#a31a05f8afb69e5885700cc4ad3b161b2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [big\_handle](structbt__hci__evt__le__big__sync__established.md#a31a05f8afb69e5885700cc4ad3b161b2);

[ 2917](structbt__hci__evt__le__big__sync__established.md#aebb25f9a63fa013ec6ef891ca498dbb4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [latency](structbt__hci__evt__le__big__sync__established.md#aebb25f9a63fa013ec6ef891ca498dbb4)[3];

[ 2918](structbt__hci__evt__le__big__sync__established.md#a383dc92f6d16ec971455e20665cd7496) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [nse](structbt__hci__evt__le__big__sync__established.md#a383dc92f6d16ec971455e20665cd7496);

[ 2919](structbt__hci__evt__le__big__sync__established.md#a451466916fbe2f220c277b4b4e62241d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bn](structbt__hci__evt__le__big__sync__established.md#a451466916fbe2f220c277b4b4e62241d);

[ 2920](structbt__hci__evt__le__big__sync__established.md#a6b750de25b2a1afc38995030953364ce) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pto](structbt__hci__evt__le__big__sync__established.md#a6b750de25b2a1afc38995030953364ce);

[ 2921](structbt__hci__evt__le__big__sync__established.md#afd52315dafe02ee28bc26f058b12fe9e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [irc](structbt__hci__evt__le__big__sync__established.md#afd52315dafe02ee28bc26f058b12fe9e);

[ 2922](structbt__hci__evt__le__big__sync__established.md#a13db0d402636a71ed029575c1e5771c5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_pdu](structbt__hci__evt__le__big__sync__established.md#a13db0d402636a71ed029575c1e5771c5);

[ 2923](structbt__hci__evt__le__big__sync__established.md#a610313c11c65faf82e06a121affb8b2b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [iso\_interval](structbt__hci__evt__le__big__sync__established.md#a610313c11c65faf82e06a121affb8b2b);

[ 2924](structbt__hci__evt__le__big__sync__established.md#a2fa405310a8fed0341001b316ca7bd4f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_bis](structbt__hci__evt__le__big__sync__established.md#a2fa405310a8fed0341001b316ca7bd4f);

[ 2925](structbt__hci__evt__le__big__sync__established.md#a48766968cb677614f525ea36551ad6c8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__big__sync__established.md#a48766968cb677614f525ea36551ad6c8)[0];

2926} \_\_packed;

2927

[ 2928](hci__types_8h.md#a9c79430501848b9e75a21020920a8ca8)#define BT\_HCI\_EVT\_LE\_BIG\_SYNC\_LOST 0x1e

[ 2929](structbt__hci__evt__le__big__sync__lost.md)struct [bt\_hci\_evt\_le\_big\_sync\_lost](structbt__hci__evt__le__big__sync__lost.md) {

[ 2930](structbt__hci__evt__le__big__sync__lost.md#ae59a9c18363f7aee67563494d98aa971) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [big\_handle](structbt__hci__evt__le__big__sync__lost.md#ae59a9c18363f7aee67563494d98aa971);

[ 2931](structbt__hci__evt__le__big__sync__lost.md#a02b724a60e71805088aefca9989ad878) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reason](structbt__hci__evt__le__big__sync__lost.md#a02b724a60e71805088aefca9989ad878);

2932} \_\_packed;

2933

[ 2934](hci__types_8h.md#aeb33301a950a9520d7ff706dddb07951)#define BT\_HCI\_EVT\_LE\_REQ\_PEER\_SCA\_COMPLETE 0x1f

[ 2935](structbt__hci__evt__le__req__peer__sca__complete.md)struct [bt\_hci\_evt\_le\_req\_peer\_sca\_complete](structbt__hci__evt__le__req__peer__sca__complete.md) {

[ 2936](structbt__hci__evt__le__req__peer__sca__complete.md#a814d17b8aae9dd68f57402c857ca1810) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__req__peer__sca__complete.md#a814d17b8aae9dd68f57402c857ca1810);

[ 2937](structbt__hci__evt__le__req__peer__sca__complete.md#ab6b648e7f4bff9e84b274e9e22a26166) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__req__peer__sca__complete.md#ab6b648e7f4bff9e84b274e9e22a26166);

[ 2938](structbt__hci__evt__le__req__peer__sca__complete.md#a88f93ead6ec67e1612b1a0e8402a30e7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sca](structbt__hci__evt__le__req__peer__sca__complete.md#a88f93ead6ec67e1612b1a0e8402a30e7);

2939} \_\_packed;

2940

2943/\* Local Transmit power changed. \*/

[ 2944](hci__types_8h.md#a443a5a524ec41bf2ea86eab74dd022dc)#define BT\_HCI\_LE\_TX\_POWER\_REPORT\_REASON\_LOCAL\_CHANGED 0x00

2945/\* Remote Transmit power changed. \*/

[ 2946](hci__types_8h.md#a1fbc1b017b13987a017af7cd90bdf708)#define BT\_HCI\_LE\_TX\_POWER\_REPORT\_REASON\_REMOTE\_CHANGED 0x01

2947/\* HCI\_LE\_Read\_Remote\_Transmit\_Power\_Level command completed. \*/

[ 2948](hci__types_8h.md#a268761b9eae9c84f74394a6098f15ee8)#define BT\_HCI\_LE\_TX\_POWER\_REPORT\_REASON\_READ\_REMOTE\_COMPLETED 0x02

2949

[ 2950](hci__types_8h.md#a835280c0bf13ddebf451fef5f08c22d0)#define BT\_HCI\_EVT\_LE\_TRANSMIT\_POWER\_REPORT 0x21

[ 2951](structbt__hci__evt__le__transmit__power__report.md)struct [bt\_hci\_evt\_le\_transmit\_power\_report](structbt__hci__evt__le__transmit__power__report.md) {

[ 2952](structbt__hci__evt__le__transmit__power__report.md#af1629e59dd651e1616b89f4958f47c92) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__evt__le__transmit__power__report.md#af1629e59dd651e1616b89f4958f47c92);

[ 2953](structbt__hci__evt__le__transmit__power__report.md#a4feadb14800c1b51a9cc523c1d6a9063) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__evt__le__transmit__power__report.md#a4feadb14800c1b51a9cc523c1d6a9063);

[ 2954](structbt__hci__evt__le__transmit__power__report.md#a341cc0c5cc1ea969e2024b67056a5439) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reason](structbt__hci__evt__le__transmit__power__report.md#a341cc0c5cc1ea969e2024b67056a5439);

[ 2955](structbt__hci__evt__le__transmit__power__report.md#ad6130863713cf31a1cbe33de9fb5428f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__evt__le__transmit__power__report.md#ad6130863713cf31a1cbe33de9fb5428f);

[ 2956](structbt__hci__evt__le__transmit__power__report.md#aa0df9c50a555fa40ed25a14f7b6a5e77) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power\_level](structbt__hci__evt__le__transmit__power__report.md#aa0df9c50a555fa40ed25a14f7b6a5e77);

[ 2957](structbt__hci__evt__le__transmit__power__report.md#a2dc33da8f36cceda362d0c87098b02d6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_power\_level\_flag](structbt__hci__evt__le__transmit__power__report.md#a2dc33da8f36cceda362d0c87098b02d6);

[ 2958](structbt__hci__evt__le__transmit__power__report.md#ac42d60325235f517728ff44385361db2) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [delta](structbt__hci__evt__le__transmit__power__report.md#ac42d60325235f517728ff44385361db2);

2959} \_\_packed;

2960

[ 2961](hci__types_8h.md#a651e36b5529cb7f289721573434154cd)#define BT\_HCI\_EVT\_LE\_BIGINFO\_ADV\_REPORT 0x22

[ 2962](structbt__hci__evt__le__biginfo__adv__report.md)struct [bt\_hci\_evt\_le\_biginfo\_adv\_report](structbt__hci__evt__le__biginfo__adv__report.md) {

[ 2963](structbt__hci__evt__le__biginfo__adv__report.md#a8be20bfc607e6ce34ea75c53e285b0d5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sync\_handle](structbt__hci__evt__le__biginfo__adv__report.md#a8be20bfc607e6ce34ea75c53e285b0d5);

[ 2964](structbt__hci__evt__le__biginfo__adv__report.md#ae68f803bbc3f06e7190f62be98d2fe66) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_bis](structbt__hci__evt__le__biginfo__adv__report.md#ae68f803bbc3f06e7190f62be98d2fe66);

[ 2965](structbt__hci__evt__le__biginfo__adv__report.md#ae28d5378a7e2ef59fabb62a3a430ccc8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [nse](structbt__hci__evt__le__biginfo__adv__report.md#ae28d5378a7e2ef59fabb62a3a430ccc8);

[ 2966](structbt__hci__evt__le__biginfo__adv__report.md#ae92b69ab0bc257d4f50b98e071c6038b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [iso\_interval](structbt__hci__evt__le__biginfo__adv__report.md#ae92b69ab0bc257d4f50b98e071c6038b);

[ 2967](structbt__hci__evt__le__biginfo__adv__report.md#ada35f690706be1c6ee8f40787bbe53e5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bn](structbt__hci__evt__le__biginfo__adv__report.md#ada35f690706be1c6ee8f40787bbe53e5);

[ 2968](structbt__hci__evt__le__biginfo__adv__report.md#af3a871d3de34b90fc2b09b0725caf479) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pto](structbt__hci__evt__le__biginfo__adv__report.md#af3a871d3de34b90fc2b09b0725caf479);

[ 2969](structbt__hci__evt__le__biginfo__adv__report.md#a9c1235653245b517a105570c60ddfa09) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [irc](structbt__hci__evt__le__biginfo__adv__report.md#a9c1235653245b517a105570c60ddfa09);

[ 2970](structbt__hci__evt__le__biginfo__adv__report.md#a12a000c049e85d2b24720d1a362d28df) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_pdu](structbt__hci__evt__le__biginfo__adv__report.md#a12a000c049e85d2b24720d1a362d28df);

[ 2971](structbt__hci__evt__le__biginfo__adv__report.md#a81e236ceb24012bc267f656f20f1f8c4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sdu\_interval](structbt__hci__evt__le__biginfo__adv__report.md#a81e236ceb24012bc267f656f20f1f8c4)[3];

[ 2972](structbt__hci__evt__le__biginfo__adv__report.md#a084c13c4b0c9c8dca0653b56e53a0c74) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_sdu](structbt__hci__evt__le__biginfo__adv__report.md#a084c13c4b0c9c8dca0653b56e53a0c74);

[ 2973](structbt__hci__evt__le__biginfo__adv__report.md#a2301112acf22cf68d6495ff85f0f29bf) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__hci__evt__le__biginfo__adv__report.md#a2301112acf22cf68d6495ff85f0f29bf);

[ 2974](structbt__hci__evt__le__biginfo__adv__report.md#abe0636beae2f51004193ad5f7c9efeef) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [framing](structbt__hci__evt__le__biginfo__adv__report.md#abe0636beae2f51004193ad5f7c9efeef);

[ 2975](structbt__hci__evt__le__biginfo__adv__report.md#ae63eaf93f728109b5fb77ca3179ba99c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [encryption](structbt__hci__evt__le__biginfo__adv__report.md#ae63eaf93f728109b5fb77ca3179ba99c);

2976} \_\_packed;

2977

2978/\* Event mask bits \*/

2979

[ 2980](hci__types_8h.md#a25201544478590f6ee87a829410c612b)#define BT\_EVT\_BIT(n) (1ULL << (n))

2981

[ 2982](hci__types_8h.md#a79851cd962916f9be81e29ce9797e901)#define BT\_EVT\_MASK\_INQUIRY\_COMPLETE BT\_EVT\_BIT(0)

[ 2983](hci__types_8h.md#a5a13adda8bf4f015550a043667e0b67d)#define BT\_EVT\_MASK\_CONN\_COMPLETE BT\_EVT\_BIT(2)

[ 2984](hci__types_8h.md#ad77bbcd4fb8b0e37700492e8a3cccd38)#define BT\_EVT\_MASK\_CONN\_REQUEST BT\_EVT\_BIT(3)

[ 2985](hci__types_8h.md#a5ea9d4fb977c660bc33be93c73817705)#define BT\_EVT\_MASK\_DISCONN\_COMPLETE BT\_EVT\_BIT(4)

[ 2986](hci__types_8h.md#ad4f80dd3fdf22b23d47785a507aa5a85)#define BT\_EVT\_MASK\_AUTH\_COMPLETE BT\_EVT\_BIT(5)

[ 2987](hci__types_8h.md#a4433027483d6d63911b59c4fe605ba69)#define BT\_EVT\_MASK\_REMOTE\_NAME\_REQ\_COMPLETE BT\_EVT\_BIT(6)

[ 2988](hci__types_8h.md#a334c571248a1aad285bb11bc39d2ade8)#define BT\_EVT\_MASK\_ENCRYPT\_CHANGE BT\_EVT\_BIT(7)

[ 2989](hci__types_8h.md#a7ccade60a01e0f8a175b3b11b5e20f6d)#define BT\_EVT\_MASK\_REMOTE\_FEATURES BT\_EVT\_BIT(10)

[ 2990](hci__types_8h.md#a87331cabdea78ace1577cbf2fa7e3523)#define BT\_EVT\_MASK\_REMOTE\_VERSION\_INFO BT\_EVT\_BIT(11)

[ 2991](hci__types_8h.md#a079c00e59422034a9f977af7dd20234c)#define BT\_EVT\_MASK\_HARDWARE\_ERROR BT\_EVT\_BIT(15)

[ 2992](hci__types_8h.md#a4b4a80b51b2c20bf28fbfac57679a86e)#define BT\_EVT\_MASK\_ROLE\_CHANGE BT\_EVT\_BIT(17)

[ 2993](hci__types_8h.md#a9f5612d89848aafb6e9063a55e5cd6b4)#define BT\_EVT\_MASK\_PIN\_CODE\_REQ BT\_EVT\_BIT(21)

[ 2994](hci__types_8h.md#a1e16ab7caf239e804c0c2057e9b49e42)#define BT\_EVT\_MASK\_LINK\_KEY\_REQ BT\_EVT\_BIT(22)

[ 2995](hci__types_8h.md#aa20a3ce217a60070826d0b55ebd105be)#define BT\_EVT\_MASK\_LINK\_KEY\_NOTIFY BT\_EVT\_BIT(23)

[ 2996](hci__types_8h.md#a829ea33c603291d331faba58689b0198)#define BT\_EVT\_MASK\_DATA\_BUFFER\_OVERFLOW BT\_EVT\_BIT(25)

[ 2997](hci__types_8h.md#aeb5b4cbc01a8cebea5ce8e0090d37261)#define BT\_EVT\_MASK\_INQUIRY\_RESULT\_WITH\_RSSI BT\_EVT\_BIT(33)

[ 2998](hci__types_8h.md#a9d3bbaa1eb1dbe72714b922dcada3347)#define BT\_EVT\_MASK\_REMOTE\_EXT\_FEATURES BT\_EVT\_BIT(34)

[ 2999](hci__types_8h.md#a4f1a905136cb713c09fb5197dd099ce2)#define BT\_EVT\_MASK\_SYNC\_CONN\_COMPLETE BT\_EVT\_BIT(43)

[ 3000](hci__types_8h.md#a9b361fe6314f56fcb016bacb064af815)#define BT\_EVT\_MASK\_EXTENDED\_INQUIRY\_RESULT BT\_EVT\_BIT(46)

[ 3001](hci__types_8h.md#af8d96cc1cf99a7130d4c181450998cb7)#define BT\_EVT\_MASK\_ENCRYPT\_KEY\_REFRESH\_COMPLETE BT\_EVT\_BIT(47)

[ 3002](hci__types_8h.md#a845de3735dc3989d3a9d54cf5e55b408)#define BT\_EVT\_MASK\_IO\_CAPA\_REQ BT\_EVT\_BIT(48)

[ 3003](hci__types_8h.md#a409e33dbe4fdb1dc90050e0b4eab1f86)#define BT\_EVT\_MASK\_IO\_CAPA\_RESP BT\_EVT\_BIT(49)

[ 3004](hci__types_8h.md#a1c04cc7d04f056e5edfc4ddaa97c657f)#define BT\_EVT\_MASK\_USER\_CONFIRM\_REQ BT\_EVT\_BIT(50)

[ 3005](hci__types_8h.md#af56d87ffc24c2e4c08db68ab019fd58e)#define BT\_EVT\_MASK\_USER\_PASSKEY\_REQ BT\_EVT\_BIT(51)

[ 3006](hci__types_8h.md#a6a08ace148ea2728614a3bab02c21f65)#define BT\_EVT\_MASK\_SSP\_COMPLETE BT\_EVT\_BIT(53)

[ 3007](hci__types_8h.md#a2eb47347a5685a290087b236d696971e)#define BT\_EVT\_MASK\_USER\_PASSKEY\_NOTIFY BT\_EVT\_BIT(58)

[ 3008](hci__types_8h.md#a59f89d39350b396f8d0c986e2d477bba)#define BT\_EVT\_MASK\_LE\_META\_EVENT BT\_EVT\_BIT(61)

3009

3010/\* Page 2 \*/

[ 3011](hci__types_8h.md#abe39e63cbdee9bfeac36a1b6a4d40aba)#define BT\_EVT\_MASK\_NUM\_COMPLETE\_DATA\_BLOCKS BT\_EVT\_BIT(8)

[ 3012](hci__types_8h.md#aff43216feb0c29c6813d198473f34fdc)#define BT\_EVT\_MASK\_TRIGG\_CLOCK\_CAPTURE BT\_EVT\_BIT(14)

[ 3013](hci__types_8h.md#ac078d5b46d7e227726cb7456e2163d3f)#define BT\_EVT\_MASK\_SYNCH\_TRAIN\_COMPLETE BT\_EVT\_BIT(15)

[ 3014](hci__types_8h.md#a8901b477ec3584af207b3648b221bb92)#define BT\_EVT\_MASK\_SYNCH\_TRAIN\_RX BT\_EVT\_BIT(16)

[ 3015](hci__types_8h.md#aa8842138b1146d3581c39062d11a6305)#define BT\_EVT\_MASK\_CL\_PER\_BC\_RX BT\_EVT\_BIT(17)

[ 3016](hci__types_8h.md#af513eaa35861cfcfefba97e0263e3f5b)#define BT\_EVT\_MASK\_CL\_PER\_BC\_TIMEOUT BT\_EVT\_BIT(18)

[ 3017](hci__types_8h.md#a9b82f06f42651c32f4c0db9826002134)#define BT\_EVT\_MASK\_TRUNC\_PAGE\_COMPLETE BT\_EVT\_BIT(19)

[ 3018](hci__types_8h.md#ad078befa197baac20294dc0d46eff9dd)#define BT\_EVT\_MASK\_PER\_PAGE\_RSP\_TIMEOUT BT\_EVT\_BIT(20)

[ 3019](hci__types_8h.md#a35f42f297b980a050deceb71237883ba)#define BT\_EVT\_MASK\_CL\_PER\_BC\_CH\_MAP\_CHANGE BT\_EVT\_BIT(21)

[ 3020](hci__types_8h.md#ae8106016a80e123016c6d2fc406224d7)#define BT\_EVT\_MASK\_INQUIRY\_RSP\_NOT BT\_EVT\_BIT(22)

[ 3021](hci__types_8h.md#a33753df12afb5f7e19be01f9febc5d23)#define BT\_EVT\_MASK\_AUTH\_PAYLOAD\_TIMEOUT\_EXP BT\_EVT\_BIT(23)

[ 3022](hci__types_8h.md#a8bfac36e993c48d12bdeb7c130fdd6dc)#define BT\_EVT\_MASK\_SAM\_STATUS\_CHANGE BT\_EVT\_BIT(24)

3023

[ 3024](hci__types_8h.md#a59cd7a15e5b562adb6397509463e375c)#define BT\_EVT\_MASK\_LE\_CONN\_COMPLETE BT\_EVT\_BIT(0)

[ 3025](hci__types_8h.md#a39a55a4c3e71db708e39c8110a2349f7)#define BT\_EVT\_MASK\_LE\_ADVERTISING\_REPORT BT\_EVT\_BIT(1)

[ 3026](hci__types_8h.md#ab1988671f4017f6434dc0438b2e8b9f6)#define BT\_EVT\_MASK\_LE\_CONN\_UPDATE\_COMPLETE BT\_EVT\_BIT(2)

[ 3027](hci__types_8h.md#adba1a3a872ee26a41218c9104e9f957b)#define BT\_EVT\_MASK\_LE\_REMOTE\_FEAT\_COMPLETE BT\_EVT\_BIT(3)

[ 3028](hci__types_8h.md#ab495948af67d01208eff1adb9a33e489)#define BT\_EVT\_MASK\_LE\_LTK\_REQUEST BT\_EVT\_BIT(4)

[ 3029](hci__types_8h.md#ac3eeaa0610a6ac6d3b57880042071f2a)#define BT\_EVT\_MASK\_LE\_CONN\_PARAM\_REQ BT\_EVT\_BIT(5)

[ 3030](hci__types_8h.md#a73489ce7067d812e8443e242ee53a5e6)#define BT\_EVT\_MASK\_LE\_DATA\_LEN\_CHANGE BT\_EVT\_BIT(6)

[ 3031](hci__types_8h.md#a281d70b2b596b918972b59e684b6a476)#define BT\_EVT\_MASK\_LE\_P256\_PUBLIC\_KEY\_COMPLETE BT\_EVT\_BIT(7)

[ 3032](hci__types_8h.md#afbe64037a16680397614ba2db136b452)#define BT\_EVT\_MASK\_LE\_GENERATE\_DHKEY\_COMPLETE BT\_EVT\_BIT(8)

[ 3033](hci__types_8h.md#afb3b477cb835e60c3e77237451ebae5b)#define BT\_EVT\_MASK\_LE\_ENH\_CONN\_COMPLETE BT\_EVT\_BIT(9)

[ 3034](hci__types_8h.md#a3e84268b1e701ae37c77e95847490222)#define BT\_EVT\_MASK\_LE\_DIRECT\_ADV\_REPORT BT\_EVT\_BIT(10)

[ 3035](hci__types_8h.md#ab5f6014468b107486aba04ba698453ed)#define BT\_EVT\_MASK\_LE\_PHY\_UPDATE\_COMPLETE BT\_EVT\_BIT(11)

[ 3036](hci__types_8h.md#a1d7fc1a3ea229622560de8cf0bb63a81)#define BT\_EVT\_MASK\_LE\_EXT\_ADVERTISING\_REPORT BT\_EVT\_BIT(12)

[ 3037](hci__types_8h.md#a96142f5d79029a93a99152ade46fc005)#define BT\_EVT\_MASK\_LE\_PER\_ADV\_SYNC\_ESTABLISHED BT\_EVT\_BIT(13)

[ 3038](hci__types_8h.md#ad7fc62afd0e1e3dc040567d91320e18e)#define BT\_EVT\_MASK\_LE\_PER\_ADVERTISING\_REPORT BT\_EVT\_BIT(14)

[ 3039](hci__types_8h.md#ae78587797f24987f36c348fe790438b2)#define BT\_EVT\_MASK\_LE\_PER\_ADV\_SYNC\_LOST BT\_EVT\_BIT(15)

[ 3040](hci__types_8h.md#a372f6b8e355972d63e5f9ff45a486e9d)#define BT\_EVT\_MASK\_LE\_SCAN\_TIMEOUT BT\_EVT\_BIT(16)

[ 3041](hci__types_8h.md#a11330b1b6847d77d3ba88e1de0aaa36e)#define BT\_EVT\_MASK\_LE\_ADV\_SET\_TERMINATED BT\_EVT\_BIT(17)

[ 3042](hci__types_8h.md#a3f13865e913a1c6afb6d8d05a6d84608)#define BT\_EVT\_MASK\_LE\_SCAN\_REQ\_RECEIVED BT\_EVT\_BIT(18)

[ 3043](hci__types_8h.md#acee0428356c4853fe664709fc1675f02)#define BT\_EVT\_MASK\_LE\_CHAN\_SEL\_ALGO BT\_EVT\_BIT(19)

[ 3044](hci__types_8h.md#a6ef13decc171530c00f12b0226fa9ed1)#define BT\_EVT\_MASK\_LE\_CONNECTIONLESS\_IQ\_REPORT BT\_EVT\_BIT(20)

[ 3045](hci__types_8h.md#a3b2f133db5641414b95bfd953d715ff3)#define BT\_EVT\_MASK\_LE\_CONNECTION\_IQ\_REPORT BT\_EVT\_BIT(21)

[ 3046](hci__types_8h.md#afbd3991be814ec6462d62fbc4c898ac0)#define BT\_EVT\_MASK\_LE\_CTE\_REQUEST\_FAILED BT\_EVT\_BIT(22)

[ 3047](hci__types_8h.md#a5b2139ce8847bfcdbcd99c3241fb5ea2)#define BT\_EVT\_MASK\_LE\_PAST\_RECEIVED BT\_EVT\_BIT(23)

[ 3048](hci__types_8h.md#a9e41b4cb965576490fb39f7dc396722f)#define BT\_EVT\_MASK\_LE\_CIS\_ESTABLISHED BT\_EVT\_BIT(24)

[ 3049](hci__types_8h.md#aa24e9569ace049098a6d822ad7433e26)#define BT\_EVT\_MASK\_LE\_CIS\_REQ BT\_EVT\_BIT(25)

[ 3050](hci__types_8h.md#a447ff4a3e4dfba390ce9729e45abb410)#define BT\_EVT\_MASK\_LE\_BIG\_COMPLETE BT\_EVT\_BIT(26)

[ 3051](hci__types_8h.md#ad4b775d48bfa14c00c78ac1fbb8f2a2a)#define BT\_EVT\_MASK\_LE\_BIG\_TERMINATED BT\_EVT\_BIT(27)

[ 3052](hci__types_8h.md#ab88b8bcde1d07b5f16c55c4cbf4fd20d)#define BT\_EVT\_MASK\_LE\_BIG\_SYNC\_ESTABLISHED BT\_EVT\_BIT(28)

[ 3053](hci__types_8h.md#a87abdedde8bd43f845fe604c80612ca0)#define BT\_EVT\_MASK\_LE\_BIG\_SYNC\_LOST BT\_EVT\_BIT(29)

[ 3054](hci__types_8h.md#a01e518d3bb3d4f99c335743362a84080)#define BT\_EVT\_MASK\_LE\_REQ\_PEER\_SCA\_COMPLETE BT\_EVT\_BIT(30)

[ 3055](hci__types_8h.md#a6aad398435aa48ba67f6917bca2a690e)#define BT\_EVT\_MASK\_LE\_PATH\_LOSS\_THRESHOLD BT\_EVT\_BIT(31)

[ 3056](hci__types_8h.md#a7f9d3cdf0de067ad408bec600b9a691f)#define BT\_EVT\_MASK\_LE\_TRANSMIT\_POWER\_REPORTING BT\_EVT\_BIT(32)

[ 3057](hci__types_8h.md#aff9c37de1e55e6a7085b3a521f34d3e0)#define BT\_EVT\_MASK\_LE\_BIGINFO\_ADV\_REPORT BT\_EVT\_BIT(33)

3058

[ 3059](hci__types_8h.md#a92a360ad268c29e1616de1e16748eb44)#define BT\_EVT\_MASK\_LE\_PER\_ADV\_SYNC\_ESTABLISHED\_V2 BT\_EVT\_BIT(35)

[ 3060](hci__types_8h.md#ad78d5a027581dee52c54bb3f5a19b68d)#define BT\_EVT\_MASK\_LE\_PER\_ADVERTISING\_REPORT\_V2 BT\_EVT\_BIT(36)

[ 3061](hci__types_8h.md#a93aec31c1636fec90b609981736eb2de)#define BT\_EVT\_MASK\_LE\_PAST\_RECEIVED\_V2 BT\_EVT\_BIT(37)

[ 3062](hci__types_8h.md#af0e2c2e66bdac52fbe5e9c91ca26fe49)#define BT\_EVT\_MASK\_LE\_PER\_ADV\_SUBEVENT\_DATA\_REQ BT\_EVT\_BIT(38)

[ 3063](hci__types_8h.md#ab8a9486fedec169e4d44b249f2445acf)#define BT\_EVT\_MASK\_LE\_PER\_ADV\_RESPONSE\_REPORT BT\_EVT\_BIT(39)

[ 3064](hci__types_8h.md#a8b40a701334d25741a6e17ffd86576ad)#define BT\_EVT\_MASK\_LE\_ENH\_CONN\_COMPLETE\_V2 BT\_EVT\_BIT(40)

3065

[ 3067](hci__types_8h.md#a27c890210eded48f159073cccef8582a)#define BT\_HCI\_ERR\_SUCCESS 0x00

[ 3068](hci__types_8h.md#a376012d3b8f7814870e3f03f6cbabb89)#define BT\_HCI\_ERR\_UNKNOWN\_CMD 0x01

[ 3069](hci__types_8h.md#afd68afeb0296e3af363d7d60eaf4e9a1)#define BT\_HCI\_ERR\_UNKNOWN\_CONN\_ID 0x02

[ 3070](hci__types_8h.md#a5dfcb0d206b98be7eacdc67547bb8a2c)#define BT\_HCI\_ERR\_HW\_FAILURE 0x03

[ 3071](hci__types_8h.md#a1e89c8eb63dee6bd720ef9354c867519)#define BT\_HCI\_ERR\_PAGE\_TIMEOUT 0x04

[ 3072](hci__types_8h.md#a070d51dd0de3288f9811f90a558c889b)#define BT\_HCI\_ERR\_AUTH\_FAIL 0x05

[ 3073](hci__types_8h.md#a39f129aefe81c2d06f70552ace008a15)#define BT\_HCI\_ERR\_PIN\_OR\_KEY\_MISSING 0x06

[ 3074](hci__types_8h.md#ac54f84b29901185822f6bad2edf86b61)#define BT\_HCI\_ERR\_MEM\_CAPACITY\_EXCEEDED 0x07

[ 3075](hci__types_8h.md#ab702caf5cd73431cc9aede8891f74610)#define BT\_HCI\_ERR\_CONN\_TIMEOUT 0x08

[ 3076](hci__types_8h.md#a490798f4f1e226e66475f0fb84cfbcd5)#define BT\_HCI\_ERR\_CONN\_LIMIT\_EXCEEDED 0x09

[ 3077](hci__types_8h.md#a56a3d3d9d7798334b29c02214a2e73bf)#define BT\_HCI\_ERR\_SYNC\_CONN\_LIMIT\_EXCEEDED 0x0a

[ 3078](hci__types_8h.md#abcf4cd921e304758cc969a83445d70ec)#define BT\_HCI\_ERR\_CONN\_ALREADY\_EXISTS 0x0b

[ 3079](hci__types_8h.md#a5ee9f2e9625d732e84e5ef593bb2a3f9)#define BT\_HCI\_ERR\_CMD\_DISALLOWED 0x0c

[ 3080](hci__types_8h.md#a0efddbffb31b93158b10a3f678f94f4e)#define BT\_HCI\_ERR\_INSUFFICIENT\_RESOURCES 0x0d

[ 3081](hci__types_8h.md#a08d4bdfc189bccbdb97a51b0089e77a0)#define BT\_HCI\_ERR\_INSUFFICIENT\_SECURITY 0x0e

[ 3082](hci__types_8h.md#a366f85b3bcb3f578b2572149c69b7fc0)#define BT\_HCI\_ERR\_BD\_ADDR\_UNACCEPTABLE 0x0f

[ 3083](hci__types_8h.md#ae4682cbd7a9b9dedd25926efe029c0d7)#define BT\_HCI\_ERR\_CONN\_ACCEPT\_TIMEOUT 0x10

[ 3084](hci__types_8h.md#af73db17855859676827bad84e2ccbabe)#define BT\_HCI\_ERR\_UNSUPP\_FEATURE\_PARAM\_VAL 0x11

[ 3085](hci__types_8h.md#afc76c774f5e71423eb9fea910d1860e9)#define BT\_HCI\_ERR\_INVALID\_PARAM 0x12

[ 3086](hci__types_8h.md#ac0e3b44027180d7a2dedb59395c4b111)#define BT\_HCI\_ERR\_REMOTE\_USER\_TERM\_CONN 0x13

[ 3087](hci__types_8h.md#a5eeadfb220c24b2e7f5ce3fd21e5d46a)#define BT\_HCI\_ERR\_REMOTE\_LOW\_RESOURCES 0x14

[ 3088](hci__types_8h.md#a083f1fc52300f7e47c2f8d4e50551851)#define BT\_HCI\_ERR\_REMOTE\_POWER\_OFF 0x15

[ 3089](hci__types_8h.md#a0f07b75be216456e9370485dca0da992)#define BT\_HCI\_ERR\_LOCALHOST\_TERM\_CONN 0x16

[ 3090](hci__types_8h.md#a11d42e0347cc9d1d50ccd45c2e9a39f6)#define BT\_HCI\_ERR\_REPEATED\_ATTEMPTS 0x17

[ 3091](hci__types_8h.md#a60823c337c91aa95348dcae250a83977)#define BT\_HCI\_ERR\_PAIRING\_NOT\_ALLOWED 0x18

[ 3092](hci__types_8h.md#a0f81b5c19358982bd33c527239200b08)#define BT\_HCI\_ERR\_UNKNOWN\_LMP\_PDU 0x19

[ 3093](hci__types_8h.md#a516751f02bd497a020783f69bcf71453)#define BT\_HCI\_ERR\_UNSUPP\_REMOTE\_FEATURE 0x1a

[ 3094](hci__types_8h.md#a5e28f04c454361508bc791c6ce292bc2)#define BT\_HCI\_ERR\_SCO\_OFFSET\_REJECTED 0x1b

[ 3095](hci__types_8h.md#a5093c6357fcefd1ccdcbdf9a99f18e7c)#define BT\_HCI\_ERR\_SCO\_INTERVAL\_REJECTED 0x1c

[ 3096](hci__types_8h.md#ad8f77a43360e8ab2e6c71a103e14c951)#define BT\_HCI\_ERR\_SCO\_AIR\_MODE\_REJECTED 0x1d

[ 3097](hci__types_8h.md#a943fe81109d82983018b558b9274f9a3)#define BT\_HCI\_ERR\_INVALID\_LL\_PARAM 0x1e

[ 3098](hci__types_8h.md#ab3833bbb70b6a2e57870d8243f528b90)#define BT\_HCI\_ERR\_UNSPECIFIED 0x1f

[ 3099](hci__types_8h.md#af1fa61561b6a91d08f81e9c19cbe89f7)#define BT\_HCI\_ERR\_UNSUPP\_LL\_PARAM\_VAL 0x20

[ 3100](hci__types_8h.md#a070d016f54e7f5f0a7ca6d8c8218505f)#define BT\_HCI\_ERR\_ROLE\_CHANGE\_NOT\_ALLOWED 0x21

[ 3101](hci__types_8h.md#a6317763780d9c81e6752d5a2c8ce3172)#define BT\_HCI\_ERR\_LL\_RESP\_TIMEOUT 0x22

[ 3102](hci__types_8h.md#a0e280074290680d62ad4721384bb603e)#define BT\_HCI\_ERR\_LL\_PROC\_COLLISION 0x23

[ 3103](hci__types_8h.md#a47c02d44d40d785db6fee28c88d3c5b4)#define BT\_HCI\_ERR\_LMP\_PDU\_NOT\_ALLOWED 0x24

[ 3104](hci__types_8h.md#aeb5499a707e1c41cbd9db882cfdf0677)#define BT\_HCI\_ERR\_ENC\_MODE\_NOT\_ACCEPTABLE 0x25

[ 3105](hci__types_8h.md#aee97132db4398e2db0a6e115ca20b9b4)#define BT\_HCI\_ERR\_LINK\_KEY\_CANNOT\_BE\_CHANGED 0x26

[ 3106](hci__types_8h.md#a0e02fd84d7a355f42fe006c756936d78)#define BT\_HCI\_ERR\_REQUESTED\_QOS\_NOT\_SUPPORTED 0x27

[ 3107](hci__types_8h.md#a2d336db995ab250f94de66da952c642c)#define BT\_HCI\_ERR\_INSTANT\_PASSED 0x28

[ 3108](hci__types_8h.md#a059c7d5619823eddf2c541b40a6464cb)#define BT\_HCI\_ERR\_PAIRING\_NOT\_SUPPORTED 0x29

[ 3109](hci__types_8h.md#a3b461d65baa95f8f984b212264dc5072)#define BT\_HCI\_ERR\_DIFF\_TRANS\_COLLISION 0x2a

[ 3110](hci__types_8h.md#a37c2fdc6b32b4a2cb70d5c17dfbe262b)#define BT\_HCI\_ERR\_QOS\_UNACCEPTABLE\_PARAM 0x2c

[ 3111](hci__types_8h.md#a88363d1eb1c0d13dc8138af8edc76abc)#define BT\_HCI\_ERR\_QOS\_REJECTED 0x2d

[ 3112](hci__types_8h.md#a3b9fc13a3e3ecc9f0f4431487c0301b5)#define BT\_HCI\_ERR\_CHAN\_ASSESS\_NOT\_SUPPORTED 0x2e

[ 3113](hci__types_8h.md#a334efee11bd7086e0611c8f628d65abb)#define BT\_HCI\_ERR\_INSUFF\_SECURITY 0x2f

[ 3114](hci__types_8h.md#a29c763a2e70820fae7e2e825d22f4991)#define BT\_HCI\_ERR\_PARAM\_OUT\_OF\_MANDATORY\_RANGE 0x30

[ 3115](hci__types_8h.md#ac9c9a68e696e038d7b05af89e3a0c7b6)#define BT\_HCI\_ERR\_ROLE\_SWITCH\_PENDING 0x32

[ 3116](hci__types_8h.md#ac6244ca7123879ef039c2c5486d50d41)#define BT\_HCI\_ERR\_RESERVED\_SLOT\_VIOLATION 0x34

[ 3117](hci__types_8h.md#ab40a919a2d87376f2aca6d2ea3f55758)#define BT\_HCI\_ERR\_ROLE\_SWITCH\_FAILED 0x35

[ 3118](hci__types_8h.md#a1b7094ad185ed22542f370ab1101c1ae)#define BT\_HCI\_ERR\_EXT\_INQ\_RESP\_TOO\_LARGE 0x36

[ 3119](hci__types_8h.md#afd8840ad198dfdb666bf24851a478c70)#define BT\_HCI\_ERR\_SIMPLE\_PAIR\_NOT\_SUPP\_BY\_HOST 0x37

[ 3120](hci__types_8h.md#a107d85e39fec3146d6b017deb047571b)#define BT\_HCI\_ERR\_HOST\_BUSY\_PAIRING 0x38

[ 3121](hci__types_8h.md#a1adf558f8f606612ca96bdbbb55e0e78)#define BT\_HCI\_ERR\_CONN\_REJECTED\_DUE\_TO\_NO\_CHAN 0x39

[ 3122](hci__types_8h.md#a33167856fe838b833fe42d92c3eac4eb)#define BT\_HCI\_ERR\_CONTROLLER\_BUSY 0x3a

[ 3123](hci__types_8h.md#a712e214942c0d151597ce04e9d0df453)#define BT\_HCI\_ERR\_UNACCEPT\_CONN\_PARAM 0x3b

[ 3124](hci__types_8h.md#abfa408d8366ff3cae1cd35fffcda30c0)#define BT\_HCI\_ERR\_ADV\_TIMEOUT 0x3c

[ 3125](hci__types_8h.md#a71dd49b1b5dc51ad7db8da9aecf9ff06)#define BT\_HCI\_ERR\_TERM\_DUE\_TO\_MIC\_FAIL 0x3d

[ 3126](hci__types_8h.md#ac6c44be2e737d7a10b5c886c69d6b1a5)#define BT\_HCI\_ERR\_CONN\_FAIL\_TO\_ESTAB 0x3e

[ 3127](hci__types_8h.md#af0b9f71a874ca2c3587256c7f665e9fa)#define BT\_HCI\_ERR\_MAC\_CONN\_FAILED 0x3f

[ 3128](hci__types_8h.md#a6e9a4db5962d79b5a7f43a4c2919c9e9)#define BT\_HCI\_ERR\_CLOCK\_ADJUST\_REJECTED 0x40

[ 3129](hci__types_8h.md#a9e7483e2d7f46981e9d1fcdbb8a7515c)#define BT\_HCI\_ERR\_SUBMAP\_NOT\_DEFINED 0x41

[ 3130](hci__types_8h.md#a7646bc91f5dbb28c5eeda7e1828f2e30)#define BT\_HCI\_ERR\_UNKNOWN\_ADV\_IDENTIFIER 0x42

[ 3131](hci__types_8h.md#a86b092455cfd220d48af2bea04900b5b)#define BT\_HCI\_ERR\_LIMIT\_REACHED 0x43

[ 3132](hci__types_8h.md#a85433a7b3bcac0a507d7f6376a084142)#define BT\_HCI\_ERR\_OP\_CANCELLED\_BY\_HOST 0x44

[ 3133](hci__types_8h.md#ab63f7d0c79aaa57abf59aa18e112345f)#define BT\_HCI\_ERR\_PACKET\_TOO\_LONG 0x45

[ 3134](hci__types_8h.md#a9c62f8f73470a3157a60f8d6d56b22a4)#define BT\_HCI\_ERR\_TOO\_LATE 0x46

[ 3135](hci__types_8h.md#a8dcf345b1fea1364f490f40963992cd6)#define BT\_HCI\_ERR\_TOO\_EARLY 0x47

3136

3137#ifdef \_\_cplusplus

3138}

3139#endif

3140

3141#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_HCI\_TYPES\_H\_ \*/

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

**Definition** hci\_types.h:71

[bt\_hci\_acl\_hdr::handle](structbt__hci__acl__hdr.md#a8c88ef62a848699e06c49f97e1169363)

uint16\_t handle

**Definition** hci\_types.h:72

[bt\_hci\_acl\_hdr::len](structbt__hci__acl__hdr.md#af55b9c9256f35ada5786e9e5dd1d01bf)

uint16\_t len

**Definition** hci\_types.h:73

[bt\_hci\_cis\_params\_test](structbt__hci__cis__params__test.md)

**Definition** hci\_types.h:1993

[bt\_hci\_cis\_params\_test::cis\_id](structbt__hci__cis__params__test.md#a0a215b4dffac2aae4ae4310c54de073e)

uint8\_t cis\_id

**Definition** hci\_types.h:1994

[bt\_hci\_cis\_params\_test::c\_sdu](structbt__hci__cis__params__test.md#a98a120efb1495dd90858bef45eb95891)

uint16\_t c\_sdu

**Definition** hci\_types.h:1996

[bt\_hci\_cis\_params\_test::c\_phy](structbt__hci__cis__params__test.md#aa7ba56fb91718d43ca30ff643757e08e)

uint8\_t c\_phy

**Definition** hci\_types.h:2000

[bt\_hci\_cis\_params\_test::p\_phy](structbt__hci__cis__params__test.md#ab636126046023a329451673c57b4ce96)

uint8\_t p\_phy

**Definition** hci\_types.h:2001

[bt\_hci\_cis\_params\_test::p\_pdu](structbt__hci__cis__params__test.md#abce4bd6045642b4d29668865655f1548)

uint16\_t p\_pdu

**Definition** hci\_types.h:1999

[bt\_hci\_cis\_params\_test::p\_bn](structbt__hci__cis__params__test.md#ac66b7183d8148250246f17a157dc3d29)

uint8\_t p\_bn

**Definition** hci\_types.h:2003

[bt\_hci\_cis\_params\_test::nse](structbt__hci__cis__params__test.md#ad0cc6d393a536cb3cd83d456b950fc52)

uint8\_t nse

**Definition** hci\_types.h:1995

[bt\_hci\_cis\_params\_test::c\_pdu](structbt__hci__cis__params__test.md#adc092a44b58bcc78f3dfe88528ca724c)

uint16\_t c\_pdu

**Definition** hci\_types.h:1998

[bt\_hci\_cis\_params\_test::c\_bn](structbt__hci__cis__params__test.md#adf5dda2be46f3c2c1a1fe398672416ff)

uint8\_t c\_bn

**Definition** hci\_types.h:2002

[bt\_hci\_cis\_params\_test::p\_sdu](structbt__hci__cis__params__test.md#aefeca493efe0141590570e8a44bb8f8d)

uint16\_t p\_sdu

**Definition** hci\_types.h:1997

[bt\_hci\_cis\_params](structbt__hci__cis__params.md)

**Definition** hci\_types.h:1962

[bt\_hci\_cis\_params::p\_phy](structbt__hci__cis__params.md#a18bc8e4b531d9fd16f18e10a0d931f6c)

uint8\_t p\_phy

**Definition** hci\_types.h:1967

[bt\_hci\_cis\_params::c\_phy](structbt__hci__cis__params.md#a5a5fcd9276d912446fe84d875ae74c2f)

uint8\_t c\_phy

**Definition** hci\_types.h:1966

[bt\_hci\_cis\_params::cis\_id](structbt__hci__cis__params.md#a6dcfca11d7f827b1b7a62b507620d4de)

uint8\_t cis\_id

**Definition** hci\_types.h:1963

[bt\_hci\_cis\_params::c\_sdu](structbt__hci__cis__params.md#a8a85b914ba5585c6b362da3deb8d42d9)

uint16\_t c\_sdu

**Definition** hci\_types.h:1964

[bt\_hci\_cis\_params::c\_rtn](structbt__hci__cis__params.md#aa7fa628692f959db63788c6580cc5c66)

uint8\_t c\_rtn

**Definition** hci\_types.h:1968

[bt\_hci\_cis\_params::p\_rtn](structbt__hci__cis__params.md#ad55e197ccb70c83fcd4c1c6ba485f468)

uint8\_t p\_rtn

**Definition** hci\_types.h:1969

[bt\_hci\_cis\_params::p\_sdu](structbt__hci__cis__params.md#ae2bffbaf0c4dde9144a7887177b3ffdb)

uint16\_t p\_sdu

**Definition** hci\_types.h:1965

[bt\_hci\_cis](structbt__hci__cis.md)

**Definition** hci\_types.h:2028

[bt\_hci\_cis::acl\_handle](structbt__hci__cis.md#a754c3c75c0ad13a11d89fa3347112e2c)

uint16\_t acl\_handle

**Definition** hci\_types.h:2030

[bt\_hci\_cis::cis\_handle](structbt__hci__cis.md#a84165d526c10a91fa42d306276d97c74)

uint16\_t cis\_handle

**Definition** hci\_types.h:2029

[bt\_hci\_cmd\_hdr](structbt__hci__cmd__hdr.md)

**Definition** hci\_types.h:120

[bt\_hci\_cmd\_hdr::opcode](structbt__hci__cmd__hdr.md#a09c63aab094ca0f39bab44708fdb83e4)

uint16\_t opcode

**Definition** hci\_types.h:121

[bt\_hci\_cmd\_hdr::param\_len](structbt__hci__cmd__hdr.md#afe2a97da8b473cafd3cc4e5e52dadf93)

uint8\_t param\_len

**Definition** hci\_types.h:122

[bt\_hci\_codec\_capability\_info](structbt__hci__codec__capability__info.md)

**Definition** hci\_types.h:848

[bt\_hci\_codec\_capability\_info::length](structbt__hci__codec__capability__info.md#a24516347742a8fd9f3386d78b66a4e81)

uint8\_t length

**Definition** hci\_types.h:849

[bt\_hci\_codec\_capability\_info::data](structbt__hci__codec__capability__info.md#ac53f02f2abdb832ed82da35a36abc323)

uint8\_t data[0]

**Definition** hci\_types.h:850

[bt\_hci\_cp\_accept\_conn\_req](structbt__hci__cp__accept__conn__req.md)

**Definition** hci\_types.h:382

[bt\_hci\_cp\_accept\_conn\_req::role](structbt__hci__cp__accept__conn__req.md#a95e445018d1b9da5a914f0845bb9dbad)

uint8\_t role

**Definition** hci\_types.h:384

[bt\_hci\_cp\_accept\_conn\_req::bdaddr](structbt__hci__cp__accept__conn__req.md#aa2954d98fdd42882cf7095e4ce7a3dc5)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:383

[bt\_hci\_cp\_accept\_sync\_conn\_req](structbt__hci__cp__accept__sync__conn__req.md)

**Definition** hci\_types.h:399

[bt\_hci\_cp\_accept\_sync\_conn\_req::max\_latency](structbt__hci__cp__accept__sync__conn__req.md#a4ba6dffd840ef868524b490d227fd085)

uint16\_t max\_latency

**Definition** hci\_types.h:403

[bt\_hci\_cp\_accept\_sync\_conn\_req::tx\_bandwidth](structbt__hci__cp__accept__sync__conn__req.md#a53fe4c6d61dbb99f99aa445b2c47a8ef)

uint32\_t tx\_bandwidth

**Definition** hci\_types.h:401

[bt\_hci\_cp\_accept\_sync\_conn\_req::bdaddr](structbt__hci__cp__accept__sync__conn__req.md#a6a5a56d3a9d1a6d1064e7bd4c9fd333e)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:400

[bt\_hci\_cp\_accept\_sync\_conn\_req::pkt\_type](structbt__hci__cp__accept__sync__conn__req.md#ab5d9c27ebdf45fb54b0c6330b5b095be)

uint16\_t pkt\_type

**Definition** hci\_types.h:406

[bt\_hci\_cp\_accept\_sync\_conn\_req::retrans\_effort](structbt__hci__cp__accept__sync__conn__req.md#ab5ece67c5a1e62fc4124556eef743c26)

uint8\_t retrans\_effort

**Definition** hci\_types.h:405

[bt\_hci\_cp\_accept\_sync\_conn\_req::rx\_bandwidth](structbt__hci__cp__accept__sync__conn__req.md#aceda6dbd3e221ad080850e9635886a86)

uint32\_t rx\_bandwidth

**Definition** hci\_types.h:402

[bt\_hci\_cp\_accept\_sync\_conn\_req::content\_format](structbt__hci__cp__accept__sync__conn__req.md#adba31b588bf12e852cc43b85c006aaa3)

uint16\_t content\_format

**Definition** hci\_types.h:404

[bt\_hci\_cp\_auth\_requested](structbt__hci__cp__auth__requested.md)

**Definition** hci\_types.h:447

[bt\_hci\_cp\_auth\_requested::handle](structbt__hci__cp__auth__requested.md#a079490f8f8569e281ce16f13847cbf33)

uint16\_t handle

**Definition** hci\_types.h:448

[bt\_hci\_cp\_codec\_id](structbt__hci__cp__codec__id.md)

**Definition** hci\_types.h:836

[bt\_hci\_cp\_codec\_id::vs\_codec\_id](structbt__hci__cp__codec__id.md#a70296440c202544af11db2dc8e80fc5b)

uint16\_t vs\_codec\_id

**Definition** hci\_types.h:839

[bt\_hci\_cp\_codec\_id::company\_id](structbt__hci__cp__codec__id.md#a98fd438270a64d843fa27c7c196645df)

uint16\_t company\_id

**Definition** hci\_types.h:838

[bt\_hci\_cp\_codec\_id::coding\_format](structbt__hci__cp__codec__id.md#aec80c74b12edb9c63330cc5a404eed5d)

uint8\_t coding\_format

**Definition** hci\_types.h:837

[bt\_hci\_cp\_configure\_data\_path](structbt__hci__cp__configure__data__path.md)

**Definition** hci\_types.h:682

[bt\_hci\_cp\_configure\_data\_path::vs\_config\_len](structbt__hci__cp__configure__data__path.md#a2573fe029e1774bf5fa7e8cffff08cec)

uint8\_t vs\_config\_len

**Definition** hci\_types.h:685

[bt\_hci\_cp\_configure\_data\_path::data\_path\_dir](structbt__hci__cp__configure__data__path.md#a528ba2bd5a220d1b7db064f8b51a8718)

uint8\_t data\_path\_dir

**Definition** hci\_types.h:683

[bt\_hci\_cp\_configure\_data\_path::data\_path\_id](structbt__hci__cp__configure__data__path.md#a92967e6b5258b2acd6d82bfbfb8b7940)

uint8\_t data\_path\_id

**Definition** hci\_types.h:684

[bt\_hci\_cp\_configure\_data\_path::vs\_config](structbt__hci__cp__configure__data__path.md#aa79c4aa6603b09f49a8c7f216f135e6e)

uint8\_t vs\_config[0]

**Definition** hci\_types.h:686

[bt\_hci\_cp\_connect\_cancel](structbt__hci__cp__connect__cancel.md)

**Definition** hci\_types.h:373

[bt\_hci\_cp\_connect\_cancel::bdaddr](structbt__hci__cp__connect__cancel.md#a2adaf1b708689525e44e9a9572f5f357)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:374

[bt\_hci\_cp\_connect](structbt__hci__cp__connect.md)

**Definition** hci\_types.h:357

[bt\_hci\_cp\_connect::pscan\_rep\_mode](structbt__hci__cp__connect.md#a35b0e1f73f696aae2ca519e16d7bb668)

uint8\_t pscan\_rep\_mode

**Definition** hci\_types.h:360

[bt\_hci\_cp\_connect::packet\_type](structbt__hci__cp__connect.md#a652a4e01641893a8588110dc505ceea0)

uint16\_t packet\_type

**Definition** hci\_types.h:359

[bt\_hci\_cp\_connect::bdaddr](structbt__hci__cp__connect.md#a6f0753aad19d4c9591fa74152d151aa9)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:358

[bt\_hci\_cp\_connect::allow\_role\_switch](structbt__hci__cp__connect.md#a7a3d772bfd4c83236f9f1ad657e33f17)

uint8\_t allow\_role\_switch

**Definition** hci\_types.h:363

[bt\_hci\_cp\_connect::clock\_offset](structbt__hci__cp__connect.md#ac379ec381ad4cf6760750203924e5dda)

uint16\_t clock\_offset

**Definition** hci\_types.h:362

[bt\_hci\_cp\_connect::reserved](structbt__hci__cp__connect.md#aef01fcac1b9792353bd8095e6911d6c3)

uint8\_t reserved

**Definition** hci\_types.h:361

[bt\_hci\_cp\_disconnect](structbt__hci__cp__disconnect.md)

**Definition** hci\_types.h:367

[bt\_hci\_cp\_disconnect::reason](structbt__hci__cp__disconnect.md#a8e10edb1e700c1ef38f39bf20b9b374f)

uint8\_t reason

**Definition** hci\_types.h:369

[bt\_hci\_cp\_disconnect::handle](structbt__hci__cp__disconnect.md#a9cb5bcd135082c37a19cce57ffa123ff)

uint16\_t handle

**Definition** hci\_types.h:368

[bt\_hci\_cp\_host\_buffer\_size](structbt__hci__cp__host__buffer__size.md)

**Definition** hci\_types.h:615

[bt\_hci\_cp\_host\_buffer\_size::acl\_mtu](structbt__hci__cp__host__buffer__size.md#a07039a81ba81c700a26009ea407744b6)

uint16\_t acl\_mtu

**Definition** hci\_types.h:616

[bt\_hci\_cp\_host\_buffer\_size::sco\_mtu](structbt__hci__cp__host__buffer__size.md#a1b1d8c7f60ecbb13699b815bc8fca550)

uint8\_t sco\_mtu

**Definition** hci\_types.h:617

[bt\_hci\_cp\_host\_buffer\_size::acl\_pkts](structbt__hci__cp__host__buffer__size.md#a8240837fecc7c50461724b697f0eda47)

uint16\_t acl\_pkts

**Definition** hci\_types.h:618

[bt\_hci\_cp\_host\_buffer\_size::sco\_pkts](structbt__hci__cp__host__buffer__size.md#a943252480194e1a8608951be08b6b91c)

uint16\_t sco\_pkts

**Definition** hci\_types.h:619

[bt\_hci\_cp\_host\_num\_completed\_packets](structbt__hci__cp__host__num__completed__packets.md)

**Definition** hci\_types.h:628

[bt\_hci\_cp\_host\_num\_completed\_packets::h](structbt__hci__cp__host__num__completed__packets.md#a127f146b4967de49bc74b90ce1643eb7)

struct bt\_hci\_handle\_count h[0]

**Definition** hci\_types.h:630

[bt\_hci\_cp\_host\_num\_completed\_packets::num\_handles](structbt__hci__cp__host__num__completed__packets.md#a43a42e52757de9ec307e8a828dff416f)

uint8\_t num\_handles

**Definition** hci\_types.h:629

[bt\_hci\_cp\_io\_capability\_neg\_reply](structbt__hci__cp__io__capability__neg__reply.md)

**Definition** hci\_types.h:520

[bt\_hci\_cp\_io\_capability\_neg\_reply::reason](structbt__hci__cp__io__capability__neg__reply.md#a82c54e5ad7fd4a6d81952832ae4de373)

uint8\_t reason

**Definition** hci\_types.h:522

[bt\_hci\_cp\_io\_capability\_neg\_reply::bdaddr](structbt__hci__cp__io__capability__neg__reply.md#a8dba05bc84de2573eaea43ea9e428015)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:521

[bt\_hci\_cp\_io\_capability\_reply](structbt__hci__cp__io__capability__reply.md)

**Definition** hci\_types.h:491

[bt\_hci\_cp\_io\_capability\_reply::capability](structbt__hci__cp__io__capability__reply.md#a0995c81ba1f653c59bda9a444fb17915)

uint8\_t capability

**Definition** hci\_types.h:493

[bt\_hci\_cp\_io\_capability\_reply::authentication](structbt__hci__cp__io__capability__reply.md#a8983418dca3a7725f3b113a4d0ee177e)

uint8\_t authentication

**Definition** hci\_types.h:495

[bt\_hci\_cp\_io\_capability\_reply::oob\_data](structbt__hci__cp__io__capability__reply.md#ac002ea0b276200a15d603b5ac83666e5)

uint8\_t oob\_data

**Definition** hci\_types.h:494

[bt\_hci\_cp\_io\_capability\_reply::bdaddr](structbt__hci__cp__io__capability__reply.md#afbe2bc0c1dcc0791a98068b052aea1f2)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:492

[bt\_hci\_cp\_le\_accept\_cis](structbt__hci__cp__le__accept__cis.md)

**Definition** hci\_types.h:2049

[bt\_hci\_cp\_le\_accept\_cis::handle](structbt__hci__cp__le__accept__cis.md#aec6a6c80403d5827df10cd8722bc12e4)

uint16\_t handle

**Definition** hci\_types.h:2050

[bt\_hci\_cp\_le\_add\_dev\_to\_fal](structbt__hci__cp__le__add__dev__to__fal.md)

**Definition** hci\_types.h:1040

[bt\_hci\_cp\_le\_add\_dev\_to\_fal::addr](structbt__hci__cp__le__add__dev__to__fal.md#a11ec9f3cd9b80f34094e70d8eeb13be3)

bt\_addr\_le\_t addr

**Definition** hci\_types.h:1041

[bt\_hci\_cp\_le\_add\_dev\_to\_per\_adv\_list](structbt__hci__cp__le__add__dev__to__per__adv__list.md)

**Definition** hci\_types.h:1640

[bt\_hci\_cp\_le\_add\_dev\_to\_per\_adv\_list::sid](structbt__hci__cp__le__add__dev__to__per__adv__list.md#a97d9c5dd0cc4b3ab7f6ebfec206b7407)

uint8\_t sid

**Definition** hci\_types.h:1642

[bt\_hci\_cp\_le\_add\_dev\_to\_per\_adv\_list::addr](structbt__hci__cp__le__add__dev__to__per__adv__list.md#ad93d72bfa7e4123ee9728f6bf73b69df)

bt\_addr\_le\_t addr

**Definition** hci\_types.h:1641

[bt\_hci\_cp\_le\_add\_dev\_to\_rl](structbt__hci__cp__le__add__dev__to__rl.md)

**Definition** hci\_types.h:1225

[bt\_hci\_cp\_le\_add\_dev\_to\_rl::peer\_id\_addr](structbt__hci__cp__le__add__dev__to__rl.md#a3daf2041f04381a56c2cbcd4bb33f4c0)

bt\_addr\_le\_t peer\_id\_addr

**Definition** hci\_types.h:1226

[bt\_hci\_cp\_le\_add\_dev\_to\_rl::local\_irk](structbt__hci__cp__le__add__dev__to__rl.md#ab5caa38e6eeab09b4a69084b1890317b)

uint8\_t local\_irk[16]

**Definition** hci\_types.h:1228

[bt\_hci\_cp\_le\_add\_dev\_to\_rl::peer\_irk](structbt__hci__cp__le__add__dev__to__rl.md#aedc27c868a7a4cbd3c175f67db4e3242)

uint8\_t peer\_irk[16]

**Definition** hci\_types.h:1227

[bt\_hci\_cp\_le\_big\_create\_sync](structbt__hci__cp__le__big__create__sync.md)

**Definition** hci\_types.h:2107

[bt\_hci\_cp\_le\_big\_create\_sync::bcode](structbt__hci__cp__le__big__create__sync.md#a053475c3af12e6e37dc4befcf634d68f)

uint8\_t bcode[16]

**Definition** hci\_types.h:2111

[bt\_hci\_cp\_le\_big\_create\_sync::mse](structbt__hci__cp__le__big__create__sync.md#a37050e3eb914ff06495695d44c3fdb50)

uint8\_t mse

**Definition** hci\_types.h:2112

[bt\_hci\_cp\_le\_big\_create\_sync::encryption](structbt__hci__cp__le__big__create__sync.md#a482edf3326e2dd720b14a03609c1256a)

uint8\_t encryption

**Definition** hci\_types.h:2110

[bt\_hci\_cp\_le\_big\_create\_sync::sync\_timeout](structbt__hci__cp__le__big__create__sync.md#a55e83bc3722ce2dbf943879a80ef2872)

uint16\_t sync\_timeout

**Definition** hci\_types.h:2113

[bt\_hci\_cp\_le\_big\_create\_sync::big\_handle](structbt__hci__cp__le__big__create__sync.md#a6692dae077ce1ce4f31bc94b9d391afd)

uint8\_t big\_handle

**Definition** hci\_types.h:2108

[bt\_hci\_cp\_le\_big\_create\_sync::bis](structbt__hci__cp__le__big__create__sync.md#a6d1050c2a0522be215d82d3874fed4b6)

uint8\_t bis[0]

**Definition** hci\_types.h:2115

[bt\_hci\_cp\_le\_big\_create\_sync::sync\_handle](structbt__hci__cp__le__big__create__sync.md#a70b031f24cdf231e5c168b155517eae0)

uint16\_t sync\_handle

**Definition** hci\_types.h:2109

[bt\_hci\_cp\_le\_big\_create\_sync::num\_bis](structbt__hci__cp__le__big__create__sync.md#a7efae2c8dc46d13fb2abca677ac152b0)

uint8\_t num\_bis

**Definition** hci\_types.h:2114

[bt\_hci\_cp\_le\_big\_terminate\_sync](structbt__hci__cp__le__big__terminate__sync.md)

**Definition** hci\_types.h:2119

[bt\_hci\_cp\_le\_big\_terminate\_sync::big\_handle](structbt__hci__cp__le__big__terminate__sync.md#ad7e4de2a9a3222c1bb8fa048cacd06fa)

uint8\_t big\_handle

**Definition** hci\_types.h:2120

[bt\_hci\_cp\_le\_conn\_cte\_req\_enable](structbt__hci__cp__le__conn__cte__req__enable.md)

**Definition** hci\_types.h:1808

[bt\_hci\_cp\_le\_conn\_cte\_req\_enable::requested\_cte\_length](structbt__hci__cp__le__conn__cte__req__enable.md#a4d4e41bbe95457ce5e8ad68ffeb85200)

uint8\_t requested\_cte\_length

**Definition** hci\_types.h:1812

[bt\_hci\_cp\_le\_conn\_cte\_req\_enable::requested\_cte\_type](structbt__hci__cp__le__conn__cte__req__enable.md#a5a7443a86e770de4bf7292d813e966e7)

uint8\_t requested\_cte\_type

**Definition** hci\_types.h:1813

[bt\_hci\_cp\_le\_conn\_cte\_req\_enable::cte\_request\_interval](structbt__hci__cp__le__conn__cte__req__enable.md#a956a1a8794b75e962d03cdcf81847cfc)

uint16\_t cte\_request\_interval

**Definition** hci\_types.h:1811

[bt\_hci\_cp\_le\_conn\_cte\_req\_enable::enable](structbt__hci__cp__le__conn__cte__req__enable.md#aaf38e3d5664d81ae7ac8d3b1bb03c646)

uint8\_t enable

**Definition** hci\_types.h:1810

[bt\_hci\_cp\_le\_conn\_cte\_req\_enable::handle](structbt__hci__cp__le__conn__cte__req__enable.md#af340b3b97f9fb12c24baa38415620b44)

uint16\_t handle

**Definition** hci\_types.h:1809

[bt\_hci\_cp\_le\_conn\_cte\_rsp\_enable](structbt__hci__cp__le__conn__cte__rsp__enable.md)

**Definition** hci\_types.h:1822

[bt\_hci\_cp\_le\_conn\_cte\_rsp\_enable::handle](structbt__hci__cp__le__conn__cte__rsp__enable.md#a9d78072143513020620e02a744d4fa9b)

uint16\_t handle

**Definition** hci\_types.h:1823

[bt\_hci\_cp\_le\_conn\_cte\_rsp\_enable::enable](structbt__hci__cp__le__conn__cte__rsp__enable.md#ae5eaaae211732d772ea53f3936ab32d2)

uint8\_t enable

**Definition** hci\_types.h:1824

[bt\_hci\_cp\_le\_conn\_param\_req\_neg\_reply](structbt__hci__cp__le__conn__param__req__neg__reply.md)

**Definition** hci\_types.h:1172

[bt\_hci\_cp\_le\_conn\_param\_req\_neg\_reply::handle](structbt__hci__cp__le__conn__param__req__neg__reply.md#a0040e4a50c5c5479b539eb0bafb7b305)

uint16\_t handle

**Definition** hci\_types.h:1173

[bt\_hci\_cp\_le\_conn\_param\_req\_neg\_reply::reason](structbt__hci__cp__le__conn__param__req__neg__reply.md#a8c283ac844805224b1ffeb9801e8b14b)

uint8\_t reason

**Definition** hci\_types.h:1174

[bt\_hci\_cp\_le\_conn\_param\_req\_reply](structbt__hci__cp__le__conn__param__req__reply.md)

**Definition** hci\_types.h:1157

[bt\_hci\_cp\_le\_conn\_param\_req\_reply::interval\_min](structbt__hci__cp__le__conn__param__req__reply.md#a10547c7d4836980947d17bbde0d75a51)

uint16\_t interval\_min

**Definition** hci\_types.h:1159

[bt\_hci\_cp\_le\_conn\_param\_req\_reply::min\_ce\_len](structbt__hci__cp__le__conn__param__req__reply.md#a512d605d5c4aacf81b78794fcf260abf)

uint16\_t min\_ce\_len

**Definition** hci\_types.h:1163

[bt\_hci\_cp\_le\_conn\_param\_req\_reply::latency](structbt__hci__cp__le__conn__param__req__reply.md#a8c76816cc230387c249ab8e05c402964)

uint16\_t latency

**Definition** hci\_types.h:1161

[bt\_hci\_cp\_le\_conn\_param\_req\_reply::max\_ce\_len](structbt__hci__cp__le__conn__param__req__reply.md#a932e6a3a45ec0409656325f7246d5d7e)

uint16\_t max\_ce\_len

**Definition** hci\_types.h:1164

[bt\_hci\_cp\_le\_conn\_param\_req\_reply::handle](structbt__hci__cp__le__conn__param__req__reply.md#aa3b938afe13d4e05806fb6cdfab5cb14)

uint16\_t handle

**Definition** hci\_types.h:1158

[bt\_hci\_cp\_le\_conn\_param\_req\_reply::interval\_max](structbt__hci__cp__le__conn__param__req__reply.md#aed58f9aa722a284ae39df842394c06cf)

uint16\_t interval\_max

**Definition** hci\_types.h:1160

[bt\_hci\_cp\_le\_conn\_param\_req\_reply::timeout](structbt__hci__cp__le__conn__param__req__reply.md#af25a3f226ceccbe19e7f1482ed5f141e)

uint16\_t timeout

**Definition** hci\_types.h:1162

[bt\_hci\_cp\_le\_create\_big\_test](structbt__hci__cp__le__create__big__test.md)

**Definition** hci\_types.h:2081

[bt\_hci\_cp\_le\_create\_big\_test::max\_pdu](structbt__hci__cp__le__create__big__test.md#a2652e0f340f13635a5da6335ec43e801)

uint16\_t max\_pdu

**Definition** hci\_types.h:2089

[bt\_hci\_cp\_le\_create\_big\_test::pto](structbt__hci__cp__le__create__big__test.md#a2f2eaa258463dd51a9f6042e75ecfec6)

uint8\_t pto

**Definition** hci\_types.h:2095

[bt\_hci\_cp\_le\_create\_big\_test::sdu\_interval](structbt__hci__cp__le__create__big__test.md#a331b1a8ef66804cf20d6681e1bc5aefb)

uint8\_t sdu\_interval[3]

**Definition** hci\_types.h:2085

[bt\_hci\_cp\_le\_create\_big\_test::bcode](structbt__hci__cp__le__create__big__test.md#a333319a03d2087067247c4f5e595b4e5)

uint8\_t bcode[16]

**Definition** hci\_types.h:2097

[bt\_hci\_cp\_le\_create\_big\_test::nse](structbt__hci__cp__le__create__big__test.md#a402c19da1ecf273bc942ecc560730567)

uint8\_t nse

**Definition** hci\_types.h:2087

[bt\_hci\_cp\_le\_create\_big\_test::packing](structbt__hci__cp__le__create__big__test.md#a49822f8e1617e30aab9b0d7d790697a3)

uint8\_t packing

**Definition** hci\_types.h:2091

[bt\_hci\_cp\_le\_create\_big\_test::encryption](structbt__hci__cp__le__create__big__test.md#a50c4308abda01581b436b7867304e982)

uint8\_t encryption

**Definition** hci\_types.h:2096

[bt\_hci\_cp\_le\_create\_big\_test::iso\_interval](structbt__hci__cp__le__create__big__test.md#a6475ae77af80e89bb65596bc6f907a58)

uint16\_t iso\_interval

**Definition** hci\_types.h:2086

[bt\_hci\_cp\_le\_create\_big\_test::irc](structbt__hci__cp__le__create__big__test.md#a66ce7ba0498053a588de9097cbbc0891)

uint8\_t irc

**Definition** hci\_types.h:2094

[bt\_hci\_cp\_le\_create\_big\_test::num\_bis](structbt__hci__cp__le__create__big__test.md#a6ce270f0afd185c44fa5a2c67a7783fb)

uint8\_t num\_bis

**Definition** hci\_types.h:2084

[bt\_hci\_cp\_le\_create\_big\_test::phy](structbt__hci__cp__le__create__big__test.md#a731ca2f90c17a4f3f868660e51649ce6)

uint8\_t phy

**Definition** hci\_types.h:2090

[bt\_hci\_cp\_le\_create\_big\_test::bn](structbt__hci__cp__le__create__big__test.md#a734174187486ac760b8bf0e566166842)

uint8\_t bn

**Definition** hci\_types.h:2093

[bt\_hci\_cp\_le\_create\_big\_test::max\_sdu](structbt__hci__cp__le__create__big__test.md#a7ebbc81306109e035f89154738900395)

uint16\_t max\_sdu

**Definition** hci\_types.h:2088

[bt\_hci\_cp\_le\_create\_big\_test::big\_handle](structbt__hci__cp__le__create__big__test.md#ac202f5cee0c1d0456b200606860fd5ab)

uint8\_t big\_handle

**Definition** hci\_types.h:2082

[bt\_hci\_cp\_le\_create\_big\_test::framing](structbt__hci__cp__le__create__big__test.md#acc5b2c30db0c7642d12019f8241dab26)

uint8\_t framing

**Definition** hci\_types.h:2092

[bt\_hci\_cp\_le\_create\_big\_test::adv\_handle](structbt__hci__cp__le__create__big__test.md#aece09ae6264e0cc1a5548f1603a3f61a)

uint8\_t adv\_handle

**Definition** hci\_types.h:2083

[bt\_hci\_cp\_le\_create\_big](structbt__hci__cp__le__create__big.md)

**Definition** hci\_types.h:2065

[bt\_hci\_cp\_le\_create\_big::max\_sdu](structbt__hci__cp__le__create__big.md#a06fd74e9a5f172060835524da5851c71)

uint16\_t max\_sdu

**Definition** hci\_types.h:2070

[bt\_hci\_cp\_le\_create\_big::bcode](structbt__hci__cp__le__create__big.md#a0b4b2d77cd0f579aab190336b14597c5)

uint8\_t bcode[16]

**Definition** hci\_types.h:2077

[bt\_hci\_cp\_le\_create\_big::max\_latency](structbt__hci__cp__le__create__big.md#a15018e5ebc124bbe90644b38fe3e7e76)

uint16\_t max\_latency

**Definition** hci\_types.h:2071

[bt\_hci\_cp\_le\_create\_big::rtn](structbt__hci__cp__le__create__big.md#a1cb0dd106bf4a1a0c473333d089c95e7)

uint8\_t rtn

**Definition** hci\_types.h:2072

[bt\_hci\_cp\_le\_create\_big::sdu\_interval](structbt__hci__cp__le__create__big.md#a2960a9891b827529c9fa1b68a747e2d5)

uint8\_t sdu\_interval[3]

**Definition** hci\_types.h:2069

[bt\_hci\_cp\_le\_create\_big::framing](structbt__hci__cp__le__create__big.md#a330916d60c05ec2ef7a71933b62c203a)

uint8\_t framing

**Definition** hci\_types.h:2075

[bt\_hci\_cp\_le\_create\_big::encryption](structbt__hci__cp__le__create__big.md#a490bd68d137f8cf60ea2ccd5ea4495e9)

uint8\_t encryption

**Definition** hci\_types.h:2076

[bt\_hci\_cp\_le\_create\_big::phy](structbt__hci__cp__le__create__big.md#a56cb773a03e4927c3b6bf4d2a6ed6ed9)

uint8\_t phy

**Definition** hci\_types.h:2073

[bt\_hci\_cp\_le\_create\_big::adv\_handle](structbt__hci__cp__le__create__big.md#aa686eec31ca4c831262dd34d41f9a1fb)

uint8\_t adv\_handle

**Definition** hci\_types.h:2067

[bt\_hci\_cp\_le\_create\_big::packing](structbt__hci__cp__le__create__big.md#ac027390db21320fb9d1002161c4c2f67)

uint8\_t packing

**Definition** hci\_types.h:2074

[bt\_hci\_cp\_le\_create\_big::num\_bis](structbt__hci__cp__le__create__big.md#ad8491c970417e63c6a98c12278a89c86)

uint8\_t num\_bis

**Definition** hci\_types.h:2068

[bt\_hci\_cp\_le\_create\_big::big\_handle](structbt__hci__cp__le__create__big.md#af5412e4a69c05a09b2e818322636a98a)

uint8\_t big\_handle

**Definition** hci\_types.h:2066

[bt\_hci\_cp\_le\_create\_cis](structbt__hci__cp__le__create__cis.md)

**Definition** hci\_types.h:2033

[bt\_hci\_cp\_le\_create\_cis::cis](structbt__hci__cp__le__create__cis.md#a5a323d09df7813fc9b834cc1d205d101)

struct bt\_hci\_cis cis[0]

**Definition** hci\_types.h:2035

[bt\_hci\_cp\_le\_create\_cis::num\_cis](structbt__hci__cp__le__create__cis.md#acd348a7d68947af8e7119b2e1a864481)

uint8\_t num\_cis

**Definition** hci\_types.h:2034

[bt\_hci\_cp\_le\_create\_conn](structbt__hci__cp__le__create__conn.md)

**Definition** hci\_types.h:1015

[bt\_hci\_cp\_le\_create\_conn::scan\_interval](structbt__hci__cp__le__create__conn.md#a1a830a0f6cd961d534c338031b2b691b)

uint16\_t scan\_interval

**Definition** hci\_types.h:1016

[bt\_hci\_cp\_le\_create\_conn::filter\_policy](structbt__hci__cp__le__create__conn.md#a2ca5063f5082a0f330676e56253a21c7)

uint8\_t filter\_policy

**Definition** hci\_types.h:1018

[bt\_hci\_cp\_le\_create\_conn::min\_ce\_len](structbt__hci__cp__le__create__conn.md#a476501ccd209f3a52082decf906ca8f0)

uint16\_t min\_ce\_len

**Definition** hci\_types.h:1025

[bt\_hci\_cp\_le\_create\_conn::conn\_latency](structbt__hci__cp__le__create__conn.md#a5a9d5c1d44adac876680a517b1fad63f)

uint16\_t conn\_latency

**Definition** hci\_types.h:1023

[bt\_hci\_cp\_le\_create\_conn::max\_ce\_len](structbt__hci__cp__le__create__conn.md#a5b329aa8b48e03998e969b2436d35ab5)

uint16\_t max\_ce\_len

**Definition** hci\_types.h:1026

[bt\_hci\_cp\_le\_create\_conn::own\_addr\_type](structbt__hci__cp__le__create__conn.md#a63c7f9e89528105e484a60e41eeb8a30)

uint8\_t own\_addr\_type

**Definition** hci\_types.h:1020

[bt\_hci\_cp\_le\_create\_conn::conn\_interval\_min](structbt__hci__cp__le__create__conn.md#a988cf154b0df1ff9af8d34ce73a920dd)

uint16\_t conn\_interval\_min

**Definition** hci\_types.h:1021

[bt\_hci\_cp\_le\_create\_conn::conn\_interval\_max](structbt__hci__cp__le__create__conn.md#aa009d54866d9c675c2785412bdbd182f)

uint16\_t conn\_interval\_max

**Definition** hci\_types.h:1022

[bt\_hci\_cp\_le\_create\_conn::peer\_addr](structbt__hci__cp__le__create__conn.md#aa51da7602eb2b44528964c8b706bb043)

bt\_addr\_le\_t peer\_addr

**Definition** hci\_types.h:1019

[bt\_hci\_cp\_le\_create\_conn::scan\_window](structbt__hci__cp__le__create__conn.md#abf61e67f5e20adc44b5b9314ed43bccc)

uint16\_t scan\_window

**Definition** hci\_types.h:1017

[bt\_hci\_cp\_le\_create\_conn::supervision\_timeout](structbt__hci__cp__le__create__conn.md#ae8e0ad70a3b23ac035c237db0d57adc4)

uint16\_t supervision\_timeout

**Definition** hci\_types.h:1024

[bt\_hci\_cp\_le\_default\_past\_param](structbt__hci__cp__le__default__past__param.md)

**Definition** hci\_types.h:1913

[bt\_hci\_cp\_le\_default\_past\_param::timeout](structbt__hci__cp__le__default__past__param.md#a159f5245f86b27198264bdcf394d719f)

uint16\_t timeout

**Definition** hci\_types.h:1916

[bt\_hci\_cp\_le\_default\_past\_param::skip](structbt__hci__cp__le__default__past__param.md#a214cb0597d0065bc2c056fe9c51a2220)

uint16\_t skip

**Definition** hci\_types.h:1915

[bt\_hci\_cp\_le\_default\_past\_param::mode](structbt__hci__cp__le__default__past__param.md#a2ef92304264ad0bf1560accf306bb6d9)

uint8\_t mode

**Definition** hci\_types.h:1914

[bt\_hci\_cp\_le\_default\_past\_param::cte\_type](structbt__hci__cp__le__default__past__param.md#af18f679f5833c1d782b4e474af5d819c)

uint8\_t cte\_type

**Definition** hci\_types.h:1917

[bt\_hci\_cp\_le\_encrypt](structbt__hci__cp__le__encrypt.md)

**Definition** hci\_types.h:1081

[bt\_hci\_cp\_le\_encrypt::key](structbt__hci__cp__le__encrypt.md#ab64f1bab8ad3a98217db96e6765a7d24)

uint8\_t key[16]

**Definition** hci\_types.h:1082

[bt\_hci\_cp\_le\_encrypt::plaintext](structbt__hci__cp__le__encrypt.md#ad520b84e6e2a4e62f7fefba248c4cf10)

uint8\_t plaintext[16]

**Definition** hci\_types.h:1083

[bt\_hci\_cp\_le\_enh\_rx\_test](structbt__hci__cp__le__enh__rx__test.md)

**Definition** hci\_types.h:1334

[bt\_hci\_cp\_le\_enh\_rx\_test::rx\_ch](structbt__hci__cp__le__enh__rx__test.md#a3aa5b3947a4a0c87342695469bf056ec)

uint8\_t rx\_ch

**Definition** hci\_types.h:1335

[bt\_hci\_cp\_le\_enh\_rx\_test::mod\_index](structbt__hci__cp__le__enh__rx__test.md#a9151393e9f05a2ded484a1248a6edb88)

uint8\_t mod\_index

**Definition** hci\_types.h:1337

[bt\_hci\_cp\_le\_enh\_rx\_test::phy](structbt__hci__cp__le__enh__rx__test.md#aa2bf385221680b25ce184b4ea5d63cd4)

uint8\_t phy

**Definition** hci\_types.h:1336

[bt\_hci\_cp\_le\_enh\_tx\_test](structbt__hci__cp__le__enh__tx__test.md)

**Definition** hci\_types.h:1346

[bt\_hci\_cp\_le\_enh\_tx\_test::tx\_ch](structbt__hci__cp__le__enh__tx__test.md#a0b7883b36d511c6da1bac543f1aae446)

uint8\_t tx\_ch

**Definition** hci\_types.h:1347

[bt\_hci\_cp\_le\_enh\_tx\_test::phy](structbt__hci__cp__le__enh__tx__test.md#a718442db29c5ac455c3e2aac9844cdd0)

uint8\_t phy

**Definition** hci\_types.h:1350

[bt\_hci\_cp\_le\_enh\_tx\_test::pkt\_payload](structbt__hci__cp__le__enh__tx__test.md#a9ccb91be1554172d6c724e438508bfe5)

uint8\_t pkt\_payload

**Definition** hci\_types.h:1349

[bt\_hci\_cp\_le\_enh\_tx\_test::test\_data\_len](structbt__hci__cp__le__enh__tx__test.md#af1e27be0ad23887c0e71024739b00f8d)

uint8\_t test\_data\_len

**Definition** hci\_types.h:1348

[bt\_hci\_cp\_le\_ext\_create\_conn\_v2](structbt__hci__cp__le__ext__create__conn__v2.md)

**Definition** hci\_types.h:1547

[bt\_hci\_cp\_le\_ext\_create\_conn\_v2::own\_addr\_type](structbt__hci__cp__le__ext__create__conn__v2.md#a05fd0089a0fd43f98042835231407a60)

uint8\_t own\_addr\_type

**Definition** hci\_types.h:1551

[bt\_hci\_cp\_le\_ext\_create\_conn\_v2::peer\_addr](structbt__hci__cp__le__ext__create__conn__v2.md#a25466a04d224bdf495266b0064c424dd)

bt\_addr\_le\_t peer\_addr

**Definition** hci\_types.h:1552

[bt\_hci\_cp\_le\_ext\_create\_conn\_v2::subevent](structbt__hci__cp__le__ext__create__conn__v2.md#a536da199958b3b54469f5b4b029e1bac)

uint8\_t subevent

**Definition** hci\_types.h:1549

[bt\_hci\_cp\_le\_ext\_create\_conn\_v2::filter\_policy](structbt__hci__cp__le__ext__create__conn__v2.md#a66632dbac1605cff69e8da566e800347)

uint8\_t filter\_policy

**Definition** hci\_types.h:1550

[bt\_hci\_cp\_le\_ext\_create\_conn\_v2::p](structbt__hci__cp__le__ext__create__conn__v2.md#a8d606c5aa480f54c8da9f42a35ad513e)

struct bt\_hci\_ext\_conn\_phy p[0]

**Definition** hci\_types.h:1554

[bt\_hci\_cp\_le\_ext\_create\_conn\_v2::adv\_handle](structbt__hci__cp__le__ext__create__conn__v2.md#addf1f80c4d3625e0c6d6e716f6e2e207)

uint8\_t adv\_handle

**Definition** hci\_types.h:1548

[bt\_hci\_cp\_le\_ext\_create\_conn\_v2::phys](structbt__hci__cp__le__ext__create__conn__v2.md#ae2d3e3079a2848907224bb7ff0efc64b)

uint8\_t phys

**Definition** hci\_types.h:1553

[bt\_hci\_cp\_le\_ext\_create\_conn](structbt__hci__cp__le__ext__create__conn.md)

**Definition** hci\_types.h:1539

[bt\_hci\_cp\_le\_ext\_create\_conn::filter\_policy](structbt__hci__cp__le__ext__create__conn.md#a0561b446effa3f735a405c0b307466bf)

uint8\_t filter\_policy

**Definition** hci\_types.h:1540

[bt\_hci\_cp\_le\_ext\_create\_conn::own\_addr\_type](structbt__hci__cp__le__ext__create__conn.md#a12a99044f54e3d5dae30a64392444cbf)

uint8\_t own\_addr\_type

**Definition** hci\_types.h:1541

[bt\_hci\_cp\_le\_ext\_create\_conn::peer\_addr](structbt__hci__cp__le__ext__create__conn.md#a79bc55d9f5b1d719de4fb404db9008f3)

bt\_addr\_le\_t peer\_addr

**Definition** hci\_types.h:1542

[bt\_hci\_cp\_le\_ext\_create\_conn::p](structbt__hci__cp__le__ext__create__conn.md#acdb436d6bf2864745ec579622ae0d532)

struct bt\_hci\_ext\_conn\_phy p[0]

**Definition** hci\_types.h:1544

[bt\_hci\_cp\_le\_ext\_create\_conn::phys](structbt__hci__cp__le__ext__create__conn.md#ae859ff0da5e9cdc872943fd74774ef7e)

uint8\_t phys

**Definition** hci\_types.h:1543

[bt\_hci\_cp\_le\_generate\_dhkey\_v2](structbt__hci__cp__le__generate__dhkey__v2.md)

**Definition** hci\_types.h:1218

[bt\_hci\_cp\_le\_generate\_dhkey\_v2::key\_type](structbt__hci__cp__le__generate__dhkey__v2.md#a3d47ad6d9df4d4023d2586c915ee8f2c)

uint8\_t key\_type

**Definition** hci\_types.h:1220

[bt\_hci\_cp\_le\_generate\_dhkey\_v2::key](structbt__hci__cp__le__generate__dhkey__v2.md#acc3007adf301674b9e847297007c3cd1)

uint8\_t key[64]

**Definition** hci\_types.h:1219

[bt\_hci\_cp\_le\_generate\_dhkey](structbt__hci__cp__le__generate__dhkey.md)

**Definition** hci\_types.h:1208

[bt\_hci\_cp\_le\_generate\_dhkey::key](structbt__hci__cp__le__generate__dhkey.md#a0f67195504d877a1d11b7dfb77d09fcc)

uint8\_t key[64]

**Definition** hci\_types.h:1209

[bt\_hci\_cp\_le\_iso\_receive\_test](structbt__hci__cp__le__iso__receive__test.md)

**Definition** hci\_types.h:2176

[bt\_hci\_cp\_le\_iso\_receive\_test::payload\_type](structbt__hci__cp__le__iso__receive__test.md#a9ce7e13fc1c1a7c87c01e1ecb24c5324)

uint8\_t payload\_type

**Definition** hci\_types.h:2178

[bt\_hci\_cp\_le\_iso\_receive\_test::handle](structbt__hci__cp__le__iso__receive__test.md#ac1272441f5c7b79e1ef5f644f099d19e)

uint16\_t handle

**Definition** hci\_types.h:2177

[bt\_hci\_cp\_le\_iso\_test\_end](structbt__hci__cp__le__iso__test__end.md)

**Definition** hci\_types.h:2200

[bt\_hci\_cp\_le\_iso\_test\_end::handle](structbt__hci__cp__le__iso__test__end.md#ab792ec021319024828bd7609e0fe7e96)

uint16\_t handle

**Definition** hci\_types.h:2201

[bt\_hci\_cp\_le\_iso\_transmit\_test](structbt__hci__cp__le__iso__transmit__test.md)

**Definition** hci\_types.h:2165

[bt\_hci\_cp\_le\_iso\_transmit\_test::payload\_type](structbt__hci__cp__le__iso__transmit__test.md#a0653c77af723cc43a6b911816a8db437)

uint8\_t payload\_type

**Definition** hci\_types.h:2167

[bt\_hci\_cp\_le\_iso\_transmit\_test::handle](structbt__hci__cp__le__iso__transmit__test.md#adffb0d57afc090692ab36ebeaad21bbd)

uint16\_t handle

**Definition** hci\_types.h:2166

[bt\_hci\_cp\_le\_ltk\_req\_neg\_reply](structbt__hci__cp__le__ltk__req__neg__reply.md)

**Definition** hci\_types.h:1115

[bt\_hci\_cp\_le\_ltk\_req\_neg\_reply::handle](structbt__hci__cp__le__ltk__req__neg__reply.md#add8cc3b13432e233ceb5c2c11e0107c0)

uint16\_t handle

**Definition** hci\_types.h:1116

[bt\_hci\_cp\_le\_ltk\_req\_reply](structbt__hci__cp__le__ltk__req__reply.md)

**Definition** hci\_types.h:1105

[bt\_hci\_cp\_le\_ltk\_req\_reply::ltk](structbt__hci__cp__le__ltk__req__reply.md#a2d16b44af344237a890341943c4a6582)

uint8\_t ltk[16]

**Definition** hci\_types.h:1107

[bt\_hci\_cp\_le\_ltk\_req\_reply::handle](structbt__hci__cp__le__ltk__req__reply.md#a46d87451acc1f1ce2ff35dd0dd238db3)

uint16\_t handle

**Definition** hci\_types.h:1106

[bt\_hci\_cp\_le\_past\_param](structbt__hci__cp__le__past__param.md)

**Definition** hci\_types.h:1899

[bt\_hci\_cp\_le\_past\_param::cte\_type](structbt__hci__cp__le__past__param.md#a47c571ff27a59e0a7cbcb460303ee194)

uint8\_t cte\_type

**Definition** hci\_types.h:1904

[bt\_hci\_cp\_le\_past\_param::skip](structbt__hci__cp__le__past__param.md#a622499d51e917f7828629de2291812e5)

uint16\_t skip

**Definition** hci\_types.h:1902

[bt\_hci\_cp\_le\_past\_param::conn\_handle](structbt__hci__cp__le__past__param.md#a9c99cdd5ae5de58960677781c2287c4d)

uint16\_t conn\_handle

**Definition** hci\_types.h:1900

[bt\_hci\_cp\_le\_past\_param::mode](structbt__hci__cp__le__past__param.md#aa36345a550dfabeef48b430d1a1b0030)

uint8\_t mode

**Definition** hci\_types.h:1901

[bt\_hci\_cp\_le\_past\_param::timeout](structbt__hci__cp__le__past__param.md#aec9aa4ffe41c6b6f5cfcbc59eb57efca)

uint16\_t timeout

**Definition** hci\_types.h:1903

[bt\_hci\_cp\_le\_per\_adv\_create\_sync](structbt__hci__cp__le__per__adv__create__sync.md)

**Definition** hci\_types.h:1623

[bt\_hci\_cp\_le\_per\_adv\_create\_sync::addr](structbt__hci__cp__le__per__adv__create__sync.md#a3a0a0bc1bd5014f2ede0c4ef6cc30d24)

bt\_addr\_le\_t addr

**Definition** hci\_types.h:1626

[bt\_hci\_cp\_le\_per\_adv\_create\_sync::sync\_timeout](structbt__hci__cp__le__per__adv__create__sync.md#a46ea01403f68d42a315ff629374b2a95)

uint16\_t sync\_timeout

**Definition** hci\_types.h:1628

[bt\_hci\_cp\_le\_per\_adv\_create\_sync::skip](structbt__hci__cp__le__per__adv__create__sync.md#a554552684fa2a8d0022f9e31ade9c222)

uint16\_t skip

**Definition** hci\_types.h:1627

[bt\_hci\_cp\_le\_per\_adv\_create\_sync::cte\_type](structbt__hci__cp__le__per__adv__create__sync.md#a905b2a9166dd668df5929f0866769576)

uint8\_t cte\_type

**Definition** hci\_types.h:1629

[bt\_hci\_cp\_le\_per\_adv\_create\_sync::sid](structbt__hci__cp__le__per__adv__create__sync.md#ab5c4debe1babb98c60c1f1bfdf55359a)

uint8\_t sid

**Definition** hci\_types.h:1625

[bt\_hci\_cp\_le\_per\_adv\_create\_sync::options](structbt__hci__cp__le__per__adv__create__sync.md#aff300f352ec5f0fece90f88db811ef75)

uint8\_t options

**Definition** hci\_types.h:1624

[bt\_hci\_cp\_le\_per\_adv\_set\_info\_transfer](structbt__hci__cp__le__per__adv__set__info__transfer.md)

**Definition** hci\_types.h:1876

[bt\_hci\_cp\_le\_per\_adv\_set\_info\_transfer::conn\_handle](structbt__hci__cp__le__per__adv__set__info__transfer.md#a3b2f0c510ef9b385cb42bf9a194fa574)

uint16\_t conn\_handle

**Definition** hci\_types.h:1877

[bt\_hci\_cp\_le\_per\_adv\_set\_info\_transfer::service\_data](structbt__hci__cp__le__per__adv__set__info__transfer.md#a5f14c3265bffdf3e30a554a3686e9e0c)

uint16\_t service\_data

**Definition** hci\_types.h:1878

[bt\_hci\_cp\_le\_per\_adv\_set\_info\_transfer::adv\_handle](structbt__hci__cp__le__per__adv__set__info__transfer.md#a75b2c0fa1d50ef9d3761ac25f487750b)

uint8\_t adv\_handle

**Definition** hci\_types.h:1879

[bt\_hci\_cp\_le\_per\_adv\_sync\_transfer](structbt__hci__cp__le__per__adv__sync__transfer.md)

**Definition** hci\_types.h:1864

[bt\_hci\_cp\_le\_per\_adv\_sync\_transfer::service\_data](structbt__hci__cp__le__per__adv__sync__transfer.md#a1327de0f9b2ebd1eaa97b51850087460)

uint16\_t service\_data

**Definition** hci\_types.h:1866

[bt\_hci\_cp\_le\_per\_adv\_sync\_transfer::sync\_handle](structbt__hci__cp__le__per__adv__sync__transfer.md#a38537b7f01a93f7a3e8cfcb92098a172)

uint16\_t sync\_handle

**Definition** hci\_types.h:1867

[bt\_hci\_cp\_le\_per\_adv\_sync\_transfer::conn\_handle](structbt__hci__cp__le__per__adv__sync__transfer.md#a991f77d6f2f0c301fe3322050b2d359f)

uint16\_t conn\_handle

**Definition** hci\_types.h:1865

[bt\_hci\_cp\_le\_per\_adv\_terminate\_sync](structbt__hci__cp__le__per__adv__terminate__sync.md)

**Definition** hci\_types.h:1635

[bt\_hci\_cp\_le\_per\_adv\_terminate\_sync::handle](structbt__hci__cp__le__per__adv__terminate__sync.md#a607fce7fd5c88e12f82e3d9731bd7f1a)

uint16\_t handle

**Definition** hci\_types.h:1636

[bt\_hci\_cp\_le\_read\_chan\_map](structbt__hci__cp__le__read__chan__map.md)

**Definition** hci\_types.h:1066

[bt\_hci\_cp\_le\_read\_chan\_map::handle](structbt__hci__cp__le__read__chan__map.md#abea9aec016a0433b3e4837d53d6b5d2b)

uint16\_t handle

**Definition** hci\_types.h:1067

[bt\_hci\_cp\_le\_read\_iso\_link\_quality](structbt__hci__cp__le__read__iso__link__quality.md)

**Definition** hci\_types.h:2223

[bt\_hci\_cp\_le\_read\_iso\_link\_quality::handle](structbt__hci__cp__le__read__iso__link__quality.md#a346fb3cf08203725d5943e42f03cb40d)

uint16\_t handle

**Definition** hci\_types.h:2224

[bt\_hci\_cp\_le\_read\_iso\_tx\_sync](structbt__hci__cp__le__read__iso__tx__sync.md)

**Definition** hci\_types.h:1934

[bt\_hci\_cp\_le\_read\_iso\_tx\_sync::handle](structbt__hci__cp__le__read__iso__tx__sync.md#a8edc469f73540d4300b1716c96e17c9f)

uint16\_t handle

**Definition** hci\_types.h:1935

[bt\_hci\_cp\_le\_read\_local\_rpa](structbt__hci__cp__le__read__local__rpa.md)

**Definition** hci\_types.h:1254

[bt\_hci\_cp\_le\_read\_local\_rpa::peer\_id\_addr](structbt__hci__cp__le__read__local__rpa.md#aa96cd60066003e4a7a1f482fb81557f8)

bt\_addr\_le\_t peer\_id\_addr

**Definition** hci\_types.h:1255

[bt\_hci\_cp\_le\_read\_peer\_rpa](structbt__hci__cp__le__read__peer__rpa.md)

**Definition** hci\_types.h:1245

[bt\_hci\_cp\_le\_read\_peer\_rpa::peer\_id\_addr](structbt__hci__cp__le__read__peer__rpa.md#ab0c70a1dbe5152b1fc926b90ec3387b3)

bt\_addr\_le\_t peer\_id\_addr

**Definition** hci\_types.h:1246

[bt\_hci\_cp\_le\_read\_phy](structbt__hci__cp__le__read__phy.md)

**Definition** hci\_types.h:1289

[bt\_hci\_cp\_le\_read\_phy::handle](structbt__hci__cp__le__read__phy.md#a7e0a4fa47b613c86364e6e94c2d0bef1)

uint16\_t handle

**Definition** hci\_types.h:1290

[bt\_hci\_cp\_le\_read\_remote\_features](structbt__hci__cp__le__read__remote__features.md)

**Definition** hci\_types.h:1076

[bt\_hci\_cp\_le\_read\_remote\_features::handle](structbt__hci__cp__le__read__remote__features.md#a843997555fd36f102c83a7d59f65eea9)

uint16\_t handle

**Definition** hci\_types.h:1077

[bt\_hci\_cp\_le\_read\_test\_counters](structbt__hci__cp__le__read__test__counters.md)

**Definition** hci\_types.h:2187

[bt\_hci\_cp\_le\_read\_test\_counters::handle](structbt__hci__cp__le__read__test__counters.md#a230d973c2db177c3595bb4808ebf5cd2)

uint16\_t handle

**Definition** hci\_types.h:2188

[bt\_hci\_cp\_le\_read\_tx\_power\_level](structbt__hci__cp__le__read__tx__power__level.md)

**Definition** hci\_types.h:583

[bt\_hci\_cp\_le\_read\_tx\_power\_level::phy](structbt__hci__cp__le__read__tx__power__level.md#a4863396dfe4dca65aaef68293e29291b)

uint8\_t phy

**Definition** hci\_types.h:585

[bt\_hci\_cp\_le\_read\_tx\_power\_level::handle](structbt__hci__cp__le__read__tx__power__level.md#af8c2d89b183d7bdc0f55a0bf783a373d)

uint16\_t handle

**Definition** hci\_types.h:584

[bt\_hci\_cp\_le\_reject\_cis](structbt__hci__cp__le__reject__cis.md)

**Definition** hci\_types.h:2054

[bt\_hci\_cp\_le\_reject\_cis::handle](structbt__hci__cp__le__reject__cis.md#ad697d740bdf5a565090a548e7e8fd399)

uint16\_t handle

**Definition** hci\_types.h:2055

[bt\_hci\_cp\_le\_reject\_cis::reason](structbt__hci__cp__le__reject__cis.md#aec5bd3e4d27b6e3a2653112b36a3d128)

uint8\_t reason

**Definition** hci\_types.h:2056

[bt\_hci\_cp\_le\_rem\_dev\_from\_fal](structbt__hci__cp__le__rem__dev__from__fal.md)

**Definition** hci\_types.h:1045

[bt\_hci\_cp\_le\_rem\_dev\_from\_fal::addr](structbt__hci__cp__le__rem__dev__from__fal.md#afe6054303093cc930d1089ca6a16101c)

bt\_addr\_le\_t addr

**Definition** hci\_types.h:1046

[bt\_hci\_cp\_le\_rem\_dev\_from\_per\_adv\_list](structbt__hci__cp__le__rem__dev__from__per__adv__list.md)

**Definition** hci\_types.h:1646

[bt\_hci\_cp\_le\_rem\_dev\_from\_per\_adv\_list::sid](structbt__hci__cp__le__rem__dev__from__per__adv__list.md#a6629f3ececf586792a14f3c028cc8e8c)

uint8\_t sid

**Definition** hci\_types.h:1648

[bt\_hci\_cp\_le\_rem\_dev\_from\_per\_adv\_list::addr](structbt__hci__cp__le__rem__dev__from__per__adv__list.md#adc420288f6a79c1a92f57241d3da3d81)

bt\_addr\_le\_t addr

**Definition** hci\_types.h:1647

[bt\_hci\_cp\_le\_rem\_dev\_from\_rl](structbt__hci__cp__le__rem__dev__from__rl.md)

**Definition** hci\_types.h:1232

[bt\_hci\_cp\_le\_rem\_dev\_from\_rl::peer\_id\_addr](structbt__hci__cp__le__rem__dev__from__rl.md#aacb577a7ae13322145fccdffc3161541)

bt\_addr\_le\_t peer\_id\_addr

**Definition** hci\_types.h:1233

[bt\_hci\_cp\_le\_remove\_adv\_set](structbt__hci__cp__le__remove__adv__set.md)

**Definition** hci\_types.h:1456

[bt\_hci\_cp\_le\_remove\_adv\_set::handle](structbt__hci__cp__le__remove__adv__set.md#ab33bf918b10d847bb8fb8ac2409780e6)

uint8\_t handle

**Definition** hci\_types.h:1457

[bt\_hci\_cp\_le\_remove\_cig](structbt__hci__cp__le__remove__cig.md)

**Definition** hci\_types.h:2039

[bt\_hci\_cp\_le\_remove\_cig::cig\_id](structbt__hci__cp__le__remove__cig.md#addf395d945f14afbf2d39fa4d0d22f31)

uint8\_t cig\_id

**Definition** hci\_types.h:2040

[bt\_hci\_cp\_le\_remove\_iso\_path](structbt__hci__cp__le__remove__iso__path.md)

**Definition** hci\_types.h:2150

[bt\_hci\_cp\_le\_remove\_iso\_path::path\_dir](structbt__hci__cp__le__remove__iso__path.md#a46e4b28917ff963ff4b672749fde0971)

uint8\_t path\_dir

**Definition** hci\_types.h:2152

[bt\_hci\_cp\_le\_remove\_iso\_path::handle](structbt__hci__cp__le__remove__iso__path.md#ad0106791003f9d1173f2a9f102903c45)

uint16\_t handle

**Definition** hci\_types.h:2151

[bt\_hci\_cp\_le\_req\_peer\_sca](structbt__hci__cp__le__req__peer__sca.md)

**Definition** hci\_types.h:2129

[bt\_hci\_cp\_le\_req\_peer\_sca::handle](structbt__hci__cp__le__req__peer__sca.md#a39d65681da55b26f2900f06cde637d88)

uint16\_t handle

**Definition** hci\_types.h:2130

[bt\_hci\_cp\_le\_rx\_test\_v3](structbt__hci__cp__le__rx__test__v3.md)

**Definition** hci\_types.h:1694

[bt\_hci\_cp\_le\_rx\_test\_v3::expected\_cte\_type](structbt__hci__cp__le__rx__test__v3.md#a55b5c4739e456167f17bf3899d096e61)

uint8\_t expected\_cte\_type

**Definition** hci\_types.h:1699

[bt\_hci\_cp\_le\_rx\_test\_v3::slot\_durations](structbt__hci__cp__le__rx__test__v3.md#a5cd5a44b0832b9f6e2198b9ad714b99b)

uint8\_t slot\_durations

**Definition** hci\_types.h:1700

[bt\_hci\_cp\_le\_rx\_test\_v3::mod\_index](structbt__hci__cp__le__rx__test__v3.md#a7ffde9dc565194c0108177cf11b02b5b)

uint8\_t mod\_index

**Definition** hci\_types.h:1697

[bt\_hci\_cp\_le\_rx\_test\_v3::ant\_ids](structbt__hci__cp__le__rx__test__v3.md#aa6cd0835068f378949da182af13e2438)

uint8\_t ant\_ids[0]

**Definition** hci\_types.h:1702

[bt\_hci\_cp\_le\_rx\_test\_v3::switch\_pattern\_len](structbt__hci__cp__le__rx__test__v3.md#ab0832e72ef90b1269928378638fcb194)

uint8\_t switch\_pattern\_len

**Definition** hci\_types.h:1701

[bt\_hci\_cp\_le\_rx\_test\_v3::rx\_ch](structbt__hci__cp__le__rx__test__v3.md#abd33b70c948d4ee42d96d0d2e7f7cb1c)

uint8\_t rx\_ch

**Definition** hci\_types.h:1695

[bt\_hci\_cp\_le\_rx\_test\_v3::expected\_cte\_len](structbt__hci__cp__le__rx__test__v3.md#ad1a1082d27b8a10e25eebd347404637c)

uint8\_t expected\_cte\_len

**Definition** hci\_types.h:1698

[bt\_hci\_cp\_le\_rx\_test\_v3::phy](structbt__hci__cp__le__rx__test__v3.md#ad1c211c59cf34d76429d4d4548966630)

uint8\_t phy

**Definition** hci\_types.h:1696

[bt\_hci\_cp\_le\_rx\_test](structbt__hci__cp__le__rx__test.md)

**Definition** hci\_types.h:1130

[bt\_hci\_cp\_le\_rx\_test::rx\_ch](structbt__hci__cp__le__rx__test.md#a11cb21a7625d9c097eba0a7b68e93f3f)

uint8\_t rx\_ch

**Definition** hci\_types.h:1131

[bt\_hci\_cp\_le\_set\_addr\_res\_enable](structbt__hci__cp__le__set__addr__res__enable.md)

**Definition** hci\_types.h:1266

[bt\_hci\_cp\_le\_set\_addr\_res\_enable::enable](structbt__hci__cp__le__set__addr__res__enable.md#ad0548178cbc9bc2db54612a748a2bd65)

uint8\_t enable

**Definition** hci\_types.h:1267

[bt\_hci\_cp\_le\_set\_adv\_data](structbt__hci__cp__le__set__adv__data.md)

**Definition** hci\_types.h:960

[bt\_hci\_cp\_le\_set\_adv\_data::len](structbt__hci__cp__le__set__adv__data.md#a664313db17c12adb0de14371e46d26a8)

uint8\_t len

**Definition** hci\_types.h:961

[bt\_hci\_cp\_le\_set\_adv\_data::data](structbt__hci__cp__le__set__adv__data.md#a6fb8734ff5a9b77586b3e283b83985bb)

uint8\_t data[31]

**Definition** hci\_types.h:962

[bt\_hci\_cp\_le\_set\_adv\_enable](structbt__hci__cp__le__set__adv__enable.md)

**Definition** hci\_types.h:975

[bt\_hci\_cp\_le\_set\_adv\_enable::enable](structbt__hci__cp__le__set__adv__enable.md#a15e92d187d586fef560adf9c793f776a)

uint8\_t enable

**Definition** hci\_types.h:976

[bt\_hci\_cp\_le\_set\_adv\_param](structbt__hci__cp__le__set__adv__param.md)

**Definition** hci\_types.h:943

[bt\_hci\_cp\_le\_set\_adv\_param::channel\_map](structbt__hci__cp__le__set__adv__param.md#a2269ae424e47adddce5aa5f2f5b84c89)

uint8\_t channel\_map

**Definition** hci\_types.h:949

[bt\_hci\_cp\_le\_set\_adv\_param::min\_interval](structbt__hci__cp__le__set__adv__param.md#a2476c2a1858eab7e9b1449c1901363c4)

uint16\_t min\_interval

**Definition** hci\_types.h:944

[bt\_hci\_cp\_le\_set\_adv\_param::filter\_policy](structbt__hci__cp__le__set__adv__param.md#a662c5ae81f25a897a8e597f7227a1e39)

uint8\_t filter\_policy

**Definition** hci\_types.h:950

[bt\_hci\_cp\_le\_set\_adv\_param::type](structbt__hci__cp__le__set__adv__param.md#a9b09964156846fd480911dcc2d996a98)

uint8\_t type

**Definition** hci\_types.h:946

[bt\_hci\_cp\_le\_set\_adv\_param::max\_interval](structbt__hci__cp__le__set__adv__param.md#ab42c6b8f482e782d09386a3a1758903d)

uint16\_t max\_interval

**Definition** hci\_types.h:945

[bt\_hci\_cp\_le\_set\_adv\_param::direct\_addr](structbt__hci__cp__le__set__adv__param.md#ac774ef72175e43b083d04ecac263941b)

bt\_addr\_le\_t direct\_addr

**Definition** hci\_types.h:948

[bt\_hci\_cp\_le\_set\_adv\_param::own\_addr\_type](structbt__hci__cp__le__set__adv__param.md#ad8c74cac74254354b314f07df7df1bf0)

uint8\_t own\_addr\_type

**Definition** hci\_types.h:947

[bt\_hci\_cp\_le\_set\_adv\_set\_random\_addr](structbt__hci__cp__le__set__adv__set__random__addr.md)

**Definition** hci\_types.h:1354

[bt\_hci\_cp\_le\_set\_adv\_set\_random\_addr::bdaddr](structbt__hci__cp__le__set__adv__set__random__addr.md#a2883e9bf7ef6a34712eda2594e23c146)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:1356

[bt\_hci\_cp\_le\_set\_adv\_set\_random\_addr::handle](structbt__hci__cp__le__set__adv__set__random__addr.md#aafa39422a16cc4ff11c8073e9c0aab71)

uint8\_t handle

**Definition** hci\_types.h:1355

[bt\_hci\_cp\_le\_set\_cig\_params\_test](structbt__hci__cp__le__set__cig__params__test.md)

**Definition** hci\_types.h:2006

[bt\_hci\_cp\_le\_set\_cig\_params\_test::p\_interval](structbt__hci__cp__le__set__cig__params__test.md#a0cf0f3f7c10b29d74ab64aa30a4969de)

uint8\_t p\_interval[3]

**Definition** hci\_types.h:2009

[bt\_hci\_cp\_le\_set\_cig\_params\_test::cig\_id](structbt__hci__cp__le__set__cig__params__test.md#a161ae960cbd4f7833815285d04f87e46)

uint8\_t cig\_id

**Definition** hci\_types.h:2007

[bt\_hci\_cp\_le\_set\_cig\_params\_test::sca](structbt__hci__cp__le__set__cig__params__test.md#a1d060539ff26677c1326a6ed3394fb6e)

uint8\_t sca

**Definition** hci\_types.h:2013

[bt\_hci\_cp\_le\_set\_cig\_params\_test::c\_ft](structbt__hci__cp__le__set__cig__params__test.md#a1eae50a97188304852589fd95e994150)

uint8\_t c\_ft

**Definition** hci\_types.h:2010

[bt\_hci\_cp\_le\_set\_cig\_params\_test::framing](structbt__hci__cp__le__set__cig__params__test.md#a2cb6745b8f908cd2e7d5f12a092c3b69)

uint8\_t framing

**Definition** hci\_types.h:2015

[bt\_hci\_cp\_le\_set\_cig\_params\_test::num\_cis](structbt__hci__cp__le__set__cig__params__test.md#a50c345ef03c669f476e143728f42cd6d)

uint8\_t num\_cis

**Definition** hci\_types.h:2016

[bt\_hci\_cp\_le\_set\_cig\_params\_test::cis](structbt__hci__cp__le__set__cig__params__test.md#a5e07eb0d7d13e57be457d1b77a5dba12)

struct bt\_hci\_cis\_params\_test cis[0]

**Definition** hci\_types.h:2017

[bt\_hci\_cp\_le\_set\_cig\_params\_test::packing](structbt__hci__cp__le__set__cig__params__test.md#a7275312e8b1c8ebc2af7992f765b392c)

uint8\_t packing

**Definition** hci\_types.h:2014

[bt\_hci\_cp\_le\_set\_cig\_params\_test::c\_interval](structbt__hci__cp__le__set__cig__params__test.md#aa392cbac058beefd0e410fcc9821a0c3)

uint8\_t c\_interval[3]

**Definition** hci\_types.h:2008

[bt\_hci\_cp\_le\_set\_cig\_params\_test::iso\_interval](structbt__hci__cp__le__set__cig__params__test.md#aa77765d90fde67c52e4f2d483f0a3ee0)

uint16\_t iso\_interval

**Definition** hci\_types.h:2012

[bt\_hci\_cp\_le\_set\_cig\_params\_test::p\_ft](structbt__hci__cp__le__set__cig__params__test.md#af2ed1bf1a6beaff884c3ce3faf26bfb2)

uint8\_t p\_ft

**Definition** hci\_types.h:2011

[bt\_hci\_cp\_le\_set\_cig\_params](structbt__hci__cp__le__set__cig__params.md)

**Definition** hci\_types.h:1972

[bt\_hci\_cp\_le\_set\_cig\_params::c\_interval](structbt__hci__cp__le__set__cig__params.md#a14f5c0cf7f99ab406714501038048035)

uint8\_t c\_interval[3]

**Definition** hci\_types.h:1974

[bt\_hci\_cp\_le\_set\_cig\_params::sca](structbt__hci__cp__le__set__cig__params.md#a46a657cdfbc7a49e6761d9f18d980c2a)

uint8\_t sca

**Definition** hci\_types.h:1976

[bt\_hci\_cp\_le\_set\_cig\_params::p\_interval](structbt__hci__cp__le__set__cig__params.md#a50a260a15f3a0ceae716da6c04c5b768)

uint8\_t p\_interval[3]

**Definition** hci\_types.h:1975

[bt\_hci\_cp\_le\_set\_cig\_params::packing](structbt__hci__cp__le__set__cig__params.md#a79fc069492741f14f348650abef4c66b)

uint8\_t packing

**Definition** hci\_types.h:1977

[bt\_hci\_cp\_le\_set\_cig\_params::cig\_id](structbt__hci__cp__le__set__cig__params.md#a7dbf75c6ed92a053c4ec0d8f7268c92e)

uint8\_t cig\_id

**Definition** hci\_types.h:1973

[bt\_hci\_cp\_le\_set\_cig\_params::p\_latency](structbt__hci__cp__le__set__cig__params.md#a810822396b97d54988ec57561b4ee7d5)

uint16\_t p\_latency

**Definition** hci\_types.h:1980

[bt\_hci\_cp\_le\_set\_cig\_params::framing](structbt__hci__cp__le__set__cig__params.md#a867bf5ddbcadd27dbec2c3059d67d6d6)

uint8\_t framing

**Definition** hci\_types.h:1978

[bt\_hci\_cp\_le\_set\_cig\_params::cis](structbt__hci__cp__le__set__cig__params.md#ac922e59065920421f40468754d2ba5a2)

struct bt\_hci\_cis\_params cis[0]

**Definition** hci\_types.h:1982

[bt\_hci\_cp\_le\_set\_cig\_params::num\_cis](structbt__hci__cp__le__set__cig__params.md#adf468a8a195447a7bbed4dcd53d287f6)

uint8\_t num\_cis

**Definition** hci\_types.h:1981

[bt\_hci\_cp\_le\_set\_cig\_params::c\_latency](structbt__hci__cp__le__set__cig__params.md#afec8ebd17cc6ca5b3d13ef54f406df62)

uint16\_t c\_latency

**Definition** hci\_types.h:1979

[bt\_hci\_cp\_le\_set\_cl\_cte\_sampling\_enable](structbt__hci__cp__le__set__cl__cte__sampling__enable.md)

**Definition** hci\_types.h:1754

[bt\_hci\_cp\_le\_set\_cl\_cte\_sampling\_enable::max\_sampled\_cte](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#a38e770b3e5f9d7d63a564dfa7c80451f)

uint8\_t max\_sampled\_cte

**Definition** hci\_types.h:1758

[bt\_hci\_cp\_le\_set\_cl\_cte\_sampling\_enable::switch\_pattern\_len](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#a4f52142ef1d2365859189b7a2abe050b)

uint8\_t switch\_pattern\_len

**Definition** hci\_types.h:1759

[bt\_hci\_cp\_le\_set\_cl\_cte\_sampling\_enable::ant\_ids](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#a67bb2dbfe1707f76a5e211e007459c22)

uint8\_t ant\_ids[0]

**Definition** hci\_types.h:1760

[bt\_hci\_cp\_le\_set\_cl\_cte\_sampling\_enable::sync\_handle](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#a91d3458e2049ab434e220403b7ba235d)

uint16\_t sync\_handle

**Definition** hci\_types.h:1755

[bt\_hci\_cp\_le\_set\_cl\_cte\_sampling\_enable::slot\_durations](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#aaaed0fc39158c653041fd760a00cecec)

uint8\_t slot\_durations

**Definition** hci\_types.h:1757

[bt\_hci\_cp\_le\_set\_cl\_cte\_sampling\_enable::sampling\_enable](structbt__hci__cp__le__set__cl__cte__sampling__enable.md#aca9e1316c716525f00308f64b8c6cec4)

uint8\_t sampling\_enable

**Definition** hci\_types.h:1756

[bt\_hci\_cp\_le\_set\_cl\_cte\_tx\_enable](structbt__hci__cp__le__set__cl__cte__tx__enable.md)

**Definition** hci\_types.h:1741

[bt\_hci\_cp\_le\_set\_cl\_cte\_tx\_enable::cte\_enable](structbt__hci__cp__le__set__cl__cte__tx__enable.md#a3530dae940caefeafb9de4ac761ee080)

uint8\_t cte\_enable

**Definition** hci\_types.h:1743

[bt\_hci\_cp\_le\_set\_cl\_cte\_tx\_enable::handle](structbt__hci__cp__le__set__cl__cte__tx__enable.md#a55125c808a888eeecfee9410bcb55859)

uint8\_t handle

**Definition** hci\_types.h:1742

[bt\_hci\_cp\_le\_set\_cl\_cte\_tx\_params](structbt__hci__cp__le__set__cl__cte__tx__params.md)

**Definition** hci\_types.h:1731

[bt\_hci\_cp\_le\_set\_cl\_cte\_tx\_params::ant\_ids](structbt__hci__cp__le__set__cl__cte__tx__params.md#a27a228653ea560a77369a6b1829a8a9d)

uint8\_t ant\_ids[0]

**Definition** hci\_types.h:1737

[bt\_hci\_cp\_le\_set\_cl\_cte\_tx\_params::switch\_pattern\_len](structbt__hci__cp__le__set__cl__cte__tx__params.md#a8208571653e444221648d2a884eabfae)

uint8\_t switch\_pattern\_len

**Definition** hci\_types.h:1736

[bt\_hci\_cp\_le\_set\_cl\_cte\_tx\_params::cte\_type](structbt__hci__cp__le__set__cl__cte__tx__params.md#a869192cea35f4cd57984614e4c8bb5a5)

uint8\_t cte\_type

**Definition** hci\_types.h:1734

[bt\_hci\_cp\_le\_set\_cl\_cte\_tx\_params::handle](structbt__hci__cp__le__set__cl__cte__tx__params.md#a8f20e6e3bb408551d6cc494ad19391c4)

uint8\_t handle

**Definition** hci\_types.h:1732

[bt\_hci\_cp\_le\_set\_cl\_cte\_tx\_params::cte\_len](structbt__hci__cp__le__set__cl__cte__tx__params.md#ab5c4742cf37cf7e802423beb4a9b4fa2)

uint8\_t cte\_len

**Definition** hci\_types.h:1733

[bt\_hci\_cp\_le\_set\_cl\_cte\_tx\_params::cte\_count](structbt__hci__cp__le__set__cl__cte__tx__params.md#af5e82bf572b385904a0f24219bdc72ca)

uint8\_t cte\_count

**Definition** hci\_types.h:1735

[bt\_hci\_cp\_le\_set\_conn\_cte\_rx\_params](structbt__hci__cp__le__set__conn__cte__rx__params.md)

**Definition** hci\_types.h:1769

[bt\_hci\_cp\_le\_set\_conn\_cte\_rx\_params::ant\_ids](structbt__hci__cp__le__set__conn__cte__rx__params.md#a519c37f5d797d8ddac5ba9be7c14b9f9)

uint8\_t ant\_ids[0]

**Definition** hci\_types.h:1774

[bt\_hci\_cp\_le\_set\_conn\_cte\_rx\_params::sampling\_enable](structbt__hci__cp__le__set__conn__cte__rx__params.md#a615cae822878cf1344a990e30fa80044)

uint8\_t sampling\_enable

**Definition** hci\_types.h:1771

[bt\_hci\_cp\_le\_set\_conn\_cte\_rx\_params::slot\_durations](structbt__hci__cp__le__set__conn__cte__rx__params.md#a6246d492b94c67af9604b89912dbdb61)

uint8\_t slot\_durations

**Definition** hci\_types.h:1772

[bt\_hci\_cp\_le\_set\_conn\_cte\_rx\_params::handle](structbt__hci__cp__le__set__conn__cte__rx__params.md#a76968866cf5c6ef4bfb983cb6b68a827)

uint16\_t handle

**Definition** hci\_types.h:1770

[bt\_hci\_cp\_le\_set\_conn\_cte\_rx\_params::switch\_pattern\_len](structbt__hci__cp__le__set__conn__cte__rx__params.md#a89194a5b9e6c7f0c176c915e451911df)

uint8\_t switch\_pattern\_len

**Definition** hci\_types.h:1773

[bt\_hci\_cp\_le\_set\_conn\_cte\_tx\_params](structbt__hci__cp__le__set__conn__cte__tx__params.md)

**Definition** hci\_types.h:1790

[bt\_hci\_cp\_le\_set\_conn\_cte\_tx\_params::switch\_pattern\_len](structbt__hci__cp__le__set__conn__cte__tx__params.md#a8f0e5ee74662056f00eaa3a8c72f6fc4)

uint8\_t switch\_pattern\_len

**Definition** hci\_types.h:1793

[bt\_hci\_cp\_le\_set\_conn\_cte\_tx\_params::cte\_types](structbt__hci__cp__le__set__conn__cte__tx__params.md#ab47f852b476ac2c35fc0631180e19fb4)

uint8\_t cte\_types

**Definition** hci\_types.h:1792

[bt\_hci\_cp\_le\_set\_conn\_cte\_tx\_params::ant\_ids](structbt__hci__cp__le__set__conn__cte__tx__params.md#abff85d652b3b2fd55ad78e53887cd7ce)

uint8\_t ant\_ids[0]

**Definition** hci\_types.h:1794

[bt\_hci\_cp\_le\_set\_conn\_cte\_tx\_params::handle](structbt__hci__cp__le__set__conn__cte__tx__params.md#ae0a482982d804ffd7d16ea2b413e538d)

uint16\_t handle

**Definition** hci\_types.h:1791

[bt\_hci\_cp\_le\_set\_data\_len](structbt__hci__cp__le__set__data__len.md)

**Definition** hci\_types.h:1182

[bt\_hci\_cp\_le\_set\_data\_len::tx\_time](structbt__hci__cp__le__set__data__len.md#a15285a4e8bf8e359bb326de4b30ba8f1)

uint16\_t tx\_time

**Definition** hci\_types.h:1185

[bt\_hci\_cp\_le\_set\_data\_len::handle](structbt__hci__cp__le__set__data__len.md#a874869090428a7f380c5466353573eba)

uint16\_t handle

**Definition** hci\_types.h:1183

[bt\_hci\_cp\_le\_set\_data\_len::tx\_octets](structbt__hci__cp__le__set__data__len.md#ac579e84a004a09813bbe0ed61db11931)

uint16\_t tx\_octets

**Definition** hci\_types.h:1184

[bt\_hci\_cp\_le\_set\_default\_phy](structbt__hci__cp__le__set__default__phy.md)

**Definition** hci\_types.h:1307

[bt\_hci\_cp\_le\_set\_default\_phy::tx\_phys](structbt__hci__cp__le__set__default__phy.md#a0c4ab2d91021466fd136af3a0b6bde2a)

uint8\_t tx\_phys

**Definition** hci\_types.h:1309

[bt\_hci\_cp\_le\_set\_default\_phy::rx\_phys](structbt__hci__cp__le__set__default__phy.md#a4c3410f2ce9fb2817bc5d143908936d1)

uint8\_t rx\_phys

**Definition** hci\_types.h:1310

[bt\_hci\_cp\_le\_set\_default\_phy::all\_phys](structbt__hci__cp__le__set__default__phy.md#abe1d83e372e874739588812040d0b540)

uint8\_t all\_phys

**Definition** hci\_types.h:1308

[bt\_hci\_cp\_le\_set\_event\_mask](structbt__hci__cp__le__set__event__mask.md)

**Definition** hci\_types.h:899

[bt\_hci\_cp\_le\_set\_event\_mask::events](structbt__hci__cp__le__set__event__mask.md#af7de4823aca253f15e57f54ee9b3879e)

uint8\_t events[8]

**Definition** hci\_types.h:900

[bt\_hci\_cp\_le\_set\_ext\_adv\_data](structbt__hci__cp__le__set__ext__adv__data.md)

**Definition** hci\_types.h:1413

[bt\_hci\_cp\_le\_set\_ext\_adv\_data::data](structbt__hci__cp__le__set__ext__adv__data.md#a7d7df52500eb53a64b6ba5e62f6cf14f)

uint8\_t data[0]

**Definition** hci\_types.h:1418

[bt\_hci\_cp\_le\_set\_ext\_adv\_data::handle](structbt__hci__cp__le__set__ext__adv__data.md#a803bb793eefcc714c6c4034123a2e487)

uint8\_t handle

**Definition** hci\_types.h:1414

[bt\_hci\_cp\_le\_set\_ext\_adv\_data::op](structbt__hci__cp__le__set__ext__adv__data.md#ac5eaa1834f82024055923d08a3bef6b3)

uint8\_t op

**Definition** hci\_types.h:1415

[bt\_hci\_cp\_le\_set\_ext\_adv\_data::len](structbt__hci__cp__le__set__ext__adv__data.md#aea3055cc7ffbaf4cd14996d885e21ba3)

uint8\_t len

**Definition** hci\_types.h:1417

[bt\_hci\_cp\_le\_set\_ext\_adv\_data::frag\_pref](structbt__hci__cp__le__set__ext__adv__data.md#af9eef9f59bfec5867ea36bdf33e3a9b1)

uint8\_t frag\_pref

**Definition** hci\_types.h:1416

[bt\_hci\_cp\_le\_set\_ext\_adv\_enable](structbt__hci__cp__le__set__ext__adv__enable.md)

**Definition** hci\_types.h:1437

[bt\_hci\_cp\_le\_set\_ext\_adv\_enable::s](structbt__hci__cp__le__set__ext__adv__enable.md#a04911e19f3b2f0079d4e12980d11157f)

struct bt\_hci\_ext\_adv\_set s[0]

**Definition** hci\_types.h:1440

[bt\_hci\_cp\_le\_set\_ext\_adv\_enable::set\_num](structbt__hci__cp__le__set__ext__adv__enable.md#a06088af8b432ac134943d9ebb7778ac7)

uint8\_t set\_num

**Definition** hci\_types.h:1439

[bt\_hci\_cp\_le\_set\_ext\_adv\_enable::enable](structbt__hci__cp__le__set__ext__adv__enable.md#ab7148b47bf052d8cba1f6bf3385051c8)

uint8\_t enable

**Definition** hci\_types.h:1438

[bt\_hci\_cp\_le\_set\_ext\_adv\_param](structbt__hci__cp__le__set__ext__adv__param.md)

**Definition** hci\_types.h:1380

[bt\_hci\_cp\_le\_set\_ext\_adv\_param::prim\_adv\_phy](structbt__hci__cp__le__set__ext__adv__param.md#a048874197ccbdbc626f0563be5c41ec7)

uint8\_t prim\_adv\_phy

**Definition** hci\_types.h:1390

[bt\_hci\_cp\_le\_set\_ext\_adv\_param::prim\_max\_interval](structbt__hci__cp__le__set__ext__adv__param.md#a08aa741a56e825a11424bf024ac65e14)

uint8\_t prim\_max\_interval[3]

**Definition** hci\_types.h:1384

[bt\_hci\_cp\_le\_set\_ext\_adv\_param::filter\_policy](structbt__hci__cp__le__set__ext__adv__param.md#a29a62f8989f89b014cadbad9b94e996a)

uint8\_t filter\_policy

**Definition** hci\_types.h:1388

[bt\_hci\_cp\_le\_set\_ext\_adv\_param::own\_addr\_type](structbt__hci__cp__le__set__ext__adv__param.md#a3594f7337ccd739f59ac7845757de0e8)

uint8\_t own\_addr\_type

**Definition** hci\_types.h:1386

[bt\_hci\_cp\_le\_set\_ext\_adv\_param::props](structbt__hci__cp__le__set__ext__adv__param.md#a4af102ae90ca6917b3134491c5ff079f)

uint16\_t props

**Definition** hci\_types.h:1382

[bt\_hci\_cp\_le\_set\_ext\_adv\_param::sec\_adv\_max\_skip](structbt__hci__cp__le__set__ext__adv__param.md#a5793c6afe545290a1e792bcc73585b72)

uint8\_t sec\_adv\_max\_skip

**Definition** hci\_types.h:1391

[bt\_hci\_cp\_le\_set\_ext\_adv\_param::tx\_power](structbt__hci__cp__le__set__ext__adv__param.md#a5f7f3e477b5b0b8122b85f3e53dd7878)

int8\_t tx\_power

**Definition** hci\_types.h:1389

[bt\_hci\_cp\_le\_set\_ext\_adv\_param::handle](structbt__hci__cp__le__set__ext__adv__param.md#a65fe609dde9515212659087a024e7c65)

uint8\_t handle

**Definition** hci\_types.h:1381

[bt\_hci\_cp\_le\_set\_ext\_adv\_param::peer\_addr](structbt__hci__cp__le__set__ext__adv__param.md#a819e599df4025036fab2dabd7c61ea37)

bt\_addr\_le\_t peer\_addr

**Definition** hci\_types.h:1387

[bt\_hci\_cp\_le\_set\_ext\_adv\_param::prim\_min\_interval](structbt__hci__cp__le__set__ext__adv__param.md#ab5a80941b3d832c2906daed8cf069a02)

uint8\_t prim\_min\_interval[3]

**Definition** hci\_types.h:1383

[bt\_hci\_cp\_le\_set\_ext\_adv\_param::sec\_adv\_phy](structbt__hci__cp__le__set__ext__adv__param.md#abc82ba984647eb00bc490c01ce746a15)

uint8\_t sec\_adv\_phy

**Definition** hci\_types.h:1392

[bt\_hci\_cp\_le\_set\_ext\_adv\_param::prim\_channel\_map](structbt__hci__cp__le__set__ext__adv__param.md#ad7a0b9028bcdb57a9011d4677412aed5)

uint8\_t prim\_channel\_map

**Definition** hci\_types.h:1385

[bt\_hci\_cp\_le\_set\_ext\_adv\_param::scan\_req\_notify\_enable](structbt__hci__cp__le__set__ext__adv__param.md#ae694df46b1db4b029d1e177768b3821f)

uint8\_t scan\_req\_notify\_enable

**Definition** hci\_types.h:1394

[bt\_hci\_cp\_le\_set\_ext\_adv\_param::sid](structbt__hci__cp__le__set__ext__adv__param.md#af8bc3509fdd5e89c27db466727fe1cd9)

uint8\_t sid

**Definition** hci\_types.h:1393

[bt\_hci\_cp\_le\_set\_ext\_scan\_enable](structbt__hci__cp__le__set__ext__scan__enable.md)

**Definition** hci\_types.h:1519

[bt\_hci\_cp\_le\_set\_ext\_scan\_enable::enable](structbt__hci__cp__le__set__ext__scan__enable.md#a922d0c5a7ccb6c1e1864f662227b8307)

uint8\_t enable

**Definition** hci\_types.h:1520

[bt\_hci\_cp\_le\_set\_ext\_scan\_enable::filter\_dup](structbt__hci__cp__le__set__ext__scan__enable.md#aa5b0939838ab13eb8299f4a4b2fd3f14)

uint8\_t filter\_dup

**Definition** hci\_types.h:1521

[bt\_hci\_cp\_le\_set\_ext\_scan\_enable::period](structbt__hci__cp__le__set__ext__scan__enable.md#aa60c8ade7047dcd202d83cfc3f18ada2)

uint16\_t period

**Definition** hci\_types.h:1523

[bt\_hci\_cp\_le\_set\_ext\_scan\_enable::duration](structbt__hci__cp__le__set__ext__scan__enable.md#adcd5e00a240f3e7395d0d25994b4013a)

uint16\_t duration

**Definition** hci\_types.h:1522

[bt\_hci\_cp\_le\_set\_ext\_scan\_param](structbt__hci__cp__le__set__ext__scan__param.md)

**Definition** hci\_types.h:1508

[bt\_hci\_cp\_le\_set\_ext\_scan\_param::own\_addr\_type](structbt__hci__cp__le__set__ext__scan__param.md#a3418aa8dbdb8062ee452f5756eb9f30c)

uint8\_t own\_addr\_type

**Definition** hci\_types.h:1509

[bt\_hci\_cp\_le\_set\_ext\_scan\_param::filter\_policy](structbt__hci__cp__le__set__ext__scan__param.md#a47f6cf7f83451dcc2feac1a8d5837ad8)

uint8\_t filter\_policy

**Definition** hci\_types.h:1510

[bt\_hci\_cp\_le\_set\_ext\_scan\_param::phys](structbt__hci__cp__le__set__ext__scan__param.md#a6c38b7d074eb3c0cf5c301eb6c03b60c)

uint8\_t phys

**Definition** hci\_types.h:1511

[bt\_hci\_cp\_le\_set\_ext\_scan\_param::p](structbt__hci__cp__le__set__ext__scan__param.md#ab4eab9a52dca01bc19b35607d6ec5d36)

struct bt\_hci\_ext\_scan\_phy p[0]

**Definition** hci\_types.h:1512

[bt\_hci\_cp\_le\_set\_ext\_scan\_rsp\_data](structbt__hci__cp__le__set__ext__scan__rsp__data.md)

**Definition** hci\_types.h:1422

[bt\_hci\_cp\_le\_set\_ext\_scan\_rsp\_data::op](structbt__hci__cp__le__set__ext__scan__rsp__data.md#a3323a0844680b71cb8aedffa034837d7)

uint8\_t op

**Definition** hci\_types.h:1424

[bt\_hci\_cp\_le\_set\_ext\_scan\_rsp\_data::len](structbt__hci__cp__le__set__ext__scan__rsp__data.md#a6024eac85f600ed3b7051a84b91bdcfa)

uint8\_t len

**Definition** hci\_types.h:1426

[bt\_hci\_cp\_le\_set\_ext\_scan\_rsp\_data::handle](structbt__hci__cp__le__set__ext__scan__rsp__data.md#a8cf0624b9968686c7f6765ee25e11c90)

uint8\_t handle

**Definition** hci\_types.h:1423

[bt\_hci\_cp\_le\_set\_ext\_scan\_rsp\_data::data](structbt__hci__cp__le__set__ext__scan__rsp__data.md#ab086720e1a22523ba155cb238ad75197)

uint8\_t data[0]

**Definition** hci\_types.h:1427

[bt\_hci\_cp\_le\_set\_ext\_scan\_rsp\_data::frag\_pref](structbt__hci__cp__le__set__ext__scan__rsp__data.md#ac4e1691926df370b290c9e6d866d310d)

uint8\_t frag\_pref

**Definition** hci\_types.h:1425

[bt\_hci\_cp\_le\_set\_host\_chan\_classif](structbt__hci__cp__le__set__host__chan__classif.md)

**Definition** hci\_types.h:1061

[bt\_hci\_cp\_le\_set\_host\_chan\_classif::ch\_map](structbt__hci__cp__le__set__host__chan__classif.md#a0fb81bcdebe7da416cc4317486106752)

uint8\_t ch\_map[5]

**Definition** hci\_types.h:1062

[bt\_hci\_cp\_le\_set\_host\_feature](structbt__hci__cp__le__set__host__feature.md)

**Definition** hci\_types.h:2213

[bt\_hci\_cp\_le\_set\_host\_feature::bit\_value](structbt__hci__cp__le__set__host__feature.md#a78b67164bce232466ab348f8937682c3)

uint8\_t bit\_value

**Definition** hci\_types.h:2215

[bt\_hci\_cp\_le\_set\_host\_feature::bit\_number](structbt__hci__cp__le__set__host__feature.md#adcca35df216061ea08bd27e10fefd5e9)

uint8\_t bit\_number

**Definition** hci\_types.h:2214

[bt\_hci\_cp\_le\_set\_pawr\_response\_data](structbt__hci__cp__le__set__pawr__response__data.md)

**Definition** hci\_types.h:1574

[bt\_hci\_cp\_le\_set\_pawr\_response\_data::sync\_handle](structbt__hci__cp__le__set__pawr__response__data.md#a034afaaacf4b2168b9cd54cfde583b5c)

uint16\_t sync\_handle

**Definition** hci\_types.h:1575

[bt\_hci\_cp\_le\_set\_pawr\_response\_data::response\_data](structbt__hci__cp__le__set__pawr__response__data.md#a39cbc74ab95881b6dde8fa377d2951e5)

uint8\_t response\_data[0]

**Definition** hci\_types.h:1581

[bt\_hci\_cp\_le\_set\_pawr\_response\_data::response\_slot](structbt__hci__cp__le__set__pawr__response__data.md#a4356344510833196533bb9582f6fe18a)

uint8\_t response\_slot

**Definition** hci\_types.h:1579

[bt\_hci\_cp\_le\_set\_pawr\_response\_data::request\_subevent](structbt__hci__cp__le__set__pawr__response__data.md#a675a223891b28f06e78df6223439dc28)

uint8\_t request\_subevent

**Definition** hci\_types.h:1577

[bt\_hci\_cp\_le\_set\_pawr\_response\_data::response\_data\_length](structbt__hci__cp__le__set__pawr__response__data.md#a8c546fa3c6d969d44c54926330e5cf85)

uint8\_t response\_data\_length

**Definition** hci\_types.h:1580

[bt\_hci\_cp\_le\_set\_pawr\_response\_data::response\_subevent](structbt__hci__cp__le__set__pawr__response__data.md#aaf2e0eb3b491b5ccd15ba5259fd900c7)

uint8\_t response\_subevent

**Definition** hci\_types.h:1578

[bt\_hci\_cp\_le\_set\_pawr\_response\_data::request\_event](structbt__hci__cp__le__set__pawr__response__data.md#aaf5c337af93f13e243451b46a94ffb77)

uint16\_t request\_event

**Definition** hci\_types.h:1576

[bt\_hci\_cp\_le\_set\_pawr\_subevent\_data\_element](structbt__hci__cp__le__set__pawr__subevent__data__element.md)

**Definition** hci\_types.h:1558

[bt\_hci\_cp\_le\_set\_pawr\_subevent\_data\_element::response\_slot\_start](structbt__hci__cp__le__set__pawr__subevent__data__element.md#a90178bcd86c1bad0a768f391ce11613f)

uint8\_t response\_slot\_start

**Definition** hci\_types.h:1560

[bt\_hci\_cp\_le\_set\_pawr\_subevent\_data\_element::subevent\_data](structbt__hci__cp__le__set__pawr__subevent__data__element.md#a91c975189e409b733ac9a4af5763b12a)

uint8\_t subevent\_data[0]

**Definition** hci\_types.h:1563

[bt\_hci\_cp\_le\_set\_pawr\_subevent\_data\_element::subevent](structbt__hci__cp__le__set__pawr__subevent__data__element.md#abf33f93f0f1ddf3532c6cae13483ec1e)

uint8\_t subevent

**Definition** hci\_types.h:1559

[bt\_hci\_cp\_le\_set\_pawr\_subevent\_data\_element::subevent\_data\_length](structbt__hci__cp__le__set__pawr__subevent__data__element.md#ace5860dfa0f628eaed2b68b171d875da)

uint8\_t subevent\_data\_length

**Definition** hci\_types.h:1562

[bt\_hci\_cp\_le\_set\_pawr\_subevent\_data\_element::response\_slot\_count](structbt__hci__cp__le__set__pawr__subevent__data__element.md#ad8da1cc672eedf8be8cfc7d0d7ec1b41)

uint8\_t response\_slot\_count

**Definition** hci\_types.h:1561

[bt\_hci\_cp\_le\_set\_pawr\_subevent\_data](structbt__hci__cp__le__set__pawr__subevent__data.md)

**Definition** hci\_types.h:1566

[bt\_hci\_cp\_le\_set\_pawr\_subevent\_data::adv\_handle](structbt__hci__cp__le__set__pawr__subevent__data.md#a47d84125d15cce1fc969db3e5caa07e1)

uint8\_t adv\_handle

**Definition** hci\_types.h:1567

[bt\_hci\_cp\_le\_set\_pawr\_subevent\_data::num\_subevents](structbt__hci__cp__le__set__pawr__subevent__data.md#a9397eebd6771ad159d1bdae0d59e5f46)

uint8\_t num\_subevents

**Definition** hci\_types.h:1568

[bt\_hci\_cp\_le\_set\_pawr\_subevent\_data::subevents](structbt__hci__cp__le__set__pawr__subevent__data.md#aa932c1f19de96f89a79bbcb3ecbc1f5d)

struct bt\_hci\_cp\_le\_set\_pawr\_subevent\_data\_element subevents[0]

**Definition** hci\_types.h:1569

[bt\_hci\_cp\_le\_set\_pawr\_sync\_subevent](structbt__hci__cp__le__set__pawr__sync__subevent.md)

**Definition** hci\_types.h:1585

[bt\_hci\_cp\_le\_set\_pawr\_sync\_subevent::num\_subevents](structbt__hci__cp__le__set__pawr__sync__subevent.md#a2648ff50e0bad585e77e6f340836555a)

uint8\_t num\_subevents

**Definition** hci\_types.h:1588

[bt\_hci\_cp\_le\_set\_pawr\_sync\_subevent::sync\_handle](structbt__hci__cp__le__set__pawr__sync__subevent.md#a89f3092c2dd561e5469bb5bf57a06172)

uint16\_t sync\_handle

**Definition** hci\_types.h:1586

[bt\_hci\_cp\_le\_set\_pawr\_sync\_subevent::subevents](structbt__hci__cp__le__set__pawr__sync__subevent.md#a9a362ae841e5305b3985c4b2d88c6753)

uint8\_t subevents[0]

**Definition** hci\_types.h:1589

[bt\_hci\_cp\_le\_set\_pawr\_sync\_subevent::periodic\_adv\_properties](structbt__hci__cp__le__set__pawr__sync__subevent.md#aa73b23816e6c2c6546de15f6f6caff27)

uint16\_t periodic\_adv\_properties

**Definition** hci\_types.h:1587

[bt\_hci\_cp\_le\_set\_per\_adv\_data](structbt__hci__cp__le__set__per__adv__data.md)

**Definition** hci\_types.h:1481

[bt\_hci\_cp\_le\_set\_per\_adv\_data::handle](structbt__hci__cp__le__set__per__adv__data.md#a93cbb46ce6664880487e009a0b47af02)

uint8\_t handle

**Definition** hci\_types.h:1482

[bt\_hci\_cp\_le\_set\_per\_adv\_data::op](structbt__hci__cp__le__set__per__adv__data.md#aac34596f0970c976c4ef71250d326c2c)

uint8\_t op

**Definition** hci\_types.h:1483

[bt\_hci\_cp\_le\_set\_per\_adv\_data::data](structbt__hci__cp__le__set__per__adv__data.md#adaf581f8db6aafb4dc5df669df7ad26d)

uint8\_t data[0]

**Definition** hci\_types.h:1485

[bt\_hci\_cp\_le\_set\_per\_adv\_data::len](structbt__hci__cp__le__set__per__adv__data.md#ae6ee631a153cb6fed88695e599f63e91)

uint8\_t len

**Definition** hci\_types.h:1484

[bt\_hci\_cp\_le\_set\_per\_adv\_enable](structbt__hci__cp__le__set__per__adv__enable.md)

**Definition** hci\_types.h:1492

[bt\_hci\_cp\_le\_set\_per\_adv\_enable::handle](structbt__hci__cp__le__set__per__adv__enable.md#a998f4e38a56f771f234ce099b4528a3d)

uint8\_t handle

**Definition** hci\_types.h:1494

[bt\_hci\_cp\_le\_set\_per\_adv\_enable::enable](structbt__hci__cp__le__set__per__adv__enable.md#afff649b908264c617b249bcfbebadd53)

uint8\_t enable

**Definition** hci\_types.h:1493

[bt\_hci\_cp\_le\_set\_per\_adv\_param\_v2](structbt__hci__cp__le__set__per__adv__param__v2.md)

**Definition** hci\_types.h:1594

[bt\_hci\_cp\_le\_set\_per\_adv\_param\_v2::num\_response\_slots](structbt__hci__cp__le__set__per__adv__param__v2.md#a2483eb4457f9dc22ff8473175662e260)

uint8\_t num\_response\_slots

**Definition** hci\_types.h:1603

[bt\_hci\_cp\_le\_set\_per\_adv\_param\_v2::response\_slot\_spacing](structbt__hci__cp__le__set__per__adv__param__v2.md#a35fcc697e60d3c398f03be7503f611bd)

uint8\_t response\_slot\_spacing

**Definition** hci\_types.h:1602

[bt\_hci\_cp\_le\_set\_per\_adv\_param\_v2::subevent\_interval](structbt__hci__cp__le__set__per__adv__param__v2.md#a79dfc3b13068d9c51f0a756f025aaeba)

uint8\_t subevent\_interval

**Definition** hci\_types.h:1600

[bt\_hci\_cp\_le\_set\_per\_adv\_param\_v2::num\_subevents](structbt__hci__cp__le__set__per__adv__param__v2.md#a7bea764aa5d21e03946804566b1f9869)

uint8\_t num\_subevents

**Definition** hci\_types.h:1599

[bt\_hci\_cp\_le\_set\_per\_adv\_param\_v2::max\_interval](structbt__hci__cp__le__set__per__adv__param__v2.md#acc9718286ab0847a3444d3fc2d3c93bc)

uint16\_t max\_interval

**Definition** hci\_types.h:1597

[bt\_hci\_cp\_le\_set\_per\_adv\_param\_v2::response\_slot\_delay](structbt__hci__cp__le__set__per__adv__param__v2.md#acdeb503c0a13291158ad389c9f6ac206)

uint8\_t response\_slot\_delay

**Definition** hci\_types.h:1601

[bt\_hci\_cp\_le\_set\_per\_adv\_param\_v2::props](structbt__hci__cp__le__set__per__adv__param__v2.md#ad2d658bb0be35aee6b5c133fece89068)

uint16\_t props

**Definition** hci\_types.h:1598

[bt\_hci\_cp\_le\_set\_per\_adv\_param\_v2::min\_interval](structbt__hci__cp__le__set__per__adv__param__v2.md#ae36e28210a515f73648e6f8b3984fb55)

uint16\_t min\_interval

**Definition** hci\_types.h:1596

[bt\_hci\_cp\_le\_set\_per\_adv\_param\_v2::handle](structbt__hci__cp__le__set__per__adv__param__v2.md#aee1088b46914c8e26d9e97ce573291c6)

uint8\_t handle

**Definition** hci\_types.h:1595

[bt\_hci\_cp\_le\_set\_per\_adv\_param](structbt__hci__cp__le__set__per__adv__param.md)

**Definition** hci\_types.h:1466

[bt\_hci\_cp\_le\_set\_per\_adv\_param::max\_interval](structbt__hci__cp__le__set__per__adv__param.md#a1a2a69ea6e310710892184ced472eb8a)

uint16\_t max\_interval

**Definition** hci\_types.h:1469

[bt\_hci\_cp\_le\_set\_per\_adv\_param::handle](structbt__hci__cp__le__set__per__adv__param.md#a2b61031952b3893add7677d3802e368b)

uint8\_t handle

**Definition** hci\_types.h:1467

[bt\_hci\_cp\_le\_set\_per\_adv\_param::props](structbt__hci__cp__le__set__per__adv__param.md#a879ea10e1ab217b4aa49dfcf3b394691)

uint16\_t props

**Definition** hci\_types.h:1470

[bt\_hci\_cp\_le\_set\_per\_adv\_param::min\_interval](structbt__hci__cp__le__set__per__adv__param.md#af01696ef6bf02e7db37d45a0c9852ef5)

uint16\_t min\_interval

**Definition** hci\_types.h:1468

[bt\_hci\_cp\_le\_set\_per\_adv\_recv\_enable](structbt__hci__cp__le__set__per__adv__recv__enable.md)

**Definition** hci\_types.h:1858

[bt\_hci\_cp\_le\_set\_per\_adv\_recv\_enable::handle](structbt__hci__cp__le__set__per__adv__recv__enable.md#a1e626eecf1d3f0820c3b2a13fd84b92f)

uint16\_t handle

**Definition** hci\_types.h:1859

[bt\_hci\_cp\_le\_set\_per\_adv\_recv\_enable::enable](structbt__hci__cp__le__set__per__adv__recv__enable.md#a2187ec96822726daa5e43e910cc41cc3)

uint8\_t enable

**Definition** hci\_types.h:1860

[bt\_hci\_cp\_le\_set\_phy](structbt__hci__cp__le__set__phy.md)

**Definition** hci\_types.h:1318

[bt\_hci\_cp\_le\_set\_phy::tx\_phys](structbt__hci__cp__le__set__phy.md#a06880062ff486b532ebeb789adb57d1e)

uint8\_t tx\_phys

**Definition** hci\_types.h:1321

[bt\_hci\_cp\_le\_set\_phy::phy\_opts](structbt__hci__cp__le__set__phy.md#a458ab90f83b60fafa66167f474c0800d)

uint16\_t phy\_opts

**Definition** hci\_types.h:1323

[bt\_hci\_cp\_le\_set\_phy::rx\_phys](structbt__hci__cp__le__set__phy.md#ab30eb68920a0578b16794250e592b12a)

uint8\_t rx\_phys

**Definition** hci\_types.h:1322

[bt\_hci\_cp\_le\_set\_phy::handle](structbt__hci__cp__le__set__phy.md#ad0759eea02017674459d4ce0af0e526e)

uint16\_t handle

**Definition** hci\_types.h:1319

[bt\_hci\_cp\_le\_set\_phy::all\_phys](structbt__hci__cp__le__set__phy.md#afb8d056dc7d8824eec0ef16fdf9ce924)

uint8\_t all\_phys

**Definition** hci\_types.h:1320

[bt\_hci\_cp\_le\_set\_privacy\_mode](structbt__hci__cp__le__set__privacy__mode.md)

**Definition** hci\_types.h:1683

[bt\_hci\_cp\_le\_set\_privacy\_mode::id\_addr](structbt__hci__cp__le__set__privacy__mode.md#a404cc9f04cd11924445f12eb4471ef2e)

bt\_addr\_le\_t id\_addr

**Definition** hci\_types.h:1684

[bt\_hci\_cp\_le\_set\_privacy\_mode::mode](structbt__hci__cp__le__set__privacy__mode.md#a8ca00418b0638bba6ef586d6cbf253a5)

uint8\_t mode

**Definition** hci\_types.h:1685

[bt\_hci\_cp\_le\_set\_random\_address](structbt__hci__cp__le__set__random__address.md)

**Definition** hci\_types.h:917

[bt\_hci\_cp\_le\_set\_random\_address::bdaddr](structbt__hci__cp__le__set__random__address.md#a919ef74473f4f86d00595ec8606789d0)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:918

[bt\_hci\_cp\_le\_set\_rpa\_timeout](structbt__hci__cp__le__set__rpa__timeout.md)

**Definition** hci\_types.h:1271

[bt\_hci\_cp\_le\_set\_rpa\_timeout::rpa\_timeout](structbt__hci__cp__le__set__rpa__timeout.md#a6b1befe9d2131a889de17339ec1941fa)

uint16\_t rpa\_timeout

**Definition** hci\_types.h:1272

[bt\_hci\_cp\_le\_set\_scan\_enable](structbt__hci__cp__le__set__scan__enable.md)

**Definition** hci\_types.h:1005

[bt\_hci\_cp\_le\_set\_scan\_enable::enable](structbt__hci__cp__le__set__scan__enable.md#a5e429a0b11be1493515803a360932b06)

uint8\_t enable

**Definition** hci\_types.h:1006

[bt\_hci\_cp\_le\_set\_scan\_enable::filter\_dup](structbt__hci__cp__le__set__scan__enable.md#a77b0f05c0e76681ed633bd42b3f21811)

uint8\_t filter\_dup

**Definition** hci\_types.h:1007

[bt\_hci\_cp\_le\_set\_scan\_param](structbt__hci__cp__le__set__scan__param.md)

**Definition** hci\_types.h:989

[bt\_hci\_cp\_le\_set\_scan\_param::window](structbt__hci__cp__le__set__scan__param.md#a3b5b4767092fc69a63d2219d60722407)

uint16\_t window

**Definition** hci\_types.h:992

[bt\_hci\_cp\_le\_set\_scan\_param::addr\_type](structbt__hci__cp__le__set__scan__param.md#a694c74a6fc95f767d2e89e6596d51e98)

uint8\_t addr\_type

**Definition** hci\_types.h:993

[bt\_hci\_cp\_le\_set\_scan\_param::filter\_policy](structbt__hci__cp__le__set__scan__param.md#ab7a268e17a5d564d475ff9dee5e6e14b)

uint8\_t filter\_policy

**Definition** hci\_types.h:994

[bt\_hci\_cp\_le\_set\_scan\_param::scan\_type](structbt__hci__cp__le__set__scan__param.md#ad19a479cc3c27ab24286b537b646261e)

uint8\_t scan\_type

**Definition** hci\_types.h:990

[bt\_hci\_cp\_le\_set\_scan\_param::interval](structbt__hci__cp__le__set__scan__param.md#adcd8be074a8b19e0e7d02c4ea8209c93)

uint16\_t interval

**Definition** hci\_types.h:991

[bt\_hci\_cp\_le\_set\_scan\_rsp\_data](structbt__hci__cp__le__set__scan__rsp__data.md)

**Definition** hci\_types.h:966

[bt\_hci\_cp\_le\_set\_scan\_rsp\_data::len](structbt__hci__cp__le__set__scan__rsp__data.md#a0fe51008184419c9560bb5d8f287d8be)

uint8\_t len

**Definition** hci\_types.h:967

[bt\_hci\_cp\_le\_set\_scan\_rsp\_data::data](structbt__hci__cp__le__set__scan__rsp__data.md#aa719449dc2b85f094081d66398b72c7d)

uint8\_t data[31]

**Definition** hci\_types.h:968

[bt\_hci\_cp\_le\_set\_tx\_power\_report\_enable](structbt__hci__cp__le__set__tx__power__report__enable.md)

**Definition** hci\_types.h:601

[bt\_hci\_cp\_le\_set\_tx\_power\_report\_enable::local\_enable](structbt__hci__cp__le__set__tx__power__report__enable.md#a30580470d1ba516d86c8b157ca415ef3)

uint8\_t local\_enable

**Definition** hci\_types.h:603

[bt\_hci\_cp\_le\_set\_tx\_power\_report\_enable::handle](structbt__hci__cp__le__set__tx__power__report__enable.md#a4a37c87f8f6a966a90c5de09096d1356)

uint16\_t handle

**Definition** hci\_types.h:602

[bt\_hci\_cp\_le\_set\_tx\_power\_report\_enable::remote\_enable](structbt__hci__cp__le__set__tx__power__report__enable.md#ab4e8fb4fd7a1fbbc8b5736f8a6f65c5e)

uint8\_t remote\_enable

**Definition** hci\_types.h:604

[bt\_hci\_cp\_le\_setup\_iso\_path](structbt__hci__cp__le__setup__iso__path.md)

**Definition** hci\_types.h:2134

[bt\_hci\_cp\_le\_setup\_iso\_path::handle](structbt__hci__cp__le__setup__iso__path.md#a0054fede0e583cef0dbcf6ef3134e480)

uint16\_t handle

**Definition** hci\_types.h:2135

[bt\_hci\_cp\_le\_setup\_iso\_path::codec\_config\_len](structbt__hci__cp__le__setup__iso__path.md#a1a816d8e8c434a05ea897b74bc4d89c7)

uint8\_t codec\_config\_len

**Definition** hci\_types.h:2140

[bt\_hci\_cp\_le\_setup\_iso\_path::controller\_delay](structbt__hci__cp__le__setup__iso__path.md#a31948436e6608f9943d34ce89a65c64c)

uint8\_t controller\_delay[3]

**Definition** hci\_types.h:2139

[bt\_hci\_cp\_le\_setup\_iso\_path::codec\_id](structbt__hci__cp__le__setup__iso__path.md#a5256fc99b362e3a5f986ef2b71b29ccb)

struct bt\_hci\_cp\_codec\_id codec\_id

**Definition** hci\_types.h:2138

[bt\_hci\_cp\_le\_setup\_iso\_path::path\_id](structbt__hci__cp__le__setup__iso__path.md#a7c07d69b2005af1f7f2618f2bfa60d50)

uint8\_t path\_id

**Definition** hci\_types.h:2137

[bt\_hci\_cp\_le\_setup\_iso\_path::path\_dir](structbt__hci__cp__le__setup__iso__path.md#a89c1324359a4fc2f10fee9ebbac5cf2b)

uint8\_t path\_dir

**Definition** hci\_types.h:2136

[bt\_hci\_cp\_le\_setup\_iso\_path::codec\_config](structbt__hci__cp__le__setup__iso__path.md#ade4dee947e3d288f769d2d69fc57f96a)

uint8\_t codec\_config[0]

**Definition** hci\_types.h:2141

[bt\_hci\_cp\_le\_start\_encryption](structbt__hci__cp__le__start__encryption.md)

**Definition** hci\_types.h:1097

[bt\_hci\_cp\_le\_start\_encryption::handle](structbt__hci__cp__le__start__encryption.md#a4ac6d63f336e36a347242153aced4c71)

uint16\_t handle

**Definition** hci\_types.h:1098

[bt\_hci\_cp\_le\_start\_encryption::ediv](structbt__hci__cp__le__start__encryption.md#a640d201bbfa6f6d8476be02d3656e847)

uint16\_t ediv

**Definition** hci\_types.h:1100

[bt\_hci\_cp\_le\_start\_encryption::ltk](structbt__hci__cp__le__start__encryption.md#a99d2dd719ce38976e9da8a73f26839a1)

uint8\_t ltk[16]

**Definition** hci\_types.h:1101

[bt\_hci\_cp\_le\_start\_encryption::rand](structbt__hci__cp__le__start__encryption.md#ade8ae824dc5d85671971a3baafee8f54)

uint64\_t rand

**Definition** hci\_types.h:1099

[bt\_hci\_cp\_le\_terminate\_big](structbt__hci__cp__le__terminate__big.md)

**Definition** hci\_types.h:2101

[bt\_hci\_cp\_le\_terminate\_big::reason](structbt__hci__cp__le__terminate__big.md#a958ab6b2f2bb30c825060498e6917a18)

uint8\_t reason

**Definition** hci\_types.h:2103

[bt\_hci\_cp\_le\_terminate\_big::big\_handle](structbt__hci__cp__le__terminate__big.md#acb5fb9451cf890245a85704579b1d1c8)

uint8\_t big\_handle

**Definition** hci\_types.h:2102

[bt\_hci\_cp\_le\_tx\_test\_v3](structbt__hci__cp__le__tx__test__v3.md)

**Definition** hci\_types.h:1707

[bt\_hci\_cp\_le\_tx\_test\_v3::test\_data\_len](structbt__hci__cp__le__tx__test__v3.md#a1c0828e51bb6c24e9dd1f12b5badcfea)

uint8\_t test\_data\_len

**Definition** hci\_types.h:1709

[bt\_hci\_cp\_le\_tx\_test\_v3::switch\_pattern\_len](structbt__hci__cp__le__tx__test__v3.md#a459b850f35c61bf7f53d3730245cb4bb)

uint8\_t switch\_pattern\_len

**Definition** hci\_types.h:1714

[bt\_hci\_cp\_le\_tx\_test\_v3::cte\_len](structbt__hci__cp__le__tx__test__v3.md#a52d2d6dcc188d5f02904e0e56f461841)

uint8\_t cte\_len

**Definition** hci\_types.h:1712

[bt\_hci\_cp\_le\_tx\_test\_v3::tx\_ch](structbt__hci__cp__le__tx__test__v3.md#a6486882bc375f229a88bbfa53be49670)

uint8\_t tx\_ch

**Definition** hci\_types.h:1708

[bt\_hci\_cp\_le\_tx\_test\_v3::phy](structbt__hci__cp__le__tx__test__v3.md#a712a30d9d6afc7d302041e1de6721de4)

uint8\_t phy

**Definition** hci\_types.h:1711

[bt\_hci\_cp\_le\_tx\_test\_v3::pkt\_payload](structbt__hci__cp__le__tx__test__v3.md#ad8f2d2ca3ad3be28c0aec9e8a0e1bc61)

uint8\_t pkt\_payload

**Definition** hci\_types.h:1710

[bt\_hci\_cp\_le\_tx\_test\_v3::cte\_type](structbt__hci__cp__le__tx__test__v3.md#adf6b1653902fb13cc1ccc32cd91c990f)

uint8\_t cte\_type

**Definition** hci\_types.h:1713

[bt\_hci\_cp\_le\_tx\_test\_v3::ant\_ids](structbt__hci__cp__le__tx__test__v3.md#afdb6dd44108e9a4a21ac31a74c1e083f)

uint8\_t ant\_ids[0]

**Definition** hci\_types.h:1715

[bt\_hci\_cp\_le\_tx\_test\_v4\_tx\_power](structbt__hci__cp__le__tx__test__v4__tx__power.md)

**Definition** hci\_types.h:2262

[bt\_hci\_cp\_le\_tx\_test\_v4\_tx\_power::tx\_power](structbt__hci__cp__le__tx__test__v4__tx__power.md#a2a8b1c31787066ad2b471aec5c261085)

int8\_t tx\_power

**Definition** hci\_types.h:2263

[bt\_hci\_cp\_le\_tx\_test\_v4](structbt__hci__cp__le__tx__test__v4.md)

**Definition** hci\_types.h:2241

[bt\_hci\_cp\_le\_tx\_test\_v4::switch\_pattern\_len](structbt__hci__cp__le__tx__test__v4.md#a2039a87b5f32c4a45b8f858808df7cdc)

uint8\_t switch\_pattern\_len

**Definition** hci\_types.h:2248

[bt\_hci\_cp\_le\_tx\_test\_v4::tx\_ch](structbt__hci__cp__le__tx__test__v4.md#a3ccae40f09b2763b2b07dc16982f3973)

uint8\_t tx\_ch

**Definition** hci\_types.h:2242

[bt\_hci\_cp\_le\_tx\_test\_v4::ant\_ids](structbt__hci__cp__le__tx__test__v4.md#a3fe8ab7c0ee389dce8592cb7a38bc42c)

uint8\_t ant\_ids[0]

**Definition** hci\_types.h:2249

[bt\_hci\_cp\_le\_tx\_test\_v4::phy](structbt__hci__cp__le__tx__test__v4.md#a5db011159fe75f4522e03ea1efdc57bd)

uint8\_t phy

**Definition** hci\_types.h:2245

[bt\_hci\_cp\_le\_tx\_test\_v4::test\_data\_len](structbt__hci__cp__le__tx__test__v4.md#a7a8e2610fb8903ccfb6e4b08017f6112)

uint8\_t test\_data\_len

**Definition** hci\_types.h:2243

[bt\_hci\_cp\_le\_tx\_test\_v4::cte\_len](structbt__hci__cp__le__tx__test__v4.md#a8dea923a63e787de3bfe07611eb7a1ed)

uint8\_t cte\_len

**Definition** hci\_types.h:2246

[bt\_hci\_cp\_le\_tx\_test\_v4::pkt\_payload](structbt__hci__cp__le__tx__test__v4.md#abdd393eb264f04acf65e2dce4bd65ac0)

uint8\_t pkt\_payload

**Definition** hci\_types.h:2244

[bt\_hci\_cp\_le\_tx\_test\_v4::cte\_type](structbt__hci__cp__le__tx__test__v4.md#ae950f71a3fcfca0cf738bc28693256cf)

uint8\_t cte\_type

**Definition** hci\_types.h:2247

[bt\_hci\_cp\_le\_tx\_test](structbt__hci__cp__le__tx__test.md)

**Definition** hci\_types.h:1144

[bt\_hci\_cp\_le\_tx\_test::test\_data\_len](structbt__hci__cp__le__tx__test.md#a55c5f1621a51da03500910fc9664df54)

uint8\_t test\_data\_len

**Definition** hci\_types.h:1146

[bt\_hci\_cp\_le\_tx\_test::tx\_ch](structbt__hci__cp__le__tx__test.md#aae634b277125066ecbc36d119bc4244f)

uint8\_t tx\_ch

**Definition** hci\_types.h:1145

[bt\_hci\_cp\_le\_tx\_test::pkt\_payload](structbt__hci__cp__le__tx__test.md#ad93908905d370842f16e16cc45280495)

uint8\_t pkt\_payload

**Definition** hci\_types.h:1147

[bt\_hci\_cp\_le\_write\_default\_data\_len](structbt__hci__cp__le__write__default__data__len.md)

**Definition** hci\_types.h:1200

[bt\_hci\_cp\_le\_write\_default\_data\_len::max\_tx\_octets](structbt__hci__cp__le__write__default__data__len.md#a0ffb8c52d9031dfe448eac0943a4a49c)

uint16\_t max\_tx\_octets

**Definition** hci\_types.h:1201

[bt\_hci\_cp\_le\_write\_default\_data\_len::max\_tx\_time](structbt__hci__cp__le__write__default__data__len.md#a2ada0ea5ee8ac8e6d59fc6adc18421b8)

uint16\_t max\_tx\_time

**Definition** hci\_types.h:1202

[bt\_hci\_cp\_le\_write\_rf\_path\_comp](structbt__hci__cp__le__write__rf__path__comp.md)

**Definition** hci\_types.h:1674

[bt\_hci\_cp\_le\_write\_rf\_path\_comp::rx\_path\_comp](structbt__hci__cp__le__write__rf__path__comp.md#a11aad5607e444cf55dd5878f1f6f9436)

int16\_t rx\_path\_comp

**Definition** hci\_types.h:1676

[bt\_hci\_cp\_le\_write\_rf\_path\_comp::tx\_path\_comp](structbt__hci__cp__le__write__rf__path__comp.md#a5f99b131f3fba91706bdc8277c1abba1)

int16\_t tx\_path\_comp

**Definition** hci\_types.h:1675

[bt\_hci\_cp\_link\_key\_neg\_reply](structbt__hci__cp__link__key__neg__reply.md)

**Definition** hci\_types.h:422

[bt\_hci\_cp\_link\_key\_neg\_reply::bdaddr](structbt__hci__cp__link__key__neg__reply.md#aca3114707eb7c631af582626551619cd)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:423

[bt\_hci\_cp\_link\_key\_reply](structbt__hci__cp__link__key__reply.md)

**Definition** hci\_types.h:416

[bt\_hci\_cp\_link\_key\_reply::link\_key](structbt__hci__cp__link__key__reply.md#a2af0b4b55a5ffcff0221da841ba0cbba)

uint8\_t link\_key[16]

**Definition** hci\_types.h:418

[bt\_hci\_cp\_link\_key\_reply::bdaddr](structbt__hci__cp__link__key__reply.md#ab5221952fbcfe413d7c3bd3a441a9b17)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:417

[bt\_hci\_cp\_pin\_code\_neg\_reply](structbt__hci__cp__pin__code__neg__reply.md)

**Definition** hci\_types.h:438

[bt\_hci\_cp\_pin\_code\_neg\_reply::bdaddr](structbt__hci__cp__pin__code__neg__reply.md#a8aec3ba6c530850dce0a2d7b7f7f86ee)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:439

[bt\_hci\_cp\_pin\_code\_reply](structbt__hci__cp__pin__code__reply.md)

**Definition** hci\_types.h:427

[bt\_hci\_cp\_pin\_code\_reply::bdaddr](structbt__hci__cp__pin__code__reply.md#a627800dcb580110be785576dfcc49bb1)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:428

[bt\_hci\_cp\_pin\_code\_reply::pin\_len](structbt__hci__cp__pin__code__reply.md#aa0cbf668608c3eb4998356ad7b18c01a)

uint8\_t pin\_len

**Definition** hci\_types.h:429

[bt\_hci\_cp\_pin\_code\_reply::pin\_code](structbt__hci__cp__pin__code__reply.md#afc4ed5ae429087f4692af716d6b56997)

uint8\_t pin\_code[16]

**Definition** hci\_types.h:430

[bt\_hci\_cp\_read\_auth\_payload\_timeout](structbt__hci__cp__read__auth__payload__timeout.md)

**Definition** hci\_types.h:660

[bt\_hci\_cp\_read\_auth\_payload\_timeout::handle](structbt__hci__cp__read__auth__payload__timeout.md#adcdd657feb3ea6b892e2a5034365dd77)

uint16\_t handle

**Definition** hci\_types.h:661

[bt\_hci\_cp\_read\_codec\_capabilities](structbt__hci__cp__read__codec__capabilities.md)

**Definition** hci\_types.h:843

[bt\_hci\_cp\_read\_codec\_capabilities::direction](structbt__hci__cp__read__codec__capabilities.md#a237695f4d0a1359d5ce71d831708a69c)

uint8\_t direction

**Definition** hci\_types.h:846

[bt\_hci\_cp\_read\_codec\_capabilities::transport](structbt__hci__cp__read__codec__capabilities.md#a6479561573172356d7515ef92f75b8d4)

uint8\_t transport

**Definition** hci\_types.h:845

[bt\_hci\_cp\_read\_codec\_capabilities::codec\_id](structbt__hci__cp__read__codec__capabilities.md#ad48b7f228742d86a71dffa314331bbe1)

struct bt\_hci\_cp\_codec\_id codec\_id

**Definition** hci\_types.h:844

[bt\_hci\_cp\_read\_ctlr\_delay](structbt__hci__cp__read__ctlr__delay.md)

**Definition** hci\_types.h:860

[bt\_hci\_cp\_read\_ctlr\_delay::codec\_id](structbt__hci__cp__read__ctlr__delay.md#a2afb9ca8bc2e24cd479b29bc1a53c867)

struct bt\_hci\_cp\_codec\_id codec\_id

**Definition** hci\_types.h:861

[bt\_hci\_cp\_read\_ctlr\_delay::direction](structbt__hci__cp__read__ctlr__delay.md#a5e9f74d4f82809289038da29af0c663d)

uint8\_t direction

**Definition** hci\_types.h:863

[bt\_hci\_cp\_read\_ctlr\_delay::transport](structbt__hci__cp__read__ctlr__delay.md#a60a6a5b87896d0c27d734b56ead58a9b)

uint8\_t transport

**Definition** hci\_types.h:862

[bt\_hci\_cp\_read\_ctlr\_delay::codec\_config](structbt__hci__cp__read__ctlr__delay.md#a6c15d141c40bca8bd095f4a86f5a93bd)

uint8\_t codec\_config[0]

**Definition** hci\_types.h:865

[bt\_hci\_cp\_read\_ctlr\_delay::codec\_config\_len](structbt__hci__cp__read__ctlr__delay.md#ac881526b479d5f1717efbe35cdcc7e87)

uint8\_t codec\_config\_len

**Definition** hci\_types.h:864

[bt\_hci\_cp\_read\_encryption\_key\_size](structbt__hci__cp__read__encryption__key__size.md)

**Definition** hci\_types.h:887

[bt\_hci\_cp\_read\_encryption\_key\_size::handle](structbt__hci__cp__read__encryption__key__size.md#af15765007fd0e2fc4186b54323553019)

uint16\_t handle

**Definition** hci\_types.h:888

[bt\_hci\_cp\_read\_local\_ext\_features](structbt__hci__cp__read__local__ext__features.md)

**Definition** hci\_types.h:726

[bt\_hci\_cp\_read\_local\_ext\_features::page](structbt__hci__cp__read__local__ext__features.md#a79c6a6a6f1026a7e9ee774183ea7e132)

uint8\_t page

**Definition** hci\_types.h:727

[bt\_hci\_cp\_read\_remote\_ext\_features](structbt__hci__cp__read__remote__ext__features.md)

**Definition** hci\_types.h:480

[bt\_hci\_cp\_read\_remote\_ext\_features::page](structbt__hci__cp__read__remote__ext__features.md#a6aff189605b276998e58b051429a5cd2)

uint8\_t page

**Definition** hci\_types.h:482

[bt\_hci\_cp\_read\_remote\_ext\_features::handle](structbt__hci__cp__read__remote__ext__features.md#aaa236c11d148252e34fd20d794d991f3)

uint16\_t handle

**Definition** hci\_types.h:481

[bt\_hci\_cp\_read\_remote\_features](structbt__hci__cp__read__remote__features.md)

**Definition** hci\_types.h:475

[bt\_hci\_cp\_read\_remote\_features::handle](structbt__hci__cp__read__remote__features.md#ae14362a04c00b37342f3cc413f3933d3)

uint16\_t handle

**Definition** hci\_types.h:476

[bt\_hci\_cp\_read\_remote\_version\_info](structbt__hci__cp__read__remote__version__info.md)

**Definition** hci\_types.h:486

[bt\_hci\_cp\_read\_remote\_version\_info::handle](structbt__hci__cp__read__remote__version__info.md#a504b83f16a82b1e179d74547c7a29bf3)

uint16\_t handle

**Definition** hci\_types.h:487

[bt\_hci\_cp\_read\_rssi](structbt__hci__cp__read__rssi.md)

**Definition** hci\_types.h:874

[bt\_hci\_cp\_read\_rssi::handle](structbt__hci__cp__read__rssi.md#a0662bc56b344ca2bf9a2dcabe8a13c09)

uint16\_t handle

**Definition** hci\_types.h:875

[bt\_hci\_cp\_read\_tx\_power\_level](structbt__hci__cp__read__tx__power__level.md)

**Definition** hci\_types.h:567

[bt\_hci\_cp\_read\_tx\_power\_level::type](structbt__hci__cp__read__tx__power__level.md#a1920e671ec2deda1daf47f06a86d2881)

uint8\_t type

**Definition** hci\_types.h:569

[bt\_hci\_cp\_read\_tx\_power\_level::handle](structbt__hci__cp__read__tx__power__level.md#a1c268364fc80b9478d70b7eb997d9825)

uint16\_t handle

**Definition** hci\_types.h:568

[bt\_hci\_cp\_reject\_conn\_req](structbt__hci__cp__reject__conn__req.md)

**Definition** hci\_types.h:410

[bt\_hci\_cp\_reject\_conn\_req::reason](structbt__hci__cp__reject__conn__req.md#a1c2e234d6d00296bc01962b95e849df0)

uint8\_t reason

**Definition** hci\_types.h:412

[bt\_hci\_cp\_reject\_conn\_req::bdaddr](structbt__hci__cp__reject__conn__req.md#a9a1cb4173367c6f018fbd30a47c590b4)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:411

[bt\_hci\_cp\_remote\_name\_cancel](structbt__hci__cp__remote__name__cancel.md)

**Definition** hci\_types.h:466

[bt\_hci\_cp\_remote\_name\_cancel::bdaddr](structbt__hci__cp__remote__name__cancel.md#a0b7b4362804077ce828aeeb2b8af86b9)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:467

[bt\_hci\_cp\_remote\_name\_request](structbt__hci__cp__remote__name__request.md)

**Definition** hci\_types.h:458

[bt\_hci\_cp\_remote\_name\_request::bdaddr](structbt__hci__cp__remote__name__request.md#a5093f7bb70fa36f4948039d02d594e27)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:459

[bt\_hci\_cp\_remote\_name\_request::clock\_offset](structbt__hci__cp__remote__name__request.md#a5d7ea30052f8e4e2b3564659ca187c48)

uint16\_t clock\_offset

**Definition** hci\_types.h:462

[bt\_hci\_cp\_remote\_name\_request::reserved](structbt__hci__cp__remote__name__request.md#ab1883aa2b08d89f9c3190f338808a43c)

uint8\_t reserved

**Definition** hci\_types.h:461

[bt\_hci\_cp\_remote\_name\_request::pscan\_rep\_mode](structbt__hci__cp__remote__name__request.md#aed0aea58ca6f5dc15220083d377cbf5c)

uint8\_t pscan\_rep\_mode

**Definition** hci\_types.h:460

[bt\_hci\_cp\_set\_conn\_encrypt](structbt__hci__cp__set__conn__encrypt.md)

**Definition** hci\_types.h:452

[bt\_hci\_cp\_set\_conn\_encrypt::handle](structbt__hci__cp__set__conn__encrypt.md#a39e0c40ed6e6e9387ae384fd122fca4b)

uint16\_t handle

**Definition** hci\_types.h:453

[bt\_hci\_cp\_set\_conn\_encrypt::encrypt](structbt__hci__cp__set__conn__encrypt.md#aa259563efd49d04a8886f74169fd30b1)

uint8\_t encrypt

**Definition** hci\_types.h:454

[bt\_hci\_cp\_set\_ctl\_to\_host\_flow](structbt__hci__cp__set__ctl__to__host__flow.md)

**Definition** hci\_types.h:610

[bt\_hci\_cp\_set\_ctl\_to\_host\_flow::flow\_enable](structbt__hci__cp__set__ctl__to__host__flow.md#a75b614de1ab1fbfc6aa9c11d833976a6)

uint8\_t flow\_enable

**Definition** hci\_types.h:611

[bt\_hci\_cp\_set\_event\_mask\_page\_2](structbt__hci__cp__set__event__mask__page__2.md)

**Definition** hci\_types.h:644

[bt\_hci\_cp\_set\_event\_mask\_page\_2::events\_page\_2](structbt__hci__cp__set__event__mask__page__2.md#aacf1308d0892226e2c10216a07cd1fcc)

uint8\_t events\_page\_2[8]

**Definition** hci\_types.h:645

[bt\_hci\_cp\_set\_event\_mask](structbt__hci__cp__set__event__mask.md)

**Definition** hci\_types.h:526

[bt\_hci\_cp\_set\_event\_mask::events](structbt__hci__cp__set__event__mask.md#ab3af227511f47ee03f2d6aba8ae65c5d)

uint8\_t events[8]

**Definition** hci\_types.h:527

[bt\_hci\_cp\_setup\_sync\_conn](structbt__hci__cp__setup__sync__conn.md)

**Definition** hci\_types.h:388

[bt\_hci\_cp\_setup\_sync\_conn::rx\_bandwidth](structbt__hci__cp__setup__sync__conn.md#a137601ab44970782e2f3d4fcd2c8fcc2)

uint32\_t rx\_bandwidth

**Definition** hci\_types.h:391

[bt\_hci\_cp\_setup\_sync\_conn::content\_format](structbt__hci__cp__setup__sync__conn.md#a4d7df5b1aa714bc14d0b6c3cbccc5014)

uint16\_t content\_format

**Definition** hci\_types.h:393

[bt\_hci\_cp\_setup\_sync\_conn::max\_latency](structbt__hci__cp__setup__sync__conn.md#a5ffb5e552d4913974a10a16083f82864)

uint16\_t max\_latency

**Definition** hci\_types.h:392

[bt\_hci\_cp\_setup\_sync\_conn::retrans\_effort](structbt__hci__cp__setup__sync__conn.md#a61ebbc775d3ca0724ea173d72a96e0c0)

uint8\_t retrans\_effort

**Definition** hci\_types.h:394

[bt\_hci\_cp\_setup\_sync\_conn::pkt\_type](structbt__hci__cp__setup__sync__conn.md#a6d4c16a4d77d3ee4f8f65ab18a0f192d)

uint16\_t pkt\_type

**Definition** hci\_types.h:395

[bt\_hci\_cp\_setup\_sync\_conn::tx\_bandwidth](structbt__hci__cp__setup__sync__conn.md#aa35718e13a7d778c779be535c2b1945e)

uint32\_t tx\_bandwidth

**Definition** hci\_types.h:390

[bt\_hci\_cp\_setup\_sync\_conn::handle](structbt__hci__cp__setup__sync__conn.md#ad065185846694fc0070bb366e642f1c7)

uint16\_t handle

**Definition** hci\_types.h:389

[bt\_hci\_cp\_user\_confirm\_reply](structbt__hci__cp__user__confirm__reply.md)

**Definition** hci\_types.h:500

[bt\_hci\_cp\_user\_confirm\_reply::bdaddr](structbt__hci__cp__user__confirm__reply.md#abe0e8da3e590c565364ed30ba107a0e6)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:501

[bt\_hci\_cp\_user\_passkey\_neg\_reply](structbt__hci__cp__user__passkey__neg__reply.md)

**Definition** hci\_types.h:515

[bt\_hci\_cp\_user\_passkey\_neg\_reply::bdaddr](structbt__hci__cp__user__passkey__neg__reply.md#ade9d7068054b15089b8c238ecc3e4397)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:516

[bt\_hci\_cp\_user\_passkey\_reply](structbt__hci__cp__user__passkey__reply.md)

**Definition** hci\_types.h:509

[bt\_hci\_cp\_user\_passkey\_reply::bdaddr](structbt__hci__cp__user__passkey__reply.md#a56dbb4a858ecbf36eee61e24ed3742cf)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:510

[bt\_hci\_cp\_user\_passkey\_reply::passkey](structbt__hci__cp__user__passkey__reply.md#a80483025a32f37e7f75b3a220d48148c)

uint32\_t passkey

**Definition** hci\_types.h:511

[bt\_hci\_cp\_write\_auth\_payload\_timeout](structbt__hci__cp__write__auth__payload__timeout.md)

**Definition** hci\_types.h:671

[bt\_hci\_cp\_write\_auth\_payload\_timeout::auth\_payload\_timeout](structbt__hci__cp__write__auth__payload__timeout.md#a385c88012b09ec561b9ba7edaadeb574)

uint16\_t auth\_payload\_timeout

**Definition** hci\_types.h:673

[bt\_hci\_cp\_write\_auth\_payload\_timeout::handle](structbt__hci__cp__write__auth__payload__timeout.md#ad99d5b9f416f11492ac0f412b400aeb6)

uint16\_t handle

**Definition** hci\_types.h:672

[bt\_hci\_cp\_write\_class\_of\_device](structbt__hci__cp__write__class__of__device.md)

**Definition** hci\_types.h:560

[bt\_hci\_cp\_write\_class\_of\_device::class\_of\_device](structbt__hci__cp__write__class__of__device.md#acc3b940de1a5da095e8a4f18e69229f2)

uint8\_t class\_of\_device[3]

**Definition** hci\_types.h:561

[bt\_hci\_cp\_write\_conn\_accept\_timeout](structbt__hci__cp__write__conn__accept__timeout.md)

**Definition** hci\_types.h:544

[bt\_hci\_cp\_write\_conn\_accept\_timeout::conn\_accept\_timeout](structbt__hci__cp__write__conn__accept__timeout.md#a13de5f88920c6a41dafa598734b7acf9)

uint16\_t conn\_accept\_timeout

**Definition** hci\_types.h:545

[bt\_hci\_cp\_write\_inquiry\_mode](structbt__hci__cp__write__inquiry__mode.md)

**Definition** hci\_types.h:634

[bt\_hci\_cp\_write\_inquiry\_mode::mode](structbt__hci__cp__write__inquiry__mode.md#a827e138b7faaec54ec84a1cc1e0c480f)

uint8\_t mode

**Definition** hci\_types.h:635

[bt\_hci\_cp\_write\_le\_host\_supp](structbt__hci__cp__write__le__host__supp.md)

**Definition** hci\_types.h:649

[bt\_hci\_cp\_write\_le\_host\_supp::le](structbt__hci__cp__write__le__host__supp.md#ace1838a80b6061231b536f36e8999ac0)

uint8\_t le

**Definition** hci\_types.h:650

[bt\_hci\_cp\_write\_le\_host\_supp::simul](structbt__hci__cp__write__le__host__supp.md#ad2c27c0f98b2334490022e90563e1271)

uint8\_t simul

**Definition** hci\_types.h:651

[bt\_hci\_cp\_write\_sc\_host\_supp](structbt__hci__cp__write__sc__host__supp.md)

**Definition** hci\_types.h:655

[bt\_hci\_cp\_write\_sc\_host\_supp::sc\_support](structbt__hci__cp__write__sc__host__supp.md#a48ef951f4de05c5772be5c08edca7cec)

uint8\_t sc\_support

**Definition** hci\_types.h:656

[bt\_hci\_cp\_write\_ssp\_mode](structbt__hci__cp__write__ssp__mode.md)

**Definition** hci\_types.h:639

[bt\_hci\_cp\_write\_ssp\_mode::mode](structbt__hci__cp__write__ssp__mode.md#a8ebf7f7890adec53aa8c2307d2b1a33f)

uint8\_t mode

**Definition** hci\_types.h:640

[bt\_hci\_evt\_auth\_complete](structbt__hci__evt__auth__complete.md)

**Definition** hci\_types.h:2300

[bt\_hci\_evt\_auth\_complete::handle](structbt__hci__evt__auth__complete.md#a7a78803e156218f138866fbb13fdadce)

uint16\_t handle

**Definition** hci\_types.h:2302

[bt\_hci\_evt\_auth\_complete::status](structbt__hci__evt__auth__complete.md#ae2b4b5bcc7195247626004d46ee22dd5)

uint8\_t status

**Definition** hci\_types.h:2301

[bt\_hci\_evt\_auth\_payload\_timeout\_exp](structbt__hci__evt__auth__payload__timeout__exp.md)

**Definition** hci\_types.h:2588

[bt\_hci\_evt\_auth\_payload\_timeout\_exp::handle](structbt__hci__evt__auth__payload__timeout__exp.md#a799bc3c63fe5083d61d8bf152ef4cee7)

uint16\_t handle

**Definition** hci\_types.h:2589

[bt\_hci\_evt\_cc\_status](structbt__hci__evt__cc__status.md)

**Definition** hci\_types.h:2341

[bt\_hci\_evt\_cc\_status::status](structbt__hci__evt__cc__status.md#a97cceaa218700da9b529ebadbb08c42c)

uint8\_t status

**Definition** hci\_types.h:2342

[bt\_hci\_evt\_cmd\_complete](structbt__hci__evt__cmd__complete.md)

**Definition** hci\_types.h:2336

[bt\_hci\_evt\_cmd\_complete::opcode](structbt__hci__evt__cmd__complete.md#a3e61d980b4fa3084d3c50ead735fb76d)

uint16\_t opcode

**Definition** hci\_types.h:2338

[bt\_hci\_evt\_cmd\_complete::ncmd](structbt__hci__evt__cmd__complete.md#a4da0539f81057722c8c322685bc12a40)

uint8\_t ncmd

**Definition** hci\_types.h:2337

[bt\_hci\_evt\_cmd\_status](structbt__hci__evt__cmd__status.md)

**Definition** hci\_types.h:2346

[bt\_hci\_evt\_cmd\_status::opcode](structbt__hci__evt__cmd__status.md#a34002b693dc201083be4be77cfddcdb5)

uint16\_t opcode

**Definition** hci\_types.h:2349

[bt\_hci\_evt\_cmd\_status::ncmd](structbt__hci__evt__cmd__status.md#aed690e1cea2411df167e66cfaa742639)

uint8\_t ncmd

**Definition** hci\_types.h:2348

[bt\_hci\_evt\_cmd\_status::status](structbt__hci__evt__cmd__status.md#aedd1560409005dbce409b892af1e3edf)

uint8\_t status

**Definition** hci\_types.h:2347

[bt\_hci\_evt\_conn\_complete](structbt__hci__evt__conn__complete.md)

**Definition** hci\_types.h:2277

[bt\_hci\_evt\_conn\_complete::status](structbt__hci__evt__conn__complete.md#a3dbf4fef53279003b7304ffee4a55e56)

uint8\_t status

**Definition** hci\_types.h:2278

[bt\_hci\_evt\_conn\_complete::bdaddr](structbt__hci__evt__conn__complete.md#a60a2ca6a8f16e4562c12b369685efa9b)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:2280

[bt\_hci\_evt\_conn\_complete::encr\_enabled](structbt__hci__evt__conn__complete.md#a975617e8b568675a3ed8883cbe411557)

uint8\_t encr\_enabled

**Definition** hci\_types.h:2282

[bt\_hci\_evt\_conn\_complete::handle](structbt__hci__evt__conn__complete.md#ad8877912008ea7445a67abc43aab5021)

uint16\_t handle

**Definition** hci\_types.h:2279

[bt\_hci\_evt\_conn\_complete::link\_type](structbt__hci__evt__conn__complete.md#afd9a21adf7d35205fb7e222c2e9e0328)

uint8\_t link\_type

**Definition** hci\_types.h:2281

[bt\_hci\_evt\_conn\_request](structbt__hci__evt__conn__request.md)

**Definition** hci\_types.h:2286

[bt\_hci\_evt\_conn\_request::bdaddr](structbt__hci__evt__conn__request.md#a03a2ee7ff7754173dff0809e4ebce9e6)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:2287

[bt\_hci\_evt\_conn\_request::dev\_class](structbt__hci__evt__conn__request.md#a6059d7c56f45d2fe047a7324db1e820d)

uint8\_t dev\_class[3]

**Definition** hci\_types.h:2288

[bt\_hci\_evt\_conn\_request::link\_type](structbt__hci__evt__conn__request.md#ae11d550701f64717a7d6df5c89b92d0e)

uint8\_t link\_type

**Definition** hci\_types.h:2289

[bt\_hci\_evt\_data\_buf\_overflow](structbt__hci__evt__data__buf__overflow.md)

**Definition** hci\_types.h:2404

[bt\_hci\_evt\_data\_buf\_overflow::link\_type](structbt__hci__evt__data__buf__overflow.md#ae0201e03ebb9b9b33e9eae593a56355f)

uint8\_t link\_type

**Definition** hci\_types.h:2405

[bt\_hci\_evt\_disconn\_complete](structbt__hci__evt__disconn__complete.md)

**Definition** hci\_types.h:2293

[bt\_hci\_evt\_disconn\_complete::reason](structbt__hci__evt__disconn__complete.md#a172554fbacf7aaa4dfbafe58b60fa5e6)

uint8\_t reason

**Definition** hci\_types.h:2296

[bt\_hci\_evt\_disconn\_complete::handle](structbt__hci__evt__disconn__complete.md#ab75f198a6495ad02a00bb3df99ab4258)

uint16\_t handle

**Definition** hci\_types.h:2295

[bt\_hci\_evt\_disconn\_complete::status](structbt__hci__evt__disconn__complete.md#aed22ac781e9d70d11e7ebbe6f2e063bd)

uint8\_t status

**Definition** hci\_types.h:2294

[bt\_hci\_evt\_encrypt\_change](structbt__hci__evt__encrypt__change.md)

**Definition** hci\_types.h:2313

[bt\_hci\_evt\_encrypt\_change::encrypt](structbt__hci__evt__encrypt__change.md#a61cc0e3c209acbb289d071515b44860a)

uint8\_t encrypt

**Definition** hci\_types.h:2316

[bt\_hci\_evt\_encrypt\_change::handle](structbt__hci__evt__encrypt__change.md#a7737f659115ca602c1224c364a4c7404)

uint16\_t handle

**Definition** hci\_types.h:2315

[bt\_hci\_evt\_encrypt\_change::status](structbt__hci__evt__encrypt__change.md#af063bbd28d29edbcc81e907631167de7)

uint8\_t status

**Definition** hci\_types.h:2314

[bt\_hci\_evt\_encrypt\_key\_refresh\_complete](structbt__hci__evt__encrypt__key__refresh__complete.md)

**Definition** hci\_types.h:2541

[bt\_hci\_evt\_encrypt\_key\_refresh\_complete::handle](structbt__hci__evt__encrypt__key__refresh__complete.md#af5562687a4f6e3a1e82cd1a81cec5ad6)

uint16\_t handle

**Definition** hci\_types.h:2543

[bt\_hci\_evt\_encrypt\_key\_refresh\_complete::status](structbt__hci__evt__encrypt__key__refresh__complete.md#afdd162cff0f1eedfe9e8ee7223b3226e)

uint8\_t status

**Definition** hci\_types.h:2542

[bt\_hci\_evt\_extended\_inquiry\_result](structbt__hci__evt__extended__inquiry__result.md)

**Definition** hci\_types.h:2529

[bt\_hci\_evt\_extended\_inquiry\_result::eir](structbt__hci__evt__extended__inquiry__result.md#a1eba2841941f7cdbb00f548ebf0485e9)

uint8\_t eir[240]

**Definition** hci\_types.h:2537

[bt\_hci\_evt\_extended\_inquiry\_result::rssi](structbt__hci__evt__extended__inquiry__result.md#a21f7f48422bcfb867c9ca2e4411a2fbd)

int8\_t rssi

**Definition** hci\_types.h:2536

[bt\_hci\_evt\_extended\_inquiry\_result::clock\_offset](structbt__hci__evt__extended__inquiry__result.md#a30c5586d954585006238e8c2b33a7601)

uint16\_t clock\_offset

**Definition** hci\_types.h:2535

[bt\_hci\_evt\_extended\_inquiry\_result::num\_reports](structbt__hci__evt__extended__inquiry__result.md#a76e4e82d1dedaee94bd730a4134d7d77)

uint8\_t num\_reports

**Definition** hci\_types.h:2530

[bt\_hci\_evt\_extended\_inquiry\_result::addr](structbt__hci__evt__extended__inquiry__result.md#a955a7d36736badfae1f39fa9eda61ebb)

bt\_addr\_t addr

**Definition** hci\_types.h:2531

[bt\_hci\_evt\_extended\_inquiry\_result::cod](structbt__hci__evt__extended__inquiry__result.md#ab4ebcf09817827d1d10ddeee13832759)

uint8\_t cod[3]

**Definition** hci\_types.h:2534

[bt\_hci\_evt\_extended\_inquiry\_result::reserved](structbt__hci__evt__extended__inquiry__result.md#ab6ec4b5efe058e225d173cbda9a16f2e)

uint8\_t reserved

**Definition** hci\_types.h:2533

[bt\_hci\_evt\_extended\_inquiry\_result::pscan\_rep\_mode](structbt__hci__evt__extended__inquiry__result.md#aba4aac84e23ca9d283cb8af265dcaf0d)

uint8\_t pscan\_rep\_mode

**Definition** hci\_types.h:2532

[bt\_hci\_evt\_hardware\_error](structbt__hci__evt__hardware__error.md)

**Definition** hci\_types.h:2353

[bt\_hci\_evt\_hardware\_error::hardware\_code](structbt__hci__evt__hardware__error.md#ab7be990e7cc32df43a3c976cb922e333)

uint8\_t hardware\_code

**Definition** hci\_types.h:2354

[bt\_hci\_evt\_hdr](structbt__hci__evt__hdr.md)

**Definition** hci\_types.h:48

[bt\_hci\_evt\_hdr::len](structbt__hci__evt__hdr.md#a2d580a0c12b29d23002ee9d494c9e16d)

uint8\_t len

**Definition** hci\_types.h:50

[bt\_hci\_evt\_hdr::evt](structbt__hci__evt__hdr.md#aba3aca89bfbe7e8cbd144765cb20fcea)

uint8\_t evt

**Definition** hci\_types.h:49

[bt\_hci\_evt\_inquiry\_complete](structbt__hci__evt__inquiry__complete.md)

**Definition** hci\_types.h:2272

[bt\_hci\_evt\_inquiry\_complete::status](structbt__hci__evt__inquiry__complete.md#aa8c1e8dc9807476f4759a3b3648b6332)

uint8\_t status

**Definition** hci\_types.h:2273

[bt\_hci\_evt\_inquiry\_result\_with\_rssi](structbt__hci__evt__inquiry__result__with__rssi.md)

**Definition** hci\_types.h:2409

[bt\_hci\_evt\_inquiry\_result\_with\_rssi::reserved](structbt__hci__evt__inquiry__result__with__rssi.md#a09914ee9998c0b59cb35ed74d08aa4f2)

uint8\_t reserved

**Definition** hci\_types.h:2412

[bt\_hci\_evt\_inquiry\_result\_with\_rssi::pscan\_rep\_mode](structbt__hci__evt__inquiry__result__with__rssi.md#a0a5c188d0d40b4259cbeb613c0dd12cf)

uint8\_t pscan\_rep\_mode

**Definition** hci\_types.h:2411

[bt\_hci\_evt\_inquiry\_result\_with\_rssi::clock\_offset](structbt__hci__evt__inquiry__result__with__rssi.md#a1ee08f85103581994a88345cc94d7494)

uint16\_t clock\_offset

**Definition** hci\_types.h:2414

[bt\_hci\_evt\_inquiry\_result\_with\_rssi::rssi](structbt__hci__evt__inquiry__result__with__rssi.md#a6d19e6400d7015db7122516e570d7989)

int8\_t rssi

**Definition** hci\_types.h:2415

[bt\_hci\_evt\_inquiry\_result\_with\_rssi::cod](structbt__hci__evt__inquiry__result__with__rssi.md#ad9b4920e2864ed8350de038dffe64574)

uint8\_t cod[3]

**Definition** hci\_types.h:2413

[bt\_hci\_evt\_inquiry\_result\_with\_rssi::addr](structbt__hci__evt__inquiry__result__with__rssi.md#af955dd1660f83e41e6d1b2b5aecf8133)

bt\_addr\_t addr

**Definition** hci\_types.h:2410

[bt\_hci\_evt\_io\_capa\_req](structbt__hci__evt__io__capa__req.md)

**Definition** hci\_types.h:2547

[bt\_hci\_evt\_io\_capa\_req::bdaddr](structbt__hci__evt__io__capa__req.md#a52412f7bd8f8dea391904b9f2444b50a)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:2548

[bt\_hci\_evt\_io\_capa\_resp](structbt__hci__evt__io__capa__resp.md)

**Definition** hci\_types.h:2552

[bt\_hci\_evt\_io\_capa\_resp::authentication](structbt__hci__evt__io__capa__resp.md#a160cb3aea96bf698520e11673a40b2d7)

uint8\_t authentication

**Definition** hci\_types.h:2556

[bt\_hci\_evt\_io\_capa\_resp::capability](structbt__hci__evt__io__capa__resp.md#a851eae620ad90067957d4dec2f04efbe)

uint8\_t capability

**Definition** hci\_types.h:2554

[bt\_hci\_evt\_io\_capa\_resp::oob\_data](structbt__hci__evt__io__capa__resp.md#ab12325d1536fe6a75d0a137bea301e8f)

uint8\_t oob\_data

**Definition** hci\_types.h:2555

[bt\_hci\_evt\_io\_capa\_resp::bdaddr](structbt__hci__evt__io__capa__resp.md#adac9c9f3999099fd460651e3b012fd0f)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:2553

[bt\_hci\_evt\_le\_adv\_set\_terminated](structbt__hci__evt__le__adv__set__terminated.md)

**Definition** hci\_types.h:2770

[bt\_hci\_evt\_le\_adv\_set\_terminated::num\_completed\_ext\_adv\_evts](structbt__hci__evt__le__adv__set__terminated.md#a192f13d6223e437261a225e6b28d04db)

uint8\_t num\_completed\_ext\_adv\_evts

**Definition** hci\_types.h:2774

[bt\_hci\_evt\_le\_adv\_set\_terminated::status](structbt__hci__evt__le__adv__set__terminated.md#a583409e2dc912af2bd5e83124fce3a72)

uint8\_t status

**Definition** hci\_types.h:2771

[bt\_hci\_evt\_le\_adv\_set\_terminated::conn\_handle](structbt__hci__evt__le__adv__set__terminated.md#af2503ee8e1c9add6927fa65b69c48551)

uint16\_t conn\_handle

**Definition** hci\_types.h:2773

[bt\_hci\_evt\_le\_adv\_set\_terminated::adv\_handle](structbt__hci__evt__le__adv__set__terminated.md#af35564406269144cfa2532cd510aa0bd)

uint8\_t adv\_handle

**Definition** hci\_types.h:2772

[bt\_hci\_evt\_le\_advertising\_info](structbt__hci__evt__le__advertising__info.md)

**Definition** hci\_types.h:2610

[bt\_hci\_evt\_le\_advertising\_info::length](structbt__hci__evt__le__advertising__info.md#a11c223103bf89300bd90cb8725746121)

uint8\_t length

**Definition** hci\_types.h:2613

[bt\_hci\_evt\_le\_advertising\_info::addr](structbt__hci__evt__le__advertising__info.md#a1d6863f1a601a2df9d772e3cc1fec118)

bt\_addr\_le\_t addr

**Definition** hci\_types.h:2612

[bt\_hci\_evt\_le\_advertising\_info::evt\_type](structbt__hci__evt__le__advertising__info.md#a5943685ccd3491a883ba9450f700bb86)

uint8\_t evt\_type

**Definition** hci\_types.h:2611

[bt\_hci\_evt\_le\_advertising\_info::data](structbt__hci__evt__le__advertising__info.md#af7d9d720ca67714f2a809e2530a1ff98)

uint8\_t data[0]

**Definition** hci\_types.h:2614

[bt\_hci\_evt\_le\_advertising\_report](structbt__hci__evt__le__advertising__report.md)

**Definition** hci\_types.h:2616

[bt\_hci\_evt\_le\_advertising\_report::adv\_info](structbt__hci__evt__le__advertising__report.md#a9762be19de1f24be4d4626e7e2f8205d)

struct bt\_hci\_evt\_le\_advertising\_info adv\_info[0]

**Definition** hci\_types.h:2618

[bt\_hci\_evt\_le\_advertising\_report::num\_reports](structbt__hci__evt__le__advertising__report.md#ac69aab36aa421630357e4c6706c13e75)

uint8\_t num\_reports

**Definition** hci\_types.h:2617

[bt\_hci\_evt\_le\_big\_complete](structbt__hci__evt__le__big__complete.md)

**Definition** hci\_types.h:2891

[bt\_hci\_evt\_le\_big\_complete::irc](structbt__hci__evt__le__big__complete.md#a07163dee904412d6d8faca8563a944d9)

uint8\_t irc

**Definition** hci\_types.h:2900

[bt\_hci\_evt\_le\_big\_complete::iso\_interval](structbt__hci__evt__le__big__complete.md#a0b0d19d442ed8f1025165c435786ba09)

uint16\_t iso\_interval

**Definition** hci\_types.h:2902

[bt\_hci\_evt\_le\_big\_complete::big\_handle](structbt__hci__evt__le__big__complete.md#a14eaa705f1df38337722a41e8189f807)

uint8\_t big\_handle

**Definition** hci\_types.h:2893

[bt\_hci\_evt\_le\_big\_complete::bn](structbt__hci__evt__le__big__complete.md#a2327e42013033767af233d1c2c3acc56)

uint8\_t bn

**Definition** hci\_types.h:2898

[bt\_hci\_evt\_le\_big\_complete::latency](structbt__hci__evt__le__big__complete.md#a2727d329c37e3b3644cfad02d86abb55)

uint8\_t latency[3]

**Definition** hci\_types.h:2895

[bt\_hci\_evt\_le\_big\_complete::sync\_delay](structbt__hci__evt__le__big__complete.md#a2847d5fc997f80a3e21b7e03d80c9574)

uint8\_t sync\_delay[3]

**Definition** hci\_types.h:2894

[bt\_hci\_evt\_le\_big\_complete::pto](structbt__hci__evt__le__big__complete.md#a6c295870732d65002ec21b4b607e7c0b)

uint8\_t pto

**Definition** hci\_types.h:2899

[bt\_hci\_evt\_le\_big\_complete::max\_pdu](structbt__hci__evt__le__big__complete.md#a8b433ac376e347bf391d4dd804c469f3)

uint16\_t max\_pdu

**Definition** hci\_types.h:2901

[bt\_hci\_evt\_le\_big\_complete::num\_bis](structbt__hci__evt__le__big__complete.md#a995c8fe06ec087f16b771c38171745b1)

uint8\_t num\_bis

**Definition** hci\_types.h:2903

[bt\_hci\_evt\_le\_big\_complete::phy](structbt__hci__evt__le__big__complete.md#abfa6d6bc135350737451e053aa7d212c)

uint8\_t phy

**Definition** hci\_types.h:2896

[bt\_hci\_evt\_le\_big\_complete::status](structbt__hci__evt__le__big__complete.md#ad6787806a3622b3bd3da4512bb8ddffe)

uint8\_t status

**Definition** hci\_types.h:2892

[bt\_hci\_evt\_le\_big\_complete::nse](structbt__hci__evt__le__big__complete.md#ae77364aafe179588f7b8414292e35f5e)

uint8\_t nse

**Definition** hci\_types.h:2897

[bt\_hci\_evt\_le\_big\_complete::handle](structbt__hci__evt__le__big__complete.md#af1c8bd66c3dba70df22f8655b4f27925)

uint16\_t handle[0]

**Definition** hci\_types.h:2904

[bt\_hci\_evt\_le\_big\_sync\_established](structbt__hci__evt__le__big__sync__established.md)

**Definition** hci\_types.h:2914

[bt\_hci\_evt\_le\_big\_sync\_established::max\_pdu](structbt__hci__evt__le__big__sync__established.md#a13db0d402636a71ed029575c1e5771c5)

uint16\_t max\_pdu

**Definition** hci\_types.h:2922

[bt\_hci\_evt\_le\_big\_sync\_established::num\_bis](structbt__hci__evt__le__big__sync__established.md#a2fa405310a8fed0341001b316ca7bd4f)

uint8\_t num\_bis

**Definition** hci\_types.h:2924

[bt\_hci\_evt\_le\_big\_sync\_established::big\_handle](structbt__hci__evt__le__big__sync__established.md#a31a05f8afb69e5885700cc4ad3b161b2)

uint8\_t big\_handle

**Definition** hci\_types.h:2916

[bt\_hci\_evt\_le\_big\_sync\_established::nse](structbt__hci__evt__le__big__sync__established.md#a383dc92f6d16ec971455e20665cd7496)

uint8\_t nse

**Definition** hci\_types.h:2918

[bt\_hci\_evt\_le\_big\_sync\_established::bn](structbt__hci__evt__le__big__sync__established.md#a451466916fbe2f220c277b4b4e62241d)

uint8\_t bn

**Definition** hci\_types.h:2919

[bt\_hci\_evt\_le\_big\_sync\_established::handle](structbt__hci__evt__le__big__sync__established.md#a48766968cb677614f525ea36551ad6c8)

uint16\_t handle[0]

**Definition** hci\_types.h:2925

[bt\_hci\_evt\_le\_big\_sync\_established::iso\_interval](structbt__hci__evt__le__big__sync__established.md#a610313c11c65faf82e06a121affb8b2b)

uint16\_t iso\_interval

**Definition** hci\_types.h:2923

[bt\_hci\_evt\_le\_big\_sync\_established::pto](structbt__hci__evt__le__big__sync__established.md#a6b750de25b2a1afc38995030953364ce)

uint8\_t pto

**Definition** hci\_types.h:2920

[bt\_hci\_evt\_le\_big\_sync\_established::status](structbt__hci__evt__le__big__sync__established.md#a8feb21ef6eacf45dfc09b09e0bce04b1)

uint8\_t status

**Definition** hci\_types.h:2915

[bt\_hci\_evt\_le\_big\_sync\_established::latency](structbt__hci__evt__le__big__sync__established.md#aebb25f9a63fa013ec6ef891ca498dbb4)

uint8\_t latency[3]

**Definition** hci\_types.h:2917

[bt\_hci\_evt\_le\_big\_sync\_established::irc](structbt__hci__evt__le__big__sync__established.md#afd52315dafe02ee28bc26f058b12fe9e)

uint8\_t irc

**Definition** hci\_types.h:2921

[bt\_hci\_evt\_le\_big\_sync\_lost](structbt__hci__evt__le__big__sync__lost.md)

**Definition** hci\_types.h:2929

[bt\_hci\_evt\_le\_big\_sync\_lost::reason](structbt__hci__evt__le__big__sync__lost.md#a02b724a60e71805088aefca9989ad878)

uint8\_t reason

**Definition** hci\_types.h:2931

[bt\_hci\_evt\_le\_big\_sync\_lost::big\_handle](structbt__hci__evt__le__big__sync__lost.md#ae59a9c18363f7aee67563494d98aa971)

uint8\_t big\_handle

**Definition** hci\_types.h:2930

[bt\_hci\_evt\_le\_big\_terminate](structbt__hci__evt__le__big__terminate.md)

**Definition** hci\_types.h:2908

[bt\_hci\_evt\_le\_big\_terminate::reason](structbt__hci__evt__le__big__terminate.md#a0303ac64b825f93210dfc70a8a081ea6)

uint8\_t reason

**Definition** hci\_types.h:2910

[bt\_hci\_evt\_le\_big\_terminate::big\_handle](structbt__hci__evt__le__big__terminate.md#ad9c9e6d42661366d62d79163fa9ad1c7)

uint8\_t big\_handle

**Definition** hci\_types.h:2909

[bt\_hci\_evt\_le\_biginfo\_adv\_report](structbt__hci__evt__le__biginfo__adv__report.md)

**Definition** hci\_types.h:2962

[bt\_hci\_evt\_le\_biginfo\_adv\_report::max\_sdu](structbt__hci__evt__le__biginfo__adv__report.md#a084c13c4b0c9c8dca0653b56e53a0c74)

uint16\_t max\_sdu

**Definition** hci\_types.h:2972

[bt\_hci\_evt\_le\_biginfo\_adv\_report::max\_pdu](structbt__hci__evt__le__biginfo__adv__report.md#a12a000c049e85d2b24720d1a362d28df)

uint16\_t max\_pdu

**Definition** hci\_types.h:2970

[bt\_hci\_evt\_le\_biginfo\_adv\_report::phy](structbt__hci__evt__le__biginfo__adv__report.md#a2301112acf22cf68d6495ff85f0f29bf)

uint8\_t phy

**Definition** hci\_types.h:2973

[bt\_hci\_evt\_le\_biginfo\_adv\_report::sdu\_interval](structbt__hci__evt__le__biginfo__adv__report.md#a81e236ceb24012bc267f656f20f1f8c4)

uint8\_t sdu\_interval[3]

**Definition** hci\_types.h:2971

[bt\_hci\_evt\_le\_biginfo\_adv\_report::sync\_handle](structbt__hci__evt__le__biginfo__adv__report.md#a8be20bfc607e6ce34ea75c53e285b0d5)

uint16\_t sync\_handle

**Definition** hci\_types.h:2963

[bt\_hci\_evt\_le\_biginfo\_adv\_report::irc](structbt__hci__evt__le__biginfo__adv__report.md#a9c1235653245b517a105570c60ddfa09)

uint8\_t irc

**Definition** hci\_types.h:2969

[bt\_hci\_evt\_le\_biginfo\_adv\_report::framing](structbt__hci__evt__le__biginfo__adv__report.md#abe0636beae2f51004193ad5f7c9efeef)

uint8\_t framing

**Definition** hci\_types.h:2974

[bt\_hci\_evt\_le\_biginfo\_adv\_report::bn](structbt__hci__evt__le__biginfo__adv__report.md#ada35f690706be1c6ee8f40787bbe53e5)

uint8\_t bn

**Definition** hci\_types.h:2967

[bt\_hci\_evt\_le\_biginfo\_adv\_report::nse](structbt__hci__evt__le__biginfo__adv__report.md#ae28d5378a7e2ef59fabb62a3a430ccc8)

uint8\_t nse

**Definition** hci\_types.h:2965

[bt\_hci\_evt\_le\_biginfo\_adv\_report::encryption](structbt__hci__evt__le__biginfo__adv__report.md#ae63eaf93f728109b5fb77ca3179ba99c)

uint8\_t encryption

**Definition** hci\_types.h:2975

[bt\_hci\_evt\_le\_biginfo\_adv\_report::num\_bis](structbt__hci__evt__le__biginfo__adv__report.md#ae68f803bbc3f06e7190f62be98d2fe66)

uint8\_t num\_bis

**Definition** hci\_types.h:2964

[bt\_hci\_evt\_le\_biginfo\_adv\_report::iso\_interval](structbt__hci__evt__le__biginfo__adv__report.md#ae92b69ab0bc257d4f50b98e071c6038b)

uint16\_t iso\_interval

**Definition** hci\_types.h:2966

[bt\_hci\_evt\_le\_biginfo\_adv\_report::pto](structbt__hci__evt__le__biginfo__adv__report.md#af3a871d3de34b90fc2b09b0725caf479)

uint8\_t pto

**Definition** hci\_types.h:2968

[bt\_hci\_evt\_le\_chan\_sel\_algo](structbt__hci__evt__le__chan__sel__algo.md)

**Definition** hci\_types.h:2787

[bt\_hci\_evt\_le\_chan\_sel\_algo::handle](structbt__hci__evt__le__chan__sel__algo.md#a16393279e08073dad549e111e610c8e8)

uint16\_t handle

**Definition** hci\_types.h:2788

[bt\_hci\_evt\_le\_chan\_sel\_algo::chan\_sel\_algo](structbt__hci__evt__le__chan__sel__algo.md#a976a62e81b094a59ce42cb6ad3ce45ac)

uint8\_t chan\_sel\_algo

**Definition** hci\_types.h:2789

[bt\_hci\_evt\_le\_cis\_established](structbt__hci__evt__le__cis__established.md)

**Definition** hci\_types.h:2863

[bt\_hci\_evt\_le\_cis\_established::interval](structbt__hci__evt__le__cis__established.md#a0bcdc0d8b3b776660d2e51427f9634dd)

uint16\_t interval

**Definition** hci\_types.h:2879

[bt\_hci\_evt\_le\_cis\_established::p\_ft](structbt__hci__evt__le__cis__established.md#a200afaff044b9eea653d8aee13297dc2)

uint8\_t p\_ft

**Definition** hci\_types.h:2876

[bt\_hci\_evt\_le\_cis\_established::p\_phy](structbt__hci__evt__le__cis__established.md#a25b84cf026775b582c7944e265ffb0b2)

uint8\_t p\_phy

**Definition** hci\_types.h:2871

[bt\_hci\_evt\_le\_cis\_established::status](structbt__hci__evt__le__cis__established.md#a4d90dbeda130a6142ff0b7f9e2ee7c16)

uint8\_t status

**Definition** hci\_types.h:2864

[bt\_hci\_evt\_le\_cis\_established::c\_phy](structbt__hci__evt__le__cis__established.md#a53ea1da3f31313ab73b511c72912bd33)

uint8\_t c\_phy

**Definition** hci\_types.h:2870

[bt\_hci\_evt\_le\_cis\_established::nse](structbt__hci__evt__le__cis__established.md#a683856418764b1110d5c5fea0494fe1e)

uint8\_t nse

**Definition** hci\_types.h:2872

[bt\_hci\_evt\_le\_cis\_established::c\_latency](structbt__hci__evt__le__cis__established.md#a877913bb4b9016c64793458de94d84a0)

uint8\_t c\_latency[3]

**Definition** hci\_types.h:2868

[bt\_hci\_evt\_le\_cis\_established::conn\_handle](structbt__hci__evt__le__cis__established.md#a932e8df0222eb3bcf7bee753414d529e)

uint16\_t conn\_handle

**Definition** hci\_types.h:2865

[bt\_hci\_evt\_le\_cis\_established::c\_bn](structbt__hci__evt__le__cis__established.md#ab6b2d892e3c1e4f6aedee722049b75d3)

uint8\_t c\_bn

**Definition** hci\_types.h:2873

[bt\_hci\_evt\_le\_cis\_established::cig\_sync\_delay](structbt__hci__evt__le__cis__established.md#ac4e5a2535e3e8d3782adac63a4c5a8d9)

uint8\_t cig\_sync\_delay[3]

**Definition** hci\_types.h:2866

[bt\_hci\_evt\_le\_cis\_established::p\_bn](structbt__hci__evt__le__cis__established.md#ad0a79bfadd413bf572b697069695c0a5)

uint8\_t p\_bn

**Definition** hci\_types.h:2874

[bt\_hci\_evt\_le\_cis\_established::c\_ft](structbt__hci__evt__le__cis__established.md#ad0f3bd5f81b660afbc4927a777c2c18e)

uint8\_t c\_ft

**Definition** hci\_types.h:2875

[bt\_hci\_evt\_le\_cis\_established::cis\_sync\_delay](structbt__hci__evt__le__cis__established.md#ae71d6753849ae3c57327c8763cab1802)

uint8\_t cis\_sync\_delay[3]

**Definition** hci\_types.h:2867

[bt\_hci\_evt\_le\_cis\_established::p\_max\_pdu](structbt__hci__evt__le__cis__established.md#ae8b195f433570e28e42a5f9d321964de)

uint16\_t p\_max\_pdu

**Definition** hci\_types.h:2878

[bt\_hci\_evt\_le\_cis\_established::c\_max\_pdu](structbt__hci__evt__le__cis__established.md#ae9fdecff4342f25de30165a4531ad703)

uint16\_t c\_max\_pdu

**Definition** hci\_types.h:2877

[bt\_hci\_evt\_le\_cis\_established::p\_latency](structbt__hci__evt__le__cis__established.md#aefb2d4e0458cbe990903a9f449189c30)

uint8\_t p\_latency[3]

**Definition** hci\_types.h:2869

[bt\_hci\_evt\_le\_cis\_req](structbt__hci__evt__le__cis__req.md)

**Definition** hci\_types.h:2883

[bt\_hci\_evt\_le\_cis\_req::cis\_id](structbt__hci__evt__le__cis__req.md#abdf99eeb7a30c8238bbabdcd60a4847a)

uint8\_t cis\_id

**Definition** hci\_types.h:2887

[bt\_hci\_evt\_le\_cis\_req::cig\_id](structbt__hci__evt__le__cis__req.md#ae0ef0ac224bde55de13df4e5eeaf26be)

uint8\_t cig\_id

**Definition** hci\_types.h:2886

[bt\_hci\_evt\_le\_cis\_req::cis\_handle](structbt__hci__evt__le__cis__req.md#aeed6f4bf58cdb301d6b784a202722acc)

uint16\_t cis\_handle

**Definition** hci\_types.h:2885

[bt\_hci\_evt\_le\_cis\_req::acl\_handle](structbt__hci__evt__le__cis__req.md#af8529013adb87340298a89d4727e6867)

uint16\_t acl\_handle

**Definition** hci\_types.h:2884

[bt\_hci\_evt\_le\_conn\_complete](structbt__hci__evt__le__conn__complete.md)

**Definition** hci\_types.h:2596

[bt\_hci\_evt\_le\_conn\_complete::clock\_accuracy](structbt__hci__evt__le__conn__complete.md#a3fff4c3b30da5922f75d36d97fdeee33)

uint8\_t clock\_accuracy

**Definition** hci\_types.h:2604

[bt\_hci\_evt\_le\_conn\_complete::supv\_timeout](structbt__hci__evt__le__conn__complete.md#a4a90c9824d167b6c45b301e18bfe7f17)

uint16\_t supv\_timeout

**Definition** hci\_types.h:2603

[bt\_hci\_evt\_le\_conn\_complete::handle](structbt__hci__evt__le__conn__complete.md#a67618a1efa0149fadc1063a719d5b674)

uint16\_t handle

**Definition** hci\_types.h:2598

[bt\_hci\_evt\_le\_conn\_complete::role](structbt__hci__evt__le__conn__complete.md#a8455e714d4333d90c2f117892f3dcd6f)

uint8\_t role

**Definition** hci\_types.h:2599

[bt\_hci\_evt\_le\_conn\_complete::status](structbt__hci__evt__le__conn__complete.md#a897981117139c0e53ea7275b689f3799)

uint8\_t status

**Definition** hci\_types.h:2597

[bt\_hci\_evt\_le\_conn\_complete::peer\_addr](structbt__hci__evt__le__conn__complete.md#a97e1aaa10832292ddfe4ee6731ef8999)

bt\_addr\_le\_t peer\_addr

**Definition** hci\_types.h:2600

[bt\_hci\_evt\_le\_conn\_complete::latency](structbt__hci__evt__le__conn__complete.md#ab60cb42ecc83632c61656cd352b71cbe)

uint16\_t latency

**Definition** hci\_types.h:2602

[bt\_hci\_evt\_le\_conn\_complete::interval](structbt__hci__evt__le__conn__complete.md#abe4bc0407d0295329631cb14672a7ee7)

uint16\_t interval

**Definition** hci\_types.h:2601

[bt\_hci\_evt\_le\_conn\_param\_req](structbt__hci__evt__le__conn__param__req.md)

**Definition** hci\_types.h:2645

[bt\_hci\_evt\_le\_conn\_param\_req::interval\_max](structbt__hci__evt__le__conn__param__req.md#a0ed70d1a89f270073f78823d38af6ac9)

uint16\_t interval\_max

**Definition** hci\_types.h:2648

[bt\_hci\_evt\_le\_conn\_param\_req::handle](structbt__hci__evt__le__conn__param__req.md#a4746a001a070f152a3c1c870a7e74df1)

uint16\_t handle

**Definition** hci\_types.h:2646

[bt\_hci\_evt\_le\_conn\_param\_req::interval\_min](structbt__hci__evt__le__conn__param__req.md#a9a9dfc026feb46337b0a36920204b24e)

uint16\_t interval\_min

**Definition** hci\_types.h:2647

[bt\_hci\_evt\_le\_conn\_param\_req::latency](structbt__hci__evt__le__conn__param__req.md#a9f61f0a3e6b6d2e2c6af2f4aef625b75)

uint16\_t latency

**Definition** hci\_types.h:2649

[bt\_hci\_evt\_le\_conn\_param\_req::timeout](structbt__hci__evt__le__conn__param__req.md#ae34de4a3d3e3e4686391eb9d9585dc87)

uint16\_t timeout

**Definition** hci\_types.h:2650

[bt\_hci\_evt\_le\_conn\_update\_complete](structbt__hci__evt__le__conn__update__complete.md)

**Definition** hci\_types.h:2622

[bt\_hci\_evt\_le\_conn\_update\_complete::interval](structbt__hci__evt__le__conn__update__complete.md#a69aa00c0c50978b2aa620aad671119f3)

uint16\_t interval

**Definition** hci\_types.h:2625

[bt\_hci\_evt\_le\_conn\_update\_complete::handle](structbt__hci__evt__le__conn__update__complete.md#a81c0688a5e3b4b3a4d92fbc756a068d5)

uint16\_t handle

**Definition** hci\_types.h:2624

[bt\_hci\_evt\_le\_conn\_update\_complete::supv\_timeout](structbt__hci__evt__le__conn__update__complete.md#aca728975619a10a6e3280b127b59f2f1)

uint16\_t supv\_timeout

**Definition** hci\_types.h:2627

[bt\_hci\_evt\_le\_conn\_update\_complete::status](structbt__hci__evt__le__conn__update__complete.md#ad428bd5e29d40f7551ccdd0747e429d6)

uint8\_t status

**Definition** hci\_types.h:2623

[bt\_hci\_evt\_le\_conn\_update\_complete::latency](structbt__hci__evt__le__conn__update__complete.md#ade2421709a35e0cd0fce3a4d992470c3)

uint16\_t latency

**Definition** hci\_types.h:2626

[bt\_hci\_evt\_le\_connection\_iq\_report](structbt__hci__evt__le__connection__iq__report.md)

**Definition** hci\_types.h:2822

[bt\_hci\_evt\_le\_connection\_iq\_report::cte\_type](structbt__hci__evt__le__connection__iq__report.md#a0188ce28a6c0a2002ae2c64a7bd95e52)

uint8\_t cte\_type

**Definition** hci\_types.h:2828

[bt\_hci\_evt\_le\_connection\_iq\_report::rssi\_ant\_id](structbt__hci__evt__le__connection__iq__report.md#a135498a4abae604967f94840e2f88d2c)

uint8\_t rssi\_ant\_id

**Definition** hci\_types.h:2827

[bt\_hci\_evt\_le\_connection\_iq\_report::conn\_evt\_counter](structbt__hci__evt__le__connection__iq__report.md#a1f388ba96bd52f9ce0f68bacb2945ed8)

uint16\_t conn\_evt\_counter

**Definition** hci\_types.h:2831

[bt\_hci\_evt\_le\_connection\_iq\_report::conn\_handle](structbt__hci__evt__le__connection__iq__report.md#a446f4eab3db19452a84023a676333d1d)

uint16\_t conn\_handle

**Definition** hci\_types.h:2823

[bt\_hci\_evt\_le\_connection\_iq\_report::rssi](structbt__hci__evt__le__connection__iq__report.md#a49e63523f7219174540666c7e5ab3550)

int16\_t rssi

**Definition** hci\_types.h:2826

[bt\_hci\_evt\_le\_connection\_iq\_report::sample](structbt__hci__evt__le__connection__iq__report.md#a5acc2683312523a1137db7897a7373a6)

struct bt\_hci\_le\_iq\_sample sample[0]

**Definition** hci\_types.h:2833

[bt\_hci\_evt\_le\_connection\_iq\_report::slot\_durations](structbt__hci__evt__le__connection__iq__report.md#a74670ca77bb2be81db2cee613dd9c82b)

uint8\_t slot\_durations

**Definition** hci\_types.h:2829

[bt\_hci\_evt\_le\_connection\_iq\_report::sample\_count](structbt__hci__evt__le__connection__iq__report.md#a801dd9373935ba06175ac52237fea759)

uint8\_t sample\_count

**Definition** hci\_types.h:2832

[bt\_hci\_evt\_le\_connection\_iq\_report::rx\_phy](structbt__hci__evt__le__connection__iq__report.md#aa052e03491647acc9f7a6dc7d91cedcc)

uint8\_t rx\_phy

**Definition** hci\_types.h:2824

[bt\_hci\_evt\_le\_connection\_iq\_report::data\_chan\_idx](structbt__hci__evt__le__connection__iq__report.md#ac01a14c591c8bd8e6313aff021ca8d61)

uint8\_t data\_chan\_idx

**Definition** hci\_types.h:2825

[bt\_hci\_evt\_le\_connection\_iq\_report::packet\_status](structbt__hci__evt__le__connection__iq__report.md#af66e8f09a4442b658b80a6eb4dd3064b)

uint8\_t packet\_status

**Definition** hci\_types.h:2830

[bt\_hci\_evt\_le\_connectionless\_iq\_report](structbt__hci__evt__le__connectionless__iq__report.md)

**Definition** hci\_types.h:2808

[bt\_hci\_evt\_le\_connectionless\_iq\_report::rssi](structbt__hci__evt__le__connectionless__iq__report.md#a09112f3711aca00b56045c46958c0992)

int16\_t rssi

**Definition** hci\_types.h:2811

[bt\_hci\_evt\_le\_connectionless\_iq\_report::sample](structbt__hci__evt__le__connectionless__iq__report.md#a1a81f2c8653d85dc29582eed67b4a2a8)

struct bt\_hci\_le\_iq\_sample sample[0]

**Definition** hci\_types.h:2818

[bt\_hci\_evt\_le\_connectionless\_iq\_report::sync\_handle](structbt__hci__evt__le__connectionless__iq__report.md#a36f853d29b8dae1dd393546bbdec5ae2)

uint16\_t sync\_handle

**Definition** hci\_types.h:2809

[bt\_hci\_evt\_le\_connectionless\_iq\_report::sample\_count](structbt__hci__evt__le__connectionless__iq__report.md#a39109ea3f657d0566a73c7ca81bdd2b1)

uint8\_t sample\_count

**Definition** hci\_types.h:2817

[bt\_hci\_evt\_le\_connectionless\_iq\_report::cte\_type](structbt__hci__evt__le__connectionless__iq__report.md#a6b11b00199b002129c569cfec6e83174)

uint8\_t cte\_type

**Definition** hci\_types.h:2813

[bt\_hci\_evt\_le\_connectionless\_iq\_report::slot\_durations](structbt__hci__evt__le__connectionless__iq__report.md#a9d9f0cfe343d81c44e8342b81e2a0608)

uint8\_t slot\_durations

**Definition** hci\_types.h:2814

[bt\_hci\_evt\_le\_connectionless\_iq\_report::packet\_status](structbt__hci__evt__le__connectionless__iq__report.md#ab6fb0f6e32e32a3364ae79d867d9e640)

uint8\_t packet\_status

**Definition** hci\_types.h:2815

[bt\_hci\_evt\_le\_connectionless\_iq\_report::per\_evt\_counter](structbt__hci__evt__le__connectionless__iq__report.md#abfeb0aaa411464bbd7bca927219144fb)

uint16\_t per\_evt\_counter

**Definition** hci\_types.h:2816

[bt\_hci\_evt\_le\_connectionless\_iq\_report::chan\_idx](structbt__hci__evt__le__connectionless__iq__report.md#af50e710884a17191d22f652eaf5788fd)

uint8\_t chan\_idx

**Definition** hci\_types.h:2810

[bt\_hci\_evt\_le\_connectionless\_iq\_report::rssi\_ant\_id](structbt__hci__evt__le__connectionless__iq__report.md#af8c2055666a97f3c8d95747c59515c31)

uint8\_t rssi\_ant\_id

**Definition** hci\_types.h:2812

[bt\_hci\_evt\_le\_cte\_req\_failed](structbt__hci__evt__le__cte__req__failed.md)

**Definition** hci\_types.h:2839

[bt\_hci\_evt\_le\_cte\_req\_failed::status](structbt__hci__evt__le__cte__req__failed.md#a1433f25dee38014dbd2d061b6d75741a)

uint8\_t status

**Definition** hci\_types.h:2845

[bt\_hci\_evt\_le\_cte\_req\_failed::conn\_handle](structbt__hci__evt__le__cte__req__failed.md#aa903954fa411e4ae49a613b4e76219dc)

uint16\_t conn\_handle

**Definition** hci\_types.h:2846

[bt\_hci\_evt\_le\_data\_len\_change](structbt__hci__evt__le__data__len__change.md)

**Definition** hci\_types.h:2654

[bt\_hci\_evt\_le\_data\_len\_change::max\_rx\_octets](structbt__hci__evt__le__data__len__change.md#a60ecd89a8bbf06ae55b577e3d708d16f)

uint16\_t max\_rx\_octets

**Definition** hci\_types.h:2658

[bt\_hci\_evt\_le\_data\_len\_change::handle](structbt__hci__evt__le__data__len__change.md#a62ebc2f337f23f678c651bf3a276a2a7)

uint16\_t handle

**Definition** hci\_types.h:2655

[bt\_hci\_evt\_le\_data\_len\_change::max\_tx\_time](structbt__hci__evt__le__data__len__change.md#a8264e7ec4aa37e9a699f81d0c56afa40)

uint16\_t max\_tx\_time

**Definition** hci\_types.h:2657

[bt\_hci\_evt\_le\_data\_len\_change::max\_rx\_time](structbt__hci__evt__le__data__len__change.md#a90771e400b998565e7a8bbf4288edd01)

uint16\_t max\_rx\_time

**Definition** hci\_types.h:2659

[bt\_hci\_evt\_le\_data\_len\_change::max\_tx\_octets](structbt__hci__evt__le__data__len__change.md#ae5ce481170336acafbe85687c672281b)

uint16\_t max\_tx\_octets

**Definition** hci\_types.h:2656

[bt\_hci\_evt\_le\_direct\_adv\_info](structbt__hci__evt__le__direct__adv__info.md)

**Definition** hci\_types.h:2689

[bt\_hci\_evt\_le\_direct\_adv\_info::rssi](structbt__hci__evt__le__direct__adv__info.md#a013e5d53ed53e4cd0b923a55c68e20bc)

int8\_t rssi

**Definition** hci\_types.h:2693

[bt\_hci\_evt\_le\_direct\_adv\_info::addr](structbt__hci__evt__le__direct__adv__info.md#a66bbb3e53d84e8c39b216edf91ad131d)

bt\_addr\_le\_t addr

**Definition** hci\_types.h:2691

[bt\_hci\_evt\_le\_direct\_adv\_info::dir\_addr](structbt__hci__evt__le__direct__adv__info.md#ad4ca2d5395bc4c5b95527ac1491c940e)

bt\_addr\_le\_t dir\_addr

**Definition** hci\_types.h:2692

[bt\_hci\_evt\_le\_direct\_adv\_info::evt\_type](structbt__hci__evt__le__direct__adv__info.md#aed957c96860c5f92f9485ab743ce832b)

uint8\_t evt\_type

**Definition** hci\_types.h:2690

[bt\_hci\_evt\_le\_direct\_adv\_report](structbt__hci__evt__le__direct__adv__report.md)

**Definition** hci\_types.h:2695

[bt\_hci\_evt\_le\_direct\_adv\_report::direct\_adv\_info](structbt__hci__evt__le__direct__adv__report.md#a82800d58d4c3ed1fca49b6575bd8f957)

struct bt\_hci\_evt\_le\_direct\_adv\_info direct\_adv\_info[0]

**Definition** hci\_types.h:2697

[bt\_hci\_evt\_le\_direct\_adv\_report::num\_reports](structbt__hci__evt__le__direct__adv__report.md#ae8d1f96739c8fda8827d1c0521f00f94)

uint8\_t num\_reports

**Definition** hci\_types.h:2696

[bt\_hci\_evt\_le\_enh\_conn\_complete\_v2](structbt__hci__evt__le__enh__conn__complete__v2.md)

**Definition** hci\_types.h:2500

[bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::peer\_rpa](structbt__hci__evt__le__enh__conn__complete__v2.md#a014e8bf891684c4cd9e5ec53d986d412)

bt\_addr\_t peer\_rpa

**Definition** hci\_types.h:2506

[bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::local\_rpa](structbt__hci__evt__le__enh__conn__complete__v2.md#a10a1cbf0e9e21bc127dc64adadd53773)

bt\_addr\_t local\_rpa

**Definition** hci\_types.h:2505

[bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::interval](structbt__hci__evt__le__enh__conn__complete__v2.md#a237b8313970cc63b7e57c0ce4913392e)

uint16\_t interval

**Definition** hci\_types.h:2507

[bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::supv\_timeout](structbt__hci__evt__le__enh__conn__complete__v2.md#a2b2ac4890eb9604a3f5cd40f55c2c066)

uint16\_t supv\_timeout

**Definition** hci\_types.h:2509

[bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::role](structbt__hci__evt__le__enh__conn__complete__v2.md#a3343de57a24fa2ebdccf9411f388817d)

uint8\_t role

**Definition** hci\_types.h:2503

[bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::latency](structbt__hci__evt__le__enh__conn__complete__v2.md#a3daa32ac19c4eda4a49bebb64f3145be)

uint16\_t latency

**Definition** hci\_types.h:2508

[bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::clock\_accuracy](structbt__hci__evt__le__enh__conn__complete__v2.md#a7bb168061803d1122e8ee47dc8af3ae9)

uint8\_t clock\_accuracy

**Definition** hci\_types.h:2510

[bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::peer\_addr](structbt__hci__evt__le__enh__conn__complete__v2.md#a7df28c9ddec607d5a84572bb421b7f5a)

bt\_addr\_le\_t peer\_addr

**Definition** hci\_types.h:2504

[bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::sync\_handle](structbt__hci__evt__le__enh__conn__complete__v2.md#a81dca94a6f2a8ea3da7a5a316daa5941)

uint16\_t sync\_handle

**Definition** hci\_types.h:2512

[bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::adv\_handle](structbt__hci__evt__le__enh__conn__complete__v2.md#a883ba3aed9aed00ec0ce425999d97180)

uint8\_t adv\_handle

**Definition** hci\_types.h:2511

[bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::status](structbt__hci__evt__le__enh__conn__complete__v2.md#ad72ba07d766135a94474a9d004da1a66)

uint8\_t status

**Definition** hci\_types.h:2501

[bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::handle](structbt__hci__evt__le__enh__conn__complete__v2.md#affe2dba0634e0215579fb13d77016a8c)

uint16\_t handle

**Definition** hci\_types.h:2502

[bt\_hci\_evt\_le\_enh\_conn\_complete](structbt__hci__evt__le__enh__conn__complete.md)

**Definition** hci\_types.h:2675

[bt\_hci\_evt\_le\_enh\_conn\_complete::handle](structbt__hci__evt__le__enh__conn__complete.md#a13ceff445de6a89f6ea0e832e8b3fba9)

uint16\_t handle

**Definition** hci\_types.h:2677

[bt\_hci\_evt\_le\_enh\_conn\_complete::peer\_addr](structbt__hci__evt__le__enh__conn__complete.md#a4906d6991489e95f8c74aacf5ad8c22e)

bt\_addr\_le\_t peer\_addr

**Definition** hci\_types.h:2679

[bt\_hci\_evt\_le\_enh\_conn\_complete::peer\_rpa](structbt__hci__evt__le__enh__conn__complete.md#a4ece4379733f1ab404fa03f4794192a4)

bt\_addr\_t peer\_rpa

**Definition** hci\_types.h:2681

[bt\_hci\_evt\_le\_enh\_conn\_complete::clock\_accuracy](structbt__hci__evt__le__enh__conn__complete.md#a5641e5cb17df4613cd85f5ad3ba8541c)

uint8\_t clock\_accuracy

**Definition** hci\_types.h:2685

[bt\_hci\_evt\_le\_enh\_conn\_complete::latency](structbt__hci__evt__le__enh__conn__complete.md#a7276bf433c21ffcd3582463492af107b)

uint16\_t latency

**Definition** hci\_types.h:2683

[bt\_hci\_evt\_le\_enh\_conn\_complete::supv\_timeout](structbt__hci__evt__le__enh__conn__complete.md#aa99df131f3fb0330ff8051015d2b78dc)

uint16\_t supv\_timeout

**Definition** hci\_types.h:2684

[bt\_hci\_evt\_le\_enh\_conn\_complete::local\_rpa](structbt__hci__evt__le__enh__conn__complete.md#ab275bcb4a3dd09525b446c01e4e5fdad)

bt\_addr\_t local\_rpa

**Definition** hci\_types.h:2680

[bt\_hci\_evt\_le\_enh\_conn\_complete::interval](structbt__hci__evt__le__enh__conn__complete.md#ac0565ecf0c459275d147933bbdaa9fbc)

uint16\_t interval

**Definition** hci\_types.h:2682

[bt\_hci\_evt\_le\_enh\_conn\_complete::status](structbt__hci__evt__le__enh__conn__complete.md#ae26575416658bf285c45f57ddf426eb2)

uint8\_t status

**Definition** hci\_types.h:2676

[bt\_hci\_evt\_le\_enh\_conn\_complete::role](structbt__hci__evt__le__enh__conn__complete.md#af24298f8c1d58882b4962a14086fc5c7)

uint8\_t role

**Definition** hci\_types.h:2678

[bt\_hci\_evt\_le\_ext\_advertising\_info](structbt__hci__evt__le__ext__advertising__info.md)

**Definition** hci\_types.h:2722

[bt\_hci\_evt\_le\_ext\_advertising\_info::evt\_type](structbt__hci__evt__le__ext__advertising__info.md#a040c27dbcb337162f7ca857b8cb84cfe)

uint16\_t evt\_type

**Definition** hci\_types.h:2723

[bt\_hci\_evt\_le\_ext\_advertising\_info::prim\_phy](structbt__hci__evt__le__ext__advertising__info.md#a088f0e6ea0dfbad25d5f72d0741f7d6d)

uint8\_t prim\_phy

**Definition** hci\_types.h:2725

[bt\_hci\_evt\_le\_ext\_advertising\_info::length](structbt__hci__evt__le__ext__advertising__info.md#a20ca10813f6b3aaba2756a5fe00d3878)

uint8\_t length

**Definition** hci\_types.h:2732

[bt\_hci\_evt\_le\_ext\_advertising\_info::direct\_addr](structbt__hci__evt__le__ext__advertising__info.md#a37f4e4981566b43d6e7c7dfffc5b13fb)

bt\_addr\_le\_t direct\_addr

**Definition** hci\_types.h:2731

[bt\_hci\_evt\_le\_ext\_advertising\_info::tx\_power](structbt__hci__evt__le__ext__advertising__info.md#a39217e77e495e8c4c6288917f8e4d2dc)

int8\_t tx\_power

**Definition** hci\_types.h:2728

[bt\_hci\_evt\_le\_ext\_advertising\_info::sid](structbt__hci__evt__le__ext__advertising__info.md#a5b4d4adff4d97c06311a76abd9847727)

uint8\_t sid

**Definition** hci\_types.h:2727

[bt\_hci\_evt\_le\_ext\_advertising\_info::rssi](structbt__hci__evt__le__ext__advertising__info.md#a6213edbc3ae30f02a6bf2d8e069cd035)

int8\_t rssi

**Definition** hci\_types.h:2729

[bt\_hci\_evt\_le\_ext\_advertising\_info::interval](structbt__hci__evt__le__ext__advertising__info.md#a7da4e49c49eccbf009491bb7da01e111)

uint16\_t interval

**Definition** hci\_types.h:2730

[bt\_hci\_evt\_le\_ext\_advertising\_info::data](structbt__hci__evt__le__ext__advertising__info.md#a9e5536277b0132c8374147677a787b68)

uint8\_t data[0]

**Definition** hci\_types.h:2733

[bt\_hci\_evt\_le\_ext\_advertising\_info::addr](structbt__hci__evt__le__ext__advertising__info.md#acec6858e41ae1b44a2a2ee6d6dbc294d)

bt\_addr\_le\_t addr

**Definition** hci\_types.h:2724

[bt\_hci\_evt\_le\_ext\_advertising\_info::sec\_phy](structbt__hci__evt__le__ext__advertising__info.md#af4d863e12e6f8f19426a14af292fa6d2)

uint8\_t sec\_phy

**Definition** hci\_types.h:2726

[bt\_hci\_evt\_le\_ext\_advertising\_report](structbt__hci__evt__le__ext__advertising__report.md)

**Definition** hci\_types.h:2735

[bt\_hci\_evt\_le\_ext\_advertising\_report::num\_reports](structbt__hci__evt__le__ext__advertising__report.md#a72fc9736934b415e88c51a1f96179871)

uint8\_t num\_reports

**Definition** hci\_types.h:2736

[bt\_hci\_evt\_le\_ext\_advertising\_report::adv\_info](structbt__hci__evt__le__ext__advertising__report.md#a84b9c47a79ccea04198721e2f05ac1a8)

struct bt\_hci\_evt\_le\_ext\_advertising\_info adv\_info[0]

**Definition** hci\_types.h:2737

[bt\_hci\_evt\_le\_generate\_dhkey\_complete](structbt__hci__evt__le__generate__dhkey__complete.md)

**Definition** hci\_types.h:2669

[bt\_hci\_evt\_le\_generate\_dhkey\_complete::status](structbt__hci__evt__le__generate__dhkey__complete.md#a3d10643dd45a71b71d35dfa455ed8590)

uint8\_t status

**Definition** hci\_types.h:2670

[bt\_hci\_evt\_le\_generate\_dhkey\_complete::dhkey](structbt__hci__evt__le__generate__dhkey__complete.md#a8cd8ece786c1443ed43bd3b8fcd4d9bf)

uint8\_t dhkey[32]

**Definition** hci\_types.h:2671

[bt\_hci\_evt\_le\_ltk\_request](structbt__hci__evt__le__ltk__request.md)

**Definition** hci\_types.h:2638

[bt\_hci\_evt\_le\_ltk\_request::ediv](structbt__hci__evt__le__ltk__request.md#a54d5cbde249349337595085c6c3cabad)

uint16\_t ediv

**Definition** hci\_types.h:2641

[bt\_hci\_evt\_le\_ltk\_request::rand](structbt__hci__evt__le__ltk__request.md#a765cba614cd7a972156b6361536b753f)

uint64\_t rand

**Definition** hci\_types.h:2640

[bt\_hci\_evt\_le\_ltk\_request::handle](structbt__hci__evt__le__ltk__request.md#aed00ae384cb7d0deace8d0cc0f8e0068)

uint16\_t handle

**Definition** hci\_types.h:2639

[bt\_hci\_evt\_le\_meta\_event](structbt__hci__evt__le__meta__event.md)

**Definition** hci\_types.h:2583

[bt\_hci\_evt\_le\_meta\_event::subevent](structbt__hci__evt__le__meta__event.md#a536464a525f8d0f9df915be5ee3d33da)

uint8\_t subevent

**Definition** hci\_types.h:2584

[bt\_hci\_evt\_le\_p256\_public\_key\_complete](structbt__hci__evt__le__p256__public__key__complete.md)

**Definition** hci\_types.h:2663

[bt\_hci\_evt\_le\_p256\_public\_key\_complete::status](structbt__hci__evt__le__p256__public__key__complete.md#a57d51fca3a707b445db2534d1e175241)

uint8\_t status

**Definition** hci\_types.h:2664

[bt\_hci\_evt\_le\_p256\_public\_key\_complete::key](structbt__hci__evt__le__p256__public__key__complete.md#af482f81d438b878fb826edbac8d84833)

uint8\_t key[64]

**Definition** hci\_types.h:2665

[bt\_hci\_evt\_le\_past\_received\_v2](structbt__hci__evt__le__past__received__v2.md)

**Definition** hci\_types.h:2456

[bt\_hci\_evt\_le\_past\_received\_v2::sync\_handle](structbt__hci__evt__le__past__received__v2.md#a00bf4bdf12fce6cbf2874b9c4ae09f9f)

uint16\_t sync\_handle

**Definition** hci\_types.h:2460

[bt\_hci\_evt\_le\_past\_received\_v2::adv\_sid](structbt__hci__evt__le__past__received__v2.md#a05d798c9415541ef7f5716992157b1a1)

uint8\_t adv\_sid

**Definition** hci\_types.h:2461

[bt\_hci\_evt\_le\_past\_received\_v2::interval](structbt__hci__evt__le__past__received__v2.md#a736af2c2ee0afd3cb00e8eb4d103991c)

uint16\_t interval

**Definition** hci\_types.h:2464

[bt\_hci\_evt\_le\_past\_received\_v2::clock\_accuracy](structbt__hci__evt__le__past__received__v2.md#a78853d14c3bf9a9aba3c4e15b2e06abb)

uint8\_t clock\_accuracy

**Definition** hci\_types.h:2465

[bt\_hci\_evt\_le\_past\_received\_v2::response\_slot\_delay](structbt__hci__evt__le__past__received__v2.md#a9f55d5f6d17d11e72f7cac363a69fe97)

uint8\_t response\_slot\_delay

**Definition** hci\_types.h:2468

[bt\_hci\_evt\_le\_past\_received\_v2::num\_subevents](structbt__hci__evt__le__past__received__v2.md#ab8a2a55fe071218284d60f1a2896945b)

uint8\_t num\_subevents

**Definition** hci\_types.h:2466

[bt\_hci\_evt\_le\_past\_received\_v2::response\_slot\_spacing](structbt__hci__evt__le__past__received__v2.md#acf711399e575295dcef73cfeeb844eab)

uint8\_t response\_slot\_spacing

**Definition** hci\_types.h:2469

[bt\_hci\_evt\_le\_past\_received\_v2::service\_data](structbt__hci__evt__le__past__received__v2.md#acffc2fa22a16a3a12a4f7dfc3bb45866)

uint16\_t service\_data

**Definition** hci\_types.h:2459

[bt\_hci\_evt\_le\_past\_received\_v2::conn\_handle](structbt__hci__evt__le__past__received__v2.md#adb011949f592ec7f8843d4fd47eca2e9)

uint16\_t conn\_handle

**Definition** hci\_types.h:2458

[bt\_hci\_evt\_le\_past\_received\_v2::phy](structbt__hci__evt__le__past__received__v2.md#ae7a73293519ab45aec40a9a1aeaa4e89)

uint8\_t phy

**Definition** hci\_types.h:2463

[bt\_hci\_evt\_le\_past\_received\_v2::subevent\_interval](structbt__hci__evt__le__past__received__v2.md#aefdc5ac7ef125f4dc5865c198b98c67d)

uint8\_t subevent\_interval

**Definition** hci\_types.h:2467

[bt\_hci\_evt\_le\_past\_received\_v2::status](structbt__hci__evt__le__past__received__v2.md#aefe79f973eda8c7c5670c7a721d55d8a)

uint8\_t status

**Definition** hci\_types.h:2457

[bt\_hci\_evt\_le\_past\_received\_v2::addr](structbt__hci__evt__le__past__received__v2.md#aff78554e8980635290767e9877ac479b)

bt\_addr\_le\_t addr

**Definition** hci\_types.h:2462

[bt\_hci\_evt\_le\_past\_received](structbt__hci__evt__le__past__received.md)

**Definition** hci\_types.h:2850

[bt\_hci\_evt\_le\_past\_received::clock\_accuracy](structbt__hci__evt__le__past__received.md#a00d570636a55c1d84723ad3bc5705d80)

uint8\_t clock\_accuracy

**Definition** hci\_types.h:2859

[bt\_hci\_evt\_le\_past\_received::adv\_sid](structbt__hci__evt__le__past__received.md#a110c7cdd2ff1178d1ca686abaae92b05)

uint8\_t adv\_sid

**Definition** hci\_types.h:2855

[bt\_hci\_evt\_le\_past\_received::status](structbt__hci__evt__le__past__received.md#a1b2c229c99d06f44057b88458f168e7c)

uint8\_t status

**Definition** hci\_types.h:2851

[bt\_hci\_evt\_le\_past\_received::conn\_handle](structbt__hci__evt__le__past__received.md#a1bdbaddb4003cea40738ee540ecb8789)

uint16\_t conn\_handle

**Definition** hci\_types.h:2852

[bt\_hci\_evt\_le\_past\_received::sync\_handle](structbt__hci__evt__le__past__received.md#a2cea2f3b9d51ace91ddf63639e821328)

uint16\_t sync\_handle

**Definition** hci\_types.h:2854

[bt\_hci\_evt\_le\_past\_received::addr](structbt__hci__evt__le__past__received.md#a3e368e95a6831f823d2efa0c0bc1ef51)

bt\_addr\_le\_t addr

**Definition** hci\_types.h:2856

[bt\_hci\_evt\_le\_past\_received::interval](structbt__hci__evt__le__past__received.md#a41ea6099d3cca1caf37ff518a4e95492)

uint16\_t interval

**Definition** hci\_types.h:2858

[bt\_hci\_evt\_le\_past\_received::service\_data](structbt__hci__evt__le__past__received.md#adaa1e432db60a2529ad6266f16604e15)

uint16\_t service\_data

**Definition** hci\_types.h:2853

[bt\_hci\_evt\_le\_past\_received::phy](structbt__hci__evt__le__past__received.md#aedb668e6f3232b1db9035ea89ccf1b71)

uint8\_t phy

**Definition** hci\_types.h:2857

[bt\_hci\_evt\_le\_per\_adv\_response\_report](structbt__hci__evt__le__per__adv__response__report.md)

**Definition** hci\_types.h:2491

[bt\_hci\_evt\_le\_per\_adv\_response\_report::num\_responses](structbt__hci__evt__le__per__adv__response__report.md#a37f3519eefe33e87d49c7c2ad0f8b40c)

uint8\_t num\_responses

**Definition** hci\_types.h:2495

[bt\_hci\_evt\_le\_per\_adv\_response\_report::responses](structbt__hci__evt__le__per__adv__response__report.md#a3b1bcca7a7dbc6fcf5709f6152268b87)

struct bt\_hci\_evt\_le\_per\_adv\_response responses[0]

**Definition** hci\_types.h:2496

[bt\_hci\_evt\_le\_per\_adv\_response\_report::tx\_status](structbt__hci__evt__le__per__adv__response__report.md#a46a5b74321a80697fd700a276be18ed3)

uint8\_t tx\_status

**Definition** hci\_types.h:2494

[bt\_hci\_evt\_le\_per\_adv\_response\_report::adv\_handle](structbt__hci__evt__le__per__adv__response__report.md#a9d746015a9c2b48c54008319c892b063)

uint8\_t adv\_handle

**Definition** hci\_types.h:2492

[bt\_hci\_evt\_le\_per\_adv\_response\_report::subevent](structbt__hci__evt__le__per__adv__response__report.md#ad4f8f61150f82f4ba420e3c0a1f333c2)

uint8\_t subevent

**Definition** hci\_types.h:2493

[bt\_hci\_evt\_le\_per\_adv\_response](structbt__hci__evt__le__per__adv__response.md)

**Definition** hci\_types.h:2481

[bt\_hci\_evt\_le\_per\_adv\_response::rssi](structbt__hci__evt__le__per__adv__response.md#a1100429baf398067a396a6ba8db6778a)

int8\_t rssi

**Definition** hci\_types.h:2483

[bt\_hci\_evt\_le\_per\_adv\_response::cte\_type](structbt__hci__evt__le__per__adv__response.md#a4197fbae54be038502312efc14b66320)

uint8\_t cte\_type

**Definition** hci\_types.h:2484

[bt\_hci\_evt\_le\_per\_adv\_response::tx\_power](structbt__hci__evt__le__per__adv__response.md#a74e304822ec7a431802cf8a7539d640e)

int8\_t tx\_power

**Definition** hci\_types.h:2482

[bt\_hci\_evt\_le\_per\_adv\_response::data\_status](structbt__hci__evt__le__per__adv__response.md#aa524756d2cce0718ecfd66704eaf389d)

uint8\_t data\_status

**Definition** hci\_types.h:2486

[bt\_hci\_evt\_le\_per\_adv\_response::response\_slot](structbt__hci__evt__le__per__adv__response.md#aa5b5467f4edd52fb8de078b0948141f0)

uint8\_t response\_slot

**Definition** hci\_types.h:2485

[bt\_hci\_evt\_le\_per\_adv\_response::data](structbt__hci__evt__le__per__adv__response.md#ace3b58eba63b55ce5f3038d4a7877ec2)

uint8\_t data[0]

**Definition** hci\_types.h:2488

[bt\_hci\_evt\_le\_per\_adv\_response::data\_length](structbt__hci__evt__le__per__adv__response.md#af68f0dc92118f78f6f5b0ffbf1854664)

uint8\_t data\_length

**Definition** hci\_types.h:2487

[bt\_hci\_evt\_le\_per\_adv\_subevent\_data\_request](structbt__hci__evt__le__per__adv__subevent__data__request.md)

**Definition** hci\_types.h:2473

[bt\_hci\_evt\_le\_per\_adv\_subevent\_data\_request::subevent\_data\_count](structbt__hci__evt__le__per__adv__subevent__data__request.md#a45cdb248b80602a7f14f24e0324e6f97)

uint8\_t subevent\_data\_count

**Definition** hci\_types.h:2476

[bt\_hci\_evt\_le\_per\_adv\_subevent\_data\_request::subevent\_start](structbt__hci__evt__le__per__adv__subevent__data__request.md#a8f7fd9b149aa52422cb3eb874b91943d)

uint8\_t subevent\_start

**Definition** hci\_types.h:2475

[bt\_hci\_evt\_le\_per\_adv\_subevent\_data\_request::adv\_handle](structbt__hci__evt__le__per__adv__subevent__data__request.md#ae6f6ef17edabfd210a7e6597087ff512)

uint8\_t adv\_handle

**Definition** hci\_types.h:2474

[bt\_hci\_evt\_le\_per\_adv\_sync\_established\_v2](structbt__hci__evt__le__per__adv__sync__established__v2.md)

**Definition** hci\_types.h:2428

[bt\_hci\_evt\_le\_per\_adv\_sync\_established\_v2::sid](structbt__hci__evt__le__per__adv__sync__established__v2.md#a0ce9a9170d93ff69f25ff35eb163511f)

uint8\_t sid

**Definition** hci\_types.h:2431

[bt\_hci\_evt\_le\_per\_adv\_sync\_established\_v2::clock\_accuracy](structbt__hci__evt__le__per__adv__sync__established__v2.md#a13ab0e87d6673a34e51f3112a5fd5a0c)

uint8\_t clock\_accuracy

**Definition** hci\_types.h:2435

[bt\_hci\_evt\_le\_per\_adv\_sync\_established\_v2::phy](structbt__hci__evt__le__per__adv__sync__established__v2.md#a36b5c8454ee3635d2298592c83166f14)

uint8\_t phy

**Definition** hci\_types.h:2433

[bt\_hci\_evt\_le\_per\_adv\_sync\_established\_v2::interval](structbt__hci__evt__le__per__adv__sync__established__v2.md#a958630cb9e275ab6f8ed0c548958e5ee)

uint16\_t interval

**Definition** hci\_types.h:2434

[bt\_hci\_evt\_le\_per\_adv\_sync\_established\_v2::status](structbt__hci__evt__le__per__adv__sync__established__v2.md#a96b975f5a2fcf193b0b58c230486ec36)

uint8\_t status

**Definition** hci\_types.h:2429

[bt\_hci\_evt\_le\_per\_adv\_sync\_established\_v2::response\_slot\_spacing](structbt__hci__evt__le__per__adv__sync__established__v2.md#aacb6946dbfeb2ffbc251910853559329)

uint8\_t response\_slot\_spacing

**Definition** hci\_types.h:2439

[bt\_hci\_evt\_le\_per\_adv\_sync\_established\_v2::handle](structbt__hci__evt__le__per__adv__sync__established__v2.md#ab7d3793e782d7b2bb311b8a5ac3a871b)

uint16\_t handle

**Definition** hci\_types.h:2430

[bt\_hci\_evt\_le\_per\_adv\_sync\_established\_v2::adv\_addr](structbt__hci__evt__le__per__adv__sync__established__v2.md#abd67ec989479eb793e7bf99a4cf371b8)

bt\_addr\_le\_t adv\_addr

**Definition** hci\_types.h:2432

[bt\_hci\_evt\_le\_per\_adv\_sync\_established\_v2::response\_slot\_delay](structbt__hci__evt__le__per__adv__sync__established__v2.md#ac4c2bc8789513692ce0f2cc81aa59476)

uint8\_t response\_slot\_delay

**Definition** hci\_types.h:2438

[bt\_hci\_evt\_le\_per\_adv\_sync\_established\_v2::subevent\_interval](structbt__hci__evt__le__per__adv__sync__established__v2.md#ad21df6269d8242d94ba9cbc1e0d4d344)

uint8\_t subevent\_interval

**Definition** hci\_types.h:2437

[bt\_hci\_evt\_le\_per\_adv\_sync\_established\_v2::num\_subevents](structbt__hci__evt__le__per__adv__sync__established__v2.md#af4fb92baa4f98c08c990ba505faf9226)

uint8\_t num\_subevents

**Definition** hci\_types.h:2436

[bt\_hci\_evt\_le\_per\_adv\_sync\_established](structbt__hci__evt__le__per__adv__sync__established.md)

**Definition** hci\_types.h:2741

[bt\_hci\_evt\_le\_per\_adv\_sync\_established::handle](structbt__hci__evt__le__per__adv__sync__established.md#a3af8529a858992f347ce9570c5696133)

uint16\_t handle

**Definition** hci\_types.h:2743

[bt\_hci\_evt\_le\_per\_adv\_sync\_established::interval](structbt__hci__evt__le__per__adv__sync__established.md#a4873b917a5bc140bb2f04ad2bee5dd69)

uint16\_t interval

**Definition** hci\_types.h:2747

[bt\_hci\_evt\_le\_per\_adv\_sync\_established::status](structbt__hci__evt__le__per__adv__sync__established.md#a9ebe918fee3121168dc5b45e64aaf263)

uint8\_t status

**Definition** hci\_types.h:2742

[bt\_hci\_evt\_le\_per\_adv\_sync\_established::sid](structbt__hci__evt__le__per__adv__sync__established.md#ab11929ef8d3c71c6f2cb7c549be21282)

uint8\_t sid

**Definition** hci\_types.h:2744

[bt\_hci\_evt\_le\_per\_adv\_sync\_established::phy](structbt__hci__evt__le__per__adv__sync__established.md#ab7ce6f56a69b54f02cde8fdae6860e42)

uint8\_t phy

**Definition** hci\_types.h:2746

[bt\_hci\_evt\_le\_per\_adv\_sync\_established::adv\_addr](structbt__hci__evt__le__per__adv__sync__established.md#adf65527ea968f4ece37d7e3c91c795d1)

bt\_addr\_le\_t adv\_addr

**Definition** hci\_types.h:2745

[bt\_hci\_evt\_le\_per\_adv\_sync\_established::clock\_accuracy](structbt__hci__evt__le__per__adv__sync__established.md#aee68069899cc10bc38ad9fb95cf9b7b7)

uint8\_t clock\_accuracy

**Definition** hci\_types.h:2748

[bt\_hci\_evt\_le\_per\_adv\_sync\_lost](structbt__hci__evt__le__per__adv__sync__lost.md)

**Definition** hci\_types.h:2763

[bt\_hci\_evt\_le\_per\_adv\_sync\_lost::handle](structbt__hci__evt__le__per__adv__sync__lost.md#a286d534634411da53a2bda8cdfb077f8)

uint16\_t handle

**Definition** hci\_types.h:2764

[bt\_hci\_evt\_le\_per\_advertising\_report\_v2](structbt__hci__evt__le__per__advertising__report__v2.md)

**Definition** hci\_types.h:2443

[bt\_hci\_evt\_le\_per\_advertising\_report\_v2::length](structbt__hci__evt__le__per__advertising__report__v2.md#a30f4e81346957ad4f9f0488dd93fafc3)

uint8\_t length

**Definition** hci\_types.h:2451

[bt\_hci\_evt\_le\_per\_advertising\_report\_v2::cte\_type](structbt__hci__evt__le__per__advertising__report__v2.md#a3276c2e11c946744b73426f54bf62b8c)

uint8\_t cte\_type

**Definition** hci\_types.h:2447

[bt\_hci\_evt\_le\_per\_advertising\_report\_v2::handle](structbt__hci__evt__le__per__advertising__report__v2.md#a34b15fb9b5b4f0d199ccf274dd489c6a)

uint16\_t handle

**Definition** hci\_types.h:2444

[bt\_hci\_evt\_le\_per\_advertising\_report\_v2::tx\_power](structbt__hci__evt__le__per__advertising__report__v2.md#a37a9eb7d417da9285e22cc7f83071c69)

int8\_t tx\_power

**Definition** hci\_types.h:2445

[bt\_hci\_evt\_le\_per\_advertising\_report\_v2::periodic\_event\_counter](structbt__hci__evt__le__per__advertising__report__v2.md#a499d82e1e3cfc501d399f570ebbcdc42)

uint16\_t periodic\_event\_counter

**Definition** hci\_types.h:2448

[bt\_hci\_evt\_le\_per\_advertising\_report\_v2::data\_status](structbt__hci__evt__le__per__advertising__report__v2.md#a73496cc962721538e27e9924fff0f3db)

uint8\_t data\_status

**Definition** hci\_types.h:2450

[bt\_hci\_evt\_le\_per\_advertising\_report\_v2::data](structbt__hci__evt__le__per__advertising__report__v2.md#a7af1cd4ec9df24e575a83a640eea36d2)

uint8\_t data[0]

**Definition** hci\_types.h:2452

[bt\_hci\_evt\_le\_per\_advertising\_report\_v2::rssi](structbt__hci__evt__le__per__advertising__report__v2.md#ad598ffd0108825803a4734959a354bd8)

int8\_t rssi

**Definition** hci\_types.h:2446

[bt\_hci\_evt\_le\_per\_advertising\_report\_v2::subevent](structbt__hci__evt__le__per__advertising__report__v2.md#af27b23fe38e9ff092d8839cd81749456)

uint8\_t subevent

**Definition** hci\_types.h:2449

[bt\_hci\_evt\_le\_per\_advertising\_report](structbt__hci__evt__le__per__advertising__report.md)

**Definition** hci\_types.h:2752

[bt\_hci\_evt\_le\_per\_advertising\_report::length](structbt__hci__evt__le__per__advertising__report.md#a0ab1d3c5d7eb1487862451cc65c66a76)

uint8\_t length

**Definition** hci\_types.h:2758

[bt\_hci\_evt\_le\_per\_advertising\_report::data](structbt__hci__evt__le__per__advertising__report.md#a1f9cdfc01e46e59e957b0c557bae620a)

uint8\_t data[0]

**Definition** hci\_types.h:2759

[bt\_hci\_evt\_le\_per\_advertising\_report::tx\_power](structbt__hci__evt__le__per__advertising__report.md#a3a09aca94284a9e4af765d4da543698e)

int8\_t tx\_power

**Definition** hci\_types.h:2754

[bt\_hci\_evt\_le\_per\_advertising\_report::cte\_type](structbt__hci__evt__le__per__advertising__report.md#aa683d1a4bd3a851f26b3028f566b76e4)

uint8\_t cte\_type

**Definition** hci\_types.h:2756

[bt\_hci\_evt\_le\_per\_advertising\_report::data\_status](structbt__hci__evt__le__per__advertising__report.md#abf23b23a12cbfeb7f996e71e2fe8b11c)

uint8\_t data\_status

**Definition** hci\_types.h:2757

[bt\_hci\_evt\_le\_per\_advertising\_report::handle](structbt__hci__evt__le__per__advertising__report.md#af81ce5bb18ef7fa1d94d00412886b081)

uint16\_t handle

**Definition** hci\_types.h:2753

[bt\_hci\_evt\_le\_per\_advertising\_report::rssi](structbt__hci__evt__le__per__advertising__report.md#af874c29b89326877b499f6be1052a626)

int8\_t rssi

**Definition** hci\_types.h:2755

[bt\_hci\_evt\_le\_phy\_update\_complete](structbt__hci__evt__le__phy__update__complete.md)

**Definition** hci\_types.h:2701

[bt\_hci\_evt\_le\_phy\_update\_complete::handle](structbt__hci__evt__le__phy__update__complete.md#a70f472edef3b25fb23490ea6dcce9d43)

uint16\_t handle

**Definition** hci\_types.h:2703

[bt\_hci\_evt\_le\_phy\_update\_complete::status](structbt__hci__evt__le__phy__update__complete.md#a927a9e6982b29ecd4c3972b19a9bcdc2)

uint8\_t status

**Definition** hci\_types.h:2702

[bt\_hci\_evt\_le\_phy\_update\_complete::tx\_phy](structbt__hci__evt__le__phy__update__complete.md#ad184e10b7af71582db64ec5d3a66cff9)

uint8\_t tx\_phy

**Definition** hci\_types.h:2704

[bt\_hci\_evt\_le\_phy\_update\_complete::rx\_phy](structbt__hci__evt__le__phy__update__complete.md#ad792ffec08aa8e383009e2e353a03fcd)

uint8\_t rx\_phy

**Definition** hci\_types.h:2705

[bt\_hci\_evt\_le\_remote\_feat\_complete](structbt__hci__evt__le__remote__feat__complete.md)

**Definition** hci\_types.h:2631

[bt\_hci\_evt\_le\_remote\_feat\_complete::features](structbt__hci__evt__le__remote__feat__complete.md#a61101c21e317aa07b08725a7ffbb4b81)

uint8\_t features[8]

**Definition** hci\_types.h:2634

[bt\_hci\_evt\_le\_remote\_feat\_complete::status](structbt__hci__evt__le__remote__feat__complete.md#a8a80bade7644f986fec41462843d8319)

uint8\_t status

**Definition** hci\_types.h:2632

[bt\_hci\_evt\_le\_remote\_feat\_complete::handle](structbt__hci__evt__le__remote__feat__complete.md#a9a0da26d9415169f02b6c9472120afe7)

uint16\_t handle

**Definition** hci\_types.h:2633

[bt\_hci\_evt\_le\_req\_peer\_sca\_complete](structbt__hci__evt__le__req__peer__sca__complete.md)

**Definition** hci\_types.h:2935

[bt\_hci\_evt\_le\_req\_peer\_sca\_complete::status](structbt__hci__evt__le__req__peer__sca__complete.md#a814d17b8aae9dd68f57402c857ca1810)

uint8\_t status

**Definition** hci\_types.h:2936

[bt\_hci\_evt\_le\_req\_peer\_sca\_complete::sca](structbt__hci__evt__le__req__peer__sca__complete.md#a88f93ead6ec67e1612b1a0e8402a30e7)

uint8\_t sca

**Definition** hci\_types.h:2938

[bt\_hci\_evt\_le\_req\_peer\_sca\_complete::handle](structbt__hci__evt__le__req__peer__sca__complete.md#ab6b648e7f4bff9e84b274e9e22a26166)

uint16\_t handle

**Definition** hci\_types.h:2937

[bt\_hci\_evt\_le\_scan\_req\_received](structbt__hci__evt__le__scan__req__received.md)

**Definition** hci\_types.h:2778

[bt\_hci\_evt\_le\_scan\_req\_received::handle](structbt__hci__evt__le__scan__req__received.md#a62c6d5e5b7079665c0aea8eb676a0433)

uint8\_t handle

**Definition** hci\_types.h:2779

[bt\_hci\_evt\_le\_scan\_req\_received::addr](structbt__hci__evt__le__scan__req__received.md#a7dca5ad876dc97859a139d8bd4b207af)

bt\_addr\_le\_t addr

**Definition** hci\_types.h:2780

[bt\_hci\_evt\_le\_transmit\_power\_report](structbt__hci__evt__le__transmit__power__report.md)

**Definition** hci\_types.h:2951

[bt\_hci\_evt\_le\_transmit\_power\_report::tx\_power\_level\_flag](structbt__hci__evt__le__transmit__power__report.md#a2dc33da8f36cceda362d0c87098b02d6)

uint8\_t tx\_power\_level\_flag

**Definition** hci\_types.h:2957

[bt\_hci\_evt\_le\_transmit\_power\_report::reason](structbt__hci__evt__le__transmit__power__report.md#a341cc0c5cc1ea969e2024b67056a5439)

uint8\_t reason

**Definition** hci\_types.h:2954

[bt\_hci\_evt\_le\_transmit\_power\_report::handle](structbt__hci__evt__le__transmit__power__report.md#a4feadb14800c1b51a9cc523c1d6a9063)

uint16\_t handle

**Definition** hci\_types.h:2953

[bt\_hci\_evt\_le\_transmit\_power\_report::tx\_power\_level](structbt__hci__evt__le__transmit__power__report.md#aa0df9c50a555fa40ed25a14f7b6a5e77)

int8\_t tx\_power\_level

**Definition** hci\_types.h:2956

[bt\_hci\_evt\_le\_transmit\_power\_report::delta](structbt__hci__evt__le__transmit__power__report.md#ac42d60325235f517728ff44385361db2)

int8\_t delta

**Definition** hci\_types.h:2958

[bt\_hci\_evt\_le\_transmit\_power\_report::phy](structbt__hci__evt__le__transmit__power__report.md#ad6130863713cf31a1cbe33de9fb5428f)

uint8\_t phy

**Definition** hci\_types.h:2955

[bt\_hci\_evt\_le\_transmit\_power\_report::status](structbt__hci__evt__le__transmit__power__report.md#af1629e59dd651e1616b89f4958f47c92)

uint8\_t status

**Definition** hci\_types.h:2952

[bt\_hci\_evt\_link\_key\_notify](structbt__hci__evt__link__key__notify.md)

**Definition** hci\_types.h:2392

[bt\_hci\_evt\_link\_key\_notify::bdaddr](structbt__hci__evt__link__key__notify.md#a02647d66142c037b8bca2e748bc15319)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:2393

[bt\_hci\_evt\_link\_key\_notify::link\_key](structbt__hci__evt__link__key__notify.md#a4a1b50d8874d01a6a5dc5c52524c9bed)

uint8\_t link\_key[16]

**Definition** hci\_types.h:2394

[bt\_hci\_evt\_link\_key\_notify::key\_type](structbt__hci__evt__link__key__notify.md#a664580660a690af0d9ae3a62d79ad94b)

uint8\_t key\_type

**Definition** hci\_types.h:2395

[bt\_hci\_evt\_link\_key\_req](structbt__hci__evt__link__key__req.md)

**Definition** hci\_types.h:2376

[bt\_hci\_evt\_link\_key\_req::bdaddr](structbt__hci__evt__link__key__req.md#aed882dfb6b632383543bd7e60536ccc6)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:2377

[bt\_hci\_evt\_num\_completed\_packets](structbt__hci__evt__num__completed__packets.md)

**Definition** hci\_types.h:2365

[bt\_hci\_evt\_num\_completed\_packets::num\_handles](structbt__hci__evt__num__completed__packets.md#a666ed2c19596a89ab0c77275cbe18d1e)

uint8\_t num\_handles

**Definition** hci\_types.h:2366

[bt\_hci\_evt\_num\_completed\_packets::h](structbt__hci__evt__num__completed__packets.md#a94fb176924f7e844704be28851366052)

struct bt\_hci\_handle\_count h[0]

**Definition** hci\_types.h:2367

[bt\_hci\_evt\_pin\_code\_req](structbt__hci__evt__pin__code__req.md)

**Definition** hci\_types.h:2371

[bt\_hci\_evt\_pin\_code\_req::bdaddr](structbt__hci__evt__pin__code__req.md#a8649a30cd8c7ecf9ee006ddc2e625908)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:2372

[bt\_hci\_evt\_remote\_ext\_features](structbt__hci__evt__remote__ext__features.md)

**Definition** hci\_types.h:2419

[bt\_hci\_evt\_remote\_ext\_features::handle](structbt__hci__evt__remote__ext__features.md#a0191b80b4f4d5360972faa6d5edf5055)

uint16\_t handle

**Definition** hci\_types.h:2421

[bt\_hci\_evt\_remote\_ext\_features::features](structbt__hci__evt__remote__ext__features.md#a084199f8e30669c2a1a631af26c0d69a)

uint8\_t features[8]

**Definition** hci\_types.h:2424

[bt\_hci\_evt\_remote\_ext\_features::status](structbt__hci__evt__remote__ext__features.md#a4f1d489aaa5626e485d34a9ae4cf9a34)

uint8\_t status

**Definition** hci\_types.h:2420

[bt\_hci\_evt\_remote\_ext\_features::page](structbt__hci__evt__remote__ext__features.md#aeece2b8d46f4a3713d63df29058f2d9c)

uint8\_t page

**Definition** hci\_types.h:2422

[bt\_hci\_evt\_remote\_ext\_features::max\_page](structbt__hci__evt__remote__ext__features.md#afa577407f4ded5404394f42e7c73e10b)

uint8\_t max\_page

**Definition** hci\_types.h:2423

[bt\_hci\_evt\_remote\_features](structbt__hci__evt__remote__features.md)

**Definition** hci\_types.h:2320

[bt\_hci\_evt\_remote\_features::status](structbt__hci__evt__remote__features.md#a2cedd8392c87914272ff250a56c80574)

uint8\_t status

**Definition** hci\_types.h:2321

[bt\_hci\_evt\_remote\_features::features](structbt__hci__evt__remote__features.md#a70c97b9fbf7c363eab7b27f3a4e86e96)

uint8\_t features[8]

**Definition** hci\_types.h:2323

[bt\_hci\_evt\_remote\_features::handle](structbt__hci__evt__remote__features.md#ada0249bdb7108c5d347fea1218c4f878)

uint16\_t handle

**Definition** hci\_types.h:2322

[bt\_hci\_evt\_remote\_name\_req\_complete](structbt__hci__evt__remote__name__req__complete.md)

**Definition** hci\_types.h:2306

[bt\_hci\_evt\_remote\_name\_req\_complete::bdaddr](structbt__hci__evt__remote__name__req__complete.md#a380121873bf059b7c8a4abdf212f4235)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:2308

[bt\_hci\_evt\_remote\_name\_req\_complete::name](structbt__hci__evt__remote__name__req__complete.md#a3e54674692f7fc1670fa389e293714c7)

uint8\_t name[248]

**Definition** hci\_types.h:2309

[bt\_hci\_evt\_remote\_name\_req\_complete::status](structbt__hci__evt__remote__name__req__complete.md#ab43d4a3c19d829b829cc7b40a67959f3)

uint8\_t status

**Definition** hci\_types.h:2307

[bt\_hci\_evt\_remote\_version\_info](structbt__hci__evt__remote__version__info.md)

**Definition** hci\_types.h:2327

[bt\_hci\_evt\_remote\_version\_info::subversion](structbt__hci__evt__remote__version__info.md#a02188119418a5a6dd8a4d0c37f5a060d)

uint16\_t subversion

**Definition** hci\_types.h:2332

[bt\_hci\_evt\_remote\_version\_info::handle](structbt__hci__evt__remote__version__info.md#a1703a9ac9a5e1ba3ed396fe5799f9f51)

uint16\_t handle

**Definition** hci\_types.h:2329

[bt\_hci\_evt\_remote\_version\_info::status](structbt__hci__evt__remote__version__info.md#a196f9489183d6e0116ff687df66c60c0)

uint8\_t status

**Definition** hci\_types.h:2328

[bt\_hci\_evt\_remote\_version\_info::version](structbt__hci__evt__remote__version__info.md#a8442b9f2bdc6cbce564c9bcec4169a20)

uint8\_t version

**Definition** hci\_types.h:2330

[bt\_hci\_evt\_remote\_version\_info::manufacturer](structbt__hci__evt__remote__version__info.md#aaa9c3875143700b6ed013715cb3c7107)

uint16\_t manufacturer

**Definition** hci\_types.h:2331

[bt\_hci\_evt\_role\_change](structbt__hci__evt__role__change.md)

**Definition** hci\_types.h:2358

[bt\_hci\_evt\_role\_change::bdaddr](structbt__hci__evt__role__change.md#a18dd22435ae40fcf1c4fd2b90b402c60)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:2360

[bt\_hci\_evt\_role\_change::role](structbt__hci__evt__role__change.md#a2e5736d63e30326c33bec8ebdf986c62)

uint8\_t role

**Definition** hci\_types.h:2361

[bt\_hci\_evt\_role\_change::status](structbt__hci__evt__role__change.md#aafe1a9e43a9a42d4030846180e55b8ef)

uint8\_t status

**Definition** hci\_types.h:2359

[bt\_hci\_evt\_ssp\_complete](structbt__hci__evt__ssp__complete.md)

**Definition** hci\_types.h:2571

[bt\_hci\_evt\_ssp\_complete::status](structbt__hci__evt__ssp__complete.md#a33d3d47c1cef71cfb787a1195d9b4ec2)

uint8\_t status

**Definition** hci\_types.h:2572

[bt\_hci\_evt\_ssp\_complete::bdaddr](structbt__hci__evt__ssp__complete.md#a5030cf334f97cdd982001b3278ed9db1)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:2573

[bt\_hci\_evt\_sync\_conn\_complete](structbt__hci__evt__sync__conn__complete.md)

**Definition** hci\_types.h:2516

[bt\_hci\_evt\_sync\_conn\_complete::tx\_interval](structbt__hci__evt__sync__conn__complete.md#a4b93873ad6f5388657511d87fc0a8c85)

uint8\_t tx\_interval

**Definition** hci\_types.h:2521

[bt\_hci\_evt\_sync\_conn\_complete::air\_mode](structbt__hci__evt__sync__conn__complete.md#a5f6068569bf649bcd1d13928f56f9703)

uint8\_t air\_mode

**Definition** hci\_types.h:2525

[bt\_hci\_evt\_sync\_conn\_complete::retansmission\_window](structbt__hci__evt__sync__conn__complete.md#a68a31880c8aab9245be043c1719464d3)

uint8\_t retansmission\_window

**Definition** hci\_types.h:2522

[bt\_hci\_evt\_sync\_conn\_complete::rx\_pkt\_length](structbt__hci__evt__sync__conn__complete.md#a6a455f56da4666cb602e6c05157e166d)

uint16\_t rx\_pkt\_length

**Definition** hci\_types.h:2523

[bt\_hci\_evt\_sync\_conn\_complete::bdaddr](structbt__hci__evt__sync__conn__complete.md#a78f5560783400f1d1a63b2c9d69fa7ed)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:2519

[bt\_hci\_evt\_sync\_conn\_complete::handle](structbt__hci__evt__sync__conn__complete.md#aa48aa29ff73e93e8d961013f066c1b5e)

uint16\_t handle

**Definition** hci\_types.h:2518

[bt\_hci\_evt\_sync\_conn\_complete::link\_type](structbt__hci__evt__sync__conn__complete.md#aacf9919945e9b755913da145f0fe78ae)

uint8\_t link\_type

**Definition** hci\_types.h:2520

[bt\_hci\_evt\_sync\_conn\_complete::tx\_pkt\_length](structbt__hci__evt__sync__conn__complete.md#ab4d4106d5120f10e8300834db12740d8)

uint16\_t tx\_pkt\_length

**Definition** hci\_types.h:2524

[bt\_hci\_evt\_sync\_conn\_complete::status](structbt__hci__evt__sync__conn__complete.md#accd17a95f35ab1988122df7584830f60)

uint8\_t status

**Definition** hci\_types.h:2517

[bt\_hci\_evt\_user\_confirm\_req](structbt__hci__evt__user__confirm__req.md)

**Definition** hci\_types.h:2560

[bt\_hci\_evt\_user\_confirm\_req::bdaddr](structbt__hci__evt__user__confirm__req.md#aaeec83c50764c322af7cd64259e54a97)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:2561

[bt\_hci\_evt\_user\_confirm\_req::passkey](structbt__hci__evt__user__confirm__req.md#ac333729f5a7d9241ac26aeb7d3f77935)

uint32\_t passkey

**Definition** hci\_types.h:2562

[bt\_hci\_evt\_user\_passkey\_notify](structbt__hci__evt__user__passkey__notify.md)

**Definition** hci\_types.h:2577

[bt\_hci\_evt\_user\_passkey\_notify::passkey](structbt__hci__evt__user__passkey__notify.md#a7f6a367e50d41cb7d8897db05db826be)

uint32\_t passkey

**Definition** hci\_types.h:2579

[bt\_hci\_evt\_user\_passkey\_notify::bdaddr](structbt__hci__evt__user__passkey__notify.md#af020e1cd131473fe06a193529a0499ac)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:2578

[bt\_hci\_evt\_user\_passkey\_req](structbt__hci__evt__user__passkey__req.md)

**Definition** hci\_types.h:2566

[bt\_hci\_evt\_user\_passkey\_req::bdaddr](structbt__hci__evt__user__passkey__req.md#a7f1005423296906e0374050bc30781ce)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:2567

[bt\_hci\_ext\_adv\_set](structbt__hci__ext__adv__set.md)

**Definition** hci\_types.h:1431

[bt\_hci\_ext\_adv\_set::max\_ext\_adv\_evts](structbt__hci__ext__adv__set.md#a4467ac9a564ea24bb701de46cda2579a)

uint8\_t max\_ext\_adv\_evts

**Definition** hci\_types.h:1434

[bt\_hci\_ext\_adv\_set::handle](structbt__hci__ext__adv__set.md#a9d0fd3f6659db172ff4efd74c2c2d216)

uint8\_t handle

**Definition** hci\_types.h:1432

[bt\_hci\_ext\_adv\_set::duration](structbt__hci__ext__adv__set.md#acc2afc91fe5c0dfcb4c95eaade4a047a)

uint16\_t duration

**Definition** hci\_types.h:1433

[bt\_hci\_ext\_conn\_phy](structbt__hci__ext__conn__phy.md)

**Definition** hci\_types.h:1528

[bt\_hci\_ext\_conn\_phy::max\_ce\_len](structbt__hci__ext__conn__phy.md#a3c3ccb93014758b3215718d2672ce7f3)

uint16\_t max\_ce\_len

**Definition** hci\_types.h:1536

[bt\_hci\_ext\_conn\_phy::scan\_interval](structbt__hci__ext__conn__phy.md#a4f78503fe42ee81fea740ba1643a732e)

uint16\_t scan\_interval

**Definition** hci\_types.h:1529

[bt\_hci\_ext\_conn\_phy::conn\_interval\_max](structbt__hci__ext__conn__phy.md#a7bcf66a3372d92c809d8427796915b88)

uint16\_t conn\_interval\_max

**Definition** hci\_types.h:1532

[bt\_hci\_ext\_conn\_phy::conn\_latency](structbt__hci__ext__conn__phy.md#a7dd57b7ef0b13b15da47e92076f87d79)

uint16\_t conn\_latency

**Definition** hci\_types.h:1533

[bt\_hci\_ext\_conn\_phy::conn\_interval\_min](structbt__hci__ext__conn__phy.md#a7fc06c1a458aedb6b29381450a5a4df0)

uint16\_t conn\_interval\_min

**Definition** hci\_types.h:1531

[bt\_hci\_ext\_conn\_phy::supervision\_timeout](structbt__hci__ext__conn__phy.md#aaec54c0743dfc08923b5ccd8fc1a4015)

uint16\_t supervision\_timeout

**Definition** hci\_types.h:1534

[bt\_hci\_ext\_conn\_phy::scan\_window](structbt__hci__ext__conn__phy.md#ae0e950c8004bd595631f95a289a5c871)

uint16\_t scan\_window

**Definition** hci\_types.h:1530

[bt\_hci\_ext\_conn\_phy::min\_ce\_len](structbt__hci__ext__conn__phy.md#af48212961ce21f5222e57f70ffeb811b)

uint16\_t min\_ce\_len

**Definition** hci\_types.h:1535

[bt\_hci\_ext\_scan\_phy](structbt__hci__ext__scan__phy.md)

**Definition** hci\_types.h:1498

[bt\_hci\_ext\_scan\_phy::interval](structbt__hci__ext__scan__phy.md#a2f087d18bde86d0ac81a14a09ae5b9b0)

uint16\_t interval

**Definition** hci\_types.h:1500

[bt\_hci\_ext\_scan\_phy::type](structbt__hci__ext__scan__phy.md#a4cfebc7b2709973953bed9a09a793b7e)

uint8\_t type

**Definition** hci\_types.h:1499

[bt\_hci\_ext\_scan\_phy::window](structbt__hci__ext__scan__phy.md#a9c0196f0d5f0064796c15a5df2ad4c07)

uint16\_t window

**Definition** hci\_types.h:1501

[bt\_hci\_handle\_count](structbt__hci__handle__count.md)

**Definition** hci\_types.h:622

[bt\_hci\_handle\_count::count](structbt__hci__handle__count.md#a71577f376985909744fa14f246e69e1d)

uint16\_t count

**Definition** hci\_types.h:624

[bt\_hci\_handle\_count::handle](structbt__hci__handle__count.md#acacc000905835724b7fe882a8ad85f82)

uint16\_t handle

**Definition** hci\_types.h:623

[bt\_hci\_iso\_data\_hdr](structbt__hci__iso__data__hdr.md)

**Definition** hci\_types.h:100

[bt\_hci\_iso\_data\_hdr::sn](structbt__hci__iso__data__hdr.md#a66ed7e709658d3bb3ead2c7242e596b1)

uint16\_t sn

**Definition** hci\_types.h:101

[bt\_hci\_iso\_data\_hdr::slen](structbt__hci__iso__data__hdr.md#ab04366e16e692bb4664c0cdbf89983eb)

uint16\_t slen

**Definition** hci\_types.h:102

[bt\_hci\_iso\_hdr](structbt__hci__iso__hdr.md)

**Definition** hci\_types.h:113

[bt\_hci\_iso\_hdr::len](structbt__hci__iso__hdr.md#ab33ae914a9eba85b35c78e45e0f5255f)

uint16\_t len

**Definition** hci\_types.h:115

[bt\_hci\_iso\_hdr::handle](structbt__hci__iso__hdr.md#af5113383fbcd0e70828f986720c38572)

uint16\_t handle

**Definition** hci\_types.h:114

[bt\_hci\_iso\_ts\_data\_hdr](structbt__hci__iso__ts__data__hdr.md)

**Definition** hci\_types.h:106

[bt\_hci\_iso\_ts\_data\_hdr::ts](structbt__hci__iso__ts__data__hdr.md#a58c5a3c5dc0aaf7d498b7ecaea6595bd)

uint32\_t ts

**Definition** hci\_types.h:107

[bt\_hci\_iso\_ts\_data\_hdr::data](structbt__hci__iso__ts__data__hdr.md#a77cb6fe6584e603488ac5949bf6bf736)

struct bt\_hci\_iso\_data\_hdr data

**Definition** hci\_types.h:108

[bt\_hci\_le\_iq\_sample](structbt__hci__le__iq__sample.md)

**Definition** hci\_types.h:2803

[bt\_hci\_le\_iq\_sample::q](structbt__hci__le__iq__sample.md#a775b6e0ab1842594bc00998faec613f3)

int8\_t q

**Definition** hci\_types.h:2805

[bt\_hci\_le\_iq\_sample::i](structbt__hci__le__iq__sample.md#aacf452456eecd4ad4dab083593b11104)

int8\_t i

**Definition** hci\_types.h:2804

[bt\_hci\_op\_inquiry](structbt__hci__op__inquiry.md)

**Definition** hci\_types.h:348

[bt\_hci\_op\_inquiry::lap](structbt__hci__op__inquiry.md#abdd03feccecbdbbb5d2c7c7f3213b62f)

uint8\_t lap[3]

**Definition** hci\_types.h:349

[bt\_hci\_op\_inquiry::num\_rsp](structbt__hci__op__inquiry.md#ac8ed23243dbd9a7c46fedd8abe9666f5)

uint8\_t num\_rsp

**Definition** hci\_types.h:351

[bt\_hci\_op\_inquiry::length](structbt__hci__op__inquiry.md#ae77fa706c9875b5568a4af26a7724d08)

uint8\_t length

**Definition** hci\_types.h:350

[bt\_hci\_rp\_configure\_data\_path](structbt__hci__rp__configure__data__path.md)

**Definition** hci\_types.h:689

[bt\_hci\_rp\_configure\_data\_path::status](structbt__hci__rp__configure__data__path.md#a10cfe9bf5a7be202706957d7b8e1f371)

uint8\_t status

**Definition** hci\_types.h:690

[bt\_hci\_rp\_connect\_cancel](structbt__hci__rp__connect__cancel.md)

**Definition** hci\_types.h:376

[bt\_hci\_rp\_connect\_cancel::status](structbt__hci__rp__connect__cancel.md#a05d0c9e4163bc62a57dba8618294eb65)

uint8\_t status

**Definition** hci\_types.h:377

[bt\_hci\_rp\_connect\_cancel::bdaddr](structbt__hci__rp__connect__cancel.md#a0ccfcbd294aa067879ab8d7a41bc41c9)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:378

[bt\_hci\_rp\_le\_big\_terminate\_sync](structbt__hci__rp__le__big__terminate__sync.md)

**Definition** hci\_types.h:2123

[bt\_hci\_rp\_le\_big\_terminate\_sync::big\_handle](structbt__hci__rp__le__big__terminate__sync.md#a741ab80e08e7ecfc5a0158ec0cf14654)

uint8\_t big\_handle

**Definition** hci\_types.h:2125

[bt\_hci\_rp\_le\_big\_terminate\_sync::status](structbt__hci__rp__le__big__terminate__sync.md#ad4d1d4238402ef829a1ff9ed3b1dc050)

uint8\_t status

**Definition** hci\_types.h:2124

[bt\_hci\_rp\_le\_conn\_cte\_req\_enable](structbt__hci__rp__le__conn__cte__req__enable.md)

**Definition** hci\_types.h:1816

[bt\_hci\_rp\_le\_conn\_cte\_req\_enable::status](structbt__hci__rp__le__conn__cte__req__enable.md#a1e76e7a6da194a433c1fa6ac2bc36b80)

uint8\_t status

**Definition** hci\_types.h:1817

[bt\_hci\_rp\_le\_conn\_cte\_req\_enable::handle](structbt__hci__rp__le__conn__cte__req__enable.md#af00adb07a144156a37fb5fc47ca61ccb)

uint16\_t handle

**Definition** hci\_types.h:1818

[bt\_hci\_rp\_le\_conn\_cte\_rsp\_enable](structbt__hci__rp__le__conn__cte__rsp__enable.md)

**Definition** hci\_types.h:1827

[bt\_hci\_rp\_le\_conn\_cte\_rsp\_enable::status](structbt__hci__rp__le__conn__cte__rsp__enable.md#a8a21bc015408cc77c5d229cd77289dcc)

uint8\_t status

**Definition** hci\_types.h:1828

[bt\_hci\_rp\_le\_conn\_cte\_rsp\_enable::handle](structbt__hci__rp__le__conn__cte__rsp__enable.md#ab16f226d871d7d55c3f900614d59d8a1)

uint16\_t handle

**Definition** hci\_types.h:1829

[bt\_hci\_rp\_le\_conn\_param\_req\_neg\_reply](structbt__hci__rp__le__conn__param__req__neg__reply.md)

**Definition** hci\_types.h:1176

[bt\_hci\_rp\_le\_conn\_param\_req\_neg\_reply::status](structbt__hci__rp__le__conn__param__req__neg__reply.md#a3804e64f9e8693e3e5899067212f6873)

uint8\_t status

**Definition** hci\_types.h:1177

[bt\_hci\_rp\_le\_conn\_param\_req\_neg\_reply::handle](structbt__hci__rp__le__conn__param__req__neg__reply.md#ac88f44127c0a1b9b191a27cc003c1052)

uint16\_t handle

**Definition** hci\_types.h:1178

[bt\_hci\_rp\_le\_conn\_param\_req\_reply](structbt__hci__rp__le__conn__param__req__reply.md)

**Definition** hci\_types.h:1166

[bt\_hci\_rp\_le\_conn\_param\_req\_reply::status](structbt__hci__rp__le__conn__param__req__reply.md#a2f0a9f5b087d1f12c100ef4521e015ff)

uint8\_t status

**Definition** hci\_types.h:1167

[bt\_hci\_rp\_le\_conn\_param\_req\_reply::handle](structbt__hci__rp__le__conn__param__req__reply.md#a3e598cd87d5298a1cc62ac79a4f34a6e)

uint16\_t handle

**Definition** hci\_types.h:1168

[bt\_hci\_rp\_le\_default\_past\_param](structbt__hci__rp__le__default__past__param.md)

**Definition** hci\_types.h:1920

[bt\_hci\_rp\_le\_default\_past\_param::status](structbt__hci__rp__le__default__past__param.md#a292e2d655c77e8cda0d01fc07b43b8c4)

uint8\_t status

**Definition** hci\_types.h:1921

[bt\_hci\_rp\_le\_encrypt](structbt__hci__rp__le__encrypt.md)

**Definition** hci\_types.h:1085

[bt\_hci\_rp\_le\_encrypt::enc\_data](structbt__hci__rp__le__encrypt.md#ac20cd9f4ceffea6999114f65437aefdc)

uint8\_t enc\_data[16]

**Definition** hci\_types.h:1087

[bt\_hci\_rp\_le\_encrypt::status](structbt__hci__rp__le__encrypt.md#aee480917cc6af7dea77717a9cb5840bb)

uint8\_t status

**Definition** hci\_types.h:1086

[bt\_hci\_rp\_le\_iso\_receive\_test](structbt__hci__rp__le__iso__receive__test.md)

**Definition** hci\_types.h:2181

[bt\_hci\_rp\_le\_iso\_receive\_test::status](structbt__hci__rp__le__iso__receive__test.md#a028a77001a5e24dda8fac38718103ef0)

uint8\_t status

**Definition** hci\_types.h:2182

[bt\_hci\_rp\_le\_iso\_receive\_test::handle](structbt__hci__rp__le__iso__receive__test.md#a863a8a44af979a8b1b9d084563b2fe9a)

uint16\_t handle

**Definition** hci\_types.h:2183

[bt\_hci\_rp\_le\_iso\_test\_end](structbt__hci__rp__le__iso__test__end.md)

**Definition** hci\_types.h:2204

[bt\_hci\_rp\_le\_iso\_test\_end::missed\_cnt](structbt__hci__rp__le__iso__test__end.md#a10b3ee6110bc0bb9279b22f9963715c1)

uint32\_t missed\_cnt

**Definition** hci\_types.h:2208

[bt\_hci\_rp\_le\_iso\_test\_end::status](structbt__hci__rp__le__iso__test__end.md#a16feaeb739f6ed34d9ce3fc86248955c)

uint8\_t status

**Definition** hci\_types.h:2205

[bt\_hci\_rp\_le\_iso\_test\_end::handle](structbt__hci__rp__le__iso__test__end.md#a4a4625d7b78abf3c039842df2a72ce8b)

uint16\_t handle

**Definition** hci\_types.h:2206

[bt\_hci\_rp\_le\_iso\_test\_end::received\_cnt](structbt__hci__rp__le__iso__test__end.md#a55490978e7416ecc308bf510f05afd4f)

uint32\_t received\_cnt

**Definition** hci\_types.h:2207

[bt\_hci\_rp\_le\_iso\_test\_end::failed\_cnt](structbt__hci__rp__le__iso__test__end.md#ab4352fd5d9b822fb7fb75f8f5e2db6a9)

uint32\_t failed\_cnt

**Definition** hci\_types.h:2209

[bt\_hci\_rp\_le\_iso\_transmit\_test](structbt__hci__rp__le__iso__transmit__test.md)

**Definition** hci\_types.h:2170

[bt\_hci\_rp\_le\_iso\_transmit\_test::status](structbt__hci__rp__le__iso__transmit__test.md#a01ae01d11c606f559107b8c54781d843)

uint8\_t status

**Definition** hci\_types.h:2171

[bt\_hci\_rp\_le\_iso\_transmit\_test::handle](structbt__hci__rp__le__iso__transmit__test.md#a0863c47551b328984e00c392f9f11660)

uint16\_t handle

**Definition** hci\_types.h:2172

[bt\_hci\_rp\_le\_ltk\_req\_neg\_reply](structbt__hci__rp__le__ltk__req__neg__reply.md)

**Definition** hci\_types.h:1118

[bt\_hci\_rp\_le\_ltk\_req\_neg\_reply::status](structbt__hci__rp__le__ltk__req__neg__reply.md#a92306e47450b239233a3f39c645eaa4e)

uint8\_t status

**Definition** hci\_types.h:1119

[bt\_hci\_rp\_le\_ltk\_req\_neg\_reply::handle](structbt__hci__rp__le__ltk__req__neg__reply.md#ad0f4f9300d9a8b737b41211972151017)

uint16\_t handle

**Definition** hci\_types.h:1120

[bt\_hci\_rp\_le\_ltk\_req\_reply](structbt__hci__rp__le__ltk__req__reply.md)

**Definition** hci\_types.h:1109

[bt\_hci\_rp\_le\_ltk\_req\_reply::handle](structbt__hci__rp__le__ltk__req__reply.md#a2dfe012e641e5d8bd6c0f2e15e5a54c2)

uint16\_t handle

**Definition** hci\_types.h:1111

[bt\_hci\_rp\_le\_ltk\_req\_reply::status](structbt__hci__rp__le__ltk__req__reply.md#a831950bab8994f36c96c543310400752)

uint8\_t status

**Definition** hci\_types.h:1110

[bt\_hci\_rp\_le\_past\_param](structbt__hci__rp__le__past__param.md)

**Definition** hci\_types.h:1907

[bt\_hci\_rp\_le\_past\_param::status](structbt__hci__rp__le__past__param.md#a9630362b3d885b13869a4c0fe9e97b12)

uint8\_t status

**Definition** hci\_types.h:1908

[bt\_hci\_rp\_le\_past\_param::conn\_handle](structbt__hci__rp__le__past__param.md#ae6b8a5d7e790516de2f91e41fd893111)

uint16\_t conn\_handle

**Definition** hci\_types.h:1909

[bt\_hci\_rp\_le\_per\_adv\_set\_info\_transfer](structbt__hci__rp__le__per__adv__set__info__transfer.md)

**Definition** hci\_types.h:1882

[bt\_hci\_rp\_le\_per\_adv\_set\_info\_transfer::conn\_handle](structbt__hci__rp__le__per__adv__set__info__transfer.md#a696e5cab4d7507ea79b0e116c4bb92e2)

uint16\_t conn\_handle

**Definition** hci\_types.h:1884

[bt\_hci\_rp\_le\_per\_adv\_set\_info\_transfer::status](structbt__hci__rp__le__per__adv__set__info__transfer.md#ab1592bfadd45315ff47e86b7c50374ad)

uint8\_t status

**Definition** hci\_types.h:1883

[bt\_hci\_rp\_le\_per\_adv\_sync\_transfer](structbt__hci__rp__le__per__adv__sync__transfer.md)

**Definition** hci\_types.h:1870

[bt\_hci\_rp\_le\_per\_adv\_sync\_transfer::conn\_handle](structbt__hci__rp__le__per__adv__sync__transfer.md#ab8b4357fd92e01a5f61d3127b04c0318)

uint16\_t conn\_handle

**Definition** hci\_types.h:1872

[bt\_hci\_rp\_le\_per\_adv\_sync\_transfer::status](structbt__hci__rp__le__per__adv__sync__transfer.md#adb536c4694d2e7c5b91e9f68986e97e1)

uint8\_t status

**Definition** hci\_types.h:1871

[bt\_hci\_rp\_le\_rand](structbt__hci__rp__le__rand.md)

**Definition** hci\_types.h:1091

[bt\_hci\_rp\_le\_rand::rand](structbt__hci__rp__le__rand.md#a3f706af9d2baf9e2b199242a28cec9e5)

uint8\_t rand[8]

**Definition** hci\_types.h:1093

[bt\_hci\_rp\_le\_rand::status](structbt__hci__rp__le__rand.md#a73320168836caa3caf724282402e80de)

uint8\_t status

**Definition** hci\_types.h:1092

[bt\_hci\_rp\_le\_read\_ant\_info](structbt__hci__rp__le__read__ant__info.md)

**Definition** hci\_types.h:1846

[bt\_hci\_rp\_le\_read\_ant\_info::num\_ant](structbt__hci__rp__le__read__ant__info.md#a1f79b45751d39ebb9349df93d0ff2e13)

uint8\_t num\_ant

**Definition** hci\_types.h:1849

[bt\_hci\_rp\_le\_read\_ant\_info::switch\_sample\_rates](structbt__hci__rp__le__read__ant__info.md#a2c78d3db239c9e00729d91834eb60f21)

uint8\_t switch\_sample\_rates

**Definition** hci\_types.h:1848

[bt\_hci\_rp\_le\_read\_ant\_info::max\_cte\_len](structbt__hci__rp__le__read__ant__info.md#a625cc8fa8553eafbbb31cbc0b3f303c7)

uint8\_t max\_cte\_len

**Definition** hci\_types.h:1851

[bt\_hci\_rp\_le\_read\_ant\_info::status](structbt__hci__rp__le__read__ant__info.md#ae1388d3eee3085af7f2b0b57b2aa7b1e)

uint8\_t status

**Definition** hci\_types.h:1847

[bt\_hci\_rp\_le\_read\_ant\_info::max\_switch\_pattern\_len](structbt__hci__rp__le__read__ant__info.md#ae75fe0b9f5fe8c88a8e8482eef299348)

uint8\_t max\_switch\_pattern\_len

**Definition** hci\_types.h:1850

[bt\_hci\_rp\_le\_read\_buffer\_size\_v2](structbt__hci__rp__le__read__buffer__size__v2.md)

**Definition** hci\_types.h:1925

[bt\_hci\_rp\_le\_read\_buffer\_size\_v2::acl\_max\_num](structbt__hci__rp__le__read__buffer__size__v2.md#a1c7938defb076d973b8339c17cc930df)

uint8\_t acl\_max\_num

**Definition** hci\_types.h:1928

[bt\_hci\_rp\_le\_read\_buffer\_size\_v2::status](structbt__hci__rp__le__read__buffer__size__v2.md#a3b9cc0577d0f5f3c2b934a28915f2177)

uint8\_t status

**Definition** hci\_types.h:1926

[bt\_hci\_rp\_le\_read\_buffer\_size\_v2::iso\_max\_len](structbt__hci__rp__le__read__buffer__size__v2.md#a9758d477c502575a1c176eb6a63e1a1a)

uint16\_t iso\_max\_len

**Definition** hci\_types.h:1929

[bt\_hci\_rp\_le\_read\_buffer\_size\_v2::iso\_max\_num](structbt__hci__rp__le__read__buffer__size__v2.md#ac3379adf42f9bbee8ae72fb4a7606fd1)

uint8\_t iso\_max\_num

**Definition** hci\_types.h:1930

[bt\_hci\_rp\_le\_read\_buffer\_size\_v2::acl\_max\_len](structbt__hci__rp__le__read__buffer__size__v2.md#ac391149d3d7442e074aad4b98659bd02)

uint16\_t acl\_max\_len

**Definition** hci\_types.h:1927

[bt\_hci\_rp\_le\_read\_buffer\_size](structbt__hci__rp__le__read__buffer__size.md)

**Definition** hci\_types.h:904

[bt\_hci\_rp\_le\_read\_buffer\_size::le\_max\_num](structbt__hci__rp__le__read__buffer__size.md#a3e393d6c51d8c3f8a5d88413198e3f28)

uint8\_t le\_max\_num

**Definition** hci\_types.h:907

[bt\_hci\_rp\_le\_read\_buffer\_size::le\_max\_len](structbt__hci__rp__le__read__buffer__size.md#a8bc64cd8743984cd5a8dedfc86aaee56)

uint16\_t le\_max\_len

**Definition** hci\_types.h:906

[bt\_hci\_rp\_le\_read\_buffer\_size::status](structbt__hci__rp__le__read__buffer__size.md#a90a1206f1dbbefd298e5323ac07691f1)

uint8\_t status

**Definition** hci\_types.h:905

[bt\_hci\_rp\_le\_read\_chan\_map](structbt__hci__rp__le__read__chan__map.md)

**Definition** hci\_types.h:1069

[bt\_hci\_rp\_le\_read\_chan\_map::ch\_map](structbt__hci__rp__le__read__chan__map.md#a2899c53f17ba2293b95477ba25fd1b3d)

uint8\_t ch\_map[5]

**Definition** hci\_types.h:1072

[bt\_hci\_rp\_le\_read\_chan\_map::status](structbt__hci__rp__le__read__chan__map.md#a73a51f243bf4881f9024ba67cf2426ad)

uint8\_t status

**Definition** hci\_types.h:1070

[bt\_hci\_rp\_le\_read\_chan\_map::handle](structbt__hci__rp__le__read__chan__map.md#a8fcec46574f5601bf0837aae8f745b38)

uint16\_t handle

**Definition** hci\_types.h:1071

[bt\_hci\_rp\_le\_read\_chan\_tx\_power](structbt__hci__rp__le__read__chan__tx__power.md)

**Definition** hci\_types.h:954

[bt\_hci\_rp\_le\_read\_chan\_tx\_power::status](structbt__hci__rp__le__read__chan__tx__power.md#a09a3805bccdabef399d21b29f84e3a4f)

uint8\_t status

**Definition** hci\_types.h:955

[bt\_hci\_rp\_le\_read\_chan\_tx\_power::tx\_power\_level](structbt__hci__rp__le__read__chan__tx__power.md#a3b6b79d1d28c3e4bf565ae364089f365)

int8\_t tx\_power\_level

**Definition** hci\_types.h:956

[bt\_hci\_rp\_le\_read\_default\_data\_len](structbt__hci__rp__le__read__default__data__len.md)

**Definition** hci\_types.h:1193

[bt\_hci\_rp\_le\_read\_default\_data\_len::max\_tx\_octets](structbt__hci__rp__le__read__default__data__len.md#a1ec4ba1c0286132e87fcffeb988a37f9)

uint16\_t max\_tx\_octets

**Definition** hci\_types.h:1195

[bt\_hci\_rp\_le\_read\_default\_data\_len::status](structbt__hci__rp__le__read__default__data__len.md#a62d735826ad3ca5d4bea7d0fb87dea7e)

uint8\_t status

**Definition** hci\_types.h:1194

[bt\_hci\_rp\_le\_read\_default\_data\_len::max\_tx\_time](structbt__hci__rp__le__read__default__data__len.md#ae193eab40c2afa55b78a1906e6a26f26)

uint16\_t max\_tx\_time

**Definition** hci\_types.h:1196

[bt\_hci\_rp\_le\_read\_fal\_size](structbt__hci__rp__le__read__fal__size.md)

**Definition** hci\_types.h:1032

[bt\_hci\_rp\_le\_read\_fal\_size::status](structbt__hci__rp__le__read__fal__size.md#aaceae885848bbdbf71241e7aa3881db5)

uint8\_t status

**Definition** hci\_types.h:1033

[bt\_hci\_rp\_le\_read\_fal\_size::fal\_size](structbt__hci__rp__le__read__fal__size.md#ac5fcb88478c1faadf7f7ca6a9f838dde)

uint8\_t fal\_size

**Definition** hci\_types.h:1034

[bt\_hci\_rp\_le\_read\_iso\_link\_quality](structbt__hci__rp__le__read__iso__link__quality.md)

**Definition** hci\_types.h:2227

[bt\_hci\_rp\_le\_read\_iso\_link\_quality::tx\_last\_subevent\_packets](structbt__hci__rp__le__read__iso__link__quality.md#a0d4468f6871716414ef4a601791bac58)

uint32\_t tx\_last\_subevent\_packets

**Definition** hci\_types.h:2232

[bt\_hci\_rp\_le\_read\_iso\_link\_quality::tx\_flushed\_packets](structbt__hci__rp__le__read__iso__link__quality.md#a12c0c3f9fe6c3c94742367f30bdcc630)

uint32\_t tx\_flushed\_packets

**Definition** hci\_types.h:2231

[bt\_hci\_rp\_le\_read\_iso\_link\_quality::crc\_error\_packets](structbt__hci__rp__le__read__iso__link__quality.md#a353070a64655a39f5410fe76e9168e97)

uint32\_t crc\_error\_packets

**Definition** hci\_types.h:2234

[bt\_hci\_rp\_le\_read\_iso\_link\_quality::duplicate\_packets](structbt__hci__rp__le__read__iso__link__quality.md#a68c23277e65dc5694f5a27ee2cd364ff)

uint32\_t duplicate\_packets

**Definition** hci\_types.h:2236

[bt\_hci\_rp\_le\_read\_iso\_link\_quality::rx\_unreceived\_packets](structbt__hci__rp__le__read__iso__link__quality.md#a6a16d0aa7ed220bac1ade12eb0f7703e)

uint32\_t rx\_unreceived\_packets

**Definition** hci\_types.h:2235

[bt\_hci\_rp\_le\_read\_iso\_link\_quality::retransmitted\_packets](structbt__hci__rp__le__read__iso__link__quality.md#a7be135da9607045f60b616b84a68f5db)

uint32\_t retransmitted\_packets

**Definition** hci\_types.h:2233

[bt\_hci\_rp\_le\_read\_iso\_link\_quality::handle](structbt__hci__rp__le__read__iso__link__quality.md#a9f2e8c26081ede43c7712b851d79f2cd)

uint16\_t handle

**Definition** hci\_types.h:2229

[bt\_hci\_rp\_le\_read\_iso\_link\_quality::tx\_unacked\_packets](structbt__hci__rp__le__read__iso__link__quality.md#aae42e05dff474062726b92c6d45eae4f)

uint32\_t tx\_unacked\_packets

**Definition** hci\_types.h:2230

[bt\_hci\_rp\_le\_read\_iso\_link\_quality::status](structbt__hci__rp__le__read__iso__link__quality.md#aef80c600f8916c098e08c43ca718d630)

uint8\_t status

**Definition** hci\_types.h:2228

[bt\_hci\_rp\_le\_read\_iso\_tx\_sync](structbt__hci__rp__le__read__iso__tx__sync.md)

**Definition** hci\_types.h:1938

[bt\_hci\_rp\_le\_read\_iso\_tx\_sync::status](structbt__hci__rp__le__read__iso__tx__sync.md#a188ef5dba77c754c46094135cc52641c)

uint8\_t status

**Definition** hci\_types.h:1939

[bt\_hci\_rp\_le\_read\_iso\_tx\_sync::offset](structbt__hci__rp__le__read__iso__tx__sync.md#a29770c3172d5e45409392aa8ffc835ef)

uint8\_t offset[3]

**Definition** hci\_types.h:1943

[bt\_hci\_rp\_le\_read\_iso\_tx\_sync::timestamp](structbt__hci__rp__le__read__iso__tx__sync.md#a35520a3e50afc03ed969b6c5ca9e15d9)

uint32\_t timestamp

**Definition** hci\_types.h:1942

[bt\_hci\_rp\_le\_read\_iso\_tx\_sync::handle](structbt__hci__rp__le__read__iso__tx__sync.md#a8c0003043d3896b1ff93dc33dccc76b4)

uint16\_t handle

**Definition** hci\_types.h:1940

[bt\_hci\_rp\_le\_read\_iso\_tx\_sync::seq](structbt__hci__rp__le__read__iso__tx__sync.md#af2a02f68aa0a757757c490e707954952)

uint16\_t seq

**Definition** hci\_types.h:1941

[bt\_hci\_rp\_le\_read\_local\_features](structbt__hci__rp__le__read__local__features.md)

**Definition** hci\_types.h:911

[bt\_hci\_rp\_le\_read\_local\_features::status](structbt__hci__rp__le__read__local__features.md#ac1000822beba8a7be0dda684c0a86b6b)

uint8\_t status

**Definition** hci\_types.h:912

[bt\_hci\_rp\_le\_read\_local\_features::features](structbt__hci__rp__le__read__local__features.md#ada42e525338cd5526ff211c359c93b3b)

uint8\_t features[8]

**Definition** hci\_types.h:913

[bt\_hci\_rp\_le\_read\_local\_rpa](structbt__hci__rp__le__read__local__rpa.md)

**Definition** hci\_types.h:1257

[bt\_hci\_rp\_le\_read\_local\_rpa::status](structbt__hci__rp__le__read__local__rpa.md#a55b1ac66c986c0a7879b144163064be2)

uint8\_t status

**Definition** hci\_types.h:1258

[bt\_hci\_rp\_le\_read\_local\_rpa::local\_rpa](structbt__hci__rp__le__read__local__rpa.md#a5b27c5b02cb290452be62c22772fbc53)

bt\_addr\_t local\_rpa

**Definition** hci\_types.h:1259

[bt\_hci\_rp\_le\_read\_max\_adv\_data\_len](structbt__hci__rp__le__read__max__adv__data__len.md)

**Definition** hci\_types.h:1444

[bt\_hci\_rp\_le\_read\_max\_adv\_data\_len::status](structbt__hci__rp__le__read__max__adv__data__len.md#a978911dc5028d1f36820447de8e9e5f7)

uint8\_t status

**Definition** hci\_types.h:1445

[bt\_hci\_rp\_le\_read\_max\_adv\_data\_len::max\_adv\_data\_len](structbt__hci__rp__le__read__max__adv__data__len.md#aa4084a89de4929c3e8e2630d0aad7f82)

uint16\_t max\_adv\_data\_len

**Definition** hci\_types.h:1446

[bt\_hci\_rp\_le\_read\_max\_data\_len](structbt__hci__rp__le__read__max__data__len.md)

**Definition** hci\_types.h:1276

[bt\_hci\_rp\_le\_read\_max\_data\_len::max\_tx\_octets](structbt__hci__rp__le__read__max__data__len.md#a2c0b159c6248cb9df458d587f82a4152)

uint16\_t max\_tx\_octets

**Definition** hci\_types.h:1278

[bt\_hci\_rp\_le\_read\_max\_data\_len::status](structbt__hci__rp__le__read__max__data__len.md#a654b34b1ee038bf442550a340a26070c)

uint8\_t status

**Definition** hci\_types.h:1277

[bt\_hci\_rp\_le\_read\_max\_data\_len::max\_tx\_time](structbt__hci__rp__le__read__max__data__len.md#a6adc84bf3cc86f234e61982d871899b6)

uint16\_t max\_tx\_time

**Definition** hci\_types.h:1279

[bt\_hci\_rp\_le\_read\_max\_data\_len::max\_rx\_octets](structbt__hci__rp__le__read__max__data__len.md#a9273dac6614f1e120f0539b746bfd6cc)

uint16\_t max\_rx\_octets

**Definition** hci\_types.h:1280

[bt\_hci\_rp\_le\_read\_max\_data\_len::max\_rx\_time](structbt__hci__rp__le__read__max__data__len.md#a963ef9c097906c8db46c35459eb4ecab)

uint16\_t max\_rx\_time

**Definition** hci\_types.h:1281

[bt\_hci\_rp\_le\_read\_num\_adv\_sets](structbt__hci__rp__le__read__num__adv__sets.md)

**Definition** hci\_types.h:1450

[bt\_hci\_rp\_le\_read\_num\_adv\_sets::status](structbt__hci__rp__le__read__num__adv__sets.md#a590934059fb851a14b2eec66f32a5334)

uint8\_t status

**Definition** hci\_types.h:1451

[bt\_hci\_rp\_le\_read\_num\_adv\_sets::num\_sets](structbt__hci__rp__le__read__num__adv__sets.md#a7dd26bda7a8ab75fed2af19bb5af34fc)

uint8\_t num\_sets

**Definition** hci\_types.h:1452

[bt\_hci\_rp\_le\_read\_peer\_rpa](structbt__hci__rp__le__read__peer__rpa.md)

**Definition** hci\_types.h:1248

[bt\_hci\_rp\_le\_read\_peer\_rpa::peer\_rpa](structbt__hci__rp__le__read__peer__rpa.md#a4eeee179819865ba5d5171d9bd33e5e9)

bt\_addr\_t peer\_rpa

**Definition** hci\_types.h:1250

[bt\_hci\_rp\_le\_read\_peer\_rpa::status](structbt__hci__rp__le__read__peer__rpa.md#a9c8c799e8c9fbb9f64865e55cdb1f9ef)

uint8\_t status

**Definition** hci\_types.h:1249

[bt\_hci\_rp\_le\_read\_per\_adv\_list\_size](structbt__hci__rp__le__read__per__adv__list__size.md)

**Definition** hci\_types.h:1654

[bt\_hci\_rp\_le\_read\_per\_adv\_list\_size::status](structbt__hci__rp__le__read__per__adv__list__size.md#a70aa5b466bdbbd309fc59570625c35e5)

uint8\_t status

**Definition** hci\_types.h:1655

[bt\_hci\_rp\_le\_read\_per\_adv\_list\_size::list\_size](structbt__hci__rp__le__read__per__adv__list__size.md#ab6c4ed1037327669aef623f3a1e9d601)

uint8\_t list\_size

**Definition** hci\_types.h:1656

[bt\_hci\_rp\_le\_read\_phy](structbt__hci__rp__le__read__phy.md)

**Definition** hci\_types.h:1292

[bt\_hci\_rp\_le\_read\_phy::rx\_phy](structbt__hci__rp__le__read__phy.md#a5a060e0c0d1e5f33222ab10a5d3977e8)

uint8\_t rx\_phy

**Definition** hci\_types.h:1296

[bt\_hci\_rp\_le\_read\_phy::tx\_phy](structbt__hci__rp__le__read__phy.md#a644c0065d97e5de006dc28f7bca62268)

uint8\_t tx\_phy

**Definition** hci\_types.h:1295

[bt\_hci\_rp\_le\_read\_phy::status](structbt__hci__rp__le__read__phy.md#a65d412e37eb2cd839fae262f4f9d5b28)

uint8\_t status

**Definition** hci\_types.h:1293

[bt\_hci\_rp\_le\_read\_phy::handle](structbt__hci__rp__le__read__phy.md#ae708b4f8ad2632d73bedea640f138d9f)

uint16\_t handle

**Definition** hci\_types.h:1294

[bt\_hci\_rp\_le\_read\_rf\_path\_comp](structbt__hci__rp__le__read__rf__path__comp.md)

**Definition** hci\_types.h:1667

[bt\_hci\_rp\_le\_read\_rf\_path\_comp::rx\_path\_comp](structbt__hci__rp__le__read__rf__path__comp.md#a0f46a99c74006dc0a4dfd1a49c72e077)

int16\_t rx\_path\_comp

**Definition** hci\_types.h:1670

[bt\_hci\_rp\_le\_read\_rf\_path\_comp::tx\_path\_comp](structbt__hci__rp__le__read__rf__path__comp.md#a827fa954277823efdc5838c317a1460a)

int16\_t tx\_path\_comp

**Definition** hci\_types.h:1669

[bt\_hci\_rp\_le\_read\_rf\_path\_comp::status](structbt__hci__rp__le__read__rf__path__comp.md#a84a04bcc64ea6d50fe41e9b416a5ada1)

uint8\_t status

**Definition** hci\_types.h:1668

[bt\_hci\_rp\_le\_read\_rl\_size](structbt__hci__rp__le__read__rl__size.md)

**Definition** hci\_types.h:1239

[bt\_hci\_rp\_le\_read\_rl\_size::rl\_size](structbt__hci__rp__le__read__rl__size.md#a90c28070ee094c99c21c4dd229ff6ce5)

uint8\_t rl\_size

**Definition** hci\_types.h:1241

[bt\_hci\_rp\_le\_read\_rl\_size::status](structbt__hci__rp__le__read__rl__size.md#af8a10aab21d54cce3529b1307769f6c6)

uint8\_t status

**Definition** hci\_types.h:1240

[bt\_hci\_rp\_le\_read\_supp\_states](structbt__hci__rp__le__read__supp__states.md)

**Definition** hci\_types.h:1124

[bt\_hci\_rp\_le\_read\_supp\_states::le\_states](structbt__hci__rp__le__read__supp__states.md#a9b60476cc158a701b29b28bd21375130)

uint8\_t le\_states[8]

**Definition** hci\_types.h:1126

[bt\_hci\_rp\_le\_read\_supp\_states::status](structbt__hci__rp__le__read__supp__states.md#aeed0cc41ee521c27f07d8cbf4b377a4f)

uint8\_t status

**Definition** hci\_types.h:1125

[bt\_hci\_rp\_le\_read\_test\_counters](structbt__hci__rp__le__read__test__counters.md)

**Definition** hci\_types.h:2191

[bt\_hci\_rp\_le\_read\_test\_counters::handle](structbt__hci__rp__le__read__test__counters.md#a8121f879a3fb5550cc1aa468aacb81b7)

uint16\_t handle

**Definition** hci\_types.h:2193

[bt\_hci\_rp\_le\_read\_test\_counters::received\_cnt](structbt__hci__rp__le__read__test__counters.md#a8c4b2674fb129ca0de0bc45c608e13c7)

uint32\_t received\_cnt

**Definition** hci\_types.h:2194

[bt\_hci\_rp\_le\_read\_test\_counters::status](structbt__hci__rp__le__read__test__counters.md#ae1e78d68e9f55b31092a07575a66c1c0)

uint8\_t status

**Definition** hci\_types.h:2192

[bt\_hci\_rp\_le\_read\_test\_counters::missed\_cnt](structbt__hci__rp__le__read__test__counters.md#ae96d05ffb2fbc681c804b04c8791aeab)

uint32\_t missed\_cnt

**Definition** hci\_types.h:2195

[bt\_hci\_rp\_le\_read\_test\_counters::failed\_cnt](structbt__hci__rp__le__read__test__counters.md#af6261d3547cd9b377fedc7a36891c2f7)

uint32\_t failed\_cnt

**Definition** hci\_types.h:2196

[bt\_hci\_rp\_le\_read\_tx\_power\_level](structbt__hci__rp__le__read__tx__power__level.md)

**Definition** hci\_types.h:588

[bt\_hci\_rp\_le\_read\_tx\_power\_level::status](structbt__hci__rp__le__read__tx__power__level.md#a4c83db208bfcb7c9fd2211d192a26d90)

uint8\_t status

**Definition** hci\_types.h:589

[bt\_hci\_rp\_le\_read\_tx\_power\_level::max\_tx\_power\_level](structbt__hci__rp__le__read__tx__power__level.md#a5f9c59660f7c5842712a4ad9ae1d9527)

int8\_t max\_tx\_power\_level

**Definition** hci\_types.h:593

[bt\_hci\_rp\_le\_read\_tx\_power\_level::current\_tx\_power\_level](structbt__hci__rp__le__read__tx__power__level.md#ad14f660eb67f1014d1a62b0e5a113969)

int8\_t current\_tx\_power\_level

**Definition** hci\_types.h:592

[bt\_hci\_rp\_le\_read\_tx\_power\_level::phy](structbt__hci__rp__le__read__tx__power__level.md#ae65a43aad74b1081e88afdb533cbe813)

uint8\_t phy

**Definition** hci\_types.h:591

[bt\_hci\_rp\_le\_read\_tx\_power\_level::handle](structbt__hci__rp__le__read__tx__power__level.md#aec00dfb34abce2d95af183b74f63d1f3)

uint16\_t handle

**Definition** hci\_types.h:590

[bt\_hci\_rp\_le\_read\_tx\_power](structbt__hci__rp__le__read__tx__power.md)

**Definition** hci\_types.h:1660

[bt\_hci\_rp\_le\_read\_tx\_power::max\_tx\_power](structbt__hci__rp__le__read__tx__power.md#a1d794f1f7ea77eceac7dae2546eab047)

int8\_t max\_tx\_power

**Definition** hci\_types.h:1663

[bt\_hci\_rp\_le\_read\_tx\_power::min\_tx\_power](structbt__hci__rp__le__read__tx__power.md#a6d4ab95efda5cfc97ae11d83787da8d7)

int8\_t min\_tx\_power

**Definition** hci\_types.h:1662

[bt\_hci\_rp\_le\_read\_tx\_power::status](structbt__hci__rp__le__read__tx__power.md#a805629b92c65e006082d819f578ed555)

uint8\_t status

**Definition** hci\_types.h:1661

[bt\_hci\_rp\_le\_reject\_cis](structbt__hci__rp__le__reject__cis.md)

**Definition** hci\_types.h:2059

[bt\_hci\_rp\_le\_reject\_cis::handle](structbt__hci__rp__le__reject__cis.md#acd8311e13bdfd7edb2d404d80006f9d4)

uint16\_t handle

**Definition** hci\_types.h:2061

[bt\_hci\_rp\_le\_reject\_cis::status](structbt__hci__rp__le__reject__cis.md#af2dc8a839d3e19821ab8ec0d3dc427ec)

uint8\_t status

**Definition** hci\_types.h:2060

[bt\_hci\_rp\_le\_remove\_cig](structbt__hci__rp__le__remove__cig.md)

**Definition** hci\_types.h:2043

[bt\_hci\_rp\_le\_remove\_cig::status](structbt__hci__rp__le__remove__cig.md#a1335f26f1dc67ff8e2a1960d1b24b1a0)

uint8\_t status

**Definition** hci\_types.h:2044

[bt\_hci\_rp\_le\_remove\_cig::cig\_id](structbt__hci__rp__le__remove__cig.md#a82e74fbbce714b035b1e53fd5f1b09b5)

uint8\_t cig\_id

**Definition** hci\_types.h:2045

[bt\_hci\_rp\_le\_remove\_iso\_path](structbt__hci__rp__le__remove__iso__path.md)

**Definition** hci\_types.h:2155

[bt\_hci\_rp\_le\_remove\_iso\_path::status](structbt__hci__rp__le__remove__iso__path.md#ab22e50e594e19931526feacd9bff33a3)

uint8\_t status

**Definition** hci\_types.h:2156

[bt\_hci\_rp\_le\_remove\_iso\_path::handle](structbt__hci__rp__le__remove__iso__path.md#ae3b7704359989ca13582a5cd3742f588)

uint16\_t handle

**Definition** hci\_types.h:2157

[bt\_hci\_rp\_le\_set\_cig\_params\_test](structbt__hci__rp__le__set__cig__params__test.md)

**Definition** hci\_types.h:2020

[bt\_hci\_rp\_le\_set\_cig\_params\_test::handle](structbt__hci__rp__le__set__cig__params__test.md#a08b07863ed63ab627401c0c80bc3c7b4)

uint16\_t handle[0]

**Definition** hci\_types.h:2024

[bt\_hci\_rp\_le\_set\_cig\_params\_test::num\_handles](structbt__hci__rp__le__set__cig__params__test.md#a10816d0875092c8e6bd4b13b819c43c7)

uint8\_t num\_handles

**Definition** hci\_types.h:2023

[bt\_hci\_rp\_le\_set\_cig\_params\_test::cig\_id](structbt__hci__rp__le__set__cig__params__test.md#a65c11059bc00244e58d2ab8373e3e725)

uint8\_t cig\_id

**Definition** hci\_types.h:2022

[bt\_hci\_rp\_le\_set\_cig\_params\_test::status](structbt__hci__rp__le__set__cig__params__test.md#a932eadb4d750f79b4a7a9c3feb90fdcd)

uint8\_t status

**Definition** hci\_types.h:2021

[bt\_hci\_rp\_le\_set\_cig\_params](structbt__hci__rp__le__set__cig__params.md)

**Definition** hci\_types.h:1985

[bt\_hci\_rp\_le\_set\_cig\_params::handle](structbt__hci__rp__le__set__cig__params.md#a2e95c6217d11169a8a611ea95dce70b6)

uint16\_t handle[0]

**Definition** hci\_types.h:1989

[bt\_hci\_rp\_le\_set\_cig\_params::status](structbt__hci__rp__le__set__cig__params.md#a8426a2b9927bee05fb9a46b4b261c743)

uint8\_t status

**Definition** hci\_types.h:1986

[bt\_hci\_rp\_le\_set\_cig\_params::num\_handles](structbt__hci__rp__le__set__cig__params.md#a8aff643e0ae41455eb9391cfdb45ebda)

uint8\_t num\_handles

**Definition** hci\_types.h:1988

[bt\_hci\_rp\_le\_set\_cig\_params::cig\_id](structbt__hci__rp__le__set__cig__params.md#a951dc88e0cde4e1f0274684498741eac)

uint8\_t cig\_id

**Definition** hci\_types.h:1987

[bt\_hci\_rp\_le\_set\_cl\_cte\_sampling\_enable](structbt__hci__rp__le__set__cl__cte__sampling__enable.md)

**Definition** hci\_types.h:1763

[bt\_hci\_rp\_le\_set\_cl\_cte\_sampling\_enable::sync\_handle](structbt__hci__rp__le__set__cl__cte__sampling__enable.md#a44db7f831e8d730ec3c80c01ef9543aa)

uint16\_t sync\_handle

**Definition** hci\_types.h:1765

[bt\_hci\_rp\_le\_set\_cl\_cte\_sampling\_enable::status](structbt__hci__rp__le__set__cl__cte__sampling__enable.md#a5962f97cef6e53452cdccab1c3440519)

uint8\_t status

**Definition** hci\_types.h:1764

[bt\_hci\_rp\_le\_set\_conn\_cte\_rx\_params](structbt__hci__rp__le__set__conn__cte__rx__params.md)

**Definition** hci\_types.h:1777

[bt\_hci\_rp\_le\_set\_conn\_cte\_rx\_params::handle](structbt__hci__rp__le__set__conn__cte__rx__params.md#a3c3fb92d422e7ccaf0c98706d46b3e5a)

uint16\_t handle

**Definition** hci\_types.h:1779

[bt\_hci\_rp\_le\_set\_conn\_cte\_rx\_params::status](structbt__hci__rp__le__set__conn__cte__rx__params.md#ad38bb356876c16904e408405607de73c)

uint8\_t status

**Definition** hci\_types.h:1778

[bt\_hci\_rp\_le\_set\_conn\_cte\_tx\_params](structbt__hci__rp__le__set__conn__cte__tx__params.md)

**Definition** hci\_types.h:1797

[bt\_hci\_rp\_le\_set\_conn\_cte\_tx\_params::status](structbt__hci__rp__le__set__conn__cte__tx__params.md#a56f62b6d2c42cd22f73026a2fabc6986)

uint8\_t status

**Definition** hci\_types.h:1798

[bt\_hci\_rp\_le\_set\_conn\_cte\_tx\_params::handle](structbt__hci__rp__le__set__conn__cte__tx__params.md#aad553d484daed7ca08de132f4fb849ee)

uint16\_t handle

**Definition** hci\_types.h:1799

[bt\_hci\_rp\_le\_set\_data\_len](structbt__hci__rp__le__set__data__len.md)

**Definition** hci\_types.h:1187

[bt\_hci\_rp\_le\_set\_data\_len::handle](structbt__hci__rp__le__set__data__len.md#a207c6da11e0bb145bed7a9e551ddc608)

uint16\_t handle

**Definition** hci\_types.h:1189

[bt\_hci\_rp\_le\_set\_data\_len::status](structbt__hci__rp__le__set__data__len.md#a8667db355a95691d58845f89e919aea4)

uint8\_t status

**Definition** hci\_types.h:1188

[bt\_hci\_rp\_le\_set\_ext\_adv\_param](structbt__hci__rp__le__set__ext__adv__param.md)

**Definition** hci\_types.h:1396

[bt\_hci\_rp\_le\_set\_ext\_adv\_param::status](structbt__hci__rp__le__set__ext__adv__param.md#a6baae317455ffbb489066fcd1fb068c8)

uint8\_t status

**Definition** hci\_types.h:1397

[bt\_hci\_rp\_le\_set\_ext\_adv\_param::tx\_power](structbt__hci__rp__le__set__ext__adv__param.md#a8a876d0e3d4d9d066a27c054569f0b9a)

int8\_t tx\_power

**Definition** hci\_types.h:1398

[bt\_hci\_rp\_le\_set\_host\_feature](structbt__hci__rp__le__set__host__feature.md)

**Definition** hci\_types.h:2218

[bt\_hci\_rp\_le\_set\_host\_feature::status](structbt__hci__rp__le__set__host__feature.md#a2e7cfc16da9fc0d00c35111811bf7c28)

uint8\_t status

**Definition** hci\_types.h:2219

[bt\_hci\_rp\_le\_setup\_iso\_path](structbt__hci__rp__le__setup__iso__path.md)

**Definition** hci\_types.h:2144

[bt\_hci\_rp\_le\_setup\_iso\_path::handle](structbt__hci__rp__le__setup__iso__path.md#aa8effdcc4ba155b840ef789f20bad19e)

uint16\_t handle

**Definition** hci\_types.h:2146

[bt\_hci\_rp\_le\_setup\_iso\_path::status](structbt__hci__rp__le__setup__iso__path.md#adde60b0dc6ec3d8caccae1d55d78d9a4)

uint8\_t status

**Definition** hci\_types.h:2145

[bt\_hci\_rp\_le\_test\_end](structbt__hci__rp__le__test__end.md)

**Definition** hci\_types.h:1151

[bt\_hci\_rp\_le\_test\_end::status](structbt__hci__rp__le__test__end.md#a2ac412ef9a5fc7651315afe042856cce)

uint8\_t status

**Definition** hci\_types.h:1152

[bt\_hci\_rp\_le\_test\_end::rx\_pkt\_count](structbt__hci__rp__le__test__end.md#a9e283118e4ea48b0df66a4cd1c1cf9a1)

uint16\_t rx\_pkt\_count

**Definition** hci\_types.h:1153

[bt\_hci\_rp\_pin\_code\_neg\_reply](structbt__hci__rp__pin__code__neg__reply.md)

**Definition** hci\_types.h:441

[bt\_hci\_rp\_pin\_code\_neg\_reply::status](structbt__hci__rp__pin__code__neg__reply.md#a10bcc55407e22417256c464684a41e58)

uint8\_t status

**Definition** hci\_types.h:442

[bt\_hci\_rp\_pin\_code\_neg\_reply::bdaddr](structbt__hci__rp__pin__code__neg__reply.md#a168caf2a517aa573bd6acaf48e414e9b)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:443

[bt\_hci\_rp\_pin\_code\_reply](structbt__hci__rp__pin__code__reply.md)

**Definition** hci\_types.h:432

[bt\_hci\_rp\_pin\_code\_reply::status](structbt__hci__rp__pin__code__reply.md#a3f167661b8d3f63ab12e6f64fb33986b)

uint8\_t status

**Definition** hci\_types.h:433

[bt\_hci\_rp\_pin\_code\_reply::bdaddr](structbt__hci__rp__pin__code__reply.md#afc7c991fd8050e8aae56b8587b5ee01d)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:434

[bt\_hci\_rp\_read\_auth\_payload\_timeout](structbt__hci__rp__read__auth__payload__timeout.md)

**Definition** hci\_types.h:664

[bt\_hci\_rp\_read\_auth\_payload\_timeout::status](structbt__hci__rp__read__auth__payload__timeout.md#a3eadeab880eb75c914be654dbc685f3f)

uint8\_t status

**Definition** hci\_types.h:665

[bt\_hci\_rp\_read\_auth\_payload\_timeout::auth\_payload\_timeout](structbt__hci__rp__read__auth__payload__timeout.md#ab4092720dad9a01f4e179eb2f0112aed)

uint16\_t auth\_payload\_timeout

**Definition** hci\_types.h:667

[bt\_hci\_rp\_read\_auth\_payload\_timeout::handle](structbt__hci__rp__read__auth__payload__timeout.md#ab53b7e03c68dcd040e38fdc7429b2d3b)

uint16\_t handle

**Definition** hci\_types.h:666

[bt\_hci\_rp\_read\_bd\_addr](structbt__hci__rp__read__bd__addr.md)

**Definition** hci\_types.h:752

[bt\_hci\_rp\_read\_bd\_addr::status](structbt__hci__rp__read__bd__addr.md#a5230de2a3a6c4161d076b59901790e1e)

uint8\_t status

**Definition** hci\_types.h:753

[bt\_hci\_rp\_read\_bd\_addr::bdaddr](structbt__hci__rp__read__bd__addr.md#aec2c022a465982a3868100699c95f4e6)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:754

[bt\_hci\_rp\_read\_buffer\_size](structbt__hci__rp__read__buffer__size.md)

**Definition** hci\_types.h:743

[bt\_hci\_rp\_read\_buffer\_size::status](structbt__hci__rp__read__buffer__size.md#a6adf126acfcec722dc078d097d2b2ba8)

uint8\_t status

**Definition** hci\_types.h:744

[bt\_hci\_rp\_read\_buffer\_size::sco\_max\_len](structbt__hci__rp__read__buffer__size.md#a7d475559145f469006b2ef147704cd99)

uint8\_t sco\_max\_len

**Definition** hci\_types.h:746

[bt\_hci\_rp\_read\_buffer\_size::acl\_max\_num](structbt__hci__rp__read__buffer__size.md#a87ff361282be71aa60c7f88c50a7492f)

uint16\_t acl\_max\_num

**Definition** hci\_types.h:747

[bt\_hci\_rp\_read\_buffer\_size::acl\_max\_len](structbt__hci__rp__read__buffer__size.md#aba3f1597c929e3721c769beb98000218)

uint16\_t acl\_max\_len

**Definition** hci\_types.h:745

[bt\_hci\_rp\_read\_buffer\_size::sco\_max\_num](structbt__hci__rp__read__buffer__size.md#abc01fa1df6d787f0a2cb865daed5f4cc)

uint16\_t sco\_max\_num

**Definition** hci\_types.h:748

[bt\_hci\_rp\_read\_codec\_capabilities](structbt__hci__rp__read__codec__capabilities.md)

**Definition** hci\_types.h:852

[bt\_hci\_rp\_read\_codec\_capabilities::num\_capabilities](structbt__hci__rp__read__codec__capabilities.md#a71b7df63502bf42a26868e69893ddcfe)

uint8\_t num\_capabilities

**Definition** hci\_types.h:854

[bt\_hci\_rp\_read\_codec\_capabilities::status](structbt__hci__rp__read__codec__capabilities.md#ac224ea998e3af12f97232288266da8d2)

uint8\_t status

**Definition** hci\_types.h:853

[bt\_hci\_rp\_read\_codec\_capabilities::capabilities](structbt__hci__rp__read__codec__capabilities.md#ae0c84013512c461f3b6231162d6f3020)

uint8\_t capabilities[0]

**Definition** hci\_types.h:856

[bt\_hci\_rp\_read\_codecs\_v2](structbt__hci__rp__read__codecs__v2.md)

**Definition** hci\_types.h:830

[bt\_hci\_rp\_read\_codecs\_v2::codecs](structbt__hci__rp__read__codecs__v2.md#a098563f274de085ac97415f1b5e15f3c)

uint8\_t codecs[0]

**Definition** hci\_types.h:833

[bt\_hci\_rp\_read\_codecs\_v2::status](structbt__hci__rp__read__codecs__v2.md#a2e9866d0f9fb42b54c406a9ea5890913)

uint8\_t status

**Definition** hci\_types.h:831

[bt\_hci\_rp\_read\_codecs](structbt__hci__rp__read__codecs.md)

**Definition** hci\_types.h:806

[bt\_hci\_rp\_read\_codecs::status](structbt__hci__rp__read__codecs.md#a017182988634c6acbfbfdd7c9609f5dc)

uint8\_t status

**Definition** hci\_types.h:807

[bt\_hci\_rp\_read\_codecs::codecs](structbt__hci__rp__read__codecs.md#a44e615f375b35cce9f949562555c429b)

uint8\_t codecs[0]

**Definition** hci\_types.h:809

[bt\_hci\_rp\_read\_conn\_accept\_timeout](structbt__hci__rp__read__conn__accept__timeout.md)

**Definition** hci\_types.h:538

[bt\_hci\_rp\_read\_conn\_accept\_timeout::conn\_accept\_timeout](structbt__hci__rp__read__conn__accept__timeout.md#a01ca30c92311ec1df19a4cf835ea74cf)

uint16\_t conn\_accept\_timeout

**Definition** hci\_types.h:540

[bt\_hci\_rp\_read\_conn\_accept\_timeout::status](structbt__hci__rp__read__conn__accept__timeout.md#afeb5888722ee368e02c6b27b75ab2a70)

uint8\_t status

**Definition** hci\_types.h:539

[bt\_hci\_rp\_read\_ctlr\_delay](structbt__hci__rp__read__ctlr__delay.md)

**Definition** hci\_types.h:867

[bt\_hci\_rp\_read\_ctlr\_delay::status](structbt__hci__rp__read__ctlr__delay.md#a2f17081cf767643f3a9ad9d115ef5320)

uint8\_t status

**Definition** hci\_types.h:868

[bt\_hci\_rp\_read\_ctlr\_delay::max\_ctlr\_delay](structbt__hci__rp__read__ctlr__delay.md#a4c468053c4a86d1ab462c1e6f17f1013)

uint8\_t max\_ctlr\_delay[3]

**Definition** hci\_types.h:870

[bt\_hci\_rp\_read\_ctlr\_delay::min\_ctlr\_delay](structbt__hci__rp__read__ctlr__delay.md#ab48d1d92cdf9470a93487434b3824d17)

uint8\_t min\_ctlr\_delay[3]

**Definition** hci\_types.h:869

[bt\_hci\_rp\_read\_encryption\_key\_size](structbt__hci__rp__read__encryption__key__size.md)

**Definition** hci\_types.h:890

[bt\_hci\_rp\_read\_encryption\_key\_size::status](structbt__hci__rp__read__encryption__key__size.md#a17213ccb9179739aa79c3749a2296f65)

uint8\_t status

**Definition** hci\_types.h:891

[bt\_hci\_rp\_read\_encryption\_key\_size::handle](structbt__hci__rp__read__encryption__key__size.md#af0b89b2035f956891244b10409be0f51)

uint16\_t handle

**Definition** hci\_types.h:892

[bt\_hci\_rp\_read\_encryption\_key\_size::key\_size](structbt__hci__rp__read__encryption__key__size.md#af1cd71c6216b26d460c04a68405f05d5)

uint8\_t key\_size

**Definition** hci\_types.h:893

[bt\_hci\_rp\_read\_local\_ext\_features](structbt__hci__rp__read__local__ext__features.md)

**Definition** hci\_types.h:729

[bt\_hci\_rp\_read\_local\_ext\_features::max\_page](structbt__hci__rp__read__local__ext__features.md#a3532e208b3fd347db80d8c55eade3c2d)

uint8\_t max\_page

**Definition** hci\_types.h:732

[bt\_hci\_rp\_read\_local\_ext\_features::ext\_features](structbt__hci__rp__read__local__ext__features.md#a669e8c6faa4e45f472e4f8a3ebb03050)

uint8\_t ext\_features[8]

**Definition** hci\_types.h:733

[bt\_hci\_rp\_read\_local\_ext\_features::page](structbt__hci__rp__read__local__ext__features.md#a7e3669651dc2c2ed9541b7e4945a27f9)

uint8\_t page

**Definition** hci\_types.h:731

[bt\_hci\_rp\_read\_local\_ext\_features::status](structbt__hci__rp__read__local__ext__features.md#a9011f2c89f75939fa92fcf249d2203da)

uint8\_t status

**Definition** hci\_types.h:730

[bt\_hci\_rp\_read\_local\_features](structbt__hci__rp__read__local__features.md)

**Definition** hci\_types.h:737

[bt\_hci\_rp\_read\_local\_features::status](structbt__hci__rp__read__local__features.md#a0ff73da5704ada47f8f79c113254820d)

uint8\_t status

**Definition** hci\_types.h:738

[bt\_hci\_rp\_read\_local\_features::features](structbt__hci__rp__read__local__features.md#ae660b4a772f96bf72bd08124bf26b352)

uint8\_t features[8]

**Definition** hci\_types.h:739

[bt\_hci\_rp\_read\_local\_version\_info](structbt__hci__rp__read__local__version__info.md)

**Definition** hci\_types.h:710

[bt\_hci\_rp\_read\_local\_version\_info::hci\_revision](structbt__hci__rp__read__local__version__info.md#a04161ed3cc0b9c3c442e3464501ce118)

uint16\_t hci\_revision

**Definition** hci\_types.h:713

[bt\_hci\_rp\_read\_local\_version\_info::hci\_version](structbt__hci__rp__read__local__version__info.md#a1cc521426e530344a328e935152dd488)

uint8\_t hci\_version

**Definition** hci\_types.h:712

[bt\_hci\_rp\_read\_local\_version\_info::lmp\_subversion](structbt__hci__rp__read__local__version__info.md#a43f29cf08a2399e818bfa441c6b7a1f3)

uint16\_t lmp\_subversion

**Definition** hci\_types.h:716

[bt\_hci\_rp\_read\_local\_version\_info::lmp\_version](structbt__hci__rp__read__local__version__info.md#a634641751852f66aabb408bf1b4d0cd2)

uint8\_t lmp\_version

**Definition** hci\_types.h:714

[bt\_hci\_rp\_read\_local\_version\_info::manufacturer](structbt__hci__rp__read__local__version__info.md#a7cd6ba190137eaf7c4eb9c2d7e5b36ce)

uint16\_t manufacturer

**Definition** hci\_types.h:715

[bt\_hci\_rp\_read\_local\_version\_info::status](structbt__hci__rp__read__local__version__info.md#a935f990f7c28f7c89660c2b8ab975f43)

uint8\_t status

**Definition** hci\_types.h:711

[bt\_hci\_rp\_read\_rssi](structbt__hci__rp__read__rssi.md)

**Definition** hci\_types.h:877

[bt\_hci\_rp\_read\_rssi::rssi](structbt__hci__rp__read__rssi.md#a1071300bd61fcaab65683187ae393cae)

int8\_t rssi

**Definition** hci\_types.h:880

[bt\_hci\_rp\_read\_rssi::status](structbt__hci__rp__read__rssi.md#a8f91b69a99bd61a7a59d84b3a9c3f235)

uint8\_t status

**Definition** hci\_types.h:878

[bt\_hci\_rp\_read\_rssi::handle](structbt__hci__rp__read__rssi.md#aa3c4041dd240b1185c7fc8bbef74a17a)

uint16\_t handle

**Definition** hci\_types.h:879

[bt\_hci\_rp\_read\_supported\_commands](structbt__hci__rp__read__supported__commands.md)

**Definition** hci\_types.h:720

[bt\_hci\_rp\_read\_supported\_commands::status](structbt__hci__rp__read__supported__commands.md#a3d36d892f83cfcb1d2fc955ec71ff061)

uint8\_t status

**Definition** hci\_types.h:721

[bt\_hci\_rp\_read\_supported\_commands::commands](structbt__hci__rp__read__supported__commands.md#afd0dc4411a4c7692515139392bffedd0)

uint8\_t commands[64]

**Definition** hci\_types.h:722

[bt\_hci\_rp\_read\_tx\_power\_level](structbt__hci__rp__read__tx__power__level.md)

**Definition** hci\_types.h:572

[bt\_hci\_rp\_read\_tx\_power\_level::tx\_power\_level](structbt__hci__rp__read__tx__power__level.md#a46526b820038bb445a7824a7b4bfc870)

int8\_t tx\_power\_level

**Definition** hci\_types.h:575

[bt\_hci\_rp\_read\_tx\_power\_level::handle](structbt__hci__rp__read__tx__power__level.md#ac2bd21e90145102bc483c2b0b3cdd416)

uint16\_t handle

**Definition** hci\_types.h:574

[bt\_hci\_rp\_read\_tx\_power\_level::status](structbt__hci__rp__read__tx__power__level.md#af40a8e2e663872e8d9fdde839cc6d1b4)

uint8\_t status

**Definition** hci\_types.h:573

[bt\_hci\_rp\_remote\_name\_cancel](structbt__hci__rp__remote__name__cancel.md)

**Definition** hci\_types.h:469

[bt\_hci\_rp\_remote\_name\_cancel::bdaddr](structbt__hci__rp__remote__name__cancel.md#a455432799a1272f88b2b00a35a2e7ef5)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:471

[bt\_hci\_rp\_remote\_name\_cancel::status](structbt__hci__rp__remote__name__cancel.md#ac7fadee392b126cb50cef7a6336926cb)

uint8\_t status

**Definition** hci\_types.h:470

[bt\_hci\_rp\_user\_confirm\_reply](structbt__hci__rp__user__confirm__reply.md)

**Definition** hci\_types.h:503

[bt\_hci\_rp\_user\_confirm\_reply::bdaddr](structbt__hci__rp__user__confirm__reply.md#a91678db3ae2a696ba7b9dd5bc080c488)

bt\_addr\_t bdaddr

**Definition** hci\_types.h:505

[bt\_hci\_rp\_user\_confirm\_reply::status](structbt__hci__rp__user__confirm__reply.md#ab07114550c2da3c1e9925cb883bf3a89)

uint8\_t status

**Definition** hci\_types.h:504

[bt\_hci\_rp\_write\_auth\_payload\_timeout](structbt__hci__rp__write__auth__payload__timeout.md)

**Definition** hci\_types.h:676

[bt\_hci\_rp\_write\_auth\_payload\_timeout::handle](structbt__hci__rp__write__auth__payload__timeout.md#a467c6585c913dba03dcfdf5bf4fa688e)

uint16\_t handle

**Definition** hci\_types.h:678

[bt\_hci\_rp\_write\_auth\_payload\_timeout::status](structbt__hci__rp__write__auth__payload__timeout.md#af1783a29e6a167fc20b62bd273215b35)

uint8\_t status

**Definition** hci\_types.h:677

[bt\_hci\_rp\_write\_conn\_accept\_timeout](structbt__hci__rp__write__conn__accept__timeout.md)

**Definition** hci\_types.h:548

[bt\_hci\_rp\_write\_conn\_accept\_timeout::status](structbt__hci__rp__write__conn__accept__timeout.md#a1f9eee1a5843747e0d224b86b602a3da)

uint8\_t status

**Definition** hci\_types.h:549

[bt\_hci\_sco\_hdr](structbt__hci__sco__hdr.md)

**Definition** hci\_types.h:41

[bt\_hci\_sco\_hdr::len](structbt__hci__sco__hdr.md#a158f67c3743684c28728b62db5cf2590)

uint8\_t len

**Definition** hci\_types.h:43

[bt\_hci\_sco\_hdr::handle](structbt__hci__sco__hdr.md#a4b4c915bec966c17567c14e2df9c1581)

uint16\_t handle

**Definition** hci\_types.h:42

[bt\_hci\_std\_codec\_info\_v2](structbt__hci__std__codec__info__v2.md)

**Definition** hci\_types.h:813

[bt\_hci\_std\_codec\_info\_v2::codec\_id](structbt__hci__std__codec__info__v2.md#ae82a0896904c7feb2634579b393bf05e)

uint8\_t codec\_id

**Definition** hci\_types.h:814

[bt\_hci\_std\_codec\_info\_v2::transports](structbt__hci__std__codec__info__v2.md#aea766ba4b911223eeb351e0123e54f5f)

uint8\_t transports

**Definition** hci\_types.h:815

[bt\_hci\_std\_codec\_info](structbt__hci__std__codec__info.md)

**Definition** hci\_types.h:791

[bt\_hci\_std\_codec\_info::codec\_id](structbt__hci__std__codec__info.md#a56e21eca5bbc83cb081aea1c67a7a60d)

uint8\_t codec\_id

**Definition** hci\_types.h:792

[bt\_hci\_std\_codecs\_v2](structbt__hci__std__codecs__v2.md)

**Definition** hci\_types.h:817

[bt\_hci\_std\_codecs\_v2::codec\_info](structbt__hci__std__codecs__v2.md#aafdb6d96d99063a7a447d80e1830a624)

struct bt\_hci\_std\_codec\_info\_v2 codec\_info[0]

**Definition** hci\_types.h:819

[bt\_hci\_std\_codecs\_v2::num\_codecs](structbt__hci__std__codecs__v2.md#ab14fdde478e290235f68aae375969c09)

uint8\_t num\_codecs

**Definition** hci\_types.h:818

[bt\_hci\_std\_codecs](structbt__hci__std__codecs.md)

**Definition** hci\_types.h:794

[bt\_hci\_std\_codecs::codec\_info](structbt__hci__std__codecs.md#a32767e90384ef74a3e740597eacfcf53)

struct bt\_hci\_std\_codec\_info codec\_info[0]

**Definition** hci\_types.h:796

[bt\_hci\_std\_codecs::num\_codecs](structbt__hci__std__codecs.md#ad3e63bf445bb6b8e654baa8490cdf547)

uint8\_t num\_codecs

**Definition** hci\_types.h:795

[bt\_hci\_vs\_codec\_info\_v2](structbt__hci__vs__codec__info__v2.md)

**Definition** hci\_types.h:821

[bt\_hci\_vs\_codec\_info\_v2::company\_id](structbt__hci__vs__codec__info__v2.md#aa6ce27b4acd3dff516e4d7ed2e6434bc)

uint16\_t company\_id

**Definition** hci\_types.h:822

[bt\_hci\_vs\_codec\_info\_v2::transports](structbt__hci__vs__codec__info__v2.md#ac2a91a045e4b53315850b6d4f1d38b2c)

uint8\_t transports

**Definition** hci\_types.h:824

[bt\_hci\_vs\_codec\_info\_v2::codec\_id](structbt__hci__vs__codec__info__v2.md#ae7b7d5d65629a1e3039b3c7cf167a9c1)

uint16\_t codec\_id

**Definition** hci\_types.h:823

[bt\_hci\_vs\_codec\_info](structbt__hci__vs__codec__info.md)

**Definition** hci\_types.h:798

[bt\_hci\_vs\_codec\_info::codec\_id](structbt__hci__vs__codec__info.md#a3c7eea7bae36c7a63457051401526382)

uint16\_t codec\_id

**Definition** hci\_types.h:800

[bt\_hci\_vs\_codec\_info::company\_id](structbt__hci__vs__codec__info.md#a8170dac825b76f3dfb5fde5eed04c4c0)

uint16\_t company\_id

**Definition** hci\_types.h:799

[bt\_hci\_vs\_codecs\_v2](structbt__hci__vs__codecs__v2.md)

**Definition** hci\_types.h:826

[bt\_hci\_vs\_codecs\_v2::codec\_info](structbt__hci__vs__codecs__v2.md#a6cd8aa58517d59d565474513f755cfee)

struct bt\_hci\_vs\_codec\_info\_v2 codec\_info[0]

**Definition** hci\_types.h:828

[bt\_hci\_vs\_codecs\_v2::num\_codecs](structbt__hci__vs__codecs__v2.md#ae4cb3a40401594f8e0f18391b9d31a23)

uint8\_t num\_codecs

**Definition** hci\_types.h:827

[bt\_hci\_vs\_codecs](structbt__hci__vs__codecs.md)

**Definition** hci\_types.h:802

[bt\_hci\_vs\_codecs::num\_codecs](structbt__hci__vs__codecs.md#a2caf18ce5905e3962da000f3b00b623f)

uint8\_t num\_codecs

**Definition** hci\_types.h:803

[bt\_hci\_vs\_codecs::codec\_info](structbt__hci__vs__codecs.md#a4e72426599d5bc617fde4f1a4a095527)

struct bt\_hci\_vs\_codec\_info codec\_info[0]

**Definition** hci\_types.h:804

[bt\_hci\_write\_local\_name](structbt__hci__write__local__name.md)

**Definition** hci\_types.h:533

[bt\_hci\_write\_local\_name::local\_name](structbt__hci__write__local__name.md#a8d2cd9a16525c3fc10ae0e3f196110da)

uint8\_t local\_name[248]

**Definition** hci\_types.h:534

[hci\_cp\_le\_conn\_update](structhci__cp__le__conn__update.md)

**Definition** hci\_types.h:1050

[hci\_cp\_le\_conn\_update::min\_ce\_len](structhci__cp__le__conn__update.md#a3ae86fccacf462463fe520eb1e06fa62)

uint16\_t min\_ce\_len

**Definition** hci\_types.h:1056

[hci\_cp\_le\_conn\_update::max\_ce\_len](structhci__cp__le__conn__update.md#a401169ccc5dbf6cf0abd6154738f00dc)

uint16\_t max\_ce\_len

**Definition** hci\_types.h:1057

[hci\_cp\_le\_conn\_update::handle](structhci__cp__le__conn__update.md#a5606b8795defc338b27d1a130064351e)

uint16\_t handle

**Definition** hci\_types.h:1051

[hci\_cp\_le\_conn\_update::conn\_latency](structhci__cp__le__conn__update.md#a8e48e5e195aea7f581cfc7246da79d72)

uint16\_t conn\_latency

**Definition** hci\_types.h:1054

[hci\_cp\_le\_conn\_update::conn\_interval\_max](structhci__cp__le__conn__update.md#a99fc0b3b0f810f1d6e174aa9045d298a)

uint16\_t conn\_interval\_max

**Definition** hci\_types.h:1053

[hci\_cp\_le\_conn\_update::supervision\_timeout](structhci__cp__le__conn__update.md#ab76ecdf6f7e5a5bb581cbd26f67d8f9f)

uint16\_t supervision\_timeout

**Definition** hci\_types.h:1055

[hci\_cp\_le\_conn\_update::conn\_interval\_min](structhci__cp__le__conn__update.md#adcfee3c727118069897515a00e7ead66)

uint16\_t conn\_interval\_min

**Definition** hci\_types.h:1052

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [hci\_types.h](hci__types_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/rpr_8h_source.html
original_path: doxygen/html/rpr_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rpr.h

[Go to the documentation of this file.](rpr_8h.md)

1/\*

2 \* Copyright (c) 2020 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_BT\_MESH\_RPR\_H\_\_

8#define ZEPHYR\_INCLUDE\_BT\_MESH\_RPR\_H\_\_

9

10#include <[zephyr/kernel.h](kernel_8h.md)>

11#include <[zephyr/bluetooth/mesh/main.h](main_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

22

[ 24](group__bt__mesh__rpr.md#ga94522cf0b3832b576100b787808474bd)#define BT\_MESH\_RPR\_UNPROV\_HASH BIT(0)

[ 25](group__bt__mesh__rpr.md#ga31bbb1483d5bdd10e0a9da0978bd90c0)#define BT\_MESH\_RPR\_UNPROV\_ACTIVE BIT(1)

[ 26](group__bt__mesh__rpr.md#gac33ea72f94eb986592941ca10b7884f1)#define BT\_MESH\_RPR\_UNPROV\_FOUND BIT(2)

[ 27](group__bt__mesh__rpr.md#ga8121bae9a6158a5f2df4bc154237e05b)#define BT\_MESH\_RPR\_UNPROV\_REPORTED BIT(3)

[ 28](group__bt__mesh__rpr.md#gac1eebae68c05d9e59599d0601055790d)#define BT\_MESH\_RPR\_UNPROV\_EXT BIT(4)

[ 29](group__bt__mesh__rpr.md#ga8349a9af764b3e502bf5ecd8bb0ce203)#define BT\_MESH\_RPR\_UNPROV\_HAS\_LINK BIT(5)

[ 30](group__bt__mesh__rpr.md#ga1dc95fc6baba79d9bc4007169fcfe55b)#define BT\_MESH\_RPR\_UNPROV\_EXT\_ADV\_RXD BIT(6)

31

[ 33](group__bt__mesh__rpr.md#ga2b7e2636da150f5c5cb4e3bdee13c745)#define BT\_MESH\_RPR\_EXT\_SCAN\_TIME\_MIN 1

[ 35](group__bt__mesh__rpr.md#ga2a5241b2e87fec227740dd4f2de3a68a)#define BT\_MESH\_RPR\_EXT\_SCAN\_TIME\_MAX 21

36

[ 37](group__bt__mesh__rpr.md#ga77d2f7158e7629dc54acafbf65e6af90)enum [bt\_mesh\_rpr\_status](group__bt__mesh__rpr.md#ga77d2f7158e7629dc54acafbf65e6af90) {

[ 38](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90a9375e568e9b69ab37484b91cfca75117) [BT\_MESH\_RPR\_SUCCESS](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90a9375e568e9b69ab37484b91cfca75117),

[ 39](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90aeec9abd5c000ea23fe9b7aa396f8b599) [BT\_MESH\_RPR\_ERR\_SCANNING\_CANNOT\_START](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90aeec9abd5c000ea23fe9b7aa396f8b599),

[ 40](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90ab5ff83c3503d6f709dfeb1423b957c26) [BT\_MESH\_RPR\_ERR\_INVALID\_STATE](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90ab5ff83c3503d6f709dfeb1423b957c26),

[ 41](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90abb00e5ea05d585e1350d2b46d2fdda82) [BT\_MESH\_RPR\_ERR\_LIMITED\_RESOURCES](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90abb00e5ea05d585e1350d2b46d2fdda82),

[ 42](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90a9297132714fd4a3a6e426a89da7205e3) [BT\_MESH\_RPR\_ERR\_LINK\_CANNOT\_OPEN](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90a9297132714fd4a3a6e426a89da7205e3),

[ 43](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90aedea52611aef2a72da9f41100d17edc4) [BT\_MESH\_RPR\_ERR\_LINK\_OPEN\_FAILED](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90aedea52611aef2a72da9f41100d17edc4),

[ 44](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90a7677dece8ef7018469a30ec33b8cf9c8) [BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_BY\_DEVICE](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90a7677dece8ef7018469a30ec33b8cf9c8),

[ 45](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90afe2ea78fee8b23c53d462f48ba530095) [BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_BY\_SERVER](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90afe2ea78fee8b23c53d462f48ba530095),

[ 46](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90a97dd7c06604a54aa508ee044c3ad86e3) [BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_BY\_CLIENT](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90a97dd7c06604a54aa508ee044c3ad86e3),

[ 47](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90aa91b75cfc7e8ed3dde00fb727bb91943) [BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_AS\_CANNOT\_RECEIVE\_PDU](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90aa91b75cfc7e8ed3dde00fb727bb91943),

[ 48](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90a5a0c58335ee0a2759de08c602d2922bb) [BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_AS\_CANNOT\_SEND\_PDU](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90a5a0c58335ee0a2759de08c602d2922bb),

[ 49](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90aed508e4f4a7f37c7804322a44037b0b4) [BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_AS\_CANNOT\_DELIVER\_PDU\_REPORT](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90aed508e4f4a7f37c7804322a44037b0b4),

50};

51

[ 52](group__bt__mesh__rpr.md#gabdc6782290a2c1652156e3f932e65291)enum [bt\_mesh\_rpr\_scan](group__bt__mesh__rpr.md#gabdc6782290a2c1652156e3f932e65291) {

[ 53](group__bt__mesh__rpr.md#ggabdc6782290a2c1652156e3f932e65291ad7b3cf3c950862565a8a6637448b3079) [BT\_MESH\_RPR\_SCAN\_IDLE](group__bt__mesh__rpr.md#ggabdc6782290a2c1652156e3f932e65291ad7b3cf3c950862565a8a6637448b3079),

[ 54](group__bt__mesh__rpr.md#ggabdc6782290a2c1652156e3f932e65291abb2fcc52856a2cf0b4315c253c498690) [BT\_MESH\_RPR\_SCAN\_MULTI](group__bt__mesh__rpr.md#ggabdc6782290a2c1652156e3f932e65291abb2fcc52856a2cf0b4315c253c498690),

[ 55](group__bt__mesh__rpr.md#ggabdc6782290a2c1652156e3f932e65291a3e732d2c256ec0c45b30b3623354c0fd) [BT\_MESH\_RPR\_SCAN\_SINGLE](group__bt__mesh__rpr.md#ggabdc6782290a2c1652156e3f932e65291a3e732d2c256ec0c45b30b3623354c0fd),

56};

57

[ 58](group__bt__mesh__rpr.md#gafef25a17e477638702ed742656b59573)enum [bt\_mesh\_rpr\_node\_refresh](group__bt__mesh__rpr.md#gafef25a17e477638702ed742656b59573) {

[ 60](group__bt__mesh__rpr.md#ggafef25a17e477638702ed742656b59573a9723efd45622d3a9ba7a2ae07dddb574) [BT\_MESH\_RPR\_NODE\_REFRESH\_DEVKEY](group__bt__mesh__rpr.md#ggafef25a17e477638702ed742656b59573a9723efd45622d3a9ba7a2ae07dddb574),

[ 62](group__bt__mesh__rpr.md#ggafef25a17e477638702ed742656b59573a52ff469f64d554cd31ee2228c542b7bf) [BT\_MESH\_RPR\_NODE\_REFRESH\_ADDR](group__bt__mesh__rpr.md#ggafef25a17e477638702ed742656b59573a52ff469f64d554cd31ee2228c542b7bf),

[ 64](group__bt__mesh__rpr.md#ggafef25a17e477638702ed742656b59573a700c5b506c4c85d12e578c0c5e3016b6) [BT\_MESH\_RPR\_NODE\_REFRESH\_COMPOSITION](group__bt__mesh__rpr.md#ggafef25a17e477638702ed742656b59573a700c5b506c4c85d12e578c0c5e3016b6),

65};

66

[ 67](group__bt__mesh__rpr.md#ga0266611238d10f8e97f2b07156991f43)enum [bt\_mesh\_rpr\_link\_state](group__bt__mesh__rpr.md#ga0266611238d10f8e97f2b07156991f43) {

[ 68](group__bt__mesh__rpr.md#gga0266611238d10f8e97f2b07156991f43a73441835adf51cd7c7cf57c36d4df4fb) [BT\_MESH\_RPR\_LINK\_IDLE](group__bt__mesh__rpr.md#gga0266611238d10f8e97f2b07156991f43a73441835adf51cd7c7cf57c36d4df4fb),

[ 69](group__bt__mesh__rpr.md#gga0266611238d10f8e97f2b07156991f43aaf2850d86c8f176c1a00afd14f9f70a9) [BT\_MESH\_RPR\_LINK\_OPENING](group__bt__mesh__rpr.md#gga0266611238d10f8e97f2b07156991f43aaf2850d86c8f176c1a00afd14f9f70a9),

[ 70](group__bt__mesh__rpr.md#gga0266611238d10f8e97f2b07156991f43a8821935b6e6ea3dcf40a81c285a19c36) [BT\_MESH\_RPR\_LINK\_ACTIVE](group__bt__mesh__rpr.md#gga0266611238d10f8e97f2b07156991f43a8821935b6e6ea3dcf40a81c285a19c36),

[ 71](group__bt__mesh__rpr.md#gga0266611238d10f8e97f2b07156991f43a6e0002cda37a86ecc1b4eb66c3b1cee7) [BT\_MESH\_RPR\_LINK\_SENDING](group__bt__mesh__rpr.md#gga0266611238d10f8e97f2b07156991f43a6e0002cda37a86ecc1b4eb66c3b1cee7),

[ 72](group__bt__mesh__rpr.md#gga0266611238d10f8e97f2b07156991f43a86e13d121f282d5b8e5ee7f2cd69d494) [BT\_MESH\_RPR\_LINK\_CLOSING](group__bt__mesh__rpr.md#gga0266611238d10f8e97f2b07156991f43a86e13d121f282d5b8e5ee7f2cd69d494),

73};

74

[ 76](structbt__mesh__rpr__node.md)struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) {

[ 78](structbt__mesh__rpr__node.md#a10ec7b9c480513e742566c6c3b9c4973) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr](structbt__mesh__rpr__node.md#a10ec7b9c480513e742566c6c3b9c4973);

[ 80](structbt__mesh__rpr__node.md#a2197a70aa97209a60136a09da1f513b2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_idx](structbt__mesh__rpr__node.md#a2197a70aa97209a60136a09da1f513b2);

[ 82](structbt__mesh__rpr__node.md#a4a73478764d4d15642475b8a822130af) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ttl](structbt__mesh__rpr__node.md#a4a73478764d4d15642475b8a822130af);

83};

84

[ 86](structbt__mesh__rpr__unprov.md)struct [bt\_mesh\_rpr\_unprov](structbt__mesh__rpr__unprov.md) {

[ 88](structbt__mesh__rpr__unprov.md#aa5fe6bad39edcb45d2e024c1c890c680) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [uuid](structbt__mesh__rpr__unprov.md#aa5fe6bad39edcb45d2e024c1c890c680)[16];

[ 90](structbt__mesh__rpr__unprov.md#a9d0103e4899b445c2c20d62749889e3e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structbt__mesh__rpr__unprov.md#a9d0103e4899b445c2c20d62749889e3e);

[ 92](structbt__mesh__rpr__unprov.md#a26ffffb174704a0a6a35418886e2a971) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__mesh__rpr__unprov.md#a26ffffb174704a0a6a35418886e2a971);

[ 94](structbt__mesh__rpr__unprov.md#a51e9bfeb3145c29644378d6ec5400e75) [bt\_mesh\_prov\_oob\_info\_t](group__bt__mesh__prov.md#gaf93f7b49dada5c3f7accc54663648e48) [oob](structbt__mesh__rpr__unprov.md#a51e9bfeb3145c29644378d6ec5400e75);

[ 99](structbt__mesh__rpr__unprov.md#ade58aed40bfaffb6f23a4e0570e370dd) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [hash](structbt__mesh__rpr__unprov.md#ade58aed40bfaffb6f23a4e0570e370dd);

100};

101

[ 103](structbt__mesh__rpr__link.md)struct [bt\_mesh\_rpr\_link](structbt__mesh__rpr__link.md) {

[ 105](structbt__mesh__rpr__link.md#a03387a0134a1364c0c2420064960eb03) enum [bt\_mesh\_rpr\_status](group__bt__mesh__rpr.md#ga77d2f7158e7629dc54acafbf65e6af90) [status](structbt__mesh__rpr__link.md#a03387a0134a1364c0c2420064960eb03);

[ 107](structbt__mesh__rpr__link.md#ade33cee01b4f4d2a3a82ed868895c173) enum [bt\_mesh\_rpr\_link\_state](group__bt__mesh__rpr.md#ga0266611238d10f8e97f2b07156991f43) [state](structbt__mesh__rpr__link.md#ade33cee01b4f4d2a3a82ed868895c173);

108};

109

111

112#ifdef \_\_cplusplus

113}

114#endif

115

116#endif /\* ZEPHYR\_INCLUDE\_BT\_MESH\_RPR\_H\_\_ \*/

[bt\_mesh\_prov\_oob\_info\_t](group__bt__mesh__prov.md#gaf93f7b49dada5c3f7accc54663648e48)

bt\_mesh\_prov\_oob\_info\_t

Out of Band information location.

**Definition** main.h:69

[bt\_mesh\_rpr\_link\_state](group__bt__mesh__rpr.md#ga0266611238d10f8e97f2b07156991f43)

bt\_mesh\_rpr\_link\_state

**Definition** rpr.h:67

[bt\_mesh\_rpr\_status](group__bt__mesh__rpr.md#ga77d2f7158e7629dc54acafbf65e6af90)

bt\_mesh\_rpr\_status

**Definition** rpr.h:37

[bt\_mesh\_rpr\_scan](group__bt__mesh__rpr.md#gabdc6782290a2c1652156e3f932e65291)

bt\_mesh\_rpr\_scan

**Definition** rpr.h:52

[bt\_mesh\_rpr\_node\_refresh](group__bt__mesh__rpr.md#gafef25a17e477638702ed742656b59573)

bt\_mesh\_rpr\_node\_refresh

**Definition** rpr.h:58

[BT\_MESH\_RPR\_LINK\_SENDING](group__bt__mesh__rpr.md#gga0266611238d10f8e97f2b07156991f43a6e0002cda37a86ecc1b4eb66c3b1cee7)

@ BT\_MESH\_RPR\_LINK\_SENDING

**Definition** rpr.h:71

[BT\_MESH\_RPR\_LINK\_IDLE](group__bt__mesh__rpr.md#gga0266611238d10f8e97f2b07156991f43a73441835adf51cd7c7cf57c36d4df4fb)

@ BT\_MESH\_RPR\_LINK\_IDLE

**Definition** rpr.h:68

[BT\_MESH\_RPR\_LINK\_CLOSING](group__bt__mesh__rpr.md#gga0266611238d10f8e97f2b07156991f43a86e13d121f282d5b8e5ee7f2cd69d494)

@ BT\_MESH\_RPR\_LINK\_CLOSING

**Definition** rpr.h:72

[BT\_MESH\_RPR\_LINK\_ACTIVE](group__bt__mesh__rpr.md#gga0266611238d10f8e97f2b07156991f43a8821935b6e6ea3dcf40a81c285a19c36)

@ BT\_MESH\_RPR\_LINK\_ACTIVE

**Definition** rpr.h:70

[BT\_MESH\_RPR\_LINK\_OPENING](group__bt__mesh__rpr.md#gga0266611238d10f8e97f2b07156991f43aaf2850d86c8f176c1a00afd14f9f70a9)

@ BT\_MESH\_RPR\_LINK\_OPENING

**Definition** rpr.h:69

[BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_AS\_CANNOT\_SEND\_PDU](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90a5a0c58335ee0a2759de08c602d2922bb)

@ BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_AS\_CANNOT\_SEND\_PDU

**Definition** rpr.h:48

[BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_BY\_DEVICE](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90a7677dece8ef7018469a30ec33b8cf9c8)

@ BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_BY\_DEVICE

**Definition** rpr.h:44

[BT\_MESH\_RPR\_ERR\_LINK\_CANNOT\_OPEN](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90a9297132714fd4a3a6e426a89da7205e3)

@ BT\_MESH\_RPR\_ERR\_LINK\_CANNOT\_OPEN

**Definition** rpr.h:42

[BT\_MESH\_RPR\_SUCCESS](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90a9375e568e9b69ab37484b91cfca75117)

@ BT\_MESH\_RPR\_SUCCESS

**Definition** rpr.h:38

[BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_BY\_CLIENT](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90a97dd7c06604a54aa508ee044c3ad86e3)

@ BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_BY\_CLIENT

**Definition** rpr.h:46

[BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_AS\_CANNOT\_RECEIVE\_PDU](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90aa91b75cfc7e8ed3dde00fb727bb91943)

@ BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_AS\_CANNOT\_RECEIVE\_PDU

**Definition** rpr.h:47

[BT\_MESH\_RPR\_ERR\_INVALID\_STATE](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90ab5ff83c3503d6f709dfeb1423b957c26)

@ BT\_MESH\_RPR\_ERR\_INVALID\_STATE

**Definition** rpr.h:40

[BT\_MESH\_RPR\_ERR\_LIMITED\_RESOURCES](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90abb00e5ea05d585e1350d2b46d2fdda82)

@ BT\_MESH\_RPR\_ERR\_LIMITED\_RESOURCES

**Definition** rpr.h:41

[BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_AS\_CANNOT\_DELIVER\_PDU\_REPORT](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90aed508e4f4a7f37c7804322a44037b0b4)

@ BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_AS\_CANNOT\_DELIVER\_PDU\_REPORT

**Definition** rpr.h:49

[BT\_MESH\_RPR\_ERR\_LINK\_OPEN\_FAILED](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90aedea52611aef2a72da9f41100d17edc4)

@ BT\_MESH\_RPR\_ERR\_LINK\_OPEN\_FAILED

**Definition** rpr.h:43

[BT\_MESH\_RPR\_ERR\_SCANNING\_CANNOT\_START](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90aeec9abd5c000ea23fe9b7aa396f8b599)

@ BT\_MESH\_RPR\_ERR\_SCANNING\_CANNOT\_START

**Definition** rpr.h:39

[BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_BY\_SERVER](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90afe2ea78fee8b23c53d462f48ba530095)

@ BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_BY\_SERVER

**Definition** rpr.h:45

[BT\_MESH\_RPR\_SCAN\_SINGLE](group__bt__mesh__rpr.md#ggabdc6782290a2c1652156e3f932e65291a3e732d2c256ec0c45b30b3623354c0fd)

@ BT\_MESH\_RPR\_SCAN\_SINGLE

**Definition** rpr.h:55

[BT\_MESH\_RPR\_SCAN\_MULTI](group__bt__mesh__rpr.md#ggabdc6782290a2c1652156e3f932e65291abb2fcc52856a2cf0b4315c253c498690)

@ BT\_MESH\_RPR\_SCAN\_MULTI

**Definition** rpr.h:54

[BT\_MESH\_RPR\_SCAN\_IDLE](group__bt__mesh__rpr.md#ggabdc6782290a2c1652156e3f932e65291ad7b3cf3c950862565a8a6637448b3079)

@ BT\_MESH\_RPR\_SCAN\_IDLE

**Definition** rpr.h:53

[BT\_MESH\_RPR\_NODE\_REFRESH\_ADDR](group__bt__mesh__rpr.md#ggafef25a17e477638702ed742656b59573a52ff469f64d554cd31ee2228c542b7bf)

@ BT\_MESH\_RPR\_NODE\_REFRESH\_ADDR

Change the Device key and address.

**Definition** rpr.h:62

[BT\_MESH\_RPR\_NODE\_REFRESH\_COMPOSITION](group__bt__mesh__rpr.md#ggafef25a17e477638702ed742656b59573a700c5b506c4c85d12e578c0c5e3016b6)

@ BT\_MESH\_RPR\_NODE\_REFRESH\_COMPOSITION

Change the Device key and composition.

**Definition** rpr.h:64

[BT\_MESH\_RPR\_NODE\_REFRESH\_DEVKEY](group__bt__mesh__rpr.md#ggafef25a17e477638702ed742656b59573a9723efd45622d3a9ba7a2ae07dddb574)

@ BT\_MESH\_RPR\_NODE\_REFRESH\_DEVKEY

Change the Device key.

**Definition** rpr.h:60

[kernel.h](kernel_8h.md)

Public kernel APIs.

[main.h](main_8h.md)

Bluetooth Mesh Protocol APIs.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[bt\_mesh\_rpr\_link](structbt__mesh__rpr__link.md)

Remote Provisioning Link status.

**Definition** rpr.h:103

[bt\_mesh\_rpr\_link::status](structbt__mesh__rpr__link.md#a03387a0134a1364c0c2420064960eb03)

enum bt\_mesh\_rpr\_status status

Link status.

**Definition** rpr.h:105

[bt\_mesh\_rpr\_link::state](structbt__mesh__rpr__link.md#ade33cee01b4f4d2a3a82ed868895c173)

enum bt\_mesh\_rpr\_link\_state state

Link state.

**Definition** rpr.h:107

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

[bt\_mesh\_rpr\_node::ttl](structbt__mesh__rpr__node.md#a4a73478764d4d15642475b8a822130af)

uint8\_t ttl

Time To Live value used when communicating with the node.

**Definition** rpr.h:82

[bt\_mesh\_rpr\_unprov](structbt__mesh__rpr__unprov.md)

Unprovisioned device.

**Definition** rpr.h:86

[bt\_mesh\_rpr\_unprov::rssi](structbt__mesh__rpr__unprov.md#a26ffffb174704a0a6a35418886e2a971)

int8\_t rssi

RSSI of unprovisioned device, as received by server.

**Definition** rpr.h:92

[bt\_mesh\_rpr\_unprov::oob](structbt__mesh__rpr__unprov.md#a51e9bfeb3145c29644378d6ec5400e75)

bt\_mesh\_prov\_oob\_info\_t oob

Out of band information.

**Definition** rpr.h:94

[bt\_mesh\_rpr\_unprov::flags](structbt__mesh__rpr__unprov.md#a9d0103e4899b445c2c20d62749889e3e)

uint8\_t flags

Flags, see BT\_MESH\_RPR\_UNPROV\_\* flags.

**Definition** rpr.h:90

[bt\_mesh\_rpr\_unprov::uuid](structbt__mesh__rpr__unprov.md#aa5fe6bad39edcb45d2e024c1c890c680)

uint8\_t uuid[16]

Unprovisioned device UUID.

**Definition** rpr.h:88

[bt\_mesh\_rpr\_unprov::hash](structbt__mesh__rpr__unprov.md#ade58aed40bfaffb6f23a4e0570e370dd)

uint32\_t hash

URI hash in unprovisioned beacon.

**Definition** rpr.h:99

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [rpr.h](rpr_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

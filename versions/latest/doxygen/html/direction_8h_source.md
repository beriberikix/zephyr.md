---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/direction_8h_source.html
original_path: doxygen/html/direction_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

direction.h

[Go to the documentation of this file.](direction_8h.md)

1/\*

2 \* Copyright (c) 2020 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_DF\_H\_

8#define ZEPHYR\_INCLUDE\_BLUETOOTH\_DF\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11

12#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h.md)>

13#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

14

[ 16](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05)enum [bt\_df\_cte\_type](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05) {

[ 18](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05a1f24630a9b6afc19e1f671a4b5906dd1) [BT\_DF\_CTE\_TYPE\_NONE](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05a1f24630a9b6afc19e1f671a4b5906dd1) = 0,

[ 20](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05a6c91466a8e8dfe73665749b263b26207) [BT\_DF\_CTE\_TYPE\_AOA](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05a6c91466a8e8dfe73665749b263b26207) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 26](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05a331e4cc8da9f583ad18422cd260018da) [BT\_DF\_CTE\_TYPE\_AOD\_1US](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05a331e4cc8da9f583ad18422cd260018da) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 32](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05aeeb9304adba4363faaa8e3d299abfdb8) [BT\_DF\_CTE\_TYPE\_AOD\_2US](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05aeeb9304adba4363faaa8e3d299abfdb8) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 34](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05a3e1c5452412a00c994ad005858e03ac7) [BT\_DF\_CTE\_TYPE\_ALL](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05a3e1c5452412a00c994ad005858e03ac7) = ([BT\_DF\_CTE\_TYPE\_AOA](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05a6c91466a8e8dfe73665749b263b26207) | [BT\_DF\_CTE\_TYPE\_AOD\_1US](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05a331e4cc8da9f583ad18422cd260018da) | [BT\_DF\_CTE\_TYPE\_AOD\_2US](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05aeeb9304adba4363faaa8e3d299abfdb8))

35};

36

[ 38](direction_8h.md#a546598ce9a81161ad1ba098a7b1a8df4)enum [bt\_df\_antenna\_switching\_slot](direction_8h.md#a546598ce9a81161ad1ba098a7b1a8df4) {

[ 39](direction_8h.md#a546598ce9a81161ad1ba098a7b1a8df4a68c89c394d7a1d92560a1e51fa1b069a) [BT\_DF\_ANTENNA\_SWITCHING\_SLOT\_1US](direction_8h.md#a546598ce9a81161ad1ba098a7b1a8df4a68c89c394d7a1d92560a1e51fa1b069a) = 0x1,

[ 40](direction_8h.md#a546598ce9a81161ad1ba098a7b1a8df4ad59a9caab9aeced1f95dd1fe8778fe38) [BT\_DF\_ANTENNA\_SWITCHING\_SLOT\_2US](direction_8h.md#a546598ce9a81161ad1ba098a7b1a8df4ad59a9caab9aeced1f95dd1fe8778fe38) = 0x2

41};

42

[ 44](direction_8h.md#ab9acadbaf03dd976a2ee185574effb4c)enum [bt\_df\_packet\_status](direction_8h.md#ab9acadbaf03dd976a2ee185574effb4c) {

[ 46](direction_8h.md#ab9acadbaf03dd976a2ee185574effb4ca10328e978a6641f5f787f4f4e9b50d6c) [BT\_DF\_CTE\_CRC\_OK](direction_8h.md#ab9acadbaf03dd976a2ee185574effb4ca10328e978a6641f5f787f4f4e9b50d6c) = 0x0,

[ 51](direction_8h.md#ab9acadbaf03dd976a2ee185574effb4cadf830cbbe3043423eff237b983bf1c92) [BT\_DF\_CTE\_CRC\_ERR\_CTE\_BASED\_TIME](direction_8h.md#ab9acadbaf03dd976a2ee185574effb4cadf830cbbe3043423eff237b983bf1c92) = 0x1,

[ 55](direction_8h.md#ab9acadbaf03dd976a2ee185574effb4cacdc558d9892228b4403cb782ed2260f9) [BT\_DF\_CTE\_CRC\_ERR\_CTE\_BASED\_OTHER](direction_8h.md#ab9acadbaf03dd976a2ee185574effb4cacdc558d9892228b4403cb782ed2260f9) = 0x2,

[ 57](direction_8h.md#ab9acadbaf03dd976a2ee185574effb4ca70ea13abb5e1626304f8ef4e22564a8b) [BT\_DF\_CTE\_INSUFFICIENT\_RESOURCES](direction_8h.md#ab9acadbaf03dd976a2ee185574effb4ca70ea13abb5e1626304f8ef4e22564a8b) = 0xFF

58};

59

[ 66](structbt__df__adv__cte__tx__param.md)struct [bt\_df\_adv\_cte\_tx\_param](structbt__df__adv__cte__tx__param.md) {

[ 68](structbt__df__adv__cte__tx__param.md#a2ab62db4279338e05cd9e5c222c3aab2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_len](structbt__df__adv__cte__tx__param.md#a2ab62db4279338e05cd9e5c222c3aab2);

[ 75](structbt__df__adv__cte__tx__param.md#a4af32abbb603d1b7a533771a23d6e9ee) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__df__adv__cte__tx__param.md#a4af32abbb603d1b7a533771a23d6e9ee);

[ 77](structbt__df__adv__cte__tx__param.md#a288d635221a752b231033803acddd261) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_count](structbt__df__adv__cte__tx__param.md#a288d635221a752b231033803acddd261);

[ 79](structbt__df__adv__cte__tx__param.md#ac974c5bb804912f5940b2ede5f6394a1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_ant\_ids](structbt__df__adv__cte__tx__param.md#ac974c5bb804912f5940b2ede5f6394a1);

[ 81](structbt__df__adv__cte__tx__param.md#ac1f251cb2205ce345dc3815b53f13918) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[ant\_ids](structbt__df__adv__cte__tx__param.md#ac1f251cb2205ce345dc3815b53f13918);

82};

83

[ 92](structbt__df__per__adv__sync__cte__rx__param.md)struct [bt\_df\_per\_adv\_sync\_cte\_rx\_param](structbt__df__per__adv__sync__cte__rx__param.md) {

[ 98](structbt__df__per__adv__sync__cte__rx__param.md#a1740d3f41dddd755fc1e04216c8070e5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_types](structbt__df__per__adv__sync__cte__rx__param.md#a1740d3f41dddd755fc1e04216c8070e5);

[ 100](structbt__df__per__adv__sync__cte__rx__param.md#abff68c9f2e42e3fe6e8b155f5390f219) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [slot\_durations](structbt__df__per__adv__sync__cte__rx__param.md#abff68c9f2e42e3fe6e8b155f5390f219);

[ 102](structbt__df__per__adv__sync__cte__rx__param.md#ac64232b5e9b2c6acfadfca1c95fd1021) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_cte\_count](structbt__df__per__adv__sync__cte__rx__param.md#ac64232b5e9b2c6acfadfca1c95fd1021);

[ 104](structbt__df__per__adv__sync__cte__rx__param.md#ae358cbd7b1dd59a7d0a931c8a5fbd94d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_ant\_ids](structbt__df__per__adv__sync__cte__rx__param.md#ae358cbd7b1dd59a7d0a931c8a5fbd94d);

[ 106](structbt__df__per__adv__sync__cte__rx__param.md#ac83de1a86fef076d6c8fc6bccbe49a64) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[ant\_ids](structbt__df__per__adv__sync__cte__rx__param.md#ac83de1a86fef076d6c8fc6bccbe49a64);

107};

108

[ 109](direction_8h.md#a53df7da4b178b4a6e4dd68e9266c0771)enum [bt\_df\_iq\_sample](direction_8h.md#a53df7da4b178b4a6e4dd68e9266c0771) {

[ 113](direction_8h.md#a53df7da4b178b4a6e4dd68e9266c0771a82ee06924dbf1fd3f9c68891b1ccdef4) [BT\_DF\_IQ\_SAMPLE\_8\_BITS\_INT](direction_8h.md#a53df7da4b178b4a6e4dd68e9266c0771a82ee06924dbf1fd3f9c68891b1ccdef4),

[ 115](direction_8h.md#a53df7da4b178b4a6e4dd68e9266c0771a25db2bd4a02678b2ea026ec47b6c2b1b) [BT\_DF\_IQ\_SAMPLE\_16\_BITS\_INT](direction_8h.md#a53df7da4b178b4a6e4dd68e9266c0771a25db2bd4a02678b2ea026ec47b6c2b1b),

116};

117

[ 118](structbt__df__per__adv__sync__iq__samples__report.md)struct [bt\_df\_per\_adv\_sync\_iq\_samples\_report](structbt__df__per__adv__sync__iq__samples__report.md) {

[ 120](structbt__df__per__adv__sync__iq__samples__report.md#ad4d213aa20a0c2fe329606ed789436fd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [chan\_idx](structbt__df__per__adv__sync__iq__samples__report.md#ad4d213aa20a0c2fe329606ed789436fd);

[ 122](structbt__df__per__adv__sync__iq__samples__report.md#a48793aad0f603d1763f06453e837a9d9) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [rssi](structbt__df__per__adv__sync__iq__samples__report.md#a48793aad0f603d1763f06453e837a9d9);

[ 124](structbt__df__per__adv__sync__iq__samples__report.md#a0b07042bad2a28065b8ea4def73c91d3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rssi\_ant\_id](structbt__df__per__adv__sync__iq__samples__report.md#a0b07042bad2a28065b8ea4def73c91d3);

[ 126](structbt__df__per__adv__sync__iq__samples__report.md#aa81e74769290f427b60398eb976b4a2a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__df__per__adv__sync__iq__samples__report.md#aa81e74769290f427b60398eb976b4a2a);

[ 128](structbt__df__per__adv__sync__iq__samples__report.md#ab256dc21c5d707a9195967caaa13e3e0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [slot\_durations](structbt__df__per__adv__sync__iq__samples__report.md#ab256dc21c5d707a9195967caaa13e3e0);

[ 130](structbt__df__per__adv__sync__iq__samples__report.md#a6fea28c1d3b00f1fd7bcb7264f4c3fc9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_status](structbt__df__per__adv__sync__iq__samples__report.md#a6fea28c1d3b00f1fd7bcb7264f4c3fc9);

[ 132](structbt__df__per__adv__sync__iq__samples__report.md#a1a9c763fa7dd445b5dea8c2bb7b82bc0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [per\_evt\_counter](structbt__df__per__adv__sync__iq__samples__report.md#a1a9c763fa7dd445b5dea8c2bb7b82bc0);

[ 134](structbt__df__per__adv__sync__iq__samples__report.md#a4d1da7208e043f5ae015612cee16ee25) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sample\_count](structbt__df__per__adv__sync__iq__samples__report.md#a4d1da7208e043f5ae015612cee16ee25);

[ 136](structbt__df__per__adv__sync__iq__samples__report.md#a88d950cdaa4f08a0fa3eb26f1fed7982) enum [bt\_df\_iq\_sample](direction_8h.md#a53df7da4b178b4a6e4dd68e9266c0771) [sample\_type](structbt__df__per__adv__sync__iq__samples__report.md#a88d950cdaa4f08a0fa3eb26f1fed7982);

138 union {

[ 139](structbt__df__per__adv__sync__iq__samples__report.md#a64c2936dc8180fc34651b18199241a9b) struct [bt\_hci\_le\_iq\_sample](structbt__hci__le__iq__sample.md) const \*[sample](structbt__df__per__adv__sync__iq__samples__report.md#a64c2936dc8180fc34651b18199241a9b);

[ 140](structbt__df__per__adv__sync__iq__samples__report.md#ae0a28844a5588af05bbde046f6355ddf) struct [bt\_hci\_le\_iq\_sample16](structbt__hci__le__iq__sample16.md) const \*[sample16](structbt__df__per__adv__sync__iq__samples__report.md#ae0a28844a5588af05bbde046f6355ddf);

141 };

142};

143

[ 144](structbt__df__conn__cte__rx__param.md)struct [bt\_df\_conn\_cte\_rx\_param](structbt__df__conn__cte__rx__param.md) {

[ 150](structbt__df__conn__cte__rx__param.md#a3401f31865ced48d89c2b4560bcd4512) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_types](structbt__df__conn__cte__rx__param.md#a3401f31865ced48d89c2b4560bcd4512);

[ 152](structbt__df__conn__cte__rx__param.md#afe2dae75b7138b374f991c58f8143c9d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [slot\_durations](structbt__df__conn__cte__rx__param.md#afe2dae75b7138b374f991c58f8143c9d);

[ 154](structbt__df__conn__cte__rx__param.md#aee2ed2d86e2740e166434ede099b1250) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_ant\_ids](structbt__df__conn__cte__rx__param.md#aee2ed2d86e2740e166434ede099b1250);

[ 156](structbt__df__conn__cte__rx__param.md#a35c2aac4512e2ffce19346c9bf51f033) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[ant\_ids](structbt__df__conn__cte__rx__param.md#a35c2aac4512e2ffce19346c9bf51f033);

157};

158

[ 159](direction_8h.md#a953634e6a88617a8729541d6b5bd0dd6)enum [bt\_df\_conn\_iq\_report\_err](direction_8h.md#a953634e6a88617a8729541d6b5bd0dd6) {

[ 161](direction_8h.md#a953634e6a88617a8729541d6b5bd0dd6acd6f87bd43540cc1b44e5e023a4d0519) [BT\_DF\_IQ\_REPORT\_ERR\_SUCCESS](direction_8h.md#a953634e6a88617a8729541d6b5bd0dd6acd6f87bd43540cc1b44e5e023a4d0519),

[ 163](direction_8h.md#a953634e6a88617a8729541d6b5bd0dd6a53596e4aa9a96006cee3c899150d7a0e) [BT\_DF\_IQ\_REPORT\_ERR\_NO\_CTE](direction_8h.md#a953634e6a88617a8729541d6b5bd0dd6a53596e4aa9a96006cee3c899150d7a0e),

[ 165](direction_8h.md#a953634e6a88617a8729541d6b5bd0dd6a7f3f42ede92bafd169620bebddc75512) [BT\_DF\_IQ\_REPORT\_ERR\_PEER\_REJECTED](direction_8h.md#a953634e6a88617a8729541d6b5bd0dd6a7f3f42ede92bafd169620bebddc75512),

166};

167

[ 168](structbt__df__conn__iq__samples__report.md)struct [bt\_df\_conn\_iq\_samples\_report](structbt__df__conn__iq__samples__report.md) {

[ 170](structbt__df__conn__iq__samples__report.md#ab6e31e979bba969a18804cf8c9b88f03) enum [bt\_df\_conn\_iq\_report\_err](direction_8h.md#a953634e6a88617a8729541d6b5bd0dd6) [err](structbt__df__conn__iq__samples__report.md#ab6e31e979bba969a18804cf8c9b88f03);

[ 172](structbt__df__conn__iq__samples__report.md#ac14e792a3ce2f3297ddab49e801ba640) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_phy](structbt__df__conn__iq__samples__report.md#ac14e792a3ce2f3297ddab49e801ba640);

[ 174](structbt__df__conn__iq__samples__report.md#a9374ecd1437f532dec863c527d22348d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [chan\_idx](structbt__df__conn__iq__samples__report.md#a9374ecd1437f532dec863c527d22348d);

[ 176](structbt__df__conn__iq__samples__report.md#aac825fbdecd6a5a82da0097a8694fb65) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [rssi](structbt__df__conn__iq__samples__report.md#aac825fbdecd6a5a82da0097a8694fb65);

[ 178](structbt__df__conn__iq__samples__report.md#a7c5147b426bb87f9d11c8bdffb91ff02) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rssi\_ant\_id](structbt__df__conn__iq__samples__report.md#a7c5147b426bb87f9d11c8bdffb91ff02);

[ 180](structbt__df__conn__iq__samples__report.md#a4d467a7ac76dc9ed6331c10172895097) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__df__conn__iq__samples__report.md#a4d467a7ac76dc9ed6331c10172895097);

[ 182](structbt__df__conn__iq__samples__report.md#a578132e4a88e739451cf80eba7345094) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [slot\_durations](structbt__df__conn__iq__samples__report.md#a578132e4a88e739451cf80eba7345094);

[ 184](structbt__df__conn__iq__samples__report.md#afdc456a8af5a31ee62c489534af3ecdb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_status](structbt__df__conn__iq__samples__report.md#afdc456a8af5a31ee62c489534af3ecdb);

[ 186](structbt__df__conn__iq__samples__report.md#ac7f3993bd20bd44354f15f098e423c33) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_evt\_counter](structbt__df__conn__iq__samples__report.md#ac7f3993bd20bd44354f15f098e423c33);

[ 188](structbt__df__conn__iq__samples__report.md#a1e7901b81c8618e4515cd22a681b4d43) enum [bt\_df\_iq\_sample](direction_8h.md#a53df7da4b178b4a6e4dd68e9266c0771) [sample\_type](structbt__df__conn__iq__samples__report.md#a1e7901b81c8618e4515cd22a681b4d43);

[ 190](structbt__df__conn__iq__samples__report.md#a60500e954e2694a209c2d103887b2685) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sample\_count](structbt__df__conn__iq__samples__report.md#a60500e954e2694a209c2d103887b2685);

192 union {

[ 193](structbt__df__conn__iq__samples__report.md#aa9b177817075e3781256ec2c7d5ac0ce) struct [bt\_hci\_le\_iq\_sample](structbt__hci__le__iq__sample.md) const \*[sample](structbt__df__conn__iq__samples__report.md#aa9b177817075e3781256ec2c7d5ac0ce);

[ 194](structbt__df__conn__iq__samples__report.md#a55e1d7d31557f0e1f59ad91834460b78) struct [bt\_hci\_le\_iq\_sample16](structbt__hci__le__iq__sample16.md) const \*[sample16](structbt__df__conn__iq__samples__report.md#a55e1d7d31557f0e1f59ad91834460b78);

195 };

196};

197

[ 198](structbt__df__conn__cte__tx__param.md)struct [bt\_df\_conn\_cte\_tx\_param](structbt__df__conn__cte__tx__param.md) {

[ 203](structbt__df__conn__cte__tx__param.md#af78df8115d2fac5b8f6132b48a56bc1c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_types](structbt__df__conn__cte__tx__param.md#af78df8115d2fac5b8f6132b48a56bc1c);

[ 205](structbt__df__conn__cte__tx__param.md#ad49bc64170e8ee4741aa01393284e7de) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_ant\_ids](structbt__df__conn__cte__tx__param.md#ad49bc64170e8ee4741aa01393284e7de);

[ 207](structbt__df__conn__cte__tx__param.md#a9df1dac6180e77a4c7abc80890346c4a) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[ant\_ids](structbt__df__conn__cte__tx__param.md#a9df1dac6180e77a4c7abc80890346c4a);

208};

209

[ 210](structbt__df__conn__cte__req__params.md)struct [bt\_df\_conn\_cte\_req\_params](structbt__df__conn__cte__req__params.md) {

[ 217](structbt__df__conn__cte__req__params.md#ab8148905943e0d87a37740ab891b9ef7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__df__conn__cte__req__params.md#ab8148905943e0d87a37740ab891b9ef7);

[ 219](structbt__df__conn__cte__req__params.md#a71340a450e573612a271467c51110166) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_length](structbt__df__conn__cte__req__params.md#a71340a450e573612a271467c51110166);

[ 226](structbt__df__conn__cte__req__params.md#ae8232614ec9201e4572675d793b2292a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__df__conn__cte__req__params.md#ae8232614ec9201e4572675d793b2292a);

227};

228

[ 237](direction_8h.md#ae98248377f111deb6aa0565db1d3f690)int [bt\_df\_set\_adv\_cte\_tx\_param](direction_8h.md#ae98248377f111deb6aa0565db1d3f690)(struct bt\_le\_ext\_adv \*adv,

238 const struct [bt\_df\_adv\_cte\_tx\_param](structbt__df__adv__cte__tx__param.md) \*params);

239

[ 251](direction_8h.md#ab03ec552192056eb8ddb9aae49029265)int [bt\_df\_adv\_cte\_tx\_enable](direction_8h.md#ab03ec552192056eb8ddb9aae49029265)(struct bt\_le\_ext\_adv \*adv);

252

[ 260](direction_8h.md#a248cd22ad9afe050e3d535f7124112d9)int [bt\_df\_adv\_cte\_tx\_disable](direction_8h.md#a248cd22ad9afe050e3d535f7124112d9)(struct bt\_le\_ext\_adv \*adv);

261

[ 273](direction_8h.md#a26c40ea36de60266f029763551cd9d4e)int [bt\_df\_per\_adv\_sync\_cte\_rx\_enable](direction_8h.md#a26c40ea36de60266f029763551cd9d4e)(struct bt\_le\_per\_adv\_sync \*sync,

274 const struct [bt\_df\_per\_adv\_sync\_cte\_rx\_param](structbt__df__per__adv__sync__cte__rx__param.md) \*params);

275

[ 283](direction_8h.md#ac2064484bb3c4ea6ae5eb684f3ace008)int [bt\_df\_per\_adv\_sync\_cte\_rx\_disable](direction_8h.md#ac2064484bb3c4ea6ae5eb684f3ace008)(struct bt\_le\_per\_adv\_sync \*sync);

284

[ 293](direction_8h.md#a92d0b485a83a7395b3613b144b6e749f)int [bt\_df\_conn\_cte\_rx\_enable](direction_8h.md#a92d0b485a83a7395b3613b144b6e749f)(struct bt\_conn \*conn, const struct [bt\_df\_conn\_cte\_rx\_param](structbt__df__conn__cte__rx__param.md) \*params);

294

[ 302](direction_8h.md#a861696041baa770ef3968789afd4cbac)int [bt\_df\_conn\_cte\_rx\_disable](direction_8h.md#a861696041baa770ef3968789afd4cbac)(struct bt\_conn \*conn);

303

[ 318](direction_8h.md#aa0eba41c1a810c9592e0097ee4fe7329)int [bt\_df\_set\_conn\_cte\_tx\_param](direction_8h.md#aa0eba41c1a810c9592e0097ee4fe7329)(struct bt\_conn \*conn, const struct [bt\_df\_conn\_cte\_tx\_param](structbt__df__conn__cte__tx__param.md) \*params);

319

[ 330](direction_8h.md#a84fee1f1ac25af73bb7a8f91ed912c67)int [bt\_df\_conn\_cte\_req\_enable](direction_8h.md#a84fee1f1ac25af73bb7a8f91ed912c67)(struct bt\_conn \*conn, const struct [bt\_df\_conn\_cte\_req\_params](structbt__df__conn__cte__req__params.md) \*params);

331

[ 341](direction_8h.md#ade1a048c3fdf11e979fa9a74f33bc375)int [bt\_df\_conn\_cte\_req\_disable](direction_8h.md#ade1a048c3fdf11e979fa9a74f33bc375)(struct bt\_conn \*conn);

342

[ 352](direction_8h.md#a5e4a5168020d488561646beac48916f5)int [bt\_df\_conn\_cte\_rsp\_enable](direction_8h.md#a5e4a5168020d488561646beac48916f5)(struct bt\_conn \*conn);

353

[ 363](direction_8h.md#a856cfbe26fba92c80f4cf6012a0bbafe)int [bt\_df\_conn\_cte\_rsp\_disable](direction_8h.md#a856cfbe26fba92c80f4cf6012a0bbafe)(struct bt\_conn \*conn);

364

365#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_DF\_H\_ \*/

[bluetooth.h](bluetooth_2bluetooth_8h.md)

Bluetooth subsystem core APIs.

[bt\_df\_adv\_cte\_tx\_disable](direction_8h.md#a248cd22ad9afe050e3d535f7124112d9)

int bt\_df\_adv\_cte\_tx\_disable(struct bt\_le\_ext\_adv \*adv)

Disable transmission of Constant Tone Extension for the given advertising set.

[bt\_df\_per\_adv\_sync\_cte\_rx\_enable](direction_8h.md#a26c40ea36de60266f029763551cd9d4e)

int bt\_df\_per\_adv\_sync\_cte\_rx\_enable(struct bt\_le\_per\_adv\_sync \*sync, const struct bt\_df\_per\_adv\_sync\_cte\_rx\_param \*params)

Enable receive and sampling of Constant Tone Extension for the given sync set.

[bt\_df\_iq\_sample](direction_8h.md#a53df7da4b178b4a6e4dd68e9266c0771)

bt\_df\_iq\_sample

**Definition** direction.h:109

[BT\_DF\_IQ\_SAMPLE\_16\_BITS\_INT](direction_8h.md#a53df7da4b178b4a6e4dd68e9266c0771a25db2bd4a02678b2ea026ec47b6c2b1b)

@ BT\_DF\_IQ\_SAMPLE\_16\_BITS\_INT

Reported IQ samples have 16 bits signed integer format.

**Definition** direction.h:115

[BT\_DF\_IQ\_SAMPLE\_8\_BITS\_INT](direction_8h.md#a53df7da4b178b4a6e4dd68e9266c0771a82ee06924dbf1fd3f9c68891b1ccdef4)

@ BT\_DF\_IQ\_SAMPLE\_8\_BITS\_INT

Reported IQ samples have 8 bits signed integer format.

**Definition** direction.h:113

[bt\_df\_antenna\_switching\_slot](direction_8h.md#a546598ce9a81161ad1ba098a7b1a8df4)

bt\_df\_antenna\_switching\_slot

Allowed antenna switching slots: 1 us or 2 us.

**Definition** direction.h:38

[BT\_DF\_ANTENNA\_SWITCHING\_SLOT\_1US](direction_8h.md#a546598ce9a81161ad1ba098a7b1a8df4a68c89c394d7a1d92560a1e51fa1b069a)

@ BT\_DF\_ANTENNA\_SWITCHING\_SLOT\_1US

**Definition** direction.h:39

[BT\_DF\_ANTENNA\_SWITCHING\_SLOT\_2US](direction_8h.md#a546598ce9a81161ad1ba098a7b1a8df4ad59a9caab9aeced1f95dd1fe8778fe38)

@ BT\_DF\_ANTENNA\_SWITCHING\_SLOT\_2US

**Definition** direction.h:40

[bt\_df\_conn\_cte\_rsp\_enable](direction_8h.md#a5e4a5168020d488561646beac48916f5)

int bt\_df\_conn\_cte\_rsp\_enable(struct bt\_conn \*conn)

Enable Constant Tone Extension response procedure for a connection.

[bt\_df\_cte\_type](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05)

bt\_df\_cte\_type

Constant Tone Extension (CTE) types.

**Definition** direction.h:16

[BT\_DF\_CTE\_TYPE\_NONE](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05a1f24630a9b6afc19e1f671a4b5906dd1)

@ BT\_DF\_CTE\_TYPE\_NONE

Convenience value for purposes where non of CTE types is allowed.

**Definition** direction.h:18

[BT\_DF\_CTE\_TYPE\_AOD\_1US](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05a331e4cc8da9f583ad18422cd260018da)

@ BT\_DF\_CTE\_TYPE\_AOD\_1US

Angle of Departure mode with 1 us antenna switching slots.

**Definition** direction.h:26

[BT\_DF\_CTE\_TYPE\_ALL](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05a3e1c5452412a00c994ad005858e03ac7)

@ BT\_DF\_CTE\_TYPE\_ALL

Convenience value that collects all possible CTE types in one entry.

**Definition** direction.h:34

[BT\_DF\_CTE\_TYPE\_AOA](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05a6c91466a8e8dfe73665749b263b26207)

@ BT\_DF\_CTE\_TYPE\_AOA

Angle of Arrival mode.

**Definition** direction.h:20

[BT\_DF\_CTE\_TYPE\_AOD\_2US](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05aeeb9304adba4363faaa8e3d299abfdb8)

@ BT\_DF\_CTE\_TYPE\_AOD\_2US

Angle of Departure mode with 2 us antenna switching slots.

**Definition** direction.h:32

[bt\_df\_conn\_cte\_req\_enable](direction_8h.md#a84fee1f1ac25af73bb7a8f91ed912c67)

int bt\_df\_conn\_cte\_req\_enable(struct bt\_conn \*conn, const struct bt\_df\_conn\_cte\_req\_params \*params)

Enable Constant Tone Extension request procedure for a connection.

[bt\_df\_conn\_cte\_rsp\_disable](direction_8h.md#a856cfbe26fba92c80f4cf6012a0bbafe)

int bt\_df\_conn\_cte\_rsp\_disable(struct bt\_conn \*conn)

Disable Constant Tone Extension response procedure for a connection.

[bt\_df\_conn\_cte\_rx\_disable](direction_8h.md#a861696041baa770ef3968789afd4cbac)

int bt\_df\_conn\_cte\_rx\_disable(struct bt\_conn \*conn)

Disable receive and sampling of Constant Tone Extension for the connection object.

[bt\_df\_conn\_cte\_rx\_enable](direction_8h.md#a92d0b485a83a7395b3613b144b6e749f)

int bt\_df\_conn\_cte\_rx\_enable(struct bt\_conn \*conn, const struct bt\_df\_conn\_cte\_rx\_param \*params)

Enable receive and sampling of Constant Tone Extension for the connection object.

[bt\_df\_conn\_iq\_report\_err](direction_8h.md#a953634e6a88617a8729541d6b5bd0dd6)

bt\_df\_conn\_iq\_report\_err

**Definition** direction.h:159

[BT\_DF\_IQ\_REPORT\_ERR\_NO\_CTE](direction_8h.md#a953634e6a88617a8729541d6b5bd0dd6a53596e4aa9a96006cee3c899150d7a0e)

@ BT\_DF\_IQ\_REPORT\_ERR\_NO\_CTE

Received PDU without CTE.

**Definition** direction.h:163

[BT\_DF\_IQ\_REPORT\_ERR\_PEER\_REJECTED](direction_8h.md#a953634e6a88617a8729541d6b5bd0dd6a7f3f42ede92bafd169620bebddc75512)

@ BT\_DF\_IQ\_REPORT\_ERR\_PEER\_REJECTED

Peer rejected CTE request.

**Definition** direction.h:165

[BT\_DF\_IQ\_REPORT\_ERR\_SUCCESS](direction_8h.md#a953634e6a88617a8729541d6b5bd0dd6acd6f87bd43540cc1b44e5e023a4d0519)

@ BT\_DF\_IQ\_REPORT\_ERR\_SUCCESS

IQ samples report received successfully.

**Definition** direction.h:161

[bt\_df\_set\_conn\_cte\_tx\_param](direction_8h.md#aa0eba41c1a810c9592e0097ee4fe7329)

int bt\_df\_set\_conn\_cte\_tx\_param(struct bt\_conn \*conn, const struct bt\_df\_conn\_cte\_tx\_param \*params)

Set Constant Tone Extension transmission parameters for a connection.

[bt\_df\_adv\_cte\_tx\_enable](direction_8h.md#ab03ec552192056eb8ddb9aae49029265)

int bt\_df\_adv\_cte\_tx\_enable(struct bt\_le\_ext\_adv \*adv)

Enable transmission of Constant Tone Extension for the given advertising set.

[bt\_df\_packet\_status](direction_8h.md#ab9acadbaf03dd976a2ee185574effb4c)

bt\_df\_packet\_status

Possible statuses of PDU that contained reported CTE.

**Definition** direction.h:44

[BT\_DF\_CTE\_CRC\_OK](direction_8h.md#ab9acadbaf03dd976a2ee185574effb4ca10328e978a6641f5f787f4f4e9b50d6c)

@ BT\_DF\_CTE\_CRC\_OK

Received PDU had CRC OK.

**Definition** direction.h:46

[BT\_DF\_CTE\_INSUFFICIENT\_RESOURCES](direction_8h.md#ab9acadbaf03dd976a2ee185574effb4ca70ea13abb5e1626304f8ef4e22564a8b)

@ BT\_DF\_CTE\_INSUFFICIENT\_RESOURCES

There were no sufficient resources to sample CTE.

**Definition** direction.h:57

[BT\_DF\_CTE\_CRC\_ERR\_CTE\_BASED\_OTHER](direction_8h.md#ab9acadbaf03dd976a2ee185574effb4cacdc558d9892228b4403cb782ed2260f9)

@ BT\_DF\_CTE\_CRC\_ERR\_CTE\_BASED\_OTHER

Received PDU had incorrect CRC, but Radio peripheral was able to process sampling of CTE in some othe...

**Definition** direction.h:55

[BT\_DF\_CTE\_CRC\_ERR\_CTE\_BASED\_TIME](direction_8h.md#ab9acadbaf03dd976a2ee185574effb4cadf830cbbe3043423eff237b983bf1c92)

@ BT\_DF\_CTE\_CRC\_ERR\_CTE\_BASED\_TIME

Received PDU had incorrect CRC, but Radio peripheral was able to parse CTEInfo field of the PDU and p...

**Definition** direction.h:51

[bt\_df\_per\_adv\_sync\_cte\_rx\_disable](direction_8h.md#ac2064484bb3c4ea6ae5eb684f3ace008)

int bt\_df\_per\_adv\_sync\_cte\_rx\_disable(struct bt\_le\_per\_adv\_sync \*sync)

Disable receive and sampling of Constant Tone Extension for the given sync set.

[bt\_df\_conn\_cte\_req\_disable](direction_8h.md#ade1a048c3fdf11e979fa9a74f33bc375)

int bt\_df\_conn\_cte\_req\_disable(struct bt\_conn \*conn)

Disable Constant Tone Extension request procedure for a connection.

[bt\_df\_set\_adv\_cte\_tx\_param](direction_8h.md#ae98248377f111deb6aa0565db1d3f690)

int bt\_df\_set\_adv\_cte\_tx\_param(struct bt\_le\_ext\_adv \*adv, const struct bt\_df\_adv\_cte\_tx\_param \*params)

Set or update the Constant Tone Extension parameters for periodic advertising set.

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[bt\_df\_adv\_cte\_tx\_param](structbt__df__adv__cte__tx__param.md)

Constant Tone Extension parameters for connectionless transmission.

**Definition** direction.h:66

[bt\_df\_adv\_cte\_tx\_param::cte\_count](structbt__df__adv__cte__tx__param.md#a288d635221a752b231033803acddd261)

uint8\_t cte\_count

Number of CTE to transmit in each periodic adv interval.

**Definition** direction.h:77

[bt\_df\_adv\_cte\_tx\_param::cte\_len](structbt__df__adv__cte__tx__param.md#a2ab62db4279338e05cd9e5c222c3aab2)

uint8\_t cte\_len

Length of CTE in 8us units.

**Definition** direction.h:68

[bt\_df\_adv\_cte\_tx\_param::cte\_type](structbt__df__adv__cte__tx__param.md#a4af32abbb603d1b7a533771a23d6e9ee)

uint8\_t cte\_type

CTE type.

**Definition** direction.h:75

[bt\_df\_adv\_cte\_tx\_param::ant\_ids](structbt__df__adv__cte__tx__param.md#ac1f251cb2205ce345dc3815b53f13918)

uint8\_t \* ant\_ids

List of antenna IDs in the pattern.

**Definition** direction.h:81

[bt\_df\_adv\_cte\_tx\_param::num\_ant\_ids](structbt__df__adv__cte__tx__param.md#ac974c5bb804912f5940b2ede5f6394a1)

uint8\_t num\_ant\_ids

Number of Antenna IDs in the switch pattern.

**Definition** direction.h:79

[bt\_df\_conn\_cte\_req\_params](structbt__df__conn__cte__req__params.md)

**Definition** direction.h:210

[bt\_df\_conn\_cte\_req\_params::cte\_length](structbt__df__conn__cte__req__params.md#a71340a450e573612a271467c51110166)

uint8\_t cte\_length

Requested length of the CTE in 8 us units.

**Definition** direction.h:219

[bt\_df\_conn\_cte\_req\_params::interval](structbt__df__conn__cte__req__params.md#ab8148905943e0d87a37740ab891b9ef7)

uint16\_t interval

Requested interval for initiating the CTE Request procedure.

**Definition** direction.h:217

[bt\_df\_conn\_cte\_req\_params::cte\_type](structbt__df__conn__cte__req__params.md#ae8232614ec9201e4572675d793b2292a)

uint8\_t cte\_type

Requested type of the CTE.

**Definition** direction.h:226

[bt\_df\_conn\_cte\_rx\_param](structbt__df__conn__cte__rx__param.md)

**Definition** direction.h:144

[bt\_df\_conn\_cte\_rx\_param::cte\_types](structbt__df__conn__cte__rx__param.md#a3401f31865ced48d89c2b4560bcd4512)

uint8\_t cte\_types

Bitfield with allowed CTE types.

**Definition** direction.h:150

[bt\_df\_conn\_cte\_rx\_param::ant\_ids](structbt__df__conn__cte__rx__param.md#a35c2aac4512e2ffce19346c9bf51f033)

const uint8\_t \* ant\_ids

Antenna switch pattern.

**Definition** direction.h:156

[bt\_df\_conn\_cte\_rx\_param::num\_ant\_ids](structbt__df__conn__cte__rx__param.md#aee2ed2d86e2740e166434ede099b1250)

uint8\_t num\_ant\_ids

Length of antenna switch pattern.

**Definition** direction.h:154

[bt\_df\_conn\_cte\_rx\_param::slot\_durations](structbt__df__conn__cte__rx__param.md#afe2dae75b7138b374f991c58f8143c9d)

uint8\_t slot\_durations

Antenna switching slots (bt\_df\_antenna\_switching\_slot).

**Definition** direction.h:152

[bt\_df\_conn\_cte\_tx\_param](structbt__df__conn__cte__tx__param.md)

Constant Tone Extension parameters for CTE transmission in connected mode.

**Definition** direction.h:198

[bt\_df\_conn\_cte\_tx\_param::ant\_ids](structbt__df__conn__cte__tx__param.md#a9df1dac6180e77a4c7abc80890346c4a)

const uint8\_t \* ant\_ids

Antenna switch pattern.

**Definition** direction.h:207

[bt\_df\_conn\_cte\_tx\_param::num\_ant\_ids](structbt__df__conn__cte__tx__param.md#ad49bc64170e8ee4741aa01393284e7de)

uint8\_t num\_ant\_ids

Number of antenna switch pattern.

**Definition** direction.h:205

[bt\_df\_conn\_cte\_tx\_param::cte\_types](structbt__df__conn__cte__tx__param.md#af78df8115d2fac5b8f6132b48a56bc1c)

uint8\_t cte\_types

Bitfield with allowed CTE types (bt\_df\_cte\_type.

**Definition** direction.h:203

[bt\_df\_conn\_iq\_samples\_report](structbt__df__conn__iq__samples__report.md)

**Definition** direction.h:168

[bt\_df\_conn\_iq\_samples\_report::sample\_type](structbt__df__conn__iq__samples__report.md#a1e7901b81c8618e4515cd22a681b4d43)

enum bt\_df\_iq\_sample sample\_type

Type of IQ samples provided in a report.

**Definition** direction.h:188

[bt\_df\_conn\_iq\_samples\_report::cte\_type](structbt__df__conn__iq__samples__report.md#a4d467a7ac76dc9ed6331c10172895097)

uint8\_t cte\_type

Type of CTE (bt\_df\_cte\_type).

**Definition** direction.h:180

[bt\_df\_conn\_iq\_samples\_report::sample16](structbt__df__conn__iq__samples__report.md#a55e1d7d31557f0e1f59ad91834460b78)

struct bt\_hci\_le\_iq\_sample16 const \* sample16

**Definition** direction.h:194

[bt\_df\_conn\_iq\_samples\_report::slot\_durations](structbt__df__conn__iq__samples__report.md#a578132e4a88e739451cf80eba7345094)

uint8\_t slot\_durations

Duration of slots when received CTE type is AoA (bt\_df\_antenna\_switching\_slot).

**Definition** direction.h:182

[bt\_df\_conn\_iq\_samples\_report::sample\_count](structbt__df__conn__iq__samples__report.md#a60500e954e2694a209c2d103887b2685)

uint8\_t sample\_count

Number of IQ samples in report.

**Definition** direction.h:190

[bt\_df\_conn\_iq\_samples\_report::rssi\_ant\_id](structbt__df__conn__iq__samples__report.md#a7c5147b426bb87f9d11c8bdffb91ff02)

uint8\_t rssi\_ant\_id

Id of antenna used to measure the RSSI.

**Definition** direction.h:178

[bt\_df\_conn\_iq\_samples\_report::chan\_idx](structbt__df__conn__iq__samples__report.md#a9374ecd1437f532dec863c527d22348d)

uint8\_t chan\_idx

Channel index used to receive PDU with CTE that was sampled.

**Definition** direction.h:174

[bt\_df\_conn\_iq\_samples\_report::sample](structbt__df__conn__iq__samples__report.md#aa9b177817075e3781256ec2c7d5ac0ce)

struct bt\_hci\_le\_iq\_sample const \* sample

**Definition** direction.h:193

[bt\_df\_conn\_iq\_samples\_report::rssi](structbt__df__conn__iq__samples__report.md#aac825fbdecd6a5a82da0097a8694fb65)

int16\_t rssi

The RSSI of the PDU with CTE (excluding CTE).

**Definition** direction.h:176

[bt\_df\_conn\_iq\_samples\_report::err](structbt__df__conn__iq__samples__report.md#ab6e31e979bba969a18804cf8c9b88f03)

enum bt\_df\_conn\_iq\_report\_err err

Report receive failed reason.

**Definition** direction.h:170

[bt\_df\_conn\_iq\_samples\_report::rx\_phy](structbt__df__conn__iq__samples__report.md#ac14e792a3ce2f3297ddab49e801ba640)

uint8\_t rx\_phy

PHY that was used to receive PDU with CTE that was sampled.

**Definition** direction.h:172

[bt\_df\_conn\_iq\_samples\_report::conn\_evt\_counter](structbt__df__conn__iq__samples__report.md#ac7f3993bd20bd44354f15f098e423c33)

uint16\_t conn\_evt\_counter

Value of connection event counter when the CTE was received and sampled.

**Definition** direction.h:186

[bt\_df\_conn\_iq\_samples\_report::packet\_status](structbt__df__conn__iq__samples__report.md#afdc456a8af5a31ee62c489534af3ecdb)

uint8\_t packet\_status

Status of received PDU with CTE (bt\_df\_packet\_status).

**Definition** direction.h:184

[bt\_df\_per\_adv\_sync\_cte\_rx\_param](structbt__df__per__adv__sync__cte__rx__param.md)

Constant Tone Extension parameters for connectionless reception.

**Definition** direction.h:92

[bt\_df\_per\_adv\_sync\_cte\_rx\_param::cte\_types](structbt__df__per__adv__sync__cte__rx__param.md#a1740d3f41dddd755fc1e04216c8070e5)

uint8\_t cte\_types

Bitfield with allowed CTE types.

**Definition** direction.h:98

[bt\_df\_per\_adv\_sync\_cte\_rx\_param::slot\_durations](structbt__df__per__adv__sync__cte__rx__param.md#abff68c9f2e42e3fe6e8b155f5390f219)

uint8\_t slot\_durations

Antenna switching slots (bt\_df\_antenna\_switching\_slot).

**Definition** direction.h:100

[bt\_df\_per\_adv\_sync\_cte\_rx\_param::max\_cte\_count](structbt__df__per__adv__sync__cte__rx__param.md#ac64232b5e9b2c6acfadfca1c95fd1021)

uint8\_t max\_cte\_count

Max number of CTEs to receive.

**Definition** direction.h:102

[bt\_df\_per\_adv\_sync\_cte\_rx\_param::ant\_ids](structbt__df__per__adv__sync__cte__rx__param.md#ac83de1a86fef076d6c8fc6bccbe49a64)

const uint8\_t \* ant\_ids

Antenna switch pattern.

**Definition** direction.h:106

[bt\_df\_per\_adv\_sync\_cte\_rx\_param::num\_ant\_ids](structbt__df__per__adv__sync__cte__rx__param.md#ae358cbd7b1dd59a7d0a931c8a5fbd94d)

uint8\_t num\_ant\_ids

Length of antenna switch pattern.

**Definition** direction.h:104

[bt\_df\_per\_adv\_sync\_iq\_samples\_report](structbt__df__per__adv__sync__iq__samples__report.md)

**Definition** direction.h:118

[bt\_df\_per\_adv\_sync\_iq\_samples\_report::rssi\_ant\_id](structbt__df__per__adv__sync__iq__samples__report.md#a0b07042bad2a28065b8ea4def73c91d3)

uint8\_t rssi\_ant\_id

Id of antenna used to measure the RSSI.

**Definition** direction.h:124

[bt\_df\_per\_adv\_sync\_iq\_samples\_report::per\_evt\_counter](structbt__df__per__adv__sync__iq__samples__report.md#a1a9c763fa7dd445b5dea8c2bb7b82bc0)

uint16\_t per\_evt\_counter

Value of the paEventCounter of the AUX\_SYNC\_IND PDU.

**Definition** direction.h:132

[bt\_df\_per\_adv\_sync\_iq\_samples\_report::rssi](structbt__df__per__adv__sync__iq__samples__report.md#a48793aad0f603d1763f06453e837a9d9)

int16\_t rssi

The RSSI of the PDU with CTE (excluding CTE).

**Definition** direction.h:122

[bt\_df\_per\_adv\_sync\_iq\_samples\_report::sample\_count](structbt__df__per__adv__sync__iq__samples__report.md#a4d1da7208e043f5ae015612cee16ee25)

uint8\_t sample\_count

Number of IQ samples in report.

**Definition** direction.h:134

[bt\_df\_per\_adv\_sync\_iq\_samples\_report::sample](structbt__df__per__adv__sync__iq__samples__report.md#a64c2936dc8180fc34651b18199241a9b)

struct bt\_hci\_le\_iq\_sample const \* sample

**Definition** direction.h:139

[bt\_df\_per\_adv\_sync\_iq\_samples\_report::packet\_status](structbt__df__per__adv__sync__iq__samples__report.md#a6fea28c1d3b00f1fd7bcb7264f4c3fc9)

uint8\_t packet\_status

Status of received PDU with CTE (bt\_df\_packet\_status).

**Definition** direction.h:130

[bt\_df\_per\_adv\_sync\_iq\_samples\_report::sample\_type](structbt__df__per__adv__sync__iq__samples__report.md#a88d950cdaa4f08a0fa3eb26f1fed7982)

enum bt\_df\_iq\_sample sample\_type

Type of IQ samples provided in a report.

**Definition** direction.h:136

[bt\_df\_per\_adv\_sync\_iq\_samples\_report::cte\_type](structbt__df__per__adv__sync__iq__samples__report.md#aa81e74769290f427b60398eb976b4a2a)

uint8\_t cte\_type

Type of CTE (bt\_df\_cte\_type).

**Definition** direction.h:126

[bt\_df\_per\_adv\_sync\_iq\_samples\_report::slot\_durations](structbt__df__per__adv__sync__iq__samples__report.md#ab256dc21c5d707a9195967caaa13e3e0)

uint8\_t slot\_durations

Duration of slots when received CTE type is AoA (bt\_df\_antenna\_switching\_slot).

**Definition** direction.h:128

[bt\_df\_per\_adv\_sync\_iq\_samples\_report::chan\_idx](structbt__df__per__adv__sync__iq__samples__report.md#ad4d213aa20a0c2fe329606ed789436fd)

uint8\_t chan\_idx

Channel index used to receive PDU with CTE that was sampled.

**Definition** direction.h:120

[bt\_df\_per\_adv\_sync\_iq\_samples\_report::sample16](structbt__df__per__adv__sync__iq__samples__report.md#ae0a28844a5588af05bbde046f6355ddf)

struct bt\_hci\_le\_iq\_sample16 const \* sample16

**Definition** direction.h:140

[bt\_hci\_le\_iq\_sample16](structbt__hci__le__iq__sample16.md)

**Definition** hci\_vs.h:273

[bt\_hci\_le\_iq\_sample](structbt__hci__le__iq__sample.md)

**Definition** hci\_types.h:3320

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [direction.h](direction_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/drivers_2dma_8h_source.html
original_path: doxygen/html/drivers_2dma_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dma.h

[Go to the documentation of this file.](drivers_2dma_8h.md)

1

6

7/\*

8 \* Copyright (c) 2016 Intel Corporation

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12

13#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_H\_

14#define ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_H\_

15

16#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

17#include <[zephyr/device.h](device_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

23

30

[ 34](group__dma__interface.md#gae442d8ba73be7e53b68165647b0ea402)enum [dma\_channel\_direction](group__dma__interface.md#gae442d8ba73be7e53b68165647b0ea402) {

[ 36](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a52f28a5eff23fcddd2a138092d9f7cd5) [MEMORY\_TO\_MEMORY](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a52f28a5eff23fcddd2a138092d9f7cd5) = 0x0,

[ 38](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a4617446ef0e7c2bced585b309011a25a) [MEMORY\_TO\_PERIPHERAL](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a4617446ef0e7c2bced585b309011a25a),

[ 40](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a5fbc19c9e12c11973c0cf0a593ccf165) [PERIPHERAL\_TO\_MEMORY](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a5fbc19c9e12c11973c0cf0a593ccf165),

[ 42](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402ae23cbfefccef9d19dd91f0c746004449) [PERIPHERAL\_TO\_PERIPHERAL](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402ae23cbfefccef9d19dd91f0c746004449),

[ 44](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a7e2b4150c28b057598975e95e8b7494c) [HOST\_TO\_MEMORY](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a7e2b4150c28b057598975e95e8b7494c),

[ 46](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a61e65f3065bf7cdb40efc9039debbb60) [MEMORY\_TO\_HOST](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a61e65f3065bf7cdb40efc9039debbb60),

47

[ 51](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402ae7c3dacfd3496576c41f9c663537419a) [DMA\_CHANNEL\_DIRECTION\_COMMON\_COUNT](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402ae7c3dacfd3496576c41f9c663537419a),

52

[ 57](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a273f9cdcc2af613375cb3e235bfda037) [DMA\_CHANNEL\_DIRECTION\_PRIV\_START](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a273f9cdcc2af613375cb3e235bfda037) = [DMA\_CHANNEL\_DIRECTION\_COMMON\_COUNT](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402ae7c3dacfd3496576c41f9c663537419a),

58

[ 62](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a9114b4138c9dfb506b9428a229c55a02) [DMA\_CHANNEL\_DIRECTION\_MAX](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a9114b4138c9dfb506b9428a229c55a02) = 0x7

63};

64

[ 70](group__dma__interface.md#gafe0877ef4bd7790a4bcd46052088231c)enum [dma\_addr\_adj](group__dma__interface.md#gafe0877ef4bd7790a4bcd46052088231c) {

[ 72](group__dma__interface.md#ggafe0877ef4bd7790a4bcd46052088231cac1fe38db8443f6d8e406c66ba6bdd15e) [DMA\_ADDR\_ADJ\_INCREMENT](group__dma__interface.md#ggafe0877ef4bd7790a4bcd46052088231cac1fe38db8443f6d8e406c66ba6bdd15e),

[ 74](group__dma__interface.md#ggafe0877ef4bd7790a4bcd46052088231caacc38507d8ef3eb8021ae85d9b61b717) [DMA\_ADDR\_ADJ\_DECREMENT](group__dma__interface.md#ggafe0877ef4bd7790a4bcd46052088231caacc38507d8ef3eb8021ae85d9b61b717),

[ 76](group__dma__interface.md#ggafe0877ef4bd7790a4bcd46052088231cafeb870c1a6f9db8238a97f3ac9c6da4f) [DMA\_ADDR\_ADJ\_NO\_CHANGE](group__dma__interface.md#ggafe0877ef4bd7790a4bcd46052088231cafeb870c1a6f9db8238a97f3ac9c6da4f),

77};

78

[ 82](group__dma__interface.md#gade594552920aabbfd2106059a338498b)enum [dma\_channel\_filter](group__dma__interface.md#gade594552920aabbfd2106059a338498b) {

[ 83](group__dma__interface.md#ggade594552920aabbfd2106059a338498ba54326b41a55d7a64c808cea83520b94f) [DMA\_CHANNEL\_NORMAL](group__dma__interface.md#ggade594552920aabbfd2106059a338498ba54326b41a55d7a64c808cea83520b94f), /\* normal DMA channel \*/

[ 84](group__dma__interface.md#ggade594552920aabbfd2106059a338498bacffe4591bb7577cd8596d4dc1b51838c) [DMA\_CHANNEL\_PERIODIC](group__dma__interface.md#ggade594552920aabbfd2106059a338498bacffe4591bb7577cd8596d4dc1b51838c), /\* can be triggered by periodic sources \*/

85};

86

[ 90](group__dma__interface.md#ga08c366c8d47672eeeb37b258af20101b)enum [dma\_attribute\_type](group__dma__interface.md#ga08c366c8d47672eeeb37b258af20101b) {

[ 91](group__dma__interface.md#gga08c366c8d47672eeeb37b258af20101ba486ede0649882311fd344a52983d5f3f) [DMA\_ATTR\_BUFFER\_ADDRESS\_ALIGNMENT](group__dma__interface.md#gga08c366c8d47672eeeb37b258af20101ba486ede0649882311fd344a52983d5f3f),

[ 92](group__dma__interface.md#gga08c366c8d47672eeeb37b258af20101baa6b28cfc17b80884dddc18fcaa2b6873) [DMA\_ATTR\_BUFFER\_SIZE\_ALIGNMENT](group__dma__interface.md#gga08c366c8d47672eeeb37b258af20101baa6b28cfc17b80884dddc18fcaa2b6873),

[ 93](group__dma__interface.md#gga08c366c8d47672eeeb37b258af20101baa07cc26d400fa919df133552eb2e317b) [DMA\_ATTR\_COPY\_ALIGNMENT](group__dma__interface.md#gga08c366c8d47672eeeb37b258af20101baa07cc26d400fa919df133552eb2e317b),

[ 94](group__dma__interface.md#gga08c366c8d47672eeeb37b258af20101bafcaffeb0a1c7be27d258d73968196d18) [DMA\_ATTR\_MAX\_BLOCK\_COUNT](group__dma__interface.md#gga08c366c8d47672eeeb37b258af20101bafcaffeb0a1c7be27d258d73968196d18),

95};

96

[ 104](structdma__block__config.md)struct [dma\_block\_config](structdma__block__config.md) {

105#ifdef CONFIG\_DMA\_64BIT

107 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [source\_address](structdma__block__config.md#a9fbd1deae8936a806ecc79bad3f3b9bb);

109 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [dest\_address](structdma__block__config.md#a9a66e0a647c55e94423ababf44c04325);

110#else

[ 112](structdma__block__config.md#a9fbd1deae8936a806ecc79bad3f3b9bb) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [source\_address](structdma__block__config.md#a9fbd1deae8936a806ecc79bad3f3b9bb);

[ 114](structdma__block__config.md#a9a66e0a647c55e94423ababf44c04325) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dest\_address](structdma__block__config.md#a9a66e0a647c55e94423ababf44c04325);

115#endif

[ 117](structdma__block__config.md#a3180ef98f007ad9be7f6ff363dc125c3) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [source\_gather\_interval](structdma__block__config.md#a3180ef98f007ad9be7f6ff363dc125c3);

[ 119](structdma__block__config.md#a18bafb80538bca9c12197955770b6511) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dest\_scatter\_interval](structdma__block__config.md#a18bafb80538bca9c12197955770b6511);

[ 121](structdma__block__config.md#ae38027f6262c34d9f1abe4f923d904b4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dest\_scatter\_count](structdma__block__config.md#ae38027f6262c34d9f1abe4f923d904b4);

[ 123](structdma__block__config.md#a8ffcde07d02317b3cc1b327bd0b88395) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [source\_gather\_count](structdma__block__config.md#a8ffcde07d02317b3cc1b327bd0b88395);

[ 125](structdma__block__config.md#a3fdab19df16d5e96054aabffbf27fcc1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [block\_size](structdma__block__config.md#a3fdab19df16d5e96054aabffbf27fcc1);

[ 127](structdma__block__config.md#a937168582c7473fe1b2b696cd1433605) struct [dma\_block\_config](structdma__block__config.md) \*[next\_block](structdma__block__config.md#a937168582c7473fe1b2b696cd1433605);

[ 129](structdma__block__config.md#abbac399f6c6e18ad2ed25359ebb799ef) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [source\_gather\_en](structdma__block__config.md#abbac399f6c6e18ad2ed25359ebb799ef) : 1;

[ 131](structdma__block__config.md#a778935d5b806002b902b72304b845ea0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dest\_scatter\_en](structdma__block__config.md#a778935d5b806002b902b72304b845ea0) : 1;

[ 139](structdma__block__config.md#a9110f948520186aa5718f57b4bbbd24a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [source\_addr\_adj](structdma__block__config.md#a9110f948520186aa5718f57b4bbbd24a) : 2;

[ 147](structdma__block__config.md#ad69502226d2c60adbdb9fe5e93dc0a05) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dest\_addr\_adj](structdma__block__config.md#ad69502226d2c60adbdb9fe5e93dc0a05) : 2;

[ 149](structdma__block__config.md#a4f8f5b65002f65eaacdd3dde26c47170) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [source\_reload\_en](structdma__block__config.md#a4f8f5b65002f65eaacdd3dde26c47170) : 1;

[ 151](structdma__block__config.md#a7dedf429f44f3af6fcc0db125d6494c8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dest\_reload\_en](structdma__block__config.md#a7dedf429f44f3af6fcc0db125d6494c8) : 1;

[ 153](structdma__block__config.md#a877a30b62fd8e0e1773890a10c8a2751) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [fifo\_mode\_control](structdma__block__config.md#a877a30b62fd8e0e1773890a10c8a2751) : 4;

[ 160](structdma__block__config.md#aecf6805b898a70922c58d15127bafc92) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flow\_control\_mode](structdma__block__config.md#aecf6805b898a70922c58d15127bafc92) : 1;

161

162 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \_reserved : 3;

163};

164

[ 166](group__dma__interface.md#gad4fc9a9c59f4e07c81a4c2f3b57c9ccb)#define DMA\_STATUS\_COMPLETE 0

[ 168](group__dma__interface.md#gab74c89289c8429071522cb89ac066eea)#define DMA\_STATUS\_BLOCK 1

169

[ 188](group__dma__interface.md#ga94745b4472ee1addd4f82db4e59e9fb5)typedef void (\*[dma\_callback\_t](group__dma__interface.md#ga94745b4472ee1addd4f82db4e59e9fb5))(const struct [device](structdevice.md) \*dev, void \*user\_data,

189 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, int status);

190

[ 195](structdma__config.md)struct [dma\_config](structdma__config.md) {

[ 197](structdma__config.md#a8e6c5cab5ec030066a3e57e0507fbf9f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dma\_slot](structdma__config.md#a8e6c5cab5ec030066a3e57e0507fbf9f) : 8;

[ 209](structdma__config.md#aaf903b1badff8b0fc4ef18a34c2773d7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [channel\_direction](structdma__config.md#aaf903b1badff8b0fc4ef18a34c2773d7) : 3;

[ 216](structdma__config.md#a39526177f03017d245651b4f51820161) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [complete\_callback\_en](structdma__config.md#a39526177f03017d245651b4f51820161) : 1;

[ 223](structdma__config.md#a66d7fe742d6e1c1f2e58a49105892961) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [error\_callback\_en](structdma__config.md#a66d7fe742d6e1c1f2e58a49105892961) : 1;

[ 230](structdma__config.md#a2927e31730c6ca2f5ac8db38c255d9f7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [source\_handshake](structdma__config.md#a2927e31730c6ca2f5ac8db38c255d9f7) : 1;

[ 237](structdma__config.md#af570b4050200ec510df323bd31558233) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dest\_handshake](structdma__config.md#af570b4050200ec510df323bd31558233) : 1;

[ 241](structdma__config.md#a284d96c59945aaa851d235802aee979a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [channel\_priority](structdma__config.md#a284d96c59945aaa851d235802aee979a) : 4;

[ 243](structdma__config.md#a7c77afc1f546efda6ce22f50560b8840) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [source\_chaining\_en](structdma__config.md#a7c77afc1f546efda6ce22f50560b8840) : 1;

[ 245](structdma__config.md#a8a304fdada9ec7fc87402449e1410486) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dest\_chaining\_en](structdma__config.md#a8a304fdada9ec7fc87402449e1410486) : 1;

[ 247](structdma__config.md#ace2dc918fcfea264a579b1084fcb7fe5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [linked\_channel](structdma__config.md#ace2dc918fcfea264a579b1084fcb7fe5) : 7;

[ 249](structdma__config.md#afa70dbf1ee7bb5fb6a771f634783b7a2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cyclic](structdma__config.md#afa70dbf1ee7bb5fb6a771f634783b7a2) : 1;

250

251 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \_reserved : 3;

[ 253](structdma__config.md#ac9144783b4843182451b440d97ecd273) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [source\_data\_size](structdma__config.md#ac9144783b4843182451b440d97ecd273) : 16;

[ 255](structdma__config.md#adfa9efbfbef3ed41b2f8dd5b9c441e08) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dest\_data\_size](structdma__config.md#adfa9efbfbef3ed41b2f8dd5b9c441e08) : 16;

[ 257](structdma__config.md#ad750b724bab1503ded7c163d8228aa80) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [source\_burst\_length](structdma__config.md#ad750b724bab1503ded7c163d8228aa80) : 16;

[ 259](structdma__config.md#aca47b00f817e55bf662fdd6767a59ed0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dest\_burst\_length](structdma__config.md#aca47b00f817e55bf662fdd6767a59ed0) : 16;

[ 261](structdma__config.md#adb776a4940c71b61cab60eb05159b2d4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [block\_count](structdma__config.md#adb776a4940c71b61cab60eb05159b2d4);

[ 263](structdma__config.md#aca6a1cb9b580a61bf91490fecf10cb16) struct [dma\_block\_config](structdma__block__config.md) \*[head\_block](structdma__config.md#aca6a1cb9b580a61bf91490fecf10cb16);

[ 265](structdma__config.md#a510eed1cadbf411c9e94e1d1fb43d39d) void \*[user\_data](structdma__config.md#a510eed1cadbf411c9e94e1d1fb43d39d);

[ 267](structdma__config.md#a69110abc43227bd7df217c4e25bb964b) [dma\_callback\_t](group__dma__interface.md#ga94745b4472ee1addd4f82db4e59e9fb5) [dma\_callback](structdma__config.md#a69110abc43227bd7df217c4e25bb964b);

268};

269

[ 273](structdma__status.md)struct [dma\_status](structdma__status.md) {

[ 275](structdma__status.md#a92ec05d9207caa828064661897f2f31c) bool [busy](structdma__status.md#a92ec05d9207caa828064661897f2f31c);

[ 277](structdma__status.md#aacfe94ad8e60ea77bca2423bd9bf8409) enum [dma\_channel\_direction](group__dma__interface.md#gae442d8ba73be7e53b68165647b0ea402) [dir](structdma__status.md#aacfe94ad8e60ea77bca2423bd9bf8409);

[ 279](structdma__status.md#a3a33f92b1d100f988fca2bea0a6deb24) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pending\_length](structdma__status.md#a3a33f92b1d100f988fca2bea0a6deb24);

[ 281](structdma__status.md#a2b481bf13de03e49146eb6a26563776e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [free](structdma__status.md#a2b481bf13de03e49146eb6a26563776e);

[ 283](structdma__status.md#aa7288b85f41098e59ad4f96dcea4ccde) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [write\_position](structdma__status.md#aa7288b85f41098e59ad4f96dcea4ccde);

[ 285](structdma__status.md#afa401acfb26cd26b73e4a52066989847) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [read\_position](structdma__status.md#afa401acfb26cd26b73e4a52066989847);

[ 287](structdma__status.md#a9f743c98e6343d55eccc27e528b79b1a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [total\_copied](structdma__status.md#a9f743c98e6343d55eccc27e528b79b1a);

288};

289

[ 295](structdma__context.md)struct [dma\_context](structdma__context.md) {

[ 297](structdma__context.md#a25355c8cc60df536c9a37cdef52aa653) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [magic](structdma__context.md#a25355c8cc60df536c9a37cdef52aa653);

[ 299](structdma__context.md#ac6685cf14ca69c7b77160e5031c0a800) int [dma\_channels](structdma__context.md#ac6685cf14ca69c7b77160e5031c0a800);

[ 301](structdma__context.md#a5b5776088155c9f19488d479924bec8e) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*[atomic](structdma__context.md#a5b5776088155c9f19488d479924bec8e);

302};

303

[ 305](group__dma__interface.md#gae28ba5114dc2e9ecb89ccf9b623e938f)#define DMA\_MAGIC 0x47494749

306

313typedef int (\*dma\_api\_config)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

314 struct [dma\_config](structdma__config.md) \*config);

315

316#ifdef CONFIG\_DMA\_64BIT

317typedef int (\*dma\_api\_reload)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

318 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) src, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) dst, size\_t size);

319#else

320typedef int (\*dma\_api\_reload)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

321 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) src, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dst, size\_t size);

322#endif

323

324typedef int (\*dma\_api\_start)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel);

325

326typedef int (\*dma\_api\_stop)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel);

327

328typedef int (\*dma\_api\_suspend)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel);

329

330typedef int (\*dma\_api\_resume)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel);

331

332typedef int (\*dma\_api\_get\_status)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

333 struct [dma\_status](structdma__status.md) \*status);

334

335typedef int (\*dma\_api\_get\_attribute)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) type, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*value);

336

350typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*dma\_api\_chan\_filter)(const struct [device](structdevice.md) \*dev,

351 int channel, void \*filter\_param);

352

353\_\_subsystem struct dma\_driver\_api {

354 dma\_api\_config config;

355 dma\_api\_reload reload;

356 dma\_api\_start start;

357 dma\_api\_stop stop;

358 dma\_api\_suspend suspend;

359 dma\_api\_resume resume;

360 dma\_api\_get\_status get\_status;

361 dma\_api\_get\_attribute get\_attribute;

362 dma\_api\_chan\_filter chan\_filter;

363};

367

[ 379](group__dma__interface.md#ga6df1a6b89f271a0eae01c17b748bd2df)static inline int [dma\_config](group__dma__interface.md#ga6df1a6b89f271a0eae01c17b748bd2df)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

380 struct [dma\_config](structdma__config.md) \*config)

381{

382 const struct dma\_driver\_api \*api =

383 (const struct dma\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

384

385 return api->config(dev, channel, config);

386}

387

401#ifdef CONFIG\_DMA\_64BIT

402static inline int [dma\_reload](group__dma__interface.md#ga55bd5d550349c11c63ef47c2ed861f36)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

403 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) src, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) dst, size\_t size)

404#else

[ 405](group__dma__interface.md#ga55bd5d550349c11c63ef47c2ed861f36)static inline int [dma\_reload](group__dma__interface.md#ga55bd5d550349c11c63ef47c2ed861f36)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

406 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) src, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dst, size\_t size)

407#endif

408{

409 const struct dma\_driver\_api \*api =

410 (const struct dma\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

411

412 if (api->reload) {

413 return api->reload(dev, channel, src, dst, size);

414 }

415

416 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

417}

418

[ 438](group__dma__interface.md#gac2ddafd17680f59e4e8fe5f6e2eaba48)\_\_syscall int [dma\_start](group__dma__interface.md#gac2ddafd17680f59e4e8fe5f6e2eaba48)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel);

439

440static inline int z\_impl\_dma\_start(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel)

441{

442 const struct dma\_driver\_api \*api =

443 (const struct dma\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

444

445 return api->start(dev, channel);

446}

447

[ 466](group__dma__interface.md#ga305cc72d0804028b77aa82dd07c926ad)\_\_syscall int [dma\_stop](group__dma__interface.md#ga305cc72d0804028b77aa82dd07c926ad)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel);

467

468static inline int z\_impl\_dma\_stop(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel)

469{

470 const struct dma\_driver\_api \*api =

471 (const struct dma\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

472

473 return api->stop(dev, channel);

474}

475

476

[ 493](group__dma__interface.md#ga6779850f6082259f5bef29b1282effdb)\_\_syscall int [dma\_suspend](group__dma__interface.md#ga6779850f6082259f5bef29b1282effdb)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel);

494

495static inline int z\_impl\_dma\_suspend(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel)

496{

497 const struct dma\_driver\_api \*api = (const struct dma\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

498

499 if (api->suspend == NULL) {

500 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

501 }

502 return api->suspend(dev, channel);

503}

504

[ 521](group__dma__interface.md#ga89a3d056803d7f2dd1c8b6e535ef4f1d)\_\_syscall int [dma\_resume](group__dma__interface.md#ga89a3d056803d7f2dd1c8b6e535ef4f1d)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel);

522

523static inline int z\_impl\_dma\_resume(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel)

524{

525 const struct dma\_driver\_api \*api = (const struct dma\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

526

527 if (api->resume == NULL) {

528 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

529 }

530 return api->resume(dev, channel);

531}

532

[ 547](group__dma__interface.md#ga91cc55f781744069f1f9f29249bdee8d)\_\_syscall int [dma\_request\_channel](group__dma__interface.md#ga91cc55f781744069f1f9f29249bdee8d)(const struct [device](structdevice.md) \*dev,

548 void \*filter\_param);

549

550static inline int z\_impl\_dma\_request\_channel(const struct [device](structdevice.md) \*dev,

551 void \*filter\_param)

552{

553 int i = 0;

554 int channel = -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

555 const struct dma\_driver\_api \*api =

556 (const struct dma\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

557 /\* dma\_context shall be the first one in dev data \*/

558 struct [dma\_context](structdma__context.md) \*dma\_ctx = (struct [dma\_context](structdma__context.md) \*)dev->[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

559

560 if (dma\_ctx->magic != [DMA\_MAGIC](group__dma__interface.md#gae28ba5114dc2e9ecb89ccf9b623e938f)) {

561 return channel;

562 }

563

564 for (i = 0; i < dma\_ctx->dma\_channels; i++) {

565 if (![atomic\_test\_and\_set\_bit](group__atomic__apis.md#ga7ff45e13aa5f8be5d7a550e49f5c720b)(dma\_ctx->atomic, i)) {

566 if (api->chan\_filter &&

567 !api->chan\_filter(dev, i, filter\_param)) {

568 [atomic\_clear\_bit](group__atomic__apis.md#ga1c1693d524c49d11fd32b323a39d718e)(dma\_ctx->atomic, i);

569 continue;

570 }

571 channel = i;

572 break;

573 }

574 }

575

576 return channel;

577}

578

[ 590](group__dma__interface.md#gab02df5277d79a04a65132365e7b5d3de)\_\_syscall void [dma\_release\_channel](group__dma__interface.md#gab02df5277d79a04a65132365e7b5d3de)(const struct [device](structdevice.md) \*dev,

591 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel);

592

593static inline void z\_impl\_dma\_release\_channel(const struct [device](structdevice.md) \*dev,

594 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel)

595{

596 struct [dma\_context](structdma__context.md) \*dma\_ctx = (struct [dma\_context](structdma__context.md) \*)dev->[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

597

598 if (dma\_ctx->magic != [DMA\_MAGIC](group__dma__interface.md#gae28ba5114dc2e9ecb89ccf9b623e938f)) {

599 return;

600 }

601

602 if ((int)channel < dma\_ctx->[dma\_channels](structdma__context.md#ac6685cf14ca69c7b77160e5031c0a800)) {

603 [atomic\_clear\_bit](group__atomic__apis.md#ga1c1693d524c49d11fd32b323a39d718e)(dma\_ctx->atomic, channel);

604 }

605

606}

607

[ 620](group__dma__interface.md#ga729d8f1163458d447d0a4b20cb9e4659)\_\_syscall int [dma\_chan\_filter](group__dma__interface.md#ga729d8f1163458d447d0a4b20cb9e4659)(const struct [device](structdevice.md) \*dev,

621 int channel, void \*filter\_param);

622

623static inline int z\_impl\_dma\_chan\_filter(const struct [device](structdevice.md) \*dev,

624 int channel, void \*filter\_param)

625{

626 const struct dma\_driver\_api \*api =

627 (const struct dma\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

628

629 if (api->chan\_filter) {

630 return api->chan\_filter(dev, channel, filter\_param);

631 }

632

633 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

634}

635

[ 652](group__dma__interface.md#ga2cae500f1f9ed42ad338a40ec8655544)static inline int [dma\_get\_status](group__dma__interface.md#ga2cae500f1f9ed42ad338a40ec8655544)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

653 struct [dma\_status](structdma__status.md) \*[stat](structstat.md))

654{

655 const struct dma\_driver\_api \*api =

656 (const struct dma\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

657

658 if (api->get\_status) {

659 return api->get\_status(dev, channel, [stat](structstat.md));

660 }

661

662 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

663}

664

[ 682](group__dma__interface.md#ga641f3fa492bfb17cf9f0a0361d429257)static inline int [dma\_get\_attribute](group__dma__interface.md#ga641f3fa492bfb17cf9f0a0361d429257)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) type, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*value)

683{

684 const struct dma\_driver\_api \*api = (const struct dma\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

685

686 if (api->get\_attribute) {

687 return api->get\_attribute(dev, type, value);

688 }

689

690 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

691}

692

[ 706](group__dma__interface.md#gadd1724a843bba4ccc1c65c9fb9d3d921)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dma\_width\_index](group__dma__interface.md#gadd1724a843bba4ccc1c65c9fb9d3d921)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size)

707{

708 /\* Check boundaries (max supported width is 32 Bytes) \*/

709 if (size < 1 || size > 32) {

710 return 0; /\* Zero is the default (8 Bytes) \*/

711 }

712

713 /\* Ensure size is a power of 2 \*/

714 if (![is\_power\_of\_two](group__sys-util.md#gadfe7046eb6c39bb3c84c18d8ac7a230e)(size)) {

715 return 0; /\* Zero is the default (8 Bytes) \*/

716 }

717

718 /\* Convert to bit pattern for writing to a register \*/

719 return [find\_msb\_set](ffs_8h.md#a088db7d02e8f1fc559cbe1ec048494e8)(size);

720}

721

[ 735](group__dma__interface.md#gaac27f2ee664671884087ee3d2a2863ce)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dma\_burst\_index](group__dma__interface.md#gaac27f2ee664671884087ee3d2a2863ce)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) burst)

736{

737 /\* Check boundaries (max supported burst length is 256) \*/

738 if (burst < 1 || burst > 256) {

739 return 0; /\* Zero is the default (1 burst length) \*/

740 }

741

742 /\* Ensure burst is a power of 2 \*/

743 if (!(burst & (burst - 1))) {

744 return 0; /\* Zero is the default (1 burst length) \*/

745 }

746

747 /\* Convert to bit pattern for writing to a register \*/

748 return [find\_msb\_set](ffs_8h.md#a088db7d02e8f1fc559cbe1ec048494e8)(burst);

749}

750

[ 760](group__dma__interface.md#ga542e1a0fa0d851a51e4c8abf9a820e0c)#define DMA\_BUF\_ADDR\_ALIGNMENT(node) DT\_PROP(node, dma\_buf\_addr\_alignment)

761

[ 771](group__dma__interface.md#ga76dfdfecc732319908f381883c630a2b)#define DMA\_BUF\_SIZE\_ALIGNMENT(node) DT\_PROP(node, dma\_buf\_size\_alignment)

772

[ 779](group__dma__interface.md#ga083e8b0a863b0833c55158053d286f15)#define DMA\_COPY\_ALIGNMENT(node) DT\_PROP(node, dma\_copy\_alignment)

780

784

785#ifdef \_\_cplusplus

786}

787#endif

788

789#include <syscalls/dma.h>

790

791#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_H\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[device.h](device_8h.md)

[find\_msb\_set](ffs_8h.md#a088db7d02e8f1fc559cbe1ec048494e8)

static ALWAYS\_INLINE unsigned int find\_msb\_set(uint32\_t op)

find most significant bit set in a 32-bit word

**Definition** ffs.h:31

[atomic\_clear\_bit](group__atomic__apis.md#ga1c1693d524c49d11fd32b323a39d718e)

static void atomic\_clear\_bit(atomic\_t \*target, int bit)

Atomically clear a bit.

**Definition** atomic.h:191

[atomic\_test\_and\_set\_bit](group__atomic__apis.md#ga7ff45e13aa5f8be5d7a550e49f5c720b)

static bool atomic\_test\_and\_set\_bit(atomic\_t \*target, int bit)

Atomically set a bit.

**Definition** atomic.h:170

[dma\_attribute\_type](group__dma__interface.md#ga08c366c8d47672eeeb37b258af20101b)

dma\_attribute\_type

DMA attributes.

**Definition** dma.h:90

[dma\_get\_status](group__dma__interface.md#ga2cae500f1f9ed42ad338a40ec8655544)

static int dma\_get\_status(const struct device \*dev, uint32\_t channel, struct dma\_status \*stat)

get current runtime status of DMA transfer

**Definition** dma.h:652

[dma\_stop](group__dma__interface.md#ga305cc72d0804028b77aa82dd07c926ad)

int dma\_stop(const struct device \*dev, uint32\_t channel)

Stops the DMA transfer and disables the channel.

[dma\_reload](group__dma__interface.md#ga55bd5d550349c11c63ef47c2ed861f36)

static int dma\_reload(const struct device \*dev, uint32\_t channel, uint32\_t src, uint32\_t dst, size\_t size)

Reload buffer(s) for a DMA channel.

**Definition** dma.h:405

[dma\_get\_attribute](group__dma__interface.md#ga641f3fa492bfb17cf9f0a0361d429257)

static int dma\_get\_attribute(const struct device \*dev, uint32\_t type, uint32\_t \*value)

get attribute of a dma controller

**Definition** dma.h:682

[dma\_suspend](group__dma__interface.md#ga6779850f6082259f5bef29b1282effdb)

int dma\_suspend(const struct device \*dev, uint32\_t channel)

Suspend a DMA channel transfer.

[dma\_config](group__dma__interface.md#ga6df1a6b89f271a0eae01c17b748bd2df)

static int dma\_config(const struct device \*dev, uint32\_t channel, struct dma\_config \*config)

Configure individual channel for DMA transfer.

**Definition** dma.h:379

[dma\_chan\_filter](group__dma__interface.md#ga729d8f1163458d447d0a4b20cb9e4659)

int dma\_chan\_filter(const struct device \*dev, int channel, void \*filter\_param)

DMA channel filter.

[dma\_resume](group__dma__interface.md#ga89a3d056803d7f2dd1c8b6e535ef4f1d)

int dma\_resume(const struct device \*dev, uint32\_t channel)

Resume a DMA channel transfer.

[dma\_request\_channel](group__dma__interface.md#ga91cc55f781744069f1f9f29249bdee8d)

int dma\_request\_channel(const struct device \*dev, void \*filter\_param)

request DMA channel.

[dma\_callback\_t](group__dma__interface.md#ga94745b4472ee1addd4f82db4e59e9fb5)

void(\* dma\_callback\_t)(const struct device \*dev, void \*user\_data, uint32\_t channel, int status)

Callback function for DMA transfer completion.

**Definition** dma.h:188

[dma\_burst\_index](group__dma__interface.md#gaac27f2ee664671884087ee3d2a2863ce)

static uint32\_t dma\_burst\_index(uint32\_t burst)

Look-up generic burst index to be used in registers.

**Definition** dma.h:735

[dma\_release\_channel](group__dma__interface.md#gab02df5277d79a04a65132365e7b5d3de)

void dma\_release\_channel(const struct device \*dev, uint32\_t channel)

release DMA channel.

[dma\_start](group__dma__interface.md#gac2ddafd17680f59e4e8fe5f6e2eaba48)

int dma\_start(const struct device \*dev, uint32\_t channel)

Enables DMA channel and starts the transfer, the channel must be configured beforehand.

[dma\_width\_index](group__dma__interface.md#gadd1724a843bba4ccc1c65c9fb9d3d921)

static uint32\_t dma\_width\_index(uint32\_t size)

Look-up generic width index to be used in registers.

**Definition** dma.h:706

[dma\_channel\_filter](group__dma__interface.md#gade594552920aabbfd2106059a338498b)

dma\_channel\_filter

DMA channel attributes.

**Definition** dma.h:82

[DMA\_MAGIC](group__dma__interface.md#gae28ba5114dc2e9ecb89ccf9b623e938f)

#define DMA\_MAGIC

Magic code to identify context content.

**Definition** dma.h:305

[dma\_channel\_direction](group__dma__interface.md#gae442d8ba73be7e53b68165647b0ea402)

dma\_channel\_direction

DMA channel direction.

**Definition** dma.h:34

[dma\_addr\_adj](group__dma__interface.md#gafe0877ef4bd7790a4bcd46052088231c)

dma\_addr\_adj

DMA address adjustment.

**Definition** dma.h:70

[DMA\_ATTR\_BUFFER\_ADDRESS\_ALIGNMENT](group__dma__interface.md#gga08c366c8d47672eeeb37b258af20101ba486ede0649882311fd344a52983d5f3f)

@ DMA\_ATTR\_BUFFER\_ADDRESS\_ALIGNMENT

**Definition** dma.h:91

[DMA\_ATTR\_COPY\_ALIGNMENT](group__dma__interface.md#gga08c366c8d47672eeeb37b258af20101baa07cc26d400fa919df133552eb2e317b)

@ DMA\_ATTR\_COPY\_ALIGNMENT

**Definition** dma.h:93

[DMA\_ATTR\_BUFFER\_SIZE\_ALIGNMENT](group__dma__interface.md#gga08c366c8d47672eeeb37b258af20101baa6b28cfc17b80884dddc18fcaa2b6873)

@ DMA\_ATTR\_BUFFER\_SIZE\_ALIGNMENT

**Definition** dma.h:92

[DMA\_ATTR\_MAX\_BLOCK\_COUNT](group__dma__interface.md#gga08c366c8d47672eeeb37b258af20101bafcaffeb0a1c7be27d258d73968196d18)

@ DMA\_ATTR\_MAX\_BLOCK\_COUNT

**Definition** dma.h:94

[DMA\_CHANNEL\_NORMAL](group__dma__interface.md#ggade594552920aabbfd2106059a338498ba54326b41a55d7a64c808cea83520b94f)

@ DMA\_CHANNEL\_NORMAL

**Definition** dma.h:83

[DMA\_CHANNEL\_PERIODIC](group__dma__interface.md#ggade594552920aabbfd2106059a338498bacffe4591bb7577cd8596d4dc1b51838c)

@ DMA\_CHANNEL\_PERIODIC

**Definition** dma.h:84

[DMA\_CHANNEL\_DIRECTION\_PRIV\_START](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a273f9cdcc2af613375cb3e235bfda037)

@ DMA\_CHANNEL\_DIRECTION\_PRIV\_START

This and higher values are dma controller or soc specific.

**Definition** dma.h:57

[MEMORY\_TO\_PERIPHERAL](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a4617446ef0e7c2bced585b309011a25a)

@ MEMORY\_TO\_PERIPHERAL

Memory to peripheral.

**Definition** dma.h:38

[MEMORY\_TO\_MEMORY](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a52f28a5eff23fcddd2a138092d9f7cd5)

@ MEMORY\_TO\_MEMORY

Memory to memory.

**Definition** dma.h:36

[PERIPHERAL\_TO\_MEMORY](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a5fbc19c9e12c11973c0cf0a593ccf165)

@ PERIPHERAL\_TO\_MEMORY

Peripheral to memory.

**Definition** dma.h:40

[MEMORY\_TO\_HOST](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a61e65f3065bf7cdb40efc9039debbb60)

@ MEMORY\_TO\_HOST

Memory to host.

**Definition** dma.h:46

[HOST\_TO\_MEMORY](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a7e2b4150c28b057598975e95e8b7494c)

@ HOST\_TO\_MEMORY

Host to memory.

**Definition** dma.h:44

[DMA\_CHANNEL\_DIRECTION\_MAX](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a9114b4138c9dfb506b9428a229c55a02)

@ DMA\_CHANNEL\_DIRECTION\_MAX

Maximum allowed value (3 bit field!).

**Definition** dma.h:62

[PERIPHERAL\_TO\_PERIPHERAL](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402ae23cbfefccef9d19dd91f0c746004449)

@ PERIPHERAL\_TO\_PERIPHERAL

Peripheral to peripheral.

**Definition** dma.h:42

[DMA\_CHANNEL\_DIRECTION\_COMMON\_COUNT](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402ae7c3dacfd3496576c41f9c663537419a)

@ DMA\_CHANNEL\_DIRECTION\_COMMON\_COUNT

Number of all common channel directions.

**Definition** dma.h:51

[DMA\_ADDR\_ADJ\_DECREMENT](group__dma__interface.md#ggafe0877ef4bd7790a4bcd46052088231caacc38507d8ef3eb8021ae85d9b61b717)

@ DMA\_ADDR\_ADJ\_DECREMENT

Decrement the address.

**Definition** dma.h:74

[DMA\_ADDR\_ADJ\_INCREMENT](group__dma__interface.md#ggafe0877ef4bd7790a4bcd46052088231cac1fe38db8443f6d8e406c66ba6bdd15e)

@ DMA\_ADDR\_ADJ\_INCREMENT

Increment the address.

**Definition** dma.h:72

[DMA\_ADDR\_ADJ\_NO\_CHANGE](group__dma__interface.md#ggafe0877ef4bd7790a4bcd46052088231cafeb870c1a6f9db8238a97f3ac9c6da4f)

@ DMA\_ADDR\_ADJ\_NO\_CHANGE

No change the address.

**Definition** dma.h:76

[is\_power\_of\_two](group__sys-util.md#gadfe7046eb6c39bb3c84c18d8ac7a230e)

static bool is\_power\_of\_two(unsigned int x)

Is x a power of two?

**Definition** util.h:411

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:61

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:83

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:397

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[dma\_block\_config](structdma__block__config.md)

DMA block configuration structure.

**Definition** dma.h:104

[dma\_block\_config::dest\_scatter\_interval](structdma__block__config.md#a18bafb80538bca9c12197955770b6511)

uint32\_t dest\_scatter\_interval

Address adjustment at scatter boundary.

**Definition** dma.h:119

[dma\_block\_config::source\_gather\_interval](structdma__block__config.md#a3180ef98f007ad9be7f6ff363dc125c3)

uint32\_t source\_gather\_interval

Address adjustment at gather boundary.

**Definition** dma.h:117

[dma\_block\_config::block\_size](structdma__block__config.md#a3fdab19df16d5e96054aabffbf27fcc1)

uint32\_t block\_size

Number of bytes to be transferred for this block.

**Definition** dma.h:125

[dma\_block\_config::source\_reload\_en](structdma__block__config.md#a4f8f5b65002f65eaacdd3dde26c47170)

uint16\_t source\_reload\_en

Reload source address at the end of block transfer.

**Definition** dma.h:149

[dma\_block\_config::dest\_scatter\_en](structdma__block__config.md#a778935d5b806002b902b72304b845ea0)

uint16\_t dest\_scatter\_en

Enable destination scattering when set to 1.

**Definition** dma.h:131

[dma\_block\_config::dest\_reload\_en](structdma__block__config.md#a7dedf429f44f3af6fcc0db125d6494c8)

uint16\_t dest\_reload\_en

Reload destination address at the end of block transfer.

**Definition** dma.h:151

[dma\_block\_config::fifo\_mode\_control](structdma__block__config.md#a877a30b62fd8e0e1773890a10c8a2751)

uint16\_t fifo\_mode\_control

FIFO fill before starting transfer, HW specific meaning.

**Definition** dma.h:153

[dma\_block\_config::source\_gather\_count](structdma__block__config.md#a8ffcde07d02317b3cc1b327bd0b88395)

uint16\_t source\_gather\_count

Continuous transfer count between gather boundaries.

**Definition** dma.h:123

[dma\_block\_config::source\_addr\_adj](structdma__block__config.md#a9110f948520186aa5718f57b4bbbd24a)

uint16\_t source\_addr\_adj

Source address adjustment option.

**Definition** dma.h:139

[dma\_block\_config::next\_block](structdma__block__config.md#a937168582c7473fe1b2b696cd1433605)

struct dma\_block\_config \* next\_block

Pointer to next block in a transfer list.

**Definition** dma.h:127

[dma\_block\_config::dest\_address](structdma__block__config.md#a9a66e0a647c55e94423ababf44c04325)

uint32\_t dest\_address

block starting address at destination

**Definition** dma.h:114

[dma\_block\_config::source\_address](structdma__block__config.md#a9fbd1deae8936a806ecc79bad3f3b9bb)

uint32\_t source\_address

block starting address at source

**Definition** dma.h:112

[dma\_block\_config::source\_gather\_en](structdma__block__config.md#abbac399f6c6e18ad2ed25359ebb799ef)

uint16\_t source\_gather\_en

Enable source gathering when set to 1.

**Definition** dma.h:129

[dma\_block\_config::dest\_addr\_adj](structdma__block__config.md#ad69502226d2c60adbdb9fe5e93dc0a05)

uint16\_t dest\_addr\_adj

Destination address adjustment.

**Definition** dma.h:147

[dma\_block\_config::dest\_scatter\_count](structdma__block__config.md#ae38027f6262c34d9f1abe4f923d904b4)

uint16\_t dest\_scatter\_count

Continuous transfer count between scatter boundaries.

**Definition** dma.h:121

[dma\_block\_config::flow\_control\_mode](structdma__block__config.md#aecf6805b898a70922c58d15127bafc92)

uint16\_t flow\_control\_mode

Transfer flow control mode.

**Definition** dma.h:160

[dma\_config](structdma__config.md)

DMA configuration structure.

**Definition** dma.h:195

[dma\_config::channel\_priority](structdma__config.md#a284d96c59945aaa851d235802aee979a)

uint32\_t channel\_priority

Channel priority for arbitration, HW specific.

**Definition** dma.h:241

[dma\_config::source\_handshake](structdma__config.md#a2927e31730c6ca2f5ac8db38c255d9f7)

uint32\_t source\_handshake

Source handshake, HW specific.

**Definition** dma.h:230

[dma\_config::complete\_callback\_en](structdma__config.md#a39526177f03017d245651b4f51820161)

uint32\_t complete\_callback\_en

Completion callback enable.

**Definition** dma.h:216

[dma\_config::user\_data](structdma__config.md#a510eed1cadbf411c9e94e1d1fb43d39d)

void \* user\_data

Optional attached user data for callbacks.

**Definition** dma.h:265

[dma\_config::error\_callback\_en](structdma__config.md#a66d7fe742d6e1c1f2e58a49105892961)

uint32\_t error\_callback\_en

Error callback enable.

**Definition** dma.h:223

[dma\_config::dma\_callback](structdma__config.md#a69110abc43227bd7df217c4e25bb964b)

dma\_callback\_t dma\_callback

Optional callback for completion and error events.

**Definition** dma.h:267

[dma\_config::source\_chaining\_en](structdma__config.md#a7c77afc1f546efda6ce22f50560b8840)

uint32\_t source\_chaining\_en

Source chaining enable, HW specific.

**Definition** dma.h:243

[dma\_config::dest\_chaining\_en](structdma__config.md#a8a304fdada9ec7fc87402449e1410486)

uint32\_t dest\_chaining\_en

Destination chaining enable, HW specific.

**Definition** dma.h:245

[dma\_config::dma\_slot](structdma__config.md#a8e6c5cab5ec030066a3e57e0507fbf9f)

uint32\_t dma\_slot

Which peripheral and direction, HW specific.

**Definition** dma.h:197

[dma\_config::channel\_direction](structdma__config.md#aaf903b1badff8b0fc4ef18a34c2773d7)

uint32\_t channel\_direction

Direction the transfers are occurring.

**Definition** dma.h:209

[dma\_config::source\_data\_size](structdma__config.md#ac9144783b4843182451b440d97ecd273)

uint32\_t source\_data\_size

Width of source data (in bytes).

**Definition** dma.h:253

[dma\_config::dest\_burst\_length](structdma__config.md#aca47b00f817e55bf662fdd6767a59ed0)

uint32\_t dest\_burst\_length

Destination burst length in bytes.

**Definition** dma.h:259

[dma\_config::head\_block](structdma__config.md#aca6a1cb9b580a61bf91490fecf10cb16)

struct dma\_block\_config \* head\_block

Pointer to the first block in the transfer list.

**Definition** dma.h:263

[dma\_config::linked\_channel](structdma__config.md#ace2dc918fcfea264a579b1084fcb7fe5)

uint32\_t linked\_channel

Linked channel, HW specific.

**Definition** dma.h:247

[dma\_config::source\_burst\_length](structdma__config.md#ad750b724bab1503ded7c163d8228aa80)

uint32\_t source\_burst\_length

Source burst length in bytes.

**Definition** dma.h:257

[dma\_config::block\_count](structdma__config.md#adb776a4940c71b61cab60eb05159b2d4)

uint32\_t block\_count

Number of blocks in transfer list.

**Definition** dma.h:261

[dma\_config::dest\_data\_size](structdma__config.md#adfa9efbfbef3ed41b2f8dd5b9c441e08)

uint32\_t dest\_data\_size

Width of destination data (in bytes).

**Definition** dma.h:255

[dma\_config::dest\_handshake](structdma__config.md#af570b4050200ec510df323bd31558233)

uint32\_t dest\_handshake

Destination handshake, HW specific.

**Definition** dma.h:237

[dma\_config::cyclic](structdma__config.md#afa70dbf1ee7bb5fb6a771f634783b7a2)

uint32\_t cyclic

Cyclic transfer list, HW specific.

**Definition** dma.h:249

[dma\_context](structdma__context.md)

DMA context structure Note: the dma\_context shall be the first member of DMA client driver Data,...

**Definition** dma.h:295

[dma\_context::magic](structdma__context.md#a25355c8cc60df536c9a37cdef52aa653)

int32\_t magic

magic code to identify the context

**Definition** dma.h:297

[dma\_context::atomic](structdma__context.md#a5b5776088155c9f19488d479924bec8e)

atomic\_t \* atomic

atomic holding bit flags for each channel to mark as used/unused

**Definition** dma.h:301

[dma\_context::dma\_channels](structdma__context.md#ac6685cf14ca69c7b77160e5031c0a800)

int dma\_channels

number of dma channels

**Definition** dma.h:299

[dma\_status](structdma__status.md)

DMA runtime status structure.

**Definition** dma.h:273

[dma\_status::free](structdma__status.md#a2b481bf13de03e49146eb6a26563776e)

uint32\_t free

Available buffers space, HW specific.

**Definition** dma.h:281

[dma\_status::pending\_length](structdma__status.md#a3a33f92b1d100f988fca2bea0a6deb24)

uint32\_t pending\_length

Pending length to be transferred in bytes, HW specific.

**Definition** dma.h:279

[dma\_status::busy](structdma__status.md#a92ec05d9207caa828064661897f2f31c)

bool busy

Is the current DMA transfer busy or idle.

**Definition** dma.h:275

[dma\_status::total\_copied](structdma__status.md#a9f743c98e6343d55eccc27e528b79b1a)

uint64\_t total\_copied

Total copied, HW specific.

**Definition** dma.h:287

[dma\_status::write\_position](structdma__status.md#aa7288b85f41098e59ad4f96dcea4ccde)

uint32\_t write\_position

Write position in circular DMA buffer, HW specific.

**Definition** dma.h:283

[dma\_status::dir](structdma__status.md#aacfe94ad8e60ea77bca2423bd9bf8409)

enum dma\_channel\_direction dir

Direction fo the transfer.

**Definition** dma.h:277

[dma\_status::read\_position](structdma__status.md#afa401acfb26cd26b73e4a52066989847)

uint32\_t read\_position

Read position in circular DMA buffer, HW specific.

**Definition** dma.h:285

[stat](structstat.md)

**Definition** stat.h:92

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dma.h](drivers_2dma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

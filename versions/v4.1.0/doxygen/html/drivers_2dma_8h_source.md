---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2dma_8h_source.html
original_path: doxygen/html/drivers_2dma_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

16#include <[zephyr/kernel.h](kernel_8h.md)>

17#include <[zephyr/device.h](device_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

23

32

[ 36](group__dma__interface.md#gae442d8ba73be7e53b68165647b0ea402)enum [dma\_channel\_direction](group__dma__interface.md#gae442d8ba73be7e53b68165647b0ea402) {

[ 38](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a52f28a5eff23fcddd2a138092d9f7cd5) [MEMORY\_TO\_MEMORY](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a52f28a5eff23fcddd2a138092d9f7cd5) = 0x0,

[ 40](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a4617446ef0e7c2bced585b309011a25a) [MEMORY\_TO\_PERIPHERAL](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a4617446ef0e7c2bced585b309011a25a),

[ 42](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a5fbc19c9e12c11973c0cf0a593ccf165) [PERIPHERAL\_TO\_MEMORY](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a5fbc19c9e12c11973c0cf0a593ccf165),

[ 44](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402ae23cbfefccef9d19dd91f0c746004449) [PERIPHERAL\_TO\_PERIPHERAL](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402ae23cbfefccef9d19dd91f0c746004449),

[ 46](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a7e2b4150c28b057598975e95e8b7494c) [HOST\_TO\_MEMORY](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a7e2b4150c28b057598975e95e8b7494c),

[ 48](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a61e65f3065bf7cdb40efc9039debbb60) [MEMORY\_TO\_HOST](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a61e65f3065bf7cdb40efc9039debbb60),

49

[ 53](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402ae7c3dacfd3496576c41f9c663537419a) [DMA\_CHANNEL\_DIRECTION\_COMMON\_COUNT](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402ae7c3dacfd3496576c41f9c663537419a),

54

[ 59](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a273f9cdcc2af613375cb3e235bfda037) [DMA\_CHANNEL\_DIRECTION\_PRIV\_START](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a273f9cdcc2af613375cb3e235bfda037) = [DMA\_CHANNEL\_DIRECTION\_COMMON\_COUNT](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402ae7c3dacfd3496576c41f9c663537419a),

60

[ 64](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a9114b4138c9dfb506b9428a229c55a02) [DMA\_CHANNEL\_DIRECTION\_MAX](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a9114b4138c9dfb506b9428a229c55a02) = 0x7

65};

66

[ 72](group__dma__interface.md#gafe0877ef4bd7790a4bcd46052088231c)enum [dma\_addr\_adj](group__dma__interface.md#gafe0877ef4bd7790a4bcd46052088231c) {

[ 74](group__dma__interface.md#ggafe0877ef4bd7790a4bcd46052088231cac1fe38db8443f6d8e406c66ba6bdd15e) [DMA\_ADDR\_ADJ\_INCREMENT](group__dma__interface.md#ggafe0877ef4bd7790a4bcd46052088231cac1fe38db8443f6d8e406c66ba6bdd15e),

[ 76](group__dma__interface.md#ggafe0877ef4bd7790a4bcd46052088231caacc38507d8ef3eb8021ae85d9b61b717) [DMA\_ADDR\_ADJ\_DECREMENT](group__dma__interface.md#ggafe0877ef4bd7790a4bcd46052088231caacc38507d8ef3eb8021ae85d9b61b717),

[ 78](group__dma__interface.md#ggafe0877ef4bd7790a4bcd46052088231cafeb870c1a6f9db8238a97f3ac9c6da4f) [DMA\_ADDR\_ADJ\_NO\_CHANGE](group__dma__interface.md#ggafe0877ef4bd7790a4bcd46052088231cafeb870c1a6f9db8238a97f3ac9c6da4f),

79};

80

[ 84](group__dma__interface.md#gade594552920aabbfd2106059a338498b)enum [dma\_channel\_filter](group__dma__interface.md#gade594552920aabbfd2106059a338498b) {

[ 85](group__dma__interface.md#ggade594552920aabbfd2106059a338498ba54326b41a55d7a64c808cea83520b94f) [DMA\_CHANNEL\_NORMAL](group__dma__interface.md#ggade594552920aabbfd2106059a338498ba54326b41a55d7a64c808cea83520b94f), /\* normal DMA channel \*/

[ 86](group__dma__interface.md#ggade594552920aabbfd2106059a338498bacffe4591bb7577cd8596d4dc1b51838c) [DMA\_CHANNEL\_PERIODIC](group__dma__interface.md#ggade594552920aabbfd2106059a338498bacffe4591bb7577cd8596d4dc1b51838c), /\* can be triggered by periodic sources \*/

87};

88

[ 92](group__dma__interface.md#ga08c366c8d47672eeeb37b258af20101b)enum [dma\_attribute\_type](group__dma__interface.md#ga08c366c8d47672eeeb37b258af20101b) {

[ 93](group__dma__interface.md#gga08c366c8d47672eeeb37b258af20101ba486ede0649882311fd344a52983d5f3f) [DMA\_ATTR\_BUFFER\_ADDRESS\_ALIGNMENT](group__dma__interface.md#gga08c366c8d47672eeeb37b258af20101ba486ede0649882311fd344a52983d5f3f),

[ 94](group__dma__interface.md#gga08c366c8d47672eeeb37b258af20101baa6b28cfc17b80884dddc18fcaa2b6873) [DMA\_ATTR\_BUFFER\_SIZE\_ALIGNMENT](group__dma__interface.md#gga08c366c8d47672eeeb37b258af20101baa6b28cfc17b80884dddc18fcaa2b6873),

[ 95](group__dma__interface.md#gga08c366c8d47672eeeb37b258af20101baa07cc26d400fa919df133552eb2e317b) [DMA\_ATTR\_COPY\_ALIGNMENT](group__dma__interface.md#gga08c366c8d47672eeeb37b258af20101baa07cc26d400fa919df133552eb2e317b),

[ 96](group__dma__interface.md#gga08c366c8d47672eeeb37b258af20101bafcaffeb0a1c7be27d258d73968196d18) [DMA\_ATTR\_MAX\_BLOCK\_COUNT](group__dma__interface.md#gga08c366c8d47672eeeb37b258af20101bafcaffeb0a1c7be27d258d73968196d18),

97};

98

[ 106](structdma__block__config.md)struct [dma\_block\_config](structdma__block__config.md) {

107#ifdef CONFIG\_DMA\_64BIT

109 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [source\_address](structdma__block__config.md#a9fbd1deae8936a806ecc79bad3f3b9bb);

111 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [dest\_address](structdma__block__config.md#a9a66e0a647c55e94423ababf44c04325);

112#else

[ 114](structdma__block__config.md#a9fbd1deae8936a806ecc79bad3f3b9bb) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [source\_address](structdma__block__config.md#a9fbd1deae8936a806ecc79bad3f3b9bb);

[ 116](structdma__block__config.md#a9a66e0a647c55e94423ababf44c04325) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dest\_address](structdma__block__config.md#a9a66e0a647c55e94423ababf44c04325);

117#endif

[ 119](structdma__block__config.md#a3180ef98f007ad9be7f6ff363dc125c3) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [source\_gather\_interval](structdma__block__config.md#a3180ef98f007ad9be7f6ff363dc125c3);

[ 121](structdma__block__config.md#a18bafb80538bca9c12197955770b6511) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dest\_scatter\_interval](structdma__block__config.md#a18bafb80538bca9c12197955770b6511);

[ 123](structdma__block__config.md#ae38027f6262c34d9f1abe4f923d904b4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dest\_scatter\_count](structdma__block__config.md#ae38027f6262c34d9f1abe4f923d904b4);

[ 125](structdma__block__config.md#a8ffcde07d02317b3cc1b327bd0b88395) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [source\_gather\_count](structdma__block__config.md#a8ffcde07d02317b3cc1b327bd0b88395);

[ 127](structdma__block__config.md#a3fdab19df16d5e96054aabffbf27fcc1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [block\_size](structdma__block__config.md#a3fdab19df16d5e96054aabffbf27fcc1);

[ 129](structdma__block__config.md#a937168582c7473fe1b2b696cd1433605) struct [dma\_block\_config](structdma__block__config.md) \*[next\_block](structdma__block__config.md#a937168582c7473fe1b2b696cd1433605);

[ 131](structdma__block__config.md#abbac399f6c6e18ad2ed25359ebb799ef) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [source\_gather\_en](structdma__block__config.md#abbac399f6c6e18ad2ed25359ebb799ef) : 1;

[ 133](structdma__block__config.md#a778935d5b806002b902b72304b845ea0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dest\_scatter\_en](structdma__block__config.md#a778935d5b806002b902b72304b845ea0) : 1;

[ 141](structdma__block__config.md#a9110f948520186aa5718f57b4bbbd24a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [source\_addr\_adj](structdma__block__config.md#a9110f948520186aa5718f57b4bbbd24a) : 2;

[ 149](structdma__block__config.md#ad69502226d2c60adbdb9fe5e93dc0a05) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dest\_addr\_adj](structdma__block__config.md#ad69502226d2c60adbdb9fe5e93dc0a05) : 2;

[ 151](structdma__block__config.md#a4f8f5b65002f65eaacdd3dde26c47170) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [source\_reload\_en](structdma__block__config.md#a4f8f5b65002f65eaacdd3dde26c47170) : 1;

[ 153](structdma__block__config.md#a7dedf429f44f3af6fcc0db125d6494c8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dest\_reload\_en](structdma__block__config.md#a7dedf429f44f3af6fcc0db125d6494c8) : 1;

[ 155](structdma__block__config.md#a877a30b62fd8e0e1773890a10c8a2751) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [fifo\_mode\_control](structdma__block__config.md#a877a30b62fd8e0e1773890a10c8a2751) : 4;

[ 162](structdma__block__config.md#aecf6805b898a70922c58d15127bafc92) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flow\_control\_mode](structdma__block__config.md#aecf6805b898a70922c58d15127bafc92) : 1;

163

164 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \_reserved : 3;

165};

166

[ 168](group__dma__interface.md#gad4fc9a9c59f4e07c81a4c2f3b57c9ccb)#define DMA\_STATUS\_COMPLETE 0

[ 170](group__dma__interface.md#gab74c89289c8429071522cb89ac066eea)#define DMA\_STATUS\_BLOCK 1

171

[ 190](group__dma__interface.md#ga94745b4472ee1addd4f82db4e59e9fb5)typedef void (\*[dma\_callback\_t](group__dma__interface.md#ga94745b4472ee1addd4f82db4e59e9fb5))(const struct [device](structdevice.md) \*dev, void \*user\_data,

191 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, int status);

192

[ 197](structdma__config.md)struct [dma\_config](structdma__config.md) {

[ 199](structdma__config.md#a8e6c5cab5ec030066a3e57e0507fbf9f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dma\_slot](structdma__config.md#a8e6c5cab5ec030066a3e57e0507fbf9f) : 8;

[ 211](structdma__config.md#aaf903b1badff8b0fc4ef18a34c2773d7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [channel\_direction](structdma__config.md#aaf903b1badff8b0fc4ef18a34c2773d7) : 3;

[ 218](structdma__config.md#a39526177f03017d245651b4f51820161) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [complete\_callback\_en](structdma__config.md#a39526177f03017d245651b4f51820161) : 1;

[ 225](structdma__config.md#a416a0ef20318fe77d7e383caeee67e94) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [error\_callback\_dis](structdma__config.md#a416a0ef20318fe77d7e383caeee67e94) : 1;

[ 232](structdma__config.md#a2927e31730c6ca2f5ac8db38c255d9f7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [source\_handshake](structdma__config.md#a2927e31730c6ca2f5ac8db38c255d9f7) : 1;

[ 239](structdma__config.md#af570b4050200ec510df323bd31558233) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dest\_handshake](structdma__config.md#af570b4050200ec510df323bd31558233) : 1;

[ 243](structdma__config.md#a284d96c59945aaa851d235802aee979a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [channel\_priority](structdma__config.md#a284d96c59945aaa851d235802aee979a) : 4;

[ 245](structdma__config.md#a7c77afc1f546efda6ce22f50560b8840) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [source\_chaining\_en](structdma__config.md#a7c77afc1f546efda6ce22f50560b8840) : 1;

[ 247](structdma__config.md#a8a304fdada9ec7fc87402449e1410486) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dest\_chaining\_en](structdma__config.md#a8a304fdada9ec7fc87402449e1410486) : 1;

[ 249](structdma__config.md#ace2dc918fcfea264a579b1084fcb7fe5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [linked\_channel](structdma__config.md#ace2dc918fcfea264a579b1084fcb7fe5) : 7;

[ 251](structdma__config.md#afa70dbf1ee7bb5fb6a771f634783b7a2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cyclic](structdma__config.md#afa70dbf1ee7bb5fb6a771f634783b7a2) : 1;

252

253 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \_reserved : 3;

[ 255](structdma__config.md#ac9144783b4843182451b440d97ecd273) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [source\_data\_size](structdma__config.md#ac9144783b4843182451b440d97ecd273) : 16;

[ 257](structdma__config.md#adfa9efbfbef3ed41b2f8dd5b9c441e08) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dest\_data\_size](structdma__config.md#adfa9efbfbef3ed41b2f8dd5b9c441e08) : 16;

[ 259](structdma__config.md#ad750b724bab1503ded7c163d8228aa80) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [source\_burst\_length](structdma__config.md#ad750b724bab1503ded7c163d8228aa80) : 16;

[ 261](structdma__config.md#aca47b00f817e55bf662fdd6767a59ed0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dest\_burst\_length](structdma__config.md#aca47b00f817e55bf662fdd6767a59ed0) : 16;

[ 263](structdma__config.md#adb776a4940c71b61cab60eb05159b2d4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [block\_count](structdma__config.md#adb776a4940c71b61cab60eb05159b2d4);

[ 265](structdma__config.md#aca6a1cb9b580a61bf91490fecf10cb16) struct [dma\_block\_config](structdma__block__config.md) \*[head\_block](structdma__config.md#aca6a1cb9b580a61bf91490fecf10cb16);

[ 267](structdma__config.md#a510eed1cadbf411c9e94e1d1fb43d39d) void \*[user\_data](structdma__config.md#a510eed1cadbf411c9e94e1d1fb43d39d);

[ 269](structdma__config.md#a69110abc43227bd7df217c4e25bb964b) [dma\_callback\_t](group__dma__interface.md#ga94745b4472ee1addd4f82db4e59e9fb5) [dma\_callback](structdma__config.md#a69110abc43227bd7df217c4e25bb964b);

270};

271

[ 275](structdma__status.md)struct [dma\_status](structdma__status.md) {

[ 277](structdma__status.md#a92ec05d9207caa828064661897f2f31c) bool [busy](structdma__status.md#a92ec05d9207caa828064661897f2f31c);

[ 279](structdma__status.md#aacfe94ad8e60ea77bca2423bd9bf8409) enum [dma\_channel\_direction](group__dma__interface.md#gae442d8ba73be7e53b68165647b0ea402) [dir](structdma__status.md#aacfe94ad8e60ea77bca2423bd9bf8409);

[ 281](structdma__status.md#a3a33f92b1d100f988fca2bea0a6deb24) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pending\_length](structdma__status.md#a3a33f92b1d100f988fca2bea0a6deb24);

[ 283](structdma__status.md#a2b481bf13de03e49146eb6a26563776e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [free](structdma__status.md#a2b481bf13de03e49146eb6a26563776e);

[ 285](structdma__status.md#aa7288b85f41098e59ad4f96dcea4ccde) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [write\_position](structdma__status.md#aa7288b85f41098e59ad4f96dcea4ccde);

[ 287](structdma__status.md#afa401acfb26cd26b73e4a52066989847) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [read\_position](structdma__status.md#afa401acfb26cd26b73e4a52066989847);

[ 289](structdma__status.md#a9f743c98e6343d55eccc27e528b79b1a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [total\_copied](structdma__status.md#a9f743c98e6343d55eccc27e528b79b1a);

290};

291

[ 297](structdma__context.md)struct [dma\_context](structdma__context.md) {

[ 299](structdma__context.md#a25355c8cc60df536c9a37cdef52aa653) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [magic](structdma__context.md#a25355c8cc60df536c9a37cdef52aa653);

[ 301](structdma__context.md#ac6685cf14ca69c7b77160e5031c0a800) int [dma\_channels](structdma__context.md#ac6685cf14ca69c7b77160e5031c0a800);

[ 303](structdma__context.md#a5b5776088155c9f19488d479924bec8e) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*[atomic](structdma__context.md#a5b5776088155c9f19488d479924bec8e);

304};

305

[ 307](group__dma__interface.md#gae28ba5114dc2e9ecb89ccf9b623e938f)#define DMA\_MAGIC 0x47494749

308

315typedef int (\*dma\_api\_config)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

316 struct [dma\_config](structdma__config.md) \*config);

317

318#ifdef CONFIG\_DMA\_64BIT

319typedef int (\*dma\_api\_reload)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

320 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) src, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) dst, size\_t size);

321#else

322typedef int (\*dma\_api\_reload)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

323 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) src, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dst, size\_t size);

324#endif

325

326typedef int (\*dma\_api\_start)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel);

327

328typedef int (\*dma\_api\_stop)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel);

329

330typedef int (\*dma\_api\_suspend)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel);

331

332typedef int (\*dma\_api\_resume)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel);

333

334typedef int (\*dma\_api\_get\_status)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

335 struct [dma\_status](structdma__status.md) \*status);

336

337typedef int (\*dma\_api\_get\_attribute)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) type, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*value);

338

352typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*dma\_api\_chan\_filter)(const struct [device](structdevice.md) \*dev,

353 int channel, void \*filter\_param);

354

366typedef void (\*dma\_api\_chan\_release)(const struct [device](structdevice.md) \*dev,

367 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel);

368

369\_\_subsystem struct dma\_driver\_api {

370 dma\_api\_config config;

371 dma\_api\_reload reload;

372 dma\_api\_start start;

373 dma\_api\_stop stop;

374 dma\_api\_suspend suspend;

375 dma\_api\_resume resume;

376 dma\_api\_get\_status get\_status;

377 dma\_api\_get\_attribute get\_attribute;

378 dma\_api\_chan\_filter chan\_filter;

379 dma\_api\_chan\_release chan\_release;

380};

384

[ 396](group__dma__interface.md#ga6df1a6b89f271a0eae01c17b748bd2df)static inline int [dma\_config](group__dma__interface.md#ga6df1a6b89f271a0eae01c17b748bd2df)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

397 struct [dma\_config](structdma__config.md) \*config)

398{

399 const struct dma\_driver\_api \*api =

400 (const struct dma\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

401

402 return api->config(dev, channel, config);

403}

404

418#ifdef CONFIG\_DMA\_64BIT

419static inline int [dma\_reload](group__dma__interface.md#ga55bd5d550349c11c63ef47c2ed861f36)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

420 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) src, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) dst, size\_t size)

421#else

[ 422](group__dma__interface.md#ga55bd5d550349c11c63ef47c2ed861f36)static inline int [dma\_reload](group__dma__interface.md#ga55bd5d550349c11c63ef47c2ed861f36)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

423 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) src, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dst, size\_t size)

424#endif

425{

426 const struct dma\_driver\_api \*api =

427 (const struct dma\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

428

429 if (api->reload) {

430 return api->reload(dev, channel, src, dst, size);

431 }

432

433 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

434}

435

[ 455](group__dma__interface.md#gac2ddafd17680f59e4e8fe5f6e2eaba48)\_\_syscall int [dma\_start](group__dma__interface.md#gac2ddafd17680f59e4e8fe5f6e2eaba48)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel);

456

457static inline int z\_impl\_dma\_start(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel)

458{

459 const struct dma\_driver\_api \*api =

460 (const struct dma\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

461

462 return api->start(dev, channel);

463}

464

[ 483](group__dma__interface.md#ga305cc72d0804028b77aa82dd07c926ad)\_\_syscall int [dma\_stop](group__dma__interface.md#ga305cc72d0804028b77aa82dd07c926ad)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel);

484

485static inline int z\_impl\_dma\_stop(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel)

486{

487 const struct dma\_driver\_api \*api =

488 (const struct dma\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

489

490 return api->stop(dev, channel);

491}

492

493

[ 510](group__dma__interface.md#ga6779850f6082259f5bef29b1282effdb)\_\_syscall int [dma\_suspend](group__dma__interface.md#ga6779850f6082259f5bef29b1282effdb)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel);

511

512static inline int z\_impl\_dma\_suspend(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel)

513{

514 const struct dma\_driver\_api \*api = (const struct dma\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

515

516 if (api->suspend == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

517 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

518 }

519 return api->suspend(dev, channel);

520}

521

[ 538](group__dma__interface.md#ga89a3d056803d7f2dd1c8b6e535ef4f1d)\_\_syscall int [dma\_resume](group__dma__interface.md#ga89a3d056803d7f2dd1c8b6e535ef4f1d)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel);

539

540static inline int z\_impl\_dma\_resume(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel)

541{

542 const struct dma\_driver\_api \*api = (const struct dma\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

543

544 if (api->resume == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

545 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

546 }

547 return api->resume(dev, channel);

548}

549

[ 566](group__dma__interface.md#ga91cc55f781744069f1f9f29249bdee8d)\_\_syscall int [dma\_request\_channel](group__dma__interface.md#ga91cc55f781744069f1f9f29249bdee8d)(const struct [device](structdevice.md) \*dev,

567 void \*filter\_param);

568

569static inline int z\_impl\_dma\_request\_channel(const struct [device](structdevice.md) \*dev,

570 void \*filter\_param)

571{

572 int i = 0;

573 int channel = -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

574 const struct dma\_driver\_api \*api =

575 (const struct dma\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

576 /\* dma\_context shall be the first one in dev data \*/

577 struct [dma\_context](structdma__context.md) \*dma\_ctx = (struct [dma\_context](structdma__context.md) \*)dev->[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

578

579 if (dma\_ctx->magic != [DMA\_MAGIC](group__dma__interface.md#gae28ba5114dc2e9ecb89ccf9b623e938f)) {

580 return channel;

581 }

582

583 for (i = 0; i < dma\_ctx->dma\_channels; i++) {

584 if (![atomic\_test\_and\_set\_bit](group__atomic__apis.md#ga7ff45e13aa5f8be5d7a550e49f5c720b)(dma\_ctx->atomic, i)) {

585 if (api->chan\_filter &&

586 !api->chan\_filter(dev, i, filter\_param)) {

587 [atomic\_clear\_bit](group__atomic__apis.md#ga1c1693d524c49d11fd32b323a39d718e)(dma\_ctx->atomic, i);

588 continue;

589 }

590 channel = i;

591 break;

592 }

593 }

594

595 return channel;

596}

597

[ 611](group__dma__interface.md#gab02df5277d79a04a65132365e7b5d3de)\_\_syscall void [dma\_release\_channel](group__dma__interface.md#gab02df5277d79a04a65132365e7b5d3de)(const struct [device](structdevice.md) \*dev,

612 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel);

613

614static inline void z\_impl\_dma\_release\_channel(const struct [device](structdevice.md) \*dev,

615 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel)

616{

617 const struct dma\_driver\_api \*api =

618 (const struct dma\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

619 struct [dma\_context](structdma__context.md) \*dma\_ctx = (struct [dma\_context](structdma__context.md) \*)dev->[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

620

621 if (dma\_ctx->magic != [DMA\_MAGIC](group__dma__interface.md#gae28ba5114dc2e9ecb89ccf9b623e938f)) {

622 return;

623 }

624

625 if ((int)channel < dma\_ctx->[dma\_channels](structdma__context.md#ac6685cf14ca69c7b77160e5031c0a800)) {

626 if (api->chan\_release) {

627 api->chan\_release(dev, channel);

628 }

629

630 [atomic\_clear\_bit](group__atomic__apis.md#ga1c1693d524c49d11fd32b323a39d718e)(dma\_ctx->atomic, channel);

631 }

632

633}

634

[ 647](group__dma__interface.md#ga729d8f1163458d447d0a4b20cb9e4659)\_\_syscall int [dma\_chan\_filter](group__dma__interface.md#ga729d8f1163458d447d0a4b20cb9e4659)(const struct [device](structdevice.md) \*dev,

648 int channel, void \*filter\_param);

649

650static inline int z\_impl\_dma\_chan\_filter(const struct [device](structdevice.md) \*dev,

651 int channel, void \*filter\_param)

652{

653 const struct dma\_driver\_api \*api =

654 (const struct dma\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

655

656 if (api->chan\_filter) {

657 return api->chan\_filter(dev, channel, filter\_param);

658 }

659

660 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

661}

662

[ 679](group__dma__interface.md#ga2cae500f1f9ed42ad338a40ec8655544)static inline int [dma\_get\_status](group__dma__interface.md#ga2cae500f1f9ed42ad338a40ec8655544)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

680 struct [dma\_status](structdma__status.md) \*[stat](structstat.md))

681{

682 const struct dma\_driver\_api \*api =

683 (const struct dma\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

684

685 if (api->get\_status) {

686 return api->get\_status(dev, channel, [stat](structstat.md));

687 }

688

689 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

690}

691

[ 709](group__dma__interface.md#ga641f3fa492bfb17cf9f0a0361d429257)static inline int [dma\_get\_attribute](group__dma__interface.md#ga641f3fa492bfb17cf9f0a0361d429257)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) type, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*value)

710{

711 const struct dma\_driver\_api \*api = (const struct dma\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

712

713 if (api->get\_attribute) {

714 return api->get\_attribute(dev, type, value);

715 }

716

717 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

718}

719

[ 733](group__dma__interface.md#gadd1724a843bba4ccc1c65c9fb9d3d921)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dma\_width\_index](group__dma__interface.md#gadd1724a843bba4ccc1c65c9fb9d3d921)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size)

734{

735 /\* Check boundaries (max supported width is 32 Bytes) \*/

736 if (size < 1 || size > 32) {

737 return 0; /\* Zero is the default (8 Bytes) \*/

738 }

739

740 /\* Ensure size is a power of 2 \*/

741 if (![is\_power\_of\_two](group__sys-util.md#gadfe7046eb6c39bb3c84c18d8ac7a230e)(size)) {

742 return 0; /\* Zero is the default (8 Bytes) \*/

743 }

744

745 /\* Convert to bit pattern for writing to a register \*/

746 return [find\_msb\_set](ffs_8h.md#a088db7d02e8f1fc559cbe1ec048494e8)(size);

747}

748

[ 762](group__dma__interface.md#gaac27f2ee664671884087ee3d2a2863ce)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dma\_burst\_index](group__dma__interface.md#gaac27f2ee664671884087ee3d2a2863ce)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) burst)

763{

764 /\* Check boundaries (max supported burst length is 256) \*/

765 if (burst < 1 || burst > 256) {

766 return 0; /\* Zero is the default (1 burst length) \*/

767 }

768

769 /\* Ensure burst is a power of 2 \*/

770 if (!(burst & (burst - 1))) {

771 return 0; /\* Zero is the default (1 burst length) \*/

772 }

773

774 /\* Convert to bit pattern for writing to a register \*/

775 return [find\_msb\_set](ffs_8h.md#a088db7d02e8f1fc559cbe1ec048494e8)(burst);

776}

777

[ 787](group__dma__interface.md#ga542e1a0fa0d851a51e4c8abf9a820e0c)#define DMA\_BUF\_ADDR\_ALIGNMENT(node) DT\_PROP(node, dma\_buf\_addr\_alignment)

788

[ 798](group__dma__interface.md#ga76dfdfecc732319908f381883c630a2b)#define DMA\_BUF\_SIZE\_ALIGNMENT(node) DT\_PROP(node, dma\_buf\_size\_alignment)

799

[ 806](group__dma__interface.md#ga083e8b0a863b0833c55158053d286f15)#define DMA\_COPY\_ALIGNMENT(node) DT\_PROP(node, dma\_copy\_alignment)

807

811

812#ifdef \_\_cplusplus

813}

814#endif

815

816#include <zephyr/syscalls/dma.h>

817

818#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_H\_ \*/

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

Atomically set a bit and test it.

**Definition** atomic.h:170

[dma\_attribute\_type](group__dma__interface.md#ga08c366c8d47672eeeb37b258af20101b)

dma\_attribute\_type

DMA attributes.

**Definition** dma.h:92

[dma\_get\_status](group__dma__interface.md#ga2cae500f1f9ed42ad338a40ec8655544)

static int dma\_get\_status(const struct device \*dev, uint32\_t channel, struct dma\_status \*stat)

get current runtime status of DMA transfer

**Definition** dma.h:679

[dma\_stop](group__dma__interface.md#ga305cc72d0804028b77aa82dd07c926ad)

int dma\_stop(const struct device \*dev, uint32\_t channel)

Stops the DMA transfer and disables the channel.

[dma\_reload](group__dma__interface.md#ga55bd5d550349c11c63ef47c2ed861f36)

static int dma\_reload(const struct device \*dev, uint32\_t channel, uint32\_t src, uint32\_t dst, size\_t size)

Reload buffer(s) for a DMA channel.

**Definition** dma.h:422

[dma\_get\_attribute](group__dma__interface.md#ga641f3fa492bfb17cf9f0a0361d429257)

static int dma\_get\_attribute(const struct device \*dev, uint32\_t type, uint32\_t \*value)

get attribute of a dma controller

**Definition** dma.h:709

[dma\_suspend](group__dma__interface.md#ga6779850f6082259f5bef29b1282effdb)

int dma\_suspend(const struct device \*dev, uint32\_t channel)

Suspend a DMA channel transfer.

[dma\_config](group__dma__interface.md#ga6df1a6b89f271a0eae01c17b748bd2df)

static int dma\_config(const struct device \*dev, uint32\_t channel, struct dma\_config \*config)

Configure individual channel for DMA transfer.

**Definition** dma.h:396

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

**Definition** dma.h:190

[dma\_burst\_index](group__dma__interface.md#gaac27f2ee664671884087ee3d2a2863ce)

static uint32\_t dma\_burst\_index(uint32\_t burst)

Look-up generic burst index to be used in registers.

**Definition** dma.h:762

[dma\_release\_channel](group__dma__interface.md#gab02df5277d79a04a65132365e7b5d3de)

void dma\_release\_channel(const struct device \*dev, uint32\_t channel)

release DMA channel.

[dma\_start](group__dma__interface.md#gac2ddafd17680f59e4e8fe5f6e2eaba48)

int dma\_start(const struct device \*dev, uint32\_t channel)

Enables DMA channel and starts the transfer, the channel must be configured beforehand.

[dma\_width\_index](group__dma__interface.md#gadd1724a843bba4ccc1c65c9fb9d3d921)

static uint32\_t dma\_width\_index(uint32\_t size)

Look-up generic width index to be used in registers.

**Definition** dma.h:733

[dma\_channel\_filter](group__dma__interface.md#gade594552920aabbfd2106059a338498b)

dma\_channel\_filter

DMA channel attributes.

**Definition** dma.h:84

[DMA\_MAGIC](group__dma__interface.md#gae28ba5114dc2e9ecb89ccf9b623e938f)

#define DMA\_MAGIC

Magic code to identify context content.

**Definition** dma.h:307

[dma\_channel\_direction](group__dma__interface.md#gae442d8ba73be7e53b68165647b0ea402)

dma\_channel\_direction

DMA channel direction.

**Definition** dma.h:36

[dma\_addr\_adj](group__dma__interface.md#gafe0877ef4bd7790a4bcd46052088231c)

dma\_addr\_adj

DMA address adjustment.

**Definition** dma.h:72

[DMA\_ATTR\_BUFFER\_ADDRESS\_ALIGNMENT](group__dma__interface.md#gga08c366c8d47672eeeb37b258af20101ba486ede0649882311fd344a52983d5f3f)

@ DMA\_ATTR\_BUFFER\_ADDRESS\_ALIGNMENT

**Definition** dma.h:93

[DMA\_ATTR\_COPY\_ALIGNMENT](group__dma__interface.md#gga08c366c8d47672eeeb37b258af20101baa07cc26d400fa919df133552eb2e317b)

@ DMA\_ATTR\_COPY\_ALIGNMENT

**Definition** dma.h:95

[DMA\_ATTR\_BUFFER\_SIZE\_ALIGNMENT](group__dma__interface.md#gga08c366c8d47672eeeb37b258af20101baa6b28cfc17b80884dddc18fcaa2b6873)

@ DMA\_ATTR\_BUFFER\_SIZE\_ALIGNMENT

**Definition** dma.h:94

[DMA\_ATTR\_MAX\_BLOCK\_COUNT](group__dma__interface.md#gga08c366c8d47672eeeb37b258af20101bafcaffeb0a1c7be27d258d73968196d18)

@ DMA\_ATTR\_MAX\_BLOCK\_COUNT

**Definition** dma.h:96

[DMA\_CHANNEL\_NORMAL](group__dma__interface.md#ggade594552920aabbfd2106059a338498ba54326b41a55d7a64c808cea83520b94f)

@ DMA\_CHANNEL\_NORMAL

**Definition** dma.h:85

[DMA\_CHANNEL\_PERIODIC](group__dma__interface.md#ggade594552920aabbfd2106059a338498bacffe4591bb7577cd8596d4dc1b51838c)

@ DMA\_CHANNEL\_PERIODIC

**Definition** dma.h:86

[DMA\_CHANNEL\_DIRECTION\_PRIV\_START](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a273f9cdcc2af613375cb3e235bfda037)

@ DMA\_CHANNEL\_DIRECTION\_PRIV\_START

This and higher values are dma controller or soc specific.

**Definition** dma.h:59

[MEMORY\_TO\_PERIPHERAL](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a4617446ef0e7c2bced585b309011a25a)

@ MEMORY\_TO\_PERIPHERAL

Memory to peripheral.

**Definition** dma.h:40

[MEMORY\_TO\_MEMORY](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a52f28a5eff23fcddd2a138092d9f7cd5)

@ MEMORY\_TO\_MEMORY

Memory to memory.

**Definition** dma.h:38

[PERIPHERAL\_TO\_MEMORY](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a5fbc19c9e12c11973c0cf0a593ccf165)

@ PERIPHERAL\_TO\_MEMORY

Peripheral to memory.

**Definition** dma.h:42

[MEMORY\_TO\_HOST](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a61e65f3065bf7cdb40efc9039debbb60)

@ MEMORY\_TO\_HOST

Memory to host.

**Definition** dma.h:48

[HOST\_TO\_MEMORY](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a7e2b4150c28b057598975e95e8b7494c)

@ HOST\_TO\_MEMORY

Host to memory.

**Definition** dma.h:46

[DMA\_CHANNEL\_DIRECTION\_MAX](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a9114b4138c9dfb506b9428a229c55a02)

@ DMA\_CHANNEL\_DIRECTION\_MAX

Maximum allowed value (3 bit field!).

**Definition** dma.h:64

[PERIPHERAL\_TO\_PERIPHERAL](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402ae23cbfefccef9d19dd91f0c746004449)

@ PERIPHERAL\_TO\_PERIPHERAL

Peripheral to peripheral.

**Definition** dma.h:44

[DMA\_CHANNEL\_DIRECTION\_COMMON\_COUNT](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402ae7c3dacfd3496576c41f9c663537419a)

@ DMA\_CHANNEL\_DIRECTION\_COMMON\_COUNT

Number of all common channel directions.

**Definition** dma.h:53

[DMA\_ADDR\_ADJ\_DECREMENT](group__dma__interface.md#ggafe0877ef4bd7790a4bcd46052088231caacc38507d8ef3eb8021ae85d9b61b717)

@ DMA\_ADDR\_ADJ\_DECREMENT

Decrement the address.

**Definition** dma.h:76

[DMA\_ADDR\_ADJ\_INCREMENT](group__dma__interface.md#ggafe0877ef4bd7790a4bcd46052088231cac1fe38db8443f6d8e406c66ba6bdd15e)

@ DMA\_ADDR\_ADJ\_INCREMENT

Increment the address.

**Definition** dma.h:74

[DMA\_ADDR\_ADJ\_NO\_CHANGE](group__dma__interface.md#ggafe0877ef4bd7790a4bcd46052088231cafeb870c1a6f9db8238a97f3ac9c6da4f)

@ DMA\_ADDR\_ADJ\_NO\_CHANGE

No change the address.

**Definition** dma.h:78

[is\_power\_of\_two](group__sys-util.md#gadfe7046eb6c39bb3c84c18d8ac7a230e)

static bool is\_power\_of\_two(unsigned int x)

Is x a power of two?

**Definition** util.h:439

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:60

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[kernel.h](kernel_8h.md)

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

**Definition** device.h:453

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:463

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:459

[dma\_block\_config](structdma__block__config.md)

DMA block configuration structure.

**Definition** dma.h:106

[dma\_block\_config::dest\_scatter\_interval](structdma__block__config.md#a18bafb80538bca9c12197955770b6511)

uint32\_t dest\_scatter\_interval

Address adjustment at scatter boundary.

**Definition** dma.h:121

[dma\_block\_config::source\_gather\_interval](structdma__block__config.md#a3180ef98f007ad9be7f6ff363dc125c3)

uint32\_t source\_gather\_interval

Address adjustment at gather boundary.

**Definition** dma.h:119

[dma\_block\_config::block\_size](structdma__block__config.md#a3fdab19df16d5e96054aabffbf27fcc1)

uint32\_t block\_size

Number of bytes to be transferred for this block.

**Definition** dma.h:127

[dma\_block\_config::source\_reload\_en](structdma__block__config.md#a4f8f5b65002f65eaacdd3dde26c47170)

uint16\_t source\_reload\_en

Reload source address at the end of block transfer.

**Definition** dma.h:151

[dma\_block\_config::dest\_scatter\_en](structdma__block__config.md#a778935d5b806002b902b72304b845ea0)

uint16\_t dest\_scatter\_en

Enable destination scattering when set to 1.

**Definition** dma.h:133

[dma\_block\_config::dest\_reload\_en](structdma__block__config.md#a7dedf429f44f3af6fcc0db125d6494c8)

uint16\_t dest\_reload\_en

Reload destination address at the end of block transfer.

**Definition** dma.h:153

[dma\_block\_config::fifo\_mode\_control](structdma__block__config.md#a877a30b62fd8e0e1773890a10c8a2751)

uint16\_t fifo\_mode\_control

FIFO fill before starting transfer, HW specific meaning.

**Definition** dma.h:155

[dma\_block\_config::source\_gather\_count](structdma__block__config.md#a8ffcde07d02317b3cc1b327bd0b88395)

uint16\_t source\_gather\_count

Continuous transfer count between gather boundaries.

**Definition** dma.h:125

[dma\_block\_config::source\_addr\_adj](structdma__block__config.md#a9110f948520186aa5718f57b4bbbd24a)

uint16\_t source\_addr\_adj

Source address adjustment option.

**Definition** dma.h:141

[dma\_block\_config::next\_block](structdma__block__config.md#a937168582c7473fe1b2b696cd1433605)

struct dma\_block\_config \* next\_block

Pointer to next block in a transfer list.

**Definition** dma.h:129

[dma\_block\_config::dest\_address](structdma__block__config.md#a9a66e0a647c55e94423ababf44c04325)

uint32\_t dest\_address

block starting address at destination

**Definition** dma.h:116

[dma\_block\_config::source\_address](structdma__block__config.md#a9fbd1deae8936a806ecc79bad3f3b9bb)

uint32\_t source\_address

block starting address at source

**Definition** dma.h:114

[dma\_block\_config::source\_gather\_en](structdma__block__config.md#abbac399f6c6e18ad2ed25359ebb799ef)

uint16\_t source\_gather\_en

Enable source gathering when set to 1.

**Definition** dma.h:131

[dma\_block\_config::dest\_addr\_adj](structdma__block__config.md#ad69502226d2c60adbdb9fe5e93dc0a05)

uint16\_t dest\_addr\_adj

Destination address adjustment.

**Definition** dma.h:149

[dma\_block\_config::dest\_scatter\_count](structdma__block__config.md#ae38027f6262c34d9f1abe4f923d904b4)

uint16\_t dest\_scatter\_count

Continuous transfer count between scatter boundaries.

**Definition** dma.h:123

[dma\_block\_config::flow\_control\_mode](structdma__block__config.md#aecf6805b898a70922c58d15127bafc92)

uint16\_t flow\_control\_mode

Transfer flow control mode.

**Definition** dma.h:162

[dma\_config](structdma__config.md)

DMA configuration structure.

**Definition** dma.h:197

[dma\_config::channel\_priority](structdma__config.md#a284d96c59945aaa851d235802aee979a)

uint32\_t channel\_priority

Channel priority for arbitration, HW specific.

**Definition** dma.h:243

[dma\_config::source\_handshake](structdma__config.md#a2927e31730c6ca2f5ac8db38c255d9f7)

uint32\_t source\_handshake

Source handshake, HW specific.

**Definition** dma.h:232

[dma\_config::complete\_callback\_en](structdma__config.md#a39526177f03017d245651b4f51820161)

uint32\_t complete\_callback\_en

Completion callback enable.

**Definition** dma.h:218

[dma\_config::error\_callback\_dis](structdma__config.md#a416a0ef20318fe77d7e383caeee67e94)

uint32\_t error\_callback\_dis

Error callback disable.

**Definition** dma.h:225

[dma\_config::user\_data](structdma__config.md#a510eed1cadbf411c9e94e1d1fb43d39d)

void \* user\_data

Optional attached user data for callbacks.

**Definition** dma.h:267

[dma\_config::dma\_callback](structdma__config.md#a69110abc43227bd7df217c4e25bb964b)

dma\_callback\_t dma\_callback

Optional callback for completion and error events.

**Definition** dma.h:269

[dma\_config::source\_chaining\_en](structdma__config.md#a7c77afc1f546efda6ce22f50560b8840)

uint32\_t source\_chaining\_en

Source chaining enable, HW specific.

**Definition** dma.h:245

[dma\_config::dest\_chaining\_en](structdma__config.md#a8a304fdada9ec7fc87402449e1410486)

uint32\_t dest\_chaining\_en

Destination chaining enable, HW specific.

**Definition** dma.h:247

[dma\_config::dma\_slot](structdma__config.md#a8e6c5cab5ec030066a3e57e0507fbf9f)

uint32\_t dma\_slot

Which peripheral and direction, HW specific.

**Definition** dma.h:199

[dma\_config::channel\_direction](structdma__config.md#aaf903b1badff8b0fc4ef18a34c2773d7)

uint32\_t channel\_direction

Direction the transfers are occurring.

**Definition** dma.h:211

[dma\_config::source\_data\_size](structdma__config.md#ac9144783b4843182451b440d97ecd273)

uint32\_t source\_data\_size

Width of source data (in bytes).

**Definition** dma.h:255

[dma\_config::dest\_burst\_length](structdma__config.md#aca47b00f817e55bf662fdd6767a59ed0)

uint32\_t dest\_burst\_length

Destination burst length in bytes.

**Definition** dma.h:261

[dma\_config::head\_block](structdma__config.md#aca6a1cb9b580a61bf91490fecf10cb16)

struct dma\_block\_config \* head\_block

Pointer to the first block in the transfer list.

**Definition** dma.h:265

[dma\_config::linked\_channel](structdma__config.md#ace2dc918fcfea264a579b1084fcb7fe5)

uint32\_t linked\_channel

Linked channel, HW specific.

**Definition** dma.h:249

[dma\_config::source\_burst\_length](structdma__config.md#ad750b724bab1503ded7c163d8228aa80)

uint32\_t source\_burst\_length

Source burst length in bytes.

**Definition** dma.h:259

[dma\_config::block\_count](structdma__config.md#adb776a4940c71b61cab60eb05159b2d4)

uint32\_t block\_count

Number of blocks in transfer list.

**Definition** dma.h:263

[dma\_config::dest\_data\_size](structdma__config.md#adfa9efbfbef3ed41b2f8dd5b9c441e08)

uint32\_t dest\_data\_size

Width of destination data (in bytes).

**Definition** dma.h:257

[dma\_config::dest\_handshake](structdma__config.md#af570b4050200ec510df323bd31558233)

uint32\_t dest\_handshake

Destination handshake, HW specific.

**Definition** dma.h:239

[dma\_config::cyclic](structdma__config.md#afa70dbf1ee7bb5fb6a771f634783b7a2)

uint32\_t cyclic

Cyclic transfer list, HW specific.

**Definition** dma.h:251

[dma\_context](structdma__context.md)

DMA context structure Note: the dma\_context shall be the first member of DMA client driver Data,...

**Definition** dma.h:297

[dma\_context::magic](structdma__context.md#a25355c8cc60df536c9a37cdef52aa653)

int32\_t magic

magic code to identify the context

**Definition** dma.h:299

[dma\_context::atomic](structdma__context.md#a5b5776088155c9f19488d479924bec8e)

atomic\_t \* atomic

atomic holding bit flags for each channel to mark as used/unused

**Definition** dma.h:303

[dma\_context::dma\_channels](structdma__context.md#ac6685cf14ca69c7b77160e5031c0a800)

int dma\_channels

number of dma channels

**Definition** dma.h:301

[dma\_status](structdma__status.md)

DMA runtime status structure.

**Definition** dma.h:275

[dma\_status::free](structdma__status.md#a2b481bf13de03e49146eb6a26563776e)

uint32\_t free

Available buffers space, HW specific.

**Definition** dma.h:283

[dma\_status::pending\_length](structdma__status.md#a3a33f92b1d100f988fca2bea0a6deb24)

uint32\_t pending\_length

Pending length to be transferred in bytes, HW specific.

**Definition** dma.h:281

[dma\_status::busy](structdma__status.md#a92ec05d9207caa828064661897f2f31c)

bool busy

Is the current DMA transfer busy or idle.

**Definition** dma.h:277

[dma\_status::total\_copied](structdma__status.md#a9f743c98e6343d55eccc27e528b79b1a)

uint64\_t total\_copied

Total copied, HW specific.

**Definition** dma.h:289

[dma\_status::write\_position](structdma__status.md#aa7288b85f41098e59ad4f96dcea4ccde)

uint32\_t write\_position

Write position in circular DMA buffer, HW specific.

**Definition** dma.h:285

[dma\_status::dir](structdma__status.md#aacfe94ad8e60ea77bca2423bd9bf8409)

enum dma\_channel\_direction dir

Direction for the transfer.

**Definition** dma.h:279

[dma\_status::read\_position](structdma__status.md#afa401acfb26cd26b73e4a52066989847)

uint32\_t read\_position

Read position in circular DMA buffer, HW specific.

**Definition** dma.h:287

[stat](structstat.md)

**Definition** stat.h:57

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dma.h](drivers_2dma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

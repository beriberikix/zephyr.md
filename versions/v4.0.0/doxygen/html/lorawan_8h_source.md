---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/lorawan_8h_source.html
original_path: doxygen/html/lorawan_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lorawan.h

[Go to the documentation of this file.](lorawan_8h.md)

1/\*

2 \* Copyright (c) 2020 Manivannan Sadhasivam <mani@kernel.org>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_LORAWAN\_LORAWAN\_H\_

8#define ZEPHYR\_INCLUDE\_LORAWAN\_LORAWAN\_H\_

9

19

20#include <[zephyr/device.h](device_8h.md)>

21#include <[zephyr/sys/slist.h](slist_8h.md)>

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

[ 30](group__lorawan__api.md#ga88b65799c3f1d98fbce80927218c0837)enum [lorawan\_class](group__lorawan__api.md#ga88b65799c3f1d98fbce80927218c0837) {

[ 31](group__lorawan__api.md#gga88b65799c3f1d98fbce80927218c0837a538e56348e6d5b506e661e3af18aee6c) [LORAWAN\_CLASS\_A](group__lorawan__api.md#gga88b65799c3f1d98fbce80927218c0837a538e56348e6d5b506e661e3af18aee6c) = 0x00,

[ 32](group__lorawan__api.md#gga88b65799c3f1d98fbce80927218c0837a79a9c205ac583051b2e072389491c7cb) [LORAWAN\_CLASS\_B](group__lorawan__api.md#gga88b65799c3f1d98fbce80927218c0837a79a9c205ac583051b2e072389491c7cb) = 0x01,

[ 33](group__lorawan__api.md#gga88b65799c3f1d98fbce80927218c0837ad158a1985688bbe54b20a8a808774547) [LORAWAN\_CLASS\_C](group__lorawan__api.md#gga88b65799c3f1d98fbce80927218c0837ad158a1985688bbe54b20a8a808774547) = 0x02,

34};

35

[ 39](group__lorawan__api.md#ga2bf50442214ecdc717f1a24dc058a338)enum [lorawan\_act\_type](group__lorawan__api.md#ga2bf50442214ecdc717f1a24dc058a338) {

[ 40](group__lorawan__api.md#gga2bf50442214ecdc717f1a24dc058a338a5f262e334bc46278bec491cd022b612a) [LORAWAN\_ACT\_OTAA](group__lorawan__api.md#gga2bf50442214ecdc717f1a24dc058a338a5f262e334bc46278bec491cd022b612a) = 0,

[ 41](group__lorawan__api.md#gga2bf50442214ecdc717f1a24dc058a338a13bb2a28232081844e36308977ec6701) [LORAWAN\_ACT\_ABP](group__lorawan__api.md#gga2bf50442214ecdc717f1a24dc058a338a13bb2a28232081844e36308977ec6701),

42};

43

[ 47](group__lorawan__api.md#ga0635d19612db9009775eae8e527d4897)enum [lorawan\_channels\_mask\_size](group__lorawan__api.md#ga0635d19612db9009775eae8e527d4897) {

[ 48](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a577c304c4c1998916203e9ec7ae6e1be) [LORAWAN\_CHANNELS\_MASK\_SIZE\_AS923](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a577c304c4c1998916203e9ec7ae6e1be) = 1,

[ 49](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a1bc4cacfd02a630226f629ed61f4e1ca) [LORAWAN\_CHANNELS\_MASK\_SIZE\_AU915](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a1bc4cacfd02a630226f629ed61f4e1ca) = 6,

[ 50](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a2bdaecd6f1f853cd370ba89b465a9ee1) [LORAWAN\_CHANNELS\_MASK\_SIZE\_CN470](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a2bdaecd6f1f853cd370ba89b465a9ee1) = 6,

[ 51](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a8f2f25b3ab1167f69aa594a034b27180) [LORAWAN\_CHANNELS\_MASK\_SIZE\_CN779](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a8f2f25b3ab1167f69aa594a034b27180) = 1,

[ 52](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a3b7968012bf2c8fa7adef454fc33124a) [LORAWAN\_CHANNELS\_MASK\_SIZE\_EU433](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a3b7968012bf2c8fa7adef454fc33124a) = 1,

[ 53](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a3bc215c41b7fb5652c6729756b8f979a) [LORAWAN\_CHANNELS\_MASK\_SIZE\_EU868](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a3bc215c41b7fb5652c6729756b8f979a) = 1,

[ 54](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a7443e6adbaaf4f7cb2037d8f3e42d86a) [LORAWAN\_CHANNELS\_MASK\_SIZE\_KR920](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a7443e6adbaaf4f7cb2037d8f3e42d86a) = 1,

[ 55](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a9564d246e39448f478412861a3a87b7e) [LORAWAN\_CHANNELS\_MASK\_SIZE\_IN865](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a9564d246e39448f478412861a3a87b7e) = 1,

[ 56](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a054ebab376354c8a9e6a5f4e9f6f78ee) [LORAWAN\_CHANNELS\_MASK\_SIZE\_US915](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a054ebab376354c8a9e6a5f4e9f6f78ee) = 6,

[ 57](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897aaa05e08a24aded2ada511fd2d1f4cebd) [LORAWAN\_CHANNELS\_MASK\_SIZE\_RU864](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897aaa05e08a24aded2ada511fd2d1f4cebd) = 1,

58};

59

[ 63](group__lorawan__api.md#ga276e66fb8ce88f853d1987686e31fc86)enum [lorawan\_datarate](group__lorawan__api.md#ga276e66fb8ce88f853d1987686e31fc86) {

[ 64](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a4b60b8eb52c07b40cbaaf94a4c56e1f6) [LORAWAN\_DR\_0](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a4b60b8eb52c07b40cbaaf94a4c56e1f6) = 0,

[ 65](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86ade4655b32ca976c317fa9f44ac8b148a) [LORAWAN\_DR\_1](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86ade4655b32ca976c317fa9f44ac8b148a),

[ 66](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a941f8a603aeb54560be7125a55c74159) [LORAWAN\_DR\_2](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a941f8a603aeb54560be7125a55c74159),

[ 67](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a4ac565dbaae0c6ad4e62dc34ca0c013a) [LORAWAN\_DR\_3](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a4ac565dbaae0c6ad4e62dc34ca0c013a),

[ 68](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a6f6cd4ecd247f67cad08ede84649a939) [LORAWAN\_DR\_4](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a6f6cd4ecd247f67cad08ede84649a939),

[ 69](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a08f879f1054ca54e488180b07d7ff952) [LORAWAN\_DR\_5](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a08f879f1054ca54e488180b07d7ff952),

[ 70](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86acc624ccf8a9585889c3685217f56099f) [LORAWAN\_DR\_6](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86acc624ccf8a9585889c3685217f56099f),

[ 71](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86aac8afba95d7187f0829aae7abda894d5) [LORAWAN\_DR\_7](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86aac8afba95d7187f0829aae7abda894d5),

[ 72](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a080b31031f5a2b54d84ed49b133b0a86) [LORAWAN\_DR\_8](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a080b31031f5a2b54d84ed49b133b0a86),

[ 73](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86afbc8d04236410a6107cccfd71ba4bace) [LORAWAN\_DR\_9](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86afbc8d04236410a6107cccfd71ba4bace),

[ 74](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a0a18193e15d268d262d58897d39993b3) [LORAWAN\_DR\_10](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a0a18193e15d268d262d58897d39993b3),

[ 75](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a2a631e746ffc5c4378e39b7a90dd44e2) [LORAWAN\_DR\_11](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a2a631e746ffc5c4378e39b7a90dd44e2),

[ 76](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a0df057cf1505ba94876deaeddd515548) [LORAWAN\_DR\_12](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a0df057cf1505ba94876deaeddd515548),

[ 77](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a18bfd63ae262f992d9d12f8d56cc217e) [LORAWAN\_DR\_13](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a18bfd63ae262f992d9d12f8d56cc217e),

[ 78](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a1ad3be15c2e60d0bb2f3c12faf279efa) [LORAWAN\_DR\_14](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a1ad3be15c2e60d0bb2f3c12faf279efa),

[ 79](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a4738baf87e0cb2e64d9c525e40dd6e0a) [LORAWAN\_DR\_15](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a4738baf87e0cb2e64d9c525e40dd6e0a),

80};

81

[ 85](group__lorawan__api.md#gacb8efaa0761f8761146a0e913dcb627d)enum [lorawan\_region](group__lorawan__api.md#gacb8efaa0761f8761146a0e913dcb627d) {

[ 86](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627da6a1ba05859d575a28095437436c8e6a6) [LORAWAN\_REGION\_AS923](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627da6a1ba05859d575a28095437436c8e6a6),

[ 87](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627da2744fe63701f5a5f23706b6f37672c70) [LORAWAN\_REGION\_AU915](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627da2744fe63701f5a5f23706b6f37672c70),

[ 88](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627da52d67181588c94d2a423040b4b5a1de4) [LORAWAN\_REGION\_CN470](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627da52d67181588c94d2a423040b4b5a1de4),

[ 89](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627dadb106a189c4c647e5e3af89cc753e0d8) [LORAWAN\_REGION\_CN779](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627dadb106a189c4c647e5e3af89cc753e0d8),

[ 90](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627dabcb9529d8f449bcb85a893fdd20f9180) [LORAWAN\_REGION\_EU433](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627dabcb9529d8f449bcb85a893fdd20f9180),

[ 91](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627da404530e5008260260131de051283f7ba) [LORAWAN\_REGION\_EU868](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627da404530e5008260260131de051283f7ba),

[ 92](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627dafae64ea9dd2c2ee7e897fc0f94484da5) [LORAWAN\_REGION\_KR920](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627dafae64ea9dd2c2ee7e897fc0f94484da5),

[ 93](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627da9113b34d94da40149442f432fd97e86c) [LORAWAN\_REGION\_IN865](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627da9113b34d94da40149442f432fd97e86c),

[ 94](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627da70e25dd006efc115617631f64cc34c88) [LORAWAN\_REGION\_US915](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627da70e25dd006efc115617631f64cc34c88),

[ 95](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627dad30a636d45def6889e2b5cbf60f28c0e) [LORAWAN\_REGION\_RU864](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627dad30a636d45def6889e2b5cbf60f28c0e),

96};

97

[ 101](group__lorawan__api.md#ga5d78efba3f8e62ccd6317aed8af4bc54)enum [lorawan\_message\_type](group__lorawan__api.md#ga5d78efba3f8e62ccd6317aed8af4bc54) {

[ 102](group__lorawan__api.md#gga5d78efba3f8e62ccd6317aed8af4bc54a9855d8332363a554db9dde446cc409b7) [LORAWAN\_MSG\_UNCONFIRMED](group__lorawan__api.md#gga5d78efba3f8e62ccd6317aed8af4bc54a9855d8332363a554db9dde446cc409b7) = 0,

[ 103](group__lorawan__api.md#gga5d78efba3f8e62ccd6317aed8af4bc54a40ee76ac8d0b40d06903fc06a7ef1989) [LORAWAN\_MSG\_CONFIRMED](group__lorawan__api.md#gga5d78efba3f8e62ccd6317aed8af4bc54a40ee76ac8d0b40d06903fc06a7ef1989),

104};

105

[ 114](structlorawan__join__otaa.md)struct [lorawan\_join\_otaa](structlorawan__join__otaa.md) {

[ 116](structlorawan__join__otaa.md#aacf3523f615f08fac1993e0bdc354072) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[join\_eui](structlorawan__join__otaa.md#aacf3523f615f08fac1993e0bdc354072);

[ 118](structlorawan__join__otaa.md#af1a96b4fa17ee70ee0e8ba078b02a6bc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[nwk\_key](structlorawan__join__otaa.md#af1a96b4fa17ee70ee0e8ba078b02a6bc);

[ 120](structlorawan__join__otaa.md#a28dd704e28d0bed909c3e85e516c85ea) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[app\_key](structlorawan__join__otaa.md#a28dd704e28d0bed909c3e85e516c85ea);

[ 128](structlorawan__join__otaa.md#ab83167af58040f95072a95fbaed1ff5d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dev\_nonce](structlorawan__join__otaa.md#ab83167af58040f95072a95fbaed1ff5d);

129};

130

[ 134](structlorawan__join__abp.md)struct [lorawan\_join\_abp](structlorawan__join__abp.md) {

[ 136](structlorawan__join__abp.md#ad132826d04b66f145865f9a30ff03fff) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dev\_addr](structlorawan__join__abp.md#ad132826d04b66f145865f9a30ff03fff);

[ 138](structlorawan__join__abp.md#a8019bead1dfdda7a0b05f35f128edca5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[app\_skey](structlorawan__join__abp.md#a8019bead1dfdda7a0b05f35f128edca5);

[ 140](structlorawan__join__abp.md#aa389fec6799b12e750d57aaf0b34e6b0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[nwk\_skey](structlorawan__join__abp.md#aa389fec6799b12e750d57aaf0b34e6b0);

[ 142](structlorawan__join__abp.md#a7a409fa2f3761c49085818768a62d216) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[app\_eui](structlorawan__join__abp.md#a7a409fa2f3761c49085818768a62d216);

143};

144

[ 148](structlorawan__join__config.md)struct [lorawan\_join\_config](structlorawan__join__config.md) {

150 union {

[ 151](structlorawan__join__config.md#a7e2db9310308b59f652d72a3d7b3f7ff) struct [lorawan\_join\_otaa](structlorawan__join__otaa.md) [otaa](structlorawan__join__config.md#a7e2db9310308b59f652d72a3d7b3f7ff);

[ 152](structlorawan__join__config.md#a0b44703df9ebe466ccf1d7744138daee) struct [lorawan\_join\_abp](structlorawan__join__abp.md) [abp](structlorawan__join__config.md#a0b44703df9ebe466ccf1d7744138daee);

153 };

154

[ 156](structlorawan__join__config.md#af5c973ed774255858b2219f737a3fe0a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[dev\_eui](structlorawan__join__config.md#af5c973ed774255858b2219f737a3fe0a);

157

[ 159](structlorawan__join__config.md#a9dbe39641f878e4c997a16711fdb5585) enum [lorawan\_act\_type](group__lorawan__api.md#ga2bf50442214ecdc717f1a24dc058a338) [mode](structlorawan__join__config.md#a9dbe39641f878e4c997a16711fdb5585);

160};

161

[ 163](group__lorawan__api.md#ga83dbf2575eaae85f1837567e9fb729a4)#define LW\_RECV\_PORT\_ANY UINT16\_MAX

164

[ 168](structlorawan__downlink__cb.md)struct [lorawan\_downlink\_cb](structlorawan__downlink__cb.md) {

[ 176](structlorawan__downlink__cb.md#a0479e13faf06b99cf9023ebed8022131) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [port](structlorawan__downlink__cb.md#a0479e13faf06b99cf9023ebed8022131);

[ 190](structlorawan__downlink__cb.md#adee407633f1c6fa35178769cb9355178) void (\*[cb](structlorawan__downlink__cb.md#adee407633f1c6fa35178769cb9355178))([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [port](structlorawan__downlink__cb.md#a0479e13faf06b99cf9023ebed8022131), bool data\_pending,

191 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) rssi, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) snr,

192 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data);

[ 194](structlorawan__downlink__cb.md#ad54df4a4ab38003d59f82b19fb16f5fd) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structlorawan__downlink__cb.md#ad54df4a4ab38003d59f82b19fb16f5fd);

195};

196

[ 204](group__lorawan__api.md#ga17a7a2e1dbfa19b9f7e18a81be5514dd)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) (\*[lorawan\_battery\_level\_cb\_t](group__lorawan__api.md#ga17a7a2e1dbfa19b9f7e18a81be5514dd))(void);

205

[ 211](group__lorawan__api.md#ga87a8d911f1c825bcf8c77ada568f3ed4)typedef void (\*[lorawan\_dr\_changed\_cb\_t](group__lorawan__api.md#ga87a8d911f1c825bcf8c77ada568f3ed4))(enum [lorawan\_datarate](group__lorawan__api.md#ga276e66fb8ce88f853d1987686e31fc86) dr);

212

[ 223](group__lorawan__api.md#ga9771704a8bcab778dd30653a0fbdeb2f)void [lorawan\_register\_battery\_level\_callback](group__lorawan__api.md#ga9771704a8bcab778dd30653a0fbdeb2f)([lorawan\_battery\_level\_cb\_t](group__lorawan__api.md#ga17a7a2e1dbfa19b9f7e18a81be5514dd) cb);

224

[ 230](group__lorawan__api.md#gab91f31477cd44e10692ca9d56d137ae2)void [lorawan\_register\_downlink\_callback](group__lorawan__api.md#gab91f31477cd44e10692ca9d56d137ae2)(struct [lorawan\_downlink\_cb](structlorawan__downlink__cb.md) \*cb);

231

[ 240](group__lorawan__api.md#ga505e8d27bc7bc029feb93bbe4982d329)void [lorawan\_register\_dr\_changed\_callback](group__lorawan__api.md#ga505e8d27bc7bc029feb93bbe4982d329)([lorawan\_dr\_changed\_cb\_t](group__lorawan__api.md#ga87a8d911f1c825bcf8c77ada568f3ed4) cb);

241

[ 251](group__lorawan__api.md#ga5b2c7543c45801c9d0d7f46546771f17)int [lorawan\_join](group__lorawan__api.md#ga5b2c7543c45801c9d0d7f46546771f17)(const struct [lorawan\_join\_config](structlorawan__join__config.md) \*config);

252

[ 260](group__lorawan__api.md#ga640d93930e09327ee87563597f919725)int [lorawan\_start](group__lorawan__api.md#ga640d93930e09327ee87563597f919725)(void);

261

[ 278](group__lorawan__api.md#ga23758c3225e3ebf62bbe91b7589b67d7)int [lorawan\_send](group__lorawan__api.md#ga23758c3225e3ebf62bbe91b7589b67d7)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) port, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len, enum [lorawan\_message\_type](group__lorawan__api.md#ga5d78efba3f8e62ccd6317aed8af4bc54) type);

279

[ 290](group__lorawan__api.md#gab9768bad8d0c18410f6b8e946e89cbbe)int [lorawan\_set\_class](group__lorawan__api.md#gab9768bad8d0c18410f6b8e946e89cbbe)(enum [lorawan\_class](group__lorawan__api.md#ga88b65799c3f1d98fbce80927218c0837) dev\_class);

291

[ 299](group__lorawan__api.md#ga14f9cb6a11c585f9ac4e9986735a82c3)int [lorawan\_set\_conf\_msg\_tries](group__lorawan__api.md#ga14f9cb6a11c585f9ac4e9986735a82c3)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tries);

300

[ 312](group__lorawan__api.md#ga432929bd5911e04e57ef178b65e1beaa)void [lorawan\_enable\_adr](group__lorawan__api.md#ga432929bd5911e04e57ef178b65e1beaa)(bool enable);

313

[ 327](group__lorawan__api.md#ga243c3200693ae9c81dea238068afc7dd)int [lorawan\_set\_channels\_mask](group__lorawan__api.md#ga243c3200693ae9c81dea238068afc7dd)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*channels\_mask, size\_t channels\_mask\_size);

328

[ 338](group__lorawan__api.md#gaaa70ba5aa545b59233bc906948a4030d)int [lorawan\_set\_datarate](group__lorawan__api.md#gaaa70ba5aa545b59233bc906948a4030d)(enum [lorawan\_datarate](group__lorawan__api.md#ga276e66fb8ce88f853d1987686e31fc86) dr);

339

[ 348](group__lorawan__api.md#ga6d1b45c5543473ff4fbcef473a8e0e35)enum [lorawan\_datarate](group__lorawan__api.md#ga276e66fb8ce88f853d1987686e31fc86) [lorawan\_get\_min\_datarate](group__lorawan__api.md#ga6d1b45c5543473ff4fbcef473a8e0e35)(void);

349

[ 360](group__lorawan__api.md#ga94e3c282537618efae65e8ada1f88e81)void [lorawan\_get\_payload\_sizes](group__lorawan__api.md#ga94e3c282537618efae65e8ada1f88e81)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*max\_next\_payload\_size,

361 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*max\_payload\_size);

362

[ 373](group__lorawan__api.md#gaaf60e8b09d6f8d3a89aa2089c137fd3f)int [lorawan\_set\_region](group__lorawan__api.md#gaaf60e8b09d6f8d3a89aa2089c137fd3f)(enum [lorawan\_region](group__lorawan__api.md#gacb8efaa0761f8761146a0e913dcb627d) region);

374

375#ifdef CONFIG\_LORAWAN\_APP\_CLOCK\_SYNC

376

389int lorawan\_clock\_sync\_run(void);

390

403int lorawan\_clock\_sync\_get([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*gps\_time);

404

405#endif /\* CONFIG\_LORAWAN\_APP\_CLOCK\_SYNC \*/

406

407#ifdef CONFIG\_LORAWAN\_FRAG\_TRANSPORT

408

421int lorawan\_frag\_transport\_run(void (\*transport\_finished\_cb)(void));

422

423#endif /\* CONFIG\_LORAWAN\_FRAG\_TRANSPORT \*/

424

425#ifdef \_\_cplusplus

426}

427#endif

428

432

433#endif /\* ZEPHYR\_INCLUDE\_LORAWAN\_LORAWAN\_H\_ \*/

[device.h](device_8h.md)

[lorawan\_channels\_mask\_size](group__lorawan__api.md#ga0635d19612db9009775eae8e527d4897)

lorawan\_channels\_mask\_size

LoRaWAN channels mask sizes.

**Definition** lorawan.h:47

[lorawan\_set\_conf\_msg\_tries](group__lorawan__api.md#ga14f9cb6a11c585f9ac4e9986735a82c3)

int lorawan\_set\_conf\_msg\_tries(uint8\_t tries)

Set the number of tries used for transmissions.

[lorawan\_battery\_level\_cb\_t](group__lorawan__api.md#ga17a7a2e1dbfa19b9f7e18a81be5514dd)

uint8\_t(\* lorawan\_battery\_level\_cb\_t)(void)

Defines the battery level callback handler function signature.

**Definition** lorawan.h:204

[lorawan\_send](group__lorawan__api.md#ga23758c3225e3ebf62bbe91b7589b67d7)

int lorawan\_send(uint8\_t port, uint8\_t \*data, uint8\_t len, enum lorawan\_message\_type type)

Send data to the LoRaWAN network.

[lorawan\_set\_channels\_mask](group__lorawan__api.md#ga243c3200693ae9c81dea238068afc7dd)

int lorawan\_set\_channels\_mask(uint16\_t \*channels\_mask, size\_t channels\_mask\_size)

Set the channels mask.

[lorawan\_datarate](group__lorawan__api.md#ga276e66fb8ce88f853d1987686e31fc86)

lorawan\_datarate

LoRaWAN datarate types.

**Definition** lorawan.h:63

[lorawan\_act\_type](group__lorawan__api.md#ga2bf50442214ecdc717f1a24dc058a338)

lorawan\_act\_type

LoRaWAN activation types.

**Definition** lorawan.h:39

[lorawan\_enable\_adr](group__lorawan__api.md#ga432929bd5911e04e57ef178b65e1beaa)

void lorawan\_enable\_adr(bool enable)

Enable Adaptive Data Rate (ADR).

[lorawan\_register\_dr\_changed\_callback](group__lorawan__api.md#ga505e8d27bc7bc029feb93bbe4982d329)

void lorawan\_register\_dr\_changed\_callback(lorawan\_dr\_changed\_cb\_t cb)

Register a callback to be called when the datarate changes.

[lorawan\_join](group__lorawan__api.md#ga5b2c7543c45801c9d0d7f46546771f17)

int lorawan\_join(const struct lorawan\_join\_config \*config)

Join the LoRaWAN network.

[lorawan\_message\_type](group__lorawan__api.md#ga5d78efba3f8e62ccd6317aed8af4bc54)

lorawan\_message\_type

LoRaWAN message types.

**Definition** lorawan.h:101

[lorawan\_start](group__lorawan__api.md#ga640d93930e09327ee87563597f919725)

int lorawan\_start(void)

Start the LoRaWAN stack.

[lorawan\_get\_min\_datarate](group__lorawan__api.md#ga6d1b45c5543473ff4fbcef473a8e0e35)

enum lorawan\_datarate lorawan\_get\_min\_datarate(void)

Get the minimum possible datarate.

[lorawan\_dr\_changed\_cb\_t](group__lorawan__api.md#ga87a8d911f1c825bcf8c77ada568f3ed4)

void(\* lorawan\_dr\_changed\_cb\_t)(enum lorawan\_datarate dr)

Defines the datarate changed callback handler function signature.

**Definition** lorawan.h:211

[lorawan\_class](group__lorawan__api.md#ga88b65799c3f1d98fbce80927218c0837)

lorawan\_class

LoRaWAN class types.

**Definition** lorawan.h:30

[lorawan\_get\_payload\_sizes](group__lorawan__api.md#ga94e3c282537618efae65e8ada1f88e81)

void lorawan\_get\_payload\_sizes(uint8\_t \*max\_next\_payload\_size, uint8\_t \*max\_payload\_size)

Get the current payload sizes.

[lorawan\_register\_battery\_level\_callback](group__lorawan__api.md#ga9771704a8bcab778dd30653a0fbdeb2f)

void lorawan\_register\_battery\_level\_callback(lorawan\_battery\_level\_cb\_t cb)

Register a battery level callback function.

[lorawan\_set\_datarate](group__lorawan__api.md#gaaa70ba5aa545b59233bc906948a4030d)

int lorawan\_set\_datarate(enum lorawan\_datarate dr)

Set the default data rate.

[lorawan\_set\_region](group__lorawan__api.md#gaaf60e8b09d6f8d3a89aa2089c137fd3f)

int lorawan\_set\_region(enum lorawan\_region region)

Set the region and frequency to be used.

[lorawan\_register\_downlink\_callback](group__lorawan__api.md#gab91f31477cd44e10692ca9d56d137ae2)

void lorawan\_register\_downlink\_callback(struct lorawan\_downlink\_cb \*cb)

Register a callback to be run on downlink packets.

[lorawan\_set\_class](group__lorawan__api.md#gab9768bad8d0c18410f6b8e946e89cbbe)

int lorawan\_set\_class(enum lorawan\_class dev\_class)

Set the current device class.

[lorawan\_region](group__lorawan__api.md#gacb8efaa0761f8761146a0e913dcb627d)

lorawan\_region

LoRaWAN region types.

**Definition** lorawan.h:85

[LORAWAN\_CHANNELS\_MASK\_SIZE\_US915](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a054ebab376354c8a9e6a5f4e9f6f78ee)

@ LORAWAN\_CHANNELS\_MASK\_SIZE\_US915

Region US915 mask size.

**Definition** lorawan.h:56

[LORAWAN\_CHANNELS\_MASK\_SIZE\_AU915](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a1bc4cacfd02a630226f629ed61f4e1ca)

@ LORAWAN\_CHANNELS\_MASK\_SIZE\_AU915

Region AU915 mask size.

**Definition** lorawan.h:49

[LORAWAN\_CHANNELS\_MASK\_SIZE\_CN470](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a2bdaecd6f1f853cd370ba89b465a9ee1)

@ LORAWAN\_CHANNELS\_MASK\_SIZE\_CN470

Region CN470 mask size.

**Definition** lorawan.h:50

[LORAWAN\_CHANNELS\_MASK\_SIZE\_EU433](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a3b7968012bf2c8fa7adef454fc33124a)

@ LORAWAN\_CHANNELS\_MASK\_SIZE\_EU433

Region EU433 mask size.

**Definition** lorawan.h:52

[LORAWAN\_CHANNELS\_MASK\_SIZE\_EU868](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a3bc215c41b7fb5652c6729756b8f979a)

@ LORAWAN\_CHANNELS\_MASK\_SIZE\_EU868

Region EU868 mask size.

**Definition** lorawan.h:53

[LORAWAN\_CHANNELS\_MASK\_SIZE\_AS923](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a577c304c4c1998916203e9ec7ae6e1be)

@ LORAWAN\_CHANNELS\_MASK\_SIZE\_AS923

Region AS923 mask size.

**Definition** lorawan.h:48

[LORAWAN\_CHANNELS\_MASK\_SIZE\_KR920](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a7443e6adbaaf4f7cb2037d8f3e42d86a)

@ LORAWAN\_CHANNELS\_MASK\_SIZE\_KR920

Region KR920 mask size.

**Definition** lorawan.h:54

[LORAWAN\_CHANNELS\_MASK\_SIZE\_CN779](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a8f2f25b3ab1167f69aa594a034b27180)

@ LORAWAN\_CHANNELS\_MASK\_SIZE\_CN779

Region CN779 mask size.

**Definition** lorawan.h:51

[LORAWAN\_CHANNELS\_MASK\_SIZE\_IN865](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a9564d246e39448f478412861a3a87b7e)

@ LORAWAN\_CHANNELS\_MASK\_SIZE\_IN865

Region IN865 mask size.

**Definition** lorawan.h:55

[LORAWAN\_CHANNELS\_MASK\_SIZE\_RU864](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897aaa05e08a24aded2ada511fd2d1f4cebd)

@ LORAWAN\_CHANNELS\_MASK\_SIZE\_RU864

Region RU864 mask size.

**Definition** lorawan.h:57

[LORAWAN\_DR\_8](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a080b31031f5a2b54d84ed49b133b0a86)

@ LORAWAN\_DR\_8

DR8 data rate.

**Definition** lorawan.h:72

[LORAWAN\_DR\_5](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a08f879f1054ca54e488180b07d7ff952)

@ LORAWAN\_DR\_5

DR5 data rate.

**Definition** lorawan.h:69

[LORAWAN\_DR\_10](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a0a18193e15d268d262d58897d39993b3)

@ LORAWAN\_DR\_10

DR10 data rate.

**Definition** lorawan.h:74

[LORAWAN\_DR\_12](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a0df057cf1505ba94876deaeddd515548)

@ LORAWAN\_DR\_12

DR12 data rate.

**Definition** lorawan.h:76

[LORAWAN\_DR\_13](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a18bfd63ae262f992d9d12f8d56cc217e)

@ LORAWAN\_DR\_13

DR13 data rate.

**Definition** lorawan.h:77

[LORAWAN\_DR\_14](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a1ad3be15c2e60d0bb2f3c12faf279efa)

@ LORAWAN\_DR\_14

DR14 data rate.

**Definition** lorawan.h:78

[LORAWAN\_DR\_11](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a2a631e746ffc5c4378e39b7a90dd44e2)

@ LORAWAN\_DR\_11

DR11 data rate.

**Definition** lorawan.h:75

[LORAWAN\_DR\_15](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a4738baf87e0cb2e64d9c525e40dd6e0a)

@ LORAWAN\_DR\_15

DR15 data rate.

**Definition** lorawan.h:79

[LORAWAN\_DR\_3](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a4ac565dbaae0c6ad4e62dc34ca0c013a)

@ LORAWAN\_DR\_3

DR3 data rate.

**Definition** lorawan.h:67

[LORAWAN\_DR\_0](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a4b60b8eb52c07b40cbaaf94a4c56e1f6)

@ LORAWAN\_DR\_0

DR0 data rate.

**Definition** lorawan.h:64

[LORAWAN\_DR\_4](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a6f6cd4ecd247f67cad08ede84649a939)

@ LORAWAN\_DR\_4

DR4 data rate.

**Definition** lorawan.h:68

[LORAWAN\_DR\_2](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a941f8a603aeb54560be7125a55c74159)

@ LORAWAN\_DR\_2

DR2 data rate.

**Definition** lorawan.h:66

[LORAWAN\_DR\_7](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86aac8afba95d7187f0829aae7abda894d5)

@ LORAWAN\_DR\_7

DR7 data rate.

**Definition** lorawan.h:71

[LORAWAN\_DR\_6](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86acc624ccf8a9585889c3685217f56099f)

@ LORAWAN\_DR\_6

DR6 data rate.

**Definition** lorawan.h:70

[LORAWAN\_DR\_1](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86ade4655b32ca976c317fa9f44ac8b148a)

@ LORAWAN\_DR\_1

DR1 data rate.

**Definition** lorawan.h:65

[LORAWAN\_DR\_9](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86afbc8d04236410a6107cccfd71ba4bace)

@ LORAWAN\_DR\_9

DR9 data rate.

**Definition** lorawan.h:73

[LORAWAN\_ACT\_ABP](group__lorawan__api.md#gga2bf50442214ecdc717f1a24dc058a338a13bb2a28232081844e36308977ec6701)

@ LORAWAN\_ACT\_ABP

Activation by Personalization (ABP).

**Definition** lorawan.h:41

[LORAWAN\_ACT\_OTAA](group__lorawan__api.md#gga2bf50442214ecdc717f1a24dc058a338a5f262e334bc46278bec491cd022b612a)

@ LORAWAN\_ACT\_OTAA

Over-the-Air Activation (OTAA).

**Definition** lorawan.h:40

[LORAWAN\_MSG\_CONFIRMED](group__lorawan__api.md#gga5d78efba3f8e62ccd6317aed8af4bc54a40ee76ac8d0b40d06903fc06a7ef1989)

@ LORAWAN\_MSG\_CONFIRMED

Confirmed message.

**Definition** lorawan.h:103

[LORAWAN\_MSG\_UNCONFIRMED](group__lorawan__api.md#gga5d78efba3f8e62ccd6317aed8af4bc54a9855d8332363a554db9dde446cc409b7)

@ LORAWAN\_MSG\_UNCONFIRMED

Unconfirmed message.

**Definition** lorawan.h:102

[LORAWAN\_CLASS\_A](group__lorawan__api.md#gga88b65799c3f1d98fbce80927218c0837a538e56348e6d5b506e661e3af18aee6c)

@ LORAWAN\_CLASS\_A

Class A device.

**Definition** lorawan.h:31

[LORAWAN\_CLASS\_B](group__lorawan__api.md#gga88b65799c3f1d98fbce80927218c0837a79a9c205ac583051b2e072389491c7cb)

@ LORAWAN\_CLASS\_B

Class B device.

**Definition** lorawan.h:32

[LORAWAN\_CLASS\_C](group__lorawan__api.md#gga88b65799c3f1d98fbce80927218c0837ad158a1985688bbe54b20a8a808774547)

@ LORAWAN\_CLASS\_C

Class C device.

**Definition** lorawan.h:33

[LORAWAN\_REGION\_AU915](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627da2744fe63701f5a5f23706b6f37672c70)

@ LORAWAN\_REGION\_AU915

Australia 915 MHz frequency band.

**Definition** lorawan.h:87

[LORAWAN\_REGION\_EU868](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627da404530e5008260260131de051283f7ba)

@ LORAWAN\_REGION\_EU868

Europe 868 MHz frequency band.

**Definition** lorawan.h:91

[LORAWAN\_REGION\_CN470](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627da52d67181588c94d2a423040b4b5a1de4)

@ LORAWAN\_REGION\_CN470

China 470 MHz frequency band.

**Definition** lorawan.h:88

[LORAWAN\_REGION\_AS923](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627da6a1ba05859d575a28095437436c8e6a6)

@ LORAWAN\_REGION\_AS923

Asia 923 MHz frequency band.

**Definition** lorawan.h:86

[LORAWAN\_REGION\_US915](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627da70e25dd006efc115617631f64cc34c88)

@ LORAWAN\_REGION\_US915

United States 915 MHz frequency band.

**Definition** lorawan.h:94

[LORAWAN\_REGION\_IN865](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627da9113b34d94da40149442f432fd97e86c)

@ LORAWAN\_REGION\_IN865

India 865 MHz frequency band.

**Definition** lorawan.h:93

[LORAWAN\_REGION\_EU433](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627dabcb9529d8f449bcb85a893fdd20f9180)

@ LORAWAN\_REGION\_EU433

Europe 433 MHz frequency band.

**Definition** lorawan.h:90

[LORAWAN\_REGION\_RU864](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627dad30a636d45def6889e2b5cbf60f28c0e)

@ LORAWAN\_REGION\_RU864

Russia 864 MHz frequency band.

**Definition** lorawan.h:95

[LORAWAN\_REGION\_CN779](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627dadb106a189c4c647e5e3af89cc753e0d8)

@ LORAWAN\_REGION\_CN779

China 779 MHz frequency band.

**Definition** lorawan.h:89

[LORAWAN\_REGION\_KR920](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627dafae64ea9dd2c2ee7e897fc0f94484da5)

@ LORAWAN\_REGION\_KR920

South Korea 920 MHz frequency band.

**Definition** lorawan.h:92

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[slist.h](slist_8h.md)

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

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[lorawan\_downlink\_cb](structlorawan__downlink__cb.md)

LoRaWAN downlink callback parameters.

**Definition** lorawan.h:168

[lorawan\_downlink\_cb::port](structlorawan__downlink__cb.md#a0479e13faf06b99cf9023ebed8022131)

uint16\_t port

Port to handle messages for.

**Definition** lorawan.h:176

[lorawan\_downlink\_cb::node](structlorawan__downlink__cb.md#ad54df4a4ab38003d59f82b19fb16f5fd)

sys\_snode\_t node

Node for callback list.

**Definition** lorawan.h:194

[lorawan\_downlink\_cb::cb](structlorawan__downlink__cb.md#adee407633f1c6fa35178769cb9355178)

void(\* cb)(uint8\_t port, bool data\_pending, int16\_t rssi, int8\_t snr, uint8\_t len, const uint8\_t \*data)

Callback function to run on downlink data.

**Definition** lorawan.h:190

[lorawan\_join\_abp](structlorawan__join__abp.md)

LoRaWAN join parameters for activation by personalization (ABP).

**Definition** lorawan.h:134

[lorawan\_join\_abp::app\_eui](structlorawan__join__abp.md#a7a409fa2f3761c49085818768a62d216)

uint8\_t \* app\_eui

Application EUI.

**Definition** lorawan.h:142

[lorawan\_join\_abp::app\_skey](structlorawan__join__abp.md#a8019bead1dfdda7a0b05f35f128edca5)

uint8\_t \* app\_skey

Application session key.

**Definition** lorawan.h:138

[lorawan\_join\_abp::nwk\_skey](structlorawan__join__abp.md#aa389fec6799b12e750d57aaf0b34e6b0)

uint8\_t \* nwk\_skey

Network session key.

**Definition** lorawan.h:140

[lorawan\_join\_abp::dev\_addr](structlorawan__join__abp.md#ad132826d04b66f145865f9a30ff03fff)

uint32\_t dev\_addr

Device address on the network.

**Definition** lorawan.h:136

[lorawan\_join\_config](structlorawan__join__config.md)

LoRaWAN join parameters.

**Definition** lorawan.h:148

[lorawan\_join\_config::abp](structlorawan__join__config.md#a0b44703df9ebe466ccf1d7744138daee)

struct lorawan\_join\_abp abp

ABP join parameters.

**Definition** lorawan.h:152

[lorawan\_join\_config::otaa](structlorawan__join__config.md#a7e2db9310308b59f652d72a3d7b3f7ff)

struct lorawan\_join\_otaa otaa

OTAA join parameters.

**Definition** lorawan.h:151

[lorawan\_join\_config::mode](structlorawan__join__config.md#a9dbe39641f878e4c997a16711fdb5585)

enum lorawan\_act\_type mode

Activation mode.

**Definition** lorawan.h:159

[lorawan\_join\_config::dev\_eui](structlorawan__join__config.md#af5c973ed774255858b2219f737a3fe0a)

uint8\_t \* dev\_eui

Device EUI.

**Definition** lorawan.h:156

[lorawan\_join\_otaa](structlorawan__join__otaa.md)

LoRaWAN join parameters for over-the-Air activation (OTAA).

**Definition** lorawan.h:114

[lorawan\_join\_otaa::app\_key](structlorawan__join__otaa.md#a28dd704e28d0bed909c3e85e516c85ea)

uint8\_t \* app\_key

Application Key.

**Definition** lorawan.h:120

[lorawan\_join\_otaa::join\_eui](structlorawan__join__otaa.md#aacf3523f615f08fac1993e0bdc354072)

uint8\_t \* join\_eui

Join EUI.

**Definition** lorawan.h:116

[lorawan\_join\_otaa::dev\_nonce](structlorawan__join__otaa.md#ab83167af58040f95072a95fbaed1ff5d)

uint16\_t dev\_nonce

Device Nonce.

**Definition** lorawan.h:128

[lorawan\_join\_otaa::nwk\_key](structlorawan__join__otaa.md#af1a96b4fa17ee70ee0e8ba078b02a6bc)

uint8\_t \* nwk\_key

Network Key.

**Definition** lorawan.h:118

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [lorawan](dir_025fd8c7c9e823719407606758d0c447.md)
- [lorawan.h](lorawan_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

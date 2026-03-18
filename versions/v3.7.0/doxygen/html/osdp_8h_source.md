---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/osdp_8h_source.html
original_path: doxygen/html/osdp_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

osdp.h

[Go to the documentation of this file.](osdp_8h.md)

1/\*

2 \* Copyright (c) 2020 Siddharth Chandrasekaran <siddharth@embedjournal.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef \_OSDP\_H\_

13#define \_OSDP\_H\_

14

15#include <[zephyr/kernel.h](kernel_8h.md)>

16#include <[stdint.h](stdint_8h.md)>

17

18#include <[zephyr/sys/slist.h](slist_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

[ 24](osdp_8h.md#acfd9e52e3ca23e6ef3d1cb55a0fa5714)#define OSDP\_CMD\_TEXT\_MAX\_LEN 32

[ 25](osdp_8h.md#a04a0aa00cbe34e1723be1a4763f63e94)#define OSDP\_CMD\_KEYSET\_KEY\_MAX\_LEN 32

[ 26](osdp_8h.md#af531800483155468768b89d20c3377d6)#define OSDP\_EVENT\_MAX\_DATALEN 64

27

[ 31](structosdp__cmd__output.md)struct [osdp\_cmd\_output](structosdp__cmd__output.md) {

[ 37](structosdp__cmd__output.md#af5e1d55c987dd82ed4959f251a811846) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [output\_no](structosdp__cmd__output.md#af5e1d55c987dd82ed4959f251a811846);

[ 49](structosdp__cmd__output.md#a1037244ed5f7c78eab51d6c08130b5d0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [control\_code](structosdp__cmd__output.md#a1037244ed5f7c78eab51d6c08130b5d0);

[ 53](structosdp__cmd__output.md#a4cd89d5c683b31d0e8eaf007443703a6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timer\_count](structosdp__cmd__output.md#a4cd89d5c683b31d0e8eaf007443703a6);

54};

55

[ 59](osdp_8h.md#a97ee0d8eb19e4e37ac89b2b6d338b84e)enum [osdp\_led\_color\_e](osdp_8h.md#a97ee0d8eb19e4e37ac89b2b6d338b84e) {

[ 60](osdp_8h.md#a97ee0d8eb19e4e37ac89b2b6d338b84ea72a45fa8f0b48a165c5507e456b4b1e7) [OSDP\_LED\_COLOR\_NONE](osdp_8h.md#a97ee0d8eb19e4e37ac89b2b6d338b84ea72a45fa8f0b48a165c5507e456b4b1e7),

[ 61](osdp_8h.md#a97ee0d8eb19e4e37ac89b2b6d338b84ea6832c2b25f228213022d0dbb5f5e1584) [OSDP\_LED\_COLOR\_RED](osdp_8h.md#a97ee0d8eb19e4e37ac89b2b6d338b84ea6832c2b25f228213022d0dbb5f5e1584),

[ 62](osdp_8h.md#a97ee0d8eb19e4e37ac89b2b6d338b84eac4024077b8804580d2480708e0b14ae4) [OSDP\_LED\_COLOR\_GREEN](osdp_8h.md#a97ee0d8eb19e4e37ac89b2b6d338b84eac4024077b8804580d2480708e0b14ae4),

[ 63](osdp_8h.md#a97ee0d8eb19e4e37ac89b2b6d338b84eadd22879185802d0705d7195e1d9bd42c) [OSDP\_LED\_COLOR\_AMBER](osdp_8h.md#a97ee0d8eb19e4e37ac89b2b6d338b84eadd22879185802d0705d7195e1d9bd42c),

[ 64](osdp_8h.md#a97ee0d8eb19e4e37ac89b2b6d338b84eadc9d0a41de52b0aa20e428e79e7c6b66) [OSDP\_LED\_COLOR\_BLUE](osdp_8h.md#a97ee0d8eb19e4e37ac89b2b6d338b84eadc9d0a41de52b0aa20e428e79e7c6b66),

[ 65](osdp_8h.md#a97ee0d8eb19e4e37ac89b2b6d338b84ea0a80ccbb26b42ebc2cca602c7be3117a) [OSDP\_LED\_COLOR\_SENTINEL](osdp_8h.md#a97ee0d8eb19e4e37ac89b2b6d338b84ea0a80ccbb26b42ebc2cca602c7be3117a)

66};

67

[ 71](structosdp__cmd__led__params.md)struct [osdp\_cmd\_led\_params](structosdp__cmd__led__params.md) {

[ 83](structosdp__cmd__led__params.md#ae95e3b87bbccd7d9897fef329001ce39) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [control\_code](structosdp__cmd__led__params.md#ae95e3b87bbccd7d9897fef329001ce39);

[ 87](structosdp__cmd__led__params.md#adde9dfdd167d9dfc122b56cf5e47b10f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [on\_count](structosdp__cmd__led__params.md#adde9dfdd167d9dfc122b56cf5e47b10f);

[ 91](structosdp__cmd__led__params.md#a278ff380c2ab7d9c83b55aa49b3137cb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [off\_count](structosdp__cmd__led__params.md#a278ff380c2ab7d9c83b55aa49b3137cb);

[ 95](structosdp__cmd__led__params.md#a80b47a4c55494d7062c4a83fd81b0910) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [on\_color](structosdp__cmd__led__params.md#a80b47a4c55494d7062c4a83fd81b0910);

[ 99](structosdp__cmd__led__params.md#ac6f1c1269697fcab96b6f68d62381ded) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [off\_color](structosdp__cmd__led__params.md#ac6f1c1269697fcab96b6f68d62381ded);

[ 103](structosdp__cmd__led__params.md#a002de25cd5070cb96e90ccd0d2091216) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timer\_count](structosdp__cmd__led__params.md#a002de25cd5070cb96e90ccd0d2091216);

104};

105

[ 109](structosdp__cmd__led.md)struct [osdp\_cmd\_led](structosdp__cmd__led.md) {

[ 113](structosdp__cmd__led.md#afe5e061d91fda9f008b5f8e5441df467) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reader](structosdp__cmd__led.md#afe5e061d91fda9f008b5f8e5441df467);

[ 117](structosdp__cmd__led.md#ae4ff10389198d00047ffa2a7ec7d15ac) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [led\_number](structosdp__cmd__led.md#ae4ff10389198d00047ffa2a7ec7d15ac);

[ 121](structosdp__cmd__led.md#a2130237d1b79ee36c5f5087cdec7acfb) struct [osdp\_cmd\_led\_params](structosdp__cmd__led__params.md) [temporary](structosdp__cmd__led.md#a2130237d1b79ee36c5f5087cdec7acfb);

[ 125](structosdp__cmd__led.md#a033fd34a88b03d22a088bd7d2676efb5) struct [osdp\_cmd\_led\_params](structosdp__cmd__led__params.md) [permanent](structosdp__cmd__led.md#a033fd34a88b03d22a088bd7d2676efb5);

126};

127

[ 131](structosdp__cmd__buzzer.md)struct [osdp\_cmd\_buzzer](structosdp__cmd__buzzer.md) {

[ 135](structosdp__cmd__buzzer.md#a0e97e1e33eac4f25e5a05586f8135ab3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reader](structosdp__cmd__buzzer.md#a0e97e1e33eac4f25e5a05586f8135ab3);

[ 143](structosdp__cmd__buzzer.md#a16d0f385264e247d942367a6a13a77af) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [control\_code](structosdp__cmd__buzzer.md#a16d0f385264e247d942367a6a13a77af);

[ 147](structosdp__cmd__buzzer.md#a9082cf0dd2e3e9d31d95051f2952d611) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [on\_count](structosdp__cmd__buzzer.md#a9082cf0dd2e3e9d31d95051f2952d611);

[ 151](structosdp__cmd__buzzer.md#ac83cdb57418fc28f11c686e79e811492) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [off\_count](structosdp__cmd__buzzer.md#ac83cdb57418fc28f11c686e79e811492);

[ 155](structosdp__cmd__buzzer.md#a0ea92ffb8ed7527e0373c0530edfb61d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rep\_count](structosdp__cmd__buzzer.md#a0ea92ffb8ed7527e0373c0530edfb61d);

156};

157

[ 161](structosdp__cmd__text.md)struct [osdp\_cmd\_text](structosdp__cmd__text.md) {

[ 165](structosdp__cmd__text.md#a3fa3d0780aa98542a270f6bdb6f49737) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reader](structosdp__cmd__text.md#a3fa3d0780aa98542a270f6bdb6f49737);

[ 173](structosdp__cmd__text.md#a46fe3f66e01229e763a6f06bd8bdfab8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [control\_code](structosdp__cmd__text.md#a46fe3f66e01229e763a6f06bd8bdfab8);

[ 177](structosdp__cmd__text.md#acde9abcb023eb77845af8ea0935e63fa) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [temp\_time](structosdp__cmd__text.md#acde9abcb023eb77845af8ea0935e63fa);

[ 181](structosdp__cmd__text.md#a16f11f35eacb2876b09d148349b7ed3c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [offset\_row](structosdp__cmd__text.md#a16f11f35eacb2876b09d148349b7ed3c);

[ 185](structosdp__cmd__text.md#a5e7b4c03b1649d8edbf53932ee90f7b3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [offset\_col](structosdp__cmd__text.md#a5e7b4c03b1649d8edbf53932ee90f7b3);

[ 189](structosdp__cmd__text.md#a4dcdd83d3b8d424533ca997111f5cd94) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [length](structosdp__cmd__text.md#a4dcdd83d3b8d424533ca997111f5cd94);

[ 193](structosdp__cmd__text.md#a3a94fa8b18d18845b60476148e2b7325) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structosdp__cmd__text.md#a3a94fa8b18d18845b60476148e2b7325)[[OSDP\_CMD\_TEXT\_MAX\_LEN](osdp_8h.md#acfd9e52e3ca23e6ef3d1cb55a0fa5714)];

194};

195

[ 200](structosdp__cmd__comset.md)struct [osdp\_cmd\_comset](structosdp__cmd__comset.md) {

[ 204](structosdp__cmd__comset.md#af318dc8d5c8148902a2f824d72120ddc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [address](structosdp__cmd__comset.md#af318dc8d5c8148902a2f824d72120ddc);

[ 210](structosdp__cmd__comset.md#a9de97b54c83b9643f1dd3413ec3b15e6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [baud\_rate](structosdp__cmd__comset.md#a9de97b54c83b9643f1dd3413ec3b15e6);

211};

212

[ 221](structosdp__cmd__keyset.md)struct [osdp\_cmd\_keyset](structosdp__cmd__keyset.md) {

[ 226](structosdp__cmd__keyset.md#add89930f6c3b88355fcd2f95573080e6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structosdp__cmd__keyset.md#add89930f6c3b88355fcd2f95573080e6);

[ 230](structosdp__cmd__keyset.md#a673a4897ae2ff6aa9b88af6440fdc5a6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [length](structosdp__cmd__keyset.md#a673a4897ae2ff6aa9b88af6440fdc5a6);

[ 234](structosdp__cmd__keyset.md#af85adb3e9c4f73a91fb7a430ff17f6df) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structosdp__cmd__keyset.md#af85adb3e9c4f73a91fb7a430ff17f6df)[[OSDP\_CMD\_KEYSET\_KEY\_MAX\_LEN](osdp_8h.md#a04a0aa00cbe34e1723be1a4763f63e94)];

235};

236

[ 240](osdp_8h.md#abd8555e895d9370da1400f76c931ba21)enum [osdp\_cmd\_e](osdp_8h.md#abd8555e895d9370da1400f76c931ba21) {

[ 241](osdp_8h.md#abd8555e895d9370da1400f76c931ba21ac59ca019a8253de6e662cd0a09adae1b) [OSDP\_CMD\_OUTPUT](osdp_8h.md#abd8555e895d9370da1400f76c931ba21ac59ca019a8253de6e662cd0a09adae1b) = 1,

[ 242](osdp_8h.md#abd8555e895d9370da1400f76c931ba21a652b1ddc2ecbf295ef20e7f896a45c42) [OSDP\_CMD\_LED](osdp_8h.md#abd8555e895d9370da1400f76c931ba21a652b1ddc2ecbf295ef20e7f896a45c42),

[ 243](osdp_8h.md#abd8555e895d9370da1400f76c931ba21a876b0be45c76196699326ac80f05fc03) [OSDP\_CMD\_BUZZER](osdp_8h.md#abd8555e895d9370da1400f76c931ba21a876b0be45c76196699326ac80f05fc03),

[ 244](osdp_8h.md#abd8555e895d9370da1400f76c931ba21ae7da10f0f9c405838264d475b92b4c01) [OSDP\_CMD\_TEXT](osdp_8h.md#abd8555e895d9370da1400f76c931ba21ae7da10f0f9c405838264d475b92b4c01),

[ 245](osdp_8h.md#abd8555e895d9370da1400f76c931ba21a3abb5eec417c6889734c7f91b34b7a8f) [OSDP\_CMD\_KEYSET](osdp_8h.md#abd8555e895d9370da1400f76c931ba21a3abb5eec417c6889734c7f91b34b7a8f),

[ 246](osdp_8h.md#abd8555e895d9370da1400f76c931ba21a008614ac1abea52942de74ffd33ce289) [OSDP\_CMD\_COMSET](osdp_8h.md#abd8555e895d9370da1400f76c931ba21a008614ac1abea52942de74ffd33ce289),

[ 247](osdp_8h.md#abd8555e895d9370da1400f76c931ba21a80e5942403acbd058d52dd5d58a3aeea) [OSDP\_CMD\_SENTINEL](osdp_8h.md#abd8555e895d9370da1400f76c931ba21a80e5942403acbd058d52dd5d58a3aeea)

248};

249

[ 254](structosdp__cmd.md)struct [osdp\_cmd](structosdp__cmd.md) {

256 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

[ 262](structosdp__cmd.md#a47c50d8c39cd47a7ad282dc91c4e9da8) enum [osdp\_cmd\_e](osdp_8h.md#abd8555e895d9370da1400f76c931ba21) [id](structosdp__cmd.md#a47c50d8c39cd47a7ad282dc91c4e9da8);

264 union {

[ 265](structosdp__cmd.md#acc408da549c0ef9a83e5a569b64dcb36) struct [osdp\_cmd\_led](structosdp__cmd__led.md) [led](structosdp__cmd.md#acc408da549c0ef9a83e5a569b64dcb36);

[ 266](structosdp__cmd.md#a62250f899e17c6fd94a1629f5ef9a479) struct [osdp\_cmd\_buzzer](structosdp__cmd__buzzer.md) [buzzer](structosdp__cmd.md#a62250f899e17c6fd94a1629f5ef9a479);

[ 267](structosdp__cmd.md#a70630f6a8fbebacc27d889dec52336c8) struct [osdp\_cmd\_text](structosdp__cmd__text.md) [text](structosdp__cmd.md#a70630f6a8fbebacc27d889dec52336c8);

[ 268](structosdp__cmd.md#aa745b1efadce9bc41e7253b76bdf2adf) struct [osdp\_cmd\_output](structosdp__cmd__output.md) [output](structosdp__cmd.md#aa745b1efadce9bc41e7253b76bdf2adf);

[ 269](structosdp__cmd.md#a54d63398e914cd41567288f0da456e11) struct [osdp\_cmd\_comset](structosdp__cmd__comset.md) [comset](structosdp__cmd.md#a54d63398e914cd41567288f0da456e11);

[ 270](structosdp__cmd.md#ad629c2622377800a0deab60756fa35a4) struct [osdp\_cmd\_keyset](structosdp__cmd__keyset.md) [keyset](structosdp__cmd.md#ad629c2622377800a0deab60756fa35a4);

271 };

272};

273

[ 278](osdp_8h.md#a976512dfb1a4dc3ea9326d72a0abb5e7)enum [osdp\_event\_cardread\_format\_e](osdp_8h.md#a976512dfb1a4dc3ea9326d72a0abb5e7) {

[ 279](osdp_8h.md#a976512dfb1a4dc3ea9326d72a0abb5e7a8ae3a81c63d022a674e9282a770b8471) [OSDP\_CARD\_FMT\_RAW\_UNSPECIFIED](osdp_8h.md#a976512dfb1a4dc3ea9326d72a0abb5e7a8ae3a81c63d022a674e9282a770b8471),

[ 280](osdp_8h.md#a976512dfb1a4dc3ea9326d72a0abb5e7ab051b59f26c70ea48f7c353fae16b29e) [OSDP\_CARD\_FMT\_RAW\_WIEGAND](osdp_8h.md#a976512dfb1a4dc3ea9326d72a0abb5e7ab051b59f26c70ea48f7c353fae16b29e),

[ 281](osdp_8h.md#a976512dfb1a4dc3ea9326d72a0abb5e7a5e654daacf0c0c084bac2ea4886bb059) [OSDP\_CARD\_FMT\_ASCII](osdp_8h.md#a976512dfb1a4dc3ea9326d72a0abb5e7a5e654daacf0c0c084bac2ea4886bb059),

[ 282](osdp_8h.md#a976512dfb1a4dc3ea9326d72a0abb5e7a6b7fa6ec118b9602fd68eceb6b4959d1) [OSDP\_CARD\_FMT\_SENTINEL](osdp_8h.md#a976512dfb1a4dc3ea9326d72a0abb5e7a6b7fa6ec118b9602fd68eceb6b4959d1)

283};

284

[ 293](structosdp__event__cardread.md)struct [osdp\_event\_cardread](structosdp__event__cardread.md) {

[ 297](structosdp__event__cardread.md#ac6be298c814fcc933d6919a2c7fbb24c) int [reader\_no](structosdp__event__cardread.md#ac6be298c814fcc933d6919a2c7fbb24c);

[ 301](structosdp__event__cardread.md#a7a94e50e9729468baac011dde4806f00) enum [osdp\_event\_cardread\_format\_e](osdp_8h.md#a976512dfb1a4dc3ea9326d72a0abb5e7) [format](structosdp__event__cardread.md#a7a94e50e9729468baac011dde4806f00);

[ 307](structosdp__event__cardread.md#a025b2965987644fe08581b93d1067cb1) int [direction](structosdp__event__cardread.md#a025b2965987644fe08581b93d1067cb1);

[ 311](structosdp__event__cardread.md#a025f3a460042fda69212db1c20d40bc5) int [length](structosdp__event__cardread.md#a025f3a460042fda69212db1c20d40bc5);

[ 315](structosdp__event__cardread.md#af431337d9312618312360ef723f15b98) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structosdp__event__cardread.md#af431337d9312618312360ef723f15b98)[[OSDP\_EVENT\_MAX\_DATALEN](osdp_8h.md#af531800483155468768b89d20c3377d6)];

316};

317

[ 321](structosdp__event__keypress.md)struct [osdp\_event\_keypress](structosdp__event__keypress.md) {

[ 327](structosdp__event__keypress.md#ae6964a42e982021ef44372dca6af1166) int [reader\_no](structosdp__event__keypress.md#ae6964a42e982021ef44372dca6af1166);

[ 331](structosdp__event__keypress.md#a41460942a34a488c78712bfba164f865) int [length](structosdp__event__keypress.md#a41460942a34a488c78712bfba164f865);

[ 335](structosdp__event__keypress.md#a88ac427349340142426e69fb99242cb4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structosdp__event__keypress.md#a88ac427349340142426e69fb99242cb4)[[OSDP\_EVENT\_MAX\_DATALEN](osdp_8h.md#af531800483155468768b89d20c3377d6)];

336};

337

[ 341](osdp_8h.md#a81548fab575d89f66b45a5d4ac85984d)enum [osdp\_event\_type](osdp_8h.md#a81548fab575d89f66b45a5d4ac85984d) {

[ 342](osdp_8h.md#a81548fab575d89f66b45a5d4ac85984da0e5b42ad610675190f1d32a736a51250) [OSDP\_EVENT\_CARDREAD](osdp_8h.md#a81548fab575d89f66b45a5d4ac85984da0e5b42ad610675190f1d32a736a51250),

[ 343](osdp_8h.md#a81548fab575d89f66b45a5d4ac85984da7c51d3f04f97758a6fb24eb4fc69a05c) [OSDP\_EVENT\_KEYPRESS](osdp_8h.md#a81548fab575d89f66b45a5d4ac85984da7c51d3f04f97758a6fb24eb4fc69a05c),

[ 344](osdp_8h.md#a81548fab575d89f66b45a5d4ac85984da34bf34919ee65fe9a943856df65c5e47) [OSDP\_EVENT\_SENTINEL](osdp_8h.md#a81548fab575d89f66b45a5d4ac85984da34bf34919ee65fe9a943856df65c5e47)

345};

346

[ 350](structosdp__event.md)struct [osdp\_event](structosdp__event.md) {

352 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

[ 358](structosdp__event.md#ae72763214c94751d359bf1887d8ea35a) enum [osdp\_event\_type](osdp_8h.md#a81548fab575d89f66b45a5d4ac85984d) [type](structosdp__event.md#ae72763214c94751d359bf1887d8ea35a);

360 union {

[ 361](structosdp__event.md#a35759c65fc80592e42d948059f8178d3) struct [osdp\_event\_keypress](structosdp__event__keypress.md) [keypress](structosdp__event.md#a35759c65fc80592e42d948059f8178d3);

[ 362](structosdp__event.md#ae2488838c114c72ebf0286a6f5c67814) struct [osdp\_event\_cardread](structosdp__event__cardread.md) [cardread](structosdp__event.md#ae2488838c114c72ebf0286a6f5c67814);

363 };

364};

365

[ 381](osdp_8h.md#a6a71149ab51996f345c20ad34d725803)typedef int (\*[pd\_command\_callback\_t](osdp_8h.md#a6a71149ab51996f345c20ad34d725803))(void \*arg, struct [osdp\_cmd](structosdp__cmd.md) \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615));

382

[ 396](osdp_8h.md#aa02ec1fa8d7da5d694d5c2ae163e03cd)typedef int (\*[cp\_event\_callback\_t](osdp_8h.md#aa02ec1fa8d7da5d694d5c2ae163e03cd))(void \*arg, int pd, struct [osdp\_event](structosdp__event.md) \*ev);

397

398#if defined(CONFIG\_OSDP\_MODE\_PD) || defined(\_\_DOXYGEN\_\_)

399

405

[ 413](osdp_8h.md#aa79d4fde3ae007e6c829d56daf8c3e49)void [osdp\_pd\_set\_command\_callback](osdp_8h.md#aa79d4fde3ae007e6c829d56daf8c3e49)([pd\_command\_callback\_t](osdp_8h.md#a6a71149ab51996f345c20ad34d725803) cb, void \*arg);

414

[ 424](osdp_8h.md#ac097208c2b197ec4ebe567d59831a29f)int [osdp\_pd\_notify\_event](osdp_8h.md#ac097208c2b197ec4ebe567d59831a29f)(const struct [osdp\_event](structosdp__event.md) \*event);

425

429

430#else /\* CONFIG\_OSDP\_MODE\_PD \*/

431

444int osdp\_cp\_send\_command(int pd, struct [osdp\_cmd](structosdp__cmd.md) \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615));

445

446

454void osdp\_cp\_set\_event\_callback([cp\_event\_callback\_t](osdp_8h.md#aa02ec1fa8d7da5d694d5c2ae163e03cd) cb, void \*arg);

455

456#endif /\* CONFIG\_OSDP\_MODE\_PD \*/

457

458#if defined(CONFIG\_OSDP\_SC\_ENABLED) || defined(\_\_DOXYGEN\_\_)

459

466

[ 471](osdp_8h.md#ab1335ca06ebddff18873971e4dc03c40)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [osdp\_get\_sc\_status\_mask](osdp_8h.md#ab1335ca06ebddff18873971e4dc03c40)(void);

472

476

477#endif

478

479#ifdef \_\_cplusplus

480}

481#endif

482

483#endif /\* \_OSDP\_H\_ \*/

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[kernel.h](kernel_8h.md)

Public kernel APIs.

[OSDP\_CMD\_KEYSET\_KEY\_MAX\_LEN](osdp_8h.md#a04a0aa00cbe34e1723be1a4763f63e94)

#define OSDP\_CMD\_KEYSET\_KEY\_MAX\_LEN

Max length of key data for keyset command.

**Definition** osdp.h:25

[pd\_command\_callback\_t](osdp_8h.md#a6a71149ab51996f345c20ad34d725803)

int(\* pd\_command\_callback\_t)(void \*arg, struct osdp\_cmd \*cmd)

Callback for PD command notifications.

**Definition** osdp.h:381

[osdp\_event\_type](osdp_8h.md#a81548fab575d89f66b45a5d4ac85984d)

osdp\_event\_type

OSDP PD Events.

**Definition** osdp.h:341

[OSDP\_EVENT\_CARDREAD](osdp_8h.md#a81548fab575d89f66b45a5d4ac85984da0e5b42ad610675190f1d32a736a51250)

@ OSDP\_EVENT\_CARDREAD

Card read event.

**Definition** osdp.h:342

[OSDP\_EVENT\_SENTINEL](osdp_8h.md#a81548fab575d89f66b45a5d4ac85984da34bf34919ee65fe9a943856df65c5e47)

@ OSDP\_EVENT\_SENTINEL

Max event value.

**Definition** osdp.h:344

[OSDP\_EVENT\_KEYPRESS](osdp_8h.md#a81548fab575d89f66b45a5d4ac85984da7c51d3f04f97758a6fb24eb4fc69a05c)

@ OSDP\_EVENT\_KEYPRESS

Keypad press event.

**Definition** osdp.h:343

[osdp\_event\_cardread\_format\_e](osdp_8h.md#a976512dfb1a4dc3ea9326d72a0abb5e7)

osdp\_event\_cardread\_format\_e

Various card formats that a PD can support.

**Definition** osdp.h:278

[OSDP\_CARD\_FMT\_ASCII](osdp_8h.md#a976512dfb1a4dc3ea9326d72a0abb5e7a5e654daacf0c0c084bac2ea4886bb059)

@ OSDP\_CARD\_FMT\_ASCII

ASCII card format.

**Definition** osdp.h:281

[OSDP\_CARD\_FMT\_SENTINEL](osdp_8h.md#a976512dfb1a4dc3ea9326d72a0abb5e7a6b7fa6ec118b9602fd68eceb6b4959d1)

@ OSDP\_CARD\_FMT\_SENTINEL

Max card format value.

**Definition** osdp.h:282

[OSDP\_CARD\_FMT\_RAW\_UNSPECIFIED](osdp_8h.md#a976512dfb1a4dc3ea9326d72a0abb5e7a8ae3a81c63d022a674e9282a770b8471)

@ OSDP\_CARD\_FMT\_RAW\_UNSPECIFIED

Unspecified card format.

**Definition** osdp.h:279

[OSDP\_CARD\_FMT\_RAW\_WIEGAND](osdp_8h.md#a976512dfb1a4dc3ea9326d72a0abb5e7ab051b59f26c70ea48f7c353fae16b29e)

@ OSDP\_CARD\_FMT\_RAW\_WIEGAND

Wiegand card format.

**Definition** osdp.h:280

[osdp\_led\_color\_e](osdp_8h.md#a97ee0d8eb19e4e37ac89b2b6d338b84e)

osdp\_led\_color\_e

LED Colors as specified in OSDP for the on\_color/off\_color parameters.

**Definition** osdp.h:59

[OSDP\_LED\_COLOR\_SENTINEL](osdp_8h.md#a97ee0d8eb19e4e37ac89b2b6d338b84ea0a80ccbb26b42ebc2cca602c7be3117a)

@ OSDP\_LED\_COLOR\_SENTINEL

Max value.

**Definition** osdp.h:65

[OSDP\_LED\_COLOR\_RED](osdp_8h.md#a97ee0d8eb19e4e37ac89b2b6d338b84ea6832c2b25f228213022d0dbb5f5e1584)

@ OSDP\_LED\_COLOR\_RED

Red.

**Definition** osdp.h:61

[OSDP\_LED\_COLOR\_NONE](osdp_8h.md#a97ee0d8eb19e4e37ac89b2b6d338b84ea72a45fa8f0b48a165c5507e456b4b1e7)

@ OSDP\_LED\_COLOR\_NONE

No color.

**Definition** osdp.h:60

[OSDP\_LED\_COLOR\_GREEN](osdp_8h.md#a97ee0d8eb19e4e37ac89b2b6d338b84eac4024077b8804580d2480708e0b14ae4)

@ OSDP\_LED\_COLOR\_GREEN

Green.

**Definition** osdp.h:62

[OSDP\_LED\_COLOR\_BLUE](osdp_8h.md#a97ee0d8eb19e4e37ac89b2b6d338b84eadc9d0a41de52b0aa20e428e79e7c6b66)

@ OSDP\_LED\_COLOR\_BLUE

Blue.

**Definition** osdp.h:64

[OSDP\_LED\_COLOR\_AMBER](osdp_8h.md#a97ee0d8eb19e4e37ac89b2b6d338b84eadd22879185802d0705d7195e1d9bd42c)

@ OSDP\_LED\_COLOR\_AMBER

Amber.

**Definition** osdp.h:63

[cp\_event\_callback\_t](osdp_8h.md#aa02ec1fa8d7da5d694d5c2ae163e03cd)

int(\* cp\_event\_callback\_t)(void \*arg, int pd, struct osdp\_event \*ev)

Callback for CP event notifications.

**Definition** osdp.h:396

[osdp\_pd\_set\_command\_callback](osdp_8h.md#aa79d4fde3ae007e6c829d56daf8c3e49)

void osdp\_pd\_set\_command\_callback(pd\_command\_callback\_t cb, void \*arg)

Set callback method for PD command notification.

[osdp\_get\_sc\_status\_mask](osdp_8h.md#ab1335ca06ebddff18873971e4dc03c40)

uint32\_t osdp\_get\_sc\_status\_mask(void)

Get the current SC status mask.

[osdp\_cmd\_e](osdp_8h.md#abd8555e895d9370da1400f76c931ba21)

osdp\_cmd\_e

OSDP application exposed commands.

**Definition** osdp.h:240

[OSDP\_CMD\_COMSET](osdp_8h.md#abd8555e895d9370da1400f76c931ba21a008614ac1abea52942de74ffd33ce289)

@ OSDP\_CMD\_COMSET

PD Communication Configuration Command.

**Definition** osdp.h:246

[OSDP\_CMD\_KEYSET](osdp_8h.md#abd8555e895d9370da1400f76c931ba21a3abb5eec417c6889734c7f91b34b7a8f)

@ OSDP\_CMD\_KEYSET

Encryption Key Set Command.

**Definition** osdp.h:245

[OSDP\_CMD\_LED](osdp_8h.md#abd8555e895d9370da1400f76c931ba21a652b1ddc2ecbf295ef20e7f896a45c42)

@ OSDP\_CMD\_LED

Reader LED control command.

**Definition** osdp.h:242

[OSDP\_CMD\_SENTINEL](osdp_8h.md#abd8555e895d9370da1400f76c931ba21a80e5942403acbd058d52dd5d58a3aeea)

@ OSDP\_CMD\_SENTINEL

Max command value.

**Definition** osdp.h:247

[OSDP\_CMD\_BUZZER](osdp_8h.md#abd8555e895d9370da1400f76c931ba21a876b0be45c76196699326ac80f05fc03)

@ OSDP\_CMD\_BUZZER

Reader buzzer control command.

**Definition** osdp.h:243

[OSDP\_CMD\_OUTPUT](osdp_8h.md#abd8555e895d9370da1400f76c931ba21ac59ca019a8253de6e662cd0a09adae1b)

@ OSDP\_CMD\_OUTPUT

Output control command.

**Definition** osdp.h:241

[OSDP\_CMD\_TEXT](osdp_8h.md#abd8555e895d9370da1400f76c931ba21ae7da10f0f9c405838264d475b92b4c01)

@ OSDP\_CMD\_TEXT

Reader text output command.

**Definition** osdp.h:244

[osdp\_pd\_notify\_event](osdp_8h.md#ac097208c2b197ec4ebe567d59831a29f)

int osdp\_pd\_notify\_event(const struct osdp\_event \*event)

API to notify PD events to CP.

[OSDP\_CMD\_TEXT\_MAX\_LEN](osdp_8h.md#acfd9e52e3ca23e6ef3d1cb55a0fa5714)

#define OSDP\_CMD\_TEXT\_MAX\_LEN

Max length of text for text command.

**Definition** osdp.h:24

[OSDP\_EVENT\_MAX\_DATALEN](osdp_8h.md#af531800483155468768b89d20c3377d6)

#define OSDP\_EVENT\_MAX\_DATALEN

Max length of event data.

**Definition** osdp.h:26

[slist.h](slist_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[osdp\_cmd\_buzzer](structosdp__cmd__buzzer.md)

Sent from CP to control the behaviour of a buzzer in the PD.

**Definition** osdp.h:131

[osdp\_cmd\_buzzer::reader](structosdp__cmd__buzzer.md#a0e97e1e33eac4f25e5a05586f8135ab3)

uint8\_t reader

Reader number.

**Definition** osdp.h:135

[osdp\_cmd\_buzzer::rep\_count](structosdp__cmd__buzzer.md#a0ea92ffb8ed7527e0373c0530edfb61d)

uint8\_t rep\_count

The number of times to repeat the ON/OFF cycle; 0: forever.

**Definition** osdp.h:155

[osdp\_cmd\_buzzer::control\_code](structosdp__cmd__buzzer.md#a16d0f385264e247d942367a6a13a77af)

uint8\_t control\_code

Control code.

**Definition** osdp.h:143

[osdp\_cmd\_buzzer::on\_count](structosdp__cmd__buzzer.md#a9082cf0dd2e3e9d31d95051f2952d611)

uint8\_t on\_count

The ON duration of the sound, in units of 100 ms.

**Definition** osdp.h:147

[osdp\_cmd\_buzzer::off\_count](structosdp__cmd__buzzer.md#ac83cdb57418fc28f11c686e79e811492)

uint8\_t off\_count

The OFF duration of the sound, in units of 100 ms.

**Definition** osdp.h:151

[osdp\_cmd\_comset](structosdp__cmd__comset.md)

Sent in response to a COMSET command.

**Definition** osdp.h:200

[osdp\_cmd\_comset::baud\_rate](structosdp__cmd__comset.md#a9de97b54c83b9643f1dd3413ec3b15e6)

uint32\_t baud\_rate

Baud rate.

**Definition** osdp.h:210

[osdp\_cmd\_comset::address](structosdp__cmd__comset.md#af318dc8d5c8148902a2f824d72120ddc)

uint8\_t address

Unit ID to which this PD will respond after the change takes effect.

**Definition** osdp.h:204

[osdp\_cmd\_keyset](structosdp__cmd__keyset.md)

This command transfers an encryption key from the CP to a PD.

**Definition** osdp.h:221

[osdp\_cmd\_keyset::length](structosdp__cmd__keyset.md#a673a4897ae2ff6aa9b88af6440fdc5a6)

uint8\_t length

Number of bytes of key data - (Key Length in bits + 7) / 8.

**Definition** osdp.h:230

[osdp\_cmd\_keyset::type](structosdp__cmd__keyset.md#add89930f6c3b88355fcd2f95573080e6)

uint8\_t type

Type of keys:

**Definition** osdp.h:226

[osdp\_cmd\_keyset::data](structosdp__cmd__keyset.md#af85adb3e9c4f73a91fb7a430ff17f6df)

uint8\_t data[32]

Key data.

**Definition** osdp.h:234

[osdp\_cmd\_led\_params](structosdp__cmd__led__params.md)

LED params sub-structure.

**Definition** osdp.h:71

[osdp\_cmd\_led\_params::timer\_count](structosdp__cmd__led__params.md#a002de25cd5070cb96e90ccd0d2091216)

uint16\_t timer\_count

Time in units of 100 ms (only for temporary mode).

**Definition** osdp.h:103

[osdp\_cmd\_led\_params::off\_count](structosdp__cmd__led__params.md#a278ff380c2ab7d9c83b55aa49b3137cb)

uint8\_t off\_count

The OFF duration of the flash, in units of 100 ms.

**Definition** osdp.h:91

[osdp\_cmd\_led\_params::on\_color](structosdp__cmd__led__params.md#a80b47a4c55494d7062c4a83fd81b0910)

uint8\_t on\_color

Color to set during the ON timer (see osdp\_led\_color\_e).

**Definition** osdp.h:95

[osdp\_cmd\_led\_params::off\_color](structosdp__cmd__led__params.md#ac6f1c1269697fcab96b6f68d62381ded)

uint8\_t off\_color

Color to set during the OFF timer (see osdp\_led\_color\_e).

**Definition** osdp.h:99

[osdp\_cmd\_led\_params::on\_count](structosdp__cmd__led__params.md#adde9dfdd167d9dfc122b56cf5e47b10f)

uint8\_t on\_count

The ON duration of the flash, in units of 100 ms.

**Definition** osdp.h:87

[osdp\_cmd\_led\_params::control\_code](structosdp__cmd__led__params.md#ae95e3b87bbccd7d9897fef329001ce39)

uint8\_t control\_code

Control code.

**Definition** osdp.h:83

[osdp\_cmd\_led](structosdp__cmd__led.md)

Sent from CP to PD to control the behaviour of it's on-board LEDs.

**Definition** osdp.h:109

[osdp\_cmd\_led::permanent](structosdp__cmd__led.md#a033fd34a88b03d22a088bd7d2676efb5)

struct osdp\_cmd\_led\_params permanent

Permanent LED status descriptor.

**Definition** osdp.h:125

[osdp\_cmd\_led::temporary](structosdp__cmd__led.md#a2130237d1b79ee36c5f5087cdec7acfb)

struct osdp\_cmd\_led\_params temporary

Ephemeral LED status descriptor.

**Definition** osdp.h:121

[osdp\_cmd\_led::led\_number](structosdp__cmd__led.md#ae4ff10389198d00047ffa2a7ec7d15ac)

uint8\_t led\_number

LED number.

**Definition** osdp.h:117

[osdp\_cmd\_led::reader](structosdp__cmd__led.md#afe5e061d91fda9f008b5f8e5441df467)

uint8\_t reader

Reader number.

**Definition** osdp.h:113

[osdp\_cmd\_output](structosdp__cmd__output.md)

Command sent from CP to Control digital output of PD.

**Definition** osdp.h:31

[osdp\_cmd\_output::control\_code](structosdp__cmd__output.md#a1037244ed5f7c78eab51d6c08130b5d0)

uint8\_t control\_code

Control code.

**Definition** osdp.h:49

[osdp\_cmd\_output::timer\_count](structosdp__cmd__output.md#a4cd89d5c683b31d0e8eaf007443703a6)

uint16\_t timer\_count

Time in units of 100 ms.

**Definition** osdp.h:53

[osdp\_cmd\_output::output\_no](structosdp__cmd__output.md#af5e1d55c987dd82ed4959f251a811846)

uint8\_t output\_no

Output number.

**Definition** osdp.h:37

[osdp\_cmd\_text](structosdp__cmd__text.md)

Command to manipulate any display units that the PD supports.

**Definition** osdp.h:161

[osdp\_cmd\_text::offset\_row](structosdp__cmd__text.md#a16f11f35eacb2876b09d148349b7ed3c)

uint8\_t offset\_row

Row to display the first character (1-indexed).

**Definition** osdp.h:181

[osdp\_cmd\_text::data](structosdp__cmd__text.md#a3a94fa8b18d18845b60476148e2b7325)

uint8\_t data[32]

The string to display.

**Definition** osdp.h:193

[osdp\_cmd\_text::reader](structosdp__cmd__text.md#a3fa3d0780aa98542a270f6bdb6f49737)

uint8\_t reader

Reader number.

**Definition** osdp.h:165

[osdp\_cmd\_text::control\_code](structosdp__cmd__text.md#a46fe3f66e01229e763a6f06bd8bdfab8)

uint8\_t control\_code

Control code.

**Definition** osdp.h:173

[osdp\_cmd\_text::length](structosdp__cmd__text.md#a4dcdd83d3b8d424533ca997111f5cd94)

uint8\_t length

Number of characters in the string.

**Definition** osdp.h:189

[osdp\_cmd\_text::offset\_col](structosdp__cmd__text.md#a5e7b4c03b1649d8edbf53932ee90f7b3)

uint8\_t offset\_col

Column to display the first character (1-indexed).

**Definition** osdp.h:185

[osdp\_cmd\_text::temp\_time](structosdp__cmd__text.md#acde9abcb023eb77845af8ea0935e63fa)

uint8\_t temp\_time

Duration to display temporary text, in seconds.

**Definition** osdp.h:177

[osdp\_cmd](structosdp__cmd.md)

OSDP Command Structure.

**Definition** osdp.h:254

[osdp\_cmd::id](structosdp__cmd.md#a47c50d8c39cd47a7ad282dc91c4e9da8)

enum osdp\_cmd\_e id

Command ID.

**Definition** osdp.h:262

[osdp\_cmd::comset](structosdp__cmd.md#a54d63398e914cd41567288f0da456e11)

struct osdp\_cmd\_comset comset

Comset command structure.

**Definition** osdp.h:269

[osdp\_cmd::buzzer](structosdp__cmd.md#a62250f899e17c6fd94a1629f5ef9a479)

struct osdp\_cmd\_buzzer buzzer

Buzzer command structure.

**Definition** osdp.h:266

[osdp\_cmd::text](structosdp__cmd.md#a70630f6a8fbebacc27d889dec52336c8)

struct osdp\_cmd\_text text

Text command structure.

**Definition** osdp.h:267

[osdp\_cmd::output](structosdp__cmd.md#aa745b1efadce9bc41e7253b76bdf2adf)

struct osdp\_cmd\_output output

Output command structure.

**Definition** osdp.h:268

[osdp\_cmd::led](structosdp__cmd.md#acc408da549c0ef9a83e5a569b64dcb36)

struct osdp\_cmd\_led led

LED command structure.

**Definition** osdp.h:265

[osdp\_cmd::keyset](structosdp__cmd.md#ad629c2622377800a0deab60756fa35a4)

struct osdp\_cmd\_keyset keyset

Keyset command structure.

**Definition** osdp.h:270

[osdp\_event\_cardread](structosdp__event__cardread.md)

OSDP event cardread.

**Definition** osdp.h:293

[osdp\_event\_cardread::direction](structosdp__event__cardread.md#a025b2965987644fe08581b93d1067cb1)

int direction

Direction of data in data array.

**Definition** osdp.h:307

[osdp\_event\_cardread::length](structosdp__event__cardread.md#a025f3a460042fda69212db1c20d40bc5)

int length

Length of card data in bytes or bits depending on format.

**Definition** osdp.h:311

[osdp\_event\_cardread::format](structosdp__event__cardread.md#a7a94e50e9729468baac011dde4806f00)

enum osdp\_event\_cardread\_format\_e format

Format of the card being read.

**Definition** osdp.h:301

[osdp\_event\_cardread::reader\_no](structosdp__event__cardread.md#ac6be298c814fcc933d6919a2c7fbb24c)

int reader\_no

Reader number.

**Definition** osdp.h:297

[osdp\_event\_cardread::data](structosdp__event__cardread.md#af431337d9312618312360ef723f15b98)

uint8\_t data[64]

Card data of length bytes or bits bits depending on format.

**Definition** osdp.h:315

[osdp\_event\_keypress](structosdp__event__keypress.md)

OSDP Event Keypad.

**Definition** osdp.h:321

[osdp\_event\_keypress::length](structosdp__event__keypress.md#a41460942a34a488c78712bfba164f865)

int length

Length of keypress data in bytes.

**Definition** osdp.h:331

[osdp\_event\_keypress::data](structosdp__event__keypress.md#a88ac427349340142426e69fb99242cb4)

uint8\_t data[64]

Keypress data of length bytes.

**Definition** osdp.h:335

[osdp\_event\_keypress::reader\_no](structosdp__event__keypress.md#ae6964a42e982021ef44372dca6af1166)

int reader\_no

Reader number.

**Definition** osdp.h:327

[osdp\_event](structosdp__event.md)

OSDP Event structure.

**Definition** osdp.h:350

[osdp\_event::keypress](structosdp__event.md#a35759c65fc80592e42d948059f8178d3)

struct osdp\_event\_keypress keypress

Keypress event structure.

**Definition** osdp.h:361

[osdp\_event::cardread](structosdp__event.md#ae2488838c114c72ebf0286a6f5c67814)

struct osdp\_event\_cardread cardread

Card read event structure.

**Definition** osdp.h:362

[osdp\_event::type](structosdp__event.md#ae72763214c94751d359bf1887d8ea35a)

enum osdp\_event\_type type

Event type.

**Definition** osdp.h:358

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [osdp.h](osdp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/off__raw__tx__api_8h_source.html
original_path: doxygen/html/off__raw__tx__api_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

off\_raw\_tx\_api.h

[Go to the documentation of this file.](off__raw__tx__api_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

13

14#ifndef INCLUDE\_ZEPHYR\_DRIVERS\_OFF\_RAW\_TX\_API\_H\_

15#define INCLUDE\_ZEPHYR\_DRIVERS\_OFF\_RAW\_TX\_API\_H\_

16

17#include <[stdbool.h](stdbool_8h.md)>

18#include <[stdint.h](stdint_8h.md)>

19#include "osal\_api.h"

20

21/\* Minimum frame size for raw packet transmission \*/

[ 22](group__nrf70__off__raw__tx__api.md#gae2e1b9b12b8e4478e994d76888f40900)#define NRF\_WIFI\_OFF\_RAW\_TX\_FRAME\_SIZE\_MIN 26

23/\* Maximum frame size for raw packet transmission \*/

[ 24](group__nrf70__off__raw__tx__api.md#ga83452cafd85400cf926c656201d77959)#define NRF\_WIFI\_OFF\_RAW\_TX\_FRAME\_SIZE\_MAX 600

25/\* Maximum length of country code\*/

[ 26](group__nrf70__off__raw__tx__api.md#ga55204b43c73489568ea1af9cee7ff130)#define NRF\_WIFI\_COUNTRY\_CODE\_LEN 2

[ 31](group__nrf70__off__raw__tx__api.md#ga3370994917570dfe6ff14b0c5ecd123d)enum [nrf\_wifi\_off\_raw\_tx\_rate](group__nrf70__off__raw__tx__api.md#ga3370994917570dfe6ff14b0c5ecd123d) {

[ 33](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da77f65aafc9e4063c00b3864f49c179da) [RATE\_1M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da77f65aafc9e4063c00b3864f49c179da),

[ 35](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123dacb4eb3c940da0cfa69cb0e57f8bbbef4) [RATE\_2M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123dacb4eb3c940da0cfa69cb0e57f8bbbef4),

[ 37](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da4e03ebda6563231013ffd799f28d2e29) [RATE\_5\_5M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da4e03ebda6563231013ffd799f28d2e29),

[ 39](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123dab7398b3c15bfd6d39711e8a89b7d3b06) [RATE\_11M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123dab7398b3c15bfd6d39711e8a89b7d3b06),

[ 41](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da20cc375919c198887fcbc8da795eec49) [RATE\_6M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da20cc375919c198887fcbc8da795eec49),

[ 43](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da60095536fa78d822f490296fe5a131af) [RATE\_9M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da60095536fa78d822f490296fe5a131af),

[ 45](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da0657fa7fa3d22e8c7113754a26541d76) [RATE\_12M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da0657fa7fa3d22e8c7113754a26541d76),

[ 47](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123daaeb9a1cc5312660ed227c28fa52e03f3) [RATE\_18M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123daaeb9a1cc5312660ed227c28fa52e03f3),

[ 49](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123dab45ef31556754a8a79ebae9ca1082148) [RATE\_24M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123dab45ef31556754a8a79ebae9ca1082148),

[ 51](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123dadc7638f55562af7781e0a4b08118477c) [RATE\_36M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123dadc7638f55562af7781e0a4b08118477c),

[ 53](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da851615a4ce04de41e72adf7c91bbbe11) [RATE\_48M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da851615a4ce04de41e72adf7c91bbbe11),

[ 55](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da05960a1ad3453423c65ff0e5d774bf3e) [RATE\_54M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da05960a1ad3453423c65ff0e5d774bf3e),

[ 57](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da755b9128a7146e4a2084d02a8d2d5760) [RATE\_MCS0](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da755b9128a7146e4a2084d02a8d2d5760),

[ 59](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da289e2a220decd89241fe02c0d033d04b) [RATE\_MCS1](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da289e2a220decd89241fe02c0d033d04b),

[ 61](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123dad123030681213480f5bebd7a3e6de676) [RATE\_MCS2](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123dad123030681213480f5bebd7a3e6de676),

[ 63](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da661c627527435aaa5f47cb90c922bf7e) [RATE\_MCS3](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da661c627527435aaa5f47cb90c922bf7e),

[ 65](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123dafdc18a82657bc74a3ea15a459f1366fd) [RATE\_MCS4](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123dafdc18a82657bc74a3ea15a459f1366fd),

[ 67](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123dae1274d875d22d0079a9e3b64ea979e1b) [RATE\_MCS5](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123dae1274d875d22d0079a9e3b64ea979e1b),

[ 69](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da2d3d9d6eb775d5b2856de24a3359942a) [RATE\_MCS6](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da2d3d9d6eb775d5b2856de24a3359942a),

[ 71](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123daf5b862e8fcaae4a26a415741eaf40de1) [RATE\_MCS7](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123daf5b862e8fcaae4a26a415741eaf40de1),

[ 73](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123daf90f54fa68da0241bf9055a23e3f43ab) [RATE\_MAX](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123daf90f54fa68da0241bf9055a23e3f43ab)

74};

75

76

[ 81](group__nrf70__off__raw__tx__api.md#ga7cc32e6229ddd41db7d310f29a3fc09d)enum [nrf\_wifi\_off\_raw\_tx\_he\_gi](group__nrf70__off__raw__tx__api.md#ga7cc32e6229ddd41db7d310f29a3fc09d) {

[ 83](group__nrf70__off__raw__tx__api.md#gga7cc32e6229ddd41db7d310f29a3fc09da991485bf09a58a8f9b1751d5c0781598) [HE\_GI\_800NS](group__nrf70__off__raw__tx__api.md#gga7cc32e6229ddd41db7d310f29a3fc09da991485bf09a58a8f9b1751d5c0781598),

[ 85](group__nrf70__off__raw__tx__api.md#gga7cc32e6229ddd41db7d310f29a3fc09da7fad526cc4b6544d13f688395229336f) [HE\_GI\_1600NS](group__nrf70__off__raw__tx__api.md#gga7cc32e6229ddd41db7d310f29a3fc09da7fad526cc4b6544d13f688395229336f),

[ 87](group__nrf70__off__raw__tx__api.md#gga7cc32e6229ddd41db7d310f29a3fc09da14c3bac543f5c886265a22bb77f47b71) [HE\_GI\_3200NS](group__nrf70__off__raw__tx__api.md#gga7cc32e6229ddd41db7d310f29a3fc09da14c3bac543f5c886265a22bb77f47b71),

[ 89](group__nrf70__off__raw__tx__api.md#gga7cc32e6229ddd41db7d310f29a3fc09da132ff7b3dfe33b1f49f7c5e87b95264c) [HE\_GI\_MAX](group__nrf70__off__raw__tx__api.md#gga7cc32e6229ddd41db7d310f29a3fc09da132ff7b3dfe33b1f49f7c5e87b95264c)

90};

91

92

[ 97](group__nrf70__off__raw__tx__api.md#ga87b545520cdcc2ed387ebed770420c61)enum [nrf\_wifi\_off\_raw\_tx\_he\_ltf](group__nrf70__off__raw__tx__api.md#ga87b545520cdcc2ed387ebed770420c61) {

[ 99](group__nrf70__off__raw__tx__api.md#gga87b545520cdcc2ed387ebed770420c61ae6ec0118f3e5c10892790e2cbea4d701) [HE\_LTF\_3200NS](group__nrf70__off__raw__tx__api.md#gga87b545520cdcc2ed387ebed770420c61ae6ec0118f3e5c10892790e2cbea4d701),

[ 101](group__nrf70__off__raw__tx__api.md#gga87b545520cdcc2ed387ebed770420c61ab3d148ec3de601ae0b10538edf1bb7e2) [HE\_LTF\_6400NS](group__nrf70__off__raw__tx__api.md#gga87b545520cdcc2ed387ebed770420c61ab3d148ec3de601ae0b10538edf1bb7e2),

[ 103](group__nrf70__off__raw__tx__api.md#gga87b545520cdcc2ed387ebed770420c61a204188c45996539fa1b6141ed40f3448) [HE\_LTF\_12800NS](group__nrf70__off__raw__tx__api.md#gga87b545520cdcc2ed387ebed770420c61a204188c45996539fa1b6141ed40f3448),

[ 105](group__nrf70__off__raw__tx__api.md#gga87b545520cdcc2ed387ebed770420c61ae0b112fb129512eeef0bebc6956281cd) [HE\_LTF\_MAX](group__nrf70__off__raw__tx__api.md#gga87b545520cdcc2ed387ebed770420c61ae0b112fb129512eeef0bebc6956281cd)

106};

107

[ 112](group__nrf70__off__raw__tx__api.md#ga4c785f4ac1c2f8c81be4e39f76a54131)enum [nrf\_wifi\_off\_raw\_tx\_tput\_mode](group__nrf70__off__raw__tx__api.md#ga4c785f4ac1c2f8c81be4e39f76a54131) {

[ 114](group__nrf70__off__raw__tx__api.md#gga4c785f4ac1c2f8c81be4e39f76a54131aa2cafbe7518c4c690fda12ca6bdc9023) [TPUT\_MODE\_LEGACY](group__nrf70__off__raw__tx__api.md#gga4c785f4ac1c2f8c81be4e39f76a54131aa2cafbe7518c4c690fda12ca6bdc9023),

[ 116](group__nrf70__off__raw__tx__api.md#gga4c785f4ac1c2f8c81be4e39f76a54131a2e61c593601ecb2a30ffe58c8a88a72e) [TPUT\_MODE\_HT](group__nrf70__off__raw__tx__api.md#gga4c785f4ac1c2f8c81be4e39f76a54131a2e61c593601ecb2a30ffe58c8a88a72e),

[ 118](group__nrf70__off__raw__tx__api.md#gga4c785f4ac1c2f8c81be4e39f76a54131aeb282682e2bfa2e610cf0e2b2822d21e) [TPUT\_MODE\_VHT](group__nrf70__off__raw__tx__api.md#gga4c785f4ac1c2f8c81be4e39f76a54131aeb282682e2bfa2e610cf0e2b2822d21e),

[ 120](group__nrf70__off__raw__tx__api.md#gga4c785f4ac1c2f8c81be4e39f76a54131abe6d341d6c32b9fb1d5f2658b687f9dd) [TPUT\_MODE\_HE\_SU](group__nrf70__off__raw__tx__api.md#gga4c785f4ac1c2f8c81be4e39f76a54131abe6d341d6c32b9fb1d5f2658b687f9dd),

[ 122](group__nrf70__off__raw__tx__api.md#gga4c785f4ac1c2f8c81be4e39f76a54131ace4701907a49d610806d61eafd3dd6c6) [TPUT\_MODE\_HE\_ER\_SU](group__nrf70__off__raw__tx__api.md#gga4c785f4ac1c2f8c81be4e39f76a54131ace4701907a49d610806d61eafd3dd6c6),

[ 124](group__nrf70__off__raw__tx__api.md#gga4c785f4ac1c2f8c81be4e39f76a54131a3989864c3272ca71728b6baa6bfdbd3e) [TPUT\_MODE\_HE\_TB](group__nrf70__off__raw__tx__api.md#gga4c785f4ac1c2f8c81be4e39f76a54131a3989864c3272ca71728b6baa6bfdbd3e),

[ 126](group__nrf70__off__raw__tx__api.md#gga4c785f4ac1c2f8c81be4e39f76a54131a4cd1f38b7adc6a1722903963bc8876ac) [TPUT\_MODE\_MAX](group__nrf70__off__raw__tx__api.md#gga4c785f4ac1c2f8c81be4e39f76a54131a4cd1f38b7adc6a1722903963bc8876ac)

127};

128

[ 133](structnrf__wifi__off__raw__tx__stats.md)struct [nrf\_wifi\_off\_raw\_tx\_stats](structnrf__wifi__off__raw__tx__stats.md) {

[ 135](structnrf__wifi__off__raw__tx__stats.md#a4b4ec40c9c58f1c004182b8be773e838) unsigned int [off\_raw\_tx\_pkt\_sent](structnrf__wifi__off__raw__tx__stats.md#a4b4ec40c9c58f1c004182b8be773e838);

136};

137

[ 142](structnrf__wifi__off__raw__tx__conf.md)struct [nrf\_wifi\_off\_raw\_tx\_conf](structnrf__wifi__off__raw__tx__conf.md) {

[ 144](structnrf__wifi__off__raw__tx__conf.md#a2a772fb8c30ac44592a437d9782d76cf) unsigned int [period\_us](structnrf__wifi__off__raw__tx__conf.md#a2a772fb8c30ac44592a437d9782d76cf);

[ 146](structnrf__wifi__off__raw__tx__conf.md#a328e1b3b7411e5685683c8718a05173e) unsigned int [tx\_pwr](structnrf__wifi__off__raw__tx__conf.md#a328e1b3b7411e5685683c8718a05173e);

[ 148](structnrf__wifi__off__raw__tx__conf.md#abff388f54589d410b10e2e55a4574314) unsigned int [chan](structnrf__wifi__off__raw__tx__conf.md#abff388f54589d410b10e2e55a4574314);

[ 150](structnrf__wifi__off__raw__tx__conf.md#a907d509fb2988e5003120ccff4f24932) bool [short\_preamble](structnrf__wifi__off__raw__tx__conf.md#a907d509fb2988e5003120ccff4f24932);

151 /\* Number of times a packet should be retried at each possible rate \*/

[ 152](structnrf__wifi__off__raw__tx__conf.md#ab88c522e97c5f624b78133a3d184ebd0) unsigned int [num\_retries](structnrf__wifi__off__raw__tx__conf.md#ab88c522e97c5f624b78133a3d184ebd0);

[ 154](structnrf__wifi__off__raw__tx__conf.md#a631f15bbd4930256b3b6f64175a630b7) enum [nrf\_wifi\_off\_raw\_tx\_tput\_mode](group__nrf70__off__raw__tx__api.md#ga4c785f4ac1c2f8c81be4e39f76a54131) [tput\_mode](structnrf__wifi__off__raw__tx__conf.md#a631f15bbd4930256b3b6f64175a630b7);

155 /\* Rate at which packet needs to be transmitted. Refer &enum nrf\_wifi\_off\_raw\_tx\_rate \*/

[ 156](structnrf__wifi__off__raw__tx__conf.md#a52419b8149b390888491511413e17f98) enum [nrf\_wifi\_off\_raw\_tx\_rate](group__nrf70__off__raw__tx__api.md#ga3370994917570dfe6ff14b0c5ecd123d) [rate](structnrf__wifi__off__raw__tx__conf.md#a52419b8149b390888491511413e17f98);

[ 158](structnrf__wifi__off__raw__tx__conf.md#a3e56b1bf386d483d0f6eb04b00c46cac) enum [nrf\_wifi\_off\_raw\_tx\_he\_gi](group__nrf70__off__raw__tx__api.md#ga7cc32e6229ddd41db7d310f29a3fc09d) [he\_gi](structnrf__wifi__off__raw__tx__conf.md#a3e56b1bf386d483d0f6eb04b00c46cac);

[ 160](structnrf__wifi__off__raw__tx__conf.md#a30ca67432373107948926c646c951237) enum [nrf\_wifi\_off\_raw\_tx\_he\_ltf](group__nrf70__off__raw__tx__api.md#ga87b545520cdcc2ed387ebed770420c61) [he\_ltf](structnrf__wifi__off__raw__tx__conf.md#a30ca67432373107948926c646c951237);

161 /\* Pointer to packet to be transmitted \*/

[ 162](structnrf__wifi__off__raw__tx__conf.md#a5a110783498904f3e2a40b1c768a9af2) void \*[pkt](structnrf__wifi__off__raw__tx__conf.md#a5a110783498904f3e2a40b1c768a9af2);

[ 164](structnrf__wifi__off__raw__tx__conf.md#a447104d9cf7cd3ba6b7a50548e940a9e) unsigned int [pkt\_len](structnrf__wifi__off__raw__tx__conf.md#a447104d9cf7cd3ba6b7a50548e940a9e);

165};

166

167

[ 189](group__nrf70__off__raw__tx__api.md#gae92b971e8f9da2237b70ef1117f2db81)int [nrf70\_off\_raw\_tx\_init](group__nrf70__off__raw__tx__api.md#gae92b971e8f9da2237b70ef1117f2db81)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*mac\_addr, unsigned char \*country\_code);

190

[ 197](group__nrf70__off__raw__tx__api.md#gaeec6aa07ed4904d85a627fc06e230b54)void [nrf70\_off\_raw\_tx\_deinit](group__nrf70__off__raw__tx__api.md#gaeec6aa07ed4904d85a627fc06e230b54)(void);

198

[ 210](group__nrf70__off__raw__tx__api.md#ga7b49f9fccf1e3b70d2ccdd1d5014f919)int [nrf70\_off\_raw\_tx\_conf\_update](group__nrf70__off__raw__tx__api.md#ga7b49f9fccf1e3b70d2ccdd1d5014f919)(struct [nrf\_wifi\_off\_raw\_tx\_conf](structnrf__wifi__off__raw__tx__conf.md) \*conf);

211

[ 222](group__nrf70__off__raw__tx__api.md#gadc830596fc31ceb1411de20862bb1fe6)int [nrf70\_off\_raw\_tx\_start](group__nrf70__off__raw__tx__api.md#gadc830596fc31ceb1411de20862bb1fe6)(struct [nrf\_wifi\_off\_raw\_tx\_conf](structnrf__wifi__off__raw__tx__conf.md) \*conf);

223

[ 233](group__nrf70__off__raw__tx__api.md#ga80fa22a8e47b3a97c13e172ea143b888)int [nrf70\_off\_raw\_tx\_stop](group__nrf70__off__raw__tx__api.md#ga80fa22a8e47b3a97c13e172ea143b888)(void);

234

[ 246](group__nrf70__off__raw__tx__api.md#gaa4cb9cb754a79c7d92bebf43cff790f2)int [nrf70\_off\_raw\_tx\_mac\_addr\_get](group__nrf70__off__raw__tx__api.md#gaa4cb9cb754a79c7d92bebf43cff790f2)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*mac\_addr);

247

[ 258](group__nrf70__off__raw__tx__api.md#ga144f311e93e0d77d3bf47c35f7963cd1)int [nrf70\_off\_raw\_tx\_stats](group__nrf70__off__raw__tx__api.md#ga144f311e93e0d77d3bf47c35f7963cd1)(struct [nrf\_wifi\_off\_raw\_tx\_stats](structnrf__wifi__off__raw__tx__stats.md) \*off\_raw\_tx\_stats);

262#endif /\* INCLUDE\_ZEPHYR\_DRIVERS\_OFF\_RAW\_TX\_API\_H\_ \*/

[nrf70\_off\_raw\_tx\_stats](group__nrf70__off__raw__tx__api.md#ga144f311e93e0d77d3bf47c35f7963cd1)

int nrf70\_off\_raw\_tx\_stats(struct nrf\_wifi\_off\_raw\_tx\_stats \*off\_raw\_tx\_stats)

Get statistics of the offloaded raw TX.

[nrf\_wifi\_off\_raw\_tx\_rate](group__nrf70__off__raw__tx__api.md#ga3370994917570dfe6ff14b0c5ecd123d)

nrf\_wifi\_off\_raw\_tx\_rate

Transmission rates Rate to be used for transmitting a packet.

**Definition** off\_raw\_tx\_api.h:31

[nrf\_wifi\_off\_raw\_tx\_tput\_mode](group__nrf70__off__raw__tx__api.md#ga4c785f4ac1c2f8c81be4e39f76a54131)

nrf\_wifi\_off\_raw\_tx\_tput\_mode

Throughput mode Throughput mode to be used for transmitting the packet.

**Definition** off\_raw\_tx\_api.h:112

[nrf70\_off\_raw\_tx\_conf\_update](group__nrf70__off__raw__tx__api.md#ga7b49f9fccf1e3b70d2ccdd1d5014f919)

int nrf70\_off\_raw\_tx\_conf\_update(struct nrf\_wifi\_off\_raw\_tx\_conf \*conf)

Update the configured offloaded raw TX parameters.

[nrf\_wifi\_off\_raw\_tx\_he\_gi](group__nrf70__off__raw__tx__api.md#ga7cc32e6229ddd41db7d310f29a3fc09d)

nrf\_wifi\_off\_raw\_tx\_he\_gi

HE guard interval value Value of the guard interval to be used between symbols when transmitting usin...

**Definition** off\_raw\_tx\_api.h:81

[nrf70\_off\_raw\_tx\_stop](group__nrf70__off__raw__tx__api.md#ga80fa22a8e47b3a97c13e172ea143b888)

int nrf70\_off\_raw\_tx\_stop(void)

Stop the offloaded raw TX.

[nrf\_wifi\_off\_raw\_tx\_he\_ltf](group__nrf70__off__raw__tx__api.md#ga87b545520cdcc2ed387ebed770420c61)

nrf\_wifi\_off\_raw\_tx\_he\_ltf

HE long training field duration Value of the long training field duration to be used when transmittin...

**Definition** off\_raw\_tx\_api.h:97

[nrf70\_off\_raw\_tx\_mac\_addr\_get](group__nrf70__off__raw__tx__api.md#gaa4cb9cb754a79c7d92bebf43cff790f2)

int nrf70\_off\_raw\_tx\_mac\_addr\_get(uint8\_t \*mac\_addr)

Get the MAC address of the nRF70 device.

[nrf70\_off\_raw\_tx\_start](group__nrf70__off__raw__tx__api.md#gadc830596fc31ceb1411de20862bb1fe6)

int nrf70\_off\_raw\_tx\_start(struct nrf\_wifi\_off\_raw\_tx\_conf \*conf)

Start the offloaded raw TX.

[nrf70\_off\_raw\_tx\_init](group__nrf70__off__raw__tx__api.md#gae92b971e8f9da2237b70ef1117f2db81)

int nrf70\_off\_raw\_tx\_init(uint8\_t \*mac\_addr, unsigned char \*country\_code)

Initialize the nRF70 for operating in the offloaded raw TX mode.

[nrf70\_off\_raw\_tx\_deinit](group__nrf70__off__raw__tx__api.md#gaeec6aa07ed4904d85a627fc06e230b54)

void nrf70\_off\_raw\_tx\_deinit(void)

Initialize the nRF70 for operating in the offloaded raw TX mode.

[RATE\_54M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da05960a1ad3453423c65ff0e5d774bf3e)

@ RATE\_54M

54 Mbps

**Definition** off\_raw\_tx\_api.h:55

[RATE\_12M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da0657fa7fa3d22e8c7113754a26541d76)

@ RATE\_12M

12 Mbps

**Definition** off\_raw\_tx\_api.h:45

[RATE\_6M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da20cc375919c198887fcbc8da795eec49)

@ RATE\_6M

6 Mbps

**Definition** off\_raw\_tx\_api.h:41

[RATE\_MCS1](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da289e2a220decd89241fe02c0d033d04b)

@ RATE\_MCS1

MCS 1.

**Definition** off\_raw\_tx\_api.h:59

[RATE\_MCS6](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da2d3d9d6eb775d5b2856de24a3359942a)

@ RATE\_MCS6

MCS 6.

**Definition** off\_raw\_tx\_api.h:69

[RATE\_5\_5M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da4e03ebda6563231013ffd799f28d2e29)

@ RATE\_5\_5M

5.5 Mbps

**Definition** off\_raw\_tx\_api.h:37

[RATE\_9M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da60095536fa78d822f490296fe5a131af)

@ RATE\_9M

9 Mbps

**Definition** off\_raw\_tx\_api.h:43

[RATE\_MCS3](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da661c627527435aaa5f47cb90c922bf7e)

@ RATE\_MCS3

MCS 3.

**Definition** off\_raw\_tx\_api.h:63

[RATE\_MCS0](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da755b9128a7146e4a2084d02a8d2d5760)

@ RATE\_MCS0

MCS 0.

**Definition** off\_raw\_tx\_api.h:57

[RATE\_1M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da77f65aafc9e4063c00b3864f49c179da)

@ RATE\_1M

1 Mbps

**Definition** off\_raw\_tx\_api.h:33

[RATE\_48M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da851615a4ce04de41e72adf7c91bbbe11)

@ RATE\_48M

48 Mbps

**Definition** off\_raw\_tx\_api.h:53

[RATE\_18M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123daaeb9a1cc5312660ed227c28fa52e03f3)

@ RATE\_18M

18 Mbps

**Definition** off\_raw\_tx\_api.h:47

[RATE\_24M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123dab45ef31556754a8a79ebae9ca1082148)

@ RATE\_24M

24 Mbps

**Definition** off\_raw\_tx\_api.h:49

[RATE\_11M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123dab7398b3c15bfd6d39711e8a89b7d3b06)

@ RATE\_11M

11 Mbps

**Definition** off\_raw\_tx\_api.h:39

[RATE\_2M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123dacb4eb3c940da0cfa69cb0e57f8bbbef4)

@ RATE\_2M

2 Mbps

**Definition** off\_raw\_tx\_api.h:35

[RATE\_MCS2](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123dad123030681213480f5bebd7a3e6de676)

@ RATE\_MCS2

MCS 2.

**Definition** off\_raw\_tx\_api.h:61

[RATE\_36M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123dadc7638f55562af7781e0a4b08118477c)

@ RATE\_36M

36 Mbps

**Definition** off\_raw\_tx\_api.h:51

[RATE\_MCS5](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123dae1274d875d22d0079a9e3b64ea979e1b)

@ RATE\_MCS5

MCS 5.

**Definition** off\_raw\_tx\_api.h:67

[RATE\_MCS7](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123daf5b862e8fcaae4a26a415741eaf40de1)

@ RATE\_MCS7

MCS 7.

**Definition** off\_raw\_tx\_api.h:71

[RATE\_MAX](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123daf90f54fa68da0241bf9055a23e3f43ab)

@ RATE\_MAX

Invalid rate.

**Definition** off\_raw\_tx\_api.h:73

[RATE\_MCS4](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123dafdc18a82657bc74a3ea15a459f1366fd)

@ RATE\_MCS4

MCS 4.

**Definition** off\_raw\_tx\_api.h:65

[TPUT\_MODE\_HT](group__nrf70__off__raw__tx__api.md#gga4c785f4ac1c2f8c81be4e39f76a54131a2e61c593601ecb2a30ffe58c8a88a72e)

@ TPUT\_MODE\_HT

High Throughput mode (11n).

**Definition** off\_raw\_tx\_api.h:116

[TPUT\_MODE\_HE\_TB](group__nrf70__off__raw__tx__api.md#gga4c785f4ac1c2f8c81be4e39f76a54131a3989864c3272ca71728b6baa6bfdbd3e)

@ TPUT\_MODE\_HE\_TB

HE TB mode.

**Definition** off\_raw\_tx\_api.h:124

[TPUT\_MODE\_MAX](group__nrf70__off__raw__tx__api.md#gga4c785f4ac1c2f8c81be4e39f76a54131a4cd1f38b7adc6a1722903963bc8876ac)

@ TPUT\_MODE\_MAX

Highest throughput mode currently defined.

**Definition** off\_raw\_tx\_api.h:126

[TPUT\_MODE\_LEGACY](group__nrf70__off__raw__tx__api.md#gga4c785f4ac1c2f8c81be4e39f76a54131aa2cafbe7518c4c690fda12ca6bdc9023)

@ TPUT\_MODE\_LEGACY

Legacy mode.

**Definition** off\_raw\_tx\_api.h:114

[TPUT\_MODE\_HE\_SU](group__nrf70__off__raw__tx__api.md#gga4c785f4ac1c2f8c81be4e39f76a54131abe6d341d6c32b9fb1d5f2658b687f9dd)

@ TPUT\_MODE\_HE\_SU

HE SU mode.

**Definition** off\_raw\_tx\_api.h:120

[TPUT\_MODE\_HE\_ER\_SU](group__nrf70__off__raw__tx__api.md#gga4c785f4ac1c2f8c81be4e39f76a54131ace4701907a49d610806d61eafd3dd6c6)

@ TPUT\_MODE\_HE\_ER\_SU

HE ER SU mode.

**Definition** off\_raw\_tx\_api.h:122

[TPUT\_MODE\_VHT](group__nrf70__off__raw__tx__api.md#gga4c785f4ac1c2f8c81be4e39f76a54131aeb282682e2bfa2e610cf0e2b2822d21e)

@ TPUT\_MODE\_VHT

Very high throughput mode (11ac).

**Definition** off\_raw\_tx\_api.h:118

[HE\_GI\_MAX](group__nrf70__off__raw__tx__api.md#gga7cc32e6229ddd41db7d310f29a3fc09da132ff7b3dfe33b1f49f7c5e87b95264c)

@ HE\_GI\_MAX

Invalid value.

**Definition** off\_raw\_tx\_api.h:89

[HE\_GI\_3200NS](group__nrf70__off__raw__tx__api.md#gga7cc32e6229ddd41db7d310f29a3fc09da14c3bac543f5c886265a22bb77f47b71)

@ HE\_GI\_3200NS

3200 ns

**Definition** off\_raw\_tx\_api.h:87

[HE\_GI\_1600NS](group__nrf70__off__raw__tx__api.md#gga7cc32e6229ddd41db7d310f29a3fc09da7fad526cc4b6544d13f688395229336f)

@ HE\_GI\_1600NS

1600 ns

**Definition** off\_raw\_tx\_api.h:85

[HE\_GI\_800NS](group__nrf70__off__raw__tx__api.md#gga7cc32e6229ddd41db7d310f29a3fc09da991485bf09a58a8f9b1751d5c0781598)

@ HE\_GI\_800NS

800 ns

**Definition** off\_raw\_tx\_api.h:83

[HE\_LTF\_12800NS](group__nrf70__off__raw__tx__api.md#gga87b545520cdcc2ed387ebed770420c61a204188c45996539fa1b6141ed40f3448)

@ HE\_LTF\_12800NS

12.8us

**Definition** off\_raw\_tx\_api.h:103

[HE\_LTF\_6400NS](group__nrf70__off__raw__tx__api.md#gga87b545520cdcc2ed387ebed770420c61ab3d148ec3de601ae0b10538edf1bb7e2)

@ HE\_LTF\_6400NS

6.4us

**Definition** off\_raw\_tx\_api.h:101

[HE\_LTF\_MAX](group__nrf70__off__raw__tx__api.md#gga87b545520cdcc2ed387ebed770420c61ae0b112fb129512eeef0bebc6956281cd)

@ HE\_LTF\_MAX

Invalid value.

**Definition** off\_raw\_tx\_api.h:105

[HE\_LTF\_3200NS](group__nrf70__off__raw__tx__api.md#gga87b545520cdcc2ed387ebed770420c61ae6ec0118f3e5c10892790e2cbea4d701)

@ HE\_LTF\_3200NS

3.2us

**Definition** off\_raw\_tx\_api.h:99

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[nrf\_wifi\_off\_raw\_tx\_conf](structnrf__wifi__off__raw__tx__conf.md)

Configuration parameters for offloaded raw TX Parameters which can be used to configure the offloaded...

**Definition** off\_raw\_tx\_api.h:142

[nrf\_wifi\_off\_raw\_tx\_conf::period\_us](structnrf__wifi__off__raw__tx__conf.md#a2a772fb8c30ac44592a437d9782d76cf)

unsigned int period\_us

Time interval (in microseconds) between transmissions.

**Definition** off\_raw\_tx\_api.h:144

[nrf\_wifi\_off\_raw\_tx\_conf::he\_ltf](structnrf__wifi__off__raw__tx__conf.md#a30ca67432373107948926c646c951237)

enum nrf\_wifi\_off\_raw\_tx\_he\_ltf he\_ltf

HE GI.

**Definition** off\_raw\_tx\_api.h:160

[nrf\_wifi\_off\_raw\_tx\_conf::tx\_pwr](structnrf__wifi__off__raw__tx__conf.md#a328e1b3b7411e5685683c8718a05173e)

unsigned int tx\_pwr

Transmit power in dBm (0 to 20).

**Definition** off\_raw\_tx\_api.h:146

[nrf\_wifi\_off\_raw\_tx\_conf::he\_gi](structnrf__wifi__off__raw__tx__conf.md#a3e56b1bf386d483d0f6eb04b00c46cac)

enum nrf\_wifi\_off\_raw\_tx\_he\_gi he\_gi

HE GI.

**Definition** off\_raw\_tx\_api.h:158

[nrf\_wifi\_off\_raw\_tx\_conf::pkt\_len](structnrf__wifi__off__raw__tx__conf.md#a447104d9cf7cd3ba6b7a50548e940a9e)

unsigned int pkt\_len

Packet length of the frame to be transmitted, (min 26 bytes and max 600 bytes).

**Definition** off\_raw\_tx\_api.h:164

[nrf\_wifi\_off\_raw\_tx\_conf::rate](structnrf__wifi__off__raw__tx__conf.md#a52419b8149b390888491511413e17f98)

enum nrf\_wifi\_off\_raw\_tx\_rate rate

**Definition** off\_raw\_tx\_api.h:156

[nrf\_wifi\_off\_raw\_tx\_conf::pkt](structnrf__wifi__off__raw__tx__conf.md#a5a110783498904f3e2a40b1c768a9af2)

void \* pkt

**Definition** off\_raw\_tx\_api.h:162

[nrf\_wifi\_off\_raw\_tx\_conf::tput\_mode](structnrf__wifi__off__raw__tx__conf.md#a631f15bbd4930256b3b6f64175a630b7)

enum nrf\_wifi\_off\_raw\_tx\_tput\_mode tput\_mode

Throughput mode for packet transmittion.

**Definition** off\_raw\_tx\_api.h:154

[nrf\_wifi\_off\_raw\_tx\_conf::short\_preamble](structnrf__wifi__off__raw__tx__conf.md#a907d509fb2988e5003120ccff4f24932)

bool short\_preamble

Set to TRUE to use short preamble for FALSE to disable short preamble.

**Definition** off\_raw\_tx\_api.h:150

[nrf\_wifi\_off\_raw\_tx\_conf::num\_retries](structnrf__wifi__off__raw__tx__conf.md#ab88c522e97c5f624b78133a3d184ebd0)

unsigned int num\_retries

**Definition** off\_raw\_tx\_api.h:152

[nrf\_wifi\_off\_raw\_tx\_conf::chan](structnrf__wifi__off__raw__tx__conf.md#abff388f54589d410b10e2e55a4574314)

unsigned int chan

Channel number on which to transmit.

**Definition** off\_raw\_tx\_api.h:148

[nrf\_wifi\_off\_raw\_tx\_stats](structnrf__wifi__off__raw__tx__stats.md)

This structure defines the Offloaded raw tx debug statistics.

**Definition** off\_raw\_tx\_api.h:133

[nrf\_wifi\_off\_raw\_tx\_stats::off\_raw\_tx\_pkt\_sent](structnrf__wifi__off__raw__tx__stats.md#a4b4ec40c9c58f1c004182b8be773e838)

unsigned int off\_raw\_tx\_pkt\_sent

Number of packets sent.

**Definition** off\_raw\_tx\_api.h:135

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [wifi](dir_478165533ab14baf575002d17a842a12.md)
- [nrfwifi](dir_c91d2a2631cf359b4e5400921c6df939.md)
- [off\_raw\_tx](dir_5b827d67886bcec2df18bed4a6a0ce24.md)
- [off\_raw\_tx\_api.h](off__raw__tx__api_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

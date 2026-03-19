---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/off__raw__tx__api_8h.html
original_path: doxygen/html/off__raw__tx__api_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

off\_raw\_tx\_api.h File Reference

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](off__raw__tx__api_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [nrf\_wifi\_off\_raw\_tx\_stats](structnrf__wifi__off__raw__tx__stats.md) |
|  | This structure defines the Offloaded raw tx debug statistics. [More...](structnrf__wifi__off__raw__tx__stats.md#details) |
| struct | [nrf\_wifi\_off\_raw\_tx\_conf](structnrf__wifi__off__raw__tx__conf.md) |
|  | - Configuration parameters for offloaded raw TX Parameters which can be used to configure the offloaded raw TX operation.  [More...](structnrf__wifi__off__raw__tx__conf.md#details) |

| Macros | |
| --- | --- |
| #define | [NRF\_WIFI\_OFF\_RAW\_TX\_FRAME\_SIZE\_MIN](group__nrf70__off__raw__tx__api.md#gae2e1b9b12b8e4478e994d76888f40900)   26 |
| #define | [NRF\_WIFI\_OFF\_RAW\_TX\_FRAME\_SIZE\_MAX](group__nrf70__off__raw__tx__api.md#ga83452cafd85400cf926c656201d77959)   600 |
| #define | [NRF\_WIFI\_COUNTRY\_CODE\_LEN](group__nrf70__off__raw__tx__api.md#ga55204b43c73489568ea1af9cee7ff130)   2 |

| Enumerations | |
| --- | --- |
| enum | [nrf\_wifi\_off\_raw\_tx\_rate](group__nrf70__off__raw__tx__api.md#ga3370994917570dfe6ff14b0c5ecd123d) {     [RATE\_1M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da77f65aafc9e4063c00b3864f49c179da) , [RATE\_2M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123dacb4eb3c940da0cfa69cb0e57f8bbbef4) , [RATE\_5\_5M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da4e03ebda6563231013ffd799f28d2e29) , [RATE\_11M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123dab7398b3c15bfd6d39711e8a89b7d3b06) ,     [RATE\_6M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da20cc375919c198887fcbc8da795eec49) , [RATE\_9M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da60095536fa78d822f490296fe5a131af) , [RATE\_12M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da0657fa7fa3d22e8c7113754a26541d76) , [RATE\_18M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123daaeb9a1cc5312660ed227c28fa52e03f3) ,     [RATE\_24M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123dab45ef31556754a8a79ebae9ca1082148) , [RATE\_36M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123dadc7638f55562af7781e0a4b08118477c) , [RATE\_48M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da851615a4ce04de41e72adf7c91bbbe11) , [RATE\_54M](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da05960a1ad3453423c65ff0e5d774bf3e) ,     [RATE\_MCS0](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da755b9128a7146e4a2084d02a8d2d5760) , [RATE\_MCS1](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da289e2a220decd89241fe02c0d033d04b) , [RATE\_MCS2](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123dad123030681213480f5bebd7a3e6de676) , [RATE\_MCS3](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da661c627527435aaa5f47cb90c922bf7e) ,     [RATE\_MCS4](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123dafdc18a82657bc74a3ea15a459f1366fd) , [RATE\_MCS5](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123dae1274d875d22d0079a9e3b64ea979e1b) , [RATE\_MCS6](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123da2d3d9d6eb775d5b2856de24a3359942a) , [RATE\_MCS7](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123daf5b862e8fcaae4a26a415741eaf40de1) ,     [RATE\_MAX](group__nrf70__off__raw__tx__api.md#gga3370994917570dfe6ff14b0c5ecd123daf90f54fa68da0241bf9055a23e3f43ab)   } |
|  | - Transmission rates Rate to be used for transmitting a packet.  [More...](group__nrf70__off__raw__tx__api.md#ga3370994917570dfe6ff14b0c5ecd123d) |
| enum | [nrf\_wifi\_off\_raw\_tx\_he\_gi](group__nrf70__off__raw__tx__api.md#ga7cc32e6229ddd41db7d310f29a3fc09d) { [HE\_GI\_800NS](group__nrf70__off__raw__tx__api.md#gga7cc32e6229ddd41db7d310f29a3fc09da991485bf09a58a8f9b1751d5c0781598) , [HE\_GI\_1600NS](group__nrf70__off__raw__tx__api.md#gga7cc32e6229ddd41db7d310f29a3fc09da7fad526cc4b6544d13f688395229336f) , [HE\_GI\_3200NS](group__nrf70__off__raw__tx__api.md#gga7cc32e6229ddd41db7d310f29a3fc09da14c3bac543f5c886265a22bb77f47b71) , [HE\_GI\_MAX](group__nrf70__off__raw__tx__api.md#gga7cc32e6229ddd41db7d310f29a3fc09da132ff7b3dfe33b1f49f7c5e87b95264c) } |
|  | - HE guard interval value Value of the guard interval to be used between symbols when transmitting using HE.  [More...](group__nrf70__off__raw__tx__api.md#ga7cc32e6229ddd41db7d310f29a3fc09d) |
| enum | [nrf\_wifi\_off\_raw\_tx\_he\_ltf](group__nrf70__off__raw__tx__api.md#ga87b545520cdcc2ed387ebed770420c61) { [HE\_LTF\_3200NS](group__nrf70__off__raw__tx__api.md#gga87b545520cdcc2ed387ebed770420c61ae6ec0118f3e5c10892790e2cbea4d701) , [HE\_LTF\_6400NS](group__nrf70__off__raw__tx__api.md#gga87b545520cdcc2ed387ebed770420c61ab3d148ec3de601ae0b10538edf1bb7e2) , [HE\_LTF\_12800NS](group__nrf70__off__raw__tx__api.md#gga87b545520cdcc2ed387ebed770420c61a204188c45996539fa1b6141ed40f3448) , [HE\_LTF\_MAX](group__nrf70__off__raw__tx__api.md#gga87b545520cdcc2ed387ebed770420c61ae0b112fb129512eeef0bebc6956281cd) } |
|  | - HE long training field duration Value of the long training field duration to be used when transmitting using HE.  [More...](group__nrf70__off__raw__tx__api.md#ga87b545520cdcc2ed387ebed770420c61) |
| enum | [nrf\_wifi\_off\_raw\_tx\_tput\_mode](group__nrf70__off__raw__tx__api.md#ga4c785f4ac1c2f8c81be4e39f76a54131) {     [TPUT\_MODE\_LEGACY](group__nrf70__off__raw__tx__api.md#gga4c785f4ac1c2f8c81be4e39f76a54131aa2cafbe7518c4c690fda12ca6bdc9023) , [TPUT\_MODE\_HT](group__nrf70__off__raw__tx__api.md#gga4c785f4ac1c2f8c81be4e39f76a54131a2e61c593601ecb2a30ffe58c8a88a72e) , [TPUT\_MODE\_VHT](group__nrf70__off__raw__tx__api.md#gga4c785f4ac1c2f8c81be4e39f76a54131aeb282682e2bfa2e610cf0e2b2822d21e) , [TPUT\_MODE\_HE\_SU](group__nrf70__off__raw__tx__api.md#gga4c785f4ac1c2f8c81be4e39f76a54131abe6d341d6c32b9fb1d5f2658b687f9dd) ,     [TPUT\_MODE\_HE\_ER\_SU](group__nrf70__off__raw__tx__api.md#gga4c785f4ac1c2f8c81be4e39f76a54131ace4701907a49d610806d61eafd3dd6c6) , [TPUT\_MODE\_HE\_TB](group__nrf70__off__raw__tx__api.md#gga4c785f4ac1c2f8c81be4e39f76a54131a3989864c3272ca71728b6baa6bfdbd3e) , [TPUT\_MODE\_MAX](group__nrf70__off__raw__tx__api.md#gga4c785f4ac1c2f8c81be4e39f76a54131a4cd1f38b7adc6a1722903963bc8876ac)   } |
|  | - Throughput mode Throughput mode to be used for transmitting the packet.  [More...](group__nrf70__off__raw__tx__api.md#ga4c785f4ac1c2f8c81be4e39f76a54131) |

| Functions | |
| --- | --- |
| int | [nrf70\_off\_raw\_tx\_init](group__nrf70__off__raw__tx__api.md#gae92b971e8f9da2237b70ef1117f2db81) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*mac\_addr, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char \*country\_code) |
|  | Initialize the nRF70 for operating in the offloaded raw TX mode. |
| void | [nrf70\_off\_raw\_tx\_deinit](group__nrf70__off__raw__tx__api.md#gaeec6aa07ed4904d85a627fc06e230b54) (void) |
|  | Initialize the nRF70 for operating in the offloaded raw TX mode. |
| int | [nrf70\_off\_raw\_tx\_conf\_update](group__nrf70__off__raw__tx__api.md#ga7b49f9fccf1e3b70d2ccdd1d5014f919) (struct [nrf\_wifi\_off\_raw\_tx\_conf](structnrf__wifi__off__raw__tx__conf.md) \*conf) |
|  | Update the configured offloaded raw TX parameters. |
| int | [nrf70\_off\_raw\_tx\_start](group__nrf70__off__raw__tx__api.md#gadc830596fc31ceb1411de20862bb1fe6) (struct [nrf\_wifi\_off\_raw\_tx\_conf](structnrf__wifi__off__raw__tx__conf.md) \*conf) |
|  | Start the offloaded raw TX. |
| int | [nrf70\_off\_raw\_tx\_stop](group__nrf70__off__raw__tx__api.md#ga80fa22a8e47b3a97c13e172ea143b888) (void) |
|  | Stop the offloaded raw TX. |
| int | [nrf70\_off\_raw\_tx\_mac\_addr\_get](group__nrf70__off__raw__tx__api.md#gaa4cb9cb754a79c7d92bebf43cff790f2) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*mac\_addr) |
|  | Get the MAC address of the nRF70 device. |
| int | [nrf70\_off\_raw\_tx\_stats](group__nrf70__off__raw__tx__api.md#ga144f311e93e0d77d3bf47c35f7963cd1) (struct [nrf\_wifi\_off\_raw\_tx\_stats](structnrf__wifi__off__raw__tx__stats.md) \*off\_raw\_tx\_stats) |
|  | Get statistics of the offloaded raw TX. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [wifi](dir_478165533ab14baf575002d17a842a12.md)
- [nrf\_wifi](dir_827a5ceb820ded32f2709b259acb2436.md)
- [off\_raw\_tx](dir_3fae98f0cbcd50766b2608f215856819.md)
- [off\_raw\_tx\_api.h](off__raw__tx__api_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

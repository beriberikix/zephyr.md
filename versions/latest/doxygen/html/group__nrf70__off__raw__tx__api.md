---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__nrf70__off__raw__tx__api.html
original_path: doxygen/html/group__nrf70__off__raw__tx__api.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nRF70 Offloaded raw TX API

File containing API's for the Offloaded raw TX feature.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [nrf\_wifi\_off\_raw\_tx\_stats](structnrf__wifi__off__raw__tx__stats.md) |
|  | This structure defines the Offloaded raw tx debug statistics. [More...](structnrf__wifi__off__raw__tx__stats.md#details) |
| struct | [nrf\_wifi\_off\_raw\_tx\_conf](structnrf__wifi__off__raw__tx__conf.md) |
|  | - Configuration parameters for offloaded raw TX Parameters which can be used to configure the offloaded raw TX operation.  [More...](structnrf__wifi__off__raw__tx__conf.md#details) |

| Macros | |
| --- | --- |
| #define | [NRF\_WIFI\_OFF\_RAW\_TX\_FRAME\_SIZE\_MIN](#gae2e1b9b12b8e4478e994d76888f40900)   26 |
| #define | [NRF\_WIFI\_OFF\_RAW\_TX\_FRAME\_SIZE\_MAX](#ga83452cafd85400cf926c656201d77959)   600 |
| #define | [NRF\_WIFI\_COUNTRY\_CODE\_LEN](#ga55204b43c73489568ea1af9cee7ff130)   2 |

| Enumerations | |
| --- | --- |
| enum | [nrf\_wifi\_off\_raw\_tx\_rate](#ga3370994917570dfe6ff14b0c5ecd123d) {     [RATE\_1M](#gga3370994917570dfe6ff14b0c5ecd123da77f65aafc9e4063c00b3864f49c179da) , [RATE\_2M](#gga3370994917570dfe6ff14b0c5ecd123dacb4eb3c940da0cfa69cb0e57f8bbbef4) , [RATE\_5\_5M](#gga3370994917570dfe6ff14b0c5ecd123da4e03ebda6563231013ffd799f28d2e29) , [RATE\_11M](#gga3370994917570dfe6ff14b0c5ecd123dab7398b3c15bfd6d39711e8a89b7d3b06) ,     [RATE\_6M](#gga3370994917570dfe6ff14b0c5ecd123da20cc375919c198887fcbc8da795eec49) , [RATE\_9M](#gga3370994917570dfe6ff14b0c5ecd123da60095536fa78d822f490296fe5a131af) , [RATE\_12M](#gga3370994917570dfe6ff14b0c5ecd123da0657fa7fa3d22e8c7113754a26541d76) , [RATE\_18M](#gga3370994917570dfe6ff14b0c5ecd123daaeb9a1cc5312660ed227c28fa52e03f3) ,     [RATE\_24M](#gga3370994917570dfe6ff14b0c5ecd123dab45ef31556754a8a79ebae9ca1082148) , [RATE\_36M](#gga3370994917570dfe6ff14b0c5ecd123dadc7638f55562af7781e0a4b08118477c) , [RATE\_48M](#gga3370994917570dfe6ff14b0c5ecd123da851615a4ce04de41e72adf7c91bbbe11) , [RATE\_54M](#gga3370994917570dfe6ff14b0c5ecd123da05960a1ad3453423c65ff0e5d774bf3e) ,     [RATE\_MCS0](#gga3370994917570dfe6ff14b0c5ecd123da755b9128a7146e4a2084d02a8d2d5760) , [RATE\_MCS1](#gga3370994917570dfe6ff14b0c5ecd123da289e2a220decd89241fe02c0d033d04b) , [RATE\_MCS2](#gga3370994917570dfe6ff14b0c5ecd123dad123030681213480f5bebd7a3e6de676) , [RATE\_MCS3](#gga3370994917570dfe6ff14b0c5ecd123da661c627527435aaa5f47cb90c922bf7e) ,     [RATE\_MCS4](#gga3370994917570dfe6ff14b0c5ecd123dafdc18a82657bc74a3ea15a459f1366fd) , [RATE\_MCS5](#gga3370994917570dfe6ff14b0c5ecd123dae1274d875d22d0079a9e3b64ea979e1b) , [RATE\_MCS6](#gga3370994917570dfe6ff14b0c5ecd123da2d3d9d6eb775d5b2856de24a3359942a) , [RATE\_MCS7](#gga3370994917570dfe6ff14b0c5ecd123daf5b862e8fcaae4a26a415741eaf40de1) ,     [RATE\_MAX](#gga3370994917570dfe6ff14b0c5ecd123daf90f54fa68da0241bf9055a23e3f43ab)   } |
|  | - Transmission rates Rate to be used for transmitting a packet.  [More...](#ga3370994917570dfe6ff14b0c5ecd123d) |
| enum | [nrf\_wifi\_off\_raw\_tx\_he\_gi](#ga7cc32e6229ddd41db7d310f29a3fc09d) { [HE\_GI\_800NS](#gga7cc32e6229ddd41db7d310f29a3fc09da991485bf09a58a8f9b1751d5c0781598) , [HE\_GI\_1600NS](#gga7cc32e6229ddd41db7d310f29a3fc09da7fad526cc4b6544d13f688395229336f) , [HE\_GI\_3200NS](#gga7cc32e6229ddd41db7d310f29a3fc09da14c3bac543f5c886265a22bb77f47b71) , [HE\_GI\_MAX](#gga7cc32e6229ddd41db7d310f29a3fc09da132ff7b3dfe33b1f49f7c5e87b95264c) } |
|  | - HE guard interval value Value of the guard interval to be used between symbols when transmitting using HE.  [More...](#ga7cc32e6229ddd41db7d310f29a3fc09d) |
| enum | [nrf\_wifi\_off\_raw\_tx\_he\_ltf](#ga87b545520cdcc2ed387ebed770420c61) { [HE\_LTF\_3200NS](#gga87b545520cdcc2ed387ebed770420c61ae6ec0118f3e5c10892790e2cbea4d701) , [HE\_LTF\_6400NS](#gga87b545520cdcc2ed387ebed770420c61ab3d148ec3de601ae0b10538edf1bb7e2) , [HE\_LTF\_12800NS](#gga87b545520cdcc2ed387ebed770420c61a204188c45996539fa1b6141ed40f3448) , [HE\_LTF\_MAX](#gga87b545520cdcc2ed387ebed770420c61ae0b112fb129512eeef0bebc6956281cd) } |
|  | - HE long training field duration Value of the long training field duration to be used when transmitting using HE.  [More...](#ga87b545520cdcc2ed387ebed770420c61) |
| enum | [nrf\_wifi\_off\_raw\_tx\_tput\_mode](#ga4c785f4ac1c2f8c81be4e39f76a54131) {     [TPUT\_MODE\_LEGACY](#gga4c785f4ac1c2f8c81be4e39f76a54131aa2cafbe7518c4c690fda12ca6bdc9023) , [TPUT\_MODE\_HT](#gga4c785f4ac1c2f8c81be4e39f76a54131a2e61c593601ecb2a30ffe58c8a88a72e) , [TPUT\_MODE\_VHT](#gga4c785f4ac1c2f8c81be4e39f76a54131aeb282682e2bfa2e610cf0e2b2822d21e) , [TPUT\_MODE\_HE\_SU](#gga4c785f4ac1c2f8c81be4e39f76a54131abe6d341d6c32b9fb1d5f2658b687f9dd) ,     [TPUT\_MODE\_HE\_ER\_SU](#gga4c785f4ac1c2f8c81be4e39f76a54131ace4701907a49d610806d61eafd3dd6c6) , [TPUT\_MODE\_HE\_TB](#gga4c785f4ac1c2f8c81be4e39f76a54131a3989864c3272ca71728b6baa6bfdbd3e) , [TPUT\_MODE\_MAX](#gga4c785f4ac1c2f8c81be4e39f76a54131a4cd1f38b7adc6a1722903963bc8876ac)   } |
|  | - Throughput mode Throughput mode to be used for transmitting the packet.  [More...](#ga4c785f4ac1c2f8c81be4e39f76a54131) |

| Functions | |
| --- | --- |
| int | [nrf70\_off\_raw\_tx\_init](#gae92b971e8f9da2237b70ef1117f2db81) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*mac\_addr, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char \*country\_code) |
|  | Initialize the nRF70 for operating in the offloaded raw TX mode. |
| void | [nrf70\_off\_raw\_tx\_deinit](#gaeec6aa07ed4904d85a627fc06e230b54) (void) |
|  | Initialize the nRF70 for operating in the offloaded raw TX mode. |
| int | [nrf70\_off\_raw\_tx\_conf\_update](#ga7b49f9fccf1e3b70d2ccdd1d5014f919) (struct [nrf\_wifi\_off\_raw\_tx\_conf](structnrf__wifi__off__raw__tx__conf.md) \*conf) |
|  | Update the configured offloaded raw TX parameters. |
| int | [nrf70\_off\_raw\_tx\_start](#gadc830596fc31ceb1411de20862bb1fe6) (struct [nrf\_wifi\_off\_raw\_tx\_conf](structnrf__wifi__off__raw__tx__conf.md) \*conf) |
|  | Start the offloaded raw TX. |
| int | [nrf70\_off\_raw\_tx\_stop](#ga80fa22a8e47b3a97c13e172ea143b888) (void) |
|  | Stop the offloaded raw TX. |
| int | [nrf70\_off\_raw\_tx\_mac\_addr\_get](#gaa4cb9cb754a79c7d92bebf43cff790f2) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*mac\_addr) |
|  | Get the MAC address of the nRF70 device. |
| int | [nrf70\_off\_raw\_tx\_stats](#ga144f311e93e0d77d3bf47c35f7963cd1) (struct [nrf\_wifi\_off\_raw\_tx\_stats](structnrf__wifi__off__raw__tx__stats.md) \*off\_raw\_tx\_stats) |
|  | Get statistics of the offloaded raw TX. |

## Detailed Description

File containing API's for the Offloaded raw TX feature.

## Macro Definition Documentation

## [◆ ](#ga55204b43c73489568ea1af9cee7ff130)NRF\_WIFI\_COUNTRY\_CODE\_LEN

| #define NRF\_WIFI\_COUNTRY\_CODE\_LEN   2 |
| --- |

`#include <[off_raw_tx_api.h](off__raw__tx__api_8h.md)>`

## [◆ ](#ga83452cafd85400cf926c656201d77959)NRF\_WIFI\_OFF\_RAW\_TX\_FRAME\_SIZE\_MAX

| #define NRF\_WIFI\_OFF\_RAW\_TX\_FRAME\_SIZE\_MAX   600 |
| --- |

`#include <[off_raw_tx_api.h](off__raw__tx__api_8h.md)>`

## [◆ ](#gae2e1b9b12b8e4478e994d76888f40900)NRF\_WIFI\_OFF\_RAW\_TX\_FRAME\_SIZE\_MIN

| #define NRF\_WIFI\_OFF\_RAW\_TX\_FRAME\_SIZE\_MIN   26 |
| --- |

`#include <[off_raw_tx_api.h](off__raw__tx__api_8h.md)>`

## Enumeration Type Documentation

## [◆ ](#ga7cc32e6229ddd41db7d310f29a3fc09d)nrf\_wifi\_off\_raw\_tx\_he\_gi

| enum [nrf\_wifi\_off\_raw\_tx\_he\_gi](#ga7cc32e6229ddd41db7d310f29a3fc09d) |
| --- |

`#include <[off_raw_tx_api.h](off__raw__tx__api_8h.md)>`

- HE guard interval value Value of the guard interval to be used between symbols when transmitting using HE.

| Enumerator | |
| --- | --- |
| HE\_GI\_800NS | 800 ns |
| HE\_GI\_1600NS | 1600 ns |
| HE\_GI\_3200NS | 3200 ns |
| HE\_GI\_MAX | Invalid value. |

## [◆ ](#ga87b545520cdcc2ed387ebed770420c61)nrf\_wifi\_off\_raw\_tx\_he\_ltf

| enum [nrf\_wifi\_off\_raw\_tx\_he\_ltf](#ga87b545520cdcc2ed387ebed770420c61) |
| --- |

`#include <[off_raw_tx_api.h](off__raw__tx__api_8h.md)>`

- HE long training field duration Value of the long training field duration to be used when transmitting using HE.

| Enumerator | |
| --- | --- |
| HE\_LTF\_3200NS | 3.2us |
| HE\_LTF\_6400NS | 6.4us |
| HE\_LTF\_12800NS | 12.8us |
| HE\_LTF\_MAX | Invalid value. |

## [◆ ](#ga3370994917570dfe6ff14b0c5ecd123d)nrf\_wifi\_off\_raw\_tx\_rate

| enum [nrf\_wifi\_off\_raw\_tx\_rate](#ga3370994917570dfe6ff14b0c5ecd123d) |
| --- |

`#include <[off_raw_tx_api.h](off__raw__tx__api_8h.md)>`

- Transmission rates Rate to be used for transmitting a packet.

| Enumerator | |
| --- | --- |
| RATE\_1M | 1 Mbps |
| RATE\_2M | 2 Mbps |
| RATE\_5\_5M | 5.5 Mbps |
| RATE\_11M | 11 Mbps |
| RATE\_6M | 6 Mbps |
| RATE\_9M | 9 Mbps |
| RATE\_12M | 12 Mbps |
| RATE\_18M | 18 Mbps |
| RATE\_24M | 24 Mbps |
| RATE\_36M | 36 Mbps |
| RATE\_48M | 48 Mbps |
| RATE\_54M | 54 Mbps |
| RATE\_MCS0 | MCS 0. |
| RATE\_MCS1 | MCS 1. |
| RATE\_MCS2 | MCS 2. |
| RATE\_MCS3 | MCS 3. |
| RATE\_MCS4 | MCS 4. |
| RATE\_MCS5 | MCS 5. |
| RATE\_MCS6 | MCS 6. |
| RATE\_MCS7 | MCS 7. |
| RATE\_MAX | Invalid rate. |

## [◆ ](#ga4c785f4ac1c2f8c81be4e39f76a54131)nrf\_wifi\_off\_raw\_tx\_tput\_mode

| enum [nrf\_wifi\_off\_raw\_tx\_tput\_mode](#ga4c785f4ac1c2f8c81be4e39f76a54131) |
| --- |

`#include <[off_raw_tx_api.h](off__raw__tx__api_8h.md)>`

- Throughput mode Throughput mode to be used for transmitting the packet.

| Enumerator | |
| --- | --- |
| TPUT\_MODE\_LEGACY | Legacy mode. |
| TPUT\_MODE\_HT | High Throughput mode (11n). |
| TPUT\_MODE\_VHT | Very high throughput mode (11ac). |
| TPUT\_MODE\_HE\_SU | HE SU mode. |
| TPUT\_MODE\_HE\_ER\_SU | HE ER SU mode. |
| TPUT\_MODE\_HE\_TB | HE TB mode. |
| TPUT\_MODE\_MAX | Highest throughput mode currently defined. |

## Function Documentation

## [◆ ](#ga7b49f9fccf1e3b70d2ccdd1d5014f919)nrf70\_off\_raw\_tx\_conf\_update()

| int nrf70\_off\_raw\_tx\_conf\_update | ( | struct [nrf\_wifi\_off\_raw\_tx\_conf](structnrf__wifi__off__raw__tx__conf.md) \* | *conf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[off_raw_tx_api.h](off__raw__tx__api_8h.md)>`

Update the configured offloaded raw TX parameters.

Parameters
:   | conf | Configuration parameters to be updated for the offloaded raw TX operation. |
    | --- | --- |

This function is used to update configured parameters for offloaded raw TX operation. This function should be used to when the parameters need to be updated during an ongoing raw TX operation without having to stop it.

Return values
:   | 0 | If the operation was successful. |
    | --- | --- |
    | -1 | If the operation failed. |

## [◆ ](#gaeec6aa07ed4904d85a627fc06e230b54)nrf70\_off\_raw\_tx\_deinit()

| void nrf70\_off\_raw\_tx\_deinit | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[off_raw_tx_api.h](off__raw__tx__api_8h.md)>`

Initialize the nRF70 for operating in the offloaded raw TX mode.

This function is deinitializes the nRF70 device.

## [◆ ](#gae92b971e8f9da2237b70ef1117f2db81)nrf70\_off\_raw\_tx\_init()

| int nrf70\_off\_raw\_tx\_init | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *mac\_addr*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char \* | *country\_code* ) |

`#include <[off_raw_tx_api.h](off__raw__tx__api_8h.md)>`

Initialize the nRF70 for operating in the offloaded raw TX mode.

Parameters
:   | mac\_addr | MAC address to be used for the nRF70 device. |
    | --- | --- |
    | country\_code | Country code to be set for regularity domain. |

This function is initializes the nRF70 device for offloaded raw TX mode by:

- Powering it up,
- Downloading a firmware patch (if any).
- Initializing the firmware to accept further commands

The mac\_addr parameter is used to set the MAC address of the nRF70 device. This address can be used to override the MAC addresses programmed in the OTP and the value configured (if any) in CONFIG\_WIFI\_FIXED\_MAC\_ADDRESS. The priority order in which the MAC address values for the nRF70 device are used is:

- If mac\_addr is provided, the MAC address is set to the value provided.
- If CONFIG\_WIFI\_FIXED\_MAC\_ADDRESS is enabled, the MAC address uses the Kconfig value.
- If none of the above are provided, the MAC address is set to the value programmed in the OTP.

Return values
:   | 0 | If the operation was successful. |
    | --- | --- |
    | -1 | If the operation failed. |

## [◆ ](#gaa4cb9cb754a79c7d92bebf43cff790f2)nrf70\_off\_raw\_tx\_mac\_addr\_get()

| int nrf70\_off\_raw\_tx\_mac\_addr\_get | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *mac\_addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[off_raw_tx_api.h](off__raw__tx__api_8h.md)>`

Get the MAC address of the nRF70 device.

Parameters
:   | mac\_addr | Buffer to store the MAC address. |
    | --- | --- |

This function is used to get the MAC address of the nRF70 device. The MAC address is stored in the buffer pointed by mac\_addr. The MAC address is expected to be a 6 byte value.

Return values
:   | 0 | If the operation was successful. |
    | --- | --- |
    | -1 | If the operation failed. |

## [◆ ](#gadc830596fc31ceb1411de20862bb1fe6)nrf70\_off\_raw\_tx\_start()

| int nrf70\_off\_raw\_tx\_start | ( | struct [nrf\_wifi\_off\_raw\_tx\_conf](structnrf__wifi__off__raw__tx__conf.md) \* | *conf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[off_raw_tx_api.h](off__raw__tx__api_8h.md)>`

Start the offloaded raw TX.

Parameters
:   | conf | Configuration parameters necessary for the offloaded raw TX operation. |
    | --- | --- |

This function is used to start offloaded raw TX operation. When this function is invoked the nRF70 device will start transmitting frames as per the configuration specified by `conf`.

Return values
:   | 0 | If the operation was successful. |
    | --- | --- |
    | -1 | If the operation failed. |

## [◆ ](#ga144f311e93e0d77d3bf47c35f7963cd1)nrf70\_off\_raw\_tx\_stats()

| int nrf70\_off\_raw\_tx\_stats | ( | struct [nrf\_wifi\_off\_raw\_tx\_stats](structnrf__wifi__off__raw__tx__stats.md) \* | *off\_raw\_tx\_stats* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[off_raw_tx_api.h](off__raw__tx__api_8h.md)>`

Get statistics of the offloaded raw TX.

Parameters
:   | off\_raw\_tx\_stats | Statistics of the offloaded raw TX operation. |
    | --- | --- |

This function is used to get statistics of offloaded raw TX operation. When this function is invoked the nRF70 device will show statistics.

Return values
:   | 0 | If the operation was successful. |
    | --- | --- |
    | -1 | If the operation failed. |

## [◆ ](#ga80fa22a8e47b3a97c13e172ea143b888)nrf70\_off\_raw\_tx\_stop()

| int nrf70\_off\_raw\_tx\_stop | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[off_raw_tx_api.h](off__raw__tx__api_8h.md)>`

Stop the offloaded raw TX.

This function is used to stop offloaded raw TX operation. When this function is invoked the nRF70 device will stop transmitting frames.

Return values
:   | 0 | If the operation was successful. |
    | --- | --- |
    | -1 | If the operation failed. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

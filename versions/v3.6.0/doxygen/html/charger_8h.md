---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/charger_8h.html
original_path: doxygen/html/charger_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

charger.h File Reference

Charger APIs.
[More...](#details)

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <syscalls/charger.h>`

[Go to the source code of this file.](charger_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [charger\_current\_notifier](structcharger__current__notifier.md) |
|  | The input current thresholds for the charger to notify the system. [More...](structcharger__current__notifier.md#details) |
| union | [charger\_propval](unioncharger__propval.md) |
|  | container for a [charger\_property](group__charger__interface.md#ga6eb3b4cc76e4f1e34732b7853eb860b7 "Runtime Dynamic Battery Parameters.") value [More...](unioncharger__propval.md#details) |
| struct | [charger\_driver\_api](structcharger__driver__api.md) |
|  | Charging device API. [More...](structcharger__driver__api.md#details) |

| Typedefs | |
| --- | --- |
| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [charger\_prop\_t](group__charger__interface.md#ga4ce808890de2d01cdb75feddbf275635) |
|  | A charger property's identifier. |
| typedef int(\* | [charger\_get\_property\_t](group__charger__interface.md#gafb7488129e0a6c086d3ff0ffadb6c82b)) (const struct [device](structdevice.md) \*dev, const [charger\_prop\_t](group__charger__interface.md#ga4ce808890de2d01cdb75feddbf275635) prop, union [charger\_propval](unioncharger__propval.md) \*val) |
|  | Callback API for getting a charger property. |
| typedef int(\* | [charger\_set\_property\_t](group__charger__interface.md#ga6556781abf0e81eee431c88cb894a8e6)) (const struct [device](structdevice.md) \*dev, const [charger\_prop\_t](group__charger__interface.md#ga4ce808890de2d01cdb75feddbf275635) prop, const union [charger\_propval](unioncharger__propval.md) \*val) |
|  | Callback API for setting a charger property. |
| typedef int(\* | [charger\_charge\_enable\_t](group__charger__interface.md#gaf035c2972693a8763fd08b7db8c9c0bd)) (const struct [device](structdevice.md) \*dev, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Callback API enabling or disabling a charge cycle. |

| Enumerations | |
| --- | --- |
| enum | [charger\_property](group__charger__interface.md#ga6eb3b4cc76e4f1e34732b7853eb860b7) {     [CHARGER\_PROP\_ONLINE](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a1c8906c0e4e278b84cab7d126cf95526) = 0 , [CHARGER\_PROP\_PRESENT](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a0dd5ee0d22cba6440c3f3583582d405b) , [CHARGER\_PROP\_STATUS](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a73b9f45dd43347016a4dd6e15cd78cf6) , [CHARGER\_PROP\_CHARGE\_TYPE](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7aff40a23cd65dcab5b3118fd9da3aaf95) ,     [CHARGER\_PROP\_HEALTH](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a2cc8bc744a98284e6c96a6ffb30ec654) , [CHARGER\_PROP\_CONSTANT\_CHARGE\_CURRENT\_UA](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a81a18d7286bfcf729402db6990ddc306) , [CHARGER\_PROP\_PRECHARGE\_CURRENT\_UA](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7aa8d97a1db907ccd40a7b5d917c0a9ab9) , [CHARGER\_PROP\_CHARGE\_TERM\_CURRENT\_UA](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7ac60d2e9945e8f1eaf0e824b778a377fc) ,     [CHARGER\_PROP\_CONSTANT\_CHARGE\_VOLTAGE\_UV](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a5b4a6c4f1f6abb7a568c7c42dca696bf) , [CHARGER\_PROP\_INPUT\_REGULATION\_CURRENT\_UA](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a703a0e374053a410ec154eac117f9085) , [CHARGER\_PROP\_INPUT\_REGULATION\_VOLTAGE\_UV](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a1e60d770a5d8e47118040ace3c6d8ec0) , [CHARGER\_PROP\_INPUT\_CURRENT\_NOTIFICATION](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a70f2c71cd9d4e0f88ee36886094540fe) ,     [CHARGER\_PROP\_COMMON\_COUNT](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a3c6d858ad83fa0aeca39ce33817f3732) , [CHARGER\_PROP\_CUSTOM\_BEGIN](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a279bd89ce909be3ea95be2fee33b08b3) = CHARGER\_PROP\_COMMON\_COUNT + 1 , [CHARGER\_PROP\_MAX](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a97342ebdadce27894e82dc57ed54724e) = UINT16\_MAX   } |
|  | Runtime Dynamic Battery Parameters. [More...](group__charger__interface.md#ga6eb3b4cc76e4f1e34732b7853eb860b7) |
| enum | [charger\_online](group__charger__interface.md#gad95d2b1aaf18ac3a1c536f2d40317c19) { [CHARGER\_ONLINE\_OFFLINE](group__charger__interface.md#ggad95d2b1aaf18ac3a1c536f2d40317c19a50004df0b037325d33d21427a847a5b3) = 0 , [CHARGER\_ONLINE\_FIXED](group__charger__interface.md#ggad95d2b1aaf18ac3a1c536f2d40317c19a119679acb9bcc173831003dfa309f5a6) , [CHARGER\_ONLINE\_PROGRAMMABLE](group__charger__interface.md#ggad95d2b1aaf18ac3a1c536f2d40317c19a2b51eb24ac1047c99f8079beb261503e) } |
|  | External supply states. [More...](group__charger__interface.md#gad95d2b1aaf18ac3a1c536f2d40317c19) |
| enum | [charger\_status](group__charger__interface.md#ga4a3c46bc0916082d15e665f7665c89d7) {     [CHARGER\_STATUS\_UNKNOWN](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7ad474b06c524aea24b1ecb2e7d6621fa5) = 0 , [CHARGER\_STATUS\_CHARGING](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7ad95370e7cd6dc5d72e73d741b41cb8ad) , [CHARGER\_STATUS\_DISCHARGING](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7ad06083516280a41fec5f8cc649ff499e) , [CHARGER\_STATUS\_NOT\_CHARGING](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7a445d1979c2541ead57ddaa89dc57c658) ,     [CHARGER\_STATUS\_FULL](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7a2f550ea27e63b2eab78cc673d3e692cf)   } |
|  | Charging states. [More...](group__charger__interface.md#ga4a3c46bc0916082d15e665f7665c89d7) |
| enum | [charger\_charge\_type](group__charger__interface.md#gaee833a379a8674621d2fdf9b57d1f803) {     [CHARGER\_CHARGE\_TYPE\_UNKNOWN](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803aab6c7ea7d961c131bc91f91a9fa7cce4) = 0 , [CHARGER\_CHARGE\_TYPE\_NONE](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803a71e7c6a73193c0ce1ba0467d93b72f17) , [CHARGER\_CHARGE\_TYPE\_TRICKLE](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803acc5367f61f10e6574ec01d090598cbf8) , [CHARGER\_CHARGE\_TYPE\_FAST](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803ae2b5fc2d034a037c9eee5afca2c5a711) ,     [CHARGER\_CHARGE\_TYPE\_STANDARD](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803a004c6c71a3a9943e151ed4fa49746ee6) , [CHARGER\_CHARGE\_TYPE\_ADAPTIVE](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803aa5a6d6cc9767fb0b19d13070c108ccc2) , [CHARGER\_CHARGE\_TYPE\_LONGLIFE](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803acaa4a3c513188cd9dba71c98639bd31f) , [CHARGER\_CHARGE\_TYPE\_BYPASS](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803abe42aac55841886e2a69b94018918ee8)   } |
|  | Charge algorithm types. [More...](group__charger__interface.md#gaee833a379a8674621d2fdf9b57d1f803) |
| enum | [charger\_health](group__charger__interface.md#gaab33241d3b85ab0770be9b1bd17e4412) {     [CHARGER\_HEALTH\_UNKNOWN](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a21f2873586a920885d411e8dd02786ad) = 0 , [CHARGER\_HEALTH\_GOOD](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a7fe49d6d81fc76c70ab979eece42d538) , [CHARGER\_HEALTH\_OVERHEAT](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412affd0237aed52d704e51f18a4d57f3b3b) , [CHARGER\_HEALTH\_OVERVOLTAGE](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412affbc931d777af7a03233d0dbed364459) ,     [CHARGER\_HEALTH\_UNSPEC\_FAILURE](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a7651b0b32b8472caa8545278bef4e8fa) , [CHARGER\_HEALTH\_COLD](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a24b2e80a03d4d06a267f3264edd64967) , [CHARGER\_HEALTH\_WATCHDOG\_TIMER\_EXPIRE](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412ab9c81803fd5a1dd6a843765304e592ce) , [CHARGER\_HEALTH\_SAFETY\_TIMER\_EXPIRE](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a17ccf9a3e7878c11e6a34bf5a4e38a82) ,     [CHARGER\_HEALTH\_CALIBRATION\_REQUIRED](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a1936cf89fd8e7286831a91dc218c25f1) , [CHARGER\_HEALTH\_WARM](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a206b491bf7e7efc60b9a41d69a2d305f) , [CHARGER\_HEALTH\_COOL](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412aad346d9b4b43998367facd491bc0ecd3) , [CHARGER\_HEALTH\_HOT](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412aa3cd6b3e3e2ccfde03ba49912a2efcf1) ,     [CHARGER\_HEALTH\_NO\_BATTERY](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a50dabeb87f23ca712b5c78f0e5a4c60b)   } |
|  | Charger health conditions. [More...](group__charger__interface.md#gaab33241d3b85ab0770be9b1bd17e4412) |
| enum | [charger\_notification\_severity](group__charger__interface.md#ga2e7d7f15725db4d502bc3f46476a310d) { [CHARGER\_SEVERITY\_PEAK](group__charger__interface.md#gga2e7d7f15725db4d502bc3f46476a310da667f21cc72028772d09228424f75b40b) = 0 , [CHARGER\_SEVERITY\_CRITICAL](group__charger__interface.md#gga2e7d7f15725db4d502bc3f46476a310da6bb0e1059a26d31380094530da94e3e8) , [CHARGER\_SEVERITY\_WARNING](group__charger__interface.md#gga2e7d7f15725db4d502bc3f46476a310da347972f338fe70920f72c85dcdd1f885) } |
|  | Charger severity levels for system notifications. [More...](group__charger__interface.md#ga2e7d7f15725db4d502bc3f46476a310d) |

| Functions | |
| --- | --- |
| int | [charger\_get\_prop](group__charger__interface.md#ga00e5b61d517c93d7d3c863b14b07b738) (const struct [device](structdevice.md) \*dev, const [charger\_prop\_t](group__charger__interface.md#ga4ce808890de2d01cdb75feddbf275635) prop, union [charger\_propval](unioncharger__propval.md) \*val) |
|  | Fetch a battery charger property. |
| int | [charger\_set\_prop](group__charger__interface.md#ga0036e3f5924585457a99a2e444ef5aab) (const struct [device](structdevice.md) \*dev, const [charger\_prop\_t](group__charger__interface.md#ga4ce808890de2d01cdb75feddbf275635) prop, const union [charger\_propval](unioncharger__propval.md) \*val) |
|  | Set a battery charger property. |
| int | [charger\_charge\_enable](group__charger__interface.md#gace1ea9841574d75d314db078df5a0b3a) (const struct [device](structdevice.md) \*dev, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enable or disable a charge cycle. |

## Detailed Description

Charger APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [charger.h](charger_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

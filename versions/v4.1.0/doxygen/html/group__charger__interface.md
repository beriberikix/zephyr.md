---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__charger__interface.html
original_path: doxygen/html/group__charger__interface.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Charger Interface

[Device Driver APIs](group__io__interfaces.md)

Charger Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [charger\_current\_notifier](structcharger__current__notifier.md) |
|  | The input current thresholds for the charger to notify the system. [More...](structcharger__current__notifier.md#details) |
| union | [charger\_propval](unioncharger__propval.md) |
|  | container for a [charger\_property](#ga6eb3b4cc76e4f1e34732b7853eb860b7) value [More...](unioncharger__propval.md#details) |
| struct | [charger\_driver\_api](structcharger__driver__api.md) |
|  | Charging device API. [More...](structcharger__driver__api.md#details) |

| Typedefs | |
| --- | --- |
| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [charger\_prop\_t](#ga4ce808890de2d01cdb75feddbf275635) |
|  | A charger property's identifier. |
| typedef void(\* | [charger\_status\_notifier\_t](#ga7666697bde91b66829113efe151d1cb2)) (enum [charger\_status](#ga4a3c46bc0916082d15e665f7665c89d7) status) |
|  | The charger status change callback to notify the system. |
| typedef void(\* | [charger\_online\_notifier\_t](#gab29c2fafc53988555d72974199f25475)) (enum [charger\_online](#gad95d2b1aaf18ac3a1c536f2d40317c19) online) |
|  | The charger online change callback to notify the system. |
| typedef int(\* | [charger\_get\_property\_t](#gafb7488129e0a6c086d3ff0ffadb6c82b)) (const struct [device](structdevice.md) \*dev, const [charger\_prop\_t](#ga4ce808890de2d01cdb75feddbf275635) prop, union [charger\_propval](unioncharger__propval.md) \*val) |
|  | Callback API for getting a charger property. |
| typedef int(\* | [charger\_set\_property\_t](#ga6556781abf0e81eee431c88cb894a8e6)) (const struct [device](structdevice.md) \*dev, const [charger\_prop\_t](#ga4ce808890de2d01cdb75feddbf275635) prop, const union [charger\_propval](unioncharger__propval.md) \*val) |
|  | Callback API for setting a charger property. |
| typedef int(\* | [charger\_charge\_enable\_t](#gaf035c2972693a8763fd08b7db8c9c0bd)) (const struct [device](structdevice.md) \*dev, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Callback API enabling or disabling a charge cycle. |

| Enumerations | |
| --- | --- |
| enum | [charger\_property](#ga6eb3b4cc76e4f1e34732b7853eb860b7) {     [CHARGER\_PROP\_ONLINE](#gga6eb3b4cc76e4f1e34732b7853eb860b7a1c8906c0e4e278b84cab7d126cf95526) = 0 , [CHARGER\_PROP\_PRESENT](#gga6eb3b4cc76e4f1e34732b7853eb860b7a0dd5ee0d22cba6440c3f3583582d405b) , [CHARGER\_PROP\_STATUS](#gga6eb3b4cc76e4f1e34732b7853eb860b7a73b9f45dd43347016a4dd6e15cd78cf6) , [CHARGER\_PROP\_CHARGE\_TYPE](#gga6eb3b4cc76e4f1e34732b7853eb860b7aff40a23cd65dcab5b3118fd9da3aaf95) ,     [CHARGER\_PROP\_HEALTH](#gga6eb3b4cc76e4f1e34732b7853eb860b7a2cc8bc744a98284e6c96a6ffb30ec654) , [CHARGER\_PROP\_CONSTANT\_CHARGE\_CURRENT\_UA](#gga6eb3b4cc76e4f1e34732b7853eb860b7a81a18d7286bfcf729402db6990ddc306) , [CHARGER\_PROP\_PRECHARGE\_CURRENT\_UA](#gga6eb3b4cc76e4f1e34732b7853eb860b7aa8d97a1db907ccd40a7b5d917c0a9ab9) , [CHARGER\_PROP\_CHARGE\_TERM\_CURRENT\_UA](#gga6eb3b4cc76e4f1e34732b7853eb860b7ac60d2e9945e8f1eaf0e824b778a377fc) ,     [CHARGER\_PROP\_CONSTANT\_CHARGE\_VOLTAGE\_UV](#gga6eb3b4cc76e4f1e34732b7853eb860b7a5b4a6c4f1f6abb7a568c7c42dca696bf) , [CHARGER\_PROP\_INPUT\_REGULATION\_CURRENT\_UA](#gga6eb3b4cc76e4f1e34732b7853eb860b7a703a0e374053a410ec154eac117f9085) , [CHARGER\_PROP\_INPUT\_REGULATION\_VOLTAGE\_UV](#gga6eb3b4cc76e4f1e34732b7853eb860b7a1e60d770a5d8e47118040ace3c6d8ec0) , [CHARGER\_PROP\_INPUT\_CURRENT\_NOTIFICATION](#gga6eb3b4cc76e4f1e34732b7853eb860b7a70f2c71cd9d4e0f88ee36886094540fe) ,     [CHARGER\_PROP\_DISCHARGE\_CURRENT\_NOTIFICATION](#gga6eb3b4cc76e4f1e34732b7853eb860b7a3d3e3190b016a9c31ed5c82e2ade0b72) , [CHARGER\_PROP\_SYSTEM\_VOLTAGE\_NOTIFICATION\_UV](#gga6eb3b4cc76e4f1e34732b7853eb860b7ace0a0e6cbc0ccaf166ff0df7e1b275c0) , [CHARGER\_PROP\_STATUS\_NOTIFICATION](#gga6eb3b4cc76e4f1e34732b7853eb860b7a9340eb6fb5b80370148a43366b753d9b) , [CHARGER\_PROP\_ONLINE\_NOTIFICATION](#gga6eb3b4cc76e4f1e34732b7853eb860b7a389920359b8866af70b164d68820d4b7) ,     [CHARGER\_PROP\_COMMON\_COUNT](#gga6eb3b4cc76e4f1e34732b7853eb860b7a3c6d858ad83fa0aeca39ce33817f3732) , [CHARGER\_PROP\_CUSTOM\_BEGIN](#gga6eb3b4cc76e4f1e34732b7853eb860b7a279bd89ce909be3ea95be2fee33b08b3) = CHARGER\_PROP\_COMMON\_COUNT + 1 , [CHARGER\_PROP\_MAX](#gga6eb3b4cc76e4f1e34732b7853eb860b7a97342ebdadce27894e82dc57ed54724e) = UINT16\_MAX   } |
|  | Runtime Dynamic Battery Parameters. [More...](#ga6eb3b4cc76e4f1e34732b7853eb860b7) |
| enum | [charger\_online](#gad95d2b1aaf18ac3a1c536f2d40317c19) { [CHARGER\_ONLINE\_OFFLINE](#ggad95d2b1aaf18ac3a1c536f2d40317c19a50004df0b037325d33d21427a847a5b3) = 0 , [CHARGER\_ONLINE\_FIXED](#ggad95d2b1aaf18ac3a1c536f2d40317c19a119679acb9bcc173831003dfa309f5a6) , [CHARGER\_ONLINE\_PROGRAMMABLE](#ggad95d2b1aaf18ac3a1c536f2d40317c19a2b51eb24ac1047c99f8079beb261503e) } |
|  | External supply states. [More...](#gad95d2b1aaf18ac3a1c536f2d40317c19) |
| enum | [charger\_status](#ga4a3c46bc0916082d15e665f7665c89d7) {     [CHARGER\_STATUS\_UNKNOWN](#gga4a3c46bc0916082d15e665f7665c89d7ad474b06c524aea24b1ecb2e7d6621fa5) = 0 , [CHARGER\_STATUS\_CHARGING](#gga4a3c46bc0916082d15e665f7665c89d7ad95370e7cd6dc5d72e73d741b41cb8ad) , [CHARGER\_STATUS\_DISCHARGING](#gga4a3c46bc0916082d15e665f7665c89d7ad06083516280a41fec5f8cc649ff499e) , [CHARGER\_STATUS\_NOT\_CHARGING](#gga4a3c46bc0916082d15e665f7665c89d7a445d1979c2541ead57ddaa89dc57c658) ,     [CHARGER\_STATUS\_FULL](#gga4a3c46bc0916082d15e665f7665c89d7a2f550ea27e63b2eab78cc673d3e692cf)   } |
|  | Charging states. [More...](#ga4a3c46bc0916082d15e665f7665c89d7) |
| enum | [charger\_charge\_type](#gaee833a379a8674621d2fdf9b57d1f803) {     [CHARGER\_CHARGE\_TYPE\_UNKNOWN](#ggaee833a379a8674621d2fdf9b57d1f803aab6c7ea7d961c131bc91f91a9fa7cce4) = 0 , [CHARGER\_CHARGE\_TYPE\_NONE](#ggaee833a379a8674621d2fdf9b57d1f803a71e7c6a73193c0ce1ba0467d93b72f17) , [CHARGER\_CHARGE\_TYPE\_TRICKLE](#ggaee833a379a8674621d2fdf9b57d1f803acc5367f61f10e6574ec01d090598cbf8) , [CHARGER\_CHARGE\_TYPE\_FAST](#ggaee833a379a8674621d2fdf9b57d1f803ae2b5fc2d034a037c9eee5afca2c5a711) ,     [CHARGER\_CHARGE\_TYPE\_STANDARD](#ggaee833a379a8674621d2fdf9b57d1f803a004c6c71a3a9943e151ed4fa49746ee6) , [CHARGER\_CHARGE\_TYPE\_ADAPTIVE](#ggaee833a379a8674621d2fdf9b57d1f803aa5a6d6cc9767fb0b19d13070c108ccc2) , [CHARGER\_CHARGE\_TYPE\_LONGLIFE](#ggaee833a379a8674621d2fdf9b57d1f803acaa4a3c513188cd9dba71c98639bd31f) , [CHARGER\_CHARGE\_TYPE\_BYPASS](#ggaee833a379a8674621d2fdf9b57d1f803abe42aac55841886e2a69b94018918ee8)   } |
|  | Charge algorithm types. [More...](#gaee833a379a8674621d2fdf9b57d1f803) |
| enum | [charger\_health](#gaab33241d3b85ab0770be9b1bd17e4412) {     [CHARGER\_HEALTH\_UNKNOWN](#ggaab33241d3b85ab0770be9b1bd17e4412a21f2873586a920885d411e8dd02786ad) = 0 , [CHARGER\_HEALTH\_GOOD](#ggaab33241d3b85ab0770be9b1bd17e4412a7fe49d6d81fc76c70ab979eece42d538) , [CHARGER\_HEALTH\_OVERHEAT](#ggaab33241d3b85ab0770be9b1bd17e4412affd0237aed52d704e51f18a4d57f3b3b) , [CHARGER\_HEALTH\_OVERVOLTAGE](#ggaab33241d3b85ab0770be9b1bd17e4412affbc931d777af7a03233d0dbed364459) ,     [CHARGER\_HEALTH\_UNSPEC\_FAILURE](#ggaab33241d3b85ab0770be9b1bd17e4412a7651b0b32b8472caa8545278bef4e8fa) , [CHARGER\_HEALTH\_COLD](#ggaab33241d3b85ab0770be9b1bd17e4412a24b2e80a03d4d06a267f3264edd64967) , [CHARGER\_HEALTH\_WATCHDOG\_TIMER\_EXPIRE](#ggaab33241d3b85ab0770be9b1bd17e4412ab9c81803fd5a1dd6a843765304e592ce) , [CHARGER\_HEALTH\_SAFETY\_TIMER\_EXPIRE](#ggaab33241d3b85ab0770be9b1bd17e4412a17ccf9a3e7878c11e6a34bf5a4e38a82) ,     [CHARGER\_HEALTH\_CALIBRATION\_REQUIRED](#ggaab33241d3b85ab0770be9b1bd17e4412a1936cf89fd8e7286831a91dc218c25f1) , [CHARGER\_HEALTH\_WARM](#ggaab33241d3b85ab0770be9b1bd17e4412a206b491bf7e7efc60b9a41d69a2d305f) , [CHARGER\_HEALTH\_COOL](#ggaab33241d3b85ab0770be9b1bd17e4412aad346d9b4b43998367facd491bc0ecd3) , [CHARGER\_HEALTH\_HOT](#ggaab33241d3b85ab0770be9b1bd17e4412aa3cd6b3e3e2ccfde03ba49912a2efcf1) ,     [CHARGER\_HEALTH\_NO\_BATTERY](#ggaab33241d3b85ab0770be9b1bd17e4412a50dabeb87f23ca712b5c78f0e5a4c60b)   } |
|  | Charger health conditions. [More...](#gaab33241d3b85ab0770be9b1bd17e4412) |
| enum | [charger\_notification\_severity](#ga2e7d7f15725db4d502bc3f46476a310d) { [CHARGER\_SEVERITY\_PEAK](#gga2e7d7f15725db4d502bc3f46476a310da667f21cc72028772d09228424f75b40b) = 0 , [CHARGER\_SEVERITY\_CRITICAL](#gga2e7d7f15725db4d502bc3f46476a310da6bb0e1059a26d31380094530da94e3e8) , [CHARGER\_SEVERITY\_WARNING](#gga2e7d7f15725db4d502bc3f46476a310da347972f338fe70920f72c85dcdd1f885) } |
|  | Charger severity levels for system notifications. [More...](#ga2e7d7f15725db4d502bc3f46476a310d) |

| Functions | |
| --- | --- |
| int | [charger\_get\_prop](#ga00e5b61d517c93d7d3c863b14b07b738) (const struct [device](structdevice.md) \*dev, const [charger\_prop\_t](#ga4ce808890de2d01cdb75feddbf275635) prop, union [charger\_propval](unioncharger__propval.md) \*val) |
|  | Fetch a battery charger property. |
| int | [charger\_set\_prop](#ga0036e3f5924585457a99a2e444ef5aab) (const struct [device](structdevice.md) \*dev, const [charger\_prop\_t](#ga4ce808890de2d01cdb75feddbf275635) prop, const union [charger\_propval](unioncharger__propval.md) \*val) |
|  | Set a battery charger property. |
| int | [charger\_charge\_enable](#gace1ea9841574d75d314db078df5a0b3a) (const struct [device](structdevice.md) \*dev, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enable or disable a charge cycle. |

## Detailed Description

Charger Interface.

## Typedef Documentation

## [◆ ](#gaf035c2972693a8763fd08b7db8c9c0bd)charger\_charge\_enable\_t

| typedef int(\* charger\_charge\_enable\_t) (const struct [device](structdevice.md) \*dev, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| --- |

`#include <[charger.h](charger_8h.md)>`

Callback API enabling or disabling a charge cycle.

See [charger\_charge\_enable()](#gace1ea9841574d75d314db078df5a0b3a) for argument description

## [◆ ](#gafb7488129e0a6c086d3ff0ffadb6c82b)charger\_get\_property\_t

| typedef int(\* charger\_get\_property\_t) (const struct [device](structdevice.md) \*dev, const [charger\_prop\_t](#ga4ce808890de2d01cdb75feddbf275635) prop, union [charger\_propval](unioncharger__propval.md) \*val) |
| --- |

`#include <[charger.h](charger_8h.md)>`

Callback API for getting a charger property.

See charger\_get\_property() for argument description

## [◆ ](#gab29c2fafc53988555d72974199f25475)charger\_online\_notifier\_t

| typedef void(\* charger\_online\_notifier\_t) (enum [charger\_online](#gad95d2b1aaf18ac3a1c536f2d40317c19) online) |
| --- |

`#include <[charger.h](charger_8h.md)>`

The charger online change callback to notify the system.

Parameters
:   | online | Current external supply state |
    | --- | --- |

## [◆ ](#ga4ce808890de2d01cdb75feddbf275635)charger\_prop\_t

| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [charger\_prop\_t](#ga4ce808890de2d01cdb75feddbf275635) |
| --- |

`#include <[charger.h](charger_8h.md)>`

A charger property's identifier.

See [charger\_property](#ga6eb3b4cc76e4f1e34732b7853eb860b7) for a list of identifiers

## [◆ ](#ga6556781abf0e81eee431c88cb894a8e6)charger\_set\_property\_t

| typedef int(\* charger\_set\_property\_t) (const struct [device](structdevice.md) \*dev, const [charger\_prop\_t](#ga4ce808890de2d01cdb75feddbf275635) prop, const union [charger\_propval](unioncharger__propval.md) \*val) |
| --- |

`#include <[charger.h](charger_8h.md)>`

Callback API for setting a charger property.

See charger\_set\_property() for argument description

## [◆ ](#ga7666697bde91b66829113efe151d1cb2)charger\_status\_notifier\_t

| typedef void(\* charger\_status\_notifier\_t) (enum [charger\_status](#ga4a3c46bc0916082d15e665f7665c89d7) status) |
| --- |

`#include <[charger.h](charger_8h.md)>`

The charger status change callback to notify the system.

Parameters
:   | status | Current charging state |
    | --- | --- |

## Enumeration Type Documentation

## [◆ ](#gaee833a379a8674621d2fdf9b57d1f803)charger\_charge\_type

| enum [charger\_charge\_type](#gaee833a379a8674621d2fdf9b57d1f803) |
| --- |

`#include <[charger.h](charger_8h.md)>`

Charge algorithm types.

| Enumerator | |
| --- | --- |
| CHARGER\_CHARGE\_TYPE\_UNKNOWN | Charge type is unknown. |
| CHARGER\_CHARGE\_TYPE\_NONE | Charging is not occurring. |
| CHARGER\_CHARGE\_TYPE\_TRICKLE | Charging is occurring at the slowest desired charge rate, typically for battery detection or preconditioning. |
| CHARGER\_CHARGE\_TYPE\_FAST | Charging is occurring at the fastest desired charge rate. |
| CHARGER\_CHARGE\_TYPE\_STANDARD | Charging is occurring at a moderate charge rate. |
| CHARGER\_CHARGE\_TYPE\_ADAPTIVE |  |
| CHARGER\_CHARGE\_TYPE\_LONGLIFE |  |
| CHARGER\_CHARGE\_TYPE\_BYPASS |  |

## [◆ ](#gaab33241d3b85ab0770be9b1bd17e4412)charger\_health

| enum [charger\_health](#gaab33241d3b85ab0770be9b1bd17e4412) |
| --- |

`#include <[charger.h](charger_8h.md)>`

Charger health conditions.

These conditions determine the ability to, or the rate of, charge

| Enumerator | |
| --- | --- |
| CHARGER\_HEALTH\_UNKNOWN | Charger health condition is unknown. |
| CHARGER\_HEALTH\_GOOD | Charger health condition is good. |
| CHARGER\_HEALTH\_OVERHEAT | The charger device is overheated. |
| CHARGER\_HEALTH\_OVERVOLTAGE | The battery voltage has exceeded its overvoltage threshold. |
| CHARGER\_HEALTH\_UNSPEC\_FAILURE | The battery or charger device is experiencing an unspecified failure. |
| CHARGER\_HEALTH\_COLD | The battery temperature is below the "cold" threshold. |
| CHARGER\_HEALTH\_WATCHDOG\_TIMER\_EXPIRE | The charger device's watchdog timer has expired. |
| CHARGER\_HEALTH\_SAFETY\_TIMER\_EXPIRE | The charger device's safety timer has expired. |
| CHARGER\_HEALTH\_CALIBRATION\_REQUIRED | The charger device requires calibration. |
| CHARGER\_HEALTH\_WARM | The battery temperature is in the "warm" range. |
| CHARGER\_HEALTH\_COOL | The battery temperature is in the "cool" range. |
| CHARGER\_HEALTH\_HOT | The battery temperature is below the "hot" threshold. |
| CHARGER\_HEALTH\_NO\_BATTERY | The charger device does not detect a battery. |

## [◆ ](#ga2e7d7f15725db4d502bc3f46476a310d)charger\_notification\_severity

| enum [charger\_notification\_severity](#ga2e7d7f15725db4d502bc3f46476a310d) |
| --- |

`#include <[charger.h](charger_8h.md)>`

Charger severity levels for system notifications.

| Enumerator | |
| --- | --- |
| CHARGER\_SEVERITY\_PEAK | Most severe level, typically triggered instantaneously. |
| CHARGER\_SEVERITY\_CRITICAL | More severe than the warning level, less severe than peak. |
| CHARGER\_SEVERITY\_WARNING | Base severity level. |

## [◆ ](#gad95d2b1aaf18ac3a1c536f2d40317c19)charger\_online

| enum [charger\_online](#gad95d2b1aaf18ac3a1c536f2d40317c19) |
| --- |

`#include <[charger.h](charger_8h.md)>`

External supply states.

| Enumerator | |
| --- | --- |
| CHARGER\_ONLINE\_OFFLINE | External supply not present. |
| CHARGER\_ONLINE\_FIXED | External supply is present and of fixed output. |
| CHARGER\_ONLINE\_PROGRAMMABLE | External supply is present and of programmable output. |

## [◆ ](#ga6eb3b4cc76e4f1e34732b7853eb860b7)charger\_property

| enum [charger\_property](#ga6eb3b4cc76e4f1e34732b7853eb860b7) |
| --- |

`#include <[charger.h](charger_8h.md)>`

Runtime Dynamic Battery Parameters.

| Enumerator | |
| --- | --- |
| CHARGER\_PROP\_ONLINE | Indicates if external supply is present for the charger.  Value should be of type enum [charger\_online](#gad95d2b1aaf18ac3a1c536f2d40317c19) |
| CHARGER\_PROP\_PRESENT | Reports whether or not a battery is present.  Value should be of type bool |
| CHARGER\_PROP\_STATUS | Represents the charging status of the charger.  Value should be of type enum [charger\_status](#ga4a3c46bc0916082d15e665f7665c89d7) |
| CHARGER\_PROP\_CHARGE\_TYPE | Represents the charging algo type of the charger.  Value should be of type enum [charger\_charge\_type](#gaee833a379a8674621d2fdf9b57d1f803) |
| CHARGER\_PROP\_HEALTH | Represents the health of the charger.  Value should be of type enum [charger\_health](#gaab33241d3b85ab0770be9b1bd17e4412) |
| CHARGER\_PROP\_CONSTANT\_CHARGE\_CURRENT\_UA | Configuration of current sink used for charging in µA. |
| CHARGER\_PROP\_PRECHARGE\_CURRENT\_UA | Configuration of current sink used for conditioning in µA. |
| CHARGER\_PROP\_CHARGE\_TERM\_CURRENT\_UA | Configuration of charge termination target in µA. |
| CHARGER\_PROP\_CONSTANT\_CHARGE\_VOLTAGE\_UV | Configuration of charge voltage regulation target in µV. |
| CHARGER\_PROP\_INPUT\_REGULATION\_CURRENT\_UA | Configuration of the input current regulation target in µA.  This value is a rising current threshold that is regulated by reducing the charge current output |
| CHARGER\_PROP\_INPUT\_REGULATION\_VOLTAGE\_UV | Configuration of the input voltage regulation target in µV.  This value is a falling voltage threshold that is regulated by reducing the charge current output |
| CHARGER\_PROP\_INPUT\_CURRENT\_NOTIFICATION | Configuration to issue a notification to the system based on the input current level and timing.  Value should be of type struct [charger\_current\_notifier](structcharger__current__notifier.md "The input current thresholds for the charger to notify the system.") |
| CHARGER\_PROP\_DISCHARGE\_CURRENT\_NOTIFICATION | Configuration to issue a notification to the system based on the battery discharge current level and timing.  Value should be of type struct [charger\_current\_notifier](structcharger__current__notifier.md "The input current thresholds for the charger to notify the system.") |
| CHARGER\_PROP\_SYSTEM\_VOLTAGE\_NOTIFICATION\_UV | Configuration of the falling system voltage threshold where a notification is issued to the system, measured in µV. |
| CHARGER\_PROP\_STATUS\_NOTIFICATION | Configuration to issue a notification to the system based on the charger status change.  Value should be of type [charger\_status\_notifier\_t](#ga7666697bde91b66829113efe151d1cb2) |
| CHARGER\_PROP\_ONLINE\_NOTIFICATION | Configuration to issue a notification to the system based on the charger online change.  Value should be of type [charger\_online\_notifier\_t](#gab29c2fafc53988555d72974199f25475) |
| CHARGER\_PROP\_COMMON\_COUNT | Reserved to demark end of common charger properties. |
| CHARGER\_PROP\_CUSTOM\_BEGIN | Reserved to demark downstream custom properties - use this value as the actual value may change over future versions of this API. |
| CHARGER\_PROP\_MAX | Reserved to demark end of valid enum properties. |

## [◆ ](#ga4a3c46bc0916082d15e665f7665c89d7)charger\_status

| enum [charger\_status](#ga4a3c46bc0916082d15e665f7665c89d7) |
| --- |

`#include <[charger.h](charger_8h.md)>`

Charging states.

| Enumerator | |
| --- | --- |
| CHARGER\_STATUS\_UNKNOWN | Charging device state is unknown. |
| CHARGER\_STATUS\_CHARGING | Charging device is charging a battery. |
| CHARGER\_STATUS\_DISCHARGING | Charging device is not able to charge a battery. |
| CHARGER\_STATUS\_NOT\_CHARGING | Charging device is not charging a battery. |
| CHARGER\_STATUS\_FULL | The battery is full and the charging device will not attempt charging. |

## Function Documentation

## [◆ ](#gace1ea9841574d75d314db078df5a0b3a)charger\_charge\_enable()

| int charger\_charge\_enable | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) |

`#include <[charger.h](charger_8h.md)>`

Enable or disable a charge cycle.

Parameters
:   | dev | Pointer to the battery charger device |
    | --- | --- |
    | enable | true enables a charge cycle, false disables a charge cycle |

Return values
:   | 0 | if successful |
    | --- | --- |
    | -EIO | if communication with the charger failed |
    | -EINVAL | if the conditions for initiating charging are invalid |

## [◆ ](#ga00e5b61d517c93d7d3c863b14b07b738)charger\_get\_prop()

| int charger\_get\_prop | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [charger\_prop\_t](#ga4ce808890de2d01cdb75feddbf275635) | *prop*, |
|  |  | union [charger\_propval](unioncharger__propval.md) \* | *val* ) |

`#include <[charger.h](charger_8h.md)>`

Fetch a battery charger property.

Parameters
:   | dev | Pointer to the battery charger device |
    | --- | --- |
    | prop | Charger property to get |
    | val | Pointer to [charger\_propval](unioncharger__propval.md "container for a charger_property value") union |

Return values
:   | 0 | if successful |
    | --- | --- |
    | < | 0 if getting property failed |

## [◆ ](#ga0036e3f5924585457a99a2e444ef5aab)charger\_set\_prop()

| int charger\_set\_prop | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [charger\_prop\_t](#ga4ce808890de2d01cdb75feddbf275635) | *prop*, |
|  |  | const union [charger\_propval](unioncharger__propval.md) \* | *val* ) |

`#include <[charger.h](charger_8h.md)>`

Set a battery charger property.

Parameters
:   | dev | Pointer to the battery charger device |
    | --- | --- |
    | prop | Charger property to set |
    | val | Pointer to [charger\_propval](unioncharger__propval.md "container for a charger_property value") union |

Return values
:   | 0 | if successful |
    | --- | --- |
    | < | 0 if setting property failed |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

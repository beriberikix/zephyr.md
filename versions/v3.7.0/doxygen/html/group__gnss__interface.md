---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__gnss__interface.html
original_path: doxygen/html/group__gnss__interface.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

GNSS Interface

[Device Driver APIs](group__io__interfaces.md)

GNSS Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [gnss\_periodic\_config](structgnss__periodic__config.md) |
|  | GNSS periodic tracking configuration. [More...](structgnss__periodic__config.md#details) |
| struct | [gnss\_info](structgnss__info.md) |
|  | GNSS info data structure. [More...](structgnss__info.md#details) |
| struct | [gnss\_time](structgnss__time.md) |
|  | GNSS time data structure. [More...](structgnss__time.md#details) |
| struct | [gnss\_driver\_api](structgnss__driver__api.md) |
|  | GNSS API structure. [More...](structgnss__driver__api.md#details) |
| struct | [gnss\_data](structgnss__data.md) |
|  | GNSS data structure. [More...](structgnss__data.md#details) |
| struct | [gnss\_data\_callback](structgnss__data__callback.md) |
|  | GNSS callback structure. [More...](structgnss__data__callback.md#details) |
| struct | [gnss\_satellite](structgnss__satellite.md) |
|  | GNSS satellite structure. [More...](structgnss__satellite.md#details) |
| struct | [gnss\_satellites\_callback](structgnss__satellites__callback.md) |
|  | GNSS callback structure. [More...](structgnss__satellites__callback.md#details) |

| Macros | |
| --- | --- |
| #define | [GNSS\_DATA\_CALLBACK\_DEFINE](#gae9c3fd5804bd6f8e6790cb1b7e47e4a6)(\_dev, \_callback) |
|  | Register a callback structure for GNSS data published. |
| #define | [GNSS\_SATELLITES\_CALLBACK\_DEFINE](#ga414a414635e1cd00ef800edaf70bc234)(\_dev, \_callback) |
|  | Register a callback structure for GNSS satellites published. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [gnss\_set\_fix\_rate\_t](#ga79e5975d5ec6c0557af4a71004a6da93)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fix\_interval\_ms) |
|  | API for setting fix rate. |
| typedef int(\* | [gnss\_get\_fix\_rate\_t](#ga63a98e08bc7e4b9c70a27de48dc9cd8c)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*fix\_interval\_ms) |
|  | API for getting fix rate. |
| typedef int(\* | [gnss\_set\_periodic\_config\_t](#ga28c72dd966fd2d2860fc83a405c7b4a1)) (const struct [device](structdevice.md) \*dev, const struct [gnss\_periodic\_config](structgnss__periodic__config.md) \*periodic\_config) |
|  | API for setting periodic tracking configuration. |
| typedef int(\* | [gnss\_get\_periodic\_config\_t](#ga7aae2a68b2cc133861483e16e61240a9)) (const struct [device](structdevice.md) \*dev, struct [gnss\_periodic\_config](structgnss__periodic__config.md) \*periodic\_config) |
|  | API for setting periodic tracking configuration. |
| typedef int(\* | [gnss\_set\_navigation\_mode\_t](#gae946fce6ecced7c8fa09e06d75855abe)) (const struct [device](structdevice.md) \*dev, enum [gnss\_navigation\_mode](#gadb734bb12433276d3014e08a1d21bb18) mode) |
|  | API for setting navigation mode. |
| typedef int(\* | [gnss\_get\_navigation\_mode\_t](#ga9705b36019161fde431e78d943eff604)) (const struct [device](structdevice.md) \*dev, enum [gnss\_navigation\_mode](#gadb734bb12433276d3014e08a1d21bb18) \*mode) |
|  | API for getting navigation mode. |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [gnss\_systems\_t](#ga731907f9ae501909bf26ecae5441a5ce) |
|  | Type storing bitmask of GNSS systems. |
| typedef int(\* | [gnss\_set\_enabled\_systems\_t](#ga91948cc0567c343bee62b6c70a2f461d)) (const struct [device](structdevice.md) \*dev, [gnss\_systems\_t](#ga731907f9ae501909bf26ecae5441a5ce) systems) |
|  | API for enabling systems. |
| typedef int(\* | [gnss\_get\_enabled\_systems\_t](#gad87bd07c46ea1f79caf9a484c51ec0c9)) (const struct [device](structdevice.md) \*dev, [gnss\_systems\_t](#ga731907f9ae501909bf26ecae5441a5ce) \*systems) |
|  | API for getting enabled systems. |
| typedef int(\* | [gnss\_get\_supported\_systems\_t](#gaf52a65dee0d28286ac40e5c8bc86825a)) (const struct [device](structdevice.md) \*dev, [gnss\_systems\_t](#ga731907f9ae501909bf26ecae5441a5ce) \*systems) |
|  | API for getting enabled systems. |
| typedef void(\* | [gnss\_data\_callback\_t](#ga025c965369275ad8e5ab5ad44c14a23b)) (const struct [device](structdevice.md) \*dev, const struct [gnss\_data](structgnss__data.md) \*data) |
|  | Template for GNSS data callback. |
| typedef void(\* | [gnss\_satellites\_callback\_t](#ga80cf700468d1c942cfa064368e212e6f)) (const struct [device](structdevice.md) \*dev, const struct [gnss\_satellite](structgnss__satellite.md) \*satellites, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size) |
|  | Template for GNSS satellites callback. |

| Enumerations | |
| --- | --- |
| enum | [gnss\_pps\_mode](#ga2b43ac2fec33053a769b7070c4ed3263) { [GNSS\_PPS\_MODE\_DISABLED](#gga2b43ac2fec33053a769b7070c4ed3263a5e9af4b08bd41a1aa1bf01c0e290d9fc) = 0 , [GNSS\_PPS\_MODE\_ENABLED](#gga2b43ac2fec33053a769b7070c4ed3263a9cdbb144191c83f4a7a2cc27268eacfa) = 1 , [GNSS\_PPS\_MODE\_ENABLED\_AFTER\_LOCK](#gga2b43ac2fec33053a769b7070c4ed3263a2df416ad912a84135eff1e30977b4507) = 2 , [GNSS\_PPS\_MODE\_ENABLED\_WHILE\_LOCKED](#gga2b43ac2fec33053a769b7070c4ed3263afc82bd9ebcfd9d3b6111c9e82fc79ecc) = 3 } |
|  | GNSS PPS modes. [More...](#ga2b43ac2fec33053a769b7070c4ed3263) |
| enum | [gnss\_navigation\_mode](#gadb734bb12433276d3014e08a1d21bb18) { [GNSS\_NAVIGATION\_MODE\_ZERO\_DYNAMICS](#ggadb734bb12433276d3014e08a1d21bb18a96f01438a205c0d557eb5ea4f80425ff) = 0 , [GNSS\_NAVIGATION\_MODE\_LOW\_DYNAMICS](#ggadb734bb12433276d3014e08a1d21bb18ac5f4b57f2b0f732f9ae8051cb8ac9453) = 1 , [GNSS\_NAVIGATION\_MODE\_BALANCED\_DYNAMICS](#ggadb734bb12433276d3014e08a1d21bb18ab7fd6073a1e7d28ebf6ae9bc51ded88d) = 2 , [GNSS\_NAVIGATION\_MODE\_HIGH\_DYNAMICS](#ggadb734bb12433276d3014e08a1d21bb18a5f57c5f13e22a94c003f582e8c41a27f) = 3 } |
|  | GNSS navigation modes. [More...](#gadb734bb12433276d3014e08a1d21bb18) |
| enum | [gnss\_system](#ga928a05b4e820a9fcc8bc2db81f5f8c79) {     [GNSS\_SYSTEM\_GPS](#gga928a05b4e820a9fcc8bc2db81f5f8c79a84d3fc7ebefad4b20c58335bb7ca3e33) = BIT(0) , [GNSS\_SYSTEM\_GLONASS](#gga928a05b4e820a9fcc8bc2db81f5f8c79a6f5a6de0d8196df55ade83d1f09de7dd) = BIT(1) , [GNSS\_SYSTEM\_GALILEO](#gga928a05b4e820a9fcc8bc2db81f5f8c79a1456923f0dd999b26e167fccc2461d5c) = BIT(2) , [GNSS\_SYSTEM\_BEIDOU](#gga928a05b4e820a9fcc8bc2db81f5f8c79a25a0162daa071267b63d2c7331a46c55) = BIT(3) ,     [GNSS\_SYSTEM\_QZSS](#gga928a05b4e820a9fcc8bc2db81f5f8c79aac9ccafec388c071468ef16981679dff) = BIT(4) , [GNSS\_SYSTEM\_IRNSS](#gga928a05b4e820a9fcc8bc2db81f5f8c79a833e14eb77d70b3c5eb2843026b63242) = BIT(5) , [GNSS\_SYSTEM\_SBAS](#gga928a05b4e820a9fcc8bc2db81f5f8c79a3e759b71b7e531d6c2c3068108e263dd) = BIT(6) , [GNSS\_SYSTEM\_IMES](#gga928a05b4e820a9fcc8bc2db81f5f8c79a6a216ab95d09806435af4257b4d189e9) = BIT(7)   } |
|  | Systems contained in [gnss\_systems\_t](#ga731907f9ae501909bf26ecae5441a5ce). [More...](#ga928a05b4e820a9fcc8bc2db81f5f8c79) |
| enum | [gnss\_fix\_status](#ga15536308e2229a45493d06e8b61e63d9) { [GNSS\_FIX\_STATUS\_NO\_FIX](#gga15536308e2229a45493d06e8b61e63d9a508bbeea1550d5020e579e6a311fbdbe) = 0 , [GNSS\_FIX\_STATUS\_GNSS\_FIX](#gga15536308e2229a45493d06e8b61e63d9a8ad1fb7bf9f4d2607cb86f40a901e343) = 1 , [GNSS\_FIX\_STATUS\_DGNSS\_FIX](#gga15536308e2229a45493d06e8b61e63d9a213553f5fa30cfa99317fcc28d0af1cc) = 2 , [GNSS\_FIX\_STATUS\_ESTIMATED\_FIX](#gga15536308e2229a45493d06e8b61e63d9a19c4e932246f410ee702122d80fbfbeb) = 3 } |
|  | GNSS fix status. [More...](#ga15536308e2229a45493d06e8b61e63d9) |
| enum | [gnss\_fix\_quality](#gacf5a3464c487ae7609d526c73ccc758a) {     [GNSS\_FIX\_QUALITY\_INVALID](#ggacf5a3464c487ae7609d526c73ccc758aa67256fb63beab67ba6e7cbb63916af30) = 0 , [GNSS\_FIX\_QUALITY\_GNSS\_SPS](#ggacf5a3464c487ae7609d526c73ccc758aa316ea7e84abca8f04bbf95d3d73cea3f) = 1 , [GNSS\_FIX\_QUALITY\_DGNSS](#ggacf5a3464c487ae7609d526c73ccc758aa65df312eef5cd8b24384440629f534f8) = 2 , [GNSS\_FIX\_QUALITY\_GNSS\_PPS](#ggacf5a3464c487ae7609d526c73ccc758aab4de07a3891e7c89d5bd23fec7add20f) = 3 ,     [GNSS\_FIX\_QUALITY\_RTK](#ggacf5a3464c487ae7609d526c73ccc758aa5256b22bb56e93c788d52a641c2a15a6) = 4 , [GNSS\_FIX\_QUALITY\_FLOAT\_RTK](#ggacf5a3464c487ae7609d526c73ccc758aaedd76bb21200df49fd82243d4a394ac6) = 5 , [GNSS\_FIX\_QUALITY\_ESTIMATED](#ggacf5a3464c487ae7609d526c73ccc758aa851d88a47c1314eed8bc25e5cc7ba35a) = 6   } |
|  | GNSS fix quality. [More...](#gacf5a3464c487ae7609d526c73ccc758a) |

| Functions | |
| --- | --- |
| int | [gnss\_set\_fix\_rate](#ga16e8326737f114bd6017983812c7f28d) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fix\_interval\_ms) |
|  | Set the GNSS fix rate. |
| int | [gnss\_get\_fix\_rate](#ga8e625fb3f8758eab78c115d12bef6a72) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*fix\_interval\_ms) |
|  | Get the GNSS fix rate. |
| int | [gnss\_set\_periodic\_config](#ga7bc2a97398d2e0621cb2d36546ffae67) (const struct [device](structdevice.md) \*dev, const struct [gnss\_periodic\_config](structgnss__periodic__config.md) \*config) |
|  | Set the GNSS periodic tracking configuration. |
| int | [gnss\_get\_periodic\_config](#ga34c284fda5f2106f796caf3b25ad587c) (const struct [device](structdevice.md) \*dev, struct [gnss\_periodic\_config](structgnss__periodic__config.md) \*config) |
|  | Get the GNSS periodic tracking configuration. |
| int | [gnss\_set\_navigation\_mode](#ga9d0347640e68d5702b1cb43ddf8380df) (const struct [device](structdevice.md) \*dev, enum [gnss\_navigation\_mode](#gadb734bb12433276d3014e08a1d21bb18) mode) |
|  | Set the GNSS navigation mode. |
| int | [gnss\_get\_navigation\_mode](#gae5614f8125dad02a3ebd30400b575e6d) (const struct [device](structdevice.md) \*dev, enum [gnss\_navigation\_mode](#gadb734bb12433276d3014e08a1d21bb18) \*mode) |
|  | Get the GNSS navigation mode. |
| int | [gnss\_set\_enabled\_systems](#ga818e42c7a979623679eba26887662823) (const struct [device](structdevice.md) \*dev, [gnss\_systems\_t](#ga731907f9ae501909bf26ecae5441a5ce) systems) |
|  | Set enabled GNSS systems. |
| int | [gnss\_get\_enabled\_systems](#ga155126e113195c08158ef49e2a6b4f6a) (const struct [device](structdevice.md) \*dev, [gnss\_systems\_t](#ga731907f9ae501909bf26ecae5441a5ce) \*systems) |
|  | Get enabled GNSS systems. |
| int | [gnss\_get\_supported\_systems](#ga598609846ff196ff300fcad8237b2d51) (const struct [device](structdevice.md) \*dev, [gnss\_systems\_t](#ga731907f9ae501909bf26ecae5441a5ce) \*systems) |
|  | Get supported GNSS systems. |

## Detailed Description

GNSS Interface.

Since
:   3.6

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#gae9c3fd5804bd6f8e6790cb1b7e47e4a6)GNSS\_DATA\_CALLBACK\_DEFINE

| #define GNSS\_DATA\_CALLBACK\_DEFINE | ( |  | *\_dev*, |
| --- | --- | --- | --- |
|  |  |  | *\_callback* ) |

`#include <[gnss.h](gnss_8h.md)>`

Register a callback structure for GNSS data published.

Parameters
:   | \_dev | Device pointer |
    | --- | --- |
    | \_callback | The callback function |

## [◆ ](#ga414a414635e1cd00ef800edaf70bc234)GNSS\_SATELLITES\_CALLBACK\_DEFINE

| #define GNSS\_SATELLITES\_CALLBACK\_DEFINE | ( |  | *\_dev*, |
| --- | --- | --- | --- |
|  |  |  | *\_callback* ) |

`#include <[gnss.h](gnss_8h.md)>`

Register a callback structure for GNSS satellites published.

Parameters
:   | \_dev | Device pointer |
    | --- | --- |
    | \_callback | The callback function |

## Typedef Documentation

## [◆ ](#ga025c965369275ad8e5ab5ad44c14a23b)gnss\_data\_callback\_t

| typedef void(\* gnss\_data\_callback\_t) (const struct [device](structdevice.md) \*dev, const struct [gnss\_data](structgnss__data.md) \*data) |
| --- |

`#include <[gnss.h](gnss_8h.md)>`

Template for GNSS data callback.

## [◆ ](#gad87bd07c46ea1f79caf9a484c51ec0c9)gnss\_get\_enabled\_systems\_t

| typedef int(\* gnss\_get\_enabled\_systems\_t) (const struct [device](structdevice.md) \*dev, [gnss\_systems\_t](#ga731907f9ae501909bf26ecae5441a5ce) \*systems) |
| --- |

`#include <[gnss.h](gnss_8h.md)>`

API for getting enabled systems.

## [◆ ](#ga63a98e08bc7e4b9c70a27de48dc9cd8c)gnss\_get\_fix\_rate\_t

| typedef int(\* gnss\_get\_fix\_rate\_t) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*fix\_interval\_ms) |
| --- |

`#include <[gnss.h](gnss_8h.md)>`

API for getting fix rate.

## [◆ ](#ga9705b36019161fde431e78d943eff604)gnss\_get\_navigation\_mode\_t

| typedef int(\* gnss\_get\_navigation\_mode\_t) (const struct [device](structdevice.md) \*dev, enum [gnss\_navigation\_mode](#gadb734bb12433276d3014e08a1d21bb18) \*mode) |
| --- |

`#include <[gnss.h](gnss_8h.md)>`

API for getting navigation mode.

## [◆ ](#ga7aae2a68b2cc133861483e16e61240a9)gnss\_get\_periodic\_config\_t

| typedef int(\* gnss\_get\_periodic\_config\_t) (const struct [device](structdevice.md) \*dev, struct [gnss\_periodic\_config](structgnss__periodic__config.md) \*periodic\_config) |
| --- |

`#include <[gnss.h](gnss_8h.md)>`

API for setting periodic tracking configuration.

## [◆ ](#gaf52a65dee0d28286ac40e5c8bc86825a)gnss\_get\_supported\_systems\_t

| typedef int(\* gnss\_get\_supported\_systems\_t) (const struct [device](structdevice.md) \*dev, [gnss\_systems\_t](#ga731907f9ae501909bf26ecae5441a5ce) \*systems) |
| --- |

`#include <[gnss.h](gnss_8h.md)>`

API for getting enabled systems.

## [◆ ](#ga80cf700468d1c942cfa064368e212e6f)gnss\_satellites\_callback\_t

| typedef void(\* gnss\_satellites\_callback\_t) (const struct [device](structdevice.md) \*dev, const struct [gnss\_satellite](structgnss__satellite.md) \*satellites, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size) |
| --- |

`#include <[gnss.h](gnss_8h.md)>`

Template for GNSS satellites callback.

## [◆ ](#ga91948cc0567c343bee62b6c70a2f461d)gnss\_set\_enabled\_systems\_t

| typedef int(\* gnss\_set\_enabled\_systems\_t) (const struct [device](structdevice.md) \*dev, [gnss\_systems\_t](#ga731907f9ae501909bf26ecae5441a5ce) systems) |
| --- |

`#include <[gnss.h](gnss_8h.md)>`

API for enabling systems.

## [◆ ](#ga79e5975d5ec6c0557af4a71004a6da93)gnss\_set\_fix\_rate\_t

| typedef int(\* gnss\_set\_fix\_rate\_t) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fix\_interval\_ms) |
| --- |

`#include <[gnss.h](gnss_8h.md)>`

API for setting fix rate.

## [◆ ](#gae946fce6ecced7c8fa09e06d75855abe)gnss\_set\_navigation\_mode\_t

| typedef int(\* gnss\_set\_navigation\_mode\_t) (const struct [device](structdevice.md) \*dev, enum [gnss\_navigation\_mode](#gadb734bb12433276d3014e08a1d21bb18) mode) |
| --- |

`#include <[gnss.h](gnss_8h.md)>`

API for setting navigation mode.

## [◆ ](#ga28c72dd966fd2d2860fc83a405c7b4a1)gnss\_set\_periodic\_config\_t

| typedef int(\* gnss\_set\_periodic\_config\_t) (const struct [device](structdevice.md) \*dev, const struct [gnss\_periodic\_config](structgnss__periodic__config.md) \*periodic\_config) |
| --- |

`#include <[gnss.h](gnss_8h.md)>`

API for setting periodic tracking configuration.

## [◆ ](#ga731907f9ae501909bf26ecae5441a5ce)gnss\_systems\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [gnss\_systems\_t](#ga731907f9ae501909bf26ecae5441a5ce) |
| --- |

`#include <[gnss.h](gnss_8h.md)>`

Type storing bitmask of GNSS systems.

## Enumeration Type Documentation

## [◆ ](#gacf5a3464c487ae7609d526c73ccc758a)gnss\_fix\_quality

| enum [gnss\_fix\_quality](#gacf5a3464c487ae7609d526c73ccc758a) |
| --- |

`#include <[gnss.h](gnss_8h.md)>`

GNSS fix quality.

| Enumerator | |
| --- | --- |
| GNSS\_FIX\_QUALITY\_INVALID | Invalid fix. |
| GNSS\_FIX\_QUALITY\_GNSS\_SPS | Standard positioning service. |
| GNSS\_FIX\_QUALITY\_DGNSS | Differential GNSS. |
| GNSS\_FIX\_QUALITY\_GNSS\_PPS | Precise positioning service. |
| GNSS\_FIX\_QUALITY\_RTK | Real-time kinematic. |
| GNSS\_FIX\_QUALITY\_FLOAT\_RTK | Floating real-time kinematic. |
| GNSS\_FIX\_QUALITY\_ESTIMATED | Estimated fix. |

## [◆ ](#ga15536308e2229a45493d06e8b61e63d9)gnss\_fix\_status

| enum [gnss\_fix\_status](#ga15536308e2229a45493d06e8b61e63d9) |
| --- |

`#include <[gnss.h](gnss_8h.md)>`

GNSS fix status.

| Enumerator | |
| --- | --- |
| GNSS\_FIX\_STATUS\_NO\_FIX | No GNSS fix acquired. |
| GNSS\_FIX\_STATUS\_GNSS\_FIX | GNSS fix acquired. |
| GNSS\_FIX\_STATUS\_DGNSS\_FIX | Differential GNSS fix acquired. |
| GNSS\_FIX\_STATUS\_ESTIMATED\_FIX | Estimated fix acquired. |

## [◆ ](#gadb734bb12433276d3014e08a1d21bb18)gnss\_navigation\_mode

| enum [gnss\_navigation\_mode](#gadb734bb12433276d3014e08a1d21bb18) |
| --- |

`#include <[gnss.h](gnss_8h.md)>`

GNSS navigation modes.

| Enumerator | |
| --- | --- |
| GNSS\_NAVIGATION\_MODE\_ZERO\_DYNAMICS | Dynamics have no impact on tracking. |
| GNSS\_NAVIGATION\_MODE\_LOW\_DYNAMICS | Low dynamics have higher impact on tracking. |
| GNSS\_NAVIGATION\_MODE\_BALANCED\_DYNAMICS | Low and high dynamics have equal impact on tracking. |
| GNSS\_NAVIGATION\_MODE\_HIGH\_DYNAMICS | High dynamics have higher impact on tracking. |

## [◆ ](#ga2b43ac2fec33053a769b7070c4ed3263)gnss\_pps\_mode

| enum [gnss\_pps\_mode](#ga2b43ac2fec33053a769b7070c4ed3263) |
| --- |

`#include <[gnss.h](gnss_8h.md)>`

GNSS PPS modes.

| Enumerator | |
| --- | --- |
| GNSS\_PPS\_MODE\_DISABLED | PPS output disabled. |
| GNSS\_PPS\_MODE\_ENABLED | PPS output always enabled. |
| GNSS\_PPS\_MODE\_ENABLED\_AFTER\_LOCK | PPS output enabled from first lock. |
| GNSS\_PPS\_MODE\_ENABLED\_WHILE\_LOCKED | PPS output enabled while locked. |

## [◆ ](#ga928a05b4e820a9fcc8bc2db81f5f8c79)gnss\_system

| enum [gnss\_system](#ga928a05b4e820a9fcc8bc2db81f5f8c79) |
| --- |

`#include <[gnss.h](gnss_8h.md)>`

Systems contained in [gnss\_systems\_t](#ga731907f9ae501909bf26ecae5441a5ce).

| Enumerator | |
| --- | --- |
| GNSS\_SYSTEM\_GPS | Global Positioning System (GPS). |
| GNSS\_SYSTEM\_GLONASS | GLObal NAvigation Satellite System (GLONASS). |
| GNSS\_SYSTEM\_GALILEO | Galileo. |
| GNSS\_SYSTEM\_BEIDOU | BeiDou Navigation Satellite System. |
| GNSS\_SYSTEM\_QZSS | Quasi-Zenith Satellite System (QZSS). |
| GNSS\_SYSTEM\_IRNSS | Indian Regional Navigation Satellite System (IRNSS). |
| GNSS\_SYSTEM\_SBAS | Satellite-Based Augmentation System (SBAS). |
| GNSS\_SYSTEM\_IMES | Indoor Messaging System (IMES). |

## Function Documentation

## [◆ ](#ga155126e113195c08158ef49e2a6b4f6a)gnss\_get\_enabled\_systems()

| int gnss\_get\_enabled\_systems | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [gnss\_systems\_t](#ga731907f9ae501909bf26ecae5441a5ce) \* | *systems* ) |

`#include <[gnss.h](gnss_8h.md)>`

Get enabled GNSS systems.

Parameters
:   | dev | Device instance |
    | --- | --- |
    | systems | Destination for enabled systems |

Returns
:   0 if successful
:   -errno negative errno code on failure

## [◆ ](#ga8e625fb3f8758eab78c115d12bef6a72)gnss\_get\_fix\_rate()

| int gnss\_get\_fix\_rate | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *fix\_interval\_ms* ) |

`#include <[gnss.h](gnss_8h.md)>`

Get the GNSS fix rate.

Parameters
:   | dev | Device instance |
    | --- | --- |
    | fix\_interval\_ms | Destination for fix interval in milliseconds |

Returns
:   0 if successful
:   -errno negative errno code on failure

## [◆ ](#gae5614f8125dad02a3ebd30400b575e6d)gnss\_get\_navigation\_mode()

| int gnss\_get\_navigation\_mode | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [gnss\_navigation\_mode](#gadb734bb12433276d3014e08a1d21bb18) \* | *mode* ) |

`#include <[gnss.h](gnss_8h.md)>`

Get the GNSS navigation mode.

Parameters
:   | dev | Device instance |
    | --- | --- |
    | mode | Destination for navigation mode |

Returns
:   0 if successful
:   -errno negative errno code on failure

## [◆ ](#ga34c284fda5f2106f796caf3b25ad587c)gnss\_get\_periodic\_config()

| int gnss\_get\_periodic\_config | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [gnss\_periodic\_config](structgnss__periodic__config.md) \* | *config* ) |

`#include <[gnss.h](gnss_8h.md)>`

Get the GNSS periodic tracking configuration.

Parameters
:   | dev | Device instance |
    | --- | --- |
    | config | Destination for periodic tracking configuration |

Returns
:   0 if successful
:   -errno negative errno code on failure

## [◆ ](#ga598609846ff196ff300fcad8237b2d51)gnss\_get\_supported\_systems()

| int gnss\_get\_supported\_systems | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [gnss\_systems\_t](#ga731907f9ae501909bf26ecae5441a5ce) \* | *systems* ) |

`#include <[gnss.h](gnss_8h.md)>`

Get supported GNSS systems.

Parameters
:   | dev | Device instance |
    | --- | --- |
    | systems | Destination for supported systems |

Returns
:   0 if successful
:   -errno negative errno code on failure

## [◆ ](#ga818e42c7a979623679eba26887662823)gnss\_set\_enabled\_systems()

| int gnss\_set\_enabled\_systems | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [gnss\_systems\_t](#ga731907f9ae501909bf26ecae5441a5ce) | *systems* ) |

`#include <[gnss.h](gnss_8h.md)>`

Set enabled GNSS systems.

Parameters
:   | dev | Device instance |
    | --- | --- |
    | systems | Systems to enable |

Returns
:   0 if successful
:   -errno negative errno code on failure

## [◆ ](#ga16e8326737f114bd6017983812c7f28d)gnss\_set\_fix\_rate()

| int gnss\_set\_fix\_rate | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *fix\_interval\_ms* ) |

`#include <[gnss.h](gnss_8h.md)>`

Set the GNSS fix rate.

Parameters
:   | dev | Device instance |
    | --- | --- |
    | fix\_interval\_ms | Fix interval to set in milliseconds |

Returns
:   0 if successful
:   -errno negative errno code on failure

## [◆ ](#ga9d0347640e68d5702b1cb43ddf8380df)gnss\_set\_navigation\_mode()

| int gnss\_set\_navigation\_mode | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [gnss\_navigation\_mode](#gadb734bb12433276d3014e08a1d21bb18) | *mode* ) |

`#include <[gnss.h](gnss_8h.md)>`

Set the GNSS navigation mode.

Parameters
:   | dev | Device instance |
    | --- | --- |
    | mode | Navigation mode to set |

Returns
:   0 if successful
:   -errno negative errno code on failure

## [◆ ](#ga7bc2a97398d2e0621cb2d36546ffae67)gnss\_set\_periodic\_config()

| int gnss\_set\_periodic\_config | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [gnss\_periodic\_config](structgnss__periodic__config.md) \* | *config* ) |

`#include <[gnss.h](gnss_8h.md)>`

Set the GNSS periodic tracking configuration.

Parameters
:   | dev | Device instance |
    | --- | --- |
    | config | Periodic tracking configuration to set |

Returns
:   0 if successful
:   -errno negative errno code on failure

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

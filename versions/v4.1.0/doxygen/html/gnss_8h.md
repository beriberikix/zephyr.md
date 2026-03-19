---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/gnss_8h.html
original_path: doxygen/html/gnss_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gnss.h File Reference

Public GNSS API.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/data/navigation.h](navigation_8h_source.md)>`  
`#include <[errno.h](errno_8h_source.md)>`  
`#include <zephyr/syscalls/gnss.h>`

[Go to the source code of this file.](gnss_8h_source.md)

| Data Structures | |
| --- | --- |
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
| #define | [GNSS\_DATA\_CALLBACK\_DEFINE](group__gnss__interface.md#gae9c3fd5804bd6f8e6790cb1b7e47e4a6)(\_dev, \_callback) |
|  | Register a callback structure for GNSS data published. |
| #define | [GNSS\_SATELLITES\_CALLBACK\_DEFINE](group__gnss__interface.md#ga414a414635e1cd00ef800edaf70bc234)(\_dev, \_callback) |
|  | Register a callback structure for GNSS satellites published. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [gnss\_set\_fix\_rate\_t](group__gnss__interface.md#ga79e5975d5ec6c0557af4a71004a6da93)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fix\_interval\_ms) |
|  | API for setting fix rate. |
| typedef int(\* | [gnss\_get\_fix\_rate\_t](group__gnss__interface.md#ga63a98e08bc7e4b9c70a27de48dc9cd8c)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*fix\_interval\_ms) |
|  | API for getting fix rate. |
| typedef int(\* | [gnss\_set\_navigation\_mode\_t](group__gnss__interface.md#gae946fce6ecced7c8fa09e06d75855abe)) (const struct [device](structdevice.md) \*dev, enum [gnss\_navigation\_mode](group__gnss__interface.md#gadb734bb12433276d3014e08a1d21bb18) mode) |
|  | API for setting navigation mode. |
| typedef int(\* | [gnss\_get\_navigation\_mode\_t](group__gnss__interface.md#ga9705b36019161fde431e78d943eff604)) (const struct [device](structdevice.md) \*dev, enum [gnss\_navigation\_mode](group__gnss__interface.md#gadb734bb12433276d3014e08a1d21bb18) \*mode) |
|  | API for getting navigation mode. |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [gnss\_systems\_t](group__gnss__interface.md#ga731907f9ae501909bf26ecae5441a5ce) |
|  | Type storing bitmask of GNSS systems. |
| typedef int(\* | [gnss\_set\_enabled\_systems\_t](group__gnss__interface.md#ga91948cc0567c343bee62b6c70a2f461d)) (const struct [device](structdevice.md) \*dev, [gnss\_systems\_t](group__gnss__interface.md#ga731907f9ae501909bf26ecae5441a5ce) systems) |
|  | API for enabling systems. |
| typedef int(\* | [gnss\_get\_enabled\_systems\_t](group__gnss__interface.md#gad87bd07c46ea1f79caf9a484c51ec0c9)) (const struct [device](structdevice.md) \*dev, [gnss\_systems\_t](group__gnss__interface.md#ga731907f9ae501909bf26ecae5441a5ce) \*systems) |
|  | API for getting enabled systems. |
| typedef int(\* | [gnss\_get\_supported\_systems\_t](group__gnss__interface.md#gaf52a65dee0d28286ac40e5c8bc86825a)) (const struct [device](structdevice.md) \*dev, [gnss\_systems\_t](group__gnss__interface.md#ga731907f9ae501909bf26ecae5441a5ce) \*systems) |
|  | API for getting enabled systems. |
| typedef int(\* | [gnss\_get\_latest\_timepulse\_t](group__gnss__interface.md#gaa482aa8a996b743aba7e68f36b4780a8)) (const struct [device](structdevice.md) \*dev, [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) \*timestamp) |
|  | API for getting timestamp of last PPS pulse. |
| typedef void(\* | [gnss\_data\_callback\_t](group__gnss__interface.md#ga025c965369275ad8e5ab5ad44c14a23b)) (const struct [device](structdevice.md) \*dev, const struct [gnss\_data](structgnss__data.md) \*data) |
|  | Template for GNSS data callback. |
| typedef void(\* | [gnss\_satellites\_callback\_t](group__gnss__interface.md#ga80cf700468d1c942cfa064368e212e6f)) (const struct [device](structdevice.md) \*dev, const struct [gnss\_satellite](structgnss__satellite.md) \*satellites, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size) |
|  | Template for GNSS satellites callback. |

| Enumerations | |
| --- | --- |
| enum | [gnss\_pps\_mode](group__gnss__interface.md#ga2b43ac2fec33053a769b7070c4ed3263) { [GNSS\_PPS\_MODE\_DISABLED](group__gnss__interface.md#gga2b43ac2fec33053a769b7070c4ed3263a5e9af4b08bd41a1aa1bf01c0e290d9fc) = 0 , [GNSS\_PPS\_MODE\_ENABLED](group__gnss__interface.md#gga2b43ac2fec33053a769b7070c4ed3263a9cdbb144191c83f4a7a2cc27268eacfa) = 1 , [GNSS\_PPS\_MODE\_ENABLED\_AFTER\_LOCK](group__gnss__interface.md#gga2b43ac2fec33053a769b7070c4ed3263a2df416ad912a84135eff1e30977b4507) = 2 , [GNSS\_PPS\_MODE\_ENABLED\_WHILE\_LOCKED](group__gnss__interface.md#gga2b43ac2fec33053a769b7070c4ed3263afc82bd9ebcfd9d3b6111c9e82fc79ecc) = 3 } |
|  | GNSS PPS modes. [More...](group__gnss__interface.md#ga2b43ac2fec33053a769b7070c4ed3263) |
| enum | [gnss\_navigation\_mode](group__gnss__interface.md#gadb734bb12433276d3014e08a1d21bb18) { [GNSS\_NAVIGATION\_MODE\_ZERO\_DYNAMICS](group__gnss__interface.md#ggadb734bb12433276d3014e08a1d21bb18a96f01438a205c0d557eb5ea4f80425ff) = 0 , [GNSS\_NAVIGATION\_MODE\_LOW\_DYNAMICS](group__gnss__interface.md#ggadb734bb12433276d3014e08a1d21bb18ac5f4b57f2b0f732f9ae8051cb8ac9453) = 1 , [GNSS\_NAVIGATION\_MODE\_BALANCED\_DYNAMICS](group__gnss__interface.md#ggadb734bb12433276d3014e08a1d21bb18ab7fd6073a1e7d28ebf6ae9bc51ded88d) = 2 , [GNSS\_NAVIGATION\_MODE\_HIGH\_DYNAMICS](group__gnss__interface.md#ggadb734bb12433276d3014e08a1d21bb18a5f57c5f13e22a94c003f582e8c41a27f) = 3 } |
|  | GNSS navigation modes. [More...](group__gnss__interface.md#gadb734bb12433276d3014e08a1d21bb18) |
| enum | [gnss\_system](group__gnss__interface.md#ga928a05b4e820a9fcc8bc2db81f5f8c79) {     [GNSS\_SYSTEM\_GPS](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79a84d3fc7ebefad4b20c58335bb7ca3e33) = BIT(0) , [GNSS\_SYSTEM\_GLONASS](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79a6f5a6de0d8196df55ade83d1f09de7dd) = BIT(1) , [GNSS\_SYSTEM\_GALILEO](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79a1456923f0dd999b26e167fccc2461d5c) = BIT(2) , [GNSS\_SYSTEM\_BEIDOU](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79a25a0162daa071267b63d2c7331a46c55) = BIT(3) ,     [GNSS\_SYSTEM\_QZSS](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79aac9ccafec388c071468ef16981679dff) = BIT(4) , [GNSS\_SYSTEM\_IRNSS](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79a833e14eb77d70b3c5eb2843026b63242) = BIT(5) , [GNSS\_SYSTEM\_SBAS](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79a3e759b71b7e531d6c2c3068108e263dd) = BIT(6) , [GNSS\_SYSTEM\_IMES](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79a6a216ab95d09806435af4257b4d189e9) = BIT(7)   } |
|  | Systems contained in [gnss\_systems\_t](group__gnss__interface.md#ga731907f9ae501909bf26ecae5441a5ce "Type storing bitmask of GNSS systems."). [More...](group__gnss__interface.md#ga928a05b4e820a9fcc8bc2db81f5f8c79) |
| enum | [gnss\_fix\_status](group__gnss__interface.md#ga15536308e2229a45493d06e8b61e63d9) { [GNSS\_FIX\_STATUS\_NO\_FIX](group__gnss__interface.md#gga15536308e2229a45493d06e8b61e63d9a508bbeea1550d5020e579e6a311fbdbe) = 0 , [GNSS\_FIX\_STATUS\_GNSS\_FIX](group__gnss__interface.md#gga15536308e2229a45493d06e8b61e63d9a8ad1fb7bf9f4d2607cb86f40a901e343) = 1 , [GNSS\_FIX\_STATUS\_DGNSS\_FIX](group__gnss__interface.md#gga15536308e2229a45493d06e8b61e63d9a213553f5fa30cfa99317fcc28d0af1cc) = 2 , [GNSS\_FIX\_STATUS\_ESTIMATED\_FIX](group__gnss__interface.md#gga15536308e2229a45493d06e8b61e63d9a19c4e932246f410ee702122d80fbfbeb) = 3 } |
|  | GNSS fix status. [More...](group__gnss__interface.md#ga15536308e2229a45493d06e8b61e63d9) |
| enum | [gnss\_fix\_quality](group__gnss__interface.md#gacf5a3464c487ae7609d526c73ccc758a) {     [GNSS\_FIX\_QUALITY\_INVALID](group__gnss__interface.md#ggacf5a3464c487ae7609d526c73ccc758aa67256fb63beab67ba6e7cbb63916af30) = 0 , [GNSS\_FIX\_QUALITY\_GNSS\_SPS](group__gnss__interface.md#ggacf5a3464c487ae7609d526c73ccc758aa316ea7e84abca8f04bbf95d3d73cea3f) = 1 , [GNSS\_FIX\_QUALITY\_DGNSS](group__gnss__interface.md#ggacf5a3464c487ae7609d526c73ccc758aa65df312eef5cd8b24384440629f534f8) = 2 , [GNSS\_FIX\_QUALITY\_GNSS\_PPS](group__gnss__interface.md#ggacf5a3464c487ae7609d526c73ccc758aab4de07a3891e7c89d5bd23fec7add20f) = 3 ,     [GNSS\_FIX\_QUALITY\_RTK](group__gnss__interface.md#ggacf5a3464c487ae7609d526c73ccc758aa5256b22bb56e93c788d52a641c2a15a6) = 4 , [GNSS\_FIX\_QUALITY\_FLOAT\_RTK](group__gnss__interface.md#ggacf5a3464c487ae7609d526c73ccc758aaedd76bb21200df49fd82243d4a394ac6) = 5 , [GNSS\_FIX\_QUALITY\_ESTIMATED](group__gnss__interface.md#ggacf5a3464c487ae7609d526c73ccc758aa851d88a47c1314eed8bc25e5cc7ba35a) = 6   } |
|  | GNSS fix quality. [More...](group__gnss__interface.md#gacf5a3464c487ae7609d526c73ccc758a) |

| Functions | |
| --- | --- |
| int | [gnss\_set\_fix\_rate](group__gnss__interface.md#ga16e8326737f114bd6017983812c7f28d) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fix\_interval\_ms) |
|  | Set the GNSS fix rate. |
| int | [gnss\_get\_fix\_rate](group__gnss__interface.md#ga8e625fb3f8758eab78c115d12bef6a72) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*fix\_interval\_ms) |
|  | Get the GNSS fix rate. |
| int | [gnss\_set\_navigation\_mode](group__gnss__interface.md#ga9d0347640e68d5702b1cb43ddf8380df) (const struct [device](structdevice.md) \*dev, enum [gnss\_navigation\_mode](group__gnss__interface.md#gadb734bb12433276d3014e08a1d21bb18) mode) |
|  | Set the GNSS navigation mode. |
| int | [gnss\_get\_navigation\_mode](group__gnss__interface.md#gae5614f8125dad02a3ebd30400b575e6d) (const struct [device](structdevice.md) \*dev, enum [gnss\_navigation\_mode](group__gnss__interface.md#gadb734bb12433276d3014e08a1d21bb18) \*mode) |
|  | Get the GNSS navigation mode. |
| int | [gnss\_set\_enabled\_systems](group__gnss__interface.md#ga818e42c7a979623679eba26887662823) (const struct [device](structdevice.md) \*dev, [gnss\_systems\_t](group__gnss__interface.md#ga731907f9ae501909bf26ecae5441a5ce) systems) |
|  | Set enabled GNSS systems. |
| int | [gnss\_get\_enabled\_systems](group__gnss__interface.md#ga155126e113195c08158ef49e2a6b4f6a) (const struct [device](structdevice.md) \*dev, [gnss\_systems\_t](group__gnss__interface.md#ga731907f9ae501909bf26ecae5441a5ce) \*systems) |
|  | Get enabled GNSS systems. |
| int | [gnss\_get\_supported\_systems](group__gnss__interface.md#ga598609846ff196ff300fcad8237b2d51) (const struct [device](structdevice.md) \*dev, [gnss\_systems\_t](group__gnss__interface.md#ga731907f9ae501909bf26ecae5441a5ce) \*systems) |
|  | Get supported GNSS systems. |
| int | [gnss\_get\_latest\_timepulse](group__gnss__interface.md#ga8eb37446d71c020e0517a406ea240fc2) (const struct [device](structdevice.md) \*dev, [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) \*timestamp) |
|  | Get the timestamp of the latest PPS timepulse. |

## Detailed Description

Public GNSS API.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [gnss.h](gnss_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

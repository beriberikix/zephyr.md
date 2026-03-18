---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structieee802154__config.html
original_path: doxygen/html/structieee802154__config.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ieee802154\_config Struct Reference

[Connectivity](group__connectivity.md) » [IEEE 802.15.4 and Thread APIs](group__ieee802154.md) » [IEEE 802.15.4 Drivers](group__ieee802154__driver.md)

IEEE 802.15.4 driver configuration data.
[More...](#details)

`#include <[ieee802154_radio.h](ieee802154__radio_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| struct { |  |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [enabled](#ad9361f9ba1652e46d0be25e0de39afdf) |  |
| enum [ieee802154\_fpb\_mode](group__ieee802154__driver.md#gab593bc6640ddea23c951982ca2f4c0bf)   [mode](#ad139acde94327d4b8ceb76760751521d) |  |
| }   [auto\_ack\_fpb](#ab27a654a0d53f268199e95dc21e18fd4) |
|  | see [IEEE802154\_CONFIG\_AUTO\_ACK\_FPB](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a38c67aac70d24b31996871fe4686d9ee "IEEE802154_CONFIG_AUTO_ACK_FPB") [More...](#ab27a654a0d53f268199e95dc21e18fd4) |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*   [addr](#a673f5cceb6439bc1c3527c62062151d1) |  |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [extended](#a55823097d62a69d0c92dc70fb4ff1dd5) |  |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [enabled](#ad9361f9ba1652e46d0be25e0de39afdf) |  |
| }   [ack\_fpb](#a3a5e597e53bfcc9e3bed8bac2edb74d2) |
|  | see [IEEE802154\_CONFIG\_ACK\_FPB](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09ab897aea56ea5e9ddf306c5c0d75c2cd7 "IEEE802154_CONFIG_ACK_FPB") [More...](#a3a5e597e53bfcc9e3bed8bac2edb74d2) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [pan\_coordinator](#a078ec577af3d170781ed770c80c54b72) |  |
|  | see [IEEE802154\_CONFIG\_PAN\_COORDINATOR](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09ab2b6ae3034fb469168ed29704ec045f0 "IEEE802154_CONFIG_PAN_COORDINATOR") [More...](#a078ec577af3d170781ed770c80c54b72) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [promiscuous](#aafb11c4130ff39e5c40dfe5d32c0d4e7) |  |
|  | see [IEEE802154\_CONFIG\_PROMISCUOUS](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a399313ff2d8ebb3a2d72152a9615d8c5 "IEEE802154_CONFIG_PROMISCUOUS") [More...](#aafb11c4130ff39e5c40dfe5d32c0d4e7) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [rx\_on\_when\_idle](#a8b7d4804cd051d69f3602f35cb4a8630) |  |
|  | see [IEEE802154\_CONFIG\_RX\_ON\_WHEN\_IDLE](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a9228dbe2583e5be10f64b116e87645e1 "IEEE802154_CONFIG_RX_ON_WHEN_IDLE") [More...](#a8b7d4804cd051d69f3602f35cb4a8630) |
| [ieee802154\_event\_cb\_t](group__ieee802154__driver.md#ga8219b80b8b179fc3a2ffac0dfdfb4e4b)   [event\_handler](#a1558e71a1d5ab74990964ff4deabbdb7) |  |
|  | see [IEEE802154\_CONFIG\_EVENT\_HANDLER](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a8d88a76f71cf8869b3e35e423b18c6f3 "IEEE802154_CONFIG_EVENT_HANDLER") [More...](#a1558e71a1d5ab74990964ff4deabbdb7) |
| struct [ieee802154\_key](structieee802154__key.md) \*   [mac\_keys](#a942c0d4fb244c7256530536dc132a727) |  |
|  | see [IEEE802154\_CONFIG\_MAC\_KEYS](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a8bd29c6d6aa67adaf23415eb337904c0 "IEEE802154_CONFIG_MAC_KEYS") [More...](#a942c0d4fb244c7256530536dc132a727) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [frame\_counter](#a272cfd864c7d47c6f06f26871ce07fb6) |  |
|  | see [IEEE802154\_CONFIG\_FRAME\_COUNTER](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09aad7d04b7e1c02b2d88fcbb8ab1ac313b "IEEE802154_CONFIG_FRAME_COUNTER") [More...](#a272cfd864c7d47c6f06f26871ce07fb6) |
| struct { |  |
| [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56)   [start](#a86b72101b0b21622f3cc8a2b3877e356) |  |
|  | Nanosecond resolution timestamp relative to the network subsystem's local clock defining the start of the RX window during which the receiver is expected to be listening (i.e. [More...](#a86b72101b0b21622f3cc8a2b3877e356) |
| [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56)   [duration](#ab36833b4311b03f08f67290f4edd8e41) |  |
|  | Nanosecond resolution duration of the RX window relative to the above RX window start time during which the receiver is expected to be listening (i.e. [More...](#ab36833b4311b03f08f67290f4edd8e41) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [channel](#a8f7efaa743e070479632d139f0fc57c0) |  |
| }   [rx\_slot](#aadc2714bf31484cce071e9ef7b9a4007) |
|  | see [IEEE802154\_CONFIG\_RX\_SLOT](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09af4e3dd7588ee06458f2d42f02797b3d6 "IEEE802154_CONFIG_RX_SLOT") [More...](#aadc2714bf31484cce071e9ef7b9a4007) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [csl\_period](#a5106a759148ec20c6c6c83a2581c9e88) |  |
|  | see [IEEE802154\_CONFIG\_CSL\_PERIOD](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a9fdbe95e0b7141d9150eaa4a5793c2e7 "IEEE802154_CONFIG_CSL_PERIOD") [More...](#a5106a759148ec20c6c6c83a2581c9e88) |
| [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56)   [expected\_rx\_time](#a8124aed4a4af36c0e21fd8f1b1c97e3e) |  |
|  | see [IEEE802154\_CONFIG\_EXPECTED\_RX\_TIME](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a1a71ef76d90b6882196e4c6473de6bd8 "IEEE802154_CONFIG_EXPECTED_RX_TIME") [More...](#a8124aed4a4af36c0e21fd8f1b1c97e3e) |
| struct { |  |
| struct [ieee802154\_header\_ie](structieee802154__header__ie.md) \*   [header\_ie](#a5343dec0de835943c0bef2c2d603a91d) |  |
|  | Pointer to the header IE, see section 7.4.2.1, figure 7-21. [More...](#a5343dec0de835943c0bef2c2d603a91d) |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*   [ext\_addr](#a03d6ec1a371312961f3a1ee42e113bbf) |  |
|  | Filters the devices that will receive this IE by extended address. [More...](#a03d6ec1a371312961f3a1ee42e113bbf) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [short\_addr](#aa27066dd9e54dab6795332b7413670f5) |  |
|  | Filters the devices that will receive this IE by short address. [More...](#aa27066dd9e54dab6795332b7413670f5) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [purge\_ie](#a8971a91be8748bd45027fcb730b99639) |  |
|  | Flag for purging enh ACK header IEs. [More...](#a8971a91be8748bd45027fcb730b99639) |
| }   [ack\_ie](#a39c06e32cb4a74b4d8a9864f714e8c93) |
|  | see [IEEE802154\_CONFIG\_ENH\_ACK\_HEADER\_IE](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a840e5f1db9a354e7bcd892ddb4117907 "IEEE802154_CONFIG_ENH_ACK_HEADER_IE") [More...](#a39c06e32cb4a74b4d8a9864f714e8c93) |
| }; |  |
|  | Configuration data. |

## Detailed Description

IEEE 802.15.4 driver configuration data.

## Field Documentation

## [◆ ](#a4e62cce9f7735b5bb3a53b95d886b13d)[union]

| union { ... } [ieee802154\_config](structieee802154__config.md) |
| --- |

Configuration data.

## [◆ ](#a3a5e597e53bfcc9e3bed8bac2edb74d2)[struct]

| struct { ... } ieee802154\_config::ack\_fpb |
| --- |

see [IEEE802154\_CONFIG\_ACK\_FPB](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09ab897aea56ea5e9ddf306c5c0d75c2cd7 "IEEE802154_CONFIG_ACK_FPB")

## [◆ ](#a39c06e32cb4a74b4d8a9864f714e8c93)[struct]

| struct { ... } ieee802154\_config::ack\_ie |
| --- |

see [IEEE802154\_CONFIG\_ENH\_ACK\_HEADER\_IE](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a840e5f1db9a354e7bcd892ddb4117907 "IEEE802154_CONFIG_ENH_ACK_HEADER_IE")

## [◆ ](#a673f5cceb6439bc1c3527c62062151d1)addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* ieee802154\_config::addr |
| --- |

## [◆ ](#ab27a654a0d53f268199e95dc21e18fd4)[struct]

| struct { ... } ieee802154\_config::auto\_ack\_fpb |
| --- |

see [IEEE802154\_CONFIG\_AUTO\_ACK\_FPB](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a38c67aac70d24b31996871fe4686d9ee "IEEE802154_CONFIG_AUTO_ACK_FPB")

## [◆ ](#a8f7efaa743e070479632d139f0fc57c0)channel

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ieee802154\_config::channel |
| --- |

## [◆ ](#a5106a759148ec20c6c6c83a2581c9e88)csl\_period

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ieee802154\_config::csl\_period |
| --- |

see [IEEE802154\_CONFIG\_CSL\_PERIOD](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a9fdbe95e0b7141d9150eaa4a5793c2e7 "IEEE802154_CONFIG_CSL_PERIOD")

in CPU byte order

## [◆ ](#ab36833b4311b03f08f67290f4edd8e41)duration

| [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) ieee802154\_config::duration |
| --- |

Nanosecond resolution duration of the RX window relative to the above RX window start time during which the receiver is expected to be listening (i.e.

not including any shutdown times). Only positive values larger than or equal zero are allowed.

Setting the duration to zero will disable the receiver, no matter what the start parameter.

## [◆ ](#ad9361f9ba1652e46d0be25e0de39afdf)enabled

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ieee802154\_config::enabled |
| --- |

## [◆ ](#a1558e71a1d5ab74990964ff4deabbdb7)event\_handler

| [ieee802154\_event\_cb\_t](group__ieee802154__driver.md#ga8219b80b8b179fc3a2ffac0dfdfb4e4b) ieee802154\_config::event\_handler |
| --- |

see [IEEE802154\_CONFIG\_EVENT\_HANDLER](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a8d88a76f71cf8869b3e35e423b18c6f3 "IEEE802154_CONFIG_EVENT_HANDLER")

## [◆ ](#a8124aed4a4af36c0e21fd8f1b1c97e3e)expected\_rx\_time

| [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) ieee802154\_config::expected\_rx\_time |
| --- |

see [IEEE802154\_CONFIG\_EXPECTED\_RX\_TIME](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a1a71ef76d90b6882196e4c6473de6bd8 "IEEE802154_CONFIG_EXPECTED_RX_TIME")

## [◆ ](#a03d6ec1a371312961f3a1ee42e113bbf)ext\_addr

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* ieee802154\_config::ext\_addr |
| --- |

Filters the devices that will receive this IE by extended address.

MAY be set to NULL to configure a fallback for all devices (implies that short\_addr MUST also be set to [IEEE802154\_BROADCAST\_ADDRESS](group__ieee802154__l2.md#gafae1906dc9b39c93690b127efaaacacb "IEEE802154_BROADCAST_ADDRESS")).

in big endian

## [◆ ](#a55823097d62a69d0c92dc70fb4ff1dd5)extended

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ieee802154\_config::extended |
| --- |

## [◆ ](#a272cfd864c7d47c6f06f26871ce07fb6)frame\_counter

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ieee802154\_config::frame\_counter |
| --- |

see [IEEE802154\_CONFIG\_FRAME\_COUNTER](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09aad7d04b7e1c02b2d88fcbb8ab1ac313b "IEEE802154_CONFIG_FRAME_COUNTER")

## [◆ ](#a5343dec0de835943c0bef2c2d603a91d)header\_ie

| struct [ieee802154\_header\_ie](structieee802154__header__ie.md)\* ieee802154\_config::header\_ie |
| --- |

Pointer to the header IE, see section 7.4.2.1, figure 7-21.

Certain header IEs may be incomplete if they require timing information to be injected at runtime on-the-fly, see the list in [IEEE802154\_CONFIG\_ENH\_ACK\_HEADER\_IE](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a840e5f1db9a354e7bcd892ddb4117907 "IEEE802154_CONFIG_ENH_ACK_HEADER_IE").

## [◆ ](#a942c0d4fb244c7256530536dc132a727)mac\_keys

| struct [ieee802154\_key](structieee802154__key.md)\* ieee802154\_config::mac\_keys |
| --- |

see [IEEE802154\_CONFIG\_MAC\_KEYS](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a8bd29c6d6aa67adaf23415eb337904c0 "IEEE802154_CONFIG_MAC_KEYS")

Pointer to an array containing a list of keys used for MAC encryption. Refer to secKeyIdLookupDescriptor and secKeyDescriptor in IEEE 802.15.4

The key\_value field points to a buffer containing the 16 byte key. The buffer SHALL be copied by the driver before returning from the call.

The variable length array is terminated by key\_value field set to NULL.

## [◆ ](#ad139acde94327d4b8ceb76760751521d)mode

| enum [ieee802154\_fpb\_mode](group__ieee802154__driver.md#gab593bc6640ddea23c951982ca2f4c0bf) ieee802154\_config::mode |
| --- |

## [◆ ](#a078ec577af3d170781ed770c80c54b72)pan\_coordinator

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ieee802154\_config::pan\_coordinator |
| --- |

see [IEEE802154\_CONFIG\_PAN\_COORDINATOR](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09ab2b6ae3034fb469168ed29704ec045f0 "IEEE802154_CONFIG_PAN_COORDINATOR")

## [◆ ](#aafb11c4130ff39e5c40dfe5d32c0d4e7)promiscuous

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ieee802154\_config::promiscuous |
| --- |

see [IEEE802154\_CONFIG\_PROMISCUOUS](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a399313ff2d8ebb3a2d72152a9615d8c5 "IEEE802154_CONFIG_PROMISCUOUS")

## [◆ ](#a8971a91be8748bd45027fcb730b99639)purge\_ie

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ieee802154\_config::purge\_ie |
| --- |

Flag for purging enh ACK header IEs.

When flag is set to true, driver should remove all existing header IEs, and all other entries in config should be ignored. This means that purging current header IEs and configuring a new one in the same call is not allowed.

## [◆ ](#a8b7d4804cd051d69f3602f35cb4a8630)rx\_on\_when\_idle

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ieee802154\_config::rx\_on\_when\_idle |
| --- |

see [IEEE802154\_CONFIG\_RX\_ON\_WHEN\_IDLE](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a9228dbe2583e5be10f64b116e87645e1 "IEEE802154_CONFIG_RX_ON_WHEN_IDLE")

## [◆ ](#aadc2714bf31484cce071e9ef7b9a4007)[struct]

| struct { ... } ieee802154\_config::rx\_slot |
| --- |

see [IEEE802154\_CONFIG\_RX\_SLOT](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09af4e3dd7588ee06458f2d42f02797b3d6 "IEEE802154_CONFIG_RX_SLOT")

## [◆ ](#aa27066dd9e54dab6795332b7413670f5)short\_addr

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ieee802154\_config::short\_addr |
| --- |

Filters the devices that will receive this IE by short address.

MAY be set to [IEEE802154\_BROADCAST\_ADDRESS](group__ieee802154__l2.md#gafae1906dc9b39c93690b127efaaacacb "IEEE802154_BROADCAST_ADDRESS") to configure a fallback for all devices (implies that ext\_addr MUST also set to NULL in this case).

in CPU byte order

## [◆ ](#a86b72101b0b21622f3cc8a2b3877e356)start

| [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) ieee802154\_config::start |
| --- |

Nanosecond resolution timestamp relative to the network subsystem's local clock defining the start of the RX window during which the receiver is expected to be listening (i.e.

not including any driver startup times).

Configuring an rx\_slot with the start attribute set to -1 will cancel and delete any previously active rx slot.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ieee802154\_radio.h](ieee802154__radio_8h_source.md)

- [ieee802154\_config](structieee802154__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

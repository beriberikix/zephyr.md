---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ieee802154__radio_8h.html
original_path: doxygen/html/ieee802154__radio_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ieee802154\_radio.h File Reference

Public IEEE 802.15.4 Driver API.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/net/net_if.h](net__if_8h_source.md)>`  
`#include <[zephyr/net/net_pkt.h](net__pkt_8h_source.md)>`  
`#include <[zephyr/net/net_time.h](net__time_8h_source.md)>`  
`#include <[zephyr/net/ieee802154.h](ieee802154_8h_source.md)>`  
`#include <[zephyr/net/ieee802154_ie.h](ieee802154__ie_8h_source.md)>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`

[Go to the source code of this file.](ieee802154__radio_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [ieee802154\_phy\_channel\_range](structieee802154__phy__channel__range.md) |
|  | Represents a supported channel range, see [ieee802154\_phy\_supported\_channels](structieee802154__phy__supported__channels.md "ieee802154_phy_supported_channels"). [More...](structieee802154__phy__channel__range.md#details) |
| struct | [ieee802154\_phy\_supported\_channels](structieee802154__phy__supported__channels.md) |
|  | Represents a list channels supported by a driver for a given interface, see [IEEE802154\_ATTR\_PHY\_SUPPORTED\_CHANNEL\_RANGES](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430aba76daa0a70bcdd573ecbfd63ca19e7d "IEEE802154_ATTR_PHY_SUPPORTED_CHANNEL_RANGES"). [More...](structieee802154__phy__supported__channels.md#details) |
| struct | [ieee802154\_filter](structieee802154__filter.md) |
|  | Filter value, see [ieee802154\_radio\_api::filter](structieee802154__radio__api.md#aa9502e0e014a8d05ffe235567e8c98f3 "ieee802154_radio_api::filter"). [More...](structieee802154__filter.md#details) |
| struct | [ieee802154\_key](structieee802154__key.md) |
|  | Key configuration for transmit security offloading, see [IEEE802154\_CONFIG\_MAC\_KEYS](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a8bd29c6d6aa67adaf23415eb337904c0 "IEEE802154_CONFIG_MAC_KEYS"). [More...](structieee802154__key.md#details) |
| struct | [ieee802154\_config](structieee802154__config.md) |
|  | IEEE 802.15.4 driver configuration data. [More...](structieee802154__config.md#details) |
| struct | [ieee802154\_attr\_value](structieee802154__attr__value.md) |
|  | IEEE 802.15.4 driver attribute values. [More...](structieee802154__attr__value.md#details) |
| struct | [ieee802154\_radio\_api](structieee802154__radio__api.md) |
|  | IEEE 802.15.4 driver interface API. [More...](structieee802154__radio__api.md#details) |

| Macros | |
| --- | --- |
| IEEE 802.15.4-2020, Section 6: MAC functional description | |
| #define | [IEEE802154\_PHY\_SYMBOLS\_PER\_SECOND](group__ieee802154__driver.md#gaf228d9c26cedd5c790b7ebae41b5f937)(symbol\_period\_ns) |
|  | The symbol period (and therefore symbol rate) is defined in section 6.1: "Some of the timing parameters in definition of the MAC are in units of PHY symbols. |
| IEEE 802.15.4-2020, Section 8: MAC services | |
| #define | [IEEE802154\_MAC\_A\_BASE\_SLOT\_DURATION](group__ieee802154__driver.md#gadb590005c9120e6b04aa430ebb306b8f)   60U |
|  | The number of PHY symbols forming a superframe slot when the superframe order is equal to zero, see sections 8.4.2, table 8-93, aBaseSlotDuration and section 6.2.1. |
| #define | [IEEE802154\_MAC\_A\_NUM\_SUPERFRAME\_SLOTS](group__ieee802154__driver.md#ga662c1add47deb9807e848aeeee5e6842)   16U |
|  | The number of slots contained in any superframe, see section 8.4.2, table 8-93, aNumSuperframeSlots. |
| #define | [IEEE802154\_MAC\_A\_BASE\_SUPERFRAME\_DURATION](group__ieee802154__driver.md#ga52358c63c386b72f190d3b487c9ba286)   ([IEEE802154\_MAC\_A\_BASE\_SLOT\_DURATION](group__ieee802154__driver.md#gadb590005c9120e6b04aa430ebb306b8f) \* [IEEE802154\_MAC\_A\_NUM\_SUPERFRAME\_SLOTS](group__ieee802154__driver.md#ga662c1add47deb9807e848aeeee5e6842)) |
|  | The number of PHY symbols forming a superframe when the superframe order is equal to zero, see section 8.4.2, table 8-93, aBaseSuperframeDuration. |
| #define | [IEEE802154\_MAC\_A\_UNIT\_BACKOFF\_PERIOD](group__ieee802154__driver.md#ga86f3186304b02de3096d521238d407db)(turnaround\_time) |
|  | MAC PIB attribute aUnitBackoffPeriod, see section 8.4.2, table 8-93, in symbol periods, valid for all PHYs except SUN PHY in the 920 MHz band. |
| #define | [IEEE802154\_MAC\_RESPONSE\_WAIT\_TIME\_DEFAULT](group__ieee802154__driver.md#ga132be1037c5db1311c6d0c7d74e1fe40)   32U |
|  | Default macResponseWaitTime in multiples of aBaseSuperframeDuration as defined in section 8.4.3.1, table 8-94. |
| IEEE 802.15.4-2020, Section 11: PHY services | |
| #define | [IEEE802154\_PHY\_A\_TURNAROUND\_TIME\_DEFAULT](group__ieee802154__driver.md#ga9e95bf5d8ddb1087cdd9eb2aa80d100e)   12U |
|  | Default PHY PIB attribute aTurnaroundTime, in PHY symbols, see section 11.3, table 11-1. |
| #define | [IEEE802154\_PHY\_A\_TURNAROUND\_TIME\_1MS](group__ieee802154__driver.md#ga68115b80097b116b704431808469450b)(symbol\_period\_ns) |
|  | PHY PIB attribute aTurnaroundTime for SUN, RS-GFSK, TVWS, and LECIM FSK PHY, in PHY symbols, see section 11.3, table 11-1. |
| #define | [IEEE802154\_PHY\_A\_CCA\_TIME](group__ieee802154__driver.md#gaf58b5d421167c2075dcdfdbaba5956dd)   8U |
|  | PHY PIB attribute aCcaTime, in PHY symbols, all PHYs except for SUN O-QPSK, see section 11.3, table 11-1. |
| IEEE 802.15.4-2020, Section 12: O-QPSK PHY | |
| #define | [IEEE802154\_PHY\_OQPSK\_868MHZ\_SYMBOL\_PERIOD\_NS](group__ieee802154__driver.md#ga32ce931f3d35d779e4251c37f61583f5)   40000LL |
|  | O-QPSK 868Mhz band symbol period, see section 12.3.3. |
| #define | [IEEE802154\_PHY\_OQPSK\_780\_TO\_2450MHZ\_SYMBOL\_PERIOD\_NS](group__ieee802154__driver.md#gaff3d58945d53e824f1fb1ca11dd9997b)   16000LL |
|  | O-QPSK 780MHz, 915MHz, 2380MHz and 2450MHz bands symbol period, see section 12.3.3. |
| IEEE 802.15.4-2020, Section 13: BPSK PHY | |
| #define | [IEEE802154\_PHY\_BPSK\_868MHZ\_SYMBOL\_PERIOD\_NS](group__ieee802154__driver.md#ga1dc4319d0a8d979c7455e1f71f45d885)   50000LL |
|  | BPSK 868MHz band symbol period, see section 13.3.3. |
| #define | [IEEE802154\_PHY\_BPSK\_915MHZ\_SYMBOL\_PERIOD\_NS](group__ieee802154__driver.md#gaa12344b6a118995b63c5bd4bc3180efd)   25000LL |
|  | BPSK 915MHz band symbol period, see section 13.3.3. |
| IEEE 802.15.4-2020, Section 19: SUN FSK PHY | |
| #define | [IEEE802154\_PHY\_SUN\_FSK\_863MHZ\_915MHZ\_SYMBOL\_PERIOD\_NS](group__ieee802154__driver.md#ga155b5b5a06311c1bde3f36e06d02ed7d)   20000LL |
|  | SUN FSK 863Mhz and 915MHz band symbol periods, see section 19.1, table 19-1. |
| #define | [IEEE802154\_PHY\_SUN\_FSK\_PHR\_LEN](group__ieee802154__driver.md#gac088ee6d01014a12169e74111ea61993)   2 |
|  | SUN FSK PHY header length, in bytes, see section 19.2.4. |

| Functions | |
| --- | --- |
| IEEE 802.15.4 driver utils | |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [ieee802154\_is\_ar\_flag\_set](group__ieee802154__driver.md#gaf5d7bdde2a9774f9d90604a6e203bb07) (struct [net\_buf](structnet__buf.md) \*frag) |
|  | Check if the AR flag is set on the frame inside the given [Network Packet Library](group__net__pkt.md "Network Packet Library"). |
| IEEE 802.15.4 driver callbacks | |
| enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) | [ieee802154\_handle\_ack](group__ieee802154__driver.md#ga68e1f89571ccbefef61a5496577337fc) (struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | IEEE 802.15.4 driver ACK handling callback into L2 that drivers must call when receiving an ACK package. |
| void | [ieee802154\_init](group__ieee802154__driver.md#gad2a4cb5df84ffe20b83fc54dc9bcfc91) (struct [net\_if](structnet__if.md) \*iface) |
|  | IEEE 802.15.4 driver initialization callback into L2 called by drivers to initialize the active L2 stack for a given interface. |

| IEEE 802.15.4-2020, Section 10: General PHY requirements | |
| --- | --- |
| #define | [IEEE802154\_DEFINE\_PHY\_SUPPORTED\_CHANNELS](group__ieee802154__driver.md#ga78d4df389a7bd11c55e5c7b683897a9b)(drv\_attr, from, to) |
|  | Allocate memory for the supported channels driver attribute with a single channel range constant across all driver instances. |
| enum | [ieee802154\_phy\_channel\_page](group__ieee802154__driver.md#gacabc7386bea701373dfb36ab65bd36a9) {     [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_ZERO\_OQPSK\_2450\_BPSK\_868\_915](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a72b17a977aeb6792f7d2016117f4b2f9) = BIT(0) , [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_ONE\_DEPRECATED](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a371a12ec5d762b03058fb2532fa04e45) = BIT(1) , [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_TWO\_OQPSK\_868\_915](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a5776e0160927b83f4e4e8d6479aaf804) = BIT(2) , [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_THREE\_CSS](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a6f71c162be118b0c2edce139753c867e) = BIT(3) ,     [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_FOUR\_HRP\_UWB](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a68b93381ddc1184ff0ed13456cf4b6a8) = BIT(4) , [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_FIVE\_OQPSK\_780](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a6ea456573a6ff8aed348a9dc547b2db7) = BIT(5) , [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_SIX\_RESERVED](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9ac13dda08becd3d4799d45ef02f774cc1) = BIT(6) , [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_SEVEN\_MSK](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a1f33467ec7659ef411b08f7a23663311) = BIT(7) ,     [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_EIGHT\_LRP\_UWB](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9aa0ab080c8cdac42dbf80622d075854dc) = BIT(8) , [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_NINE\_SUN\_PREDEFINED](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a996b529c9c277d6d653d0e0ffb8b2902) = BIT(9) , [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_TEN\_SUN\_FSK\_GENERIC](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a02a17ea787e99528b2a6a8f5107f2544) = BIT(10) , [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_ELEVEN\_OQPSK\_2380](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9aad0644244fb5b6cba5a295e246722e94) = BIT(11) ,     [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_TWELVE\_LECIM](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a6d4023088a3607c072acebd3940340c7) = BIT(12) , [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_THIRTEEN\_RCC](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a56dd4ae42595ef0edb109c729e333b08) = BIT(13)   } |
|  | PHY channel pages, see section 10.1.3. [More...](group__ieee802154__driver.md#gacabc7386bea701373dfb36ab65bd36a9) |

| IEEE 802.15.4-2020, Section 15: HRP UWB PHY | |
| --- | --- |
| For HRP UWB the symbol period is derived from the preamble symbol period (T\_psym), see section 11.3, table 11-1 and section 15.2.5, table 15-4 (confirmed in IEEE 802.15.4z, section 15.1). Choosing among those periods cannot be done based on channel page and channel alone. The mean pulse repetition frequency must also be known, see the 'UwbPrf' parameter of the MCPS-DATA.request primitive (section 8.3.2, table 8-88) and the preamble parameters for HRP-ERDEV length 91 codes (IEEE 802.15.4z, section 15.2.6.2, table 15-7b). | |
| #define | [IEEE802154\_PHY\_HRP\_UWB\_PRF4\_TPSYM\_SYMBOL\_PERIOD\_NS](group__ieee802154__driver.md#gabeb8a359ce54618aa7df3ee8f6a434bb)   3974.36F |
|  | Nominal PRF 4MHz symbol period. |
| #define | [IEEE802154\_PHY\_HRP\_UWB\_PRF16\_TPSYM\_SYMBOL\_PERIOD\_NS](group__ieee802154__driver.md#ga0123679fba7ca668aa158813f1bf2302)   993.59F |
|  | Nominal PRF 16MHz symbol period. |
| #define | [IEEE802154\_PHY\_HRP\_UWB\_PRF64\_TPSYM\_SYMBOL\_PERIOD\_NS](group__ieee802154__driver.md#ga59f8ba8a01171c56da6f7ae7f8983bf7)   1017.63F |
|  | Nominal PRF 64MHz symbol period. |
| #define | [IEEE802154\_PHY\_HRP\_UWB\_ERDEV\_TPSYM\_SYMBOL\_PERIOD\_NS](group__ieee802154__driver.md#gaa25ba5b644e58cfc7de5ba5aa526ea71)   729.17F |
|  | ERDEV symbol period. |
| #define | [IEEE802154\_PHY\_HRP\_UWB\_RDEV](group__ieee802154__driver.md#gacfd2faf2c3072f8851abd74fe5148ec5) |
|  | RDEV device mask. |
| #define | [IEEE802154\_PHY\_HRP\_UWB\_ERDEV](group__ieee802154__driver.md#gae02b981a3908b05b4bc0b7a2844c27c7) |
|  | ERDEV device mask. |
| enum | [ieee802154\_phy\_hrp\_uwb\_nominal\_prf](group__ieee802154__driver.md#ga13610aeef06372bc47d84464537fdded) {     [IEEE802154\_PHY\_HRP\_UWB\_PRF\_OFF](group__ieee802154__driver.md#gga13610aeef06372bc47d84464537fddeda4369c745ed378d8273a1014322f3029a) = 0 , [IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_4\_M](group__ieee802154__driver.md#gga13610aeef06372bc47d84464537fddeda9dc3c58366502aeab04a208937536369) = BIT(0) , [IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_16\_M](group__ieee802154__driver.md#gga13610aeef06372bc47d84464537fddedadf9230e6ef62ce66129bfe24f537c88a) = BIT(1) , [IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_64\_M](group__ieee802154__driver.md#gga13610aeef06372bc47d84464537fddeda2b24236d3531cab7d21673d065b7c29e) = BIT(2) ,     [IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_64\_M\_BPRF](group__ieee802154__driver.md#gga13610aeef06372bc47d84464537fddedad920ae285cdcc2a4d59f7c23e29dce27) = BIT(3) , [IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_128\_M\_HPRF](group__ieee802154__driver.md#gga13610aeef06372bc47d84464537fddedae6c88efd301a449b1a31e8aedf4e30ca) = BIT(4) , [IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_256\_M\_HPRF](group__ieee802154__driver.md#gga13610aeef06372bc47d84464537fddedacb66442cf2a5e4c539b6b7edf8419be1) = BIT(5)   } |
|  | represents the nominal pulse rate frequency of an HRP UWB PHY [More...](group__ieee802154__driver.md#ga13610aeef06372bc47d84464537fdded) |

| IEEE 802.15.4 Driver API | |
| --- | --- |
| #define | [IEEE802154\_HW\_CAPS\_BITS\_COMMON\_COUNT](group__ieee802154__driver.md#gaf143a9f110a2eb6b21104af6927159bc)   (13) |
|  | Number of bits used by [ieee802154\_hw\_caps](group__ieee802154__driver.md#gaf99cda89c29df3c0088fc57ec09cbcd4 "IEEE 802.15.4 driver capabilities.") type. |
| #define | [IEEE802154\_HW\_CAPS\_BITS\_PRIV\_START](group__ieee802154__driver.md#ga40912ccb268768b4e96ce9cad35476af)   [IEEE802154\_HW\_CAPS\_BITS\_COMMON\_COUNT](group__ieee802154__driver.md#gaf143a9f110a2eb6b21104af6927159bc) |
|  | This and higher values are specific to the protocol- or driver-specific extensions. |
| #define | [IEEE802154\_CONFIG\_RX\_SLOT\_NONE](group__ieee802154__driver.md#ga1cb6434a3a7555fe9d35c73b698cbf10)   -1LL |
|  | Configuring an RX slot with the start parameter set to this value will cancel and delete any previously configured RX slot. |
| #define | [IEEE802154\_CONFIG\_RX\_SLOT\_OFF](group__ieee802154__driver.md#ga3828a2d56a39de92c2fd79caaac4c800)   0LL |
|  | Configuring an RX slot with this start parameter while the driver is "down", will keep RX off when the driver is being started. |
| enum | [ieee802154\_hw\_caps](group__ieee802154__driver.md#gaf99cda89c29df3c0088fc57ec09cbcd4) {     [IEEE802154\_HW\_ENERGY\_SCAN](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a179ad073a5bd34e4e4af587d07ca3f73) = BIT(0) , [IEEE802154\_HW\_FCS](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a0ea21cab335dd9082feb2d08be0eb5fa) = BIT(1) , [IEEE802154\_HW\_FILTER](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4afd09f329a708d00f1384a50c59ddde27) = BIT(2) , [IEEE802154\_HW\_PROMISC](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a4adb33f2ca81a24244dead6b379cd916) = BIT(3) ,     [IEEE802154\_HW\_CSMA](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a2ee53f11e1ed6853e1f5d9dfe7d7bdf7) = BIT(4) , [IEEE802154\_HW\_TX\_RX\_ACK](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4ab383a932c0ac9deece68f02210089119) = BIT(5) , [IEEE802154\_HW\_RETRANSMISSION](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a752472a994bdcbdf9cdf86deb0231849) = BIT(6) , [IEEE802154\_HW\_RX\_TX\_ACK](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4aec16c4d418117de2d106e84297568b03) = BIT(7) ,     [IEEE802154\_HW\_TXTIME](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a435d032f42d509bd78a992de6e4d7b1d) = BIT(8) , [IEEE802154\_HW\_SLEEP\_TO\_TX](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a36f46639c08e70bc30fc98ca1043b071) = BIT(9) , [IEEE802154\_HW\_RXTIME](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a68ae68c83a87f0efc25f74edd80c4600) = BIT(10) , [IEEE802154\_HW\_TX\_SEC](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a7924c3d5bfe6dceeb2e8caa6df7edecb) = BIT(11) ,     [IEEE802154\_RX\_ON\_WHEN\_IDLE](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4ac1e00966043e5884c4cbd65fb26f0c0b) = BIT(12)   } |
|  | IEEE 802.15.4 driver capabilities. [More...](group__ieee802154__driver.md#gaf99cda89c29df3c0088fc57ec09cbcd4) |
| enum | [ieee802154\_filter\_type](group__ieee802154__driver.md#gaa1971591e72866d0f3f0d4db2931e25a) {     [IEEE802154\_FILTER\_TYPE\_IEEE\_ADDR](group__ieee802154__driver.md#ggaa1971591e72866d0f3f0d4db2931e25aa928a93b536c6408b3d77aa329c274fe8) , [IEEE802154\_FILTER\_TYPE\_SHORT\_ADDR](group__ieee802154__driver.md#ggaa1971591e72866d0f3f0d4db2931e25aa2fa1ac98a3b870fcf6e85e7ec82cfbe9) , [IEEE802154\_FILTER\_TYPE\_PAN\_ID](group__ieee802154__driver.md#ggaa1971591e72866d0f3f0d4db2931e25aab44cc830999926a5d232aedabef52653) , [IEEE802154\_FILTER\_TYPE\_SRC\_IEEE\_ADDR](group__ieee802154__driver.md#ggaa1971591e72866d0f3f0d4db2931e25aade18e03611339f5f7ec4fdcdee409c21) ,     [IEEE802154\_FILTER\_TYPE\_SRC\_SHORT\_ADDR](group__ieee802154__driver.md#ggaa1971591e72866d0f3f0d4db2931e25aac6dbb68674e7594fd4cd69bbe4ea60de)   } |
|  | Filter type, see [ieee802154\_radio\_api::filter](structieee802154__radio__api.md#aa9502e0e014a8d05ffe235567e8c98f3 "ieee802154_radio_api::filter"). [More...](group__ieee802154__driver.md#gaa1971591e72866d0f3f0d4db2931e25a) |
| enum | [ieee802154\_event](group__ieee802154__driver.md#ga3491982b677941442d904ce69fce7c5e) { [IEEE802154\_EVENT\_TX\_STARTED](group__ieee802154__driver.md#gga3491982b677941442d904ce69fce7c5eaacd61f4466f1ef926adc9e1afe6c1648) , [IEEE802154\_EVENT\_RX\_FAILED](group__ieee802154__driver.md#gga3491982b677941442d904ce69fce7c5eaef51197ca09befaee8cdfa2cde107273) , [IEEE802154\_EVENT\_RX\_OFF](group__ieee802154__driver.md#gga3491982b677941442d904ce69fce7c5eaf7ed46b9d13a232a2ea6b650514eea3d) } |
|  | Driver events, see [IEEE802154\_CONFIG\_EVENT\_HANDLER](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a8d88a76f71cf8869b3e35e423b18c6f3 "IEEE802154_CONFIG_EVENT_HANDLER"). [More...](group__ieee802154__driver.md#ga3491982b677941442d904ce69fce7c5e) |
| enum | [ieee802154\_rx\_fail\_reason](group__ieee802154__driver.md#ga04febbd15f9e6f6540d711ada5a4a1c8) { [IEEE802154\_RX\_FAIL\_NOT\_RECEIVED](group__ieee802154__driver.md#gga04febbd15f9e6f6540d711ada5a4a1c8ad584824b4813626d04a85499371b9c32) , [IEEE802154\_RX\_FAIL\_INVALID\_FCS](group__ieee802154__driver.md#gga04febbd15f9e6f6540d711ada5a4a1c8a103f6683ff71f4f7248ee1a0d09d6be4) , [IEEE802154\_RX\_FAIL\_ADDR\_FILTERED](group__ieee802154__driver.md#gga04febbd15f9e6f6540d711ada5a4a1c8a7ff9cfcc5e4dfc2bf7abe1860a39410f) , [IEEE802154\_RX\_FAIL\_OTHER](group__ieee802154__driver.md#gga04febbd15f9e6f6540d711ada5a4a1c8a5baa9dd683a717f7fbdfc5ab85935a3b) } |
|  | RX failed event reasons, see [IEEE802154\_EVENT\_RX\_FAILED](group__ieee802154__driver.md#gga3491982b677941442d904ce69fce7c5eaef51197ca09befaee8cdfa2cde107273 "IEEE802154_EVENT_RX_FAILED"). [More...](group__ieee802154__driver.md#ga04febbd15f9e6f6540d711ada5a4a1c8) |
| enum | [ieee802154\_tx\_mode](group__ieee802154__driver.md#gab2bee8752291e082cb277145cef1225d) {     [IEEE802154\_TX\_MODE\_DIRECT](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225da6904c3c7f53d46c5c8b41dd1a82b2650) , [IEEE802154\_TX\_MODE\_CCA](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225da1e23f1ad3f9d0832fd4d67fc00fd8eb5) , [IEEE802154\_TX\_MODE\_CSMA\_CA](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225da51a0e7cb482447779634062655a1ec47) , [IEEE802154\_TX\_MODE\_TXTIME](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225da9a7b8ba25603b72aecbf7f66abf26508) ,     [IEEE802154\_TX\_MODE\_TXTIME\_CCA](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225da42b4589afb2180fde053fdbbf58c0d3e) , [IEEE802154\_TX\_MODE\_COMMON\_COUNT](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225daa389aeccad62a0516678564e68fcd595) , [IEEE802154\_TX\_MODE\_PRIV\_START](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225dabbab0c864f313ee4045e5ad59ea774e2) = IEEE802154\_TX\_MODE\_COMMON\_COUNT   } |
|  | IEEE 802.15.4 Transmission mode. [More...](group__ieee802154__driver.md#gab2bee8752291e082cb277145cef1225d) |
| enum | [ieee802154\_fpb\_mode](group__ieee802154__driver.md#gab593bc6640ddea23c951982ca2f4c0bf) { [IEEE802154\_FPB\_ADDR\_MATCH\_THREAD](group__ieee802154__driver.md#ggab593bc6640ddea23c951982ca2f4c0bfa012874ab4d234bbeb2954756cf2dc9d6) , [IEEE802154\_FPB\_ADDR\_MATCH\_ZIGBEE](group__ieee802154__driver.md#ggab593bc6640ddea23c951982ca2f4c0bfac7c839b7c0649d6151f90ff1d51ae417) } |
|  | IEEE 802.15.4 Frame Pending Bit table address matching mode. [More...](group__ieee802154__driver.md#gab593bc6640ddea23c951982ca2f4c0bf) |
| enum | [ieee802154\_config\_type](group__ieee802154__driver.md#ga34aecc5996174a812b295a3a4693ad09) {     [IEEE802154\_CONFIG\_AUTO\_ACK\_FPB](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a38c67aac70d24b31996871fe4686d9ee) , [IEEE802154\_CONFIG\_ACK\_FPB](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09ab897aea56ea5e9ddf306c5c0d75c2cd7) , [IEEE802154\_CONFIG\_PAN\_COORDINATOR](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09ab2b6ae3034fb469168ed29704ec045f0) , [IEEE802154\_CONFIG\_PROMISCUOUS](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a399313ff2d8ebb3a2d72152a9615d8c5) ,     [IEEE802154\_CONFIG\_EVENT\_HANDLER](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a8d88a76f71cf8869b3e35e423b18c6f3) , [IEEE802154\_CONFIG\_MAC\_KEYS](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a8bd29c6d6aa67adaf23415eb337904c0) , [IEEE802154\_CONFIG\_FRAME\_COUNTER](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09aad7d04b7e1c02b2d88fcbb8ab1ac313b) , [IEEE802154\_CONFIG\_FRAME\_COUNTER\_IF\_LARGER](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09aa34da77f0966ff5a0e8ac73ed68554a8) ,     [IEEE802154\_CONFIG\_RX\_SLOT](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09af4e3dd7588ee06458f2d42f02797b3d6) , [IEEE802154\_CONFIG\_CSL\_PERIOD](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a9fdbe95e0b7141d9150eaa4a5793c2e7) , [IEEE802154\_CONFIG\_EXPECTED\_RX\_TIME](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a1a71ef76d90b6882196e4c6473de6bd8) , [IEEE802154\_CONFIG\_ENH\_ACK\_HEADER\_IE](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a840e5f1db9a354e7bcd892ddb4117907) ,     [IEEE802154\_CONFIG\_RX\_ON\_WHEN\_IDLE](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a9228dbe2583e5be10f64b116e87645e1) , [IEEE802154\_CONFIG\_COMMON\_COUNT](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a61df14aeb348cfc694d539b506dc23ac) , [IEEE802154\_CONFIG\_PRIV\_START](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a1653b2869208045415d83fc6708d015c) = IEEE802154\_CONFIG\_COMMON\_COUNT   } |
|  | IEEE 802.15.4 driver configuration types. [More...](group__ieee802154__driver.md#ga34aecc5996174a812b295a3a4693ad09) |
| enum | [ieee802154\_attr](group__ieee802154__driver.md#gaf4deddd3f23ebfd65fa47c5d62634430) {     [IEEE802154\_ATTR\_PHY\_SUPPORTED\_CHANNEL\_PAGES](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430a4ad28f920776c45af9d430db786a926a) , [IEEE802154\_ATTR\_PHY\_SUPPORTED\_CHANNEL\_RANGES](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430aba76daa0a70bcdd573ecbfd63ca19e7d) , [IEEE802154\_ATTR\_PHY\_HRP\_UWB\_SUPPORTED\_PRFS](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430ad90b4a118866c4942ef6f6a8ae56eb3f) , [IEEE802154\_ATTR\_COMMON\_COUNT](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430aa0830214987de7a89297777c0d1004de) ,     [IEEE802154\_ATTR\_PRIV\_START](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430ad4912dc68abc1abe54bc212f023bf511) = IEEE802154\_ATTR\_COMMON\_COUNT   } |
|  | IEEE 802.15.4 driver attributes. [More...](group__ieee802154__driver.md#gaf4deddd3f23ebfd65fa47c5d62634430) |
| typedef void(\* | [energy\_scan\_done\_cb\_t](group__ieee802154__driver.md#ga8c9ab3cecefe641a25f003eb6d014fc5)) (const struct [device](structdevice.md) \*dev, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) max\_ed) |
|  | Energy scan callback. |
| typedef void(\* | [ieee802154\_event\_cb\_t](group__ieee802154__driver.md#ga8219b80b8b179fc3a2ffac0dfdfb4e4b)) (const struct [device](structdevice.md) \*dev, enum [ieee802154\_event](group__ieee802154__driver.md#ga3491982b677941442d904ce69fce7c5e) evt, void \*event\_params) |
|  | Driver event callback. |
| static int | [ieee802154\_attr\_get\_channel\_page\_and\_range](group__ieee802154__driver.md#gaf69d2b65aa46ec4483c6bab419413ba5) (enum [ieee802154\_attr](group__ieee802154__driver.md#gaf4deddd3f23ebfd65fa47c5d62634430) attr, const enum [ieee802154\_phy\_channel\_page](group__ieee802154__driver.md#gacabc7386bea701373dfb36ab65bd36a9) phy\_supported\_channel\_page, const struct [ieee802154\_phy\_supported\_channels](structieee802154__phy__supported__channels.md) \*phy\_supported\_channels, struct [ieee802154\_attr\_value](structieee802154__attr__value.md) \*value) |
|  | Helper function to handle channel page and range to be called from drivers' attr\_get() implementation. |

## Detailed Description

Public IEEE 802.15.4 Driver API.

Note
:   All references to the standard in this file cite IEEE 802.15.4-2020.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ieee802154\_radio.h](ieee802154__radio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

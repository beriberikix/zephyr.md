---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__ieee802154__driver.html
original_path: doxygen/html/group__ieee802154__driver.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

IEEE 802.15.4 Drivers

[Connectivity](group__connectivity.md) » [IEEE 802.15.4 and Thread APIs](group__ieee802154.md)

IEEE 802.15.4 driver API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [ieee802154\_header\_ie\_vendor\_specific](structieee802154__header__ie__vendor__specific.md) |
|  | Vendor Specific Header IE, see section 7.4.2.3. [More...](structieee802154__header__ie__vendor__specific.md#details) |
| struct | [ieee802154\_header\_ie\_csl\_full](structieee802154__header__ie__csl__full.md) |
|  | Full CSL IE, see section 7.4.2.3. [More...](structieee802154__header__ie__csl__full.md#details) |
| struct | [ieee802154\_header\_ie\_csl\_reduced](structieee802154__header__ie__csl__reduced.md) |
|  | Reduced CSL IE, see section 7.4.2.3. [More...](structieee802154__header__ie__csl__reduced.md#details) |
| struct | [ieee802154\_header\_ie\_csl](structieee802154__header__ie__csl.md) |
|  | Generic CSL IE, see section 7.4.2.3. [More...](structieee802154__header__ie__csl.md#details) |
| struct | [ieee802154\_header\_ie\_rit](structieee802154__header__ie__rit.md) |
|  | RIT IE, see section 7.4.2.4. [More...](structieee802154__header__ie__rit.md#details) |
| struct | [ieee802154\_header\_ie\_rendezvous\_time\_full](structieee802154__header__ie__rendezvous__time__full.md) |
|  | Full Rendezvous Time IE, see section 7.4.2.6 (macCslInterval is nonzero). [More...](structieee802154__header__ie__rendezvous__time__full.md#details) |
| struct | [ieee802154\_header\_ie\_rendezvous\_time\_reduced](structieee802154__header__ie__rendezvous__time__reduced.md) |
|  | Reduced Rendezvous Time IE, see section 7.4.2.6 (macCslInterval is zero). [More...](structieee802154__header__ie__rendezvous__time__reduced.md#details) |
| struct | [ieee802154\_header\_ie\_rendezvous\_time](structieee802154__header__ie__rendezvous__time.md) |
|  | Rendezvous Time IE, see section 7.4.2.6. [More...](structieee802154__header__ie__rendezvous__time.md#details) |
| struct | [ieee802154\_header\_ie\_time\_correction](structieee802154__header__ie__time__correction.md) |
|  | Time Correction IE, see section 7.4.2.7. [More...](structieee802154__header__ie__time__correction.md#details) |
| struct | [ieee802154\_phy\_channel\_range](structieee802154__phy__channel__range.md) |
|  | Represents a supported channel range, see [ieee802154\_phy\_supported\_channels](structieee802154__phy__supported__channels.md "ieee802154_phy_supported_channels"). [More...](structieee802154__phy__channel__range.md#details) |
| struct | [ieee802154\_phy\_supported\_channels](structieee802154__phy__supported__channels.md) |
|  | Represents a list channels supported by a driver for a given interface, see [IEEE802154\_ATTR\_PHY\_SUPPORTED\_CHANNEL\_RANGES](#ggaf4deddd3f23ebfd65fa47c5d62634430aba76daa0a70bcdd573ecbfd63ca19e7d). [More...](structieee802154__phy__supported__channels.md#details) |
| struct | [ieee802154\_filter](structieee802154__filter.md) |
|  | Filter value, see [ieee802154\_radio\_api::filter](structieee802154__radio__api.md#aa9502e0e014a8d05ffe235567e8c98f3 "ieee802154_radio_api::filter"). [More...](structieee802154__filter.md#details) |
| struct | [ieee802154\_key](structieee802154__key.md) |
|  | Key configuration for transmit security offloading, see [IEEE802154\_CONFIG\_MAC\_KEYS](#gga34aecc5996174a812b295a3a4693ad09a8bd29c6d6aa67adaf23415eb337904c0). [More...](structieee802154__key.md#details) |
| struct | [ieee802154\_config](structieee802154__config.md) |
|  | IEEE 802.15.4 driver configuration data. [More...](structieee802154__config.md#details) |
| struct | [ieee802154\_attr\_value](structieee802154__attr__value.md) |
|  | IEEE 802.15.4 driver attribute values. [More...](structieee802154__attr__value.md#details) |
| struct | [ieee802154\_radio\_api](structieee802154__radio__api.md) |
|  | IEEE 802.15.4 driver interface API. [More...](structieee802154__radio__api.md#details) |

| IEEE 802.15.4, section 7.4.2: MAC header information elements | |
| --- | --- |
| enum | [ieee802154\_ie\_type](#ga207e3aa0454f9e4173c809cfe7ff32cd) { [IEEE802154\_IE\_TYPE\_HEADER](#gga207e3aa0454f9e4173c809cfe7ff32cda6891d992dc8d592ed8bd95cf836cab1a) = 0x0 , [IEEE802154\_IE\_TYPE\_PAYLOAD](#gga207e3aa0454f9e4173c809cfe7ff32cda87905298e0b0920f9da8053129471af7) } |
|  | Information Element Types. [More...](#ga207e3aa0454f9e4173c809cfe7ff32cd) |
| enum | [ieee802154\_header\_ie\_element\_id](#ga0de396c2c2c781ff85b94ebf577f15ce) {     [IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_VENDOR\_SPECIFIC\_IE](#gga0de396c2c2c781ff85b94ebf577f15ceaf02726c8c317ee15e92c1d43b4392c14) = 0x00 , [IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_CSL\_IE](#gga0de396c2c2c781ff85b94ebf577f15cea69e4548081815bd45ea68c52d1b66efb) = 0x1a , [IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_RIT\_IE](#gga0de396c2c2c781ff85b94ebf577f15ceaffc141c8eebdc4b39df6d7b314b8e021) = 0x1b , [IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_RENDEZVOUS\_TIME\_IE](#gga0de396c2c2c781ff85b94ebf577f15cea12b16ed83f7b7fb952b86c151af65e5e) = 0x1d ,     [IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_TIME\_CORRECTION\_IE](#gga0de396c2c2c781ff85b94ebf577f15cea3f050528506d59ba26a100e42a182330) = 0x1e , [IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_HEADER\_TERMINATION\_1](#gga0de396c2c2c781ff85b94ebf577f15cea5034cb0963de1fd64a9018937cfeaec3) = 0x7e , [IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_HEADER\_TERMINATION\_2](#gga0de396c2c2c781ff85b94ebf577f15ceabd8d5a5fe12f978ace7eb5a089df6941) = 0x7f   } |
|  | Header Information Element IDs. [More...](#ga0de396c2c2c781ff85b94ebf577f15ce) |
| static [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | [ieee802154\_header\_ie\_get\_time\_correction\_us](#gaaae70f7d15135b2e77369cef3c61ba62) (struct [ieee802154\_header\_ie\_time\_correction](structieee802154__header__ie__time__correction.md) \*ie) |
|  | Retrieve the time correction value in microseconds from a Time Correction IE, see section 7.4.2.7. |
| static void | [ieee802154\_header\_ie\_set\_element\_id](#gaef81648e58dc4fbdfd942a1d856952fa) (struct ieee802154\_header\_ie \*ie, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) element\_id) |
|  | Set the element ID of a header IE. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ieee802154\_header\_ie\_get\_element\_id](#gaec7f06d8bf0b44c3350d1d07a65c6cb4) (struct ieee802154\_header\_ie \*ie) |
|  | Get the element ID of a header IE. |
| #define | [IEEE802154\_HEADER\_IE\_HEADER\_LENGTH](#ga4f66344126179e2c98a17f19f6db516b)   [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)) |
|  | The header IE's header length (2 bytes). |
| #define | [IEEE802154\_DEFINE\_HEADER\_IE\_VENDOR\_SPECIFIC](#gafc449a0c9d4ce8f128fd716b2a537f68)(\_vendor\_oui, \_vendor\_specific\_info, \_vendor\_specific\_info\_len) |
|  | Define a vendor specific header IE, see section 7.4.2.3. |
| #define | [IEEE802154\_DEFINE\_HEADER\_IE\_CSL\_REDUCED](#ga382debc13f36ee16e0c015a2c2555c8f)(\_csl\_phase, \_csl\_period) |
|  | Define a reduced CSL IE, see section 7.4.2.3. |
| #define | [IEEE802154\_DEFINE\_HEADER\_IE\_CSL\_FULL](#ga3392a33334814ae63e212491ea90ae74)(\_csl\_phase, \_csl\_period, \_csl\_rendezvous\_time) |
|  | Define a full CSL IE, see section 7.4.2.3. |
| #define | [IEEE802154\_DEFINE\_HEADER\_IE\_TIME\_CORRECTION](#gac2549865f529b5aff1653c80ceda9650)(\_ack, \_time\_correction\_us) |
|  | Define a Time Correction IE, see section 7.4.2.7. |
| #define | [IEEE802154\_TIME\_CORRECTION\_HEADER\_IE\_LEN](#gaaaf32be17c41497c8d3be48292ad1374)   ([IEEE802154\_HEADER\_IE\_HEADER\_LENGTH](#ga4f66344126179e2c98a17f19f6db516b) + [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(struct [ieee802154\_header\_ie\_time\_correction](structieee802154__header__ie__time__correction.md))) |
|  | The length in bytes of a "Time Correction" header IE. |
| #define | [IEEE802154\_HEADER\_TERMINATION\_1\_HEADER\_IE\_LEN](#gae16b5d403da141b0f9d9279817703677)   [IEEE802154\_HEADER\_IE\_HEADER\_LENGTH](#ga4f66344126179e2c98a17f19f6db516b) |
|  | The length in bytes of a "Header Termination 1" header IE. |

| IEEE 802.15.4-2020, Section 10: General PHY requirements | |
| --- | --- |
| enum | [ieee802154\_phy\_channel\_page](#gacabc7386bea701373dfb36ab65bd36a9) {     [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_ZERO\_OQPSK\_2450\_BPSK\_868\_915](#ggacabc7386bea701373dfb36ab65bd36a9a72b17a977aeb6792f7d2016117f4b2f9) = BIT(0) , [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_ONE\_DEPRECATED](#ggacabc7386bea701373dfb36ab65bd36a9a371a12ec5d762b03058fb2532fa04e45) = BIT(1) , [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_TWO\_OQPSK\_868\_915](#ggacabc7386bea701373dfb36ab65bd36a9a5776e0160927b83f4e4e8d6479aaf804) = BIT(2) , [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_THREE\_CSS](#ggacabc7386bea701373dfb36ab65bd36a9a6f71c162be118b0c2edce139753c867e) = BIT(3) ,     [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_FOUR\_HRP\_UWB](#ggacabc7386bea701373dfb36ab65bd36a9a68b93381ddc1184ff0ed13456cf4b6a8) = BIT(4) , [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_FIVE\_OQPSK\_780](#ggacabc7386bea701373dfb36ab65bd36a9a6ea456573a6ff8aed348a9dc547b2db7) = BIT(5) , [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_SIX\_RESERVED](#ggacabc7386bea701373dfb36ab65bd36a9ac13dda08becd3d4799d45ef02f774cc1) = BIT(6) , [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_SEVEN\_MSK](#ggacabc7386bea701373dfb36ab65bd36a9a1f33467ec7659ef411b08f7a23663311) = BIT(7) ,     [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_EIGHT\_LRP\_UWB](#ggacabc7386bea701373dfb36ab65bd36a9aa0ab080c8cdac42dbf80622d075854dc) = BIT(8) , [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_NINE\_SUN\_PREDEFINED](#ggacabc7386bea701373dfb36ab65bd36a9a996b529c9c277d6d653d0e0ffb8b2902) = BIT(9) , [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_TEN\_SUN\_FSK\_GENERIC](#ggacabc7386bea701373dfb36ab65bd36a9a02a17ea787e99528b2a6a8f5107f2544) = BIT(10) , [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_ELEVEN\_OQPSK\_2380](#ggacabc7386bea701373dfb36ab65bd36a9aad0644244fb5b6cba5a295e246722e94) = BIT(11) ,     [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_TWELVE\_LECIM](#ggacabc7386bea701373dfb36ab65bd36a9a6d4023088a3607c072acebd3940340c7) = BIT(12) , [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_THIRTEEN\_RCC](#ggacabc7386bea701373dfb36ab65bd36a9a56dd4ae42595ef0edb109c729e333b08) = BIT(13)   } |
|  | PHY channel pages, see section 10.1.3. [More...](#gacabc7386bea701373dfb36ab65bd36a9) |
| #define | [IEEE802154\_DEFINE\_PHY\_SUPPORTED\_CHANNELS](#ga78d4df389a7bd11c55e5c7b683897a9b)(drv\_attr, from, to) |
|  | Allocate memory for the supported channels driver attribute with a single channel range constant across all driver instances. |

| IEEE 802.15.4-2020, Section 15: HRP UWB PHY | |
| --- | --- |
| For HRP UWB the symbol period is derived from the preamble symbol period (T\_psym), see section 11.3, table 11-1 and section 15.2.5, table 15-4 (confirmed in IEEE 802.15.4z, section 15.1). Choosing among those periods cannot be done based on channel page and channel alone. The mean pulse repetition frequency must also be known, see the 'UwbPrf' parameter of the MCPS-DATA.request primitive (section 8.3.2, table 8-88) and the preamble parameters for HRP-ERDEV length 91 codes (IEEE 802.15.4z, section 15.2.6.2, table 15-7b). | |
| enum | [ieee802154\_phy\_hrp\_uwb\_nominal\_prf](#ga13610aeef06372bc47d84464537fdded) {     [IEEE802154\_PHY\_HRP\_UWB\_PRF\_OFF](#gga13610aeef06372bc47d84464537fddeda4369c745ed378d8273a1014322f3029a) = 0 , [IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_4\_M](#gga13610aeef06372bc47d84464537fddeda9dc3c58366502aeab04a208937536369) = BIT(0) , [IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_16\_M](#gga13610aeef06372bc47d84464537fddedadf9230e6ef62ce66129bfe24f537c88a) = BIT(1) , [IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_64\_M](#gga13610aeef06372bc47d84464537fddeda2b24236d3531cab7d21673d065b7c29e) = BIT(2) ,     [IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_64\_M\_BPRF](#gga13610aeef06372bc47d84464537fddedad920ae285cdcc2a4d59f7c23e29dce27) = BIT(3) , [IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_128\_M\_HPRF](#gga13610aeef06372bc47d84464537fddedae6c88efd301a449b1a31e8aedf4e30ca) = BIT(4) , [IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_256\_M\_HPRF](#gga13610aeef06372bc47d84464537fddedacb66442cf2a5e4c539b6b7edf8419be1) = BIT(5)   } |
|  | represents the nominal pulse rate frequency of an HRP UWB PHY [More...](#ga13610aeef06372bc47d84464537fdded) |
| #define | [IEEE802154\_PHY\_HRP\_UWB\_PRF4\_TPSYM\_SYMBOL\_PERIOD\_NS](#gabeb8a359ce54618aa7df3ee8f6a434bb)   3974.36F |
|  | Nominal PRF 4MHz symbol period. |
| #define | [IEEE802154\_PHY\_HRP\_UWB\_PRF16\_TPSYM\_SYMBOL\_PERIOD\_NS](#ga0123679fba7ca668aa158813f1bf2302)   993.59F |
|  | Nominal PRF 16MHz symbol period. |
| #define | [IEEE802154\_PHY\_HRP\_UWB\_PRF64\_TPSYM\_SYMBOL\_PERIOD\_NS](#ga59f8ba8a01171c56da6f7ae7f8983bf7)   1017.63F |
|  | Nominal PRF 64MHz symbol period. |
| #define | [IEEE802154\_PHY\_HRP\_UWB\_ERDEV\_TPSYM\_SYMBOL\_PERIOD\_NS](#gaa25ba5b644e58cfc7de5ba5aa526ea71)   729.17F |
|  | ERDEV symbol period. |
| #define | [IEEE802154\_PHY\_HRP\_UWB\_RDEV](#gacfd2faf2c3072f8851abd74fe5148ec5) |
|  | RDEV device mask. |
| #define | [IEEE802154\_PHY\_HRP\_UWB\_ERDEV](#gae02b981a3908b05b4bc0b7a2844c27c7) |
|  | ERDEV device mask. |

| IEEE 802.15.4 Driver API | |
| --- | --- |
| enum | [ieee802154\_hw\_caps](#gaf99cda89c29df3c0088fc57ec09cbcd4) {     [IEEE802154\_HW\_ENERGY\_SCAN](#ggaf99cda89c29df3c0088fc57ec09cbcd4a179ad073a5bd34e4e4af587d07ca3f73) = BIT(0) , [IEEE802154\_HW\_FCS](#ggaf99cda89c29df3c0088fc57ec09cbcd4a0ea21cab335dd9082feb2d08be0eb5fa) = BIT(1) , [IEEE802154\_HW\_FILTER](#ggaf99cda89c29df3c0088fc57ec09cbcd4afd09f329a708d00f1384a50c59ddde27) = BIT(2) , [IEEE802154\_HW\_PROMISC](#ggaf99cda89c29df3c0088fc57ec09cbcd4a4adb33f2ca81a24244dead6b379cd916) = BIT(3) ,     [IEEE802154\_HW\_CSMA](#ggaf99cda89c29df3c0088fc57ec09cbcd4a2ee53f11e1ed6853e1f5d9dfe7d7bdf7) = BIT(4) , [IEEE802154\_HW\_TX\_RX\_ACK](#ggaf99cda89c29df3c0088fc57ec09cbcd4ab383a932c0ac9deece68f02210089119) = BIT(5) , [IEEE802154\_HW\_RETRANSMISSION](#ggaf99cda89c29df3c0088fc57ec09cbcd4a752472a994bdcbdf9cdf86deb0231849) = BIT(6) , [IEEE802154\_HW\_RX\_TX\_ACK](#ggaf99cda89c29df3c0088fc57ec09cbcd4aec16c4d418117de2d106e84297568b03) = BIT(7) ,     [IEEE802154\_HW\_TXTIME](#ggaf99cda89c29df3c0088fc57ec09cbcd4a435d032f42d509bd78a992de6e4d7b1d) = BIT(8) , [IEEE802154\_HW\_SLEEP\_TO\_TX](#ggaf99cda89c29df3c0088fc57ec09cbcd4a36f46639c08e70bc30fc98ca1043b071) = BIT(9) , [IEEE802154\_HW\_RXTIME](#ggaf99cda89c29df3c0088fc57ec09cbcd4a68ae68c83a87f0efc25f74edd80c4600) = BIT(10) , [IEEE802154\_HW\_TX\_SEC](#ggaf99cda89c29df3c0088fc57ec09cbcd4a7924c3d5bfe6dceeb2e8caa6df7edecb) = BIT(11) ,     [IEEE802154\_RX\_ON\_WHEN\_IDLE](#ggaf99cda89c29df3c0088fc57ec09cbcd4ac1e00966043e5884c4cbd65fb26f0c0b) = BIT(12) , [IEEE802154\_HW\_SELECTIVE\_TXCHANNEL](#ggaf99cda89c29df3c0088fc57ec09cbcd4ab6cf4f3552d6193027a538a13b95952e) = BIT(13)   } |
|  | IEEE 802.15.4 driver capabilities. [More...](#gaf99cda89c29df3c0088fc57ec09cbcd4) |
| enum | [ieee802154\_filter\_type](#gaa1971591e72866d0f3f0d4db2931e25a) {     [IEEE802154\_FILTER\_TYPE\_IEEE\_ADDR](#ggaa1971591e72866d0f3f0d4db2931e25aa928a93b536c6408b3d77aa329c274fe8) , [IEEE802154\_FILTER\_TYPE\_SHORT\_ADDR](#ggaa1971591e72866d0f3f0d4db2931e25aa2fa1ac98a3b870fcf6e85e7ec82cfbe9) , [IEEE802154\_FILTER\_TYPE\_PAN\_ID](#ggaa1971591e72866d0f3f0d4db2931e25aab44cc830999926a5d232aedabef52653) , [IEEE802154\_FILTER\_TYPE\_SRC\_IEEE\_ADDR](#ggaa1971591e72866d0f3f0d4db2931e25aade18e03611339f5f7ec4fdcdee409c21) ,     [IEEE802154\_FILTER\_TYPE\_SRC\_SHORT\_ADDR](#ggaa1971591e72866d0f3f0d4db2931e25aac6dbb68674e7594fd4cd69bbe4ea60de)   } |
|  | Filter type, see [ieee802154\_radio\_api::filter](structieee802154__radio__api.md#aa9502e0e014a8d05ffe235567e8c98f3 "ieee802154_radio_api::filter"). [More...](#gaa1971591e72866d0f3f0d4db2931e25a) |
| enum | [ieee802154\_event](#ga3491982b677941442d904ce69fce7c5e) { [IEEE802154\_EVENT\_TX\_STARTED](#gga3491982b677941442d904ce69fce7c5eaacd61f4466f1ef926adc9e1afe6c1648) , [IEEE802154\_EVENT\_RX\_FAILED](#gga3491982b677941442d904ce69fce7c5eaef51197ca09befaee8cdfa2cde107273) , [IEEE802154\_EVENT\_RX\_OFF](#gga3491982b677941442d904ce69fce7c5eaf7ed46b9d13a232a2ea6b650514eea3d) } |
|  | Driver events, see [IEEE802154\_CONFIG\_EVENT\_HANDLER](#gga34aecc5996174a812b295a3a4693ad09a8d88a76f71cf8869b3e35e423b18c6f3). [More...](#ga3491982b677941442d904ce69fce7c5e) |
| enum | [ieee802154\_rx\_fail\_reason](#ga04febbd15f9e6f6540d711ada5a4a1c8) { [IEEE802154\_RX\_FAIL\_NOT\_RECEIVED](#gga04febbd15f9e6f6540d711ada5a4a1c8ad584824b4813626d04a85499371b9c32) , [IEEE802154\_RX\_FAIL\_INVALID\_FCS](#gga04febbd15f9e6f6540d711ada5a4a1c8a103f6683ff71f4f7248ee1a0d09d6be4) , [IEEE802154\_RX\_FAIL\_ADDR\_FILTERED](#gga04febbd15f9e6f6540d711ada5a4a1c8a7ff9cfcc5e4dfc2bf7abe1860a39410f) , [IEEE802154\_RX\_FAIL\_OTHER](#gga04febbd15f9e6f6540d711ada5a4a1c8a5baa9dd683a717f7fbdfc5ab85935a3b) } |
|  | RX failed event reasons, see [IEEE802154\_EVENT\_RX\_FAILED](#gga3491982b677941442d904ce69fce7c5eaef51197ca09befaee8cdfa2cde107273). [More...](#ga04febbd15f9e6f6540d711ada5a4a1c8) |
| enum | [ieee802154\_tx\_mode](#gab2bee8752291e082cb277145cef1225d) {     [IEEE802154\_TX\_MODE\_DIRECT](#ggab2bee8752291e082cb277145cef1225da6904c3c7f53d46c5c8b41dd1a82b2650) , [IEEE802154\_TX\_MODE\_CCA](#ggab2bee8752291e082cb277145cef1225da1e23f1ad3f9d0832fd4d67fc00fd8eb5) , [IEEE802154\_TX\_MODE\_CSMA\_CA](#ggab2bee8752291e082cb277145cef1225da51a0e7cb482447779634062655a1ec47) , [IEEE802154\_TX\_MODE\_TXTIME](#ggab2bee8752291e082cb277145cef1225da9a7b8ba25603b72aecbf7f66abf26508) ,     [IEEE802154\_TX\_MODE\_TXTIME\_CCA](#ggab2bee8752291e082cb277145cef1225da42b4589afb2180fde053fdbbf58c0d3e) , [IEEE802154\_TX\_MODE\_COMMON\_COUNT](#ggab2bee8752291e082cb277145cef1225daa389aeccad62a0516678564e68fcd595) , [IEEE802154\_TX\_MODE\_PRIV\_START](#ggab2bee8752291e082cb277145cef1225dabbab0c864f313ee4045e5ad59ea774e2) = IEEE802154\_TX\_MODE\_COMMON\_COUNT   } |
|  | IEEE 802.15.4 Transmission mode. [More...](#gab2bee8752291e082cb277145cef1225d) |
| enum | [ieee802154\_fpb\_mode](#gab593bc6640ddea23c951982ca2f4c0bf) { [IEEE802154\_FPB\_ADDR\_MATCH\_THREAD](#ggab593bc6640ddea23c951982ca2f4c0bfa012874ab4d234bbeb2954756cf2dc9d6) , [IEEE802154\_FPB\_ADDR\_MATCH\_ZIGBEE](#ggab593bc6640ddea23c951982ca2f4c0bfac7c839b7c0649d6151f90ff1d51ae417) } |
|  | IEEE 802.15.4 Frame Pending Bit table address matching mode. [More...](#gab593bc6640ddea23c951982ca2f4c0bf) |
| enum | [ieee802154\_config\_type](#ga34aecc5996174a812b295a3a4693ad09) {     [IEEE802154\_CONFIG\_AUTO\_ACK\_FPB](#gga34aecc5996174a812b295a3a4693ad09a38c67aac70d24b31996871fe4686d9ee) , [IEEE802154\_CONFIG\_ACK\_FPB](#gga34aecc5996174a812b295a3a4693ad09ab897aea56ea5e9ddf306c5c0d75c2cd7) , [IEEE802154\_CONFIG\_PAN\_COORDINATOR](#gga34aecc5996174a812b295a3a4693ad09ab2b6ae3034fb469168ed29704ec045f0) , [IEEE802154\_CONFIG\_PROMISCUOUS](#gga34aecc5996174a812b295a3a4693ad09a399313ff2d8ebb3a2d72152a9615d8c5) ,     [IEEE802154\_CONFIG\_EVENT\_HANDLER](#gga34aecc5996174a812b295a3a4693ad09a8d88a76f71cf8869b3e35e423b18c6f3) , [IEEE802154\_CONFIG\_MAC\_KEYS](#gga34aecc5996174a812b295a3a4693ad09a8bd29c6d6aa67adaf23415eb337904c0) , [IEEE802154\_CONFIG\_FRAME\_COUNTER](#gga34aecc5996174a812b295a3a4693ad09aad7d04b7e1c02b2d88fcbb8ab1ac313b) , [IEEE802154\_CONFIG\_FRAME\_COUNTER\_IF\_LARGER](#gga34aecc5996174a812b295a3a4693ad09aa34da77f0966ff5a0e8ac73ed68554a8) ,     [IEEE802154\_CONFIG\_RX\_SLOT](#gga34aecc5996174a812b295a3a4693ad09af4e3dd7588ee06458f2d42f02797b3d6) , [IEEE802154\_CONFIG\_CSL\_PERIOD](#gga34aecc5996174a812b295a3a4693ad09a9fdbe95e0b7141d9150eaa4a5793c2e7) , [IEEE802154\_CONFIG\_EXPECTED\_RX\_TIME](#gga34aecc5996174a812b295a3a4693ad09a1a71ef76d90b6882196e4c6473de6bd8) , [IEEE802154\_CONFIG\_ENH\_ACK\_HEADER\_IE](#gga34aecc5996174a812b295a3a4693ad09a840e5f1db9a354e7bcd892ddb4117907) ,     [IEEE802154\_CONFIG\_RX\_ON\_WHEN\_IDLE](#gga34aecc5996174a812b295a3a4693ad09a9228dbe2583e5be10f64b116e87645e1) , [IEEE802154\_CONFIG\_COMMON\_COUNT](#gga34aecc5996174a812b295a3a4693ad09a61df14aeb348cfc694d539b506dc23ac) , [IEEE802154\_CONFIG\_PRIV\_START](#gga34aecc5996174a812b295a3a4693ad09a1653b2869208045415d83fc6708d015c) = IEEE802154\_CONFIG\_COMMON\_COUNT   } |
|  | IEEE 802.15.4 driver configuration types. [More...](#ga34aecc5996174a812b295a3a4693ad09) |
| enum | [ieee802154\_attr](#gaf4deddd3f23ebfd65fa47c5d62634430) {     [IEEE802154\_ATTR\_PHY\_SUPPORTED\_CHANNEL\_PAGES](#ggaf4deddd3f23ebfd65fa47c5d62634430a4ad28f920776c45af9d430db786a926a) , [IEEE802154\_ATTR\_PHY\_SUPPORTED\_CHANNEL\_RANGES](#ggaf4deddd3f23ebfd65fa47c5d62634430aba76daa0a70bcdd573ecbfd63ca19e7d) , [IEEE802154\_ATTR\_PHY\_HRP\_UWB\_SUPPORTED\_PRFS](#ggaf4deddd3f23ebfd65fa47c5d62634430ad90b4a118866c4942ef6f6a8ae56eb3f) , [IEEE802154\_ATTR\_COMMON\_COUNT](#ggaf4deddd3f23ebfd65fa47c5d62634430aa0830214987de7a89297777c0d1004de) ,     [IEEE802154\_ATTR\_PRIV\_START](#ggaf4deddd3f23ebfd65fa47c5d62634430ad4912dc68abc1abe54bc212f023bf511) = IEEE802154\_ATTR\_COMMON\_COUNT   } |
|  | IEEE 802.15.4 driver attributes. [More...](#gaf4deddd3f23ebfd65fa47c5d62634430) |
| typedef void(\* | [energy\_scan\_done\_cb\_t](#ga8c9ab3cecefe641a25f003eb6d014fc5)) (const struct [device](structdevice.md) \*dev, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) max\_ed) |
|  | Energy scan callback. |
| typedef void(\* | [ieee802154\_event\_cb\_t](#ga8219b80b8b179fc3a2ffac0dfdfb4e4b)) (const struct [device](structdevice.md) \*dev, enum [ieee802154\_event](#ga3491982b677941442d904ce69fce7c5e) evt, void \*event\_params) |
|  | Driver event callback. |
| static int | [ieee802154\_attr\_get\_channel\_page\_and\_range](#gaf69d2b65aa46ec4483c6bab419413ba5) (enum [ieee802154\_attr](#gaf4deddd3f23ebfd65fa47c5d62634430) attr, const enum [ieee802154\_phy\_channel\_page](#gacabc7386bea701373dfb36ab65bd36a9) phy\_supported\_channel\_page, const struct [ieee802154\_phy\_supported\_channels](structieee802154__phy__supported__channels.md) \*phy\_supported\_channels, struct [ieee802154\_attr\_value](structieee802154__attr__value.md) \*value) |
|  | Helper function to handle channel page and range to be called from drivers' attr\_get() implementation. |
| #define | [IEEE802154\_HW\_CAPS\_BITS\_COMMON\_COUNT](#gaf143a9f110a2eb6b21104af6927159bc)   (14) |
|  | Number of bits used by [ieee802154\_hw\_caps](#gaf99cda89c29df3c0088fc57ec09cbcd4) type. |
| #define | [IEEE802154\_HW\_CAPS\_BITS\_PRIV\_START](#ga40912ccb268768b4e96ce9cad35476af)   [IEEE802154\_HW\_CAPS\_BITS\_COMMON\_COUNT](#gaf143a9f110a2eb6b21104af6927159bc) |
|  | This and higher values are specific to the protocol- or driver-specific extensions. |
| #define | [IEEE802154\_CONFIG\_RX\_SLOT\_NONE](#ga1cb6434a3a7555fe9d35c73b698cbf10)   -1LL |
|  | Configuring an RX slot with the start parameter set to this value will cancel and delete any previously configured RX slot. |
| #define | [IEEE802154\_CONFIG\_RX\_SLOT\_OFF](#ga3828a2d56a39de92c2fd79caaac4c800)   0LL |
|  | Configuring an RX slot with this start parameter while the driver is "down", will keep RX off when the driver is being started. |

| IEEE 802.15.4 driver utils | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [ieee802154\_is\_ar\_flag\_set](#gaf5d7bdde2a9774f9d90604a6e203bb07) (struct [net\_buf](structnet__buf.md) \*frag) |
|  | Check if the AR flag is set on the frame inside the given [Network Packet Library](group__net__pkt.md "Network Packet Library"). |

| IEEE 802.15.4 driver callbacks | |
| --- | --- |
| enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) | [ieee802154\_handle\_ack](#ga68e1f89571ccbefef61a5496577337fc) (struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | IEEE 802.15.4 driver ACK handling callback into L2 that drivers must call when receiving an ACK package. |
| void | [ieee802154\_init](#gad2a4cb5df84ffe20b83fc54dc9bcfc91) (struct [net\_if](structnet__if.md) \*iface) |
|  | IEEE 802.15.4 driver initialization callback into L2 called by drivers to initialize the active L2 stack for a given interface. |

| IEEE 802.15.4-2020, Section 6: MAC functional description | |
| --- | --- |
| #define | [IEEE802154\_PHY\_SYMBOLS\_PER\_SECOND](#gaf228d9c26cedd5c790b7ebae41b5f937)(symbol\_period\_ns) |
|  | The symbol period (and therefore symbol rate) is defined in section 6.1: "Some of the timing parameters in definition of the MAC are in units of PHY symbols. |

| IEEE 802.15.4-2020, Section 8: MAC services | |
| --- | --- |
| #define | [IEEE802154\_MAC\_A\_BASE\_SLOT\_DURATION](#gadb590005c9120e6b04aa430ebb306b8f)   60U |
|  | The number of PHY symbols forming a superframe slot when the superframe order is equal to zero, see sections 8.4.2, table 8-93, aBaseSlotDuration and section 6.2.1. |
| #define | [IEEE802154\_MAC\_A\_NUM\_SUPERFRAME\_SLOTS](#ga662c1add47deb9807e848aeeee5e6842)   16U |
|  | The number of slots contained in any superframe, see section 8.4.2, table 8-93, aNumSuperframeSlots. |
| #define | [IEEE802154\_MAC\_A\_BASE\_SUPERFRAME\_DURATION](#ga52358c63c386b72f190d3b487c9ba286)   ([IEEE802154\_MAC\_A\_BASE\_SLOT\_DURATION](#gadb590005c9120e6b04aa430ebb306b8f) \* [IEEE802154\_MAC\_A\_NUM\_SUPERFRAME\_SLOTS](#ga662c1add47deb9807e848aeeee5e6842)) |
|  | The number of PHY symbols forming a superframe when the superframe order is equal to zero, see section 8.4.2, table 8-93, aBaseSuperframeDuration. |
| #define | [IEEE802154\_MAC\_A\_UNIT\_BACKOFF\_PERIOD](#ga86f3186304b02de3096d521238d407db)(turnaround\_time) |
|  | MAC PIB attribute aUnitBackoffPeriod, see section 8.4.2, table 8-93, in symbol periods, valid for all PHYs except SUN PHY in the 920 MHz band. |
| #define | [IEEE802154\_MAC\_RESPONSE\_WAIT\_TIME\_DEFAULT](#ga132be1037c5db1311c6d0c7d74e1fe40)   32U |
|  | Default macResponseWaitTime in multiples of aBaseSuperframeDuration as defined in section 8.4.3.1, table 8-94. |

| IEEE 802.15.4-2020, Section 11: PHY services | |
| --- | --- |
| #define | [IEEE802154\_PHY\_A\_TURNAROUND\_TIME\_DEFAULT](#ga9e95bf5d8ddb1087cdd9eb2aa80d100e)   12U |
|  | Default PHY PIB attribute aTurnaroundTime, in PHY symbols, see section 11.3, table 11-1. |
| #define | [IEEE802154\_PHY\_A\_TURNAROUND\_TIME\_1MS](#ga68115b80097b116b704431808469450b)(symbol\_period\_ns) |
|  | PHY PIB attribute aTurnaroundTime for SUN, RS-GFSK, TVWS, and LECIM FSK PHY, in PHY symbols, see section 11.3, table 11-1. |
| #define | [IEEE802154\_PHY\_A\_CCA\_TIME](#gaf58b5d421167c2075dcdfdbaba5956dd)   8U |
|  | PHY PIB attribute aCcaTime, in PHY symbols, all PHYs except for SUN O-QPSK, see section 11.3, table 11-1. |

| IEEE 802.15.4-2020, Section 12: O-QPSK PHY | |
| --- | --- |
| #define | [IEEE802154\_PHY\_OQPSK\_868MHZ\_SYMBOL\_PERIOD\_NS](#ga32ce931f3d35d779e4251c37f61583f5)   40000LL |
|  | O-QPSK 868Mhz band symbol period, see section 12.3.3. |
| #define | [IEEE802154\_PHY\_OQPSK\_780\_TO\_2450MHZ\_SYMBOL\_PERIOD\_NS](#gaff3d58945d53e824f1fb1ca11dd9997b)   16000LL |
|  | O-QPSK 780MHz, 915MHz, 2380MHz and 2450MHz bands symbol period, see section 12.3.3. |

| IEEE 802.15.4-2020, Section 13: BPSK PHY | |
| --- | --- |
| #define | [IEEE802154\_PHY\_BPSK\_868MHZ\_SYMBOL\_PERIOD\_NS](#ga1dc4319d0a8d979c7455e1f71f45d885)   50000LL |
|  | BPSK 868MHz band symbol period, see section 13.3.3. |
| #define | [IEEE802154\_PHY\_BPSK\_915MHZ\_SYMBOL\_PERIOD\_NS](#gaa12344b6a118995b63c5bd4bc3180efd)   25000LL |
|  | BPSK 915MHz band symbol period, see section 13.3.3. |

| IEEE 802.15.4-2020, Section 19: SUN FSK PHY | |
| --- | --- |
| #define | [IEEE802154\_PHY\_SUN\_FSK\_863MHZ\_915MHZ\_SYMBOL\_PERIOD\_NS](#ga155b5b5a06311c1bde3f36e06d02ed7d)   20000LL |
|  | SUN FSK 863Mhz and 915MHz band symbol periods, see section 19.1, table 19-1. |
| #define | [IEEE802154\_PHY\_SUN\_FSK\_PHR\_LEN](#gac088ee6d01014a12169e74111ea61993)   2 |
|  | SUN FSK PHY header length, in bytes, see section 19.2.4. |

## Detailed Description

IEEE 802.15.4 driver API.

Since
:   1.0

Version
:   0.8.0

This API provides a common representation of vendor-specific hardware and firmware to the native IEEE 802.15.4 L2 and OpenThread stacks. **Application developers should never interface directly with this API.** It is of interest to driver maintainers only.

The IEEE 802.15.4 driver API consists of two separate parts:

- a basic, mostly PHY-level driver API to be implemented by all drivers,
- several optional MAC-level extension points to offload performance critical or timing sensitive aspects at MAC level to the driver hardware or firmware ("hard" MAC).

Implementing the basic driver API will ensure integration with the native L2 stack as well as basic support for OpenThread. Depending on the hardware, offloading to vendor-specific hardware or firmware features may be required to achieve full compliance with the Thread protocol or IEEE 802.15.4 subprotocols (e.g. fast enough ACK packages, precise timing of timed TX/RX in the TSCH or CSL subprotocols).

Whether or not MAC-level offloading extension points need to be implemented is to be decided by individual driver maintainers. Upper layers SHOULD provide a "soft" MAC fallback whenever possible.

Note
:   All section, table and figure references are to the IEEE 802.15.4-2020 standard.

## Macro Definition Documentation

## [◆ ](#ga1cb6434a3a7555fe9d35c73b698cbf10)IEEE802154\_CONFIG\_RX\_SLOT\_NONE

| #define IEEE802154\_CONFIG\_RX\_SLOT\_NONE   -1LL |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

Configuring an RX slot with the start parameter set to this value will cancel and delete any previously configured RX slot.

## [◆ ](#ga3828a2d56a39de92c2fd79caaac4c800)IEEE802154\_CONFIG\_RX\_SLOT\_OFF

| #define IEEE802154\_CONFIG\_RX\_SLOT\_OFF   0LL |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

Configuring an RX slot with this start parameter while the driver is "down", will keep RX off when the driver is being started.

Configuring an RX slot with this start value while the driver is "up" will immediately switch RX off until either the slot is deleted, see [IEEE802154\_CONFIG\_RX\_SLOT\_NONE](#ga1cb6434a3a7555fe9d35c73b698cbf10) or a slot with a future start parameter is configured and that start time arrives.

## [◆ ](#ga3392a33334814ae63e212491ea90ae74)IEEE802154\_DEFINE\_HEADER\_IE\_CSL\_FULL

| #define IEEE802154\_DEFINE\_HEADER\_IE\_CSL\_FULL | ( |  | *\_csl\_phase*, |
| --- | --- | --- | --- |
|  |  |  | *\_csl\_period*, |
|  |  |  | *\_csl\_rendezvous\_time* ) |

`#include <[ieee802154_ie.h](ieee802154__ie_8h.md)>`

**Value:**

IEEE802154\_DEFINE\_HEADER\_IE([IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_CSL\_IE](#gga0de396c2c2c781ff85b94ebf577f15cea69e4548081815bd45ea68c52d1b66efb), \

sizeof(struct [ieee802154\_header\_ie\_csl\_full](structieee802154__header__ie__csl__full.md)), \

IEEE802154\_DEFINE\_HEADER\_IE\_CSL\_FULL\_CONTENT( \

\_csl\_phase, \_csl\_period, \_csl\_rendezvous\_time), \

csl.full)

[IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_CSL\_IE](#gga0de396c2c2c781ff85b94ebf577f15cea69e4548081815bd45ea68c52d1b66efb)

@ IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_CSL\_IE

CSL IE.

**Definition** ieee802154\_ie.h:55

[ieee802154\_header\_ie\_csl\_full](structieee802154__header__ie__csl__full.md)

Full CSL IE, see section 7.4.2.3.

**Definition** ieee802154\_ie.h:77

Define a full CSL IE, see section 7.4.2.3.

Example usage (all parameters in CPU byte order):

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) csl\_phase = ...;

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) csl\_period = ...;

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) csl\_rendezvous\_time = ...;

struct ieee802154\_header\_ie header\_ie =

[IEEE802154\_DEFINE\_HEADER\_IE\_CSL\_REDUCED](#ga382debc13f36ee16e0c015a2c2555c8f)(csl\_phase, csl\_period, csl\_rendezvous\_time);

[IEEE802154\_DEFINE\_HEADER\_IE\_CSL\_REDUCED](#ga382debc13f36ee16e0c015a2c2555c8f)

#define IEEE802154\_DEFINE\_HEADER\_IE\_CSL\_REDUCED(\_csl\_phase, \_csl\_period)

Define a reduced CSL IE, see section 7.4.2.3.

**Definition** ieee802154\_ie.h:254

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

Parameters
:   | \_csl\_phase | CSL phase in CPU byte order |
    | --- | --- |
    | \_csl\_period | CSL period in CPU byte order |
    | \_csl\_rendezvous\_time | CSL rendezvous time in CPU byte order |

## [◆ ](#ga382debc13f36ee16e0c015a2c2555c8f)IEEE802154\_DEFINE\_HEADER\_IE\_CSL\_REDUCED

| #define IEEE802154\_DEFINE\_HEADER\_IE\_CSL\_REDUCED | ( |  | *\_csl\_phase*, |
| --- | --- | --- | --- |
|  |  |  | *\_csl\_period* ) |

`#include <[ieee802154_ie.h](ieee802154__ie_8h.md)>`

**Value:**

IEEE802154\_DEFINE\_HEADER\_IE( \

[IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_CSL\_IE](#gga0de396c2c2c781ff85b94ebf577f15cea69e4548081815bd45ea68c52d1b66efb), \

sizeof(struct [ieee802154\_header\_ie\_csl\_reduced](structieee802154__header__ie__csl__reduced.md)), \

IEEE802154\_DEFINE\_HEADER\_IE\_CSL\_REDUCED\_CONTENT(\_csl\_phase, \_csl\_period), \

csl.reduced)

[ieee802154\_header\_ie\_csl\_reduced](structieee802154__header__ie__csl__reduced.md)

Reduced CSL IE, see section 7.4.2.3.

**Definition** ieee802154\_ie.h:84

Define a reduced CSL IE, see section 7.4.2.3.

Example usage (all parameters in CPU byte order):

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) csl\_phase = ...;

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) csl\_period = ...;

struct ieee802154\_header\_ie header\_ie =

[IEEE802154\_DEFINE\_HEADER\_IE\_CSL\_REDUCED](#ga382debc13f36ee16e0c015a2c2555c8f)(csl\_phase, csl\_period);

Parameters
:   | \_csl\_phase | CSL phase in CPU byte order |
    | --- | --- |
    | \_csl\_period | CSL period in CPU byte order |

## [◆ ](#gac2549865f529b5aff1653c80ceda9650)IEEE802154\_DEFINE\_HEADER\_IE\_TIME\_CORRECTION

| #define IEEE802154\_DEFINE\_HEADER\_IE\_TIME\_CORRECTION | ( |  | *\_ack*, |
| --- | --- | --- | --- |
|  |  |  | *\_time\_correction\_us* ) |

`#include <[ieee802154_ie.h](ieee802154__ie_8h.md)>`

**Value:**

IEEE802154\_DEFINE\_HEADER\_IE( \

[IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_TIME\_CORRECTION\_IE](#gga0de396c2c2c781ff85b94ebf577f15cea3f050528506d59ba26a100e42a182330), \

sizeof(struct [ieee802154\_header\_ie\_time\_correction](structieee802154__header__ie__time__correction.md)), \

IEEE802154\_DEFINE\_HEADER\_IE\_TIME\_CORRECTION\_CONTENT(\_ack, \_time\_correction\_us), \

time\_correction)

[IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_TIME\_CORRECTION\_IE](#gga0de396c2c2c781ff85b94ebf577f15cea3f050528506d59ba26a100e42a182330)

@ IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_TIME\_CORRECTION\_IE

Time correction IE.

**Definition** ieee802154\_ie.h:58

[ieee802154\_header\_ie\_time\_correction](structieee802154__header__ie__time__correction.md)

Time Correction IE, see section 7.4.2.7.

**Definition** ieee802154\_ie.h:134

Define a Time Correction IE, see section 7.4.2.7.

Example usage (parameter in CPU byte order):

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) time\_sync\_info = ...;

struct ieee802154\_header\_ie header\_ie =

[IEEE802154\_DEFINE\_HEADER\_IE\_TIME\_CORRECTION](#gac2549865f529b5aff1653c80ceda9650)(true, time\_sync\_info);

[IEEE802154\_DEFINE\_HEADER\_IE\_TIME\_CORRECTION](#gac2549865f529b5aff1653c80ceda9650)

#define IEEE802154\_DEFINE\_HEADER\_IE\_TIME\_CORRECTION(\_ack, \_time\_correction\_us)

Define a Time Correction IE, see section 7.4.2.7.

**Definition** ieee802154\_ie.h:301

Parameters
:   | \_ack | whether or not the enhanced ACK frame that receives this IE is an ACK (true) or NACK (false) |
    | --- | --- |
    | \_time\_correction\_us | the positive or negative deviation from expected RX time in microseconds |

## [◆ ](#gafc449a0c9d4ce8f128fd716b2a537f68)IEEE802154\_DEFINE\_HEADER\_IE\_VENDOR\_SPECIFIC

| #define IEEE802154\_DEFINE\_HEADER\_IE\_VENDOR\_SPECIFIC | ( |  | *\_vendor\_oui*, |
| --- | --- | --- | --- |
|  |  |  | *\_vendor\_specific\_info*, |
|  |  |  | *\_vendor\_specific\_info\_len* ) |

`#include <[ieee802154_ie.h](ieee802154__ie_8h.md)>`

**Value:**

IEEE802154\_DEFINE\_HEADER\_IE([IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_VENDOR\_SPECIFIC\_IE](#gga0de396c2c2c781ff85b94ebf577f15ceaf02726c8c317ee15e92c1d43b4392c14), \

IEEE802154\_DEFINE\_HEADER\_IE\_VENDOR\_SPECIFIC\_CONTENT\_LEN( \

\_vendor\_specific\_info\_len), \

IEEE802154\_DEFINE\_HEADER\_IE\_VENDOR\_SPECIFIC\_CONTENT( \

\_vendor\_oui, \_vendor\_specific\_info), \

vendor\_specific)

[IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_VENDOR\_SPECIFIC\_IE](#gga0de396c2c2c781ff85b94ebf577f15ceaf02726c8c317ee15e92c1d43b4392c14)

@ IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_VENDOR\_SPECIFIC\_IE

Vendor specific IE.

**Definition** ieee802154\_ie.h:54

Define a vendor specific header IE, see section 7.4.2.3.

Example usage (all parameters in little endian):

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vendor\_specific\_info[] = {...some vendor specific IE content...};

struct ieee802154\_header\_ie header\_ie = [IEEE802154\_DEFINE\_HEADER\_IE\_VENDOR\_SPECIFIC](#gafc449a0c9d4ce8f128fd716b2a537f68)(

{0x9b, 0xb8, 0xea}, vendor\_specific\_info, sizeof(vendor\_specific\_info));

[IEEE802154\_DEFINE\_HEADER\_IE\_VENDOR\_SPECIFIC](#gafc449a0c9d4ce8f128fd716b2a537f68)

#define IEEE802154\_DEFINE\_HEADER\_IE\_VENDOR\_SPECIFIC(\_vendor\_oui, \_vendor\_specific\_info, \_vendor\_specific\_info\_len)

Define a vendor specific header IE, see section 7.4.2.3.

**Definition** ieee802154\_ie.h:230

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

Parameters
:   | \_vendor\_oui | an initializer for a 3 byte vendor oui array in little endian |
    | --- | --- |
    | \_vendor\_specific\_info | pointer to a variable length [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) array with the vendor specific IE content |
    | \_vendor\_specific\_info\_len | the length of the vendor specific IE content (in bytes) |

## [◆ ](#ga78d4df389a7bd11c55e5c7b683897a9b)IEEE802154\_DEFINE\_PHY\_SUPPORTED\_CHANNELS

| #define IEEE802154\_DEFINE\_PHY\_SUPPORTED\_CHANNELS | ( |  | *drv\_attr*, |
| --- | --- | --- | --- |
|  |  |  | *from*, |
|  |  |  | *to* ) |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

**Value:**

static const struct { \

const struct [ieee802154\_phy\_channel\_range](structieee802154__phy__channel__range.md) phy\_channel\_range; \

const struct [ieee802154\_phy\_supported\_channels](structieee802154__phy__supported__channels.md) phy\_supported\_channels; \

} drv\_attr = { \

.phy\_channel\_range = {.from\_channel = (from), .to\_channel = (to)}, \

.phy\_supported\_channels = \

{ \

.ranges = &drv\_attr.phy\_channel\_range, \

.num\_ranges = 1U, \

}, \

}

[ieee802154\_phy\_channel\_range](structieee802154__phy__channel__range.md)

Represents a supported channel range, see ieee802154\_phy\_supported\_channels.

**Definition** ieee802154\_radio.h:235

[ieee802154\_phy\_supported\_channels](structieee802154__phy__supported__channels.md)

Represents a list channels supported by a driver for a given interface, see IEEE802154\_ATTR\_PHY\_SUPPO...

**Definition** ieee802154\_radio.h:244

Allocate memory for the supported channels driver attribute with a single channel range constant across all driver instances.

This is what most IEEE 802.15.4 drivers need.

Example usage:

[IEEE802154\_DEFINE\_PHY\_SUPPORTED\_CHANNELS](#ga78d4df389a7bd11c55e5c7b683897a9b)(drv\_attr, 11, 26);

[IEEE802154\_DEFINE\_PHY\_SUPPORTED\_CHANNELS](#ga78d4df389a7bd11c55e5c7b683897a9b)

#define IEEE802154\_DEFINE\_PHY\_SUPPORTED\_CHANNELS(drv\_attr, from, to)

Allocate memory for the supported channels driver attribute with a single channel range constant acro...

**Definition** ieee802154\_radio.h:282

The attribute may then be referenced like this:

... &drv\_attr.phy\_supported\_channels ...

See [ieee802154\_attr\_get\_channel\_page\_and\_range()](#gaf69d2b65aa46ec4483c6bab419413ba5) for a further shortcut that can be combined with this macro.

Parameters
:   | drv\_attr | name of the local static variable to be declared for the local attributes structure |
    | --- | --- |
    | from | the first channel to be supported |
    | to | the last channel to be supported |

## [◆ ](#ga4f66344126179e2c98a17f19f6db516b)IEEE802154\_HEADER\_IE\_HEADER\_LENGTH

| #define IEEE802154\_HEADER\_IE\_HEADER\_LENGTH   [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)) |
| --- |

`#include <[ieee802154_ie.h](ieee802154__ie_8h.md)>`

The header IE's header length (2 bytes).

## [◆ ](#gae16b5d403da141b0f9d9279817703677)IEEE802154\_HEADER\_TERMINATION\_1\_HEADER\_IE\_LEN

| #define IEEE802154\_HEADER\_TERMINATION\_1\_HEADER\_IE\_LEN   [IEEE802154\_HEADER\_IE\_HEADER\_LENGTH](#ga4f66344126179e2c98a17f19f6db516b) |
| --- |

`#include <[ieee802154_ie.h](ieee802154__ie_8h.md)>`

The length in bytes of a "Header Termination 1" header IE.

## [◆ ](#gaf143a9f110a2eb6b21104af6927159bc)IEEE802154\_HW\_CAPS\_BITS\_COMMON\_COUNT

| #define IEEE802154\_HW\_CAPS\_BITS\_COMMON\_COUNT   (14) |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

Number of bits used by [ieee802154\_hw\_caps](#gaf99cda89c29df3c0088fc57ec09cbcd4) type.

## [◆ ](#ga40912ccb268768b4e96ce9cad35476af)IEEE802154\_HW\_CAPS\_BITS\_PRIV\_START

| #define IEEE802154\_HW\_CAPS\_BITS\_PRIV\_START   [IEEE802154\_HW\_CAPS\_BITS\_COMMON\_COUNT](#gaf143a9f110a2eb6b21104af6927159bc) |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

This and higher values are specific to the protocol- or driver-specific extensions.

## [◆ ](#gadb590005c9120e6b04aa430ebb306b8f)IEEE802154\_MAC\_A\_BASE\_SLOT\_DURATION

| #define IEEE802154\_MAC\_A\_BASE\_SLOT\_DURATION   60U |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

The number of PHY symbols forming a superframe slot when the superframe order is equal to zero, see sections 8.4.2, table 8-93, aBaseSlotDuration and section 6.2.1.

## [◆ ](#ga52358c63c386b72f190d3b487c9ba286)IEEE802154\_MAC\_A\_BASE\_SUPERFRAME\_DURATION

| #define IEEE802154\_MAC\_A\_BASE\_SUPERFRAME\_DURATION   ([IEEE802154\_MAC\_A\_BASE\_SLOT\_DURATION](#gadb590005c9120e6b04aa430ebb306b8f) \* [IEEE802154\_MAC\_A\_NUM\_SUPERFRAME\_SLOTS](#ga662c1add47deb9807e848aeeee5e6842)) |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

The number of PHY symbols forming a superframe when the superframe order is equal to zero, see section 8.4.2, table 8-93, aBaseSuperframeDuration.

## [◆ ](#ga662c1add47deb9807e848aeeee5e6842)IEEE802154\_MAC\_A\_NUM\_SUPERFRAME\_SLOTS

| #define IEEE802154\_MAC\_A\_NUM\_SUPERFRAME\_SLOTS   16U |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

The number of slots contained in any superframe, see section 8.4.2, table 8-93, aNumSuperframeSlots.

## [◆ ](#ga86f3186304b02de3096d521238d407db)IEEE802154\_MAC\_A\_UNIT\_BACKOFF\_PERIOD

| #define IEEE802154\_MAC\_A\_UNIT\_BACKOFF\_PERIOD | ( |  | *turnaround\_time* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

**Value:**

(turnaround\_time + [IEEE802154\_PHY\_A\_CCA\_TIME](#gaf58b5d421167c2075dcdfdbaba5956dd))

[IEEE802154\_PHY\_A\_CCA\_TIME](#gaf58b5d421167c2075dcdfdbaba5956dd)

#define IEEE802154\_PHY\_A\_CCA\_TIME

PHY PIB attribute aCcaTime, in PHY symbols, all PHYs except for SUN O-QPSK, see section 11....

**Definition** ieee802154\_radio.h:320

MAC PIB attribute aUnitBackoffPeriod, see section 8.4.2, table 8-93, in symbol periods, valid for all PHYs except SUN PHY in the 920 MHz band.

## [◆ ](#ga132be1037c5db1311c6d0c7d74e1fe40)IEEE802154\_MAC\_RESPONSE\_WAIT\_TIME\_DEFAULT

| #define IEEE802154\_MAC\_RESPONSE\_WAIT\_TIME\_DEFAULT   32U |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

Default macResponseWaitTime in multiples of aBaseSuperframeDuration as defined in section 8.4.3.1, table 8-94.

## [◆ ](#gaf58b5d421167c2075dcdfdbaba5956dd)IEEE802154\_PHY\_A\_CCA\_TIME

| #define IEEE802154\_PHY\_A\_CCA\_TIME   8U |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

PHY PIB attribute aCcaTime, in PHY symbols, all PHYs except for SUN O-QPSK, see section 11.3, table 11-1.

## [◆ ](#ga68115b80097b116b704431808469450b)IEEE802154\_PHY\_A\_TURNAROUND\_TIME\_1MS

| #define IEEE802154\_PHY\_A\_TURNAROUND\_TIME\_1MS | ( |  | *symbol\_period\_ns* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

**Value:**

[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)([NSEC\_PER\_MSEC](group__clock__apis.md#gad16e9029e202d2dfb4cfae8f09131f8f), symbol\_period\_ns)

[NSEC\_PER\_MSEC](group__clock__apis.md#gad16e9029e202d2dfb4cfae8f09131f8f)

#define NSEC\_PER\_MSEC

number of nanoseconds per millisecond

**Definition** sys\_clock.h:86

[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)

#define DIV\_ROUND\_UP(n, d)

Divide and round up.

**Definition** util.h:352

PHY PIB attribute aTurnaroundTime for SUN, RS-GFSK, TVWS, and LECIM FSK PHY, in PHY symbols, see section 11.3, table 11-1.

## [◆ ](#ga9e95bf5d8ddb1087cdd9eb2aa80d100e)IEEE802154\_PHY\_A\_TURNAROUND\_TIME\_DEFAULT

| #define IEEE802154\_PHY\_A\_TURNAROUND\_TIME\_DEFAULT   12U |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

Default PHY PIB attribute aTurnaroundTime, in PHY symbols, see section 11.3, table 11-1.

## [◆ ](#ga1dc4319d0a8d979c7455e1f71f45d885)IEEE802154\_PHY\_BPSK\_868MHZ\_SYMBOL\_PERIOD\_NS

| #define IEEE802154\_PHY\_BPSK\_868MHZ\_SYMBOL\_PERIOD\_NS   50000LL |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

BPSK 868MHz band symbol period, see section 13.3.3.

## [◆ ](#gaa12344b6a118995b63c5bd4bc3180efd)IEEE802154\_PHY\_BPSK\_915MHZ\_SYMBOL\_PERIOD\_NS

| #define IEEE802154\_PHY\_BPSK\_915MHZ\_SYMBOL\_PERIOD\_NS   25000LL |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

BPSK 915MHz band symbol period, see section 13.3.3.

## [◆ ](#gae02b981a3908b05b4bc0b7a2844c27c7)IEEE802154\_PHY\_HRP\_UWB\_ERDEV

| #define IEEE802154\_PHY\_HRP\_UWB\_ERDEV |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

**Value:**

([IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_64\_M\_BPRF](#gga13610aeef06372bc47d84464537fddedad920ae285cdcc2a4d59f7c23e29dce27) | [IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_128\_M\_HPRF](#gga13610aeef06372bc47d84464537fddedae6c88efd301a449b1a31e8aedf4e30ca) | \

[IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_256\_M\_HPRF](#gga13610aeef06372bc47d84464537fddedacb66442cf2a5e4c539b6b7edf8419be1))

[IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_256\_M\_HPRF](#gga13610aeef06372bc47d84464537fddedacb66442cf2a5e4c539b6b7edf8419be1)

@ IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_256\_M\_HPRF

**Definition** ieee802154\_radio.h:395

[IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_64\_M\_BPRF](#gga13610aeef06372bc47d84464537fddedad920ae285cdcc2a4d59f7c23e29dce27)

@ IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_64\_M\_BPRF

enhanced ranging device (ERDEV) modes not specified in table 8-88, see IEEE 802.15....

**Definition** ieee802154\_radio.h:393

[IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_128\_M\_HPRF](#gga13610aeef06372bc47d84464537fddedae6c88efd301a449b1a31e8aedf4e30ca)

@ IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_128\_M\_HPRF

**Definition** ieee802154\_radio.h:394

ERDEV device mask.

## [◆ ](#gaa25ba5b644e58cfc7de5ba5aa526ea71)IEEE802154\_PHY\_HRP\_UWB\_ERDEV\_TPSYM\_SYMBOL\_PERIOD\_NS

| #define IEEE802154\_PHY\_HRP\_UWB\_ERDEV\_TPSYM\_SYMBOL\_PERIOD\_NS   729.17F |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

ERDEV symbol period.

## [◆ ](#ga0123679fba7ca668aa158813f1bf2302)IEEE802154\_PHY\_HRP\_UWB\_PRF16\_TPSYM\_SYMBOL\_PERIOD\_NS

| #define IEEE802154\_PHY\_HRP\_UWB\_PRF16\_TPSYM\_SYMBOL\_PERIOD\_NS   993.59F |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

Nominal PRF 16MHz symbol period.

## [◆ ](#gabeb8a359ce54618aa7df3ee8f6a434bb)IEEE802154\_PHY\_HRP\_UWB\_PRF4\_TPSYM\_SYMBOL\_PERIOD\_NS

| #define IEEE802154\_PHY\_HRP\_UWB\_PRF4\_TPSYM\_SYMBOL\_PERIOD\_NS   3974.36F |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

Nominal PRF 4MHz symbol period.

## [◆ ](#ga59f8ba8a01171c56da6f7ae7f8983bf7)IEEE802154\_PHY\_HRP\_UWB\_PRF64\_TPSYM\_SYMBOL\_PERIOD\_NS

| #define IEEE802154\_PHY\_HRP\_UWB\_PRF64\_TPSYM\_SYMBOL\_PERIOD\_NS   1017.63F |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

Nominal PRF 64MHz symbol period.

## [◆ ](#gacfd2faf2c3072f8851abd74fe5148ec5)IEEE802154\_PHY\_HRP\_UWB\_RDEV

| #define IEEE802154\_PHY\_HRP\_UWB\_RDEV |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

**Value:**

([IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_4\_M](#gga13610aeef06372bc47d84464537fddeda9dc3c58366502aeab04a208937536369) | [IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_16\_M](#gga13610aeef06372bc47d84464537fddedadf9230e6ef62ce66129bfe24f537c88a) | \

[IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_64\_M](#gga13610aeef06372bc47d84464537fddeda2b24236d3531cab7d21673d065b7c29e))

[IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_64\_M](#gga13610aeef06372bc47d84464537fddeda2b24236d3531cab7d21673d065b7c29e)

@ IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_64\_M

**Definition** ieee802154\_radio.h:386

[IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_4\_M](#gga13610aeef06372bc47d84464537fddeda9dc3c58366502aeab04a208937536369)

@ IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_4\_M

**Definition** ieee802154\_radio.h:384

[IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_16\_M](#gga13610aeef06372bc47d84464537fddedadf9230e6ef62ce66129bfe24f537c88a)

@ IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_16\_M

**Definition** ieee802154\_radio.h:385

RDEV device mask.

## [◆ ](#gaff3d58945d53e824f1fb1ca11dd9997b)IEEE802154\_PHY\_OQPSK\_780\_TO\_2450MHZ\_SYMBOL\_PERIOD\_NS

| #define IEEE802154\_PHY\_OQPSK\_780\_TO\_2450MHZ\_SYMBOL\_PERIOD\_NS   16000LL |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

O-QPSK 780MHz, 915MHz, 2380MHz and 2450MHz bands symbol period, see section 12.3.3.

## [◆ ](#ga32ce931f3d35d779e4251c37f61583f5)IEEE802154\_PHY\_OQPSK\_868MHZ\_SYMBOL\_PERIOD\_NS

| #define IEEE802154\_PHY\_OQPSK\_868MHZ\_SYMBOL\_PERIOD\_NS   40000LL |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

O-QPSK 868Mhz band symbol period, see section 12.3.3.

## [◆ ](#ga155b5b5a06311c1bde3f36e06d02ed7d)IEEE802154\_PHY\_SUN\_FSK\_863MHZ\_915MHZ\_SYMBOL\_PERIOD\_NS

| #define IEEE802154\_PHY\_SUN\_FSK\_863MHZ\_915MHZ\_SYMBOL\_PERIOD\_NS   20000LL |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

SUN FSK 863Mhz and 915MHz band symbol periods, see section 19.1, table 19-1.

## [◆ ](#gac088ee6d01014a12169e74111ea61993)IEEE802154\_PHY\_SUN\_FSK\_PHR\_LEN

| #define IEEE802154\_PHY\_SUN\_FSK\_PHR\_LEN   2 |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

SUN FSK PHY header length, in bytes, see section 19.2.4.

## [◆ ](#gaf228d9c26cedd5c790b7ebae41b5f937)IEEE802154\_PHY\_SYMBOLS\_PER\_SECOND

| #define IEEE802154\_PHY\_SYMBOLS\_PER\_SECOND | ( |  | *symbol\_period\_ns* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

**Value:**

([NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc) / symbol\_period\_ns)

[NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)

#define NSEC\_PER\_SEC

number of nanoseconds per second

**Definition** sys\_clock.h:107

The symbol period (and therefore symbol rate) is defined in section 6.1: "Some of the timing parameters in definition of the MAC are in units of PHY symbols.

For PHYs that have multiple symbol periods, the duration to be used for the MAC parameters is defined in that PHY clause."

This is not necessarily the true physical symbol period, so take care to use this macro only when either the symbol period used for MAC timing is the same as the physical symbol period or if you actually mean the MAC timing symbol period.

PHY specific symbol periods are defined in PHY specific sections below.

## [◆ ](#gaaaf32be17c41497c8d3be48292ad1374)IEEE802154\_TIME\_CORRECTION\_HEADER\_IE\_LEN

| #define IEEE802154\_TIME\_CORRECTION\_HEADER\_IE\_LEN   ([IEEE802154\_HEADER\_IE\_HEADER\_LENGTH](#ga4f66344126179e2c98a17f19f6db516b) + [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(struct [ieee802154\_header\_ie\_time\_correction](structieee802154__header__ie__time__correction.md))) |
| --- |

`#include <[ieee802154_ie.h](ieee802154__ie_8h.md)>`

The length in bytes of a "Time Correction" header IE.

## Typedef Documentation

## [◆ ](#ga8c9ab3cecefe641a25f003eb6d014fc5)energy\_scan\_done\_cb\_t

| typedef void(\* energy\_scan\_done\_cb\_t) (const struct [device](structdevice.md) \*dev, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) max\_ed) |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

Energy scan callback.

## [◆ ](#ga8219b80b8b179fc3a2ffac0dfdfb4e4b)ieee802154\_event\_cb\_t

| typedef void(\* ieee802154\_event\_cb\_t) (const struct [device](structdevice.md) \*dev, enum [ieee802154\_event](#ga3491982b677941442d904ce69fce7c5e) evt, void \*event\_params) |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

Driver event callback.

## Enumeration Type Documentation

## [◆ ](#gaf4deddd3f23ebfd65fa47c5d62634430)ieee802154\_attr

| enum [ieee802154\_attr](#gaf4deddd3f23ebfd65fa47c5d62634430) |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

IEEE 802.15.4 driver attributes.

See [ieee802154\_attr\_value](structieee802154__attr__value.md "ieee802154_attr_value") and [ieee802154\_radio\_api](structieee802154__radio__api.md "ieee802154_radio_api") for usage details.

| Enumerator | |
| --- | --- |
| IEEE802154\_ATTR\_PHY\_SUPPORTED\_CHANNEL\_PAGES | Retrieves a bit field with supported channel pages.  This attribute SHALL be implemented by all drivers. |
| IEEE802154\_ATTR\_PHY\_SUPPORTED\_CHANNEL\_RANGES | Retrieves a pointer to the array of supported channel ranges within the currently configured channel page.  This attribute SHALL be implemented by all drivers. |
| IEEE802154\_ATTR\_PHY\_HRP\_UWB\_SUPPORTED\_PRFS | Retrieves a bit field with supported HRP UWB nominal pulse repetition frequencies.  This attribute SHALL be implemented by all devices that support channel page four (HRP UWB). |
| IEEE802154\_ATTR\_COMMON\_COUNT | Number of attributes defined in [ieee802154\_attr](#gaf4deddd3f23ebfd65fa47c5d62634430). |
| IEEE802154\_ATTR\_PRIV\_START | This and higher values are specific to the protocol- or driver-specific extensions. |

## [◆ ](#ga34aecc5996174a812b295a3a4693ad09)ieee802154\_config\_type

| enum [ieee802154\_config\_type](#ga34aecc5996174a812b295a3a4693ad09) |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

IEEE 802.15.4 driver configuration types.

| Enumerator | |
| --- | --- |
| IEEE802154\_CONFIG\_AUTO\_ACK\_FPB | Indicates how the driver should set the Frame Pending bit in ACK responses for Data Requests.  If enabled, the driver should determine whether to set the bit or not based on the information provided with [IEEE802154\_CONFIG\_ACK\_FPB](#gga34aecc5996174a812b295a3a4693ad09ab897aea56ea5e9ddf306c5c0d75c2cd7) config and FPB address matching mode specified. Otherwise, Frame Pending bit should be set to 1 (see section 6.7.3).  Note  requires [IEEE802154\_HW\_TX\_RX\_ACK](#ggaf99cda89c29df3c0088fc57ec09cbcd4ab383a932c0ac9deece68f02210089119) capability and is available in any interface operational state. |
| IEEE802154\_CONFIG\_ACK\_FPB | Indicates whether to set ACK Frame Pending bit for specific address or not.  Disabling the Frame Pending bit with no address provided (NULL pointer) should disable it for all enabled addresses.  Note  requires [IEEE802154\_HW\_TX\_RX\_ACK](#ggaf99cda89c29df3c0088fc57ec09cbcd4ab383a932c0ac9deece68f02210089119) capability and is available in any interface operational state. |
| IEEE802154\_CONFIG\_PAN\_COORDINATOR | Indicates whether the device is a PAN coordinator.  This influences packet filtering.  Note  Available in any interface operational state. |
| IEEE802154\_CONFIG\_PROMISCUOUS | Enable/disable promiscuous mode.  Note  Available in any interface operational state. |
| IEEE802154\_CONFIG\_EVENT\_HANDLER | Specifies new IEEE 802.15.4 driver event handler.  Specifying NULL as a handler will disable events notification.  Note  Available in any interface operational state. |
| IEEE802154\_CONFIG\_MAC\_KEYS | Updates MAC keys, key index and the per-key frame counter for drivers supporting transmit security offloading, see section 9.5, tables 9-9 and 9-10.  The key configuration SHALL NOT be accepted if the frame counter (in case frame counter per key is true) is not strictly larger than the current frame counter associated with the same key, see sections 8.2.2, 9.2.4 g/h) and 9.4.3.  Note  Requires [IEEE802154\_HW\_TX\_SEC](#ggaf99cda89c29df3c0088fc57ec09cbcd4a7924c3d5bfe6dceeb2e8caa6df7edecb) capability and is available in any interface operational state. |
| IEEE802154\_CONFIG\_FRAME\_COUNTER | Sets the current MAC frame counter value associated with the interface for drivers supporting transmit security offloading, see section 9.5, table 9-8, secFrameCounter.  Warning  The frame counter MUST NOT be accepted if it is not strictly greater than the current frame counter associated with the interface, see sections 8.2.2, 9.2.4 g/h) and 9.4.3. Otherwise the replay protection provided by the frame counter may be compromised. Drivers SHALL return -EINVAL in case the configured frame counter does not conform to this requirement.  Note  Requires [IEEE802154\_HW\_TX\_SEC](#ggaf99cda89c29df3c0088fc57ec09cbcd4a7924c3d5bfe6dceeb2e8caa6df7edecb) capability and is available in any interface operational state. |
| IEEE802154\_CONFIG\_FRAME\_COUNTER\_IF\_LARGER | Sets the current MAC frame counter value if the provided value is greater than the current one.  Note  Requires [IEEE802154\_HW\_TX\_SEC](#ggaf99cda89c29df3c0088fc57ec09cbcd4a7924c3d5bfe6dceeb2e8caa6df7edecb) capability and is available in any interface operational state.  Warning  This configuration option does not conform to the requirements specified in #61227 as it is redundant with [IEEE802154\_CONFIG\_FRAME\_COUNTER](#gga34aecc5996174a812b295a3a4693ad09aad7d04b7e1c02b2d88fcbb8ab1ac313b), and will therefore be deprecated in the future. |
| IEEE802154\_CONFIG\_RX\_SLOT | Set or unset a radio reception window (RX slot).  This can be used for any scheduled reception, e.g.: Zigbee GP device, CSL, TSCH, etc.  The start and duration parameters of the RX slot are relative to the network subsystem's local clock. If the start parameter of the RX slot is -1 then any previously configured RX slot SHALL be canceled immediately. If the start parameter is any value in the past (including 0) or the duration parameter is zero then the receiver SHALL remain off forever until the RX slot has either been removed or re-configured to point to a future start time. If an RX slot is configured while the previous RX slot is still scheduled, then the previous slot SHALL be cancelled and the new slot scheduled instead.  RX slots MAY be programmed while the driver is "DOWN". If any past or future RX slot is configured when calling start() then the interface SHALL be placed in "UP" state but the receiver SHALL not be started.  The driver SHALL take care to start/stop the receiver autonomously, asynchronously and automatically around the RX slot. The driver SHALL resume power just before the RX slot and suspend it again after the slot unless another programmed event forces the driver not to suspend. The driver SHALL switch to the programmed channel before the RX slot and back to the channel set with set\_channel() after the RX slot. If the driver interface is "DOWN" when the start time of an RX slot arrives, then the RX slot SHALL not be observed and the receiver SHALL remain off.  If the driver is "UP" while configuring an RX slot, the driver SHALL turn off the receiver immediately and (possibly asynchronously) put the driver into the lowest possible power saving mode until the start of the RX slot. If the driver is "UP" while the RX slot is deleted, then the driver SHALL enable the receiver immediately. The receiver MUST be ready to receive packets before returning from the configure() operation in this case.  This behavior means that setting an RX slot implicitly sets the MAC PIB attribute macRxOnWhenIdle (see section 8.4.3.1, table 8-94) to "false" while deleting the RX slot implicitly sets macRxOnWhenIdle to "true".  Note  requires [IEEE802154\_HW\_RXTIME](#ggaf99cda89c29df3c0088fc57ec09cbcd4a68ae68c83a87f0efc25f74edd80c4600) capability and is available in any interface operational state.  Required for Thread 1.2 Coordinated Sampled Listening feature (see Thread specification 1.2.0, ch. 3.2.6.3). |
| IEEE802154\_CONFIG\_CSL\_PERIOD | Enables or disables a device as a CSL receiver and configures its CSL period.  Configures the CSL period in units of 10 symbol periods. Values greater than zero enable CSL if the driver supports it and the device starts to operate as a CSL receiver. Setting this to zero disables CSL on the device. If the driver does not support CSL, the configuration call SHALL return -ENOTSUP.  See section 7.4.2.3 and section 8.4.3.6, table 8-104, macCslPeriod.  Note  Confusingly the standard calls the CSL receiver "CSL coordinator" (i.e. "coordinating the CSL protocol timing", see section 6.12.2.2), although, typically, a CSL coordinator is NOT also an IEEE 802.15.4 FFD coordinator or PAN coordintor but a simple RFD end device (compare the device roles outlined in sections 5.1, 5.3, 5.5 and 6.1). To avoid confusion we therefore prefer calling CSL coordinators (typically an RFD end device) "CSL receivers" and CSL peer devices (typically FFD coordinators or PAN coordinators) "CSL transmitters". Also note that at this time, we do NOT support unsynchronized transmission with CSL wake up frames as specified in section 6.12.2.4.4.  To offload CSL receiver timing to the driver the upper layer SHALL combine several configuration options in the following way:   1. Use [IEEE802154\_CONFIG\_ENH\_ACK\_HEADER\_IE](#gga34aecc5996174a812b295a3a4693ad09a840e5f1db9a354e7bcd892ddb4117907) once with an appropriate pre-filled CSL IE and the CSL phase set to an arbitrary value or left uninitialized. The CSL phase SHALL be injected on-the-fly by the driver at runtime as outlined in 2. below. Adding a short and extended address will inform the driver of the specific CSL receiver to which it SHALL inject CSL IEs. If no addresses are given then the CSL IE will be injected into all enhanced ACK frames as soon as CSL is enabled. This configuration SHALL be done before enabling CSL by setting a CSL period greater than zero. 2. Configure [IEEE802154\_CONFIG\_EXPECTED\_RX\_TIME](#gga34aecc5996174a812b295a3a4693ad09a1a71ef76d90b6882196e4c6473de6bd8) immediately followed by [IEEE802154\_CONFIG\_CSL\_PERIOD](#gga34aecc5996174a812b295a3a4693ad09a9fdbe95e0b7141d9150eaa4a5793c2e7). To prevent race conditions, the upper layer SHALL ensure that the receiver is not enabled during or between the two calls (e.g. by a previously configured RX slot) nor SHALL a frame be transmitted concurrently.  The expected RX time SHALL point to the end of SFD of an ideally timed RX frame in an arbitrary past or future CSL channel sample, i.e. whose "end of SFD" arrives exactly at the locally predicted time inside the CSL channel sample.  The driver SHALL derive CSL anchor points and the CSL phase from the given expected RX time as follows:      ```    cslAnchorPointNs = last expected RX time                       + PHY-specific PHR duration in ns     startOfMhrNs = start of MHR of the frame containing the                   CSL IE relative to the local network clock     cslPhase = (startOfMhrNs - cslAnchorPointNs)               / (10 * PHY specific symbol period in ns)               % cslPeriod    ```      The driver SHALL set the CSL phase in the IE configured in 1. and inject that IE on-the-fly into outgoing enhanced ACK frames if the destination address conforms to the IE's address filter. 3. Use [IEEE802154\_CONFIG\_RX\_SLOT](#gga34aecc5996174a812b295a3a4693ad09af4e3dd7588ee06458f2d42f02797b3d6) periodically to schedule each CSL channel sample early enough before its start time. The size of the CSL channel sample SHALL take relative clock drift and scheduling uncertainties with respect to CSL transmitters into account as specified by the standard such that at least the full SHR of a legitimate RX frame is guaranteed to land inside the channel sample.  To this avail, the last configured expected RX time plus an integer number of CSL periods SHALL point to a fixed offset of the RX slot (not necessarily its center):      ```    expectedRxTimeNs_N = last expected RX time        + N * (cslPeriod * 10 * PHY-specific symbol period in ns)     expectedRxTimeNs_N - rxSlot_N.start == const for all N    ```      While the configured CSL period is greater than zero, drivers SHOULD validate the offset of the expected RX time inside each RX slot accordingly. If the driver finds that the offset varies from slot to slot, drivers SHOULD log the difference but SHALL nevertheless accept and schedule the RX slot with a zero success value to work around minor implementation or rounding errors in upper layers.   Configure and start a CSL receiver:   ``` ENH_ACK_HEADER_IE    |    | EXPECTED_RX_TIME (end of SFD of a perfectly timed RX frame    |    |              in any past or future channel sample)    |    |    |    | CSL_PERIOD (>0)            RX_SLOT    |    |    |                          |    v    v    v                          v -----------------------------------------------[-CSL channel sample ]----+                                     ^                                    |                                     |                                    |                                     +--------------------- loop ---------+ ```   Disable CSL on the receiver:   ``` CSL_PERIOD (=0)    |    v --------------------- ```   Update the CSL period to a new value:   ``` EXPECTED_RX_TIME (based on updated period)    |    |  CSL_PERIOD (>0, updated)       RX_SLOT    |     |                              |    v     v                              v -----------------------------------------------[-CSL channel sample ]----+                                     ^                                    |                                     |                                    |                                     +--------------------- loop ---------+ ```   Note  Available in any interface operational state.  Required for Thread 1.2 Coordinated Sampled Listening feature (see Thread specification 1.2.0, ch. 3.2.6.3). |
| IEEE802154\_CONFIG\_EXPECTED\_RX\_TIME | Configure a timepoint at which an RX frame is expected to arrive.  Configure the nanosecond resolution timepoint relative to the network subsystem's local clock at which an RX frame's end of SFD (i.e. equivalently its end of SHR, start of PHR, or in the case of PHYs with RDEV or ERDEV capability the RMARKER) is expected to arrive at the local antenna assuming perfectly synchronized local and remote network clocks and zero distance between antennas.  This parameter MAY be used to offload parts of timing sensitive TDMA (e.g. TSCH, beacon-enabled PAN including DSME), low-energy (e.g. CSL, RIT) or ranging (TDoA) protocols to the driver. In these protocols, medium access is tightly controlled such that the expected arrival time of a frame can be predicted within a well-defined time window. This feature will typically be combined with [IEEE802154\_CONFIG\_RX\_SLOT](#gga34aecc5996174a812b295a3a4693ad09af4e3dd7588ee06458f2d42f02797b3d6) although this is not a hard requirement.  The "expected RX time" MAY be interpreted slightly differently depending on the protocol context:   - CSL phase (i.e. time to the next expected CSL transmission) or anchor time (i.e. any arbitrary timepoint with "zero CSL phase") SHALL be derived by adding the PHY header duration to the expected RX time to calculate the "start of MHR" ("first symbol of MAC", see section 6.12.2.1) required by the CSL protocol, compare [IEEE802154\_CONFIG\_CSL\_PERIOD](#gga34aecc5996174a812b295a3a4693ad09a9fdbe95e0b7141d9150eaa4a5793c2e7). - In TSCH the expected RX time MAY be set to macTsRxOffset + macTsRxWait / 2. Then the time correction SHALL be calculated as the expected RX time minus actual arrival timestamp, see section 6.5.4.3. - In ranging applications, time difference of arrival (TDOA) MAY be calculated inside the driver comparing actual RMARKER timestamps against the assumed synchronized time at which the ranging frame was sent, see IEEE 802.15.4z.   In case of periodic protocols (e.g. CSL channel samples, periodic beacons of a single PAN, periodic ranging "blinks"), a single timestamp at any time in the past or in the future may be given from which other expected timestamps can be derived by adding or subtracting multiples of the RX period. See e.g. the CSL documentation in this API.  Additionally this parameter MAY be used by drivers to discipline their local representation of a distributed network clock by deriving synchronization instants related to a remote representation of the same clock (as in PTP).  Note  Available in any interface operational state.  Required for Thread 1.2 Coordinated Sampled Listening feature (see Thread specification 1.2.0, ch. 3.2.6.3). |
| IEEE802154\_CONFIG\_ENH\_ACK\_HEADER\_IE | Adds a header information element (IE) to be injected into enhanced ACK frames generated by the driver if the given destination address filter matches.  Drivers implementing the [IEEE802154\_HW\_RX\_TX\_ACK](#ggaf99cda89c29df3c0088fc57ec09cbcd4aec16c4d418117de2d106e84297568b03) capability generate ACK frames autonomously. Setting this configuration will ask the driver to inject the given preconfigured header IE when generating enhanced ACK frames where appropriate by the standard. IEs for all other frame types SHALL be provided by L2.  The driver shall return -ENOTSUP in the following cases:   - It does not support the [IEEE802154\_HW\_RX\_TX\_ACK](#ggaf99cda89c29df3c0088fc57ec09cbcd4aec16c4d418117de2d106e84297568b03), - It does not support header IE injection, - It cannot inject the runtime fields on-the-fly required for the given IE element ID (see list below).   Enhanced ACK header IEs (element IDs in parentheses) that either need to be rejected or explicitly supported and parsed by the driver because they require on-the-fly timing information injection are:   - CSL IE (0x1a) - Rendezvous Time IE (0x1d) - Time Correction IE (0x1e)   Drivers accepting this configuration option SHALL check the list of configured IEs for each outgoing enhanced ACK frame, select the ones appropriate for the received frame based on their element ID, inject any required runtime information on-the-fly and include the selected IEs into the enhanced ACK frame's MAC header.  Drivers supporting enhanced ACK header IE injection SHALL autonomously inject header termination IEs as required by the standard.  A destination short address and extended address MAY be given by L2 to filter the devices to which the given IE is included. Setting the short address to the broadcast address and the extended address to NULL will inject the given IE into all ACK frames unless a more specific filter is also present for any given destination device (fallback configuration). L2 SHALL take care to either set both address fields to valid device addresses or none.  This configuration type may be called several times with distinct element IDs and/or addresses. The driver SHALL either store all configured IE/address combinations or return -ENOMEM if no additional configuration can be stored.  Configuring a header IE with a previously configured element ID and address filter SHALL override the previous configuration. This implies that repetition of the same header IE/address combination is NOT supported.  Configuring an existing element ID/address filter combination with the header IE's length field set to zero SHALL remove that configuration. SHALL remove the fallback configuration if no address is given.  Configuring a header IE for an address filter with the header IE pointer set to NULL SHALL remove all header IE's for that address filter. SHALL remove ALL header IE configuration (including but not limited to fallbacks) if no address is given.  If any of the deleted configurations didn't previously exist, then the call SHALL be ignored. Whenever the length field is set to zero, the content fields MUST NOT be accessed by the driver.  L2 SHALL minimize the space required to keep IE configuration inside the driver by consolidating address filters and by removing configuration that is no longer required.  Note  requires [IEEE802154\_HW\_RX\_TX\_ACK](#ggaf99cda89c29df3c0088fc57ec09cbcd4aec16c4d418117de2d106e84297568b03) capability and is available in any interface operational state. Currently we only support header IEs but that may change in the future.  Required for Thread 1.2 Coordinated Sampled Listening feature (see Thread specification 1.2.0, ch. 3.2.6.3).  Required for Thread 1.2 Link Metrics feature (see Thread specification 1.2.0, ch. 4.11.3.3). |
| IEEE802154\_CONFIG\_RX\_ON\_WHEN\_IDLE | Enable/disable RxOnWhenIdle MAC PIB attribute (Table 8-94).  Since there is no clear guidance in IEEE 802.15.4 specification about the definition of an "idle period", this implementation expects that drivers use the RxOnWhenIdle attribute to determine next radio state (false --> off, true --> receive) in the following scenarios:   - Finalization of a regular frame reception task, provided that:   - The frame is received without errors and passes the filtering and it's not an spurious ACK.   - ACK is not requested or transmission of ACK is not possible due to internal conditions. - Finalization of a frame transmission or transmission of an ACK frame, when ACK is not requested in the transmitted frame. - Finalization of the reception operation of a requested ACK due to:   - ACK timeout expiration.   - Reception of an invalid ACK or not an ACK frame.   - Reception of the proper ACK, unless the transmitted frame was a Data Request Command and the frame pending bit on the received ACK is set to true. In this case the radio platform implementation SHOULD keep the receiver on until a determined timeout which triggers an idle period start. - Finalization of a stand alone CCA task. - Finalization of a CCA operation with busy result during CSMA/CA procedure. - Finalization of an Energy Detection task. - Finalization of a scheduled radio reception window (see [IEEE802154\_CONFIG\_RX\_SLOT](#gga34aecc5996174a812b295a3a4693ad09af4e3dd7588ee06458f2d42f02797b3d6)). |
| IEEE802154\_CONFIG\_COMMON\_COUNT | Number of types defined in [ieee802154\_config\_type](#ga34aecc5996174a812b295a3a4693ad09). |
| IEEE802154\_CONFIG\_PRIV\_START | This and higher values are specific to the protocol- or driver-specific extensions. |

## [◆ ](#ga3491982b677941442d904ce69fce7c5e)ieee802154\_event

| enum [ieee802154\_event](#ga3491982b677941442d904ce69fce7c5e) |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

Driver events, see [IEEE802154\_CONFIG\_EVENT\_HANDLER](#gga34aecc5996174a812b295a3a4693ad09a8d88a76f71cf8869b3e35e423b18c6f3).

| Enumerator | |
| --- | --- |
| IEEE802154\_EVENT\_TX\_STARTED | Data transmission started. |
| IEEE802154\_EVENT\_RX\_FAILED | Data reception failed. |
| IEEE802154\_EVENT\_RX\_OFF | An RX slot ended, requires [IEEE802154\_HW\_RXTIME](#ggaf99cda89c29df3c0088fc57ec09cbcd4a68ae68c83a87f0efc25f74edd80c4600).  Note  This event SHALL not be triggered by drivers when RX is synchronously switched of due to a call to stop() or an RX slot being configured. |

## [◆ ](#gaa1971591e72866d0f3f0d4db2931e25a)ieee802154\_filter\_type

| enum [ieee802154\_filter\_type](#gaa1971591e72866d0f3f0d4db2931e25a) |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

Filter type, see [ieee802154\_radio\_api::filter](structieee802154__radio__api.md#aa9502e0e014a8d05ffe235567e8c98f3 "ieee802154_radio_api::filter").

| Enumerator | |
| --- | --- |
| IEEE802154\_FILTER\_TYPE\_IEEE\_ADDR | Address type filter. |
| IEEE802154\_FILTER\_TYPE\_SHORT\_ADDR | Short address type filter. |
| IEEE802154\_FILTER\_TYPE\_PAN\_ID | PAN id type filter. |
| IEEE802154\_FILTER\_TYPE\_SRC\_IEEE\_ADDR | Source address type filter. |
| IEEE802154\_FILTER\_TYPE\_SRC\_SHORT\_ADDR | Source short address type filter. |

## [◆ ](#gab593bc6640ddea23c951982ca2f4c0bf)ieee802154\_fpb\_mode

| enum [ieee802154\_fpb\_mode](#gab593bc6640ddea23c951982ca2f4c0bf) |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

IEEE 802.15.4 Frame Pending Bit table address matching mode.

| Enumerator | |
| --- | --- |
| IEEE802154\_FPB\_ADDR\_MATCH\_THREAD | The pending bit shall be set only for addresses found in the list. |
| IEEE802154\_FPB\_ADDR\_MATCH\_ZIGBEE | The pending bit shall be cleared for short addresses found in the list. |

## [◆ ](#ga0de396c2c2c781ff85b94ebf577f15ce)ieee802154\_header\_ie\_element\_id

| enum [ieee802154\_header\_ie\_element\_id](#ga0de396c2c2c781ff85b94ebf577f15ce) |
| --- |

`#include <[ieee802154_ie.h](ieee802154__ie_8h.md)>`

Header Information Element IDs.

See section 7.4.2.1, table 7-7, partial list, only IEs actually used are implemented.

| Enumerator | |
| --- | --- |
| IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_VENDOR\_SPECIFIC\_IE | Vendor specific IE. |
| IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_CSL\_IE | CSL IE. |
| IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_RIT\_IE | RIT IE. |
| IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_RENDEZVOUS\_TIME\_IE | Rendezvous time IE. |
| IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_TIME\_CORRECTION\_IE | Time correction IE. |
| IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_HEADER\_TERMINATION\_1 | Header termination 1. |
| IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_HEADER\_TERMINATION\_2 | Header termination 2. |

## [◆ ](#gaf99cda89c29df3c0088fc57ec09cbcd4)ieee802154\_hw\_caps

| enum [ieee802154\_hw\_caps](#gaf99cda89c29df3c0088fc57ec09cbcd4) |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

IEEE 802.15.4 driver capabilities.

Any driver properties that can be represented in binary form should be modeled as capabilities. These are called "hardware" capabilities for historical reasons but may also represent driver firmware capabilities (e.g. MAC offloading features).

| Enumerator | |
| --- | --- |
| IEEE802154\_HW\_ENERGY\_SCAN | Energy detection (ED) supported (optional). |
| IEEE802154\_HW\_FCS | Frame checksum verification supported. |
| IEEE802154\_HW\_FILTER | Filtering of PAN ID, extended and short address supported. |
| IEEE802154\_HW\_PROMISC | Promiscuous mode supported. |
| IEEE802154\_HW\_CSMA | CSMA-CA procedure supported on TX. |
| IEEE802154\_HW\_TX\_RX\_ACK | Waits for ACK on TX if AR bit is set in TX pkt. |
| IEEE802154\_HW\_RETRANSMISSION | Supports retransmission on TX ACK timeout. |
| IEEE802154\_HW\_RX\_TX\_ACK | Sends ACK on RX if AR bit is set in RX pkt. |
| IEEE802154\_HW\_TXTIME | TX at specified time supported. |
| IEEE802154\_HW\_SLEEP\_TO\_TX | TX directly from sleep supported.  Note  This HW capability does not conform to the requirements specified in #61227 as it closely couples the driver to OpenThread's capability and device model which is different from Zephyr's:  - "Sleeping" is a well defined term in Zephyr related to internal power and thread management and different from "RX off" as defined in OT. - Currently all OT-capable drivers have the "sleep to TX" capability anyway plus we expect future drivers to implement it ootb as well, so no information is actually conveyed by this capability. - The start()/stop() API of a net device controls the interface's operational state. Drivers MUST respond with -ENETDOWN when calling tx() while their operational state is "DOWN", only devices in the "UP" state MAY transmit packets (RFC 2863). - A migration path has been defined in #63670 for actual removal of this capability in favor of a standard compliant configure(rx\_on/rx\_off) call, see there for details.  **[Deprecated](deprecated.md#_deprecated000028)**  Drivers and L2 SHALL not introduce additional references to this capability and remove existing ones as outlined in #63670. |
| IEEE802154\_HW\_RXTIME | Timed RX window scheduling supported. |
| IEEE802154\_HW\_TX\_SEC | TX security supported (key management, encryption and authentication). |
| IEEE802154\_RX\_ON\_WHEN\_IDLE | RxOnWhenIdle handling supported. |
| IEEE802154\_HW\_SELECTIVE\_TXCHANNEL | Support for timed transmissions on selective channel.  This capability informs that transmissions with modes [IEEE802154\_TX\_MODE\_TXTIME](#ggab2bee8752291e082cb277145cef1225da9a7b8ba25603b72aecbf7f66abf26508) and [IEEE802154\_TX\_MODE\_TXTIME\_CCA](#ggab2bee8752291e082cb277145cef1225da42b4589afb2180fde053fdbbf58c0d3e) support scheduling of timed transmissions on selective tx channel. The driver MAY have this capability only if the Kconfig option CONFIG\_IEEE802154\_SELECTIVE\_TXCHANNEL is set, otherwise the driver MUST NOT have this capability.  Please refer to the [ieee802154\_radio\_api::tx](structieee802154__radio__api.md#a70139acec22642c1fc09f2323c383fe6 "Transmit a packet fragment as a single frame.") documentation for details. |

## [◆ ](#ga207e3aa0454f9e4173c809cfe7ff32cd)ieee802154\_ie\_type

| enum [ieee802154\_ie\_type](#ga207e3aa0454f9e4173c809cfe7ff32cd) |
| --- |

`#include <[ieee802154_ie.h](ieee802154__ie_8h.md)>`

Information Element Types.

See sections 7.4.2.1 and 7.4.3.1.

| Enumerator | |
| --- | --- |
| IEEE802154\_IE\_TYPE\_HEADER | Header type. |
| IEEE802154\_IE\_TYPE\_PAYLOAD | Payload type. |

## [◆ ](#gacabc7386bea701373dfb36ab65bd36a9)ieee802154\_phy\_channel\_page

| enum [ieee802154\_phy\_channel\_page](#gacabc7386bea701373dfb36ab65bd36a9) |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

PHY channel pages, see section 10.1.3.

A device driver must support the mandatory channel pages, frequency bands and channels of at least one IEEE 802.15.4 PHY.

Channel page and number assignments have developed over several versions of the standard and are not particularly well documented. Therefore some notes about peculiarities of channel pages and channel numbering:

- The 2006 version of the standard had a read-only phyChannelsSupported PHY PIB attribute that represented channel page/number combinations as a bitmap. This attribute was removed in later versions of the standard as the number of channels increased beyond what could be represented by a bit map. That's the reason why it was decided to represent supported channels as a combination of channel pages and ranges instead.
- In the 2020 version of the standard, 13 channel pages are explicitly defined, but up to 32 pages could in principle be supported. This was a hard requirement in the 2006 standard. In later standards it is implicit from field specifications, e.g. the MAC PIB attribute macChannelPage (section 8.4.3.4, table 8-100) or channel page fields used in the SRM protocol (see section 8.2.26.5).
- ASK PHY (channel page one) was deprecated in the 2015 version of the standard. The 2020 version of the standard is a bit ambivalent whether channel page one disappeared as well or should be interpreted as O-QPSK now (see section 10.1.3.3). In Zephyr this ambivalence is resolved by deprecating channel page one.
- For some PHYs the standard doesn't clearly specify a channel page, namely the GFSK, RS-GFSK, CMB and TASK PHYs. These are all rather new and left out in our list as long as no driver wants to implement them.

Warning
:   The bit numbers are not arbitrary but represent the channel page numbers as defined by the standard. Therefore do not change the bit numbering.

| Enumerator | |
| --- | --- |
| IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_ZERO\_OQPSK\_2450\_BPSK\_868\_915 | Channel page zero supports the 2.4G channels of the O-QPSK PHY and all channels from the BPSK PHYs initially defined in the 2003 editions of the standard.  For channel page zero, 16 channels are available in the 2450 MHz band (channels 11-26, O-QPSK), 10 in the 915 MHz band (channels 1-10, BPSK), and 1 in the 868 MHz band (channel 0, BPSK).  You can retrieve the channels supported by a specific driver on this page via [IEEE802154\_ATTR\_PHY\_SUPPORTED\_CHANNEL\_RANGES](#ggaf4deddd3f23ebfd65fa47c5d62634430aba76daa0a70bcdd573ecbfd63ca19e7d) attribute.  see section 10.1.3.3 |
| IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_ONE\_DEPRECATED | Formerly ASK PHY - deprecated in IEEE 802.15.4-2015. |
| IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_TWO\_OQPSK\_868\_915 | O-QPSK PHY - 868 MHz and 915 MHz bands, see section 10.1.3.3. |
| IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_THREE\_CSS | CSS PHY - 2450 MHz band, see section 10.1.3.4. |
| IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_FOUR\_HRP\_UWB | UWB PHY - SubG, low and high bands, see section 10.1.3.5. |
| IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_FIVE\_OQPSK\_780 | O-QPSK PHY - 780 MHz band, see section 10.1.3.2. |
| IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_SIX\_RESERVED | reserved - not currently assigned |
| IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_SEVEN\_MSK | MSK PHY - 780 MHz and 2450 MHz bands, see sections 10.1.3.6, 10.1.3.7. |
| IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_EIGHT\_LRP\_UWB | LRP UWB PHY, see sections 10.1.3.8. |
| IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_NINE\_SUN\_PREDEFINED | SUN FSK/OFDM/O-QPSK PHYs - predefined bands, operating modes and channels, see sections 10.1.3.9. |
| IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_TEN\_SUN\_FSK\_GENERIC | SUN FSK/OFDM/O-QPSK PHYs - generic modulation and channel description, see sections 10.1.3.9, 7.4.4.11. |
| IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_ELEVEN\_OQPSK\_2380 | O-QPSK PHY - 2380 MHz band, see section 10.1.3.10. |
| IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_TWELVE\_LECIM | LECIM DSSS/FSK PHYs, see section 10.1.3.11. |
| IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_THIRTEEN\_RCC | RCC PHY, see section 10.1.3.12. |

## [◆ ](#ga13610aeef06372bc47d84464537fdded)ieee802154\_phy\_hrp\_uwb\_nominal\_prf

| enum [ieee802154\_phy\_hrp\_uwb\_nominal\_prf](#ga13610aeef06372bc47d84464537fdded) |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

represents the nominal pulse rate frequency of an HRP UWB PHY

| Enumerator | |
| --- | --- |
| IEEE802154\_PHY\_HRP\_UWB\_PRF\_OFF | standard modes, see section 8.3.2, table 8-88. |
| IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_4\_M |  |
| IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_16\_M |  |
| IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_64\_M |  |
| IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_64\_M\_BPRF | enhanced ranging device (ERDEV) modes not specified in table 8-88, see IEEE 802.15.4z, section 15.1, section 15.2.6.2, table 15-7b, section 15.3.4.2 and section 15.3.4.3. |
| IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_128\_M\_HPRF |  |
| IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_256\_M\_HPRF |  |

## [◆ ](#ga04febbd15f9e6f6540d711ada5a4a1c8)ieee802154\_rx\_fail\_reason

| enum [ieee802154\_rx\_fail\_reason](#ga04febbd15f9e6f6540d711ada5a4a1c8) |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

RX failed event reasons, see [IEEE802154\_EVENT\_RX\_FAILED](#gga3491982b677941442d904ce69fce7c5eaef51197ca09befaee8cdfa2cde107273).

| Enumerator | |
| --- | --- |
| IEEE802154\_RX\_FAIL\_NOT\_RECEIVED | Nothing received. |
| IEEE802154\_RX\_FAIL\_INVALID\_FCS | Frame had invalid checksum. |
| IEEE802154\_RX\_FAIL\_ADDR\_FILTERED | Address did not match. |
| IEEE802154\_RX\_FAIL\_OTHER | General reason. |

## [◆ ](#gab2bee8752291e082cb277145cef1225d)ieee802154\_tx\_mode

| enum [ieee802154\_tx\_mode](#gab2bee8752291e082cb277145cef1225d) |
| --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

IEEE 802.15.4 Transmission mode.

| Enumerator | |
| --- | --- |
| IEEE802154\_TX\_MODE\_DIRECT | Transmit packet immediately, no CCA. |
| IEEE802154\_TX\_MODE\_CCA | Perform CCA before packet transmission. |
| IEEE802154\_TX\_MODE\_CSMA\_CA | Perform full CSMA/CA procedure before packet transmission.  Note  requires IEEE802154\_HW\_CSMA capability. |
| IEEE802154\_TX\_MODE\_TXTIME | Transmit packet in the future, at the specified time, no CCA.  Note  requires IEEE802154\_HW\_TXTIME capability.  capability IEEE802154\_HW\_SELECTIVE\_TXCHANNEL may apply. |
| IEEE802154\_TX\_MODE\_TXTIME\_CCA | Transmit packet in the future, perform CCA before transmission.  Note  requires IEEE802154\_HW\_TXTIME capability.  Required for Thread 1.2 Coordinated Sampled Listening feature (see Thread specification 1.2.0, ch. 3.2.6.3).  capability IEEE802154\_HW\_SELECTIVE\_TXCHANNEL may apply. |
| IEEE802154\_TX\_MODE\_COMMON\_COUNT | Number of modes defined in [ieee802154\_tx\_mode](#gab2bee8752291e082cb277145cef1225d). |
| IEEE802154\_TX\_MODE\_PRIV\_START | This and higher values are specific to the protocol- or driver-specific extensions. |

## Function Documentation

## [◆ ](#gaf69d2b65aa46ec4483c6bab419413ba5)ieee802154\_attr\_get\_channel\_page\_and\_range()

| | int ieee802154\_attr\_get\_channel\_page\_and\_range | ( | enum [ieee802154\_attr](#gaf4deddd3f23ebfd65fa47c5d62634430) | *attr*, | | --- | --- | --- | --- | |  |  | const enum [ieee802154\_phy\_channel\_page](#gacabc7386bea701373dfb36ab65bd36a9) | *phy\_supported\_channel\_page*, | |  |  | const struct [ieee802154\_phy\_supported\_channels](structieee802154__phy__supported__channels.md) \* | *phy\_supported\_channels*, | |  |  | struct [ieee802154\_attr\_value](structieee802154__attr__value.md) \* | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

Helper function to handle channel page and range to be called from drivers' attr\_get() implementation.

This only applies to drivers with a single channel page.

Parameters
:   | attr | The attribute to be retrieved. |
    | --- | --- |
    | phy\_supported\_channel\_page | The driver's unique channel page. |
    | phy\_supported\_channels | Pointer to the structure that contains the driver's channel range or ranges. |
    | value | The pointer to the value struct provided by the user. |

Return values
:   | 0 | if the attribute could be resolved |
    | --- | --- |
    | -ENOENT | if the attribute could not be resolved |

## [◆ ](#ga68e1f89571ccbefef61a5496577337fc)ieee802154\_handle\_ack()

| | enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) ieee802154\_handle\_ack | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | struct [net\_pkt](structnet__pkt.md) \* | *pkt* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

IEEE 802.15.4 driver ACK handling callback into L2 that drivers must call when receiving an ACK package.

The IEEE 802.15.4 standard prescribes generic procedures for ACK handling on L2 (MAC) level. L2 stacks therefore have to provides a fast and re-usable generic implementation of this callback for drivers to call when receiving an ACK packet.

Note: This function is part of Zephyr's 802.15.4 stack driver -> L2 "inversion-of-control" adaptation API and must be implemented by all IEEE 802.15.4 L2 stacks.

Parameters
:   | iface | A valid pointer on a network interface that received the packet |
    | --- | --- |
    | pkt | A valid pointer on a packet to check |

Returns
:   NET\_OK if L2 handles the ACK package, NET\_CONTINUE or NET\_DROP otherwise.

Warning
:   Deviating from other functions in the net stack returning [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896 "Net Verdict."), this function will not unref the package even if it returns NET\_OK.

## [◆ ](#gaec7f06d8bf0b44c3350d1d07a65c6cb4)ieee802154\_header\_ie\_get\_element\_id()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ieee802154\_header\_ie\_get\_element\_id | ( | struct ieee802154\_header\_ie \* | *ie* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ieee802154_ie.h](ieee802154__ie_8h.md)>`

Get the element ID of a header IE.

Parameters
:   | [in] | ie | pointer to a header IE |
    | --- | --- | --- |

Returns
:   header IE element id in CPU byte order

## [◆ ](#gaaae70f7d15135b2e77369cef3c61ba62)ieee802154\_header\_ie\_get\_time\_correction\_us()

| | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) ieee802154\_header\_ie\_get\_time\_correction\_us | ( | struct [ieee802154\_header\_ie\_time\_correction](structieee802154__header__ie__time__correction.md) \* | *ie* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ieee802154_ie.h](ieee802154__ie_8h.md)>`

Retrieve the time correction value in microseconds from a Time Correction IE, see section 7.4.2.7.

Parameters
:   | [in] | ie | pointer to the Time Correction IE structure |
    | --- | --- | --- |

Returns
:   The time correction value in microseconds.

## [◆ ](#gaef81648e58dc4fbdfd942a1d856952fa)ieee802154\_header\_ie\_set\_element\_id()

| | void ieee802154\_header\_ie\_set\_element\_id | ( | struct ieee802154\_header\_ie \* | *ie*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *element\_id* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ieee802154_ie.h](ieee802154__ie_8h.md)>`

Set the element ID of a header IE.

Parameters
:   | [in] | ie | pointer to a header IE |
    | --- | --- | --- |
    | [in] | element\_id | IE element id in CPU byte order |

## [◆ ](#gad2a4cb5df84ffe20b83fc54dc9bcfc91)ieee802154\_init()

| | void ieee802154\_init | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

IEEE 802.15.4 driver initialization callback into L2 called by drivers to initialize the active L2 stack for a given interface.

Drivers must call this function as part of their own initialization routine.

Note: This function is part of Zephyr's 802.15.4 stack driver -> L2 "inversion-of-control" adaptation API and must be implemented by all IEEE 802.15.4 L2 stacks.

Parameters
:   | iface | A valid pointer on a network interface |
    | --- | --- |

## [◆ ](#gaf5d7bdde2a9774f9d90604a6e203bb07)ieee802154\_is\_ar\_flag\_set()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ieee802154\_is\_ar\_flag\_set | ( | struct [net\_buf](structnet__buf.md) \* | *frag* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ieee802154_radio.h](ieee802154__radio_8h.md)>`

Check if the AR flag is set on the frame inside the given [Network Packet Library](group__net__pkt.md "Network Packet Library").

Parameters
:   | frag | A valid pointer on a [net\_buf](structnet__buf.md "Network buffer representation.") structure, must not be NULL, and its length should be at least 1 byte (ImmAck frames are the shortest supported frames with 3 bytes excluding FCS). |
    | --- | --- |

Returns
:   true if AR flag is set, false otherwise

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

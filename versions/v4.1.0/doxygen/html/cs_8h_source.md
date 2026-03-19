---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/cs_8h_source.html
original_path: doxygen/html/cs_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cs.h

[Go to the documentation of this file.](cs_8h.md)

1

4

5/\*

6 \* Copyright (c) 2024 Nordic Semiconductor ASA

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_CS\_H\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_CS\_H\_

12

19

20#include <[stdint.h](stdint_8h.md)>

21#include <[stdbool.h](stdbool_8h.md)>

22

23#include <[zephyr/bluetooth/hci\_types.h](hci__types_8h.md)>

24#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

25

26#ifdef \_\_cplusplus

27extern "C" {

28#endif

29

[ 38](group__bt__le__cs.md#ga95e2d24515e45096912440fe8a6bd3a0)#define BT\_LE\_CS\_CHANNEL\_BIT\_GET(chmap, bit) (((chmap)[(bit) / 8] >> ((bit) % 8)) & 1)

39

[ 47](group__bt__le__cs.md#gadcd3351ef99d42e93c89d48f1c8ba668)#define BT\_LE\_CS\_CHANNEL\_BIT\_SET\_VAL(chmap, bit, val) \

48 ((chmap)[(bit) / 8] = ((chmap)[(bit) / 8] & ~BIT((bit) % 8)) | ((val) << ((bit) % 8)))

49

[ 50](group__bt__le__cs.md#ga9f286cdeeee0e9df06e6b3df1e9ab643)enum [bt\_le\_cs\_sync\_antenna\_selection\_opt](group__bt__le__cs.md#ga9f286cdeeee0e9df06e6b3df1e9ab643) {

[ 52](group__bt__le__cs.md#gga9f286cdeeee0e9df06e6b3df1e9ab643a5de14d0cc770615bd08c4e3d197bae90) [BT\_LE\_CS\_ANTENNA\_SELECTION\_OPT\_ONE](group__bt__le__cs.md#gga9f286cdeeee0e9df06e6b3df1e9ab643a5de14d0cc770615bd08c4e3d197bae90) = [BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_ONE](hci__types_8h.md#a7fa26323384443ba9c5e635047b74f51),

[ 54](group__bt__le__cs.md#gga9f286cdeeee0e9df06e6b3df1e9ab643a7ce16e0eab20cf432c8e93a7f6be8ca5) [BT\_LE\_CS\_ANTENNA\_SELECTION\_OPT\_TWO](group__bt__le__cs.md#gga9f286cdeeee0e9df06e6b3df1e9ab643a7ce16e0eab20cf432c8e93a7f6be8ca5) = [BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_TWO](hci__types_8h.md#aa6d146c85e3148a2afb66023d94c2eeb),

[ 56](group__bt__le__cs.md#gga9f286cdeeee0e9df06e6b3df1e9ab643a35ae07887f3d55bcbd10d531f09c841d) [BT\_LE\_CS\_ANTENNA\_SELECTION\_OPT\_THREE](group__bt__le__cs.md#gga9f286cdeeee0e9df06e6b3df1e9ab643a35ae07887f3d55bcbd10d531f09c841d) = [BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_THREE](hci__types_8h.md#a8721a8f4670a8038d66d42adea061f57),

[ 58](group__bt__le__cs.md#gga9f286cdeeee0e9df06e6b3df1e9ab643aa5370917d0f46fe654ba42fbbd587ceb) [BT\_LE\_CS\_ANTENNA\_SELECTION\_OPT\_FOUR](group__bt__le__cs.md#gga9f286cdeeee0e9df06e6b3df1e9ab643aa5370917d0f46fe654ba42fbbd587ceb) = [BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_FOUR](hci__types_8h.md#af0d407f944831f8c85f91fb60f5bc618),

[ 60](group__bt__le__cs.md#gga9f286cdeeee0e9df06e6b3df1e9ab643aa23b552af8b16b1371f7a362089eaca7) [BT\_LE\_CS\_ANTENNA\_SELECTION\_OPT\_REPETITIVE](group__bt__le__cs.md#gga9f286cdeeee0e9df06e6b3df1e9ab643aa23b552af8b16b1371f7a362089eaca7) = [BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_REP](hci__types_8h.md#afad5b26b2a6ce125b6198856d20bcdd8),

[ 62](group__bt__le__cs.md#gga9f286cdeeee0e9df06e6b3df1e9ab643a861f35bdbe322238bdad67568e5674f3) [BT\_LE\_CS\_ANTENNA\_SELECTION\_OPT\_NO\_RECOMMENDATION](group__bt__le__cs.md#gga9f286cdeeee0e9df06e6b3df1e9ab643a861f35bdbe322238bdad67568e5674f3) = [BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_NONE](hci__types_8h.md#aed2444a40bc79ccf3f383dd961036f5e),

63};

64

[ 66](structbt__le__cs__set__default__settings__param.md)struct [bt\_le\_cs\_set\_default\_settings\_param](structbt__le__cs__set__default__settings__param.md) {

[ 68](structbt__le__cs__set__default__settings__param.md#a6a68056e10ea18ab2bb33202a39387a4) bool [enable\_initiator\_role](structbt__le__cs__set__default__settings__param.md#a6a68056e10ea18ab2bb33202a39387a4);

[ 70](structbt__le__cs__set__default__settings__param.md#a7e532de60b09424da17be0e61dbafb2d) bool [enable\_reflector\_role](structbt__le__cs__set__default__settings__param.md#a7e532de60b09424da17be0e61dbafb2d);

[ 73](structbt__le__cs__set__default__settings__param.md#a581ab5686e3eedfde84817d0ffcff587) enum [bt\_le\_cs\_sync\_antenna\_selection\_opt](group__bt__le__cs.md#ga9f286cdeeee0e9df06e6b3df1e9ab643) [cs\_sync\_antenna\_selection](structbt__le__cs__set__default__settings__param.md#a581ab5686e3eedfde84817d0ffcff587);

[ 80](structbt__le__cs__set__default__settings__param.md#a31a3b73d2bc44306f6905a2a1958b62b) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [max\_tx\_power](structbt__le__cs__set__default__settings__param.md#a31a3b73d2bc44306f6905a2a1958b62b);

81};

82

[ 84](group__bt__le__cs.md#ga782a500f611320a6f3feed9897ab8e16)enum [bt\_le\_cs\_test\_cs\_sync\_antenna\_selection](group__bt__le__cs.md#ga782a500f611320a6f3feed9897ab8e16) {

[ 85](group__bt__le__cs.md#gga782a500f611320a6f3feed9897ab8e16a054f9b7f51323480106f11929425599f) [BT\_LE\_CS\_TEST\_CS\_SYNC\_ANTENNA\_SELECTION\_ONE](group__bt__le__cs.md#gga782a500f611320a6f3feed9897ab8e16a054f9b7f51323480106f11929425599f) = [BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_ONE](hci__types_8h.md#a7fa26323384443ba9c5e635047b74f51),

[ 86](group__bt__le__cs.md#gga782a500f611320a6f3feed9897ab8e16aa1931403e835ab2e18982dd0f2a67803) [BT\_LE\_CS\_TEST\_CS\_SYNC\_ANTENNA\_SELECTION\_TWO](group__bt__le__cs.md#gga782a500f611320a6f3feed9897ab8e16aa1931403e835ab2e18982dd0f2a67803) = [BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_TWO](hci__types_8h.md#aa6d146c85e3148a2afb66023d94c2eeb),

[ 87](group__bt__le__cs.md#gga782a500f611320a6f3feed9897ab8e16aa059024bd3d90677ee00d4accd99f39c) [BT\_LE\_CS\_TEST\_CS\_SYNC\_ANTENNA\_SELECTION\_THREE](group__bt__le__cs.md#gga782a500f611320a6f3feed9897ab8e16aa059024bd3d90677ee00d4accd99f39c) = [BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_THREE](hci__types_8h.md#a8721a8f4670a8038d66d42adea061f57),

[ 88](group__bt__le__cs.md#gga782a500f611320a6f3feed9897ab8e16a678e1a8120f21f3707d4b9ea22bd8c47) [BT\_LE\_CS\_TEST\_CS\_SYNC\_ANTENNA\_SELECTION\_FOUR](group__bt__le__cs.md#gga782a500f611320a6f3feed9897ab8e16a678e1a8120f21f3707d4b9ea22bd8c47) = [BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_FOUR](hci__types_8h.md#af0d407f944831f8c85f91fb60f5bc618),

89};

90

[ 92](group__bt__le__cs.md#gaf34c59887e8a6da0560b6428733fe8d0)enum [bt\_le\_cs\_snr\_control](group__bt__le__cs.md#gaf34c59887e8a6da0560b6428733fe8d0) {

[ 93](group__bt__le__cs.md#ggaf34c59887e8a6da0560b6428733fe8d0a78af4f3bbf5adfc8ee6f9d459bb96e7d) [BT\_LE\_CS\_SNR\_CONTROL\_18dB](group__bt__le__cs.md#ggaf34c59887e8a6da0560b6428733fe8d0a78af4f3bbf5adfc8ee6f9d459bb96e7d) = [BT\_HCI\_OP\_LE\_CS\_SNR\_18](hci__types_8h.md#a96b13fb3b363a5436e1b9633f54bb248),

[ 94](group__bt__le__cs.md#ggaf34c59887e8a6da0560b6428733fe8d0a685a458547bda6af6c88626ee08c4110) [BT\_LE\_CS\_SNR\_CONTROL\_21dB](group__bt__le__cs.md#ggaf34c59887e8a6da0560b6428733fe8d0a685a458547bda6af6c88626ee08c4110) = [BT\_HCI\_OP\_LE\_CS\_SNR\_21](hci__types_8h.md#a4b93a8bceafd49d6ca65816924bb4230),

[ 95](group__bt__le__cs.md#ggaf34c59887e8a6da0560b6428733fe8d0a02394d7394f79a6e91a8f81070fdf82e) [BT\_LE\_CS\_SNR\_CONTROL\_24dB](group__bt__le__cs.md#ggaf34c59887e8a6da0560b6428733fe8d0a02394d7394f79a6e91a8f81070fdf82e) = [BT\_HCI\_OP\_LE\_CS\_SNR\_24](hci__types_8h.md#a135a4dc2f191d2a931b4270e00774cb2),

[ 96](group__bt__le__cs.md#ggaf34c59887e8a6da0560b6428733fe8d0a43a7b210424a2aa2830a07676d3499b8) [BT\_LE\_CS\_SNR\_CONTROL\_27dB](group__bt__le__cs.md#ggaf34c59887e8a6da0560b6428733fe8d0a43a7b210424a2aa2830a07676d3499b8) = [BT\_HCI\_OP\_LE\_CS\_SNR\_27](hci__types_8h.md#a52eb27d8f726a2ed6859149fcdf2355d),

[ 97](group__bt__le__cs.md#ggaf34c59887e8a6da0560b6428733fe8d0a18bb25e63782e9993a3853d929d58ee1) [BT\_LE\_CS\_SNR\_CONTROL\_30dB](group__bt__le__cs.md#ggaf34c59887e8a6da0560b6428733fe8d0a18bb25e63782e9993a3853d929d58ee1) = [BT\_HCI\_OP\_LE\_CS\_SNR\_30](hci__types_8h.md#a181c2d98b93bd18e9edc11a6f9535331),

[ 98](group__bt__le__cs.md#ggaf34c59887e8a6da0560b6428733fe8d0a1a5c531f590f14773b7ddc9b0ec8cae9) [BT\_LE\_CS\_SNR\_CONTROL\_NOT\_USED](group__bt__le__cs.md#ggaf34c59887e8a6da0560b6428733fe8d0a1a5c531f590f14773b7ddc9b0ec8cae9) = [BT\_HCI\_OP\_LE\_CS\_SNR\_NOT\_USED](hci__types_8h.md#a4aa2e02ce5110be3dc68a801bb583372),

99};

100

[ 102](group__bt__le__cs.md#gaf50910d51c69e216ef6eb22b5c0f2d28)enum [bt\_le\_cs\_test\_override\_3\_pm\_tone\_ext](group__bt__le__cs.md#gaf50910d51c69e216ef6eb22b5c0f2d28) {

[ 104](group__bt__le__cs.md#ggaf50910d51c69e216ef6eb22b5c0f2d28aa5f4fea24a1b27736cfc36c470a3a008) [BT\_LE\_CS\_TEST\_OVERRIDE\_3\_NO\_TONE\_EXT](group__bt__le__cs.md#ggaf50910d51c69e216ef6eb22b5c0f2d28aa5f4fea24a1b27736cfc36c470a3a008) = [BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_NONE](hci__types_8h.md#a9ed8967faa3ee3824433422709148330),

[ 106](group__bt__le__cs.md#ggaf50910d51c69e216ef6eb22b5c0f2d28aee2c022be115a4c865d5524795f2d039) [BT\_LE\_CS\_TEST\_OVERRIDE\_3\_INITIATOR\_TONE\_EXT\_ONLY](group__bt__le__cs.md#ggaf50910d51c69e216ef6eb22b5c0f2d28aee2c022be115a4c865d5524795f2d039) = [BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_INIT](hci__types_8h.md#a0513bf5ca6eb9f43a7e8cecaf943c4d7),

[ 108](group__bt__le__cs.md#ggaf50910d51c69e216ef6eb22b5c0f2d28ab504c3a24b36413ea2395bd579e5bba2) [BT\_LE\_CS\_TEST\_OVERRIDE\_3\_REFLECTOR\_TONE\_EXT\_ONLY](group__bt__le__cs.md#ggaf50910d51c69e216ef6eb22b5c0f2d28ab504c3a24b36413ea2395bd579e5bba2) = [BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_REFL](hci__types_8h.md#aa24ae1cf1501de66660051a4a62246df),

[ 110](group__bt__le__cs.md#ggaf50910d51c69e216ef6eb22b5c0f2d28ad2b323c3c54409545458c08fc6660cf4) [BT\_LE\_CS\_TEST\_OVERRIDE\_3\_INITIATOR\_AND\_REFLECTOR\_TONE\_EXT](group__bt__le__cs.md#ggaf50910d51c69e216ef6eb22b5c0f2d28ad2b323c3c54409545458c08fc6660cf4) =

111 [BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_BOTH](hci__types_8h.md#ad7a89a9365e20e4cd1e44bdb74ae7ecb),

[ 120](group__bt__le__cs.md#ggaf50910d51c69e216ef6eb22b5c0f2d28a9a691cb7b4a9cff799d848fc79cf40dd) [BT\_LE\_CS\_TEST\_OVERRIDE\_3\_REPETITIVE\_TONE\_EXT](group__bt__le__cs.md#ggaf50910d51c69e216ef6eb22b5c0f2d28a9a691cb7b4a9cff799d848fc79cf40dd) = [BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_REPEAT](hci__types_8h.md#a50fba6ab75b37ccf39452211ba05e896),

121};

122

[ 183](group__bt__le__cs.md#ga1ba4d7d919cb5c09469f8e8aa05bb04d)enum [bt\_le\_cs\_test\_override\_4\_tone\_antenna\_permutation](group__bt__le__cs.md#ga1ba4d7d919cb5c09469f8e8aa05bb04d) {

[ 184](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da72b3c5a4d07ae3c73e9bb131c725d17f) [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_00](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da72b3c5a4d07ae3c73e9bb131c725d17f) = [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_00](hci__types_8h.md#aa4ba4be270035da446389766b795c327),

[ 185](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da7aed472d8ed1b3fc84e89531134fc71c) [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_01](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da7aed472d8ed1b3fc84e89531134fc71c) = [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_01](hci__types_8h.md#aa0e9e2081d3cbbb60de9b6dcffe77239),

[ 186](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dab986f2c0c54de93cfdf5a5334aafffb2) [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_02](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dab986f2c0c54de93cfdf5a5334aafffb2) = [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_02](hci__types_8h.md#a762c5efa09e1fba989fdfb0bdcba9b9c),

[ 187](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da7731f27f1af37ba740764e9875d28482) [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_03](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da7731f27f1af37ba740764e9875d28482) = [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_03](hci__types_8h.md#a2cc7a5d5d2105b1a428703e274cc5388),

[ 188](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da3fe0da05e9c2493af3ea42a0c6cd4b17) [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_04](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da3fe0da05e9c2493af3ea42a0c6cd4b17) = [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_04](hci__types_8h.md#a03ffb0ffb8e98b26390575b153471bab),

[ 189](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04daa73b01369a29b4ea7de2aadb71efe699) [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_05](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04daa73b01369a29b4ea7de2aadb71efe699) = [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_05](hci__types_8h.md#adbd3820e0ffa5f99e27778217d477010),

[ 190](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dae4f815603cdffeb82711b994be2209dc) [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_06](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dae4f815603cdffeb82711b994be2209dc) = [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_06](hci__types_8h.md#a70607449d6bd6207783e319e77d63b16),

[ 191](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da28e1b78a9bb927c4d38047e2aed57a15) [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_07](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da28e1b78a9bb927c4d38047e2aed57a15) = [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_07](hci__types_8h.md#acc79a879ea527c2901a8b91dae58d0ed),

[ 192](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dab1cbcd7ceb33fb13b7d70b0dc671849c) [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_08](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dab1cbcd7ceb33fb13b7d70b0dc671849c) = [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_08](hci__types_8h.md#a9dfd88863d649182855edc8c268107d6),

[ 193](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dae7f0fedfabe1748f9918befedbc45944) [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_09](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dae7f0fedfabe1748f9918befedbc45944) = [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_09](hci__types_8h.md#ae5a27304aa1cefdfb26ae2cbf42532e3),

[ 194](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da2ac77dab1caf34f436075dab45cc4aea) [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_10](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da2ac77dab1caf34f436075dab45cc4aea) = [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_10](hci__types_8h.md#a0e9664c52808aa246218f92a4fb55516),

[ 195](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dad85a40214189a9c036c95d88fb752a0c) [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_11](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dad85a40214189a9c036c95d88fb752a0c) = [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_11](hci__types_8h.md#a8fbc80d91e4a1ae04c76cda189cd5d83),

[ 196](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da45f979b88a3d63c4f270d246c98f3b53) [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_12](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da45f979b88a3d63c4f270d246c98f3b53) = [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_12](hci__types_8h.md#a4c4a44bd33ebf97852e6640b0d510fdd),

[ 197](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da2b34111edb7b0b1412de7d4485cbc164) [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_13](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da2b34111edb7b0b1412de7d4485cbc164) = [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_13](hci__types_8h.md#a08690b2f762d24c34966b839a6d5e696),

[ 198](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da5ab31e2b89fef73d838ade33de5d770b) [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_14](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da5ab31e2b89fef73d838ade33de5d770b) = [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_14](hci__types_8h.md#ac2cd3ed1583f86af0480b8481cedca1e),

[ 199](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da144a6190783b1fbc5ccde1b9f0ec3581) [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_15](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da144a6190783b1fbc5ccde1b9f0ec3581) = [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_15](hci__types_8h.md#ab2b0745d98053775e9bf073e36ce5d78),

[ 200](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dae87750d18c24ddcece72919e107da671) [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_16](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dae87750d18c24ddcece72919e107da671) = [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_16](hci__types_8h.md#add2c42aa2583b93b0f98ac33ca61ca9d),

[ 201](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dabe494d770af056108d4679364a93acce) [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_17](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dabe494d770af056108d4679364a93acce) = [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_17](hci__types_8h.md#a08db476ea6516691baeb9007b553281d),

[ 202](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04daad5f0f4d2818f986472f8cca57b37ea9) [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_18](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04daad5f0f4d2818f986472f8cca57b37ea9) = [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_18](hci__types_8h.md#a9f0bf05cb0aac50e1df43397c3b913bc),

[ 203](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dac02f9fa05c0f35bb306fde66bc80ab21) [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_19](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dac02f9fa05c0f35bb306fde66bc80ab21) = [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_19](hci__types_8h.md#a5df817bdfefc4de0a1309cf71908a105),

[ 204](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dad355ee587eff65a2a2f80274fc6c5081) [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_20](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dad355ee587eff65a2a2f80274fc6c5081) = [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_20](hci__types_8h.md#ae64e5a409523b94ef1ce315ed49afed0),

[ 205](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da3cc8b9dfadae103bdbb0fb79c523f553) [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_21](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da3cc8b9dfadae103bdbb0fb79c523f553) = [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_21](hci__types_8h.md#a46f70b5096593956795cc381e33c4aa2),

[ 206](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dadf2778f065f696ad43ceca71aa6a8a80) [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_22](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dadf2778f065f696ad43ceca71aa6a8a80) = [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_22](hci__types_8h.md#abe9fa4621e9c004421170b0166ea14e1),

[ 207](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dac3a263bfe1f80c38647d6aeab42b12c3) [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_23](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dac3a263bfe1f80c38647d6aeab42b12c3) = [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_23](hci__types_8h.md#afc41ca64d03a7ed8ea82a641a0217436),

[ 211](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da2abd10e7d80703b3d849ad19d65af31f) [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_LOOP](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da2abd10e7d80703b3d849ad19d65af31f) =

212 [BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_LOOP](hci__types_8h.md#ac9d7cb5a339759b7e0c4ed150a487ca3),

213};

214

[ 216](group__bt__le__cs.md#gacb3f437225ad1d6320ee424c39ebc82a)enum [bt\_le\_cs\_test\_override\_7\_ss\_marker\_value](group__bt__le__cs.md#gacb3f437225ad1d6320ee424c39ebc82a) {

[ 217](group__bt__le__cs.md#ggacb3f437225ad1d6320ee424c39ebc82aa99a26684d34169d062150f61cb0ba889) [BT\_LE\_CS\_TEST\_OVERRIDE\_7\_SS\_MARKER\_VAL\_0011](group__bt__le__cs.md#ggacb3f437225ad1d6320ee424c39ebc82aa99a26684d34169d062150f61cb0ba889) = [BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_VAL\_0011](hci__types_8h.md#a45e1ff56f1a6dcc59b784905e4fc6726),

[ 218](group__bt__le__cs.md#ggacb3f437225ad1d6320ee424c39ebc82aa6b6bc126c5e2a97de33d6c83230ebb92) [BT\_LE\_CS\_TEST\_OVERRIDE\_7\_SS\_MARKER\_VAL\_1100](group__bt__le__cs.md#ggacb3f437225ad1d6320ee424c39ebc82aa6b6bc126c5e2a97de33d6c83230ebb92) = [BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_VAL\_1100](hci__types_8h.md#a5d3c206a5067ddc5a02a5d5e8c3eb7a3),

[ 220](group__bt__le__cs.md#ggacb3f437225ad1d6320ee424c39ebc82aa3a3078691c778d1c7a30fe9400bc5f0f) [BT\_LE\_CS\_TEST\_OVERRIDE\_7\_SS\_MARKER\_VAL\_LOOP](group__bt__le__cs.md#ggacb3f437225ad1d6320ee424c39ebc82aa3a3078691c778d1c7a30fe9400bc5f0f) = [BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_VAL\_LOOP](hci__types_8h.md#a24d2e56f620500905572e786f2523b0e),

221};

222

[ 224](group__bt__le__cs.md#ga731bbaa98dab7c88725fc64b66da62eb)enum [bt\_le\_cs\_test\_override\_8\_cs\_sync\_payload\_pattern](group__bt__le__cs.md#ga731bbaa98dab7c88725fc64b66da62eb) {

[ 226](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62eba3c8bc2a6858dc2d0de02b3b681a854a0) [BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_PRBS9](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62eba3c8bc2a6858dc2d0de02b3b681a854a0) = [BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_PRBS9](hci__types_8h.md#a4f922c5e0662adf8471686dfa9b719ec),

[ 228](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62eba109f2588e566b9651b67dbbf9583813c) [BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_11110000](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62eba109f2588e566b9651b67dbbf9583813c) = [BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_11110000](hci__types_8h.md#af20dfb1e245afc06a495179d700f126f),

[ 230](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62ebaef4b4455b236d70fae6a0138050d0835) [BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_10101010](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62ebaef4b4455b236d70fae6a0138050d0835) = [BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_10101010](hci__types_8h.md#ae133ef2939518d660df5322551157d47),

[ 232](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62eba1b910950b96ad0b47b0b235a2e8e45c8) [BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_PRBS15](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62eba1b910950b96ad0b47b0b235a2e8e45c8) = [BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_PRBS15](hci__types_8h.md#a92bc70a5ad7938a46ac9f2127f1bc2d9),

[ 234](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62ebabc520467cdbaaf34d0c815e0d62bd097) [BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_11111111](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62ebabc520467cdbaaf34d0c815e0d62bd097) = [BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_11111111](hci__types_8h.md#aa94eda86c6ffe85a65267f285dae5cb1),

[ 236](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62eba1b46b8b073ca599cb89d86b261fa4dd5) [BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_00000000](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62eba1b46b8b073ca599cb89d86b261fa4dd5) = [BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_00000000](hci__types_8h.md#a04a26b8600cac8c82247a7d51122f600),

[ 238](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62eba4f4ec5a6d46734e8c5801e9e79535b70) [BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_00001111](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62eba4f4ec5a6d46734e8c5801e9e79535b70) = [BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_00001111](hci__types_8h.md#abf19d511680005828add231d64e1e3f0),

[ 240](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62eba6c59258c52a5889e0b11aa0fb0f99bcb) [BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_01010101](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62eba6c59258c52a5889e0b11aa0fb0f99bcb) = [BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_01010101](hci__types_8h.md#a53f0ca5604489a38a1367736a5297b45),

[ 242](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62ebaf68334f70d91d587e906533ad544fef1) [BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_USER](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62ebaf68334f70d91d587e906533ad544fef1) = [BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_USER](hci__types_8h.md#a94007d8250c3524ad0b86745dbb74b3b),

243};

244

[ 246](structbt__le__cs__test__param.md)struct [bt\_le\_cs\_test\_param](structbt__le__cs__test__param.md) {

[ 248](structbt__le__cs__test__param.md#a93e487780ffb55c66708bd6c3b293456) enum [bt\_conn\_le\_cs\_main\_mode](group__bt__conn.md#ga133504278b6e01993ff36e96a238484f) [main\_mode](structbt__le__cs__test__param.md#a93e487780ffb55c66708bd6c3b293456);

[ 250](structbt__le__cs__test__param.md#a6b0ce9871c26b0a5c9c98a9339d234e1) enum [bt\_conn\_le\_cs\_sub\_mode](group__bt__conn.md#ga07c6f1248c9a6da0168bd3d398925daf) [sub\_mode](structbt__le__cs__test__param.md#a6b0ce9871c26b0a5c9c98a9339d234e1);

[ 255](structbt__le__cs__test__param.md#ac13c4390574bd9a540b632c3ee387870) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [main\_mode\_repetition](structbt__le__cs__test__param.md#ac13c4390574bd9a540b632c3ee387870);

[ 257](structbt__le__cs__test__param.md#a84f346fafa174ba8b2acf33ff3db72eb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mode\_0\_steps](structbt__le__cs__test__param.md#a84f346fafa174ba8b2acf33ff3db72eb);

[ 259](structbt__le__cs__test__param.md#a797dda190cc01447054ee4dc08f2a332) enum [bt\_conn\_le\_cs\_role](group__bt__conn.md#ga0e6f6d4fdbdfc3ed75fef4a95136076f) [role](structbt__le__cs__test__param.md#a797dda190cc01447054ee4dc08f2a332);

[ 261](structbt__le__cs__test__param.md#ab3af198a629e0fb082a177b6b482771a) enum [bt\_conn\_le\_cs\_rtt\_type](group__bt__conn.md#gaffd6abf9b92cc8d8463797a73b840f51) [rtt\_type](structbt__le__cs__test__param.md#ab3af198a629e0fb082a177b6b482771a);

[ 263](structbt__le__cs__test__param.md#a41c70c829d16299eb7d25029ddad01bb) enum [bt\_conn\_le\_cs\_sync\_phy](group__bt__conn.md#gaadbf6a4dba28aec90ea07b7da634e1bb) [cs\_sync\_phy](structbt__le__cs__test__param.md#a41c70c829d16299eb7d25029ddad01bb);

[ 265](structbt__le__cs__test__param.md#af26b66e0a28e4f3c6fce0dd5ad8a7606) enum [bt\_le\_cs\_test\_cs\_sync\_antenna\_selection](group__bt__le__cs.md#ga782a500f611320a6f3feed9897ab8e16) [cs\_sync\_antenna\_selection](structbt__le__cs__test__param.md#af26b66e0a28e4f3c6fce0dd5ad8a7606);

[ 270](structbt__le__cs__test__param.md#a78aeb8d6e7ac9565ea19a1ffd51ceb6a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [subevent\_len](structbt__le__cs__test__param.md#a78aeb8d6e7ac9565ea19a1ffd51ceb6a);

[ 275](structbt__le__cs__test__param.md#a1bff7f98cb72a9f73b0499b8fc89d262) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [subevent\_interval](structbt__le__cs__test__param.md#a1bff7f98cb72a9f73b0499b8fc89d262);

[ 280](structbt__le__cs__test__param.md#aaf09c64fcfa1a0a4257d805ad9b49d56) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_num\_subevents](structbt__le__cs__test__param.md#aaf09c64fcfa1a0a4257d805ad9b49d56);

[ 292](structbt__le__cs__test__param.md#a5951fa7f55752905a0180e8389c3d245) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [transmit\_power\_level](structbt__le__cs__test__param.md#a5951fa7f55752905a0180e8389c3d245);

[ 305](structbt__le__cs__test__param.md#a02437a42f0c3e8563d1600b02e7ca517) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [t\_ip1\_time](structbt__le__cs__test__param.md#a02437a42f0c3e8563d1600b02e7ca517);

[ 318](structbt__le__cs__test__param.md#a1ce5f3400442ebdd8cf45f9db6367e58) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [t\_ip2\_time](structbt__le__cs__test__param.md#a1ce5f3400442ebdd8cf45f9db6367e58);

[ 333](structbt__le__cs__test__param.md#a8a2d1540e35d194729df373c79f9eaf2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [t\_fcs\_time](structbt__le__cs__test__param.md#a8a2d1540e35d194729df373c79f9eaf2);

[ 341](structbt__le__cs__test__param.md#a8eb7e6fcf4431513404ac5f75da401a9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [t\_pm\_time](structbt__le__cs__test__param.md#a8eb7e6fcf4431513404ac5f75da401a9);

[ 351](structbt__le__cs__test__param.md#a94c3e1dcfb7290b61784c5dcd6a67531) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [t\_sw\_time](structbt__le__cs__test__param.md#a94c3e1dcfb7290b61784c5dcd6a67531);

[ 355](structbt__le__cs__test__param.md#aff02c121f9c8ae63a137dbb19bf4acd2) enum [bt\_conn\_le\_cs\_tone\_antenna\_config\_selection](group__bt__conn.md#gab7acdbdf273fc760799cf0d8cf71591c) [tone\_antenna\_config\_selection](structbt__le__cs__test__param.md#aff02c121f9c8ae63a137dbb19bf4acd2);

[ 357](structbt__le__cs__test__param.md#aa58cf62583c83e32362216bc060a9a8e) enum [bt\_le\_cs\_snr\_control](group__bt__le__cs.md#gaf34c59887e8a6da0560b6428733fe8d0) [initiator\_snr\_control](structbt__le__cs__test__param.md#aa58cf62583c83e32362216bc060a9a8e);

[ 359](structbt__le__cs__test__param.md#aaa7305e11ee3e22b10b4ceb3c743d4e9) enum [bt\_le\_cs\_snr\_control](group__bt__le__cs.md#gaf34c59887e8a6da0560b6428733fe8d0) [reflector\_snr\_control](structbt__le__cs__test__param.md#aaa7305e11ee3e22b10b4ceb3c743d4e9);

[ 361](structbt__le__cs__test__param.md#a3ba9bfaa63f144af3117233e7a7e3d3d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [drbg\_nonce](structbt__le__cs__test__param.md#a3ba9bfaa63f144af3117233e7a7e3d3d);

362

[ 382](structbt__le__cs__test__param.md#a0ac14a9e1055870ee33ef83e54c1a248) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [override\_config](structbt__le__cs__test__param.md#a0ac14a9e1055870ee33ef83e54c1a248);

383

385 struct {

[ 389](structbt__le__cs__test__param.md#a5f0cefe32070be29bc918ff4f7a3a46d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel\_map\_repetition](structbt__le__cs__test__param.md#a5f0cefe32070be29bc918ff4f7a3a46d);

390 union {

391 struct {

[ 392](structbt__le__cs__test__param.md#acb2eed00edb4cac80ce097b241d8e1c8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_channels](structbt__le__cs__test__param.md#acb2eed00edb4cac80ce097b241d8e1c8);

[ 393](structbt__le__cs__test__param.md#aeb66cc7b6744cd1709d6199d2ae2dc98) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[channels](structbt__le__cs__test__param.md#aeb66cc7b6744cd1709d6199d2ae2dc98);

[ 394](structbt__le__cs__test__param.md#a7eb22e2e410701b2baa5f7d9d7123721) } [set](structbt__le__cs__test__param.md#a7eb22e2e410701b2baa5f7d9d7123721);

395 struct {

[ 396](structbt__le__cs__test__param.md#a6092db75cfc8143d2e308fce87c18dfe) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel\_map](structbt__le__cs__test__param.md#a6092db75cfc8143d2e308fce87c18dfe)[10];

[ 397](structbt__le__cs__test__param.md#ad2f4775d56677c63ef1ff71c0d3bc08a) enum [bt\_conn\_le\_cs\_chsel\_type](group__bt__conn.md#ga34e4837a77c7afd6999095985ddad4f0) [channel\_selection\_type](structbt__le__cs__test__param.md#ad2f4775d56677c63ef1ff71c0d3bc08a);

[ 398](structbt__le__cs__test__param.md#a656de42b2afb3d9c53899d3c4d6f3a88) enum [bt\_conn\_le\_cs\_ch3c\_shape](group__bt__conn.md#gaf2331ec1f1222de51fc4f30566e1c52b) [ch3c\_shape](structbt__le__cs__test__param.md#a656de42b2afb3d9c53899d3c4d6f3a88);

[ 399](structbt__le__cs__test__param.md#aac51c328149cce847057b913f2733198) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ch3c\_jump](structbt__le__cs__test__param.md#aac51c328149cce847057b913f2733198);

[ 400](structbt__le__cs__test__param.md#a1c241926b6d1c57c1bde197c1fb37251) } [not\_set](structbt__le__cs__test__param.md#a1c241926b6d1c57c1bde197c1fb37251);

401 };

[ 402](structbt__le__cs__test__param.md#a802545d0c7f560166250d4ad585a7d80) } [override\_config\_0](structbt__le__cs__test__param.md#a802545d0c7f560166250d4ad585a7d80);

403

405 struct {

[ 406](structbt__le__cs__test__param.md#a1e92044ae3538cb71a9192ebcbd8c884) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [main\_mode\_steps](structbt__le__cs__test__param.md#a1e92044ae3538cb71a9192ebcbd8c884);

[ 407](structbt__le__cs__test__param.md#a63e8e44842b894bee57ffdcdee4f2cd0) } [override\_config\_2](structbt__le__cs__test__param.md#a63e8e44842b894bee57ffdcdee4f2cd0);

408

410 struct {

[ 411](structbt__le__cs__test__param.md#a905f49912a99c105ce4087c4d3327deb) enum [bt\_le\_cs\_test\_override\_3\_pm\_tone\_ext](group__bt__le__cs.md#gaf50910d51c69e216ef6eb22b5c0f2d28) [t\_pm\_tone\_ext](structbt__le__cs__test__param.md#a905f49912a99c105ce4087c4d3327deb);

[ 412](structbt__le__cs__test__param.md#afe036f2effcb41c9a4d888592916c329) } [override\_config\_3](structbt__le__cs__test__param.md#afe036f2effcb41c9a4d888592916c329);

413

415 struct {

[ 416](structbt__le__cs__test__param.md#a22e2ec51e87887b74c8251fa004a4497) enum [bt\_le\_cs\_test\_override\_4\_tone\_antenna\_permutation](group__bt__le__cs.md#ga1ba4d7d919cb5c09469f8e8aa05bb04d) [tone\_antenna\_permutation](structbt__le__cs__test__param.md#a22e2ec51e87887b74c8251fa004a4497);

[ 417](structbt__le__cs__test__param.md#a40671e60cf8e1ff16e7389f6a24c9bb7) } [override\_config\_4](structbt__le__cs__test__param.md#a40671e60cf8e1ff16e7389f6a24c9bb7);

418

420 struct {

[ 422](structbt__le__cs__test__param.md#a355cdcf57dcafdfdc98959ec6b742cc1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cs\_sync\_aa\_initiator](structbt__le__cs__test__param.md#a355cdcf57dcafdfdc98959ec6b742cc1);

[ 424](structbt__le__cs__test__param.md#ad8ce97db93b0fbc267552db64491483a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cs\_sync\_aa\_reflector](structbt__le__cs__test__param.md#ad8ce97db93b0fbc267552db64491483a);

[ 425](structbt__le__cs__test__param.md#a9bba99348c662adad1f16194409b2ae1) } [override\_config\_5](structbt__le__cs__test__param.md#a9bba99348c662adad1f16194409b2ae1);

426

428 struct {

[ 433](structbt__le__cs__test__param.md#a1404de78072df4910a1823eadcb78cd1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ss\_marker1\_position](structbt__le__cs__test__param.md#a1404de78072df4910a1823eadcb78cd1);

[ 442](structbt__le__cs__test__param.md#a093b0425d87266c9cb31c8dc209477ff) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ss\_marker2\_position](structbt__le__cs__test__param.md#a093b0425d87266c9cb31c8dc209477ff);

[ 443](structbt__le__cs__test__param.md#af4f16878d530ec19294673756e7b6358) } [override\_config\_6](structbt__le__cs__test__param.md#af4f16878d530ec19294673756e7b6358);

444

446 struct {

[ 448](structbt__le__cs__test__param.md#aad705c92184ed8f1577bac68dc810373) enum [bt\_le\_cs\_test\_override\_7\_ss\_marker\_value](group__bt__le__cs.md#gacb3f437225ad1d6320ee424c39ebc82a) [ss\_marker\_value](structbt__le__cs__test__param.md#aad705c92184ed8f1577bac68dc810373);

[ 449](structbt__le__cs__test__param.md#a9a2763c3062b2ee4d8a1d70393ed2aa2) } [override\_config\_7](structbt__le__cs__test__param.md#a9a2763c3062b2ee4d8a1d70393ed2aa2);

450

452 struct {

[ 454](structbt__le__cs__test__param.md#ace81aeaeefc788ccf6bb1b6c491ff0b2) enum [bt\_le\_cs\_test\_override\_8\_cs\_sync\_payload\_pattern](group__bt__le__cs.md#ga731bbaa98dab7c88725fc64b66da62eb) [cs\_sync\_payload\_pattern](structbt__le__cs__test__param.md#ace81aeaeefc788ccf6bb1b6c491ff0b2);

[ 464](structbt__le__cs__test__param.md#a79ce15e5034572a4b5015240b7db4de5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cs\_sync\_user\_payload](structbt__le__cs__test__param.md#a79ce15e5034572a4b5015240b7db4de5)[16];

[ 465](structbt__le__cs__test__param.md#afb85cec959d8bd59b560828af14dbced) } [override\_config\_8](structbt__le__cs__test__param.md#afb85cec959d8bd59b560828af14dbced);

466};

467

[ 469](group__bt__le__cs.md#ga22822b2dd21d64c8c64a66f2b5dee9b1)enum [bt\_le\_cs\_create\_config\_context](group__bt__le__cs.md#ga22822b2dd21d64c8c64a66f2b5dee9b1) {

[ 471](group__bt__le__cs.md#gga22822b2dd21d64c8c64a66f2b5dee9b1adb8a8af222fed7262bdb57bc4f18a706) [BT\_LE\_CS\_CREATE\_CONFIG\_CONTEXT\_LOCAL\_ONLY](group__bt__le__cs.md#gga22822b2dd21d64c8c64a66f2b5dee9b1adb8a8af222fed7262bdb57bc4f18a706),

[ 475](group__bt__le__cs.md#gga22822b2dd21d64c8c64a66f2b5dee9b1ae5107dfa011451ecaa404906fabc41e4) [BT\_LE\_CS\_CREATE\_CONFIG\_CONTEXT\_LOCAL\_AND\_REMOTE](group__bt__le__cs.md#gga22822b2dd21d64c8c64a66f2b5dee9b1ae5107dfa011451ecaa404906fabc41e4)

476};

477

[ 479](structbt__le__cs__create__config__params.md)struct [bt\_le\_cs\_create\_config\_params](structbt__le__cs__create__config__params.md) {

[ 481](structbt__le__cs__create__config__params.md#a59615f8de0a39f124ae3d2e2876ecc30) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structbt__le__cs__create__config__params.md#a59615f8de0a39f124ae3d2e2876ecc30);

[ 483](structbt__le__cs__create__config__params.md#a2bdbff2e20106e4a6925a8018d491a9c) enum [bt\_conn\_le\_cs\_main\_mode](group__bt__conn.md#ga133504278b6e01993ff36e96a238484f) [main\_mode\_type](structbt__le__cs__create__config__params.md#a2bdbff2e20106e4a6925a8018d491a9c);

[ 485](structbt__le__cs__create__config__params.md#a1bec59da1343bbc70a575d6dbde56309) enum [bt\_conn\_le\_cs\_sub\_mode](group__bt__conn.md#ga07c6f1248c9a6da0168bd3d398925daf) [sub\_mode\_type](structbt__le__cs__create__config__params.md#a1bec59da1343bbc70a575d6dbde56309);

[ 487](structbt__le__cs__create__config__params.md#ae7ff30dcfcb4460dac48c139bdac0f75) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [min\_main\_mode\_steps](structbt__le__cs__create__config__params.md#ae7ff30dcfcb4460dac48c139bdac0f75);

[ 489](structbt__le__cs__create__config__params.md#aa8951ab286210ab87c460ed315d091bf) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_main\_mode\_steps](structbt__le__cs__create__config__params.md#aa8951ab286210ab87c460ed315d091bf);

[ 494](structbt__le__cs__create__config__params.md#a9a7c56e1d04d634aaab4f3b81c506be3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [main\_mode\_repetition](structbt__le__cs__create__config__params.md#a9a7c56e1d04d634aaab4f3b81c506be3);

[ 496](structbt__le__cs__create__config__params.md#af824b6b56fba318588ebcf707d6e7a24) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mode\_0\_steps](structbt__le__cs__create__config__params.md#af824b6b56fba318588ebcf707d6e7a24);

[ 498](structbt__le__cs__create__config__params.md#a2581694b25afa7903786c7848c133c38) enum [bt\_conn\_le\_cs\_role](group__bt__conn.md#ga0e6f6d4fdbdfc3ed75fef4a95136076f) [role](structbt__le__cs__create__config__params.md#a2581694b25afa7903786c7848c133c38);

[ 500](structbt__le__cs__create__config__params.md#a0a34afa329e88af8fcbcff1a8b0a1bcd) enum [bt\_conn\_le\_cs\_rtt\_type](group__bt__conn.md#gaffd6abf9b92cc8d8463797a73b840f51) [rtt\_type](structbt__le__cs__create__config__params.md#a0a34afa329e88af8fcbcff1a8b0a1bcd);

[ 502](structbt__le__cs__create__config__params.md#a4329d967361e330077ca9064bdc3fc5f) enum [bt\_conn\_le\_cs\_sync\_phy](group__bt__conn.md#gaadbf6a4dba28aec90ea07b7da634e1bb) [cs\_sync\_phy](structbt__le__cs__create__config__params.md#a4329d967361e330077ca9064bdc3fc5f);

[ 506](structbt__le__cs__create__config__params.md#a6eff424679cb98ba2d749636618744ce) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel\_map\_repetition](structbt__le__cs__create__config__params.md#a6eff424679cb98ba2d749636618744ce);

[ 508](structbt__le__cs__create__config__params.md#ac83ef36301b0d990cb3a7cf1e630c957) enum [bt\_conn\_le\_cs\_chsel\_type](group__bt__conn.md#ga34e4837a77c7afd6999095985ddad4f0) [channel\_selection\_type](structbt__le__cs__create__config__params.md#ac83ef36301b0d990cb3a7cf1e630c957);

[ 510](structbt__le__cs__create__config__params.md#a14ac5115fa91bc7ed4a4aa7a0786f81f) enum [bt\_conn\_le\_cs\_ch3c\_shape](group__bt__conn.md#gaf2331ec1f1222de51fc4f30566e1c52b) [ch3c\_shape](structbt__le__cs__create__config__params.md#a14ac5115fa91bc7ed4a4aa7a0786f81f);

[ 512](structbt__le__cs__create__config__params.md#ad0ea92b48ac4e9753ee422f2286c1ded) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ch3c\_jump](structbt__le__cs__create__config__params.md#ad0ea92b48ac4e9753ee422f2286c1ded);

[ 518](structbt__le__cs__create__config__params.md#adcf6276f58bd19ec61800160979fd472) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel\_map](structbt__le__cs__create__config__params.md#adcf6276f58bd19ec61800160979fd472)[10];

519};

520

[ 522](structbt__le__cs__test__cb.md)struct [bt\_le\_cs\_test\_cb](structbt__le__cs__test__cb.md) {

[ 527](structbt__le__cs__test__cb.md#a2a3ca580a3c3d55aa2f2323a318827f9) void (\*[le\_cs\_test\_subevent\_data\_available](structbt__le__cs__test__cb.md#a2a3ca580a3c3d55aa2f2323a318827f9))(struct [bt\_conn\_le\_cs\_subevent\_result](structbt__conn__le__cs__subevent__result.md) \*data);

[ 529](structbt__le__cs__test__cb.md#a7da5731fb2ae9e7fc3cece78a7468663) void (\*[le\_cs\_test\_end\_complete](structbt__le__cs__test__cb.md#a7da5731fb2ae9e7fc3cece78a7468663))(void);

530};

531

[ 533](structbt__le__cs__subevent__step.md)struct [bt\_le\_cs\_subevent\_step](structbt__le__cs__subevent__step.md) {

[ 535](structbt__le__cs__subevent__step.md#a82103efe7c897abdf5bbb9c0a23cfba4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mode](structbt__le__cs__subevent__step.md#a82103efe7c897abdf5bbb9c0a23cfba4);

[ 537](structbt__le__cs__subevent__step.md#a54b47ddae09d8ab3f57124f71c4efbca) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel](structbt__le__cs__subevent__step.md#a54b47ddae09d8ab3f57124f71c4efbca);

[ 539](structbt__le__cs__subevent__step.md#a32d2c13c5513220cf1cd7a13fb18c501) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_len](structbt__le__cs__subevent__step.md#a32d2c13c5513220cf1cd7a13fb18c501);

[ 541](structbt__le__cs__subevent__step.md#a46494728a82c6d50f6acd8f88e1a0842) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structbt__le__cs__subevent__step.md#a46494728a82c6d50f6acd8f88e1a0842);

542};

543

[ 545](structbt__le__cs__iq__sample.md)struct [bt\_le\_cs\_iq\_sample](structbt__le__cs__iq__sample.md) {

[ 546](structbt__le__cs__iq__sample.md#ab25db98b90a2f3c9a20a40efb1050c29) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [i](structbt__le__cs__iq__sample.md#ab25db98b90a2f3c9a20a40efb1050c29);

[ 547](structbt__le__cs__iq__sample.md#a33dd41ba3b8027035bde1610c4a77a98) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [q](structbt__le__cs__iq__sample.md#a33dd41ba3b8027035bde1610c4a77a98);

548};

549

[ 560](group__bt__le__cs.md#gaf99d82194bbcc471c3de2094b39a2201)struct [bt\_le\_cs\_iq\_sample](structbt__le__cs__iq__sample.md) [bt\_le\_cs\_parse\_pct](group__bt__le__cs.md#gaf99d82194bbcc471c3de2094b39a2201)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pct[3]);

561

[ 569](group__bt__le__cs.md#gaa979dc080cf277a2382b6ba77f8a1c09)void [bt\_le\_cs\_set\_valid\_chmap\_bits](group__bt__le__cs.md#gaa979dc080cf277a2382b6ba77f8a1c09)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel\_map[10]);

570

[ 582](group__bt__le__cs.md#gadb3afd94cd11d035cfe34c6a63b37b19)int [bt\_le\_cs\_read\_remote\_supported\_capabilities](group__bt__le__cs.md#gadb3afd94cd11d035cfe34c6a63b37b19)(struct bt\_conn \*conn);

583

[ 596](group__bt__le__cs.md#ga6ee9b8fa52b96dce41b1c879865fa938)int [bt\_le\_cs\_set\_default\_settings](group__bt__le__cs.md#ga6ee9b8fa52b96dce41b1c879865fa938)(struct bt\_conn \*conn,

597 const struct [bt\_le\_cs\_set\_default\_settings\_param](structbt__le__cs__set__default__settings__param.md) \*params);

598

[ 610](group__bt__le__cs.md#ga127034536a98743d359c749fe7c79dba)int [bt\_le\_cs\_read\_remote\_fae\_table](group__bt__le__cs.md#ga127034536a98743d359c749fe7c79dba)(struct bt\_conn \*conn);

611

[ 623](group__bt__le__cs.md#gaf03c4ed5c7e179ee3b374efa857188e2)int [bt\_le\_cs\_test\_cb\_register](group__bt__le__cs.md#gaf03c4ed5c7e179ee3b374efa857188e2)(struct [bt\_le\_cs\_test\_cb](structbt__le__cs__test__cb.md) cs\_test\_cb);

624

[ 645](group__bt__le__cs.md#gada91ff7c7a82620d77bf78781ebea356)int [bt\_le\_cs\_start\_test](group__bt__le__cs.md#gada91ff7c7a82620d77bf78781ebea356)(const struct [bt\_le\_cs\_test\_param](structbt__le__cs__test__param.md) \*params);

646

[ 661](group__bt__le__cs.md#ga27bae87f9769a2d5802c57adfa201b23)int [bt\_le\_cs\_create\_config](group__bt__le__cs.md#ga27bae87f9769a2d5802c57adfa201b23)(struct bt\_conn \*conn, struct [bt\_le\_cs\_create\_config\_params](structbt__le__cs__create__config__params.md) \*params,

662 enum [bt\_le\_cs\_create\_config\_context](group__bt__le__cs.md#ga22822b2dd21d64c8c64a66f2b5dee9b1) context);

663

[ 676](group__bt__le__cs.md#ga2a27b80e72ff2bfe986b3cbe11f225f3)int [bt\_le\_cs\_remove\_config](group__bt__le__cs.md#ga2a27b80e72ff2bfe986b3cbe11f225f3)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) config\_id);

677

[ 689](group__bt__le__cs.md#ga4742baeb1eb46969233f787344cb5e11)int [bt\_le\_cs\_stop\_test](group__bt__le__cs.md#ga4742baeb1eb46969233f787344cb5e11)(void);

690

[ 705](group__bt__le__cs.md#gadcd85f3799f4219a01e84fc281ff1a31)void [bt\_le\_cs\_step\_data\_parse](group__bt__le__cs.md#gadcd85f3799f4219a01e84fc281ff1a31)(struct [net\_buf\_simple](structnet__buf__simple.md) \*step\_data\_buf,

706 bool (\*func)(struct [bt\_le\_cs\_subevent\_step](structbt__le__cs__subevent__step.md) \*step, void \*user\_data),

707 void \*user\_data);

708

[ 721](group__bt__le__cs.md#ga346a46dc3321c5bab034904bf09aa4e3)int [bt\_le\_cs\_security\_enable](group__bt__le__cs.md#ga346a46dc3321c5bab034904bf09aa4e3)(struct bt\_conn \*conn);

722

[ 723](structbt__le__cs__procedure__enable__param.md)struct [bt\_le\_cs\_procedure\_enable\_param](structbt__le__cs__procedure__enable__param.md) {

[ 724](structbt__le__cs__procedure__enable__param.md#aa776933876805f8e7074abbf47634ea4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [config\_id](structbt__le__cs__procedure__enable__param.md#aa776933876805f8e7074abbf47634ea4);

[ 725](structbt__le__cs__procedure__enable__param.md#a01416dc5ed8f0315f050f76ce8ca3034) enum [bt\_conn\_le\_cs\_procedure\_enable\_state](group__bt__conn.md#gaf3653de72793f775e33fd9eb04c3e7a2) [enable](structbt__le__cs__procedure__enable__param.md#a01416dc5ed8f0315f050f76ce8ca3034);

726};

727

[ 741](group__bt__le__cs.md#ga2b6f3c3795b5eeb424542c1858f84cbc)int [bt\_le\_cs\_procedure\_enable](group__bt__le__cs.md#ga2b6f3c3795b5eeb424542c1858f84cbc)(struct bt\_conn \*conn,

742 const struct [bt\_le\_cs\_procedure\_enable\_param](structbt__le__cs__procedure__enable__param.md) \*params);

743

[ 744](group__bt__le__cs.md#ga9e008daa9c0c1702aa3b4479e7a37ca4)enum [bt\_le\_cs\_procedure\_phy](group__bt__le__cs.md#ga9e008daa9c0c1702aa3b4479e7a37ca4) {

[ 745](group__bt__le__cs.md#gga9e008daa9c0c1702aa3b4479e7a37ca4aa1dcc1e15aac59898c0a6c229593a76b) [BT\_LE\_CS\_PROCEDURE\_PHY\_1M](group__bt__le__cs.md#gga9e008daa9c0c1702aa3b4479e7a37ca4aa1dcc1e15aac59898c0a6c229593a76b) = [BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_1M](hci__types_8h.md#a3a8f1c94f40696f18e18810f736497e3),

[ 746](group__bt__le__cs.md#gga9e008daa9c0c1702aa3b4479e7a37ca4a072649a66bf1260ce37bd16fc7a9185d) [BT\_LE\_CS\_PROCEDURE\_PHY\_2M](group__bt__le__cs.md#gga9e008daa9c0c1702aa3b4479e7a37ca4a072649a66bf1260ce37bd16fc7a9185d) = [BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_2M](hci__types_8h.md#a016f68a621de8d332f3073df4faf1702),

[ 747](group__bt__le__cs.md#gga9e008daa9c0c1702aa3b4479e7a37ca4a1ceb33afa661774e1077caced63bf263) [BT\_LE\_CS\_PROCEDURE\_PHY\_CODED\_S8](group__bt__le__cs.md#gga9e008daa9c0c1702aa3b4479e7a37ca4a1ceb33afa661774e1077caced63bf263) = [BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_CODED\_S8](hci__types_8h.md#a2543f9fa20db642fb8b47b949c50af6a),

[ 748](group__bt__le__cs.md#gga9e008daa9c0c1702aa3b4479e7a37ca4a5370237bdbceb37a631425f472ddc322) [BT\_LE\_CS\_PROCEDURE\_PHY\_CODED\_S2](group__bt__le__cs.md#gga9e008daa9c0c1702aa3b4479e7a37ca4a5370237bdbceb37a631425f472ddc322) = [BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_CODED\_S2](hci__types_8h.md#a776a14d8e7fdca584475f26b441c8bfb),

749};

750

[ 751](group__bt__le__cs.md#gaf278a44ad602ce7e365ac0d71bcc48b4)#define BT\_LE\_CS\_PROCEDURE\_PREFERRED\_PEER\_ANTENNA\_1 BIT(0)

[ 752](group__bt__le__cs.md#ga5ff36f6e97668a9d1b6ccd39492c68f7)#define BT\_LE\_CS\_PROCEDURE\_PREFERRED\_PEER\_ANTENNA\_2 BIT(1)

[ 753](group__bt__le__cs.md#ga66ea3f214385c395e5f14ca80a0655b0)#define BT\_LE\_CS\_PROCEDURE\_PREFERRED\_PEER\_ANTENNA\_3 BIT(2)

[ 754](group__bt__le__cs.md#gaa2c1c3d5e451df7ec58b4c8d3dedcf9a)#define BT\_LE\_CS\_PROCEDURE\_PREFERRED\_PEER\_ANTENNA\_4 BIT(3)

755

[ 756](structbt__le__cs__set__procedure__parameters__param.md)struct [bt\_le\_cs\_set\_procedure\_parameters\_param](structbt__le__cs__set__procedure__parameters__param.md) {

757 /\* The ID associated with the desired configuration (0 to 3) \*/

[ 758](structbt__le__cs__set__procedure__parameters__param.md#a03e8b91ccc78b02faed1864e6b4ad885) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [config\_id](structbt__le__cs__set__procedure__parameters__param.md#a03e8b91ccc78b02faed1864e6b4ad885);

759

760 /\* Max. duration for each CS procedure, where T = N \* 0.625 ms (0x0001 to 0xFFFF) \*/

[ 761](structbt__le__cs__set__procedure__parameters__param.md#a9b28e4b6f887201ca7f2188b07d37e4c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_procedure\_len](structbt__le__cs__set__procedure__parameters__param.md#a9b28e4b6f887201ca7f2188b07d37e4c);

762

763 /\* Min. number of connection events between consecutive CS procedures (0x0001 to 0xFFFF) \*/

[ 764](structbt__le__cs__set__procedure__parameters__param.md#a967adc0e39da8e3ff96b998f3807542e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [min\_procedure\_interval](structbt__le__cs__set__procedure__parameters__param.md#a967adc0e39da8e3ff96b998f3807542e);

765

766 /\* Max. number of connection events between consecutive CS procedures (0x0001 to 0xFFFF) \*/

[ 767](structbt__le__cs__set__procedure__parameters__param.md#ac48eb6d0021c676738f17437fdcbc3e8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_procedure\_interval](structbt__le__cs__set__procedure__parameters__param.md#ac48eb6d0021c676738f17437fdcbc3e8);

768

769 /\* Max. number of procedures to be scheduled (0x0000 for no limit; otherwise 0x0001

770 \* to 0xFFFF)

771 \*/

[ 772](structbt__le__cs__set__procedure__parameters__param.md#a7a00113e7849b604efc38d904fce0389) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_procedure\_count](structbt__le__cs__set__procedure__parameters__param.md#a7a00113e7849b604efc38d904fce0389);

773

774 /\* Min. suggested duration for each CS subevent in microseconds (1250 us to 4 s) \*/

[ 775](structbt__le__cs__set__procedure__parameters__param.md#ab45195cbf8021c861384ead2cedae8da) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [min\_subevent\_len](structbt__le__cs__set__procedure__parameters__param.md#ab45195cbf8021c861384ead2cedae8da);

776

777 /\* Max. suggested duration for each CS subevent in microseconds (1250 us to 4 s) \*/

[ 778](structbt__le__cs__set__procedure__parameters__param.md#a0166c72225d70e7c1afc9cf9be613835) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_subevent\_len](structbt__le__cs__set__procedure__parameters__param.md#a0166c72225d70e7c1afc9cf9be613835);

779

780 /\* Antenna configuration index \*/

[ 781](structbt__le__cs__set__procedure__parameters__param.md#a3f7c838bcfb9c0e3d7ad803aefdc33c4) enum [bt\_conn\_le\_cs\_tone\_antenna\_config\_selection](group__bt__conn.md#gab7acdbdf273fc760799cf0d8cf71591c) [tone\_antenna\_config\_selection](structbt__le__cs__set__procedure__parameters__param.md#a3f7c838bcfb9c0e3d7ad803aefdc33c4);

782

783 /\* Phy \*/

[ 784](structbt__le__cs__set__procedure__parameters__param.md#a7f42131c93874c0be297752d8103b585) enum [bt\_le\_cs\_procedure\_phy](group__bt__le__cs.md#ga9e008daa9c0c1702aa3b4479e7a37ca4) [phy](structbt__le__cs__set__procedure__parameters__param.md#a7f42131c93874c0be297752d8103b585);

785

786 /\* Transmit power delta, in signed dB, to indicate the recommended difference between the

787 \* remote device's power level for the CS tones and RTT packets and the existing power

788 \* level for the Phy indicated by the Phy parameter (0x80 for no recommendation)

789 \*/

[ 790](structbt__le__cs__set__procedure__parameters__param.md#abb995a318cf74ff7cbd8882ddfb155cc) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power\_delta](structbt__le__cs__set__procedure__parameters__param.md#abb995a318cf74ff7cbd8882ddfb155cc);

791

792 /\* Preferred peer antenna (Bitmask of BT\_LE\_CS\_PROCEDURE\_PREFERRED\_PEER\_ANTENNA\_\*) \*/

[ 793](structbt__le__cs__set__procedure__parameters__param.md#aa1158161ee5e49217ad6a85b6c92d993) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [preferred\_peer\_antenna](structbt__le__cs__set__procedure__parameters__param.md#aa1158161ee5e49217ad6a85b6c92d993);

794

795 /\* Initiator SNR control adjustment \*/

[ 796](structbt__le__cs__set__procedure__parameters__param.md#a2fb81c447beb1238cb88610589458816) enum [bt\_le\_cs\_snr\_control](group__bt__le__cs.md#gaf34c59887e8a6da0560b6428733fe8d0) [snr\_control\_initiator](structbt__le__cs__set__procedure__parameters__param.md#a2fb81c447beb1238cb88610589458816);

797

798 /\* Reflector SNR control adjustment \*/

[ 799](structbt__le__cs__set__procedure__parameters__param.md#ab053facc218a6566a31e33d0831d385f) enum [bt\_le\_cs\_snr\_control](group__bt__le__cs.md#gaf34c59887e8a6da0560b6428733fe8d0) [snr\_control\_reflector](structbt__le__cs__set__procedure__parameters__param.md#ab053facc218a6566a31e33d0831d385f);

800};

801

[ 814](group__bt__le__cs.md#gad6e0fb9c7f92678598d9780b78710961)int [bt\_le\_cs\_set\_procedure\_parameters](group__bt__le__cs.md#gad6e0fb9c7f92678598d9780b78710961)(struct bt\_conn \*conn,

815 const struct [bt\_le\_cs\_set\_procedure\_parameters\_param](structbt__le__cs__set__procedure__parameters__param.md) \*params);

816

[ 836](group__bt__le__cs.md#gafcd6a882c0da413bfef5a56e53323389)int [bt\_le\_cs\_set\_channel\_classification](group__bt__le__cs.md#gafcd6a882c0da413bfef5a56e53323389)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel\_classification[10]);

837

[ 849](group__bt__le__cs.md#gaa49ff6e8340bd1753485deeec8036d1b)int [bt\_le\_cs\_read\_local\_supported\_capabilities](group__bt__le__cs.md#gaa49ff6e8340bd1753485deeec8036d1b)(struct [bt\_conn\_le\_cs\_capabilities](structbt__conn__le__cs__capabilities.md) \*ret);

850

[ 864](group__bt__le__cs.md#ga9d4b5b21886f0dd89b4073acaaa787a1)int [bt\_le\_cs\_write\_cached\_remote\_supported\_capabilities](group__bt__le__cs.md#ga9d4b5b21886f0dd89b4073acaaa787a1)(

865 struct bt\_conn \*conn, const struct [bt\_conn\_le\_cs\_capabilities](structbt__conn__le__cs__capabilities.md) \*params);

866

[ 879](group__bt__le__cs.md#ga63aa61d2bd3cf9ecb3ea9f1d02bb5b8c)int [bt\_le\_cs\_write\_cached\_remote\_fae\_table](group__bt__le__cs.md#ga63aa61d2bd3cf9ecb3ea9f1d02bb5b8c)(struct bt\_conn \*conn, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) remote\_fae\_table[72]);

880

881#ifdef \_\_cplusplus

882}

883#endif

884

888

889#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_CS\_H\_ \*/

[conn.h](conn_8h.md)

Bluetooth connection handling.

[bt\_conn\_le\_cs\_sub\_mode](group__bt__conn.md#ga07c6f1248c9a6da0168bd3d398925daf)

bt\_conn\_le\_cs\_sub\_mode

Channel sounding sub mode.

**Definition** conn.h:428

[bt\_conn\_le\_cs\_role](group__bt__conn.md#ga0e6f6d4fdbdfc3ed75fef4a95136076f)

bt\_conn\_le\_cs\_role

Channel sounding role.

**Definition** conn.h:440

[bt\_conn\_le\_cs\_main\_mode](group__bt__conn.md#ga133504278b6e01993ff36e96a238484f)

bt\_conn\_le\_cs\_main\_mode

Channel sounding main mode.

**Definition** conn.h:418

[bt\_conn\_le\_cs\_chsel\_type](group__bt__conn.md#ga34e4837a77c7afd6999095985ddad4f0)

bt\_conn\_le\_cs\_chsel\_type

Channel sounding channel selection type.

**Definition** conn.h:476

[bt\_conn\_le\_cs\_sync\_phy](group__bt__conn.md#gaadbf6a4dba28aec90ea07b7da634e1bb)

bt\_conn\_le\_cs\_sync\_phy

Channel sounding PHY used for CS sync.

**Definition** conn.h:466

[bt\_conn\_le\_cs\_tone\_antenna\_config\_selection](group__bt__conn.md#gab7acdbdf273fc760799cf0d8cf71591c)

bt\_conn\_le\_cs\_tone\_antenna\_config\_selection

CS Test Tone Antennna Config Selection.

**Definition** conn.h:1590

[bt\_conn\_le\_cs\_ch3c\_shape](group__bt__conn.md#gaf2331ec1f1222de51fc4f30566e1c52b)

bt\_conn\_le\_cs\_ch3c\_shape

Channel sounding channel sequence shape.

**Definition** conn.h:484

[bt\_conn\_le\_cs\_procedure\_enable\_state](group__bt__conn.md#gaf3653de72793f775e33fd9eb04c3e7a2)

bt\_conn\_le\_cs\_procedure\_enable\_state

**Definition** conn.h:1558

[bt\_conn\_le\_cs\_rtt\_type](group__bt__conn.md#gaffd6abf9b92cc8d8463797a73b840f51)

bt\_conn\_le\_cs\_rtt\_type

Channel sounding RTT type.

**Definition** conn.h:448

[bt\_le\_cs\_read\_remote\_fae\_table](group__bt__le__cs.md#ga127034536a98743d359c749fe7c79dba)

int bt\_le\_cs\_read\_remote\_fae\_table(struct bt\_conn \*conn)

Read Remote FAE Table.

[bt\_le\_cs\_test\_override\_4\_tone\_antenna\_permutation](group__bt__le__cs.md#ga1ba4d7d919cb5c09469f8e8aa05bb04d)

bt\_le\_cs\_test\_override\_4\_tone\_antenna\_permutation

CS Test Override 4 Tone Antenna Permutation.

**Definition** cs.h:183

[bt\_le\_cs\_create\_config\_context](group__bt__le__cs.md#ga22822b2dd21d64c8c64a66f2b5dee9b1)

bt\_le\_cs\_create\_config\_context

CS config creation context.

**Definition** cs.h:469

[bt\_le\_cs\_create\_config](group__bt__le__cs.md#ga27bae87f9769a2d5802c57adfa201b23)

int bt\_le\_cs\_create\_config(struct bt\_conn \*conn, struct bt\_le\_cs\_create\_config\_params \*params, enum bt\_le\_cs\_create\_config\_context context)

Create CS configuration.

[bt\_le\_cs\_remove\_config](group__bt__le__cs.md#ga2a27b80e72ff2bfe986b3cbe11f225f3)

int bt\_le\_cs\_remove\_config(struct bt\_conn \*conn, uint8\_t config\_id)

Create CS configuration.

[bt\_le\_cs\_procedure\_enable](group__bt__le__cs.md#ga2b6f3c3795b5eeb424542c1858f84cbc)

int bt\_le\_cs\_procedure\_enable(struct bt\_conn \*conn, const struct bt\_le\_cs\_procedure\_enable\_param \*params)

CS Procedure Enable.

[bt\_le\_cs\_security\_enable](group__bt__le__cs.md#ga346a46dc3321c5bab034904bf09aa4e3)

int bt\_le\_cs\_security\_enable(struct bt\_conn \*conn)

CS Security Enable.

[bt\_le\_cs\_stop\_test](group__bt__le__cs.md#ga4742baeb1eb46969233f787344cb5e11)

int bt\_le\_cs\_stop\_test(void)

Stop ongoing CS Test.

[bt\_le\_cs\_write\_cached\_remote\_fae\_table](group__bt__le__cs.md#ga63aa61d2bd3cf9ecb3ea9f1d02bb5b8c)

int bt\_le\_cs\_write\_cached\_remote\_fae\_table(struct bt\_conn \*conn, int8\_t remote\_fae\_table[72])

CS Write Cached Remote FAE Table.

[bt\_le\_cs\_set\_default\_settings](group__bt__le__cs.md#ga6ee9b8fa52b96dce41b1c879865fa938)

int bt\_le\_cs\_set\_default\_settings(struct bt\_conn \*conn, const struct bt\_le\_cs\_set\_default\_settings\_param \*params)

Set Channel Sounding default settings.

[bt\_le\_cs\_test\_override\_8\_cs\_sync\_payload\_pattern](group__bt__le__cs.md#ga731bbaa98dab7c88725fc64b66da62eb)

bt\_le\_cs\_test\_override\_8\_cs\_sync\_payload\_pattern

CS Test Override 8 CS\_SYNC Payload Pattern.

**Definition** cs.h:224

[bt\_le\_cs\_test\_cs\_sync\_antenna\_selection](group__bt__le__cs.md#ga782a500f611320a6f3feed9897ab8e16)

bt\_le\_cs\_test\_cs\_sync\_antenna\_selection

CS Test CS\_SYNC Antenna Identifier.

**Definition** cs.h:84

[bt\_le\_cs\_write\_cached\_remote\_supported\_capabilities](group__bt__le__cs.md#ga9d4b5b21886f0dd89b4073acaaa787a1)

int bt\_le\_cs\_write\_cached\_remote\_supported\_capabilities(struct bt\_conn \*conn, const struct bt\_conn\_le\_cs\_capabilities \*params)

CS Write Cached Remote Supported Capabilities.

[bt\_le\_cs\_procedure\_phy](group__bt__le__cs.md#ga9e008daa9c0c1702aa3b4479e7a37ca4)

bt\_le\_cs\_procedure\_phy

**Definition** cs.h:744

[bt\_le\_cs\_sync\_antenna\_selection\_opt](group__bt__le__cs.md#ga9f286cdeeee0e9df06e6b3df1e9ab643)

bt\_le\_cs\_sync\_antenna\_selection\_opt

**Definition** cs.h:50

[bt\_le\_cs\_read\_local\_supported\_capabilities](group__bt__le__cs.md#gaa49ff6e8340bd1753485deeec8036d1b)

int bt\_le\_cs\_read\_local\_supported\_capabilities(struct bt\_conn\_le\_cs\_capabilities \*ret)

CS Read Local Supported Capabilities.

[bt\_le\_cs\_set\_valid\_chmap\_bits](group__bt__le__cs.md#gaa979dc080cf277a2382b6ba77f8a1c09)

void bt\_le\_cs\_set\_valid\_chmap\_bits(uint8\_t channel\_map[10])

Set all valid channel map bits.

[bt\_le\_cs\_test\_override\_7\_ss\_marker\_value](group__bt__le__cs.md#gacb3f437225ad1d6320ee424c39ebc82a)

bt\_le\_cs\_test\_override\_7\_ss\_marker\_value

CS Test Override 7 Sounding Sequence Marker Value.

**Definition** cs.h:216

[bt\_le\_cs\_set\_procedure\_parameters](group__bt__le__cs.md#gad6e0fb9c7f92678598d9780b78710961)

int bt\_le\_cs\_set\_procedure\_parameters(struct bt\_conn \*conn, const struct bt\_le\_cs\_set\_procedure\_parameters\_param \*params)

CS Set Procedure Parameters.

[bt\_le\_cs\_start\_test](group__bt__le__cs.md#gada91ff7c7a82620d77bf78781ebea356)

int bt\_le\_cs\_start\_test(const struct bt\_le\_cs\_test\_param \*params)

Start a CS test.

[bt\_le\_cs\_read\_remote\_supported\_capabilities](group__bt__le__cs.md#gadb3afd94cd11d035cfe34c6a63b37b19)

int bt\_le\_cs\_read\_remote\_supported\_capabilities(struct bt\_conn \*conn)

Read Remote Supported Capabilities.

[bt\_le\_cs\_step\_data\_parse](group__bt__le__cs.md#gadcd85f3799f4219a01e84fc281ff1a31)

void bt\_le\_cs\_step\_data\_parse(struct net\_buf\_simple \*step\_data\_buf, bool(\*func)(struct bt\_le\_cs\_subevent\_step \*step, void \*user\_data), void \*user\_data)

Parse CS Subevent Step Data.

[bt\_le\_cs\_test\_cb\_register](group__bt__le__cs.md#gaf03c4ed5c7e179ee3b374efa857188e2)

int bt\_le\_cs\_test\_cb\_register(struct bt\_le\_cs\_test\_cb cs\_test\_cb)

Register callbacks for the CS Test mode.

[bt\_le\_cs\_snr\_control](group__bt__le__cs.md#gaf34c59887e8a6da0560b6428733fe8d0)

bt\_le\_cs\_snr\_control

CS SNR control options.

**Definition** cs.h:92

[bt\_le\_cs\_test\_override\_3\_pm\_tone\_ext](group__bt__le__cs.md#gaf50910d51c69e216ef6eb22b5c0f2d28)

bt\_le\_cs\_test\_override\_3\_pm\_tone\_ext

CS Test Override 3 T\_PM Tone Extension.

**Definition** cs.h:102

[bt\_le\_cs\_parse\_pct](group__bt__le__cs.md#gaf99d82194bbcc471c3de2094b39a2201)

struct bt\_le\_cs\_iq\_sample bt\_le\_cs\_parse\_pct(const uint8\_t pct[3])

Extract in-phase and quadrature terms from HCI-formatted PCT.

[bt\_le\_cs\_set\_channel\_classification](group__bt__le__cs.md#gafcd6a882c0da413bfef5a56e53323389)

int bt\_le\_cs\_set\_channel\_classification(uint8\_t channel\_classification[10])

CS Set Channel Classification.

[BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_15](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da144a6190783b1fbc5ccde1b9f0ec3581)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_15

**Definition** cs.h:199

[BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_07](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da28e1b78a9bb927c4d38047e2aed57a15)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_07

**Definition** cs.h:191

[BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_LOOP](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da2abd10e7d80703b3d849ad19d65af31f)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_LOOP

Loop through all valid Antenna Permutation Indices starting from the lowest index.

**Definition** cs.h:211

[BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_10](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da2ac77dab1caf34f436075dab45cc4aea)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_10

**Definition** cs.h:194

[BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_13](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da2b34111edb7b0b1412de7d4485cbc164)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_13

**Definition** cs.h:197

[BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_21](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da3cc8b9dfadae103bdbb0fb79c523f553)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_21

**Definition** cs.h:205

[BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_04](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da3fe0da05e9c2493af3ea42a0c6cd4b17)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_04

**Definition** cs.h:188

[BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_12](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da45f979b88a3d63c4f270d246c98f3b53)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_12

**Definition** cs.h:196

[BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_14](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da5ab31e2b89fef73d838ade33de5d770b)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_14

**Definition** cs.h:198

[BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_00](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da72b3c5a4d07ae3c73e9bb131c725d17f)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_00

**Definition** cs.h:184

[BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_03](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da7731f27f1af37ba740764e9875d28482)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_03

**Definition** cs.h:187

[BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_01](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da7aed472d8ed1b3fc84e89531134fc71c)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_01

**Definition** cs.h:185

[BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_05](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04daa73b01369a29b4ea7de2aadb71efe699)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_05

**Definition** cs.h:189

[BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_18](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04daad5f0f4d2818f986472f8cca57b37ea9)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_18

**Definition** cs.h:202

[BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_08](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dab1cbcd7ceb33fb13b7d70b0dc671849c)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_08

**Definition** cs.h:192

[BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_02](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dab986f2c0c54de93cfdf5a5334aafffb2)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_02

**Definition** cs.h:186

[BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_17](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dabe494d770af056108d4679364a93acce)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_17

**Definition** cs.h:201

[BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_19](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dac02f9fa05c0f35bb306fde66bc80ab21)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_19

**Definition** cs.h:203

[BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_23](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dac3a263bfe1f80c38647d6aeab42b12c3)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_23

**Definition** cs.h:207

[BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_20](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dad355ee587eff65a2a2f80274fc6c5081)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_20

**Definition** cs.h:204

[BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_11](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dad85a40214189a9c036c95d88fb752a0c)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_11

**Definition** cs.h:195

[BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_22](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dadf2778f065f696ad43ceca71aa6a8a80)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_22

**Definition** cs.h:206

[BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_06](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dae4f815603cdffeb82711b994be2209dc)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_06

**Definition** cs.h:190

[BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_09](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dae7f0fedfabe1748f9918befedbc45944)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_09

**Definition** cs.h:193

[BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_16](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dae87750d18c24ddcece72919e107da671)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_16

**Definition** cs.h:200

[BT\_LE\_CS\_CREATE\_CONFIG\_CONTEXT\_LOCAL\_ONLY](group__bt__le__cs.md#gga22822b2dd21d64c8c64a66f2b5dee9b1adb8a8af222fed7262bdb57bc4f18a706)

@ BT\_LE\_CS\_CREATE\_CONFIG\_CONTEXT\_LOCAL\_ONLY

Write CS configuration in local Controller only.

**Definition** cs.h:471

[BT\_LE\_CS\_CREATE\_CONFIG\_CONTEXT\_LOCAL\_AND\_REMOTE](group__bt__le__cs.md#gga22822b2dd21d64c8c64a66f2b5dee9b1ae5107dfa011451ecaa404906fabc41e4)

@ BT\_LE\_CS\_CREATE\_CONFIG\_CONTEXT\_LOCAL\_AND\_REMOTE

Write CS configuration in both local and remote Controller using Channel Sounding Configuration proce...

**Definition** cs.h:475

[BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_11110000](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62eba109f2588e566b9651b67dbbf9583813c)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_11110000

Repeated '11110000' payload sequence.

**Definition** cs.h:228

[BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_00000000](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62eba1b46b8b073ca599cb89d86b261fa4dd5)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_00000000

Repeated '00000000' payload sequence.

**Definition** cs.h:236

[BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_PRBS15](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62eba1b910950b96ad0b47b0b235a2e8e45c8)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_PRBS15

PRBS15 payload sequence.

**Definition** cs.h:232

[BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_PRBS9](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62eba3c8bc2a6858dc2d0de02b3b681a854a0)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_PRBS9

PRBS9 payload sequence.

**Definition** cs.h:226

[BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_00001111](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62eba4f4ec5a6d46734e8c5801e9e79535b70)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_00001111

Repeated '00001111' payload sequence.

**Definition** cs.h:238

[BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_01010101](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62eba6c59258c52a5889e0b11aa0fb0f99bcb)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_01010101

Repeated '01010101' payload sequence.

**Definition** cs.h:240

[BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_11111111](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62ebabc520467cdbaaf34d0c815e0d62bd097)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_11111111

Repeated '11111111' payload sequence.

**Definition** cs.h:234

[BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_10101010](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62ebaef4b4455b236d70fae6a0138050d0835)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_10101010

Repeated '10101010' payload sequence.

**Definition** cs.h:230

[BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_USER](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62ebaf68334f70d91d587e906533ad544fef1)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_USER

Custom payload provided by the user.

**Definition** cs.h:242

[BT\_LE\_CS\_TEST\_CS\_SYNC\_ANTENNA\_SELECTION\_ONE](group__bt__le__cs.md#gga782a500f611320a6f3feed9897ab8e16a054f9b7f51323480106f11929425599f)

@ BT\_LE\_CS\_TEST\_CS\_SYNC\_ANTENNA\_SELECTION\_ONE

**Definition** cs.h:85

[BT\_LE\_CS\_TEST\_CS\_SYNC\_ANTENNA\_SELECTION\_FOUR](group__bt__le__cs.md#gga782a500f611320a6f3feed9897ab8e16a678e1a8120f21f3707d4b9ea22bd8c47)

@ BT\_LE\_CS\_TEST\_CS\_SYNC\_ANTENNA\_SELECTION\_FOUR

**Definition** cs.h:88

[BT\_LE\_CS\_TEST\_CS\_SYNC\_ANTENNA\_SELECTION\_THREE](group__bt__le__cs.md#gga782a500f611320a6f3feed9897ab8e16aa059024bd3d90677ee00d4accd99f39c)

@ BT\_LE\_CS\_TEST\_CS\_SYNC\_ANTENNA\_SELECTION\_THREE

**Definition** cs.h:87

[BT\_LE\_CS\_TEST\_CS\_SYNC\_ANTENNA\_SELECTION\_TWO](group__bt__le__cs.md#gga782a500f611320a6f3feed9897ab8e16aa1931403e835ab2e18982dd0f2a67803)

@ BT\_LE\_CS\_TEST\_CS\_SYNC\_ANTENNA\_SELECTION\_TWO

**Definition** cs.h:86

[BT\_LE\_CS\_PROCEDURE\_PHY\_2M](group__bt__le__cs.md#gga9e008daa9c0c1702aa3b4479e7a37ca4a072649a66bf1260ce37bd16fc7a9185d)

@ BT\_LE\_CS\_PROCEDURE\_PHY\_2M

**Definition** cs.h:746

[BT\_LE\_CS\_PROCEDURE\_PHY\_CODED\_S8](group__bt__le__cs.md#gga9e008daa9c0c1702aa3b4479e7a37ca4a1ceb33afa661774e1077caced63bf263)

@ BT\_LE\_CS\_PROCEDURE\_PHY\_CODED\_S8

**Definition** cs.h:747

[BT\_LE\_CS\_PROCEDURE\_PHY\_CODED\_S2](group__bt__le__cs.md#gga9e008daa9c0c1702aa3b4479e7a37ca4a5370237bdbceb37a631425f472ddc322)

@ BT\_LE\_CS\_PROCEDURE\_PHY\_CODED\_S2

**Definition** cs.h:748

[BT\_LE\_CS\_PROCEDURE\_PHY\_1M](group__bt__le__cs.md#gga9e008daa9c0c1702aa3b4479e7a37ca4aa1dcc1e15aac59898c0a6c229593a76b)

@ BT\_LE\_CS\_PROCEDURE\_PHY\_1M

**Definition** cs.h:745

[BT\_LE\_CS\_ANTENNA\_SELECTION\_OPT\_THREE](group__bt__le__cs.md#gga9f286cdeeee0e9df06e6b3df1e9ab643a35ae07887f3d55bcbd10d531f09c841d)

@ BT\_LE\_CS\_ANTENNA\_SELECTION\_OPT\_THREE

Use antenna identifier 3 for CS\_SYNC packets.

**Definition** cs.h:56

[BT\_LE\_CS\_ANTENNA\_SELECTION\_OPT\_ONE](group__bt__le__cs.md#gga9f286cdeeee0e9df06e6b3df1e9ab643a5de14d0cc770615bd08c4e3d197bae90)

@ BT\_LE\_CS\_ANTENNA\_SELECTION\_OPT\_ONE

Use antenna identifier 1 for CS\_SYNC packets.

**Definition** cs.h:52

[BT\_LE\_CS\_ANTENNA\_SELECTION\_OPT\_TWO](group__bt__le__cs.md#gga9f286cdeeee0e9df06e6b3df1e9ab643a7ce16e0eab20cf432c8e93a7f6be8ca5)

@ BT\_LE\_CS\_ANTENNA\_SELECTION\_OPT\_TWO

Use antenna identifier 2 for CS\_SYNC packets.

**Definition** cs.h:54

[BT\_LE\_CS\_ANTENNA\_SELECTION\_OPT\_NO\_RECOMMENDATION](group__bt__le__cs.md#gga9f286cdeeee0e9df06e6b3df1e9ab643a861f35bdbe322238bdad67568e5674f3)

@ BT\_LE\_CS\_ANTENNA\_SELECTION\_OPT\_NO\_RECOMMENDATION

No recommendation for local controller antenna selection.

**Definition** cs.h:62

[BT\_LE\_CS\_ANTENNA\_SELECTION\_OPT\_REPETITIVE](group__bt__le__cs.md#gga9f286cdeeee0e9df06e6b3df1e9ab643aa23b552af8b16b1371f7a362089eaca7)

@ BT\_LE\_CS\_ANTENNA\_SELECTION\_OPT\_REPETITIVE

Use antennas in repetitive order from 1 to 4 for CS\_SYNC packets.

**Definition** cs.h:60

[BT\_LE\_CS\_ANTENNA\_SELECTION\_OPT\_FOUR](group__bt__le__cs.md#gga9f286cdeeee0e9df06e6b3df1e9ab643aa5370917d0f46fe654ba42fbbd587ceb)

@ BT\_LE\_CS\_ANTENNA\_SELECTION\_OPT\_FOUR

Use antenna identifier 4 for CS\_SYNC packets.

**Definition** cs.h:58

[BT\_LE\_CS\_TEST\_OVERRIDE\_7\_SS\_MARKER\_VAL\_LOOP](group__bt__le__cs.md#ggacb3f437225ad1d6320ee424c39ebc82aa3a3078691c778d1c7a30fe9400bc5f0f)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_7\_SS\_MARKER\_VAL\_LOOP

Loop through pattern '0011' and '1100' (in transmission order).

**Definition** cs.h:220

[BT\_LE\_CS\_TEST\_OVERRIDE\_7\_SS\_MARKER\_VAL\_1100](group__bt__le__cs.md#ggacb3f437225ad1d6320ee424c39ebc82aa6b6bc126c5e2a97de33d6c83230ebb92)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_7\_SS\_MARKER\_VAL\_1100

**Definition** cs.h:218

[BT\_LE\_CS\_TEST\_OVERRIDE\_7\_SS\_MARKER\_VAL\_0011](group__bt__le__cs.md#ggacb3f437225ad1d6320ee424c39ebc82aa99a26684d34169d062150f61cb0ba889)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_7\_SS\_MARKER\_VAL\_0011

**Definition** cs.h:217

[BT\_LE\_CS\_SNR\_CONTROL\_24dB](group__bt__le__cs.md#ggaf34c59887e8a6da0560b6428733fe8d0a02394d7394f79a6e91a8f81070fdf82e)

@ BT\_LE\_CS\_SNR\_CONTROL\_24dB

**Definition** cs.h:95

[BT\_LE\_CS\_SNR\_CONTROL\_30dB](group__bt__le__cs.md#ggaf34c59887e8a6da0560b6428733fe8d0a18bb25e63782e9993a3853d929d58ee1)

@ BT\_LE\_CS\_SNR\_CONTROL\_30dB

**Definition** cs.h:97

[BT\_LE\_CS\_SNR\_CONTROL\_NOT\_USED](group__bt__le__cs.md#ggaf34c59887e8a6da0560b6428733fe8d0a1a5c531f590f14773b7ddc9b0ec8cae9)

@ BT\_LE\_CS\_SNR\_CONTROL\_NOT\_USED

**Definition** cs.h:98

[BT\_LE\_CS\_SNR\_CONTROL\_27dB](group__bt__le__cs.md#ggaf34c59887e8a6da0560b6428733fe8d0a43a7b210424a2aa2830a07676d3499b8)

@ BT\_LE\_CS\_SNR\_CONTROL\_27dB

**Definition** cs.h:96

[BT\_LE\_CS\_SNR\_CONTROL\_21dB](group__bt__le__cs.md#ggaf34c59887e8a6da0560b6428733fe8d0a685a458547bda6af6c88626ee08c4110)

@ BT\_LE\_CS\_SNR\_CONTROL\_21dB

**Definition** cs.h:94

[BT\_LE\_CS\_SNR\_CONTROL\_18dB](group__bt__le__cs.md#ggaf34c59887e8a6da0560b6428733fe8d0a78af4f3bbf5adfc8ee6f9d459bb96e7d)

@ BT\_LE\_CS\_SNR\_CONTROL\_18dB

**Definition** cs.h:93

[BT\_LE\_CS\_TEST\_OVERRIDE\_3\_REPETITIVE\_TONE\_EXT](group__bt__le__cs.md#ggaf50910d51c69e216ef6eb22b5c0f2d28a9a691cb7b4a9cff799d848fc79cf40dd)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_3\_REPETITIVE\_TONE\_EXT

Applicable for mode-2 and mode-3 only:

**Definition** cs.h:120

[BT\_LE\_CS\_TEST\_OVERRIDE\_3\_NO\_TONE\_EXT](group__bt__le__cs.md#ggaf50910d51c69e216ef6eb22b5c0f2d28aa5f4fea24a1b27736cfc36c470a3a008)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_3\_NO\_TONE\_EXT

Initiator and reflector tones sent without tone extension.

**Definition** cs.h:104

[BT\_LE\_CS\_TEST\_OVERRIDE\_3\_REFLECTOR\_TONE\_EXT\_ONLY](group__bt__le__cs.md#ggaf50910d51c69e216ef6eb22b5c0f2d28ab504c3a24b36413ea2395bd579e5bba2)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_3\_REFLECTOR\_TONE\_EXT\_ONLY

Initiator tone sent without extension, reflector tone sent with tone extension.

**Definition** cs.h:108

[BT\_LE\_CS\_TEST\_OVERRIDE\_3\_INITIATOR\_AND\_REFLECTOR\_TONE\_EXT](group__bt__le__cs.md#ggaf50910d51c69e216ef6eb22b5c0f2d28ad2b323c3c54409545458c08fc6660cf4)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_3\_INITIATOR\_AND\_REFLECTOR\_TONE\_EXT

Initiator and reflector tones sent with tone extension.

**Definition** cs.h:110

[BT\_LE\_CS\_TEST\_OVERRIDE\_3\_INITIATOR\_TONE\_EXT\_ONLY](group__bt__le__cs.md#ggaf50910d51c69e216ef6eb22b5c0f2d28aee2c022be115a4c865d5524795f2d039)

@ BT\_LE\_CS\_TEST\_OVERRIDE\_3\_INITIATOR\_TONE\_EXT\_ONLY

Initiator tone sent with extension, reflector tone sent without tone extension.

**Definition** cs.h:106

[hci\_types.h](hci__types_8h.md)

[BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_2M](hci__types_8h.md#a016f68a621de8d332f3073df4faf1702)

#define BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_2M

**Definition** hci\_types.h:2541

[BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_04](hci__types_8h.md#a03ffb0ffb8e98b26390575b153471bab)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_04

**Definition** hci\_types.h:2644

[BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_00000000](hci__types_8h.md#a04a26b8600cac8c82247a7d51122f600)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_00000000

**Definition** hci\_types.h:2677

[BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_INIT](hci__types_8h.md#a0513bf5ca6eb9f43a7e8cecaf943c4d7)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_INIT

**Definition** hci\_types.h:2635

[BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_13](hci__types_8h.md#a08690b2f762d24c34966b839a6d5e696)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_13

**Definition** hci\_types.h:2653

[BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_17](hci__types_8h.md#a08db476ea6516691baeb9007b553281d)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_17

**Definition** hci\_types.h:2657

[BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_10](hci__types_8h.md#a0e9664c52808aa246218f92a4fb55516)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_10

**Definition** hci\_types.h:2650

[BT\_HCI\_OP\_LE\_CS\_SNR\_24](hci__types_8h.md#a135a4dc2f191d2a931b4270e00774cb2)

#define BT\_HCI\_OP\_LE\_CS\_SNR\_24

**Definition** hci\_types.h:2613

[BT\_HCI\_OP\_LE\_CS\_SNR\_30](hci__types_8h.md#a181c2d98b93bd18e9edc11a6f9535331)

#define BT\_HCI\_OP\_LE\_CS\_SNR\_30

**Definition** hci\_types.h:2615

[BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_VAL\_LOOP](hci__types_8h.md#a24d2e56f620500905572e786f2523b0e)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_VAL\_LOOP

**Definition** hci\_types.h:2670

[BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_CODED\_S8](hci__types_8h.md#a2543f9fa20db642fb8b47b949c50af6a)

#define BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_CODED\_S8

**Definition** hci\_types.h:2542

[BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_03](hci__types_8h.md#a2cc7a5d5d2105b1a428703e274cc5388)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_03

**Definition** hci\_types.h:2643

[BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_1M](hci__types_8h.md#a3a8f1c94f40696f18e18810f736497e3)

#define BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_1M

**Definition** hci\_types.h:2540

[BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_VAL\_0011](hci__types_8h.md#a45e1ff56f1a6dcc59b784905e4fc6726)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_VAL\_0011

**Definition** hci\_types.h:2668

[BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_21](hci__types_8h.md#a46f70b5096593956795cc381e33c4aa2)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_21

**Definition** hci\_types.h:2661

[BT\_HCI\_OP\_LE\_CS\_SNR\_NOT\_USED](hci__types_8h.md#a4aa2e02ce5110be3dc68a801bb583372)

#define BT\_HCI\_OP\_LE\_CS\_SNR\_NOT\_USED

**Definition** hci\_types.h:2616

[BT\_HCI\_OP\_LE\_CS\_SNR\_21](hci__types_8h.md#a4b93a8bceafd49d6ca65816924bb4230)

#define BT\_HCI\_OP\_LE\_CS\_SNR\_21

**Definition** hci\_types.h:2612

[BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_12](hci__types_8h.md#a4c4a44bd33ebf97852e6640b0d510fdd)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_12

**Definition** hci\_types.h:2652

[BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_PRBS9](hci__types_8h.md#a4f922c5e0662adf8471686dfa9b719ec)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_PRBS9

**Definition** hci\_types.h:2672

[BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_REPEAT](hci__types_8h.md#a50fba6ab75b37ccf39452211ba05e896)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_REPEAT

**Definition** hci\_types.h:2638

[BT\_HCI\_OP\_LE\_CS\_SNR\_27](hci__types_8h.md#a52eb27d8f726a2ed6859149fcdf2355d)

#define BT\_HCI\_OP\_LE\_CS\_SNR\_27

**Definition** hci\_types.h:2614

[BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_01010101](hci__types_8h.md#a53f0ca5604489a38a1367736a5297b45)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_01010101

**Definition** hci\_types.h:2679

[BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_VAL\_1100](hci__types_8h.md#a5d3c206a5067ddc5a02a5d5e8c3eb7a3)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_VAL\_1100

**Definition** hci\_types.h:2669

[BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_19](hci__types_8h.md#a5df817bdfefc4de0a1309cf71908a105)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_19

**Definition** hci\_types.h:2659

[BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_06](hci__types_8h.md#a70607449d6bd6207783e319e77d63b16)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_06

**Definition** hci\_types.h:2646

[BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_02](hci__types_8h.md#a762c5efa09e1fba989fdfb0bdcba9b9c)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_02

**Definition** hci\_types.h:2642

[BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_CODED\_S2](hci__types_8h.md#a776a14d8e7fdca584475f26b441c8bfb)

#define BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_CODED\_S2

**Definition** hci\_types.h:2543

[BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_ONE](hci__types_8h.md#a7fa26323384443ba9c5e635047b74f51)

#define BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_ONE

**Definition** hci\_types.h:2509

[BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_THREE](hci__types_8h.md#a8721a8f4670a8038d66d42adea061f57)

#define BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_THREE

**Definition** hci\_types.h:2511

[BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_11](hci__types_8h.md#a8fbc80d91e4a1ae04c76cda189cd5d83)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_11

**Definition** hci\_types.h:2651

[BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_PRBS15](hci__types_8h.md#a92bc70a5ad7938a46ac9f2127f1bc2d9)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_PRBS15

**Definition** hci\_types.h:2675

[BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_USER](hci__types_8h.md#a94007d8250c3524ad0b86745dbb74b3b)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_USER

**Definition** hci\_types.h:2680

[BT\_HCI\_OP\_LE\_CS\_SNR\_18](hci__types_8h.md#a96b13fb3b363a5436e1b9633f54bb248)

#define BT\_HCI\_OP\_LE\_CS\_SNR\_18

**Definition** hci\_types.h:2611

[BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_08](hci__types_8h.md#a9dfd88863d649182855edc8c268107d6)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_08

**Definition** hci\_types.h:2648

[BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_NONE](hci__types_8h.md#a9ed8967faa3ee3824433422709148330)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_NONE

**Definition** hci\_types.h:2634

[BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_18](hci__types_8h.md#a9f0bf05cb0aac50e1df43397c3b913bc)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_18

**Definition** hci\_types.h:2658

[BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_01](hci__types_8h.md#aa0e9e2081d3cbbb60de9b6dcffe77239)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_01

**Definition** hci\_types.h:2641

[BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_REFL](hci__types_8h.md#aa24ae1cf1501de66660051a4a62246df)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_REFL

**Definition** hci\_types.h:2636

[BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_00](hci__types_8h.md#aa4ba4be270035da446389766b795c327)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_00

**Definition** hci\_types.h:2640

[BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_TWO](hci__types_8h.md#aa6d146c85e3148a2afb66023d94c2eeb)

#define BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_TWO

**Definition** hci\_types.h:2510

[BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_11111111](hci__types_8h.md#aa94eda86c6ffe85a65267f285dae5cb1)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_11111111

**Definition** hci\_types.h:2676

[BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_15](hci__types_8h.md#ab2b0745d98053775e9bf073e36ce5d78)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_15

**Definition** hci\_types.h:2655

[BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_22](hci__types_8h.md#abe9fa4621e9c004421170b0166ea14e1)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_22

**Definition** hci\_types.h:2662

[BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_00001111](hci__types_8h.md#abf19d511680005828add231d64e1e3f0)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_00001111

**Definition** hci\_types.h:2678

[BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_14](hci__types_8h.md#ac2cd3ed1583f86af0480b8481cedca1e)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_14

**Definition** hci\_types.h:2654

[BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_LOOP](hci__types_8h.md#ac9d7cb5a339759b7e0c4ed150a487ca3)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_LOOP

**Definition** hci\_types.h:2664

[BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_07](hci__types_8h.md#acc79a879ea527c2901a8b91dae58d0ed)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_07

**Definition** hci\_types.h:2647

[BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_BOTH](hci__types_8h.md#ad7a89a9365e20e4cd1e44bdb74ae7ecb)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_BOTH

**Definition** hci\_types.h:2637

[BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_05](hci__types_8h.md#adbd3820e0ffa5f99e27778217d477010)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_05

**Definition** hci\_types.h:2645

[BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_16](hci__types_8h.md#add2c42aa2583b93b0f98ac33ca61ca9d)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_16

**Definition** hci\_types.h:2656

[BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_10101010](hci__types_8h.md#ae133ef2939518d660df5322551157d47)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_10101010

**Definition** hci\_types.h:2674

[BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_09](hci__types_8h.md#ae5a27304aa1cefdfb26ae2cbf42532e3)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_09

**Definition** hci\_types.h:2649

[BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_20](hci__types_8h.md#ae64e5a409523b94ef1ce315ed49afed0)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_20

**Definition** hci\_types.h:2660

[BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_NONE](hci__types_8h.md#aed2444a40bc79ccf3f383dd961036f5e)

#define BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_NONE

**Definition** hci\_types.h:2514

[BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_FOUR](hci__types_8h.md#af0d407f944831f8c85f91fb60f5bc618)

#define BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_FOUR

**Definition** hci\_types.h:2512

[BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_11110000](hci__types_8h.md#af20dfb1e245afc06a495179d700f126f)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_11110000

**Definition** hci\_types.h:2673

[BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_REP](hci__types_8h.md#afad5b26b2a6ce125b6198856d20bcdd8)

#define BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_REP

**Definition** hci\_types.h:2513

[BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_23](hci__types_8h.md#afc41ca64d03a7ed8ea82a641a0217436)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_23

**Definition** hci\_types.h:2663

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[bt\_conn\_le\_cs\_capabilities](structbt__conn__le__cs__capabilities.md)

Remote channel sounding capabilities for LE connections supporting CS.

**Definition** conn.h:297

[bt\_conn\_le\_cs\_subevent\_result](structbt__conn__le__cs__subevent__result.md)

Subevent data for LE connections supporting CS.

**Definition** conn.h:580

[bt\_le\_cs\_create\_config\_params](structbt__le__cs__create__config__params.md)

CS Create Config params.

**Definition** cs.h:479

[bt\_le\_cs\_create\_config\_params::rtt\_type](structbt__le__cs__create__config__params.md#a0a34afa329e88af8fcbcff1a8b0a1bcd)

enum bt\_conn\_le\_cs\_rtt\_type rtt\_type

RTT type.

**Definition** cs.h:500

[bt\_le\_cs\_create\_config\_params::ch3c\_shape](structbt__le__cs__create__config__params.md#a14ac5115fa91bc7ed4a4aa7a0786f81f)

enum bt\_conn\_le\_cs\_ch3c\_shape ch3c\_shape

User-specified channel sequence shape.

**Definition** cs.h:510

[bt\_le\_cs\_create\_config\_params::sub\_mode\_type](structbt__le__cs__create__config__params.md#a1bec59da1343bbc70a575d6dbde56309)

enum bt\_conn\_le\_cs\_sub\_mode sub\_mode\_type

Sub CS mode type.

**Definition** cs.h:485

[bt\_le\_cs\_create\_config\_params::role](structbt__le__cs__create__config__params.md#a2581694b25afa7903786c7848c133c38)

enum bt\_conn\_le\_cs\_role role

CS role.

**Definition** cs.h:498

[bt\_le\_cs\_create\_config\_params::main\_mode\_type](structbt__le__cs__create__config__params.md#a2bdbff2e20106e4a6925a8018d491a9c)

enum bt\_conn\_le\_cs\_main\_mode main\_mode\_type

Main CS mode type.

**Definition** cs.h:483

[bt\_le\_cs\_create\_config\_params::cs\_sync\_phy](structbt__le__cs__create__config__params.md#a4329d967361e330077ca9064bdc3fc5f)

enum bt\_conn\_le\_cs\_sync\_phy cs\_sync\_phy

CS Sync PHY.

**Definition** cs.h:502

[bt\_le\_cs\_create\_config\_params::id](structbt__le__cs__create__config__params.md#a59615f8de0a39f124ae3d2e2876ecc30)

uint8\_t id

CS configuration ID.

**Definition** cs.h:481

[bt\_le\_cs\_create\_config\_params::channel\_map\_repetition](structbt__le__cs__create__config__params.md#a6eff424679cb98ba2d749636618744ce)

uint8\_t channel\_map\_repetition

The number of times the Channel\_Map field will be cycled through for non-mode-0 steps within a CS pro...

**Definition** cs.h:506

[bt\_le\_cs\_create\_config\_params::main\_mode\_repetition](structbt__le__cs__create__config__params.md#a9a7c56e1d04d634aaab4f3b81c506be3)

uint8\_t main\_mode\_repetition

Number of main mode steps taken from the end of the last CS subevent to be repeated at the beginning ...

**Definition** cs.h:494

[bt\_le\_cs\_create\_config\_params::max\_main\_mode\_steps](structbt__le__cs__create__config__params.md#aa8951ab286210ab87c460ed315d091bf)

uint8\_t max\_main\_mode\_steps

Maximum number of CS main mode steps to be executed before a submode step is executed.

**Definition** cs.h:489

[bt\_le\_cs\_create\_config\_params::channel\_selection\_type](structbt__le__cs__create__config__params.md#ac83ef36301b0d990cb3a7cf1e630c957)

enum bt\_conn\_le\_cs\_chsel\_type channel\_selection\_type

Channel selection type.

**Definition** cs.h:508

[bt\_le\_cs\_create\_config\_params::ch3c\_jump](structbt__le__cs__create__config__params.md#ad0ea92b48ac4e9753ee422f2286c1ded)

uint8\_t ch3c\_jump

Number of channels skipped in each rising and falling sequence.

**Definition** cs.h:512

[bt\_le\_cs\_create\_config\_params::channel\_map](structbt__le__cs__create__config__params.md#adcf6276f58bd19ec61800160979fd472)

uint8\_t channel\_map[10]

Channel map used for CS procedure Channels n = 0, 1, 23, 24, 25, 77, and 78 are not allowed and shall...

**Definition** cs.h:518

[bt\_le\_cs\_create\_config\_params::min\_main\_mode\_steps](structbt__le__cs__create__config__params.md#ae7ff30dcfcb4460dac48c139bdac0f75)

uint8\_t min\_main\_mode\_steps

Minimum number of CS main mode steps to be executed before a submode step is executed.

**Definition** cs.h:487

[bt\_le\_cs\_create\_config\_params::mode\_0\_steps](structbt__le__cs__create__config__params.md#af824b6b56fba318588ebcf707d6e7a24)

uint8\_t mode\_0\_steps

Number of CS mode-0 steps to be included at the beginning of each CS subevent.

**Definition** cs.h:496

[bt\_le\_cs\_iq\_sample](structbt__le__cs__iq__sample.md)

Sign-extended IQ value extracted from step data.

**Definition** cs.h:545

[bt\_le\_cs\_iq\_sample::q](structbt__le__cs__iq__sample.md#a33dd41ba3b8027035bde1610c4a77a98)

int16\_t q

**Definition** cs.h:547

[bt\_le\_cs\_iq\_sample::i](structbt__le__cs__iq__sample.md#ab25db98b90a2f3c9a20a40efb1050c29)

int16\_t i

**Definition** cs.h:546

[bt\_le\_cs\_procedure\_enable\_param](structbt__le__cs__procedure__enable__param.md)

**Definition** cs.h:723

[bt\_le\_cs\_procedure\_enable\_param::enable](structbt__le__cs__procedure__enable__param.md#a01416dc5ed8f0315f050f76ce8ca3034)

enum bt\_conn\_le\_cs\_procedure\_enable\_state enable

**Definition** cs.h:725

[bt\_le\_cs\_procedure\_enable\_param::config\_id](structbt__le__cs__procedure__enable__param.md#aa776933876805f8e7074abbf47634ea4)

uint8\_t config\_id

**Definition** cs.h:724

[bt\_le\_cs\_set\_default\_settings\_param](structbt__le__cs__set__default__settings__param.md)

Default CS settings in the local Controller.

**Definition** cs.h:66

[bt\_le\_cs\_set\_default\_settings\_param::max\_tx\_power](structbt__le__cs__set__default__settings__param.md#a31a3b73d2bc44306f6905a2a1958b62b)

int8\_t max\_tx\_power

Maximum output power (Effective Isotropic Radiated Power) to be used for all CS transmissions.

**Definition** cs.h:80

[bt\_le\_cs\_set\_default\_settings\_param::cs\_sync\_antenna\_selection](structbt__le__cs__set__default__settings__param.md#a581ab5686e3eedfde84817d0ffcff587)

enum bt\_le\_cs\_sync\_antenna\_selection\_opt cs\_sync\_antenna\_selection

Antenna identifier to be used for CS\_SYNC packets by the local controller.

**Definition** cs.h:73

[bt\_le\_cs\_set\_default\_settings\_param::enable\_initiator\_role](structbt__le__cs__set__default__settings__param.md#a6a68056e10ea18ab2bb33202a39387a4)

bool enable\_initiator\_role

Enable CS initiator role.

**Definition** cs.h:68

[bt\_le\_cs\_set\_default\_settings\_param::enable\_reflector\_role](structbt__le__cs__set__default__settings__param.md#a7e532de60b09424da17be0e61dbafb2d)

bool enable\_reflector\_role

Enable CS reflector role.

**Definition** cs.h:70

[bt\_le\_cs\_set\_procedure\_parameters\_param](structbt__le__cs__set__procedure__parameters__param.md)

**Definition** cs.h:756

[bt\_le\_cs\_set\_procedure\_parameters\_param::max\_subevent\_len](structbt__le__cs__set__procedure__parameters__param.md#a0166c72225d70e7c1afc9cf9be613835)

uint32\_t max\_subevent\_len

**Definition** cs.h:778

[bt\_le\_cs\_set\_procedure\_parameters\_param::config\_id](structbt__le__cs__set__procedure__parameters__param.md#a03e8b91ccc78b02faed1864e6b4ad885)

uint8\_t config\_id

**Definition** cs.h:758

[bt\_le\_cs\_set\_procedure\_parameters\_param::snr\_control\_initiator](structbt__le__cs__set__procedure__parameters__param.md#a2fb81c447beb1238cb88610589458816)

enum bt\_le\_cs\_snr\_control snr\_control\_initiator

**Definition** cs.h:796

[bt\_le\_cs\_set\_procedure\_parameters\_param::tone\_antenna\_config\_selection](structbt__le__cs__set__procedure__parameters__param.md#a3f7c838bcfb9c0e3d7ad803aefdc33c4)

enum bt\_conn\_le\_cs\_tone\_antenna\_config\_selection tone\_antenna\_config\_selection

**Definition** cs.h:781

[bt\_le\_cs\_set\_procedure\_parameters\_param::max\_procedure\_count](structbt__le__cs__set__procedure__parameters__param.md#a7a00113e7849b604efc38d904fce0389)

uint16\_t max\_procedure\_count

**Definition** cs.h:772

[bt\_le\_cs\_set\_procedure\_parameters\_param::phy](structbt__le__cs__set__procedure__parameters__param.md#a7f42131c93874c0be297752d8103b585)

enum bt\_le\_cs\_procedure\_phy phy

**Definition** cs.h:784

[bt\_le\_cs\_set\_procedure\_parameters\_param::min\_procedure\_interval](structbt__le__cs__set__procedure__parameters__param.md#a967adc0e39da8e3ff96b998f3807542e)

uint16\_t min\_procedure\_interval

**Definition** cs.h:764

[bt\_le\_cs\_set\_procedure\_parameters\_param::max\_procedure\_len](structbt__le__cs__set__procedure__parameters__param.md#a9b28e4b6f887201ca7f2188b07d37e4c)

uint16\_t max\_procedure\_len

**Definition** cs.h:761

[bt\_le\_cs\_set\_procedure\_parameters\_param::preferred\_peer\_antenna](structbt__le__cs__set__procedure__parameters__param.md#aa1158161ee5e49217ad6a85b6c92d993)

uint8\_t preferred\_peer\_antenna

**Definition** cs.h:793

[bt\_le\_cs\_set\_procedure\_parameters\_param::snr\_control\_reflector](structbt__le__cs__set__procedure__parameters__param.md#ab053facc218a6566a31e33d0831d385f)

enum bt\_le\_cs\_snr\_control snr\_control\_reflector

**Definition** cs.h:799

[bt\_le\_cs\_set\_procedure\_parameters\_param::min\_subevent\_len](structbt__le__cs__set__procedure__parameters__param.md#ab45195cbf8021c861384ead2cedae8da)

uint32\_t min\_subevent\_len

**Definition** cs.h:775

[bt\_le\_cs\_set\_procedure\_parameters\_param::tx\_power\_delta](structbt__le__cs__set__procedure__parameters__param.md#abb995a318cf74ff7cbd8882ddfb155cc)

int8\_t tx\_power\_delta

**Definition** cs.h:790

[bt\_le\_cs\_set\_procedure\_parameters\_param::max\_procedure\_interval](structbt__le__cs__set__procedure__parameters__param.md#ac48eb6d0021c676738f17437fdcbc3e8)

uint16\_t max\_procedure\_interval

**Definition** cs.h:767

[bt\_le\_cs\_subevent\_step](structbt__le__cs__subevent__step.md)

Subevent result step.

**Definition** cs.h:533

[bt\_le\_cs\_subevent\_step::data\_len](structbt__le__cs__subevent__step.md#a32d2c13c5513220cf1cd7a13fb18c501)

uint8\_t data\_len

Length of role- and mode-specific information being reported.

**Definition** cs.h:539

[bt\_le\_cs\_subevent\_step::data](structbt__le__cs__subevent__step.md#a46494728a82c6d50f6acd8f88e1a0842)

const uint8\_t \* data

Pointer to role- and mode-specific information.

**Definition** cs.h:541

[bt\_le\_cs\_subevent\_step::channel](structbt__le__cs__subevent__step.md#a54b47ddae09d8ab3f57124f71c4efbca)

uint8\_t channel

CS step channel index.

**Definition** cs.h:537

[bt\_le\_cs\_subevent\_step::mode](structbt__le__cs__subevent__step.md#a82103efe7c897abdf5bbb9c0a23cfba4)

uint8\_t mode

CS step mode.

**Definition** cs.h:535

[bt\_le\_cs\_test\_cb](structbt__le__cs__test__cb.md)

Callbacks for CS Test.

**Definition** cs.h:522

[bt\_le\_cs\_test\_cb::le\_cs\_test\_subevent\_data\_available](structbt__le__cs__test__cb.md#a2a3ca580a3c3d55aa2f2323a318827f9)

void(\* le\_cs\_test\_subevent\_data\_available)(struct bt\_conn\_le\_cs\_subevent\_result \*data)

CS Test Subevent data.

**Definition** cs.h:527

[bt\_le\_cs\_test\_cb::le\_cs\_test\_end\_complete](structbt__le__cs__test__cb.md#a7da5731fb2ae9e7fc3cece78a7468663)

void(\* le\_cs\_test\_end\_complete)(void)

CS Test End Complete.

**Definition** cs.h:529

[bt\_le\_cs\_test\_param](structbt__le__cs__test__param.md)

CS Test parameters.

**Definition** cs.h:246

[bt\_le\_cs\_test\_param::t\_ip1\_time](structbt__le__cs__test__param.md#a02437a42f0c3e8563d1600b02e7ca517)

uint8\_t t\_ip1\_time

Interlude time in microseconds between the RTT packets.

**Definition** cs.h:305

[bt\_le\_cs\_test\_param::ss\_marker2\_position](structbt__le__cs__test__param.md#a093b0425d87266c9cb31c8dc209477ff)

uint8\_t ss\_marker2\_position

Bit number where the second marker in the channel sounding sequence starts.

**Definition** cs.h:442

[bt\_le\_cs\_test\_param::override\_config](structbt__le__cs__test__param.md#a0ac14a9e1055870ee33ef83e54c1a248)

uint16\_t override\_config

Override configuration.

**Definition** cs.h:382

[bt\_le\_cs\_test\_param::ss\_marker1\_position](structbt__le__cs__test__param.md#a1404de78072df4910a1823eadcb78cd1)

uint8\_t ss\_marker1\_position

Bit number where the first marker in the channel sounding sequence starts.

**Definition** cs.h:433

[bt\_le\_cs\_test\_param::subevent\_interval](structbt__le__cs__test__param.md#a1bff7f98cb72a9f73b0499b8fc89d262)

uint16\_t subevent\_interval

Gap between the start of two consecutive CS subevents (N \* 0.625 ms).

**Definition** cs.h:275

[bt\_le\_cs\_test\_param::not\_set](structbt__le__cs__test__param.md#a1c241926b6d1c57c1bde197c1fb37251)

struct bt\_le\_cs\_test\_param::@106321000344037342130355154251116277123014277104::@004161220363243147110117347275156307215315245046::@243256100044376016026157302016364131061162161002 not\_set

[bt\_le\_cs\_test\_param::t\_ip2\_time](structbt__le__cs__test__param.md#a1ce5f3400442ebdd8cf45f9db6367e58)

uint8\_t t\_ip2\_time

Interlude time in microseconds between the CS tones.

**Definition** cs.h:318

[bt\_le\_cs\_test\_param::main\_mode\_steps](structbt__le__cs__test__param.md#a1e92044ae3538cb71a9192ebcbd8c884)

uint8\_t main\_mode\_steps

**Definition** cs.h:406

[bt\_le\_cs\_test\_param::tone\_antenna\_permutation](structbt__le__cs__test__param.md#a22e2ec51e87887b74c8251fa004a4497)

enum bt\_le\_cs\_test\_override\_4\_tone\_antenna\_permutation tone\_antenna\_permutation

**Definition** cs.h:416

[bt\_le\_cs\_test\_param::cs\_sync\_aa\_initiator](structbt__le__cs__test__param.md#a355cdcf57dcafdfdc98959ec6b742cc1)

uint32\_t cs\_sync\_aa\_initiator

Access Address used in CS\_SYNC packets sent by the initiator.

**Definition** cs.h:422

[bt\_le\_cs\_test\_param::drbg\_nonce](structbt__le__cs__test__param.md#a3ba9bfaa63f144af3117233e7a7e3d3d)

uint16\_t drbg\_nonce

Determines octets 14 and 15 of the initial value of the DRBG nonce.

**Definition** cs.h:361

[bt\_le\_cs\_test\_param::override\_config\_4](structbt__le__cs__test__param.md#a40671e60cf8e1ff16e7389f6a24c9bb7)

struct bt\_le\_cs\_test\_param::@047036113353301246134147147240332273017103252272 override\_config\_4

Override config bit 4.

[bt\_le\_cs\_test\_param::cs\_sync\_phy](structbt__le__cs__test__param.md#a41c70c829d16299eb7d25029ddad01bb)

enum bt\_conn\_le\_cs\_sync\_phy cs\_sync\_phy

CS\_SYNC PHY.

**Definition** cs.h:263

[bt\_le\_cs\_test\_param::transmit\_power\_level](structbt__le__cs__test__param.md#a5951fa7f55752905a0180e8389c3d245)

uint8\_t transmit\_power\_level

Desired TX power level for the CS procedure.

**Definition** cs.h:292

[bt\_le\_cs\_test\_param::channel\_map\_repetition](structbt__le__cs__test__param.md#a5f0cefe32070be29bc918ff4f7a3a46d)

uint8\_t channel\_map\_repetition

Number of times the channels indicated by the channel map or channel field are cycled through for non...

**Definition** cs.h:389

[bt\_le\_cs\_test\_param::channel\_map](structbt__le__cs__test__param.md#a6092db75cfc8143d2e308fce87c18dfe)

uint8\_t channel\_map[10]

**Definition** cs.h:396

[bt\_le\_cs\_test\_param::override\_config\_2](structbt__le__cs__test__param.md#a63e8e44842b894bee57ffdcdee4f2cd0)

struct bt\_le\_cs\_test\_param::@003053364055242343147372322263347332311206206121 override\_config\_2

Override config bit 2.

[bt\_le\_cs\_test\_param::ch3c\_shape](structbt__le__cs__test__param.md#a656de42b2afb3d9c53899d3c4d6f3a88)

enum bt\_conn\_le\_cs\_ch3c\_shape ch3c\_shape

**Definition** cs.h:398

[bt\_le\_cs\_test\_param::sub\_mode](structbt__le__cs__test__param.md#a6b0ce9871c26b0a5c9c98a9339d234e1)

enum bt\_conn\_le\_cs\_sub\_mode sub\_mode

CS sub-mode to be used during the CS procedure.

**Definition** cs.h:250

[bt\_le\_cs\_test\_param::subevent\_len](structbt__le__cs__test__param.md#a78aeb8d6e7ac9565ea19a1ffd51ceb6a)

uint32\_t subevent\_len

CS subevent length in microseconds.

**Definition** cs.h:270

[bt\_le\_cs\_test\_param::role](structbt__le__cs__test__param.md#a797dda190cc01447054ee4dc08f2a332)

enum bt\_conn\_le\_cs\_role role

CS Test role.

**Definition** cs.h:259

[bt\_le\_cs\_test\_param::cs\_sync\_user\_payload](structbt__le__cs__test__param.md#a79ce15e5034572a4b5015240b7db4de5)

uint8\_t cs\_sync\_user\_payload[16]

User payload for CS\_SYNC packets.

**Definition** cs.h:464

[bt\_le\_cs\_test\_param::set](structbt__le__cs__test__param.md#a7eb22e2e410701b2baa5f7d9d7123721)

struct bt\_le\_cs\_test\_param::@106321000344037342130355154251116277123014277104::@004161220363243147110117347275156307215315245046::@201372320033151046366046151146151364345234303230 set

[bt\_le\_cs\_test\_param::override\_config\_0](structbt__le__cs__test__param.md#a802545d0c7f560166250d4ad585a7d80)

struct bt\_le\_cs\_test\_param::@106321000344037342130355154251116277123014277104 override\_config\_0

override config bit 0.

[bt\_le\_cs\_test\_param::mode\_0\_steps](structbt__le__cs__test__param.md#a84f346fafa174ba8b2acf33ff3db72eb)

uint8\_t mode\_0\_steps

Number of CS mode-0 steps at the beginning of the test CS subevent.

**Definition** cs.h:257

[bt\_le\_cs\_test\_param::t\_fcs\_time](structbt__le__cs__test__param.md#a8a2d1540e35d194729df373c79f9eaf2)

uint8\_t t\_fcs\_time

Time in microseconds for frequency changes.

**Definition** cs.h:333

[bt\_le\_cs\_test\_param::t\_pm\_time](structbt__le__cs__test__param.md#a8eb7e6fcf4431513404ac5f75da401a9)

uint8\_t t\_pm\_time

Time in microseconds for the phase measurement period of the CS tones.

**Definition** cs.h:341

[bt\_le\_cs\_test\_param::t\_pm\_tone\_ext](structbt__le__cs__test__param.md#a905f49912a99c105ce4087c4d3327deb)

enum bt\_le\_cs\_test\_override\_3\_pm\_tone\_ext t\_pm\_tone\_ext

**Definition** cs.h:411

[bt\_le\_cs\_test\_param::main\_mode](structbt__le__cs__test__param.md#a93e487780ffb55c66708bd6c3b293456)

enum bt\_conn\_le\_cs\_main\_mode main\_mode

CS mode to be used during the CS procedure.

**Definition** cs.h:248

[bt\_le\_cs\_test\_param::t\_sw\_time](structbt__le__cs__test__param.md#a94c3e1dcfb7290b61784c5dcd6a67531)

uint8\_t t\_sw\_time

Time in microseconds for the antenna switch period of the CS tones.

**Definition** cs.h:351

[bt\_le\_cs\_test\_param::override\_config\_7](structbt__le__cs__test__param.md#a9a2763c3062b2ee4d8a1d70393ed2aa2)

struct bt\_le\_cs\_test\_param::@007153217060260001262015051113223371162207350270 override\_config\_7

Override config bit 7.

[bt\_le\_cs\_test\_param::override\_config\_5](structbt__le__cs__test__param.md#a9bba99348c662adad1f16194409b2ae1)

struct bt\_le\_cs\_test\_param::@306174002367146332060336050126141102344263230035 override\_config\_5

Override config bit 5.

[bt\_le\_cs\_test\_param::initiator\_snr\_control](structbt__le__cs__test__param.md#aa58cf62583c83e32362216bc060a9a8e)

enum bt\_le\_cs\_snr\_control initiator\_snr\_control

Initiator SNR control options.

**Definition** cs.h:357

[bt\_le\_cs\_test\_param::reflector\_snr\_control](structbt__le__cs__test__param.md#aaa7305e11ee3e22b10b4ceb3c743d4e9)

enum bt\_le\_cs\_snr\_control reflector\_snr\_control

Reflector SNR control options.

**Definition** cs.h:359

[bt\_le\_cs\_test\_param::ch3c\_jump](structbt__le__cs__test__param.md#aac51c328149cce847057b913f2733198)

uint8\_t ch3c\_jump

**Definition** cs.h:399

[bt\_le\_cs\_test\_param::ss\_marker\_value](structbt__le__cs__test__param.md#aad705c92184ed8f1577bac68dc810373)

enum bt\_le\_cs\_test\_override\_7\_ss\_marker\_value ss\_marker\_value

Value of the Sounding Sequence marker.

**Definition** cs.h:448

[bt\_le\_cs\_test\_param::max\_num\_subevents](structbt__le__cs__test__param.md#aaf09c64fcfa1a0a4257d805ad9b49d56)

uint8\_t max\_num\_subevents

Maximum allowed number of subevents in the procedure.

**Definition** cs.h:280

[bt\_le\_cs\_test\_param::rtt\_type](structbt__le__cs__test__param.md#ab3af198a629e0fb082a177b6b482771a)

enum bt\_conn\_le\_cs\_rtt\_type rtt\_type

RTT variant.

**Definition** cs.h:261

[bt\_le\_cs\_test\_param::main\_mode\_repetition](structbt__le__cs__test__param.md#ac13c4390574bd9a540b632c3ee387870)

uint8\_t main\_mode\_repetition

Number of main mode steps taken from the end of the last CS subevent to be repeated at the beginning ...

**Definition** cs.h:255

[bt\_le\_cs\_test\_param::num\_channels](structbt__le__cs__test__param.md#acb2eed00edb4cac80ce097b241d8e1c8)

uint8\_t num\_channels

**Definition** cs.h:392

[bt\_le\_cs\_test\_param::cs\_sync\_payload\_pattern](structbt__le__cs__test__param.md#ace81aeaeefc788ccf6bb1b6c491ff0b2)

enum bt\_le\_cs\_test\_override\_8\_cs\_sync\_payload\_pattern cs\_sync\_payload\_pattern

CS\_SYNC payload pattern selection.

**Definition** cs.h:454

[bt\_le\_cs\_test\_param::channel\_selection\_type](structbt__le__cs__test__param.md#ad2f4775d56677c63ef1ff71c0d3bc08a)

enum bt\_conn\_le\_cs\_chsel\_type channel\_selection\_type

**Definition** cs.h:397

[bt\_le\_cs\_test\_param::cs\_sync\_aa\_reflector](structbt__le__cs__test__param.md#ad8ce97db93b0fbc267552db64491483a)

uint32\_t cs\_sync\_aa\_reflector

Access Address used in CS\_SYNC packets sent by the reflector.

**Definition** cs.h:424

[bt\_le\_cs\_test\_param::channels](structbt__le__cs__test__param.md#aeb66cc7b6744cd1709d6199d2ae2dc98)

uint8\_t \* channels

**Definition** cs.h:393

[bt\_le\_cs\_test\_param::cs\_sync\_antenna\_selection](structbt__le__cs__test__param.md#af26b66e0a28e4f3c6fce0dd5ad8a7606)

enum bt\_le\_cs\_test\_cs\_sync\_antenna\_selection cs\_sync\_antenna\_selection

Antenna identifier to be used for CS\_SYNC packets.

**Definition** cs.h:265

[bt\_le\_cs\_test\_param::override\_config\_6](structbt__le__cs__test__param.md#af4f16878d530ec19294673756e7b6358)

struct bt\_le\_cs\_test\_param::@152075077314110252106202146230153076061113246010 override\_config\_6

Override config bit 6.

[bt\_le\_cs\_test\_param::override\_config\_8](structbt__le__cs__test__param.md#afb85cec959d8bd59b560828af14dbced)

struct bt\_le\_cs\_test\_param::@340345041122346372210303127151130042323321312270 override\_config\_8

Override config bit 8.

[bt\_le\_cs\_test\_param::override\_config\_3](structbt__le__cs__test__param.md#afe036f2effcb41c9a4d888592916c329)

struct bt\_le\_cs\_test\_param::@342071114140363132331214214166215340132164011373 override\_config\_3

Override config bit 3.

[bt\_le\_cs\_test\_param::tone\_antenna\_config\_selection](structbt__le__cs__test__param.md#aff02c121f9c8ae63a137dbb19bf4acd2)

enum bt\_conn\_le\_cs\_tone\_antenna\_config\_selection tone\_antenna\_config\_selection

Antenna Configuration Index used during antenna switching during the tone phases of CS steps.

**Definition** cs.h:355

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** net\_buf.h:89

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [cs.h](cs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

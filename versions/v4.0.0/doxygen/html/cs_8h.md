---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/cs_8h.html
original_path: doxygen/html/cs_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cs.h File Reference

Bluetooth Channel Sounding handling.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/bluetooth/hci_types.h](hci__types_8h_source.md)>`  
`#include <[zephyr/bluetooth/conn.h](conn_8h_source.md)>`

[Go to the source code of this file.](cs_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_le\_cs\_set\_default\_settings\_param](structbt__le__cs__set__default__settings__param.md) |
|  | Default CS settings in the local Controller. [More...](structbt__le__cs__set__default__settings__param.md#details) |
| struct | [bt\_le\_cs\_test\_param](structbt__le__cs__test__param.md) |
|  | CS Test parameters. [More...](structbt__le__cs__test__param.md#details) |
| struct | [bt\_le\_cs\_create\_config\_params](structbt__le__cs__create__config__params.md) |
|  | CS Create Config params. [More...](structbt__le__cs__create__config__params.md#details) |
| struct | [bt\_le\_cs\_test\_cb](structbt__le__cs__test__cb.md) |
|  | Callbacks for CS Test. [More...](structbt__le__cs__test__cb.md#details) |
| struct | [bt\_le\_cs\_subevent\_step](structbt__le__cs__subevent__step.md) |
|  | Subevent result step. [More...](structbt__le__cs__subevent__step.md#details) |
| struct | [bt\_le\_cs\_iq\_sample](structbt__le__cs__iq__sample.md) |
|  | Sign-extended IQ value extracted from step data. [More...](structbt__le__cs__iq__sample.md#details) |
| struct | [bt\_le\_cs\_procedure\_enable\_param](structbt__le__cs__procedure__enable__param.md) |
| struct | [bt\_le\_cs\_set\_procedure\_parameters\_param](structbt__le__cs__set__procedure__parameters__param.md) |

| Macros | |
| --- | --- |
| #define | [BT\_LE\_CS\_CHANNEL\_BIT\_GET](group__bt__le__cs.md#ga95e2d24515e45096912440fe8a6bd3a0)(chmap, bit) |
|  | Macro for getting a specific channel bit in CS channel map. |
| #define | [BT\_LE\_CS\_CHANNEL\_BIT\_SET\_VAL](group__bt__le__cs.md#gadcd3351ef99d42e93c89d48f1c8ba668)(chmap, bit, val) |
|  | Macro for setting a specific channel bit value in CS channel map. |
| #define | [BT\_LE\_CS\_PROCEDURE\_PREFERRED\_PEER\_ANTENNA\_1](group__bt__le__cs.md#gaf278a44ad602ce7e365ac0d71bcc48b4)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [BT\_LE\_CS\_PROCEDURE\_PREFERRED\_PEER\_ANTENNA\_2](group__bt__le__cs.md#ga5ff36f6e97668a9d1b6ccd39492c68f7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [BT\_LE\_CS\_PROCEDURE\_PREFERRED\_PEER\_ANTENNA\_3](group__bt__le__cs.md#ga66ea3f214385c395e5f14ca80a0655b0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [BT\_LE\_CS\_PROCEDURE\_PREFERRED\_PEER\_ANTENNA\_4](group__bt__le__cs.md#gaa2c1c3d5e451df7ec58b4c8d3dedcf9a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |

| Enumerations | |
| --- | --- |
| enum | [bt\_le\_cs\_sync\_antenna\_selection\_opt](group__bt__le__cs.md#ga9f286cdeeee0e9df06e6b3df1e9ab643) {     [BT\_LE\_CS\_ANTENNA\_SELECTION\_OPT\_ONE](group__bt__le__cs.md#gga9f286cdeeee0e9df06e6b3df1e9ab643a5de14d0cc770615bd08c4e3d197bae90) = BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_ONE , [BT\_LE\_CS\_ANTENNA\_SELECTION\_OPT\_TWO](group__bt__le__cs.md#gga9f286cdeeee0e9df06e6b3df1e9ab643a7ce16e0eab20cf432c8e93a7f6be8ca5) = BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_TWO , [BT\_LE\_CS\_ANTENNA\_SELECTION\_OPT\_THREE](group__bt__le__cs.md#gga9f286cdeeee0e9df06e6b3df1e9ab643a35ae07887f3d55bcbd10d531f09c841d) = BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_THREE , [BT\_LE\_CS\_ANTENNA\_SELECTION\_OPT\_FOUR](group__bt__le__cs.md#gga9f286cdeeee0e9df06e6b3df1e9ab643aa5370917d0f46fe654ba42fbbd587ceb) = BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_FOUR ,     [BT\_LE\_CS\_ANTENNA\_SELECTION\_OPT\_REPETITIVE](group__bt__le__cs.md#gga9f286cdeeee0e9df06e6b3df1e9ab643aa23b552af8b16b1371f7a362089eaca7) = BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_REP , [BT\_LE\_CS\_ANTENNA\_SELECTION\_OPT\_NO\_RECOMMENDATION](group__bt__le__cs.md#gga9f286cdeeee0e9df06e6b3df1e9ab643a861f35bdbe322238bdad67568e5674f3) = BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_NONE   } |
| enum | [bt\_le\_cs\_test\_cs\_sync\_antenna\_selection](group__bt__le__cs.md#ga782a500f611320a6f3feed9897ab8e16) { [BT\_LE\_CS\_TEST\_CS\_SYNC\_ANTENNA\_SELECTION\_ONE](group__bt__le__cs.md#gga782a500f611320a6f3feed9897ab8e16a054f9b7f51323480106f11929425599f) = BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_ONE , [BT\_LE\_CS\_TEST\_CS\_SYNC\_ANTENNA\_SELECTION\_TWO](group__bt__le__cs.md#gga782a500f611320a6f3feed9897ab8e16aa1931403e835ab2e18982dd0f2a67803) = BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_TWO , [BT\_LE\_CS\_TEST\_CS\_SYNC\_ANTENNA\_SELECTION\_THREE](group__bt__le__cs.md#gga782a500f611320a6f3feed9897ab8e16aa059024bd3d90677ee00d4accd99f39c) = BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_THREE , [BT\_LE\_CS\_TEST\_CS\_SYNC\_ANTENNA\_SELECTION\_FOUR](group__bt__le__cs.md#gga782a500f611320a6f3feed9897ab8e16a678e1a8120f21f3707d4b9ea22bd8c47) = BT\_HCI\_OP\_LE\_CS\_ANTENNA\_SEL\_FOUR } |
|  | CS Test CS\_SYNC Antenna Identifier. [More...](group__bt__le__cs.md#ga782a500f611320a6f3feed9897ab8e16) |
| enum | [bt\_le\_cs\_initiator\_snr\_control](group__bt__le__cs.md#ga105e85b2839668f201cdf0cd76649c25) {     [BT\_LE\_CS\_INITIATOR\_SNR\_CONTROL\_18dB](group__bt__le__cs.md#gga105e85b2839668f201cdf0cd76649c25a6a1927592102a62e3ecf4360526c9f50) = BT\_HCI\_OP\_LE\_CS\_INITIATOR\_SNR\_18 , [BT\_LE\_CS\_INITIATOR\_SNR\_CONTROL\_21dB](group__bt__le__cs.md#gga105e85b2839668f201cdf0cd76649c25a3ef03bdb3e665f84d829f4060d1b27ac) = BT\_HCI\_OP\_LE\_CS\_INITIATOR\_SNR\_21 , [BT\_LE\_CS\_INITIATOR\_SNR\_CONTROL\_24dB](group__bt__le__cs.md#gga105e85b2839668f201cdf0cd76649c25a0a3cb13b419342e26be529db77444f42) = BT\_HCI\_OP\_LE\_CS\_INITIATOR\_SNR\_24 , [BT\_LE\_CS\_INITIATOR\_SNR\_CONTROL\_27dB](group__bt__le__cs.md#gga105e85b2839668f201cdf0cd76649c25a4bfe8b515d041202a9b4303bef3a97b9) = BT\_HCI\_OP\_LE\_CS\_INITIATOR\_SNR\_27 ,     [BT\_LE\_CS\_INITIATOR\_SNR\_CONTROL\_30dB](group__bt__le__cs.md#gga105e85b2839668f201cdf0cd76649c25a02a0baf0cd6c639f3d7d536ba0cb6bc0) = BT\_HCI\_OP\_LE\_CS\_INITIATOR\_SNR\_30 , [BT\_LE\_CS\_INITIATOR\_SNR\_CONTROL\_NOT\_USED](group__bt__le__cs.md#gga105e85b2839668f201cdf0cd76649c25aeecbde86761466bdbc48d24aed4e4e77) = BT\_HCI\_OP\_LE\_CS\_INITIATOR\_SNR\_NOT\_USED   } |
|  | CS Test Initiator SNR control options. [More...](group__bt__le__cs.md#ga105e85b2839668f201cdf0cd76649c25) |
| enum | [bt\_le\_cs\_reflector\_snr\_control](group__bt__le__cs.md#ga1195f68548bbda5a1fc567547768f3c1) {     [BT\_LE\_CS\_REFLECTOR\_SNR\_CONTROL\_18dB](group__bt__le__cs.md#gga1195f68548bbda5a1fc567547768f3c1ad8b150440aae1b8ab2015d4613584256) = BT\_HCI\_OP\_LE\_CS\_REFLECTOR\_SNR\_18 , [BT\_LE\_CS\_REFLECTOR\_SNR\_CONTROL\_21dB](group__bt__le__cs.md#gga1195f68548bbda5a1fc567547768f3c1af284e75c085e6bdd8fbe5dba7bc33d6d) = BT\_HCI\_OP\_LE\_CS\_REFLECTOR\_SNR\_21 , [BT\_LE\_CS\_REFLECTOR\_SNR\_CONTROL\_24dB](group__bt__le__cs.md#gga1195f68548bbda5a1fc567547768f3c1a73ef8c87df55662275331435a89394ec) = BT\_HCI\_OP\_LE\_CS\_REFLECTOR\_SNR\_24 , [BT\_LE\_CS\_REFLECTOR\_SNR\_CONTROL\_27dB](group__bt__le__cs.md#gga1195f68548bbda5a1fc567547768f3c1a3b0fc640e6cc044bd246f29f2c426d46) = BT\_HCI\_OP\_LE\_CS\_REFLECTOR\_SNR\_27 ,     [BT\_LE\_CS\_REFLECTOR\_SNR\_CONTROL\_30dB](group__bt__le__cs.md#gga1195f68548bbda5a1fc567547768f3c1a7d37f5ddbc26c43ae094705b38021dd2) = BT\_HCI\_OP\_LE\_CS\_REFLECTOR\_SNR\_30 , [BT\_LE\_CS\_REFLECTOR\_SNR\_CONTROL\_NOT\_USED](group__bt__le__cs.md#gga1195f68548bbda5a1fc567547768f3c1a7d3cef632135ef86e2f684ea4160cc21) = BT\_HCI\_OP\_LE\_CS\_REFLECTOR\_SNR\_NOT\_USED   } |
|  | CS Test Reflector SNR control options. [More...](group__bt__le__cs.md#ga1195f68548bbda5a1fc567547768f3c1) |
| enum | [bt\_le\_cs\_test\_override\_3\_pm\_tone\_ext](group__bt__le__cs.md#gaf50910d51c69e216ef6eb22b5c0f2d28) {     [BT\_LE\_CS\_TEST\_OVERRIDE\_3\_NO\_TONE\_EXT](group__bt__le__cs.md#ggaf50910d51c69e216ef6eb22b5c0f2d28aa5f4fea24a1b27736cfc36c470a3a008) = BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_NONE , [BT\_LE\_CS\_TEST\_OVERRIDE\_3\_INITIATOR\_TONE\_EXT\_ONLY](group__bt__le__cs.md#ggaf50910d51c69e216ef6eb22b5c0f2d28aee2c022be115a4c865d5524795f2d039) = BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_INIT , [BT\_LE\_CS\_TEST\_OVERRIDE\_3\_REFLECTOR\_TONE\_EXT\_ONLY](group__bt__le__cs.md#ggaf50910d51c69e216ef6eb22b5c0f2d28ab504c3a24b36413ea2395bd579e5bba2) = BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_REFL , [BT\_LE\_CS\_TEST\_OVERRIDE\_3\_INITIATOR\_AND\_REFLECTOR\_TONE\_EXT](group__bt__le__cs.md#ggaf50910d51c69e216ef6eb22b5c0f2d28ad2b323c3c54409545458c08fc6660cf4) ,     [BT\_LE\_CS\_TEST\_OVERRIDE\_3\_REPETITIVE\_TONE\_EXT](group__bt__le__cs.md#ggaf50910d51c69e216ef6eb22b5c0f2d28a9a691cb7b4a9cff799d848fc79cf40dd) = BT\_HCI\_OP\_LE\_CS\_TEST\_TONE\_EXT\_REPEAT   } |
|  | CS Test Override 3 T\_PM Tone Extension. [More...](group__bt__le__cs.md#gaf50910d51c69e216ef6eb22b5c0f2d28) |
| enum | [bt\_le\_cs\_test\_override\_4\_tone\_antenna\_permutation](group__bt__le__cs.md#ga1ba4d7d919cb5c09469f8e8aa05bb04d) {     [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_00](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da72b3c5a4d07ae3c73e9bb131c725d17f) = BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_00 , [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_01](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da7aed472d8ed1b3fc84e89531134fc71c) = BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_01 , [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_02](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dab986f2c0c54de93cfdf5a5334aafffb2) = BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_02 , [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_03](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da7731f27f1af37ba740764e9875d28482) = BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_03 ,     [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_04](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da3fe0da05e9c2493af3ea42a0c6cd4b17) = BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_04 , [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_05](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04daa73b01369a29b4ea7de2aadb71efe699) = BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_05 , [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_06](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dae4f815603cdffeb82711b994be2209dc) = BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_06 , [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_07](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da28e1b78a9bb927c4d38047e2aed57a15) = BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_07 ,     [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_08](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dab1cbcd7ceb33fb13b7d70b0dc671849c) = BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_08 , [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_09](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dae7f0fedfabe1748f9918befedbc45944) = BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_09 , [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_10](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da2ac77dab1caf34f436075dab45cc4aea) = BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_10 , [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_11](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dad85a40214189a9c036c95d88fb752a0c) = BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_11 ,     [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_12](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da45f979b88a3d63c4f270d246c98f3b53) = BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_12 , [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_13](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da2b34111edb7b0b1412de7d4485cbc164) = BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_13 , [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_14](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da5ab31e2b89fef73d838ade33de5d770b) = BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_14 , [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_15](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da144a6190783b1fbc5ccde1b9f0ec3581) = BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_15 ,     [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_16](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dae87750d18c24ddcece72919e107da671) = BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_16 , [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_17](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dabe494d770af056108d4679364a93acce) = BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_17 , [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_18](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04daad5f0f4d2818f986472f8cca57b37ea9) = BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_18 , [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_19](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dac02f9fa05c0f35bb306fde66bc80ab21) = BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_19 ,     [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_20](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dad355ee587eff65a2a2f80274fc6c5081) = BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_20 , [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_21](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da3cc8b9dfadae103bdbb0fb79c523f553) = BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_21 , [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_22](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dadf2778f065f696ad43ceca71aa6a8a80) = BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_22 , [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_23](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04dac3a263bfe1f80c38647d6aeab42b12c3) = BT\_HCI\_OP\_LE\_CS\_TEST\_AP\_INDEX\_23 ,     [BT\_LE\_CS\_TEST\_OVERRIDE\_4\_ANTENNA\_PERMUTATION\_INDEX\_LOOP](group__bt__le__cs.md#gga1ba4d7d919cb5c09469f8e8aa05bb04da2abd10e7d80703b3d849ad19d65af31f)   } |
|  | CS Test Override 4 Tone Antenna Permutation. [More...](group__bt__le__cs.md#ga1ba4d7d919cb5c09469f8e8aa05bb04d) |
| enum | [bt\_le\_cs\_test\_override\_7\_ss\_marker\_value](group__bt__le__cs.md#gacb3f437225ad1d6320ee424c39ebc82a) { [BT\_LE\_CS\_TEST\_OVERRIDE\_7\_SS\_MARKER\_VAL\_0011](group__bt__le__cs.md#ggacb3f437225ad1d6320ee424c39ebc82aa99a26684d34169d062150f61cb0ba889) = BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_VAL\_0011 , [BT\_LE\_CS\_TEST\_OVERRIDE\_7\_SS\_MARKER\_VAL\_1100](group__bt__le__cs.md#ggacb3f437225ad1d6320ee424c39ebc82aa6b6bc126c5e2a97de33d6c83230ebb92) = BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_VAL\_1100 , [BT\_LE\_CS\_TEST\_OVERRIDE\_7\_SS\_MARKER\_VAL\_LOOP](group__bt__le__cs.md#ggacb3f437225ad1d6320ee424c39ebc82aa3a3078691c778d1c7a30fe9400bc5f0f) = BT\_HCI\_OP\_LE\_CS\_TEST\_SS\_MARKER\_VAL\_LOOP } |
|  | CS Test Override 7 Sounding Sequence Marker Value. [More...](group__bt__le__cs.md#gacb3f437225ad1d6320ee424c39ebc82a) |
| enum | [bt\_le\_cs\_test\_override\_8\_cs\_sync\_payload\_pattern](group__bt__le__cs.md#ga731bbaa98dab7c88725fc64b66da62eb) {     [BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_PRBS9](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62eba3c8bc2a6858dc2d0de02b3b681a854a0) = BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_PRBS9 , [BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_11110000](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62eba109f2588e566b9651b67dbbf9583813c) = BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_11110000 , [BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_10101010](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62ebaef4b4455b236d70fae6a0138050d0835) = BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_10101010 , [BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_PRBS15](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62eba1b910950b96ad0b47b0b235a2e8e45c8) = BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_PRBS15 ,     [BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_11111111](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62ebabc520467cdbaaf34d0c815e0d62bd097) = BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_11111111 , [BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_00000000](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62eba1b46b8b073ca599cb89d86b261fa4dd5) = BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_00000000 , [BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_00001111](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62eba4f4ec5a6d46734e8c5801e9e79535b70) = BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_00001111 , [BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_01010101](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62eba6c59258c52a5889e0b11aa0fb0f99bcb) = BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_01010101 ,     [BT\_LE\_CS\_TEST\_OVERRIDE\_8\_PAYLOAD\_PATTERN\_USER](group__bt__le__cs.md#gga731bbaa98dab7c88725fc64b66da62ebaf68334f70d91d587e906533ad544fef1) = BT\_HCI\_OP\_LE\_CS\_TEST\_PAYLOAD\_USER   } |
|  | CS Test Override 8 CS\_SYNC Payload Pattern. [More...](group__bt__le__cs.md#ga731bbaa98dab7c88725fc64b66da62eb) |
| enum | [bt\_le\_cs\_create\_config\_context](group__bt__le__cs.md#ga22822b2dd21d64c8c64a66f2b5dee9b1) { [BT\_LE\_CS\_CREATE\_CONFIG\_CONTEXT\_LOCAL\_ONLY](group__bt__le__cs.md#gga22822b2dd21d64c8c64a66f2b5dee9b1adb8a8af222fed7262bdb57bc4f18a706) , [BT\_LE\_CS\_CREATE\_CONFIG\_CONTEXT\_LOCAL\_AND\_REMOTE](group__bt__le__cs.md#gga22822b2dd21d64c8c64a66f2b5dee9b1ae5107dfa011451ecaa404906fabc41e4) } |
|  | CS config creation context. [More...](group__bt__le__cs.md#ga22822b2dd21d64c8c64a66f2b5dee9b1) |
| enum | [bt\_le\_cs\_procedure\_phy](group__bt__le__cs.md#ga9e008daa9c0c1702aa3b4479e7a37ca4) { [BT\_LE\_CS\_PROCEDURE\_PHY\_1M](group__bt__le__cs.md#gga9e008daa9c0c1702aa3b4479e7a37ca4aa1dcc1e15aac59898c0a6c229593a76b) = BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_1M , [BT\_LE\_CS\_PROCEUDRE\_PHY\_2M](group__bt__le__cs.md#gga9e008daa9c0c1702aa3b4479e7a37ca4a571652b572ff8439a51515b065f63c5b) = BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_2M , [BT\_LE\_CS\_PROCEDURE\_PHY\_CODED\_S8](group__bt__le__cs.md#gga9e008daa9c0c1702aa3b4479e7a37ca4a1ceb33afa661774e1077caced63bf263) = BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_CODED\_S8 , [BT\_LE\_CS\_PROCEDURE\_PHY\_CODED\_S2](group__bt__le__cs.md#gga9e008daa9c0c1702aa3b4479e7a37ca4a5370237bdbceb37a631425f472ddc322) = BT\_HCI\_OP\_LE\_CS\_PROCEDURE\_PHY\_CODED\_S2 } |

| Functions | |
| --- | --- |
| struct [bt\_le\_cs\_iq\_sample](structbt__le__cs__iq__sample.md) | [bt\_le\_cs\_parse\_pct](group__bt__le__cs.md#gaf99d82194bbcc471c3de2094b39a2201) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pct[3]) |
|  | Extract in-phase and quadrature terms from HCI-formatted PCT. |
| void | [bt\_le\_cs\_set\_valid\_chmap\_bits](group__bt__le__cs.md#gaa979dc080cf277a2382b6ba77f8a1c09) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel\_map[10]) |
|  | Set all valid channel map bits. |
| int | [bt\_le\_cs\_read\_remote\_supported\_capabilities](group__bt__le__cs.md#gadb3afd94cd11d035cfe34c6a63b37b19) (struct bt\_conn \*conn) |
|  | Read Remote Supported Capabilities. |
| int | [bt\_le\_cs\_set\_default\_settings](group__bt__le__cs.md#ga6ee9b8fa52b96dce41b1c879865fa938) (struct bt\_conn \*conn, const struct [bt\_le\_cs\_set\_default\_settings\_param](structbt__le__cs__set__default__settings__param.md) \*params) |
|  | Set Channel Sounding default settings. |
| int | [bt\_le\_cs\_read\_remote\_fae\_table](group__bt__le__cs.md#ga127034536a98743d359c749fe7c79dba) (struct bt\_conn \*conn) |
|  | Read Remote FAE Table. |
| int | [bt\_le\_cs\_test\_cb\_register](group__bt__le__cs.md#gaf03c4ed5c7e179ee3b374efa857188e2) (struct [bt\_le\_cs\_test\_cb](structbt__le__cs__test__cb.md) cs\_test\_cb) |
|  | Register callbacks for the CS Test mode. |
| int | [bt\_le\_cs\_start\_test](group__bt__le__cs.md#gada91ff7c7a82620d77bf78781ebea356) (const struct [bt\_le\_cs\_test\_param](structbt__le__cs__test__param.md) \*params) |
|  | Start a CS test. |
| int | [bt\_le\_cs\_create\_config](group__bt__le__cs.md#ga27bae87f9769a2d5802c57adfa201b23) (struct bt\_conn \*conn, struct [bt\_le\_cs\_create\_config\_params](structbt__le__cs__create__config__params.md) \*params, enum [bt\_le\_cs\_create\_config\_context](group__bt__le__cs.md#ga22822b2dd21d64c8c64a66f2b5dee9b1) context) |
|  | Create CS configuration. |
| int | [bt\_le\_cs\_remove\_config](group__bt__le__cs.md#ga2a27b80e72ff2bfe986b3cbe11f225f3) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) config\_id) |
|  | Create CS configuration. |
| int | [bt\_le\_cs\_stop\_test](group__bt__le__cs.md#ga4742baeb1eb46969233f787344cb5e11) (void) |
|  | Stop ongoing CS Test. |
| void | [bt\_le\_cs\_step\_data\_parse](group__bt__le__cs.md#gadcd85f3799f4219a01e84fc281ff1a31) (struct [net\_buf\_simple](structnet__buf__simple.md) \*step\_data\_buf, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\*func)(struct [bt\_le\_cs\_subevent\_step](structbt__le__cs__subevent__step.md) \*step, void \*user\_data), void \*user\_data) |
|  | Parse CS Subevent Step Data. |
| int | [bt\_le\_cs\_security\_enable](group__bt__le__cs.md#ga346a46dc3321c5bab034904bf09aa4e3) (struct bt\_conn \*conn) |
|  | CS Security Enable. |
| int | [bt\_le\_cs\_procedure\_enable](group__bt__le__cs.md#ga2b6f3c3795b5eeb424542c1858f84cbc) (struct bt\_conn \*conn, const struct [bt\_le\_cs\_procedure\_enable\_param](structbt__le__cs__procedure__enable__param.md) \*params) |
|  | CS Procedure Enable. |
| int | [bt\_le\_cs\_set\_procedure\_parameters](group__bt__le__cs.md#gad6e0fb9c7f92678598d9780b78710961) (struct bt\_conn \*conn, const struct [bt\_le\_cs\_set\_procedure\_parameters\_param](structbt__le__cs__set__procedure__parameters__param.md) \*params) |
|  | CS Set Procedure Parameters. |
| int | [bt\_le\_cs\_set\_channel\_classification](group__bt__le__cs.md#gafcd6a882c0da413bfef5a56e53323389) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel\_classification[10]) |
|  | CS Set Channel Classification. |
| int | [bt\_le\_cs\_read\_local\_supported\_capabilities](group__bt__le__cs.md#gaa49ff6e8340bd1753485deeec8036d1b) (struct [bt\_conn\_le\_cs\_capabilities](structbt__conn__le__cs__capabilities.md) \*ret) |
|  | CS Read Local Supported Capabilities. |
| int | [bt\_le\_cs\_write\_cached\_remote\_supported\_capabilities](group__bt__le__cs.md#ga9d4b5b21886f0dd89b4073acaaa787a1) (struct bt\_conn \*conn, const struct [bt\_conn\_le\_cs\_capabilities](structbt__conn__le__cs__capabilities.md) \*params) |
|  | CS Write Cached Remote Supported Capabilities. |
| int | [bt\_le\_cs\_write\_cached\_remote\_fae\_table](group__bt__le__cs.md#ga97dac4af57b2d6cefe478c1c07dffcca) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) remote\_fae\_table[72]) |
|  | CS Write Cached Remote FAE Table. |

## Detailed Description

Bluetooth Channel Sounding handling.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [cs.h](cs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

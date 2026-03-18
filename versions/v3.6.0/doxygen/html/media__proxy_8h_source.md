---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/media__proxy_8h_source.html
original_path: doxygen/html/media__proxy_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

media\_proxy.h

[Go to the documentation of this file.](media__proxy_8h.md)

1/\*

2 \* Copyright (c) 2019 - 2021 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_MEDIA\_PROXY\_H\_

8#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_MEDIA\_PROXY\_H\_

9

38

39#include <[stdint.h](stdint_8h.md)>

40#include <[stdbool.h](stdbool_8h.md)>

41

42#include <[zephyr/bluetooth/bluetooth.h](bluetooth_8h.md)>

43

44/\* TODO: Remove dependency on mcs.h \*/

45#include "[mcs.h](mcs_8h.md)"

46

47#ifdef \_\_cplusplus

48extern "C" {

49#endif

50

51

[ 55](structmpl__cmd.md)struct [mpl\_cmd](structmpl__cmd.md) {

[ 56](structmpl__cmd.md#a5cb29ca9e5a6b8249c69cc975b345e2f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [opcode](structmpl__cmd.md#a5cb29ca9e5a6b8249c69cc975b345e2f);

[ 57](structmpl__cmd.md#aca5e50b9f883a3c81f10ad51032a31f9) bool [use\_param](structmpl__cmd.md#aca5e50b9f883a3c81f10ad51032a31f9);

[ 58](structmpl__cmd.md#ade5ed4d0ff2aeb192b8ed6b586c9bc9e) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [param](structmpl__cmd.md#ade5ed4d0ff2aeb192b8ed6b586c9bc9e);

59};

60

[ 64](structmpl__cmd__ntf.md)struct [mpl\_cmd\_ntf](structmpl__cmd__ntf.md) {

[ 65](structmpl__cmd__ntf.md#adcd5228cef8b7629d54053b155a91aa7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [requested\_opcode](structmpl__cmd__ntf.md#adcd5228cef8b7629d54053b155a91aa7);

[ 66](structmpl__cmd__ntf.md#a776bd9459d320e609697905067c0b284) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [result\_code](structmpl__cmd__ntf.md#a776bd9459d320e609697905067c0b284);

67};

68

[ 72](structmpl__sci.md)struct [mpl\_sci](structmpl__sci.md) {

[ 73](structmpl__sci.md#a348314407c7b46d5ed583b97dfe932bc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structmpl__sci.md#a348314407c7b46d5ed583b97dfe932bc);

[ 74](structmpl__sci.md#a1dfc87f7e8b509ca05cbcd97a245953f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structmpl__sci.md#a1dfc87f7e8b509ca05cbcd97a245953f);

[ 75](structmpl__sci.md#abcb13d8005212f480eaaf8a8296f6023) char [param](structmpl__sci.md#abcb13d8005212f480eaaf8a8296f6023)[[SEARCH\_PARAM\_MAX](group__bt__mcs.md#ga81665fd87487cbaf1c0f90f1e0b2126a)];

76};

77

[ 81](structmpl__search.md)struct [mpl\_search](structmpl__search.md) {

[ 82](structmpl__search.md#a9b9c64d3d9a25951da58ebf47bb63617) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structmpl__search.md#a9b9c64d3d9a25951da58ebf47bb63617);

[ 83](structmpl__search.md#aa2332c1802786e2ef0486ede1c3a24c7) char [search](structmpl__search.md#aa2332c1802786e2ef0486ede1c3a24c7)[[SEARCH\_LEN\_MAX](group__bt__mcs.md#gaf771b17acd202a20450b6ea939ddee3b)]; /\* Concatenated search control items \*/

84}; /\* - (type, length, param) \*/

85

[ 91](group__bt__media__proxy.md#ga61732644eecad1442d5cedbda8f8cc08)#define MEDIA\_PROXY\_PLAYBACK\_SPEED\_MIN -128

[ 92](group__bt__media__proxy.md#ga5462f8d5ce98cc33a131b2e7b5548c41)#define MEDIA\_PROXY\_PLAYBACK\_SPEED\_QUARTER -128

[ 93](group__bt__media__proxy.md#ga4c765363c2a5b0d9800864859746ae33)#define MEDIA\_PROXY\_PLAYBACK\_SPEED\_HALF -64

[ 94](group__bt__media__proxy.md#ga6d8854bd54dcbb657f0ba545ec231368)#define MEDIA\_PROXY\_PLAYBACK\_SPEED\_UNITY 0

[ 95](group__bt__media__proxy.md#gaa53d906340c0b2adb314945f5299464e)#define MEDIA\_PROXY\_PLAYBACK\_SPEED\_DOUBLE 64

[ 96](group__bt__media__proxy.md#gaaccc9d75f96b5fe2de101b119a516d36)#define MEDIA\_PROXY\_PLAYBACK\_SPEED\_MAX 127

97

[ 105](group__bt__media__proxy.md#gaa6aa7a6e98631152b4bd77b60c78d58a)#define MEDIA\_PROXY\_SEEKING\_SPEED\_FACTOR\_MAX 64

[ 106](group__bt__media__proxy.md#ga67c1069fa01425ad6cd8f36438b71826)#define MEDIA\_PROXY\_SEEKING\_SPEED\_FACTOR\_MIN 4

[ 107](group__bt__media__proxy.md#ga58495e58bf84235efcee89289fc992c2)#define MEDIA\_PROXY\_SEEKING\_SPEED\_FACTOR\_ZERO 0

108

[ 112](group__bt__media__proxy.md#ga8e721b49c361d2395bd8eb740d43e282)#define MEDIA\_PROXY\_PLAYING\_ORDER\_SINGLE\_ONCE 0x01

[ 113](group__bt__media__proxy.md#gadf5f0c15cb88cd92f49db1b57dbd2c18)#define MEDIA\_PROXY\_PLAYING\_ORDER\_SINGLE\_REPEAT 0x02

[ 114](group__bt__media__proxy.md#ga63055a150b93f06e076b97abb6f6f682)#define MEDIA\_PROXY\_PLAYING\_ORDER\_INORDER\_ONCE 0x03

[ 115](group__bt__media__proxy.md#ga437068b9d90404cc68d41faaedfac9a8)#define MEDIA\_PROXY\_PLAYING\_ORDER\_INORDER\_REPEAT 0x04

[ 116](group__bt__media__proxy.md#ga48a33dd8fbb8a8ab162c18bc0e9b7531)#define MEDIA\_PROXY\_PLAYING\_ORDER\_OLDEST\_ONCE 0x05

[ 117](group__bt__media__proxy.md#ga63a33c4e3267ab39ab5892fb5b0bbe89)#define MEDIA\_PROXY\_PLAYING\_ORDER\_OLDEST\_REPEAT 0x06

[ 118](group__bt__media__proxy.md#gac344111e2b043cdfbcb9ac272622b16f)#define MEDIA\_PROXY\_PLAYING\_ORDER\_NEWEST\_ONCE 0x07

[ 119](group__bt__media__proxy.md#gaf10b815dc579dc67b1f092e0a85c51d9)#define MEDIA\_PROXY\_PLAYING\_ORDER\_NEWEST\_REPEAT 0x08

[ 120](group__bt__media__proxy.md#gae152374af5d567cf65d6d7b236b792a4)#define MEDIA\_PROXY\_PLAYING\_ORDER\_SHUFFLE\_ONCE 0x09

[ 121](group__bt__media__proxy.md#ga45161ec08b67e4d3bd59efa45027f3aa)#define MEDIA\_PROXY\_PLAYING\_ORDER\_SHUFFLE\_REPEAT 0x0a

122

[ 129](group__bt__media__proxy.md#ga55b5a00ea9ec849e7c495463e5f1869d)#define MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_SINGLE\_ONCE BIT(0)

[ 130](group__bt__media__proxy.md#ga465a82ace21a0e88356eccaf038f58e9)#define MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_SINGLE\_REPEAT BIT(1)

[ 131](group__bt__media__proxy.md#ga8fee464b8e17fffc4361972df15062af)#define MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_INORDER\_ONCE BIT(2)

[ 132](group__bt__media__proxy.md#ga7faeff14de245ea670ca447b0adc4820)#define MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_INORDER\_REPEAT BIT(3)

[ 133](group__bt__media__proxy.md#gae3d848fc0b9117fe9bc51327627ac635)#define MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_OLDEST\_ONCE BIT(4)

[ 134](group__bt__media__proxy.md#ga7fa415d845dd1fefc8bdb74532878131)#define MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_OLDEST\_REPEAT BIT(5)

[ 135](group__bt__media__proxy.md#ga334f9e16ea7a52bfb6357ad619e3601b)#define MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_NEWEST\_ONCE BIT(6)

[ 136](group__bt__media__proxy.md#gaaf5f08e2dd624e2bb1bd9b72ab4b2b33)#define MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_NEWEST\_REPEAT BIT(7)

[ 137](group__bt__media__proxy.md#ga3e998cda3e91f1c9fbb8496a748bcf12)#define MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_SHUFFLE\_ONCE BIT(8)

[ 138](group__bt__media__proxy.md#ga4f0689fe1fc0ac2b3f9b9ef4ed1afb8b)#define MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_SHUFFLE\_REPEAT BIT(9)

139

[ 143](group__bt__media__proxy.md#gab8c465e0e63898e53c39171b89d668c9)#define MEDIA\_PROXY\_STATE\_INACTIVE 0x00

[ 144](group__bt__media__proxy.md#ga1967c76b290f1d20515740cf7139f49c)#define MEDIA\_PROXY\_STATE\_PLAYING 0x01

[ 145](group__bt__media__proxy.md#ga85325d7ff75ec05275a875d7d5540a6c)#define MEDIA\_PROXY\_STATE\_PAUSED 0x02

[ 146](group__bt__media__proxy.md#gaa207ee7666ab18c40e5b1d2a6ed7f034)#define MEDIA\_PROXY\_STATE\_SEEKING 0x03

[ 147](group__bt__media__proxy.md#gab0c8f3510109f18ef6445f035b27cbe9)#define MEDIA\_PROXY\_STATE\_LAST 0x04

148

[ 152](group__bt__media__proxy.md#gadd400bc6900abe1956d4de4efb212683)#define MEDIA\_PROXY\_OP\_PLAY 0x01

[ 153](group__bt__media__proxy.md#ga69bcb42294e8cd1eb062bbe19399a3df)#define MEDIA\_PROXY\_OP\_PAUSE 0x02

[ 154](group__bt__media__proxy.md#gabc2b497b95728325208e28db6d5cf4f8)#define MEDIA\_PROXY\_OP\_FAST\_REWIND 0x03

[ 155](group__bt__media__proxy.md#gac0c0730bcf6592c5d2c61d21d09efb2b)#define MEDIA\_PROXY\_OP\_FAST\_FORWARD 0x04

[ 156](group__bt__media__proxy.md#gaf3707d44c7a3305ba896c0257b2109b3)#define MEDIA\_PROXY\_OP\_STOP 0x05

157

[ 158](group__bt__media__proxy.md#gaceb240f7f21074b6b7f9ed1e9d645cb0)#define MEDIA\_PROXY\_OP\_MOVE\_RELATIVE 0x10

159

[ 160](group__bt__media__proxy.md#ga7846fa5da200e0d921056b410e60677e)#define MEDIA\_PROXY\_OP\_PREV\_SEGMENT 0x20

[ 161](group__bt__media__proxy.md#gada5e3114b2b00f4ea27adf884f49429e)#define MEDIA\_PROXY\_OP\_NEXT\_SEGMENT 0x21

[ 162](group__bt__media__proxy.md#gac2e5c8e2cadd05092fa186f05ae74e57)#define MEDIA\_PROXY\_OP\_FIRST\_SEGMENT 0x22

[ 163](group__bt__media__proxy.md#ga3f317208b9d8495c498325a4d37d41ad)#define MEDIA\_PROXY\_OP\_LAST\_SEGMENT 0x23

[ 164](group__bt__media__proxy.md#gab3bbf7eb7c562bc6a5148c75eb99ada5)#define MEDIA\_PROXY\_OP\_GOTO\_SEGMENT 0x24

165

[ 166](group__bt__media__proxy.md#ga1b7db568fc3153c29ed4e951d95bee8e)#define MEDIA\_PROXY\_OP\_PREV\_TRACK 0x30

[ 167](group__bt__media__proxy.md#gaae4cc32663f02bf96d1dcbbc8453e40b)#define MEDIA\_PROXY\_OP\_NEXT\_TRACK 0x31

[ 168](group__bt__media__proxy.md#ga5c272e2e9b24ce92a7df7373d1b002cc)#define MEDIA\_PROXY\_OP\_FIRST\_TRACK 0x32

[ 169](group__bt__media__proxy.md#ga72614d9a2fa4c938f1c7055bc219c8bc)#define MEDIA\_PROXY\_OP\_LAST\_TRACK 0x33

[ 170](group__bt__media__proxy.md#gaf2f100d41413b14c5dbd8f2641a13bb0)#define MEDIA\_PROXY\_OP\_GOTO\_TRACK 0x34

171

[ 172](group__bt__media__proxy.md#gae15386adcfe1c5ca56eac7d0292dffd0)#define MEDIA\_PROXY\_OP\_PREV\_GROUP 0x40

[ 173](group__bt__media__proxy.md#ga3cf10acf1ef8b7d3252eb37cb4e35f97)#define MEDIA\_PROXY\_OP\_NEXT\_GROUP 0x41

[ 174](group__bt__media__proxy.md#ga5eb0a22c257e370cd76d73f7fa9e342c)#define MEDIA\_PROXY\_OP\_FIRST\_GROUP 0x42

[ 175](group__bt__media__proxy.md#gaa6ac8f8bf674c0ffec22bd061e9be3dc)#define MEDIA\_PROXY\_OP\_LAST\_GROUP 0x43

[ 176](group__bt__media__proxy.md#ga139d2ced243a6ff47d8335583974a0da)#define MEDIA\_PROXY\_OP\_GOTO\_GROUP 0x44

177

[ 181](group__bt__media__proxy.md#ga22c2599cd62a263a01c06c9bd9fff054)#define MEDIA\_PROXY\_OPCODES\_SUPPORTED\_LEN 4

182

[ 186](group__bt__media__proxy.md#gafe30bb1287b9a44655d76364d4832eac)#define MEDIA\_PROXY\_OP\_SUP\_PLAY BIT(0)

[ 187](group__bt__media__proxy.md#gaec37a692c28ca90c8053db9de2a6c44f)#define MEDIA\_PROXY\_OP\_SUP\_PAUSE BIT(1)

[ 188](group__bt__media__proxy.md#ga99952473bafd76f6ceaf141307510f28)#define MEDIA\_PROXY\_OP\_SUP\_FAST\_REWIND BIT(2)

[ 189](group__bt__media__proxy.md#ga05453105bc3d1579110e908b794e3ac5)#define MEDIA\_PROXY\_OP\_SUP\_FAST\_FORWARD BIT(3)

[ 190](group__bt__media__proxy.md#ga060ff676a0b2f249a26aaf61147b68e8)#define MEDIA\_PROXY\_OP\_SUP\_STOP BIT(4)

191

[ 192](group__bt__media__proxy.md#ga03c393a29c68529e4dd9038e3947468b)#define MEDIA\_PROXY\_OP\_SUP\_MOVE\_RELATIVE BIT(5)

193

[ 194](group__bt__media__proxy.md#ga3d39700e21cbdf2906321c8899e0b626)#define MEDIA\_PROXY\_OP\_SUP\_PREV\_SEGMENT BIT(6)

[ 195](group__bt__media__proxy.md#ga26ae64ece06a1f6f8dd7eb2c9965a4b6)#define MEDIA\_PROXY\_OP\_SUP\_NEXT\_SEGMENT BIT(7)

[ 196](group__bt__media__proxy.md#ga916ce95086dfeb127e124a8c5d530371)#define MEDIA\_PROXY\_OP\_SUP\_FIRST\_SEGMENT BIT(8)

[ 197](group__bt__media__proxy.md#gaf193ea0b4a34e3981f2f45d3b9c228a2)#define MEDIA\_PROXY\_OP\_SUP\_LAST\_SEGMENT BIT(9)

[ 198](group__bt__media__proxy.md#ga7af591de387958f5c187ba8d0e834247)#define MEDIA\_PROXY\_OP\_SUP\_GOTO\_SEGMENT BIT(10)

199

[ 200](group__bt__media__proxy.md#gafe8bab8f90281e5894e5f79f32449e63)#define MEDIA\_PROXY\_OP\_SUP\_PREV\_TRACK BIT(11)

[ 201](group__bt__media__proxy.md#gafc061bc953b0338aded4cef681f9e963)#define MEDIA\_PROXY\_OP\_SUP\_NEXT\_TRACK BIT(12)

[ 202](group__bt__media__proxy.md#ga6e1d53fedf09bd95bcf112495dcfd64f)#define MEDIA\_PROXY\_OP\_SUP\_FIRST\_TRACK BIT(13)

[ 203](group__bt__media__proxy.md#gaf43188bb438b9a766d07cd2fa900e079)#define MEDIA\_PROXY\_OP\_SUP\_LAST\_TRACK BIT(14)

[ 204](group__bt__media__proxy.md#gad2364a0ef8c54bd9fa3372edddae32b0)#define MEDIA\_PROXY\_OP\_SUP\_GOTO\_TRACK BIT(15)

205

[ 206](group__bt__media__proxy.md#ga496060d673b48e045a5a2a57aa82bddc)#define MEDIA\_PROXY\_OP\_SUP\_PREV\_GROUP BIT(16)

[ 207](group__bt__media__proxy.md#ga324dae538f28e818eea79c83aaa0b22c)#define MEDIA\_PROXY\_OP\_SUP\_NEXT\_GROUP BIT(17)

[ 208](group__bt__media__proxy.md#ga716af4c6eb702729ec4f9ff9ccc49b32)#define MEDIA\_PROXY\_OP\_SUP\_FIRST\_GROUP BIT(18)

[ 209](group__bt__media__proxy.md#gac944825600367a41e8213dfd9de569a3)#define MEDIA\_PROXY\_OP\_SUP\_LAST\_GROUP BIT(19)

[ 210](group__bt__media__proxy.md#gaec8b6d2d684c81b9da9fee870e0258c2)#define MEDIA\_PROXY\_OP\_SUP\_GOTO\_GROUP BIT(20)

211

[ 215](group__bt__media__proxy.md#gaa56458b11f4cb78f1265ea8538774108)#define MEDIA\_PROXY\_CMD\_SUCCESS 0x01

[ 216](group__bt__media__proxy.md#ga1637459cd6eaf9d4d63a04d1facc29b7)#define MEDIA\_PROXY\_CMD\_NOT\_SUPPORTED 0x02

[ 217](group__bt__media__proxy.md#ga7d0595796a80348b570add74c6dfa14e)#define MEDIA\_PROXY\_CMD\_PLAYER\_INACTIVE 0x03

[ 218](group__bt__media__proxy.md#gaf2c68cb2ac32973b85594660d43688dd)#define MEDIA\_PROXY\_CMD\_CANNOT\_BE\_COMPLETED 0x04

219

[ 223](group__bt__media__proxy.md#ga8be6fd8d9bb08836bea1c3f0d2e577ea)#define MEDIA\_PROXY\_SEARCH\_TYPE\_TRACK\_NAME 0x01

[ 224](group__bt__media__proxy.md#gaf0dbc19f843a444076d8886b1a05709b)#define MEDIA\_PROXY\_SEARCH\_TYPE\_ARTIST\_NAME 0x02

[ 225](group__bt__media__proxy.md#ga1f0fb19dea467e90afd670ed9af0c092)#define MEDIA\_PROXY\_SEARCH\_TYPE\_ALBUM\_NAME 0x03

[ 226](group__bt__media__proxy.md#gaca10de7253c1cdcf5e0c6544de33c116)#define MEDIA\_PROXY\_SEARCH\_TYPE\_GROUP\_NAME 0x04

[ 227](group__bt__media__proxy.md#ga28b1d7de2174e3714786cb369232f339)#define MEDIA\_PROXY\_SEARCH\_TYPE\_EARLIEST\_YEAR 0x05

[ 228](group__bt__media__proxy.md#ga01fb087af00bf492d19cc19adcaa9dea)#define MEDIA\_PROXY\_SEARCH\_TYPE\_LATEST\_YEAR 0x06

[ 229](group__bt__media__proxy.md#ga55c3a003881a75ce964e23fc3b0cea8e)#define MEDIA\_PROXY\_SEARCH\_TYPE\_GENRE 0x07

[ 230](group__bt__media__proxy.md#gad758e14fbe978ffd95364a6fb27eab40)#define MEDIA\_PROXY\_SEARCH\_TYPE\_ONLY\_TRACKS 0x08

[ 231](group__bt__media__proxy.md#ga25270f6c90daaace6a80f3255aaaf7fd)#define MEDIA\_PROXY\_SEARCH\_TYPE\_ONLY\_GROUPS 0x09

232

[ 236](group__bt__media__proxy.md#ga2627f632efab868adddeebb59243497c)#define MEDIA\_PROXY\_SEARCH\_SUCCESS 0x01

[ 237](group__bt__media__proxy.md#gaf406225a87c697d784c5a429e89d2354)#define MEDIA\_PROXY\_SEARCH\_FAILURE 0x02

238

239/\* Group object object types \*/

[ 240](group__bt__media__proxy.md#ga7412b20ea355713443b7165f077b0a0d)#define MEDIA\_PROXY\_GROUP\_OBJECT\_TRACK\_TYPE 0x00

[ 241](group__bt__media__proxy.md#ga63abba926894a45e187e3f4e4610cb35)#define MEDIA\_PROXY\_GROUP\_OBJECT\_GROUP\_TYPE 0x01

242

243

247struct media\_player;

248

249/\* PUBLIC API FOR CONTROLLERS \*/

250

[ 255](structmedia__proxy__ctrl__cbs.md)struct [media\_proxy\_ctrl\_cbs](structmedia__proxy__ctrl__cbs.md) {

256

[ 268](structmedia__proxy__ctrl__cbs.md#af2cd0f93aadd451f1b358e2d2d6a0049) void (\*[local\_player\_instance](structmedia__proxy__ctrl__cbs.md#af2cd0f93aadd451f1b358e2d2d6a0049))(struct media\_player \*player, int err);

269

270#ifdef CONFIG\_MCTL\_REMOTE\_PLAYER\_CONTROL

282 void (\*discover\_player)(struct media\_player \*player, int err);

283#endif /\* CONFIG\_MCTL\_REMOTE\_PLAYER\_CONTROL \*/

284

[ 296](structmedia__proxy__ctrl__cbs.md#a94b5ec6bc20299b722bd0e2cb28aed5e) void (\*[player\_name\_recv](structmedia__proxy__ctrl__cbs.md#a94b5ec6bc20299b722bd0e2cb28aed5e))(struct media\_player \*player, int err, const char \*name);

297

[ 309](structmedia__proxy__ctrl__cbs.md#aaa7ba216e604be1c447a93231a0857d0) void (\*[icon\_id\_recv](structmedia__proxy__ctrl__cbs.md#aaa7ba216e604be1c447a93231a0857d0))(struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

310

[ 322](structmedia__proxy__ctrl__cbs.md#a53c4809b7a10b9057f565411429d691b) void (\*[icon\_url\_recv](structmedia__proxy__ctrl__cbs.md#a53c4809b7a10b9057f565411429d691b))(struct media\_player \*player, int err, const char \*url);

323

[ 333](structmedia__proxy__ctrl__cbs.md#ade71f132ef66c7bfd13b1b1f3200681d) void (\*[track\_changed\_recv](structmedia__proxy__ctrl__cbs.md#ade71f132ef66c7bfd13b1b1f3200681d))(struct media\_player \*player, int err);

334

[ 346](structmedia__proxy__ctrl__cbs.md#ac1afc71ed04faa87e644d095ef14946f) void (\*[track\_title\_recv](structmedia__proxy__ctrl__cbs.md#ac1afc71ed04faa87e644d095ef14946f))(struct media\_player \*player, int err, const char \*title);

347

[ 359](structmedia__proxy__ctrl__cbs.md#a85c0bfc83bb26c74b11b5cb8182ff1e0) void (\*[track\_duration\_recv](structmedia__proxy__ctrl__cbs.md#a85c0bfc83bb26c74b11b5cb8182ff1e0))(struct media\_player \*player, int err, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) duration);

360

[ 373](structmedia__proxy__ctrl__cbs.md#a6aa029523978e02dc1c8c7ff798e2433) void (\*[track\_position\_recv](structmedia__proxy__ctrl__cbs.md#a6aa029523978e02dc1c8c7ff798e2433))(struct media\_player \*player, int err, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) position);

374

[ 386](structmedia__proxy__ctrl__cbs.md#a54f9f50e3b8f99b586a2c522a67da213) void (\*[track\_position\_write](structmedia__proxy__ctrl__cbs.md#a54f9f50e3b8f99b586a2c522a67da213))(struct media\_player \*player, int err, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) position);

387

[ 400](structmedia__proxy__ctrl__cbs.md#a5eb1466e8ba100c9d3cb12f097328b9e) void (\*[playback\_speed\_recv](structmedia__proxy__ctrl__cbs.md#a5eb1466e8ba100c9d3cb12f097328b9e))(struct media\_player \*player, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed);

401

[ 413](structmedia__proxy__ctrl__cbs.md#ad84d5caca4be208bd5e5d93f5c801ddf) void (\*[playback\_speed\_write](structmedia__proxy__ctrl__cbs.md#ad84d5caca4be208bd5e5d93f5c801ddf))(struct media\_player \*player, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed);

414

[ 426](structmedia__proxy__ctrl__cbs.md#a2ba0e73f7e67c38f5abe555305753d0f) void (\*[seeking\_speed\_recv](structmedia__proxy__ctrl__cbs.md#a2ba0e73f7e67c38f5abe555305753d0f))(struct media\_player \*player, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed);

427

[ 439](structmedia__proxy__ctrl__cbs.md#aa7e7f7724689844491a4885544fc450c) void (\*[track\_segments\_id\_recv](structmedia__proxy__ctrl__cbs.md#aa7e7f7724689844491a4885544fc450c))(struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

440

[ 453](structmedia__proxy__ctrl__cbs.md#aa3c2bd1734c6235eb2026915dbebc6c2) void (\*[current\_track\_id\_recv](structmedia__proxy__ctrl__cbs.md#aa3c2bd1734c6235eb2026915dbebc6c2))(struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

454

[ 466](structmedia__proxy__ctrl__cbs.md#a66f35a59821f53f4ed9aa7dea0e4d654) void (\*[current\_track\_id\_write](structmedia__proxy__ctrl__cbs.md#a66f35a59821f53f4ed9aa7dea0e4d654))(struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

467

[ 480](structmedia__proxy__ctrl__cbs.md#a5692c0d142977b8ec7a4ffb765fd0687) void (\*[next\_track\_id\_recv](structmedia__proxy__ctrl__cbs.md#a5692c0d142977b8ec7a4ffb765fd0687))(struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

481

[ 493](structmedia__proxy__ctrl__cbs.md#a08b6fe1079b759de1f5a9f7751a22f21) void (\*[next\_track\_id\_write](structmedia__proxy__ctrl__cbs.md#a08b6fe1079b759de1f5a9f7751a22f21))(struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

494

[ 506](structmedia__proxy__ctrl__cbs.md#a3c2b39bc46f8b2a7155c14dd430add8e) void (\*[parent\_group\_id\_recv](structmedia__proxy__ctrl__cbs.md#a3c2b39bc46f8b2a7155c14dd430add8e))(struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

507

[ 520](structmedia__proxy__ctrl__cbs.md#a858a8854259c8e7a09164b916fae309a) void (\*[current\_group\_id\_recv](structmedia__proxy__ctrl__cbs.md#a858a8854259c8e7a09164b916fae309a))(struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

521

[ 533](structmedia__proxy__ctrl__cbs.md#ad1a65519a958aa27091a2ba41260db04) void (\*[current\_group\_id\_write](structmedia__proxy__ctrl__cbs.md#ad1a65519a958aa27091a2ba41260db04))(struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

534

[ 547](structmedia__proxy__ctrl__cbs.md#a92a3b0e3254d6b26e0d18476dce3b01e) void (\*[playing\_order\_recv](structmedia__proxy__ctrl__cbs.md#a92a3b0e3254d6b26e0d18476dce3b01e))(struct media\_player \*player, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order);

548

[ 560](structmedia__proxy__ctrl__cbs.md#a67cf70c9b72a87b03009f1da0a8980f2) void (\*[playing\_order\_write](structmedia__proxy__ctrl__cbs.md#a67cf70c9b72a87b03009f1da0a8980f2))(struct media\_player \*player, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order);

561

[ 573](structmedia__proxy__ctrl__cbs.md#a85182342b606c78127f2690ac1beab7d) void (\*[playing\_orders\_supported\_recv](structmedia__proxy__ctrl__cbs.md#a85182342b606c78127f2690ac1beab7d))(struct media\_player \*player, int err,

574 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) orders);

575

[ 588](structmedia__proxy__ctrl__cbs.md#ad4199644afcf356a565b884129ca0cf3) void (\*[media\_state\_recv](structmedia__proxy__ctrl__cbs.md#ad4199644afcf356a565b884129ca0cf3))(struct media\_player \*player, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

589

[ 601](structmedia__proxy__ctrl__cbs.md#a89bb28499c989a9a2ad13d40dda6c6db) void (\*[command\_send](structmedia__proxy__ctrl__cbs.md#a89bb28499c989a9a2ad13d40dda6c6db))(struct media\_player \*player, int err, const struct [mpl\_cmd](structmpl__cmd.md) \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615));

602

[ 614](structmedia__proxy__ctrl__cbs.md#a90481b6563033a4520b85307e07e2e3a) void (\*[command\_recv](structmedia__proxy__ctrl__cbs.md#a90481b6563033a4520b85307e07e2e3a))(struct media\_player \*player, int err,

615 const struct [mpl\_cmd\_ntf](structmpl__cmd__ntf.md) \*result);

616

[ 628](structmedia__proxy__ctrl__cbs.md#a06fadb043fd0a795f872063b7950d414) void (\*[commands\_supported\_recv](structmedia__proxy__ctrl__cbs.md#a06fadb043fd0a795f872063b7950d414))(struct media\_player \*player, int err, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) opcodes);

629

[ 641](structmedia__proxy__ctrl__cbs.md#aee4a556023d56c3a0d4c2036b3bc0799) void (\*[search\_send](structmedia__proxy__ctrl__cbs.md#aee4a556023d56c3a0d4c2036b3bc0799))(struct media\_player \*player, int err, const struct [mpl\_search](structmpl__search.md) \*search);

642

[ 659](structmedia__proxy__ctrl__cbs.md#a0678ad4950c6f526c78d2143e9b7c385) void (\*[search\_recv](structmedia__proxy__ctrl__cbs.md#a0678ad4950c6f526c78d2143e9b7c385))(struct media\_player \*player, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) result\_code);

660

[ 672](structmedia__proxy__ctrl__cbs.md#af067e55ef7f676ad3c05f838160ed21e) void (\*[search\_results\_id\_recv](structmedia__proxy__ctrl__cbs.md#af067e55ef7f676ad3c05f838160ed21e))(struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

673

[ 685](structmedia__proxy__ctrl__cbs.md#a08f3f55a5b56d1ede9141013fe456119) void (\*[content\_ctrl\_id\_recv](structmedia__proxy__ctrl__cbs.md#a08f3f55a5b56d1ede9141013fe456119))(struct media\_player \*player, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ccid);

686};

687

[ 695](group__bt__media__proxy.md#ga352228fb77498b61205a22b0f3a75c8e)int [media\_proxy\_ctrl\_register](group__bt__media__proxy.md#ga352228fb77498b61205a22b0f3a75c8e)(struct [media\_proxy\_ctrl\_cbs](structmedia__proxy__ctrl__cbs.md) \*ctrl\_cbs);

696

[ 714](group__bt__media__proxy.md#ga5aaa486e0c3663e21477984e54642ed1)int [media\_proxy\_ctrl\_discover\_player](group__bt__media__proxy.md#ga5aaa486e0c3663e21477984e54642ed1)(struct bt\_conn \*conn);

715

[ 723](group__bt__media__proxy.md#ga2261222d8581ed86e91a276b13359126)int [media\_proxy\_ctrl\_get\_player\_name](group__bt__media__proxy.md#ga2261222d8581ed86e91a276b13359126)(struct media\_player \*player);

724

[ 740](group__bt__media__proxy.md#ga5efccb39cdb97eed476e0c0bff461ec1)int [media\_proxy\_ctrl\_get\_icon\_id](group__bt__media__proxy.md#ga5efccb39cdb97eed476e0c0bff461ec1)(struct media\_player \*player);

741

[ 749](group__bt__media__proxy.md#gab6df6fe71c8273eca855eb3be27290dd)int [media\_proxy\_ctrl\_get\_icon\_url](group__bt__media__proxy.md#gab6df6fe71c8273eca855eb3be27290dd)(struct media\_player \*player);

750

[ 758](group__bt__media__proxy.md#gabfbb49e79204130cb004f217af771b80)int [media\_proxy\_ctrl\_get\_track\_title](group__bt__media__proxy.md#gabfbb49e79204130cb004f217af771b80)(struct media\_player \*player);

759

[ 770](group__bt__media__proxy.md#ga488441418a8f2d358092019bbfe16788)int [media\_proxy\_ctrl\_get\_track\_duration](group__bt__media__proxy.md#ga488441418a8f2d358092019bbfe16788)(struct media\_player \*player);

771

[ 783](group__bt__media__proxy.md#gae0bb75feb49a68b495150c6fba2f21a7)int [media\_proxy\_ctrl\_get\_track\_position](group__bt__media__proxy.md#gae0bb75feb49a68b495150c6fba2f21a7)(struct media\_player \*player);

784

[ 799](group__bt__media__proxy.md#ga776bb5f16cf1f4f6cc3842aabd86b781)int [media\_proxy\_ctrl\_set\_track\_position](group__bt__media__proxy.md#ga776bb5f16cf1f4f6cc3842aabd86b781)(struct media\_player \*player, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) position);

800

[ 818](group__bt__media__proxy.md#ga2d64a23b3f881579a603a04baeb64088)int [media\_proxy\_ctrl\_get\_playback\_speed](group__bt__media__proxy.md#ga2d64a23b3f881579a603a04baeb64088)(struct media\_player \*player);

819

[ 839](group__bt__media__proxy.md#gabafbc857c3e6befe98e339acb58f17fb)int [media\_proxy\_ctrl\_set\_playback\_speed](group__bt__media__proxy.md#gabafbc857c3e6befe98e339acb58f17fb)(struct media\_player \*player, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed);

840

[ 857](group__bt__media__proxy.md#ga817ca4ab611e214493fbc918036def0f)int [media\_proxy\_ctrl\_get\_seeking\_speed](group__bt__media__proxy.md#ga817ca4ab611e214493fbc918036def0f)(struct media\_player \*player);

858

[ 874](group__bt__media__proxy.md#ga1afcc097cb36c4f11141b82ce28e8126)int [media\_proxy\_ctrl\_get\_track\_segments\_id](group__bt__media__proxy.md#ga1afcc097cb36c4f11141b82ce28e8126)(struct media\_player \*player);

875

[ 891](group__bt__media__proxy.md#gaebe7e3683041e28bef40df75cc991dea)int [media\_proxy\_ctrl\_get\_current\_track\_id](group__bt__media__proxy.md#gaebe7e3683041e28bef40df75cc991dea)(struct media\_player \*player);

892

[ 906](group__bt__media__proxy.md#gaea6adacedaded10f7c2c0f91b7159f74)int [media\_proxy\_ctrl\_set\_current\_track\_id](group__bt__media__proxy.md#gaea6adacedaded10f7c2c0f91b7159f74)(struct media\_player \*player, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

907

[ 920](group__bt__media__proxy.md#gae32da32bd504061801730805729242e1)int [media\_proxy\_ctrl\_get\_next\_track\_id](group__bt__media__proxy.md#gae32da32bd504061801730805729242e1)(struct media\_player \*player);

921

[ 934](group__bt__media__proxy.md#ga43b797717fb9b36b94a606dfabeb0fa7)int [media\_proxy\_ctrl\_set\_next\_track\_id](group__bt__media__proxy.md#ga43b797717fb9b36b94a606dfabeb0fa7)(struct media\_player \*player, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

935

[ 953](group__bt__media__proxy.md#ga12dc878be39814660900ba875e13e537)int [media\_proxy\_ctrl\_get\_parent\_group\_id](group__bt__media__proxy.md#ga12dc878be39814660900ba875e13e537)(struct media\_player \*player);

954

[ 970](group__bt__media__proxy.md#ga2ae50a1988305b4247ff0af796b6d93e)int [media\_proxy\_ctrl\_get\_current\_group\_id](group__bt__media__proxy.md#ga2ae50a1988305b4247ff0af796b6d93e)(struct media\_player \*player);

971

[ 985](group__bt__media__proxy.md#gae496885d0124f4e3fc2c0f203fcff118)int [media\_proxy\_ctrl\_set\_current\_group\_id](group__bt__media__proxy.md#gae496885d0124f4e3fc2c0f203fcff118)(struct media\_player \*player, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

986

[ 994](group__bt__media__proxy.md#ga2f93bcde2460c6638880f8e6631eb68e)int [media\_proxy\_ctrl\_get\_playing\_order](group__bt__media__proxy.md#ga2f93bcde2460c6638880f8e6631eb68e)(struct media\_player \*player);

995

[ 1006](group__bt__media__proxy.md#gaa4040e97100f6e70527e6ad201309bbe)int [media\_proxy\_ctrl\_set\_playing\_order](group__bt__media__proxy.md#gaa4040e97100f6e70527e6ad201309bbe)(struct media\_player \*player, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order);

1007

[ 1018](group__bt__media__proxy.md#ga030899757b79251f1d5a1055f65fe989)int [media\_proxy\_ctrl\_get\_playing\_orders\_supported](group__bt__media__proxy.md#ga030899757b79251f1d5a1055f65fe989)(struct media\_player \*player);

1019

[ 1029](group__bt__media__proxy.md#ga9433aaf24776c30557ea694795e75b3e)int [media\_proxy\_ctrl\_get\_media\_state](group__bt__media__proxy.md#ga9433aaf24776c30557ea694795e75b3e)(struct media\_player \*player);

1030

[ 1044](group__bt__media__proxy.md#ga590762e7272b99fb8ac50a7841424670)int [media\_proxy\_ctrl\_send\_command](group__bt__media__proxy.md#ga590762e7272b99fb8ac50a7841424670)(struct media\_player \*player, const struct [mpl\_cmd](structmpl__cmd.md) \*command);

1045

[ 1056](group__bt__media__proxy.md#ga15804287093b20d4a1616380729b33c8)int [media\_proxy\_ctrl\_get\_commands\_supported](group__bt__media__proxy.md#ga15804287093b20d4a1616380729b33c8)(struct media\_player \*player);

1057

[ 1077](group__bt__media__proxy.md#ga052c3fabac4a44ee2802ddd4a6c5c9ac)int [media\_proxy\_ctrl\_send\_search](group__bt__media__proxy.md#ga052c3fabac4a44ee2802ddd4a6c5c9ac)(struct media\_player \*player, const struct [mpl\_search](structmpl__search.md) \*search);

1078

[ 1095](group__bt__media__proxy.md#ga580a0c9fa47460be59f0571ee11a41b4)int [media\_proxy\_ctrl\_get\_search\_results\_id](group__bt__media__proxy.md#ga580a0c9fa47460be59f0571ee11a41b4)(struct media\_player \*player);

1096

[ 1108](group__bt__media__proxy.md#ga23488e77985a04216ec7c7fa785f09fc)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [media\_proxy\_ctrl\_get\_content\_ctrl\_id](group__bt__media__proxy.md#ga23488e77985a04216ec7c7fa785f09fc)(struct media\_player \*player);

1109

1110

1111/\* PUBLIC API FOR PLAYERS \*/

1112

[ 1117](structmedia__proxy__pl__calls.md)struct [media\_proxy\_pl\_calls](structmedia__proxy__pl__calls.md) {

1118

[ 1124](structmedia__proxy__pl__calls.md#a2946f7572e12ffabc5f6ba2f562d52cf) const char \*(\*get\_player\_name)(void);

1125

[ 1137](structmedia__proxy__pl__calls.md#ad1215725454c6b76dcdc197a275c03cf) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) (\*[get\_icon\_id](structmedia__proxy__pl__calls.md#ad1215725454c6b76dcdc197a275c03cf))(void);

1138

[ 1146](structmedia__proxy__pl__calls.md#a319dd309f94c45292613ab9caa0e399b) const char \*(\*get\_icon\_url)(void);

1147

[ 1153](structmedia__proxy__pl__calls.md#af9fc0af545c8c28f8f4dbf8c6afb4acf) const char \*(\*get\_track\_title)(void);

1154

[ 1163](structmedia__proxy__pl__calls.md#a1b852ccc45a6ee1174b9d58df3b599b6) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) (\*[get\_track\_duration](structmedia__proxy__pl__calls.md#a1b852ccc45a6ee1174b9d58df3b599b6))(void);

1164

[ 1174](structmedia__proxy__pl__calls.md#a11ea1cf984a7d11ac7e61405df84ee06) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) (\*[get\_track\_position](structmedia__proxy__pl__calls.md#a11ea1cf984a7d11ac7e61405df84ee06))(void);

1175

[ 1187](structmedia__proxy__pl__calls.md#a001ae07161b8a6c7dfc9c2e471f229e5) void (\*[set\_track\_position](structmedia__proxy__pl__calls.md#a001ae07161b8a6c7dfc9c2e471f229e5))([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) position);

1188

[ 1204](structmedia__proxy__pl__calls.md#ae1006d5c684e12e1e1c927f71aa93930) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) (\*[get\_playback\_speed](structmedia__proxy__pl__calls.md#ae1006d5c684e12e1e1c927f71aa93930))(void);

1205

[ 1222](structmedia__proxy__pl__calls.md#a7535dad9be2f4b83c8a7c55fccc8a7af) void (\*[set\_playback\_speed](structmedia__proxy__pl__calls.md#a7535dad9be2f4b83c8a7c55fccc8a7af))([int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed);

1223

[ 1238](structmedia__proxy__pl__calls.md#aebf24b582cf33786f2dc17765d858a15) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) (\*[get\_seeking\_speed](structmedia__proxy__pl__calls.md#aebf24b582cf33786f2dc17765d858a15))(void);

1239

[ 1251](structmedia__proxy__pl__calls.md#a86a71b788b54a4e7c966f162fcab6433) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) (\*[get\_track\_segments\_id](structmedia__proxy__pl__calls.md#a86a71b788b54a4e7c966f162fcab6433))(void);

1252

[ 1264](structmedia__proxy__pl__calls.md#a7f19bd75114835d151ff5b26733ed450) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) (\*[get\_current\_track\_id](structmedia__proxy__pl__calls.md#a7f19bd75114835d151ff5b26733ed450))(void);

1265

[ 1274](structmedia__proxy__pl__calls.md#a422cec33063313a9aab86baf0bd65ef1) void (\*[set\_current\_track\_id](structmedia__proxy__pl__calls.md#a422cec33063313a9aab86baf0bd65ef1))([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

1275

[ 1284](structmedia__proxy__pl__calls.md#af939a96fbcfe474dfcdcfb353ae0aac5) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) (\*[get\_next\_track\_id](structmedia__proxy__pl__calls.md#af939a96fbcfe474dfcdcfb353ae0aac5))(void);

1285

[ 1293](structmedia__proxy__pl__calls.md#acbf8dc9dcc8fbaba44d436310c92f3a9) void (\*[set\_next\_track\_id](structmedia__proxy__pl__calls.md#acbf8dc9dcc8fbaba44d436310c92f3a9))([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

1294

[ 1308](structmedia__proxy__pl__calls.md#a1409764199d47d0c27d07e13c8fa8f68) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) (\*[get\_parent\_group\_id](structmedia__proxy__pl__calls.md#a1409764199d47d0c27d07e13c8fa8f68))(void);

1309

[ 1321](structmedia__proxy__pl__calls.md#a98b02d4689cd5e279f43094f3ca09339) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) (\*[get\_current\_group\_id](structmedia__proxy__pl__calls.md#a98b02d4689cd5e279f43094f3ca09339))(void);

1322

[ 1331](structmedia__proxy__pl__calls.md#a5049e21965e7fd08aaeafcbedf76809c) void (\*[set\_current\_group\_id](structmedia__proxy__pl__calls.md#a5049e21965e7fd08aaeafcbedf76809c))([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

1332

[ 1338](structmedia__proxy__pl__calls.md#a98989105d01265de4b268b623a26df2e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) (\*[get\_playing\_order](structmedia__proxy__pl__calls.md#a98989105d01265de4b268b623a26df2e))(void);

1339

[ 1348](structmedia__proxy__pl__calls.md#ad6fad92957146aeaf1bec0e56606da72) void (\*[set\_playing\_order](structmedia__proxy__pl__calls.md#ad6fad92957146aeaf1bec0e56606da72))([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order);

1349

[ 1359](structmedia__proxy__pl__calls.md#a9b733c3187cc032ef6644a16ffd3f7c9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) (\*[get\_playing\_orders\_supported](structmedia__proxy__pl__calls.md#a9b733c3187cc032ef6644a16ffd3f7c9))(void);

1360

[ 1369](structmedia__proxy__pl__calls.md#a6a339aa7ee564acacffd2637eeb8e7ea) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) (\*[get\_media\_state](structmedia__proxy__pl__calls.md#a6a339aa7ee564acacffd2637eeb8e7ea))(void);

1370

[ 1380](structmedia__proxy__pl__calls.md#abae1ff89136b93ce4dee5dbe12e6791d) void (\*[send\_command](structmedia__proxy__pl__calls.md#abae1ff89136b93ce4dee5dbe12e6791d))(const struct [mpl\_cmd](structmpl__cmd.md) \*command);

1381

[ 1391](structmedia__proxy__pl__calls.md#ae0a4457fcc35d32541f2557698d5aa83) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[get\_commands\_supported](structmedia__proxy__pl__calls.md#ae0a4457fcc35d32541f2557698d5aa83))(void);

1392

[ 1402](structmedia__proxy__pl__calls.md#a416ca20a05a66f4ce28635159173f064) void (\*[send\_search](structmedia__proxy__pl__calls.md#a416ca20a05a66f4ce28635159173f064))(const struct [mpl\_search](structmpl__search.md) \*search);

1403

[ 1416](structmedia__proxy__pl__calls.md#adf4003ba8ef1a5c38b75876f864564c5) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) (\*[get\_search\_results\_id](structmedia__proxy__pl__calls.md#adf4003ba8ef1a5c38b75876f864564c5))(void);

1417

[ 1427](structmedia__proxy__pl__calls.md#a64bc23cc61e69b1b6c4050f76a9bc674) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) (\*[get\_content\_ctrl\_id](structmedia__proxy__pl__calls.md#a64bc23cc61e69b1b6c4050f76a9bc674))(void);

1428};

1429

[ 1443](group__bt__media__proxy.md#gac75e27a4a5e169481723cd6b39678274)int [media\_proxy\_pl\_register](group__bt__media__proxy.md#gac75e27a4a5e169481723cd6b39678274)(struct [media\_proxy\_pl\_calls](structmedia__proxy__pl__calls.md) \*pl\_calls);

1444

1445/\* Initialize player - TODO: Move to player header file \*/

[ 1446](group__bt__media__proxy.md#gab0b10b3de5674f2172e1a2f779cbe8d5)int [media\_proxy\_pl\_init](group__bt__media__proxy.md#gab0b10b3de5674f2172e1a2f779cbe8d5)(void);

1447

1448/\* TODO: Find best location for this call, and move this one also \*/

[ 1449](group__bt__media__proxy.md#gaf535f1ab028407432ef890d278d936e0)struct bt\_ots \*[bt\_mcs\_get\_ots](group__bt__media__proxy.md#gaf535f1ab028407432ef890d278d936e0)(void);

1450

1451/\* Callbacks from the player to the media proxy \*/

[ 1459](group__bt__media__proxy.md#ga0a70dc60a4d6acbcc58e220b75dad92a)void [media\_proxy\_pl\_name\_cb](group__bt__media__proxy.md#ga0a70dc60a4d6acbcc58e220b75dad92a)(const char \*name);

1460

[ 1468](group__bt__media__proxy.md#gadd348a8d5aff193f7a9113a759e85b1d)void [media\_proxy\_pl\_icon\_url\_cb](group__bt__media__proxy.md#gadd348a8d5aff193f7a9113a759e85b1d)(const char \*url);

1469

[ 1475](group__bt__media__proxy.md#ga4a93a18cb0b75cb16828243f0d37b4b4)void [media\_proxy\_pl\_track\_changed\_cb](group__bt__media__proxy.md#ga4a93a18cb0b75cb16828243f0d37b4b4)(void);

1476

[ 1484](group__bt__media__proxy.md#ga9489b517e4baa215f0b7b59243cee11c)void [media\_proxy\_pl\_track\_title\_cb](group__bt__media__proxy.md#ga9489b517e4baa215f0b7b59243cee11c)(char \*title);

1485

[ 1496](group__bt__media__proxy.md#ga7b0f9633a5322557b91ea97eafac9f34)void [media\_proxy\_pl\_track\_duration\_cb](group__bt__media__proxy.md#ga7b0f9633a5322557b91ea97eafac9f34)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) duration);

1497

[ 1513](group__bt__media__proxy.md#ga61d494d7e149cfa2c3f9546c1e3b99bd)void [media\_proxy\_pl\_track\_position\_cb](group__bt__media__proxy.md#ga61d494d7e149cfa2c3f9546c1e3b99bd)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) position);

1514

[ 1522](group__bt__media__proxy.md#ga17c2ca149050e1382eb556f6dcccad21)void [media\_proxy\_pl\_playback\_speed\_cb](group__bt__media__proxy.md#ga17c2ca149050e1382eb556f6dcccad21)([int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed);

1523

[ 1531](group__bt__media__proxy.md#gaeaf89f4b760870896ed42687562971ca)void [media\_proxy\_pl\_seeking\_speed\_cb](group__bt__media__proxy.md#gaeaf89f4b760870896ed42687562971ca)([int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed);

1532

[ 1541](group__bt__media__proxy.md#gadcad4efdd714159d5d9611bbf74d5fae)void [media\_proxy\_pl\_current\_track\_id\_cb](group__bt__media__proxy.md#gadcad4efdd714159d5d9611bbf74d5fae)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

1542

[ 1550](group__bt__media__proxy.md#gaf0bd3447e64b6128710c07461766a0c9)void [media\_proxy\_pl\_next\_track\_id\_cb](group__bt__media__proxy.md#gaf0bd3447e64b6128710c07461766a0c9)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

1551

[ 1559](group__bt__media__proxy.md#ga64730f46b87cf9089aff65b6be12f42d)void [media\_proxy\_pl\_parent\_group\_id\_cb](group__bt__media__proxy.md#ga64730f46b87cf9089aff65b6be12f42d)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

1560

[ 1568](group__bt__media__proxy.md#gad02f2924e1aa765c04cbbc6441e7d063)void [media\_proxy\_pl\_current\_group\_id\_cb](group__bt__media__proxy.md#gad02f2924e1aa765c04cbbc6441e7d063)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

1569

[ 1577](group__bt__media__proxy.md#ga96e8156b0267f3d55ee52ab307d81985)void [media\_proxy\_pl\_playing\_order\_cb](group__bt__media__proxy.md#ga96e8156b0267f3d55ee52ab307d81985)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order);

1578

[ 1586](group__bt__media__proxy.md#ga842d7951a04702d6f819de44c47b9cac)void [media\_proxy\_pl\_media\_state\_cb](group__bt__media__proxy.md#ga842d7951a04702d6f819de44c47b9cac)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

1587

[ 1597](group__bt__media__proxy.md#ga694e83401835149833024cf094b98cd1)void [media\_proxy\_pl\_command\_cb](group__bt__media__proxy.md#ga694e83401835149833024cf094b98cd1)(const struct [mpl\_cmd\_ntf](structmpl__cmd__ntf.md) \*cmd\_ntf);

1598

[ 1606](group__bt__media__proxy.md#ga70ea8a24a4e853a191e0947e1c2d1145)void [media\_proxy\_pl\_commands\_supported\_cb](group__bt__media__proxy.md#ga70ea8a24a4e853a191e0947e1c2d1145)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) opcodes);

1607

[ 1620](group__bt__media__proxy.md#ga8c0d75f61120047bacd0b933534e1b41)void [media\_proxy\_pl\_search\_cb](group__bt__media__proxy.md#ga8c0d75f61120047bacd0b933534e1b41)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) result\_code);

1621

[ 1630](group__bt__media__proxy.md#ga35896de266f2a2bd101279e4ce9900c7)void [media\_proxy\_pl\_search\_results\_id\_cb](group__bt__media__proxy.md#ga35896de266f2a2bd101279e4ce9900c7)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

1631

1632#ifdef \_\_cplusplus

1633}

1634#endif

1635 /\* End of group bt\_media\_proxy \*/

1637

1638#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_MEDIA\_PROXY\_H\_ \*/

[bluetooth.h](bluetooth_8h.md)

Bluetooth subsystem core APIs.

[SEARCH\_PARAM\_MAX](group__bt__mcs.md#ga81665fd87487cbaf1c0f90f1e0b2126a)

#define SEARCH\_PARAM\_MAX

**Definition** mcs.h:171

[SEARCH\_LEN\_MAX](group__bt__mcs.md#gaf771b17acd202a20450b6ea939ddee3b)

#define SEARCH\_LEN\_MAX

**Definition** mcs.h:169

[media\_proxy\_ctrl\_get\_playing\_orders\_supported](group__bt__media__proxy.md#ga030899757b79251f1d5a1055f65fe989)

int media\_proxy\_ctrl\_get\_playing\_orders\_supported(struct media\_player \*player)

Read Playing Orders Supported.

[media\_proxy\_ctrl\_send\_search](group__bt__media__proxy.md#ga052c3fabac4a44ee2802ddd4a6c5c9ac)

int media\_proxy\_ctrl\_send\_search(struct media\_player \*player, const struct mpl\_search \*search)

Set Search.

[media\_proxy\_pl\_name\_cb](group__bt__media__proxy.md#ga0a70dc60a4d6acbcc58e220b75dad92a)

void media\_proxy\_pl\_name\_cb(const char \*name)

Player name changed callback.

[media\_proxy\_ctrl\_get\_parent\_group\_id](group__bt__media__proxy.md#ga12dc878be39814660900ba875e13e537)

int media\_proxy\_ctrl\_get\_parent\_group\_id(struct media\_player \*player)

Read Parent Group Object ID.

[media\_proxy\_ctrl\_get\_commands\_supported](group__bt__media__proxy.md#ga15804287093b20d4a1616380729b33c8)

int media\_proxy\_ctrl\_get\_commands\_supported(struct media\_player \*player)

Read Commands Supported.

[media\_proxy\_pl\_playback\_speed\_cb](group__bt__media__proxy.md#ga17c2ca149050e1382eb556f6dcccad21)

void media\_proxy\_pl\_playback\_speed\_cb(int8\_t speed)

Playback speed callback.

[media\_proxy\_ctrl\_get\_track\_segments\_id](group__bt__media__proxy.md#ga1afcc097cb36c4f11141b82ce28e8126)

int media\_proxy\_ctrl\_get\_track\_segments\_id(struct media\_player \*player)

Read Current Track Segments Object ID.

[media\_proxy\_ctrl\_get\_player\_name](group__bt__media__proxy.md#ga2261222d8581ed86e91a276b13359126)

int media\_proxy\_ctrl\_get\_player\_name(struct media\_player \*player)

Read Media Player Name.

[media\_proxy\_ctrl\_get\_content\_ctrl\_id](group__bt__media__proxy.md#ga23488e77985a04216ec7c7fa785f09fc)

uint8\_t media\_proxy\_ctrl\_get\_content\_ctrl\_id(struct media\_player \*player)

Read Content Control ID.

[media\_proxy\_ctrl\_get\_current\_group\_id](group__bt__media__proxy.md#ga2ae50a1988305b4247ff0af796b6d93e)

int media\_proxy\_ctrl\_get\_current\_group\_id(struct media\_player \*player)

Read Current Group Object ID.

[media\_proxy\_ctrl\_get\_playback\_speed](group__bt__media__proxy.md#ga2d64a23b3f881579a603a04baeb64088)

int media\_proxy\_ctrl\_get\_playback\_speed(struct media\_player \*player)

Get Playback Speed.

[media\_proxy\_ctrl\_get\_playing\_order](group__bt__media__proxy.md#ga2f93bcde2460c6638880f8e6631eb68e)

int media\_proxy\_ctrl\_get\_playing\_order(struct media\_player \*player)

Read Playing Order.

[media\_proxy\_ctrl\_register](group__bt__media__proxy.md#ga352228fb77498b61205a22b0f3a75c8e)

int media\_proxy\_ctrl\_register(struct media\_proxy\_ctrl\_cbs \*ctrl\_cbs)

Register a controller with the media\_proxy.

[media\_proxy\_pl\_search\_results\_id\_cb](group__bt__media__proxy.md#ga35896de266f2a2bd101279e4ce9900c7)

void media\_proxy\_pl\_search\_results\_id\_cb(uint64\_t id)

Search Results object ID callback.

[media\_proxy\_ctrl\_set\_next\_track\_id](group__bt__media__proxy.md#ga43b797717fb9b36b94a606dfabeb0fa7)

int media\_proxy\_ctrl\_set\_next\_track\_id(struct media\_player \*player, uint64\_t id)

Set Next Track Object ID.

[media\_proxy\_ctrl\_get\_track\_duration](group__bt__media__proxy.md#ga488441418a8f2d358092019bbfe16788)

int media\_proxy\_ctrl\_get\_track\_duration(struct media\_player \*player)

Read Track Duration.

[media\_proxy\_pl\_track\_changed\_cb](group__bt__media__proxy.md#ga4a93a18cb0b75cb16828243f0d37b4b4)

void media\_proxy\_pl\_track\_changed\_cb(void)

Track changed callback.

[media\_proxy\_ctrl\_get\_search\_results\_id](group__bt__media__proxy.md#ga580a0c9fa47460be59f0571ee11a41b4)

int media\_proxy\_ctrl\_get\_search\_results\_id(struct media\_player \*player)

Read Search Results Object ID.

[media\_proxy\_ctrl\_send\_command](group__bt__media__proxy.md#ga590762e7272b99fb8ac50a7841424670)

int media\_proxy\_ctrl\_send\_command(struct media\_player \*player, const struct mpl\_cmd \*command)

Send Command.

[media\_proxy\_ctrl\_discover\_player](group__bt__media__proxy.md#ga5aaa486e0c3663e21477984e54642ed1)

int media\_proxy\_ctrl\_discover\_player(struct bt\_conn \*conn)

Discover a remote media player.

[media\_proxy\_ctrl\_get\_icon\_id](group__bt__media__proxy.md#ga5efccb39cdb97eed476e0c0bff461ec1)

int media\_proxy\_ctrl\_get\_icon\_id(struct media\_player \*player)

Read Icon Object ID.

[media\_proxy\_pl\_track\_position\_cb](group__bt__media__proxy.md#ga61d494d7e149cfa2c3f9546c1e3b99bd)

void media\_proxy\_pl\_track\_position\_cb(int32\_t position)

Track position callback.

[media\_proxy\_pl\_parent\_group\_id\_cb](group__bt__media__proxy.md#ga64730f46b87cf9089aff65b6be12f42d)

void media\_proxy\_pl\_parent\_group\_id\_cb(uint64\_t id)

Parent group object ID callback.

[media\_proxy\_pl\_command\_cb](group__bt__media__proxy.md#ga694e83401835149833024cf094b98cd1)

void media\_proxy\_pl\_command\_cb(const struct mpl\_cmd\_ntf \*cmd\_ntf)

Command callback.

[media\_proxy\_pl\_commands\_supported\_cb](group__bt__media__proxy.md#ga70ea8a24a4e853a191e0947e1c2d1145)

void media\_proxy\_pl\_commands\_supported\_cb(uint32\_t opcodes)

Commands supported callback.

[media\_proxy\_ctrl\_set\_track\_position](group__bt__media__proxy.md#ga776bb5f16cf1f4f6cc3842aabd86b781)

int media\_proxy\_ctrl\_set\_track\_position(struct media\_player \*player, int32\_t position)

Set Track Position.

[media\_proxy\_pl\_track\_duration\_cb](group__bt__media__proxy.md#ga7b0f9633a5322557b91ea97eafac9f34)

void media\_proxy\_pl\_track\_duration\_cb(int32\_t duration)

Track duration callback.

[media\_proxy\_ctrl\_get\_seeking\_speed](group__bt__media__proxy.md#ga817ca4ab611e214493fbc918036def0f)

int media\_proxy\_ctrl\_get\_seeking\_speed(struct media\_player \*player)

Get Seeking Speed.

[media\_proxy\_pl\_media\_state\_cb](group__bt__media__proxy.md#ga842d7951a04702d6f819de44c47b9cac)

void media\_proxy\_pl\_media\_state\_cb(uint8\_t state)

Media state callback.

[media\_proxy\_pl\_search\_cb](group__bt__media__proxy.md#ga8c0d75f61120047bacd0b933534e1b41)

void media\_proxy\_pl\_search\_cb(uint8\_t result\_code)

Search callback.

[media\_proxy\_ctrl\_get\_media\_state](group__bt__media__proxy.md#ga9433aaf24776c30557ea694795e75b3e)

int media\_proxy\_ctrl\_get\_media\_state(struct media\_player \*player)

Read Media State.

[media\_proxy\_pl\_track\_title\_cb](group__bt__media__proxy.md#ga9489b517e4baa215f0b7b59243cee11c)

void media\_proxy\_pl\_track\_title\_cb(char \*title)

Track title callback.

[media\_proxy\_pl\_playing\_order\_cb](group__bt__media__proxy.md#ga96e8156b0267f3d55ee52ab307d81985)

void media\_proxy\_pl\_playing\_order\_cb(uint8\_t order)

Playing order callback.

[media\_proxy\_ctrl\_set\_playing\_order](group__bt__media__proxy.md#gaa4040e97100f6e70527e6ad201309bbe)

int media\_proxy\_ctrl\_set\_playing\_order(struct media\_player \*player, uint8\_t order)

Set Playing Order.

[media\_proxy\_pl\_init](group__bt__media__proxy.md#gab0b10b3de5674f2172e1a2f779cbe8d5)

int media\_proxy\_pl\_init(void)

[media\_proxy\_ctrl\_get\_icon\_url](group__bt__media__proxy.md#gab6df6fe71c8273eca855eb3be27290dd)

int media\_proxy\_ctrl\_get\_icon\_url(struct media\_player \*player)

Read Icon URL.

[media\_proxy\_ctrl\_set\_playback\_speed](group__bt__media__proxy.md#gabafbc857c3e6befe98e339acb58f17fb)

int media\_proxy\_ctrl\_set\_playback\_speed(struct media\_player \*player, int8\_t speed)

Set Playback Speed.

[media\_proxy\_ctrl\_get\_track\_title](group__bt__media__proxy.md#gabfbb49e79204130cb004f217af771b80)

int media\_proxy\_ctrl\_get\_track\_title(struct media\_player \*player)

Read Track Title.

[media\_proxy\_pl\_register](group__bt__media__proxy.md#gac75e27a4a5e169481723cd6b39678274)

int media\_proxy\_pl\_register(struct media\_proxy\_pl\_calls \*pl\_calls)

Register a player with the media proxy.

[media\_proxy\_pl\_current\_group\_id\_cb](group__bt__media__proxy.md#gad02f2924e1aa765c04cbbc6441e7d063)

void media\_proxy\_pl\_current\_group\_id\_cb(uint64\_t id)

Current group object ID callback.

[media\_proxy\_pl\_current\_track\_id\_cb](group__bt__media__proxy.md#gadcad4efdd714159d5d9611bbf74d5fae)

void media\_proxy\_pl\_current\_track\_id\_cb(uint64\_t id)

Current track object ID callback.

[media\_proxy\_pl\_icon\_url\_cb](group__bt__media__proxy.md#gadd348a8d5aff193f7a9113a759e85b1d)

void media\_proxy\_pl\_icon\_url\_cb(const char \*url)

Player icon URL changed callback.

[media\_proxy\_ctrl\_get\_track\_position](group__bt__media__proxy.md#gae0bb75feb49a68b495150c6fba2f21a7)

int media\_proxy\_ctrl\_get\_track\_position(struct media\_player \*player)

Read Track Position.

[media\_proxy\_ctrl\_get\_next\_track\_id](group__bt__media__proxy.md#gae32da32bd504061801730805729242e1)

int media\_proxy\_ctrl\_get\_next\_track\_id(struct media\_player \*player)

Read Next Track Object ID.

[media\_proxy\_ctrl\_set\_current\_group\_id](group__bt__media__proxy.md#gae496885d0124f4e3fc2c0f203fcff118)

int media\_proxy\_ctrl\_set\_current\_group\_id(struct media\_player \*player, uint64\_t id)

Set Current Group Object ID.

[media\_proxy\_ctrl\_set\_current\_track\_id](group__bt__media__proxy.md#gaea6adacedaded10f7c2c0f91b7159f74)

int media\_proxy\_ctrl\_set\_current\_track\_id(struct media\_player \*player, uint64\_t id)

Set Current Track Object ID.

[media\_proxy\_pl\_seeking\_speed\_cb](group__bt__media__proxy.md#gaeaf89f4b760870896ed42687562971ca)

void media\_proxy\_pl\_seeking\_speed\_cb(int8\_t speed)

Seeking speed callback.

[media\_proxy\_ctrl\_get\_current\_track\_id](group__bt__media__proxy.md#gaebe7e3683041e28bef40df75cc991dea)

int media\_proxy\_ctrl\_get\_current\_track\_id(struct media\_player \*player)

Read Current Track Object ID.

[media\_proxy\_pl\_next\_track\_id\_cb](group__bt__media__proxy.md#gaf0bd3447e64b6128710c07461766a0c9)

void media\_proxy\_pl\_next\_track\_id\_cb(uint64\_t id)

Next track object ID callback.

[bt\_mcs\_get\_ots](group__bt__media__proxy.md#gaf535f1ab028407432ef890d278d936e0)

struct bt\_ots \* bt\_mcs\_get\_ots(void)

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[mcs.h](mcs_8h.md)

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[media\_proxy\_ctrl\_cbs](structmedia__proxy__ctrl__cbs.md)

Callbacks to a controller, from the media proxy.

**Definition** media\_proxy.h:255

[media\_proxy\_ctrl\_cbs::search\_recv](structmedia__proxy__ctrl__cbs.md#a0678ad4950c6f526c78d2143e9b7c385)

void(\* search\_recv)(struct media\_player \*player, int err, uint8\_t result\_code)

Search result code receive callback.

**Definition** media\_proxy.h:659

[media\_proxy\_ctrl\_cbs::commands\_supported\_recv](structmedia__proxy__ctrl__cbs.md#a06fadb043fd0a795f872063b7950d414)

void(\* commands\_supported\_recv)(struct media\_player \*player, int err, uint32\_t opcodes)

Commands supported receive callback.

**Definition** media\_proxy.h:628

[media\_proxy\_ctrl\_cbs::next\_track\_id\_write](structmedia__proxy__ctrl__cbs.md#a08b6fe1079b759de1f5a9f7751a22f21)

void(\* next\_track\_id\_write)(struct media\_player \*player, int err, uint64\_t id)

Next Track Object ID write callback.

**Definition** media\_proxy.h:493

[media\_proxy\_ctrl\_cbs::content\_ctrl\_id\_recv](structmedia__proxy__ctrl__cbs.md#a08f3f55a5b56d1ede9141013fe456119)

void(\* content\_ctrl\_id\_recv)(struct media\_player \*player, int err, uint8\_t ccid)

Content Control ID receive callback.

**Definition** media\_proxy.h:685

[media\_proxy\_ctrl\_cbs::seeking\_speed\_recv](structmedia__proxy__ctrl__cbs.md#a2ba0e73f7e67c38f5abe555305753d0f)

void(\* seeking\_speed\_recv)(struct media\_player \*player, int err, int8\_t speed)

Seeking Speed receive callback.

**Definition** media\_proxy.h:426

[media\_proxy\_ctrl\_cbs::parent\_group\_id\_recv](structmedia__proxy__ctrl__cbs.md#a3c2b39bc46f8b2a7155c14dd430add8e)

void(\* parent\_group\_id\_recv)(struct media\_player \*player, int err, uint64\_t id)

Parent Group Object ID receive callback.

**Definition** media\_proxy.h:506

[media\_proxy\_ctrl\_cbs::icon\_url\_recv](structmedia__proxy__ctrl__cbs.md#a53c4809b7a10b9057f565411429d691b)

void(\* icon\_url\_recv)(struct media\_player \*player, int err, const char \*url)

Media Player Icon URL receive callback.

**Definition** media\_proxy.h:322

[media\_proxy\_ctrl\_cbs::track\_position\_write](structmedia__proxy__ctrl__cbs.md#a54f9f50e3b8f99b586a2c522a67da213)

void(\* track\_position\_write)(struct media\_player \*player, int err, int32\_t position)

Track Position write callback.

**Definition** media\_proxy.h:386

[media\_proxy\_ctrl\_cbs::next\_track\_id\_recv](structmedia__proxy__ctrl__cbs.md#a5692c0d142977b8ec7a4ffb765fd0687)

void(\* next\_track\_id\_recv)(struct media\_player \*player, int err, uint64\_t id)

Next Track Object ID receive callback.

**Definition** media\_proxy.h:480

[media\_proxy\_ctrl\_cbs::playback\_speed\_recv](structmedia__proxy__ctrl__cbs.md#a5eb1466e8ba100c9d3cb12f097328b9e)

void(\* playback\_speed\_recv)(struct media\_player \*player, int err, int8\_t speed)

Playback Speed receive callback.

**Definition** media\_proxy.h:400

[media\_proxy\_ctrl\_cbs::current\_track\_id\_write](structmedia__proxy__ctrl__cbs.md#a66f35a59821f53f4ed9aa7dea0e4d654)

void(\* current\_track\_id\_write)(struct media\_player \*player, int err, uint64\_t id)

Current Track Object ID write callback.

**Definition** media\_proxy.h:466

[media\_proxy\_ctrl\_cbs::playing\_order\_write](structmedia__proxy__ctrl__cbs.md#a67cf70c9b72a87b03009f1da0a8980f2)

void(\* playing\_order\_write)(struct media\_player \*player, int err, uint8\_t order)

Playing Order write callback.

**Definition** media\_proxy.h:560

[media\_proxy\_ctrl\_cbs::track\_position\_recv](structmedia__proxy__ctrl__cbs.md#a6aa029523978e02dc1c8c7ff798e2433)

void(\* track\_position\_recv)(struct media\_player \*player, int err, int32\_t position)

Track Position receive callback.

**Definition** media\_proxy.h:373

[media\_proxy\_ctrl\_cbs::playing\_orders\_supported\_recv](structmedia__proxy__ctrl__cbs.md#a85182342b606c78127f2690ac1beab7d)

void(\* playing\_orders\_supported\_recv)(struct media\_player \*player, int err, uint16\_t orders)

Playing Orders Supported receive callback.

**Definition** media\_proxy.h:573

[media\_proxy\_ctrl\_cbs::current\_group\_id\_recv](structmedia__proxy__ctrl__cbs.md#a858a8854259c8e7a09164b916fae309a)

void(\* current\_group\_id\_recv)(struct media\_player \*player, int err, uint64\_t id)

Current Group Object ID receive callback.

**Definition** media\_proxy.h:520

[media\_proxy\_ctrl\_cbs::track\_duration\_recv](structmedia__proxy__ctrl__cbs.md#a85c0bfc83bb26c74b11b5cb8182ff1e0)

void(\* track\_duration\_recv)(struct media\_player \*player, int err, int32\_t duration)

Track Duration receive callback.

**Definition** media\_proxy.h:359

[media\_proxy\_ctrl\_cbs::command\_send](structmedia__proxy__ctrl__cbs.md#a89bb28499c989a9a2ad13d40dda6c6db)

void(\* command\_send)(struct media\_player \*player, int err, const struct mpl\_cmd \*cmd)

Command send callback.

**Definition** media\_proxy.h:601

[media\_proxy\_ctrl\_cbs::command\_recv](structmedia__proxy__ctrl__cbs.md#a90481b6563033a4520b85307e07e2e3a)

void(\* command\_recv)(struct media\_player \*player, int err, const struct mpl\_cmd\_ntf \*result)

Command result receive callback.

**Definition** media\_proxy.h:614

[media\_proxy\_ctrl\_cbs::playing\_order\_recv](structmedia__proxy__ctrl__cbs.md#a92a3b0e3254d6b26e0d18476dce3b01e)

void(\* playing\_order\_recv)(struct media\_player \*player, int err, uint8\_t order)

Playing Order receive callback.

**Definition** media\_proxy.h:547

[media\_proxy\_ctrl\_cbs::player\_name\_recv](structmedia__proxy__ctrl__cbs.md#a94b5ec6bc20299b722bd0e2cb28aed5e)

void(\* player\_name\_recv)(struct media\_player \*player, int err, const char \*name)

Media Player Name receive callback.

**Definition** media\_proxy.h:296

[media\_proxy\_ctrl\_cbs::current\_track\_id\_recv](structmedia__proxy__ctrl__cbs.md#aa3c2bd1734c6235eb2026915dbebc6c2)

void(\* current\_track\_id\_recv)(struct media\_player \*player, int err, uint64\_t id)

Current Track Object ID receive callback.

**Definition** media\_proxy.h:453

[media\_proxy\_ctrl\_cbs::track\_segments\_id\_recv](structmedia__proxy__ctrl__cbs.md#aa7e7f7724689844491a4885544fc450c)

void(\* track\_segments\_id\_recv)(struct media\_player \*player, int err, uint64\_t id)

Track Segments Object ID receive callback.

**Definition** media\_proxy.h:439

[media\_proxy\_ctrl\_cbs::icon\_id\_recv](structmedia__proxy__ctrl__cbs.md#aaa7ba216e604be1c447a93231a0857d0)

void(\* icon\_id\_recv)(struct media\_player \*player, int err, uint64\_t id)

Media Player Icon Object ID receive callback.

**Definition** media\_proxy.h:309

[media\_proxy\_ctrl\_cbs::track\_title\_recv](structmedia__proxy__ctrl__cbs.md#ac1afc71ed04faa87e644d095ef14946f)

void(\* track\_title\_recv)(struct media\_player \*player, int err, const char \*title)

Track Title receive callback.

**Definition** media\_proxy.h:346

[media\_proxy\_ctrl\_cbs::current\_group\_id\_write](structmedia__proxy__ctrl__cbs.md#ad1a65519a958aa27091a2ba41260db04)

void(\* current\_group\_id\_write)(struct media\_player \*player, int err, uint64\_t id)

Current Group Object ID write callback.

**Definition** media\_proxy.h:533

[media\_proxy\_ctrl\_cbs::media\_state\_recv](structmedia__proxy__ctrl__cbs.md#ad4199644afcf356a565b884129ca0cf3)

void(\* media\_state\_recv)(struct media\_player \*player, int err, uint8\_t state)

Media State receive callback.

**Definition** media\_proxy.h:588

[media\_proxy\_ctrl\_cbs::playback\_speed\_write](structmedia__proxy__ctrl__cbs.md#ad84d5caca4be208bd5e5d93f5c801ddf)

void(\* playback\_speed\_write)(struct media\_player \*player, int err, int8\_t speed)

Playback Speed write callback.

**Definition** media\_proxy.h:413

[media\_proxy\_ctrl\_cbs::track\_changed\_recv](structmedia__proxy__ctrl__cbs.md#ade71f132ef66c7bfd13b1b1f3200681d)

void(\* track\_changed\_recv)(struct media\_player \*player, int err)

Track changed receive callback.

**Definition** media\_proxy.h:333

[media\_proxy\_ctrl\_cbs::search\_send](structmedia__proxy__ctrl__cbs.md#aee4a556023d56c3a0d4c2036b3bc0799)

void(\* search\_send)(struct media\_player \*player, int err, const struct mpl\_search \*search)

Search send callback.

**Definition** media\_proxy.h:641

[media\_proxy\_ctrl\_cbs::search\_results\_id\_recv](structmedia__proxy__ctrl__cbs.md#af067e55ef7f676ad3c05f838160ed21e)

void(\* search\_results\_id\_recv)(struct media\_player \*player, int err, uint64\_t id)

Search Results Object ID receive callback See also media\_proxy\_ctrl\_get\_search\_results\_id().

**Definition** media\_proxy.h:672

[media\_proxy\_ctrl\_cbs::local\_player\_instance](structmedia__proxy__ctrl__cbs.md#af2cd0f93aadd451f1b358e2d2d6a0049)

void(\* local\_player\_instance)(struct media\_player \*player, int err)

Media Player Instance callback.

**Definition** media\_proxy.h:268

[media\_proxy\_pl\_calls](structmedia__proxy__pl__calls.md)

Available calls in a player, that the media proxy can call.

**Definition** media\_proxy.h:1117

[media\_proxy\_pl\_calls::set\_track\_position](structmedia__proxy__pl__calls.md#a001ae07161b8a6c7dfc9c2e471f229e5)

void(\* set\_track\_position)(int32\_t position)

Set Track Position.

**Definition** media\_proxy.h:1187

[media\_proxy\_pl\_calls::get\_track\_position](structmedia__proxy__pl__calls.md#a11ea1cf984a7d11ac7e61405df84ee06)

int32\_t(\* get\_track\_position)(void)

Read Track Position.

**Definition** media\_proxy.h:1174

[media\_proxy\_pl\_calls::get\_parent\_group\_id](structmedia__proxy__pl__calls.md#a1409764199d47d0c27d07e13c8fa8f68)

uint64\_t(\* get\_parent\_group\_id)(void)

Read Parent Group Object ID.

**Definition** media\_proxy.h:1308

[media\_proxy\_pl\_calls::get\_track\_duration](structmedia__proxy__pl__calls.md#a1b852ccc45a6ee1174b9d58df3b599b6)

int32\_t(\* get\_track\_duration)(void)

Read Track Duration.

**Definition** media\_proxy.h:1163

[media\_proxy\_pl\_calls::send\_search](structmedia__proxy__pl__calls.md#a416ca20a05a66f4ce28635159173f064)

void(\* send\_search)(const struct mpl\_search \*search)

Set Search.

**Definition** media\_proxy.h:1402

[media\_proxy\_pl\_calls::set\_current\_track\_id](structmedia__proxy__pl__calls.md#a422cec33063313a9aab86baf0bd65ef1)

void(\* set\_current\_track\_id)(uint64\_t id)

Set Current Track Object ID.

**Definition** media\_proxy.h:1274

[media\_proxy\_pl\_calls::set\_current\_group\_id](structmedia__proxy__pl__calls.md#a5049e21965e7fd08aaeafcbedf76809c)

void(\* set\_current\_group\_id)(uint64\_t id)

Set Current Group Object ID.

**Definition** media\_proxy.h:1331

[media\_proxy\_pl\_calls::get\_content\_ctrl\_id](structmedia__proxy__pl__calls.md#a64bc23cc61e69b1b6c4050f76a9bc674)

uint8\_t(\* get\_content\_ctrl\_id)(void)

Read Content Control ID.

**Definition** media\_proxy.h:1427

[media\_proxy\_pl\_calls::get\_media\_state](structmedia__proxy__pl__calls.md#a6a339aa7ee564acacffd2637eeb8e7ea)

uint8\_t(\* get\_media\_state)(void)

Read Media State.

**Definition** media\_proxy.h:1369

[media\_proxy\_pl\_calls::set\_playback\_speed](structmedia__proxy__pl__calls.md#a7535dad9be2f4b83c8a7c55fccc8a7af)

void(\* set\_playback\_speed)(int8\_t speed)

Set Playback Speed.

**Definition** media\_proxy.h:1222

[media\_proxy\_pl\_calls::get\_current\_track\_id](structmedia__proxy__pl__calls.md#a7f19bd75114835d151ff5b26733ed450)

uint64\_t(\* get\_current\_track\_id)(void)

Read Current Track Object ID.

**Definition** media\_proxy.h:1264

[media\_proxy\_pl\_calls::get\_track\_segments\_id](structmedia__proxy__pl__calls.md#a86a71b788b54a4e7c966f162fcab6433)

uint64\_t(\* get\_track\_segments\_id)(void)

Read Current Track Segments Object ID.

**Definition** media\_proxy.h:1251

[media\_proxy\_pl\_calls::get\_playing\_order](structmedia__proxy__pl__calls.md#a98989105d01265de4b268b623a26df2e)

uint8\_t(\* get\_playing\_order)(void)

Read Playing Order.

**Definition** media\_proxy.h:1338

[media\_proxy\_pl\_calls::get\_current\_group\_id](structmedia__proxy__pl__calls.md#a98b02d4689cd5e279f43094f3ca09339)

uint64\_t(\* get\_current\_group\_id)(void)

Read Current Group Object ID.

**Definition** media\_proxy.h:1321

[media\_proxy\_pl\_calls::get\_playing\_orders\_supported](structmedia__proxy__pl__calls.md#a9b733c3187cc032ef6644a16ffd3f7c9)

uint16\_t(\* get\_playing\_orders\_supported)(void)

Read Playing Orders Supported.

**Definition** media\_proxy.h:1359

[media\_proxy\_pl\_calls::send\_command](structmedia__proxy__pl__calls.md#abae1ff89136b93ce4dee5dbe12e6791d)

void(\* send\_command)(const struct mpl\_cmd \*command)

Send Command.

**Definition** media\_proxy.h:1380

[media\_proxy\_pl\_calls::set\_next\_track\_id](structmedia__proxy__pl__calls.md#acbf8dc9dcc8fbaba44d436310c92f3a9)

void(\* set\_next\_track\_id)(uint64\_t id)

Set Next Track Object ID.

**Definition** media\_proxy.h:1293

[media\_proxy\_pl\_calls::get\_icon\_id](structmedia__proxy__pl__calls.md#ad1215725454c6b76dcdc197a275c03cf)

uint64\_t(\* get\_icon\_id)(void)

Read Icon Object ID.

**Definition** media\_proxy.h:1137

[media\_proxy\_pl\_calls::set\_playing\_order](structmedia__proxy__pl__calls.md#ad6fad92957146aeaf1bec0e56606da72)

void(\* set\_playing\_order)(uint8\_t order)

Set Playing Order.

**Definition** media\_proxy.h:1348

[media\_proxy\_pl\_calls::get\_search\_results\_id](structmedia__proxy__pl__calls.md#adf4003ba8ef1a5c38b75876f864564c5)

uint64\_t(\* get\_search\_results\_id)(void)

Read Search Results Object ID.

**Definition** media\_proxy.h:1416

[media\_proxy\_pl\_calls::get\_commands\_supported](structmedia__proxy__pl__calls.md#ae0a4457fcc35d32541f2557698d5aa83)

uint32\_t(\* get\_commands\_supported)(void)

Read Commands Supported.

**Definition** media\_proxy.h:1391

[media\_proxy\_pl\_calls::get\_playback\_speed](structmedia__proxy__pl__calls.md#ae1006d5c684e12e1e1c927f71aa93930)

int8\_t(\* get\_playback\_speed)(void)

Get Playback Speed.

**Definition** media\_proxy.h:1204

[media\_proxy\_pl\_calls::get\_seeking\_speed](structmedia__proxy__pl__calls.md#aebf24b582cf33786f2dc17765d858a15)

int8\_t(\* get\_seeking\_speed)(void)

Get Seeking Speed.

**Definition** media\_proxy.h:1238

[media\_proxy\_pl\_calls::get\_next\_track\_id](structmedia__proxy__pl__calls.md#af939a96fbcfe474dfcdcfb353ae0aac5)

uint64\_t(\* get\_next\_track\_id)(void)

Read Next Track Object ID.

**Definition** media\_proxy.h:1284

[mpl\_cmd\_ntf](structmpl__cmd__ntf.md)

Media command notification.

**Definition** media\_proxy.h:64

[mpl\_cmd\_ntf::result\_code](structmpl__cmd__ntf.md#a776bd9459d320e609697905067c0b284)

uint8\_t result\_code

**Definition** media\_proxy.h:66

[mpl\_cmd\_ntf::requested\_opcode](structmpl__cmd__ntf.md#adcd5228cef8b7629d54053b155a91aa7)

uint8\_t requested\_opcode

**Definition** media\_proxy.h:65

[mpl\_cmd](structmpl__cmd.md)

Media player command.

**Definition** media\_proxy.h:55

[mpl\_cmd::opcode](structmpl__cmd.md#a5cb29ca9e5a6b8249c69cc975b345e2f)

uint8\_t opcode

**Definition** media\_proxy.h:56

[mpl\_cmd::use\_param](structmpl__cmd.md#aca5e50b9f883a3c81f10ad51032a31f9)

bool use\_param

**Definition** media\_proxy.h:57

[mpl\_cmd::param](structmpl__cmd.md#ade5ed4d0ff2aeb192b8ed6b586c9bc9e)

int32\_t param

**Definition** media\_proxy.h:58

[mpl\_sci](structmpl__sci.md)

Search control item.

**Definition** media\_proxy.h:72

[mpl\_sci::type](structmpl__sci.md#a1dfc87f7e8b509ca05cbcd97a245953f)

uint8\_t type

MEDIA\_PROXY\_SEARCH\_TYPE\_<...>.

**Definition** media\_proxy.h:74

[mpl\_sci::len](structmpl__sci.md#a348314407c7b46d5ed583b97dfe932bc)

uint8\_t len

Length of type and parameter.

**Definition** media\_proxy.h:73

[mpl\_sci::param](structmpl__sci.md#abcb13d8005212f480eaaf8a8296f6023)

char param[62]

Search parameter.

**Definition** media\_proxy.h:75

[mpl\_search](structmpl__search.md)

Search.

**Definition** media\_proxy.h:81

[mpl\_search::len](structmpl__search.md#a9b9c64d3d9a25951da58ebf47bb63617)

uint8\_t len

**Definition** media\_proxy.h:82

[mpl\_search::search](structmpl__search.md#aa2332c1802786e2ef0486ede1c3a24c7)

char search[64]

**Definition** media\_proxy.h:83

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [media\_proxy.h](media__proxy_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

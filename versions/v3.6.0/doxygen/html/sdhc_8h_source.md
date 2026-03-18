---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/sdhc_8h_source.html
original_path: doxygen/html/sdhc_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sdhc.h

[Go to the documentation of this file.](sdhc_8h.md)

1/\*

2 \* Copyright 2022 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SDHC\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_SDHC\_H\_

14

15#include <[errno.h](errno_8h.md)>

16#include <[zephyr/device.h](device_8h.md)>

17#include <[zephyr/sd/sd\_spec.h](sd__spec_8h.md)>

18

25

26#ifdef \_\_cplusplus

27extern "C" {

28#endif

29

30

[ 35](group__sdhc__interface.md#gaacc4249f628bcd8967f16713a7def8ae)#define SDHC\_TIMEOUT\_FOREVER (-1)

37

[ 44](structsdhc__command.md)struct [sdhc\_command](structsdhc__command.md) {

[ 45](structsdhc__command.md#a320ad415df67e1d9b4c09f95993dd17f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [opcode](structsdhc__command.md#a320ad415df67e1d9b4c09f95993dd17f);

[ 46](structsdhc__command.md#af6b98d5f1cecf25af2480b1d359f200e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [arg](structsdhc__command.md#af6b98d5f1cecf25af2480b1d359f200e);

[ 47](structsdhc__command.md#a37a3c1608b5c13311c833c4ad24ff1f9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [response](structsdhc__command.md#a37a3c1608b5c13311c833c4ad24ff1f9)[4];

[ 48](structsdhc__command.md#af758a4e0e3b090912f6e9abd7c4be8f3) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [response\_type](structsdhc__command.md#af758a4e0e3b090912f6e9abd7c4be8f3);

[ 49](structsdhc__command.md#a39ba0b1e99814471939dc7bbb7d098eb) unsigned int [retries](structsdhc__command.md#a39ba0b1e99814471939dc7bbb7d098eb);

[ 50](structsdhc__command.md#a92cf023d28aa6106d603ff7f67a7e04b) int [timeout\_ms](structsdhc__command.md#a92cf023d28aa6106d603ff7f67a7e04b);

51};

52

[ 53](group__sdhc__interface.md#gaff462431ff5c38c74c24772cfbccc1fd)#define SDHC\_NATIVE\_RESPONSE\_MASK 0xF

[ 54](group__sdhc__interface.md#ga48071d79eddd5178f4b36756a19a21b2)#define SDHC\_SPI\_RESPONSE\_TYPE\_MASK 0xF0

55

[ 62](structsdhc__data.md)struct [sdhc\_data](structsdhc__data.md) {

[ 63](structsdhc__data.md#aad1e8462d94b4243c981147eab6c962d) unsigned int [block\_addr](structsdhc__data.md#aad1e8462d94b4243c981147eab6c962d);

[ 64](structsdhc__data.md#a20b0ca14adadcdb8d3681240faf5e7b6) unsigned int [block\_size](structsdhc__data.md#a20b0ca14adadcdb8d3681240faf5e7b6);

[ 65](structsdhc__data.md#a47b378d455167bb8d7d05d2f058977fa) unsigned int [blocks](structsdhc__data.md#a47b378d455167bb8d7d05d2f058977fa);

[ 66](structsdhc__data.md#ae68f1e7f1fbff14c24bd42fa300f9e15) unsigned int [bytes\_xfered](structsdhc__data.md#ae68f1e7f1fbff14c24bd42fa300f9e15);

[ 67](structsdhc__data.md#a0f656d093a5cdf3bd09ffee279ad452d) void \*[data](structsdhc__data.md#a0f656d093a5cdf3bd09ffee279ad452d);

[ 68](structsdhc__data.md#afcf3942de27cd164b6da8dfefa864a8a) int [timeout\_ms](structsdhc__data.md#afcf3942de27cd164b6da8dfefa864a8a);

69};

70

[ 78](group__sdhc__interface.md#gaf26909ae9fffdc6ac02abd8094d16dc8)enum [sdhc\_bus\_mode](group__sdhc__interface.md#gaf26909ae9fffdc6ac02abd8094d16dc8) {

[ 79](group__sdhc__interface.md#ggaf26909ae9fffdc6ac02abd8094d16dc8a5408bfd39f7ab8c79735d8a956dc9b1a) [SDHC\_BUSMODE\_OPENDRAIN](group__sdhc__interface.md#ggaf26909ae9fffdc6ac02abd8094d16dc8a5408bfd39f7ab8c79735d8a956dc9b1a) = 1,

[ 80](group__sdhc__interface.md#ggaf26909ae9fffdc6ac02abd8094d16dc8ae47425099c55e2191de84a8cbfa17959) [SDHC\_BUSMODE\_PUSHPULL](group__sdhc__interface.md#ggaf26909ae9fffdc6ac02abd8094d16dc8ae47425099c55e2191de84a8cbfa17959) = 2,

81};

82

[ 90](group__sdhc__interface.md#gad63742820bb18ca18cd2f96547e12eb9)enum [sdhc\_power](group__sdhc__interface.md#gad63742820bb18ca18cd2f96547e12eb9) {

[ 91](group__sdhc__interface.md#ggad63742820bb18ca18cd2f96547e12eb9a621f9456dbce2647567e2e2d049a4c07) [SDHC\_POWER\_OFF](group__sdhc__interface.md#ggad63742820bb18ca18cd2f96547e12eb9a621f9456dbce2647567e2e2d049a4c07) = 1,

[ 92](group__sdhc__interface.md#ggad63742820bb18ca18cd2f96547e12eb9a9442e1400bdfa373a6874cd1434ab604) [SDHC\_POWER\_ON](group__sdhc__interface.md#ggad63742820bb18ca18cd2f96547e12eb9a9442e1400bdfa373a6874cd1434ab604) = 2,

93};

94

[ 101](group__sdhc__interface.md#gad8bab66ec505c8356fac7785a8955448)enum [sdhc\_bus\_width](group__sdhc__interface.md#gad8bab66ec505c8356fac7785a8955448) {

[ 102](group__sdhc__interface.md#ggad8bab66ec505c8356fac7785a8955448a875995b349ed5c81e6f34569c35079a0) [SDHC\_BUS\_WIDTH1BIT](group__sdhc__interface.md#ggad8bab66ec505c8356fac7785a8955448a875995b349ed5c81e6f34569c35079a0) = 1U,

[ 103](group__sdhc__interface.md#ggad8bab66ec505c8356fac7785a8955448a4e679800f8863d5650827a0330ef22b6) [SDHC\_BUS\_WIDTH4BIT](group__sdhc__interface.md#ggad8bab66ec505c8356fac7785a8955448a4e679800f8863d5650827a0330ef22b6) = 4U,

[ 104](group__sdhc__interface.md#ggad8bab66ec505c8356fac7785a8955448a2b28e7702abe63e03d2b77994d30e156) [SDHC\_BUS\_WIDTH8BIT](group__sdhc__interface.md#ggad8bab66ec505c8356fac7785a8955448a2b28e7702abe63e03d2b77994d30e156) = 8U,

105};

106

[ 114](group__sdhc__interface.md#ga6f006ca8fd9ff8a68ac46a0bb7d4bc90)enum [sdhc\_timing\_mode](group__sdhc__interface.md#ga6f006ca8fd9ff8a68ac46a0bb7d4bc90) {

[ 115](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a8c5c11b75f76771dfedebc6d4a844e55) [SDHC\_TIMING\_LEGACY](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a8c5c11b75f76771dfedebc6d4a844e55) = 1U,

[ 117](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90af5f82fc8f4b281e44b5e78f229d9564b) [SDHC\_TIMING\_HS](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90af5f82fc8f4b281e44b5e78f229d9564b) = 2U,

[ 119](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90aa48069d7a8a43308d308c9fe67543d86) [SDHC\_TIMING\_SDR12](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90aa48069d7a8a43308d308c9fe67543d86) = 3U,

[ 121](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a8c77db56b6a006c1cff9f70e20f6d016) [SDHC\_TIMING\_SDR25](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a8c77db56b6a006c1cff9f70e20f6d016) = 4U,

[ 123](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a836ffb1abaf681d2992c8c906f5e2c94) [SDHC\_TIMING\_SDR50](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a836ffb1abaf681d2992c8c906f5e2c94) = 5U,

[ 125](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90ae2b69f73212e34bbbfb1c02c27740bd1) [SDHC\_TIMING\_SDR104](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90ae2b69f73212e34bbbfb1c02c27740bd1) = 6U,

[ 127](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90afc9b5aa9339c4ffdea8d6452c10ba5fa) [SDHC\_TIMING\_DDR50](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90afc9b5aa9339c4ffdea8d6452c10ba5fa) = 7U,

[ 129](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a80c5035dc9976f8ee4d7b1f20f21e692) [SDHC\_TIMING\_DDR52](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a80c5035dc9976f8ee4d7b1f20f21e692) = 8U,

[ 131](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90ae892594e6a91a70ade2dc983bda2d145) [SDHC\_TIMING\_HS200](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90ae892594e6a91a70ade2dc983bda2d145) = 9U,

[ 133](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a56909869d92eb1c212051c8a23449ebc) [SDHC\_TIMING\_HS400](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a56909869d92eb1c212051c8a23449ebc) = 10U,

135};

136

[ 144](group__sdhc__interface.md#ga34041edf280f125b8500809226b3de5d)enum [sd\_voltage](group__sdhc__interface.md#ga34041edf280f125b8500809226b3de5d) {

[ 145](group__sdhc__interface.md#gga34041edf280f125b8500809226b3de5da186c3fbdedaf8840a8204d770de1e56d) [SD\_VOL\_3\_3\_V](group__sdhc__interface.md#gga34041edf280f125b8500809226b3de5da186c3fbdedaf8840a8204d770de1e56d) = 1U,

[ 147](group__sdhc__interface.md#gga34041edf280f125b8500809226b3de5daad6c30a3ea2280c9235ba538b52edf11) [SD\_VOL\_3\_0\_V](group__sdhc__interface.md#gga34041edf280f125b8500809226b3de5daad6c30a3ea2280c9235ba538b52edf11) = 2U,

[ 149](group__sdhc__interface.md#gga34041edf280f125b8500809226b3de5dafeed0c640efe6df6f13f76b95138373d) [SD\_VOL\_1\_8\_V](group__sdhc__interface.md#gga34041edf280f125b8500809226b3de5dafeed0c640efe6df6f13f76b95138373d) = 3U,

[ 151](group__sdhc__interface.md#gga34041edf280f125b8500809226b3de5da6dd8c2d9590dfe38bb77a21c350d36af) [SD\_VOL\_1\_2\_V](group__sdhc__interface.md#gga34041edf280f125b8500809226b3de5da6dd8c2d9590dfe38bb77a21c350d36af) = 4U,

153};

154

[ 161](structsdhc__host__caps.md)struct [sdhc\_host\_caps](structsdhc__host__caps.md) {

[ 162](structsdhc__host__caps.md#a3a57e12aa8f53ad1c1fb44696622f587) unsigned int [timeout\_clk\_freq](structsdhc__host__caps.md#a3a57e12aa8f53ad1c1fb44696622f587): 5;

163 unsigned int \_rsvd\_6: 1;

[ 164](structsdhc__host__caps.md#a8af558ed3b7af437f1782aea9ee6794e) unsigned int [timeout\_clk\_unit](structsdhc__host__caps.md#a8af558ed3b7af437f1782aea9ee6794e): 1;

[ 165](structsdhc__host__caps.md#a20ada015fecce002d233fefac5c4ead4) unsigned int [sd\_base\_clk](structsdhc__host__caps.md#a20ada015fecce002d233fefac5c4ead4): 8;

[ 166](structsdhc__host__caps.md#a97dbad3360b56a44fb1ab0d77aa90bc4) unsigned int [max\_blk\_len](structsdhc__host__caps.md#a97dbad3360b56a44fb1ab0d77aa90bc4): 2;

[ 167](structsdhc__host__caps.md#ad09f103fc8ce341d25e1f824e97bd665) unsigned int [bus\_8\_bit\_support](structsdhc__host__caps.md#ad09f103fc8ce341d25e1f824e97bd665): 1;

[ 168](structsdhc__host__caps.md#a70b8180301c72db291b9d53bf5379655) unsigned int [bus\_4\_bit\_support](structsdhc__host__caps.md#a70b8180301c72db291b9d53bf5379655): 1;

[ 169](structsdhc__host__caps.md#acfa1c5e96f2afeab40185a1ef37d7efb) unsigned int [adma\_2\_support](structsdhc__host__caps.md#acfa1c5e96f2afeab40185a1ef37d7efb): 1;

170 unsigned int \_rsvd\_20: 1;

[ 171](structsdhc__host__caps.md#aaec0cd01cc4e8bf334e5c3ee151d5d98) unsigned int [high\_spd\_support](structsdhc__host__caps.md#aaec0cd01cc4e8bf334e5c3ee151d5d98): 1;

[ 172](structsdhc__host__caps.md#a22f2877854669589f0483cf91e504df6) unsigned int [sdma\_support](structsdhc__host__caps.md#a22f2877854669589f0483cf91e504df6): 1;

[ 173](structsdhc__host__caps.md#af343879ebc21f5c2d57ffa962dacb796) unsigned int [suspend\_res\_support](structsdhc__host__caps.md#af343879ebc21f5c2d57ffa962dacb796): 1;

[ 174](structsdhc__host__caps.md#ac6e2eb088ed7d7c3f3f5011ad55ba543) unsigned int [vol\_330\_support](structsdhc__host__caps.md#ac6e2eb088ed7d7c3f3f5011ad55ba543): 1;

[ 175](structsdhc__host__caps.md#a7fdf6832fbcc9dce7e20ee87d9063665) unsigned int [vol\_300\_support](structsdhc__host__caps.md#a7fdf6832fbcc9dce7e20ee87d9063665): 1;

[ 176](structsdhc__host__caps.md#aa39ef2d70314dbf2517bd3df6fbd4694) unsigned int [vol\_180\_support](structsdhc__host__caps.md#aa39ef2d70314dbf2517bd3df6fbd4694): 1;

[ 177](structsdhc__host__caps.md#ad8e4ca0d2fb39486b469224218d2eb7b) unsigned int [address\_64\_bit\_support\_v4](structsdhc__host__caps.md#ad8e4ca0d2fb39486b469224218d2eb7b): 1;

[ 178](structsdhc__host__caps.md#a0f33c7e168ade12675795d2c0d5b5ea2) unsigned int [address\_64\_bit\_support\_v3](structsdhc__host__caps.md#a0f33c7e168ade12675795d2c0d5b5ea2): 1;

[ 179](structsdhc__host__caps.md#a6fa0525ee3b2a0313cc9b83dc820b831) unsigned int [sdio\_async\_interrupt\_support](structsdhc__host__caps.md#a6fa0525ee3b2a0313cc9b83dc820b831): 1;

[ 180](structsdhc__host__caps.md#a3231007bc5fcc731e97236b29333f7ee) unsigned int [slot\_type](structsdhc__host__caps.md#a3231007bc5fcc731e97236b29333f7ee): 2;

[ 181](structsdhc__host__caps.md#a63dabbc7c24dc41c8103be81ee6e673f) unsigned int [sdr50\_support](structsdhc__host__caps.md#a63dabbc7c24dc41c8103be81ee6e673f): 1;

[ 182](structsdhc__host__caps.md#a3e6f73ea9df9c207cddda31de45621be) unsigned int [sdr104\_support](structsdhc__host__caps.md#a3e6f73ea9df9c207cddda31de45621be): 1;

[ 183](structsdhc__host__caps.md#aa22adb0079aa3864df4461d841852684) unsigned int [ddr50\_support](structsdhc__host__caps.md#aa22adb0079aa3864df4461d841852684): 1;

[ 184](structsdhc__host__caps.md#a146c7403d7ecbbffbd6aa0c1c4fad1b5) unsigned int [uhs\_2\_support](structsdhc__host__caps.md#a146c7403d7ecbbffbd6aa0c1c4fad1b5): 1;

[ 185](structsdhc__host__caps.md#a43086e5bc5d6384b8eb0709c1cf1756e) unsigned int [drv\_type\_a\_support](structsdhc__host__caps.md#a43086e5bc5d6384b8eb0709c1cf1756e): 1;

[ 186](structsdhc__host__caps.md#aafcfb75fd131430df0a372e6ac2c8b34) unsigned int [drv\_type\_c\_support](structsdhc__host__caps.md#aafcfb75fd131430df0a372e6ac2c8b34): 1;

[ 187](structsdhc__host__caps.md#ad2c9e66bbd9a442d872fd559fd7a833c) unsigned int [drv\_type\_d\_support](structsdhc__host__caps.md#ad2c9e66bbd9a442d872fd559fd7a833c): 1;

188 unsigned int \_rsvd\_39: 1;

[ 189](structsdhc__host__caps.md#ab7a145bf44747d7d9e68ff743520cc2c) unsigned int [retune\_timer\_count](structsdhc__host__caps.md#ab7a145bf44747d7d9e68ff743520cc2c): 4;

[ 190](structsdhc__host__caps.md#ac54a191e04ff6c266390d1fb8d4f84d3) unsigned int [sdr50\_needs\_tuning](structsdhc__host__caps.md#ac54a191e04ff6c266390d1fb8d4f84d3): 1;

[ 191](structsdhc__host__caps.md#a48680d522d417e68ec3371b3831faa01) unsigned int [retuning\_mode](structsdhc__host__caps.md#a48680d522d417e68ec3371b3831faa01): 2;

[ 192](structsdhc__host__caps.md#afffade3ad661ead23ed0f74b770172ff) unsigned int [clk\_multiplier](structsdhc__host__caps.md#afffade3ad661ead23ed0f74b770172ff): 8;

193 unsigned int \_rsvd\_56: 3;

[ 194](structsdhc__host__caps.md#a90a90218bcd866cbfae2354c5b0af3de) unsigned int [adma3\_support](structsdhc__host__caps.md#a90a90218bcd866cbfae2354c5b0af3de): 1;

[ 195](structsdhc__host__caps.md#a2f5d5859cbe06ab449f95c0a108c2250) unsigned int [vdd2\_180\_support](structsdhc__host__caps.md#a2f5d5859cbe06ab449f95c0a108c2250): 1;

196 unsigned int \_rsvd\_61: 3;

[ 197](structsdhc__host__caps.md#a956a426ca18a02aa4c81e7b2c576531c) unsigned int [hs200\_support](structsdhc__host__caps.md#a956a426ca18a02aa4c81e7b2c576531c): 1;

[ 198](structsdhc__host__caps.md#ad23716b3541a99dfe935e06aa9c8f256) unsigned int [hs400\_support](structsdhc__host__caps.md#ad23716b3541a99dfe935e06aa9c8f256): 1;

199};

200

[ 208](structsdhc__io.md)struct [sdhc\_io](structsdhc__io.md) {

[ 209](structsdhc__io.md#aaa15197b8f1947a67dcd8522aa62afc5) enum [sdhc\_clock\_speed](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539) [clock](structsdhc__io.md#aaa15197b8f1947a67dcd8522aa62afc5);

[ 210](structsdhc__io.md#a2b4456b108778aada0d42b8c8107b3e9) enum [sdhc\_bus\_mode](group__sdhc__interface.md#gaf26909ae9fffdc6ac02abd8094d16dc8) [bus\_mode](structsdhc__io.md#a2b4456b108778aada0d42b8c8107b3e9);

[ 211](structsdhc__io.md#ac503fb9fba7ffdb01695a77780972930) enum [sdhc\_power](group__sdhc__interface.md#gad63742820bb18ca18cd2f96547e12eb9) [power\_mode](structsdhc__io.md#ac503fb9fba7ffdb01695a77780972930);

[ 212](structsdhc__io.md#a904b05c7e73e80bb7326b0bfcb6b7103) enum [sdhc\_bus\_width](group__sdhc__interface.md#gad8bab66ec505c8356fac7785a8955448) [bus\_width](structsdhc__io.md#a904b05c7e73e80bb7326b0bfcb6b7103);

[ 213](structsdhc__io.md#a85c50f625d8606bb4c07a228c0de24e4) enum [sdhc\_timing\_mode](group__sdhc__interface.md#ga6f006ca8fd9ff8a68ac46a0bb7d4bc90) [timing](structsdhc__io.md#a85c50f625d8606bb4c07a228c0de24e4);

[ 214](structsdhc__io.md#a0c62aaa1a8a7700ebb00a38ce2e57d11) enum [sd\_driver\_type](sd__spec_8h.md#a314c38b1b0603c003e67b5dec2228d4b) [driver\_type](structsdhc__io.md#a0c62aaa1a8a7700ebb00a38ce2e57d11);

[ 215](structsdhc__io.md#ade8b8cd4e4f4b21f5fa8e3fb2661917e) enum [sd\_voltage](group__sdhc__interface.md#ga34041edf280f125b8500809226b3de5d) [signal\_voltage](structsdhc__io.md#ade8b8cd4e4f4b21f5fa8e3fb2661917e);

216};

217

[ 223](structsdhc__host__props.md)struct [sdhc\_host\_props](structsdhc__host__props.md) {

[ 224](structsdhc__host__props.md#aef7123dfa5690bc0525aa40dc623307c) unsigned int [f\_max](structsdhc__host__props.md#aef7123dfa5690bc0525aa40dc623307c);

[ 225](structsdhc__host__props.md#a28c69ba3fdae1393daa551f3f9b91057) unsigned int [f\_min](structsdhc__host__props.md#a28c69ba3fdae1393daa551f3f9b91057);

[ 226](structsdhc__host__props.md#a7f7b22b7b8fb46df0ec19e2bef2a4702) unsigned int [power\_delay](structsdhc__host__props.md#a7f7b22b7b8fb46df0ec19e2bef2a4702);

[ 227](structsdhc__host__props.md#ad60bf89e594a031f6be015888466a113) struct [sdhc\_host\_caps](structsdhc__host__caps.md) [host\_caps](structsdhc__host__props.md#ad60bf89e594a031f6be015888466a113);

[ 228](structsdhc__host__props.md#afebe4aad820c1672635fd30aacec20e4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_current\_330](structsdhc__host__props.md#afebe4aad820c1672635fd30aacec20e4);

[ 229](structsdhc__host__props.md#ac247312c9b10768fe878afc5c85d9eba) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_current\_300](structsdhc__host__props.md#ac247312c9b10768fe878afc5c85d9eba);

[ 230](structsdhc__host__props.md#a43d2b80ec0a5682783e4297c734a3c88) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_current\_180](structsdhc__host__props.md#a43d2b80ec0a5682783e4297c734a3c88);

[ 231](structsdhc__host__props.md#abb18e33d99ed1e4a4400dccd2149816f) bool [is\_spi](structsdhc__host__props.md#abb18e33d99ed1e4a4400dccd2149816f);

232};

233

[ 239](group__sdhc__interface.md#gab449b2f6b41e791d327f7d92b2b58c2d)enum [sdhc\_interrupt\_source](group__sdhc__interface.md#gab449b2f6b41e791d327f7d92b2b58c2d) {

[ 240](group__sdhc__interface.md#ggab449b2f6b41e791d327f7d92b2b58c2dae3a741e98cdb1e8c0ddc8c3baaf64b59) [SDHC\_INT\_SDIO](group__sdhc__interface.md#ggab449b2f6b41e791d327f7d92b2b58c2dae3a741e98cdb1e8c0ddc8c3baaf64b59) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 241](group__sdhc__interface.md#ggab449b2f6b41e791d327f7d92b2b58c2dab9df16a6ed1c7961bb9cab34ebe99f87) [SDHC\_INT\_INSERTED](group__sdhc__interface.md#ggab449b2f6b41e791d327f7d92b2b58c2dab9df16a6ed1c7961bb9cab34ebe99f87) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 242](group__sdhc__interface.md#ggab449b2f6b41e791d327f7d92b2b58c2da6e0a03105c6aba203daa53acb6b7c15c) [SDHC\_INT\_REMOVED](group__sdhc__interface.md#ggab449b2f6b41e791d327f7d92b2b58c2da6e0a03105c6aba203daa53acb6b7c15c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

243};

244

[ 254](group__sdhc__interface.md#ga5d207e3b3d76ed9dbfa7d68a92755cbe)typedef void (\*[sdhc\_interrupt\_cb\_t](group__sdhc__interface.md#ga5d207e3b3d76ed9dbfa7d68a92755cbe))(const struct [device](structdevice.md) \*dev, int reason,

255 const void \*user\_data);

256

[ 257](structsdhc__driver__api.md)\_\_subsystem struct [sdhc\_driver\_api](structsdhc__driver__api.md) {

[ 258](structsdhc__driver__api.md#ac034dfc17e064170e76280394005c76c) int (\*[reset](structsdhc__driver__api.md#ac034dfc17e064170e76280394005c76c))(const struct [device](structdevice.md) \*dev);

[ 259](structsdhc__driver__api.md#a577d162b282b2f9eeb91cf07e7578905) int (\*[request](structsdhc__driver__api.md#a577d162b282b2f9eeb91cf07e7578905))(const struct [device](structdevice.md) \*dev,

260 struct [sdhc\_command](structsdhc__command.md) \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

261 struct [sdhc\_data](structsdhc__data.md) \*data);

[ 262](structsdhc__driver__api.md#adb40a93f64a1a8dc1548a4651091ecf9) int (\*[set\_io](structsdhc__driver__api.md#adb40a93f64a1a8dc1548a4651091ecf9))(const struct [device](structdevice.md) \*dev, struct [sdhc\_io](structsdhc__io.md) \*ios);

[ 263](structsdhc__driver__api.md#a06fb6fdfd0c528056c36476f914f94c9) int (\*[get\_card\_present](structsdhc__driver__api.md#a06fb6fdfd0c528056c36476f914f94c9))(const struct [device](structdevice.md) \*dev);

[ 264](structsdhc__driver__api.md#a6075f8ef38200e700ec133fbeb8c8121) int (\*[execute\_tuning](structsdhc__driver__api.md#a6075f8ef38200e700ec133fbeb8c8121))(const struct [device](structdevice.md) \*dev);

[ 265](structsdhc__driver__api.md#ac642c06d5ec9f697be8fa46cede3bc64) int (\*[card\_busy](structsdhc__driver__api.md#ac642c06d5ec9f697be8fa46cede3bc64))(const struct [device](structdevice.md) \*dev);

[ 266](structsdhc__driver__api.md#af2b83b0ea2afbbdf065b5919c6b822c2) int (\*[get\_host\_props](structsdhc__driver__api.md#af2b83b0ea2afbbdf065b5919c6b822c2))(const struct [device](structdevice.md) \*dev,

267 struct [sdhc\_host\_props](structsdhc__host__props.md) \*props);

[ 268](structsdhc__driver__api.md#a42941f226f2adfe5b8275923bff434ff) int (\*[enable\_interrupt](structsdhc__driver__api.md#a42941f226f2adfe5b8275923bff434ff))(const struct [device](structdevice.md) \*dev,

269 [sdhc\_interrupt\_cb\_t](group__sdhc__interface.md#ga5d207e3b3d76ed9dbfa7d68a92755cbe) callback,

270 int sources, void \*user\_data);

[ 271](structsdhc__driver__api.md#aa50466e31e01d639e459bab204cf1ee5) int (\*[disable\_interrupt](structsdhc__driver__api.md#aa50466e31e01d639e459bab204cf1ee5))(const struct [device](structdevice.md) \*dev, int sources);

272};

273

[ 286](group__sdhc__interface.md#gad6b082a75f1272620b79a7d3a08862f7)\_\_syscall int [sdhc\_hw\_reset](group__sdhc__interface.md#gad6b082a75f1272620b79a7d3a08862f7)(const struct [device](structdevice.md) \*dev);

287

288static inline int z\_impl\_sdhc\_hw\_reset(const struct [device](structdevice.md) \*dev)

289{

290 const struct [sdhc\_driver\_api](structsdhc__driver__api.md) \*api = (const struct [sdhc\_driver\_api](structsdhc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

291

292 if (!api->reset) {

293 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

294 }

295

296 return api->reset(dev);

297}

298

299

[ 313](group__sdhc__interface.md#gac708d55e92a7705f92b90ee6baa65f74)\_\_syscall int [sdhc\_request](group__sdhc__interface.md#gac708d55e92a7705f92b90ee6baa65f74)(const struct [device](structdevice.md) \*dev, struct [sdhc\_command](structsdhc__command.md) \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

314 struct [sdhc\_data](structsdhc__data.md) \*data);

315

316static inline int z\_impl\_sdhc\_request(const struct [device](structdevice.md) \*dev,

317 struct [sdhc\_command](structsdhc__command.md) \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

318 struct [sdhc\_data](structsdhc__data.md) \*data)

319{

320 const struct [sdhc\_driver\_api](structsdhc__driver__api.md) \*api = (const struct [sdhc\_driver\_api](structsdhc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

321

322 if (!api->request) {

323 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

324 }

325

326 return api->request(dev, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), data);

327}

328

[ 341](group__sdhc__interface.md#ga0e6d8259cca442bd1356d00f668d35c4)\_\_syscall int [sdhc\_set\_io](group__sdhc__interface.md#ga0e6d8259cca442bd1356d00f668d35c4)(const struct [device](structdevice.md) \*dev, struct [sdhc\_io](structsdhc__io.md) \*io);

342

343static inline int z\_impl\_sdhc\_set\_io(const struct [device](structdevice.md) \*dev,

344 struct [sdhc\_io](structsdhc__io.md) \*io)

345{

346 const struct [sdhc\_driver\_api](structsdhc__driver__api.md) \*api = (const struct [sdhc\_driver\_api](structsdhc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

347

348 if (!api->set\_io) {

349 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

350 }

351

352 return api->set\_io(dev, io);

353}

354

[ 366](group__sdhc__interface.md#ga85184688da845759dbfb706aac5eac7d)\_\_syscall int [sdhc\_card\_present](group__sdhc__interface.md#ga85184688da845759dbfb706aac5eac7d)(const struct [device](structdevice.md) \*dev);

367

368static inline int z\_impl\_sdhc\_card\_present(const struct [device](structdevice.md) \*dev)

369{

370 const struct [sdhc\_driver\_api](structsdhc__driver__api.md) \*api = (const struct [sdhc\_driver\_api](structsdhc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

371

372 if (!api->get\_card\_present) {

373 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

374 }

375

376 return api->get\_card\_present(dev);

377}

378

379

[ 391](group__sdhc__interface.md#gab5c2711c99573e031938faaa41862971)\_\_syscall int [sdhc\_execute\_tuning](group__sdhc__interface.md#gab5c2711c99573e031938faaa41862971)(const struct [device](structdevice.md) \*dev);

392

393static inline int z\_impl\_sdhc\_execute\_tuning(const struct [device](structdevice.md) \*dev)

394{

395 const struct [sdhc\_driver\_api](structsdhc__driver__api.md) \*api = (const struct [sdhc\_driver\_api](structsdhc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

396

397 if (!api->execute\_tuning) {

398 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

399 }

400

401 return api->execute\_tuning(dev);

402}

403

[ 415](group__sdhc__interface.md#ga91acdc4a6bc2aecc988fdde6ee61ed46)\_\_syscall int [sdhc\_card\_busy](group__sdhc__interface.md#ga91acdc4a6bc2aecc988fdde6ee61ed46)(const struct [device](structdevice.md) \*dev);

416

417static inline int z\_impl\_sdhc\_card\_busy(const struct [device](structdevice.md) \*dev)

418{

419 const struct [sdhc\_driver\_api](structsdhc__driver__api.md) \*api = (const struct [sdhc\_driver\_api](structsdhc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

420

421 if (!api->card\_busy) {

422 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

423 }

424

425 return api->card\_busy(dev);

426}

427

428

[ 439](group__sdhc__interface.md#gab55cf88ae79e5aa9e2110b298048df8e)\_\_syscall int [sdhc\_get\_host\_props](group__sdhc__interface.md#gab55cf88ae79e5aa9e2110b298048df8e)(const struct [device](structdevice.md) \*dev,

440 struct [sdhc\_host\_props](structsdhc__host__props.md) \*props);

441

442static inline int z\_impl\_sdhc\_get\_host\_props(const struct [device](structdevice.md) \*dev,

443 struct [sdhc\_host\_props](structsdhc__host__props.md) \*props)

444{

445 const struct [sdhc\_driver\_api](structsdhc__driver__api.md) \*api = (const struct [sdhc\_driver\_api](structsdhc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

446

447 if (!api->get\_host\_props) {

448 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

449 }

450

451 return api->get\_host\_props(dev, props);

452}

453

[ 469](group__sdhc__interface.md#ga8e4beb1135aa5c0d32f999ca953224d2)\_\_syscall int [sdhc\_enable\_interrupt](group__sdhc__interface.md#ga8e4beb1135aa5c0d32f999ca953224d2)(const struct [device](structdevice.md) \*dev,

470 [sdhc\_interrupt\_cb\_t](group__sdhc__interface.md#ga5d207e3b3d76ed9dbfa7d68a92755cbe) callback,

471 int sources, void \*user\_data);

472

473static inline int z\_impl\_sdhc\_enable\_interrupt(const struct [device](structdevice.md) \*dev,

474 [sdhc\_interrupt\_cb\_t](group__sdhc__interface.md#ga5d207e3b3d76ed9dbfa7d68a92755cbe) callback,

475 int sources, void \*user\_data)

476{

477 const struct [sdhc\_driver\_api](structsdhc__driver__api.md) \*api = (const struct [sdhc\_driver\_api](structsdhc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

478

479 if (!api->enable\_interrupt) {

480 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

481 }

482

483 return api->enable\_interrupt(dev, callback, sources, user\_data);

484}

485

[ 498](group__sdhc__interface.md#ga6264f62c6427973749c8d49fb908f569)\_\_syscall int [sdhc\_disable\_interrupt](group__sdhc__interface.md#ga6264f62c6427973749c8d49fb908f569)(const struct [device](structdevice.md) \*dev, int sources);

499

500static inline int z\_impl\_sdhc\_disable\_interrupt(const struct [device](structdevice.md) \*dev,

501 int sources)

502{

503 const struct [sdhc\_driver\_api](structsdhc__driver__api.md) \*api = (const struct [sdhc\_driver\_api](structsdhc__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

504

505 if (!api->disable\_interrupt) {

506 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

507 }

508

509 return api->disable\_interrupt(dev, sources);

510}

511

515

516#ifdef \_\_cplusplus

517}

518#endif

519

520#include <syscalls/sdhc.h>

521#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SDHC\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[sdhc\_set\_io](group__sdhc__interface.md#ga0e6d8259cca442bd1356d00f668d35c4)

int sdhc\_set\_io(const struct device \*dev, struct sdhc\_io \*io)

set I/O properties of SDHC

[sd\_voltage](group__sdhc__interface.md#ga34041edf280f125b8500809226b3de5d)

sd\_voltage

SD voltage.

**Definition** sdhc.h:144

[sdhc\_interrupt\_cb\_t](group__sdhc__interface.md#ga5d207e3b3d76ed9dbfa7d68a92755cbe)

void(\* sdhc\_interrupt\_cb\_t)(const struct device \*dev, int reason, const void \*user\_data)

SDHC card interrupt callback prototype.

**Definition** sdhc.h:254

[sdhc\_disable\_interrupt](group__sdhc__interface.md#ga6264f62c6427973749c8d49fb908f569)

int sdhc\_disable\_interrupt(const struct device \*dev, int sources)

Disable SDHC interrupt sources.

[sdhc\_timing\_mode](group__sdhc__interface.md#ga6f006ca8fd9ff8a68ac46a0bb7d4bc90)

sdhc\_timing\_mode

SD host controller timing mode.

**Definition** sdhc.h:114

[sdhc\_card\_present](group__sdhc__interface.md#ga85184688da845759dbfb706aac5eac7d)

int sdhc\_card\_present(const struct device \*dev)

check for SDHC card presence

[sdhc\_enable\_interrupt](group__sdhc__interface.md#ga8e4beb1135aa5c0d32f999ca953224d2)

int sdhc\_enable\_interrupt(const struct device \*dev, sdhc\_interrupt\_cb\_t callback, int sources, void \*user\_data)

Enable SDHC interrupt sources.

[sdhc\_card\_busy](group__sdhc__interface.md#ga91acdc4a6bc2aecc988fdde6ee61ed46)

int sdhc\_card\_busy(const struct device \*dev)

check if SD card is busy

[sdhc\_interrupt\_source](group__sdhc__interface.md#gab449b2f6b41e791d327f7d92b2b58c2d)

sdhc\_interrupt\_source

SD host controller interrupt sources.

**Definition** sdhc.h:239

[sdhc\_get\_host\_props](group__sdhc__interface.md#gab55cf88ae79e5aa9e2110b298048df8e)

int sdhc\_get\_host\_props(const struct device \*dev, struct sdhc\_host\_props \*props)

Get SD host controller properties.

[sdhc\_execute\_tuning](group__sdhc__interface.md#gab5c2711c99573e031938faaa41862971)

int sdhc\_execute\_tuning(const struct device \*dev)

run SDHC tuning

[sdhc\_request](group__sdhc__interface.md#gac708d55e92a7705f92b90ee6baa65f74)

int sdhc\_request(const struct device \*dev, struct sdhc\_command \*cmd, struct sdhc\_data \*data)

Send command to SDHC.

[sdhc\_power](group__sdhc__interface.md#gad63742820bb18ca18cd2f96547e12eb9)

sdhc\_power

SD host controller power.

**Definition** sdhc.h:90

[sdhc\_hw\_reset](group__sdhc__interface.md#gad6b082a75f1272620b79a7d3a08862f7)

int sdhc\_hw\_reset(const struct device \*dev)

reset SDHC controller state

[sdhc\_bus\_width](group__sdhc__interface.md#gad8bab66ec505c8356fac7785a8955448)

sdhc\_bus\_width

SD host controller bus width.

**Definition** sdhc.h:101

[sdhc\_bus\_mode](group__sdhc__interface.md#gaf26909ae9fffdc6ac02abd8094d16dc8)

sdhc\_bus\_mode

SD bus mode.

**Definition** sdhc.h:78

[SD\_VOL\_3\_3\_V](group__sdhc__interface.md#gga34041edf280f125b8500809226b3de5da186c3fbdedaf8840a8204d770de1e56d)

@ SD\_VOL\_3\_3\_V

card operation voltage around 3.3v

**Definition** sdhc.h:145

[SD\_VOL\_1\_2\_V](group__sdhc__interface.md#gga34041edf280f125b8500809226b3de5da6dd8c2d9590dfe38bb77a21c350d36af)

@ SD\_VOL\_1\_2\_V

card operation voltage around 1.2v

**Definition** sdhc.h:151

[SD\_VOL\_3\_0\_V](group__sdhc__interface.md#gga34041edf280f125b8500809226b3de5daad6c30a3ea2280c9235ba538b52edf11)

@ SD\_VOL\_3\_0\_V

card operation voltage around 3.0v

**Definition** sdhc.h:147

[SD\_VOL\_1\_8\_V](group__sdhc__interface.md#gga34041edf280f125b8500809226b3de5dafeed0c640efe6df6f13f76b95138373d)

@ SD\_VOL\_1\_8\_V

card operation voltage around 1.8v

**Definition** sdhc.h:149

[SDHC\_TIMING\_HS400](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a56909869d92eb1c212051c8a23449ebc)

@ SDHC\_TIMING\_HS400

HS400 mode.

**Definition** sdhc.h:133

[SDHC\_TIMING\_DDR52](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a80c5035dc9976f8ee4d7b1f20f21e692)

@ SDHC\_TIMING\_DDR52

DDR52 mode.

**Definition** sdhc.h:129

[SDHC\_TIMING\_SDR50](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a836ffb1abaf681d2992c8c906f5e2c94)

@ SDHC\_TIMING\_SDR50

SDR49 mode.

**Definition** sdhc.h:123

[SDHC\_TIMING\_LEGACY](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a8c5c11b75f76771dfedebc6d4a844e55)

@ SDHC\_TIMING\_LEGACY

Legacy 3.3V Mode.

**Definition** sdhc.h:115

[SDHC\_TIMING\_SDR25](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a8c77db56b6a006c1cff9f70e20f6d016)

@ SDHC\_TIMING\_SDR25

High speed mode & SDR25.

**Definition** sdhc.h:121

[SDHC\_TIMING\_SDR12](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90aa48069d7a8a43308d308c9fe67543d86)

@ SDHC\_TIMING\_SDR12

Identification mode & SDR12.

**Definition** sdhc.h:119

[SDHC\_TIMING\_SDR104](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90ae2b69f73212e34bbbfb1c02c27740bd1)

@ SDHC\_TIMING\_SDR104

SDR104 mode.

**Definition** sdhc.h:125

[SDHC\_TIMING\_HS200](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90ae892594e6a91a70ade2dc983bda2d145)

@ SDHC\_TIMING\_HS200

HS200 mode.

**Definition** sdhc.h:131

[SDHC\_TIMING\_HS](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90af5f82fc8f4b281e44b5e78f229d9564b)

@ SDHC\_TIMING\_HS

Legacy High speed mode (3.3V).

**Definition** sdhc.h:117

[SDHC\_TIMING\_DDR50](group__sdhc__interface.md#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90afc9b5aa9339c4ffdea8d6452c10ba5fa)

@ SDHC\_TIMING\_DDR50

DDR50 mode.

**Definition** sdhc.h:127

[SDHC\_INT\_REMOVED](group__sdhc__interface.md#ggab449b2f6b41e791d327f7d92b2b58c2da6e0a03105c6aba203daa53acb6b7c15c)

@ SDHC\_INT\_REMOVED

Card was removed from slot.

**Definition** sdhc.h:242

[SDHC\_INT\_INSERTED](group__sdhc__interface.md#ggab449b2f6b41e791d327f7d92b2b58c2dab9df16a6ed1c7961bb9cab34ebe99f87)

@ SDHC\_INT\_INSERTED

Card was inserted into slot.

**Definition** sdhc.h:241

[SDHC\_INT\_SDIO](group__sdhc__interface.md#ggab449b2f6b41e791d327f7d92b2b58c2dae3a741e98cdb1e8c0ddc8c3baaf64b59)

@ SDHC\_INT\_SDIO

Card interrupt, used by SDIO cards.

**Definition** sdhc.h:240

[SDHC\_POWER\_OFF](group__sdhc__interface.md#ggad63742820bb18ca18cd2f96547e12eb9a621f9456dbce2647567e2e2d049a4c07)

@ SDHC\_POWER\_OFF

**Definition** sdhc.h:91

[SDHC\_POWER\_ON](group__sdhc__interface.md#ggad63742820bb18ca18cd2f96547e12eb9a9442e1400bdfa373a6874cd1434ab604)

@ SDHC\_POWER\_ON

**Definition** sdhc.h:92

[SDHC\_BUS\_WIDTH8BIT](group__sdhc__interface.md#ggad8bab66ec505c8356fac7785a8955448a2b28e7702abe63e03d2b77994d30e156)

@ SDHC\_BUS\_WIDTH8BIT

**Definition** sdhc.h:104

[SDHC\_BUS\_WIDTH4BIT](group__sdhc__interface.md#ggad8bab66ec505c8356fac7785a8955448a4e679800f8863d5650827a0330ef22b6)

@ SDHC\_BUS\_WIDTH4BIT

**Definition** sdhc.h:103

[SDHC\_BUS\_WIDTH1BIT](group__sdhc__interface.md#ggad8bab66ec505c8356fac7785a8955448a875995b349ed5c81e6f34569c35079a0)

@ SDHC\_BUS\_WIDTH1BIT

**Definition** sdhc.h:102

[SDHC\_BUSMODE\_OPENDRAIN](group__sdhc__interface.md#ggaf26909ae9fffdc6ac02abd8094d16dc8a5408bfd39f7ab8c79735d8a956dc9b1a)

@ SDHC\_BUSMODE\_OPENDRAIN

**Definition** sdhc.h:79

[SDHC\_BUSMODE\_PUSHPULL](group__sdhc__interface.md#ggaf26909ae9fffdc6ac02abd8094d16dc8ae47425099c55e2191de84a8cbfa17959)

@ SDHC\_BUSMODE\_PUSHPULL

**Definition** sdhc.h:80

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:83

[sd\_spec.h](sd__spec_8h.md)

[sd\_driver\_type](sd__spec_8h.md#a314c38b1b0603c003e67b5dec2228d4b)

sd\_driver\_type

SD driver types.

**Definition** sd\_spec.h:459

[sdhc\_clock\_speed](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539)

sdhc\_clock\_speed

SD host controller clock speed.

**Definition** sd\_spec.h:413

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[sdhc\_command](structsdhc__command.md)

SD host controller command structure.

**Definition** sdhc.h:44

[sdhc\_command::opcode](structsdhc__command.md#a320ad415df67e1d9b4c09f95993dd17f)

uint32\_t opcode

SD Host specification CMD index.

**Definition** sdhc.h:45

[sdhc\_command::response](structsdhc__command.md#a37a3c1608b5c13311c833c4ad24ff1f9)

uint32\_t response[4]

SD card response field.

**Definition** sdhc.h:47

[sdhc\_command::retries](structsdhc__command.md#a39ba0b1e99814471939dc7bbb7d098eb)

unsigned int retries

Max number of retries.

**Definition** sdhc.h:49

[sdhc\_command::timeout\_ms](structsdhc__command.md#a92cf023d28aa6106d603ff7f67a7e04b)

int timeout\_ms

Command timeout in milliseconds.

**Definition** sdhc.h:50

[sdhc\_command::arg](structsdhc__command.md#af6b98d5f1cecf25af2480b1d359f200e)

uint32\_t arg

SD host specification argument.

**Definition** sdhc.h:46

[sdhc\_command::response\_type](structsdhc__command.md#af758a4e0e3b090912f6e9abd7c4be8f3)

uint32\_t response\_type

Expected SD response type.

**Definition** sdhc.h:48

[sdhc\_data](structsdhc__data.md)

SD host controller data structure.

**Definition** sdhc.h:62

[sdhc\_data::data](structsdhc__data.md#a0f656d093a5cdf3bd09ffee279ad452d)

void \* data

Data to transfer or receive.

**Definition** sdhc.h:67

[sdhc\_data::block\_size](structsdhc__data.md#a20b0ca14adadcdb8d3681240faf5e7b6)

unsigned int block\_size

Block size.

**Definition** sdhc.h:64

[sdhc\_data::blocks](structsdhc__data.md#a47b378d455167bb8d7d05d2f058977fa)

unsigned int blocks

Number of blocks.

**Definition** sdhc.h:65

[sdhc\_data::block\_addr](structsdhc__data.md#aad1e8462d94b4243c981147eab6c962d)

unsigned int block\_addr

Block to start read from.

**Definition** sdhc.h:63

[sdhc\_data::bytes\_xfered](structsdhc__data.md#ae68f1e7f1fbff14c24bd42fa300f9e15)

unsigned int bytes\_xfered

populated with number of bytes sent by SDHC

**Definition** sdhc.h:66

[sdhc\_data::timeout\_ms](structsdhc__data.md#afcf3942de27cd164b6da8dfefa864a8a)

int timeout\_ms

data timeout in milliseconds

**Definition** sdhc.h:68

[sdhc\_driver\_api](structsdhc__driver__api.md)

**Definition** sdhc.h:257

[sdhc\_driver\_api::get\_card\_present](structsdhc__driver__api.md#a06fb6fdfd0c528056c36476f914f94c9)

int(\* get\_card\_present)(const struct device \*dev)

**Definition** sdhc.h:263

[sdhc\_driver\_api::enable\_interrupt](structsdhc__driver__api.md#a42941f226f2adfe5b8275923bff434ff)

int(\* enable\_interrupt)(const struct device \*dev, sdhc\_interrupt\_cb\_t callback, int sources, void \*user\_data)

**Definition** sdhc.h:268

[sdhc\_driver\_api::request](structsdhc__driver__api.md#a577d162b282b2f9eeb91cf07e7578905)

int(\* request)(const struct device \*dev, struct sdhc\_command \*cmd, struct sdhc\_data \*data)

**Definition** sdhc.h:259

[sdhc\_driver\_api::execute\_tuning](structsdhc__driver__api.md#a6075f8ef38200e700ec133fbeb8c8121)

int(\* execute\_tuning)(const struct device \*dev)

**Definition** sdhc.h:264

[sdhc\_driver\_api::disable\_interrupt](structsdhc__driver__api.md#aa50466e31e01d639e459bab204cf1ee5)

int(\* disable\_interrupt)(const struct device \*dev, int sources)

**Definition** sdhc.h:271

[sdhc\_driver\_api::reset](structsdhc__driver__api.md#ac034dfc17e064170e76280394005c76c)

int(\* reset)(const struct device \*dev)

**Definition** sdhc.h:258

[sdhc\_driver\_api::card\_busy](structsdhc__driver__api.md#ac642c06d5ec9f697be8fa46cede3bc64)

int(\* card\_busy)(const struct device \*dev)

**Definition** sdhc.h:265

[sdhc\_driver\_api::set\_io](structsdhc__driver__api.md#adb40a93f64a1a8dc1548a4651091ecf9)

int(\* set\_io)(const struct device \*dev, struct sdhc\_io \*ios)

**Definition** sdhc.h:262

[sdhc\_driver\_api::get\_host\_props](structsdhc__driver__api.md#af2b83b0ea2afbbdf065b5919c6b822c2)

int(\* get\_host\_props)(const struct device \*dev, struct sdhc\_host\_props \*props)

**Definition** sdhc.h:266

[sdhc\_host\_caps](structsdhc__host__caps.md)

SD host controller capabilities.

**Definition** sdhc.h:161

[sdhc\_host\_caps::address\_64\_bit\_support\_v3](structsdhc__host__caps.md#a0f33c7e168ade12675795d2c0d5b5ea2)

unsigned int address\_64\_bit\_support\_v3

64-bit system address support for V3

**Definition** sdhc.h:178

[sdhc\_host\_caps::uhs\_2\_support](structsdhc__host__caps.md#a146c7403d7ecbbffbd6aa0c1c4fad1b5)

unsigned int uhs\_2\_support

UHS-II support.

**Definition** sdhc.h:184

[sdhc\_host\_caps::sd\_base\_clk](structsdhc__host__caps.md#a20ada015fecce002d233fefac5c4ead4)

unsigned int sd\_base\_clk

SD base clock frequency.

**Definition** sdhc.h:165

[sdhc\_host\_caps::sdma\_support](structsdhc__host__caps.md#a22f2877854669589f0483cf91e504df6)

unsigned int sdma\_support

SDMA support.

**Definition** sdhc.h:172

[sdhc\_host\_caps::vdd2\_180\_support](structsdhc__host__caps.md#a2f5d5859cbe06ab449f95c0a108c2250)

unsigned int vdd2\_180\_support

1.8V VDD2 support

**Definition** sdhc.h:195

[sdhc\_host\_caps::slot\_type](structsdhc__host__caps.md#a3231007bc5fcc731e97236b29333f7ee)

unsigned int slot\_type

Slot type.

**Definition** sdhc.h:180

[sdhc\_host\_caps::timeout\_clk\_freq](structsdhc__host__caps.md#a3a57e12aa8f53ad1c1fb44696622f587)

unsigned int timeout\_clk\_freq

Timeout clock frequency.

**Definition** sdhc.h:162

[sdhc\_host\_caps::sdr104\_support](structsdhc__host__caps.md#a3e6f73ea9df9c207cddda31de45621be)

unsigned int sdr104\_support

SDR104 support.

**Definition** sdhc.h:182

[sdhc\_host\_caps::drv\_type\_a\_support](structsdhc__host__caps.md#a43086e5bc5d6384b8eb0709c1cf1756e)

unsigned int drv\_type\_a\_support

Driver type A support.

**Definition** sdhc.h:185

[sdhc\_host\_caps::retuning\_mode](structsdhc__host__caps.md#a48680d522d417e68ec3371b3831faa01)

unsigned int retuning\_mode

Re-tuning mode.

**Definition** sdhc.h:191

[sdhc\_host\_caps::sdr50\_support](structsdhc__host__caps.md#a63dabbc7c24dc41c8103be81ee6e673f)

unsigned int sdr50\_support

SDR50 support.

**Definition** sdhc.h:181

[sdhc\_host\_caps::sdio\_async\_interrupt\_support](structsdhc__host__caps.md#a6fa0525ee3b2a0313cc9b83dc820b831)

unsigned int sdio\_async\_interrupt\_support

Asynchronous interrupt support.

**Definition** sdhc.h:179

[sdhc\_host\_caps::bus\_4\_bit\_support](structsdhc__host__caps.md#a70b8180301c72db291b9d53bf5379655)

unsigned int bus\_4\_bit\_support

4 bit bus support

**Definition** sdhc.h:168

[sdhc\_host\_caps::vol\_300\_support](structsdhc__host__caps.md#a7fdf6832fbcc9dce7e20ee87d9063665)

unsigned int vol\_300\_support

Voltage support 3.0V.

**Definition** sdhc.h:175

[sdhc\_host\_caps::timeout\_clk\_unit](structsdhc__host__caps.md#a8af558ed3b7af437f1782aea9ee6794e)

unsigned int timeout\_clk\_unit

Timeout clock unit.

**Definition** sdhc.h:164

[sdhc\_host\_caps::adma3\_support](structsdhc__host__caps.md#a90a90218bcd866cbfae2354c5b0af3de)

unsigned int adma3\_support

ADMA3 support.

**Definition** sdhc.h:194

[sdhc\_host\_caps::hs200\_support](structsdhc__host__caps.md#a956a426ca18a02aa4c81e7b2c576531c)

unsigned int hs200\_support

HS200 support.

**Definition** sdhc.h:197

[sdhc\_host\_caps::max\_blk\_len](structsdhc__host__caps.md#a97dbad3360b56a44fb1ab0d77aa90bc4)

unsigned int max\_blk\_len

Max block length.

**Definition** sdhc.h:166

[sdhc\_host\_caps::ddr50\_support](structsdhc__host__caps.md#aa22adb0079aa3864df4461d841852684)

unsigned int ddr50\_support

DDR50 support.

**Definition** sdhc.h:183

[sdhc\_host\_caps::vol\_180\_support](structsdhc__host__caps.md#aa39ef2d70314dbf2517bd3df6fbd4694)

unsigned int vol\_180\_support

Voltage support 1.8V.

**Definition** sdhc.h:176

[sdhc\_host\_caps::high\_spd\_support](structsdhc__host__caps.md#aaec0cd01cc4e8bf334e5c3ee151d5d98)

unsigned int high\_spd\_support

High speed support.

**Definition** sdhc.h:171

[sdhc\_host\_caps::drv\_type\_c\_support](structsdhc__host__caps.md#aafcfb75fd131430df0a372e6ac2c8b34)

unsigned int drv\_type\_c\_support

Driver type C support.

**Definition** sdhc.h:186

[sdhc\_host\_caps::retune\_timer\_count](structsdhc__host__caps.md#ab7a145bf44747d7d9e68ff743520cc2c)

unsigned int retune\_timer\_count

Timer count for re-tuning.

**Definition** sdhc.h:189

[sdhc\_host\_caps::sdr50\_needs\_tuning](structsdhc__host__caps.md#ac54a191e04ff6c266390d1fb8d4f84d3)

unsigned int sdr50\_needs\_tuning

Use tuning for SDR50.

**Definition** sdhc.h:190

[sdhc\_host\_caps::vol\_330\_support](structsdhc__host__caps.md#ac6e2eb088ed7d7c3f3f5011ad55ba543)

unsigned int vol\_330\_support

Voltage support 3.3V.

**Definition** sdhc.h:174

[sdhc\_host\_caps::adma\_2\_support](structsdhc__host__caps.md#acfa1c5e96f2afeab40185a1ef37d7efb)

unsigned int adma\_2\_support

ADMA2 support.

**Definition** sdhc.h:169

[sdhc\_host\_caps::bus\_8\_bit\_support](structsdhc__host__caps.md#ad09f103fc8ce341d25e1f824e97bd665)

unsigned int bus\_8\_bit\_support

8-bit Support for embedded device

**Definition** sdhc.h:167

[sdhc\_host\_caps::hs400\_support](structsdhc__host__caps.md#ad23716b3541a99dfe935e06aa9c8f256)

unsigned int hs400\_support

HS400 support.

**Definition** sdhc.h:198

[sdhc\_host\_caps::drv\_type\_d\_support](structsdhc__host__caps.md#ad2c9e66bbd9a442d872fd559fd7a833c)

unsigned int drv\_type\_d\_support

Driver type D support.

**Definition** sdhc.h:187

[sdhc\_host\_caps::address\_64\_bit\_support\_v4](structsdhc__host__caps.md#ad8e4ca0d2fb39486b469224218d2eb7b)

unsigned int address\_64\_bit\_support\_v4

64-bit system address support for V4

**Definition** sdhc.h:177

[sdhc\_host\_caps::suspend\_res\_support](structsdhc__host__caps.md#af343879ebc21f5c2d57ffa962dacb796)

unsigned int suspend\_res\_support

Suspend/Resume support.

**Definition** sdhc.h:173

[sdhc\_host\_caps::clk\_multiplier](structsdhc__host__caps.md#afffade3ad661ead23ed0f74b770172ff)

unsigned int clk\_multiplier

Clock multiplier.

**Definition** sdhc.h:192

[sdhc\_host\_props](structsdhc__host__props.md)

SD host controller properties.

**Definition** sdhc.h:223

[sdhc\_host\_props::f\_min](structsdhc__host__props.md#a28c69ba3fdae1393daa551f3f9b91057)

unsigned int f\_min

Min bus frequency.

**Definition** sdhc.h:225

[sdhc\_host\_props::max\_current\_180](structsdhc__host__props.md#a43d2b80ec0a5682783e4297c734a3c88)

uint32\_t max\_current\_180

Max current (in mA) at 1.8V.

**Definition** sdhc.h:230

[sdhc\_host\_props::power\_delay](structsdhc__host__props.md#a7f7b22b7b8fb46df0ec19e2bef2a4702)

unsigned int power\_delay

Delay to allow SD to power up or down (in ms).

**Definition** sdhc.h:226

[sdhc\_host\_props::is\_spi](structsdhc__host__props.md#abb18e33d99ed1e4a4400dccd2149816f)

bool is\_spi

Is the host using SPI mode.

**Definition** sdhc.h:231

[sdhc\_host\_props::max\_current\_300](structsdhc__host__props.md#ac247312c9b10768fe878afc5c85d9eba)

uint32\_t max\_current\_300

Max current (in mA) at 3.0V.

**Definition** sdhc.h:229

[sdhc\_host\_props::host\_caps](structsdhc__host__props.md#ad60bf89e594a031f6be015888466a113)

struct sdhc\_host\_caps host\_caps

Host capability bitfield.

**Definition** sdhc.h:227

[sdhc\_host\_props::f\_max](structsdhc__host__props.md#aef7123dfa5690bc0525aa40dc623307c)

unsigned int f\_max

Max bus frequency.

**Definition** sdhc.h:224

[sdhc\_host\_props::max\_current\_330](structsdhc__host__props.md#afebe4aad820c1672635fd30aacec20e4)

uint32\_t max\_current\_330

Max current (in mA) at 3.3V.

**Definition** sdhc.h:228

[sdhc\_io](structsdhc__io.md)

SD host controller I/O control structure.

**Definition** sdhc.h:208

[sdhc\_io::driver\_type](structsdhc__io.md#a0c62aaa1a8a7700ebb00a38ce2e57d11)

enum sd\_driver\_type driver\_type

SD driver type.

**Definition** sdhc.h:214

[sdhc\_io::bus\_mode](structsdhc__io.md#a2b4456b108778aada0d42b8c8107b3e9)

enum sdhc\_bus\_mode bus\_mode

command output mode

**Definition** sdhc.h:210

[sdhc\_io::timing](structsdhc__io.md#a85c50f625d8606bb4c07a228c0de24e4)

enum sdhc\_timing\_mode timing

SD bus timing.

**Definition** sdhc.h:213

[sdhc\_io::bus\_width](structsdhc__io.md#a904b05c7e73e80bb7326b0bfcb6b7103)

enum sdhc\_bus\_width bus\_width

SD bus width.

**Definition** sdhc.h:212

[sdhc\_io::clock](structsdhc__io.md#aaa15197b8f1947a67dcd8522aa62afc5)

enum sdhc\_clock\_speed clock

Clock rate.

**Definition** sdhc.h:209

[sdhc\_io::power\_mode](structsdhc__io.md#ac503fb9fba7ffdb01695a77780972930)

enum sdhc\_power power\_mode

SD power supply mode.

**Definition** sdhc.h:211

[sdhc\_io::signal\_voltage](structsdhc__io.md#ade8b8cd4e4f4b21f5fa8e3fb2661917e)

enum sd\_voltage signal\_voltage

IO signalling voltage (usually 1.8 or 3.3V).

**Definition** sdhc.h:215

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sdhc.h](sdhc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

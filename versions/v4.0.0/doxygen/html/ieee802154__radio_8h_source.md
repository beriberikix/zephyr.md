---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ieee802154__radio_8h_source.html
original_path: doxygen/html/ieee802154__radio_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ieee802154\_radio.h

[Go to the documentation of this file.](ieee802154__radio_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation.

3 \* Copyright (c) 2023 F. Grandel, Zephyr Project

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

14

15#ifndef ZEPHYR\_INCLUDE\_NET\_IEEE802154\_RADIO\_H\_

16#define ZEPHYR\_INCLUDE\_NET\_IEEE802154\_RADIO\_H\_

17

18#include <[zephyr/device.h](device_8h.md)>

19#include <[zephyr/net/net\_if.h](net__if_8h.md)>

20#include <[zephyr/net/net\_pkt.h](net__pkt_8h.md)>

21#include <[zephyr/net/net\_time.h](net__time_8h.md)>

22#include <[zephyr/net/ieee802154.h](ieee802154_8h.md)>

23#include <[zephyr/net/ieee802154\_ie.h](ieee802154__ie_8h.md)>

24#include <[zephyr/sys/util.h](sys_2util_8h.md)>

25

26#ifdef \_\_cplusplus

27extern "C" {

28#endif

29

65

70

[ 84](group__ieee802154__driver.md#gaf228d9c26cedd5c790b7ebae41b5f937)#define IEEE802154\_PHY\_SYMBOLS\_PER\_SECOND(symbol\_period\_ns) (NSEC\_PER\_SEC / symbol\_period\_ns)

85

87

88

93

[ 99](group__ieee802154__driver.md#gadb590005c9120e6b04aa430ebb306b8f)#define IEEE802154\_MAC\_A\_BASE\_SLOT\_DURATION 60U

100

[ 105](group__ieee802154__driver.md#ga662c1add47deb9807e848aeeee5e6842)#define IEEE802154\_MAC\_A\_NUM\_SUPERFRAME\_SLOTS 16U

106

[ 111](group__ieee802154__driver.md#ga52358c63c386b72f190d3b487c9ba286)#define IEEE802154\_MAC\_A\_BASE\_SUPERFRAME\_DURATION \

112 (IEEE802154\_MAC\_A\_BASE\_SLOT\_DURATION \* IEEE802154\_MAC\_A\_NUM\_SUPERFRAME\_SLOTS)

113

[ 118](group__ieee802154__driver.md#ga86f3186304b02de3096d521238d407db)#define IEEE802154\_MAC\_A\_UNIT\_BACKOFF\_PERIOD(turnaround\_time) \

119 (turnaround\_time + IEEE802154\_PHY\_A\_CCA\_TIME)

120

[ 125](group__ieee802154__driver.md#ga132be1037c5db1311c6d0c7d74e1fe40)#define IEEE802154\_MAC\_RESPONSE\_WAIT\_TIME\_DEFAULT 32U

126

128

129

134

[ 169](group__ieee802154__driver.md#gacabc7386bea701373dfb36ab65bd36a9)enum [ieee802154\_phy\_channel\_page](group__ieee802154__driver.md#gacabc7386bea701373dfb36ab65bd36a9) {

[ 183](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a72b17a977aeb6792f7d2016117f4b2f9) [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_ZERO\_OQPSK\_2450\_BPSK\_868\_915](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a72b17a977aeb6792f7d2016117f4b2f9) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

184

[ 186](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a371a12ec5d762b03058fb2532fa04e45) [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_ONE\_DEPRECATED](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a371a12ec5d762b03058fb2532fa04e45) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

187

[ 189](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a5776e0160927b83f4e4e8d6479aaf804) [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_TWO\_OQPSK\_868\_915](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a5776e0160927b83f4e4e8d6479aaf804) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

190

[ 192](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a6f71c162be118b0c2edce139753c867e) [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_THREE\_CSS](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a6f71c162be118b0c2edce139753c867e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

193

[ 195](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a68b93381ddc1184ff0ed13456cf4b6a8) [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_FOUR\_HRP\_UWB](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a68b93381ddc1184ff0ed13456cf4b6a8) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

196

[ 198](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a6ea456573a6ff8aed348a9dc547b2db7) [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_FIVE\_OQPSK\_780](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a6ea456573a6ff8aed348a9dc547b2db7) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

199

[ 201](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9ac13dda08becd3d4799d45ef02f774cc1) [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_SIX\_RESERVED](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9ac13dda08becd3d4799d45ef02f774cc1) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

202

[ 204](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a1f33467ec7659ef411b08f7a23663311) [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_SEVEN\_MSK](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a1f33467ec7659ef411b08f7a23663311) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

205

[ 207](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9aa0ab080c8cdac42dbf80622d075854dc) [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_EIGHT\_LRP\_UWB](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9aa0ab080c8cdac42dbf80622d075854dc) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8),

208

[ 213](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a996b529c9c277d6d653d0e0ffb8b2902) [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_NINE\_SUN\_PREDEFINED](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a996b529c9c277d6d653d0e0ffb8b2902) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9),

214

[ 219](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a02a17ea787e99528b2a6a8f5107f2544) [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_TEN\_SUN\_FSK\_GENERIC](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a02a17ea787e99528b2a6a8f5107f2544) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10),

220

[ 222](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9aad0644244fb5b6cba5a295e246722e94) [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_ELEVEN\_OQPSK\_2380](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9aad0644244fb5b6cba5a295e246722e94) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11),

223

[ 225](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a6d4023088a3607c072acebd3940340c7) [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_TWELVE\_LECIM](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a6d4023088a3607c072acebd3940340c7) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12),

226

[ 228](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a56dd4ae42595ef0edb109c729e333b08) [IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_THIRTEEN\_RCC](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a56dd4ae42595ef0edb109c729e333b08) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13),

229};

230

[ 235](structieee802154__phy__channel__range.md)struct [ieee802154\_phy\_channel\_range](structieee802154__phy__channel__range.md) {

[ 236](structieee802154__phy__channel__range.md#aec90e36227a7d9cc1dfc18231341dd03) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [from\_channel](structieee802154__phy__channel__range.md#aec90e36227a7d9cc1dfc18231341dd03);

[ 237](structieee802154__phy__channel__range.md#a78af593807753dbfcfce88166f4c1f58) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [to\_channel](structieee802154__phy__channel__range.md#a78af593807753dbfcfce88166f4c1f58);

238};

239

[ 244](structieee802154__phy__supported__channels.md)struct [ieee802154\_phy\_supported\_channels](structieee802154__phy__supported__channels.md) {

[ 251](structieee802154__phy__supported__channels.md#a73ccabf887b567a0ce3ddc5f8a3eeed1) const struct [ieee802154\_phy\_channel\_range](structieee802154__phy__channel__range.md) \*const [ranges](structieee802154__phy__supported__channels.md#a73ccabf887b567a0ce3ddc5f8a3eeed1);

252

[ 254](structieee802154__phy__supported__channels.md#a8fb56a7fc6be96035cf4b51891582da9) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_ranges](structieee802154__phy__supported__channels.md#a8fb56a7fc6be96035cf4b51891582da9);

255};

256

[ 282](group__ieee802154__driver.md#ga78d4df389a7bd11c55e5c7b683897a9b)#define IEEE802154\_DEFINE\_PHY\_SUPPORTED\_CHANNELS(drv\_attr, from, to) \

283 static const struct { \

284 const struct ieee802154\_phy\_channel\_range phy\_channel\_range; \

285 const struct ieee802154\_phy\_supported\_channels phy\_supported\_channels; \

286 } drv\_attr = { \

287 .phy\_channel\_range = {.from\_channel = (from), .to\_channel = (to)}, \

288 .phy\_supported\_channels = \

289 { \

290 .ranges = &drv\_attr.phy\_channel\_range, \

291 .num\_ranges = 1U, \

292 }, \

293 }

294

296

297

302

[ 307](group__ieee802154__driver.md#ga9e95bf5d8ddb1087cdd9eb2aa80d100e)#define IEEE802154\_PHY\_A\_TURNAROUND\_TIME\_DEFAULT 12U

308

[ 313](group__ieee802154__driver.md#ga68115b80097b116b704431808469450b)#define IEEE802154\_PHY\_A\_TURNAROUND\_TIME\_1MS(symbol\_period\_ns) \

314 DIV\_ROUND\_UP(NSEC\_PER\_MSEC, symbol\_period\_ns)

315

[ 320](group__ieee802154__driver.md#gaf58b5d421167c2075dcdfdbaba5956dd)#define IEEE802154\_PHY\_A\_CCA\_TIME 8U

321

323

324

325

330

[ 332](group__ieee802154__driver.md#ga32ce931f3d35d779e4251c37f61583f5)#define IEEE802154\_PHY\_OQPSK\_868MHZ\_SYMBOL\_PERIOD\_NS 40000LL

333

[ 338](group__ieee802154__driver.md#gaff3d58945d53e824f1fb1ca11dd9997b)#define IEEE802154\_PHY\_OQPSK\_780\_TO\_2450MHZ\_SYMBOL\_PERIOD\_NS 16000LL

339

341

342

347

[ 349](group__ieee802154__driver.md#ga1dc4319d0a8d979c7455e1f71f45d885)#define IEEE802154\_PHY\_BPSK\_868MHZ\_SYMBOL\_PERIOD\_NS 50000LL

350

[ 352](group__ieee802154__driver.md#gaa12344b6a118995b63c5bd4bc3180efd)#define IEEE802154\_PHY\_BPSK\_915MHZ\_SYMBOL\_PERIOD\_NS 25000LL

353

355

356

370

[ 372](group__ieee802154__driver.md#gabeb8a359ce54618aa7df3ee8f6a434bb)#define IEEE802154\_PHY\_HRP\_UWB\_PRF4\_TPSYM\_SYMBOL\_PERIOD\_NS 3974.36F

[ 374](group__ieee802154__driver.md#ga0123679fba7ca668aa158813f1bf2302)#define IEEE802154\_PHY\_HRP\_UWB\_PRF16\_TPSYM\_SYMBOL\_PERIOD\_NS 993.59F

[ 376](group__ieee802154__driver.md#ga59f8ba8a01171c56da6f7ae7f8983bf7)#define IEEE802154\_PHY\_HRP\_UWB\_PRF64\_TPSYM\_SYMBOL\_PERIOD\_NS 1017.63F

[ 378](group__ieee802154__driver.md#gaa25ba5b644e58cfc7de5ba5aa526ea71)#define IEEE802154\_PHY\_HRP\_UWB\_ERDEV\_TPSYM\_SYMBOL\_PERIOD\_NS 729.17F

379

[ 381](group__ieee802154__driver.md#ga13610aeef06372bc47d84464537fdded)enum [ieee802154\_phy\_hrp\_uwb\_nominal\_prf](group__ieee802154__driver.md#ga13610aeef06372bc47d84464537fdded) {

[ 383](group__ieee802154__driver.md#gga13610aeef06372bc47d84464537fddeda4369c745ed378d8273a1014322f3029a) [IEEE802154\_PHY\_HRP\_UWB\_PRF\_OFF](group__ieee802154__driver.md#gga13610aeef06372bc47d84464537fddeda4369c745ed378d8273a1014322f3029a) = 0,

[ 384](group__ieee802154__driver.md#gga13610aeef06372bc47d84464537fddeda9dc3c58366502aeab04a208937536369) [IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_4\_M](group__ieee802154__driver.md#gga13610aeef06372bc47d84464537fddeda9dc3c58366502aeab04a208937536369) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 385](group__ieee802154__driver.md#gga13610aeef06372bc47d84464537fddedadf9230e6ef62ce66129bfe24f537c88a) [IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_16\_M](group__ieee802154__driver.md#gga13610aeef06372bc47d84464537fddedadf9230e6ef62ce66129bfe24f537c88a) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 386](group__ieee802154__driver.md#gga13610aeef06372bc47d84464537fddeda2b24236d3531cab7d21673d065b7c29e) [IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_64\_M](group__ieee802154__driver.md#gga13610aeef06372bc47d84464537fddeda2b24236d3531cab7d21673d065b7c29e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

387

[ 393](group__ieee802154__driver.md#gga13610aeef06372bc47d84464537fddedad920ae285cdcc2a4d59f7c23e29dce27) [IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_64\_M\_BPRF](group__ieee802154__driver.md#gga13610aeef06372bc47d84464537fddedad920ae285cdcc2a4d59f7c23e29dce27) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 394](group__ieee802154__driver.md#gga13610aeef06372bc47d84464537fddedae6c88efd301a449b1a31e8aedf4e30ca) [IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_128\_M\_HPRF](group__ieee802154__driver.md#gga13610aeef06372bc47d84464537fddedae6c88efd301a449b1a31e8aedf4e30ca) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 395](group__ieee802154__driver.md#gga13610aeef06372bc47d84464537fddedacb66442cf2a5e4c539b6b7edf8419be1) [IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_256\_M\_HPRF](group__ieee802154__driver.md#gga13610aeef06372bc47d84464537fddedacb66442cf2a5e4c539b6b7edf8419be1) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

396};

397

[ 399](group__ieee802154__driver.md#gacfd2faf2c3072f8851abd74fe5148ec5)#define IEEE802154\_PHY\_HRP\_UWB\_RDEV \

400 (IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_4\_M | IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_16\_M | \

401 IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_64\_M)

402

[ 404](group__ieee802154__driver.md#gae02b981a3908b05b4bc0b7a2844c27c7)#define IEEE802154\_PHY\_HRP\_UWB\_ERDEV \

405 (IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_64\_M\_BPRF | IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_128\_M\_HPRF | \

406 IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_256\_M\_HPRF)

407

409

410

415

[ 417](group__ieee802154__driver.md#ga155b5b5a06311c1bde3f36e06d02ed7d)#define IEEE802154\_PHY\_SUN\_FSK\_863MHZ\_915MHZ\_SYMBOL\_PERIOD\_NS 20000LL

418

[ 420](group__ieee802154__driver.md#gac088ee6d01014a12169e74111ea61993)#define IEEE802154\_PHY\_SUN\_FSK\_PHR\_LEN 2

421

423

428

[ 437](group__ieee802154__driver.md#gaf99cda89c29df3c0088fc57ec09cbcd4)enum [ieee802154\_hw\_caps](group__ieee802154__driver.md#gaf99cda89c29df3c0088fc57ec09cbcd4) {

438

439 /\*

440 \* PHY capabilities

441 \*

442 \* The following capabilities describe features of the underlying radio

443 \* hardware (PHY/L1).

444 \*/

445

[ 447](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a179ad073a5bd34e4e4af587d07ca3f73) [IEEE802154\_HW\_ENERGY\_SCAN](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a179ad073a5bd34e4e4af587d07ca3f73) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

448

449 /\*

450 \* MAC offloading capabilities (optional)

451 \*

452 \* The following MAC/L2 features may optionally be offloaded to

453 \* specialized hardware or proprietary driver firmware ("hard MAC").

454 \*

455 \* L2 implementations will have to provide a "soft MAC" fallback for

456 \* these features in case the driver does not support them natively.

457 \*

458 \* Note: Some of these offloading capabilities may be mandatory in

459 \* practice to stay within timing requirements of certain IEEE 802.15.4

460 \* protocols, e.g. CPUs may not be fast enough to send ACKs within the

461 \* required delays in the 2.4 GHz band without hard MAC support.

462 \*/

463

[ 465](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a0ea21cab335dd9082feb2d08be0eb5fa) [IEEE802154\_HW\_FCS](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a0ea21cab335dd9082feb2d08be0eb5fa) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

466

[ 468](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4afd09f329a708d00f1384a50c59ddde27) [IEEE802154\_HW\_FILTER](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4afd09f329a708d00f1384a50c59ddde27) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

469

[ 471](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a4adb33f2ca81a24244dead6b379cd916) [IEEE802154\_HW\_PROMISC](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a4adb33f2ca81a24244dead6b379cd916) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

472

[ 474](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a2ee53f11e1ed6853e1f5d9dfe7d7bdf7) [IEEE802154\_HW\_CSMA](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a2ee53f11e1ed6853e1f5d9dfe7d7bdf7) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

475

[ 477](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4ab383a932c0ac9deece68f02210089119) [IEEE802154\_HW\_TX\_RX\_ACK](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4ab383a932c0ac9deece68f02210089119) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

478

[ 480](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a752472a994bdcbdf9cdf86deb0231849) [IEEE802154\_HW\_RETRANSMISSION](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a752472a994bdcbdf9cdf86deb0231849) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

481

[ 483](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4aec16c4d418117de2d106e84297568b03) [IEEE802154\_HW\_RX\_TX\_ACK](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4aec16c4d418117de2d106e84297568b03) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

484

[ 486](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a435d032f42d509bd78a992de6e4d7b1d) [IEEE802154\_HW\_TXTIME](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a435d032f42d509bd78a992de6e4d7b1d) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8),

487

[ 512](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a36f46639c08e70bc30fc98ca1043b071) [IEEE802154\_HW\_SLEEP\_TO\_TX](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a36f46639c08e70bc30fc98ca1043b071) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9),

513

[ 515](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a68ae68c83a87f0efc25f74edd80c4600) [IEEE802154\_HW\_RXTIME](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a68ae68c83a87f0efc25f74edd80c4600) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10),

516

[ 518](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a7924c3d5bfe6dceeb2e8caa6df7edecb) [IEEE802154\_HW\_TX\_SEC](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a7924c3d5bfe6dceeb2e8caa6df7edecb) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11),

519

[ 521](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4ac1e00966043e5884c4cbd65fb26f0c0b) [IEEE802154\_RX\_ON\_WHEN\_IDLE](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4ac1e00966043e5884c4cbd65fb26f0c0b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12),

522

[ 534](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4ab6cf4f3552d6193027a538a13b95952e) [IEEE802154\_HW\_SELECTIVE\_TXCHANNEL](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4ab6cf4f3552d6193027a538a13b95952e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13),

535

536 /\* Note: Update also IEEE802154\_HW\_CAPS\_BITS\_COMMON\_COUNT when changing

537 \* the ieee802154\_hw\_caps type.

538 \*/

539};

540

[ 542](group__ieee802154__driver.md#gaf143a9f110a2eb6b21104af6927159bc)#define IEEE802154\_HW\_CAPS\_BITS\_COMMON\_COUNT (14)

543

[ 545](group__ieee802154__driver.md#ga40912ccb268768b4e96ce9cad35476af)#define IEEE802154\_HW\_CAPS\_BITS\_PRIV\_START IEEE802154\_HW\_CAPS\_BITS\_COMMON\_COUNT

546

[ 548](group__ieee802154__driver.md#gaa1971591e72866d0f3f0d4db2931e25a)enum [ieee802154\_filter\_type](group__ieee802154__driver.md#gaa1971591e72866d0f3f0d4db2931e25a) {

[ 549](group__ieee802154__driver.md#ggaa1971591e72866d0f3f0d4db2931e25aa928a93b536c6408b3d77aa329c274fe8) [IEEE802154\_FILTER\_TYPE\_IEEE\_ADDR](group__ieee802154__driver.md#ggaa1971591e72866d0f3f0d4db2931e25aa928a93b536c6408b3d77aa329c274fe8),

[ 550](group__ieee802154__driver.md#ggaa1971591e72866d0f3f0d4db2931e25aa2fa1ac98a3b870fcf6e85e7ec82cfbe9) [IEEE802154\_FILTER\_TYPE\_SHORT\_ADDR](group__ieee802154__driver.md#ggaa1971591e72866d0f3f0d4db2931e25aa2fa1ac98a3b870fcf6e85e7ec82cfbe9),

[ 551](group__ieee802154__driver.md#ggaa1971591e72866d0f3f0d4db2931e25aab44cc830999926a5d232aedabef52653) [IEEE802154\_FILTER\_TYPE\_PAN\_ID](group__ieee802154__driver.md#ggaa1971591e72866d0f3f0d4db2931e25aab44cc830999926a5d232aedabef52653),

[ 552](group__ieee802154__driver.md#ggaa1971591e72866d0f3f0d4db2931e25aade18e03611339f5f7ec4fdcdee409c21) [IEEE802154\_FILTER\_TYPE\_SRC\_IEEE\_ADDR](group__ieee802154__driver.md#ggaa1971591e72866d0f3f0d4db2931e25aade18e03611339f5f7ec4fdcdee409c21),

[ 553](group__ieee802154__driver.md#ggaa1971591e72866d0f3f0d4db2931e25aac6dbb68674e7594fd4cd69bbe4ea60de) [IEEE802154\_FILTER\_TYPE\_SRC\_SHORT\_ADDR](group__ieee802154__driver.md#ggaa1971591e72866d0f3f0d4db2931e25aac6dbb68674e7594fd4cd69bbe4ea60de),

554};

555

[ 557](group__ieee802154__driver.md#ga3491982b677941442d904ce69fce7c5e)enum [ieee802154\_event](group__ieee802154__driver.md#ga3491982b677941442d904ce69fce7c5e) {

[ 559](group__ieee802154__driver.md#gga3491982b677941442d904ce69fce7c5eaacd61f4466f1ef926adc9e1afe6c1648) [IEEE802154\_EVENT\_TX\_STARTED](group__ieee802154__driver.md#gga3491982b677941442d904ce69fce7c5eaacd61f4466f1ef926adc9e1afe6c1648),

[ 561](group__ieee802154__driver.md#gga3491982b677941442d904ce69fce7c5eaef51197ca09befaee8cdfa2cde107273) [IEEE802154\_EVENT\_RX\_FAILED](group__ieee802154__driver.md#gga3491982b677941442d904ce69fce7c5eaef51197ca09befaee8cdfa2cde107273),

[ 569](group__ieee802154__driver.md#gga3491982b677941442d904ce69fce7c5eaf7ed46b9d13a232a2ea6b650514eea3d) [IEEE802154\_EVENT\_RX\_OFF](group__ieee802154__driver.md#gga3491982b677941442d904ce69fce7c5eaf7ed46b9d13a232a2ea6b650514eea3d),

570};

571

[ 573](group__ieee802154__driver.md#ga04febbd15f9e6f6540d711ada5a4a1c8)enum [ieee802154\_rx\_fail\_reason](group__ieee802154__driver.md#ga04febbd15f9e6f6540d711ada5a4a1c8) {

[ 575](group__ieee802154__driver.md#gga04febbd15f9e6f6540d711ada5a4a1c8ad584824b4813626d04a85499371b9c32) [IEEE802154\_RX\_FAIL\_NOT\_RECEIVED](group__ieee802154__driver.md#gga04febbd15f9e6f6540d711ada5a4a1c8ad584824b4813626d04a85499371b9c32),

[ 577](group__ieee802154__driver.md#gga04febbd15f9e6f6540d711ada5a4a1c8a103f6683ff71f4f7248ee1a0d09d6be4) [IEEE802154\_RX\_FAIL\_INVALID\_FCS](group__ieee802154__driver.md#gga04febbd15f9e6f6540d711ada5a4a1c8a103f6683ff71f4f7248ee1a0d09d6be4),

[ 579](group__ieee802154__driver.md#gga04febbd15f9e6f6540d711ada5a4a1c8a7ff9cfcc5e4dfc2bf7abe1860a39410f) [IEEE802154\_RX\_FAIL\_ADDR\_FILTERED](group__ieee802154__driver.md#gga04febbd15f9e6f6540d711ada5a4a1c8a7ff9cfcc5e4dfc2bf7abe1860a39410f),

[ 581](group__ieee802154__driver.md#gga04febbd15f9e6f6540d711ada5a4a1c8a5baa9dd683a717f7fbdfc5ab85935a3b) [IEEE802154\_RX\_FAIL\_OTHER](group__ieee802154__driver.md#gga04febbd15f9e6f6540d711ada5a4a1c8a5baa9dd683a717f7fbdfc5ab85935a3b)

582};

583

[ 585](group__ieee802154__driver.md#ga8c9ab3cecefe641a25f003eb6d014fc5)typedef void (\*[energy\_scan\_done\_cb\_t](group__ieee802154__driver.md#ga8c9ab3cecefe641a25f003eb6d014fc5))(const struct [device](structdevice.md) \*dev,

586 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) max\_ed);

587

[ 589](group__ieee802154__driver.md#ga8219b80b8b179fc3a2ffac0dfdfb4e4b)typedef void (\*[ieee802154\_event\_cb\_t](group__ieee802154__driver.md#ga8219b80b8b179fc3a2ffac0dfdfb4e4b))(const struct [device](structdevice.md) \*dev,

590 enum [ieee802154\_event](group__ieee802154__driver.md#ga3491982b677941442d904ce69fce7c5e) evt,

591 void \*event\_params);

592

[ 594](structieee802154__filter.md)struct [ieee802154\_filter](structieee802154__filter.md) {

595 union {

[ 597](structieee802154__filter.md#a636ec85ca79b2880de51ed93f6788909) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[ieee\_addr](structieee802154__filter.md#a636ec85ca79b2880de51ed93f6788909);

[ 599](structieee802154__filter.md#a16a1779ff43accda31bba35b9bdd61c3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [short\_addr](structieee802154__filter.md#a16a1779ff43accda31bba35b9bdd61c3);

[ 601](structieee802154__filter.md#a40f77239924af29d40f7595e23475e9b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pan\_id](structieee802154__filter.md#a40f77239924af29d40f7595e23475e9b);

602 };

603};

604

[ 609](structieee802154__key.md)struct [ieee802154\_key](structieee802154__key.md) {

[ 611](structieee802154__key.md#a01b760f3e622ad0a60888170e5688b9d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[key\_value](structieee802154__key.md#a01b760f3e622ad0a60888170e5688b9d);

[ 613](structieee802154__key.md#a357419c2d16a527a2417f4eded566aac) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [key\_frame\_counter](structieee802154__key.md#a357419c2d16a527a2417f4eded566aac);

[ 615](structieee802154__key.md#a5ca5258422db14b99fd37e7126cfc85d) bool [frame\_counter\_per\_key](structieee802154__key.md#a5ca5258422db14b99fd37e7126cfc85d);

[ 617](structieee802154__key.md#a732a2a89e74139bd1d8e9b358c0306c7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key\_id\_mode](structieee802154__key.md#a732a2a89e74139bd1d8e9b358c0306c7);

[ 619](structieee802154__key.md#ae0a1e354b5718e8135fb6198ea12276a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[key\_id](structieee802154__key.md#ae0a1e354b5718e8135fb6198ea12276a);

620};

621

[ 623](group__ieee802154__driver.md#gab2bee8752291e082cb277145cef1225d)enum [ieee802154\_tx\_mode](group__ieee802154__driver.md#gab2bee8752291e082cb277145cef1225d) {

[ 625](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225da6904c3c7f53d46c5c8b41dd1a82b2650) [IEEE802154\_TX\_MODE\_DIRECT](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225da6904c3c7f53d46c5c8b41dd1a82b2650),

626

[ 628](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225da1e23f1ad3f9d0832fd4d67fc00fd8eb5) [IEEE802154\_TX\_MODE\_CCA](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225da1e23f1ad3f9d0832fd4d67fc00fd8eb5),

629

[ 635](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225da51a0e7cb482447779634062655a1ec47) [IEEE802154\_TX\_MODE\_CSMA\_CA](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225da51a0e7cb482447779634062655a1ec47),

636

[ 644](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225da9a7b8ba25603b72aecbf7f66abf26508) [IEEE802154\_TX\_MODE\_TXTIME](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225da9a7b8ba25603b72aecbf7f66abf26508),

645

[ 656](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225da42b4589afb2180fde053fdbbf58c0d3e) [IEEE802154\_TX\_MODE\_TXTIME\_CCA](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225da42b4589afb2180fde053fdbbf58c0d3e),

657

[ 659](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225daa389aeccad62a0516678564e68fcd595) [IEEE802154\_TX\_MODE\_COMMON\_COUNT](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225daa389aeccad62a0516678564e68fcd595),

660

[ 662](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225dabbab0c864f313ee4045e5ad59ea774e2) [IEEE802154\_TX\_MODE\_PRIV\_START](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225dabbab0c864f313ee4045e5ad59ea774e2) = [IEEE802154\_TX\_MODE\_COMMON\_COUNT](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225daa389aeccad62a0516678564e68fcd595),

663};

664

[ 666](group__ieee802154__driver.md#gab593bc6640ddea23c951982ca2f4c0bf)enum [ieee802154\_fpb\_mode](group__ieee802154__driver.md#gab593bc6640ddea23c951982ca2f4c0bf) {

[ 668](group__ieee802154__driver.md#ggab593bc6640ddea23c951982ca2f4c0bfa012874ab4d234bbeb2954756cf2dc9d6) [IEEE802154\_FPB\_ADDR\_MATCH\_THREAD](group__ieee802154__driver.md#ggab593bc6640ddea23c951982ca2f4c0bfa012874ab4d234bbeb2954756cf2dc9d6),

669

[ 673](group__ieee802154__driver.md#ggab593bc6640ddea23c951982ca2f4c0bfac7c839b7c0649d6151f90ff1d51ae417) [IEEE802154\_FPB\_ADDR\_MATCH\_ZIGBEE](group__ieee802154__driver.md#ggab593bc6640ddea23c951982ca2f4c0bfac7c839b7c0649d6151f90ff1d51ae417),

674};

675

[ 677](group__ieee802154__driver.md#ga34aecc5996174a812b295a3a4693ad09)enum [ieee802154\_config\_type](group__ieee802154__driver.md#ga34aecc5996174a812b295a3a4693ad09) {

[ 689](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a38c67aac70d24b31996871fe4686d9ee) [IEEE802154\_CONFIG\_AUTO\_ACK\_FPB](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a38c67aac70d24b31996871fe4686d9ee),

690

[ 699](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09ab897aea56ea5e9ddf306c5c0d75c2cd7) [IEEE802154\_CONFIG\_ACK\_FPB](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09ab897aea56ea5e9ddf306c5c0d75c2cd7),

700

[ 707](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09ab2b6ae3034fb469168ed29704ec045f0) [IEEE802154\_CONFIG\_PAN\_COORDINATOR](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09ab2b6ae3034fb469168ed29704ec045f0),

708

[ 714](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a399313ff2d8ebb3a2d72152a9615d8c5) [IEEE802154\_CONFIG\_PROMISCUOUS](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a399313ff2d8ebb3a2d72152a9615d8c5),

715

[ 722](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a8d88a76f71cf8869b3e35e423b18c6f3) [IEEE802154\_CONFIG\_EVENT\_HANDLER](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a8d88a76f71cf8869b3e35e423b18c6f3),

723

[ 735](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a8bd29c6d6aa67adaf23415eb337904c0) [IEEE802154\_CONFIG\_MAC\_KEYS](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a8bd29c6d6aa67adaf23415eb337904c0),

736

[ 752](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09aad7d04b7e1c02b2d88fcbb8ab1ac313b) [IEEE802154\_CONFIG\_FRAME\_COUNTER](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09aad7d04b7e1c02b2d88fcbb8ab1ac313b),

753

[ 766](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09aa34da77f0966ff5a0e8ac73ed68554a8) [IEEE802154\_CONFIG\_FRAME\_COUNTER\_IF\_LARGER](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09aa34da77f0966ff5a0e8ac73ed68554a8),

767

[ 817](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09af4e3dd7588ee06458f2d42f02797b3d6) [IEEE802154\_CONFIG\_RX\_SLOT](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09af4e3dd7588ee06458f2d42f02797b3d6),

818

[ 949](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a9fdbe95e0b7141d9150eaa4a5793c2e7) [IEEE802154\_CONFIG\_CSL\_PERIOD](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a9fdbe95e0b7141d9150eaa4a5793c2e7),

950

[ 1003](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a1a71ef76d90b6882196e4c6473de6bd8) [IEEE802154\_CONFIG\_EXPECTED\_RX\_TIME](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a1a71ef76d90b6882196e4c6473de6bd8),

1004

[ 1085](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a840e5f1db9a354e7bcd892ddb4117907) [IEEE802154\_CONFIG\_ENH\_ACK\_HEADER\_IE](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a840e5f1db9a354e7bcd892ddb4117907),

1086

[ 1114](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a9228dbe2583e5be10f64b116e87645e1) [IEEE802154\_CONFIG\_RX\_ON\_WHEN\_IDLE](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a9228dbe2583e5be10f64b116e87645e1),

1115

[ 1117](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a61df14aeb348cfc694d539b506dc23ac) [IEEE802154\_CONFIG\_COMMON\_COUNT](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a61df14aeb348cfc694d539b506dc23ac),

1118

[ 1120](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a1653b2869208045415d83fc6708d015c) [IEEE802154\_CONFIG\_PRIV\_START](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a1653b2869208045415d83fc6708d015c) = [IEEE802154\_CONFIG\_COMMON\_COUNT](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a61df14aeb348cfc694d539b506dc23ac),

1121};

1122

[ 1127](group__ieee802154__driver.md#ga1cb6434a3a7555fe9d35c73b698cbf10)#define IEEE802154\_CONFIG\_RX\_SLOT\_NONE -1LL

1128

[ 1137](group__ieee802154__driver.md#ga3828a2d56a39de92c2fd79caaac4c800)#define IEEE802154\_CONFIG\_RX\_SLOT\_OFF 0LL

1138

[ 1140](structieee802154__config.md)struct [ieee802154\_config](structieee802154__config.md) {

1142 union {

1144 struct {

[ 1145](structieee802154__config.md#ad9361f9ba1652e46d0be25e0de39afdf) bool [enabled](structieee802154__config.md#ad9361f9ba1652e46d0be25e0de39afdf);

[ 1146](structieee802154__config.md#ad139acde94327d4b8ceb76760751521d) enum [ieee802154\_fpb\_mode](group__ieee802154__driver.md#gab593bc6640ddea23c951982ca2f4c0bf) [mode](structieee802154__config.md#ad139acde94327d4b8ceb76760751521d);

[ 1147](structieee802154__config.md#ab27a654a0d53f268199e95dc21e18fd4) } [auto\_ack\_fpb](structieee802154__config.md#ab27a654a0d53f268199e95dc21e18fd4);

1148

1150 struct {

[ 1151](structieee802154__config.md#a673f5cceb6439bc1c3527c62062151d1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[addr](structieee802154__config.md#a673f5cceb6439bc1c3527c62062151d1);

[ 1152](structieee802154__config.md#a55823097d62a69d0c92dc70fb4ff1dd5) bool [extended](structieee802154__config.md#a55823097d62a69d0c92dc70fb4ff1dd5);

1153 bool [enabled](structieee802154__config.md#ad9361f9ba1652e46d0be25e0de39afdf);

[ 1154](structieee802154__config.md#a3a5e597e53bfcc9e3bed8bac2edb74d2) } [ack\_fpb](structieee802154__config.md#a3a5e597e53bfcc9e3bed8bac2edb74d2);

1155

[ 1157](structieee802154__config.md#a078ec577af3d170781ed770c80c54b72) bool [pan\_coordinator](structieee802154__config.md#a078ec577af3d170781ed770c80c54b72);

1158

[ 1160](structieee802154__config.md#aafb11c4130ff39e5c40dfe5d32c0d4e7) bool [promiscuous](structieee802154__config.md#aafb11c4130ff39e5c40dfe5d32c0d4e7);

1161

[ 1163](structieee802154__config.md#a8b7d4804cd051d69f3602f35cb4a8630) bool [rx\_on\_when\_idle](structieee802154__config.md#a8b7d4804cd051d69f3602f35cb4a8630);

1164

[ 1166](structieee802154__config.md#a1558e71a1d5ab74990964ff4deabbdb7) [ieee802154\_event\_cb\_t](group__ieee802154__driver.md#ga8219b80b8b179fc3a2ffac0dfdfb4e4b) [event\_handler](structieee802154__config.md#a1558e71a1d5ab74990964ff4deabbdb7);

1167

[ 1182](structieee802154__config.md#a942c0d4fb244c7256530536dc132a727) struct [ieee802154\_key](structieee802154__key.md) \*[mac\_keys](structieee802154__config.md#a942c0d4fb244c7256530536dc132a727);

1183

[ 1185](structieee802154__config.md#a272cfd864c7d47c6f06f26871ce07fb6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [frame\_counter](structieee802154__config.md#a272cfd864c7d47c6f06f26871ce07fb6);

1186

1188 struct {

[ 1200](structieee802154__config.md#a86b72101b0b21622f3cc8a2b3877e356) [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) [start](structieee802154__config.md#a86b72101b0b21622f3cc8a2b3877e356);

1201

[ 1212](structieee802154__config.md#ab36833b4311b03f08f67290f4edd8e41) [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) [duration](structieee802154__config.md#ab36833b4311b03f08f67290f4edd8e41);

1213

[ 1217](structieee802154__config.md#a8f7efaa743e070479632d139f0fc57c0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel](structieee802154__config.md#a8f7efaa743e070479632d139f0fc57c0);

[ 1218](structieee802154__config.md#aadc2714bf31484cce071e9ef7b9a4007) } [rx\_slot](structieee802154__config.md#aadc2714bf31484cce071e9ef7b9a4007);

1219

[ 1225](structieee802154__config.md#a5106a759148ec20c6c6c83a2581c9e88) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [csl\_period](structieee802154__config.md#a5106a759148ec20c6c6c83a2581c9e88);

1226

[ 1230](structieee802154__config.md#a8124aed4a4af36c0e21fd8f1b1c97e3e) [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) [expected\_rx\_time](structieee802154__config.md#a8124aed4a4af36c0e21fd8f1b1c97e3e);

1231

1233 struct {

[ 1243](structieee802154__config.md#a5343dec0de835943c0bef2c2d603a91d) struct ieee802154\_header\_ie \*[header\_ie](structieee802154__config.md#a5343dec0de835943c0bef2c2d603a91d);

1244

[ 1254](structieee802154__config.md#a03d6ec1a371312961f3a1ee42e113bbf) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[ext\_addr](structieee802154__config.md#a03d6ec1a371312961f3a1ee42e113bbf);

1255

[ 1265](structieee802154__config.md#aa27066dd9e54dab6795332b7413670f5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [short\_addr](structieee802154__config.md#aa27066dd9e54dab6795332b7413670f5);

1266

[ 1274](structieee802154__config.md#a8971a91be8748bd45027fcb730b99639) bool [purge\_ie](structieee802154__config.md#a8971a91be8748bd45027fcb730b99639);

[ 1275](structieee802154__config.md#a39c06e32cb4a74b4d8a9864f714e8c93) } [ack\_ie](structieee802154__config.md#a39c06e32cb4a74b4d8a9864f714e8c93);

1276 };

1277};

1278

[ 1285](group__ieee802154__driver.md#gaf4deddd3f23ebfd65fa47c5d62634430)enum [ieee802154\_attr](group__ieee802154__driver.md#gaf4deddd3f23ebfd65fa47c5d62634430) {

[ 1290](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430a4ad28f920776c45af9d430db786a926a) [IEEE802154\_ATTR\_PHY\_SUPPORTED\_CHANNEL\_PAGES](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430a4ad28f920776c45af9d430db786a926a),

1291

[ 1297](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430aba76daa0a70bcdd573ecbfd63ca19e7d) [IEEE802154\_ATTR\_PHY\_SUPPORTED\_CHANNEL\_RANGES](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430aba76daa0a70bcdd573ecbfd63ca19e7d),

1298

[ 1304](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430ad90b4a118866c4942ef6f6a8ae56eb3f) [IEEE802154\_ATTR\_PHY\_HRP\_UWB\_SUPPORTED\_PRFS](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430ad90b4a118866c4942ef6f6a8ae56eb3f),

1305

[ 1307](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430aa0830214987de7a89297777c0d1004de) [IEEE802154\_ATTR\_COMMON\_COUNT](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430aa0830214987de7a89297777c0d1004de),

1308

[ 1312](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430ad4912dc68abc1abe54bc212f023bf511) [IEEE802154\_ATTR\_PRIV\_START](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430ad4912dc68abc1abe54bc212f023bf511) = [IEEE802154\_ATTR\_COMMON\_COUNT](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430aa0830214987de7a89297777c0d1004de),

1313};

1314

[ 1328](structieee802154__attr__value.md)struct [ieee802154\_attr\_value](structieee802154__attr__value.md) {

1329 union {

1330 /\* TODO: Implement configuration of phyCurrentPage once drivers

1331 \* need to support channel page switching at runtime.

1332 \*/

[ 1349](structieee802154__attr__value.md#a75913597f93de1a80f96bb9dc32d38df) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [phy\_supported\_channel\_pages](structieee802154__attr__value.md#a75913597f93de1a80f96bb9dc32d38df);

1350

[ 1386](structieee802154__attr__value.md#a840d2f3a2502f87806ef79c6926f73f0) const struct [ieee802154\_phy\_supported\_channels](structieee802154__phy__supported__channels.md) \*[phy\_supported\_channels](structieee802154__attr__value.md#a840d2f3a2502f87806ef79c6926f73f0);

1387

1388 /\* TODO: Allow the PRF to be configured for each TX call once

1389 \* drivers need to support PRF switching at runtime.

1390 \*/

[ 1402](structieee802154__attr__value.md#af157805fb8acffb634cba4b37472bdb3) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [phy\_hrp\_uwb\_supported\_nominal\_prfs](structieee802154__attr__value.md#af157805fb8acffb634cba4b37472bdb3);

1403 };

1404};

1405

[ 1420](group__ieee802154__driver.md#gaf69d2b65aa46ec4483c6bab419413ba5)static inline int [ieee802154\_attr\_get\_channel\_page\_and\_range](group__ieee802154__driver.md#gaf69d2b65aa46ec4483c6bab419413ba5)(

1421 enum [ieee802154\_attr](group__ieee802154__driver.md#gaf4deddd3f23ebfd65fa47c5d62634430) attr,

1422 const enum [ieee802154\_phy\_channel\_page](group__ieee802154__driver.md#gacabc7386bea701373dfb36ab65bd36a9) phy\_supported\_channel\_page,

1423 const struct [ieee802154\_phy\_supported\_channels](structieee802154__phy__supported__channels.md) \*phy\_supported\_channels,

1424 struct [ieee802154\_attr\_value](structieee802154__attr__value.md) \*value)

1425{

1426 switch (attr) {

1427 case [IEEE802154\_ATTR\_PHY\_SUPPORTED\_CHANNEL\_PAGES](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430a4ad28f920776c45af9d430db786a926a):

1428 value->[phy\_supported\_channel\_pages](structieee802154__attr__value.md#a75913597f93de1a80f96bb9dc32d38df) = phy\_supported\_channel\_page;

1429 return 0;

1430

1431 case [IEEE802154\_ATTR\_PHY\_SUPPORTED\_CHANNEL\_RANGES](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430aba76daa0a70bcdd573ecbfd63ca19e7d):

1432 value->[phy\_supported\_channels](structieee802154__attr__value.md#a840d2f3a2502f87806ef79c6926f73f0) = phy\_supported\_channels;

1433 return 0;

1434

1435 default:

1436 return -[ENOENT](group__system__errno.md#ga03e689f378f643d16ea7537918528a48);

1437 }

1438}

1439

[ 1515](structieee802154__radio__api.md)struct [ieee802154\_radio\_api](structieee802154__radio__api.md) {

[ 1523](structieee802154__radio__api.md#a09a4b5df81822845f718952c6029442c) struct net\_if\_api [iface\_api](structieee802154__radio__api.md#aa955462d8c6950dc4b5935973f4575d8);

1524

1536 enum [ieee802154\_hw\_caps](group__ieee802154__driver.md#gaf99cda89c29df3c0088fc57ec09cbcd4) (\*[get\_capabilities](structieee802154__radio__api.md#a09a4b5df81822845f718952c6029442c))(const struct [device](structdevice.md) \*dev);

1537

[ 1554](structieee802154__radio__api.md#a2cbbd0e64fae28f748bb3e4d654a92bf) int (\*[cca](structieee802154__radio__api.md#a2cbbd0e64fae28f748bb3e4d654a92bf))(const struct [device](structdevice.md) \*dev);

1555

[ 1578](structieee802154__radio__api.md#a9ad27a2ff0a839dc5b9a4e6317cc59b1) int (\*[set\_channel](structieee802154__radio__api.md#a9ad27a2ff0a839dc5b9a4e6317cc59b1))(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) channel);

1579

[ 1603](structieee802154__radio__api.md#aa9502e0e014a8d05ffe235567e8c98f3) int (\*[filter](structieee802154__radio__api.md#aa9502e0e014a8d05ffe235567e8c98f3))(const struct [device](structdevice.md) \*dev,

1604 bool set,

1605 enum [ieee802154\_filter\_type](group__ieee802154__driver.md#gaa1971591e72866d0f3f0d4db2931e25a) type,

1606 const struct [ieee802154\_filter](structieee802154__filter.md) \*[filter](structieee802154__radio__api.md#aa9502e0e014a8d05ffe235567e8c98f3));

1607

[ 1624](structieee802154__radio__api.md#aeeab6dfcde08af23357ea40f8af68f66) int (\*[set\_txpower](structieee802154__radio__api.md#aeeab6dfcde08af23357ea40f8af68f66))(const struct [device](structdevice.md) \*dev, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) dbm);

1625

[ 1718](structieee802154__radio__api.md#a70139acec22642c1fc09f2323c383fe6) int (\*[tx](structieee802154__radio__api.md#a70139acec22642c1fc09f2323c383fe6))(const struct [device](structdevice.md) \*dev, enum [ieee802154\_tx\_mode](group__ieee802154__driver.md#gab2bee8752291e082cb277145cef1225d) mode,

1719 struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*frag);

1720

[ 1742](structieee802154__radio__api.md#a0e4d57dc3a53299ddedf2140e172103d) int (\*[start](structieee802154__radio__api.md#a0e4d57dc3a53299ddedf2140e172103d))(const struct [device](structdevice.md) \*dev);

1743

[ 1766](structieee802154__radio__api.md#a75cfcfe2b9e69c2e4af53f00c8294b36) int (\*[stop](structieee802154__radio__api.md#a75cfcfe2b9e69c2e4af53f00c8294b36))(const struct [device](structdevice.md) \*dev);

1767

[ 1787](structieee802154__radio__api.md#a5b9b45e274fd6a8777cd96280b1a1b9e) int (\*[continuous\_carrier](structieee802154__radio__api.md#a5b9b45e274fd6a8777cd96280b1a1b9e))(const struct [device](structdevice.md) \*dev);

1788

[ 1824](structieee802154__radio__api.md#a9acaf4810bd5d3b026cc381bff301071) int (\*[configure](structieee802154__radio__api.md#a9acaf4810bd5d3b026cc381bff301071))(const struct [device](structdevice.md) \*dev,

1825 enum [ieee802154\_config\_type](group__ieee802154__driver.md#ga34aecc5996174a812b295a3a4693ad09) type,

1826 const struct [ieee802154\_config](structieee802154__config.md) \*config);

1827

[ 1852](structieee802154__radio__api.md#a01fc17f85f2be33877a9347f59a84c54) int (\*[ed\_scan](structieee802154__radio__api.md#a01fc17f85f2be33877a9347f59a84c54))(const struct [device](structdevice.md) \*dev,

1853 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) duration,

1854 [energy\_scan\_done\_cb\_t](group__ieee802154__driver.md#ga8c9ab3cecefe641a25f003eb6d014fc5) done\_cb);

1855

[ 1873](structieee802154__radio__api.md#a829a0d59fdcda5b6cb029ef1334a6b8b) [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) (\*[get\_time](structieee802154__radio__api.md#a829a0d59fdcda5b6cb029ef1334a6b8b))(const struct [device](structdevice.md) \*dev);

1874

[ 1895](structieee802154__radio__api.md#ae4a3ef40a5b8031c868d72ead163c97d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) (\*[get\_sch\_acc](structieee802154__radio__api.md#ae4a3ef40a5b8031c868d72ead163c97d))(const struct [device](structdevice.md) \*dev);

1896

[ 1918](structieee802154__radio__api.md#a0b3e0ed1385dd428c861e08c79849ef4) int (\*[attr\_get](structieee802154__radio__api.md#a0b3e0ed1385dd428c861e08c79849ef4))(const struct [device](structdevice.md) \*dev,

1919 enum [ieee802154\_attr](group__ieee802154__driver.md#gaf4deddd3f23ebfd65fa47c5d62634430) attr,

1920 struct [ieee802154\_attr\_value](structieee802154__attr__value.md) \*value);

1921};

1922

1923/\* Make sure that the network interface API is properly setup inside

1924 \* IEEE 802.15.4 driver API struct (it is the first one).

1925 \*/

1926BUILD\_ASSERT(offsetof(struct [ieee802154\_radio\_api](structieee802154__radio__api.md), iface\_api) == 0);

1927

1929

1934

1936#define IEEE802154\_AR\_FLAG\_SET (0x20)

1938

[ 1949](group__ieee802154__driver.md#gaf5d7bdde2a9774f9d90604a6e203bb07)static inline bool [ieee802154\_is\_ar\_flag\_set](group__ieee802154__driver.md#gaf5d7bdde2a9774f9d90604a6e203bb07)(struct [net\_buf](structnet__buf.md) \*frag)

1950{

1951 return (\*frag->[data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56) & IEEE802154\_AR\_FLAG\_SET);

1952}

1953

1955

1960

1961/\* TODO: Fix drivers to either unref the packet before they return NET\_OK or to

1962 \* return NET\_CONTINUE instead. See note below.

1963 \*/

[ 1986](group__ieee802154__driver.md#ga68e1f89571ccbefef61a5496577337fc)extern enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) [ieee802154\_handle\_ack](group__ieee802154__driver.md#ga68e1f89571ccbefef61a5496577337fc)(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

1987

2001#ifndef CONFIG\_IEEE802154\_RAW\_MODE

[ 2002](group__ieee802154__driver.md#gad2a4cb5df84ffe20b83fc54dc9bcfc91)extern void [ieee802154\_init](group__ieee802154__driver.md#gad2a4cb5df84ffe20b83fc54dc9bcfc91)(struct [net\_if](structnet__if.md) \*iface);

2003#else

2004#define ieee802154\_init(\_iface\_)

2005#endif /\* CONFIG\_IEEE802154\_RAW\_MODE \*/

2006

2008

2009#ifdef \_\_cplusplus

2010}

2011#endif

2012

2016

2017#endif /\* ZEPHYR\_INCLUDE\_NET\_IEEE802154\_RADIO\_H\_ \*/

[device.h](device_8h.md)

[ieee802154\_rx\_fail\_reason](group__ieee802154__driver.md#ga04febbd15f9e6f6540d711ada5a4a1c8)

ieee802154\_rx\_fail\_reason

RX failed event reasons, see IEEE802154\_EVENT\_RX\_FAILED.

**Definition** ieee802154\_radio.h:573

[ieee802154\_phy\_hrp\_uwb\_nominal\_prf](group__ieee802154__driver.md#ga13610aeef06372bc47d84464537fdded)

ieee802154\_phy\_hrp\_uwb\_nominal\_prf

represents the nominal pulse rate frequency of an HRP UWB PHY

**Definition** ieee802154\_radio.h:381

[ieee802154\_event](group__ieee802154__driver.md#ga3491982b677941442d904ce69fce7c5e)

ieee802154\_event

Driver events, see IEEE802154\_CONFIG\_EVENT\_HANDLER.

**Definition** ieee802154\_radio.h:557

[ieee802154\_config\_type](group__ieee802154__driver.md#ga34aecc5996174a812b295a3a4693ad09)

ieee802154\_config\_type

IEEE 802.15.4 driver configuration types.

**Definition** ieee802154\_radio.h:677

[ieee802154\_handle\_ack](group__ieee802154__driver.md#ga68e1f89571ccbefef61a5496577337fc)

enum net\_verdict ieee802154\_handle\_ack(struct net\_if \*iface, struct net\_pkt \*pkt)

IEEE 802.15.4 driver ACK handling callback into L2 that drivers must call when receiving an ACK packa...

[ieee802154\_event\_cb\_t](group__ieee802154__driver.md#ga8219b80b8b179fc3a2ffac0dfdfb4e4b)

void(\* ieee802154\_event\_cb\_t)(const struct device \*dev, enum ieee802154\_event evt, void \*event\_params)

Driver event callback.

**Definition** ieee802154\_radio.h:589

[energy\_scan\_done\_cb\_t](group__ieee802154__driver.md#ga8c9ab3cecefe641a25f003eb6d014fc5)

void(\* energy\_scan\_done\_cb\_t)(const struct device \*dev, int16\_t max\_ed)

Energy scan callback.

**Definition** ieee802154\_radio.h:585

[ieee802154\_filter\_type](group__ieee802154__driver.md#gaa1971591e72866d0f3f0d4db2931e25a)

ieee802154\_filter\_type

Filter type, see ieee802154\_radio\_api::filter.

**Definition** ieee802154\_radio.h:548

[ieee802154\_tx\_mode](group__ieee802154__driver.md#gab2bee8752291e082cb277145cef1225d)

ieee802154\_tx\_mode

IEEE 802.15.4 Transmission mode.

**Definition** ieee802154\_radio.h:623

[ieee802154\_fpb\_mode](group__ieee802154__driver.md#gab593bc6640ddea23c951982ca2f4c0bf)

ieee802154\_fpb\_mode

IEEE 802.15.4 Frame Pending Bit table address matching mode.

**Definition** ieee802154\_radio.h:666

[ieee802154\_phy\_channel\_page](group__ieee802154__driver.md#gacabc7386bea701373dfb36ab65bd36a9)

ieee802154\_phy\_channel\_page

PHY channel pages, see section 10.1.3.

**Definition** ieee802154\_radio.h:169

[ieee802154\_init](group__ieee802154__driver.md#gad2a4cb5df84ffe20b83fc54dc9bcfc91)

void ieee802154\_init(struct net\_if \*iface)

IEEE 802.15.4 driver initialization callback into L2 called by drivers to initialize the active L2 st...

[ieee802154\_attr](group__ieee802154__driver.md#gaf4deddd3f23ebfd65fa47c5d62634430)

ieee802154\_attr

IEEE 802.15.4 driver attributes.

**Definition** ieee802154\_radio.h:1285

[ieee802154\_is\_ar\_flag\_set](group__ieee802154__driver.md#gaf5d7bdde2a9774f9d90604a6e203bb07)

static bool ieee802154\_is\_ar\_flag\_set(struct net\_buf \*frag)

Check if the AR flag is set on the frame inside the given Network Packet Library.

**Definition** ieee802154\_radio.h:1949

[ieee802154\_attr\_get\_channel\_page\_and\_range](group__ieee802154__driver.md#gaf69d2b65aa46ec4483c6bab419413ba5)

static int ieee802154\_attr\_get\_channel\_page\_and\_range(enum ieee802154\_attr attr, const enum ieee802154\_phy\_channel\_page phy\_supported\_channel\_page, const struct ieee802154\_phy\_supported\_channels \*phy\_supported\_channels, struct ieee802154\_attr\_value \*value)

Helper function to handle channel page and range to be called from drivers' attr\_get() implementation...

**Definition** ieee802154\_radio.h:1420

[ieee802154\_hw\_caps](group__ieee802154__driver.md#gaf99cda89c29df3c0088fc57ec09cbcd4)

ieee802154\_hw\_caps

IEEE 802.15.4 driver capabilities.

**Definition** ieee802154\_radio.h:437

[IEEE802154\_RX\_FAIL\_INVALID\_FCS](group__ieee802154__driver.md#gga04febbd15f9e6f6540d711ada5a4a1c8a103f6683ff71f4f7248ee1a0d09d6be4)

@ IEEE802154\_RX\_FAIL\_INVALID\_FCS

Frame had invalid checksum.

**Definition** ieee802154\_radio.h:577

[IEEE802154\_RX\_FAIL\_OTHER](group__ieee802154__driver.md#gga04febbd15f9e6f6540d711ada5a4a1c8a5baa9dd683a717f7fbdfc5ab85935a3b)

@ IEEE802154\_RX\_FAIL\_OTHER

General reason.

**Definition** ieee802154\_radio.h:581

[IEEE802154\_RX\_FAIL\_ADDR\_FILTERED](group__ieee802154__driver.md#gga04febbd15f9e6f6540d711ada5a4a1c8a7ff9cfcc5e4dfc2bf7abe1860a39410f)

@ IEEE802154\_RX\_FAIL\_ADDR\_FILTERED

Address did not match.

**Definition** ieee802154\_radio.h:579

[IEEE802154\_RX\_FAIL\_NOT\_RECEIVED](group__ieee802154__driver.md#gga04febbd15f9e6f6540d711ada5a4a1c8ad584824b4813626d04a85499371b9c32)

@ IEEE802154\_RX\_FAIL\_NOT\_RECEIVED

Nothing received.

**Definition** ieee802154\_radio.h:575

[IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_64\_M](group__ieee802154__driver.md#gga13610aeef06372bc47d84464537fddeda2b24236d3531cab7d21673d065b7c29e)

@ IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_64\_M

**Definition** ieee802154\_radio.h:386

[IEEE802154\_PHY\_HRP\_UWB\_PRF\_OFF](group__ieee802154__driver.md#gga13610aeef06372bc47d84464537fddeda4369c745ed378d8273a1014322f3029a)

@ IEEE802154\_PHY\_HRP\_UWB\_PRF\_OFF

standard modes, see section 8.3.2, table 8-88.

**Definition** ieee802154\_radio.h:383

[IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_4\_M](group__ieee802154__driver.md#gga13610aeef06372bc47d84464537fddeda9dc3c58366502aeab04a208937536369)

@ IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_4\_M

**Definition** ieee802154\_radio.h:384

[IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_256\_M\_HPRF](group__ieee802154__driver.md#gga13610aeef06372bc47d84464537fddedacb66442cf2a5e4c539b6b7edf8419be1)

@ IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_256\_M\_HPRF

**Definition** ieee802154\_radio.h:395

[IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_64\_M\_BPRF](group__ieee802154__driver.md#gga13610aeef06372bc47d84464537fddedad920ae285cdcc2a4d59f7c23e29dce27)

@ IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_64\_M\_BPRF

enhanced ranging device (ERDEV) modes not specified in table 8-88, see IEEE 802.15....

**Definition** ieee802154\_radio.h:393

[IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_16\_M](group__ieee802154__driver.md#gga13610aeef06372bc47d84464537fddedadf9230e6ef62ce66129bfe24f537c88a)

@ IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_16\_M

**Definition** ieee802154\_radio.h:385

[IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_128\_M\_HPRF](group__ieee802154__driver.md#gga13610aeef06372bc47d84464537fddedae6c88efd301a449b1a31e8aedf4e30ca)

@ IEEE802154\_PHY\_HRP\_UWB\_NOMINAL\_128\_M\_HPRF

**Definition** ieee802154\_radio.h:394

[IEEE802154\_EVENT\_TX\_STARTED](group__ieee802154__driver.md#gga3491982b677941442d904ce69fce7c5eaacd61f4466f1ef926adc9e1afe6c1648)

@ IEEE802154\_EVENT\_TX\_STARTED

Data transmission started.

**Definition** ieee802154\_radio.h:559

[IEEE802154\_EVENT\_RX\_FAILED](group__ieee802154__driver.md#gga3491982b677941442d904ce69fce7c5eaef51197ca09befaee8cdfa2cde107273)

@ IEEE802154\_EVENT\_RX\_FAILED

Data reception failed.

**Definition** ieee802154\_radio.h:561

[IEEE802154\_EVENT\_RX\_OFF](group__ieee802154__driver.md#gga3491982b677941442d904ce69fce7c5eaf7ed46b9d13a232a2ea6b650514eea3d)

@ IEEE802154\_EVENT\_RX\_OFF

An RX slot ended, requires IEEE802154\_HW\_RXTIME.

**Definition** ieee802154\_radio.h:569

[IEEE802154\_CONFIG\_PRIV\_START](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a1653b2869208045415d83fc6708d015c)

@ IEEE802154\_CONFIG\_PRIV\_START

This and higher values are specific to the protocol- or driver-specific extensions.

**Definition** ieee802154\_radio.h:1120

[IEEE802154\_CONFIG\_EXPECTED\_RX\_TIME](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a1a71ef76d90b6882196e4c6473de6bd8)

@ IEEE802154\_CONFIG\_EXPECTED\_RX\_TIME

Configure a timepoint at which an RX frame is expected to arrive.

**Definition** ieee802154\_radio.h:1003

[IEEE802154\_CONFIG\_AUTO\_ACK\_FPB](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a38c67aac70d24b31996871fe4686d9ee)

@ IEEE802154\_CONFIG\_AUTO\_ACK\_FPB

Indicates how the driver should set the Frame Pending bit in ACK responses for Data Requests.

**Definition** ieee802154\_radio.h:689

[IEEE802154\_CONFIG\_PROMISCUOUS](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a399313ff2d8ebb3a2d72152a9615d8c5)

@ IEEE802154\_CONFIG\_PROMISCUOUS

Enable/disable promiscuous mode.

**Definition** ieee802154\_radio.h:714

[IEEE802154\_CONFIG\_COMMON\_COUNT](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a61df14aeb348cfc694d539b506dc23ac)

@ IEEE802154\_CONFIG\_COMMON\_COUNT

Number of types defined in ieee802154\_config\_type.

**Definition** ieee802154\_radio.h:1117

[IEEE802154\_CONFIG\_ENH\_ACK\_HEADER\_IE](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a840e5f1db9a354e7bcd892ddb4117907)

@ IEEE802154\_CONFIG\_ENH\_ACK\_HEADER\_IE

Adds a header information element (IE) to be injected into enhanced ACK frames generated by the drive...

**Definition** ieee802154\_radio.h:1085

[IEEE802154\_CONFIG\_MAC\_KEYS](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a8bd29c6d6aa67adaf23415eb337904c0)

@ IEEE802154\_CONFIG\_MAC\_KEYS

Updates MAC keys, key index and the per-key frame counter for drivers supporting transmit security of...

**Definition** ieee802154\_radio.h:735

[IEEE802154\_CONFIG\_EVENT\_HANDLER](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a8d88a76f71cf8869b3e35e423b18c6f3)

@ IEEE802154\_CONFIG\_EVENT\_HANDLER

Specifies new IEEE 802.15.4 driver event handler.

**Definition** ieee802154\_radio.h:722

[IEEE802154\_CONFIG\_RX\_ON\_WHEN\_IDLE](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a9228dbe2583e5be10f64b116e87645e1)

@ IEEE802154\_CONFIG\_RX\_ON\_WHEN\_IDLE

Enable/disable RxOnWhenIdle MAC PIB attribute (Table 8-94).

**Definition** ieee802154\_radio.h:1114

[IEEE802154\_CONFIG\_CSL\_PERIOD](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a9fdbe95e0b7141d9150eaa4a5793c2e7)

@ IEEE802154\_CONFIG\_CSL\_PERIOD

Enables or disables a device as a CSL receiver and configures its CSL period.

**Definition** ieee802154\_radio.h:949

[IEEE802154\_CONFIG\_FRAME\_COUNTER\_IF\_LARGER](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09aa34da77f0966ff5a0e8ac73ed68554a8)

@ IEEE802154\_CONFIG\_FRAME\_COUNTER\_IF\_LARGER

Sets the current MAC frame counter value if the provided value is greater than the current one.

**Definition** ieee802154\_radio.h:766

[IEEE802154\_CONFIG\_FRAME\_COUNTER](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09aad7d04b7e1c02b2d88fcbb8ab1ac313b)

@ IEEE802154\_CONFIG\_FRAME\_COUNTER

Sets the current MAC frame counter value associated with the interface for drivers supporting transmi...

**Definition** ieee802154\_radio.h:752

[IEEE802154\_CONFIG\_PAN\_COORDINATOR](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09ab2b6ae3034fb469168ed29704ec045f0)

@ IEEE802154\_CONFIG\_PAN\_COORDINATOR

Indicates whether the device is a PAN coordinator.

**Definition** ieee802154\_radio.h:707

[IEEE802154\_CONFIG\_ACK\_FPB](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09ab897aea56ea5e9ddf306c5c0d75c2cd7)

@ IEEE802154\_CONFIG\_ACK\_FPB

Indicates whether to set ACK Frame Pending bit for specific address or not.

**Definition** ieee802154\_radio.h:699

[IEEE802154\_CONFIG\_RX\_SLOT](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09af4e3dd7588ee06458f2d42f02797b3d6)

@ IEEE802154\_CONFIG\_RX\_SLOT

Set or unset a radio reception window (RX slot).

**Definition** ieee802154\_radio.h:817

[IEEE802154\_FILTER\_TYPE\_SHORT\_ADDR](group__ieee802154__driver.md#ggaa1971591e72866d0f3f0d4db2931e25aa2fa1ac98a3b870fcf6e85e7ec82cfbe9)

@ IEEE802154\_FILTER\_TYPE\_SHORT\_ADDR

Short address type filter.

**Definition** ieee802154\_radio.h:550

[IEEE802154\_FILTER\_TYPE\_IEEE\_ADDR](group__ieee802154__driver.md#ggaa1971591e72866d0f3f0d4db2931e25aa928a93b536c6408b3d77aa329c274fe8)

@ IEEE802154\_FILTER\_TYPE\_IEEE\_ADDR

Address type filter.

**Definition** ieee802154\_radio.h:549

[IEEE802154\_FILTER\_TYPE\_PAN\_ID](group__ieee802154__driver.md#ggaa1971591e72866d0f3f0d4db2931e25aab44cc830999926a5d232aedabef52653)

@ IEEE802154\_FILTER\_TYPE\_PAN\_ID

PAN id type filter.

**Definition** ieee802154\_radio.h:551

[IEEE802154\_FILTER\_TYPE\_SRC\_SHORT\_ADDR](group__ieee802154__driver.md#ggaa1971591e72866d0f3f0d4db2931e25aac6dbb68674e7594fd4cd69bbe4ea60de)

@ IEEE802154\_FILTER\_TYPE\_SRC\_SHORT\_ADDR

Source short address type filter.

**Definition** ieee802154\_radio.h:553

[IEEE802154\_FILTER\_TYPE\_SRC\_IEEE\_ADDR](group__ieee802154__driver.md#ggaa1971591e72866d0f3f0d4db2931e25aade18e03611339f5f7ec4fdcdee409c21)

@ IEEE802154\_FILTER\_TYPE\_SRC\_IEEE\_ADDR

Source address type filter.

**Definition** ieee802154\_radio.h:552

[IEEE802154\_TX\_MODE\_CCA](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225da1e23f1ad3f9d0832fd4d67fc00fd8eb5)

@ IEEE802154\_TX\_MODE\_CCA

Perform CCA before packet transmission.

**Definition** ieee802154\_radio.h:628

[IEEE802154\_TX\_MODE\_TXTIME\_CCA](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225da42b4589afb2180fde053fdbbf58c0d3e)

@ IEEE802154\_TX\_MODE\_TXTIME\_CCA

Transmit packet in the future, perform CCA before transmission.

**Definition** ieee802154\_radio.h:656

[IEEE802154\_TX\_MODE\_CSMA\_CA](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225da51a0e7cb482447779634062655a1ec47)

@ IEEE802154\_TX\_MODE\_CSMA\_CA

Perform full CSMA/CA procedure before packet transmission.

**Definition** ieee802154\_radio.h:635

[IEEE802154\_TX\_MODE\_DIRECT](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225da6904c3c7f53d46c5c8b41dd1a82b2650)

@ IEEE802154\_TX\_MODE\_DIRECT

Transmit packet immediately, no CCA.

**Definition** ieee802154\_radio.h:625

[IEEE802154\_TX\_MODE\_TXTIME](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225da9a7b8ba25603b72aecbf7f66abf26508)

@ IEEE802154\_TX\_MODE\_TXTIME

Transmit packet in the future, at the specified time, no CCA.

**Definition** ieee802154\_radio.h:644

[IEEE802154\_TX\_MODE\_COMMON\_COUNT](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225daa389aeccad62a0516678564e68fcd595)

@ IEEE802154\_TX\_MODE\_COMMON\_COUNT

Number of modes defined in ieee802154\_tx\_mode.

**Definition** ieee802154\_radio.h:659

[IEEE802154\_TX\_MODE\_PRIV\_START](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225dabbab0c864f313ee4045e5ad59ea774e2)

@ IEEE802154\_TX\_MODE\_PRIV\_START

This and higher values are specific to the protocol- or driver-specific extensions.

**Definition** ieee802154\_radio.h:662

[IEEE802154\_FPB\_ADDR\_MATCH\_THREAD](group__ieee802154__driver.md#ggab593bc6640ddea23c951982ca2f4c0bfa012874ab4d234bbeb2954756cf2dc9d6)

@ IEEE802154\_FPB\_ADDR\_MATCH\_THREAD

The pending bit shall be set only for addresses found in the list.

**Definition** ieee802154\_radio.h:668

[IEEE802154\_FPB\_ADDR\_MATCH\_ZIGBEE](group__ieee802154__driver.md#ggab593bc6640ddea23c951982ca2f4c0bfac7c839b7c0649d6151f90ff1d51ae417)

@ IEEE802154\_FPB\_ADDR\_MATCH\_ZIGBEE

The pending bit shall be cleared for short addresses found in the list.

**Definition** ieee802154\_radio.h:673

[IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_TEN\_SUN\_FSK\_GENERIC](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a02a17ea787e99528b2a6a8f5107f2544)

@ IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_TEN\_SUN\_FSK\_GENERIC

SUN FSK/OFDM/O-QPSK PHYs - generic modulation and channel description, see sections 10....

**Definition** ieee802154\_radio.h:219

[IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_SEVEN\_MSK](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a1f33467ec7659ef411b08f7a23663311)

@ IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_SEVEN\_MSK

MSK PHY - 780 MHz and 2450 MHz bands, see sections 10.1.3.6, 10.1.3.7.

**Definition** ieee802154\_radio.h:204

[IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_ONE\_DEPRECATED](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a371a12ec5d762b03058fb2532fa04e45)

@ IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_ONE\_DEPRECATED

Formerly ASK PHY - deprecated in IEEE 802.15.4-2015.

**Definition** ieee802154\_radio.h:186

[IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_THIRTEEN\_RCC](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a56dd4ae42595ef0edb109c729e333b08)

@ IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_THIRTEEN\_RCC

RCC PHY, see section 10.1.3.12.

**Definition** ieee802154\_radio.h:228

[IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_TWO\_OQPSK\_868\_915](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a5776e0160927b83f4e4e8d6479aaf804)

@ IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_TWO\_OQPSK\_868\_915

O-QPSK PHY - 868 MHz and 915 MHz bands, see section 10.1.3.3.

**Definition** ieee802154\_radio.h:189

[IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_FOUR\_HRP\_UWB](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a68b93381ddc1184ff0ed13456cf4b6a8)

@ IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_FOUR\_HRP\_UWB

UWB PHY - SubG, low and high bands, see section 10.1.3.5.

**Definition** ieee802154\_radio.h:195

[IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_TWELVE\_LECIM](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a6d4023088a3607c072acebd3940340c7)

@ IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_TWELVE\_LECIM

LECIM DSSS/FSK PHYs, see section 10.1.3.11.

**Definition** ieee802154\_radio.h:225

[IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_FIVE\_OQPSK\_780](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a6ea456573a6ff8aed348a9dc547b2db7)

@ IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_FIVE\_OQPSK\_780

O-QPSK PHY - 780 MHz band, see section 10.1.3.2.

**Definition** ieee802154\_radio.h:198

[IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_THREE\_CSS](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a6f71c162be118b0c2edce139753c867e)

@ IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_THREE\_CSS

CSS PHY - 2450 MHz band, see section 10.1.3.4.

**Definition** ieee802154\_radio.h:192

[IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_ZERO\_OQPSK\_2450\_BPSK\_868\_915](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a72b17a977aeb6792f7d2016117f4b2f9)

@ IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_ZERO\_OQPSK\_2450\_BPSK\_868\_915

Channel page zero supports the 2.4G channels of the O-QPSK PHY and all channels from the BPSK PHYs in...

**Definition** ieee802154\_radio.h:183

[IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_NINE\_SUN\_PREDEFINED](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9a996b529c9c277d6d653d0e0ffb8b2902)

@ IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_NINE\_SUN\_PREDEFINED

SUN FSK/OFDM/O-QPSK PHYs - predefined bands, operating modes and channels, see sections 10....

**Definition** ieee802154\_radio.h:213

[IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_EIGHT\_LRP\_UWB](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9aa0ab080c8cdac42dbf80622d075854dc)

@ IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_EIGHT\_LRP\_UWB

LRP UWB PHY, see sections 10.1.3.8.

**Definition** ieee802154\_radio.h:207

[IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_ELEVEN\_OQPSK\_2380](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9aad0644244fb5b6cba5a295e246722e94)

@ IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_ELEVEN\_OQPSK\_2380

O-QPSK PHY - 2380 MHz band, see section 10.1.3.10.

**Definition** ieee802154\_radio.h:222

[IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_SIX\_RESERVED](group__ieee802154__driver.md#ggacabc7386bea701373dfb36ab65bd36a9ac13dda08becd3d4799d45ef02f774cc1)

@ IEEE802154\_ATTR\_PHY\_CHANNEL\_PAGE\_SIX\_RESERVED

reserved - not currently assigned

**Definition** ieee802154\_radio.h:201

[IEEE802154\_ATTR\_PHY\_SUPPORTED\_CHANNEL\_PAGES](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430a4ad28f920776c45af9d430db786a926a)

@ IEEE802154\_ATTR\_PHY\_SUPPORTED\_CHANNEL\_PAGES

Retrieves a bit field with supported channel pages.

**Definition** ieee802154\_radio.h:1290

[IEEE802154\_ATTR\_COMMON\_COUNT](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430aa0830214987de7a89297777c0d1004de)

@ IEEE802154\_ATTR\_COMMON\_COUNT

Number of attributes defined in ieee802154\_attr.

**Definition** ieee802154\_radio.h:1307

[IEEE802154\_ATTR\_PHY\_SUPPORTED\_CHANNEL\_RANGES](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430aba76daa0a70bcdd573ecbfd63ca19e7d)

@ IEEE802154\_ATTR\_PHY\_SUPPORTED\_CHANNEL\_RANGES

Retrieves a pointer to the array of supported channel ranges within the currently configured channel ...

**Definition** ieee802154\_radio.h:1297

[IEEE802154\_ATTR\_PRIV\_START](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430ad4912dc68abc1abe54bc212f023bf511)

@ IEEE802154\_ATTR\_PRIV\_START

This and higher values are specific to the protocol- or driver-specific extensions.

**Definition** ieee802154\_radio.h:1312

[IEEE802154\_ATTR\_PHY\_HRP\_UWB\_SUPPORTED\_PRFS](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430ad90b4a118866c4942ef6f6a8ae56eb3f)

@ IEEE802154\_ATTR\_PHY\_HRP\_UWB\_SUPPORTED\_PRFS

Retrieves a bit field with supported HRP UWB nominal pulse repetition frequencies.

**Definition** ieee802154\_radio.h:1304

[IEEE802154\_HW\_FCS](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a0ea21cab335dd9082feb2d08be0eb5fa)

@ IEEE802154\_HW\_FCS

Frame checksum verification supported.

**Definition** ieee802154\_radio.h:465

[IEEE802154\_HW\_ENERGY\_SCAN](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a179ad073a5bd34e4e4af587d07ca3f73)

@ IEEE802154\_HW\_ENERGY\_SCAN

Energy detection (ED) supported (optional).

**Definition** ieee802154\_radio.h:447

[IEEE802154\_HW\_CSMA](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a2ee53f11e1ed6853e1f5d9dfe7d7bdf7)

@ IEEE802154\_HW\_CSMA

CSMA-CA procedure supported on TX.

**Definition** ieee802154\_radio.h:474

[IEEE802154\_HW\_SLEEP\_TO\_TX](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a36f46639c08e70bc30fc98ca1043b071)

@ IEEE802154\_HW\_SLEEP\_TO\_TX

TX directly from sleep supported.

**Definition** ieee802154\_radio.h:512

[IEEE802154\_HW\_TXTIME](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a435d032f42d509bd78a992de6e4d7b1d)

@ IEEE802154\_HW\_TXTIME

TX at specified time supported.

**Definition** ieee802154\_radio.h:486

[IEEE802154\_HW\_PROMISC](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a4adb33f2ca81a24244dead6b379cd916)

@ IEEE802154\_HW\_PROMISC

Promiscuous mode supported.

**Definition** ieee802154\_radio.h:471

[IEEE802154\_HW\_RXTIME](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a68ae68c83a87f0efc25f74edd80c4600)

@ IEEE802154\_HW\_RXTIME

Timed RX window scheduling supported.

**Definition** ieee802154\_radio.h:515

[IEEE802154\_HW\_RETRANSMISSION](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a752472a994bdcbdf9cdf86deb0231849)

@ IEEE802154\_HW\_RETRANSMISSION

Supports retransmission on TX ACK timeout.

**Definition** ieee802154\_radio.h:480

[IEEE802154\_HW\_TX\_SEC](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a7924c3d5bfe6dceeb2e8caa6df7edecb)

@ IEEE802154\_HW\_TX\_SEC

TX security supported (key management, encryption and authentication).

**Definition** ieee802154\_radio.h:518

[IEEE802154\_HW\_TX\_RX\_ACK](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4ab383a932c0ac9deece68f02210089119)

@ IEEE802154\_HW\_TX\_RX\_ACK

Waits for ACK on TX if AR bit is set in TX pkt.

**Definition** ieee802154\_radio.h:477

[IEEE802154\_HW\_SELECTIVE\_TXCHANNEL](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4ab6cf4f3552d6193027a538a13b95952e)

@ IEEE802154\_HW\_SELECTIVE\_TXCHANNEL

Support for timed transmissions on selective channel.

**Definition** ieee802154\_radio.h:534

[IEEE802154\_RX\_ON\_WHEN\_IDLE](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4ac1e00966043e5884c4cbd65fb26f0c0b)

@ IEEE802154\_RX\_ON\_WHEN\_IDLE

RxOnWhenIdle handling supported.

**Definition** ieee802154\_radio.h:521

[IEEE802154\_HW\_RX\_TX\_ACK](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4aec16c4d418117de2d106e84297568b03)

@ IEEE802154\_HW\_RX\_TX\_ACK

Sends ACK on RX if AR bit is set in RX pkt.

**Definition** ieee802154\_radio.h:483

[IEEE802154\_HW\_FILTER](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4afd09f329a708d00f1384a50c59ddde27)

@ IEEE802154\_HW\_FILTER

Filtering of PAN ID, extended and short address supported.

**Definition** ieee802154\_radio.h:468

[net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)

net\_verdict

Net Verdict.

**Definition** net\_core.h:102

[net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56)

int64\_t net\_time\_t

Any occurrence of net\_time\_t specifies a concept of nanosecond resolution scalar time span,...

**Definition** net\_time.h:103

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[ENOENT](group__system__errno.md#ga03e689f378f643d16ea7537918528a48)

#define ENOENT

No such file or directory.

**Definition** errno.h:40

[ieee802154.h](ieee802154_8h.md)

IEEE 802.15.4 native L2 stack public header.

[ieee802154\_ie.h](ieee802154__ie_8h.md)

IEEE 802.15.4 MAC information element (IE) related types and helpers.

[net\_if.h](net__if_8h.md)

Public API for network interface.

[net\_pkt.h](net__pkt_8h.md)

Network packet buffer descriptor API.

[net\_time.h](net__time_8h.md)

Representation of nanosecond resolution elapsed time and timestamps in the network stack.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[ieee802154\_attr\_value](structieee802154__attr__value.md)

IEEE 802.15.4 driver attribute values.

**Definition** ieee802154\_radio.h:1328

[ieee802154\_attr\_value::phy\_supported\_channel\_pages](structieee802154__attr__value.md#a75913597f93de1a80f96bb9dc32d38df)

uint32\_t phy\_supported\_channel\_pages

A bit field that represents the supported channel pages, see ieee802154\_phy\_channel\_page.

**Definition** ieee802154\_radio.h:1349

[ieee802154\_attr\_value::phy\_supported\_channels](structieee802154__attr__value.md#a840d2f3a2502f87806ef79c6926f73f0)

const struct ieee802154\_phy\_supported\_channels \* phy\_supported\_channels

Pointer to a structure representing channel ranges currently available on the selected channel page.

**Definition** ieee802154\_radio.h:1386

[ieee802154\_attr\_value::phy\_hrp\_uwb\_supported\_nominal\_prfs](structieee802154__attr__value.md#af157805fb8acffb634cba4b37472bdb3)

uint32\_t phy\_hrp\_uwb\_supported\_nominal\_prfs

A bit field representing supported HRP UWB pulse repetition frequencies (PRF), see enum ieee802154\_ph...

**Definition** ieee802154\_radio.h:1402

[ieee802154\_config](structieee802154__config.md)

IEEE 802.15.4 driver configuration data.

**Definition** ieee802154\_radio.h:1140

[ieee802154\_config::ext\_addr](structieee802154__config.md#a03d6ec1a371312961f3a1ee42e113bbf)

const uint8\_t \* ext\_addr

Filters the devices that will receive this IE by extended address.

**Definition** ieee802154\_radio.h:1254

[ieee802154\_config::pan\_coordinator](structieee802154__config.md#a078ec577af3d170781ed770c80c54b72)

bool pan\_coordinator

see IEEE802154\_CONFIG\_PAN\_COORDINATOR

**Definition** ieee802154\_radio.h:1157

[ieee802154\_config::event\_handler](structieee802154__config.md#a1558e71a1d5ab74990964ff4deabbdb7)

ieee802154\_event\_cb\_t event\_handler

see IEEE802154\_CONFIG\_EVENT\_HANDLER

**Definition** ieee802154\_radio.h:1166

[ieee802154\_config::frame\_counter](structieee802154__config.md#a272cfd864c7d47c6f06f26871ce07fb6)

uint32\_t frame\_counter

see IEEE802154\_CONFIG\_FRAME\_COUNTER

**Definition** ieee802154\_radio.h:1185

[ieee802154\_config::ack\_ie](structieee802154__config.md#a39c06e32cb4a74b4d8a9864f714e8c93)

struct ieee802154\_config::@110307323070236071131232105145036043000055221302::@005301360373345054306047221374265242072206100157 ack\_ie

see IEEE802154\_CONFIG\_ENH\_ACK\_HEADER\_IE

[ieee802154\_config::ack\_fpb](structieee802154__config.md#a3a5e597e53bfcc9e3bed8bac2edb74d2)

struct ieee802154\_config::@110307323070236071131232105145036043000055221302::@117015150333345107057234147304240206273333351324 ack\_fpb

see IEEE802154\_CONFIG\_ACK\_FPB

[ieee802154\_config::csl\_period](structieee802154__config.md#a5106a759148ec20c6c6c83a2581c9e88)

uint32\_t csl\_period

see IEEE802154\_CONFIG\_CSL\_PERIOD

**Definition** ieee802154\_radio.h:1225

[ieee802154\_config::header\_ie](structieee802154__config.md#a5343dec0de835943c0bef2c2d603a91d)

struct ieee802154\_header\_ie \* header\_ie

Pointer to the header IE, see section 7.4.2.1, figure 7-21.

**Definition** ieee802154\_radio.h:1243

[ieee802154\_config::extended](structieee802154__config.md#a55823097d62a69d0c92dc70fb4ff1dd5)

bool extended

Is extended address.

**Definition** ieee802154\_radio.h:1152

[ieee802154\_config::addr](structieee802154__config.md#a673f5cceb6439bc1c3527c62062151d1)

uint8\_t \* addr

little endian for both short and extended address

**Definition** ieee802154\_radio.h:1151

[ieee802154\_config::expected\_rx\_time](structieee802154__config.md#a8124aed4a4af36c0e21fd8f1b1c97e3e)

net\_time\_t expected\_rx\_time

see IEEE802154\_CONFIG\_EXPECTED\_RX\_TIME

**Definition** ieee802154\_radio.h:1230

[ieee802154\_config::start](structieee802154__config.md#a86b72101b0b21622f3cc8a2b3877e356)

net\_time\_t start

Nanosecond resolution timestamp relative to the network subsystem's local clock defining the start of...

**Definition** ieee802154\_radio.h:1200

[ieee802154\_config::purge\_ie](structieee802154__config.md#a8971a91be8748bd45027fcb730b99639)

bool purge\_ie

Flag for purging enh ACK header IEs.

**Definition** ieee802154\_radio.h:1274

[ieee802154\_config::rx\_on\_when\_idle](structieee802154__config.md#a8b7d4804cd051d69f3602f35cb4a8630)

bool rx\_on\_when\_idle

see IEEE802154\_CONFIG\_RX\_ON\_WHEN\_IDLE

**Definition** ieee802154\_radio.h:1163

[ieee802154\_config::channel](structieee802154__config.md#a8f7efaa743e070479632d139f0fc57c0)

uint8\_t channel

Used channel.

**Definition** ieee802154\_radio.h:1217

[ieee802154\_config::mac\_keys](structieee802154__config.md#a942c0d4fb244c7256530536dc132a727)

struct ieee802154\_key \* mac\_keys

see IEEE802154\_CONFIG\_MAC\_KEYS

**Definition** ieee802154\_radio.h:1182

[ieee802154\_config::short\_addr](structieee802154__config.md#aa27066dd9e54dab6795332b7413670f5)

uint16\_t short\_addr

Filters the devices that will receive this IE by short address.

**Definition** ieee802154\_radio.h:1265

[ieee802154\_config::rx\_slot](structieee802154__config.md#aadc2714bf31484cce071e9ef7b9a4007)

struct ieee802154\_config::@110307323070236071131232105145036043000055221302::@231214146026334237075020313153116027155117003216 rx\_slot

see IEEE802154\_CONFIG\_RX\_SLOT

[ieee802154\_config::promiscuous](structieee802154__config.md#aafb11c4130ff39e5c40dfe5d32c0d4e7)

bool promiscuous

see IEEE802154\_CONFIG\_PROMISCUOUS

**Definition** ieee802154\_radio.h:1160

[ieee802154\_config::auto\_ack\_fpb](structieee802154__config.md#ab27a654a0d53f268199e95dc21e18fd4)

struct ieee802154\_config::@110307323070236071131232105145036043000055221302::@157332356170373250105215351305040236107225232072 auto\_ack\_fpb

see IEEE802154\_CONFIG\_AUTO\_ACK\_FPB

[ieee802154\_config::duration](structieee802154__config.md#ab36833b4311b03f08f67290f4edd8e41)

net\_time\_t duration

Nanosecond resolution duration of the RX window relative to the above RX window start time during whi...

**Definition** ieee802154\_radio.h:1212

[ieee802154\_config::mode](structieee802154__config.md#ad139acde94327d4b8ceb76760751521d)

enum ieee802154\_fpb\_mode mode

Auto ACK FPB mode.

**Definition** ieee802154\_radio.h:1146

[ieee802154\_config::enabled](structieee802154__config.md#ad9361f9ba1652e46d0be25e0de39afdf)

bool enabled

Is auto ACK FPB enabled.

**Definition** ieee802154\_radio.h:1145

[ieee802154\_filter](structieee802154__filter.md)

Filter value, see ieee802154\_radio\_api::filter.

**Definition** ieee802154\_radio.h:594

[ieee802154\_filter::short\_addr](structieee802154__filter.md#a16a1779ff43accda31bba35b9bdd61c3)

uint16\_t short\_addr

Short address, in CPU byte order.

**Definition** ieee802154\_radio.h:599

[ieee802154\_filter::pan\_id](structieee802154__filter.md#a40f77239924af29d40f7595e23475e9b)

uint16\_t pan\_id

PAN ID, in CPU byte order.

**Definition** ieee802154\_radio.h:601

[ieee802154\_filter::ieee\_addr](structieee802154__filter.md#a636ec85ca79b2880de51ed93f6788909)

uint8\_t \* ieee\_addr

Extended address, in little endian.

**Definition** ieee802154\_radio.h:597

[ieee802154\_key](structieee802154__key.md)

Key configuration for transmit security offloading, see IEEE802154\_CONFIG\_MAC\_KEYS.

**Definition** ieee802154\_radio.h:609

[ieee802154\_key::key\_value](structieee802154__key.md#a01b760f3e622ad0a60888170e5688b9d)

uint8\_t \* key\_value

Key material.

**Definition** ieee802154\_radio.h:611

[ieee802154\_key::key\_frame\_counter](structieee802154__key.md#a357419c2d16a527a2417f4eded566aac)

uint32\_t key\_frame\_counter

Initial value of frame counter associated with the key, see section 9.4.3.

**Definition** ieee802154\_radio.h:613

[ieee802154\_key::frame\_counter\_per\_key](structieee802154__key.md#a5ca5258422db14b99fd37e7126cfc85d)

bool frame\_counter\_per\_key

Indicates if per-key frame counter should be used, see section 9.4.3.

**Definition** ieee802154\_radio.h:615

[ieee802154\_key::key\_id\_mode](structieee802154__key.md#a732a2a89e74139bd1d8e9b358c0306c7)

uint8\_t key\_id\_mode

Key Identifier Mode, see section 9.4.2.3, Table 9-7.

**Definition** ieee802154\_radio.h:617

[ieee802154\_key::key\_id](structieee802154__key.md#ae0a1e354b5718e8135fb6198ea12276a)

uint8\_t \* key\_id

Key Identifier, see section 9.4.4.

**Definition** ieee802154\_radio.h:619

[ieee802154\_phy\_channel\_range](structieee802154__phy__channel__range.md)

Represents a supported channel range, see ieee802154\_phy\_supported\_channels.

**Definition** ieee802154\_radio.h:235

[ieee802154\_phy\_channel\_range::to\_channel](structieee802154__phy__channel__range.md#a78af593807753dbfcfce88166f4c1f58)

uint16\_t to\_channel

To channel range.

**Definition** ieee802154\_radio.h:237

[ieee802154\_phy\_channel\_range::from\_channel](structieee802154__phy__channel__range.md#aec90e36227a7d9cc1dfc18231341dd03)

uint16\_t from\_channel

From channel range.

**Definition** ieee802154\_radio.h:236

[ieee802154\_phy\_supported\_channels](structieee802154__phy__supported__channels.md)

Represents a list channels supported by a driver for a given interface, see IEEE802154\_ATTR\_PHY\_SUPPO...

**Definition** ieee802154\_radio.h:244

[ieee802154\_phy\_supported\_channels::ranges](structieee802154__phy__supported__channels.md#a73ccabf887b567a0ce3ddc5f8a3eeed1)

const struct ieee802154\_phy\_channel\_range \*const ranges

Pointer to an array of channel range structures.

**Definition** ieee802154\_radio.h:251

[ieee802154\_phy\_supported\_channels::num\_ranges](structieee802154__phy__supported__channels.md#a8fb56a7fc6be96035cf4b51891582da9)

const uint8\_t num\_ranges

The number of currently available channel ranges.

**Definition** ieee802154\_radio.h:254

[ieee802154\_radio\_api](structieee802154__radio__api.md)

IEEE 802.15.4 driver interface API.

**Definition** ieee802154\_radio.h:1515

[ieee802154\_radio\_api::ed\_scan](structieee802154__radio__api.md#a01fc17f85f2be33877a9347f59a84c54)

int(\* ed\_scan)(const struct device \*dev, uint16\_t duration, energy\_scan\_done\_cb\_t done\_cb)

Run an energy detection scan.

**Definition** ieee802154\_radio.h:1852

[ieee802154\_radio\_api::get\_capabilities](structieee802154__radio__api.md#a09a4b5df81822845f718952c6029442c)

enum ieee802154\_hw\_caps(\* get\_capabilities)(const struct device \*dev)

Get the device driver capabilities.

**Definition** ieee802154\_radio.h:1536

[ieee802154\_radio\_api::attr\_get](structieee802154__radio__api.md#a0b3e0ed1385dd428c861e08c79849ef4)

int(\* attr\_get)(const struct device \*dev, enum ieee802154\_attr attr, struct ieee802154\_attr\_value \*value)

Get the value of a driver specific attribute.

**Definition** ieee802154\_radio.h:1918

[ieee802154\_radio\_api::start](structieee802154__radio__api.md#a0e4d57dc3a53299ddedf2140e172103d)

int(\* start)(const struct device \*dev)

Start the device.

**Definition** ieee802154\_radio.h:1742

[ieee802154\_radio\_api::cca](structieee802154__radio__api.md#a2cbbd0e64fae28f748bb3e4d654a92bf)

int(\* cca)(const struct device \*dev)

Clear Channel Assessment - Check channel's activity.

**Definition** ieee802154\_radio.h:1554

[ieee802154\_radio\_api::continuous\_carrier](structieee802154__radio__api.md#a5b9b45e274fd6a8777cd96280b1a1b9e)

int(\* continuous\_carrier)(const struct device \*dev)

Start continuous carrier wave transmission.

**Definition** ieee802154\_radio.h:1787

[ieee802154\_radio\_api::tx](structieee802154__radio__api.md#a70139acec22642c1fc09f2323c383fe6)

int(\* tx)(const struct device \*dev, enum ieee802154\_tx\_mode mode, struct net\_pkt \*pkt, struct net\_buf \*frag)

Transmit a packet fragment as a single frame.

**Definition** ieee802154\_radio.h:1718

[ieee802154\_radio\_api::stop](structieee802154__radio__api.md#a75cfcfe2b9e69c2e4af53f00c8294b36)

int(\* stop)(const struct device \*dev)

Stop the device.

**Definition** ieee802154\_radio.h:1766

[ieee802154\_radio\_api::get\_time](structieee802154__radio__api.md#a829a0d59fdcda5b6cb029ef1334a6b8b)

net\_time\_t(\* get\_time)(const struct device \*dev)

Get the current time in nanoseconds relative to the network subsystem's local uptime clock as represe...

**Definition** ieee802154\_radio.h:1873

[ieee802154\_radio\_api::configure](structieee802154__radio__api.md#a9acaf4810bd5d3b026cc381bff301071)

int(\* configure)(const struct device \*dev, enum ieee802154\_config\_type type, const struct ieee802154\_config \*config)

Set or update driver configuration.

**Definition** ieee802154\_radio.h:1824

[ieee802154\_radio\_api::set\_channel](structieee802154__radio__api.md#a9ad27a2ff0a839dc5b9a4e6317cc59b1)

int(\* set\_channel)(const struct device \*dev, uint16\_t channel)

Set current channel.

**Definition** ieee802154\_radio.h:1578

[ieee802154\_radio\_api::filter](structieee802154__radio__api.md#aa9502e0e014a8d05ffe235567e8c98f3)

int(\* filter)(const struct device \*dev, bool set, enum ieee802154\_filter\_type type, const struct ieee802154\_filter \*filter)

Set/Unset PAN ID, extended or short address filters.

**Definition** ieee802154\_radio.h:1603

[ieee802154\_radio\_api::iface\_api](structieee802154__radio__api.md#aa955462d8c6950dc4b5935973f4575d8)

struct net\_if\_api iface\_api

network interface API

**Definition** ieee802154\_radio.h:1523

[ieee802154\_radio\_api::get\_sch\_acc](structieee802154__radio__api.md#ae4a3ef40a5b8031c868d72ead163c97d)

uint8\_t(\* get\_sch\_acc)(const struct device \*dev)

Get the current estimated worst case accuracy (maximum ± deviation from the nominal frequency) of the...

**Definition** ieee802154\_radio.h:1895

[ieee802154\_radio\_api::set\_txpower](structieee802154__radio__api.md#aeeab6dfcde08af23357ea40f8af68f66)

int(\* set\_txpower)(const struct device \*dev, int16\_t dbm)

Set TX power level in dbm.

**Definition** ieee802154\_radio.h:1624

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

[net\_buf::data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56)

uint8\_t \* data

Pointer to the start of data in the buffer.

**Definition** net\_buf.h:1032

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:680

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:91

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ieee802154\_radio.h](ieee802154__radio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

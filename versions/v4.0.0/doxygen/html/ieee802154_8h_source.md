---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ieee802154_8h_source.html
original_path: doxygen/html/ieee802154_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ieee802154.h

[Go to the documentation of this file.](ieee802154_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_NET\_IEEE802154\_H\_

15#define ZEPHYR\_INCLUDE\_NET\_IEEE802154\_H\_

16

17#include <[limits.h](limits_8h.md)>

18#include <[zephyr/net/net\_l2.h](net__l2_8h.md)>

19#include <[zephyr/net/net\_mgmt.h](net__mgmt_8h.md)>

20#include <[zephyr/crypto/cipher.h](cipher_8h.md)>

21#include <[zephyr/net/ieee802154\_radio.h](ieee802154__radio_8h.md)>

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

78

103

[ 111](group__ieee802154__l2.md#gac63b5ae7ed99b168871b5fc08ecde7a1)#define IEEE802154\_MAX\_PHY\_PACKET\_SIZE 127

112

[ 120](group__ieee802154__l2.md#ga1243000b59167777e078060fd3c1c218)#define IEEE802154\_FCS\_LENGTH 2

121

[ 136](group__ieee802154__l2.md#ga987d42d1d8117ec58cf3f9cae4e66139)#define IEEE802154\_MTU (IEEE802154\_MAX\_PHY\_PACKET\_SIZE - IEEE802154\_FCS\_LENGTH)

137

138/\* TODO: Support flexible MTU and FCS lengths for IEEE 802.15.4-2015ff \*/

139

[ 141](group__ieee802154__l2.md#gaee7ec8e4ba396f3cd658bcb22a9352e8)#define IEEE802154\_SHORT\_ADDR\_LENGTH 2

142

[ 144](group__ieee802154__l2.md#ga355350794ec26788bc855da53d311bea)#define IEEE802154\_EXT\_ADDR\_LENGTH 8

145

[ 147](group__ieee802154__l2.md#gae405ed23baf91fa3d96c81d5121faa1a)#define IEEE802154\_MAX\_ADDR\_LENGTH IEEE802154\_EXT\_ADDR\_LENGTH

148

[ 153](group__ieee802154__l2.md#ga692a16d957c1e1ce76808cda325fd6c5)#define IEEE802154\_NO\_CHANNEL USHRT\_MAX

154

[ 159](group__ieee802154__l2.md#gafae1906dc9b39c93690b127efaaacacb)#define IEEE802154\_BROADCAST\_ADDRESS 0xffff

160

[ 166](group__ieee802154__l2.md#ga43369b4a9ea0961395cd135b9fe18d03)#define IEEE802154\_NO\_SHORT\_ADDRESS\_ASSIGNED 0xfffe

167

[ 169](group__ieee802154__l2.md#ga1a40fed9dcd802af0283d7808e8b283b)#define IEEE802154\_BROADCAST\_PAN\_ID 0xffff

170

[ 175](group__ieee802154__l2.md#gaf6718b4e9873d9b2e6786103ebcea1bc)#define IEEE802154\_SHORT\_ADDRESS\_NOT\_ASSOCIATED IEEE802154\_BROADCAST\_ADDRESS

176

[ 181](group__ieee802154__l2.md#ga89cc35f42374255c986bcd23f15bfc14)#define IEEE802154\_PAN\_ID\_NOT\_ASSOCIATED IEEE802154\_BROADCAST\_PAN\_ID

182

[ 184](structieee802154__security__ctx.md)struct [ieee802154\_security\_ctx](structieee802154__security__ctx.md) {

[ 192](structieee802154__security__ctx.md#adc4ce1ddf15b8b0bc4f283747b858b02) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [frame\_counter](structieee802154__security__ctx.md#adc4ce1ddf15b8b0bc4f283747b858b02);

193

195 struct [cipher\_ctx](structcipher__ctx.md) enc;

196 struct [cipher\_ctx](structcipher__ctx.md) dec;

198

[ 210](structieee802154__security__ctx.md#a3478b9a5430e12ca2c5641e1417a43d4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key](structieee802154__security__ctx.md#a3478b9a5430e12ca2c5641e1417a43d4)[16];

211

[ 213](structieee802154__security__ctx.md#a1665374abce017c4b60e5c2085b19d8f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key\_len](structieee802154__security__ctx.md#a1665374abce017c4b60e5c2085b19d8f);

214

[ 225](structieee802154__security__ctx.md#a65d1ca01bf7ed917a008591c8be0ca19) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [level](structieee802154__security__ctx.md#a65d1ca01bf7ed917a008591c8be0ca19) : 3;

226

[ 237](structieee802154__security__ctx.md#afc41da04241f4fcc11e9d9f7728315d9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key\_mode](structieee802154__security__ctx.md#afc41da04241f4fcc11e9d9f7728315d9) : 2;

238

240 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_unused : 3;

242};

243

[ 245](group__ieee802154__l2.md#ga7a4fb2d89381bba54514bf8396fb6d26)enum [ieee802154\_device\_role](group__ieee802154__l2.md#ga7a4fb2d89381bba54514bf8396fb6d26) {

[ 246](group__ieee802154__l2.md#gga7a4fb2d89381bba54514bf8396fb6d26a9909ce934f56e6b5b6c1bc53345a65b5) [IEEE802154\_DEVICE\_ROLE\_ENDDEVICE](group__ieee802154__l2.md#gga7a4fb2d89381bba54514bf8396fb6d26a9909ce934f56e6b5b6c1bc53345a65b5),

[ 247](group__ieee802154__l2.md#gga7a4fb2d89381bba54514bf8396fb6d26abc23f55210c7ff0747bddc9c679b4f68) [IEEE802154\_DEVICE\_ROLE\_COORDINATOR](group__ieee802154__l2.md#gga7a4fb2d89381bba54514bf8396fb6d26abc23f55210c7ff0747bddc9c679b4f68),

[ 248](group__ieee802154__l2.md#gga7a4fb2d89381bba54514bf8396fb6d26a2b25d9e19f374d3f3ef6329bdf942340) [IEEE802154\_DEVICE\_ROLE\_PAN\_COORDINATOR](group__ieee802154__l2.md#gga7a4fb2d89381bba54514bf8396fb6d26a2b25d9e19f374d3f3ef6329bdf942340),

249};

250

[ 252](structieee802154__context.md)struct [ieee802154\_context](structieee802154__context.md) {

[ 262](structieee802154__context.md#ae3c9b2de2e55d619f2d8acf5cf8b7491) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pan\_id](structieee802154__context.md#ae3c9b2de2e55d619f2d8acf5cf8b7491);

263

[ 273](structieee802154__context.md#ad02d219198201aee98ab1ab1793cfe6b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [channel](structieee802154__context.md#ad02d219198201aee98ab1ab1793cfe6b);

274

[ 286](structieee802154__context.md#a64e992804fcd463ff437ac88c296dfab) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [short\_addr](structieee802154__context.md#a64e992804fcd463ff437ac88c296dfab);

287

[ 296](structieee802154__context.md#a3dbbea6bef660e17b3bbf7c02a4672cc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ext\_addr](structieee802154__context.md#a3dbbea6bef660e17b3bbf7c02a4672cc)[[IEEE802154\_MAX\_ADDR\_LENGTH](group__ieee802154__l2.md#gae405ed23baf91fa3d96c81d5121faa1a)];

297

[ 299](structieee802154__context.md#a77b6b4d41835dc2ee0f28a4109136733) struct [net\_linkaddr\_storage](structnet__linkaddr__storage.md) [linkaddr](structieee802154__context.md#a77b6b4d41835dc2ee0f28a4109136733);

300

301#ifdef CONFIG\_NET\_L2\_IEEE802154\_SECURITY

[ 303](structieee802154__context.md#a0a4cc252326f86af4d142d32950d2af6) struct [ieee802154\_security\_ctx](structieee802154__security__ctx.md) [sec\_ctx](structieee802154__context.md#a0a4cc252326f86af4d142d32950d2af6);

304#endif

305

306#ifdef CONFIG\_NET\_L2\_IEEE802154\_MGMT

[ 308](structieee802154__context.md#a06de84ddc495a80777b87f8934da94e5) struct [ieee802154\_req\_params](structieee802154__req__params.md) \*[scan\_ctx](structieee802154__context.md#a06de84ddc495a80777b87f8934da94e5);

309

[ 314](structieee802154__context.md#a35bfac224aff80f256853cb0d8ce8466) struct k\_sem [scan\_ctx\_lock](structieee802154__context.md#a35bfac224aff80f256853cb0d8ce8466);

315

[ 328](structieee802154__context.md#a84053e172fbfd9d59c4d8e7a1b98d5b6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [coord\_ext\_addr](structieee802154__context.md#a84053e172fbfd9d59c4d8e7a1b98d5b6)[[IEEE802154\_MAX\_ADDR\_LENGTH](group__ieee802154__l2.md#gae405ed23baf91fa3d96c81d5121faa1a)];

329

[ 343](structieee802154__context.md#abf1cc83c3a4880513137e7e4955174c1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [coord\_short\_addr](structieee802154__context.md#abf1cc83c3a4880513137e7e4955174c1);

344#endif

345

[ 347](structieee802154__context.md#a800a07927c4faec1dca2910a65c1baae) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [tx\_power](structieee802154__context.md#a800a07927c4faec1dca2910a65c1baae);

348

[ 350](structieee802154__context.md#acf1fcafe106362eba112ea946a575bbd) enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) [flags](structieee802154__context.md#acf1fcafe106362eba112ea946a575bbd);

351

[ 358](structieee802154__context.md#a5618dec853ce41bbfa48e2aaa3f73262) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sequence](structieee802154__context.md#a5618dec853ce41bbfa48e2aaa3f73262);

359

[ 372](structieee802154__context.md#a70b2a2936aca60a5bc4fc2b98aa11497) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [device\_role](structieee802154__context.md#a70b2a2936aca60a5bc4fc2b98aa11497) : 2;

373

375 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_unused : 5;

377

[ 381](structieee802154__context.md#a511059cb95c0d52c907464a1891586aa) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ack\_requested](structieee802154__context.md#a511059cb95c0d52c907464a1891586aa): 1;

382

[ 384](structieee802154__context.md#a0eeefef60bc7c266b2bb26893404ff86) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ack\_seq](structieee802154__context.md#a0eeefef60bc7c266b2bb26893404ff86);

385

[ 387](structieee802154__context.md#a641c70a792f47431be8a0ffe2635a11f) struct k\_sem [ack\_lock](structieee802154__context.md#a641c70a792f47431be8a0ffe2635a11f);

388

[ 395](structieee802154__context.md#a462527426b11b80ee53a3f91aacf1e1e) struct k\_sem [ctx\_lock](structieee802154__context.md#a462527426b11b80ee53a3f91aacf1e1e);

396};

397

399

400/\* L2 context type to be used with NET\_L2\_GET\_CTX\_TYPE \*/

401#define IEEE802154\_L2\_CTX\_TYPE struct ieee802154\_context

402

404

405#ifdef \_\_cplusplus

406}

407#endif

408

412

413#endif /\* ZEPHYR\_INCLUDE\_NET\_IEEE802154\_H\_ \*/

[cipher.h](cipher_8h.md)

Crypto Cipher structure definitions.

[ieee802154\_device\_role](group__ieee802154__l2.md#ga7a4fb2d89381bba54514bf8396fb6d26)

ieee802154\_device\_role

IEEE 802.15.4 device role.

**Definition** ieee802154.h:245

[IEEE802154\_MAX\_ADDR\_LENGTH](group__ieee802154__l2.md#gae405ed23baf91fa3d96c81d5121faa1a)

#define IEEE802154\_MAX\_ADDR\_LENGTH

IEEE 802.15.4 maximum address length.

**Definition** ieee802154.h:147

[IEEE802154\_DEVICE\_ROLE\_PAN\_COORDINATOR](group__ieee802154__l2.md#gga7a4fb2d89381bba54514bf8396fb6d26a2b25d9e19f374d3f3ef6329bdf942340)

@ IEEE802154\_DEVICE\_ROLE\_PAN\_COORDINATOR

PAN coordinator.

**Definition** ieee802154.h:248

[IEEE802154\_DEVICE\_ROLE\_ENDDEVICE](group__ieee802154__l2.md#gga7a4fb2d89381bba54514bf8396fb6d26a9909ce934f56e6b5b6c1bc53345a65b5)

@ IEEE802154\_DEVICE\_ROLE\_ENDDEVICE

End device.

**Definition** ieee802154.h:246

[IEEE802154\_DEVICE\_ROLE\_COORDINATOR](group__ieee802154__l2.md#gga7a4fb2d89381bba54514bf8396fb6d26abc23f55210c7ff0747bddc9c679b4f68)

@ IEEE802154\_DEVICE\_ROLE\_COORDINATOR

Coordinator.

**Definition** ieee802154.h:247

[net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516)

net\_l2\_flags

L2 flags.

**Definition** net\_l2.h:36

[ieee802154\_radio.h](ieee802154__radio_8h.md)

Public IEEE 802.15.4 Driver API.

[limits.h](limits_8h.md)

[net\_l2.h](net__l2_8h.md)

Public API for network L2 interface.

[net\_mgmt.h](net__mgmt_8h.md)

Network Management API public header.

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

[cipher\_ctx](structcipher__ctx.md)

Structure encoding session parameters.

**Definition** cipher.h:110

[ieee802154\_context](structieee802154__context.md)

IEEE 802.15.4 L2 context.

**Definition** ieee802154.h:252

[ieee802154\_context::scan\_ctx](structieee802154__context.md#a06de84ddc495a80777b87f8934da94e5)

struct ieee802154\_req\_params \* scan\_ctx

Pointer to scanning parameters and results, guarded by scan\_ctx\_lock.

**Definition** ieee802154.h:308

[ieee802154\_context::sec\_ctx](structieee802154__context.md#a0a4cc252326f86af4d142d32950d2af6)

struct ieee802154\_security\_ctx sec\_ctx

Security context.

**Definition** ieee802154.h:303

[ieee802154\_context::ack\_seq](structieee802154__context.md#a0eeefef60bc7c266b2bb26893404ff86)

uint8\_t ack\_seq

ACK expected sequence number, guarded by ack\_lock.

**Definition** ieee802154.h:384

[ieee802154\_context::scan\_ctx\_lock](structieee802154__context.md#a35bfac224aff80f256853cb0d8ce8466)

struct k\_sem scan\_ctx\_lock

Used to maintain integrity of data for all fields in this struct unless otherwise documented on field...

**Definition** ieee802154.h:314

[ieee802154\_context::ext\_addr](structieee802154__context.md#a3dbbea6bef660e17b3bbf7c02a4672cc)

uint8\_t ext\_addr[8]

Extended Address (in little endian).

**Definition** ieee802154.h:296

[ieee802154\_context::ctx\_lock](structieee802154__context.md#a462527426b11b80ee53a3f91aacf1e1e)

struct k\_sem ctx\_lock

Context lock.

**Definition** ieee802154.h:395

[ieee802154\_context::ack\_requested](structieee802154__context.md#a511059cb95c0d52c907464a1891586aa)

uint8\_t ack\_requested

ACK requested flag, guarded by ack\_lock.

**Definition** ieee802154.h:381

[ieee802154\_context::sequence](structieee802154__context.md#a5618dec853ce41bbfa48e2aaa3f73262)

uint8\_t sequence

Data sequence number.

**Definition** ieee802154.h:358

[ieee802154\_context::ack\_lock](structieee802154__context.md#a641c70a792f47431be8a0ffe2635a11f)

struct k\_sem ack\_lock

ACK lock, guards ack\_\* fields.

**Definition** ieee802154.h:387

[ieee802154\_context::short\_addr](structieee802154__context.md#a64e992804fcd463ff437ac88c296dfab)

uint16\_t short\_addr

Short Address (in CPU byte order).

**Definition** ieee802154.h:286

[ieee802154\_context::device\_role](structieee802154__context.md#a70b2a2936aca60a5bc4fc2b98aa11497)

uint8\_t device\_role

Device Role.

**Definition** ieee802154.h:372

[ieee802154\_context::linkaddr](structieee802154__context.md#a77b6b4d41835dc2ee0f28a4109136733)

struct net\_linkaddr\_storage linkaddr

Link layer address (in big endian).

**Definition** ieee802154.h:299

[ieee802154\_context::tx\_power](structieee802154__context.md#a800a07927c4faec1dca2910a65c1baae)

int16\_t tx\_power

Transmission power in dBm.

**Definition** ieee802154.h:347

[ieee802154\_context::coord\_ext\_addr](structieee802154__context.md#a84053e172fbfd9d59c4d8e7a1b98d5b6)

uint8\_t coord\_ext\_addr[8]

Coordinator extended address.

**Definition** ieee802154.h:328

[ieee802154\_context::coord\_short\_addr](structieee802154__context.md#abf1cc83c3a4880513137e7e4955174c1)

uint16\_t coord\_short\_addr

Coordinator short address.

**Definition** ieee802154.h:343

[ieee802154\_context::flags](structieee802154__context.md#acf1fcafe106362eba112ea946a575bbd)

enum net\_l2\_flags flags

L2 flags.

**Definition** ieee802154.h:350

[ieee802154\_context::channel](structieee802154__context.md#ad02d219198201aee98ab1ab1793cfe6b)

uint16\_t channel

Channel Number.

**Definition** ieee802154.h:273

[ieee802154\_context::pan\_id](structieee802154__context.md#ae3c9b2de2e55d619f2d8acf5cf8b7491)

uint16\_t pan\_id

PAN ID.

**Definition** ieee802154.h:262

[ieee802154\_req\_params](structieee802154__req__params.md)

Scanning parameters.

**Definition** ieee802154\_mgmt.h:311

[ieee802154\_security\_ctx](structieee802154__security__ctx.md)

Interface-level security attributes, see section 9.5.

**Definition** ieee802154.h:184

[ieee802154\_security\_ctx::key\_len](structieee802154__security__ctx.md#a1665374abce017c4b60e5c2085b19d8f)

uint8\_t key\_len

Length in bytes of the interface-level security key material.

**Definition** ieee802154.h:213

[ieee802154\_security\_ctx::key](structieee802154__security__ctx.md#a3478b9a5430e12ca2c5641e1417a43d4)

uint8\_t key[16]

Interface-level frame encryption security key material.

**Definition** ieee802154.h:210

[ieee802154\_security\_ctx::level](structieee802154__security__ctx.md#a65d1ca01bf7ed917a008591c8be0ca19)

uint8\_t level

Frame security level, possible values are defined in section 9.4.2.2, table 9-6.

**Definition** ieee802154.h:225

[ieee802154\_security\_ctx::frame\_counter](structieee802154__security__ctx.md#adc4ce1ddf15b8b0bc4f283747b858b02)

uint32\_t frame\_counter

Interface-level outgoing frame counter, section 9.5, table 9-8, secFrameCounter.

**Definition** ieee802154.h:192

[ieee802154\_security\_ctx::key\_mode](structieee802154__security__ctx.md#afc41da04241f4fcc11e9d9f7728315d9)

uint8\_t key\_mode

Frame security key mode.

**Definition** ieee802154.h:237

[net\_linkaddr\_storage](structnet__linkaddr__storage.md)

Hardware link address structure.

**Definition** net\_linkaddr.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ieee802154.h](ieee802154_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

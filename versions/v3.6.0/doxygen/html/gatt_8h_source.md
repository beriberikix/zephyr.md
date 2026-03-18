---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/gatt_8h_source.html
original_path: doxygen/html/gatt_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gatt.h

[Go to the documentation of this file.](gatt_8h.md)

1

4

5/\*

6 \* Copyright (c) 2015-2016 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_GATT\_H\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_GATT\_H\_

12

19

20#include <[stdint.h](stdint_8h.md)>

21#include <stddef.h>

22

23#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

24

25#include <[zephyr/sys/slist.h](slist_8h.md)>

26#include <[zephyr/sys/util.h](util_8h.md)>

27#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

28#include <[zephyr/bluetooth/uuid.h](uuid_8h.md)>

29#include <[zephyr/bluetooth/att.h](att_8h.md)>

30#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

31

32#ifdef \_\_cplusplus

33extern "C" {

34#endif

35

[ 37](group__bt__gatt.md#ga96e57500d2340a45badb23701cc43833)enum [bt\_gatt\_perm](group__bt__gatt.md#ga96e57500d2340a45badb23701cc43833) {

[ 39](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a81a1c35d981593c4c0d344dd0f7e898a) [BT\_GATT\_PERM\_NONE](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a81a1c35d981593c4c0d344dd0f7e898a) = 0,

40

[ 42](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a9afb838c2cef657e9cd035ef27521f17) [BT\_GATT\_PERM\_READ](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a9afb838c2cef657e9cd035ef27521f17) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

43

[ 45](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a0f611698ca511f565b247a813ea016cf) [BT\_GATT\_PERM\_WRITE](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a0f611698ca511f565b247a813ea016cf) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

46

[ 51](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a0d0afe4a6389102f85e355468cb7984d) [BT\_GATT\_PERM\_READ\_ENCRYPT](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a0d0afe4a6389102f85e355468cb7984d) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

52

[ 57](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a662b9af6f435d788aa4e6829725f670f) [BT\_GATT\_PERM\_WRITE\_ENCRYPT](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a662b9af6f435d788aa4e6829725f670f) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

58

[ 64](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833ad83f4c03608f674c00ebc93e63d08583) [BT\_GATT\_PERM\_READ\_AUTHEN](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833ad83f4c03608f674c00ebc93e63d08583) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

65

[ 71](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833add3893c94a788ff2e5256595a533a266) [BT\_GATT\_PERM\_WRITE\_AUTHEN](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833add3893c94a788ff2e5256595a533a266) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

72

[ 78](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833ab384b61f6ead9d140011da917c950d79) [BT\_GATT\_PERM\_PREPARE\_WRITE](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833ab384b61f6ead9d140011da917c950d79) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

79

[ 84](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833af62e397dfd87fe763b9c9fc1d5072f57) [BT\_GATT\_PERM\_READ\_LESC](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833af62e397dfd87fe763b9c9fc1d5072f57) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

85

[ 90](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833ac56183af896e2a58439c625420efca94) [BT\_GATT\_PERM\_WRITE\_LESC](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833ac56183af896e2a58439c625420efca94) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8),

91};

92

[ 100](group__bt__gatt.md#gaff31756c1bf8ee755e65b1e0fb689bb7)#define BT\_GATT\_ERR(\_att\_err) (-(\_att\_err))

101

103enum {

[ 109](group__bt__gatt.md#gga11c5a2eb0b62de9a2493ad5335fae383a019cf6118a0cfacbfad20c1cc5838383) [BT\_GATT\_WRITE\_FLAG\_PREPARE](group__bt__gatt.md#gga11c5a2eb0b62de9a2493ad5335fae383a019cf6118a0cfacbfad20c1cc5838383) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

110

[ 116](group__bt__gatt.md#gga11c5a2eb0b62de9a2493ad5335fae383a770df41b7d433e8ce349b19e4657ba78) [BT\_GATT\_WRITE\_FLAG\_CMD](group__bt__gatt.md#gga11c5a2eb0b62de9a2493ad5335fae383a770df41b7d433e8ce349b19e4657ba78) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

117

[ 124](group__bt__gatt.md#gga11c5a2eb0b62de9a2493ad5335fae383ad4e8f43c03da10c15685bd1a0109708b) [BT\_GATT\_WRITE\_FLAG\_EXECUTE](group__bt__gatt.md#gga11c5a2eb0b62de9a2493ad5335fae383ad4e8f43c03da10c15685bd1a0109708b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

125};

126

127/\* Forward declaration of GATT Attribute structure \*/

128struct [bt\_gatt\_attr](structbt__gatt__attr.md);

129

[ 145](group__bt__gatt.md#ga57e36bf94652531964fd4237c203fe7b)typedef [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[bt\_gatt\_attr\_read\_func\_t](group__bt__gatt.md#ga57e36bf94652531964fd4237c203fe7b))(struct bt\_conn \*conn,

146 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr,

147 void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len,

148 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset);

149

[ 163](group__bt__gatt.md#ga3fd8527a0f3e8f3699dc0d3b0339eba1)typedef [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[bt\_gatt\_attr\_write\_func\_t](group__bt__gatt.md#ga3fd8527a0f3e8f3699dc0d3b0339eba1))(struct bt\_conn \*conn,

164 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr,

165 const void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len,

166 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

167

[ 169](structbt__gatt__attr.md)struct [bt\_gatt\_attr](structbt__gatt__attr.md) {

[ 171](structbt__gatt__attr.md#a6958f507f9ff172018be458ebc86106f) const struct [bt\_uuid](structbt__uuid.md) \*[uuid](structbt__gatt__attr.md#a6958f507f9ff172018be458ebc86106f);

[ 172](structbt__gatt__attr.md#a074abc719494ca35997a452f526e7ecc) [bt\_gatt\_attr\_read\_func\_t](group__bt__gatt.md#ga57e36bf94652531964fd4237c203fe7b) [read](structbt__gatt__attr.md#a074abc719494ca35997a452f526e7ecc);

[ 174](structbt__gatt__attr.md#a1ecd78536067f4bded506e0daccefd35) [bt\_gatt\_attr\_write\_func\_t](group__bt__gatt.md#ga3fd8527a0f3e8f3699dc0d3b0339eba1) [write](structbt__gatt__attr.md#a1ecd78536067f4bded506e0daccefd35);

[ 176](structbt__gatt__attr.md#adeb063fb101fab45dd789c7212c43357) void \*[user\_data](structbt__gatt__attr.md#adeb063fb101fab45dd789c7212c43357);

[ 178](structbt__gatt__attr.md#aeee42a3d3ca15e40cf11cc0c3fde106b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__gatt__attr.md#aeee42a3d3ca15e40cf11cc0c3fde106b);

[ 183](structbt__gatt__attr.md#a0849a40254622080d05e8559c4fdb9e2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [perm](structbt__gatt__attr.md#a0849a40254622080d05e8559c4fdb9e2);

184};

185

[ 187](structbt__gatt__service__static.md)struct [bt\_gatt\_service\_static](structbt__gatt__service__static.md) {

[ 189](structbt__gatt__service__static.md#a38f9e02241fe37f68df5dd8782b59e9f) const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*[attrs](structbt__gatt__service__static.md#a38f9e02241fe37f68df5dd8782b59e9f);

[ 191](structbt__gatt__service__static.md#a84c35a391e372396e2ec89eaf0d4d047) size\_t [attr\_count](structbt__gatt__service__static.md#a84c35a391e372396e2ec89eaf0d4d047);

192};

193

[ 195](structbt__gatt__service.md)struct [bt\_gatt\_service](structbt__gatt__service.md) {

[ 197](structbt__gatt__service.md#a0281e96ab54519df641f6c489fdc6b5b) struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*[attrs](structbt__gatt__service.md#a0281e96ab54519df641f6c489fdc6b5b);

[ 199](structbt__gatt__service.md#a87d8316a92ae04678d7be0ae76ed86cb) size\_t [attr\_count](structbt__gatt__service.md#a87d8316a92ae04678d7be0ae76ed86cb);

200

[ 201](structbt__gatt__service.md#a8ce51bcd55e4f9a80a00bcac2c20b2d1) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structbt__gatt__service.md#a8ce51bcd55e4f9a80a00bcac2c20b2d1);

202};

203

[ 205](structbt__gatt__service__val.md)struct [bt\_gatt\_service\_val](structbt__gatt__service__val.md) {

[ 207](structbt__gatt__service__val.md#a683e01db92400e76aed32b7a81369a55) const struct [bt\_uuid](structbt__uuid.md) \*[uuid](structbt__gatt__service__val.md#a683e01db92400e76aed32b7a81369a55);

[ 209](structbt__gatt__service__val.md#a75b6fcf0f9f29ad05ccac0e83bcb31b7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [end\_handle](structbt__gatt__service__val.md#a75b6fcf0f9f29ad05ccac0e83bcb31b7);

210};

211

[ 213](structbt__gatt__include.md)struct [bt\_gatt\_include](structbt__gatt__include.md) {

[ 215](structbt__gatt__include.md#afa028e8daae00e3b1bc0b866c4335af3) const struct [bt\_uuid](structbt__uuid.md) \*[uuid](structbt__gatt__include.md#afa028e8daae00e3b1bc0b866c4335af3);

[ 217](structbt__gatt__include.md#ac7f6c1a8018f483dce14f0fe21031232) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [start\_handle](structbt__gatt__include.md#ac7f6c1a8018f483dce14f0fe21031232);

[ 219](structbt__gatt__include.md#a54d20cebfd6ba62b692c363acdc25d61) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [end\_handle](structbt__gatt__include.md#a54d20cebfd6ba62b692c363acdc25d61);

220};

221

[ 223](structbt__gatt__cb.md)struct [bt\_gatt\_cb](structbt__gatt__cb.md) {

[ 233](structbt__gatt__cb.md#a93fe1a626ab59c38ef56f02671f88980) void (\*[att\_mtu\_updated](structbt__gatt__cb.md#a93fe1a626ab59c38ef56f02671f88980))(struct bt\_conn \*conn, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) rx);

234

[ 235](structbt__gatt__cb.md#af9fcf17dcea66b1dee8cc5ecd625cdec) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structbt__gatt__cb.md#af9fcf17dcea66b1dee8cc5ecd625cdec);

236};

237

[ 239](structbt__gatt__authorization__cb.md)struct [bt\_gatt\_authorization\_cb](structbt__gatt__authorization__cb.md) {

[ 251](structbt__gatt__authorization__cb.md#a7b1bcbe10f12c90ee4e3214e36e9c2a3) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[read\_authorize](structbt__gatt__authorization__cb.md#a7b1bcbe10f12c90ee4e3214e36e9c2a3))(struct bt\_conn \*conn,

252 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr);

253

[ 265](structbt__gatt__authorization__cb.md#a7c12bd14f87f91e672eaaf92e1aa6e7b) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[write\_authorize](structbt__gatt__authorization__cb.md#a7c12bd14f87f91e672eaaf92e1aa6e7b))(struct bt\_conn \*conn,

266 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr);

267};

268

270

[ 277](group__bt__gatt.md#ga86bddd8211e7466b0457173a0dd412f0)#define BT\_GATT\_CHRC\_BROADCAST 0x01

[ 283](group__bt__gatt.md#gaa243a11d6d8b3e3be815c0893e0220f3)#define BT\_GATT\_CHRC\_READ 0x02

[ 289](group__bt__gatt.md#ga9c029ca574eb3c5992685b279388ac85)#define BT\_GATT\_CHRC\_WRITE\_WITHOUT\_RESP 0x04

[ 295](group__bt__gatt.md#gad482d8db34707e1f9da1d8e2ddd5507e)#define BT\_GATT\_CHRC\_WRITE 0x08

[ 302](group__bt__gatt.md#gab8cd9649bdfd125a26065a8ced762a98)#define BT\_GATT\_CHRC\_NOTIFY 0x10

[ 308](group__bt__gatt.md#gaa9639b9d655ea41767584b638add1f2b)#define BT\_GATT\_CHRC\_INDICATE 0x20

[ 314](group__bt__gatt.md#gaab3a26a00f88a6eacd36f2841004204c)#define BT\_GATT\_CHRC\_AUTH 0x40

[ 321](group__bt__gatt.md#gac84d73a0ad50bfd149ad83181315de1a)#define BT\_GATT\_CHRC\_EXT\_PROP 0x80

322

[ 324](structbt__gatt__chrc.md)struct [bt\_gatt\_chrc](structbt__gatt__chrc.md) {

[ 326](structbt__gatt__chrc.md#af3b4c22ae37b912c8edf58294cc50702) const struct [bt\_uuid](structbt__uuid.md) \*[uuid](structbt__gatt__chrc.md#af3b4c22ae37b912c8edf58294cc50702);

[ 328](structbt__gatt__chrc.md#a2ca6aec1a621fdfd12142a1188d37bd3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [value\_handle](structbt__gatt__chrc.md#a2ca6aec1a621fdfd12142a1188d37bd3);

[ 330](structbt__gatt__chrc.md#a81bb8257052d7c8d03b51acaa51e5011) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [properties](structbt__gatt__chrc.md#a81bb8257052d7c8d03b51acaa51e5011);

331};

332

[ 334](group__bt__gatt.md#gad1825f8deafc36d7e8f09c2835884fc6)#define BT\_GATT\_CEP\_RELIABLE\_WRITE 0x0001

[ 335](group__bt__gatt.md#ga64898ec8390c89c1fc5bdf0364220a43)#define BT\_GATT\_CEP\_WRITABLE\_AUX 0x0002

336

[ 338](structbt__gatt__cep.md)struct [bt\_gatt\_cep](structbt__gatt__cep.md) {

[ 340](structbt__gatt__cep.md#a317442dc204f7632b0c5da8a8a9a98b5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [properties](structbt__gatt__cep.md#a317442dc204f7632b0c5da8a8a9a98b5);

341};

342

344

[ 350](group__bt__gatt.md#ga240a10df32aa7a256a103ceee7211f8d)#define BT\_GATT\_CCC\_NOTIFY 0x0001

[ 356](group__bt__gatt.md#ga60ff2ddcc2e3148881a2f15745ba06e8)#define BT\_GATT\_CCC\_INDICATE 0x0002

357

[ 359](structbt__gatt__ccc.md)struct [bt\_gatt\_ccc](structbt__gatt__ccc.md) {

[ 361](structbt__gatt__ccc.md#ac8fa1028c5e87aa025832257b18fa7c3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](structbt__gatt__ccc.md#ac8fa1028c5e87aa025832257b18fa7c3);

362};

363

365

[ 372](group__bt__gatt.md#ga7a7d3cfa6eec4baa0b57ec9c4bc41f7a)#define BT\_GATT\_SCC\_BROADCAST 0x0001

373

[ 375](structbt__gatt__scc.md)struct [bt\_gatt\_scc](structbt__gatt__scc.md) {

[ 377](structbt__gatt__scc.md#aa7ddf1810f6d47e59c364b7489823d00) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](structbt__gatt__scc.md#aa7ddf1810f6d47e59c364b7489823d00);

378};

379

[ 381](structbt__gatt__cpf.md)struct [bt\_gatt\_cpf](structbt__gatt__cpf.md) {

[ 383](structbt__gatt__cpf.md#ab0ca135a75130b3ffc0c5bf375f3528f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [format](structbt__gatt__cpf.md#ab0ca135a75130b3ffc0c5bf375f3528f);

[ 387](structbt__gatt__cpf.md#a3690a86c942badb2d2698481b03e436d) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [exponent](structbt__gatt__cpf.md#a3690a86c942badb2d2698481b03e436d);

[ 389](structbt__gatt__cpf.md#a2a9f3d3f72b9acb1ef7f2dc765e5a231) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [unit](structbt__gatt__cpf.md#a2a9f3d3f72b9acb1ef7f2dc765e5a231);

[ 391](structbt__gatt__cpf.md#a1dfbb9fc1e1397d2abec04b216d7ae33) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [name\_space](structbt__gatt__cpf.md#a1dfbb9fc1e1397d2abec04b216d7ae33);

[ 393](structbt__gatt__cpf.md#a3c48dd5ea717fbaf510d13c64a370c06) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [description](structbt__gatt__cpf.md#a3c48dd5ea717fbaf510d13c64a370c06);

394};

395

401

[ 409](group__bt__gatt__server.md#ga270c8a52bf3d512defc373f8c29b59f2)void [bt\_gatt\_cb\_register](group__bt__gatt__server.md#ga270c8a52bf3d512defc373f8c29b59f2)(struct [bt\_gatt\_cb](structbt__gatt__cb.md) \*cb);

410

[ 429](group__bt__gatt__server.md#ga5eee6afc6db391ffeda295d298bf6a56)int [bt\_gatt\_authorization\_cb\_register](group__bt__gatt__server.md#ga5eee6afc6db391ffeda295d298bf6a56)(const struct [bt\_gatt\_authorization\_cb](structbt__gatt__authorization__cb.md) \*cb);

430

[ 457](group__bt__gatt__server.md#gab4d9cfea04e44445d5dc30ad52842b64)int [bt\_gatt\_service\_register](group__bt__gatt__server.md#gab4d9cfea04e44445d5dc30ad52842b64)(struct [bt\_gatt\_service](structbt__gatt__service.md) \*svc);

458

[ 465](group__bt__gatt__server.md#gaf5bf0205fad5f7ad187b764d23deba6b)int [bt\_gatt\_service\_unregister](group__bt__gatt__server.md#gaf5bf0205fad5f7ad187b764d23deba6b)(struct [bt\_gatt\_service](structbt__gatt__service.md) \*svc);

466

[ 473](group__bt__gatt__server.md#gae5c1e8b7bb1e673e228f03d1d084be9a)bool [bt\_gatt\_service\_is\_registered](group__bt__gatt__server.md#gae5c1e8b7bb1e673e228f03d1d084be9a)(const struct [bt\_gatt\_service](structbt__gatt__service.md) \*svc);

474

475enum {

[ 476](group__bt__gatt__server.md#ggab94ce0108483b70392b31a621aa0712aaa3f2a25e27c7065a2c7bb2a9ff09542e) [BT\_GATT\_ITER\_STOP](group__bt__gatt__server.md#ggab94ce0108483b70392b31a621aa0712aaa3f2a25e27c7065a2c7bb2a9ff09542e) = 0,

[ 477](group__bt__gatt__server.md#ggab94ce0108483b70392b31a621aa0712aaea569feffa4815d3443e12be78c684f5) [BT\_GATT\_ITER\_CONTINUE](group__bt__gatt__server.md#ggab94ce0108483b70392b31a621aa0712aaea569feffa4815d3443e12be78c684f5),

478};

479

[ 490](group__bt__gatt__server.md#ga60284611c90729b289fe806524ba9209)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) (\*[bt\_gatt\_attr\_func\_t](group__bt__gatt__server.md#ga60284611c90729b289fe806524ba9209))(const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr,

491 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__gatt__attr.md#aeee42a3d3ca15e40cf11cc0c3fde106b),

492 void \*[user\_data](structbt__gatt__attr.md#adeb063fb101fab45dd789c7212c43357));

493

[ 506](group__bt__gatt__server.md#gad8d8f513004f391167212d7bf9f7ff10)void [bt\_gatt\_foreach\_attr\_type](group__bt__gatt__server.md#gad8d8f513004f391167212d7bf9f7ff10)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_handle, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) end\_handle,

507 const struct [bt\_uuid](structbt__uuid.md) \*[uuid](structbt__gatt__attr.md#a6958f507f9ff172018be458ebc86106f),

508 const void \*attr\_data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_matches,

509 [bt\_gatt\_attr\_func\_t](group__bt__gatt__server.md#ga60284611c90729b289fe806524ba9209) func,

510 void \*[user\_data](structbt__gatt__attr.md#adeb063fb101fab45dd789c7212c43357));

511

[ 521](group__bt__gatt__server.md#gaa93b5e0f2870ed135447bead903c175a)static inline void [bt\_gatt\_foreach\_attr](group__bt__gatt__server.md#gaa93b5e0f2870ed135447bead903c175a)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_handle, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) end\_handle,

522 [bt\_gatt\_attr\_func\_t](group__bt__gatt__server.md#ga60284611c90729b289fe806524ba9209) func,

523 void \*[user\_data](structbt__gatt__attr.md#adeb063fb101fab45dd789c7212c43357))

524{

525 [bt\_gatt\_foreach\_attr\_type](group__bt__gatt__server.md#gad8d8f513004f391167212d7bf9f7ff10)(start\_handle, end\_handle, NULL, NULL, 0, func,

526 [user\_data](structbt__gatt__attr.md#adeb063fb101fab45dd789c7212c43357));

527}

528

[ 537](group__bt__gatt__server.md#ga35cecaa43b00b374062d29cca1479d85)struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*[bt\_gatt\_attr\_next](group__bt__gatt__server.md#ga35cecaa43b00b374062d29cca1479d85)(const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr);

538

[ 553](group__bt__gatt__server.md#gad2f3272b1dc42378104b492ec7caf6b0)struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*[bt\_gatt\_find\_by\_uuid](group__bt__gatt__server.md#gad2f3272b1dc42378104b492ec7caf6b0)(const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr,

554 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) attr\_count,

555 const struct [bt\_uuid](structbt__uuid.md) \*[uuid](structbt__gatt__attr.md#a6958f507f9ff172018be458ebc86106f));

556

[ 564](group__bt__gatt__server.md#ga2d51136ea1bd6cdb50900639506fd9f7)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [bt\_gatt\_attr\_get\_handle](group__bt__gatt__server.md#ga2d51136ea1bd6cdb50900639506fd9f7)(const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr);

565

[ 576](group__bt__gatt__server.md#ga99738cf4f05eae4c6da17cc3420827d8)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [bt\_gatt\_attr\_value\_handle](group__bt__gatt__server.md#ga99738cf4f05eae4c6da17cc3420827d8)(const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr);

577

[ 593](group__bt__gatt__server.md#gaf6d253849932b706ec7f303568980dfa)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [bt\_gatt\_attr\_read](group__bt__gatt__server.md#gaf6d253849932b706ec7f303568980dfa)(struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr,

594 void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) buf\_len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset,

595 const void \*value, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) value\_len);

596

[ 612](group__bt__gatt__server.md#gacae81c0f272bad7e6ac93c0d13b678c6)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [bt\_gatt\_attr\_read\_service](group__bt__gatt__server.md#gacae81c0f272bad7e6ac93c0d13b678c6)(struct bt\_conn \*conn,

613 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr,

614 void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset);

615

[ 623](group__bt__gatt__server.md#ga04c7887fb67107bd060dd023fd3186d5)#define BT\_GATT\_SERVICE\_DEFINE(\_name, ...) \

624 const struct bt\_gatt\_attr attr\_##\_name[] = { \_\_VA\_ARGS\_\_ }; \

625 const STRUCT\_SECTION\_ITERABLE(bt\_gatt\_service\_static, \_name) = \

626 BT\_GATT\_SERVICE(attr\_##\_name)

627

628#define \_BT\_GATT\_ATTRS\_ARRAY\_DEFINE(n, \_instances, \_attrs\_def) \

629 static struct bt\_gatt\_attr attrs\_##n[] = \_attrs\_def(\_instances[n])

630

631#define \_BT\_GATT\_SERVICE\_ARRAY\_ITEM(\_n, \_) BT\_GATT\_SERVICE(attrs\_##\_n)

632

[ 648](group__bt__gatt__server.md#ga8bb3aeef20465d7f6e38f6bbddef74e5)#define BT\_GATT\_SERVICE\_INSTANCE\_DEFINE( \

649 \_name, \_instances, \_instance\_num, \_attrs\_def) \

650 BUILD\_ASSERT(ARRAY\_SIZE(\_instances) == \_instance\_num, \

651 "The number of array elements does not match its size"); \

652 LISTIFY(\_instance\_num, \_BT\_GATT\_ATTRS\_ARRAY\_DEFINE, (;), \

653 \_instances, \_attrs\_def); \

654 static struct bt\_gatt\_service \_name[] = { \

655 LISTIFY(\_instance\_num, \_BT\_GATT\_SERVICE\_ARRAY\_ITEM, (,)) \

656 }

657

[ 665](group__bt__gatt__server.md#ga7d413ec013b91a633ec24d80d2814e2b)#define BT\_GATT\_SERVICE(\_attrs) \

666{ \

667 .attrs = \_attrs, \

668 .attr\_count = ARRAY\_SIZE(\_attrs), \

669}

670

[ 678](group__bt__gatt__server.md#gaacada0ff1029af959b6fcd6703d4a0bf)#define BT\_GATT\_PRIMARY\_SERVICE(\_service) \

679 BT\_GATT\_ATTRIBUTE(BT\_UUID\_GATT\_PRIMARY, BT\_GATT\_PERM\_READ, \

680 bt\_gatt\_attr\_read\_service, NULL, (void \*)\_service)

681

[ 692](group__bt__gatt__server.md#gaecb4d30282677d3450ad79c5f83f3445)#define BT\_GATT\_SECONDARY\_SERVICE(\_service) \

693 BT\_GATT\_ATTRIBUTE(BT\_UUID\_GATT\_SECONDARY, BT\_GATT\_PERM\_READ, \

694 bt\_gatt\_attr\_read\_service, NULL, (void \*)\_service)

695

[ 711](group__bt__gatt__server.md#ga4313a63decac2c8b7c4a1764df3d53ea)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [bt\_gatt\_attr\_read\_included](group__bt__gatt__server.md#ga4313a63decac2c8b7c4a1764df3d53ea)(struct bt\_conn \*conn,

712 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr,

713 void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset);

714

[ 722](group__bt__gatt__server.md#ga08ffee706d271b75a54b1b99249dba24)#define BT\_GATT\_INCLUDE\_SERVICE(\_service\_incl) \

723 BT\_GATT\_ATTRIBUTE(BT\_UUID\_GATT\_INCLUDE, BT\_GATT\_PERM\_READ, \

724 bt\_gatt\_attr\_read\_included, NULL, \_service\_incl)

725

[ 741](group__bt__gatt__server.md#gad58b526a06334530c13292d14a11257c)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [bt\_gatt\_attr\_read\_chrc](group__bt__gatt__server.md#gad58b526a06334530c13292d14a11257c)(struct bt\_conn \*conn,

742 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf,

743 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset);

744

[ 745](group__bt__gatt__server.md#ga7f19592a722c41d6c1d2421d166dd78a)#define BT\_GATT\_CHRC\_INIT(\_uuid, \_handle, \_props) \

746{ \

747 .uuid = \_uuid, \

748 .value\_handle = \_handle, \

749 .properties = \_props, \

750}

751

[ 769](group__bt__gatt__server.md#ga9e739546dbd906d3b3c4f1ed5ad9f41e)#define BT\_GATT\_CHARACTERISTIC(\_uuid, \_props, \_perm, \_read, \_write, \_user\_data) \

770 BT\_GATT\_ATTRIBUTE(BT\_UUID\_GATT\_CHRC, BT\_GATT\_PERM\_READ, \

771 bt\_gatt\_attr\_read\_chrc, NULL, \

772 ((struct bt\_gatt\_chrc[]) { \

773 BT\_GATT\_CHRC\_INIT(\_uuid, 0U, \_props), \

774 })), \

775 BT\_GATT\_ATTRIBUTE(\_uuid, \_perm, \_read, \_write, \_user\_data)

776

777#if defined(CONFIG\_BT\_SETTINGS\_CCC\_LAZY\_LOADING)

778 #define BT\_GATT\_CCC\_MAX (CONFIG\_BT\_MAX\_CONN)

779#elif defined(CONFIG\_BT\_CONN)

780 #define BT\_GATT\_CCC\_MAX (CONFIG\_BT\_MAX\_PAIRED + CONFIG\_BT\_MAX\_CONN)

781#else

[ 782](group__bt__gatt__server.md#gac1c0a195c1ec1ff2cdd5bf6d0ba6ad00) #define BT\_GATT\_CCC\_MAX 0

783#endif

784

[ 786](structbt__gatt__ccc__cfg.md)struct [bt\_gatt\_ccc\_cfg](structbt__gatt__ccc__cfg.md) {

[ 788](structbt__gatt__ccc__cfg.md#ac17ddefe7ca6dbac921ee4c6f44fbf51) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structbt__gatt__ccc__cfg.md#ac17ddefe7ca6dbac921ee4c6f44fbf51);

[ 790](structbt__gatt__ccc__cfg.md#ab316080693b2c4daf5fd45e2c0501c70) [bt\_addr\_le\_t](structbt__addr__le__t.md) [peer](structbt__gatt__ccc__cfg.md#ab316080693b2c4daf5fd45e2c0501c70);

[ 792](structbt__gatt__ccc__cfg.md#a92acf7329f66638ac6c657c8eaa795ac) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [value](structbt__gatt__ccc__cfg.md#a92acf7329f66638ac6c657c8eaa795ac);

793};

794

796struct \_bt\_gatt\_ccc {

798 struct [bt\_gatt\_ccc\_cfg](structbt__gatt__ccc__cfg.md) cfg[[BT\_GATT\_CCC\_MAX](group__bt__gatt__server.md#gac1c0a195c1ec1ff2cdd5bf6d0ba6ad00)];

799

801 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) value;

802

808 void (\*cfg\_changed)(const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) value);

809

819 [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*cfg\_write)(struct bt\_conn \*conn,

820 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) value);

821

833 [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*cfg\_match)(struct bt\_conn \*conn,

834 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr);

835};

836

[ 853](group__bt__gatt__server.md#ga2e85b42136e2c6a4cb5b7ad8a2532573)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [bt\_gatt\_attr\_read\_ccc](group__bt__gatt__server.md#ga2e85b42136e2c6a4cb5b7ad8a2532573)(struct bt\_conn \*conn,

854 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf,

855 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset);

856

[ 873](group__bt__gatt__server.md#gabba965b676650a55cb9934072b34c75e)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [bt\_gatt\_attr\_write\_ccc](group__bt__gatt__server.md#gabba965b676650a55cb9934072b34c75e)(struct bt\_conn \*conn,

874 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, const void \*buf,

875 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

876

877

[ 887](group__bt__gatt__server.md#ga59fd77199435e461e03a80c7121bb869)#define BT\_GATT\_CCC\_INITIALIZER(\_changed, \_write, \_match) \

888 { \

889 .cfg = {}, \

890 .cfg\_changed = \_changed, \

891 .cfg\_write = \_write, \

892 .cfg\_match = \_match, \

893 }

894

[ 904](group__bt__gatt__server.md#gad8b296ecfd1139680f21da7904b9f585)#define BT\_GATT\_CCC\_MANAGED(\_ccc, \_perm) \

905 BT\_GATT\_ATTRIBUTE(BT\_UUID\_GATT\_CCC, \_perm, \

906 bt\_gatt\_attr\_read\_ccc, bt\_gatt\_attr\_write\_ccc, \

907 \_ccc)

908

[ 918](group__bt__gatt__server.md#ga140b9c25d10244bebd9c891f881fdc94)#define BT\_GATT\_CCC(\_changed, \_perm) \

919 BT\_GATT\_CCC\_MANAGED(((struct \_bt\_gatt\_ccc[]) \

920 {BT\_GATT\_CCC\_INITIALIZER(\_changed, NULL, NULL)}), \_perm)

921

[ 938](group__bt__gatt__server.md#ga5893166f1b24f437a94ccf1fc57c7917)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [bt\_gatt\_attr\_read\_cep](group__bt__gatt__server.md#ga5893166f1b24f437a94ccf1fc57c7917)(struct bt\_conn \*conn,

939 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf,

940 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset);

941

[ 949](group__bt__gatt__server.md#ga55a82cada1093c4ff75fe5504ac504b1)#define BT\_GATT\_CEP(\_value) \

950 BT\_GATT\_DESCRIPTOR(BT\_UUID\_GATT\_CEP, BT\_GATT\_PERM\_READ, \

951 bt\_gatt\_attr\_read\_cep, NULL, (void \*)\_value)

952

[ 970](group__bt__gatt__server.md#ga29421c8788b47b6a648704d27d5f0d28)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [bt\_gatt\_attr\_read\_cud](group__bt__gatt__server.md#ga29421c8788b47b6a648704d27d5f0d28)(struct bt\_conn \*conn,

971 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf,

972 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset);

973

[ 983](group__bt__gatt__server.md#ga1e1cd9d0853e2dcbefcb85fda44dc9c7)#define BT\_GATT\_CUD(\_value, \_perm) \

984 BT\_GATT\_DESCRIPTOR(BT\_UUID\_GATT\_CUD, \_perm, bt\_gatt\_attr\_read\_cud, \

985 NULL, (void \*)\_value)

986

[ 1003](group__bt__gatt__server.md#ga5ae96590a0aaa5c4c3863a4a14d80fdd)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [bt\_gatt\_attr\_read\_cpf](group__bt__gatt__server.md#ga5ae96590a0aaa5c4c3863a4a14d80fdd)(struct bt\_conn \*conn,

1004 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf,

1005 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset);

1006

[ 1014](group__bt__gatt__server.md#ga3835fcfdf7a5f917e21c9d17e75162be)#define BT\_GATT\_CPF(\_value) \

1015 BT\_GATT\_DESCRIPTOR(BT\_UUID\_GATT\_CPF, BT\_GATT\_PERM\_READ, \

1016 bt\_gatt\_attr\_read\_cpf, NULL, (void \*)\_value)

1017

[ 1032](group__bt__gatt__server.md#ga83207fc083454327004f7d3c3e5b3840)#define BT\_GATT\_DESCRIPTOR(\_uuid, \_perm, \_read, \_write, \_user\_data) \

1033 BT\_GATT\_ATTRIBUTE(\_uuid, \_perm, \_read, \_write, \_user\_data)

1034

[ 1047](group__bt__gatt__server.md#gac4abfeb068d16dcdaceee812c12bf406)#define BT\_GATT\_ATTRIBUTE(\_uuid, \_perm, \_read, \_write, \_user\_data) \

1048{ \

1049 .uuid = \_uuid, \

1050 .read = \_read, \

1051 .write = \_write, \

1052 .user\_data = \_user\_data, \

1053 .handle = 0, \

1054 .perm = \_perm, \

1055}

1056

[ 1062](group__bt__gatt__server.md#gac55832607b95f394d26a64ed1cfe5bba)typedef void (\*[bt\_gatt\_complete\_func\_t](group__bt__gatt__server.md#gac55832607b95f394d26a64ed1cfe5bba)) (struct bt\_conn \*conn, void \*user\_data);

1063

[ 1064](structbt__gatt__notify__params.md)struct [bt\_gatt\_notify\_params](structbt__gatt__notify__params.md) {

[ 1070](structbt__gatt__notify__params.md#a2994cbe737fad725c60427000c21c373) const struct [bt\_uuid](structbt__uuid.md) \*[uuid](structbt__gatt__notify__params.md#a2994cbe737fad725c60427000c21c373);

[ 1076](structbt__gatt__notify__params.md#a6187d0457763a15a623129e3e9e98e13) const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*[attr](structbt__gatt__notify__params.md#a6187d0457763a15a623129e3e9e98e13);

[ 1078](structbt__gatt__notify__params.md#afaa276cff9cbf204c433ca776904ef32) const void \*[data](structbt__gatt__notify__params.md#afaa276cff9cbf204c433ca776904ef32);

[ 1080](structbt__gatt__notify__params.md#a4a511da0b099ca88d895594caf7aaa6a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structbt__gatt__notify__params.md#a4a511da0b099ca88d895594caf7aaa6a);

[ 1082](structbt__gatt__notify__params.md#ace3c6b5f5ed78b9f64c25b868d3bfbe2) [bt\_gatt\_complete\_func\_t](group__bt__gatt__server.md#gac55832607b95f394d26a64ed1cfe5bba) [func](structbt__gatt__notify__params.md#ace3c6b5f5ed78b9f64c25b868d3bfbe2);

[ 1084](structbt__gatt__notify__params.md#adec9a6f6ea0604e82b90dd47bb9951fa) void \*[user\_data](structbt__gatt__notify__params.md#adec9a6f6ea0604e82b90dd47bb9951fa);

1085#if defined(CONFIG\_BT\_EATT)

[ 1086](structbt__gatt__notify__params.md#a978d7a42c39a098cedf751936f280fac) enum [bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c) [chan\_opt](structbt__gatt__notify__params.md#a978d7a42c39a098cedf751936f280fac);

1087#endif /\* CONFIG\_BT\_EATT \*/

1088};

1089

[ 1111](group__bt__gatt__server.md#ga55e3ef7cb43b8acb0a27643c78390146)int [bt\_gatt\_notify\_cb](group__bt__gatt__server.md#ga55e3ef7cb43b8acb0a27643c78390146)(struct bt\_conn \*conn,

1112 struct [bt\_gatt\_notify\_params](structbt__gatt__notify__params.md) \*params);

1113

[ 1165](group__bt__gatt__server.md#ga8071d6063f85c0a78155f6b2ac2da635)int [bt\_gatt\_notify\_multiple](group__bt__gatt__server.md#ga8071d6063f85c0a78155f6b2ac2da635)(struct bt\_conn \*conn,

1166 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_params,

1167 struct [bt\_gatt\_notify\_params](structbt__gatt__notify__params.md) params[]);

1168

[ 1188](group__bt__gatt__server.md#ga74ee552864c563aa5bc939f37395c14a)static inline int [bt\_gatt\_notify](group__bt__gatt__server.md#ga74ee552864c563aa5bc939f37395c14a)(struct bt\_conn \*conn,

1189 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr,

1190 const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len)

1191{

1192 struct [bt\_gatt\_notify\_params](structbt__gatt__notify__params.md) params;

1193

1194 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(&params, 0, sizeof(params));

1195

1196 params.[attr](structbt__gatt__notify__params.md#a6187d0457763a15a623129e3e9e98e13) = [attr](structbt__gatt__notify__params.md#a6187d0457763a15a623129e3e9e98e13);

1197 params.[data](structbt__gatt__notify__params.md#afaa276cff9cbf204c433ca776904ef32) = [data](structbt__gatt__notify__params.md#afaa276cff9cbf204c433ca776904ef32);

1198 params.[len](structbt__gatt__notify__params.md#a4a511da0b099ca88d895594caf7aaa6a) = [len](structbt__gatt__notify__params.md#a4a511da0b099ca88d895594caf7aaa6a);

1199#if defined(CONFIG\_BT\_EATT)

1200 params.[chan\_opt](structbt__gatt__notify__params.md#a978d7a42c39a098cedf751936f280fac) = [BT\_ATT\_CHAN\_OPT\_NONE](group__bt__att.md#ggac593a27ecf029f33f50f990b2947562ca14e709b93e78dcc511339a99360ba739);

1201#endif /\* CONFIG\_BT\_EATT \*/

1202

1203 return [bt\_gatt\_notify\_cb](group__bt__gatt__server.md#ga55e3ef7cb43b8acb0a27643c78390146)(conn, &params);

1204}

1205

[ 1225](group__bt__gatt__server.md#ga24bae284dbc71cd4075649c4bc348b7c)static inline int [bt\_gatt\_notify\_uuid](group__bt__gatt__server.md#ga24bae284dbc71cd4075649c4bc348b7c)(struct bt\_conn \*conn,

1226 const struct [bt\_uuid](structbt__uuid.md) \*[uuid](structbt__gatt__notify__params.md#a2994cbe737fad725c60427000c21c373),

1227 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*[attr](structbt__gatt__notify__params.md#a6187d0457763a15a623129e3e9e98e13),

1228 const void \*[data](structbt__gatt__notify__params.md#afaa276cff9cbf204c433ca776904ef32), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structbt__gatt__notify__params.md#a4a511da0b099ca88d895594caf7aaa6a))

1229{

1230 struct [bt\_gatt\_notify\_params](structbt__gatt__notify__params.md) params;

1231

1232 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(&params, 0, sizeof(params));

1233

1234 params.[uuid](structbt__gatt__notify__params.md#a2994cbe737fad725c60427000c21c373) = [uuid](structbt__gatt__notify__params.md#a2994cbe737fad725c60427000c21c373);

1235 params.[attr](structbt__gatt__notify__params.md#a6187d0457763a15a623129e3e9e98e13) = [attr](structbt__gatt__notify__params.md#a6187d0457763a15a623129e3e9e98e13);

1236 params.[data](structbt__gatt__notify__params.md#afaa276cff9cbf204c433ca776904ef32) = [data](structbt__gatt__notify__params.md#afaa276cff9cbf204c433ca776904ef32);

1237 params.[len](structbt__gatt__notify__params.md#a4a511da0b099ca88d895594caf7aaa6a) = [len](structbt__gatt__notify__params.md#a4a511da0b099ca88d895594caf7aaa6a);

1238#if defined(CONFIG\_BT\_EATT)

1239 params.[chan\_opt](structbt__gatt__notify__params.md#a978d7a42c39a098cedf751936f280fac) = [BT\_ATT\_CHAN\_OPT\_NONE](group__bt__att.md#ggac593a27ecf029f33f50f990b2947562ca14e709b93e78dcc511339a99360ba739);

1240#endif /\* CONFIG\_BT\_EATT \*/

1241

1242 return [bt\_gatt\_notify\_cb](group__bt__gatt__server.md#ga55e3ef7cb43b8acb0a27643c78390146)(conn, &params);

1243}

1244

1245/\* Forward declaration of the bt\_gatt\_indicate\_params structure \*/

1246struct [bt\_gatt\_indicate\_params](structbt__gatt__indicate__params.md);

1247

[ 1255](group__bt__gatt__server.md#ga1294850e6bdcbe7a8f42f2956fd837a8)typedef void (\*[bt\_gatt\_indicate\_func\_t](group__bt__gatt__server.md#ga1294850e6bdcbe7a8f42f2956fd837a8))(struct bt\_conn \*conn,

1256 struct [bt\_gatt\_indicate\_params](structbt__gatt__indicate__params.md) \*params,

1257 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) err);

1258

[ 1259](group__bt__gatt__server.md#ga5d47ed9eaea22c8f00db14329daee8fe)typedef void (\*[bt\_gatt\_indicate\_params\_destroy\_t](group__bt__gatt__server.md#ga5d47ed9eaea22c8f00db14329daee8fe))(

1260 struct [bt\_gatt\_indicate\_params](structbt__gatt__indicate__params.md) \*params);

1261

[ 1263](structbt__gatt__indicate__params.md)struct [bt\_gatt\_indicate\_params](structbt__gatt__indicate__params.md) {

[ 1269](structbt__gatt__indicate__params.md#afde06f47d7a817291e437593ea01bccd) const struct [bt\_uuid](structbt__uuid.md) \*[uuid](structbt__gatt__indicate__params.md#afde06f47d7a817291e437593ea01bccd);

[ 1275](structbt__gatt__indicate__params.md#acbbee3a71838492416b20bb5cff89801) const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*[attr](structbt__gatt__indicate__params.md#acbbee3a71838492416b20bb5cff89801);

[ 1277](structbt__gatt__indicate__params.md#af9eb83c3fba49ee3cd6162d5a2791707) [bt\_gatt\_indicate\_func\_t](group__bt__gatt__server.md#ga1294850e6bdcbe7a8f42f2956fd837a8) [func](structbt__gatt__indicate__params.md#af9eb83c3fba49ee3cd6162d5a2791707);

[ 1279](structbt__gatt__indicate__params.md#aeb346dc4c0e4a298c66f394d037a6514) [bt\_gatt\_indicate\_params\_destroy\_t](group__bt__gatt__server.md#ga5d47ed9eaea22c8f00db14329daee8fe) [destroy](structbt__gatt__indicate__params.md#aeb346dc4c0e4a298c66f394d037a6514);

[ 1281](structbt__gatt__indicate__params.md#ae1d657512c99d5bba6fc99a450a6da32) const void \*[data](structbt__gatt__indicate__params.md#ae1d657512c99d5bba6fc99a450a6da32);

[ 1283](structbt__gatt__indicate__params.md#a10ad44140371165951eeac18cb3d0e7f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structbt__gatt__indicate__params.md#a10ad44140371165951eeac18cb3d0e7f);

1285 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_ref;

1286#if defined(CONFIG\_BT\_EATT)

[ 1287](structbt__gatt__indicate__params.md#a0e536938123ecb4f3ba6736c1de2a599) enum [bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c) [chan\_opt](structbt__gatt__indicate__params.md#a0e536938123ecb4f3ba6736c1de2a599);

1288#endif /\* CONFIG\_BT\_EATT \*/

1289};

1290

[ 1316](group__bt__gatt__server.md#ga4f2272692cc0f1d44638828012296c80)int [bt\_gatt\_indicate](group__bt__gatt__server.md#ga4f2272692cc0f1d44638828012296c80)(struct bt\_conn \*conn,

1317 struct [bt\_gatt\_indicate\_params](structbt__gatt__indicate__params.md) \*params);

1318

1319

[ 1338](group__bt__gatt__server.md#gabd4df0a264dae10e43797992a567be7d)bool [bt\_gatt\_is\_subscribed](group__bt__gatt__server.md#gabd4df0a264dae10e43797992a567be7d)(struct bt\_conn \*conn,

1339 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ccc\_type);

1340

[ 1350](group__bt__gatt__server.md#ga351fd7658eaecbbfa60f1769119ef733)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [bt\_gatt\_get\_mtu](group__bt__gatt__server.md#ga351fd7658eaecbbfa60f1769119ef733)(struct bt\_conn \*conn);

1351

1353

1359

[ 1361](structbt__gatt__exchange__params.md)struct [bt\_gatt\_exchange\_params](structbt__gatt__exchange__params.md) {

[ 1363](structbt__gatt__exchange__params.md#a76f4d3e779da9c725914574ac2e22ad1) void (\*[func](structbt__gatt__exchange__params.md#a76f4d3e779da9c725914574ac2e22ad1))(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) err,

1364 struct [bt\_gatt\_exchange\_params](structbt__gatt__exchange__params.md) \*params);

1365};

1366

[ 1394](group__bt__gatt__client.md#ga0f41da23c6559a8254b04295aff8198d)int [bt\_gatt\_exchange\_mtu](group__bt__gatt__client.md#ga0f41da23c6559a8254b04295aff8198d)(struct bt\_conn \*conn,

1395 struct [bt\_gatt\_exchange\_params](structbt__gatt__exchange__params.md) \*params);

1396

1397struct [bt\_gatt\_discover\_params](structbt__gatt__discover__params.md);

1398

[ 1443](group__bt__gatt__client.md#gabd3bcd3c1560956726574faed332fb13)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) (\*[bt\_gatt\_discover\_func\_t](group__bt__gatt__client.md#gabd3bcd3c1560956726574faed332fb13))(struct bt\_conn \*conn,

1444 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr,

1445 struct [bt\_gatt\_discover\_params](structbt__gatt__discover__params.md) \*params);

1446

1448enum {

[ 1450](group__bt__gatt__client.md#ggaa7bf94a9823d44c702cc26dc8ade8403ada9ac33aa77f6043da8133dcf269478f) [BT\_GATT\_DISCOVER\_PRIMARY](group__bt__gatt__client.md#ggaa7bf94a9823d44c702cc26dc8ade8403ada9ac33aa77f6043da8133dcf269478f),

[ 1452](group__bt__gatt__client.md#ggaa7bf94a9823d44c702cc26dc8ade8403a21be62548b816c7960a54dd6e3b37a97) [BT\_GATT\_DISCOVER\_SECONDARY](group__bt__gatt__client.md#ggaa7bf94a9823d44c702cc26dc8ade8403a21be62548b816c7960a54dd6e3b37a97),

[ 1454](group__bt__gatt__client.md#ggaa7bf94a9823d44c702cc26dc8ade8403a80afff1c83bb5ebb5603af699f2c26da) [BT\_GATT\_DISCOVER\_INCLUDE](group__bt__gatt__client.md#ggaa7bf94a9823d44c702cc26dc8ade8403a80afff1c83bb5ebb5603af699f2c26da),

[ 1459](group__bt__gatt__client.md#ggaa7bf94a9823d44c702cc26dc8ade8403a71355dfe0bf30c88f9fe2f7da1ba10ae) [BT\_GATT\_DISCOVER\_CHARACTERISTIC](group__bt__gatt__client.md#ggaa7bf94a9823d44c702cc26dc8ade8403a71355dfe0bf30c88f9fe2f7da1ba10ae),

[ 1468](group__bt__gatt__client.md#ggaa7bf94a9823d44c702cc26dc8ade8403a0ccb2587aa8f21361c5d73847a33ecbe) [BT\_GATT\_DISCOVER\_DESCRIPTOR](group__bt__gatt__client.md#ggaa7bf94a9823d44c702cc26dc8ade8403a0ccb2587aa8f21361c5d73847a33ecbe),

[ 1477](group__bt__gatt__client.md#ggaa7bf94a9823d44c702cc26dc8ade8403afe2167b873b848935d56f6ee7f2c444c) [BT\_GATT\_DISCOVER\_ATTRIBUTE](group__bt__gatt__client.md#ggaa7bf94a9823d44c702cc26dc8ade8403afe2167b873b848935d56f6ee7f2c444c),

[ 1488](group__bt__gatt__client.md#ggaa7bf94a9823d44c702cc26dc8ade8403a81a1f8737c415544a0f793f4e626bb61) [BT\_GATT\_DISCOVER\_STD\_CHAR\_DESC](group__bt__gatt__client.md#ggaa7bf94a9823d44c702cc26dc8ade8403a81a1f8737c415544a0f793f4e626bb61),

1489};

1490

[ 1492](structbt__gatt__discover__params.md)struct [bt\_gatt\_discover\_params](structbt__gatt__discover__params.md) {

[ 1494](structbt__gatt__discover__params.md#a77d6665c01902e4e23cf8de8a9436262) const struct [bt\_uuid](structbt__uuid.md) \*[uuid](structbt__gatt__discover__params.md#a77d6665c01902e4e23cf8de8a9436262);

[ 1496](structbt__gatt__discover__params.md#a337d7366c12451938f12eec4dc60903e) [bt\_gatt\_discover\_func\_t](group__bt__gatt__client.md#gabd3bcd3c1560956726574faed332fb13) [func](structbt__gatt__discover__params.md#a337d7366c12451938f12eec4dc60903e);

1497 union {

1498 struct {

[ 1500](structbt__gatt__discover__params.md#a65ca3c9aad7c02d48fd35c4d6f69dc70) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [attr\_handle](structbt__gatt__discover__params.md#a65ca3c9aad7c02d48fd35c4d6f69dc70);

[ 1502](structbt__gatt__discover__params.md#a0d2604e7c3ee8969cb5096cbf5793fdb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [start\_handle](structbt__gatt__discover__params.md#a0d2604e7c3ee8969cb5096cbf5793fdb);

[ 1504](structbt__gatt__discover__params.md#a225868498c34411cc3fc2be8e678e85e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [end\_handle](structbt__gatt__discover__params.md#a225868498c34411cc3fc2be8e678e85e);

1505 } \_included;

1507 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_handle;

1508 };

1510 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [end\_handle](structbt__gatt__discover__params.md#a225868498c34411cc3fc2be8e678e85e);

[ 1512](structbt__gatt__discover__params.md#ab0f056c90954e1246d897019abd1e7fc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__gatt__discover__params.md#ab0f056c90954e1246d897019abd1e7fc);

1513#if defined(CONFIG\_BT\_GATT\_AUTO\_DISCOVER\_CCC) || defined(\_\_DOXYGEN\_\_)

[ 1515](structbt__gatt__discover__params.md#a87b130c520ce50f835d0589fd22a844c) struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \*[sub\_params](structbt__gatt__discover__params.md#a87b130c520ce50f835d0589fd22a844c);

1516#endif /\* defined(CONFIG\_BT\_GATT\_AUTO\_DISCOVER\_CCC) || defined(\_\_DOXYGEN\_\_) \*/

1517#if defined(CONFIG\_BT\_EATT)

[ 1518](structbt__gatt__discover__params.md#aba7585e3d0eefb323fcde9bcc88e287d) enum [bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c) [chan\_opt](structbt__gatt__discover__params.md#aba7585e3d0eefb323fcde9bcc88e287d);

1519#endif /\* CONFIG\_BT\_EATT \*/

1520};

1521

[ 1558](group__bt__gatt__client.md#gac06a945e5f7939b6716bc4f2cea781bd)int [bt\_gatt\_discover](group__bt__gatt__client.md#gac06a945e5f7939b6716bc4f2cea781bd)(struct bt\_conn \*conn,

1559 struct [bt\_gatt\_discover\_params](structbt__gatt__discover__params.md) \*params);

1560

1561struct [bt\_gatt\_read\_params](structbt__gatt__read__params.md);

1562

[ 1578](group__bt__gatt__client.md#ga1ca94b4f2b6c456b6134e05127993569)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) (\*[bt\_gatt\_read\_func\_t](group__bt__gatt__client.md#ga1ca94b4f2b6c456b6134e05127993569))(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) err,

1579 struct [bt\_gatt\_read\_params](structbt__gatt__read__params.md) \*params,

1580 const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length);

1581

[ 1583](structbt__gatt__read__params.md)struct [bt\_gatt\_read\_params](structbt__gatt__read__params.md) {

[ 1585](structbt__gatt__read__params.md#a3ea107db0b7537c9dccb2aa6d8f916fb) [bt\_gatt\_read\_func\_t](group__bt__gatt__client.md#ga1ca94b4f2b6c456b6134e05127993569) [func](structbt__gatt__read__params.md#a3ea107db0b7537c9dccb2aa6d8f916fb);

[ 1590](structbt__gatt__read__params.md#a0a36063ac0b110fbf57ef6a66f7bece8) size\_t [handle\_count](structbt__gatt__read__params.md#a0a36063ac0b110fbf57ef6a66f7bece8);

1591 union {

1592 struct {

[ 1594](structbt__gatt__read__params.md#af37beb6a69b3a6b90da0594b099bd64d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__gatt__read__params.md#af37beb6a69b3a6b90da0594b099bd64d);

[ 1596](structbt__gatt__read__params.md#a27f685a45c405bb2784fe369513724ad) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [offset](structbt__gatt__read__params.md#a27f685a45c405bb2784fe369513724ad);

[ 1597](structbt__gatt__read__params.md#a1ff7320ad5b67fff803ecd1a4e801b84) } [single](structbt__gatt__read__params.md#a1ff7320ad5b67fff803ecd1a4e801b84);

1598 struct {

[ 1602](structbt__gatt__read__params.md#a2794b8806933d0e16cfc77f4087fdeda) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*[handles](structbt__gatt__read__params.md#a2794b8806933d0e16cfc77f4087fdeda);

[ 1613](structbt__gatt__read__params.md#a77d05cbc54b125fc35d180cf91bf9cb9) bool [variable](structbt__gatt__read__params.md#a77d05cbc54b125fc35d180cf91bf9cb9);

[ 1614](structbt__gatt__read__params.md#adc0e62e7ee39e034193f347f79b436d7) } [multiple](structbt__gatt__read__params.md#adc0e62e7ee39e034193f347f79b436d7);

1615 struct {

[ 1617](structbt__gatt__read__params.md#ac11db1652cd5cee567d666d3697f3a4b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [start\_handle](structbt__gatt__read__params.md#ac11db1652cd5cee567d666d3697f3a4b);

[ 1619](structbt__gatt__read__params.md#a8b2a2b912efe557e24276a654087e75c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [end\_handle](structbt__gatt__read__params.md#a8b2a2b912efe557e24276a654087e75c);

[ 1621](structbt__gatt__read__params.md#ae2ba6ce4043769b86a050fd767248111) const struct [bt\_uuid](structbt__uuid.md) \*[uuid](structbt__gatt__read__params.md#ae2ba6ce4043769b86a050fd767248111);

[ 1622](structbt__gatt__read__params.md#a790606149a7619dd4338a6c6e7d24eaa) } [by\_uuid](structbt__gatt__read__params.md#a790606149a7619dd4338a6c6e7d24eaa);

1623 };

1624#if defined(CONFIG\_BT\_EATT)

[ 1625](structbt__gatt__read__params.md#a1335d1f9aefeff89a57efe78335cb41b) enum [bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c) [chan\_opt](structbt__gatt__read__params.md#a1335d1f9aefeff89a57efe78335cb41b);

1626#endif /\* CONFIG\_BT\_EATT \*/

1628 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \_att\_mtu;

1629};

1630

[ 1673](group__bt__gatt__client.md#ga1a18dd726ab960a88d7f85f2a014141a)int [bt\_gatt\_read](group__bt__gatt__client.md#ga1a18dd726ab960a88d7f85f2a014141a)(struct bt\_conn \*conn, struct [bt\_gatt\_read\_params](structbt__gatt__read__params.md) \*params);

1674

1675struct [bt\_gatt\_write\_params](structbt__gatt__write__params.md);

1676

[ 1684](group__bt__gatt__client.md#ga2bca8c4a45f41e0400a9e0147f4baf50)typedef void (\*[bt\_gatt\_write\_func\_t](group__bt__gatt__client.md#ga2bca8c4a45f41e0400a9e0147f4baf50))(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) err,

1685 struct [bt\_gatt\_write\_params](structbt__gatt__write__params.md) \*params);

1686

[ 1688](structbt__gatt__write__params.md)struct [bt\_gatt\_write\_params](structbt__gatt__write__params.md) {

[ 1690](structbt__gatt__write__params.md#a3468e3b75f3f9eda12bc4963f48cf9aa) [bt\_gatt\_write\_func\_t](group__bt__gatt__client.md#ga2bca8c4a45f41e0400a9e0147f4baf50) [func](structbt__gatt__write__params.md#a3468e3b75f3f9eda12bc4963f48cf9aa);

[ 1692](structbt__gatt__write__params.md#a384c5c15f248df5b327423ca32637bad) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__gatt__write__params.md#a384c5c15f248df5b327423ca32637bad);

[ 1694](structbt__gatt__write__params.md#add53cc08465d28f33bc48a1e8649ac1a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [offset](structbt__gatt__write__params.md#add53cc08465d28f33bc48a1e8649ac1a);

[ 1696](structbt__gatt__write__params.md#ab6510ef242e73325adb074322746c27c) const void \*[data](structbt__gatt__write__params.md#ab6510ef242e73325adb074322746c27c);

[ 1698](structbt__gatt__write__params.md#aded956dac2d398b642faeec81fdb9ec3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [length](structbt__gatt__write__params.md#aded956dac2d398b642faeec81fdb9ec3);

1699#if defined(CONFIG\_BT\_EATT)

[ 1700](structbt__gatt__write__params.md#ad79905c16f7ba5289817de552ece1a48) enum [bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c) [chan\_opt](structbt__gatt__write__params.md#ad79905c16f7ba5289817de552ece1a48);

1701#endif /\* CONFIG\_BT\_EATT \*/

1702};

1703

[ 1726](group__bt__gatt__client.md#ga843a42e68e0497d88d3f655f8ffd58d4)int [bt\_gatt\_write](group__bt__gatt__client.md#ga843a42e68e0497d88d3f655f8ffd58d4)(struct bt\_conn \*conn, struct [bt\_gatt\_write\_params](structbt__gatt__write__params.md) \*params);

1727

[ 1763](group__bt__gatt__client.md#ga49439413d12b5a8a1c68735e961ab6fa)int [bt\_gatt\_write\_without\_response\_cb](group__bt__gatt__client.md#ga49439413d12b5a8a1c68735e961ab6fa)(struct bt\_conn \*conn, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) handle,

1764 const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length,

1765 bool sign, [bt\_gatt\_complete\_func\_t](group__bt__gatt__server.md#gac55832607b95f394d26a64ed1cfe5bba) func,

1766 void \*user\_data);

1767

[ 1789](group__bt__gatt__client.md#ga9fc78e32230637a6f092da2400c50fe7)static inline int [bt\_gatt\_write\_without\_response](group__bt__gatt__client.md#ga9fc78e32230637a6f092da2400c50fe7)(struct bt\_conn \*conn,

1790 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) handle, const void \*data,

1791 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length, bool sign)

1792{

1793 return [bt\_gatt\_write\_without\_response\_cb](group__bt__gatt__client.md#ga49439413d12b5a8a1c68735e961ab6fa)(conn, handle, data, length,

1794 sign, NULL, NULL);

1795}

1796

1797struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md);

1798

[ 1815](group__bt__gatt__client.md#gab3e53eb5f9bb1eda7bf612ef95755b4d)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) (\*[bt\_gatt\_notify\_func\_t](group__bt__gatt__client.md#gab3e53eb5f9bb1eda7bf612ef95755b4d))(struct bt\_conn \*conn,

1816 struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \*params,

1817 const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length);

1818

[ 1826](group__bt__gatt__client.md#ga2e914e63b4b91fa56bc3295283c43714)typedef void (\*[bt\_gatt\_subscribe\_func\_t](group__bt__gatt__client.md#ga2e914e63b4b91fa56bc3295283c43714))(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) err,

1827 struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \*params);

1828

1830enum {

[ 1840](group__bt__gatt__client.md#gga07d7c3837ad936e586fdb11c0bd122d6aecdcb3baa850505f459523091c92a1cb) [BT\_GATT\_SUBSCRIBE\_FLAG\_VOLATILE](group__bt__gatt__client.md#gga07d7c3837ad936e586fdb11c0bd122d6aecdcb3baa850505f459523091c92a1cb),

1841

[ 1854](group__bt__gatt__client.md#gga07d7c3837ad936e586fdb11c0bd122d6a30bfd3fb4bf4f17653ba00942ba2b2e6) [BT\_GATT\_SUBSCRIBE\_FLAG\_NO\_RESUB](group__bt__gatt__client.md#gga07d7c3837ad936e586fdb11c0bd122d6a30bfd3fb4bf4f17653ba00942ba2b2e6),

1855

[ 1863](group__bt__gatt__client.md#gga07d7c3837ad936e586fdb11c0bd122d6afe1c3dc9380c33debd32a275d5bce8ad) [BT\_GATT\_SUBSCRIBE\_FLAG\_WRITE\_PENDING](group__bt__gatt__client.md#gga07d7c3837ad936e586fdb11c0bd122d6afe1c3dc9380c33debd32a275d5bce8ad),

1864

[ 1875](group__bt__gatt__client.md#gga07d7c3837ad936e586fdb11c0bd122d6a56aa5f332d4098e3942d7a902198f7ab) [BT\_GATT\_SUBSCRIBE\_FLAG\_SENT](group__bt__gatt__client.md#gga07d7c3837ad936e586fdb11c0bd122d6a56aa5f332d4098e3942d7a902198f7ab),

1876

[ 1877](group__bt__gatt__client.md#gga07d7c3837ad936e586fdb11c0bd122d6a5640a1e06740a89859c5f4b183d58e79) [BT\_GATT\_SUBSCRIBE\_NUM\_FLAGS](group__bt__gatt__client.md#gga07d7c3837ad936e586fdb11c0bd122d6a5640a1e06740a89859c5f4b183d58e79)

1878};

1879

[ 1881](structbt__gatt__subscribe__params.md)struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) {

[ 1883](structbt__gatt__subscribe__params.md#acf237ef097e8b847eb049fb0a5d4b759) [bt\_gatt\_notify\_func\_t](group__bt__gatt__client.md#gab3e53eb5f9bb1eda7bf612ef95755b4d) [notify](structbt__gatt__subscribe__params.md#acf237ef097e8b847eb049fb0a5d4b759);

[ 1887](structbt__gatt__subscribe__params.md#a91595407b8de4e862652e41100668f0a) [bt\_gatt\_subscribe\_func\_t](group__bt__gatt__client.md#ga2e914e63b4b91fa56bc3295283c43714) [subscribe](structbt__gatt__subscribe__params.md#a91595407b8de4e862652e41100668f0a);

1888

[ 1890](structbt__gatt__subscribe__params.md#a1cedb0e0067c8648c603296a63d2e3ee) [bt\_gatt\_write\_func\_t](group__bt__gatt__client.md#ga2bca8c4a45f41e0400a9e0147f4baf50) [write](structbt__gatt__subscribe__params.md#a1cedb0e0067c8648c603296a63d2e3ee);

[ 1892](structbt__gatt__subscribe__params.md#a9248418eb04a5b7a0faed5077c40bf22) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [value\_handle](structbt__gatt__subscribe__params.md#a9248418eb04a5b7a0faed5077c40bf22);

[ 1894](structbt__gatt__subscribe__params.md#a77c53cdfd4143483b33a8ecf6061561e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [ccc\_handle](structbt__gatt__subscribe__params.md#a77c53cdfd4143483b33a8ecf6061561e);

1895#if defined(CONFIG\_BT\_GATT\_AUTO\_DISCOVER\_CCC) || defined(\_\_DOXYGEN\_\_)

[ 1897](structbt__gatt__subscribe__params.md#af806d24aa97db1f2e9a021e719598a6d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [end\_handle](structbt__gatt__subscribe__params.md#af806d24aa97db1f2e9a021e719598a6d);

[ 1899](structbt__gatt__subscribe__params.md#ad3a3b9335b85777d65bdf875486e292a) struct [bt\_gatt\_discover\_params](structbt__gatt__discover__params.md) \*[disc\_params](structbt__gatt__subscribe__params.md#ad3a3b9335b85777d65bdf875486e292a);

1900#endif /\* defined(CONFIG\_BT\_GATT\_AUTO\_DISCOVER\_CCC) || defined(\_\_DOXYGEN\_\_) \*/

[ 1902](structbt__gatt__subscribe__params.md#a3bff1209b7a0b5908408a568622d0150) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [value](structbt__gatt__subscribe__params.md#a3bff1209b7a0b5908408a568622d0150);

1903#if defined(CONFIG\_BT\_SMP)

[ 1908](structbt__gatt__subscribe__params.md#a5b34bad1cf39bb3efd5faf516473dd4a) [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) [min\_security](structbt__gatt__subscribe__params.md#a5b34bad1cf39bb3efd5faf516473dd4a);

1909#endif

[ 1911](structbt__gatt__subscribe__params.md#aedd24024881e22372505355024cd716b) [ATOMIC\_DEFINE](group__atomic__apis.md#ga249c575db9764486197709b327f7370e)([flags](structbt__gatt__subscribe__params.md#aedd24024881e22372505355024cd716b), [BT\_GATT\_SUBSCRIBE\_NUM\_FLAGS](group__bt__gatt__client.md#gga07d7c3837ad936e586fdb11c0bd122d6a5640a1e06740a89859c5f4b183d58e79));

1912

[ 1913](structbt__gatt__subscribe__params.md#acbc7c9d38361e3b702fdf5efd7383b34) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structbt__gatt__subscribe__params.md#acbc7c9d38361e3b702fdf5efd7383b34);

1914#if defined(CONFIG\_BT\_EATT)

[ 1915](structbt__gatt__subscribe__params.md#ae139848da09705d37fe7c9de4c1a4087) enum [bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c) [chan\_opt](structbt__gatt__subscribe__params.md#ae139848da09705d37fe7c9de4c1a4087);

1916#endif /\* CONFIG\_BT\_EATT \*/

1917};

1918

[ 1956](group__bt__gatt__client.md#ga7d4a8e18f51ba6476886a15f81f48e5c)int [bt\_gatt\_subscribe](group__bt__gatt__client.md#ga7d4a8e18f51ba6476886a15f81f48e5c)(struct bt\_conn \*conn,

1957 struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \*params);

1958

[ 1975](group__bt__gatt__client.md#ga791b8bb8a4c085b022fafc0535a63511)int [bt\_gatt\_resubscribe](group__bt__gatt__client.md#ga791b8bb8a4c085b022fafc0535a63511)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*peer,

1976 struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \*params);

1977

[ 2002](group__bt__gatt__client.md#ga56509c9b8f73f729cfa5e75be22d79ae)int [bt\_gatt\_unsubscribe](group__bt__gatt__client.md#ga56509c9b8f73f729cfa5e75be22d79ae)(struct bt\_conn \*conn,

2003 struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \*params);

2004

[ 2022](group__bt__gatt__client.md#ga5193dea59a016692f94cf950d6b4f4f7)void [bt\_gatt\_cancel](group__bt__gatt__client.md#ga5193dea59a016692f94cf950d6b4f4f7)(struct bt\_conn \*conn, void \*params);

2023

2025

2026#ifdef \_\_cplusplus

2027}

2028#endif

2029

2033

2034#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_GATT\_H\_ \*/

[att.h](att_8h.md)

Attribute Protocol handling.

[conn.h](conn_8h.md)

Bluetooth connection handling.

[ATOMIC\_DEFINE](group__atomic__apis.md#ga249c575db9764486197709b327f7370e)

#define ATOMIC\_DEFINE(name, num\_bits)

Define an array of atomic variables.

**Definition** atomic.h:111

[bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c)

bt\_att\_chan\_opt

ATT channel option bit field values.

**Definition** att.h:146

[BT\_ATT\_CHAN\_OPT\_NONE](group__bt__att.md#ggac593a27ecf029f33f50f990b2947562ca14e709b93e78dcc511339a99360ba739)

@ BT\_ATT\_CHAN\_OPT\_NONE

Both Enhanced and Unenhanced channels can be used.

**Definition** att.h:148

[bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783)

bt\_security\_t

Security level.

**Definition** conn.h:352

[bt\_gatt\_exchange\_mtu](group__bt__gatt__client.md#ga0f41da23c6559a8254b04295aff8198d)

int bt\_gatt\_exchange\_mtu(struct bt\_conn \*conn, struct bt\_gatt\_exchange\_params \*params)

Exchange MTU.

[bt\_gatt\_read](group__bt__gatt__client.md#ga1a18dd726ab960a88d7f85f2a014141a)

int bt\_gatt\_read(struct bt\_conn \*conn, struct bt\_gatt\_read\_params \*params)

Read Attribute Value by handle.

[bt\_gatt\_read\_func\_t](group__bt__gatt__client.md#ga1ca94b4f2b6c456b6134e05127993569)

uint8\_t(\* bt\_gatt\_read\_func\_t)(struct bt\_conn \*conn, uint8\_t err, struct bt\_gatt\_read\_params \*params, const void \*data, uint16\_t length)

Read callback function.

**Definition** gatt.h:1578

[bt\_gatt\_write\_func\_t](group__bt__gatt__client.md#ga2bca8c4a45f41e0400a9e0147f4baf50)

void(\* bt\_gatt\_write\_func\_t)(struct bt\_conn \*conn, uint8\_t err, struct bt\_gatt\_write\_params \*params)

Write callback function.

**Definition** gatt.h:1684

[bt\_gatt\_subscribe\_func\_t](group__bt__gatt__client.md#ga2e914e63b4b91fa56bc3295283c43714)

void(\* bt\_gatt\_subscribe\_func\_t)(struct bt\_conn \*conn, uint8\_t err, struct bt\_gatt\_subscribe\_params \*params)

Subscription callback function.

**Definition** gatt.h:1826

[bt\_gatt\_write\_without\_response\_cb](group__bt__gatt__client.md#ga49439413d12b5a8a1c68735e961ab6fa)

int bt\_gatt\_write\_without\_response\_cb(struct bt\_conn \*conn, uint16\_t handle, const void \*data, uint16\_t length, bool sign, bt\_gatt\_complete\_func\_t func, void \*user\_data)

Write Attribute Value by handle without response with callback.

[bt\_gatt\_cancel](group__bt__gatt__client.md#ga5193dea59a016692f94cf950d6b4f4f7)

void bt\_gatt\_cancel(struct bt\_conn \*conn, void \*params)

Try to cancel the first pending request identified by params.

[bt\_gatt\_unsubscribe](group__bt__gatt__client.md#ga56509c9b8f73f729cfa5e75be22d79ae)

int bt\_gatt\_unsubscribe(struct bt\_conn \*conn, struct bt\_gatt\_subscribe\_params \*params)

Unsubscribe Attribute Value Notification.

[bt\_gatt\_resubscribe](group__bt__gatt__client.md#ga791b8bb8a4c085b022fafc0535a63511)

int bt\_gatt\_resubscribe(uint8\_t id, const bt\_addr\_le\_t \*peer, struct bt\_gatt\_subscribe\_params \*params)

Resubscribe Attribute Value Notification subscription.

[bt\_gatt\_subscribe](group__bt__gatt__client.md#ga7d4a8e18f51ba6476886a15f81f48e5c)

int bt\_gatt\_subscribe(struct bt\_conn \*conn, struct bt\_gatt\_subscribe\_params \*params)

Subscribe Attribute Value Notification.

[bt\_gatt\_write](group__bt__gatt__client.md#ga843a42e68e0497d88d3f655f8ffd58d4)

int bt\_gatt\_write(struct bt\_conn \*conn, struct bt\_gatt\_write\_params \*params)

Write Attribute Value by handle.

[bt\_gatt\_write\_without\_response](group__bt__gatt__client.md#ga9fc78e32230637a6f092da2400c50fe7)

static int bt\_gatt\_write\_without\_response(struct bt\_conn \*conn, uint16\_t handle, const void \*data, uint16\_t length, bool sign)

Write Attribute Value by handle without response.

**Definition** gatt.h:1789

[bt\_gatt\_notify\_func\_t](group__bt__gatt__client.md#gab3e53eb5f9bb1eda7bf612ef95755b4d)

uint8\_t(\* bt\_gatt\_notify\_func\_t)(struct bt\_conn \*conn, struct bt\_gatt\_subscribe\_params \*params, const void \*data, uint16\_t length)

Notification callback function.

**Definition** gatt.h:1815

[bt\_gatt\_discover\_func\_t](group__bt__gatt__client.md#gabd3bcd3c1560956726574faed332fb13)

uint8\_t(\* bt\_gatt\_discover\_func\_t)(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr, struct bt\_gatt\_discover\_params \*params)

Discover attribute callback function.

**Definition** gatt.h:1443

[bt\_gatt\_discover](group__bt__gatt__client.md#gac06a945e5f7939b6716bc4f2cea781bd)

int bt\_gatt\_discover(struct bt\_conn \*conn, struct bt\_gatt\_discover\_params \*params)

GATT Discover function.

[BT\_GATT\_SUBSCRIBE\_FLAG\_NO\_RESUB](group__bt__gatt__client.md#gga07d7c3837ad936e586fdb11c0bd122d6a30bfd3fb4bf4f17653ba00942ba2b2e6)

@ BT\_GATT\_SUBSCRIBE\_FLAG\_NO\_RESUB

No resubscribe flag.

**Definition** gatt.h:1854

[BT\_GATT\_SUBSCRIBE\_NUM\_FLAGS](group__bt__gatt__client.md#gga07d7c3837ad936e586fdb11c0bd122d6a5640a1e06740a89859c5f4b183d58e79)

@ BT\_GATT\_SUBSCRIBE\_NUM\_FLAGS

**Definition** gatt.h:1877

[BT\_GATT\_SUBSCRIBE\_FLAG\_SENT](group__bt__gatt__client.md#gga07d7c3837ad936e586fdb11c0bd122d6a56aa5f332d4098e3942d7a902198f7ab)

@ BT\_GATT\_SUBSCRIBE\_FLAG\_SENT

Sent flag.

**Definition** gatt.h:1875

[BT\_GATT\_SUBSCRIBE\_FLAG\_VOLATILE](group__bt__gatt__client.md#gga07d7c3837ad936e586fdb11c0bd122d6aecdcb3baa850505f459523091c92a1cb)

@ BT\_GATT\_SUBSCRIBE\_FLAG\_VOLATILE

Persistence flag.

**Definition** gatt.h:1840

[BT\_GATT\_SUBSCRIBE\_FLAG\_WRITE\_PENDING](group__bt__gatt__client.md#gga07d7c3837ad936e586fdb11c0bd122d6afe1c3dc9380c33debd32a275d5bce8ad)

@ BT\_GATT\_SUBSCRIBE\_FLAG\_WRITE\_PENDING

Write pending flag.

**Definition** gatt.h:1863

[BT\_GATT\_DISCOVER\_DESCRIPTOR](group__bt__gatt__client.md#ggaa7bf94a9823d44c702cc26dc8ade8403a0ccb2587aa8f21361c5d73847a33ecbe)

@ BT\_GATT\_DISCOVER\_DESCRIPTOR

Discover Descriptors.

**Definition** gatt.h:1468

[BT\_GATT\_DISCOVER\_SECONDARY](group__bt__gatt__client.md#ggaa7bf94a9823d44c702cc26dc8ade8403a21be62548b816c7960a54dd6e3b37a97)

@ BT\_GATT\_DISCOVER\_SECONDARY

Discover Secondary Services.

**Definition** gatt.h:1452

[BT\_GATT\_DISCOVER\_CHARACTERISTIC](group__bt__gatt__client.md#ggaa7bf94a9823d44c702cc26dc8ade8403a71355dfe0bf30c88f9fe2f7da1ba10ae)

@ BT\_GATT\_DISCOVER\_CHARACTERISTIC

Discover Characteristic Values.

**Definition** gatt.h:1459

[BT\_GATT\_DISCOVER\_INCLUDE](group__bt__gatt__client.md#ggaa7bf94a9823d44c702cc26dc8ade8403a80afff1c83bb5ebb5603af699f2c26da)

@ BT\_GATT\_DISCOVER\_INCLUDE

Discover Included Services.

**Definition** gatt.h:1454

[BT\_GATT\_DISCOVER\_STD\_CHAR\_DESC](group__bt__gatt__client.md#ggaa7bf94a9823d44c702cc26dc8ade8403a81a1f8737c415544a0f793f4e626bb61)

@ BT\_GATT\_DISCOVER\_STD\_CHAR\_DESC

Discover standard characteristic descriptor values.

**Definition** gatt.h:1488

[BT\_GATT\_DISCOVER\_PRIMARY](group__bt__gatt__client.md#ggaa7bf94a9823d44c702cc26dc8ade8403ada9ac33aa77f6043da8133dcf269478f)

@ BT\_GATT\_DISCOVER\_PRIMARY

Discover Primary Services.

**Definition** gatt.h:1450

[BT\_GATT\_DISCOVER\_ATTRIBUTE](group__bt__gatt__client.md#ggaa7bf94a9823d44c702cc26dc8ade8403afe2167b873b848935d56f6ee7f2c444c)

@ BT\_GATT\_DISCOVER\_ATTRIBUTE

Discover Attributes.

**Definition** gatt.h:1477

[bt\_gatt\_indicate\_func\_t](group__bt__gatt__server.md#ga1294850e6bdcbe7a8f42f2956fd837a8)

void(\* bt\_gatt\_indicate\_func\_t)(struct bt\_conn \*conn, struct bt\_gatt\_indicate\_params \*params, uint8\_t err)

Indication complete result callback.

**Definition** gatt.h:1255

[bt\_gatt\_notify\_uuid](group__bt__gatt__server.md#ga24bae284dbc71cd4075649c4bc348b7c)

static int bt\_gatt\_notify\_uuid(struct bt\_conn \*conn, const struct bt\_uuid \*uuid, const struct bt\_gatt\_attr \*attr, const void \*data, uint16\_t len)

Notify attribute value change by UUID.

**Definition** gatt.h:1225

[bt\_gatt\_cb\_register](group__bt__gatt__server.md#ga270c8a52bf3d512defc373f8c29b59f2)

void bt\_gatt\_cb\_register(struct bt\_gatt\_cb \*cb)

Register GATT callbacks.

[bt\_gatt\_attr\_read\_cud](group__bt__gatt__server.md#ga29421c8788b47b6a648704d27d5f0d28)

ssize\_t bt\_gatt\_attr\_read\_cud(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr, void \*buf, uint16\_t len, uint16\_t offset)

Read Characteristic User Description Descriptor Attribute helper.

[bt\_gatt\_attr\_get\_handle](group__bt__gatt__server.md#ga2d51136ea1bd6cdb50900639506fd9f7)

uint16\_t bt\_gatt\_attr\_get\_handle(const struct bt\_gatt\_attr \*attr)

Get Attribute handle.

[bt\_gatt\_attr\_read\_ccc](group__bt__gatt__server.md#ga2e85b42136e2c6a4cb5b7ad8a2532573)

ssize\_t bt\_gatt\_attr\_read\_ccc(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr, void \*buf, uint16\_t len, uint16\_t offset)

Read Client Characteristic Configuration Attribute helper.

[bt\_gatt\_get\_mtu](group__bt__gatt__server.md#ga351fd7658eaecbbfa60f1769119ef733)

uint16\_t bt\_gatt\_get\_mtu(struct bt\_conn \*conn)

Get ATT MTU for a connection.

[bt\_gatt\_attr\_next](group__bt__gatt__server.md#ga35cecaa43b00b374062d29cca1479d85)

struct bt\_gatt\_attr \* bt\_gatt\_attr\_next(const struct bt\_gatt\_attr \*attr)

Iterate to the next attribute.

[bt\_gatt\_attr\_read\_included](group__bt__gatt__server.md#ga4313a63decac2c8b7c4a1764df3d53ea)

ssize\_t bt\_gatt\_attr\_read\_included(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr, void \*buf, uint16\_t len, uint16\_t offset)

Read Include Attribute helper.

[bt\_gatt\_indicate](group__bt__gatt__server.md#ga4f2272692cc0f1d44638828012296c80)

int bt\_gatt\_indicate(struct bt\_conn \*conn, struct bt\_gatt\_indicate\_params \*params)

Indicate attribute value change.

[bt\_gatt\_notify\_cb](group__bt__gatt__server.md#ga55e3ef7cb43b8acb0a27643c78390146)

int bt\_gatt\_notify\_cb(struct bt\_conn \*conn, struct bt\_gatt\_notify\_params \*params)

Notify attribute value change.

[bt\_gatt\_attr\_read\_cep](group__bt__gatt__server.md#ga5893166f1b24f437a94ccf1fc57c7917)

ssize\_t bt\_gatt\_attr\_read\_cep(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr, void \*buf, uint16\_t len, uint16\_t offset)

Read Characteristic Extended Properties Attribute helper.

[bt\_gatt\_attr\_read\_cpf](group__bt__gatt__server.md#ga5ae96590a0aaa5c4c3863a4a14d80fdd)

ssize\_t bt\_gatt\_attr\_read\_cpf(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr, void \*buf, uint16\_t len, uint16\_t offset)

Read Characteristic Presentation format Descriptor Attribute helper.

[bt\_gatt\_indicate\_params\_destroy\_t](group__bt__gatt__server.md#ga5d47ed9eaea22c8f00db14329daee8fe)

void(\* bt\_gatt\_indicate\_params\_destroy\_t)(struct bt\_gatt\_indicate\_params \*params)

**Definition** gatt.h:1259

[bt\_gatt\_authorization\_cb\_register](group__bt__gatt__server.md#ga5eee6afc6db391ffeda295d298bf6a56)

int bt\_gatt\_authorization\_cb\_register(const struct bt\_gatt\_authorization\_cb \*cb)

Register GATT authorization callbacks.

[bt\_gatt\_attr\_func\_t](group__bt__gatt__server.md#ga60284611c90729b289fe806524ba9209)

uint8\_t(\* bt\_gatt\_attr\_func\_t)(const struct bt\_gatt\_attr \*attr, uint16\_t handle, void \*user\_data)

Attribute iterator callback.

**Definition** gatt.h:490

[bt\_gatt\_notify](group__bt__gatt__server.md#ga74ee552864c563aa5bc939f37395c14a)

static int bt\_gatt\_notify(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr, const void \*data, uint16\_t len)

Notify attribute value change.

**Definition** gatt.h:1188

[bt\_gatt\_notify\_multiple](group__bt__gatt__server.md#ga8071d6063f85c0a78155f6b2ac2da635)

int bt\_gatt\_notify\_multiple(struct bt\_conn \*conn, uint16\_t num\_params, struct bt\_gatt\_notify\_params params[])

Send multiple notifications in a single PDU.

[bt\_gatt\_attr\_value\_handle](group__bt__gatt__server.md#ga99738cf4f05eae4c6da17cc3420827d8)

uint16\_t bt\_gatt\_attr\_value\_handle(const struct bt\_gatt\_attr \*attr)

Get the handle of the characteristic value descriptor.

[bt\_gatt\_foreach\_attr](group__bt__gatt__server.md#gaa93b5e0f2870ed135447bead903c175a)

static void bt\_gatt\_foreach\_attr(uint16\_t start\_handle, uint16\_t end\_handle, bt\_gatt\_attr\_func\_t func, void \*user\_data)

Attribute iterator.

**Definition** gatt.h:521

[bt\_gatt\_service\_register](group__bt__gatt__server.md#gab4d9cfea04e44445d5dc30ad52842b64)

int bt\_gatt\_service\_register(struct bt\_gatt\_service \*svc)

Register GATT service.

[bt\_gatt\_attr\_write\_ccc](group__bt__gatt__server.md#gabba965b676650a55cb9934072b34c75e)

ssize\_t bt\_gatt\_attr\_write\_ccc(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr, const void \*buf, uint16\_t len, uint16\_t offset, uint8\_t flags)

Write Client Characteristic Configuration Attribute helper.

[bt\_gatt\_is\_subscribed](group__bt__gatt__server.md#gabd4df0a264dae10e43797992a567be7d)

bool bt\_gatt\_is\_subscribed(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr, uint16\_t ccc\_type)

Check if connection have subscribed to attribute.

[BT\_GATT\_CCC\_MAX](group__bt__gatt__server.md#gac1c0a195c1ec1ff2cdd5bf6d0ba6ad00)

#define BT\_GATT\_CCC\_MAX

**Definition** gatt.h:782

[bt\_gatt\_complete\_func\_t](group__bt__gatt__server.md#gac55832607b95f394d26a64ed1cfe5bba)

void(\* bt\_gatt\_complete\_func\_t)(struct bt\_conn \*conn, void \*user\_data)

Notification complete result callback.

**Definition** gatt.h:1062

[bt\_gatt\_attr\_read\_service](group__bt__gatt__server.md#gacae81c0f272bad7e6ac93c0d13b678c6)

ssize\_t bt\_gatt\_attr\_read\_service(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr, void \*buf, uint16\_t len, uint16\_t offset)

Read Service Attribute helper.

[bt\_gatt\_find\_by\_uuid](group__bt__gatt__server.md#gad2f3272b1dc42378104b492ec7caf6b0)

struct bt\_gatt\_attr \* bt\_gatt\_find\_by\_uuid(const struct bt\_gatt\_attr \*attr, uint16\_t attr\_count, const struct bt\_uuid \*uuid)

Find Attribute by UUID.

[bt\_gatt\_attr\_read\_chrc](group__bt__gatt__server.md#gad58b526a06334530c13292d14a11257c)

ssize\_t bt\_gatt\_attr\_read\_chrc(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr, void \*buf, uint16\_t len, uint16\_t offset)

Read Characteristic Attribute helper.

[bt\_gatt\_foreach\_attr\_type](group__bt__gatt__server.md#gad8d8f513004f391167212d7bf9f7ff10)

void bt\_gatt\_foreach\_attr\_type(uint16\_t start\_handle, uint16\_t end\_handle, const struct bt\_uuid \*uuid, const void \*attr\_data, uint16\_t num\_matches, bt\_gatt\_attr\_func\_t func, void \*user\_data)

Attribute iterator by type.

[bt\_gatt\_service\_is\_registered](group__bt__gatt__server.md#gae5c1e8b7bb1e673e228f03d1d084be9a)

bool bt\_gatt\_service\_is\_registered(const struct bt\_gatt\_service \*svc)

Check if GATT service is registered.

[bt\_gatt\_service\_unregister](group__bt__gatt__server.md#gaf5bf0205fad5f7ad187b764d23deba6b)

int bt\_gatt\_service\_unregister(struct bt\_gatt\_service \*svc)

Unregister GATT service.

[bt\_gatt\_attr\_read](group__bt__gatt__server.md#gaf6d253849932b706ec7f303568980dfa)

ssize\_t bt\_gatt\_attr\_read(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr, void \*buf, uint16\_t buf\_len, uint16\_t offset, const void \*value, uint16\_t value\_len)

Generic Read Attribute value helper.

[BT\_GATT\_ITER\_STOP](group__bt__gatt__server.md#ggab94ce0108483b70392b31a621aa0712aaa3f2a25e27c7065a2c7bb2a9ff09542e)

@ BT\_GATT\_ITER\_STOP

**Definition** gatt.h:476

[BT\_GATT\_ITER\_CONTINUE](group__bt__gatt__server.md#ggab94ce0108483b70392b31a621aa0712aaea569feffa4815d3443e12be78c684f5)

@ BT\_GATT\_ITER\_CONTINUE

**Definition** gatt.h:477

[bt\_gatt\_attr\_write\_func\_t](group__bt__gatt.md#ga3fd8527a0f3e8f3699dc0d3b0339eba1)

ssize\_t(\* bt\_gatt\_attr\_write\_func\_t)(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr, const void \*buf, uint16\_t len, uint16\_t offset, uint8\_t flags)

Attribute write callback.

**Definition** gatt.h:163

[bt\_gatt\_attr\_read\_func\_t](group__bt__gatt.md#ga57e36bf94652531964fd4237c203fe7b)

ssize\_t(\* bt\_gatt\_attr\_read\_func\_t)(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr, void \*buf, uint16\_t len, uint16\_t offset)

Attribute read callback.

**Definition** gatt.h:145

[bt\_gatt\_perm](group__bt__gatt.md#ga96e57500d2340a45badb23701cc43833)

bt\_gatt\_perm

GATT attribute permission bit field values.

**Definition** gatt.h:37

[BT\_GATT\_WRITE\_FLAG\_PREPARE](group__bt__gatt.md#gga11c5a2eb0b62de9a2493ad5335fae383a019cf6118a0cfacbfad20c1cc5838383)

@ BT\_GATT\_WRITE\_FLAG\_PREPARE

Attribute prepare write flag.

**Definition** gatt.h:109

[BT\_GATT\_WRITE\_FLAG\_CMD](group__bt__gatt.md#gga11c5a2eb0b62de9a2493ad5335fae383a770df41b7d433e8ce349b19e4657ba78)

@ BT\_GATT\_WRITE\_FLAG\_CMD

Attribute write command flag.

**Definition** gatt.h:116

[BT\_GATT\_WRITE\_FLAG\_EXECUTE](group__bt__gatt.md#gga11c5a2eb0b62de9a2493ad5335fae383ad4e8f43c03da10c15685bd1a0109708b)

@ BT\_GATT\_WRITE\_FLAG\_EXECUTE

Attribute write execute flag.

**Definition** gatt.h:124

[BT\_GATT\_PERM\_READ\_ENCRYPT](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a0d0afe4a6389102f85e355468cb7984d)

@ BT\_GATT\_PERM\_READ\_ENCRYPT

Attribute read permission with encryption.

**Definition** gatt.h:51

[BT\_GATT\_PERM\_WRITE](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a0f611698ca511f565b247a813ea016cf)

@ BT\_GATT\_PERM\_WRITE

Attribute write permission.

**Definition** gatt.h:45

[BT\_GATT\_PERM\_WRITE\_ENCRYPT](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a662b9af6f435d788aa4e6829725f670f)

@ BT\_GATT\_PERM\_WRITE\_ENCRYPT

Attribute write permission with encryption.

**Definition** gatt.h:57

[BT\_GATT\_PERM\_NONE](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a81a1c35d981593c4c0d344dd0f7e898a)

@ BT\_GATT\_PERM\_NONE

No operations supported, e.g.

**Definition** gatt.h:39

[BT\_GATT\_PERM\_READ](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a9afb838c2cef657e9cd035ef27521f17)

@ BT\_GATT\_PERM\_READ

Attribute read permission.

**Definition** gatt.h:42

[BT\_GATT\_PERM\_PREPARE\_WRITE](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833ab384b61f6ead9d140011da917c950d79)

@ BT\_GATT\_PERM\_PREPARE\_WRITE

Attribute prepare write permission.

**Definition** gatt.h:78

[BT\_GATT\_PERM\_WRITE\_LESC](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833ac56183af896e2a58439c625420efca94)

@ BT\_GATT\_PERM\_WRITE\_LESC

Attribute write permission with LE Secure Connection encryption.

**Definition** gatt.h:90

[BT\_GATT\_PERM\_READ\_AUTHEN](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833ad83f4c03608f674c00ebc93e63d08583)

@ BT\_GATT\_PERM\_READ\_AUTHEN

Attribute read permission with authentication.

**Definition** gatt.h:64

[BT\_GATT\_PERM\_WRITE\_AUTHEN](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833add3893c94a788ff2e5256595a533a266)

@ BT\_GATT\_PERM\_WRITE\_AUTHEN

Attribute write permission with authentication.

**Definition** gatt.h:71

[BT\_GATT\_PERM\_READ\_LESC](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833af62e397dfd87fe763b9c9fc1d5072f57)

@ BT\_GATT\_PERM\_READ\_LESC

Attribute read permission with LE Secure Connection encryption.

**Definition** gatt.h:84

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[slist.h](slist_8h.md)

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)

void \* memset(void \*buf, int c, size\_t n)

[bt\_addr\_le\_t](structbt__addr__le__t.md)

Bluetooth LE Device Address.

**Definition** addr.h:49

[bt\_gatt\_attr](structbt__gatt__attr.md)

GATT Attribute structure.

**Definition** gatt.h:169

[bt\_gatt\_attr::read](structbt__gatt__attr.md#a074abc719494ca35997a452f526e7ecc)

bt\_gatt\_attr\_read\_func\_t read

**Definition** gatt.h:172

[bt\_gatt\_attr::perm](structbt__gatt__attr.md#a0849a40254622080d05e8559c4fdb9e2)

uint16\_t perm

Attribute permissions.

**Definition** gatt.h:183

[bt\_gatt\_attr::write](structbt__gatt__attr.md#a1ecd78536067f4bded506e0daccefd35)

bt\_gatt\_attr\_write\_func\_t write

Attribute write callback.

**Definition** gatt.h:174

[bt\_gatt\_attr::uuid](structbt__gatt__attr.md#a6958f507f9ff172018be458ebc86106f)

const struct bt\_uuid \* uuid

Attribute UUID.

**Definition** gatt.h:171

[bt\_gatt\_attr::user\_data](structbt__gatt__attr.md#adeb063fb101fab45dd789c7212c43357)

void \* user\_data

Attribute user data.

**Definition** gatt.h:176

[bt\_gatt\_attr::handle](structbt__gatt__attr.md#aeee42a3d3ca15e40cf11cc0c3fde106b)

uint16\_t handle

Attribute handle.

**Definition** gatt.h:178

[bt\_gatt\_authorization\_cb](structbt__gatt__authorization__cb.md)

GATT authorization callback structure.

**Definition** gatt.h:239

[bt\_gatt\_authorization\_cb::read\_authorize](structbt__gatt__authorization__cb.md#a7b1bcbe10f12c90ee4e3214e36e9c2a3)

bool(\* read\_authorize)(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr)

Authorize the GATT read operation.

**Definition** gatt.h:251

[bt\_gatt\_authorization\_cb::write\_authorize](structbt__gatt__authorization__cb.md#a7c12bd14f87f91e672eaaf92e1aa6e7b)

bool(\* write\_authorize)(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr)

Authorize the GATT write operation.

**Definition** gatt.h:265

[bt\_gatt\_cb](structbt__gatt__cb.md)

GATT callback structure.

**Definition** gatt.h:223

[bt\_gatt\_cb::att\_mtu\_updated](structbt__gatt__cb.md#a93fe1a626ab59c38ef56f02671f88980)

void(\* att\_mtu\_updated)(struct bt\_conn \*conn, uint16\_t tx, uint16\_t rx)

The maximum ATT MTU on a connection has changed.

**Definition** gatt.h:233

[bt\_gatt\_cb::node](structbt__gatt__cb.md#af9fcf17dcea66b1dee8cc5ecd625cdec)

sys\_snode\_t node

**Definition** gatt.h:235

[bt\_gatt\_ccc\_cfg](structbt__gatt__ccc__cfg.md)

GATT CCC configuration entry.

**Definition** gatt.h:786

[bt\_gatt\_ccc\_cfg::value](structbt__gatt__ccc__cfg.md#a92acf7329f66638ac6c657c8eaa795ac)

uint16\_t value

Configuration value.

**Definition** gatt.h:792

[bt\_gatt\_ccc\_cfg::peer](structbt__gatt__ccc__cfg.md#ab316080693b2c4daf5fd45e2c0501c70)

bt\_addr\_le\_t peer

Remote peer address.

**Definition** gatt.h:790

[bt\_gatt\_ccc\_cfg::id](structbt__gatt__ccc__cfg.md#ac17ddefe7ca6dbac921ee4c6f44fbf51)

uint8\_t id

Local identity, BT\_ID\_DEFAULT in most cases.

**Definition** gatt.h:788

[bt\_gatt\_ccc](structbt__gatt__ccc.md)

Client Characteristic Configuration Attribute Value.

**Definition** gatt.h:359

[bt\_gatt\_ccc::flags](structbt__gatt__ccc.md#ac8fa1028c5e87aa025832257b18fa7c3)

uint16\_t flags

Client Characteristic Configuration flags.

**Definition** gatt.h:361

[bt\_gatt\_cep](structbt__gatt__cep.md)

Characteristic Extended Properties Attribute Value.

**Definition** gatt.h:338

[bt\_gatt\_cep::properties](structbt__gatt__cep.md#a317442dc204f7632b0c5da8a8a9a98b5)

uint16\_t properties

Characteristic Extended properties.

**Definition** gatt.h:340

[bt\_gatt\_chrc](structbt__gatt__chrc.md)

Characteristic Attribute Value.

**Definition** gatt.h:324

[bt\_gatt\_chrc::value\_handle](structbt__gatt__chrc.md#a2ca6aec1a621fdfd12142a1188d37bd3)

uint16\_t value\_handle

Characteristic Value handle.

**Definition** gatt.h:328

[bt\_gatt\_chrc::properties](structbt__gatt__chrc.md#a81bb8257052d7c8d03b51acaa51e5011)

uint8\_t properties

Characteristic properties.

**Definition** gatt.h:330

[bt\_gatt\_chrc::uuid](structbt__gatt__chrc.md#af3b4c22ae37b912c8edf58294cc50702)

const struct bt\_uuid \* uuid

Characteristic UUID.

**Definition** gatt.h:326

[bt\_gatt\_cpf](structbt__gatt__cpf.md)

GATT Characteristic Presentation Format Attribute Value.

**Definition** gatt.h:381

[bt\_gatt\_cpf::name\_space](structbt__gatt__cpf.md#a1dfbb9fc1e1397d2abec04b216d7ae33)

uint8\_t name\_space

Name space of the description.

**Definition** gatt.h:391

[bt\_gatt\_cpf::unit](structbt__gatt__cpf.md#a2a9f3d3f72b9acb1ef7f2dc765e5a231)

uint16\_t unit

Unit of the characteristic.

**Definition** gatt.h:389

[bt\_gatt\_cpf::exponent](structbt__gatt__cpf.md#a3690a86c942badb2d2698481b03e436d)

int8\_t exponent

Exponent field to determine how the value of this characteristic is further formatted.

**Definition** gatt.h:387

[bt\_gatt\_cpf::description](structbt__gatt__cpf.md#a3c48dd5ea717fbaf510d13c64a370c06)

uint16\_t description

Description of the characteristic as defined in a higher layer profile.

**Definition** gatt.h:393

[bt\_gatt\_cpf::format](structbt__gatt__cpf.md#ab0ca135a75130b3ffc0c5bf375f3528f)

uint8\_t format

Format of the value of the characteristic.

**Definition** gatt.h:383

[bt\_gatt\_discover\_params](structbt__gatt__discover__params.md)

GATT Discover Attributes parameters.

**Definition** gatt.h:1492

[bt\_gatt\_discover\_params::start\_handle](structbt__gatt__discover__params.md#a0d2604e7c3ee8969cb5096cbf5793fdb)

uint16\_t start\_handle

Included service start handle.

**Definition** gatt.h:1502

[bt\_gatt\_discover\_params::end\_handle](structbt__gatt__discover__params.md#a225868498c34411cc3fc2be8e678e85e)

uint16\_t end\_handle

Included service end handle.

**Definition** gatt.h:1504

[bt\_gatt\_discover\_params::func](structbt__gatt__discover__params.md#a337d7366c12451938f12eec4dc60903e)

bt\_gatt\_discover\_func\_t func

Discover attribute callback.

**Definition** gatt.h:1496

[bt\_gatt\_discover\_params::attr\_handle](structbt__gatt__discover__params.md#a65ca3c9aad7c02d48fd35c4d6f69dc70)

uint16\_t attr\_handle

Include service attribute declaration handle.

**Definition** gatt.h:1500

[bt\_gatt\_discover\_params::uuid](structbt__gatt__discover__params.md#a77d6665c01902e4e23cf8de8a9436262)

const struct bt\_uuid \* uuid

Discover UUID type.

**Definition** gatt.h:1494

[bt\_gatt\_discover\_params::sub\_params](structbt__gatt__discover__params.md#a87b130c520ce50f835d0589fd22a844c)

struct bt\_gatt\_subscribe\_params \* sub\_params

Only for stack-internal use, used for automatic discovery.

**Definition** gatt.h:1515

[bt\_gatt\_discover\_params::type](structbt__gatt__discover__params.md#ab0f056c90954e1246d897019abd1e7fc)

uint8\_t type

Discover type.

**Definition** gatt.h:1512

[bt\_gatt\_discover\_params::chan\_opt](structbt__gatt__discover__params.md#aba7585e3d0eefb323fcde9bcc88e287d)

enum bt\_att\_chan\_opt chan\_opt

**Definition** gatt.h:1518

[bt\_gatt\_exchange\_params](structbt__gatt__exchange__params.md)

GATT Exchange MTU parameters.

**Definition** gatt.h:1361

[bt\_gatt\_exchange\_params::func](structbt__gatt__exchange__params.md#a76f4d3e779da9c725914574ac2e22ad1)

void(\* func)(struct bt\_conn \*conn, uint8\_t err, struct bt\_gatt\_exchange\_params \*params)

Response callback.

**Definition** gatt.h:1363

[bt\_gatt\_include](structbt__gatt__include.md)

Include Attribute Value.

**Definition** gatt.h:213

[bt\_gatt\_include::end\_handle](structbt__gatt__include.md#a54d20cebfd6ba62b692c363acdc25d61)

uint16\_t end\_handle

Service end handle.

**Definition** gatt.h:219

[bt\_gatt\_include::start\_handle](structbt__gatt__include.md#ac7f6c1a8018f483dce14f0fe21031232)

uint16\_t start\_handle

Service start handle.

**Definition** gatt.h:217

[bt\_gatt\_include::uuid](structbt__gatt__include.md#afa028e8daae00e3b1bc0b866c4335af3)

const struct bt\_uuid \* uuid

Service UUID.

**Definition** gatt.h:215

[bt\_gatt\_indicate\_params](structbt__gatt__indicate__params.md)

GATT Indicate Value parameters.

**Definition** gatt.h:1263

[bt\_gatt\_indicate\_params::chan\_opt](structbt__gatt__indicate__params.md#a0e536938123ecb4f3ba6736c1de2a599)

enum bt\_att\_chan\_opt chan\_opt

**Definition** gatt.h:1287

[bt\_gatt\_indicate\_params::len](structbt__gatt__indicate__params.md#a10ad44140371165951eeac18cb3d0e7f)

uint16\_t len

Indicate Value length.

**Definition** gatt.h:1283

[bt\_gatt\_indicate\_params::attr](structbt__gatt__indicate__params.md#acbbee3a71838492416b20bb5cff89801)

const struct bt\_gatt\_attr \* attr

Indicate Attribute object.

**Definition** gatt.h:1275

[bt\_gatt\_indicate\_params::data](structbt__gatt__indicate__params.md#ae1d657512c99d5bba6fc99a450a6da32)

const void \* data

Indicate Value data.

**Definition** gatt.h:1281

[bt\_gatt\_indicate\_params::destroy](structbt__gatt__indicate__params.md#aeb346dc4c0e4a298c66f394d037a6514)

bt\_gatt\_indicate\_params\_destroy\_t destroy

Indicate operation complete callback.

**Definition** gatt.h:1279

[bt\_gatt\_indicate\_params::func](structbt__gatt__indicate__params.md#af9eb83c3fba49ee3cd6162d5a2791707)

bt\_gatt\_indicate\_func\_t func

Indicate Value callback.

**Definition** gatt.h:1277

[bt\_gatt\_indicate\_params::uuid](structbt__gatt__indicate__params.md#afde06f47d7a817291e437593ea01bccd)

const struct bt\_uuid \* uuid

Indicate Attribute UUID type.

**Definition** gatt.h:1269

[bt\_gatt\_notify\_params](structbt__gatt__notify__params.md)

**Definition** gatt.h:1064

[bt\_gatt\_notify\_params::uuid](structbt__gatt__notify__params.md#a2994cbe737fad725c60427000c21c373)

const struct bt\_uuid \* uuid

Notification Attribute UUID type.

**Definition** gatt.h:1070

[bt\_gatt\_notify\_params::len](structbt__gatt__notify__params.md#a4a511da0b099ca88d895594caf7aaa6a)

uint16\_t len

Notification Value length.

**Definition** gatt.h:1080

[bt\_gatt\_notify\_params::attr](structbt__gatt__notify__params.md#a6187d0457763a15a623129e3e9e98e13)

const struct bt\_gatt\_attr \* attr

Notification Attribute object.

**Definition** gatt.h:1076

[bt\_gatt\_notify\_params::chan\_opt](structbt__gatt__notify__params.md#a978d7a42c39a098cedf751936f280fac)

enum bt\_att\_chan\_opt chan\_opt

**Definition** gatt.h:1086

[bt\_gatt\_notify\_params::func](structbt__gatt__notify__params.md#ace3c6b5f5ed78b9f64c25b868d3bfbe2)

bt\_gatt\_complete\_func\_t func

Notification Value callback.

**Definition** gatt.h:1082

[bt\_gatt\_notify\_params::user\_data](structbt__gatt__notify__params.md#adec9a6f6ea0604e82b90dd47bb9951fa)

void \* user\_data

Notification Value callback user data.

**Definition** gatt.h:1084

[bt\_gatt\_notify\_params::data](structbt__gatt__notify__params.md#afaa276cff9cbf204c433ca776904ef32)

const void \* data

Notification Value data.

**Definition** gatt.h:1078

[bt\_gatt\_read\_params](structbt__gatt__read__params.md)

GATT Read parameters.

**Definition** gatt.h:1583

[bt\_gatt\_read\_params::handle\_count](structbt__gatt__read__params.md#a0a36063ac0b110fbf57ef6a66f7bece8)

size\_t handle\_count

If equals to 1 single.handle and single.offset are used.

**Definition** gatt.h:1590

[bt\_gatt\_read\_params::chan\_opt](structbt__gatt__read__params.md#a1335d1f9aefeff89a57efe78335cb41b)

enum bt\_att\_chan\_opt chan\_opt

**Definition** gatt.h:1625

[bt\_gatt\_read\_params::single](structbt__gatt__read__params.md#a1ff7320ad5b67fff803ecd1a4e801b84)

struct bt\_gatt\_read\_params::@261011265054333145327063036013076000041270205077::@014103030255120232336162043075024363164026324042 single

[bt\_gatt\_read\_params::handles](structbt__gatt__read__params.md#a2794b8806933d0e16cfc77f4087fdeda)

uint16\_t \* handles

Attribute handles to read with Read Multiple Characteristic Values.

**Definition** gatt.h:1602

[bt\_gatt\_read\_params::offset](structbt__gatt__read__params.md#a27f685a45c405bb2784fe369513724ad)

uint16\_t offset

Attribute data offset.

**Definition** gatt.h:1596

[bt\_gatt\_read\_params::func](structbt__gatt__read__params.md#a3ea107db0b7537c9dccb2aa6d8f916fb)

bt\_gatt\_read\_func\_t func

Read attribute callback.

**Definition** gatt.h:1585

[bt\_gatt\_read\_params::variable](structbt__gatt__read__params.md#a77d05cbc54b125fc35d180cf91bf9cb9)

bool variable

If true use Read Multiple Variable Length Characteristic Values procedure.

**Definition** gatt.h:1613

[bt\_gatt\_read\_params::by\_uuid](structbt__gatt__read__params.md#a790606149a7619dd4338a6c6e7d24eaa)

struct bt\_gatt\_read\_params::@261011265054333145327063036013076000041270205077::@225064320074250320152102140230075031204036137360 by\_uuid

[bt\_gatt\_read\_params::end\_handle](structbt__gatt__read__params.md#a8b2a2b912efe557e24276a654087e75c)

uint16\_t end\_handle

Last requested handle number.

**Definition** gatt.h:1619

[bt\_gatt\_read\_params::start\_handle](structbt__gatt__read__params.md#ac11db1652cd5cee567d666d3697f3a4b)

uint16\_t start\_handle

First requested handle number.

**Definition** gatt.h:1617

[bt\_gatt\_read\_params::multiple](structbt__gatt__read__params.md#adc0e62e7ee39e034193f347f79b436d7)

struct bt\_gatt\_read\_params::@261011265054333145327063036013076000041270205077::@270001321042100045315333245270042352035110262201 multiple

[bt\_gatt\_read\_params::uuid](structbt__gatt__read__params.md#ae2ba6ce4043769b86a050fd767248111)

const struct bt\_uuid \* uuid

2 or 16 octet UUID.

**Definition** gatt.h:1621

[bt\_gatt\_read\_params::handle](structbt__gatt__read__params.md#af37beb6a69b3a6b90da0594b099bd64d)

uint16\_t handle

Attribute handle.

**Definition** gatt.h:1594

[bt\_gatt\_scc](structbt__gatt__scc.md)

Server Characteristic Configuration Attribute Value.

**Definition** gatt.h:375

[bt\_gatt\_scc::flags](structbt__gatt__scc.md#aa7ddf1810f6d47e59c364b7489823d00)

uint16\_t flags

Server Characteristic Configuration flags.

**Definition** gatt.h:377

[bt\_gatt\_service\_static](structbt__gatt__service__static.md)

GATT Service structure.

**Definition** gatt.h:187

[bt\_gatt\_service\_static::attrs](structbt__gatt__service__static.md#a38f9e02241fe37f68df5dd8782b59e9f)

const struct bt\_gatt\_attr \* attrs

Service Attributes.

**Definition** gatt.h:189

[bt\_gatt\_service\_static::attr\_count](structbt__gatt__service__static.md#a84c35a391e372396e2ec89eaf0d4d047)

size\_t attr\_count

Service Attribute count.

**Definition** gatt.h:191

[bt\_gatt\_service\_val](structbt__gatt__service__val.md)

Service Attribute Value.

**Definition** gatt.h:205

[bt\_gatt\_service\_val::uuid](structbt__gatt__service__val.md#a683e01db92400e76aed32b7a81369a55)

const struct bt\_uuid \* uuid

Service UUID.

**Definition** gatt.h:207

[bt\_gatt\_service\_val::end\_handle](structbt__gatt__service__val.md#a75b6fcf0f9f29ad05ccac0e83bcb31b7)

uint16\_t end\_handle

Service end handle.

**Definition** gatt.h:209

[bt\_gatt\_service](structbt__gatt__service.md)

GATT Service structure.

**Definition** gatt.h:195

[bt\_gatt\_service::attrs](structbt__gatt__service.md#a0281e96ab54519df641f6c489fdc6b5b)

struct bt\_gatt\_attr \* attrs

Service Attributes.

**Definition** gatt.h:197

[bt\_gatt\_service::attr\_count](structbt__gatt__service.md#a87d8316a92ae04678d7be0ae76ed86cb)

size\_t attr\_count

Service Attribute count.

**Definition** gatt.h:199

[bt\_gatt\_service::node](structbt__gatt__service.md#a8ce51bcd55e4f9a80a00bcac2c20b2d1)

sys\_snode\_t node

**Definition** gatt.h:201

[bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md)

GATT Subscribe parameters.

**Definition** gatt.h:1881

[bt\_gatt\_subscribe\_params::write](structbt__gatt__subscribe__params.md#a1cedb0e0067c8648c603296a63d2e3ee)

bt\_gatt\_write\_func\_t write

**Definition** gatt.h:1890

[bt\_gatt\_subscribe\_params::value](structbt__gatt__subscribe__params.md#a3bff1209b7a0b5908408a568622d0150)

uint16\_t value

Subscribe value.

**Definition** gatt.h:1902

[bt\_gatt\_subscribe\_params::min\_security](structbt__gatt__subscribe__params.md#a5b34bad1cf39bb3efd5faf516473dd4a)

bt\_security\_t min\_security

Minimum required security for received notification.

**Definition** gatt.h:1908

[bt\_gatt\_subscribe\_params::ccc\_handle](structbt__gatt__subscribe__params.md#a77c53cdfd4143483b33a8ecf6061561e)

uint16\_t ccc\_handle

Subscribe CCC handle.

**Definition** gatt.h:1894

[bt\_gatt\_subscribe\_params::subscribe](structbt__gatt__subscribe__params.md#a91595407b8de4e862652e41100668f0a)

bt\_gatt\_subscribe\_func\_t subscribe

Subscribe CCC write request response callback If given, called with the subscription parameters given...

**Definition** gatt.h:1887

[bt\_gatt\_subscribe\_params::value\_handle](structbt__gatt__subscribe__params.md#a9248418eb04a5b7a0faed5077c40bf22)

uint16\_t value\_handle

Subscribe value handle.

**Definition** gatt.h:1892

[bt\_gatt\_subscribe\_params::node](structbt__gatt__subscribe__params.md#acbc7c9d38361e3b702fdf5efd7383b34)

sys\_snode\_t node

**Definition** gatt.h:1913

[bt\_gatt\_subscribe\_params::notify](structbt__gatt__subscribe__params.md#acf237ef097e8b847eb049fb0a5d4b759)

bt\_gatt\_notify\_func\_t notify

Notification value callback.

**Definition** gatt.h:1883

[bt\_gatt\_subscribe\_params::disc\_params](structbt__gatt__subscribe__params.md#ad3a3b9335b85777d65bdf875486e292a)

struct bt\_gatt\_discover\_params \* disc\_params

Discover parameters used when ccc\_handle = 0.

**Definition** gatt.h:1899

[bt\_gatt\_subscribe\_params::chan\_opt](structbt__gatt__subscribe__params.md#ae139848da09705d37fe7c9de4c1a4087)

enum bt\_att\_chan\_opt chan\_opt

**Definition** gatt.h:1915

[bt\_gatt\_subscribe\_params::flags](structbt__gatt__subscribe__params.md#aedd24024881e22372505355024cd716b)

atomic\_t flags[ATOMIC\_BITMAP\_SIZE(BT\_GATT\_SUBSCRIBE\_NUM\_FLAGS)]

Subscription flags.

**Definition** gatt.h:1911

[bt\_gatt\_subscribe\_params::end\_handle](structbt__gatt__subscribe__params.md#af806d24aa97db1f2e9a021e719598a6d)

uint16\_t end\_handle

Subscribe End handle (for automatic discovery).

**Definition** gatt.h:1897

[bt\_gatt\_write\_params](structbt__gatt__write__params.md)

GATT Write parameters.

**Definition** gatt.h:1688

[bt\_gatt\_write\_params::func](structbt__gatt__write__params.md#a3468e3b75f3f9eda12bc4963f48cf9aa)

bt\_gatt\_write\_func\_t func

Response callback.

**Definition** gatt.h:1690

[bt\_gatt\_write\_params::handle](structbt__gatt__write__params.md#a384c5c15f248df5b327423ca32637bad)

uint16\_t handle

Attribute handle.

**Definition** gatt.h:1692

[bt\_gatt\_write\_params::data](structbt__gatt__write__params.md#ab6510ef242e73325adb074322746c27c)

const void \* data

Data to be written.

**Definition** gatt.h:1696

[bt\_gatt\_write\_params::chan\_opt](structbt__gatt__write__params.md#ad79905c16f7ba5289817de552ece1a48)

enum bt\_att\_chan\_opt chan\_opt

**Definition** gatt.h:1700

[bt\_gatt\_write\_params::offset](structbt__gatt__write__params.md#add53cc08465d28f33bc48a1e8649ac1a)

uint16\_t offset

Attribute data offset.

**Definition** gatt.h:1694

[bt\_gatt\_write\_params::length](structbt__gatt__write__params.md#aded956dac2d398b642faeec81fdb9ec3)

uint16\_t length

Length of the data.

**Definition** gatt.h:1698

[bt\_uuid](structbt__uuid.md)

This is a 'tentative' type and should be used as a pointer only.

**Definition** uuid.h:49

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[util.h](util_8h.md)

Misc utilities.

[uuid.h](uuid_8h.md)

Bluetooth UUID handling.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [gatt.h](gatt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

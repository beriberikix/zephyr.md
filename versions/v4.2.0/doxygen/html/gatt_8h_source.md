---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/gatt_8h_source.html
original_path: doxygen/html/gatt_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

22

23#include <[stdint.h](stdint_8h.md)>

24#include <stddef.h>

25#include <[string.h](string_8h.md)>

26

27#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

28

29#include <zephyr/autoconf.h>

30#include <[zephyr/bluetooth/addr.h](addr_8h.md)>

31#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

32#include <[zephyr/bluetooth/uuid.h](bluetooth_2uuid_8h.md)>

33#include <[zephyr/bluetooth/att.h](att_8h.md)>

34#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

35#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

36#include <[zephyr/sys/slist.h](slist_8h.md)>

37#include <[zephyr/sys/util.h](sys_2util_8h.md)>

38#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

39#include <[zephyr/toolchain.h](toolchain_8h.md)>

40

41#ifdef \_\_cplusplus

42extern "C" {

43#endif

44

[ 46](group__bt__gatt.md#ga96e57500d2340a45badb23701cc43833)enum [bt\_gatt\_perm](group__bt__gatt.md#ga96e57500d2340a45badb23701cc43833) {

[ 48](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a81a1c35d981593c4c0d344dd0f7e898a) [BT\_GATT\_PERM\_NONE](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a81a1c35d981593c4c0d344dd0f7e898a) = 0,

49

[ 51](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a9afb838c2cef657e9cd035ef27521f17) [BT\_GATT\_PERM\_READ](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a9afb838c2cef657e9cd035ef27521f17) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

52

[ 54](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a0f611698ca511f565b247a813ea016cf) [BT\_GATT\_PERM\_WRITE](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a0f611698ca511f565b247a813ea016cf) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

55

[ 60](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a0d0afe4a6389102f85e355468cb7984d) [BT\_GATT\_PERM\_READ\_ENCRYPT](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a0d0afe4a6389102f85e355468cb7984d) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

61

[ 66](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a662b9af6f435d788aa4e6829725f670f) [BT\_GATT\_PERM\_WRITE\_ENCRYPT](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a662b9af6f435d788aa4e6829725f670f) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

67

[ 73](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833ad83f4c03608f674c00ebc93e63d08583) [BT\_GATT\_PERM\_READ\_AUTHEN](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833ad83f4c03608f674c00ebc93e63d08583) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

74

[ 80](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833add3893c94a788ff2e5256595a533a266) [BT\_GATT\_PERM\_WRITE\_AUTHEN](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833add3893c94a788ff2e5256595a533a266) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

81

[ 87](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833ab384b61f6ead9d140011da917c950d79) [BT\_GATT\_PERM\_PREPARE\_WRITE](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833ab384b61f6ead9d140011da917c950d79) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

88

[ 93](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833af62e397dfd87fe763b9c9fc1d5072f57) [BT\_GATT\_PERM\_READ\_LESC](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833af62e397dfd87fe763b9c9fc1d5072f57) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

94

[ 99](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833ac56183af896e2a58439c625420efca94) [BT\_GATT\_PERM\_WRITE\_LESC](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833ac56183af896e2a58439c625420efca94) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8),

100};

101

[ 109](group__bt__gatt.md#gaff31756c1bf8ee755e65b1e0fb689bb7)#define BT\_GATT\_ERR(\_att\_err) (-(\_att\_err))

110

[ 112](group__bt__gatt.md#ga830d437c8d0757f53af1de6aa3031906)enum [bt\_gatt\_attr\_write\_flag](group__bt__gatt.md#ga830d437c8d0757f53af1de6aa3031906) {

[ 118](group__bt__gatt.md#gga830d437c8d0757f53af1de6aa3031906a019cf6118a0cfacbfad20c1cc5838383) [BT\_GATT\_WRITE\_FLAG\_PREPARE](group__bt__gatt.md#gga830d437c8d0757f53af1de6aa3031906a019cf6118a0cfacbfad20c1cc5838383) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

119

[ 125](group__bt__gatt.md#gga830d437c8d0757f53af1de6aa3031906a770df41b7d433e8ce349b19e4657ba78) [BT\_GATT\_WRITE\_FLAG\_CMD](group__bt__gatt.md#gga830d437c8d0757f53af1de6aa3031906a770df41b7d433e8ce349b19e4657ba78) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

126

[ 133](group__bt__gatt.md#gga830d437c8d0757f53af1de6aa3031906ad4e8f43c03da10c15685bd1a0109708b) [BT\_GATT\_WRITE\_FLAG\_EXECUTE](group__bt__gatt.md#gga830d437c8d0757f53af1de6aa3031906ad4e8f43c03da10c15685bd1a0109708b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

134};

135

136/\* Forward declaration of GATT Attribute structure \*/

137struct [bt\_gatt\_attr](structbt__gatt__attr.md);

138

[ 169](group__bt__gatt.md#ga57e36bf94652531964fd4237c203fe7b)typedef [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[bt\_gatt\_attr\_read\_func\_t](group__bt__gatt.md#ga57e36bf94652531964fd4237c203fe7b))(struct bt\_conn \*conn,

170 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr,

171 void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len,

172 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset);

173

[ 212](group__bt__gatt.md#ga3fd8527a0f3e8f3699dc0d3b0339eba1)typedef [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[bt\_gatt\_attr\_write\_func\_t](group__bt__gatt.md#ga3fd8527a0f3e8f3699dc0d3b0339eba1))(struct bt\_conn \*conn,

213 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr,

214 const void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len,

215 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

216

[ 227](structbt__gatt__attr.md)struct [bt\_gatt\_attr](structbt__gatt__attr.md) {

[ 241](structbt__gatt__attr.md#a6958f507f9ff172018be458ebc86106f) const struct [bt\_uuid](structbt__uuid.md) \*[uuid](structbt__gatt__attr.md#a6958f507f9ff172018be458ebc86106f);

242

[ 254](structbt__gatt__attr.md#a074abc719494ca35997a452f526e7ecc) [bt\_gatt\_attr\_read\_func\_t](group__bt__gatt.md#ga57e36bf94652531964fd4237c203fe7b) [read](structbt__gatt__attr.md#a074abc719494ca35997a452f526e7ecc);

255

[ 267](structbt__gatt__attr.md#a1ecd78536067f4bded506e0daccefd35) [bt\_gatt\_attr\_write\_func\_t](group__bt__gatt.md#ga3fd8527a0f3e8f3699dc0d3b0339eba1) [write](structbt__gatt__attr.md#a1ecd78536067f4bded506e0daccefd35);

268

[ 280](structbt__gatt__attr.md#adeb063fb101fab45dd789c7212c43357) void \*[user\_data](structbt__gatt__attr.md#adeb063fb101fab45dd789c7212c43357);

281

[ 290](structbt__gatt__attr.md#aeee42a3d3ca15e40cf11cc0c3fde106b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__gatt__attr.md#aeee42a3d3ca15e40cf11cc0c3fde106b);

291

[ 299](structbt__gatt__attr.md#a0849a40254622080d05e8559c4fdb9e2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [perm](structbt__gatt__attr.md#a0849a40254622080d05e8559c4fdb9e2): 15;

300

309 bool \_auto\_assigned\_handle: 1;

311};

312

[ 319](structbt__gatt__service__static.md)struct [bt\_gatt\_service\_static](structbt__gatt__service__static.md) {

[ 321](structbt__gatt__service__static.md#a38f9e02241fe37f68df5dd8782b59e9f) const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*[attrs](structbt__gatt__service__static.md#a38f9e02241fe37f68df5dd8782b59e9f);

[ 323](structbt__gatt__service__static.md#a84c35a391e372396e2ec89eaf0d4d047) size\_t [attr\_count](structbt__gatt__service__static.md#a84c35a391e372396e2ec89eaf0d4d047);

324};

325

[ 332](structbt__gatt__service.md)struct [bt\_gatt\_service](structbt__gatt__service.md) {

[ 334](structbt__gatt__service.md#a0281e96ab54519df641f6c489fdc6b5b) struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*[attrs](structbt__gatt__service.md#a0281e96ab54519df641f6c489fdc6b5b);

[ 336](structbt__gatt__service.md#a87d8316a92ae04678d7be0ae76ed86cb) size\_t [attr\_count](structbt__gatt__service.md#a87d8316a92ae04678d7be0ae76ed86cb);

340 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

342};

343

[ 349](structbt__gatt__service__val.md)struct [bt\_gatt\_service\_val](structbt__gatt__service__val.md) {

[ 351](structbt__gatt__service__val.md#a683e01db92400e76aed32b7a81369a55) const struct [bt\_uuid](structbt__uuid.md) \*[uuid](structbt__gatt__service__val.md#a683e01db92400e76aed32b7a81369a55);

[ 353](structbt__gatt__service__val.md#a75b6fcf0f9f29ad05ccac0e83bcb31b7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [end\_handle](structbt__gatt__service__val.md#a75b6fcf0f9f29ad05ccac0e83bcb31b7);

354};

355

[ 362](structbt__gatt__include.md)struct [bt\_gatt\_include](structbt__gatt__include.md) {

[ 364](structbt__gatt__include.md#afa028e8daae00e3b1bc0b866c4335af3) const struct [bt\_uuid](structbt__uuid.md) \*[uuid](structbt__gatt__include.md#afa028e8daae00e3b1bc0b866c4335af3);

[ 366](structbt__gatt__include.md#ac7f6c1a8018f483dce14f0fe21031232) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [start\_handle](structbt__gatt__include.md#ac7f6c1a8018f483dce14f0fe21031232);

[ 368](structbt__gatt__include.md#a54d20cebfd6ba62b692c363acdc25d61) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [end\_handle](structbt__gatt__include.md#a54d20cebfd6ba62b692c363acdc25d61);

369};

370

[ 372](structbt__gatt__cb.md)struct [bt\_gatt\_cb](structbt__gatt__cb.md) {

[ 382](structbt__gatt__cb.md#a93fe1a626ab59c38ef56f02671f88980) void (\*[att\_mtu\_updated](structbt__gatt__cb.md#a93fe1a626ab59c38ef56f02671f88980))(struct bt\_conn \*conn, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) rx);

383

387 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

389};

390

[ 392](structbt__gatt__authorization__cb.md)struct [bt\_gatt\_authorization\_cb](structbt__gatt__authorization__cb.md) {

[ 404](structbt__gatt__authorization__cb.md#a7b1bcbe10f12c90ee4e3214e36e9c2a3) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[read\_authorize](structbt__gatt__authorization__cb.md#a7b1bcbe10f12c90ee4e3214e36e9c2a3))(struct bt\_conn \*conn,

405 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr);

406

[ 418](structbt__gatt__authorization__cb.md#a7c12bd14f87f91e672eaaf92e1aa6e7b) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[write\_authorize](structbt__gatt__authorization__cb.md#a7c12bd14f87f91e672eaaf92e1aa6e7b))(struct bt\_conn \*conn,

419 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr);

420};

421

423

[ 430](group__bt__gatt.md#ga86bddd8211e7466b0457173a0dd412f0)#define BT\_GATT\_CHRC\_BROADCAST 0x01

[ 436](group__bt__gatt.md#gaa243a11d6d8b3e3be815c0893e0220f3)#define BT\_GATT\_CHRC\_READ 0x02

[ 442](group__bt__gatt.md#ga9c029ca574eb3c5992685b279388ac85)#define BT\_GATT\_CHRC\_WRITE\_WITHOUT\_RESP 0x04

[ 448](group__bt__gatt.md#gad482d8db34707e1f9da1d8e2ddd5507e)#define BT\_GATT\_CHRC\_WRITE 0x08

[ 455](group__bt__gatt.md#gab8cd9649bdfd125a26065a8ced762a98)#define BT\_GATT\_CHRC\_NOTIFY 0x10

[ 461](group__bt__gatt.md#gaa9639b9d655ea41767584b638add1f2b)#define BT\_GATT\_CHRC\_INDICATE 0x20

[ 467](group__bt__gatt.md#gaab3a26a00f88a6eacd36f2841004204c)#define BT\_GATT\_CHRC\_AUTH 0x40

[ 474](group__bt__gatt.md#gac84d73a0ad50bfd149ad83181315de1a)#define BT\_GATT\_CHRC\_EXT\_PROP 0x80

475

[ 481](structbt__gatt__chrc.md)struct [bt\_gatt\_chrc](structbt__gatt__chrc.md) {

[ 483](structbt__gatt__chrc.md#af3b4c22ae37b912c8edf58294cc50702) const struct [bt\_uuid](structbt__uuid.md) \*[uuid](structbt__gatt__chrc.md#af3b4c22ae37b912c8edf58294cc50702);

[ 485](structbt__gatt__chrc.md#a2ca6aec1a621fdfd12142a1188d37bd3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [value\_handle](structbt__gatt__chrc.md#a2ca6aec1a621fdfd12142a1188d37bd3);

[ 487](structbt__gatt__chrc.md#a81bb8257052d7c8d03b51acaa51e5011) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [properties](structbt__gatt__chrc.md#a81bb8257052d7c8d03b51acaa51e5011);

488};

489

[ 491](group__bt__gatt.md#gad1825f8deafc36d7e8f09c2835884fc6)#define BT\_GATT\_CEP\_RELIABLE\_WRITE 0x0001

[ 492](group__bt__gatt.md#ga64898ec8390c89c1fc5bdf0364220a43)#define BT\_GATT\_CEP\_WRITABLE\_AUX 0x0002

493

[ 501](structbt__gatt__cep.md)struct [bt\_gatt\_cep](structbt__gatt__cep.md) {

[ 503](structbt__gatt__cep.md#a317442dc204f7632b0c5da8a8a9a98b5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [properties](structbt__gatt__cep.md#a317442dc204f7632b0c5da8a8a9a98b5);

504};

505

507

[ 513](group__bt__gatt.md#ga240a10df32aa7a256a103ceee7211f8d)#define BT\_GATT\_CCC\_NOTIFY 0x0001

[ 519](group__bt__gatt.md#ga60ff2ddcc2e3148881a2f15745ba06e8)#define BT\_GATT\_CCC\_INDICATE 0x0002

520

[ 525](structbt__gatt__ccc.md)struct [bt\_gatt\_ccc](structbt__gatt__ccc.md) {

[ 527](structbt__gatt__ccc.md#ac8fa1028c5e87aa025832257b18fa7c3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](structbt__gatt__ccc.md#ac8fa1028c5e87aa025832257b18fa7c3);

528};

529

531

[ 538](group__bt__gatt.md#ga7a7d3cfa6eec4baa0b57ec9c4bc41f7a)#define BT\_GATT\_SCC\_BROADCAST 0x0001

539

[ 544](structbt__gatt__scc.md)struct [bt\_gatt\_scc](structbt__gatt__scc.md) {

[ 546](structbt__gatt__scc.md#aa7ddf1810f6d47e59c364b7489823d00) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](structbt__gatt__scc.md#aa7ddf1810f6d47e59c364b7489823d00);

547};

548

[ 554](structbt__gatt__cpf.md)struct [bt\_gatt\_cpf](structbt__gatt__cpf.md) {

[ 560](structbt__gatt__cpf.md#ab0ca135a75130b3ffc0c5bf375f3528f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [format](structbt__gatt__cpf.md#ab0ca135a75130b3ffc0c5bf375f3528f);

[ 566](structbt__gatt__cpf.md#a3690a86c942badb2d2698481b03e436d) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [exponent](structbt__gatt__cpf.md#a3690a86c942badb2d2698481b03e436d);

[ 572](structbt__gatt__cpf.md#a2a9f3d3f72b9acb1ef7f2dc765e5a231) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [unit](structbt__gatt__cpf.md#a2a9f3d3f72b9acb1ef7f2dc765e5a231);

[ 579](structbt__gatt__cpf.md#a1dfbb9fc1e1397d2abec04b216d7ae33) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [name\_space](structbt__gatt__cpf.md#a1dfbb9fc1e1397d2abec04b216d7ae33);

[ 586](structbt__gatt__cpf.md#a3c48dd5ea717fbaf510d13c64a370c06) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [description](structbt__gatt__cpf.md#a3c48dd5ea717fbaf510d13c64a370c06);

587};

588

594

[ 611](group__bt__gatt__server.md#gaf6d3f1e904f1a847afeb30236bad98a2)static inline const char \*[bt\_gatt\_err\_to\_str](group__bt__gatt__server.md#gaf6d3f1e904f1a847afeb30236bad98a2)(int gatt\_err)

612{

613 return [bt\_att\_err\_to\_str](group__bt__att.md#gad2305f28744276d97aefd26bdb79023c)((gatt\_err) < 0 ? -(gatt\_err) : (gatt\_err));

614}

615

[ 623](group__bt__gatt__server.md#ga270c8a52bf3d512defc373f8c29b59f2)void [bt\_gatt\_cb\_register](group__bt__gatt__server.md#ga270c8a52bf3d512defc373f8c29b59f2)(struct [bt\_gatt\_cb](structbt__gatt__cb.md) \*cb);

624

[ 643](group__bt__gatt__server.md#ga5eee6afc6db391ffeda295d298bf6a56)int [bt\_gatt\_authorization\_cb\_register](group__bt__gatt__server.md#ga5eee6afc6db391ffeda295d298bf6a56)(const struct [bt\_gatt\_authorization\_cb](structbt__gatt__authorization__cb.md) \*cb);

644

[ 671](group__bt__gatt__server.md#gab4d9cfea04e44445d5dc30ad52842b64)int [bt\_gatt\_service\_register](group__bt__gatt__server.md#gab4d9cfea04e44445d5dc30ad52842b64)(struct [bt\_gatt\_service](structbt__gatt__service.md) \*svc);

672

[ 679](group__bt__gatt__server.md#gaf5bf0205fad5f7ad187b764d23deba6b)int [bt\_gatt\_service\_unregister](group__bt__gatt__server.md#gaf5bf0205fad5f7ad187b764d23deba6b)(struct [bt\_gatt\_service](structbt__gatt__service.md) \*svc);

680

[ 687](group__bt__gatt__server.md#gae5c1e8b7bb1e673e228f03d1d084be9a)bool [bt\_gatt\_service\_is\_registered](group__bt__gatt__server.md#gae5c1e8b7bb1e673e228f03d1d084be9a)(const struct [bt\_gatt\_service](structbt__gatt__service.md) \*svc);

688

[ 692](group__bt__gatt__server.md#gab38994257f53473e62e01eff8f236ee1)enum [bt\_gatt\_iter](group__bt__gatt__server.md#gab38994257f53473e62e01eff8f236ee1) {

[ 693](group__bt__gatt__server.md#ggab38994257f53473e62e01eff8f236ee1aa3f2a25e27c7065a2c7bb2a9ff09542e) [BT\_GATT\_ITER\_STOP](group__bt__gatt__server.md#ggab38994257f53473e62e01eff8f236ee1aa3f2a25e27c7065a2c7bb2a9ff09542e) = 0,

[ 694](group__bt__gatt__server.md#ggab38994257f53473e62e01eff8f236ee1aea569feffa4815d3443e12be78c684f5) [BT\_GATT\_ITER\_CONTINUE](group__bt__gatt__server.md#ggab38994257f53473e62e01eff8f236ee1aea569feffa4815d3443e12be78c684f5),

695};

696

[ 707](group__bt__gatt__server.md#ga60284611c90729b289fe806524ba9209)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) (\*[bt\_gatt\_attr\_func\_t](group__bt__gatt__server.md#ga60284611c90729b289fe806524ba9209))(const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr,

708 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__gatt__attr.md#aeee42a3d3ca15e40cf11cc0c3fde106b),

709 void \*[user\_data](structbt__gatt__attr.md#adeb063fb101fab45dd789c7212c43357));

710

[ 724](group__bt__gatt__server.md#gad8d8f513004f391167212d7bf9f7ff10)void [bt\_gatt\_foreach\_attr\_type](group__bt__gatt__server.md#gad8d8f513004f391167212d7bf9f7ff10)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_handle, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) end\_handle,

725 const struct [bt\_uuid](structbt__uuid.md) \*[uuid](structuuid.md),

726 const void \*attr\_data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_matches,

727 [bt\_gatt\_attr\_func\_t](group__bt__gatt__server.md#ga60284611c90729b289fe806524ba9209) func,

728 void \*[user\_data](structbt__gatt__attr.md#adeb063fb101fab45dd789c7212c43357));

729

[ 739](group__bt__gatt__server.md#gaa93b5e0f2870ed135447bead903c175a)static inline void [bt\_gatt\_foreach\_attr](group__bt__gatt__server.md#gaa93b5e0f2870ed135447bead903c175a)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_handle, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) end\_handle,

740 [bt\_gatt\_attr\_func\_t](group__bt__gatt__server.md#ga60284611c90729b289fe806524ba9209) func,

741 void \*[user\_data](structbt__gatt__attr.md#adeb063fb101fab45dd789c7212c43357))

742{

743 [bt\_gatt\_foreach\_attr\_type](group__bt__gatt__server.md#gad8d8f513004f391167212d7bf9f7ff10)(start\_handle, end\_handle, [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), 0, func,

744 [user\_data](structbt__gatt__attr.md#adeb063fb101fab45dd789c7212c43357));

745}

746

[ 755](group__bt__gatt__server.md#ga35cecaa43b00b374062d29cca1479d85)struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*[bt\_gatt\_attr\_next](group__bt__gatt__server.md#ga35cecaa43b00b374062d29cca1479d85)(const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr);

756

[ 771](group__bt__gatt__server.md#gad2f3272b1dc42378104b492ec7caf6b0)struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*[bt\_gatt\_find\_by\_uuid](group__bt__gatt__server.md#gad2f3272b1dc42378104b492ec7caf6b0)(const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr,

772 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) attr\_count,

773 const struct [bt\_uuid](structbt__uuid.md) \*[uuid](structuuid.md));

774

[ 783](group__bt__gatt__server.md#ga2d51136ea1bd6cdb50900639506fd9f7)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [bt\_gatt\_attr\_get\_handle](group__bt__gatt__server.md#ga2d51136ea1bd6cdb50900639506fd9f7)(const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr);

784

[ 796](group__bt__gatt__server.md#ga99738cf4f05eae4c6da17cc3420827d8)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [bt\_gatt\_attr\_value\_handle](group__bt__gatt__server.md#ga99738cf4f05eae4c6da17cc3420827d8)(const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr);

797

[ 813](group__bt__gatt__server.md#gaf6d253849932b706ec7f303568980dfa)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [bt\_gatt\_attr\_read](group__bt__gatt__server.md#gaf6d253849932b706ec7f303568980dfa)(struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr,

814 void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) buf\_len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset,

815 const void \*value, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) value\_len);

816

[ 832](group__bt__gatt__server.md#gacae81c0f272bad7e6ac93c0d13b678c6)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [bt\_gatt\_attr\_read\_service](group__bt__gatt__server.md#gacae81c0f272bad7e6ac93c0d13b678c6)(struct bt\_conn \*conn,

833 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr,

834 void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset);

835

[ 843](group__bt__gatt__server.md#ga04c7887fb67107bd060dd023fd3186d5)#define BT\_GATT\_SERVICE\_DEFINE(\_name, ...) \

844 const struct bt\_gatt\_attr attr\_##\_name[] = { \_\_VA\_ARGS\_\_ }; \

845 const STRUCT\_SECTION\_ITERABLE(bt\_gatt\_service\_static, \_name) = \

846 BT\_GATT\_SERVICE(attr\_##\_name)

847

848#define \_BT\_GATT\_ATTRS\_ARRAY\_DEFINE(n, \_instances, \_attrs\_def) \

849 static struct bt\_gatt\_attr attrs\_##n[] = \_attrs\_def(\_instances[n])

850

851#define \_BT\_GATT\_SERVICE\_ARRAY\_ITEM(\_n, \_) BT\_GATT\_SERVICE(attrs\_##\_n)

852

[ 868](group__bt__gatt__server.md#ga8bb3aeef20465d7f6e38f6bbddef74e5)#define BT\_GATT\_SERVICE\_INSTANCE\_DEFINE( \

869 \_name, \_instances, \_instance\_num, \_attrs\_def) \

870 BUILD\_ASSERT(ARRAY\_SIZE(\_instances) == \_instance\_num, \

871 "The number of array elements does not match its size"); \

872 LISTIFY(\_instance\_num, \_BT\_GATT\_ATTRS\_ARRAY\_DEFINE, (;), \

873 \_instances, \_attrs\_def); \

874 static struct bt\_gatt\_service \_name[] = { \

875 LISTIFY(\_instance\_num, \_BT\_GATT\_SERVICE\_ARRAY\_ITEM, (,)) \

876 }

877

[ 885](group__bt__gatt__server.md#ga7d413ec013b91a633ec24d80d2814e2b)#define BT\_GATT\_SERVICE(\_attrs) \

886{ \

887 .attrs = \_attrs, \

888 .attr\_count = ARRAY\_SIZE(\_attrs), \

889}

890

[ 898](group__bt__gatt__server.md#gaacada0ff1029af959b6fcd6703d4a0bf)#define BT\_GATT\_PRIMARY\_SERVICE(\_service) \

899 BT\_GATT\_ATTRIBUTE(BT\_UUID\_GATT\_PRIMARY, BT\_GATT\_PERM\_READ, \

900 bt\_gatt\_attr\_read\_service, NULL, (void \*)\_service)

901

[ 912](group__bt__gatt__server.md#gaecb4d30282677d3450ad79c5f83f3445)#define BT\_GATT\_SECONDARY\_SERVICE(\_service) \

913 BT\_GATT\_ATTRIBUTE(BT\_UUID\_GATT\_SECONDARY, BT\_GATT\_PERM\_READ, \

914 bt\_gatt\_attr\_read\_service, NULL, (void \*)\_service)

915

[ 932](group__bt__gatt__server.md#ga4313a63decac2c8b7c4a1764df3d53ea)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [bt\_gatt\_attr\_read\_included](group__bt__gatt__server.md#ga4313a63decac2c8b7c4a1764df3d53ea)(struct bt\_conn \*conn,

933 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr,

934 void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset);

935

[ 943](group__bt__gatt__server.md#ga08ffee706d271b75a54b1b99249dba24)#define BT\_GATT\_INCLUDE\_SERVICE(\_service\_incl) \

944 BT\_GATT\_ATTRIBUTE(BT\_UUID\_GATT\_INCLUDE, BT\_GATT\_PERM\_READ, \

945 bt\_gatt\_attr\_read\_included, NULL, \_service\_incl)

946

[ 962](group__bt__gatt__server.md#gad58b526a06334530c13292d14a11257c)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [bt\_gatt\_attr\_read\_chrc](group__bt__gatt__server.md#gad58b526a06334530c13292d14a11257c)(struct bt\_conn \*conn,

963 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf,

964 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset);

965

[ 976](group__bt__gatt__server.md#ga7f19592a722c41d6c1d2421d166dd78a)#define BT\_GATT\_CHRC\_INIT(\_uuid, \_handle, \_props) \

977{ \

978 .uuid = \_uuid, \

979 .value\_handle = \_handle, \

980 .properties = \_props, \

981}

982

[ 1000](group__bt__gatt__server.md#ga9e739546dbd906d3b3c4f1ed5ad9f41e)#define BT\_GATT\_CHARACTERISTIC(\_uuid, \_props, \_perm, \_read, \_write, \_user\_data) \

1001 BT\_GATT\_ATTRIBUTE(BT\_UUID\_GATT\_CHRC, BT\_GATT\_PERM\_READ, \

1002 bt\_gatt\_attr\_read\_chrc, NULL, \

1003 ((struct bt\_gatt\_chrc[]) { \

1004 BT\_GATT\_CHRC\_INIT(\_uuid, 0U, \_props), \

1005 })), \

1006 BT\_GATT\_ATTRIBUTE(\_uuid, \_perm, \_read, \_write, \_user\_data)

1007

1019#if defined(CONFIG\_BT\_SETTINGS\_CCC\_LAZY\_LOADING)

1020 #define BT\_GATT\_CCC\_MAX (CONFIG\_BT\_MAX\_CONN)

1021#elif defined(CONFIG\_BT\_CONN)

1022 #define BT\_GATT\_CCC\_MAX (CONFIG\_BT\_MAX\_PAIRED + CONFIG\_BT\_MAX\_CONN)

1023#else

[ 1024](group__bt__gatt__server.md#gac1c0a195c1ec1ff2cdd5bf6d0ba6ad00) #define BT\_GATT\_CCC\_MAX 0

1025#endif

1026

[ 1033](structbt__gatt__ccc__cfg.md)struct [bt\_gatt\_ccc\_cfg](structbt__gatt__ccc__cfg.md) {

[ 1035](structbt__gatt__ccc__cfg.md#ac17ddefe7ca6dbac921ee4c6f44fbf51) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structbt__gatt__ccc__cfg.md#ac17ddefe7ca6dbac921ee4c6f44fbf51);

[ 1037](structbt__gatt__ccc__cfg.md#ab316080693b2c4daf5fd45e2c0501c70) [bt\_addr\_le\_t](structbt__addr__le__t.md) [peer](structbt__gatt__ccc__cfg.md#ab316080693b2c4daf5fd45e2c0501c70);

[ 1042](structbt__gatt__ccc__cfg.md#a92acf7329f66638ac6c657c8eaa795ac) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [value](structbt__gatt__ccc__cfg.md#a92acf7329f66638ac6c657c8eaa795ac);

1043};

1044

1046#define \_bt\_gatt\_ccc bt\_gatt\_ccc\_managed\_user\_data \_\_DEPRECATED\_MACRO

1047

[ 1052](structbt__gatt__ccc__managed__user__data.md)struct [bt\_gatt\_ccc\_managed\_user\_data](structbt__gatt__ccc__managed__user__data.md) {

[ 1054](structbt__gatt__ccc__managed__user__data.md#a44987dc5be9442436f6033c30bbb42fd) struct [bt\_gatt\_ccc\_cfg](structbt__gatt__ccc__cfg.md) [cfg](structbt__gatt__ccc__managed__user__data.md#a44987dc5be9442436f6033c30bbb42fd)[[BT\_GATT\_CCC\_MAX](group__bt__gatt__server.md#gac1c0a195c1ec1ff2cdd5bf6d0ba6ad00)];

1055

[ 1057](structbt__gatt__ccc__managed__user__data.md#a883177671ea068f1dcbab36197abfdfd) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [value](structbt__gatt__ccc__managed__user__data.md#a883177671ea068f1dcbab36197abfdfd);

1058

[ 1064](structbt__gatt__ccc__managed__user__data.md#a166073fca5a342b859fb42482547b80c) void (\*[cfg\_changed](structbt__gatt__ccc__managed__user__data.md#a166073fca5a342b859fb42482547b80c))(const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [value](structbt__gatt__ccc__managed__user__data.md#a883177671ea068f1dcbab36197abfdfd));

1065

[ 1075](structbt__gatt__ccc__managed__user__data.md#a7ba4c03ef2a0c2c85e17ef1147934536) [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[cfg\_write](structbt__gatt__ccc__managed__user__data.md#a7ba4c03ef2a0c2c85e17ef1147934536))(struct bt\_conn \*conn,

1076 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [value](structbt__gatt__ccc__managed__user__data.md#a883177671ea068f1dcbab36197abfdfd));

1077

[ 1089](structbt__gatt__ccc__managed__user__data.md#afc0c5226be7d9b2d3d039f86960a2ed3) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[cfg\_match](structbt__gatt__ccc__managed__user__data.md#afc0c5226be7d9b2d3d039f86960a2ed3))(struct bt\_conn \*conn,

1090 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr);

1091};

1092

[ 1112](group__bt__gatt__server.md#ga2e85b42136e2c6a4cb5b7ad8a2532573)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [bt\_gatt\_attr\_read\_ccc](group__bt__gatt__server.md#ga2e85b42136e2c6a4cb5b7ad8a2532573)(struct bt\_conn \*conn,

1113 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf,

1114 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset);

1115

[ 1135](group__bt__gatt__server.md#gabba965b676650a55cb9934072b34c75e)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [bt\_gatt\_attr\_write\_ccc](group__bt__gatt__server.md#gabba965b676650a55cb9934072b34c75e)(struct bt\_conn \*conn,

1136 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, const void \*buf,

1137 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

1138

[ 1140](group__bt__gatt__server.md#gab422808c5af1a1da27e15fd458d96bb8)#define BT\_GATT\_CCC\_INITIALIZER BT\_GATT\_CCC\_MANAGED\_USER\_DATA\_INIT \_\_DEPRECATED\_MACRO

1141

[ 1151](group__bt__gatt__server.md#gae3a23386bfe38e0127b74e0f4b5e5667)#define BT\_GATT\_CCC\_MANAGED\_USER\_DATA\_INIT(\_changed, \_write, \_match) \

1152 { \

1153 .cfg = {}, \

1154 .cfg\_changed = \_changed, \

1155 .cfg\_write = \_write, \

1156 .cfg\_match = \_match, \

1157 }

1158

[ 1171](group__bt__gatt__server.md#gad8b296ecfd1139680f21da7904b9f585)#define BT\_GATT\_CCC\_MANAGED(\_ccc, \_perm) \

1172 BT\_GATT\_ATTRIBUTE(BT\_UUID\_GATT\_CCC, \_perm, \

1173 bt\_gatt\_attr\_read\_ccc, bt\_gatt\_attr\_write\_ccc, \

1174 \_ccc)

1175

[ 1185](group__bt__gatt__server.md#ga140b9c25d10244bebd9c891f881fdc94)#define BT\_GATT\_CCC(\_changed, \_perm) \

1186 BT\_GATT\_CCC\_MANAGED(((struct bt\_gatt\_ccc\_managed\_user\_data[]){ \

1187 BT\_GATT\_CCC\_MANAGED\_USER\_DATA\_INIT(\_changed, NULL, NULL)}), \

1188 \_perm)

1189

[ 1200](group__bt__gatt__server.md#ga9a6fa72eb2b6e9438ad677365c998428)#define BT\_GATT\_CCC\_WITH\_WRITE\_CB(\_changed, \_write, \_perm) \

1201 BT\_GATT\_CCC\_MANAGED(((struct bt\_gatt\_ccc\_managed\_user\_data[]){ \

1202 BT\_GATT\_CCC\_MANAGED\_USER\_DATA\_INIT(\_changed, \_write, NULL)}), \

1203 \_perm)

1204

[ 1221](group__bt__gatt__server.md#ga5893166f1b24f437a94ccf1fc57c7917)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [bt\_gatt\_attr\_read\_cep](group__bt__gatt__server.md#ga5893166f1b24f437a94ccf1fc57c7917)(struct bt\_conn \*conn,

1222 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf,

1223 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset);

1224

[ 1232](group__bt__gatt__server.md#ga55a82cada1093c4ff75fe5504ac504b1)#define BT\_GATT\_CEP(\_value) \

1233 BT\_GATT\_DESCRIPTOR(BT\_UUID\_GATT\_CEP, BT\_GATT\_PERM\_READ, \

1234 bt\_gatt\_attr\_read\_cep, NULL, (void \*)\_value)

1235

[ 1253](group__bt__gatt__server.md#ga29421c8788b47b6a648704d27d5f0d28)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [bt\_gatt\_attr\_read\_cud](group__bt__gatt__server.md#ga29421c8788b47b6a648704d27d5f0d28)(struct bt\_conn \*conn,

1254 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf,

1255 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset);

1256

[ 1266](group__bt__gatt__server.md#ga1e1cd9d0853e2dcbefcb85fda44dc9c7)#define BT\_GATT\_CUD(\_value, \_perm) \

1267 BT\_GATT\_DESCRIPTOR(BT\_UUID\_GATT\_CUD, \_perm, bt\_gatt\_attr\_read\_cud, \

1268 NULL, (void \*)\_value)

1269

[ 1286](group__bt__gatt__server.md#ga5ae96590a0aaa5c4c3863a4a14d80fdd)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [bt\_gatt\_attr\_read\_cpf](group__bt__gatt__server.md#ga5ae96590a0aaa5c4c3863a4a14d80fdd)(struct bt\_conn \*conn,

1287 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf,

1288 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset);

1289

[ 1297](group__bt__gatt__server.md#ga3835fcfdf7a5f917e21c9d17e75162be)#define BT\_GATT\_CPF(\_value) \

1298 BT\_GATT\_DESCRIPTOR(BT\_UUID\_GATT\_CPF, BT\_GATT\_PERM\_READ, \

1299 bt\_gatt\_attr\_read\_cpf, NULL, (void \*)\_value)

1300

[ 1315](group__bt__gatt__server.md#ga83207fc083454327004f7d3c3e5b3840)#define BT\_GATT\_DESCRIPTOR(\_uuid, \_perm, \_read, \_write, \_user\_data) \

1316 BT\_GATT\_ATTRIBUTE(\_uuid, \_perm, \_read, \_write, \_user\_data)

1317

[ 1330](group__bt__gatt__server.md#gac4abfeb068d16dcdaceee812c12bf406)#define BT\_GATT\_ATTRIBUTE(\_uuid, \_perm, \_read, \_write, \_user\_data) \

1331{ \

1332 .uuid = \_uuid, \

1333 .read = \_read, \

1334 .write = \_write, \

1335 .user\_data = \_user\_data, \

1336 .handle = 0, \

1337 .perm = \_perm, \

1338}

1339

[ 1345](group__bt__gatt__server.md#gac55832607b95f394d26a64ed1cfe5bba)typedef void (\*[bt\_gatt\_complete\_func\_t](group__bt__gatt__server.md#gac55832607b95f394d26a64ed1cfe5bba)) (struct bt\_conn \*conn, void \*user\_data);

1346

[ 1351](structbt__gatt__notify__params.md)struct [bt\_gatt\_notify\_params](structbt__gatt__notify__params.md) {

[ 1357](structbt__gatt__notify__params.md#a2994cbe737fad725c60427000c21c373) const struct [bt\_uuid](structbt__uuid.md) \*[uuid](structbt__gatt__notify__params.md#a2994cbe737fad725c60427000c21c373);

[ 1363](structbt__gatt__notify__params.md#a6187d0457763a15a623129e3e9e98e13) const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*[attr](structbt__gatt__notify__params.md#a6187d0457763a15a623129e3e9e98e13);

[ 1365](structbt__gatt__notify__params.md#afaa276cff9cbf204c433ca776904ef32) const void \*[data](structbt__gatt__notify__params.md#afaa276cff9cbf204c433ca776904ef32);

[ 1367](structbt__gatt__notify__params.md#a4a511da0b099ca88d895594caf7aaa6a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structbt__gatt__notify__params.md#a4a511da0b099ca88d895594caf7aaa6a);

[ 1369](structbt__gatt__notify__params.md#ace3c6b5f5ed78b9f64c25b868d3bfbe2) [bt\_gatt\_complete\_func\_t](group__bt__gatt__server.md#gac55832607b95f394d26a64ed1cfe5bba) [func](structbt__gatt__notify__params.md#ace3c6b5f5ed78b9f64c25b868d3bfbe2);

[ 1371](structbt__gatt__notify__params.md#adec9a6f6ea0604e82b90dd47bb9951fa) void \*[user\_data](structbt__gatt__notify__params.md#adec9a6f6ea0604e82b90dd47bb9951fa);

1372#if defined(CONFIG\_BT\_EATT) || defined(\_\_DOXYGEN\_\_)

[ 1374](structbt__gatt__notify__params.md#a978d7a42c39a098cedf751936f280fac) enum [bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c) [chan\_opt](structbt__gatt__notify__params.md#a978d7a42c39a098cedf751936f280fac);

1375#endif /\* CONFIG\_BT\_EATT \*/

1376};

1377

[ 1397](group__bt__gatt__server.md#ga55e3ef7cb43b8acb0a27643c78390146)int [bt\_gatt\_notify\_cb](group__bt__gatt__server.md#ga55e3ef7cb43b8acb0a27643c78390146)(struct bt\_conn \*conn,

1398 struct [bt\_gatt\_notify\_params](structbt__gatt__notify__params.md) \*params);

1399

[ 1451](group__bt__gatt__server.md#ga8071d6063f85c0a78155f6b2ac2da635)int [bt\_gatt\_notify\_multiple](group__bt__gatt__server.md#ga8071d6063f85c0a78155f6b2ac2da635)(struct bt\_conn \*conn,

1452 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_params,

1453 struct [bt\_gatt\_notify\_params](structbt__gatt__notify__params.md) params[]);

1454

[ 1474](group__bt__gatt__server.md#ga74ee552864c563aa5bc939f37395c14a)static inline int [bt\_gatt\_notify](group__bt__gatt__server.md#ga74ee552864c563aa5bc939f37395c14a)(struct bt\_conn \*conn,

1475 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr,

1476 const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len)

1477{

1478 struct [bt\_gatt\_notify\_params](structbt__gatt__notify__params.md) params;

1479

1480 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(&params, 0, sizeof(params));

1481

1482 params.[attr](structbt__gatt__notify__params.md#a6187d0457763a15a623129e3e9e98e13) = [attr](structbt__gatt__notify__params.md#a6187d0457763a15a623129e3e9e98e13);

1483 params.[data](structbt__gatt__notify__params.md#afaa276cff9cbf204c433ca776904ef32) = [data](structbt__gatt__notify__params.md#afaa276cff9cbf204c433ca776904ef32);

1484 params.[len](structbt__gatt__notify__params.md#a4a511da0b099ca88d895594caf7aaa6a) = [len](structbt__gatt__notify__params.md#a4a511da0b099ca88d895594caf7aaa6a);

1485#if defined(CONFIG\_BT\_EATT)

1486 params.[chan\_opt](structbt__gatt__notify__params.md#a978d7a42c39a098cedf751936f280fac) = [BT\_ATT\_CHAN\_OPT\_NONE](group__bt__att.md#ggac593a27ecf029f33f50f990b2947562ca14e709b93e78dcc511339a99360ba739);

1487#endif /\* CONFIG\_BT\_EATT \*/

1488

1489 return [bt\_gatt\_notify\_cb](group__bt__gatt__server.md#ga55e3ef7cb43b8acb0a27643c78390146)(conn, &params);

1490}

1491

[ 1511](group__bt__gatt__server.md#ga24bae284dbc71cd4075649c4bc348b7c)static inline int [bt\_gatt\_notify\_uuid](group__bt__gatt__server.md#ga24bae284dbc71cd4075649c4bc348b7c)(struct bt\_conn \*conn,

1512 const struct [bt\_uuid](structbt__uuid.md) \*[uuid](structuuid.md),

1513 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*[attr](structbt__gatt__notify__params.md#a6187d0457763a15a623129e3e9e98e13),

1514 const void \*[data](structbt__gatt__notify__params.md#afaa276cff9cbf204c433ca776904ef32), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structbt__gatt__notify__params.md#a4a511da0b099ca88d895594caf7aaa6a))

1515{

1516 struct [bt\_gatt\_notify\_params](structbt__gatt__notify__params.md) params;

1517

1518 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(&params, 0, sizeof(params));

1519

1520 params.[uuid](structbt__gatt__notify__params.md#a2994cbe737fad725c60427000c21c373) = [uuid](structuuid.md);

1521 params.[attr](structbt__gatt__notify__params.md#a6187d0457763a15a623129e3e9e98e13) = [attr](structbt__gatt__notify__params.md#a6187d0457763a15a623129e3e9e98e13);

1522 params.[data](structbt__gatt__notify__params.md#afaa276cff9cbf204c433ca776904ef32) = [data](structbt__gatt__notify__params.md#afaa276cff9cbf204c433ca776904ef32);

1523 params.[len](structbt__gatt__notify__params.md#a4a511da0b099ca88d895594caf7aaa6a) = [len](structbt__gatt__notify__params.md#a4a511da0b099ca88d895594caf7aaa6a);

1524#if defined(CONFIG\_BT\_EATT)

1525 params.[chan\_opt](structbt__gatt__notify__params.md#a978d7a42c39a098cedf751936f280fac) = [BT\_ATT\_CHAN\_OPT\_NONE](group__bt__att.md#ggac593a27ecf029f33f50f990b2947562ca14e709b93e78dcc511339a99360ba739);

1526#endif /\* CONFIG\_BT\_EATT \*/

1527

1528 return [bt\_gatt\_notify\_cb](group__bt__gatt__server.md#ga55e3ef7cb43b8acb0a27643c78390146)(conn, &params);

1529}

1530

1531/\* Forward declaration of the bt\_gatt\_indicate\_params structure \*/

1532struct [bt\_gatt\_indicate\_params](structbt__gatt__indicate__params.md);

1533

[ 1541](group__bt__gatt__server.md#ga1294850e6bdcbe7a8f42f2956fd837a8)typedef void (\*[bt\_gatt\_indicate\_func\_t](group__bt__gatt__server.md#ga1294850e6bdcbe7a8f42f2956fd837a8))(struct bt\_conn \*conn,

1542 struct [bt\_gatt\_indicate\_params](structbt__gatt__indicate__params.md) \*params,

1543 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) err);

1544

[ 1553](group__bt__gatt__server.md#ga5d47ed9eaea22c8f00db14329daee8fe)typedef void (\*[bt\_gatt\_indicate\_params\_destroy\_t](group__bt__gatt__server.md#ga5d47ed9eaea22c8f00db14329daee8fe))(

1554 struct [bt\_gatt\_indicate\_params](structbt__gatt__indicate__params.md) \*params);

1555

[ 1561](structbt__gatt__indicate__params.md)struct [bt\_gatt\_indicate\_params](structbt__gatt__indicate__params.md) {

[ 1567](structbt__gatt__indicate__params.md#afde06f47d7a817291e437593ea01bccd) const struct [bt\_uuid](structbt__uuid.md) \*[uuid](structbt__gatt__indicate__params.md#afde06f47d7a817291e437593ea01bccd);

[ 1573](structbt__gatt__indicate__params.md#acbbee3a71838492416b20bb5cff89801) const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*[attr](structbt__gatt__indicate__params.md#acbbee3a71838492416b20bb5cff89801);

[ 1575](structbt__gatt__indicate__params.md#af9eb83c3fba49ee3cd6162d5a2791707) [bt\_gatt\_indicate\_func\_t](group__bt__gatt__server.md#ga1294850e6bdcbe7a8f42f2956fd837a8) [func](structbt__gatt__indicate__params.md#af9eb83c3fba49ee3cd6162d5a2791707);

[ 1577](structbt__gatt__indicate__params.md#aeb346dc4c0e4a298c66f394d037a6514) [bt\_gatt\_indicate\_params\_destroy\_t](group__bt__gatt__server.md#ga5d47ed9eaea22c8f00db14329daee8fe) [destroy](structbt__gatt__indicate__params.md#aeb346dc4c0e4a298c66f394d037a6514);

[ 1579](structbt__gatt__indicate__params.md#ae1d657512c99d5bba6fc99a450a6da32) const void \*[data](structbt__gatt__indicate__params.md#ae1d657512c99d5bba6fc99a450a6da32);

[ 1581](structbt__gatt__indicate__params.md#a10ad44140371165951eeac18cb3d0e7f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structbt__gatt__indicate__params.md#a10ad44140371165951eeac18cb3d0e7f);

1583 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_ref;

1584#if defined(CONFIG\_BT\_EATT) || defined(\_\_DOXYGEN\_\_)

[ 1586](structbt__gatt__indicate__params.md#a0e536938123ecb4f3ba6736c1de2a599) enum [bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c) [chan\_opt](structbt__gatt__indicate__params.md#a0e536938123ecb4f3ba6736c1de2a599);

1587#endif /\* CONFIG\_BT\_EATT \*/

1588};

1589

[ 1615](group__bt__gatt__server.md#ga4f2272692cc0f1d44638828012296c80)int [bt\_gatt\_indicate](group__bt__gatt__server.md#ga4f2272692cc0f1d44638828012296c80)(struct bt\_conn \*conn,

1616 struct [bt\_gatt\_indicate\_params](structbt__gatt__indicate__params.md) \*params);

1617

[ 1636](group__bt__gatt__server.md#gabd4df0a264dae10e43797992a567be7d)bool [bt\_gatt\_is\_subscribed](group__bt__gatt__server.md#gabd4df0a264dae10e43797992a567be7d)(struct bt\_conn \*conn,

1637 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ccc\_type);

1638

[ 1648](group__bt__gatt__server.md#ga351fd7658eaecbbfa60f1769119ef733)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [bt\_gatt\_get\_mtu](group__bt__gatt__server.md#ga351fd7658eaecbbfa60f1769119ef733)(struct bt\_conn \*conn);

1649

[ 1665](group__bt__gatt__server.md#ga6653de5e245cae6dc12cd0b45acbe028)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [bt\_gatt\_get\_uatt\_mtu](group__bt__gatt__server.md#ga6653de5e245cae6dc12cd0b45acbe028)(struct bt\_conn \*conn);

1666

1668

1674

[ 1683](structbt__gatt__exchange__params.md)struct [bt\_gatt\_exchange\_params](structbt__gatt__exchange__params.md) {

[ 1685](structbt__gatt__exchange__params.md#a76f4d3e779da9c725914574ac2e22ad1) void (\*[func](structbt__gatt__exchange__params.md#a76f4d3e779da9c725914574ac2e22ad1))(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) err,

1686 struct [bt\_gatt\_exchange\_params](structbt__gatt__exchange__params.md) \*params);

1687};

1688

[ 1713](group__bt__gatt__client.md#ga0f41da23c6559a8254b04295aff8198d)int [bt\_gatt\_exchange\_mtu](group__bt__gatt__client.md#ga0f41da23c6559a8254b04295aff8198d)(struct bt\_conn \*conn,

1714 struct [bt\_gatt\_exchange\_params](structbt__gatt__exchange__params.md) \*params);

1715

1716struct [bt\_gatt\_discover\_params](structbt__gatt__discover__params.md);

1717

[ 1767](group__bt__gatt__client.md#gabd3bcd3c1560956726574faed332fb13)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) (\*[bt\_gatt\_discover\_func\_t](group__bt__gatt__client.md#gabd3bcd3c1560956726574faed332fb13))(struct bt\_conn \*conn,

1768 const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr,

1769 struct [bt\_gatt\_discover\_params](structbt__gatt__discover__params.md) \*params);

1770

[ 1772](group__bt__gatt__client.md#gaea89c65f17050820d54568f636b6554a)enum [bt\_gatt\_discover\_type](group__bt__gatt__client.md#gaea89c65f17050820d54568f636b6554a) {

[ 1774](group__bt__gatt__client.md#ggaea89c65f17050820d54568f636b6554aada9ac33aa77f6043da8133dcf269478f) [BT\_GATT\_DISCOVER\_PRIMARY](group__bt__gatt__client.md#ggaea89c65f17050820d54568f636b6554aada9ac33aa77f6043da8133dcf269478f),

[ 1776](group__bt__gatt__client.md#ggaea89c65f17050820d54568f636b6554aa21be62548b816c7960a54dd6e3b37a97) [BT\_GATT\_DISCOVER\_SECONDARY](group__bt__gatt__client.md#ggaea89c65f17050820d54568f636b6554aa21be62548b816c7960a54dd6e3b37a97),

[ 1778](group__bt__gatt__client.md#ggaea89c65f17050820d54568f636b6554aa80afff1c83bb5ebb5603af699f2c26da) [BT\_GATT\_DISCOVER\_INCLUDE](group__bt__gatt__client.md#ggaea89c65f17050820d54568f636b6554aa80afff1c83bb5ebb5603af699f2c26da),

[ 1783](group__bt__gatt__client.md#ggaea89c65f17050820d54568f636b6554aa71355dfe0bf30c88f9fe2f7da1ba10ae) [BT\_GATT\_DISCOVER\_CHARACTERISTIC](group__bt__gatt__client.md#ggaea89c65f17050820d54568f636b6554aa71355dfe0bf30c88f9fe2f7da1ba10ae),

[ 1792](group__bt__gatt__client.md#ggaea89c65f17050820d54568f636b6554aa0ccb2587aa8f21361c5d73847a33ecbe) [BT\_GATT\_DISCOVER\_DESCRIPTOR](group__bt__gatt__client.md#ggaea89c65f17050820d54568f636b6554aa0ccb2587aa8f21361c5d73847a33ecbe),

[ 1801](group__bt__gatt__client.md#ggaea89c65f17050820d54568f636b6554aafe2167b873b848935d56f6ee7f2c444c) [BT\_GATT\_DISCOVER\_ATTRIBUTE](group__bt__gatt__client.md#ggaea89c65f17050820d54568f636b6554aafe2167b873b848935d56f6ee7f2c444c),

[ 1812](group__bt__gatt__client.md#ggaea89c65f17050820d54568f636b6554aa81a1f8737c415544a0f793f4e626bb61) [BT\_GATT\_DISCOVER\_STD\_CHAR\_DESC](group__bt__gatt__client.md#ggaea89c65f17050820d54568f636b6554aa81a1f8737c415544a0f793f4e626bb61),

1813};

1814

[ 1816](group__bt__gatt__client.md#ga7ca44e95989a143ae0b21e4a5316561d)#define BT\_GATT\_AUTO\_DISCOVER\_CCC\_HANDLE 0x0000U

1817

[ 1819](structbt__gatt__discover__params.md)struct [bt\_gatt\_discover\_params](structbt__gatt__discover__params.md) {

[ 1821](structbt__gatt__discover__params.md#a77d6665c01902e4e23cf8de8a9436262) const struct [bt\_uuid](structbt__uuid.md) \*[uuid](structbt__gatt__discover__params.md#a77d6665c01902e4e23cf8de8a9436262);

[ 1823](structbt__gatt__discover__params.md#a337d7366c12451938f12eec4dc60903e) [bt\_gatt\_discover\_func\_t](group__bt__gatt__client.md#gabd3bcd3c1560956726574faed332fb13) [func](structbt__gatt__discover__params.md#a337d7366c12451938f12eec4dc60903e);

1824 union {

1826 struct {

[ 1828](structbt__gatt__discover__params.md#a65ca3c9aad7c02d48fd35c4d6f69dc70) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [attr\_handle](structbt__gatt__discover__params.md#a65ca3c9aad7c02d48fd35c4d6f69dc70);

[ 1830](structbt__gatt__discover__params.md#a0d2604e7c3ee8969cb5096cbf5793fdb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [start\_handle](structbt__gatt__discover__params.md#a0d2604e7c3ee8969cb5096cbf5793fdb);

[ 1832](structbt__gatt__discover__params.md#a225868498c34411cc3fc2be8e678e85e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [end\_handle](structbt__gatt__discover__params.md#a225868498c34411cc3fc2be8e678e85e);

1833 } \_included;

1835 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_handle;

1836 };

1843 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [end\_handle](structbt__gatt__discover__params.md#a225868498c34411cc3fc2be8e678e85e);

[ 1845](structbt__gatt__discover__params.md#ab0f056c90954e1246d897019abd1e7fc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__gatt__discover__params.md#ab0f056c90954e1246d897019abd1e7fc);

1846#if defined(CONFIG\_BT\_GATT\_AUTO\_DISCOVER\_CCC) || defined(\_\_DOXYGEN\_\_)

[ 1848](structbt__gatt__discover__params.md#a87b130c520ce50f835d0589fd22a844c) struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \*[sub\_params](structbt__gatt__discover__params.md#a87b130c520ce50f835d0589fd22a844c);

1849#endif /\* defined(CONFIG\_BT\_GATT\_AUTO\_DISCOVER\_CCC) || defined(\_\_DOXYGEN\_\_) \*/

1850#if defined(CONFIG\_BT\_EATT) || defined(\_\_DOXYGEN\_\_)

[ 1852](structbt__gatt__discover__params.md#aba7585e3d0eefb323fcde9bcc88e287d) enum [bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c) [chan\_opt](structbt__gatt__discover__params.md#aba7585e3d0eefb323fcde9bcc88e287d);

1853#endif /\* CONFIG\_BT\_EATT \*/

1854};

1855

[ 1889](group__bt__gatt__client.md#gac06a945e5f7939b6716bc4f2cea781bd)int [bt\_gatt\_discover](group__bt__gatt__client.md#gac06a945e5f7939b6716bc4f2cea781bd)(struct bt\_conn \*conn,

1890 struct [bt\_gatt\_discover\_params](structbt__gatt__discover__params.md) \*params);

1891

1892struct [bt\_gatt\_read\_params](structbt__gatt__read__params.md);

1893

[ 1909](group__bt__gatt__client.md#ga1ca94b4f2b6c456b6134e05127993569)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) (\*[bt\_gatt\_read\_func\_t](group__bt__gatt__client.md#ga1ca94b4f2b6c456b6134e05127993569))(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) err,

1910 struct [bt\_gatt\_read\_params](structbt__gatt__read__params.md) \*params,

1911 const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length);

1912

[ 1914](structbt__gatt__read__params.md)struct [bt\_gatt\_read\_params](structbt__gatt__read__params.md) {

[ 1916](structbt__gatt__read__params.md#a3ea107db0b7537c9dccb2aa6d8f916fb) [bt\_gatt\_read\_func\_t](group__bt__gatt__client.md#ga1ca94b4f2b6c456b6134e05127993569) [func](structbt__gatt__read__params.md#a3ea107db0b7537c9dccb2aa6d8f916fb);

[ 1921](structbt__gatt__read__params.md#a0a36063ac0b110fbf57ef6a66f7bece8) size\_t [handle\_count](structbt__gatt__read__params.md#a0a36063ac0b110fbf57ef6a66f7bece8);

1922 union {

1923 struct {

[ 1925](structbt__gatt__read__params.md#af37beb6a69b3a6b90da0594b099bd64d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__gatt__read__params.md#af37beb6a69b3a6b90da0594b099bd64d);

[ 1927](structbt__gatt__read__params.md#a27f685a45c405bb2784fe369513724ad) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [offset](structbt__gatt__read__params.md#a27f685a45c405bb2784fe369513724ad);

[ 1928](structbt__gatt__read__params.md#a4cf61907bb95a2be6513d214b7030723) } [single](structbt__gatt__read__params.md#a4cf61907bb95a2be6513d214b7030723);

1929 struct {

[ 1933](structbt__gatt__read__params.md#a2794b8806933d0e16cfc77f4087fdeda) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*[handles](structbt__gatt__read__params.md#a2794b8806933d0e16cfc77f4087fdeda);

[ 1944](structbt__gatt__read__params.md#a77d05cbc54b125fc35d180cf91bf9cb9) bool [variable](structbt__gatt__read__params.md#a77d05cbc54b125fc35d180cf91bf9cb9);

[ 1945](structbt__gatt__read__params.md#a521f5d1859dd9271fa2c595012dacd25) } [multiple](structbt__gatt__read__params.md#a521f5d1859dd9271fa2c595012dacd25);

1946 struct {

[ 1958](structbt__gatt__read__params.md#ac11db1652cd5cee567d666d3697f3a4b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [start\_handle](structbt__gatt__read__params.md#ac11db1652cd5cee567d666d3697f3a4b);

[ 1968](structbt__gatt__read__params.md#a8b2a2b912efe557e24276a654087e75c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [end\_handle](structbt__gatt__read__params.md#a8b2a2b912efe557e24276a654087e75c);

[ 1970](structbt__gatt__read__params.md#ae2ba6ce4043769b86a050fd767248111) const struct [bt\_uuid](structbt__uuid.md) \*[uuid](structbt__gatt__read__params.md#ae2ba6ce4043769b86a050fd767248111);

[ 1971](structbt__gatt__read__params.md#a86b81f185490e63a07d2a62dd26a7f74) } [by\_uuid](structbt__gatt__read__params.md#a86b81f185490e63a07d2a62dd26a7f74);

1972 };

1973#if defined(CONFIG\_BT\_EATT) || defined(\_\_DOXYGEN\_\_)

[ 1975](structbt__gatt__read__params.md#a1335d1f9aefeff89a57efe78335cb41b) enum [bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c) [chan\_opt](structbt__gatt__read__params.md#a1335d1f9aefeff89a57efe78335cb41b);

1976#endif /\* CONFIG\_BT\_EATT \*/

1978 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \_att\_mtu;

1979};

1980

[ 2020](group__bt__gatt__client.md#ga1a18dd726ab960a88d7f85f2a014141a)int [bt\_gatt\_read](group__bt__gatt__client.md#ga1a18dd726ab960a88d7f85f2a014141a)(struct bt\_conn \*conn, struct [bt\_gatt\_read\_params](structbt__gatt__read__params.md) \*params);

2021

2022struct [bt\_gatt\_write\_params](structbt__gatt__write__params.md);

2023

[ 2031](group__bt__gatt__client.md#ga2bca8c4a45f41e0400a9e0147f4baf50)typedef void (\*[bt\_gatt\_write\_func\_t](group__bt__gatt__client.md#ga2bca8c4a45f41e0400a9e0147f4baf50))(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) err,

2032 struct [bt\_gatt\_write\_params](structbt__gatt__write__params.md) \*params);

2033

[ 2035](structbt__gatt__write__params.md)struct [bt\_gatt\_write\_params](structbt__gatt__write__params.md) {

[ 2037](structbt__gatt__write__params.md#a3468e3b75f3f9eda12bc4963f48cf9aa) [bt\_gatt\_write\_func\_t](group__bt__gatt__client.md#ga2bca8c4a45f41e0400a9e0147f4baf50) [func](structbt__gatt__write__params.md#a3468e3b75f3f9eda12bc4963f48cf9aa);

[ 2039](structbt__gatt__write__params.md#a384c5c15f248df5b327423ca32637bad) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__gatt__write__params.md#a384c5c15f248df5b327423ca32637bad);

[ 2041](structbt__gatt__write__params.md#add53cc08465d28f33bc48a1e8649ac1a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [offset](structbt__gatt__write__params.md#add53cc08465d28f33bc48a1e8649ac1a);

[ 2043](structbt__gatt__write__params.md#ab6510ef242e73325adb074322746c27c) const void \*[data](structbt__gatt__write__params.md#ab6510ef242e73325adb074322746c27c);

[ 2045](structbt__gatt__write__params.md#aded956dac2d398b642faeec81fdb9ec3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [length](structbt__gatt__write__params.md#aded956dac2d398b642faeec81fdb9ec3);

2046#if defined(CONFIG\_BT\_EATT) || defined(\_\_DOXYGEN\_\_)

[ 2048](structbt__gatt__write__params.md#ad79905c16f7ba5289817de552ece1a48) enum [bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c) [chan\_opt](structbt__gatt__write__params.md#ad79905c16f7ba5289817de552ece1a48);

2049#endif /\* CONFIG\_BT\_EATT \*/

2050};

2051

[ 2069](group__bt__gatt__client.md#ga843a42e68e0497d88d3f655f8ffd58d4)int [bt\_gatt\_write](group__bt__gatt__client.md#ga843a42e68e0497d88d3f655f8ffd58d4)(struct bt\_conn \*conn, struct [bt\_gatt\_write\_params](structbt__gatt__write__params.md) \*params);

2070

[ 2096](group__bt__gatt__client.md#ga49439413d12b5a8a1c68735e961ab6fa)int [bt\_gatt\_write\_without\_response\_cb](group__bt__gatt__client.md#ga49439413d12b5a8a1c68735e961ab6fa)(struct bt\_conn \*conn, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) handle,

2097 const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length,

2098 bool sign, [bt\_gatt\_complete\_func\_t](group__bt__gatt__server.md#gac55832607b95f394d26a64ed1cfe5bba) func,

2099 void \*user\_data);

2100

[ 2119](group__bt__gatt__client.md#ga9fc78e32230637a6f092da2400c50fe7)static inline int [bt\_gatt\_write\_without\_response](group__bt__gatt__client.md#ga9fc78e32230637a6f092da2400c50fe7)(struct bt\_conn \*conn,

2120 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) handle, const void \*data,

2121 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length, bool sign)

2122{

2123 return [bt\_gatt\_write\_without\_response\_cb](group__bt__gatt__client.md#ga49439413d12b5a8a1c68735e961ab6fa)(conn, handle, data, length,

2124 sign, [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

2125}

2126

2127struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md);

2128

[ 2145](group__bt__gatt__client.md#gab3e53eb5f9bb1eda7bf612ef95755b4d)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) (\*[bt\_gatt\_notify\_func\_t](group__bt__gatt__client.md#gab3e53eb5f9bb1eda7bf612ef95755b4d))(struct bt\_conn \*conn,

2146 struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \*params,

2147 const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length);

2148

[ 2156](group__bt__gatt__client.md#ga2e914e63b4b91fa56bc3295283c43714)typedef void (\*[bt\_gatt\_subscribe\_func\_t](group__bt__gatt__client.md#ga2e914e63b4b91fa56bc3295283c43714))(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) err,

2157 struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \*params);

2158

[ 2160](group__bt__gatt__client.md#gaa43f45658809908baa72bf4e0ea745ac)enum [bt\_gatt\_sub\_flag](group__bt__gatt__client.md#gaa43f45658809908baa72bf4e0ea745ac) {

[ 2170](group__bt__gatt__client.md#ggaa43f45658809908baa72bf4e0ea745acaecdcb3baa850505f459523091c92a1cb) [BT\_GATT\_SUBSCRIBE\_FLAG\_VOLATILE](group__bt__gatt__client.md#ggaa43f45658809908baa72bf4e0ea745acaecdcb3baa850505f459523091c92a1cb),

2171

[ 2184](group__bt__gatt__client.md#ggaa43f45658809908baa72bf4e0ea745aca30bfd3fb4bf4f17653ba00942ba2b2e6) [BT\_GATT\_SUBSCRIBE\_FLAG\_NO\_RESUB](group__bt__gatt__client.md#ggaa43f45658809908baa72bf4e0ea745aca30bfd3fb4bf4f17653ba00942ba2b2e6),

2185

[ 2193](group__bt__gatt__client.md#ggaa43f45658809908baa72bf4e0ea745acafe1c3dc9380c33debd32a275d5bce8ad) [BT\_GATT\_SUBSCRIBE\_FLAG\_WRITE\_PENDING](group__bt__gatt__client.md#ggaa43f45658809908baa72bf4e0ea745acafe1c3dc9380c33debd32a275d5bce8ad),

2194

[ 2205](group__bt__gatt__client.md#ggaa43f45658809908baa72bf4e0ea745aca56aa5f332d4098e3942d7a902198f7ab) [BT\_GATT\_SUBSCRIBE\_FLAG\_SENT](group__bt__gatt__client.md#ggaa43f45658809908baa72bf4e0ea745aca56aa5f332d4098e3942d7a902198f7ab),

2206

[ 2207](group__bt__gatt__client.md#ggaa43f45658809908baa72bf4e0ea745aca5640a1e06740a89859c5f4b183d58e79) [BT\_GATT\_SUBSCRIBE\_NUM\_FLAGS](group__bt__gatt__client.md#ggaa43f45658809908baa72bf4e0ea745aca5640a1e06740a89859c5f4b183d58e79)

2208};

2209

[ 2211](structbt__gatt__subscribe__params.md)struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) {

[ 2213](structbt__gatt__subscribe__params.md#acf237ef097e8b847eb049fb0a5d4b759) [bt\_gatt\_notify\_func\_t](group__bt__gatt__client.md#gab3e53eb5f9bb1eda7bf612ef95755b4d) [notify](structbt__gatt__subscribe__params.md#acf237ef097e8b847eb049fb0a5d4b759);

[ 2217](structbt__gatt__subscribe__params.md#a91595407b8de4e862652e41100668f0a) [bt\_gatt\_subscribe\_func\_t](group__bt__gatt__client.md#ga2e914e63b4b91fa56bc3295283c43714) [subscribe](structbt__gatt__subscribe__params.md#a91595407b8de4e862652e41100668f0a);

2218

[ 2220](structbt__gatt__subscribe__params.md#a9248418eb04a5b7a0faed5077c40bf22) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [value\_handle](structbt__gatt__subscribe__params.md#a9248418eb04a5b7a0faed5077c40bf22);

[ 2222](structbt__gatt__subscribe__params.md#a77c53cdfd4143483b33a8ecf6061561e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [ccc\_handle](structbt__gatt__subscribe__params.md#a77c53cdfd4143483b33a8ecf6061561e);

2223#if defined(CONFIG\_BT\_GATT\_AUTO\_DISCOVER\_CCC) || defined(\_\_DOXYGEN\_\_)

[ 2225](structbt__gatt__subscribe__params.md#af806d24aa97db1f2e9a021e719598a6d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [end\_handle](structbt__gatt__subscribe__params.md#af806d24aa97db1f2e9a021e719598a6d);

[ 2227](structbt__gatt__subscribe__params.md#ad3a3b9335b85777d65bdf875486e292a) struct [bt\_gatt\_discover\_params](structbt__gatt__discover__params.md) \*[disc\_params](structbt__gatt__subscribe__params.md#ad3a3b9335b85777d65bdf875486e292a);

2228#endif /\* defined(CONFIG\_BT\_GATT\_AUTO\_DISCOVER\_CCC) || defined(\_\_DOXYGEN\_\_) \*/

[ 2230](structbt__gatt__subscribe__params.md#a3bff1209b7a0b5908408a568622d0150) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [value](structbt__gatt__subscribe__params.md#a3bff1209b7a0b5908408a568622d0150);

2231#if defined(CONFIG\_BT\_SMP)

[ 2236](structbt__gatt__subscribe__params.md#a5b34bad1cf39bb3efd5faf516473dd4a) [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) [min\_security](structbt__gatt__subscribe__params.md#a5b34bad1cf39bb3efd5faf516473dd4a);

2237#endif

[ 2239](structbt__gatt__subscribe__params.md#aedd24024881e22372505355024cd716b) [ATOMIC\_DEFINE](group__atomic__apis.md#ga249c575db9764486197709b327f7370e)([flags](structbt__gatt__subscribe__params.md#aedd24024881e22372505355024cd716b), [BT\_GATT\_SUBSCRIBE\_NUM\_FLAGS](group__bt__gatt__client.md#ggaa43f45658809908baa72bf4e0ea745aca5640a1e06740a89859c5f4b183d58e79));

2240

2244 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

2246#if defined(CONFIG\_BT\_EATT) || defined(\_\_DOXYGEN\_\_)

[ 2248](structbt__gatt__subscribe__params.md#ae139848da09705d37fe7c9de4c1a4087) enum [bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c) [chan\_opt](structbt__gatt__subscribe__params.md#ae139848da09705d37fe7c9de4c1a4087);

2249#endif /\* CONFIG\_BT\_EATT \*/

2250};

2251

[ 2286](group__bt__gatt__client.md#ga7d4a8e18f51ba6476886a15f81f48e5c)int [bt\_gatt\_subscribe](group__bt__gatt__client.md#ga7d4a8e18f51ba6476886a15f81f48e5c)(struct bt\_conn \*conn,

2287 struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \*params);

2288

[ 2305](group__bt__gatt__client.md#ga791b8bb8a4c085b022fafc0535a63511)int [bt\_gatt\_resubscribe](group__bt__gatt__client.md#ga791b8bb8a4c085b022fafc0535a63511)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*peer,

2306 struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \*params);

2307

[ 2330](group__bt__gatt__client.md#ga56509c9b8f73f729cfa5e75be22d79ae)int [bt\_gatt\_unsubscribe](group__bt__gatt__client.md#ga56509c9b8f73f729cfa5e75be22d79ae)(struct bt\_conn \*conn,

2331 struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \*params);

2332

[ 2350](group__bt__gatt__client.md#ga5193dea59a016692f94cf950d6b4f4f7)void [bt\_gatt\_cancel](group__bt__gatt__client.md#ga5193dea59a016692f94cf950d6b4f4f7)(struct bt\_conn \*conn, void \*params);

2351

2353

2354#ifdef \_\_cplusplus

2355}

2356#endif

2357

2361

2362#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_GATT\_H\_ \*/

[addr.h](addr_8h.md)

Bluetooth device address definitions and utilities.

[att.h](att_8h.md)

Attribute Protocol handling.

[uuid.h](bluetooth_2uuid_8h.md)

Bluetooth UUID handling.

[conn.h](conn_8h.md)

Bluetooth connection handling.

[ATOMIC\_DEFINE](group__atomic__apis.md#ga249c575db9764486197709b327f7370e)

#define ATOMIC\_DEFINE(name, num\_bits)

Define an array of atomic variables.

**Definition** atomic.h:111

[bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c)

bt\_att\_chan\_opt

ATT channel option bit field values.

**Definition** att.h:177

[bt\_att\_err\_to\_str](group__bt__att.md#gad2305f28744276d97aefd26bdb79023c)

static const char \* bt\_att\_err\_to\_str(uint8\_t att\_err)

Converts a ATT error to string.

**Definition** att.h:127

[BT\_ATT\_CHAN\_OPT\_NONE](group__bt__att.md#ggac593a27ecf029f33f50f990b2947562ca14e709b93e78dcc511339a99360ba739)

@ BT\_ATT\_CHAN\_OPT\_NONE

Both Enhanced and Unenhanced channels can be used.

**Definition** att.h:179

[bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783)

bt\_security\_t

Security level.

**Definition** conn.h:814

[bt\_gatt\_exchange\_mtu](group__bt__gatt__client.md#ga0f41da23c6559a8254b04295aff8198d)

int bt\_gatt\_exchange\_mtu(struct bt\_conn \*conn, struct bt\_gatt\_exchange\_params \*params)

Exchange MTU.

[bt\_gatt\_read](group__bt__gatt__client.md#ga1a18dd726ab960a88d7f85f2a014141a)

int bt\_gatt\_read(struct bt\_conn \*conn, struct bt\_gatt\_read\_params \*params)

Read Attribute Value by handle.

[bt\_gatt\_read\_func\_t](group__bt__gatt__client.md#ga1ca94b4f2b6c456b6134e05127993569)

uint8\_t(\* bt\_gatt\_read\_func\_t)(struct bt\_conn \*conn, uint8\_t err, struct bt\_gatt\_read\_params \*params, const void \*data, uint16\_t length)

Read callback function.

**Definition** gatt.h:1909

[bt\_gatt\_write\_func\_t](group__bt__gatt__client.md#ga2bca8c4a45f41e0400a9e0147f4baf50)

void(\* bt\_gatt\_write\_func\_t)(struct bt\_conn \*conn, uint8\_t err, struct bt\_gatt\_write\_params \*params)

Write callback function.

**Definition** gatt.h:2031

[bt\_gatt\_subscribe\_func\_t](group__bt__gatt__client.md#ga2e914e63b4b91fa56bc3295283c43714)

void(\* bt\_gatt\_subscribe\_func\_t)(struct bt\_conn \*conn, uint8\_t err, struct bt\_gatt\_subscribe\_params \*params)

Subscription callback function.

**Definition** gatt.h:2156

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

**Definition** gatt.h:2119

[bt\_gatt\_sub\_flag](group__bt__gatt__client.md#gaa43f45658809908baa72bf4e0ea745ac)

bt\_gatt\_sub\_flag

Subscription flags.

**Definition** gatt.h:2160

[bt\_gatt\_notify\_func\_t](group__bt__gatt__client.md#gab3e53eb5f9bb1eda7bf612ef95755b4d)

uint8\_t(\* bt\_gatt\_notify\_func\_t)(struct bt\_conn \*conn, struct bt\_gatt\_subscribe\_params \*params, const void \*data, uint16\_t length)

Notification callback function.

**Definition** gatt.h:2145

[bt\_gatt\_discover\_func\_t](group__bt__gatt__client.md#gabd3bcd3c1560956726574faed332fb13)

uint8\_t(\* bt\_gatt\_discover\_func\_t)(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr, struct bt\_gatt\_discover\_params \*params)

Discover attribute callback function.

**Definition** gatt.h:1767

[bt\_gatt\_discover](group__bt__gatt__client.md#gac06a945e5f7939b6716bc4f2cea781bd)

int bt\_gatt\_discover(struct bt\_conn \*conn, struct bt\_gatt\_discover\_params \*params)

GATT Discover function.

[bt\_gatt\_discover\_type](group__bt__gatt__client.md#gaea89c65f17050820d54568f636b6554a)

bt\_gatt\_discover\_type

GATT Discover types.

**Definition** gatt.h:1772

[BT\_GATT\_SUBSCRIBE\_FLAG\_NO\_RESUB](group__bt__gatt__client.md#ggaa43f45658809908baa72bf4e0ea745aca30bfd3fb4bf4f17653ba00942ba2b2e6)

@ BT\_GATT\_SUBSCRIBE\_FLAG\_NO\_RESUB

No resubscribe flag.

**Definition** gatt.h:2184

[BT\_GATT\_SUBSCRIBE\_NUM\_FLAGS](group__bt__gatt__client.md#ggaa43f45658809908baa72bf4e0ea745aca5640a1e06740a89859c5f4b183d58e79)

@ BT\_GATT\_SUBSCRIBE\_NUM\_FLAGS

**Definition** gatt.h:2207

[BT\_GATT\_SUBSCRIBE\_FLAG\_SENT](group__bt__gatt__client.md#ggaa43f45658809908baa72bf4e0ea745aca56aa5f332d4098e3942d7a902198f7ab)

@ BT\_GATT\_SUBSCRIBE\_FLAG\_SENT

Sent flag.

**Definition** gatt.h:2205

[BT\_GATT\_SUBSCRIBE\_FLAG\_VOLATILE](group__bt__gatt__client.md#ggaa43f45658809908baa72bf4e0ea745acaecdcb3baa850505f459523091c92a1cb)

@ BT\_GATT\_SUBSCRIBE\_FLAG\_VOLATILE

Persistence flag.

**Definition** gatt.h:2170

[BT\_GATT\_SUBSCRIBE\_FLAG\_WRITE\_PENDING](group__bt__gatt__client.md#ggaa43f45658809908baa72bf4e0ea745acafe1c3dc9380c33debd32a275d5bce8ad)

@ BT\_GATT\_SUBSCRIBE\_FLAG\_WRITE\_PENDING

Write pending flag.

**Definition** gatt.h:2193

[BT\_GATT\_DISCOVER\_DESCRIPTOR](group__bt__gatt__client.md#ggaea89c65f17050820d54568f636b6554aa0ccb2587aa8f21361c5d73847a33ecbe)

@ BT\_GATT\_DISCOVER\_DESCRIPTOR

Discover Descriptors.

**Definition** gatt.h:1792

[BT\_GATT\_DISCOVER\_SECONDARY](group__bt__gatt__client.md#ggaea89c65f17050820d54568f636b6554aa21be62548b816c7960a54dd6e3b37a97)

@ BT\_GATT\_DISCOVER\_SECONDARY

Discover Secondary Services.

**Definition** gatt.h:1776

[BT\_GATT\_DISCOVER\_CHARACTERISTIC](group__bt__gatt__client.md#ggaea89c65f17050820d54568f636b6554aa71355dfe0bf30c88f9fe2f7da1ba10ae)

@ BT\_GATT\_DISCOVER\_CHARACTERISTIC

Discover Characteristic Values.

**Definition** gatt.h:1783

[BT\_GATT\_DISCOVER\_INCLUDE](group__bt__gatt__client.md#ggaea89c65f17050820d54568f636b6554aa80afff1c83bb5ebb5603af699f2c26da)

@ BT\_GATT\_DISCOVER\_INCLUDE

Discover Included Services.

**Definition** gatt.h:1778

[BT\_GATT\_DISCOVER\_STD\_CHAR\_DESC](group__bt__gatt__client.md#ggaea89c65f17050820d54568f636b6554aa81a1f8737c415544a0f793f4e626bb61)

@ BT\_GATT\_DISCOVER\_STD\_CHAR\_DESC

Discover standard characteristic descriptor values.

**Definition** gatt.h:1812

[BT\_GATT\_DISCOVER\_PRIMARY](group__bt__gatt__client.md#ggaea89c65f17050820d54568f636b6554aada9ac33aa77f6043da8133dcf269478f)

@ BT\_GATT\_DISCOVER\_PRIMARY

Discover Primary Services.

**Definition** gatt.h:1774

[BT\_GATT\_DISCOVER\_ATTRIBUTE](group__bt__gatt__client.md#ggaea89c65f17050820d54568f636b6554aafe2167b873b848935d56f6ee7f2c444c)

@ BT\_GATT\_DISCOVER\_ATTRIBUTE

Discover Attributes.

**Definition** gatt.h:1801

[bt\_gatt\_indicate\_func\_t](group__bt__gatt__server.md#ga1294850e6bdcbe7a8f42f2956fd837a8)

void(\* bt\_gatt\_indicate\_func\_t)(struct bt\_conn \*conn, struct bt\_gatt\_indicate\_params \*params, uint8\_t err)

Indication complete result callback.

**Definition** gatt.h:1541

[bt\_gatt\_notify\_uuid](group__bt__gatt__server.md#ga24bae284dbc71cd4075649c4bc348b7c)

static int bt\_gatt\_notify\_uuid(struct bt\_conn \*conn, const struct bt\_uuid \*uuid, const struct bt\_gatt\_attr \*attr, const void \*data, uint16\_t len)

Notify attribute value change by UUID.

**Definition** gatt.h:1511

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

Callback to destroy or clean up the GATT Indicate Value parameters.

**Definition** gatt.h:1553

[bt\_gatt\_authorization\_cb\_register](group__bt__gatt__server.md#ga5eee6afc6db391ffeda295d298bf6a56)

int bt\_gatt\_authorization\_cb\_register(const struct bt\_gatt\_authorization\_cb \*cb)

Register GATT authorization callbacks.

[bt\_gatt\_attr\_func\_t](group__bt__gatt__server.md#ga60284611c90729b289fe806524ba9209)

uint8\_t(\* bt\_gatt\_attr\_func\_t)(const struct bt\_gatt\_attr \*attr, uint16\_t handle, void \*user\_data)

Attribute iterator callback.

**Definition** gatt.h:707

[bt\_gatt\_get\_uatt\_mtu](group__bt__gatt__server.md#ga6653de5e245cae6dc12cd0b45acbe028)

uint16\_t bt\_gatt\_get\_uatt\_mtu(struct bt\_conn \*conn)

Get Unenhanced ATT (UATT) MTU for a connection.

[bt\_gatt\_notify](group__bt__gatt__server.md#ga74ee552864c563aa5bc939f37395c14a)

static int bt\_gatt\_notify(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr, const void \*data, uint16\_t len)

Notify attribute value change.

**Definition** gatt.h:1474

[bt\_gatt\_notify\_multiple](group__bt__gatt__server.md#ga8071d6063f85c0a78155f6b2ac2da635)

int bt\_gatt\_notify\_multiple(struct bt\_conn \*conn, uint16\_t num\_params, struct bt\_gatt\_notify\_params params[])

Send multiple notifications in a single PDU.

[bt\_gatt\_attr\_value\_handle](group__bt__gatt__server.md#ga99738cf4f05eae4c6da17cc3420827d8)

uint16\_t bt\_gatt\_attr\_value\_handle(const struct bt\_gatt\_attr \*attr)

Get the handle of the characteristic value descriptor.

[bt\_gatt\_foreach\_attr](group__bt__gatt__server.md#gaa93b5e0f2870ed135447bead903c175a)

static void bt\_gatt\_foreach\_attr(uint16\_t start\_handle, uint16\_t end\_handle, bt\_gatt\_attr\_func\_t func, void \*user\_data)

Attribute iterator.

**Definition** gatt.h:739

[bt\_gatt\_iter](group__bt__gatt__server.md#gab38994257f53473e62e01eff8f236ee1)

bt\_gatt\_iter

to be used as return values for bt\_gatt\_attr\_func\_t and bt\_gatt\_read\_func\_t type callbacks.

**Definition** gatt.h:692

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

BT\_GATT\_CCC\_MAX is defined depending on whether CONFIG\_BT\_SETTINGS\_CCC\_LAZY\_LOADING or CONFIG\_BT\_CONN...

**Definition** gatt.h:1024

[bt\_gatt\_complete\_func\_t](group__bt__gatt__server.md#gac55832607b95f394d26a64ed1cfe5bba)

void(\* bt\_gatt\_complete\_func\_t)(struct bt\_conn \*conn, void \*user\_data)

Notification complete result callback.

**Definition** gatt.h:1345

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

[bt\_gatt\_err\_to\_str](group__bt__gatt__server.md#gaf6d3f1e904f1a847afeb30236bad98a2)

static const char \* bt\_gatt\_err\_to\_str(int gatt\_err)

Converts a GATT error to string.

**Definition** gatt.h:611

[BT\_GATT\_ITER\_STOP](group__bt__gatt__server.md#ggab38994257f53473e62e01eff8f236ee1aa3f2a25e27c7065a2c7bb2a9ff09542e)

@ BT\_GATT\_ITER\_STOP

**Definition** gatt.h:693

[BT\_GATT\_ITER\_CONTINUE](group__bt__gatt__server.md#ggab38994257f53473e62e01eff8f236ee1aea569feffa4815d3443e12be78c684f5)

@ BT\_GATT\_ITER\_CONTINUE

**Definition** gatt.h:694

[bt\_gatt\_attr\_write\_func\_t](group__bt__gatt.md#ga3fd8527a0f3e8f3699dc0d3b0339eba1)

ssize\_t(\* bt\_gatt\_attr\_write\_func\_t)(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr, const void \*buf, uint16\_t len, uint16\_t offset, uint8\_t flags)

Attribute Value write implementation.

**Definition** gatt.h:212

[bt\_gatt\_attr\_read\_func\_t](group__bt__gatt.md#ga57e36bf94652531964fd4237c203fe7b)

ssize\_t(\* bt\_gatt\_attr\_read\_func\_t)(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr, void \*buf, uint16\_t len, uint16\_t offset)

Attribute read callback.

**Definition** gatt.h:169

[bt\_gatt\_attr\_write\_flag](group__bt__gatt.md#ga830d437c8d0757f53af1de6aa3031906)

bt\_gatt\_attr\_write\_flag

GATT attribute write flags.

**Definition** gatt.h:112

[bt\_gatt\_perm](group__bt__gatt.md#ga96e57500d2340a45badb23701cc43833)

bt\_gatt\_perm

GATT attribute permission bit field values.

**Definition** gatt.h:46

[BT\_GATT\_WRITE\_FLAG\_PREPARE](group__bt__gatt.md#gga830d437c8d0757f53af1de6aa3031906a019cf6118a0cfacbfad20c1cc5838383)

@ BT\_GATT\_WRITE\_FLAG\_PREPARE

Attribute prepare write flag.

**Definition** gatt.h:118

[BT\_GATT\_WRITE\_FLAG\_CMD](group__bt__gatt.md#gga830d437c8d0757f53af1de6aa3031906a770df41b7d433e8ce349b19e4657ba78)

@ BT\_GATT\_WRITE\_FLAG\_CMD

Attribute write command flag.

**Definition** gatt.h:125

[BT\_GATT\_WRITE\_FLAG\_EXECUTE](group__bt__gatt.md#gga830d437c8d0757f53af1de6aa3031906ad4e8f43c03da10c15685bd1a0109708b)

@ BT\_GATT\_WRITE\_FLAG\_EXECUTE

Attribute write execute flag.

**Definition** gatt.h:133

[BT\_GATT\_PERM\_READ\_ENCRYPT](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a0d0afe4a6389102f85e355468cb7984d)

@ BT\_GATT\_PERM\_READ\_ENCRYPT

Attribute read permission with encryption.

**Definition** gatt.h:60

[BT\_GATT\_PERM\_WRITE](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a0f611698ca511f565b247a813ea016cf)

@ BT\_GATT\_PERM\_WRITE

Attribute write permission.

**Definition** gatt.h:54

[BT\_GATT\_PERM\_WRITE\_ENCRYPT](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a662b9af6f435d788aa4e6829725f670f)

@ BT\_GATT\_PERM\_WRITE\_ENCRYPT

Attribute write permission with encryption.

**Definition** gatt.h:66

[BT\_GATT\_PERM\_NONE](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a81a1c35d981593c4c0d344dd0f7e898a)

@ BT\_GATT\_PERM\_NONE

No operations supported, e.g.

**Definition** gatt.h:48

[BT\_GATT\_PERM\_READ](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a9afb838c2cef657e9cd035ef27521f17)

@ BT\_GATT\_PERM\_READ

Attribute read permission.

**Definition** gatt.h:51

[BT\_GATT\_PERM\_PREPARE\_WRITE](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833ab384b61f6ead9d140011da917c950d79)

@ BT\_GATT\_PERM\_PREPARE\_WRITE

Attribute prepare write permission.

**Definition** gatt.h:87

[BT\_GATT\_PERM\_WRITE\_LESC](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833ac56183af896e2a58439c625420efca94)

@ BT\_GATT\_PERM\_WRITE\_LESC

Attribute write permission with LE Secure Connection encryption.

**Definition** gatt.h:99

[BT\_GATT\_PERM\_READ\_AUTHEN](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833ad83f4c03608f674c00ebc93e63d08583)

@ BT\_GATT\_PERM\_READ\_AUTHEN

Attribute read permission with authentication.

**Definition** gatt.h:73

[BT\_GATT\_PERM\_WRITE\_AUTHEN](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833add3893c94a788ff2e5256595a533a266)

@ BT\_GATT\_PERM\_WRITE\_AUTHEN

Attribute write permission with authentication.

**Definition** gatt.h:80

[BT\_GATT\_PERM\_READ\_LESC](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833af62e397dfd87fe763b9c9fc1d5072f57)

@ BT\_GATT\_PERM\_READ\_LESC

Attribute read permission with LE Secure Connection encryption.

**Definition** gatt.h:93

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

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

[string.h](string_8h.md)

[memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)

void \* memset(void \*buf, int c, size\_t n)

[bt\_addr\_le\_t](structbt__addr__le__t.md)

Bluetooth LE Device Address.

**Definition** addr.h:49

[bt\_gatt\_attr](structbt__gatt__attr.md)

GATT Attribute.

**Definition** gatt.h:227

[bt\_gatt\_attr::read](structbt__gatt__attr.md#a074abc719494ca35997a452f526e7ecc)

bt\_gatt\_attr\_read\_func\_t read

Attribute Value read method.

**Definition** gatt.h:254

[bt\_gatt\_attr::perm](structbt__gatt__attr.md#a0849a40254622080d05e8559c4fdb9e2)

uint16\_t perm

Attribute Permissions.

**Definition** gatt.h:299

[bt\_gatt\_attr::write](structbt__gatt__attr.md#a1ecd78536067f4bded506e0daccefd35)

bt\_gatt\_attr\_write\_func\_t write

Attribute Value write method.

**Definition** gatt.h:267

[bt\_gatt\_attr::uuid](structbt__gatt__attr.md#a6958f507f9ff172018be458ebc86106f)

const struct bt\_uuid \* uuid

Attribute Type.

**Definition** gatt.h:241

[bt\_gatt\_attr::user\_data](structbt__gatt__attr.md#adeb063fb101fab45dd789c7212c43357)

void \* user\_data

Private data for read() and write() implementation.

**Definition** gatt.h:280

[bt\_gatt\_attr::handle](structbt__gatt__attr.md#aeee42a3d3ca15e40cf11cc0c3fde106b)

uint16\_t handle

Attribute Handle.

**Definition** gatt.h:290

[bt\_gatt\_authorization\_cb](structbt__gatt__authorization__cb.md)

GATT authorization callback structure.

**Definition** gatt.h:392

[bt\_gatt\_authorization\_cb::read\_authorize](structbt__gatt__authorization__cb.md#a7b1bcbe10f12c90ee4e3214e36e9c2a3)

bool(\* read\_authorize)(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr)

Authorize the GATT read operation.

**Definition** gatt.h:404

[bt\_gatt\_authorization\_cb::write\_authorize](structbt__gatt__authorization__cb.md#a7c12bd14f87f91e672eaaf92e1aa6e7b)

bool(\* write\_authorize)(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr)

Authorize the GATT write operation.

**Definition** gatt.h:418

[bt\_gatt\_cb](structbt__gatt__cb.md)

GATT callback structure.

**Definition** gatt.h:372

[bt\_gatt\_cb::att\_mtu\_updated](structbt__gatt__cb.md#a93fe1a626ab59c38ef56f02671f88980)

void(\* att\_mtu\_updated)(struct bt\_conn \*conn, uint16\_t tx, uint16\_t rx)

The maximum ATT MTU on a connection has changed.

**Definition** gatt.h:382

[bt\_gatt\_ccc\_cfg](structbt__gatt__ccc__cfg.md)

GATT CCC configuration entry.

**Definition** gatt.h:1033

[bt\_gatt\_ccc\_cfg::value](structbt__gatt__ccc__cfg.md#a92acf7329f66638ac6c657c8eaa795ac)

uint16\_t value

Configuration value Value used to enable or disable notifications or indications for a specific chara...

**Definition** gatt.h:1042

[bt\_gatt\_ccc\_cfg::peer](structbt__gatt__ccc__cfg.md#ab316080693b2c4daf5fd45e2c0501c70)

bt\_addr\_le\_t peer

Remote peer address.

**Definition** gatt.h:1037

[bt\_gatt\_ccc\_cfg::id](structbt__gatt__ccc__cfg.md#ac17ddefe7ca6dbac921ee4c6f44fbf51)

uint8\_t id

Local identity, BT\_ID\_DEFAULT in most cases.

**Definition** gatt.h:1035

[bt\_gatt\_ccc\_managed\_user\_data](structbt__gatt__ccc__managed__user__data.md)

Internal representation of CCC value.

**Definition** gatt.h:1052

[bt\_gatt\_ccc\_managed\_user\_data::cfg\_changed](structbt__gatt__ccc__managed__user__data.md#a166073fca5a342b859fb42482547b80c)

void(\* cfg\_changed)(const struct bt\_gatt\_attr \*attr, uint16\_t value)

CCC attribute changed callback.

**Definition** gatt.h:1064

[bt\_gatt\_ccc\_managed\_user\_data::cfg](structbt__gatt__ccc__managed__user__data.md#a44987dc5be9442436f6033c30bbb42fd)

struct bt\_gatt\_ccc\_cfg cfg[0]

Configuration for each connection.

**Definition** gatt.h:1054

[bt\_gatt\_ccc\_managed\_user\_data::cfg\_write](structbt__gatt__ccc__managed__user__data.md#a7ba4c03ef2a0c2c85e17ef1147934536)

ssize\_t(\* cfg\_write)(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr, uint16\_t value)

CCC attribute write validation callback.

**Definition** gatt.h:1075

[bt\_gatt\_ccc\_managed\_user\_data::value](structbt__gatt__ccc__managed__user__data.md#a883177671ea068f1dcbab36197abfdfd)

uint16\_t value

Highest value of all connected peer's subscriptions.

**Definition** gatt.h:1057

[bt\_gatt\_ccc\_managed\_user\_data::cfg\_match](structbt__gatt__ccc__managed__user__data.md#afc0c5226be7d9b2d3d039f86960a2ed3)

bool(\* cfg\_match)(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr)

CCC attribute match handler.

**Definition** gatt.h:1089

[bt\_gatt\_ccc](structbt__gatt__ccc.md)

Client Characteristic Configuration Attribute Value.

**Definition** gatt.h:525

[bt\_gatt\_ccc::flags](structbt__gatt__ccc.md#ac8fa1028c5e87aa025832257b18fa7c3)

uint16\_t flags

Client Characteristic Configuration flags, a bitmap of BT\_GATT\_CCC\_\* macros.

**Definition** gatt.h:527

[bt\_gatt\_cep](structbt__gatt__cep.md)

Characteristic Extended Properties Attribute Value.

**Definition** gatt.h:501

[bt\_gatt\_cep::properties](structbt__gatt__cep.md#a317442dc204f7632b0c5da8a8a9a98b5)

uint16\_t properties

Characteristic Extended properties, a bitmap of BT\_GATT\_CEP\_\* macros.

**Definition** gatt.h:503

[bt\_gatt\_chrc](structbt__gatt__chrc.md)

Attribute Value of a Characteristic Declaration.

**Definition** gatt.h:481

[bt\_gatt\_chrc::value\_handle](structbt__gatt__chrc.md#a2ca6aec1a621fdfd12142a1188d37bd3)

uint16\_t value\_handle

Characteristic Value handle.

**Definition** gatt.h:485

[bt\_gatt\_chrc::properties](structbt__gatt__chrc.md#a81bb8257052d7c8d03b51acaa51e5011)

uint8\_t properties

Characteristic properties, a bitmap of BT\_GATT\_CHRC\_\* macros.

**Definition** gatt.h:487

[bt\_gatt\_chrc::uuid](structbt__gatt__chrc.md#af3b4c22ae37b912c8edf58294cc50702)

const struct bt\_uuid \* uuid

Characteristic UUID.

**Definition** gatt.h:483

[bt\_gatt\_cpf](structbt__gatt__cpf.md)

GATT Characteristic Presentation Format Attribute Value.

**Definition** gatt.h:554

[bt\_gatt\_cpf::name\_space](structbt__gatt__cpf.md#a1dfbb9fc1e1397d2abec04b216d7ae33)

uint8\_t name\_space

Name space of the description.

**Definition** gatt.h:579

[bt\_gatt\_cpf::unit](structbt__gatt__cpf.md#a2a9f3d3f72b9acb1ef7f2dc765e5a231)

uint16\_t unit

UUID of the unit of the characteristic.

**Definition** gatt.h:572

[bt\_gatt\_cpf::exponent](structbt__gatt__cpf.md#a3690a86c942badb2d2698481b03e436d)

int8\_t exponent

Exponent field for value formatting.

**Definition** gatt.h:566

[bt\_gatt\_cpf::description](structbt__gatt__cpf.md#a3c48dd5ea717fbaf510d13c64a370c06)

uint16\_t description

Description of the characteristic as defined in a higher layer profile.

**Definition** gatt.h:586

[bt\_gatt\_cpf::format](structbt__gatt__cpf.md#ab0ca135a75130b3ffc0c5bf375f3528f)

uint8\_t format

Format of the value of the characteristic.

**Definition** gatt.h:560

[bt\_gatt\_discover\_params](structbt__gatt__discover__params.md)

GATT Discover Attributes parameters.

**Definition** gatt.h:1819

[bt\_gatt\_discover\_params::start\_handle](structbt__gatt__discover__params.md#a0d2604e7c3ee8969cb5096cbf5793fdb)

uint16\_t start\_handle

Starting attribute handle for included service.

**Definition** gatt.h:1830

[bt\_gatt\_discover\_params::end\_handle](structbt__gatt__discover__params.md#a225868498c34411cc3fc2be8e678e85e)

uint16\_t end\_handle

Ending attribute handle for included service.

**Definition** gatt.h:1832

[bt\_gatt\_discover\_params::func](structbt__gatt__discover__params.md#a337d7366c12451938f12eec4dc60903e)

bt\_gatt\_discover\_func\_t func

Discover attribute callback.

**Definition** gatt.h:1823

[bt\_gatt\_discover\_params::attr\_handle](structbt__gatt__discover__params.md#a65ca3c9aad7c02d48fd35c4d6f69dc70)

uint16\_t attr\_handle

Include service attribute declaration handle.

**Definition** gatt.h:1828

[bt\_gatt\_discover\_params::uuid](structbt__gatt__discover__params.md#a77d6665c01902e4e23cf8de8a9436262)

const struct bt\_uuid \* uuid

Discover UUID type.

**Definition** gatt.h:1821

[bt\_gatt\_discover\_params::sub\_params](structbt__gatt__discover__params.md#a87b130c520ce50f835d0589fd22a844c)

struct bt\_gatt\_subscribe\_params \* sub\_params

Only for stack-internal use, used for automatic discovery.

**Definition** gatt.h:1848

[bt\_gatt\_discover\_params::type](structbt__gatt__discover__params.md#ab0f056c90954e1246d897019abd1e7fc)

uint8\_t type

Discover type.

**Definition** gatt.h:1845

[bt\_gatt\_discover\_params::chan\_opt](structbt__gatt__discover__params.md#aba7585e3d0eefb323fcde9bcc88e287d)

enum bt\_att\_chan\_opt chan\_opt

Att channel options.

**Definition** gatt.h:1852

[bt\_gatt\_exchange\_params](structbt__gatt__exchange__params.md)

GATT Exchange MTU parameters.

**Definition** gatt.h:1683

[bt\_gatt\_exchange\_params::func](structbt__gatt__exchange__params.md#a76f4d3e779da9c725914574ac2e22ad1)

void(\* func)(struct bt\_conn \*conn, uint8\_t err, struct bt\_gatt\_exchange\_params \*params)

Callback for MTU exchange response.

**Definition** gatt.h:1685

[bt\_gatt\_include](structbt__gatt__include.md)

Include Attribute Value.

**Definition** gatt.h:362

[bt\_gatt\_include::end\_handle](structbt__gatt__include.md#a54d20cebfd6ba62b692c363acdc25d61)

uint16\_t end\_handle

Handle of the last attribute within the included service.

**Definition** gatt.h:368

[bt\_gatt\_include::start\_handle](structbt__gatt__include.md#ac7f6c1a8018f483dce14f0fe21031232)

uint16\_t start\_handle

Handle of the first attribute within the included service.

**Definition** gatt.h:366

[bt\_gatt\_include::uuid](structbt__gatt__include.md#afa028e8daae00e3b1bc0b866c4335af3)

const struct bt\_uuid \* uuid

Service UUID.

**Definition** gatt.h:364

[bt\_gatt\_indicate\_params](structbt__gatt__indicate__params.md)

GATT Indicate Value parameters.

**Definition** gatt.h:1561

[bt\_gatt\_indicate\_params::chan\_opt](structbt__gatt__indicate__params.md#a0e536938123ecb4f3ba6736c1de2a599)

enum bt\_att\_chan\_opt chan\_opt

Att channel options.

**Definition** gatt.h:1586

[bt\_gatt\_indicate\_params::len](structbt__gatt__indicate__params.md#a10ad44140371165951eeac18cb3d0e7f)

uint16\_t len

Indicate Value length.

**Definition** gatt.h:1581

[bt\_gatt\_indicate\_params::attr](structbt__gatt__indicate__params.md#acbbee3a71838492416b20bb5cff89801)

const struct bt\_gatt\_attr \* attr

Indicate Attribute object.

**Definition** gatt.h:1573

[bt\_gatt\_indicate\_params::data](structbt__gatt__indicate__params.md#ae1d657512c99d5bba6fc99a450a6da32)

const void \* data

Indicate Value data.

**Definition** gatt.h:1579

[bt\_gatt\_indicate\_params::destroy](structbt__gatt__indicate__params.md#aeb346dc4c0e4a298c66f394d037a6514)

bt\_gatt\_indicate\_params\_destroy\_t destroy

Indicate operation complete callback.

**Definition** gatt.h:1577

[bt\_gatt\_indicate\_params::func](structbt__gatt__indicate__params.md#af9eb83c3fba49ee3cd6162d5a2791707)

bt\_gatt\_indicate\_func\_t func

Indicate Value callback.

**Definition** gatt.h:1575

[bt\_gatt\_indicate\_params::uuid](structbt__gatt__indicate__params.md#afde06f47d7a817291e437593ea01bccd)

const struct bt\_uuid \* uuid

Indicate Attribute UUID type.

**Definition** gatt.h:1567

[bt\_gatt\_notify\_params](structbt__gatt__notify__params.md)

GATT notification parameters.

**Definition** gatt.h:1351

[bt\_gatt\_notify\_params::uuid](structbt__gatt__notify__params.md#a2994cbe737fad725c60427000c21c373)

const struct bt\_uuid \* uuid

Notification Attribute UUID type.

**Definition** gatt.h:1357

[bt\_gatt\_notify\_params::len](structbt__gatt__notify__params.md#a4a511da0b099ca88d895594caf7aaa6a)

uint16\_t len

Notification Value length.

**Definition** gatt.h:1367

[bt\_gatt\_notify\_params::attr](structbt__gatt__notify__params.md#a6187d0457763a15a623129e3e9e98e13)

const struct bt\_gatt\_attr \* attr

Notification Attribute object.

**Definition** gatt.h:1363

[bt\_gatt\_notify\_params::chan\_opt](structbt__gatt__notify__params.md#a978d7a42c39a098cedf751936f280fac)

enum bt\_att\_chan\_opt chan\_opt

Att channel options.

**Definition** gatt.h:1374

[bt\_gatt\_notify\_params::func](structbt__gatt__notify__params.md#ace3c6b5f5ed78b9f64c25b868d3bfbe2)

bt\_gatt\_complete\_func\_t func

Notification Value callback.

**Definition** gatt.h:1369

[bt\_gatt\_notify\_params::user\_data](structbt__gatt__notify__params.md#adec9a6f6ea0604e82b90dd47bb9951fa)

void \* user\_data

Notification Value callback user data.

**Definition** gatt.h:1371

[bt\_gatt\_notify\_params::data](structbt__gatt__notify__params.md#afaa276cff9cbf204c433ca776904ef32)

const void \* data

Notification Value data.

**Definition** gatt.h:1365

[bt\_gatt\_read\_params](structbt__gatt__read__params.md)

GATT Read parameters.

**Definition** gatt.h:1914

[bt\_gatt\_read\_params::handle\_count](structbt__gatt__read__params.md#a0a36063ac0b110fbf57ef6a66f7bece8)

size\_t handle\_count

If equals to 1 single.handle and single.offset are used.

**Definition** gatt.h:1921

[bt\_gatt\_read\_params::chan\_opt](structbt__gatt__read__params.md#a1335d1f9aefeff89a57efe78335cb41b)

enum bt\_att\_chan\_opt chan\_opt

Att channel options.

**Definition** gatt.h:1975

[bt\_gatt\_read\_params::handles](structbt__gatt__read__params.md#a2794b8806933d0e16cfc77f4087fdeda)

uint16\_t \* handles

Attribute handles to read with Read Multiple Characteristic Values.

**Definition** gatt.h:1933

[bt\_gatt\_read\_params::offset](structbt__gatt__read__params.md#a27f685a45c405bb2784fe369513724ad)

uint16\_t offset

Attribute data offset.

**Definition** gatt.h:1927

[bt\_gatt\_read\_params::func](structbt__gatt__read__params.md#a3ea107db0b7537c9dccb2aa6d8f916fb)

bt\_gatt\_read\_func\_t func

Read attribute callback.

**Definition** gatt.h:1916

[bt\_gatt\_read\_params::single](structbt__gatt__read__params.md#a4cf61907bb95a2be6513d214b7030723)

struct bt\_gatt\_read\_params::@172336054125152351005356152301225305321016010030::@372352161252260236002106024214036013303007152222 single

[bt\_gatt\_read\_params::multiple](structbt__gatt__read__params.md#a521f5d1859dd9271fa2c595012dacd25)

struct bt\_gatt\_read\_params::@172336054125152351005356152301225305321016010030::@371162354121151156017205063160212333251365073232 multiple

[bt\_gatt\_read\_params::variable](structbt__gatt__read__params.md#a77d05cbc54b125fc35d180cf91bf9cb9)

bool variable

If true use Read Multiple Variable Length Characteristic Values procedure.

**Definition** gatt.h:1944

[bt\_gatt\_read\_params::by\_uuid](structbt__gatt__read__params.md#a86b81f185490e63a07d2a62dd26a7f74)

struct bt\_gatt\_read\_params::@172336054125152351005356152301225305321016010030::@261011265054333145327063036013076000041270205077 by\_uuid

[bt\_gatt\_read\_params::end\_handle](structbt__gatt__read__params.md#a8b2a2b912efe557e24276a654087e75c)

uint16\_t end\_handle

Requested end attribute handle number.

**Definition** gatt.h:1968

[bt\_gatt\_read\_params::start\_handle](structbt__gatt__read__params.md#ac11db1652cd5cee567d666d3697f3a4b)

uint16\_t start\_handle

Requested start attribute handle number.

**Definition** gatt.h:1958

[bt\_gatt\_read\_params::uuid](structbt__gatt__read__params.md#ae2ba6ce4043769b86a050fd767248111)

const struct bt\_uuid \* uuid

2 or 16 octet UUID.

**Definition** gatt.h:1970

[bt\_gatt\_read\_params::handle](structbt__gatt__read__params.md#af37beb6a69b3a6b90da0594b099bd64d)

uint16\_t handle

Attribute handle.

**Definition** gatt.h:1925

[bt\_gatt\_scc](structbt__gatt__scc.md)

Server Characteristic Configuration Attribute Value.

**Definition** gatt.h:544

[bt\_gatt\_scc::flags](structbt__gatt__scc.md#aa7ddf1810f6d47e59c364b7489823d00)

uint16\_t flags

Server Characteristic Configuration flags, a bitmap of BT\_GATT\_SCC\_\* macros.

**Definition** gatt.h:546

[bt\_gatt\_service\_static](structbt__gatt__service__static.md)

Static GATT Service structure.

**Definition** gatt.h:319

[bt\_gatt\_service\_static::attrs](structbt__gatt__service__static.md#a38f9e02241fe37f68df5dd8782b59e9f)

const struct bt\_gatt\_attr \* attrs

Service Attributes.

**Definition** gatt.h:321

[bt\_gatt\_service\_static::attr\_count](structbt__gatt__service__static.md#a84c35a391e372396e2ec89eaf0d4d047)

size\_t attr\_count

Service Attribute count.

**Definition** gatt.h:323

[bt\_gatt\_service\_val](structbt__gatt__service__val.md)

Service Attribute Value.

**Definition** gatt.h:349

[bt\_gatt\_service\_val::uuid](structbt__gatt__service__val.md#a683e01db92400e76aed32b7a81369a55)

const struct bt\_uuid \* uuid

Service UUID.

**Definition** gatt.h:351

[bt\_gatt\_service\_val::end\_handle](structbt__gatt__service__val.md#a75b6fcf0f9f29ad05ccac0e83bcb31b7)

uint16\_t end\_handle

Handle of the last Attribute within the Service.

**Definition** gatt.h:353

[bt\_gatt\_service](structbt__gatt__service.md)

GATT Service structure.

**Definition** gatt.h:332

[bt\_gatt\_service::attrs](structbt__gatt__service.md#a0281e96ab54519df641f6c489fdc6b5b)

struct bt\_gatt\_attr \* attrs

Service Attributes.

**Definition** gatt.h:334

[bt\_gatt\_service::attr\_count](structbt__gatt__service.md#a87d8316a92ae04678d7be0ae76ed86cb)

size\_t attr\_count

Service Attribute count.

**Definition** gatt.h:336

[bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md)

GATT Subscribe parameters.

**Definition** gatt.h:2211

[bt\_gatt\_subscribe\_params::value](structbt__gatt__subscribe__params.md#a3bff1209b7a0b5908408a568622d0150)

uint16\_t value

Subscribe value.

**Definition** gatt.h:2230

[bt\_gatt\_subscribe\_params::min\_security](structbt__gatt__subscribe__params.md#a5b34bad1cf39bb3efd5faf516473dd4a)

bt\_security\_t min\_security

Minimum required security for received notification.

**Definition** gatt.h:2236

[bt\_gatt\_subscribe\_params::ccc\_handle](structbt__gatt__subscribe__params.md#a77c53cdfd4143483b33a8ecf6061561e)

uint16\_t ccc\_handle

Subscribe CCC handle.

**Definition** gatt.h:2222

[bt\_gatt\_subscribe\_params::subscribe](structbt__gatt__subscribe__params.md#a91595407b8de4e862652e41100668f0a)

bt\_gatt\_subscribe\_func\_t subscribe

Subscribe CCC write request response callback If given, called with the subscription parameters given...

**Definition** gatt.h:2217

[bt\_gatt\_subscribe\_params::value\_handle](structbt__gatt__subscribe__params.md#a9248418eb04a5b7a0faed5077c40bf22)

uint16\_t value\_handle

Subscribe value handle.

**Definition** gatt.h:2220

[bt\_gatt\_subscribe\_params::notify](structbt__gatt__subscribe__params.md#acf237ef097e8b847eb049fb0a5d4b759)

bt\_gatt\_notify\_func\_t notify

Notification value callback.

**Definition** gatt.h:2213

[bt\_gatt\_subscribe\_params::disc\_params](structbt__gatt__subscribe__params.md#ad3a3b9335b85777d65bdf875486e292a)

struct bt\_gatt\_discover\_params \* disc\_params

Discover parameters used when ccc\_handle = BT\_GATT\_AUTO\_DISCOVER\_CCC\_HANDLE.

**Definition** gatt.h:2227

[bt\_gatt\_subscribe\_params::chan\_opt](structbt__gatt__subscribe__params.md#ae139848da09705d37fe7c9de4c1a4087)

enum bt\_att\_chan\_opt chan\_opt

Att channel options.

**Definition** gatt.h:2248

[bt\_gatt\_subscribe\_params::flags](structbt__gatt__subscribe__params.md#aedd24024881e22372505355024cd716b)

atomic\_t flags[ATOMIC\_BITMAP\_SIZE(BT\_GATT\_SUBSCRIBE\_NUM\_FLAGS)]

Subscription flags, see bt\_gatt\_sub\_flag.

**Definition** gatt.h:2239

[bt\_gatt\_subscribe\_params::end\_handle](structbt__gatt__subscribe__params.md#af806d24aa97db1f2e9a021e719598a6d)

uint16\_t end\_handle

Subscribe End handle (for automatic discovery).

**Definition** gatt.h:2225

[bt\_gatt\_write\_params](structbt__gatt__write__params.md)

GATT Write parameters.

**Definition** gatt.h:2035

[bt\_gatt\_write\_params::func](structbt__gatt__write__params.md#a3468e3b75f3f9eda12bc4963f48cf9aa)

bt\_gatt\_write\_func\_t func

Response callback.

**Definition** gatt.h:2037

[bt\_gatt\_write\_params::handle](structbt__gatt__write__params.md#a384c5c15f248df5b327423ca32637bad)

uint16\_t handle

Attribute handle.

**Definition** gatt.h:2039

[bt\_gatt\_write\_params::data](structbt__gatt__write__params.md#ab6510ef242e73325adb074322746c27c)

const void \* data

Data to be written.

**Definition** gatt.h:2043

[bt\_gatt\_write\_params::chan\_opt](structbt__gatt__write__params.md#ad79905c16f7ba5289817de552ece1a48)

enum bt\_att\_chan\_opt chan\_opt

Att channel options.

**Definition** gatt.h:2048

[bt\_gatt\_write\_params::offset](structbt__gatt__write__params.md#add53cc08465d28f33bc48a1e8649ac1a)

uint16\_t offset

Attribute data offset.

**Definition** gatt.h:2041

[bt\_gatt\_write\_params::length](structbt__gatt__write__params.md#aded956dac2d398b642faeec81fdb9ec3)

uint16\_t length

Length of the data.

**Definition** gatt.h:2045

[bt\_uuid](structbt__uuid.md)

This is a 'tentative' type and should be used as a pointer only.

**Definition** uuid.h:50

[uuid](structuuid.md)

Binary representation of a UUID.

**Definition** uuid.h:48

[atomic.h](sys_2atomic_8h.md)

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[util.h](sys_2util_8h.md)

Misc utilities.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [gatt.h](gatt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

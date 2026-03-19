---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/modbus_8h_source.html
original_path: doxygen/html/modbus_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

modbus.h

[Go to the documentation of this file.](modbus_8h.md)

1/\*

2 \* Copyright (c) 2020 PHYTEC Messtechnik GmbH

3 \* Copyright (c) 2021 Nordic Semiconductor ASA

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8/\*

9 \* Client API in this file is based on mbm\_core.c from uC/Modbus Stack.

10 \*

11 \* uC/Modbus

12 \* The Embedded Modbus Stack

13 \*

14 \* Copyright 2003-2020 Silicon Laboratories Inc. www.silabs.com

15 \*

16 \* SPDX-License-Identifier: APACHE-2.0

17 \*

18 \* This software is subject to an open source license and is distributed by

19 \* Silicon Laboratories Inc. pursuant to the terms of the Apache License,

20 \* Version 2.0 available at www.apache.org/licenses/LICENSE-2.0.

21 \*/

22

29

30#ifndef ZEPHYR\_INCLUDE\_MODBUS\_H\_

31#define ZEPHYR\_INCLUDE\_MODBUS\_H\_

32

33#include <[zephyr/drivers/uart.h](drivers_2uart_8h.md)>

34#include <[zephyr/sys/slist.h](slist_8h.md)>

35#ifdef \_\_cplusplus

36extern "C" {

37#endif

38

[ 40](group__modbus.md#ga1015513d4d3b6621fc18dcfda79116a2)#define MODBUS\_MBAP\_LENGTH 7

[ 42](group__modbus.md#gae8a6fcfc117e7c4b2ac32aef90155698)#define MODBUS\_MBAP\_AND\_FC\_LENGTH (MODBUS\_MBAP\_LENGTH + 1)

43

[ 48](group__modbus.md#ga12557dda3e72ac45aefee3f9cbb18960)#define MODBUS\_EXC\_NONE 0

[ 50](group__modbus.md#ga934994f66a61c0d11d00dd52a748cc78)#define MODBUS\_EXC\_ILLEGAL\_FC 1

[ 52](group__modbus.md#ga9ab4fc4caaf2e051ae697d44a9fa98e3)#define MODBUS\_EXC\_ILLEGAL\_DATA\_ADDR 2

[ 54](group__modbus.md#ga5bcd9c7edd91d59af1453cde2376412f)#define MODBUS\_EXC\_ILLEGAL\_DATA\_VAL 3

[ 56](group__modbus.md#ga6bcf75ff2d522f1a542caa41b47a5ac8)#define MODBUS\_EXC\_SERVER\_DEVICE\_FAILURE 4

[ 58](group__modbus.md#ga9cfec884c72b7fc404d82c16f57e858d)#define MODBUS\_EXC\_ACK 5

[ 60](group__modbus.md#ga37f02ccee238e7c8ab33f150b2bcd793)#define MODBUS\_EXC\_SERVER\_DEVICE\_BUSY 6

[ 62](group__modbus.md#gad9b56cf73a31d77cd78d48695ea44659)#define MODBUS\_EXC\_MEM\_PARITY\_ERROR 8

[ 64](group__modbus.md#ga9903d7d283c11a4b8854ef5706b5aaba)#define MODBUS\_EXC\_GW\_PATH\_UNAVAILABLE 10

[ 66](group__modbus.md#gae61e3ee73e2288006f3dd2f081b4d1de)#define MODBUS\_EXC\_GW\_TARGET\_FAILED\_TO\_RESP 11

68

[ 72](structmodbus__adu.md)struct [modbus\_adu](structmodbus__adu.md) {

[ 74](structmodbus__adu.md#a04f0aa95985cc491649ba47f8ba064c8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [trans\_id](structmodbus__adu.md#a04f0aa95985cc491649ba47f8ba064c8);

[ 76](structmodbus__adu.md#ae0422aacfe323ce6ca83069a54315fa0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [proto\_id](structmodbus__adu.md#ae0422aacfe323ce6ca83069a54315fa0);

[ 78](structmodbus__adu.md#aa33f175677a0100c1f8a84a72c5ca247) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [length](structmodbus__adu.md#aa33f175677a0100c1f8a84a72c5ca247);

[ 80](structmodbus__adu.md#ab1fc3e76f3f406c8a0715055088d290d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [unit\_id](structmodbus__adu.md#ab1fc3e76f3f406c8a0715055088d290d);

[ 82](structmodbus__adu.md#a015e7b842349dc5567cc51cbf1f87420) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [fc](structmodbus__adu.md#a015e7b842349dc5567cc51cbf1f87420);

[ 84](structmodbus__adu.md#a7e94e4a0557717445ab2d791f8a97b7b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structmodbus__adu.md#a7e94e4a0557717445ab2d791f8a97b7b)[CONFIG\_MODBUS\_BUFFER\_SIZE - 4];

[ 86](structmodbus__adu.md#a78b8008e05c8d588d0ecba71e432d14e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [crc](structmodbus__adu.md#a78b8008e05c8d588d0ecba71e432d14e);

87};

88

[ 116](group__modbus.md#ga05b118dc87ebe3739cac4e9572104ffb)int [modbus\_read\_coils](group__modbus.md#ga05b118dc87ebe3739cac4e9572104ffb)(const int iface,

117 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id,

118 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_addr,

119 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const coil\_tbl,

120 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_coils);

121

[ 150](group__modbus.md#ga921fd6036ff1b8a416dc02e30bb6e653)int [modbus\_read\_dinputs](group__modbus.md#ga921fd6036ff1b8a416dc02e30bb6e653)(const int iface,

151 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id,

152 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_addr,

153 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const di\_tbl,

154 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_di);

155

[ 173](group__modbus.md#ga7d7221b32fbf2395e69e25ef2dbaa036)int [modbus\_read\_holding\_regs](group__modbus.md#ga7d7221b32fbf2395e69e25ef2dbaa036)(const int iface,

174 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id,

175 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_addr,

176 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*const reg\_buf,

177 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_regs);

178

[ 196](group__modbus.md#ga5ff31ca21cf2d1b081d172228d6c2154)int [modbus\_read\_input\_regs](group__modbus.md#ga5ff31ca21cf2d1b081d172228d6c2154)(const int iface,

197 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id,

198 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_addr,

199 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*const reg\_buf,

200 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_regs);

201

[ 214](group__modbus.md#gaccac4f72b5d66a5a2e6c444dda251c41)int [modbus\_write\_coil](group__modbus.md#gaccac4f72b5d66a5a2e6c444dda251c41)(const int iface,

215 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id,

216 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) coil\_addr,

217 const bool coil\_state);

218

[ 232](group__modbus.md#gaf06d2553af8b8e9ab58f54b8b7e2055b)int [modbus\_write\_holding\_reg](group__modbus.md#gaf06d2553af8b8e9ab58f54b8b7e2055b)(const int iface,

233 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id,

234 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_addr,

235 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_val);

236

[ 250](group__modbus.md#gac924251f66ca6f357d8b7d90075df210)int [modbus\_request\_diagnostic](group__modbus.md#gac924251f66ca6f357d8b7d90075df210)(const int iface,

251 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id,

252 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sfunc,

253 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data,

254 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*const data\_out);

255

[ 283](group__modbus.md#gac0fa22cd0d1fa861fdbc04b65ea60d7e)int [modbus\_write\_coils](group__modbus.md#gac0fa22cd0d1fa861fdbc04b65ea60d7e)(const int iface,

284 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id,

285 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_addr,

286 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const coil\_tbl,

287 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_coils);

288

[ 306](group__modbus.md#gadc8273292e0efc8c0d65c00eea7a22c5)int [modbus\_write\_holding\_regs](group__modbus.md#gadc8273292e0efc8c0d65c00eea7a22c5)(const int iface,

307 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id,

308 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_addr,

309 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*const reg\_buf,

310 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_regs);

311

[ 329](group__modbus.md#ga9a8ae6fb4b1aee398f5b19f074d07ea9)int [modbus\_read\_holding\_regs\_fp](group__modbus.md#ga9a8ae6fb4b1aee398f5b19f074d07ea9)(const int iface,

330 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id,

331 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_addr,

332 float \*const reg\_buf,

333 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_regs);

334

[ 352](group__modbus.md#ga762da245db3ca4f60fb3aa6c5783c73d)int [modbus\_write\_holding\_regs\_fp](group__modbus.md#ga762da245db3ca4f60fb3aa6c5783c73d)(const int iface,

353 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id,

354 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_addr,

355 float \*const reg\_buf,

356 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_regs);

357

[ 359](structmodbus__user__callbacks.md)struct [modbus\_user\_callbacks](structmodbus__user__callbacks.md) {

[ 361](structmodbus__user__callbacks.md#a3353b3aa0ec073fb9031a5c151e9995b) int (\*[coil\_rd](structmodbus__user__callbacks.md#a3353b3aa0ec073fb9031a5c151e9995b))([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, bool \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

362

[ 364](structmodbus__user__callbacks.md#a0dad31490d8b5d454f06a8b7805a09fd) int (\*[coil\_wr](structmodbus__user__callbacks.md#a0dad31490d8b5d454f06a8b7805a09fd))([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, bool [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

365

[ 367](structmodbus__user__callbacks.md#aa6fd8fc2663c6a982ec17a162ae56961) int (\*[discrete\_input\_rd](structmodbus__user__callbacks.md#aa6fd8fc2663c6a982ec17a162ae56961))([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, bool \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

368

[ 370](structmodbus__user__callbacks.md#a91a9270bd945935b74c6f5e021429d42) int (\*[input\_reg\_rd](structmodbus__user__callbacks.md#a91a9270bd945935b74c6f5e021429d42))([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*reg);

371

[ 373](structmodbus__user__callbacks.md#ae315e76c3ceefbd65ef8cea500b43df5) int (\*[input\_reg\_rd\_fp](structmodbus__user__callbacks.md#ae315e76c3ceefbd65ef8cea500b43df5))([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, float \*reg);

374

[ 376](structmodbus__user__callbacks.md#acf5fe90fab9765bd83d1ab2075d073a2) int (\*[holding\_reg\_rd](structmodbus__user__callbacks.md#acf5fe90fab9765bd83d1ab2075d073a2))([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*reg);

377

[ 379](structmodbus__user__callbacks.md#a4ca1ed4bfc93b36d939f847d7ac9f8da) int (\*[holding\_reg\_wr](structmodbus__user__callbacks.md#a4ca1ed4bfc93b36d939f847d7ac9f8da))([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg);

380

[ 382](structmodbus__user__callbacks.md#a821e0aacd7c90eff5e7c0047cc88a855) int (\*[holding\_reg\_rd\_fp](structmodbus__user__callbacks.md#a821e0aacd7c90eff5e7c0047cc88a855))([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, float \*reg);

383

[ 385](structmodbus__user__callbacks.md#a333b5781c35e781e7021f53d5a357482) int (\*[holding\_reg\_wr\_fp](structmodbus__user__callbacks.md#a333b5781c35e781e7021f53d5a357482))([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, float reg);

386};

387

[ 398](group__modbus.md#gaa17880a268d6b3b9553de835c800af27)int [modbus\_iface\_get\_by\_name](group__modbus.md#gaa17880a268d6b3b9553de835c800af27)(const char \*iface\_name);

399

[ 409](group__modbus.md#ga6d74be1fffb9d5697fe5708827aa7ef1)typedef int (\*[modbus\_raw\_cb\_t](group__modbus.md#ga6d74be1fffb9d5697fe5708827aa7ef1))(const int iface, const struct [modbus\_adu](structmodbus__adu.md) \*adu,

410 void \*user\_data);

411

[ 433](group__modbus.md#ga2a7ba41a2fb7f6bf5194c02dcab07ae3)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[modbus\_custom\_cb\_t](group__modbus.md#ga2a7ba41a2fb7f6bf5194c02dcab07ae3))(const int iface,

434 const struct [modbus\_adu](structmodbus__adu.md) \*const rx\_adu,

435 struct [modbus\_adu](structmodbus__adu.md) \*const tx\_adu,

436 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const excep\_code,

437 void \*const user\_data);

438

443struct modbus\_custom\_fc {

444 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

445 [modbus\_custom\_cb\_t](group__modbus.md#ga2a7ba41a2fb7f6bf5194c02dcab07ae3) cb;

446 void \*user\_data;

447 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) fc;

448 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) excep\_code;

449};

451

[ 455](group__modbus.md#gaa0acc60971d0f773719431173632fd30)#define MODBUS\_CUSTOM\_FC\_DEFINE(name, user\_cb, user\_fc, userdata) \

456 static struct modbus\_custom\_fc modbus\_cfg\_##name = { \

457 .cb = user\_cb, \

458 .user\_data = userdata, \

459 .fc = user\_fc, \

460 .excep\_code = MODBUS\_EXC\_NONE, \

461 }

462

[ 466](group__modbus.md#ga4bd8913e1c77a1e4b19585caa9f77c2e)enum [modbus\_mode](group__modbus.md#ga4bd8913e1c77a1e4b19585caa9f77c2e) {

[ 468](group__modbus.md#gga4bd8913e1c77a1e4b19585caa9f77c2ea52033dc2ef37fc286a590b1f97d946ef) [MODBUS\_MODE\_RTU](group__modbus.md#gga4bd8913e1c77a1e4b19585caa9f77c2ea52033dc2ef37fc286a590b1f97d946ef),

[ 470](group__modbus.md#gga4bd8913e1c77a1e4b19585caa9f77c2eafdf029741cc1bdecb2cb9baf4f06732a) [MODBUS\_MODE\_ASCII](group__modbus.md#gga4bd8913e1c77a1e4b19585caa9f77c2eafdf029741cc1bdecb2cb9baf4f06732a),

[ 472](group__modbus.md#gga4bd8913e1c77a1e4b19585caa9f77c2ea4d05b2cfd56ccf15eb1d8c7bb71071ec) [MODBUS\_MODE\_RAW](group__modbus.md#gga4bd8913e1c77a1e4b19585caa9f77c2ea4d05b2cfd56ccf15eb1d8c7bb71071ec),

473};

474

[ 478](structmodbus__serial__param.md)struct [modbus\_serial\_param](structmodbus__serial__param.md) {

[ 480](structmodbus__serial__param.md#af3989f5e20eb96080d456114ef4d86e5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [baud](structmodbus__serial__param.md#af3989f5e20eb96080d456114ef4d86e5);

[ 486](structmodbus__serial__param.md#a337a18f3ad923bf758cb432b9a2d8ada) enum [uart\_config\_parity](group__uart__interface.md#gab2ab6aacb6e3c43bb26d4274157e5711) [parity](structmodbus__serial__param.md#a337a18f3ad923bf758cb432b9a2d8ada);

[ 493](structmodbus__serial__param.md#a6f5819e3fbaf756f9150fdff431196c4) enum [uart\_config\_stop\_bits](group__uart__interface.md#gafc1aecb863e2456d73b78a49fcbad72e) [stop\_bits\_client](structmodbus__serial__param.md#a6f5819e3fbaf756f9150fdff431196c4);

494};

495

[ 499](structmodbus__server__param.md)struct [modbus\_server\_param](structmodbus__server__param.md) {

[ 501](structmodbus__server__param.md#ad8f72ea4e7dbbd81e23415e25b7d94be) struct [modbus\_user\_callbacks](structmodbus__user__callbacks.md) \*[user\_cb](structmodbus__server__param.md#ad8f72ea4e7dbbd81e23415e25b7d94be);

[ 503](structmodbus__server__param.md#a323a3a9be08f3c77df9f06b135f7f379) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [unit\_id](structmodbus__server__param.md#a323a3a9be08f3c77df9f06b135f7f379);

504};

505

[ 506](structmodbus__raw__cb.md)struct [modbus\_raw\_cb](structmodbus__raw__cb.md) {

[ 507](structmodbus__raw__cb.md#ab2904f52d7ec1e1a791380ddc334558d) [modbus\_raw\_cb\_t](group__modbus.md#ga6d74be1fffb9d5697fe5708827aa7ef1) [raw\_tx\_cb](structmodbus__raw__cb.md#ab2904f52d7ec1e1a791380ddc334558d);

[ 508](structmodbus__raw__cb.md#abfa01344b7fc37adb2a3b23d4cc9507f) void \*[user\_data](structmodbus__raw__cb.md#abfa01344b7fc37adb2a3b23d4cc9507f);

509};

510

[ 515](structmodbus__iface__param.md)struct [modbus\_iface\_param](structmodbus__iface__param.md) {

[ 517](structmodbus__iface__param.md#ae73f218d8810afb0c2efbf865ba8b3ba) enum [modbus\_mode](group__modbus.md#ga4bd8913e1c77a1e4b19585caa9f77c2e) [mode](structmodbus__iface__param.md#ae73f218d8810afb0c2efbf865ba8b3ba);

518 union {

[ 519](structmodbus__iface__param.md#a77d88f81d11b0f9338ca227930abf53d) struct [modbus\_server\_param](structmodbus__server__param.md) [server](structmodbus__iface__param.md#a77d88f81d11b0f9338ca227930abf53d);

[ 523](structmodbus__iface__param.md#a7726b39e43e660adb63e24b4cf2e7ab7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rx\_timeout](structmodbus__iface__param.md#a7726b39e43e660adb63e24b4cf2e7ab7);

524 };

525 union {

[ 527](structmodbus__iface__param.md#a77ff747b2e789e96691483994be1d596) struct [modbus\_serial\_param](structmodbus__serial__param.md) [serial](structmodbus__iface__param.md#a77ff747b2e789e96691483994be1d596);

[ 529](structmodbus__iface__param.md#a6e06fe6fc4ba31b25b5ef461ee0e4f81) struct [modbus\_raw\_cb](structmodbus__raw__cb.md) [rawcb](structmodbus__iface__param.md#a6e06fe6fc4ba31b25b5ef461ee0e4f81);

530 };

531};

532

[ 541](group__modbus.md#gae4d34276c467bf54e0849a1098e56f8b)int [modbus\_init\_server](group__modbus.md#gae4d34276c467bf54e0849a1098e56f8b)(const int iface, struct [modbus\_iface\_param](structmodbus__iface__param.md) param);

542

[ 551](group__modbus.md#ga943eff819ecf1bc268714783047888ef)int [modbus\_init\_client](group__modbus.md#ga943eff819ecf1bc268714783047888ef)(const int iface, struct [modbus\_iface\_param](structmodbus__iface__param.md) param);

552

[ 562](group__modbus.md#ga32a6319cc51eb5a98dcb58b3231b9d34)int [modbus\_disable](group__modbus.md#ga32a6319cc51eb5a98dcb58b3231b9d34)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) iface);

563

[ 572](group__modbus.md#ga6d40e9eda6b8ead6d071d4192ffe489b)int [modbus\_raw\_submit\_rx](group__modbus.md#ga6d40e9eda6b8ead6d071d4192ffe489b)(const int iface, const struct [modbus\_adu](structmodbus__adu.md) \*adu);

573

[ 581](group__modbus.md#ga8fdae6a92e27a845296c9d8ce4b8078e)void [modbus\_raw\_put\_header](group__modbus.md#ga8fdae6a92e27a845296c9d8ce4b8078e)(const struct [modbus\_adu](structmodbus__adu.md) \*adu, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*header);

582

[ 589](group__modbus.md#ga333072d3536d7b6f0680ceecc2c5bddf)void [modbus\_raw\_get\_header](group__modbus.md#ga333072d3536d7b6f0680ceecc2c5bddf)(struct [modbus\_adu](structmodbus__adu.md) \*adu, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*header);

590

[ 598](group__modbus.md#gad250c40ba13a7d8c9189de17d1fd31aa)void [modbus\_raw\_set\_server\_failure](group__modbus.md#gad250c40ba13a7d8c9189de17d1fd31aa)(struct [modbus\_adu](structmodbus__adu.md) \*adu);

599

[ 612](group__modbus.md#ga7aa5dfd6e457980e9e9b8a77810ec31e)int [modbus\_raw\_backend\_txn](group__modbus.md#ga7aa5dfd6e457980e9e9b8a77810ec31e)(const int iface, struct [modbus\_adu](structmodbus__adu.md) \*adu);

613

[ 630](group__modbus.md#gacd88a4f35a13cc6864654927296803c4)int [modbus\_register\_user\_fc](group__modbus.md#gacd88a4f35a13cc6864654927296803c4)(const int iface, struct modbus\_custom\_fc \*custom\_fc);

631

632#ifdef \_\_cplusplus

633}

634#endif

635

639

640#endif /\* ZEPHYR\_INCLUDE\_MODBUS\_H\_ \*/

[uart.h](drivers_2uart_8h.md)

Public APIs for UART drivers.

[modbus\_read\_coils](group__modbus.md#ga05b118dc87ebe3739cac4e9572104ffb)

int modbus\_read\_coils(const int iface, const uint8\_t unit\_id, const uint16\_t start\_addr, uint8\_t \*const coil\_tbl, const uint16\_t num\_coils)

Coil read (FC01).

[modbus\_custom\_cb\_t](group__modbus.md#ga2a7ba41a2fb7f6bf5194c02dcab07ae3)

bool(\* modbus\_custom\_cb\_t)(const int iface, const struct modbus\_adu \*const rx\_adu, struct modbus\_adu \*const tx\_adu, uint8\_t \*const excep\_code, void \*const user\_data)

Custom function code handler function signature.

**Definition** modbus.h:433

[modbus\_disable](group__modbus.md#ga32a6319cc51eb5a98dcb58b3231b9d34)

int modbus\_disable(const uint8\_t iface)

Disable Modbus Interface.

[modbus\_raw\_get\_header](group__modbus.md#ga333072d3536d7b6f0680ceecc2c5bddf)

void modbus\_raw\_get\_header(struct modbus\_adu \*adu, const uint8\_t \*header)

Get MBAP header from a buffer.

[modbus\_mode](group__modbus.md#ga4bd8913e1c77a1e4b19585caa9f77c2e)

modbus\_mode

Modbus interface mode.

**Definition** modbus.h:466

[modbus\_read\_input\_regs](group__modbus.md#ga5ff31ca21cf2d1b081d172228d6c2154)

int modbus\_read\_input\_regs(const int iface, const uint8\_t unit\_id, const uint16\_t start\_addr, uint16\_t \*const reg\_buf, const uint16\_t num\_regs)

Read input registers (FC04).

[modbus\_raw\_submit\_rx](group__modbus.md#ga6d40e9eda6b8ead6d071d4192ffe489b)

int modbus\_raw\_submit\_rx(const int iface, const struct modbus\_adu \*adu)

Submit raw ADU.

[modbus\_raw\_cb\_t](group__modbus.md#ga6d74be1fffb9d5697fe5708827aa7ef1)

int(\* modbus\_raw\_cb\_t)(const int iface, const struct modbus\_adu \*adu, void \*user\_data)

ADU raw callback function signature.

**Definition** modbus.h:409

[modbus\_write\_holding\_regs\_fp](group__modbus.md#ga762da245db3ca4f60fb3aa6c5783c73d)

int modbus\_write\_holding\_regs\_fp(const int iface, const uint8\_t unit\_id, const uint16\_t start\_addr, float \*const reg\_buf, const uint16\_t num\_regs)

Write floating-point holding registers (FC16).

[modbus\_raw\_backend\_txn](group__modbus.md#ga7aa5dfd6e457980e9e9b8a77810ec31e)

int modbus\_raw\_backend\_txn(const int iface, struct modbus\_adu \*adu)

Use interface as backend to send and receive ADU.

[modbus\_read\_holding\_regs](group__modbus.md#ga7d7221b32fbf2395e69e25ef2dbaa036)

int modbus\_read\_holding\_regs(const int iface, const uint8\_t unit\_id, const uint16\_t start\_addr, uint16\_t \*const reg\_buf, const uint16\_t num\_regs)

Read holding registers (FC03).

[modbus\_raw\_put\_header](group__modbus.md#ga8fdae6a92e27a845296c9d8ce4b8078e)

void modbus\_raw\_put\_header(const struct modbus\_adu \*adu, uint8\_t \*header)

Put MBAP header into a buffer.

[modbus\_read\_dinputs](group__modbus.md#ga921fd6036ff1b8a416dc02e30bb6e653)

int modbus\_read\_dinputs(const int iface, const uint8\_t unit\_id, const uint16\_t start\_addr, uint8\_t \*const di\_tbl, const uint16\_t num\_di)

Read discrete inputs (FC02).

[modbus\_init\_client](group__modbus.md#ga943eff819ecf1bc268714783047888ef)

int modbus\_init\_client(const int iface, struct modbus\_iface\_param param)

Configure Modbus Interface as raw ADU client.

[modbus\_read\_holding\_regs\_fp](group__modbus.md#ga9a8ae6fb4b1aee398f5b19f074d07ea9)

int modbus\_read\_holding\_regs\_fp(const int iface, const uint8\_t unit\_id, const uint16\_t start\_addr, float \*const reg\_buf, const uint16\_t num\_regs)

Read floating-point holding registers (FC03).

[modbus\_iface\_get\_by\_name](group__modbus.md#gaa17880a268d6b3b9553de835c800af27)

int modbus\_iface\_get\_by\_name(const char \*iface\_name)

Get Modbus interface index according to interface name.

[modbus\_write\_coils](group__modbus.md#gac0fa22cd0d1fa861fdbc04b65ea60d7e)

int modbus\_write\_coils(const int iface, const uint8\_t unit\_id, const uint16\_t start\_addr, uint8\_t \*const coil\_tbl, const uint16\_t num\_coils)

Write coils (FC15).

[modbus\_request\_diagnostic](group__modbus.md#gac924251f66ca6f357d8b7d90075df210)

int modbus\_request\_diagnostic(const int iface, const uint8\_t unit\_id, const uint16\_t sfunc, const uint16\_t data, uint16\_t \*const data\_out)

Read diagnostic (FC08).

[modbus\_write\_coil](group__modbus.md#gaccac4f72b5d66a5a2e6c444dda251c41)

int modbus\_write\_coil(const int iface, const uint8\_t unit\_id, const uint16\_t coil\_addr, const bool coil\_state)

Write single coil (FC05).

[modbus\_register\_user\_fc](group__modbus.md#gacd88a4f35a13cc6864654927296803c4)

int modbus\_register\_user\_fc(const int iface, struct modbus\_custom\_fc \*custom\_fc)

Register a user-defined function code handler.

[modbus\_raw\_set\_server\_failure](group__modbus.md#gad250c40ba13a7d8c9189de17d1fd31aa)

void modbus\_raw\_set\_server\_failure(struct modbus\_adu \*adu)

Set Server Device Failure exception.

[modbus\_write\_holding\_regs](group__modbus.md#gadc8273292e0efc8c0d65c00eea7a22c5)

int modbus\_write\_holding\_regs(const int iface, const uint8\_t unit\_id, const uint16\_t start\_addr, uint16\_t \*const reg\_buf, const uint16\_t num\_regs)

Write holding registers (FC16).

[modbus\_init\_server](group__modbus.md#gae4d34276c467bf54e0849a1098e56f8b)

int modbus\_init\_server(const int iface, struct modbus\_iface\_param param)

Configure Modbus Interface as raw ADU server.

[modbus\_write\_holding\_reg](group__modbus.md#gaf06d2553af8b8e9ab58f54b8b7e2055b)

int modbus\_write\_holding\_reg(const int iface, const uint8\_t unit\_id, const uint16\_t start\_addr, const uint16\_t reg\_val)

Write single holding register (FC06).

[MODBUS\_MODE\_RAW](group__modbus.md#gga4bd8913e1c77a1e4b19585caa9f77c2ea4d05b2cfd56ccf15eb1d8c7bb71071ec)

@ MODBUS\_MODE\_RAW

Modbus raw ADU mode.

**Definition** modbus.h:472

[MODBUS\_MODE\_RTU](group__modbus.md#gga4bd8913e1c77a1e4b19585caa9f77c2ea52033dc2ef37fc286a590b1f97d946ef)

@ MODBUS\_MODE\_RTU

Modbus over serial line RTU mode.

**Definition** modbus.h:468

[MODBUS\_MODE\_ASCII](group__modbus.md#gga4bd8913e1c77a1e4b19585caa9f77c2eafdf029741cc1bdecb2cb9baf4f06732a)

@ MODBUS\_MODE\_ASCII

Modbus over serial line ASCII mode.

**Definition** modbus.h:470

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[uart\_config\_parity](group__uart__interface.md#gab2ab6aacb6e3c43bb26d4274157e5711)

uart\_config\_parity

Parity modes.

**Definition** uart.h:78

[uart\_config\_stop\_bits](group__uart__interface.md#gafc1aecb863e2456d73b78a49fcbad72e)

uart\_config\_stop\_bits

Number of stop bits.

**Definition** uart.h:87

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[slist.h](slist_8h.md)

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[modbus\_adu](structmodbus__adu.md)

Frame struct used internally and for raw ADU support.

**Definition** modbus.h:72

[modbus\_adu::fc](structmodbus__adu.md#a015e7b842349dc5567cc51cbf1f87420)

uint8\_t fc

Function Code.

**Definition** modbus.h:82

[modbus\_adu::trans\_id](structmodbus__adu.md#a04f0aa95985cc491649ba47f8ba064c8)

uint16\_t trans\_id

Transaction Identifier.

**Definition** modbus.h:74

[modbus\_adu::crc](structmodbus__adu.md#a78b8008e05c8d588d0ecba71e432d14e)

uint16\_t crc

RTU CRC.

**Definition** modbus.h:86

[modbus\_adu::data](structmodbus__adu.md#a7e94e4a0557717445ab2d791f8a97b7b)

uint8\_t data[CONFIG\_MODBUS\_BUFFER\_SIZE - 4]

Transaction Data.

**Definition** modbus.h:84

[modbus\_adu::length](structmodbus__adu.md#aa33f175677a0100c1f8a84a72c5ca247)

uint16\_t length

Length of the data only (not the length of unit ID + PDU).

**Definition** modbus.h:78

[modbus\_adu::unit\_id](structmodbus__adu.md#ab1fc3e76f3f406c8a0715055088d290d)

uint8\_t unit\_id

Unit Identifier.

**Definition** modbus.h:80

[modbus\_adu::proto\_id](structmodbus__adu.md#ae0422aacfe323ce6ca83069a54315fa0)

uint16\_t proto\_id

Protocol Identifier.

**Definition** modbus.h:76

[modbus\_iface\_param](structmodbus__iface__param.md)

User parameter structure to configure Modbus interface as client or server.

**Definition** modbus.h:515

[modbus\_iface\_param::rawcb](structmodbus__iface__param.md#a6e06fe6fc4ba31b25b5ef461ee0e4f81)

struct modbus\_raw\_cb rawcb

Pointer to raw ADU callback function.

**Definition** modbus.h:529

[modbus\_iface\_param::rx\_timeout](structmodbus__iface__param.md#a7726b39e43e660adb63e24b4cf2e7ab7)

uint32\_t rx\_timeout

Amount of time client will wait for a response from the server.

**Definition** modbus.h:523

[modbus\_iface\_param::server](structmodbus__iface__param.md#a77d88f81d11b0f9338ca227930abf53d)

struct modbus\_server\_param server

**Definition** modbus.h:519

[modbus\_iface\_param::serial](structmodbus__iface__param.md#a77ff747b2e789e96691483994be1d596)

struct modbus\_serial\_param serial

Serial support parameter of the interface.

**Definition** modbus.h:527

[modbus\_iface\_param::mode](structmodbus__iface__param.md#ae73f218d8810afb0c2efbf865ba8b3ba)

enum modbus\_mode mode

Mode of the interface.

**Definition** modbus.h:517

[modbus\_raw\_cb](structmodbus__raw__cb.md)

**Definition** modbus.h:506

[modbus\_raw\_cb::raw\_tx\_cb](structmodbus__raw__cb.md#ab2904f52d7ec1e1a791380ddc334558d)

modbus\_raw\_cb\_t raw\_tx\_cb

**Definition** modbus.h:507

[modbus\_raw\_cb::user\_data](structmodbus__raw__cb.md#abfa01344b7fc37adb2a3b23d4cc9507f)

void \* user\_data

**Definition** modbus.h:508

[modbus\_serial\_param](structmodbus__serial__param.md)

Modbus serial line parameter.

**Definition** modbus.h:478

[modbus\_serial\_param::parity](structmodbus__serial__param.md#a337a18f3ad923bf758cb432b9a2d8ada)

enum uart\_config\_parity parity

parity UART's parity setting: UART\_CFG\_PARITY\_NONE, UART\_CFG\_PARITY\_EVEN, UART\_CFG\_PARITY\_ODD

**Definition** modbus.h:486

[modbus\_serial\_param::stop\_bits\_client](structmodbus__serial__param.md#a6f5819e3fbaf756f9150fdff431196c4)

enum uart\_config\_stop\_bits stop\_bits\_client

stop\_bits\_client UART's stop bits setting if in client mode: UART\_CFG\_STOP\_BITS\_0\_5,...

**Definition** modbus.h:493

[modbus\_serial\_param::baud](structmodbus__serial__param.md#af3989f5e20eb96080d456114ef4d86e5)

uint32\_t baud

Baudrate of the serial line.

**Definition** modbus.h:480

[modbus\_server\_param](structmodbus__server__param.md)

Modbus server parameter.

**Definition** modbus.h:499

[modbus\_server\_param::unit\_id](structmodbus__server__param.md#a323a3a9be08f3c77df9f06b135f7f379)

uint8\_t unit\_id

Modbus unit ID of the server.

**Definition** modbus.h:503

[modbus\_server\_param::user\_cb](structmodbus__server__param.md#ad8f72ea4e7dbbd81e23415e25b7d94be)

struct modbus\_user\_callbacks \* user\_cb

Pointer to the User Callback structure.

**Definition** modbus.h:501

[modbus\_user\_callbacks](structmodbus__user__callbacks.md)

Modbus Server User Callback structure.

**Definition** modbus.h:359

[modbus\_user\_callbacks::coil\_wr](structmodbus__user__callbacks.md#a0dad31490d8b5d454f06a8b7805a09fd)

int(\* coil\_wr)(uint16\_t addr, bool state)

Coil write callback.

**Definition** modbus.h:364

[modbus\_user\_callbacks::holding\_reg\_wr\_fp](structmodbus__user__callbacks.md#a333b5781c35e781e7021f53d5a357482)

int(\* holding\_reg\_wr\_fp)(uint16\_t addr, float reg)

Floating Point Holding Register write callback.

**Definition** modbus.h:385

[modbus\_user\_callbacks::coil\_rd](structmodbus__user__callbacks.md#a3353b3aa0ec073fb9031a5c151e9995b)

int(\* coil\_rd)(uint16\_t addr, bool \*state)

Coil read callback.

**Definition** modbus.h:361

[modbus\_user\_callbacks::holding\_reg\_wr](structmodbus__user__callbacks.md#a4ca1ed4bfc93b36d939f847d7ac9f8da)

int(\* holding\_reg\_wr)(uint16\_t addr, uint16\_t reg)

Holding Register write callback.

**Definition** modbus.h:379

[modbus\_user\_callbacks::holding\_reg\_rd\_fp](structmodbus__user__callbacks.md#a821e0aacd7c90eff5e7c0047cc88a855)

int(\* holding\_reg\_rd\_fp)(uint16\_t addr, float \*reg)

Floating Point Holding Register read callback.

**Definition** modbus.h:382

[modbus\_user\_callbacks::input\_reg\_rd](structmodbus__user__callbacks.md#a91a9270bd945935b74c6f5e021429d42)

int(\* input\_reg\_rd)(uint16\_t addr, uint16\_t \*reg)

Input Register read callback.

**Definition** modbus.h:370

[modbus\_user\_callbacks::discrete\_input\_rd](structmodbus__user__callbacks.md#aa6fd8fc2663c6a982ec17a162ae56961)

int(\* discrete\_input\_rd)(uint16\_t addr, bool \*state)

Discrete Input read callback.

**Definition** modbus.h:367

[modbus\_user\_callbacks::holding\_reg\_rd](structmodbus__user__callbacks.md#acf5fe90fab9765bd83d1ab2075d073a2)

int(\* holding\_reg\_rd)(uint16\_t addr, uint16\_t \*reg)

Holding Register read callback.

**Definition** modbus.h:376

[modbus\_user\_callbacks::input\_reg\_rd\_fp](structmodbus__user__callbacks.md#ae315e76c3ceefbd65ef8cea500b43df5)

int(\* input\_reg\_rd\_fp)(uint16\_t addr, float \*reg)

Floating Point Input Register read callback.

**Definition** modbus.h:373

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modbus](dir_4256a22177f338086a49d2e4cf070454.md)
- [modbus.h](modbus_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
